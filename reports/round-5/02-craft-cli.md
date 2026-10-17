# 02 EXECUTOR craft CLI — round 5 worker fragment

Worker: 02 EXECUTOR craft CLI. Owned files only: `tools/check-craft-exercise.py` (this
fragment's subject) and this report. Baseline 1ccb2b7119039d8026ad1d004f20427623838b94;
changes sit in the working tree — workers do not commit, the parent commits under the lane
identity and owns the hash citation.

## Work performed

Normalized the six observed malformed-input crash paths of the craft-exercise checker from
exit 1 + traceback to exit 2 with stable diagnostic IDs, and extended `--selftest` with real
subprocess CLI positive/negative cases. No exercise JSON, existing report, gate, fixture, or
historical byte touched (`git status` shows only `tools/check-craft-exercise.py` as this
worker's modification).

## Landed changes (working tree, awaiting parent commit)

- `main` now parses arguments explicitly (`parse_args`) and loads files through
  `read_json_file` / `read_report_text`; a `CliError` prints
  `CLI-ERROR <ID>: <message>` to stderr and returns exit 2. Only narrow
  `OSError` / `UnicodeDecodeError` / `json.JSONDecodeError` handlers exist, each immediately
  converted to a specific diagnostic; `run_checks` internals stay unguarded so real defects
  still traceback visibly.
- Stable IDs (all exit 2): `CRAFT-CLI-USAGE` (missing/extra/unknown argument),
  `CRAFT-CLI-NOT-FOUND` (unreadable exercise), `CRAFT-CLI-UTF8` (non-UTF-8 exercise),
  `CRAFT-CLI-JSON` (malformed JSON), `CRAFT-CLI-SHAPE` (non-object root),
  `CRAFT-CLI-REPORT-VALUE` (`--report` without value), `CRAFT-CLI-REPORT-OPEN`,
  `CRAFT-CLI-REPORT-UTF8`.
- `--selftest` keeps the ten in-process tamper detections and now also runs
  `run_cli_selftest`: 11 real subprocess cases over fixtures in an isolated
  `tempfile.mkdtemp` (removed afterwards) — positive run, `--counts`, `--report` on the
  existing report `reports/supplement-opencode-1/32-craft-exercise.md` (read-only), a run
  from a foreign cwd, the six malformed exit-2 controls, and an exit-1 genuine-finding
  fixture (tampered copy without `negative_control`); each exit-2 case asserts its ID and
  that no `Traceback` leaks. Selftest output: `SELFTEST OK 10/10 tamper cases detected` +
  `CLI-SELFTEST OK 11/11 cases passed`.
- `--selftest` default exercise path resolves cwd-first, then repo root via the script
  location, so the selftest runs from any cwd. Law engine, ten tamper cases, findings exit 1,
  positive-run output line, and `--counts` JSON are byte-identical in behavior.

## Before → after (observed)

| Control | Baseline | After |
| --- | --- | --- |
| missing argument | exit 1, IndexError traceback | exit 2, `CRAFT-CLI-USAGE` |
| missing file | exit 1, FileNotFoundError traceback | exit 2, `CRAFT-CLI-NOT-FOUND` |
| malformed JSON | exit 1, JSONDecodeError traceback | exit 2, `CRAFT-CLI-JSON` |
| non-UTF-8 | exit 1, UnicodeDecodeError traceback | exit 2, `CRAFT-CLI-UTF8` |
| wrong root shape (array) | exit 1, AttributeError traceback | exit 2, `CRAFT-CLI-SHAPE` |
| missing `--report` value | exit 1, IndexError traceback | exit 2, `CRAFT-CLI-REPORT-VALUE` |

Preserved: genuine findings exit 1 (`FAIL <ID>: ...` + count), clean run exit 0
(`OK all checks passed (audits=7, mech_cases=11, derivations=9, approx_checks_runner=37)`),
`--counts` exit 0 JSON, read-only optional `--report` on the existing report exit 0,
`SELFTEST OK 10/10`.

## Actual tests run (repo root unless noted; all exits as shown)

- `python3 tools/check-craft-exercise.py examples/supplement-opencode-1/sound-change-vs-taboo.json` → exit 0
- same + `--counts` → exit 0; + `--report reports/supplement-opencode-1/32-craft-exercise.md` → exit 0
- `python3 tools/check-craft-exercise.py --selftest` → exit 0 (10/10 + 11/11)
- six malformed controls, one invocation each → exit 2, expected `CRAFT-CLI-*` ID in stderr, `Traceback` count 0
- tampered copy (popped `negative_control`) via subprocess → exit 1, `FAIL CONTROL-MISSING: D1 lacks negative_control`, no traceback
- from `/tmp/cwd5`: `--selftest` → exit 0; absolute exercise path → exit 0; cwd-relative nonexistent path → exit 2 `CRAFT-CLI-NOT-FOUND`
- `python3 -m py_compile tools/check-craft-exercise.py` → OK

## Limits

- The `--counts`/`--report` acceptance and the seven-gate battery lives with other workers
  (`tools/check-gate-battery.py` did not exist at my run time); I verified only my owned tool.
- Round-3 frozen manifest replay is parent-level; unchanged checker output above is my
  evidence of non-interference, not a replay.
- `--report` value is consumed as-is (a token like `--counts` after `--report` yields
  `CRAFT-CLI-REPORT-OPEN` exit 2 rather than baseline's traceback); repeated `--report`
  takes the last value.
- Exit-1-preservation at CLI level is proven by one tampered fixture case, not by mutating
  the real exercise.

## Post-review repair (P2/P5/P6) — appended after reports/round-5/15-cli-review.md

Work performed, same ownership (`tools/check-craft-exercise.py` only; diff +318/−29 vs
baseline includes the round-1 work above; original observed history above is unchanged):

- P2 — boundary shape validation: new `validate_shape(doc)` runs in `main` (after load,
  before any check) and in `run_selftest` (before the battery). It rejects, with exit 2
  `CRAFT-CLI-SHAPE`, exactly the shapes a `run_checks` dereference would crash on:
  wrong-typed `exercise` / `audits` / `audit_counts` / `derivations` / `law_list` /
  `law_list.order` / `mech_expectations(.cases)` / `name_avoidance(.distribution_test →
  .public_roll_year_340)` / `borrowed_garment_terms(.terms)` / `symbol_readings(.readings)`
  containers and their row objects, plus the string-typed fields the checker calls string
  or key operations on (`source_excerpt`, `basis`, `stratum`, `constraint`, `motif`,
  `term`/`reading`/`audience`, law-order entries, mech-case word keys) and the three
  `audit_counts` verdict keys that feed arithmetic. Chosen contract: string/number-typed
  fields are required to be exactly that type, so wrong-typed leaves are boundary rejections
  (exit 2), not findings; missing keys and wrong domain values (verdicts, counts, strata
  content) remain exit-1 findings. `run_checks`, the law engine, and the ten tamper cases
  are semantically untouched.
- P5 — `--report --counts`: `parse_args` now rejects any `--report` value beginning with
  `-` as a missing value → exit 2 `CRAFT-CLI-REPORT-VALUE` (previously it consumed the
  flag as a filename and failed with `CRAFT-CLI-REPORT-OPEN`). Documented contract: option
  values must not begin with `-`.
- P6 — `--selftest` strict contract: it accepts at most one optional exercise path
  positioned after `--selftest` and no other tokens; a positional before `--selftest`, a
  second positional, or any flag → exit 2 `CRAFT-CLI-USAGE` (previously a leading
  positional was silently adopted as the target and other tokens were silently discarded).
  The explicit custom target stays supported: it is loaded, `validate_shape`d, and checked
  by new `require_selftest_target`, which verifies the fixed slots the ten-tamper battery
  indexes (audits[0], audit_counts, derivations[0].negative_control,
  mech_expectations.cases[0].cases, symbol_readings.readings, exercise.era_staging,
  borrowed_garment_terms.terms[4], name_avoidance roll chain) and exits 2 `CRAFT-CLI-SHAPE`
  with a named missing slot instead of KeyError/IndexError deep in the battery.
- CLI battery grew 11 → 18 real subprocess cases: the two confirmed P2 counterexamples
  (`{"audits":[3]}`, `{"audits":{"x":1}}`), plus `{"exercise":[1]}`, `report-flag-value`,
  `selftest-conflicting-mode`, `selftest-positional-before`, and `selftest-thin-target`
  (custom target lacking battery slots → exit 2 `CRAFT-CLI-SHAPE`), each asserting exit
  code, stable ID, and no `Traceback` leak.

Defects found in my own first repair attempt and fixed (recorded honestly; both were
selftest-harness bugs, not checker-semantics changes):

- The `selftest-custom-target` CLI case pointed `--selftest` at the real exercise, whose
  battery re-ran the same case — unbounded subprocess recursion (one 60s+ hang observed,
  killed via task stop; `pgrep` afterwards found no survivors). Replaced by the bounded
  `selftest-thin-target` exit-2 case; the custom-target success form is verified once
  manually below, not inside the battery, so the battery cannot recurse.
- The strict-parse `raise CliError` sat outside `run_selftest`'s try/except → traceback
  exit 1 on exactly the ambiguity cases it was meant to reject; moved inside the try.
- `validate_shape`/`require_selftest_target` indexed `doc["exercise"]` directly, crashing
  with KeyError on a doc lacking the key (caught by the battery's own
  `selftest-thin-target` case before any external run); now `doc.get("exercise", {})`.

Actual tests run (all observed this session):

- `python3 tools/check-craft-exercise.py --selftest` → exit 0,
  `SELFTEST OK 10/10 tamper cases detected` + `CLI-SELFTEST OK 18/18 cases passed` (~0.42 s);
  also exit 0 from `/tmp/rep5b` and with `--selftest <abs path to real exercise>` (explicit
  custom target success form).
- From foreign cwd `/tmp/rep5b`: `{"audits":[3]}` / `{"audits":{"x":1}}` /
  `{"exercise":[1]}` / `{"audit_counts":"x"}` → each exit 2, `CRAFT-CLI-SHAPE`, 0
  tracebacks. `--report --counts` → exit 2 `CRAFT-CLI-REPORT-VALUE`. `<exercise> --selftest`
  → exit 2 `CRAFT-CLI-USAGE`. `--selftest <exercise> --counts` → exit 2 `CRAFT-CLI-USAGE`.
- Regression: original six malformed controls (no argument, missing file, malformed JSON,
  non-UTF-8, array root, missing `--report` value) → all exit 2; positive run, `--counts`,
  `--report` on the existing report → exit 0; tampered-copy finding → exit 1
  (inside the battery); `python3 -m py_compile` → OK.
- `git status` for this worker: only `tools/check-craft-exercise.py` modified and
  `reports/round-5/02-craft-cli.md` added; exercise JSON, gates, fixtures, sources,
  shared bookkeeping untouched; no commits made.

Limits:

- Boundary typing is contract-by-documentation: wrong-typed leaves (e.g. an integer
  `stratum`) exit 2 as malformed shape rather than degrading into findings; only wrong
  domain values stay findings. Reviewers wanting finding-level degradation would need a
  semantic change to `run_checks`, which was out of scope.
- The battery proves the custom-target *rejection* path (`selftest-thin-target`) but not
  the custom-target success path, to keep it non-recursive; the success form was verified
  manually once. Any future battery case that passes `--selftest` a full exercise will
  recurse again — do not add one.
- Degenerate-but-valid custom targets other than the eight named slots are not
  precondition-checked beyond `validate_shape`.
- Still parent-level: gate battery, frozen manifest replays, validation runs; my
  non-interference evidence is the unchanged positive/counts/report/selftest outputs.
