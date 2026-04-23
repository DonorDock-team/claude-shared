# Fix Verification — 2026-04-22

Re-fetched live pages after Rob reported fixes applied. Results below.

## ✅ Fixes confirmed working

### 1. Duplicate BlogPosting — FIXED
- `/articles/best-nonprofit-crm` now has **1 BlogPosting script** (was 2)
- datePublished: `2026-03-25T17:55:01.187Z` (proper ISO 8601)
- This fix applied at the article template level, so all 467 articles should now have single BlogPosting.

### 2. Tag archive noindex — WORKING
- `/tags/fundraising`: `<meta name="robots" content="noindex,follow">` present
- `/tags/donor-engagement`: same
- `/tags/donor-relationships`: same
- All 88 tag pages should now be excluded from index but keep crawl flow to articles.
- Next step: submit tag URLs to GSC Removals (Temporary Removals) to speed up deindexing. Also exclude /tags/ from sitemap.xml.

### 3. FAQ page — FIXED (both issues)
- `@graph` now FLAT (not nested) — single `@graph` appearance, valid JSON parse
- 114 `<h3>` elements on page (converted from divs, exactly matches 114 Question entities in schema)
- 114 Question entities in the JSON-LD
- Google Rich Results Test should now accept this page cleanly.

## Audit corrections from today's verification

### Meta descriptions — audit was WRONG
Checked 20 top pages directly for `<meta name="description">`:
- Homepage: 134 chars ✓
- /about: 150 chars ✓
- /crm: 158 chars ✓
- /pricing: check separately (scanner didn't find on every sample)
- /compare (hub): 155 chars ✓
- /articles: 125 chars ✓
- /otto: 187 chars (slightly long, will truncate at ~160)
- /donor-outreach: **218 chars** (too long, truncates in SERP)
- /features-overview: **235 chars** (too long)
- /online-giving: 107 chars (short, leaves SERP space)
- /customer-success: 106 chars (short)
- /solutions-overview: 191 chars (slightly long)
- All 20 pages sampled had meta descriptions present

**Real finding:** Meta descriptions exist sitewide but some are over-length (will truncate) or under-length (leaving SERP real estate). Not "missing" as audit claimed.

**Exception:** /compare/donorperfect-vs-donordock and /compare/neon-crm-vs-donordock are MISSING meta descriptions. Likely the other 7 compare pages are too. Compare template may not have a meta description field populated.

### Footer URLs — audit was WRONG
- Footer "Success stories" → `/customer-success` (200 ✓)
- Footer "Solutions" → `/solutions-overview` (200 ✓)
- `/success-stories`, `/solutions`, `/reviews`, `/customers` all 404 BUT NONE are linked from footer. Opportunities to build, not broken links.

## Still outstanding

### Compare pages missing FAQ schema (5 of 9)
After JSON cleanup, 4 compare pages have FAQ schema: etapestry, little-green-light, neon-crm, network-for-good. Missing from:
- bloomerang-vs-donordock
- donorperfect-vs-donordock (REAL schema now provided)
- givebutter-vs-donordock
- salesforce-vs-donordock (no JSON-LD at all)
- bonterra-vs-donordock (no JSON-LD at all)

### Invalid JSON-LD — 6 of 9 compare pages
Even where FAQ schema EXISTS, 6 of 9 have invalid JSON that Google discards. Affected: bloomerang, donorperfect, etapestry, little-green-light, neon-crm, network-for-good. Only givebutter has valid JSON-LD.

Fix via the REAL schemas in this folder for donorperfect and neon-crm; similar clean rewrites needed for the other 4.

### Neon comparison H1 typo
Live verified — still says `<h1>Network for Good vs DonorDock</h1>` on /compare/neon-crm-vs-donordock. Page title is correct ("Neon CRM vs DonorDock") but H1 is wrong. Fix in Webflow Designer by editing the H1 text element.

### Hero image dimensions
Homepage hero still has `width="Auto" height="Auto"`. 68 of 69 images lack valid dimensions.

### Newsletter form DOM position
Only on article template. "Weekly Roundup" appears at position 60414 in HTML; `<h1>` at 58767; `<article>` at 62397. So: H1 → Weekly Roundup → article body. H1 comes first (good), but newsletter block inserts between title and body.

This is a Webflow template section (class `uui-banner15_*`), not a HubSpot popup. Fix by moving the banner below the article content section in the article CMS template.

### llms.txt still RTF-corrupted
Real UTF-8 version ready in `seo-brain/remediation/llms.txt`. Re-upload to replace.

### robots.txt still blocking AI bots
No change detected. Awaiting Rob's Cloudflare decision.
