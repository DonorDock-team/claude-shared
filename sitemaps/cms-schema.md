# DonorDock Webflow CMS Reference

## Articles Collection Schema

Collection ID: `6532889f2379aa018d3520b7`

| Field Slug | Display Name | Type | Required | Notes |
|------------|-------------|------|----------|-------|
| `name` | Title | PlainText | Yes | Max 256 chars |
| `slug` | Slug | PlainText | Yes | Kebab-case, max 256 chars |
| `blog-post-preview` | Blog Post Preview | PlainText | Yes | Excerpt for article cards |
| `blog-post-summary` | Content | RichText | No | Full article body in HTML |
| `reading-time` | Reading Time | PlainText | No | Number only (e.g., "7") |
| `main-image` | Main Image | Image | No | Hero image, upload separately |
| `alt-text-feature-image` | Alt text Feature Image | PlainText | No | Alt text for hero image |
| `authors-2` | Authors (Team Member) | Reference | No | Ref to People collection |
| `categories` | Categories | MultiReference | No | Ref to Article Categories |
| `tags-3` | Tags | MultiReference | No | Ref to Article Tags |
| `featured` | Featured | Switch | No | Default false |
| `canonical-url` | Canonical URL | PlainText | No | Only if republishing |

---

## Article Categories (Collection: `6532889f2379aa018d352166`)

| Name | ID |
|------|-----|
| Fundraising | `6532889f2379aa018d3526aa` |
| Donor Management | `6532889f2379aa018d35266e` |
| Nonprofit Strategy | `6532889f2379aa018d352677` |
| Outreach | `6532889f2379aa018d35269e` |
| DonorDock Updates | `6532889f2379aa018d35263e` |
| Podcast | `6532889f2379aa018d35269f` |

---

## Article Tags (Collection: `6532889f2379aa018d35206b`)

Use these IDs when mapping tags. Pick 2-4 relevant tags per article.

| Name | ID |
|------|-----|
| CRM | `6532889f2379aa018d35216f` |
| Donor Management | `6532889f2379aa018d3521d4` |
| Donor Relationships | `6532889f2379aa018d3520b8` |
| Donor Engagement | `6532889f2379aa018d35225f` |
| donor stewardship | `67ab77f741582d94f4d5746a` |
| donor segmentation | `658d8d8b8702a18e8d456b38` |
| donor database | `67bf258a632143eb430ae105` |
| Fundraising | `6532889f2379aa018d3523a2` |
| Online Fundraising | `6532889f2379aa018d3521c4` |
| Online Giving | `6532889f2379aa018d3521da` |
| Nonprofit Strategy | `6532889f2379aa018d3521db` |
| nonprofit marketing | `6532889f2379aa018d3526ff` |
| nonprofit leadership | `6532889f2379aa018d352714` |
| nonprofit finance | `6568a38eebacfc7f62f10432` |
| nonprofit website | `6532889f2379aa018d352722` |
| Nonprofit AI | `693099c2cdacdef589684566` |
| Outreach | `6532889f2379aa018d35206c` |
| Marketing | `6532889f2379aa018d35216d` |
| Events | `6532889f2379aa018d352399` |
| Reporting | `6532889f2379aa018d352274` |
| Product Updates | `6532889f2379aa018d352050` |
| Product Tips | `6532889f2379aa018d352366` |
| DonorDock Updates | `6532889f2379aa018d352293` |
| Starting a Nonprofit | `6532889f2379aa018d35216a` |
| Direct Mail | `6532889f2379aa018d35216e` |
| Matching Gifts | `6532889f2379aa018d35209a` |
| Year End Fundraising | `6532889f2379aa018d35219c` |
| Year End Communication | `6532889f2379aa018d352369` |
| Contribution Statements | `6532889f2379aa018d352398` |
| Annual Reporting | `6532889f2379aa018d35216b` |
| board of directors | `6532889f2379aa018d352715` |
| board | `67570210c489f42d35723d94` |
| GivingTuesday | `6532889f2379aa018d352719` |
| Peer-to-peer fundraising | `6532889f2379aa018d352725` |
| Platform Fees | `6532889f2379aa018d352726` |
| text-to-give | `653a71103f30855318ea7b2f` |
| text message fundraising | `65b90f0fc84160e49b5b7413` |
| NMS | `65b2b2b4ae35b5a8756afdff` |
| Professional Development | `659d5fb3af054b13685260f6` |
| grants | `65fc3d8252e202f32d49ee62` |
| volunteers | `664b731cf5b9af576926540d` |
| volunteer management | `66e1a27f5d88ed2777dc5576` |
| volunteer tracking | `66e1a27fce46f4a2ea619b3d` |
| major gifts | `66fd5224d793160c4f039efd` |
| moves management | `67068c7dc599119ae035182c` |
| community engagement | `6787d80656bfe62a418ae505` |
| Agile Stewardship Model | `67dadc189e6cd38b5155b49d` |
| Planned Giving | `6979211c0381b6540a8c7ba5` |
| podcast | `6532889f2379aa018d35216c` |

---

## Known Authors

| Name | ID | Position |
|------|-----|----------|
| Rob Burke (default) | `6532889f2379aa018d352707` | CMO |
| Noah Barnett | `680b86151e257477c2defb0a` | Chief Strategy Officer |
| Leigh Smith | `68c85d9150f59175978ae3a5` | Nonprofit Advisor |

---

## CMS Item Creation Template

When creating a draft article, use this structure with `create_collection_items`:

```
Collection ID: 6532889f2379aa018d3520b7

{
  "fieldData": [
    {
      "name": "Article Title Here",
      "slug": "article-title-here",
      "blog-post-preview": "1-2 sentence preview excerpt.",
      "blog-post-summary": "<h2>First Section</h2><p>Article body HTML...</p>",
      "reading-time": "7",
      "authors-2": "6532889f2379aa018d352707",
      "featured": false,
      "categories": ["category-id-1"],
      "tags-3": ["tag-id-1", "tag-id-2"],
      "alt-text-feature-image": "Descriptive alt text for hero image"
    }
  ],
  "isDraft": true,
  "isArchived": false
}
```

Important notes:
- `reading-time` is just the number as a string (e.g., "7"), not "7 min"
- `blog-post-summary` is the full article HTML body (no h1, start with h2)
- `authors-2` is a single Reference (not MultiReference), pass the ID string directly
- `categories` and `tags-3` are MultiReference arrays of ID strings
- Always set `isDraft: true` — never publish live from this pipeline
