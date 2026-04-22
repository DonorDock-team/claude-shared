# DonorDock AEO Readiness — Phase 1 Baseline Audit
**Target:** https://donordock.com
**Audit Date:** 2026-04-22
**Auditor:** claude-rank AEO module + manual page-level review
**Pages Analyzed:** 18 (homepage, pricing, features, FAQ, about, 4 comparison pages, 4 sample articles, 3 solution pages, resources, articles index) + full 617-URL sitemap review
**Competitors in scope:** DonorPerfect, Bloomerang, Network for Good, Givebutter, Neon One

---

## Executive Summary

DonorDock has a **surprisingly strong AEO foundation** masked by **three fixable structural problems** that are suppressing featured-snippet and AI-answer visibility. The scanner gives a baseline **AEO score of 65/100** — middle of the pack — but our manual review puts the functional ceiling much higher: the raw content quality is well above the score, but the markup, page structure, and crawler configuration are leaking it.

The single biggest finding is that `/robots.txt` **explicitly blocks every major AI crawler** (GPTBot, ClaudeBot, Google-Extended, CCBot, Applebot-Extended, Amazonbot, Bytespider, meta-externalagent). This is a GEO/AI-search showstopper that will not show up in a traditional SEO audit — ChatGPT, Claude, Perplexity, Google AI Overviews, Gemini, and Apple Intelligence are all being told "do not cite us." Fixing only that one line unlocks the entire AEO strategy.

Second biggest finding: `/faq` already has **114 questions with full FAQPage schema** — a massive corpus of structured Q&A that is among the richest on the site. But because the visible questions are rendered as Webflow styled `<div>` accordions (not `<h2>`/`<h3>`), and because the schema is nested inside a double-`@graph` wrapper that Google's Rich Results Test frequently mis-parses, much of that answer surface is at risk of not earning FAQ rich results.

Third: every content page has the **"Weekly Roundup" newsletter signup form rendered in the DOM before the main content**, so the first paragraph Google and LLMs encounter is "Signup Successful! Oops! Something went wrong…" instead of the article lede. This is directly killing paragraph-snippet eligibility on the entire blog.

Once these three issues are addressed, the site has the raw material (114 FAQ Q&A pairs, 279 articles, 9 comparison pages, BlogPosting schema site-wide, AggregateRating and Review schema already deployed) to become the #1 AEO presence in the nonprofit CRM space within 90 days.

**Priority (do-in-order):**
1. **Unblock AI crawlers in robots.txt** (cannot be overstated)
2. **Move the "Weekly Roundup" form to a side rail or below-fold** on all templates
3. **Add FAQPage schema to `/pricing`** (10+ visible Q&A, currently no FAQ schema) and to all 9 comparison pages
4. **Convert FAQ page accordion headings to proper `<h2>`/`<h3>` semantic elements**
5. **Stand up HowTo schema** on the migration checklist, CRM selection guide, and SROI calculation articles

---

## AEO Readiness Score: 65/100

| Dimension | Score | Notes |
|---|---|---|
| Schema breadth | 72 | Strong: SoftwareApplication, AggregateRating, BlogPosting, Review, FAQPage (one page) |
| Schema completeness | 55 | FAQ schema only on /faq and /compare/network-for-good. HowTo missing everywhere. |
| Direct-answer snippet readiness | 40 | Newsletter form pollutes lede; article bodies bury answers |
| Question-format heading coverage | 25 | 114 questions locked in schema but rendered as divs, not H2/H3 |
| Voice search readiness | 35 | Zero speakable schema; few 29-word voice-length answers |
| List/table snippet readiness | 30 | Zero HTML `<table>` on 9 comparison pages |
| AI crawler accessibility (GEO) | **10** | **CRITICAL**: all major AI bots blocked via robots.txt |
| llms.txt quality | 20 | File exists but served as RTF-encoded blob, not plain text |

---

## 20 Target AEO Questions (seed for strategy/aeo-questions.md)

### Brand-intent (30 days)
1. What is DonorDock? → `/`
2. How much does DonorDock cost? → `/pricing`
3. Is DonorDock free? → `/pricing` (new Q&A)
4. Does DonorDock work for small nonprofits? → `/crm` or new page
5. Can I migrate from Bloomerang to DonorDock? → `/compare/bloomerang-vs-donordock`

### Competitive (60 days)
6. DonorDock vs Bloomerang — which is better for small nonprofits?
7. DonorDock vs DonorPerfect — what's the difference?
8. DonorDock vs Network for Good — which should I choose?
9. DonorDock vs Givebutter — what are the trade-offs?
10. Is there a Bloomerang alternative for small nonprofits? → new page

### Category education (90 days, highest AI-citation volume)
11. What is a nonprofit CRM? → NEW PILLAR
12. What features should a nonprofit CRM have? → `/articles/best-nonprofit-crm`
13. How do I choose a nonprofit CRM?
14. How much does nonprofit CRM software cost? → NEW
15. What is donor stewardship? → NEW PILLAR
16. How do I migrate donor data to a new CRM?
17. What is the best nonprofit CRM for small organizations?
18. Can I use a spreadsheet instead of a CRM?
19. How do I calculate social return on investment for a nonprofit?
20. How long does nonprofit CRM onboarding take? → NEW

---

## Critical Findings Summary

1. **Robots.txt blocks GPTBot, ClaudeBot, Google-Extended, CCBot, Applebot-Extended, Amazonbot, Bytespider, meta-externalagent via Cloudflare managed content** — this is a Cloudflare default that was never consciously chosen. Self-sabotage at platform level.
2. **llms.txt served as RTF file** — any AI parser treats as broken
3. **Newsletter form renders in DOM before article content** — first words crawlers see on every article are "Weekly Roundup Gain free tools... Signup Successful! Oops!"
4. **Nested @graph on /faq schema** — Google Rich Results Test can fail to parse
5. **FAQ questions rendered as divs not H2/H3** — 114 questions' worth of value at risk

## Schema Gaps

**Missing FAQPage schema on:**
- `/pricing` (10+ visible Q&A — biggest single-page AEO win)
- 7 of 9 `/compare/*` pages
- `/integrations`, `/crm`, `/online-giving`

**Missing HowTo schema on:**
- `/articles/nonprofit-crm-migration-checklist` (has Phase 1–5 structure)
- `/articles/how-to-calculate-nonprofit-social-return-on-investment`
- `/articles/best-nonprofit-crm`

**Missing speakable schema:** all 18 pages

**Missing BreadcrumbList:** 17 of 18 pages

## Strategic Phased Rollout

**Weeks 1-2:** Unblock robots.txt, fix llms.txt, move newsletter form, add FAQ schema to /pricing, flatten nested @graph
**Weeks 3-4:** Convert FAQ accordions to H2/H3, add FAQ schema to all 9 compare pages, add HowTo schema, rewrite compare page H1s, add 40-word direct-answer paragraphs, mark up comparison grids as tables
**Weeks 5-8:** 5 missing pillar pages, speakable schema, VideoObject schema, BreadcrumbList sitewide, Course/Event schema for /academy and /webinars-events
**Weeks 9-12:** Competitor displacement via long-tail compare pages, 20-article alternatives cluster, "best nonprofit CRM for [X]" monthly series

**Baseline established. Full manual review plus scanner data in session transcript.**
