# DX-Architecture

Public repository of Cursor Agent Skills for DX Architecture workflows.

## Skills

| Skill | Description |
| --- | --- |
| [`genstudio-email-prompts`](.cursor/skills/genstudio-email-prompts/) | Craft Adobe GenStudio for Performance Marketing prompts for Red Hat email experiences (single-product and multipod). |

## Using skills in Cursor

### In this project

Skills in `.cursor/skills/` are available automatically when you open this repository in Cursor. Invoke with:

```text
/genstudio-email-prompts
```

### Install into another project

Copy the skill folder into that project's `.cursor/skills/` directory:

```bash
mkdir -p /path/to/project/.cursor/skills
cp -R .cursor/skills/genstudio-email-prompts /path/to/project/.cursor/skills/
```

### Personal install (all projects)

```bash
mkdir -p ~/.cursor/skills
cp -R .cursor/skills/genstudio-email-prompts ~/.cursor/skills/
```

## Adding a skill

1. Create `.cursor/skills/<skill-name>/SKILL.md` with YAML frontmatter (`name`, `description`).
2. Add optional supporting files (`reference.md`, `examples.md`, scripts).
3. Keep `SKILL.md` concise; put deep detail in linked files.

See Cursor’s [Agent Skills](https://cursor.com/docs) guidance for authoring tips.
