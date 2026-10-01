# Ansible adoption — CRM title / persona analysis

**Source:** `Ansible_Customer_Contact_Role.csv`  
**Filter (per user):** Ansible customers in the **adoption** stage **and** member of an Ansible opportunity  
**Grain:** Unique job title × Title Persona × Persona Segment, with opportunity count  
**Totals:** 8,293 title rows · ~46,274 opportunity-weight sum  

---

## Headline findings

| Title Persona (seniority) | Unique titles | Opp weight |
|---|---:|---:|
| Default (IC / unclassified seniority) | 4,566 | 23,583 |
| Managers | 1,644 | 10,090 |
| Directors | 964 | 6,040 |
| CXOs | 630 | 3,794 |
| XVPs | 489 | 2,767 |

| Persona Segment | Unique titles | Opp weight | Share of opps |
|---|---:|---:|---:|
| Default | 3,064 | 14,174 | 30.6% |
| AppDev ITDM | 1,394 | 10,185 | 22.0% |
| IT C-Suite | 609 | 4,390 | 9.5% |
| System Administrator | 803 | 4,275 | 9.2% |
| Developer | 712 | 3,819 | 8.3% |
| Enterprise Architect | 388 | 2,358 | 5.1% |
| Business Analyst | 389 | 1,946 | 4.2% |
| C-Suite | 244 | 1,051 | 2.3% |
| Network Architect | 179 | 881 | 1.9% |
| Procurement | 93 | 775 | 1.7% |
| Platform Engineer | 96 | 513 | 1.1% |
| Automation Architects | 70 | 490 | 1.1% |
| Line of Business | 56 | 413 | 0.9% |
| Network Admin / Ops | 83 | 369 | 0.8% |
| Site Reliability Engineer | 43 | 256 | 0.6% |
| IT Operations Leader | 25 | 161 | 0.3% |
| IT Security / Compliance | 15 | 101 | 0.2% |
| Data Scientist IC | 28 | 105 | 0.2% |
| Data Scientist Leader | 2 | 12 | &lt;0.1% |

**Implication:** Named segments cover ~**69%** of opportunity weight. The **Default** segment alone is ~**31%** and needs cleanup before auto-assign. **AppDev ITDM** is the dominant named buying-group signal for adoption contacts.

---

## Recommended AJO role mapping (v1)

| AJO role | Persona segments to include | Opp weight | Notes |
|---|---|---:|---|
| **Practitioner** | System Administrator, Developer, Platform Engineer, Network Admin / Ops, SRE, Data Scientist IC, IT Security / Compliance | ~20% | Mostly Title Persona = Default (IC). Seniority Managers in these segments can dual-map to Champion if needed. |
| **Influencer** | Enterprise Architect, Network Architect, Automation Architects | ~8% | Strong architecture / standards lane; aligns with network + automation tactics. |
| **Champion** | AppDev ITDM, IT Operations Leader, Line of Business | ~23% | AppDev ITDM is Manager/Director-heavy — internal drivers of adoption. |
| **Decision Maker** | IT C-Suite, C-Suite | ~12% | CXO / XVP / Director-heavy; Expand + Renew branches. |
| **Exclude / Other (v1)** | Procurement; Persona Segment = Default | ~32% | Procurement = buying process, not adoption nurture. Default = too noisy for auto-assign. |

**Hold for review (do not auto-map yet):**

- **Business Analyst (~4%)** — many titles look like sourcing / consulting / misc; not a clean Champion signal.
- **Automation Architects** — segment is right thematically, but top titles show some misfiles (e.g. unrelated Program Manager). Prefer title-keyword reinforce (`Automation`, `Architect`, `AIOps`) in auto-assign rules.
- **Developer** — useful for Practitioner, but includes managers/VPs and non-English generics; combine segment + title keywords.

### Seniority tip for auto-assign

Within **AppDev ITDM**, opportunity weight is mostly **Managers (46%)** and **Directors (30%)** — treat as Champion (and Influencer when title contains Architect / Automation).  
Within **System Administrator** / **Developer** / **Platform Engineer**, weight is mostly **Default** — treat as Practitioner.

---

## Interim GenStudio persona bridge

| GenStudio persona | Primary CRM segments | AJO roles |
|---|---|---|
| **Champion** | AppDev ITDM, IT Operations Leader, Line of Business | Champion |
| **Technical Practitioner / Architect** | System Administrator, Platform Engineer, SRE, Network Admin / Ops, Enterprise / Network / Automation Architects | Practitioner, Influencer |
| **Developer** | Developer (IC titles) | Practitioner |

---

## Data-quality caveats

1. **Default segment is large** — do not use as a positive inclusion rule; use for a cleanup backlog.
2. **Segment labels are imperfect** — spot-check Automation Architects, Business Analyst, Developer before hard-coding.
3. **Opportunity weight ≠ unique people** — one contact/title can touch many opportunities; good for prioritization, not for headcount.
4. **Adoption-stage + opportunity member** filter already applied upstream — this list is already post-sale leaning, which fits the AJO adoption use case.

---

## Suggested next CRM / DA steps

1. Export **person-level** counts (not only title uniqueness) for the mapped segments.  
2. Build title-keyword overlays for Architect / Automation / Network / Admin / Manager.  
3. Sample 50 Default-segment titles for reclassification rules.  
4. Tech Sales workshop: confirm required counts for Champion + Practitioner + Decision Maker completeness.  
5. Drop Procurement from adoption journey membership (keep available for commercial journeys only).
