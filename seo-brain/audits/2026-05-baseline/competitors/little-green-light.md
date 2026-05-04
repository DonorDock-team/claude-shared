# Competitor SEO Audit — Little Green Light (LGL)

**Updated:** 2026-05-04
**Source:** Live crawl of littlegreenlight.com (sitemap_index.xml, post-sitemap.xml, page-sitemap.xml, robots.txt, llms.txt, /pricing/, /why-lgl/, /blog/) + WebSearch of G2 / Capterra / TrustRadius / third-party comparison pages.
**Analyst:** seo-brain monthly baseline
**Competitor URL:** https://www.littlegreenlight.com
**Compared against:** /tmp/dd-citations-runner/seo-brain/audits/2026-04-baseline/competitors/little-green-light.md

---

## 1. Tier
**SMB nonprofit.** Same as April. US-only (geo-blocks EU/UK/CH). Targets small-to-mid nonprofits under $2M budget, 1–5 staff. ICP overlap with DonorDock remains ~90%.

## 2. Content Engine
- **Post sitemap:** ~500+ blog posts (steady from April's 502). Lastmod on /blog/ index = **2026-04-27**, but most individual post URLs still show a 2022-03-28 lastmod (Yoast quirk — content updated, sitemap stale).
- **Page sitemap:** **182 entries** (up from **136** in April → **+46 pages, +34%**). Material expansion of static surface in 30 days.
- **Cadence:** Still ~1 post every 7–10 days. Latest 5: "Using LGL Email Builder…" (Apr 30), "Financial documents for grant apps" (Apr 22), "Mail and Email options" (Apr 16), "Event follow-up strategy" (Apr 9), "Matching gifts" (Mar 26).
- **Topical pillars (unchanged):** practitioner fundraising how-tos — appeals, retention, GivingTuesday, year-end, matching gifts, pledges, grants, segmented appeals, in-kind. Editorial tone, not commercial.
- **DELTA:** Page count growth (+34%) is the biggest signal this month — investigate which 46 pages were added (likely vertical, webinar, or guide expansion).

## 3. Schema Coverage
- **Sitemap generator:** Yoast SEO (still v27.4 referenced in llms.txt). Index sitemap valid; **tag sitemap stale (2022-03-28 lastmod)** — minor housekeeping smell.
- **Homepage JSON-LD (April baseline, unchanged):** WebPage, WebSite (with SearchAction), Organization (with sameAs), ImageObject, BreadcrumbList. Article schema on blog posts (Yoast default).
- **Still missing:** SoftwareApplication, Product, AggregateRating, FAQPage, foundingDate.
- **DELTA:** **No schema improvements detected.** LGL has not added Product/SoftwareApplication/FAQ/AggregateRating in 30 days. The AEO/GEO opening DonorDock identified in April remains wide open.

## 4. Pricing
**Visible, ungated, and unchanged:**
| Constituents | $/mo |
|---|---|
| up to 2,500 | $45 |
| up to 5,000 | $60 |
| up to 10,000 | $75 |
| up to 20,000 | $90 |
| up to 30,000 | $105 |
| up to 40,000 | $120 |
| up to 50,000 | $135 |
| 50k–200k | +$15/10k tier |

- 30-day free trial, no card. No contracts, no setup, no cancellation fee, **unlimited users** at every tier.
- Online donation processing: **0% to LGL**, processor fees only (Stripe/PayPal, "starting at 2.2% + $0.30").
- Prepay discounts: 10% annual / 5% 6-mo / 2.5% 3-mo.
- **DELTA:** No pricing change. Still the sharpest weapon in their SEO arsenal — owns the "affordable donor management" cluster.

## 5. Review Counts (G2 + Capterra)
| Platform | April baseline (implied) | May actual | Delta |
|---|---|---|---|
| **G2** (rating / count) | not measured | **4.2 stars / 37 reviews** (62-review aggregate across LGL "products" page) | new data |
| **Capterra** | not measured | **4.7–4.8 stars / 316 reviews** (308 positive, 6 neutral, 2 negative) | new data |
| Cross-platform aggregate | — | **~413+ reviews / ~93% satisfaction** (G2/Capterra/GetApp/SWA) | new data |

- LGL Capterra category scores: Ease 4.6, Support 4.7, Features 4.5, Value **4.9**.
- **DELTA:** First time we've captured these. Capterra is LGL's strongest review surface (316 reviews vs. G2's 37). Value-for-money score (4.9) is their public-facing moat — DonorDock should expect this to be cited in third-party comparisons and AI answers.

## 6. Pillar Pages LGL Owns
1. **/pricing/** — transparent calculator, owns "donor management software pricing"
2. **Six vertical pages:** /animal-care/, /human-services/, /arts/, /land-trusts/, /schools/, /libraries/
3. **/online-donations/** — fee transparency play
4. **/why-lgl/** — anti-spreadsheet + uptime + bank-level security claims
5. **/reviews/** — testimonial wall
6. **/migrate-to-lgl/** — switcher capture
7. **/consultants-network/** — backlink farm via partner ecosystem
8. **Webinar archive** (~20+ /webinar-slug/ landing pages)
9. **Ebook gates** (10+ PDF lead-magnets)
10. **Blog category hubs** (Tips, Fundraising Strategy, Product, Features, News)
- **DELTA:** Pillar set unchanged. The +46 new pages added in May are most likely additional webinars/guides/verticals — worth a follow-up crawl to confirm which clusters they're reinforcing.

## 7. Comparison Page Targeting DonorDock?
- **No.** Page-sitemap search confirms only **one** competitor alternative URL: **/kindful-alternative/**. Still no donordock-alternative, bloomerang-alternative, donorperfect-alternative, neon-alternative, salesforce-alternative, etapestry-alternative, raisers-edge-alternative, network-for-good-alternative, bonterra-alternative, givebutter-alternative, classy-alternative.
- DonorDock continues to publish 10 comparison pages including a live **/compare/little-green-light-vs-donordock**.
- Third-party comparison surface (TrustRadius, Zeffy, G2, SoftwareAdvice) is active and ranks for "DonorDock vs Little Green Light" — DonorDock's owned page is in good company there.
- **DELTA:** **None.** LGL still has not built a single defensive comparison page in 30 days. DonorDock's 10-to-1 comparison-SEO advantage holds.

## 8. Attack / Defend / Lateral

**ATTACK (where DD presses):**
- **Schema gap is widening in our favor.** LGL hasn't moved on SoftwareApplication / Product / AggregateRating / FAQPage. Ship these on DD homepage, /pricing, /compare/* and /crm pillar this month to capture rich-result + AI-citation real estate while LGL coasts.
- **AI-search / GEO surface remains LGL's blind spot.** Cloudflare AI-bot blocks (ClaudeBot, CCBot, Google-Extended, Amazonbot) still in place in April baseline; nothing in May suggests a reversal. Their llms.txt is still Yoast-auto-generated and thin.
- **Comparison moat.** Defend the 10 vs-pages with FAQPage schema + above-fold tables + refreshed pricing. Add the three lateral pages flagged in April (Kindful-post-sunset, Keela, Virtuous).
- **Modern/AI/easy keyword cluster.** LGL's content cadence is still 100% practitioner how-to — zero AI/automation/Otto vocabulary. Wide open.

**DEFEND (where LGL presses DD):**
- **Capterra 316 reviews + 4.9 value score.** This will surface in AI answers and "best donor CRM under $X" lists. DD must keep growing reviewer count + maintain visible pricing context on every comparison surface so $45 vs $98+ never appears without our TCO framing.
- **15-year tenure + consultant ecosystem.** LGL's affiliate/consultant backlink profile keeps compounding. Don't try to out-link them on head-term "donor management software" — flank instead.
- **Page-count expansion (+34% in 30 days).** Real signal. They're investing somewhere. Watch which clusters get reinforced — if it's vertical pages, DD's vertical-page sprint becomes more urgent.

**LATERAL (where DD goes around them):**
- Vertical pages LGL doesn't have: churches/faith-based, healthcare nonprofits, advocacy, environmental, food banks.
- Size-based pages: "donor CRM for nonprofits under $500k budget," "for solo development director," "under 100 members."
- "Leaving Little Green Light" migration hub (recommended in April — ship it).
- Mobile / text-to-give / SMS outreach SEO surface — LGL barely mentions mobile.
- "Is LGL worth it?" / "problems with LGL" mid-funnel doubt queries.

---

## DELTAS at a Glance (April → May)

| Signal | April | May | Direction |
|---|---|---|---|
| Blog posts | 502 | ~500+ (steady) | flat |
| Static pages | 136 | **182** | **+34%** ⬆ |
| Schema gaps | 4 critical missing | 4 critical missing | flat (DD opportunity preserved) |
| Pricing | $45–$135/mo | $45–$135/mo | flat |
| AI-bot blocks | ClaudeBot/CCBot/G-Ext/Amazon | (assumed unchanged) | flat |
| Comparison pages targeting DD | 0 | 0 | flat |
| Total comparison pages | 1 (Kindful) | 1 (Kindful) | flat |
| llms.txt | Yoast-auto, 30 lines | Yoast-auto, same | flat |
| G2 reviews | not captured | 37 reviews / 4.2★ | new |
| Capterra reviews | not captured | 316 reviews / 4.7–4.8★ | new |

**Headline:** LGL added meaningful page surface in 30 days (+46 pages) but did not close any of the schema, comparison, or AI-search gaps DonorDock identified in April. The opening to win GEO/AEO citations and comparison intent is **still wide open** — and the clock is the only thing closing it.

---

## Sources
- [LGL sitemap_index.xml](https://www.littlegreenlight.com/sitemap_index.xml)
- [LGL post-sitemap.xml](https://www.littlegreenlight.com/post-sitemap.xml)
- [LGL page-sitemap.xml](https://www.littlegreenlight.com/page-sitemap.xml)
- [LGL robots.txt](https://www.littlegreenlight.com/robots.txt)
- [LGL llms.txt](https://www.littlegreenlight.com/llms.txt)
- [LGL pricing](https://www.littlegreenlight.com/pricing/)
- [LGL why-lgl](https://www.littlegreenlight.com/why-lgl/)
- [LGL blog](https://www.littlegreenlight.com/blog/)
- [G2 — Little Green Light reviews](https://www.g2.com/products/little-green-light/reviews)
- [Capterra — Little Green Light reviews](https://www.capterra.com/p/123954/Little-Green-Light/reviews/)
- [TrustRadius — DonorDock vs LGL](https://www.trustradius.com/compare-products/donordock-vs-little-green-light)
- [DonorDock comparison page](https://www.donordock.com/compare/little-green-light-vs-donordock)
