# ExecReceipts — round-88 w1 (milestone r88-v1)

Seat: ExecReceipts (leaf executor). Judged on operability and depth.
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, toplevel asserted, HEAD `4b76524c51e1c2f76c99eeb3b629cfac08a44a76` (the frozen revision).

## 1. Bottom line

- **No land exists yet.** Claims O and D cannot be measured at a land. I did not run any future or fabricated land. The only counter runs are against the frozen head as a labelled pre-land control.
- **Pre-land control (lands = frozen head): O KILLED, D KILLED, rc 1.** This is the expected no-work result. Every O/D leg that depends on the unlanded artifacts fails. The frozen-counterfeit scores match their frozen expectations (honest 13, constant-pass 3, shotgun-all-labels 4, extra-id 4, filename-only 0).
- **The counter's `--selftest` returns rc 0 but is a false green.** The `exact-accepted` check passes only because its reader crashes and emits nothing. A correct reader would make that check fail. The runner records this as `FALSE_GREEN`. The rc-0 selftest is not evidence and must not be cited as a pass.
- **Deliverable:** `stage/ExecReceipts/run-final.py` (runner), plus receipts in `stage/ExecReceipts/pre-land-control-frozen/`, `guard-lands-absent/`, `guard-base-not-descendant/`, `manual-selftest/`.
- No production-file edits, no commits, no mutating git. No installs. No task calls and no subagents.

## 2. Runner: `stage/ExecReceipts/run-final.py`

Usage: `python3 -B <stage>/run-final.py --lands REV --out <stage>/<dir> --work /fast/scratch/hyaku/kotodama-r88/<name>` (`--keep-work` optional).

Runner sha256 `5422f22d4a7bd7a2523ef7d8168746525aa9f97d8f52210887cdd5d237c73852`. Python 3.14.8, git 2.56.0.

What it collects for one LANDS revision:

1. **Committed counter receipts.** The counter `reports/round-88/measure88.py` is materialised from the LANDS blob into scratch and run from there with `--root <lane> --lands <rev>`. Its `counter_sha256` is therefore the committed blob hash, and the runner cross-checks it (`counter_sha256_equals_lands_blob`). Claims O and D each get their own run and verdict (`PASS`/`KILLED`/`INPUTS_ABSENT`). Selftest runs separately.
2. **Selftest audit** (`selftest-audit.json`). Imports the copied counter and replays its exact-accepted check with the reader the counter builds, and with a reader that really emits the report.
3. **Census with rc.** Four scopes: worktree (stamped `revision_stamp: null`, HEAD and dirty paths recorded), and committed scopes for base, frozen and lands, each from a scratch clone checked out detached at that revision and asserted by toplevel.
4. **Registry.** Parsed from `git cat-file blob` of `corpus/SOURCES.md` at base, frozen and lands: row counts, tiers, statuses, rows for S931–S933, removed/added/changed rows, and per-column classification against the append-only rule (only `status`, `recheck`, `used_by` may change in place). Non-row line changes are also recorded.
5. **D independent check.** The heading count, section table rows and columns, cited new IDs, mined tier/status and byte growth, computed by the runner separately from the counter.
6. **No-harm.** Landed paths from `FROZEN..LANDS`, checked against the claimed `exports` read from the frozen `claims.json`. `PROVINCE.md` and `corpus/knowledge/**` changes outside the numerals entry, and whether the numerals entry changed only by pure insertion.
7. **Hashes and ancestry.** Blob sha256 of the frozen paths at base, controls, frozen and lands, an amendment check (lands vs frozen must be identical for the counter, `claims.json`, `cases.json`, and the four counterfeits), and ancestry booleans.

Guards (all fail closed, no counter run):
- `--out` must be under the ExecReceipts stage; `--work` must be below `/fast/scratch/hyaku/kotodama-r88/`.
- Lane git is limited to read-only verbs. `git status` uses `--no-optional-locks`. Clone checkouts are in scratch with toplevel asserted.
- LANDS must resolve to a commit and descend from the frozen head.
- Exit codes: 0 all pass, 1 any KILLED, FALSE_GREEN or failed audit, 2 usage / absent LANDS / absent inputs.

Logs (`stdout`/`stderr` of every subprocess) are copied into `out/logs/` before `SHA256SUMS` is written. I fixed a defect found during the first control run, where SHA sums were written before the logs were copied in. `sha256sum -c SHA256SUMS` verifies cleanly now.

## 3. Commands run and observed rc

| Command | rc | Result |
|---|---|---|
| `git rev-parse --show-toplevel`, `git rev-parse HEAD` (lane) | 0 | toplevel = lane; HEAD = 4b76524c |
| `git merge-base --is-ancestor` base/controls → frozen | 0 | both ancestors of frozen |
| `python3 -B reports/round-88/measure88.py --selftest` (HEAD copy) | 0 | `exact-accepted`, `extra-id-refused`, `set-equality` all `passed: true` (false green, see §4) |
| `python3 -m py_compile run-final.py` | 0 | compiles |
| runner `--lands 1111…` (nonexistent) | 2 | guard: `LANDS_ABSENT`, no counter run |
| runner `--lands 4956282…` (base; base is an ancestor of frozen, so frozen is not an ancestor of base) | 2 | guard: `LANDS_NOT_DESCENDANT_OF_FROZEN` |
| runner `--out /tmp/x` | 2 | guard: out outside stage |
| runner `--work /tmp/x` | 2 | guard: work outside scratch |
| runner `--lands 4b76524c… --out pre-land-control-frozen` | 1 | COLLECTED; O KILLED, D KILLED, selftest FALSE_GREEN; frozen amendments PASS; noharm PASS (vacuous, lands == frozen); registry old-row clean PASS |
| `sha256sum -c SHA256SUMS` (control) | 0 | OK, 14 log files included |
| unit checks on runner classifiers, synthetic in-memory strings | — | see §5 |
| `bash scripts/sources-census.sh validate --root <fleet> kotodama` (worktree) | 0 | 36 TSV lines (W01 5, W04 30), 0 E-codes; 9 dirty paths |
| same, committed base / frozen / lands clones | 0 | identical 36-line output at each committed scope |

Census script sha256 `3fb72615…` (`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh`).

## 4. Counter defects (reported, not retrofitted)

Frozen counter `reports/round-88/measure88.py` was not edited. Each defect below is grounded in a line I read, or in an observed control run.

1. **Selftest is a false green (observed, L254–257).** `counter_built_reader_emits_report: false`. The reader is generated with the JSON body as a *path* (`pathlib.Path("{…}").read_text()`), so it raises `FileNotFoundError` with rc 1 and no stdout. The `exact-accepted` check is `passed = (not ok) if wanted is False else True`, which passes exactly when the comparison refuses. A correct reader (replayed in the audit) is accepted by the comparison, so the check would be `False` and the selftest would exit 1. The check is inverted relative to its own docstring ("must accept a correct report").
2. **`extra-id-refused` is unconditionally True (L254).** Its `wanted` is `True`, so `passed = True` regardless of `ok`. It never tests the refusal.
3. **`set-equality` is a tautology (L256–257).** It compares a set literal to a set literal, so it touches no code under test.
   - An existing lane artifact, `reports/round-88/counter-selftest-false-green.json` (not mine, produced by another seat), shows the same `FileNotFoundError` traceback. I observed its head only and rely on my own replay.
4. **Worktree fallback in the O path (L131–133, L147–148).** `materialize` falls back to the worktree file when the LANDS blob is absent, and `cases_raw` falls back to base then worktree. The claim's `separability` says O "reads only the committed r86 baseline packet, reports/round-88/cases.json, tools/check-attestation-packet.py and reports/round-88/controls/*". The runner records `worktree_fallback_risk`. At the control, `tools/check-finding-sets.py` is absent everywhere, so no unlanded bytes are read. Code-read only, not exercised: a dirty worktree copy of the battery at lands would be graded.
5. **`counter_sha256` is the running file's hash (L197, L236).** It hashes `__file__`. A worktree-run stamp is therefore not the committed revision. Mitigated by the runner, which runs the committed copy and cross-checks it.
6. **D `table-rows` and `table-columns` are section-wide (L214–219).** Section bounds stop only at `\n## `, so `###` subsections count, and any 5-row table in the section satisfies the leg. The table is not checked to be the typology table. `new-rows-cited` (L220) is a bare regex over the whole section, so a prose mention counts.
7. **D `growth-bytes` is whole-file (L234).** Padding elsewhere in the entry satisfies the 2500-byte leg. The runner's `pure_insertion` check on the numerals entry is the mitigation, but the counter does not enforce it.
8. **Docstring drift (L13 vs L47).** Docstring says `filename-oracle 1`; `EXPECT` and `claims.json` say `filename-only 0`. The code's value is the frozen one, so the docstring is wrong.
9. **`battery-agrees` depends on the battery's JSON `passed` key (L190–191),** with no schema check; a missing key becomes `None` and fails rather than erroring. Safe but opaque.
10. **`claims.json` `census_before` says "854 rows" from `validate`.** `validate` prints no row count; the 854 is from census or registry parsing. The runner's registry parse gives 854 at base, frozen and lands.

## 5. Registry, noharm and unit checks

- SOURCES.md blob is identical at base, controls and frozen (`8cf12728…`), so the registry has not changed since base. 854 rows; tiers A 505 / B 326 / C 23; statuses mined 753 / queued 58 / rejected 43.
- S931–S933 are absent at frozen and at the control (no rows yet), as the claims' `before` predicts.
- Numerals entry is byte-identical base→frozen (`57fc7669…`, 34831 bytes). The D heading count is 0 at frozen.
- Old-row check: at the control, 0 rows removed, 0 changed, 0 added, 0 non-row line changes, clean.
- Unit checks on the runner's classifiers, run on synthetic in-memory strings (never written to the lane, never a land):
  - allowed in-place `status`/`recheck` edit → clean; tier edit → disallowed; removed row → not clean.
  - insertion-only edit of an entry → `pure_insertion` true; in-place edit → false.
  - D-independent on a correct fixture (heading, 5×5 table, all three IDs cited, mined B): `heading 1, data_rows 5, max_cols 5, cited [S931, S932, S933], mined B/mined ×3, growth 311`.
  - An earlier fixture error (citations placed after the next `##`) was mine, corrected, and re-run. Not a runner defect.

## 6. Unresolved

- **O and D are unmeasured.** There is no land; the runner must be re-run at the real LANDS revision. Every verdict in this report is the pre-land control, not a land.
- **Positive-path coverage is partial.** The runner's pass branch (a committed land where O and D pass) has not been exercised end-to-end. I did not fabricate a land to test it; the classifiers were tested in isolation only.
- **Counter defects §4 (1–3) make the selftest unusable as evidence.** Any claim that cites "selftest exit 0" is false. The L1 should either fix the counter at its next land or drop the selftest leg.
- **Planner-policy conflict:** L1 holds the planner seat; I did not resolve it and did not act on it.
- **Freshness/lowest-axis and R86-C1 debt** are untouched by this seat.

## 7. Tools

None installed or updated. Existing: Python 3.14.8, git 2.56.0, bash, gawk (used by the census script). No pacman transactions.

## 8. Commands for the L1 / main agent to run

- At the real land: `python3 -B <stage>/run-final.py --lands <land-sha> --out <stage>/<name> --work /fast/scratch/hyaku/kotodama-r88/<name>`.
- Read `<out>/manifest.json` for `verdict` and `rc`, and `<out>/claim-O.json` / `claim-D.json` for legs.
- Do not cite `selftest` as a pass; the verdict will show `FALSE_GREEN`.
