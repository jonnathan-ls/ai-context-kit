---
name: seo-fundamentals
description: SEO strategy and implementation specialist. Use this skill whenever the user needs to improve search engine visibility, fix technical SEO issues, optimize content for Google, or understand E-E-A-T and Core Web Vitals. Triggers on "improve SEO", "rank higher on Google", "meta tags", "sitemap", "core web vitals", "page speed", "schema markup", "title tag", "backlinks", "crawling issues", "robots.txt", "canonical", "E-E-A-T". Covers technical SEO, content strategy, schema markup, and measurement.
---

# SEO Fundamentals

Principles and decisions for search engine visibility. Covers technical SEO, E-E-A-T, Core Web Vitals, content strategy, and measurement — ordered by impact.

## When to Use

- User wants to rank higher in Google search results
- User has technical SEO issues (crawling, indexing, performance)
- User needs to optimize a page's meta tags, headings, or schema
- User wants to understand or improve E-E-A-T signals
- User needs to set up measurement for organic traffic

## Priority Framework

Address SEO in this order — fundamentals before tactics:

```
1. Technical foundation  — Can Google crawl and index the site?
2. E-E-A-T signals       — Does the content demonstrate expertise and trust?
3. Core Web Vitals       — Does the page load and respond fast enough?
4. Content quality       — Is the content the best answer for the query?
5. Schema markup         — Is structured data helping Google understand it?
6. Backlink signals      — Are authoritative sites linking to this content?
```

## Technical SEO

### Crawlability Checklist

- [ ] `robots.txt` exists and does not block important pages
- [ ] XML sitemap submitted to Google Search Console
- [ ] No broken internal links (404s on key pages)
- [ ] Canonical tags set on duplicate or near-duplicate pages
- [ ] HTTPS enabled across the entire site
- [ ] Clean, descriptive URL structure (no query parameter soup)

### Example: robots.txt

```
User-agent: *
Disallow: /admin/
Disallow: /private/

Sitemap: https://example.com/sitemap.xml
```

### Example: Canonical tag

```html
<link rel="canonical" href="https://example.com/canonical-page/" />
```

## E-E-A-T Framework

| Signal | What It Means | How to Demonstrate It |
|--------|--------------|----------------------|
| **Experience** | First-hand knowledge | Real examples, personal stories, case data |
| **Expertise** | Deep domain knowledge | Credentials, detailed technical coverage |
| **Authoritativeness** | Industry recognition | Backlinks, mentions, citations |
| **Trustworthiness** | Accuracy and transparency | Sources cited, corrections noted, HTTPS |

E-E-A-T is not a direct ranking factor — it is a quality signal that informs how Google evaluates a site over time.

## Core Web Vitals

| Metric | Target | What It Measures | Primary Cause of Failure |
|--------|--------|-----------------|--------------------------|
| **LCP** | < 2.5s | Largest visible element load time | Unoptimized images, slow server |
| **INP** | < 200ms | Interaction responsiveness | Heavy JavaScript on main thread |
| **CLS** | < 0.1 | Visual layout stability | Images without dimensions, late-loading ads |

Measure with: Google PageSpeed Insights, Search Console Core Web Vitals report.

## On-Page SEO

### Page Element Best Practices

| Element | Best Practice | Example |
|---------|--------------|---------|
| Title tag | 50-60 chars, primary keyword near front | `"React Testing Guide — Best Practices 2026"` |
| Meta description | 150-160 chars, compelling, includes keyword | `"Learn how to write reliable React tests..."` |
| H1 | One per page, matches search intent | `<h1>React Testing Guide</h1>` |
| H2-H6 | Logical hierarchy, secondary keywords | Subtopics that support the H1 |
| Alt text | Descriptive, not keyword-stuffed | `alt="Developer writing unit tests in VS Code"` |

## Schema Markup

Add structured data to help Google display rich results:

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "React Testing Best Practices",
  "author": { "@type": "Person", "name": "Jane Smith" },
  "datePublished": "2026-01-15",
  "dateModified": "2026-03-01"
}
```

Common schema types and when to use them:

| Type | Use Case |
|------|----------|
| `Article` | Blog posts, guides, news |
| `FAQPage` | Q&A sections (may show in search) |
| `Product` | E-commerce product pages |
| `Organization` | Company home/about pages |
| `BreadcrumbList` | Navigation trail in search results |

## Content SEO

### Quality Signals

| Factor | Why It Matters |
|--------|---------------|
| **Depth** | Comprehensive coverage satisfies search intent |
| **Freshness** | Updated content signals continued relevance |
| **Uniqueness** | Original data, insights, or framing earns citations |
| **Readability** | Clear writing reduces bounce rate |

### Ranking Factor Priority

1. Relevant, high-quality content matching search intent
2. Backlinks from authoritative sites in the same niche
3. Page experience (Core Web Vitals passing thresholds)
4. Mobile-friendliness
5. Technical SEO fundamentals in place

## Measurement

| What to Track | Tool |
|---------------|------|
| Keyword rankings | Google Search Console, Ahrefs |
| Organic traffic | Google Analytics |
| Core Web Vitals | PageSpeed Insights, Search Console |
| Indexing status | Google Search Console Coverage report |
| Backlinks | Ahrefs, Semrush |

## Anti-Patterns

- **Do not** stuff keywords — Google penalizes unnatural repetition.
- **Do not** publish AI-generated content without human review and original insights.
- **Do not** use multiple H1 tags on a single page.
- **Do not** set `noindex` on pages you want ranked.
- **Do not** ignore Core Web Vitals — they affect ranking, not just UX.
- **Do not** skip canonical tags on paginated or filtered URLs — duplicate content dilutes ranking signals.
