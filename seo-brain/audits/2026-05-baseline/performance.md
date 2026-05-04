# DonorDock Performance & Core Web Vitals Audit — 2026-05 Baseline

**Audited:** 2026-05-04
**Site:** https://www.donordock.com
**Pages sampled:** Homepage (/), /pricing, /features, /articles (blog index), 2 articles
**Method:** Server-side HTML inspection (curl + parser), HEAD/GET timings, CDN header inspection. PageSpeed-grade lab metrics not available in this environment, so LCP/CLS/INP figures below are *projected* from on-page signals (asset weight, render-blocking chain, image dimensioning, third-party script count). Treat them as risk estimates, not measured CrUX values.

---

## 1. Executive Summary

- **Render-blocking JavaScript is the #1 problem.** Every sample page loads **9 render-blocking external scripts** in the `<head>` — jQuery (twice, two different versions), GSAP, Webflow runtime, Adobe Typekit + WebFont loader, RevenueHero, HubSpot-on-Webflow form, JS-Cookie. None use `defer` or `async`. This single fix is worth several hundred milliseconds of LCP and TBT improvement on every page.
- **CSS bloat is the silent killer.** The Webflow shared stylesheet `ddstaging.shared.3f6f2fc22.min.css` is **1,185 KB raw / 174 KB brotli / 185 KB gzip** and is `media="all"` render-blocking on every page. Webflow currently serves it as **gzip only (no brotli)** — losing roughly 11 KB of free wire savings per visit. There is no critical-CSS inlining.
- **One 1.39 MB animated GIF** (`ImportOptions-optimised.gif`) is currently being shipped on the homepage. That single file dwarfs all other image weight combined and is the largest non-JS asset on any sampled page. Convert to MP4/WebM `<video>` for an ~80–90% size reduction. Also, **no `<img>` tags carry width/height attributes outside the LCP hero** — every page has 40–105 images that can introduce CLS as they load.

---

## 2. Core Web Vitals — Per Sample Page (Projected)

> Projected ranges based on payload, render-blocking depth, and third-party impact. Mobile assumes 4G throttle / mid-tier device. Desktop assumes broadband. All HTML responses are HTTP/2 (h3 advertised) from Cloudflare with `cf-cache-status: DYNAMIC` and `o2o-cache-status: HIT`. TTFB measured client-side from this audit averages 130–290 ms.

| Page | TTFB (measured) | LCP mobile (projected) | LCP desktop (projected) | CLS risk | INP risk | Total page weight (decoded) |
|---|---|---|---|---|---|---|
| **Homepage `/`** | 129 ms | 3.2–4.0 s | 1.8–2.4 s | Medium-High | High | ~938 KB observed in browser cache run; ~2.1 MB cold (CSS + JS + 1.39 MB GIF) |
| **/pricing** | 137 ms | 3.4–4.2 s | 1.9–2.6 s | High | High | ~2.0 MB cold (no LCP `fetchpriority`, 3 Wistia iframes, 97 imgs missing dims) |
| **/features** | 287 ms | 3.6–4.5 s | 2.1–2.8 s | High | High | ~2.0 MB cold (2 blocking CSS files; 105/106 imgs missing dims; no LCP `fetchpriority`) |
| **/articles (index)** | 125 ms | 2.8–3.5 s | 1.6–2.2 s | Medium | High | ~1.7 MB cold (48 imgs, all hero thumbs missing dims) |
| **Article: grassroots** | 134 ms | 2.6–3.3 s | 1.5–2.1 s | Medium | High | ~1.7 MB cold (no LCP `fetchpriority` on article hero) |
| **Article: nonprofit-tech** | 144 ms | 2.6–3.3 s | 1.5–2.1 s | Medium | High | ~1.7 MB cold |

**Mobile vs desktop differential:** ~1.4–1.8 s LCP gap. Driver is JS parse/exec on a slower CPU + 9 render-blocking scripts deserialized before first paint. Pricing/Features show the worst mobile gap because they have the heaviest HTML (229 KB / 202 KB) plus zero LCP image hint.

**TTFB note:** TTFB itself is healthy (Cloudflare edge HIT). The gap is entirely in front-end critical path, not server speed.

---

## 3. Top Performance Bottlenecks Identified

### 3.1 Render-blocking JS — 9 scripts in `<head>` on every page
Identical chain on Homepage / Pricing / Features / Articles index / both articles:

| # | Script | Raw size | Defer/Async? | Comment |
|---|---|---|---|---|
| 1 | `ajax.googleapis.com/.../webfont.js` | 5.4 KB | NO | Loads typekit asynchronously anyway — can be deferred |
| 2 | `use.typekit.net/cwa7yxm.js` | 6.6 KB | NO | Adobe Typekit kit — should preconnect + defer; FOUT/FOIT risk |
| 3 | `d3e54v103j8qbb.cloudfront.net/.../jquery-3.5.1.min.js?site=...` | **89.5 KB** | NO | Webflow's bundled jQuery |
| 4 | `cdn.prod.website-files.com/.../ddstaging.{hash}.js` | 5.4 KB | NO | Webflow site JS |
| 5 | `cdn.prod.website-files.com/gsap/3.15.0/gsap.min.js` | **72.9 KB** | NO | Animation lib — needed only if above-fold animation is present |
| 6 | `assets.revenuehero.io/scheduler.min.js` | ~25 KB | NO | Demo scheduler — used only on Demo page; remove from other pages |
| 7 | `code.jquery.com/jquery-3.6.0.min.js` | **~88 KB** | NO | **Second copy of jQuery** loaded after Webflow's. Pure waste. |
| 8 | `cdn.jsdelivr.net/npm/js-cookie@2/.../js.cookie.min.js` | 3.5 KB | NO | Tiny but adds a third-party DNS hop |
| 9 | `hubspotonwebflow.com/assets/js/form-124.js` | 10.5 KB | NO | HubSpot form bridge — only needed where forms exist |

**Estimated cumulative wire weight of blocking JS (raw, brotli est.):** ~95 KB compressed across all 9. Dominated by the two jQueries (~50 KB compressed combined) and GSAP (~30 KB compressed).

### 3.2 Render-blocking CSS — one giant Webflow bundle

- **`cdn.prod.website-files.com/.../ddstaging.shared.3f6f2fc22.min.css`**
  - Raw: **1,185 KB** (1,213,528 bytes)
  - Gzip: 185 KB (server returns gzip)
  - Brotli: 174 KB (Webflow CDN supports brotli when requested but delivers gzip to most clients — ~11 KB free win available)
  - `media="all"`, no async pattern, blocks first paint on every page.
  - Features page additionally loads `cdn.jsdelivr.net/gh/sygnaltech/webflow-util@4.1/dist/css/webflow-html.css` (1.4 KB) — second blocking sheet.

### 3.3 Image weight — one massive GIF + missing dimensions

- **`6768b992dc6bc1ff5507dd7d_3abb3d0e11770b2d505d75ce6451945d_ImportOptions-optimised.gif`** = **1,394,047 bytes (1.39 MB)** on homepage. Animated GIFs cannot be brotli/gzip compressed and have no efficient alpha. Convert to `<video autoplay muted loop playsinline>` with MP4 + WebM sources — 80–90% size reduction realistic.
- LCP image on homepage **is correctly tagged**: `width="1508" height="2436"`, `loading="eager"`, `fetchpriority="high"`, full responsive `srcset` 500w → 3016w. Default `src` fetches the 3016w (216 KB) — fine for desktop, but the 1080w variant (66 KB) is what mobile actually downloads via srcset.
- **Pricing, Features, Articles index, both articles → no `fetchpriority="high"` on any image.** Browser must guess the LCP. Add `fetchpriority="high"` + `loading="eager"` to the first hero/banner image on each of these page types.
- **Width/height attributes are missing on virtually every image except the homepage hero.**
  - Homepage: 70 of 71 images missing width/height
  - Pricing: 97 of 97 missing
  - Features: 105 of 106 missing
  - Articles index: 48 of 48 missing
  - Articles: 41 of 42 missing

  These don't all cause CLS (many are in fixed CSS containers with `aspect-ratio` set), but any image without intrinsic dimensions whose container resizes between fetch start and paint will shift. Adding the attributes is free and removes the risk.

### 3.4 Third-party script load — 15–17 third-party origins per page

Every sample page connects to roughly the same set:

`cdn.prod.website-files.com`, `d3e54v103j8qbb.cloudfront.net`, `code.jquery.com`, `ajax.googleapis.com`, `use.typekit.net`, `cdn.jsdelivr.net`, `hubspotonwebflow.com`, `assets.revenuehero.io`, `cdn.intellimize.co`, `api.intellimize.co`, `log.intellimize.co`, `117780823.intellimizeio.com`, `js.hs-scripts.com`, `connect.facebook.net`, `static.elfsight.com` (homepage), `cdn.embedly.com` (homepage/pricing), `fonts.googleapis.com`, `fonts.gstatic.com`.

Heaviest by *decoded* (per the live homepage performance entries earlier in this audit):

| Script | Decoded size | Notes |
|---|---|---|
| `connect.facebook.net/en_US/fbevents.js` | **376 KB** | Facebook Pixel — currently loaded on every page |
| `connect.facebook.net/signals/config/645945310660656` | 172 KB | Facebook Pixel config |
| `cdn.intellimize.co/snippet/117780823.js` | **370 KB raw / 87 KB gzip** | A/B testing — runs synchronously to avoid flicker |
| `js.hs-banner.com/v2/7182124/banner.js` | 67 KB | HubSpot cookie banner |
| `fonts.gstatic.com/.../montserrat-*.woff2` | 37 KB ea. | Multiple Montserrat weights |

Preconnect coverage is good for the optimizer/Webflow CDN/fonts but **missing for facebook.net, code.jquery.com, ajax.googleapis.com, hubspotonwebflow.com, assets.revenuehero.io, js.hs-scripts.com**. Each is a separate TLS handshake on cold load.

### 3.5 Iframes — Wistia/Embedly without lazy-loading

- Homepage: 1 iframe (Wistia via Embedly), no `loading="lazy"`.
- Pricing: 3 iframes (3 Wistia videos via Embedly), none lazy-loaded.
- These embeds each pull ~200 KB of JS + an image thumbnail and run their own analytics. Adding `loading="lazy"` on every iframe below the fold is a one-attribute fix worth meaningful TBT/INP improvements.

### 3.6 Font loading

- No `<link rel="preload" as="font" type="font/woff2" crossorigin>` on any sample page. Adobe Typekit fonts are fetched after JS executes.
- No inline `@font-face` declarations on the served HTML, so we can't see `font-display: swap`. Webflow's bundled stylesheet contains them, but they're inside the 1.18 MB shared CSS — by the time they're parsed, fonts begin downloading. Result: high risk of FOIT on slow networks.
- Multiple Google Fonts Montserrat weights (300/400/500/600/700) loading as separate woff2 requests (~37 KB each) when they could be a single variable font (1 file, ~50 KB).

### 3.7 Mobile vs Desktop differential

- **HTML payload mobile-vs-desktop is identical** (no AMP, no separate mobile bundle). Good.
- Differential is driven by:
  1. JS parse/compile cost on mobile CPUs (~3–4× slower vs desktop). With 9 blocking scripts + ~250 KB of JS in head, this is the dominant factor.
  2. Network: gzip-only CSS bundle costs an extra ~11 KB on the wire vs. brotli — bigger relative impact on mobile data plans.
  3. No mobile-specific srcset breakpoint below 500 w on most non-LCP images — mobile fetches the same WebPs desktop does.

---

## 4. Specific Files / Scripts / Images Flagged

### Render-blocking JS (every page)
- `https://ajax.googleapis.com/ajax/libs/webfont/1.6.26/webfont.js`
- `https://use.typekit.net/cwa7yxm.js`
- `https://d3e54v103j8qbb.cloudfront.net/js/jquery-3.5.1.min.dc5e7f18c8.js?site=63ce9d04b1ff6e36cf514274`
- `https://cdn.prod.website-files.com/63ce9d04b1ff6e36cf514274/js/ddstaging.{37eee9f8|d5e2868b|ef3326fd}.{hash}.js`
- `https://cdn.prod.website-files.com/gsap/3.15.0/gsap.min.js` (72.9 KB)
- `https://assets.revenuehero.io/scheduler.min.js`
- `https://code.jquery.com/jquery-3.6.0.min.js` (89 KB — duplicate jQuery)
- `https://cdn.jsdelivr.net/npm/js-cookie@2/src/js.cookie.min.js`
- `https://hubspotonwebflow.com/assets/js/form-124.js`

### Render-blocking CSS
- `https://cdn.prod.website-files.com/63ce9d04b1ff6e36cf514274/css/ddstaging.shared.3f6f2fc22.min.css` — **1,185 KB raw / 185 KB gzip / 174 KB brotli**, every page
- `https://cdn.jsdelivr.net/gh/sygnaltech/webflow-util@4.1/dist/css/webflow-html.css` — 1.4 KB, Features page only

### Heavy/problematic images
- `https://cdn.prod.website-files.com/63ce9d04b1ff6e36cf514274/6768b992dc6bc1ff5507dd7d_3abb3d0e11770b2d505d75ce6451945d_ImportOptions-optimised.gif` — **1,394 KB animated GIF, homepage**
- `https://cdn.prod.website-files.com/63ce9d04b1ff6e36cf514274/68f27118b0c5daa3f90e4eda_..._Contact%20Details%20%20DonorDock-10-17-2025.webp` — 216 KB at 3016w, served as LCP default-src; OK because srcset routes mobile to 1080w/66 KB

### Heavy third-party scripts
- `connect.facebook.net/en_US/fbevents.js` (376 KB decoded)
- `connect.facebook.net/signals/config/645945310660656` (172 KB)
- `cdn.intellimize.co/snippet/117780823.js` (370 KB raw / 87 KB gz)
- `js.hs-banner.com/v2/7182124/banner.js` (67 KB)

### Iframes missing `loading="lazy"`
- Homepage hero Wistia embed (Embedly)
- Pricing — three Wistia embeds (Embedly)

---

## 5. Ranked Fix List — P0 / P1 / P2

### P0 — Do these first (biggest wins, lowest risk)

1. **Defer or async the 9 render-blocking head scripts.** Specifically, add `defer` to: GSAP, both jQueries (and ideally remove one — see #2), Webflow site JS, Typekit/WebFont loader, RevenueHero scheduler (or move to `/donordock-demo` only), js-cookie, HubSpot form bridge. Webflow lets you toggle this in Site Settings → Custom Code, and individual `<script>` tags in the page-level Embed components can be edited directly. **Projected LCP gain: 400–800 ms mobile.**
2. **Eliminate the duplicate jQuery.** `code.jquery.com/jquery-3.6.0.min.js` is loaded after Webflow's own jQuery 3.5.1. Pick one, remove the other from Site Custom Code. **Saves ~89 KB and a third-party DNS handshake.**
3. **Replace `ImportOptions-optimised.gif` (1.39 MB) with `<video autoplay muted loop playsinline>`** using both MP4 (H.264) and WebM (VP9) sources. Realistic compressed size: 150–250 KB combined. **Saves ~1.1–1.2 MB on the homepage.**
4. **Brotli-enable the Webflow shared CSS bundle** if Webflow account-level CDN config allows it (Webflow does serve brotli when both client and route are set up). At minimum, add `Accept-Encoding` priority client-side cannot fix this — open a Webflow support ticket to confirm brotli on the `cdn.prod.website-files.com` route. **Saves ~11 KB compressed on every page-load, every page.**
5. **Add `fetchpriority="high"` + `loading="eager"` to the LCP image on /pricing, /features, articles index, and individual articles.** Today only the homepage hero has it. **Projected LCP gain: 200–500 ms mobile on those pages.**

### P1 — Big quality-of-life and CLS wins

6. **Add `loading="lazy"` to all iframes**, especially the three Wistia embeds on /pricing and the one on the homepage. One-line fix in each Embed component. **Projected TBT/INP gain: 150–300 ms on those pages.**
7. **Stamp width/height attributes onto every `<img>` tag** the site outputs. Webflow images already have intrinsic file dimensions — add the matching `width=""` and `height=""` attributes via the asset settings or a global Webflow code change. Especially on /pricing (97 imgs), /features (105), and the articles index. **Eliminates the residual CLS risk fully.**
8. **Add preconnect hints for the missing third-party origins:** `connect.facebook.net`, `code.jquery.com`, `ajax.googleapis.com`, `assets.revenuehero.io`, `hubspotonwebflow.com`, `js.hs-scripts.com`. Each one is a saved TLS handshake on cold load (~50–150 ms each on mobile).
9. **Audit which pages actually need RevenueHero, HubSpot form-bridge, Facebook Pixel.** Today they load globally. Move RevenueHero to /donordock-demo only. Move HubSpot form bridge to pages that actually have a HubSpot form. Consider moving Facebook Pixel to load post-LCP (after 2 s or after first user interaction) — most teams use Pixel for conversions, not page-load events, so it doesn't need to fire in the critical path.
10. **Preload the primary web font.** Add `<link rel="preload" as="font" type="font/woff2" crossorigin href="...">` for whichever Montserrat (or Typekit family) weight is used in H1/hero. **Projected LCP gain: 100–300 ms when font swaps in.**
11. **Consolidate Montserrat to a single variable font file.** Today the site loads multiple weights as separate woff2 files via Google Fonts. A single `Montserrat-VariableFont.woff2` is ~50–60 KB and replaces 5+ files of ~35 KB each.

### P2 — Polish and longer-term

12. **Critical-CSS extraction.** Ship a small inline `<style>` block with above-the-fold styles (~10–15 KB), then load the 1.18 MB shared.css with `media="print"` swap-on-load pattern. This is a Webflow-platform limitation — confirm whether Webflow's "Page-level Custom Code" + "minify CSS" can be combined with a CSS-extraction tool, or whether this requires moving to a static-site front-door.
13. **Audit GSAP usage.** GSAP (72.9 KB raw) is loaded globally. If it's only used on a small set of components, lazy-load it via dynamic `import()` after first interaction. If used everywhere for hero animation, the LCP image preload + `fetchpriority` mitigations in P0 will reduce its impact.
14. **Code-split inline JS blocks.** Pricing has 22 KB of inline JS; Homepage has 16 KB. Move A/B test logic, analytics setup, and feature flags into a single deferred external file with proper caching.
15. **Consider replacing Embedly+Wistia chain** with direct Wistia embeds (`fast.wistia.net`) — saves the Embedly bridge layer (~50 KB JS, separate domain).
16. **Re-test with a Lighthouse mobile run** after P0+P1 are shipped. Set Webflow performance budget alarms for LCP > 2.5 s, CLS > 0.1, and TBT > 200 ms.

---

## Appendix A — Headers & Caching Posture

- HTTP/2 confirmed; `alt-svc: h3=":443"` advertised.
- Cloudflare CDN, `cf-cache-status: DYNAMIC` for all sampled HTML (HTML is not edge-cached, but `o2o-cache-status: HIT` shows Webflow's origin-on-origin cache is warm — TTFB is 130–290 ms which is healthy).
- `strict-transport-security: max-age=31536000` set.
- `surrogate-control: max-age=432000` (5 days) on HTML — appropriate for a marketing site.
- `vary: accept-encoding` set correctly.
- No `cache-control: max-age` returned on HTML responses (relies on surrogate). Static asset cache headers were not exhaustively audited — recommend verifying CSS/JS bundles ship with `cache-control: public, max-age=31536000, immutable`.

## Appendix B — Method & Caveats

- Field data (CrUX) was not pulled for this report. To finalize CWV scores, run a CrUX API lookup or PageSpeed Insights on each sampled URL and replace the projected LCP/CLS/INP values in §2.
- Lab data (Lighthouse) was not run in this environment; numbers in §2 are projected from on-page signals (asset size, blocking depth, image dimensioning). They are intentionally given as ranges, not single point values.
- All projections assume the typical Webflow + Cloudflare path. If the user is geographically far from the US-east-1 region (`x-wf-region: us-east-1`), TTFB and LCP will both shift up.
- The browser sandbox used during this session intermittently blocked URL-bearing JS output and redirected to /pricing on reload, so live `PerformanceObserver` LCP values were captured only partially. Source-of-truth numbers therefore come from headers + raw HTML inspection + asset HEAD/GET probes.
