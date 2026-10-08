#!/usr/bin/env python3
"""
DonorDock Help Center Release Notes Fetcher
===========================================
Scrapes https://helpcenter.donordock.com/kb/en/product-updates-150346 for
release-note entries published on or after a given date, then fetches each article
and parses its sections into a structured digest.

Output: JSON with an `entries` array. Each entry:
  { date, title, url, new_features: [...], updates: [...], fixes: [...],
    other: [...], raw_markdown }

Usage:
    python3 fetch-release-notes.py --since YYYY-MM-DD --output digest.json \
        [--exclude-urls-from state.json]

The --since date is INCLUSIVE: a note dated on the cutoff day is in scope. That
closes a gap where a note dated on the cutoff day but posted after that week's
run fell between two windows (Product Updates 9-18-2026 was missed that way).
Pass --exclude-urls-from with the audit's state.json so notes already audited
(its `last_release_note_urls`) are not audited twice.
"""

import argparse
import json
import re
import sys
import time
from datetime import datetime

try:
    import requests
    from bs4 import BeautifulSoup
    from markdownify import markdownify as md
except ImportError:
    print("Missing deps. pip install requests beautifulsoup4 markdownify --break-system-packages")
    sys.exit(1)

INDEX_URL = "https://helpcenter.donordock.com/kb/en/product-updates-150346"
HEADERS = {"User-Agent": "Mozilla/5.0 DonorDock-Audit/1.0"}

DATE_RE = re.compile(r"(\d{1,2})[./](\d{1,2})[./](\d{4})")

SECTION_KEYWORDS = {
    "new_features": ["new", "added", "new feature", "new in", "introducing"],
    "updates":      ["improved", "updated", "enhanced", "changed", "update"],
    "fixes":        ["fixed", "bug fix", "bug fixes", "resolved"],
}


def fetch(url):
    r = requests.get(url, headers=HEADERS, timeout=30)
    r.raise_for_status()
    return BeautifulSoup(r.text, "html.parser")


def parse_date(text):
    m = DATE_RE.search(text or "")
    if not m:
        return None
    mo, d, y = map(int, m.groups())
    try:
        return datetime(y, mo, d).date()
    except ValueError:
        return None


def discover_entries():
    """Return list of {title, url, date} from the index page."""
    soup = fetch(INDEX_URL)
    entries = []
    seen = set()
    for a in soup.find_all("a", href=True):
        href = a["href"]
        title = (a.get_text() or "").strip()
        if not title:
            continue
        if not re.search(r"(release|product\s*update)", title, re.I):
            continue
        if href.startswith("/"):
            url = "https://helpcenter.donordock.com" + href
        elif href.startswith("http"):
            url = href
        else:
            continue
        if url in seen or url == INDEX_URL:
            continue
        seen.add(url)
        d = parse_date(title)
        entries.append({"title": title, "url": url, "date": d.isoformat() if d else None})
    return entries


def guide_key(url):
    """Stable identity for a Help Center guide: the URL up to /Steps/."""
    return url.split("/Steps/")[0].rstrip("/")


def classify_heading(text):
    t = (text or "").strip().lower()
    for bucket, keywords in SECTION_KEYWORDS.items():
        for kw in keywords:
            if t.startswith(kw) or f" {kw} " in f" {t} ":
                return bucket
    return "other"


def parse_article(url):
    soup = fetch(url)
    main = soup.find("main") or soup.find("article") or soup.body
    for sel in ["nav", "footer", "header"]:
        for el in main.find_all(sel):
            el.decompose()

    result = {"new_features": [], "updates": [], "fixes": [], "other": []}
    current_bucket = "other"
    current_item = None

    for el in main.find_all(["h1", "h2", "h3", "h4", "h5", "h6", "p", "li"]):
        text = el.get_text(" ", strip=True)
        if not text:
            continue
        if el.name in ("h1", "h2", "h3", "h4", "h5", "h6"):
            current_bucket = classify_heading(text)
            current_item = {"heading": text, "body": []}
            result[current_bucket].append(current_item)
        else:
            if current_item is None:
                current_item = {"heading": "(intro)", "body": []}
                result[current_bucket].append(current_item)
            if text not in current_item["body"]:
                current_item["body"].append(text)

    raw_md = md(str(main), heading_style="ATX").strip()
    return result, raw_md


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--since", required=True, help="ISO date YYYY-MM-DD. Entries dated on or after this date are fetched (inclusive).")
    ap.add_argument("--exclude-urls-from", help="JSON file holding a list of URLs, or an object with `last_release_note_urls`. Those entries are skipped as already audited.")
    ap.add_argument("--output", default="release-digest.json")
    ap.add_argument("--delay", type=float, default=0.3)
    args = ap.parse_args()

    try:
        since = datetime.fromisoformat(args.since).date()
    except ValueError:
        print(f"Bad --since value: {args.since}", file=sys.stderr)
        sys.exit(2)

    print(f"Discovering release-note entries at {INDEX_URL}...")
    entries = discover_entries()
    print(f"Found {len(entries)} candidate entries on index page.")

    audited = set()
    if args.exclude_urls_from:
        with open(args.exclude_urls_from) as f:
            data = json.load(f)
        urls = data.get("last_release_note_urls", []) if isinstance(data, dict) else data
        audited = {guide_key(u) for u in urls}

    scoped = []
    for e in entries:
        if not e["date"]:
            continue
        if datetime.fromisoformat(e["date"]).date() < since:
            continue
        if guide_key(e["url"]) in audited:
            print(f"  skipping already-audited {e['date']}  {e['title']}")
            continue
        scoped.append(e)

    print(f"{len(scoped)} entries on or after {since.isoformat()} not yet audited.")

    digest = {"since": since.isoformat(), "fetched_at": datetime.utcnow().isoformat() + "Z", "entries": []}

    for e in sorted(scoped, key=lambda x: x["date"]):
        print(f"  fetching {e['date']}  {e['title']}")
        try:
            sections, raw_md = parse_article(e["url"])
        except Exception as ex:
            print(f"  ! failed: {ex}")
            continue
        digest["entries"].append({
            "date": e["date"],
            "title": e["title"],
            "url": e["url"],
            "new_features": sections["new_features"],
            "updates": sections["updates"],
            "fixes": sections["fixes"],
            "other": sections["other"],
            "raw_markdown": raw_md,
        })
        time.sleep(args.delay)

    with open(args.output, "w") as f:
        json.dump(digest, f, indent=2)

    print(f"Wrote {args.output} — {len(digest['entries'])} entries.")


if __name__ == "__main__":
    main()
