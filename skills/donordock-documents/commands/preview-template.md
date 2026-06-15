---
description: Render a template with its built-in sample data so the user can see the design before committing to a real prospect.
argument-hint: <template-name>
---

# /preview-template — Render a template with sample data

Argument: `$ARGUMENTS` (template name — e.g., `sales-proposal` or `one-pager`)

You are rendering a template with the canonical sample data so the user can review the design.

## Step 1 — Validate the template name

Check `tool/templates/<name>/definition.json` exists. If not, list available templates and ask the user which one.

## Step 2 — Build with sample data

```bash
cd ~/Documents/DonorDock/Claude/Projects/Document-Templates/donordock-documents/tool
node build.js <template-name>
```

This uses the bundled `templates/<name>/sample-data.json` (typically the Well Summit example for sales-proposal, MHF for one-pager) and writes to `templates/<name>/preview.html`.

## Step 3 — Surface

Open the rendered preview.html in the user's browser, or note the path. Mention:
- This is the canonical design — what every prospect document inherits from
- To customize for a real prospect, use `/proposal <prospect>` or `/onepager <prospect>`

## Don't

- Don't modify the sample-data.json — that's the canonical reference for the template
