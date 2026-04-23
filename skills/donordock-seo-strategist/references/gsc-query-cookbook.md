# GSC Query Cookbook

Common Google Search Console queries via MCP. Use these to ground SEO recommendations in real data rather than estimates.

**Available tools** (via MCP `mcp__gsc__*`):
- `site_snapshot` — total clicks/impressions/CTR/position over N days
- `quick_wins` — queries ranking 4-15 with high impressions (push-to-page-1 opportunities)
- `content_gaps` — queries at position 20+ with impressions (create-content opportunities)
- `topic_cluster_performance` — aggregate metrics for a URL-pattern
- `advanced_search_analytics` — custom query/filter/dimension
- `ctr_opportunities` — pages with impressions but below-expected CTR
- `content_decay` — pages declining over 3 consecutive 30-day periods
- `ctr_vs_benchmark`, `cannibalization_check`, `traffic_drops` — specialized
- `inspect_url`, `submit_url`, `submit_batch`, `submit_sitemap` — submission tools

---

## Quick recipes

### "What are our top monthly opportunities?"
```
quick_wins(days=90, min_impressions=200)
```
Returns queries at positions 4-15 with high impressions. Sort by `opportunity` field — that's estimated click lift if we push to position 1-3.

### "Where should we create new content?"
```
content_gaps(days=90, min_impressions=100)
```
Returns queries we're ranked 20+ for with real impressions. Each one is an unmet search demand we can build a page for.

### "How is pillar X performing?"
```
topic_cluster_performance(path_pattern="/PILLAR-SLUG", days=90)
```
Aggregated clicks/impressions/CTR/position for all pages matching the pattern + top 5 pages + top queries.

### "How many impressions is the site getting this quarter?"
```
site_snapshot(days=90)
```
Total metrics with prior-period comparison.

### "Which pages need better meta descriptions?"
```
ctr_opportunities(days=28, min_impressions=500)
```
Pages with high impressions but CTR below benchmark — likely meta description issues.

### "Are any pages losing traffic?"
```
content_decay()
```
Pages with consistent 3-consecutive-30-day-period decline.

### "Custom dive: all queries containing 'stewardship'"
```
advanced_search_analytics(
  days=90,
  dimensions=["query"],
  filters=[{"dimension": "query", "operator": "contains", "expression": "stewardship"}],
  row_limit=100,
  order_by="impressions"
)
```

### "How does /pricing page rank?"
```
advanced_search_analytics(
  days=90,
  dimensions=["query", "page"],
  filters=[{"dimension": "page", "operator": "equals", "expression": "https://www.donordock.com/pricing"}],
  row_limit=50
)
```

### "Which competitor-intent queries are we winning?"
```
advanced_search_analytics(
  days=90,
  dimensions=["query"],
  filters=[{"dimension": "query", "operator": "includingRegex", "expression": "bloomerang|donorperfect|neon|givebutter|little green"}],
  row_limit=100
)
```

### "Are we ranking for any brand-confusion queries?"
```
advanced_search_analytics(
  days=90,
  dimensions=["query"],
  filters=[{"dimension": "query", "operator": "contains", "expression": "donordock"}],
  row_limit=50
)
```

---

## Pillar cluster monitoring (monthly)

Run topic_cluster_performance for each of the 7 pillars and log to the monthly opportunity report:

```
topic_cluster_performance(path_pattern="/smart-steward-method", days=30)
topic_cluster_performance(path_pattern="/crm", days=30)
topic_cluster_performance(path_pattern="/online-giving", days=30)
topic_cluster_performance(path_pattern="/fundraising-strategy", days=30)
topic_cluster_performance(path_pattern="/donor-outreach", days=30)
topic_cluster_performance(path_pattern="/otto", days=30)
topic_cluster_performance(path_pattern="/donor-retention", days=30)
```

Also monitor:
- `/articles/` — full blog performance
- `/compare/` — comparison SERP performance
- `/features/` — feature page performance
- `/solution/` — solution page performance

---

## Triage: query → interpretation

| Position | Impressions | Clicks | Action |
|---|---|---|---|
| 1-3 | >500 | Low | CTR problem — investigate meta description / title |
| 4-10 | >500 | Moderate | Quick win — push to page 1 via content + internal links |
| 11-20 | >500 | Low | Content gap — needs stronger page or new article |
| 20-50 | >500 | Zero-low | Content gap — create dedicated page |
| 50+ | >100 | Zero | Uncontested content gap — prime opportunity |
| Any | <50 | Any | Low priority — don't over-invest |

---

## Common pitfalls

1. **90 days vs 28 days** — default to 28 for fresh signals, 90 for stable trends. Don't mix.
2. **Brand queries dominate when aggregated** — filter them out with `notContains donordock` for category analysis.
3. **Impressions ≠ search volume** — GSC only shows what we appeared for, not total market demand. For market-sizing, use external tools.
4. **Position avg can mislead** — a "position 6 avg" could mean half impressions at position 3 and half at position 9. Look at distribution via date dimension.
5. **Low CTR doesn't always mean bad meta** — if the query is informational and we rank below a featured snippet, CTR is structurally capped. Check SERP features.

---

## When to run fresh GSC queries

**Always run fresh:**
- Monthly opportunity report generation
- "Should we write X?" strategic questions (validate keyword opportunity)
- Comparison page performance check
- Content validation where a ranking claim is made

**Use cached data acceptably:**
- Strategic planning where exact numbers don't matter
- Historical trend analysis
- Baseline comparison (keyword-universe.md has the 2026-04-23 baseline)

**Never use cached data:**
- Claims about current rankings in published content
- Client/Rob-facing performance reports
- Anything where the data will be read 30+ days after generation
