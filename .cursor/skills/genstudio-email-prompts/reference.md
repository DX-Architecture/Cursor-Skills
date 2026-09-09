# GenStudio prompt reference

Source guidance (read when refining structure or troubleshooting bad generation):

- [Write effective prompts](https://experienceleague.adobe.com/en/docs/genstudio-for-performance-marketing/user-guide/intro/effective-prompts)
- [Email experiences](https://experienceleague.adobe.com/en/docs/genstudio-for-performance-marketing/user-guide/create/email-experiences)
- [Prompting AI agents (Adobe Business)](https://business.adobe.com/blog/prompting-ai-agents)

## Effective prompt components

GenStudio prompts work best with:

- **Descriptive language** — for copy: audience, purpose, features, examples, actions
- **Examples** and details not already covered by configured guidelines
- **Prompt criteria** — Parameters (Brand, Persona, Product) + optional asset + descriptive prompt

If guidelines are selected in Parameters, do not paste those lists into the prompt. Still rewrite the brief so restricted words never appear in prompt text—Create echoes that wording into copy, which Brand validation then scores.

## Structured prompts (multi-section email)

For multipod templates:

1. Generic user prompt first
2. Section-specific directives that **match template section names**
3. Valid section name families: **Pod**, **Group**, **Section**, **Module** (e.g. `Pod1`, `Pod2`)
4. Case-insensitive (`pod1` = `Pod1`)
5. Demarcation between name and directive: `,` `:` `;` `#` `$` `!` `~` `|` `@` `=` `-` `%` `&` `*` `^` `_`
6. If structure is invalid, GenStudio may apply the whole prompt to all sections

Adobe’s sample pattern:

```
Create an exciting multi-pod email focusing on Creative Cloud and its powerful generative AI capabilities.

Encourage customers to convert to Photoshop or use a free Photoshop trial. We want to better educate them about app features.

Pod1: Focus on Adobe Photoshop and its new generative AI tools that enable creators to bring images to life in minutes.

Pod2: Focus on Adobe Illustrator and its new generative AI tools, such as Generative Shape Fill...

Pod3: Focus on Adobe Acrobat Pro...
```

## Email experience context

- Create generates **four variants** on the Canvas
- Editable fields: pre-header, headline, sub-headline, body, CTA, image
- Multi-section emails: products/assets per section; **one visual asset per section**
- Progressive load order: variant names → subject lines → pre-headers → headlines/body/CTAs → subsequent section bodies → brand validation

## Agent-style prompting principles (enterprise)

From Adobe’s agent prompting guidance, apply to GenStudio briefs:

- Clear **goal** and success criteria
- **Constraints**: tone, length expectations, compliance, required terms
- Rich but relevant **context** (audience, offer, product proof)—avoid noise
- Prefer reusable, standardized prompt templates over one-off vague asks
- Iterate with feedback (refine prompt; avoid certain words/themes if needed)

## Best practices checklist

- [ ] Specific about what to do and not do
- [ ] External/campaign context when useful
- [ ] Guidelines used in Parameters, not pasted as lists into the prompt
- [ ] Prompt wording passes brand-score hygiene—no restricted words echoed from the brief or Product value props ([brand-guidelines.md](brand-guidelines.md))
- [ ] Persona and product from repo lists ([personas.md](personas.md), [products.md](products.md))
- [ ] Pod names match the email template
- [ ] One distinct focus per pod
- [ ] Body ≤ 3 sentences per pod; length encoded in pod directives when useful
- [ ] Body rhythm (avoid long, information-dense sentences with similar length; do not start the body with “You”) lives in Brand Email Body channel guidelines—not the prompt
- [ ] Brand voice (tone and values), editorial, and restrictions live in Brand Parameters; apply substitutions in the prompt rather than pasting the lists
- [ ] Channel character limits respected ([channel-guidelines.md](channel-guidelines.md))
- [ ] After a low Brand score, iterate with Content check **Needs review** items as targeted avoidances
- [ ] Ready to iterate after first generation

## Red Hat sources

- `Red Hat Style and Brand/Red Hat_Channel Guidelines.pdf` — email style + character limits (local, gitignored)
- [brand-guidelines.md](brand-guidelines.md) — Brand tone of voice, values, editorial, and restrictions
- [GenStudio Personas_WIP](https://docs.google.com/document/d/1Zbqq5GNc5SZ9wwdA6sq8PMuLaeYA0R4i-NsxZ66k5TA/edit?usp=sharing) — Champion, Technical Practitioner / Architect, Developer (see [personas.md](personas.md))
- `GenStudio Products.txt` — RHEL, product trial, Developer program, OpenShift Platform Plus, Ansible Automation Platform (see [products.md](products.md))
- `Red Hat Style and Brand/CY6Q1 GenStudio Testing - Prompt exampels.pdf` / `Prompt Examples.pdf` — validated multipod/single-pod prompt patterns
- `Red Hat Style and Brand/Character Count_Template.pdf` — supplemental module counts (excluding spaces)
