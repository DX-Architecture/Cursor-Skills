---
name: genstudio-email-prompts
description: Craft Adobe GenStudio for Performance Marketing prompts for Red Hat email experiences—single-product and multipod (Pod1, Pod2+) structured prompts with channel character limits, GenStudio personas, product guidelines, and brand-score wording hygiene. Use when the user asks for GenStudio prompts, email marketing prompts, multipod emails, pod-based email copy, GenStudio Create briefings for RHEL, OpenShift Platform Plus, Ansible Automation Platform, Developer program, or product trial, or when generated email scored low on Brand / Content check.
---

# GenStudio Email Prompts

Produce paste-ready prompts for **Adobe GenStudio for Performance Marketing** email experiences. Output the prompt only (plus a short GenStudio Parameters checklist when helpful)—not the email copy itself unless asked.

## When to use

- User wants a GenStudio prompt for promotional, nurture, or educational email
- Single product **or** multi-product (multipod) emails using `Pod1`, `Pod2`, etc.
- Refining a weak prompt into GenStudio’s structured format
- Generated variants scored low on Brand / Content check and the prompt needs a rewrite

## Products (GenStudio Parameters)

Use only these product guidelines unless the user specifies another. Full descriptions, value props, and messaging preferences: [products.md](products.md).

| Product | Notes |
|---------|--------|
| **Red Hat Enterprise Linux** | Hybrid OS foundation; lead with why RHEL (not why Linux); hardened foundation and closed-loop remediation; hybrid consistency; Lightspeed for ops, risk, and compliance outcomes |
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

If the user says “Technical Practitioners & Influencers,” map to **Technical Practitioner / Architect** (and Champion when influencer/advocacy framing is needed). If they say **Selectors** (tactical acquire-and-use choices), map to **Technical Practitioner / Architect**. Note the assumption.

## Email channel limits & style

Enforce Red Hat channel guidelines in pod directives and when reviewing generated copy. Full rules: [channel-guidelines.md](channel-guidelines.md).

| Element | Limit |
|---------|--------|
| Subject line | 30–50 characters; offer in the first 30; verbs Get, Start, Explore, Try—never Unlock |
| Preheader | 40–90 characters; extra context in the first 40; do not repeat the subject |
| Headline | Max **8 words**; outcome in the first 3 words |
| Sub-headline | 45 characters max |
| Body | Max **3 sentences per section**; outcomes over description; do not start with You |
| CTA | **2–4 words**; verb + object (Start your trial, Explore RHEL)—never Learn more, Click here, or Unlock |

**Style:** short paragraphs; active voice; contractions allowed; avoid `flexible` / `scalable`; entire email—no `free` / `win` / `unlock` (use **no-cost**). Canonical Channel text: [channel-guidelines.md](channel-guidelines.md).

**Body rhythm** (Brand → Channel → Email → Body—not the prompt): 3 sentences per section; one idea per sentence; operational problem then guidance; do not start the first sentence with “You”; vary sentence length. Use when reviewing generated copy.

**Brand voice** (Brand → Tone of voice and Brand values—not the prompt): stability and hybrid cloud engineering; community-driven innovation; practical, no-hype technical voice; operational problem then guidance; Red Hat as enabler. Values: Open, Authentic, Helpful, Brave (no competitor attacks). Canonical text: [brand-guidelines.md](brand-guidelines.md). Do not put Tone’s word `flexibility` in email prompts—Channel still bans `flexible`.

**Brand editorial** (Brand → Editorial guidelines and Editorial restrictions—not the prompt): full product name first in body; approved abbreviations (e.g. RHEL) in subject/headline; Red Hat as “it” or “we/our,” not “they.” Restrictions: no uncited superlatives; no “secure/more secure”; no AI-typical wording (including testament / tapestry); no vague words without a direct object; no “the” before product names; no unqualified “the cloud” or “the edge” (use hybrid cloud, edge computing, edge device). Use when reviewing generated copy. Canonical text: [brand-guidelines.md](brand-guidelines.md).

**In prompts:** bake length into pod lines when helpful, e.g. `Pod1: In 3 sentences maximum…` or `Pod2: In 2 sentences maximum…` (body still ≤ 3 sentences per section). Do not paste Email Channel, Brand voice, Brand values, or Brand editorial lists into the prompt (Parameters already inject them). **Do rewrite the brief** so restricted words never appear in the prompt—GenStudio echoes prompt wording into copy, and Brand score is % of Brand guidelines passed vs tested on that copy. Substitution table: [brand-guidelines.md](brand-guidelines.md). Never put `Unlock`, `flexible`, `free`, `Learn more`, `click here`, `the cloud`, or `the edge` in the prompt.

## Inputs to collect

If missing, ask briefly—or infer and note assumptions:

| Input | Notes |
|-------|--------|
| **Email type** | Single-section or multipod |
| **Goal / CTA intent** | Motivate, educate, drive trial, standardize, partner action |
| **Persona** | Champion, Technical Practitioner / Architect, or Developer |
| **Product(s)** | From the list above; one per pod when multipod |
| **Key message / benefits** | Align to persona + product messaging preferences; translate restricted brief language (see brand-score hygiene) |
| **Tone / do-nots** | Per channel guidelines + any campaign constraints |
| **Content check failures** | If the user reports a low Brand score, ask for the Content check **Needs review** items (or paste them) |

Brand, Persona, and Product **guidelines** are selected in GenStudio Parameters—do **not** paste those lists into the prompt.

## Brand-score hygiene

Brand score = guidelines passed ÷ guidelines tested on generated copy ([Brand validation](https://experienceleague.adobe.com/en/docs/genstudio-for-performance-marketing/user-guide/guidelines/brand-validation)). Prompt text is not scored, but Create copies prompt phrases into headlines and body.

**Before outputting a prompt, scan it** (and any product phrases you were about to copy) against the substitution table in [brand-guidelines.md](brand-guidelines.md). Common leaks:

- User said “security / secure / more secure / advanced security” → name capabilities and outcomes (compliance baselines, live kernel patching, Lightspeed-assisted detection and remediation; lower risk, less unplanned downtime). Never put `secure`, `more secure`, `security`, or `security-focused` in the prompt.
- Product Parameters are Brand-aligned in [products.md](products.md). Still do not copy Product sentences into the prompt; name capabilities and outcomes.
- Vague words without a direct object (`streamline`, `powerful`, `robust`, `leverage`, `utilize`, `seamless`, `frictionless`) and Channel bans (`flexible`, `flexibility`, `scalable`, `free`, `win`, `unlock`) must not appear in the prompt either.
- Do not write `the` before a product name. Do not write `the cloud` or `the edge`; use hybrid cloud, public cloud, cloud workloads, edge computing, or edge device.

If the user brief used restricted words, rewrite them in the prompt and list the rewrite under **Assumptions**.

### After a low Brand score

1. Ask for Content check **Needs review** items if not provided.
2. Rewrite the prompt: remove echoed restricted words; add **only** the failed items as targeted avoidances (Adobe: iterate by asking Create to avoid certain words/themes).
3. Do not dump the full Brand guideline list into the prompt.
4. Return the revised paste-ready prompt.

## Prompt construction rules

Structured prompts give the LLM field-specific instructions. Use them for multi-section experiences (including multi-pod emails). Source: [structured-prompts.png](structured-prompts.png).

1. **Lead with a generic user prompt** — intent, persona/audience, overall product/theme.
2. **Then add section-specific directives** (`Pod1`, `Pod2`, …).
3. **Match template field names exactly** — as the template defines them. Common names: `Pod` / `Group` / `Section` / `Module` (e.g. `Pod1`), `introduction`, `on-image text`, `headline`, `footer`. Duplicate fields are numbered (`on_image_text1`, `on_image_text2`). Case-insensitive.
4. **Separate name from directive** with `:`, `;`, `-`, or `,`: `Pod1: Focus on…` or `Pod1; Describe how to easily edit text and swap images.`
5. **Be specific** — audience, purpose, features, benefits, action; include character/sentence caps per pod when useful. Use named capabilities and outcomes, not restricted category labels.
6. **One focus per pod** — distinct product or benefit.
7. **Pass brand-score hygiene** — no restricted words in the prompt (see above).
8. **Iterate** — after Content check failures, add targeted word/theme avoidances only.

If the structure pattern is not followed, GenStudio treats the prompt as **global** and applies it to all sections, which usually reduces performance.

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
3. **Assumptions** (only if inferred)—include any restricted-brief rewrites (e.g. “security” → named capabilities)
4. Optional: remind of subject (30–50), preheader (40–90), headline (8 words), CTA (2–4 words) if the user will edit fields manually

Do not generate subject lines, headlines, or body copy unless asked.

## Trademark & naming

Preserve ®/™ when the user supplies them (e.g. `Red Hat® Enterprise Linux®`). Do not invent marks.

## References

- Channel limits & email style: [channel-guidelines.md](channel-guidelines.md)
- Brand voice, editorial, and restrictions: [brand-guidelines.md](brand-guidelines.md)
- Persona descriptions & messaging: [personas.md](personas.md)
- Product descriptions & messaging: [products.md](products.md)
- Adobe GenStudio rules: [reference.md](reference.md)
- Adobe structured-prompt source: [structured-prompts.png](structured-prompts.png)
- Examples: [examples.md](examples.md)

Local brand PDFs (gitignored): `Red Hat Style and Brand/Red Hat_Channel Guidelines.pdf`, `Red Hat Style and Brand/Persona.pdf`, `Red Hat Style and Brand/Prompt Examples.pdf`  
Personas source: [GenStudio Personas_WIP](https://docs.google.com/document/d/1Zbqq5GNc5SZ9wwdA6sq8PMuLaeYA0R4i-NsxZ66k5TA/edit?usp=sharing) → [personas.md](personas.md)  
Products source: [GenStudio Products](https://docs.google.com/document/d/1SBPVonkB1fq5vjLSOOp2NCDu1ZonZcKRsvoNyx0KkYk/edit?usp=sharing) (`GenStudio Products.txt`) → [products.md](products.md)
