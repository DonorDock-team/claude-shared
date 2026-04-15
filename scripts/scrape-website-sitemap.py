#!/usr/bin/env python3
"""
DonorDock Website Sitemap Scraper
==================================
Fetches the donordock.com sitemap.xml, enriches each URL with page title
and meta description, classifies pages into sections, and outputs a
structured JSON sitemap optimized for LLM context windows.

Designed to run on a weekly schedule to keep the shared content registry
up to date. Output goes to DonorDock-team/claude-shared sitemaps/.

Usage:
    python scrape-website-sitemap.py [OPTIONS]

Options:
    --sitemap-url URL    Sitemap XML URL (default: https://www.donordock.com/sitemap.xml)
    --output FILE        Output file (default: ./website-sitemap.json)
    --workers INT        Concurrent fetch workers (default: 10)
    --delay FLOAT        Delay between request starts in seconds (default: 0.1)
    --timeout INT        Per-request timeout in seconds (default: 10)
"""

import argparse
import json
import re
import time
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Missing dependencies. Install them with:")
    print("  pip install requests beautifulsoup4 lxml --break-system-packages")
    sys.exit(1)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
}

# Section classification by URL path prefix
SECTION_MAP = [
    ("/articles/", "articles"),
    ("/features/", "features"),
    ("/integrations/", "integrations"),
    ("/tools/", "tools"),
    ("/success-stories/", "success-stories"),
    ("/compare/", "compare"),
    ("/solutions/", "solutions"),
    ("/academy/", "academy"),
]

# Paths to exclude entirely
EXCLUDED_PREFIXES = [
    "/tags/",
    "/team/",
    "/lp/",
    "/landing/",
]


def classify_section(url):
    """Classify a URL into a section based on its path."""
    path = urlparse(url).path
    for prefix, section in SECTION_MAP:
        if path.startswith(prefix):
            return section
    return "core"


def is_excluded(url):
    """Check if a URL should be excluded from the sitemap."""
    path = urlparse(url).path
    for prefix in EXCLUDED_PREFIXES:
        if path.startswith(prefix):
            return True
    return False


def fetch_sitemap_urls(sitemap_url):
    """Fetch and parse sitemap.xml to extract all URLs."""
    print(f"Fetching sitemap: {sitemap_url}")
    resp = requests.get(sitemap_url, headers=HEADERS, timeout=30)
    resp.raise_for_status()

    # Parse XML - try lxml first, fall back to html.parser
    try:
        soup = BeautifulSoup(resp.content, "lxml-xml")
    except Exception:
        soup = BeautifulSoup(resp.content, "html.parser")

    urls = []
    for loc in soup.find_all("loc"):
        url = loc.get_text(strip=True)
        if url:
            urls.append(url)

    return urls


def fetch_page_metadata(url, timeout=10):
    """Fetch a single page and extract title + meta description."""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=timeout)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        # Extract title: prefer og:title, fall back to <title> tag
        title = None
        og_title = soup.find("meta", property="og:title")
        if og_title and og_title.get("content"):
            title = og_title["content"].strip()
        if not title:
            title_tag = soup.find("title")
            if title_tag:
                title = title_tag.get_text(strip=True)

        # Extract description: prefer meta description, fall back to og:description
        description = None
        meta_desc = soup.find("meta", attrs={"name": "description"})
        if meta_desc and meta_desc.get("content"):
            description = meta_desc["content"].strip()
        if not description:
            og_desc = soup.find("meta", property="og:description")
            if og_desc and og_desc.get("content"):
                description = og_desc["content"].strip()

        return {
            "url": url,
            "title": title or url.split("/")[-1].replace("-", " ").title(),
            "description": description,
            "section": classify_section(url),
        }

    except Exception as e:
        # Return minimal entry on failure
        return {
            "url": url,
            "title": url.split("/")[-1].replace("-", " ").title(),
            "description": None,
            "section": classify_section(url),
            "_error": str(e),
        }


def main():
    parser = argparse.ArgumentParser(
        description="Scrape donordock.com sitemap into a JSON index"
    )
    parser.add_argument(
        "--sitemap-url",
        default="https://www.donordock.com/sitemap.xml",
    )
    parser.add_argument("--output", default="./website-sitemap.json")
    parser.add_argument("--workers", type=int, default=10)
    parser.add_argument("--delay", type=float, default=0.1)
    parser.add_argument("--timeout", type=int, default=10)
    args = parser.parse_args()

    # Phase 1: Fetch all URLs from sitemap.xml
    all_urls = fetch_sitemap_urls(args.sitemap_url)
    print(f"Found {len(all_urls)} URLs in sitemap.xml")

    # Filter out excluded paths
    urls = [u for u in all_urls if not is_excluded(u)]
    excluded_count = len(all_urls) - len(urls)
    print(f"Excluded {excluded_count} URLs (tags, team, landing pages)")
    print(f"Processing {len(urls)} URLs")

    # Phase 2: Fetch metadata for each page concurrently
    print(f"\nFetching page metadata ({args.workers} workers)...")
    pages = []
    errors = []
    completed = 0

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {}
        for i, url in enumerate(urls):
            future = executor.submit(fetch_page_metadata, url, args.timeout)
            futures[future] = url
            # Stagger requests
            if i < len(urls) - 1:
                time.sleep(args.delay)

        for future in as_completed(futures):
            completed += 1
            result = future.result()
            if "_error" in result:
                errors.append({"url": result["url"], "error": result.pop("_error")})
            pages.append(result)

            if completed % 50 == 0 or completed == len(urls):
                print(f"  [{completed}/{len(urls)}] pages processed")

    # Sort pages by section, then by URL
    pages.sort(key=lambda p: (p["section"], p["url"]))

    # Phase 3: Build section index
    section_index = {}
    for page in pages:
        section = page["section"]
        section_index[section] = section_index.get(section, 0) + 1

    # Phase 4: Build output
    sitemap = {
        "website": {
            "name": "DonorDock Website",
            "base_url": "https://www.donordock.com",
            "source": args.sitemap_url,
            "scraped_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "total_pages": len(pages),
            "total_sections": len(section_index),
        },
        "section_index": dict(sorted(section_index.items())),
        "pages": pages,
    }

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(sitemap, f, indent=2, ensure_ascii=False)

    file_size = len(json.dumps(sitemap, ensure_ascii=False))

    # Phase 5: Summary
    print(f"\nSitemap saved to: {args.output}")
    print(f"Total pages: {len(pages)}")
    print(f"File size: {file_size:,} bytes ({file_size / 1024:.1f} KB)")
    print(f"\nSection breakdown:")
    for section, count in sorted(section_index.items()):
        print(f"  {section}: {count} pages")

    if errors:
        print(f"\nWarning: {len(errors)} pages had fetch errors:")
        for err in errors[:10]:
            print(f"  {err['url']}: {err['error']}")
        if len(errors) > 10:
            print(f"  ... and {len(errors) - 10} more")


if __name__ == "__main__":
    main()
