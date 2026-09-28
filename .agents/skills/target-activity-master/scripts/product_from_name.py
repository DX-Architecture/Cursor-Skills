"""Derive Product label from Activity or Experience Name using contains rules."""

from __future__ import annotations

import re

# First match wins (order matters for overlapping names).
PRODUCT_RULES: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("RHEL", ("rhel", "infrastructure")),
    ("Openshift", ("openshift", "virtualization", "app-development", "ove")),
    ("Ansible", ("ansible", "automation")),
    (
        "AI",
        (
            "rhoai",
            "rhai",
            "ai infrence",
            "ai inference",
            " ai ",
            "ai - ",
        ),
    ),
)

TOKEN_NEEDLES = frozenset({"ove"})


def _matches_needle(lower: str, needle: str) -> bool:
    if needle in TOKEN_NEEDLES:
        return bool(re.search(rf"\b{re.escape(needle)}\b", lower))
    return needle in lower


def product_from_name(name: str) -> str:
    lower = (name or "").lower()
    for product, needles in PRODUCT_RULES:
        if any(_matches_needle(lower, needle) for needle in needles):
            return product
    return ""
