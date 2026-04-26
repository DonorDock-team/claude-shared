# DonorDock AEO Citation Runner

Tracks how often DonorDock is cited by AI search engines (Claude, ChatGPT, Perplexity, Gemini) when nonprofits ask the queries we care about. Runs the prompt bank weekly, stores per-prompt-per-engine results, and produces a human-readable report.

## What it does

1. Reads the prompt bank at `seo-brain/tracking/prompts.json`
2. Filters prompts by priority (`top-50`, `full`, or `aio`)
3. Loads API keys from 1Password via `op` CLI
4. Runs each selected prompt against each enabled engine
5. Detects: DonorDock mention (yes/no, position in response), competitor mentions, cited URLs
6. Saves per-prompt-per-engine JSON + a daily summary + a Markdown report

## One-time setup

```bash
# Install deps
pip3 install -r requirements.txt

# Sign in to 1Password (must do this in the same shell that runs the script)
eval $(op signin)

# Verify key access (won't print the keys, just confirms readability)
op item get "Claude API Key" --field credential --reveal > /dev/null && echo "✓ Claude OK"
op item get "OpenAI API Credentials - DonorDock" --field credential --reveal > /dev/null && echo "✓ OpenAI OK"
op item get "Perplexity - DonorDock API Credentials" --field credential --reveal > /dev/null && echo "✓ Perplexity OK"
op item get "Google AI API key (Yarn)" --field credential --reveal > /dev/null && echo "✓ Gemini OK"
```

## Usage

```bash
# Validate config + bank without API calls
python3 run.py --dry-run

# Thursday — top-50 drift run (~50 prompts × 4 engines = 200 calls)
python3 run.py --priority top-50

# Monday — full bank (~150 prompts × 4 engines = 600 calls)
python3 run.py --priority full

# Saturday — AIO subset (use Chrome MCP separately; this only filters the JSON)
python3 run.py --priority aio --dry-run

# Run only specific engines (e.g., quick test or skip Perplexity if outage)
python3 run.py --priority top-50 --engines claude,openai

# Tune concurrency (default 8)
python3 run.py --priority full --concurrency 4
```

## Output structure

```
seo-brain/tracking/ai-citations/
└── 2026-04-28/                    # one folder per run date (UTC)
    ├── _summary.json              # aggregate metrics
    ├── _report.md                 # human-readable report
    ├── anthropic/
    │   ├── P001.json              # raw response + parsed signals per prompt
    │   ├── P002.json
    │   └── …
    ├── openai/
    │   └── …
    ├── perplexity/
    │   └── …
    └── gemini/
        └── …
```

### Per-prompt JSON shape

```json
{
  "prompt_id": "P005",
  "prompt_text": "DonorDock vs Bloomerang",
  "engine": "anthropic",
  "timestamp": "2026-04-28T13:00:00+00:00",
  "success": true,
  "error": null,
  "response_text": "DonorDock and Bloomerang are both…",
  "donordock_mentioned": true,
  "donordock_position": 0,
  "competitors_mentioned": ["Bloomerang"],
  "urls_cited": ["https://www.donordock.com/articles/best-nonprofit-crm"],
  "input_tokens": 42,
  "output_tokens": 614,
  "estimated_cost_usd": 0.009336,
  "meta": {"model": "claude-sonnet-4-5"}
}
```

## Editing the prompt bank

The bank lives at `seo-brain/tracking/prompts.json`. Three ways to edit:

1. **GitHub web UI** — most common; edits get committed via PR
2. **Local clone + commit** — same idea, more comfortable in VS Code
3. **Phase 7 dashboard (TBD)** — will provide a web editor that writes back via the GitHub MCP

### Common edits

```jsonc
// Disable a prompt that's no longer relevant
{ "id": "P150", "active": false }

// Move a prompt from full-only to top-50 (gets the Thu drift run)
{ "id": "P099", "priority": "top-50" }

// Toggle AIO eligibility (Saturday Chrome run)
{ "id": "P042", "aio": true }

// Add a new prompt — append to the array, use next P-id
{
  "id": "P151",
  "text": "How do nonprofits track recurring donor lifetime value",
  "phase": "AWARENESS",
  "pillar": "Donor Retention",
  "icp": "Medium Nonprofits",
  "priority": "full-only",
  "category": "operational",
  "active": true,
  "aio": false
}
```

The runner picks up changes on the next run. No restart, no rebuild.

## Scheduling

Phase 6 wires this into automated weekly cron via the `scheduled-tasks` MCP. For now, run manually on:

- **Mon 6am ET** — `python3 run.py --priority full`
- **Thu 6am ET** — `python3 run.py --priority top-50`
- **Sat 6am ET** — Google AIO via Chrome MCP (separate workflow, not this script)

## Cost estimation

Per-call cost (1K input / 2K output, average):

| Engine | Per call |
|---|---|
| Claude Sonnet 4.5 | ~$0.033 |
| GPT-4o | ~$0.025 |
| Perplexity Sonar Pro | ~$0.038 |
| Gemini 1.5 Flash | ~$0.001 |
| **Combined per prompt** | **~$0.097** |

Monthly estimate at the locked cadence:
- Mon full bank: 4 × 150 × ~$0.097 = ~$58
- Thu top-50: 4 × 50 × ~$0.097 = ~$19
- Sat AIO via Chrome: $0 (browser-based)
- **Total: ~$77/mo** (well under $200 budget)

The runner writes `estimated_cost_usd` per call to per-prompt JSON, and the summary aggregates total cost. Watch the report `_report.md` over time — actual costs will land slightly higher than estimates because real responses may exceed the 2K-token assumption.

## Troubleshooting

**`op item get` fails** — make sure `eval $(op signin)` ran in the current shell. The runner inherits its env from there.

**HTTP 429 rate limit** — drop concurrency: `--concurrency 4` or `--concurrency 2`.

**An engine is down** — exclude it: `--engines claude,openai,gemini`. The runner records a missing-engine result for later analysis if you re-run later that day.

**JSON validation error in prompts.json** — run `python3 -c "import json; json.load(open('../prompts.json'))"` from the runner dir to find the offending line.

## Future enhancements (Phase 6+)

- Weekly delta report (this week vs last week vs 4-week trend)
- Auto-alert when DonorDock citation rate drops >5% week-over-week
- Phase 7 dashboard with prompt editor + citation trend charts
- Phase 8 Asana integration to auto-create improvement tasks for prompts with declining citation
