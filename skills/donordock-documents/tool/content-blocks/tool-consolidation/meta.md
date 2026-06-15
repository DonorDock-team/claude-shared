# tool-consolidation

**Purpose:** Before/after page that contrasts the prospect's current disconnected tools with DonorDock's consolidated capabilities. Two columns, equal weight, with a small red callout on the "before" side and a purple callout on the "after" side.

## When to use

- Page 3 of a sales proposal, right after `your-moment`
- Any time the prospect is currently running 3+ fragmented tools and consolidation is the core selling point

## When NOT to use

- Prospects who are new to fundraising tech (no "today" to contrast against)
- Renewal proposals — the prospect is already on DonorDock; "before" doesn't apply
- One-pagers — too dense

## Slot definitions

| Slot | Type | Required | Notes |
|---|---|---|---|
| `eyebrow` | string | no | Default `Tool Consolidation`. |
| `title` | string | yes | First line of the heading, e.g., `One platform`. |
| `highlight` | string | yes | Highlighted second line, e.g., `instead of four.`. Uses `.highlight-blue`. |
| `subtitle` | string | yes | 1-2 sentence framing of the consolidation problem. |
| `today.title` | string | yes | Left column title, e.g., `Today: Four disconnected tools`. |
| `today.items` | array of `{name, body}` | yes | 3-5 cards listing current tools. |
| `today.callout` | `{title, body}` | no | Red/coral callout at the bottom, e.g., `The cost of fragmentation`. |
| `with_donordock.title` | string | yes | Right column title, e.g., `With DonorDock: Everything connected`. |
| `with_donordock.items` | array of `{name, body}` | yes | 3-5 cards. Recommend pairing each with a `today.items` card. |
| `with_donordock.callout` | `{title, body}` | no | Purple callout at the bottom, e.g., `The value of integration`. |

## Layout guarantees

- Two-column grid (`grid-template-columns: 1fr 1fr`), gap `--space-lg`
- "Today" column title is charcoal; "With DonorDock" column title is brand-purple
- Card borders subtle on "today" side, purple-tinted on "with-donordock" side
- Callouts use color-coded left borders (coral for cost, purple for value)

## Don't

- Don't have unequal card counts between today and with_donordock — they should line up visually
- Don't include positive framing in the "today" cards — keep them about the gap/cost
- Don't use generic capability names in `with_donordock.items` — they should explicitly replace something on the left
