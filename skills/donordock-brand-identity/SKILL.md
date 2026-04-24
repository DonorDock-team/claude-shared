---
name: donordock-brand-identity
description: >
  DonorDock's brand identity system — voice, visual design, positioning, ICP, and competitive landscape. Use for ANY creative or communications work: writing (articles, emails, social, web copy, ads, newsletters), visual design (presentations, graphics, PDFs, slides), positioning (comparisons, battlecards, objection handling, pitch decks), and brand decisions (taglines, campaigns, naming). Trigger whenever someone mentions DonorDock brand, voice, tone, colors, fonts, messaging, positioning, ICP, competitors, or any content that should look and sound like DonorDock. Also trigger for presentations, social media, comparison content, email campaigns, website pages, or any external-facing DonorDock content — even without saying "brand." If it represents DonorDock, this skill applies.
---

# DonorDock Brand Identity System

This is the single source of truth for DonorDock's brand — voice, visual identity, positioning, ICP, and competitive landscape. Every team member creating anything that represents DonorDock should follow these guidelines.

Before starting any deliverable, identify what you're making and read the relevant reference file(s):

| What you're creating | Read first |
|---|---|
| Written content (articles, emails, social, web copy, newsletters) | `references/voice-and-writing.md` |
| Visual design (graphics, presentations, PDFs, slides, social images) | `references/visual-identity.md` + `references/Visual-Components-Reference.md` |
| Competitive or positioning content (comparisons, battlecards, sales) | `references/positioning-and-competitors.md` |
| Content about or for a specific audience | `references/icp-and-audience.md` |
| Feature-focused content (product pages, demos, feature highlights) | `references/feature-benefit-map.md` |
| HTML artifacts, dashboards, any coded visual output | `references/dd-components.css` (drop-in stylesheet) + `references/Visual-Components-Reference.md` |

For most deliverables, you'll need at least voice + one other reference. For anything external-facing, skim all five.

### Visual Component System

For any visual design work, DonorDock has a component system with reusable patterns:

- **`references/Visual-Components-Reference.md`** -- The spec: 3-level depth system, named components (DDCard, DDHeading, DDHighlightPill, etc.), shadow hierarchy, cross-platform scaling, color pairing rules
- **`references/dd-components.css`** -- Drop-in CSS stylesheet with all brand tokens as CSS custom properties and pre-built classes. Use this when generating HTML artifacts, dashboards, documents, or any non-Remotion visual output.
- **`references/dd-visual-example.html`** -- Interactive HTML prototype showing every component at both 16:9 video and 8.5x11 letter scale. Open this to see what the components should look like. Use it as a visual reference when building anything.

---

## Quality Review System

After creating a draft of any DonorDock content, run it through the appropriate review agents before delivering the final version. This catches brand drift, factual errors, and missed optimization opportunities that are hard to spot as the author.

### When to Use Review Agents

| Content type | Required reviewers | Why |
|---|---|---|
| Blog articles, website pages | Brand Critic + SEO/AEO Strategist + Researcher | Public content needs voice compliance, search optimization, and verified facts |
| Comparison/positioning pages | Brand Critic + SEO/AEO Strategist + Researcher | Competitor claims must be accurate; search visibility matters |
| Social media posts | Brand Critic only | Quick content; voice check is sufficient |
| Marketing emails | Brand Critic only | Voice and tone check; SEO not relevant for email |
| Visual design (graphics, slides, etc.) | Visual Reviewer + Brand Critic (for any copy) | Design compliance plus copy check |
| Help center / how-to content | Brand Critic + Researcher | Voice consistency and accuracy |
| Sales materials / battlecards | Brand Critic + Researcher | Claims must be verifiable; voice must be respectful |

### How the Review Process Works

1. **Create the draft** following the brand guidelines and reference files
2. **Spawn the appropriate review agent(s)** as subagents, passing them the draft content and the relevant agent instructions from `agents/`
3. **Each reviewer returns a structured assessment** with specific issues, suggested fixes, and a verdict (PASS / NEEDS REVISION / MAJOR REWRITE)
4. **Incorporate the feedback** into a revised version
5. **Deliver the final version** -- one revision pass is the standard. Don't loop endlessly.

### Agent Instructions

Each agent has detailed instructions in the `agents/` directory. Read the relevant file before spawning the agent:

| Agent | File | What they check |
|---|---|---|
| **Brand Critic** | `agents/brand-critic.md` | Voice, vocabulary, content guardrails, tone-context match, branded terms |
| **Visual Reviewer** | `agents/visual-reviewer.md` | Colors, typography, buttons, spacing, logo usage, design feel |
| **SEO/AEO Strategist (LIGHT)** | `agents/seo-aeo-strategist.md` | Quick voice + light SEO compliance on a single piece of content. **For deep SEO/pillar/keyword/schema/competitor work, invoke the `donordock-seo-strategist` skill instead** (see Cross-Skill section below). |
| **Researcher** | `agents/researcher.md` | Fact-checking, source verification, competitor accuracy, citation quality |

### Spawning Review Agents

When spawning a review agent, provide:
- The full draft content (or path to the output file)
- The agent instructions (read from the agents/ file)
- The content type and intended audience so the reviewer has context

Example pattern for a blog article:
```
1. Read agents/brand-critic.md, agents/seo-aeo-strategist.md, agents/researcher.md
2. Spawn Brand Critic agent with: the draft + brand-critic instructions
3. Spawn SEO/AEO agent with: the draft + seo-aeo instructions
4. Spawn Researcher agent with: the draft + researcher instructions
   (spawn all three in parallel if subagents are available)
5. Collect all three reviews
6. Apply fixes from all reviews in a single revision pass
7. Deliver the final version
```

For quick content like social posts or short emails, run the Brand Critic review inline (no need for a separate agent) -- just mentally apply the checklist from `agents/brand-critic.md` before delivering.

---

## Cross-Skill: donordock-seo-strategist

This skill (brand-identity) is paired with `donordock-seo-strategist`. Both read the same source-of-truth from `DonorDock-team/claude-shared/seo-brain/`. **Division of labor:**

| Question | Skill |
|---|---|
| Voice, tone, vocabulary, banned words | This skill |
| Visual design, color, typography, logo | This skill |
| Tone by channel (email vs social vs help) | This skill |
| Messaging frameworks, value propositions, brand guardrails | This skill |
| Keyword research, ranking analysis, GSC data | seo-strategist |
| Pillar architecture, content topic strategy | seo-strategist |
| AEO question planning, FAQPage schema | seo-strategist |
| Schema (JSON-LD) requirements, generation, validation | seo-strategist |
| Competitor landscape, comparison page strategy | seo-strategist |
| Content standards (structural rules, internal linking density) | seo-strategist |
| Monthly opportunity reports, content gap analysis | seo-strategist |
| Pre-publish validation (combined) | BOTH — spawn brand-critic + content-validator in parallel |

**Invocation rules:**
- For any content task (article, comparison page, pillar page) → invoke BOTH skills. Brand-identity sets voice; seo-strategist sets pillar/keyword/structure/schema.
- For pure voice/visual questions → this skill alone
- For pure SEO/keyword/schema questions → seo-strategist alone
- For monthly opportunity generation → seo-strategist (spawns its `opportunity-generator` subagent)
- For content validation pre-publish → run both subagents in parallel: this skill's `brand-critic` + seo-strategist's `content-validator`

**The `seo-aeo-strategist` subagent inside THIS skill is intentionally LIGHT.** It does a quick voice + structural-SEO compliance check on a single piece of content. For deep strategic questions ("should we write X?", "what pillar does this fit?", "what's our competitive angle vs Virtuous?"), invoke the full `donordock-seo-strategist` skill.

---

## Quick-Reference Brand Snapshot

**Who we are:** DonorDock is an all-in-one donor management platform built for growing nonprofits. We help lean fundraising teams put all their tools in one place so they can focus on what actually moves the needle — building donor relationships.

**Mission:** We are there for you, so that you can be there for others.

**Origin:** In 2017, co-founders Matt Bitzegaio (developer) and Andrew Lutgen saw that nonprofits were overlooked — getting price breaks on systems that weren't designed for their needs. They built DonorDock to be easy-to-use, purpose-built for growing and mid-sized nonprofits whose staff wear many hats.

**Brand personality:** Think of DonorDock as "Teammate Tyson" — a knowledgeable, warm expert with the heart of a teacher. A bit nerdy in a cool way. If you have a problem, he has a solution or resource. He's a sage: confident and clear, but never arrogant. Empathetic and human.

**Core values:**
1. **Transparency** — Open and honest in communication, internally and with customers
2. **Simplicity** — Pursuing innovative simplicity so everyone can focus on what matters most
3. **Versatility** — Data-driven, adaptable to changing processes, needs, and demands
4. **Empathy** — Decisions grounded in the wellbeing of team members and customers
5. **Confidence** — Focused on big-picture decisions, not shaken by short-term pressures

**What we stand for publicly:** Simplicity. Focus. You don't need to do more — you need to focus on what matters most. Consolidation over complexity.

**What we stay neutral on:** Politics, religious beliefs, partisan positions.

---

## The DonorDock Voice (Quick Rules)

The full voice guide is in `references/voice-and-writing.md`. Here's the cheat sheet:

**We are:** Mentor, Personable, Involved, Confident, Honest/Transparent/Trustworthy

**We are NOT:** Salesy, Standoffish, Dismissive, Arrogant, Unethical

**Our writing should feel:**
1. **Human** — "A real person wrote this, they seem cool and use words I understand."
2. **Mentoring** — "I've learned so much from them, they're like a part of our team."
3. **Clear** — "Everything they do is simple to understand and use."
4. **Empathetic** — "They get us, our nonprofit struggles are seen."
5. **Confident** — "I can trust their opinion, they seem to know their stuff."

**Words we love:** Donor Management, Fundraise, Steward, Smart Stewardship, Smart Steward Method, Smart, Engagement, Easy-to-use, One Place, Platform, Impact, Focus, Grow, Growing, Meaningful, Relationships, Action Board, Otto, Smart Nudges

**Never use:** ActionBoard (wrong — it's "Action Board" as two words), "small nonprofit," "first CRM," "solo ED," "one-person shop," "no platform fees" (we have a 1% platform fee on online donations), "free processing"

**Words we avoid:** Fee, Free tier, Cheap, Simple (use "easy-to-use" instead), Small (use "growing" or "lean"), Product/Software when referring to DonorDock (use "platform")

**Punctuation rule:** Never use em-dashes ( — ) in any public-facing content. Use commas instead, or split into two sentences. This applies to all written content: articles, emails, social posts, web copy, comparison pages, everything.

**Branded term:** Always say "DonorDock" or "DonorDock platform" -- never "product" or "software."

---

## Visual Identity (Quick Rules)

The full visual system is in `references/visual-identity.md`. Here's the essentials:

**Brand colors:**
- DD Purple (CTA): `#8C2CBF` — primary buttons, key accents
- DD Navy (Text): `#303034` — all primary text, headings
- DD Cream: `#FFFCF5` — warm white backgrounds
- DD Light Blue: `#F7F9F9` — hero/section backgrounds

**Platform pillar colors (used for visual language — icons, accents, feature sections):**
- Blue `#0F8FED` — CRM & Donor Management
- Green `#4BBE71` — Outreach & Engagement
- Yellow `#FBBF4C` — Online Giving
- Orange `#DD4E07` — Project Management & Activation

**Typography:**
- Primary font: **Silka webfont** (all headings, body, nav, buttons)
- Otto sub-brand only: **Quicksand**
- H1: 60px, weight 400, letter-spacing -1.8px
- Body: 16px, weight 400, line-height 1.5
- Article body: 20px, weight 400, line-height 1.7

**Buttons:** Pill-shaped (border-radius 100px), DD Purple fill, white text, 600 weight

**Design feel:** Approachable professionalism — clean, airy, soft gradients, generous whitespace. Warm but modern. Nothing sharp or corporate.

**Primary logo:** DonorDock horizontal logo with dark text.
`https://raw.githubusercontent.com/DonorDock-team/claude-shared/main/assets/logos-DonorDock/DonorDock-Logo-Dark.png`

**Logo variants (all on GitHub — prepend base URL):**
- Light (dark backgrounds): `https://raw.githubusercontent.com/DonorDock-team/claude-shared/main/assets/logos-DonorDock/DonorDock-Logo-Light.png`
- All white: `https://raw.githubusercontent.com/DonorDock-team/claude-shared/main/assets/logos-DonorDock/DonorDock-Logo-ALLWHITE.png`
- Icon SVG: `https://raw.githubusercontent.com/DonorDock-team/claude-shared/main/assets/logos-DonorDock/logo-icon.svg`
- Icon PNG (for circles): `https://raw.githubusercontent.com/DonorDock-team/claude-shared/main/assets/logos-DonorDock/logo-icon-forcircle.png`

---

## Positioning Snapshot

**Category:** Donor Management CRM / All-in-One Fundraising Platform

**One-liner:** Your fundraising, all in one place. For lean teams who do it all — one tool that does, too.

**Pricing:** One plan. $500/month. All features included, unlimited contacts. Annual billing. 90-day money-back guarantee. No contracts.

**Plan details (factual, not for positioning copy):** 5 users included, additional users at per-user pricing. Don't call out user counts in marketing or positioning — treat it like email or text message limits (a plan detail, not a selling point). Never say "unlimited users."

**Promise:** One place for everything deserves one plan with everything.

**Trust signals:** 4.8 stars on G2 and Capterra. Trusted by 7,200+ users. G2 Momentum Leader. #1 Easiest Setup, Best Support, Easiest to Use, Easiest Admin, Best Meets Requirements, Easiest to Do Business With.

**Top 3 competitors:** Bloomerang, Network for Good, DonorPerfect. See `references/positioning-and-competitors.md` for detailed positioning against each.

**How we talk about competitors:** We never disparage. We position through clarity about who we're built for and how we're different. We help people find the right fit — even if it's not us. See the competitive reference for specific framing guidance.

---

## Audience Snapshot

**Best-fit customer:** Community-funded nonprofits outgrowing duct-tape systems who want fundraising to feel lighter, not louder.

**ICP sweet spot:**
- $1M–$10M annual revenue (floor: $1M — we don't target below this)
- 15–75 employees, 7–15 CRM users
- 5k–50k contacts
- Individual-giving-heavy fundraising model
- Lean fundraising team (3+ FTE) — not solo operators, not 2-person shops
- Willing to invest $5k+/year to reduce friction

**NOT ICP:** congregational churches (Planning Center / Breeze own that), nonprofits under $1M revenue, solo operators, grant-only or government-funded organizations, enterprise ($50M+) nonprofits needing deep customization. Faith-based nonprofits WITH development programs ARE ICP (parachurch orgs, religious social services, faith-based foundations) — the distinction is donor-development fundraising vs congregational-giving.

**How we talk about our customers:** They are nonprofit leaders and founders who wear many hats. They have tool overload. They are doing good work but are drowning in not enough time, not enough resources.

**How we talk about the sector:** This sector is underserved. Nonprofits provide immense value and need to operate with the same rigor as for-profit businesses — not asking for handouts but for partnership and support to deliver value to their communities.

**How we talk about our team:** We are a lean team, just like those we serve. We reference our values often. We are open, transparent, fun, and dedicated to serving and providing value first.

See `references/icp-and-audience.md` for the full ICP profile, disqualification criteria, and audience-specific tone guidance.

---

## Tone by Context

Our brand has one voice but the tone shifts by audience and content type:

| Context | Tone |
|---|---|
| **New customers** | Excited, Instructive, Personable |
| **Existing customers** | Informative, Straightforward, Personable |
| **Responding to complaints** | Calm, Empathetic, Helpful & Informative |
| **Writing for the public** | Confident, Upbeat, All-inclusive, Encouraging |

| Content type | Tone |
|---|---|
| **How-to content** | Clear steps/points, Instructive, Engaging, Encouraging |
| **Storytelling content** | Heartfelt, Empathetic, Thoughtful |
| **Advertising copy** | Straightforward, Thoughtful, Focused on solving pain points |
| **Social copy** | A little fun, Confident/Intelligent, Thought leadership opinions |

---

## Content Guardrails

These apply to everything created under this brand:

1. **Lead with empathy, close with action.** Acknowledge the reader's reality before offering solutions.
2. **Teach, don't sell.** Position DonorDock as a mentor, not a vendor. Value first, always.
3. **Keep it scannable.** Short paragraphs (1-3 sentences), descriptive headings, bullets for tips. Busy nonprofit people are your readers.
4. **Use second person.** Talk directly to the reader: "you," "your team," "your donors."
5. **Make it feel human.** Contractions are good. Questions are good. A light touch of humor or a vivid analogy is great.
6. **Every CTA should feel like an invitation**, not a command. "See DonorDock in action" not "Buy now."
7. **Always circle back to the mission.** The reader's mission matters most. DonorDock exists to support it.
8. **Never claim to be cheap or free.** We are high-value. One plan, $500/month, everything included. Never say "unlimited users" — user counts are a plan detail, not a positioning point.
9. **Never disparage competitors.** Be truthful about differences. Frame through "who we're for" not "why they're bad."
10. **Social proof is always welcome.** Weave in ratings, G2 badges, user count, and real customer language when natural.

---

## Live Assets & Resources

**GitHub repo (public, no auth needed):**
Base URL: `https://raw.githubusercontent.com/DonorDock-team/claude-shared/main/`

To fetch any file, prepend the base URL to the path below. **When looking for new or updated assets, always read the repo README first** (`https://raw.githubusercontent.com/DonorDock-team/claude-shared/main/README.md`) — it's the index of everything available and is kept up to date as assets are added or reorganized.

| Asset | Repo Path | Notes |
|---|---|---|
| Website sitemap | `sitemaps/website-sitemap.json` | 520+ pages with titles, descriptions, and sections, auto-updated weekly |
| Help center sitemap | `sitemaps/helpcenter-sitemap.json` | 300+ articles with full content, auto-updated weekly |
| YouTube video catalog | `sitemaps/youtube-catalog.json` | 120+ long-form videos from @donordock and @FundraisingLab with categories and people tags, auto-updated weekly (shorts excluded) |
| DonorDock logos | `assets/logos-DonorDock/` | Dark, Light, All-White, Icon (SVG + PNG) |
| Otto illustrations (PNG) | `assets/logos-Otto/PNG/` | 20+ Otto character poses (waving, reading, pointing, multitasking, etc.) |
| Otto illustrations (SVG) | `assets/logos-Otto/SVG/` | Vector versions of Otto |
| Icons | `assets/icons/` | DonorDock icon SVG |
| CMS schema (Webflow) | `skills/ff-article-pipeline/references/cms-schema.md` | Collection schemas, IDs, tags |
| Shared scripts | `scripts/` | Reusable automation scripts |
| Config | `config/skill-settings.json` | Shared settings for skills |

**Website comparison pages:**
- https://www.donordock.com/compare
- https://www.donordock.com/compare/bloomerang-vs-donordock
- https://www.donordock.com/compare/network-for-good-vs-donordock
- https://www.donordock.com/compare/donorperfect-vs-donordock
- https://www.donordock.com/compare/neon-crm-vs-donordock
- https://www.donordock.com/compare/givebutter-vs-donordock

**Social proof source:** https://www.g2.com/products/donordock/reviews

---

## Checklist: Before You Ship

Before publishing or delivering any DonorDock-branded content, verify:

- [ ] Voice sounds human, mentoring, and confident — not salesy or corporate
- [ ] Uses "DonorDock" or "DonorDock platform" — never "product" or "software"
- [ ] Avoids banned words (fee, free tier, cheap, simple, small)
- [ ] Visual design uses brand colors, Silka font, pill-shaped CTAs
- [ ] Competitor mentions are respectful and framed through "who we're for"
- [ ] Includes social proof where natural (ratings, badges, user count)
- [ ] CTA feels like an invitation, not a demand
- [ ] Content leads with empathy for the reader's challenges before offering solutions
- [ ] Appropriate review agents have been run (see Quality Review System above)
- [ ] Facts and statistics are verified with credible sources
- [ ] Public-facing content is optimized for search and AI answer engines
