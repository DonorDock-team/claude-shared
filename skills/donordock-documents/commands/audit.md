---
description: Run the DonorDock brand auditor against a file, content block, template, or directory. Catches non-token colors, unauthorized fonts, and emoji icons.
argument-hint: <file-or-directory>
---

# /audit — Run the brand auditor

Argument: `$ARGUMENTS` (path to scan — file, content-block folder, template output, or the whole `content-blocks/` library)

You are running the DonorDock brand auditor against a target and reporting findings.

## Step 1 — Resolve the target

If $ARGUMENTS is given, treat it as the path to audit. Otherwise, ask the user what to scan.

Common targets:
- A specific generated proposal — `~/Documents/DonorDock/Claude/Deliverables/Proposals/Acme.html`
- A single content block — `content-blocks/cover-purple`
- The whole library — `content-blocks`
- A specific template's output — `templates/sales-proposal/preview.html`

If the user gives a relative path, resolve it relative to `~/Documents/DonorDock/Claude/Projects/Document-Templates/donordock-documents/tool/`.

## Step 2 — Run the auditor

```bash
cd ~/Documents/DonorDock/Claude/Projects/Document-Templates/donordock-documents/tool
node audit.js <resolved-path>
```

Or for machine-readable output to inspect findings programmatically:

```bash
node audit.js --json <resolved-path>
```

## Step 3 — Interpret + recommend

The auditor reports three kinds of finding:

- **`emoji` (ERROR)** — hard rule, must be replaced with a Lucide SVG icon or one of the allowed glyphs (★ ✓ → ↗ ✦)
- **`color` (warn)** — a hex/rgb/rgba/hsl value not in `tokens.css`. Three remediations: replace with a `var(--token-name)`, add a new token to `tokens.css` if the color is legitimate brand, or add a pattern to the allowlist in `audit.js` for translucent/dynamic values
- **`font` (warn)** — a `font-family` value outside the approved set. Replace with `var(--font-primary)` or `var(--font-secondary)`

Group the findings by remediation type. For each one, give the specific token or replacement you'd recommend.

## Step 4 — Optionally re-audit

If the user fixes findings, offer to re-run the audit to confirm.

## Don't

- Don't dismiss color warnings without checking — they often surface legitimate brand drift
- Don't add to the allowlist without verifying. The default answer for a recurring color is "tokenize it."
- Don't auto-fix the user's files. Surface the findings and let the human decide.
