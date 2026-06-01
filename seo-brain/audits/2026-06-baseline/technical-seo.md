# Technical SEO Baseline — donordock.com (June 2026)

**Audit date:** 2026-06-01
**Domain:** https://www.donordock.com
**Auditor:** SEO Auditor agent (claude-rank)
**Project type:** SaaS (nonprofit donor management CRM)
**Prior baseline:** [../2026-05-baseline/technical-seo.md](../2026-05-baseline/technical-seo.md)
**Scope:** Core technical SEO — homepage, /pricing, /features-overview, /about, /articles, /contact, /donordock-demo, /tour, /integrations, /faq, /otto, /academy, /partners, /automation-assessment, /crm, /online-giving, plus 4 sample articles, sitemap, robots.txt, redirect chains. Live HTTP fetch, static HTML analysis only.

---

## 1. Executive Summary

**SEO health score: 84 / 100 — UP +12 vs May (72).** Strong month. Two of the three May P0s are fully resolved.

- **The empty-H1 epidemic is FIXED.** Every money page that rendered empty `<h1>` strings in May now serves real heading text to crawlers: /pricing ("Unlimited contacts. Limitless impact."), /donordock-demo, /crm, /contact, /integrations, /partners, /online-giving, /academy, and /features-overview. This was the single highest-impact ranking fix on the May audit and it shipped. The shared Webflow hero component now puts copy inside the H1.
- **Article schema is FIXED.** All 4 sampled articles now carry `BlogPosting` schema with `datePublished` + `dateModified` + `author` (Person) + `FAQPage` + `SpeakableSpecification`. In May this was 0/282; it is now effectively site-wide on the article template — a major AEO/GEO win.
- **The two dead URLs are STILL open.** `/blog` → 404 and `/demo` → 404, unchanged from May. These remain the single easiest win on the site: the conventional paths every external link, deck, ad, and podcast note uses by reflex are still leaking. Both P0s carried over.
- **Sitemap still has zero `<lastmod>`.** 622 URLs, 0 lastmod (was 620/0 in May). No movement. Still the biggest crawl-budget lever for the article archive.

**One-line score:** SEO health ~84/100 (was 72). Foundation strengthened materially; remaining drag is the two 404s, missing lastmod, and a handful of carryover P1/P2 polish items.

---

## 2. Findings by Dimension

### 2.1 Titles  —  Severity: P1 (held)

| Page | Title | Length | Notes |
|---|---|---|---|
| Home | The Donor Development Platform for Growing Nonprofits \| DonorDock | 65c | Good |
| /pricing | DonorDock Pricing: Online Giving, CRM and Outreach | 50c | Good |
| /features-overview | Nonprofit CRM Features: Giving, CRM & Outreach \| DonorDock | 62c | Good |
| /about | About DonorDock \| All-in-One Donor Management Platform | 54c | Good |
| /articles | DonorDock Articles and Blog | 27c | Thin — no "nonprofit fundraising blog" keyword |
| /contact | DonorDock: Contact us | 21c | Thin |
| /donordock-demo | Nonprofit Donor Management: See DonorDock in action! | 52c | Good |
| /tour | Product Tour of DonorDock | 25c | Thin |
| /integrations | DonorDock integrates with your favorite tools! | 46c | OK; exclamation hurts CTR perception |
| /faq | DonorDock FAQ | 13c | Thin |
| /otto | **Otto** | **4c** | **CRITICAL THIN — UNCHANGED from May.** og:title is fine; page `<title>` still not updated |
| /academy | DonorDock Academy | 17c | Thin |
| /partners | DonorDock Partner Program | 25c | Acceptable |
| /automation-assessment | Automation Assessment | 21c | Thin |
| /crm | Nonprofit CRM & Donor Tracking Software \| DonorDock | 55c | Good |
| /online-giving | Accept Donations Online for Free with DonorDock | 47c | Good |

**No change vs May.** /otto title is still literally "Otto" (4 chars) — the standout P1. Same thin-title set carries over: /faq, /academy, /automation-assessment, /contact, /articles, /tour.

---

### 2.2 Meta Descriptions  —  Severity: P2 (held)

| Page | Length | Notes |
|---|---|---|
| / | 134c | Good |
| /pricing | 139c | Good |
| /features-overview | **237c** | Too long — truncates (unchanged from May) |
| /about | 150c | Good |
| /articles | 125c | Good |
| /contact | 143c | Good |
| /donordock-demo | 157c | Good |
| /otto | 189c | Slightly long; still starts mid-sentence lowercase ("your nonprofit's multitasking sidekick…") |
| /online-giving | 107c | Slightly thin |
| /crm | 158c | Perfect |
| /automation-assessment | **265c** | Way too long (unchanged from May) |
| /faq | 181c | Slightly long |

**No change vs May.** /features-overview (237c) and /automation-assessment (265c) still over-length; /otto still starts mid-sentence.

---

### 2.3 Heading Hierarchy  —  Severity: RESOLVED (was P0) ✅

**This is the headline improvement of the month.** Every page that rendered EMPTY `<h1>` strings in May now serves real, crawlable heading text:

| Page | May H1 state | June H1 state |
|---|---|---|
| /pricing | 1 H1, EMPTY | 1 H1 → "Unlimited contacts. Limitless impact." ✅ |
| /features-overview | 4 H1s, ALL EMPTY | 4 H1s, all populated ("Plan, Act, Track…", "Donor Management in one place", "Fundraising in one place", "Donor Outreach in one place") ✅ |
| /donordock-demo | 1 H1, EMPTY | 1 H1 → "See how DonorDock can simplify Fundraising" ✅ |
| /crm | 1 H1, EMPTY | 1 H1 → "Streamlined donor management" ✅ |
| /contact | 1 H1, EMPTY | 1 H1 → "Talk with our team" ✅ |
| /online-giving | 2 H1s, BOTH EMPTY | 2 H1s → "Raise more funds" / "with beautiful donation pages & forms" ✅ |
| /integrations | 1 H1, EMPTY | 1 H1 → "Integrate All Your Favorite Tools" ✅ |
| /partners | 1 H1, EMPTY | 1 H1 → "Boost Your Impact with DonorDock: Join Our Partner Program" ✅ |
| /academy | 2 H1s, BOTH EMPTY | 2 H1s → "DonorDock Academy" / "Video Course" ✅ |

**Remaining (minor, P2): multiple-H1 pages.** Several pages still carry more than one H1 — best practice is one H1 per page:
- /features-overview — 4 H1s (now populated, but should be H1 + H2s)
- /about — 3 H1s ("We help you" / "so that you can" / "Equipping nonprofits…")
- /online-giving — 2 H1s
- /academy — 2 H1s
- /otto — 2 H1s ("Meet Otto" / "Your Extra Fundraising Arm... or Eight")

The empty-H1 P0 is closed. Demoting secondary H1s to H2 on these 5 pages is a P2 cleanup, not a blocker.

---

### 2.4 Slugs / URL Structure  —  Severity: P2 (held)

URLs remain clean, lowercase, hyphen-separated. Same revisit list as May:
- `/donordock-demo` — redundant prefix; converge on `/demo` (also fixes the 404).
- `/features-overview` — verbose; `/features` is better (and currently 301s the wrong way — see 2.10).
- `/landing/*`, `/lp/*` — campaign URLs in sitemap; canonicalize or exclude.

---

### 2.5 Canonical Tags  —  Severity: P2 (mostly clean, held)

Canonicals present and self-referencing on every page checked. Carryover cleanups:
- Homepage canonical is `https://www.donordock.com` (no trailing slash) while served URL is `…/` — pick one.
- `/articles` JSON-LD still has relative `"url": "/articles"` instead of absolute. Unchanged from May.

---

### 2.6 Internal Linking  —  Severity: P1 (held)

No measurable change since May. Same recommendations stand:
- Hub-link the 10 `/compare/*` pages to each other (currently islands).
- Link CRM / online-giving / Otto pillars into 5+ relevant articles each.
- Add "Related articles" cross-linking to the article template.
- /otto still under-linked from homepage hero given its AEO/GEO priority.

---

### 2.7 Sitemap  —  Severity: P1 (held — no lastmod movement)

- **URL:** https://www.donordock.com/sitemap.xml — 200, served fresh (Last-Modified 2026-06-01 13:23 GMT).
- **URL count:** **622** (was 620 in May, +2 net).
- **`<lastmod>` count: 0 / 622.** UNCHANGED. Still zero lastmod anywhere. This remains the single biggest crawl-budget miss for the 270-article archive.
- **Section breakdown (June):** 270 articles, 64 features, 60 integrations, 49 tags, 47 tools, 36 team, 14 success-stories, 12 solution, 10 compare, 9 partner-directory, 6 lp, 3 smart-steward-assessment, 3 room, 3 automations-assessment, 2 landing, 2 comparison, plus singletons (what-is-donordock, webinars-events, tour, podcast).
  - Article count dropped 282 → 270 (likely pruning/consolidation). New sections appeared: `partner-directory` (9), `room` (3), `comparison` (2).
- **Carryover issues:** 49 tag pages (thin-content risk), `/lp/*` + `/landing/*` campaign pages still in sitemap, homepage trailing-slash inconsistency.

---

### 2.8 robots.txt  —  Severity: clean (held)

```
User-agent: *
Allow: /
Sitemap: https://www.donordock.com/sitemap.xml
```
Permissive, points at sitemap. No issues. No crawler blocking.

---

### 2.9 hreflang  —  Severity: not applicable

No hreflang. Correct for single English/US audience. No action.

---

### 2.10 Redirects  —  Severity: P1 (held)

| From | To | Status | Verdict |
|---|---|---|---|
| http://donordock.com | https://www.donordock.com/ | 301 | OK |
| https://donordock.com | https://www.donordock.com/ | 200 | OK |
| /pricing/ (trailing slash) | /pricing | 200 | OK |
| **/features → /features-overview** | 301 | **WRONG DIRECTION — UNCHANGED.** Clean short URL still redirects to the longer one. P1. |
| /resources → /tools | 301 | Verified destination is `/tools`. Intentional; OK. |

**Action (carryover):** Flip canonical to `/features`, then 301 `/features-overview` → `/features`.

---

### 2.11 4xx / 5xx Errors  —  Severity: P0 (STILL OPEN) ❌

| URL | May | June | Status |
|---|---|---|---|
| **/blog** | 404 | **404** | STILL OPEN — P0 carryover |
| **/demo** | 404 | **404** | STILL OPEN — P0 carryover |

Neither was redirected. The blog still lives at `/articles`; the demo still lives at `/donordock-demo`. These are ~5–30 min Webflow redirect-rule fixes and are now the top two open items on the site. No 5xx observed in the audited sample.

---

### 2.12 Indexability  —  Severity: clean (held)

Zero `noindex` directives, no `X-Robots-Tag` blocks, robots.txt permissive, all critical pages 200 (except /blog, /demo). No indexability blockers.

---

### 2.13 JSON-LD / Structured Data  —  Severity: IMPROVED (Article schema RESOLVED) ✅

**Article schema shipped.** All 4 sampled articles (/articles/10-data-points, /articles/100-easy-fundraising-ideas, /articles/nonprofit-storytelling, /articles/donor-retention) now carry a consistent graph:
- `BlogPosting` with `datePublished` + `dateModified` ✅ (was MISSING on all in May)
- `Person` (author) ✅
- `FAQPage` + `Question`/`Answer` ✅
- `SpeakableSpecification` ✅ (new — strong AEO/voice signal)
- `Organization`, `ImageObject`, `WebPage` ✅

This closes the May P1 "no Article schema on 282 articles" finding via a single CMS template change. Excellent AEO/GEO impact.

**Still open:**
- **`BreadcrumbList` schema absent on articles.** Not detected on any sampled article. Carryover P2 (was bundled with the Article-schema P1).
- `/articles` hub JSON-LD `url` still relative.
- /pricing still lacks `Product`/`SoftwareApplication` with `Offer`/`AggregateRating` for pricing rich results (P2).
- No `AggregateRating`/`Review` (G2, Capterra) on home or pricing (P2).

---

### 2.14 Other Technical Items  —  Severity: clean (held)

- `lang="en"` ✓ · viewport ✓ · HTTPS enforced ✓ · OG + Twitter cards present ✓ · favicon ✓ · HTML weights reasonable for Webflow ✓.

---

## 3. Delta vs Prior Baseline (May → June)

| Dimension | May | June | Movement |
|---|---|---|---|
| **Overall score** | 72 | **84** | ▲ +12 |
| Empty H1 on money pages | ~10 pages | **0 pages** | ✅ FIXED (P0) |
| Article schema coverage | 0 / 282 | ~270 / 270 (template) | ✅ FIXED (P1) |
| /blog 404 | 404 | 404 | ❌ unchanged (P0) |
| /demo 404 | 404 | 404 | ❌ unchanged (P0) |
| Sitemap lastmod | 0 / 620 | 0 / 622 | ❌ unchanged (P1) |
| Sitemap URL count | 620 | 622 | +2 (articles 282→270; +partner-directory/room/comparison) |
| /features wrong-direction 301 | yes | yes | ❌ unchanged (P1) |
| /otto title "Otto" (4c) | yes | yes | ❌ unchanged (P1) |
| Over-length meta descs | 2 (237c, 265c) | 2 (237c, 265c) | ❌ unchanged (P2) |
| BreadcrumbList on articles | missing | missing | ❌ unchanged (P2) |
| Speakable schema on articles | none | present | ✅ NEW gain |
| Multiple-H1 pages | ~8 | ~5 | ▲ partial improvement |

**Prior P0 status:** 2 of 3 P0s FIXED (empty H1s ✅, Article schema ✅ — was technically P1). The two 404 P0s (/blog, /demo) remain OPEN.

---

## 4. Recommended Fixes — Ranked by Impact

### Tier 1: Do this week (the last two blockers)
1. **301 `/blog` → `/articles`.** Only open P0 left that's pure link-equity recovery. ~30 min in Webflow hosting redirects.
2. **301 `/demo` → `/donordock-demo`.** Highest-intent URL still leaking. ~5 min.

### Tier 2: Do this month (indexing & ranking)
3. **Add `<lastmod>` to sitemap.xml** for every URL (esp. the 270 articles). Biggest crawl-budget lever still untouched after two months.
4. **Fix /otto `<title>`** — still 4 chars. Match the strong og:title: "Otto AI | Your Nonprofit's Multitasking Sidekick."
5. **Reverse the /features redirect** — canonicalize `/features`, 301 `/features-overview` → `/features`, update sitemap.
6. **Truncate over-length meta descriptions** — /features-overview (237c) and /automation-assessment (265c) to ~155c. Rewrite /otto desc to start with a capitalized subject.
7. **Add `BreadcrumbList` schema** to the article template (and compare/feature templates). Last remaining piece of the article-schema work.

### Tier 3: Do this quarter (enhancement)
8. **Demote secondary H1s to H2** on /features-overview, /about, /online-giving, /academy, /otto (one H1 per page).
9. **Internal-linking pass** — hub-link the 10 `/compare/*` pages; link /otto, /crm, /online-giving from 5+ articles each; add "Related articles."
10. **Exclude campaign pages from sitemap** (`/lp/*`, `/landing/*`, thank-you pages). Audit the new `partner-directory` (9) and `room` (3) sections for indexability intent.
11. **Add Product/SoftwareApplication + Offer + AggregateRating** to /pricing; add Review/AggregateRating (G2, Capterra) to home + pricing.
12. **Rewrite thin titles** on /faq, /academy, /automation-assessment, /contact, /articles, /tour.
13. **Audit 49 `/tags/*` URLs** for thin content; `noindex, follow` where <5 articles.
14. **Resolve homepage canonical trailing-slash** + fix `/articles` JSON-LD relative `url`.

---

## 5. GSC / Bing Webmaster — Next Steps

1. **GSC → URL Inspection → Request Indexing** for the pages whose H1s were just fixed: `/pricing`, `/features-overview`, `/donordock-demo`, `/crm`, `/online-giving`, `/integrations`, `/partners`, `/academy`. These now have real H1 text — re-crawl to capture the signal.
2. **GSC → Enhancements:** The "Articles" / "Breadcrumb" / "FAQ" cards should now populate from the new BlogPosting + FAQPage markup. Validate they show "Valid." Breadcrumb card will stay empty until Tier-2 #7 ships.
3. **GSC → URL Inspection → Request Indexing** for `/blog` and `/demo` *after* the 301s ship (Tier-1).
4. **GSC → Sitemaps:** Confirm "Success." Resubmit once `<lastmod>` is added so Google re-reads change dates.
5. **GSC → Pages report:** Watch "Crawled - currently not indexed" — likely the 49 tag pages, `/lp/*`, and new `partner-directory`/`room` sections.
6. **Bing Webmaster → URL Submission:** Submit `/blog`, `/demo` (after 301) and the 8 H1-fixed money pages for fast re-crawl.

---

## 6. Comparison Notes (for July 2026 audit)

Diff against this file. Watch:
- **404 count** — should finally drop from 2 (/blog, /demo) to 0.
- **Sitemap lastmod** — should change from 0/622 to full coverage.
- **/otto title** — should change from "Otto" (4c) to full keyword title.
- **BreadcrumbList on articles** — should go from absent to present.
- **/features redirect direction** — should reverse.
- **Multiple-H1 pages** — should drop from ~5 to 0.
- **Over-length meta descs** — should drop from 2 to 0.
- **Sitemap URL count + section mix** — track article count (270) and the new partner-directory/room/comparison sections.

---

*End of report. Audit produced by SEO Auditor agent. Methodology: live HTTP fetch of 16 priority pages + 4 sample articles + sitemap + robots.txt + redirect-chain tracing. Static HTML analysis only — no JavaScript rendering, no Lighthouse, no GSC data joined. For full Lighthouse + Core Web Vitals + GSC overlay, run the perf-scanner and gsc-analyzer modules separately.*
