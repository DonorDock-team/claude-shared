# Webflow Article Template Schema (Canonical)

**Status:** LIVE as of 2026-04-24. All `/blog/{slug}` URLs emit BlogPosting + FAQPage automatically.

**Source of truth:** This file. If this differs from the live Webflow template, update the template, not this file.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│  Webflow Article Template (CMS: Articles, 6532889f…3520b7)  │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  [HEAD]                                                      │
│  ┌───────────────────────────────────────────────────────┐  │
│  │ <script type="application/ld+json">                   │  │
│  │   BlogPosting  ← binds 15+ CMS fields dynamically     │  │
│  │ </script>                                             │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                              │
│  [BODY]                                                      │
│  ┌───────────────────────────────────────────────────────┐  │
│  │ <section> "Frequently asked questions"                │  │
│  │   Webflow Collection List bound to article-faqs       │  │
│  │   Each item → <div class="uui-faq01_component">       │  │
│  │     Q: .uui-faq01_question h5                         │  │
│  │     A: .uui-faq01_answer .w-richtext                  │  │
│  │                                                        │  │
│  │ <script>  ← IIFE, runs at page load                   │  │
│  │   Iterates .uui-faq01_component → FAQPage JSON-LD     │  │
│  │   Injects into document.head                          │  │
│  │ </script>                                             │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## CMS Fields Required for Full Schema Coverage

**Articles collection** (`6532889f2379aa018d3520b7`):

| Field | Slug | Type | Required | Binds to |
|---|---|---|---|---|
| Title | `name` | PlainText | ✅ | `headline` |
| Slug | `slug` | PlainText | ✅ | URL |
| Blog Post Preview | `blog-post-preview` | PlainText | ✅ | `description` |
| Content | `blog-post-summary` | RichText | ✅ | (visible body, not schema) |
| Main Image | `main-image` | Image | ✅ | `image.url` |
| Alt Text | `alt-text-feature-image` | PlainText | ✅ | `image.caption` |
| Authors (Team Member) | `authors-2` | Reference | ✅ | `author.*` (name, jobTitle, image, email, sameAs) |
| Canonical URL | `canonical-url` | PlainText | ✅ | `mainEntityOfPage.@id` + `@id` (with `#article`) |
| Pillar | `pillar` | Reference → Content Pillars | ✅ | `articleSection` + `isPartOf.name/@id` |
| SEO Keywords | `seo-keywords` | PlainText (comma-separated) | ✅ | `keywords` |
| Article FAQs | `article-faqs` | MultiReference → Article FAQs | ✅ (4–6) | FAQPage `mainEntity` (via JS DOM read) |
| Reading Time | `reading-time` | PlainText | — | (internal, not schema) |
| Tags | `tags-3` | MultiReference | — | (internal) |
| Categories | `categories` | MultiReference | — | (internal) |
| Featured | `featured` | Switch | — | (internal) |

**Content Pillars collection** (`69eb6ca5f842967743d226a2`):

| Field | Slug | Type | Required | Use |
|---|---|---|---|---|
| Name | `name` | PlainText | ✅ | `articleSection`, `isPartOf.name` |
| Slug | `slug` | PlainText | ✅ | (internal) |
| Pillar URL | `pillar-url` | PlainText | ✅ | `isPartOf.@id` (with `https://www.donordock.com` prefix) |
| Description | `description` | RichText | — | (used in pillar cards, not schema) |

**Article FAQs collection** (`69eb6dd45879eb3ff72efb52`):

| Field | Slug | Type | Required | Use |
|---|---|---|---|---|
| Question | `name` | PlainText (max 256) | ✅ | FAQ question |
| Slug | `slug` | PlainText | ✅ | (internal) |
| Answer | `answer-2` | RichText | ✅ | FAQ answer. Note: slug is `answer-2` due to Webflow slug history; display name is "Answer" |

---

## The Seven Locked Pillar Items

| Pillar Name | Item ID | Pillar URL |
|---|---|---|
| Donor Stewardship | `69eb6cb822a81ad28a27e801` | `/smart-steward-method` |
| CRM | `69eb6cd27fa93ec8ab484322` | `/crm` |
| Online Giving | `69eb6ce266456b7917d21f43` | `/online-giving` |
| Fundraising Strategy | `69eb6cec3a55627ab83d8743` | `/fundraising-strategy` |
| Donor Engagement | `69eb6cf56aa6f92a3a162f6b` | `/donor-outreach` |
| AI for Nonprofits | `69eb6cfd66ac68d8d7702716` | `/otto` |
| Donor Retention | `69eb6d05f4bf8b3eeaface0a` | `/donor-retention` |

---

## BlogPosting JSON-LD Template (in the article template `<head>`)

This is the exact JSON-LD embed pasted into the Webflow article template. Every `{{ ... }}` is a Webflow CMS field binding set via the "Add Field" picker in the Designer.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "@id": "{{ Canonical URL }}#article",
  "headline": "{{ Title }}",
  "description": "{{ Blog Post Preview }}",
  "image": {
    "@type": "ImageObject",
    "url": "{{ Main Image }}",
    "caption": "{{ Alt text Feature Image }}"
  },
  "author": {
    "@type": "Person",
    "name": "{{ Authors (Team Member) → Name }}",
    "jobTitle": "{{ Authors (Team Member) → Author's Position }}",
    "image": "{{ Authors (Team Member) → Picture }}",
    "email": "{{ Authors (Team Member) → Email }}",
    "sameAs": [
      "{{ Authors (Team Member) → LinkedIn Profile Link }}",
      "{{ Authors (Team Member) → Twitter Profile Link }}",
      "{{ Authors (Team Member) → Facebook Profile Link }}",
      "{{ Authors (Team Member) → Instagram Profile Link }}"
    ]
  },
  "publisher": {
    "@type": "Organization",
    "name": "DonorDock",
    "url": "https://www.donordock.com",
    "logo": {
      "@type": "ImageObject",
      "url": "https://cdn.prod.website-files.com/63ce9d04b1ff6e36cf514274/63d946401af9adeec7e695b6_DonorDock%20Logo%20-%20Dark.svg"
    }
  },
  "datePublished": "{{ Published On }}",
  "dateModified": "{{ Updated On }}",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "{{ Canonical URL }}"
  },
  "isPartOf": {
    "@type": "WebPage",
    "@id": "https://www.donordock.com{{ Pillar → Pillar URL }}",
    "name": "{{ Pillar → Name }}"
  },
  "articleSection": "{{ Pillar → Name }}",
  "keywords": "{{ seo-keywords }}",
  "inLanguage": "en-US",
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelector": ["h1", ".article-intro", "h2"]
  }
}
</script>
```

---

## FAQPage JS Assembler (in the article template, after the FAQ Collection List)

Placed in an HTML Embed element at the end of the FAQ section. Runs at page load, reads the rendered `.uui-faq01_component` items from the DOM, assembles a valid FAQPage JSON-LD, injects into `<head>`.

```html
<script>
(function() {
  var items = document.querySelectorAll('.uui-faq01_component');
  if (items.length === 0) return;
  var mainEntity = [];
  items.forEach(function(item) {
    var q = item.querySelector('.uui-faq01_question h5') || item.querySelector('.uui-faq01_question');
    var a = item.querySelector('.uui-faq01_answer .w-richtext') || item.querySelector('.uui-faq01_answer');
    if (!q || !a) return;
    var qText = q.textContent.trim();
    var aText = a.textContent.trim();
    if (!qText || !aText) return;
    mainEntity.push({
      "@type": "Question",
      "name": qText,
      "acceptedAnswer": {
        "@type": "Answer",
        "text": aText
      }
    });
  });
  if (mainEntity.length === 0) return;
  var schema = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": mainEntity
  };
  var canonical = document.querySelector('link[rel="canonical"]');
  if (canonical) schema.isPartOf = { "@id": canonical.href + "#article" };
  var s = document.createElement('script');
  s.type = 'application/ld+json';
  s.textContent = JSON.stringify(schema);
  document.head.appendChild(s);
})();
</script>
```

**Why JS-assembled and not inline JSON-LD in a Collection List:** Webflow cannot emit valid JSON from Collection Lists due to the trailing-comma problem. JS assembly guarantees valid JSON with `JSON.stringify()`. Googlebot executes JS during indexing and picks up the injected schema. Verified via Google Rich Results Test.

**Scoping note:** The answer selector is scoped to `.w-richtext` so it skips the "Last updated" footer div that may appear inside `.uui-faq01_answer` alongside the actual answer. If the FAQ card template changes, re-verify the selector scope.

---

## Verification Procedure

After any template change:

1. **View-source check** — confirm BlogPosting JSON-LD renders in `<head>` with all dynamic bindings resolved (no literal `{{ Field }}` strings, no empty strings from null CMS fields).
2. **DOM check** — load a published article, inspect the FAQ section, confirm `.uui-faq01_component` elements have populated `.uui-faq01_question` (h5 text) and `.uui-faq01_answer .w-richtext` (answer text).
3. **Browser DevTools** — in Elements panel, expand `<head>`, find the two `<script type="application/ld+json">` blocks at the bottom (BlogPosting and JS-injected FAQPage).
4. **Google Rich Results Test** — https://search.google.com/test/rich-results → paste URL. Should detect both Article + FAQ items.
5. **If anything fails** — check CMS field completeness first (missing values produce empty schema strings), then template bindings, then the JS assembler.

---

## Test Reference Article

First successfully verified article using this system:
- **URL:** https://www.donordock.com/blog/best-nonprofit-crm
- **Title:** Best Nonprofit CRM Platforms in 2026: The Ultimate Buyer's Guide
- **Pillar:** CRM
- **FAQs:** 5 tied (all Q&A validated in Rich Results Test)
- **Validated:** 2026-04-24

Use this article as the canonical reference when debugging.

---

## Supplementary Schema (NOT in template — requires manual paste)

The template covers only BlogPosting + FAQPage. For these add-ons, spawn the `schema-drafter` subagent and paste output into Webflow Page Settings → Custom Code → Before `</body>`:

- **HowTo** — when the article is truly step-by-step with discrete tool/material/time fields
- **Dataset** — when the article hosts or links to downloadable original data (e.g., State of Stewardship report)
- **VideoObject** — if the article has a featured YouTube video that deserves its own schema entity

Everything else (pillar pages, comparison pages, feature pages, homepage) still requires `schema-drafter` for full custom schema — those URLs do NOT use the article template.
