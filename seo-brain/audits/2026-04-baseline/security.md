# Security Headers Audit — donordock.com
**Audit Date:** 2026-04-22
**Target:** https://donordock.com (→ https://www.donordock.com)
**Stack:** Webflow hosting + Cloudflare edge
**Audit Type:** Phase 1 baseline — observation only

---

## Executive Summary

DonorDock's security posture is **moderate-to-good for a marketing site** but leaves meaningful SEO trust signals on the table. Site is served end-to-end over HTTPS with valid TLS 1.2/1.3 and HTTP/2 + HTTP/3 via Cloudflare. Three of the "critical seven" security headers are present: **HSTS**, **X-Frame-Options**, and a partial **Content-Security-Policy** (frame-ancestors only).

**Missing:** full CSP (script/style/connect), **X-Content-Type-Options**, **Referrer-Policy**, **Permissions-Policy**, **Cross-Origin-Opener-Policy (COOP)**, **Cross-Origin-Embedder-Policy (COEP)**, **Cross-Origin-Resource-Policy (CORP)**.

None currently block Google crawling. But absence is detectable by security scanners (Mozilla Observatory, securityheaders.com, Lighthouse Best Practices). Lighthouse Best Practices flows into GSC "Page Experience."

**Net SEO effect:** No current penalty. Measurable upside of 10–15 points on Lighthouse Best Practices. More importantly: DonorDock serves nonprofits handling donor PII — visible security hygiene is a trust signal prospects check.

**All fixes applyable at Cloudflare edge** (Transform Rules → Response Headers). No dev work. 30 minutes for cautious rollout.

---

## Security Score: 62/100 (C+)

| Dimension | Score | Grade |
|---|---|---|
| Transport Security (HTTPS/TLS/HSTS) | 95 | A |
| Clickjacking Defense | 90 | A |
| Content Security Policy | 35 | D |
| MIME Sniffing Protection | 0 | F |
| Referrer Leakage Control | 0 | F |
| Feature/Permissions Policy | 0 | F |
| Cross-Origin Isolation | 0 | F |
| Cookie Security | 80 | B |

---

## Per-Header Analysis

### HSTS — Present, partially configured
**Observed:** `strict-transport-security: max-age=31536000`
- Missing `includeSubDomains` — app.donordock.com, help.donordock.com etc not protected by parent policy
- Missing `preload` — not eligible for HSTS Preload List

**Exact header to set:**
```
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
```
Note: Only add `preload` after confirming every subdomain supports HTTPS. Preload is effectively permanent.

### CSP — Minimal (frame-ancestors only)
**Observed:** `content-security-policy: frame-ancestors 'self'`

Missing: default-src, script-src, style-src, img-src, connect-src, font-src, form-action, base-uri, object-src, upgrade-insecure-requests.

**Recommended staged rollout** — Report-Only mode for 7–14 days, collect violation reports, then switch to enforcing:

```
Content-Security-Policy-Report-Only: default-src 'self' https:; script-src 'self' 'unsafe-inline' 'unsafe-eval' https://*.webflow.com https://*.website-files.com https://www.googletagmanager.com https://www.google-analytics.com https://www.youtube.com https://cdn.jsdelivr.net; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://*.webflow.com https://*.website-files.com; img-src 'self' data: https: blob:; font-src 'self' https://fonts.gstatic.com data:; connect-src 'self' https://www.google-analytics.com https://*.hubspot.com https://*.hsforms.com; frame-src 'self' https://www.youtube.com https://*.hubspot.com; frame-ancestors 'self'; base-uri 'self'; form-action 'self' https://*.hubspot.com; object-src 'none'; upgrade-insecure-requests
```

### X-Frame-Options — Present and correct
**Observed:** `x-frame-options: SAMEORIGIN` — keep as-is

### X-Content-Type-Options — MISSING
Cheapest, safest security header to add. Zero compatibility risk.
**Set:** `X-Content-Type-Options: nosniff`
**SEO impact:** Direct Lighthouse Best Practices check. Missing = visible red flag in PageSpeed Insights.

### Referrer-Policy — MISSING
**Set:** `Referrer-Policy: strict-origin-when-cross-origin`
**SEO impact:** Analytics accuracy (partners see less referral data), backlink reciprocity, privacy compliance.

### Permissions-Policy — MISSING
**Set (restrictive, safe for marketing site):**
```
Permissions-Policy: accelerometer=(), ambient-light-sensor=(), autoplay=(self), battery=(), camera=(), cross-origin-isolated=(), display-capture=(), document-domain=(), encrypted-media=(), execution-while-not-rendered=(), execution-while-out-of-viewport=(), fullscreen=(self), geolocation=(), gyroscope=(), keyboard-map=(), magnetometer=(), microphone=(), midi=(), navigation-override=(), payment=(), picture-in-picture=(self), publickey-credentials-get=(), screen-wake-lock=(), sync-xhr=(self), usb=(), web-share=(self), xr-spatial-tracking=(), interest-cohort=()
```

### COOP — MISSING
**Set:** `Cross-Origin-Opener-Policy: same-origin-allow-popups` (safer) or `same-origin`

### COEP — MISSING (high breakage risk)
Defer. Not needed for marketing site. Only required for SharedArrayBuffer.

### CORP — MISSING
**Set:** `Cross-Origin-Resource-Policy: same-site` (allows www + app subdomain asset sharing)

---

## HTTPS/TLS Configuration — EXCELLENT

| Check | Status |
|---|---|
| HTTPS | ✓ Pass (301 http→https) |
| TLS 1.2 / 1.3 | ✓ Pass |
| TLS 1.0/1.1 disabled | ✓ Pass |
| HTTP/2 | ✓ Pass |
| HTTP/3 (QUIC) | ✓ Pass (`alt-svc: h3=":443"`) |
| Apex → www redirect | ✓ Pass |
| Mixed content | ✓ None detected |
| Certificate | ✓ Cloudflare valid |

---

## Cookie Security

**Observed:** `_cfuvid` (Cloudflare visitor ID)
- `Secure` ✓, `HttpOnly` ✓, `SameSite=None` (required for cross-origin CDN), `Path=/`, `Domain=donordock.com`

Only Cloudflare infrastructure cookie set. No first-party DonorDock session cookies on marketing site (correct — app lives on subdomain).

---

## Exact Cloudflare Transform Rule Config

**Rules → Transform Rules → Modify Response Header** — action "Set static":

| Header | Value |
|---|---|
| Strict-Transport-Security | `max-age=63072000; includeSubDomains; preload` |
| X-Content-Type-Options | `nosniff` |
| Referrer-Policy | `strict-origin-when-cross-origin` |
| Permissions-Policy | (see full string above) |
| Cross-Origin-Opener-Policy | `same-origin-allow-popups` |
| Cross-Origin-Resource-Policy | `same-site` |
| Content-Security-Policy-Report-Only | (see full string above) |

**Filter expression:** `(http.host eq "www.donordock.com") or (http.host eq "donordock.com")`

---

## Quick Wins (Priority Order)

1. **Add `X-Content-Type-Options: nosniff`** — zero risk, 30-second fix, immediate Lighthouse bump
2. **Add `Referrer-Policy: strict-origin-when-cross-origin`** — zero risk, fixes analytics
3. **Add Permissions-Policy** — zero risk on marketing site, strong trust signal
4. **Upgrade HSTS** to `max-age=63072000; includeSubDomains` (hold off on preload until subdomain audit)
5. **Deploy CSP Report-Only** — 7-14 days telemetry before enforcing
6. **Add CORP `same-site`** — prevents hotlinking
7. **Add COOP `same-origin-allow-popups`** — test HubSpot forms + Webflow popups after

**Deferred:** COEP (high breakage risk, low SEO value for marketing site); HSTS preload submission (wait for subdomain coverage confirmation)

---

## Strategic Recommendations

**Phase 1 (next 2 weeks):** Quick wins 1, 2, 3, 6. Single Cloudflare Transform Rule. Moves from C+ to B+. Monitor RUM 48 hours.

**Phase 2 (weeks 3-4):** CSP Report-Only deployment. Report endpoint via Cloudflare Workers or report-uri.com. 10-14 days of data, then enforce.

**Phase 3 (month 2+):** Subdomain hardening. Audit every subdomain for HTTPS. Once coverage confirmed, enable `includeSubDomains` and submit to HSTS preload.

**Monitoring:** Monthly securityheaders.com scan, Lighthouse Best Practices threshold alerts. When adding any new third-party script, update CSP in same PR — otherwise CSP drift will force permanent `'unsafe-inline'`.

**SEO value summary of Phase 1+2:**
- Lighthouse Best Practices: +10 to +15 points (est. 85 → 95+)
- GSC Page Experience: stays in Good with stronger margin
- Vendor security questionnaires: moves from "partial" to "meets best practice"
- Direct ranking impact: small. HTTPS is a ranking factor, other headers are indirect trust signals.

**Watch-out:** If CSP is enforcing and Webflow pushes new inline script source, page breaks silently. Keep report endpoint always-on (even post-enforcement), review weekly. If Webflow update introduces new required source, add to allowlist within an hour.

**End of audit.**
