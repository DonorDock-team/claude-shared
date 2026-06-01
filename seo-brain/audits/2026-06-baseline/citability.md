# DonorDock AI Citability Audit — June 2026 Baseline

**Auditor:** Citability Auditor (claude-rank)
**Date:** 2026-06-01
**Prior baseline:** [../2026-05-baseline/citability.md](../2026-05-baseline/citability.md)
**Scope:** Homepage, /pricing, /about, /faq (new), top articles
**Methodology:** 7-dimension scoring (1–10 per dimension) modeling citation likelihood across ChatGPT, Perplexity, Google AI Overviews, Claude, and Gemini.

---

## 1. Executive Summary

- **Overall sitewide citability holds at 76/100 (7.6/10), flat vs. May.** The article engine remains best-in-class and a genuine citation magnet. Two of the four known structural issues from May moved this month — one fixed, one regressed — and the net effect is a wash on the headline number. The trend is **flat (0)** after April→May's +34-point surge.

- **One real win: the rolling future-date bug is fixed.** Sampled articles now carry plausible past last-updated stamps (Apr 25 and Apr 28, 2026), not the forward-rolling dates flagged in prior runs. Freshness signals on articles are now trustworthy to crawlers.

- **Two issues got worse or stalled.** (1) **Entity inconsistency is now four-way, not three-way** — homepage/pricing say "7,600+ users," /about says "5,000+ leaders," and llms.txt still says "~1,300 nonprofits / 7,200+ users" (now stale on the user count too). The single most-repeated AI-trust recommendation across three months remains unactioned and has degraded. (2) **The sitemap still has zero `<lastmod>` dates** across now-1,071 URLs (up from 1,032).

- **New surface, new gap: /faq is now live with 80+ Q&A pairs — and carries NO FAQPage schema.** This is the single highest-leverage unrealized opportunity on the site this month. These are verbatim the questions AI users ask; marked up, this page could become a primary citation source. Unmarked, it is invisible to answer-engine extraction logic that keys on FAQPage entities.

- **Marketing pages still lag at 5.7/10** (essentially flat vs. May's 5.6). /pricing improved content depth (FAQ count 3→11) but still no schema, no author, no date, no TL;DR. Reconciling entities + shipping FAQPage schema on /faq and /pricing would lift sitewide to ~8.3.

---

## 2. Citability Scores by Page (per dimension, 1–10)

Dimension legend:
**A**=Authority signals · **D**=Data/stat density · **AF**=Direct-answer format · **S**=Source attribution · **F**=Freshness · **SD**=Structured data · **C**=Crawlability

| Page | A | D | AF | S | F | SD | C | **Avg** | **Δ May** |
|---|---|---|---|---|---|---|---|---|---|
| **/articles/why-fundraisers-under-ask** | 8 | 10 | 8 | 10 | 9 | 9 | 10 | **9.1** | −0.2 |
| **/articles/grassroots-fundraising-playbook** | 8 | 10 | 9 | 9 | 9 | 9 | 10 | **9.1** | 0.0 |
| **/articles/fundraising-intangible-impact** | 8 | 9 | 9 | 10 | 9 | 9 | 10 | **9.1** | 0.0 |
| **/articles/lapsed-donor-re-engagement** | 8 | 10 | 9 | 8 | 9 | 9 | 10 | **9.0** | 0.0 |
| **/articles/invisible-confidence-gap** | 7 | 10 | 9 | 8 | 9 | 9 | 10 | **8.9** | 0.0 |
| **/articles/nonprofit-technology-adoption** | 8 | 9 | 9 | 8 | 9 | 9 | 10 | **8.9** | 0.0 |
| **/articles/best-nonprofit-crm** | 7 | 8 | 8 | 5 | 9 | 9 | 10 | **8.0** | 0.0 |
| **/faq** (new) | 5 | 3 | 8 | 3 | 3 | 4 | 10 | **5.1** | NEW |
| **/about** | 7 | 6 | 5 | 3 | 4 | 7 | 10 | **6.0** | 0.0 |
| **/pricing** | 5 | 7 | 7 | 3 | 4 | 7 | 10 | **6.1** | 0.0 |
| **/ (homepage)** | 5 | 5 | 5 | 2 | 3 | 8 | 10 | **5.4** | 0.0 |
| **/features** | 4 | 4 | 4 | 2 | 3 | 6 | 10 | **4.7** | 0.0 |

**Sitewide average: 7.6/10 (76/100)** — flat vs. May. Article average: **8.9** (−0.0). Marketing-page average (faq/about/pricing/home/features): **5.7** (+0.1 vs. 5.6).

---

## 3. Trend vs. May

| Metric | April | May | **June** | Δ May→Jun |
|---|---|---|---|---|
| Overall /100 | 42 | 76 | **76** | **0** |
| Article avg /10 | — | 8.9 | 8.9 | 0.0 |
| Marketing-page avg /10 | — | 5.6 | 5.7 | +0.1 |
| Top article (under-ask) | — | 9.3 | 9.1 | −0.2 |

The April→May jump was driven by the article engine maturing (citations, schema, freshness). June is a **consolidation month** — no regression in the headline, but the four known infrastructure/entity issues that would unlock the next tier (76 → 83+) remain largely unaddressed. The plateau is a content-ops signal, not a content-quality one.

---

## 4. Re-Verification of Known Issues

| Known issue (from May) | June status | Detail |
|---|---|---|
| **Rolling future-date bug on articles** | ✅ **FIXED** | Sampled articles show plausible past last-updated dates (under-ask: Apr 25; lapsed-donor: Apr 28). No forward-rolling dates observed. |
| **Entity-count inconsistency** | ❌ **WORSE (4-way)** | Homepage/pricing: "7,600+ users" (was 7,200). /about: "5,000+ leaders." llms.txt: "~1,300 nonprofits / 7,200+ users" — now stale vs. the 7,600 figure. No reconciliation; drift increased. |
| **Sitemap missing `<lastmod>`** | ❌ **NOT FIXED** | 1,071 URLs (up from 1,032), still `<loc>`-only, no date tags. |
| **FAQPage schema only on articles, not /pricing** | ❌ **NOT FIXED + EXPANDED** | /pricing FAQs grew 3→11, still unmarked. New /faq page has 80+ Q&A, also unmarked. |

---

## 5. New & Notable This Month

### /faq is live (5.1) — biggest new opportunity
- **80+ Q&A across 5 sections** (Getting Started, Donor Management CRM, Outreach & Email, Online Giving, Project Management). Answers are mostly front-loaded and self-contained ("No. DonorDock includes unlimited contacts at no extra cost…").
- **No FAQPage JSON-LD.** This is the page's defining weakness. With markup, it becomes one of the most citable surfaces on the entire domain — it is literally a corpus of the questions AI users ask about nonprofit CRMs.
- Thin on authority (no attribution) and stats (only one G2 reference), so even marked up it scores on structure, not data. Marking it up alone lifts SD 4→9 and the page to ~6.5.

### /under-ask article dipped to 9.1 (−0.2)
- Headings are now **declarative, not question-form** ("Why We Under-Ask: The Psychology Behind Playing Small"). May noted question-format H2/H3 as a strength here; that appears to have regressed in an edit. Direct-answer dimension AF 9→8. Content and citations remain excellent.

### Stat consistency within content improved
- The "$54 per 1,000 messages / 5% social conversion" stat now appears consistently across homepage, pricing, and multiple articles — good internal triangulation. The problem is org-identity numbers (user/nonprofit counts), not content stats.

---

## 6. Lowest-Scoring Pages (Unchanged Priorities)

- **/features (4.7)** — still no author, no stats beyond "100+ features / 5,000+ apps," no citations, no date, declarative non-answer headings. Unchanged from May.
- **/ homepage (5.4)** — still 2 H1s ("Fundraising & Stewardship" + "All In One Place"), no author, no date, no TL;DR. Strong schema, thin extractable content.
- **/about (6.0)** — strong trust facts ($9B+ tracked, founded 2017, named co-founders, full G2/Capterra badge wall) but no Person schema, no date, and it is the source of the "5,000+ leaders" figure that conflicts with the homepage.

---

## 7. Top Fixes to Raise Citation Probability (June)

### Priority 1 — Do this month (unlocks the plateau)

1. **Mark up /faq AND /pricing with FAQPage JSON-LD.** Two pages, ~91 Q&A pairs total, currently zero markup. Highest single lift available. *Est: /faq 5.1→6.5, /pricing 6.1→7.3; sitewide +0.4.*

2. **Reconcile entity counts — now 3rd month flagged, now worse.** Pick one source of truth and propagate to homepage, /pricing, /about, and **llms.txt** (which is stale at 7,200). Recommend: "7,600+ users across ~1,300 nonprofits." Update llms.txt same day. *AI engines triangulate org-identity facts and de-rank inconsistent sources.*

3. **Add `<lastmod>` to sitemap.xml** (1,071 URLs, still none). Webflow exposes this. *Est: +0.5 on Freshness sitewide.*

### Priority 2 — Marketing-page content

4. **Restore question-format headings on /under-ask** and audit other articles for the same edit regression. Reverts AF 8→9.

5. **Add TL;DR / "Quick answer" boxes** to /pricing, /about, /features, homepage (40–60 words, "DonorDock is [definition] for [audience], starting at $500/mo").

6. **Author-attribute /pricing, /features, /about, /faq** ("Reviewed by Matt Bitzegaio, Co-founder & CEO") + Person schema.

### Priority 3 — Depth

7. **Add DonorDock first-party data to articles.** Sampled articles (incl. lapsed-donor) still cite zero proprietary data despite $9B+ tracked and 7,600 users. First-party stats are uniquely citable.

8. **Comparison table on /articles/best-nonprofit-crm** (still missing; AI Overviews preferentially extract tables).

---

## Appendix A — Crawlability Verification

| Check | Status |
|---|---|
| robots.txt allows AI bots | Yes — universal Allow: / |
| sitemap.xml present | Yes (1,071 URLs, up from 1,032) |
| sitemap has lastmod | **No — gap (3rd month)** |
| llms.txt present | Yes — but entity counts stale (7,200 vs live 7,600) |
| HTTPS / canonical | Yes |

## Appendix B — Schema Coverage

| Page | FAQPage schema | Notes |
|---|---|---|
| Articles | Yes | Working, paired with BlogPosting |
| /pricing | **No** | 11 visible Q&A, unmarked |
| /faq (new) | **No** | 80+ visible Q&A, unmarked — top opportunity |
| Homepage | n/a | SoftwareApplication/Product/WebPage; still 2 H1s |

## Appendix C — Author Attribution

- **Articles:** "Rob Burke, CMO" — consistent. Strong.
- **/about:** Co-founders named (Matt Bitzegaio, Andrew Lutgen), no Person schema.
- **/pricing, /features, /faq, /homepage:** No author. Gap.

---

**Bottom line:** June is a hold at 76/100. The date bug is fixed (good), but the entity-consistency problem worsened to a four-way split and the sitemap + FAQ-schema gaps persist. The fastest path off the plateau is mechanical, not editorial: mark up /faq and /pricing FAQs, reconcile the user/nonprofit counts (including the stale llms.txt), and add sitemap lastmod. Those three moves alone project 76 → ~83.
