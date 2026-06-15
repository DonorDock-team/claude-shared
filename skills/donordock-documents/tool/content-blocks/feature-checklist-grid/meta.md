# feature-checklist-grid

**Purpose:** Compact grid of feature/capability labels for one-pagers. Shows platform breadth without taking up the full half-page that `platform-overview-quad` requires.

## When to use

- One-pagers (typically the bottom third of the page)
- Compact summaries in two-page partner overviews

## When NOT to use

- Full sales proposals — use `platform-overview-quad` instead
- Marketing emails — too design-heavy

## Slot definitions

| Slot | Type | Required | Notes |
|---|---|---|---|
| `title` | string | no | Optional heading above the grid, e.g., `Everything included` or `What's in the platform`. |
| `columns` | `3 \| 4 \| 5` | no | Default `4`. Pick 3 for fewer items, 5 for very dense. |
| `items` | array of `{label, accent?}` | yes | 6-15 capability labels. |
| `items[].label` | string | yes | Short capability name, ideally under 24 chars. |
| `items[].accent` | `"purple" \| "blue" \| "green" \| "orange" \| "yellow" \| "coral"` | no | Default `purple`. Color-coded dot. |

## Layout guarantees

- Grid is regular columns × rows
- Each cell has a tiny colored dot left of its label
- No icons (Phase 2+ may add Lucide SVG support)

## Don't

- Don't write sentences in `label` — short phrases only (`Contact records`, `Online giving pages`)
- Don't use more than 15 items — switch to `platform-overview-quad`
- Don't pass emoji as the accent — accents are CSS-driven dots only
