# Round 14 — gate-keeper survey: receipt preservation, routed repairs, retrospective

source: `reports/round-14/claims.json`; `reports/round-14/targets.json`; `reports/round-12/defects/{ledger.json,routed.md,fix-09.md,fix-10.md,fix-11.md}`; filed round-8–12 validation receipts; `reports/round-11/recheck/summary.json`; `reports/round-12/recount/dispositions.md`; `LOG.md`; `SCORECARD.md`.
verified-at: opening survey 2026-10-17T23:57:50Z; read-only census 2026-10-17T23:58:36Z. Later observations, if any, are appended below.
recheck: use the read-only census below; read the assigned round-14 runner receipt after integration. Do not run historical round validators in the live lane: their counting commands can write filed receipts.

Scope: X01 writes only this lesson. The declared baseline is `926c86f8be3cc9307f8f10dce55768c290b6f94d` (`reports/round-14/claims.json:5`); observed declaration HEAD was `a7bc9e9ff05a57515c5efaaa7e50116eb30938ff` (`git rev-parse HEAD`, 2026-10-17T23:57:50Z). These are different roles, not competing baseline pins. This survey is not independent promotion verification, a domain-truth certification, or a round admission.

## Evidence commands and opening fragment index

The following read-only census ran from the lane root at **2026-10-17T23:58:36Z**, with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`. It supplies the historical verdicts, queue counts, and receipt census used below; it does not execute any round runner.

```sh
python3 -B - <<'PY'
from datetime import datetime, timezone
from pathlib import Path
import json
print(datetime.now(timezone.utc).isoformat(timespec='seconds'))
for number in range(8, 13):
    data = json.loads(Path(f'reports/round-{number}/validation.json').read_text())
    print(number, data['acceptance_checks_passed'], {key: value['passed'] for key, value in data['claims'].items()})
entries = json.loads(Path('reports/round-12/defects/ledger.json').read_text())['entries']
for status in ('routed', 'fixed-with-control'):
    ids = [entry['id'] for entry in entries if entry['status'] == status]
    print(status, len(ids), ids)
rows = [json.loads(path.read_text()) for path in Path('reports/round-11/recheck').glob('row-*.json')]
print('r11', len(rows), sum(row.get('stable') is True for row in rows), sum(row.get('stable') is False for row in rows), sum(row.get('new_hash') is None for row in rows))
PY
```

Opening inventory command/date: `sorted(str(p) for p in Path('reports/round-14').rglob('*') if p.is_file() and '__pycache__' not in p.parts)` and `len(...)`, executed inside the read-only Python survey at **2026-10-17T23:57:50Z**. It returned **2 files**, `claims.json` and `targets.json`. No fixer/verifier fragments, receipt guard, retrospective, round-14 runner, or round-14 validation receipt had landed in that snapshot. Dependencies are polled at the prescribed sixty-second interval for at most twenty minutes. Presence alone will not count as acceptance.

Receipt-preservation control at **2026-10-17T23:58:01Z**: compare `Path(path).read_bytes()` with `subprocess.check_output(['git', 'show', f'{revision}:{path}'])`, then print byte equality and each SHA-256. Round-8 `validation.json` equalled its `e1694ba` blob (`359932a7debf6ec39f3182ac078ae3e900860efd97831f6b41bfe818b96ccfba`); round-9 equalled its `9dc18ec` blob (`036f84278c4817901413d97839ceba78aa8a367f91579de7505c92800611e418`). This independently confirms the restored opening bytes, not prevention of another overwrite.

## Gate

Axes: **O / operability**, **D / depth**, **C / calibration**. Here C means calibration, unlike round-10 C / coverage. The declarations remain unchanged; no new scalar rubric or relaxed threshold is introduced.

### O — every routed item needs a disposition and a control

Declared threshold location: `reports/round-14/claims.json:14`; counting command: `python3 reports/round-14/run-validation.py` (assigned runner owner only). The resolution ledger must bind each routed identity to applied-with-control or resolved-by-documentation evidence, and the post-change battery, craft, D2, and D3 regressions must be green.

**Queue-accounting finding:** the census dated above returned **15** filed defect rows: **7 routed / 8 fixed-with-control**, not the **8 routed / 7 fixed** reported by `SCORECARD.md` round-12 O and `LOG.md` round-12 admission. The routed IDs are `R8-AUDCNT`, `R9-BATROOT`, `R10-F04`, `R10-F05`, `R10-IXCLS`, `R10-STATCONFL`, and `R10-RUNHASH`. `R11-DRAFT` is already marked fixed-with-control in the filed ledger. Meanwhile `reports/round-12/defects/routed.md` is a broader routing narrative containing supplementary report, integrity, and dispatch findings. These are different populations. The integrator must name the declared round-14 population and reconcile its mapping in a new record; do not invent another open row, silently relabel the filed ledger, or equate the narrative headings with the structured queue.

Minimum evidence/control pairs for the named queue and its report reconciliation:

- `R9-BATROOT`: make the default-root battery discover the historical myth/naming baselines without requiring an undocumented extra argument. Control: actual default invocation green plus a missing/tampered-baseline negative; retain digest checking. Extra-root success alone is not default-root coverage. Filed location evidence: `routed.md` R9-SWEEP-01 and `sweep-r9.md` (commands dated 2026-10-17).
- `R8-AUDCNT`: append an erratum distinguishing the filed audit's **12/12** from the reproduced **14/14**. Control: same harness command and stdout digest tied to the corrected count, with the historical audit unchanged. Source command/date: `python3 tools/harness/r8_checks.py --selftest`, 2026-10-17, `reports/round-12/recount/r8-2.md` and `recount/dispositions.md` item 2; quoted count location: `reports/round-8/operability/audit.md:57`.
- `R10-F04`: carry forward `fix-09.md` as a new effective tracker correction. Control: normalize verifier basenames and require set equality against live verifier files. A separate correction record leaves the tracker hash unchanged; an explicitly append-only new erratum key changes that hash, so it must instead reconstruct all original bytes exactly when its insertion/separator is removed and preserve the original finding-array bytes and fields. Do not confuse these preservation contracts. The earlier separate-record controls and superseded parser attempts are preserved in `reports/round-12/defects/fix-09.md` (2026-10-17); the new-key control is `reports/round-14/fix-tracker-pointer.md` (2026-10-17T23:58:18Z).
- `R10-F05` and supplementary round-11 report reconciliation: distinguish an in-lane draft from an authorized final filing; keep the round-11 rejection. Control: new report pointers or explicitly bounded lane-only integration records, corrected entry counts, and a settled receipt census with denominators. Absence in the lane is not proof of absence at an out-of-scope fleet destination; X01 does not inspect that destination.
- `R10-IXCLS`: keep index-updater fragments outside the author population in a successor classifier; do not patch the filed round-10 runner. Control: planted updater names, including the suffixed form, must not inflate authors, while a genuine author still counts.
- `R10-STATCONFL`: reconcile stale-fixed labels against the retained runner bytes and the integrator's reversion. Control: digest/history comparison and effective status consistent with the surviving implementation. A documented stale command is not a retained fix.
- `R10-RUNHASH`: resolve a full retained runner digest or document that a historical draft prefix is unrecoverable. Control: current runner/receipt binding and retained-blob search; keep the old prefix as a snapshot, not a current pin. `reports/round-12/defects/fix-10.md` supplies the dated current-digest and no-hit controls, even though the filed structured queue still routes the item.

Opening O reading: **not demonstrated**; the round-14 ledger and post-change regression receipts were absent. This is a missing-dependency reading, not a final failure or an assertion that earlier fixes did not occur.

### D — prevent a recheck from becoming a filed write

Declared threshold location: `reports/round-14/claims.json:22`; counting commands: the assigned round-14 runner and `python3 tools/harness/receipt_guard.py --selftest`. Required deliverable: importable guard plus CLI; refuse overwrite of an already-committed receipt unless **`REFRESH_RECEIPTS=1`** is explicitly set; refusal exits **3** with a named diagnostic; round-14-and-later runners use it. Historical runners remain filed unchanged; exposure is documented through a new erratum rather than patched away.

The causal lesson is narrower than “workers should be careful”: a counting command can itself be a writer. `reports/round-11/adjacency.md` §§1.3–1.4 and `reports/round-12/defects/routed.md` R8-SWEEP-01 record historical round validators overwriting their own output during live rechecks (observations dated 2026-10-17). Restoring the admitted bytes repairs the artifact but leaves that mechanism alive.

Required control boundary: a committed receipt must remain byte-identical on refusal; explicit refresh must take the allowed path; first uncommitted receipt creation must remain possible; arbitrary truthy refresh values must not silently authorize the write. A guard library or successful CLI check is not enough unless the actual successor runner invokes it before the write or any nested receipt-writing work. Test refusals in isolated in-lane repositories/copies, never against a filed historical output. This lesson does not authorize `REFRESH_RECEIPTS=1` in the live lane.

Opening D reading: **not demonstrated**; implementation, import/CLI controls, and runner wiring were absent. Do not retrofit the guard into filed round-8–12 runner bytes under this assignment.

### C — retrospective must separate final verdicts from snapshots

Declared threshold location: `reports/round-14/claims.json:29`; counting command: the assigned round-14 runner. The retrospective must name each round's final state and each claim's honored-or-failed threshold, enumerate conformance-defect classes with dispositions, restate the freshness-calibration question, and agree with the appended SCORECARD summary. A scribe's provisional close does not supersede a later filed verdict.

The read-only census at **2026-10-17T23:58:36Z** establishes the following recorded acceptance states; `LOG.md` admission/rejection headings supply final-state context. No historical runner was re-executed:

| round | final recorded state | claim outcomes and required qualification |
|---|---|---|
| 8 | admitted | F/O/D true in the restored receipt; preserve raw versus reconciled support, the audit-count erratum, and the receipt's isolated-pinned replay scope rather than claiming a live-tree freeze. |
| 9 | admitted | F/O/D true; O retains a known default-root/standard-layout coverage qualification until the successor control demonstrates the repair. |
| 10 | admitted | C/F/O true; C is coverage, not calibration. Preserve updater classification, reverted-fix status, tracker, hash, and draft-report corrections as new records. |
| 11 | rejected | D/O true, F false. Failed freshness cannot be converted into a round admission by the successful D/O legs or a later threshold amendment. |
| 12 | admitted | C/O/A true; admitting an adjacency audit does not mean accepting the handoff whose semantic gaps that audit filed. |
| 13 | operator-skipped | `LOG.md` “Regimen amendment 3” records the skip and deferred claims; declarations and interrupted dispatch attempts are not completed work or passed thresholds. |

Thus the retrospective's historical population is **4 admissions / 1 rejection / 1 skip** (receipt census above, 2026-10-17; round-13 state from `LOG.md:3065-3080`, dated 2026-10-17). This is not a count of six successful rounds and does not include an undecided round-14 result. Operator amendments are versioned schedule changes, not retroactive evidence of launches; `LOG.md` amendment entries and `SCORECARD.md` final amended regimen are the lane-local sources.

Freshness calibration control: the census above found **192** row receipts, **147** `stable=True`, **45** `stable=False`, and **3** missing new hashes. `reports/round-12/recount/dispositions.md` §“Reconciled Round-11 counts” (read-only recount, 2026-10-17) separates **189** comparable rows into **147** stable and **42** hash-unstable; the **45** includes the missing-hash rows, while **46** cause-bearing drift rows also include row 101's exit-only change. Comparable stability is **147/189 = 0.777777…**; all-row stability is **147/192 = 0.765625**. Both fail the unchanged **0.95** threshold in `reports/round-11/claims.json:31`. Never write the false equation “147/192 = 0.778”.

Operator question, not a self-authorized recalibration: what population and normalization should a future freshness threshold measure across legitimate build changes, volatile paths/timings, unreproducible commands, and recording defects? Name the future denominator and independent controls before dispatch; preserve round-11's rejection and the existing pause on freshness axis-move claims. Hash equality and unchanged semantic verdicts are separate channels, and exit-only drift must not disappear behind an unchanged stdout hash.

Opening C reading: **not demonstrated**; no round-14 retrospective or summary row had landed at the opening survey. This lesson supplies gate checks, not a substitute retrospective or permission to rewrite earlier lessons.

## Gate-keeper closeout rule

Do not admit a claim from a requested model, worker allocation, fragment count, a repair recommendation, or a self-reported green. Re-survey the integrated evidence and read the assigned runner's final receipt; confirm its runner/input bindings, every routed item's control, and the green post-change regressions. Record missing or red legs honestly. Source support is not whole-claim truth; packet shape is not handoff acceptance; neither is canon.

At the opening survey **no round-14 claim is admitted by X01**. The assigned acceptance owner and integrator retain the round verdict; independent spot-check status remains pending. Historical artifacts stay read-only, and corrections live in new records.

## Subsequent observations — read-only controls, not round acceptance

### 2026-10-18T00:00:19Z: delivered correction controls replayed

X01 extracted the indicated shell fence from each inspected Markdown artifact and executed it through `subprocess.run(['bash'], input=block, text=True)`, with `TMPDIR=$PWD/.scratch` and `PYTHONDONTWRITEBYTECODE=1`. The extraction was `re.findall(r'^```sh\n(.*?)^```$', text, re.M | re.S)[index]`, or the same expression with `bash` for the stale-status record. These were read-only controls, not historical runner invocations. The following results and counts belong to this command/date:

| control source / shell fence | result | bounded observation |
|---|---|---|
| `reports/round-14/fix-tracker-pointer.md`, first `sh` | exit 0 | Effective verifier set is 4/4, versus the historical list's 3; the original 24 finding rows and all original bytes reconstruct exactly after removing the new-key insertion. Missing/extra-verifier and original-row-mutation negatives reject. |
| `reports/round-14/fix-index-classification.md`, first `sh` | exit 0 | Correct role map has 10 authors, 10 reviewers, 4 auditors, 2 updaters. The filed expression counts 11 authors; removing a genuine author gives a false legacy 10 but corrected 9, below the unchanged minimum. This is controlled documentation, not a patch to the filed runner. |
| `reports/round-14/fix-status-conflicts.md`, first `bash` | exit 0 | Ledger positions 114, 132, 174 reconcile to documented-stale; the retained runner lacks the proposed helper. The planted stale-fixed assertion is rejected. |
| `reports/round-14/fix-runner-hash.md`, second `sh` / Control B | **exit 1** | Its unchanged-source assertion fails on `reports/round-12/defects/ledger.json`, now carrying the separately owned exposure appendix. Do not describe this delivered command as green merely because earlier runner/hash checks succeeded. |
| `reports/round-14/errata/r10-draft-status.md`, first `sh` | exit 0 | The settled addition count is 10, split 3/3/2/2; the obsolete 8-entry candidate is rejected. Draft and receipt match filing bytes; the external report pointer is an indirect in-lane attestation, not an inspected external report. |
| `reports/round-14/errata/r11-draft-census.md`, first `sh` / C1 | exit 0 | Both settled denominators, the unchanged 0.95 failure, receipt/input pins, and committed round-11 source bytes agree. This does not make that artifact's separate whole-tree C2 sentinel green. |

The earlier X01 whole-history `git diff --exit-code -- reports/round-{8,9,10,11,12}` assertion also failed at **2026-10-17T23:59:41Z** on the tracker erratum. That failure is retained, not hidden by changing its expected value. `reports/round-14/scope.md` §2 correctly distinguishes an allowed new-key exception from literal whole-file byte invariance and flags the declaration's stricter no-modified-filed-bytes wording for the integrator. An append-only exception must be explicitly dispositioned; a clean-tree claim would be false.

### Exposure appendix and guard probes

At **2026-10-18T00:00:55Z**, a separate read-only Python/Git control compared `a7bc9e9:reports/round-12/defects/ledger.json` with its current bytes. It asserted equality of the original entry prefix and reconstructed the original file by removing only the appended entry and separator. Result: **15 original entries preserved**, one new `FRR-14-EXPOSURE` entry; reconstruction exact. Whole-file SHA-256 changed from `a100c048a2f29374d1da7ab0b147f915c06678c7ab2366a4aef60db235c08a69` to `328f33d2375a8b90213d8ece20e833523abcb675af51be11f7458f0424bd1a60`. Thus the current ledger has an added round-14 exposure record; the opening 15-row queue census is a historical population, not a count to copy over the appended ledger. The new entry and `reports/round-14/guard/scribe.md` document legacy exposure, not retroactive protection.

At **2026-10-18T00:01:12Z**, X01 used `env` without `REFRESH_RECEIPTS`, `python3 -B tools/harness/receipt_guard.py --repo-root <lane> <target>`, and the imported `round_runner_main` with a memory-only callback. The committed round-8 receipt probe exited **3**, named `RECEIPT-GUARD-COMMITTED`, and included full commit/blob identities; the new-path probe exited **0** without creating its target. Catching the API's `SystemExit` verified **3**, no callback call, and unchanged receipt bytes. The guard source remained unchanged across this probe, SHA-256 `82eec760c45a81bb12a71423ba3137797a5a84f5c70d7f400c02b236dfd60c5e`. These are refusal/read-only API checks, not refresh-mode or actual round-runner integration tests; no live override was set. An immediately preceding probe expecting the earlier return-code API instead terminated at the expected refusal, illustrating why a moving implementation's contract and digest must be reread before interpreting a check.

`reports/round-14/guard/scribe.md` §5 retains a separate earlier **19/20** selftest result with a Git-root-binding failure (its command dated 2026-10-18T00:00:20Z). The guard had changed by the later X01 probe. Only the implementation/negative/integration owners' settled selftest and real runner controls can close that failure; the direct refusal checks above do not substitute for them.

### Other landed evidence and remaining dependencies at 2026-10-18T00:01:13Z

The timestamped `Path('reports/round-14').rglob('*')` survey found the battery-root fix, `verify-2.md`, guard design/scribe, correction records, scope report, retrospective audits, and report/LOG/SCORECARD drafts. The consolidated resolver, retrospective, runner, and validation receipt remained dependencies at this cutoff.

- `fix-battery-roots.md` demonstrates a compatibility discovery root, not relocation into the frozen-layout standard. Its actual default battery command improved exit 2 to 0; its selftest includes the root-omission negative, and its copied-tree snapshot tamper still exits 2. Source commands/dates and **7/7 coverage**, **8 pins**, **29/29 selftest** counts are in §§“Before and after”, “Persistent regression control”, and “Live-CLI negatives” (2026-10-17). X01 did not independently run this scratch-writing control; the assigned verifiers/regression owners retain that leg.
- `verify-2.md` independently replays the tracker's original-byte reconstruction and effective-set controls at 2026-10-18T00:00:21Z. This supports the additive correction, not an assertion that its whole-file digest stayed unchanged.
- `retrospective-audit-C08.md` C08-F03 identifies a second bookkeeping boundary: the declaration's “2 operator amendments” versus LOG's amendment-3 record. A valid retrospective must enumerate the named amendments (`51e5901`, `9437788`, `3dba77a`; source-map control dated 2026-10-17 in `retrospective-audit-C07.md`) or explicitly distinguish structural amendments from the provider-only route change. No unqualified total is manufactured here.

The round-wide O/D/C gate remains **pending**, including honest disposition of the failed delivered preservation assertion, the declared population mapping, final guard/runner controls, actual post-change regressions, retrospective audits, and parent SCORECARD/LOG integration.

### Later evidence through 2026-10-18T00:06:12Z

- **Lesson control:** X01 replayed the first `sh` block of `reports/round-14/lessons-audit.md` at **2026-10-18T00:03:43Z**, using the extraction/`subprocess.run` method above: exit **0**. It checked the historical Gate candidate sets, the new O/D/C headings, both freshness ratios, protected receipt/lesson hashes, and the pinned historical queue separately from the live appendix. Its tested lesson SHA-256 was `1ac65806ae6384ce6e78974fd04f543795c455135ae509a9a744944c04eb2f33`; later lesson additions require a new final integrity check rather than pretending this was a final-text hash.
- **Post-root-fix regressions:** `reports/round-14/regression.md` records **13/13** actual commands exiting 0 at **2026-10-17T23:59:57Z–23:59:58Z**, including the default battery, battery/craft selftests, D2/D3 selftests/checks and typed-label/coupling calls. Each command, stream digest, result location and code pin is in that report's final command inventory. X01's read-only regex/SHA-256 comparison at **2026-10-18T00:04:10Z** checked **15/15** cited tool, generated-packet and historical-receipt pins against the delivered files; all matched. The checked regression-report SHA-256 was `50a9c5b760634ba5a464093528eab59df5cea944672c2ec7471a71f5e1675444`. That is evidence binding, not another X01 runtime regression batch. `verify-1.md` separately demonstrates the actual default command and its omission/tamper negatives.
- **Guard failure superseded for a named revision:** `reports/round-14/guard/scribe.md` §7 records the guard selftest at **2026-10-18T00:02:28Z**, exit **0**, **45/45** controls, guard SHA-256 `d2297da4e6ceabb2eab84bb6e3beab16d82132aca0e313f0bdf21243304123a1`. This supersedes its earlier root-binding failure for those bytes only. Do not merge the earlier 20-control inventory and the later 45-control inventory into an invented denominator.
- **Load-bearing historical replay:** `reports/round-14/guard/retro-tests.json` and `.md` record `python3 reports/round-14/guard/retro-tests.py` at **2026-10-18T00:02:43Z–00:02:57Z**, exit **0**, **12/12** controls under that same guard digest. In independent disposable clones, the guard refuses the actual unchanged historical runners before their callback; the unguarded and explicit-refresh controls reach the writers; re-removing the override protects dirty committed receipts. The round-9 unguarded control stays acceptance-true while changing receipt bytes, directly proving why a green flag does not establish preservation. All live historical runner/receipt pins remain unchanged. Round 9 correctly uses its own filing revision because it does not exist at round 8's filing. None of these controls retrofits old live runners or certifies the production round-14 wiring.
- **Retrospective now present:** X01 replayed M2, the second `sh` block of `reports/round-14/loop1-retrospective.md`, at **2026-10-18T00:06:12Z**: exit **0**, unchanged text during that execution, SHA-256 `915e19489929efbadcdd382e44c4b1c4e06ce02073e9c7f2a9fe0606e0ba55c9`. The control confirms final-state/claim flags, receipt revision equality, both freshness populations and the original queue. The prose explicitly distinguishes historical PASS booleans from strict failures/gaps: round-8 live replay, round-9 standard/default coverage, round-10 stale-fixed assertions, and round-12 entry-receipt provenance. It enumerates six conformance classes with controls/open prevention tasks and restates the operator question. Independent final-text auditor bindings and the actual SCORECARD append were still to verify at this cutoff.

Two integration caveats must remain visible, not be treated as new work by X01:

1. `SKILL.md:208` still describes the pre-fix default battery as exit 2 and tells users to add the legacy root. `lessons-audit.md` X06-G05 flags this current-use documentation mismatch. The authorized integrator should reconcile it against the retained battery root fix; neither its current default success nor this lesson retroactively makes the old layout standard-conforming.
2. The retrospective discloses that the original round-12 adjacency entry rows point to the absent `reports/round-12/adjacency/entries.md`. Its M2 control deliberately detects the missing path; this is a reported provenance gap, not a green path-resolution control. The real A11–A12 source-boundary review is separately attributed and must not be called the missing assigned receipt. Any new correction belongs to its authorized owner; do not manufacture a historical file.

At the **2026-10-18T00:06:12Z** dependency census (`Path.is_file()` plus SHA-256), the consolidated routed-resolution and primary validation receipt were still absent. The guarded runner had landed, but source presence and an in-progress `rerun.json` are not a settled acceptance verdict. O/C therefore remain incomplete integration claims, and D still needs the actual successor-runner control/receipt binding before round admission can be considered.

### Follow-up through 2026-10-18T00:11:30Z

The append-only preservation contract now has an independently executed whole-history control without pretending its earlier zero-diff sentinels passed. At **2026-10-18T00:09:13Z**, X01 replayed the second `sh` block of `reports/round-14/verify-3.md`: exit **0**, `APPEND_ONLY_INTEGRITY=PASS` (stdout result location: that control's final line). It permits only the named tracker erratum and exposure-ledger addition, reconstructs every original byte outside those insertions, and checks the unchanged baseline bytes of all historical validation receipts. The verified report's SHA-256 was `430b9a27d43bdda747e2198d1ad87325e716e04abda942e3869ca65360a3728d`. Its §“Original broad controls are not silently called green” explicitly retains the failed runner-hash A/B and census C2 commands. This is an additional, correctly scoped integrity proof, not a retroactive PASS for those failed commands.

The consolidated retrospective changed after its first audits, and the old bindings correctly stopped certifying it. The current text SHA-256 is `c1457e85320f3d4616e5029fed107f0ed4a12f49b41bb2b2d1927f5c3b0d413b` (X01 SHA-256/presence probes at **2026-10-18T00:08:50Z**, **00:09:13Z**, and **00:11:18Z**). The C07/C08 artifacts now explicitly re-audit that revision at **00:08:31Z** and retain their rejected stale-digest attempt. X01 replayed C07's delivered, hash-bound `sh` command at **00:11:29Z–00:11:30Z**, exit **0**: positive citations, line ranges and every declared claim set pass; the historical missing entry-receipt provenance remains disclosed. Thus the earlier missing-final-auditor-binding condition is superseded for this revision, not for future edits.

`reports/round-14/retro-consistency.md` C3 additionally binds this retrospective, the proposed summary and the actual pre-append SCORECARD, with dated content/command controls. Its final parent-follow-up section correctly says the consistent proposed row is **still a draft**. At the **00:11:18Z** dependency probe, the primary resolver/validation receipt remained absent; the earlier actual-SCORECARD pointer probe was false. Auditor approval of a retrospective or draft row is not evidence that the required shared SCORECARD append has landed.

## Survey close — 2026-10-18T00:18:01Z

The dependency watcher completed normally after its prescribed bound: `for tick in range(21): Path(path).is_file(); time.sleep(60)` with no sleep after the last check, **2026-10-17T23:57:50Z–2026-10-18T00:17:50Z**. Its last check still lacked `reports/round-14/routed-resolution.json` and `reports/round-14/validation.json`. The close control at **00:18:01Z** independently used `Path.is_file()`, `Path.rglob('*')` excluding `__pycache__`, `len(...)`, SHA-256 and the actual SCORECARD text: **38** round-14 report files, the same missing primary artifacts, and no retrospective pointer in the shared SCORECARD. The watch is finished; no background wait remains with this seat.

### Gate readings at this survey close

- **Admitted by X01: none.** This is a bounded survey with incomplete parent integration, not a final rejection of round 14.
- **O / operability — withheld, not yet demonstrated end-to-end.** The fixes, documentation corrections, explicit additive-preservation control and independent regression receipts are substantive positive evidence. The mandatory consolidated resolution ledger and declared-eight-item crosswalk are absent. Preserve the failed broad source sentinels as failures; use the explicitly scoped controls for their actual purpose. Current-use battery documentation still requires the authorized integration correction.
- **D / depth — guard behavior demonstrated for its tested revision; round admission withheld.** Guard selftest, miniature runner controls and actual historical-writer clone controls are positive evidence. The closing guard digest remains `d2297da4e6ceabb2eab84bb6e3beab16d82132aca0e313f0bdf21243304123a1`. The successor runner has continued changing; its close digest is `b06bf6b12cf87377c52d245e6b1da413aab2ab17620d98dd7bc2a6ce467273b8` (SHA-256 close control, **00:18:01Z**), without a primary validation receipt to bind the final implementation and actual integrated result. Do not treat earlier runner selftests or source presence as a settled run on these bytes. Historical runners remain unwired and unsafe to run live, as the exposure erratum explicitly says.
- **C / calibration — retrospective supported; required integration incomplete.** Both auditors now bind the retained `c1457e85…` retrospective and preserve strict threshold failures, final states, six taxonomy groups and the future operator question. The required actual SCORECARD summary append has not landed. A passing proposed-row consistency check does not complete that leg.
- **Spot-check result:** X01's read-only correction, census, candidate/pointer, exact-byte reconstruction and regression-pin checks are recorded above with commands, dates and limits. Full settled-tree acceptance and the independent post-settle rerun remain pending; an in-progress rerun artifact is not their result. No historical validator, live receipt override, outside-lane write, commit or push was performed by X01.

Rejected interpretations at close: green fragments as whole-round admission; eight declared work packages as eight historically routed ledger rows; new-key preservation as an unchanged whole-file hash; zero stdout drift as receipt preservation; admitted audit as accepted handoff; and useful D/O claims as admission of rejected round 11. Each confuses a named evidence channel or time boundary. The restored round-8/9 receipts still match the opening hashes at the close control; restoration is preserved, not misrepresented as prevention.

Parent handoff: land and verify the explicit routed-resolution mapping; integrate the permitted SCORECARD/LOG and current-use documentation changes; bind the final successor-runner controls and primary receipt; obtain the independent settled-tree rerun; then decide the final round verdict. Record later outcomes in new entries, never by rewriting the filed round-8–12 snapshots or turning this bounded survey into a claim it did not verify.
