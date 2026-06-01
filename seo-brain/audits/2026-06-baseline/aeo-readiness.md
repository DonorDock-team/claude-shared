# AEO Readiness Audit — donordock.com

**Audited:** 2026-06-01
**Dimension:** AEO (Answer Engine Optimization) — featured snippets, People Also Ask, voice search, FAQ/HowTo rich results
**Prior baseline:** [../2026-05-baseline/aeo-readiness.md](../2026-05-baseline/aeo-readiness.md)
**Pages sampled:** Homepage, /pricing, /faq, /features, /about, /contact, /articles (index), /articles/* (3 step-based articles)
**Method:** Live raw-HTML fetch (curl, full UA) + JSON-LD `@type` extraction + heading/answer-block/table/list inventory + FAQ word-count analysis. Markdown-render fetch used as a cross-check for visible content.

---

## 1. Executive Summary

**Site-wide AEO score: 59 / 100 — up +5 from May (54), reversing part of April→May decline (65 → 54).** This month's gain is real, not a measurement artifact: every audited article now ships a **FAQPage** schema block it did not have in May, and **/pricing finally has BreadcrumbList** (a flagged May gap, now closed). The article hub remains DonorDock's AEO engine; the core marketing pages (homepage, /features, /about, /contact) are essentially unchanged and continue to sit out of every snippet and PAA surface.

**The good news (movement onto snippet surfaces):**
- **Articles added FAQPage schema.** All three audited step-based articles now carry a valid `FAQPage` + `Question` + `Answer` block plus `SpeakableSpecification`. This is partial delivery of May rec #6 — they moved from zero PAA eligibility to FAQ-rich-result eligible.
- **/pricing closed its BreadcrumbList gap** (May rec #9). It now carries FAQPage, BreadcrumbList, WebSite, Audience, and UnitPriceSpecification schema — the most complete page on the site.

**The bad news (still stuck, and one regression):**
- **HowTo schema still missing everywhere** — the #1 May recommendation. All three articles have clean, ordered "Step 1…Step 7" H2 sequences but zero HowTo markup. The highest-leverage win is still on the table.
- **The new article FAQPage blocks contain only ONE question each.** May rec #6 asked for 3–5 PAA-shaped questions per article. One Q&A is a foothold, not the long-tail PAA capture the structure can support.
- **/contact REGRESSED.** It now returns **zero JSON-LD of any kind** (in May it at least rendered phone/hours on-page; the page still has no LocalBusiness/ContactPage schema and now no schema at all). It remains the weakest page on the site.
- **Homepage, /features, /about: no change.** No question H2s, no FAQ schema, no HTML comparison table, no `<ol>`, no speakable. The homepage "Old Way / New Way" comparison and 5-step setup process are still un-tabled and un-ordered.

---

## 2. AEO Score Per Page Type

| Page | Jun Score | May Score | Δ | Rationale |
|---|---|---|---|---|
| **/pricing** | **90 / 100** | 88 | **+2** | FAQPage (10 Q&As, all 31–60 words), SoftwareApplication, Organization, Offer, AggregateRating, Audience, UnitPriceSpecification, **BreadcrumbList now added**, WebSite. Still missing: speakable, and an HTML comparison table for the price/add-on grid (still rendered as divs, `<table>` count = 0). |
| **/faq** | **84 / 100** | n/a (new sample) | — | Massive FAQPage with **114 Question/Answer pairs** wrapped in valid schema, plus visible `<h3>` question headings (e.g., "Can I migrate from Bloomerang, DonorPerfect, or other CRMs?"). Exemplary PAA inventory. Missing: speakable, BreadcrumbList, sub-topic H2 grouping. |
| **/articles/* (step articles)** | **80 / 100** | 76 | **+4** | BlogPosting + **SpeakableSpecification** + **FAQPage (new)** per article, clean "Step N:" H2 sequences. Missing: **HowTo schema (still 0)**; FAQ blocks hold only **1 question each** (target 3–5); 2 of 3 articles still use `<ul>` not `<ol>` for steps. |
| **/articles (blog index)** | **70 / 100** | 70 | **0** | CollectionPage with 12 BlogPosting `hasPart` entries (strong AI-crawler signal). Unchanged: only "Recent articles" rendered as H2; no on-page topic-cluster H2s, no question-format navigation. |
| **Homepage** | **42 / 100** | 42 | **0** | WebPage + SoftwareApplication + Organization + AggregateRating + Offer + ContactPoint. Still: zero question H2/H3, no FAQ schema, no speakable, no `<table>` (Old Way/New Way still divs), no `<ol>` for the 5-step setup. |
| **/features** | **38 / 100** | 38 | **0** | SoftwareApplication featureList + Offer + WebPage. Still: no FAQ, no question H2s, no comparison table, feature definitions still 20–25 words (below the 40–60 snippet sweet spot). |
| **/about** | **35 / 100** | 35 | **0** | AboutPage + Organization + 2× Person + SoftwareApplication + AggregateRating + ContactPoint — clean schema. Still: no question H2s, no FAQ, multi-H1 hierarchy confusion unaddressed. |
| **/contact** | **28 / 100** | 30 | **−2** | **REGRESSION: zero JSON-LD now present** (was none structured before but page is otherwise unchanged). Still no LocalBusiness/ContactPage schema, no FAQ block, no question H2s. Phone (701-490-8653) and hours (Mon–Fri 8–5 CST) remain machine-invisible. |

**Site-wide: 59 / 100 (May 54, April 65).** The +5 is driven by the article FAQPage rollout and the /pricing breadcrumb fix. The marketing-page floor (28–42) is unchanged and continues to cap the site.

---

## 3. Month-over-Month Delta Detail

### Moved ONTO snippet / PAA surfaces
- **/articles/conflict-healthy-culture-nonprofit-guide** — added FAQPage + Question/Answer + SpeakableSpecification (was BlogPosting + speakable only). Now FAQ-rich-result eligible.
- **/articles/grassroots-fundraising-playbook-new-nonprofits** — same: FAQPage added.
- **/articles/how-to-build-planned-giving-program-nonprofit** — same: FAQPage added (7 clean Step H2s, prime HowTo candidate still untapped).
- **/pricing** — BreadcrumbList added; now eligible for breadcrumb-enhanced SERP display, lifting CTR on its existing FAQ rich result.

### Moved OFF / regressed
- **/contact** — lost all JSON-LD (now 0 `@type` blocks). Net AEO posture worse than May.

### No change (still off every snippet surface)
- **Homepage, /features, /about** — identical AEO profile to May. Zero question headings, zero FAQ schema, zero HTML tables, zero ordered lists across all three.

### Partially-delivered May recommendations
| May Rec | Status Jun |
|---|---|
| #1 Add HowTo to step articles | **Not done** — HowTo count still 0 site-wide |
| #6 Article-foot FAQ (3–5 Qs) | **Partial** — FAQPage added but only 1 Q&A per article |
| #9 BreadcrumbList site-wide | **Partial** — added to /pricing only; absent on home/features/about/contact/faq/articles |
| #2 FAQ on /features | Not done |
| #3 LocalBusiness/ContactPage on /contact | Not done (regressed) |
| #4 Homepage 5-step → `<ol>` + HowTo | Not done |
| #7 Homepage Old/New `<table>` | Not done |
| #8 Fix /about heading hierarchy | Not done |

---

## 4. Specific Snippet / PAA Opportunities Still Missed

- **HowTo rich results (highest leverage).** Three articles have textbook 6–7 step "Step N:" H2 ladders and FAQ schema already wired — adding HowTo JSON-LD is a template-once-apply-many job that unlocks how-to rich results on "how to build a planned giving program", "how to build a conflict-healthy culture", "grassroots fundraising steps".
- **Article FAQ depth.** Each article's lone Q&A should grow to 3–5 PAA-shaped questions (e.g., for planned giving: "What is a planned giving program?", "How do small nonprofits start planned giving?", "How long does it take to build a planned giving program?"). The schema container already exists — just add entries.
- **Ordered-list markup.** 2 of 3 articles render their steps as `<ul>` (or no list); convert to `<ol>` for list-snippet eligibility now that HowTo is being considered.
- **/contact is invisible to voice.** "Hey Siri, what are DonorDock's support hours?" has nothing to lift. Add ContactPage + LocalBusiness JSON-LD (phone, hours Mon–Fri 8–5 CST, contact URL) and 3–4 question H2s. Restore at minimum the Organization/ContactPoint schema that exists on the homepage.
- **Homepage / features definitions.** Still no 40–60-word direct answer to "What is DonorDock?" or "What is ActionBoard?"; current answers run 20–25 words. Voice/snippet bots need the fuller answer block under a question heading.
- **HTML comparison tables.** Zero `<table>` elements anywhere on home/features/pricing. The homepage Old-Way/New-Way and the pricing add-on grid are both table-snippet candidates rendered as styled divs.

---

## 5. Prioritized Recommendations (June)

| # | Recommendation | Page | Effort | Expected Lift |
|---|---|---|---|---|
| **1** | **Add HowTo schema** to the 3 step-based articles. Steps + FAQPage are already in place; this is the single biggest unclaimed win, carried over from May. | /articles/* | Low | How-to rich results on multiple "how to…" queries |
| **2** | **Expand each article FAQPage from 1 → 3–5 questions.** Container exists; add real PAA-shaped Q&As with 40–60-word answers. | /articles/* | Low | Long-tail PAA capture around hub topics |
| **3** | **Restore + extend /contact schema.** Add ContactPage + LocalBusiness JSON-LD (phone, hours, URL) and 4 question H2s. Fixes this month's regression. | /contact | Low | Voice + brand-support PAA; reverses score drop |
| **4** | **Convert article steps to `<ol>`** (2 of 3 still aren't), pairing with rec #1. | /articles/* | Low | List-snippet eligibility |
| **5** | **Add FAQPage to /features** (6–8 feature questions, 40–60-word answers) — unchanged from May. | /features | Medium | Feature-curiosity PAA; competitive defense |
| **6** | **Homepage: ordered-list + HowTo for the 5-step setup; wrap Old/New comparison in `<table>`.** | / | Low–Med | "How does DonorDock work" list snippet + comparison-table snippet |
| **7** | **Roll BreadcrumbList out beyond /pricing** to /faq, /articles, /features, /about (one Webflow embed pattern). | All | Low | Compounding CTR on existing snippets |
| **8** | **Add speakable to /pricing and /faq** so voice assistants can read the strongest Q&A content aloud. | /pricing, /faq | Low | Voice-answer eligibility on the two best pages |
| **9** | **Fix /about multi-H1 hierarchy** + add brand-curiosity question H2s ("Who founded DonorDock?", "Where is DonorDock based?"). | /about | Medium | Brand PAA; removes parser confusion |
| **10** | **Surface topic-cluster H2s on /articles index** (Fundraising, Donor Management, Strategy, Outreach). | /articles | Medium | On-page topical clarity for SEO + AI hub signal |

---

## 6. Verification Checklist (Post-Deploy)

1. Run [Rich Results Test](https://search.google.com/test/rich-results) on each article after HowTo is added; confirm both FAQPage and HowTo validate together.
2. Validate restored /contact schema (ContactPage/LocalBusiness) in Rich Results Test before pushing live.
3. GSC → Enhancements → monitor FAQPage, HowTo, Breadcrumbs for new errors (the article FAQPage rollout should now appear here).
4. GSC → Performance → Search Appearance → filter FAQ + HowTo rich results 30 days post-deploy.
5. Re-request indexing for all updated article URLs + /pricing (breadcrumb) + /contact via GSC URL Inspection and Bing URL Submission.
6. Spot-check voice: "What are DonorDock's hours?", "How do I build a planned giving program?" should resolve to crisp ~30-word answers within 30–60 days.

---

## Reachability Notes
All sampled URLs returned HTTP 200. /contact returns 200 with content but **no JSON-LD blocks** (confirmed via raw-HTML grep — not a fetch artifact). No pages were blocked or unreachable.

---

**Audit conducted by:** AEO Auditor (claude-rank)
**Methodology:** Live raw-HTML fetch via curl with full UA, JSON-LD `@type` extraction, heading/list/table inventory, FAQ answer word-count and question-count analysis, schema validation against schema.org spec, month-over-month diff against 2026-05 baseline.
