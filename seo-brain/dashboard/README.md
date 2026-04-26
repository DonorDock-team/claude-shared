# SEO Brain Dashboard

Single-page HTML dashboard for the DonorDock SEO/AEO/GEO tracking system. Reads live from `claude-shared` via the GitHub raw URL — no build, no host, no auth needed for read-only views.

## Three ways to open it

1. **Local file** — clone `claude-shared`, open `seo-brain/dashboard/index.html` in any browser. Always shows latest data because it fetches from `raw.githubusercontent.com` on every refresh.

2. **Bookmark the raw URL** — paste this into a browser bookmark and open with a single click:
   ```
   https://raw.githubusercontent.com/DonorDock-team/claude-shared/main/seo-brain/dashboard/index.html
   ```
   ⚠️ GitHub serves raw HTML as `text/plain` so the page won't render. Use option 1 (local file) or option 3 (CDN proxy).

3. **CDN proxy** (renders the HTML correctly):
   ```
   https://cdn.jsdelivr.net/gh/DonorDock-team/claude-shared@main/seo-brain/dashboard/index.html
   ```
   Public CDN, free, refreshes on every commit to main (12hr cache).

## Tabs

### Citations
- Latest run date + filter (top-50 / full)
- Aggregate DonorDock citation rate vs prior week (with delta)
- Per-engine breakdown table (runs, OK, hits, citation %, cost)
- Competitor mention counter
- Drill-down hint pointing at the per-prompt JSON

### Pillar Health
- Backfill progress bar (X of 290 articles)
- 7 pillar cards each showing article count + URL link
- Reads from `seo-brain/backfill/pillar-snapshot.json` (maintained by backfill batch writers)

### Prompt Editor
- Filter + search across all 150 prompts
- Inline edit: text, pillar, priority, active/AIO toggles
- Add new prompt (auto-IDs as next P-number)
- **Save flow:**
  - With PAT (set once in Settings → stored in localStorage): "Open PR via GitHub API" creates a branch, commits the new prompts.json, opens a PR, and pops it open in a new tab
  - Without PAT: "Download JSON" gives you the new file to commit manually via GitHub web UI

### Opportunities
- Renders the latest `seo-brain/opportunities/{YYYY-MM}.md` inline
- Updated monthly by the `monthly-opportunity-report` scheduled task

## Authentication (prompt editor only)

Set a GitHub Personal Access Token via the ⚙ Settings button.

**Required scope:** `repo` on `DonorDock-team/claude-shared`

The PAT is stored only in this browser's `localStorage` under key `dd-dashboard-pat`. Never transmitted anywhere except `api.github.com`. To clear: Settings → Clear, or open DevTools → Application → Local Storage and delete the key.

For fine-grained PATs (recommended), scope to:
- Repository: `DonorDock-team/claude-shared`
- Permissions: Contents (read+write), Pull requests (write)

## Why no build step?

Single HTML file, vanilla JS, no dependencies. Total weight ~30KB. Loads from raw GitHub directly. The whole dashboard is greppable and editable in any text editor. If you want to add a chart library or framework later, swap the `<script>` for whatever you want — the data fetches and state model are simple enough to port.

## Data sources

| Tab | Source path |
|---|---|
| Citations | `seo-brain/tracking/ai-citations/{YYYY-MM-DD}/_summary.json` (probes today + 14 days back) |
| Pillar Health | `seo-brain/backfill/pillar-snapshot.json` (with hardcoded fallback) |
| Prompt Editor | `seo-brain/tracking/prompts.json` |
| Opportunities | `seo-brain/opportunities/{YYYY-MM}.md` (probes current + 6 months back) |

## Refresh behavior

Dashboard appends `?t={timestamp}` cache-buster to every fetch. GitHub's raw URL CDN has a 5-minute cache; the cache-buster ensures you always see the latest committed state.

Click the **↻ Refresh** button in the header to force-reload all 4 tabs.

## Roadmap

- v1.1 — Charts: 12-week trend line for citation rate per engine
- v1.2 — GSC overlay on pillar health (impressions, CTR, position per pillar URL)
- v1.3 — Citation drill-down view (click a prompt → see all 4 engines' responses inline)
- v1.4 — Asana integration: click "Open task" on a missed-citation prompt to spawn a content task in Asana

## Known limits

- The 14-day probe for latest citation data is wasteful — Phase 8 will add a `latest.json` pointer maintained by the runner to find the latest run in one fetch.
- Rendering 150 rows in the prompt editor with `<textarea>` per row is intentional; if the bank grows past 500 the table will need virtualization.
- The Opportunities tab renders Markdown as preformatted text. Phase 7.1 will add a real Markdown renderer (likely `marked` from CDN).
