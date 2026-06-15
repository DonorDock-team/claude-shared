---
description: Open the visual gallery showing every content block in the library with rendered previews. Useful for browsing what's available before composing a new template.
argument-hint:
---

# /list-content-blocks — Show the content block gallery

You are surfacing the visual library of content blocks so the user can see what's available.

## Step 1 — Regenerate the gallery (defensive)

```bash
cd ~/Documents/DonorDock/Claude/Projects/Document-Templates/donordock-documents/tool
node preview.js --all
node gallery.js
```

This ensures every content block has a fresh `preview.html` and the gallery is up to date.

## Step 2 — Open or describe the gallery

The gallery lives at `tool/gallery/index.html`. Either:

- **Open in browser** — `open ~/Documents/DonorDock/Claude/Projects/Document-Templates/donordock-documents/tool/gallery/index.html`
- **Or surface inline** — read each `content-blocks/<name>/meta.md` and present a list with name + purpose

## Step 3 — Group by use case

Surface the blocks in three groups so the user can find what they need:

- **Chrome** (used on every page): `header-band`, `footer-band`
- **Proposal pages** (8-9 page sales-proposal templates): `cover-purple`, `your-moment`, `tool-consolidation`, `platform-overview-quad`, `donor-intelligence-quad`, `onboarding-3phase`, `pricing-card-purple`, `why-donordock-stats`, `next-steps-numbered`
- **Optional inserts**: `competitor-comparison-table`, `limited-time-offer-sidebar`, `quote-block`
- **One-pager blocks**: `before-after-chips`, `feature-checklist-grid`, `pricing-strip-purple`

For each block, also give the path to its `meta.md` so the user can read the full slot definitions.

## Don't

- Don't describe blocks from memory — read the actual `meta.md` files
- Don't suggest creating new content blocks via `/new-template` — that command builds new TEMPLATES from existing blocks. To create a new content BLOCK, use `/new-content-block` (which is a gated, design-team workflow)
