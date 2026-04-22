# Remediation Guide

Direct fix instructions and copy-paste schemas for Phase 1 critical findings. All items verified against live site 2026-04-22.

## Priority order (by impact ÷ effort)

### P0 — Do this week
1. Fix invalid JSON on `/pricing` (copy-paste `schemas/pricing-page.html`)
2. Fix invalid JSON on `/compare/donorperfect-vs-donordock`
3. Fix Neon compare page H1 typo ("Network for Good" → "Neon CRM")
4. Unblock AI bots in Cloudflare (strategic call — see `robots-txt-fix.md`)
5. Re-save `llms.txt` as UTF-8 plain text

### P1 — Do this month
6. Add FAQPage schema to 5 compare pages missing it + 7 feature pages with visible FAQ
7. Fix hero image dimensions (homepage) + batch audit all image elements in Webflow
8. Add meta descriptions sitewide (empty on all pages)
9. Fix duplicate BlogPosting on article template
10. Noindex 88 tag archive pages (simpler than rescuing)
11. Move newsletter form out of DOM-first article position

### P2 — Do this quarter
12. Build missing 4 solution pages (grants, events-and-fundraisers, recurring-giving, program-management)
13. Build sub-vertical solution pages (education, faith-based, human-services, arts-culture, healthcare)
14. Build `/team` index + add 150-word bios to each /team/* page
15. Fix 6 remaining compare pages with invalid JSON (bloomerang, etapestry, little-green-light, network-for-good, neon-crm + add JSON to bonterra, salesforce)

## Files in this folder

- `fix-checklist.md` — step-by-step for every fix
- `schemas/pricing-page.html` — complete pricing JSON-LD (copy-paste into Page Settings → Custom Code → Before `</body>`)
- `schemas/howto-migration-checklist.html` — HowTo schema for `/articles/nonprofit-crm-migration-checklist`
- `schemas/howto-sroi-calculation.html` — HowTo schema for `/articles/how-to-calculate-nonprofit-social-return-on-investment`
- `schemas/howto-crm-selection.html` — FAQPage schema for `/articles/nonprofit-crm-buyers-guide-12-questions-to-ask` (better fit than HowTo given 12 questions)
- `schemas/compare-faqpage-template.html` — reusable FAQPage template for compare pages
- `robots-txt-fix.md` — Cloudflare steps to unblock AI bots
- `meta-description-bulk-draft.md` — proposed meta descriptions for top 20 pages (for Webflow MCP bulk update)
- `webflow-designer-steps.md` — detailed Designer UI steps for non-code fixes
