# cover-purple

**Purpose:** Page 1 of a proposal or formal document. Establishes the brand voice, names the prospect, previews capabilities, and sets visual tone.

## When to use

- Sales proposals (8-9 page templates)
- Partnership overviews
- Executive summaries
- Customer-facing onboarding playbooks (first page)

## When NOT to use

- One-pagers — they have no cover; use `header-band` instead
- Internal documents not sent to customers
- Any document where the brand statement "Your fundraising, all in one place" isn't accurate framing

## Slot definitions

| Slot | Type | Required | Notes |
|---|---|---|---|
| `prepared_for` | string | yes | Prospect/customer name. Goes into the top-right badge. |
| `headline` | string | yes | First line of the cover headline. Typically a setup phrase ending in a comma. |
| `highlight` | string | yes | Second line — the phrase that gets the cream-chip highlight backdrop. |
| `subtitle` | string | yes | 2-3 sentence summary of what this document is. Stays under 280 chars to keep cover clean. |
| `chips` | array of string | no | Capability pills. Recommend 4-7 chips, each under 20 chars. Skip the array entirely if not needed. |
| `meta.left` | string | yes | Bottom-left meta. Almost always `donordock.com`. |
| `meta.center` | string | yes | Bottom-center meta. Almost always `Month Year` (e.g., `May 2026`). |
| `meta.right` | string | yes | Bottom-right meta. Typically `Prepared by Noah Barnett · nbarnett@donordock.com`. |
| `badge_label` | string | no | Overrides the "Prepared for X" badge. Use for cases like `Evaluation Overview` or `Partnership Proposal`. |

## Layout guarantees

- Full-bleed (8.5" × 11"), purple background — uses `--brand-purple` token
- Logo is fixed to top-left, badge to top-right
- Headline is vertically centered in the flexible middle region (`.cover-hero`)
- Meta band is anchored to the bottom with a translucent top border

## Don't

- Don't pass HTML in any slot — only plain text
- Don't add inline `style=` overrides to the rendered output to "tweak" the layout — open a new content block instead
- Don't use the cream highlight for the entire headline. The pattern is `[setup line][highlight on second line]` — never both lines highlighted

## Examples

See `sample-data.json` for the canonical Well Summit example.
