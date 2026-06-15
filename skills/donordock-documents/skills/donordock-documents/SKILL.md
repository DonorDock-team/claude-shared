---
name: donordock-documents
description: DonorDock document generation system. Use this skill whenever the user wants to create a sales proposal, one-pager, partner overview, executive summary, or any branded PDF/HTML document for a DonorDock prospect or customer. Also trigger when the user asks to audit a finished document against brand standards, list available templates, browse the content block library, or compose a new template. Even without explicit slash commands, requests like "make a proposal for X", "build a one-pager for Y", "check this document for brand drift", "what templates do we have" — all route here. Works alongside donordock-brand-identity (voice/colors/positioning).
---

# DonorDock Documents

You are the entry point for DonorDock's document generation system. When the user mentions creating, reviewing, or composing branded DonorDock documents — proposals, one-pagers, partner overviews, executive summaries — and they haven't used a slash command directly, route them to the right one.

## Routing map

| User says… | Route to |
|---|---|
| "Create / build / make a proposal for X" | `/proposal X` |
| "Need a quick summary / one-pager / sheet for X" | `/onepager X` |
| "What templates do we have?" | `/list-templates` |
| "What content blocks are in the library?" | `/list-content-blocks` |
| "Show me what the proposal looks like" | `/preview-template sales-proposal` |
| "Audit / check / review this document for brand" | `/audit <path>` |
| "I want to make a new template for [doc type]" | `/new-template [name]` |
| "I want to design a new content block" | `/new-content-block <description>` |
| Generic "I want to create a document" without a clear type | `/document` |

## What this skill owns

- Document templates (`sales-proposal`, `one-pager`, plus team-added)
- The content block library (17 pixel-locked partials at `tool/content-blocks/`)
- The brand auditor (`tool/audit.js` — token, font, emoji enforcement)
- The build pipeline (`tool/build.js` — assembles documents from templates + data)

## What this skill does NOT own

- **Voice, tone, copy** — that's the `donordock-brand-identity` skill. When generating copy for slot text, defer to brand-identity for voice.
- **Product knowledge for help-center-style answers** — that's `donordock-helpcenter`.
- **SEO/AEO/GEO strategy** — that's `donordock-seo-strategist`.

## Visual conventions enforced by this skill

These are non-negotiable — the brand auditor catches violations:

- **Colors**: only values declared in `tool/tokens.css`. Hard-coded hex/rgb is a violation.
- **Fonts**: only Silka (primary) or Quicksand (Otto sub-brand) plus standard fallbacks.
- **Icons**: only Lucide SVGs or colored CSS dots. NO emoji glyphs anywhere.
- **Cards**: shadow-led elevation (`var(--shadow-md)`), thin `rgba(0,0,0,0.06)` outline, no left-side color bars.
- **Highlight pattern in headings**: brand-purple-light chip with brand-purple text (`.highlight-purple`), or cream chip with purple text on dark backgrounds (`.highlight-on-purple`).

## Platform pillar color mapping (from `donordock-brand-identity`)

When picking accents for capability blocks (`platform-overview-quad`, `donor-intelligence-quad`, `feature-checklist-grid`):

| Pillar | Accent |
|---|---|
| CRM, Donor Management, Contact data, Reporting | **blue** |
| Outreach, Email, Texting, Automations (comm) | **green** |
| Online Giving, Payments, DAFPay, Receipts | **yellow** |
| Project Management, Action Board, Tasks, Asks Board | **orange** |
| Otto AI, Smart Nudges, AI features | **purple** |

## File locations

- Tool: `~/Documents/DonorDock/Claude/Projects/Document-Templates/donordock-documents/tool/`
- Output: `~/Documents/DonorDock/Claude/Deliverables/Proposals/` (create folder if missing)
- Gallery: `tool/gallery/index.html` (open in browser to browse content blocks)
