# Schema Coverage Baseline — donordock.com

**Audit date:** 2026-04-22
**Audited by:** claude-rank Schema Auditor
**Target:** https://donordock.com (Webflow-hosted, 617 URLs in sitemap.xml)
**Project type:** SaaS (nonprofit CRM) + publisher (279 articles) + compare-heavy competitive portfolio
**Method:** Direct HTTPS fetch with redirect-follow (`www.donordock.com`), JSON-LD extracted from each page's rendered HTML, validated as strict JSON and against Google's Rich Results required-field spec.
**Pages sampled:** 35 unique URLs across every major template (home, pricing, FAQ, product, compare, articles, solution, feature, integration, success-story, team, podcast index, tour, contact, careers, events, partners, demo, academy, bootcamp, customer-success, about).

---

## 1. Executive Summary

DonorDock has partial schema coverage with four structural problems that are actively costing rich-result eligibility today:

1. **Six of nine compare pages ship invalid JSON.** Trailing commas, a missing object literal, and a stray closing bracket cause `JSON.parse` to fail. When a JSON-LD script throws on parse, Google discards every schema in that script — so the embedded `FAQPage`, `SoftwareApplication`, `Review`, and (on /compare/network-for-good) `BreadcrumbList` are all invisible to Search today. This is the single highest-leverage fix in the audit.
2. **/pricing ships invalid JSON.** The SoftwareApplication offers array has a second, empty object (`},\n }\n]`) that breaks parsing. Google sees nothing for /pricing — no SoftwareApplication, no aggregateRating, no offer.
3. **Every article has two conflicting BlogPosting scripts** — one machine-generated (CMS), one hand-added. The two blocks disagree on datePublished format (ISO 8601 vs "Mar 25, 2026"), author detail, and image shape. Google will pick one non-deterministically. This also puts every article author's Person schema at risk: the Rob Burke and Noah Barnett sameAs arrays contain three empty strings (`"",""","` "), which fails schema.org URL validation.
4. **/faq nests `@graph` inside `@graph`.** This non-standard structure is a known Rich Results Test failure pattern — the outer wrapper has no `@type`, so Google treats the node as ambiguous. The underlying FAQPage has 114 questions that are being partially ignored.

Beyond these bugs, the site is missing seven schemas that directly map to rich results nonprofits search for:

- No `Organization` root entity anywhere (only nested inside `about.provider` — Google cannot use it for the Knowledge Panel)
- No `WebSite` + `SearchAction` (blocks sitelinks search box)
- No `BreadcrumbList` on 8 of 9 compare pages, 10 of 10 solution pages, pricing, FAQ, homepage, or any product page (/crm, /donor-outreach, /online-giving)
- No `PodcastSeries` / `PodcastEpisode` schema on the two podcast hubs
- No `VideoObject` despite embedded YouTube on both podcast pages (2 videos each), Wistia on /convince-your-team (16 videos), and embedded video on /project-management (36 refs), /donor-outreach (12 refs), /otto (12 refs), /crm (8 refs)
- No `HowTo` on the step-based articles that naturally fit it (Q4 checklist, imposter-syndrome 90-day plan, data-migration guides)
- No `speakable` property on any article or FAQ — meaningful gap for voice assistants / Google Assistant read-aloud

Three pages ship zero JSON-LD at all: `/tour`, `/contact`, `/careers`.

**Overall score:** 42/100. Good bones — the product pages use `SoftwareApplication` correctly with `aggregateRating`, the FAQ page content is excellent source material, the article template is nearly right — but the parse errors and duplicates cut effective coverage roughly in half.

---

## 2. Schema Coverage Map (per-page inventory)

Columns: file path, current JSON-LD `@type`s, notes. `BROKEN` = JSON parse error, all schema on that page is invisible to Google. `DUP` = duplicate of same `@type` on same page.

### Root / marketing templates

| Page | Current schemas | Status |
|---|---|---|
| `/` (home) | `WebPage` → `about: SoftwareApplication` (featureList, aggregateRating 4.8/200, Offer, provider.Organization) | OK but incomplete — no standalone Organization, no WebSite, no BreadcrumbList |
| `/pricing` | `WebPage` → `about: SoftwareApplication` with offers list + aggregateRating | **BROKEN** — extra `}` inside offers array (line 30). Entire block invisible to Google. |
| `/faq` | `@graph` → `@graph` → `[FAQPage (114 Q), WebPage]` | **BROKEN PATTERN** — nested @graph. Outer wrapper has no @type. |
| `/about` | `AboutPage` → `about: SoftwareApplication` with founder[Matt, Andrew], aggregateRating | OK but AboutPage is weak — should host `Organization` with `foundingDate`, `numberOfEmployees`, `address`, `sameAs` |
| `/contact` | none | **ZERO SCHEMA** — needs ContactPage + Organization with address/telephone |
| `/tour` | none | **ZERO SCHEMA** — missing VideoObject, missing WebPage |
| `/careers` | none | **ZERO SCHEMA** — ideal for JobPosting aggregate or Organization.employmentCategory |
| `/webinars-events` | `CollectionPage` → `hasPart[Event, Event, ...]` with startDate, VirtualLocation, performer | OK — one of the cleaner schemas on the site |
| `/articles` (hub) | `CollectionPage` → `hasPart[BlogPosting, BlogPosting, ...]` | OK for hub; entries are listing-only (no full BlogPosting payload) |
| `/compare` (hub) | `WebPage` → `about: SoftwareApplication` | OK — no ItemList of comparison targets (missed opportunity) |
| `/integrations` (hub) | `WebPage` → `about: SoftwareApplication` | OK — no ItemList of integrations |
| `/features-overview` | `WebPage` → `about: SoftwareApplication` | OK — no ItemList of features |
| `/solutions-overview` | none | **ZERO SCHEMA** |
| `/customer-success` | `CollectionPage` | **BROKEN** — Webflow anti-flicker `<style>` injected inside JSON-LD block, breaks parse |
| `/otto` | `WebPage` → `about: SoftwareApplication` | OK; 12 video refs suggest VideoObject needed |
| `/project-management` | `WebPage` → `about: SoftwareApplication` | 36 video refs — VideoObject missing |
| `/smart-steward-method` | `WebPage` → `about: SoftwareApplication` | OK for now |
| `/partners` | none | **ZERO SCHEMA** |
| `/donordock-demo` | `WebPage` → `about: SoftwareApplication` | OK — should be WebPage with `potentialAction: ReserveAction` |
| `/academy` | `WebPage` | Bare — missing `Course` / `EducationalOccupationalProgram` |
| `/fundraising-bootcamp` | `WebPage` | Bare — missing `Course` |
| `/beyond-the-donation-podcast` | `WebPage` | Missing `PodcastSeries`, missing VideoObject (2 YouTube embeds) |
| `/the-focused-fundraiser-podcast` | `WebPage` | Missing `PodcastSeries`, missing VideoObject (2 YouTube embeds) |
| `/convince-your-team` | none | **ZERO SCHEMA** — 16 Wistia embeds, no VideoObject |

### Product pages

| Page | Current | Status |
|---|---|---|
| `/crm` | `WebPage` → `about: SoftwareApplication` (subcategory CRM, 13 features, `reviewCount` 200) | Has rating quirk: uses `reviewCount` — on other pages uses `ratingCount`. Pick one consistently. No BreadcrumbList. No VideoObject despite 8 video refs. |
| `/donor-outreach` | `WebPage` → `about: SoftwareApplication` (8 features, aggregateRating 4/6, Review[] with Patrick K) | Has review[] (good). But aggregateRating 4/6 is inconsistent with 4.8/200 elsewhere. No BreadcrumbList. 12 video refs. |
| `/online-giving` | `WebPage` → `about: SoftwareApplication` (12 features, aggregateRating 4.8/200) | OK — no BreadcrumbList |

### Compare pages (9 total, 6 BROKEN)

| Page | Parse status | Schemas in source | Notes |
|---|---|---|---|
| `/compare/bloomerang-vs-donordock` | **BROKEN** trailing comma L35 | `WebPage`, `SoftwareApplication`, `mainEntity: ItemList` | H1 is brand-neutral ("The Difference Between Retention Scores & Relationship Growth") — missing competitor comparison anchor |
| `/compare/donorperfect-vs-donordock` | **BROKEN** trailing comma L22 | `WebPage`, `SoftwareApplication`, `Review` | No FAQPage in source |
| `/compare/etapestry-vs-donordock` | **BROKEN** missing comma L21 | `WebPage`, `SoftwareApplication`, `FAQPage` (5 Q), `BreadcrumbList` | — |
| `/compare/givebutter-vs-donordock` | OK | `WebPage`, `SoftwareApplication`, `mainEntity: ItemList` | No FAQPage — should have one |
| `/compare/little-green-light-vs-donordock` | **BROKEN** extra data L69 | `WebPage`, `SoftwareApplication`, `Review`, `FAQPage` (5 Q) | **H1 BUG**: "Network for Good vs DonorDock" — wrong competitor |
| `/compare/neon-crm-vs-donordock` | **BROKEN** trailing comma L23 | `WebPage`, `SoftwareApplication`, `Review`, `FAQPage` (3 Q) | **H1 BUG**: "Network for Good vs DonorDock" — wrong competitor |
| `/compare/network-for-good-vs-donordock` | **BROKEN** trailing comma L23 | `WebPage`, `SoftwareApplication`, `Review`, `FAQPage` (4 Q), `BreadcrumbList` | Only compare page with BreadcrumbList |
| `/compare/salsa-crm-engage-vs-donordock` | **BROKEN** trailing comma L13 | `WebPage`, `SoftwareApplication`, `Review` | No FAQPage |
| `/compare/spreadsheets-vs-donordock` | OK | `WebPage`, `SoftwareApplication`, `Review`, `FAQPage` (7 Q) | Only compare page that validates cleanly AND has FAQ |

### Solution pages (10 total)

All 10 use the same template: `WebPage → about: SoftwareApplication`, `mainEntity`, `dateModified`, `datePublished`. No BreadcrumbList on any. No HowTo despite how-to content (donor-retention, annual-fund, board-reporting). Sampled: `/solution/annual-fund`, `/solution/donor-retention`, `/solution/major-gifts`, `/solution/team-collaboration` — all identical pattern.

### Feature pages (61 total)

Sampled `/features/accept-recurring-gifts` and `/features/ai-features-for-email`. Both use `WebPage → about: SoftwareApplication` with `@id`, `breadcrumb` (BreadcrumbList present), `publisher`. **Feature pages are the best-structured template on the site.**

### Integration pages (59 total)

Sampled `/integrations/airtable`, `/integrations/mailchimp`, `/integrations/quickbooks-online`, `/integrations/zapier`. All use `WebPage → about: SoftwareApplication`, `breadcrumb` (BreadcrumbList present), `publisher`. Good. Could be upgraded to `CreativeWork` with `isPartOf` referencing DonorDock SoftwareApplication.

### Article pages (279 total)

Every article has **two BlogPosting scripts**. Sampled 5 articles — all the same pattern:

- Block 1 (CMS-injected): full shape — headline, image.ImageObject, author.Person with jobTitle+image+email+sameAs, publisher, datePublished ISO, dateModified ISO, mainEntityOfPage (empty @id), keywords, inLanguage.
- Block 2 (hand/Webflow-injected): reduced shape — headline, image string, author.Person with only name+url, publisher, datePublished "Mar 25, 2026" format.

**Duplicates confirmed:** `articles_best-nonprofit-crm`, `articles_from-imposter-syndrome`, `articles_end-of-year-success`, `articles_how-to-calculate-nonprofit-sroi`, `articles_how-to-write-nonprofit-about-page-donor-hero`. Author Person blocks include empty-string sameAs entries for both Rob Burke and Noah Barnett (`["https://linkedin.com/...", "", "", ""]`).

### Team pages (36 total)

Sampled `/team/noah-barnett` and `/team/matt-bitzegaio`. **Zero JSON-LD.** These are ideal `Person` / `ProfilePage` schema targets.

### Success story pages (14 total)

Sampled `/success-stories/family-programs-hawaii`, `/success-stories/cancergrace`. Both use `CollectionPage` with `about: Organization`. **Wrong type** — these are case studies / customer testimonials and should be `Article` with `about: NonprofitOrganization` (the customer) plus `Review` with `itemReviewed: SoftwareApplication` (DonorDock). Current schema provides no rich-result benefit.

---

## 3. Validation Errors (Google Rich Results Test predictions)

Every error below was reproduced by running the raw JSON-LD through `json.loads()` — Google's parser uses a JSON-spec strict parser with the same result.

### Category A — JSON syntax errors (schema is 100% invisible to Google)

| Page | Exact error | Location | Rich Result impact |
|---|---|---|---|
| `/pricing` | `Expecting value: line 30 column 7` — empty `{}` after offer | line 30 | No SoftwareApplication, no Offer, no aggregateRating visible |
| `/compare/bloomerang-vs-donordock` | Illegal trailing comma before end of array | line 35 col 27 | No SoftwareApplication, no featureList |
| `/compare/donorperfect-vs-donordock` | Illegal trailing comma before end of object | line 22 col 24 | No SoftwareApplication, no Review |
| `/compare/etapestry-vs-donordock` | Expecting `,` delimiter | line 21 col 9 | No FAQPage (5 Q), no BreadcrumbList, no SoftwareApplication |
| `/compare/little-green-light-vs-donordock` | Extra data after JSON | line 69 col 4 | No FAQPage (5 Q), no Review, no SoftwareApplication |
| `/compare/neon-crm-vs-donordock` | Illegal trailing comma before end of object | line 23 col 24 | No FAQPage (3 Q), no Review, no SoftwareApplication |
| `/compare/network-for-good-vs-donordock` | Illegal trailing comma before end of object | line 23 col 24 | No FAQPage (4 Q), no BreadcrumbList, no Review, no SoftwareApplication |
| `/compare/salsa-crm-engage-vs-donordock` | Illegal trailing comma | line 13 col 31 | No SoftwareApplication, no Review |
| `/customer-success` | Invalid control character (HTML `<style>` inside JSON) | line 157 | No CollectionPage, no hasPart list of stories |

### Category B — Structural / non-standard schema that Google may flag

| Page | Issue | Likely Rich Results Test result |
|---|---|---|
| `/faq` | Triple-nested: outer `{"@graph":[{"@context":"...","@graph":[FAQPage, WebPage]}]}`. Outer node has no `@type`. | Parser may warn "Unnamed item" and drop outer. FAQPage inside may still validate, but `mainEntity: WebPage` inside same sub-graph will not link to the FAQPage. Rich result eligibility: partial at best. |
| All 279 articles | Two `BlogPosting` scripts with same headline but different `image` shape (`{ImageObject}` vs string) and different `datePublished` format (ISO vs `Mar 25, 2026` — the text-format date fails schema.org ISO 8601 requirement). | Google picks one non-deterministically, may flag conflicting metadata, article rich result eligibility unstable. |
| All articles with Rob Burke or Noah Barnett | Author `Person.sameAs` contains empty strings: `["https://www.linkedin.com/in/robjburke/", "", "", ""]`. | Empty string fails URL validation. Google drops those array items and may log a warning in Search Console's URL Inspection. |
| `/compare/little-green-light-vs-donordock` + `/compare/neon-crm-vs-donordock` | H1 says "Network for Good vs DonorDock" — inconsistent with URL, title tag, and schema `name`. | Schema won't flag this, but Google's entity reconciliation penalizes the contradictions (AI Overviews / Gemini may refuse to cite). |

### Category C — Google-spec field gaps (validates but loses rich result eligibility)

| Page | Schema | Missing required/recommended | Consequence |
|---|---|---|---|
| `/crm`, `/donor-outreach`, `/online-giving` | `SoftwareApplication` | Missing `@id`, missing root `Organization`, no `applicationSubCategory` on 2 of 3 | Software app rich card eligibility depends on the root product graph being solid |
| `/donor-outreach` SoftwareApplication | `aggregateRating: 4/6` | Disagrees with site-wide 4.8/200 — Google flags as inconsistent entity | Rating rich result suppressed |
| All compare pages SoftwareApplication | `aggregateRating` missing on 5 of 9 | Can't trigger star rating in search | — |
| `/webinars-events` events | Most events missing `offers`, `image`, `endDate` | Event rich result partially shown | — |
| `/about` AboutPage | Should be `AboutPage` mentioning root `Organization` with `foundingDate`, `numberOfEmployees`, `address`, `founders`, `sameAs`, `contactPoint` | Organization knowledge panel never triggers | — |
| Home | No `WebSite` with `potentialAction: SearchAction` | Sitelinks search box disabled in Google Search | — |
| Home + all pages | No `BreadcrumbList` except feature + integration templates | Breadcrumb rich result missing for 80%+ of pages | — |

---

## 4. Gap Analysis — what DonorDock has vs what a SaaS + publisher should have

Using Google's rich-result spec (developers.google.com/search/docs/appearance/structured-data) as the reference.

| Schema type | Should appear | Currently appears | Gap |
|---|---|---|---|
| `Organization` (root, site-wide via `@graph`) | every page | 0 pages | 100% |
| `WebSite` with `SearchAction` | homepage only | 0 pages | 100% |
| `BreadcrumbList` | every page except home | 59 integrations + 61 features + 1 compare = ~121 pages | ~80% missing on high-value pages (home, pricing, FAQ, product, solution, compare, article) |
| `SoftwareApplication` (root product) | 5 pages (home, /crm, /donor-outreach, /online-giving, /pricing) | 5 pages (but /pricing broken) | broken offer on pricing |
| `FAQPage` | /faq, /pricing (10+ Q visible), 9 compare pages (at minimum the "Worried about data migration?" block + more) | /faq (114 Q, nested), 4 compare pages in source (but 3 broken) | /pricing missing; 5 compare pages missing FAQPage entirely; 1 served correctly |
| `HowTo` | how-to articles (Q4 checklist, migration checklist, imposter-syndrome 90-day plan, SROI calculator) | 0 | 100% |
| `Article` / `BlogPosting` | 279 articles | 279 (duplicated) | all have duplicates |
| `Person` (authors) | embedded in every article | embedded (broken sameAs) | sameAs empty-strings |
| `ProfilePage` + `Person` | 36 team pages | 0 | 100% |
| `Event` | /webinars-events | yes, CollectionPage.hasPart | ✓ present, light on fields |
| `PodcastSeries` + `PodcastEpisode` | 2 podcast hubs + episodes | 0 | 100% |
| `VideoObject` | /tour, /convince-your-team (16 videos), /project-management (36), /donor-outreach (12), /otto (12), /crm (8), both podcast pages (2 each) | 0 | 100% |
| `Review` / `aggregateRating` | product pages, compare pages | partial (on product, some compare — but most compare pages BROKEN so invisible) | uneven |
| `ItemList` (compare index, feature-overview, solutions-overview, /compare pages that name tools) | several | 0 standalone; embedded on 2 compare pages | missing |
| `Course` | /academy, /fundraising-bootcamp | 0 | 100% |
| `ReserveAction` / `ContactPoint` | /donordock-demo, /contact | 0 | 100% |
| `JobPosting` | /careers | 0 | 100% |
| `NonprofitOrganization` (as reviewedItem) | 14 success stories | 0 | 100% |
| `speakable` | /faq, homepage hero, article intros | 0 | 100% |
| `LocalBusiness` or `Organization.address` | homepage, contact | 0 | no physical address / phone in structured data |

---

## 5. Priority Rich Result Opportunities

Ranked by impact × effort. All are recoverable now.

### Top priority (fix-first, measurable lift in 2–4 weeks)

1. **Fix the 6 broken compare-page JSON-LD blocks** — restores `FAQPage` (on 4 pages), `SoftwareApplication`, `Review`, and `BreadcrumbList` from literal invisibility. Targets: "bloomerang vs donordock" (kw volume), "donorperfect alternative", "neon crm alternative", "network for good alternative", "little green light alternative". Rich result: FAQ rich snippets, star ratings, breadcrumbs.
2. **Fix the /pricing broken Offer array** — restores the product offer, aggregateRating, and unblocks product rich card eligibility for the commercial-intent query "donordock pricing".
3. **Deduplicate BlogPosting on 279 articles** — keep the richer CMS-generated block, delete the hand-added one. Fix empty-string `sameAs` on author Person. Removes Google's non-determinism, unlocks article rich result eligibility sitewide.
4. **Un-nest `/faq` @graph** — rewrite as a single top-level `FAQPage` with `mainEntity` = 114 Question[]. Biggest volume-weighted FAQ page on the site today.
5. **Add root `Organization` + `WebSite` via site-wide `@graph`** — inject once in Webflow `<head>` custom code. Unlocks Knowledge Panel, sitelinks search box, and provides the canonical entity identity every other schema references via `@id`.

### Second priority (2–6 weeks)

6. **Add `FAQPage` to `/pricing`** (10+ visible Q already on the page) and to the 5 compare pages that don't have it.
7. **Add `BreadcrumbList` sitewide** — feature+integration templates have it; replicate that Webflow binding on home, pricing, FAQ, product, solution, compare, article, about, contact, tour, careers, team, success-stories, podcast.
8. **Add `VideoObject` wherever a video is embedded** — start with /tour (0 schema today + video hero), /convince-your-team (16 videos, 0 schema), both podcast pages. Requires thumbnail URL, uploadDate, duration ISO-8601, and contentUrl or embedUrl.
9. **Add `Person` + `ProfilePage` to 36 team pages** — unlocks author credibility signal for 279 articles that reference these people.
10. **Add `PodcastSeries` + `PodcastEpisode`** on the two podcast hubs and every episode article.

### Third priority (nice-to-have, higher effort)

11. **Add `HowTo`** to the ~10 articles that are clearly step-based (data migration checklist, imposter-syndrome 90-day plan, SROI, Q4 checklist, setup guides).
12. **Add `speakable` selectors** to the FAQPage and article intros.
13. **Upgrade /success-stories templates** to `Article` + `Review` (itemReviewed: SoftwareApplication "DonorDock") + `about: NonprofitOrganization` (the customer).
14. **Add `Course` to /academy, /fundraising-bootcamp**.
15. **Add `JobPosting`** schema to /careers (stub or aggregate).
16. **Fix the H1 on /compare/neon-crm and /compare/little-green-light** (says "Network for Good") — not strictly schema but blocks entity reconciliation.

---

## 6. Detailed Schema Recommendations by Page Type

### 6.1 Root `Organization` + `WebSite` (inject site-wide in Webflow head)

Unlocks Knowledge Panel and sitelinks search box. The `@id` provides a reusable anchor that every page's schema can reference.

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://www.donordock.com/#organization",
      "name": "DonorDock",
      "alternateName": "DonorDock, Inc.",
      "url": "https://www.donordock.com",
      "logo": {
        "@type": "ImageObject",
        "@id": "https://www.donordock.com/#logo",
        "url": "https://cdn.prod.website-files.com/63ce9d04b1ff6e36cf514274/63d946401af9adeec7e695b6_DonorDock%20Logo%20-%20Dark.svg",
        "width": 400,
        "height": 120,
        "caption": "DonorDock"
      },
      "image": { "@id": "https://www.donordock.com/#logo" },
      "description": "DonorDock is an all-in-one fundraising and donor management platform built for small-to-mid nonprofits. Donor CRM, online giving, and donor outreach in one place.",
      "foundingDate": "2018",
      "founders": [
        { "@type": "Person", "name": "Matt Bitzegaio" },
        { "@type": "Person", "name": "Andrew Lutgen" }
      ],
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "[FILL IN]",
        "addressLocality": "Fargo",
        "addressRegion": "ND",
        "postalCode": "[FILL IN]",
        "addressCountry": "US"
      },
      "contactPoint": [{
        "@type": "ContactPoint",
        "telephone": "[FILL IN]",
        "contactType": "customer support",
        "email": "support@donordock.com",
        "availableLanguage": ["en"],
        "areaServed": "US"
      }],
      "sameAs": [
        "https://www.facebook.com/donordock",
        "https://www.instagram.com/donordock",
        "https://www.linkedin.com/company/donordock",
        "https://www.tiktok.com/@donordock",
        "https://www.youtube.com/@donordock"
      ]
    },
    {
      "@type": "WebSite",
      "@id": "https://www.donordock.com/#website",
      "url": "https://www.donordock.com",
      "name": "DonorDock",
      "publisher": { "@id": "https://www.donordock.com/#organization" },
      "inLanguage": "en-US",
      "potentialAction": {
        "@type": "SearchAction",
        "target": {
          "@type": "EntryPoint",
          "urlTemplate": "https://www.donordock.com/search?q={search_term_string}"
        },
        "query-input": "required name=search_term_string"
      }
    }
  ]
}
```

Note: if DonorDock doesn't have a site-search endpoint yet, omit the `SearchAction` block for now; it's eligible only when a real search URL exists.

### 6.2 Homepage `/` — extend the existing WebPage

Replace the current single `WebPage` block with a graph that references the root Organization + WebSite, adds BreadcrumbList (trivial: 1 item), and keeps the nested SoftwareApplication.

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://www.donordock.com/#webpage",
      "url": "https://www.donordock.com/",
      "name": "CRM, Outreach, and Fundraising for Nonprofits",
      "description": "Steward donor relationships with an easy-to-use nonprofit CRM. Donor management, email, and giving pages in one place.",
      "isPartOf": { "@id": "https://www.donordock.com/#website" },
      "about": { "@id": "https://www.donordock.com/#software" },
      "inLanguage": "en-US",
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://cdn.prod.website-files.com/63ce9d04b1ff6e36cf514274/6532889f2379aa018d3524f7_Website%20Meta%20Description%20Image.webp"
      },
      "speakable": {
        "@type": "SpeakableSpecification",
        "cssSelector": ["h1", ".hero-subhead", "[data-speakable]"]
      }
    },
    {
      "@type": "SoftwareApplication",
      "@id": "https://www.donordock.com/#software",
      "name": "DonorDock",
      "applicationCategory": "BusinessApplication",
      "applicationSubCategory": "Nonprofit CRM Software",
      "operatingSystem": "Web, iOS, Android",
      "description": "All-in-one fundraising platform for small-to-mid nonprofits: donor CRM, online giving, donor outreach.",
      "url": "https://www.donordock.com/",
      "provider": { "@id": "https://www.donordock.com/#organization" },
      "offers": {
        "@type": "Offer",
        "url": "https://www.donordock.com/pricing",
        "availability": "https://schema.org/InStock",
        "priceCurrency": "USD",
        "price": "500",
        "priceValidUntil": "2027-12-31"
      },
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.8",
        "bestRating": "5",
        "worstRating": "1",
        "ratingCount": "200"
      },
      "featureList": [
        "Donor Management", "Email & Text Communication", "Online Giving",
        "Project Management", "AI Tools (Otto)", "Reporting & Analytics",
        "Task Automation", "Ask Pipelines", "Volunteer & Event Management",
        "Recurring Gift Management"
      ]
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.donordock.com/" }
      ]
    }
  ]
}
```

Note on rating consistency: pick either `ratingCount` OR `reviewCount`, not both. Use `ratingCount` site-wide. Fix /crm (uses `reviewCount: 200`) and /donor-outreach (uses `reviewCount: 6, ratingValue: 4`).

### 6.3 `/pricing` — fix broken JSON + add FAQPage + BreadcrumbList

Current block is broken (empty object in offers array). Replace entirely. Note the offer array should reflect ALL published plans, not just ONE Plan — verify the other tiers and add them.

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://www.donordock.com/pricing#webpage",
      "url": "https://www.donordock.com/pricing",
      "name": "DonorDock Pricing: Online Giving, CRM and Outreach",
      "description": "An all-in-one fundraising tool built for growing nonprofits: Donor Management CRM, Online Giving pages, and Donor Outreach.",
      "isPartOf": { "@id": "https://www.donordock.com/#website" },
      "about": { "@id": "https://www.donordock.com/#software" },
      "breadcrumb": { "@id": "https://www.donordock.com/pricing#breadcrumb" },
      "mainEntity": { "@id": "https://www.donordock.com/pricing#faq" },
      "inLanguage": "en-US"
    },
    {
      "@type": "SoftwareApplication",
      "@id": "https://www.donordock.com/#software",
      "name": "DonorDock",
      "applicationCategory": "BusinessApplication",
      "operatingSystem": "Web",
      "description": "All-in-one fundraising platform for growing nonprofits with donor management CRM, online giving pages, and donor outreach tools.",
      "offers": [
        {
          "@type": "Offer",
          "name": "ONE Plan",
          "price": "500",
          "priceCurrency": "USD",
          "priceSpecification": {
            "@type": "UnitPriceSpecification",
            "price": "500",
            "priceCurrency": "USD",
            "unitText": "MONTH",
            "billingDuration": "P1Y"
          },
          "description": "A fully equipped platform with generous capacity across your team and communications. Includes unlimited contacts, 5 users, 10,000 marketing emails per month, 1,000 text message credits per month, and 10 automations.",
          "availability": "https://schema.org/InStock",
          "url": "https://www.donordock.com/pricing#one-plan"
        }
      ],
      "featureList": [
        "Unlimited contacts", "Donor Management CRM", "Online Giving pages",
        "Donor Outreach with email and text", "Project Management",
        "Otto Intelligence automation", "Fundraising reports",
        "QuickBooks integration", "100+ integrations", "SOC 2 Type 2 certified",
        "90 day money-back guarantee", "White-glove data migration", "Human support"
      ],
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.8",
        "bestRating": "5",
        "ratingCount": "200"
      },
      "provider": { "@id": "https://www.donordock.com/#organization" }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://www.donordock.com/pricing#breadcrumb",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.donordock.com/" },
        { "@type": "ListItem", "position": 2, "name": "Pricing", "item": "https://www.donordock.com/pricing" }
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://www.donordock.com/pricing#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How does DonorDock help nonprofits manage fundraising and donors?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "DonorDock centralizes contacts, gifts, communication history, tasks, and giving forms in one workspace so your team can manage fundraising without switching between tools."
          }
        },
        {
          "@type": "Question",
          "name": "How quickly can I get set up with DonorDock?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Most teams are live in under two weeks with white-glove data migration. Self-starters can be sending their first appeal the same day."
          }
        }
        /* ...add all 10+ visible questions on /pricing verbatim... */
      ]
    }
  ]
}
```

### 6.4 `/faq` — un-nest the @graph

Current structure is `{"@graph":[{"@graph":[FAQPage, WebPage]}]}` (triple-nested, outer has no @type). Flatten to:

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://www.donordock.com/faq#webpage",
      "url": "https://www.donordock.com/faq",
      "name": "DonorDock FAQ",
      "description": "Get your frequently asked questions answered about DonorDock.",
      "isPartOf": { "@id": "https://www.donordock.com/#website" },
      "mainEntity": { "@id": "https://www.donordock.com/faq#faqpage" },
      "breadcrumb": { "@id": "https://www.donordock.com/faq#breadcrumb" },
      "speakable": {
        "@type": "SpeakableSpecification",
        "cssSelector": [".faq-question", ".faq-answer"]
      }
    },
    {
      "@type": "FAQPage",
      "@id": "https://www.donordock.com/faq#faqpage",
      "mainEntity": [
        /* all 114 Question objects, flattened one level */
        {
          "@type": "Question",
          "name": "What is DonorDock and who is it designed for?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "DonorDock is an all-in-one fundraising and donor management platform built for fundraising teams who need CRM, online giving, outreach, automation, and project management in one place."
          }
        }
        /* ...113 more... */
      ]
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://www.donordock.com/faq#breadcrumb",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.donordock.com/" },
        { "@type": "ListItem", "position": 2, "name": "FAQ", "item": "https://www.donordock.com/faq" }
      ]
    }
  ]
}
```

### 6.5 Article template (apply to all 279 articles)

Delete the second/hand-added BlogPosting block. Keep ONE block with the CMS shape (ISO datePublished, full author Person, ImageObject image). Fix `sameAs` to be an array with real URLs only.

```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "@id": "https://www.donordock.com/articles/{slug}#article",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://www.donordock.com/articles/{slug}" },
  "headline": "{headline}",
  "description": "{meta description}",
  "image": {
    "@type": "ImageObject",
    "url": "{hero image URL}",
    "width": 1200,
    "height": 630,
    "caption": "{hero alt text}"
  },
  "author": {
    "@type": "Person",
    "@id": "https://www.donordock.com/team/{author-slug}#person",
    "name": "Rob Burke",
    "jobTitle": "Chief Marketing Officer",
    "image": "https://cdn.prod.website-files.com/.../rob-burke.webp",
    "email": "rburke@donordock.com",
    "url": "https://www.donordock.com/team/rob-burke",
    "sameAs": [
      "https://www.linkedin.com/in/robjburke/"
    ],
    "worksFor": { "@id": "https://www.donordock.com/#organization" }
  },
  "publisher": { "@id": "https://www.donordock.com/#organization" },
  "datePublished": "2026-03-25T17:55:01Z",
  "dateModified": "2026-03-25T17:55:01Z",
  "keywords": ["Fundraising", "Nonprofit CRM", "Donor Relationships"],
  "articleSection": "Fundraising",
  "wordCount": 3200,
  "inLanguage": "en-US",
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelector": ["article h1", "article .article-intro"]
  }
}
```

Key fixes from current state:
- Remove empty strings from `sameAs`
- Use ISO 8601 for `datePublished` (the duplicate block's `"Mar 25, 2026"` format is invalid)
- Add `@id` on article so other schemas (FAQPage, HowTo) on the same article can reference it
- Add `worksFor` → root Organization reference
- Add `wordCount`, `articleSection`, `speakable`

For step-based articles, wrap the same page with both `BlogPosting` AND `HowTo` (legal — they describe the same content from different angles):

```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "End-of-Year Success: a 7-week execution checklist for Q4",
  "description": "Execute a focused Q4 fundraising plan in 7 weeks.",
  "totalTime": "P7W",
  "step": [
    { "@type": "HowToStep", "position": 1, "name": "Week 1 — Segment donors",
      "text": "Split your list into lapsed, active, and new.", "url": "https://www.donordock.com/articles/{slug}#week-1" },
    { "@type": "HowToStep", "position": 2, "name": "Week 2 — Plan GivingTuesday", "text": "...", "url": "#week-2" }
    /* ...5 more... */
  ],
  "image": "{hero URL}"
}
```

### 6.6 Compare page template (apply to all 9 compare pages)

Every compare page should be a `@graph` with: `WebPage`, `SoftwareApplication` (DonorDock), `SoftwareApplication` (competitor, with Review showing DonorDock's perspective), `FAQPage` (with the visible Q&A), `BreadcrumbList`. Fix all JSON syntax errors (trailing commas, extra braces). Example for /compare/bloomerang-vs-donordock:

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://www.donordock.com/compare/bloomerang-vs-donordock#webpage",
      "url": "https://www.donordock.com/compare/bloomerang-vs-donordock",
      "name": "Bloomerang vs DonorDock: Nonprofit CRM Comparison",
      "description": "Compare Bloomerang and DonorDock side by side. See how DonorDock's all-in-one CRM with unlimited contacts, AI tools, and daily action features stacks up against Bloomerang.",
      "isPartOf": { "@id": "https://www.donordock.com/#website" },
      "about": { "@id": "https://www.donordock.com/#software" },
      "breadcrumb": { "@id": "https://www.donordock.com/compare/bloomerang-vs-donordock#breadcrumb" },
      "mainEntity": { "@id": "https://www.donordock.com/compare/bloomerang-vs-donordock#faq" },
      "inLanguage": "en-US"
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://www.donordock.com/compare/bloomerang-vs-donordock#breadcrumb",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.donordock.com/" },
        { "@type": "ListItem", "position": 2, "name": "Compare", "item": "https://www.donordock.com/compare" },
        { "@type": "ListItem", "position": 3, "name": "Bloomerang vs DonorDock", "item": "https://www.donordock.com/compare/bloomerang-vs-donordock" }
      ]
    },
    {
      "@type": "SoftwareApplication",
      "@id": "https://www.donordock.com/#software",
      "name": "DonorDock",
      "applicationCategory": "BusinessApplication",
      "applicationSubCategory": "Nonprofit CRM Software",
      "operatingSystem": "Web",
      "offers": { "@type": "Offer", "url": "https://www.donordock.com/pricing", "availability": "https://schema.org/InStock", "priceCurrency": "USD" },
      "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.8", "bestRating": "5", "ratingCount": "200" },
      "featureList": [
        "Donor Management CRM", "Online Giving", "Email Marketing",
        "Text Messaging", "Automations", "Custom Reporting", "Unlimited Contacts"
      ],
      "description": "DonorDock combines fundraising, CRM, email, and donor stewardship in one simple platform with unlimited contacts, AI tools, and daily action features."
    },
    {
      "@type": "FAQPage",
      "@id": "https://www.donordock.com/compare/bloomerang-vs-donordock#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "How does DonorDock compare to Bloomerang for small nonprofits?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "DonorDock includes unlimited contacts on its ONE Plan and was voted 'Easiest Setup' on G2, while Bloomerang prices by contact tier. Both offer strong donor CRM features, but DonorDock is better suited for teams who want an all-in-one tool with online giving and outreach built in."
          }
        },
        {
          "@type": "Question",
          "name": "Is DonorDock cheaper than Bloomerang?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "DonorDock's ONE Plan starts at $500/month with unlimited contacts, while Bloomerang pricing scales with contact count. For most small-to-mid nonprofits, DonorDock is more affordable, especially as your list grows."
          }
        },
        {
          "@type": "Question",
          "name": "Can I migrate my Bloomerang data to DonorDock?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes — DonorDock includes white-glove data migration from Bloomerang, Salesforce, DonorPerfect, Little Green Light, and most other CRMs at no extra cost during onboarding."
          }
        }
      ]
    }
  ]
}
```

Apply the identical template to all 9 compare pages, updating competitor name, FAQ content, and the comparative Review block where present.

### 6.7 Product page template (`/crm`, `/donor-outreach`, `/online-giving`)

Normalize aggregateRating (consistent 4.8/200 everywhere), add BreadcrumbList, add VideoObject for embedded demos, reference root Organization via @id. Current `/crm` is closest to right — below is the target shape:

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://www.donordock.com/crm#webpage",
      "url": "https://www.donordock.com/crm",
      "name": "Nonprofit CRM & Donor Tracking Software",
      "description": "Manage donor data, giving history, and engagement in one powerful CRM.",
      "isPartOf": { "@id": "https://www.donordock.com/#website" },
      "about": { "@id": "https://www.donordock.com/crm#software" },
      "breadcrumb": { "@id": "https://www.donordock.com/crm#breadcrumb" },
      "inLanguage": "en-US"
    },
    {
      "@type": "SoftwareApplication",
      "@id": "https://www.donordock.com/crm#software",
      "name": "DonorDock CRM",
      "applicationCategory": "BusinessApplication",
      "applicationSubCategory": "Nonprofit CRM Software",
      "operatingSystem": "Web",
      "description": "Manage donor data, giving history, and engagement in one powerful CRM. DonorDock's tools help small nonprofits streamline donor management with clarity and control.",
      "offers": { "@type": "Offer", "url": "https://www.donordock.com/pricing", "availability": "https://schema.org/InStock", "priceCurrency": "USD" },
      "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.8", "bestRating": "5", "ratingCount": "200" },
      "featureList": [
        "Donor Management", "Activity Tracking", "Giving Timeline",
        "Campaign & Appeal Management", "Contact Management", "Automations",
        "AskBoard for Moves Management", "Otto AI Assistant", "Fundraising Reports",
        "Custom Fields", "Data Import & Migration", "Donor Segmentation",
        "Integration with 100+ apps"
      ],
      "provider": { "@id": "https://www.donordock.com/#organization" }
    },
    {
      "@type": "VideoObject",
      "name": "DonorDock CRM overview",
      "description": "Walk through the DonorDock CRM: contacts, gifts, and the Ask board.",
      "thumbnailUrl": "https://cdn.prod.website-files.com/.../crm-overview-thumb.webp",
      "uploadDate": "2025-09-01T00:00:00Z",
      "duration": "PT2M30S",
      "contentUrl": "https://www.youtube.com/watch?v=XXXXX",
      "embedUrl": "https://www.youtube.com/embed/XXXXX"
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://www.donordock.com/crm#breadcrumb",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.donordock.com/" },
        { "@type": "ListItem", "position": 2, "name": "CRM", "item": "https://www.donordock.com/crm" }
      ]
    }
  ]
}
```

### 6.8 Team page template (apply to all 36 team pages)

Currently zero schema. Add:

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "ProfilePage",
      "@id": "https://www.donordock.com/team/rob-burke#profilepage",
      "url": "https://www.donordock.com/team/rob-burke",
      "name": "Rob Burke — Chief Marketing Officer at DonorDock",
      "description": "Rob Burke leads marketing at DonorDock.",
      "isPartOf": { "@id": "https://www.donordock.com/#website" },
      "mainEntity": { "@id": "https://www.donordock.com/team/rob-burke#person" },
      "breadcrumb": { "@id": "https://www.donordock.com/team/rob-burke#breadcrumb" }
    },
    {
      "@type": "Person",
      "@id": "https://www.donordock.com/team/rob-burke#person",
      "name": "Rob Burke",
      "givenName": "Rob",
      "familyName": "Burke",
      "jobTitle": "Chief Marketing Officer",
      "email": "rburke@donordock.com",
      "image": "https://cdn.prod.website-files.com/.../rob-burke.webp",
      "worksFor": { "@id": "https://www.donordock.com/#organization" },
      "sameAs": [
        "https://www.linkedin.com/in/robjburke/"
      ],
      "knowsAbout": ["Nonprofit marketing", "SEO", "Donor engagement", "Fundraising strategy"]
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://www.donordock.com/team/rob-burke#breadcrumb",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.donordock.com/" },
        { "@type": "ListItem", "position": 2, "name": "Team", "item": "https://www.donordock.com/team" },
        { "@type": "ListItem", "position": 3, "name": "Rob Burke", "item": "https://www.donordock.com/team/rob-burke" }
      ]
    }
  ]
}
```

### 6.9 Podcast pages (both hubs + every episode)

Add `PodcastSeries` to each hub and `PodcastEpisode` to each episode. Hub template:

```json
{
  "@context": "https://schema.org",
  "@type": "PodcastSeries",
  "@id": "https://www.donordock.com/the-focused-fundraiser-podcast#series",
  "name": "The Focused Fundraiser",
  "description": "Practical fundraising strategies for small-nonprofit teams.",
  "url": "https://www.donordock.com/the-focused-fundraiser-podcast",
  "webFeed": "https://feeds.buzzsprout.com/XXXXXXX.rss",
  "author": { "@id": "https://www.donordock.com/#organization" },
  "publisher": { "@id": "https://www.donordock.com/#organization" },
  "image": "https://cdn.prod.website-files.com/.../focused-fundraiser-cover.webp",
  "inLanguage": "en-US"
}
```

Episode template (on article pages that are podcast episodes):

```json
{
  "@context": "https://schema.org",
  "@type": "PodcastEpisode",
  "name": "How to calculate nonprofit social return on investment",
  "url": "https://www.donordock.com/articles/how-to-calculate-nonprofit-social-return-on-investment",
  "episodeNumber": 12,
  "partOfSeries": { "@id": "https://www.donordock.com/the-focused-fundraiser-podcast#series" },
  "datePublished": "2025-11-05",
  "duration": "PT32M10S",
  "associatedMedia": {
    "@type": "MediaObject",
    "contentUrl": "https://traffic.buzzsprout.com/.../episode-012.mp3"
  },
  "description": "A step-by-step guide to measuring SROI for small nonprofits."
}
```

### 6.10 VideoObject (any page with an embedded video)

```json
{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "DonorDock 3-minute product tour",
  "description": "See how DonorDock helps small nonprofits manage donors, accept gifts, and communicate — all in one place.",
  "thumbnailUrl": "https://cdn.prod.website-files.com/.../tour-thumbnail.webp",
  "uploadDate": "2025-06-15T00:00:00Z",
  "duration": "PT3M12S",
  "contentUrl": "https://www.youtube.com/watch?v=XXXXX",
  "embedUrl": "https://www.youtube.com/embed/XXXXX",
  "publisher": { "@id": "https://www.donordock.com/#organization" }
}
```

Priority pages needing VideoObject: `/tour`, `/convince-your-team` (16 Wistia videos), `/project-management`, `/donor-outreach`, `/otto`, `/crm`, both podcast hubs, `/donordock-demo`.

### 6.11 Success story template (replace current CollectionPage)

Current success-story pages use `CollectionPage → about: Organization` — wrong. These are case studies.

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Article",
      "@id": "https://www.donordock.com/success-stories/family-programs-hawaii#article",
      "headline": "How Family Programs Hawaii saved 15 hours a week with DonorDock",
      "description": "A case study on Family Programs Hawaii's switch to DonorDock.",
      "author": { "@id": "https://www.donordock.com/#organization" },
      "publisher": { "@id": "https://www.donordock.com/#organization" },
      "datePublished": "2025-06-01",
      "image": "https://cdn.prod.website-files.com/.../fph-hero.webp",
      "about": { "@id": "https://www.donordock.com/success-stories/family-programs-hawaii#nonprofit" }
    },
    {
      "@type": "NonprofitOrganization",
      "@id": "https://www.donordock.com/success-stories/family-programs-hawaii#nonprofit",
      "name": "Family Programs Hawaii",
      "url": "https://www.familyprogramshawaii.org/",
      "description": "Hawaii-based nonprofit supporting children and families."
    },
    {
      "@type": "Review",
      "itemReviewed": { "@id": "https://www.donordock.com/#software" },
      "author": { "@id": "https://www.donordock.com/success-stories/family-programs-hawaii#nonprofit" },
      "reviewRating": { "@type": "Rating", "ratingValue": "5", "bestRating": "5" },
      "reviewBody": "Quote from the customer case study."
    }
  ]
}
```

### 6.12 `/tour`, `/contact`, `/careers` (currently zero schema)

**/tour:**

```json
{
  "@context": "https://schema.org",
  "@graph": [
    { "@type": "WebPage", "@id": "https://www.donordock.com/tour#webpage", "url": "https://www.donordock.com/tour", "name": "DonorDock Product Tour", "isPartOf": { "@id": "https://www.donordock.com/#website" }, "about": { "@id": "https://www.donordock.com/#software" } },
    { "@type": "VideoObject", "name": "DonorDock 3-minute tour", "description": "...", "thumbnailUrl": "...", "uploadDate": "2025-06-15T00:00:00Z", "duration": "PT3M", "contentUrl": "...", "embedUrl": "..." },
    { "@type": "BreadcrumbList", "itemListElement": [ { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.donordock.com/" }, { "@type": "ListItem", "position": 2, "name": "Tour", "item": "https://www.donordock.com/tour" } ] }
  ]
}
```

**/contact:**

```json
{
  "@context": "https://schema.org",
  "@graph": [
    { "@type": "ContactPage", "@id": "https://www.donordock.com/contact#webpage", "url": "https://www.donordock.com/contact", "name": "Contact DonorDock", "isPartOf": { "@id": "https://www.donordock.com/#website" }, "mainEntity": { "@id": "https://www.donordock.com/#organization" } },
    { "@type": "BreadcrumbList", "itemListElement": [ { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.donordock.com/" }, { "@type": "ListItem", "position": 2, "name": "Contact", "item": "https://www.donordock.com/contact" } ] }
  ]
}
```

**/careers:**

```json
{
  "@context": "https://schema.org",
  "@graph": [
    { "@type": "WebPage", "@id": "https://www.donordock.com/careers#webpage", "url": "https://www.donordock.com/careers", "name": "Careers at DonorDock", "isPartOf": { "@id": "https://www.donordock.com/#website" } },
    { "@type": "Organization", "@id": "https://www.donordock.com/#organization" },
    { "@type": "BreadcrumbList", "itemListElement": [ { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.donordock.com/" }, { "@type": "ListItem", "position": 2, "name": "Careers", "item": "https://www.donordock.com/careers" } ] }
  ]
}
```

For each open role, add a per-job `JobPosting` block:

```json
{
  "@context": "https://schema.org",
  "@type": "JobPosting",
  "title": "Senior Product Designer",
  "description": "...full role description with HTML allowed...",
  "datePosted": "2026-04-01",
  "validThrough": "2026-06-30T23:59:59Z",
  "employmentType": "FULL_TIME",
  "hiringOrganization": { "@id": "https://www.donordock.com/#organization" },
  "jobLocation": { "@type": "Place", "address": { "@type": "PostalAddress", "addressLocality": "Fargo", "addressRegion": "ND", "addressCountry": "US" } },
  "baseSalary": { "@type": "MonetaryAmount", "currency": "USD", "value": { "@type": "QuantitativeValue", "minValue": 90000, "maxValue": 120000, "unitText": "YEAR" } }
}
```

### 6.13 Pillar/Academy/Bootcamp (`Course` schema)

```json
{
  "@context": "https://schema.org",
  "@type": "Course",
  "name": "DonorDock Fundraising Bootcamp",
  "description": "A free 6-week bootcamp for small-nonprofit fundraisers.",
  "provider": { "@id": "https://www.donordock.com/#organization" },
  "hasCourseInstance": {
    "@type": "CourseInstance",
    "courseMode": "Online",
    "courseWorkload": "PT2H",
    "startDate": "2026-05-01",
    "endDate": "2026-06-12"
  }
}
```

---

## 7. Submission & Verification Guidance

### 7.1 Before deploying

1. For every generated JSON-LD block, paste it into https://validator.schema.org/ — expect zero errors, zero warnings.
2. Then paste into https://search.google.com/test/rich-results — expect "Item is eligible for rich results" and at least one eligible enhancement detected.
3. Hand-validate the offending pages (`/pricing`, 6 compare pages, `/faq`, `/customer-success`) as the top-priority set.

### 7.2 Deployment pattern (Webflow)

- Site-wide `Organization` + `WebSite` graph: put in the Webflow project settings → Custom Code → Head Code (runs on every page).
- Per-page schemas: use Webflow's per-page "Before `</head>` tag" custom code slot, bound to CMS fields where possible.
- Article BlogPosting: fix the CMS template once; delete the second (hand-added) script source. Author sameAs: bind to team-member sameAs field (Person collection item), filter out empty strings at bind time.
- For the 114-question FAQPage: consider generating the JSON-LD programmatically from the Webflow CMS "FAQ" collection to eliminate manual JSON drift — each time a question is added/edited in the CMS, the schema regenerates.

### 7.3 Post-deployment verification (within 72 hours)

1. **Google Search Console → URL Inspection**: run Live Test on `/pricing`, `/faq`, the 9 compare pages, 3 product pages, a sample article, a sample team page, `/tour`, `/contact`. Confirm structured data is detected with zero errors.
2. **GSC → Enhancements**: monitor for new cards appearing: "FAQ", "Products", "Breadcrumbs", "Sitelinks searchbox", "Videos". Errors/warnings surface here within 2–7 days of re-crawl.
3. **Request indexing** for the 15–20 priority pages after deployment so Google picks up the new schema quickly.
4. **Bing Webmaster Tools**: submit sitemap refresh. Bing powers ChatGPT Search and Copilot — broken schema on DonorDock today is invisible to both.

### 7.4 Ongoing (weekly for first month, then monthly)

- Set a Search Console email alert for "Structured data errors"
- Track CTR lift by page type in GSC (filter by URL pattern) — FAQ rich results typically add 3–7% CTR, breadcrumbs 2–4%, star ratings on product 5–15%
- Re-run `schema-coverage.md` audit monthly to catch template drift; watch for new duplicate BlogPosting appearances when the Webflow CMS is edited
- When new compare pages or solution pages are added, ensure they follow the templates in Section 6.6 / 6.7

### 7.5 Additional platforms worth submitting to

- Yandex Webmaster (emerging AEO source for Kagi/You.com)
- Brave Search Webmaster Tools (distinct crawler — Brave and Kagi both check schema)
- Perplexity and ChatGPT Search discover schema primarily through Bing and Google, so fixing GSC coverage fixes those downstream

---

## 8. Quick-reference scorecard

| Metric | Current | Target | Gap |
|---|---|---|---|
| Pages with valid JSON-LD | 79% (28 of 35 sampled) | 100% | 7 pages broken |
| Pages with BreadcrumbList | 17% (6 of 35) | 100% | 29 pages |
| Pages with root Organization via `@id` | 0% | 100% | every page |
| Articles with single BlogPosting | 0% (all duplicated) | 100% | 279 articles |
| Team pages with Person schema | 0% (0 of 36) | 100% | 36 pages |
| Compare pages with FAQPage in served HTML | 11% (1 of 9 — spreadsheets) | 100% | 8 pages |
| Product pages with VideoObject | 0% | 100% | 3 pages + /tour |
| Podcast pages with PodcastSeries/Episode | 0% | 100% | 2 hubs + episodes |
| Overall schema health score | 42/100 | 90+/100 | 48 points |

The single largest point gain (~18 points) is fixing the 7 broken JSON blocks — that recovers schema that already exists in the source but is unparseable. The second largest (~12 points) is deduplicating BlogPosting across 279 articles. Together those two fixes take the score from 42 to ~72 and are both mechanical edits inside existing Webflow templates.
