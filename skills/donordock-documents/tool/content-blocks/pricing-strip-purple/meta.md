# pricing-strip-purple

**Purpose:** Compact horizontal pricing block for one-pagers. The condensed version of `pricing-card-purple` — fits in the bottom third of a single page.

## When to use

- One-pagers and partner overviews where the full pricing-card-purple is too tall
- Compact pricing displays in batch outreach pages

## When NOT to use

- Full sales proposals — use `pricing-card-purple` instead
- Internal documents

## Slot definitions

| Slot | Type | Required | Notes |
|---|---|---|---|
| `price.amount` | string | yes | e.g., `$500`. |
| `price.period` | string | yes | e.g., `/month`. |
| `price.billing_note` | string | no | e.g., `$6,000 billed annually`. |
| `chips` | array of string | no | 2-4 short feature chips. |
| `included` | array of string | yes | 4-8 short feature lines (no $-signs or icons). |
| `footnote.title` | string | yes-if-footnote | Bold lead, e.g., `Q2 onboarding offer:`. |
| `footnote.body` | string | yes-if-footnote | The rest of the offer line. |

## Layout guarantees

- Purple background with cream/inverse text — matches `pricing-card-purple`
- 2-col grid: amount + chips on left, 2-col include list on right
- Optional footnote pill sits below the include list

## Don't

- Don't use more than 8 include items — the right side overflows
- Don't put paragraphs in `included` — short phrases only
- Don't use without a one-pager context — for proposals, the full card is the right pattern
