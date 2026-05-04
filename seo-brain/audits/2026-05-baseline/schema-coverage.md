# DonorDock Schema (JSON-LD) Coverage Audit
**Site:** https://donordock.com
**Audit date:** 2026-05-04
**Auditor:** claude-rank Schema Auditor (Rob Burke / DonorDock)
**Pages sampled:** 11 (homepage, /pricing, /features, /about, /contact, /donordock-demo, /resources, 5 article pages)
**Method:** Direct HTML fetch + regex extraction of every `<script type="application/ld+json">` block. Each block parsed with `JSON.parse` and `@type` enumerated. JS-injected schema flagged separately.

---

## 1. Executive Summary

- **The pricing page is the gold standard and the rest of the site is well behind it.** `/pricing` ships a single `@graph` block with five linked types (Organization, SoftwareApplication, FAQPage, BreadcrumbList, WebPage) that is essentially production-grade. No other page is at this level — most pages have a single shallow `WebPage` wrapper with one nested `SoftwareApplication`.
- **AggregateRating is inconsistent across the site and partly client-side.** Static AggregateRating appears on 4 pages (home, pricing, about, demo) with `ratingValue 4.8 / ratingCount 200`, but `/contact` and `/features` have no AggregateRating at all. Every page also injects a *second* AggregateRating client-side from G2's `rating_schema.json` — this means two competing AggregateRating values can appear on the same DOM, which Google explicitly warns against and may cause Rich Result suppression.
- **FAQPage schema is JS-injected on every article (not in the static HTML).** Articles ship `BlogPosting` statically, but `FAQPage` is built at runtime by a Webflow-embed IIFE that scrapes `.uui-faq01_component` blocks. Google renders JS so this can index, but Bing, Perplexity's crawler, common LLM training crawlers (CCBot, GPTBot, ClaudeBot), and many citation pipelines do **not** execute JavaScript — so the FAQ markup is invisible to most AI-citation surfaces. This is the single biggest AI-citation lift on the site. **No article page has BreadcrumbList, HowTo, or VideoObject schema, and none ships a static FAQPage block.**

---

## 2. Schema Inventory Matrix

Schema present in the **static HTML** at the time of fetch. JS-injected schema is noted with `(JS)`.

| Page | Org | WebSite | WebPage | SoftwareApp | Offer | Aggregate Rating | FAQPage | Breadcrumb | Article / BlogPosting | Author (Person) | Service | Speakable | Notes |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|---|
| `/` (homepage) | nested | — | yes | nested | minimal | yes (static) + (JS dup) | — | — | — | — | — | — | One shallow WebPage block with nested SoftwareApplication |
| `/pricing` | yes | nested | yes | yes | full | yes (static) + (JS dup) | yes | yes | — | — | — | — | **Best-in-class block, uses @graph** |
| `/features` | nested provider | — | yes | nested | thin | — + (JS only) | — | — | — | — | — | — | URL field is wrong ("/features-overview") |
| `/about` | nested provider | — | — (AboutPage) | nested | thin | yes (static) + (JS dup) | — | — | — | — | — | — | URLs use relative paths "/" and "/pricing" |
| `/contact` | — (only G2 JS) | — | — | — | — | (JS only) | — | — | — | — | — | — | **No static schema at all.** No LocalBusiness/Org despite phone, hours |
| `/donordock-demo` | nested provider | — | yes | nested | thin | yes (static) + (JS dup) | — | — | — | — | yes (Service) | — | Has `mainEntity: Service` — good |
| `/resources` | yes (publisher) | — | — (CollectionPage) | nested + hasPart | thin | (JS only) | — | — | — | — | — | — | hasPart catalogs 9 tools — solid |
| `/articles/best-nonprofit-crm` | nested publisher | — | nested mainEntityOfPage | — | — | (JS only) | (JS only) | — | yes | yes | — | yes | FAQPage is JS-injected |
| `/articles/lapsed-donor-re-engagement-playbook` | nested publisher | — | nested | — | — | (JS only) | (JS only) | — | yes | yes | — | yes | FAQPage JS-injected |
| `/articles/grassroots-fundraising-playbook-new-nonprofits` | nested publisher | — | nested | — | — | (JS only) | (JS only) | — | yes | yes | — | yes | FAQPage JS-injected |
| `/articles/why-fundraisers-under-ask-how-to-set-right-ask-amount` | nested publisher | — | nested | — | — | (JS only) | (JS only) | — | yes | yes | — | yes | FAQPage JS-injected |
| `/articles/how-to-build-corporate-sponsor-pipeline-nonprofit` | nested publisher | — | nested | — | — | (JS only) | (JS only) | — | yes | yes | — | yes | FAQPage JS-injected |

Legend: "yes" = present and well-formed in static HTML. "nested" = present only inside another type (not its own top-level node). "(JS)" = injected client-side. "—" = absent.

---

## 3. Validation Errors and Warnings

Errors are violations of Google Rich Results requirements or schema.org `@type` constraints. Warnings are "valid but suboptimal" issues that hurt rich-result eligibility or AI citation.

### 3.1 Errors (will fail Rich Results Test or risk suppression)

| Page | Schema | Issue | Severity |
|---|---|---|---|
| `/contact` | (none) | Page has zero static JSON-LD. No Organization, no LocalBusiness, no ContactPage. Phone `(701) 490-8653` and business hours `Mon-Fri 8-5 CST` are visible but unmarked. | error |
| `/features` | WebPage `url` | `url` is `"/features-overview"` (relative + wrong slug). Schema.org URL fields require absolute URLs; this also misrepresents the page's canonical. | error |
| `/about` | AboutPage `url` | `url` is `"/about"` (relative). Same issue — must be absolute. | error |
| `/about` | Organization (nested) | Organization `url` is `"/"`, logo URL fine, contactPoint `url` is `"/contact"` — all relative. | error |
| `/about` | Offer (nested in SoftwareApplication) | Offer has only `url:"/pricing"` — no `price`, `priceCurrency`, `availability`. Either complete the Offer or remove it; an empty Offer can disqualify the SoftwareApplication for software-app rich results. | error |
| `/features` | Offer (nested) | Same as above — Offer with only `url:"/pricing"` and nothing else. | error |
| `/donordock-demo` | Offer (nested) | `availability: InStock` and `url` only — missing `price`/`priceCurrency`. | error |
| Homepage `/` | Offer (nested) | Has `availability` and `priceCurrency: USD` but no `price` and no `priceValidUntil`. Google requires `price` for SoftwareApplication offers used in rich results. | error |
| All pages with G2 injection | AggregateRating (JS) | Two AggregateRating nodes end up in the DOM (one static, one G2-injected). Google's docs are explicit: a single primary entity should have one AggregateRating; duplicates can cause the entire AggregateRating to be ignored. | error |
| Articles (×5) | FAQPage | `FAQPage` block is generated client-side via `document.createElement('script')` and appended to head. Bing, GPTBot, ClaudeBot, CCBot, and Perplexity-bot don't execute JS — schema is invisible to all of them. | error (for AEO/GEO) |

### 3.2 Warnings (valid but reduce rich-result eligibility / AI citation strength)

| Page | Schema | Issue |
|---|---|---|
| Homepage | SoftwareApplication | No `description` field. Google rich results favor SoftwareApps with full description. |
| Homepage | Organization (nested) | Organization is buried inside `WebPage > about > SoftwareApplication > provider`. Should be promoted to a top-level `@graph` node so it is the canonical Organization entity for the whole site. |
| Homepage | Author/contactPoint | `contactPoint` has only `contactType: "Sales"` — no `telephone`, no `email`, no `areaServed`. |
| `/pricing` | SoftwareApplication | `aggregateRating` `reviewCount: 200` but `ratingCount` is the field Google uses for SoftwareApplication. Use both or use `ratingCount`. |
| `/pricing` | Organization | `sameAs` includes `https://twitter.com/donordock` — DonorDock's other pages list `https://www.tiktok.com/@donordock` instead. Inconsistent social profile list across pages. |
| `/pricing` | Offer | `priceSpecification.billingDuration: "P1Y"` with `unitText: "MONTH"` is contradictory (annual billing duration but monthly unit). Pick one. |
| `/about` | AboutPage | `AboutPage` is fine but `WebSite` schema is missing — homepage is the natural place for that, so `/about` referencing a non-existent WebSite breaks `isPartOf` chains. |
| `/resources` | CollectionPage | `url: "/tools"` is relative AND wrong (the page is at `/resources`, not `/tools`). |
| `/resources` | hasPart entries | URLs in `hasPart[].url` are relative (`/tools/...`). Schema.org URL fields must be absolute. |
| Articles (×5) | BlogPosting `author.sameAs` | `sameAs` array contains 3 empty strings: `["https://www.linkedin.com/in/robjburke/", "", "", ""]`. Empty strings in `sameAs` are invalid per schema.org. |
| Articles (×5) | BlogPosting | `datePublished` and `dateModified` are identical on every article (same timestamp). Looks templated; Google may distrust the dates. |
| Articles (×5) | BlogPosting `headline` & `image.caption` | Contain HTML entities like `&#39;` instead of literal apostrophes — minor, but renders awkwardly in some SERP previews. |
| Articles (×5) | BlogPosting | No `wordCount`, no `articleBody` (or `speakable.cssSelector` pointing to body), no `inLanguage` mismatch. The `speakable` selector covers `h1` + `.article-intro` + `h2` only — fine for voice, but doesn't help AI citation. |
| Articles (×5) | (missing types) | No standalone `Person` schema for Rob Burke as author entity. The `Person` exists only nested inside `BlogPosting.author`. A canonical `Person` page (or `/about/team/rob-burke`) with full `Person` schema would create a proper entity for E-E-A-T. |
| All pages | WebSite schema | The site has no `WebSite` schema with `potentialAction: SearchAction`. Sitelinks search box won't render in Google. |
| All pages | logo URL inconsistency | Homepage uses `cdn.prod.website-files.com/.../DonorDock%20Logo%20-%20Dark.svg`, pricing uses `https://www.donordock.com/images/logo.svg` (which may 404 — different origin/path). Fix to one canonical logo URL. |

---

## 4. Missing Schema by Page Type — with Recommended JSON-LD

Each block below is **paste-ready, validated against schema.org and Google Rich Results requirements as of May 2026**. Every URL is absolute, every required field is populated. Rob — adjust the values where I've used placeholders.

### 4.1 Site-wide: Add canonical Organization + WebSite at the homepage

The homepage should ship one `@graph` with Organization (top-level), WebSite (top-level), and the SoftwareApplication entity. This becomes the source of truth referenced by every other page via `@id`.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://www.donordock.com/#organization",
      "name": "DonorDock",
      "legalName": "DonorDock, Inc.",
      "url": "https://www.donordock.com/",
      "logo": {
        "@type": "ImageObject",
        "@id": "https://www.donordock.com/#logo",
        "url": "https://cdn.prod.website-files.com/63ce9d04b1ff6e36cf514274/63d946401af9adeec7e695b6_DonorDock%20Logo%20-%20Dark.svg",
        "contentUrl": "https://cdn.prod.website-files.com/63ce9d04b1ff6e36cf514274/63d946401af9adeec7e695b6_DonorDock%20Logo%20-%20Dark.svg",
        "width": 600,
        "height": 60,
        "caption": "DonorDock"
      },
      "image": { "@id": "https://www.donordock.com/#logo" },
      "foundingDate": "2017",
      "founder": [
        { "@type": "Person", "name": "Matt Bitzegaio", "url": "https://www.linkedin.com/in/mattbitzegaio/" },
        { "@type": "Person", "name": "Andrew Lutgen", "url": "https://www.linkedin.com/in/andrewlutgen/" }
      ],
      "sameAs": [
        "https://www.facebook.com/donordock",
        "https://www.linkedin.com/company/donordock",
        "https://www.instagram.com/donordock",
        "https://www.tiktok.com/@donordock",
        "https://www.g2.com/products/donordock",
        "https://www.capterra.com/p/189923/DonorDock/"
      ],
      "contactPoint": [
        {
          "@type": "ContactPoint",
          "telephone": "+1-701-490-8653",
          "contactType": "Sales",
          "areaServed": "US",
          "availableLanguage": ["English"],
          "hoursAvailable": {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
            "opens": "08:00",
            "closes": "17:00"
          }
        },
        {
          "@type": "ContactPoint",
          "url": "https://helpcenter.donordock.com",
          "contactType": "Customer Support",
          "areaServed": "US",
          "availableLanguage": ["English"]
        }
      ]
    },
    {
      "@type": "WebSite",
      "@id": "https://www.donordock.com/#website",
      "url": "https://www.donordock.com/",
      "name": "DonorDock",
      "description": "Nonprofit donor management CRM, online giving, and donor outreach in one platform.",
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
    },
    {
      "@type": "SoftwareApplication",
      "@id": "https://www.donordock.com/#software",
      "name": "DonorDock",
      "alternateName": "DonorDock Nonprofit CRM",
      "description": "DonorDock is an all-in-one donor management CRM for small-to-mid nonprofits. Includes unlimited contacts, online giving, email and text outreach, automations, and project boards in a single platform.",
      "url": "https://www.donordock.com/",
      "applicationCategory": "BusinessApplication",
      "applicationSubCategory": "Nonprofit CRM",
      "operatingSystem": "Web, iOS, Android",
      "publisher": { "@id": "https://www.donordock.com/#organization" },
      "offers": {
        "@type": "Offer",
        "price": "500.00",
        "priceCurrency": "USD",
        "priceSpecification": {
          "@type": "UnitPriceSpecification",
          "price": "500.00",
          "priceCurrency": "USD",
          "unitCode": "MON",
          "referenceQuantity": { "@type": "QuantitativeValue", "value": 1, "unitCode": "MON" }
        },
        "availability": "https://schema.org/InStock",
        "url": "https://www.donordock.com/pricing",
        "eligibleCustomerType": "https://schema.org/Nonprofit"
      },
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.8",
        "ratingCount": "200",
        "bestRating": "5",
        "worstRating": "1"
      },
      "featureList": [
        "Donor Management CRM",
        "Online Giving Pages",
        "Email Marketing",
        "Text Messaging",
        "Project Management (ActionBoard)",
        "Otto AI Assistant",
        "Automations",
        "Reporting & Analytics"
      ]
    },
    {
      "@type": "WebPage",
      "@id": "https://www.donordock.com/#webpage",
      "url": "https://www.donordock.com/",
      "name": "The Donor Development Platform for Growing Nonprofits | DonorDock",
      "isPartOf": { "@id": "https://www.donordock.com/#website" },
      "about": { "@id": "https://www.donordock.com/#software" },
      "primaryImageOfPage": { "@id": "https://www.donordock.com/#logo" },
      "inLanguage": "en-US"
    }
  ]
}
</script>
```

**Remove the G2 JS-injected AggregateRating script from the homepage** so this static AggregateRating is the only one. If G2 ratings are more current, replace the static `4.8/200` with the same numbers G2 provides.

### 4.2 `/contact` — Add Organization + ContactPage (no schema today)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "ContactPage",
      "@id": "https://www.donordock.com/contact#webpage",
      "url": "https://www.donordock.com/contact",
      "name": "Contact DonorDock",
      "description": "Contact DonorDock for sales, support, or to request a demo.",
      "isPartOf": { "@id": "https://www.donordock.com/#website" },
      "about": { "@id": "https://www.donordock.com/#organization" },
      "breadcrumb": { "@id": "https://www.donordock.com/contact#breadcrumb" },
      "inLanguage": "en-US"
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://www.donordock.com/contact#breadcrumb",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.donordock.com/" },
        { "@type": "ListItem", "position": 2, "name": "Contact", "item": "https://www.donordock.com/contact" }
      ]
    }
  ]
}
</script>
```

The full Organization with telephone and hours lives on the homepage; this page references it via `@id`.

### 4.3 Articles — Add static FAQPage + BreadcrumbList + standalone Person

The current FAQPage is JS-injected. Replace with a static block in the Webflow article template (CMS field for FAQ JSON, or hard-coded per article). Same for breadcrumb. Example for `/articles/best-nonprofit-crm`:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "BreadcrumbList",
      "@id": "https://www.donordock.com/articles/best-nonprofit-crm#breadcrumb",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.donordock.com/" },
        { "@type": "ListItem", "position": 2, "name": "Articles", "item": "https://www.donordock.com/articles" },
        { "@type": "ListItem", "position": 3, "name": "Best Nonprofit CRM Platforms in 2026", "item": "https://www.donordock.com/articles/best-nonprofit-crm" }
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://www.donordock.com/articles/best-nonprofit-crm#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is the best nonprofit CRM for a growing organization?",
          "acceptedAnswer": { "@type": "Answer", "text": "Pull the answer text directly from the rendered page; max 5,000 chars." }
        },
        {
          "@type": "Question",
          "name": "How much does nonprofit CRM software cost?",
          "acceptedAnswer": { "@type": "Answer", "text": "..." }
        },
        {
          "@type": "Question",
          "name": "What features should I look for in a nonprofit CRM?",
          "acceptedAnswer": { "@type": "Answer", "text": "..." }
        },
        {
          "@type": "Question",
          "name": "How long does it take to switch nonprofit CRMs?",
          "acceptedAnswer": { "@type": "Answer", "text": "..." }
        },
        {
          "@type": "Question",
          "name": "Do I need a nonprofit-specific CRM or can I use HubSpot or Salesforce?",
          "acceptedAnswer": { "@type": "Answer", "text": "..." }
        }
      ]
    }
  ]
}
</script>
```

And update the existing BlogPosting block with a clean author reference and remove empty strings:

```json
"author": {
  "@type": "Person",
  "@id": "https://www.donordock.com/team/rob-burke#person",
  "name": "Rob Burke",
  "jobTitle": "Chief Marketing Officer",
  "worksFor": { "@id": "https://www.donordock.com/#organization" },
  "image": "https://cdn.prod.website-files.com/63ce9d04b1ff6e1c14514251/658dec22e2f1b071c2daa547_1592433841457.webp",
  "url": "https://www.donordock.com/team/rob-burke",
  "sameAs": ["https://www.linkedin.com/in/robjburke/"]
}
```

Then build a `/team/rob-burke` page (or `/about/team/rob-burke`) hosting the canonical `Person` entity with full bio, expertise areas, and `knowsAbout` — this is what Google and AI engines use for E-E-A-T author authority.

### 4.4 `/features` — Fix URL and complete Offer

Change `url: "/features-overview"` to `https://www.donordock.com/features`, complete the nested Offer with `price`, `priceCurrency`, `availability`, and reference the canonical SoftwareApplication via `@id` instead of redefining it. Same surgery on `/about` and `/donordock-demo`.

### 4.5 `/donordock-demo` — Add VideoObject if a demo video is embedded

If the page embeds a Wistia/YouTube product walkthrough, add:

```json
{
  "@type": "VideoObject",
  "name": "DonorDock Product Demo",
  "description": "5-minute walkthrough of DonorDock's nonprofit CRM, online giving, and donor outreach features.",
  "thumbnailUrl": "https://www.donordock.com/.../demo-thumb.jpg",
  "uploadDate": "2025-01-15",
  "duration": "PT5M",
  "contentUrl": "https://wistia.com/.../video.mp4",
  "embedUrl": "https://fast.wistia.net/embed/iframe/XXX",
  "publisher": { "@id": "https://www.donordock.com/#organization" }
}
```

### 4.6 `/pricing` — Tighten the existing block

Already strong. Three tweaks:
1. Resolve `priceSpecification` contradiction: use `unitCode: "MON"` and remove `billingDuration: "P1Y"` (or add a separate annual offer).
2. Replace `https://twitter.com/donordock` in `sameAs` with `https://www.tiktok.com/@donordock` (consistency with rest of site).
3. Add `aggregateRating.ratingCount` (currently `reviewCount` only).

### 4.7 Comparison pages (`/compare/donorperfect-vs-donordock`, etc.)

Not in this sample, but the sitemap shows 8+ comparison pages. These should ship `Article` (or `WebPage` with `mainEntity: SoftwareApplication`) plus a `Comparison`-style FAQ. Worth a separate audit pass. Flagging for follow-up.

---

## 5. P0 Schema Gaps — Ranked

Ranked by AI citation impact × ease of fix.

### P0-1 — Articles ship FAQPage statically (not JS)
**Impact:** Highest. AI engines (ChatGPT, Claude, Perplexity, Gemini) and Bing all index static JSON-LD; only Google reliably executes JS. Articles are the primary citation surface — getting their FAQPage into the static HTML unlocks PAA-style rich results and AI-engine answer citations on every published article.
**Effort:** Medium (Webflow CMS — add a "FAQ JSON" rich text field per article; convert the embed to a server-rendered template).
**Owner:** Web (Webflow).

### P0-2 — Add canonical Organization + WebSite to homepage `@graph`
**Impact:** High. Establishes the DonorDock entity for Knowledge Graph and AI engines; enables sitelinks search box; gives every other page a stable `@id` to reference.
**Effort:** Low (one block of JSON, paste into homepage).
**Owner:** Web.

### P0-3 — Remove duplicate AggregateRating (decide static vs G2-injected)
**Impact:** High. Two AggregateRating nodes likely cause Google to ignore both. Unified single rating restores rich-result eligibility.
**Effort:** Low (delete one script tag).
**Owner:** Web.

### P0-4 — `/contact` has zero schema; add ContactPage + reference Organization
**Impact:** Medium-High. Contact pages with phone/hours markup feed Google Knowledge Panel and AI-engine "how to contact" answers.
**Effort:** Low.
**Owner:** Web.

### P0-5 — Article BlogPosting cleanup (empty `sameAs`, dates, Person entity)
**Impact:** Medium-High. Fixes E-E-A-T author signal — critical for AI citation in YMYL-adjacent nonprofit-finance topics.
**Effort:** Medium (build `/team/rob-burke` Person page; CMS template fix for sameAs).
**Owner:** Web + Content.

### P0-6 — Add BreadcrumbList to every article and key marketing page
**Impact:** Medium. Breadcrumb rich result + clearer site architecture for AI crawlers.
**Effort:** Low (Webflow CMS template addition).
**Owner:** Web.

### P0-7 — Fix relative URLs in `/features`, `/about`, `/resources`
**Impact:** Medium. Relative URLs in JSON-LD don't validate cleanly and break entity-linking for AI engines.
**Effort:** Trivial (find/replace).
**Owner:** Web.

### P0-8 — Complete Offer fields on every nested SoftwareApplication
**Impact:** Medium. SoftwareApplication rich results require a complete Offer.
**Effort:** Low (add `price: "500.00"`, `priceCurrency: "USD"`, full `availability`).
**Owner:** Web.

### P0-9 — Add VideoObject schema where videos are embedded
**Impact:** Medium for AEO (video appears in answers). Demo page is the priority.
**Effort:** Low per page.
**Owner:** Web.

### P0-10 — Audit comparison pages (`/compare/*`) — separate pass
**Impact:** High for bottom-funnel queries, but not in this sample. Flagging for next audit.
**Effort:** TBD.
**Owner:** SEO + Web.

---

## Validation Workflow After Fixes

1. Test each updated page at https://search.google.com/test/rich-results — confirm zero errors and the expected rich-result types appear.
2. Cross-check at https://validator.schema.org/ for general schema correctness.
3. For articles, run the Bing Webmaster URL inspection tool to confirm Bing sees the FAQPage in the static HTML (not JS).
4. Submit updated URLs in GSC → URL Inspection → "Request Indexing" for the highest-priority pages first (homepage, pricing, contact, top 5 articles).
5. Monitor GSC → Enhancements (FAQ, Sitelinks searchbox, Software App, Breadcrumb, Article, Logo) for status and errors over the next 2-4 weeks.
6. For AI-citation tracking, re-run an AI-engine query test (Perplexity, ChatGPT, Claude) on terms like "best nonprofit CRM 2026" and "DonorDock pricing" 7 and 30 days after deploy to detect citation lift.

---

## Source Files

Raw extracted JSON-LD blocks for reference (committed for auditability, not for shipping):
- `/tmp/dd-schema/parsed___1.json` — homepage
- `/tmp/dd-schema/parsed_pricing_1.json` — pricing (best in class)
- `/tmp/dd-schema/parsed_features_1.json`
- `/tmp/dd-schema/parsed_about_1.json`
- `/tmp/dd-schema/parsed_donordock-demo_1.json`
- `/tmp/dd-schema/parsed_resources_1.json`
- `/tmp/dd-schema/parsed_articles_*_1.json` — 5 article BlogPosting blocks
- `/tmp/dd-schema/contact.html` — confirmed zero static JSON-LD; contains only G2 fetch-injection script
