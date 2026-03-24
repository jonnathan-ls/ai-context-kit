# Source Evaluation Hierarchy

## Purpose

Establish a credibility assessment system that weights sources appropriately. Higher-tier sources carry more evidentiary weight. When sources conflict, tier determines priority.

---

## The Four-Tier System

### TIER 1: Primary, Direct, Authoritative

**Definition**: Official, primary authority sources directly applicable to decision

**Examples**:
- Government regulations & building codes (Brazil: ABNT norms, NBR standards)
- Official permits & approval requirements
- Regulatory compliance documentation
- Verified primary research (statistical surveys, peer-reviewed studies)
- Direct experience/data from known reliable sources

**Weight in Analysis**: HIGHEST
- These are fact base
- Can stand alone without corroboration
- Set legal/regulatory baseline
- Carry highest confidence in analysis

**Confidence if used**: 🟢 HIGH (95%+) if directly applicable

**Examples by Topic**:

| Topic | TIER 1 Sources |
|-------|---|
| Construction | Building codes (ABNT), municipal permits, structural standards |
| Finance | Official cost data, verified benchmarks, audited financials |
| Regulatory | Government regulations, compliance requirements, permit specifications |
| Technical | Industry standards (ISO, NBR), manufacturer specs |

### TIER 2: Secondary, Established, Credible

**Definition**: Credible secondary sources with recognized authority, professional standards, established methodologies

**Examples**:
- Professional association guidelines (CREA, CONFEA for construction)
- Industry benchmarks (published cost data, labor rates)
- Recognized analyst firms (Gartner, IDC where relevant)
- University research, government reports
- Expert whitepapers from recognized authorities
- Market research from established firms

**Weight in Analysis**: HIGH
- Strong supporting evidence
- Requires some corroboration for critical decisions
- Sets market/industry baseline
- Professional credibility assumed

**Confidence if used**: 🟡 MEDIUM-HIGH (75-90%) with TIER 1 support, or 🟡 MEDIUM (70-75%) standalone

**Examples by Topic**:

| Topic | TIER 2 Sources |
|-------|---|
| Construction | Labor rate surveys, material cost benchmarks, project case studies |
| Finance | Market analysis from investment banks, financial benchmarks |
| Market | Industry association reports, consultant analysis |
| Technical | Best practice guides, industry standards documentation |

### TIER 3: Tertiary, Supportive, Contextual

**Definition**: Commentary, analysis, and contextual information from credible but non-authoritative sources

**Examples**:
- Industry commentary (analyst blogs, trade journals)
- Case studies (similar projects, lessons learned)
- Expert opinions (attributed, from recognized experts)
- Published research with clear limitations noted
- Historical data (may not reflect current state)
- Aggregate user feedback/reviews

**Weight in Analysis**: MEDIUM
- Useful for context and pattern identification
- Can support but not replace tier-1/2 evidence
- Subject to author interpretation
- Valuable for identifying trends

**Confidence if used**: 🟠 LOW-MEDIUM (55-75%) and requires tier-1/2 support

**Examples by Topic**:

| Topic | TIER 3 Sources |
|-------|---|
| Construction | Contractor reviews, project blogs, forum discussions (with caveats) |
| Finance | Market commentary, analyst opinions, industry blog posts |
| Market | Consultant reports where methodology unclear, trend commentary |
| Technical | Community best practices, StackOverflow threads, expert Q&A |

### TIER 4: Supplementary, Anecdotal, Background

**Definition**: Discussion, anecdotes, and background information; minimal evidentiary weight

**Examples**:
- Forum discussions, Reddit threads, social media
- Anecdotal evidence ("I heard someone say...")
- Blog posts without source citations
- Internal rumors or hearsay
- Outdated information (no longer current)
- Entertainment content discussing topic

**Weight in Analysis**: LOW/MINIMAL
- Use only for background color
- Cannot stand alone
- Highly subject to bias
- Useful for identifying questions, not answers

**Confidence if used**: 🔴 UNVERIFIED or "context only"

**Examples by Topic**:

| Topic | TIER 4 Sources |
|-------|---|
| Construction | Contractor anecdotes, forum complaints, "I know someone who..." |
| Finance | Bar talk economics, social media speculation |
| Market | Forum discussions without data, internet rumors |
| Technical | Hypothetical "what-ifs", unverified claims |

---

## Credibility Assessment Scorecard

For each source, evaluate:

| Criterion | TIER 1 | TIER 2 | TIER 3 | TIER 4 |
|-----------|--------|--------|--------|--------|
| **Authority** | Official/primary | Recognized expert | Credible commentator | Casual source |
| **Methodology** | Rigorous/verified | Professional standard | Clear but limited | Unclear/vague |
| **Recency** | Current | Current or timely | May be dated | Often outdated |
| **Sourceability** | Fully traceable | Traceable | Partially traceable | Not traceable |
| **Bias Risk** | Low (official) | Moderate | Moderate-High | High |
| **Availability** | Complete | Accessible | May require access | Public |
| **Verification** | Verifiable | Professional | Checkable | Not verifiable |

---

## Using the Hierarchy in Analysis

### When Sources Agree (Same Finding)

```
TIER 1 + TIER 2 confirm finding
  → 🟢 HIGH confidence (95%+)
  → Use as fact base

TIER 2 + TIER 3 both support
  → 🟡 MEDIUM confidence (75-85%)
  → Strong supporting evidence, but verify further if critical

TIER 3 + TIER 4 agree only
  → 🟠 LOW confidence (50-60%)
  → Indicator only; don't make decisions on this alone
```

### When Sources Conflict

```
TIER 1 vs. Other Tiers
  → TIER 1 wins (official authority)
  
TIER 2 vs. TIER 3
  → TIER 2 typically wins (established vs. commentary)
  
TIER 2 vs. TIER 2 (Different sources)
  Assess: Recency, sample size, methodology transparency
  
Same Tier, Different Conclusions
  Assess: Data quality, sample representativeness, potential bias
```

**Example**:
```
BUILDING CODES (TIER 1) say: Maximum 3-story residential
CONTRACTOR BLOG (TIER 3) says: "Everyone builds 4-5 stories"

Analysis: TIER 1 is authoritative. Blog represents anecdote/risk.
Recommendation: Code compliance required; contractor claims suggest
enforcement gap that should be investigated.
```

### Missing Sources (Gaps)

```
Critical Decision Area: NOT covered by any source
  → Mark as GAP
  → Research it OR
  → Note as assumption ("assuming X is true...")
  → Flag as risk if assumption critical

Do NOT make up data to fill gaps.
```

---

## Practical Application

### Step 1: Source Inventory

Create table for topic:

| Source | Tier | Topic | Credibility Notes | Limitations |
|--------|------|-------|--|--|
| ABNT Building Code | 1 | Technical standards | Official government | Generic; local variation needed |
| CREA Labor Report | 2 | Labor costs | Professional association | Salary data; actual rates vary |
| Contractor Blog | 3 | Market trends | Contractor perspective | Anecdotal |
| Forum Discussion | 4 | Project tips | Crowd-sourced | No verification possible |

### Step 2: Assess Coverage

- Which tiers are well-represented? ✓
- Which are missing? 
- Major gaps?

### Step 3: Weight Analysis

When presenting findings:
- TIER 1 sources carry highest weight
- Mix of TIER 1 + 2 = strong evidence
- TIER 3 alone = supporting context only
- TIER 4 = don't use for facts

### Step 4: Confidence Assignment

For each finding:
```
Finding: "Labor rates in São Paulo average R$ X/day"
Source: CREA 2024 Labor Report (TIER 2)
Confidence: 🟡 MEDIUM (75%) - Professional source but aggregate data.
Caveat: Actual rates vary by skill level, project type, negotiation.
```

---

## Special Cases

### Academic/Research Sources

```
PEER-REVIEWED STUDY (published in recognized journal)
  → Typically TIER 2 (professional, but may have limitations)
  → Confidence depends on sample size, methodology
  → Note publication date (old research = less current)

UNIVERSITY REPORT (from established institution)
  → Typically TIER 2-3 (depends on methodology clarity)
  → More credible if funded independently
  → Less credible if funded by vendor with agenda

THESIS/DISSERTATION
  → Typically TIER 3 (research but not peer-reviewed)
  → Value depends on advisor, institution
```

### Expert Opinions

```
ATTRIBUTED EXPERT OPINION (from recognized expert in field)
  → Typically TIER 3
  → More credible if data-supported
  → Less credible if just assertion

UNNAMED "INDUSTRY EXPERT"
  → Typically TIER 4
  → Cannot verify credibility or potential bias
  → Useful for ideas, not evidence
```

### Industry Data

```
PUBLISHED BENCHMARKS (from recognized source)
  → Typically TIER 2
  → More credible if methodology transparent
  → Note: Benchmarks may not match your specifics

INTERNAL DATA (from company's own experience)
  → Can be TIER 1-2 if well-documented
  → How verified? How recent?
  → Note: May not be representative of market
```

---

## Quality Control Checklist

When evaluating source credibility:

- [ ] What tier is this source? (be honest)
- [ ] Who published/verified it? (credible?)
- [ ] When was it published? (current enough?)
- [ ] What's the methodology? (rigorous?)
- [ ] What's the potential bias? (author incentives?)
- [ ] Is it directly applicable? (or extrapolation needed?)
- [ ] What are stated limitations? (methodology caveats?)
- [ ] Can reader verify independently? (traceable?)
- [ ] Does it contradict other sources? (if so, assess credibility)
- [ ] What confidence level is appropriate? (🟢🟡🟠🔴)

---

## Common Mistakes to Avoid

❌ **Treating TIER 3 as TIER 1**
- "The contractor said so" does NOT override building codes
- "I read online" is not official information

❌ **Assuming recent = accurate**
- Dated TIER 1 source > recent TIER 4 rumor
- Currency matters less than authority

❌ **Hiding contradictions**
- Multiple sources disagree?
- Surface it, don't average them

❌ **Mixing anonymous opinion with attributed data**
- "People say X" ≠ "Survey found X"
- Attribute and tier appropriately

✅ **DO: Explicitly state tier for each source**
✅ **DO: Justify confidence based on tier + methodology**
✅ **DO: Flag gaps where critical sources missing**
✅ **DO: Surface contradictions for resolution**
