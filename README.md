# DX-Architecture

Public catalog of Cursor Agent Skills for DX Architecture workflows. Open this repository in Cursor to use skills automatically, or copy individual skill folders into another project.

## Skills

| Skill | Description |
| --- | --- |
| [`genstudio-email-prompts`](.cursor/skills/genstudio-email-prompts/) | Craft Adobe GenStudio for Performance Marketing prompts for Red Hat email experiences (single-product and multipod). |
| [`target-activity-master`](.cursor/skills/target-activity-master/) | Format and clean Adobe Target MCP activity master CSVs (live-in-period inclusion, exclusions, date formatting, paused/reactivated and multi-mbox cleanup). |

## Repository structure

```text
.cursor/skills/
  <skill-name>/
    SKILL.md          # required — instructions + frontmatter
    reference.md      # optional
    examples.md       # optional
    scripts/          # optional
CONTRIBUTING.md       # how to add or improve skills
.github/              # PR and issue templates
```

Each skill is a self-contained folder under `.cursor/skills/`. Contributors add new skills by creating a new folder and opening a PR.

## Using skills in Cursor

### In this project

Skills in `.cursor/skills/` load when you open this repository in Cursor. Invoke with:

```text
/genstudio-email-prompts
```

### Install into another project

```bash
mkdir -p /path/to/project/.cursor/skills
cp -R .cursor/skills/genstudio-email-prompts /path/to/project/.cursor/skills/
```

### Personal install (all projects)

```bash
mkdir -p ~/.cursor/skills
cp -R .cursor/skills/genstudio-email-prompts ~/.cursor/skills/
```

## Contributing

We welcome new skills and improvements.

1. Read [CONTRIBUTING.md](CONTRIBUTING.md)
2. Add your skill under `.cursor/skills/<skill-name>/`
3. Update the Skills table above
4. Open a pull request

To discuss an idea first, open a **New skill proposal** issue.
