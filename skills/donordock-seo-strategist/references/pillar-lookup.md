# Pillar Lookup — quick reference

Fast-lookup table for pillar → URL → keyword cluster → AEO questions mapping. Use this to route any content or strategic question to the right pillar quickly without re-reading the full `pillars.md`.

**Source of truth:** `seo-brain/strategy/pillars.md`. This doc is a summary; if they conflict, pillars.md wins.

---

## The 7 locked pillars

| # | Pillar | Pillar URL | Flagship role |
|---|---|---|---|
| 1 | **Donor Stewardship** | `/smart-steward-method` | **Master pillar** — anchors Smart Stewardship category |
| 2 | Nonprofit CRM / Donor Database | `/crm` | Category-level buyer evaluation |
| 3 | Online Giving | `/online-giving` | Transactional + counter-Givebutter-tipping |
| 4 | Fundraising Strategy | `/fundraising-strategy` (root) | Strategic planning layer |
| 5 | Donor Engagement / Outreach | `/donor-outreach` | Multichannel communication |
| 6 | AI for Nonprofits | `/otto` | First-mover AI category |
| 7 | Donor Retention | `/donor-retention` (root) | Attack Bloomerang legacy positioning |

---

## Keyword cluster heads by pillar

### Pillar 1 — Donor Stewardship
P0: donor stewardship, donor stewardship plan, smart stewardship, smart steward method
P1: major donor stewardship, monthly donor stewardship, stewardship touchpoints, stewardship framework, donor stewardship strategy

### Pillar 2 — Nonprofit CRM
P0: nonprofit CRM, donor management software, best nonprofit CRM, nonprofit CRM with unlimited contacts, nonprofit CRM pricing
P1: donor database, nonprofit CRM with AI, nonprofit CRM with text messaging, how to choose nonprofit CRM, nonprofit CRM migration

### Pillar 3 — Online Giving
P0: nonprofit online giving, online donation form, 1% platform fee nonprofit
P1: recurring donations nonprofit, Apple Pay donations nonprofit, Google Pay nonprofit, platform fees explained

### Pillar 4 — Fundraising Strategy
P0: nonprofit fundraising strategy, annual fundraising plan, fundraising plan template
P1: capital campaign guide, moves management, major gifts strategy, fundraising campaign calendar, donor pipeline

### Pillar 5 — Donor Engagement / Outreach
P0: nonprofit email marketing, donor communication strategy, nonprofit text messaging
P1: donor nurture sequence, donor thank-you template, donor segmentation, donation receipt template

### Pillar 6 — AI for Nonprofits
P0: AI for nonprofit fundraising, ChatGPT for nonprofits, AI donor stewardship, nonprofit CRM with AI, Otto AI DonorDock, Smart Nudges
P1: AI donor thank-yous, AI prompts for fundraisers, AI donor segmentation

### Pillar 7 — Donor Retention
P0: donor retention, donor retention rate, donor retention benchmarks, donor retention strategies
P1: second gift strategy, lapsed donor reactivation, nonprofit donor retention rate 2026

---

## Pillar → supporting URLs (existing content map)

### Pillar 1 — Donor Stewardship
- Pillar: `/smart-steward-method`
- Intent-match supporting: `/solution/donor-stewardship`
- Content: `/articles/the-relationship-loop-a-nonprofit-stewardship-framework`, `/articles/moves-management`, `/articles/moves-management-for-small-teams-from-hello-to-ask`, `/articles/the-middle-child-effect-why-your-mid-level-donors-are-your-secret-weapon`, `/articles/5-tips-donor-lifecycle`, `/articles/donor-intent`, `/articles/building-a-donor-pipeline-that-lasts`

### Pillar 2 — Nonprofit CRM
- Pillar: `/crm`
- Supporting: `/articles/best-nonprofit-crm`, `/articles/nonprofit-crm-buyers-guide-12-questions-to-ask`, `/articles/nonprofit-crm-migration-checklist`, `/articles/constituent-relationship-management`, `/articles/data-hygiene`, `/articles/nonprofit-glossary`, `/articles/donor-segmentation`, `/articles/10-data-points`
- Comparisons: all 10 `/compare/*` pages

### Pillar 3 — Online Giving
- Pillar: `/online-giving`
- Features: `/features/recurring-donations`, `/features/apple-pay-google-pay`, `/features/scan-to-donate`
- Supporting articles: TBD

### Pillar 4 — Fundraising Strategy
- Pillar: `/fundraising-strategy` (TO BUILD)
- Solutions: `/solution/annual-fund`, `/solution/major-gifts`, `/solution/membership-management`
- Supporting: `/articles/nonprofit-marketing`, `/articles/100-easy-fundraising-ideas`, `/articles/needs-based-budgeting-nonprofit-fundraising`, `/articles/major-donor-pitch-investment-story`, `/articles/why-fundraisers-under-ask-how-to-set-right-ask-amount`, `/articles/5-8-fundraising-plays-that-actually-work`

### Pillar 5 — Donor Engagement / Outreach
- Pillar: `/donor-outreach`
- Features: `/features/email-marketing`, `/features/text-messaging`, `/features/moves-management`
- Supporting articles: TBD

### Pillar 6 — AI for Nonprofits
- Pillar: `/otto`
- Supporting: `/articles/ai-training-for-nonprofits`, `/articles/how-nonprofits-can-use-ai-for-donor-stewardship`, `/articles/why-your-crm-notes-are-your-secret-weapon-and-how-ai-makes-them-even-better`

### Pillar 7 — Donor Retention
- Pillar: `/donor-retention` (TO BUILD)
- Existing: `/articles/donor-retention`, `/articles/donor-engagement`, `/articles/increase-donor-engagement-relationship-fundraising`

---

## Routing logic

Given any content topic, follow this decision tree to find its pillar:

```
Topic mentions donor stewardship, thank-you, acknowledgment, relationship, cultivation journey?
 → Pillar 1 (Donor Stewardship)

Topic mentions CRM, donor database, buyer's guide, software comparison, data management?
 → Pillar 2 (Nonprofit CRM)

Topic mentions donation form, online giving, payment processing, platform fees, recurring donations?
 → Pillar 3 (Online Giving)

Topic mentions fundraising strategy, annual plan, capital campaign, campaign calendar, major gifts tactics?
 → Pillar 4 (Fundraising Strategy)

Topic mentions email, text/SMS, multichannel, donor nurture, thank-you templates, donor segmentation for outreach?
 → Pillar 5 (Donor Engagement / Outreach)

Topic mentions AI, Otto, ChatGPT for nonprofits, Smart Nudges, automation, AI tools?
 → Pillar 6 (AI for Nonprofits)

Topic mentions retention rate, lapsed donors, second gift, recurring donor retention, donor attrition, benchmarks?
 → Pillar 7 (Donor Retention)

Topic mentions multiple pillars (e.g., "AI for donor stewardship")?
 → Pick the PRIMARY pillar (in that case, Pillar 1 because stewardship is the noun; Pillar 6 is the modifier).
 → Cross-link to the secondary pillar in the article body.

Topic doesn't fit any of the 7?
 → Either it's off-strategy and we shouldn't write it, OR
 → It's a new pillar candidate Rob needs to approve before adding to pillars.md.
```
