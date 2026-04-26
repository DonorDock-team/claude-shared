---
name: ff-article-pipeline
description: "disable-model-invocation: true ONLY use when explicitly invoked via slash command or when the user literally says 'run ff-article-pipeline' or 'run the article pipeline skill'. Do NOT auto-trigger on general blog, article, writing, or content requests. This skill runs an automated end-to-end pipeline that researches, writes, illustrates, and publishes two SEO/AEO articles to DonorDock's Webflow CMS from a transcript."
---

# Focused Fundraiser Article Pipeline

This skill runs a complete pipeline that takes a transcript (or topic) and produces two polished, SEO-optimized blog articles with custom hero images, then publishes them as drafts in DonorDock's Webflow CMS.

## When to Use

- User provides a transcript, podcast recording notes, or topic and wants blog articles
- User says "write DonorDock articles", "FF articles", "blog pipeline", "transcript to articles"
- User wants to create thought-leadership content for The Focused Fundraiser blog

## Required Context

- Apply the `donordock-brand-identity` skill for voice, ICP, visual, and positioning guidance
- Apply the `donordock-seo-strategist` skill at strategic checkpoints: angle validation (Step 1), pillar/keyword/AEO assignment during writing (Step 2 & 5), pre-publish validation (Step 7)
- Both skills read shared source-of-truth from `DonorDock-team/claude-shared/seo-brain/` — never duplicate their content here; reference and load
- Treat each post as a standalone article even when source material is a shared transcript
- All articles target experienced but stretched nonprofit development teams (3+ FTE) at growing/mid-sized nonprofits ($1M-$10M revenue), per the locked ICP in brand-positioning.md. NOT solo operators, NOT churches, NOT first-CRM beginners.

## Skill Integration Map

This pipeline orchestrates two DonorDock skills + Webflow + GitHub MCPs.

| Step | brand-identity provides | seo-strategist provides |
|---|---|---|
| 1 (Angle discovery) | ICP language check on each candidate angle | Pillar fit + keyword opportunity from GSC + AEO question coverage from aeo-questions.md |
| 2 (Write Article 1) | Voice + tone + vocabulary + banned-words check | Content-standards structural rules (TL;DR, question H2s, FAQ count, internal linking density) |
| 3 (Metadata 1) | Brand-positioning.md banned terms scan | Pillar tag assignment, keyword cluster cross-reference, canonical URL |
| 4 (Image 1) | Locked visual system (cream bg, Silka type, DonorDock icon, brand palette) — see `references/visual-identity.md` | (no SEO input) |
| 5 (Write Article 2) | Voice + differentiation check | DIFFERENT pillar/keyword/AEO from Article 1 |
| 6 (Metadata 2) | Same as Step 3 | Same as Step 3 |
| 7 (FAQ + Publish) | brand-critic subagent (voice review) | content-validator subagent (structure, CMS field completeness, FAQ coverage) + AEO-question sourcing for FAQ generation — run in parallel with brand-critic + researcher |

**Subagents to spawn:**
- `donordock-brand-identity` → `brand-critic` (voice), `researcher` (facts), `seo-aeo-strategist` (LIGHT — quick voice/SEO compliance only; defer deep SEO work to the strategist skill)
- `donordock-seo-strategist` → `strategy-advisor` (Step 1 angle validation), `content-validator` (Step 7 pre-publish), `schema-drafter` (only if article is HowTo/Dataset type — template handles standard BlogPosting + FAQPage automatically)

If neither skill is available in the environment, halt the pipeline and surface a warning. Do not silently produce articles without strategic + brand validation.

## Transcript Processing Log

A local JSON log at `/Users/rob/Documents/DonorDock/Claude/Projects/The Focused Fundraiser/transcript-processing-log.json` tracks which transcripts have been processed by each scheduled task. This prevents any transcript from being used twice by the same task.

**When running as a scheduled task (not manual invocation):**
1. At the start of the pipeline, read the log file using the `Read` tool at the path above
2. Skip any transcript that already has a non-null `ff-article-pipeline` value in the log
3. After successfully publishing both article drafts, update the log by adding or updating the transcript's entry with the `ff-article-pipeline` key set to the current ISO timestamp
4. Write the updated log back to the same file path using the `Write` tool

**When running manually:** The log check is optional. If the user explicitly provides a transcript, process it regardless of log status. Still update the log afterward so other tasks know it was used.

**Log entry format:**
```json
{
  "filename": "episode-42.txt",
  "folder": "Transcripts",
  "ff-article-pipeline": "2026-03-17T12:00:00Z",
  "podcast-metadata-creator": null,
  "weekly-ff-email": null,
  "ff-social-posts": null
}
```

## Article Differentiation Strategy (CRITICAL)

The two articles produced from each transcript MUST be substantially different from each other. They should feel like they were written by different authors for different sections of a magazine. A reader who sees both should never think "these are basically the same article."

**The two articles must differ across ALL of these dimensions:**

| Dimension | Article 1 | Article 2 |
|-----------|-----------|-----------|
| **Content type** | Strategic/analytical (frameworks, models, trend analysis, research-backed arguments) | Tactical/actionable (step-by-step guides, templates, checklists, how-to walkthroughs) |
| **Reader mindset** | "I need to understand this better" (educate, persuade, reframe) | "I need to do this now" (enable, equip, accelerate) |
| **Primary keyword family** | Broader, higher-volume keyword (e.g., "donor retention strategies") | Specific, long-tail keyword (e.g., "how to write a lapsed donor re-engagement email") |
| **Structure** | Essay-style with research, data, expert perspective, and narrative flow | Numbered steps, actionable sections, examples, templates, or before/after comparisons |
| **CTA angle** | Thought leadership (subscribe, share, explore DonorDock's approach) | Utility (try this template, use this checklist, start with DonorDock) |
| **Tone** | Reflective, analytical, "here's what the data says" | Direct, practical, "here's exactly how to do it" |

**What counts as "too similar" (avoid ALL of these):**
- Same primary keyword or search intent
- Same H2 structure or section topics
- Overlapping advice (if Article 1 says "segment your donors by giving level," Article 2 should NOT repeat that same advice)
- Same examples or case study scenarios
- Same DonorDock features highlighted

**Differentiation checkpoint:** Before writing Article 2, explicitly list 3-5 ways it differs from Article 1 across the dimensions above. If you can't identify clear differences, rethink the angle.

## Shared Resources (GitHub)

The CMS schema and website sitemap live in the `DonorDock-team/claude-shared` GitHub repo under the `sitemaps/` folder. These are the single source of truth and should always be fetched fresh at the start of every pipeline run so you're working with the latest data (tags, categories, URLs, etc.) rather than stale bundled copies.

At the beginning of Step 1, use the GitHub `get_file_contents` tool to fetch all three files:

| File | Repo Path | What it contains |
|------|-----------|------------------|
| CMS Schema | `sitemaps/cms-schema.md` | Collection IDs, field schema, tag/category IDs, author IDs, CMS item creation template |
| Website Sitemap | `sitemaps/website-sitemap.json` | 520+ donordock.com pages with URLs, titles, descriptions, sections -- use for internal linking |
| YouTube Catalog | `sitemaps/youtube-catalog.json` | 120+ long-form videos from @donordock and @FundraisingLab with categories and people tags -- use for video links in articles |

```
Owner: DonorDock-team
Repo: claude-shared
Paths:
  - sitemaps/cms-schema.md
  - sitemaps/website-sitemap.json
  - sitemaps/youtube-catalog.json
```

These files provide:
- **Tag and category IDs** for CMS publishing (from cms-schema.md)
- **Valid internal link targets** for articles (from the website sitemap)
- **Content audit data** to avoid duplicating existing topics (cross-reference with CMS article list)
- **YouTube video links** for embedding relevant videos in articles (from the YouTube catalog)

---

## Pipeline Overview

The pipeline has 7 steps that run end-to-end without approval gates:

1. **Research & Angle Discovery** -- Analyze input, audit existing CMS content for gaps, propose two deliberately different angles (pillar + keyword + AEO assigned via `strategy-advisor`)
2. **Write Article 1** -- Draft a strategic/analytical SEO/AEO article
3. **Generate Metadata 1** -- SEO title, meta description, slug, read time, tags, pillar ref, seo-keywords, canonical URL
4. **Image Creation 1** -- Generate hero via Nano Banana using the locked DonorDock style (cream bg, Silka type, topic-tailored illustration), overlay DonorDock icon, compress to WebP
5. **Write Article 2** -- Draft a tactical/actionable article (verify differentiation first)
6. **Generate Metadata 2** -- Same metadata process for article 2 (different pillar or different keyword cluster)
7. **Image Creation 2 + FAQ Generation + Publish Both** -- Generate second hero image, create/reuse 4–6 Article FAQs per article, link them via multi-reference, run parallel validator agents, create both Webflow drafts with all CMS fields populated, update transcript log

---

## Step 1: Research & Angle Discovery

### Inputs
- Transcript file path (if provided) -- read it in full
- Topic/title (if provided instead of transcript)

### Process

1. **Fetch shared resources from GitHub** -- Before anything else, use the GitHub `get_file_contents` tool (owner: `DonorDock-team`, repo: `claude-shared`) to fetch these files in parallel:
   - `sitemaps/cms-schema.md` -- for CMS field schema, tag/category IDs, author IDs, and the item creation template
   - `sitemaps/website-sitemap.json` -- for valid donordock.com page URLs to use as internal links
   - `sitemaps/youtube-catalog.json` -- to find relevant DonorDock or Focused Fundraiser videos to link in articles
   - `/Users/rob/Documents/DonorDock/Claude/Projects/The Focused Fundraiser/transcript-processing-log.json` -- to check which transcripts have already been processed (scheduled task runs only; read using the `Read` tool)

2. **Read the transcript or topic** thoroughly. Extract every distinct theme, insight, quote, and actionable takeaway.

3. **Audit existing DonorDock articles** for content gaps:
   - Use the Webflow `data_cms_tool` to list recent articles in collection `6532889f2379aa018d3520b7` (fetch 30-50 items with `sortBy: lastPublished, sortOrder: desc`)
   - Compare themes from the transcript against existing article titles and previews
   - Cross-reference against the website sitemap to understand what content already exists across DonorDock properties
   - Identify 2 angles that fill genuine gaps -- topics the blog hasn't covered or hasn't covered recently

4. **Apply the Differentiation Strategy** -- The two angles MUST map to the Article Differentiation Strategy table above:
   - **Angle 1 (Strategic):** A broader, analytical take. Think "why this matters" or "what the research says." Target a higher-volume keyword.
   - **Angle 2 (Tactical):** A specific, actionable take. Think "how to do this" or "step-by-step guide." Target a long-tail keyword.
   - Verify the two angles target different search intents and would attract different click-throughs in search results
   - If both angles feel similar, discard one and find a genuinely different angle from the transcript

5. **Web research** to gather 3-5 supporting data points per angle from trusted nonprofit sources:
   - Acceptable: FEP, Giving USA, AFP, Nonprofit Quarterly, Chronicle of Philanthropy, NTEN, BoardSource, National Council of Nonprofits, and others like them
   - Never use competitor CRM sources (Bloomerang, Little Green Light, Neon, Kindful, Networkforgood, donor perfect, etc.) as citation sources
   - Never fabricate URLs or statistics

6. **Validate both angles via the seo-strategist skill's `strategy-advisor` subagent.** For each candidate angle, spawn the agent. It returns:
   - Pillar fit (must map to one of the 7 locked pillars in `seo-brain/strategy/pillars.md`)
   - Keyword opportunity (live GSC data check via `mcp__gsc__advanced_search_analytics`)
   - AEO question coverage from `seo-brain/strategy/aeo-questions.md`
   - Recommendation: WRITE / REFRESH EXISTING / SKIP / ESCALATE TO ROB
   - Pillar URL the article should link UP to + 2-3 sibling articles for lateral linking
   
   **Decision rules:**
   - Both angles return WRITE with DIFFERENT pillars → proceed (best case: maximum strategic surface)
   - Both angles return WRITE with same pillar but different keyword clusters → proceed
   - One returns REFRESH EXISTING → discuss with user; consider refreshing existing article instead of writing new
   - Either returns SKIP → discard angle, find new one from transcript
   - Either returns ESCALATE TO ROB → pause pipeline, surface to user
   
   **Never skip this step.** Off-pillar articles dilute strategic surface and waste publishing slots.

7. **Output**: Present both article angles with:
   - Working title
   - Content type label (Strategic/Analytical or Tactical/Actionable)
   - Target search query (what someone would Google to find this)
   - 2-3 sentence summary of the angle
   - Key supporting data points with sources
   - How this angle differs from the other one (1 sentence)
   - **Pillar assignment** (one of 7 from pillars.md) + **pillar page URL** the article links to
   - **Primary keyword** (from keyword-universe.md) with GSC data (current position + monthly impressions)
   - **AEO questions** from aeo-questions.md this article will answer in its FAQ section (3-5 questions)
   - **Sibling articles** for lateral linking (2-3 from same pillar cluster)

Then proceed directly to writing.

---

## Step 2: Write Article 1 (Strategic/Analytical)

### Article Requirements

- **Length**: 1,600-2,400 words
- **Content type**: Strategic, analytical, research-backed. This article should make the reader think differently about a topic.
- **Structure**: H1 title -> H2 sections -> H3 subsections where needed. Use essay-style flow with data, expert perspective, and narrative.
- **Voice**: Second person ("you/your") throughout. Warm, practical, direct. No jargon walls. Write like a smart colleague who respects the reader's time.
- **Format constraints**:
  - No tables (Webflow rich text handles them poorly)
  - No em dashes -- use commas, periods, or parentheses instead
  - Short paragraphs (2-4 sentences max)
  - Use scannable lists where they genuinely help
  - Bold key phrases sparingly for scannability

### SEO/AEO Structure (per seo-strategist content-standards.md)

- H1 contains the primary keyword identified in Step 1
- **TL;DR block** immediately after H1 (40-word direct-answer paragraph in `<blockquote>` or styled `<p>`) — answer the headline question directly. Critical for AEO featured-snippet capture.
- Include the target query verbatim once in the first 150 words
- Use **question-format H2s** drawn from the AEO questions identified in Step 1 — they are designed for featured snippet + People Also Ask + AI engine extraction
- Include a "quick answer" paragraph near the top (2-3 sentences that directly answer the target query)
- Naturally weave in 2-3 related long-tail keywords from the pillar's keyword cluster
- **Required FAQ section** at the bottom with 3-5 of the AEO questions identified in Step 1, each answered in 40-60 words (paragraph snippet length)
- **Required pillar uplink** — at least one contextual body link to the pillar page assigned in Step 1
- **Required lateral links** — at least 2-3 contextual body links to sibling articles in the same pillar cluster

### Brand-positioning compliance (per seo-strategist brand-positioning.md)

Before submitting metadata + body:
- Confirm no prohibited terms: "small nonprofit," "first CRM," "solo ED," "tiny nonprofit," "one-person shop," "church" (as DonorDock target audience), "tithing," "no platform fees," "free processing"
- Confirm "Action Board" is two words (not "ActionBoard")
- Confirm pricing references say "1% platform fee on online donations" (never "no platform fees" or "free")
- Confirm Smart Stewardship framing where the topic touches stewardship, retention, or donor relationships
- Confirm upmarket language: "growing nonprofits" / "mid-sized nonprofits" / "development teams" — NEVER "small nonprofits" or "first CRM"

### Internal Linking

- Include 2-4 validated internal links to existing DonorDock pages
- Only link to URLs confirmed to exist in the website sitemap (`sitemaps/website-sitemap.json`) or the CMS article list fetched via Webflow
- Website sitemap links work well for linking to product pages, pricing, or feature overview pages
- When a YouTube video is directly relevant to the article topic, include it as a contextual link (e.g., "Watch our quick guide to [topic]") using the URL from `sitemaps/youtube-catalog.json`. The catalog contains long-form videos only (shorts are excluded).
- Never fabricate or guess a DonorDock URL
- Use descriptive anchor text, not "click here" or "learn more"

### DonorDock Mentions

- Mention DonorDock 2-4 times naturally within the article
- On first mention, reference a specific feature by name (e.g., "DonorDock's built-in task management", "DonorDock's donor timeline")
- Keep mentions organic -- the article should be valuable even without DonorDock references
- Never make the article feel like a product pitch

### Output Format

Write the article body in clean HTML suitable for Webflow rich text.

**CRITICAL -- Webflow Rich Text API Formatting Rules:**

Webflow's CMS API will **silently strip HTML elements** (especially lists) that contain whitespace or newlines between tags. The entire article HTML must be submitted as a **single continuous string with zero newlines or extra whitespace between tags**. This is the #1 cause of lists and other elements disappearing after publish.

**Required format (all inline, no `\n` between tags):**
```
<p>Here is a list:</p><ul><li>First item</li><li>Second item</li><li>Third item</li></ul><p>Next paragraph.</p>
```

**Broken format (newlines between tags -- Webflow WILL strip the list):**
```
<ul>
<li>First item</li>
<li>Second item</li>
</ul>
```

**Allowed tags:**
- `<h2>`, `<h3>` for headings (no `<h1>` -- that's the CMS title field)
- `<p>` for paragraphs
- `<ul><li>` or `<ol><li>` for lists -- must be inline with no newlines between tags
- `<a href="...">` for links
- `<strong>` for bold emphasis (use sparingly inside `<li>` tags)
- `<blockquote>` for pull quotes

**Forbidden:**
- No inline styles, no classes, no divs
- No newlines (`\n`) or extra whitespace between any HTML tags in the final output string
- No `<br>` tags (use separate `<p>` tags instead)
- No `<table>` elements (Webflow rich text renders them poorly)

**Implementation note:** When passing the HTML string to the `blog-post-summary` field in the Webflow CMS API call, the entire HTML body must be a single unbroken string value. Do NOT use multiline strings, template literals, or any format that introduces `\n` characters between HTML tags. Build the string as one continuous line of HTML. This applies to both `create_collection_items` and `update_collection_items` calls.

---

## Step 3: Generate Metadata (Article 1)

Generate these fields from the completed article:

| Field | Spec |
|-------|------|
| **SEO Title** | Under 60 characters, includes primary keyword |
| **Meta Description** | Under 160 characters, compelling and includes keyword |
| **Slug** | Kebab-case, concise, keyword-rich (e.g., `nonprofit-crm-migration-checklist`) |
| **Reading Time** | Calculate at ~250 WPM, output just the number (e.g., `7`) |
| **Blog Post Preview** | 1-2 sentence excerpt for the article card (under 200 chars) |
| **Tags** | 2-4 tag IDs from the tags list in the CMS schema (fetched from GitHub in Step 1) |
| **Categories** | 1-2 category IDs from the categories list in the CMS schema (fetched from GitHub in Step 1) |
| **Author** | `6532889f2379aa018d352707` (Rob Burke) unless specified otherwise |
| **Pillar** (required) | ID of ONE of the 7 locked content pillars (from Step 1 `strategy-advisor` output). Single reference, not multi. Binds to BlogPosting `articleSection` + `isPartOf` schema properties. See "Pillar ID Reference" below. |
| **SEO Keywords** (required) | 3–10 comma-separated keywords drawn from the pillar's keyword cluster in `seo-brain/strategy/keyword-universe.md`. Binds to BlogPosting `keywords` schema property. Example: `best nonprofit CRM, nonprofit CRM comparison, donor management software, …` |
| **Canonical URL** (required) | Full `https://www.donordock.com/articles/[slug]` URL. (Note: `/blog/[slug]` 301-redirects to `/articles/[slug]` — always use `/articles/` for canonical so it points at the final destination.) Binds to BlogPosting `mainEntityOfPage.@id` and `@id` (with `#article` fragment). |

---

## Step 4: Hero Image Creation (Article 1)

Every DonorDock blog hero uses a **locked visual system**. The goal: consistent brand look across all articles while still tailoring the scene to the article topic for high click-through. Never deviate from this spec — deviation breaks the series feel.

### Locked style system

| Element | Spec |
|---|---|
| Canvas | 1920×1080, 16:9, WebP output |
| Background | DonorDock Cream `#FFFCF5` with optional very soft pastel gradient overlay (mint, butter-yellow, or dusty lavender at 10–15% opacity) — never pure white, never dark |
| Illustration style | Modern flat vector with soft 3D shading. Rounded friendly forms. Never photorealism, never pure flat cartoon, never 3D render |
| Palette (locked) | Illustration accent colors pulled ONLY from DonorDock brand: Navy `#1F3252`, DD Purple `#8C2CBF`, DD Blue, DD Light Blue, soft coral/warm orange accent. No neon. No pure black or pure white inside the illustration |
| Typography (rendered in illustration) | Title in **Silka Bold** (fallback: a close geometric sans). Subtitle in **Silka Medium**, ~45% title size. Color: dark charcoal `#1a1f36`. Never pure black. |
| Title placement | Left-aligned, within the left 40% of canvas. Vertically centered in that region. NEVER overlap the illustration focal point. |
| Illustration placement | Right 55–60% of canvas |
| Logo safe zone | Keep bottom-right ~200×200 region clear of illustration detail — the DonorDock icon is composited there in post-processing |
| Characters (when used) | Diverse, casual-professional, mid-action (typing, talking, gesturing). Waist-up or mid-distance. 1–5 characters max. No close-up faces. |
| Props | Laptops, charts/dashboards, notebooks, arrows, plants, coffee cups — always relevant to the topic |
| Whitespace | Generous and airy — not packed edge-to-edge |

Cross-reference `donordock-brand-identity/references/visual-identity.md` for the full brand visual rules and any palette hex codes.

### Build the Nano Banana prompt

Use this exact scaffold. Only fill in `[TITLE]`, `[SUBTITLE]`, and `[SCENE]`. Keep every other line verbatim — the locked tokens keep the series consistent.

```
Wide banner hero image, 1920x1080, for a DonorDock nonprofit fundraising article.

STYLE (LOCKED — do not deviate):
- Background: soft cream color #FFFCF5, generous whitespace
- Modern flat vector illustration with soft 3D shading, rounded friendly forms
- Illustration accent palette: navy #1F3252, DD purple #8C2CBF, DD blue, light blue, soft coral. No neon, no pure black, no pure white inside the illustration
- Characters (if present): diverse, casual-professional, mid-action, waist-up, friendly expressions, no close-up faces
- Props relevant to the topic: laptops, charts, dashboards, notebooks, arrows, plants
- Do NOT use stock-photo realism or 3D render aesthetic

LAYOUT (LOCKED):
- Left 40% of canvas: calm background area with title text rendered clean and readable
- Title text (render exactly, crisp Silka-style bold sans-serif, dark charcoal #1a1f36, left-aligned): "[TITLE]"
- Subtitle below title in lighter weight, ~45% title size, same charcoal color: "[SUBTITLE]"
- Right 60% of canvas: topic illustration (below)
- Bottom-right 200x200 area: leave clear, no illustration detail — a logo is composited there in post
- Optional warm accent underline (soft coral or yellow) behind 1–2 key words of the title for visual punch

TOPIC ILLUSTRATION (right 60%):
[SCENE — 1–3 sentence description tailored to the article topic. Example for a CRM article: "Two diverse fundraisers collaborating at a laptop with a CRM dashboard visible on screen, growth charts floating behind them, a small office plant in the foreground."]

NEGATIVE PROMPT (do not include):
- No DonorDock logo, no watermark, no "DonorDock" text anywhere in the illustration
- No garbled or illegible text
- No dark backgrounds
- No more than 5 characters
- No close-up faces
```

### Generate the image

Call `nanobanana_generate_image`:
- **model**: `nanobanana2`
- **aspect_ratio**: `16:9`
- **image_size**: `2K`
- **output_dir**: current session's working directory

### Visual QA gate (required)

Before moving on, verify the generated image:

1. Background is clearly the cream color (not white, not grey)
2. Title text rendered cleanly and spells correctly — no garbled characters
3. Subtitle rendered cleanly
4. Bottom-right corner is empty and ready for logo overlay
5. No unwanted logos/watermarks appeared
6. No close-up faces or more than 5 characters
7. Illustration style feels consistent with prior DonorDock hero images

If any check fails: regenerate with a slightly reworded prompt. Tightening the title in quotes and re-asserting "crisp legible sans-serif" usually fixes text issues. Maximum 2 regeneration attempts before falling back to manual handoff.

### Overlay the DonorDock icon (post-processing)

The DonorDock icon (not the full wordmark logo) is composited onto the bottom-right corner of the finished illustration:

```bash
# Download icon once per session
ICON_PATH="[WORKING_DIR]/donordock-icon.png"
curl -sSL "https://raw.githubusercontent.com/DonorDock-team/claude-shared/main/assets/logos-DonorDock/logo-icon-forcircle.png" -o "$ICON_PATH"

# Composite icon onto generated hero (bottom-right, 140x140, 60px margin)
python3 << 'PYEOF'
from PIL import Image
base = Image.open("[GEN_IMAGE_PATH]").convert("RGBA")
icon = Image.open("[ICON_PATH]").convert("RGBA")
icon = icon.resize((140, 140), Image.LANCZOS)
pos = (base.width - 140 - 60, base.height - 140 - 60)
base.paste(icon, pos, icon)
base.convert("RGB").save("[COMPOSITED_PATH]", "PNG")
PYEOF
```

See `donordock-brand-identity/SKILL.md` lines 199–206 for all DonorDock logo/icon asset URLs. Always use the **icon** (not the horizontal wordmark) for this overlay.

### Compress to WebP

```bash
# Install cwebp if needed
which cwebp || (apt-get update -qq && apt-get install -y -qq webp)

# Compress to WebP, quality 80, 1920x1080, target under 200KB
cwebp -q 80 -resize 1920 1080 "[COMPOSITED_PATH]" -o "[WORKING_DIR]/article-1-hero.webp"

FILE_SIZE=$(stat -f%z "[WORKING_DIR]/article-1-hero.webp" 2>/dev/null || stat -c%s "[WORKING_DIR]/article-1-hero.webp")
if [ "$FILE_SIZE" -gt 204800 ]; then
  cwebp -q 65 -resize 1920 1080 "[COMPOSITED_PATH]" -o "[WORKING_DIR]/article-1-hero.webp"
fi
```

Pillow fallback:
```bash
pip install Pillow --break-system-packages -q
python3 -c "
from PIL import Image
import os
img = Image.open('[COMPOSITED_PATH]').convert('RGB')
img = img.resize((1920, 1080), Image.LANCZOS)
img.save('[WORKING_DIR]/article-1-hero.webp', 'WEBP', quality=80)
size = os.path.getsize('[WORKING_DIR]/article-1-hero.webp')
if size > 204800:
    img.save('[WORKING_DIR]/article-1-hero.webp', 'WEBP', quality=65)
"
```

Save the final WebP path for the Webflow publish step. Alt text for this image becomes the `alt-text-feature-image` CMS field in Step 7.

---

## Step 5: Write Article 2 (Tactical/Actionable)

### Pre-Writing Differentiation Check

Before writing, explicitly state:
1. Article 1's content type, primary keyword, and structure approach
2. Article 2's content type, primary keyword, and structure approach
3. 3-5 specific ways Article 2 will differ from Article 1

If you cannot clearly articulate these differences, STOP and rethink the angle before proceeding.

### Article Requirements

- **Length**: 1,600-2,400 words
- **Content type**: Tactical, actionable, implementation-focused. This article should help the reader DO something concrete.
- **Structure**: Step-by-step sections, numbered processes, actionable checklists, templates, examples, or before/after comparisons. NOT essay-style.
- **Voice**: Same warm, practical tone as Article 1, but more "roll up your sleeves" energy.
- **Unique content**: Do NOT reuse advice, examples, data points, or DonorDock feature mentions from Article 1. Find fresh angles even when drawing from the same transcript.

The second article must be:
- **Distinct** from Article 1 in content type, keyword family, structure, and advice given
- Equally well-researched with its own supporting data
- Cross-linkable to Article 1 where natural (include a link to Article 1's slug if relevant)

Use the same SEO/AEO structure, internal linking rules, DonorDock mention guidelines, and HTML output format as Step 2.

---

## Step 6: Generate Metadata (Article 2)

Repeat Step 3 for the second article. Ensure the slug, title, tags, and target keyword are distinct from Article 1.

---

## Step 7: Image Creation (Article 2) + Publish Both to Webflow

### Generate Article 2's Hero Image

Repeat Step 4 for Article 2, saving as `article-2-hero.webp`.

### Upload Images to Webflow

For each article, upload the WebP hero image as a Webflow asset using the `asset_tool`:
- Use site ID `63ce9d04b1ff6e36cf514274`
- Set alt text to a descriptive string about the article topic

Note: If the asset_tool doesn't support direct file upload, the image will need to be uploaded manually. In that case, skip the `main-image` field and note it for the user to add in Webflow.

### FAQ Generation & Linking (required — before publish)

The Webflow article template emits a **FAQPage JSON-LD schema** dynamically by iterating the article's `article-faqs` multi-reference field. Every article MUST have 4–6 FAQs linked before publish.

For each article:

1. **Extract 4–6 questions from the article content** that a reader would realistically ask. Requirements:
   - Full questions ending in `?` (not fragments)
   - Directly answered by the article body
   - Aligned with the article's AEO questions identified in Step 1 and the universe in `seo-brain/strategy/aeo-questions.md`
   - No duplication of each other (semantic distinctness)

2. **Write the answers** (40–100 words each, HTML-wrapped `<p>…</p>`):
   - Answer the question directly in the first sentence
   - Include specific numbers, tools, or data points where relevant
   - Use DonorDock voice — warm, clear, never corporate
   - Obey all brand-positioning.md rules (no "no platform fees", no "first CRM", Action Board two-words, etc.)

3. **Check for reusable FAQs** before creating new items:
   ```
   mcp__25b1a090…__data_cms_tool → list_collection_items
     collection_id: 69eb6dd45879eb3ff72efb52 (Article FAQs)
     request: { limit: 100, sortBy: "name" }
   ```
   - Compare each candidate question against existing FAQ `name` values by keyword + semantic similarity
   - If a substantively identical FAQ already exists, **reuse its item ID** instead of creating a duplicate
   - FAQs can be shared across multiple articles via the multi-reference field

4. **Create new FAQ items** only for questions not already covered:
   ```
   mcp__25b1a090…__data_cms_tool → create_collection_items
     collection_id: 69eb6dd45879eb3ff72efb52
     request: {
       fieldData: [
         {
           "name": "[Full question ending in ?]",
           "slug": "[kebab-case-slug]",
           "answer-2": "<p>[40–100 word answer, HTML]</p>"
         }
       ]
     }
   ```
   **Note:** the answer field slug is `answer-2` (legacy slug reservation). In Webflow Designer the field displays as "Answer" and the template uses display-name binding, so the slug quirk does not affect rendering. Always use `answer-2` in API calls.

5. **Collect all FAQ item IDs** (reused + newly created). This array populates the `article-faqs` multi-reference in the publish payload below.

6. **Publish the FAQs** (so they're live when the article publishes):
   ```
   mcp__25b1a090…__data_cms_tool → publish_collection_items
     collection_id: 69eb6dd45879eb3ff72efb52
     request: { itemIds: [...all FAQ IDs...] }
   ```

### Create Webflow CMS Drafts

For each article, create a draft item using `data_cms_tool` → `create_collection_items`:

**IMPORTANT: The `blog-post-summary` value MUST be a single continuous HTML string with NO newlines between tags. See Output Format in Step 2.**

```
Collection ID: 6532889f2379aa018d3520b7

Request structure:
{
  "fieldData": [
    {
      "name": "[SEO Title]",
      "slug": "[kebab-case-slug]",
      "blog-post-preview": "[1-2 sentence excerpt]",
      "blog-post-summary": "[Full article HTML body as ONE continuous string -- no newlines between tags]",
      "reading-time": "[number only, e.g. 7]",
      "authors-2": "6532889f2379aa018d352707",
      "featured": false,
      "categories": ["[category-id-1]", "[category-id-2]"],
      "tags-3": ["[tag-id-1]", "[tag-id-2]", "[tag-id-3]"],
      "alt-text-feature-image": "[Descriptive alt text for the hero image]",
      "canonical-url": "https://www.donordock.com/articles/[slug]",
      "pillar": "[single pillar item ID from locked table below]",
      "seo-keywords": "[3–10 comma-separated keywords from pillar keyword-universe]",
      "article-faqs": ["[faq-id-1]", "[faq-id-2]", "[faq-id-3]", "[faq-id-4]"]
    }
  ],
  "isDraft": true,
  "isArchived": false
}
```

**Pillar ID Reference (locked — never discover dynamically):**

| Pillar | Item ID | Pillar URL |
|---|---|---|
| Donor Stewardship | `69eb6cb822a81ad28a27e801` | `/smart-steward-method` |
| CRM | `69eb6cd27fa93ec8ab484322` | `/crm` |
| Online Giving | `69eb6ce266456b7917d21f43` | `/online-giving` |
| Fundraising Strategy | `69eb6cec3a55627ab83d8743` | `/fundraising-strategy` |
| Donor Engagement | `69eb6cf56aa6f92a3a162f6b` | `/donor-outreach` |
| AI for Nonprofits | `69eb6cfd66ac68d8d7702716` | `/otto` |
| Donor Retention | `69eb6d05f4bf8b3eeaface0a` | `/donor-retention` |

**Article FAQs collection ID:** `69eb6dd45879eb3ff72efb52`

**Formatting verification after publish:**
- Fetch the created item back using `list_collection_items` with the item's slug
- Confirm that `<ul>` and `<ol>` list blocks survived (they will be missing if newlines were present)
- Confirm that headings (h2, h3) are intact
- Confirm that links have proper href attributes
- Confirm `pillar`, `seo-keywords`, `canonical-url`, `article-faqs` all populated
- If lists were stripped, re-submit the HTML as a single-line string using `update_collection_items`

### Pre-Publish Validation (required)

Before submitting drafts to Webflow CMS, run validation in parallel via subagents:

1. **brand-identity → brand-critic** subagent — voice, vocabulary, tone-context, banned words. Returns PASS / NEEDS REVISION / MAJOR REWRITE
2. **seo-strategist → content-validator** subagent — structural standards, pillar tag confirmation, FAQ coverage (4–6 items, all tied), internal linking density, prohibited language scan, CMS field completeness (pillar ref, seo-keywords, canonical-url, alt-text, article-faqs). Pass it: full article HTML + claimed pillar + target URL + primary keyword. Returns same verdict scale.
3. **brand-identity → researcher** subagent (optional but recommended for thought-leadership pieces) — fact-check, source verification

**Decision rules:**
- All three return PASS → proceed to publish
- Any return NEEDS REVISION → apply fixes in a single revision pass, then publish (no second-loop)
- Any return MAJOR REWRITE → halt pipeline, surface to user with the rewrite reasoning

Do not loop endlessly. One revision pass is the standard.

### Schema (handled by the Webflow article template — no per-article schema writing)

The article template at `/articles/[slug]` emits **two JSON-LD schemas automatically** by reading the CMS fields you populated above. The pipeline does NOT write per-article BlogPosting or FAQPage schema code. (`/blog/[slug]` is a legacy URL pattern that 301-redirects to `/articles/[slug]`.)

**BlogPosting** (static `<script>` in `<head>`, dynamic-bound):
- Pulls from `name`, `blog-post-preview`, `main-image`, `alt-text-feature-image`, `authors-2.*`, `canonical-url`, `pillar.name` + `pillar.pillar-url`, `seo-keywords`
- Includes `articleSection`, `isPartOf`, `speakable`, `inLanguage: en-US`, `publisher`, `datePublished`, `dateModified`

**FAQPage** (runtime JS-assembled from the DOM):
- Iterates the rendered `.uui-faq01_component` items
- Extracts question from `.uui-faq01_question h5`, answer from `.uui-faq01_answer .w-richtext`
- Injects a valid FAQPage JSON-LD block into `<head>` at page load
- Googlebot executes JS during indexing and picks up the injected schema

This means the pipeline's ONLY job is to populate CMS fields correctly. The schema "just works" if:
- Every field in the publish payload is populated
- The selected pillar exists in the Content Pillars collection and has `pillar-url` set
- The article-faqs multi-ref contains 4–6 FAQ items that are published

**When to still invoke `schema-drafter`:** If the article is specifically a HowTo (step-by-step) or references original Dataset content (e.g., the State of Stewardship report), spawn `donordock-seo-strategist → schema-drafter` to write supplementary HowTo/Dataset JSON-LD to paste into the article's Webflow Page Settings → Custom Code. Skip this agent for standard blog articles — the template covers them fully.

See `seo-brain/remediation/webflow-article-template-schema.md` for the canonical template schema + FAQ JS + CMS field reference.

### Update Transcript Processing Log

After both articles are successfully created as drafts:
1. Fetch the current `config/transcript-processing-log.json` from GitHub (get the latest SHA)
2. Find or create the entry for this transcript's filename
3. Set the `ff-article-pipeline` field to the current ISO timestamp
4. Push the updated file back using `create_or_update_file` with the current SHA

### Final Output

After both drafts are created, report to the user:
- Article 1: title, slug, Webflow item ID, word count, content type (Strategic), **pillar assignment**, **primary keyword + GSC baseline**, **FAQ count** (created vs reused from existing)
- Article 2: title, slug, Webflow item ID, word count, content type (Tactical), **pillar assignment**, **primary keyword + GSC baseline**, **FAQ count** (created vs reused from existing)
- Differentiation summary (1-2 sentences on how the articles differ)
- Image status for each (uploaded, needs manual upload, or regeneration needed)
- Any tags/categories that were created vs. mapped to existing ones
- **CMS field completeness check** — confirm `pillar`, `seo-keywords`, `canonical-url`, `alt-text-feature-image`, and `article-faqs` all populated on both articles
- **Schema coverage** — confirm template will emit BlogPosting + FAQPage for each article based on populated fields (no custom schema needed). Flag if HowTo/Dataset supplementary schema was written by schema-drafter.
- Transcript log status (updated or skipped)
- **Validation verdict** from brand-critic + content-validator + researcher (PASS / NEEDS REVISION / MAJOR REWRITE per agent)
- **Strategic surface delta** — how this run advances the 7-pillar plan (e.g., "+1 article to Pillar 5 / Donor Engagement; first AEO-question coverage for 'how do I write a donor thank-you'")

---

## Webflow Constants (Hardcoded)

These IDs are fixed. Never run discovery calls for them.

| Resource | ID |
|----------|-----|
| Site ID | `63ce9d04b1ff6e36cf514274` |
| Articles Collection | `6532889f2379aa018d3520b7` |
| Tags Collection | `6532889f2379aa018d35206b` |
| Categories Collection | `6532889f2379aa018d352166` |
| Content Pillars Collection | `69eb6ca5f842967743d226a2` |
| Article FAQs Collection | `69eb6dd45879eb3ff72efb52` |
| Author: Rob Burke | `6532889f2379aa018d352707` |
| People Collection | `6532889f2379aa018d3520ff` |

**FAQ answer field slug:** `answer-2` (display name "Answer" — slug is legacy; use `answer-2` in API calls)

**Brand asset URLs (from donordock-brand-identity skill):**
| Asset | URL |
|---|---|
| DonorDock icon PNG (for hero overlay) | `https://raw.githubusercontent.com/DonorDock-team/claude-shared/main/assets/logos-DonorDock/logo-icon-forcircle.png` |
| Silka font files | `https://raw.githubusercontent.com/DonorDock-team/claude-shared/main/assets/fonts/Silka-{Weight}.otf` |

---

## Guardrails

- Keep copy practical, specific, and mission-connected
- Assume experienced but stretched nonprofit operators, not beginner fundraisers
- Never fabricate URLs, statistics, or data points
- Never link to competitor CRM sites as sources
- Never publish live -- always `isDraft: true`
- The two articles MUST be substantially different (see Article Differentiation Strategy). If they feel similar during writing, stop and rethink.
- If a user request conflicts with voice/ICP norms, follow the request and note the tradeoff briefly
- If image generation fails, continue the pipeline and note the failure for manual resolution
