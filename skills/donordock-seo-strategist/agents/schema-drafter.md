# Schema Drafter Subagent

## Purpose

Generate copy-paste-ready JSON-LD schema for any URL + content type. Takes into account:
- The pillar assignment (affects `articleSection`, breadcrumb)
- The primary keyword + visible content (schema must match page content)
- Any competitor/comparison context (affects Review/AggregateRating shape)
- The locked content-standards.md schema requirements

## Inputs

- Target URL (existing or to-build)
- Content type (pillar / article / comparison / feature / solution / team / integration / podcast-episode / dataset / home)
- Visible content summary (headings, body text, FAQ Qs, CTA)
- Author name
- Pillar claim (optional, inferred if not provided)

## Process

### 1. Load context
- `references/schema-templates.md` (this skill) — base templates
- `seo-brain/strategy/content-standards.md` — required schemas per content type
- If comparison page: `seo-brain/audits/2026-04-baseline/competitors/{competitor}.md` for real review quotes

### 2. Select template
Match content type to template in schema-templates.md.

### 3. Populate with real content
- Pull actual headings, FAQ Qs, author bio, pricing
- No `REPLACE_WITH_*` placeholders in output
- If real content unavailable for a required field, flag and request from user

### 4. Validate before output
- Parse as JSON (no trailing commas)
- Flat `@graph` (no nesting)
- `@id` on top-level nodes
- Canonical URLs

### 5. Return deliverable

```markdown
# Schema for [URL]

**Content type:** [type]
**Pillar:** [pillar name]

## Paste instructions

In Webflow Designer:
1. Navigate to [URL] page
2. Page Settings → Custom Code → [Inside `<head>` tag / Before `</body>` tag]
3. Delete any existing JSON-LD block
4. Paste the block below
5. Save and publish
6. Validate at https://search.google.com/test/rich-results

## JSON-LD Block

```json
[Complete valid JSON-LD here]
```

## Validation results

- JSON parse: ✅ VALID
- Schema.org spec: [manually verify at validator.schema.org]
- Google Rich Results eligible: [FAQ / HowTo / Product / etc.]

## Visibility check

Confirmed present in schema text:
- [list of page-visible questions/answers/quotes that match schema]

## Cross-reference

Matches content-standards.md requirements for [content type]: ✅
Matches pillar strategy for [pillar]: ✅

## Follow-up

After deploy:
- Wait 24-72 hours
- Check GSC → Enhancements → FAQ / HowTo / Product for detection
- Re-submit URL via gsc.submit_url if not detected after 72 hours
```

---

## Content-type-specific rules

### Pillar page schema
- WebPage + SoftwareApplication + Offer + AggregateRating + FAQPage (10+ Qs) + BreadcrumbList + Organization ref + Person (author)
- `mainEntity` in WebPage points to the SoftwareApplication or primary entity
- FAQ Qs drawn from `aeo-questions.md` for that pillar, matched to visible H3/H4 Q&A on the page

### Article/blog schema
- Article or BlogPosting (prefer Article for newer content)
- Single BlogPosting/Article script (NOT two — that was a Phase 1 bug)
- Person (author) with `sameAs` LinkedIn + `knowsAbout`
- Publisher = DonorDock Organization
- `datePublished` + `dateModified` in ISO 8601 (no human-readable format)
- If step-format → add HowTo
- If FAQ section present → add FAQPage

### Comparison page schema
- SoftwareApplication + Offer + AggregateRating with `isBasedOn` (G2/Capterra URLs)
- Review × N with real customer quotes (extract from /compare/{competitor}-vs-donordock live page via curl)
- FAQPage with 6-8 competitor-specific Qs
- BreadcrumbList (Home → Compare → {Competitor})
- Use extracted reviews, NOT placeholders

### Feature page schema
- SoftwareApplication (feature-scoped, e.g., `applicationSubCategory: "Recurring Giving"`)
- BreadcrumbList
- HowTo if the page covers "how to use [feature]"
- ImageObject for screenshots

### Solution page schema
- WebPage + FAQPage + BreadcrumbList
- SoftwareApplication reference for the umbrella product

### Team bio page schema
- ProfilePage + Person with full fields (jobTitle, worksFor, knowsAbout, sameAs, image, description)
- If author is departed (Elisha, Sami, Sarah, Scott): add `description` with "Former [Title] at DonorDock"

### Integration page schema
- SoftwareApplication (the integration combo)
- HowTo (integration setup steps)
- BreadcrumbList
- Product partner reference

### Podcast episode schema
- PodcastEpisode + VideoObject (if video on YouTube)
- Associated with PodcastSeries `@id`
- Person schema for guest
- Transcript link if available

### Dataset (for State of Stewardship report)
- Dataset + CreativeWork
- `creator` = Organization
- `isAccessibleForFree` true
- `license` CC-BY-4.0 or similar
- `keywords` array
- `distribution` pointing to PDF + HTML microsite

### Homepage schema
- Organization + WebSite + SoftwareApplication + Offer + AggregateRating
- Single flat @graph with all five

---

## Schema quality enforcement

Before returning any schema:

- [ ] JSON parses via `json.loads()` — no trailing commas
- [ ] Only ONE `@graph` level (flat structure)
- [ ] `@context: https://schema.org` at top
- [ ] Every top-level object has `@id` and `@type`
- [ ] Canonical URLs with `#fragment` IDs
- [ ] No Unicode surrogate pairs / emoji issues
- [ ] FAQ Qs exactly match visible H2/H3 + Q text on page
- [ ] Review entities have real quotes (not placeholders)
- [ ] AggregateRating matches site-wide facts (4.8 / 200+ reviews per brand-positioning.md)
- [ ] Organization `@id` references match across files

---

## Output format

Return markdown with:
1. Paste instructions (specific to Webflow)
2. The JSON-LD block (clean, ready to copy)
3. Validation results
4. Visibility cross-check (schema text must match visible content)
5. Pillar/standards cross-reference confirmation
6. Follow-up steps (GSC validation)

---

## Edge cases

### Compare page where customer reviews are sparse
Pull the 3-5 best quotes from G2/Capterra via web search or customer success team. If <3 reviews exist, pause and ask Rob.

### Article by departed author
Use Option 1 policy from eeat-signals.md: keep byline + add "Former" note in Person `description`. Schema still includes the author's Person object.

### Pillar page that targets multiple keywords
Use primary keyword in `description`; include secondary in body text (not schema). FAQ Qs should cover all primary + secondary keyword intents.

### Dataset schema for research report
Only ship Dataset schema when the report is publicly accessible. Include `isAccessibleForFree` + `license` explicitly.

---

## Don't-do list

- Don't include `REPLACE_WITH_*` placeholders in output
- Don't nest `@graph` inside `@graph`
- Don't duplicate `@id` values
- Don't use human-readable dates — always ISO 8601
- Don't claim facts not in brand-positioning.md (pricing, review count, founder names)
- Don't invent review content — extract from live page or customer success team
- Don't deploy schema that hasn't been validated
