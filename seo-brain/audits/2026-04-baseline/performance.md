# Performance Audit — donordock.com (Baseline)

**Audit date:** 2026-04-22
**URL audited:** https://www.donordock.com/ (homepage)
**Purpose:** Phase 1 baseline for seo-brain/. No auto-fixes applied.
**Platform:** Webflow + Cloudflare (Brotli compression confirmed)

---

## Executive Summary

DonorDock's homepage scores **65/100** on static HTML performance audit — mid-tier baseline driven by (1) render-blocking script sprawl, (2) 1.22 MB uncompressed CSS bundle blocking first paint, (3) mis-configured LCP hero image, (4) duplicate library loads. Fixes are unambiguous, cheap, mostly within Webflow custom-code surface — no re-platforming required.

Signs of recent optimization work exist (Cloudflare + Brotli, preconnects to 7 origins, GTM lazy-loaded on first interaction, Silka fonts use `font-display: optional`, Intellimize anti-flicker timeout capped at 4s). But foundational blocking-resource chain undoes most of it. Estimated Lighthouse mobile Performance: **55–68**.

**Three highest-leverage wins:**
1. Fix the hero image (`width="Auto" height="Auto"` literally broken, no fetchpriority, 216 KB served)
2. Remove duplicate jQuery + js-cookie loads (~90 KB saved + version-conflict risk)
3. Defer 5 render-blocking third-party scripts (400–900 ms off first paint on mobile 4G)

---

## Performance Score: 65/100

| Metric | Value |
|---|---|
| Estimated Lighthouse mobile | 55–68 |
| Estimated Lighthouse desktop | 75–85 |
| High-severity findings | 3 |
| External script domains | 10 |
| Render-blocking scripts in head | 5 |
| Render-blocking scripts in body | 4 |
| CSS (uncompressed) | 1,220,481 bytes (1.22 MB) |

---

## Core Web Vitals Estimates

### LCP — Estimated 2.8–3.6s mobile (FAILING)

LCP element = hero image. Issues:
- 216,298 bytes WebP (heavy for hero)
- `loading="eager"` (correct) but **no `fetchpriority="high"`**
- **`width="Auto" height="Auto"`** — literally string "Auto" (browsers ignore, causes CLS)
- **Not preloaded** — only `<link rel="preload">` in head is Intellimize
- **No srcset** — same 216 KB served to mobile and desktop
- **Intellimize anti-flicker shield blanks page for up to 4 seconds** while script loads

### CLS — Estimated 0.10–0.25 (NEEDS IMPROVEMENT to POOR)

**68 of 69 images missing valid width/height attributes.** CLS contributors:
- Hero image (broken dimensions)
- 62 lazy-loaded images without dimensions
- G2 review badge (third-party, no height reservation)
- HubSpot form embed (injects after script load)
- RevenueHero scheduler widget
- Elfsight platform embed
- Font swap from system → Quicksand (swap not optional)

### INP — Estimated 180–320ms

Main-thread pressure: Two jQuery instances (Webflow's 3.5.1 + separate 3.6.0 overwrites `$` global), GSAP 3.15 (72 KB), HubSpot form-124.js, RevenueHero scheduler, Intellimize 87 KB.

**GTM deferred until first scroll/touch/mousemove** — saving grace.

### TTFB — 180–450ms

Cloudflare `cf-cache-status: BYPASS` on homepage (dynamic). 301 redirect chain `donordock.com → www.donordock.com` costs ~100ms.

---

## Render-Blocking Resources

### HEAD (Critical Chain)
| Order | Resource | Size | Blocking | Notes |
|---|---|---|---|---|
| 1 | `ddstaging.shared.b1cd873e7.min.css` | 179 KB / 1.22 MB | YES | Styles for every page, not just homepage |
| 2 | `webfont.js` (Google WebFont Loader v1.6.26) | 5.4 KB | YES | Ancient library |
| 3 | Inline `WebFont.load` | <1 KB | YES | |
| 4 | `use.typekit.net/cwa7yxm.js` | 6.6 KB | YES | One font, one weight, overkill |
| 5 | Inline `Typekit.load()` | <1 KB | YES | |
| 6 | Inline anti-flicker + Webflow touch | ~2 KB | YES | **4-second whole-page hide** |
| 7 | Intellimize client | 87 KB | Semi | Preloaded + async but page hidden until resolve or 4s timeout |

### BODY
| Script | Size | Attribute | Notes |
|---|---|---|---|
| jQuery 3.5.1 (Webflow) | 89.5 KB | none | Required by Webflow |
| ddstaging.js | 5.5 KB | none | Tiny |
| GSAP 3.15.0 | 72.9 KB | none | Blocks parse |
| RevenueHero scheduler | 28.6 KB | none | Below-fold widget |
| **jQuery 3.6.0 (duplicate)** | 85 KB | none | **Overwrites Webflow's jQuery** |
| HubSpot form-124.js | 10.5 KB | none | Can defer |
| HubSpot tracking | — | async defer | Good |
| js.cookie v3 | — | async | Good |
| **js.cookie v2 (duplicate)** | — | none | **Redundant with v3, blocking** |
| Finsweet cookie consent | — | async | Good |
| Elfsight platform | — | async | Good |

---

## Image Optimization

### Hero / LCP Image — CRITICAL

```html
<img src="...Contact%20Details%20%20DonorDock-10-17-2025.webp"
     loading="eager"
     width="Auto"
     height="Auto"
     alt="Desktop mockup of DonorDock">
```

**Problems:**
1. `width="Auto" height="Auto"` — strings, not numbers — ignored by browsers. Someone typed "Auto" into Webflow attribute field.
2. No `fetchpriority="high"`
3. Not preloaded in head
4. Not responsive (216 KB to all devices)
5. No srcset

**Exact fix:**
```html
<link rel="preload" as="image" href="<hero-url>" fetchpriority="high">
<img src="<hero-url>"
     loading="eager" fetchpriority="high"
     width="1200" height="800"
     srcset="<hero-url>?w=800 800w, <hero-url>?w=1200 1200w, <hero-url>?w=1600 1600w"
     sizes="(max-width: 768px) 100vw, 60vw">
```

### Loading Attribute Distribution
- `loading="eager"`: 5 (should be 1 — only LCP; 4 icons incorrectly eager)
- `loading="lazy"`: 62 (good)
- No loading attribute: 4 (includes G2 badge, `${app.name}` template placeholder — unresolved Webflow component bug)
- With `fetchpriority="high"`: **0** (should be 1)

### Dimension Coverage
- Total `<img>`: 69
- With valid width/height: **1** (close-icon, by accident)
- Missing/broken: **68** — largest CLS driver on page

### Unresolved Webflow Template Bug
```html
<img src="${DD_LOGO}" alt="DonorDock logo">
<img alt="${app.name}" src="${app.url}">
```
Two img tags contain literal template syntax — component variables not populated. Renders as broken images in production. File as separate bug.

---

## Font Loading

DonorDock loads fonts from **four sources** on a single page:

1. **Self-hosted via Webflow:** Silka (3 weights), Quicksand (5 weights), Dancingscript, webflow-icons
2. **Google Fonts via WebFont Loader:** Montserrat (18 variations!), Inconsolata (2)
3. **Adobe Typekit:** Shadows Into Light (1 weight)
4. **Inline icon font:** webflow-icons

**Problems:**
- Shadows Into Light loaded TWICE (self-hosted + Typekit)
- 18 Montserrat variants — overkill
- Quicksand/Dancingscript use `.ttf` instead of `woff2` (30% larger)
- WebFont Loader deprecated since 2016
- Adobe Typekit for one decorative font — poor ROI

Only ONE preload in head — Intellimize. NOT preloaded: hero LCP image, primary webfont, main CSS.

---

## Mobile-First Indexing

**Positive:** viewport meta correct, responsive CSS, WebP hero, Cloudflare+Brotli, googlebot-mobile sees same DOM, HTTPS+HSTS enabled.

**Risk:** 1.22 MB CSS on 4G = 1.5–3s blocking parse. Total main-thread JS >300 KB uncompressed. 216 KB hero to phones (should be <80 KB). 4-second anti-flicker shield.

**Estimated mobile CWV field scores:**
- LCP mobile: 3.0–4.2s → **borderline POOR** (good <2.5s)
- CLS mobile: 0.15–0.28 → **NEEDS IMPROVEMENT to POOR** (good <0.1)
- INP mobile: 180–380ms → **NEEDS IMPROVEMENT** (good <200ms)

Likely failing GSC Core Web Vitals "Needs improvement" or "Poor" tier for Mobile. This is a ranking headwind.

---

## Quick Wins

### Tier 1 — This Week
1. **Fix hero LCP image** — Webflow: set width=1200, height=800, custom attr `fetchpriority="high"`, add preload to homepage head. **Impact:** LCP -400–900ms.
2. **Remove duplicate jQuery 3.6.0** — find custom code, delete. **Impact:** 31 KB saved + no $ collision.
3. **Remove duplicate js-cookie v2** — migrate custom code to v3 (API identical).
4. **Add `defer` to GSAP, HubSpot form-124, RevenueHero** — Webflow Custom Code footer. **Impact:** 65 KB main-thread work deferred, first paint -250–500ms mobile.
5. **Move 4 eager-loaded feature icons to lazy** — Webflow Designer, they're below fold.

### Tier 2 — This Month
6. **Batch-add width/height to every image in Webflow.** One focused hour per template. **Impact:** CLS 0.15–0.25 → under 0.1. Single biggest SEO/CWV ranking risk.
7. **Consolidate font loaders** — Self-host Montserrat + Inconsolata + Shadows Into Light as woff2. Remove WebFont Loader + Typekit entirely.
8. **Reduce Montserrat from 18 variants to 3.**
9. **Audit Intellimize anti-flicker 4-second shield** — scope to specific mutable elements only. Largest LCP threat on slow connections.
10. **Preload hero image and primary webfont.**

### Tier 3 — This Quarter
11. **Split the 1.22 MB CSS bundle.** Hardest fix but highest ceiling. LCP -600ms+ mobile 4G.
12. **Lazy-load RevenueHero** (fire on CTA click).
13. **Replace Elfsight with static HTML.**
14. **Set up real CWV monitoring** — PageSpeed Insights API, GSC CWV report, or RUM tool.
15. **Fix unresolved Webflow template placeholders** (`${DD_LOGO}`, `${app.name}`).

---

## Strategic Recommendations

1. **Treat baseline as ceiling, not floor.** Capture real CrUX field data in Phase 2.
2. **Webflow platform tax is real but solvable.** Mega-CSS bundle is biggest constraint.
3. **Consolidation beats optimization.** 10+ third-party script domains — audit each for ROI. One removal > five micro-optimizations.
4. **Font strategy is quick strategic win.** 4-source, 9-family, 30+-variant load is inherited complexity.
5. **Build performance budget into Webflow workflow.** Publish budget in seo-brain/: "any new image must have width/height and loading," "any new script must be deferred/async," "third-party domains capped at 8."
6. **CLS is hidden ranking killer.** 68/69 images no dimensions = likely "Needs improvement" band. Batch-fix flips entire site to CLS Good band.
7. **Re-audit after each Tier batch.** Fix, re-scan, confirm, next tier.

**For DonorDock leadership:** GSC is almost certainly flagging CWV issues on mobile. Check GSC → Core Web Vitals in the next 30 days — tells you real user experience. Good bones: Cloudflare+Brotli, mostly-correct lazy loading, Silka font-display optional, GTM lazy. Remaining issues concentrated in surgical fixes, not re-platform.

**End of report.**
