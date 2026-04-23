# DonorDock Brand Positioning Rules

**Owner:** Rob Burke (CMO)
**Locked:** 2026-04-23
**Scope:** All seo-brain content, strategy docs, website copy, schemas, articles, AI outputs

This document is the source of truth for DonorDock positioning language. Every strategy doc, article, schema, and audit report must follow these rules. When content conflicts with this doc, this doc wins.

---

## 1. Product / feature naming

| Correct | Wrong | Notes |
|---|---|---|
| Action Board | ActionBoard | Two words. Rebranded 2026. Update all references. |
| Smart Steward Method | SmartStewardMethod | Spaced. Proprietary framework. |
| Smart Nudges | SmartNudges | Spaced. |
| Otto | OttoAI, Otto AI Assistant (in body copy, refer to "Otto" alone; "Otto AI assistant" only for first-introduction context) | AI assistant product. |
| Smart Stewardship | — | Brand-wide positioning/tagline. THE owned category. |
| DonorDock | Donor Dock, donor-dock | One word, capital D-D. |

## 2. Owned category / positioning

**Primary tagline / positioning:** **Smart Stewardship**

This is DonorDock's owned category term — equivalent to Virtuous's "Responsive Fundraising." Every pillar article, comparison page, ad, and announcement anchors back to Smart Stewardship. The supporting product elements (Smart Steward Method, Smart Nudges, Action Board, Otto) all reinforce the Smart Stewardship narrative.

**How to use Smart Stewardship:**
- In pillar article intros: explicitly name Smart Stewardship as the methodology
- In comparison pages: frame the "why DonorDock" answer through the Smart Stewardship lens
- In llms.txt: lead with Smart Stewardship as the category
- In schema: position as `knowsAbout` on author Person schema for Rob, Matt, and other named experts
- In ads: headline variants using "Smart Stewardship" language

## 3. Target ICP (UPMARKET DIRECTION)

### Use these terms
- **Growing nonprofits** (primary descriptor)
- **Mid-sized nonprofits**
- **Development teams** (when referring to the buyer team)
- **Development Directors** (when referring to the individual buyer)
- **Nonprofits with 1,000–50,000 contacts** (sizing)
- **Upgrading from [legacy CRM or spreadsheets]** (when messaging migration)

### Do NOT use
- **Small nonprofits** (too downmarket; DonorDock is moving up)
- **Tiny nonprofits / solo ED / one-person shop** (downmarket ICP)
- **First CRM** (suggests early-stage; we target upgraders, not first-timers)
- **Starting a nonprofit** (not an ICP pillar anymore)
- **Volunteer-run nonprofits** (too small for current ICP)
- **Under-$500k budget nonprofits** (too small)

### Rationale
DonorDock's strategic direction is moving upmarket. Historically the site used "small-to-mid nonprofits" — this is being replaced by "growing and mid-sized nonprofits." The small-tier messaging is not abandoned on the live site yet, but new content, strategy docs, and schema should follow the upmarket direction.

## 4. Verticals — what we target, what we don't

### Priority verticals (active targets)
- Human services nonprofits
- Arts & culture
- Education foundations (university foundations, K-12 districts with development teams)
- Environmental nonprofits
- Healthcare foundations
- Advocacy nonprofits
- Community foundations
- Animal care (larger organizations)

### DE-PRIORITIZE (not a fit)
- **Churches** (congregational / ChMS-integrated fundraising) — NOT a DonorDock ICP fit. Do not recommend DonorDock target individual churches or congregational giving use cases (Planning Center / Breeze / Tithe.ly own this).
- **Religious organizations where the primary use case is weekly offering / tithing** — NOT fit.

### NOTE: "Faith-based" is OK as a vertical
- **Faith-based nonprofits** that operate as 501(c)(3)s doing fundraising (e.g., faith-based community foundations, religious ministries with formal development programs, rescue missions, religious social services, parachurch organizations) ARE a valid DonorDock target. The distinction is: churches-as-churches are not ICP; faith-based nonprofits that fundraise like other nonprofits ARE ICP.
- Content may reference faith-based donor programs, faith-based fundraising strategy, religious nonprofit operations.
- Very small all-volunteer orgs (below 1,000 contacts or under $250k budget)
- International nonprofits (US-focused)

## 5. Pillar strategy (locked 2026-04-23)

The canonical pillar list is:
1. **Donor Stewardship** (`/solution/donor-stewardship` + supporting cluster)
2. **Nonprofit CRM / Donor Database** (`/crm` + cluster)
3. **Online Giving** (`/online-giving` + cluster)
4. **Fundraising Strategy** (needs new pillar page; 59 articles to cluster)
5. **Donor Engagement / Outreach** (`/donor-outreach` as hub — NOT /guides/donor-engagement; 65 articles to cluster)
6. **AI for Nonprofits** (`/otto` as pillar, expanding)
7. **Donor Retention** (new pillar; Rob's core narrative)

### REMOVED from pillar list
- ~~Starting a Nonprofit~~ — removed 2026-04-23 (upmarket move; not ICP)

## 6. Pricing & platform fee messaging

**Always say:**
- "$500/month" (flat)
- "Unlimited contacts"
- "5 users included"
- "1% platform fee on online donations"
- "Plus standard Stripe/PayPal processing fees (typically 2.2% + $0.30 for nonprofits)"
- "No long-term contracts, no hidden fees"
- "90-day money-back guarantee"

**Never say:**
- "Free processing" or "no processing fees"
- "No platform fees" (we DO have a 1% platform fee)
- "Always free" (brand rule — never claim free)

## 7. Competitive positioning guardrails

When comparing to competitors:
- Lead with **Smart Stewardship** as DonorDock's category, not just "all-in-one nonprofit CRM"
- Frame the value proposition upmarket: transparent pricing predictability, Smart Stewardship methodology, Action Board/Smart Nudges/Otto/Smart Steward Method product ecosystem
- Name competitor features accurately; don't disparage
- Target buyers actively evaluating or ready to migrate — NOT first-time buyers

## 8. Schema / structured data positioning

When writing schema:
- `applicationSubCategory`: "Nonprofit CRM" or "Donor Management Software"
- `audience.audienceType`: "Growing and mid-sized nonprofits, 501(c)(3) charities, development teams"
- `knowsAbout` on Person schema (Rob, Matt): include "Smart Stewardship," "donor stewardship," "nonprofit fundraising"
- `award` / `knowsAbout` can reference Smart Steward Method, Action Board, Smart Nudges, Otto as named proprietary methodologies/products

## 9. Numeric references (fact-checked 2026-04-23)

When citing DonorDock metrics in content or schema:

| Fact | Verified value | Source |
|---|---|---|
| Sitemap URLs | 619 | https://www.donordock.com/sitemap.xml |
| Articles | 281 | Sitemap count of /articles/* |
| Tag archive pages | 49 | Sitemap count of /tags/* |
| Feature pages | 62 | Sitemap count of /features/* |
| Integration pages | 60 | Sitemap count of /integrations/* |
| Team bio pages | 36 | Sitemap count of /team/* |
| Comparison pages | 10 | Sitemap count of /compare/* |
| Solution pages | 10 | Sitemap count of /solution/* |
| Tool pages | 47 | Sitemap count of /tools/* |
| Customer reviews | 200+ | Aggregate from G2 + Capterra (verify quarterly) |
| Rating | 4.8/5 | Aggregate |
| Users (individual logins) | 7,200+ | llms.txt / site claim |
| Customer nonprofits (organizations) | ~1,300 | Rob 2026-04-23 clarification |
| Gifts tracked | $9B+ | llms.txt / site claim |
| Founded | 2017 | Fargo, ND |
| Founders | Matt Bitzegaio + Andrew Lutgen | |

### DO NOT cite these (outdated or inflated)
- ~~"467 articles"~~ — incorrect. Use 281.
- ~~"88 tag archive pages"~~ — incorrect. Use 49.
- ~~"1,115 URLs" / "sitemap grew to 1,115"~~ — fabricated. Actual 619.
- ~~"$79/month"~~ — outdated pricing. Use $500/mo.

## 10. Language patterns to watch in Phase 2+

When drafting new content, audit for:
- Any mention of "small nonprofits" → replace with "growing nonprofits"
- Any mention of "first CRM" or "first donor database" → reframe as "upgrading from legacy"
- Any mention of "solo ED" / "one-person shop" → reframe as "development team" or "development director"
- Any mention of "church" / "congregational" / "tithing" as DonorDock target vertical → remove (OK in competitor descriptions)
- "Faith-based" (non-church) nonprofits ARE OK as DonorDock target — fundraising-focused 501(c)(3)s with development programs
- Any mention of "ActionBoard" → correct to "Action Board"
- Any mention of "no platform fees" / "free processing" → correct to "1% platform fee"

## 11. When rules are unclear

Escalate to Rob before publishing content that:
- Makes a brand claim not covered in this doc
- Targets a vertical not listed above
- Cites a numeric fact not on the table in section 9
- Uses competitive language about named competitors beyond descriptive factual comparison

---

**This doc supersedes all prior positioning language in seo-brain/audits/, seo-brain/remediation/, and related files. When content conflicts, this doc wins. Updates require Rob's approval and a commit message starting with `brand-positioning:`.**
