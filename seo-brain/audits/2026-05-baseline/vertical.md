# Vertical SEO Audit — donordock.com

**Vertical:** SaaS + Nonprofit-Tech (Donor Management / Nonprofit CRM)
**Audit date:** 2026-05-04
**Scope:** SoftwareApplication schema, pricing transparency, trial/demo UX, comparison pages, nonprofit trust signals, review-platform presence, vertical keyword targeting.
**Auditor:** Vertical Auditor (claude-rank)

---

## 1. Executive Summary

- **Schema foundation is strong but inconsistent.** The `/pricing` page is best-in-class (rich SoftwareApplication with `applicationSubCategory: "Nonprofit CRM"`, audience targeting, FAQPage, BreadcrumbList, UnitPriceSpecification). The homepage is solid but missing `description`, `applicationSubCategory`, `screenshot`, and per-plan offers. `/tour` and `/partners` ship with **zero JSON-LD**, and `/features-overview` has only a stub. Standardize pricing-page-quality schema across every product page.
- **No free-trial offer surfaced anywhere — only "Schedule a Demo."** Every CTA on home, pricing, comparison, CRM, and features pages routes to a HubSpot demo booking. For a small-nonprofit ICP (often <$1M budget, no buying committee), the lack of a self-serve trial or freemium tier raises the activation bar and concedes long-tail "free donor management software" search to Givebutter/Donorbox. Add an explicit free-trial path or sandbox account, and surface it as a primary CTA.
- **Comparison coverage is excellent (9 vs-pages live) but conversion infrastructure is thin.** Pages rank against Bloomerang, DonorPerfect, Neon CRM, Little Green Light, Givebutter, Network for Good, Salsa, eTapestry, and spreadsheets — but they lack ComparisonTable / ItemList schema, individual reviewer schema for switcher quotes, and migration-specific CTAs ("free data migration from X"). Pages also reuse generic SoftwareApplication schema with no competitor named in JSON-LD, so AI search engines won't surface DonorDock as a direct alternative.

---

## 2. SaaS Vertical Signals — Checklist

| Signal | Status | Notes |
|---|---|---|
| SoftwareApplication JSON-LD on homepage | Yes | Has name, applicationCategory, featureList (10 items), AggregateRating 4.8/200, Organization provider with sameAs. |
| SoftwareApplication on /pricing | Yes (best on site) | Adds applicationSubCategory "Nonprofit CRM", description, audience, eligibleCustomerType: Nonprofit, UnitPriceSpecification. **Use this as the template for every product page.** |
| SoftwareApplication on /crm | Partial | Has Offer + AggregateRating but no description, no applicationSubCategory, no screenshot. |
| SoftwareApplication on /features-overview | Stub | Only name, category, OS, featureList. Missing description, rating, audience, screenshot, full Offer. |
| SoftwareApplication on /tour | Missing | Tour page has 1 JSON-LD block (likely WebPage only) — no SoftwareApplication. High-intent product page should not skip schema. |
| SoftwareApplication on /partners | Missing | Same gap. Add Organization + service schema at minimum. |
| `screenshot` field | Missing everywhere | Add 1–3 product screenshots per SoftwareApplication block. Critical for AI search visual citations. |
| `softwareVersion` | Missing | Helps with freshness signals; tie to changelog. |
| `releaseNotes` / changelog page | Not detected | Add `/changelog` or `/whats-new` with WebPage schema; link from footer. |
| Offer with explicit `price` | Yes on /pricing ($500/mo annual = $40/mo entry, $60/mo Pro) | Homepage Offer has currency + InStock but **no price**. Add price string to homepage Offer. |
| Multiple Offers (per plan) | Missing | Pricing schema only shows one "DonorDock ONE Plan" Offer; consider an OfferCatalog if there are tier variations. |
| FAQPage on pricing | Yes | Strong. |
| FAQPage on home / features | Missing | High-value addition for AI Overviews. |
| BreadcrumbList | Only on /pricing | Add site-wide. |
| Organization schema with sameAs | Yes | Facebook, Instagram, LinkedIn, TikTok. **Missing:** YouTube, X/Twitter, G2, Capterra, Crunchbase. |
| ContactPoint | Yes | Sales contact only. Add a "customer support" ContactPoint. |
| Course schema on /academy | Yes | Good — leverage for ICP authority. |
| AboutPage schema on /about | Yes | Good. |
| AggregateRating consistency | 4.8 / 200 reviews used in 4+ schemas | Verify the 200 count matches G2 + Capterra public total; if it's a roll-up, document the source in a `reviewedBy` field. |
| HowTo schema on onboarding/setup | Missing | Add to /onboarding and any "how to import" articles. |
| API documentation page | Not detected | If API exists, add `/api` page with `APIReference` schema. |
| Comparison pages (9 live) | Yes | bloomerang, donorperfect, etapestry, little-green-light, neon-crm, network-for-good, salsa, givebutter, spreadsheets. |
| Pricing transparency on /pricing | Strong | $40/mo entry, $60/mo Pro, $500/mo enterprise, money-back, "Cancel anytime", 1% platform fee disclosed. |
| Free trial CTA | **Missing site-wide** | Every CTA reads "Schedule a Demo." No "Start free trial" or "Try it free" anywhere. |
| Demo booking UX | HubSpot Meeting embed on /donordock-demo | Functional. Add availability schema (`Reservation` or `Service` with `availableChannel`). |
| Integration logos / page | Yes (/integrations) | Mailchimp, QuickBooks, Stripe, Zapier (77 mentions), Salesforce, Outlook, Gmail, Slack, Asana visible. Schema is stub — add `featureList` of all integrations and link partners. |
| Trust badges (SOC 2, etc.) | Partial | "SOC 2 Type II certified" on /pricing and /crm. Not surfaced on home, features, or comparison pages. Add SOC 2 badge prominently above-the-fold. |

**Score: 64/100.** Foundation is real; execution is patchy. Standardize schema and surface trial/security signals globally.

---

## 3. Nonprofit Vertical Signals — Checklist

| Signal | Status | Notes |
|---|---|---|
| Audience schema with `audienceType` = nonprofits | Yes on /pricing | "Nonprofit organizations, 501(c)(3) charities, small to mid-size nonprofits" — excellent. **Add to home, /crm, /features-overview, /compare/***. |
| `eligibleCustomerType: Nonprofit` on Offer | Yes on /pricing | Good. Replicate site-wide. |
| 501(c)(3) language on home | Missing | Only 1 mention site-wide (on /pricing). Surface "built for 501(c)(3) organizations" in hero copy. |
| "Built for nonprofits" / "by nonprofit founders" | Not detected as standalone phrase | "Trusted by 7,200" appears on /about — strong number, but no founder/origin story tied to nonprofit roots in schema or hero. |
| Nonprofit-specific testimonials | Implicit (200 reviews, 7,200 customers) | Add `Review` schema with reviewer's nonprofit name, mission area (animal welfare, food bank, faith-based, etc.) for AI citation richness. |
| Nonprofit-tech integrations called out | Partial | QuickBooks, Stripe, Mailchimp, Zapier exist. Missing nonprofit-native: **DAFs (Donor-Advised Funds), Benevity, Bonterra/Network for Good migration, Double the Donation matching, GoFundMe Charity, Classy import**. Add a nonprofit-tech-specific integration cluster page. |
| Pricing for small nonprofits | Strong | $40/mo entry tier is competitive for <$500K budget orgs. Make this the headline above-the-fold of /pricing. |
| Free tier or trial for under-resourced orgs | Missing | Many competitors (Givebutter free, Donorbox free, Little Green Light $39/mo) are perceived as cheaper. Counter with a transparent free trial. |
| Money-back guarantee | Yes (90-day money-back referenced on /pricing) | Surface on home + every comparison page. |
| Nonprofit founder / mission narrative | On /about | Good. Promote founder story to home + comparison pages — buyers in this segment buy from people. |
| Data security for donor data | SOC 2 Type II noted | Add a `/security` or `/trust` page with full schema (Organization with `hasCredential` for SOC 2). |
| GDPR / CCPA / Canadian PIPEDA | Not detected | Many small US nonprofits also serve Canadian/UK donors. Add explicit compliance language. |
| Industry-specific pages (faith-based, animal welfare, food bank, education, etc.) | Not detected in sitemap | Major content gap. Each is a high-intent vertical search cluster. |
| Free nonprofit resources (templates, guides) | Yes (academy, articles, podcast, smart-steward-method, fundraising-bootcamp) | Strong. Tag heavily with audience schema. |
| Convince-your-team / board approval kit | Yes (/convince-your-team) | Excellent — rare and high-converting. Promote it from pricing and comparison pages. |
| Nonprofit-specific keywords in H1s | Yes | "Donor Management to Donor Momentum" — on-brand but **doesn't include the search phrase "donor management software for small nonprofits"**. Optimize one H1 or H2 per page for the literal query. |
| Receipt / IRS-compliant donation acknowledgments | Mentioned in product but not surfaced for SEO | Add "IRS-compliant tax receipts" as a featureList item in schema and a dedicated page. |
| Grant management / 990 reporting | Not detected | Adjacent search demand; even a single article would capture it. |

**Score: 58/100.** ICP fit is real, but the site under-signals "nonprofit-built" status to crawlers and AI engines.

---

## 4. Comparison / Competitor Page Coverage

**Live comparison pages (9):**
1. `/compare/bloomerang-vs-donordock`
2. `/compare/donorperfect-vs-donordock`
3. `/compare/etapestry-vs-donordock`
4. `/compare/little-green-light-vs-donordock`
5. `/compare/neon-crm-vs-donordock`
6. `/compare/network-for-good-vs-donordock`
7. `/compare/salsa-crm-engage-vs-donordock`
8. `/compare/givebutter-vs-donordock`
9. `/compare/spreadsheets-vs-donordock`
10. `/compare` (hub)

**Coverage gaps (high-priority competitors missing):**
- **Kindful** (acquired by Bloomerang but still ranks for kindful queries / migration intent)
- **Salesforce Nonprofit Cloud / NPSP** (high-volume search, enterprise-leakage upmarket)
- **Virtuous CRM** (direct mid-market competitor, growing share of voice)
- **Keela** (nonprofit-CRM, AI-positioned, similar SMB ICP)
- **Donorbox** (giving-platform-first, a common point-of-comparison for budget-conscious buyers)
- **Funraise** (mentioned on home but no /compare page)
- **CiviCRM** (open-source; converts skeptical buyers researching free alternatives)
- **Aplos** (nonprofit accounting + CRM bundle)
- **Sumac** (Canadian/UK heavy)
- **Raiser's Edge NXT / Blackbaud** (legacy enterprise; capture downmarket migration)

**Schema gaps on existing comparison pages:**
- Pages use a generic SoftwareApplication block — **the competitor is never named in JSON-LD**. Add a second SoftwareApplication entity for the competitor (or use ItemList of two SoftwareApplications) and a `subjectOf` linking to the comparison.
- No **ComparisonTable / Table** schema or `ItemList` of feature differences. AI engines summarize tables natively when marked up.
- No FAQPage on comparison pages (would capture "is bloomerang or donordock better for…" type queries).
- No individual `Review` blocks with switcher testimonials ("we moved from Bloomerang to DonorDock because…"). These convert at 2–3x of generic reviews on bottom-of-funnel pages.
- No BreadcrumbList.
- CTAs are all "Schedule a Demo" — add a switcher-specific CTA: "Get a free Bloomerang → DonorDock migration plan."

**Recommended new comparison content:**
- One pillar **"Best donor management software for small nonprofits 2026"** page with ItemList schema covering 8–10 competitors and DonorDock anchored as #1 with rationale.
- Migration-specific landing pages: `/migrate/bloomerang-to-donordock`, `/migrate/donorperfect-to-donordock`, etc. (different intent than `/compare`).

---

## 5. Review Platform Presence

| Platform | Listed | Linked from site | Schema reference | Action |
|---|---|---|---|---|
| **G2** | Yes (g2.com/products/donordock/reviews) | Home, pricing, crm, about | Mentioned in featureList copy; not in `sameAs` | Add `https://www.g2.com/products/donordock` to Organization sameAs array. |
| **Capterra** | Yes (capterra.com/p/184187/DonorDock/) | Home, crm, about | Not in sameAs | Add Capterra URL to sameAs. |
| **Software Advice** | Status unknown — no outbound link detected | Not linked | No schema | Claim listing if not already; add to sameAs. Software Advice and GetApp share Capterra's parent (Gartner Digital Markets), so a single submission may populate all three. |
| **GetApp** | Status unknown | Not linked | No schema | Same as above. |
| **TrustRadius** | Not detected | Not linked | No schema | Lower priority for SMB nonprofit; nice-to-have. |
| **TechSoup** (nonprofit-specific) | Not detected on site | Not linked | No schema | **High priority.** TechSoup is the single most-trafficked nonprofit-software directory. Validation here is worth more than another generic SaaS review platform. |
| **Idealware / Nonprofit Tech for Good** | Not detected | Not linked | No schema | Pitch for inclusion in their annual donor management roundups. |
| **NTEN community** | Not detected | Not linked | No schema | Membership + thought-leadership presence drives high-quality citations. |
| **Capterra Shortlist / G2 Leader badges** | Not detected on site | Not linked | No schema | If awarded, surface badges above the fold + add `Award` schema to Organization. |

**Bottom line:** G2 and Capterra are linked; everything else is unclaimed or under-leveraged. Nonprofit-specific directories (TechSoup, Idealware) move the needle more than additional generic SaaS sites for this ICP.

---

## 6. Top 10 Vertical-Specific Actions (priority order)

1. **Add an explicit free-trial CTA site-wide.** Either a 14-day or 30-day no-credit-card trial, or a sandbox account. Surface it as a co-equal primary CTA next to "Schedule a Demo." Without it, DonorDock concedes the "free donor management software" long-tail and bottom-funnel comparison traffic. Also captures the buyer who clicks "free trial" before they're willing to talk to a human — that's most small-nonprofit EDs.

2. **Standardize the /pricing-quality SoftwareApplication schema across home, /crm, /features-overview, /tour, /partners, /integrations, and every /compare/* page.** The pricing schema is best-in-class (description, applicationSubCategory: "Nonprofit CRM", audience, eligibleCustomerType: Nonprofit, UnitPriceSpecification, FAQPage). Use it as the template. Add `screenshot` field with 2–3 product screens.

3. **Add Audience + 501(c)(3) signals to home, /crm, /features-overview, and all /compare/* pages.** The phrase "for 501(c)(3) nonprofits" should appear in H1 or hero subhead on home. Add Audience schema with audienceType "Nonprofit organizations, 501(c)(3) charities" everywhere.

4. **Upgrade comparison pages.** Add (a) a second SoftwareApplication entity naming the competitor, (b) ItemList or Table schema for the feature comparison grid, (c) FAQPage with "Is X better than Y for small nonprofits?" Q&As, (d) Review schema for at least one switcher testimonial per page, (e) a switcher-specific CTA: "Free migration from Bloomerang."

5. **Build the missing comparison pages** — at minimum: Kindful, Salesforce NPSP, Virtuous, Keela, Donorbox, Funraise. Plus a pillar "Best donor management software for small nonprofits 2026" with full ItemList schema. This is the single highest-ROI content investment for AI Overviews and ChatGPT citations.

6. **Add review platforms to Organization `sameAs`** — G2, Capterra, plus claim Software Advice / GetApp / TechSoup. The current sameAs only covers social. Search engines and AI use sameAs to confirm entity authority.

7. **Surface SOC 2 Type II + security trust signals globally.** Currently only on /pricing and /crm. Add a SOC 2 badge in the footer site-wide, create a `/security` or `/trust` page with `hasCredential` schema, and add to home hero. Donor-data trust is a buying-committee blocker.

8. **Add FAQPage schema to home, /features-overview, /crm, and every comparison page.** Pricing has it; nothing else does. Each FAQPage should target a specific People-Also-Ask cluster ("how much does donor management software cost," "is donordock free," "what's the best CRM for a small nonprofit," etc.).

9. **Build vertical sub-pages for nonprofit segments**: `/for/faith-based`, `/for/animal-welfare`, `/for/food-banks`, `/for/education-nonprofits`, `/for/health-charities`, `/for/arts-culture`. Each with audience-specific Audience schema, testimonial Review schema from that segment, and tailored featureList. These are clean ranking opportunities with low competition and high intent.

10. **Add nonprofit-native integrations to the integrations page and schema** — DAFs (Fidelity Charitable, Schwab, Vanguard), Benevity, Double the Donation, Bonterra migration, Classy import, GoFundMe Charity, Givebutter export. Several are likely already supported via Zapier; surface them explicitly. AI engines listing "best donor CRM with DAF support" need to see this in your structured data.

---

## Quick Stats

- **Pages audited:** 10 (home, pricing, crm, features-overview, tour, donordock-demo, integrations, partners, about, academy) + comparison sample
- **Sitemap URLs:** 620
- **Schema completeness — pricing page:** ~92/100
- **Schema completeness — homepage:** ~70/100
- **Schema completeness — tour / partners:** ~15/100 (WebPage only)
- **Comparison pages live:** 9 (target: 15+)
- **Free-trial CTA presence:** 0 instances detected
- **"Schedule a Demo" CTA presence:** dominant across all pages
- **Review-platform outbound links:** 2 (G2, Capterra)
- **Nonprofit-specific integration partners called out:** ~0 (all integrations are generic SaaS — QuickBooks, Stripe, Mailchimp, Zapier, Salesforce, Slack, Asana)

---

## Appendix — Detected Schema Inventory

| Page | JSON-LD blocks | Schema types |
|---|---|---|
| `/` (home) | 2 | SoftwareApplication, Organization, Offer, AggregateRating, ContactPoint, ImageObject, WebPage |
| `/pricing` | 3+ | SoftwareApplication, Offer, UnitPriceSpecification, Audience, AggregateRating, Organization, FAQPage (Question/Answer), BreadcrumbList, ListItem, Person, WebPage, WebSite |
| `/crm` | 1 | SoftwareApplication, Offer, AggregateRating, ImageObject, Organization, WebPage |
| `/features-overview` | 1 | SoftwareApplication (stub), Offer, WebPage |
| `/tour` | 1 | WebPage only — **no SoftwareApplication** |
| `/donordock-demo` | 1 | SoftwareApplication, Service, Audience, Offer, ImageObject, Organization, AggregateRating, WebPage |
| `/integrations` | 1 | SoftwareApplication (stub), Offer, WebPage |
| `/partners` | 1 | WebPage only — **no SoftwareApplication / Service** |
| `/about` | 1 | AboutPage, Organization, Person, AggregateRating, ContactPoint, ImageObject, SoftwareApplication, Offer |
| `/academy` | 1 | Course, CourseInstance, Schedule, Organization, ImageObject, WebPage |
| `/compare/*` | 1 | SoftwareApplication, AggregateRating, Offer, Organization, ItemList, ListItem, ImageObject, WebPage — **competitor not named in schema** |

---

*End of audit. Findings written to: `/tmp/dd-citations-runner/seo-brain/audits/2026-05-baseline/vertical.md`*
