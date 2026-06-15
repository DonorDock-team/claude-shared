# pricing-card-purple

**Purpose:** Investment summary page. Big purple price card up top, two-column breakdown (everything included + contextual sidebar) below, optional guarantee callout at the bottom.

## When to use

- Page 7 of every sales proposal
- Partnership overviews and quote documents

## When NOT to use

- One-pagers — use `pricing-card-compact` instead (Phase 2+)
- Internal documents
- Anything where there's no clear price to commit to

## Slot definitions

| Slot | Type | Required | Notes |
|---|---|---|---|
| `eyebrow` | string | no | Default `Investment Summary`. |
| `title` | string | yes | First line of heading. |
| `highlight` | string | yes | Highlighted second line. |
| `subtitle` | string | yes | 1 sentence framing. |
| `price.amount` | string | yes | The dollar figure, e.g., `$500`. No currency symbol logic — pass exactly what to render. |
| `price.period` | string | yes | e.g., `/month`. |
| `price.billing_note` | string | no | e.g., `$6,000 billed annually`. |
| `price.chips` | array of string | no | 3-5 chip badges shown to the right of the price. |
| `included.title` | string | yes | e.g., `Everything included`. |
| `included.items` | array of string | yes | 6-12 features. |
| `sidebar` | `{title, body?, items?}` | no | Right column. Use for context-specific framing (e.g., "For your Lily Foundation proposal"). |
| `guarantee` | `{title, body}` | no | Green-tinted callout at the bottom. |

## Layout guarantees

- Price card uses `--brand-purple` background with cream/inverse text
- Price amount is 3.5rem bold, vertically centered
- Two-column detail grid below
- Sidebar (when present) uses light-purple bg + purple title
- Guarantee callout uses green-light bg + green text

## Don't

- Don't put marketing copy in `included.items` — these are feature names, short and concrete
- Don't render more than 12 included items — switch to two columns or split the page
- Don't use red/orange/yellow chips in `price.chips` — they fight the purple. Stick with `.chip-purple-outline`.
