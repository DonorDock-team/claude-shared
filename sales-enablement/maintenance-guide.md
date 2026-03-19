# Sales Enablement Maintenance Guide

How to keep the Claude Project knowledge base accurate and current.

---

## Update Triggers

Re-upload docs when any of these happen:

| Trigger | What to update | Who owns it |
|---|---|---|
| New feature ships | Product knowledge base | Rob / Marketing |
| Pricing changes | All three docs (pricing refs throughout) | Rob |
| New competitor enters consideration set | Competitor battlecards | Rob / Marketing |
| Competitor changes pricing or features | Competitor battlecards | Rob / Marketing |
| New objection pattern emerges from sales calls | Objection handling playbook | Rob + Sales |
| G2/Capterra ratings or badges change | Product knowledge base (social proof section) | Rob |
| Quarterly review | All docs — full audit | Rob |

---

## Quarterly Audit Checklist

Run this every quarter (set a calendar reminder or build a scheduled Cowork task):

- [ ] Are all pricing numbers current? (Ours + competitors)
- [ ] Are G2/Capterra ratings and badge claims current?
- [ ] Has the user count changed? (Update "7,200+ users" if so)
- [ ] Have any new features launched that aren't in the product knowledge base?
- [ ] Have any competitors made significant changes (pricing, features, acquisitions)?
- [ ] Are there new objections the sales team is hearing that aren't covered?
- [ ] Are the competitive "framing statements" still accurate and useful?
- [ ] Has the ICP or qualification criteria shifted?

---

## How to Update the Claude Project

1. Edit the relevant markdown file in `Projects/Sales-Enablement/`
2. Go to the Claude Project settings
3. Remove the old version of the doc from Project Knowledge
4. Upload the updated version
5. Test with a few questions to verify the new info surfaces correctly

**Tip:** Keep a changelog at the bottom of each doc so you know what changed and when. Example:

```
## Changelog
- 2026-03-18: Initial version
- 2026-04-15: Updated Bloomerang pricing, added Keela battlecard
- 2026-07-01: Q3 audit — refreshed all competitor pricing, updated user count to 8,000+
```

---

## Automating the Prep Work

While you can't auto-upload to a Claude Project, you CAN automate content generation:

**Option 1: Scheduled Cowork task (recommended)**
Set up a monthly task that:
- Pulls latest help center content
- Compares against the product knowledge base
- Flags stale sections
- Drafts updated content for your review

You'd still manually upload, but the hard part (finding what's stale and writing updates) is handled.

**Option 2: Manual monthly check**
Spend 30 minutes monthly scanning for changes. Check:
- DonorDock changelog / release notes
- Competitor pricing pages
- G2 comparison page
- Sales team Slack for recurring questions

---

## Feedback Loop

Ask the sales team monthly:
1. "What questions did the Sales Brain answer well?"
2. "What questions did it get wrong or not know?"
3. "What new objections are you hearing?"

Use the answers to update docs and refine the system prompt.
