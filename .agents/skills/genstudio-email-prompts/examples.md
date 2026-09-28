# GenStudio email prompt examples

Aligned with `CY6Q1 GenStudio Testing - Prompt exampels.pdf`, Adobe structured-prompt format ([structured-prompts.png](structured-prompts.png)), and Red Hat channel limits, then rewritten so prompts pass brand-score hygiene. CY6Q1 source prompts may still contain restricted words (`streamline`, `secure`, `security-focused`); do not copy those words into new prompts.

Sentence rhythm and “do not start the body with You” live in Brand → Channel guidelines → Email → Body. Do not repeat them in the prompt.

## Adobe format (structure only)

Adobe’s canonical structured prompt. Use this **shape** (generic prompt, then `PodN:` directives). Do not copy Creative Cloud product copy or “free trial” wording into Red Hat briefs.

```
Create an exciting multi-pod email focusing on Creative Cloud and its powerful generative AI capabilities.

Encourage customers to convert to Photoshop or use a free Photoshop trial. We want to better educate them about app features.

Pod1: Focus on Adobe Photoshop and its new generative AI tools that enable creators to bring images to life in minutes.

Pod2: Focus on Adobe Illustrator and its new generative AI tools, such as Generative Shape Fill, which allows you to quickly fill your vector outline and explore a variety of options that match the look and feel of your own artwork.

Pod3: Focus on Adobe Acrobat Pro. Make users aware that with Acrobat Pro they can edit images and text inside a PDF.
```

## Example 1 — Multipod (RHEL + Developer program)

**Persona:** Technical Practitioner / Architect  
**Products:** Red Hat Enterprise Linux, Red Hat Developer program

**Prompt:**

```
Write a promotional multipod email to motivate Technical Practitioners & Influencers to standardize and increase business agility using Red Hat® Enterprise Linux®.

Pod1: In 300-400 characters in a conversational tone emphasize how Red Hat® Enterprise Linux® (RHEL) lets IT teams use a single set of tools to deploy, run, and manage workloads across multiple footprints. Transform infrastructure from a complex operational burden into a stable, consistent foundation for rapid innovation.

Pod2: In 2 sentences maximum promote Red Hat Developer program curated learning paths for common development tasks for RHEL
```

**Parameters:** Persona = Technical Practitioner / Architect; Products = Red Hat Enterprise Linux + Red Hat Developer program; multipod template.

---

## Example 2 — Single pod (RHEL cloud)

**Persona:** Technical Practitioner  
**Product:** Red Hat Enterprise Linux

**Prompt:**

```
Create a marketing email for the selector and Technical Practitioner persona focused on accelerating cloud growth using Red Hat® Enterprise Linux® and drive awareness of use cases.

Pod1: In 400 characters or less focus on how Red Hat® Enterprise Linux® is optimized for cloud environments and provides a consistent, manageable foundation for getting the most value from cloud investments. Users have the freedom to use the cloud provider or providers of choice while keeping one operating experience across all footprints.
```

**Parameters:** Persona = Technical Practitioner / Architect; Product = Red Hat Enterprise Linux; single-pod / selector template.

---

## Example 3 — Multipod (OpenShift Platform Plus + product trial)

**Persona:** Developer  
**Products:** Red Hat OpenShift Platform Plus, Red Hat product trial

**Prompt:**

```
Write a promotional multipod email to motivate Developers to ship cloud-native applications faster using Red Hat® OpenShift® Platform Plus. Use a peer-to-peer, code-first tone. Avoid marketing hyperbole.

Pod1: In 300-400 characters focus on Red Hat® OpenShift® Platform Plus as a unified hybrid cloud platform that reduces inner-loop toil from local development to production while keeping access controls and policy in the workflow.

Pod2: In 2 sentences maximum promote a no-cost Red Hat product trial so developers can validate OpenShift Platform Plus in their own environment—not for production use.
```

**Parameters:** Persona = Developer; Products = Red Hat OpenShift Platform Plus + Red Hat product trial; multipod.

---

## Example 4 — Multipod (RHEL + product trial)

**Persona:** Champion  
**Products:** Red Hat Enterprise Linux, Red Hat product trial

**Prompt:**

```
Write a promotional multipod email to motivate Champions to build internal urgency and align stakeholders around standardizing on Red Hat® Enterprise Linux®.

Pod1: In 3 sentences maximum emphasize hybrid cloud consistency, predictable lifecycle, and proof points Champions can use to justify ROI and overcome executive inertia.

Pod2: In 2 sentences maximum promote a no-cost Red Hat product trial with full subscription-level access so teams can evaluate RHEL before purchase.
```

**Parameters:** Persona = Champion; Products = Red Hat Enterprise Linux + Red Hat product trial; multipod.

---

## Example 5 — Multipod (RHEL risk/compliance + product trial)

**Persona:** Technical Practitioner / Architect (Selectors)  
**Products:** Red Hat Enterprise Linux, Red Hat product trial

User brief said “advanced security capabilities.” Those words are rewritten so Brand restriction on “secure / more secure” does not echo into copy.

**Prompt:**

```
Write a promotional multipod email to motivate Selectors who make tactical choices about which technologies to acquire and use to evaluate Red Hat Enterprise Linux for built-in capabilities that lower risk, save time, and mitigate downtime while supporting compliance.

Pod1: In 300-400 characters focus on Red Hat Enterprise Linux capabilities that help organizations lower risk, save time, and mitigate unplanned downtime while supporting compliance. Emphasize compliance baselines, live kernel patching, and Lightspeed-assisted detection and remediation as proof of those outcomes. Lead with why Red Hat Enterprise Linux, not why Linux.

Pod2: In 2 sentences maximum promote a no-cost Red Hat product trial with full subscription-level access so Selectors can evaluate Red Hat Enterprise Linux in their own environment before purchase—not for production use.
```

**Parameters:** Persona = Technical Practitioner / Architect; Products = Red Hat Enterprise Linux + Red Hat product trial; multipod.

---

## Example 6 — Technical copywriter (RHEL + Lightspeed, single section)

**Persona:** Developer + Technical Practitioner / Architect (Developers, SysAdmins, DevOps, Technical Influencers)  
**Product:** Red Hat Enterprise Linux (Lightspeed + stack remediation path)  
**Theme:** Simplify Tasks. Amplify Results.

Proven shape from a high-performing brief. Restricted wording rewritten for brand-score hygiene (`seamless` → works across).

**Prompt:**

```
Act as a Principal Technical Copywriter specializing in enterprise IT solutions. Write a concise promotional email tailored for Developers, Systems Administrators, DevOps Engineers, and Technical Influencers.

Core objective:
Show how Red Hat Enterprise Linux and Red Hat Lightspeed identify vulnerabilities and performance bottlenecks before they cause downtime, and how that guidance works across Red Hat Enterprise Linux, Red Hat Satellite, and Red Hat Ansible Automation Platform. Frame operational friction and talent shortages as solvable with built-in AI assistance.

Body:
Length: Strictly 300–400 characters total.
Theme: “Simplify Tasks. Amplify Results.”
Key points:
- Position Red Hat Lightspeed as assistance for operational friction and talent shortages.
- Explain how Lightspeed identifies vulnerabilities and performance bottlenecks before downtime occurs.
- Mention operating with predictive analytics to identify and remediate risks.
- Highlight build, operate, and protect tasks across Red Hat Enterprise Linux, Red Hat Satellite, and Red Hat Ansible Automation Platform, including migration from CentOS Linux.
End with a concluding statement that lands the outcome or next step (still within 300–400 characters and ≤ 3 sentences).

Tone: Direct, authoritative, developer-friendly. Avoid high-level marketing jargon.

Subject line: Align with the core offer in the body. Do not end with a period.
Preheader: 40–90 characters. Clear positive outcome. Do not repeat the subject verbatim. Do not end with a period.
Headline: Maximum 8 words. Specific to proactive IT management or AI-assisted operations. Do not end with a period.
Subheadline: Maximum 45 characters. Do not end with a period.
```

**Parameters:** Personas = Developer and/or Technical Practitioner / Architect; Product = Red Hat Enterprise Linux; single-section template (Create fills subject/preheader/headline/subheadline from the field-craft block).  
**Assumptions:** Satellite and Ansible Automation Platform are stack context for the remediation path, not separate Product Parameters unless the template is multipod.
