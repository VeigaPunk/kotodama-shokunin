# R14-X07 — retrospective / SCORECARD consistency

Axes: calibration (honest final states and compatible counting populations), operability (read-only reproduction), and historical integrity (no filed runner execution).

**Status: PASS for the hash-bound numerical/final-state comparison below, with historical discrepancies explicitly preserved.** The consolidated `reports/round-14/loop1-retrospective.md`, historical SCORECARD rows, and proposed loop-summary row were compared on **2026-10-18T00:07:01+00:00**. This is not independent literal-conformance certification or round-14 admission. The actual SCORECARD/LOG append and overall acceptance remain parent integration work; this worker writes only this file.

Reference revision: `a7bc9e9ff05a57515c5efaaa7e50116eb30938ff`. Source observations began on 2026-10-17; control C1 passed at **2026-10-18T00:02:15+00:00**. Historical quantities below are pinned to that revision, not to a concurrently changing working-tree ledger. Every count below is either reproduced by C1 or explicitly attributed to its cited historical record.

## Final-state and claim baseline

| Round | SCORECARD final-state location | Filed claim flags | Consistency requirement |
|---|---|---|---|
| 8 | `SCORECARD.md:100-122`, admitted | D/F/O true | Preserve admission; freshness receipts are scoped passage support, not whole-claim certification. |
| 9 | `SCORECARD.md:130-152`, admitted | D/F/O true | Preserve admission; D3 was newly admitted here, not retroactively in failed round 7. |
| 10 | `SCORECARD.md:160-182`, admitted | C/F/O true | Preserve admission; coverage additions are distinct from author-fragment counts. |
| 11 | `SCORECARD.md:184-205`, rejected | D/O true, F false | Never convert passing D/O flags into round admission or retrospectively lower F's threshold. |
| 12 | `SCORECARD.md:207-229`, admitted | C/O/A true | Preserve admission while separately retaining the handoff semantic rejection. |
| 13 | `LOG.md:3077-3080`; amended map at `SCORECARD.md:239-248` | Declared D/C/O unexecuted, deferred | Operator-skipped, not an admitted, rejected, or provider-failed work round. |

C1 reproduces **4 admitted / 1 rejected / 1 skipped** across this retrospective window. The executed rounds have **15 stored claim flags: 14 passed / 1 failed**. Only **12 passing flags belong to admitted rounds**; round 11's other **2 passing flags** remain evidence from a rejected round. Round 13's **3 unexecuted declarations** are not successes or failed measurements. These are counts of filed Boolean claim results, not proof that all literal after-state clauses were honored, numeric quality scores, or independent runtime-worker receipts.

A retrospective may therefore retain a filed PASS while honestly identifying an unhonored clause. The shards explicitly qualify round-8 D's repaired-live-tree frozen replay (`retro/r8.md:78-101`), round-9 O's default-root standard completeness (`retro/r9.md:61-89`), and round-10 F's reverted stale-fixed assertions (`retro/r10.md:60-98`). These do not change the stored flag totals or silently rescind historical admission. The proposed SCORECARD summary correctly labels its **14/1** as stored harness flags (`reports/round-14/scorecard-draft.md:16-21`), not fourteen unqualified threshold successes. The underlying reproduction command is C1; historical measurements are dated 2026-10-17.

## Historical mismatches the retrospective must disclose

- **X07-01 — round-11 denominator shorthand.** `SCORECARD.md:196` and `LOG.md:3021-3024` combine coverage of **192 rows**, **147 stable**, **45 unstable** with the diagnostic **0.778**. The comparable acceptance population is **189 = 147 stable + 42 unstable**; **3 no-hash rows** remain dispositioned but outside that denominator. Thus **147/189 = 0.7777777777777778**, while **147/192 = 0.765625** (filed summary **0.7656**). Both fail the unchanged **0.95** threshold. C1 is the arithmetic/verdict control; `reports/round-14/errata/r11-draft-census.md:13-36` supplies the new integration wording. Do not use the draft's **149/43** in-flight census as settled data (`reports/round-11/report-draft.md:135-155`). Documentation correction only; no old bytes are rewritten here.
- **X07-02 — round-12 fixed/routed split.** The admitted prose at `SCORECARD.md:218` and `LOG.md:3039-3042` says **15 = 7 fixed + 8 routed**. The filed receipt's `claims.O.measurement.bounded_fixes.value` / `round14_routes.value` and the committed defect ledger instead say **15 = 8 fixed-with-control + 7 routed**. C1 enumerates that committed population and asserts the discrepancy rather than silently choosing a channel. The round-14 assignment of **8 routed work items** is a separate work-package scope, not proof that the filed ledger has eight `status: routed` rows. A new integration note must explain the distinction; do not rewrite the admitted row or claim all historical prose matches.
- **X07-03 — operator-amendment counting boundary.** `reports/round-14/claims.json:28` says **2 operator amendments**, while `SCORECARD.md:239` explicitly says **amended 3×**. The local amendment history includes structural GLM addition, the provider-only route designation, and expand cancellation / GLM pinning (`LOG.md:3048-3080`; commit pointers in `reports/round-14/retrospective-audit-C07.md:11`). If a retrospective counts only structural amendments, it must name that narrower population and exclude the provider-only change explicitly. C1 detects the conflicting labels; an unqualified total of two does not match SCORECARD.
- **X07-04 — historical plan is not current execution.** `SCORECARD.md:233-238` still plans a Grok round 13, but the newer amendment at `:239-248` cancels expand rounds and records the skip. The retrospective must follow the final operator state, not treat the stale plan or requested worker count as completed work. Control: C1 requires the explicit skip entry at `LOG.md:3077-3080` and separately checks filed acceptance flags. No dispatch trace or external fleet file is independently verified by this check.

The round-12 recount channels are compatible when named: **89 rows = 12 exact matches + 77 dispositioned rows**, with the SCORECARD's **16 worker dispositions + 61 integrator coverage rows = 77** (`SCORECARD.md:217`; filed `validation.json.claims.C.measurement`; C1). Do not call all 89 exact matches or 89 independently completed worker receipts.

The round-12 ledger acquired a new round-14 exposure entry during this wave (`FRR-14-EXPOSURE`). A working-tree count at this stage is therefore not the original round-12 count. C1 deliberately reads committed source bytes; an append-only erratum must be reported as an addition, not as a correction to the historical population size.

## C1 — pinned, read-only numerical control

Run from the lane root. Observed **2026-10-18T00:02:15+00:00**, exit **0**. No historical validator is imported or run; no scratch or receipt is written.

```sh
export TMPDIR="$PWD/.scratch"
python3 -B - <<'PY'
from collections import Counter
from datetime import datetime, timezone
import json, re, subprocess
revision = 'a7bc9e9ff05a57515c5efaaa7e50116eb30938ff'
def filed(path):
    return subprocess.check_output(['git', 'show', f'{revision}:{path}'])
def load(path):
    return json.loads(filed(path))
score = filed('SCORECARD.md').decode()
states = {int(n): ('rejected' if 'NOT admitted' in tail else 'admitted')
          for n, tail in re.findall(r'^## Axes — round (8|9|10|11|12)\b([^\n]*)$', score, re.M)}
assert states == {8: 'admitted', 9: 'admitted', 10: 'admitted', 11: 'rejected', 12: 'admitted'}
receipts = {r: load(f'reports/round-{r}/validation.json') for r in states}
assert all(v['acceptance_checks_passed'] == (states[r] == 'admitted') for r, v in receipts.items())
claims = [c['passed'] for v in receipts.values() for c in v['claims'].values()]
assert (len(claims), sum(claims), len(claims) - sum(claims)) == (15, 14, 1)
assert sum(c['passed'] for r, v in receipts.items() if states[r] == 'admitted' for c in v['claims'].values()) == 12
assert len(load('reports/round-13/claims.json')['claims']) == 3
assert 'Round 13 status:** operator-skipped' in filed('LOG.md').decode()
rows = [load(f'reports/round-11/recheck/row-{i:03d}.json') for i in range(192)]
f = receipts[11]['claims']['F']['measurement']
assert (len(rows), sum(x['stable'] is True for x in rows), sum(x['stable'] is False for x in rows),
        sum(x.get('new_hash') is None for x in rows)) == (192, 147, 45, 3)
assert (f['rows_rechecked'], f['stable'], f['unstable']) == (189, 147, 42)
assert f['stability'] == 147 / 189 and f['stability'] < 0.95 and 147 / 192 < 0.95
assert receipts[11]['thresholds']['F']['min_stability'] == 0.95
c = receipts[12]['claims']['C']['measurement']
o = receipts[12]['claims']['O']['measurement']
assert tuple(c[k]['value'] for k in ('recounted_rows', 'matched_rows', 'dispositioned_rows')) == (89, 12, 77)
entries = load('reports/round-12/defects/ledger.json')['entries']
assert len(entries) == 15 and Counter(e['status'] for e in entries) == {'fixed-with-control': 8, 'routed': 7}
assert tuple(o[k]['value'] for k in ('bounded_fixes', 'round14_routes')) == (8, 7)
assert '7 fixed-with-control bounded' in score and '8 routed to round 14' in score
assert 'amended 3× same day' in score
assert '2 operator amendments' in load('reports/round-14/claims.json')['claims'][2]['before']
recounts = load('reports/round-12/recount/ledger.json')
assert Counter(r['verdict'] for r in recounts) == {'match': 12, 'disposition': 77}
assert sum('integrator' in str(r).lower() for r in recounts) == 61
assert 77 - 61 == 16
print('C1 PASS', datetime.now(timezone.utc).isoformat(timespec='seconds'))
print('states 4 admitted / 1 rejected / 1 skipped; stored flags 14 passed / 1 failed; 12 passing flags in admitted rounds')
print('r11 147/189 comparable and 147/192 all-row both fail 0.95; r12 recount 89=12+77; dispositions 77=16+61')
print('r12 receipt/ledger 8 fixed + 7 routed differs from historical prose 7 + 8; amendment labels 3 vs 2')
PY
```

An initial working-tree version of C1 failed its original-size ledger assertion after the parallel append-only exposure entry landed. That failure was retained as a population-change signal, not bypassed by changing the historical expected count. The final control pins the reference revision, preserving the original population and documenting later entries separately. The delivered C1 command was extracted from this file and rerun successfully at **2026-10-18T00:02:55+00:00**. The final delivered C1 (including flag wording and recount decomposition) and C3 both passed at **2026-10-18T00:08:23+00:00**, exit **0**; C3 again reported **19/19 material checks** and all embedded command exits **0**. The delivered-file whitespace check and `git diff --check -- reports/round-14/retro-consistency.md` also passed.

## Final-text comparison and disposition

The dependency was initially absent, was polled at 60-second intervals, and was available for inspection at **2026-10-18T00:05:37Z**, within the permitted wait. The comparison completed at **2026-10-18T00:07:01+00:00**. No historical validator was executed while waiting or checking.

| Compared surface | SCORECARD/source counterpart | Result |
|---|---|---|
| Retrospective `:18-34`; proposed summary `scorecard-draft.md:10-29` | SCORECARD round-state sections and LOG's final skip entry | PASS: same 4/1/1 states, same 14/1 stored claim flags; neither text converts passing flags into unconditional literal-conformance certification. |
| Round 8 `:49-69` | `SCORECARD.md:112-116`; restored receipt and R8 claim declaration | PASS with explicit qualification: scoped 15/15 receipts, 215 harness passage keys, 11 partial / 4 unresolved, 14/14 harness controls; the repaired-live-tree replay clause is not claimed fully honored. |
| Round 9 `:71-96` | `SCORECARD.md:142-147`; restored receipt and R9 claim declaration | PASS with explicit qualification: 12 hunter documents / 4 residuals; 8 baselines / 7 gates with custom roots; historical default-root failure is disclosed rather than erased by the successor repair. |
| Round 10 `:98-124` | `SCORECARD.md:170-174`; filed receipt and original tracker | PASS with explicit qualification: 179→189 entries, additions 3/3/2/2; 192 ledger rows / 36 frozen keys; 24 findings with 18/5/1 dispositions. Ten actual authors are not eleven; the reverted repair is not called a retained fix. |
| Round 11 `:126-158` | `SCORECARD.md:194-205`; filed receipt/summary | PASS: 15 holds + 1 note, not 16 holds; both 147/189 and 147/192 disclosed, both below 95%; the round remains rejected. The in-flight 149/43 is not substituted for settled 147/45. |
| Round 12 `:160-192` | `SCORECARD.md:217-227`; original recount/defect ledgers | PASS with discrepancy retained: 89 = 12 exact + 77 dispositions, including 61 integrator rows; receipt/ledger 8 fixed + 7 routed is not silently equated with prose 7 + 8. Audit admission remains distinct from semantic handoff rejection. The absent assigned entry-receipt pointer is disclosed, not fabricated. |
| Round 13 and amendments `:194-238` | `SCORECARD.md:233-255`; chronological LOG amendments | PASS: final skip supersedes the stale expansion plan; claims stay unexecuted/deferred. Two structural amendments versus three total amendment commits is explicitly scoped. |
| Classes and calibration `:240-301` | Historical defects / paused freshness policy | PASS: six named classes are a taxonomy, not six incidents, routed items, or scores; controls/open obligations are retained. The operator question remains pending and does not repair the old failed 95% claim. |

The table is a source/content comparison, not a new claim that all historic thresholds passed. Counts above are independently reproduced by C1 and by the embedded source controls executed through C3. Historical measurement date remains **2026-10-17**; the C3 reproduction/comparison date is **2026-10-18T00:07:01+00:00**.

### C2/C3 — receipt preservation, delivered controls, and content binding

At **2026-10-18T00:05:38+00:00**, a read-only byte comparison found all five round-8–12 validation receipts equal to their admission/rejection revisions. C3 repeats those comparisons through retrospective M2 and runs the retrospective's M1/M2/M3 controls plus the proposed SCORECARD census concurrently. All **four top-level commands exit 0**; M1 independently runs the **four shard reproduction blocks**. The content comparison has **19 material checks**, all passing at **2026-10-18T00:07:01+00:00**. These are reporting checks, not a replacement for the parent-owned regression or acceptance receipt.

Bound input hashes at that comparison:

- `reports/round-14/loop1-retrospective.md`: `c1457e85320f3d4616e5029fed107f0ed4a12f49b41bb2b2d1927f5c3b0d413b`
- `reports/round-14/scorecard-draft.md`: `73580b1f559c2e379ec9b6b9a17761135da406bfeb692396bcd97eb7680518a6`
- `SCORECARD.md`: `9b5e6436a62f30601565f359aff6dc31337dec509afae9378ca16d6c681e1818`

The following read-only control fails if those inputs change; a later parent append needs a new comparison, not reinterpretation of this receipt as covering unseen bytes.

```sh
export TMPDIR="$PWD/.scratch"
python3 -B - <<'PY'
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
import hashlib, re, subprocess
expected = {
    'reports/round-14/loop1-retrospective.md': 'c1457e85320f3d4616e5029fed107f0ed4a12f49b41bb2b2d1927f5c3b0d413b',
    'reports/round-14/scorecard-draft.md': '73580b1f559c2e379ec9b6b9a17761135da406bfeb692396bcd97eb7680518a6',
    'SCORECARD.md': '9b5e6436a62f30601565f359aff6dc31337dec509afae9378ca16d6c681e1818',
}
raw = {p: Path(p).read_bytes() for p in expected}
assert all(hashlib.sha256(raw[p]).hexdigest() == digest for p, digest in expected.items())
r, d, s = (raw[p].decode() for p in expected)
rows = {int(n): state.strip() for n, state in re.findall(r'^\| (8|9|10|11|12|13) \| ([^|]+) \|', r, re.M)}
assert rows == {8: 'admitted', 9: 'admitted', 10: 'admitted', 11: 'rejected', 12: 'admitted', 13: 'skipped, by operator'}
for n, state in {8: 'admitted', 9: 'admitted', 10: 'admitted', 11: 'rejected', 12: 'admitted'}.items():
    heading = re.search(rf'^## Axes — round {n}\b([^\n]*)$', s, re.M)
    assert heading and (('NOT admitted' in heading[1]) == (state == 'rejected'))
assert '**Four admitted, one rejected, one operator-skipped:**' in r
assert '**4 admitted** (8, 9, 10, 12); **1 rejected** (11); **1 operator-skipped** (13)' in d
assert '**14 passed / one failed**' in r and '**14 passed / 1 failed**' in d
checks = {
    'r8 passage scope': '15/15 receipts and 15 passage-bearing residuals; 215 harness passage keys' in r,
    'r8 raw/conservative split': '11 partial-support / four unresolved' in r,
    'r8 count erratum': '14/14 harness controls' in r and "audit's 12/12 is wrong" in r,
    'r8 strict replay qualification': 'strict repaired-live-tree replay clause not fully honored' in r,
    'r9 scoped movements': '12 hunter JSON documents, three strategies for each of four residuals' in r,
    'r9 default gap qualification': 'default-runner after-state not honored' in r and 'historical default finds five and exits 2' in r,
    'r10 coverage/author units': '179 → 189 entries, additions linguistics 3 / myth-symbol 3 / culture-material 2 / verification 2' in r and 'Actual author fragments are ten' in r,
    'r10 finding dispositions': '24 rows, 18 fixed-with-control / five wont-fix / one wrong / zero pending' in r,
    'r10 corrected stale-fixed scope': 'particular fixed-status assertions failed against retained bytes' in r,
    'r11 holds vs findings': '16 finding tokens comprise 15 holds plus one note, never 16 holds' in r,
    'r11 both denominators': '147/189 = 0.777777' in r and '147/192 = 0.765625' in r,
    'r11 failed threshold': 'below 0.95' in r and '**FAILED AS DECLARED:**' in r,
    'r12 recount units': '89 rows = 12 exact matches + 77 dispositions' in r and '61 integrator coverage rows' in r,
    'r12 defect conflict disclosed': 'eight fixed-with-control / seven routed, while LOG/SCORECARD say seven fixed / eight routed' in r,
    'r12 audit vs transfer': 'Handoff semantics are explicitly REJECTED despite passing envelope shape' in r,
    'amendments count boundary': '**two structural schedule amendments**' in r and '**three amendment commits in total**' in r,
    'six classes are taxonomy': 'These **six classes** are a retrospective taxonomy, not six atomic incidents' in r and len(re.findall(r'^\| K[1-6] —', r, re.M)) == 6,
    'operator calibration remains pending': '**No option or new threshold is selected here.**' in r,
    'checkpoint not full loop completion': 'this six-record checkpoint is not a claim that the full amended loop is done' in r,
}
assert len(checks) == 19 and all(checks.values()), [name for name, ok in checks.items() if not ok]
blocks = [('retrospective M' + str(i + 1), b) for i, b in enumerate(re.findall(r'```sh\n(.*?)\n```', r, re.S))]
blocks += [('SCORECARD draft census', re.search(r'```bash\n(.*?)\n```', d, re.S).group(1))]
assert len(blocks) == 4

def run(item):
    label, block = item
    result = subprocess.run(['bash', '-c', block], text=True, capture_output=True, timeout=120)
    return label, result

with ThreadPoolExecutor(max_workers=4) as pool:
    results = list(pool.map(run, blocks))
for label, result in results:
    print(label, 'exit', result.returncode)
    if result.returncode:
        print(result.stdout, result.stderr)
assert all(result.returncode == 0 for _, result in results)
assert all(Path(p).read_bytes() == data for p, data in raw.items())
print('C3 PASS', datetime.now(timezone.utc).isoformat(timespec='seconds'), 'material_checks', len(checks))
for p, digest in expected.items():
    print('SHA256', p, digest)
PY
```

### Parent follow-up boundary

The proposed summary row is consistent with the checked retrospective, but it is still a draft: `git status --short -- SCORECARD.md` showed no shared SCORECARD change at the comparison. The parent must land its append, then compare the delivered shared row and refresh the SCORECARD content binding. This report does not request or perform any old receipt refresh, threshold change, external final-report inspection, guard promotion, or overall round-14 admission. Historical pointer/provenance gaps and prevention obligations disclosed by the retrospective remain named follow-up items, not silently fixed by numerical consistency.
