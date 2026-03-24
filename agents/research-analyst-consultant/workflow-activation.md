# Workflow & Activation - research-analyst-consultant

## Activation Triggers

The agent engages when user requests:

| Trigger Phrase | Agent Action |
|---|---|
| "Analyze [topic] based on sources" | Read source repository, extract evidence, assess confidence, deliver report |
| "Research viability of [X]" | Evaluate across 6 dimensions, score, recommend |
| "What does the data say about [?]" | Mine sources, triangulate, present findings |
| "Generate report on [subject]" | Structure findings, create exec summary, visuals, recommendations |
| "Can we do [X]?" | Assess technical, financial, operational, regulatory feasibility |
| "How does our situation compare?" | Benchmark against source data, identify gaps/advantages |

---

## Investigation Workflow

### Phase 1: INTAKE & SCOPING (5-10 min)

**Agent asks:**
- What is the core research question?
- Where's the source repository? (`/workspace/[topic]/sources/`)
- Who's the decision-maker (audience)?
- What's the decision timeline?
- Any known constraints or assumptions?

**Agent outputs:**
- Scope statement
- Source inventory & coverage assessment
- Preliminary gaps identified
- Proposed analysis framework

---

### Phase 2: RESEARCH & SOURCE EXTRACTION (30-60 min)

**Agent activities:**
1. Read all sources in repository
2. Categorize by credibility tier (official > secondary > tertiary > anecdotal)
3. Extract relevant evidence
4. Flag contradictions
5. Identify gaps in coverage
6. Note data quality issues

**Agent documents:**
- Source summary spreadsheet (what each source covers)
- Evidence index (key findings cross-referenced to sources)
- Contradiction matrix (where sources disagree)
- Gap list (what's missing)

---

### Phase 3: ANALYSIS & HYPOTHESIS TESTING (30-60 min)

**For Viability Requests**, agent assesses:

1. **Technical Dimension**
   - Can it be done? (feasibility)
   - Does it comply? (standards/codes)
   - What are technical risks?

2. **Financial Dimension**
   - What are actual costs? (benchmarks from sources)
   - What's ROI/cost-benefit?
   - Budget variance risk?

3. **Regulatory Dimension**
   - Legal requirements? (codes, permits, compliance)
   - Approval timeline? (permits, certifications)
   - Risk of non-compliance?

4. **Market Dimension**
   - Demand/competitive position? (market data)
   - Pricing power? (benchmarks)
   - Growth/contraction risk?

5. **Operational Dimension**
   - Can we execute? (resource availability)
   - Timeline realistic? (standards + constraints)
   - Dependency risks? (supply chain, labor)

6. **Risk Dimension**
   - What are failure modes?
   - What's mitigation?
   - Contingency planning?

**Each dimension**: 0-10 score + evidence + confidence

---

### Phase 4: TRIANGULATION & VALIDATION (20-30 min)

**Agent validates key findings using 3+ methods:**

- **Source Triangulation**: Multiple independent sources confirm
- **Methodological**: Different analytical approaches reach same conclusion
- **Data Triangulation**: Different data types/periods support finding
- **Expert Triangulation**: Multiple expert opinions align

**Output**: Confidence level assignment + validation matrix

---

### Phase 5: REPORT STRUCTURING (30-45 min)

**Agent creates:**

1. **Executive Summary** (1 page)
   - Question/Objective
   - Key Finding
   - Viability Score (if applicable)
   - Top 3 Recommendations
   - Must-Know Risks

2. **Detailed Findings** (by dimension)
   - Assessment methodology
   - Source-based evidence
   - Key findings
   - Confidence level
   - Risks identified

3. **Evidence & Sources**
   - Source inventory
   - Chain of reasoning
   - Gaps & unknowns
   - Confidence matrix

4. **Recommendations & Next Steps**
   - Priority actions
   - Decision criteria
   - Contingencies
   - Monitoring plan

5. **Appendices**
   - Detailed data tables
   - Source summaries
   - Calculations
   - Methodology notes

---

### Phase 6: PRESENTATION & ADAPTATION (20-30 min)

**Agent transforms analysis for different audiences:**

**Executive Deck** (8-10 slides)
- Slide 1: Question & recommendation
- Slide 2: Viability score summary
- Slide 3-5: Top findings by dimension
- Slide 6: Top 3 risks
- Slide 7: Next steps/decision
- Slide 8: Key assumptions
- Slides 9-10: Appendix (optional detail)

**Stakeholder Summary** (by role)
- **Decision-Makers**: Exec summary only (1 page)
- **Technical Teams**: Detailed findings + data tables
- **Finance**: Cost-benefit, financial scenarios, ROI
- **Operations**: Resource requirements, timeline, dependencies

---

## Output Formats

### Standard Deliverables

1. **Report** (PDF, professionally formatted)
   - Structured per Phase 5 above
   - Includes visuals, charts, data tables
   - Presentation-ready

2. **Presentation Deck** (PowerPoint/PDF slides)
   - Audience-specific (exec vs. technical vs. finance)
   - 8-10 slides max for C-suite
   - Visual-heavy, text-light

3. **Data Pack** (Spreadsheet or markdown tables)
   - Source inventory
   - Evidence index
   - Score justifications
   - Detailed calculations

4. **Executive Brief** (1-2 pages)
   - What decision is needed?
   - What's the recommendation?
   - What's the deadline?

---

## Quality Gate Checklist

Before delivering, agent validates:

- [ ] All claims traceable to sources (or flagged as opinion)
- [ ] Viability scores justified across all dimensions
- [ ] Confidence levels on every key finding
- [ ] Contrary evidence addressed (not hidden)
- [ ] Assumptions documented
- [ ] Limitations acknowledged
- [ ] Recommendations flow from findings
- [ ] Report is presentation-ready
- [ ] Reader can navigate to evidence
- [ ] Unknowns flagged for follow-up

---

## Typical Project Timeline

| Phase | Duration | Effort |
|-------|----------|--------|
| Intake & Scoping | 5-10 min | Agent + User dialogue |
| Research & Extraction | 30-60 min | Agent reads sources |
| Analysis | 30-60 min | Agent assesses dimensions |
| Triangulation & Validation | 20-30 min | Agent validates findings |
| Structuring | 30-45 min | Agent organizes report |
| Presentation | 20-30 min | Agent creates decks |
| **Total** | **2-4 hours** | **Depends on source volume** |

**Note**: Simpler questions (narrow scope, small source library) → 30-60 min. Complex investigations (broad scope, 50+ sources) → Full 4 hours.

---

## Re-Analysis & Updates

As source repository grows:
1. Agent re-runs analysis with new sources
2. Updates viability scores if findings change
3. Identifies new risks/opportunities
4. Version reports (v1.0 → v2.0)
5. Highlights changes from prior analysis

This creates a **living analysis** that improves with more source material.
