# header-band

**Purpose:** Identifies the document and customer at the top of every interior page. DonorDock logo on the left, customer name in uppercase eyebrow style on the right, thin underline.

## When to use

- Top of every interior page in a multi-page document (proposals, executive summaries, partnership overviews, onboarding playbooks)
- Compact identification on one-pagers (in place of a full cover)

## When NOT to use

- Page 1 cover — use `cover-purple` instead, which has its own logo + badge layout
- Dark callout sections inside a page — those handle their own framing
- Inside Otto-branded sections — they use a different header treatment (Phase 2+)

## Slot definitions

| Slot | Type | Required | Notes |
|---|---|---|---|
| `prepared_for` | string | yes | Customer name, will be uppercased via CSS. Keep under 40 chars. |
| `variant` | "dark" \| "light" | no | Default `dark` (charcoal logo + tertiary text on light bg). Use `light` only inside a dark-themed page. |

## Layout guarantees

- Logo height fixed at 26px
- Label aligned right, uppercased, letter-spaced 0.08em
- Thin 1px underline using `--border-light`

## Don't

- Don't pass already-uppercased text in `prepared_for` — the CSS handles that via `text-transform: uppercase`
- Don't add a date or page number here — that belongs in `footer-band`
