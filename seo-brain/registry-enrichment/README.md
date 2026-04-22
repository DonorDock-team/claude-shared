# Registry Enrichment

SEO metadata layered over the Content Registry (`sitemaps/website-sitemap.json`).

We do **not** duplicate URLs. We cross-reference by URL.

## Files

| File | Purpose |
|---|---|
| `url-enrichment.json` | Per-URL SEO metadata |

## Per-URL fields

- `url` — matches `sitemaps/website-sitemap.json` entry
- `pillar` — assignment from `strategy/pillars.md`
- `cluster` — keyword cluster from `strategy/keyword-universe.md`
- `primary_keyword` — target keyword
- `intent` — informational / commercial / transactional / navigational
- `content_type` — pillar-page / article / landing / comparison / FAQ / tool
- `aeo_structure` — { has_faq_schema, is_paa_formatted, has_citation_worthy_paragraphs }
- `citability_score` — from `rank-citability` most recent run
- `internal_links_in` — count of inbound internal links
- `internal_links_out` — count of outbound internal links
- `last_audited` — ISO date
- `recommended_actions` — array of strings

## Update cadence

- On publish of new content — by content creation skills
- Monthly — refreshed by audit pipeline
- Weekly — link counts refreshed by crawl
