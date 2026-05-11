# Weekly Citation Digest — Rolling 12-Week Archive

This file holds the most recent 12 weeks of AI citation digests, newest first.
Older weeks rotate to `seo-brain/tracking/archive/weekly-summary-{year}.md`.

Each week synthesizes three runs:
- **Monday** — full 150-prompt bank across Anthropic, OpenAI, Perplexity, Gemini
- **Thursday** — drift run (re-test of full bank)
- **Saturday** — Google AI Overview (Chrome) for top-20 prompts

---

# Weekly Citation Digest — Week of 2026-05-04

_Baseline week — no prior week data for WoW deltas._

## Headline
- Aggregate citation rate this week: **15.3%** (Thu) vs **14.2%** (Mon) — **+1.1pp intra-week**
- Best engine: **Perplexity** at **31.3%** (Thu, up from 26.7% Mon)
- Worst engines: Anthropic / OpenAI / Gemini all flat at **10.0%**
- Google AIO render rate: **100%** of 19 eligible queries — DD cited in **78.9%** (15/19)

## By engine (full 150-prompt bank)
| Engine | This Mon | This Thu | Δ Mon→Thu | Last Week Mon | Δ WoW |
|---|---|---|---|---|---|
| Anthropic | 10.1% | 10.0% | -0.1pp | — | n/a (baseline) |
| OpenAI | 10.0% | 10.0% | 0.0pp | — | n/a (baseline) |
| Perplexity | 26.7% | 31.3% | **+4.6pp** | — | n/a (baseline) |
| Gemini | 10.0% | 10.0% | 0.0pp | — | n/a (baseline) |
| **All** | **14.2%** | **15.3%** | **+1.1pp** | — | n/a (baseline) |

> Perplexity drove the entire weekly lift. The three other engines were perfectly flat at 10.0% — that's a structural ceiling on owned-brand prompts (P001–P015 cluster) and almost nothing else.

## Pillar performance (Thursday run, all engines)
| Pillar | DD citation rate | Top citing engine |
|---|---|---|
| Brand (P001–P014 etc.) | **100.0%** (20/20) | Anthropic |
| Comparison ("DonorDock vs X" / "Alternative to X") | **50.0%** (38/76) | Perplexity |
| Feature ("Donor CRM with X") | 17.9% (5/28) | Perplexity |
| Pricing | 8.3% (1/12) | Perplexity |
| Best-of / Vertical | 8.3% (12/144) | Perplexity |
| How-to | 2.4% (2/84) | Perplexity |
| Competitor weakness ("Hidden costs of…" / "X problems") | **0.0%** (0/40) | — |

## Wins this week (cited Thu, not Mon — Perplexity, all)
- P025 — Donor CRM with flat rate pricing no per user fees
- P042 — Best donor CRM for faith-based nonprofits
- P046 — Best donor CRM for arts and cultural nonprofits
- P060 — Donor CRM with recurring giving
- P063 — Donor CRM with text messaging
- P066 — Donor CRM with campaign and appeal tracking
- P080 — Best donor CRM for private K-12 schools
- P088 — Best donor CRM for food security organizations
- P125 — Smart Stewardship vs Responsive Fundraising
- P141 — Easy donor database for fundraisers

## Losses this week (cited Mon, not Thu — Perplexity, all)
- P034 — Best nonprofit CRM for growing organizations
- P043 — Best donor CRM for human services nonprofits
- P058 — Donor CRM with online giving forms

> Net flip on Perplexity: **+7 prompts**. All movement is on Perplexity — the other three engines were stable.

## Competitive landscape (mentions across all engines, full bank)
| Competitor | This Mon | This Thu | Δ Mon→Thu |
|---|---|---|---|
| Bloomerang | 302 | 320 | +18 |
| DonorPerfect | 242 | 254 | +12 |
| Little Green Light | 153 | 170 | +17 |
| Kindful | 150 | 156 | +6 |
| Blackbaud | 113 | 129 | +16 |
| Salesforce Nonprofit Cloud | 111 | 124 | +13 |
| Neon CRM | 116 | 107 | -9 |
| Givebutter | 77 | 87 | +10 |
| Raiser's Edge | 61 | 81 | +20 |
| Virtuous | 54 | 64 | +10 |
| Network for Good | 49 | 44 | -5 |
| Bonterra | 41 | 42 | +1 |
| Neon One | 31 | 40 | +9 |

> Bloomerang, DonorPerfect, LGL, and Blackbaud (the Big 4) are pulling away — every one of them added mentions Mon→Thu. Only Neon CRM and Network for Good lost ground.

## Google AIO highlights
- AIO rendered on **19/19** eligible prompts (100% render rate)
- DD cited within AIO: **78.9%** (15/19)
- AIO wins: P001–P014, P017 (all Brand + Comparison prompts where DD owns the space)
- Missed AIO opportunities (high-intent prompts where AIO showed competitors instead):

| Prompt | Competitors in AIO |
|---|---|
| **P015** — Alternative to Bloomerang | Neon One, Keela, Givebutter, Blackbaud, DonorPerfect, Raiser's Edge, Virtuous, Bloomerang |
| **P016** — Alternative to DonorPerfect | Blackbaud, LGL, Raiser's Edge, DonorPerfect, Bloomerang, Givebutter, Virtuous |
| **P018** — Alternative to Kindful | LGL, Bloomerang, Kindful, DonorBox |
| **P019** — Alternative to Blackbaud Raiser's Edge | Raiser's Edge, DonorPerfect, Bloomerang, Neon CRM, Virtuous, Blackbaud |

## Recommended actions (P0/P1)

**P0 — Win back AIO on "Alternative to X" prompts**
DD is invisible in AIO for the four biggest "Alternative to" queries (P015/P016/P018/P019). These are high-intent, near-bottom-of-funnel prompts. Strengthen the four corresponding `/compare/alternative-to-{bloomerang,donorperfect,kindful,blackbaud}` pages — explicit "best DonorDock alternative" framing, comparison tables, schema, and citations from G2 / Capterra to feed AIO sources.

**P0 — Build the Competitor Weakness pillar (currently 0% citation across 40 prompts)**
Zero DD citations on prompts like "Hidden costs of Neon CRM" (P096), "Network for Good problems" (P132), "Givebutter limitations" (P133), "Hidden costs of Network for Good" (P097). These are gift-wrapped switching-intent queries. Need objective, well-cited teardown content (with G2/Capterra/Reddit references) on each competitor's known limitations.

**P1 — Lift Best-of / Vertical pillar (8.3%, largest pillar by volume — 144 prompts)**
Biggest single source of unrealized citation. Vertical pages for faith-based, human services, arts/cultural, K-12 schools, hospitals, museums need stronger AEO signals — clear "DonorDock is best for X because…" answers, vertical-specific case studies, and schema.

**P1 — Close the engine gap on Anthropic / OpenAI / Gemini (all stuck at 10.0%)**
Three of four engines are flat at exactly 10% — they're only citing DD on the 15 owned-brand prompts and ignoring everything else. Perplexity is doing the work because it surfaces a wider source pool. Push for citations on G2, Capterra, and high-DR roundup sites that the LLM training cuts and retrieval layers actually use.

**P1 — Stabilize Perplexity wins**
Three Perplexity prompts flipped DD-out Mon→Thu (P034, P043, P058). Worth inspecting whether new competitor content was published or if Perplexity's source ranking shifted. Re-run drift mid-week next week to confirm.

---
