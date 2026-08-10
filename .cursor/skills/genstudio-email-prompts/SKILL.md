---
name: genstudio-email-prompts
description: Craft Adobe GenStudio for Performance Marketing prompts for Red Hat email experiences—single-product and multipod (Pod1, Pod2+) structured prompts with channel character limits and GenStudio personas. Use when the user asks for GenStudio prompts, email marketing prompts, multipod emails, pod-based email copy, or GenStudio Create briefings for RHEL, OpenShift, Developer program, Partner, or product trial.
---

# GenStudio Email Prompts

Produce paste-ready prompts for **Adobe GenStudio for Performance Marketing** email experiences. Output the prompt only (plus a short GenStudio Parameters checklist when helpful)—not the email copy itself unless asked.

## When to use

- User wants a GenStudio prompt for promotional, nurture, or educational email
- Single product **or** multi-product (multipod) emails using `Pod1`, `Pod2`, etc.
- Refining a weak prompt into GenStudio’s structured format

## Products (GenStudio Parameters)

Use only these product guidelines unless the user specifies another:

- Red Hat Enterprise Linux
- Red Hat OpenShift
- Red Hat Developer program
- Red Hat Partner
- Red Hat product trial

Map each pod to one product/offer focus when possible.

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

**Style:** scannable; customer benefit first; active voice; second person when appropriate; Oxford commas; avoid contractions; avoid vague words (e.g. “flexible,” “scalable”); subject/preheader—no “free/win/unlock” (use “no-cost”); CTA verbs like Download, Register, Start, Explore, Watch—never “click here.”

**In prompts:** bake length into pod lines when helpful, e.g. `Pod1: In 300-400 characters…` or `Pod2: In 2 sentences maximum…` (body still ≤ 3 sentences per pod).

## Inputs to collect

If missing, ask briefly—or infer and note assumptions:

| Input | Notes |
|-------|--------|
| **Email type** | Single-section or multipod |
| **Goal / CTA intent** | Motivate, educate, drive trial, standardize, partner action |
| **Persona** | Champion, Technical Practitioner / Architect, or Developer |
| **Product(s)** | From the list above; one per pod when multipod |
| **Key message / benefits** | Align to persona messaging preferences |
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
- Persona descriptions & messaging: [personas.md](personas.md)
- Adobe GenStudio rules: [reference.md](reference.md)
- Examples: [examples.md](examples.md)

Source PDFs (local, gitignored): `Red Hat Style and Brand/Red Hat_Channel Guidelines.pdf`, `Red Hat Style and Brand/GenStudio persona repository.pdf`, `Red Hat Style and Brand/CY6Q1 GenStudio Testing - Prompt exampels.pdf`
