# Technical SEO Baseline — donordock.com (May 2026)

**Audit date:** 2026-05-04
**Domain:** https://www.donordock.com
**Auditor:** SEO Auditor agent (claude-rank)
**Project type:** SaaS (nonprofit donor management CRM)
**Scope:** Core technical SEO — homepage, /pricing, /features, /about, /blog, /contact, /demo, plus 10 supporting pages and a sample article. Sitemap-wide spot checks included.
**Baseline file:** This is the May 2026 baseline; future months should diff against this file.

---

## 1. Executive Summary

- **Two high-traffic intent URLs return 404s** — `/blog` and `/demo` are dead. These are the URLs prospects, sales decks, and external links most often point at. Every external link, podcast mention, ad, and old-deck reference using these paths is currently leaking. P0.
- **Heading hierarchy is broken on most money pages.** Pricing, /features-overview, /contact, /donordock-demo, /crm, /integrations, /partners, /online-giving and others render H1 elements in the markup that are *empty* (text styled in a child div, not in the H1 itself). Webflow renders no actual H1 string for crawlers on pricing — the most commercially important page on the site.
- **Otherwise the technical foundation is solid.** robots.txt is permissive and points at the sitemap, sitemap.xml lists 620 URLs (282 articles), canonicals are present and correct on every page checked, OG/Twitter tags are universal, JSON-LD is on every audited page (Organization, WebPage, FAQPage, Article, BreadcrumbList variants), HTTPS is enforced, and apex resolves cleanly to www.

**One-line score:** SEO health ~72/100. Foundation is healthy; lost-URL leakage and missing H1 strings are dragging it down.

---

## 2. Findings by Dimension

### 2.1 Titles  —  Severity: P1

| Page | Title | Length | Notes |
|---|---|---|---|
| Home | The Donor Development Platform for Growing Nonprofits \| DonorDock | 65c | Good |
| /pricing | DonorDock Pricing: Online Giving, CRM and Outreach | 50c | Good |
| /features-overview | Nonprofit CRM Features: Giving, CRM & Outreach \| DonorDock | 62c | Good |
| /about | About DonorDock \| All-in-One Donor Management Platform | 54c | Good |
| /articles | DonorDock Articles and Blog | 27c | **Thin** — no keyword for "nonprofit fundraising blog" or similar |
| /contact | DonorDock: Contact us | 21c | **Thin** — no keyword/value |
| /donordock-demo | Nonprofit Donor Management: See DonorDock in action! | 52c | Good |
| /tour | Product Tour of DonorDock | 25c | **Thin** — could include "nonprofit CRM" |
| /integrations | DonorDock integrates with your favorite tools! | 46c | OK but exclamation hurts CTR perception |
| /faq | DonorDock FAQ | 13c | **Thin** — should be "DonorDock FAQ \| Nonprofit CRM Questions" or similar |
| /otto | Otto | **4c** | **CRITICAL THIN.** Single word title. og:title is fine ("Otto AI \| Your Nonprofit's Multitasking Sidekick") — page <title> was not updated to match |
| /academy | DonorDock Academy | 17c | Thin |
| /partners | DonorDock Partner Program | 25c | Acceptable |
| /automation-assessment | Automation Assessment | 21c | **Thin** — needs brand and keyword |
| /crm | Nonprofit CRM & Donor Tracking Software \| DonorDock | 55c | Good |
| /online-giving | Accept Donations Online for Free with DonorDock | 47c | Good |

**P1 issues:** /otto, /faq, /academy, /automation-assessment, /contact, /articles, /tour all have weak/short titles missing pillar keywords (nonprofit, fundraising, donor management).

---

### 2.2 Meta Descriptions  —  Severity: P2

All audited pages have meta descriptions. Length checks:

| Page | Meta-desc length | Notes |
|---|---|---|
| /home | 134c | Good (target 120-160) |
| /pricing | 139c | Good |
| /features-overview | **237c** | Too long — Google will truncate ~160c, second half is wasted |
| /about | 150c | Good |
| /articles | 125c | Good |
| /contact | 143c | Good |
| /donordock-demo | 157c | Good |
| /tour | 150c | Good |
| /integrations | 139c | Good |
| /faq | 181c | Slightly long |
| /otto | 189c | Slightly long, also starts mid-sentence ("your nonprofit's multitasking sidekick…" — no leading capital, no subject) |
| /online-giving | 107c | Slightly thin |
| /crm | 158c | Perfect |
| /automation-assessment | **265c** | Way too long — will truncate ungracefully |

**P2 issues:** /features-overview (237c), /automation-assessment (265c), /otto (starts mid-sentence) need rewrites.

---

### 2.3 Heading Hierarchy  —  Severity: P0

This is the biggest discovered issue. Several pages render `<h1>` tags that contain no text — Webflow places the visible heading copy in a child element, leaving the H1 empty for crawlers and screen readers.

**Pages with EMPTY H1 strings (most critical):**

- `/pricing` — 1 H1 element, text is empty. Pricing is the highest-intent page on the site.
- `/features-overview` — **4 H1 elements**, all empty.
- `/contact` — 1 H1 element, empty.
- `/donordock-demo` — 1 H1 element, empty (the demo signup landing page!)
- `/crm` — 1 H1 element, empty.
- `/integrations` — 1 H1 element, empty.
- `/partners` — 1 H1 element, empty.
- `/online-giving` — 2 H1 elements, both empty.
- `/academy` — 2 H1 elements, both empty.

**Pages with multiple H1s:**

- `/home` — 2 H1s (`Fundraising & Stewardship` + one A/B test variant — Optibase test wrapping)
- `/about` — 3 H1s (`We help you`, `so that you can`, third empty)
- `/features-overview` — 4 (all empty)
- `/otto` — 2 H1s
- `/online-giving` — 2 H1s
- `/academy` — 2 H1s
- `/compare/spreadsheets-vs-donordock` — 3 H1s
- `/compare/network-for-good-vs-donordock` — 2 H1s

**Pages with clean, single, non-empty H1s (good examples):**

- `/articles` — `Donor Development Hub`
- `/automation-assessment` — `What level of automation is your nonprofit at?`
- `/faq` — `Frequently asked questions`
- `/tour` — `Take a Tour of DonorDock`
- 5 of 7 compare pages
- All sampled article pages (e.g., `/articles/10-data-points` → `Are you collecting these 10 donor data points?`)

**Why this matters:** Google uses H1 as a strong topical signal, especially for AI Overviews and AEO. Empty H1 tags on pricing, demo and CRM pages are unforced ranking errors. This is a Webflow template-level issue — fixing the template fixes ~10+ pages at once.

---

### 2.4 Slugs / URL Structure  —  Severity: P2

URLs are clean, lowercase, hyphen-separated, descriptive. Examples that score well:
- `/pricing`, `/about`, `/tour`, `/integrations`, `/faq`
- `/compare/donorperfect-vs-donordock`
- `/articles/100-easy-fundraising-ideas`

**Slugs to revisit:**

- `/donordock-demo` — redundant prefix; standard convention is `/demo` (which would also fix the 404 — see 2.13). Consider 301'ing `/donordock-demo` → `/demo` once /demo is built.
- `/features-overview` — verbose. `/features` is better (currently 301s to /features-overview, the *opposite* of best practice).
- `/convince-your-team` — unusual but ranks for branded long-tail; keep.
- `/landing/whichhatareyou` — campaign URL inside sitemap; should be canonicalized OR excluded from sitemap (low evergreen value).
- `/links` — generic; if this is a Linktree-style page, exclude from sitemap.

---

### 2.5 Canonical Tags  —  Severity: P2 (mostly clean)

Canonicals are present and correctly self-referencing on every page audited. Two cleanup items:

- `/articles` JSON-LD has `"url": "/articles"` (relative) instead of absolute `https://www.donordock.com/articles`. Cosmetic, but Google prefers absolute URLs in schema.
- `/home` (root) canonical is `https://www.donordock.com` (no trailing slash) while the actual served URL is `https://www.donordock.com/`. Both resolve, but pick one to avoid mixed signals.

---

### 2.6 Internal Linking  —  Severity: P1

Homepage has **95 internal (relative) links** plus 6 absolute internal links — healthy on a count basis. However:

- Many of those are footer/nav links repeated. Effective unique destination links from the body region appear closer to ~25.
- `/articles` (the blog hub) and individual articles don't appear to receive prominent internal links from money pages (pricing, /tour). High-traffic articles like `/articles/100-easy-fundraising-ideas` are not surfaced from `/online-giving`, `/crm`, etc.
- No "Related articles" or topic-cluster cross-linking visible on the article page sampled (`/articles/10-data-points`).
- `/otto` (Otto AI page) is not strongly linked from the homepage hero or features pages — given it's the strongest AEO/GEO topic right now (AI for nonprofits), it deserves more internal love.
- The `/compare/*` cluster has 7 pages (DonorPerfect, eTapestry, Little Green Light, Neon, Network for Good, Salsa, Spreadsheets). These should hub-link to each other ("Also comparing DonorDock to…") — currently each is an island.

**Recommendation:** Build a topic-cluster internal-linking pass: link the CRM pillar (`/crm`), online giving pillar (`/online-giving`), and Otto pillar (`/otto`) into 3-5 high-traffic articles each.

---

### 2.7 Sitemap  —  Severity: P1

- **URL:** https://www.donordock.com/sitemap.xml
- **Status:** 200, served fresh (Last-Modified header today, 2026-05-04 15:50:23 GMT)
- **URL count:** 620 entries
- **Section breakdown:**
  - 282 articles
  - 62 features (likely individual feature pages)
  - 60 integrations (individual integration pages)
  - 49 tags (article tag pages)
  - 47 tools
  - 36 team (likely staff bio pages)
  - 14 success-stories
  - 10 solution
  - 10 compare (only 7 in markup; sitemap has extras — investigate)
  - 6 lp (landing pages)
  - 3 smart-steward-assessment
  - 3 automations-assessment

**Issues:**

- **No `<lastmod>` tags anywhere.** 620 URLs and zero lastmod is a big miss — Googlebot uses lastmod to prioritize recrawl. Adding lastmod to articles alone would meaningfully accelerate indexing of new content. P1.
- **49 tag pages** in the sitemap. Tag/taxonomy pages are often thin and duplicate-content prone. Spot-check these for indexability; consider noindex if they are auto-generated thin pages.
- **6 landing pages (`/lp/*`) and `/landing/whichhatareyou`** in the sitemap. Campaign LPs typically should NOT be in the sitemap (they have short shelf lives and dilute crawl budget). Verify, then exclude.
- Sitemap has `https://www.donordock.com` as homepage (no trailing slash), while the served URL has a trailing slash. Minor consistency issue.
- No sitemap index file — fine at 620 URLs, but if the article count grows past ~5,000 you'll want to split into article/integration/tools/static sub-sitemaps.

---

### 2.8 robots.txt  —  Severity: clean

```
User-agent: *
Allow: /
Sitemap: https://www.donordock.com/sitemap.xml
```

Permissive, points at the sitemap correctly. **No issues.** Could optionally add explicit `Disallow:` for `/landing/`, `/lp/`, `/automation-assessment/` thank-you pages, etc., but not urgent.

---

### 2.9 hreflang  —  Severity: not applicable

No hreflang tags on any page. **This is correct** — DonorDock serves a single English/US audience. No action needed unless international expansion is planned.

---

### 2.10 Redirects  —  Severity: P1

| From | To | Status | Verdict |
|---|---|---|---|
| http://donordock.com | https://www.donordock.com/ | 301 chain | OK (Cloudflare handles) |
| https://donordock.com | https://www.donordock.com/ | resolves to 200 | OK |
| /pricing/ (trailing slash) | /pricing | 200 (treated equal) | OK — Webflow accepts both, no canonical conflict because canonical points to no-slash version |
| **/features → /features-overview** | 301 | **WRONG DIRECTION** — short, clean URL is redirecting to a longer, less-clean URL. Best practice is the reverse. P1. |
| /resources | 301 (target unknown — check) | Verify destination and that it's needed. |

**Action:** Swap the canonical URL from `/features-overview` to `/features`, then 301 `/features-overview` → `/features`. Update sitemap.

---

### 2.11 4xx / 5xx Errors  —  Severity: P0

Two confirmed P0 dead URLs:

- **`/blog` → 404.** This is the canonical "blog" path that 90%+ of external mentions, ads, decks, podcast notes, and social posts will use by reflex. Currently the blog lives at `/articles`. Either 301 `/blog` → `/articles`, or rebuild `/blog` as the primary path and 301 `/articles` → `/blog` (preserving article URLs as `/blog/article-slug`).
- **`/demo` → 404.** The demo lives at `/donordock-demo`. The shorter path is what people type. 301 `/demo` → `/donordock-demo` immediately. (Better long-term: rename `/donordock-demo` to `/demo`.)

No 5xx errors observed in the audited sample.

---

### 2.12 Indexability  —  Severity: clean

- Zero `noindex` directives observed on any audited page.
- No `X-Robots-Tag` blocking headers.
- robots.txt is permissive.
- All critical pages return 200 (except /blog and /demo above).

**No indexability blockers.** Google should be able to crawl and index everything DonorDock wants indexed.

---

### 2.13 JSON-LD / Structured Data  —  Severity: P2 (good shape, opportunities exist)

Every audited page has 2 JSON-LD blocks. Confirmed types:

- **Home:** WebPage + SoftwareApplication
- **Pricing:** Organization graph (founders, sameAs links)
- **FAQ:** FAQPage with Question/Answer pairs (excellent — eligible for rich results)
- **Articles hub:** CollectionPage
- **Article sample (`/articles/10-data-points`):** has JSON-LD but **NO `Article` schema and NO `BreadcrumbList` schema** detected — this is a P1 miss for individual articles. Article schema with author, datePublished, dateModified is critical for E-E-A-T.

**Recommendations:**

- P1: Add `Article` schema (with `author`, `datePublished`, `dateModified`, `headline`, `image`) to all 282 articles. This is a Webflow CMS template change.
- P1: Add `BreadcrumbList` schema to articles, compare pages, and feature pages.
- P2: Add `Product` or `SoftwareApplication` with `Offer`/`AggregateRating` to /pricing for rich results eligibility.
- P2: Add `Review` or `AggregateRating` (G2, Capterra reviews) to homepage and pricing.

---

### 2.14 Other Technical Items  —  Severity: clean

- HTML lang attribute: `lang="en"` ✓
- Viewport meta: `width=device-width, initial-scale=1` ✓
- HTTPS: enforced site-wide ✓
- Open Graph and Twitter Card: present on every audited page ✓
- Favicon: present ✓
- Page weights: 100KB-260KB HTML — reasonable for Webflow

---

## 3. URLs With Issues (Quick Reference)

| URL | Issue | Severity |
|---|---|---|
| https://www.donordock.com/blog | 404 | P0 |
| https://www.donordock.com/demo | 404 | P0 |
| https://www.donordock.com/pricing | Empty H1 | P0 |
| https://www.donordock.com/features-overview | 4 empty H1s | P0 |
| https://www.donordock.com/donordock-demo | Empty H1 | P0 |
| https://www.donordock.com/contact | Empty H1 | P1 |
| https://www.donordock.com/crm | Empty H1 | P1 |
| https://www.donordock.com/integrations | Empty H1 | P1 |
| https://www.donordock.com/online-giving | 2 empty H1s | P1 |
| https://www.donordock.com/partners | Empty H1 | P1 |
| https://www.donordock.com/academy | 2 empty H1s, thin title | P1 |
| https://www.donordock.com/otto | Title is just "Otto" (4 chars) | P1 |
| https://www.donordock.com/about | 3 H1s | P1 |
| https://www.donordock.com/features → /features-overview | Wrong-direction 301 | P1 |
| https://www.donordock.com/automation-assessment | Meta desc 265c (truncates) | P2 |
| https://www.donordock.com/features-overview | Meta desc 237c (truncates) | P2 |
| https://www.donordock.com/articles/* | No Article schema, no Breadcrumb schema (282 articles affected) | P1 |
| sitemap.xml | No `<lastmod>` on any URL (620 affected) | P1 |
| sitemap.xml | Includes `/landing/*` and `/lp/*` campaign pages | P2 |
| /compare/spreadsheets-vs-donordock | 3 H1s | P2 |
| /compare/network-for-good-vs-donordock | 2 H1s | P2 |

---

## 4. Recommended Fixes — Ranked by Impact

### Tier 1: Do this week (blocking issues)

1. **301 `/blog` → `/articles`.** Recovers external link equity from every podcast, ad, deck, and social post that uses the conventional /blog path. ~30 minutes in Webflow hosting redirect rules.
2. **301 `/demo` → `/donordock-demo`.** Same logic — direct URL leakage on the highest-intent page on the site. ~5 minutes.
3. **Fix the empty-H1 Webflow template/symbol.** This is the highest-impact ranking fix on the audit. Identify the shared hero component used on /pricing, /features-overview, /donordock-demo, /crm, /contact, /online-giving, /integrations, /partners, /academy and put the visible heading text inside the actual `<h1>` tag (not a child div styled as H1). Estimated reach: 10+ money pages fixed in a single template change.

### Tier 2: Do this month (indexing & ranking)

4. **Add Article + BreadcrumbList schema to all 282 articles.** Single CMS template change, massive AEO/GEO impact. Include `author`, `datePublished`, `dateModified`, `headline`, `image`.
5. **Add `<lastmod>` to sitemap.xml** for every URL. If Webflow's auto-sitemap doesn't support this, regenerate weekly. Single biggest crawl-budget win for the article archive.
6. **Rewrite thin titles** on /otto (especially — "Otto" is 4 characters), /faq, /academy, /automation-assessment, /contact. Match the og:title pattern that's already strong (e.g., Otto's og:title is `Otto AI | Your Nonprofit's Multitasking Sidekick`).
7. **Truncate over-length meta descriptions** on /automation-assessment (265c) and /features-overview (237c) to ~155c.
8. **Reverse the /features redirect.** Make `/features` the canonical URL; 301 `/features-overview` → `/features`. Clean URL = better CTR + cleaner backlinks.

### Tier 3: Do this quarter (enhancement)

9. **Internal-linking pass:** Hub-link the 7 `/compare/*` pages to each other. Link `/otto`, `/crm`, `/online-giving` from 5+ relevant articles each. Add "Related articles" to article template.
10. **Exclude campaign pages from sitemap** (`/landing/*`, `/lp/*`, thank-you pages). Prevents crawl-budget waste and indexing of low-value pages.
11. **Add Product/SoftwareApplication schema with Offer + AggregateRating** to /pricing — unlocks pricing rich results in SERP.
12. **Audit the 49 `/tags/*` URLs** for thin content. Consider `noindex, follow` on auto-generated tag pages with <5 articles.
13. **Resolve the homepage canonical mismatch** — pick `https://www.donordock.com/` (with trailing slash, matching served URL) and use it consistently in canonical, sitemap, and JSON-LD.
14. **Fix /articles JSON-LD** — change `"url": "/articles"` to absolute `"url": "https://www.donordock.com/articles"`.

---

## 5. GSC / Bing Webmaster — Next Steps

After Tier 1 fixes ship:

1. **GSC → Sitemaps:** Confirm sitemap is "Success" status. Resubmit after lastmod is added.
2. **GSC → URL Inspection → Request Indexing** for: `/blog` (after 301), `/demo` (after 301), `/pricing` (after H1 fix), `/donordock-demo` (after H1 fix), `/features-overview` or `/features` (whichever you canonicalize).
3. **GSC → Pages report:** Look for "Crawled - currently not indexed" — likely candidates are the thin tag pages and any /lp/* in the sitemap.
4. **GSC → Enhancements report:** After Article schema deploys, the "Articles" enhancement card should populate. Validate FAQPage and Organization markup are showing as "Valid."
5. **Bing Webmaster Tools → URL Submission:** Submit `/blog`, `/demo`, `/pricing`, `/donordock-demo` after fixes. Bing's URL Submission API gives near-instant re-crawl.
6. **GSC → Coverage:** Check for any URLs marked "Excluded → Redirect" — confirm `/features-overview` shows up as a redirect once the canonical is flipped.

---

## 6. Comparison Notes (for next month's audit)

When running the June 2026 baseline, diff against this file. Specifically watch:

- **404 count** — should drop from 2 (/blog, /demo) to 0.
- **Empty H1 count** — should drop from ~10+ pages to 0.
- **Thin title count** (<25 chars on commercial pages) — should drop from 5 to 0-1.
- **Sitemap lastmod presence** — should change from 0 / 620 to 620 / 620.
- **Article schema coverage** — should rise from 0 / 282 to 282 / 282.
- **Total indexable URLs** — track sitemap count change month over month.
- **Compare-page H1 cleanliness** — should drop from 2 problem pages to 0.

---

*End of report. Audit produced by SEO Auditor agent. Methodology: live HTTP fetch of 16 priority pages + 1 sample article + sitemap + robots.txt. Static HTML analysis only — no JavaScript rendering, no Lighthouse, no GSC data joined. For full Lighthouse + Core Web Vitals + GSC overlay, run the perf-scanner and gsc-analyzer modules separately.*
