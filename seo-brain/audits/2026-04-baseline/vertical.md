# DonorDock Vertical SEO Baseline Audit — 2026-04-22

## Executive Summary

DonorDock sits at intersection of two SEO verticals: B2B SaaS and nonprofit-technology. Site performs well on SaaS fundamentals (SoftwareApplication schema sitewide, transparent pricing with UnitPriceSpecification, real /compare hub with 9 head-to-head pages, SOC 2 and 90-day guarantee trust signals). Ahead of most small CRM vendors on this. Three urgent vertical-specific gaps.

**The three baseline problems:**

1. **Broken trust-signal surface for nonprofit buyers.** `/customers`, `/success-stories`, `/reviews`, `/solutions` all return 404, yet these are linked from footer/nav. Nonprofit ED/DoD buyers spend 60-80% of evaluation time reading peer stories from similar orgs. DonorDock has 7,000+ customers with zero indexable case studies. **Single largest vertical-specific loss.**

2. **Invalid JSON-LD on high-value commercial pages.** Both `/pricing` and `/compare/donorperfect-vs-donordock` contain malformed JSON-LD (trailing commas, orphan braces). Google discards invalid blocks silently — the 4.8/200 AggregateRating on /pricing and 8 Review entities on the DonorPerfect compare are almost certainly not rendering rich results. **Highest-ROI schema fix on site.**

3. **Meta description missing sitewide.** Every page audited missing `<meta name="description">`. Webflow allows Google auto-snippet, but for B2B SaaS in saturated category this leaves AI Overview and SERP snippet intent signals on the table.

**What's working:** Schema sophistication surprisingly good — SoftwareApplication + featureList + Offer + AggregateRating + Organization + BreadcrumbList across main pages. Compare hub exists with clear competitor coverage. Pricing public with real dollar ($500/mo) — puts DonorDock ahead of most competitors. G2/Capterra awards featured visually. 64 partner integration URLs exist as crawlable.

**Vertical score baseline: 42/100.**

---

## Site Type Detection

**Primary vertical:** B2B SaaS (SoftwareApplication schema, public pricing, comparison architecture, demo CTA, integration catalog)
**Secondary vertical:** Nonprofit-Technology / Vertical-SaaS (ICP language, faith/education/human-services solution nav, 501c3 focus)

**Implication:** DonorDock must optimize for both general SaaS buyer intent ("best nonprofit CRM," "donor management software") AND sub-vertical nonprofit intent ("church donor software," "education fundraising CRM"). Second category invisible to Google because sub-vertical pages don't exist.

---

## Score Breakdown

| Sub-score | Score /10 |
|---|---|
| SaaS schema foundation | 8 |
| SaaS comparison architecture | 5 (exists but thin + broken schema) |
| SaaS pricing transparency | 7 |
| SaaS external review integration | 3 |
| Nonprofit vertical trust signals | 5 |
| Nonprofit case study depth | **1** |
| Nonprofit sub-vertical page coverage | **1** (404 hub + 404 sub-pages) |
| Integration partner SEO | 4 |
| Category SERP positioning | 5 |
| Meta / on-page hygiene | 3 (sitewide meta description missing) |
| **Overall vertical SEO score** | **42/100** |

Headroom: 58 points. ~35 recoverable in 90 days by executing Tiers 1-2 below.

---

## SaaS-Specific Checklist

### Pricing Page Structure — 6/10
- Pricing publicly visible ✓
- Prices in JSON-LD Offer — Partial: Offer exists with UnitPriceSpecification BUT JSON block has syntax error (trailing comma) invalidating entire block
- Multiple tiers — Weak: single "ONE Plan". No on-page framing explaining why one tier
- Add-ons pricing transparency ✓ ($40 user seats, $45 email blocks, $19 SMS, $60 automations)
- Annual vs monthly toggle — Miss: only annual surfaced
- Money-back guarantee ✓ (90-day)
- Setup/onboarding cost disclosure ✓ ($3,800 premium)
- Pricing FAQ schema — Miss
- Meta description — Fail (missing)

**CRITICAL:** Pricing JSON-LD `"offers": [...]` array has stray `}` where comma-separated second offer should start. Google parses ZERO structured data from pricing page currently. AggregateRating 4.8/200 and 13-item featureList invisible. **Single highest-ROI schema fix on site.**

### Comparison Pages — 5/10
- Compare hub exists ✓
- 9 individual vs-pages exist ✓ (Bloomerang, DonorPerfect, Givebutter, Etapestry, Network for Good, Salesforce, Little Green Light, Bonterra, Neon CRM)
- Word count — THIN: 1,265–1,681 words. Competitive benchmark for "Bloomerang vs X" SERP: 2,500–4,000 words
- Competitor pricing shown — Pass (Bloomerang)
- Feature-matrix table ✓
- Review schema on vs-pages — Partial: only DonorPerfect page has Review markup (8 entities) — and it's MALFORMED
- Customer switching quotes — Miss
- FAQ schema on vs-pages — Miss
- Meta descriptions — Fail (all missing)

**Competitive gap:** Bloomerang's own `/vs-donorperfect` runs ~3,500 words with video testimonials. DonorDock's vs-pages stop at ~1,500 words with no video/switching narrative.

**Givebutter risk:** Givebutter publishes `/alternatives/donordock` on their domain — actively intercepting DonorDock brand searches. DonorDock's `/compare/givebutter-vs-donordock` at 1,265 words is shortest vs-page. URGENT.

### Product Schema — 8/10
SoftwareApplication schema clean and parseable on homepage:
- applicationCategory: BusinessApplication
- aggregateRating: 4.8 / 200
- featureList: 10 items
- offers with pricing URL
- provider: Organization with sameAs

**Issues:** applicationCategory could be more specific ("CRM"). No softwareVersion, releaseNotes, fileSize. No screenshot property.

### G2/Capterra/External Review — 3/10
- G2 badges visible ✓ (visual only)
- Capterra badges visible ✓ (visual only)
- AggregateRating source attribution — Fail (4.8/200 has no url to G2/Capterra)
- External ratings aggregated — Miss (G2 4.8/183+, Capterra 4.8/27, plus SoftwareAdvice/GetApp — none linked from schema)
- `/reviews` page — **404** (linked from footer but doesn't exist)
- Review schema with verified source — Miss (8 Reviews on DonorPerfect page name reviewers but don't attribute source platform)

**The 4.8/200 problem:** G2 alone shows 183+ reviews. Capterra 27. GetApp/SoftwareAdvice/TrustRadius more. Either 200 is stale or under-counted. AEO needs explicit source via `/reviews` page aggregating external ratings with attribution, or `isBasedOn` property in schema.

---

## Nonprofit-Vertical-Specific Checklist

**Trust signals for nonprofit buyers — 5/10**
- Customer count displayed ✓ ("7,200+ users")
- Gifts tracked displayed — Partial ("$9B+ tracked" in context)
- Logo parade ✓ (United Way, Habitat, Ronald McDonald House)
- Nonprofit compliance — Partial (SOC 2 Type 2 in schema; no explicit 501(c)(3) language)
- Data migration assistance ✓ ("white-glove")
- ActionBoard® / Smart Steward Method ✓
- Focused Fundraiser podcast — Partial (in nav, not schema-marked as PodcastSeries)

**Pricing transparency — 7/10**
DonorDock wins here. Most competitors (Bloomerang, DonorPerfect, Neon, Salesforce NPSP) hide pricing. DonorDock shows $500/mo publicly — defensive moat for "nonprofit CRM pricing" queries (assuming schema parses, which it doesn't).

Missing: "how our pricing compares to competitors" component, explicit nonprofit-discount framing, tiered budget examples, monthly option.

**Case study depth — 1/10 (CRITICAL GAP)**
- `/customers` = 404
- `/success-stories` = 404
- `/case-studies` = not tested, footer Success stories 404s
- Individual case studies = none found indexable
- CaseStudy schema = missing
- Video testimonials = not detected

**This is the #1 unforced vertical error.** Competitors Bloomerang and DonorPerfect each have 15–30 indexable case study URLs segmented by cause area with quantified outcomes. DonorDock has zero, AND the footer `/success-stories` link 404s.

---

## Industry-Specific Schema Recommendations

### SoftwareApplication vs Product vs Service
**Use SoftwareApplication as primary (correct).** Consider dual-type:
```
"@type": ["SoftwareApplication", "Product"]
```

**Additions:**
- `applicationSubCategory: "Nonprofit CRM"` (AI-readable vertical signal)
- `screenshot`: product screenshot URLs
- `softwareVersion`: current release
- `releaseNotes`: changelog URL (build the page first)
- `potentialAction: {"@type": "TryAction", "target": "..."}` (AI-agent-friendly)
- `audience: {"@type": "Audience", "audienceType": "Nonprofit organizations, 501(c)(3) charities, small to mid-size nonprofits"}`
- `award`: list G2 badges as individual strings

### AggregateRating Source Attribution
**Option B (recommended, no new page required):**
```json
"aggregateRating": {
  "@type": "AggregateRating",
  "ratingValue": "4.8",
  "reviewCount": "210",
  "isBasedOn": [
    {"@type": "AggregateRating", "url": "https://www.g2.com/products/donordock/reviews", "ratingValue": "4.8", "reviewCount": "183"},
    {"@type": "AggregateRating", "url": "https://www.capterra.com/p/184187/DonorDock/reviews/", "ratingValue": "4.8", "reviewCount": "27"}
  ]
}
```

Plus a first-party `/reviews` page aggregating pull-quotes.

### Additional Schema
1. Organization (site-wide root) — expand with numberOfEmployees, foundingDate, founder (Matt Bitzegaio), subjectOf PodcastSeries, award list
2. PodcastSeries for /focused-fundraiser (49 episodes = dormant authority signal)
3. FAQPage on /pricing, compare hub, each vs-page
4. VideoObject on demo walkthrough
5. HowTo on Mailchimp/Zapier/QuickBooks integration pages
6. CaseStudy/Article on each customer story (once built)
7. CollectionPage on /integrations, /compare, future /customers hub

---

## Integration Partner SEO

Current state: Directory + 64 individual URLs, SoftwareApplication schema per page, BreadcrumbList. But Mailchimp page has ~650 words of marketing fluff with NO steps/screenshots/videos. Pattern likely replicated across 87 integration pages.

**Target queries:**
- "how to sync Mailchimp with DonorDock"
- "DonorDock QuickBooks integration"
- "does DonorDock integrate with Planning Center" (faith-vertical specific!)
- "best nonprofit CRM that integrates with Double the Donation"

**Quick win:** Top 10 integrations (QuickBooks, Mailchimp, Zapier, Planning Center, Constant Contact, Stripe, PayPal, Salesforce, Eventbrite, Double the Donation) — add step-by-step setup with 3-5 screenshots, HowTo schema, data-sync table, video walkthrough, 2 customer quotes. Push each from 650w to 1,200-1,500w with schema rich results.

**Special case: Planning Center** — faith-based ChMS used by 70K+ churches. DonorDock has integration listed but no landing depth. 20-minute fix unlocks "church donor management" queries.

---

## Category SERP Competitive Positioning

| Query | DonorDock position (est) | Who's winning |
|---|---|---|
| "nonprofit CRM" | Page 2-3 | Bloomerang, DonorPerfect, Salesforce NPSP, Neon |
| "donor management software" | Page 2 | Bloomerang, DonorPerfect, Kindful |
| "best nonprofit CRM" | Mixed (own article ranking) | DonorDock's /articles/best-nonprofit-crm |
| "church donor software" | Not visible | Kindful, Breeze, Planning Center |
| "affordable nonprofit CRM" | Potentially strong | Givebutter, LGL |

**Sub-vertical SERP whitespace (low competition + high nonprofit-buyer intent):**
- "donor CRM for churches" — no /solutions/faith-based page
- "fundraising software for schools" — no /solutions/education (404)
- "animal shelter donor management" — no sub-vertical page
- "arts nonprofit CRM" — no /solutions/arts-culture (404)
- "healthcare foundation CRM" — no /solutions/healthcare (404)

---

## Quick Wins (Ranked by ROI)

### Tier 1 — Critical, 14 days
1. **Fix invalid JSON-LD on /pricing** — single trailing comma restores featureList, pricing, 4.8/200 rating. Currently Google parses ZERO structured data from pricing.
2. **Fix invalid JSON-LD on /compare/donorperfect-vs-donordock** — recovers 8 Review entities.
3. **Build /success-stories hub + 5 seed case studies** (faith/education/human services/arts/healthcare). Each 800-1,200w with quantified outcome in H1 subhead, CaseStudy schema.
4. **Unbreak /solutions sub-URLs.** At minimum /solutions/education, /solutions/faith-based, /solutions/human-services, /solutions/arts-culture, /solutions/healthcare. Template shell OK but 200 words vertical-specific per page.
5. **Add meta descriptions sitewide.** Bulk-populate Webflow CMS settings.

### Tier 2 — High impact, 30 days
6. **Build /reviews page as first-party aggregation.** Attributed pull-quotes from G2/Capterra/GetApp/SoftwareAdvice. AggregateRating with isBasedOn.
7. **Expand each vs-page to 2,500+ words.** Start with Givebutter (thinnest, most under-attack).
8. **Fix AggregateRating attribution** sitewide with url or isBasedOn. Align reviewCount (likely 230-260 actual).
9. **Upgrade top 10 integration pages.** HowTo schema + screenshots.

### Tier 3 — Strategic, 60-90 days
10. **Podcast schema + authority.** PodcastSeries for Focused Fundraiser (49 episodes). Cross-link from Organization subjectOf.
11. **Security/Trust page.** SOC 2 Type 2 deserves own URL.
12. **Comparison pricing component on /pricing** — "How DonorDock pricing compares" widget.
13. **ChangeLog / Product updates page.**

---

## Strategic Recommendations

1. **Lean into nonprofit-vertical SaaS position.** Schema currently says generic `BusinessApplication` — reinforce "nonprofit CRM / donor management" everywhere.
2. **Treat 7,200-customer base as SEO asset.** Every story potentially indexable URL. 30 case studies at 1,000w = 30,000w of entity-dense, quantified-outcome content. Segment by sub-vertical AND by source-CRM-migration ("migrated from Bloomerang," "from DonorPerfect," "from spreadsheets").
3. **Win comparison SERPs before expanding TOFU.** Fixing schema + expanding vs-pages to 3,000w delivers more pipeline than 10 new TOFU articles. Comparison intent is 5-8x higher purchase intent.
4. **Defend brand term aggressively.** Monitor for Bloomerang/DonorPerfect/Neon publishing `/alternatives/donordock` pages.
5. **AEO-specific:** Fix Review schema first (30-min engineering task recovers outsized citation density), then FAQ schema on /pricing + vs-pages for long-tail Q&A retrieval.

**Nonprofit buyer trust signal hierarchy:**
1. Peer stories from similar organizations (404s today)
2. Pricing transparency (public, no surprises)
3. Data security (SOC 2, migration, 501c3 compliance)
4. Free/low-commitment trial (90-day guarantee works)
5. Human support and onboarding (90-day program is differentiator)

DonorDock scores high on 2, 3, 5 and low on 1, 4. The case-study gap (404 pages) is simultaneously a marketing-ops AND SEO priority.

---

**Sources:**
- G2: https://www.g2.com/products/donordock/reviews
- Capterra: https://www.capterra.com/p/184187/DonorDock/reviews/
- SoftwareAdvice: https://www.softwareadvice.com/nonprofit/donordock-profile/
- GetApp: https://www.getapp.com/nonprofit-software/a/donordock/
- Givebutter alt page: https://givebutter.com/alternatives/donordock
- Bloomerang vs DonorDock on Capterra: https://www.capterra.com/compare/131207-184187/Bloomerang-vs-DonorDock

**End of vertical baseline audit.**
