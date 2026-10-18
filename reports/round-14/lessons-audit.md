# R14-X06 — lessons audit and Gate-section check

- Axes: **O / operability** (lessons retain runnable, controlled evidence), **D / depth** (receipt-writer protection has an explicit boundary), **C / calibration** (survey snapshots never become invented final verdicts).
- Assignment: X06; this report is the only file authored by this worker. No historical validator, receipt refresh, commit, push, external filing inspection, or source re-fetch is performed.
- Declaration: `reports/round-14/claims.json` and `targets.json`; declared baseline `926c86f8be3cc9307f8f10dce55768c290b6f94d`. Audit source revision: `a7bc9e9ff05a57515c5efaaa7e50116eb30938ff` (declaration HEAD, not the baseline).
- Audit verdict: **historical Gate structure and the new lesson's provisional Gate are supported; final round-14 closeout remains pending**. This is a lesson audit, not an admission or independent promotion verification.

## Scope and evidence boundary

The corpus contract requires a `## Gate` with candidates, admitted/rejected readings and reasons, and a spot-check result. The reviewed surfaces are `corpus/lessons/round-8.md` through `round-12.md` and the new `corpus/lessons/round-14.md`. The round-13 operator skip is read from `LOG.md:3065-3080`; an absent round-13 lesson or receipt is not evidence of completed work.

The read-only Gate census at **2026-10-17T23:58:55Z** found **5 historical lessons, 5 Gate sections, and 15 candidate claims**. Every candidate set matches its own declaration: round 8 F/O/D; round 9 F/O/D; round 10 C/F/O; round 11 D/O/F; round 12 C/O/A. Reproduction/control is E1 below. Here round-10 C is **coverage**; round-12 and round-14 C are **calibration**.

At that same timestamp, each historical validation receipt matched its HEAD blob. Receipt reads produce observations about filed evidence; they do not rerun or independently certify every underlying domain claim. The later consolidated control also tests missing/duplicated candidates and the false denominator equation in memory.

## Historical lessons: survey versus final state

All historical lessons explicitly bound their readings to an unfinished survey window. Their statements that nothing was admitted at survey close are not false final-round verdicts, and must not be edited to look retrospectively prescient. A new integration record must connect those snapshots to the later recorded state.

The final booleans below were independently read from `reports/round-8` through `round-12/validation.json` on **2026-10-17T23:57:58Z** and checked again by E1. `LOG.md` admission/rejection headings and `SCORECARD.md` round sections supply the recorded admission decisions, not the earlier survey lessons.

| Round | Historical Gate location and boundary | Final recorded state | Qualification to carry forward |
|---|---|---|---|
| 8 | `corpus/lessons/round-8.md:58-181`; survey admitted none, F/O green and D red, spot-check pending | **ADMITTED**, F/O/D true | Keep the survey's failed selftest/pin state as historical. Use the restored admission receipt, not a live writer rerun; the audit's control-count correction is a new erratum. |
| 9 | `corpus/lessons/round-9.md:74-223`; survey admitted none, D freeze red, spot-check pending | **ADMITTED**, F/O/D true | The authorized D3 re-pin is distinct from deterministic assembly. O's default-root/layout qualification survives the admission and needs a successor control. |
| 10 | `corpus/lessons/round-10.md:83-241`; survey admitted none, C/F red, O green, spot-check pending | **ADMITTED**, C/F/O true | Entry counts, author-role counts, and updater fragments are distinct populations. Reverted repairs cannot be called retained fixes. |
| 11 | `corpus/lessons/round-11.md:94-274`; survey admitted none, F below threshold, unresolved in-flight receipt issues | **REJECTED**, D/O true and F false | Keep the rejection and the declared stability threshold. Later schema/census correction does not make F pass. |
| 12 | `corpus/lessons/round-12.md:20-52`; missing dependencies at survey close, later audit sample noted, no final admission asserted | **ADMITTED**, C/O/A true | Admission of an audit does not accept the semantically rejected handoff. Keep the independent sample's environmental hash mismatch and the defect-population discrepancy visible. |

Round 13 remains **OPERATOR-SKIPPED**: `LOG.md:3077-3080` records cancellation and deferred claims; declarations and interrupted attempts do not earn threshold credit. Thus the loop-1 historical state census is **4 admissions / 1 rejection / 1 skip** (E1 receipt census plus the dated operator entry). This is not six successful rounds and excludes undecided round 14.

### Gate findings and controls

- **X06-G01 — closure evidence is not the survey.** The old lessons carry candidates, explicit no-admission readings, and reasons. Their spot-check status is historical/pending, not an independent final verification. Round 12 has substantive audit-result evidence at `round-12.md:46-50`, despite lacking the literal `spot-check` label; do not misreport that as no audit. Control: use each dated survey boundary, compare the filed receipt and LOG decision, and append a new final-state cross-reference rather than rewriting old lessons. The table above is that bounded cross-reference, not a replacement final fleet report.
- **X06-G02 — round-11 denominator channels must remain separate.** The independent read-only row census at **2026-10-17T23:58:55Z** found **192 rows, 189 comparable, 147 hash-equal, 42 hash-unequal, 3 without a new hash**. All-row stability is **147/192 = 0.765625**; comparable stability is **147/189 = 0.777777…**, the filed diagnostic's **0.778**. Both fail the unchanged **0.95** threshold (`reports/round-11/claims.json:31`). The **45** unstable/no-hash dispositions and **46** cause-bearing drift rows differ because row 101 has exit-only drift (`reports/round-12/recount/dispositions.md:77-79`, dated recount). Control: E1 derives from hashes and rejects the false equation `147/192 = 0.778`; `reports/round-14/errata/r11-draft-census.md` C1 supplies the stronger input-pin/summary/verdict control. Do not promote disposition to stability or retroactively lower the threshold.
- **X06-G03 — queue populations differ before round 14.** At **2026-10-17T23:58:55Z**, the filed defect ledger had **15 entries = 8 fixed-with-control + 7 routed**, while `SCORECARD.md:218` and `LOG.md:3039-3042` say **7 fixes / 8 routes**. A read-only `git show`/JSON Counter at **2026-10-17T23:59:11Z** confirmed the 8/7 split already existed at round-12 admission `44070b4a6038f54e78d8d5be551e549fe202b0ee` and the declared round-14 baseline. `R11-DRAFT` was already fixed-with-control for a final-report pointer; its separate census reconciliation is not thereby complete. The routing narrative has **12 open-section subheadings**, a broader population (E1 heading census). Control: the new resolver must explicitly map its declared eight-item integration population to the seven literal routed IDs plus the report-reconciliation work; no invented open row, silent threshold reduction, or rewritten old status is acceptable.
- **X06-G04 — append-only additions change live totals.** The first combined control at **2026-10-18T00:00:54Z** aborted on a live-ledger status-count assertion. A read-only follow-up at **00:01:04Z** found a concurrently appended documentation entry: **16 live entries = 8 fixed-with-control + 7 routed + 1 resolved-by-documentation**. No source was written by this audit. Control: E1 pins the original population to the declaration revision, checks that the live entry prefix preserves those objects, and reports later entries separately. A changing live aggregate must not replace a historical denominator.
- **X06-G05 — current battery documentation requires reconciliation.** `SKILL.md:208` still describes the default battery as exiting 2 with myth/naming uncovered. `reports/round-14/fix-battery-roots.md:29-44` reports a dated default invocation exiting 0 and a green added regression after adding the preserved legacy root. That record explicitly calls the change a discovery compatibility exception, **not** retroactive standard-layout conformity (`:12-16`). Control: the integrator should add/update its authorized current-use documentation and cite the actual post-change default/tamper control; neither this audit nor a green discovery result relocates or re-freezes historical baselines. X06 does not edit SKILL.md.

## Round-14 lesson Gate check

`corpus/lessons/round-14.md:35-94` was read on **2026-10-18T00:00:54Z**. Its Gate correctly names **O / operability, D / depth, C / calibration**, uses the declared counting commands, keeps each opening reading not-demonstrated with a dependency reason, and awards no admission. It explicitly says independent spot-check status is pending. This is appropriate provisional Gate content, not a completed Gate result.

The lesson correctly carries the important distinctions:

- O's declared integration population must be mapped explicitly; custom-root success is not default-root success; updater fragments are not authors; a documented stale repair is not a retained fix.
- D requires an importable guard and real CLI, refusal exit **3** with a named diagnostic for a committed receipt unless exactly **`REFRESH_RECEIPTS=1`**, and actual successor-runner wiring. Guard presence is not a successful refusal or refresh test. The lesson does not authorize a live override or patch filed runners.
- C preserves final admitted/rejected/skipped states, both round-11 denominators, the failed historical threshold, and the still-open future calibration question. Shape-green handoff evidence is not semantic acceptance or canon.

**Closeout control:** append a dated Gate observation after the actual resolver, guard controls, retrospective, post-change regressions, and assigned runner receipt settle. That observation must name admitted/rejected claims with reasons and the actual spot-check result; keep the opening snapshot intact. Read the final runner/input hashes instead of merely seeing a receipt filename. The assigned runner, not X06, runs `python3 reports/round-14/run-validation.py`.

## Gate for this audit

- **Candidates:** historical lessons' Gate completeness; new lesson's O/D/C threshold fidelity; honest final-state and denominator cross-reference; immutable historical reads.
- **Admitted as audit observations:** the candidate mappings, historical receipt flags, denominator distinction, inherited queue-count mismatch, and the new lesson's bounded provisional wording, with E1 and cited source locations.
- **Rejected interpretations, with reasons:** a survey's no-admission line as the final state (wrong time boundary); successful D/O as round-11 admission (F failed); 0.778 over 192 (wrong denominator); default discovery as full frozen-layout conformance (different contract); guard source presence or a draft retrospective as an executed pass (missing runtime/evidence leg).
- **Spot-check result:** read-only JSON/Git/Markdown checks only; no fresh source access, domain/cultural clearance, independent promotion verdict, historical writer execution, or claimed round-wide regression rerun. Integrated round-14 claim admission remains pending its assigned evidence.

## E1 — reproducible read-only lesson control

This is the delivered audit's control, not an instruction to invoke old counting commands. It emits its own UTC date and source revision. New-entry counts are printed separately from the pinned historical population. Missing/duplicate-candidate and wrong-denominator controls are planted in memory only.

```sh
export TMPDIR="$PWD/.scratch" PYTHONDONTWRITEBYTECODE=1
python3 -B - <<'PY'
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import hashlib, json, re, subprocess

revision = 'a7bc9e9ff05a57515c5efaaa7e50116eb30938ff'
def git_bytes(path):
    return subprocess.check_output(['git', 'show', f'{revision}:{path}'])
def load(path):
    return json.loads(Path(path).read_text())
protected = [Path(f'{root}/round-{n}/{name}')
             for n in range(8, 13)
             for root, name in [('reports', 'claims.json'),
                                ('reports', 'validation.json')]]
protected += [Path(f'corpus/lessons/round-{n}.md') for n in range(8, 13)]
before = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in protected}
print('AUDIT_UTC', datetime.now(timezone.utc).isoformat(timespec='seconds'))
print('SOURCE_REVISION', revision)
for n in range(8, 13):
    lesson = Path(f'corpus/lessons/round-{n}.md').read_text()
    declaration = load(f'reports/round-{n}/claims.json')
    receipt = load(f'reports/round-{n}/validation.json')
    assert len(re.findall(r'^## Gate$', lesson, re.M)) == 1
    gate = lesson.split('## Gate', 1)[1]
    candidates = re.findall(r'^- \*\*([A-Z]) /', gate, re.M)
    expected = [c['id'] for c in declaration['claims']]
    assert Counter(candidates) == Counter(expected)
    assert Counter(candidates[:-1]) != Counter(expected)
    assert Counter(candidates + [candidates[0]]) != Counter(expected)
    flags = {k: v['passed'] for k, v in receipt['claims'].items()}
    assert receipt['acceptance_checks_passed'] is all(flags.values())
    for path in (f'corpus/lessons/round-{n}.md',
                 f'reports/round-{n}/validation.json'):
        assert Path(path).read_bytes() == git_bytes(path)
    print('ROUND', n, 'candidates', candidates, 'filed_claims', flags,
          'acceptance', receipt['acceptance_checks_passed'])
rows = [load(p) for p in Path('reports/round-11/recheck').glob('row-*.json')]
comparable = [r for r in rows if r.get('new_hash') is not None]
stable = sum(r['new_hash'] == r['prior_hash'] for r in comparable)
assert (len(rows), len(comparable), stable) == (192, 189, 147)
assert sum(r.get('stable') is True for r in rows) == stable
assert stable / len(rows) == 0.765625
assert round(stable / len(comparable), 3) == 0.778
assert round(stable / len(rows), 3) != 0.778
assert stable / len(rows) < 0.95 and stable / len(comparable) < 0.95
assert load('reports/round-11/validation.json')['claims']['F']['passed'] is False
print('R11', 'all', stable / len(rows), 'comparable', stable / len(comparable),
      'threshold', 0.95, 'FAIL')
ledger = 'reports/round-12/defects/ledger.json'
original = json.loads(git_bytes(ledger))['entries']
live = load(ledger)['entries']
assert Counter(r['status'] for r in original) == {
    'fixed-with-control': 8, 'routed': 7}
assert live[:len(original)] == original
print('R12_FILED', len(original), dict(Counter(r['status'] for r in original)))
print('R12_LIVE', len(live), dict(Counter(r['status'] for r in live)))
print('R12_APPENDED_IDS', [r['id'] for r in live[len(original):]])
routed = Path('reports/round-12/defects/routed.md').read_text()
print('ROUTING_NARRATIVE_HEADINGS', len(re.findall(
    r'^### ', routed.split('## Findings not routed as open')[0], re.M)))
lesson14 = Path('corpus/lessons/round-14.md').read_text()
assert len(re.findall(r'^## Gate$', lesson14, re.M)) == 1
candidates14 = re.findall(r'^### ([A-Z]) —', lesson14, re.M)
expected14 = [c['id'] for c in load('reports/round-14/claims.json')['claims']]
assert Counter(candidates14) == Counter(expected14)
assert 'python3 reports/round-14/run-validation.py' in lesson14
assert 'python3 tools/harness/receipt_guard.py --selftest' in lesson14
assert 'REFRESH_RECEIPTS=1' in lesson14
print('R14_GATE', candidates14, 'lesson_sha256',
      hashlib.sha256(lesson14.encode()).hexdigest())
assert before == {str(p): hashlib.sha256(p.read_bytes()).hexdigest()
                  for p in protected}
print('PASS: candidate controls, filed receipts, denominator controls,',
      'original queue prefix, and protected hashes')
PY
```

Execution result: **PASS**, exit **0**, at **2026-10-18T00:02:18Z**, by extracting and executing this report's actual fenced shell block with `python3 -B` / `subprocess.run(['bash', '-c', block], check=True)`. E1 confirmed the candidate controls, filed receipt bytes, denominator controls, original queue prefix, and unchanged protected hashes. Its round-14 lesson snapshot SHA-256 was `1ac65806ae6384ce6e78974fd04f543795c455135ae509a9a744944c04eb2f33`; its appended ledger-ID observation was `FRR-14-EXPOSURE`. The round-14 Gate is a separately authored, moving survey; that hash identifies the version checked, not a freeze of future append-only observations.

`git diff --check -- reports/round-14/lessons-audit.md` exited **0** on **2026-10-18T00:02:18Z**. A sixty-second dependency poll at **00:03:18Z** found the round-14 lesson and runner present, but `loop1-retrospective.md`, `routed-resolution.json`, and `validation.json` still pending. Final integration dependencies are checked separately; no absent dependency is passed by E1.
