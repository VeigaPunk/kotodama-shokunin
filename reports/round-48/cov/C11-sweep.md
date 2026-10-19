# C11 — sweep verifier (claim C): a staged 224 tree, sweep green, prose vector sums 224

- Seat: `C11` | role: verifier | claim: **C** (coverage) | round 48, loop 2, position 2
- Baseline: `git rev-parse HEAD` → `a01405dd36367292255c2652ac0a601f4cd6a0af` (= `reports/round-48/claims.json:7`), 2026-10-19
- Out path: `reports/round-48/cov/C11-sweep.md` (this file; the only file I wrote outside `$TMPDIR`-staged scratch)
- Non-author statement: I authored no C fragment. The entry I staged is a **verification fixture** (136 lines, written by me to exercise the sweep), **not** C01's draft. The claim's authored bytes remain C01's; the recipe below re-runs on them unchanged.

**One-line judgment.** On a staged 224 tree the index sweep is **green**: `rows 224 files 224`, `missing 0 / topic_mismatch 0 / orphan 0 / drift {}`, `totals_line 224 totals_ok True`, `footer_ok True`, exit 0. The footer vector is `25/26/26/29/24/94` = **224**, and the repaired rev-2.4 prose vector now sums correctly (220 → 223). Three planted controls each turn the sweep red, so the green is measured, not assumed.

---

## 1. Why the stage is faithful

`sweep.py` derives all its paths from its own location (`reports/round-28/readme/sweep.py:44-47`: `LANE = HERE/../../..`, then `corpus/README.md` and `corpus/knowledge`), so a staged tree needs the same *relative depth*: `<stage>/reports/round-28/readme/sweep.py` + `<stage>/corpus/`. Both were copied with `cp -a`; the copied script is byte-identical to the repo's (`sha256sum` of both → `9b2ccac0046831fdaf48863ccd0ff6ca0fa390d044746c876e83a71c06f0cdd3`, two identical lines).

```
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
S=.scratch/r48-c11/stage
mkdir -p $S/reports/round-28/readme
cp -a corpus $S/corpus
cp reports/round-28/readme/sweep.py $S/reports/round-28/readme/sweep.py
```

**Pristine control (before any delta):**

```
$ find $S/corpus/knowledge -name '*.md' | wc -l
223
$ python3 -B $S/reports/round-28/readme/sweep.py | tail -3
footer_live {"total": 223, "dir_totals": [25, 26, 25, 29, 24, 94], ...}
footer_findings [] footer_ok True
readme_sha256 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
```

The staged README sha equals the live one (`7c788a1d…`), and the live sweep at HEAD produces the same sha and `rows 223 files 223`. So the stage starts at exact parity with production; every delta below is attributable to the round.

## 2. The delta applied to the stage

Six edits, each asserted to match exactly once (a Python `str.replace` guarded by `count == 1`):

| # | Edit | Before | After |
|---|---|---|---|
| 1 | culture-material section header | `## culture-material/ (25)` | `(26)` (staged README:246) |
| 2 | new row in filename order | between `calendar-festival-systems.md` and `costume-semiotics.md` | inserted at staged README:253; topic text generated from the entry's own `- topic:` block |
| 3 | totals line | `Total knowledge entries: 223.` | `224.` (staged README:557) |
| 4 | counts footer | `(total 223 files; directory totals 25/26/25/29/24/94)` | `(total 224 files; directory totals 25/26/26/29/24/94)` (staged README:559-561) |
| 5 | rev-2.4 prose-vector repair | `25/23/25/29/24/94 → **25/23/26/25/24/94**` (sums 217) | `25/23/25/29/24/94 → **25/26/25/29/24/94**` (sums 220 → 223) |
| 6 | rev-2.5 block inserted before rev 2.3 | — | staged README:14-23, states 223 → 224 and 25/26/25/29/24/94 → 25/26/26/29/24/94 |

Row placement checked independently: the section's 26 filenames are **sorted**, and `cartography-and-mapmaking.md` sits at index 5 with `calendar-festival-systems.md` before and `costume-semiotics.md` after. Row text is byte-equal to the entry's `topic_of()` join — independently recomputed, `row == "- \`cartography-and-mapmaking.md\` — " + topic` → `True` (row 1,305 chars; sweep reports `topic_mismatch 0`).

**Entry length discipline.** Fixture entry: **136 lines**, inside the live band `min 103 / median 149 / max 221` (recomputed over the 25 live culture-material files). It is 0.62× the live max, not r47's 790-line over-build. This is evidence that a right-sized body lands, not a claim that C01's body is this one.

**Landing surface.** `sha256sum` over every live and staged `corpus/knowledge/**/*.md` diffs to exactly one added line — no existing entry modified:

```
$ diff .scratch/r48-c11/live.sha .scratch/r48-c11/stage.sha
99a100
> 2521e759977f4488cbb571fad8e57b0347186f496b1604e46404060c969a733e  knowledge/culture-material/cartography-and-mapmaking.md
```

New entry sha256: `2521e759977f4488cbb571fad8e57b0347186f496b1604e46404060c969a733e`. Staged README sha256 after all six edits: `8b025254d02051ec053f83f1d60a6b315d1bd95bbaf9725a35bf8dcdd820161b` (589 lines).

## 3. The measurement at 224 (the delivery certificate)

```
$ python3 -B .scratch/r48-c11/stage/reports/round-28/readme/sweep.py
parts {"civilizations": 94, "culture-material": 26, "linguistics": 25, "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 224 files 224
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 224 totals_ok True
footer {"date": "2026-10-19", "command": "python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge", "total": 224, "dir_totals": [25, 26, 26, 29, 24, 94]}
footer_live {"total": 224, "dir_totals": [25, 26, 26, 29, 24, 94], "order": ["linguistics", "myth-symbol", "culture-material", "synthesis", "verification", "civilizations"]}
footer_findings [] footer_ok True
readme_sha256 8b025254d02051ec053f83f1d60a6b315d1bd95bbaf9725a35bf8dcdd820161b
EXIT=0
```

JSON form: `ok True rows 224 files 224 footer_ok True totals True`.

Independent recounts (not read from the sweep):

```
$ find .scratch/r48-c11/stage/corpus/knowledge -name '*.md' | wc -l
224
$ ls .scratch/r48-c11/stage/corpus/knowledge/culture-material/*.md | wc -l
26
```

## 4. Prose-vector arithmetic (the leg the sweep does NOT cover)

The sweep measures the footer vector and the totals line; it does **not** read the revision prose. So the prose vector is checked separately, by summing every six-tuple in the staged README:

```
footer total 224 vector 25/26/26/29/24/94 sum 224
totals line 224
rev2.5 vectors ['25/26/25/29/24/94', '25/26/26/29/24/94', '25/26/25/29/24/94']
rev2.4 vectors [('25/23/25/29/24/94', 220), ('25/26/25/29/24/94', 223)]
```

Reading: rev 2.4's before-vector 220 and after-vector 223 are now correct (previously the after-vector printed 217); rev 2.5 moves 223 → **224**; the footer states 224; the totals line states 224. All four agree.

- **Recorded defect being repaired** (live bytes, `corpus/README.md:5-13`, defective line `:11`): rev 2.4 printed `→ **25/23/26/25/24/94**` = 217, against a stated total of 223. The repair keeps the before-vector (220) and corrects the after-vector to the measured partition `25/26/25/29/24/94` (223).
- Rev 2.5's own prose avoids reprinting a bare defective 6-tuple; it describes the defect in words (myth-symbol left at 23, culture-material raised to 26) so a naive "sum every vector" check cannot pick up a 217 from narrative text.

## 5. Negative controls — the green is falsifiable

Three broken copies of the stage; each mutates one thing an integrator could plausibly get wrong:

| Control | Mutation | Sweep result |
|---|---|---|
| `nc1` | new README row deleted (entry still on disk) | `ok False`, `rows 223 files 224`, `missing_from_index 1 ['culture-material/cartography-and-mapmaking.md']`, exit **1** |
| `nc2` | footer reverted to `(total 223 … 25/26/25/29/24/94)` | `ok False`, `footer_findings [FOOTER_TOTAL 223 vs 224, FOOTER_DIR_TOTALS [25,26,25,29,24,94] vs [25,26,26,29,24,94]]`, exit **1** |
| `nc3` | section header reverted to `(25)` | `ok False`, `header_drift {'culture-material': {'declared': 25, 'files': 26}}`, exit **1** |

Exit codes: `stage EXIT=0`, `nc1 EXIT=1`, `nc2 EXIT=1`, `nc3 EXIT=1`. So the same instrument that certifies 224 also rejects a missing row, a stale footer, and an un-updated header.

## 6. Scope, limits, and what the integrator must redo

- **This is a sweep certificate only.** It does not certify the entry's content, arithmetic, citations, boundary table or worked example — C03/C04/C05/C12/C14 own those, and they must audit C01's real body, not my fixture.
- **Re-run against the assembled draft.** The sweep's only dependencies on the entry are (a) the filename `cartography-and-mapmaking.md`, (b) the exact `- topic:` text, (c) that exactly one file is added. If C01's topic differs from my fixture's, the README row must be regenerated from C01's topic (byte-equal), then this recipe re-run; the expected output is identical except `readme_sha256`.
- **Method note for the integrator:** do not edit `corpus/README.md` and then run the sweep in-tree *before* landing the entry — the sweep is read-only over the lane and will go red on the half-applied state (`missing_from_index` if the row precedes the file, `orphan_rows` if the file precedes the row). Apply both, then run. (I used a staged copy precisely to avoid mutating the live index during a parallel wave.)
- **No live writes.** `git status --porcelain` after all staging → `?? reports/round-46/review/`, `?? reports/round-48/` only; nothing under `corpus/` changed, no filed bytes touched, no in-tree `run-validation.py` executed.
- **Out of scope here:** the README duplicate-H1 (measured in the stage as unchanged: `h1 index count 2`, staged README:1 and :3) is claim **Ca**; phasing this C-stage into a Ca-ready tree was not done and must not be read as a Ca result.
- **To-verify:** none. Every figure above is a command output captured this run; the fixture entry's own external-content marks are the fixture's problem, not this certificate's.
