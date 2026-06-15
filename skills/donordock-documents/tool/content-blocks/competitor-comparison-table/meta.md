# competitor-comparison-table

**Purpose:** Side-by-side dimension table comparing DonorDock to 2-3 competitors on dimensions like pricing model, migration cost, support level. DonorDock column visually distinguished in brand-purple.

## When to use

- Optional insert under `pricing-card-purple` when the prospect is shopping competitors
- Comparison sections in evaluation overviews

## When NOT to use

- When DonorDock isn't the clear winner on every dimension you list — don't pick fights you'll lose
- One-pagers — too dense
- Documents going to existing customers

## Slot definitions

| Slot | Type | Required | Notes |
|---|---|---|---|
| `caption` | string | no | Small uppercase line above the table, e.g., `Pricing comparison`. |
| `competitors` | array of string | yes | 2-3 competitor names. Column headers. |
| `rows` | array of `{dimension, donordock_value, competitor_values}` | yes | 2-5 dimensions to compare. |
| `rows[].dimension` | string | yes | What's being compared, e.g., `Pricing` or `Migration`. |
| `rows[].donordock_value` | string | yes | DonorDock's value for this dimension. |
| `rows[].competitor_values` | array of string | yes | One value per competitor, in the same order as `competitors`. |

## Layout guarantees

- DonorDock column always second from left, brand-purple text
- Dimension column is uppercased + muted
- Subtle cream background card

## Don't

- Don't include rows where DonorDock loses — pick dimensions where the comparison clearly favors DonorDock
- Don't write paragraphs in cells — short phrases only
- Don't compare more than 3 competitors at once — the table compresses too tight
