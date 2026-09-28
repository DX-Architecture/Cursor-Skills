#!/usr/bin/env python3
"""Check email section character counts against fixed limits."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

LIMITS = {
    "Subject Line": {"limit": 40, "optional": False},
    "Preheader": {"limit": 50, "optional": False},
    "H1": {"limit": 35, "optional": True},
    "H2": {"limit": 40, "optional": True},
    "H3": {"limit": 35, "optional": True},
    "Body": {"limit": 500, "optional": False},
    "CTA": {"limit": 25, "optional": False},
    "Secondary CTA": {"limit": 200, "optional": True},
}

LABEL_ALIASES = {
    "subject line": "Subject Line",
    "subject": "Subject Line",
    "preheader": "Preheader",
    "pre-header": "Preheader",
    "pre header": "Preheader",
    "preview text": "Preheader",
    "h1": "H1",
    "h1 (optional)": "H1",
    "hero/banner heading": "H1",
    "hero banner heading": "H1",
    "h2": "H2",
    "h2 (optional)": "H2",
    "hero – title": "H2",
    "hero - title": "H2",
    "hero title": "H2",
    "h3": "H3",
    "h3 (optional)": "H3",
    "body": "Body",
    "body copy": "Body",
    "cta": "CTA",
    "cta button copy": "CTA",
    "secondary cta": "Secondary CTA",
    "secondary cta (optional)": "Secondary CTA",
}

LABEL_PATTERN = re.compile(
    r"^(Subject Line|Subject|Preheader|Pre-header|Pre header|Preview text|"
    r"H1(?: \(optional\))?|Hero/banner heading|Hero banner heading|"
    r"H2(?: \(optional\))?|Hero [–-] Title|Hero Title|"
    r"H3(?: \(optional\))?|Body copy|Body|CTA button copy|CTA|"
    r"Secondary CTA(?: \(optional\))?)\s*:\s*(.*)$",
    re.IGNORECASE,
)


def normalize_label(label: str) -> str | None:
    return LABEL_ALIASES.get(label.strip().lower())


def count_chars(value: str) -> int:
    return len(value.strip())


def parse_labeled_text(text: str) -> dict[str, str]:
    sections: dict[str, list[str]] = {}
    current: str | None = None
    for raw_line in text.splitlines():
        match = LABEL_PATTERN.match(raw_line.strip())
        if match:
            current = normalize_label(match.group(1))
            if current is None:
                continue
            sections[current] = []
            remainder = match.group(2).strip()
            if remainder:
                sections[current].append(remainder)
            continue
        if current is not None:
            sections[current].append(raw_line)
    return {name: "\n".join(lines).strip() for name, lines in sections.items()}


def evaluate(sections: dict[str, str]) -> list[dict[str, object]]:
    rows = []
    for name, spec in LIMITS.items():
        raw = sections.get(name, "")
        text = raw.strip() if isinstance(raw, str) else ""
        optional = spec["optional"]
        limit = spec["limit"]
        if not text:
            rows.append(
                {
                    "section": name,
                    "count": 0,
                    "limit": limit,
                    "status": "Skipped" if optional else "Fail (missing)",
                    "pass": optional,
                }
            )
            continue
        count = count_chars(text)
        over = count - limit
        passed = over <= 0
        rows.append(
            {
                "section": name,
                "count": count,
                "limit": limit,
                "status": "Pass" if passed else f"Fail ({over} over)",
                "pass": passed,
            }
        )
    return rows


def render_table(rows: list[dict[str, object]]) -> str:
    lines = [
        "| Section | Count | Limit | Status |",
        "|---|---|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['section']} | {row['count']} | {row['limit']} | {row['status']} |"
        )
    overall = all(row["pass"] for row in rows)
    lines.append("")
    lines.append(f"Overall: **{'Pass' if overall else 'Fail'}**")
    return "\n".join(lines)


def load_sections(args: argparse.Namespace) -> dict[str, str]:
    if args.json:
        data = json.loads(args.json)
        if not isinstance(data, dict):
            raise SystemExit("JSON input must be an object of section name -> copy")
        sections = {}
        for key, value in data.items():
            name = normalize_label(str(key))
            if name:
                sections[name] = "" if value is None else str(value)
        return sections

    source = Path(args.path).read_text(encoding="utf-8") if args.path else sys.stdin.read()
    if not source.strip():
        raise SystemExit("No copy provided")
    stripped = source.strip()
    if stripped.startswith("{"):
        data = json.loads(stripped)
        return {
            name: str(value)
            for key, value in data.items()
            if (name := normalize_label(str(key)))
        }
    return parse_labeled_text(source)


def main() -> int:
    parser = argparse.ArgumentParser(description="Check email section character counts")
    parser.add_argument("path", nargs="?", help="Path to labeled copy or JSON")
    parser.add_argument("--json", help="JSON object of section copy")
    args = parser.parse_args()
    rows = evaluate(load_sections(args))
    print(render_table(rows))
    return 0 if all(row["pass"] for row in rows) else 1


if __name__ == "__main__":
    raise SystemExit(main())
