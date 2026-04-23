# Phase 1 Baseline — Executive Summary

**Period:** 2026-04-22 to 2026-04-23
**Scope:** Site audit (9 dimensions) + competitor audit (8 vendors) + remediation
**Owner:** Rob Burke (CMO, rburke@donordock.com)
**Status:** Phase 1 complete. Ready for Phase 2 strategy.

This summary synthesizes 9 site audits, 8 competitor audits, and the remediation work completed between 2026-04-22 and 2026-04-23. It is the canonical input to Phase 2 strategy documents.

---

## 1. DonorDock site scorecard (starting baseline)

| Dimension | Score | Grade | Trend post-remediation |
|---|---|---|---|
| Technical SEO | 72/100 | B- | Many fixes landed live (tag noindex, BlogPosting dedupe, Neon H1, newsletter DOM) |
| AEO Readiness | 65/100 | C+ | FAQ page flat @graph + 114 H3 accordions landed |
| GEO Readiness | 32/100 | F | **Blocked on Cloudflare robots.txt decision (Rob in progress)** |
| AI Citability | 42/100 | D+ | Content is citable; entity signals still weak |
| Performance | 65/100 | C | CLS + render-blocking remain; Auto dimensions mostly fixed |
| Security | 62/100 | C+ | Headers cleanup not yet applied |
| Schema coverage | mixed | mixed | 2 of 9 compare pages + pricing fixed with real content schemas; 6 still invalid or missing |
| Content quality | 58/100 | C | Tag noindex fixed; pillar-cluster wiring and decay refresh outstanding |
| Vertical SEO | 42/100 | F | Meta descriptions corrected on compare pages; case-study gap remains |

### Confirmed live (Rob's publish, 2026-04-23)

- BlogPosting deduplicated (467 articles, 1 script each)
- 88 tag archive pages: `meta robots=noindex,follow` applied
- /faq page: flat @graph + 114 H3 accordions + 114 Question entities + valid JSON
- Neon compare H1 typo fixed ("Neon CRM vs DonorDock")
- Newsletter form removed from article template DOM (no longer between H1 and body)
- llms.txt: UTF-8 plain text with 1% platform fee messaging + strategic content map
- Compare pages: meta descriptions populated on all 10
- DonorPerfect compare schema: valid JSON, 3 real FAQ Q&A, 6 real Reviews
- Neon compare schema: valid JSON, 2 real FAQ Q&A, 3 real Reviews
- Homepage hero: Auto width/height removed
- /solution/donor-stewardship: Auto removed from 3 mockup images

### Still outstanding

| Item | Owner | Blocker |
|---|---|---|
| robots.txt AI bot unblock | Rob (Cloudflare) | Strategic decision + Cloudflare config |
| Re-paste corrected pricing schema with "1% platform fee" | Rob | Minor — live schema has old "no platform fees" Offer description |
| Article CMS template featured image still `width="Auto" height="Auto"` | Rob (Webflow Designer) | 1 template fix = 467 article pages |
| FAQ schema on 7 remaining compare pages + pricing + /features/* | Rob | Content exists visually, schema missing |
| Compare-page pricing data refresh (/compare/network-for-good-vs-donordock shows stale $79/mo, should be $500) | Rob | Content edit |

---

## 2. Cross-audit themes (9 site + 8 competitor)

Themes that surfaced in 5+ audits:

### 2A. robots.txt vs llms.txt conflict is the single biggest blocker
DonorDock's Cloudflare robots.txt blocks ClaudeBot, GPTBot, Google-Extended, CCBot, Applebot-Extended, Bytespider, Amazonbot, meta-externalagent. DonorDock's llms.txt invites them ("Training: allowed, Commercial use: allowed with attribution"). Bots respect robots.txt first — the llms.txt isn't being read.

Flagged by: GEO audit, Citability audit, AEO audit, Bloomerang audit, DonorPerfect audit, Neon audit.

**Competitor posture:**
- Bloomerang: implicit allow (no explicit block or allow). AI-trainable.
- DonorPerfect: no AI directives at all. Fully open to all crawlers.
- Network for Good / Bonterra: permissive, no llms.txt.
- Givebutter: permissive.
- Keela: permissive.
- Virtuous: permissive.
- Little Green Light: blocks ClaudeBot/CCBot/Google-Extended via Cloudflare (same as DonorDock) AND publishes llms.txt (same contradiction).
- Neon One: blocks via Cloudflare WAF aggressively — even standard curl gets 403.

**DonorDock is in a minority of 2 (with LGL) on AI bot blocking. 6 of 8 competitors are freely AI-trainable.** This is the highest-leverage single decision for Phase 2.

### 2B. FAQ schema at scale is DonorDock's biggest uncaptured AEO asset
114 questions live on /faq with proper schema now. But:
- 7 of 9 compare pages have no FAQ schema (or invalid JSON wrapping it)
- /pricing has visible FAQ but no schema
- 6+ feature pages have visible FAQs but no schema
- 467 articles have no FAQ schema even where content is Q&A-structured

Competitor benchmark: Bloomerang's flagship article ("21 Best Nonprofit CRMs") has only 4 Questions in schema. We can easily beat this with 10-15 per page across the site.

### 2C. Comparison page whitespace is DonorDock's durable moat
DonorDock has 10 comparison pages. Competitors have:
- Bloomerang: 0
- DonorPerfect: 5 pages (but none vs DonorDock)
- Network for Good/Bonterra: 0 vs DonorDock
- Givebutter: 1 (the /alternatives/donordock page — #1 ranking, shared template)
- Keela: 0 vs DonorDock
- Neon One: 0 vs DonorDock (5 other comparisons, none for us)
- LGL: 1 (Kindful alternative only)
- Virtuous: 0

**6 of 8 competitors don't defend their brand SERP against DonorDock.** This is uncontested search territory we already occupy.

### 2D. Content volume gap is real but not existential
- Bloomerang: ~2,000 URLs (1,306 blog + 152 pages + 72 guides + 100+ case studies across 13 segmented sitemaps)
- DonorPerfect: ~800 URLs (648 blog + 157 pages)
- Virtuous: ~1,000 URLs (646 blog + 187 pages + 75 case studies + 41 gated resources)
- LGL: ~700 URLs (502 blog + 136 pages)
- Bonterra: ~1,600-1,800 URLs
- Keela: 20K-35K ranking keywords (estimated)
- DonorDock: 467 articles + 100 pages + 88 tag archives (now noindexed)

DonorDock is ~3-4x smaller than content leaders but not catastrophically so. The fix is cluster strategy (pillar + supporting), not brute-force volume.

### 2E. DonorDock's structural advantages vs the field
- **Transparent pricing** ($500/mo flat + 1% online) — every competitor except LGL gates pricing
- **Unlimited contacts** — no contact-tier tax, becomes decisive at 2,500+ contacts vs Bloomerang/DonorPerfect/Neon
- **10 comparison pages** — unmatched in category
- **Strategic llms.txt** (118 lines, hand-written) vs competitors' auto-generated Yoast defaults
- **Strong homepage schema** — SoftwareApplication + AggregateRating + Offer (Bloomerang, DonorPerfect, LGL all missing this)
- **Founder-led with real author schema** — Matt Bitzegaio + Rob Burke as named experts. DonorPerfect has 648 blog posts with ZERO author bylines.
- **SOC 2 Type II** — surfaced in schema
- **Focused Fundraiser Podcast** (49+ episodes) — latent E-E-A-T asset if transcripts + schema added
- **ActionBoard, Smart Steward Method, Otto** — proprietary frameworks/IP worth schema-izing

### 2F. DonorDock's structural gaps
- AI crawler blocking contradicts llms.txt (see 2A)
- FAQ schema missing at scale (see 2B)
- Small content footprint vs top 3 competitors (see 2D)
- No vertical landing pages comparable to LGL's 6 (animal care, human services, arts, land trusts, schools, libraries)
- No glossary program (high-volume AEO opportunity — DonorPerfect has 7 terms, LGL has 0)
- No original research / benchmark report (Virtuous has 5 vertical reports, Neon has "Generosity Report," Bloomerang has retention benchmarks)
- Tagline/positioning soft (no named worldview term — Virtuous owns "Responsive Fundraising," Bloomerang owns "Retention-first")
- Compare pages inconsistent on schema validity — 6 of 9 still ship invalid JSON

---

## 3. Competitive landscape synthesis

### 3A. Top competitive threats (ordered by urgency)

**1. Virtuous** — Biggest content-engine threat. 2.8-10x content lead by asset type, fully operationalized "Responsive Fundraising" category (book, playbook, RNS annual summit, 5 vertical benchmark reports, Chief AI Officer hire). Targets up to $5M fundraising revenue (overlap with DonorDock upper ICP). Must-build: `/compare/virtuous-vs-donordock` before Virtuous builds one first.

**2. Givebutter** — Only competitor actively attacking DonorDock's brand SERP. Their `/alternatives/donordock` ranks #1 for "givebutter vs donordock." Uses shared template (defensible). Social-proof gap is acute: 871 vs 33 reviews. But tipping model is their documented vulnerability — public reviews cite donor-trust issues, "dark pattern" complaints, surprise 3% charges. DonorDock's flat $500 + 1% wins TCO at 2,500+ contacts.

**3. Bloomerang** — Content incumbent, 2,000+ URLs, decade of domain authority on evergreen fundraising terms. But pricing is gated (tiered by contact count, opaque). No public comparison pages at all — uncontested SERP for "Bloomerang vs DonorDock" and "Bloomerang alternative."

**4. Bonterra / Network for Good** — Mentions DonorDock by name dismissively in [/blog/nonprofit-crm-guide](https://www.bonterratech.com/blog/nonprofit-crm-guide) as "entry-level, limited communication features." Soft attack worth counter-messaging. Our own `/compare/network-for-good-vs-donordock` still shows stale $79/mo — needs update to reflect current pricing.

**5. DonorPerfect** — 648 blog posts with zero author bylines is a major E-E-A-T gap DonorDock can exploit. No SoftwareApplication/AggregateRating/FAQPage schema on their homepage. Publishes /fundraising-software/compare-donor-management-systems/ pages for Keela/Bloomerang/Raiser's Edge/Salesforce — but NOT DonorDock.

**6. Neon One** — Cloudflare WAF hard-blocks programmatic access (even Googlebot UA gets 403). "Suite vs ONE plan" is the sharpest positioning wedge: Neon's $99-$409 tiered suite with add-on percentages (+10% memberships, +20% events) vs DonorDock's flat $500 single plan.

**7. Keela** — Canadian-origin. Strong education content (Keela Academy, templates, benchmarks). Does NOT publish "Keela vs DonorDock." Weak on US-specific IRS/501(c)(3) content — uncontested for DonorDock.

**8. Little Green Light** — Tenured but exiting AI-search surface (blocks ClaudeBot/CCBot/Google-Extended). 10,000+ customers as a fixed switcher pool. LGL has only 1 comparison page (Kindful alternative). Price sticker ($45-$135/mo tiered) is a reframe challenge — move the conversation off $/mo onto TCO + capability + time-saved.

### 3B. Content gaps the entire competitive set leaves open

DonorDock can own these without direct contestation:
- **"Small nonprofit" / "first CRM" / "solo ED" queries** — Bloomerang, Virtuous, DonorPerfect all pitch above this ICP
- **Transparent-pricing + TCO content** — almost every competitor gates pricing
- **Platform-fee comparison content** — "1% vs 3%," "true cost of tip-based donation models"
- **Migration content** — "switch from Bloomerang/DonorPerfect/LGL/Keela/Kindful/NFG" — all uncontested
- **US-specific IRS/501(c)(3)/state compliance content** — Keela leans Canadian, others under-serve
- **Church / faith-based / rural / arts nonprofit verticals** — under-served across the field
- **AI-era fundraising operations practical content** — all competitors positioning AI but content is thin
- **"Otto vs Penny vs [Virtuous AI]" head-to-head AI-assistant comparisons**
- **Free template and toolkit library** — Keela owns, others don't invest
- **Annual original-data benchmark report** — Neon has Generosity Report, Virtuous has RNS benchmarks, DonorDock has 7,200 customers + $9B tracked gifts as raw material but no report yet

---

## 4. Top-20 priorities for Phase 2 strategy

Ranked by expected impact × reversibility. Items 1-7 feed directly into Phase 2 pillar/keyword/AEO strategy docs.

### Must-fix foundations (Phase 2 prerequisite)
1. **Unblock AI crawlers in Cloudflare** — GPTBot, ClaudeBot, Google-Extended, PerplexityBot, anthropic-ai, CCBot. Reconcile with llms.txt invitation. Single highest-leverage decision.
2. **Re-paste corrected pricing schema** with "1% platform fee" wording (5-minute fix, blocks AEO on pricing page).
3. **Fix article CMS template featured image** Auto dimensions (1 edit = 467 pages).
4. **Publish 4 missing compare-page schemas** (Bloomerang, Givebutter, eTapestry, Little Green Light + rewrite invalid ones on Network for Good, Neon). Use real FAQ + Review content.
5. **Fix pricing on /compare/network-for-good-vs-donordock** (stale $79/mo → $500/mo).

### Phase 2 strategy inputs (directly feed pillars/keywords/AEO docs)
6. **Pillar candidate list** (feeds `strategy/pillars.md`):
   - Donor Stewardship (54 articles exist; /solution/donor-stewardship pillar)
   - Nonprofit CRM / Donor Database (28 articles; /crm pillar)
   - Online Giving (28 articles; /online-giving pillar)
   - Fundraising Strategy (59 articles; needs new /guides/fundraising-strategy pillar)
   - Donor Engagement (65 articles; needs new hub)
   - AI for Nonprofits (/otto pillar, expanding)
   - Starting a Nonprofit (23 articles; /guides/starting-a-nonprofit)
   - Donor Retention (new pillar; Rob's core narrative)
7. **AEO question set** (feeds `strategy/aeo-questions.md`) — 20 seed questions from Phase 1 AEO audit (brand, competitive, category)
8. **Keyword opportunity list** (feeds `strategy/keyword-universe.md`):
   - "donor management software for small nonprofits" (ICP match, competitor dominated)
   - "nonprofit CRM with text messaging" (differentiator — we have it, no optimized page)
   - "Apple Pay donations for nonprofits" (we have feature, weak page)
   - "donor stewardship plan template" (tool/resource gap)
   - "move management nonprofit CRM" (technical query, high buyer intent)
   - "nonprofit CRM unlimited contacts" (structural differentiator)
   - "1% platform fee vs 3%" (pricing transparency)
   - Plus long-tail vertical: "donor CRM for churches," "fundraising software for schools," etc.
9. **ICP intent map** (feeds `strategy/icp-intent-map.md`) — ICP segments × journey stages × search queries
10. **Competitor landscape doc** (feeds `strategy/competitor-landscape.md`) — synthesis from 8 competitor audits above

### High-impact content builds (Phase 2-3)
11. **Vertical landing pages** — match LGL's 6 (animal care, human services, arts, land trusts, schools, libraries) + add churches, healthcare, advocacy, food banks
12. **Glossary program** — 60 terms at `/glossary/{term}` with DefinedTerm + FAQPage schema
13. **"Switch from [competitor]" migration hub** — Bloomerang, DonorPerfect, LGL, Keela, Kindful, NFG
14. **"Small Nonprofit Fundraising Benchmarks 2026" annual report** — uses DonorDock's 7,200 customers + $9B tracked gifts as original-research asset
15. **Named worldview / category term** (competitive response to Virtuous's "Responsive Fundraising") — candidates: "Smart Stewardship," "Relationship Fundraising," "Lean Fundraising"
16. **Interactive pricing calculator** — shows competitor TCO vs DonorDock flat rate at 500/1000/5000/10000 contacts
17. **`/compare/virtuous-vs-donordock`** and `/compare/keela-vs-donordock` — Phase 2 must-builds before they attack
18. **Podcast episode transcripts + VideoObject schema** — 49+ FF episodes = latent AEO asset

### Foundation-level (ongoing)
19. **Author bylines + Person schema sitewide** — Matt, Rob, Bridgette, Noah, Sami, Scott with /authors/{name} profile pages + knowsAbout markup
20. **SoftwareApplication + Product + AggregateRating on product pages** — /crm, /online-giving, /donor-outreach, /otto currently only have WebPage schema

---

## 5. Phase 2 kickoff inputs

Strategy docs to draft in Phase 2 now have source material from this Phase 1 baseline:

| Strategy doc | Source files |
|---|---|
| `strategy/pillars.md` | 8 pillar candidates above + site audit pillar analysis |
| `strategy/keyword-universe.md` | Keyword opportunity list above + competitor SERP analysis |
| `strategy/aeo-questions.md` | 20 seed questions from AEO audit + competitor FAQ analysis |
| `strategy/icp-intent-map.md` | ICP segments + journey stages (to draft) + competitor ICP overlap |
| `strategy/competitor-landscape.md` | Direct synthesis from 8 competitor audits in `competitors/` folder |
| `strategy/eeat-signals.md` | Authors, credentials, original research, trust signals to build |
| `strategy/content-standards.md` | Voice, structure, schema requirements, internal linking rules |

---

## 6. Process lessons from Phase 1

1. **Audit agents hallucinate when unconstrained** — vertical-auditor invented URL patterns (/success-stories, /solutions) that don't exist; agent claim that homepage was "missing meta description" contradicted direct verification. Phase 2 and beyond: require every factual claim to link to a specific URL, CMS item ID, or brand doc path. Re-verify before acting.
2. **Live-fetching beats generic analysis** — Bloomerang, DonorPerfect, Givebutter audits that actually fetched competitor sites produced higher-quality outputs than Keela (estimated/directional only). Insist on live fetching for future audits.
3. **Schema presence ≠ schema validity** — 6 of 9 compare pages had FAQ schema text but invalid JSON wrappers causing Google to discard everything. Always validate JSON parse, not just regex-match.
4. **Rob's own docs (Projects/Website/schema-markup-audit-2026-03-25.md) should have been the primary source** — ground truth about 1% platform fee was already documented. Phase 2 must start by reading existing brand/messaging docs before drafting new ones.
5. **Source-of-truth hierarchy for Phase 2:** (a) live page content, (b) CMS collection items via Webflow API, (c) brand docs in /Projects/, (d) founder/Rob direct input, (e) audit agent output (treat as draft only).

---

**Phase 1 baseline locked at commit [9cd91d9](https://github.com/DonorDock-team/claude-shared/commit/9cd91d93abaf9d444fcb7a1a914f1e64ca8ffdfe) + competitor audit commits. Ready for Phase 2 kickoff.**
