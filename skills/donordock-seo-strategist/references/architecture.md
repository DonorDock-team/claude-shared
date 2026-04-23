# Architecture — how this skill interacts with the DonorDock skill ecosystem

This document is the canonical map of how `donordock-seo-strategist` relates to other skills and the shared source-of-truth (`seo-brain/` repo).

---

## Shared source-of-truth: `seo-brain/` repo

All DonorDock SEO/AEO/brand-positioning knowledge lives at `DonorDock-team/claude-shared/seo-brain/`:

```
seo-brain/
├── strategy/              ← Human-curated. Locked. Both skills read from here.
│   ├── brand-positioning.md
│   ├── pillars.md
│   ├── keyword-universe.md
│   ├── aeo-questions.md
│   ├── content-standards.md
│   ├── competitor-landscape.md
│   ├── icp-intent-map.md
│   ├── eeat-signals.md
│   └── state-of-stewardship-report.md
├── audits/                ← Dated audit snapshots (baseline + monthly)
├── opportunities/         ← Monthly opportunity reports (Phase 5+)
├── tracking/              ← SERP + AI citation tracking (Phase 5+)
├── remediation/           ← Open fix items
└── registry-enrichment/   ← SEO metadata layered over sitemaps/
```

**Rule:** Never duplicate content from `seo-brain/` inside any skill. Skills reference; they don't copy. When strategy changes, update the repo once — all skills see it next session.

---

## Skill-to-skill interaction map

### donordock-brand-identity (voice, visual, messaging ICP)

**Relationship:** parallel skill with clear division of labor.

**Brand-identity owns:**
- Voice and tone guidelines
- Vocabulary and banned words
- Visual design (colors, typography, components)
- Tone-by-channel (email, social, web, help)
- Messaging frameworks
- Brand-safety checks
- Existing subagents: brand-critic, visual-reviewer, researcher, seo-aeo-strategist (LIGHT SEO compliance check)

**SEO-strategist owns:**
- Pillar architecture
- Keyword research and priorities
- AEO question universe
- Schema requirements
- Competitor landscape
- Structural content standards
- Monthly opportunity generation
- GSC analysis

**Invocation pattern:**
- When creating any content: invoke BOTH skills. Brand-identity sets voice/tone. SEO-strategist sets pillar/keyword/schema/structure.
- When reviewing a draft: run BOTH skills' review subagents. Brand-critic for voice; content-validator for structure.
- When asked a pure voice question: defer to brand-identity, don't interfere.
- When asked a pure SEO question: defer to this skill, don't interfere.

**Existing seo-aeo-strategist subagent in brand-identity:** keep it for quick tactical checks on a single piece of content (voice + light SEO). For strategic questions and deep validation, invoke this full skill.

### ff-article-pipeline (auto-generated podcast-to-article pipeline)

**Relationship:** this skill is a dependency for ff-article-pipeline (Phase 4 integration).

**Integration plan (Phase 4):**
1. At pipeline start, load both brand-identity and seo-strategist skills
2. Topic mapping step: seo-strategist's strategy-advisor subagent maps episode topic to pillar + keyword cluster + AEO question set
3. Draft generation step: brand-identity provides voice; seo-strategist provides structural requirements (TL;DR, question-format H2s, FAQ from aeo-questions.md, pillar link, schema stub)
4. Pre-publish review: spawn brand-critic (voice) + content-validator (structure) + researcher (facts) in parallel
5. Post-publish: seo-strategist's content-validator writes to registry-enrichment with the new URL's pillar/cluster/intent assignment

**Rule:** ff-article-pipeline should NOT duplicate strategy logic. It invokes this skill for strategy decisions.

### write-like-matt / write-like-rob (first-person content)

**Relationship:** brand voice skills. Defer SEO to this skill only when content is search-intended.

**Invocation pattern:**
- LinkedIn posts, personal essays, podcast show notes → brand-identity + write-like-* only. No SEO strategist needed.
- Article bylined by Matt or Rob on the DonorDock site → all three: brand-identity + write-like-* + seo-strategist.
- Thought-leadership piece destined for the /articles/ directory → seo-strategist runs pillar/keyword assignment even if voice is first-person founder.

### donordock-helpcenter (product support content)

**Relationship:** minimal interaction. Help-center content is customer-facing, rarely SEO-priority.

**Invocation pattern:**
- Normal help article → helpcenter skill alone
- Help article that doubles as a pillar/cluster piece (e.g., "how to set up recurring donations" — rankable topic) → also invoke seo-strategist for schema + pillar tagging
- HowTo schema on tutorial-type help articles → seo-strategist's schema-drafter provides the JSON-LD

### donordock-import-mapper, docx, pptx, xlsx, remotion-video-graphics, pdf

**Relationship:** orthogonal. These are content-format skills, not content-strategy skills.

**Invocation pattern:**
- A PDF being generated for public consumption may need schema (CreativeWork, Dataset for reports) → seo-strategist's schema-drafter
- Video for YouTube embedded on a page → schema-drafter generates VideoObject
- Otherwise these skills operate independently

### Claude Rank suite (rank-audit, rank-geo, rank-aeo, etc.)

**Relationship:** this skill orchestrates them strategically.

**Invocation pattern:**
- Monthly audit cadence (Phase 6) → seo-strategist triggers rank-audit, parses output, writes summary to `seo-brain/audits/YYYY-MM/`
- Ad-hoc competitive query → seo-strategist spawns rank-compete subagent for a named competitor
- URL-specific citability check → seo-strategist spawns rank-citability subagent
- The strategist NEVER embeds the rank suite's logic — it invokes them

---

## Decision tree: which skill do I invoke?

```
Is it about DonorDock?
│
├─ No → don't use these skills
│
└─ Yes → What kind of question?
    │
    ├─ Voice / tone / vocabulary / brand copy → brand-identity
    ├─ Visual / color / typography / logo → brand-identity
    ├─ Channel-specific copy (email/social/help) → brand-identity + channel skill
    ├─ Keyword / ranking / GSC / pillar / schema / competitor SEO → seo-strategist
    ├─ Content validation (pre-publish review) → BOTH skills
    ├─ Content creation (new article/page) → BOTH skills
    ├─ Monthly opportunity report → seo-strategist
    ├─ Help article draft → helpcenter (+ seo-strategist IF it's pillar-targeted)
    ├─ Podcast article from transcript → ff-article-pipeline (invokes BOTH skills internally)
    ├─ Linkedin/personal post by Rob or Matt → brand-identity + write-like-*
    ├─ Visual asset (slide, graphic, PDF) → brand-identity + format-skill (pptx/docx/pdf)
    └─ Custom data analysis / SEO research → seo-strategist (uses GSC MCP, GitHub MCP)
```

---

## Rules of engagement

1. **This skill never overrides brand-identity on voice.** If a SEO recommendation conflicts with a brand voice rule, brand-identity wins.
2. **Brand-identity never overrides this skill on schema or pillar assignment.** If brand-identity's seo-aeo-strategist subagent suggests something that conflicts with `seo-brain/strategy/`, this skill's content-validator catches it and flags.
3. **Both skills read the same brand-positioning.md.** If either notices the rules drift, update the repo — never update one skill without the other.
4. **When in doubt, both skills can be invoked.** The redundancy catches gaps. Don't let either skill try to answer outside its scope.
5. **GSC MCP access is available only via this skill.** Brand-identity does not use GSC. If brand-identity needs a ranking data point, it invokes this skill.

---

## Future expansion

- **Phase 5:** AI citation tracking across ChatGPT/Perplexity/Claude/Gemini/AIO will be a new subagent under this skill (`agents/ai-citation-tracker.md`, not built yet).
- **Phase 6:** scheduled automation (monthly audit + weekly SERP + daily citation tracking) triggers this skill's agents.
- **Phase 7:** HTML dashboard generator reads from this skill's outputs.
- **Phase 8:** Asana integration for approvals feeds from this skill's opportunity-generator.

All future Phase 5-8 additions will be subagents under this skill or separate but cross-referenced skills.
