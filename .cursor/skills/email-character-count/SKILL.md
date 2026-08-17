---
name: email-character-count
description: >-
  Checks email copy character counts against section limits (subject line,
  preheader, H1, H2, H3, body, CTA, secondary CTA). Use only when the user
  explicitly asks to check email length, character counts, subject line,
  preheader, or these section guidelines.
disable-model-invocation: true
---

# Email character count

Count characters in each provided section and compare them to these limits.

## Limits

| Section | Limit | Required |
|---|---|---|
| Subject Line | 40 | yes |
| Preheader | 50 | yes |
| H1 (optional) | 35 | no |
| H2 (optional) | 40 | no |
| H3 (optional) | 35 | no |
| Body | 500 | yes |
| CTA | 25 | yes |
| Secondary CTA (optional) | 200 | no |

Use these values exactly. Do not substitute industry averages.

## Field aliases

Map copy-doc labels to skill sections when needed:

| Copy-doc label | Section |
|---|---|
| Subject line | Subject Line |
| Preview text | Preheader |
| Hero/banner heading | H1 |
| Hero – Title | H2 |
| Body copy | Body |
| CTA button copy | CTA |
| Secondary CTA | Secondary CTA |

## How to count

- Count every character, including spaces and punctuation.
- Trim leading and trailing whitespace first; do not count it.
- Do not count the section label (`Subject Line:`, `H1:`, etc.).
- Skip optional sections that are missing or empty. Do not fail them.
- Fail a required section if it is missing or empty.

## Workflow

1. Extract the copy for each section the user provided.
2. Run the checker (preferred), from this repository root:

```bash
python3 .cursor/skills/email-character-count/scripts/check_counts.py path/to/copy.txt
```

Or pass JSON:

```bash
python3 .cursor/skills/email-character-count/scripts/check_counts.py --json '{"Subject Line":"...","Preheader":"...","Body":"...","CTA":"..."}'
```

From the skill folder, use `python3 scripts/check_counts.py` instead.

3. If the script cannot run, count manually with the same rules and the same output format.
4. Report results. Do not rewrite copy unless the user asks.

## Output

Use this table, then a one-line pass/fail summary:

```markdown
| Section | Count | Limit | Status |
|---|---|---|---|
| Subject Line | 38 | 40 | Pass |
| Preheader | 52 | 50 | Fail (2 over) |
```

Status values:

- `Pass` — count is within the limit
- `Fail (N over)` — count exceeds the limit
- `Fail (missing)` — required section is empty
- `Skipped` — optional section not provided

Overall: **Pass** only if every required section passes and every provided optional section passes.

## Input format

Accept labeled copy like this:

```
Subject Line: ...
Preheader: ...
H1: ...
H2: ...
H3: ...
Body: ...
CTA: ...
Secondary CTA: ...
```

Optional headings may be omitted. Body may be multiple lines until the next section label.
