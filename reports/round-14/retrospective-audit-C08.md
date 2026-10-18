# R14-C08 — retrospective number audit

Axis: calibration. Scope: read-only re-derivation of loop-1 retrospective numbers, not re-admission of past rounds. Initial source census: 2026-10-17T23:58:41Z–23:59:04Z. Final consolidated-text audit applies to SHA-256 `c1457e85320f3d4616e5029fed107f0ed4a12f49b41bb2b2d1927f5c3b0d413b`; see the final audit below. All four delivered C07/C08 reproduction blocks passed at 2026-10-18T00:09:30Z. Earlier sections preserve dated intermediate findings. No filed round runner was invoked, no source receipt was regenerated, and no historical number was overwritten by this auditor.

## Integration findings requiring explicit treatment

- **C08-F01 — defect totals conflict across historical channels.** A read-only Python `Counter(row['status'] for row in json.load(open('reports/round-12/defects/ledger.json'))['entries'])` at 2026-10-17T23:58:41Z reproduces **15 entries = 8 fixed-with-control + 7 routed**. `reports/round-12/validation.json` independently records `claims.O.measurement.bounded_fixes.value = 8` and `round14_routes.value = 7`. The admitted prose in `LOG.md:3039-3042` / `SCORECARD.md:218` says **7 fixed / 8 routed**. Neither reading should silently replace the other. Control: enumerate ledger IDs, print the Counter, and name the prose-vs-ledger difference in the retrospective. The routed note's heading inventory is yet another channel: do not equate headings with ledger entries.
- **C08-F02 — round-11 denominator and drift channels must stay separate.** The read-only row census at 2026-10-17T23:58:41Z gives **192 receipts, 189 with a comparable hash, 147 hash-stable, 42 hash-unstable, and 3 no-hash**; **147/189 = 0.7777777777777778**, whereas **147/192 = 0.765625**. The filed receipt uses the comparable ratio; the summary records the all-row ratio rounded to **0.7656**. Both fail the declared **0.95**. There are **45** hash-unstable/no-hash rows with named causes, while validation lists **46** drift rows because row 101 adds exit-only drift. Control: derive from row hashes, not the ambiguous historical equation; corroborate `reports/round-12/recount/r11-1.md:9-17`, `r11-2.md:9-15`, and `dispositions.md:77-79`.
- **C08-F03 — amendment count needs a named counting boundary.** `LOG.md:3048-3063` records the GLM addition and the provider amendment; `LOG.md:3065-3080` records expand cancellation / GLM pinning as amendment 3. `SCORECARD.md:239` explicitly says amended 3×. If the retrospective retains the declaration's “2 operator amendments”, it must say that counts only structural amendments and excludes the provider-only route change. Control: enumerate the three dated amendment commits (`51e5901`, `9437788`, `3dba77a`) rather than claiming an unqualified total of two.
- **C08-F04 — worker-completion prose is not a dispatch trace.** `claims.json.workers` is a requested count. LOG/SCORECARD completion numbers are operator-reported evidence, not independent runtime receipts. In particular, `reports/round-12/defects/routed.md:98-104` explicitly preserves the round-11 availability-trace gap. Control: label request and operator report separately; do not infer launches or model identity from the declaration.

## Reproduced source measurements

All measurements below are from read-only Python JSON parses / Git tree listings on 2026-10-17T23:58:41Z or 23:58:48Z. Reproduction command is included below. These are source facts, not a pass on the pending consolidated retrospective.

| measurement | re-derived value | source location |
|---|---|---|
| Final states for rounds 8–13 | admitted 8, 9, 10, 12; rejected 11; operator-skipped 13 | Each round 8–12 `validation.json.acceptance_checks_passed`; `LOG.md:3077-3080` for the skip |
| State totals | 4 admitted / 1 rejected / 1 skipped | Same state map, with skip explicitly operator-recorded |
| Filed claim booleans across rounds 8–12 | 14 passed / 1 failed | Each `validation.json.claims.*.passed`; only round-11 F is false |
| Round-8 F | 15 IDs / 15 receipts / 15 substantive-passage rows; 215 passage keys; 11 partial-support / 4 unresolved | `reports/round-8/validation.json.claims.F.measurement`, `freshness/reconciliation.json.rows` |
| Round-8 harness controls | 14/14, not audit prose's 12/12 | `reports/round-8/validation.json.claims.O.measurement.harness_fix`; `reports/round-8/operability/audit.md:57` is the conflicting filed quote |
| Round-9 F | 4 reconciliation rows, all partial-support; 12 hunter JSON files | `reports/round-9/freshness/reconciliation.json.rows`; `freshness/R*-receipt.json` |
| Corpus at round-8 and round-9 admission | 179 files: civilizations 94, culture-material 16, linguistics 16, myth-symbol 16, synthesis 24, verification 13 | Git tree at `e1694ba` / `9dc18ec`, restricted to Markdown under `corpus/knowledge` |
| Corpus at round-10 admission | 189 files: civilizations 94, culture-material 18, linguistics 19, myth-symbol 19, synthesis 24, verification 15 | Git tree at `94ca098`; additions 2/3/3/2 in the four thin partitions |
| Round-10 drift ledger | 192 rows; 153 current / 29 stale-documented / 10 stale-fixed as filed | `reports/round-10/drift/ledger.json[*].round10_verdict`; not a claim that all stale-fixed statuses remain accurate |
| Round-10 tracker | 24 rows: 18 fixed-with-control / 5 wont-fix (one qualified string) / 1 wrong | `reports/round-10/findings-tracker.json.findings[*].disposition` |
| Round-12 recount | 89 rows: 12 match / 77 disposition; 61 rows mention integrator | `reports/round-12/recount/ledger.json[*].verdict`; the 77 includes the original 16 disposition rows plus 61 integration rows |
| Round-12 defects | 15 = 8 fixed-with-control + 7 routed | `reports/round-12/defects/ledger.json.entries`; conflicts with 7/8 prose as noted above |

## Read-only reproduction control

Run from the lane root. This re-derives the stated counts without importing or running an old round validator; command observed on 2026-10-17 as specified above.

```sh
export TMPDIR="$PWD/.scratch"
python3 - <<'PY'
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import json, subprocess
load = lambda p: json.loads(Path(p).read_text())
print('AUDIT_UTC', datetime.now(timezone.utc).isoformat())
vs = {n: load(f'reports/round-{n}/validation.json') for n in range(8, 13)}
print('receipt_states', {n: d['acceptance_checks_passed'] for n, d in vs.items()})
print('claims', Counter(v['passed'] for d in vs.values() for v in d['claims'].values()))
for n in (8, 9):
    rows = load(f'reports/round-{n}/freshness/reconciliation.json')['rows']
    print('reconciliation', n, len(rows), Counter(r['reconciled_disposition'] for r in rows))
    print('hunter_jsons', n, len(list(Path(f'reports/round-{n}/freshness').glob('R*-receipt.json'))))
f = vs[8]['claims']['F']['measurement']
print('r8_f', {k: len(f[k]) for k in ('declared_ids', 'receipts_present', 'substantive_passages')}, f['distinct_substantive_passage_keys'])
h = vs[8]['claims']['O']['measurement']['harness_fix']
print('r8_harness', h['controls_passed'], h['controls_total'])
for rev in ('e1694ba', '9dc18ec', '94ca098'):
    ps = [p for p in subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', rev, '--', 'corpus/knowledge']).decode().splitlines() if p.endswith('.md')]
    print('corpus', rev, len(ps), Counter(p.split('/')[2] for p in ps))
rows = load('reports/round-10/drift/ledger.json')
print('r10_drift', len(rows), Counter(r['round10_verdict'] for r in rows))
rows = load('reports/round-10/findings-tracker.json')['findings']
print('r10_tracker', len(rows), Counter(r['disposition'] for r in rows))
rows = [load(p) for p in Path('reports/round-11/recheck').glob('row-*.json')]
comp = [r for r in rows if r.get('new_hash') is not None]
stable = [r for r in comp if r['new_hash'] == r['prior_hash']]
unstable = [r for r in comp if r['new_hash'] != r['prior_hash']]
nohash = [r for r in rows if r.get('new_hash') is None]
print('r11', len(rows), len(comp), len(stable), len(unstable), len(nohash), len(stable)/len(comp), len(stable)/len(rows))
print('r11_missing_causes', sum(not r.get('drift_cause') for r in unstable + nohash))
print('r11_drift_rows', len(vs[11]['claims']['F']['measurement']['drift_rows']))
rows = load('reports/round-12/recount/ledger.json')
print('r12_recount', len(rows), Counter(r['verdict'] for r in rows), 'integrator_rows', sum('integrator' in str(r).lower() for r in rows))
rows = json.loads(subprocess.check_output(['git', 'show', '44070b4:reports/round-12/defects/ledger.json']))['entries']
print('r12_filed_defects', len(rows), Counter(r['status'] for r in rows))
print('r12_filed_routed_ids', [r['id'] for r in rows if r['status'] == 'routed'])
live = load('reports/round-12/defects/ledger.json')['entries']
assert live[:len(rows)] == rows
print('r12_live_defects_including_later_appendices', len(live), Counter(r['status'] for r in live))
PY
```

## Measurement-boundary control

At 2026-10-18T00:02:24Z (local date 2026-10-17), an attempted exact live-ledger count assertion failed. A read-only `git diff -- reports/round-12/defects/ledger.json` and JSON comparison at 00:02:33Z explained why: the authorized D08 scribe had appended `FRR-14-EXPOSURE`, whose status is `resolved-by-documentation`. The original filed block remains 15 entries with the 8/7 split; the current augmented ledger is 16 entries with 8 fixed, 7 routed, and 1 documentation resolution. This is an expected append-only measurement-boundary change, not evidence that the historical census was wrong. The reproduction control now pins the historical census to `git show 44070b4:reports/round-12/defects/ledger.json`, verifies that the current ledger's original entry prefix is unchanged, and labels the live augmented total separately. No historical artifact was edited by this auditor.

## Independent numeric controls and upstream shards

At 2026-10-18T00:02:54Z (local date 2026-10-17), the revised embedded reproduction command exited 0. A separate read-only assertion control accepted the filed 8/7 status split, rejected the swapped 7/8 split, rejected the false all-row equation `147/192 = 0.778`, confirmed both genuine ratios remain below 0.95, and confirmed the original filed entry prefix is unchanged by the live appendix. Command: Python `Counter` over `json.loads(subprocess.check_output(['git','show','44070b4:reports/round-12/defects/ledger.json']))['entries']`, plus independent per-receipt hash comparison and rounded-ratio assertions.

The four upstream retrospective shards subsequently landed. At 2026-10-18T00:04:31Z their embedded commands were extracted and independently executed, all with exit 0. They reproduced the following additional distinctions:

- Round 9 has three final verifier documents (`verify-F01F02.md`, `verify-F03.md`, `verify-F04.md`), with the combined F01/F02 document already present at `9dc18ec`. The earlier two-document audit was an in-flight snapshot. Its 48/71/60/45 harness readings count nested retrieval units, not 12 hunter documents.
- Round 10 has 10 actual `C[0-9][0-9].md` author fragments versus 11 recorded authorship fragments; its tracker has 24 rows and 18/5/1 dispositions after normalizing the qualified wont-fix string. Its original summary lists verifier files 1/2/4, not all four; the report omission is distinct from execution absence.
- The original round-12 adjacency ledger has ten entry rows all pointing to the absent `reports/round-12/adjacency/entries.md`. The shard discloses that gap instead of claiming ten separately filed entry-audit receipts. See C07-F01 in `reports/round-14/retrospective-audit-C07.md`.

Exact rerun wrapper (each shard was run independently):

```sh
export TMPDIR="$PWD/.scratch"
python3 - <<'PY'
from pathlib import Path
import re, subprocess
for name in ('r8', 'r9', 'r10', 'r11-13'):
    p = Path(f'reports/round-14/retro/{name}.md')
    blocks = re.findall(r'```sh\n(.*?)\n```', p.read_text(), re.S)
    assert len(blocks) == 1
    subprocess.run(['bash', '-c', blocks[0]], check=True)
    print('PASS', p)
PY
```

## Final consolidated-text number audit

Audited deliverable: `reports/round-14/loop1-retrospective.md`, SHA-256 `c1457e85320f3d4616e5029fed107f0ed4a12f49b41bb2b2d1927f5c3b0d413b`, observed 2026-10-18T00:07:58Z. **Result: numeric reproduction and calibrated reporting PASS for that digest.** This is not a claim that every historical threshold passed, every receipt exists, or the full amended loop / round 14 is complete.

The first snapshot's M1/M2/M3 controls passed at 00:05:49Z. The final-fragment checks correctly rejected its now-stale digest at 00:07:52Z after the scribe clarified absent-runner wording, located the amendment shorthand, and recorded M2's result. The updated text was read in full and all three exact M1/M2/M3 blocks were independently re-executed concurrently at **2026-10-18T00:08:31Z** (local date 2026-10-17); all exited **0**, with the digest unchanged across the rerun. M1 itself runs the four shard controls concurrently. Outputs reproduce the source-measurement table above, and M2 additionally asserts byte equality of all five preserved validation receipts with their admission/rejection revisions.

The final text correctly incorporates every earlier C08 finding:

- **C08-F01 dispositioned:** lines 169–180 name the original 15 = 8 fixed + 7 routed measurement separately from the 7/8 admitted prose and the eight-item new work assignment. M2 pins the historical ledger before the later append-only exposure entry; it does not pretend there is an eighth original routed row.
- **C08-F02 dispositioned:** lines 138–158 and 282–285 keep 147/189 = 77.7778% separate from 147/192 = 76.5625%, both below the original 95%; 42 + 3 = 45 stays separate from 46 drift rows. The nine runner-recognized audit reruns are explicitly distinguished from the original auditor's 17 sampled reruns, corroborated at `reports/round-11/recheck/audit.md:124-130`.
- **C08-F03 dispositioned:** lines 222–236 enumerate all three amendment commits and explicitly restrict “two” to structural amendments, excluding the provider-only change. M3 reproduces all commit identities, subjects and timestamps.
- **C08-F04 dispositioned:** lines 198–204 and 236–241 distinguish operator-reported interrupted/no-output history from declaration requests and independent dispatch traces. Round-13 target numbers are not claimed as completed measurements.

Additional quantity/threshold checks on 2026-10-18T00:06:28Z used a read-only JSON parse of the filed round-8/9/11/12 receipts: round 8's 20-row repair inventory, 39/39 selftest and isolated 7/7 versus live seven-unevaluable split; round 9's eight baselines / seven gates / seven unchanged gate scripts; round 11's new replay 11/11 and nine runner-recognized auditor reruns; round 12's 51 source-command requirements and no reported missing key. Existing shard/source controls preserve the 16 finding-token / 15 hold + one note distinction, not a false 16-hold result. The successor battery claim at lines 91–96 is supported by `reports/round-14/fix-battery-roots.md:29-44,81-110`, which names its actual commands, dates, after counts and fail-closed negatives; the retrospective does not relabel old layouts as standard-complete.

The six K1–K6 table rows are reproducibly six taxonomy groups, explicitly not six incidents. The executed-round claim tables contain 15 rows; the three round-13 declarations remain separately deferred. This roster/taxonomy check is in the C07 reproduction command, re-run against the same digest. Historical 14 passed / 1 failed flags remain instrument results, not a conformance-quality score.

Exact final-control wrapper (three blocks executed concurrently at the final observation above):

```sh
export TMPDIR="$PWD/.scratch"
python3 - <<'PY'
from pathlib import Path
from hashlib import sha256
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import re, subprocess
p = Path('reports/round-14/loop1-retrospective.md')
assert sha256(p.read_bytes()).hexdigest() == 'c1457e85320f3d4616e5029fed107f0ed4a12f49b41bb2b2d1927f5c3b0d413b'
blocks = re.findall(r'```sh\n(.*?)\n```', p.read_text(), re.S)
assert len(blocks) == 3
with ThreadPoolExecutor(max_workers=3) as pool:
    results = list(pool.map(lambda b: subprocess.run(['bash', '-c', b], text=True, capture_output=True, timeout=120), blocks))
for i, result in enumerate(results, 1):
    print('M' + str(i), 'exit', result.returncode)
    print(result.stdout, end='')
    print(result.stderr, end='')
assert all(r.returncode == 0 for r in results)
print('C08 final controls PASS', datetime.now(timezone.utc).isoformat())
PY
```

## Safety / remaining integration obligations

The source validation receipts were compared byte-for-byte with their admission/rejection revisions at 2026-10-17T23:58:22Z, by M2 at 2026-10-18T00:05:49Z, and in the final rerun at 00:08:31Z. All matched: round 8 `e1694ba`, round 9 `9dc18ec`, round 10 `94ca098`, round 11 `a3f6fce`, round 12 `44070b4`. No filed validator was imported or run by this auditor, and no source receipt or historical byte was overwritten. Only the C07/C08 fragments were written.

The unresolved historical `entries.md` pointer is honestly disclosed, not fixed; external final-report verification, the declared-eight-item resolver crosswalk, SCORECARD/LOG integration, guard/regression acceptance, and actual dispatch evidence remain their owners' responsibilities. A later change to the audited retrospective requires fresh hash-bound checks. This numeric audit does not substitute for overall round-14 acceptance.
