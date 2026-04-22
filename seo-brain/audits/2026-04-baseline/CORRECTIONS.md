# Audit Corrections — 2026-04-22

After Rob's review, we re-verified audit findings against the live site. Recording corrections here so the Phase 2 strategy doesn't build on bad facts.

## Corrections (audit was wrong)

### 1. Footer URLs
**Audit claimed:** `/customers`, `/success-stories`, `/solutions`, `/reviews` all 404 and linked from footer
**Reality:** Footer links point to:
- "Success stories" → `/customer-success` ✔ 200
- "Solutions" → `/solutions-overview` ✔ 200
- `/reviews` and `/customers` are NOT linked from the footer — they simply don't exist (opportunities to build, not broken links)

**Root cause:** The vertical-auditor agent fabricated common B2B SaaS URL patterns instead of reading the actual footer HTML.

### 2. FAQPage schema breadth
**Audit claimed:** FAQPage schema only on `/faq` and `/compare/network-for-good-vs-donordock`
**Reality (verified via direct HTML inspection 2026-04-22):**

| Page | FAQPage schema | Valid JSON? |
|---|---|---|
| /faq | yes | yes (but nested `@graph`) |
| /pricing | **NO** (visible FAQ exists, no schema) | n/a |
| /compare/bloomerang-vs-donordock | no | **invalid** |
| /compare/donorperfect-vs-donordock | no | **invalid** |
| /compare/givebutter-vs-donordock | no | valid |
| /compare/network-for-good-vs-donordock | yes | **invalid** |
| /compare/neon-crm-vs-donordock | yes | **invalid** |
| /compare/etapestry-vs-donordock | yes | **invalid** |
| /compare/little-green-light-vs-donordock | yes | **invalid** |
| /compare/salesforce-vs-donordock | no JSON-LD at all | — |
| /compare/bonterra-vs-donordock | no JSON-LD at all | — |
| /solution/donor-stewardship | yes | valid |
| /solution/major-gifts | yes | valid |
| /solution/annual-fund | yes | valid |
| /solution/membership-management | yes | valid |
| /solution/volunteer-tracking | yes | valid |
| /solution/grants, /solution/events-and-fundraisers, /solution/recurring-giving, /solution/program-management | 404 (don't exist) | — |
| /features/moves-management | no (visible FAQ exists) | n/a |
| /features/contact-management, /features/email-marketing, /features/text-messaging, /features/project-management, /features/recurring-donations | no FAQ schema | n/a |

**Key finding:** Even where FAQ schema text EXISTS on compare pages, 6 of 9 compare pages ship INVALID JSON-LD, which Google discards. So functionally, Google may see FAQ schema on fewer pages than the raw text suggests.

### 3. Pricing page FAQ
**Audit claimed:** "Pricing missing FAQ"
**Reality:** Pricing page has VISIBLE "Frequently asked" section, but NO FAQPage schema markup. The visible content exists; what's missing is the JSON-LD that tells Google it's a FAQ.

## Findings CONFIRMED against live site

### 1. Neon compare page H1 typo
`<h1>Network for Good vs DonorDock</h1>` on `/compare/neon-crm-vs-donordock`. Rob: this is a real live bug, not an audit error. URL slug is neon-crm, page title is "Neon CRM vs DonorDock," but H1 is wrong competitor.

### 2. Invalid JSON-LD on compare pages
6 of 9 compare pages ship invalid JSON that Google cannot parse: bloomerang, donorperfect, etapestry, little-green-light, neon-crm, network-for-good. Plus bonterra and salesforce have NO JSON-LD at all. Only givebutter has valid JSON-LD.

### 3. Duplicate BlogPosting schema on articles
`/articles/best-nonprofit-crm` ships 2 BlogPosting scripts:
- Block 1: `datePublished: "2026-03-25T17:55:01.187Z"` (ISO 8601 — correct)
- Block 2: `datePublished: "Mar 25, 2026"` (human-readable — incorrect format)

Both have same author (Rob Burke). Google picks one non-deterministically. Schema validators may flag Block 2's date format as invalid.

### 4. Missing pages (opportunities, not broken links)
- `/reviews` — 404, not linked from footer. Build for AEO citation aggregation.
- `/customers` — 404, not linked. Alternative hub for case studies.
- `/team` index — 404. 36 individual `/team/*` pages orphaned.
- `/podcast-episodes` — 404. 50 episode pages under `/articles/beyond-the-donation-episode-*`.
- `/solutions/[sub-vertical]` — `/solutions/education`, `/solutions/faith-based`, `/solutions/human-services`, `/solutions/arts-culture`, `/solutions/healthcare` all 404. Sub-vertical SEO opportunity.
- `/solution/grants`, `/solution/events-and-fundraisers`, `/solution/recurring-giving`, `/solution/program-management` — 404. These are referenced in the solutions-overview but don't exist.

### 5. Robots.txt AI bot blocking
Confirmed blocks GPTBot, ClaudeBot, Google-Extended, CCBot, Applebot-Extended, Amazonbot, Bytespider, meta-externalagent. Competitors block none. This is Cloudflare's Managed Content Signal default, not a conscious choice.

### 6. llms.txt RTF encoding
File returns 200 but body is RTF-wrapped. No AI parser can read it.

### 7. Hero image dimensions
Confirmed: `width="Auto" height="Auto"` on homepage hero. 68 of 69 images on homepage lack valid dimensions. Sitewide CLS risk.

## Lessons for future audits

1. **Auditor agents can hallucinate URL patterns.** Future audits must ground URL claims in the live sitemap + actual footer/nav HTML.
2. **Schema presence ≠ schema validity.** Future audits must validate JSON parse, not just regex-match `"@type"`.
3. **Visible content ≠ schema markup.** Clarify this distinction in audit reports — Rob correctly flagged that the pricing page has visible FAQ but what was missing is the schema.
