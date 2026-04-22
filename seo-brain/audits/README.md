# Audits

Dated, append-only snapshots of site state. Never overwritten.

## Naming

- Baseline: `YYYY-MM-baseline/` (Phase 1, one-time)
- Monthly: `YYYY-MM/` (Phase 6, recurring)

Each folder contains per-audit markdown files plus an `executive-summary.md`.

## Per-folder contents

| File | Source |
|---|---|
| `technical-seo.md` | `rank-audit` |
| `performance.md` | `rank-perf` |
| `security.md` | `rank-security` |
| `schema-coverage.md` | `rank-schema` |
| `geo-readiness.md` | `rank-geo` |
| `aeo-readiness.md` | `rank-aeo` |
| `citability.md` | `rank-citability` |
| `content-quality.md` | `rank-content` |
| `vertical.md` | `rank-vertical` |
| `competitors/<name>.md` | `rank-compete` per competitor |
| `sitemap-analysis.md` | Cross-reference with `sitemaps/website-sitemap.json` |
| `backlinks.md` | GSC Links report (manual export monthly) |
| `executive-summary.md` | Claude synthesis for Rob |

## Cadence

- Baseline: once (Phase 1)
- Monthly: 1st of each month via scheduled task (Phase 6)

## Diff protocol

Monthly audits include a diff section comparing against the prior month: fixes completed, new issues, trend direction.
