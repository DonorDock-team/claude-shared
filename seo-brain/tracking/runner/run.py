#!/usr/bin/env python3
"""
DonorDock AEO Citation Runner

Runs the prompt bank against 4 AI engines (Claude, GPT-4o, Perplexity, Gemini),
detects DonorDock + competitor mentions, stores per-prompt-per-engine JSON results,
and writes a run summary report.

Usage:
    python3 run.py --priority top-50    # ~50 prompts × 4 engines (Thu drift)
    python3 run.py --priority full      # ~150 prompts × 4 engines (Mon comprehensive)
    python3 run.py --priority aio       # AIO subset only (Sat — but uses Chrome MCP, not API)
    python3 run.py --dry-run            # Validate config + prompt bank, no API calls
    python3 run.py --engines claude,openai  # Run only specific engines

Environment:
    Reads API keys from 1Password via `op` CLI. Required items:
      - "Claude API Key"
      - "OpenAI API Credentials - DonorDock"
      - "Perplexity - DonorDock API Credentials"
      - "Google AI API key (Yarn)"

    `op signin` must be active in the shell before running.

Output:
    seo-brain/tracking/ai-citations/{YYYY-MM-DD}/{engine}/{prompt-id}.json
    seo-brain/tracking/ai-citations/{YYYY-MM-DD}/_summary.json
    seo-brain/tracking/ai-citations/{YYYY-MM-DD}/_report.md
"""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    import httpx
except ImportError:
    print("Missing dep: httpx. Install with: pip install httpx", file=sys.stderr)
    sys.exit(1)

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
RUNNER_DIR = Path(__file__).parent.resolve()
TRACKING_DIR = RUNNER_DIR.parent
PROMPTS_PATH = TRACKING_DIR / "prompts.json"
RESULTS_ROOT = TRACKING_DIR / "ai-citations"


def redact_secrets(s: str) -> str:
    """Strip API keys from any string before it is persisted or committed.

    Error messages from httpx include the full request URL, and the Gemini
    endpoint carries the API key as a ``?key=`` query param, so a raw error
    string can leak a live key into the public repo. Scrub it here.
    """
    import re
    if not s:
        return s
    # key/token query params, e.g. ...generateContent?key=AIza...
    s = re.sub(r'([?&](?:key|api_key|apikey|access_token|token)=)[^&\s\'"]+',
               r'\1REDACTED', s, flags=re.IGNORECASE)
    # bare provider key tokens (defensive)
    s = re.sub(r'AIzaSy[A-Za-z0-9_\-]{20,}', 'REDACTED', s)   # Google
    s = re.sub(r'sk-[A-Za-z0-9_\-]{20,}', 'REDACTED', s)      # OpenAI / Anthropic
    s = re.sub(r'pplx-[A-Za-z0-9_\-]{20,}', 'REDACTED', s)    # Perplexity
    return s

# ---------------------------------------------------------------------------
# Key sources (in priority order)
#
# 1. Environment variables (preferred for scheduled runs — no GUI prompts)
# 2. ~/.config/donordock/seo.env file (shell-style env file, auto-loaded)
# 3. 1Password CLI (fallback, requires desktop app unlock + may prompt)
#
# Set up the env file once with:
#   mkdir -p ~/.config/donordock
#   chmod 700 ~/.config/donordock
#   touch ~/.config/donordock/seo.env
#   chmod 600 ~/.config/donordock/seo.env
#   # then add ANTHROPIC_API_KEY=... etc. (one per line)
# ---------------------------------------------------------------------------
ENV_KEY_MAP = {
    "anthropic":   "ANTHROPIC_API_KEY",
    "openai":      "OPENAI_API_KEY",
    "perplexity":  "PERPLEXITY_API_KEY",
    "gemini":      "GEMINI_API_KEY",
}

OP_LABELS = {
    "anthropic":   "Claude API Key",
    "openai":      "OpenAI API Credentials - DonorDock",
    "perplexity":  "Perplexity - DonorDock API Credentials",
    "gemini":      "Google AI API key (Yarn)",
}

ENV_FILE = Path.home() / ".config" / "donordock" / "seo.env"


def load_env_file() -> None:
    """Load KEY=value lines from ~/.config/donordock/seo.env into os.environ.

    File values fill any env var that is unset OR empty. A non-empty existing
    env var keeps priority (explicit env beats file) — this lets you do
    `ANTHROPIC_API_KEY=foo python3 run.py` to override a single key without
    editing the file.
    """
    if not ENV_FILE.exists():
        return
    try:
        for raw in ENV_FILE.read_text().splitlines():
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            if "=" not in line:
                continue
            k, v = line.split("=", 1)
            k = k.strip()
            v = v.strip().strip('"').strip("'")
            # Only fill if existing env var is unset or empty
            if v and not os.environ.get(k):
                os.environ[k] = v
    except Exception as e:
        print(f"[warn] failed to read {ENV_FILE}: {e}", file=sys.stderr)


def get_key(engine: str) -> str:
    """Return the API key for `engine`. Tries env vars first, then 1Password."""
    env_var = ENV_KEY_MAP.get(engine)
    if env_var and os.environ.get(env_var):
        return os.environ[env_var].strip()
    return op_get(OP_LABELS[engine])

# ---------------------------------------------------------------------------
# Pricing (per-million-tokens). Rough; update as providers change pricing.
# Used for cost estimation only — not for billing.
# ---------------------------------------------------------------------------
PRICING = {
    "anthropic":  {"in": 3.00,  "out": 15.00},   # Claude Sonnet 4
    "openai":     {"in": 2.50,  "out": 10.00},   # GPT-4o
    "perplexity": {"in": 3.00,  "out": 15.00, "request_fee": 0.005},  # Sonar Pro
    "gemini":     {"in": 0.30,  "out": 2.50},    # Gemini 2.5 Flash
}

# ---------------------------------------------------------------------------
# DonorDock + competitor detection patterns
# ---------------------------------------------------------------------------
DONORDOCK_PATTERN = re.compile(r"\b(donor[\s-]?dock|donordock\.com)\b", re.IGNORECASE)
URL_PATTERN = re.compile(r"https?://[^\s\)\]\}<>]+", re.IGNORECASE)


def load_prompts() -> dict[str, Any]:
    if not PROMPTS_PATH.exists():
        raise SystemExit(f"prompts.json not found at {PROMPTS_PATH}")
    with PROMPTS_PATH.open() as f:
        return json.load(f)


def op_get(label: str) -> str:
    """Fetch the secret value of a 1Password item.

    Tries common field names in order, then falls back to scanning all CONCEALED
    fields on the item. Works with API Credential items, Login items, and
    Secure Notes with custom credential fields.
    """
    # Try common field name conventions in order
    for field in ("credential", "password", "api key", "API Key", "key", "token"):
        try:
            result = subprocess.run(
                ["op", "item", "get", label, "--field", field, "--reveal"],
                capture_output=True, text=True, check=True,
            )
            val = result.stdout.strip()
            if val:
                return val
        except subprocess.CalledProcessError:
            continue

    # Last-resort fallback: parse JSON, return first CONCEALED field that has a value
    try:
        result = subprocess.run(
            ["op", "item", "get", label, "--format=json"],
            capture_output=True, text=True, check=True,
        )
        data = json.loads(result.stdout)
        for f in data.get("fields", []):
            if f.get("type") == "CONCEALED" and f.get("value"):
                return f["value"].strip()
    except (subprocess.CalledProcessError, json.JSONDecodeError):
        pass

    raise SystemExit(
        f"Failed to read 1Password item '{label}'. "
        f"Tried field names: credential, password, api key, key, token, plus all CONCEALED fields. "
        f"Make sure the 1Password desktop app is unlocked and the item exists with a credential value."
    )


def detect_donordock(text: str) -> bool:
    return bool(DONORDOCK_PATTERN.search(text))


def detect_competitors(text: str, competitor_list: list[str]) -> list[str]:
    found = []
    for c in competitor_list:
        if re.search(r"\b" + re.escape(c) + r"\b", text, re.IGNORECASE):
            found.append(c)
    return sorted(set(found))


def extract_urls(text: str) -> list[str]:
    return list({m.group(0).rstrip(".,;:") for m in URL_PATTERN.finditer(text)})


def donordock_position(text: str) -> int | None:
    """Character offset of first DonorDock mention (lower = better/earlier)."""
    m = DONORDOCK_PATTERN.search(text)
    return m.start() if m else None


# ---------------------------------------------------------------------------
# Engine adapters — each takes a prompt + key, returns (response_text, in_tokens, out_tokens, raw_meta)
# ---------------------------------------------------------------------------

async def call_anthropic(client: httpx.AsyncClient, prompt: str, key: str) -> tuple[str, int, int, dict]:
    r = await client.post(
        "https://api.anthropic.com/v1/messages",
        headers={
            "x-api-key": key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
        json={
            "model": "claude-sonnet-4-5",
            "max_tokens": 2048,
            "messages": [{"role": "user", "content": prompt}],
        },
        timeout=60.0,
    )
    r.raise_for_status()
    data = r.json()
    text = "".join(block.get("text", "") for block in data.get("content", []))
    usage = data.get("usage", {})
    return text, usage.get("input_tokens", 0), usage.get("output_tokens", 0), {"model": data.get("model")}


async def call_openai(client: httpx.AsyncClient, prompt: str, key: str) -> tuple[str, int, int, dict]:
    r = await client.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {key}",
            "content-type": "application/json",
        },
        json={
            "model": "gpt-4o",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 2048,
        },
        timeout=60.0,
    )
    r.raise_for_status()
    data = r.json()
    text = data["choices"][0]["message"]["content"]
    usage = data.get("usage", {})
    return text, usage.get("prompt_tokens", 0), usage.get("completion_tokens", 0), {"model": data.get("model")}


async def call_perplexity(client: httpx.AsyncClient, prompt: str, key: str) -> tuple[str, int, int, dict]:
    r = await client.post(
        "https://api.perplexity.ai/chat/completions",
        headers={
            "Authorization": f"Bearer {key}",
            "content-type": "application/json",
        },
        json={
            "model": "sonar-pro",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 2048,
            "return_citations": True,
        },
        timeout=120.0,
    )
    r.raise_for_status()
    data = r.json()
    text = data["choices"][0]["message"]["content"]
    usage = data.get("usage", {})
    citations = data.get("citations", []) or []
    return text, usage.get("prompt_tokens", 0), usage.get("completion_tokens", 0), {
        "model": data.get("model"),
        "perplexity_citations": citations,
    }


GEMINI_MODEL = "gemini-2.5-flash"


async def call_gemini(client: httpx.AsyncClient, prompt: str, key: str) -> tuple[str, int, int, dict]:
    r = await client.post(
        f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent?key={key}",
        headers={"content-type": "application/json"},
        json={
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {"maxOutputTokens": 2048},
        },
        timeout=60.0,
    )
    r.raise_for_status()
    data = r.json()
    candidates = data.get("candidates", [])
    if not candidates:
        return "", 0, 0, {"warning": "no candidates in Gemini response", "model": GEMINI_MODEL}
    parts = candidates[0].get("content", {}).get("parts", [])
    text = "".join(p.get("text", "") for p in parts)
    usage = data.get("usageMetadata", {})
    return text, usage.get("promptTokenCount", 0), usage.get("candidatesTokenCount", 0), {"model": GEMINI_MODEL}


ENGINES = {
    "anthropic":  call_anthropic,
    "openai":     call_openai,
    "perplexity": call_perplexity,
    "gemini":     call_gemini,
}


# ---------------------------------------------------------------------------
# Per-prompt orchestration
# ---------------------------------------------------------------------------

@dataclass
class PromptResult:
    prompt_id: str
    prompt_text: str
    engine: str
    timestamp: str
    success: bool
    error: str | None
    response_text: str
    donordock_mentioned: bool
    donordock_position: int | None
    competitors_mentioned: list[str]
    urls_cited: list[str]
    input_tokens: int
    output_tokens: int
    estimated_cost_usd: float
    meta: dict


def estimate_cost(engine: str, in_tokens: int, out_tokens: int) -> float:
    p = PRICING[engine]
    cost = (in_tokens * p["in"] + out_tokens * p["out"]) / 1_000_000
    if "request_fee" in p:
        cost += p["request_fee"]
    return round(cost, 6)


async def run_one(client: httpx.AsyncClient, prompt: dict, engine: str, key: str, competitors: list[str], sem: asyncio.Semaphore) -> PromptResult:
    pid = prompt["id"]
    text = prompt["text"]
    ts = datetime.now(timezone.utc).isoformat()
    async with sem:
        try:
            response, in_tok, out_tok, meta = await ENGINES[engine](client, text, key)
            return PromptResult(
                prompt_id=pid,
                prompt_text=text,
                engine=engine,
                timestamp=ts,
                success=True,
                error=None,
                response_text=response,
                donordock_mentioned=detect_donordock(response),
                donordock_position=donordock_position(response),
                competitors_mentioned=detect_competitors(response, competitors),
                urls_cited=extract_urls(response),
                input_tokens=in_tok,
                output_tokens=out_tok,
                estimated_cost_usd=estimate_cost(engine, in_tok, out_tok),
                meta=meta,
            )
        except Exception as e:
            return PromptResult(
                prompt_id=pid,
                prompt_text=text,
                engine=engine,
                timestamp=ts,
                success=False,
                error=redact_secrets(f"{type(e).__name__}: {e}"),
                response_text="",
                donordock_mentioned=False,
                donordock_position=None,
                competitors_mentioned=[],
                urls_cited=[],
                input_tokens=0,
                output_tokens=0,
                estimated_cost_usd=0.0,
                meta={},
            )


def filter_prompts(prompts: list[dict], priority: str) -> list[dict]:
    active = [p for p in prompts if p.get("active", True)]
    if priority == "full":
        return active
    if priority == "top-50":
        return [p for p in active if p.get("priority") == "top-50"]
    if priority == "aio":
        return [p for p in active if p.get("aio", False)]
    raise SystemExit(f"unknown priority filter: {priority}")


# ---------------------------------------------------------------------------
# Main runner
# ---------------------------------------------------------------------------

async def main_async(args) -> int:
    config = load_prompts()
    competitors = config["competitors_to_track"]
    all_prompts = config["prompts"]
    selected = filter_prompts(all_prompts, args.priority)

    requested_engines = args.engines.split(",") if args.engines else list(ENGINES.keys())
    for e in requested_engines:
        if e not in ENGINES:
            raise SystemExit(f"unknown engine: {e}")

    print(f"[run] priority={args.priority}  engines={requested_engines}  prompts={len(selected)}")

    if args.dry_run:
        print(f"[dry-run] would run {len(selected)} prompts × {len(requested_engines)} engines = {len(selected)*len(requested_engines)} API calls")
        return 0

    # Load keys — env file first, then env vars, then 1Password
    load_env_file()
    keys = {}
    for engine in requested_engines:
        env_var = ENV_KEY_MAP.get(engine)
        if env_var and os.environ.get(env_var):
            print(f"[keys] {engine}: env var {env_var}")
            keys[engine] = os.environ[env_var].strip()
        else:
            label = OP_LABELS[engine]
            print(f"[keys] {engine}: 1Password '{label}' (env var {env_var} not set)")
            keys[engine] = op_get(label)
    print(f"[keys] all keys loaded.")

    # Output dir
    today = datetime.now(timezone.utc).date().isoformat()
    run_dir = RESULTS_ROOT / today
    run_dir.mkdir(parents=True, exist_ok=True)
    for engine in requested_engines:
        (run_dir / engine).mkdir(exist_ok=True)

    # Concurrency: keep modest to avoid rate limits
    sem = asyncio.Semaphore(args.concurrency)

    results: list[PromptResult] = []
    async with httpx.AsyncClient() as client:
        tasks = []
        for prompt in selected:
            for engine in requested_engines:
                tasks.append(run_one(client, prompt, engine, keys[engine], competitors, sem))
        # progress every 10 completions
        completed = 0
        for fut in asyncio.as_completed(tasks):
            r = await fut
            results.append(r)
            completed += 1
            mark = "✓" if r.success else "✗"
            dd = "DD" if r.donordock_mentioned else "  "
            print(f"  [{completed}/{len(tasks)}] {mark} {dd} {r.engine:11s} {r.prompt_id} {r.prompt_text[:60]}{'…' if len(r.prompt_text) > 60 else ''}")
            # Save per-result JSON immediately
            (run_dir / r.engine / f"{r.prompt_id}.json").write_text(json.dumps(asdict(r), indent=2))

    # Build summary
    summary = build_summary(results, config, args.priority, today)
    (run_dir / "_summary.json").write_text(json.dumps(summary, indent=2))
    (run_dir / "_report.md").write_text(render_report(summary, results))

    print(f"\n[done] {len(results)} results written to {run_dir}")
    print(f"       Citation rate: DonorDock mentioned in {summary['donordock_citation_rate_pct']}% of responses")
    print(f"       Estimated cost: ${summary['total_estimated_cost_usd']}")
    print(f"       Report: {run_dir}/_report.md")

    return 0


_POSITION_RANK = {"early": 0, "mid": 1, "late": 2, "n/a": 3}


def position_label(pos: int | None) -> str:
    """Bucket a DonorDock character offset into early / mid / late."""
    if pos is None:
        return "n/a"
    if pos < 200:
        return "early"
    if pos < 800:
        return "mid"
    return "late"


def build_summary(results: list[PromptResult], config: dict, priority: str, run_date: str) -> dict:
    total = len(results)
    successes = [r for r in results if r.success]
    dd_hits = [r for r in successes if r.donordock_mentioned]

    # Prompt-bank metadata (pillar + canonical text) keyed by prompt id.
    pid_meta = {p["id"]: {"pillar": p.get("pillar", "Unknown"), "text": p.get("text", "")}
                for p in config.get("prompts", [])}

    by_engine: dict[str, dict] = {}
    for r in results:
        e = r.engine
        be = by_engine.setdefault(e, {"total": 0, "ok": 0, "errors": 0, "donordock_hits": 0, "cost_usd": 0.0})
        be["total"] += 1
        if r.success:
            be["ok"] += 1
            if r.donordock_mentioned:
                be["donordock_hits"] += 1
            be["cost_usd"] += r.estimated_cost_usd
        else:
            be["errors"] += 1

    competitor_hits: dict[str, int] = {}
    for r in successes:
        for c in r.competitors_mentioned:
            competitor_hits[c] = competitor_hits.get(c, 0) + 1

    # Roll successes up per prompt: which engines cited DonorDock, which competitors
    # showed up, best (earliest) DonorDock position, and how many engines answered.
    by_prompt: dict[str, dict] = {}
    for r in successes:
        d = by_prompt.setdefault(r.prompt_id, {"cited": set(), "ok": set(), "comps": {}, "best_pos": None})
        d["ok"].add(r.engine)
        if r.donordock_mentioned:
            d["cited"].add(r.engine)
            if r.donordock_position is not None:
                d["best_pos"] = r.donordock_position if d["best_pos"] is None else min(d["best_pos"], r.donordock_position)
        for c in r.competitors_mentioned:
            d["comps"][c] = d["comps"].get(c, 0) + 1

    # Per-pillar citation rate + the competitor most cited inside that pillar's prompts.
    pillar_agg: dict[str, dict] = {}
    for r in successes:
        pil = pid_meta.get(r.prompt_id, {}).get("pillar", "Unknown")
        pa = pillar_agg.setdefault(pil, {"prompts": set(), "ok": 0, "hits": 0, "comps": {}})
        pa["prompts"].add(r.prompt_id)
        pa["ok"] += 1
        if r.donordock_mentioned:
            pa["hits"] += 1
        for c in r.competitors_mentioned:
            pa["comps"][c] = pa["comps"].get(c, 0) + 1
    by_pillar = {}
    for pil, pa in pillar_agg.items():
        top_comp = max(pa["comps"].items(), key=lambda kv: kv[1]) if pa["comps"] else None
        by_pillar[pil] = {
            "prompts": len(pa["prompts"]),
            "ok": pa["ok"],
            "donordock_hits": pa["hits"],
            "citation_rate_pct": round(100 * pa["hits"] / max(1, pa["ok"]), 1),
            "top_competitor": ({"name": top_comp[0], "mentions": top_comp[1]} if top_comp else None),
        }

    # Top wins: prompts where DonorDock was cited, strongest first (most engines, earliest).
    wins = []
    for pid, d in by_prompt.items():
        if d["cited"]:
            wins.append({
                "prompt_id": pid,
                "prompt_text": pid_meta.get(pid, {}).get("text", ""),
                "pillar": pid_meta.get(pid, {}).get("pillar", "Unknown"),
                "engines": sorted(d["cited"]),
                "n_engines": len(d["cited"]),
                "position": position_label(d["best_pos"]),
            })
    wins.sort(key=lambda w: (-w["n_engines"], _POSITION_RANK[w["position"]], w["prompt_id"]))

    # Top misses: prompts where DonorDock was cited by ZERO engines but competitors were —
    # the most contested gaps come first (most distinct competitors, then most engines answering).
    misses = []
    for pid, d in by_prompt.items():
        if not d["cited"] and d["comps"]:
            comps_sorted = sorted(d["comps"].items(), key=lambda kv: -kv[1])
            misses.append({
                "prompt_id": pid,
                "prompt_text": pid_meta.get(pid, {}).get("text", ""),
                "pillar": pid_meta.get(pid, {}).get("pillar", "Unknown"),
                "competitors": [c for c, _ in comps_sorted[:5]],
                "n_competitors": len(d["comps"]),
                "n_engines_missed": len(d["ok"]),
            })
    misses.sort(key=lambda m: (-m["n_competitors"], -m["n_engines_missed"], m["prompt_id"]))

    return {
        "run_date": run_date,
        "priority_filter": priority,
        "total_runs": total,
        "successes": len(successes),
        "errors": total - len(successes),
        "donordock_hits": len(dd_hits),
        "donordock_citation_rate_pct": round(100 * len(dd_hits) / max(1, len(successes)), 1),
        "total_estimated_cost_usd": round(sum(r.estimated_cost_usd for r in successes), 4),
        "by_engine": {k: {**v, "cost_usd": round(v["cost_usd"], 4),
                          "citation_rate_pct": round(100 * v["donordock_hits"] / max(1, v["ok"]), 1)}
                      for k, v in by_engine.items()},
        "competitor_mentions": dict(sorted(competitor_hits.items(), key=lambda kv: -kv[1])),
        "by_pillar": dict(sorted(by_pillar.items(), key=lambda kv: -kv[1]["citation_rate_pct"])),
        "top_wins": wins[:25],
        "top_misses": misses[:25],
    }


def render_report(summary: dict, results: list[PromptResult]) -> str:
    lines = [
        f"# AEO Citation Run — {summary['run_date']}",
        "",
        f"**Priority filter:** `{summary['priority_filter']}`",
        f"**Total runs:** {summary['total_runs']}  (successes {summary['successes']}, errors {summary['errors']})",
        f"**DonorDock citation rate:** **{summary['donordock_citation_rate_pct']}%**  ({summary['donordock_hits']}/{summary['successes']})",
        f"**Total estimated cost:** ${summary['total_estimated_cost_usd']}",
        "",
        "## By engine",
        "| Engine | Runs | OK | Errors | DD hits | Citation % | Cost |",
        "|---|---|---|---|---|---|---|",
    ]
    for engine, v in summary["by_engine"].items():
        lines.append(
            f"| {engine} | {v['total']} | {v['ok']} | {v['errors']} | {v['donordock_hits']} | {v['citation_rate_pct']}% | ${v['cost_usd']} |"
        )
    lines += ["", "## Competitor mentions (across all engines)", ""]
    for c, n in summary["competitor_mentions"].items():
        lines.append(f"- {c}: {n}")
    lines += [
        "",
        "## Wins (DonorDock cited)",
        "",
    ]
    wins = [r for r in results if r.success and r.donordock_mentioned]
    for r in wins[:50]:
        pos_label = "early" if (r.donordock_position is not None and r.donordock_position < 200) else \
                    ("mid" if (r.donordock_position is not None and r.donordock_position < 800) else "late")
        lines.append(f"- [{r.engine}] **{r.prompt_id}** ({pos_label}) — {r.prompt_text}")
    lines += [
        "",
        "## Misses (no DonorDock mention) — opportunities",
        "",
    ]
    misses = [r for r in results if r.success and not r.donordock_mentioned]
    for r in misses[:50]:
        comps = ", ".join(r.competitors_mentioned[:5]) if r.competitors_mentioned else "—"
        lines.append(f"- [{r.engine}] **{r.prompt_id}** — {r.prompt_text}  _(competitors cited: {comps})_")
    if len(misses) > 50:
        lines.append(f"- _… and {len(misses) - 50} more misses_")
    lines += ["", "## Errors", ""]
    errs = [r for r in results if not r.success]
    for r in errs:
        lines.append(f"- [{r.engine}] **{r.prompt_id}** — {r.error}")
    if not errs:
        lines.append("_None._")
    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Summary rebuild — regenerate _summary.json/_report.md for past runs from the
# committed per-prompt JSON, using the current build_summary schema. Lets us
# backfill new fields (by_pillar, top_wins, top_misses) into historical runs
# without re-hitting any API. No keys or network required.
# ---------------------------------------------------------------------------

def reconstruct_results(run_dir: Path) -> list[PromptResult]:
    """Load every per-prompt JSON under a run dir's engine folders into PromptResults."""
    results: list[PromptResult] = []
    for engine_dir in sorted(run_dir.iterdir()):
        if not engine_dir.is_dir() or engine_dir.name not in ENGINES:
            continue  # skip aio-chrome and other non-API engine folders
        for f in sorted(engine_dir.glob("*.json")):
            try:
                data = json.loads(f.read_text())
                # Tolerate older JSON that predates a field by filling dataclass defaults.
                results.append(PromptResult(**{k: data.get(k) for k in PromptResult.__dataclass_fields__}))
            except Exception as e:
                print(f"[warn] could not load {f}: {e}", file=sys.stderr)
    return results


def rebuild_all_summaries(config: dict) -> int:
    """Rewrite _summary.json + _report.md for every dated run dir found on disk."""
    n = 0
    for run_dir in sorted(RESULTS_ROOT.iterdir()):
        if not run_dir.is_dir() or not re.match(r"\d{4}-\d{2}-\d{2}$", run_dir.name):
            continue
        results = reconstruct_results(run_dir)
        if not results:
            print(f"[skip] {run_dir.name}: no per-engine results (AIO-only or empty)")
            continue
        priority, run_date = "full", run_dir.name
        existing = run_dir / "_summary.json"
        if existing.exists():
            try:
                old = json.loads(existing.read_text())
                priority = old.get("priority_filter", priority)
                run_date = old.get("run_date", run_date)
            except Exception:
                pass
        else:
            priority = "full" if len({r.prompt_id for r in results}) > 80 else "top-50"
        summary = build_summary(results, config, priority, run_date)
        existing.write_text(json.dumps(summary, indent=2))
        (run_dir / "_report.md").write_text(render_report(summary, results))
        n += 1
        print(f"[rebuilt] {run_dir.name}: {summary['donordock_citation_rate_pct']}% cite · "
              f"{len(summary['top_wins'])} wins · {len(summary['top_misses'])} misses · "
              f"{len(summary['by_pillar'])} pillars")
    print(f"[done] rebuilt {n} run summaries")
    return n


def parse_args():
    p = argparse.ArgumentParser(description="DonorDock AEO Citation Runner")
    p.add_argument("--priority", choices=["top-50", "full", "aio"], default="full")
    p.add_argument("--engines", help="Comma-separated subset: claude,openai,perplexity,gemini")
    p.add_argument("--concurrency", type=int, default=8, help="Max concurrent in-flight requests")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--rebuild-summaries", action="store_true",
                   help="Regenerate _summary.json/_report.md for all past runs from committed JSON (no API calls)")
    return p.parse_args()


if __name__ == "__main__":
    args = parse_args()
    if args.rebuild_summaries:
        rebuild_all_summaries(load_prompts())
        sys.exit(0)
    sys.exit(asyncio.run(main_async(args)))
