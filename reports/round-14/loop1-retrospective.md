# Loop-1 retrospective — rounds 8–13

Historical record date: **2026-10-17**. Consolidated in round 14 on
**2026-10-18 UTC** (2026-10-17 local). Axes: **calibration accuracy**,
**threshold integrity**, **evidence traceability**, and **filed-artifact
preservation**. This is a recorded-outcome checkpoint, not completion of the
amended loop, a new round admission, or independent promotion verification.

Merged source shards: `reports/round-14/retro/r8.md`,
`reports/round-14/retro/r9.md`, `reports/round-14/retro/r10.md`, and
`reports/round-14/retro/r11-13.md`. Their read-only reproduction commands were
executed concurrently on **2026-10-18T00:03:02Z**, all exiting **0** (M1 below).
The source-map and number-audit findings in
`reports/round-14/retrospective-audit-C07.md` and
`reports/round-14/retrospective-audit-C08.md` are incorporated as qualifications,
not treated as independent approval of this final text.

## Recorded final states and counting boundary

**Four admitted, one rejected, one operator-skipped:** rounds 8, 9, 10 and 12
are admitted; round 11 is rejected; round 13 is skipped. The filed claim flags
are **14 passed / one failed**, but those flags are not a literal-conformance
score: the strict qualifications below remain failures or gaps even where a
historical harness recorded PASS. Counts come from M1 and the read-only M2
control, not new invocations of the historical validators.

| round | final recorded state | filed claim flags | final-state evidence |
|---|---|---|---|
| 8 | admitted | F/O/D PASS | `reports/round-8/validation.json`; `SCORECARD.md:100-122`; `LOG.md:2921-2951` |
| 9 | admitted | F/O/D PASS | `reports/round-9/validation.json`; `SCORECARD.md:130-158`; `LOG.md:2954-2985` |
| 10 | admitted | C/coverage, F, O PASS | `reports/round-10/validation.json`; `SCORECARD.md:160-182`; `LOG.md:2987-3008` |
| 11 | rejected | D/O PASS; F FAIL | `reports/round-11/validation.json`; `SCORECARD.md:184-205`; `LOG.md:3010-3029` |
| 12 | admitted | C/calibration, O, A PASS | `reports/round-12/validation.json`; `SCORECARD.md:207-229`; `LOG.md:3031-3046` |
| 13 | skipped, by operator | D/C/O unexecuted and deferred | `reports/round-13/claims.json`; `LOG.md:3065-3080` |

The final state is not the declaration's `declared-before-dispatch` field or an
in-flight report draft. Baselines come from each `claims.json.baseline_revision`;
short declaration/preparation labels in old LOG/SCORECARD prose are not alternate
baselines. The resolved baseline/declaration distinction for round 10 is in
`reports/round-12/defects/fix-11.md`, with its commit-resolution controls.

Each round section below names its historical counting command and date. These
commands identify the filed measurement, **not instructions to rerun a writer
in the live lane**. Source counts were re-extracted by M1; M2 additionally checks
receipt bytes against their admission/closure revisions. Current-tree rechecks,
source-truth judgments, worker dispatch traces, and historical final states are
different evidence channels.

## Round 8 — admitted, with a strict replay qualification

Declaration: `reports/round-8/claims.json:11-31`. Historical counting command,
**2026-10-17**: `python3 reports/round-8/run-validation.py`; D also names
`python3 tools/d2-typed-labels.py --selftest`. Results below are the filed
`reports/round-8/validation.json` measurements, re-extracted by M1.

| claim | unchanged threshold | honored-or-failed disposition |
|---|---|---|
| F / freshness | Every residual has a passage/access-failure receipt; at least eight have substantive passages; preserve passage/whole-claim separation and raw labels. | **Honored at receipt/passage scope:** 15/15 receipts and 15 passage-bearing residuals; 215 harness passage keys. Reconciliation remains 11 partial-support / four unresolved, not 15 confirmed whole claims. Negative controls reject missing coverage, false distinctness, erased scope separation and missing raw labels. |
| O / operability | Benign duplicates accepted without inflation; real identity collisions rejected; required legacy defects repaired or quarantined with controls; battery/craft stay green. | **Honored for the bounded contract:** 14/14 harness controls; 20 inventory rows with 11 required review IDs covered. The audit's 12/12 is wrong, not a smaller final result. `reports/round-14/errata/r8-audit-count.md` reproduces 14/14 and rejects 12/12 without rewriting the audit. |
| D / depth | Typed-label/era-material/rank capability, positive and malformed controls, deterministic D2, no-drift frozen replay, documented decision/capability rows. | **Filed PASS; strict repaired-live-tree replay clause not fully honored.** The tool demonstrates 39/39 selftests and deterministic assembly, but the accepted replay restores historical gate bytes and reproduces the old manifest 7/7. The live-reference leg exits 2 with seven unevaluable rows; no round-8 manifest exists in that measurement. Historical compatibility is not a new frozen verdict over the repaired typed flow. |

The replay qualification is explicit in
`reports/round-8/validation.json` → `claims.D.measurement.replay_frozen` and
`reports/round-8/depth/test-replay.md:9-20,104-121,171`; that report's C1–C5
controls detect gate, snapshot and output tampering. The later round-12 recount
in `reports/round-12/recount/r8-1.md` examined a clobbered/later-tree receipt
before restoration; its failed D result must not be mistaken for the restored
admission receipt's boolean. Neither channel authorizes an unqualified live-tree
no-drift claim. New-generation wired typed replay is later round-11 work.

## Round 9 — admitted, with a baseline-layout/default-root gap

Declaration: `reports/round-9/claims.json:11-31`. Historical counting command,
**2026-10-17**: `python3 reports/round-9/run-validation.py`; D also names
`python3 tools/assemble-culture-d3.py --check`. Results are filed measurements
in `reports/round-9/validation.json`, re-extracted by M1.

| claim | unchanged threshold | honored-or-failed disposition |
|---|---|---|
| F / freshness | At least two escalated receipts per residual; at least two residuals move to primary/scholarly partial-support-or-better; preserve raw labels and deeper limits. | **Numeric floors honored:** 12 hunter JSON documents, three strategies for each of four residuals; all four reconcile to partial-support, none to whole-claim support. Three verifier documents cover all four residuals. Earlier snapshots missing the combined F01/F02 verifier are not the final state: it exists in the admission commit. |
| O / operability | Standard-conforming committed baselines for all seven gates; battery validates every baseline and rejects tampering; selftests green and no unexplained gate changes. | **Filed PASS; unqualified standard-complete default-runner after-state not honored.** Eight baseline files cover seven gates through the explicit three-root run, exit 0. The historical default finds five and exits 2, leaving myth and naming uncovered. The runner reports rather than fails this gap. Its tamper controls do not make the default discovery or old layout conformant. |
| D / depth | Delivered-tree deterministic D3 assembly, green coupling selftest, no-drift frozen expectation, demonstrated capability row. | **Honored as round-9 work:** repeated assembly exits 0 with identical output; coupling selftest and the D3 frozen call exit 0 with no findings or drift. This does not retroactively admit round 7 or establish an accepted lore transfer. |

`reports/round-14/retro/r9.md:24-59` preserves the distinction between receipt
documents and the harness's nested retrieval-unit counts. Its admission-blob
check confirms `reports/round-9/freshness/verify-F01F02.md` was present at close.
The historical battery gap is at
`reports/round-9/baselines/registry.md:168-175,239-242` and
`reports/round-12/defects/sweep-r9.md`.

The successor repair in `reports/round-14/fix-battery-roots.md` demonstrates the
plain default command exiting 0 after adding the preserved round-9 root, with
7/7 gates covered and eight pinned baselines; its selftest and planted omission /
tamper negatives are the controls. This is a documented discovery compatibility
exception, **not** relocation of filed baselines into the standard layout and
not retroactive fulfillment of round 9's unqualified wording.

## Round 10 — admitted, with classification and stale-fixed corrections

Declaration: `reports/round-10/claims.json:11-30`. Historical counting command,
**2026-10-17**: `python3 reports/round-10/run-validation.py`. Filed measurements
in `reports/round-10/validation.json` and the admission tracker are re-extracted
by M1; the tracker is read from its admission revision, not its new erratum key.

| claim | unchanged threshold | honored-or-failed disposition |
|---|---|---|
| C / coverage | At least ten sourced, gap-named entries; at least two in each thin partition; complete apparatus and decision records; index agrees with files. | **Honored:** 179 → 189 entries, additions linguistics 3 / myth-symbol 3 / culture-material 2 / verification 2. Actual author fragments are ten, not the receipt's inflated eleven: the extra count is an index updater. Ten still meets the unchanged floor. `reports/round-14/fix-index-classification.md` demonstrates the correction and rejects a missing-author false pass. |
| F / freshness | Every cited executable/counting command rerun with hash/verdict; registry matched; stale items genuinely fixed with evidence or documented with a reason. | **Filed PASS; frozen command coverage honored, particular fixed-status assertions failed against retained bytes.** The ledger has 192 rows, 36/36 required keys, and filed statuses 153 current / 29 stale-documented / ten stale-fixed. Two stale-fixed rows cite an unretained round-8 runner repair; another documented-stale row still describes that repair. Their effective correction is stale-documented, not a retained fix. |
| O / operability | Every finding in the four named review files dispositioned with controls or documented reasons; no undispositioned finding or green regression loss. | **Finding-disposition contract honored:** 24 rows, 18 fixed-with-control / five wont-fix / one wrong / zero pending, with four verifier files. The receipt's no-regression reading is indirect through the ledger, not a fresh battery run. The original tracker summary omits verifier 3, not its actual execution; the append-only correction has a verifier-set and original-row-preservation control. |

Later-tree command coverage of 36/38 reflects later SCORECARD additions, not a
new round-10 admission result (`reports/round-12/recount/r10-2.md`, `r10-4.md`).
The stale-fixed conflict is corrected, with retained-byte/AST and planted-status
controls, in `reports/round-14/fix-status-conflicts.md`: the original runner lacks
`gate_blob_for_pin`, so a fix-report path alone cannot prove a delivered repair.
The filed statuses remain historical; they are not rewritten by this summary.

`reports/round-14/errata/r10-draft-status.md` reconciles the draft's eight-entry
SHONEN bullet with ten actual additions, retaining the in-flight draft and its
floor failures. `reports/round-14/fix-tracker-pointer.md` carries the verifier
erratum and controls. `reports/round-14/fix-runner-hash.md` pins the retained
final runner while leaving the draft's unrecovered prefix explicitly to-verify.
An in-lane draft does not prove a fleet final report absent. External filing
attestations are cited through lane-local evidence, not freshly verified here.

## Round 11 — rejected; D/O verified, F failed as declared

Declaration: `reports/round-11/claims.json:11-32`. Historical counting command,
**2026-10-17**: `python3 reports/round-11/run-validation.py`; D also names
`python3 tools/assemble-d2.py --check`. Filed results are in
`reports/round-11/validation.json`; M1/M2 and the independent round-12 recount
separate the populations instead of reproducing the ambiguous old equation.

| claim | unchanged threshold | honored-or-failed disposition |
|---|---|---|
| D / depth | Wired typed D2 flow; translated labels off the sound channel; owed forms retained as named holds; exact expected set; frozen replay; D2/D3/battery checks green. | **Honored for the named flow:** exact 16 finding tokens comprise 15 holds plus one note, never 16 holds; ten translated-label phonology artifacts removed. Assembly/projection checks pass and the new manifest reproduces 11/11. Channel-smuggling, silent-form-drop and hold-laundering negatives are caught. Open holds remain design debt. |
| O / operability | Live D2/D3 handoff exercise validates in isolation; 16/16 fields, 20/20 glossary entries, contract references, frozen baseline and positive/malformed controls. | **Honored structurally:** exercise and settled selftest exit 0 with the required shape and no findings. The draft's earlier missing-component crash is not the final result. This gate is not a semantic-transfer or bilateral-acknowledgment decision. |
| F / freshness | At least 15 one-to-one rechecks; at least 95% hash-stable; every drift dispositioned; at least five independent audit reruns. | **FAILED AS DECLARED:** 192 receipt rows, 189 byte-comparable, 147 hash-stable; 147/189 = 0.777777… (77.7778%, diagnostic 0.778), below 0.95. The all-row channel is 147/192 = 0.765625 (76.5625%, summary 0.7656), also below 0.95. Coverage, causes and audit sampling do not replace the failed stability clause. |

The comparable population contains 42 hash-unstable rows; three prose-control
rows have no comparable hash. Thus 42 + 3 = 45 unstable/unreproducible cases,
all dispositioned. The validator's 46 drift rows additionally include row 101:
its stdout hash is equal but its exit changes 0 → 2 because scratch inputs are
gone (`reports/round-11/recheck/row-101.json:11-22`). A stable stdout digest is
neither stable execution semantics nor proof of an unchanged filed tree.

The filed runner recognizes nine independent audit reruns, exceeding five;
`reports/round-11/recheck/audit.md:124-130` separately documents 17 sampled
re-runs. Those are different reporting instruments; neither sample count is a
new stability denominator. Independent denominator and exact-set controls are
in `reports/round-12/recount/r11-1.md`, `r11-2.md`, `r11-4.md`, and
`reports/round-12/recount/dispositions.md:77-79`.

The draft's 149 stable / 43 unstable is a dated in-flight census, not the
settled 147 / 45. `reports/round-14/errata/r11-draft-census.md` carries the
read-only census/pin controls and preserves the rejection. Round 11 remains
**REJECTED**; a later audit, useful D/O capability, denominator correction or
new operator rule does not retroactively admit it.

## Round 12 — admitted audit, not accepted handoff

Declaration: `reports/round-12/claims.json:11-29`. Historical counting command,
**2026-10-17**: `python3 reports/round-12/run-validation.py`. Measurements are
the filed `reports/round-12/validation.json`; historical ledger counts below use
the round-14 declared baseline, before the new exposure erratum (M2).

| claim | unchanged threshold | honored-or-failed disposition |
|---|---|---|
| C / calibration | Recount every prior counting-command requirement; exact match or licensed cause for every discrepancy; independently reproduce round-11 F failure. | **Filed instrument PASS, with execution-scope qualification:** 89 rows = 12 exact matches + 77 dispositions; 51 normalized source-command requirements, none reported missing. The 61 integrator coverage rows inside those dispositions are not 61 exact replays: some lack prior values or contain non-executable descriptive commands with 127/n/a outcomes. The failed F result is independently reproduced; coverage/disposition is not universal literal executability or truth certification. |
| O / operability | Consolidate every defect; bounded fixes with controls or owner-bearing round-14 routing; regressions green. | **Queue contract honored; headline count inconsistent:** the filed 15-row ledger and validator have eight fixed-with-control / seven routed, while LOG/SCORECARD say seven fixed / eight routed. Restoration and actual regressions have evidence; prevention and default-root conformance were not established by restoration/custom-root runs. Preserve both historical channels and the unchanged eight-item round-14 assignment. |
| A / adjacency | Audit new entries, contract and province; report rather than absorb bleed. | **Audit/disclosure recorded; entry-receipt provenance incomplete.** Ten entry verdicts and zero unfiled bleed are recorded. All original entry pointers name an absent `entries.md` in the adjacency directory. The A11–A12 scribe directly reviewed ten sources, but that is not the missing assigned A01–A04 receipts. Handoff semantics are explicitly REJECTED despite passing envelope shape. |

The historical seven aggregate routed IDs are R8-AUDCNT, R9-BATROOT, R10-F04,
R10-F05, R10-IXCLS, R10-STATCONFL and R10-RUNHASH. R11-DRAFT is already
fixed-with-control in that ledger, while routing prose still carries final-report
and census-integration notes. The owner-note headings, ledger rows and declared
round-14 eight-item worklist are distinct denominators. An explicit integration
crosswalk is required; this retrospective neither drops a task nor invents an
eighth historically routed row. A new round-14 exposure entry does not become a
sixteenth original round-12 defect.

The missing receipt pointer is disclosed by M1/M2 using
`reports/round-12/adjacency/ledger.json`; it is not repaired here or hidden by an
invented file. `reports/round-12/adjacency/A11-A12-handoff.md:13,19-26,44-59`
contains the real, separately attributed source-boundary review. A permitted new
pointer/evidence correction remains with the integrator.

`reports/round-12/adjacency/A11-A12-handoff.md:7-17,69-72` and
`reports/round-12/adjacency/contract.md` reject transfer for missing per-claim
uncertainty, aggregate D2 coupling, and pending bilateral acknowledgment. The
16/16-field, 20-entry shape pass is not acceptance, canon, rights clearance or
lore acknowledgment. An admitted audit can honestly record a rejected handoff.

## Round 13 — operator-skipped, all claims deferred

Final authority: `LOG.md:3065-3080`, superseding the earlier resume plan.
`reports/round-13/claims.json:11-30` is retained as a declaration, not a result.
Its counting command, declared on **2026-10-17**, is a Python invocation of the
round-local `run-validation.py`; neither that runner nor a validation receipt
was delivered in the inspected round directory (M1). This is an absent declared
deliverable, not an executable evidence pointer. The operator record reports
two interrupted attempts and zero output files; this is operator-reported
execution history, not an inference that the provider failed or a newly
verified runtime dispatch trace.

- **D / depth:** deterministic NON-CANON D4 through the typed pipeline, exact
  holds/frozen replay and preserved D2/D3 — **unexecuted/deferred**, not honored
  and not empirically falsified; moved to a loop-2 build.
- **C / coverage:** status/date/command receipts for all 94 civilization entries
  — **unexecuted/deferred** to GLM rounds 15–16. The 94 is a declared target,
  not a measured completion count or 94 independently certified civilizations.
- **O / operability:** handoff-v2 uncertainty and claim-to-record links, semantic
  re-audit/pass-or-owned-gaps, preserved 16/16 + 20/20 shape —
  **unexecuted/deferred** with the map to GLM rounds 15–16.

No completed-round or capability credit is assigned to the skipped round.
Integration remains round 14 and the amended loop still includes rounds 15–16;
this six-record checkpoint is not a claim that the full amended loop is done.

## Operator amendments and execution-evidence limits

The shorthand “2 operator amendments” at `reports/round-14/claims.json:28` is
meaningful only for the **two structural schedule amendments**, excluding the
separate provider-only change. There are **three amendment commits in total**.
M3 verifies their identities and dates without inferring runtime dispatch from
requested models:

1. `51e590100f7bb3c2d30f5cc9e91a0ad981505179`, 2026-10-17T20:48:21-03:00:
   add two GLM rounds per loop; interrupted round-13 state recorded.
2. `94377884a78a73ad5396acb0d5f48a539a7a0448`, 2026-10-17T20:48:44-03:00:
   designate round 19's DeepSeek build on Hyper, a provider amendment.
3. `3dba77a722c6a2e885447a47971205fd97c11605`, 2026-10-17T20:55:04-03:00:
   cancel expand rounds, skip round 13, pin the end-of-loop GLM rounds to
   16-worker Flash-low/MAX; handoff-v2/civ-map and D4 scopes deferred.

Sources: `LOG.md:3048-3080`, `SCORECARD.md:239-255`, and the commit subjects.
Requested worker/model fields are not actual launch, concurrency, completion or
wire-model receipts. Operator-reported completion shortfalls and round-12
integrator coverage are not proof of additional autonomous worker completions.
The round-11 availability-trace gap remains named in
`reports/round-12/defects/routed.md:98-104`.

## Conformance-defect class table

These **six classes** are a retrospective taxonomy, not six atomic incidents or
a replacement for the fixed/routed ledger. Availability and resource handling
share one execution-environment class; count/schema errors and report-status
errors are separated. Each disposition names a control or an explicitly open
prevention/follow-up obligation.

| class | loop-1 evidence | disposition and control |
|---|---|---|
| K1 — scope confinement / out-of-lane writes | Round-9 V09 fragment landed at the fleet parent. The stray AccessDenied PDF is explicitly unattributed in `reports/round-9/adjacency.md:191-228`, despite aggregate prose grouping both as lane cleanup. | **Historical relocation documented**, not two proven worker breaches. OOL-9a in the filed round-12 ledger carries the relocation/scope-check control. **Dispatch-time prevention remains open:** bind cwd/output root and reject a planted out-of-root destination, as routed at `reports/round-12/defects/routed.md:18-24`. A later clean snapshot does not erase the breach. |
| K2 — filed-artifact integrity / receipt clobber and post-filing mutation | FRR-10, FRR-12a/b; round-11 live rechecks called validators that write their own receipts; the index-updater addendum is a separate post-filing mutation (`reports/round-11/adjacency.md:39-77`). | **Receipt restoration verified**, not root-cause prevention: M2 compares the restored receipts to admission blobs. `reports/round-14/guard/scribe.md` and the appended FRR-14-EXPOSURE entry document unguarded legacy writers. Successor guard selftest, exact-override/default-refusal and actual runner-boundary controls belong to D; do not infer their green status from this summary. Historical writers must stay isolated or unexecuted. |
| K3 — availability, dispatch provenance and execution resources | Round-10 pre-launch 402 attempts; late/capacity-limited seats; round-11 dispatch-trace gap; round-9 `/tmp` inode exhaustion (`reports/round-10/availability-attempt-1.json`, `reports/round-9/adjacency.md:300-304`, routing trace item above). | **Failed launches recorded; authorized retry/operator amendments distinguished from provider failure.** Attempt files are controls for those failures, not proof of successful later wire identity. In-lane scratch with `TMPDIR=$PWD/.scratch` bounds scratch writes. Machine cleanup and complete contemporaneous request/launch/completion/fallback traces remain owner tasks; no cleanup or missing execution record is fabricated here. |
| K4 — baseline layout / default-root conformance | Round-9 standard/layout/default-root divergence: explicit roots cover all gates while the default misses myth/naming (`reports/round-9/baselines/registry.md:168-175,239-242`). | **Applied-with-control for successor discovery**, documented in `reports/round-14/fix-battery-roots.md`: default invocation green, required-root omission caught, snapshot tamper remains unevaluable. Old layout remains a compatibility exception, not rewritten or retrospectively certified standard-complete. Battery pin validation is not frozen-verdict replay. |
| K5 — schema, counting and measurement-contract defects | Round-8 12/12 versus 14/14; round-10 index-updater inflation; round-11 mixed denominators, prose-only/truncated commands and volatile hash surfaces (`reports/round-12/recount/dispositions.md`). | **Bounded count corrections controlled:** `reports/round-14/errata/r8-audit-count.md` rejects 12/12; `reports/round-14/fix-index-classification.md` rejects updater inflation and a missing-author false pass; `reports/round-14/errata/r11-draft-census.md` verifies both populations and rejection. Future freshness measurement policy remains operator-pending; disposition never turns an unstable/non-executable row into a stable success. |
| K6 — report/status/provenance reconciliation | In-flight drafts versus final receipts; stale-fixed claims after reversion; missing verifier pointer; unresolved draft runner prefix; baseline/declaration shorthand; missing round-12 entry-receipt pointer; queue and amendment-count ambiguities. | **Documentation corrections carry controls**, not retroactive execution: round-14 draft/census errata, `fix-status-conflicts.md`, `fix-tracker-pointer.md`, `fix-runner-hash.md`, plus round-12 `fix-11.md`. Their read-only byte/role/status comparisons and planted negatives preserve old values. M2/M3 preserve queue/amendment counting boundaries. **Still open:** the missing assigned entry receipt/pointer, external-final-report content verification, and any prevention obligation not covered by those bounded fixes. |

The new tracker erratum key and the exposure-ledger entry are explicit permitted
additive corrections, not evidence that every historical file is byte-identical.
`reports/round-14/fix-tracker-pointer.md` and
`reports/round-14/guard/scribe.md` reconstruct the original bytes outside their
insertions; `reports/round-14/scope.md` independently distinguishes additive
preservation from whole-file equality. This scribe changes none of those files
and does not normalize their non-green broad-tree sentinels into passes.

## Restated freshness-threshold question for the operator — pending

**Which preregistered, revision-bound instrument should govern future freshness
claims during build rounds: raw byte-hash stability on a quiet pinned tree, a
declared normalized semantic/exit comparison, or a separately measured,
change-aware stability budget? What threshold and denominator should it use?**

Loop-1 data motivating the decision, not an argument for retroactive admission:

- Round-8/9 freshness claims measured scoped retrieval and residual movement;
  their successful floors did not certify whole historical claims.
- Round 10 built a 192-row command ledger while the corpus and SKILL changed;
  36 frozen citation keys were covered, but later legitimate work changes the
  surface and some claimed repairs were reverted.
- Round 11 covered all 192 rows; 147/189 comparable = 77.7778% and
  147/192 all-row = 76.5625%. Both fail the unchanged 95% threshold. All causes
  named does not mean all bytes stable. Row 101 additionally demonstrates
  equal stdout hashes with changed exit/stderr.
- The independent round-12 recount separates legitimate change, environmental
  output and defects. Battery timing/random mirror paths, absolute inventory
  roots and newline capture conventions can change hashes without a changed
  gate verdict; prose/truncated commands cannot support exact replay. The
  89-row match/disposition audit has only 12 exact matches, not 89.

Before a future freshness claim is dispatched, the operator-selected contract
must name the baseline/evaluation revisions and measurement window; command
identity and count unit; comparable/no-hash population; hash streams including
stderr and exits; any normalization; treatment of legitimate changes; and the
failure threshold. It also needs negative controls for a real semantic
regression, an exit-only drift, a missing/non-executable command, and a
receipt-writing side effect. Tree preservation must be checked independently of
stdout stability. Normalization must not erase meaningful findings or failures.

**No option or new threshold is selected here.** Round 11 stays rejected under
its original declaration. Freshness axis-move claims stay paused pending the
operator ruling (`SCORECARD.md:201-205`; `LOG.md:3021-3029`). Neither a quiet-tree
assumption nor a prospective semantic metric repairs historical conformance.

## Merge verification and reproducible controls

### M1 — execute the four shard read-only reproduction blocks

Executed on **2026-10-18T00:03:02Z**, all four exit codes **0**. This re-extracts
the historical measurements and checks the shard's preserved receipt/pin facts;
it does not run their historical counting commands or perform source retrievals.

```sh
export TMPDIR=$PWD/.scratch
export PYTHONDONTWRITEBYTECODE=1
python3 - <<'PY'
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
import re, subprocess
paths = ['reports/round-14/retro/r8.md', 'reports/round-14/retro/r9.md',
         'reports/round-14/retro/r10.md', 'reports/round-14/retro/r11-13.md']
def check(path):
    blocks = re.findall(r'```sh\n(.*?)\n```', Path(path).read_text(), re.S)
    assert len(blocks) == 1, (path, len(blocks))
    run = subprocess.run(['bash'], input=blocks[0], text=True,
                         capture_output=True, timeout=60)
    return path, run.returncode, run.stdout, run.stderr
print('measured_at_utc=' + datetime.now(timezone.utc).isoformat())
with ThreadPoolExecutor(max_workers=4) as pool:
    results = list(pool.map(check, paths))
for path, code, out, err in results:
    print(path, 'exit', code)
    print(out, end='')
    print(err, end='')
assert all(code == 0 for _, code, _, _ in results)
PY
```

### M2 — final-state, denominator, original-queue and receipt controls

Executed directly from this document on **2026-10-18T00:05:35Z**, exit **0**:
state totals 4/1/1; filed claim flags 14/1; round-11 total/comparable/stable/no-hash
192/189/147/3 with both ratios below 0.95; original round-12 queue 15 entries,
eight fixed / seven routed. All five validation receipts equal their named
admission/closure revisions. The original entry-receipt pointer gap is detected
and reported, **not** accepted as a valid receipt or represented as fixed.

This control reads the original round-12 ledgers at the declared round-14
baseline so appended round-14 corrections do not inflate historical counts.
No historical validator is imported or run.

```sh
export TMPDIR=$PWD/.scratch
export PYTHONDONTWRITEBYTECODE=1
python3 - <<'PY'
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import json, re, subprocess
load = lambda path: json.loads(Path(path).read_text())
base = load('reports/round-14/claims.json')['baseline_revision']
revisions = {8: 'e1694bad6ac96aca45a11ca5746582b275929355',
             9: '9dc18ec1339bffd6f81e74f1a5742464ef578749',
             10: '94ca098b8ab03be52ec80f6925538e5e2c0ed327',
             11: 'a3f6fcef2d92a1099581140c81d4264e9a4e2aa3',
             12: '44070b4a6038f54e78d8d5be551e549fe202b0ee'}
vs = {n: load(f'reports/round-{n}/validation.json') for n in revisions}
states = {n: 'admitted' if v['acceptance_checks_passed'] else 'rejected'
          for n, v in vs.items()}
assert '**Round 13 status:** operator-skipped before any work landed' in Path('LOG.md').read_text()
states[13] = 'skipped'
assert states == {8: 'admitted', 9: 'admitted', 10: 'admitted',
                  11: 'rejected', 12: 'admitted', 13: 'skipped'}
flags = Counter(v['passed'] for d in vs.values() for v in d['claims'].values())
assert flags == {True: 14, False: 1}
for n, revision in revisions.items():
    p = f'reports/round-{n}/validation.json'
    assert Path(p).read_bytes() == subprocess.check_output(['git', 'show', f'{revision}:{p}']), p
rows = [load(p) for p in Path('reports/round-11/recheck').glob('row-*.json')]
comparable = [r for r in rows if re.fullmatch('[0-9a-f]{64}', r.get('new_hash') or '')]
stable = sum(r['stable'] is True for r in rows)
assert (len(rows), len(comparable), stable) == (192, 189, 147)
assert sum(r['stable'] is False for r in rows) == 45
assert all(r.get('drift_cause') for r in rows if r['stable'] is False)
assert len(vs[11]['claims']['F']['measurement']['drift_rows']) == 46
assert stable / len(rows) < .95 and stable / len(comparable) < .95
queue = json.loads(subprocess.check_output(['git', 'show', base + ':reports/round-12/defects/ledger.json']))['entries']
statuses = Counter(r['status'] for r in queue)
assert len(queue) == 15 and statuses == {'fixed-with-control': 8, 'routed': 7}
a = json.loads(subprocess.check_output(['git', 'show', base + ':reports/round-12/adjacency/ledger.json']))
entry_receipts = {r['filed_path'] for r in a['entries']}
assert len(a['entries']) == 10 and len(entry_receipts) == 1
assert not any(Path(p).exists() for p in entry_receipts)
print('measured_at_utc=' + datetime.now(timezone.utc).isoformat())
print('states', dict(Counter(states.values())), 'filed_claim_flags', dict(flags))
print('r11 total/comparable/stable/no_hash', len(rows), len(comparable), stable, len(rows)-len(comparable))
print('r11 comparable/all ratios', stable / len(comparable), stable / len(rows))
print('original_r12_queue', len(queue), dict(statuses))
print('r12_entry_pointer_gap', sorted(entry_receipts))
print('validation_receipt_revision_equality=PASS; no historical runner executed')
PY
```

### M3 — amendment identity control

Executed on **2026-10-18T00:01:31Z**; all three commit queries exited 0 and
returned the subjects/dates in the amendment section. Two are structural
schedule changes; one is provider-only. Command:

```sh
export TMPDIR=$PWD/.scratch
python3 - <<'PY'
from datetime import datetime, timezone
import subprocess
print('checked_at_utc=' + datetime.now(timezone.utc).isoformat())
for rev in ('51e590100f7bb3c2d30f5cc9e91a0ad981505179',
            '94377884a78a73ad5396acb0d5f48a539a7a0448',
            '3dba77a722c6a2e885447a47971205fd97c11605'):
    print(subprocess.check_output(['git', 'show', '-s',
          '--format=%H %cI %s', rev], text=True).strip())
PY
```

The parent owns SCORECARD/LOG integration, the routed-resolution crosswalk,
guard and regression acceptance, actual dispatch evidence, and authorized final
filing. Their overall round-14 results are not asserted by this retrospective.
