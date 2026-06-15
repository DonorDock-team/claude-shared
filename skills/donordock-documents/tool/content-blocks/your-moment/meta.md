# your-moment

**Purpose:** Frames the prospect's current situation against what they need from a platform. Sets up the rest of the proposal as "here's why this matters now."

## When to use

- Page 2 of every sales proposal (after the cover)
- Discovery-driven documents where the prospect's situation needs to be named explicitly

## When NOT to use

- One-pagers — too much real estate
- Generic capability decks where there's no specific prospect context
- Renewal proposals — the prospect already knows their situation; use a renewal-specific block instead (Phase 2+)

## Slot definitions

| Slot | Type | Required | Notes |
|---|---|---|---|
| `eyebrow` | string | no | Default `Your Moment`. Uppercased automatically. |
| `title` | string | yes | Main heading text. First line before the highlight. Up to ~40 chars. |
| `highlight` | string | yes | Highlighted phrase, ends the heading. Gets the brand-purple-light chip. |
| `subtitle` | string | yes | 1-2 sentence framing of why this moment matters. |
| `where_you_are` | object | yes | Left column — narrative of the prospect's current state. |
| `where_you_are.title` | string | yes | Card title, e.g., `Where you are today`. |
| `where_you_are.items` | array of `{heading, body}` | yes | 2-4 narrative sub-sections. |
| `what_you_need` | object | yes | Right column — checklist of platform requirements. |
| `what_you_need.title` | string | yes | Card title, e.g., `What you need from a platform`. |
| `what_you_need.items` | array of string | yes | 5-9 checklist items. |
| `quote` | object | no | Optional pull quote anchored at the bottom. |
| `quote.text` | string | yes-if-quote | The quote, in italics. |
| `quote.attribution` | string | yes-if-quote | Speaker name, role, organization. |

## Layout guarantees

- Two-column cream cards, equal width (`grid-template-columns: 1fr 1fr`)
- Each card has its own internal structure: narrative vs. checklist
- Optional quote uses the standard purple-left-border treatment

## Don't

- Don't use more than 4 narrative items in `where_you_are` — they crowd the card
- Don't use more than 9 checklist items in `what_you_need` — the card runs over
- Don't write the heading like a question ("Where are you today?") — keep declarative
