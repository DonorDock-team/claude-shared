---
description: Generic document creation — pick from the available DonorDock document templates.
argument-hint: [optional context]
---

# /document — Pick a template and build

Argument: `$ARGUMENTS` (any seed context — prospect name, doc type hint, etc.)

You are helping the user create a DonorDock document but they haven't told you which template to use. Your job is to route them to the right command.

## Step 1 — List available templates

Read each `tool/templates/*/definition.json` and surface them as choices:

- **`sales-proposal`** — 8-9 page formal proposal with cover, problem framing, platform overview, donor intelligence, onboarding timeline, pricing, why DonorDock, and next steps. Use for serious sales conversations and grant-narrative support.
- **`one-pager`** — single Letter page with before/after migration story, capability grid, and compact pricing. Use for first-touch sends, partner referrals, board sneak-peeks.

If there are team-added templates in `tool/templates/_team/`, surface those too.

## Step 2 — Route

Based on the user's context and answer, invoke the right command:

- "I want a full proposal for X" → `/proposal X`
- "I need a quick summary for X" → `/onepager X`
- "Show me what the proposal template looks like" → `/preview-template sales-proposal`

If the user describes a need that doesn't match an existing template (e.g., "I need a board pre-read"), suggest `/new-template` to compose a new one from existing content blocks.

## Don't

- Don't invent template names or describe templates that don't exist on disk
- Don't try to build a document yourself — route to the specific command which has the full build flow
