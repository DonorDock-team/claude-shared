# DonorDock GEO Readiness Audit — Phase 1 Baseline

**Target:** https://donordock.com (canonical: https://www.donordock.com)
**Audit Date:** 2026-04-22
**Auditor:** claude-rank GEO Auditor
**Purpose:** Establish the starting-line baseline for DonorDock's new SEO/AEO strategist system.

---

## Executive Summary

DonorDock is currently **invisible to 4 of the 5 major AI search engines** it wants to win. The root cause is a single line in `robots.txt` that disallows `GPTBot`, `ClaudeBot`, `Google-Extended`, `CCBot`, and `Applebot-Extended`. This is an inherited Cloudflare managed-content policy that was likely never reviewed against DonorDock's marketing strategy.

Every other GEO signal on the site is stronger than expected — author schema is real, BlogPosting is well-formed on articles, the homepage has both `Organization` and `SoftwareApplication` with `aggregateRating`, and `/articles/best-nonprofit-crm` is a 3,119-word citation-ready buyer's guide authored by the CMO. None of that work can be ingested by ChatGPT, Claude, Perplexity (via OAI), or Google AI Overviews because the bots are walled off at the door.

**The #1 baseline fact:** DonorDock is competing for AI citations with both hands tied behind its back. Competitors (DonorPerfect, Bloomerang, Givebutter, Network for Good, Neon One) have **zero AI bot restrictions**. When a nonprofit asks ChatGPT "What's the best CRM for small nonprofits?" today, DonorDock is structurally incapable of being part of the answer.

**AI Readiness Level: Level 0 (Invisible)**

**GEO Readiness Score: 32 / 100**
- Access: 10/30 (critical — majority of AI bots blocked)
- Content structure: 14/25
- Schema/entity: 10/20
- EEAT signals: 8/15
- Submission/discovery: 0/10

---

## AI Engine Readiness Matrix

| Engine | Current Status | Impact |
|---|---|---|
| ChatGPT Search | GPTBot **BLOCKED** | Training data cut off, limited AI citations |
| Perplexity | PerplexityBot allowed (default) | **READY** |
| Google AI Overviews/Gemini | Google-Extended **BLOCKED** | Excluded from AI surfaces |
| Claude/Claude Search | ClaudeBot **BLOCKED** | Cannot be cited in claude.ai |
| Microsoft Copilot | Bingbot allowed | **READY** |
| Apple Intelligence | Applebot-Extended **BLOCKED** | Training excluded |
| Meta AI | meta-externalagent **BLOCKED** | Not citable |
| Common Crawl | CCBot **BLOCKED** | Excluded from dataset most LLMs train on |

**Competitor robots.txt comparison:** Bloomerang, DonorPerfect, Givebutter, Network for Good, Neon One — **NONE block AI bots**. DonorDock is alone in shutting them out.

---

## llms.txt Broken — RTF Served as text/plain

The llms.txt file at https://donordock.com/llms.txt returns HTTP 200 with Content-Type `text/plain; charset=utf-8`, but the body begins:
```
{\rtf1\ansi\ansicpg1252\cocoartf2822 ...
```

Someone wrote the llms.txt content in Apple TextEdit (or similar) and saved it as RTF instead of plain text. The file contains intended policy copy ("Allow: all / Training: allowed / Attribution: Please reference 'DonorDock'") but wrapped in RTF markup that no LLM parser can read.

**This is a silent, invisible failure.** 200 response, correct headers, wrong bytes. Been shipping broken since deployment.

Also: the RTF policy says "Allow: all / Training: allowed" while robots.txt blocks 9 AI bots. Direct contradiction.

---

## Citation Readiness — EEAT Signals

### What's working
- **Real author schema on articles** — Rob Burke (CMO), Noah Barnett (CSO) with real job titles, emails, images
- **Organization + aggregateRating** — 4.8/5, ratingCount 200, sameAs social profiles
- **Freshness dates** — datePublished + dateModified on articles

### What's broken
- No `/authors/*` bio pages — Person schema makes claims the site doesn't back up
- No `knowsAbout` or `alumniOf` on Person schema
- Ratings self-declared, not linked to G2/Capterra
- No publish date on marketing pages (/crm, /pricing, /compare/*)
- Noah's `sameAs` array contains empty strings — schema validator errors

---

## Schema Coverage by Page

| URL | Schemas | Grade |
|---|---|---|
| `/` | WebPage + SoftwareApplication + Organization + AggregateRating | B+ |
| `/about` | AboutPage + SoftwareApplication + Person founders | B |
| `/pricing` | WebPage + SoftwareApplication | C |
| `/crm` | WebPage only | D |
| `/faq` | FAQPage | B |
| `/compare/bloomerang-vs-donordock` | WebPage only | D |
| `/articles/best-nonprofit-crm` | BlogPosting × 2 (duplicated) + Person | B- |

**Key gaps:** ItemList on /compare/*, Product/SoftwareApplication on product pages, BreadcrumbList sitewide, HowTo on tutorial articles, VideoObject where videos embed, Event on /webinars-events.

---

## Strategic Recommendations — Priority Order

### P1 — Week 1 of Phase 2: Unblock the bots
Edit robots.txt to allow GPTBot, ClaudeBot, Google-Extended, CCBot, Applebot-Extended, PerplexityBot, OAI-SearchBot, ChatGPT-User, anthropic-ai, Claude-Web. Change Cloudflare Content-Signal to `search=yes, ai-input=yes, ai-train=yes`. **Expected uplift: 4 of 5 target engines crawling within 14-30 days.**

### P2 — Week 1: Fix llms.txt
Re-save as UTF-8 plain text. Reconcile policy with robots.txt. Add content map.

### P3 — Weeks 2-4: Comparison pages → real tables + ItemList schema
`/compare/*` URLs are the highest-intent AI-query pages. Currently zero tables, zero ItemList. Single largest citation-probability uplift available.

### P4 — Weeks 3-6: Question-format H2s on homepage, product pages, pricing
### P5 — Weeks 4-8: Author authority pages (/authors/rob-burke, /authors/noah-barnett, /authors/matt-bitzegaio)
### P6 — Weeks 6-10: Schema upgrade pass — Product/SoftwareApplication on product pages, ItemList on compare pages, BreadcrumbList sitewide
### P7 — Week 8+: Freshness + submission plumbing (datePublished on marketing pages, sitemap lastmod, IndexNow)
### P8 — Phase 3+: Content gap-fill for missing definitional pages

---

## Phase 5 Tracking Seeds

When daily AI citation tracker goes live, measure:
1. Presence in answer for each of 5 engines for 20+ target queries
2. Citation count per engine
3. Position in answer (first, top 3, mentioned, absent)
4. Competitor citation share for same queries
5. Which donordock.com URL gets cited

Expected trajectory: Perplexity citations jump within 30 days post-fix. ChatGPT/Claude/Google AI take 30-90 days as indexes refresh.

**End of baseline audit. No auto-fixes applied.**
