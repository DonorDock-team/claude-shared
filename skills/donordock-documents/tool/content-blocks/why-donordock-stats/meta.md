# why-donordock-stats

**Purpose:** The "why us" page. Stats row at the top, brand-story narrative on the left, G2 recognition + pull quote on the right.

## When to use

- Page 8 of every sales proposal, right before `next-steps-numbered`
- Partnership overviews where credibility/social proof matters

## When NOT to use

- One-pagers — too much real estate; use `feature-checklist-grid` with a small stats strip instead
- Customer-only documents (onboarding playbooks) — they already chose DonorDock

## Slot definitions

| Slot | Type | Required | Notes |
|---|---|---|---|
| `eyebrow` | string | no | Default `Why DonorDock`. |
| `title` | string | yes | First line of heading, e.g., `More than a platform.`. |
| `highlight` | string | yes | Highlighted second line, e.g., `A partnership.`. |
| `subtitle` | string | yes | 1-2 sentence framing. |
| `stats` | array of `{value, label}` | yes | Exactly 4 stats. |
| `narrative.title` | string | yes | Brand-story heading. |
| `narrative.paragraphs` | array of string | yes | 1-3 paragraphs of brand story. |
| `context_card` | `{title, items}` | no | Sub-card under the narrative — typically `Also relevant for X` with bullets of integrations/fit-for-prospect details. |
| `recognition.title` | string | yes-if-recognition | e.g., `G2 Recognition`. |
| `recognition.badges` | array of string | yes-if-recognition | 4 short badges, e.g., `#1 Easiest to Use`. |
| `quote.text` | string | yes-if-quote | Italicized pull quote. |
| `quote.attribution` | string | yes-if-quote | Source. |

## Layout guarantees

- Stats row is exactly 4 columns
- Stat value is brand-purple, 2.5rem bold
- Detail grid below is 2 columns
- Recognition badges grid is 2×2

## Don't

- Don't use more than 4 stats — the grid breaks
- Don't put pricing in stats — pricing has its own block
- Don't write the narrative as a sales pitch — it should read like a story
