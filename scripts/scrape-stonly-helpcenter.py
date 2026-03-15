#!/usr/bin/env python3
"""
Reusable Stonly Help Center Scraper
====================================
Crawls a Stonly-hosted help center, discovers all categories and articles,
extracts full text content, and outputs a structured JSON sitemap.

Usage:
    python scrape-stonly-helpcenter.py [OPTIONS]

Options:
    --base-url URL      Base URL of the help center (default: https://helpcenter.donordock.com)
    --entry-path PATH   Entry path to start crawling (default: /kb/en/)
    --output FILE       Output JSON file path (default: ./helpcenter-sitemap.json)
    --delay SECONDS     Delay between requests in seconds (default: 0.3)
    --max-content INT   Max content chars per article before truncation (default: 10000)
    --no-content        Only extract titles/URLs/categories, skip full content

This scraper is designed for Stonly-hosted help centers but can work with
similar knowledge base platforms that use category → article URL structures.

The output JSON structure:
{
    "help_center": { metadata },
    "category_index": { category → [articles] },
    "articles": [ { title, category, url, path, content, content_length } ]
}

Skills and plugins can fetch this JSON from a shared URL (e.g., GitHub raw)
to answer product questions without having to crawl the site each time.
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


def discover_categories(base_url, entry_path):
    """Crawl the main page and discover all category URLs."""
    url = base_url + entry_path
    print(f"Discovering categories from {url}")
    resp = requests.get(url, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    categories = {}
    for link in soup.find_all("a", href=True):
        href = link["href"]
        text = link.get_text(strip=True)
        # Category pages: /kb/en/category-name-123456
        if re.match(r"^/kb/en/[\w-]+-\d+$", href) and text:
            categories[text] = href
        # Standalone guide pages in nav
        elif re.match(r"^/kb/guide/en/", href) and text:
            categories.setdefault("__standalone__", [])
            categories["__standalone__"].append({"title": text, "path": href})

    print(f"  Found {len(categories)} categories")
    return categories


def discover_articles_in_category(base_url, category_name, category_path):
    """Crawl a category page and find all article links."""
    url = base_url + category_path
    print(f"  Crawling category: {category_name}")
    resp = requests.get(url, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    articles = []
    seen = set()
    for link in soup.find_all("a", href=True):
        href = link["href"]
        text = link.get_text(strip=True)
        # Article pages: /kb/guide/en/article-slug-ID/Steps/STEPID
        if re.match(r"^/kb/guide/en/[\w-]+/Steps/\d+$", href) and text and href not in seen:
            seen.add(href)
            articles.append({"title": text, "path": href})

    # Also check for subcategory links and crawl them
    for link in soup.find_all("a", href=True):
        href = link["href"]
        text = link.get_text(strip=True)
        if re.match(r"^/kb/en/[\w-]+-\d+$", href) and text and href != category_path:
            sub_url = base_url + href
            try:
                sub_resp = requests.get(sub_url, headers=HEADERS, timeout=15)
                sub_soup = BeautifulSoup(sub_resp.text, "html.parser")
                for sub_link in sub_soup.find_all("a", href=True):
                    sub_href = sub_link["href"]
                    sub_text = sub_link.get_text(strip=True)
                    if re.match(r"^/kb/guide/en/[\w-]+/Steps/\d+$", sub_href) and sub_text and sub_href not in seen:
                        seen.add(sub_href)
                        articles.append({"title": sub_text, "path": sub_href})
                time.sleep(0.2)
            except Exception:
                pass

    print(f"    Found {len(articles)} articles")
    return articles


def extract_content(base_url, path, max_content=10000):
    """Fetch an article page and extract the main text content."""
    url = base_url + path
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        # Remove non-content elements
        for tag in soup(["script", "style", "nav", "footer", "header"]):
            tag.decompose()

        # Try to find the main content area
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

        # Get text, clean up
        text = content_area.get_text(separator="\n", strip=True)
        lines = [line.strip() for line in text.split("\n") if line.strip()]
        text = "\n".join(lines)

        if len(text) > max_content:
            text = text[:max_content] + "... [content truncated]"

        return text
    except Exception as e:
        return f"[Error fetching content: {str(e)}]"


def main():
    parser = argparse.ArgumentParser(description="Scrape a Stonly help center into a JSON sitemap")
    parser.add_argument("--base-url", default="https://helpcenter.donordock.com",
                        help="Base URL of the help center")
    parser.add_argument("--entry-path", default="/kb/en/",
                        help="Entry path to start crawling")
    parser.add_argument("--output", default="./helpcenter-sitemap.json",
                        help="Output JSON file path")
    parser.add_argument("--delay", type=float, default=0.3,
                        help="Delay between requests in seconds")
    parser.add_argument("--max-content", type=int, default=10000,
                        help="Max content chars per article before truncation")
    parser.add_argument("--no-content", action="store_true",
                        help="Only extract titles/URLs/categories, skip full content")
    args = parser.parse_args()

    base_url = args.base_url.rstrip("/")

    # Phase 1: Discover categories
    categories = discover_categories(base_url, args.entry_path)

    # Phase 2: Discover articles in each category
    all_articles = []
    seen_paths = set()

    for cat_name, cat_path in categories.items():
        if cat_name == "__standalone__":
            # These are direct guide links from the main page
            for article in cat_path:
                if article["path"] not in seen_paths:
                    seen_paths.add(article["path"])
                    all_articles.append({
                        "category": "General",
                        "title": article["title"],
                        "path": article["path"],
                    })
            continue

        articles = discover_articles_in_category(base_url, cat_name, cat_path)
        for article in articles:
            if article["path"] not in seen_paths:
                seen_paths.add(article["path"])
                all_articles.append({
                    "category": cat_name,
                    "title": article["title"],
                    "path": article["path"],
                })
        time.sleep(args.delay)

    print(f"\nTotal unique articles discovered: {len(all_articles)}")

    # Phase 3: Extract content from each article
    results = []
    for i, article in enumerate(all_articles):
        if args.no_content:
            content = ""
            content_length = 0
        else:
            print(f"[{i+1}/{len(all_articles)}] Scraping: {article['title']}")
            content = extract_content(base_url, article["path"], args.max_content)
            content_length = len(content)
            time.sleep(args.delay)

        results.append({
            "title": article["title"],
            "category": article["category"],
            "url": base_url + article["path"],
            "path": article["path"],
            "content": content,
            "content_length": content_length,
        })

    # Phase 4: Build the sitemap JSON
    category_index = {}
    for article in results:
        cat = article["category"]
        if cat not in category_index:
            category_index[cat] = []
        category_index[cat].append({
            "title": article["title"],
            "url": article["url"],
        })

    sitemap = {
        "help_center": {
            "name": f"{base_url} Help Center",
            "base_url": base_url,
            "scraped_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "total_articles": len(results),
            "categories": list(category_index.keys()),
        },
        "category_index": category_index,
        "articles": results,
    }

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(sitemap, f, indent=2, ensure_ascii=False)

    print(f"\nSitemap saved to: {args.output}")
    print(f"Total articles: {len(results)}")
    print(f"Categories: {len(category_index)}")
    for cat, arts in category_index.items():
        print(f"  {cat}: {len(arts)} articles")


if __name__ == "__main__":
    main()
