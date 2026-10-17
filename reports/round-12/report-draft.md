# kotodama — round 12 report (DRAFT BODY — orchestrator finalizes)

> **Scribe X04 draft.** Assembled from the round-12 evidence present at
> **2026-10-17T22:59:15Z**. This is an audit report, not an admission or a
> validator receipt. Several required consolidation artifacts remain absent;
> the round-12 validator was not run because its `main()` writes
> `reports/round-12/validation.json` (`run-validation.py:804-807`). No
> round-8–11 artifact was edited by this scribe, and no commit or push was
> performed.

The declaration records operator loop 1 of 3, the verify round over rounds
8–11, baseline `a3f6fcef2d92a1099581140c81d4264e9a4e2aa3`, requested model
`openai-codex/gpt-6-luna-max`, and 64 requested workers
(`reports/round-12/claims.json`, declared 2026-10-17). These are declaration
fields, not an independently verified dispatch receipt.

## Work performed

### Calibration — claim C

The recount fragments cover the four source rounds and their individual
measurements are useful, but a read-only comparison against the validator's
command extractor does **not** establish the required complete recount. On
2026-10-17T22:56:03Z, the read-only command `export TMPDIR="$PWD/.scratch"
PYTHONDONTWRITEBYTECODE=1; python3 - <<'PY'` loaded `command_sources()` from
`reports/round-12/run-validation.py`, parsed `reports/round-12/recount/ledger.json`,
and compared normalized `(source round, command)` keys: it extracted 51 unique
source-command keys, while the ledger had 28 rows and 21 unique normalized keys;
43 expected keys were absent, 13 keys were unreferenced, and some command keys
were duplicated or did not normalize. The same probe found eight keys in common.
Thus the ledger's presented rows cannot be treated as 100% coverage. The probe
was read-only; it did not invoke the validator or write `validation.json`.

The independent audit fragment arrived during the final dependency wait. It
records 13 distinct ledger commands independently re-run on 2026-10-17; 12
reproduced and one round-9 battery hash differed from the ledger's observed
hash, while exit status and structured results matched. The auditor classifies
that mismatch as environmental because random `.scratch/gate-battery-*` paths
survive the existing normalizer (`reports/round-12/recount/audit.md`, per-command
timestamps). A separate read-only check at 2026-10-17T22:57:55Z confirmed the
validator's filename scan recognizes `recount/audit.md` and finds 13 source
commands in it, satisfying its documented minimum of eight. However, the
validator's unresolved-mismatch regular expression also matches `C23` in the
phrase “mismatch is C23-F1”; this would likely report a false positive despite
the explicit environmental disposition. The validator was not run to test that
inference.

Round-specific recount findings (all recount receipts dated 2026-10-17):

- **Round 8.** The isolated-clone `python3 reports/round-8/run-validation.py`
  recount reproduces the F measurements (15 declared IDs, receipts and
  substantive passages; 215 distinct passage keys). O changes from recorded
  fail to observed pass because the later round-11 commit cleared the previously
  dirty round-7 validation path; 12 of 14 control stdout hashes differ because
  `.scratch` paths are unnormalized. D remains failed: replay exits 2 with 7
  rows, 0 reproduced, and 7 unevaluable; the restored-gate count changed from 7
  to 8 after a later gate was added (`recount/r8-1.md`; command above, isolated
  shared-object clone, 2026-10-17). `python3 tools/harness/r8_checks.py
  --selftest` reproduces 14/14, but round-8 operability prose says 12/12 with the
  same digest; this is an unresolved historical transcription defect
  (`recount/r8-2.md`; both measurements 2026-10-17). The same fragment records
  successful `python3 tools/check-gate-battery.py --selftest` (28/28),
  `python3 tools/check-craft-exercise.py --selftest` (10/10 tamper and 18/18
  CLI cases), and `python3 tools/d2-typed-labels.py --selftest` (39/39), all on
  2026-10-17. A read-only tree count reproduces the admission total of 179
  Markdown files and its six partition counts; the live `find corpus/knowledge
  -type f -name '*.md' | wc -l` is 189 because later round-10 work added 10
  files (`recount/r8-3.md`; both tree commands, 2026-10-17). A read-only target /
  header comparison finds six declared civilization ranges but only five
  contiguous fragments for the same 94-item coverage, an allocation-record
  defect rather than missing corpus content (`recount/r8-3.md`; Python
  comparison, 2026-10-17). `python3 tools/assemble-d2.py --check` repeats
  byte-identically; current typed-label check/emit output differs from a
  historical tool-revision-bound receipt, while current repeated emits match
  each other (`recount/r8-4.md`; both commands, 2026-10-17).
- **Round 9.** The custom-root `python3 tools/check-gate-battery.py
  --baselines-root tools/gates/frozen --baselines-root tools/gates/expected
  --baselines-root reports/round-9/baselines` run reports 8 pins, all 7 gates
  covered, 7 pass, 0 fail, and 0 unevaluable; its observed stdout hash differs
  because `.scratch` paths are not normalized (`recount/r9-1.md`; command,
  2026-10-17). `python3 tools/assemble-culture-d3.py --check` and the frozen
  `python3 tools/check-evidence-coupling.py ... --frozen ...` replay reproduce
  their recorded normalized outputs and zero findings (`recount/r9-2.md` and
  `r9-3.md`; respective commands, 2026-10-17). The original 179-path metadata
  readings reproduce; current counts are 189 files and strict-A missing fields
  rise from 64 to 70 because six later round-10 entries lack a singular
  `source:` line. Source inventory rises from 179 files / 584 markers to 189 /
  633 (`recount/r9-4.md`; read-only Python census and
  `python3 tools/source-audit-inventory.py --json --summary`, 2026-10-17).
  V09 is present in the current 11-fragment listing although it was absent at
  the earlier audit snapshot (`recount/r9-4.md`; `ls reports/round-9/metadata/
  v*.md | wc -l`, 2026-10-17).
- **Round 10.** A read-only census reproduces 189 corpus files, 10 additions
  since its baseline, and the declared per-partition minimums
  (`recount/r10-1.md`; corpus/README/source-inventory/Git census, 2026-10-17).
  The frozen R10 F surface is 36/36 covered, but the live surface is 36/38 with
  2 later command additions (`recount/r10-2.md`; read-only extraction using
  round-10 `command_key`/`covers` functions, 2026-10-17). The tracker recount
  matches 24 rows and 18 extracted IDs, with dispositions 18
  fixed-with-control, 5 wont-fix, and 1 wrong (`recount/r10-3.md`; read-only
  tracker recount, 2026-10-17). The recorded live invocation of
  `python3 reports/round-10/run-validation.py` returned C PASS, F FAIL, O PASS,
  exit 1, citing 36/38 coverage; it briefly rewrote the filed
  `reports/round-10/validation.json`, which its worker restored from HEAD and
  checked with `git diff --quiet` exit 0 (`recount/r10-4.md`; invocation and
  restoration check, 2026-10-17). Do not rerun it.
- **Round 11.** A read-only Python census over the 192 row receipts and ledger
  finds 189 byte-comparable, 147 stable, 42 hash-unstable, and 3 without hashes.
  The comparable-row ratio is 147/189 = 0.777777… (0.778); the all-row ratio is
  147/192 = 0.765625. The phrase “147/192 stable = 0.778” is therefore
  mathematically inconsistent. The 45 hash-unstable-plus-unreproducible rows
  have named causes; the 46 validation drift rows include row 101's separately
  dispositioned exit-only drift (`recount/r11-1.md` and `r11-2.md`; read-only
  Python census, 2026-10-17). `python3 tools/gates/typed-pipeline-gate.py
  --json` exits 0 with the exact 16-token set, 15 holds and 1 note; expected
  and live sets match (`recount/r11-3.md`; command and receipt comparison,
  2026-10-17). The filed round-11 runner was not invoked because it writes its
  filed validation JSON; independent read-only recomputation still confirms F
  below 0.95 and D equality (`recount/r11-4.md`; read-only census and gate
  command, 2026-10-17). The rejection remains consistent with validation,
  SCORECARD and LOG (`defects/sweep-r11.md`; read-only comparison, 2026-10-17).

### Operability — claim O

The earlier inventory found sweeps for rounds 8, 9, and 11 but not round 10;
round-10's sweep arrived during the final wait. The final inventory has all four
(`reports/round-12/**/*`, at 2026-10-17T22:55:03Z and 2026-10-17T22:59:15Z,
respectively; sweep audits dated 2026-10-17). Their findings must remain visible,
not be silently repaired in filed history:

- Round 8's acceptance receipt was true at its cited work commit but is false in
  the current tree after the round-11 commit rewrote that filed JSON. The sweep
  attributes the only post-close change to that commit and the runner's
  write-to-output behavior; preserve the drift rather than restoring or
  regenerating the filed receipt (`sweep-r8.md`; Git history, JSON comparison
  and status checks, 2026-10-17).
- Round 9's accepted receipt does not settle the default baseline-layout defect:
  the default battery finds 5 baselines and leaves 2 of 7 gates uncovered,
  while the custom-root run finds 8 pins and covers all 7 gates. The two
  required gate baselines are outside the standard layout. Keep the recorded
  paths unchanged and route reconciliation to round 14 (`sweep-r9.md`;
  `python3 tools/check-gate-battery.py` and its custom-root invocation,
  2026-10-17).
- The round-10 sweep records findings F-01 through F-06: LOG baseline versus
  declaration confusion; updater misclassification; conflicting stale-fixed
  records for a reverted round-8 runner; a missing verifier name in the
  tracker; an unfinalized SHONEN draft with an 8-versus-10 entry-count conflict
  (read-only Python check of the draft and receipt, `sweep-r10.md`,
  2026-10-17); and an unresolved historical runner-hash prefix. Its read-only hash audit
  finds 74/76 current input paths match and attributes the 2 mismatches to
  later round-11 changes (`sweep-r10.md`; its cited Git, Python and SHA-256
  measurements, 2026-10-17). No round-10 runner was invoked by that sweep.
- Round 11 remains rejected, while its in-lane report is still a draft and
  retains the stale in-flight F count of 149 stable / 43 unstable rather than
  the settled 147 / 45. Current validation bindings match, but the report must
  be finalized without rewriting the filed draft (`sweep-r11.md`; read-only
  receipt census and digest comparison, 2026-10-17).

The required consolidated `reports/round-12/defects/ledger.json` and
`reports/round-12/defects/routed.md` were still absent in the final inventory
(`reports/round-12/**/*`, 2026-10-17T22:59:15Z). Consequently there is no
machine-readable cross-round queue showing every defect, bounded fix, owner,
round-14 route, or before/after control. The claim that small fixes landed with
controls and all larger items were routed is **not established** by the
individual sweeps alone.

Regression evidence is green but is not a substitute for the missing defect
ledger. At the checkout named in `defects/regression.md`, the dated commands
report: gate-battery selftest 28/28; craft selftest 10/10 tamper and 18/18 CLI;
typed-label selftest 39/39; D2 assembler selftest 42/42; D3 assembler selftest
85/85; and the custom-root battery 7 pass / 0 fail / 0 unevaluable. The same
record reports successful positive craft run and byte-identical D2, typed-label
and D3 checks (`defects/regression.md`; each command and its immediately
preceding `date -Iseconds`, 2026-10-17). These are controls at the recorded
checkout, not proof that a bounded conformance fix has been integrated.

### Adjacency — claim A

The handoff shape gate is green but does not authorize transfer. At
2026-10-17T22:37:57Z, `python3 tools/gates/handoff-packet-check.py
reports/round-11/handoff/packet.md` returned exit 0, 16/16 required fields,
20 glossary entries, and 0 findings. At 2026-10-17T22:45:44Z a read-only manifest
hash check matched all 21 file-backed artifact rows. These checks do not cure
semantic gaps: same-revision bilateral acknowledgment is pending; the claim
ledger has no explicit per-claim uncertainty field or claim-to-record/edge key;
and D2 coupling is aggregated rather than expressed per source-target record
(`adjacency/contract.md`; commands and timestamps above, 2026-10-17). Keep the
packet classified as a successful non-canon, deliberately unbound exercise, not
an accepted handoff. The old round-8 L0 digest premise is stale; the governance
acknowledgment remains open in the latest recorded evidence, and the live
out-of-lane L0 surface was not inspected (`adjacency/contract.md`, status
snapshot at 2026-10-17).

The province review finds no scope drift across the reviewed round-8 typed
labels, round-9 D3 work, round-10 entries and round-11 typed pipeline/handoff;
`PROVINCE.md` remains accurate and no correction is recommended. A read-only
presence command found all 10 named round-10 corpus additions (`province.md`,
2026-10-17T22:49:37Z); `git diff --quiet
a3f6fcef2d92a1099581140c81d4264e9a4e2aa3 -- PROVINCE.md` was empty at
2026-10-17T22:49:19Z (`province.md`). This is a static scope review, not a
rerun of historical pipelines. The substantive review is present as
`reports/round-12/adjacency/province.md`, but the validator specifically reads
`reports/round-12/adjacency/province-check.md`; that expected path was absent in
the final inventory (`reports/round-12/**/*`, 2026-10-17T22:59:15Z).

The adjacent ledger is also absent: `reports/round-12/adjacency/ledger.json`
was not present at the final inventory (`reports/round-12/**/*`,
2026-10-17T22:59:15Z). The review supports a no-drift conclusion for the
inspected work, but the required per-entry structured accounting and
zero-unreported-bleed assertion cannot be verified from the missing ledger.

### Scope and side effects

The scope watch records a clean fleet-root status and no post-declaration
commits at its 2026-10-17T19:38:31-03:00 snapshot. Of 19 sibling repositories,
18 were clean then; `lore-shokunin` had 10,807 dirty paths, mostly under its
round-97 work, with no post-cutoff commit and no evidence attributing those
changes to Kotodama (`reports/round-12/scope.md`; dated `git status` and `git
log` census, 2026-10-17). Sibling cleanliness is therefore not fully
established. At the final scribe check, `git status --short -- reports/round-8
reports/round-9 reports/round-10 reports/round-11` was empty
(2026-10-17T22:59:15Z); the temporary round-10 receipt rewrite reported above
had been restored before this check.

## Before → after and status

| claim | evidenced state | current assessment |
|---|---|---|
| C / calibration | Recount fragments, a machine ledger, and an independent sample exist; key historical discrepancies have named causes. | **Not demonstrated as claimed.** Read-only extractor comparison finds missing source-command keys and duplicate/unreferenced rows (the same `command_sources()`-versus-ledger probe, 2026-10-17T22:56:03Z); the independent battery-hash difference is explicitly dispositioned environmental (`recount/audit.md`, 2026-10-17). |
| O / operability | Cross-round sweeps and regression receipts exist. | **Not demonstrated as claimed.** No consolidated defect ledger or round-14 routing note; no auditable bounded-fix ledger. Filed-receipt rewrite, default-baseline conformance, report finalization and other defects remain open. |
| A / adjacency | Contract review and province review exist; the handoff shape gate is green. | **Not demonstrated as claimed.** No adjacency ledger or validator-named province-check file; semantic handoff gaps and bilateral acknowledgment remain open. |

These are evidence assessments, not the missing machine receipt and not a final
admission decision. No validator result is asserted. In particular, do not
interpret the successful regression checks or handoff shape gate as passing all
three round-12 claims.

## Open items for the orchestrator

1. Complete the recount ledger against every unique source-command key and
   resolve duplicates/unreferenced rows; disposition the auditor's environmental
   hash mismatch without hiding it. Correct or explicitly account for the
   validator's `C23-F1` text-matching false positive before relying on its
   audit scan.
2. Create the consolidated defect ledger and owner-bearing round-14 routing
   note. State which bounded fixes, if any, landed and attach before/after
   controls; preserve all filed round-8–11 receipts and report drafts.
3. Create the structured adjacency ledger and satisfy the province-review
   filename contract or amend the validator's contract through an authorized
   change; retain the substantive province review as evidence. Resolve the
   contract acknowledgment with lore/integrator, and keep the handoff explicitly
   non-canon until both sides acknowledge the same revision.
4. Only after those dependencies are reconciled should the orchestrator decide
   whether to run the round-12 validator and publish a final report. Its output
   path is a new `reports/round-12/validation.json`; no historical runner should
   be invoked to manufacture a fresh receipt.
