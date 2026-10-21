# ReviewLessonsIndex — round 50: what `corpus/lessons/round-50.md` requires for the lessons audit to read findings 0

Seat: `ChousaR27R2.ReviewLessonsIndex-4` (leaf reviewer; no delegation).
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, base `4ad2683` (= HEAD).
Lane writes: this report only. The audit ran on temp copies. Advice to the round-50 integrator, not an admission.

## Verdict

The lessons index is **not at findings 0 at base**. Writing `round-50.md` alone cannot keep the audit green: the same change must also repair three base findings (F1). Section 3 is the exact requirement list. Section 4 shows that each requirement is necessary, using 17 one-mutation controls (N0–N15, with N11b) plus a baseline on a temp copy.

## 1. Current state (temp copy of the lane working tree, read-only)

- Copy: `/tmp/rli-r50.NYRfPn`, made with `tar` excluding `.git`, `.jj`, `.ufo`. All 35 `corpus/lessons/*.md` files and the audit script are byte-identical to base (`git hash-object` per file vs `git rev-parse 4ad2683:…`, 35/35 equal). No `git status`, `diff`, `add`, `commit`, `stash`, `checkout`, or `reset` was run in the lane.
- `python3 -B reports/round-25/audit/c31-lessons-index-audit.py --selftest` → `SELFTEST OK: 28/28`, exit 0.
- Default run `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` → exit **1**, `findings: 3`. Checks: C31 FAIL, C32 PASS (78 owners), C33 PASS, C34 FAIL, C34c PASS, C34b FAIL.
- Counts: lesson files 35; index rows 34; queue rows 78; formats gate-keeper 22 / fragment-index 5 / plain 8. README sha256 `99920503d7100760…` (44802 B).

## 2. Findings (severity order)

### F1 HIGH — base is red: three findings
- **C31-1** unindexed-file `round-49-verifier-spotcheck.md`. Committed at `4ad2683`. The README table has no row for it; the last `round-49` row is `corpus/lessons/README.md:104`.
- **C34-1** pin-drift `round-49.md`. README:104 says `bytes=35993 lines=293 sha8=272eab2e`. Live is `39223 / 317 / 51ab6a5c`.
- **C34-2** prose-arithmetic-drift. README:106 says `**Rows: 34. Files: 34.**`. Measured `[34, 35]`.

### F2 HIGH — nothing runs the audit, so red lands unnoticed
- No `*.py` file in the lane references `c31-lessons-index-audit` (`_grep`, gitignore respected). `reports/round-*/run-validation.py` does not invoke it either.
- The round-49 pin went stale in two later commits. `c6a174d` pinned 35993 B. `8cee755` (`+20` insertions, `0` deletions, 38784 B) and `d91c632` (`+4`, `0`, 39223 B) changed the file. The later bytes do not start with the `c6a174d` bytes, so the change is line insertion, not a tail append. No line was rewritten, but the pinned lesson changed without a re-pin.
- README:226 (Q-28-1) already records that the lessons ledger was "off the acceptance surface". SCORECARD.md:972 records green at revision-4 time only.
- Advice (not applied): put the audit on the round-50 acceptance surface, and gate on its default exit code (F3).

### F3 MEDIUM — `--json` exits 0 regardless of findings
- The `--json` branch returns 0 (`c31-lessons-index-audit.py:445-447`) before the findings check (`:460`). At base, `--json` reports three findings with exit 0, while the default run exits 1. Every control with findings shows `json_exit=0`.
- Gate on the default exit or on `findings`. Read pins from the receipt's `live` entries, not from its exit code.

### F4 MEDIUM — stale prose is unchecked and already wrong at base
- C34b reads the first `Rows: **N**` (collected at `:297-298`, taken with `[0]` at `:303`) and the last `**Rows: N. Files: M.**` (`:299-300`, last match wins). Everything else is hand-maintained. Control N15 (`Of the 33 index rows` left in place) → findings 0.
- Already stale at base:
  - §1 annotation `# 33` (README:40-41); 35 files now.
  - §4 `Of the 33 index rows, 30 carry…` and `the three that carry none` (README:255-258). Measured at base: 34 rows, 30 carry at least one question, four carry none (README self-row, round-1, round-25, round-49).
  - §3 histogram (README:128-157). Live: gate-keeper 22, fragment-index 5, plain 8.
  - Revision-4 line `plain 7 (total 34)` (README:460-462). Live: plain 8, total 35.

### F5 MEDIUM — Q-28-4 tells the scribe to do what the audit forbids
- README:229 says "re-pin as a new row, never an edit". A second row for one file is `C31-3 duplicate-row` (`:208-211`). Control N13 fails with `C31-3` and `C34-2`.
- The only route that passes is an in-place pin refresh, with old and new values recorded in a revision block (the revision-2 precedent, README:379-385).

### F6 LOW — audit calibration limits (tool owner; not gating round 50)
- **C33** (`:230-243`) is a substring test (`name in idx["text"]`). It passes unless a class name occurs nowhere in the README, and the §2 cells always contain all three. It does not check that §3 documents them.
- **C32** (`:151-167`) is existence-only. Control N12 (owner `round-50`, a directory) passes. Nothing checks that the owner closes the item. Disposition pointers are unchecked (README:346-351 names this as a known limit).
- **C34c** splits on `|` naively (`:279`). Harmless for the format and contract cells, which come first in the row.
- Pins use `splitlines()` (`:104`, `:109`), not `wc -l`. Control N9: a lesson without a final newline measures `lines=15`; `wc -l` gives 14, and the audit flags the `wc` value.

### F7 INFO — round-50 must be gate-keeper, 4/4
- README:453-455 records that the fleet sources contract asks every new `corpus/SOURCES.md` row for a round-lesson `## Gate` record. The round-50 frontier step opens SOURCES rows (task context). A lesson without a `## Gate` section would not carry that record. The audit does not check this. The basis is the README's account; I did not re-read the sources contract.

## 3. Requirements: what `corpus/lessons/round-50.md` needs for findings 0

**Lesson file**
- **L1** Exactly `corpus/lessons/round-50.md`, directly in `corpus/lessons/`. Any other `*.md` there without a row (drafts such as `round-50-draft.md`) is a finding (glob at `:101`).
- **L2** Class (`:47-54`, `:72-78`): a line that is exactly `## Gate` (trailing whitespace only) makes it gate-keeper. `## Gate — round 50` classifies as plain (N8). A `## Fragment index` line wins over Gate. Use gate-keeper (F7).
- **L3** Contract (`:81-89`): four column-0 lines `source:`, `verified-at:`, `recheck:`, `scope:`. The cell is `N/4`. `- source:`, `**source:**` and `sources:` do not count.
- **L4** Pin after the last byte change. Any later change to the file gives C34-1 (N7).
- **L5** Measure with the audit, not `wc -l`: `bytes` = file size; `lines` = `len(text.splitlines())`; `sha8` = first 8 hex of sha256 of the raw bytes. `python3 -B reports/round-25/audit/c31-lessons-index-audit.py --json` gives these in `live`.

**Index rows (README §2)**
- **I1** One row for `round-50.md`, after the round-49 row (README:104), in this shape:
  ```
  | `corpus/lessons/round-50.md` | gate-keeper | 4/4 | <Q-ids or none> | <disposition pointer> | bytes=<B> lines=<L> sha8=<S> |
  ```
  Pointer and Q cells: no unescaped `|` (N14).
- **I2** Row for the committed spot-check. It is required even if round 50 never lands, because it is C31-1 at base:
  ```
  | `corpus/lessons/round-49-verifier-spotcheck.md` | plain | 0/4 | none (the adjudication names no open item id) | `corpus/lessons/round-49.md` (the adjudicated lesson; outside-review record) | bytes=1880 lines=17 sha8=b1169c50 |
  ```
- **I3** In-place re-pin of README:104. Replace `bytes=35993 lines=293 sha8=272eab2e` with `bytes=39223 lines=317 sha8=51ab6a5c`. Never a second row (C31-3, N13).

**Counts and queue (machine-read)**
- **P1** README:106 becomes `**Rows: 36. Files: 36.**` once both rows land (34+2 rows; 35+1 file). It must stay the last bold `Rows: N. Files: M.` in the file (`:300`).
- **P2** README:255 `Rows: **78**.` stays 78 unless round 50 carries open questions. Each new Q row needs four cells and a resolving owner: a path, `operator`, `parent`, `lore-shokunin`, `integrator`, or `round-N` with `reports/round-N/` present (N10, N11b, N14). Update the first `Rows: **N**` in place.

**Prose the audit does not check (correct in place; revision-3 precedent)**
- §1 (README:40-41) `# 33` → `# 36`.
- §4 (README:255-258): recount the rows, the rows carrying a question, and the rows carrying none.
- §3 histogram (README:128-157): live class counts.
- Roll-call (README:353-354): add revisions 4 and 5.

**Revision bump (README §6 rule: superseding edits land as a new revision block)**
- **V1** Append `## Revision 5 — round-50 index rows (2026-10-21)` after the revision-4 block (end of file, README:467). It should state: rows added; the in-place re-pin with old and new values; the in-place count changes; the audit before (3 findings, exit 1) and after (0, exit 0; selftest 28/28); and the boundary.
- **V2** The block must contain no line starting with `|` and no bold `Rows:` count phrasing.
- **V3** No filed row's provenance text changes. The only pin that changes is round-49.md's, and the block records it.

**Sequence**
1. Finalize `round-50.md`.
2. Measure it with `--json` (`live`).
3. Write the rows, the counts and the revision block.
4. Run the default audit: exit 0 and `findings: 0`. Run `--selftest`: 28/28.
5. Any later byte change to a lesson restarts at step 2.

**Expected end state** (gate-keeper round-50, no Q rows): rows 36, files 36, queue 78, formats gate-keeper 23 / fragment-index 5 / plain 8, findings 0.

**Ready-to-apply bump:** `/tmp/rli-r50-readme-revision5.diff` (5 hunks, +25/−7). It carries the spot-check row and the round-49 re-pin as measured. Its round-50 row holds fixture pins (`bytes=499 lines=15 sha8=420b1b0b`) and must be replaced with the final measured values.

## 4. Controls (temp copy `/tmp/rli-r50.NYRfPn-sim`; one mutation each, bytes restored after each)

| id | mutation | default exit | findings | shows |
|---|---|---|---|---|
| BASE | revision-5 bytes | 0 | none | spec sufficiency |
| N0 | round-50.md absent, row kept | 1 | C31-2 ghost; C34-2 | a row needs its file |
| N1 | round-50 row dropped | 1 | C31-1; C34-2 | I1 |
| N2 | spot-check row dropped | 1 | C31-1; C34-2 | I2 |
| N3 | round-49 pin back at 35993 | 1 | C34-1 (bytes, lines, sha8) | I3 |
| N4 | count left 34/34 | 1 | C34-2 | P1 |
| N5 | contract 3/4, file has 4/4 | 1 | C34-3 contract | L3, I1 |
| N6 | class plain, file is gate-keeper | 1 | C34-3 format | L2, I1 |
| N7 | one byte added after pin | 1 | C34-1 bytes, sha8 | L4 |
| N8 | heading `## Gate — round 50`, pin refreshed | 1 | C34-3 format | L2 exact heading |
| N9 | pin lines = `wc -l`, no final newline | 1 | C34-1 lines 14 vs 15 | L5 |
| N10 | Q row, owner missing path (count 79) | 1 | C32-1 | P2 |
| N11 | Q row, owner `parent` (count 79) | 0 | none | P2 passes when right |
| N11b | Q row added, count left 78 | 1 | C34-2 queue 79 vs 78 | P2 |
| N12 | owner `round-50` | 0 | none | C32 existence-only (F6) |
| N13 | round-49 as a second row | 1 | C31-3; C34-2 rows 37 vs files 36 | F5 |
| N14 | Q row with unescaped pipe in question | 1 | C32-1 `<no owner cell>` | I4 |
| N15 | stale `Of the 33 index rows` | 0 | none | F4: prose unchecked |

After all controls, the revised README and the fixture were restored byte-for-byte, and the selftest read 28/28, exit 0.

## 5. Residual risk and verification gaps

- The round-50 pins in §3 and the diff are fixture values. Real pins come from the final `round-50.md` bytes.
- The `## Gate` requirement rests on the README's account of the sources contract (README:453-455). I did not re-read `corpus/SOURCES-CONTRACT-v1.md`.
- Disposition pointers are judgement calls. No tool resolves them.
- Not run, by scope: `reports/round-50/jj-colocation-probe.py`, `tools/check-claim-separability.py`, `reports/round-28/readme/sweep.py`, and any C, O or Ca check.
- The audit was run on a temp copy, as assigned. The copy is byte-identical for every input the audit reads, but nothing was run in the lane itself.
- Lessons-index changes touch no claim's `lands` (C: knowledge entry and `corpus/README.md`; O: three tools; Ca: three paths; `reports/round-50/claims.json`). The index revision does not change separability.
- Temp artifacts, outside the lane (about 930 MB, deletable): `/tmp/rli-r50.NYRfPn` (pristine copy), `/tmp/rli-r50.NYRfPn-sim` (simulation copy, restored), `/tmp/rli-r50-readme-revision5.diff`, and small fixtures under `/tmp/rli-*`.

## 6. Tooling record

- No installs or upgrades. Python 3.14.8 was already present and used as `python3`.
- Read-only git only: `cat-file`, `ls-tree`, `log`, `show`, `rev-parse`, and `hash-object` without `-w`.
- Standard coreutils and tar for the copy, plus `cmp`, `sha256sum`, `diff`, `wc`.
