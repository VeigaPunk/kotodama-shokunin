# Round 24 — cold-run B: SKILL.md executable surface executed by a fresh-context seat

Seat: executor B, round 24 (non-author verifier; zero lane history). Contract
honored: I read ONLY `SKILL.md`, `AGENTS.md`, `PROVINCE.md`, `SHONEN.md` — no
`LOG.md`, no `SCORECARD.md`, no corpus bodies, no `reports/round-8..23`
content. Directory listings (`examples/`, `tools/gates/frozen/…`) and the
round-24 dispatch files (`claims.json`, `targets.json`, both named READ-FIRST
in the dispatch) were used for command targeting only. `git show 291c714:…` /
`git archive HEAD` were used solely to execute SKILL.md's own documented
restore-and-replay recipe (§E10) — no historical artifacts read. No git
mutations; no writes outside this file, `.scratch/` (gitignored), and test
trees under `TMPDIR=/tmp/coldrun-b`.

Target interpretation: "the SKILL.md executable checklist" executed as the
full executable surface — the Gates-and-probes table, the D3 replay checklist
(`SKILL.md:571-590`), the D4 typed-pipeline authorities, and the round-scoped
re-run commands — because the four-item prose checklist at `SKILL.md:408-420`
contains only one named executable (executor A's report covers that reading;
see §4). Every command ran from the lane repo root; scratch rule
`TMPDIR=$PWD/.scratch` used except where a tool refuses in-repo temp roots
(F2).

## 0. Executed command list (commands → exit codes)

Gates table / probes (D2 packet `examples/culture-d2/packet.d2.yml`, D3
artifacts, D4 artifacts — paths grounded in `examples/` listings):

| # | Command | Exit | Observed |
|---|---|---|---|
| E1 | `python3 tools/check-gate-battery.py` (default) | 0 | `pass 7 / fail 0 / unevaluable 0`; duty-2 baselines auto-discovered 19, `coverage: 9/9`, `baseline_exit 0`; `originals.preserved: true, modified: 0` |
| E2 | `python3 tools/check-gate-battery.py --baselines-root reports/round-9/baselines` | 2 | `BASELINE-GATE-UNCOVERED` — the documented remedy fail-closes (matches A's E8, independently reproduced) |
| E3 | `python3 tools/assemble-d2.py --check` | 0 | `packet.d2.yml: byte-identical deterministic assembly` |
| E4 | `python3 tools/assemble-culture-d3.py --check` | 0 | both derived outputs byte-identical |
| E5 | `python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json` | 0 | `findings: []` |
| E6 | `python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json` | 0 | frozen comparison clean |
| E7 | `python3 tools/check-craft-exercise.py examples/supplement-opencode-1/sound-change-vs-taboo.json` | 0 | `OK all checks passed (audits=7, mech_cases=11, derivations=9, approx_checks_runner=37)` |
| E8 | `python3 tools/gates/naming-collision-gate.py examples/culture-d3/packet.gates.yml` | 1 | `NAME-NEAR` E0/E1 + 2× `CROSS-HOLD` HOLD — exactly the pair SKILL.md's D3 checklist step 3 says to keep |
| E9 | `python3 tools/gates/costume-era-consistency-gate.py examples/culture-d3/packet.gates.yml` | 1 | `R-01` note on C03 — exactly the finding step 3 says to keep |
| E10 | `python3 tools/gates/handoff-packet-check.py examples/culture-d3/handoff.md` | 0 | `fields=16/16 glossary-entries=20 findings=0` (D3 step 4 envelope leg) |
| E11 | `python3 tools/gates/handoff-packet-check.py examples/handoff-packet.sample.md` | 0 | 16/16, 20 rows, 0 findings |
| E12 | `python3 tools/gates/phonology-sanity-gate.py examples/culture-d2/packet.d2.yml` | 1 | `A-NEUTRAL` REVIEWs — matches SKILL.md "Using the evidence" row 1 |
| E13 | `python3 tools/gates/lexicon-coverage-audit.py examples/culture-d2/packet.d2.yml` | 0 | clean |
| E14 | `python3 tools/gates/myth-consistency-gate.py examples/culture-d2/packet.d2.yml` | 0 | clean |
| E15 | `python3 tools/gates/costume-era-consistency-gate.py examples/culture-d2/packet.d2.yml` | 0 | clean |
| E16 | `python3 tools/gates/provenance-audit.py corpus/knowledge/synthesis/` | 0 | `files=29 marks=111 findings=0` |
| E17 | `python3 tools/source-audit-inventory.py --json` | 0 | schema emitted, `read_only: true` |

Frozen replay:

| # | Command | Exit | Observed |
|---|---|---|---|
| E18 | `python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv` (live tree) | 2 | 7/7 `gate_digest_mismatch` — matches SKILL.md's documented live-tree verdict |
| E19 | restore the manifest's six gate files from `291c714` into an isolated `git archive HEAD` export, then `python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv --repo-root <export>` | 0 | `REPLAY OK: 7/7 rows reproduced` — SKILL.md's pinned-revision recipe reproduces EXACTLY as written |
| E20 | `python3 tools/replay-frozen.py tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv` with `TMPDIR=$PWD/.scratch` | 2 | 3/3 rows `mirror_unsafe`: "temporary root is inside the repo" — F2 below |
| E21 | same with `TMPDIR=/tmp/coldrun-b` (outside repo) | 0 | 3/3 reproduced (round-22 section's "3 rows, exit 0" holds under the undocumented precondition) |

D4 typed-pipeline authorities (SKILL.md round-8..23 D-section):

| # | Command | Exit | Observed |
|---|---|---|---|
| E22 | `python3 tools/d2-typed-labels.py --selftest` | 0 | `163/163 checks passed` — matches SKILL.md's pinned count exactly |
| E23 | `python3 tools/harness/packet_uncertainty.py --selftest` | 0 | 19 checks |
| E24 | `python3 tools/gates/typed-pipeline-gate.py` (flagless) | 0 | `16/16 legs passed` — flagless resolution works as documented |
| E25 | `python3 tools/assemble-d4-typed.py --check` | 0 | byte-identical deterministic typed packet |
| E26 | `python3 tools/d2-typed-labels.py --check examples/culture-d4/typed-labels.d4.yml --packet examples/culture-d4/packet.d4.yml` | 0 | named-pair check byte-identical |

Selftests (isolated where the tool writes fixtures; battery duty-1 covers the
seven legacy ones in disposable copies):

| # | Command | Exit | Observed |
|---|---|---|---|
| E27 | `python3 tools/assemble-d2.py --selftest` | 0 | 42/42 |
| E28 | `python3 tools/assemble-culture-d3.py --selftest` | 0 | 85/85 |
| E29 | `python3 tools/check-evidence-coupling.py --selftest` | 0 | selftest_passed true |
| E30 | `python3 tools/check-craft-exercise.py --selftest` | 0 | 10/10 tamper + 18/18 CLI |
| E31 | `python3 tools/gates/naming-collision-gate.py --selftest` | 0 | 12 findings / 11 ids |
| E32 | `python3 tools/gates/handoff-packet-check.py --selftest` | 0 | 11 findings / 9 ids |
| E33 | `python3 tools/source-audit-inventory.py --selftest` | 0 | exact-count controls pass |

Round-scoped re-run commands (run in a pristine `git clone` of HEAD at
`/tmp/coldrun-b/clone`, so the receipts they write never touch filed paths;
cross-checked in a pristine `git archive HEAD` export — same verdicts):

| # | Command | Exit | Observed |
|---|---|---|---|
| E34 | `python3 reports/round-5/run-validation.py` | 1 | F: `non-append corpus edit: ('corpus/lessons/supplement-opencode-1/sources/ottoman.json', 'OTT-06')`; O: runs the round-3 replay in the live tree and `expected 0, got 2` — the very exit-2 behavior SKILL.md:481-484 documents as correct for the live tree. F3 below. |
| E35 | `python3 reports/round-6/run-validation.py` | 1 | `error: "historical file changed: .gitignore"` (preservation pin vs current tree) |
| E36 | `python3 reports/round-7/run-validation.py` | 1 | F: `wrong rejection for duplicate-parent-receipt-does-not-inflate: parent check identity collision`; O passes; receipt records the saved_template conformance defect as "not an F or O failure" while still exiting 1 — no expected verdict is documented anywhere in the seat's four files |

Seat-artifact note (transparency): one earlier export was contaminated by my
own E19 gate restore before running E34 there; its r5 battery-leg failure is
mine, discarded, and E34-E36 were re-run in the clean clone.

## 1. Findings

- **F1 (stale documentation, corroborates A's F5).** `SKILL.md:501` states the
  battery's committed default exits 2 (`BASELINE-GATE-UNCOVERED` for myth and
  naming) and that `--baselines-root reports/round-9/baselines` reaches 0.
  Both halves are inverted on today's tree: default exit 0 with 19 baselines
  auto-discovered and `coverage: 9/9` (E1); the instructed flag yields exit 2
  (E2, independently confirming A). Evidence: E1/E2 output in `.scratch/`.
  Condition: correct the cell (default exit 0; round-9 root as historical
  context only).
- **F2 (undocumented precondition on a documented exit-0 command).** The
  round-22 section pins `d4-repin/MANIFEST.tsv` at "3 rows, exit 0"; E20 shows
  it exit 2 `mirror_unsafe` under the round-mandated `TMPDIR=$PWD/.scratch`,
  exit 0 only with a TMPDIR outside the repo (E21). The frozen-replay row's
  write scope ("auto-cleaned scratch only") does not state the outside-repo
  requirement. Condition: name the TMPDIR constraint where the exit-0 pin is
  stated.
- **F3 (re-run commands have no documented expected verdicts, and all three
  currently fail at clean HEAD).** SKILL.md presents `reports/round-5/6/7/
  run-validation.py` as re-runnable acceptance (lines 516-518, 541-542,
  587-590) without stating any expected exit. Measured at clean HEAD (E34-E36):
  all exit 1 with distinct causes (non-append corpus edit; historical
  .gitignore changed; identity-collision control + recorded template
  conformance defect). A fresh seat cannot distinguish an honest recorded
  failure from a break without lane history it is forbidden to read. Note the
  round-5 O-leg contradicts SKILL.md's own current replay documentation
  (live tree is documented to exit 2, the script expects 0). Condition: state
  current expected verdicts (or dated errata) for the three rows.
- **F4 (write-path hazard).** E34-E36 write `reports/round-N/validation.json`
  into whatever tree they run in (measured: receipts created in my clone and
  export). SKILL.md gives the isolated-export caveat only for the battery and
  the frozen replay, not for these; a fresh seat that obeys a
  write-only-assigned-files dispatch cannot run them in place, and one that
  follows SKILL.md literally overwrites filed receipts. Observed in the shared
  tree at seat start: ` M reports/round-7/validation.json` (mtime
  2026-10-18 13:08:06, 1-line diff) — pre-existing, not produced by any
  command in my list, and also present at executor A's seat start. Condition:
  extend the isolation caveat to the three run-validation commands.
- **F5 (ambiguity, protocol-level).** "The SKILL.md executable checklist" has
  two defensible readings: the `SKILL.md:408-420` prose checklist (executor
  A's target; its items 1/3/4 name no operand) versus the gates/D3/D4
  executable surface (this report). Likewise the dispatch's "four files" were
  not enumerated per seat: A's set included `corpus/README.md`, mine
  `SHONEN.md`. Both runs stayed within closed four-file sets; the parent
  should pin the reading and the file list for future cold runs.
- **F6 (minor ambiguity).** D3 checklist step 4's first half ("compare the
  handoff's glossary, names, source bridges and digest rows against actual
  packet bytes") is manual prose with no tool; only the second half is a gate
  (E10). The main checklist's "executable where a tool exists" caveat is not
  repeated on the D3 checklist.

## 2. What held (box-3 positive evidence)

- Every pointer SKILL.md's executable surface names resolves on today's tree;
  no missing tool, fixture, or example path was hit in ~35 invocations.
- Pinned selftest counts reproduce exactly: `163/163` (E22 vs SKILL.md's
  claim), plus 42/42, 85/85, 16/16 legs, 10/10+18/18.
- The hardest documented recipe — restore the six gates from `291c714`, replay
  the round-3 manifest in an isolated tree — reproduces 7/7 exit 0 exactly as
  SKILL.md:459,481-484 promises (E19), and the live-tree exit-2/7×mismatch
  state matches the same lines (E18).
- The full D2→D3→D4 chain is byte-identical at HEAD (E3/E4/E25/E26), the D3
  checklist's step-3 expectations reproduce verbatim on real artifacts (E8/E9:
  CROSS-HOLD + NAME-NEAR, R-01 on C03), and the D3/D4 handoff envelopes pass
  (E10/E11: 16 fields, 20 glossary rows, 0 findings).
- Gate write discipline held everywhere the table claims it (battery
  `preserved: true, modified: 0`; inventory `read_only: true`).

## 3. Conditions under which the executable surface is end-to-end runnable

1. F1's battery cell is corrected (or read as historical), else a fresh
   executor fail-closes a green battery by following the documented remedy.
2. F2's TMPDIR-outside-repo precondition is stated on the d4-repin exit-0 pin.
3. F3's three re-run rows gain current expected verdicts; until then a fresh
   seat must treat their exit 1 as unadjudicated.
4. F4's isolation caveat covers the three run-validation commands.

Under those four conditions, every SKILL.md command I executed matches its
documented verdict; today, items 1-2 are live breaks for a cold executor
(they mislead), items 3-4 are undocumented-state ambiguities (they dead-end).

## 4. Conceptual comparison with cold-run A (read after my execution was complete)

- **Independent agreement on the one overlapping stale row.** A's F5 and my F1
  are the same defect found independently with the same measurements (default
  0 / flag 2). I additionally reproduced A's E8 after reading their report —
  same exit 2. Highest-confidence finding of the round.
- **Complementary targets, no contradictions.** A executed the four-item prose
  checklist (`SKILL.md:408-420`) and found items 1/3/4 lack operands; I
  executed the gates/D3/D4 surface and found it green except the two doc rows
  and the three unadjudicated re-runs. The two readings of "the executable
  checklist" should be merged for the box-3 verdict: machinery executes and
  matches its pins; the prose checklist is 1-of-4 executable by design; the
  re-run scripts execute but have no declared pass state (my F3).
- **Corroborated hygiene.** A saw the same pre-existing
  ` M reports/round-7/validation.json` at seat start and attributed it to
  concurrent seats, as I do (F4); A's corpus-clean result (199 files, exit 0)
  is consistent with my synthesis-partition run (29 files, exit 0).
- **No overlap conflict.** A ran 9 commands, I ran ~35; the only common
  families (battery, provenance-audit, handoff-packet-check, inventory)
  agree on every verdict.

## 5. Seat hygiene

Writes: this report, `.scratch/` (gitignored, incl. the `coldrun-b-export`
test tree), and `/tmp/coldrun-b` (outside-repo test trees). No `git add`
or commit; no writes to rounds 8-23 artifacts; no lane-history artifacts
read (LOG.md, SCORECARD.md, corpus bodies, reports/round-8..23 — the sole
exceptions are this round's `cold-run-a.md` after execution, and the two
dispatch JSONs the dispatch itself ordered read first).
