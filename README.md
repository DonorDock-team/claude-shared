# DonorDock Claude Shared

Shared files, skills, templates, and assets used by Claude across the DonorDock team. Any team member's Claude can pull from this repo during conversations and skill execution.

## How It Works

- **Public repo** — no auth needed for reads, any Claude session can access files instantly
- **Team members** can edit files directly in GitHub's web UI (click the pencil icon on any file)
- **Version history** is automatic — every change is tracked and reversible

### Base URL for Raw Files

```
https://raw.githubusercontent.com/DonorDock-team/claude-shared/main/
```

Example — fetching the website sitemap from a skill:

```bash
curl -s "https://raw.githubusercontent.com/DonorDock-team/claude-shared/main/sitemaps/website-sitemap.json"
```

---

## Repo Structure

```
├── sitemaps/               ← JSON sitemaps and content indexes for DonorDock properties
│   ├── website-sitemap.json     ← 520+ pages, auto-updated weekly
│   ├── youtube-catalog.json     ← Video index for @donordock + @FundraisingLab, auto-updated weekly
│   ├── helpcenter-sitemap.json  ← 300+ articles with full content, auto-updated weekly
│   ├── helpcenter-summaries-p1..p4.json  ← Paginated help center summaries
│   └── cms-schema.md            ← Webflow CMS collection schemas and IDs
│
├── scripts/                ← Reusable standalone scripts
│   ├── scrape-stonly-helpcenter.py   ← Generic Stonly help center scraper
│   └── scrape-website-sitemap.py    ← Website sitemap scraper (fetches sitemap.xml + page metadata)
│
├── skills/                 ← Skill files (SKILL.md + references)
│   ├── donordock-helpcenter/  ← Answers product questions from help center
│   │   └── SKILL.md
│   ├── ff-article-pipeline/
│   │   ├── SKILL.md
│   │   └── references/
│   │       └── cms-schema.md
│   └── frontend-design/
│       └── SKILL.md
│
├── sales-enablement/       ← Sales team enablement docs (battlecards, objections, product KB)
│   ├── README.md               ← Setup instructions for the Claude Project
│   ├── system-prompt.md        ← System prompt for the Sales Brain Claude Project
│   ├── competitor-battlecards.md  ← Side-by-side positioning vs. 5 competitors
│   ├── objection-handling-playbook.md  ← Common objections with response frameworks
│   ├── product-knowledge-base.md  ← Feature/benefit reference by product area
│   └── maintenance-guide.md    ← How to keep docs current
│
├── assets/                 ← Brand assets (logos, icons, images, fonts)
│   ├── logos/
│   │   ├── donordock-logo-full.svg
│   │   ├── donordock-logo-mark.svg
│   │   └── donordock-logo-white.svg
│   ├── icons/
│   │   └── donordock-icon.svg
│   ├── fonts/
│   │   ├── Silka-Black.otf
│   │   ├── Silka-Bold.otf
│   │   ├── Silka-Medium.otf
│   │   ├── Silka-Regular.otf
│   │   ├── Silka-RegularItalic.otf
│   │   ├── Silka-SemiBold.otf
│   │   └── Silka-SemiBoldItalic.otf
│   └── images/
│       └── .gitkeep
│
├── plugins/               ← Distributable plugin packages (.plugin files)
│   └── donordock-helpcenter.plugin
│
├── templates/              ← Reusable templates for content generation
│   ├── emails/
│   └── webflow/
│
├── reference/              ← Shared reference data (brand, ICP, etc.)
│
└── config/                 ← Shared configuration for skills/plugins
    ├── skill-settings.json
    └── transcript-processing-log.json  ← Tracks which transcripts each task has processed
```

---

## File Index

| Path | Description | Owner | Last Updated |
|------|-------------|-------|--------------|
| `sitemaps/website-sitemap.json` | 520+ DonorDock.com pages with titles, descriptions, and section classification, auto-updated weekly | Rob | 2026-04-15 |
| `sitemaps/youtube-catalog.json` | 47+ videos from @donordock and @FundraisingLab with categories (podcast, training, testimonial, etc.) and people tags, auto-updated weekly | Rob | 2026-04-15 |
| `sitemaps/helpcenter-sitemap.json` | Help center article index (300+ articles with full content), auto-updated weekly | Rob | 2026-03-14 |
| `scripts/scrape-website-sitemap.py` | Website sitemap scraper — fetches sitemap.xml, enriches with page title/description, classifies by section | Rob | 2026-04-15 |
| `scripts/scrape-stonly-helpcenter.py` | Reusable Stonly help center scraper — works for any Stonly-hosted site | Rob | 2026-03-14 |
| `skills/donordock-helpcenter/SKILL.md` | Answers DonorDock product questions using help center sitemap | Rob | 2026-03-14 |
| `skills/ff-article-pipeline/SKILL.md` | Focused Fundraiser article generation pipeline | Rob | 2026-03-17 |
| `skills/ff-article-pipeline/references/cms-schema.md` | Webflow CMS collection schemas, IDs, and tags | Rob | — |
| `skills/frontend-design/SKILL.md` | Frontend design guidelines for distinctive UI work | Rob | — |
| `skills/donordock-video/SKILL.md` | DonorDock motion-graphics video production with Remotion | Rob | 2026-06-04 |
| `skills/remotion-video-graphics/SKILL.md` | Remotion video graphics for DonorDock branded motion content | Rob | 2026-06-04 |
| `sales-enablement/README.md` | Setup instructions for the Sales Brain Claude Project | Rob | 2026-03-19 |
| `sales-enablement/system-prompt.md` | System prompt — paste into Claude Project Instructions | Rob | 2026-03-19 |
| `sales-enablement/competitor-battlecards.md` | Side-by-side positioning vs. Bloomerang, NfG, DonorPerfect, Givebutter, Neon CRM | Rob | 2026-03-19 |
| `sales-enablement/objection-handling-playbook.md` | Top objections with suggested response frameworks | Rob | 2026-03-19 |
| `sales-enablement/product-knowledge-base.md` | Feature/benefit quick-reference organized by product area | Rob | 2026-03-19 |
| `sales-enablement/maintenance-guide.md` | How to keep the enablement docs current (triggers, quarterly checklist, feedback loop) | Rob | 2026-03-19 |
| `assets/logos/` | DonorDock logo SVGs (full, mark, white variants) | Rob | — |
| `assets/icons/` | DonorDock icon SVGs | Rob | — |
| `assets/fonts/` | Silka font family — Black, Bold, Medium, Regular, RegularItalic, SemiBold, SemiBoldItalic (.otf) | Rob | 2026-03-20 |
| `plugins/donordock-helpcenter.plugin` | Packaged help center plugin (skill + scraper + references) | Rob | 2026-03-14 |
| `config/skill-settings.json` | Shared settings referenced by skills at runtime | Rob | — |
| `config/transcript-processing-log.json` | Shared log preventing duplicate transcript processing across scheduled tasks | Rob | 2026-03-17 |

---

## For Team Members

### Reading files (everyone)

No setup needed. When you're chatting with Claude and a skill runs, it automatically fetches what it needs from this repo.

### Editing files

1. Navigate to the file in GitHub
2. Click the **pencil icon** (edit) in the top right
3. Make your changes
4. Add a short description of what you changed in the "Commit changes" box
5. Click **Commit changes**

That's it — the next time any Claude session fetches that file, it gets the updated version.

### Adding new files

1. Navigate to the folder where the file should live
2. Click **Add file** → **Create new file**
3. Name it and add content
4. Commit

### Updating the index

When you add or significantly change a file, update the **File Index** table in this README so the team knows what's available.

---

## For Skill Developers

### Fetching files in a skill

```bash
# Simple fetch
SITEMAP=$(curl -s "https://raw.githubusercontent.com/DonorDock-team/claude-shared/main/sitemaps/website-sitemap.json")

# Fetch and save locally for processing
curl -s "https://raw.githubusercontent.com/DonorDock-team/claude-shared/main/sitemaps/helpcenter-sitemap.json" \
  -o /home/claude/helpcenter-sitemap.json

# Fetch an SVG asset
curl -s "https://raw.githubusercontent.com/DonorDock-team/claude-shared/main/assets/logos/donordock-logo-full.svg" \
  -o /home/claude/logo.svg

# Fetch a font file
curl -s "https://raw.githubusercontent.com/DonorDock-team/claude-shared/main/assets/fonts/Silka-Bold.otf" \
  -o /home/claude/Silka-Bold.otf
```

### Writing back to the repo (requires token)

For skills that need to update files (e.g., refreshing a sitemap):

```bash
# Base64 encode the content
CONTENT=$(base64 -w 0 updated-sitemap.json)

# Get the current file's SHA (required for updates)
SHA=$(curl -s -H "Authorization: token $GITHUB_TOKEN" \
  "https://api.github.com/repos/DonorDock-team/claude-shared/contents/sitemaps/website-sitemap.json" \
  | jq -r '.sha')

# Update the file
curl -X PUT \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Content-Type: application/json" \
  "https://api.github.com/repos/DonorDock-team/claude-shared/contents/sitemaps/website-sitemap.json" \
  -d "{\"message\":\"Auto-update website sitemap\",\"content\":\"$CONTENT\",\"sha\":\"$SHA\"}"
```

Store the token in `config/skill-settings.json` or pass it as a skill parameter.

---

## Conventions

- **Filenames**: lowercase, kebab-case (`website-sitemap.json`, not `Website Sitemap.json`)
- **Format**: Markdown (`.md`) for docs, JSON for structured data, SVG for vector graphics
- **One topic per file**: Easier to find, fetch, and update
- **Summary at top**: Every `.md` file should start with a 1-2 sentence description of what it contains
- **No secrets**: This is a public repo. Never commit API keys, tokens, or passwords. Use `config/skill-settings.json` with placeholder values and inject real values at runtime.
