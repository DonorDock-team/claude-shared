# Competitor Quick Reference

One-line-per-competitor fast lookup. Use when answering a competitor question without re-reading the full `competitor-landscape.md` or individual audit files.

**Source of truth:** `seo-brain/strategy/competitor-landscape.md` + `seo-brain/audits/2026-04-baseline/competitors/*.md`.

---

## Tier 1 — Active threats, head-to-head

### Virtuous (virtuous.org) 🔴
- **Position:** "Responsive Fundraising" category owner, book + playbook + RNS summit + 5 vertical benchmark reports + Chief AI Officer
- **Pricing:** ~$8,000/year (~$667/mo) enterprise tier. Upmarket shift from historical $199/mo entry.
- **Content:** 646 posts + 187 pages + 75 case studies + 41 gated (2.8-10x DonorDock)
- **ICP overlap:** Targets up to $5M — direct overlap with DonorDock upper ICP
- **Vs DonorDock:** NEITHER publishes a /compare. **First-mover wins SERP.**
- **DonorDock attack:** Operational vs philosophical category framing (Smart Stewardship is systematic; Responsive is philosophical)

### Givebutter (givebutter.com) 🔴
- **Position:** Freemium, consumer UI, 3% platform fee donor-tip-offset model
- **Pricing:** "Free" + 3% platform fee (or "tip-covered" — donor psychology manipulation)
- **ICP overlap:** Below DonorDock mid-market floor historically; moving upmarket
- **Vs DonorDock:** Their `/alternatives/donordock` ranks #1 for "givebutter vs donordock." Shared template (not custom hit piece). Defensible.
- **DonorDock attack:** 1% transparent vs 3% hidden. TCO calculator. Donor-trust defense (public reviews document "dark pattern" complaints). 871 vs 33 reviews = social proof gap.

### Bloomerang (bloomerang.com) 🟡
- **Position:** "Retention-first CRM" — original founding promise
- **Pricing:** OPAQUE. /pricing returns 403 to scrapers. Tiered by contact count.
- **Content:** ~2,000 URLs (1,306 blog + 152 pages + 72 guides + 100+ case studies). Decade of authority.
- **Vs DonorDock:** Publishes ZERO public comparison pages. DonorDock owns the SERP.
- **Technical:** Yoast auto-generated llms.txt (78 lines, surface). NO SoftwareApplication/AggregateRating on homepage.
- **DonorDock attack:** Pricing transparency content ("Bloomerang pricing calculator at 2,500 / 5,000 / 10,000 contacts"). Smart Stewardship as "retention is a stewardship outcome" — reframe the category.

---

## Tier 2 — Direct, meaningful overlap

### Bonterra / Network for Good (bonterratech.com) 🟡
- **Position:** Consolidated "Bonterra Network for Good" product line. 10-product suite. Legacy NFG domain 301s to Bonterra.
- **Pricing:** Gated.
- **Direct attack:** **Mentions DonorDock by name dismissively** in /blog/nonprofit-crm-guide as "entry-level" with "limited communication features." **DonorDock is OMITTED from their newer "31+ top solutions 2026" listicle.**
- **DonorDock attack:** Counter-message the "entry-level" mention. Migration content ("leaving Bonterra"). Author E-E-A-T (they have 993 posts with NO bylines).
- **DonorDock's /compare page:** /compare/network-for-good-vs-donordock — Rob fixed stale pricing recently; hidden-table instance at `.compare-page-table-body.hidden` may still need cleanup.

### DonorPerfect (donorperfect.com) 🟡
- **Position:** 20-year incumbent. 75,000 professionals / 11,000 orgs / 25+ sectors.
- **Pricing:** Opaque. Core/Plus/Pro tiers. Starts ~$450/mo. Modular add-ons for auctions, crowdfunding, moves mgmt.
- **Content:** ~800 URLs (648 blog + 157 pages). 265 posts tagged "fundraising-software."
- **Vs DonorDock:** Publishes /compare pages for Keela, Bloomerang, Raiser's Edge, Salesforce, Kindful — **but NOT DonorDock.** Uncontested SERP.
- **Technical:** Yoast default schema. NO SoftwareApplication/AggregateRating/FAQPage. **ZERO author bylines on 648 posts** — major E-E-A-T leapfrog opportunity.
- **DonorDock attack:** Author bylines + Person schema are our moat. Modular pricing attack ("DonorPerfect hidden costs at X-feature level"). Schema upgrade catches us up.

### Neon One (neonone.com) 🟡
- **Position:** "Suite / platform." Neon CRM + Neon Websites + Neon Giving + Neon Pay.
- **Pricing:** $99-$409/mo tiered. Add-on %: +10% memberships, +20% events, 3% processing.
- **Technical:** **Cloudflare WAF hard-blocks programmatic access** (403 to curl, WebFetch, Googlebot-UA). Our audit relied on SERP + G2/Capterra/press.
- **Vs DonorDock:** Neon's /compare covers Bloomerang/Salesforce/Blackbaud/DonorPerfect/WildApricot — NOT us.
- **DonorDock attack:** "Suite vs ONE plan" is the cleanest wedge. $99 Essentials is a lure; real total cost with events + memberships + payments lands $150-$300+/mo. DonorDock flat $500 wins clearly at 2,500+ contacts.
- **Research asset:** Neon has "Generosity Report" + "Recurring Giving Report." DonorDock's State of Stewardship Report counters with DIFFERENT angle (stewardship, not dollars).

---

## Tier 3 — Adjacent or receding

### Little Green Light (littlegreenlight.com) 🟢
- **Position:** "Affordable donor management for small and mid-sized nonprofits." 15+ years, 10,000+ customers.
- **Pricing:** $45-$135/mo tiered by constituent count. No platform fees. Unlimited users.
- **ICP:** LGL skews below DonorDock's upmarket direction. We exit competition as we move up.
- **Technical:** **Blocks ClaudeBot/CCBot/Google-Extended via Cloudflare.** Exiting AI-search surface. Publishes Yoast-auto llms.txt while blocking the bots that need to read it (contradiction).
- **Vs DonorDock:** LGL has ONE compare page (Kindful alternative only). We're #1 for "Little Green Light alternative."
- **DonorDock attack:** "Modern / AI / easy" cluster (LGL can't credibly target). Migration-from-LGL hub (10,000-customer switcher pool). Unlimited-contacts (LGL jumps to $90/mo at 20k contacts).

### Keela (keela.co) 🟢
- **Position:** "All-in-one nonprofit CRM" + Keela Academy education layer. Canadian-origin with strong CRA/bilingual content.
- **Pricing:** Tiered ~$99/mo starting, scales by contacts.
- **ICP:** High overlap on small-mid US but Canadian/international is their moat.
- **Technical:** Webflow + Elementor + Yoast. Permissive AI bot posture.
- **Vs DonorDock:** Keela does NOT publish /vs/donordock. First-mover wins.
- **DonorDock attack:** US-specific IRS/501(c)(3)/state compliance content (Keela weak here). Template/toolkit gap (Keela owns that space for Canadian nonprofits).

---

## Comparison page coverage map

| Competitor | DonorDock's /compare page | Competitor's vs-DonorDock page |
|---|---|---|
| Bloomerang | /compare/bloomerang-vs-donordock | **None** — uncontested |
| DonorPerfect | /compare/donorperfect-vs-donordock | **None** — uncontested |
| Network for Good (Bonterra) | /compare/network-for-good-vs-donordock | **None** — uncontested |
| Givebutter | /compare/givebutter-vs-donordock | **/alternatives/donordock** — ranks #1, shared template |
| Neon CRM | /compare/neon-crm-vs-donordock | **None** — uncontested |
| Little Green Light | /compare/little-green-light-vs-donordock | **None** — LGL only has Kindful alt page |
| eTapestry | /compare/etapestry-vs-donordock | **None** |
| Bonterra | /compare/bonterra-vs-donordock | Same as NFG (Bonterra = parent) |
| Salesforce (NPSP) | /compare/salesforce-vs-donordock | **None** |
| Spreadsheets | /compare/spreadsheets-vs-donordock | N/A |
| **Virtuous** | **MISSING — must build (Priority 1)** | **None** — first-mover wins |
| **Keela** | **MISSING — must build** | **None** — first-mover wins |
| **Kindful** (now Bloomerang) | MISSING — consider | — |

---

## Rules for invoking competitor claims

1. **Cite source:** every competitor fact must cite a specific line in a competitor audit file or `competitor-landscape.md`
2. **Freshness:** if a pricing or product claim is >30 days old, flag as "may need re-verification"
3. **Never disparage:** factual, comparison-based language only. If tempted to disparage, re-frame through "who we're for" vs "why they're bad"
4. **Match the audit:** if a competitor audit says X, don't contradict X without justification. Update the audit if new info surfaces.
5. **Quarterly refresh required** — next scheduled 2026-07-22
