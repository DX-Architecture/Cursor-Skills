# Contributing

Thanks for helping grow the DX Architecture Cursor skills catalog.

## Add a new skill

1. Fork the repo and create a branch:
   ```bash
   git checkout -b add/<skill-name>
   ```
2. Create a skill folder:
   ```bash
   mkdir -p .cursor/skills/<skill-name>
   ```
3. Add a required `SKILL.md` (see template below).
4. Optionally add supporting files:
   - `reference.md` — deep docs
   - `examples.md` — concrete input/output examples
   - `scripts/` — helper scripts the agent should run
5. Update the **Skills** table in `README.md`.
6. Open a pull request using the PR template.

### Naming

- Folder and `name:` field: lowercase letters, numbers, hyphens only (e.g. `genstudio-email-prompts`)
- Max 64 characters
- Prefer specific names over generic ones (`review-pr-checklists`, not `helper`)

### Skill template

Create `.cursor/skills/<skill-name>/SKILL.md`:

```markdown
---
name: skill-name
description: What the skill does and when to use it. Include trigger terms.
---

# Skill Title

## When to use

- Situation 1
- Situation 2

## Instructions

1. Step one
2. Step two

## Examples

Concrete example of expected output.

## Additional resources

- [reference.md](reference.md)
- [examples.md](examples.md)
```

### Checklist before opening a PR

- [ ] Skill lives in `.cursor/skills/<skill-name>/`
- [ ] `SKILL.md` has `name` and `description` frontmatter
- [ ] Description is third person and includes both **what** and **when**
- [ ] `SKILL.md` stays concise (prefer under 500 lines)
- [ ] No secrets, credentials, or private machine paths
- [ ] README Skills table updated
- [ ] Skill is self-contained (works when copied into another project)

## Improve an existing skill

Open a PR against the skill folder. Prefer small, focused changes (docs, examples, or instruction clarity).

## Report an issue

Use the **New skill proposal** issue template if you want to discuss a skill before implementing it, or open a blank issue for bugs/docs gaps.
