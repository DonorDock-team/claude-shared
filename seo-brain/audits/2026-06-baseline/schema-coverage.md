# DonorDock Schema (JSON-LD) Coverage Audit
**Site:** https://donordock.com
**Audit date:** 2026-06-01
**Auditor:** claude-rank Schema Auditor (Rob Burke / DonorDock)
**Prior baseline:** [../2026-05-baseline/schema-coverage.md](../2026-05-baseline/schema-coverage.md)
**Pages sampled:** 14 (homepage, /pricing, /features, /about, /contact, /donordock-demo, /resources, 5 article pages, 2 compare pages)
**Method:** Direct HTML fetch (Chrome desktop UA) + regex extraction of every `<script type="application/ld+json">` block. Each block parsed with `JSON.parse` and `@type` enumerated recursively (including `@graph`). JS-injected schema flagged separately by isolating `createElement`/IIFE patterns from genuine static blocks. This month adds two `/compare/*` pages per the P0-10 follow-up.

---

## 1. Executive Summary

- **Coverage trend: flat-to-slightly-improved. The four critical issues flagged in May are all still OPEN.** None of the P0-1 through P0-4 items shipped. Two small wins did land: `/pricing` now carries a top-level `WebSite` node inside its `@graph`, and article `datePublished`/`dateModified` are now distinct (no longer identical templated timestamps). Everything else holds at the May baseline.
- **`/pricing` remains the gold-standard template and is fully intact** — the same five-node `@graph` (Organization, SoftwareApplication, FAQPage, BreadcrumbList, WebPage) parses clean. No other page has been brought up to this level.
- **The #1 AI-citation blocker is unchanged: article FAQPage is still built client-side.** Every sampled article ships exactly one static `BlogPosting` block; the `FAQPage` is still assembled at runtime by a Webflow-embed IIFE that scrapes `.uui-faq01_component` blocks and `document.createElement('script')`s the schema into the head. It remains invisible to GPTBot, ClaudeBot, CCBot, PerplexityBot, and Bingbot across 281+ articles. This is still the single biggest AI-citation lift on the site.
- **New finding (P0-10 follow-up): `/compare/bloomerang-vs-donordock` has a broken JSON-LD block.** A trailing comma in the `featureList` array (`"Unlimited Contacts",\n    ]`) makes the entire block fail `JSON.parse` — so Google, Bing, and every AI crawler drop ALL schema on that page. `/compare/givebutter-vs-donordock` by contrast is well-formed (WebPage + SoftwareApplication + Offer + ItemList). The compare cluster is inconsistent and one page is fully broken.

---

## 2. Coverage Summary & Trend

| Metric | 2026-05 | 2026-06 | Trend |
|---|---|---|---|
| Pages sampled | 11 | 14 | +3 (added 2 compare pages, expanded) |
| Pages with valid static JSON-LD | 9 / 11 | 11 / 14 | ↑ count, but `/contact` still 0 and `/compare/bloomerang` now broken |
| Gold-standard `@graph` pages | 1 (`/pricing`) | 1 (`/pricing`) | → flat |
| Pages with top-level `WebSite` | 0 | 1 (`/pricing`) | ↑ slight |
| Pages with `SearchAction` (sitelinks box) | 0 | 0 | → still none |
| Articles with **static** FAQPage | 0 / 5 | 0 / 5 | → **OPEN** |
| Pages with duplicate (static + G2-JS) AggregateRating | 4 | 4 | → **OPEN** |
| `/contact` static schema | none | none | → **OPEN** |
| Broken/unparseable JSON-LD blocks | 0 | 1 (`/compare/bloomerang`) | ↓ regression |
| Relative-URL errors (`/features`, `/about`, `/resources`) | 3 | 3 | → unfixed |

**Overall grade: C+ (unchanged from May).** `/pricing` is an A; the long tail (articles, contact, compare) drags the site average down. No P0 closed this month.

---

## 3. Schema Inventory Matrix

Schema present in the **static HTML** at fetch time. JS-injected schema noted with `(JS)`.

| Page | Org | WebSite | WebPage | SoftwareApp | Offer | Aggregate Rating | FAQPage | Breadcrumb | Article/BlogPosting | Author | Service | ItemList | Notes |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|---|
| `/` | nested | — | yes | nested | minimal | yes (static)+(JS dup) | — | — | — | — | — | — | Still one shallow WebPage; no top-level Org/WebSite |
| `/pricing` | yes | **yes (new)** | yes | yes | full | yes (static)+(JS dup) | yes | yes | — | nested Person | — | — | **Best-in-class @graph (5 nodes), intact; WebSite added** |
| `/features` | nested | — | yes | nested | thin | — +(JS only) | — | — | — | — | — | — | `url` still `/features-overview` (wrong + relative) |
| `/about` | nested | — | AboutPage | nested | thin | yes (static)+(JS dup) | — | — | — | — | — | — | Top url still `/about` (relative); Org url missing |
| `/contact` | — (G2 JS only) | — | — | — | — | (JS only) | — | — | — | — | — | — | **Still zero static JSON-LD** |
| `/donordock-demo` | nested | — | yes | nested | thin | yes (static)+(JS dup) | — | — | — | — | yes | — | Service node good; FAQ-inject pattern also present |
| `/resources` | yes | — | CollectionPage | nested+hasPart | thin | (JS only) | — | — | — | — | — | — | `url` still `/tools` (relative + wrong) |
| `/compare/bloomerang-vs-donordock` | — | — | — | — | — | — | — | — | — | — | — | — | **BROKEN — trailing comma, whole block fails JSON.parse** |
| `/compare/givebutter-vs-donordock` | — | — | yes | yes | yes | yes (static)+(JS dup) | — | — | — | — | — | yes | Well-formed; ItemList comparison table — good |
| `/articles/best-nonprofit-crm` | nested | — | nested mainEntityOfPage | — | — | (JS only) | **(JS only)** | — | yes | yes | — | — | FAQPage still JS-injected |
| `/articles/lapsed-donor-re-engagement-playbook` | nested | — | nested | — | — | (JS only) | **(JS only)** | — | yes | yes | — | — | FAQPage JS-injected |
| `/articles/grassroots-fundraising-playbook-new-nonprofits` | nested | — | nested | — | — | (JS only) | **(JS only)** | — | yes | yes | — | — | FAQPage JS-injected |
| `/articles/why-fundraisers-under-ask-...` | nested | — | nested | — | — | (JS only) | **(JS only)** | — | yes | yes | — | — | FAQPage JS-injected |
| `/articles/how-to-build-corporate-sponsor-pipeline-nonprofit` | nested | — | nested | — | — | (JS only) | **(JS only)** | — | yes | yes | — | — | FAQPage JS-injected |

Legend: "yes" = present and well-formed in static HTML. "nested" = present only inside another type. "(JS)" = injected client-side. "—" = absent.

---

## 4. Re-Verification of Critical Prior Findings

These four were the May #1 P0 and the other top-priority items. Each re-checked against the live HTML this run.

### 4.1 Article FAQPage (was JS-injected) — **STILL OPEN**
Every sampled article ships exactly **one** static `ld+json` block, containing only `BlogPosting` (+ nested ImageObject, Person, Organization, WebPage, SpeakableSpecification), length ~2,025 bytes. The `FAQPage` text appears only inside an inline JavaScript IIFE:
```js
mainEntity.push({ "@type":"Question", "name":qText, "acceptedAnswer":{ "@type":"Answer","text":aText } });
...
var schema = { "@context":"https://schema.org","@type":"FAQPage","mainEntity":mainEntity };
... document.createElement('script') ... // appended at runtime
```
This is byte-for-byte the same runtime construction flagged in May. **Status: OPEN. Invisible to GPTBot / ClaudeBot / CCBot / PerplexityBot / Bingbot on all 281+ articles.** Still the highest-value fix on the site.

### 4.2 Duplicate G2-injected AggregateRating — **STILL OPEN (not deduplicated)**
Home, /pricing, /about, /donordock-demo each carry exactly **1 static `AggregateRating` node (4.8 / 200)** AND a live G2 fetch-and-inject script that adds a second rating to the DOM at runtime. Two competing AggregateRating values still coexist on the same page — the condition Google warns can suppress the rich result entirely. No deduplication shipped. `/features` and `/contact` still have no static rating (G2-JS only).

### 4.3 `/contact` static JSON-LD — **STILL OPEN**
Precise extraction returns **0 static `ld+json` blocks**. Phone `(701) 490-8653` and Mon–Fri 8–5 CST hours remain in visible text but unmarked. Only the G2 fetch-injection script is present. No `ContactPage`, no `LocalBusiness`, no `Organization`.

### 4.4 `/pricing` gold-standard `@graph` — **INTACT (+ improved)**
The single `@graph` block parses clean with all 5 linked nodes: `Organization`, `SoftwareApplication`, `FAQPage`, `BreadcrumbList`, `WebPage`. **Improvement:** a top-level `WebSite` node is now present in the page's markup (the only page on the site with one). Still missing `SearchAction` for the sitelinks search box.

---

## 5. Delta vs 2026-05 Baseline

### Improvements (✅)
- **`/pricing` gained a `WebSite` node** — first WebSite schema anywhere on the site (partial progress on P0-2, but on pricing rather than the canonical homepage).
- **Article dates de-templated** — `datePublished` (2026-05-11T...) and `dateModified` (2026-05-06T...) are now distinct, resolving the "identical timestamp" warning from May §3.2.
- **Compare-page audit completed** (P0-10) — `/compare/givebutter-vs-donordock` is well-formed with a useful `ItemList` comparison node.

### Regressions / New (🔴)
- **`/compare/bloomerang-vs-donordock` JSON-LD is broken** — trailing comma in `featureList` (`"Unlimited Contacts",\n    ]`) fails `JSON.parse`. The page's entire schema is dropped by all crawlers. New P0.
- **Compare cluster is inconsistent** — one page broken, one clean; no shared template.

### Unchanged / still OPEN (⏸)
- P0-1 article static FAQPage — OPEN
- P0-2 homepage canonical Organization + WebSite — OPEN (homepage still has neither top-level)
- P0-3 duplicate AggregateRating dedup — OPEN
- P0-4 `/contact` schema — OPEN
- P0-5 article `author.sameAs` still `["...robjburke/","","",""]` (3 empty strings — invalid) — OPEN
- P0-6 BreadcrumbList on articles — OPEN (none present)
- P0-7 relative/wrong URLs: `/features` → `/features-overview`, `/about` → `/about`, `/resources` → `/tools` — all unchanged, OPEN
- P0-8 incomplete nested Offers (no `price`) — OPEN
- P0-9 VideoObject on demo — OPEN

**Net: 3 small wins, 1 new regression, 9 P0s carried forward. No P0 fully closed.**

---

## 6. Validation Errors & Warnings (current)

### 6.1 Errors
| Page | Schema | Issue | Severity |
|---|---|---|---|
| `/compare/bloomerang-vs-donordock` | (whole block) | Trailing comma in `featureList` array → `JSON.parse` fails → all schema ignored sitewide-crawler. | error (NEW) |
| `/contact` | (none) | Zero static JSON-LD. Phone + hours unmarked. | error |
| `/features` | WebPage `url` | `url: "/features-overview"` (relative + wrong slug). | error |
| `/about` | AboutPage / Organization | Top `url: "/about"` relative; nested Org `url` absent. | error |
| `/resources` | CollectionPage `url` | `url: "/tools"` relative + wrong (page is `/resources`). | error |
| Home, /features, /demo, /about | Offer (nested) | Offers missing `price` (and others missing `priceCurrency`). SoftwareApplication offer incomplete. | error |
| All rated pages | AggregateRating | Static + G2-JS = two AggregateRating nodes; duplicate risks suppression. | error |
| Articles (×5) | FAQPage | JS-injected; invisible to non-JS crawlers (Bing + all AI bots). | error (AEO/GEO) |

### 6.2 Warnings
| Page | Schema | Issue |
|---|---|---|
| Articles (×5) | `author.sameAs` | Still contains 3 empty strings — invalid per schema.org. |
| Homepage | Organization | Still buried in `WebPage > about > SoftwareApplication > provider`; not a top-level entity. |
| Home / all | WebSite + SearchAction | Homepage has no WebSite; no page has `SearchAction` → no sitelinks search box. |
| `/pricing` | Offer | `priceSpecification` month/year unit contradiction still present (per May §3.2). |
| All | logo URL | Two different logo URLs across pages (CDN svg vs `/images/logo.svg`) — not unified. |
| Articles (×5) | BlogPosting | No BreadcrumbList, no `wordCount`/`articleBody`, no standalone `Person` entity for author E-E-A-T. |

---

## 7. P0 Schema Gaps — Ranked (carried forward + new)

Ranked by AI-citation impact × ease of fix.

### P0-1 — Ship article FAQPage statically (not JS) — **OPEN, top priority**
Highest AI-citation lift. Convert the Webflow FAQ embed to a server-rendered per-article `FAQPage` JSON field. Owner: Web (Webflow). Effort: Medium.

### P0-2 — Add canonical Organization + WebSite to homepage `@graph` — **OPEN**
`/pricing` now proves the WebSite block works — replicate it at the homepage as the canonical site entity, give it an `@id` every page references, and add `SearchAction`. Owner: Web. Effort: Low.

### P0-3 — Remove duplicate AggregateRating — **OPEN**
Decide static vs G2-injected; delete one. Owner: Web. Effort: Low.

### P0-4 — `/contact` ContactPage + Organization reference — **OPEN**
Mark phone/hours; reference the canonical Org. Owner: Web. Effort: Low.

### P0-NEW — Fix `/compare/bloomerang-vs-donordock` broken JSON-LD — **NEW**
Remove the trailing comma in `featureList`; then standardize all 9+ compare pages on the clean `/compare/givebutter` template. Validate every compare page. Owner: Web. Effort: Trivial (the fix) + Low (templating).

### P0-5 — Article BlogPosting cleanup (empty `sameAs`, Person entity) — **OPEN** (dates now fixed ✅)

### P0-6 — BreadcrumbList on every article + key marketing page — **OPEN**

### P0-7 — Fix relative/wrong URLs (`/features`, `/about`, `/resources`) — **OPEN**

### P0-8 — Complete nested Offer fields (`price`, `priceCurrency`) — **OPEN**

### P0-9 — VideoObject on `/donordock-demo` and video articles — **OPEN**

---

## 8. Validation Workflow After Fixes

1. Re-run each updated page at https://search.google.com/test/rich-results — confirm zero errors and expected rich-result types.
2. Cross-check at https://validator.schema.org/.
3. For articles + `/compare/bloomerang`, run Bing Webmaster URL inspection to confirm the schema is in the **static** HTML (not JS).
4. GSC → URL Inspection → Request Indexing for homepage, contact, broken compare page, top 5 articles first.
5. Monitor GSC → Enhancements (FAQ, Sitelinks searchbox, Software App, Breadcrumb, Article, Merchant/Review) over 2–4 weeks.
6. Re-run AI-engine citation tests (Perplexity, ChatGPT, Claude) on "best nonprofit CRM 2026" and "DonorDock vs Bloomerang" 7 and 30 days post-deploy.

---

## Source Files
Raw fetched HTML committed for auditability under `/tmp/dd-schema-jun/`:
- `home.html`, `pricing.html` (gold standard, now +WebSite), `features.html`, `about.html`, `contact.html` (0 static blocks), `donordock-demo.html`, `resources.html`
- `art_*.html` (5 articles — BlogPosting static, FAQPage JS-only)
- `cmp_bloomerang-vs-donordock.html` (broken JSON-LD), `cmp_givebutter-vs-donordock.html` (clean)
