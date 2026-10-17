# 15 — Mutation review: craft checker CLI and isolated-battery approach (round 5)

Reviewer: worker 15 (MUTATION REVIEWER CLI). Baseline pinned to `1ccb2b7119039d8026ad1d004f20427623838b94`.
Method: counterexamples were re-run against baseline bytes extracted to
`reports/supplement-opencode-1/scratch/round5-15/baseline-check-craft-exercise.py`
(`git show HEAD:tools/check-craft-exercise.py`) after the live working-tree copy mutated
mid-review (see "In-flight mutation window"). All probes are bounded to
`reports/supplement-opencode-1/scratch/round5-15/`; no worker code edited, no live fixture
or source mutation, no writes outside my owned files and scratch.

## Work performed

- Read baseline `tools/check-craft-exercise.py` in full (375 lines) and ran baseline positive
  controls: `--selftest` → `SELFTEST OK 10/10 tamper cases detected` exit 0; positive exercise
  check → `OK all checks passed (audits=7, mech_cases=11, derivations=9)` exit 0; `--counts` exit 0.
- Ran 8 baseline-pinned counterexamples (B1–B8) plus live-tree probes P1–P15 covering malformed
  input, option confusion, exit semantics, and gate selftest write behavior.
- Grepped the seven gate scripts for filesystem writes and located each selftest's write targets.
- Checked executor availability at start and end of review.

## Findings

### F1. Malformed input: all six controls crash with exit 1 + raw traceback (baseline)

Every malformed control from the claim-O list was reproduced against pinned baseline bytes; each
ends in an uncaught exception, Python default exit 1, full traceback:

| Probe | Input | Terminal exception | Exit |
|---|---|---|---|
| B1 | no argument | `IndexError: list index out of range` (`path = argv[1]`, check-craft-exercise.py:341) | 1 |
| B2 | missing file | `FileNotFoundError` (:342) | 1 |
| B3 | malformed JSON | `json.decoder.JSONDecodeError` (:343) | 1 |
| B4 | non-UTF-8 | `UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff` | 1 |
| B5 | wrong root shape (`[]` / `"s"` / `null`) | `AttributeError: 'list'/'str'/'NoneType' object has no attribute 'get'` (:112) | 1 |
| B6 | missing `--report` value | `IndexError` (:346) | 1 |

Claim O's requirement (all six exit 2 with stable diagnostics, no traceback) is therefore a real
gap at baseline, not a paper one. Verified empirically, not assumed.

### F2. Exit semantics: crash exit 1 is indistinguishable from genuine-findings exit 1

The tool's documented contract is "exits 0 on clean, 1 on findings" (:7). B1–B6 all exit 1 via
uncaught exception, so a consumer keying on exit code alone cannot tell "audit finding" from
"checker crashed before looking". This is the core misleading-exit-semantics defect the claim-O
exit-2 contract fixes.

### F3. Option confusion: positional parsing, flags matched anywhere in argv

- `--report` before the path: `path = argv[1]` becomes `--report` → `FileNotFoundError: '--report'` exit 1 (P7).
- `--report --counts`: `--counts` is consumed as the report filename → `FileNotFoundError: '--counts'` exit 1 (P6b).
- Intended counts mode without a path: same `FileNotFoundError: '--counts'`, not a usage message (P8/B-class).
- `--selftest` anywhere in argv switches mode and the positional path is silently ignored:
  baseline `baseline-check-craft-exercise.py <malformed.json> --selftest` prints
  `SELFTEST OK 10/10` exit 0 — the named malformed target is never opened (B8). Silent success
  while the requested file went unchecked is the worst exit-semantics case found.

### F4. LAW-ORDER early return silently skips most checks

`run_checks` returns early at check-craft-exercise.py:171 when `law_list.order` is malformed,
skipping name-avoidance, register-partition, loan-strata, symbol-readings, universal-phrase,
sacred-term, canon-hygiene, method-trace and report-heading checks without disclosure. Probe:
a fixture carrying BOTH a broken law order AND the banned phrase "always means" (plus a bad
verdict) reports only 3 findings, no `UNIVERSAL-PHRASE`; the identical phrase tamper with intact
law order is detected. Same exit 1 both ways — coverage loss is invisible in the exit code and
the output never says checks were skipped.

### F5. `--counts` success output is the declared counts echoed, not measured counts

`--counts` prints `json.dumps(counts)` where `counts = doc.get("audit_counts", {})` (:141, :352) —
verified programmatically: printed JSON == the document's own `audit_counts` block, exit 0. A
reader can mistake echoed declared counts for a measurement; measured values surface only inside
`AUDIT-COUNT-MISMATCH` finding text when they disagree.

### F6. CWD-relative default path

`--selftest`'s default exercise path (:330) is CWD-relative: running the tool from any directory
other than the repo root crashes with `FileNotFoundError` exit 1 (P11), again colliding with the
findings exit code.

### F7. Live writes: craft checker is read-only; five legacy gate selftests are not

`check-craft-exercise.py` performs no filesystem writes (only reads at :331, :342, :346-347).
By contrast, gate selftests rewrite fixture/expected files inside the live tree:
`costume-era-consistency-gate.py:140-143,1454-1457`, `lexicon-coverage-audit.py:125-126,1402-1403`,
`myth-consistency-gate.py:100,1038-1041`, `phonology-sanity-gate.py:116-117,1222-1225`,
`provenance-audit.py:405,408,413` (root-relative fixture dir); `handoff-packet-check.py` already
uses `tempfile.TemporaryDirectory` (:113,:829-831). This empirically supports the claim-O premise
that a wrapper alone cannot make the legacy selftests read-only and that copied-tree isolation is
the right isolation mechanism.

## Isolated-battery executor: unreviewed (not landed)

`tools/check-gate-battery.py` was **absent** at review start (13:29) and present but **untracked**
at review end; `git status` shows `?? tools/check-gate-battery.py` and ` M tools/check-craft-exercise.py`.
"Landed means committed" (round contract), so executor output is **unreviewed** at this time.
Read-only inspection of the in-flight bytes (approach-level only, no verdicts): mirror via
`tempfile.mkdtemp(prefix="gate-battery-")` + `shutil.copytree` of the fixture tree, hash
before/after of original gate/fixture bytes, documented 0/1/2 exit contract (1 = genuine
selftest failure, 2 = could-not-evaluate), child launch as `[sys.executable, path, "--selftest"]`
with `shell=False`, argparse-based options. No execution of the battery was attempted (racing a
mid-write worker file would produce unverifiable evidence).

## In-flight mutation window (observation, not a finding)

The live `tools/check-craft-exercise.py` changed during this review: positive `--selftest` banner
moved from `SELFTEST OK 10/10 tamper cases detected` (P0, baseline behavior) to
`CLI-SELFTEST OK 11/11 cases passed` (P12) between probes, consistent with a round worker editing
the shared tree pre-commit. All findings above are anchored to pinned baseline bytes (B-series) or
baseline-code reading, so they stand regardless of what the worker commits. The parent's
acceptance run should judge committed bytes; these probes can be re-run verbatim from
`reports/supplement-opencode-1/scratch/round5-15/`.

## Verdict summary (author-side evidence; parent judges axes)

- Malformed input handling at baseline: fails all six controls (F1) — the claim-O exit-2 target is justified and previously measured correctly.
- Accidental live writes: craft checker clean; battery isolation approach motivated by confirmed live-writing selftests (F7).
- Option confusion: present in five distinct forms (F3), worst case silent success (B8).
- Misleading exit semantics: crash/findings collision (F2), undisclosed check-skip (F4), declared-counts echo (F5), CWD crash (F6).
- Landed executor output: unreviewed — absent at review start, uncommitted at review end.

## Limits

- Baseline checker bytes only; the worker's in-flight checker/battery edits are out of my scope and were not reviewed or judged.
- `replay-frozen.py` and the D2 assembler were not reviewed (outside assignment).
- Provenance-audit's fixture-root anchoring was not chased to its definition; the battery's hash-before/after design covers it.
- Probes and fixtures (including tampered payloads) persist only under `reports/supplement-opencode-1/scratch/round5-15/`.
- This fragment is author-side review evidence; it is not independent promotion verification and makes no canon or round-admission judgment.

---

# Actual-output review of the completed diff (post-worker review, same worker 15)

Reviewed the delivered bytes of `tools/check-craft-exercise.py` (M, +197/−29 vs baseline) and
`tools/check-gate-battery.py` (new, 322 lines) as they stood at review end, still uncommitted in
the working tree against baseline 1ccb2b71. `run_checks`/`tamper_tests` are byte-unchanged (diff
deletions touch only the old CLI shell), so all baseline findings above remain historical and
unchanged. Craft probes N1–N16 ran against the delivered live bytes (read-only invocations);
battery probes R1–R11 ran ONLY against a sandbox copy under
`reports/supplement-opencode-1/scratch/round5-15/bat/` with fake gates using the real gate
filenames — the full battery was never run on live gates (parent owns acceptance), and no live
gate or fixture byte changed (verified: `git diff --name-only -- tools/gates/` empty, zero
`gate-battery-*`/`craft-cli-selftest-*` dirs left in /tmp).

## Confirmed new bugs (severity-ranked)

### P1 — HIGH: battery maps a crashed selftest to "genuine finding" exit 1
The docstring promises exit 2 for "abnormal child death" (check-gate-battery.py:14-15), but
`classify_exit` (:72-77) and `run_child` (:139-146) key solely on the process exit code: any
exit 1 becomes outcome `fail` + `GATE-SELFTEST-FAIL` and `battery_exit` (:80-88) returns 1,
which consumers must read as "a genuine finding" (:13). A gate selftest that dies with an
uncaught Python exception also exits 1 — normally, with no stable finding IDs — and is
misclassified. `STABLE_ID_RE` (:50) exists but is applied only in `run_selftest`, never in
`run_battery` to qualify a `fail` outcome. Exact repro (sandbox, R1):
fake `myth-consistency-gate.py` = `raise NameError("boom")\n`, six fake pass gates, battery copy
run with default timeout → child `observed_exit: 1`, `stderr_head` = raw `NameError` traceback,
summary `fail: 1`, **battery_exit = 1**, finding `GATE-SELFTEST-FAIL "selftest exited 1"`.
Contrast runs prove the intent is achievable: exit 7 → exit 2 `GATE-ABNORMAL-EXIT` (R2),
SIGKILL → exit 2 `exit -9` (R5), hang → exit 2 `GATE-TIMEOUT` (R4) — only the crash class slips
into 1. Fix direction: require a failing child's captured output to contain at least one
stable-ID finding line (`FAIL <STABLE-ID>`) before mapping to exit 1; otherwise exit 2.
The battery's own selftest (R11: `SELFTEST OK 5/5`, exit 0) does not cover this class, so its
passing green says nothing about it.

### P2 — HIGH: malformed nested data still crashes to exit 1, colliding with findings
The delivered craft CLI maps only file/CLI-level errors to exit 2 (`try` at :507-515 wraps
`parse_args`/`read_json_file`/`read_report_text`); `run_checks` runs outside it (:517). Any
shape-valid-root / shape-broken-nesting document crashes with an uncaught `AttributeError`
traceback and Python default exit 1 — indistinguishable from genuine audit findings, the exact
misleading-exit class the round set out to remove. Exact repro (N-series fixtures in scratch):
`{"audits": [3]}` → `AttributeError: 'int' object has no attribute 'get'`, exit 1, traceback
(N10, audit loop :119-127); `{"audits": {"x": 1}}` → same class (N11). Note two related shapes
survive only by accident of the `LAW-ORDER` early return (:171): `mech_expectations.cases: "xy"`
and `borrowed_garment_terms.terms: [1]` produce clean findings, not crashes, because the early
return skips those sections first (N13/N14). Fix direction: wrap `run_checks` and map
exceptions to a `CRAFT-CLI-INTERNAL-SHAPE`-style exit-2 diagnostic, or type-guard the audit and
mech loops.

### P3 — LOW: "originals preserved" is hash-set-covered for modification, blind to additions
`hash_snapshot` over `battery_paths()` (:61-65, :213-215) diffs per-file digests but never
compares the path set: a selftest that ADDS a new file under the original `tools/gates/fixtures/`
(via an absolute path) yields battery exit 0, `originals.preserved: true`, no findings (R7:
fake gate `open(<orig-fixture-dir>/NEWFILE.txt,'w')` → `exit=0 7p preserved=True`). Modification
of an existing original IS caught (R6: append to `fixtures/seed.yml` → exit 2
`GATE-BYTES-CHANGED`, `preserved: false`). Defense-in-depth only — real gates anchor paths via
`__file__`/HERE so mirror runs cannot reach originals, and children run with `cwd=mirror`
(:199-205) — but the report field overstates what is measured. Fix direction: compare the
post-run `rglob` file list against `before.keys()` too.

### P4 — LOW: `--timeout` accepts zero/negative floats, producing absurd all-unevaluable runs
`argparse type=float` (:309) admits `--timeout -5` / `0`: every gate is launched and instantly
timed out, report says `GATE-TIMEOUT "no exit within -5.0s"` ×7, battery exit 2 (R8). Exit
class ("could-not-evaluate") is at least right; a usage error (like `--timeout abc` → argparse
exit 2, R9) would be cleaner. Fix direction: validate `timeout > 0` and raise
`parser.error`.

### P5 — LOW: `--report` consumes a following flag as its value with a misleading message
`--report --counts` → `report = "--counts"` (:401-405) → exit 2
`CRAFT-CLI-REPORT-OPEN: cannot read report '--counts': No such file or directory` (N7). Exit
class is correct (2, stable ID, no traceback) but the diagnostic blames a nonexistent file
instead of a missing value; the adjacent missing-value case gets the accurate
`CRAFT-CLI-REPORT-VALUE` (N6).

### P6 — LOW: `--selftest` anywhere in argv still silently discards the positional target
`python3 tools/check-craft-exercise.py <path> --selftest` enters selftest mode; the named path
is never opened, default-exercise selftest prints `SELFTEST OK 10/10` + `CLI-SELFTEST OK 11/11`
and exits 0 (N9 — rerun of baseline B8 against delivered bytes). Deterministic mode-flag
semantics (`--selftest` cannot also be a positional under the new `parse_args`, :406-407), but
the silent-success-wrong-target outcome persists; a warning when extra positionals precede the
flag would close it.

## Verified-good in the delivered bytes (probed, not assumed)

- All six claim-O malformed craft controls exit **2** with stable IDs and no traceback: no-arg
  `CRAFT-CLI-USAGE`, missing file `CRAFT-CLI-NOT-FOUND`, malformed JSON `CRAFT-CLI-JSON`,
  non-UTF-8 `CRAFT-CLI-UTF8`, root-shape `CRAFT-CLI-SHAPE`, missing `--report` value
  `CRAFT-CLI-REPORT-VALUE` (N1–N6); unknown option `--count` → `CRAFT-CLI-USAGE` exit 2 (N8).
- The delivered craft CLI selftest is genuinely subprocess-level (spawns
  `[sys.executable, script, ...]` over isolated tempdir fixtures, :456-459) and passes on the
  delivered bytes: `SELFTEST OK 10/10` + `CLI-SELFTEST OK 11/11`, exit 0 (N16); its 11 cases
  cover all six malformed controls plus a finding-exit-1 case and a traceback-leak assertion.
- Battery isolation is real: each child is `[sys.executable, <mirror script>, --selftest]` with
  `cwd=mirror`, `shell=False` (:199-205, :111-118); mirrors are `mkdtemp` + `rmtree` and none
  leaked (0 in /tmp after 12+ runs); sandbox-modification detection works (R6).
- Abnormal exits map correctly except P1: exit 7 → 2, SIGKILL → 2, timeout → 2, missing gate →
  precheck exit 2 with no children run (R10), bad `--timeout` string → argparse exit 2 (R9).
- Battery `--selftest` on delivered bytes: 5/5 controls, exit 0 (R11) — claims accurate for the
  classes covered (pass/fail/missing/timeout/stable-IDs); the crash-exit-1 class of P1 is not
  among them.

## Deferred / out-of-scope (historical, unchanged — not new regressions)

- `LAW-ORDER` early-return silent check-skip (baseline F4, :171) and `--counts` declared-echo
  (baseline F5, :520) persist byte-unchanged per diff.
- `resolve_repo_path` (:353-358, :478) fixes only the selftest default-path CWD sensitivity
  (baseline F6); non-selftest invocations always take an explicit path, so no residual exposure.
- No symlinks exist under `tools/gates/fixtures` today (`find -type l` empty); code-level
  hardening note only: `copytree` default preserves symlinks as links, so a future fixture
  symlink pointing outside the hashed set would evade both mirror isolation and the P3 hash
  check. No live instance.
- Grandchild-process leak on `TimeoutExpired` not probed (real gates spawn no children);
  `--keep-mirror` not exercised (avoids /tmp litter), code-read only.

## Limits

- The delivered bytes are still uncommitted (` M`/`??` in `git status`); all P-findings cite
  these bytes and should be re-confirmed against the parent's acceptance commit if the worker
  amends before commit.
- Full battery and the other acceptance counting commands were deliberately not run on live
  gates (parent's job); battery behavior was characterized with 7-gate fake setups in the
  sandbox only, which cannot speak to the real gates' pass/fail state — only to the battery's
  own classification and isolation logic.
- Craft nested-shape probes covered the audit/mech/terms blocks reached before or behind the
  `LAW-ORDER` early return; every other nested section shares the same unprotected-`run_checks`
  exposure (P2), so the two repros are representative, not exhaustive.
- Author-side evidence only; no promotion, admission, or canon judgment is made here.

---

# Battery repair re-review (agent-458 bytes, same worker 15)

Scope-limited replay against the current `tools/check-gate-battery.py` (475 lines, still
uncommitted) after executor agent-458's repair. Sandbox refreshed at
`reports/supplement-opencode-1/scratch/round5-15/bat2/` from the delivered bytes; only the named
regressions were replayed (R1 crash, recognized genuine failure, R7 added-original-file, invalid
timeouts) plus one bounded crash-after-fail-line probe and the delivered `--selftest` once. The
broad original review was not repeated; the craft checker was not inspected or executed; no live
legacy selftest ran; `tools/gates/` diff empty and zero `gate-battery-*` dirs in /tmp after all
runs.

## Prior findings: fix verification (observed outcomes)

- **P1 (crash→exit1 misclassification): FIXED.** Sandbox traceback crash (fake
  `myth-consistency-gate.py` = `raise NameError("boom")`, six pass gates) now yields
  `outcome: unevaluable`, finding `GATE-CRASH-EXIT1` ("exit 1 without recognizable stable
  failure evidence; conservatively treated as a crashed child, not a finding", :204-212),
  `stderr_tail` retains `NameError: boom`, **battery exit 2**. Mechanism: exit-1 children map to
  `fail` only when captured output contains a line-anchored marker from
  `FAILURE_MARKER_RES` (`^SELFTEST FAIL`, `^FAIL \S`, `^failed: \S`; :75-79, :121-127, applied
  at :195 to the full captured streams — the 2000-char report truncation is display-only).
- **P3 (additions to originals undetected): FIXED.** Fake gate adding
  `fixtures/ADDED.txt` into the sandbox originals tree → `GATE-BYTES-CHANGED`,
  `preserved: false`, `added=1`, detail `added:fixtures/ADDED.txt`, **battery exit 2**
  (`diff_snapshots` :113-118 now returns modified/added/deleted; report counts at :317-324).
  Deletion coverage is unit-checked by the delivered selftest's `CTRL-TREE-DIFF`.
- **P4 (negative/zero timeout accepted): FIXED.** `--timeout -5`, `--timeout 0`,
  `--timeout abc` → argparse usage errors, exit 2, stable messages ("timeout must be a positive
  finite number...", "not a number: 'abc'") via `positive_float` (:82-91); non-finite values
  take the same guard (code-read; not separately executed).
- **Recognized genuine failure preserved (claim contract): VERIFIED.** Fake gate printing
  `FAIL MYTH-X: seeded` then exiting 1 → `GATE-SELFTEST-FAIL` with detail
  "selftest exited 1 with stable evidence: FAIL MYTH-X: seeded", outcome `fail`,
  **battery exit 1**.
- **False-clean audit of the conservative mapping: no false clean found.** Unrecognized
  exit-1 → `unevaluable` → exit 2, never 0; the docstring (:21-34) now explicitly documents that
  the five bare-`assert` legacy gates' genuine failures will classify as exit 2, not exit 1
  ("nonzero, not-green either way; it only refuses to vouch for which kind") — an honest,
  conservative consequence, not a green-wash. The delivered `--selftest` now has 9 controls
  including `CTRL-RECOGNIZED-FAIL`, `CTRL-EXIT1-UNRECOGNIZED`, `CTRL-CRASH-EXIT1` and
  `CTRL-TREE-DIFF` and passes `SELFTEST OK 9/9` exit 0 on the delivered bytes, closing the
  earlier selftest-coverage gap behind P1.
- Isolation unchanged and intact: children still `[sys.executable, <mirror script>,
  "--selftest"]`, `cwd=mirror`, `shell=False` (:277-285, :162-169); mkdtemp/rmtree mirror
  (:258, :287-290), none leaked.

## Bounded residual observations (new, LOW, no blocker)

- **R-A: a crash following an apparent failure line still reads exit 1.** Fake gate printing
  `FAIL MYTH-X: seeded` and then crashing (`1/0`) → evidence matches the earlier line →
  outcome `fail`, **battery exit 1**, detail cites the FAIL line while `stderr_tail` carries
  `ZeroDivisionError: division by zero`. The conservative marker rule cannot distinguish
  "genuine finding, then unrelated crash" from "genuine finding"; the mislabel direction is
  under-escalation (exit 1 instead of exit 2) and the crash evidence stays inspectable in
  `stderr_tail`. Bounded single probe per assignment; not developed into a general audit.
  Accepted-limitation note for the parent; a `GATE-OUTPUT-AND-CRASH` variant finding keyed on
  `stderr_tail` traceback shapes would be one possible tightening.
- **R-B: pass verdicts trust exit code only (pre-existing, unchanged).** A gate that prints
  `FAIL MYTH-X: seeded` but exits 0 yields outcome `pass`, battery exit 0, no findings (bounded
  probe C2). This is inherent to the exit-code contract over trusted historical gate bytes and
  predates the repair; recorded so the false-clean question is answered on both sides: the
  conservative mapping introduces no new false clean, and the only false-clean surface remains
  "exit code lies", which the battery does not claim to audit.

## Verdict for this re-review

P1, P3, P4 are fixed and verified at runtime in an isolated sandbox; genuine-failure exit-1
mapping is preserved with recognized evidence; no false clean introduced; remaining items R-A
and R-B are LOW, documented, and non-blocking. No blocker for the battery executor from this
reviewer. Craft checker remains unreviewed this pass (executor still finishing); the earlier
P2/P5/P6 craft findings stand as written. Author-side continuity review only — no promotion,
admission, or canon judgment.

---

# Final bounded re-review (agent-457 craft bytes + agent-458 battery veto, worker 15)

Scope-limited replay only: craft N10/N11, N7, N9, and an explicitly supported
`--selftest <exercise.json>` invocation under a strict timeout; battery R-A (fail-line-then-crash)
on refreshed sandbox bytes (`scratch/round5-15/bat2/tools/check-gate-battery.py`, copied from the
current 488-line file) plus one delivered `--selftest` run. Craft bytes are 664 lines, still
uncommitted. No broad audit, no live gate selftests, no original-tree mutations (`tools/gates/`
diff empty throughout), no code edits or commits.

## Prior findings: fix verification (exact observed outcomes)

- **P2 / N10–N11 (nested malformed audits crashed to exit 1): FIXED.**
  `{"audits": [3]}` → `CLI-ERROR CRAFT-CLI-SHAPE: 'audits[0]' must be a JSON object`, exit 2,
  no traceback; `{"audits": {"x": 1}}` → `CRAFT-CLI-SHAPE: 'audits' must be a JSON array`,
  exit 2. Mechanism: a `require()` shape-guard layer (:399, :405-441+) validates the mutated
  structure before `run_checks`. This verifies the two repro'd crashes only — no claim of
  arbitrary-schema safety for every possible malformed document is made or implied.
- **P5 / N7 (`--report --counts` flag eaten as value): FIXED.** Now
  `CRAFT-CLI-REPORT-VALUE: --report needs a report file path`, exit 2 — the accurate
  missing-value diagnostic replaces the misleading "cannot read report '--counts'".
- **P6 / N9 (positional silently ignored by `--selftest`): FIXED.**
  `check-craft-exercise.py <path> --selftest` → `CRAFT-CLI-USAGE: unexpected argument before
  --selftest: '<path>'`, exit 2 — the malformed named target can no longer be silently skipped.
- **Strict-timeout explicit selftest (no recursion/hang): PASS.**
  `timeout 30 python3 tools/check-craft-exercise.py --selftest
  examples/supplement-opencode-1/sound-change-vs-taboo.json` → exit 0 in **425 ms** wall,
  printing `SELFTEST OK 10/10 tamper cases detected` + `CLI-SELFTEST OK 18/18 cases passed`
  (10 domain + 18 CLI, matching the executor's report). The conflicting-mode guard
  (`--selftest` + other tokens → `CRAFT-CLI-USAGE` exit 2, usage :26-28, selftest case
  "selftest-conflicting-mode") stops self-referential re-entry before the subprocess driver
  runs; the 18 subprocess cases themselves complete and clean their tempdir.
- **R-A (battery: crash after an apparent failure line mislabeled exit 1): FIXED.** Replay on
  current battery bytes: fake gate printing `FAIL MYTH-X: seeded` then crashing (`1/0`) →
  traceback veto (`^Traceback \(most recent call last\):`, :121-127) rejects the earlier
  marker → `GATE-CRASH-EXIT1` ("exit 1 with a Python traceback or without stable failure
  evidence; conservatively treated..."), outcome `unevaluable`, `stderr_tail` retains
  `ZeroDivisionError: division by zero`, **battery exit 2**. Under-escalation is gone for this
  class; recognized failures without tracebacks still map to exit 1 (verified last pass, bytes
  for that path unchanged). Delivered battery `--selftest`: `SELFTEST OK 10/10 controls behaved
  as expected`, exit 0 — the parent-reported 10/10 count observed directly.

## Informational: /tmp residue from the repair session (not a delivered-bytes defect)

428 historical `craft-cli-selftest-*` directories in /tmp (timestamps ~14:14, during the craft
repair iterations; each ~56K holding the selftest's 8 fixture files, ~24 MB total; zero
`gate-battery-*`). The delivered bytes leak none: across the timed explicit selftest (which
spawns all 18 subprocess cases), the battery selftest, and every probe this pass, the count went
428 → 428. Probable source: earlier repair iterations or SIGKILLed children dying between
`mkdtemp` and the `finally` cleanup. Left in place — outside my write scope; trivially
sweepable (`rm -rf /tmp/craft-cli-selftest-*`) at the parent's discretion.

## Final verdict for this reviewer

N10/N11 (P2), N7 (P5), N9 (P6), the recursion/hang concern, and battery R-A are all fixed and
verified at runtime against the delivered bytes; no new defect surfaced within this bounded
scope; no blocker from this reviewer for either executor. All earlier findings in this file
remain historical record; observed fixes do not certify arbitrary-schema safety, and this is
author-side continuity evidence only — not independent promotion verification and no canon,
admission, or round judgment.
