# Fix Checklist — DonorDock Webflow

Each item has: WHERE to fix, EXACT steps, and WHY it matters.

---

## 1. robots.txt — Unblock AI bots

**WHERE:** Cloudflare (NOT Webflow). The blocks are from Cloudflare's Managed Content Signal policy, not your Webflow robots.txt.

**Evidence:** `/robots.txt` shows `User-agent: ClaudeBot` / `User-agent: GPTBot` / etc. with `Disallow: /`. These are injected by Cloudflare's "Block AI Scrapers" feature.

**Steps:**
1. Log into Cloudflare dashboard → select `donordock.com` zone
2. Security → **Bots** → look for "AI Scrapers and Crawlers" or "Content Signals"
   - If set to "Block all" → switch to "Allow selectively" and allow GPTBot, ClaudeBot, Google-Extended, Applebot-Extended, PerplexityBot, OAI-SearchBot, ChatGPT-User, anthropic-ai, Claude-Web, CCBot
3. If the setting isn't there, check:
   - Rules → **Transform Rules** for any robots.txt override
   - Rules → **WAF → Managed Rules** for AI-bot managed rules
4. Alternative: Rules → **Managed Transforms** → disable "Block AI scrapers" if enabled
5. After change, wait 5 minutes, then curl `https://www.donordock.com/robots.txt` to verify AI bot lines are gone

**Webflow side:** Once Cloudflare is fixed, you can also set your Webflow Project Settings → SEO → robots.txt to explicitly include:
```
User-agent: *
Allow: /

User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: anthropic-ai
Allow: /

User-agent: CCBot
Allow: /

Sitemap: https://www.donordock.com/sitemap.xml
```

**Strategic note:** This is a brand/IP call. Blocking AI scrapers preserves your content from training use, but also blocks AI citations (ChatGPT, Perplexity, Gemini, AI Overviews). For DonorDock's stated AEO strategy, unblocking is required. Weigh with legal if needed.

---

## 2. Pricing page — Fix invalid JSON + add FAQPage

**WHERE:** Webflow Designer → Pages panel → `/pricing` → Page Settings (gear icon) → Custom Code → "Inside `<head>` tag" or "Before `</body>` tag"

**Current problem:** The SoftwareApplication JSON-LD has a trailing comma in the offers array that breaks parsing. Google sees zero schema on /pricing.

**Steps:**
1. Open Webflow Designer → `/pricing` page
2. Click the gear icon for Page Settings
3. Scroll to "Custom Code" → find the existing `<script type="application/ld+json">` block
4. Select all text inside that script tag, delete it
5. Paste the contents of `seo-brain/remediation/schemas/pricing-page.html` (everything between and including the `<script>` tags)
6. Save and publish
7. Verify: https://search.google.com/test/rich-results → enter https://www.donordock.com/pricing → confirm SoftwareApplication + FAQPage detected

---

## 3. DonorPerfect compare — Fix invalid JSON

**WHERE:** Webflow Designer → Pages → Compare → `donorperfect-vs-donordock` → Page Settings → Custom Code

**Steps:**
1. Same pattern as pricing — find the broken `<script type="application/ld+json">` block
2. Validate the existing JSON by copying it into https://jsonlint.com — it will highlight the trailing comma / orphan brace
3. Fix the specific syntax error, OR replace entirely with clean SoftwareApplication + Review schema
4. Re-test with Google Rich Results Test

**Quick fix you can do yourself:** Often these errors are just `},]` — change to `}]`. Or `...,\n }` after the last object — delete the comma and empty brace.

---

## 4. Neon compare page H1 typo

**WHERE:** Webflow Designer → Pages → Compare → `neon-crm-vs-donordock`

**Steps:**
1. Open the page in Designer
2. Find the H1 element (hero heading)
3. Change text from `Network for Good vs DonorDock` to `Neon CRM vs DonorDock`
4. Check the page's JSON-LD block too — the Review schemas may reference the wrong competitor name
5. Publish

**Verified live:** Yes, H1 was wrong as of 2026-04-22. Rob, re-verify after fix to confirm.

---

## 5. llms.txt — Re-save as UTF-8 plain text

**WHERE:** Wherever this file is hosted. Let me know if it's:
- Webflow asset (uploaded file)
- Webflow code embed (inline text in a page)
- A redirect/rewrite rule pointing to another location

**Steps (assuming Webflow asset):**
1. Open the llms.txt source in **VS Code** (NOT TextEdit — TextEdit defaults to RTF)
2. If VS Code opens it as RTF, use "Change Encoding" → UTF-8
3. Content should look like:
```
# DonorDock llms.txt

# About
DonorDock is a donor management CRM for small-to-mid nonprofits.

# Policy
Training: allowed
Attribution: Please reference "DonorDock" and link to https://donordock.com

# Key pages
/pricing - DonorDock pricing ($500/mo, unlimited contacts)
/crm - Donor relationship management
/online-giving - Accept donations online
/compare - Compare DonorDock to other nonprofit CRMs
/faq - Frequently asked questions
/articles - Fundraising and nonprofit guidance

# Contact
https://www.donordock.com/contact
```
4. Save as `llms.txt` with UTF-8 encoding, no BOM, Unix line endings
5. Re-upload to Webflow assets (or wherever it's hosted)
6. Verify: `curl -s https://donordock.com/llms.txt | head -3` should show plain text

---

## 6. Hero image dimensions (homepage + sitewide)

**WHERE:** Webflow Designer → Homepage → hero section

**Current:** `<img ... width="Auto" height="Auto" ...>` (literal strings, broken)

**Steps — Homepage hero (do this first, highest impact):**
1. Open Homepage in Designer
2. Click the hero image element
3. In Settings panel on right → find Width and Height fields
4. Set Width: `1200` (or actual pixel width of your asset)
5. Set Height: `800` (or actual)
6. Scroll down to "Custom attributes" → Add attribute → Name: `fetchpriority`, Value: `high`
7. Page Settings → Custom Code → Inside `<head>` → add:
```html
<link rel="preload" as="image" href="<HERO_IMAGE_URL>" fetchpriority="high">
```
8. Publish

**Sitewide batch fix (CLS ranking factor):**
Since 68 of 69 images on homepage lack dimensions, this is a template-level problem. For each Webflow template (Article CMS template, Feature CMS template, Compare CMS template, Solution CMS template, Integration CMS template, Team CMS template, homepage, static pages):
1. Walk through each image element
2. Set Width + Height in the Settings panel
3. Webflow also supports Responsive Images if enabled — Project Settings → Hosting → make sure this is on

Prioritize templates by traffic: Article template > Homepage > Compare template > Feature template > others.

---

## 7. Meta description — add sitewide

**What it is:** Meta description is the 150-160 character blurb Google shows UNDER your page title in search results. It's also what AI engines (ChatGPT, Perplexity) often use as a one-line summary of the page.

**Where it lives in HTML:** `<meta name="description" content="...">`

**Where to set in Webflow:** Every page has Page Settings → SEO Settings → "Meta Description" field.

**Current state:** Empty on every DonorDock page audited.

**Fix options:**

### Option A (fastest): I do bulk update via Webflow MCP
I have access to the Webflow Data API `update_page_settings` tool. I can pull every page's title + content, draft an optimized meta description (150-160 chars, includes primary keyword), and update all pages in one pass. Drafts to review would land in `seo-brain/remediation/meta-description-bulk-draft.md`.

### Option B: You add one at a time in Designer
Page Settings → SEO → Meta Description field. 150-160 chars. Each page needs a unique description that:
- Includes the primary keyword
- Describes the page's specific value
- Has a soft CTA ("Learn more," "Compare," "See pricing")

**Recommendation:** Let me run Option A for the top 20 pages (homepage, pricing, compare hub, 9 compare pages, /crm, /online-giving, /donor-outreach, /otto, /tour, /about, /features-overview). You review drafts, approve, I push. 1-2 hours total.

---

## 8. Duplicate BlogPosting scripts on articles

**WHERE:** Article CMS template page in Webflow Designer.

**Evidence:** `/articles/best-nonprofit-crm` has 2 `BlogPosting` scripts — one with ISO 8601 dates, one with human-readable dates. Replicated across all 467 articles because it's a template-level issue.

**How to find which is which:**
- Script 1: likely in Page Settings → Custom Code → Before `</body>` — uses CMS field bindings like `{{wf {"path":"datePublished","type":"DateTime"} }}` — outputs ISO 8601 — KEEP THIS ONE
- Script 2: likely a Code Embed element somewhere inside the article template body — uses `{{wf {"path":"date-published","type":"PlainText"} }}` — outputs human-readable — DELETE

**Steps:**
1. Open Article CMS template page in Designer
2. In Navigator panel (left sidebar), search for "Code Embed" or "Embed" — you'll find one inside the article body
3. Click it, check its content — if it contains `"@type":"BlogPosting"`, delete the element
4. Go to Page Settings → Custom Code → verify there's one BlogPosting script there using ISO 8601 format
5. Publish
6. Verify: curl a random article, grep for `BlogPosting` — should see 1, not 2

---

## 9. Tag archive pages (88) — noindex approach

**Your intuition is right.** Rescuing 88 tag pages with hand-crafted content is expensive; noindexing them is faster and safer for SEO.

**Steps:**
1. Webflow Designer → Pages → CMS Collection Pages → Tags template
2. Page Settings (gear icon) → SEO → look for "Allow search engines to index this page" — UNCHECK it
   - If that option isn't at CMS template level, go to Option B below
3. Or Option B: Page Settings → Custom Code → Inside `<head>` → add:
```html
<meta name="robots" content="noindex,follow">
```
4. Also exclude from sitemap: Project Settings → SEO → Advanced → Exclude paths → `/tags/`
5. Publish
6. Submit request in GSC → Removals → Temporary removals for tag URLs (speeds up deindex)

**Note:** `noindex,follow` means Google won't show the tag pages in search but WILL still crawl outbound links. You keep link equity flowing to the articles.

**Keep the 10 strongest tags for later rescue:** fundraising, donor-engagement, donor-relationships, nonprofit-strategy, donor-stewardship, donor-management, online-fundraising, outreach, crm, grants. After noindex is in place and proven to lift site quality scores, come back in Q3 and hand-craft editorial intros for these 10 to bring them back as topic landing pages.

---

## 10. Newsletter form DOM position

**Problem:** "Weekly Roundup" form renders in article template DOM BEFORE the article body. First words crawlers see on every article: "Signup Successful! Oops! Something went wrong..."

**Fix in Webflow:**
1. Open Article CMS template page in Designer
2. In Navigator panel, find the "Weekly Roundup" form section
3. Note its current position (probably a section above the article body)
4. **Option A (simplest):** Drag the newsletter section below the article body section in the Navigator
5. **Option B (preserves visual):** Keep visual position via CSS — wrap article body + sidebar in a flex container, apply `order: -1` to article body so it's first in DOM but sidebar rendered right
6. Publish
7. Verify: curl an article, grep for "Signup Successful" location — should be AFTER the article content in the HTML

---

## 11. FAQ page — accordions as divs + nested @graph

**Two separate fixes on `/faq`:**

### A. Convert div accordions to semantic H2/H3
**Problem:** FAQ questions render as styled `<div>` accordions. Google cross-checks schema against visible headings; when the schema says FAQPage but the visible text isn't in headings, FAQ rich results can be suppressed.

**Steps:**
1. Webflow Designer → /faq page
2. Click one of the question accordion headers
3. In the Settings panel → "Tag" dropdown → change from `Div Block` to `Heading 3`
4. Repeat for all 114 question elements (or apply via a Global Class if they all share one)
5. OR if they're component instances, edit the component once and all instances update

### B. Fix nested @graph wrapper
**Problem:** /faq JSON-LD is structured as `{ "@context":..., "@graph": [{ "@context":..., "@graph": [...] }] }` — the nested `@graph` can cause Google's Rich Results Test to fail.

**Steps:**
1. Page Settings → Custom Code → find the JSON-LD script
2. Flatten to: `{ "@context":"https://schema.org", "@graph": [ ...all 114 Question entities... ] }`
3. Validate at https://validator.schema.org
4. Publish

---

## 12. Add FAQPage schema to compare pages + feature pages missing it

**Compare pages missing FAQPage:** bloomerang, donorperfect, givebutter (has valid JSON, needs FAQ added), bonterra (empty JSON-LD entirely), salesforce (empty)

**Feature pages missing FAQPage (but visible FAQ):** moves-management, contact-management, email-marketing, text-messaging, project-management, recurring-donations, and others

**Use template:** `seo-brain/remediation/schemas/compare-faqpage-template.html`. Replace question/answer placeholders with actual Q&A already on each page.

---

## Direct Webflow MCP actions I can take for you

I have access to Webflow's Data API. Here's what I CAN do directly (on your OK):

- **Update page meta descriptions** in bulk via `update_page_settings`. Works for any static or CMS page. Draft list in `meta-description-bulk-draft.md`.
- **Update page SEO titles** in bulk (same tool).
- **List all pages** to generate an inventory (already done — 100+ pages found).
- **Add inline site scripts** via `data_scripts_tool` (site-wide JS). Not the same as per-page JSON-LD, but could be used for site-wide Organization schema.

What I CANNOT do via the Data API:
- Edit per-page Custom Code blocks (where most JSON-LD lives). This is Designer-only.
- Edit element attributes (width/height on images, attribute changes). Designer-only.
- Move elements in the DOM (newsletter form repositioning). Designer-only.
- Change element types (div → H3 accordions). Designer-only.

If you open Webflow Designer and it's connected to this session, I may be able to use Designer tools (element_tool, style_tool, etc.) to do some of the Designer-level fixes. Worth a try if you want — open the pricing page in Designer and let me know.
