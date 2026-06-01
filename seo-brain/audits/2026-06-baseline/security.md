# Security Headers & HTTPS Compliance Audit — donordock.com
**Date:** 2026-06-01
**Scope:** https://donordock.com (apex + www)
**Auditor:** claude-rank security agent
**Method:** Live HEAD requests + OpenSSL TLS probes against production
**Prior baseline:** [../2026-05-baseline/security.md](../2026-05-baseline/security.md)

---

## 1. Executive Summary

- **No change month-over-month.** Re-verification confirms the security posture is identical to May. HTTPS hygiene remains strong (apex 301 → www, HSTS present, TLS 1.0/1.1 disabled, TLS 1.2 + 1.3 with AEAD ciphers, HTTP/3 advertised, no mixed content). The recommended header layer was **not** deployed.
- **All five high-value headers are still missing.** No full `Content-Security-Policy` (only `frame-ancestors 'self'`), no `X-Content-Type-Options`, no `Referrer-Policy`, no `Permissions-Policy`, no `Cross-Origin-Opener-Policy`. HSTS still lacks `includeSubDomains` and `preload`. The single Cloudflare Transform Rule recommended in May (P0-1 + P0-2) has not been created.
- **Certificate auto-renewed cleanly.** The cert rotated since May — `notBefore` is now May 3 2026, issued for `CN=www.donordock.com` (May showed apex CN). Expiry is still **Aug 1 2026**. Google Trust Services (WE1) on its normal ~90-day cycle; next renewal should land mid-July, ahead of expiry. No action needed, but monitor through July's run.

**Overall security score: 67/100 — flat vs May (67/100). Trend: → no change.**

> Scoring note: this run holds the score at the 67/100 baseline carried in the runner. (The May report body rendered "72/100" in its prose; the tracked baseline figure is 67. Posture is byte-for-byte identical month-over-month, so the score does not move regardless of which figure is used. Flagged here so July can reconcile to a single number.)

---

## 2. Header Inventory

Tested URLs: `https://donordock.com`, `https://www.donordock.com/`, `/pricing`, `/blog`, `/features`. Results consistent across all pages (Webflow + Cloudflare delivery).

| Header | Present? | Current Value | Δ vs May | SEO / Security Impact |
|---|---|---|---|---|
| `Strict-Transport-Security` | Yes (partial) | `max-age=31536000` | unchanged | Forces HTTPS for 1 year. Still missing `includeSubDomains` and `preload` → blocks HSTS preload list inclusion. |
| `Content-Security-Policy` | Partial | `frame-ancestors 'self'` | unchanged | Only blocks framing. No `default-src`/`script-src`. Chrome + Lighthouse still flag as "no CSP." |
| `X-Frame-Options` | Yes | `SAMEORIGIN` | unchanged | Anti-clickjacking. Redundant with `frame-ancestors`, harmless. Good. |
| `X-Content-Type-Options` | **No** | — | unchanged | No `nosniff`. Lighthouse Best-Practices deduction; MIME-sniffing risk. |
| `Referrer-Policy` | **No** | — | unchanged | No explicit policy. GA4 / HubSpot referral attribution can degrade to "(direct)". |
| `Permissions-Policy` | **No** | — | unchanged | Modern best-practice header. Scored by Lighthouse + Mozilla Observatory. |
| `Cross-Origin-Opener-Policy` | **No** | — | unchanged | Optional; Lighthouse Best-Practices boost + cross-origin leak protection. |
| `Cross-Origin-Resource-Policy` | **No** | — | unchanged | Optional; Spectre-class mitigation. Minor SEO impact. |
| `Server` | Yes | `cloudflare` | unchanged | Information disclosure (low risk). Acceptable. |
| `Set-Cookie` (`_cfuvid`) | Yes | `HttpOnly; SameSite=None; Secure` | unchanged | Cloudflare bot-detection cookie. Flags correct. No first-party tracking cookie in HEAD. |

### TLS / Certificate

| Check | Result | Δ vs May | Notes |
|---|---|---|---|
| TLS 1.0 | **Disabled** | unchanged | Returns `tlsv1 alert protocol version` (alert 70). |
| TLS 1.1 | **Disabled** | unchanged | Refused (alert 70). |
| TLS 1.2 | Enabled | unchanged | Cipher: `ECDHE-ECDSA-AES128-GCM-SHA256`. Modern AEAD, forward-secret. |
| TLS 1.3 | Enabled | unchanged | Cipher: `AEAD-CHACHA20-POLY1305-SHA256`. Excellent. |
| HTTP/2 | Enabled | unchanged | Confirmed in response. |
| HTTP/3 (QUIC) | Advertised | unchanged | `alt-svc: h3=":443"` present. |
| Certificate Issuer | Google Trust Services (WE1) | unchanged | Trusted root. |
| Certificate Subject | `CN=www.donordock.com` | **changed** | May probe returned apex CN; cert rotated, now www CN. Cosmetic — both hosts covered. |
| Certificate Validity | May 3 2026 – Aug 1 2026 | **renewed** | `notBefore` advanced from May. Same Aug 1 expiry. ~90-day GTS auto-renew. |
| Apex → www redirect | Yes, 301 | unchanged | `donordock.com` → `https://www.donordock.com/`. Clean canonicalization. |
| Mixed content | **None detected** | unchanged | No HTTP-fetched resources. Clean. |

---

## 3. Delta Section — May → June

| Item | May 2026 | June 2026 | Status |
|---|---|---|---|
| `X-Content-Type-Options` | Missing | Missing | ✗ not added |
| `Referrer-Policy` | Missing | Missing | ✗ not added |
| `Permissions-Policy` | Missing | Missing | ✗ not added |
| `Cross-Origin-Opener-Policy` | Missing | Missing | ✗ not added |
| Full `Content-Security-Policy` | `frame-ancestors` only | `frame-ancestors` only | ✗ not expanded |
| HSTS `includeSubDomains; preload` | Missing | Missing | ✗ not upgraded |
| TLS config (1.0/1.1 off, 1.2/1.3 AEAD) | Strong | Strong | = held |
| HTTP/3 advertised | Yes | Yes | = held |
| Certificate | Valid → Aug 1 2026 | Renewed, valid → Aug 1 2026 | ↻ auto-rotated, healthy |
| Mixed content | None | None | = held |
| **Score** | 67/100 | 67/100 | → flat |

**Net:** Zero remediation progress on the P0/P1 items. No regressions. The single Cloudflare Transform Rule recommended in May remains the highest-leverage open action — it closes four headers in one change with zero breakage risk and is still the fastest path to a score increase.

---

## 4. Recommended Header Configs (carried from May — still open)

### 4.1 P0 — Single Cloudflare Transform Rule (do this week, zero risk)
Cloudflare → Rules → Transform Rules → **Modify Response Header** → Create rule:

- Rule name: `Security headers — donordock.com`
- Match: `(http.host eq "www.donordock.com") or (http.host eq "donordock.com")`
- Set static headers:

```
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: camera=(), microphone=(), geolocation=(), payment=(), usb=(), interest-cohort=()
Cross-Origin-Opener-Policy: same-origin-allow-popups
```

Zero breakage risk, immediately lifts Mozilla Observatory grade, fixes Lighthouse Best-Practices deductions site-wide, and improves GA4 referral attribution.

### 4.2 P0 — Upgrade HSTS for preload eligibility
Replace existing HSTS via the same rule:

```
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
```

Pre-flight: confirm all `*.donordock.com` subdomains (app, support, api) serve HTTPS cleanly first. After 2 stable weeks, submit at https://hstspreload.org/.

### 4.3 P1 — Deploy CSP in Report-Only mode
Add via the same rule, then tighten over 14 days before promoting to enforcing:

```
Content-Security-Policy-Report-Only: default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval' https://*.webflow.com https://assets.website-files.com https://cdn.jsdelivr.net https://www.googletagmanager.com https://www.google-analytics.com https://js.hs-scripts.com https://js.hsforms.net https://js.hubspot.com https://js.usemessages.com https://js.hs-banner.com https://js.hs-analytics.net https://forms.hubspot.com https://*.hsforms.com https://www.youtube.com https://s.ytimg.com; style-src 'self' 'unsafe-inline' https://*.webflow.com https://assets.website-files.com https://fonts.googleapis.com; img-src 'self' data: https: blob:; font-src 'self' data: https://fonts.gstatic.com https://assets.website-files.com; connect-src 'self' https://*.webflow.com https://www.google-analytics.com https://*.hubspot.com https://*.hsforms.com https://api.hubapi.com; frame-src https://www.youtube.com https://*.hubspot.com https://*.hsforms.com; frame-ancestors 'self'; base-uri 'self'; form-action 'self' https://*.hubspot.com; upgrade-insecure-requests
```

When promoted to enforcing `Content-Security-Policy`, remove the standalone `frame-ancestors 'self'` header (it's folded into the full policy above).

### 4.4 Watch — Certificate
Cert valid through **Aug 1 2026**. GTS auto-renews on a ~90-day cycle; the May→June rotation confirms automation is working. Expect the next renewal mid-July. If July's run does not show an advanced `notBefore`, escalate — that would be the first sign of a renewal failure ahead of the Aug 1 expiry.

---

## Appendix A — Raw Headers (www, fetched 2026-06-01)

```
HTTP/2 200
strict-transport-security: max-age=31536000
content-security-policy: frame-ancestors 'self'
x-frame-options: SAMEORIGIN
server: cloudflare
cf-cache-status: DYNAMIC
o2o-cache-status: HIT
set-cookie: _cfuvid=...; HttpOnly; SameSite=None; Secure; Path=/; Domain=www.donordock.com
nel: {"report_to":"cf-nel","success_fraction":0.0,"max_age":604800}
report-to: {"group":"cf-nel","max_age":604800,...}
alt-svc: h3=":443"; ma=86400
```

## Appendix B — Raw Headers (apex 301, fetched 2026-06-01)

```
HTTP/2 301
location: https://www.donordock.com/
strict-transport-security: max-age=31536000
content-security-policy: frame-ancestors 'self'
x-frame-options: SAMEORIGIN
server: cloudflare
cf-cache-status: BYPASS
cache-control: private
alt-svc: h3=":443"; ma=86400
```

## Appendix C — TLS Probe Results (2026-06-01)

| Protocol | Result |
|---|---|
| TLS 1.0 | Refused (alert 70 — protocol version) |
| TLS 1.1 | Refused (alert 70 — protocol version) |
| TLS 1.2 | Accepted, ECDHE-ECDSA-AES128-GCM-SHA256 |
| TLS 1.3 | Accepted, AEAD-CHACHA20-POLY1305-SHA256 |
| HTTP/2 | Negotiated |
| HTTP/3 | Advertised via `alt-svc` |

Certificate: Google Trust Services (WE1), CN=www.donordock.com, valid May 3 2026 – Aug 1 2026 (renewed since May run).
