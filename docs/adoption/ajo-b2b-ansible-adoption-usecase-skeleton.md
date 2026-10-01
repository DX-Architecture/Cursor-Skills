# AJO B2B Use Case Skeleton — Ansible Adoption Experience

**Status:** Draft skeleton (personas TBD)  
**Product / solution interest:** Red Hat Ansible Automation Platform (AAP)  
**Orchestration surface:** Adobe Journey Optimizer B2B Edition (account journeys + buying groups)  
**Primary trigger thesis:** Product usage **or lack of usage** (plus proxy signals while AAP EoA is incomplete) to nurture the right buying-group roles  
**Sources in `/adoption`:** Adoption Framework Primary Deck (Jun 2026), Evidence of Adoption Overview (Jun 2026), ALG maturity / Automation sales-tactics screenshots  
**Related contacts (from decks):** Ansible BU — Tricia McConnell; Adoption Framework — Corinne Russo / Britni Coble; EoA — Bianca Gallina; Experiences & Signals — Jay Hall  

---

## 1. Why / What / How / Dependencies / DA Lead

### Why
Customers buy AAP but do not consistently progress from entitlement → active automation → multi-team / multi-use-case value. Fragmented consumption metrics alone mislead (telemetry gaps, no entitlement context, false under-deployment). Without role-aware nurture, Marketing over-messages practitioners, under-enables champions, and Sales/CS miss risk and expansion moments.

### What
An **always-on AJO B2B account journey** for entitled AAP accounts that:

1. Builds / refreshes an **AAP solution-interest buying group** with required roles.
2. Classifies the account on **adoption maturity** (Initial → Innovator) using available **usage + proxy signals**.
3. Branches nurture and sales alerts by **maturity gap** and **role** (usage risk vs expansion readiness).
4. Measures impact via engagement, completeness, maturity movement, and renewal/expansion outcomes.

### How (AJO B2B pattern)

| Layer | Approach |
|---|---|
| Unit of orchestration | **Account** (not person-only) |
| Solution interest | Ansible Automation Platform |
| Membership | Buying group role template + auto-assign rules |
| Readiness | Completeness score + engagement score + maturity/proxy band |
| Triggers | Usage / non-usage events, inactivity windows, entitlement without activation, proficiency/perception proxies |
| Actions | Role-specific email/SMS, content offers, sales alerts, suppress when high-touch owns the account |
| Exit / handoff | Sales-ready / risk escalation / maturity advance / suppress lists |

### Dependencies

| Dependency | Notes | Status |
|---|---|---|
| AAP EoA model | Monthly account maturity 1–5 across 4Ps | **Blocked — telemetry gaps** (EoA deck) |
| Telemetry-agnostic proxies | Needed for disconnected / low-confidence accounts | Roadmap (CY26) |
| Signal → AEP/RT-CDP B2B | Account + person attributes for journey conditions | TBD — DA |
| Buying group role template | AAP-specific roles + assignment filters | **Draft placeholders below** |
| Personas / messaging map | Copy & offer personalization | **TBD — see §6** |
| Content / offer catalog by stage & role | Labs, learning, CoE, Services, references | Partial (framework + tactics slide) |
| Conflict / frequency rules | vs Marketo AAP nurtures, AGI, ServiceNow playbook | TBD |
| Sales / RHSC alert path | Risk & expansion handoffs | Pattern exists (DDP / Sales Assistant) |

### DA Lead
**TBD** — assign Analytics / AEP owner for signal schema, confidence bands, and journey-eligible audiences.

---

## 2. Business outcomes

| Outcome | Working definition |
|---|---|
| Faster time-to-value | Move accounts from Initial/Developing → Operational on usage + proficiency proxies |
| Protect renewal | Detect “quiet but stuck” accounts (low usage / high basic support / poor sentiment) before renewal window |
| Expand responsibly | Surface expansion only when usage breadth + perception support it (not volume spam) |
| Role coverage | Raise buying-group completeness for required AAP roles |
| Coordinated motion | Digital (AJO) + high-touch (Tech Sales / CS) share the same maturity language |

---

## 3. Scope

### In scope (v1 skeleton)
- Post-sale / entitled AAP accounts (Adopt focus; Onboard and Renew as adjacent stages)
- Account journey with role-aware branches for **usage risk** and **healthy usage / expand**
- Proxy-first signals until AAP EoA is production-ready
- Placeholder AJO roles + interim GenStudio persona mapping

### Out of scope (v1)
- Net-new acquire / Learn-only journeys
- Full AAP EoA-dependent branching (design for, do not block on)
- In-app Intercom/Amplitude orchestration (adjacent channel; not AJO B2B core)
- Persona-finalized creative production

---

## 4. Lifecycle alignment

Adoption Framework spine: **Learn → Onboard → Adopt → Expand → Renew**

| Lifecycle stage | AJO job for this use case | Maturity focus (ALG / EoA) |
|---|---|---|
| Onboard | Confirm activation; first successful automation milestone | 1 Initial → 2 Developing |
| Adopt | Deepen usage across teams/features; raise proficiency | 2 → 3 Operational |
| Expand | Multi-domain / platform breadth when ready | 3 → 4 Optimizing |
| Renew | Risk remediation + value proof for economic buyers | Any; prioritize low maturity + near renewal |

**v1 primary stage:** Adopt (with Onboard entry and Renew-risk side door).

---

## 5. Buying group — role placeholders

AJO B2B solution interest: **Red Hat Ansible Automation Platform**

Use AJO default role types as **placeholders** until AAP-specific role templates and personas are approved. Completeness defaults to ≥1 member per required role unless Sales defines otherwise.

| AJO role (placeholder) | Required? (v1 proposal) | Job in adoption journey | Typical concerns (working) |
|---|---|---|---|
| **Practitioner** | Yes | Operate AAP day-to-day; first jobs → advanced automation | Skills, how-to, friction, time-to-first-success |
| **Champion** | Yes | Internal advocate; drives multi-team adoption | Proof, enablement kits, CoE / community of practice |
| **Influencer** | Yes | Architecture / standards; expands use cases | Patterns, integrations, governance, trusted content |
| **Decision Maker** | Yes (for Expand / Renew branches) | Budget, renewal, expansion | Outcomes, risk, ROI, Services |
| **Executive Steering Committee** | No (v1) | Optional for large enterprise | Strategy / AIOps / automation as imperative |
| **Other** | Catch-all | Do not primary-nurture | — |

### Role × 4P ownership (working heuristic)

| Dimension | Primary roles to nurture | Secondary |
|---|---|---|
| **Product Usage** | Practitioner, Influencer | Champion |
| **Proficiency** | Practitioner | Champion (peer enablement) |
| **Performance** | Decision Maker, Champion | Influencer |
| **Perception** | Champion, Decision Maker | Influencer |

---

## 6. Personas & titles (CRM-informed — messaging still TBD)

### Status
**CRM title/persona inventory is in** (`Ansible_Customer_Contact_Role.csv` → analysis in `crm-title-persona-analysis.md`).  
Filter: adoption-stage Ansible customers who are members of an Ansible opportunity (8,293 title rows).  

**Messaging personas are still TBD** (GenStudio copy preferences not locked). Use the CRM **Persona Segment** map below for AJO role auto-assign drafts; do not block journey structure on final GenStudio persona copy.

### CRM → AJO role map (v1 proposal)

| AJO role | Include Persona Segments | ~Opp weight | Notes |
|---|---|---:|---|
| **Practitioner** | System Administrator, Developer, Platform Engineer, Network Admin / Ops, SRE, Data Scientist IC, IT Security / Compliance | ~20% | Mostly IC / Default seniority |
| **Influencer** | Enterprise Architect, Network Architect, Automation Architects | ~8% | Reinforce with title keywords (`Architect`, `Automation`, `AIOps`) |
| **Champion** | AppDev ITDM, IT Operations Leader, Line of Business | ~23% | AppDev ITDM is the largest named segment (~22%); Manager/Director-heavy |
| **Decision Maker** | IT C-Suite, C-Suite | ~12% | CXO / XVP / Director-heavy; Expand + Renew |
| **Exclude / Other** | Procurement; Persona Segment = **Default** | ~32% | Default too noisy for auto-assign; Procurement ≠ adoption nurture |

**Hold for review:** Business Analyst (~4%) — many sourcing/consulting titles; do not auto-map to Champion yet.

### Top named segments (by opportunity weight)

| Rank | Persona Segment | Opp share | Primary AJO role |
|---|---|---:|---|
| 1 | AppDev ITDM | 22.0% | Champion |
| 2 | IT C-Suite | 9.5% | Decision Maker |
| 3 | System Administrator | 9.2% | Practitioner |
| 4 | Developer | 8.3% | Practitioner |
| 5 | Enterprise Architect | 5.1% | Influencer |
| — | Default (unclassified) | 30.6% | Exclude from auto-assign |

### Interim GenStudio bridge (content only)

| GenStudio persona | Primary CRM segments | AJO roles |
|---|---|---|
| Champion | AppDev ITDM, IT Operations Leader, Line of Business | Champion |
| Technical Practitioner / Architect | SysAdmin, Platform Eng, SRE, Network Admin/Ops, Enterprise / Network / Automation Architects | Practitioner, Influencer |
| Developer | Developer (IC titles) | Practitioner |

### Remaining validation steps
1. Person-level counts (not only unique titles) for mapped segments.
2. Title-keyword overlays + sample reclassify 50 Default titles.
3. Tech Sales completeness workshop (required role counts).
4. Confirm Business Analyst and Automation Architects segment quality.
5. Lock GenStudio messaging preferences per persona after PMM review.

---

## 7. Entry, branch, and exit logic

### Entry (account qualifies when)
Working draft — finalize with DA:

- Account has **AAP entitlement / subscription** active, **and**
- Solution interest = AAP buying group exists or can be created, **and**
- At least one marketable member in a required role **or** completeness play is allowed to recruit missing roles, **and**
- Not on global suppress / competing exclusive journey (TBD).

### Primary branches

```
Account enters (entitled AAP)
 ├─ Missing required roles → Completeness / role-recruitment play
 ├─ Usage RISK (entitled + low/no usage OR stalled inactivity)
 │    ├─ Practitioner / Influencer → Proficiency + first-value nurture
 │    └─ Champion / Decision Maker → Risk narrative + enablement / Services CTA
 ├─ Usage HEALTHY but narrow (single team / limited features)
 │    └─ Influencer / Champion → “Automate at scale” / CoE / reuse patterns
 ├─ Usage HEALTHY + expansion signals
 │    └─ Decision Maker / Champion → Expand offers (domain, AIOps, integrations)
 └─ Near renewal + low maturity → Renew-risk play + sales alert
```

### Exit / suppress (draft)
- Maturity band advances past journey objective (e.g. sustained Operational+)
- Sales/CS owns active high-touch adoption task (suppress digital or switch to air cover only)
- Opt-down / unsubscribe / legal suppress
- Account loses AAP entitlement
- Frequency / conflict caps hit

---

## 8. Signal inventory (usage + proxies)

**Constraint:** AAP EoA is **blocked on telemetry gaps**. Design journeys with **confidence bands** (EoA: High / Medium / Low) and prefer multi-signal rules.

### Product Usage (breadth)
| Signal (working) | Risk example | Expansion example | Confidence if telemetry thin |
|---|---|---|---|
| Activation (installed / first controller activity) | Entitled, never activated | — | Medium with entitlements |
| Consumption (jobs / hosts / capacity) | Flat or decaying activity | Growing consumption | Needs telemetry or proxy |
| Feature usage | Basics only; no advanced features | Advanced / multi-feature | Low until AAP EoA |
| Active users / teams | Single-team automation | Multi-team | Proxy via portal + CRM |
| Age / tenure since purchase | Long tenure + low usage | — | High (subscription data) |

### Performance / Proficiency / Perception (proxies)
| Dimension | Example inputs (from EoA) | Journey use |
|---|---|---|
| Performance | Update frequency, deployment health, support severity | Stability risk → Decision Maker / Champion |
| Proficiency | Docs/Portal visits, support complexity, learning paths/certs (TBA) | Low proficiency → Practitioner enablement |
| Perception | CES, targeted feedback, advocacy (TBA) | Negative sentiment → fix-it; positive → reference/expand |

### v1 “good enough” trigger recipes (proxy-friendly)

| Trigger name | Logic (draft) | Primary roles | Intent |
|---|---|---|---|
| `AAP_NO_ACTIVATION` | Entitled ≥ N days, no activation signal | Practitioner, Champion | Onboard / first value |
| `AAP_USAGE_STALL` | Prior activity, then inactivity ≥ X days | Practitioner, Influencer | Re-engage / unblock |
| `AAP_LOW_BREADTH` | Usage present but single-team / limited feature proxies | Champion, Influencer | Scale adoption |
| `AAP_PROFICIENCY_GAP` | High basic support + low learning engagement | Practitioner | Skills / labs |
| `AAP_PERCEPTION_RISK` | Negative CES / feedback | Champion, Decision Maker | Value proof / CS handoff |
| `AAP_EXPAND_READY` | Healthy usage + engagement + completeness OK | Decision Maker, Champion | Domain / AIOps / integrations |
| `AAP_RENEW_RISK` | Renewal ≤ Y days + low maturity / risk signals | Decision Maker + sales alert | Protect ARR |

---

## 9. Role × maturity action matrix (content TBD)

Actions drawn from ALG “Advancing Adoption Maturity” + Automation sales tactics. Replace asset names when catalog is mapped.

| Maturity | Practitioner | Champion | Influencer | Decision Maker |
|---|---|---|---|---|
| **1 Initial** | First use case pilot; onboarding; essentials training | Awareness + early-win kit | Identify key teams / use cases | Define KPIs / business value framing |
| **2 Developing** | Essential tasks; standardize configs | Internal value storytelling | Expand across teams | Track KPIs; Services if stuck |
| **3 Operational** | Advanced features; automate deployments | Peer advocacy; track sentiment | Integrations (ITSM, obs, Win, etc.) | Efficiency KPI outcomes |
| **4 Optimizing** | Expert paths; production workload depth | CoE / community of practice | Embed in business strategy | Sustain KPI targets; expand domains |
| **5 Innovator** | Emerging capabilities; latest releases | External advocacy / references | Thought leadership / best practices | Industry leadership narrative |

### Use-case paths (optional journey lanes later)
From Automation sales-tactics screenshot — not v1 blockers:

1. **Automate at scale** — reuse, trusted supply chain, CoP, hyperscaler procurement  
2. **Optimize / modernize IT ops** — ticket volume, ITSM/obs/FinOps, cross-sell RHEL/virt/AI  
3. **AIOps** — alert fatigue → agentic / intelligent assistant  
4. **Network automation** — find network architects & ops leaders  

---

## 10. AJO configuration checklist (build-ready later)

- [ ] Solution interest: Ansible Automation Platform  
- [ ] Role template + auto-assign filters (title, product interest, Marketo list exclusions)  
- [ ] Completeness thresholds per role  
- [ ] Engagement score weights aligned to adoption (de-emphasize email-only inflation — see existing AJO scoring work)  
- [ ] Account journey graph: entry → wait/listen → role splits → offers → sales alert nodes  
- [ ] Named journey nodes for CJA / reporting  
- [ ] Cap / quiet hours / Marketo concurrency exclusions  
- [ ] Sales alert payload: account, maturity band, trigger, missing roles, recommended play  

---

## 11. Success metrics

| Layer | Metric |
|---|---|
| Orchestration | Buying-group completeness; % accounts with required roles; journey enter/exit |
| Engagement | Role-level email engagement; content completion (labs/learning) |
| Adoption | Proxy or EoA maturity movement (e.g. % L1/L2 → L3 in 90 days) |
| Revenue | Renewal retention on nurtured risk accounts; expansion opptys influenced (pattern: SNow pilot tracked opptys/$ ) |
| Coordination | % risk triggers with sales task created; digital suppress when high-touch active |

---

## 12. Open questions

1. Who owns **DA Lead** and the AAP proxy signal dictionary for AEP?  
2. Is v1 limited to **telemetry-on** accounts, or must we cover low-confidence proxies from day one?  
3. Which existing **AAP Journey Orchestration Playbook** (ServiceNow) assets reuse vs rewrite for general adoption?  
4. When does **Ansible Adoption Progression Guide** / **Ansible EoA data** land (framework “coming soon”)?  
5. Final **required roles** and counts for completeness = sales-ready?  
6. Persona approval path: Ansible PMM + Customer Marketing + GenStudio?  

---

## 13. Suggested next artifacts to add under `/adoption`

| Priority | Artifact | Unlocks |
|---|---|---|
| P0 | AAP signal / proxy dictionary (even draft) | Real trigger definitions |
| P0 | ~~Title → AJO role mapping (CRM extract)~~ → **refine** auto-assign rules from §6 + drop Default/Procurement | Role template auto-assign |
| P1 | GenStudio messaging lock + person-level CRM counts | Copy & GenStudio |
| P1 | Offer/asset list by maturity × role | Journey content nodes |
| P2 | Ansible Adoption Progression Guide | Milestone language |
| P2 | Conflict matrix vs Marketo / AGI / SNow | Safe always-on execution |

---

## Document control

| Version | Date | Notes |
|---|---|---|
| 0.1 | 2026-10-01 | Skeleton from Adoption Framework + EoA + ALG screenshots; personas TBD |
| 0.2 | 2026-10-01 | CRM title/persona CSV ingested; §6 role map drafted; messaging personas still TBD |
