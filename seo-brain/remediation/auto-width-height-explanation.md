# Why `width="Auto"` / `height="Auto"` is Broken (Not Responsive)

## What you might expect it to do

"Auto" sounds like it means "let the browser decide the size based on viewport / container." In CSS, `width: auto;` does mean exactly that.

## What it actually does in HTML `<img>` attributes

The `<img>` tag's `width` and `height` attributes are **not CSS properties**. They are HTML attributes that must be **non-negative integers** representing intrinsic pixel dimensions. When a browser sees `<img width="Auto">`, it treats "Auto" as an invalid value and ignores the attribute entirely, falling back to "unknown dimensions."

The browser can't know the image's aspect ratio until it fetches the file, decodes it, and measures pixel dimensions. Until that happens, the layout reserves zero space for the image.

## The three problems this causes

### 1. Cumulative Layout Shift (CLS) — Core Web Vitals ranking factor
When the image finally loads, the browser suddenly realizes it's 1200px tall. Everything below the image jumps down by 1200 pixels. That jump is "layout shift." Google measures layout shifts, gives your page a CLS score, and penalizes high-CLS pages in search rankings.

With 68 of 69 images on the homepage missing valid dimensions, the homepage likely has a very high CLS score — this is a known ranking headwind showing up in Google Search Console → Core Web Vitals.

### 2. Lost LCP opportunity
The Largest Contentful Paint (LCP) is measured against when the hero image finishes loading. If the browser can't reserve space for the hero until the full image arrives, LCP is delayed. Pages with explicit `width` and `height` allow the browser to lay out correctly BEFORE the image bytes arrive.

### 3. Responsive images are separate from this
You want images that scale to container width? Do it with CSS, not with `width="Auto"` on the HTML attribute.

Correct pattern:
```html
<img src="hero.webp"
     width="1200"
     height="800"
     style="max-width: 100%; height: auto;"
     loading="eager"
     fetchpriority="high">
```

- `width="1200" height="800"`: intrinsic pixel dimensions — browser reserves a 1200×800 box in the layout immediately, maintains 3:2 aspect ratio if scaled.
- `style="max-width: 100%; height: auto"`: CSS scales the image to fit container width while preserving aspect ratio. Here `auto` IS valid — it's a CSS value, not an HTML attribute value.
- Result: responsive image that scales with browser width AND reserves correct space in layout to avoid CLS.

## Why you want to fix this

1. **SEO rankings.** CLS is a confirmed Google ranking signal. High CLS → lower rankings.
2. **Core Web Vitals in Google Search Console.** Currently very likely showing "Needs improvement" or "Poor" for mobile. This is visible to Google and to anyone who tests your page with PageSpeed Insights.
3. **AI engine ranking.** Perplexity and ChatGPT increasingly use Core Web Vitals as a signal for "is this a quality page worth citing."
4. **Real user experience.** Visitors see the hero image appear, and the entire page jumps. Bad first impression on mobile especially.
5. **CRO (conversion rate optimization).** Layout shifts are correlated with lower conversion rates — people mis-click buttons that moved, leave faster.

## How to fix in Webflow

### Option A: per-image (correct but tedious)
1. Webflow Designer → Homepage
2. Click the hero image
3. In Settings panel on right side, find "Width" and "Height" fields — set to actual pixel dimensions of your image (e.g., 1200 and 800)
4. Repeat for every other image element on the page
5. Apply the CSS above via global image style: `max-width: 100%; height: auto;`

### Option B: Global Webflow fix (recommended)
Enable Webflow's **Responsive Images** feature:
- Project Settings → Hosting tab → look for "Responsive Images" toggle — turn ON
- This auto-generates `srcset` and `sizes` attributes for every uploaded image
- Webflow reads the actual pixel dimensions of each uploaded asset and uses them as the default `width` and `height` attributes on the `<img>` tag
- This will NOT retroactively fix existing images that had `Auto` manually typed, but will prevent new ones from having the problem

### Option C: Find-and-replace audit
Many of the `Auto` values likely came from someone typing into the Designer's Width/Height field when the field was empty. Go through each page template (Article, Feature, Compare, Solution, Homepage, Integration, Team) and remove any `Auto` values from image Width/Height fields, replacing with real numbers. Webflow accepts integer values or empty (for responsive).
