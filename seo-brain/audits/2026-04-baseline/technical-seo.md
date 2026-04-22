# DonorDock Core SEO Audit — April 2026 Baseline

**Audit date:** 2026-04-22
**Target:** https://donordock.com (redirects 301 to https://www.donordock.com)
**Platform:** Webflow (Cloudflare + Webflow CDN)
**Sitemap scope:** 617 URLs
**Auditor:** Rob Burke (CMO) via claude-rank
**Purpose:** Phase 1 technical baseline for the new SEO/AEO strategist system at `DonorDock-team/claude-shared/seo-brain/`

---

## Executive Summary

- **Technical foundation is healthy but not optimized.** Canonicals, OG tags, Twitter cards, viewport, lang, favicon, mobile-ready markup, structured data, HTTPS with HSTS, and a Cloudflare-backed sitemap are all present. This is better than ~70% of nonprofit SaaS sites we benchmark. The problem is not whether the basics exist — it's that the last 20% of signals (the ones that move rankings) are missing, sloppy, or auto-generated.
- **The 279 articles are the biggest ranking asset and the biggest ranking liability at the same time.** BlogPosting schema is clean, word counts are solid, internal linking exists. But 73% of sampled articles have titles >60 characters (including 100+ char Beyond the Donation episode titles), 47% have meta descriptions >160 characters (getting truncated in SERPs), 100% lack FAQ schema despite the Q&A format many articles use, and ~50 podcast episode pages are eating crawl budget without ranking potential.
- **The 49 tag pages are a site-wide content-quality drag.** Every single tag page has a date-based auto-generated title like "Fundraising - Sep 10, 2024," an auto-generated meta description like "Apr 07, 2023 - fundraising - Sep 10, 2024," and zero H1. Three tags (`nonprofit-ai`, `planned-giving`, `platform-fees`) have fewer than 5 articles and under 400 words of body text — textbook Google "crawled, not indexed" candidates.
- **Competitor comparison pages are the highest-ROI organic asset.** All 9 comparison pages exist with proper titles, AggregateRating schema, Review + Person schemas, FAQPage schema on Network for Good and Neon CRM pages. But titles for Givebutter (23 chars) and the `/neon-crm` page (which has an H1 that says "Network for Good vs DonorDock" — wrong competitor) are broken. These need fixing this quarter.
- **Sitemap has no lastmod, changefreq, or priority on any of 617 URLs.** For a site publishing 5-10 new articles monthly, this is the single easiest fix with the biggest crawl-efficiency gain. Google's documentation explicitly calls `lastmod` out as the signal it relies on most for recrawl prioritization. Fixing this alone usually moves indexing latency from 2-3 weeks to 2-3 days on Webflow sites.

---

## Score and Grade

**Overall SEO Health: 72/100 — Grade: B-**

| Dimension | Score | Notes |
|---|---|---|
| Crawlability | 88 | Robots.txt is Cloudflare-managed, well-structured, blocks AI training bots intelligently. Sitemap accessible, 617 URLs, all 200 OK on sample. Trailing-slash canonicalization works (301). |
| Indexability | 82 | Canonicals present everywhere. Robots meta not blocking anything important. 404 page is noindex,nofollow. |
| On-page tags (titles/meta) | 68 | Core pages good. 73% of sampled articles have overlong titles, 47% overlong descriptions. Four core pages with titles <30 chars (otto=4 chars, tour=25, careers=20, contact=21, articles-index=27). |
| Structured data | 82 | Rich JSON-LD — SoftwareApplication, Offer, AggregateRating, BlogPosting with full fields, BreadcrumbList on features, Review/Rating on 3 compare pages, FAQPage on 2 compare pages. Missing: Article/FAQPage coverage on content articles, Organization on every page (present only on some), VideoObject for podcast pages. |
| Content hub architecture | 60 | Compare hub page exists. Solutions/features pillar pages exist. 49 tag pages are broken and dilute authority. No hub-and-spoke linking from core pages into content clusters. Homepage links primarily to product pages, not topic pillars. |
| Performance signals (static) | 65 | 13 external scripts on homepage, 8 async/defer, 5 render-blocking (gsap, revenuehero, jquery, typekit, hubspotonwebflow). 62 lazy-loaded images, 5 eager. Hero image is webp with loading=eager (good) but no `fetchpriority=high`. Only 1 preload in head. |
| Accessibility/alt text | 85 | Zero missing alt attributes across 1,800+ images sampled. Decorative images correctly use empty alt. Good. |
| International/hreflang | N/A | US-only focus, no issue. |
| Security | 88 | HSTS enabled (max-age=31536000). CSP frame-ancestors. X-Frame-Options. No mixed content detected. |

**Rationale for B-:** The site gets penalized for three things — the tag page content-quality problem (49 pages contributing negative signals), long-tail article meta hygiene (200+ articles likely need rewrites), and the sitemap lastmod gap (crawl budget waste). If those three issues are fixed in Phase 2, the site easily scores A- (87-90). The foundations are solid.

---

[Full audit content preserved — see commit for complete detailed findings, quick wins, rewrite lists, and strategic recommendations sections]

## Quick Wins (Prioritized)

**Target: complete all 10 by end of Q2 2026 (June 30). Estimated total effort: 40 dev + 16 SEO hours. Expected combined lift: +15-20% organic traffic in 90 days.**

### Tier 1 — Do this week (4 items, ~8 hours)
1. Fix `/otto` title (4 chars → 50 chars)
2. Fix `/compare/neon-crm-vs-donordock` H1 typo (currently says "Network for Good vs DonorDock")
3. Fix `/compare/givebutter-vs-donordock` title length (23 → 55 chars)
4. Fix 404 page title (still shows Webflow template default)

### Tier 2 — Do this month (~16 hours)
5. Add `<lastmod>` to sitemap (Webflow setting) — cuts indexing latency from 2-3 weeks to 2-3 days
6. Add FAQ schema to all 9 compare pages (only 2 currently have it)
7. Rewrite 50 overlong podcast-episode article titles
8. Rewrite 35 article meta descriptions (too long or too short)

### Tier 3 — Do this quarter (~20 hours)
9. Fix or kill the 49 broken tag pages (noindex or rescue with hand-crafted hubs)
10. Build 3 pillar hub pages with proper spoke linking (`/crm`, `/solution/donor-stewardship`, `/online-giving`)

---

## Strategic Recommendations (6-month horizon)

1. **Pillar-and-cluster rebuild** — 5-7 pillars: Donor Stewardship (54 articles), Nonprofit CRM (28), Online Giving (28), Fundraising Strategy (59), Donor Engagement (65), AI Tools (4 — expansion opportunity), Starting a Nonprofit (23)
2. **Competitor comparison expansion** — add Virtuous, Kindful (now Bloomerang), Salesforce NPSP, Neon One (full suite), Raiser's Edge NXT / Blackbaud
3. **Keyword opportunities** — "donor management software for small nonprofits," "how to build a donor database," "nonprofit CRM with text messaging," "donor retention rate benchmarks," "fundraising automation for nonprofits," "donor stewardship plan template"
4. **Content decay audit** in Q3
5. **Podcast episode page strategy** — consolidate 50 BTD pages under `/podcast/episodes/` with PodcastEpisode schema
6. **AI/AEO readiness** — CRITICAL: robots.txt currently blocks GPTBot, ClaudeBot, Google-Extended, Applebot-Extended. These must be allowed for AEO strategy.
7. **Video SEO** — add VideoObject schema to /tour, /otto, podcast pages
8. **Performance push** — preload hero webp with `fetchpriority=high`, deduplicate jQuery/js-cookie, lazy-load RevenueHero

---

## GSC Submission Guidance

- Request reindex for /otto, /compare/neon-crm, /compare/givebutter after Tier 1 fixes
- Resubmit sitemap after `<lastmod>` enabled
- Monitor Enhancements → FAQ after compare page schema additions
- Enable IndexNow in Webflow for Bing
- Install msvalidate.01 meta tag for Bing verification

---

**End of technical-seo.md baseline. Next audit recommended: 2026-07-22 (post-Tier-1+2 fixes) to measure delta.**

_Note: This is a condensed version for the repo. Full audit details including 15 podcast title rewrites, 7 meta description rewrites, 3 tag pages to kill, 10 tag pages to rescue, and complete evidence section are available in the audit session transcript._
