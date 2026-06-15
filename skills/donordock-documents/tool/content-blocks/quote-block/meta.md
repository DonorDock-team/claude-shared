# quote-block

**Purpose:** Standalone pull quote for anchoring a page with a customer or prospect voice. Standard purple-left-border treatment.

## When to use

- Anywhere a customer or prospect quote needs visual weight
- Inside `your-moment`, it's already embedded — don't double up
- Between other content blocks where a moment of breathing room is wanted

## When NOT to use

- For testimonials in a grid — use `testimonial-grid` (Phase 2+)
- For internal narrative copy — that's regular paragraph text

## Slot definitions

| Slot | Type | Required | Notes |
|---|---|---|---|
| `text` | string | yes | The quote itself, will be rendered in italics. |
| `attribution` | string | yes | Speaker name, role, organization. |
| `variant` | `"default" \| "soft" \| "dark"` | no | Default uses light-purple bg. `soft` uses cream. `dark` uses dark callout bg with inverse text. |

## Don't

- Don't wrap the quote text in quotation marks — the styling does the work
- Don't use the dark variant on a dark page background — it'll disappear
