# Strategy Loader — session-start loading protocol

Before answering any substantive SEO/AEO question, load the locked strategy from the `seo-brain/` repo. This document defines the loading order, triage rules, and freshness checks.

---

## Primary load order (every session)

Load these in order. Each is loaded from `DonorDock-team/claude-shared/seo-brain/strategy/` unless noted.

### 1. brand-positioning.md (always, first)
The rules of engagement. Contains: Action Board (two words), Smart Stewardship as owned category, upmarket ICP ($1M floor, 3+ FTE), verticals (faith-based OK, churches NOT), pricing messaging (1% platform fee), verified facts (~1,300 nonprofits, 7,200+ users, $9B+ tracked gifts, 4.8/5 rating).

**Source of truth for anything that represents DonorDock.** If another doc conflicts, this wins.

### 2. pillars.md (always, second)
The 7 locked content pillars. Pillar URLs: /smart-steward-method (master), /crm, /online-giving, /donor-outreach, /fundraising-strategy (root), /otto (AI), /donor-retention (root).

### 3. content-standards.md (always, third)
Pre-publish checklist, schema requirements by content type, structural rules (TL;DR, question-format H2s, FAQ count per pillar page, internal linking density, image standards, meta tag standards).

### 4. Context-dependent — load based on query type

| Query type | Load these |
|---|---|
| "Should we write about X?" | `keyword-universe.md` + `aeo-questions.md` + `competitor-landscape.md` + `icp-intent-map.md` |
| "Validate this draft" | `content-standards.md` (already loaded) + pillar section from `pillars.md` matching the draft's topic |
| "What schema does /X need?" | `content-standards.md` + `references/schema-templates.md` (this skill) |
| "Competitor question about X" | `competitor-landscape.md` + specific file from `audits/2026-04-baseline/competitors/X.md` |
| "Generate monthly opportunities" | ALL strategy docs + `audits/2026-04-baseline/executive-summary.md` + last 90 days GSC data |
| "What is our ICP?" | `icp-intent-map.md` + `brand-positioning.md` |
| "What is Smart Stewardship?" | `brand-positioning.md` + `state-of-stewardship-report.md` |

### 5. Never load unless explicitly needed

- Full Phase 1 audit files (`audits/2026-04-baseline/*.md`) — too much detail for most questions. Load specific competitor audits only when answering questions about that competitor.
- Historical monthly opportunity reports (`opportunities/*.md`) — reference prior decisions; load on request.
- Tracking files (`tracking/*.json`) — machine data, not analysis. Load programmatically for specific metrics queries.

---

## Freshness checks

Strategy docs are human-curated and change slowly. GSC data changes daily. Audit data changes monthly.

### Before answering with a data-dependent claim

1. **Strategy claim** (pillars, positioning, ICP) → trust repo; no freshness check needed
2. **Ranking claim** (e.g., "we rank #5 for 'donor CRM'") → call GSC MCP (`advanced_search_analytics` or `topic_cluster_performance`) for fresh data
3. **Customer count / rating / facts** (e.g., 1,300 nonprofits, 4.8/5) → trust `brand-positioning.md` section 9 "Verified numeric facts"
4. **Competitor pricing claim** → check `competitor-landscape.md` timestamp. If >30 days old, flag "may be stale" and recommend re-verification
5. **Live site state** (e.g., "is schema deployed on /pricing?") → fetch live HTML + parse; don't trust Phase 1 audit for live state after remediation

---

## Hierarchy of authority

When sources conflict:

1. **Rob's direct input in the current conversation** — highest authority
2. **`seo-brain/strategy/brand-positioning.md`** — rules of engagement
3. **`seo-brain/strategy/pillars.md`** — canonical pillar list + URLs
4. **Other `seo-brain/strategy/*.md`** docs
5. **Phase 1 audit findings** (`seo-brain/audits/2026-04-baseline/`)
6. **Audit agent hypotheses** (competitors/*.md) — treat as draft until verified
7. **External best-practice defaults** — only when repo is silent

---

## When repo data is missing or stale

1. **Check if `seo-brain/opportunities/YYYY-MM.md`** has the answer from a recent run
2. **Check `seo-brain/tracking/*.json`** for recent observation data
3. **Run a live GSC query** if the question is ranking/CTR/impression related
4. **Fetch live URL** via Bash curl if the question is about current site state
5. **If still missing**, acknowledge the gap and propose (a) live data fetch, (b) create a new strategy doc, or (c) defer to Rob for input

Never fabricate. Never answer with "I think" without marking it as uncertain.

---

## Example: correct loading sequence for "Should we write an article about donor retention?"

1. Load `brand-positioning.md` — confirms upmarket language, Smart Stewardship framing required
2. Load `pillars.md` — confirms Donor Retention is a locked pillar with URL `/donor-retention`
3. Load `keyword-universe.md` — pulls Donor Retention keyword cluster + GSC data ("donor retention" pos 74.3, 505 imps; "donor retention strategies" pos 52.6, 527 imps — big opportunity)
4. Load `aeo-questions.md` — pulls AEO questions for Donor Retention pillar
5. Load `competitor-landscape.md` — confirms Bloomerang is the retention-incumbent; check our attack angle
6. Optional GSC live query — `quick_wins` filtered for retention-related queries to freshen the data
7. Answer: "Yes, write it. High priority — P0. Specific positioning: Smart Stewardship is systematic retention. Title hypothesis: 'Donor Retention: The Complete Smart Stewardship Guide'. Target URL: /donor-retention (new pillar page). Link from there to /articles/donor-retention-strategies (fill existing 404) and /articles/donor-retention (existing article). FAQ schema required with 8+ Qs drawn from aeo-questions.md. Draft 2,500+ words, cite AFP Fundraising Effectiveness Project. Expected impact: capture ~500 monthly impressions currently ranked page 5+."

That's the pattern. Load what's needed, cite sources, give specific guidance.
