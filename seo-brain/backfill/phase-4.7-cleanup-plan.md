# Phase 4.7 — Article Cleanup + URL Hygiene Plan

**Status:** Closed (2026-05-07)
**Owner:** Rob (review + approve) → Claude Queue executor (run)
**Total articles touched:** ~55 across 13 workstream categories
**Source:** Aggregated from Phase 4.5 batch proposals (B1–B14)
**Outcomes:** see `seo-brain/cleanup/2026-05-phase-4.7-completed.md`

## Closeout summary (2026-05-07)

All 14 Asana tasks in Claude Queue are in ✅ Done. Rob worked through every task and either executed, adjusted, or chose to skip. Two explicit scope decisions diverged from the original plan:

- **Session-notes / training articles → removed, not migrated to `/help/`.** Workstreams 1, 2, 3, 6 are closed via removal + 410/301 rather than building a help-center IA. The `donordock-helpcenter` skill route is deferred.
- **No `/news/` URL built (workstream 4).** Product changelog cluster handled in place (or removed) for now. A future `/news/` or `/changelog/` IA is parked.

The four executed waves (3A title rewrites, 3B body sweeps, 4A glossary expansion, 4B crypto + AmazonSmile refreshes) shipped 96 articles live. See completion summary for per-workstream detail.

## Why this exists

Phase 4.5 backfilled metadata (pillar, keywords, canonical, FAQs, alt-text) on all 290 articles in the Webflow Articles collection so the dynamic schema template can render BlogPosting + FAQPage for each. During that work, ~55 articles surfaced as needing additional treatment beyond field backfill — content rewrites, URL migrations, redirects, retitles, and editorial decisions. Phase 4.7 is the cleanup pass that handles those.

## Constraints

- **Surgical scope per workstream.** Each Asana task touches one category only.
- **All article URL changes need 301 redirects.** Webflow redirect map is the source of truth.
- **No FAQ-library changes.** Phase 4.5 saturated the library at 223 items; Phase 4.7 reuses, never creates new.
- **Brand-positioning compliance.** All rewrites obey `seo-brain/strategy/brand-positioning.md` (no "small nonprofit" head-term, no "first CRM", no churches as target, "1% platform fee" never "no platform fees", "Action Board" two words).

## Execution model

Each workstream below becomes one Asana task in **Claude Queue → 💡 Proposed**, assigned to Rob, due day-of-creation. Rob reviews, edits the execution prompt, moves approved tasks to **📥 To Do**. The `weekly-claude-queue-executor` scheduled task (Mon 9:43am ET) processes To Do items.

---

## The 14 workstreams

### 1. /help/onboarding/ migration — DonorDock onboarding lessons (8 articles)

**Articles:** lesson-1-getting-started, lesson-2-settings-and-users, lesson-3-onboard-your-data, lesson-4-input-data, lesson-5-know-your-priorities-next-moves, lesson-6-become-a-data-expert, lesson-7-templates-for-receipts-and-marketing, lesson-8-engage-donors-through-email

**Why:** Onboarding lessons are user-facing, not prospect-facing. They have low SEO value at /articles/ and clutter the blog. They belong in /help/onboarding/ (or a similar in-product help URL).

**Action:**
1. Decide target URL pattern (likely `/help/onboarding/lesson-N-{slug}` or `/onboarding/lesson-N`)
2. Create new pages at target URLs (Webflow Pages, not CMS — these aren't blog content)
3. Copy body content + update internal cross-links
4. 301 redirect the 8 /articles/ URLs to the new locations
5. Webflow CMS items: archive (don't delete — preserve for redirect mapping)

**Effort:** L (2-4 hours). Separate skill: probably `donordock-helpcenter`.

---

### 2. /help/integrations/ migration (6 articles)

**Articles:** donordock-and-quickbooks, event-attendance-record-in-eventbrite-donordock-through-zapier, eventbrite-zapier-donordock-magic, how-to-launch-productivity-using-donordock-and-zapier, session-review-using-jotform-with-donordock, (one more TBD from B12 review)

**Why:** Integration tutorials are help-center content, not blog content.

**Action:** Same pattern as #1 — move to /help/integrations/{integration}, 301 the old URLs. Consolidate the 2 Eventbrite/Zapier dups into one canonical page.

**Effort:** M (1-2 hours).

---

### 3. /help/{topic}/ migration — feature-specific session notes (5 articles)

**Articles:** /help/imports/, /help/receipts/, /help/reporting/, /help/email/ (effective-communication-through-donordock-email + apple-mail-privacy-measures)

**Action:** Each gets a /help/{topic}/ home with these articles consolidated underneath.

**Effort:** M (1-2 hours).

---

### 4. /news/ migration — product changelog cluster (6 articles)

**Articles:** announcing-our-latest-greatest-updates, donordock-latest-feature-releases, product-update-signup-forms, the-latest-and-greatest-in-donordock, you-can-excel-with-donordock, (and B6 #13 Noah Barnett press release if that's still in /articles/)

**Why:** Product announcements are time-bound. They don't deserve evergreen blog real estate.

**Action:** Build /news/ or /changelog/ section. Move all 6. 301 from /articles/. Future product announcements ship there directly.

**Effort:** M.

---

### 5. /sites-by-donordock/ resource (1 article)

**Article:** session-notes-website-best-practices-and-sites-by-donordock

**Action:** If "Sites by DonorDock" is a feature/product, surface as a feature page at /sites-by-donordock/ instead of buried session notes. Otherwise, archive.

**Effort:** S.

---

### 6. Generic session-notes archive (10 articles, 410/noindex)

**Articles:** session-notes-a-donordock-review, session-notes-action-board-updates, session-notes-bulk-emails, session-notes-donordock-quickbooks (overlap w/ #2), session-notes-imports-giving-hearts-day-import-pointers, session-notes-marketing-bulk-emails, session-notes-new-updates-improved-donordock, session-notes-receipts (overlap w/ #3), session-notes-relationships-2-0, session-notes-relationships-badges-marketing-lists, session-notes-reporting (overlap w/ #3), session-notes-updates-to-direct-mail-support-and-marketing, session-notes-year-end-reporting

**Why:** Generic "what we covered in Tuesday's session" notes have zero evergreen SEO value. They're internal training records that escaped to the blog.

**Action:** Most should be **410 Gone** (not 301 — there's no equivalent destination). A few with reusable content can be salvaged into the /help/ migrations above (#3).

**Effort:** M.

---

### 7. Off-ICP "starting a nonprofit" cluster — 301 or 410 (4 articles)

**Articles:** starting-nonprofit, starting-a-nonprofit-everything-you-need-to-know-to-go-from-a-passion-to-a-plan, building-strategy-budgets-and-community-support-for-your-new-nonprofit, grassroots-fundraising-playbook-new-nonprofits

**Why:** "Starting a nonprofit" is a deprecated pillar (per `seo-brain/strategy/pillars.md`). DonorDock's ICP is **growing nonprofits with $1M+ revenue and 3+ FTE dev teams**, not founders launching new orgs. These articles attract off-ICP traffic and dilute the brand-positioning message.

**Action:** Decision per article: **410 Gone** (no equivalent), **301 to /fundraising-strategy** (if topic adjacent), or **rewrite + retitle** for ICP fit (rare). Default = 410.

**Effort:** S (mostly redirect map updates).

---

### 8. Slug normalization (6+ articles)

**Issues:**
- `beyond-the-donation-episode-007` (3-digit) vs `episode-08`/`episode-10` (2-digit). Pick one format, normalize all 30+ episode slugs, 301-redirect the rest.
- `year-end-givingits-not-too-late-to-rally-your-supporters` — malformed concatenation
- `end-of-year-templates-7cc49` — auto-disambiguated suffix (Webflow re-import artifact)
- `eventbrite-zapier-donordock-magic` — vague "magic"
- `how-to-launch-productivity-using-donordock-and-zapier` — vague "launch productivity"
- `fundraising-events-increase-engagment` — typo "engagment"

**Action:** Decide canonical slugs, change in Webflow, update internal links sitewide, 301 from old slugs.

**Effort:** M-L (slug changes are cascade-y).

---

### 9. Article consolidation — Eventbrite/Zapier duplicate pair

**Articles:** event-attendance-record-in-eventbrite-donordock-through-zapier + eventbrite-zapier-donordock-magic

**Why:** Same topic, two articles. Consolidate into one canonical page in /help/integrations/eventbrite or similar.

**Action:** Pick the stronger article, merge the better content from the other, 301 the loser.

**Effort:** S.

---

### 10. Title fixes + product rebrands (6 articles)

**Items:**
- B5 Ep. 08 title typo — "Blue Cyper" → "Blue Cypher"
- B11 #A9 title — `Ep. 14 | , an interview with…` empty episode tag
- Classy → GoFundMe Pro rebrand (B9 #3 `your-guide-to-integrating-donordock-and-classy`) — body update + URL change
- Meta Charitable Giving Tools sunset (B11 #A2) — body update; service shut down Aug 2024
- AmazonSmile (B12 #4) — re-angle from "list of alternatives" to "shift from passive to active recurring giving" per Smart Stewardship lens
- nonprofit-glossary expansion — 26 → 40-50 terms

**Action:** Per-article copy edit + republish. Where slug changes, add 301.

**Effort:** L (per-article, ~30 min each).

---

### 11. REFRESH-OR-RETIRE editorial decisions (2 articles)

**Articles:** B5 #6 nonprofit-crypto-donations (older voice + 2025 partner landscape needs update), B12 #4 (AmazonSmile — covered in #10)

**Action:** Rob decides per article: refresh in voice + reintroduce, or retire to /news/ as historical content.

**Effort:** S (decision) + L (if refresh wins).

---

### 12. Smart Stewardship anchoring (1 article)

**Article:** B13 #7 fundraising-framework-empowering-nonprofits — uses legacy "Do Good Better" tagline rather than the current Smart Stewardship methodology.

**Action:** Rewrite framing to anchor on Smart Stewardship per `seo-brain/strategy/brand-positioning.md`.

**Effort:** M.

---

### 13. Title-level prohibited rewrites + 301 redirect (~13 articles)

**Articles:** all articles where the title or slug contains "Small ___ Teams", "Small Nonprofit ___", etc. — flagged across batches B4 #6, B4 #9, B5 #6, #8, #10, #11, #16, B6 #3, #8, B10 #6, B12 (small-nonprofits-crm), and others.

**Why:** Brand-positioning prohibits "small nonprofit" / "small team" head-term targeting. Articles attracting off-ICP traffic on those queries should retitle to upmarket language ("growing nonprofit", "development team", "growing fundraising team").

**Action:** Per article — title rewrite + slug rename + 301 from old slug + body sweep for in-paragraph "small ___" instances. Coordinate with /crm pillar internal-link updates.

**Effort:** L (each article is ~30 min; ~13 articles = 1 full day).

---

### 14. Body-level "small nonprofit" voice sweeps (~15 articles)

**Articles:** flagged across B5, B7, B10 — articles where in-paragraph "small nonprofit" / "small team" language exists but the title is OK.

**Action:** Surgical find/replace in body content. Preserve everything else.

**Effort:** M (10-15 min per article).

---

### 15. Duplicate Ep. 36 → 301 redirect (1 pair)

**Articles:** B8 #14 + #15 (both Ep. 36 / Carly Euler — Webflow re-import created `-03d16` suffix duplicate)

**Action:** Decide canonical (#14), 301 #15 → #14, archive #15 in CMS.

**Effort:** S.

---

## Execution sequencing recommendation

**Wave 1 (high-leverage, low-risk):**
- #7 Off-ICP "starting a nonprofit" cluster (4 → 410)
- #6 Generic session-notes archive (10 → 410)
- #15 Ep. 36 dup (1 → 301)
- #1 Onboarding lessons migration (8 → /help/onboarding/)

**Wave 2 (medium effort, content-touching):**
- #2-#5 /help/ + /news/ migrations (~17 articles)
- #14 Body-level voice sweeps (~15 articles)

**Wave 3 (high-leverage, content-rewriting):**
- #13 Title-level rewrites + 301s (~13 articles)
- #10 Title fixes + product rebrands (~6 articles)
- #12 Smart Stewardship anchoring (1)

**Wave 4 (judgment calls):**
- #11 REFRESH-OR-RETIRE editorial decisions (2)
- #8 Slug normalization (~6, but cascade-y)

## After Phase 4.7

Once Phase 4.7 closes, the entire DonorDock content surface is:
- Schema-rendered (Phase 4.5)
- URL-hygiene-clean (Phase 4.7)
- Brand-positioning-compliant (Phase 4.7)
- Continuously tracked (Phase 5 + 6)
- Visible in dashboard (Phase 7)
- Acted on via Claude Queue → To Do (Phase 8)

The system is in steady state. Future articles ship via the ff-article-pipeline skill, which has been updated to populate all required CMS fields out of the gate (Phase 4 integration). New articles never need backfill.
