---
name: donordock-helpcenter
description: >
  DonorDock Help Center knowledge base for answering product questions, troubleshooting,
  and guiding users through DonorDock features. Use this skill whenever someone asks
  "how do I do X in DonorDock", "where is the setting for Y", "can DonorDock do Z",
  or any question about DonorDock features, setup, configuration, integrations, imports,
  gifts, contacts, reports, boards, automations, emails, letters, text messages,
  online giving, templates, pledges, campaigns, appeals, funds, receipts, signup forms,
  activities, custom fields, or event tracking. Also trigger when someone asks about
  DonorDock billing, team management, Zapier integration, or API access.
  Even if the user doesn't say "DonorDock" explicitly, trigger this skill for any
  product support or feature question that clearly relates to the DonorDock platform.
---

# DonorDock Help Center Knowledge Base

Answer DonorDock product questions accurately by looking up the right help center article.

## Data Sources

1. **Sitemap JSON** — A compact index of 318+ help center articles with titles, URLs, category breadcrumbs, and ~200-char summaries. Stored in GitHub at `DonorDock-team/claude-shared` and updated regularly. (~148KB, compact format)
2. **Live article pages** — The actual help center at `https://helpcenter.donordock.com/kb/en/` for the most current information.

## Sitemap Format

The sitemap JSON has this structure:
```json
{
  "help_center": { "total_articles": 318, "format": "compact", ... },
  "category_index": { "Category > Subcategory": ["Article Title 1", ...] },
  "articles": [
    {
      "title": "Article Title",
      "url": "https://helpcenter.donordock.com/kb/guide/en/...",
      "category": "Topics > Contacts",
      "summary": "First ~200 chars of article content..."
    }
  ]
}
```

Key fields per article: `title`, `url`, `category` (breadcrumb path), `summary` (short snippet).
The `category_index` maps each category path to a list of article titles for quick lookup.

## Answering a Question

### Step 1: Fetch the sitemap index

Use the GitHub MCP server to read the sitemap:

```
get_file_contents from repo: DonorDock-team/claude-shared
path: sitemaps/helpcenter-sitemap.json
```

**Fallback methods** (in order):
1. Raw URL: `https://raw.githubusercontent.com/DonorDock-team/claude-shared/main/sitemaps/helpcenter-sitemap.json`
2. Browse the help center directly at `https://helpcenter.donordock.com/kb/en/`

### Step 2: Find the right article(s)

Search the sitemap by scanning article titles, categories, and summaries for relevance to the user's question.

**Use the `category_index` for fast lookup** — scan category names first to narrow down, then check article titles within matching categories.

Categories use breadcrumb paths (e.g., `Topics > Gifts`, `Topics > Integrations > Integration Builder Apps > Quickbooks`). Top-level categories include:

- **Getting Started** — Setup, onboarding, international support
- **Video Guides** — DonorDock 101 course, deep dive videos
- **Product Updates** — Feature release announcements
- **Topics > Contacts** — Donors, prospects, badges, marketing lists, households
- **Topics > Custom Fields** — Creating and using custom fields on contacts
- **Topics > Imports** — Bulk importing contacts, gifts, activities; migration guides (Raiser's Edge, Salsalabs, Mailchimp, GiftWorks, DonorBox, QuickBooks)
- **Topics > Gifts** — Donations, recurring gifts, soft credits, tribute gifts, gift tags, DAF tracking
- **Topics > Receipts** — Donation receipts, contribution statements
- **Topics > Pledges** — Pledge tracking and management
- **Topics > Campaigns Appeals And Funds** — Organizing transactions
- **Topics > Online Giving** — Giving pages, payment processors, DAFpay, Chariot
- **Topics > Reporting** — Reports, dashboards, mailing lists, filtering
- **Topics > Boards** — ActionBoard, AskBoard, ProjectBoard task management
- **Topics > Automations** — Triggers, steps, filters, journeys
- **Topics > Emails** — Email marketing, outreach, templates, statistics
- **Topics > Letters** — Bulk letters, receipts, labels
- **Topics > Text Messages** — Text-to-donate, bulk texting, text credits, A2P registration
- **Topics > Activities** — Phone calls, meetings, tasks, event attendance, volunteers, asks
- **Topics > Templates** — Email/letter templates, merge tags
- **Topics > Integrations** — Zapier, API keys, integration builder, Google Analytics
  - **... > Integration Builder Apps** — Subcategories for specific integrations (QuickBooks, OneCause, Mailchimp, etc.)
- **Topics > Signup Forms** — Signup form creation, embedding, RSVP lists
- **Topics > Settings** — Organization settings, team management, billing, user profiles, domain authentication
- **Topics > Event Tracking** — Tracking events in DonorDock

### Step 3: Provide the answer

The compact sitemap includes only summaries (~200 chars each), not full article content. Use this workflow:

1. **Find matching articles** by title/category/summary in the sitemap
2. **If the summary is sufficient** to answer the question, answer directly and link the article
3. **If more detail is needed**, use WebFetch to load the specific article URL for the full content

Always include a source link to the relevant help center article(s) at the end of the answer.

### Format

- Answer in clear, concise language
- Include step-by-step instructions for "how do I..." questions
- Link to the specific article URL(s) used
- Reference multiple articles if relevant
- If no article covers the topic, say so and suggest contacting DonorDock support

---

## Updating the Sitemap

When asked to refresh or update the help center sitemap:

### Option A: Full re-scrape (comprehensive)

Always pull the scraper from the GitHub repo (never use a local copy -- the repo is the single source of truth):

```bash
curl -sO https://raw.githubusercontent.com/DonorDock-team/claude-shared/main/scripts/scrape-stonly-helpcenter.py
pip install requests beautifulsoup4 --break-system-packages -q
python scrape-stonly-helpcenter.py --output helpcenter-sitemap.json
```

The scraper uses BFS crawling with global nav filtering to discover articles at any nesting depth. Default output is compact format (title + URL + category + summary). Use `--full-content` flag for full article text (much larger output).

Then push the updated sitemap to GitHub:

```
push_files to repo: DonorDock-team/claude-shared
branch: main
files: [{ path: "sitemaps/helpcenter-sitemap.json", content: [file contents] }]
message: "Weekly helpcenter sitemap refresh - [DATE] - [ARTICLE_COUNT] articles"
```

### Option B: Targeted update (single article)

If only specific articles changed, fetch the sitemap via GitHub MCP, update the relevant entries, and push back:

1. Read current sitemap via `get_file_contents` from `DonorDock-team/claude-shared` → `sitemaps/helpcenter-sitemap.json`
2. Fetch the updated article(s) via WebFetch from their help center URLs
3. Replace the matching entries in the JSON
4. Write back via `push_files` with an appropriate commit message
