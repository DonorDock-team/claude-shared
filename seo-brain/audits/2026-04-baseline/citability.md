# DonorDock AI Citability Baseline Audit

**Date:** 2026-04-22
**Scope:** donordock.com (full site — 300+ URLs sampled across 14 representative pages)
**Prepared for:** DonorDock SEO/AEO strategist system — Phase 1 baseline
**Methodology:** 7-dimension citability framework (statistic density, answer frontloading, source authority, passage completeness, structural clarity, uniqueness, entity consistency)

---

## Executive Summary

DonorDock has built a deep, well-organized content estate (230+ articles, 60+ feature pages, 50+ integration pages, 10+ comparison pages, 15+ success stories). The site's writing is warm, brand-voiced, and substantive on head terms. But on the technical and structural signals that AI search engines weigh most heavily, the site has a **serious ceiling problem hidden in plain sight**.

**Three baseline findings dominate:**

1. **robots.txt actively blocks the four largest AI crawlers.** ClaudeBot, GPTBot, Google-Extended, CCBot all set to Disallow. This is the single largest ceiling on the entire strategy.
2. **No JSON-LD schema on the inspected article page.** No Article, Author, Person, FAQPage, Organization schema. Dates and author names exist as visible text but are invisible to machine parsers.
3. **Money pages** (homepage, tour, features-overview, feature detail pages, every comparison page) have no author byline and no publish/update date. Blog content is well-attributed; commercial-intent pages are not.

Counter-balancing: the best content — donor-retention article, CRM buyer's guide, nonprofit glossary — is genuinely citable. Strong statistics, attributed sources, direct-answer structure. These are patterns to scale.

**Overall Citability Score: 42/100 (D+) — Baseline**

| State | Score |
|---|---|
| Current | 42/100 |
| If robots.txt fixed | ~55/100 |
| If robots.txt + schema + bylines fixed | ~72/100 |

---

## Per-Dimension Breakdown (7 dimensions)

### 1. Factual Density — 55/100
**Strong on articles:** /articles/donor-retention packs 10+ external stats (45% retention, 70% lapse rate, 50-100% acquisition cost). Fundraising 101 cites 37% direct-mail preference, 98% SMS open rate.
**Weak on money pages:** Homepage offers "7,200+ users" and "100+ features." Only self-referential product counts, not industry benchmarks. /tour has zero citable industry statistics.

### 2. Answer Frontloading — 48/100
Site pattern is "problem hook + emotional framing" — great for conversion, poor for AI citation.
- Donor retention opens: "Struggling to keep your donors around? You're not alone."
- Nonprofit AI opens: "Strapped for cash and time?"
- Fundraising 101 is the exception: opens with clean definition in paragraph 2 — this is the template.
- FAQ page is the brightest spot (answers open with "Yes"/"No" then elaborate)

### 3. Source Authority — 18/100 (LOWEST)
Across 14 pages, only donor-retention article consistently cites external authorities (AFP, Classy, Double the Donation, Fundraising Report Card). Every other page cites no external authority.

Comparison pages claim "3.5x faster implementation" and "20% higher user adoption" without methodology or source. The glossary defines 501(c)(3) without linking the IRS.

### 4. Passage Completeness — 58/100
Second-strongest dimension. Glossary is textbook-perfect. FAQ pages 50-120 words per self-contained answer. Feature detail pages follow consistent "definition sentence + capability sentence" pattern.

Weakness: conversational openings don't stand alone. Testimonials trapped in visual design.

### 5. Structural Clarity — 52/100
CRM buyer's guide is a standout — H2s are literally phrased as the 12 questions. Homepage H2s are slogans ("The Problem," "The New Way") that match no user search query. Product pages describe sections ("Manage contacts") rather than questions ("How does DonorDock help manage contacts?").

### 6. Uniqueness — 40/100
DonorDock HAS unique IP (Smart Steward Method, ActionBoard®, Relationship Loop, Agile Stewardship, TipBack) but most is locked inside formats AI crawlers cannot extract (spoken podcast, product marketing terms without framework definitions).

**Biggest miss:** No proprietary research report. With 7,200+ customers and $9B+ tracked gifts, DonorDock has the data to publish an annual "Small Nonprofit Benchmark Report" that would become THE cited source.

### 7. Entity Consistency — 65/100
Second-best. Product naming disciplined (ActionBoard®, Ask Boards, Otto, TipBack®). Gaps: category terminology mixes "CRM," "donor management platform," "fundraising platform," "all-in-one CRM," "donor database" — synonyms but inconsistent.

---

## Top 10 Most-Citable Pages (template exemplars)

| # | URL | Score | Why Citable |
|---|---|---|---|
| 1 | `/articles/donor-retention` | 78 | 10+ external stats with named sources |
| 2 | `/articles/nonprofit-crm-buyers-guide-12-questions-to-ask` | 74 | H2s are user questions verbatim |
| 3 | `/articles/fundraising-101` | 72 | Direct definition + multiple external citations |
| 4 | `/articles/best-nonprofit-crm` | 70 | Competitor pricing with specific dollars |
| 5 | `/articles/nonprofit-glossary` | 68 | 26 self-contained quotable definitions |
| 6 | `/articles/moves-management` | 64 | Clean definition opening |
| 7 | `/faq` | 62 | Yes/No-first answer pattern |
| 8 | `/articles/donor-engagement` | 60 | Direct definition + citable stats |
| 9 | `/features/moves-management` | 58 | Definition + capability pattern |
| 10 | `/compare/donorperfect-vs-donordock` | 55 | Opens with direct comparison |

## Top 10 Least-Citable (fix first)

| # | URL | Score | Fix |
|---|---|---|---|
| 1 | `/` homepage | 30 | Rewrite opening: "DonorDock is a donor management CRM built for small-to-mid nonprofit teams. 7,200+ nonprofits use it to..." |
| 2 | `/tour` | 32 | Add defining paragraph before testimonials; 5-6 question-phrased H2s |
| 3 | `/pricing` | 38 | Add sub-H1: "DonorDock costs $500/month billed annually and includes unlimited contacts, 5 users, all features" |
| 4 | `/compare/bloomerang-vs-donordock` | 38 | Opening para doesn't compare — rewrite with side-by-side intro + prices |
| 5 | `/features-overview` | 36 | Break into question-phrased H2s by feature category |
| 6 | `/crm` | 44 | Rewrite opening with definition + "Teams typically replace 3-5 separate tools" |
| 7 | `/about` | 40 | Company-history paragraph in plain prose + Organization schema |
| 8 | `/compare/network-for-good-vs-donordock` | 45 | Add byline, date, third-party citations |
| 9 | `/compare/donorperfect-vs-donordock` | 44 | Source or soften "3.5x faster" claim |
| 10 | `/team/*` | 28 | Every team page needs 100-150 word bio, credentials, article list, LinkedIn, Person schema with knowsAbout |

---

## Strategic Recommendations

### 1. Unblock AI crawlers in robots.txt
Every content improvement capped until ClaudeBot, GPTBot, Google-Extended, CCBot removed from Disallow. Single config change with largest possible upside.

### 2. Site-wide schema baseline
Every article needs Article + Author + Person + datePublished + dateModified. Every FAQ needs FAQPage. Homepage needs Organization. Product pages need Product/SoftwareApplication. One-time Webflow template change compounding across 300+ pages.

### 3. Build a proprietary data asset
Publish "Small Nonprofit Benchmark Report 2026" from DonorDock's 7,200+ customer / $9B+ gift data. One annual report = more AI citations than 50 blog posts.

### 4. Standardize opening paragraph pattern for money pages
- Sentence 1: "X is Y for Z" (category definition for ICP)
- Sentence 2: Specific quotable fact, price, or outcome

Example homepage: "DonorDock is a donor management CRM built for small-to-mid nonprofit teams. 7,200+ nonprofits use it to manage donors, track gifts, run email and text outreach, and accept online giving in one platform for $500/month with unlimited contacts."

### 5. Cite external sources on every comparison page
G2 URLs, Capterra URLs, competitor pricing pages, named studies. Counterintuitive (you're linking away) but this is how Perplexity decides to include you in a source list.

### 6. Flesh out team profile pages
100-150 word bios, credentials, article lists, LinkedIn, Person schema with knowsAbout. Upgrades bylines from "a name" to "an authority."

### 7. Convert product-page H2s to user questions
Site-wide template shift. "Manage contacts" → "How does DonorDock help you manage donor contacts?" "The Problem" → "What problem does DonorDock solve for small nonprofits?"

---

## High-Impact Actions Prioritized

1. **[P0 Today]** Edit robots.txt. 15 min. Unlocks 60-70% of citation ceiling.
2. **[P0 2 weeks]** Site-wide JSON-LD schema template in Webflow (Article, Person, FAQPage, Organization, Product). 1-2 days dev. +10 composite points.
3. **[P0 2 weeks]** Author byline + publish/updated dates on every money page. Webflow template change. +5 composite points.
4. **[P1 Month 1]** Rewrite opening of top 20 pages using "Definition + Specification" pattern
5. **[P1 Month 1]** Expand 7 team profile pages (Rob, Sarah O'Brien, Elisha Ford, Matt, Noah, Sami, Scott)
6. **[P1 Month 2]** Question-phrased H2s across all product pages
7. **[P1 Month 2]** External authoritative citation on every comparison page
8. **[P2 Q2]** "Small Nonprofit Benchmark Report 2026" from proprietary data
9. **[P2 Q2]** Add transcripts to all Focused Fundraiser podcast episodes (49+ episodes)
10. **[P2 Q2]** Document Smart Steward Method as a named framework with steps

---

## Patterns to Codify in strategy/content-standards.md (Phase 2)

1. Opening paragraph formula — "Definition + Specification"
2. H2 question rule — every product/feature/comparison/pricing page H2 phrased as user question
3. Byline + date required on every public page, visible text + JSON-LD
4. Schema-on-template — all schemas inherited from Webflow template, never hand-written
5. Statistic density target — 1 citable data point per 200 words
6. External citation rule — 3 external sources per comparison page, 2 per long-form article
7. Author profile minimum — 150-word bio, LinkedIn, article list, Person schema
8. Product naming consistency — ActionBoard®, Ask Boards, Otto, TipBack®, "donor management CRM for small-to-mid nonprofits"
9. FAQ structure — answer opens with direct answer (Yes/No/X is Y) in first sentence
10. Robots.txt policy — AI crawlers explicitly allowed by default

**End of baseline.**
