# Bloomerang Competitor SEO/AEO Audit — June 2026 Baseline

**Competitor:** Bloomerang (https://bloomerang.com — .co continues to 301 to .com)
**Audit date:** 2026-06-01
**Prior baseline:** 2026-05-04

---

## 1. Tier
**Mid-market nonprofit, expanding into SMB and enterprise.** Multi-product "Intelligent Giving Platform" play (CRM + Fundraising + Volunteer + AI "Penny"). Qgiv = "Bloomerang Fundraising," InitLive = "Bloomerang Volunteer." **PE ownership: Warburg Pincus (growth investment, Feb 2024) alongside JMI Equity** — correcting May's "JMI-only" note; both remain on the board. No new M&A this month. **Product motion this month:** Dataro partnership (May 2026) adding predictive donor modeling + AI prospect research inside Bloomerang; "Conversational Reporting" (plain-language report builder) in alpha, GA planned summer 2026. AI/"intelligent platform" is now the dominant positioning theme.

## 2. Content Engine
- **Blog posts:** ~700+ (Yoast split sitemaps consolidated — May's `post-sitemap.xml` / `post-sitemap2.xml` now 404; posts roll into `sitemap.xml`). Estimate down modestly from May's ~893; pruning/consolidation trend continues.
- **Marketing pages:** ~400+ total URLs in consolidated sitemap; marketing/product page tranche roughly flat vs May's 161.
- **Sitemap restructure:** **Bloomerang collapsed its segmented Yoast sitemaps into a single `sitemap.xml` urlset** — the per-type post/page/guide sitemaps that May relied on for exact counts are gone. Exact blog count no longer cleanly derivable; treat ~700+ as the working figure.
- **Pillars:** Nonprofit CRM, donor retention, fundraising tactics (year-end, events, P2P, capital campaigns, major gifts), board governance, volunteer management, grant writing, DAFs, AI/Penny.
- **Frequency:** Steady; AI-themed posts increasing.

## 3. Schema Coverage
- **Homepage:** Schema not cleanly extractable this pass (renderer returned no JSON-LD in fetched HTML — likely JS-injected; treat as inconclusive, was Organization/WebSite/WebPage/Breadcrumb in May). **Still no SoftwareApplication/Product/Offer/AggregateRating observed.**
- **Flagship article (/blog/nonprofit-crm/):** Article, FAQPage, Organization. **FAQPage now carries 7 questions (up from 4 in May)** — Bloomerang is closing the schema-depth gap DonorDock was exploiting. Title now "21 Top Nonprofit CRM Solutions to Manage Supporters in 2026," updated 05/22/2026. Still no HowTo, VideoObject, or Review schema.
- **/alternative/* pages:** Still no FAQPage schema observed — AEO gap on their own comparison pages persists.
- **DonorDock advantage holds** on homepage rich-result types (SoftwareApplication + Offer + AggregateRating), but the flagship FAQ-arbitrage lane narrowed.

## 4. Pricing
**Unchanged from May.** Published starting prices per product:
- Bloomerang Fundraising: starting **$40/mo** (annual) — *now noted "must be purchased as part of bundle with Bloomerang CRM"*
- Bloomerang CRM: starting **$125/mo** (annual)
- Bloomerang Volunteer: starting **$119/mo** (annual)
- Giving Platform bundle: now shows **two tiers — Standard and Pro**, both "Contact Sales for Pricing" (Pro adds unlimited automated outreach + event tools)
- Model: **constituent-based**, "budget won't spike unexpectedly as you grow," unlimited users.
- **No free trial.** CTAs: Contact Sales, Book a Demo, Product Tour.

**DELTA from May:** Prices flat. Two changes: (1) Fundraising now explicitly **bundle-locked to CRM** (can't buy standalone at $40), and (2) bundle split into **Standard/Pro tiers**. Both push buyers toward higher-priced bundles — reinforces DonorDock's flat-rate + standalone-simplicity attack.

## 5. Review Counts (G2 + Capterra)
- **G2 — Giving Platform (combined):** ~1,199 / 4.6 — flat vs May.
- **G2 — CRM only:** ~872 / 4.7 — flat.
- **G2 — Fundraising (Qgiv):** ~235 / 4.5 — flat.
- **G2 — Volunteer:** ~36 / 4.3 (now captured).
- **Capterra:** **1,287 reviews / 4.7 stars** (now a hard count vs May's "several hundred, blocked" estimate). 97% positive sentiment.
- DonorDock context: 4.8/5, ~200+ reviews. Bloomerang volume still ~5–6x.

**DELTA from May:** G2 essentially flat. Capterra now confirmed at 1,287/4.7 (establishes a real baseline). Review moat steady, not accelerating.

## 6. Pillar Pages (SEO-Strong Hubs)
- `/blog/nonprofit-crm/` — flagship, "21 Top Nonprofit CRMs," ~6K words, updated 05/22/2026, FAQPage now 7 Qs.
- `/alternative/` — competitor-comparison hub (15 pages, see §7).
- `/product-tours/`, `/integrations/`, `/ai/` + `/ai/use-cases/` (Penny), `/resources/`, `/webinars-events/`, `/tools/`, `/experience/`.
- Listicle real estate intact: "21 Best Nonprofit CRMs," "Best Nonprofit Software," fundraising-apps, moves management, capital campaigns, DAF, P2P, text-to-give.

## 7. Comparison Page Targeting DonorDock
**STILL NO DonorDock page. All four variants 404 (re-tested this month):**
- `/alternative/donordock/` — 404
- `/compare/donordock/` — 404
- `/donordock-alternative/` — 404
- `/vs/donordock/` — 404

**`/alternative/` hub now lists 15 competitors** (vs "17+" in May — slight consolidation): DonorPerfect, Bonterra Network for Good, Blackbaud Raiser's Edge, Blackbaud eTapestry, Neon One, Bonterra EveryAction, Bonterra Salsa, Little Green Light, Virtuous, Donorbox, Volgistics, Volunteer Impact (Better Impact), Spreadsheets, SignUpGenius, VolunteerHub. **DonorDock not mentioned anywhere on the hub.**

**Implication:** DonorDock's "Bloomerang alternative" / "vs Bloomerang" SERP lane remains **wide open** for a second straight month. Bloomerang is consolidating, not expanding, this program — ship DD's comparison + migration content now while the window holds.

## 8. Attack / Defend / Lateral

**Attack (DonorDock pushes here):**
- **"Bloomerang vs DonorDock" SERP** — still uncontested. Ship now.
- **Migration content** — "Switching from Bloomerang," "Exporting from Bloomerang." They won't write the counter.
- **Bundle/pricing transparency** — Fundraising is now bundle-locked to CRM (no true $40 standalone); bundle is opaque Standard/Pro. Build a "what Bloomerang actually costs at 1K/5K/10K constituents" calculator; flat $500/mo wins above ~1,500 records.
- **Penny/Conversational Reporting vs Otto** — Bloomerang's AI is still alpha/beta and launch-announcement-heavy. DD can claim "AI that ships today" framing.
- **`/alternative/*` FAQPage gap** — their comparison pages still lack FAQ schema; DD can out-AEO equivalent pages.
- **Small/growing-nonprofit niche** — "first real CRM," "graduating from spreadsheets," "under 1,000 donors."

**Defend (Bloomerang genuinely stronger):**
- Decade of domain authority + topical breadth — out-answer, don't out-publish.
- Volunteer-management content depth (dedicated product moat).
- Review volume (~5–6x DD). Keep pumping G2/Capterra + surface in schema.
- E-E-A-T bylined experts; flagship FAQ now deeper (7 Qs) — DD must keep FAQ schema richer than 7 Qs on equivalent pages.
- Integration breadth + new Dataro AI predictive-modeling story.

**Lateral (Bloomerang ignores, easy to claim):**
- Faith-based, rural, arts/culture, advocacy verticals.
- "Nonprofit CRM under $X" budget roundups.
- Platform-fee transparency (1% vs typical 3–5%).
- DIY/spreadsheet first-time-upgrade migration content.
- Founder-led / Fargo / heartland trust (vs Warburg Pincus + JMI PE ownership).
- Podcast/transcript repurposing with VideoObject + Article schema.

---

## DELTA Summary vs May 2026 Baseline

| Item | May 2026 | June 2026 | Direction |
|---|---|---|---|
| PE ownership | JMI Equity | **Warburg Pincus + JMI** (Feb-2024 deal, corrected) | Clarified, not new |
| Recent product | Penny AI (beta) | **+ Dataro partnership, Conversational Reporting (alpha)** | AI push continuing |
| Blog post count | ~893 | **~700+ (sitemaps consolidated; exact count lost)** | DOWN / harder to measure |
| Sitemap structure | Segmented Yoast (post/page/guide) | **Single `sitemap.xml` urlset** | RESTRUCTURED |
| Marketing pages | 161 | ~flat (in 400+ total URLs) | Steady |
| Pricing | $40/$125/$119 starting | **Same; Fundraising now CRM-bundle-locked; bundle split Standard/Pro** | Pushes upsell |
| Free trial | None | None | Unchanged |
| `/alternative/` count | 17+ | **15** | Slight consolidation |
| DonorDock-targeted page | None (404) | **Still none (404 ×4)** | DD lane still open |
| Flagship FAQPage | 4 Qs | **7 Qs** | Schema gap narrowing |
| G2 (Giving Platform) | ~1,199 / 4.6 | ~1,199 / 4.6 | Flat |
| G2 (CRM) | ~872 / 4.7 | ~872 / 4.7 | Flat |
| Capterra | "several hundred," blocked | **1,287 / 4.7 (confirmed)** | Now measured |

**Top 3 things that changed this month:**
1. **Flagship FAQPage deepened 4 → 7 questions** — Bloomerang is closing the FAQ-schema/AEO arbitrage lane DonorDock had on equivalent pages. DD must keep its FAQ schema richer (8+ Qs) to hold the citation edge.
2. **Pricing tightened toward upsell** — Bloomerang Fundraising is now bundle-locked to CRM (no real standalone $40), and the Giving Platform bundle split into Standard/Pro (both Contact-Sales). Strengthens DD's flat-rate, buy-only-what-you-need attack.
3. **Sitemaps consolidated into a single `sitemap.xml`** — segmented post/page/guide sitemaps removed; exact blog-post counting is no longer clean. Working estimate ~700+ (continued pruning). Update tooling that scraped the old per-type sitemap URLs.

**Threat trend: STEADY.** No DonorDock comparison page (lane open second month), reviews flat, comparison program slightly contracted. Offsetting: FAQ-schema depth and pricing-upsell mechanics improved. Net — no escalation against DonorDock specifically this month.

---

**End of report.**
