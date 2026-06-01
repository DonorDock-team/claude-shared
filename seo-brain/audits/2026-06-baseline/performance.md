# DonorDock Performance & Core Web Vitals Audit — 2026-06 Baseline

**Audited:** 2026-06-01
**Site:** https://www.donordock.com
**Prior baseline:** [../2026-05-baseline/performance.md](../2026-05-baseline/performance.md)
**Pages sampled:** Homepage (/), /pricing, /features, /articles (blog index)
**Method:** Server-side HTML inspection (curl + parser), HEAD/GET timings + content-encoding probes, CDN header inspection. PageSpeed-grade lab metrics not available in this environment, so LCP/CLS/INP figures are *projected* from on-page signals (asset weight, render-blocking chain, script position, image dimensioning, third-party count). Treat as risk estimates, not measured CrUX values.

---

## Score: 71 / 100  ·  Trend: ▲ +9 vs May (was 62)

**Why it moved up.** Three structural wins landed since the May baseline:
1. **Render-blocking scripts dropped from 9-in-head to 2-in-head.** The heavy libraries (both jQueries, GSAP, RevenueHero, HubSpot form bridge, js-cookie) have moved from `<head>` to the bottom of `<body>`. They are still synchronous (no `defer`/`async`), but they no longer block first paint — this is the single biggest lab-metric improvement of the month.
2. **Brotli is now live on the Webflow shared CSS bundle.** May served gzip-only; June serves `content-encoding: br` (178 KB vs 190 KB gzip vs 1,218 KB raw). The ~11 KB/visit free win flagged in May P0-#4 is captured.
3. **Facebook Pixel is gone.** The 376 KB `fbevents.js` + 172 KB config that loaded on every page in May are no longer present — roughly 550 KB of decoded third-party JS removed sitewide.

**Why it isn't higher.** The two flagship May findings are unaddressed: the **1.39 MB hero GIF is still shipping** and the **duplicate jQuery (3.5.1 + 3.6.0) is still loaded**. Iframes still lack lazy-loading, no font preload exists, and the `fetchpriority` that appeared on sub-pages is set to `low` (deprioritizing), not the `high` LCP hint that was recommended.

---

## 1. Prior-Finding Re-Check (May → June)

| # | May finding | June status | Detail |
|---|---|---|---|
| 1 | 9 render-blocking head scripts | **PARTIAL FIX ▲** | Only **2 blocking scripts remain in `<head>`** (`webfont.js`, `use.typekit.net`). jQuery x2, GSAP, RevenueHero, HubSpot bridge, js-cookie all relocated to end of `<body>`. Still no `defer`/`async`, but out of the critical paint path. |
| 2 | Duplicate jQuery (3.5.1 + 3.6.0) | **NOT FIXED ✗** | Both still load on every page: `d3e54v103j8qbb.cloudfront.net/.../jquery-3.5.1.min.js` and `code.jquery.com/jquery-3.6.0.min.js`. ~89 KB pure waste persists. |
| 3 | ~1,185 KB Webflow CSS bundle, gzip-only | **IMPROVED ▲** | New hash `ddstaging.shared.cc789c21d.min.css`. Raw grew slightly to **1,218 KB**, but now served **brotli (178 KB wire)**. Net wire weight *down* vs May's 190 KB gzip. Still render-blocking `media="all"`; no critical-CSS inlining. |
| 4 | 1.39 MB hero GIF on homepage | **NOT FIXED ✗** | `...ImportOptions-optimised.gif` confirmed live at **1,394,047 bytes**. Identical file, identical size. Still the single largest non-JS asset on the site. |
| 5 | No `loading="lazy"` on Wistia/Embedly iframes | **NOT FIXED ✗** | Homepage Wistia/Embedly iframe: 0 lazy. /pricing: 3 iframes, 0 lazy. (Images did gain lazy-loading broadly — 75 lazy imgs on homepage — but the heavy iframes did not.) |
| 6 | No `fetchpriority="high"` on non-homepage LCP images | **NOT FIXED (regressed signal) ✗** | `fetchpriority` now *appears* on /pricing (5), /features (2), /articles (3) — but **every instance is `="low"`**, deprioritizing those images. No page outside the homepage has a `fetchpriority="high"` LCP hint. Homepage retains 2× `high` on its hero. |
| 7 | TTFB healthy 130–290 ms | **HOLDING ▲** | Homepage TTFB **131 ms**, /articles 135 ms, /features ~330 ms, /pricing ~350 ms. Cloudflare edge, HTTP/2, HSTS `max-age=31536000`, `surrogate-control: max-age=432000` all intact. Pricing/features TTFB a touch higher than May but well within healthy range. |

**Net:** 3 of 7 improved (scripts repositioned, brotli, Pixel removed), 1 bonus win (Pixel), 4 still open (GIF, dup jQuery, iframe lazy, LCP hint).

---

## 2. Core Web Vitals — Per Sample Page (Projected)

> Projected from payload, blocking-script position, third-party count, and image dimensioning. Mobile assumes 4G throttle / mid-tier device. All HTML is HTTP/2 from Cloudflare, `cf-cache-status: DYNAMIC`. Measured TTFB this run: 131–350 ms.

| Page | TTFB (measured) | LCP mobile (proj.) | LCP desktop (proj.) | CLS risk | INP risk | Notes vs May |
|---|---|---|---|---|---|---|
| **Homepage `/`** | 131 ms | 2.6–3.4 s | 1.5–2.1 s | Medium | Medium-High | ▲ ~0.6 s faster — scripts left head; Pixel gone. Still carries 1.39 MB GIF. |
| **/pricing** | 350 ms | 3.0–3.8 s | 1.7–2.4 s | Medium-High | High | ▲ scripts repositioned; ✗ 3 non-lazy Wistia iframes; `fetchpriority=low` hurts LCP image. |
| **/features** | 332 ms | 3.1–3.9 s | 1.8–2.5 s | Medium-High | High | ▲ second blocking CSS sheet no longer detected; 107 imgs, most still missing dims. |
| **/articles (index)** | 135 ms | 2.5–3.2 s | 1.4–2.0 s | Medium | Medium | ▲ broad lazy-loading on thumbs reduces network contention. |

**Mobile vs desktop differential:** narrowed to ~1.1–1.5 s (was 1.4–1.8 s). Driver is now body-positioned synchronous JS parse/exec rather than head-blocking. Removing the duplicate jQuery and deferring the body scripts would close most of the remaining gap.

---

## 3. Open Bottlenecks (Detail)

### 3.1 The 1.39 MB hero GIF — still the #1 fix
`cdn.prod.website-files.com/.../6768b992dc6bc1ff5507dd7d_..._ImportOptions-optimised.gif` = **1,394,047 bytes**, unchanged. GIFs don't brotli/gzip. Convert to `<video autoplay muted loop playsinline>` with MP4 (H.264) + WebM (VP9) sources → realistic 150–250 KB combined. **Saves ~1.1–1.2 MB on homepage.** The homepage already contains 2 `<video>` tags, so the pattern is in use elsewhere — this is a drop-in swap.

### 3.2 Duplicate jQuery — still loaded twice
`jquery-3.5.1` (Webflow bundled) + `jquery-3.6.0` (`code.jquery.com`) both present on all 4 pages. Remove the 3.6.0 copy from Site Custom Code. **Saves ~89 KB + a third-party DNS/TLS hop.**

### 3.3 Body scripts are repositioned but still synchronous
The relocation to `<body>` end is good, but jQuery 3.5.1, GSAP, RevenueHero, and the HubSpot form bridge still have no `defer`. They block `DOMContentLoaded` and add to TBT/INP. Adding `defer` (or removing where unused — RevenueHero only needs `/donordock-demo`) is the next-tier win.

### 3.4 Iframes still not lazy-loaded
Homepage Wistia/Embedly iframe + 3 on /pricing carry no `loading="lazy"`. Each Embedly→Wistia chain pulls ~200 KB JS + thumbnail + its own analytics. One-attribute fix per embed.

### 3.5 `fetchpriority="low"` on sub-page images — wrong direction
/pricing, /features, /articles now emit `fetchpriority="low"` on multiple images and **zero `="high"`**. The LCP candidate on each of those pages should get `fetchpriority="high"` + `loading="eager"`. Today the browser must guess, and some near-fold images are actively deprioritized.

### 3.6 Font loading — no preload, head-blocking loader scripts
`webfont.js` (ajax.googleapis.com) + `use.typekit.net/cwa7yxm.js` are the only 2 remaining `<head>` blockers. No `<link rel="preload" as="font" crossorigin>` on any page → FOIT risk on slow networks. Preload the primary hero font weight and `defer` the WebFont loader.

### 3.7 Third-party origins still missing preconnect
Preconnect present for: website-files, fonts.googleapis, fonts.gstatic, 3× intellimize, jsdelivr. **Still missing:** `code.jquery.com`, `ajax.googleapis.com`, `use.typekit.net`, `assets.revenuehero.io`, `hubspotonwebflow.com`, `js.hs-scripts.com`. (Facebook origins no longer needed — Pixel removed.)

---

## 4. Ranked Fix List

### P0 — biggest remaining wins
1. **Replace the 1.39 MB hero GIF with `<video>` (MP4 + WebM).** Saves ~1.1–1.2 MB on homepage. Highest single-asset impact on the site.
2. **Remove the duplicate jQuery 3.6.0.** Saves ~89 KB + a TLS hop on every page.
3. **Add `defer` to the body-positioned scripts** (jQuery 3.5.1, GSAP, RevenueHero, HubSpot bridge) and scope RevenueHero to `/donordock-demo` only. Projected mobile LCP/TBT gain: 200–500 ms.

### P1 — CLS / LCP polish
4. **Flip sub-page LCP images from `fetchpriority="low"` to `"high"`** (+ `loading="eager"`) on /pricing, /features, /articles. Today they're deprioritized.
5. **Add `loading="lazy"` to the Wistia/Embedly iframes** (homepage + 3 on /pricing). 150–300 ms TBT/INP each.
6. **Add width/height to remaining undimensioned images** on /pricing (97), /features (107), /articles (48). Free CLS insurance.
7. **Add preconnect** for `code.jquery.com`, `ajax.googleapis.com`, `use.typekit.net`, `assets.revenuehero.io`, `hubspotonwebflow.com`, `js.hs-scripts.com`.
8. **Preload the primary hero font** (`<link rel="preload" as="font" type="font/woff2" crossorigin>`) and `defer` `webfont.js` + Typekit loader out of the head.

### P2 — longer-term
9. **Critical-CSS inlining** for the 1,218 KB shared bundle (still render-blocking; brotli helps the wire but not the parse/block). Inline ~10–15 KB above-fold, async-load the rest.
10. **Audit GSAP global load** — lazy-load via dynamic `import()` if only used on a few components.
11. **Run a real Lighthouse/CrUX pass** to replace projected CWV with measured values; set Webflow budget alarms (LCP > 2.5 s, CLS > 0.1, TBT > 200 ms).

---

## Appendix — Headers & Caching (June)
- HTTP/2 confirmed; Cloudflare CDN; `cf-cache-status: DYNAMIC` on HTML.
- `strict-transport-security: max-age=31536000` ✓
- `surrogate-control: max-age=432000` (5 days) ✓
- **CSS bundle now negotiates brotli** (`content-encoding: br`, 178 KB wire) — new this month.
- Shared CSS raw size grew 1,185 KB → 1,218 KB (more components shipped); offset by brotli.

## Appendix — Method & Caveats
- No CrUX/Lighthouse field or lab data in this environment; §2 values are projected ranges from on-page signals, not measured.
- Sizes verified via `content-length` and `Accept-Encoding` probes (identity/gzip/br).
- /features returns 301 → final 200 (canonical redirect); both audited.
