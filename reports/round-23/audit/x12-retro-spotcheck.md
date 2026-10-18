# R23-X12 — retrospective-audit spot check: loop-2 numbers unchanged post-r22

Date: 2026-10-18. Seat: R23-X12 (scribe/audit fragment; the parent integrates into
LOG.md). Scope: read-only spot check that the round-22 loop-2 retrospective
(`reports/round-22/loop2-retrospective.md`) and every headline number it reports
are unchanged after the round-22 close commit `0e81d9d99514631d6717e1ff354d5a5a759aa980`
(the commit that first filed the retrospective) through r23-declare `7b181a5` and the
current working tree. This is a spot check, not a full C07/C08 pointer re-audit, not
admission, promotion, canon clearance, or round-23 acceptance.

Scratch discipline: `export TMPDIR=$PWD/.scratch` before scratch-writing commands;
`PYTHONDONTWRITEBYTECODE=1` throughout; the control below writes nothing (reads,
Git blob comparisons, in-memory negatives only). No round validator was executed.
No filed round-8–22 artifact was modified by this seat; no commit or push.

## Verdict

**UNCHANGED — spot check PASS.** The retrospective still hashes to
`4966516923f3b8e6bc4bba8d203607ee2e76fa51c4154024c93892525ef501a1` (368 lines),
byte-identical at `0e81d9d` (r22 close), `7b181a5` (r23 declare = HEAD), and in the
working tree. All four upstream shards and both fix fragments match the C08-recorded
digests and are blob-identical to their r22-close versions. All 17 number-source
artifacts are blob-identical across r22-close → r23-declare → worktree, and every
headline number re-derives to the filed values.

## Method and counts (control below, measured 2026-10-18T15:15:06Z)

1. **Digest + blob identity** — SHA-256 plus `git show <rev>:path` byte comparison
   of the retrospective at `0e81d9d`, `7b181a5`, worktree: identical; 368 lines.
   (The retrospective first appears in history at `0e81d9d`; it is absent at
   r22-declare `cd9c8e4`, where only worker fragments existed — expected parent
   integration at close, not a rewrite.)
2. **Upstream inputs** — 6 files (retro shards `r17/r18/r19/r20-21.md`, fixes
   `snapshot-r17.md`, `r18-supersession.md`): SHA-256 equal to the C08-recorded
   values **and** byte-equal to their r22-close blobs.
3. **Number anchors** — 17 artifacts (r17–r21 `claims.json`+`validation.json`,
   r21 `defects/ledger.json` + `recount/ledger.json`, r11 `validation.json` +
   `recheck/summary.json`, r18 `civ-map-r18.json`, r17
   `d4/expected-holds.fragment.json`, r22 `claims.json`): worktree ==
   r22-close blob == r23-declare blob.
4. **Headline numbers re-derived** (same values the retrospective reports):
   states 4 admitted (18–21) + 1 rejected (17); claim flags 14 pass / 1 fail
   (r17 D); r19 receipt-binding exception preserved (claims `e571894…` vs receipt
   `169c616`); defect queue 23 entries = conformance 9 / process 7 / bookkeeping 7,
   open 13 / closed 5 / observation 5, non-closed routes 18 (== r21 O
   `round22_routes`); recount 63 rows = 39 match + 24 disposition with 52 distinct
   literal commands (== r21 C measurement 63/63/39/24); r11 freshness 147/189 =
   0.7777… and 147/192 = 0.765625, both < 0.95, r11 still failed; r17 civ 7 fixed /
   5 attempted / 16 fragments; r18 map 94 entries / 12 transitions / 82 carried
   with statuses 83 current + 11 stale-fixed; r17 holds fragment (17, 1).
5. **Retrospective structure** — exactly one table row per round 17–21, each row's
   claim roster equal to that round's declared claim IDs; 7 K1–K7 taxonomy rows;
   the r22 declaration holds 3 claims with O items numbered (1)–(6).

## In-flight observations (other seats' writes; neither is a retrospective anchor)

Observed 2026-10-18T15:15–15:16Z via `git status`/`git diff HEAD`:

- `reports/round-22/fixes/regression.md` differs from HEAD (+122/−54): the
  IN-PROGRESS r22 O12 stub is being rewritten into a closing GREEN verdict in the
  working tree. The retrospective does **not** cite this path (literal scan: 0
  matches), so no retrospective number is affected. Committed history of the file
  is untouched.
- `examples/culture-d2/expected-holds.json` appeared modified mid-check (5+/2−):
  an r23 combined-source re-pin (new `projector_sha256` `2819f687…`, prior pin
  preserved under `supersedes_pins`, new frozen generation
  `tools/gates/frozen/round-23/repin-d2/MANIFEST.tsv` — the sanctioned new-row
  re-pin pattern). The retrospective cites this path **0** times; its D2
  byte-identity numbers bind to committed revisions (verified blob-stable in
  anchor set via r21 recount citations).

Both are consistent with the r23 O-lane assignments (successor pins, regression
green) and are recorded here as observations only; their own controls belong to
the seats that wrote them.

## Negative controls (2026-10-18T15:16:03Z; in-memory, no fixtures)

Retroactive r17 admission rejected; swapped queue statuses (13↔5) rejected;
"all 63 recount rows matched" rejected; r19 claims/receipt baseline equality
rejected; retrospective digest drift rejected (in-memory appended byte detected;
re-read digest still equal).

## Reproduction control

Run from the lane root, read-only:

```sh
export TMPDIR="$PWD/.scratch"
export PYTHONDONTWRITEBYTECODE=1
python3 - <<'PY'
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
import json, re, subprocess
load = lambda p: json.loads(Path(p).read_text())
print('AUDIT_UTC', datetime.now(timezone.utc).isoformat())
R22CLOSE = '0e81d9d99514631d6717e1ff354d5a5a759aa980'
retro = Path('reports/round-22/loop2-retrospective.md')
raw = retro.read_bytes()
digest = sha256(raw).hexdigest()
assert digest == '4966516923f3b8e6bc4bba8d203607ee2e76fa51c4154024c93892525ef501a1'
assert raw == subprocess.check_output(['git', 'show', R22CLOSE + ':reports/round-22/loop2-retrospective.md'])
assert len(raw.decode().splitlines()) == 368
recorded = {
 'reports/round-22/retro/r17.md': '72ddd5d07a99b9645cb795d2b6d616845439f0e286737cd6fa9606033eeba9b9',
 'reports/round-22/retro/r18.md': '6137ae968ad103b3771d71b164e763543ee8a39fdf1cba512b1365a9b103b4ed',
 'reports/round-22/retro/r19.md': '71a109cfcb02ddd595e07db5bee33a504a762dd6370876102ebc75d833a3be50',
 'reports/round-22/retro/r20-21.md': 'd8931776794c690e9dd628e1b24fe9b6c1ee13a30d266c660cb679ae882e2853',
 'reports/round-22/fixes/snapshot-r17.md': 'aa14cbb6e96aa10e06fad8d3ca79e9923f655055446fbd763f1376ec439298e5',
 'reports/round-22/fixes/r18-supersession.md': 'dec9a980d1fdbadfa404fbcb16455c6e0c6318334fcb8ed58d63255698175282',
}
for name, want in recorded.items():
    b = Path(name).read_bytes()
    assert sha256(b).hexdigest() == want and b == subprocess.check_output(['git', 'show', R22CLOSE + ':' + name]), name
anchors = [f'reports/round-{n}/{k}' for n in range(17, 22) for k in ('claims.json', 'validation.json')]
anchors += ['reports/round-21/defects/ledger.json', 'reports/round-21/recount/ledger.json',
            'reports/round-11/validation.json', 'reports/round-11/recheck/summary.json',
            'reports/round-18/civ-map-r18.json', 'reports/round-17/d4/expected-holds.fragment.json',
            'reports/round-22/claims.json']
for name in anchors:
    b = Path(name).read_bytes()
    assert b == subprocess.check_output(['git', 'show', R22CLOSE + ':' + name]), name
accept = {17: False, 18: True, 19: True, 20: True, 21: True}
flags, states = Counter(), Counter()
for n, expected in accept.items():
    v = load(f'reports/round-{n}/validation.json'); c = load(f'reports/round-{n}/claims.json')
    assert v['acceptance_checks_passed'] is expected
    assert set(v['claims']) == {r['id'] for r in c['claims']}
    flags.update(r['passed'] for r in v['claims'].values())
    states['admitted' if expected else 'rejected'] += 1
    if n == 19:
        assert c['baseline_revision'] == 'e5718945a1ab0a0c3db955338d2cae77d68fd348'
        assert v['baseline_revision'] == '169c616' and c['baseline_revision'] != v['baseline_revision']
    else:
        assert c['baseline_revision'] == v['baseline_revision']
assert states == {'admitted': 4, 'rejected': 1} and flags == {True: 14, False: 1}
q = load('reports/round-21/defects/ledger.json')['entries']
assert len(q) == len({r['id'] for r in q}) == 23
assert Counter(r['classification'] for r in q) == {'conformance': 9, 'process': 7, 'bookkeeping': 7}
assert Counter(r['status'] for r in q) == {'open': 13, 'closed': 5, 'observation': 5}
assert sum(r['status'] != 'closed' for r in q) == load('reports/round-21/validation.json')['claims']['O']['measurement']['round22_routes']['value'] == 18
rows = load('reports/round-21/recount/ledger.json')
assert len(rows) == 63 and Counter(r['verdict'] for r in rows) == {'match': 39, 'disposition': 24}
assert len({r['command'] for r in rows}) == 52
m = load('reports/round-21/validation.json')['claims']['C']['measurement']
assert (m['source_command_total']['value'], m['recounted_rows']['value'], m['matched_rows']['value'], m['dispositioned_rows']['value']) == (63, 63, 39, 24)
f = load('reports/round-11/validation.json')['claims']['F']; s = load('reports/round-11/recheck/summary.json')
assert f['passed'] is False and f['measurement']['stable'] == s['stable'] == 147
assert f['measurement']['rows_rechecked'] == 189 and s['rows_reckecked'] == 192 and 147/189 < .95 and 147/192 < .95
c17 = load('reports/round-17/validation.json')['claims']['C']['measurement']
assert (c17['fixed_count']['value'], c17['attempted_count']['value'], c17['fragments']['value']) == (7, 5, 16)
civ = load('reports/round-18/civ-map-r18.json')
assert (len(civ['entries']), len(civ['transitions']), civ['rows_carried_verbatim']) == (94, 12, 82)
assert Counter(r['status'] for r in civ['entries']) == {'current': 83, 'stale-fixed': 11}
frag = load('reports/round-17/d4/expected-holds.fragment.json')
assert (len(frag['holds']), len(frag['notes'])) == (17, 1)
s = raw.decode()
for n in range(17, 22):
    tab = re.findall(rf'^\| {n} —.*$', s, re.M)
    assert len(tab) == 1
    ids = re.findall(r'\b([CODA])\b', tab[0].split('|')[2])
    assert set(ids) == {r['id'] for r in load(f'reports/round-{n}/claims.json')['claims']} and len(ids) == 3
assert len(re.findall(r'^\| K[1-7] ', s, re.M)) == 7
decl = load('reports/round-22/claims.json')['claims']
assert len(decl) == 3
assert re.findall(r'\((\d+)\)', next(r for r in decl if r['id'] == 'O')['before']) == ['1', '2', '3', '4', '5', '6']
assert b'round-22/fixes/regression' not in raw and b'culture-d2/expected-holds' not in raw
print('changed_vs_HEAD (observation only):', subprocess.check_output(['git', 'diff', '--name-only', HEAD]).decode().split() if (HEAD := subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip()) else [])
print('retro_digest', digest, '| lines', len(s.splitlines()), '| states', dict(states), '| flags', dict(flags))
print('queue 23 = 9/7/7 classes, 13/5/5 statuses, 18 routes | recount 63 = 39+24, 52 commands')
print('r11 147/189 <0.95, 147/192 <0.95 | r17 civ 7/5/16 | r18 map 94/12/82 (83+11) | holds fragment (17,1)')
neg = {
 'retroactive_r17_admission_rejected': not load('reports/round-17/validation.json')['acceptance_checks_passed'],
 'swapped_queue_statuses_rejected': Counter(r['status'] for r in q) != {'open': 5, 'closed': 13, 'observation': 5},
 'all_recount_matched_claim_rejected': sum(r['verdict'] == 'match' for r in rows) != len(rows),
 'r19_binding_equality_rejected': load('reports/round-19/claims.json')['baseline_revision'] != load('reports/round-19/validation.json')['baseline_revision'],
 'retro_digest_stability': sha256(retro.read_bytes()).hexdigest() == digest,
 'tampered_digest_detected': sha256(retro.read_bytes() + b'x').hexdigest() != digest,
}
assert all(neg.values()), neg
print('negative_controls', neg)
print('X12 SPOT CHECK PASS')
PY
```

Initial execution: exit 0 at 2026-10-18T15:15:06Z (positive sections) with
negatives re-confirmed at 15:16:03Z; no lane file was written by the control. If
the retrospective digest ever changes, this spot check must be re-run and the
change dispositioned before any "loop-2 numbers unchanged" claim is repeated.

## Limits

Spot check only: it re-derives the retrospective's headline numbers and binds
their sources to committed revisions; it does not re-run C07's full 48-citation
pointer audit, C08's eight-command shard replay, or any historical validator, and
it makes no claim about rounds 22–24 completion, the r23 O/D claims, freshness
thresholds, or lore/canon clearance.
