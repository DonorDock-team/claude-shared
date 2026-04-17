#!/usr/bin/env python3
"""
DonorDock Webflow Page Snapshotter
==================================
Fetches live donordock.com pages (filtered by sitemap section), strips
nav/footer/chrome, converts main content to markdown, and writes one .md
file per page plus an index.json mapping url -> file -> sha256.

Purpose: give the weekly release audit a full-content snapshot of static
pages (Home, Pricing, Comparison, Integrations) so it can detect stale or
missing copy, not just titles and tags.

Usage:
    python3 snapshot-webflow-pages.py \
        --sitemap <url-or-path> \
        --sections core compare integrations \
        --output-dir ./snapshot/pages
"""

import argparse
import hashlib
import json
import os
import sys
import time
from pathlib import Path
from urllib.parse import urlparse

try:
    import requests
    from bs4 import BeautifulSoup
    from markdownify import markdownify as md
except ImportError:
    print("Missing deps. pip install requests beautifulsoup4 markdownify --break-system-packages")
    sys.exit(1)

HEADERS = {"User-Agent": "Mozilla/5.0 DonorDock-Audit/1.0"}
STRIP_SELECTORS = ["nav", "footer", "header", "script", "style", "noscript",
                   "[role=navigation]", "[role=banner]", "[role=contentinfo]",
                   ".w-nav", ".w-footer", ".navbar", ".footer"]


def load_sitemap(source):
    if source.startswith("http://") or source.startswith("https://"):
        r = requests.get(source, headers=HEADERS, timeout=30)
        r.raise_for_status()
        return r.json()
    with open(source) as f:
        return json.load(f)


def slugify_url(url):
    p = urlparse(url)
    path = p.path.strip("/") or "home"
    return path.replace("/", "__") or "home"


def snapshot_page(url):
    r = requests.get(url, headers=HEADERS, timeout=30)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")

    for sel in STRIP_SELECTORS:
        for el in soup.select(sel):
            el.decompose()

    main = soup.find("main") or soup.body
    title = (soup.title.get_text().strip() if soup.title else "")
    meta_desc = ""
    m = soup.find("meta", attrs={"name": "description"})
    if m and m.get("content"):
        meta_desc = m["content"].strip()

    body_md = md(str(main), heading_style="ATX").strip()
    sha = hashlib.sha256(body_md.encode("utf-8")).hexdigest()

    front = [
        f"# {title}",
        "",
        f"**URL:** {url}",
        f"**Meta description:** {meta_desc}",
        f"**Captured:** {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}",
        f"**SHA256:** {sha}",
        "",
        "---",
        "",
    ]
    return "\n".join(front) + body_md, sha, title, meta_desc


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sitemap", required=True, help="URL or path to website-sitemap.json")
    ap.add_argument("--sections", nargs="+", required=True,
                    help="Sitemap sections to include, e.g. core compare integrations")
    ap.add_argument("--output-dir", required=True)
    ap.add_argument("--delay", type=float, default=0.4)
    ap.add_argument("--limit", type=int, default=0, help="Optional cap on pages (0 = no limit)")
    args = ap.parse_args()

    sitemap = load_sitemap(args.sitemap)
    pages = [p for p in sitemap.get("pages", []) if p.get("section") in args.sections]
    if args.limit:
        pages = pages[: args.limit]

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    index = {"captured_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
             "sections": args.sections, "pages": []}

    print(f"Snapshotting {len(pages)} pages into {out_dir}...")
    failures = 0
    for i, p in enumerate(pages, 1):
        url = p["url"]
        slug = slugify_url(url)
        try:
            body, sha, title, meta_desc = snapshot_page(url)
            path = out_dir / f"{slug}.md"
            path.write_text(body)
            index["pages"].append({"url": url, "section": p["section"],
                                   "title": title, "meta_description": meta_desc,
                                   "file": str(path.relative_to(out_dir)),
                                   "sha256": sha})
            print(f"  [{i}/{len(pages)}] {url}")
        except Exception as ex:
            failures += 1
            print(f"  [{i}/{len(pages)}] FAIL {url}: {ex}")
        time.sleep(args.delay)

    with open(out_dir / "index.json", "w") as f:
        json.dump(index, f, indent=2)

    print(f"Done. {len(index['pages'])} pages saved, {failures} failures.")
    if failures and failures >= len(pages) // 2:
        print("More than half failed — aborting with nonzero exit.", file=sys.stderr)
        sys.exit(3)


if __name__ == "__main__":
    main()
