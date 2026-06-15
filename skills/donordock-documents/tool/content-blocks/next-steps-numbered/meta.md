# next-steps-numbered

**Purpose:** Closing page of a proposal. 3-step numbered next-action list with a dark contact card at the bottom containing the rep's identity and a CTA button.

## When to use

- Final page (page 9) of every sales proposal
- Partnership overviews where there's a clear post-doc action

## When NOT to use

- One-pagers — the contact card is sufficient on its own
- Internal documents

## Slot definitions

| Slot | Type | Required | Notes |
|---|---|---|---|
| `eyebrow` | string | no | Default `Next Steps`. |
| `title` | string | yes | First line of heading, e.g., `Ready when`. |
| `highlight` | string | yes | Highlighted second line, e.g., `you are.`. |
| `subtitle` | string | yes | 1-2 sentence framing of what the prospect should do next. |
| `steps` | array of `{heading, body}` | yes | Exactly 3 numbered steps. |
| `steps[].heading` | string | yes | Imperative phrase, e.g., `Share this with your team`. |
| `steps[].body` | string | yes | 1-3 sentences explaining the step. |
| `contact.name` | string | yes | Rep's full name. |
| `contact.role` | string | yes | Rep's title at DonorDock. |
| `contact.email` | string | yes | Rep's email. |
| `contact.website` | string | no | Optional. Default `donordock.com`. |
| `contact.cta_message` | string | no | Small line above the CTA, e.g., `Questions? We're easy to reach.` |
| `contact.cta_label` | string | yes | CTA button text, e.g., `Schedule a Call`. |

## Layout guarantees

- Steps use a purple circular number badge
- Each step row has a thin bottom border (except last)
- Contact card uses `--bg-dark` background with cream/inverse text
- CTA button is a purple pill on the right

## Don't

- Don't use more than 3 steps — the visual rhythm fights it
- Don't include phone numbers or office addresses — keep contact light
- Don't recolor the CTA button — it's the brand-purple call to action everywhere
