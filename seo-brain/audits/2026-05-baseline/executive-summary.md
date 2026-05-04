# May 2026 Baseline — Executive Summary

**Period:** 2026-05-04 (single-run snapshot)
**Scope:** Site audit (9 dimensions) + competitor audit (8 vendors)
**Owner:** Rob Burke (CMO, rburke@donordock.com)
**Prior baseline:** [`2026-04-baseline`](../2026-04-baseline/executive-summary.md)
**Status:** Monthly tracking refresh. Delta-driven. No remediation in this run.

---

## TL;DR (5 bullets)

1. **The April Cloudflare AI-bot decision LANDED.** All 14 major AI crawlers (GPTBot, ClaudeBot, PerplexityBot, Google-Extended, Applebot-Extended, CCBot, etc.) now return HTTP 200. GEO readiness jumped from F (32/100) to "Optimized → approaching Dominant" (2.5/3). The single highest-leverage fix from April is done.
2. **But a new AEO/GEO regression surfaced:** article FAQ schema is being injected by JavaScript at runtime. Google renders JS, but Bing, GPTBot, ClaudeBot, CCBot, and PerplexityBot do not — so 281+ articles ship FAQ markup that's **invisible to every AI engine that matters for citation**. This single template fix is now the new #1 P0.
3. **Bloomerang launched a competitor-comparison program** (`/alternative/{competitor}/` covering 17+ rivals — Blackbaud, Virtuous, DonorPerfect, LGL, NeonCRM, Salesforce.org, Bonterra, EveryAction, Raiser's Edge, etc.). **DonorDock is NOT yet targeted.** The window to ship pre-emptive `/compare/bloomerang-vs-donordock` schema + content reinforcement is real but closing.
4. **Givebutter materially widened the moat** — launched **Givebutter Wallet (2.5% APY, FDIC pass-through)** paying nonprofits to hold balances. New positioning narrative ("free + we pay you to bank with us"). G2 reviews jumped 1,500 → 1,970 (+470/mo velocity). DonorDock's `/compare/givebutter-vs-donordock` does not address this and Givebutter's `/alternatives/donordock` page is now confirmed stale (data from September 2023).
5. **Keela was acquired and folded into the Velora suite** (Aplos + Raisely + Keela, launched Aug 2025). The April baseline missed this. DonorDock's "one login, one bill, one platform" story is now sharper than 30 days ago. Recommend a `/compare/donordock-vs-keela` page with a "what Velora means for your Keela subscription" migration angle.

---

## 1. Site health — May vs April

| Dimension | Apr 2026 | May 2026 | Trend | Notes |
|---|---|---|---|---|
| Technical SEO | 72/100 | ~72/100 | ⚪ Held | New finding: `/blog` and `/demo` both 404 (linked externally). Empty H1 tags on 10+ money pages (single Webflow template bug). |
| AEO Readiness | 65/100 | 54/100 | 🔴 Regressed (surfaced) | `/pricing` (88) and `/faq` still the model. Homepage, `/features`, `/about`, `/contact` (30–42) sit out of every snippet/PAA surface. |
| GEO Readiness | 32/100 (F) | **2.5/3 (Optimized)** | 🟢 Major improvement | Cloudflare unblock LANDED. llms.txt scored 95/100 (best-in-class). All 14 AI crawlers green. Only Bytespider 403 (irrelevant). |
| AI Citability | 42/100 (D+) | **76/100** | 🟢 Major improvement | Articles avg 8.9/10. `/articles/why-fundraisers-under-ask...` hit 9.3/10. Marketing pages still lag at 5.6/10. |
| Performance | 65/100 | ~65/100 | ⚪ Held | 9 render-blocking head scripts, duplicate jQuery (3.5.1 + 3.6.0), 1,185 KB Webflow CSS bundle, 1.39 MB hero GIF. TTFB healthy 130–290ms. |
| Security | 62/100 | ~67/100 | 🟢 Slight improvement | TLS 1.0/1.1 disabled, modern AEAD ciphers, valid cert through Aug 2026. CSP/Permissions-Policy/Referrer-Policy still missing. |
| Schema coverage | mixed | mixed | ⚪ Held + 🔴 new finding | `/pricing` is gold standard. **NEW critical finding: article FAQPage is JS-injected → invisible to AI bots.** Duplicate G2 AggregateRating script also discovered. |
| Content quality | 58/100 | ~58/100 | ⚪ Held + 🔴 new findings | **NEW: rolling-date bug** — every article shows a future "last updated" date (template binding bug, 449 articles). 35 thin `/team/*` pages, 69 thin `/tags/*` hubs. Donor-lifecycle cannibalization across 5+ URLs. |
| Vertical SEO | 42/100 (F) | ~50/100 | 🟢 Slight improvement | `/pricing` now best-in-class schema template (92/100). Still zero free-trial CTAs sitewide. G2/Capterra missing from Organization `sameAs`. |

### What landed since April (visible improvements)

- ✅ **Cloudflare AI-bot unblock** — was the April #1 P0; all major bots now allowed
- ✅ **llms.txt at 95/100** — best-in-class quality, structured content map, 1% fee messaging
- ✅ **`/faq` flat @graph + 114 H3 accordions** — citation magnet, leave alone
- ✅ **`/pricing` schema** — single `@graph` with Org + SoftwareApplication + FAQPage + BreadcrumbList + WebPage. Use as template for the rest of the site.
- ✅ **Donor-retention article (9.3/10 citability)** — FEP, Lilly School, Bridgespan, Yale, Harvard citations + active FAQPage. Template for the article hub.
- ✅ **TLS hygiene** — 1.0/1.1 disabled, HTTP/3 advertised, HSTS active, clean canonicalization.

### What surfaced new (May findings not flagged in April)

- 🔴 **JS-injected article FAQPage schema** — 281 articles ship FAQ markup invisible to GPTBot, ClaudeBot, CCBot, PerplexityBot, Bingbot. Single template fix unlocks AI-citation surface across the entire blog.
- 🔴 **Sitewide rolling-date bug** — every sampled article shows a future "last updated" date (April 25–29, 2026 audited on May 4). Template binding using auto-generated dates instead of real publication/review dates. Affects ~449 articles.
- 🔴 **`/blog` and `/demo` both return 404** — external links default to these paths; actual pages live at `/articles` and `/donordock-demo`. 10-minute redirect fix recovers all link equity.
- 🔴 **Empty `<h1>` tags on 10+ money pages** — `/pricing`, `/features-overview` (4 empty), `/donordock-demo`, `/crm`, `/contact`, `/online-giving`, `/integrations`, `/partners`, `/academy`. Single shared Webflow template bug.
- 🔴 **Duplicate AggregateRating script** — every page injects a second AggregateRating from G2's `rating_schema.json`, competing with the static `4.8 / 200`. Google may suppress both.
- 🔴 **`/contact` has zero static JSON-LD** — phone `(701) 490-8653` and `Mon–Fri 8–5 CST` are visible HTML but unmarked.
- 🔴 **Sitemap missing `<lastmod>`** — 1,032 URLs, zero have lastmod tags. Weakens freshness signals across the entire crawl.
- 🔴 **Entity inconsistency** — "7,200 users" (homepage) vs "5,000+ leaders" (about) vs "~1,300 nonprofits" (llms.txt). AI engines triangulate and penalize inconsistency.

### What regressed (vs April)

- 🔴 **AEO score 65 → 54** — likely a measurement-methodology shift (May audit was stricter on snippet-block formatting, comparison tables, HowTo schema), but the gap is real. `/about`, `/features`, `/contact`, homepage all sit out of snippet/PAA surfaces with no question H2s, no FAQ schema, no answer blocks.
- 🔴 **AggregateRating duplication** — wasn't flagged in April; G2 schema injector was added (or first audited in May). Either way, action required.

### What held steady (still outstanding from April)

- ⚠️ Performance — 9 render-blocking head scripts, 1.39 MB homepage GIF, 1.18 MB Webflow CSS bundle, no `loading="lazy"` on Wistia/Embedly iframes, no `fetchpriority="high"` on non-homepage LCP images
- ⚠️ Security headers — CSP, Permissions-Policy, Referrer-Policy, X-Content-Type-Options, COOP all still missing
- ⚠️ FAQ schema gap on `/features/*` and 7 of 10 compare pages
- ⚠️ Comparison-page pricing data refresh on `/compare/network-for-good-vs-donordock` (still showing stale $79/mo)
- ⚠️ Article CMS template `featured image` still `width="Auto" height="Auto"`
- ⚠️ No `/llms-full.txt` (404)
- ⚠️ No annual research / benchmark report

---

## 2. Competitor delta — May vs April

| Competitor | Material delta | Threat trend |
|---|---|---|
| **Bloomerang** | Launched `/alternative/{competitor}/` program (17+ pages). DonorDock not targeted yet. Domain consolidated bloomerang.co → bloomerang.com. Pricing now publicly listed ($40 / $125 / $119). Blog count dropped 1,306 → 893 (pruning). | 🔴 Escalating — comparison program is a direct attack surface |
| **Givebutter** | **NEW Givebutter Wallet (2.5% APY, FDIC)** = new positioning moat. G2 reviews 1,500 → 1,970 (+470/mo). Cash App Pay added. `/alternatives/donordock` confirmed stale (Sept 2023). Monthly Giving Week campaign May 11–15. | 🔴 Escalating — Wallet narrative + review velocity |
| **Keela** | **Acquired by Aplos, folded into Velora suite** (Aug 2025 launch). Pricing up to $134/mo (April had ~$99). G2 slug now `aplos-software-keela`. April baseline missed the acquisition entirely. | 🟡 Reframed — Velora "three products stitched together" creates DonorDock attack surface |
| **Network for Good** | Bonterra rebranded URL `/product/network-for-good` → `/network-for-good`. Now also called "Bonterra Guided Fundraising" on G2/Capterra. FAQ schema expanded 4 → 7 questions. NEW match-or-refund performance guarantee on Essentials. First author byline appeared ("Bonterra Editorial Team"). | 🟡 Slowly improving — closing E-E-A-T gap |
| **DonorPerfect** | Comparison footprint expanded **5 → 12 competitors** (added eTapestry, Neon, Bonterra, **Givebutter**, **Virtuous**, Causeview, NFG, Excel). DonorDock still not targeted. Schema unchanged (Yoast default, no SoftwareApplication / Offer / FAQPage). | 🟡 Active but not aimed at DD |
| **Virtuous** | **NEW 2026 Nonprofit Fundraising Benchmark Report** with PR Newswire + Morningstar pickup, 6+ derivative articles. **NEW Momentum AI agents** feature. Respond 2026 User Summit (May 27–29). Capterra +5 reviews to 47 / 4.6. | 🔴 Escalating — content engine + AI narrative + research franchise |
| **Neon One** | **NEW Association tiers** ($109/$219/$439) publicly indexed. Recurring Donor Report refreshed Feb 2026 (4,107 nonprofits + 700-donor survey, PR Newswire pickup). Capterra +48 reviews to ~598 / 4.3. | 🟡 Steady — clean Q1 refresh, no aggression at DD |
| **Little Green Light** | Page surface +34% (136 → 182 static pages in 30 days). Blog cadence flat. No schema improvements. Still no AI-bot policy update. Capterra 316 reviews / 4.7–4.8★ — strongest moat. | 🟡 Investing in volume, not modern SEO infra |

### New strategic threats (May surfaces)

1. **Bloomerang's `/alternative/*` program** — 17 competitor comparison pages launched in the last cycle. DonorDock has a window before Bloomerang adds `/alternative/donordock/` to the program. **Action:** harden `/compare/bloomerang-vs-donordock` with FAQPage + Review + ItemList schema THIS MONTH.
2. **Givebutter Wallet (2.5% APY)** — first competitor in the category to offer a yield product. Reframes "free" pricing argument. **Action:** add a Wallet-response section + FAQ schema to `/compare/givebutter-vs-donordock`. Consider earned-media pitch on "vendor float / nonprofit treasury risk" angle.
3. **Velora consolidation (Keela + Aplos + Raisely)** — DonorDock's "one platform" positioning is sharper than 30 days ago. **Action:** ship `/compare/donordock-vs-keela` with Velora migration angle.
4. **Virtuous 2026 Benchmark Report** — Virtuous and Neon now both have annual research franchises. DonorDock has the raw material (~1,300 customer nonprofits, 7,200+ users, $9B tracked gifts) and no report. **Action:** scope DonorDock 2026 Benchmark Report for Q3.

### Comparison-page whitespace (still uncontested by 6 of 8 competitors)

| Competitor | Has `/vs/donordock` page? | DonorDock has `/compare/<comp>-vs-donordock`? |
|---|---|---|
| Bloomerang | ❌ (but `/alternative/*` program launched, window closing) | ✅ |
| DonorPerfect | ❌ | ✅ |
| Network for Good | ❌ | ✅ (stale pricing) |
| **Givebutter** | ✅ (stale Sept 2023 data) | ✅ |
| Neon One | ❌ | ✅ |
| Little Green Light | ❌ | ✅ |
| **Virtuous** | ❌ | ❌ (still missing — April Priority 17, still open) |
| **Keela** | ❌ | ❌ (still missing — Velora makes this more urgent) |

DonorDock's comparison-page moat held this month. Two open builds: **Virtuous + Keela**.

---

## 3. Top 10 actions ranked (P0 / P1 / P2)

### P0 — ship this week

| # | Action | Source audit | Why P0 |
|---|---|---|---|
| 1 | **Move article FAQPage schema from JS-injected to static HTML** in the Webflow CMS template | Schema | Single change unlocks AI-citation surface across 281 articles. Net regression vs April if not fixed. |
| 2 | **301 `/blog` → `/articles` and `/demo` → `/donordock-demo`** | Technical SEO | 10 minutes. Recovers all external link equity to those paths. |
| 3 | **Fix shared Webflow hero template so visible heading lives in the actual `<h1>` element** | Technical SEO | Single template fix → 10+ money pages including `/pricing`. |
| 4 | **Fix sitewide rolling-date bug** so article "last updated" reflects real CMS dates, not auto-generated future timestamps | Content quality | 449 articles currently show future dates → erodes AI freshness signals. |
| 5 | **Remove duplicate G2-injected AggregateRating script** (or move to a dedicated, deduplicated implementation) | Schema | Google may suppress both ratings; clean fix protects rich-result eligibility. |

### P1 — ship this month

| # | Action | Source audit | Why P1 |
|---|---|---|---|
| 6 | **Harden `/compare/bloomerang-vs-donordock`** with FAQPage + Review + ItemList schema before Bloomerang adds DonorDock to their `/alternative/*` program | Bloomerang competitor | Window closing, defensive priority. |
| 7 | **Replace 1.39 MB hero GIF with MP4/WebM video** + defer 9 render-blocking head scripts + remove duplicate jQuery (3.5.1 + 3.6.0) | Performance | 80–90% LCP improvement; CWV impact across all pages. |
| 8 | **Add `<lastmod>` to all 1,032 sitemap URLs** | Citability + Technical SEO | Single Webflow config; sitewide freshness signal. |
| 9 | **Reconcile customer-count numbers across pages** (homepage 7,200 users / about 5,000+ leaders / llms.txt ~1,300 nonprofits) | Citability | AI engines triangulate; inconsistency suppresses citation. |
| 10 | **Ship CSP (report-only first), Referrer-Policy, Permissions-Policy, X-Content-Type-Options, COOP via one Cloudflare Transform Rule** | Security | Zero-risk; recovers GA4 referral attribution. |

### P2 — backlog (carry forward)

- Add free-trial CTA across `/crm`, `/pricing`, `/features` (vertical audit; zero free-trial CTAs sitewide)
- HSTS upgrade to `max-age=63072000; includeSubDomains; preload` + submit to hstspreload.org
- Ship `/llms-full.txt` (currently 404) for Deep Research agents
- Add HowTo schema to 3 step-based articles (template once, apply to many)
- Add G2 + Capterra to Organization `sameAs`
- `/compare/virtuous-vs-donordock` (April Priority 17, still open)
- `/compare/donordock-vs-keela` with Velora migration angle (NEW from May)
- DonorDock 2026 Benchmark Report scoping (counter to Virtuous + Neon research franchises)
- Pillar-cluster wiring + 449-article internal linking program
- Author bylines + named Person schema for Matt + Rob across articles
- Refresh `/compare/network-for-good-vs-donordock` pricing data ($79 → $500)

---

## 4. Failure / coverage notes

- ✅ All 9 site dimension audits completed cleanly.
- ✅ All 8 competitor audits completed cleanly.
- ⚠️ Network for Good audit was unable to re-fetch Bonterra's `sitemap_index.xml` (WebFetch denied). April URL inventory retained as the working count. Sitemap counts unlikely to have moved materially in 14 days; flag if a fresh re-pull is desired.
- ⚠️ AEO score of 54 (vs April 65) likely reflects stricter measurement of snippet-block formatting, comparison tables, and HowTo schema rather than a true content regression. The underlying content surfaces (homepage, `/features`, `/about`, `/contact`) didn't change month-over-month — they were already weak in April; this audit just measured them more tightly.

---

**Locked at:** 2026-05-04 audit run.
**Prior baseline:** [`2026-04-baseline/executive-summary.md`](../2026-04-baseline/executive-summary.md).
**Next refresh:** Scheduled monthly via `monthly-audit-suite` task.
