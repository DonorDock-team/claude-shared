# AEO Questions Universe

**Locked:** 2026-04-23
**Owner:** Rob Burke (CMO)
**Refresh:** Quarterly
**Source:** Phase 1 AEO audit + competitor FAQ analysis + pillars.md

Questions we want DonorDock to answer in Google Featured Snippets, People Also Ask, ChatGPT, Perplexity, Google AI Overviews, Gemini, Apple Intelligence. Each question tagged to pillar + target URL + answer format. Deploy via FAQPage schema on target pages.

---

## Tier 1 — Brand / transactional (own within 30 days)

These are pure-intent queries where a prospect is evaluating DonorDock or actively buying.

| Question | Pillar | Target URL | Answer format |
|---|---|---|---|
| What is DonorDock? | (all) | / (homepage) | 40-word definitional paragraph |
| How much does DonorDock cost? | CRM | /pricing | Direct "DonorDock is $500/month with unlimited contacts…" |
| Does DonorDock have a free trial? | CRM | /pricing or /get-a-trial | Direct answer |
| Is DonorDock good for growing nonprofits? | CRM | / or /crm | Direct + ICP statement |
| How does DonorDock compare to Bloomerang? | CRM | /compare/bloomerang-vs-donordock | Structured table + answer |
| How does DonorDock compare to DonorPerfect? | CRM | /compare/donorperfect-vs-donordock | Same |
| How does DonorDock compare to Givebutter? | CRM | /compare/givebutter-vs-donordock | Same (with 1% vs 3% framing) |
| How does DonorDock compare to Little Green Light? | CRM | /compare/little-green-light-vs-donordock | Same |
| Does DonorDock integrate with QuickBooks? | CRM | /integrations/quickbooks | Direct yes + how |
| Does DonorDock integrate with Mailchimp? | Outreach | /integrations/mailchimp | Same |
| Can I migrate from Bloomerang to DonorDock? | CRM | /compare/bloomerang-vs-donordock | Yes + 90-day onboarding explanation |
| Does DonorDock charge platform fees? | Online Giving | /pricing | Honest 1% answer |

## Tier 2 — Category-education (own within 90 days)

These are informational queries where the prospect is problem-aware but pre-DonorDock awareness. Where AI engines most often cite a source.

### Donor Stewardship pillar
- What is donor stewardship?
- What is the Smart Steward Method?
- What is Smart Stewardship?
- How do I build a donor stewardship plan?
- What are donor stewardship best practices?
- How often should I thank donors?
- What is a stewardship journey?
- What is a stewardship touchpoint?
- How do I steward major donors?
- How do I steward monthly donors?

### Nonprofit CRM pillar
- What is a nonprofit CRM?
- What is the difference between a nonprofit CRM and donor database?
- What features should a nonprofit CRM have?
- How do I choose a nonprofit CRM?
- How much does nonprofit CRM software cost?
- How long does nonprofit CRM implementation take?
- Can I use a spreadsheet instead of a CRM?
- How do I migrate donor data to a new CRM?
- What is the best nonprofit CRM for growing organizations?
- Do I need a nonprofit CRM?

### Online Giving pillar
- How do platform fees work for nonprofit donations?
- What is the difference between a 1% and 3% platform fee?
- How do I accept Apple Pay donations?
- How do I set up recurring donations?
- What is the best online giving platform for growing nonprofits?
- Do donors pay the platform fee or does the nonprofit?
- Are nonprofit platform fees tax-deductible?
- How do I embed a donation form on my website?

### Fundraising Strategy pillar
- How do I build a nonprofit fundraising plan?
- What is moves management?
- How do I run a capital campaign?
- What is a major gifts strategy?
- How do I segment donors for fundraising?
- What are the key nonprofit fundraising KPIs?
- How do I build an annual fundraising calendar?
- What is a donor pipeline?

### Donor Engagement / Outreach pillar
- How do I write a donor thank-you letter?
- How often should nonprofits email donors?
- Should nonprofits use text messaging?
- What is a donor nurture sequence?
- How do I segment donors for email?
- What should be in a donor welcome email?
- How do I acknowledge major donors?
- What is multichannel donor engagement?

### AI for Nonprofits pillar
- How can AI help nonprofit fundraising?
- What is Otto (DonorDock AI)?
- How can ChatGPT help nonprofits?
- Can AI write donor thank-yous?
- What is AI donor segmentation?
- How do I use AI for donor stewardship?
- What is AI-assisted fundraising?
- Are AI tools safe for nonprofit donor data?

### Donor Retention pillar
- What is donor retention rate?
- What is a good donor retention rate?
- How do I improve donor retention?
- Why do donors stop giving?
- What is second-gift retention?
- How do I reactivate lapsed donors?
- How do I benchmark donor retention?
- What is recurring donor retention?

---

## Tier 3 — Long-tail and voice-search (own within 12 months)

Voice search and AI assistants extract from these. Keep answers 14-29 words where possible.

- "Hey Siri, what's the best donor management software for a nonprofit?"
- "How do I set up online giving for a nonprofit?"
- "How do I automate donor thank-yous?"
- "What software do nonprofits use for fundraising?"
- "How do nonprofits segment their email lists?"
- "What is a CRM for nonprofits?"
- "How much does donor management software cost?"
- "How do I retain monthly donors?"
- Plus a growing set of transcribed podcast-quote-worthy Q&A pairs from Focused Fundraiser episodes

---

## Deployment rules (schema)

1. **Every pillar page** gets FAQPage schema with 10+ Tier 1/2 questions from its pillar section above.
2. **Every compare page** gets FAQPage schema with 6-8 competitor-specific Qs (from competitor-landscape.md).
3. **Every top-20 article** gets 5-8 FAQPage Qs drawn from Tier 2 pool above.
4. **Answer length:** 40-60 words for paragraph snippets; 14-29 words for voice-search-eligible answers.
5. **Answer opener:** Lead with direct answer ("Yes,", "No,", "X is Y,") then elaborate.
6. **Every answer must cite a source** or reference a DonorDock product/feature/methodology (Smart Stewardship, Smart Steward Method, Smart Nudges, Action Board, Otto).

---

## Content standard for answer-ready blocks

Every pillar article has:
- **TL;DR block** at top (answer the headline question in 40 words)
- **FAQ section** at bottom (5-8 Qs from this universe)
- **Question-format H2/H3** where aligned to intent
- **Numbered lists** for how-to content (HowTo schema-eligible)
- **Comparison tables** where competitor content is relevant (Table + ItemList schema-eligible)

---

## Priority deployment roadmap

**Week 1-2 (Phase 2 kickoff):**
- Deploy FAQPage schema on /pricing (10 Qs already live — just need schema wrapping)
- Deploy FAQPage schema on all 10 compare pages (6-8 Qs each) — schemas already drafted in remediation/
- Tier 1 "Brand/transactional" Qs live across comparison pages

**Month 1-2:**
- FAQPage schema on all 7 pillar pages
- Tier 2 "Category education" Qs deployed in pillar page FAQ sections
- Start building missing content for unanswered category Qs (donor retention strategies, AI for nonprofits guide, etc.)

**Month 3-6:**
- Tier 3 long-tail + voice search coverage
- Quarterly AEO rankings review
- Expand to 200+ Qs total

Total target: 200 FAQPage-schema-wrapped questions across the site by end of Q3 2026.
