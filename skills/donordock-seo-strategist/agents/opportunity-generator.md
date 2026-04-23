# Opportunity Generator Subagent

## Purpose

Generate the monthly `opportunities/YYYY-MM.md` report. Synthesizes GSC data, content audit findings, competitor intel, and strategy docs into a prioritized action list for Rob.

## When to run

- **Monthly:** on the 1st of each month (or nearest business day). Scheduled automation in Phase 6 will trigger this.
- **Ad-hoc:** anytime Rob asks "what should we focus on this month?" or "what are my SEO opportunities?"
- **Post-strategy-change:** after any major strategy-doc update, regenerate to reflect new priorities.

## Inputs

- Previous month's `seo-brain/opportunities/YYYY-MM.md` (if exists)
- Current date / month
- Optional: specific focus area Rob wants emphasized

## Process

### 1. Load full strategy context
All of `seo-brain/strategy/` + `seo-brain/audits/2026-04-baseline/executive-summary.md`.

### 2. Pull fresh data from GSC

```
site_snapshot(days=28)  ← month-over-month trend
quick_wins(days=28, min_impressions=100)  ← this month's push-to-page-1 targets
content_gaps(days=90, min_impressions=100)  ← untapped demand
ctr_opportunities(days=28, min_impressions=500)  ← meta description fixes
content_decay()  ← pages slowly dying

For each of 7 pillars:
topic_cluster_performance(path_pattern="/PILLAR-URL", days=28)
```

### 3. Scan for strategic signals
- **Competitor moves:** fetch each competitor's blog index, diff against last month's audit
- **New customer stories** on /customer-success (opportunities for compare-page quotes)
- **Podcast episodes** (Focused Fundraiser): any new episodes to add VideoObject schema, add to State of Stewardship chapter lineup
- **Seasonal signals:** Giving Tuesday (Dec), year-end (Nov-Dec), Giving Season launch (Oct)

### 4. Cross-reference GSC data against strategy docs
For each GSC quick-win: does it fit a pillar? Does an AEO question in aeo-questions.md map? Is there content-standards-compliance work needed?

### 5. Prioritize
Use a P0/P1/P2 tier (matches keyword-universe.md). Order by (expected impact × ease of execution).

### 6. Write the report

```markdown
# Opportunities Report — YYYY-MM (month name)

**Generated:** 2026-05-01
**Generator:** donordock-seo-strategist opportunity-generator
**Owner:** Rob Burke (CMO)
**Review:** Rob approves items → creates Asana tasks (Phase 8)

---

## Executive summary
3-5 bullets on month-over-month performance + top priorities.

## Performance snapshot (28-day vs prior 28 days)

| Metric | This month | Prior month | Change |
|---|---|---|---|
| Clicks | X | Y | +/- Z% |
| Impressions | X | Y | +/- Z% |
| CTR | X% | Y% | +/- Z pts |
| Avg position | X.X | Y.Y | +/- Z.Z |

[Brief narrative on the trend.]

## Pillar performance

For each of 7 pillars:
- Pillar page URL
- Clicks / impressions / position this month
- Change vs prior
- Top 3 queries
- Action: [none / minor / major]

## P0 Opportunities (do this month)

### 1. [Title of opportunity]
- **Type:** [article / pillar page / comparison page / schema / migration content / refresh]
- **Target URL:** [URL]
- **Primary keyword:** [term] (GSC: pos X, Y impressions)
- **Pillar:** [pillar name]
- **Effort:** [S/M/L or hours]
- **Expected impact:** [clicks / citations / ranking shift]
- **Why now:** [GSC signal or strategic reason]
- **Draft brief:** [100-word outline of what should be written]

### 2. [Next opportunity]
...

## P1 Opportunities (do next month)

[Same format, less detail]

## P2 Opportunities (queue)

[List, minimal detail]

## CTR issues to address

Top 5-10 pages with impression volume but CTR below benchmark. Meta description rewrite recommendations.

## Content decay (pages losing traffic)

Pages declining 3 consecutive 30-day periods. Refresh or prune recommendations.

## Competitor signals

Any notable competitor moves this month:
- New compare pages they published
- New pillar content they shipped
- Pricing changes
- Acquisition / brand changes

## AEO / schema deployments needed

- Pages missing FAQ schema that are ranking positions 10-30 (high lift potential)
- Pages where visible FAQ exists but schema doesn't (quick fix)
- Compare pages with invalid JSON (ongoing cleanup)

## State of Stewardship Report milestones

If the report is in active production, list this month's checkpoint:
- Data extraction status
- Writing/design progress
- External reviewer engagement
- Launch timeline delta

## What happened last month (retrospective)

What from last month's report was shipped? What wasn't? Why?

---

## Rob's approval queue

Items for Rob to approve before they turn into Asana tasks (Phase 8):

- [ ] P0 item 1: [brief description] — approve / defer / modify
- [ ] P0 item 2: [brief description] — approve / defer / modify
- [ ] New pillar page URL: [URL] — confirm
- [ ] Meta description rewrite batch: [N pages] — approve
- [ ] Schema deployment batch: [N pages] — approve
```

### 7. Write to `seo-brain/opportunities/YYYY-MM.md`

Via `gh api` PUT to the repo. File named with the current month.

### 8. Optionally: surface critical items to Rob
If any opportunity is time-sensitive (competitor attack, ranking drop, broken page), flag at top of the report as URGENT.

---

## Prioritization heuristic

```
Priority score = (impact × ease × strategic_fit) / (competitive_pushback × execution_risk)

Where:
impact = estimated clicks + citations + ranking lift
ease = inverse of effort (S=3, M=2, L=1)
strategic_fit = alignment with pillar + Smart Stewardship + upmarket direction (1-5 scale)
competitive_pushback = how hard will competitors fight (1-5)
execution_risk = chance of flop (1-3)
```

For practical use:
- P0: score >5
- P1: score 3-5
- P2: score <3

---

## Example monthly opportunity (P0)

### "Build /donor-retention pillar page"

- **Type:** New pillar page
- **Target URL:** /donor-retention
- **Primary keyword:** "donor retention" (GSC: pos 74.3, 505 monthly impressions)
- **Pillar:** Pillar 7 (Donor Retention)
- **Effort:** L (15-25 hours)
- **Expected impact:** 150-250 monthly clicks at maturity; attacks Bloomerang's legacy positioning
- **Why now:** GSC shows 505 monthly impressions at avg pos 74.3 — we're not even on page 1. New pillar page closes the gap.
- **Draft brief:** 2,500-word pillar anchored to Smart Stewardship. Lead: "Donor retention is the downstream outcome of systematic stewardship. Here's the data and the method." Include AFP FEP citation, DonorDock State of Stewardship preview stats, 10+ FAQ. Link to Pillar 1 (Smart Stewardship) heavily. Author: Matt or Rob. Refresh /articles/donor-retention + fill /articles/donor-retention-strategies 404 + /articles/second-gift-strategy new.

---

## Output handling

- Write to `seo-brain/opportunities/YYYY-MM.md` via gh api PUT
- Email summary to Rob via Email MCP (if Phase 6/8 integration active)
- Update executive summary reference if pillar-level shifts occurred

---

## Escalation

If the month shows:
- Unexpected traffic drop >20% → flag as crisis, escalate to Rob before finishing report
- Sudden appearance of competitor /vs-donordock page → flag as defensive priority
- AI citation tracking (Phase 5) shows significant loss of AI-answer visibility → flag

These go above P0 in the report and get their own "URGENT" section at top.
