# ScoutLedgerSweepA — calibration ledger sweep A, round 75

Base: `f556d1049fe651d3d63975600b13acd9fb686f15` (lane working tree == base; `git rev-parse HEAD` = base, `git diff --stat base -- corpus/README.md reports/round-28/readme/sweep.py SHONEN.md` empty). All commands run read-only, cwd `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.

## Footer / README facts (base tree)

- Section headings: `## linguistics/ (30)` at line 344; `## myth-symbol/ (29)` at 376; `## culture-material/ (36)` at 407; `## synthesis/ (29)` at 447; `## verification/ (24)` at 479; `## civilizations/ (95)` at 505.
- Footer blocks (oldest→newest): line 749 block `Total knowledge entries: 243.` / `Counts checked 2026-10-25 ... (total 243 files; directory totals 30/29/36/29/24/95)`; line 792/794 round-73 block `Total knowledge entries: 247.` / `(total 247 files; directory totals 32/29/38/29/24/95)`; line 813/815 round-74 block `Total knowledge entries: 249.` / `(total 249 files; directory totals 32/29/40/29/24/95)`. **The LAST footer (line 813 block) is the live one** (total 249, vector 32/29/40/29/24/95 — linguistics 32, myth-symbol 29, culture-material 40, synthesis 29, verification 24, civilizations 95); README line 818 itself states the sweep "still parses the first".
- `reports/round-28/readme/sweep.py:106-108` `footer_reading()` does `m = FOOTER_RE.search(text)` — first match only, i.e. it grades against the line-749 footer (243), not the live 249 footer. Consistent with L75-04's `why`.

## Pair-by-pair (observe_cmd run EXACTLY as written)

### L75-01 — REPAIR — SHONEN.md:6
- observe_cmd: `git grep -c -E "^. S[0-9]{3}" f556d1049fe651d3d63975600b13acd9fb686f15 -- corpus/SOURCES.md`
- Output (exit 0): `f556d1049fe651d3d63975600b13acd9fb686f15:corpus/SOURCES.md:808` → parse `:([0-9]+)$` → observed **808** = expected_after 808.
- Stated token (parse `\((\d+) rows after round 56` on stated_text) → **412**. 412 ≠ 808 → **RED** ✓
- Anchor: `git show base:SHONEN.md | sed -n 6p` contains `...(412 rows after round 56 — 367 mined, 35 queued, 10 rejected...` — stated_text verbatim present at line 6 ✓

### L75-02 — REPAIR — corpus/README.md:344
- observe_cmd: `git diff --shortstat 4b825dc642cb6eb9a060e54bf8d69288fbee4904 f556d1049fe651d3d63975600b13acd9fb686f15 -- corpus/knowledge/linguistics/*.md`
- Output (exit 0): ` 32 files changed, 5689 insertions(+)` → parse `([0-9]+) files? changed` → observed **32** = expected_after 32.
- Stated token (parse `\((\d+)\)` on `## linguistics/ (30)`) → **30**. 30 ≠ 32 → **RED** ✓
- Anchor: `git show base:corpus/README.md | sed -n 344p` = `## linguistics/ (30)` — verbatim ✓

### L75-03 — REPAIR — corpus/README.md:407
- observe_cmd: `git diff --shortstat 4b825dc642cb6eb9a060e54bf8d69288fbee4904 f556d1049fe651d3d63975600b13acd9fb686f15 -- corpus/knowledge/culture-material/*.md`
- Output (exit 0): ` 40 files changed, 5590 insertions(+)` → observed **40** = expected_after 40.
- Stated token (`## culture-material/ (36)`) → **36**. 36 ≠ 40 → **RED** ✓
- Anchor: `git show base:corpus/README.md | sed -n 407p` = `## culture-material/ (36)` — verbatim ✓

### L75-04 — REPAIR — reports/round-28/readme/sweep.py:16 — ANCHOR DEFECT
- observe_cmd: `git grep -c "FOOTER_RE\.search" f556d1049fe651d3d63975600b13acd9fb686f15 -- reports/round-28/readme/sweep.py`
- Output (exit 0): `f556d1049fe651d3d63975600b13acd9fb686f15:reports/round-28/readme/sweep.py:1` → observed **1** = expected_after 1.
- Stated token (parse `adds that leg\.`) → `adds that leg.` ≠ 1 → **RED** ✓ (the pair IS red)
- **Anchor NOT verbatim**: `git show base:reports/round-28/readme/sweep.py | sed -n 16p` = `adds that leg.` — the stated_text `This instrument adds that leg.` wraps the line-15/16 boundary (line 15 ends `...This instrument`, line 16 is `adds that leg.`). The full sentence appears on no single base line. As written (stated_text × stated_at = 16) it fails the LEDGER leg "stated_text found at stated_at in the BASE tree" → **must be dropped or re-anchored pre-freeze**. Minimal re-anchor keeping the pair's meaning and its stated_parse: stated_text `adds that leg.` at `reports/round-28/readme/sweep.py:16` (verbatim at line 16, parse already `adds that leg\.`).

## Pairs NOT red / absent anchors

- All four pairs are red at base. One anchor defect: **L75-04** (above). L75-01/02/03 anchors verbatim at their stated_at lines.

## The 4 knowledge files missing an index row (base README)

Row diff per section (rows extracted between section heading and next `## <part>/` heading; zero ghosts in both sections):

**Linguistics (heading line 344; rows 345–375 = 30 rows; disk = 32 files):**
1. `conlang-scholarship.amend-2026-10-23.md` — row belongs at **line 347** (filename order: after `conlang-methodology.md` row, line 346; before `dialect-register-consistency.md` row, line 347)
2. `conlang-scholarship.md` — row belongs at **line 348** (immediately after the amend row)

**Culture-material (heading line 407; rows 409–446 = 38 rows; disk = 40 files):**
3. `heritage-taxonomy-models.amend-2026-10-24-r13.md` — row belongs at **line 429** (filename order: after `headgear-head-covering-codes.md` row, line 428; before `hunting-foraging-subsistence.md` row, line 429)
4. `heritage-taxonomy-models.md` — row belongs at **line 430** (immediately after the amend row)

(Amend-file sorts before its base file in both cases: `...scholarship.amend...` < `...scholarship.md`, `...models.amend...` < `...models.md`.)

## Install record

None — no tools installed or upgraded; only read-only git/grep/sed/wc/comm runs.

## Scratch

Working dir `/fast/scratch/hyaku/kotodama-r75/ScoutLedgerSweepA/` held only transient README.base.md and row/disk name lists; deleted before yield. No fetches, no clones, no fixtures.
