# Vertical SEO Audit — donordock.com

**Vertical:** SaaS + Nonprofit-Tech (Donor Management / Nonprofit CRM)
**Audit date:** 2026-06-01
**Scope:** SoftwareApplication schema, pricing transparency, trial/demo UX, comparison pages, nonprofit trust signals, review-platform presence, vertical keyword targeting.
**Auditor:** Vertical Auditor (claude-rank)
**Prior baseline:** [../2026-05-baseline/vertical.md](../2026-05-baseline/vertical.md)

---

## 1. Executive Summary

- **Score holds at 52/100 (May ~50). Marginal upward drift — no breakthrough.** Two small wins landed (a real `/features/trust-and-security` page now exists; `/crm` gained `applicationSubCategory: "CRM Software"`), but the two structural blockers flagged in May are **both unchanged**: zero functional free-trial CTA sitewide, and G2/Capterra still absent from every Organization `sameAs`. The site is iterating at the margins, not on the high-ROI items.

- **The free-trial story is now actively misleading in the markup.** New CSS hooks appeared in the DOM — `id="Start-for-Free-Button"`, `class="start-trial-cta"`, `class="start-14-day-trial-cta"` — but **every one of them renders the label "Schedule a Demo" and links to `/donordock-demo`.** The `/tour` "start-14-day-trial" block literally reads *"Schedule a demo and see why 7,200+ people trust DonorDock."* It looks like the dev team scaffolded a trial flow and never wired it up. From a user/crawler standpoint the trial does not exist; from a maintenance standpoint there's now dead/aspirational naming that should either be shipped or removed. **Verdict: free-trial CTA status = still zero.**

- **`sameAs` remains social-only.** Home, /crm, /about, /pricing, /donordock-demo, and the new /features/trust-and-security page all ship Organization `sameAs` arrays containing only Facebook, Instagram, LinkedIn, TikTok (pricing swaps TikTok for X/twitter). G2, Capterra, YouTube, and Crunchbase are still missing everywhere, despite G2 and Capterra being linked in body copy. This is a one-line fix per page that we have now flagged two months running.

---

## 2. Re-Verification of May's Two Open Blockers

| Item | May status | June status | Change |
|---|---|---|---|
| **Free-trial CTA (any page)** | 0 functional instances; all CTAs "Schedule a Demo" | **0 functional instances.** New `Start-for-Free-Button` / `start-14-day-trial-cta` DOM hooks exist but all render "Schedule a Demo" and link to `/donordock-demo`. Pricing "signup link" is a manual sales action ("we can send you a signup link directly"), not self-serve. | **No change** (scaffolding added, not shipped) |
| **G2 + Capterra in Organization `sameAs`** | Missing (social-only) | **Still missing.** All `sameAs` arrays remain social-only across all 7 schema-bearing pages checked. | **No change** |

Both blockers carry forward to July with the same priority.

---

## 3. SaaS Vertical Signals — Checklist

| Signal | Status | Δ vs May | Notes |
|---|---|---|---|
| SoftwareApplication JSON-LD on homepage | Yes | — | name, applicationCategory, featureList, AggregateRating 4.8/200, Organization provider w/ sameAs. |
| SoftwareApplication on /pricing | Yes (best on site, ~92/100) | — | applicationSubCategory "Nonprofit CRM", description, audience, eligibleCustomerType Nonprofit, UnitPriceSpecification, FAQPage, BreadcrumbList. Template page. |
| SoftwareApplication on /crm | Partial → improved | **+** | **Now carries `applicationSubCategory: "CRM Software"`** (was missing). Still no description/screenshot. Subcategory should read "Nonprofit CRM" to match pricing. |
| SoftwareApplication on /features-overview | Stub | — | Offer + SoftwareApplication + WebPage only. No description, rating, audience, screenshot. |
| SoftwareApplication on /tour | **Missing** | — | **0 JSON-LD blocks.** Unchanged regression — high-intent product page still ships no schema. |
| SoftwareApplication on /partners | **Missing** | — | **0 JSON-LD blocks.** Unchanged. |
| SoftwareApplication on /features/trust-and-security | Yes (NEW page) | **NEW** | New page carries SoftwareApplication + AggregateRating + BreadcrumbList + Offer + Organization. Good foundation; missing `hasCredential` for SOC 2 (see §4). |
| `screenshot` field | Missing everywhere | — | Still absent. Critical for AI visual citations. |
| `softwareVersion` / changelog | Missing / partial | — | No `/changelog`; an `/articles/donordock-latest-feature-releases` post exists but isn't schema'd as a release feed. |
| Homepage Offer with explicit `price` | No | — | Home Offer still `{availability: InStock, priceCurrency: USD}` with **no price**. Pricing has `price: 500.00`. Add price to home Offer. |
| Multiple Offers (per plan) | Missing | — | Single Offer only; consider OfferCatalog for tiers. |
| FAQPage on pricing | Yes | — | Strong. |
| FAQPage on home / features / compare | Missing | — | Still absent everywhere except pricing. |
| BreadcrumbList | /pricing + /features/trust-and-security | **+** | New page added breadcrumbs. Still not site-wide. |
| Organization `sameAs` | Social-only | — | **G2, Capterra, YouTube, Crunchbase still missing.** (Re-verify item.) |
| ContactPoint | Yes (sales only) | — | Add a "customer support" ContactPoint. |
| AggregateRating consistency | 4.8 / 200 across 6+ schemas | — | Consistent. Document the source if it's a G2+Capterra roll-up. |
| Comparison pages (9 live) | Yes | — | Count unchanged. |
| Pricing transparency | Strong | — | $40/mo entry, $60/mo Pro, $500/mo enterprise, money-back, 1% platform fee disclosed. |
| Free trial CTA | **Missing site-wide** | — | Re-verify item. Scaffolding exists; nothing functional. |
| Integrations page | Yes (/integrations) | — | Schema still a stub (Offer + SoftwareApplication + WebPage). |
| Trust badge / SOC 2 surfacing | Improved | **+** | New `/features/trust-and-security` page surfaces SOC 2. Still no `hasCredential` schema and not in footer site-wide. |

**Score: 65/100** (May 64). Net +1 — the new trust-security page and /crm subcategory are real but minor.

---

## 4. Nonprofit Vertical Signals — Checklist

| Signal | Status | Δ | Notes |
|---|---|---|---|
| Audience schema (`audienceType` = nonprofits) | Yes on /pricing + /donordock-demo | — | Still not on home, /crm, /features-overview, /compare/*. |
| `eligibleCustomerType: Nonprofit` on Offer | Yes on /pricing | — | Replicate site-wide. |
| 501(c)(3) language on home | Missing | — | Still only surfaced on /pricing. Put it in the hero. |
| Nonprofit-specific Review schema | Missing | — | No per-reviewer Review blocks with nonprofit name / mission area. |
| Nonprofit-native integrations called out | Partial | — | Still generic SaaS only (QuickBooks, Stripe, Mailchimp, Zapier, Salesforce, Slack). No DAFs, Benevity, Double the Donation, Classy, Bonterra migration. |
| Money-back guarantee | Yes (/pricing) | — | Surface on home + comparison pages. |
| Data security for donor data | **Improved** | **+** | Dedicated `/features/trust-and-security` page now live with SOC 2 mentions. **Add Organization `hasCredential` (EducationalOccupationalCredential / Certification) for SOC 2 Type II** and link from footer site-wide. |
| GDPR / CCPA / PIPEDA | Not detected | — | Still no explicit compliance language. |
| Industry vertical pages (faith-based, animal welfare, food bank, etc.) | Not detected | — | No `/for/*` pages in sitemap. Major content gap persists. |
| Free nonprofit resources | Yes (academy, articles, podcast, bootcamp) | — | Strong. |
| Convince-your-team / board kit | Yes (/convince-your-team) | — | Promote from pricing + comparison pages. |
| IRS-compliant receipts as SEO signal | Not surfaced | — | Add as featureList item + dedicated page. |

**Score: 59/100** (May 58). Net +1 — driven entirely by the new trust-and-security page.

---

## 5. Comparison / Competitor Page Coverage

**Live comparison pages: 9** (unchanged from May): bloomerang, donorperfect, etapestry, little-green-light, neon-crm, network-for-good, salsa-crm-engage, givebutter, spreadsheets, plus the `/compare` hub.

**Still missing (high-priority):** Kindful, Salesforce NPSP, Virtuous, Keela, Donorbox, Funraise, CiviCRM, Aplos, Sumac, Raiser's Edge/Blackbaud. No `/migrate/*` landing pages. No "Best donor management software for small nonprofits 2026" pillar.

**Schema gaps on existing comparison pages (re-checked /compare/bloomerang-vs-donordock):**
- JSON-LD block present but **failed strict parse** (malformed/over-escaped) — the parser extracted 0 typed entities even though "bloomerang" appears in the raw block. This is worse than May's "competitor not named" note: the markup may not be valid to crawlers at all. **Validate this block in Google Rich Results Test.**
- **No FAQPage** (0 instances) — still missing the "is X better than Y" PAA capture.
- No ComparisonTable / ItemList of feature differences, no switcher Review schema, no BreadcrumbList, no switcher-specific migration CTA.

---

## 6. Review Platform Presence

| Platform | Linked from site | In `sameAs` | June action |
|---|---|---|---|
| **G2** | Yes (body copy) | **No** | Add `https://www.g2.com/products/donordock` to Organization sameAs. **(Re-verify item — still open.)** |
| **Capterra** | Yes (body copy) | **No** | Add Capterra URL to sameAs. **(Re-verify item — still open.)** |
| **YouTube** | Likely | No | Add channel URL to sameAs. |
| **Software Advice / GetApp** | Unknown | No | Claim + add (shared Gartner Digital Markets parent with Capterra). |
| **TechSoup** (nonprofit-specific) | Not detected | No | **Highest-value nonprofit directory.** Pursue listing. |
| **Crunchbase** | Not detected | No | Add for entity authority. |

**Bottom line unchanged:** sameAs is a social-only array. The single highest-leverage, lowest-effort fix on this whole audit — adding 2 URLs to a JSON-LD array — is now two audits old and still not done.

---

## 7. Top Vertical Actions (priority order)

1. **Ship OR strip the free-trial scaffolding.** The DOM already contains `Start-for-Free-Button` and `start-14-day-trial-cta` hooks. Either wire a real self-serve trial/sandbox to them and relabel the buttons "Start Free Trial," or remove the misleading naming. Today it's the worst of both worlds — dead code that signals intent without delivering it. A real trial is still the #1 conversion + long-tail-search unlock.
2. **Add G2 + Capterra (+ YouTube, Crunchbase) to Organization `sameAs` on every schema-bearing page.** Two-minute fix, flagged twice, entity-authority impact. Do it this cycle.
3. **Fix the comparison-page JSON-LD.** The bloomerang block didn't parse — validate all 9 pages in Rich Results Test, then add: competitor SoftwareApplication entity, ItemList feature table, FAQPage, switcher Review, BreadcrumbList, migration CTA.
4. **Add `hasCredential` (SOC 2 Type II) to Organization schema** and surface a SOC 2 badge site-wide footer, anchored on the new `/features/trust-and-security` page.
5. **Standardize /pricing-quality SoftwareApplication schema** across home, /crm (fix subcategory to "Nonprofit CRM"), /features-overview, /tour, /partners, /integrations, /compare/*. Add `screenshot` fields. Add JSON-LD to /tour and /partners (still 0 blocks).
6. **Build the missing comparison + pillar pages** (Kindful, Salesforce NPSP, Virtuous, Keela, Donorbox, Funraise) and the "Best donor management software for small nonprofits 2026" ItemList pillar.
7. **Add Audience + 501(c)(3) signals** to home, /crm, /features-overview, /compare/*.
8. **Add FAQPage schema** to home, /features-overview, /crm, every comparison page.
9. **Build `/for/*` nonprofit-segment pages** (faith-based, animal welfare, food banks, education, health, arts).
10. **Add nonprofit-native integrations** (DAFs, Benevity, Double the Donation, Classy, Bonterra migration) to /integrations copy + schema.

---

## 8. Delta Summary — May → June

**Improved (+):**
- New page `/features/trust-and-security` live (SoftwareApplication + AggregateRating + BreadcrumbList + Offer + SOC 2 copy). Addresses May action #7 partially.
- `/crm` SoftwareApplication gained `applicationSubCategory: "CRM Software"` (was absent).
- BreadcrumbList now on 2 pages (was /pricing only).
- Sitemap grew 620 → 622 URLs.

**Unchanged (=) — carried-over blockers:**
- **Free-trial CTA: still 0 functional.** New CSS/ID hooks added but all render "Schedule a Demo" → `/donordock-demo`. **(Re-verify: confirmed still open.)**
- **G2 / Capterra in `sameAs`: still missing everywhere.** sameAs remains social-only. **(Re-verify: confirmed still open.)**
- Comparison pages still 9; competitor still not modeled as a typed entity.
- /tour and /partners still ship 0 JSON-LD.
- Homepage Offer still has no `price`.
- No `/for/*` vertical pages, no `/migrate/*`, no FAQPage outside /pricing, no nonprofit-native integrations, no `hasCredential` for SOC 2.

**Regressed (–):**
- /compare/bloomerang-vs-donordock JSON-LD **failed strict parse** in this run (raw block present, 0 typed entities extracted). May have been broken during recent edits — needs validation. Possibly always borderline; flagging as a risk either way.

---

## Quick Stats

- **Overall vertical score: 52/100** (SaaS 65, Nonprofit 59 — composite weighted down by trial/sameAs/comparison blockers). **Trend: +2 vs May (~50). Slow positive drift.**
- Pages audited: 10 live pages + comparison + sitemap.
- Sitemap URLs: 622 (was 620).
- Schema completeness — /pricing: ~92/100 (template, unchanged).
- Schema completeness — homepage: ~70/100.
- Schema completeness — /tour, /partners: ~15/100 (still WebPage-level / 0 JSON-LD).
- Comparison pages live: 9 (target 15+). Unchanged.
- **Free-trial CTA presence: 0 functional** (scaffolding hooks present, non-functional).
- "Schedule a Demo" / "Book Your Demo" CTAs: dominant (9+ across sampled pages).
- Review-platform links in `sameAs`: **0** (G2/Capterra in body copy only).
- Nonprofit-native integration partners called out: ~0.

---

## Appendix — Detected Schema Inventory (June)

| Page | JSON-LD blocks | Schema types | Δ |
|---|---|---|---|
| `/` (home) | 1 | SoftwareApplication, Organization, Offer, AggregateRating, ContactPoint, ImageObject, WebPage | — |
| `/pricing` | 1 | SoftwareApplication, Offer, UnitPriceSpecification, Audience, AggregateRating, Organization, FAQPage, BreadcrumbList, ListItem, Person, WebPage, WebSite | — |
| `/crm` | 1 | SoftwareApplication (+applicationSubCategory "CRM Software"), Offer, AggregateRating, ImageObject, Organization, WebPage | **+** |
| `/features-overview` | 1 | SoftwareApplication (stub), Offer, WebPage | — |
| `/tour` | **0** | none | — |
| `/donordock-demo` | 1 | SoftwareApplication, Service, Audience, Offer, ImageObject, Organization, AggregateRating, WebPage | — |
| `/integrations` | 1 | SoftwareApplication (stub), Offer, WebPage | — |
| `/partners` | **0** | none | — |
| `/about` | 1 | AboutPage, Organization, Person, AggregateRating, ContactPoint, ImageObject, SoftwareApplication, Offer | — |
| `/features/trust-and-security` | 1 | SoftwareApplication, AggregateRating, BreadcrumbList, Offer, Organization, ImageObject, ListItem, WebPage | **NEW** |
| `/compare/bloomerang-vs-donordock` | 1 (parse-fail) | block present, 0 typed entities extracted; "bloomerang" in raw text; no FAQPage | **–** |

All Organization `sameAs` arrays this run: Facebook, Instagram, LinkedIn, TikTok (pricing: + X/twitter, − TikTok). **No G2, Capterra, YouTube, Crunchbase on any page.**

---

*End of audit. Findings written to: `/tmp/dd-citations-runner/seo-brain/audits/2026-06-baseline/vertical.md`*
