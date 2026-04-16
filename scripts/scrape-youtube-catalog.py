#!/usr/bin/env python3
"""
DonorDock YouTube Catalog Scraper
==================================
Enumerates every upload from @donordock and @FundraisingLab via the
YouTube Data API v3, plus known external appearances, and outputs a
structured JSON catalog optimized for LLM context windows.

Uses the channel's "uploads" playlist (via contentDetails.relatedPlaylists)
which is the only reliable way to get EVERY video from a channel. Keyword
searches miss videos; uploads playlists do not.

Designed to run on a weekly schedule to keep the shared content registry
up to date. Output goes to DonorDock-team/claude-shared sitemaps/.

Usage:
    python scrape-youtube-catalog.py [OPTIONS]

Environment:
    YOUTUBE_API_KEY    Required. YouTube Data API v3 key.

Options:
    --output FILE      Output file (default: ./youtube-catalog.json)
    --handles LIST     Comma-separated channel handles (default: donordock,FundraisingLab)
    --external FILE    Optional JSON file with external appearance video IDs to include
    --timeout INT      Per-request timeout in seconds (default: 15)
"""

import argparse
import json
import os
import re
import sys
import time
from datetime import datetime, timezone

try:
    import requests
except ImportError:
    print("Missing dependency. Install with:")
    print("  pip install requests --break-system-packages")
    sys.exit(1)

API_BASE = "https://www.googleapis.com/youtube/v3"

CHANNEL_CLASS = {
    "donordock": "donordock",
    "donordockinfo": "donordock",
    "fundraisinglab": "fundraisinglab",
}

KNOWN_PEOPLE = [
    "Rob Burke",
    "Bridgette Foust",
    "Matt Bitzegaio",
]

# Known external appearance video IDs (guest podcasts, conference talks, etc.)
# Kept here as a baseline; --external can extend this list.
DEFAULT_EXTERNAL_IDS = []


def iso8601_duration_to_seconds(duration: str) -> int:
    """Convert ISO 8601 duration (PT1H2M3S) to seconds."""
    if not duration:
        return 0
    m = re.match(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", duration)
    if not m:
        return 0
    h, mm, s = m.groups()
    return int(h or 0) * 3600 + int(mm or 0) * 60 + int(s or 0)


def classify_category(title: str, description: str, channel: str) -> str:
    """Infer category from title/description/channel."""
    text = f"{title} {description}".lower()

    # Focused Fundraiser podcast content
    if "focused fundraiser" in text or "ff podcast" in text:
        return "the-focused-fundraiser"
    if channel == "fundraisinglab":
        # Fundraising Lab channel is primarily the podcast
        return "the-focused-fundraiser"

    # Feature highlights / product demos
    if any(kw in text for kw in ["feature", "demo", "release", "what's new", "whats new", "product update", "new in donordock"]):
        return "feature-highlight"

    # Testimonials
    if any(kw in text for kw in ["testimonial", "success story", "customer story", "case study"]):
        return "testimonial"

    # Training / how-to
    if any(kw in text for kw in ["how to", "how-to", "tutorial", "walkthrough", "guide", "training", "setup"]):
        return "training"

    return "other"


def tag_people(title: str, description: str) -> list:
    """Find known people mentioned in title or description."""
    text = f"{title} {description}"
    found = []
    for person in KNOWN_PEOPLE:
        if person.lower() in text.lower():
            found.append(person)
    return found


def api_get(path: str, params: dict, api_key: str, timeout: int = 15) -> dict:
    """Make an authenticated GET request to the YouTube Data API."""
    params = {**params, "key": api_key}
    url = f"{API_BASE}/{path}"
    resp = requests.get(url, params=params, timeout=timeout)
    if resp.status_code != 200:
        raise RuntimeError(f"API error {resp.status_code} on {path}: {resp.text[:500]}")
    return resp.json()


def resolve_channel(handle: str, api_key: str, timeout: int) -> dict:
    """
    Resolve a @handle to channel metadata including the uploads playlist ID.
    Returns {"id", "title", "uploads_playlist_id", "handle"} or None.
    """
    # forHandle accepts with or without @
    clean = handle.lstrip("@")
    data = api_get("channels", {
        "part": "snippet,contentDetails",
        "forHandle": f"@{clean}",
    }, api_key, timeout)
    items = data.get("items", [])
    if not items:
        return None
    ch = items[0]
    return {
        "id": ch["id"],
        "title": ch["snippet"]["title"],
        "handle": f"@{clean}",
        "uploads_playlist_id": ch["contentDetails"]["relatedPlaylists"]["uploads"],
    }


def fetch_playlist_video_ids(playlist_id: str, api_key: str, timeout: int) -> list:
    """Page through a playlist and return all video IDs."""
    ids = []
    page_token = None
    while True:
        params = {
            "part": "contentDetails",
            "playlistId": playlist_id,
            "maxResults": 50,
        }
        if page_token:
            params["pageToken"] = page_token
        data = api_get("playlistItems", params, api_key, timeout)
        for item in data.get("items", []):
            vid = item.get("contentDetails", {}).get("videoId")
            if vid:
                ids.append(vid)
        page_token = data.get("nextPageToken")
        if not page_token:
            break
    return ids


def fetch_video_details(video_ids: list, api_key: str, timeout: int) -> list:
    """Fetch full video details in batches of 50."""
    details = []
    for i in range(0, len(video_ids), 50):
        batch = video_ids[i:i + 50]
        data = api_get("videos", {
            "part": "snippet,contentDetails,statistics",
            "id": ",".join(batch),
        }, api_key, timeout)
        details.extend(data.get("items", []))
    return details


def classify_channel(channel_title: str) -> str:
    """Map a channel title to our channel classification."""
    t = channel_title.lower().replace(" ", "")
    for key, val in CHANNEL_CLASS.items():
        if key in t:
            return val
    return "external"


def build_video_record(video: dict, channel_classification: str = None) -> dict:
    """Transform a raw API video object into our catalog schema."""
    snippet = video["snippet"]
    content_details = video["contentDetails"]
    vid = video["id"]

    duration_s = iso8601_duration_to_seconds(content_details.get("duration"))
    title = snippet.get("title", "")
    description = snippet.get("description", "")
    channel_title = snippet.get("channelTitle", "")

    channel = channel_classification or classify_channel(channel_title)

    thumb = (
        snippet.get("thumbnails", {}).get("high", {}).get("url")
        or snippet.get("thumbnails", {}).get("default", {}).get("url")
        or f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg"
    )

    record = {
        "id": vid,
        "title": title,
        "description": description[:200],
        "channel": channel,
        "published_at": snippet.get("publishedAt"),
        "type": "short" if duration_s and duration_s < 61 else "video",
        "duration_seconds": duration_s,
        "category": classify_category(title, description, channel),
        "people": tag_people(title, description),
        "url": f"https://www.youtube.com/watch?v={vid}",
        "thumbnail": thumb,
    }

    if channel == "external":
        record["external_channel"] = channel_title

    return record


def main():
    parser = argparse.ArgumentParser(description="Scrape DonorDock YouTube catalog via YouTube Data API v3")
    parser.add_argument("--output", default="./youtube-catalog.json")
    parser.add_argument("--handles", default="donordock,FundraisingLab")
    parser.add_argument("--external", default=None, help="Optional JSON file with list of external video IDs")
    parser.add_argument("--timeout", type=int, default=15)
    args = parser.parse_args()

    api_key = os.environ.get("YOUTUBE_API_KEY")
    if not api_key:
        print("ERROR: YOUTUBE_API_KEY environment variable is not set.", file=sys.stderr)
        sys.exit(1)

    handles = [h.strip() for h in args.handles.split(",") if h.strip()]

    # Phase 1: Resolve channels
    print(f"[1/4] Resolving {len(handles)} channel(s)...")
    channels = {}
    for handle in handles:
        ch = resolve_channel(handle, api_key, args.timeout)
        if not ch:
            print(f"  WARN: Could not resolve {handle}")
            continue
        channels[handle] = ch
        print(f"  {ch['handle']} -> {ch['title']} (uploads: {ch['uploads_playlist_id']})")

    # Phase 2: Enumerate upload playlists
    print(f"[2/4] Enumerating uploads...")
    video_ids_by_channel = {}
    all_ids = set()
    for handle, ch in channels.items():
        ids = fetch_playlist_video_ids(ch["uploads_playlist_id"], api_key, args.timeout)
        video_ids_by_channel[handle] = ids
        all_ids.update(ids)
        print(f"  {ch['handle']}: {len(ids)} videos")

    # Phase 3: Add external videos
    external_ids = list(DEFAULT_EXTERNAL_IDS)
    if args.external and os.path.exists(args.external):
        with open(args.external) as f:
            data = json.load(f)
            if isinstance(data, list):
                external_ids.extend(data)
            elif isinstance(data, dict) and "external_ids" in data:
                external_ids.extend(data["external_ids"])
    external_ids = [i for i in external_ids if i not in all_ids]
    all_ids.update(external_ids)
    print(f"[3/4] External appearances: {len(external_ids)} extra videos")

    # Phase 4: Fetch full details for every video
    print(f"[4/4] Fetching details for {len(all_ids)} videos...")
    details = fetch_video_details(list(all_ids), api_key, args.timeout)

    videos = []
    for v in details:
        # Override channel classification for external IDs
        if v["id"] in external_ids:
            record = build_video_record(v, channel_classification="external")
        else:
            record = build_video_record(v)
        videos.append(record)

    # Sort newest first
    videos.sort(key=lambda x: x["published_at"] or "", reverse=True)

    # Channel totals
    by_channel = {"donordock": 0, "fundraisinglab": 0, "external": 0}
    for v in videos:
        by_channel[v["channel"]] = by_channel.get(v["channel"], 0) + 1

    # Build final JSON
    output = {
        "youtube": {
            "scraped_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            "total_videos": len(videos),
            "channels": {
                "donordock": {
                    "name": "DonorDock",
                    "handle": "@donordock",
                    "url": "https://www.youtube.com/@donordock",
                    "video_count": by_channel["donordock"],
                },
                "fundraisinglab": {
                    "name": "Fundraising Lab",
                    "handle": "@FundraisingLab",
                    "url": "https://www.youtube.com/@FundraisingLab",
                    "video_count": by_channel["fundraisinglab"],
                },
                "external": {
                    "name": "External appearances",
                    "video_count": by_channel["external"],
                },
            },
            "categories": [
                "the-focused-fundraiser",
                "training",
                "feature-highlight",
                "testimonial",
                "shorts",
                "other",
            ],
            "people": KNOWN_PEOPLE,
        },
        "videos": videos,
    }

    with open(args.output, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    # Summary
    shorts = sum(1 for v in videos if v["type"] == "short")
    long_form = len(videos) - shorts
    size_kb = os.path.getsize(args.output) / 1024
    print("")
    print(f"Done. Wrote {args.output}")
    print(f"  Total: {len(videos)} videos ({long_form} long-form, {shorts} shorts)")
    print(f"  DonorDock: {by_channel['donordock']}")
    print(f"  Fundraising Lab: {by_channel['fundraisinglab']}")
    print(f"  External: {by_channel['external']}")
    print(f"  File size: {size_kb:.1f} KB")


if __name__ == "__main__":
    main()
