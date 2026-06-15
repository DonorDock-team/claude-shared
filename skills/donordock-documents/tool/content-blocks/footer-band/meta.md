# footer-band

**Purpose:** Bottom-of-page meta line. Identifies the document context and provides the donordock.com URL or a page number.

## When to use

- Bottom of every interior page of a multi-page document
- One-pagers (sits below the main content)

## When NOT to use

- Cover pages — `cover-purple` has its own meta band at the bottom

## Slot definitions

| Slot | Type | Required | Notes |
|---|---|---|---|
| `doc_label` | string | yes | Document identifier, typically `"DonorDock · Custom Proposal for X · Month Year"`. Keep under 80 chars. |
| `right_label` | string | no | Default `donordock.com`. Override for things like `Page 4 of 15` or a custom URL. |

## Layout guarantees

- Top border in `--border-light`
- Text in `--text-muted` (small, subtle — doesn't compete with page content)
- Flex row, left + right aligned

## Don't

- Don't use this on cover pages — `cover-purple` provides its own meta band
- Don't add icons or branded marks here — the footer is intentionally minimal
