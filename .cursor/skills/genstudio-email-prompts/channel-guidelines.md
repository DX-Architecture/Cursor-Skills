# Red Hat email channel guidelines

Source of truth for GenStudio **Brand → Channel guidelines → Email**. Do not paste these lists into the prompt when Brand is selected in Parameters.

Optimized for GenStudio Content check: one job per line, one max per field, no banned words in examples. Legacy PDF limits stay in Supplemental module counts for template overflow.

## Limits (skill + manual field edits)

| Element | Limit | Craft |
|---------|--------|--------|
| **Subject line** | 30–50 characters | Offer/outcome in the first 30 characters; action verb Get, Start, Explore, or Try—never Unlock, Free, or Win; no trailing period |
| **Preheader** | 40–90 characters | Extra context in the first 40 characters; do not repeat the subject; no trailing period |
| **Headline** | Max 8 words | Primary outcome in the first 3 words; capability only as proof; no trailing period |
| **Sub-headline** | 45 characters max | Elaborate the headline promise; no trailing period; question marks allowed |
| **Body** | Max **3 sentences per section** | One idea per sentence; outcomes over description; do not start the first sentence with You; end with a concluding statement |
| **CTA** | **2–4 words** | Action verb + object (Start your trial, Explore RHEL); never Learn more, Click here, or Unlock; no end punctuation |

Do not use a 75–150 word body target in Channel or in prompts. GenStudio scores each Body field; that range over-generates multipod sections and fails short 3-sentence pods.

## Configured in Brand → Channel → Email → General

- Maintain a clear, direct, practical, solution-oriented tone. Use short paragraphs.
- Write in active voice. Capitalize product names, acronyms, and proper initialisms.
- Contractions are allowed. Avoid flexible and scalable; name the specific behavior instead.
- Avoid free, win, and unlock anywhere in the email. Use no-cost for no-charge offers.

## Configured in Brand → Channel → Email → Subject line

- 30–50 characters. Put the offer or outcome in the first 30 characters.
- Start with an action verb such as Get, Start, Explore, or Try. Do not use Unlock, Free, or Win.
- Align with the main offer in the body. Do not use a trailing period.

## Configured in Brand → Channel → Email → Preheader

- 40–90 characters. Put the extra context in the first 40 characters.
- Add the outcome or offer the subject line did not state. Do not repeat the subject verbatim.
- Do not use a trailing period.

## Configured in Brand → Channel → Email → Headline

- Maximum 8 words. Put the primary outcome in the first 3 words.
- Lead with the reader outcome; use a product capability only to prove it.
- Do not use a trailing period.

## Configured in Brand → Channel → Email → Sub-headline

- Maximum 45 characters.
- Elaborate on the headline promise with a specific outcome or next step.
- Do not use a trailing period. Question marks are allowed.

## Configured in Brand → Channel → Email → Body

- Maximum 3 sentences per section. One idea per sentence. Prioritize outcomes over product description.
- Acknowledge a specific operational problem, then give useful guidance. Do not start the first sentence with You.
- End with a concluding statement that lands the outcome or next step—do not leave the body as an open feature list.
- Keep sentences straightforward. Vary sentence length. Avoid long clauses that delay the point.

## Configured in Brand → Channel → Email → Call-to-action

- 2–4 words. Use action verb + object (Start your trial, Explore RHEL).
- Name a specific action. Do not use Learn more, Click here, or Unlock.
- Do not use end punctuation.

## Conflicts to watch

| Conflict | Why it matters |
|----------|----------------|
| Draft subject example **Unlock** | Channel General bans `unlock`. Never use it as a subject-verb example. |
| Draft body **75–150 words** | Per-section scoring. Keep 3 sentences per section. |
| Headline max **8 words** vs template H1 ~35 characters (excluding spaces) | Channel can pass copy the HTML clips. If a template is tighter, match that box. |
| Tone says **flexibility**; Channel General bans **flexible** / **scalable** | For email prompts, still substitute. See [brand-guidelines.md](brand-guidelines.md). |

## Supplemental module counts

`Character Count_Template.pdf` lists module max characters **not including spaces** (Subject 40, Preheader 50, H1 35, H2 40, H3 35, Body 500, CTA 25, Secondary CTA 200). Prefer the **Limits** table above for GenStudio Channel and prompts unless the user cites a tighter template.

## Prompting tip

Encode body limits in pod directives, e.g.:

- `Pod1: In 300-400 characters…` or `Pod1: In 3 sentences maximum…`
- `Pod2: In 2 sentences maximum…`

Stay within **3 sentences per section** even when using a character target (`In 300-400 characters` is still allowed if it stays ≤ 3 sentences). Prefer **Strictly 300–400 characters** for single-section technical emails (see Technical copywriter pattern in [SKILL.md](SKILL.md)).

Do not paste the full Email Channel lists into the prompt. For Create-generated subject/preheader/headline/subheadline, a short field-craft block is allowed (align subject to body offer; preheader 40–90 with positive outcome and no subject repeat; headline max 8 words; subheadline max 45; no trailing periods). Do not put `Unlock`, `flexible`, `free`, `Learn more`, or `click here` in the prompt.
