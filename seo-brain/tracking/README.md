# Tracking

Time-series observations. Appended continuously.

## Structure

```
tracking/
├── serp-positions/
│   └── YYYY-WW.json           Weekly snapshot of target keyword rankings
├── ai-citations/
│   ├── daily/
│   │   └── YYYY-MM-DD.json    Daily priority-tier run (20 prompts × 5 engines)
│   └── weekly/
│       └── YYYY-WW.json       Full prompt-bank run (all prompts × 5 engines)
├── prompt-bank.md             Target prompts for AI citation tracking
└── backlinks/
    └── YYYY-MM.json           Monthly GSC Links report
```

## AI citation tracking (Phase 5)

**Daily** — tiered priority subset (~20 prompts) × 5 engines: Claude, ChatGPT, Perplexity, Gemini, Google AI Overviews
**Weekly** — full prompt bank × 5 engines

Each entry logs:
- prompt
- engine
- cited (y/n)
- position (1st / 2nd / 3rd / other / none)
- excerpt where cited
- full response (archived)
- competitor citations (who else was cited for this query)

## SERP tracking (Phase 6)

Weekly rank check for all P0 + P1 keywords from `strategy/keyword-universe.md`. Position tracked, diff reported.
