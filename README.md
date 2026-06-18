# DonorDock Claude Shared (Public)

Non-sensitive, **render-on-open** files used by Claude across the DonorDock team — brand assets, sitemaps, reusable scrapers, templates, and public web pages. Any team member's Claude can read these anonymously.

> **Sensitive content moved.** SEO brain, sales enablement, reports, skill master copies, config, and internal HTML (data-moat doc, dashboard) now live in the **private** repo `DonorDock-team/claude-private` — read it with authentication (`gh`/GitHub MCP locally, or the GitHub connector in cloud Team Claude). See `Projects/Repo-Privatization/` in the marketing workspace for the full map.

## How it works
- **Public repo** — no auth needed for reads; any Claude session or browser can fetch files instantly.
- **Base URL:** `https://raw.githubusercontent.com/DonorDock-team/claude-shared/main/`
- Example: `curl -s "https://raw.githubusercontent.com/DonorDock-team/claude-shared/main/sitemaps/website-sitemap.json"`

## What's here
```
├── assets/        ← Brand assets — logos (DonorDock + Otto), Silka fonts, icons, images
│                    (kept public so branded HTML/PDFs render on open for clients & board)
├── sitemaps/      ← website-sitemap.json, helpcenter-sitemap.json (+summaries),
│                    youtube-catalog.json, cms-schema.md — auto-updated weekly
├── scripts/       ← Reusable scrapers (read API keys from env vars; no secrets committed)
├── templates/     ← Email + Webflow templates
├── reference/     ← Shared reference data
└── docs/          ← GitHub Pages (public): gfmp-academy/ (GoFundMe Pro Academy microsite)
```
Served Pages: `https://donordock-team.github.io/claude-shared/gfmp-academy/`

## Writing back (requires auth)
Automation that refreshes the sitemaps uses the authenticated `gh` CLI / GitHub API. Example:
```bash
gh api repos/DonorDock-team/claude-shared/contents/sitemaps/website-sitemap.json --jq '.path'
```

## Conventions
- **Filenames:** lowercase, kebab-case.
- **One topic per file**; `.md` files start with a 1–2 sentence summary.
- **No secrets, ever** — this is a public repo. API keys/tokens belong in environment variables or a secret manager, **never** in a file here. (Anything sensitive goes in `claude-private`, not here.)
