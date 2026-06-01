# June 2026 Baseline — Executive Summary

**Period:** 2026-06-01 (single-run snapshot)
**Scope:** Site audit (9 dimensions) + competitor audit (8 vendors)
**Owner:** Rob Burke (CMO, rburke@donordock.com)
**Prior baseline:** [`2026-05-baseline`](../2026-05-baseline/executive-summary.md)
**Status:** Monthly tracking refresh. Delta-driven. No remediation in this run.

---

## TL;DR (5 bullets)

1. **Three of May's five P0 template fixes shipped — and they moved the numbers.** Empty `<h1>` tags on 9 money pages are FIXED, articles gained static `BlogPosting` + dates + author + Speakable, and the sitewide rolling-future-date bug is FIXED. Technical SEO jumped 72→84, Performance 62→71, Content 58→64. Best month-over-month site-health gain since the April Cloudflare unblock.
2. **But the #1 P0 — JS-injected article FAQPage — is NOT confirmed fixed, and the auditors disagree.** The schema specialist traced the FAQPage to a runtime Webflow IIFE (`document.createElement('script')`) still invisible to GPTBot/ClaudeBot/CCBot/PerplexityBot/Bingbot across 281+ articles. The technical-SEO and AEO auditors saw FAQPage in the rendered DOM and marked it fixed. **Treat as OPEN until verified in Rich Results Test / raw curl.** This is the single most important thing for Rob to check.
3. **New P0 regression: `/compare/bloomerang-vs-donordock` JSON-LD has a trailing comma in `featureList` → the entire schema block fails to parse → all structured data on the page is dropped by every crawler.** Confirmed independently by the schema and vertical auditors. ~5-minute fix; standardize the compare cluster on the clean `/compare/givebutter` template.
4. **Givebutter is the escalating competitor again — and DonorDock isn't countering it.** Givebutter is converting its Wallet into a full nonprofit operating bank (Spend Cards + Mobile Check Deposit "coming soon," new Nonprofit Investing pillar) and won Fast Company Most Innovative 2026. Their `/alternatives/donordock` page is STILL stale (Sept 2023 data) and DonorDock's own `/compare/givebutter-vs-donordock` still doesn't mention the Wallet or the stale-data angle. Review velocity did collapse (+470/mo → +87/mo), the one piece of good news.
5. **No competitor launched a DonorDock-targeted comparison page this month** (Bloomerang, DonorPerfect lanes still open for a 2nd month) — but **Neon One now names DonorDock directly in two high-ranking listicles** ("7 Best CRMs for Small Nonprofits," "21 Best Donor Management Software"), fair-to-favorable. Soft escalation: more "DonorDock vs Neon" intent now resolves on Neon's domain.

---

## 1. Site health — June vs May

| Dimension | May 2026 | June 2026 | Trend | Notes |
|---|---|---|---|---|
| Technical SEO | 72/100 | **84/100** | 🟢 Improved (+12) | Empty H1s FIXED on all 9 money pages (May P0 #3). Articles gained static BlogPosting + dates + author + Speakable. Open: `/blog` & `/demo` still 404; sitemap still 0 `<lastmod>`. |
| AEO Readiness | 54/100 | **59/100** | 🟢 Improved (+5) | Real gain, not measurement. Articles added FAQPage (1 Q each — target 3–5). HowTo schema still missing everywhere (#1 unclaimed win). `/contact` regressed to zero JSON-LD. Homepage/`/features`/`/about` floor unchanged. |
| GEO Readiness | 2.5/3 (Optimized) | **2.5/3 (Optimized)** | ⚪ Held | Regression watch PASSED — all 15 AI crawlers re-verified live, all HTTP 200; only Bytespider 403. May Cloudflare unblock held a full cycle. `/llms-full.txt` still 404. 0 of 10 May content recs implemented. |
| AI Citability | 76/100 | **76/100** | ⚪ Held | Consolidation month. Articles avg 8.9; marketing pages 5.7. Date bug FIXED. Entity inconsistency got **WORSE** (now 4-way). `/faq` newly live with 80+ Q&A but ZERO FAQPage schema. |
| Performance | 62/100 | **71/100** | 🟢 Improved (+9) | Render-blocking head scripts 9→2 (jQuery/GSAP/RevenueHero/HubSpot moved to body); Brotli now on CSS bundle; Facebook Pixel (~550 KB) removed. Open: 1.39 MB hero GIF unchanged; duplicate jQuery (3.5.1+3.6.0) unchanged; `fetchpriority` regressed (sub-pages emit `"low"`). |
| Security | 67/100 | **67/100** | ⚪ Held | Zero remediation — all 5 recommended headers still missing (CSP/X-Content-Type-Options/Referrer-Policy/Permissions-Policy/COOP). Cert auto-renewed healthy (notBefore advanced to May 3; valid through Aug 1 2026). _Note: May prose rendered "72" but tracked baseline carried 67; using 67 — reconcile to one number going forward._ |
| Schema coverage | mixed (C+) | **mixed (C+)** | ⚪ Held + 🔴 new regression | `/pricing` still gold-standard (added a WebSite node). Article dates de-templated. **NEW: `/compare/bloomerang-vs-donordock` JSON-LD trailing-comma parse failure.** JS-FAQ + duplicate AggregateRating + `/contact` zero-schema all still open. |
| Content quality | 58/100 | **64/100** | 🟢 Improved (+6) | Rolling-date bug FIXED (drove the gain). **Article count dropped 449 → 351 (−98 / −22%)** — needs crawl-vs-sitemap diff to confirm intentional prune vs accidental de-index. Flagship pillar internal-linking now live (~12 in-content links). Thin `/team/*` + `/tags/*` unchanged. |
| Vertical SEO | ~50/100 | **52/100** | 🟢 Slight improvement (+2) | New `/features/trust-and-security` page (SOC 2). `/crm` gained `applicationSubCategory`. **Free-trial CTA scaffolding appeared but is non-functional** (every "Start for Free" button renders "Schedule a Demo" → `/donordock-demo`). G2/Capterra still missing from Organization `sameAs` (2nd month). |

### What landed since May (visible improvements)

- ✅ **Empty `<h1>` on 9 money pages FIXED** — was May P0 #3, shipped sitewide via the shared template.
- ✅ **Sitewide rolling-future-date bug FIXED** — articles now carry real, varied past dates (was May P0 #4, ~449 articles).
- ✅ **Articles gained static schema** — BlogPosting + datePublished/dateModified + author + Speakable now present.
- ✅ **Render-blocking scripts 9 → 2** — jQuery, GSAP, RevenueHero, HubSpot bridge relocated out of `<head>`; Brotli enabled; Facebook Pixel removed. Drove the +9 performance gain.
- ✅ **`/pricing` schema deepened** — added a WebSite node; remains the best-in-class template.
- ✅ **Cert auto-renewal verified healthy** — GTS rotated May 3, valid through Aug 1 2026.

### What surfaced new (June findings not flagged in May)

- 🔴 **`/compare/bloomerang-vs-donordock` JSON-LD trailing-comma parse failure** — entire schema block dropped by all crawlers. NEW regression. Standardize cluster on the clean `/compare/givebutter` template and validate all 9 compare pages in Rich Results Test.
- 🔴 **Article count dropped 449 → 351 (−22%)** — concentrated in `/articles/` (sitemap total grew). Could be a deliberate thin-content prune (quality-positive) or an accidental de-index. **#1 investigation item** before any other content work.
- 🔴 **Entity inconsistency got WORSE — now a 4-way split:** homepage/pricing "7,600+ users" (up from 7,200), `/about` "5,000+ leaders," `llms.txt` still "~1,300 nonprofits / 7,200+ users" (now stale on the user count too). Third consecutive month flagged; it degraded rather than reconciled.
- 🔴 **`/faq` now live with 80+ Q&A but ZERO FAQPage schema** — combined with `/pricing`'s 11 unmarked Q&A, ~91 question/answer pairs are invisible to answer engines. Highest-leverage unrealized AEO opportunity.
- 🔴 **`/contact` regressed to zero JSON-LD** — phone `(701) 490-8653` and `Mon–Fri 8–5 CST` visible HTML but unmarked; lost what little it had.
- 🔴 **`fetchpriority` regressed** — sub-pages now emit `fetchpriority="low"` on images with no `"high"` LCP hint outside the homepage. Worse signal than May's "missing."

### What regressed (vs May)

- 🔴 **Schema:** new Bloomerang-compare parse failure (above).
- 🔴 **Citability:** entity-count split widened from 3-way to 4-way.
- 🔴 **AEO:** `/contact` lost its JSON-LD.
- 🔴 **Performance:** `fetchpriority="low"` on sub-page images.

### What held steady (still outstanding from May)

- ⚠️ **JS-injected article FAQPage** — DISPUTED this month (schema auditor: still JS-injected; technical/AEO auditors: rendered in DOM). Treat as OPEN until verified. Still the #1 P0.
- ⚠️ **Duplicate G2 AggregateRating script** — every page still injects a second rating competing with static `4.8 / 200`.
- ⚠️ **1.39 MB hero GIF** + **duplicate jQuery (3.5.1 + 3.6.0)** — neither addressed.
- ⚠️ **Security headers** — CSP, Permissions-Policy, Referrer-Policy, X-Content-Type-Options, COOP all still missing; single Cloudflare Transform Rule not created.
- ⚠️ **Sitemap missing `<lastmod>`** — 3rd month running (URL count reported variably 622 / 977 / 1,071 by different auditors depending on sitemap sampled — reconcile).
- ⚠️ **`/llms-full.txt`** still 404. **HowTo schema** still absent. **Free-trial CTAs** non-functional. **G2/Capterra** still missing from `sameAs`.
- ⚠️ **`/compare/virtuous-vs-donordock`** and **`/compare/donordock-vs-keela`** still not built.

---

## 2. Competitor delta — June vs May

| Competitor | Material delta | Threat trend |
|---|---|---|
| **Givebutter** | **Wallet expanding into a full operating bank** (Spend Cards + Mobile Check Deposit "coming soon," "cash back" framing) + new Nonprofit Investing pillar. Fast Company Most Innovative 2026. G2 1,970 → **2,057 (+87)** — velocity collapsed from +470/mo. `/alternatives/donordock` STILL stale (Sept 2023). | 🔴 Escalating — banking moat widening; DD not countering |
| **DonorPerfect** | Now **owns Givecloud** (SofterWare Jan-2026 acquisition) surfacing in content. **NEW "$99/mo" pricing anchor** (was gated) narrows DD's transparency edge. Comparison footprint flat at 12; DonorDock still not targeted. | 🟡 Moderate / rising — conversion + online-giving posture emerging |
| **Neon One** | **Now NAMES DonorDock in 2 high-ranking listicles** (fair-to-favorable). Recurring Donor Report deepened into a full content franchise. G2 390 → 418 but rating slipped 4.3 → 4.2. Pricing stable. | 🟡 Steady + soft escalation — naming us in listicles |
| **Bloomerang** | Flagship FAQPage deepened **4 → 7 Q** (narrows DD's FAQ-schema arbitrage). Pricing flat but **bundle-locked** (Fundraising no longer true standalone $40) + upsell tiers. Sitemaps consolidated (counts no longer cleanly derivable, ~700+ posts). `/alternative/` hub contracted 17 → 15. Dataro AI partnership. | 🟡 Steady — no DD-specific escalation; comparison program slightly contracted |
| **Keela** | **Velora co-branding now live** — joinvelora.com/keela headlined "Keela is Velora CRM"; suite renames all three as Velora CRM/Fundraising/Fund Accounting. Confirms the "three products, not one platform" wedge in their own words. G2 88 → 79 (erosion). keela.co still resolves. Content flat (post-acquisition slowdown confirmed). | 🟡 Down as standalone — but DD-vs-Keela window closing as Velora consolidates |
| **Network for Good** | Rebrand to "Bonterra Guided Fundraising" now canonical on G2. E-E-A-T progress **stalled** (no new named-expert bylines) — window stays open. Sitemap re-fetched (~450–500 posts). Pricing still gated. | 🟡 Flat / holding — moat intact but not widening |
| **Little Green Light** | Page growth **stalled to +1%** (April→May +34% surge was a one-off, not a program). Still zero schema / AI-bot / comparison progress (3 months). Launched a user community (retention play). Capterra flat 316 / 4.7–4.8★. | 🟡 Flat-to-declining SEO momentum — coasting |
| **Virtuous** | **Post-launch lull** — ~zero June content after the April Benchmark blitz + May summit. Respond '26 ran May 27–29; no post-event recap/PR shipped yet (derivative cluster likely incoming — re-check early June). Reviews flat (Capterra 47 / 4.6). | 🟡 Holding / cooling — big escalation already landed Apr–May |

### New strategic threats (June surfaces)

1. **Givebutter's banking expansion** — Wallet → Spend Cards + Mobile Check Deposit + Nonprofit Investing pillar reframes the "free" argument into "free + your operating bank." **Action:** add a Wallet/banking-response section + stale-data callout to `/compare/givebutter-vs-donordock` (their `/alternatives/donordock` is still Sept-2023 stale — easy contrast to draw). Consider the "vendor float / nonprofit treasury risk" earned-media angle.
2. **Neon naming DonorDock in listicles** — soft escalation; more "DonorDock vs Neon" intent now resolves on Neon's domain. **Action:** ship/strengthen DD-owned "DonorDock vs Neon" content and claim the SERP while framing is favorable.
3. **DonorPerfect's Givecloud + "$99/mo" anchor** — a more conversion- and online-giving-focused posture, plus a low-price hook that will get quoted against DD. **Action:** prep a TCO rebuttal (flat-rate-at-scale vs $99 + modules).
4. **Velora consolidation continuing** — "Keela is Velora CRM" is now in their own marketing; the "three products stitched together" wedge is sharper than ever. **Action:** ship `/compare/donordock-vs-keela` with the Velora migration angle before the window closes.

### Comparison-page whitespace (uncontested by 7 of 8 competitors)

| Competitor | Has `/vs/donordock` page? | DonorDock has `/compare/<comp>-vs-donordock`? |
|---|---|---|
| Bloomerang | ❌ (lane open 2nd month) | ✅ (⚠️ JSON-LD parse error — fix this month) |
| DonorPerfect | ❌ | ✅ |
| Network for Good | ❌ | ✅ (stale pricing) |
| Givebutter | ✅ (stale Sept 2023) | ✅ (⚠️ doesn't address Wallet) |
| Neon One | ❌ (but now names DD in listicles) | ✅ |
| Little Green Light | ❌ | ✅ |
| **Virtuous** | ❌ | ❌ (still missing — open multiple months) |
| **Keela** | ❌ | ❌ (still missing — Velora makes this more urgent) |

DonorDock's comparison-page moat held this month. Two open builds: **Virtuous + Keela**. One existing page needs a fix (Bloomerang JSON-LD) and one needs a content update (Givebutter Wallet).

---

## 3. Top 10 actions ranked (P0 / P1 / P2)

### P0 — ship this week

| # | Action | Source audit | Why P0 |
|---|---|---|---|
| 1 | **Verify article FAQPage rendering (Rich Results Test + raw curl), then move to static HTML if confirmed JS-injected** | Schema (disputed by Technical/AEO) | The auditors disagree. If the schema specialist is right, 281+ articles ship FAQ markup invisible to every AI engine — still the highest-leverage fix. Resolve the disagreement first. |
| 2 | **Fix `/compare/bloomerang-vs-donordock` JSON-LD trailing comma** and validate all 9 compare pages | Schema + Vertical | NEW regression — entire schema block fails to parse, all structured data dropped. ~5-min fix; standardize cluster on `/compare/givebutter`. |
| 3 | **Investigate article count drop 449 → 351 (−22%)** — crawl-vs-sitemap diff to confirm prune vs accidental de-index | Content quality | Could be a quality-positive prune or a silent de-index of 98 URLs. Must know which before any other content work. |
| 4 | **301 `/blog` → `/articles` and `/demo` → `/donordock-demo`** | Technical SEO | Carryover. 10 minutes. Recovers external link equity to the two most-linked dead paths. |
| 5 | **Remove duplicate G2-injected AggregateRating script** | Schema | Carryover. Google may suppress both ratings; clean fix protects rich-result eligibility. |

### P1 — ship this month

| # | Action | Source audit | Why P1 |
|---|---|---|---|
| 6 | **Add FAQPage schema to `/faq` (80+ Q&A) and `/pricing` (11 Q&A)** | Citability + AEO | ~91 Q&A pairs currently invisible to answer engines; mechanical, not editorial. Projects citability 76 → ~83. |
| 7 | **Replace 1.39 MB hero GIF with MP4/WebM** + remove duplicate jQuery + fix `fetchpriority` regression | Performance | Hero GIF is the #1 LCP drag; homepage already uses `<video>` elsewhere (drop-in). ~1.1 MB savings. |
| 8 | **Reconcile entity counts** (homepage/pricing 7,600 / about 5,000+ / llms.txt stale 1,300 + 7,200) | Citability | Now a 4-way split, 3rd month, degrading. AI engines triangulate and penalize inconsistency. |
| 9 | **Add `<lastmod>` to all sitemap URLs** | Citability + Technical SEO | 3rd month open. Single Webflow config; sitewide freshness signal. |
| 10 | **Ship security headers via one Cloudflare Transform Rule** (CSP report-only, Referrer-Policy, Permissions-Policy, X-Content-Type-Options, COOP) | Security | Zero-risk, recovers GA4 referral attribution; the same one-rule fix recommended in May. |

### P2 — backlog (carry forward)

- **Update `/compare/givebutter-vs-donordock`** with a Wallet/banking-response section + stale-data callout (Givebutter escalating)
- **Ship `/compare/virtuous-vs-donordock`** (open multiple months)
- **Ship `/compare/donordock-vs-keela`** with the Velora "three products" migration angle (window closing)
- Strengthen DonorDock-owned "vs Neon" content (Neon now names DD in listicles)
- Prep a TCO rebuttal vs DonorPerfect's new "$99/mo" anchor
- Deepen the new article FAQPage blocks from 1 Q to 3–5 Q
- Add HowTo schema to step-based articles (template once, apply to many)
- Add G2 + Capterra to Organization `sameAs` (2-min, 2 months open)
- Restore static JSON-LD on `/contact` (LocalBusiness/ContactPage)
- Ship `/llms-full.txt` (still 404)
- Fix/relabel the non-functional free-trial CTA scaffolding (or strip the dead naming)
- Author bylines + named Person schema for Matt + Rob (also counters NFG + Bloomerang E-E-A-T)
- DonorDock 2026 Benchmark Report scoping (counter to Virtuous + Neon research franchises)
- Thin-content cleanup: `/team/*` (40) + `/tags/*` (62) pages

---

## 4. Failure / coverage notes

- ✅ All 9 site dimension audits completed cleanly.
- ✅ All 8 competitor audits completed cleanly.
- ⚠️ **Auditor disagreement on article FAQPage rendering** — the schema specialist traced it to a runtime IIFE (still JS-injected); the technical-SEO and AEO auditors observed it in the rendered DOM and marked it fixed. Reported conservatively as OPEN (P0 #1) pending a Rich Results Test / raw-curl check. The difference is static-HTML-source vs JS-injection, which only the schema auditor inspects directly.
- ⚠️ **Sitemap URL count reported variably** (622 / 977 / 1,071) across auditors depending on which sitemap was sampled — reconcile to a single source-of-truth count next cycle.
- ⚠️ **Security score bookkeeping** — May prose rendered "72" but the tracked baseline carried 67; June used 67 (posture is byte-for-byte identical, so the score doesn't move either way). Reconcile to one number going forward.
- ⚠️ **Competitor review counts partially approximated** — G2 direct-fetch 403'd for Network for Good (~398 retained), Virtuous (~71 from features page), and Neon One (Cloudflare 403, blocks direct inspection — our AI-crawlability advantage holds). Counts retained from prior baseline where blocked; flagged per file.
- ⚠️ **Givebutter `/alternatives/donordock`** now redirects to `/compare` on direct fetch, masking the body — staleness inferred from SERP title/cache (confirmed Sept-2023 data, June 1).
- ⚠️ Several competitor sitemaps consolidated (Bloomerang, DonorPerfect) making exact post counts non-comparable to prior months — flagged as measurement artifacts, not confirmed content purges.

---

**Locked at:** 2026-06-01 audit run.
**Prior baseline:** [`2026-05-baseline/executive-summary.md`](../2026-05-baseline/executive-summary.md).
**Next refresh:** Scheduled monthly via `monthly-audit-suite` task.
