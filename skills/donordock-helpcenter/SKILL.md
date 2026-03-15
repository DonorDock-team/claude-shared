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

1. **Sitemap JSON** — A structured index of all 134+ help center articles with titles, categories, URLs, and full extracted content. Hosted on GitHub and updated weekly.
2. **Live article pages** — The actual help center at `https://helpcenter.donordock.com/kb/en/` for the most current information.

## Answering a Question

### Step 1: Fetch the sitemap index

Fetch the sitemap JSON from GitHub:

```
https://raw.githubusercontent.com/DonorDock-team/claude-shared/main/sitemaps/helpcenter-sitemap.json
```

Use WebFetch or curl to retrieve it. If unavailable, fall back to browsing the help center directly at `https://helpcenter.donordock.com/kb/en/`.

### Step 2: Find the right article(s)

Search the sitemap by scanning article titles and categories for relevance to the user's question. Categories include:

- **Getting Started** — Setup, onboarding, international support
- **Contacts** — Donors, prospects, badges, marketing lists, households
- **Custom Fields** — Creating and using custom fields on contacts
- **Imports** — Bulk importing contacts, gifts, activities
- **Gifts** — Donations, recurring gifts, soft credits, tribute gifts, gift tags
- **Receipts** — Donation receipts, contribution statements
- **Pledges** — Pledge tracking and management
- **Campaigns, Appeals, and Funds** — Organizing transactions
- **Online Giving** — Giving pages, payment processors, DAFpay
- **Reporting** — Reports, dashboards, mailing lists, filtering
- **Boards** — ActionBoard, AskBoard, ProjectBoard task management
- **Automations** — Triggers, steps, filters, journeys
- **Emails** — Email marketing, outreach, templates, statistics
- **Letters** — Bulk letters, receipts, labels
- **Text Messages** — Text-to-donate, bulk texting, text credits, A2P registration
- **Activities** — Phone calls, meetings, tasks, event attendance, volunteers, asks
- **Templates** — Email/letter templates, merge tags
- **Integrations** — Zapier, API keys, integration builder, Google Analytics
- **Signup Forms** — Signup form creation, embedding, RSVP lists
- **Settings** — Organization settings, team management, billing, user profiles
- **Event Tracking** — Tracking events in DonorDock
- **Video Guides** — DonorDock 101 course, deep dive videos

### Step 3: Provide the answer

If the sitemap content is sufficient, answer directly from it. If more detail is needed, use WebFetch to load the specific article URL for the most current version.

Always include a source link to the relevant help center article(s) at the end of the answer.

### Format

- Answer in clear, concise language
- Include step-by-step instructions for "how do I..." questions
- Link to the specific article URL(s) used
- Reference multiple articles if relevant
- If no article covers the topic, say so and suggest contacting DonorDock support
