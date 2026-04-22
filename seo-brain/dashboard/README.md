# Dashboard

Static HTML dashboard generated weekly from this folder's data.

## Deployment

GitHub Pages or embedded iframe in Webflow — decided in Phase 7.

## Views

| View | Source data |
|---|---|
| Overview | `audits/` + `tracking/` — traffic, rank movement, AI citations, content output |
| Pillar health | `strategy/pillars.md` + `registry-enrichment/` — coverage, traffic, gaps per pillar |
| Keyword cluster map | `strategy/keyword-universe.md` — D3 force graph |
| Article-to-pillar hierarchy | `registry-enrichment/` — tree |
| Internal link density | `registry-enrichment/` — heatmap |
| Competitor delta | `audits/*/competitors/` + `tracking/ai-citations/` — share-of-voice changes |
| Alert stream | Weekly diffs — rank drops, AI citation gains/losses, validation failures |

## Generator

`scripts/generate-seo-dashboard.py` (Phase 7). Pulls from:
- `audits/` (latest monthly)
- `tracking/` (all time-series)
- `strategy/` (pillar and keyword context)
- `registry-enrichment/url-enrichment.json`
- `sitemaps/website-sitemap.json` (via claude-shared root)

## Audience

- Primary: Rob (CMO)
- Secondary: exec team (leadership reviews)
