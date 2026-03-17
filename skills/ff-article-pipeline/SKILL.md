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

## Shared Resources (GitHub)

The CMS schema and website sitemap live in the `DonorDock-team/claude-shared` GitHub repo under the `sitemaps/` folder. These are the single source of truth and should always be fetched fresh at the start of every pipeline run so you're working with the latest data (tags, categories, URLs, etc.) rather than stale bundled copies.

At the beginning of Step 1, use the GitHub `get_file_contents` tool to fetch both files:

| File | Repo Path | What it contains |
|------|-----------|------------------|
| CMS Schema | `sitemaps/cms-schema.md` | Collection IDs, field schema, tag/category IDs, author IDs, CMS item creation template |
| Website Sitemap | `sitemaps/website-sitemap.json` | donordock.com pages with URLs, titles, sections — use for internal linking |

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

---

## Pipeline Overview

The pipeline has 7 steps that run end-to-end without approval gates:

1. **Research & Angle Discovery** — Analyze input, audit existing CMS content for gaps, propose angles
2. **Write Article 1** — Draft a full SEO/AEO article
3. **Generate Metadata 1** — SEO title, meta description, slug, read time, tags
4. **Image Creation 1** — Generate hero image via Nano Banana, compress to WebP
5. **Write Article 2** — Draft a second distinct article from same source
6. **Generate Metadata 2** — Same metadata process for article 2
7. **Image Creation 2 + Publish Both** — Generate second hero image, then create both Webflow drafts

---

## Step 1: Research & Angle Discovery

### Inputs
- Transcript file path (if provided) — read it in full
- Topic/title (if provided instead of transcript)

### Process

1. **Fetch shared resources from GitHub** — Before anything else, use the GitHub `get_file_contents` tool (owner: `DonorDock-team`, repo: `claude-shared`) to fetch both sitemaps files in parallel:
   - `sitemaps/cms-schema.md` — for CMS field schema, tag/category IDs, author IDs, and the item creation template
   - `sitemaps/website-sitemap.json` — for valid donordock.com page URLs to use as internal links

2. **Read the transcript or topic** thoroughly. Extract every distinct theme, insight, quote, and actionable takeaway.

3. **Audit existing DonorDock articles** for content gaps:
   - Use the Webflow `data_cms_tool` to list recent articles in collection `6532889f2379aa018d3520b7` (fetch 30-50 items with `sortBy: lastPublished, sortOrder: desc`)
   - Compare themes from the transcript against existing article titles and previews
   - Cross-reference against the website sitemap to understand what content already exists across DonorDock properties
   - Identify 2 angles that fill genuine gaps — topics the blog hasn't covered or hasn't covered recently

4. **Web research** to gather 3-5 supporting data points per angle from trusted nonprofit sources:
   - Acceptable: FEP, Giving USA, AFP, Nonprofit Quarterly, Chronicle of Philanthropy, NTEN, BoardSource, National Council of Nonprofits, and others like them
   - Never use competitor CRM sources (Bloomerang, Little Green Light, Neon, Kindful, Networkforgood, donor perfect, etc.) as citation sources
   - Never fabricate URLs or statistics

5. **Output**: Present both article angles with:
   - Working title
   - Target search query (what someone would Google to find this)
   - 2-3 sentence summary of the angle
   - Key supporting data points with sources

Then proceed directly to writing.

---

## Step 2: Write Article 1

### Article Requirements

- **Length**: 1,600-2,400 words
- **Structure**: H1 title → H2 sections → H3 subsections where needed
- **Voice**: Second person ("you/your") throughout. Warm, practical, direct. No jargon walls. Write like a smart colleague who respects the reader's time.
- **Format constraints**:
  - No tables (Webflow rich text handles them poorly)
  - No em dashes — use commas, periods, or parentheses instead
  - Short paragraphs (2-4 sentences max)
  - Use scannable lists where they genuinely help
  - Bold key phrases sparingly for scannability

### SEO/AEO Structure

- H1 should contain the primary keyword naturally
- Include the target query verbatim once in the first 150 words
- Use H2s that could serve as featured snippet answers (question-format H2s work well)
- Include a "quick answer" paragraph near the top (2-3 sentences that directly answer the target query) — this is your AEO play
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
- Keep mentions organic — the article should be valuable even without DonorDock references
- Never make the article feel like a product pitch

### Output Format

Write the article body in clean HTML suitable for Webflow rich text.

**CRITICAL — Webflow Rich Text API Formatting Rules:**

Webflow's CMS API will **silently strip HTML elements** (especially lists) that contain whitespace or newlines between tags. The entire article HTML must be submitted as a **single continuous string with zero newlines or extra whitespace between tags**. This is the #1 cause of lists and other elements disappearing after publish.

**Required format (all inline, no `\n` between tags):**
```
<p>Here is a list:</p><ul><li>First item</li><li>Second item</li><li>Third item</li></ul><p>Next paragraph.</p>
```

**Broken format (newlines between tags — Webflow WILL strip the list):**
```
<ul>
<li>First item</li>
<li>Second item</li>
</ul>
```

**Allowed tags:**
- `<h2>`, `<h3>` for headings (no `<h1>` — that's the CMS title field)
- `<p>` for paragraphs
- `<ul><li>` or `<ol><li>` for lists — must be inline with no newlines between tags
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
- Has high click intent — would make someone want to read the article in a social feed or search result
- Uses a clean, modern, professional aesthetic suitable for a nonprofit SaaS brand
- Avoids stock photo cliches (no handshakes, no generic "diverse team smiling at laptop")
- Works well with text overlay (leave visual breathing room, avoid busy center compositions)
- Uses warm, approachable colors that complement DonorDock's brand palette (blues, greens, warm neutrals)

Prompt template pattern:
```
Professional blog hero image for a nonprofit fundraising article about [TOPIC].
[SPECIFIC VISUAL CONCEPT that metaphorically represents the theme].
Clean modern design, warm color palette with soft blues and greens,
professional but approachable feel. High-quality editorial style photograph/illustration.
Designed for a 1920x1080 blog header with space for text overlay.
```

### Generate the Image

Call the `nanobanana_generate_image` MCP tool:
- **model**: `nanobanana2`
- **aspect_ratio**: `16:9`
- **image_size**: `2K` (will be compressed down)
- **output_dir**: Use the current session's working directory (e.g., `/sessions/<session-name>/`)

### Compress to WebP

After generation, compress the PNG to WebP format:

```bash
# Install cwebp if needed
which cwebp || (apt-get update -qq && apt-get install -y -qq webp)

# Compress to WebP, quality 80, targeting under 200KB
cwebp -q 80 -resize 1920 1080 "[INPUT_PATH]" -o "[WORKING_DIR]/article-1-hero.webp"

# Check file size — if over 200KB, re-compress at lower quality
FILE_SIZE=$(stat -f%z "[WORKING_DIR]/article-1-hero.webp" 2>/dev/null || stat -c%s "[WORKING_DIR]/article-1-hero.webp")
if [ "$FILE_SIZE" -gt 204800 ]; then
  cwebp -q 65 -resize 1920 1080 "[INPUT_PATH]" -o "[WORKING_DIR]/article-1-hero.webp"
fi
```

If cwebp is not available, use Python Pillow as a fallback:
```bash
pip install Pillow --break-system-packages -q
python3 -c "
from PIL import Image
import os
img = Image.open('[INPUT_PATH]')
img = img.resize((1920, 1080), Image.LANCZOS)
img.save('[WORKING_DIR]/article-1-hero.webp', 'WEBP', quality=80)
size = os.path.getsize('[WORKING_DIR]/article-1-hero.webp')
if size > 204800:
    img.save('[WORKING_DIR]/article-1-hero.webp', 'WEBP', quality=65)
"
```

Save the final WebP path for use in the Webflow publish step.

---

## Step 5: Write Article 2

Repeat Step 2 with the second angle from Step 1. The second article must be:
- **Distinct** from Article 1 in topic, angle, and target query
- Equally well-researched with its own supporting data
- Cross-linkable to Article 1 where natural (include a link to Article 1's slug if relevant)

Use the same writing requirements, SEO/AEO structure, and output format as Step 2.

---

## Step 6: Generate Metadata (Article 2)

Repeat Step 3 for the second article. Ensure the slug, title, and tags are distinct from Article 1.

---

## Step 7: Image Creation (Article 2) + Publish Both to Webflow

### Generate Article 2's Hero Image

Repeat Step 4 for Article 2, saving as `article-2-hero.webp`.

### Upload Images to Webflow

For each article, upload the WebP hero image as a Webflow asset using the `asset_tool`:
- Use site ID `63ce9d04b1ff6e36cf514274`
- Set alt text to a descriptive string about the article topic

Note: If the asset_tool doesn't support direct file upload, the image will need to be uploaded manually. In that case, skip the `main-image` field and note it for the user to add in Webflow.

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
      "blog-post-summary": "[Full article HTML body as ONE continuous string — no newlines between tags]",
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

### Final Output

After both drafts are created, report to the user:
- Article 1: title, slug, Webflow item ID, word count
- Article 2: title, slug, Webflow item ID, word count
- Image status for each (uploaded or needs manual upload)
- Any tags/categories that were created vs. mapped to existing ones

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
- Never publish live — always `isDraft: true`
- If a user request conflicts with voice/ICP norms, follow the request and note the tradeoff briefly
- If image generation fails, continue the pipeline and note the failure for manual resolution
