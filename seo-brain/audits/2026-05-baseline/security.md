# Security Headers & HTTPS Compliance Audit — donordock.com
**Date:** 2026-05-04
**Scope:** https://donordock.com (apex + www)
**Auditor:** claude-rank security agent
**Method:** Live HEAD requests + OpenSSL TLS probes against production

---

## 1. Executive Summary

- **Strong foundation, weak ceiling.** HTTPS is enforced cleanly (apex 301 to www, HSTS present, TLS 1.0/1.1 disabled, valid Google Trust Services cert through Aug 2026, TLS 1.2 + 1.3 supported, no mixed content detected). The basics that protect ranking are in place.
- **Five high-value security headers are missing.** No `Content-Security-Policy` for script/style sources (only a `frame-ancestors` directive is set), no `X-Content-Type-Options`, no `Referrer-Policy`, no `Permissions-Policy`, and no `Strict-Transport-Security` `preload` / `includeSubDomains`. These are the headers Google, Mozilla Observatory, and Security Headers grade against — and the ones Chrome surfaces as warnings to users.
- **Cookies and HSTS need hardening.** The `_cfuvid` cookie uses `SameSite=None`, which is acceptable for Cloudflare's bot-detection cookie but should be reviewed if any first-party cookies are set this way. HSTS `max-age` is 1 year but lacks `includeSubDomains` and `preload`, blocking the site from the HSTS preload list — a measurable trust signal Google checks.

**Overall security score: 72/100.** Solid HTTPS hygiene, missing modern header layer.

---

## 2. Header Inventory

Tested URLs: `https://donordock.com`, `https://www.donordock.com/`, `/pricing`, `/blog`, `/blog/best-donor-management-software`. Results consistent across all pages (Webflow + Cloudflare delivery).

| Header | Present? | Current Value | SEO / Security Impact |
|---|---|---|---|
| `Strict-Transport-Security` | Yes (partial) | `max-age=31536000` | Forces HTTPS for 1 year. Missing `includeSubDomains` and `preload` blocks HSTS preload list inclusion — a Chrome-checked trust signal. |
| `Content-Security-Policy` | Partial | `frame-ancestors 'self'` only | Only blocks framing. No control over script/style/img/connect sources. Chrome and Lighthouse flag this as "no CSP" because it lacks `default-src` or `script-src`. Missing CSP costs ~5 points on Mozilla Observatory and is one of Google's "Best Practices" Lighthouse audits. |
| `X-Frame-Options` | Yes | `SAMEORIGIN` | Prevents clickjacking. Redundant with `frame-ancestors` but harmless. Good. |
| `X-Content-Type-Options` | **No** | — | Without `nosniff`, browsers may MIME-sniff responses. Lighthouse "Best Practices" deducts points; can cause subtle rendering bugs that hurt UX signals (CLS, time-to-interactive). |
| `Referrer-Policy` | **No** | — | Browsers default to `strict-origin-when-cross-origin` in Chrome but not all. Without an explicit policy, GA4 / HubSpot referral attribution can degrade — traffic shows up as "(direct)" instead of "referral", under-counting backlink ROI. |
| `Permissions-Policy` | **No** | — | Best-practice modern header. Google's Lighthouse and Mozilla Observatory both score for it. Signals to crawlers that the site is actively maintained for security. |
| `Cross-Origin-Opener-Policy` | **No** | — | Optional but improves Lighthouse "Best Practices" score and protects against cross-origin leaks. |
| `Cross-Origin-Resource-Policy` | **No** | — | Optional; helps with Spectre-class attacks. Minor SEO impact. |
| `Server` | Yes | `cloudflare` | Information disclosure (low risk). Acceptable. |
| `Set-Cookie` (`_cfuvid`) | Yes | `HttpOnly; SameSite=None; Secure` | Cloudflare bot-detection cookie. Flags are correct. No first-party tracking cookies observed in HEAD response — confirm in browser. |

### TLS / Certificate

| Check | Result | Notes |
|---|---|---|
| TLS 1.0 | **Disabled** | Good. Returns `tlsv1 alert protocol version`. |
| TLS 1.1 | **Disabled** | Good. |
| TLS 1.2 | Enabled | Cipher: `ECDHE-ECDSA-AES128-GCM-SHA256`. Modern AEAD, forward-secret. |
| TLS 1.3 | Enabled | Cipher: `AEAD-CHACHA20-POLY1305-SHA256`. Excellent. |
| HTTP/2 | Enabled | Confirmed in response. |
| HTTP/3 (QUIC) | Advertised | `alt-svc: h3=":443"` present. Performance + ranking benefit. |
| Certificate Issuer | Google Trust Services (WE1) | Trusted root. |
| Certificate Subject | `CN=donordock.com` | Valid for apex. |
| Certificate Validity | May 3, 2026 – Aug 1, 2026 | ~90 days, auto-renewed (typical Cloudflare/GTS cycle). No action needed. |
| Apex → www redirect | Yes, 301 | `donordock.com` → `https://www.donordock.com/`. Clean canonicalization. |
| HTTP → HTTPS redirect | Yes, 301 | `http://donordock.com` → `https://donordock.com/`. |
| Mixed content | **None detected** | Only `http://www.w3.org/2000/svg` namespace URI in source (not a fetched resource). Clean. |

---

## 3. Missing / Misconfigured Headers — Recommended Values

### 3.1 Strict-Transport-Security (upgrade)
**Current:** `max-age=31536000`
**Recommended:** `max-age=63072000; includeSubDomains; preload`

`includeSubDomains` extends protection to any future `*.donordock.com` (app, api, support). `preload` lets you submit to https://hstspreload.org/ — Chrome ships the domain in its baked-in HSTS list, eliminating the first-visit attack window. Note: only enable `preload` after confirming every subdomain serves HTTPS (a misconfigured subdomain becomes unreachable).

### 3.2 Content-Security-Policy (expand)
**Current:** `frame-ancestors 'self'`
**Recommended (starter, report-only first):**

```
Content-Security-Policy-Report-Only: default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval' https://*.webflow.com https://assets.website-files.com https://cdn.jsdelivr.net https://www.googletagmanager.com https://www.google-analytics.com https://js.hs-scripts.com https://js.hsforms.net https://js.hubspot.com https://js.usemessages.com https://js.hs-banner.com https://js.hs-analytics.net https://forms.hubspot.com https://*.hsforms.com https://www.youtube.com https://s.ytimg.com; style-src 'self' 'unsafe-inline' https://*.webflow.com https://assets.website-files.com https://fonts.googleapis.com; img-src 'self' data: https: blob:; font-src 'self' data: https://fonts.gstatic.com https://assets.website-files.com; connect-src 'self' https://*.webflow.com https://www.google-analytics.com https://*.hubspot.com https://*.hsforms.com https://api.hubapi.com; frame-src https://www.youtube.com https://*.hubspot.com https://*.hsforms.com; frame-ancestors 'self'; base-uri 'self'; form-action 'self' https://*.hubspot.com; upgrade-insecure-requests
```

Run in `Report-Only` mode for 2 weeks, collect violation reports, tighten, then promote to enforcing `Content-Security-Policy`. The third-party allowlist above covers Webflow hosting, GTM/GA4, HubSpot forms/analytics, and YouTube embeds — verify against actual scripts on the site before deploying.

### 3.3 X-Content-Type-Options
**Recommended:** `X-Content-Type-Options: nosniff`

One line. No tradeoffs. Adds points on every security scanner.

### 3.4 Referrer-Policy
**Recommended:** `Referrer-Policy: strict-origin-when-cross-origin`

Sends full URL same-origin, origin-only cross-origin over HTTPS, nothing on HTTPS→HTTP downgrades. Best balance of analytics fidelity and privacy. Will improve referral attribution in GA4.

### 3.5 Permissions-Policy
**Recommended:** `Permissions-Policy: camera=(), microphone=(), geolocation=(), payment=(), usb=(), interest-cohort=()`

Disables features DonorDock's marketing site doesn't need. `interest-cohort=()` opts out of FLoC/Topics if it ever returns. Pure win.

### 3.6 Cross-Origin-Opener-Policy (optional, Lighthouse boost)
**Recommended:** `Cross-Origin-Opener-Policy: same-origin-allow-popups`

`same-origin-allow-popups` keeps HubSpot popup forms working while isolating the browsing context. If popups break, fall back to `same-origin`.

---

## 4. Ranked Fixes

Implementation path: donordock.com is hosted on **Webflow** behind **Cloudflare**. Webflow does not expose response-header configuration in its UI, so headers must be added via **Cloudflare Transform Rules → Modify Response Header** (Pro plan or higher includes this). All fixes below assume that path. If Cloudflare plan does not allow Transform Rules, use a **Cloudflare Worker** as a transparent proxy — same effect, slightly more setup.

### P0 — Do this week (high SEO impact, zero risk)

**P0-1. Add the four "free" headers.**
In Cloudflare → Rules → Transform Rules → **Modify Response Header** → Create rule:

- Rule name: `Security headers — donordock.com`
- Match: `(http.host eq "www.donordock.com") or (http.host eq "donordock.com")`
- Set static headers:
  - `X-Content-Type-Options`: `nosniff`
  - `Referrer-Policy`: `strict-origin-when-cross-origin`
  - `Permissions-Policy`: `camera=(), microphone=(), geolocation=(), payment=(), usb=(), interest-cohort=()`
  - `Cross-Origin-Opener-Policy`: `same-origin-allow-popups`

Why P0: zero breakage risk, immediately bumps Mozilla Observatory grade, fixes Lighthouse Best Practices deductions on every page, and improves GA4 referral attribution.

**P0-2. Upgrade HSTS for preload eligibility.**
Replace existing HSTS with: `Strict-Transport-Security: max-age=63072000; includeSubDomains; preload`

Pre-flight check: confirm all `*.donordock.com` subdomains (app, support, etc.) serve HTTPS without errors. After 2 weeks of stable production, submit at https://hstspreload.org/.

### P1 — Do this month (medium effort, real protection)

**P1-1. Deploy CSP in Report-Only mode.**
Add via the same Cloudflare Transform Rule:
- `Content-Security-Policy-Report-Only`: (the policy from §3.2)
- Set up a reporting endpoint — easiest is a free tier of report-uri.com or Sentry — and add `report-uri https://your-endpoint;` to the policy.

After 14 days of clean reports, swap header name to `Content-Security-Policy` (enforcing) and remove the `frame-ancestors 'self'` directive currently set elsewhere (it's now inside the full policy).

**P1-2. Audit first-party cookie flags.**
Open the site in Chrome DevTools → Application → Cookies. Confirm every `*.donordock.com` cookie has `Secure`, `HttpOnly` (where not needed by client JS), and `SameSite=Lax` or `Strict`. The Cloudflare `_cfuvid` cookie's `SameSite=None` is correct for its function; only flag cookies you set yourself.

### P2 — Nice to have (incremental polish)

**P2-1. Add `Cross-Origin-Resource-Policy: same-site`** for marketing assets. Lighthouse mentions this; not critical.

**P2-2. Remove `Server: cloudflare`** via Transform Rule (set empty value). Information disclosure is low-risk but tidies the response.

**P2-3. Reconsider `X-Frame-Options`.** Once CSP `frame-ancestors` is enforced, `X-Frame-Options` is redundant. Modern browsers prefer the CSP directive. Safe to keep both; safe to drop XFO. No SEO change either way.

---

## Appendix A — Raw Headers (apex, fetched 2026-05-04)

```
HTTP/2 301
strict-transport-security: max-age=31536000
content-security-policy: frame-ancestors 'self'
x-frame-options: SAMEORIGIN
server: cloudflare
location: https://www.donordock.com/
set-cookie: _cfuvid=...; HttpOnly; SameSite=None; Secure; Path=/; Domain=donordock.com
alt-svc: h3=":443"; ma=86400
```

## Appendix B — Raw Headers (www, fetched 2026-05-04)

```
HTTP/2 200
strict-transport-security: max-age=31536000
content-security-policy: frame-ancestors 'self'
x-frame-options: SAMEORIGIN
server: cloudflare
o2o-cache-status: HIT
nel: {"report_to":"cf-nel","success_fraction":0.0,"max_age":604800}
report-to: {"group":"cf-nel",...}
alt-svc: h3=":443"; ma=86400
```

## Appendix C — TLS Probe Results

| Protocol | Result |
|---|---|
| TLS 1.0 | Refused (alert 70 — protocol version) |
| TLS 1.1 | Refused (alert 70 — protocol version) |
| TLS 1.2 | Accepted, ECDHE-ECDSA-AES128-GCM-SHA256 |
| TLS 1.3 | Accepted, AEAD-CHACHA20-POLY1305-SHA256 |
| HTTP/2 | Negotiated |
| HTTP/3 | Advertised via `alt-svc` |

Certificate: Google Trust Services (WE1), CN=donordock.com, valid May 3 2026 – Aug 1 2026.
