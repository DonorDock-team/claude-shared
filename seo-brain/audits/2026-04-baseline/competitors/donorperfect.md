# DonorPerfect — Competitive SEO Audit (Phase 1 Baseline)

**Audit Date:** 2026-04-22
**Prepared for:** DonorDock seo-brain strategist system
**Competitor URL:** https://www.donorperfect.com
**Benchmarked against:** https://www.donordock.com
**Method:** rank-compete skill + live crawl of robots.txt, sitemap indexes, homepage schema, blog sitemap, comparison page corpus, SERP reconnaissance.

---

## 1. Executive Summary

- **Scale gap is real but narrowing.** DonorPerfect carries ~648 blog posts, 157 static pages, 12-segment sitemap, and a 20-year domain history claiming 75,000 nonprofit professionals / 11,000 orgs. DonorDock shows a leaner ~619 URL sitemap but still smaller blog footprint, younger domain, and no glossary infrastructure.
- **Topical authority is concentrated in "fundraising-software" (265 posts) and "featured" (104 posts).** DonorPerfect has gone wide on fundraising strategy and narrow-deep on product-led SEO, but content is almost entirely unattributed — no author bylines, no E-E-A-T credentialing, no reviewedBy markup.
- **Schema posture is minimal.** Only Yoast's default graph runs on the homepage: WebPage, WebSite, Organization, BreadcrumbList, ImageObject. No SoftwareApplication, no AggregateRating, no FAQPage, no Product — all of which DonorDock could adopt quickly to leapfrog them in AI Overviews and rich results.
- **AI/LLM access policy is wide-open and unmanaged.** robots.txt allows all crawlers, no Google-Extended / GPTBot / ClaudeBot / Applebot-Extended / CCBot directives, no llms.txt. By contrast DonorDock explicitly blocks ClaudeBot, GPTBot, Google-Extended, CCBot, Applebot-Extended, Bytespider, Amazonbot, meta-externalagent. That is a strategic fork: DonorPerfect is being trained on; DonorDock is not. Rob needs to decide which side of that to be on for GEO.
- **DonorPerfect publishes a `/fundraising-software/compare-donor-management-systems/{competitor}/` bottom-of-funnel program (Keela, Bloomerang, Raiser's Edge, Salesforce, Kindful) but does NOT publish a DonorDock page.** This is the single biggest short-term SEO/SERP opportunity: DonorDock already ranks for "DonorPerfect vs DonorDock" with its own `/compare/donorperfect-vs-donordock` page, uncontested by DonorPerfect.

---

## 2. Positioning & ICP Overlap vs DonorDock

| Dimension | DonorPerfect | DonorDock | Overlap / Gap |
|---|---|---|---|
| H1 | "We make it easy to do good." | "Built for lean nonprofit teams" | Both position around ease. DonorDock is sharper on ICP. |
| Tagline | "Nonprofits raise 25% more funds in their first year using DonorPerfect" | "The Donor Development Platform for Growing Nonprofits" | DonorPerfect leads with a proof point; DonorDock with a category. |
| Claimed scale | 75,000 professionals / 11,000 orgs / 25+ sectors | 7,200+ users | DonorPerfect uses social-proof scale. DonorDock trails on this lever. |
| Pricing transparency | Three tiers (Core / Plus / Pro) — **no prices shown**, quote-to-reveal. Starts at ~$450/mo. | Single plan at $500/mo, 1% platform fee | **DonorDock wins on transparency** — a strong E-E-A-T + trust signal. |
| ICP | Broad: 0–500 up to 200,001+ constituents. Mid-market to enterprise-leaning. | Small-to-mid lean teams. Spreadsheet-upgraders. | **Clear positioning gap.** DonorPerfect is "do-everything". DonorDock's under-50-donor through 5,000-donor sweet spot is where DonorPerfect is weakest on fit. |
| AI story | "Fundraising AI" / "Fundraiser Bot" content generation | "Otto" intelligence — gift tracking, smart comms, recurring mgmt | Roughly parity in feature narrative; DonorPerfect's AI is generative/content, DonorDock's is operational/workflow. |
| Modularity | Modular — add-ons for auctions, crowdfunding, moves mgmt, QuickBooks tier-gated | All-in-one, one plan | **DonorDock's strongest competitive wedge.** |

**ICP Overlap:** Meaningful overlap in the 50–1,000 donor mid-small band. Below 50 donors DonorPerfect is overbuilt and overpriced; above 5,000 donors DonorPerfect's modular + custom-field + API-Pro tier starts to advantage them.

---

## 3. Organic SEO Footprint

**Content volume (from sitemap index, 2026-04-21):**

| Asset | URL Count | Last Modified |
|---|---:|---|
| Blog posts (`nonprofit-technology-blog/post-sitemap.xml`) | **648** | 2026-04-21 |
| Static pages (`page-sitemap.xml`) | 157 | 2026-04-21 |
| Glossary terms (`glossary-term-sitemap.xml`) | 7 | 2026-04-21 |
| Client success stories | present | 2025-12-29 |
| Factsheets | present | 2026-03-26 |
| Whitepapers | present | 2026-04-21 |
| Videos | present | 2026-04-15 |
| Integrations | present | 2026-03-27 |
| **DonorDock sitemap (total URLs)** | **619** | — |

**Blog category concentration:**

| Category slug | Post count |
|---|---:|
| fundraising-software | 265 |
| featured | 104 |
| donorperfect | 68 (product/brand-led) |
| fundraising-strategies | 56 |
| nonprofit-technology | 31 |
| givingtuesday | 31 |
| nonprofit-news | 30 |
| donorperfect-community-network-conference | 14 |
| monthly-giving | 12 |
| donor-management-software | 11 |

**Notable keyword signals / recently published:**
- "Digital Wallets for Nonprofits" (2026-04-13)
- "How to Talk About Donor-Advised Funds Amid the 2026 Tax Changes" (2026-04-10)
- "5 Donor Segments As You Adapt to 2026 Tax Changes" (2026-04-09)
- "QR Codes for Nonprofits: 7 Ways to Send Supporters to Your Donation Form" (2026-03-11)
- "40 Monthly Giving Program Names" (2026-03-02)
- "Impact Stories that Inspire Generosity" (2026-02-27)

**Topical authority assessment:**
- **Strong:** fundraising strategy, monthly giving, major donor cultivation, end-of-year campaigns, Giving Tuesday, nonprofit reporting, Form 990 / compliance.
- **Medium:** online fundraising, payment tech, integrations.
- **Weak / underserved:** small-team operations, sub-100-donor workflows, getting-started content for new nonprofits, migration-from-spreadsheet content, AI-for-small-teams. **All are DonorDock wedges.**

**Publishing cadence:** 1–3 posts/week, consistent. Rob should expect to meet or beat a 2/week cadence to catch up within 12 months.

---

## 4. Technical SEO Posture

### robots.txt
- **User-agent:** `*`
- **Disallow:** (empty) — full crawl access
- **No AI bot directives** — no blocks or allows for GPTBot, ClaudeBot, ChatGPT-User, PerplexityBot, Google-Extended, anthropic-ai, CCBot, Applebot-Extended, Bytespider, Amazonbot, meta-externalagent.
- **Sitemaps listed:** 4 (main, blog, integrations + index)
- **Verdict:** open season for AI training. No Cloudflare content-signal block, no llms.txt. DonorPerfect is training-data rich.

### Sitemap
- Yoast-generated, segmented by post type (post, page, ofh_articles, client-success-story, factsheet, video, whitepaper, glossary-term, blog post, blog page, integrations post, integrations page).
- **Positive:** clean segmentation helps crawl efficiency.
- **Gap:** no image-sitemap or news-sitemap presence noted in the index.

### Canonical / Meta
- Homepage: `<link rel="canonical" href="https://www.donorperfect.com/" />` — clean.
- Title: "Fundraising Software for NonProfit Donor Management" (well-keyworded but generic).
- Meta description: "Nonprofits use DonorPerfect Fundraising Software for their Donor Management, Grant & Gift Tracking, Moves Management, Mass Mailing needs and more" — under 160 chars, serviceable but lacks differentiator or CTA.
- Open Graph: present (`og:type=website`, `og:title`, `og:description`, `og:url`, `og:site_name`).
- **Gap:** no clear hreflang implementation despite international presence (CA-FR, CA-EN, AU).

### Schema Markup Presence + Validity
Only **one** JSON-LD graph detected on homepage (Yoast default), containing:

| @type | Present | Notes |
|---|---|---|
| WebPage | Yes | with datePublished + dateModified |
| WebSite | Yes | with SearchAction |
| Organization | Yes | with logo, telephone, sameAs (10 profile links inc. G2, Capterra, SoftwareAdvice), numberOfEmployees 201–500 |
| BreadcrumbList | Yes | minimal — Home only on homepage |
| ImageObject | Yes (x2) | primary image + logo |
| **SoftwareApplication** | **No** | **major gap** |
| **Product** | **No** | **major gap** |
| **AggregateRating** | **No** | **major gap** — they have G2 reviews linked via sameAs but don't surface star ratings in schema |
| **FAQPage** | **No** | **major gap** for AEO/AIO |
| **Article / BlogPosting** | Not validated on homepage — needs spot-check on blog posts |
| **Person / author** | **No** | blog content has no bylines |
| **Review / reviewedBy** | **No** | |

**Validity:** Yoast schema graph is syntactically well-formed. Problem isn't validity — it's completeness.

### Key technical gaps to exploit
1. No SoftwareApplication + AggregateRating = no star-rich-result eligibility in SERPs.
2. No FAQPage = missing "People Also Ask" hooks for AEO.
3. No author schema + no bylines = weak E-E-A-T signal.
4. No llms.txt, no AI-bot directives = zero GEO posture management.

---

## 5. AEO / GEO Signals

| Signal | DonorPerfect | DonorDock |
|---|---|---|
| FAQ schema on homepage | No | (needs audit — flag for Phase 1 own-site report) |
| Author bylines on blog | **No** — 648 posts, zero named authors visible | Mixed — partial (needs audit) |
| Author schema (Person) | Not detected | — |
| Reviewed-by / medically/expert-reviewed | Not detected | — |
| Glossary / definition page program | **Only 7 terms** — underinvested | None today |
| Citation-worthiness (original data, charts, named experts) | **Low** — content is category-standard, rarely cites primary research; lots of "25% more funds" style claims without sourced methodology | Mixed |
| Press/earned-media pages | Testimonials + success stories yes; no pressroom with media pitches | — |
| llms.txt | **Absent** | Absent |
| robots.txt AI-bot policy | **Fully open, unmanaged** | Fully locked (blocks GPTBot, ClaudeBot, Google-Extended, etc.) |
| Video transcripts as indexable text | Some (AI and the Future of Fundraising has a /transcript/ page) | — |

**GEO verdict:** DonorPerfect is broadly citable by AI engines because nothing is blocked, BUT the content is weak on the qualities that make citations stick — no named experts, thin structured data, few original statistics tied to methodology. They're in AI training sets but may not be preferred citations.

**DonorDock's GEO posture today is backwards:** DonorDock blocks the very bots (ClaudeBot, GPTBot, Google-Extended, Applebot-Extended) that need to read the site to cite it in ChatGPT, Claude, Gemini, and Apple Intelligence answers. **This is a critical Phase 1 policy decision for Rob.** Pure privacy-protection blocking excludes DonorDock from AI Overviews and generative-search citations where competitors like DonorPerfect are freely indexed.

---

## 6. Content Strategy Gaps DonorPerfect Exploits (and DonorDock does not)

1. **Year-specific tax / legislation content** — DonorPerfect cranks out "2026 Tax Changes" posts fast; captures timely search surges.
2. **Named fundraising events SEO** — "Giving Tuesday" (31 posts), "End of Year" cluster. DonorPerfect owns seasonal SERPs.
3. **Category tentpole guides** — long-form monthly giving, major donors, donor retention pillars with internal-link spokes.
4. **Competitor migration funnels** — `/landing/utm/switch-and-save-raisersedge/`, "Former Raiser's Edge Customer Now Using DonorPerfect CRM" case studies.
5. **Client success stories as a sitemap type** — dedicated content type with schema-ready segmentation.
6. **Integration-led SEO** — a separate `integrations/` subdomain/path with its own sitemap indexes, targeting keywords like "QuickBooks + donor CRM", "Constant Contact + nonprofit CRM".
7. **Conference/community content** — 14 posts tagged to DPCNC (their user conference) that drive brand-defense SEO and long-tail branded traffic.
8. **Glossary footprint** (small today, 7 terms) — they have the URL structure `/nonprofit-terms-glossary/{term}/` positioned for featured-snippet capture even though underinvested.

---

## 7. Content Gaps DonorPerfect Leaves Open for DonorDock

1. **Growing mid-sized nonprofit content.** DonorPerfect's content assumes a full-time fundraising staff. Rob's ICP ("lean teams who do it all") has almost no organic competition from DonorPerfect at the <100-donor level.
2. **Transparent-pricing content.** DonorPerfect gates pricing. Queries like "DonorPerfect pricing", "DonorPerfect cost", "how much does DonorPerfect cost" are rankable for a transparent competitor — DonorDock should build a fair, factual "DonorPerfect pricing explained" article.
3. **Named author E-E-A-T.** Zero author brand on DonorPerfect. A DonorDock program pairing Matt (CEO) and Rob (CMO) with specific authored articles + LinkedIn cross-linking leapfrogs them on Google's E-E-A-T signals and AI citations.
4. **Migration-from-spreadsheets content.** DonorPerfect targets migration from Raiser's Edge. The long-tail of "Excel to donor CRM", "Google Sheets to donor database", "upgrading from spreadsheets to a real donor CRM" is wide open.
5. **AI-era fundraising operations content.** DonorPerfect has "Fundraising AI / Fundraiser Bot" narrative but thin supporting content. DonorDock can out-publish them on "AI for lean nonprofit teams", "how Otto helps", "AI prompt library for fundraisers".
6. **Citation-quality original data.** Neither has a named "State of Nonprofit Fundraising" or recurring data release with methodology. First mover wins the research-citation slot in AI answers.
7. **Glossary content built for AEO.** DonorPerfect only has 7 glossary URLs. A 60–100-term glossary at `/glossary/{term}` with FAQPage + DefinedTerm schema outranks them on informational intent within 6–9 months.
8. **Video-transcript pages as indexable content.** DonorPerfect has some `/video/{name}/transcript/` pages. DonorDock has Remotion capability but apparently no transcript-indexed strategy yet.

---

## 8. Comparison Pages — Do They Publish /alternatives?

**Yes — but not against DonorDock.**

DonorPerfect publishes competitor comparison pages at the URL pattern:
`https://www.donorperfect.com/fundraising-software/compare-donor-management-systems/{competitor}/`

Confirmed pages (via SERP reconnaissance):
- `/compare-donor-management-systems/keela/`
- `/compare-donor-management-systems/bloomerang/`
- `/compare-donor-management-systems/raisers-edge/`
- `/compare-donor-management-systems/salesforce/`
- (Kindful referenced but page existence not verified)

Plus a UTM-tagged landing page: `/landing/utm/switch-and-save-raisersedge/`

**Structure of the Keela comparison page:**
- Hero + CTA
- "You don't have to fundraise alone" brand narrative
- Feature comparison table (fundraising data, 70+ reports vs Keela's 15 dashboards)
- Customer testimonials
- Support/pricing table ($60/mo Keela support charge called out)
- Lead capture form
- **No JSON-LD schema detected on the comparison page.** Missed opportunity for Product + ComparisonTable markup.

**Critical finding:** **DonorPerfect does not publish a DonorDock comparison page.** They are not defending this keyword. DonorDock already ranks #1 for "DonorPerfect vs DonorDock" with `/compare/donorperfect-vs-donordock`. This is an uncontested SERP.

Third-party comparison sites that currently rank for the DonorDock-vs-DonorPerfect term:
- donordock.com/compare/donorperfect-vs-donordock (#1)
- getapp.com, softwareadvice.com, zeffy.com, g2.com, capterra.com (review aggregators)

---

## 9. Strategic Recommendations for DonorDock (Phase 1)

**1. Policy decision: flip the AI-bot blocking in robots.txt.**
Today DonorDock blocks ClaudeBot, GPTBot, Google-Extended, Applebot-Extended, CCBot, Bytespider, Amazonbot, meta-externalagent. DonorPerfect blocks none. To compete for citations in ChatGPT/Claude/Gemini/Apple Intelligence answers, selectively allow the *reader* bots (ChatGPT-User, ClaudeBot, PerplexityBot, Google-Extended, Applebot-Extended) while keeping training-only crawlers (CCBot, Bytespider) blocked. Publish an llms.txt pointing to canonical product, pricing, and comparison pages.

**2. Ship structured data DonorPerfect is missing.**
Add to DonorDock homepage + product pages:
- `SoftwareApplication` schema (applicationCategory: BusinessApplication, operatingSystem: Web)
- `AggregateRating` (4.8/5, 200+ reviews) — **DonorPerfect has zero rating schema despite having G2/Capterra pages**
- `Offer` with price=$500/mo + priceCurrency=USD (pricing transparency advantage)
- `FAQPage` on homepage and top landing pages (common-question answers)
- `Product` + `Review` for top customer stories
This alone gets star ratings in SERPs that DonorPerfect cannot show.

**3. Launch a glossary program at `/glossary/{term}`.**
Target 60 terms in the first 90 days using `DefinedTerm` + `FAQPage` schema. Beat DonorPerfect's 7-term glossary and capture featured-snippet + AI Overview traffic on informational intent.

**4. Stand up author bylines with Person schema and about/expertise pages.**
DonorPerfect has 648 blog posts with zero attributed authors. Put Matt Bitzegaio and Rob Burke on named articles with `Person` schema, speaking history, LinkedIn sameAs, and `author` + `reviewedBy` markup on evergreen content. This is a defensible E-E-A-T moat DonorPerfect cannot close quickly.

**5. Publish "honest DonorPerfect pricing" + expand the comparison corpus.**
DonorPerfect doesn't publish prices. DonorDock should:
- Add a factual "What does DonorPerfect cost?" article (explain the Core/Plus/Pro tiers, $450 starting price, modular add-ons).
- Defend the current `/compare/donorperfect-vs-donordock` win with FAQPage schema, refreshed G2 data, and video testimonial embeds.
- Mirror DonorPerfect's URL pattern by ensuring `/compare/{competitor}-vs-donordock` is populated for every competitor DonorPerfect targets (Keela, Bloomerang, Raiser's Edge, Salesforce) — DonorDock already publishes several; fill the gaps.

**6. Claim the "lean-team / first-CRM / Excel-upgrade" long tail.**
Build a 12-article pillar covering "spreadsheet to donor CRM", "donor database for growing nonprofit", "under 100 donors CRM", "volunteer-run nonprofit fundraising tools". DonorPerfect has near-zero coverage here and cannot pivot without abandoning their mid-market narrative.

**7. Ship an annual original-data release.**
"DonorDock State of the Lean Nonprofit Fundraiser — 2026 Report" with methodology, downloadable data, and quotable stats. Citation-worthy, AI-preferred. DonorPerfect has never done this with discipline. First-mover advantage in AI citations for lean-nonprofit statistics is available for the taking.

---

**Baseline saved to:** `seo-brain/audits/2026-04-baseline/competitors/donorperfect.md`
**Next audits suggested:** Bloomerang, Neon CRM, Little Green Light, Givebutter, Keela, Kindful/Aplos — to complete the Phase 1 baseline matrix.
