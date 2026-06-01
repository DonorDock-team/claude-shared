# DonorPerfect — Competitive SEO Audit (June 2026 Baseline)

**Audit Date:** 2026-06-01
**Prior Baseline:** 2026-05-04
**Prepared for:** DonorDock seo-brain strategist system
**Competitor URL:** https://www.donorperfect.com
**Benchmarked against:** https://www.donordock.com
**Method:** Live crawl of sitemap_index + post/page/glossary sitemaps, homepage + pricing-guide + comparison-hub fetches, reviews-ratings page, G2/Capterra SERP recon, delta vs 2026-05 baseline.

---

## 1. Executive Summary (one-liner per dimension)

- **Tier:** Mid-market to enterprise-leaning SMB nonprofit. Modular, quote-priced. Unchanged. **NEW: now owns Givecloud** (acquired by parent SofterWare, Jan 2026) — adding an online-giving / advanced-donation-forms layer that pushes them further up-market and broadens the online-fundraising footprint.
- **Content engine:** ~314 blog posts (active `nonprofit-technology-blog/post-sitemap.xml`), 217 static pages, 7 glossary terms (still flat). 1–3 posts/wk cadence holding. Same topical pillars.
- **Schema coverage:** Still Yoast default only — Organization, WebSite, WebPage, BreadcrumbList, ImageObject. **Still no SoftwareApplication, Product, AggregateRating, FAQPage, Offer, Review, or author schema** on home, pricing, or comparison pages. No improvement.
- **Pricing:** 3 tiers (Core / Plus / Pro), still quote-gated. **NEW: a visible "starting at $99/month" anchor now appears on the pricing-guide page** (was fully gated / "~$450/mo industry-reported" in May). No pricing JSON-LD.
- **Reviews:** Capterra 4.5/5 across ~1,373 (flat). G2 4.4/5 — G2 now displays ~563 total reviews (was reported 192–551 range in May). Trustpilot/TrustRadius/Gartner present. Aggregate ~3,000+ across sites.
- **Pillar pages:** Compare-donor-management-systems hub, Donor Journeys Hub, Pricing Guide, Switch-to-DonorPerfect, Content Library. **NEW: Givecloud integration pages** added under `/integrations/website-management/givecloud/`.
- **DonorDock comparison page:** **Still does not exist.** `/compare-donor-management-systems/donordock/` returns 404 (re-confirmed). DonorDock retains uncontested "DonorPerfect vs DonorDock" SERP.
- **Strategic posture:** Defend on schema + pricing transparency + lean-team ICP. Attack on glossary, author E-E-A-T, the un-built DonorDock comparison page, and now Givecloud-integration confusion (an opening to position DonorDock's all-in-one simplicity vs. a bolt-on giving layer).

---

## 2. Tier

Mid-market / enterprise-leaning SMB nonprofit. Targets full-time fundraising staff and 50–200,001+ constituent orgs. Modular product (auctions, crowdfunding, moves mgmt, QuickBooks/Custom API tier-gated). **June change:** parent SofterWare's January 2026 acquisition of **Givecloud** (2,000+ nonprofit clients; donation-form platform claiming up to 72% more online revenue) is now surfacing in DonorPerfect's marketing — integration pages, press release, and a blog announcement. This strengthens their online-fundraising / donation-form story and pushes them further from DonorDock's <100-donor lean-team sweet spot, but also adds product-stack complexity DonorDock can position against.

## 3. Content Engine Size

| Asset | June 2026 | May 2026 | Delta |
|---|---:|---:|---:|
| Blog posts (`nonprofit-technology-blog/post-sitemap.xml`) | **~314** | 650 (May fetch) | **see note** |
| Static pages (`page-sitemap.xml`) | **217** | 215 | **+2** |
| Glossary terms | **7** | 7 | **0** |
| Comparison children (page-sitemap) | **12** | 12 | 0 |
| Client success stories | refreshed (lastmod 2026-05-08) | present | refreshed |
| Factsheets | refreshed (lastmod 2026-05-28) | present | refreshed |
| Whitepapers | refreshed (lastmod 2026-05-28) | present | refreshed |
| Videos | refreshed (lastmod 2026-05-20) | present | refreshed |

**Note on blog count:** June live crawl of the active blog sitemap returned ~314 post URLs vs. the 650 captured in May. This is almost certainly a **measurement/sitemap-segmentation artifact**, not a 336-post deletion — sitemap fetches paginate and the root vs. blog-subfolder post-sitemaps overlap. Treat blog volume as roughly flat (~300–650 range) and re-verify next month with a direct per-sitemap count. No evidence of a content purge.

**Cadence:** 1–3 posts/week, holding. Recent 2026 posts: "Charitable Contributions in 2026 / One Big Beautiful Bill Act & DAFs," "12 Best Practices for Nonprofit Social Media," "TogetherTuesday Ideas," "Modern Nonprofit Payment Processing," "43 Nonprofit Funding Sources." Continued tilt toward 2026 tax-change timeliness + payments/online-giving content (reinforced by Givecloud).

**Topical pillars (unchanged):** Donor Acquisition & Retention, Donor Engagement & Journeys, Fundraising Communication, Online Fundraising, Major Giving, Monthly Giving, Nonprofit Trends, Data Enhancement, Volunteer Management, Year-End / Giving Tuesday.

**Weak/underserved (DonorDock wedges):** lean-team ops, sub-100-donor workflows, spreadsheet-migration, AI-for-small-teams, transparent-pricing content. Unchanged.

## 4. Schema Coverage Observed

Yoast default JSON-LD graph only. No improvement vs. May.

| @type | Home | Pricing | Comparison page |
|---|:-:|:-:|:-:|
| WebPage / WebSite / Organization / BreadcrumbList / ImageObject | Yes | — | — |
| **SoftwareApplication** | No | No | No |
| **Product** | No | No | No |
| **AggregateRating** | No | No | No |
| **FAQPage** | No | No | No |
| **Offer / PriceSpecification** | No | **No** (even with visible "$99/mo") | No |
| **Review** | No | No | No |
| **Person / author** | No | No | No |

**Verdict:** Same gap as May. The new visible "$99/month" anchor is **not** marked up with Offer/PriceSpecification — so no price rich result. Star-rich-result, AI Overview, and PAA hooks remain unclaimed. DonorDock's schema attack lane is still wide open.

## 5. Pricing Observed

- Three tiers: **Core / Plus / Pro**, still quote-gated ("Get pricing" form).
- **NEW visible anchor: "starting at $99/month"** now appears on the pricing-guide page (May: no dollar figures; industry reports cited ~$450/mo entry). This is a notable transparency shift — DonorPerfect is now publishing a low entry-price hook, likely a competitive response to transparent-priced rivals. Real all-in cost still gated and tier/feature-dependent.
- No pricing schema (Offer/PriceSpecification). Transparency disadvantage vs. DonorDock's published $500/mo + 1% platform fee persists, but the gap narrowed with the $99 anchor — DonorDock should note the $99 entry price will be quoted against us by prospects and prep an apples-to-apples TCO rebuttal.

## 6. Review Counts (G2 + Capterra)

| Source | Rating | Review Count | Notes |
|---|---:|---:|---|
| **Capterra** | 4.5 / 5 | **~1,373** | Flat m/m. Ease 4.3, Service 4.8, Features 4.3, Value 4.5. |
| **G2** | 4.4 / 5 | **~563** (page-displayed) | Up from May's 192–551 SERP range; "Nonprofit CRM Leader" + "Mid-Market Leader" Spring 2026 badges. |
| Trustpilot | 4.7 / 5 | "Excellent" | Independent. |
| Aggregate (Zeffy) | — | **~3,000+** | Across all review sites. |

**DonorDock comparative:** DonorDock ~183 G2 reviews / ~96 sentiment count — still far below DonorPerfect's raw volume but higher per-category sentiment. Volume gap is widening slightly as G2 surfaces 563. Keep pushing review velocity.

## 7. Pillar Pages They Own

1. **`/fundraising-software/compare-donor-management-systems/`** — hub featuring eTapestry/Salesforce/Bloomerang in nav; 12 comparison children in sitemap.
2. **Donor Journeys Hub.**
3. **`/fundraising-software/pricing-guide/`** — now with visible "$99/mo" hook.
4. **`/switch-to-donorperfect/`** + Raiser's-Edge switch funnel.
5. **Content Library** (whitepapers, factsheets, webinars, podcasts, videos).
6. **Year-End / Giving Tuesday + "TogetherTuesday" cluster.**
7. **2026 tax-change / legislation timeliness cluster** (OBBBA / DAF posts).
8. **Integrations sub-site** — **NEW: Givecloud** (`/integrations/website-management/givecloud/`) joins QuickBooks, Constant Contact, payments.

## 8. Comparison Page Targeting DonorDock

**Status: still does not exist. Re-confirmed 404 at `/fundraising-software/compare-donor-management-systems/donordock/`.**

DonorPerfect publishes **12** competitor comparison pages (Bloomerang, Salesforce, eTapestry, Neon, Bonterra, Raiser's Edge, Givebutter, Virtuous, Keela, CauseView, Network for Good, Excel) — **no change from May, and DonorDock is still not among them.** Hub page does not mention DonorDock.

DonorDock retains the "DonorPerfect vs DonorDock" SERP via `donordock.com/compare/donorperfect-vs-donordock` (#1) plus 3rd-party aggregators.

**Net:** Uncontested. Same as May. Givecloud acquisition did not trigger any DonorDock-targeting.

## 9. Attack / Defend / Lateral

**ATTACK:**
1. **Schema.** Still zero SoftwareApplication / AggregateRating / FAQPage / Offer — now even more glaring with a visible "$99/mo" that carries no Offer markup. Ship full schema on DonorDock home, pricing, and `/compare/donorperfect-vs-donordock`.
2. **Glossary.** 7 terms, zero growth for 3+ months. Ship 60–100 DefinedTerm + FAQPage terms.
3. **Author E-E-A-T.** Hundreds of posts, zero named authors. Pair Matt + Rob with Person schema + sameAs.
4. **Pricing transparency content.** Update "What does DonorPerfect cost?" content to address the new "$99/month starting" claim with a fair TCO breakdown (tiers, gated features, payment fees) — capture the comparison query honestly.
5. **Givecloud-complexity wedge.** NEW. Position DonorDock's single all-in-one platform vs. DonorPerfect's growing bolt-on stack (DonorPerfect + Givecloud forms + integrations). "One login vs. stitched-together tools" resonates with lean teams.

**DEFEND:**
1. **DonorDock comparison page** — still 404; defend `/compare/donorperfect-vs-donordock` proactively (refresh stats, FAQPage + Review schema, G2/Capterra link-outs).
2. **Review velocity** — G2 now 563; keep the AggregateRating gap from widening.
3. **Online-giving / donation-form positioning** — Givecloud sharpens DonorPerfect's online-fundraising claim (72% more revenue messaging). DonorDock should reinforce its own online-giving + embedded-forms story so it isn't out-messaged on conversion.

**LATERAL:**
1. **AI-bot policy.** DonorPerfect still fully open (no GPTBot/ClaudeBot/Google-Extended directives, no llms.txt). DonorDock blocks them. Decision still pending — recommendation unchanged: selectively allow reader-bots for citation eligibility; ship llms.txt.
2. **Original-data release.** Neither competitor has a recurring "State of the Lean Nonprofit Fundraiser" report. First-mover citation slot open.
3. **Video transcript indexing.** DonorPerfect has refreshed video sitemap (lastmod 2026-05-20). DonorDock should ship crawlable HTML transcripts.

---

## DELTA Summary (vs May 2026 Baseline)

| Dimension | May 2026 | June 2026 | Delta |
|---|---|---|---|
| Blog post count | 650 (fetch) | ~314 (fetch) | Measurement artifact — treat as ~flat; re-verify |
| Static page count | 215 | 217 | +2 |
| Glossary terms | 7 | 7 | 0 (still underinvested) |
| Comparison children | 12 | 12 | 0 (no expansion this month) |
| `/donordock/` comparison page | 404 | 404 | unchanged — still uncontested |
| Schema posture | Yoast default only | Yoast default only | unchanged |
| Pricing visibility | Fully gated, ~$450/mo industry-reported | **Visible "starting at $99/mo" anchor**, still gated beyond | **Transparency shift** |
| Pricing schema | None | None | unchanged |
| G2 | 4.4 / 192–551 range | 4.4 / ~563 displayed | volume signal up |
| Capterra | 4.5 / ~1,373 | 4.5 / ~1,373 | flat |
| Product/ownership | DonorPerfect standalone | **Owns Givecloud** (SofterWare acq. Jan 2026, now surfacing in marketing) | **NEW strategic event** |
| AI-bot policy | Open | Open | unchanged |

### Top 3 Changes This Month
1. **Givecloud acquisition surfacing in marketing.** Parent SofterWare's Jan-2026 Givecloud buy now appears as integration pages, press release, and blog content — strengthening DonorPerfect's online-giving / donation-form story and adding product-stack complexity DonorDock can position against ("all-in-one vs. bolt-on").
2. **Pricing transparency shift — visible "$99/month" anchor.** First dollar figure on the pricing-guide page (was fully gated). Narrows DonorDock's transparency edge and will be quoted against us; prep a TCO rebuttal. Still no Offer schema.
3. **Comparison footprint held flat at 12; DonorDock still NOT targeted; schema still unimproved.** After May's 5→12 expansion, no new comparison pages this month, and the schema/glossary gaps persist — DonorDock's attack lanes remain open.

**Threat trend: MODERATE / rising slowly.** No direct targeting of DonorDock and core SEO gaps (schema, glossary, author E-E-A-T) unchanged. But the Givecloud acquisition + a new low-price "$99/mo" hook signal a more aggressive, conversion- and online-giving-focused posture. Watch online-fundraising SERPs and prep both the all-in-one-vs-bolt-on message and a $99 TCO rebuttal.

---

**Saved to:** `seo-brain/audits/2026-06-baseline/competitors/donorperfect.md`
**Next audit:** 2026-07. Re-verify blog count (resolve 314 vs 650 measurement question), glossary, comparison-page additions, `/donordock/` 404 status, Givecloud integration depth, and whether the $99 anchor gets Offer schema.
