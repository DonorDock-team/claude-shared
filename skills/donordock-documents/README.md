# donordock-documents

Claude Code plugin for generating on-brand DonorDock sales proposals, one-pagers, and partnership overviews from a locked content-block library.

## What this gives you

Once installed, you can type these slash commands from any Claude Code session:

| Command | What it does |
|---|---|
| `/proposal <prospect>` | Build a full 9-page sales proposal with the Well Summit-style flow |
| `/onepager <prospect>` | Build a single-page summary with before/after + capability grid + pricing strip |
| `/document` | Pick a template if you're not sure which one |
| `/preview-template <name>` | See what a template looks like rendered with sample data |
| `/audit <path>` | Run the brand auditor against a document — catches non-token colors, unauthorized fonts, emoji icons |
| `/new-template [name]` | Sales-rep self-service — compose a new template from existing content blocks |
| `/new-content-block <desc>` | Gated path for marketing/design to add a new layout pattern |
| `/list-templates` | Show every available template (built-in + team-added) |
| `/list-content-blocks` | Open the visual library of all content blocks |

If you just describe what you want in natural language ("make a proposal for The Well Summit"), the fallback skill routes you to the right command.

## Install

```bash
# Symlink the plugin into your Claude Code plugins directory
ln -s "$(pwd)" ~/.claude/plugins/donordock-documents

# Install the Node tooling dependencies
cd tool && npm install
```

The tool requires Node 20+ and uses Handlebars for template compilation. PDF rendering (Puppeteer) is wired in `package.json` but not yet installed — for now, generated documents are HTML files that you print/export to PDF from your browser.

## File layout

```
donordock-documents/
├── plugin.json              # plugin manifest
├── commands/                # 9 slash commands
├── skills/donordock-documents/SKILL.md   # natural-language fallback
├── agents/brand-auditor.md  # specialized subagent for audits
└── tool/
    ├── tokens.css           # design tokens (single source of truth for colors/fonts/spacing)
    ├── base.css             # page setup, print styles, shared utility classes
    ├── content-blocks/      # 17 pixel-locked partials (cover-purple, your-moment, …)
    ├── templates/           # template definitions + sample data
    │   ├── sales-proposal/
    │   ├── one-pager/
    │   └── _team/           # where sales-rep-added templates land
    ├── build.js             # template → HTML, auto-runs the brand auditor
    ├── preview.js           # content-block → preview.html (visual gallery source)
    ├── gallery.js           # generates the visual block library
    ├── audit.js             # brand auditor — tokens / fonts / emoji enforcement
    ├── assets/logo/         # canonical DonorDock SVG logos
    └── tests/               # golden-image regression goldens + audit fixtures
```

## Brand enforcement

Every document produced by this plugin is **automatically audited** for:

- **Colors** — every hex/rgb/rgba/hsl value must be declared in `tool/tokens.css`
- **Fonts** — `font-family` must reference Silka, Quicksand, or standard system fallbacks
- **Emoji** — none, anywhere. Use Lucide SVG icons or colored CSS dots instead.

Emoji violations fail the build. Color and font drift surfaces as warnings.

## Companion skills

| Skill | Owns |
|---|---|
| `donordock-brand-identity` | Voice, tone, positioning, ICP, the platform pillar color mapping |
| `donordock-helpcenter` | Product knowledge for Q&A |
| `donordock-documents` (this plugin) | Document structure, templates, brand auditing |

When generating copy for a document, defer to `donordock-brand-identity` for voice. This plugin handles structure and visual brand.

## Roadmap

| Phase | Status |
|---|---|
| 1. Token foundation | ✅ |
| 2. Content block library (17 blocks) | ✅ |
| 3. First two templates (sales-proposal, one-pager) | ✅ |
| 4. Brand auditor + post-build hook | ✅ |
| 4.5. Puppeteer PDF rendering + golden-image regression | ⏳ |
| 5. Plugin packaging + slash commands | ✅ |
| 6. document-designer + copy-writer subagents | ⏳ |
| 7. Self-service /new-template + gated /new-content-block | partial (commands exist; full agent-driven flow in Phase 6) |
| 8. Validation + rollout to Noah/Toby | ⏳ |

See the full plan at `~/.claude/plans/users-rob-downloads-donordock-preventio-peppy-clock.md`.
