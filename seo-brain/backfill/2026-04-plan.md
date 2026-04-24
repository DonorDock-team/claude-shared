# Phase 4.5 — Existing Article Backfill Plan

**Status:** Pending (not yet started)
**Owner:** Rob + `donordock-seo-strategist` → `strategy-advisor` + `content-validator`
**Scope:** All ~290 existing published articles in the Webflow Articles collection (`6532889f2379aa018d3520b7`)

---

## Why This Phase Exists

As of 2026-04-24, we shipped three new required CMS fields on Articles:
- `pillar` (single reference → Content Pillars)
- `seo-keywords` (comma-separated text)
- `article-faqs` (multi-reference → Article FAQs)

All three are empty on every pre-2026-04-24 article. Without them, the dynamic Webflow template schema emits empty/missing bindings (e.g., `articleSection` and `isPartOf` blank, `keywords` blank, FAQPage not generated). The entire purpose of the template-driven schema system depends on these fields being populated across the full corpus.

This phase brings the back catalog up to parity with the new article-creation standard.

---

## Scope by the Numbers (as of 2026-04-24)

| Metric | Count |
|---|---|
| Total published articles | 290 |
| Articles with `pillar` set | 0 |
| Articles with `seo-keywords` set | 0 |
| Articles with `article-faqs` set | 0 |
| Articles with `canonical-url` set | unknown — audit early |
| Articles with `alt-text-feature-image` set | unknown — audit early |

---

## Process (batch-based)

Run in batches of ~20 articles. Review each batch with Rob before publishing to CMS.

### Per-batch workflow

1. **Fetch batch** — `list_collection_items` with `limit: 20`, sort by `lastPublished desc`. Skip any already backfilled.

2. **Per article — run `strategy-advisor` subagent** with inputs:
   - Full article HTML body
   - Current title, slug, meta description
   - Current categories/tags (if any)
   
   Returns:
   - Pillar assignment (one of 7 locked pillars) + confidence
   - Primary keyword + GSC data (position, monthly impressions)
   - 3–5 long-tail secondary keywords from pillar keyword-universe
   - WRITE / REFRESH / RETIRE verdict (for genuinely off-strategy articles — flag for Rob review)
   - 4–6 suggested FAQ questions drawn from article body + pillar-matched aeo-questions.md

3. **Per article — check for existing FAQ reuse** before creating new ones:
   - `list_collection_items` on Article FAQs collection
   - Semantic match suggested FAQs against existing FAQ names
   - Reuse existing FAQ IDs when question is substantively the same

4. **Per article — generate FAQ answers** (40–100 words each) for any newly-created FAQs, using article body as source material. Run through brand-positioning.md banned-term check.

5. **Per article — build the backfill payload**:
   ```json
   {
     "id": "[article-id]",
     "fieldData": {
       "name": "[preserved]",
       "slug": "[preserved]",
       "pillar": "[chosen-pillar-item-id]",
       "seo-keywords": "[3-10 comma-separated keywords]",
       "canonical-url": "https://www.donordock.com/blog/[slug]",
       "alt-text-feature-image": "[if currently null, generate from title + main-image context]",
       "article-faqs": ["[faq-id-1]", "[faq-id-2]", ...]
     }
   }
   ```

6. **Human review gate** — Rob reviews the 20-article batch output:
   - Pillar assignments look right?
   - Keywords map to real search intent?
   - FAQ questions are ones a reader would actually ask?
   - Any RETIRE candidates? (Articles that don't fit the upmarket ICP — solo-ED pieces, "first CRM" pieces, church-specific pieces should be flagged for delete or redirect, not rescue.)

7. **Publish batch** — update all 20 articles, publish Article FAQs collection, publish Articles collection. Verify 3 random articles via curl + Rich Results Test.

8. **Track in spreadsheet** — append batch results to `seo-brain/backfill/2026-04-articles-tracking.md`:
   | Slug | Pillar | Keywords | FAQs created | FAQs reused | Verdict | Date |

---

## Pillar Distribution Target

Based on current content-pillar mix and strategy-advisor sampling of the first 30 articles, expected distribution across 290 articles (rough estimates, will adjust after first 2 batches):

| Pillar | Expected ~# articles |
|---|---|
| Donor Stewardship | 60–80 |
| Donor Engagement | 45–60 |
| CRM | 30–45 |
| Fundraising Strategy | 40–55 |
| Online Giving | 20–30 |
| Donor Retention | 20–30 |
| AI for Nonprofits | 5–15 |
| **RETIRE candidates** | 15–30 (off-ICP, outdated, thin content) |

If the distribution diverges significantly from this (e.g., 200 articles mapped to one pillar), investigate — it usually means the topic is being over-interpreted and needs tighter pillar rules.

---

## RETIRE Criteria (flag for Rob decision, don't auto-delete)

An article is a RETIRE candidate if it:
- Explicitly targets solo EDs, "small nonprofits," "first CRM," congregational churches, or other prohibited ICP per brand-positioning.md
- Contains factually-outdated pricing (≥2 years stale), discontinued feature references, or competitor claims that have since changed
- Is <500 words AND has no visible traffic in GSC (content-thin + orphan)
- Duplicates newer coverage of the same topic without adding distinct value

Don't delete without Rob's sign-off. Redirect candidates get a 301 to the pillar page or a closer alternative article.

---

## Timeline + Effort

- **Per batch:** ~2 hours (20 articles × ~5 min avg, plus human review)
- **Total batches:** ~15
- **Total wall time:** 15–30 hours (spread over 4–6 weeks, 2–3 batches per week)
- **Can run in parallel with:** Phase 5 (AI citation tracking), Phase 6 (automation), Phase 7 (dashboard)

---

## Success Criteria

- 100% of articles (minus RETIRE) have `pillar`, `seo-keywords`, `canonical-url`, `alt-text-feature-image`, and ≥3 `article-faqs` populated
- Random 20-article sample passes Google Rich Results Test with BlogPosting + FAQPage both detected
- Pillar distribution looks reasonable (no single pillar >35% of corpus)
- Article FAQs collection has 200–500 unique items with healthy reuse (each FAQ tied to 1.5–3 articles on average)
- GSC shows measurable uplift in article-level impressions within 60 days of completion (baseline: 1.25M imps / 8,848 clicks / 0.71% CTR from April baseline audit)

---

## Output Artifacts

- `seo-brain/backfill/2026-04-articles-tracking.md` — batch-by-batch tracking sheet
- `seo-brain/backfill/retire-candidates.md` — list of RETIRE flagged articles awaiting Rob decision
- Updated Article FAQs collection — ~200–500 reusable FAQ items
- Updated Articles collection — 260+ articles fully backfilled
