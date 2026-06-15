---
description: Design a new pixel-locked content block from a description. Gated path — for Rob and marketing only. Output goes to a review queue; never auto-merged.
argument-hint: <description of the new layout pattern>
---

# /new-content-block — Design a new content block (gated)

Argument: `$ARGUMENTS` (a description of the layout pattern the user wants)

You are helping Rob or the marketing team design a NEW content block. This is the **gated path** — every new block is a permanent addition to the design system, so it has to be intentional and on-brand.

## Step 0 — Confirm the user has authority

This command is for design-owning roles (CMO, marketing, brand). If a sales rep landed here by accident, redirect them: "Sales reps create new TEMPLATES (compositions of existing blocks) via `/new-template`. Creating a new BLOCK is design work — let Rob know what pattern you need."

## Step 1 — Compare against existing blocks

Read every `content-blocks/<name>/meta.md` and check whether the requested pattern overlaps significantly with an existing block. If it does, propose the existing block first.

Example overlaps to watch for:
- "A 4-column feature grid" → very close to `feature-checklist-grid`
- "A pricing display" → existing `pricing-card-purple` (full) or `pricing-strip-purple` (compact)
- "A before/after" → existing `before-after-chips` or `tool-consolidation`
- "A 4-quadrant layout" → existing `platform-overview-quad` or `donor-intelligence-quad`

If a real new pattern is needed, continue.

## Step 2 — Spec the new block

Help the user define:

1. **Name** (kebab-case, descriptive, not redundant with existing — e.g., `testimonial-grid-3col`, `roadmap-quarters-row`, `team-photo-strip`)
2. **Purpose** — one sentence: what does it do, why does it exist
3. **When to use / when NOT to use** — for the `meta.md`
4. **Slot definitions** — every named slot, its type, whether required, character limits, allowed values
5. **Layout intent** — describe the visual structure (rows, columns, grid, callouts) so it can be implemented in HTML+CSS

## Step 3 — Generate candidate HTML+CSS

Build a draft `template.hbs` that:

- Uses ONLY design tokens from `tool/tokens.css` (no inline hex colors, no inline font names)
- Uses ONLY the approved card/chip/atom patterns from `tool/base.css`
- Has NO emoji glyphs (use Lucide SVGs or CSS dots)
- Has NO left-side colored border accents (brand is shadow-led, not border-led)
- Uses the shared `.accent-card` class for cards that need tinted/elevated treatment

Bias toward composition: prefer reusing existing partials (header-band, chip, eyebrow-pill, etc.) rather than re-implementing them.

## Step 4 — Write the full block folder

Create:

```
content-blocks/<name>/
├── template.hbs       # the HTML
├── meta.md            # purpose, when to use, slot definitions, don'ts
├── sample-data.json   # realistic example data
└── slots.schema.json  # JSON Schema for validation
```

Follow the format of `content-blocks/cover-purple/` exactly.

## Step 5 — Render preview

```bash
cd ~/Documents/DonorDock/Claude/Projects/Document-Templates/donordock-documents/tool
node preview.js <new-block-name>
node audit.js content-blocks/<new-block-name>
```

The block MUST pass the brand auditor (no emoji errors, no color/font warnings beyond explicitly allowlisted patterns).

## Step 6 — Review queue

The new block is created but NOT yet added to any template. The user (Rob/marketing) should:

1. Review the preview visually
2. Re-run `node gallery.js` so it appears in the visual library
3. Decide whether to add it to existing templates or wait for use cases
4. If approved, commit it; if rejected, delete the folder

## Don't

- Don't auto-add the new block to any template's spine. That's a separate human decision.
- Don't use any hex/rgb/font value not in `tokens.css`. If you need a new color, add it as a TOKEN first, then use the token.
- Don't add an emoji. Ever. The auditor will reject it.
- Don't recreate an existing block under a new name. Always check for overlap first.
