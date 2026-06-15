---
description: Interactively compose a new document template by picking from existing content blocks. Sales-rep self-service. The new template is saved under tool/templates/_team/ for team review.
argument-hint: [optional name]
---

# /new-template — Compose a new template from existing content blocks

Argument: `$ARGUMENTS` (optional working name for the new template)

You are helping a sales rep create a new template by composing existing content blocks. This is the **self-service** path — they cannot write new HTML, they can only pick from blocks the design system already approves.

## Step 1 — Name it

Ask for a kebab-case template name if not provided. Examples: `partnership-overview`, `renewal-proposal`, `board-pre-read`, `executive-summary`. Validate it doesn't already exist in `tool/templates/` or `tool/templates/_team/`.

## Step 2 — Discover what's available

List the content blocks (you can read each `content-blocks/<name>/meta.md` or call `/list-content-blocks` for the visual gallery). Group them by use:
- Chrome (header-band, footer-band)
- Cover/intro patterns
- Multi-column content (your-moment, tool-consolidation, platform-overview-quad, donor-intelligence-quad)
- Timeline (onboarding-3phase)
- Pricing (pricing-card-purple, pricing-strip-purple)
- Closing (why-donordock-stats, next-steps-numbered)
- Optional inserts (quote-block, competitor-comparison-table, limited-time-offer-sidebar)
- One-pager primitives (before-after-chips, feature-checklist-grid)

## Step 3 — Walk through composition

For each page in the new template, ask:

1. **Which block(s) on this page?** — single block (e.g., just `your-moment`) or composed (e.g., `pricing-card-purple` + `limited-time-offer-sidebar` on one page)
2. **Required or optional?** — required pages always render; optional pages can be toggled off per-document
3. **If optional, what's the default?** — `default: true` (on unless turned off) or `default: false` (off unless turned on)
4. **No chrome?** — full-bleed covers skip the header-band/footer-band wrap

Sanity-check the composition as you go:
- Every multi-page template should start with a cover or `header-band` on page 1
- Every multi-page template needs `next-steps-numbered` or equivalent closing
- A document can't have two `pricing-card-purple` blocks
- A `compose` array shouldn't mix full-page blocks with strip blocks

## Step 4 — Detect missing blocks

If the user describes a layout pattern that doesn't exist (e.g., "I need a 3-column testimonial row"), DO NOT make one up. Tell them: "That layout pattern doesn't exist yet. Closest matches are `feature-checklist-grid` or `donor-intelligence-quad`. If you really need a new pattern, ask Rob or marketing to create a new content block via `/new-content-block`."

## Step 5 — Write the new template

Create the folder and files:

```
tool/templates/_team/<template-name>/
├── definition.json    # the spine
└── sample-data.json   # placeholder data the user filled in
```

Follow the format of `tool/templates/sales-proposal/definition.json`.

## Step 6 — Verify

Run:

```bash
cd ~/Documents/DonorDock/Claude/Projects/Document-Templates/donordock-documents/tool
node build.js <template-name>
```

If it renders without errors and the audit passes, surface the preview path to the user.

## Step 7 — Note the team queue

Remind the user that team-added templates land in `_team/` and Rob reviews them periodically. If two reps create similar templates, Rob may consolidate them into a canonical built-in.

## Don't

- Don't write new HTML, new CSS, or new content blocks. This command composes EXISTING blocks only.
- Don't bypass the schema — every chosen block's `slots.schema.json` must be respected in the sample data.
- Don't allow two of the same block in one spine.
