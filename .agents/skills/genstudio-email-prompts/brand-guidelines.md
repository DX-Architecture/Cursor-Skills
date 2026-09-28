# Brand guidelines

Source of truth for GenStudio **Brand → Tone of voice**, **Brand values**, **Editorial guidelines**, and **Editorial restrictions**. Do not paste these lists into the prompt when Brand is selected in Parameters. **Do apply the substitution table** so restricted words never appear in the prompt—Create echoes prompt phrasing into copy, and Brand score tests that copy.

Approved short names (what you may shorten *to*, and what never to use) stay in Product guidelines: [products.md](products.md).

Email field craft and character limits stay in Channel guidelines: [channel-guidelines.md](channel-guidelines.md).

Adobe caps Tone of voice and Brand values at **3–6 guidelines** each.

## Configured in Brand → Tone of voice

- Focus on stability, enterprise-grade reliability, and solving tangible hybrid cloud engineering challenges.
- Emphasize community-driven innovation, flexibility, and freedom from vendor lock-in.
- Be clear, direct, and practical. Prefer specific outcomes over slogans.
- Acknowledge the reader’s operational problem, then move to useful guidance. Do not open with sympathy or “You know…”
- Respect technical audiences. Speak clearly without fluff or overly dramatic marketing hype.
- Frame Red Hat as an enabler—giving developers and architects the tools to build anywhere.

## Configured in Brand → Brand values

- Open: Prefer transparency and collaboration over secrecy and control. Use inclusive language. Do not lecture.
- Authentic: Prefer truth over hype. Acknowledge complexity. Do not overpromise.
- Helpful: Prefer customer success over company promotion. Give an actionable next step the reader can take.
- Brave: Take a clear, principled position. Challenge industry assumptions with respect. Do not attack competitors.

## Configured in Brand → Editorial guidelines

- Refer to products by full name on first use in body copy. Approved abbreviations (e.g., RHEL) are allowed in subject lines/headlines.
- Use parentheses only for approved initialisms such as RHEL; for other products, shorten to the approved name without inventing an initialism.
- Leave common terms such as AI, HTML, and PIN abbreviated; they do not need expansion on first use.
- Refer to Red Hat as “it” (third person) or “we/our” (first-person brand voice). Do not use “they.”

## Configured in Brand → Editorial restrictions

- Avoid absolute and superlative claims such as leading, best, fastest, only, or 100% unless a citation appears in the copy.
- Avoid calling a product or environment “secure” or “more secure.” Name the capability or outcome instead (for example, compliance baselines, live kernel patching).
- Avoid AI-typical wording: delve, harness, pivotal, landscape, testament, tapestry, unwavering, and openings like “In today’s fast-paced…”
- Avoid vague words used without a direct object: robust, powerful, strong, streamline, leverage, utilize, seamless, frictionless.
- Avoid “the” before product names (write “Red Hat Enterprise Linux,” not “the Red Hat Enterprise Linux”).
- Avoid “the cloud” as an unqualified noun. Specify whose environment (for example, a public cloud, a hybrid cloud, or an organization’s cloud). Prefer “cloud” as a modifier: cloud workloads, cloud providers.
- Avoid “the edge” unless the first use is qualified (for example, the edge of the network). Use “an edge device” for hardware. Use “edge computing” for the concept.

## Prompt wording (brand-score hygiene)

Do not paste this table into GenStudio. Use it to rewrite the user brief and any Product value-prop phrases before they go into the prompt.

| If the brief or product text says | Write in the prompt |
|-----------------------------------|---------------------|
| secure, more secure, security, security-focused, built-in security, advanced security, proactive security | Named capabilities (compliance baselines, live kernel patching, Lightspeed-assisted detection and remediation) and outcomes (lower risk, less unplanned downtime, support compliance) |
| robust, powerful, strong, streamline, leverage, utilize, seamless, frictionless (used without a direct object) | A specific operational outcome with an object (one set of tools, fewer manual steps, less unplanned downtime) |
| flexible, flexibility, scalable | How it works in this environment (one operating experience across footprints; add capacity without rebuilding). Channel still bans `flexible` / `scalable` even though Tone mentions flexibility. |
| the Red Hat Enterprise Linux / the [Product] | Red Hat Enterprise Linux (no “the”) |
| the cloud | A named environment: public cloud, hybrid cloud, cloud workloads, cloud providers |
| the edge | Qualify first use (the edge of the network); an edge device for hardware; edge computing for the concept |
| free, free trial, win, unlock | no-cost product trial (Channel, not Brand) |
| click here, Learn more, Unlock | omit; CTA is 2–4 words, verb + object (Start your trial, Explore RHEL) (Channel, not Brand) |
| leading, best, fastest, only, 100% | omit unless a citation will appear in the generated copy |
| delve, harness, pivotal, landscape, testament, tapestry, unwavering, “In today’s fast-paced…” | omit |

GenStudio also matches close variants: `security` and `security-focused` typically fail the “secure / more secure” restriction. Prefer capability names over the category label.

Body copy: full product name on first use. Do not assume `RHEL` (or other approved abbreviations) is allowed in body after first mention—the configured rule only permits those abbreviations in subject lines and headlines.

## Conflicts to watch

These are live in GenStudio as written. Do not silently rewrite the configured lists. See the Issues list when reviewing Brand vs Channel scores.

| Conflict | Why it matters |
|----------|----------------|
| Tone says **flexibility**; Channel Email General bans **flexible** / **scalable** | Brand may reward “flexibility”; email Channel may fail the same copy. For email prompts, still substitute—do not put `flexible` / `flexibility` in the prompt. |
| Tone: prefer specific outcomes over slogans **and** “tools to build anywhere” | Internal Tone tension. Prefer named outcomes in prompts; do not echo “build anywhere.” |
| Tone: “freedom from vendor lock-in” vs Brave: do not attack competitors | Lock-in copy can read as a competitor attack. Frame portability / choice of footprint, not “escape Vendor X.” |
| Tone frames **developers and architects** | Champion / Selector emails can drift off-persona. Keep persona in the prompt; do not default every email to developers. |
| Tone is **6 / 6** (Adobe cap) | More Tone lines = more Brand checks that can fail. |
| Editorial no longer requires sentence case, “application” not “app,” numerals, or expand-on-first-use for LLM-style abbreviations | Those rules are **not scored** unless they live in Channel. `app` vs `application` is no longer a Brand editorial check. |
| Vague-word rule is now **without a direct object**; `enhance` / `improve` / `please` / `click here` dropped from Brand | `streamline operations` may now pass Brand. `click here` and `Learn more` are still Channel CTA fails. |
| Editorial bans **the cloud** / **the edge** | Product copy and briefs often say “in the cloud” or “to the edge.” In prompts use hybrid cloud, public cloud, cloud workloads, edge computing, or edge device. |

## How this layers

| Layer | Owns |
|-------|------|
| **Tone of voice** | Stability and hybrid cloud engineering; community-driven innovation; practical, no-hype technical voice; operational problem then guidance; Red Hat as enabler for developers and architects |
| **Brand values** | Open, Authentic, Helpful, Brave (no competitor attacks) |
| **Brand editorial** | Full product name first in body; abbreviations OK in subject/headline; approved initialisms only; common terms stay abbreviated; Red Hat as “it” or “we/our,” not “they” |
| **Brand restrictions** | Absolutes, security claims, AI-typical wording (including testament / tapestry), vague words without a direct object, “the” before products, unqualified “the cloud” / “the edge” |
| **Product** | Which short forms are approved (RHEL, OpenShift Platform Plus, Ansible Automation Platform, product trial) and which are forbidden (EL, OPP, AAP, free trial) |
| **Channel (email)** | Per-field General, Subject (30–50), Preheader (40–90), Headline (8 words), Sub-headline (45), Body (3 sentences/section), CTA (2–4 words, verb + object); contractions allowed; ban “flexible” / “scalable”; ban “free” / “win” / “unlock” (use no-cost); ban “Learn more” / “click here” |

Do not add trademark symbols (® / ™ / r-ball) to Brand or Channel guidelines. Preserve marks only when the user supplies them in a brief.
