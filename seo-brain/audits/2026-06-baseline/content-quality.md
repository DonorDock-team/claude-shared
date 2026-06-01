# Content Quality Audit — donordock.com

**Audit date:** 2026-06-01
**Auditor:** Claude (claude-rank Content Auditor)
**Prior baseline:** [../2026-05-baseline/content-quality.md](../2026-05-baseline/content-quality.md)
**Scope:** Homepage, /pricing, /about, /contact, /compare, /features, /solution, /success-stories, /tags, /team, /articles (sampled across hub, pillar, and topic clusters) + GSC cannibalization data (28-day window)
**Total URLs in sitemap:** 977 (up from 893 in May) — but **articles dropped to 351 (from 449)**; growth is in non-article paths (see velocity note).

**Content Quality Score: 64 / 100** (▲ +6 vs May's 58) — **Trend: IMPROVING**

The score rose because the #1 P0 finding — the sitewide rolling-date bug — is now **FIXED**, and flagship pillar articles now show real in-content internal linking. Score is held back by unresolved thin-content (tags/team), persistent donor-lifecycle cannibalization, and an unexplained ~98-article drop in the sitemap.

---

## 1. Executive Summary

- **P0 ROLLING-DATE BUG: FIXED.** In May, every one of ~449 articles displayed a "last updated" date that auto-rolled to ~5-7 days before audit day (always "just updated") — a broken template binding. On this 2026-06-01 audit, sampled articles now show **static, varied, past-dated** timestamps: best-nonprofit-crm = April 24, donor-engagement = April 28, donor-retention/fundraising-101 = May 5-6. Different articles carry different dates, which is the expected behavior of a real CMS publish/last-reviewed field. The auto-incrementing rolling date is gone. This was the single biggest content-trust risk on the site and it has been resolved.

- **Article count fell from ~449 to 351 in the sitemap (−98, −22%).** This is a major content-engine velocity signal that needs explanation. Either (a) a large batch of thin/low-value articles was pruned or noindexed (a quality-positive move), or (b) a publishing/sitemap regression dropped URLs unintentionally. Net sitemap grew to 977, so the loss is concentrated in /articles/ while /features (98), /integrations (77), /tools (52 from 60), /team (40) shifted. **Action: confirm whether the 98 missing articles were a deliberate prune or an accidental de-index.**

- **Thin content (tags + team) is UNCHANGED.** /tags/donor-stewardship still has ~0 words of unique pillar intro — pure article-card grid. /team/rob-burke still has ~0 words of bio, no authored-article list, no credentials. Items #2 and #3 from May's ranked actions have not been actioned. Tag count is now 62 (from 69); team 40 (from 35).

- **Donor-lifecycle cannibalization PERSISTS** and is now confirmed in live GSC data, not just inferred. "donor engagement" splits across /articles/donor-engagement (pos 32.9) and /lp/donor-engagement; "nonprofit crm" splits across 4 URLs; "donor segmentation" across 3. May's #4 ranked action is outstanding.

- **Internal-linking program is PROGRESSING on flagship pages.** The donor-engagement pillar now carries ~12 in-content links to sibling articles (segmentation, retention, appreciation, storytelling, donor-journey, automation). This is real pillar-cluster wiring on at least the top pillars — a genuine improvement over May. It has NOT reached the tag hubs, which still surface zero contextual links to their canonical pillar.

---

## 2. Content Inventory Snapshot — June vs May

| Type | June Count | May Count | Δ | Notes |
|---|---|---|---|---|
| Articles (/articles/*) | **351** | 449 | **−98** | Velocity flag — prune or regression? Investigate. |
| Feature pages (/features/*) | 98 | 97 | +1 | Stable, substantive |
| Integrations (/integrations/*) | 77 | 75 | +2 | Still likely templated; not re-sampled |
| Tag hubs (/tags/*) | 62 | 69 | −7 | Still zero pillar intros |
| Tools (/tools/*) | 52 | 60 | −8 | Mixed; not re-sampled |
| Team / author (/team/*) | 40 | 35 | +5 | More authors, still ~0-word bios |
| Success stories | 14 | 14 | 0 | Still no displayed dates |
| Compare (/compare/*) | 10 | 10 | 0 | Substantive |
| Solutions (/solution/*) | 12 | 10 | +2 | Strong product-marketing |
| **Total sitemap URLs** | **977** | 893 | **+84** | Growth in non-article paths despite article drop |

---

## 3. Re-Verification of May P0 / Tracked Findings

| May Finding | May Status | June Status | Verdict |
|---|---|---|---|
| **Rolling-date bug (P0 #4, ~449 articles)** | OPEN — all articles future-rolling | Static, varied past dates (Apr 24 / Apr 28 / May 5 / May 6) | **FIXED** |
| 35 thin /team/* author pages | OPEN | 40 pages, still ~0-word bios, no article lists | **STILL OPEN** (worse by count) |
| 69 thin /tags/* hubs | OPEN | 62 hubs, still zero pillar intro text | **STILL OPEN** |
| Donor-lifecycle cannibalization (5+ URLs) | OPEN | Confirmed live in GSC: engagement, nonprofit-crm (4 URLs), segmentation (3 URLs) | **STILL OPEN** |
| ~449-article internal-linking program | OPEN | Flagship pillars now wired (~12 links on donor-engagement); tag hubs still unwired | **PARTIAL — IN PROGRESS** |

---

## 4. Cannibalization — Live GSC Confirmation (28-day)

Branded queries (site:, "donordock", "donordock login") correctly show many URLs and are NOT true cannibalization. The genuine topical splits:

| Query | Competing URLs | Top position | Issue |
|---|---|---|---|
| nonprofit crm | /articles/what-is-a-nonprofit-crm (16.4), /articles/best-nonprofit-crm (37.6), /compare/little-green-light-vs-donordock (21), / (55) | 16.4 | 4 URLs splitting; weak avg position |
| donor segmentation | /articles/donor-segmentation (20.4), /articles/segment-like-you-mean-it (54), /articles/6-donor-segments (57) | 20.4 | 3 URLs — segmentation spokes not clearly subordinate |
| best nonprofit crm | /compare (19.9), /articles/best-nonprofit-crm (26.4) | 19.9 | Hub vs pillar competing |
| donor engagement | /articles/donor-engagement (32.9), /lp/donor-engagement (43) | 32.9 | Article vs landing page |

**Action (carryover from May #4):** designate one canonical per intent; subordinate spokes via internal links and (where appropriate) canonical tags; keep /lp/* out of organic competition with the pillar.

---

## 5. Thin Content — Re-Confirmed

| URL pattern | Issue | Severity | Status |
|---|---|---|---|
| /team/* (40 pages) | ~0-word bios, no credentials, no authored-article list | HIGH | Unchanged from May |
| /tags/* (62 pages) | Pure card grids, zero unique pillar intro | HIGH | Unchanged from May |
| /success-stories/* (14) | Solid content, still no displayed publication date | LOW | Unchanged |
| /contact | Still phone-only; no HQ address / LocalBusiness schema | LOW | Unchanged |

Confirmed thin: 40 team + 62 tag = **102 thin pages** (~10.4% of sitemap; was 104 / 11.6% in May — ratio improved only because total grew).

---

## 6. Content Freshness — June

- **Resolved:** Articles now show meaningful, differentiated dates spanning April 24 → May 6, 2026, all in the past. No future-dated or auto-rolling timestamps observed in sampling.
- **Remaining:** A few articles still surface multiple dates (e.g., donor-retention shows April 25 in FAQ blocks and May 6 in the byline) — minor inconsistency between per-FAQ "last updated" stamps and the article byline date. Worth normalizing so one canonical "last reviewed" date governs the page.
- Success stories still display no date.

---

## 7. Content Gaps (carryover)

Still missing canonical pillar for the donor-stewardship topic: **/articles/donor-stewardship is a confirmed 404** despite /tags/donor-stewardship and /solution/donor-stewardship existing and the Smart Steward Method being a brand pillar. Other May gaps (fundraising pillar, volunteer-management, major-gifts, board-reporting) not re-verified this run; assume open.

---

## 8. June Delta Section

**Improved**
- Rolling-date bug fixed (P0 resolved) — primary driver of the +6 score.
- Flagship pillar internal linking live (~12 contextual links on donor-engagement).
- Thin-page ratio down slightly (10.4% vs 11.6%) as total content grew.

**Regressed / New concerns**
- Article count −98 (−22%) in sitemap — unexplained; could be quality prune (good) or de-index (bad). Highest-priority investigation for July.
- Team pages grew to 40 while bios remain empty — more thin pages, not fewer.

**Unchanged (still open)**
- Tag-hub pillar intros (62 pages).
- Team author bios + article lists (40 pages).
- Donor-lifecycle + nonprofit-crm cannibalization.
- /articles/donor-stewardship 404 / missing stewardship pillar.
- Success-story dates, /contact address.

---

## 9. Top Ranked Actions — June

| Rank | Action | Impact | Effort | Pages |
|---|---|---|---|---|
| 1 | **Investigate the 98 missing articles.** Confirm deliberate prune vs accidental de-index; restore or document. | Critical | Low | up to 98 |
| 2 | Add 300-400 word pillar intros to /tags/* hubs, linking to each canonical pillar. (carryover #2) | High | Medium | 62 |
| 3 | Build out /team/* author bios (300-500 wd, credentials, authored-article list). (carryover #3) | High | Medium | 40 |
| 4 | Resolve donor-lifecycle + nonprofit-crm cannibalization; one canonical per intent; pull /lp/* out of organic competition. (carryover #4) | High | High | 7-9 |
| 5 | Create /articles/donor-stewardship pillar (resolves 404 + anchors the tag hub). | High | Medium | 1 new |
| 6 | Normalize the per-FAQ vs byline "last updated" dates to one canonical last-reviewed field. | Medium | Low | ~351 |
| 7 | Extend the flagship internal-linking pattern from pillars to the rest of the cluster + tag hubs. | Medium | Medium | many |
| 8 | Add publication dates to 14 success stories; HQ address + LocalBusiness schema to /contact. | Medium | Low | 15 |

---

## 10. Quick Wins (this week)

1. Run a crawl-vs-sitemap diff to identify exactly which 98 article URLs left the sitemap — answer the velocity question before anything else.
2. Add the donor-stewardship pillar article (kills a 404 and anchors a 62-page-adjacent topic).
3. Add 200-word pillar intros to the top 10 tag pages.
4. Normalize the duplicate dates on FAQ-bearing articles to a single byline date.
5. Add author bio blocks to the 5 highest-traffic articles.

---

## Appendix A — Pages Sampled
Homepage, sitemap.xml, /articles/donor-engagement, /articles/best-nonprofit-crm, /articles/fundraising-101, /articles/donor-retention, /articles/donor-stewardship (404), /tags/donor-stewardship, /team/rob-burke, plus GSC cannibalization_check (28-day, min 50 impressions, 50 query blocks).

## Appendix B — Confirmed 404 this run
/articles/donor-stewardship (still missing — high-intent stewardship pillar gap).
