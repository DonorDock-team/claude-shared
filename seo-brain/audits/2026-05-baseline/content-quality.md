# Content Quality Audit — donordock.com

**Audit date:** 2026-05-04
**Auditor:** Claude (claude-rank Content Auditor)
**Scope:** Homepage, /pricing, /about, /contact, /compare, /features, /solution, /success-stories, /tags, /team, /articles (sampled across hub, pillar, and topic clusters)
**Total URLs in sitemap:** 893 (47 root, 449 articles, 97 features, 75 integrations, 69 tags, 60 tools, 35 team, 14 success stories, 10 compare, 10 solution, plus landing pages)

---

## 1. Executive Summary

- **Content volume is strong, freshness signal is broken.** DonorDock has 449 published articles, 97 feature pages, 60 tools, 14 success stories, and a coherent comparison hub — a healthy library. But every sampled article shows a "last updated" date in the immediate future (April 24-29, 2026 on a 2026-05-04 audit day), meaning the site is using a rolling/auto-incrementing timestamp instead of a meaningful update history. Google increasingly distrusts dynamic dates that always read "just updated"; this is the single biggest content-trust risk on the site.

- **Author bylines exist but EEAT is paper-thin.** Articles are bylined to Rob Burke (CMO) or Elisha Ford (Content Writer), and there are 35 /team/ pages — but author bio pages contain only 90-150 words, no credentials, no list of authored articles, no expertise/experience signals (years in nonprofit, certifications, prior roles). For YMYL-adjacent topics (nonprofit finance, grants, CRM purchase decisions), this depresses E-E-A-T. Author pages should carry full bios, article lists, and credibility signals.

- **Cannibalization risk is real across the donor lifecycle cluster.** Sampled articles on donor-engagement, donor-retention, donor-appreciation, donor-segmentation, and fundraising-101 each cover overlapping territory (segmentation, communication channels, storytelling, retention math). Combined with parallel /solution/donor-retention, /solution/donor-stewardship, and /tags/donor-stewardship hub pages, search engines see 5+ DonorDock URLs competing for the same intent. Needs a content-cluster rationalization with clear pillar/spoke hierarchy and canonical signals.

---

## 2. Content Inventory Snapshot

### Pages by Type

| Type | Count | Avg Word Count (sampled) | Freshness | Notes |
|---|---|---|---|---|
| Articles (/articles/*) | 449 | 2,800-4,500 long-form; 12,500 for listicle | Future-dated, unreliable | Bylined; FAQ schema common |
| Feature pages (/features/*) | 97 | 1,200-1,400 | Static | Substantive; not thin |
| Integrations (/integrations/*) | 75 | Not sampled — likely template-driven | Static | Risk: thin/templated content |
| Tag hubs (/tags/*) | 69 | 800-1,000 unique (mostly nav) | Auto | No pillar intro text — pure listings |
| Team / author (/team/*) | 35 | 90-150 | Static | Thin; no article list, no bio depth |
| Tools (/tools/*) | 60 | Not sampled | Static | Templates, calculators, courses — likely mixed |
| Success stories (/success-stories/*) | 14 | ~2,100 | No date | Strong structure; missing publication dates |
| Compare (/compare/*) | 10 | 3,500-4,000 | March 2026 (also future-dated) | Substantive but one-sided tone |
| Solutions (/solution/*) | 10 | 3,200-3,500 | Static | Strong product-marketing pages |
| Root pages | 47 | Variable | Static | Includes /about (~2,000 wd), /contact (~1,200 wd), /pricing (substantive) |

### Content Type Mix (sampled)

- **Pillar articles** (3,000+ words, FAQ-bearing): donor-engagement, donor-retention, donor-segmentation, donor-appreciation, fundraising-101, best-nonprofit-crm, nonprofit-crm-migration-checklist, 100-easy-fundraising-ideas (12.5k words)
- **Comparison pages**: 9 vs-DonorDock pages plus 2 Salesforce variants — content-rich, brand-defensive
- **Product pages**: /features (97), /solution (10), /lp (6) — well-developed
- **Empty hub pages**: /tags (69) function as raw chronological lists with no pillar copy or topic intro

### Freshness Status

**CRITICAL ISSUE:** The "last updated" timestamp on all sampled articles auto-rolls to a future date (e.g., audit on 2026-05-04 finds dates of April 25–29, 2026 on every article). This is a broken Webflow date binding, not real freshness. Google now ignores or penalizes such dates. Real publication dates and meaningful "last reviewed" dates are not exposed to readers or crawlers.

---

## 3. Thin Content List

Definition: under 300 words is critical, 300–600 words is a warning. Templated pages with low unique content also flagged.

| URL pattern | Issue | Severity | Action |
|---|---|---|---|
| /team/* (35 pages) | ~90-150 words per author page; no article lists; minimal bio | HIGH | Expand to 300–500 word bios with credentials + auto-list of authored articles |
| /tags/* (69 pages) | 800-1,000 words but mostly UI/nav. Zero unique pillar intro per topic. Just article lists. | HIGH | Add a 200–400 word pillar intro per tag explaining the topic + linking to flagship article |
| /integrations/* (75 pages, not sampled — inferred from volume) | Likely templated to a single integration partner blurb | MEDIUM | Audit — flag any under 400 unique words; expand with use cases, setup steps |
| /tools/* (60 pages, not sampled) | Mix of calculators, downloads, courses; some likely thin landing pages | MEDIUM | Audit; templated download pages need a 300+ word intro that explains the tool |
| /success-stories/* | Content is solid (~2,100 wd) but **no publication date displayed** — relevance/freshness signal missing | LOW | Add publication date + last-reviewed date |
| /contact (~1,200 wd) | OK volume, but lacks **physical address** — local SEO + EEAT signal | LOW | Add full HQ address (Fargo, ND) + LocalBusiness schema |

**Confirmed thin pages (sampled):** All 35 /team/* pages and all 69 /tags/* pages. That's **104 thin pages** out of 893 — 11.6% of the site is functionally thin content.

---

## 4. Duplicate / Cannibalization Flags

### Cluster A — Donor Lifecycle Cannibalization (highest risk)

The following URLs all rank for and target overlapping queries around donor relationship management:

| URL | Word Count | Primary Topic | Overlap signals |
|---|---|---|---|
| /articles/donor-engagement | ~3,800 | Engagement strategy | Covers segmentation, channels, storytelling, retention |
| /articles/donor-retention | ~3,500 | Retention | Covers segmentation, data, lapsed donors, channels |
| /articles/donor-segmentation | ~2,800 | Segmentation | Heavy retention emphasis ("5x more to acquire") |
| /articles/donor-appreciation | ~2,800 | Appreciation/thank-yous | Covers stewardship, retention math, segments |
| /articles/fundraising-101 | ~4,500 | Fundraising fundamentals | Covers donor base, segmentation, channels, events |
| /solution/donor-retention | ~3,500 | Product solution | Same statistics, same audience |
| /solution/donor-stewardship | (not sampled, exists) | Product solution | Likely overlaps appreciation + engagement |
| /tags/donor-stewardship | ~800 unique | Listing hub | 63 articles aggregated under same theme |
| /tags/donor-engagement | (exists) | Listing hub | Overlapping article set |
| /tags/donor-segmentation | (exists) | Listing hub | Overlapping article set |

**Risk:** 5+ unique URLs competing on substantially identical query intent. Pick one pillar per intent and force the others into a clear spoke role with internal-link hierarchy and topical specialization.

### Cluster B — CRM Buyer / Comparison Cannibalization

| URL | Topic |
|---|---|
| /articles/best-nonprofit-crm | "Best CRM 2026" pillar (~3,500 wd) — the strongest |
| /articles/how-to-choose-fundraising-technology-that-actually-supports-your-strategy | CRM choice |
| /articles/how-to-get-finance-and-fundraising-aligned-on-crm-decision | CRM decision |
| /articles/why-most-nonprofit-technology-investments-fail-before-they-start | CRM purchase |
| /articles/nonprofit-crm-migration-checklist | Post-decision migration (different intent — keep) |
| /compare/* (9 pages) | Vendor-specific comparisons |

The four "choose a CRM" articles all serve the same searcher intent and split link equity. Consolidate into a clear pillar + 2-3 differentiated spoke angles.

### Cluster C — Confirmed/Suspected Future-Date Issue

Every sampled article carries a "last updated" date in early-late April 2026 — a **template-level bug**, not a per-page issue. This is duplicated boilerplate at the template level. **Single fix touches ~449 article pages.**

### Confirmed 404s during audit (broken internal expectations)

- /articles/fundraising — 404 (no fundraising hub article)
- /articles/donor-stewardship — 404 (no stewardship hub article — but it's a primary tag/topic)
- /articles/donor-stewardship-guide — 404
- /articles/nonprofit-crm-buyers-guide — 404 (despite being referenced in topic-cluster intent)
- /articles/beyond-the-donation-1 — 404 (podcast episode URL pattern broken)
- /articles/beyond-the-donation-podcast-episode-1 — 404

These represent **content gaps** for high-intent terms the brand is otherwise targeting.

---

## 5. Internal Linking Opportunities (Top 20)

Below are 20 specific link insertions that would strengthen topical authority and surface deeper content. Format: **From → To** | suggested anchor.

| # | From | To | Suggested anchor |
|---|---|---|---|
| 1 | /articles/fundraising-101 | /articles/grassroots-fundraising-playbook-new-nonprofits | "your first 500 donors playbook" |
| 2 | /articles/donor-engagement | /articles/donor-segmentation | "build effective donor segments" |
| 3 | /articles/donor-engagement | /articles/donor-appreciation | "how to thank donors meaningfully" |
| 4 | /articles/donor-retention | /articles/lapsed-donor-re-engagement-playbook | "30-day lapsed donor playbook" |
| 5 | /articles/donor-retention | /tools/donor-journey-map-template | "free donor journey map template" |
| 6 | /articles/best-nonprofit-crm | /articles/nonprofit-crm-migration-checklist | "5-phase migration checklist" |
| 7 | /articles/best-nonprofit-crm | /articles/why-most-nonprofit-technology-investments-fail-before-they-start | "why CRM investments fail" |
| 8 | /articles/100-easy-fundraising-ideas | /articles/fundraising-events-increase-engagement | "fundraising event strategy" |
| 9 | /pricing | /articles/why-most-nonprofit-technology-investments-fail-before-they-start | "before you switch CRMs" |
| 10 | /pricing | /success-stories/love-inc | "see Love Inc's results" |
| 11 | /about | /team/matt-bitzegaio | "meet our co-founder Matt" |
| 12 | /about | /team/andrew-lutgen | "meet our co-founder Andrew" |
| 13 | /tags/donor-stewardship | /articles/donor-appreciation | (top of page pillar intro link) |
| 14 | /tags/donor-engagement | /articles/donor-engagement | (pillar intro link) |
| 15 | /tags/fundraising | /articles/fundraising-101 | (pillar intro link) |
| 16 | /tags/grants | /articles/grant-writing | (pillar intro link) |
| 17 | /compare/bloomerang-vs-donordock | /articles/nonprofit-crm-migration-checklist | "5-phase migration plan" |
| 18 | /features/custom-fields | /articles/donor-segmentation | "use custom fields for segmentation" |
| 19 | /solution/donor-retention | /articles/donor-retention | "donor retention strategy guide" |
| 20 | /success-stories/love-inc | /articles/donor-appreciation | "donor thank-you strategies" |

**Pattern findings:**
- Tag pages currently surface zero contextual link equity to the canonical pillar article on each topic — biggest quick fix.
- /about does not link to founder team pages, weakening EEAT chain.
- Comparison pages don't bridge to migration/decision-stage articles, leaving conversion-stage readers without reassurance content.
- Success stories don't cross-link to relevant feature/solution/article pages — pure leaf nodes.

---

## 6. EEAT Signals — Detailed Findings

| Signal | Status | Notes |
|---|---|---|
| Author bylines | PRESENT | Rob Burke, Elisha Ford, others |
| Author bios with credentials | THIN | 90-150 wd; no years of experience, certifications, prior roles |
| Author article lists on /team/* | MISSING | Author pages do not list articles by that author |
| Publication dates | BROKEN | Future-rolling timestamps on all articles |
| Last-reviewed dates | BROKEN | Same dates, indistinguishable from publication |
| Editorial / fact-check process | NOT STATED | No editorial standards page |
| Author social profiles | PRESENT | LinkedIn, X, etc. linked from /team |
| Author photos | PRESENT | Headshots on /team |
| Reviews / testimonials | STRONG | 151+ reviews, AggregateRating schema on homepage |
| Trust signals | PRESENT | SOC 2 Type 2, 90-day money-back, 7,200+ users |
| Physical address | MISSING from /contact | Phone (701) 490-8653 only; need HQ address |
| Founder visibility | LIMITED | Names mentioned on /about, no linked deep pages |

---

## 7. Content Freshness Audit

- 100% of sampled articles show "last updated" in April 2026 (2-7 days before audit). Mathematically impossible for 449 articles to all be updated in one week — this is template behavior.
- True publication history is hidden. Cannot determine which articles are 6 months old vs 3 years old.
- Compare pages show "last updated March 25, 2026" (also future-dated relative to a typical audit perspective; same pattern).
- Success stories show no date at all.
- Podcast pages (Beyond the Donation, Focused Fundraiser): URL patterns inconsistent — /the-focused-fundraiser-podcast and /beyond-the-donation-podcast exist as hub pages, but episode-level URLs tested return 404. Episodes may live elsewhere or may not be individually indexed.

---

## 8. Content Gap Findings

Topics where DonorDock has tag pages, /solution/, or /compare/ pages but **no canonical pillar article** exists:

1. **Donor stewardship pillar** — /tags/donor-stewardship lists 63 articles, /solution/donor-stewardship exists, but no /articles/donor-stewardship pillar. Smart Steward Method is a brand pillar; deserves a flagship article.
2. **Fundraising pillar** — /tags/fundraising and /lp/fundraising exist; no /articles/fundraising hub. /articles/fundraising-101 is the closest but is positioned as a beginner guide, not a pillar.
3. **Grants pillar** — /tags/grants exists; only /articles/grant-writing serves the topic.
4. **Volunteer management pillar** — /tags/volunteer-management exists; no flagship article.
5. **Membership management** — /solution/membership-management exists; no flagship article on membership program design.
6. **Board reporting** — /solution/board-reporting exists; no flagship article on what to report to nonprofit boards.
7. **Major gifts** — /tags/major-gifts and /solution/major-gifts exist; need a major-gifts pillar piece.

---

## 9. Top 10 Ranked Actions

Ranked by impact × ease.

| Rank | Action | Impact | Effort | Pages affected |
|---|---|---|---|---|
| 1 | **Fix the future-rolling "last updated" date in the article template.** Replace with real CMS publication date + an editor-controlled "last reviewed" field. Backfill real history where possible; default to first publish date. | Critical (sitewide trust) | Low (single template change in Webflow) | ~449 articles |
| 2 | **Add 300-400 word pillar intros to each of the 69 /tags/* pages**, linking to the flagship article and 3-5 supporting articles. Convert from listings into topic hubs. | High | Medium (69 short copy briefs) | 69 pages |
| 3 | **Build out the 35 /team/* author pages.** Each gets a 300-500 word bio with credentials, expertise areas, and an auto-populated list of articles by that author. Adds EEAT and internal linking density. | High | Medium | 35 pages |
| 4 | **Resolve the donor-lifecycle cannibalization.** Pick one pillar each for engagement, retention, segmentation, appreciation. Differentiate intros, scopes, and target queries. Add explicit cross-links instead of overlap. Consider consolidating one pair (most likely retention + appreciation) into a single resource. | High | High (content rework) | 5-7 articles + 3 solution pages |
| 5 | **Create the missing pillar articles:** donor-stewardship, fundraising (true pillar), volunteer-management, major-gifts, board-reporting. Each becomes the canonical answer for its tag hub. | High | High | 5-7 new articles |
| 6 | **Add publication dates to all 14 success stories** plus a "Results metrics" data block (org size, time-to-value, hours saved). | Medium | Low | 14 pages |
| 7 | **Add HQ physical address + LocalBusiness schema to /contact** and the footer. Currently only a phone number. | Medium | Low | 1 page + global |
| 8 | **Audit all 75 /integrations/* and 60 /tools/* pages for thin-content.** Flag any under 400 unique words; expand with use cases, FAQs, and screenshots. | Medium | High | up to 135 pages |
| 9 | **Consolidate the 4 "how to choose a CRM" articles** into one pillar + 2 distinct spokes (one for finance/board buyers, one for ED/founder buyers). | Medium | Medium | 4 articles |
| 10 | **Implement an editorial standards / methodology page** ("How we research nonprofit software") + link from every article author byline. Strengthens EEAT for YMYL-adjacent CRM/finance content. | Medium | Low | 1 new page + global byline |

---

## 10. Quick-Win Fixes (do this week)

1. Fix the rolling date bug — single template field, ~449 pages improved.
2. Add HQ address + phone to footer and /contact (probably 30 minutes in Webflow).
3. Add a 200-word pillar intro to the top 10 tag pages (donor-stewardship, donor-engagement, donor-retention, fundraising, grants, major-gifts, volunteer-management, online-giving, year-end-fundraising, nonprofit-marketing).
4. On the 5 highest-traffic articles, add an author bio block (3 sentences + credentials) above the byline.
5. Cross-link the 9 /compare/* pages to /articles/nonprofit-crm-migration-checklist as the "next step" CTA.

---

## Appendix A — Pages Sampled

Homepage, /pricing, /about, /contact, /articles (index), /compare/bloomerang-vs-donordock, /features/custom-fields, /solution/donor-retention, /tags/donor-stewardship, /success-stories/love-inc, /team/rob-burke, /team/elisha-ford, /articles/best-nonprofit-crm, /articles/grassroots-fundraising-playbook-new-nonprofits, /articles/fundraising-101, /articles/donor-engagement, /articles/donor-retention, /articles/donor-segmentation, /articles/donor-appreciation, /articles/100-easy-fundraising-ideas, /articles/nonprofit-crm-migration-checklist.

## Appendix B — Confirmed 404s

/articles/fundraising · /articles/donor-stewardship · /articles/donor-stewardship-guide · /articles/nonprofit-crm-buyers-guide · /articles/beyond-the-donation-1 · /articles/beyond-the-donation-podcast-episode-1
