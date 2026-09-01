---
name: genstudio-email-prompts
description: Craft Adobe GenStudio for Performance Marketing prompts for Red Hat email experiences—single-product and multipod (Pod1, Pod2+) structured prompts with channel character limits, GenStudio personas, and product guidelines. Use when the user asks for GenStudio prompts, email marketing prompts, multipod emails, pod-based email copy, or GenStudio Create briefings for RHEL, OpenShift Platform Plus, Ansible Automation Platform, Developer program, or product trial.
---

# GenStudio Email Prompts

Produce paste-ready prompts for **Adobe GenStudio for Performance Marketing** email experiences. Output the prompt only (plus a short GenStudio Parameters checklist when helpful)—not the email copy itself unless asked.

## When to use

- User wants a GenStudio prompt for promotional, nurture, or educational email
- Single product **or** multi-product (multipod) emails using `Pod1`, `Pod2`, etc.
- Refining a weak prompt into GenStudio’s structured format

## Products (GenStudio Parameters)

Use only these product guidelines unless the user specifies another. Full descriptions, value props, and messaging preferences: [products.md](products.md).

| Product | Notes |
|---------|--------|
| **Red Hat Enterprise Linux** | Hybrid OS foundation; lead with why RHEL (not why Linux); hybrid consistency; Lightspeed for ops and security |
| **Red Hat OpenShift Platform Plus** | Prefer this name (not “OpenShift” alone); hybrid app platform at scale |
| **Red Hat Ansible Automation Platform** | Prefer this name (not “Ansible” or AAP); enterprise automation at scale; Lightspeed for skills gap, not the whole story |
| **Red Hat Developer program** | No-cost membership; peer-to-peer; Join / Start building CTAs |
| **Red Hat product trial** | No-cost, typically 60-day, full-subscription-value evaluation—not production; not the Developer program |

Map each pod to one product/offer focus when possible. Briefs that say “OpenShift” map to **Red Hat OpenShift Platform Plus** unless another edition is named. Briefs that say “Ansible” map to **Red Hat Ansible Automation Platform** unless they name community Ansible, Ansible Core, or AWX.

## Personas (GenStudio Parameters)

Select from the GenStudio persona repository (WIP—not exhaustive). Full descriptions and messaging preferences: [personas.md](personas.md).

| Persona | Role examples |
|---------|----------------|
| **Champion** | System Administrator, Data Science Lead, Automation Architect, AppDev ITDM, Lead Business Analyst |
| **Technical Practitioner / Architect** | Cloud Architect, DevOps Engineer, SysAdmin, Site Reliability Engineer |
| **Developer** | Enterprise Software Engineer, Full-Stack Developer, Cloud-Native Developer, Application Architect |

If the user says “Technical Practitioners & Influencers,” map to **Technical Practitioner / Architect** (and Champion when influencer/advocacy framing is needed). Note the assumption.

## Email channel limits & style

Enforce Red Hat channel guidelines in pod directives and when reviewing generated copy. Full rules: [channel-guidelines.md](channel-guidelines.md).

| Element | Limit |
|---------|--------|
| Subject line | 30–40 characters max |
| Preheader | 40–60 characters |
| Headline | 30 characters max |
| Sub-headline | 45 characters max |
| Body | Max **3 sentences per pod**; outcomes over description |
| CTA | 20–25 characters max |

**Style:** scannable; customer benefit first; active voice; second person when appropriate; Oxford commas; contractions allowed in email; avoid vague words (e.g. “flexible,” “scalable”); entire email—no “free/win/unlock” (use “no-cost”); CTA verbs like Download, Register, Start, Explore, Watch—never “click here.”

**Channel fields** (Brand → Channel guidelines → Email—not the prompt): per-field lines for General, Subject, Preheader, Headline, Sub-headline, Body, and CTA. Body includes sentence rhythm, do not start with “You,” one focus per pod, outcome then proof. Use when reviewing generated copy. Canonical text: [channel-guidelines.md](channel-guidelines.md).

**Brand editorial** (Brand → Editorial guidelines and Editorial restrictions—not the prompt): first-use naming; sentence case headlines; numerals; “application” not “app”; Red Hat as “it.” Restrictions: no uncited superlatives; no “secure/more secure”; no AI-typical wording; no vague words used alone; no “the” before product names; no “please” or “click here.” Use when reviewing generated copy. Canonical text: [brand-guidelines.md](brand-guidelines.md).

**In prompts:** bake length into pod lines when helpful, e.g. `Pod1: In 300-400 characters…` or `Pod2: In 2 sentences maximum…` (body still ≤ 3 sentences per pod). Do not repeat Email channel field guidelines or Brand editorial guidelines or restrictions in the prompt.

## Inputs to collect

If missing, ask briefly—or infer and note assumptions:

| Input | Notes |
|-------|--------|
| **Email type** | Single-section or multipod |
| **Goal / CTA intent** | Motivate, educate, drive trial, standardize, partner action |
| **Persona** | Champion, Technical Practitioner / Architect, or Developer |
| **Product(s)** | From the list above; one per pod when multipod |
| **Key message / benefits** | Align to persona + product messaging preferences |
| **Tone / do-nots** | Per channel guidelines + any campaign constraints |

Brand, Persona, and Product **guidelines** are selected in GenStudio Parameters—do **not** paste full brand guidelines into the prompt.

## Prompt construction rules

1. **Lead with a generic user prompt** — intent, persona/audience, overall product/theme.
2. **Then add section directives** for multipod (`Pod1`, `Pod2`, …).
3. **Match template section names** — `Pod` (also `Group` / `Section` / `Module` if the template uses those). Case-insensitive.
4. **Separate name from directive** with `:`, `-`, `;`, etc.: `Pod1: Focus on…`
5. **Be specific** — audience, purpose, features, benefits, action; include character/sentence caps per pod when useful.
6. **One focus per pod** — distinct product or benefit.
7. **Iterate** — tighten specifics or name themes/words to avoid.

### Single-product

```
Write a promotional email to motivate [persona] to [goal] using [Product]. Highlight [key capabilities / benefits]. Encourage [desired action].
```

For single-pod templates, you may still use `Pod1:` with a length constraint (see [examples.md](examples.md)).

### Multipod

```
Write a promotional multipod email to motivate [persona] to [goal] using [Product A] and [Product B].

Pod1: In [N characters / N sentences] [tone], focus on [Product A] and [specific capability / benefit].

Pod2: In [N sentences maximum] focus on [Product B / program] and [specific capability / benefit].
```

## Output format

1. **Ready-to-paste GenStudio prompt** in a fenced code block
2. **Parameters checklist**: Brand; Persona; Product(s); single vs multipod; assets per pod
3. **Assumptions** (only if inferred)
4. Optional: remind of subject/preheader/headline/CTA character caps if the user will edit fields manually

Do not generate subject lines, headlines, or body copy unless asked.

## Trademark & naming

Preserve ®/™ when the user supplies them (e.g. `Red Hat® Enterprise Linux®`). Do not invent marks.

## References

- Channel limits & email style: [channel-guidelines.md](channel-guidelines.md)
- Brand editorial (abbreviations, product first-use naming): [brand-guidelines.md](brand-guidelines.md)
- Persona descriptions & messaging: [personas.md](personas.md)
- Product descriptions & messaging: [products.md](products.md)
- Adobe GenStudio rules: [reference.md](reference.md)
- Examples: [examples.md](examples.md)

Local brand PDFs (gitignored): `Red Hat Style and Brand/Red Hat_Channel Guidelines.pdf`, `Red Hat Style and Brand/Persona.pdf`, `Red Hat Style and Brand/Prompt Examples.pdf`  
Personas source: [GenStudio Personas_WIP](https://docs.google.com/document/d/1Zbqq5GNc5SZ9wwdA6sq8PMuLaeYA0R4i-NsxZ66k5TA/edit?usp=sharing) → [personas.md](personas.md)  
Products source: [GenStudio Products](https://docs.google.com/document/d/1SBPVonkB1fq5vjLSOOp2NCDu1ZonZcKRsvoNyx0KkYk/edit?usp=sharing) (`GenStudio Products.txt`) → [products.md](products.md)
