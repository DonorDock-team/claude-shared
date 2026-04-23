# Content Validation Checklist

Canonical pre-publish checklist for every piece of DonorDock content. Based on `seo-brain/strategy/content-standards.md` — if they conflict, content-standards.md wins.

Use this via the content-validator subagent (`agents/content-validator.md`) or apply inline for quick checks.

---

## Universal (every piece)

- [ ] **Pillar tagged** — one of the 7 locked pillars; if not, flag as off-strategy
- [ ] **Primary keyword identified** — and confirmed against keyword-universe.md + GSC
- [ ] **Target URL confirmed** — either existing or newly specified
- [ ] **No prohibited language** — see section below
- [ ] **Action Board** spelled as two words (flag "ActionBoard")
- [ ] **Pricing messaging correct** — $500/mo, 1% platform fee, unlimited contacts, no long-term contracts. Never "free processing" or "no platform fees."
- [ ] **Smart Stewardship framing** — on pillar pages, comparison pages, and any thought-leadership content
- [ ] **Named author byline** — visible + linked to `/team/{slug}` + Person schema in JSON-LD

---

## Pillar pages (>2,000 words)

- [ ] H1 includes primary keyword
- [ ] TL;DR block immediately after H1 (40-word summary in blockquote or styled paragraph)
- [ ] Introduction paragraph 40-60 words leading with direct answer/definition
- [ ] Table of contents (auto-generated from H2s if template supports)
- [ ] 3-8 question-format H2s
- [ ] H3 sub-sections within each H2 as needed
- [ ] At least one numbered/bulleted list (HowTo schema candidate)
- [ ] At least one comparison table where competitor content relevant (semantic `<table>`, not styled divs)
- [ ] At least one original data point OR named-source citation
- [ ] FAQ section at bottom with 5-10 Qs from aeo-questions.md
- [ ] 15-25 internal links — body contextual; link UP to other pillars + LATERALLY to 3-5 sibling pieces
- [ ] Related articles section (3-5)
- [ ] Pillar-appropriate CTA (demo, trial, gated asset)

**Schema required on pillar page:**
- [ ] WebPage with `@id`, `description`, `breadcrumb`
- [ ] BreadcrumbList
- [ ] FAQPage with 10+ Question entities
- [ ] SoftwareApplication or Product where product is central
- [ ] Person schema for named author

---

## Supporting articles (1,000-2,000 words)

- [ ] H1 includes primary keyword
- [ ] TL;DR block (optional but preferred)
- [ ] Introduction 40-60 words
- [ ] 3-6 question-format H2s
- [ ] At least one named-source citation
- [ ] FAQ section with 3-5 Qs from aeo-questions.md
- [ ] Link UP to pillar page (contextual body link, not just footer)
- [ ] Link LATERALLY to 2-3 sibling articles
- [ ] Named author byline with Person schema

**Schema required:**
- [ ] Article or BlogPosting with full fields (headline, author, datePublished, dateModified, publisher, image, description)
- [ ] Person schema for author
- [ ] BreadcrumbList
- [ ] FAQPage if FAQ present
- [ ] HowTo if step-format content

---

## Comparison pages (/compare/*)

- [ ] H1 format: "[Competitor] vs DonorDock: [Meaningful differentiator]"
- [ ] TL;DR paragraph comparing directly
- [ ] Semantic `<table>` comparison (NOT styled divs — required for table-snippet eligibility and AI parsing)
- [ ] Feature-by-feature comparison row set
- [ ] Pricing comparison row with transparent numbers
- [ ] Named customer switcher testimonial (org + person)
- [ ] Migration-focused CTA (not just demo)
- [ ] FAQPage schema with 6-8 competitor-specific questions

**Schema required:**
- [ ] SoftwareApplication
- [ ] Offer with UnitPriceSpecification
- [ ] AggregateRating with `isBasedOn` (G2/Capterra)
- [ ] Review × N (customer quotes)
- [ ] FAQPage
- [ ] BreadcrumbList
- [ ] WebPage

---

## Feature pages (/features/*)

- [ ] Feature name in H1
- [ ] One-sentence definition in first paragraph
- [ ] 3-5 feature-use-case H2s
- [ ] Related features internal linking
- [ ] Integration references if applicable
- [ ] Product screenshots with alt text + ImageObject schema
- [ ] HowTo schema if applicable

---

## Prohibited language (never use)

- "small nonprofit" / "first CRM" / "solo ED" / "one-person shop" / "tiny nonprofit"
- "Church," "congregational," "tithing" as DonorDock target audience
- "Starting a nonprofit" as target content
- "No platform fees" / "free processing" / "free online giving"
- "Best for every nonprofit"
- "ActionBoard" (must be "Action Board")
- "SmartStewardship," "SmartStewardMethod," "SmartNudges" (must be spaced)
- Em-dash ( — ) in public-facing content (use comma or split sentence; see brand-identity voice rule)

**If any of these appear in a draft, flag as REVISION REQUIRED.**

---

## Schema validation rules

Every JSON-LD block must:

- [ ] Parse as valid JSON (no trailing commas, matched braces)
- [ ] Use flat `@graph`, not nested `@graph` inside `@graph`
- [ ] Include `@id` on every top-level node
- [ ] Use canonical URLs with `#` fragments for internal references
- [ ] Not contain `REPLACE_WITH_*` placeholder tokens
- [ ] Visible content MUST match schema text (FAQ Qs in schema match H2/H3 on page)
- [ ] Use `https://schema.org` context

**Validators:**
- `https://validator.schema.org/` — strict spec compliance
- `https://search.google.com/test/rich-results` — Google rich-result eligibility
- `jsonlint.com` — quick syntax check

---

## Image standards

- [ ] Every image has `width` + `height` as integer pixel values (NOT "Auto")
- [ ] LCP image has `fetchpriority="high"` + `loading="eager"` + `<link rel="preload" as="image">` in head
- [ ] Non-LCP images have `loading="lazy"`
- [ ] `srcset` + `sizes` on responsive images
- [ ] Alt text describes image purpose (not filename or "decorative")
- [ ] File format: WebP preferred; MP4/WebM for video
- [ ] File size: <200 KB per image where possible

---

## Meta tag standards

- [ ] `<title>`: 50-60 characters, includes primary keyword
- [ ] `<meta name="description">`: 150-160 characters, includes primary keyword + soft CTA
- [ ] `<link rel="canonical">`: self-referencing unless intentional cross-domain canonical
- [ ] OpenGraph: og:title, og:description, og:url, og:image (1200×630), og:type, og:site_name
- [ ] Twitter: twitter:card=summary_large_image, twitter:title, twitter:description, twitter:image, twitter:site

---

## Internal linking density target

- Pillar article: 15-25 contextual internal links
- Supporting article: 5-15 contextual internal links
- Top-traffic articles (e.g., /articles/100-easy-fundraising-ideas): 25-40 contextual links
- Every article: 1+ link UP to pillar, 2-3 LATERAL links to sibling articles

---

## Final review pass — required agents

Before publishing, run in parallel:

1. **content-validator** (this skill) — structure, schema, internal linking, pillar tagging
2. **brand-critic** (brand-identity skill) — voice, vocabulary, tone-context match
3. **researcher** (brand-identity skill) — fact-check, source verification

Collect all three reviews → revise once → publish.

Don't loop endlessly. One revision pass is the standard.

---

## Output format for validation

When the content-validator subagent returns, it should emit:

- **Verdict:** PASS / NEEDS REVISION / MAJOR REWRITE
- **Pillar assignment confirmed:** [pillar name + URL]
- **Primary keyword confirmed:** [keyword] (GSC data: position X, Y impressions)
- **Required fixes:** itemized list of violations with specific line/element references
- **Schema recommendations:** specific JSON-LD blocks to add (reference schema-drafter if complex)
- **Summary:** 2-3 sentence overall assessment
