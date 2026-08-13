---
name: target-activity-master
description: >-
  Formats Adobe Target activity master CSVs: Date Activated and Deactivated
  Date as yyyy-mm-dd. Always excludes activities whose names contain [Debug],
  [Debug JSON RECS], [QA], or [No-Op] (case-insensitive), plus dummy ID 372957.
  Inclusion is based on revision Activated/Deactivated windows (live at any
  point in the period), not flaky API state alone. After pull/combine, run
  post-collection cleanup for paused/reactivated and multi-mbox consolidation.
  Derives a single Activity Type column (Event, XT, Recs, Auto Target, AB Test,
  Auto Allocate) from Target API data plus optional enrichment Stage.
  Use when exporting, combining, enriching, or cleaning Target activity master lists.
---

# Target activity master list

## Instructions

1. When writing or rewriting `Date Activated` and `Deactivated Date`, use **yyyy-mm-dd** only.
   - Input like `2020-11-11T21:27:21.000Z` → output `2020-11-11`
   - Prefer timestamps from activity **revisions** (Activated / Deactivated / Archived).
   - Leave the cell blank when the source date is missing.
2. **Inclusion rule:** include an activity if it was **live at any point** in the report period (revision window overlaps the period).
   - Discover candidates in API states `approved`, `deactivated`, and `saved` (UI Inactive can still be API `saved`).
   - Keep only activities with an **Activated** revision and a live window overlapping the period.
   - Never-activated drafts (no Activated revision) stay out.
3. **Always exclude** activities whose names contain any of these markers (**case-insensitive**):
   - `[Debug]`
   - `[Debug JSON RECS]`
   - `[QA]`
   - `[No-Op]`
4. **Always exclude** permanent dummy IDs in `live_windows.EXCLUDED_ACTIVITY_IDS` (currently `372957` — CP Homepage Adobe Target Ready).
5. Prefer `period-report.py` + `export-master-csv.py` (shared logic in `live_windows.py`).
6. Status column: map API `approved` → `live`; `deactivated` or `saved` (when included) → `deactivated` (UI Inactive).
7. **Domains column:** always replace `redhat.com; www.redhat.com` with only `redhat.com` (same pair in either order, with normal spacing around `;`). Leave other domain lists unchanged.
8. **Activity Type column:** derive directly from Target API data using the rules below. Do **not** emit separate `Sub-Type` or `Events/AB Tests` columns.
9. After pull + combine, run **Post-collection cleanup** (below). Do not hardcode activity IDs — detect from row patterns.

## Date examples

| Source | Output |
|--------|--------|
| `2020-11-11T21:27:21.000Z` | `2020-11-11` |
| `2026-06-29T14:38:51.000Z` | `2026-06-29` |
| *(empty)* | *(empty)* |

## Exclusions

- Name markers (case-insensitive): `[Debug]`, `[Debug JSON RECS]`, `[QA]`, `[No-Op]`
- Dummy activity ID `372957` (`CP Homepage Adobe Target Ready`)
- Do not include excluded activities in master lists, reports, or combined files.

## Activity Type

Single classification column. Allowed values:

| Activity Type | When to use |
|---------------|-------------|
| `Event` | Enrichment **Stage** is `Event` (see below) |
| `Recs` | Recommendations signals match |
| `XT` | API `type` is `xt` and not Recs |
| `Auto Target` | API `type` is `abt` with `optimizeByExperience` |
| `AB Test` | API `type` is `ab`, or `abt` with explicit experiences (not Auto Target) |
| `Auto Allocate` | API `type` is `auto_allocate` |
| *(blank)* | Unmapped types (`Unknown`, Automated Personalization, ABT unspecified, etc.) |

**Precedence** (first match wins):

1. **Event** — enrichment join **Stage** = `Event` (from `redhat_activities_experiences_4`, matched on Activity ID + Experience ID). Replaces the former `Events/AB Tests` Event override.
2. **Recs** — `has_recommendations_signals()` matches (see below).
3. **Auto Allocate** — API `type` = `auto_allocate`.
4. **AB Test** — API `type` = `ab`, or `abt` with `explicitExperiences` (and not Auto Target).
5. **Auto Target** — API `type` = `abt` with `optimizeByExperience` in `targetedExperience.explicit`.
6. **XT** — API `type` = `xt`.
7. Else leave **blank**.

Requires full activity detail from `get_activity` for `abt` discrimination (Auto Target vs AB Test). Monthly JSON alone is not sufficient for `abt` rows.

### Recs detection

Adobe API `type` is often `xt` even for Recs activities. Classify as **Recs** when any signal matches:

| Signal | Example |
|--------|---------|
| Activity name contains `recommend` or `recs` | `... \| Recs`, `... Recommendations` |
| Mbox name contains `recs` | `myRH-trainingRecs`, `myRH-eventsRecs` |
| Experience name contains `recommend` or `recs` | `RHEL recommendations`, experience named `Recs` |
| Detail payload contains recommendation criteria | `recommendationCriteria`, `criteriaId` |

Implemented in `export-master-csv.py` → `has_recommendations_signals()` and `classify_activity_type()`.

### Google Sheet enrichment (V2 Jan-July 2026)

| Column | Field | Notes |
|--------|-------|-------|
| S | Activity Type | **Active** — XT, Recs, Event, Auto Target, AB Test, Auto Allocate |
| P | Events/AB Tests | **Deprecated** — do not read or write; replaced by Activity Type (S) |
| U | events | **Active** — `True` / `False` from Activity Name keywords (`Events`, `Summit`, `Summit Connect`) |
| R | UX | From mbox skill + enrichment; do not overwrite populated cells |
| T | Multi UX (True or False) | `True` when UX is Multi-UX label or activity uses >1 unique mbox |

- Write **Activity Type** only to column S (`update-v2-activity-type.py`). Do not backfill **Sub-Type** (F) or **Events/AB Tests** (P).
- Write **events** only to column U (`update-v2-events.py`). **Never modify column P.**
- Use `classify_activity_type(act, detail, stage=…)` with **Stage** (O) when present for Event in Activity Type.

## Post-collection cleanup

Run after the live-in-period pull and combine. Key = **Activity ID + Experience ID**. Do not hardcode activity IDs.

### Paused and reactivated

**Detect:** same Activity ID + Experience ID appears with **more than one distinct** (`Date Activated`, `Deactivated Date`) pair.

**Action:** collapse to **1 row** per Activity ID + Experience ID:
- `Date Activated` = earliest (min) among those rows
- `Deactivated Date` = latest (max) among those rows
- Keep other columns from any representative row in the group

### Multi-mbox

**Detect:** same Activity ID + Experience ID appears with **more than one distinct** `Mbox` value.

**Action:** collapse to **1 row** per Activity ID + Experience ID:
- Set `Mbox` to exactly `Multi-mbox`
- Keep other columns from any representative row in the group

### Domains

**Always** rewrite the Domains cell when it is exactly the redhat.com + www.redhat.com pair:
- `redhat.com; www.redhat.com` → `redhat.com`
- `www.redhat.com; redhat.com` → `redhat.com`

Do not drop other domains from longer lists unless the entire cell is only that pair.

### Order

1. Apply name/ID exclusions (if not already applied).
2. Normalize **Domains** (`redhat.com; www.redhat.com` → `redhat.com`).
3. Apply **paused and reactivated** consolidation.
4. Apply **multi-mbox** consolidation.
5. Write the cleaned master CSV.
