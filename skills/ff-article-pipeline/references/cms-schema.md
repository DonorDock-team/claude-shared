# CMS Schema — Fetch from GitHub

This file is a pointer. The authoritative CMS schema lives in the GitHub repo and should be fetched fresh at the start of each pipeline run.

**Source:** `DonorDock-team/claude-shared` → `sitemaps/cms-schema.md`

Use the GitHub `get_file_contents` tool:
```
Owner: DonorDock-team
Repo: claude-shared
Path: sitemaps/cms-schema.md
```

The GitHub version contains all collection IDs, field schemas, tag/category IDs, author IDs, and the CMS item creation template. It is maintained as the single source of truth so that all skills and pipelines stay in sync when tags, categories, or authors are added or changed.

Also fetch this companion file for internal linking:
- `sitemaps/website-sitemap.json` — donordock.com page URLs
