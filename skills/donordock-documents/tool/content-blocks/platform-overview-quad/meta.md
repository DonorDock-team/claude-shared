# platform-overview-quad

**Purpose:** The "everything you get" page. A 4-quadrant grid covering the four pillars of the DonorDock platform: CRM / Outreach / Online Giving / Project Management. Each quadrant is sectional-color-coded.

## When to use

- Page 4 of every sales proposal — the foundational "platform-at-a-glance" page
- Partnership overviews where the buyer wants the full feature surface

## When NOT to use

- One-pagers — use `feature-checklist-grid` instead (denser, single-column)
- Renewal proposals — the customer knows the platform
- Otto-specific docs

## Slot definitions

| Slot | Type | Required | Notes |
|---|---|---|---|
| `eyebrow` | string | no | Default `Platform Overview`. |
| `title` | string | yes | First line of the heading, e.g., `Everything you need,`. |
| `highlight` | string | yes | Highlighted second line, e.g., `built to work together.`. Uses `.highlight-purple`. |
| `subtitle` | string | yes | 1-2 sentence platform framing. |
| `quadrants` | array of `{title, accent, items}` | yes | Exactly 4 quadrants. |
| `quadrants[].title` | string | yes | Quadrant name, e.g., `CRM & Donor Management`. |
| `quadrants[].accent` | `"blue" \| "green" \| "orange" \| "purple"` | yes | Sectional accent. Recommended order: blue, green, orange, purple (matches reference docs). |
| `quadrants[].items` | array of string | yes | 5-7 capability bullets per quadrant. |
| `footnote` | `{title, body}` | no | Single-line callout at the bottom, e.g., `One plan. All features.` |

## Layout guarantees

- Grid is exactly 2×2 — exactly 4 quadrants
- Each quadrant has a colored left border matching its accent
- Quadrant titles inherit the accent color
- Arrow bullets (`→`) — never disc or check bullets

## Don't

- Don't change the order of quadrants without intent — the eye sweeps L→R, top→bottom
- Don't use more than 7 items per quadrant — the card overflows
- Don't include pricing in this block — `pricing-card-purple` owns that
