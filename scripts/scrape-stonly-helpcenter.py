#!/usr/bin/env python3
"""
Stonly Help Center Scraper v2
==============================
Recursively crawls a Stonly-hosted help center to discover ALL articles
at any nesting depth. Outputs a compact JSON sitemap optimized for
LLM context windows -- title, URL, category breadcrumb, and a short
summary (first ~200 chars of content) per article.

Full article content is NOT included by default to keep the sitemap small.
Use --full-content to include it (warning: much larger output).

Changes from v1:
- Recursive category crawling (any depth, vs. 2 levels)
- Filters out global sidebar nav to avoid false recursion
- Tracks full breadcrumb path for each article
- Compact output format by default (~30-50KB vs ~300KB)
- Deduplication by URL path
- Skips release notes by default (--include-release-notes to keep them)
- Progress reporting with article count

Usage:
    python scrape-stonly-helpcenter.py [OPTIONS]

Options:
    --base-url URL            Base URL (default: https://helpcenter.donordock.com)
    --entry-path PATH         Entry path (default: /kb/en/)
    --output FILE             Output file (default: ./helpcenter-sitemap.json)
    --delay SECONDS           Delay between requests (default: 0.3)
    --full-content            Include full article content (larger output)
    --max-content INT         Max chars per article (default: 10000, with --full-content)
    --summary-length INT      Summary snippet length (default: 200)
    --include-release-notes   Include release notes articles
"""

import argparse
import json
import re
import time
import sys

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Missing dependencies. Install them with:")
    print("  pip install requests beautifulsoup4 --break-system-packages")
    sys.exit(1)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
}

# Patterns
CATEGORY_PATTERN = re.compile(r"^/kb/en/[\w-]+-\d+$")
ARTICLE_PATTERN = re.compile(r"^/kb/guide/en/[\w-]+/Steps/\d+$")


def fetch_page(url):
    """Fetch a page and return BeautifulSoup object."""
    resp = requests.get(url, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    return BeautifulSoup(resp.text, "html.parser")


def extract_links(soup):
    """Extract all category and article links from a page."""
    categories = {}
    articles = []

    for link in soup.find_all("a", href=True):
        href = link["href"]
        text = link.get_text(strip=True)
        if not text:
            continue

        if CATEGORY_PATTERN.match(href):
            # Extract clean category name from the URL slug
            # e.g. /kb/en/integration-builder-apps-473961 -> "Integration Builder Apps"
            slug = href.split("/")[-1]              # integration-builder-apps-473961
            slug = re.sub(r"-\d+$", "", slug)       # integration-builder-apps
            clean_name = slug.replace("-", " ").title()  # Integration Builder Apps
            categories[href] = clean_name
        elif ARTICLE_PATTERN.match(href):
            articles.append({"title": text, "path": href})

    return categories, articles


def extract_content(soup):
    """Extract text content from an article page."""
    for tag in soup(["script", "style", "nav", "footer", "header"]):
        tag.decompose()

    content_area = None
    for selector in [
        ".guide-content", ".step-content", ".article-content",
        ".stn-guide-content", "article", ".content", "main",
        "[class*='content']", "[class*='guide']", "[class*='step']"
    ]:
        found = soup.select(selector)
        if found:
            content_area = found[0]
            break

    if not content_area:
        content_area = soup.body if soup.body else soup

    text = content_area.get_text(separator="\n", strip=True)
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Scrape a Stonly help center into a JSON sitemap (v2)")
    parser.add_argument("--base-url", default="https://helpcenter.donordock.com")
    parser.add_argument("--entry-path", default="/kb/en/")
    parser.add_argument("--output", default="./helpcenter-sitemap.json")
    parser.add_argument("--delay", type=float, default=0.3)
    parser.add_argument("--full-content", action="store_true")
    parser.add_argument("--max-content", type=int, default=10000)
    parser.add_argument("--summary-length", type=int, default=200)
    parser.add_argument("--include-release-notes", action="store_true")
    args = parser.parse_args()

    base_url = args.base_url.rstrip("/")

    # ----------------------------------------------------------------
    # Phase 1: Discover the global nav categories from the entry page.
    # These appear in the sidebar on EVERY page, so we need to know
    # them upfront to avoid treating them as subcategories later.
    # ----------------------------------------------------------------
    print(f"Phase 1: Discovering global nav from {base_url}{args.entry_path}")
    entry_soup = fetch_page(base_url + args.entry_path)
    global_categories, standalone_articles = extract_links(entry_soup)
    global_nav_paths = set(global_categories.keys())
    print(f"  Found {len(global_categories)} global nav categories, {len(standalone_articles)} standalone articles")

    # ----------------------------------------------------------------
    # Phase 2: BFS crawl. For each category page, collect articles and
    # find subcategory links that are NOT part of the global sidebar.
    # This correctly handles arbitrary nesting depth without the
    # runaway recursion problem.
    # ----------------------------------------------------------------
    print(f"\nPhase 2: Crawling all categories (BFS)...")

    all_articles = []
    seen_article_paths = set()
    seen_category_paths = set()

    # Add standalone articles from entry page
    for article in standalone_articles:
        if article["path"] not in seen_article_paths:
            seen_article_paths.add(article["path"])
            all_articles.append({
                "title": article["title"],
                "path": article["path"],
                "breadcrumb": ["Home"],
            })

    # BFS queue: (category_path, category_name, breadcrumb_list)
    queue = []
    for cat_path, cat_name in global_categories.items():
        queue.append((cat_path, cat_name, []))
        seen_category_paths.add(cat_path)

    while queue:
        cat_path, cat_name, parent_breadcrumb = queue.pop(0)
        current_breadcrumb = parent_breadcrumb + [cat_name]
        indent = "  " * len(parent_breadcrumb)

        print(f"{indent}Crawling: {cat_name}")

        try:
            soup = fetch_page(base_url + cat_path)
        except Exception as e:
            print(f"{indent}  Error: {e}")
            continue

        page_categories, page_articles = extract_links(soup)

        # Collect articles
        new_articles = 0
        for article in page_articles:
            if article["path"] not in seen_article_paths:
                seen_article_paths.add(article["path"])
                all_articles.append({
                    "title": article["title"],
                    "path": article["path"],
                    "breadcrumb": current_breadcrumb,
                })
                new_articles += 1

        # Find TRUE subcategories: category links on this page that are
        # NOT part of the global sidebar nav and haven't been seen yet.
        new_subcats = 0
        for sub_path, sub_name in page_categories.items():
            if (sub_path not in global_nav_paths
                    and sub_path not in seen_category_paths
                    and sub_path != cat_path):
                seen_category_paths.add(sub_path)
                queue.append((sub_path, sub_name, current_breadcrumb))
                new_subcats += 1

        print(f"{indent}  {new_articles} new articles, {new_subcats} subcategories")
        time.sleep(args.delay)

    print(f"\nTotal unique articles discovered: {len(all_articles)}")

    # ----------------------------------------------------------------
    # Phase 3: Optionally filter out release notes
    # ----------------------------------------------------------------
    if not args.include_release_notes:
        before = len(all_articles)
        all_articles = [a for a in all_articles
                        if not a["title"].lower().startswith("release notes")
                        and "announcement" not in a["title"].lower()]
        filtered = before - len(all_articles)
        if filtered:
            print(f"Filtered out {filtered} release notes/announcements ({len(all_articles)} remaining)")

    # ----------------------------------------------------------------
    # Phase 3: Fetch summaries (or full content) for each article
    # ----------------------------------------------------------------
    print(f"\nPhase 3: Fetching article {'content' if args.full_content else 'summaries'}...")
    results = []
    for i, article in enumerate(all_articles):
        print(f"  [{i+1}/{len(all_articles)}] {article['title']}")

        try:
            soup = fetch_page(base_url + article["path"])
            content = extract_content(soup)
        except Exception as e:
            content = ""
            print(f"    Error: {e}")

        entry = {
            "title": article["title"],
            "url": base_url + article["path"],
            "category": " > ".join(article["breadcrumb"]) if article["breadcrumb"] else "Uncategorized",
        }

        if args.full_content:
            if len(content) > args.max_content:
                content = content[:args.max_content] + "... [truncated]"
            entry["content"] = content
        else:
            summary = content[:args.summary_length].strip()
            if len(content) > args.summary_length:
                last_period = summary.rfind(".")
                last_space = summary.rfind(" ")
                if last_period > args.summary_length * 0.6:
                    summary = summary[:last_period + 1]
                elif last_space > 0:
                    summary = summary[:last_space] + "..."
                else:
                    summary += "..."
            entry["summary"] = summary

        results.append(entry)
        time.sleep(args.delay)

    # ----------------------------------------------------------------
    # Phase 4: Build category index and output
    # ----------------------------------------------------------------
    category_index = {}
    for article in results:
        cat = article["category"]
        if cat not in category_index:
            category_index[cat] = []
        category_index[cat].append(article["title"])

    sitemap = {
        "help_center": {
            "name": "DonorDock Help Center",
            "base_url": base_url,
            "scraped_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "total_articles": len(results),
            "total_categories": len(category_index),
            "format": "full" if args.full_content else "compact",
        },
        "category_index": category_index,
        "articles": results,
    }

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(sitemap, f, indent=2, ensure_ascii=False)

    file_size = len(json.dumps(sitemap, ensure_ascii=False))
    print(f"\nSitemap saved to: {args.output}")
    print(f"Total articles: {len(results)}")
    print(f"Total categories: {len(category_index)}")
    print(f"File size: {file_size:,} bytes ({file_size/1024:.1f} KB)")
    print(f"\nCategory breakdown:")
    for cat, titles in sorted(category_index.items()):
        print(f"  {cat}: {len(titles)} articles")


if __name__ == "__main__":
    main()
