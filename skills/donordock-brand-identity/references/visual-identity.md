# DonorDock Visual Identity Guide

This reference covers everything you need to create on-brand visual deliverables — presentations, social graphics, PDFs, landing pages, email templates, and any designed asset.

**Required companion read:** Also load the **Visual Components Reference** (`Context/Visual-Components-Reference.md` in the workspace, or bundled in this skill). It defines named, reusable components (DDCard, DDHeading, DDHighlightPill, etc.) with exact CSS values, the 3-level depth system, and cross-platform scaling rules. This file covers *identity*. The components reference covers *how to build things with it*.

---

## Design Philosophy

DonorDock's visual identity communicates **approachable professionalism**. The design says: "We're modern, capable technology — but we're also warm and human."

### Core Design Principles
1. **Warm & Approachable** — Light blue backgrounds, soft shadows, rounded elements. Nothing sharp or corporate.
2. **Clean & Uncluttered** — Generous whitespace, clear hierarchy, breathing room between sections.
3. **Trust-Forward** — Social proof (ratings, avatars, customer counts) should appear on nearly every page or design.
4. **Conversion-Focused** — Purple CTAs are prominent and repeated strategically.
5. **Component-Driven** — Reuse consistent patterns across all deliverables.

---

## Color Palette

### Primary Brand Colors

| Name | Hex | RGB | Usage |
|---|---|---|---|
| **DD Purple** | `#8C2CBF` | rgb(140, 44, 191) | Primary CTA buttons, key accents, the signature brand color |
| **DD Blue** | `#0F8FED` | rgb(15, 143, 237) | Links, highlights, secondary buttons, feature accents |
| **DD Navy** | `#303034` | rgb(48, 48, 52) | All primary text, headings |
| **DD Cream** | `#FFFCF5` | rgb(255, 252, 245) | Warm white backgrounds, card surfaces |
| **DD Light Blue** | `#F7F9F9` | rgb(247, 249, 249) | Hero backgrounds, light section backgrounds |
| **White** | `#FFFFFF` | rgb(255, 255, 255) | Card backgrounds, content areas |

### Secondary / Accent Colors

| Name | Hex | RGB | Usage |
|---|---|---|---|
| **DD Violet** | `#6941C6` | rgb(105, 65, 198) | Accent text, decorative, link hover |
| **DD Coral** | `#FA5B68` | rgb(250, 91, 104) | Attention badges, highlights, alerts |
| **DD Deep Blue** | `#021A7C` | rgb(2, 26, 124) | Dark accent, link text on light backgrounds |
| **DD Link Blue** | `#197BFF` | rgb(25, 123, 255) | Inline link color |
| **DD Lavender BG** | `#F5F6FF` | rgb(245, 246, 255) | Subtle purple-tinted section backgrounds |
| **DD Light Purple BG** | `#FAF5FF` | rgb(250, 245, 255) | Light purple section backgrounds |

### Text Color Hierarchy

| Level | Hex | Usage |
|---|---|---|
| **Primary** | `#303034` | Headings, main body text |
| **Secondary** | `#56565D` | Supporting text, descriptions |
| **Tertiary** | `#475467` | Meta information, subtle text |
| **Muted** | `#6B7280` | Placeholder text, timestamps |
| **Inverse** | `#FFFCF5` | Text on dark/purple backgrounds |

### Background Color Usage

| Background | When to Use |
|---|---|
| White `#FFFFFF` | Default content areas, cards |
| Cream `#FFFCF5` | Warm sections, testimonials, alternating sections |
| Light Blue `#F7F9F9` | Hero areas, primary section backgrounds |
| Lavender `#F5F6FF` | Feature highlights, subtle purple accent sections |
| Light Purple `#FAF5FF` | CTA sections, special callouts |
| DD Purple `#8C2CBF` | Bold CTA bands, footer accents (use white/cream text) |

### Platform Pillar Colors (Visual Language)

These four colors represent the four pillars of the DonorDock platform. Use them for feature-section accents, icons, category badges, and any visual that maps content to a platform area.

| Pillar | Hex | RGB | Usage |
|---|---|---|---|
| **CRM & Donor Management** | `#0F8FED` | rgb(15, 143, 237) | Also the general brand accent blue — use for CRM features, contact profiles, data-related visuals |
| **Outreach & Engagement** | `#4BBE71` | rgb(75, 190, 113) | Email, text messaging, communications, nurture sequences |
| **Online Giving** | `#FBBF4C` | rgb(251, 191, 76) | Giving pages, donations, recurring giving, payment processing |
| **Project Management & Activation** | `#DD4E07` | rgb(221, 78, 7) | ActionBoard, tasks, projects, team coordination |

Use these pillar colors in feature grids, comparison tables, platform overview diagrams, and anywhere you need to visually categorize by platform area. They work best as icon fills, accent bars, or badge backgrounds — not as primary text or CTA colors.

### Otto Sub-Brand Colors (AI Assistant)

| Name | Hex | Usage |
|---|---|---|
| **Otto Dark BG** | `#0C050E` | Dark page backgrounds for Otto content |
| **Otto Purple** | `#8C2CBF` | Shares the main brand purple |
| **Otto Cream Text** | `#FFFCF5` | Heading text on dark Otto backgrounds |
| **Otto Light Purple** | `#FAF5FF` | Light accent sections in Otto context |
| **Otto Font** | Quicksand | Used exclusively for Otto sub-brand, never elsewhere |

---

## Typography

### Font Families

| Font | Usage | Notes |
|---|---|---|
| **Silka webfont** (fallback: Arial, sans-serif) | Everything — headings, body, nav, buttons, labels | The universal DonorDock font |
| **Quicksand** (fallback: Arial, sans-serif) | Otto sub-brand only — Otto page, Otto-themed sections | Never use outside Otto context |

### Type Scale (1.25x ratio)

| Token | Size | Weight | Line Height | Letter Spacing | Heading |
|---|---|---|---|---|---|
| text-5xl | 60px | 400 | 1.1 | -1.8px | H1 — page title (one per page) |
| text-4xl | 48px | 400 | 1.2 | -1.4px | H2 — major section headings |
| text-3xl | 38px | 600 | 1.2 | -1.1px | H3 — sub-sections |
| text-2xl | 31px | 600 | 1.2 | -0.9px | H4 — card titles, feature headers |
| text-xl | 25px | 600 | 1.3 | -0.7px | H5 — small section headers, labels |
| text-lg | 20px | 600 | 1.4 | -0.6px | H6 — fine labels, form headers |
| text-base | 16px | 400 | 1.5 | normal | Default body text |
| text-sm | 14px | 400 | 1.5 | normal | Small/meta text |
| text-xs | 13px | 400 | 1.5 | normal | Fine print, captions |

### Body Text Specifications

| Context | Size | Weight | Line Height | Color |
|---|---|---|---|---|
| Default body | 16px | 400 | 1.5 (24px) | #303034 |
| Article / long-form | 20px | 400 | 1.7 (34px) | #303034 |
| Card descriptions | 16px | 400 | 1.5 (24px) | #56565D |
| Small / meta text | 14px | 400 | 1.5 (21px) | #6B7280 |
| Nav links | 16px | 500 | 1.5 | #303034 |

### Two-Tone Headlines

Headlines can use an accent color on 1-2 key words while the rest stays DD Navy. This draws the eye to the value words.

**Primary accent colors (use by default):**
- DD Blue `#0F8FED` -- works in any context
- DD Purple `#8C2CBF` -- works in any context

**Secondary accent colors (use when content maps to that pillar):**
- Outreach Green `#4BBE71` -- for email, messaging, engagement content
- Giving Yellow `#FBBF4C` -- for donations, giving pages, payment content
- Activation Orange `#DD4E07` -- for tasks, projects, ActionBoard content

Rules: accent the emotionally resonant or differentiating words. Never accent connecting words (and, the, for, with). Maximum 1-2 accent words per line. All accent colors follow the same styling (same weight, same size, just different color). Works best at H1/H2 scale (48px+).

### Highlight Pill (Frosted Word Background)

A signature DonorDock treatment. Individual words in a headline get a subtle rounded rectangle background behind them with a thin outline border.

The pill adapts to its background context:
- On colored/tinted backgrounds: `background: rgba(255,255,255,0.75); border: 1.5px solid rgba(0,0,0,0.08); border-radius: 12px; padding: 3px 12px`
- On white backgrounds: `background: #F7F9F9; border: 1.5px solid rgba(0,0,0,0.07); border-radius: 12px; padding: 3px 12px`
- On dark backgrounds: `background: rgba(255,255,255,0.12); border: 1.5px solid rgba(255,255,255,0.15); border-radius: 12px; padding: 3px 12px`

Combine with Two-Tone Headlines: accent-colored word inside a pill for maximum emphasis.

### Content Pill (Informational Layer)

A larger pill used for phrases, feature names, stats, or key points inside or alongside cards. Unlike the Highlight Pill (single words in headlines), this acts as a visual container for structured information. Every content pill has a Level 2 shadow.

- Base: `border-radius: 100px; padding: 10px 24px; font-weight: 600; font-size: 15px; box-shadow: 0 2px 8px rgba(0,0,0,0.06)`
- On colored backgrounds: `background: rgba(255,255,255,0.8); border: 1.5px solid rgba(0,0,0,0.08)`
- On white surfaces: `background: #F7F9F9; border: 1.5px solid rgba(0,0,0,0.07)`
- On dark backgrounds: `background: rgba(255,255,255,0.1); border: 1.5px solid rgba(255,255,255,0.15); color: #FFFCF5`
- Optional accent border: `border-color: rgba(accent, 0.3)` for blue/purple/green emphasis
- Sizes: sm (6px 16px, 12px font), default, lg (14px 32px, 18px font)

Use for: feature lists, stat callouts, hero phrases, tag-like capability lists. Not for single words in headlines (use Highlight Pill).

### Font Files

Silka font files are in the DonorDock shared assets repo: `DonorDock-team/claude-shared/assets/fonts/`

Available weights: Regular (400), Medium (500), SemiBold (600), Bold (700), Black (900). Plus Regular Italic and SemiBold Italic.

Raw URL: `https://raw.githubusercontent.com/DonorDock-team/claude-shared/main/assets/fonts/Silka-{Weight}.otf`

---

## Spacing System (8px Grid)

| Token | Value | Usage |
|---|---|---|
| space-1 | 8px | Icon gaps, tight element spacing |
| space-2 | 16px | Element spacing, heading-to-body gap |
| space-3 | 24px | Card padding, grid gaps |
| space-4 | 32px | Component internal padding |
| space-5 | 48px | Compact section padding |
| space-6 | 64px | Standard section padding |
| space-7 | 80px | Hero section padding |
| space-8 | 96px | Generous section padding |

### Container Widths

| Type | Max Width | Padding |
|---|---|---|
| Main container | 1200px | 24px horizontal |
| Narrow container | 800px | 24px horizontal |
| Wide container | 1400px | 24px horizontal |
| Full-width | 100% | 0px |

---

## Button Styles

### Primary CTA Button (Purple Pill)
```
Background: #8C2CBF (DD Purple)
Text: White
Font: Silka webfont, 16px, weight 600
Padding: 14px 28px
Border-radius: 100px (pill shape)
Border: none
```

### Secondary Button (Outline Pill)
```
Background: transparent
Text: #303034 or DD Blue
Border: 1.5px solid currentColor
Border-radius: 100px
Padding: 14px 28px
Font weight: 600
```

### Tertiary / Ghost Button
```
Background: transparent
Text: DD Blue or DD Purple
Border: none
Font weight: 600
Often paired with an arrow icon →
```

### Tag / Filter Buttons
```
Background: #F7F9F9
Text: #303034
Border-radius: 100px
Font: 14px
Padding: 8px 16px
Border: 1px solid #D8D8D8
```

---

## Card Styles & Depth System

DonorDock visuals use a 3-level depth system that creates a layered, almost 3D feel. Content lives at different elevations, and the shadow hierarchy communicates importance.

### Level 0: Canvas (No Card)
Headings, subheadings, and contextual text live directly on the background with no card container. This grounds the scene and provides context for the cards above it.

### Level 1: Primary Card
The main content container. Most feature content, data panels, and key information lives here.
```
Background: #FFFFFF
Border-radius: 20px
Box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08)
Padding: 32px - 40px
Border: none (shadow provides separation)
```

### Level 2: Nested Card
A card inside a Level 1 card. Used for sub-grouping: a data detail inside a feature card, a metric inside a dashboard, an example inside an explanation.
```
Background: #FFFFFF or #F7F9F9 (tinted to differentiate from parent)
Border-radius: 12-16px (tighter than parent)
Box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06)
Padding: 16px - 24px
Border: 1px solid rgba(0, 0, 0, 0.04) (optional)
```

### Shadow Hierarchy
| Context | Shadow |
|---|---|
| Level 1 cards (primary) | `0 4px 20px rgba(0,0,0,0.08)` |
| Level 2 cards (nested) | `0 2px 8px rgba(0,0,0,0.06)` |
| Product screenshots | `0 8px 32px rgba(0,0,0,0.12)` |
| Buttons (hover) | `0 4px 12px rgba(140,44,191,0.3)` |

Nested elements always have a tighter border-radius and lighter shadow than their parent.

### Overflow
Overflow: hidden (for cards with images), visible (for cards with screenshot bleed effects)

---

## Image Treatment

| Context | Border Radius | Shadow | Notes |
|---|---|---|---|
| Person photos (hero) | 50% (circle) | none | Often with decorative icon circles |
| Product screenshots | 12–16px | medium drop shadow | Sometimes in device mockup frames |
| Article thumbnails | 12px | none | object-fit: cover |
| Team photos | 50% (circle) | none | Equal sizing |

---

## Layout Patterns

### Hero Section
- Center-aligned or left-aligned headline with product screenshot on right
- Light blue (#F7F9F9) or gradient background
- Social proof strip (avatars + stars + "Trusted by 7,200+ users") below CTA
- Primary purple CTA + secondary outline CTA
- Feature category tags/chips below the subheadline

### Feature Section
- H2 headline + supporting paragraph
- 2-3 column grid of feature cards
- Each card: icon/illustration + H4 title + short description
- Light background alternating with white

### Social Proof Section
- G2 badge row (Easiest Setup, Best Support, Easiest to Use, etc.)
- Star ratings with counts (4.8 stars, G2 and Capterra)
- Customer testimonial cards or scrolling testimonial strip
- "Voted #1 for Growing Nonprofits" heading pattern

### CTA Section
- Purple or light purple background
- Clear headline: "Start building meaningful donor relationships today."
- Primary CTA button centered
- Trust reassurances below: "No contracts. Cancel anytime. 90-day money-back guarantee."

### Pricing Section
- "One place for everything deserves one plan with everything"
- Single plan card with feature checklist (purple checkmarks)
- Trust signals: All features included, Unlimited contacts, Cancel anytime, 90-day money-back guarantee, White-glove data migration, Human support

---

## Logo Usage

### Primary Logo
The horizontal DonorDock logo with dark text is the primary mark. Use it on light backgrounds.

**GitHub URLs (direct download — no auth needed).** For the latest asset inventory, always check the repo README at `https://raw.githubusercontent.com/DonorDock-team/claude-shared/main/README.md` — new logos, Otto poses, and icons are added there first.

| Variant | URL |
|---|---|
| **Primary (dark text)** | `https://raw.githubusercontent.com/DonorDock-team/claude-shared/main/assets/logos-DonorDock/DonorDock-Logo-Dark.png` |
| **Light (for dark BGs)** | `https://raw.githubusercontent.com/DonorDock-team/claude-shared/main/assets/logos-DonorDock/DonorDock-Logo-Light.png` |
| **All white** | `https://raw.githubusercontent.com/DonorDock-team/claude-shared/main/assets/logos-DonorDock/DonorDock-Logo-ALLWHITE.png` |
| **Icon (SVG)** | `https://raw.githubusercontent.com/DonorDock-team/claude-shared/main/assets/logos-DonorDock/logo-icon.svg` |
| **Icon (PNG, for circles)** | `https://raw.githubusercontent.com/DonorDock-team/claude-shared/main/assets/logos-DonorDock/logo-icon-forcircle.png` |
| **DonorDock icon** | `https://raw.githubusercontent.com/DonorDock-team/claude-shared/main/assets/icons/donordock-icon.svg` |

**Otto illustrations (20+ character poses — PNG):**
Base path: `https://raw.githubusercontent.com/DonorDock-team/claude-shared/main/assets/logos-Otto/PNG/`

| Pose | Filename |
|---|---|
| Waving (friendly greeting) | `Otto-waving.png` |
| Pointing right | `Otto-pointing-right.png` |
| Pointing left | `Otto-pointing-left.png` |
| Pointing up | `Otto-Pointing-up.png` |
| Pointing down | `Otto-Pointing-Down.png` |
| Headset on (support) | `Otto-Headset-On.png` |
| Holding heart | `Otto-holding-heart.png` |
| Holding envelope & pencil | `Otto-holding-envelope-and-pencil.png` |
| Holding 8 letters | `Otto-holding-8-letters.png` |
| Holding integrations | `Otto-holding-8-Integrations-NEW.png` |
| Holding sign (looking down) | `Otto-holding-sign-looking-down.png` |
| Holding buoy | `Otto-Holding-onto-buoy.png` |
| Juggling tasks | `Otto-Juggling-tasks.png` |
| Multitasking | `Otto-multitasking.png` |
| On a boat | `Otto-On-A-Boat.png` |
| Dancing happy | `Otto-dancing-happy.png` |
| Reading | `Otto-Reading.png` |
| Working on laptop | `Otto-working-on-laptop.png` |
| Sitting sad | `Otto-Sitting-Sad.png` |
| Neutral (no smile) | `Otto-Neutral-no-smile.png` |

SVG versions are also available at `assets/logos-Otto/SVG/`.

### Logo Rules
- Always maintain clear space around the logo (minimum: height of the icon mark)
- Never stretch, rotate, or alter the logo proportions
- Never place the dark logo on a dark background (use light or all-white variant)
- The logo icon can be used alone in small spaces (favicons, app icons, social profile pics)
- Never recreate the logo in a different font

---

## Illustration Style

DonorDock primarily uses **product screenshots** to show the platform in context. When conceptual or decorative illustrations are needed (for abstract concepts, emotions, or non-product visuals), follow this style:

**Target style:** Clean, flat vector illustrations with soft rounded shapes — consistent with the brand's warm, approachable feel. Think modern SaaS illustration style, not corporate clip art.

**Guidelines:**
- Use the DonorDock color palette (purple, blue, cream, light blue) as the illustration palette
- Soft, rounded shapes — no hard edges or angular geometry
- Flat or subtly layered (light depth via overlapping shapes, not heavy 3D)
- People illustrations should feel inclusive and diverse, with simple/abstract features (not photorealistic)
- Conceptual metaphors are welcome (e.g., a lighthouse for guidance, a compass for direction, connected nodes for relationships)
- Keep it simple — illustrations should support the message, not distract from it

**What to avoid:**
- Isometric or 3D illustration styles (too technical/corporate)
- Hand-drawn or sketchy styles (doesn't match the clean brand)
- Overly detailed or photorealistic illustrations
- Generic "people holding a giant phone" SaaS clichés
- Illustrations that use off-brand colors

**When to use product screenshots vs. illustrations:**
- Product screenshots: When showing a specific feature, workflow, or UI element — always real DonorDock UI
- Illustrations: For abstract concepts (donor relationships, data growth, consolidation), emotional moments, or section decoration
- Icons: For feature lists, benefit grids, and navigation elements

---

## Photography & Imagery Style

DonorDock uses minimal photography. When photos are used, they should feel **real, warm, and authentic** — never like stock photography.

**When to use photography:**
- Testimonial sections (real customer photos when available)
- About/team pages (real team photos)
- Blog articles illustrating real nonprofit scenarios
- Social media featuring the team or customers

**Photo guidelines:**
- Authentic and candid over posed and staged
- Real people in real nonprofit environments (community events, offices, volunteer activities)
- Warm, natural lighting — avoid harsh studio lighting
- Diverse representation across age, race, gender, and nonprofit type
- If stock is unavoidable, choose photos that feel documentary/editorial — never the "people in business suits high-fiving" genre

**What to avoid:**
- Generic stock photos (especially "diverse business team smiling at laptop")
- Photos with heavy filters or unnatural color grading
- Photography that feels corporate, cold, or overly polished
- Photos that don't represent the nonprofit community DonorDock serves
- Low-resolution or pixelated images

**Image treatment:** Product screenshots should have 12-16px border radius and a medium drop shadow. Person photos in hero sections use full circles (50% radius). Article thumbnails get 12px radius.

---

## Iconography Style

DonorDock uses **filled/solid icons** in the brand color palette.

**Icon specifications:**
- Style: Solid/filled (not outline or line icons)
- Color: DD Purple (`#8C2CBF`), DD Blue (`#0F8FED`), or DD Navy (`#303034`) depending on context
- Size: 24px default, scale up to 32px or 48px for feature grids and hero sections
- Corner radius: Rounded to match the brand's soft, approachable feel
- Weight: Medium — not too thin, not too heavy

**Usage patterns:**
- Feature grids: Purple or blue filled icons at 32-48px, centered above feature titles
- Benefit lists: Smaller 24px icons inline with text, typically purple
- Navigation: 20-24px icons, navy color
- Checkmarks in pricing/comparison lists: Purple filled checkmarks (✓)

**What to avoid:**
- Outline/line-style icons (inconsistent with the filled brand style)
- Icons with too much detail or multiple colors within a single icon
- Mixing icon libraries or styles within the same page/design
- Icons that look technical or developer-oriented (gears, code brackets) — lean toward human/relationship metaphors

---

## Color Usage Rules

Beyond the palette itself, here's how colors should be applied:

**DD Purple (`#8C2CBF`):**
- Primary CTAs — this is the click-here color. Use it for the most important action on any page or design.
- Key accents and emphasis elements
- Never use for body text or backgrounds on light pages (too intense)
- On dark backgrounds, it works as a button fill or accent

**DD Blue (`#0F8FED`):**
- Secondary actions, links, and interactive elements
- Feature highlights and accent elements
- "Learn more" style links and secondary buttons
- Can be used for emphasis text sparingly

**DD Navy (`#303034`):**
- All body text and headings — this is the reading color
- Never use pure black (#000000) — DD Navy is warmer and more approachable

**Backgrounds — the rhythm:** Alternate between White, Light Blue, Cream, and Lavender to create visual rhythm between sections. Never stack two sections with the same background color.

**Dark mode / dark sections:** Only for Otto sub-brand content and special CTA sections. Use DD Purple or near-black (`#0C050E`) backgrounds with cream (`#FFFCF5`) text.

**Accessibility:** DD Navy text on white/light backgrounds exceeds WCAG AA contrast requirements. Always verify contrast when using colored text on colored backgrounds.

---

## What We Never Do Visually

- Use fonts other than Silka (or Quicksand for Otto only)
- Use system-ui or generic sans-serif where Silka should appear
- Create designs that feel corporate, sterile, or aggressive
- Use sharp corners on buttons (always pill-shaped, 100px radius)
- Use colors outside the defined palette
- Use pure black (#000000) for text — always DD Navy (#303034)
- Crowd the design — whitespace is a feature, not a waste
- Skip social proof on conversion-focused pages
- Use generic stock photography — prefer product screenshots, real photos, or illustrations
- Mix icon styles (outline + filled) within the same design
- Place dark logos on dark backgrounds
- Use gradients that aren't in the brand palette
- Create anything that could be mistaken for a different brand's visual language
- Use abstract decorative circles, blobs, or geometric shapes as background elements. These are a common AI-generation cliche and are not part of DonorDock's design system. Visual interest should come from the color palette, whitespace, brand assets (Otto, logos), and clean typography.
- Use em-dashes ( — ) in any text that appears in visual designs. Use commas or split the sentence instead.
