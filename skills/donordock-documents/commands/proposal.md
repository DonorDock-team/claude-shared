---
description: Create a DonorDock sales proposal for a prospect — full 9-page document with cover, problem framing, platform overview, pricing, and next steps. Routes through the document-designer + copy-writer subagents so a Zoom transcript or rep notes is enough input.
argument-hint: <prospect-name> [additional context]
---

# /proposal — Create a sales proposal

Argument: `$ARGUMENTS` (prospect name, optionally with seed context like `/proposal The Well Summit — Lily Foundation grant, lean staff`)

You are the orchestrator for creating a complete DonorDock sales proposal. You do not write the proposal yourself — you gather context, hand it to the `document-designer` subagent (which delegates copy generation to `copy-writer`), and then run the build pipeline.

## Step 1 — Gather context

Before invoking the subagent, make sure you have enough to work with. Required at minimum:

- **prospect_name** — pulled from `$ARGUMENTS` if present
- **prepared_by** — the rep's name. Default to the current user; ask if unknown.
- **prepared_by_email** — the rep's email. Default to inferring; ask if unknown.
- **context blob** — what do you actually know about the prospect? Best inputs in priority order:
  1. A Zoom transcript (best — use `zoom-transcript-finder` skill if needed)
  2. HubSpot CRM data (use the HubSpot MCP if available)
  3. Free-form rep notes (paste from rep)
  4. A reference doc the rep shared
  5. Web research (last resort, low fidelity)

If you have a thin context blob, ask the rep for more before invoking document-designer. Bad context → bad proposal.

## Step 2 — Invoke document-designer

Launch the `document-designer` subagent with this brief:

```
Template: sales-proposal
Prospect: <prospect_name>
Prepared by: <rep_name> <rep_email>
Date: <current month year>

Context:
<paste the full context blob here>

Notes from the rep (if any):
<rep's free-form notes>

Specific asks (if any):
- Include competitor table? (default: only if prospect is shopping)
- Include limited-time offer? (default: only if a real offer applies)
- Anything to specifically highlight or downplay?
```

Document-designer will:
- Read the template definition + all block schemas + all block meta files
- Decide which optional blocks to enable
- Delegate per-slot copy generation to copy-writer
- Write a complete `data.json` to `~/Documents/DonorDock/Claude/Deliverables/Proposals/<Prospect-Name>.json`
- Return a summary of decisions + any gaps

## Step 3 — Review the summary with the rep

Surface document-designer's summary to the rep:
- Which optional blocks were enabled and why
- Which were disabled and why
- Any assumptions made due to thin context
- Any quotes that were dropped (because no real quote was in the source)

Give the rep a chance to override any decision before building.

## Step 4 — Build

```bash
cd ~/Documents/DonorDock/Claude/Projects/Document-Templates/donordock-documents/tool
node build.js sales-proposal ~/Documents/DonorDock/Claude/Deliverables/Proposals/<Prospect-Name>.json ~/Documents/DonorDock/Claude/Deliverables/Proposals/<Prospect-Name>.html
```

The post-build hook runs the brand auditor automatically.

## Step 5 — Audit handoff

If the audit found:

- **Emoji errors** — the build FAILED. Something in the data introduced an emoji. Invoke `brand-auditor` for details, fix the data.json, rebuild.
- **Color/font warnings** — the build succeeded but flag-worthy issues exist. Surface them to the rep with the auditor's recommendations.
- **No findings** — confirm clean.

## Step 6 — Surface result

Hand the rep:

- The path to the generated `.html`
- A one-paragraph summary of what document-designer produced (e.g., "9 pages, with competitor table off, limited-time offer off, Otto AI emphasized in donor-intelligence section")
- The audit verdict
- A reminder that PDF export is in flight (Phase 4.5) — for now, share the HTML or print/export to PDF from the browser

## Don't

- Don't write the copy yourself. Delegate to document-designer + copy-writer. The whole point of the subagents is voice consistency and schema enforcement.
- Don't bypass the audit. If emoji errors come up, fix them — don't skip with `--no-audit`.
- Don't fabricate prospect facts. If context is thin, ask the rep before invoking subagents.
- Don't ship a proposal with quote slots filled by invented quotes. If no real quote is available, drop the quote block.
