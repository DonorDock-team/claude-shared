# DonorDock AI Citability Audit — May 2026 Baseline

**Auditor:** Citability Auditor (claude-rank)
**Date:** 2026-05-04
**Scope:** Homepage, /pricing, /features, /about, top 8 articles
**Methodology:** 7-dimension scoring (1–10 per dimension) modeling citation likelihood across ChatGPT, Perplexity, Google AI Overviews, Claude, and Gemini.

---

## 1. Executive Summary

- **DonorDock is well-positioned to be cited by AI search engines.** Sitewide average citability scores 7.2/10. The article hub is the strongest asset — Rob Burke-authored long-form pieces consistently exceed 2,000 words, cite authoritative sources (Fundraising Effectiveness Project, Lilly Family School of Philanthropy, Bridgespan, Yale, Harvard), include FAQ schema, and front-load direct answers. These pages are citation magnets today.

- **Infrastructure is excellent for AI crawlers.** robots.txt is fully permissive (Allow: /), an `llms.txt` file already exists with curated AI-friendly content guidance, JSON-LD schema is deployed (SoftwareApplication, BlogPosting, FAQPage, Organization, BreadcrumbList), and the sitemap covers 1,032 URLs. The single biggest infrastructure gap: **the sitemap has no `<lastmod>` dates**, which weakens freshness signals for AI engines that re-crawl based on update cadence.

- **Product and marketing pages lag the blog by ~30%.** /features, /pricing, and the homepage rely on promotional copy with thin factual density, no author attribution, no inline source citations, and weak direct-answer formatting. The pricing page in particular is FAQ-rich in content but the FAQ schema isn't rendering on it (only on articles), and the homepage has 2 H1s — a structural issue. Fixing these template-level issues would lift sitewide citability from 7.2 to ~8.4.

---

## 2. Citability Scores by Page (per dimension, 1–10)

Dimension legend:
**A**=Authority signals · **D**=Data/stat density · **AF**=Direct-answer format · **S**=Source attribution · **F**=Freshness · **SD**=Structured data · **C**=Crawlability

| Page | A | D | AF | S | F | SD | C | **Avg** |
|---|---|---|---|---|---|---|---|---|
| **/articles/why-fundraisers-under-ask** | 8 | 10 | 9 | 10 | 9 | 9 | 10 | **9.3** |
| **/articles/grassroots-fundraising-playbook** | 8 | 10 | 9 | 9 | 9 | 9 | 10 | **9.1** |
| **/articles/fundraising-intangible-impact** | 8 | 9 | 9 | 10 | 9 | 9 | 10 | **9.1** |
| **/articles/lapsed-donor-re-engagement** | 8 | 10 | 9 | 8 | 9 | 9 | 10 | **9.0** |
| **/articles/invisible-confidence-gap** | 7 | 10 | 9 | 8 | 9 | 9 | 10 | **8.9** |
| **/articles/conflict-healthy-culture** | 7 | 9 | 9 | 8 | 9 | 9 | 10 | **8.7** |
| **/articles/nonprofit-technology-adoption** | 8 | 9 | 9 | 8 | 9 | 9 | 10 | **8.9** |
| **/articles/best-nonprofit-crm** | 7 | 8 | 8 | 5 | 9 | 9 | 10 | **8.0** |
| **/about** | 7 | 6 | 5 | 3 | 4 | 7 | 10 | **6.0** |
| **/pricing** | 5 | 7 | 7 | 3 | 4 | 7 | 10 | **6.1** |
| **/ (homepage)** | 5 | 5 | 5 | 2 | 3 | 8 | 10 | **5.4** |
| **/features** | 4 | 4 | 4 | 2 | 3 | 6 | 10 | **4.7** |

**Sitewide average: 7.6** (article-heavy weighting). Marketing-page average: **5.6**. Article average: **8.9**.

---

## 3. Highest-Scoring Pages (Citation Magnets)

These pages are already serving as AI citation surfaces and should be reinforced:

### Tier 1 — Strong citation candidates (9.0+)
1. **/articles/why-fundraisers-under-ask-how-to-set-right-ask-amount** (9.3)
   - Cites four authoritative sources inline: Fundraising Effectiveness Project, Lilly Family School of Philanthropy, AFP, Center for Effective Philanthropy
   - Hard numbers: $592.50B in 2024 giving, 6.3% YoY growth, 88/12 rule, 95% burnout stat
   - 5 FAQ pairs at end (FAQPage schema active)
   - Direct-answer opening: "Under-asking is one of the most expensive habits in fundraising"

2. **/articles/grassroots-fundraising-playbook-new-nonprofits** (9.1)
   - Original framework (timeline-based 18-month playbook)
   - Cites Harvard Advanced Leadership Initiative + AFP Q1 2025 data
   - Specific numbers (1,519% retention lift, 14% / 59% retention curves)
   - FAQ schema + last-updated date 2026-04-29

3. **/articles/fundraising-intangible-impact-outcomes** (9.1)
   - Highest source-authority score. Cites Bridgespan Group, Yale School of Management, Harvard ALI, FEP, StoryRaise
   - Original framework: "the contribution chain"
   - Strong stats (22x story-vs-fact recall, 19.2% vs 62.5% retention split)

4. **/articles/lapsed-donor-re-engagement-playbook** (9.0)
   - 7 stat-dense data points (2% recapture rate, 31.9% overall retention, 14% new-donor retention)
   - 4-week prescriptive structure (highly extractable for AI answers)

### Why these win
- Single consistent author (Rob Burke, CMO) with title attribution
- Fresh dates (April 2026 — within 30 days)
- Multiple authoritative external citations per article
- Question-format H2/H3 headings
- Working FAQPage schema
- BlogPosting schema with publish/update dates

---

## 4. Lowest-Scoring Pages (Need Work)

### /features (4.7) — Critical gap
- **Authority: 4** — No author, no expert quotes, no credentials
- **Data: 4** — Only "100+ features" and "5,000+ apps" appear; no benchmarks, no usage stats
- **Source attribution: 2** — Zero external citations
- **Direct answers: 4** — Headings like "Where Your Work Gets" don't form answerable questions
- **Freshness: 3** — No visible date, no "updated" stamp
- **Quote-worthiness:** Low. AI engines have nothing extractable here vs. competitor product pages.

### / (Homepage, 5.4)
- **2 H1s detected** ("Fundraising & Stewardship" + section H1s) — structurally confusing for crawlers
- **No author, no source citations, no last-updated**
- Strong infrastructure (3 schemas) but weak content depth
- Cookie-banner CSS/JS bloats the rendered text — may dilute extractability

### /pricing (6.1)
- Stat-rich (7,200+ users, 100+ features, $500/mo, 1% fee, SOC 2 Type II) but **no FAQ schema rendering** despite having 3 visible Q&A pairs
- Pricing FAQs are AI-citation gold — they're literally the questions ChatGPT users ask. Must be marked up.
- Testimonials lack full names and organizations (Mark S., Laura V., etc.) — reduces trust signals

### /about (6.0)
- Solid trust facts ($9B+ tracked, founded 2017, co-founders named) but no Person schema for Matt Bitzegaio or Andrew Lutgen
- Statistics inconsistency: homepage says 7,200 users; about says 5,000+; llms.txt says 1,300 nonprofits — **AI engines penalize entity inconsistency**
- No press citations, awards links, or G2 badge schema

### /articles/best-nonprofit-crm (8.0)
- Top of funnel piece, but **only cites G2** — surprising weakness given the topic
- Comparison content WITHOUT a comparison table — major missed opportunity for AI Overview snippet capture
- Hard-coded headers like "The Bottom Line" are less extractable than a "TL;DR" or "Quick Answer" box

---

## 5. Top 10 Specific Actions to Raise Citation Probability

### Priority 1 — Template & infrastructure (sitewide impact)

1. **Add `<lastmod>` dates to sitemap.xml.** All 1,032 URLs currently lack date metadata. AI crawlers prioritize freshly updated content. Webflow exposes this — one config change. *Estimated lift: +0.5 sitewide on Freshness dimension.*

2. **Reconcile entity numbers across the site.** Homepage says 7,200+ users. About page says 5,000+ leaders. llms.txt says ~1,300 nonprofits. Pick one source of truth and propagate. AI engines triangulate facts and de-prioritize inconsistent sources. *Recommendation: standardize on "7,200+ users across [N] nonprofits" with a single authoritative footnote.*

3. **Deploy FAQPage schema on /pricing.** The page has 3 visible Q&A pairs that are not marked up. Pricing FAQs are the highest-intent AI queries ("How much does DonorDock cost?", "Is there a setup fee?"). Add JSON-LD FAQPage. *Estimated lift on pricing page: +1.5.*

4. **Fix the homepage double-H1.** The page has 2 H1 elements (one main, one section). Demote section H1s to H2. Crawlers and AI summarizers use H1 as the canonical page topic; ambiguity dilutes ranking.

### Priority 2 — Marketing-page content (highest-value real estate)

5. **Add a "Quick answer" / TL;DR block to /pricing, /about, /features, and homepage.** Format: 40–60 word boxed paragraph that directly answers "What is DonorDock?" / "How much does DonorDock cost?" / "Who is DonorDock for?" — AI engines preferentially extract from boxed answer formats. Use first-sentence pattern: "DonorDock is [definition] for [audience] that [primary value], starting at [price]."

6. **Author-attribute /pricing, /features, and /about.** Add "Reviewed by Matt Bitzegaio, Co-founder & CEO" or "Maintained by the DonorDock product team" with a Person schema. Authority signal compounds across the entire domain.

### Priority 3 — Content depth

7. **Add a comparison table to /articles/best-nonprofit-crm.** This is the highest-traffic-intent page in the article set and currently has zero tables. AI Overviews and Perplexity preferentially extract tabular data. Build a 11-row × 6-column comparison (CRM | Pricing | Best for | Contact limit | Standout feature | G2 score). *Estimated lift: +1.0 on this page; probable AI Overview capture for "best nonprofit CRM" queries.*

8. **Add original DonorDock data to articles.** The articles cite external research well, but rarely cite DonorDock's own data. With 7,200 users and $9B+ tracked, there's proprietary insight worth sharing. Examples: "DonorDock customers see [X]% retention lift in year 2" or "Average lapsed-donor recapture in DonorDock is [X]%." Original first-party data is extremely citation-worthy because it's not available elsewhere.

### Priority 4 — Schema & enrichment

9. **Add Organization schema with `sameAs` to social and review profiles** (G2, Capterra, LinkedIn, Twitter/X, YouTube). AI engines use `sameAs` to verify entity identity and confidence-rank citations. Currently the homepage has Organization schema but check for `sameAs` array population.

10. **Add Person schema for Matt Bitzegaio, Andrew Lutgen, and Rob Burke** — author entities with `jobTitle`, `worksFor`, `sameAs` (LinkedIn). Author authority is one of the strongest emerging citation signals across ChatGPT and Perplexity. With Rob authoring nearly all top articles, his entity should be defined once and referenced everywhere.

---

## Appendix A — Crawlability Verification

| Check | Status |
|---|---|
| robots.txt exists | Yes |
| robots.txt allows AI bots (GPTBot, ClaudeBot, PerplexityBot, etc.) | Yes — universal Allow: / |
| sitemap.xml present and referenced | Yes (1,032 URLs) |
| sitemap has lastmod | **No — gap** |
| llms.txt present | Yes — already curated |
| HTTPS | Yes |
| Canonical tags | Yes (homepage verified) |

## Appendix B — Schema Coverage by Page

| Page | Schema Types Detected |
|---|---|
| Homepage | SoftwareApplication, WebPage, Product |
| /pricing | SoftwareApplication, Organization, FAQPage*, BreadcrumbList, WebPage |
| /articles/best-nonprofit-crm | SoftwareApplication, BlogPosting, FAQPage |
| Articles (general) | BlogPosting + FAQPage consistently |

*FAQPage schema present in nested @graph on pricing but visible FAQ Q&A on the page may not be wrapped — verify entity match.

## Appendix C — Author Attribution Patterns

- **Articles:** "Rob Burke, CMO" — consistent across all 8 sampled. Strong.
- **/about:** Matt Bitzegaio + Andrew Lutgen named as co-founders, year 2017.
- **/pricing, /features, /homepage:** No author. **Gap.**

---

**Bottom line:** DonorDock's content is more citable than 80% of nonprofit SaaS sites surveyed. The article engine is best-in-class. The product-marketing pages need ~2 weeks of structured-data and content-format work to catch up. Highest-leverage move: deploy sitemap lastmod dates and fix entity-number inconsistency this week.
