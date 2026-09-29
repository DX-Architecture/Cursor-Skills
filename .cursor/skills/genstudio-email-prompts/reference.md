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

Source: [structured-prompts.png](structured-prompts.png) (Adobe GenStudio academy / Write effective prompts).

Structured prompts give the LLM specific instruction about what content to put in specific fields. Especially useful for experiences with many sections, including multi-pod emails.

### How it works

1. Reference the **generic user prompt first**, then section-specific directives.
2. Separate the field name from its directive with `:`, `;`, `-`, or `,` (Adobe also accepts `# $ ! ~ | @ = % & * ^ _`). Example: `Pod1; Describe how to easily edit text and swap images.`
3. Refer to fields **exactly as the template defines them**. Common names: `introduction`, `on-image text`, `headline`, `pod1`, `footer`. Duplicate field types are numbered (`on_image_text1`, `on_image_text2`). Section-name families: **Pod**, **Group**, **Section**, **Module**. Case-insensitive (`pod1` = `Pod1`).
4. If the structure pattern is not followed, GenStudio treats the prompt as **global** and applies it to all sections, which usually reduces performance.

Adobe’s sample pattern (format only—not a Red Hat prompt; do not copy “free trial” wording into Red Hat briefs):

```
Create an exciting multi-pod email focusing on Creative Cloud and its powerful generative AI capabilities.

Encourage customers to convert to Photoshop or use a free Photoshop trial. We want to better educate them about app features.

Pod1: Focus on Adobe Photoshop and its new generative AI tools that enable creators to bring images to life in minutes.

Pod2: Focus on Adobe Illustrator and its new generative AI tools, such as Generative Shape Fill, which allows you to quickly fill your vector outline and explore a variety of options that match the look and feel of your own artwork.

Pod3: Focus on Adobe Acrobat Pro. Make users aware that with Acrobat Pro they can edit images and text inside a PDF.
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
- [ ] Body ≤ 3 sentences per section; length encoded in pod directives when useful (not 75–150 words)
- [ ] Body rhythm (do not start the first sentence with “You”; vary sentence length) lives in Email Body Channel—not the prompt
- [ ] CTA is 2–4 words, verb + object; never Learn more, Click here, or Unlock
- [ ] Brand voice (tone and values), editorial, and restrictions live in Brand Parameters; apply substitutions in the prompt rather than pasting the lists
- [ ] Channel character limits respected ([channel-guidelines.md](channel-guidelines.md))
- [ ] After a low Brand score, iterate with Content check **Needs review** items as targeted avoidances
- [ ] Ready to iterate after first generation

## Red Hat sources

- `Red Hat Style and Brand/Red Hat_Channel Guidelines.pdf` — email style + character limits (local, gitignored)
- [brand-guidelines.md](brand-guidelines.md) — Brand tone of voice, values, editorial, and restrictions
- [GenStudio Personas_WIP](https://docs.google.com/document/d/1Zbqq5GNc5SZ9wwdA6sq8PMuLaeYA0R4i-NsxZ66k5TA/edit?usp=sharing) — Champion, Technical Practitioner / Architect, Developer (see [personas.md](personas.md))
- `GenStudio Products.txt` — RHEL, product trial, Developer program, OpenShift Platform Plus, Ansible Automation Platform, partner ecosystem (see [products.md](products.md))
- [structured-prompts.png](structured-prompts.png) — Adobe structured-prompt rules and Creative Cloud format example
- `Red Hat Style and Brand/CY6Q1 GenStudio Testing - Prompt exampels.pdf` / `Prompt Examples.pdf` — validated multipod/single-pod prompt patterns
- `Red Hat Style and Brand/Character Count_Template.pdf` — supplemental module counts (excluding spaces)
