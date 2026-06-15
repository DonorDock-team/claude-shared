---
description: Create a single-page DonorDock summary — before/after migration story, capability grid, and compact pricing strip on one Letter page. Routes through document-designer + copy-writer so a paragraph of rep notes is enough input.
argument-hint: <prospect-name> [additional context]
---

# /onepager — Create a one-page summary

Argument: `$ARGUMENTS` (prospect name, optionally with seed context)

You are the orchestrator for creating a single-page DonorDock summary. You delegate the work to `document-designer` + `copy-writer` rather than writing the page yourself.

## Step 1 — Gather context

Required minimum:

- **prospect_name** — from `$ARGUMENTS` or ask
- **prepared_by** + **prepared_by_email** — rep identity
- **context blob** — what's known about the prospect:
  - Their current tools (CRITICAL — drives the `before-after-chips` block. Note any tools they'll KEEP, like GoFundMe Pro or OneCause partner integrations)
  - Their pain point in one or two sentences
  - Any specific capabilities you want to highlight

One-pagers tolerate thinner context than full proposals — but the current tool stack is essential.

## Step 2 — Invoke document-designer

Launch the `document-designer` subagent with:

```
Template: one-pager
Prospect: <prospect_name>
Prepared by: <rep_name> <rep_email>
Date: <current month year>

Context:
<paste the full context blob here>

Current tool stack (required):
- <tool 1>
- <tool 2> [keep — partner integration]
- <tool 3>
- ...

Pain point:
<one or two sentences>
```

Document-designer composes data for three blocks (`before-after-chips`, `feature-checklist-grid`, `pricing-strip-purple`), delegates copy to copy-writer, and writes `~/Documents/DonorDock/Claude/Deliverables/Proposals/<Prospect-Name>-OnePager.json`.

## Step 3 — Review with rep

Quickly walk the rep through:
- Which feature-checklist items were selected (12-cell grid, color-grouped)
- Which tools were marked KEPT vs. REPLACED
- The compact pricing-strip composition
- Any context gaps

## Step 4 — Build

```bash
cd ~/Documents/DonorDock/Claude/Projects/Document-Templates/donordock-documents/tool
node build.js one-pager ~/Documents/DonorDock/Claude/Deliverables/Proposals/<Prospect-Name>-OnePager.json ~/Documents/DonorDock/Claude/Deliverables/Proposals/<Prospect-Name>-OnePager.html
```

## Step 5 — Single-page sanity check

After building, sanity-check that the page actually fits on ONE Letter page. If `feature-checklist-grid` has too many items or `before-after-chips` has too many strikethrough chips, the page may overflow. If you suspect overflow:

- Trim feature-checklist-grid to 8-12 items
- Trim before-after-chips to ≤ 8 chips per side
- Re-build

## Step 6 — Surface result

Hand the rep:
- Path to the generated `.html`
- Confirmation of what's on the page
- Audit verdict
- "Open in browser and print → Save as PDF for sharing"

## Don't

- Don't use the full `pricing-card-purple` block — it's too tall for a one-pager. The `pricing-strip-purple` is the right choice (document-designer should pick this automatically).
- Don't write copy directly. Delegate to copy-writer.
- Don't include all 17 content blocks. A one-pager is intentionally minimal.
- Don't include emoji icons.
