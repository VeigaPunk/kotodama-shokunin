# kotodama — round 14 fleet report (DRAFT BODY — integrator finalizes)

**Scribe X04; evidence cutoff 2026-10-18T00:11:54Z.** This lane-local report
is an integration draft, not an acceptance receipt, an admission, or independent
promotion verification. Bounded fix/regression results below are attributed to
their dated worker receipts. Pending items are neither failures inferred from
absence nor completed work. The integrator supplies the resolver, settled
receipt, carrying work revision, dispatch trace, LOG/SCORECARD landing, and
authorized final filing; no round-14 O/D/C admission is asserted by this draft.

## Declaration and scope

Axes: **O / operability**, **D / depth**, **C / calibration**. The declaration
is `reports/round-14/claims.json`; allocation is `reports/round-14/targets.json`.
Declared baseline: `926c86f8be3cc9307f8f10dce55768c290b6f94d`.
Declaration revision: `a7bc9e9ff05a57515c5efaaa7e50116eb30938ff`, observed with
`git show -s --format='%H %s' HEAD` on 2026-10-17T23:58:49Z. These are different
metadata fields; the declaration revision must not be relabeled the baseline.

The requested route is `openai-codex/gpt-6.1-sol`, max effort, with 32 workers
(`claims.json`, 2026-10-17). That is a request, not proof of actual wire-model
identity, concurrent worker count, launch/completion totals, or fallback.
Round-14 dispatch evidence remains to verify; round-10 availability records
cannot supply a missing round-14 trace.

This is loop 1's integrate round. The current operator amendment, recorded in
`LOG.md` under “Regimen amendment 3” and `SCORECARD.md` under “Planned”, cancels
expand rounds and places the loop-1 GLM work in rounds 15–16. Round 13 is
**operator-skipped**, not admitted or rejected: its D4, civilization-map, and
handoff-v2 declarations are deferred, not delivered. Earlier descriptions of
the superseded expand schedule remain historical.

Only this draft is this scribe's assigned output. No historical validator was
invoked, no earlier-round artifact was edited by this scribe, and no commit or
push was performed. This is not an assertion that other workers made no
append-only additions. `PROVINCE.md` and lore's canon/acknowledgment authority
remain in force.

## Claims — required result versus observed evidence

| claim | required result, unchanged | assessment at this cutoff |
|---|---|---|
| O / operability | Every declared routed item has an applied-with-control or evidence-backed documentation disposition in `reports/round-14/routed-resolution.json`; default battery coverage and battery/craft/D2/D3 regressions are green. | **Bounded fixes, independent reviews, and dated regressions present; resolver/settled receipt pending.** Both were absent at the 00:11:54Z read-only dependency probe. |
| D / depth; `receipt-guard` | Importable guard and CLI refuse an already-committed receipt overwrite with exit 3 and a named diagnostic unless `REFRESH_RECEIPTS=1`; selftest proves both modes; round-14+ runners use it; append-only exposure erratum, with rounds 8–11 runners unchanged. | **Guard, exposure erratum, historical replays and actual production-main controls present.** Earlier red attempts and tested revisions stay explicit. The runner has changed since the last clone control; rebind the delivered source and integrated result before admission. |
| C / calibration | Loop-1 retrospective names every per-round final state and claim threshold, conformance classes/dispositions, and the round-11 freshness question; SCORECARD receives a summary row. | **Consolidated retrospective and hash-bound C07/C08/consistency reviews present; shared summary landing pending.** No new threshold or retroactive admission is authorized by this report. |

Declared counting commands: `python3 reports/round-14/run-validation.py` for
O/C and the integrated D check; `python3 tools/harness/receipt_guard.py
--selftest` for D. They have **not been run by this scribe**. No successful
settled round-14 validator result is asserted here.

## Operability — routed dispositions and controls

### Preserve the denominator, reconcile the source records

The declaration requires **eight** routed dispositions. A read-only JSON census
on 2026-10-17T23:58:18Z found **15** entries in the filed round-12 defect ledger,
with **seven `routed`** and **eight `fixed-with-control`**. The filed round-12
validation receipt itself records those same ledger values, whereas
SCORECARD/LOG summarize seven fixes and eight routes. The routing prose also
has a broader checklist. These are distinct channels, not interchangeable
counts. The command is E1 below; source locations are
`reports/round-12/defects/ledger.json:5-134` and
`reports/round-12/validation.json` → `claims.O.measurement`.

The round-14 resolver must give an explicit crosswalk to the declared eight-item
queue, preserving the historical seven-row status census rather than silently
altering the requirement or rewriting the source ledger. In particular,
`R11-DRAFT` already has a filed `fixed-with-control` pointer disposition; this
draft does not invent it as an eighth still-open ledger row.

The landed correction records cover the seven literal routed IDs and the
additional round-11 report-census work package. These are attributed bounded
results, not yet the missing consolidated resolver or whole-round admission:

- `R9-BATROOT` — **applied-with-control**,
  `reports/round-14/fix-battery-roots.md`. The actual default command
  `python3 tools/check-gate-battery.py` changed from exit 2 at
  2026-10-17T20:57:35-03:00 to exit 0 at 20:58:44-03:00: **7/7 gates covered,
  eight pins, no uncovered gate**. The retained round-9 root is now a default
  discovery compatibility exception, not a retroactive standard-layout repair.
  The default-root selftest detects the planted old root omission; the real
  isolated tamper CLI detects `BASELINE-TAMPERED`, exit 2, at 20:59:15-03:00.
  Baseline bytes and old runners stay unchanged.
- `R8-AUDCNT` — **resolved-by-documentation with control**,
  `reports/round-14/errata/r8-audit-count.md`. On
  2026-10-17T23:57:57+00:00, `python3 tools/harness/r8_checks.py --selftest`
  reproduces **14/14**, exit 0; the in-memory negative rejects the audit's
  **12/12** pair. Admission-blob and protected-hash checks preserve the audit
  and receipt. The corrected quotation is at
  `reports/round-8/operability/audit.md:57`.
- `R10-F04` — **applied-with-control**,
  `reports/round-14/fix-tracker-pointer.md`. Its 2026-10-17T23:58:18Z embedded
  control applies `fix-09.md` in a new tracker `errata` key; the old fields and
  raw finding rows reconstruct exactly. The effective verifier set equals the
  live set; omission, nonexistent-extra, and original-row mutation controls
  reject planted errors. `reports/round-14/verify-2.md` independently executes
  that exact control at 2026-10-18T00:00:21.798792+00:00, exit 0. A changed
  whole-file digest is expected and is not described as byte identity.
- `R10-F05` — **resolved-by-documentation**,
  `reports/round-14/errata/r10-draft-status.md`. The dated read-only control at
  2026-10-17T20:58:40-03:00 compares baseline-to-admission additions and both
  receipts: **ten entries**, partitioned **3/3/2/2**; the old **eight-entry**
  candidate fails. The draft/receipt remain filed. External final filing is
  supported only by the cited in-lane historical attestation; the fleet file's
  content/digest was not independently inspected by this scribe.
- `R10-RUNHASH` — **resolved-by-documentation**,
  `reports/round-14/fix-runner-hash.md`. Its delivered Control B ran on
  2026-10-17T23:59:30+00:00, exit 0, binding the current full runner digest
  `23d6dc09002fe18c46778ac57d2c34246ab970a9371e7382950ca737d4019b0e`
  and rejecting short/wrong/mutated bindings. The old draft prefix remains
  unrecovered and `to-verify`, not reconstructed from the current digest.
  Its earlier broad clean-tree assertion became red after the separate tracker
  append; that red observation is retained, not recast as whole-tree green.
- `R10-IXCLS` — **resolved-by-documentation with control**,
  `reports/round-14/fix-index-classification.md`. Its read-only AST/in-memory
  control at 2026-10-17T23:58:54+00:00, exit 0, reproduces legacy **11** author
  credits versus **10** actual authors; removing an author leaves a false
  legacy **10** but corrected **9**, below the unchanged **10** minimum.
  Extra updater/support names earn no author credit. This is an executable
  correction specification, not a patch to the filed round-10 runner.
- `R10-STATCONFL` — **resolved-by-documentation**,
  `reports/round-14/fix-status-conflicts.md`. Its fenced read-only control at
  2026-10-17T23:59:32.866130+00:00, exit 0, binds retained runner bytes and
  ledger positions; positive `stale-documented` is accepted and planted
  `stale-fixed` rejected. A reverted intermediate repair is not a retained fix.
- Round-11 census/report reconciliation — **resolved-by-documentation for the
  census**, `reports/round-14/errata/r11-draft-census.md`. C1 ran at
  2026-10-17T23:58:46Z, exit 0, preserving the separate settled denominators,
  input pins, and rejected verdict below. Its strict all-file C2 sentinel
  remained red after the concurrent tracker-key addition; C1 is not that
  broader integrity certification. Final-report/SHONEN filing is separate from
  census repair and from the source ledger's already-fixed `R11-DRAFT` pointer.

Baseline/declaration metadata is corrected by the separate append-only
`reports/round-12/defects/fix-11.md`, not by editing the old LOG entry.
Receipt preservation, output-root prevention, dispatch, the historical
post-filing fragment append, and final-filing observations in the raw routing
note still require named dispositions or follow-up. They are not silently erased
by the smaller work-package denominator.

### Regression evidence

`reports/round-14/regression.md` reports **13 actual commands, all exit 0**, from
2026-10-17T23:59:57.069778+00:00 through 23:59:58.190219+00:00, after the default
battery fix. Each command/date and exact stream hash is retained in that receipt:

- `python3 tools/check-gate-battery.py --selftest`: **29/29** controls. The
  no-override `python3 tools/check-gate-battery.py`: seven selftests pass,
  eight pins, all gates covered, no fail/unevaluable; preserved gate fixtures.
- `python3 tools/check-craft-exercise.py --selftest`: **10/10** tamper and
  **18/18** CLI; positive craft and report-backed positive calls also pass.
- `python3 tools/assemble-d2.py --selftest`: **42/42**; `--check` byte-identical.
  `python3 tools/d2-typed-labels.py --selftest`: **39/39**; `--check`
  byte-identical without waiving holds.
- `python3 tools/assemble-culture-d3.py --selftest`: **85/85**; `--check`
  byte-identical. `python3 tools/check-evidence-coupling.py --selftest` and the
  actual D3 packet call pass; domain holds and NON-CANON status remain intact.

The tested battery SHA-256 is
`7aa898d627fe361517d2942a0fe2b337f15d8cdc1fcb4061b394eee60f03d574`.
The regression owner's historical-path before/after hash census found no change
during that batch. This is a dated bounded regression result, not a claim that
all other workers' additions or later edits were covered.

The independent operability receipts are now present:
`reports/round-14/verify-1.md` re-executes the real default CLI at
2026-10-18T00:02:01.577773+00:00 and planted controls at 00:02:27.848986+00:00;
`verify-2.md` verifies tracker preservation; `verify-3.md` re-executes errata
and exact additive-byte reconstruction controls. `reports/round-14/verify-4.md`
records **18/18** real regression invocations, all exit 0, using its listed
`subprocess.run` commands in the 2026-10-18T00:02:26Z and 00:05:04Z batches.
Those include typed-adapter/pipeline selftests/checks and the actual frozen D3
call; its default battery call is separately covered by V01. Do not sum unlike
control families into a domain-quality score. The final acceptance runner has
its own command inventory and must measure the settled tree.

## Depth — receipt preservation at the writer boundary

The defect is a side effect, not merely a wrong exit status: running a historical
`run-validation.py` can write its own filed `validation.json` while the measured
stdout channel still appears stable. The mechanism and affected recheck rows
are documented in `reports/round-11/adjacency.md` §§1.3–1.4 and routed in
`reports/round-12/defects/routed.md:10-16`.

`tools/harness/receipt_guard.py` now provides importable `guard_receipt`,
`ReceiptGuardError`, and the `round_runner_main` wrapper plus a direct CLI.
It checks the exact path against HEAD rather than mutable index membership;
only literal `REFRESH_RECEIPTS=1` permits a committed write, and unsafe paths or
Git-status errors fail closed. The CLI is a permission probe, not a writer.
The final observed guard SHA-256 is
`d2297da4e6ceabb2eab84bb6e3beab16d82132aca0e313f0bdf21243304123a1`.

Executed evidence, attributed to the assigned owners:

- **Retain the red attempt:** `guard/scribe.md` §5 records
  `python3 tools/harness/receipt_guard.py --selftest` at
  2026-10-18T00:00:20Z, exit 1, **19/20** controls. A nested non-repository root
  was incorrectly accepted. This is an actual initial failure, not an inferred
  one. Its §7 follow-up on 2026-10-18T00:02:28Z reports the corrected hash above,
  exit 0, **45/45** controls, including exact override/default refusal.
- **Selective runner protection:** `guard/neg-04.md` and `guard/neg-05.md`
  execute the same miniature wired callback in a disposable clone with no
  override at 2026-10-18T00:01:24Z. A committed target exits **3** before the
  measurement sentinel and preserves bytes; a new uncommitted target exits
  **0** and writes the exact intended payload. Their combined **14/14**
  assertions use the earlier `82eec760…` implementation; they are not silently
  rebound to the later guard hash.
- **Actual unchanged historical writers:**
  `reports/round-14/guard/retro-tests.py`, run from
  2026-10-18T00:02:43.159342+00:00 through 00:02:57.054385+00:00, exits **0**,
  **12/12** controls on the final guard hash. Its `retro-tests.json` and
  `retro-tests.md` show round-8 admission and round-9 filing clones: default
  wrapper refusal before entry; unguarded legacy writes that really change
  the clone's receipt; literal-1 authorized writes; subsequent dirty-receipt
  refusal; unchanged runner bytes. The round-9 control uses its actual filing
  revision because that round does not exist at the earlier round-8 revision.
  No live historical writer is executed.
- **Exposure erratum:** the new `FRR-14-EXPOSURE` entry in the round-12 defect
  ledger and `reports/round-14/guard/scribe.md` §3/§7 preserve the original
  **15** entries while documenting the additional exposure record. Its dated
  read-only control on 2026-10-18T00:01:27Z confirms **four unguarded legacy
  runners**, **eight unchanged runner/receipt paths**, and restored admission
  receipts. Restoration is not retroactive protection.
- **Real production-main controls:** `guard/neg-04.md` and `guard/neg-05.md`
  preserve the initial first-run NameError, then demonstrate actual refusal
  and publication in fresh clones. Their final batch at
  **2026-10-18T00:07:03Z** runs
  `R14_NEG_FIXTURE=production-final R14_NEG_OUTPUT=production-final-results.json PYTHONDONTWRITEBYTECODE=1 python3 .scratch/r14-d04-d05/run-production-negatives.py`
  with in-lane TMPDIR. The real `main([])`, retargeted only in memory to an
  existing committed fixture receipt, exits **3** before measurement scratch
  and preserves the receipt. The real first-run CLI writes a valid receipt
  and returns normal **acceptance exit 1**, not a crash or a false green
  admission, on the incomplete copied round. Combined assertions are
  **14/14**, aggregate exit **0**. Tested runner SHA-256:
  `11a1bc71011f16cf4371a15b297355a05419226659bb8d1fb1c70c5aa836d744`;
  guard is the final hash above. Later runner edits require rebinding; this
  does not establish acceptance for an untested successor revision.

The guard is cooperative writer preflight, not a sandbox, filesystem lock, or
race-proof guarantee. Filed rounds 8–11 stay deliberately unwired; direct live
execution remains unsafe. The opt-in does not authorize refreshing historical
receipts under this round's preservation rule. Final guard/runner source
bindings, independent receipts and integrated acceptance remain closeout work.

## Calibration — loop-1 final states, not draft snapshots

`reports/round-14/loop1-retrospective.md` has landed with explicit per-claim
honored-or-failed dispositions, rather than treating stored PASS flags as
unqualified conformance. Its M1/M2/M3 controls use read-only source/Git queries;
they are not invocations of the historical receipt writers.

At **2026-10-18T00:06:42Z**, this scribe independently extracted and executed
that artifact's **M2 fenced shell control**, exit **0**, against source SHA-256
`c1457e85320f3d4616e5029fed107f0ed4a12f49b41bb2b2d1927f5c3b0d413b`.
The command is the literal shell block under its “M2 — final-state, denominator,
original-queue and receipt controls” heading, executed with
`subprocess.run(['bash'], input=block, text=True, capture_output=True)` and
`TMPDIR=$PWD/.scratch`, bytecode disabled. It confirms **four admitted / one
rejected / one skipped**, stored **14 passed / one failed** claim flags,
original queue **15 = eight fixed + seven routed**, and all historical receipt
bytes equal their admission/rejection revisions. These are recorded outcomes,
not new quality scores or independent historical-truth certification.

| round | final state | threshold assessment retained in the retrospective |
|---|---|---|
| 8 | **ADMITTED** | F/O bounded thresholds honored. D is filed PASS but its strict repaired-live-tree no-drift replay clause is **not fully honored**: accepted historical-gate replay is not a new frozen verdict over the repaired typed flow. Retain that qualification and the audit-count erratum. |
| 9 | **ADMITTED** | F floors and D3 contract honored. O is filed PASS but the unqualified standard-complete/default-root after-state was **not honored**. Round-14 compatibility discovery does not retroactively make the old baseline layout standard-conforming. |
| 10 | **ADMITTED** | C entry floors and O finding dispositions honored. F's frozen command coverage passes, but particular stale-fixed assertions **fail against retained runner bytes** and are corrected to documented-stale; updater and missing-verifier summary defects remain visible. |
| 11 | **REJECTED** | D/O structural contracts verified. F's unchanged at-least-95% hash-stability threshold **failed as declared**; cause disposition and useful D/O work do not substitute for that clause. |
| 12 | **ADMITTED** | Filed C/O/A flags pass with explicit execution-scope, queue-count, and provenance qualifications. The original adjacency ledger's entry-receipt pointer is absent; a separately attributed source-boundary review is real evidence but not the missing assigned receipt. Audit admission is not handoff acceptance. |
| 13 | **OPERATOR-SKIPPED** | D/C/O remain unexecuted/deferred, neither achieved thresholds nor empirically failed measurements. LOG records operator cancellation, not a demonstrated provider failure. |

**Round-11 denominator correction.** The settled summary records **192**
rechecks, **147** stable and **45** unstable, giving **147/192 = 0.765625**.
The filed validator's byte-comparable channel records **189** comparable,
**147** stable, **42** unstable, giving **147/189 = 0.777777…**. Both are below
**0.95**. Sources: `reports/round-11/recheck/summary.json:4-9`,
`reports/round-11/validation.json` → `claims.F.measurement` / `failures`, and
`reports/round-11/claims.json:30-32`; independent command/date: M2 above.
The older draft's 149/43 census remains a dated in-flight snapshot, never the
settled result. Three no-hash rows explain the denominator split; an additional
exit-only drift explains why the validator lists 46 drift rows rather than 45
hash-unstable/no-hash rows. A stable stdout hash alone is insufficient.

The retrospective's **six conformance classes**, not six atomic incidents, are:
scope confinement; filed-artifact integrity; availability/dispatch/resources;
baseline-layout/default roots; schema/counting/measurement contracts; and
report/status/provenance reconciliation. Its class table binds bounded repairs
to the controls above and keeps output-root prevention, dispatch-trace gaps,
external report verification, and the missing adjacency receipt open instead of
manufacturing closure. The latter gap was positively detected by the dated M2
path-existence query, not repaired by this scribe.

**Operator question, still open:** should a future freshness claim measure a
quiet pinned tree, a predeclared normalized semantic/exit channel, or a
separately measured legitimate-change budget, and with what denominator and
threshold? Decide before dispatch; do not retrospectively admit round 11 or
resume freshness-axis moves without authority. The amendment count is scoped:
**two structural changes plus one provider-only change**, not an unqualified
total of two. Named dated commit controls are in the retrospective's M3.

C07 and C08 have now filed **hash-bound PASS assessments for the same
`c1457e85…` retrospective**, not for every historical claim or pointer.
At **2026-10-18T00:08:31Z**, C07's read-only path/range/claim control checks
positive citations and all measured/deferred claim rows; C08 independently
executes the exact M1/M2/M3 controls concurrently, all exit 0, with the source
hash unchanged. The disclosed historical missing receipt stays a gap.
`reports/round-14/retro-consistency.md` separately reports its final C1/C3
execution on **2026-10-18T00:08:23+00:00**, exit 0, **19/19 material checks**
against the retrospective, proposed summary, and then-current SCORECARD.

The actual SCORECARD/LOG landing remains parent work. Its draft append records
are `reports/round-14/scorecard-draft.md` and `reports/round-14/log-draft.md`,
not proof of shared-file integration. Appending SCORECARD changes the
consistency control's bound input and requires a new delivered-row comparison.

## Other axes, boundaries, and SHONEN evidence

No new coverage or freshness claim is declared in round 14. No new culture,
historical-truth certification, cultural clearance, lore acceptance, or canon
is claimed. Adjacency remains bounded by `PROVINCE.md`; the round-12 semantic
handoff rejection and bilateral-acknowledgment gap are not closed by a shape
check or by this report. Handoff-v2 and civilization-map work remain deferred
to the operator's later-round assignments.

The assigned `reports/round-14/scope.md` records an inherited parent-tree
`baseline-analyze.txt` exception, not an unqualified clean fleet. Its dated
porcelain/stat commands at 2026-10-17T20:57:37-03:00–20:58:57-03:00 predate or
bound the observation without attributing authorship; the lane has no cleanup
authority there. It also records unrelated sibling dirt without Kotodama
attribution and confirms unchanged PROVINCE/contract scope. These are the
scope owner's observations, not external checks performed by this scribe.

For local historical preservation, `reports/round-14/verify-3.md` provides the
stronger allowed-exception control: on **2026-10-18T00:04:49.133004+00:00**,
its read-only baseline comparison/reconstruction exits 0. Of **609** tracked
historical paths, **607** are unchanged; only the exact tracker-key and
exposure-ledger additions are allowed. Removing those insertions reconstructs
every original byte. Strict whole-file sentinels that went red during these
additions remain recorded; permitted new entries are not byte-identical files.

Promotion checklist, matching `SHONEN.md` markers:

- [~] Decision tables/error patterns/cited sources: existing typed-label
  decision-table evidence is `reports/round-8/depth/skill-table-draft.md` and
  its admitted `validation.json` → `claims.D.measurement.docs`. No new round-14
  decision table is asserted without an integrated evidence pointer.
- [~] End-to-end domain task executed and logged: the filed round-11 receipt's
  D typed-pipeline and O handoff-exercise measurements, with LOG's round-11
  entry, are lane-side evidence. This does not turn that rejected round into
  an admitted one, nor turn administrative fixes into a fresh culture task.
- [~] Executable instructions have bounded runtime evidence: the actual
  battery controls, guard selftest, clone replays and production-runner
  controls are named above. This is not a passing final round-14 receipt.
- [~] Province boundaries are retained in the assigned scope review;
  inherited hygiene exceptions, limited snapshots, and no author attribution
  for unrelated sibling dirt remain explicit, not a fleet-clean certificate.

No `[x]` is awarded by this author. A named non-author verifier and the
promotion-gate process are required by `SHONEN.md:10-11`.

## Evidence commands and receipt-integrity checks

### E1 — read-only filed state and original/live queue census

Initial observations were made on 2026-10-17T23:58:18Z–23:58:49Z. The final
reproduction below pins the **original** queue to the declared baseline and
labels current additive entries separately, so the new exposure record cannot
be mistaken for another original round-12 defect. It invokes no old runner.

```sh
export TMPDIR="$PWD/.scratch" PYTHONDONTWRITEBYTECODE=1
python3 - <<'PY'
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import json, subprocess
print('observed_at=' + datetime.now(timezone.utc).isoformat())
for n in range(8, 13):
    data = json.loads(Path(f"reports/round-{n}/validation.json").read_text())
    print(n, data["acceptance_checks_passed"],
          {key: value["passed"] for key, value in data["claims"].items()})
base = json.loads(Path('reports/round-14/claims.json').read_text())['baseline_revision']
path = 'reports/round-12/defects/ledger.json'
rows = json.loads(subprocess.check_output(['git', 'show', f'{base}:{path}']))['entries']
live = json.loads(Path(path).read_text())['entries']
assert len(rows) == 15 and Counter(row['status'] for row in rows) == {'fixed-with-control': 8, 'routed': 7}
assert live[:len(rows)] == rows
print('original', len(rows), dict(Counter(row['status'] for row in rows)))
print('original_routed', [row['id'] for row in rows if row['status'] == 'routed'])
print('current', len(live), dict(Counter(row['status'] for row in live)))
print('additions', [row['id'] for row in live[len(rows):]])
PY
```

### E2 — admission-receipt preservation, not a rerun

The read-only `git show`/byte comparison on 2026-10-17T23:58:18Z found both
restored receipts equal their admission-revision blobs:

- `e1694bad6ac96aca45a11ca5746582b275929355:reports/round-8/validation.json`;
  live SHA-256 `359932a7debf6ec39f3182ac078ae3e900860efd97831f6b41bfe818b96ccfba`.
- `9dc18ec1339bffd6f81e74f1a5742464ef578749:reports/round-9/validation.json`;
  live SHA-256 `036f84278c4817901413d97839ceba78aa8a367f91579de7505c92800611e418`.

Reproducible command:

```sh
export TMPDIR="$PWD/.scratch" PYTHONDONTWRITEBYTECODE=1
python3 - <<'PY'
from pathlib import Path
import hashlib, subprocess
for n, rev in ((8, "e1694bad6ac96aca45a11ca5746582b275929355"),
               (9, "9dc18ec1339bffd6f81e74f1a5742464ef578749")):
    path = f"reports/round-{n}/validation.json"
    live = Path(path).read_bytes()
    filed = subprocess.check_output(["git", "show", f"{rev}:{path}"])
    print(path, live == filed, hashlib.sha256(live).hexdigest())
    assert live == filed
PY
```

At 2026-10-17T23:58:32Z, `git diff -- reports/round-10/findings-tracker.json`
showed a new `errata` key for R14-O03. The later owner and V02/V03 controls
supply its original-byte reconstruction, as described above. The scribe neither
removes that permitted addition nor back-patches the old verifier list; its
whole-file hash is not falsely described as unchanged.

### Verification of this draft

On **2026-10-18T00:10:03Z**, this scribe extracted the delivered E1/E2 fenced
shell blocks using a line-anchored fence parser and executed them concurrently
with `subprocess.run(['bash'], input=block, text=True, capture_output=True)`.
**Both exit 0**; the draft bytes remained unchanged across the checks. E1
reproduces the original status split and separately reports the current
augmented ledger **16 = eight fixed + seven routed + one documentation
resolution**, with only `FRR-14-EXPOSURE` added. E2 proves both restored receipts
still equal their original filing blobs. The independent retrospective M2 run
and its exact source hash are recorded in the calibration section.

A read-only Python `pathlib`/regex literal-path and whitespace check at
**2026-10-18T00:12:42Z** found only the expressly pending resolver and round-14
validation receipt absent; existing source citations resolve. It also confirms
no trailing whitespace and a final LF. `git diff --check`, run on the shared
lane at **2026-10-18T00:11:54Z**, exits **0**. These are draft/source checks,
not an execution or green verdict of the full round-14 acceptance command.

## Integrator closeout dependencies

1. Create/bind the resolver's declared eight-item crosswalk to all raw source
   statuses, each fix's dated control, and the report-reconciliation records.
   Do not relabel the seven historical routed rows or suppress broader open
   prevention/provenance obligations.
2. Bind the final guard/runner source versions to the independent runtime
   controls and integrated result; the latest runner observed at the cutoff
   differs from the final production-clone control's pinned version.
3. Land the prepared SCORECARD/LOG appends through their owners, preserve the
   original thresholds and round-13 skip, and refresh the delivered-row
   consistency binding after the SCORECARD append.
4. Supply actual dispatch/availability and final scope evidence without
   deriving execution from the request, claiming external report inspection,
   or treating inherited hygiene exceptions as lane cleanup authority.
5. Obtain a settled `reports/round-14/validation.json` and independent rerun,
   verify their runner/input hashes and all O/D/C booleans, then decide axis
   verdicts and final admission. Do not publish this draft's bounded controls
   or its evidence cutoff as proof that those remaining integration steps ran.
