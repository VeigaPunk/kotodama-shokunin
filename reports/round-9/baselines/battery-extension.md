# R9-O15 — battery validates every committed `expected.json` (evidence fragment)

- worker seat: BASELINE R9-O15 (battery extension), round 9 claim O
- date: 2026-10-17; lane worktree at round-9 declare revision `a7bb205d3aecdaa24d91c047c8719cd8689e4ddd`
  (`git log --oneline -1`), baseline revision per claims `e1694bad6ac96aca45a11ca5746582b275929355`
- files written by this seat: `tools/check-gate-battery.py` (extension) and this fragment
- spec read first: `reports/round-9/claims.json`, `reports/round-9/targets.json`,
  `corpus/knowledge/verification/gate-frozen-run-standard.md` (§4 required fields, §6 verify
  table, §3 layout) — semantics below are that standard's, not invented here

## 1. What changed, and what provably did not

| item | before | after |
|---|---|---|
| `tools/check-gate-battery.py` | 488 lines, sha256 `077f68e488d56c633c98a0d95a24581389ed655b52e0fb553c3dec5f5ffe9b67` (`git show HEAD:tools/check-gate-battery.py \| sha256sum`, 2026-10-17T17:53-03:00) | 1117 lines, sha256 `0a126b70afa6cbd5c2565b57399c318788540e10c4940d07c906718c8b9e1aa1` (`sha256sum`, 2026-10-17T17:55-03:00; the earlier 17:53 revision `9ad0ef95…` differs only in the `BASELINE-GATE-UNCOVERED` detail text); `git diff --stat` = 648 insertions, 19 deletions |
| seven gate scripts | — | unchanged: `git status --porcelain tools/gates/*.py` prints nothing and `git hash-object <g>` equals `git rev-parse HEAD:<g>` for all seven (both commands, 2026-10-17T17:53-03:00; 0 of 7 differ) |
| battery selftest | 10 controls (round 5) | 28 controls, `SELFTEST OK 28/28`, exit 0 |
| battery report | `gates`, `findings`, `originals`, `summary`, `mirror` | same keys **plus** `baselines`; `summary` keeps exactly its four keys |

The `summary` shape is load-bearing for an existing consumer: `reports/round-5/run-validation.py:123`
asserts `data["summary"] == {"battery_exit": 0, "fail": 0, "pass": 7, "unevaluable": 0}` by exact
equality, so the baseline block went into a new top-level `baselines` key and `summary` was left
alone (values now reflect both duties: `battery_exit = max(gate_battery_exit, baseline_exit)`).

Additions in one line each: `BASELINE_*` constants; `combined_exit`; `gate_script_name` /
`implied_gate` / `expand_baseline_specs` / `normalize_inputs` / `find_expected_files`;
`verify_baseline_spec` (the checks); `inspect_baseline_file` / `inspect_baselines` (discovery +
report); `run_battery(..., baseline_roots=...)`; `--baselines-root PATH` (repeatable, for tamper
drills on a copy); 18 new selftest controls inside `run_selftest` on synthetic temp trees.

## 2. The contract implemented (gate-frozen-run-standard §4/§6)

Discovery: every file named `expected.json` or `*.expected.json` under the roots —
default `tools/gates/expected/` (the O-target's named root) **and** `tools/gates/frozen/`
(the standard's §3 root), recursively. Document shapes accepted: one baseline object, a
`baselines` / `gates` collection (list or map), or a top-level map keyed by gate name.
Input paths resolve inside the baseline directory first; absolute paths, `..` and paths that
only resolve in the live tree are refused. Each check contributes a finding, and the decisive
reading is the highest-priority one:

| finding id | condition | reading | exit contribution |
|---|---|---|---|
| `BASELINE-TAMPERED` | a declared input digest ≠ the snapshot bytes | `snapshot_tampered` | 2 |
| `BASELINE-GATE-REVISED` | `gate_sha256` ≠ the live gate script | `gate_revised` | 2 |
| `BASELINE-GATE-UNPINNED` | no `gate_sha256` | `gate_unpinned` | 2 |
| `BASELINE-UNPINNED` | `inputs` absent or empty (§4 legacy) | `unpinned (legacy)` | 2 |
| `BASELINE-PATH-ESCAPE` | input path leaves the baseline dir | `no baseline` | 2 |
| `BASELINE-EXTERNAL-INPUT` | input resolves outside the baseline | `no baseline` | 2 |
| `BASELINE-INPUT-MISSING` | pin names bytes that are not there | `no baseline` | 2 |
| `BASELINE-MALFORMED*` / `-UNREADABLE` | unparsable, non-UTF-8, bad digest shape | `no baseline` | 2 |
| `BASELINE-GATE-UNKNOWN` | gate outside the seven-name constant / no script | `no baseline` | 2 |
| `BASELINE-EXPECTED-ABSENT/-MALFORMED/-CLASS-MISMATCH/-FINDINGS-MALFORMED/-INCONSISTENT` | `expected` block missing or self-contradictory (exit∉{0,1}, class↔exit, clean-with-findings, exit-1-with-empty-set) | `no baseline` | 2 |
| `BASELINE-GATE-UNCOVERED` | one of the seven gates has no baseline under the roots | — | 2 |
| `BASELINE-ROOT-MISSING` / `BASELINE-NONE-FOUND` | no root is a directory / roots hold no `expected.json` | — | 2 |
| none | digests and pins hold | `pinned` | 0 |

Deliberate non-claims, stated so the reading cannot be laundered:

- **No gate is re-executed.** `pinned` means the pins hold, not that the verdict was compared.
  Every record carries `"verdict_replay": "not-run: ..."` and the corpus rule is
  `gate-frozen-run-standard.md` §6 row 3, exercised by the baseline's own re-run receipt
  (auditor seats R9-O18..O20). Sweep for the negative claim:
  `grep -n "subprocess\|os.system\|shell=True" tools/check-gate-battery.py` →
  3 hits (lines 86, 221, 229), all inside `run_child`, whose only callers are the gate-selftest
  loop and the selftest controls.
- **`stdout_sha256` is advisory only** (§4): verified against `run.log` when both exist, reported
  as `stdout_pin.reading = match|mismatch|run.log absent`, never a finding, never an exit change
  (control `CTRL-BASELINE-STDOUT-ADVISORY` holds exit 0 on a wrong pin).
- **The coverage rule is the measuring instrument for the round's "7/7"**: an uncovered gate is
  could-not-evaluate, per the standard's §8 fail-closed sentence ("a gate with a self-test but no
  committed baseline does not meet the two-evidences clause … not smoothed into green").
- The check writes nothing: no gate script, no fixture, no baseline, no repo path is opened for
  writing.

## 3. Controls — `python3 tools/check-gate-battery.py --selftest` (2026-10-17, exit 0)

```
control CTRL-PASS-EXIT0: exit=0 outcome=pass ids=-
control CTRL-RECOGNIZED-FAIL: exit=1 outcome=fail ids=GATE-SELFTEST-FAIL
control CTRL-FAIL-LINE-ID: exit=1 outcome=fail ids=GATE-SELFTEST-FAIL
control CTRL-EXIT1-UNRECOGNIZED: exit=1 outcome=unevaluable ids=GATE-CRASH-EXIT1
control CTRL-CRASH-EXIT1: exit=1 outcome=unevaluable ids=GATE-CRASH-EXIT1
control CTRL-MARKER-THEN-CRASH: exit=1 outcome=unevaluable ids=GATE-CRASH-EXIT1
control CTRL-MISSING-GATE: exit=None outcome=unevaluable ids=GATE-FILE-MISSING
control CTRL-TIMEOUT-GATE: exit=None outcome=unevaluable ids=GATE-TIMEOUT
control CTRL-BASELINE-PINNED: exit=0 outcome=pinned ids=-
control CTRL-BASELINE-TAMPERED: exit=2 outcome=snapshot_tampered ids=BASELINE-TAMPERED
control CTRL-BASELINE-UNPINNED: exit=2 outcome=unpinned (legacy) ids=BASELINE-UNPINNED
control CTRL-BASELINE-GATE-REVISED: exit=2 outcome=gate_revised ids=BASELINE-GATE-REVISED
control CTRL-BASELINE-GATE-UNPINNED: exit=2 outcome=gate_unpinned ids=BASELINE-GATE-UNPINNED
control CTRL-BASELINE-MALFORMED: exit=2 outcome=no baseline ids=BASELINE-GATE-UNCOVERED,BASELINE-MALFORMED
control CTRL-BASELINE-GATE-UNKNOWN: exit=2 outcome=no baseline ids=BASELINE-GATE-UNCOVERED,BASELINE-GATE-UNKNOWN
control CTRL-BASELINE-INPUT-MISSING: exit=2 outcome=no baseline ids=BASELINE-INPUT-MISSING
control CTRL-BASELINE-PATH-ESCAPE: exit=2 outcome=no baseline ids=BASELINE-PATH-ESCAPE
control CTRL-BASELINE-EXTERNAL-INPUT: exit=2 outcome=no baseline ids=BASELINE-EXTERNAL-INPUT
control CTRL-BASELINE-EXPECTED-ABSENT: exit=2 outcome=no baseline ids=BASELINE-EXPECTED-ABSENT
control CTRL-BASELINE-EXPECTED-INCONSISTENT: exit=2 outcome=no baseline ids=BASELINE-EXPECTED-INCONSISTENT
control CTRL-BASELINE-AGGREGATE: exit=0 outcome=pinned ids=-
control CTRL-BASELINE-STDOUT-ADVISORY: exit=0 outcome=pinned ids=-
control CTRL-BASELINE-UNCOVERED-GATE: exit=2 outcome=pinned ids=BASELINE-GATE-UNCOVERED
control CTRL-BASELINE-NONE-FOUND: exit=2 outcome=- ids=BASELINE-GATE-UNCOVERED,BASELINE-NONE-FOUND
control CTRL-BASELINE-ROOT-MISSING: exit=2 outcome=- ids=BASELINE-GATE-UNCOVERED,BASELINE-ROOT-MISSING
control CTRL-COMBINED-EXIT: exit=2 outcome=- ids=-
control CTRL-TREE-DIFF: exit=0 outcome=- ids=-
control CTRL-STABLE-IDS: exit=0 outcome=- ids=-
SELFTEST OK 28/28 controls behaved as expected
```

Four notes on controls that close holes a weaker check would leave:

- `CTRL-BASELINE-PATH-ESCAPE` plants `../escape.txt` **with its real digest** outside the
  baseline: a digest-only check that followed the path would read `pinned`; the control observes
  `BASELINE-PATH-ESCAPE`, reading `no baseline`, and asserts
  `baselines[0].inputs_checked == 0` (nothing outside was hashed).
- `CTRL-BASELINE-EXTERNAL-INPUT` plants a file in the gates root with a correct digest: it is
  still refused (§3 requires a copy inside the baseline).
- `CTRL-BASELINE-TAMPERED` appends one byte to the snapshot and observes `snapshot_tampered`
  with exit 2 — the measured reason the digest step is load-bearing.
- The two controls with an extra `BASELINE-GATE-UNCOVERED` id are correct, not noise: a baseline
  that cannot be read or resolved covers no gate, so the coverage rule fires beside it.

## 4. Live measurement over the wave's committed baselines (2026-10-17T17:53-03:00)

Command: `python3 tools/check-gate-battery.py` (exit 2 at measurement time).

- gate duty: `{"battery_exit": 2, "fail": 0, "pass": 7, "unevaluable": 0}` — 7/7 gate selftests
  pass in the mirror; `originals: {"modified": 0, "added": 0, "deleted": 0, "preserved": true}`
  over 28 hashed files; mirror removed.
- baseline duty: `baselines_found: 5`, `pinned: 5`, `unevaluable: 0`,
  `gates_uncovered: ["myth-consistency-gate.py", "naming-collision-gate.py"]`.
- `find tools/gates/expected tools/gates/frozen -name 'expected.json' | sort` → 5 files at the
  same timestamp: 2 under `tools/gates/expected/` (costume-era, phonology), 3 under
  `tools/gates/frozen/` (handoff, lexicon, provenance). **Finding for R9-O17 / integrator:** the
  wave's baselines landed under two roots; a discovery that read only the O-target's named
  `tools/gates/expected/` would have missed 3 of 5, which is why both roots are defaulted.

| baseline | gate | reading | inputs checked | gate pin | stdout pin |
|---|---|---|---|---|---|
| `expected/costume-era-consistency-gate/r9-pre/expected.json` | costume-era | `pinned` | 1 | match | match |
| `expected/phonology-sanity-gate/r9-pre/expected.json` | phonology | `pinned` | 1 | match | match |
| `frozen/handoff-packet-check/r9-pre/expected.json` | handoff | `pinned` | 1 | match | match |
| `frozen/lexicon-coverage-audit/r9-pre/expected.json` | lexicon | `pinned` | 1 | match | match |
| `frozen/provenance-audit/r9-pre/expected.json` | provenance | `pinned` | 20 | match | match |

`BASELINE-GATE-UNCOVERED` for the two gates without a baseline is what makes the exit 2 here: the
battery is refusing to call the two-evidences obligation met while 5 of 7 gates are pinned. When
the last two land under these roots, the same command must read exit 0 — the re-measurement is the
round's check.

### 4.1 Root divergence: the round's third root, measured not absorbed (2026-10-17T17:54:31-03:00)

`find . -name 'expected.json' -not -path './.git/*' -not -path './reports/supplement*' -not -path './.scratch*'`
at that time found 8 baseline files under three roots: 2 in `tools/gates/expected/`, 3 in
`tools/gates/frozen/`, and 3 in the round's fragment root `reports/round-9/baselines/` (handoff —
a second copy of the frozen one — plus myth and naming). Declaring the third root for one run:

```sh
python3 tools/check-gate-battery.py \
  --baselines-root tools/gates/expected \
  --baselines-root tools/gates/frozen \
  --baselines-root reports/round-9/baselines
```

→ **exit 0**; `baselines_found: 8`, `pinned: 8`, `unevaluable: 0`, `readings: {"pinned": 8}`,
`gates_covered:` all seven, `gates_uncovered: []`. Every committed baseline of this round verifies
— input digests, gate pins and advisory stdout pins included; nothing was pinned-but-tampered.
Per baseline: costume-era 1 input, phonology 1, handoff 1 (frozen) and 1 (fragment copy),
lexicon 1, provenance 20, myth 1, naming 1.

**Why this is a measurement and not a default.** The default root list is the two durable repo
homes (`tools/gates/expected/`, the O-target's named root, and `tools/gates/frozen/`, the standard
§3 root). `reports/round-9/baselines/` is round-scoped evidence space — the O-targets themselves
designate it for *fragments* — so baking it into the tool's defaults would both endorse a contested
convention (`reports/round-9/baselines/registry.md` §5 item 1: "decision needed from the
orchestrator/integrator") and couple a durable tool to one round's directory. The tool therefore
declares its roots in one constant, prints them in every report (`baselines.roots`), and accepts
`--baselines-root` (repeatable) so the orchestrator can point a run at whichever root list they
ratify. Two reconciliations make the default command green: relocate the two fragment-root
baselines into `tools/gates/frozen/<gate>/r9-pre/` (standard §3 shape, zero flags), or ratify the
fragment root and record the three-root invocation as the round's entry command. The `handoff`
baseline exists in both roots; both copies verify `pinned` at this timestamp, and the battery
counts both (no de-duplication rule exists — §8).

## 5. Tamper-rejection drill on a copied tree (`--baselines-root`)

Commands (2026-10-17T17:52-03:00, all inside `/home/vgpnk/.cache/r9o15`, no repo path written):

```sh
cp -a tools/gates/expected $W/drill/expected && cp -a tools/gates/frozen $W/drill/frozen
python3 tools/check-gate-battery.py --baselines-root $W/drill/expected --baselines-root $W/drill/frozen
printf '\n# tampered byte\n' >> $W/drill/expected/costume-era-consistency-gate/r9-pre/packet.yml
python3 tools/check-gate-battery.py --baselines-root $W/drill/expected --baselines-root $W/drill/frozen
```

| step | exit | readings | non-coverage findings |
|---|---|---|---|
| clean copy | 2 | `{"pinned": 4}` | none (2 uncovered gates only) |
| same copy, one byte appended to one snapshot | 2 | `{"pinned": 3, "snapshot_tampered": 1}` | `BASELINE-TAMPERED` on `expected/costume-era-consistency-gate/r9-pre/expected.json` |

The three untampered baselines stayed `pinned` in the same run, so the flip is attributable to the
edited byte and not to the copy; the live committed baseline was never opened for writing and a
subsequent live run still reads it `pinned` (§4). Absent-root negative:
`--baselines-root $W/does-not-exist` → exit 2, `BASELINE-ROOT-MISSING`, `baselines_found: 0`.

## 6. Read-only proof and CLI negatives (2026-10-17T17:53-03:00)

- Isolated copy hashed before/after a full check:
  `find $W/ro -type f -exec sha256sum {} + | sort` → 72 files, `diff` clean → the check wrote
  nothing, not even into the tree it inspected.
- `python3 tools/check-gate-battery.py --timeout 0` → exit 2, `argument --timeout: timeout must be
  a positive finite number of seconds, got '0'` (unchanged behaviour); `--timeout nan` → exit 2.
- `--selftest` ignores `--baselines-root` by design (controls use their own temp trees) and still
  reads `SELFTEST OK 28/28`, exit 0.

## 7. Handoff notes (not absorbed here)

- **R9-O16 (`run-validation.py`)**: the battery's gate verdict is still `summary.battery_exit`;
  baseline detail is under `.baselines.summary` (`baselines_found`, `pinned`, `unevaluable`,
  `readings`, `gates_covered`, `gates_uncovered`, `baseline_exit`). Measuring claim O needs the
  root decision made first: with the three declared roots of §4.1 the run is exit 0 with 8/8
  pinned and 7/7 covered; with the two durable roots alone it is exit 2 with 5/8 seen and two
  gates uncovered. Either way, one command measures both duties — do not compare the battery's
  exit against the O claim without stating which root list it was run with.
- **R9-O17 (registry scribe)**: the battery row in `SKILL.md` §Gates still describes selftest
  isolation only; it now also validates the baselines, declares two default roots, prints them in
  `baselines.roots`, and accepts repeatable `--baselines-root`. `reports/round-9/baselines/registry.md`
  §5 items 1 and 6 (three roots in flight, no committed discovery convention) are answered in
  this fragment's §4.1: a declared root list exists, it is printed in every report, and it is
  overridable per run — what remains is the orchestrator ratifying a root, which this seat does not
  decide. Also note the registry row's pre-extension sha256 (`6fff02df…`) is superseded by
  `0a126b70…`.
- **R9-O18..O20 (auditors)**: `--baselines-root <copy>` is the intended tamper-drill path; the
  decisive readings to expect are `snapshot_tampered` (edited snapshot), `gate_revised` (edited
  gate script), `unpinned (legacy)` (empty `inputs`), `BASELINE-GATE-UNCOVERED` (a gate missing
  from the declared roots).
- **Cross-round consumer**: `reports/round-5/run-validation.py:123` re-runs this tool and asserts
  the four-key `summary` equals `{"battery_exit": 0, "fail": 0, "pass": 7, "unevaluable": 0}`. That
  assertion is now also a statement about coverage: it holds exactly when all seven gates carry a
  baseline within the roots the run declared. If round 9 closes with the baselines still outside
  the default roots, round-5's re-run will report a failure that is the honest reading of the
  placement question, not a regression — the integrator should say which.
- `reports/round-8/run-validation.py` compares a recorded `--selftest` stdout hash against the live
  run but tolerates drift when the tool bytes changed (`tool-repaired-after-receipt`), which is the
  branch this extension takes; the record also requires the *recorded* exit codes to be zero, which
  they are (historical receipt, untouched).

## 8. Limits and `to-verify`

- The battery does not check the `revision` field against git, does not compare `expected.findings`
  order (correctly: §4 compares sets), and does not judge snapshot quality — a `pinned` baseline
  says "these bytes, this gate revision", nothing about the culture packet being good design.
- Duplicate baselines for one gate across roots (measured: `handoff-packet-check` in both
  `tools/gates/frozen/` and `reports/round-9/baselines/`) are both validated and both counted; no
  de-duplication or single-root rule exists (`to-verify` for the orchestrator's root decision).
- The `*.expected.json` discovery pattern is accepted but no such file exists in this round
  (count 0 of 8 discovered at §4.1's timestamp) — the branch is covered by controls, not by a live
  example.
- The coverage rule is a policy choice this seat made explicit above; if the orchestrator wants
  uncovered gates to be a warning instead of could-not-evaluate, that is a claim-level decision and
  needs the report to say so — the tool will keep refusing until told otherwise.
- Coverage at fragment-writing time is a moving target (concurrent wave); the authoritative number
  is a re-run of §4/§4.1, not this text. `to-verify` for whoever re-measures.

## 9. Repro

```sh
python3 tools/check-gate-battery.py --selftest   # 28/28, exit 0
python3 tools/check-gate-battery.py              # gate battery + baselines, exit 0 at 7/7 pinned
python3 tools/check-gate-battery.py --timeout 0  # usage error, exit 2
```
