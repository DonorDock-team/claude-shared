# before-after-chips

**Purpose:** Compact "today vs after DonorDock" stack diagram for one-pagers. Strikethrough chips on the left for tools being replaced; solid purple chips on the right for new capabilities; an arrow between. Tools the prospect KEEPS (partner integrations) get a yellow `· kept` chip instead of being struck through.

## When to use

- One-pagers (typically near the top, sets up the transition story)
- Migration/discovery snapshots where the prospect's current tool stack is named

## When NOT to use

- Sales proposals — use `tool-consolidation` instead (more detailed cards)
- When the prospect has no tools to compare against (greenfield deployments)

## Slot definitions

| Slot | Type | Required | Notes |
|---|---|---|---|
| `today.label` | string | yes | Left column header, e.g., `MHF TODAY`. Will be uppercased. |
| `today.items` | array of `{text, kept?}` | yes | Tool chips. Set `kept: true` for items that stay (partner integrations). |
| `today_footnote` | string | no | Small line below the left column. |
| `after.label` | string | yes | Right column header, e.g., `AFTER DONORDOCK` or `ALL IN ONE PLACE`. |
| `after.items` | array of string | yes | New capabilities, ideally pair-matched with the today.items count. |
| `after_footnote` | string | no | Small line below the right column. |

## Layout guarantees

- 1fr / auto / 1fr grid (left col / arrow / right col)
- Strikethrough chips have a 1px gray border + line-through text
- Kept chips have a yellow background (no strikethrough)
- After chips are solid brand-purple with cream text

## Don't

- Don't list more than 8 items per side — they wrap into too many rows
- Don't use this for proposal pages — `tool-consolidation` is the proposal equivalent
- Don't mix kept and strikethrough chips beyond 1-2 kept items — it dilutes the signal
