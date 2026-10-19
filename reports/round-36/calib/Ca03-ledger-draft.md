- Seat: Ca03 | executor | claim Ca | date 2026-10-19 | baseline ce103bf

# Recount ledger draft — rounds 33–35 (claim Ca, mid-loop recount)

One row per counting command filed by rounds 33, 34 and 35. Every row carries the
filed result as it appears in a filed artifact, the result I observed today at
baseline `ce103bf`, and a disposition. Nothing here rewrites a filed byte; a
mismatch is named with its cause rather than smoothed.

**Revision 2 (2026-10-19).** Revised after `reports/round-36/calib/Ca04-verify.md`
§6.1 filed two corrections against revision 1: (a) the census block contradicted my
own table — corrected below to 21 rows / 17 distinct; (b) row `RC-35-7` was `pending`
— now observed and dispositioned. Ca04's correction (b) to its own §3.2 is also
recorded: my r33 index-reconstruction method reproduces the r33 runner green.

## Method and isolation

- Non-runner commands were re-run in-tree (read-only legs, plus `.scratch` for
  temporary state). `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.
- **No filed round runner was executed in-tree** (F-C13-1). The three round
  runners were replayed only in copies, by two methods:
  - **r33** — `git clone --no-hardlinks . <copy>`; `checkout da68a6d`;
    `git reset --mixed 139e3b662900557afe54f632b468619593dc9fcb` reconstructs the
    declaration-time tree (index-tracked paths `2655`, exactly the filed
    `baseline_paths`), with the fleet inputs mirrored read-only beside the copy.
    `run-validation.py:23` derives `ROOT` from `__file__`, so this works.
  - **r34/r35** — these hardcode an absolute `ROOT`
    (`reports/round-34/run-validation.py:10`, `reports/round-35/run-validation.py:9`)
    and `os.chdir(ROOT)` (`:26` / `:36`), so they cannot run from a copy at all.
    They were replayed under `unshare -rm --propagation private` with the copy
    **bind-mounted over the lane path**, which makes the live bytes unreachable
    inside the namespace. The copy is a self-contained clone (`git clone`, no
    `--shared`): a `--shared` clone's `objects/info/alternates` points outside the
    mount and every `git` call inside the namespace dies (`fatal: bad object HEAD`).
- **TMPDIR matters.** Redirecting a runner's output to `/tmp` fails: `/tmp` is a
  tmpfs at 80% (`df -h /tmp` → `16G 13G 3.1G 80%`) and redirected runs die with
  **exit 120** and a 0-byte file. That is what killed my first two r35 attempts,
  not a runner failure. Independently measured by `Ca01-recount-33-34.md` §1 and
  `K03-recount-scout.md`. All receipts below were written under `.scratch/`.
- **Concurrency matters.** `Ca01-recount-33-34.md` §4 measures that r35's O-legs
  (`v3_controls`, `quiet_sha`) are only reproducible when the r35 runner is the
  **sole** v3-selftest consumer; a concurrent v3 consumer yields a false red
  (`v3_controls: 0`). The successful r35 run recorded below was serial.
- Both runners' `--check` mode is print-only (`--check never writes the receipt`);
  every isolated run redirected under `.scratch/`. Confirmed after the fact: the
  live `reports/round-33|34|35/validation.json` were not written by this seat.
- Three further method findings: `git archive` extracted **inside** the repo is not
  isolation — `git rev-parse` ascends to the live `.git`; the lane's `.scratch` is
  gitignored, so a copy must be made with `git clone`; and `--check` is the safest
  runner mode for a verifier that only needs the measurement.

## Census

The census depends on how each round's own runner command is counted. Three
conventions are reported so the denominator is not ambiguous; the table below
follows convention (1).

| | r33 | r34 | r35 | total |
|---|---|---|---|---|
| (1) rows in this ledger's table | 5 | 9 | 7 | **21** |
| (1) distinct commands (deduped) | 4 | 6 | 7 | **17** |
| (2) `claims.json` `counting_commands` entries (K03 §1) | 5 | 8 | 7 | **20** |
| (2) distinct `claims.json` strings (K03 §1) | 4 | 5 | 5 | **15** |

The two conventions differ in exactly two places, both definitional:

- **r34's own runner.** `reports/round-34/claims.json` declares it once per claim
  (D, O, C → 3 entries). This ledger splits it by leg scope into 4 rows (rows 8–11:
  D, O, cross, C), because each leg was observed separately and the C leg behaved
  differently from the other three. Hence r34 rows 9 vs entries 8.
- **`box1-survey.py`.** Declared in `reports/round-34/claims.json` claim C, and also
  quoted at `SCORECARD.md:617`. K03 counts SCORECARD-only strings separately; this
  ledger counts it once.

No filed number depends on the convention.

## Rows

Disposition vocabulary: `match` (observed == filed), `dispositioned-mismatch`
(observed != filed, cause named, class assigned), `could-not-reproduce` (with
owner and reason). Classes: `legitimate-change`, `environmental`, `reconstruction-artifact`.

| # | round | command | filed | observed | disposition / class |
|---|---|---|---|---|---|
| 1 | 33 | `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` | exit 0; 33 files == 33 rows, 78 queue rows, formats `{gate-keeper 21, fragment-index 5, plain 7}`, findings 0 (`reports/round-33/validation.json` claims.O.legs.O1) | exit 0; `lesson files: 33 / index rows: 33 / queue rows: 78 / formats {'gate-keeper': 21, 'fragment-index': 5, 'plain': 7}` / `findings: 0` | match |
| 2 | 33 | `python3 -B reports/round-25/audit/c31-lessons-index-audit.py --selftest` | `SELFTEST OK: 28/28 checks passed` | `SELFTEST OK: 28/28 checks passed`, exit 0 | match |
| 3 | 33 | `test -s reports/round-33/op/O05-falsifier-disposition.md` | disposition landed (claims.O counting command) | exit 0 (file present, non-empty) | match |
| 4 | 33 | `python3 reports/round-33/run-validation.py` (C-leg scope) | C legs green | isolated reconstruction, `--check` → exit 0, `acceptance true`, `failures []`, claims A/C/O/cross all `true` | match |
| 5 | 33 | `python3 reports/round-33/run-validation.py` (A-leg scope) | A legs green, incl. A3 `tracked_paths 2655` and A5 `last_touch c53782a` | same isolated run: A green. The `git reset --mixed 139e3b6…` reconstruction is what makes A3 pass — `run-validation.py:935` reads the **index** (`git ls-files`) and `:936` reads `git ls-tree 139e3b6`, so both sides measure 2655 | match |
| 6 | 34 | `python3 tools/gates/handoff-packet-check.py reports/round-34/handoff/declared-in-r7/packet.md` | gate green: 16/16 + 20/20 + findings 0 | `INFO scan: fields=16/16 glossary-entries=20 findings=0`, exit 0 | match |
| 7 | 34 | `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` | exit 0, `packet_sha256 45f57132…` | exit 0; `fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19` | match |
| 8 | 34 | `python3 reports/round-34/run-validation.py` (D-leg scope) | D1–D7 green: `claims_census true`, `freeze_packet_sha256 45f57132…`, `tamper_exit 1` | namespace-isolated clone@`4a7aede` reset `--mixed da68a6d`, `--check`: D leg byte-identical to filed | match |
| 9 | 34 | `python3 reports/round-34/run-validation.py` (O-leg scope) | O1–O5 green, `class_counts {guarded-refresh 18, unguarded-in-place 11}` | same isolated run: O leg identical (`18` / `11`), failures [] | match |
| 10 | 34 | `python3 reports/round-34/run-validation.py` (cross-leg scope) | CO1–CO5 green; `baseline_expanded da68a6d705e41f369f21e8607bfaab5b54077f84`; `claim_counts {C 13, D 27, O 15, cross 8}` | same isolated run: cross leg identical | match |
| 11 | 34 | `python3 reports/round-34/run-validation.py` (C-leg scope) | C1–C3 green, `skill_sha256 f9bd07c2…` | same isolated run: **exit 1**, C leg `failed` with `C3: filed-row edits detected for the reissue scope` | dispositioned-mismatch / **reconstruction-artifact** — `run-validation.py:258` greps `git status --porcelain -- corpus/lessons SCORECARD.md`; in my clone `SCORECARD.md` still carried the round-34 edit, so the leg fired. Not a defect in the filed record. Owner: seat Ca03. |
| 12 | 34 | `python3 tools/harness/receipt_guard_adoption.py --selftest` | selftest green (filed `op/O02-tool-source.md:41` records 38/38) | `selftest_passed: true`, `controls_passed 38`, `controls_total 38`, `live_runner_count 30`, exit 0 | match |
| 13 | 34 | `python3 tools/harness/receipt_guard_adoption.py --json` | `class_counts {guarded-refresh 18, unguarded-in-place 11}` (r34 validation O leg; SCORECARD.md:616 prose "all 29 filed runners: 18 guarded-refresh / 11 unguarded-in-place") | `class_counts {guarded-refresh 19, unguarded-in-place 11}`, `live_runner_count 30`, `findings 2`, `hazard_count 11`, `gaps 0`, `census_complete true` | dispositioned-mismatch / **environmental** (measurement instant) — the census is over the live tree and `reports/round-35/run-validation.py` landed after r34's measurement instant, so 29→30 runners and 18→19 guarded. `git ls-tree -r --name-only da68a6d | grep -c 'reports/round-.*/run-validation.py'` → 28, +r34's own runner = 29 (the filed figure); `… ce103bf …` → 30. The r34-time 18/11 reproduces exactly in the r34 reconstruction (row 9) and the live r34 `validation.json` still reads 18/11. Same disposition filed independently by Ca04 §3.1 and Ca05 §2. |
| 14 | 34 | `python3 -B reports/round-30/craft/box1-survey.py` | 28/28 named and resolvable at `skill_sha256 f9bd07c2…` | `named: 28`, `resolvable: 28`, `unnamed_in_skill: []`, `skill_sha256 f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b`, exit 0 | match |
| 15 | 35 | `for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done` | `21 / 23 / 24 / 29 / 20 / 94` = 211 | `21 / 23 / 24 / 29 / 20 / 94` = 211 | match |
| 16 | 35 | `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` | `inventory_files 211` (r35 validation C leg) | `totals.files 211` (also `files_with_marker 145`, `lines 38353`, `class_totals {substantive-flag-candidate 668, policy-use-mention 115, needs-review 293}`), exit 0 | match |
| 17 | 35 | `python3 -B reports/round-28/readme/sweep.py` | `totals_line 211 totals_ok True`; `footer_ok True`; `readme_sha256 51b966af…` (SCORECARD.md:640; r35 validation C leg `sweep_tail`) | `totals_ok True`, `footer_findings [] footer_ok True`, `readme_sha256 51b966af20483328c3e221d2ab0f766aa5cf0f5a0b140650b95eb841d6bea6f0`, exit 0 | match |
| 18 | 35 | `python3 -B tools/exercise-handoff-e2e.py --selftest` | exit 0 (claims.O counting command) | exit 0 | match |
| 19 | 35 | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json` | exit 1, named diagnostic, `traceback false` | exit 1; `handoff-v3: E2E-READSET: 1 read-set member(s) named by the frozen baseline are not in the live read set: reports/round-20/handoff/claims-map.md — the baseline row is superseded (re-point or re-freeze it)` | match |
| 20 | 35 | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest` | `v3_controls 44` (r35 validation O leg) | 44 lines matching `^  - ` in stdout (`run-validation.py:206` counts exactly that pattern), exit 0. (Ca02 §3 note: the selftest's prose header says "43 controls"; the filed 44 is the machine count the runner uses.) | match |
| 21 | 35 | `python3 reports/round-35/run-validation.py` | `acceptance_checks_passed: true`, `failures: []`, `missing_dependencies: []`, all four claims green | namespace-isolated clone@`ce103bf`, `--check` serial with `TMPDIR=.scratch`: **exit 0, `acceptance true`, `failures []`, `missing_dependencies []`, claims A/C/O/cross all `true`**; every leg measurement byte-identical to filed (A `surface_rows 15`; C `audits` + partition counts; O `quiet_sha 45f57132…`, `renderer_diff_lines 126`, `replay {exit 1, named true, names_member true, traceback false}`, `v3_controls 44`; cross `CO-godspeed` could-not-evaluate + `CO1-CO9`) | match |

## Named findings

**RC-1 (filed-byte drift, not mine).** `reports/round-35/validation.json` is dirty
against `HEAD` (`ce103bf`) at the time of this recount: `git diff HEAD` shows the
`X1-X3` measurement emptied (`{"manifest": "pending-by-construction: …"}` →
`{}`) and `measured_at_utc` moved `06:19:14.685566-03:00` →
`06:33:23.601283-03:00`; file mtime `2026-10-19 06:33:23`. My own r35 `--check`
runs wrote only under `.scratch` (`06:32:06` and later), and my r34 `--check` wrote
only under `.scratch` as well, so the 06:33:23 write is a separate actor's.
Recorded, not edited — the ruling on whether to restore or re-file belongs to the
integrator. `acceptance_checks_passed` is `true` in both versions. Independently
observed and identically attributed by `K03-recount-scout.md` §4,
`Ca01-recount-33-34.md` §5, `Ca02-recount-35.md` §5 and `Ca04-verify.md` §7;
`Ca04` §5 discloses a separate, self-repaired r34 clobber. Cause is `to-verify`
(no seat can prove identity); the mechanism is a publish-mode runner invocation
whose `os.chdir(ROOT)` targets the live tree.

**RC-2 (prose vs live count).** `SCORECARD.md:616` states "all 29 filed runners";
the live census is 30 (`ls reports/round-*/run-validation.py | wc -l`), because
`reports/round-35/run-validation.py` landed afterwards. The r34 filed figure is
correct *for r34*; the prose reads as present-tense and is now stale. Same cause
as row 13. Filed SCORECARD bytes are not edited here.

**RC-3 (r34 validation O leg).** The live `reports/round-34/validation.json` O leg
records `class_counts {guarded-refresh 18, unguarded-in-place 11}`, while its own
`failures` list is empty and `acceptance_checks_passed` is `true` — consistent
with an r34-time measurement. No drift; recorded so the 18-vs-19 question is not
re-opened per reading.

**RC-4 (carried from K03 §3.1, not absorbed).** r33's `A3` leg pins the lane-open
census as a literal (`2655`) and asserts equality with the live worktree, so after
admission the equality can never hold again — a self-invalidating gate. Its
`unexpected_paths: []` half (the real scope guard) still passes, and the growth is
fully accounted for (`+248 / −0` between `139e3b6` and `ce103bf`: round-33 +79,
round-34 +79, round-35 +78, `corpus/knowledge` +10, `REGIMEN.md` +1,
`tools/harness` +1). K03 files this as a candidate routed finding for the
integrator; this ledger records it and does not change any tool byte.

## Corrections filed against revision 1 (both from Ca04 §6.1)

1. **Census arithmetic (accepted).** Revision 1's `## Census` block and JSON
   declared `filed_entries: 20 / distinct_commands: 14 / by_round {34:{8,5}}`,
   contradicting its own 21-row table. Corrected to **21 rows / 17 distinct**,
   `by_round {33:{5,4}, 34:{9,6}, 35:{7,7}}`, with the convention difference
   against `claims.json` (20 entries / 15 distinct) now stated explicitly above.
2. **Row `RC-35-7` (accepted).** Was `pending` in revision 1; now observed (row 21)
   and dispositioned `match`.

Ca04 §6.1b also withdrew its own §3.2 "unreproducible by construction" verdict for
r33 `A3` in favour of my index-reconstruction method; recorded here for the record.

## Ledger JSON

```json
{
  "ledger": "kotodama-recount-ledger/1",
  "revision": 2,
  "round": 36,
  "claim": "Ca",
  "axis": "calibration",
  "seat": "Ca03",
  "date": "2026-10-19",
  "baseline_commit": "ce103bf",
  "observed_at_utc": "2026-10-19T09:35Z",
  "census": {"convention": "table_rows is the ledger table's row count; distinct_commands is the number of distinct shell commands",
             "table_rows": 21, "distinct_commands": 17,
             "note": "the `rows` array below carries one entry per distinct command, so its length equals `distinct_commands` (17), not `table_rows` (21). The two differ because r34's own runner is split into four leg-scope rows and because a handful of commands are filed by more than one claim.",
             "by_round": {"33": {"rows": 5, "distinct": 4},
                          "34": {"rows": 9, "distinct": 6},
                          "35": {"rows": 7, "distinct": 7}},
             "alternative_convention": {"source": "claims.json counting_commands (K03 §1)",
                                        "entries": 20, "distinct": 15,
                                        "by_round": {"33": {"entries": 5, "distinct": 4},
                                                     "34": {"entries": 8, "distinct": 5},
                                                     "35": {"entries": 7, "distinct": 5}}},
             "delta_cause": "r34's own runner is split by leg scope into 4 rows here vs 3 claims.json declarations; box1-survey.py counted once here"},
  "dispositions": {"match": 19, "dispositioned-mismatch": 1, "could-not-reproduce": 0,
                   "pending": 0, "reconstruction-artifact": 1},
  "isolation": {
    "in_tree_runner_executions": 0,
    "r33_method": "self-contained git clone @da68a6d, git reset --mixed 139e3b662900557afe54f632b468619593dc9fcb (declaration-time tree; index-tracked 2655 == filed baseline_paths), fleet inputs mirrored read-only beside the copy; runner derives ROOT from __file__ (run-validation.py:23)",
    "r34_r35_method": "unshare -rm --propagation private + bind-mount of a self-contained clone over the lane path; the runners hardcode absolute ROOT (r34:10, r35:9) and os.chdir(ROOT) (r34:26, r35:36); a --shared clone breaks git inside the namespace via objects/info/alternates",
    "tmpdir": ".scratch — /tmp is a tmpfs at 80% and redirected runs die with exit 120 (independently measured by Ca01 §1, K03)",
    "concurrency": "r35 O-legs require the sole v3-selftest consumer (Ca01 §4); the recorded r35 run was serial"
  },
  "rows": [
    {"id": "RC-33-1", "source_round": 33, "command": "python3 -B reports/round-25/audit/c31-lessons-index-audit.py", "filed": "exit 0; 33 files == 33 rows; 78 queue rows; formats {gate-keeper 21, fragment-index 5, plain 7}; findings 0", "observed": "exit 0; 33/33/78; same formats; findings 0", "disposition": "match", "evidence": "reports/round-33/validation.json claims.O.legs.O1; command output 2026-10-19"},
    {"id": "RC-33-2", "source_round": 33, "command": "python3 -B reports/round-25/audit/c31-lessons-index-audit.py --selftest", "filed": "SELFTEST OK: 28/28", "observed": "SELFTEST OK: 28/28 (exit 0)", "disposition": "match"},
    {"id": "RC-33-3", "source_round": 33, "command": "test -s reports/round-33/op/O05-falsifier-disposition.md", "filed": "disposition landed", "observed": "exit 0", "disposition": "match"},
    {"id": "RC-33-4", "source_round": 33, "command": "python3 reports/round-33/run-validation.py", "filed": "acceptance true; failures []; A/C/O/cross passed", "observed": "isolated reconstruction --check: exit 0; acceptance true; failures []; A/C/O/cross true", "disposition": "match", "snapshot": "clone @da68a6d reset --mixed 139e3b66"},
    {"id": "RC-34-1", "source_round": 34, "command": "python3 tools/gates/handoff-packet-check.py reports/round-34/handoff/declared-in-r7/packet.md", "filed": "16/16 fields; 20 glossary; findings 0", "observed": "INFO scan: fields=16/16 glossary-entries=20 findings=0; exit 0", "disposition": "match"},
    {"id": "RC-34-2", "source_round": 34, "command": "python3 tools/exercise-handoff-e2e.py --profile v3 --quiet", "filed": "exit 0; packet_sha256 45f57132…", "observed": "exit 0; packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19; links 105/105; claims 27", "disposition": "match"},
    {"id": "RC-34-3", "source_round": 34, "command": "python3 reports/round-34/run-validation.py", "filed": "acceptance true; failures []", "observed": "isolated: D/O/cross byte-identical to filed (45f57132…, tamper exit 1, 18/11, baseline_expanded da68a6d705…); C leg failed on C3 filed-row-edit detection", "disposition": "match (D/O/cross); dispositioned-mismatch (C)", "class": "reconstruction-artifact", "cause": "clone retained the round-34 SCORECARD.md edit; run-validation.py:258 greps git status -- corpus/lessons SCORECARD.md", "owner": "seat Ca03"},
    {"id": "RC-34-4", "source_round": 34, "command": "python3 tools/harness/receipt_guard_adoption.py --selftest", "filed": "selftest green (op/O02-tool-source.md:41: 38/38)", "observed": "selftest_passed true; controls 38/38; exit 0", "disposition": "match"},
    {"id": "RC-34-5", "source_round": 34, "command": "python3 tools/harness/receipt_guard_adoption.py --json", "filed": "class_counts {guarded-refresh 18, unguarded-in-place 11}", "observed": "class_counts {guarded-refresh 19, unguarded-in-place 11}; live_runner_count 30; findings 2; hazard_count 11; gaps 0; census_complete true", "disposition": "dispositioned-mismatch", "class": "environmental", "cause": "measurement instant: reports/round-35/run-validation.py landed after r34's census (git ls-tree da68a6d → 28 runners, +r34's own = 29 filed; ce103bf → 30); r34-time 18/11 reproduces in the r34 reconstruction and still reads 18/11 in the live r34 validation.json"},
    {"id": "RC-34-6", "source_round": 34, "command": "python3 -B reports/round-30/craft/box1-survey.py", "filed": "28 named / 28 resolvable at skill_sha256 f9bd07c2…", "observed": "named 28; resolvable 28; unnamed_in_skill []; skill_sha256 f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b; exit 0", "disposition": "match"},
    {"id": "RC-35-1", "source_round": 35, "command": "for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done", "filed": "21 / 23 / 24 / 29 / 20 / 94", "observed": "21 / 23 / 24 / 29 / 20 / 94", "disposition": "match"},
    {"id": "RC-35-2", "source_round": 35, "command": "python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge", "filed": "inventory_files 211", "observed": "totals.files 211; lines 38353; exit 0", "disposition": "match"},
    {"id": "RC-35-3", "source_round": 35, "command": "python3 -B reports/round-28/readme/sweep.py", "filed": "totals 211 totals_ok True; footer_ok True; readme_sha256 51b966af…", "observed": "totals_ok True; footer_findings []; footer_ok True; readme_sha256 51b966af20483328c3e221d2ab0f766aa5cf0f5a0b140650b95eb841d6bea6f0; exit 0", "disposition": "match"},
    {"id": "RC-35-4", "source_round": 35, "command": "python3 -B tools/exercise-handoff-e2e.py --selftest", "filed": "exit 0", "observed": "exit 0", "disposition": "match"},
    {"id": "RC-35-5", "source_round": 35, "command": "python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json", "filed": "exit 1; named; traceback false", "observed": "exit 1; E2E-READSET naming reports/round-20/handoff/claims-map.md", "disposition": "match"},
    {"id": "RC-35-6", "source_round": 35, "command": "python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest", "filed": "v3_controls 44", "observed": "44 lines matching '^  - '; exit 0", "disposition": "match"},
    {"id": "RC-35-7", "source_round": 35, "command": "python3 reports/round-35/run-validation.py", "filed": "acceptance true; failures []; missing_dependencies []", "observed": "namespace-isolated clone@ce103bf --check (serial, TMPDIR=.scratch): exit 0; acceptance true; failures []; missing_dependencies []; A/C/O/cross all true; every leg measurement byte-identical to filed", "disposition": "match", "snapshot": "self-contained clone @ce103bf bind-mounted over the lane path under unshare -rm"}
  ],
  "findings": [
    {"id": "RC-1", "kind": "filed-byte-drift", "artifact": "reports/round-35/validation.json", "detail": "dirty vs HEAD ce103bf: X1-X3 measurement emptied; measured_at_utc 06:19:14.685566-03:00 -> 06:33:23.601283-03:00; mtime 06:33:23", "attribution": "not this seat: my r35 --check wrote only under .scratch", "corroboration": "K03 §4, Ca01 §5, Ca02 §5, Ca04 §7 (independent, same attribution); Ca04 §5 discloses a separate self-repaired r34 clobber", "owner": "integrator", "status": "recorded-not-edited", "cause": "to-verify"},
    {"id": "RC-2", "kind": "prose-vs-live-count", "artifact": "SCORECARD.md:616", "detail": "prose 'all 29 filed runners' vs live 30 (reports/round-35/run-validation.py landed later)", "owner": "integrator", "status": "recorded-not-edited"},
    {"id": "RC-3", "kind": "reading-consistency", "artifact": "reports/round-34/validation.json", "detail": "O leg reads 18/11 with empty failures; r34-time measurement, reproduced in the r34 reconstruction", "status": "no-action"},
    {"id": "RC-4", "kind": "self-invalidating-gate", "artifact": "reports/round-33/run-validation.py:943-944", "detail": "A3 pins the lane-open census literal 2655 and asserts live equality; unreachable after admission. unexpected_paths [] still passes; +248/-0 growth fully accounted", "source": "K03-recount-scout.md §3.1 (routed, not absorbed)", "owner": "integrator", "status": "recorded-not-edited"}
  ],
  "limits": [
    "The r33 reconstruction cannot carry the cross (X1) leg without the fleet-root report; I mirrored the fleet report read-only beside the copy, and it is outside this seat's write scope.",
    "r34's C3 leg is not reproducible by construction in any clone that carries the round's own SCORECARD edit.",
    "r34/r35 counts are read from --check stdout, never from a published receipt.",
    "AgentSwarm/provider transport commands (telemetry observed-dispatch) are could-not-reproduce with owner orchestrator; they are counted by K03/Ca02/Ca04, not re-run here."
  ]
}
```

## Owed

- Nothing owed by this seat. Row `RC-35-7` (revision 1's only `pending`) is now
  observed and dispositioned `match`. The two corrections Ca04 filed against
  revision 1 are accepted and applied above.
- **Routed to the integrator (not this seat's write):**
  - Restore `reports/round-35/validation.json` to the filed
    `328e97b39eff69f45cb23801861ad2e345f8e7b3f7ae5555f1465e8d2c472124`
    (`git checkout -- reports/round-35/validation.json`) and file the
    F-C13-1-class incident record (RC-1). Byte-identical survivors exist at
    `git cat-file blob HEAD:reports/round-35/validation.json`, `.scratch/x01-clone/`,
    `.scratch/ca03/r35w/` and `.scratch/ca02/…`.
  - RC-4 (`A3` gate design) as a defects/SCORECARD finding.
  - The standing `git archive`-only isolation rule needs amending for
    hard-coded-`ROOT` runners (Ca04 §4, method disagreement 1).

## Citations

- `REGIMEN.md:25-43` — per-round contract (1–3 claims, per-axis verdicts, no scalar aggregation).
- `reports/round-36/claims.json:28-33` — claim Ca, its counting command and thresholds.
- `reports/round-36/targets.json:34` — seat Ca03's mission and `out` path.
- `reports/round-33/claims.json:32-37`, `reports/round-34/claims.json:31-51`, `reports/round-35/claims.json:30-51` — the filed counting commands.
- `reports/round-33/validation.json`, `reports/round-34/validation.json`, `reports/round-35/validation.json` — filed results quoted above.
- `SCORECARD.md:588-590` (r33), `:615-617` (r34), `:640-642` (r35) — filed before→after rows and their cited commands.
- `reports/round-21/recount/ledger.json` (63 rows), `reports/round-29/recount/ledger.json` (26 rows) — the prior recount ledgers and their row schema (`round, command, recorded, observed, verdict, cause/class`).
- `reports/round-34/run-validation.py:10,26,209,210,258`; `reports/round-35/run-validation.py:9,36,206`; `reports/round-33/run-validation.py:23,935,936,943-944` — the code paths that make the isolation method and the A3/`O2` legs behave as recorded.
- Sibling seat fragments read and reconciled: `reports/round-36/scout/K03-recount-scout.md` (§1 census, §3.1 A3, §3.2 O2, §3.3 manifest leaf, §4 incident, §6 command set), `reports/round-36/calib/Ca01-recount-33-34.md` (§1 `/tmp` exit 120, §3.2, §4 concurrency, §5 incident), `reports/round-36/calib/Ca02-recount-35.md` (§1 method, §2 r35 rows, §3 v3_controls prose note, §5 incident), `reports/round-36/calib/Ca04-verify.md` (§3.1, §6.1 corrections to revision 1, §6.1b self-correction, §7 incident).
- `AGENTS.md` (operating rules) — F-C13-1 no-in-tree-runner execution; append-only filed bytes.
- Command outputs of 2026-10-19 (in-tree legs) and the isolated `--check` runs, both recorded above; `df -h /tmp` → `16G 13G 3.1G 80%`.
