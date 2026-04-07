---
name: geo-fundamentals
description: Generative Engine Optimization (GEO) specialist. Use this skill whenever the user wants their content to be cited by AI-powered search engines like ChatGPT, Claude, Perplexity, or Gemini. Triggers on "GEO", "AI search", "cited by AI", "Perplexity ranking", "ChatGPT mentions", "AI citations", "generative search", "llms.txt", "get cited in AI responses", "show up in ChatGPT". Covers content structure, entity building, schema markup, AI crawler access, and citation measurement.
---

# GEO Fundamentals

Optimization strategy for AI-powered search engines. GEO is distinct from traditional SEO — the goal is not to rank #1 on Google, but to be cited as a source in AI-generated answers.

## When to Use

- User wants their content cited by ChatGPT, Perplexity, Claude, or Gemini
- User is creating content strategy for AI-search visibility
- User wants to understand how AI engines select sources
- User needs to configure `llms.txt` or crawler access
- User wants to measure AI citation rate

## SEO vs GEO

| Aspect | SEO | GEO |
|--------|-----|-----|
| Goal | Rank #1 on Google SERP | Be cited in AI-generated answers |
| Platform | Google, Bing | ChatGPT, Perplexity, Claude, Gemini |
| Primary metric | Click-through rate, ranking position | Citation rate, brand mentions in AI |
| Content focus | Keywords, intent matching | Entity clarity, unique data, authoritative framing |
| Success signal | Traffic from search | "According to [Brand]..." in AI answers |

## AI Engine Landscape

| Engine | Citation Style | Key Opportunity |
|--------|----------------|-----------------|
| **Perplexity** | Numbered [1][2] inline | Highest citation rate among AI engines |
| **ChatGPT** | Inline references, footnotes | Custom GPTs can surface specific sources |
| **Claude** | Contextual citations | Long-form, well-structured content |
| **Gemini** | Sources section | SEO/GEO crossover — Google index matters |

## How AI Engines Select Sources (RAG Factors)

AI engines use Retrieval-Augmented Generation to select citations:

| Factor | Approximate Weight | Optimization |
|--------|-------------------|----|
| Semantic relevance | ~40% | Match the exact question being asked |
| Keyword presence | ~20% | Include the query terms naturally |
| Authority signals | ~15% | Backlinks, Wikipedia, Knowledge Panel |
| Freshness | ~10% | Add publication and update dates |
| Source diversity | ~15% | Be a standalone authoritative source |

## Content That Gets Cited

Structure content to be easy for AI engines to extract:

| Element | Why It Gets Cited | Example |
|---------|-------------------|---------|
| **Original statistics** | Unique, citable data AI can reference | "In our 2026 survey, 73% of developers..." |
| **Clear definitions** | AI extracts direct answers | "GEO is the practice of optimizing content for AI citation." |
| **Step-by-step guides** | Actionable, structured format | Numbered steps with clear outcomes |
| **Comparison tables** | Machine-readable structured info | Tables like this one |
| **Expert quotes** | Authority transfer to the source | Named, titled quotes with context |
| **FAQ sections** | Maps directly to conversational AI queries | "Q: What is GEO? A: ..." |

## GEO Content Checklist

### Structure

- [ ] Question-based title (matches how users ask AI)
- [ ] TL;DR or summary at the top of the page
- [ ] Clear definitions for key terms
- [ ] Original data with source attribution
- [ ] FAQ section with 3-5 direct questions and answers
- [ ] Publication date and "Last updated" timestamp
- [ ] Named author with credentials

### Technical

- [ ] Article schema with `datePublished` and `dateModified`
- [ ] Person schema for author
- [ ] FAQPage schema on Q&A sections
- [ ] Page loads in under 2.5 seconds (LCP)
- [ ] Clean HTML with logical heading hierarchy

### Example: Article Schema

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "What is GEO? Guide to AI Search Optimization",
  "author": {
    "@type": "Person",
    "name": "Jane Smith",
    "jobTitle": "SEO Director"
  },
  "datePublished": "2026-01-10",
  "dateModified": "2026-04-01"
}
```

## Entity Building

AI engines rely on entity graphs. Build yours:

| Action | Purpose |
|--------|---------|
| Claim Google Knowledge Panel | Entity recognition by Google/Gemini |
| Consistent NAP across web | Entity consolidation (name, address, phone) |
| Wikipedia entry (if notable) | High-authority entity signal |
| Industry mentions and citations | Authority reinforcement |

## AI Crawler Access (`robots.txt`)

Control which AI engines can index your content:

```
# Allow all AI crawlers (recommended for GEO)
User-agent: GPTBot
Allow: /

User-agent: Claude-Web
Allow: /

User-agent: PerplexityBot
Allow: /

# To block OpenAI training (does not affect search citations)
User-agent: GPTBot
Disallow: /
```

## Measurement

| Metric | How to Track |
|--------|-------------|
| AI citations | Manually query AI engines with your target questions |
| Brand mentions in AI | Search "According to [Brand]" in Perplexity, ChatGPT |
| AI-referred traffic | UTM parameters in linked content (`utm_source=ai`) |
| Competitor citation share | Compare citation frequency for same query |

## Anti-Patterns

- **Do not** publish content without dates — AI engines deprioritize undated sources.
- **Do not** use vague attributions ("some experts say") — name sources explicitly.
- **Do not** skip author information — anonymous content scores low on E-E-A-T.
- **Do not** write thin content — AI engines extract from comprehensive sources.
- **Do not** block all AI crawlers indiscriminately — this removes you from citation pools entirely.
- **Do not** optimize for GEO without a technical SEO foundation — Google's index still feeds Gemini.
