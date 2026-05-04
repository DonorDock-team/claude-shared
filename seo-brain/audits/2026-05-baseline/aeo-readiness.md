# AEO Readiness Audit — donordock.com

**Audited:** 2026-05-04
**Pages sampled:** Homepage, /pricing, /features, /articles (blog index), /articles/* (3 top articles), /about, /contact
**Method:** Live HTML fetch + JSON-LD schema inspection + heading/answer-block analysis

---

## 1. Executive Summary

- **Pricing page is a model AEO citizen.** Ten well-formed Q&A pairs are wrapped in valid FAQPage JSON-LD, every answer falls in the 31–60-word featured-snippet sweet spot, and questions match real "How do I…" / "Can I migrate from…" search intent. This page is genuinely eligible for FAQ rich results today.
- **Article hub is doing the right things; the rest of the marketing site is not.** Articles ship with BlogPosting + speakable schema, step-numbered H2s, and tight intro paragraphs. Conversely, the homepage, /features, /about, and /contact have zero question-format headings, no FAQ schema, no comparison tables, and no direct-answer blocks — so they sit out of every snippet, PAA, and voice-answer surface they could otherwise win.
- **Two big quick wins.** (1) Convert /articles step-based content to HowTo schema — the structure is already there and ordered lists exist on 2 of 3 audited articles. (2) Add a small FAQPage to /features and /contact targeting the obvious questions ("What does DonorDock do?", "How do I contact DonorDock support?", "What are DonorDock's hours?") to capture brand + voice queries.

---

## 2. AEO Score Per Page Type

| Page | Score | Rationale |
|---|---|---|
| **/pricing** | **88 / 100** | FAQPage schema deployed, 10 Q&As, all answers 31–60 words, SoftwareApplication + Organization + Offer schema, AggregateRating present. Missing: BreadcrumbList, speakable, and HTML comparison table for the price/add-on grid. |
| **/articles/* (top articles)** | **76 / 100** | BlogPosting + speakable schema on each, author + dates + keywords, step-numbered H2s, intro paragraphs are concise. Missing: HowTo schema on step-by-step articles, FAQ blocks at the foot of each (no PAA capture), no in-article tables. |
| **/articles (blog index)** | **70 / 100** | CollectionPage schema with full hasPart BlogPosting array (excellent for AI crawlers). Missing: visible H2 categorization on the page itself (only "Recent articles" is rendered as H2), no question-format navigation, no topical clusters surfaced. |
| **Homepage** | **42 / 100** | WebPage + SoftwareApplication + Organization + AggregateRating in JSON-LD. But: zero question-format H2/H3, no FAQ schema, no direct-answer block, no speakable, no ordered list of the 5 setup steps despite step-named H3s. |
| **/features** | **38 / 100** | Strong featureList in SoftwareApplication schema (helpful for ChatGPT/Perplexity). But: no FAQs, no question H2s, no comparison table, no direct definitions of any feature. The page is named-list-of-features without snippetable answers. |
| **/about** | **35 / 100** | AboutPage + SoftwareApplication + Organization schema is present and clean. But: no question headings, no FAQ, multiple H1s ("We help you", "so that you can", "Equipping nonprofits…", "Our Mission") create heading-hierarchy confusion that hurts both SEO and AEO. |
| **/contact** | **30 / 100** | Has phone (701-490-8653), hours (Mon–Fri 8–5 CST), but: no LocalBusiness/ContactPage JSON-LD, no FAQ block, no address. Brand voice queries like "How do I contact DonorDock support?" have no structured answer to surface. |

**Site-wide AEO score: 54 / 100** — better than average for a SaaS, dragged down by the marketing pages. The pricing + articles team is clearly investing in AEO; the rest of the site has not caught up yet.

---

## 3. Specific PAA / Snippet Opportunities Missed

### Homepage

- **5-step setup process is not snippet-eligible.** The H3s read "We Will Help You Set Up Everything For Free", "Master DonorDock with Live Expert Training", "Automate Your Fundraising and Donor Management", "Gain Insights with Powerful Reporting", "See Real Results—Faster" — that is a numbered list in disguise. There is no `<ol>` markup, no HowTo schema, no step number, no "Step 1:" prefix. Google can't surface this for a "how does DonorDock work" list snippet.
- **"The Old Way vs The New Way" is not in a `<table>`.** The hero comparison ("Spreadsheets vs The DonorDock Platform") is rendered as styled divs. Wrap it in `<table>` and Google becomes eligible to lift it as a comparison-table snippet for queries like "spreadsheet vs nonprofit CRM".
- **No question-format H2s.** Real searches like "what is the best CRM for small nonprofits?" or "how does DonorDock work?" have no matching question heading on the page, so the homepage cannot win brand-PAA.
- **Hero subheadline is fragmented.** "Fundraising & Stewardship / All In One Place" is split across two H1s with a leading invisible character (`‍`). Voice assistants and snippet bots will read this awkwardly. Should be one H1, one paragraph beneath it that is a direct 40–60-word answer to "What is DonorDock?".

### /features

- **Zero question H2/H3.** The page lists capabilities ("ActionBoard™", "Project Boards", "Smart Nudges", "Ask Boards", "AUTOMATION") but never asks "What is ActionBoard?" or "How do Smart Nudges work in DonorDock?". Each of those is a real PAA candidate that competitors (Bloomerang, Little Green Light) will eventually take.
- **No comparison table.** A "DonorDock vs spreadsheet" or "DonorDock vs Bloomerang feature matrix" rendered as `<table>` would directly compete for table-snippet placement on category queries.
- **No direct definitions.** Only one ~20-word fragment ("Automation [that] takes care of repetitive tasks…") qualifies as an answer block. Each feature should open with a 40–60-word definition right under its H2.

### /about

- **Heading hierarchy is broken for AEO.** The page renders 8 separate H1s (the rotating headline animation: "manage relationships", "raise money", "enhance communication", etc., are H2s under additional H1s). When Google or Bing parse the document, the "What is DonorDock?" question has no canonical, single H1 with a clean answer beneath it.
- **"DonorDock's Origin Story" is a snippet opportunity.** Brand-curiosity queries ("who founded DonorDock", "where is DonorDock based") have a story on the page but no FAQ schema and no question H2 like "Who founded DonorDock?".

### /contact

- **No LocalBusiness or ContactPage schema.** Phone, hours, and contact form are on the page but not machine-readable. Voice search ("Hey Siri, what are DonorDock's hours?") has nothing to lift.
- **Three obvious unanswered questions:** "How do I contact DonorDock support?", "What are DonorDock's support hours?", "Does DonorDock offer phone support?" — none have a question H2 or FAQ entry on the page.

### /articles/* (top articles)

- **Step-numbered articles missing HowTo schema.** "How to Build a Conflict-Healthy Culture at Your Nonprofit" has 6 H2s starting with "Step 1:", "Step 2:", … through "Step 6:", plus one `<ol>`. This is the textbook HowTo schema candidate. Without it, the article cannot win the how-to rich result.
- **Same for "Your First 500 Donors: A Grassroots Fundraising Playbook"** — 6 explicit "Step N:" H2s, but only `<ul>` not `<ol>`, and no HowTo schema. List-snippet eligibility is forfeit.
- **Articles open with definition opportunities, not direct answers.** Article 1's first paragraph after the H1 reads: "If you lead a nonprofit team, you have probably watched a simmering tension go unaddressed until someone quietly resigned." That is a hook, not an answer. A 40–60-word direct answer to "How do you build a conflict-healthy culture at a nonprofit?" should sit right under the H1 (the speakable selector already targets `.article-intro`, so the value of the asset doubles when the content matches the markup).
- **No FAQ blocks at article foot.** Each article should end with 3–5 PAA-shaped questions (e.g., "What does conflict-healthy mean?", "How long does it take to change nonprofit culture?") wrapped in FAQPage schema. This is how DonorDock starts winning the long-tail PAA boxes around its hub topics.

### /articles (blog index)

- **CollectionPage hasPart is excellent for ChatGPT/Perplexity** but the page itself only renders an H1 ("Donor Development Hub") and one H2 ("Recent articles"). There is no topic clustering visible to Google ("Fundraising", "Donor Management", "Nonprofit Strategy" exist as keywords inside the schema but not as on-page H2 sections).

---

## 4. Pages That ARE Well-Optimized (Keep Doing)

- **/pricing FAQ is exemplary.** Ten questions, each a real search query. Every answer is between 31 and 60 words, leads with the direct answer, and uses keyword-aligned language. The FAQPage JSON-LD is well-formed and linked via `@id`. Keep this as the template for every other page.
- **Article speakable selectors are correctly targeting `h1`, `.article-intro`, `h2`** — once the intro paragraphs are tightened to 40–60 words, voice assistants will read clean answers aloud.
- **BlogPosting schema includes `keywords`, `articleSection`, `isPartOf`, `timeRequired`** — these are signals most competitors skip. The hub-and-spoke linkage (`isPartOf` pointing to `/fundraising-strategy`) gives AI crawlers a clear topical map.
- **CollectionPage `hasPart` array on /articles is a citation magnet for AI search.** ChatGPT and Perplexity can read this index in a single fetch and pull the right article without crawling each URL — that is exactly how AI Overviews discover content. Do not remove this.
- **SoftwareApplication featureList on /features lists 60+ specific features.** This is great GEO/AEO inventory for "does DonorDock have X?" queries. Keep maintaining it; it's a quiet win.
- **AggregateRating (4.8 / 200 reviews) is consistent across home, pricing, and about.** Don't drift the numbers between pages — that consistency is what lets SGE show stars next to the brand.

---

## 5. Top 10 Ranked Recommendations

| # | Recommendation | Page | Effort | Expected Lift |
|---|---|---|---|---|
| **1** | **Add HowTo schema** to the 3 audited step-based articles ("Conflict-Healthy Culture", "First 500 Donors", "Why Most Nonprofit Tech Investments Fail"). Each already has Step-numbered H2s. | /articles/* | Low (template once, apply to all step-based articles) | Featured-snippet eligibility on "how to build nonprofit culture", "how to get first donors", direct how-to rich results |
| **2** | **Add FAQPage schema to /features** with 6–8 questions: "What does ActionBoard do?", "How do Smart Nudges work?", "What's included in DonorDock's automations?", "Does DonorDock include text messaging?", "What integrations does DonorDock support?". Each answer 40–60 words. | /features | Medium | Captures feature-curiosity PAA; protects against competitor FAQ ranking |
| **3** | **Add LocalBusiness + ContactPage schema to /contact** with phone, hours (Mon–Fri 8–5 CST), and contact URL. Add 4 question H2s: "How do I contact DonorDock support?", "What are DonorDock's hours?", "Does DonorDock offer phone support?", "How do I request a demo?". | /contact | Low | Voice search wins, brand-support PAA, "near me"-style queries for nonprofit CRM support |
| **4** | **Convert the homepage 5-step process to ordered-list HTML + HowTo schema.** Prefix each H3 with "Step 1:", "Step 2:" etc., wrap in `<ol>`, and add HowTo JSON-LD with the existing 5 step names. | / | Low | Eligible for "how does DonorDock work" list snippet; PAA capture |
| **5** | **Tighten article intro paragraphs to 40–60 words of direct answer.** The speakable selector already targets `.article-intro` — make the content match. Article 1's intro should answer "How do you build a conflict-healthy nonprofit culture?" in ~50 words instead of opening with a story hook. | /articles/* | Medium | Voice search wins (Google voice answers average 29 words; 40–60 is the snippet ceiling) |
| **6** | **Add an article-foot FAQ block** (3–5 PAA-shaped Qs) wrapped in FAQPage schema to every article. Use real "People Also Ask" data — for the conflict article: "What is a conflict-healthy culture?", "How long does it take to change nonprofit culture?", "What causes conflict in nonprofits?". | /articles/* | Medium | Long-tail PAA wins; pushes articles into Google's "expanded" SERP cards |
| **7** | **Wrap the homepage "Old Way vs New Way" comparison in a real `<table>`** with `<thead>` and `<tbody>`. Google needs HTML table structure to lift table snippets. Right now it is divs and CSS. | / | Low | Table-snippet eligibility for "spreadsheet vs nonprofit CRM" queries |
| **8** | **Fix /about heading hierarchy.** Reduce to ONE H1 ("About DonorDock" or "Equipping nonprofits with the tools to further their mission"). Convert the rotating headline animation H1s ("We help you", "manage relationships", etc.) to spans inside one H1, or to H2s. Add 4 question H2s: "Who founded DonorDock?", "When was DonorDock founded?", "Where is DonorDock based?", "What is DonorDock's mission?". | /about | Medium | Brand-curiosity PAA wins; cleans up parser confusion that suppresses all snippets |
| **9** | **Add BreadcrumbList JSON-LD** site-wide (homepage → category → page). Currently zero pages have it. Breadcrumbs increase CTR on snippet results by giving searchers more context. | All | Low (one Webflow embed) | Higher CTR on every existing snippet; small but compounding |
| **10** | **Surface topic clusters as H2 sections on /articles index.** Right now the only H2 is "Recent articles". Add H2s for "Fundraising", "Donor Management", "Nonprofit Strategy", "Outreach" — the four keywords already in the BlogPosting schema. Each section can list 3–4 articles. | /articles | Medium | On-page topical clarity for SEO; better hub-and-spoke signal for AI search |

---

## Verification Checklist (Post-Deploy)

1. Run [Rich Results Test](https://search.google.com/test/rich-results) on /pricing (validate existing FAQPage), then on /features and /contact after deploy.
2. Run Rich Results Test on each updated /articles/* URL to validate HowTo schema.
3. In Google Search Console → Enhancements, monitor FAQPage, HowTo, Breadcrumbs sections for errors.
4. In GSC → Performance → Search Appearance, filter by "FAQ rich results" and "HowTo rich results" 30 days post-deploy to track wins.
5. Submit updated URLs via GSC URL Inspection ("Request Indexing") and via Bing URL Submission for Copilot visibility.
6. Spot-check voice answers: ask Google Assistant "What is DonorDock?", "How do I contact DonorDock?", "How does DonorDock work?" — should resolve to crisp, ~30-word answers within 30–60 days.

---

**Audit conducted by:** AEO Auditor (claude-rank)
**Methodology:** Live HTML fetch via curl with full UA headers, JSON-LD extraction, heading/list/table inventory, FAQ answer word-count analysis, schema validation against schema.org spec.
