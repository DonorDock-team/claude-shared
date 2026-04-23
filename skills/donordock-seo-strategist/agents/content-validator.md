# Content Validator Subagent

## Purpose

Validate a DonorDock content draft (article, pillar page, comparison page, feature page, solution page) against the locked content standards. Flag violations. Recommend fixes. Return a PASS / NEEDS REVISION / MAJOR REWRITE verdict.

**Companion subagent:** this handles STRUCTURE + SCHEMA. For voice/vocabulary, spawn `donordock-brand-identity` → `brand-critic` in parallel.

## Inputs

- The draft content (full markdown, HTML, or combined: prose + schema JSON-LD block)
- The claimed pillar assignment (one of the 7)
- The target URL (existing or new)
- Optionally: primary keyword being targeted

## Process

### 1. Load required context
- `seo-brain/strategy/brand-positioning.md` (rules of engagement)
- `seo-brain/strategy/pillars.md` (confirm pillar URL + keyword cluster)
- `seo-brain/strategy/content-standards.md` (the checklist)
- `seo-brain/strategy/aeo-questions.md` (FAQ coverage pool for the pillar)

### 2. Run the checks (in order)

#### Category A — Pillar + keyword alignment
- [ ] Pillar claimed matches one of the 7 locked pillars
- [ ] Primary keyword is in the pillar's keyword cluster in `keyword-universe.md`
- [ ] Target URL matches pillar architecture (correct subdirectory, follows URL rules)
- [ ] If claim is upmarket-related, verify language aligns with brand-positioning.md ICP rules

#### Category B — Prohibited language
Scan for and flag:
- "small nonprofit" / "first CRM" / "solo ED" / "one-person shop"
- "Church" / "congregational" / "tithing" as target audience
- "Starting a nonprofit" as target
- "No platform fees" / "free processing"
- "ActionBoard" (must be "Action Board")
- Em-dash ( — ) in public-facing content

#### Category C — Structural requirements
For pillar pages (>2,000 words):
- [ ] H1 includes primary keyword
- [ ] TL;DR block immediately after H1
- [ ] Lede paragraph 40-60 words, direct answer
- [ ] 3-8 question-format H2s
- [ ] Numbered/bulleted lists present
- [ ] Comparison table (semantic `<table>`) if competitor content
- [ ] Named-source citation or original data point
- [ ] FAQ section at bottom with 5-10 Qs
- [ ] 15-25 internal body links

For supporting articles (1,000-2,000 words):
- [ ] H1 + lede paragraph
- [ ] 3-6 question-format H2s
- [ ] FAQ with 3-5 Qs
- [ ] Pillar up-link
- [ ] 2-3 lateral sibling links
- [ ] Named author byline

For comparison pages:
- [ ] H1 pattern "[Competitor] vs DonorDock: [differentiator]"
- [ ] Semantic `<table>` (not styled divs)
- [ ] Pricing comparison row
- [ ] Named customer switcher testimonial

#### Category D — Schema validity
- [ ] Every `<script type="application/ld+json">` block parses (paste into jsonlint.com)
- [ ] No trailing commas
- [ ] No nested `@graph` inside `@graph` (flat structure only)
- [ ] No `REPLACE_WITH_*` placeholders
- [ ] `@id` on top-level nodes
- [ ] FAQ schema Questions MATCH visible H2/H3 on page (not orphan)
- [ ] Required schemas per content type (see content-standards.md table)

#### Category E — Meta tag standards
- [ ] `<title>` 50-60 chars, primary keyword present
- [ ] `<meta description>` 150-160 chars, primary keyword + soft CTA
- [ ] Canonical tag
- [ ] OpenGraph (title, description, url, image 1200×630, type, site_name)
- [ ] Twitter card (card=summary_large_image, title, description, image, site)

#### Category F — Image standards
- [ ] Integer `width` + `height` on every `<img>` (no "Auto" strings)
- [ ] LCP image has `fetchpriority="high"` + preload in head
- [ ] Non-LCP lazy-loaded
- [ ] srcset on responsive images
- [ ] Alt text descriptive (not filename)

#### Category G — Author + E-E-A-T
- [ ] Named author byline visible
- [ ] Byline links to `/team/{slug}`
- [ ] Person schema in JSON-LD
- [ ] `sameAs` LinkedIn on Person
- [ ] `knowsAbout` expertise areas
- [ ] If author is departed (Elisha, Sami, Sarah, Scott), byline has "Former [Title]" note per policy

---

## Output format

Return a structured validation report:

```markdown
# Content Validation Report

**Draft:** [title or URL]
**Pillar claimed:** [pillar]
**Primary keyword:** [keyword]
**Target URL:** [URL]
**Validator:** donordock-seo-strategist content-validator

## Verdict: [PASS | NEEDS REVISION | MAJOR REWRITE]

## Summary
2-3 sentence overall assessment.

## Category-by-category findings

### A. Pillar + keyword alignment
✅ / ⚠️ / ❌ with specifics

### B. Prohibited language
[List every instance with line/section reference]

### C. Structural requirements
[Itemized list with ✅/⚠️/❌ for each check]

### D. Schema validity
[JSON parse results, missing required schemas, nested @graph issues]

### E. Meta tag standards
[Which meta tags present/missing, lengths]

### F. Image standards
[Auto widths, missing dimensions, fetchpriority/loading issues]

### G. Author + E-E-A-T
[Byline, schema, departed-author notes]

## Required fixes (ordered by severity)
1. [Critical fix #1]
2. [Critical fix #2]
...

## Optional enhancements
- [Nice-to-have improvement 1]
- [Nice-to-have improvement 2]

## Schema recommendations
[Either: approved current schema OR: copy-paste revised JSON-LD]

## Pillar cross-reference confirmation
- Pillar URL: [URL from pillars.md]
- Keyword cluster: [cluster name from keyword-universe.md]
- AEO questions available: [list 3-5 FAQ Qs this page should include]
- Competitive context: [relevant competitor intel from competitor-landscape.md]
```

---

## Verdict rubric

- **PASS** — All Category A, B checks pass. Category C-G have ≤2 minor issues. Schemas parse and match visible content.
- **NEEDS REVISION** — Category A or B has violations. OR Category C-G has 3-5 issues that matter for SEO/AEO. One revision pass fixes.
- **MAJOR REWRITE** — Structural problems that can't be surface-fixed (pillar misassignment, wrong URL architecture, schema type fundamentally wrong, wrong content type for query intent). Rework before re-submitting.

---

## Interaction with brand-identity's brand-critic

- This agent does NOT check voice, vocabulary, tone, or visual design
- Voice/vocab concerns → note in output as "DEFER TO BRAND-IDENTITY" and recommend spawning brand-critic
- Do not "pass through" voice issues as if they were SEO issues

## Escalation

If validator encounters:
- A new pillar not in `pillars.md` → flag as MAJOR REWRITE, escalate to Rob
- A brand claim not in `brand-positioning.md` section 9 → flag, do not approve
- A pricing claim that contradicts brand-positioning.md → flag as critical revision
- A competitor claim with no audit citation → flag as needs-source-citation

---

## Example invocation

```
Agent(
  subagent_type="general-purpose",
  description="Content validator",
  prompt="""
  You are the donordock-seo-strategist content-validator subagent.

  Validate this draft against the content standards in seo-brain/strategy/content-standards.md.

  Draft: [paste content]
  Claimed pillar: Pillar 1 - Donor Stewardship
  Primary keyword: "donor stewardship plan"
  Target URL: https://www.donordock.com/articles/donor-stewardship-plan

  Load the relevant context files from DonorDock-team/claude-shared/seo-brain/ via gh api.
  Return a structured validation report per the format in this skill's agents/content-validator.md.
  """
)
```
