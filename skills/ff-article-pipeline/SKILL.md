---
name: ff-article-pipeline
description: ONLY use when explicitly invoked via slash command or when the user literally says "run ff-article-pipeline" or "run the article pipeline skill". Do NOT auto-trigger on general blog, article, writing, or content requests. This skill runs an automated end-to-end pipeline that researches, writes, illustrates, and publishes two SEO/AEO articles to DonorDock's Webflow CMS from a transcript.
---

# Focused Fundraiser Article Pipeline

This skill runs a complete pipeline that takes a transcript (or topic) and produces two polished, SEO-optimized blog articles with custom hero images, then publishes them as drafts in DonorDock's Webflow CMS.

## When to Use

- User provides a transcript, podcast recording notes, or topic and wants blog articles
- User says "write DonorDock articles", "FF articles", "blog pipeline", "transcript to articles"
- User wants to create thought-leadership content for The Focused Fundraiser blog

## Required Context

- Apply the `donordock-brand-identity` skill if available for voice, ICP, visual, and positioning guidance
- Treat each post as a standalone article even when source material is a shared transcript
- All articles target experienced but stretched nonprofit operators, not beginner fundraisers

## Transcript Processing Log

A shared JSON log at `config/transcript-processing-log.json` in the `DonorDock-team/claude-shared` GitHub repo tracks which transcripts have been processed by each scheduled task. This prevents any transcript from being used twice by the same task.

**When running as a scheduled task (not manual invocation):**
1. At the start of the pipeline, fetch the log via GitHub `get_file_contents` (owner: `DonorDock-team`, repo: `claude-shared`, path: `config/transcript-processing-log.json`)
2. Skip any transcript that already has a non-null `ff-article-pipeline` value in the log
3. After successfully publishing both article drafts, update the log by adding or updating the transcript's entry with the `ff-article-pipeline` key set to the current ISO timestamp
4. Push the updated log back to GitHub using `create_or_update_file` (include the file's current SHA for the update)

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

At the beginning of Step 1, use the GitHub `get_file_contents` tool to fetch both files:

| File | Repo Path | What it contains |
|------|-----------|------------------|
| CMS Schema | `sitemaps/cms-schema.md` | Collection IDs, field schema, tag/category IDs, author IDs, CMS item creation template |
| Website Sitemap | `sitemaps/website-sitemap.json` | donordock.com pages with URLs, titles, sections -- use for internal linking |

```
Owner: DonorDock-team
Repo: claude-shared
Paths:
  - sitemaps/cms-schema.md
  - sitemaps/website-sitemap.json
```

These files provide:
- **Tag and category IDs** for CMS publishing (from cms-schema.md)
- **Valid internal link targets** for articles (from the website sitemap)
- **Content audit data** to avoid duplicating existing topics (cross-reference with CMS article list)

## Logo and Font Assets (GitHub)

Hero images include a DonorDock logo overlay and article title text. These assets live in the `DonorDock-team/claude-shared` repo:

| Asset | Repo Path | Usage |
|-------|-----------|-------|
| White logo (primary) | `assets/logos-DonorDock/DonorDock-Logo-ALLWHITE.png` | Bottom-right corner overlay on hero images |
| Dark logo (fallback) | `assets/logos-DonorDock/DonorDock-Logo-Dark.png` | Use only if the hero image has a very light background |
| Light logo | `assets/logos-DonorDock/DonorDock-Logo-Light.png` | Alternative if white doesn't contrast well |

The white logo is the default for most hero images since nanobanana generates images with rich colors/backgrounds.

---

## Pipeline Overview

The pipeline has 7 steps that run end-to-end without approval gates:

**Dependency pre-check (run once at pipeline start):**
Before any image work, ensure Python Pillow is available for image compositing and compression:
```bash
python3 -c "from PIL import Image, ImageDraw, ImageFont" 2>/dev/null || pip3 install Pillow -q
```

1. **Research & Angle Discovery** -- Analyze input, audit existing CMS content for gaps, propose two deliberately different angles
2. **Write Article 1** -- Draft a strategic/analytical SEO/AEO article
3. **Generate Metadata 1** -- SEO title, meta description, slug, read time, tags
4. **Image Creation 1** -- Generate hero image via Nano Banana, overlay logo + title, compress to WebP under 200KB
5. **Write Article 2** -- Draft a tactical/actionable article (verify differentiation first)
6. **Generate Metadata 2** -- Same metadata process for article 2
7. **Image Creation 2 + Publish Both** -- Generate second hero image, create both Webflow drafts, update transcript log

---

## Step 1: Research & Angle Discovery

### Inputs
- Transcript file path (if provided) -- read it in full
- Topic/title (if provided instead of transcript)

### Process

1. **Fetch shared resources from GitHub** -- Before anything else, use the GitHub `get_file_contents` tool (owner: `DonorDock-team`, repo: `claude-shared`) to fetch these files in parallel:
   - `sitemaps/cms-schema.md` -- for CMS field schema, tag/category IDs, author IDs, and the item creation template
   - `sitemaps/website-sitemap.json` -- for valid donordock.com page URLs to use as internal links
   - `config/transcript-processing-log.json` -- to check which transcripts have already been processed (scheduled task runs only)

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

6. **Output**: Present both article angles with:
   - Working title
   - Content type label (Strategic/Analytical or Tactical/Actionable)
   - Target search query (what someone would Google to find this)
   - 2-3 sentence summary of the angle
   - Key supporting data points with sources
   - How this angle differs from the other one (1 sentence)

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

### SEO/AEO Structure

- H1 should contain the primary keyword naturally
- Include the target query verbatim once in the first 150 words
- Use H2s that could serve as featured snippet answers (question-format H2s work well)
- Include a "quick answer" paragraph near the top (2-3 sentences that directly answer the target query) -- this is your AEO play
- Naturally weave in 2-3 related long-tail keywords

### Internal Linking

- Include 2-4 validated internal links to existing DonorDock pages
- Only link to URLs confirmed to exist in the website sitemap (`sitemaps/website-sitemap.json`) or the CMS article list fetched via Webflow
- Website sitemap links work well for linking to product pages, pricing, or feature overview pages
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

---

## Step 4: Image Creation (Article 1)

### Build the Image Prompt

Create a Nano Banana prompt for a 1920x1080 blog hero graphic that:
- Visually represents the article's core theme
- Has high click intent -- would make someone want to read the article in a social feed or search result
- Uses a clean, modern, professional aesthetic suitable for a nonprofit SaaS brand
- Avoids stock photo cliches (no handshakes, no generic "diverse team smiling at laptop")
- **Leaves the bottom 20% of the image relatively clean/simple** -- this area will have a gradient overlay with the article title and DonorDock logo composited on top
- Uses warm, approachable colors that complement DonorDock's brand palette (blues, greens, warm neutrals)

Prompt template pattern:
```
Professional blog hero image for a nonprofit fundraising article about [TOPIC].
[SPECIFIC VISUAL CONCEPT that metaphorically represents the theme].
Clean modern design, warm color palette with soft blues and greens,
professional but approachable feel. High-quality editorial style photograph/illustration.
Designed for a 1920x1080 blog header. Keep the bottom 20% of the image
simple and uncluttered as text will be overlaid there.
```

### Generate the Image

Call the `nanobanana_generate_image` MCP tool:
- **model**: `nanobanana2`
- **aspect_ratio**: `16:9`
- **image_size**: `2K` (will be compressed down)
- **output_dir**: `/Users/rob/Documents/DonorDock/Claude Projects/Deliverables`

**IMPORTANT:** Always use this exact absolute path for `output_dir`. This is a known, accessible directory on the local filesystem that both Claude Code and scheduled tasks can read/write. Do NOT use relative paths, session directories, temp directories, or any other location.

### Composite Logo + Title Text, Then Compress to WebP (Under 200KB)

After nanobanana generates the base image, use Pillow to:
1. Add a semi-transparent dark gradient bar across the bottom ~18% of the image
2. Overlay the DonorDock white logo in the bottom-right corner
3. Add the article's SEO title as text in the bottom-left area
4. Compress to WebP under 200KB

**Logo source:** Download from the GitHub repo at runtime using urllib (no extra dependency needed):
```
https://raw.githubusercontent.com/DonorDock-team/claude-shared/main/assets/logos-DonorDock/DonorDock-Logo-ALLWHITE.png
```

**Full compositing + compression script:**
```bash
python3 << 'PYEOF'
from PIL import Image, ImageDraw, ImageFont
import urllib.request
import os
import tempfile

# --- CONFIGURATION (replace these values) ---
input_path = "[INPUT_PATH]"  # nanobanana output PNG path
article_title = "[ARTICLE TITLE]"  # The SEO title for this article
output_path = "/Users/rob/Documents/DonorDock/Claude Projects/Deliverables/article-1-hero.webp"

# --- DOWNLOAD LOGO ---
logo_url = "https://raw.githubusercontent.com/DonorDock-team/claude-shared/main/assets/logos-DonorDock/DonorDock-Logo-ALLWHITE.png"
logo_tmp = os.path.join(tempfile.gettempdir(), "dd-logo-white.png")
urllib.request.urlretrieve(logo_url, logo_tmp)

# --- OPEN AND RESIZE BASE IMAGE ---
img = Image.open(input_path).convert("RGBA")
img = img.resize((1920, 1080), Image.LANCZOS)

# --- ADD GRADIENT OVERLAY AT BOTTOM ---
# Semi-transparent black gradient covering bottom 18% for text readability
overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
draw_overlay = ImageDraw.Draw(overlay)
gradient_start_y = int(1080 * 0.82)  # Start gradient at 82% from top
for y in range(gradient_start_y, 1080):
    progress = (y - gradient_start_y) / (1080 - gradient_start_y)
    alpha = int(180 * progress)  # Fade from 0 to 180 opacity
    draw_overlay.line([(0, y), (1920, y)], fill=(0, 0, 0, alpha))
img = Image.alpha_composite(img, overlay)

# --- OVERLAY DONORDOCK LOGO (bottom-right) ---
logo = Image.open(logo_tmp).convert("RGBA")
# Resize logo proportionally to ~180px wide
logo_width = 180
logo_ratio = logo_width / logo.width
logo_height = int(logo.height * logo_ratio)
logo = logo.resize((logo_width, logo_height), Image.LANCZOS)
# Position: bottom-right with 30px padding
logo_x = 1920 - logo_width - 30
logo_y = 1080 - logo_height - 25
img.paste(logo, (logo_x, logo_y), logo)

# --- ADD ARTICLE TITLE TEXT (bottom-left) ---
draw = ImageDraw.Draw(img)
# Font fallback chain for macOS
font = None
font_size = 38
font_paths = [
    "/System/Library/Fonts/SFCompact.ttf",
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
    "/Library/Fonts/Arial Bold.ttf",
]
for fp in font_paths:
    try:
        font = ImageFont.truetype(fp, font_size)
        break
    except (IOError, OSError):
        continue
if font is None:
    font = ImageFont.load_default()

# Word-wrap the title to fit within ~65% of image width (leaving room for logo)
max_text_width = int(1920 * 0.65)
words = article_title.split()
lines = []
current_line = ""
for word in words:
    test_line = f"{current_line} {word}".strip()
    bbox = draw.textbbox((0, 0), test_line, font=font)
    if bbox[2] - bbox[0] <= max_text_width:
        current_line = test_line
    else:
        if current_line:
            lines.append(current_line)
        current_line = word
if current_line:
    lines.append(current_line)

# Draw text lines from the bottom up, 30px left padding
line_height = font_size + 8
text_y = 1080 - 30 - (len(lines) * line_height)
for line in lines:
    # Draw subtle shadow for extra readability
    draw.text((32, text_y + 2), line, font=font, fill=(0, 0, 0, 160))
    draw.text((30, text_y), line, font=font, fill=(255, 255, 255, 240))
    text_y += line_height

# --- COMPRESS TO WEBP UNDER 200KB ---
img = img.convert("RGB")  # WebP doesn't need alpha
for quality in [80, 70, 60, 50, 40]:
    img.save(output_path, "WEBP", quality=quality)
    size_kb = os.path.getsize(output_path) / 1024
    if size_kb <= 200:
        print(f"Saved at quality {quality}: {size_kb:.0f}KB")
        break
else:
    print(f"Warning: Could not get under 200KB. Final size: {size_kb:.0f}KB")

print(f"Output: {output_path}")

# Clean up temp logo
os.remove(logo_tmp)
PYEOF
```

**Notes:**
- The gradient overlay ensures both the white logo and white title text are readable over any background
- If the base image has a very light/white bottom area, the gradient handles contrast automatically
- Logo is sized at 180px wide (proportional height) -- large enough to be recognizable, small enough not to dominate
- Title text wraps to ~65% of image width so it doesn't collide with the logo on the right
- The script uses only stdlib (`urllib`, `os`, `tempfile`) plus Pillow -- no extra pip dependencies

Save the final WebP path for use in the Webflow publish step.

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

Repeat Step 4 for Article 2, with these differences:
- **output filename**: `article-2-hero.webp` (instead of `article-1-hero.webp`)
- **article_title**: Use Article 2's SEO title
- Everything else (output_dir, logo, gradient, compression) stays the same

### Upload Images to Webflow

For each article, upload the WebP hero image as a Webflow asset using the `asset_tool`:
- Use site ID `63ce9d04b1ff6e36cf514274`
- Set alt text to a descriptive string about the article topic

Note: If the asset_tool doesn't support direct file upload, the image will need to be uploaded manually. In that case, skip the `main-image` field and note it for the user to add in Webflow.

### Create Webflow CMS Drafts

For each article, create a draft item using `data_cms_tool` -> `create_collection_items`:

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
      "alt-text-feature-image": "[Descriptive alt text for the hero image]"
    }
  ],
  "isDraft": true,
  "isArchived": false
}
```

**Formatting verification after publish:**
- Fetch the created item back using `list_collection_items` with the item's slug
- Confirm that `<ul>` and `<ol>` list blocks survived (they will be missing if newlines were present)
- Confirm that headings (h2, h3) are intact
- Confirm that links have proper href attributes
- If lists were stripped, re-submit the HTML as a single-line string using `update_collection_items`

### Update Transcript Processing Log

After both articles are successfully created as drafts:
1. Fetch the current `config/transcript-processing-log.json` from GitHub (get the latest SHA)
2. Find or create the entry for this transcript's filename
3. Set the `ff-article-pipeline` field to the current ISO timestamp
4. Push the updated file back using `create_or_update_file` with the current SHA

### Final Output

After both drafts are created, report to the user:
- Article 1: title, slug, Webflow item ID, word count, content type (Strategic)
- Article 2: title, slug, Webflow item ID, word count, content type (Tactical)
- Differentiation summary (1-2 sentences on how the articles differ)
- Image status for each (uploaded or needs manual upload)
- Any tags/categories that were created vs. mapped to existing ones
- Transcript log status (updated or skipped)

---

## Webflow Constants (Hardcoded)

These IDs are fixed. Never run discovery calls for them.

| Resource | ID |
|----------|-----|
| Site ID | `63ce9d04b1ff6e36cf514274` |
| Articles Collection | `6532889f2379aa018d3520b7` |
| Tags Collection | `6532889f2379aa018d35206b` |
| Categories Collection | `6532889f2379aa018d352166` |
| Author: Rob Burke | `6532889f2379aa018d352707` |
| People Collection | `6532889f2379aa018d3520ff` |

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
