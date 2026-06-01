# GEO (Generative Engine Optimization) Readiness Audit — donordock.com
**Date:** 2026-06-01
**Auditor:** claude-rank GEO sub-agent
**Scope:** Readiness of donordock.com to be cited by ChatGPT, Perplexity, Google AI Overviews, Gemini, Claude
**Prior baseline:** [../2026-05-baseline/geo-readiness.md](../2026-05-baseline/geo-readiness.md)
**AI Readiness Level:** **2.5 of 3 (Optimized → approaching Dominant)** — *unchanged vs. May*
**Trend:** ▶ **Flat (hold).** Access posture maintained with zero regressions; none of May's content-shape fixes have shipped yet.

---

## 1. Executive Summary

- **Access posture held perfectly.** All 15 major/mid AI crawlers still return HTTP 200 — the Cloudflare unblock that landed in May has **not regressed**. Bytespider remains the only 403 (edge WAF, lowest-value crawler, no action needed). This is the single most important regression-watch item and it passed clean.
- **llms.txt is unchanged and still excellent (95/100, 7,567 bytes).** Best-in-class "Policy for AI systems" block intact (training: allowed, commercial use: allowed with attribution, naming/linking guidance). **`/llms-full.txt` is still HTTP 404** — May's #1 quick-win has not been implemented.
- **No content-shape progress this month.** Every one of the high-leverage content fixes flagged in May is still open: compare pages have **0 HTML tables**, the bloomerang compare JSON-LD **still has the trailing-comma parse error** (now at line 36), compare H1 is still the marketing tagline, **no visible author bylines** render on any article, **0 question-format H2s** on pillar articles, and the homepage still has **no "DonorDock is a…" definition block**.
- **The two citation-magnet pages held steady.** FAQ page (114 rendered question headings + valid FAQPage schema) and the donor-retention pillar (14 source references, strong stat density) remain the strongest assets and the template the rest of the site should copy.
- **Net:** This was a maintenance month. The expensive, durable foundation (access + llms.txt) is solid and stable. The remaining gap to Level 3 (Dominant) is entirely a content/Webflow-CMS execution backlog that has not been worked. Score holds; it does not advance.

---

## 2. Bot Access Matrix — RE-VERIFIED (regression watch)

**robots.txt** (https://www.donordock.com/robots.txt) — unchanged single allow-all rule:

```
User-agent: *
Allow: /
Sitemap: https://www.donordock.com/sitemap.xml
```

Each bot tested live with its **actual production User-Agent string** against `https://www.donordock.com/` on 2026-06-01:

| Bot | Powers | HTTP (Jun) | HTTP (May) | Δ |
|---|---|---|---|---|
| GPTBot | OpenAI training + ChatGPT | **200** | 200 | — |
| OAI-SearchBot | ChatGPT Search | **200** | 200 (via *) | — |
| ChatGPT-User | ChatGPT live browsing | **200** | n/a | ✓ |
| ClaudeBot | Anthropic training + Claude.ai | **200** | 200 | — |
| Claude-Web | Claude.ai live fetching | **200** | 200 (via *) | — |
| PerplexityBot | Perplexity index | **200** | 200 | — |
| Perplexity-User | Perplexity live citations | **200** | 200 (via *) | — |
| Google-Extended | Google AI Overviews + Gemini | **200** | 200 | — |
| Googlebot | Standard Google + AIO ranking | **200** | 200 (via *) | — |
| Bingbot | Microsoft Copilot + ChatGPT Browse | **200** | 200 | — |
| Applebot-Extended | Apple Intelligence | **200** | 200 | — |
| CCBot | Common Crawl (foundation data) | **200** | 200 | — |
| Meta-ExternalAgent | Meta AI (Llama training) | **200** | 200 (via *) | — |
| Amazonbot | Alexa, Rufus, Amazon AI | **200** | 200 (via *) | — |
| DuckAssistBot | DuckDuckGo AI Answer | **200** | 200 (via *) | — |
| Bytespider | ByteDance / TikTok / Doubao | **403** | 403 | — |

**Verdict:** **No regressions.** 15 of 16 crawlers return 200; the lone 403 (Bytespider) is unchanged, blocked at the CDN/WAF layer (not robots.txt), and is the lowest-value crawler in the set. Best-possible posture maintained for a second consecutive month.

**Risk (carried over):** The allow-all `User-agent: *` rule is fragile — a future per-bot `Disallow` could silently break AI visibility. Recommendation #9 (convert to an explicit named allow-list) remains open and is the cheapest defensive hardening available (~30 min).

---

## 3. llms.txt / llms-full.txt Status

| File | Jun status | May status | Δ |
|---|---|---|---|
| `/llms.txt` | **HTTP 200, 7,567 bytes** | 200, 7,567 bytes | — (byte-identical) |
| `/llms-full.txt` | **HTTP 404** | 404 | ✗ still missing |

**llms.txt quality: 95/100 — unchanged.** Verified live this month: H1 + product summary blockquote, structured Category/Audience/Pricing/Founded/Rating facts, 10 core pages, 7 capability pages, 10 competitor comparisons, 5 solutions, 6 education resources, online-giving fee structure, 10 key-differentiator bullets, and the best-in-class **"Policy for AI systems"** section (training allowed, commercial use allowed with attribution, explicit naming + linking guidance, accurate pricing/rating to pre-empt hallucination).

**Only deduction remains the missing `llms-full.txt`.** This is the single concatenated-corpus file that ChatGPT Deep Research / Perplexity Deep Research / Gemini research mode fetch when asked "tell me everything about DonorDock." It was the #1 quick-win in May and has not shipped. Lowest-effort, highest-symbolic-value item still on the board.

---

## 4. Content Citation-Readiness — Re-verification of May's Findings

All page-level scores are **unchanged** from May because no content-shape fixes shipped. Re-confirmed live this month:

| Page type | Citation-readiness | Δ vs May | Live re-check (2026-06-01) |
|---|---|---|---|
| FAQ page (`/faq`) | 92/100 | — | **114 rendered question headings + valid FAQPage schema confirmed.** Citation-magnet, holding. |
| Donor-retention pillar | 88/100 | — | **14 source references + strong % stat density confirmed.** Template page, holding. |
| Pricing (`/pricing`) | 75/100 | — | No freshness stamp / question H2 added. |
| Best-CRM pillar (`/articles/best-nonprofit-crm`) | 70/100 | — | **Still 0 real body-text source citations** (grep "according to" hits resolve to CSS/JS class names, not prose). **0 question H2s. No visible "By Rob Burke" byline.** Unchanged. |
| Compare pages (`/compare/*`) | 49/100 avg | — | **bloomerang: 0 `<table>` elements, H1 still "The Difference Between Retention Scores & Relationship Growth", JSON-LD trailing-comma parse error confirmed at line 36.** Unchanged. |
| Homepage (`/`) | 39/100 | — | **No "DonorDock is a…" definition paragraph in body HTML.** Unchanged. |

**Bottom line:** The two best pages (FAQ, donor-retention) are stable and strong. The four improvement-target page types are byte-for-byte the same as last month — the recommended work has not been started.

---

## 5. Delta Section — June vs. May

### What changed
- **Nothing materially.** This is a flat maintenance month. Scores, llms.txt bytes, robots.txt, and per-page citation-readiness are all identical to the May baseline.

### Regressions (watch items that passed)
- **None.** Critical re-verification target — all 15 AI crawlers still 200, Bytespider still 403 — **passed clean.** The May Cloudflare unblock has held for a full cycle.

### Still-open items carried from May (no progress)
| # | May recommendation | Status Jun 1 | Effort | Impact |
|---|---|---|---|---|
| 1 | Ship `/llms-full.txt` | ✗ still 404 | 1 day | High |
| 2 | Visible author bylines on articles | ✗ none rendered | 1 day | High |
| 3 | HTML comparison tables on 10 `/compare/*` | ✗ 0 tables | 3 days | High |
| 4 | Fix JSON-LD trailing comma (bloomerang + audit all 10) | ✗ still erroring (line 36) | 15 min | Medium |
| 5 | Fix compare H1 → "Bloomerang vs DonorDock…" | ✗ still tagline | 1 hr | Medium |
| 6 | "according to [source, year]" citations in pillar articles | ✗ Best-CRM still 0 | 4 days | High |
| 7 | Question-form H2s on pillar articles | ✗ still 0 | 2 days | Medium |
| 8 | Homepage "What is DonorDock?" definition block | ✗ absent | 2 hrs | Medium |
| 9 | robots.txt → explicit AI-bot allow-list | ✗ still allow-all | 30 min | Low/defensive |
| 10 | "Last updated" stamps on product/pricing pages | ✗ not added | 1 day | Medium |

**0 of 10 May recommendations implemented.**

### Score trajectory
| Month | GEO grade | AI Readiness Level | Note |
|---|---|---|---|
| Apr 2026 | F (32/100) | 0–1 (Invisible/Basic) | AI bots blocked at Cloudflare |
| May 2026 | ~2.5/3 (Optimized) | 2.5 | Cloudflare unblock LANDED; llms.txt 95/100 |
| **Jun 2026** | **~2.5/3 (Optimized)** | **2.5** | **Flat — access held, content backlog untouched** |

---

## 6. Fixes — Prioritized for July

The path to Level 3 (Dominant) is unchanged; the backlog simply did not get worked. Recommended sequencing for maximum lift-per-effort:

1. **Two sub-1-hour wins first** (clear them this week): fix the bloomerang JSON-LD trailing comma (#4, 15 min) and the compare H1 (#5, 1 hr). These are embarrassing, cheap, and one is actively breaking strict JSON-LD parsers.
2. **Ship `/llms-full.txt`** (#1, 1 day) — concatenate the 10 pillar + 10 compare + 5 solution + pricing/about/faq markdown bodies into one corpus file. Highest symbolic + deep-research-citation value for the effort.
3. **Add visible author bylines** (#2, 1 day) across all articles — name, role, photo, bio link, "Last updated" date above the body.
4. **HTML comparison tables on all 10 `/compare/*` pages** (#3, 3 days) — the single highest-leverage content upgrade for "X vs Y" AI queries.
5. **Retrofit Best-CRM (and 4 other pillars) with 4–6 sourced stats** (#6) and **question-form H2s** (#7) to match the donor-retention template.
6. **Homepage definition block** (#8) and **product-page freshness stamps** (#10).
7. **Defensive:** convert robots.txt to an explicit named AI-bot allow-list (#9).

---

## Verification Plan (after fixes ship)

1. Wait 14–28 days for AI re-crawling.
2. Run citation tests in ChatGPT Search, Perplexity, Google AI Overviews, Gemini, and Claude.ai (web search) for: "best nonprofit CRM 2026", "DonorDock vs Bloomerang", "what does DonorDock cost", "donor retention statistics".
3. Track citations in `/Users/rob/Documents/DonorDock/Claude/Data/` with date-stamped logs.
4. Resubmit sitemap to Google Search Console + Bing Webmaster Tools after deploying.
5. Enable IndexNow for Webflow (Bing/Copilot fast-indexing).
6. Re-run this audit at `/tmp/dd-citations-runner/seo-brain/audits/2026-07-baseline/` and compare deltas — especially confirm `/llms-full.txt` ships and compare-page tables land.

---

## Appendix: Raw signals captured (2026-06-01)

- Bot access: 16 user-agents tested live against homepage → 15× HTTP 200, Bytespider 403 (unchanged).
- `/llms.txt`: HTTP 200, 7,567 bytes (byte-identical to May).
- `/llms-full.txt`: HTTP 404.
- `/compare/bloomerang-vs-donordock`: `<table>` count = 0; H1 = "The Difference Between Retention Scores & Relationship Growth"; 1 JSON-LD block → **PARSE ERROR: illegal trailing comma, line 36 col 27.**
- `/articles/best-nonprofit-crm`: 0 real body-text source citations; 0 question H2s; no rendered byline.
- `/articles/donor-retention`: 14 source references; valid BlogPosting + FAQPage + Person schema; no rendered byline.
- `/faq`: 114 rendered question headings; valid FAQPage schema.
- `/` (home): no "DonorDock is a…" definition paragraph in body HTML.
- robots.txt body: `User-agent: *` / `Allow: /` / `Sitemap: https://www.donordock.com/sitemap.xml`
