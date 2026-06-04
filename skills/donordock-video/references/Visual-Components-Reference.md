# DonorDock Visual Components Reference

**Updated:** 2026-03-20
**Source:** Website screenshot audit + existing brand identity skill + Rob feedback session

This is the component-level spec for DonorDock's visual patterns. It bridges the brand identity guidelines (colors, fonts, spacing) with actual reusable components used across the website, videos, presentations, documents, and graphics. Every AI skill that produces DonorDock visuals should reference this file.

All colors referenced here come from the brand identity skill's color palette. Do not invent new colors.

---

## 1. Background System

Use the existing brand background colors from the visual identity guide. The primary backgrounds are:

| Context | Background |
|---|---|
| Video scenes | Cream `#FFFCF5` (keeps text readable on motion) |
| Section alternation (web) | Alternate `#FFFFFF`, `#F7F9F9`, `#FFFCF5`, `#F5F6FF` |
| Cards and containers | `#FFFFFF` sitting on top of any background |
| Dark/Otto sections | `#0C050E` with cream text |

---

## 2. The Layered Card System

DonorDock's visual language is built on depth. Content lives at different visual layers, and the shadow system creates an almost 3D feel. This is the most important design concept in the system.

### Three Depth Levels

**Level 0: Canvas**
The base background. No shadow. This is where headings, subheadings, and supporting text can live directly without a card. Content at this level feels grounded and contextual.

```
Background: Any brand background color (#FFFCF5, #F7F9F9, #F5F6FF, #FFFFFF)
Content: Headings, subheadings, body text, labels, dividers
Shadow: None
```

**Level 1: Primary Card**
The main content container. Floats above the canvas with a clear shadow. Most feature content, data panels, and key information lives here. This is the workhorse.

```
Background: #FFFFFF
Border-radius: 20px (web) / 24-36px (video, scaled to canvas)
Box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08)
Padding: 32px - 40px
Border: none (shadow provides separation)
```

**Level 2: Nested Card**
A card inside a card. Used when information needs sub-grouping, like a data detail panel inside a feature card, or a metric inside a dashboard card. The nested card has a subtler shadow to differentiate from Level 1 without fighting it.

```
Background: #FFFFFF or #F7F9F9 (slightly tinted to differentiate from parent)
Border-radius: 12-16px (tighter than parent)
Box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06)
Padding: 16px - 24px
Border: 1px solid rgba(0, 0, 0, 0.04) (optional, for extra separation)
```

### When to Use Each Level

**Primary use (Level 1 cards):**
- Feature explanations with supporting visuals
- Data or metric panels
- Testimonial cards
- Content that needs to feel like a distinct, digestible block

**Secondary use (Level 0, no card):**
- Section headings and subheadings
- Introductory or contextual text above a card group
- Labels, captions, and meta information
- CTA text and trust signals

**Nested use (Level 2):**
- A product screenshot or data detail inside a feature card
- Sub-metrics inside a dashboard card
- An example or callout inside an explanation card
- Any time you need to show "this belongs to that" through visual nesting

### Visual Hierarchy Rule

The layering creates a clear reading priority: your eye goes to the deepest, most elevated content first (Level 2), then the card containing it (Level 1), then the canvas context around it (Level 0). Use this intentionally. Put the most important information at the deepest level.

---

## 3. Card Components

### 3a. Standard Content Card (Level 1)

The default. Used for feature sections, pricing blocks, info panels.

```
Background: #FFFFFF
Border-radius: 20px (web) / 24-36px (video, scaled to canvas)
Box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08)
Padding: 32px - 40px
Border: none
```

### 3b. Feature Card (Text + Screenshot)

The signature DonorDock layout: text on the left, product screenshot on the right, with the screenshot partially overflowing the card boundary.

```
Layout: flex row
Text side: flex 1, left-aligned, padding 32-40px
Screenshot side: flex 0.6-0.8, positioned to bleed right/bottom edge
Screenshot: border-radius 12px, Level 2 shadow, overflow visible outside card
Card: overflow visible (not hidden) to allow screenshot bleed
```

**Composition rules:**
- Headline sits top-left, large and bold
- Body text below headline, max-width ~60% of card
- Screenshot is angled or straight, overlapping the card's right edge by 10-20%
- The screenshot itself acts as a Level 2 nested element visually

### 3c. Nested Card (Level 2)

Used inside any Level 1 card to create sub-grouping.

```
Background: #FFFFFF or #F7F9F9
Border-radius: 12-16px
Box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06)
Padding: 16px - 24px
Border: 1px solid rgba(0, 0, 0, 0.04) (optional)
```

---

## 4. Headline Text Treatments

### 4a. Standard Headline

```
Font: Silka (fallback Arial, sans-serif)
Color: DD Navy #303034
Weight: 700 (bold) for card headlines, 400 for page H1s
Letter-spacing: -1.5px for large text (40px+)
Line-height: 1.1 - 1.15
Case: Sentence case (capitalize first word + proper nouns only)
Alignment: Left (default), Center (hero/CTA sections only)
```

### 4b. Two-Tone Headline

Used for hero sections, key marketing moments, and feature titles. One or two words get an accent color while the rest stays DD Navy.

**Primary accent colors (use by default):**
```
DD Blue: #0F8FED
DD Purple: #8C2CBF
```

**Secondary accent colors (use when content maps to that pillar):**
```
Outreach Green: #4BBE71 (email, messaging, engagement content)
Giving Yellow: #FBBF4C (donations, giving pages, payment content)
Activation Orange: #DD4E07 (tasks, projects, ActionBoard content)
```

**Pattern:** The "action" or "value" words get the accent color, structural words stay navy.

```
Example (blue): "[blue]Unlimited[/blue] contacts. [blue]Limitless[/blue] impact."
Example (purple): "[purple]Built-in[/purple] Intelligence"
Example (green): "Send [green]personalized[/green] outreach at scale"
Example (yellow): "[yellow]Customizable[/yellow] giving pages"
```

**Rules:**
- Maximum 1-2 accent-colored words per line
- Accent words should be the emotionally resonant or differentiating words
- Never make connecting words (and, the, for, with) accent-colored
- Works best at H1/H2 scale (48px+)
- Blue and purple work in any context
- Green, yellow, orange should match their pillar's subject matter
- All accent colors follow the same styling rules (same weight, same size, just different color)

### 4c. Highlight Pill (Frosted Word Background)

A signature DonorDock treatment. Individual words in a headline get a subtle rounded rectangle behind them.

The pill adapts to its background context:

Every pill variant includes a thin outline border to ensure the pill is clearly visible against its background.

**On colored or tinted backgrounds (cream, light blue, lavender):**
```
Background: rgba(255, 255, 255, 0.75)
Border: 1.5px solid rgba(0, 0, 0, 0.08)
Border-radius: 12px
Padding: 3px 12px
Display: inline-block
```

**On white backgrounds:**
```
Background: #F7F9F9 or #F5F6FF (light blue or lavender tint)
Border: 1.5px solid rgba(0, 0, 0, 0.07)
Border-radius: 12px
Padding: 3px 12px
Display: inline-block
```

**On dark backgrounds (Otto/dark sections):**
```
Background: rgba(255, 255, 255, 0.12)
Border: 1.5px solid rgba(255, 255, 255, 0.15)
Border-radius: 12px
Padding: 3px 12px
Display: inline-block
```

**When to use:** Hero headlines, key value propositions, and anywhere you want to draw attention to 1-2 words. Combine with Two-Tone Headline treatment (accent-colored word inside a pill).

### 4d. Content Pill (Informational Layer)

A larger pill used as an informational layer inside or alongside cards. Unlike the Highlight Pill (4c) which wraps single words in headlines, the Content Pill holds full phrases, feature names, stats, or key points. It acts as a visual container that makes information feel tangible and structured.

Every content pill has a shadow (Level 2) to give it depth, just like cards.

**Base styles (all variants):**
```
Display: inline-flex
Align-items: center
Gap: 8px
Border-radius: 100px (full pill shape)
Padding: 10px 24px
Font: Silka, 600 weight, 15px
Color: #303034 (navy)
Box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06) (Level 2 shadow)
```

**On colored/tinted backgrounds (cream, lavender, light blue):**
```
Background: rgba(255, 255, 255, 0.8)
Border: 1.5px solid rgba(0, 0, 0, 0.08)
Box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06)
```

**On white card surfaces:**
```
Background: #F7F9F9
Border: 1.5px solid rgba(0, 0, 0, 0.07)
Box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06)
```

**On dark backgrounds:**
```
Background: rgba(255, 255, 255, 0.1)
Border: 1.5px solid rgba(255, 255, 255, 0.15)
Color: #FFFCF5 (inverse text)
Box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2)
```

**Accent-bordered variant:**
Add a tinted border that picks up an accent color for emphasis:
```
Blue accent: border-color rgba(15, 143, 237, 0.3)
Purple accent: border-color rgba(140, 44, 191, 0.3)
Green accent: border-color rgba(75, 190, 113, 0.3)
```

**Size variants:**
```
Small (--sm): padding 6px 16px, font-size 12px (for compact lists, tags)
Default: padding 10px 24px, font-size 15px
Large (--lg): padding 14px 32px, font-size 18px (for hero/canvas usage)
```

**When to use:**
- Feature lists inside cards ("Unlimited Contacts", "Built-in Email & Text")
- Stat callouts with accent-colored numbers ("1,284 Active Donors")
- Hero phrases on canvas ("All In One Place")
- Tag-like lists of capabilities (small size)
- Any time you want information to feel contained and structured without using a full card

**When NOT to use:**
- Single words inside headlines (use Highlight Pill instead)
- Full paragraphs of text (use body text)
- Navigation or interactive elements (use buttons)

---

## 5. Body Text Patterns

### Card Body Text (inside Level 1 or Level 2 cards)
```
Font: Silka
Size: 16px (web) / scaled for video canvas
Weight: 400
Color: #56565D (secondary gray)
Line-height: 1.5
Max-width: 90% of card width (don't stretch edge to edge)
```

### Canvas Body Text (Level 0, directly on background)
```
Font: Silka
Size: 18-20px
Weight: 400
Color: #303034 or #56565D
Line-height: 1.6
Max-width: 480px (keeps lines scannable)
```

---

## 6. Grid Layouts

### 2x2 Feature Grid
```
Display: grid
Grid-template-columns: 1fr 1fr
Gap: 24px
Max-width: 1200px
Margin: 0 auto
```
Each cell contains a Feature Card (3b) or Standard Content Card (3a).

### Flexible Column Grid
```
Display: grid
Grid-template-columns: repeat(auto-fit, minmax(280px, 1fr))
Gap: 24px
Max-width: 1200px
```
Adapts from 1 to 4 columns based on content.

---

## 7. Color Pairing Rules

These are the tested combinations. All colors come from the brand identity palette.

| Background | Card BG | Headline | Body | Accent |
|---|---|---|---|---|
| Cream #FFFCF5 | White #FFFFFF | Navy #303034 | Gray #56565D | Any accent color |
| Light Blue #F7F9F9 | White #FFFFFF | Navy #303034 | Gray #56565D | Any accent color |
| White #FFFFFF | Light blue #F7F9F9 or white | Navy #303034 | Gray #56565D | Any accent color |
| Lavender #F5F6FF | White #FFFFFF | Navy #303034 | Gray #56565D | Purple #8C2CBF or Blue #0F8FED |
| Purple #8C2CBF | n/a | Cream #FFFCF5 | White #FFFFFF | White |
| Dark #0C050E | n/a | Cream #FFFCF5 | White #FFFFFF | Purple #8C2CBF |

**Never combine:**
- Navy text on purple background (low contrast)
- Purple body text (reserve purple for CTAs and accents only)
- Two different accent colors in the same headline
- Pillar colors (green, yellow, orange) as body text or backgrounds

---

## 8. Shadow System

The shadow system creates the depth layering. Each level has a distinct shadow that reads as a different elevation.

| Context | Shadow | Level |
|---|---|---|
| Level 1 cards (primary) | `0 4px 20px rgba(0,0,0,0.08)` | Main content cards |
| Level 2 cards (nested) | `0 2px 8px rgba(0,0,0,0.06)` | Cards inside cards |
| Product screenshots | `0 8px 32px rgba(0,0,0,0.12)` | Floating visuals |
| Otto mascot (video) | `drop-shadow(0 12px 32px rgba(0,0,0,0.1))` | Filter shadow for PNGs |
| Buttons (hover) | `0 4px 12px rgba(140,44,191,0.3)` | Purple-tinted on hover |

**Shadow rules:**
- Level 1 shadow is the default. Use it every time you create a card.
- Level 2 shadow is always lighter than its parent. Never make nested shadows heavier than the parent.
- Product screenshots get the heaviest shadow because they need to feel like they're "popping out" of the card.
- No shadow = Level 0 (canvas). Intentionally flat.

---

## 9. Border Radius System

| Element | Radius | Notes |
|---|---|---|
| Level 1 cards | 20px (web) / 24-36px (video) | Soft, approachable |
| Level 2 cards (nested) | 12-16px | Tighter than parent |
| Buttons | 100px | Always pill-shaped |
| Product screenshots | 12-16px | Matches Level 2 feel |
| Highlight pills (text) | 12px | Snug around words |
| Content pills (info) | 100px | Full pill shape |
| Input fields | 12px | |

**Rule:** Nested elements always have a tighter radius than their parent container. This reinforces the layering.

---

## 10. Cross-Platform Scaling

### Remotion/Video Mapping (16:9 at 3840x2160)

| Web Value | Video Value | Scale Factor |
|---|---|---|
| 16px body text | 88-96px | ~5.5x |
| 20px border-radius | 28-40px | ~1.5-2x |
| 24px gap | 80-100px | ~3.5x |
| 32px padding | 120-160px | ~4.5x |
| 48px headline | 240-260px | ~5x |
| Shadow spread/blur | Scale blur by ~2x, keep opacity same | |
| Highlight pill padding | 12px 32px | ~2.5x |

### PDF/Document Mapping (8.5x11 at 72dpi)

| Web Value | PDF Value | Notes |
|---|---|---|
| 16px body text | 11-12pt | Standard body |
| 48px headline | 28-36pt | Scale to page width |
| 20px border-radius | 8-10pt | Proportional |
| 32px padding | 18-24pt | Margins |
| Shadows | Simulate with light gray borders or background tints | True shadows are limited in PDF |

### HTML Artifact Mapping (for dashboards, presentations, web components)

Use web values directly. These components should work at any viewport width from 800px to 1400px. Use the same CSS values documented in the card and typography specs.

---

## 11. Component Naming Convention

For shared components across skills, Remotion, and artifacts:

| Component | Name | Description |
|---|---|---|
| Level 1 card | `DDCard` | White card with Level 1 shadow, primary container |
| Feature card | `DDFeatureCard` | Text-left, screenshot-right with bleed |
| Nested card | `DDNestedCard` | Level 2 card for use inside DDCard |
| Highlight pill | `DDHighlightPill` | Adaptive frosted background behind a word |
| Content pill | `DDContentPill` | Larger pill for phrases, stats, feature tags inside cards |
| Two-tone heading | `DDHeading` | Navy + accent color word emphasis |
| Body text | `DDBody` | Properly styled paragraph text |
| CTA button | `DDButton` | Purple pill button |
| Feature grid | `DDFeatureGrid` | 2-column card layout |
| Canvas text | `DDCanvasText` | Level 0 heading/subheading directly on background |

These names should be used consistently in Remotion components, HTML artifacts, and skill documentation so that any AI referencing this system knows exactly what to build.

---

## 12. Font Files

Silka font files are hosted in the DonorDock shared assets repo:

**Repository:** `DonorDock-team/claude-shared`
**Path:** `assets/fonts/`

| File | Weight | Style |
|---|---|---|
| `Silka-Regular.otf` | 400 | normal |
| `Silka-RegularItalic.otf` | 400 | italic |
| `Silka-Medium.otf` | 500 | normal |
| `Silka-SemiBold.otf` | 600 | normal |
| `Silka-SemiBoldItalic.otf` | 600 | italic |
| `Silka-Bold.otf` | 700 | normal |
| `Silka-Black.otf` | 900 | normal |

**Raw URL pattern:** `https://raw.githubusercontent.com/DonorDock-team/claude-shared/main/assets/fonts/{filename}`

**For Remotion:** Download .otf files into the project's `public/fonts/` directory and use `@font-face` in a global CSS file or `staticFile()` in component styles.

**For HTML artifacts:** Use `@font-face` with the raw GitHub URLs and `format('opentype')`.

**Fallback:** Always declare `font-family: 'Silka', Arial, sans-serif`.
