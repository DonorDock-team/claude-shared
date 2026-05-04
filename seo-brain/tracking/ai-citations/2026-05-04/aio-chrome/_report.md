# Google AI Overviews Citation Report — 2026-05-04

**Method:** Chrome MCP (Rob's logged-in browser) querying Google search and parsing AI Overview panels.
**Prompts run:** 86 AIO-eligible prompts from `seo-brain/tracking/prompts.json`
**Pacing:** ~17–25 seconds between queries

## Headline numbers

| Metric | Value |
|---|---|
| AIO render rate | **84/86 (97.7%)** |
| DonorDock cited (when AIO present) | **40/84 (47.6%)** |
| CAPTCHA / bot-detection hits | 0 |
| Average AIO panel length | ~2,500 chars |

Two prompts returned no AIO panel: P030 (Donor management software with the best customer support), P048 (Donor CRM for nonprofits outgrowing their current tools).

## Top competitors cited in AIO panels

| Rank | Competitor | AIO citations |
|---|---|---|
| 1 | Bloomerang | 46 |
| 2 | DonorPerfect | 41 |
| 3 | Givebutter | 37 |
| 4 | Little Green Light | 25 |
| 5 | Neon CRM | 21 |
| 5 | Virtuous | 21 |
| 7 | Blackbaud | 18 |
| 8 | Raiser's Edge | 16 |
| 9 | Salesforce Nonprofit Cloud | 13 |
| 9 | Bonterra | 13 |

Bloomerang and DonorPerfect dominate Google AIO citations across the prompt bank.

## Top 5 prompts where AIO cites competitors but not DonorDock

These are the highest-leverage gaps to close — Google IS rendering AIO for these queries, AND it's pulling in 8–10 competitors per panel, but DonorDock is absent.

1. **P021 — Best Bloomerang alternatives** (10 competitors cited, no DonorDock)
2. **P019 — Alternative to Blackbaud Raisers Edge** (9 competitors)
3. **P020 — Cheaper alternative to Blackbaud** (9 competitors)
4. **P052 — Best CRM for a new development director** (9 competitors)
5. **P016 — Alternative to DonorPerfect** (8 competitors)

## Where DonorDock IS winning (strong AIO citations)

- **Branded queries** (P001–P004): "What is DonorDock", "Is DonorDock good", "DonorDock reviews", "DonorDock pricing" — DonorDock cited and dominant.
- **Versus queries** (P005–P014): Almost every "DonorDock vs X" prompt cites DonorDock.
- **P051 Best donor CRM for lean fundraising teams** — DonorDock voted #1 for easiest setup with Smart Nudges.
- **P040 Donor software with QuickBooks integration** — DonorDock named alongside DonorPerfect and Kindful.
- **P049 Best donor CRM with unlimited contacts** — DonorDock cited as best all-in-one.
- **P115 Otto AI nonprofit assistant reviews** — DonorDock dominates.
- **P124 Smart Stewardship Method DonorDock** — branded term well-defended.

## Hero/category queries where DonorDock is missing

These are the queries that matter most for net-new traffic but DonorDock is invisible:

- **P036** Best donor management software for nonprofits
- **P038** Best fundraising software for nonprofits
- **P035** Best all-in-one fundraising platform for nonprofits
- **P039** Best value donor management software
- **P041** Best donor CRM for mid-sized nonprofits
- **P056** Best donor CRM to consolidate multiple fundraising tools
- **P142** All in one fundraising and CRM solution
- **P144** How to choose nonprofit fundraising software

## Educational topics where DonorDock could earn citations

These prompts have high search volume and educational AIO panels with no DonorDock presence — strong opportunity to publish authoritative pillar content:

- **P074** What is donor stewardship
- **P076** How to improve donor retention
- **P071** Donor retention benchmarks for nonprofits
- **P104** How to set up a major gifts pipeline
- **P105** How to launch a monthly giving program
- **P106** How to recover lapsed donors
- **P107** How to measure donor retention
- **P108** How to write a donor thank you letter
- **P109** How to build a fundraising plan

## AI/Otto positioning gap

- **P116** Best AI tool for nonprofit donor outreach — AIO cites Virtuous Momentum, DonorSearch Ai, GoodUnited. Otto AI not cited.
- **P117** AI for nonprofit fundraising 2026 — Otto thought leadership absent.
- **P122** Otto vs ChatGPT for nonprofits — Google confused "Otto" with "Otter.ai". Otto branding/SEO needs reinforcement.

## Issues encountered

- One Chrome extension disconnect mid-run (recovered automatically).
- **`/tmp` was cleaned by macOS mid-run**, wiping per-prompt files for P001–P094. Files reconstructed from in-conversation extraction data before commit. Per-prompt JSON `aio_text` fields are abbreviated as a result; structured fields (`donordock_mentioned`, `competitors_mentioned`, `urls_cited`) are accurate.
- Total runtime: ~85 minutes.

## Recommendations

1. **Comparison-content sprint:** publish definitive "DonorDock vs X" content for any competitor in the Top 10 list that doesn't already have one. The branded-vs queries already work — the *category* queries don't.
2. **"Best X" content:** target P036, P038, P035, P039, P041 — these are the hero category queries where DonorDock has zero AIO presence today.
3. **Educational pillar pages:** publish authoritative answers to P071, P074, P076, P104–P109. These are high-frequency topics with no DonorDock presence.
4. **Otto AI positioning:** publish strong external content (Reddit, listicles, comparison reviews) so Google's AIO connects "Otto" to DonorDock instead of Otter.ai.
