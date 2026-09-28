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
  Auto Allocate) from Target API data plus optional enrichment Stage. Derives
  Derives Product from Experience Name (or Activity Name) and Stage from events plus
  Activity Name (with separate partner stage taxonomy).
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
8. **Activity Type column:** derive directly from Target API data using the rules below.
9. After pull + combine, run **Post-collection cleanup** (below). Do not hardcode activity IDs — detect from row patterns.

## Master CSV columns

Emit **only** these columns, in this order. Do **not** include `Sub-Type`, `Reporting Suite`, or `Events/AB Tests` — those are retired.

| Column | Notes |
|--------|-------|
| Correlation ID | |
| Activity ID | |
| Activity Name | |
| Experience ID | |
| Experience Name | |
| Activity Type | XT, Recs, Event, Auto Target, AB Test, Auto Allocate |
| Priority | |
| Status | `live` or `deactivated` |
| Date Activated | yyyy-mm-dd |
| Deactivated Date | yyyy-mm-dd |
| Domains | |
| Mbox | |

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

1. **Event** — enrichment join **Stage** = `Event` (from `redhat_activities_experiences_4`, matched on Activity ID + Experience ID).
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

## Product

Derive **Product** for the Google Sheet (column M) from **Experience Name** by default. Use **Activity Name** only when Experience Name is too generic. Implemented in `update-v2-product.py` (`--from experience-name` or `--from activity-name`).

**Precedence** (first match wins, case-insensitive contains unless noted):

| Product | Name contains |
|---------|----------------|
| RHEL | `rhel`, `infrastructure` |
| Openshift | `openshift`, `virtualization`, `app-development`, `OVE` (whole word only) |
| Ansible | `ansible`, `automation` |
| AI | `rhoai`, `rhai`, `ai infrence`, `ai inference`, ` ai `, `ai - ` |

- Leave **blank** when no rule matches (cross-portfolio, geo, generic experiences).
- `OVE` must match as a token (`\bove\b`) so it does not match `Discover`, `Remove`, or `Override`.
- When both Activity and Experience names are available, prefer **Experience Name** — it is more product-specific.

Reference implementation: `scripts/product_from_name.py`.

## Stage

Derive **Stage** for the Google Sheet (column N) from the **`events`** column and **Activity Name**. Implemented in `update-v2-stage.py`. Run `update-v2-events.py` first.

**Precedence** (first match wins):

1. `events` = `True` → **Event**
2. Known **partner** activity overrides (by Activity ID or PZN)
3. Partner name contains rules (partner experiences only)
4. Customer lifecycle name contains rules

### Customer lifecycle stages (Activity Name)

| Stage | Name contains |
|-------|----------------|
| Discover | `discover` |
| Learn | `learn` |
| Evaluate | `evaluate` |
| Adoption | `adopt` |
| Expand | `upsell`, `upsale`, `cross sell`, `cross-sell` |

### Partner stages

Partner experiences use a **different** stage taxonomy. Detect partner rows when **Domains** includes `connect.redhat.com`, or Activity Name includes `to-partner`, `partner program`, or `connect - red hat partner`.

| Stage | Assignment |
|-------|------------|
| Interest | Name contains `interest` |
| Conversion | Name contains `conversion` |
| Onboarding | Name contains `onboarding` |
| Growth experiences | Name contains `to-partner`, `growth experience`; or PZN2867751 / Activity ID `643220` |
| Enablement & readiness motions | Name contains `enablement`, `readiness`, `partner program`, `enablement and readiness motions`; or PZN1387300 / Activity ID `582156` |

**Do not apply customer lifecycle stages** (Discover, Learn, etc.) to partner rows.

### Partner activities — ask the user

There is **no reliable dynamic rule** for all partner-tagged activities. When you find partner rows that are **not** covered by a known override or contains rule above:

1. **Stop** and list the unmatched activities (Activity ID, Activity Name, Domains).
2. **Ask the user** which partner Stage each should receive.
3. Add explicit Activity ID / PZN overrides to `stage_from_activity_name.py` only after the user confirms.
4. Do **not** guess or leave partner rows on customer stages.

Reference implementation: `stage_from_activity_name.py` (local `adobe-target-mcp` project).

### Google Sheet enrichment (V2 tabs)

Use one tab per period, e.g. `V2 Jan-July 2026`, `V2 August 2026`. **Create the tab** in the spreadsheet before the first push if it does not exist.

**Base columns (A–L)** — from master CSV push (`push-v2-sheet-from-csv.py`):

| Col | Field |
|-----|-------|
| A | Correlation ID |
| B | Activity ID |
| C | Activity Name |
| D | Experience ID |
| E | Experience Name |
| F | Activity Type |
| G | Priority |
| H | Status |
| I | Date Activated |
| J | Deactivated Date |
| K | Domains |
| L | Mbox |

**Enrichment columns (M–R)** — filled by enrichment scripts:

| Col | Field | Notes |
|-----|-------|-------|
| M | Product | From Experience Name contains rules (`update-v2-product.py`) |
| N | Stage | From `events` + Activity Name rules; partner overrides (`update-v2-stage.py`) |
| O | Translated? | From enrichment join |
| P | UX | From **mbox-translation** skill; do not overwrite populated cells |
| Q | Multi UX (True or False) | `True` when UX is Multi-UX label or activity uses >1 unique mbox |
| R | events | `True` / `False` from Activity Name keywords (`Events`, `Summit`, `Summit Connect`) |

- Write **Product** (M) from name rules (`update-v2-product.py --tab "…" --from experience-name`).
- Write **Stage** (N) after events (`update-v2-stage.py --tab "…"`).
- Write **Activity Type** to column F on CSV push, or backfill with `update-v2-activity-type.py`.
- Fill blank **UX** (P) from mbox (`update-v2-ux-from-mbox.py --tab "…"`).
- Set **Multi UX** (Q) (`update-v2-multi-ux.py --tab "…"`).
- Write **events** (R) only (`update-v2-events.py --tab "…"`).
- All enrichment scripts accept `--tab`; default tab varies by script — always pass `--tab` for monthly runs.
- Large sheet writes: `push-v2-sheet-from-csv.py` batches updates (~30 rows) to avoid Windows command-line limits.

### Monthly pipeline

For a single calendar month (example: August 2026):

1. `period-report.py --year 2026 --month 8`
2. `export-master-csv.py --year 2026 --month 8`
3. `post-collection-cleanup.py august-2026-activities-master-list.csv`
4. `push-v2-sheet-from-csv.py --csv … --tab "V2 August 2026"`
5. `update-v2-product.py --tab "V2 August 2026" --from experience-name`
6. `update-v2-events.py --tab "V2 August 2026"`
7. `update-v2-stage.py --tab "V2 August 2026"`
8. `update-v2-ux-from-mbox.py --tab "V2 August 2026"`
9. `update-v2-multi-ux.py --tab "V2 August 2026"`

Or orchestrate with `run-august-2026-pipeline.py` (`--skip-pull` when JSON/CSV already exist).

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
