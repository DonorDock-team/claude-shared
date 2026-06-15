# limited-time-offer-sidebar

**Purpose:** Time-limited promotion callout. Used as a sidebar next to or under `pricing-card-purple` to flag a waived fee, partner discount, or signing deadline.

## When to use

- Optional add-on next to `pricing-card-purple` when there's a real deadline
- Renewal proposals with seasonal promotions

## When NOT to use

- When there's no time pressure or deadline — it loses meaning
- More than one offer at a time — pick the most compelling

## Slot definitions

| Slot | Type | Required | Notes |
|---|---|---|---|
| `title` | string | yes | Short heading, e.g., `Limited-time offer`. |
| `body` | string | yes | The offer itself. HTML allowed for inline emphasis like `<strong>$3,800</strong>`. |
| `footnote` | string | no | Optional follow-up sentence explaining why this aligns with the prospect's timeline. |
| `variant` | `"default" \| "yellow"` | no | Default is light-purple. `yellow` signals stronger urgency. |

## Layout guarantees

- Colored left border matching the variant
- Compact card — fits as a sidebar to the pricing card

## Don't

- Don't use generic offer copy — name the specific dollar amount and the specific date
- Don't use both `default` and `yellow` variants on the same page
- Don't put pricing details here — those go in `pricing-card-purple`
