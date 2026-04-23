# E-E-A-T Signals

**Locked:** 2026-04-23
**Owner:** Rob Burke (CMO)
**Refresh:** Quarterly (author credentials) / Annually (research asset)
**Source:** Phase 1 citability audit + competitor audits + brand-positioning.md

How DonorDock demonstrates **Experience, Expertise, Authoritativeness, Trust** for Google Search Quality Raters and for AI engines evaluating citation-worthiness. This doc is the canonical plan for E-E-A-T across Phase 2-8.

---

## Why E-E-A-T is a top-3 Phase 2 priority

Phase 1 audits showed DonorDock's content is citable-quality but entity/author signals are weak. Competitor audit findings:
- DonorPerfect publishes 648 blog posts with **zero author bylines** — easy leapfrog.
- Bloomerang has strong E-E-A-T on articles (named authors, consistent bylines, long-running "Ask an Expert" series).
- Virtuous publishes named authors + Chief AI Officer bylined content.
- Keela has Timi Paccioretti as consistent educator byline.

DonorDock has named founders (Matt, Andrew) + named executives (Rob, Noah, Bridgette, Sami, Scott) but E-E-A-T signals are inconsistent: bylines partial, /team/* pages thin, no /authors/ schema, no knowsAbout claims, no third-party validation surfaces.

**E-E-A-T is DonorDock's most under-leveraged owned asset.**

---

## Named experts / authors

| Person | Role | Expertise (knowsAbout) | Primary pillars | LinkedIn | Articles authored |
|---|---|---|---|---|---|
| Matt Bitzegaio | Co-founder, CEO | Nonprofit technology, donor management, mid-sized/growing nonprofit operations, Smart Stewardship, founder story | All | (link) | 10+ |
| Andrew Lutgen | Co-founder | Product strategy, nonprofit software architecture | CRM, AI for Nonprofits | (link) | fewer |
| Rob Burke | CMO | SEO, nonprofit marketing, Smart Stewardship methodology, brand positioning, AEO | Donor Stewardship, Donor Engagement, Fundraising Strategy | (link) | 10+ |
| Noah Barnett | Chief Strategy Officer | Nonprofit strategy, AI for nonprofits, Otto product narrative | Fundraising Strategy, AI for Nonprofits | (link) | 5+ |
| Bridgette Bitzegaio | Customer Success Manager | Customer success, onboarding, donor stewardship practice, CRM operations, fundraising best practices | Donor Stewardship, Donor Retention, CRM | (link) | 0 (expert voice; ghost-write or record podcast guest spots; target authored bylines in Q3) |

### Departed team members (historical authorship)
These people formerly worked at DonorDock and authored articles still live on the site. Policy decision needed for each:
- **Elisha Ford** — departed. Articles remain live.
- **Sami Bedell-Mulhern** — departed. Articles remain live.
- **Sarah O'Brien** — departed. Articles remain live.
- **Scott Holdman** — departed. Articles remain live.

**Policy options for departed authors:**
1. **Preserve byline + add "Former" note** (default recommendation). E-E-A-T retained; integrity preserved; reader sees "Written by Elisha Ford, former Customer Success Manager at DonorDock."
2. **Reassign byline** to current team member who now owns that expertise area (e.g., Bridgette for stewardship content originally by Elisha).
3. **Ghost to "DonorDock Team"** (worst for E-E-A-T — avoid).

**Recommendation:** Go with Option 1 for articles still earning meaningful traffic, Option 2 for articles under heavy revision. Never Option 3 for content on the Smart Stewardship pillar — E-E-A-T matters most there.

**Action for Rob:** Confirm LinkedIn URLs for Matt, Andrew, Rob, Noah, Bridgette. Confirm whether Bridgette is ready to be a named author (requires bio page + Person schema even if she hasn't authored yet — she can be a `reviewedBy` or podcast-quoted expert immediately).

---

## Author bio pages — required build

Every named author needs a full `/team/{slug}` page:

### Required fields per bio
- Full name + job title
- Photo (professional headshot)
- 150-250 word biography (first-person, warm, expert-positioned)
- Credentials + years of experience
- Areas of expertise (maps to knowsAbout schema)
- LinkedIn profile (sameAs)
- Twitter/X profile (sameAs)
- List of articles authored on site
- Podcast appearances (The Focused Fundraiser + external)
- Speaking engagements / webinars
- Media mentions (if applicable)

### Required schema per bio page

```json
{
  "@context": "https://schema.org",
  "@type": "ProfilePage",
  "mainEntity": {
    "@type": "Person",
    "name": "Rob Burke",
    "jobTitle": "Chief Marketing Officer",
    "worksFor": {
      "@type": "Organization",
      "name": "DonorDock",
      "url": "https://www.donordock.com"
    },
    "knowsAbout": [
      "Smart Stewardship",
      "Nonprofit marketing",
      "SEO for nonprofits",
      "Donor engagement",
      "Brand positioning"
    ],
    "sameAs": [
      "https://www.linkedin.com/in/robburke/",
      "https://twitter.com/robburke"
    ],
    "image": "https://www.donordock.com/images/team/rob-burke.jpg",
    "url": "https://www.donordock.com/team/rob-burke"
  }
}
```

---

## Byline + Person schema on articles

Every article must have:
- Visible byline at article top: "By [Full Name], [Job Title]" with headshot
- Link from byline to `/team/{slug}`
- Person schema in Article JSON-LD with `sameAs` LinkedIn + `knowsAbout`
- If article is heavily opinion-based, also include `reviewedBy` attribution to another named expert (e.g., Matt or Rob reviews a Sami article on AI)

---

## Original research asset (highest-leverage E-E-A-T move)

**Target:** Publish the "Nonprofit Fundraising Benchmark Report 2026" as DonorDock's flagship research asset.

### Why this matters for E-E-A-T
- LLMs preferentially cite primary research with methodology statements
- Gives DonorDock named authorship on data every competitor would want to cite
- Creates a perennial backlink target (competitors, academics, press will link to it)
- Differentiates from competitors' generic market reports (Bloomerang's is retention-focused; Virtuous's is vertical-specific; neither targets "growing mid-sized nonprofits" explicitly)

### Data DonorDock owns that none of the competitors do in this slice
- 7,200+ growing-nonprofit customers
- $9B+ in tracked gifts
- Actual usage patterns across Smart Steward Method, Action Board, Smart Nudges, Otto
- Recurring-giving retention rates by cohort
- Email vs text vs multichannel engagement outcomes
- Migration-inbound patterns (switchers from Bloomerang/DonorPerfect/LGL)

### Required rigor
- Named methodology (who, how many, date range, normalization approach)
- Named author (likely Matt + Rob or Matt + Noah)
- Named reviewer (external: AFP-certified professional, independent researcher, or CFRE)
- Anonymized/aggregated data only
- PDF + HTML version with Dataset schema markup
- Public microsite at /benchmark-report-2026 with press-release + download

### Target: Published by Q4 2026.

---

## Third-party validation surfaces

**Currently surfaced:**
- G2 reviews (sameAs on Organization schema)
- Capterra (sameAs)
- Instagram, Facebook, LinkedIn, TikTok (sameAs)

**To add for stronger E-E-A-T:**
- G2 reviews in Review/AggregateRating schema with explicit `isBasedOn` attribution (not just a count)
- /reviews first-party aggregation page (doesn't exist; build it)
- Press mentions page (/press or /in-the-news)
- Awards surface (G2 badges with explicit `award` schema claims)
- Public speaking / conference appearances (list on author pages)
- Podcast guest appearances on external shows (cross-link from author pages)
- Industry association memberships (AFP, etc.)

---

## Trust / compliance surface

**Currently surfaced:**
- SOC 2 Type II (mentioned in pricing FAQ)
- HTTPS + HSTS (technical)

**Existing trust surface (strong):**
- **security.donordock.com** — DonorDock's dedicated security/trust subdomain (live). Covers SOC 2 Type II, data handling, privacy, security practices.
- **Action:** Verify security.donordock.com has Organization + WebPage schema and is linked from footer/nav. Confirm it's indexable and cross-linked from /pricing FAQ around security questions.

**To enhance:**
- Cross-link security.donordock.com from every page footer (if not already)
- Add schema on the subdomain: Organization with `hasCredential` for SOC 2
- Surface directly in llms.txt as a trust anchor
- Link from author pages as a reinforcing trust signal

**Original plan (superseded by existing security.donordock.com):**
~~Build dedicated `/trust` or `/security` page with:~~
  - SOC 2 Type II certificate details
  - GDPR compliance statement
  - CCPA/CPRA statement
  - PCI DSS (for payment processing claims)
  - Data residency (US-based)
  - Data export policy (non-punitive — your data is yours)
  - Privacy policy (link)
  - Incident response policy
- Data handling explanation in schema via Organization `privacyPolicy` + `contactPoint` for security issues

---

## Focused Fundraiser Podcast as E-E-A-T asset

**Current state:** 49+ episodes. Matt + Rob as hosts. Industry guests.

**Underutilized potential:**
- Transcripts not posted (Google can't read audio-only content)
- No PodcastSeries schema on /focused-fundraiser-podcast
- No VideoObject schema on episode pages (YouTube versions exist)
- Episodes not cross-linked from author pages as "recent appearances"
- Guest experts not co-linked as named sources

### Action plan
1. Add PodcastSeries schema to /focused-fundraiser-podcast
2. Add PodcastEpisode + VideoObject schema to each /articles/beyond-the-donation-episode-* page
3. Add transcripts to all 49 episodes (Remotion/Whisper for automation)
4. Build /guests or dynamic guest-linking from episode to guest-expert pages
5. Matt and Rob author pages should list podcast appearances

**This single action adds 49+ deep content assets to the E-E-A-T surface with named-expert dialogue.**

---

## Credentials and certifications to surface

Encourage (and surface on author pages):
- CFRE (Certified Fund Raising Executive) — gold standard in fundraising
- ACFRE (Advanced Certified Fund Raising Executive)
- CAP (Chartered Advisor in Philanthropy)
- Marketing certifications (HubSpot, etc. for Rob)
- Technology certifications (SOC 2 auditor for Matt/Andrew)
- Speaking credentials (AFP conference speakers, etc.)

**Rob to audit which team members hold which credentials and surface them on `/team/*` pages.**

---

## Implementation priority

### Phase 2 (next 8 weeks)
1. Build author bio pages for Matt + Rob + Noah + Bridgette + Elisha + Sami (top 6 most-bylined)
2. Add Person + ProfilePage schema to each
3. Retrofit Person schema to every article byline (template change)
4. Update Organization schema on homepage to include founders as `founder`

### Phase 3 (Q3 2026)
5. ~~Build /trust page~~ (exists at security.donordock.com — enhance with schema + footer linking instead)
6. Build /reviews aggregation page
7. Podcast transcripts + schema for top 10 most-viewed episodes
8. Publish methodology statement for Nonprofit Fundraising Benchmark Report

### Phase 4 (Q4 2026)
9. Publish Nonprofit Fundraising Benchmark Report 2026
10. PR outreach for external citations
11. Press mentions page
12. Speaking credentials surfaced on all author pages

---

## Measurement

Track quarterly:
- Number of published articles with named author byline + Person schema (target: 90%+)
- Number of /team/* pages with full bio + schema (target: 100% of active bylines)
- AI citations referencing DonorDock as source (via Phase 5 AI citation tracking)
- Backlinks to original research (benchmark report)
- Branded searches for individual team members (Matt Bitzegaio, Rob Burke) — indicates personal brand building
