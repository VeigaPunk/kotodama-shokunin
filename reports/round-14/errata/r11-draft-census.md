# R14-O08 — round-11 draft census reconciliation

- Axis: O / operability; supporting controls: calibration and filed-artifact integrity.
- Routed finding: `reports/round-12/defects/routed.md:82-88`, R11-SWEEP-02.
- Disposition: **census resolved-by-documentation with control C1**. This new record corrects the settled reading without rewriting the historical draft, summary, receipt, or runner. The broader C2 sentinel detected a concurrent, separately owned tracker append; its non-green result is recorded below and is not a claim that the shared tree stayed unchanged.
- Evidence inspected: 2026-10-17; lane HEAD `a7bc9e9ff05a57515c5efaaa7e50116eb30938ff`.
- Scope: census reconciliation only. This is not a replacement round-11 report/SHONEN section, a new round-11 execution, an admission, or an operator threshold amendment. R11-SWEEP-01 final-report integration remains separate.

## Historical snapshot versus settled measurements

The draft explicitly dates itself to an unfinished wave: `reports/round-11/report-draft.md:3-9` says the fragments had landed by 22:12Z and that acceptance numbers were not a settled tree's. Its F section (`:135-155`) and measurement row (`:207`) record **149 stable / 43 unstable across 192 receipts**, reported there as 77.6%. Retain that value as the scribe's **2026-10-17 22:12Z historical snapshot**, not the final census. The same section's **117 rows / 93 stable / 24 unstable, 0.795** is an even earlier runner snapshot, not another settled denominator.

For the settled all-row census, use `reports/round-11/recheck/summary.json:4-8`: **192 rows, 147 stable, 45 unstable, zero undispositioned**. Its filed key is spelled `rows_reckecked`; do not silently rename the filed key. Control C1 independently recounts the row receipts and verifies their validation input pins.

The settled channels are distinct, not contradictory:

| Measurement channel | Numerator / denominator | Result | Source |
|---|---|---|---|
| All filed row receipts | 147 stable / 192 rows | 0.765625 = 76.5625%; summary stores 0.7656 | `reports/round-11/recheck/summary.json:4-8`; C1 |
| Byte-comparable validation population | 147 stable / 189 comparable rows | 0.7777777777777778 = 77.7778%; failure text rounds to 0.778 | `reports/round-11/validation.json:544-555`; C1 |

The difference is exactly `row-067.json`, `row-068.json`, and `row-069.json` under `reports/round-11/recheck/`: each has `new_hash: null`, `stable: false`, `comparison: not-applicable`, and a named cause explaining the unfiled prose-control script (`:11-18` in each receipt). Their semantic reconstructions do **not** establish byte-hash stability. They remain in the all-row census but are excluded from both the validation stability denominator and its minimum re-run count. The other **42** unstable rows are in the comparable population: **147 + 42 = 189; 189 + 3 = 192; 42 + 3 = 45**. This is the filed runner's policy (`reports/round-11/run-validation.py:1402-1429,1442-1459`) and is disclosed in the filed receipt (`reports/round-11/validation.json:864-865`), not a new exemption introduced by this erratum.

All settled counts above were reproduced by C1 on **2026-10-17T23:57:51Z**. The old draft counts are attributed historical observations, not a claim that this worker reproduced that earlier tree or identified every row that changed between snapshots.

## Verdict and integration wording

The declaration requires **>=95% hash-stable** (`reports/round-11/claims.json:27-32`). Neither settled denominator reaches it. The filed receipt has **D=true, O=true, F=false, acceptance_checks_passed=false**, with the sole round failure at `reports/round-11/validation.json:639-641`: `claim F: recheck: stability 0.778 < required 0.95`. These flags/failure are verified by C1; round 11 remains **REJECTED**.

`SCORECARD.md:184-205` and `LOG.md:3010-3029` preserve that verdict, although their 0.778 shorthand must be read as **147/189**, never 147/192. `LOG.md:3036-3038` already states the denominator correction. Any new integration/retrospective entry should carry both populations rather than copy the ambiguous shorthand.

Settled wording for the integrating scribe:

> Round 11 remains REJECTED: D/O verified, F failed its declared >=95% threshold. Coverage is 192/192 ledger rows; the settled all-row census is 147 stable / 45 unstable (147/192 = 76.5625%, filed summary 0.7656). The validation acceptance channel excludes three dispositioned, non-byte-comparable prose-control rows and measures 147/189 = 77.7778% (diagnostic 0.778). Every unstable row is dispositioned; disposition does not make it hash-stable. The draft's 149/43 census remains a dated in-flight snapshot.

This record does not retrospectively lower the threshold or claim that legitimate/environmental drift should have passed it. The operator's calibration question remains separate from the failed historical claim.

## C1 — read-only census, denominator, verdict, and source-binding control

Run from the lane root; observed **2026-10-17T23:57:51Z**, exit **0**. This reads JSON and Git blobs only; it neither imports nor runs any round validator.

```sh
export TMPDIR="$PWD/.scratch"
date -u +%Y-%m-%dT%H:%M:%SZ
python3 - <<'PY'
import hashlib, json, pathlib, re, subprocess
root = pathlib.Path('reports/round-11')
ps = sorted((root / 'recheck').glob('row-*.json'))
rows = [json.loads(p.read_text()) for p in ps]
summary = json.loads((root / 'recheck/summary.json').read_text())
validation = json.loads((root / 'validation.json').read_text())
f = validation['claims']['F']['measurement']
nulls = [p.name for p, r in zip(ps, rows) if r.get('new_hash') is None]
valid_hashes = [r for r in rows if re.fullmatch(r'[0-9a-f]{64}', r.get('new_hash') or '')]
stable = sum(r.get('stable') is True for r in rows)
unstable = sum(r.get('stable') is False for r in rows)
assert [p.name for p in ps] == [f'row-{i:03d}.json' for i in range(192)]
assert (len(rows), stable, unstable, len(valid_hashes)) == (192, 147, 45, 189)
assert nulls == ['row-067.json', 'row-068.json', 'row-069.json']
assert all(r.get('stable') is False and r.get('drift_cause') for r in rows if r.get('new_hash') is None)
assert (summary['rows_reckecked'], summary['stable'], summary['unstable'], summary['undispositioned']) == (192, 147, 45, 0)
assert summary['stability'] == round(stable / len(rows), 4)
assert (f['ledger_rows'], f['rows_rechecked'], f['stable'], f['unstable'], f['unreproducible_dispositioned']) == (192, 189, 147, 42, 3)
assert f['stability'] == stable / len(valid_hashes)
assert f['summary'] == {'rows': 192, 'stable': 147, 'unstable': 45}
assert validation['thresholds']['F']['min_stability'] == 0.95
assert stable / len(rows) < 0.95 and f['stability'] < 0.95
assert validation['claims']['D']['passed'] is True and validation['claims']['O']['passed'] is True
assert validation['claims']['F']['passed'] is False and validation['acceptance_checks_passed'] is False
assert validation['failures'] == ['claim F: recheck: stability 0.778 < required 0.95']
inputs = ['reports/round-11/claims.json', 'reports/round-11/recheck/summary.json'] + [p.as_posix() for p in ps]
assert all(hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest() == validation['input_sha256'][p] for p in inputs)
assert hashlib.sha256((root / 'run-validation.py').read_bytes()).hexdigest() == validation['runner_sha256']
for p in [root / 'report-draft.md', root / 'recheck/summary.json', root / 'validation.json', root / 'run-validation.py', root / 'claims.json']:
    assert p.read_bytes() == subprocess.check_output(['git', 'show', f'HEAD:{p.as_posix()}'])
print('PASS: contiguous rows=192 stable=147 unstable=45 no_hash=3 comparable=189')
print('all-row stability:', stable / len(rows), 'summary stored:', summary['stability'])
print('comparable stability:', f['stability'], 'comparable unstable:', f['unstable'])
print('no_hash:', ', '.join(nulls))
print('threshold=0.95; D=True O=True F=False acceptance=False; sole failure:', validation['failures'][0])
print('PASS: census input pins, runner pin, and committed source bytes agree; no round validator executed')
PY
```

## C2 — filed-round integrity control

Before writing this erratum, the manifest command below (without its expected-value assertions) ran at **2026-10-17T23:57:30Z**. It hashed the **609 tracked files** under rounds 8–12 into **0829408e91df66b0186b869120e7f04211e0bf95b90aea1ab561731dd47d1f0f**. Re-run this exact fail-closed control after writing the new record; any filed-path or byte change fails rather than being accepted as a refresh.

```sh
export TMPDIR="$PWD/.scratch"
date -u +%Y-%m-%dT%H:%M:%SZ
python3 - <<'PY'
import hashlib, pathlib, subprocess
paths = sorted(subprocess.check_output(['git', 'ls-files', '-z', '--', 'reports/round-8', 'reports/round-9', 'reports/round-10', 'reports/round-11', 'reports/round-12']).decode().split('\0'))
paths = [p for p in paths if p]
h = hashlib.sha256()
for name in paths:
    h.update(name.encode() + b'\0' + hashlib.sha256(pathlib.Path(name).read_bytes()).digest())
assert len(paths) == 609
assert h.hexdigest() == '0829408e91df66b0186b869120e7f04211e0bf95b90aea1ab561731dd47d1f0f'
print('PASS: rounds 8-12 tracked files:', len(paths), 'manifest:', h.hexdigest())
PY
```

### Observed after-control and cross-worker limitation

Both published shell blocks were extracted directly from this Markdown and executed on **2026-10-17T23:58:46Z**. **C1 passed (exit 0)** with the settled counts, denominator split, rejected verdict, validation input pins, runner pin, and committed round-11 source bytes all agreeing. **C2 failed (exit 1, digest assertion)**; do not report global filed-round integrity as green.

Read-only diagnosis on **2026-10-17T23:58:58Z** used `git diff -- reports/round-10/findings-tracker.json`, the C2 manifest calculation without assertions, and SHA-256 of that file versus `git show HEAD:reports/round-10/findings-tracker.json`. The file count remained **609**, but the manifest was **c6b6670598fc3c2a5461dc508f61ab52d606505cdc9d2914e4ab85cf56f97eec**. The sole tracked change under rounds 8–12 was an appended top-level `errata` key identifying **R14-O03**, pointing to `reports/round-14/fix-tracker-pointer.md`. The tracker SHA-256 changed from **5a0ca3de9a058de2b8e772f5f2af0bd5302a04957764e3639938f00ba496effc** (HEAD) to **4b983ae9237dda1b46fba59fac2ce8731a1a924ae9672925757bcc4ebc30def2** (observed working tree). A repeat `git status --short -- reports/round-8 reports/round-9 reports/round-10 reports/round-11 reports/round-12` plus `git diff --numstat -- reports/round-10/findings-tracker.json` at **2026-10-17T23:59:32Z** still showed only that change (**28 additions / 1 deletion**).

This worker neither authored nor reverted the tracker append. Its acceptability under the append-only-new-key rule is for the R14-O03 owner/integrator to disposition; the all-byte sentinel intentionally does not normalize or silently bless it. It does not change the round-11 census evidence verified by C1. Separately, a read-only Python assertion at **2026-10-17T23:58:58Z** checked `all(r.get('drift_cause') for r in rows if r.get('stable') is False)` over the same row JSON files and passed, supporting the all-unstable-rows-dispositioned wording above.

Only `reports/round-14/errata/r11-draft-census.md` is authored by this worker. The parent integrates any LOG/SCORECARD/routed-resolution update and the separately owned C2 observation. This worker has not changed shared bookkeeping, filed-round bytes, or Git history, and makes no whole-round regression or admission claim.
