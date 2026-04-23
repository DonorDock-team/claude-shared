# Content Standards

**Locked:** 2026-04-23
**Owner:** Rob Burke (CMO)
**Authority:** brand-positioning.md (positioning rules) — this doc covers structure/schema/voice
**Refresh:** Quarterly

Mandatory structural, schema, and voice requirements for every piece of published content. Enforced at pre-publish. This doc is the checklist every article/page/schema/ad passes through before going live.

---

## Voice guardrails (extend brand-identity skill)

- **Tone:** Warm, practical, operationally grounded. Never corporate-jargon-heavy.
- **Person:** Mostly second-person ("you"), occasional first-person plural ("we") when speaking as DonorDock, first-person singular when explicitly author-bylined.
- **Examples:** Lead with customer / fundraiser reality, not product feature list.
- **Smart Stewardship framing:** Every pillar piece opens by connecting the topic to Smart Stewardship methodology. Not every article — but every pillar and every comparison.
- **NOT allowed:**
  - "Small nonprofit" / "first CRM" / "solo ED" / "one-person shop" in DonorDock positioning
  - "Church" / "congregational" / "tithing" as target audience
  - "Starting a nonprofit" as target content
  - "Free platform fees" / "no processing fees" / "free online giving" (we charge 1%)
  - "Best for every nonprofit" (we're not — we're for growing and mid-sized)
- **Always use:** Action Board (two words), Smart Stewardship, Smart Steward Method, Smart Nudges, Otto, TipBack®

---

## Required article structure

### Pillar articles (>2,000 words)
1. **H1** — includes primary keyword; avoids DonorDock brand name unless brand article
2. **TL;DR block** immediately after H1 — 40-word summary in `<blockquote>` or styled `<p>` — answer the headline question directly (AEO-critical)
3. **Introduction paragraph** — 40-60 words leading with definition/direct answer
4. **Table of contents** (auto-generated from H2s)
5. **Body** organized in **question-format H2s** (3-8 per article)
6. **H3 sub-sections** as needed within each H2
7. **Numbered or bulleted lists** where content is sequential or enumerable (HowTo schema eligible)
8. **Comparison tables** where relevant (ItemList + Product schema eligible)
9. **Original data point or named-source citation** at least once (E-E-A-T signal)
10. **FAQ section** at bottom — 5-10 Qs from aeo-questions.md pool
11. **Author byline block** — named author, headshot, "About the author" blurb
12. **Related articles section** — 3-5 contextually linked pieces (not just chronological recent posts)
13. **Primary CTA** — pillar-appropriate (demo, trial, gated asset download)

### Supporting articles (1,000-2,000 words)
- All of the above EXCEPT TOC optional and FAQ is 3-5 Qs
- Must link UP to pillar page (contextual in-body link, not just related-posts footer)
- Must link LATERALLY to 2-3 sibling articles in same pillar

### Comparison pages (/compare/*)
- H1 format: "[Competitor] vs DonorDock: [Meaningful differentiator]"
- TL;DR paragraph directly comparing
- Comparison table (semantic `<table>`, not styled divs — for table-snippet eligibility and AI parsing)
- Feature-by-feature table
- Pricing comparison row (transparent numbers)
- FAQPage schema with 6-8 competitor-specific Qs
- Review/AggregateRating schema where reviews exist
- Customer switcher testimonial (named org + person)
- Migration CTA (not just demo)

### Feature pages (/features/*)
- SoftwareApplication schema required
- Product photos/screenshots (ImageObject schema)
- 3-5 feature-use-case H2s
- "How [feature] works" HowTo schema
- Related features internal linking
- Integration references if applicable

### Solution pages (/solution/*)
- ICP-specific opening ("For growing nonprofit development teams...")
- Problem statement before solution
- 3-5 outcome-oriented H2s
- Customer success testimonial specific to solution
- FAQPage schema

---

## Required schema markup by content type

| Content type | Required JSON-LD schemas |
|---|---|
| Homepage | Organization + WebSite (with SearchAction) + SoftwareApplication + Offer + AggregateRating |
| /pricing | Organization ref + SoftwareApplication + Offer + UnitPriceSpecification + AggregateRating + FAQPage + BreadcrumbList + WebPage |
| /compare/* | SoftwareApplication + Offer + Review × N + AggregateRating + FAQPage + BreadcrumbList + WebPage |
| /solution/* | WebPage + SoftwareApplication + FAQPage + BreadcrumbList |
| /features/* | WebPage + SoftwareApplication + BreadcrumbList |
| /articles/* | Article/BlogPosting + Person (author) + Organization (publisher) + BreadcrumbList + FAQPage (if FAQ exists) + HowTo (if step-format) + ImageObject |
| /team/* | ProfilePage + Person + Organization |
| /integrations/* | WebPage + SoftwareApplication + HowTo (integration setup) |
| /faq | FAQPage (flat @graph, NOT nested) with all Question entities |
| /glossary/* (future) | DefinedTerm + FAQPage + BreadcrumbList |
| /focused-fundraiser-podcast | PodcastSeries + BreadcrumbList |
| /articles/beyond-the-donation-episode-* | PodcastEpisode + VideoObject + Article + Person |
| /webinars-events/* | Event + Organization |

---

## Schema quality rules

1. **JSON must be valid** — validate every block before publish (jsonlint.com or validator.schema.org)
2. **No trailing commas** — 6 of 9 compare pages failed this at Phase 1 baseline
3. **No duplicate types** (don't ship 2 BlogPosting scripts per article)
4. **Flat @graph, not nested** — nested @graph can cause Google Rich Results Test parse failure
5. **No placeholder data** — no `REPLACE_WITH_*` tokens in production schemas
6. **Match visible content** — FAQ schema questions MUST match visible H2/H3 + answer text
7. **Use canonical URLs** with #fragment IDs for internal cross-references (e.g., `#software`, `#faq`)
8. **Include `@id`** on every top-level node

---

## Internal linking rules

1. **Every article links UP to pillar** (1+ contextual body link to pillar page)
2. **Every article links LATERALLY to 2-3 sibling articles** in same pillar cluster
3. **Every article can link DOWN** to more tactical articles in same pillar
4. **Every pillar page links to 15-25 supporting articles** (contextual in-body, not just footer)
5. **Homepage links to all 7 pillar pages** in a "Popular Topics" or "Guides" block
6. **Anchor text:** descriptive, keyword-aligned (never "click here" or "read more")
7. **Link density target:** 5-15 internal body links per 1,500+ word article
8. **Top-traffic articles** (e.g., /articles/100-easy-fundraising-ideas) should have 25-40 contextual links

---

## Image + media standards

1. **Every image** has `width` + `height` as integer pixel values (for CLS prevention)
2. **LCP image** has `fetchpriority="high"` + `loading="eager"` + `<link rel="preload" as="image">`
3. **All other images** have `loading="lazy"`
4. **`srcset` + `sizes`** on images displayed at multiple sizes (use Webflow Responsive Images)
5. **Alt text** describes image purpose (not filename)
6. **File format:** WebP for static, MP4/WebM for video
7. **File size:** < 200 KB per image where possible
8. **No `width="Auto"` or `height="Auto"`** as HTML attributes (invalid; use CSS instead)

---

## Meta tag standards

Every page must have:
- `<title>`: 50-60 characters, includes primary keyword
- `<meta name="description">`: 150-160 characters, includes primary keyword + CTA
- `<link rel="canonical">`: self-referencing unless intentional canonical
- `<meta property="og:title">`: match page H1 or <title>
- `<meta property="og:description">`: match or extend meta description
- `<meta property="og:url">`: canonical URL
- `<meta property="og:image">`: 1200x630 social share image
- `<meta property="og:type">`: article / website / product as appropriate
- `<meta name="twitter:card">`: summary_large_image
- `<meta name="twitter:site">`: @donordock (or brand handle)
- `<meta name="twitter:title">`, `twitter:description`, `twitter:image`

---

## Pre-publish checklist

Every piece of content passes this before going live:

- [ ] Tagged to one of the 7 pillars
- [ ] Primary keyword identified and on target URL
- [ ] H1 includes primary keyword; TL;DR block below H1
- [ ] Question-format H2s where intent aligns
- [ ] FAQ section with 3-10 Qs from aeo-questions.md pool
- [ ] Named author byline + /team/{slug} link
- [ ] 5-15 internal body links (including 1+ to pillar + 2-3 sibling articles)
- [ ] 1+ original data point or named-source citation
- [ ] All required schemas deployed (see table above)
- [ ] Schema JSON validated (no trailing commas, no nested @graph, no placeholders)
- [ ] Images have width/height + alt text + correct loading attributes
- [ ] Meta title (50-60 char), meta description (150-160 char), canonical, OG, Twitter all present
- [ ] No prohibited language (small nonprofit, first CRM, solo ED, church, no platform fees)
- [ ] Smart Stewardship framing on pillar/compare pages
- [ ] "ActionBoard" corrected to "Action Board" if copy-pasted from older content
- [ ] Links verified (no 404s)
- [ ] Mobile preview checked
- [ ] Published from a named CMS user (not template default)

---

## Enforcement mechanism for Phase 3+

### How content standards enforced at pre-publish
- **Pre-publish validation** to be built into the `donordock-seo-strategist` skill (Phase 3) — checks all rules in this doc before allowing publish
- **ff-article-pipeline** (weekly 2-article automation) must load this doc at runtime and enforce rules (Phase 4)
- **Monthly audit automation** (Phase 6) flags any existing pages that drift from these standards

### Human review required
- Anything the strategist skill flags as non-compliant
- Any new prohibited-language attempt
- Any pricing / platform fee / numerical claim
- Competitor comparison claims

---

**This doc supersedes any conflicting guidance in older brand docs. Updates require Rob's approval and a commit starting with `content-standards:`.**
