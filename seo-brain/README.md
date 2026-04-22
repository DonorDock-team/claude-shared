# DonorDock SEO Brain

Central strategic + observational layer for DonorDock's SEO and AEO program. This folder is the source of truth for:

- **Strategy** — what we are deliberately going after (pillars, keywords, AEO questions, ICP intent, competitor posture)
- **State** — what is actually happening (audits, rankings, AI citations, content inventory enrichment)
- **Proactive intelligence** — recommended next actions (monthly opportunities)
- **Integration surface** — other skills and scheduled tasks read from here to stay aligned

**Owner:** Rob Burke (CMO, rburke@donordock.com)
**Model:** Human-curated strategy. Machine-observed state. Claude-synthesized opportunities.

---

## Architecture

Four separated concerns, each with its own cadence:

| Layer | Cadence | Writer |
|---|---|---|
| Strategy | Quarterly review / as-needed | Human (Rob approves) |
| State | Daily / weekly / monthly | Automated + Claude Rank |
| Proactive | Monthly | Strategist skill |
| Integration | Read-only | Other skills |

## Folder map

```
seo-brain/
├── strategy/              Human-curated. Slow-changing. Approved by Rob.
├── audits/                Dated snapshots. Appended, never overwritten.
├── tracking/              Time-series observations (SERP, AI citations).
├── registry-enrichment/   SEO metadata layered over sitemaps/website-sitemap.json.
├── opportunities/         Monthly content opportunity reports.
└── dashboard/             Generated HTML dashboard (static site).
```

## How this connects to other systems

| System | Relationship |
|---|---|
| `sitemaps/website-sitemap.json` | URL source of truth (already in claude-shared). seo-brain enriches each URL but does not duplicate. |
| `donordock-brand-identity` skill | SEO subagents load `strategy/` at session start. (Update in Phase 4.) |
| `ff-article-pipeline` skill | Loads `strategy/` before drafting; validates post-draft. (Update in Phase 4.) |
| `donordock-seo-strategist` skill (Phase 3) | Reads this folder, answers strategic questions, runs monthly opportunity report. |
| Claude Rank suite | Audits run against the live site; output written to `audits/`. |
| Asana | Strategist skill creates tasks for approvals and recommendations. (Phase 8.) |

## Build phases

| Phase | Status | Description |
|---|---|---|
| 0 | Complete | Repo scaffold + architecture README |
| 1 | Pending | Baseline comprehensive audit |
| 2 | Pending | Strategy documents |
| 3 | Pending | Strategist skill + proactive intelligence |
| 4 | Pending | Content creation integration (brand-identity + ff-article-pipeline updates) |
| 5 | Pending | AI citation tracking (daily priority + weekly full) |
| 6 | Pending | Scheduled automation |
| 7 | Pending | HTML dashboard |
| 8 | Pending | Asana integration |

## Conventions

- **Strategy docs** — versioned via git history, never date-suffixed. Changes require commit message format: `strategy: <what> — approved by Rob <YYYY-MM-DD>`
- **Audits and tracking** — dated filenames (`YYYY-MM.md`, `YYYY-WW.json`, `YYYY-MM-DD.json`)
- **Append-only** — audit snapshots are never overwritten; they are the historical record

## Competitors tracked

**Primary (confirmed):**
- DonorPerfect
- Bloomerang
- Network for Good
- Givebutter
- Neon One

**Secondary (pending final confirmation in Phase 1):**
- Little Green Light
- Virtuous
- Keela

## Existing scheduled tasks that interact with this folder

- `website-sitemap-update` — Fridays 10:09 AM CT (feeds registry-enrichment cross-references)
- `youtube-catalog-update` — Fridays 11:03 AM CT

New scheduled tasks added in Phase 6 will run at other times to avoid contention.
