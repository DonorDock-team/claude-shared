# Fix Verification — Round 2 — 2026-04-22 evening

Re-fetched live pages after Rob published his latest batch of fixes.

## ✅ Confirmed fixed (post-publish)

### Neon compare H1 — FIXED
Live verified: `<h1>Neon CRM vs DonorDock</h1>` on `/compare/neon-crm-vs-donordock`. "Network for Good" no longer appears anywhere in the page body. Typo resolved.

### Newsletter form on article template — FIXED
Checked both `/articles/best-nonprofit-crm` and `/articles/donor-retention`. "Weekly Roundup" no longer appears in the HTML at all on either article (position = -1 = not present). Template move worked. AI crawlers + Google will now see the H1 followed immediately by the article body.

## ✅ Confirmed Round 1 fixes still holding

- **BlogPosting dedupe** — still 1 script per article
- **Tag archive noindex** — still present on /tags/* pages
- **FAQ page flat @graph + H3 accordions** — still valid

## ⚠️ Partial fix: Auto width/height images

Significant progress on most pages. Remaining pages where Auto width or height still appears on at least one image:

| Page | Auto images | Notes |
|---|---|---|
| Homepage | 1 | Hero image still has `width="1508" height="Auto"` — width was fixed, height is still "Auto" |
| Pricing | 0 | Clean ✅ |
| Compare hub | 0 | Clean ✅ |
| Compare/bloomerang-vs-donordock | 0 | Clean ✅ |
| Compare/neon-crm-vs-donordock | 0 | Clean ✅ |
| Compare/donorperfect-vs-donordock | 0 | Clean ✅ |
| Article /articles/best-nonprofit-crm | 2 | Featured image referenced twice, both have `width="Auto" height="Auto"` — likely the CMS "featured image" slot template on the articles page |
| Article /articles/donor-retention | 2 | Same pattern — same CMS featured image slot |
| Solution /solution/donor-stewardship | 3 | Templates, Timeline scroll GIF, Automations Editor images still `width="Auto" height="Auto"` |

**Where to fix:**
- Homepage hero: go to Designer → Homepage → click hero image → change Height field from `Auto` to actual pixel height (check the original WebP intrinsic height, likely ~1000)
- Article featured image: Article CMS template has a featured image element with Auto in both width and height — fix once, applies to 467 articles
- Solution page: the 3 template mockup images inside /solution/donor-stewardship each need explicit dimensions

**Important context on the other image numbers:** Pages show `valid_int=0` but most images have zero width/height attributes. This is Webflow's Responsive Images default — it relies on `srcset` without setting intrinsic `width`/`height`. For CLS prevention, best practice is BOTH width+height (for layout reservation) AND srcset (for responsive scaling). Most images without attributes are small icons/logos where CLS impact is minimal. Priority: hero images, featured images, and large content images.

## ⚠️ My error: "no platform fees"

In the llms.txt and pricing schema I pushed earlier, I wrote "no platform fees" and "no platform fees on donations." **That was my own hallucination** — I conflated the live pricing page's "No long-term contracts. No hidden fees." language with zero platform fees.

**Source of my error:** I wrote those lines from my own assumption without verifying against DonorDock source material. I did NOT pull from any live page or brand doc — I invented it.

**The correct messaging (from DonorDock's own brand docs at Projects/Website/schema-markup-audit-2026-03-25.md + online-giving.md):** DonorDock Online Giving pages include a 1% platform fee, plus standard Stripe/PayPal processing fees (typically 2.2% + $0.30 for nonprofits). Brand rule: always say "1% platform fee," never "free processing" or "no platform fees."

**Files corrected in this commit:**
- seo-brain/remediation/llms.txt (Online Giving line + Key Differentiators + new fee structure section)
- seo-brain/remediation/schemas/pricing-page-REAL.html (Offer description + WebPage description + featureList item)
- seo-brain/remediation/schemas/pricing-page.html (legacy file — now a pointer to the REAL file)

**Audit-reliability note:** This is the same failure mode I flagged in earlier audit corrections — generating content without grounding in verified sources. For Phase 2 strategy docs I will require every factual claim to link to a specific source (live URL, CMS item, or brand doc), per Rob's standards.
