# Schema Templates

Copy-paste JSON-LD templates by content type. These are structural scaffolds — fill in content, then validate before publish.

**Source of truth:** `seo-brain/strategy/content-standards.md` (section: Required schema markup by content type).

---

## Universal rules

Every JSON-LD block:
- Parse as valid JSON (no trailing commas — #1 cause of Google discarding schema)
- Flat `@graph`, not nested `@graph` inside `@graph`
- `@id` on every top-level node
- Canonical URLs with `#fragment` for internal refs
- No `REPLACE_WITH_*` tokens in production
- Visible content MUST match schema text (FAQ Qs = H2/H3 on page)

---

## Homepage schema (anchor)

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://www.donordock.com/#organization",
      "name": "DonorDock",
      "url": "https://www.donordock.com",
      "logo": "https://www.donordock.com/images/logo.svg",
      "foundingDate": "2017",
      "founder": [
        {"@type": "Person", "name": "Matt Bitzegaio"},
        {"@type": "Person", "name": "Andrew Lutgen"}
      ],
      "sameAs": [
        "https://www.facebook.com/donordock",
        "https://www.linkedin.com/company/donordock",
        "https://www.instagram.com/donordock",
        "https://www.g2.com/products/donordock",
        "https://www.capterra.com/p/184187/DonorDock/"
      ]
    },
    {
      "@type": "WebSite",
      "@id": "https://www.donordock.com/#website",
      "name": "DonorDock",
      "url": "https://www.donordock.com",
      "publisher": {"@id": "https://www.donordock.com/#organization"},
      "potentialAction": {
        "@type": "SearchAction",
        "target": {"@type": "EntryPoint", "urlTemplate": "https://www.donordock.com/search?q={search_term_string}"},
        "query-input": "required name=search_term_string"
      }
    },
    {
      "@type": "SoftwareApplication",
      "@id": "https://www.donordock.com/#software",
      "name": "DonorDock",
      "description": "DonorDock is an all-in-one donor management CRM for growing and mid-sized nonprofits, grounded in Smart Stewardship methodology. Unlimited contacts, 1% platform fee on online donations.",
      "applicationCategory": "BusinessApplication",
      "applicationSubCategory": "Nonprofit CRM",
      "operatingSystem": "Web, iOS, Android",
      "offers": {
        "@type": "Offer",
        "price": "500.00",
        "priceCurrency": "USD",
        "priceSpecification": {
          "@type": "UnitPriceSpecification",
          "price": "500.00",
          "priceCurrency": "USD",
          "unitText": "MONTH"
        }
      },
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.8",
        "reviewCount": "200",
        "bestRating": "5",
        "worstRating": "1"
      },
      "provider": {"@id": "https://www.donordock.com/#organization"}
    }
  ]
}
```

---

## Article / pillar page schema

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "@id": "https://www.donordock.com/articles/SLUG#article",
  "headline": "Article H1 here (max 110 chars)",
  "description": "150-160 char article description matching meta description",
  "image": "https://cdn.prod.website-files.com/.../hero-image.webp",
  "datePublished": "2026-04-23T09:00:00Z",
  "dateModified": "2026-04-23T09:00:00Z",
  "author": {
    "@type": "Person",
    "@id": "https://www.donordock.com/team/rob-burke#person",
    "name": "Rob Burke",
    "url": "https://www.donordock.com/team/rob-burke",
    "jobTitle": "CMO",
    "knowsAbout": ["Smart Stewardship", "Nonprofit marketing", "SEO for nonprofits"],
    "sameAs": ["https://www.linkedin.com/in/robburke/"]
  },
  "publisher": {"@id": "https://www.donordock.com/#organization"},
  "mainEntityOfPage": "https://www.donordock.com/articles/SLUG",
  "articleSection": "PILLAR_NAME"
}
```

---

## Pillar page FAQPage schema

```json
{
  "@type": "FAQPage",
  "@id": "https://www.donordock.com/PILLAR-URL#faq",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Question text from aeo-questions.md",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "40-60 word answer. Lead with direct answer. Cite a source or DonorDock methodology (Smart Stewardship, Smart Steward Method, Smart Nudges, Action Board, Otto)."
      }
    }
  ]
}
```

**Rule:** at least 10 Question entities on pillar pages. Each answer must match visible H2/H3 + paragraph on the page — Google cross-checks.

---

## HowTo schema (for step-format content)

```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to [task]",
  "description": "One-paragraph description",
  "image": "https://cdn.prod.website-files.com/.../howto-image.webp",
  "totalTime": "PT30M",
  "supply": [
    {"@type": "HowToSupply", "name": "Tool or resource 1"}
  ],
  "step": [
    {
      "@type": "HowToStep",
      "position": 1,
      "name": "Step 1: Name",
      "text": "Step 1 detailed text.",
      "url": "https://www.donordock.com/articles/SLUG#step-1"
    }
  ]
}
```

---

## Comparison page schema

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "SoftwareApplication",
      "@id": "https://www.donordock.com/compare/COMPETITOR-vs-donordock#software",
      "name": "DonorDock",
      "description": "DonorDock is an all-in-one donor management CRM for growing and mid-sized nonprofits, offered as a simpler, transparently priced alternative to [COMPETITOR].",
      "applicationCategory": "BusinessApplication",
      "applicationSubCategory": "Nonprofit CRM",
      "operatingSystem": "Web",
      "offers": {
        "@type": "Offer",
        "price": "500.00",
        "priceCurrency": "USD",
        "priceSpecification": {
          "@type": "UnitPriceSpecification",
          "price": "500.00",
          "priceCurrency": "USD",
          "unitText": "MONTH"
        }
      },
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.8",
        "reviewCount": "200",
        "bestRating": "5"
      },
      "review": [
        {
          "@type": "Review",
          "author": {"@type": "Person", "name": "Customer Name"},
          "reviewRating": {"@type": "Rating", "ratingValue": "5", "bestRating": "5"},
          "reviewBody": "Customer quote text (use real extracted quotes, not placeholders)."
        }
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://www.donordock.com/compare/COMPETITOR-vs-donordock#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What's the difference between [COMPETITOR] and DonorDock?",
          "acceptedAnswer": {"@type": "Answer", "text": "Direct comparison 40-60 words."}
        }
      ]
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://www.donordock.com/compare/COMPETITOR-vs-donordock#breadcrumb",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.donordock.com"},
        {"@type": "ListItem", "position": 2, "name": "Compare", "item": "https://www.donordock.com/compare"},
        {"@type": "ListItem", "position": 3, "name": "[COMPETITOR] vs DonorDock", "item": "https://www.donordock.com/compare/COMPETITOR-vs-donordock"}
      ]
    }
  ]
}
```

---

## Team bio (ProfilePage)

```json
{
  "@context": "https://schema.org",
  "@type": "ProfilePage",
  "mainEntity": {
    "@type": "Person",
    "@id": "https://www.donordock.com/team/SLUG#person",
    "name": "Full Name",
    "jobTitle": "Job Title",
    "worksFor": {"@id": "https://www.donordock.com/#organization"},
    "knowsAbout": ["Topic 1", "Topic 2", "Topic 3"],
    "sameAs": ["https://www.linkedin.com/in/SLUG/"],
    "image": "https://www.donordock.com/images/team/SLUG.jpg",
    "url": "https://www.donordock.com/team/SLUG",
    "description": "150-word bio"
  }
}
```

---

## Podcast (PodcastSeries + PodcastEpisode)

```json
{
  "@context": "https://schema.org",
  "@type": "PodcastSeries",
  "name": "The Focused Fundraiser",
  "url": "https://www.donordock.com/focused-fundraiser-podcast",
  "description": "49+ episodes with fundraising leaders. Hosted by Rob Burke and guests.",
  "webFeed": "https://feed-url.here",
  "image": "https://www.donordock.com/images/podcast-cover.jpg"
}
```

```json
{
  "@context": "https://schema.org",
  "@type": "PodcastEpisode",
  "name": "Episode title",
  "episodeNumber": "5",
  "url": "https://www.donordock.com/articles/beyond-the-donation-episode-5",
  "datePublished": "2026-04-23T09:00:00Z",
  "duration": "PT32M",
  "associatedMedia": {
    "@type": "MediaObject",
    "contentUrl": "https://audio-file-url.mp3"
  },
  "partOfSeries": {"@id": "https://www.donordock.com/focused-fundraiser-podcast#series"}
}
```

---

## Dataset (for State of Stewardship report)

```json
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "The State of Donor Stewardship 2026",
  "description": "Annual research asset from DonorDock analyzing donor stewardship touchpoints, outcomes, and patterns across ~1,300 nonprofit customers.",
  "url": "https://www.donordock.com/state-of-stewardship-2026",
  "creator": {"@id": "https://www.donordock.com/#organization"},
  "datePublished": "2026-11-01",
  "keywords": ["donor stewardship", "nonprofit fundraising", "donor retention benchmarks"],
  "license": "https://creativecommons.org/licenses/by/4.0/",
  "isAccessibleForFree": true
}
```

---

## Validation workflow

Before deploying any schema:

1. Paste into `jsonlint.com` — must parse
2. Paste into `validator.schema.org` — must pass spec validation
3. Copy the live URL (after deploy) into `search.google.com/test/rich-results` — must show rich-result-eligible
4. Wait 24-72 hours, check GSC Enhancements tab for FAQ, HowTo, Product rich results appearing
