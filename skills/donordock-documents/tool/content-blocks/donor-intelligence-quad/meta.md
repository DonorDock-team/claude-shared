# donor-intelligence-quad

**Purpose:** The "AI + relationship intelligence" page. Shows how DonorDock helps the team know their donors and surface the right next steps automatically.

## When to use

- Page 5 of every sales proposal, after `platform-overview-quad`
- Any document where Otto AI and Pipelines are the differentiator

## When NOT to use

- One-pagers — too dense
- Documents where the prospect already understands what a CRM does

## Slot definitions

| Slot | Type | Required | Notes |
|---|---|---|---|
| `eyebrow` | string | no | Default `Donor Intelligence`. |
| `title` | string | yes | First line, e.g., `Know your people.`. |
| `highlight` | string | yes | Highlighted second line, e.g., `Never miss the moment.`. Uses `.highlight-purple`. |
| `subtitle` | string | yes | 1-2 sentence framing. |
| `cards` | array of `{title, accent, body?, items?, mini_cards?}` | yes | Exactly 4 cards. Recommended accent sequence: blue, purple, orange, purple. |
| `cards[].title` | string | yes | Card title. |
| `cards[].accent` | `"blue" \| "green" \| "orange" \| "purple"` | yes | Sectional color. |
| `cards[].body` | string | no | Optional intro paragraph. |
| `cards[].items` | array of string | no | Optional bullet list (3-6 items). |
| `cards[].mini_cards` | array of `{label, body, accent}` | no | Used by the Automations card — 3 mini pills with their own accent (`external`, `internal`, `data`). |

## Layout guarantees

- Grid is 2×2 — exactly 4 cards
- Each card has a tinted background matching its accent (subtle)
- The Automations card uses `mini_cards` instead of `items`
- Bullet list and mini pills are mutually exclusive per card (don't use both)

## Don't

- Don't include pricing or onboarding details here — those have their own blocks
- Don't change the mini-pill accent names — they're matched in CSS to specific tints
