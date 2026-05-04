# DonorPerfect — Competitive SEO Audit (May 2026 Baseline)

**Audit Date:** 2026-05-04
**Prepared for:** DonorDock seo-brain strategist system
**Competitor URL:** https://www.donorperfect.com
**Benchmarked against:** https://www.donordock.com
**Method:** Live crawl of robots.txt + sitemap indexes, homepage + pricing + comparison hub fetches, G2/Capterra SERP recon, delta vs 2026-04 baseline.

---

## 1. Executive Summary (one-liner per dimension)

- **Tier:** Mid-market to enterprise-leaning SMB nonprofit. 0–500 up to 200,001+ constituents. Modular, quote-priced. Same as April.
- **Content engine:** ~650 blog posts (was 648), 215 static pages, 7 glossary terms (unchanged), 1–3 posts/wk cadence holding. Topical pillars are Donor Acquisition & Retention, Donor Engagement, Online Fundraising, Major Giving, Monthly Giving, Year-End / Giving Tuesday, Nonprofit Trends, Volunteer Mgmt.
- **Schema coverage:** Yoast default only — Organization, WebSite, WebPage, BreadcrumbList, ImageObject. **Still no SoftwareApplication, Product, AggregateRating, FAQPage, Review, or Person/author schema** on home, pricing, or comparison pages.
- **Pricing:** 3 tiers (Core / Plus / Pro). **Fully gated — quote-only.** Starts ~$450/mo per industry reporting. No pricing JSON-LD.
- **Reviews:** Capterra 4.5/5 across ~1,373 reviews. G2 4.4/5 (count varies 192–551 depending on source/page; SERP-reported). Trustpilot 4.7/5. Aggregate ~3,000+ reviews across review sites per Zeffy.
- **Pillar pages:** "Compare donor management systems" hub (Bloomerang/Salesforce/Etapestry featured + 9 more in sitemap), "Donor Journeys Hub", Pricing Guide, Switch-to-DonorPerfect, Whitepaper library.
- **DonorDock comparison page:** **Still does not exist.** `/compare-donor-management-systems/donordock/` returns 404. DonorDock retains uncontested SERP ownership for "DonorPerfect vs DonorDock".
- **Strategic posture:** Defend on schema + pricing transparency + lean-team ICP. Attack on glossary, author E-E-A-T, and the un-built DonorDock comparison page.

---

## 2. Tier

Mid-market / enterprise-leaning SMB nonprofit. Targets full-time fundraising staff and 50–200,001+ constituent orgs. 75,000 professionals, 11,000 orgs claimed. Modular product (auctions, crowdfunding, moves mgmt, QuickBooks tier-gated, Custom API in Pro tier only). Overbuilt for DonorDock's <100-donor lean-team sweet spot.

## 3. Content Engine Size

| Asset | May 2026 | April 2026 | Delta |
|---|---:|---:|---:|
| Blog posts (`nonprofit-technology-blog/post-sitemap.xml`) | **650** | 648 | **+2** |
| Static pages (`page-sitemap.xml`) | **215** | 157 | **+58** |
| Root post-sitemap | 14 | n/a | new visibility |
| Glossary terms | **7** | 7 | **0** |
| Client success stories | present (lastmod 2026-04-24) | present | refreshed |
| Whitepapers | present (lastmod 2026-04-21) | present | refreshed |
| Videos | present (lastmod 2026-04-15) | present | refreshed |

**Cadence:** 1–3 posts/week, holding. Recent April 2026 posts: "10 Ways to Increase Donation Form Traffic" (4/28), "How to Set Donation Ask Amounts Using Data" (4/24), "Digital Wallets for Nonprofits" (4/13), "Donor-Advised Funds Amid the 2026 Tax Changes" (4/10), "5 Donor Segments for 2026 Tax Changes" (4/9).

**Topical pillars (from blog landing nav):**
1. Donor Acquisition & Retention
2. Donor Engagement & Journeys
3. Fundraising Communication
4. Online Fundraising
5. Major Donors / Major Giving
6. Monthly Giving
7. Nonprofit Trends
8. Data Enhancement
9. Volunteer Management
10. Year End Giving & Giving Tuesday

**Strong:** monthly giving, major donor cultivation, EOY/Giving Tuesday, tax-change timeliness. **Weak/underserved (DonorDock wedges):** lean-team ops, sub-100-donor workflows, spreadsheet-migration, AI-for-small-teams, transparent-pricing content.

## 4. Schema Coverage Observed

Only Yoast default JSON-LD graph on homepage:

| @type | Home | Pricing | Comparison page (Bloomerang) |
|---|:-:|:-:|:-:|
| WebPage | Yes | — | — |
| WebSite | Yes | — | — |
| Organization | Yes | — | — |
| BreadcrumbList | Yes | — | — |
| ImageObject | Yes (x2) | — | — |
| **SoftwareApplication** | No | No | No |
| **Product** | No | No | No |
| **AggregateRating** | No | No | No |
| **FAQPage** | No | No | No |
| **Offer / PriceSpecification** | No | **No** (despite being the pricing page) | No |
| **Review** | No | No | No |
| **Person / author** | No | No | No |
| **ComparisonTable / itemReviewed** | n/a | n/a | **No** |

**Verdict:** Same gap as April. Comparison and pricing pages are entirely unmarked. Star-rich-result, AI Overview, and PAA hooks remain unclaimed by DonorPerfect.

## 5. Pricing Observed

- Three tiers: **Core**, **Plus** (Most Popular), **Pro**.
- **Visibility: gated.** Page prompts "GET YOUR CUSTOM QUOTE" + form (org name, constituent count, role).
- No dollar amounts on the pricing page. Industry reporting / Capterra: ~$450/mo entry.
- Tier-gated features include QuickBooks (Plus+), Moves Management (Plus+), Custom API (Pro only), Scheduled Reports tiering.
- **No pricing schema (Offer/PriceSpecification).** Permanent transparency disadvantage vs DonorDock's published $500/mo + 1% platform fee.

## 6. Review Counts (G2 + Capterra)

| Source | Rating | Review Count | Notes |
|---|---:|---:|---|
| **Capterra** | 4.5 / 5 | **~1,373** | 94% rated 4+ stars. Ease 4.3, Service 4.8, Features 4.3, Value 4.5. |
| **G2** | 4.4 / 5 | **192–551** (SERP-reported, scrape blocked w/403) | Range reflects different cached pages; treat as ~300–500. |
| Trustpilot | 4.7 / 5 | "Excellent" | Independent. |
| Aggregate (Zeffy) | — | **~3,000+** | Across all review sites combined. |

**DonorDock comparative:** ~183 G2 reviews / 96 sentiment vs DonorPerfect's larger volume but lower per-category satisfaction. DonorDock wins on per-review sentiment; DonorPerfect wins on raw volume signal to AI engines.

## 7. Pillar Pages They Own (SEO-strong topical hubs)

1. **`/fundraising-software/compare-donor-management-systems/`** — competitor hub featuring Etapestry/Salesforce/Bloomerang in the visible nav, with 12+ comparison children in sitemap (bloomerang, salesforce, etapestry, neon, bonterra, raisers-edge, givebutter, virtuous, keela, causeview, network-for-good, excel).
2. **Donor Journeys Hub** — engagement/retention pillar.
3. **`/fundraising-software/pricing-guide/`** — gated quote funnel; ranks for "donorperfect pricing".
4. **`/switch-to-donorperfect/`** + `/landing/utm/switch-and-save-raisersedge/` — competitor migration funnels.
5. **Content Library** (whitepapers, factsheets, webinars, podcasts) — distinct sitemap segments per content type.
6. **Year-End / Giving Tuesday cluster** — 31+ branded posts on Giving Tuesday alone.
7. **Tax-change / legislation timeliness cluster** — 2026 Tax Changes posts already published (3+ in April).
8. **Integrations sub-site** (`integrations/`) with its own sitemap index — QuickBooks, Constant Contact, payments.

## 8. Comparison Page Targeting DonorDock

**Status: does not exist. Confirmed 404 at `/fundraising-software/compare-donor-management-systems/donordock/`.**

DonorPerfect publishes 12 competitor comparison pages in sitemap but **DonorDock is not among them**. The comparison hub page does not mention DonorDock anywhere.

DonorDock retains the SERP for "DonorPerfect vs DonorDock":
1. donordock.com/compare/donorperfect-vs-donordock (#1, owned)
2. getapp.com, softwareadvice.com, zeffy.com, g2.com, capterra.com (3rd-party aggregators)

**Net:** DonorPerfect still leaves this position uncontested. Same as April.

## 9. Attack / Defend / Lateral

**ATTACK (where to press DonorPerfect):**
1. **Schema.** Ship SoftwareApplication + AggregateRating + FAQPage + Offer on homepage, pricing, and `/compare/donorperfect-vs-donordock`. DonorPerfect's pricing page has no Offer schema; comparison pages have no Product/itemReviewed. Star-rich SERPs and AI Overview hooks are free real estate.
2. **Glossary.** They have **7 terms** (zero growth m/m). Ship 60–100 terms with DefinedTerm + FAQPage schema in 90 days to dominate informational intent.
3. **Author E-E-A-T.** 650 blog posts, **zero named authors**. Pair Matt + Rob with Person schema + LinkedIn sameAs across evergreen content. Defensible moat.
4. **DonorPerfect pricing transparency content.** Publish a fair, factual "What does DonorPerfect cost?" article. Their pricing page returns no schema and gates dollar figures — a transparent ranking competitor wins this query.
5. **Lean-team / Excel-upgrade pillar.** DonorPerfect has near-zero coverage at <100 donors. 12-article pillar wins long-tail uncontested.

**DEFEND (where DonorPerfect could attack but currently isn't):**
1. **DonorDock comparison page** — still 404. Defend `/compare/donorperfect-vs-donordock` proactively: refresh stats, add FAQPage + Review schema, add Capterra/G2 link-outs, add video testimonial.
2. **G2/Capterra review velocity** — DonorPerfect has 10–20× more raw review count. Push customer review program to keep the AggregateRating gap from widening as AI engines weight volume.
3. **Tax-changes / 2026 legislation content** — DonorPerfect is fast on this. DonorDock should ship 2–3 lean-nonprofit-specific 2026 tax posts to defend the seasonal cluster.

**LATERAL (parallel, non-zero-sum moves):**
1. **AI-bot policy.** DonorPerfect remains fully open (no GPTBot/ClaudeBot/Google-Extended directives, no llms.txt). DonorDock blocks them all. **Decision still pending from April.** Recommendation unchanged: selectively allow reader-bots (ChatGPT-User, ClaudeBot, PerplexityBot, Google-Extended, Applebot-Extended) for citation eligibility; keep training-only crawlers blocked; ship llms.txt.
2. **Original-data release.** Neither competitor has shipped a recurring "State of the Lean Nonprofit Fundraiser" report. First-mover citation slot in AI answers still available.
3. **Video transcript indexing.** DonorPerfect has some `/video/{name}/transcript/` pages; DonorDock has Remotion capability but no transcript-indexed strategy. Ship transcripts as crawlable HTML.

---

## 10. DELTAS vs April 2026 Baseline

| Dimension | April 2026 | May 2026 | Delta |
|---|---|---|---|
| Blog post count | 648 | **650** | +2 (slow week) |
| Static page count | 157 | **215** | **+58** (likely sitemap re-segmentation, not 58 new pages — verify next month) |
| Glossary terms | 7 | 7 | 0 (still underinvested) |
| Comparison children (sitemap) | 5 confirmed (Keela/Bloomerang/Raiser's Edge/Salesforce + Kindful unverified) | **12 confirmed** (added Etapestry, Neon, Bonterra, Givebutter, Virtuous, Causeview, Network-for-Good, Excel) | **+7 — DonorPerfect expanded their comparison footprint significantly.** Notable: **Givebutter and Virtuous added** — both DonorDock-adjacent ICP overlap. |
| `/donordock/` comparison page | Does not exist | **Still does not exist (404 confirmed)** | unchanged — stay vigilant |
| robots.txt AI policy | Open | Open | unchanged |
| Schema posture (home / pricing / comparison) | Yoast default only | Yoast default only | unchanged |
| Pricing transparency | Gated, 3 tiers | Gated, 3 tiers | unchanged |
| G2 rating | not captured | 4.4 / ~300–500 | new datapoint |
| Capterra rating | not captured | 4.5 / ~1,373 | new datapoint |
| Recent blog focus | 2026 tax changes, monthly giving names, QR codes | + form-traffic optimization, ask-amount data | **shift toward conversion-tactic content** (form traffic, ask amounts) |

**Headline delta of the month:** **DonorPerfect added 7 competitor comparison pages, including Givebutter and Virtuous.** This signals an expanding bottom-of-funnel program. Two implications:
1. DonorDock should expect Keela/Givebutter/Virtuous comparison-page SERPs to get harder over the next 90 days.
2. The fact that DonorDock is still **not** on their target list confirms DonorPerfect either (a) doesn't see DonorDock as a meaningful threat yet, or (b) hasn't gotten to us. Either way, the uncontested `/compare/donorperfect-vs-donordock` SERP is still ours to lose.

**Second delta worth watching:** the static page count jumping 157 → 215 is suspiciously large. Most likely a sitemap segmentation change (page-sitemap.xml now includes content types previously segmented elsewhere) rather than 58 net-new pages. Spot-check next month.

---

**Saved to:** `seo-brain/audits/2026-05-baseline/competitors/donorperfect.md`
**Next audit:** 2026-06-04. Re-verify static page count delta, glossary count, comparison-page additions, and `/donordock/` 404 status.
