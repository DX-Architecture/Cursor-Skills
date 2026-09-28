---
name: mbox-translation
description: >-
  Maps Adobe Target mbox technical names to human-readable RHDC location
  labels. Use when translating mbox columns, labeling Target locations,
  enriching activity master CSVs, or when the user mentions mbox translation
  or location display names.
---

# Mbox translation

Partial mapping — revisit to fill remaining labels.

## Instructions

1. When showing or exporting Target activity data, translate `Mbox` values using the table below.
2. Prefer the **Translation** label in human-facing output; keep the technical mbox name in a separate column when both are useful.
3. Populate **UX** from the mbox using the mapping table (e.g. `hero-mbox` → `Inline - Hero`). Leave blank when no UX label is defined yet.
4. **`target-global-mbox`** and **`int_mbox`** — leave **UX** blank; these are populated by a separate mechanism (not mbox lookup).
5. **`keep-learning-json`** and **`recs-debug-mbox`** — test mboxes; leave **Translation** and **UX** blank.
6. If a mbox has no translation yet, leave the label blank (do not invent one) and note it as unmapped.
7. When the user adds or corrects a translation or UX label, update this skill's mapping table verbatim.

Suggested CSV column names: `Location` (or `Mbox Translation`) beside `Mbox`; `UX` for the UX category column.

## Mapping

| Mbox | Translation | UX |
|------|-------------|-----|
| `target-global-mbox` | General Inline UX | |
| `hp-featured-secondary` | RHDC Homepage Secondary Feature Card | Inline - Subhero secondary card |
| `int_mbox` | General Interstitial UX (ex. Banner, Sticky Card) | |
| `for-you-mbox` | RHDC For You Navigation | Inline - For You Nav |
| `hero-mbox` | RHDC Homepage Hero | Inline - Hero |
| `hp-featured-primary` | RHDC Homepage Primary Feature Card | Inline - Subhero Primary card |
| `myRH-myTrials` | Inline Banner for RHDC My Trial Page | Inline - MRH Trials Card |
| `myRH-trainingRecs` | My Red Hat Training Card | Inline - MRH Training Card |
| `myRH-certificationRecs` | My Red Hat Certification Card | Inline - Cert Card |
| `myRH-eventsRecs` | My Red Hat Events Card | Inline - MRH Event Card |
| `aside-promo-mbox` | RHDC sidepromo on blog and article pages | Inline - Blog Side Card |
| `blog-keep-exploring-mbox` | RHDC Blog Page 'Keep Exploring' | Inline - Blog Side Card |
| `customer-hero-mbox` | Customer Portal Marketing Block 1 | Inline - Marketing Block 1 |
| `deluxe-promo-mbox` | RHDC Article Page Deluxe Promo (bottom of page) | Inline - Article Bottom Promo Cards |
| `inline-promo-mbox` | RHDC Article Page Inline Promo (middle of page) | Inline - Article Middle Promo Cards |

## Still unmapped

Fill in later:

| Mbox | Translation | UX |
|------|-------------|-----|
| `keep-exploring-mbox` | | Inline - Blog Side Card |
| `affinity-data-mbox` | | Collects Affinity Data, No UX |

## Test mboxes (leave blank)

| Mbox | Translation | UX |
|------|-------------|-----|
| `keep-learning-json` | | |
| `recs-debug-mbox` | | |

Test mboxes — leave **Translation** and **UX** blank; do not map.

## Source

Derived from unique `Mbox` values in activity master CSVs (19 distinct mboxes; 15 mapped so far).
