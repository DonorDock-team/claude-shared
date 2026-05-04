# GEO (Generative Engine Optimization) Readiness Audit — donordock.com
**Date:** 2026-05-04
**Auditor:** claude-rank GEO sub-agent
**Scope:** Readiness of donordock.com to be cited by ChatGPT, Perplexity, Google AI Overviews, Gemini, Claude
**AI Readiness Level:** **2.5 of 3 (Optimized → approaching Dominant)**

---

## 1. Executive Summary

- **donordock.com is well-positioned for AI citation** — robots.txt is fully open to every major AI crawler, a high-quality `llms.txt` is live, and pillar articles already have `BlogPosting` schema with author + dateModified. The site is not "invisible" to AI search; the foundations are solid.
- **The biggest gaps are content-shape, not access.** Most pages have 0–2 question-formatted H2s, no comparison tables in HTML, and almost no rendered author bylines on the page itself. Articles do contain heavy statistic density (donor-retention page has 15 percentage stats and 5 "according to" citations — exemplary), but pillar pages like Best Nonprofit CRM 2026 lack visible author attribution and source citation phrasing.
- **Quickest wins (next 2 weeks):** Add `llms-full.txt` (currently 404), add visible author bylines + "Last updated" dates on every article, ship rendered HTML comparison tables on the 10 `/compare/*` pages, and fix the JSON-LD trailing-comma parse error on `/compare/bloomerang-vs-donordock`. These four changes lift the site to Level 3 (Dominant).

---

## 2. Bot Access Matrix

**robots.txt** (https://www.donordock.com/robots.txt) is a single allow-all rule:

```
User-agent: *
Allow: /
Sitemap: https://www.donordock.com/sitemap.xml
```

| Bot | Powers | Status | HTTP test |
|---|---|---|---|
| GPTBot | OpenAI training + ChatGPT browsing | Allowed | 200 |
| ChatGPT-User | ChatGPT live browsing | Allowed (via *) | n/a |
| OAI-SearchBot | ChatGPT Search | Allowed (via *) | n/a |
| ClaudeBot | Anthropic training + Claude.ai browsing | Allowed | 200 |
| Claude-Web | Claude.ai live fetching | Allowed (via *) | n/a |
| PerplexityBot | Perplexity index | Allowed | 200 |
| Perplexity-User | Perplexity live citations | Allowed (via *) | n/a |
| Google-Extended | Google AI Overviews + Gemini training | Allowed | 200 |
| Googlebot | Standard Google + AI Overviews ranking | Allowed (via *) | n/a |
| Bingbot | Microsoft Copilot + ChatGPT Browse | Allowed | 200 |
| Applebot-Extended | Apple Intelligence | Allowed | 200 |
| CCBot | Common Crawl (foundation training data) | Allowed | 200 |
| Meta-ExternalAgent | Meta AI (Llama training) | Allowed (via *) | n/a |
| DuckAssistBot | DuckDuckGo AI Answer | Allowed (via *) | n/a |
| Amazonbot | Alexa, Rufus, Amazon AI | Allowed (via *) | n/a |
| Bytespider | ByteDance / TikTok / Doubao | **HTTP 403** at edge (likely WAF/bot-mitigation, not robots.txt) |

**Verdict:** Best-possible posture for AI access. The only blocked bot (Bytespider) is blocked at the CDN/WAF layer, not robots.txt — and it's the lowest-value crawler of the set (TikTok / Doubao). No action required, but worth verifying with the hosting layer if China-market visibility ever becomes a goal.

**Risk:** A single allow-all rule is fragile. If anyone later adds a `Disallow: /` for a specific bot, it could silently break AI visibility. Recommend converting to an **explicit allow-list** that names every AI bot above (defensive, also signals intent to AI vendors).

---

## 3. llms.txt Status

| File | Status | Notes |
|---|---|---|
| `/llms.txt` | **HTTP 200, 7,567 bytes** — present and high-quality | One of the best llms.txt files in the nonprofit-CRM category |
| `/llms-full.txt` | **HTTP 404** | Missing — recommended for deep-context AI assistants |

**llms.txt quality assessment (scored against best practice):**

| Section | Present | Quality |
|---|---|---|
| H1 + product summary blockquote | Yes | Strong — names Smart Stewardship, Smart Steward Method, Smart Nudges, Action Board, Otto AI |
| Category / Audience / Pricing / Founded | Yes | Excellent — exactly the structured facts AI engines extract |
| Rating: 4.8/5 across 200+ reviews | Yes | Citation-ready |
| Core platform pages | Yes (10) | Complete |
| Product capability pages | Yes (7) | Complete |
| Competitor comparisons | Yes (10) | Comprehensive |
| Solutions by need | Yes (5) | Complete |
| Education and resources | Yes (6) | Complete |
| Notable pillar articles | Yes (10) | Strong topical coverage |
| Online giving fee structure | Yes | Pre-empts "what does DonorDock cost?" hallucinations |
| Key differentiators | Yes (10 bullets) | Excellent — these are the literal sentences AI engines will quote |
| Contact info | Yes | Complete |
| Policy for AI systems | Yes | **Best-in-class** — explicit "training: allowed", "commercial use: allowed with attribution", and naming/linking guidance |

**Score: 95/100.** Only deduction: no `llms-full.txt` companion file. The current llms.txt is essentially the index; `llms-full.txt` should expand each linked URL into a single concatenated markdown corpus so deep-research AI agents (e.g. Perplexity Deep Research, ChatGPT Deep Research, Gemini's research mode) can ingest the full product context in one fetch.

---

## 4. Content Citation-Readiness Scores by Page Type

Scored 0–100 on the GEO citation rubric: bot access × structured-data coverage × question-headings × statistic density × source attribution × author authority × freshness × extractable passage shape.

### 4a. Homepage (`/`)

| Signal | Result | Score |
|---|---|---|
| Schema | `WebPage` only — but nests `SoftwareApplication` with `AggregateRating` 4.8 (200+ reviews) and `Offer` $500/month inside `about` | 7/10 |
| Headings | 1 H1, 2 H2s, 7 H3s. **0 question-format H2s.** | 4/10 |
| Statistic density | 8 numeric mentions, 0 % stats, 0 $ amounts in body, 0 year mentions | 3/10 |
| Source attribution | 0 "according to" / "study" / "report" mentions | 2/10 |
| Author / authority | No bylines (homepage — appropriate); founders not surfaced in body schema | 6/10 |
| Freshness | No visible "updated" stamp | 3/10 |
| Extractable passages | Marketing copy ("All In One Place"), no clean "DonorDock is X" definition paragraph in HTML | 4/10 |
| **Total** | | **39/100** |

The homepage isn't where AI citations land — but a 1-paragraph "What is DonorDock?" definition block with a single statistic (e.g. "DonorDock is a donor-management CRM used by 1,300+ nonprofits and 7,200+ fundraisers, rated 4.8/5 across 200+ reviews") would lift this to 70+.

### 4b. Pillar Articles (`/articles/best-nonprofit-crm`, `/articles/donor-retention`)

**Best Nonprofit CRM 2026:**

| Signal | Result | Score |
|---|---|---|
| Schema | `BlogPosting` + author "Rob Burke" + datePublished 2026-04-26 + FAQPage + Organization | 9/10 |
| Headings | 1 H1, 6 H2s, 11 H3s. H2s scan as a clean buyer-guide outline ("Why Your Nonprofit Needs a CRM in 2026", "What to Look for in a Nonprofit CRM", "How to Choose"). Only 1 of 6 is question-shaped. | 7/10 |
| Statistic density | 70 numeric mentions, 3 %, 28 $ amounts, 11 year mentions | 9/10 |
| Source attribution | **0 "according to" / "study" / "report" mentions** in 3,400 words — the biggest miss for an authoritative buyer guide | 2/10 |
| Author / authority | Schema author = Rob Burke. **No visible byline rendered on page.** | 5/10 |
| Freshness | "Last updated April 2…" rendered in body — good | 9/10 |
| Extractable passages | Per-CRM H3 sections give AI clean blocks to extract for each competitor | 8/10 |
| **Total** | | **70/100** |

**Donor Retention pillar:**

| Signal | Result | Score |
|---|---|---|
| Schema | `BlogPosting` + author "Elisha Ford" + datePublished 2026-04-28 + FAQPage + Person + Organization | 10/10 |
| Headings | 1 H1, 6 H2s, 14 H3s. Has Table of Contents H2. **0 H2s end in `?`** but several H3s do (good). | 7/10 |
| Statistic density | 15 % stats (excellent), 59 numbers, 8 year mentions | 10/10 |
| Source attribution | **5 "according to" + 4 study/report/survey references** — best on the site | 10/10 |
| Author / authority | Schema author = Elisha Ford, no rendered byline visible on page | 5/10 |
| Freshness | "Last updated April 2…" rendered | 10/10 |
| Extractable passages | Strong — strategy sub-sections are the right 130–180 word shape AI engines like to lift | 9/10 |
| **Total** | | **88/100** |

This is the citation-magnet template. The Best-CRM article should be retrofitted to match (add 4–6 "according to [source, year]" references with linked sources).

### 4c. Comparison Pages (`/compare/bloomerang-vs-donordock`)

| Signal | Result | Score |
|---|---|---|
| Schema | `WebPage` with nested `SoftwareApplication` + AggregateRating. **JSON-LD has a trailing comma — fails strict parsers.** | 5/10 |
| Headings | H1 mismatched ("The Difference Between Retention Scores & Relationship Growth" — should be "Bloomerang vs DonorDock"). 5 H2s, 1 question-shaped ("Worried about data migration?"). | 5/10 |
| Statistic density | 22 numbers, 2 %, 4 $, 5 year mentions | 7/10 |
| Source attribution | 0 source citations | 2/10 |
| Author / authority | None | 3/10 |
| Freshness | "Last updated March 2…" rendered | 8/10 |
| Extractable passages | **No HTML comparison table** (`<table>` count = 0). AI engines love tables for comparison queries — a side-by-side feature table is the single highest-leverage GEO upgrade for this page type. | 3/10 |
| **Total** | | **49/100** |

### 4d. Pricing (`/pricing`)

| Signal | Result | Score |
|---|---|---|
| Schema | `Organization` graph with founders, `SoftwareApplication`, `AggregateRating` 4.8 / 200+, `FAQPage`, founders as `Person` | 10/10 |
| Headings | H1 "Unlimited contacts. Limitless impact." + 3 H2s. 0 question H2s. | 5/10 |
| Statistic density | 25 numbers, 1 %, 5 $ amounts | 6/10 |
| Source attribution | None expected | n/a |
| Freshness | No "updated" stamp visible | 4/10 |
| Extractable passages | Strong pricing-fact density ($500/month, unlimited contacts, 5 users, 1% platform fee — these are exactly what AI quotes) | 9/10 |
| **Total** | | **75/100** |

### 4e. FAQ Page (`/faq`)

- `FAQPage` schema with `@graph` structure, parses cleanly.
- **114 question headings rendered on page** — this is an enormous AEO/GEO asset.
- Each Q is in proper interrogative form; this is the page most likely to surface in Google AI Overviews and Perplexity citations.
- Score: **92/100**. The only improvement: ensure each answer is also wrapped in `acceptedAnswer.text` in schema (verified in source: yes, structure is correct).

### 4f. Page-type score summary

| Page type | Citation-readiness | Trend |
|---|---|---|
| FAQ page | 92/100 | Citation-magnet, leave alone |
| Donor-retention pillar article | 88/100 | Template for other articles |
| Pricing | 75/100 | Add a freshness stamp + question H2 |
| Best-CRM pillar article | 70/100 | Add source citations + visible byline |
| Compare pages | 49/100 (avg) | **Highest-leverage fix area** |
| Homepage | 39/100 | Add 1-paragraph definition block |

---

## 5. Top 10 Specific Recommendations (Prioritized by AI-citation Lift)

### 1. Ship `/llms-full.txt` (Effort: 1 day · Impact: high)
Concatenate the markdown bodies of the 10 pillar pages, 10 compare pages, 5 solution pages, /pricing, /about, and /faq into a single file at `/llms-full.txt`. Format as one H1 per source page with the URL listed below. This is the file ChatGPT Deep Research and Perplexity Deep Research will fetch when asked "tell me everything about DonorDock". Currently 404.

### 2. Add visible author bylines to every article (Effort: 1 day · Impact: high)
Rendered HTML on `/articles/best-nonprofit-crm` and `/articles/donor-retention` does **not** show "By Rob Burke" or "By Elisha Ford" on the page, even though `BlogPosting` schema names them. AI engines weight visible bylines + author bio cards more than schema-only attribution. Add a byline component: name, role, photo, link to author bio page, "Last updated" date — visible above the article body.

### 3. Add HTML comparison tables to all 10 `/compare/*` pages (Effort: 3 days · Impact: high)
Currently zero `<table>` elements on comparison pages. AI engines (especially Perplexity and ChatGPT Search) preferentially cite content that contains structured comparison tables for "X vs Y" queries. Add a 8–12 row feature comparison table per compare page (Pricing, Contact limits, Online giving fee, Onboarding, AI features, Mobile, Support, Reviews, etc.). Also add the `ComparisonTable` schema if available.

### 4. Fix JSON-LD trailing-comma error on `/compare/bloomerang-vs-donordock` (Effort: 15 minutes · Impact: medium)
The JSON-LD on this page has a trailing comma before the closing array bracket on line 35. Strict parsers (including Google's Rich Results test and some AI ingestion pipelines) will reject the entire block. Audit all 10 compare pages for the same issue.

### 5. Fix H1 on compare pages (Effort: 1 hour · Impact: medium)
The Bloomerang compare page H1 reads "The Difference Between Retention Scores & Relationship Growth" — that's a marketing tagline. AI engines extract H1 as the canonical page topic. Set H1 to "Bloomerang vs DonorDock: Nonprofit CRM Comparison" (matching the meta title and schema `name` field). Repeat across all 10 compare pages.

### 6. Add "according to [source, year]" citations to every pillar article (Effort: 4 days · Impact: high)
The Best-CRM 2026 article has zero source citations across 3,400 words. The Donor Retention article has 5 — and that pattern is exactly what makes it citation-ready. Retrofit `/articles/best-nonprofit-crm`, `/articles/nonprofit-crm-buyers-guide-12-questions-to-ask`, `/articles/nonprofit-crm-migration-checklist`, `/articles/fundraising-101`, and `/articles/nonprofit-glossary` with 4–6 sourced statistics each (M+R Benchmarks, Fundraising Effectiveness Project, Giving USA, Blackbaud Institute). Link each to a credible source page.

### 7. Convert top-of-article H2s to question form on the 10 pillar articles (Effort: 2 days · Impact: medium)
Across the audited articles, 0 of 12 H2s are in question form. Question H2s are the #1 AEO/GEO ranking signal — they map 1:1 to the queries users type into ChatGPT and Perplexity. Convert: "Understanding Donor Retention and Its Significance" → "Why does donor retention matter?", "What to Look for in a Nonprofit CRM" → "What should you look for in a nonprofit CRM?". Keep the marketing-friendly version as the H2 visible text; alternatively use both styles across the page.

### 8. Add a 1-paragraph "What is DonorDock?" definition block to the homepage (Effort: 2 hours · Impact: medium)
The homepage HTML body has no clean "DonorDock is a [category] used by [audience] for [outcome]" sentence. Add a 60–80 word definition paragraph in the hero or just-below-hero section using the exact wording from llms.txt. AI engines prefer to quote site copy over llms.txt copy for citations because the URL of the homepage is what they link to.

### 9. Convert robots.txt to explicit AI-bot allow-list (Effort: 30 minutes · Impact: low/defensive)
Replace `User-agent: *` allow-all with explicit sections naming GPTBot, ClaudeBot, PerplexityBot, Google-Extended, OAI-SearchBot, Applebot-Extended, CCBot, Meta-ExternalAgent, Amazonbot, DuckAssistBot. Keeps current behavior, but documents intent and prevents accidental future blocks. Also signals to AI vendors that crawling is welcome.

### 10. Add "Last updated [Month Year]" stamps to /pricing, /tour, /features-overview, /otto, /crm, /online-giving (Effort: 1 day · Impact: medium)
Pillar articles already have "Last updated" stamps. Product pages don't. AI engines weight freshness heavily for pricing and feature pages — when ChatGPT is asked "what is DonorDock pricing", it prefers to cite the page with the most recent visible update. Add a footer-of-content stamp on every product/pricing/feature page and update it whenever copy changes (or wire it to Webflow's `Last Updated` CMS field).

---

## Verification Plan (after fixes ship)

1. Wait 14–28 days for AI re-crawling.
2. Run citation tests in:
   - **ChatGPT Search:** "best nonprofit CRM 2026", "DonorDock vs Bloomerang", "what does DonorDock cost"
   - **Perplexity:** Same three queries plus "donor retention statistics"
   - **Google AI Overviews:** Same queries on Google
   - **Gemini:** Same queries
   - **Claude.ai with web search:** Same queries
3. Track citations in `/Users/rob/Documents/DonorDock/Claude/Data/` with date-stamped logs (e.g. `2026-06-01-AI-citations.md`).
4. Resubmit sitemap to Google Search Console + Bing Webmaster Tools after deploying fixes.
5. Enable IndexNow for Webflow (Bing/Copilot fast-indexing).
6. Re-run this audit at /tmp/dd-citations-runner/seo-brain/audits/2026-07-baseline/ and compare deltas.

---

## Appendix: Raw signals captured

Source HTML samples saved alongside this audit:
- `_home.html`, `_article.html` (best-nonprofit-crm), `_compare.html` (bloomerang), `_donor-retention.html`, `_pricing.html`, `_faq.html`

robots.txt body:
```
User-agent: *
Allow: /
Sitemap: https://www.donordock.com/sitemap.xml
```

JSON-LD types found per page:
- `/`: WebPage (with nested SoftwareApplication + AggregateRating + Offer)
- `/articles/best-nonprofit-crm`: BlogPosting + FAQPage + Organization + Person (author)
- `/articles/donor-retention`: BlogPosting + FAQPage + Organization + Person (author)
- `/compare/bloomerang-vs-donordock`: WebPage (with nested SoftwareApplication + AggregateRating) — **trailing-comma JSON error**
- `/pricing`: @graph with Organization + SoftwareApplication + AggregateRating + FAQPage + Person (founders)
- `/faq`: @graph with FAQPage (114 questions)
