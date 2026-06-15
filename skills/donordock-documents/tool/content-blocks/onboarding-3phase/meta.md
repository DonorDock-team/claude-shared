# onboarding-3phase

**Purpose:** Walks the prospect through the 90-day onboarding arc — Setup (1–30), Activation (31–60), Growth (61–90) — with concrete deliverables per phase. Reinforces that DonorDock includes white-glove migration.

## When to use

- Page 6 of every sales proposal, after the platform overview pages
- Onboarding playbooks given to customers post-sale (use the standalone `Your 90-Day Onboarding Roadmap` template instead for the full 15-page version)

## When NOT to use

- One-pagers — use the timeline compressed pattern instead (Phase 2+)
- Renewal proposals — onboarding doesn't apply

## Slot definitions

| Slot | Type | Required | Notes |
|---|---|---|---|
| `eyebrow` | string | no | Default `Onboarding & Migration`. Orange-tinted pill. |
| `title` | string | yes | First line of heading, e.g., `Switching platforms`. |
| `highlight` | string | yes | Highlighted second line, e.g., `shouldn't slow you down.`. |
| `subtitle` | string | yes | 1-2 sentence framing. |
| `phases` | array of `{label, name, body, closing?, result}` | yes | Exactly 3 phases. |
| `phases[].label` | string | yes | e.g., `Phase 1 · Days 1–30`. Auto-uppercased. |
| `phases[].name` | string | yes | One-word phase name, e.g., `Setup`. |
| `phases[].body` | string | yes | 2-4 sentence description of what happens in this phase. |
| `phases[].closing` | string | no | Optional second paragraph for color. |
| `phases[].result` | string | yes | One-sentence outcome, rendered in the purple-bordered callout. |
| `outcomes` | `{title, items}` | yes | Checklist of "what you'll have at the end of 90 days". |
| `outcomes.title` | string | yes | Heading for the checklist. |
| `outcomes.items` | array of string | yes | 4-8 outcome statements. |
| `support_callout` | `{title, body}` | no | Dark callout at the bottom — typically `Support doesn't stop at day 90.`. |

## Layout guarantees

- 3-column grid for phases — equal width
- Each phase's result callout has a left purple border and lavender background
- Outcomes checklist is 2 columns
- Support callout (if present) is full-width, dark background, cream text

## Don't

- Don't use more than 3 phases — the visual rhythm depends on it
- Don't put pricing or contact info here — those belong in their own blocks
