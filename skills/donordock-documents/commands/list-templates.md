---
description: List every available document template (built-in + team-added) with a one-line description and a path to the preview.
argument-hint:
---

# /list-templates — Show all available templates

You are listing every template the plugin can build.

## Step 1 — Scan templates folder

Walk `tool/templates/` and pick out every subdirectory that contains a `definition.json`.

- Built-in templates live directly under `tool/templates/`
- Team-added templates live under `tool/templates/_team/`

## Step 2 — Surface each

For each template, read its `definition.json` and report:

| Field | Source |
|---|---|
| Name | `definition.json` → `name` |
| Description | `definition.json` → `description` |
| Page count | spine length (filter out optional pages with `default: false`) |
| Preview path | `tool/templates/<name>/preview.html` (if it exists) |

Format as a clean table or list. Note which are built-in vs. team-added.

## Step 3 — Suggest next actions

- "Want to see one? `/preview-template <name>`"
- "Want to build one for a prospect? `/proposal <prospect>` or `/onepager <prospect>`"
- "Need a doc type that's not here? `/new-template`"

## Don't

- Don't describe templates from memory — read the actual `definition.json` files
- Don't include the page count for one-pagers (they're explicitly 1 page)
