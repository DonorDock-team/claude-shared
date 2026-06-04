---
name: remotion-video-graphics
description: >
  DonorDock motion graphics video production using Remotion (React). Use this skill whenever the user wants to create, edit, or iterate on a DonorDock branded video, motion graphics piece, animated explainer, product walkthrough, or any video content that should look and feel like DonorDock. Also trigger when the user mentions Remotion in the context of DonorDock, or asks to create video slides, animated scenes, or transcript-synced visuals for DonorDock. This skill works alongside the donordock-brand-identity skill (for voice, colors, and visual identity) and the remotion-best-practices skill (for Remotion technical patterns). Always load both companion skills when starting video work.
---

# DonorDock Video Production

This skill defines the design system, layout conventions, and production patterns for creating DonorDock branded motion graphics videos in Remotion. It captures decisions that have been refined through multiple iterations so you don't start from scratch each time.

**Before starting any video work, also read:**
- `donordock-brand-identity` skill -- for colors, voice, typography, and Otto mascot assets
- `remotion-best-practices` skill -- for Remotion-specific technical patterns (animations, sequencing, transitions)
- `references/Visual-Components-Reference.md` (bundled) -- component-level spec, 3-level depth system, cross-platform scaling rules
- `references/dd-visual-example.html` (bundled) -- interactive prototype showing every component at both video and letter scale. Open this to see what the components should look like.
- `references/dd-components.css` (bundled) -- CSS stylesheet with all brand tokens. Useful if generating any HTML preview or non-Remotion output alongside video work.

This skill handles the *how* of DonorDock video design. The brand identity skill handles the *what* (colors, voice, identity). The remotion skill handles the *engine* (React video framework patterns).

---

## Project Location and Structure

The Remotion project lives at `remotion-videos/` inside the DonorDock Claude workspace. All video work happens here -- do not create a separate project.

### Creating a New Video Series

Each video gets its own folder under `src/scenes/` with a kebab-case name, plus a composition file at `src/`:

```
remotion-videos/
  src/
    FundraisingStrategies.tsx       ← composition file (sequences all scenes)
    scenes/
      fundraising-strategies/       ← scene folder
        index.ts                    ← barrel export
        Icons.tsx                   ← SVG icon components for this video
        SceneTitle.tsx
        SceneTruthRelationships.tsx
        ...
```

**Steps to wire up a new video:**

1. Create the scene folder: `src/scenes/<video-name>/`
2. Create an `Icons.tsx` with SVG icon components needed for the video (see Icons section below)
3. Create scene files following the `Scene[Name].tsx` convention
4. Create `index.ts` barrel export for all scenes
5. Create the composition file at `src/<VideoName>.tsx` with `<Sequence>` wrappers
6. Register in `Root.tsx` inside a `<Folder>` with a `<Composition>`:

```tsx
import { FundraisingStrategies } from "./FundraisingStrategies";
import { TEMPLATE_5x4 } from "./templates";

// Inside RemotionRoot:
<Folder name="Fundraising-Strategies">
  <Composition
    id="FS-Full"
    component={FundraisingStrategies}
    durationInFrames={Math.round(totalSeconds * 30)}
    fps={30}
    width={TEMPLATE_5x4.width}
    height={TEMPLATE_5x4.height}
  />
</Folder>
```

### Composition File Pattern

The composition file sequences scenes using a `sec()` helper to convert seconds to frames:

```tsx
const FPS = 30;
const sec = (s: number) => Math.round(s * FPS);

export const FundraisingStrategies: React.FC = () => (
  <>
    <Sequence from={sec(0)} durationInFrames={sec(32)} premountFor={30}>
      <SceneTitle />
    </Sequence>
    <Sequence from={sec(43)} durationInFrames={sec(27)} premountFor={30}>
      <SceneTruthRelationships />
    </Sequence>
  </>
);
```

Always use `premountFor={30}` (1 second) on each Sequence so components can pre-render before they appear.

### Batching for Long Videos

Videos longer than ~5 minutes should be built in batches of 6-10 scenes. This keeps each round of work reviewable. After confirming batch 1 looks good, proceed to batch 2 using the same patterns.

---

## SVG Icons (No Emojis)

Never use emoji characters in video scenes. They render inconsistently across platforms and look unprofessional. Instead, create SVG icon components in an `Icons.tsx` file inside the video's scene folder.

Each icon component accepts `size`, `color`, and optional `strokeWidth` props:

```tsx
interface IconProps {
  size?: number;
  color?: string;
  strokeWidth?: number;
}

export const IconHeart: React.FC<IconProps> = ({
  size = 48,
  color = DD_COLORS.green,
  strokeWidth = 2,
}) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none"
    stroke={color} strokeWidth={strokeWidth}
    strokeLinecap="round" strokeLinejoin="round">
    <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" />
  </svg>
);
```

Use icons from the Lucide icon set (24x24 viewBox, stroke-based) as your design source. Color them with `DD_COLORS` values. When placing icons inside colored circles, use the color at 12% opacity as the background:

```tsx
<div style={{
  width: 120, height: 120, borderRadius: 60,
  backgroundColor: `${tip.color}12`,
  display: "flex", alignItems: "center", justifyContent: "center",
}}>
  <IconHeart size={64} color={tip.color} />
</div>
```

---

## Shared Brand Components

The Remotion project includes pre-built brand components at `src/components/brand/`. **Always use these instead of rebuilding card styles, shadows, and text treatments from scratch.**

### Import
```ts
import {
  DDCard, DDNestedCard, DDFeatureCard, DDFeatureGrid,
  DDHeading, DDHighlightPill, DDContentPill, DDBody, DDCanvasText, DDButton,
  DD_COLORS, DD_SHADOWS, DD_RADII, DD_CONTENT_PILL_STYLES,
} from "./components/brand";
```

### Available Components

| Component | Purpose | Key Props |
|---|---|---|
| `DDCard` | Level 1 primary card | `delay`, `borderRadius`, `padding`, `shadow` |
| `DDNestedCard` | Level 2 card (inside DDCard) | `delay`, `tinted`, `bordered` |
| `DDFeatureCard` | Text-left, visual-right layout | `visual`, `textFlex`, `visualFlex` |
| `DDFeatureGrid` | 2-column card grid | `columns`, `gap` |
| `DDHeading` | Two-tone headline (navy + accent) | `accents: [{text, color}]`, `fontSize` |
| `DDHighlightPill` | Frosted word background | `variant` ("frosted"/"tinted"/"glow"), `accentColor` |
| `DDContentPill` | Info pill for phrases/stats | `variant`, `accentBorder`, `size` ("sm"/"default"/"lg") |
| `DDBody` | Body paragraph text | `fontSize`, `color`, `maxWidth` |
| `DDCanvasText` | Level 0 text on background | `sub` (for subheading), `fontSize` |
| `DDButton` | Purple pill CTA | `outline`, `fontSize`, `padding` |

### Design Tokens
All brand values are in `src/components/brand/tokens.ts`:
- `DD_COLORS` -- every brand color
- `DD_SHADOWS` -- level1, level2, screenshot, otto, buttonHover
- `DD_RADII` -- level1, level2, button, screenshot, pill
- `DD_ACCENT_MAP` -- accent color hex values by name
- `DD_PILL_STYLES` -- frosted, tinted, glow highlight pill variants
- `DD_CONTENT_PILL_STYLES` -- frosted, tinted, glow content pill variants (with shadow)
- `DD_CONTENT_PILL_ACCENT_BORDERS` -- accent border colors for content pills
- `DD_FONT` -- font family, weights, and repo URLs for Silka files

### 3-Level Depth System

Every scene should use the depth hierarchy intentionally:

**Level 0 (Canvas):** Section headings, subheadings, contextual text. No card, no shadow. Use `DDCanvasText`.

**Level 1 (Primary Card):** Main content containers. Use `DDCard` or `DDFeatureCard`. Shadow: `0 4px 20px rgba(0,0,0,0.08)`.

**Level 2 (Nested Card):** Sub-details inside a Level 1 card. Use `DDNestedCard`. Shadow: `0 2px 8px rgba(0,0,0,0.06)`.

The layering creates reading priority: deepest = most important. Use staggered `delay` props (5-12 frames apart) so cards cascade in.

---

## Design System

These values have been tested across multiple rounds of iteration on a 4K canvas. They produce text and graphics that read well on screen and fill the frame without feeling cramped.

### Backgrounds

Use cream (`#FFFCF5`) as the default background for all scenes. This is the DonorDock warm white and creates visual consistency across the entire video. Avoid purple gradients, colored backgrounds, or white (`#FFFFFF`) as scene backgrounds. White cards and containers sit on top of cream, giving them subtle contrast. No exceptions -- always solid cream.

### Typography Scale

Text sizes are relative to canvas width. The values below are calibrated for a canvas around 2700px wide (5:4). For wider canvases (like 3840px 16:9), scale proportionally.

| Element | Size (5:4 @ 2700w) | Size (16:9 @ 3840w) | Weight |
|---|---|---|---|
| Hero heading (title slide) | 280px | 340px | 700 |
| Scene heading | 200-220px | 240-260px | 700 |
| Body / subtitle | 76-80px | 88-96px | 400 |
| Label (uppercase tag) | 44-52px | 52px | 600 |
| Card title | 48-80px | 56-88px | 600 |
| Card body / caption | 40-48px | 48-56px | 400-500 |
| Chart labels | 48-56px | 48-56px | 500-600 |

Headings use navy (`#303034`) by default. Use `DDHeading` with `accents` prop for two-tone color treatment. Body text uses secondary gray (`#56565D`).

Letter spacing on headings: `-1.5px` for any text above 40px. Labels use `letterSpacing: 7-8` with `textTransform: uppercase`.

### Layout Padding

Content should never hug the edges. These padding values keep text readable and shifted away from the left edge:

| Canvas | Padding |
|---|---|
| 5:4 (2700x2160) | `140px 200px` |
| 16:9 (3840x2160) | `160px 300px` |

For centered layouts (title slides, celebration slides), use flexbox centering with no explicit padding -- the content naturally sits in the middle.

### Two-Column Layout

Most informational scenes use a two-column layout: text on the left, visual on the right. Use `DDFeatureCard` for this pattern.

```tsx
<DDFeatureCard
  delay={10}
  visual={<Img src={staticFile("screenshot.png")} style={{ borderRadius: 14, boxShadow: DD_SHADOWS.screenshot }} />}
>
  <DDHeading fontSize={t.heading} accents={[{ text: "Built-in", color: "blue" }]}>
    Built-in Intelligence
  </DDHeading>
  <DDBody fontSize={t.body}>
    Automate your donor management with journeys and insights.
  </DDBody>
</DDFeatureCard>
```

### Otto Mascot

Otto illustrations are PNGs stored in `public/otto/`. When using Otto:
- Always set `width: "auto"` and `objectFit: "contain"` to prevent stretching
- Height range: 500-800px depending on canvas size and scene importance
- Add a subtle float animation: `Math.sin(frame / 20) * 6` on translateY
- Use `drop-shadow` filter for depth: `drop-shadow(0 12px 32px rgba(0,0,0,0.1))`
- Animate entrance with spring + scale interpolation

### Cards and Containers

**Use the shared brand components.** Do not hardcode card styles. Import `DDCard`, `DDNestedCard`, etc. from `./components/brand`.

If you need a card style not covered by the components, derive it from `DD_SHADOWS` and `DD_RADII` in tokens.ts rather than inventing new shadow values.

### Charts and Data Visualization

All chart animations must use `useCurrentFrame()` -- never CSS transitions (Remotion doesn't support them).

- Bar charts: colored bars with percentage labels above, category labels below
- Progress rings: SVG circles with animated stroke-dashoffset, percentage text centered
- Line charts: SVG path with animated point reveal, optional fill area at 15% opacity
- Donut charts: SVG circles with animated segments

Chart components should accept `delay` props so they animate in sequence with the scene.

### Visual Variety

Avoid making every scene a heading + bullet list. The graphics should visualize concepts, not just display text. Aim for a mix of layout types across a video:

**Layout patterns to rotate between:**

- **Horizontal flow / journey**: Icons connected by chevrons (good for processes, progressions)
- **2x2 grid of cards**: Each with icon + title + subtitle, left color border (good for 4 related concepts)
- **3-column vertical cards**: Top color bar, centered icon + text (good for 3 parallel items)
- **Stacked bar chart**: Animated segments with legend (good for showing proportions/costs)
- **Timeline / numbered steps**: Circles with vertical connector line (good for sequential processes)
- **Big centered quote**: Large text in a card with accent bar (good for key quotes)
- **Section header**: Accent line + preview cards for what's coming (good for transitions)

When planning scenes for a video, map out which layout each scene will use and avoid repeating the same layout for consecutive scenes. This keeps the visual experience engaging rather than monotonous.

**Minimum text sizes for on-screen readability (5:4 canvas):**

| Element | Minimum Size |
|---|---|
| Card title / item label | 52px |
| Card subtitle / description | 40px |
| Chart percentage label | 36px |

Anything smaller than 40px becomes hard to read when the 5:4 graphic sits alongside the speaker in a 16:9 video. When in doubt, go bigger.

---

## Animation Conventions

### Entrance Animations

Use Remotion's `spring()` for all entrances. Standard config:
```ts
spring({ frame, fps, delay: N, config: { damping: 200 } })
```

Combine with `interpolate()` for slide-up reveals:
```ts
opacity: interpolate(progress, [0, 1], [0, 1])
transform: `translateY(${interpolate(progress, [0, 1], [30, 0])}px)`
```

**For product explainers / non-transcript videos:** stagger delays by 5-12 frames for sequential elements within a card.

**For transcript-synced videos:** delays must match the SRT timecodes (see Transcript-Synced Animation Timing section above). This typically means delays of 90-900+ frames spread across the scene, not 5-12 frame increments. Only use small staggers (5-12 frames) between a parent container and its heading, not between content items that the speaker mentions at different times.

All brand components (`DDCard`, `DDHeading`, etc.) have built-in entrance animations with a `delay` prop. Example for a product explainer:
```tsx
<DDCanvasText delay={0}>Your Donors, Your Way</DDCanvasText>
<DDCard delay={10}>
  <DDHeading delay={15} accents={[{ text: "Unlimited", color: "blue" }]}>
    Unlimited contacts
  </DDHeading>
  <DDBody delay={20}>Track every relationship in one place.</DDBody>
  <DDNestedCard delay={25}>
    <span>$42,380 monthly giving</span>
  </DDNestedCard>
</DDCard>
```

### Text Components

Use the brand components for text:
- `DDHeading` -- two-tone heading with accent colors (replaces manual color spans)
- `DDHighlightPill` -- frosted pill behind emphasis words
- `DDBody` -- body paragraph with proper styling
- `DDCanvasText` -- Level 0 heading/subheading on background
- `DDButton` -- purple pill CTA

Legacy components (`FadeSlideIn`, `WordByWord`, `CountUp`, `Label`) still work but prefer brand components for new scenes.

### Transcript-Synced Animation Timing

This is the most important animation rule for transcript-synced videos. Each element must animate in when the speaker mentions it -- not all at once at the start of the scene. Viewers watch the speaker and glance at the graphic; if everything appeared already, the graphic feels static and disconnected from what's being said.

**How to calculate delays from an SRT transcript:**

1. Note the scene's start timecode (e.g., scene starts at 1:23 = 83 seconds)
2. For each visual element, find the SRT line where the speaker says it
3. Compute: `delay_in_frames = (element_timecode_seconds - scene_start_seconds) × fps`

**Example** (scene starts at 1:23, fps = 30):
```
Speaker says "restricted funding" at 1:40 → delay = (100 - 83) × 30 = 510 frames
Speaker says "competitive" at 1:49 → delay = (109 - 83) × 30 = 780 frames
Speaker says "time limited" at 1:49 → delay = (110 - 83) × 30 = 810 frames (she says it right after)
Speaker says "reporting" at 1:53 → delay = (113 - 83) × 30 = 900 frames
```

This produces delays spread across the full scene duration (510-900 frames over ~35 seconds), not clustered in the first 2 seconds (which is what happens if you just stagger by 10-15 frames).

**Document timings in each scene file** with a comment block mapping transcript lines to frame delays:
```tsx
/**
 * Truth About Grants
 * Scene starts at 1:23 (83s).
 *
 * Transcript timing (absolute → relative to 1:23):
 * 1:40 "most grants are actually restricted" → Restricted card (frame ~510)
 * 1:49 "Grants are also very competitive" → Competitive card (frame ~780)
 * 1:53 "require continuous research" → Reporting card (frame ~900)
 */
```

The heading and any container card can still appear early (frame 0 and ~60 respectively), since those provide structure. But individual content items (list items, chart bars, cards in a grid) must be timed to the transcript.

### Scene Timing (Composition Level)

Sync scenes to transcript timecodes. Use the `sec()` helper in the composition file and `<Sequence>` components with `premountFor={30}` for smooth transitions.

---

## Templates

The Remotion project includes a `src/templates.ts` file that exports pre-calibrated design tokens for each aspect ratio. Always import from this file rather than hardcoding sizes.

### Using Templates

```ts
import { TEMPLATE_5x4 } from "./templates";
// or
import { TEMPLATE_16x9 } from "./templates";

const t = TEMPLATE_5x4;

// Use in scene styles:
<div style={{ padding: t.padding, fontSize: t.heading }}>
<DDCard borderRadius={t.cardRadius} padding={`${t.cardPaddingV}px ${t.cardPaddingH}px`}>
  <DDHeading fontSize={t.heading}>Your content</DDHeading>
</DDCard>
```

Each template provides: canvas dimensions, typography scale (heroHeading, heading, body, label, cardTitle, cardBody, chartLabel), layout padding, column/card gaps, card styling (radius, padding, shadow), Otto height presets (small/medium/large), and progress ring sizing.

### Available Templates

| Template | Export | Dimensions | Use Case |
|---|---|---|---|
| 5:4 | `TEMPLATE_5x4` | 2700x2160 | Side-by-side video in a 16:9 composition |
| 16:9 | `TEMPLATE_16x9` | 3840x2160 | Standard widescreen video |

Each template also has corresponding scene files (`scenes/` for 16:9, `scenes/v2/` for 5:4) and a registered composition in `Root.tsx`.

When the user asks for a specific ratio, check if a template exists. If it does, duplicate and modify the template scenes rather than building from scratch. If it doesn't, create a new set of scene files following this skill's design system.

### Creating a New Ratio

Use the `scaleTemplate()` helper to derive tokens for any canvas size:

```ts
import { TEMPLATE_5x4, scaleTemplate } from "./templates";

// Scale the 5:4 template to a 1080x1080 square
const TEMPLATE_1x1 = scaleTemplate(TEMPLATE_5x4, 1080, 1080);
```

Then:
1. Add the new template export to `templates.ts`
2. Create a new composition in `Root.tsx` using the template's width/height/fps
3. Create scene files in a new subdirectory (e.g., `scenes/v3/`)
4. Import the template in each scene and use its tokens for all sizes
5. Test that content fits -- headings shouldn't overflow, Otto shouldn't be clipped

---

## Naming Conventions

| Thing | Convention | Example |
|---|---|---|
| Scene folder | `src/scenes/<kebab-case-name>/` | `scenes/fundraising-strategies/` |
| Scene files | `Scene[DescriptiveName].tsx` | `SceneTruthGrants.tsx`, `SceneTipFollowupPlan.tsx` |
| Icon file | `Icons.tsx` inside scene folder | `scenes/fundraising-strategies/Icons.tsx` |
| Barrel export | `index.ts` inside scene folder | `scenes/fundraising-strategies/index.ts` |
| Composition file | `src/<PascalCaseName>.tsx` | `src/FundraisingStrategies.tsx` |
| Folder in Root.tsx | `<Folder name="Kebab-Case">` | `<Folder name="Fundraising-Strategies">` |
| Composition ID | Short prefix + descriptor | `FS-Full`, `DK-Testimonial` |
| Brand components | `src/components/brand/DD[Name].tsx` | `DDCard.tsx` |

---

## Checklist Before Delivering

- [ ] All backgrounds are cream (not white, not purple gradient)
- [ ] Card shadows use `DD_SHADOWS.level1` (`0 4px 20px rgba(0,0,0,0.08)`), not old values
- [ ] Nested cards have lighter shadows than parent cards
- [ ] Text fills the frame well -- minimum 40px for any on-screen text (5:4 canvas)
- [ ] No emoji characters anywhere -- use SVG icon components from Icons.tsx
- [ ] Visual variety -- no two consecutive scenes use the same layout pattern
- [ ] Animation delays are mapped to actual SRT transcript timecodes, not just staggered by 10-15 frames
- [ ] Each scene file has a comment block documenting transcript timing
- [ ] Otto images use `objectFit: contain` and `width: auto`
- [ ] All animations use `useCurrentFrame()` -- no CSS transitions
- [ ] `<Img>` component used (not native `<img>`)
- [ ] `staticFile()` used for public folder assets
- [ ] Composition file wired with correct `<Sequence>` timecodes and `premountFor={30}`
- [ ] Registered in `Root.tsx` inside a `<Folder>` with correct dimensions from template
- [ ] TypeScript compiles clean (`npx tsc --noEmit`)
- [ ] Only import what you use -- no unused imports (TypeScript will flag these)
- [ ] Brand components used where possible (DDCard, DDHeading, etc.)
- [ ] Brand identity skill was consulted for colors and voice
