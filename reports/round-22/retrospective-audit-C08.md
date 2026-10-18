# R22-C08 — retrospective number audit

Axis: calibration. Scope: independent re-derivation of the loop-2 checkpoint, not re-admission of prior rounds. Date: 2026-10-18. **Numeric reproduction and calibrated reporting PASS** for retrospective SHA-256 `4966516923f3b8e6bc4bba8d203607ee2e76fa51c4154024c93892525ef501a1` (368 lines). The delivered eight-control wrapper passed at 14:49:02Z, including M1/M2, all four source shards and two isolated scanner/replay controls. C08-F07 is fixed by the owner. The one remaining prospective local pointer is tracked separately by C07; no overall R22 acceptance is asserted.

## Findings the retrospective must disposition

- **C08-F01 — amendment counting boundary.** An unqualified “two operator amendments” is not the complete lane history. `LOG.md:3048-3080` and Git subjects identify two structural changes (GLM additions; expand cancellation/GLM pinning) plus one provider-only designation (R19 on hyper). If “two” is retained, explicitly exclude the separately counted provider substitution. The three resolvable revisions are `51e5901`, `9437788`, `3dba77a`; none is a new loop-2 admission.
- **C08-F02 — do not collapse the route populations.** R21's defect ledger contains 23 rows: 13 open, 5 closed, 5 observation; classes are conformance 9, process 7, bookkeeping 7. R21's validator counts 18 routes because it routes every non-closed row, including observations. R22's six declared O items are a scoped integration worklist, not the cardinality of that historical ledger or its routed-note headings. The D4 bleed is the separate D claim.
- **C08-F03 — R17/R18 hold counts are different contracts.** R17 has competing declarations 6/0/0 and 17/1/0; R18 verifies the emitted 15/1/0 set. Gate 19/19 and D2 byte identity are real controls, but do not establish equality to either original declaration or close the disclosed D2 rank carry. Keep R17 rejected and call R18 an architectural/delivered-pipeline repair, not retrospective satisfaction of the entire R17 claim.
- **C08-F04 — request, reported completion and runtime evidence differ.** Every R17–R21 declaration requests 64 workers (320 requested seat-rounds); R17 targets allocate 60. LOG reports completions 30/19/17/20/20 (106), but those are operator-reported figures, not independent dispatch traces. R19's availability receipt still has `completed_workers: null`; the green acceptance receipt has no completion field. Do not fill the historical field or infer completion from admission.
- **C08-F05 — keep historical versus current evidence channels.** Filed R20 links are 102/102; R21's current pair is 105/105, with 27 claims (16 supported, 7 partial, 4 unresolved). Raw match count is 39/63, not “100% matched”; all 63 were covered as 39 match + 24 disposition. R20's README/receipt counts sum to 199 with linguistics 19, not the declaration/prose 20. R18's map has 94 rows, 12 transitions and 82 carried rows; its raw statuses are 83 current + 11 stale-fixed, not 94 freshly verified civilizations. Five R17 attempt rows must not disappear into the map's terminal-current label.
- **C08-F06 — baseline bindings and loop boundary.** Claims/receipts agree on the declared baseline except R19's receipt (`169c616`, the declaration) versus claims (`e571894…`, R18 admit). Closure prose also calls declaration commits “baseline” for R17/R18/R20/R21. New correction records are needed, not rewritten historical receipts. The R17–21 checkpoint is four admissions and one rejection, not completion of the amended eight-round R17–24 loop.

## Re-derived source numbers

The reproduction command below reads stored artifacts only and pins the five receipts to their closure Git blobs. All quantities in this section were measured 2026-10-18 by that command or the read-only selectors it contains.

- Receipt final states: R17 rejected; R18/R19/R20/R21 admitted. Stored claim flags: 14 passed, 1 failed (R17 D). These are filed harness results, not a fresh literal-threshold recertification.
- R17 C: 12 targets = 7 fixed + 5 attempted; 16 evidence fragments. D components: 12. Requested seats 64 versus target allocation 60.
- R18 map: 94 rows; 12 transition rows; 82 unchanged rows; statuses 83 current + 11 stale-fixed; terminal statuses 94 current. R18 expected/observed equality: 15 holds + 1 note, 0 fails, 16 details pinned, no extra/missing rows. Original R17 fragment: 17 holds + 1 note, distinct from the six-hold delivered-tree declaration reported in the reviews.
- R19 corpus: 10 new entries (5 verification + 5 synthesis); admission totals 199 entries, versus 189 at R17/R18 closure. R20/R21 remain 199: civilizations 94, culture-material 18, linguistics 19, myth-symbol 19, synthesis 29, verification 20.
- R21 recount: 63 `(round, command)` rows = 39 match + 24 disposition; per round 11/34/1/17 for R17/18/19/20. The filed validator's 18 integrator rows are included in the 24 dispositions, not an additional population.
- R21 defect ledger: 23 rows = 13 open + 5 closed + 5 observation; 18 non-closed routes. Classes: conformance 9, process 7, bookkeeping 7. Round distribution: R17 4, R18 3, R19 7, R20 9.
- R21 repair controls: D4 19/19; D2 pre/post stdout SHA-256 identical, 16/16; repin-D2 replay 11/11 after the ignored log prerequisite was restored in its isolated clone. The old D4 two-row generation is not that replay.
- Original paused freshness threshold: 147/189 = 0.7777777777777778 and 147/192 = 0.765625, both below 0.95. Loop-2's 39/63 = 0.6190476190476191 is a different command-recount population, not a freshness score or a proposed replacement threshold.

## Read-only reproduction control

Run from the lane root; no historical round validator is imported or executed. Observation date: 2026-10-18.

```sh
export TMPDIR="$PWD/.scratch"
python3 - <<'PY'
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
import json, subprocess
load = lambda p: json.loads(Path(p).read_text())
print('AUDIT_UTC', datetime.now(timezone.utc).isoformat())
closures = {
    17: '3dd3754207032cb81f5fb3e202fe85cf79211339',
    18: 'e5718945a1ab0a0c3db955338d2cae77d68fd348',
    19: 'caf1beac19b55f3bbce47e4a9e7e8710cc1c581d',
    20: '35b6797b42d48bec52e1e3ddba1f3afc9bb85046',
    21: '46a03257ee75dd8f685a105e47da3f45a0154172',
}
vs = {n: load(f'reports/round-{n}/validation.json') for n in closures}
assert {n: d['acceptance_checks_passed'] for n, d in vs.items()} == {
    17: False, 18: True, 19: True, 20: True, 21: True}
assert Counter(v['passed'] for d in vs.values() for v in d['claims'].values()) == {True: 14, False: 1}
print('states', {n: d['acceptance_checks_passed'] for n, d in vs.items()})
print('claim_flags', Counter(v['passed'] for d in vs.values() for v in d['claims'].values()))
for n, rev in closures.items():
    p = f'reports/round-{n}/validation.json'
    raw = Path(p).read_bytes()
    assert raw == subprocess.check_output(['git', 'show', rev + ':' + p]), p
    c = load(f'reports/round-{n}/claims.json')
    t = load(f'reports/round-{n}/targets.json')
    subprocess.run(['git', 'cat-file', '-e', c['baseline_revision'] + '^{commit}'], check=True)
    print('receipt', n, sha256(raw).hexdigest())
    print('binding', n, 'claims', c['baseline_revision'], 'receipt', vs[n]['baseline_revision'])
    print('workers', n, 'requested', c['workers'], 'target_allocation', sum(t['workers'].values()), 'route', c['requested_model'])
    ps = [p for p in subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', rev, '--', 'corpus/knowledge'], text=True).splitlines() if p.endswith('.md')]
    print('corpus_at_close', n, len(ps), Counter(p.split('/')[2] for p in ps))
c17 = vs[17]['claims']['C']['measurement']
assert (c17['fixed_count']['value'], c17['attempted_count']['value'], c17['fragments']['value']) == (7, 5, 16)
print('r17_coverage', {k: c17[k]['value'] for k in ('fixed_count', 'attempted_count', 'fragments')})
m18 = load('reports/round-18/civ-map-r18.json')
assert len(m18['entries']) == 94 and len(m18['transitions']) == 12 and m18['rows_carried_verbatim'] == 82
assert Counter(r['status'] for r in m18['entries']) == {'current': 83, 'stale-fixed': 11}
print('r18_map', len(m18['entries']), len(m18['transitions']), m18['rows_carried_verbatim'], Counter(r['status'] for r in m18['entries']), 'terminal', m18['terminal_status_counts'])
h = vs[18]['claims']['D']['measurement']['hold_set']
assert h['expected'] == h['observed'] and h['observed_counts'] == {'hold': 15, 'note': 1, 'fail': 0}
assert h['details_pinned'] == 16 and not h['missing'] and not h['extra']
f = load('reports/round-17/d4/expected-holds.fragment.json')
assert (len(f['holds']), len(f['notes'])) == (17, 1)
print('r18_delivered_holds', h['observed_counts'], 'details', h['details_pinned'], 'r17_fragment', f['counts'])
rows = load('reports/round-21/recount/ledger.json')
assert len(rows) == 63 and Counter(r['verdict'] for r in rows) == {'match': 39, 'disposition': 24}
assert len({(r['round'], r['command']) for r in rows}) == 63
print('r21_recount', len(rows), Counter(r['verdict'] for r in rows), Counter(r['round'] for r in rows))
entries = load('reports/round-21/defects/ledger.json')['entries']
assert len(entries) == 23 and Counter(r['status'] for r in entries) == {'open': 13, 'closed': 5, 'observation': 5}
assert Counter(r['classification'] for r in entries) == {'conformance': 9, 'process': 7, 'bookkeeping': 7}
print('r21_defects', len(entries), Counter(r['status'] for r in entries), Counter(r['classification'] for r in entries), Counter(r['round'] for r in entries))
print('non_closed_routes', sum(r['status'] != 'closed' for r in entries))
m21 = vs[21]['claims']['C']['measurement']
assert (m21['recounted_rows']['value'], m21['matched_rows']['value'], m21['dispositioned_rows']['value']) == (63, 39, 24)
a21 = vs[21]['claims']['A']['measurement']
print('r21_v3', a21['uncertainty_census']['value'], a21['handoff_link_counts']['filed'], a21['handoff_link_counts']['replayed'])
assert a21['uncertainty_census']['value']['statuses'] == {'supported': 16, 'partial': 7, 'unresolved': 4}
assert a21['handoff_link_counts']['filed'] == [102, 102, 0] and a21['handoff_link_counts']['replayed'] == [105, 105, 0]
print('r19_worker_completion', load('reports/round-19/availability.json')['completed_workers'])
import re
log = Path('LOG.md').read_text()
chunk = log[log.index('## 2026-10-18 — Round 17 REJECTED'):]
completions = [int(x) for x in re.findall(r'(\d+)/64 completed', chunk.split('## 2026-10-18 — Round 22')[0])]
assert completions == [30, 19, 17, 20, 20]
requested = sum(load(f'reports/round-{n}/claims.json')['workers'] for n in closures)
print('operator_reported_completions', completions, sum(completions), 'declared_requested', requested)
for rev in ('51e5901', '9437788', '3dba77a'):
    print('amendment', subprocess.check_output(['git', 'show', '-s', '--format=%H %ad %s', '--date=iso-strict', rev], text=True).strip())
print('distinct_ratios', 147/189, 147/192, 39/63)
assert 147/189 < .95 and 147/192 < .95
negative_controls = {
    'retroactive_r17_admission_rejected': not vs[17]['acceptance_checks_passed'],
    'swapped_statuses_rejected': Counter(r['status'] for r in entries) != {'open': 5, 'closed': 13, 'observation': 5},
    'all_match_claim_rejected': sum(r['verdict'] == 'match' for r in rows) != len(rows),
    'r18_zero_note_claim_rejected': h['observed_counts']['note'] != 0,
    'linguistics_20_claim_rejected': vs[20]['claims']['C']['measurement']['counts']['linguistics'] != 20,
    'completed_count_not_evidenced': load('reports/round-19/availability.json')['completed_workers'] is None,
    'freshness_denominator_conflation_rejected': round(147/192, 3) != .778,
}
assert all(negative_controls.values())
print('numeric_negative_controls', negative_controls)
print('C08 source counts PASS; historical receipts unchanged')
PY
```

The initial version of this reproduction block exited 0 at 2026-10-18T14:41:42Z. Independent numeric-positive and numeric-negative controls ran at 14:42:02Z: the genuine state/status/match values passed; retroactive R17 admission, swapped ledger statuses, “all rows matched”, zero R18 notes, linguistics 20, fabricated R19 completion and the incorrect all-row freshness equation were rejected. The command above incorporates those negatives and separately derives the operator-reported 106/320 completion/request figures.

## Consolidated-text audit — first delivered revision

The retrospective dependency was detected at 2026-10-18T14:43:43Z after two 60-second intervals, within the polling bound. Independently executed M1/M2 blocks both exited 0 at 14:43:37Z against retrospective SHA-256 `16b66788d4af85a8f924c4aaa3f300dc0f36353d82ed470110aa357ae693ae9f` (311 lines), with the bytes unchanged across those runs. The seven K1–K7 taxonomy rows enumerate every one of the 23 historical ledger IDs exactly once. All five per-round claim-ID rosters match their declarations (15 claim rows total).

The substantive qualifications in C08-F01–F06 are incorporated: two structural amendments plus the provider designation; different ledger/route populations; the qualified R17/R18 repair; R19's unknown completion; stored-versus-current readings; and the receipt-baseline exception/full-loop boundary. The freshness operator question is prospective and does not relax the old threshold.

**C08-F07 — minor reproduction-pointer defect, integration correction requested.** The six-item O paragraph attributes its count to M1, but the audited M1 only asserts three axis claims and does not count the six enumerated items. The total six is correct and independently reproduced below from the O declaration's `(1)`–`(6)` markers. Add that same control to M1 or remove the inaccurate M1 attribution. This is a pointer-to-control error, not evidence of a seventh O item or an incorrect six-item worklist; it remains open until the retrospective owner updates the text/control.

At 14:45:00Z, this additional read-only control passed. An initial audit-only shorthand parser undercounted the sampled commands because it collapsed two distinct multiline scripts into the common `python3 - <<'PY'` heading; expanding the actual filed bodies yields the correct 23. A separate initial claim-roster regex incorrectly consumed `D` as a slash suffix; the corrected whole-token control below verifies all declared IDs. Neither parser issue changes a source artifact or its historical measurement.

```sh
export TMPDIR="$PWD/.scratch"
python3 - <<'PY'
from pathlib import Path
from datetime import datetime, timezone
import json, re
load = lambda p: json.loads(Path(p).read_text())
print('AUDIT_UTC', datetime.now(timezone.utc).isoformat())
s = Path('reports/round-21/recount/audit.md').read_text()
heads = re.findall(r'^\| `([^`]+)`', s, re.M)
multiline = re.findall(r"```text\n(python3 - <<'PY'.*?)\n```", s, re.S)
commands = {c for c in heads if "<<'PY'" not in c} | set(multiline)
assert (len(heads), len(set(heads)), len(multiline), len(commands)) == (24, 22, 2, 23)
print('r21_audit_sample', 'table_rows', len(heads), 'distinct_full_commands', len(commands))
s = Path('reports/round-20/ledger-snapshot.md').read_text()
counts = [int(x) for x in re.findall(r'^\| (?:byte-identical|value-identical|moved, cause|run in its intended form).*?\*\*(\d+)\*\*', s, re.M)]
assert counts == [110, 15, 50, 1] and sum(counts) == 176 and sum(counts) + 16 == 192
print('r20_reported_snapshot', counts, 'rerun', sum(counts), 'carried', 16, 'attempted', sum(counts)+16)
s = Path('reports/round-22/loop2-retrospective.md').read_text()
for n in range(17, 22):
    rows = re.findall(rf'^\| {n} —.*$', s, re.M)
    assert len(rows) == 1
    ids = re.findall(r'\b([CODA])\b', rows[0].split('|')[2])
    declared = {r['id'] for r in load(f'reports/round-{n}/claims.json')['claims']}
    assert len(ids) == len(set(ids)) == 3 and set(ids) == declared
    print('round_claim_ids', n, ids)
ids = re.findall(r'`((?:R17|R18|R19|R20)-[A-Z0-9-]+)`', s[s.index('| K1'):s.index('Additional findings')])
expected = {r['id'] for r in load('reports/round-21/defects/ledger.json')['entries']}
assert len(ids) == len(set(ids)) == 23 and set(ids) == expected
assert len(re.findall(r'^\| K[1-7] ', s, re.M)) == 7
print('taxonomy', 'groups', 7, 'historical_IDs_exactly_once', len(ids))
o = next(r for r in load('reports/round-22/claims.json')['claims'] if r['id'] == 'O')
numbers = re.findall(r'\((\d+)\)', o['before'])
assert numbers == ['1', '2', '3', '4', '5', '6']
print('r22_declared_O_items', len(numbers))
print('C08 supplementary counts PASS')
PY
```

## Updated calibrated draft — C08-F07 closed

At 2026-10-18T14:47:00Z, the retrospective owner had incorporated the six-item O count directly in M1. It now extracts/asserts the numbered markers and prints `r22_primary_O_items 6`; **C08-F07 is closed by that passing control**, not by an auditor edit of the retrospective.

Audited retrospective SHA-256: `4966516923f3b8e6bc4bba8d203607ee2e76fa51c4154024c93892525ef501a1` (368 lines). Both updated M1/M2 blocks and all four upstream shard commands were independently executed concurrently, all six exit 0 with unchanged document bytes. The shard digests were:

- `reports/round-22/retro/r17.md`: `72ddd5d07a99b9645cb795d2b6d616845439f0e286737cd6fa9606033eeba9b9`.
- `reports/round-22/retro/r18.md`: `6137ae968ad103b3771d71b164e763543ee8a39fdf1cba512b1365a9b103b4ed`.
- `reports/round-22/retro/r19.md`: `71a109cfcb02ddd595e07db5bee33a504a762dd6370876102ebc75d833a3be50`.
- `reports/round-22/retro/r20-21.md`: `d8931776794c690e9dd628e1b24fe9b6c1ee13a30d266c660cb679ae882e2853`.

These controls reproduce the contract distinction (six-hold declaration, 17/1 fragment, 15/1 successor and only two frozen rows plus the pending full-gate row), census and roster counts, and provider-shard comparison. The latter's 62.816667/71.750000/81.866667/52.700000-minute R17–R20 spans are Git declaration-to-close intervals, not provider latency; the parent-reported completion percentages are 46.875/29.6875/26.5625/31.25 and remain explicitly non-independent attendance evidence. The integrated text credits useful R19 output without inventing a demonstrated price/performance benefit.

At 14:46:18Z, the exact reproduction block in `reports/round-22/fixes/snapshot-r17.md` (SHA-256 `aa14cbb6e96aa10e06fad8d3ca79e9923f655055446fbd763f1376ec439298e5`) was also independently executed, exit 0. It creates a fresh in-lane clone and imports only the bounded historical scanner/measurement helpers there, not the full validator/writer. Observed: 16 tracked/present/Git-matching/source-matching files; original fragments/fixed/attempted 0/0/0 with 12 missing targets; relative-root control 16/7/5 and zero missing; original root restored to zero; all 1,030 protected clone paths unchanged. Scratch checkout is ancillary, not a filed historical correction.

At 2026-10-18T14:47:35Z, the new-row/tampered-digest reproduction block in `reports/round-22/fixes/r18-supersession.md` (SHA-256 `dec9a980d1fdbadfa404fbcb16455c6e0c6318334fcb8ed58d63255698175282`) was independently executed in another fresh in-lane clone, exit 0. Successor: 2/2 reproduced, exit 0. Zeroed input digest: exit 2, 1 reproduced / 1 unevaluable, with `snapshot_tampered` and no projection gate launch. All 1,030 protected clone paths remained unchanged. This reproduces the new-row/negative-control numbers without relabeling the old historical manifest as green.

## Hash-bound verification replay

The following command replays M1/M2, the four source-shard commands and the two bounded isolated controls concurrently. It never invokes a full historical round validator. Scratch-writing commands first receive the lane-local TMPDIR; each control creates its own isolated clone. The old source-report and retrospective digests are deliberately strict: an owner edit requires re-auditing, not removal of the check.

```sh
export TMPDIR="$PWD/.scratch"
export PYTHONDONTWRITEBYTECODE=1
python3 - <<'PY'
from pathlib import Path
from hashlib import sha256
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import re, subprocess
inputs = [
    ('reports/round-22/loop2-retrospective.md', '4966516923f3b8e6bc4bba8d203607ee2e76fa51c4154024c93892525ef501a1', 'all'),
    ('reports/round-22/retro/r17.md', '72ddd5d07a99b9645cb795d2b6d616845439f0e286737cd6fa9606033eeba9b9', 'all'),
    ('reports/round-22/retro/r18.md', '6137ae968ad103b3771d71b164e763543ee8a39fdf1cba512b1365a9b103b4ed', 'all'),
    ('reports/round-22/retro/r19.md', '71a109cfcb02ddd595e07db5bee33a504a762dd6370876102ebc75d833a3be50', 'all'),
    ('reports/round-22/retro/r20-21.md', 'd8931776794c690e9dd628e1b24fe9b6c1ee13a30d266c660cb679ae882e2853', 'all'),
    ('reports/round-22/fixes/snapshot-r17.md', 'aa14cbb6e96aa10e06fad8d3ca79e9923f655055446fbd763f1376ec439298e5', 'all'),
    ('reports/round-22/fixes/r18-supersession.md', 'dec9a980d1fdbadfa404fbcb16455c6e0c6318334fcb8ed58d63255698175282', 'last'),
]
jobs, original = [], {}
for name, digest, selection in inputs:
    p = Path(name)
    raw = p.read_bytes()
    assert sha256(raw).hexdigest() == digest, name
    original[p] = raw
    blocks = re.findall(r'```sh\n(.*?)\n```', raw.decode(), re.S)
    chosen = blocks[-1:] if selection == 'last' else blocks
    for n, block in enumerate(chosen, 1):
        jobs.append((name, n, block))
assert len(jobs) == 8

def run(job):
    name, n, block = job
    result = subprocess.run(['bash', '-c', block], text=True, capture_output=True, timeout=120)
    return name, n, result

with ThreadPoolExecutor(max_workers=8) as pool:
    results = list(pool.map(run, jobs))
for name, n, result in results:
    print(name, n, 'exit', result.returncode)
    print(result.stdout, end='')
    print(result.stderr, end='')
assert all(result.returncode == 0 for name, n, result in results)
assert all(raw == p.read_bytes() for p, raw in original.items())
print('C08 eight-control replay PASS', datetime.now(timezone.utc).isoformat())
PY
```

## Final numeric verdict — 2026-10-18T14:51:38Z

**PASS for retrospective SHA-256 `4966516923f3b8e6bc4bba8d203607ee2e76fa51c4154024c93892525ef501a1`.** All three delivered C08 blocks were re-executed concurrently: source census/negative controls, supplementary roster/taxonomy/count-unit controls, and the eight-command historical-shard/isolated-control wrapper all exited 0. Every underlying document digest stayed unchanged. C08-F01–F07 are reflected or controlled in the integrated retrospective; the control-attribution defect F07 is closed by the owner's added M1 assertion.

C07's strict all-literal-pointer replay remains blocked only by the explicitly prospective parent-owned resolution JSON. Numeric calibration is not conditional on pretending that future integration file already exists, and this numeric PASS is not O/D acceptance, a completed amended loop, a freshness-threshold change or a semantic clearance.

The final live preservation comparison at 14:51:38Z reproduced 1,018 unchanged filed R8–R21 paths and manifest `8eaa73b290eb0b85240b79d91d8f2cb5d41b77d2e009003be0072e699a896ff4`; protected status and audit-fragment whitespace diagnostics were empty. Only the C07/C08 audit fragments are this worker's filed output. Ancillary isolated clones are under this lane's `.scratch`; source tools, historical reports, shared bookkeeping and sibling repositories were untouched. No full historical validator, commit or push was executed. No background task remains.
