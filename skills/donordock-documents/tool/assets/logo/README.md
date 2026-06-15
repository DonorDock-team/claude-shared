# DonorDock Logo Assets

Source: `/Users/rob/Documents/DonorDock/Graphics/Logo Assets/SVG/` (canonical brand library).

These four SVGs are the only logo files content blocks should reference. Don't redraw, recolor, or rasterize. Don't add stroke, shadow, or padding inside the SVG file.

## Files

| File | Use on… | Wordmark fill | Icon fill |
|---|---|---|---|
| `donordock-logo-dark.svg` | Light backgrounds (white, cream, off-white) — header band, footer band, interior pages | `#40454D` (charcoal) | `#0F8EED` (brand blue) |
| `donordock-logo-white.svg` | Purple, navy, or dark backgrounds — cover page, dark callouts, "Support doesn't stop" boxes | `#FFFFFF` | `#FFFFFF` |
| `donordock-logo-purple.svg` | Marketing/social variants where a single-color purple logo reads better | `#8C2CBF` | `#8C2CBF` |
| `donordock-icon.svg` | Compact spots (sidebars, favicons, social-proof rows) where the full wordmark won't fit | n/a | `#0F8EED` |

## Reference sizing

In documents the logo is sized by its bounding box width, not height:
- Cover page header: 180–200px wide
- Interior header band: 130–150px wide
- Footer (if used): 90–110px wide
- Icon-only: 24–32px

Always keep the SVG `viewBox` intact — never crop or replace it with a fixed `width`/`height`.

## Don't

- Don't apply CSS filters (`filter: invert`, `hue-rotate`) to recolor — use the pre-colored variant
- Don't add a CSS `background` behind the logo — the file already accounts for padding
- Don't scale below 90px wide (the wordmark stops being legible)
