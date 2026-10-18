# R14-V03 — independent errata and filed-byte verification

- Axis: O / operability; constraints: append-only historical corrections and honest measurement channels.
- Result: **PASS for the independent errata/content and append-only-preservation controls below.** This is not a claim that the entire historical tree has a zero Git diff or that every source report's original broad sentinel passes.
- Fixed reference: round-14 declared baseline `926c86f8be3cc9307f8f10dce55768c290b6f94d`; observed HEAD `a7bc9e9ff05a57515c5efaaa7e50116eb30938ff`.
- No historical round validator was imported or run. Only stdout-only selftests, inspected Markdown controls, JSON/AST reads, Git blob reads, and in-memory negative cases were executed.

## Errata presence and independently re-run content controls

The final preservation command below, run at **2026-10-18T00:04:49.133004+00:00**, verifies that these three nonempty new files exist: `errata/r8-audit-count.md`, `errata/r10-draft-status.md`, and `errata/r11-draft-census.md`, all under `reports/round-14/`. Their content controls were independently executed, not accepted on the strength of another worker's printed result:

- **Round-8 audit count**, `reports/round-14/errata/r8-audit-count.md`, **2026-10-18T00:00:21.838470+00:00**: its exact shell block exits **0**. `python3 tools/harness/r8_checks.py --selftest` reproduces **14/14**, rejects the audit's **12/12** candidate, matches the admission receipt's stdout SHA-256 `25bf2315e6c2f3403a3fc9028720225284b1848f1a91e62ae3808543b0f5ce58`, and leaves the audit/validation/harness protected hashes unchanged. Source-report SHA-256 at execution: `7e68a5c416ba1bbad86d5954028a6be38b83ec2649278bb20c2cb574af405ad9`.
- **Round-10 draft/count reconciliation**, `reports/round-14/errata/r10-draft-status.md`, **2026-10-18T00:00:51.207742+00:00**: its exact shell block exits **0**. Git additions and the filed receipt agree on **10 new entries**, partitioned **3 linguistics / 3 myth-symbol / 2 culture-material / 2 verification**; the obsolete **8** candidate is rejected. Filed draft and receipt bytes equal their admission-commit blobs. The fleet filing assertion is an explicitly limited historical in-lane attestation, not a fresh read of an external report. Source-report SHA-256: `00b4f9d08f1748a10c604e4be0060838567ad647bb5d362a06978aac8299d7dc`.
- **Round-11 census**, `reports/round-14/errata/r11-draft-census.md` C1, **2026-10-18T00:00:21.926584+00:00**, repeated **2026-10-18T00:04:49.196643+00:00**: the exact first shell block exits **0**. **192 contiguous receipts, 147 stable / 45 unstable**, with **3 no-hash rows** and **189 comparable rows**. The all-row ratio is **147/192 = 0.765625**; acceptance uses **147/189 = 0.7777777777777778**. Input pins and runner pin match; D/O remain true, F/acceptance remain false at the unchanged **0.95** threshold. This verifies the honest census, not a final external report or a new admission.
- **Index-updater classification**, `reports/round-14/fix-index-classification.md` first shell block, **2026-10-18T00:02:26.356442+00:00**: exit **0**, all **10** assertions pass. Real inventory: **10 authors, 10 reviewers, 4 auditors, 2 index updaters**. The filed legacy count remains **11 authors**. Removing `C10.md` in memory produces the demonstrated legacy false pass **10** versus corrected **9**, below the unchanged minimum **10**. Extra-updater, updater-only, and unknown-support cases receive no author credit. Filed runner, receipt, and backup updater remain unchanged. This is a documentation/control correction, not a retrofit of the filed runner.
- **Stale-fixed reconciliation**, `reports/round-14/fix-status-conflicts.md` exact shell block, **2026-10-18T00:02:26.399314+00:00**: exit **0**. The **192-row** historical ledger has matching one-based rows **114, 132, 174**, retaining two historical stale-fixed labels and one stale-documented label. Current correction is `stale-documented`; the planted stale-fixed assertion is rejected against retained runner SHA-256 `7eaa36789b4d71ce94ffadc93d2f5e10d6e0ca353df1c233d0ba94f29bff8369`, with no `gate_blob_for_pin` function. All **5** protected paths match HEAD.
- **Runner-hash binding**, independently read and compared with `git show 94ca098b8ab03be52ec80f6925538e5e2c0ed327:reports/round-10/run-validation.py` at **2026-10-18T00:02:51.348113+00:00**: exit **0**. Current runner, admission bytes, and receipt pin agree on full SHA-256 `23d6dc09002fe18c46778ac57d2c34246ab970a9371e7382950ca737d4019b0e`. Receipt SHA-256 is `e8571db918b2c3237256342bd95f241be5661a96019e460990c7d1fe2fc32f94`. `git log --all --full-history --format=%H -- reports/round-10/run-validation.py` yields **1 retained history commit, 0 SHA-256-prefix matches for `4529ac3d`**. That old draft prefix stays `to-verify`; no claim is made that a never-committed snapshot did not exist.

For the preceding Markdown controls, this was the execution mechanism, with `name` and `index` set to the named report and indicated control block:

```sh
export TMPDIR="$PWD/.scratch"
export PYTHONDONTWRITEBYTECODE=1
python3 - <<'PY'
import re, subprocess
from pathlib import Path
for name, index in [
    ('reports/round-14/errata/r8-audit-count.md', 0),
    ('reports/round-14/errata/r10-draft-status.md', 0),
    ('reports/round-14/errata/r11-draft-census.md', 0),
    ('reports/round-14/fix-index-classification.md', 0),
    ('reports/round-14/fix-status-conflicts.md', 0),
]:
    blocks = re.findall(r'^```(?:sh|bash)\n(.*?)^```',
        Path(name).read_text(), re.M | re.S)
    assert subprocess.run(['bash'], input=blocks[index], text=True,
                          timeout=90).returncode == 0, name
PY
```

## Git diff and exact original-byte reconstruction

At **2026-10-18T00:04:49.133004+00:00**, the following fail-closed read-only control exits **0**, printing `APPEND_ONLY_INTEGRITY=PASS`. Counts/digests here come from that command:

- **609** tracked historical paths; **607** have no diff against the declared baseline.
- The only changed historical paths are the exactly allowlisted tracker and defect ledger. No wildcard exception is granted to another filed path.
- Removing only new tracker key `errata` and its separator reconstructs every original tracker byte. Its entry is exactly `R14-O03`; see the independent SHA-differential and negative controls in `verify-2.md`.
- Removing only the new final defect-ledger entry `FRR-14-EXPOSURE` and its separator reconstructs every original ledger byte. All **15** historical entries and their raw formatting are preserved; the array now has **16** entries. Whole-ledger SHA-256 before: `a100c048a2f29374d1da7ab0b147f915c06678c7ab2366a4aef60db235c08a69`; observed after: `106a0141c82c8c2d6f3e7afce907f3f183a8cd5582da35c601604b219edf3eb3`.
- `git diff --check` over rounds 8–12 exits **0** at the final check. An earlier observation at **2026-10-18T00:02:51Z** found trailing whitespace in the then-in-flight new ledger entry; it is absent at this final check. This verifier did not edit it.

```sh
export TMPDIR="$PWD/.scratch"
export PYTHONDONTWRITEBYTECODE=1
python3 - <<'PY'
import datetime, hashlib, json, re, subprocess
from pathlib import Path
base = '926c86f8be3cc9307f8f10dce55768c290b6f94d'
roots = [f'reports/round-{number}' for number in range(8, 13)]
allowed = ['reports/round-10/findings-tracker.json',
           'reports/round-12/defects/ledger.json']
print('date=' + datetime.datetime.now(datetime.timezone.utc).isoformat())
changed = subprocess.check_output(
    ['git', 'diff', '--name-only', base, '--', *roots], text=True).splitlines()
assert changed == allowed, changed
subprocess.run(['git', 'diff', '--exit-code', base, '--', *roots,
    *[':(exclude)' + path for path in allowed]], check=True)
subprocess.run(['git', 'diff', '--check', '--', *roots], check=True)
tracker_before = subprocess.check_output(['git', 'show', base + ':' + allowed[0]])
tracker_after = Path(allowed[0]).read_bytes()
prefix, payload = tracker_after.split(b',\n  "errata": ', 1)
payload = payload.decode()
entries, end = json.JSONDecoder().raw_decode(payload)
assert prefix + payload[end:].encode() == tracker_before
assert len(entries) == 1 and entries[0]['id'] == 'R14-O03'
ledger_before = subprocess.check_output(['git', 'show', base + ':' + allowed[1]])
ledger_after = Path(allowed[1]).read_bytes()
def entry_spans(raw):
    text = raw.decode()
    start = re.search(r'"entries"\s*:\s*\[', text).end()
    spans = []
    while True:
        while text[start].isspace() or text[start] == ',':
            start += 1
        if text[start] == ']':
            break
        entry, end = json.JSONDecoder().raw_decode(text, start)
        spans.append((entry, start, end))
        start = end
    return text, spans
old_text, old_spans = entry_spans(ledger_before)
new_text, new_spans = entry_spans(ledger_after)
assert len(new_spans) == len(old_spans) + 1
assert new_spans[-1][0]['id'] == 'FRR-14-EXPOSURE'
assert [x[0] for x in new_spans[:-1]] == [x[0] for x in old_spans]
assert all(new_text[b[1]:b[2]] == old_text[a[1]:a[2]]
           for a, b in zip(old_spans, new_spans))
assert (new_text[:new_spans[-2][2]] + new_text[new_spans[-1][2]:]).encode() == ledger_before
assert {k: v for k, v in json.loads(ledger_after).items() if k != 'entries'} == {
    k: v for k, v in json.loads(ledger_before).items() if k != 'entries'}
for name in ('r8-audit-count.md', 'r10-draft-status.md', 'r11-draft-census.md'):
    path = Path('reports/round-14/errata') / name
    assert path.is_file() and path.stat().st_size > 0
for number in range(8, 13):
    path = f'reports/round-{number}/validation.json'
    raw = Path(path).read_bytes()
    assert raw == subprocess.check_output(['git', 'show', base + ':' + path])
    print(path, hashlib.sha256(raw).hexdigest())
print('APPEND_ONLY_INTEGRITY=PASS')
PY
```

The command additionally verifies all five validation receipts byte-identical to the fixed baseline. Observed receipt SHA-256 values at the same timestamp:

```text
359932a7debf6ec39f3182ac078ae3e900860efd97831f6b41bfe818b96ccfba  reports/round-8/validation.json
036f84278c4817901413d97839ceba78aa8a367f91579de7505c92800611e418  reports/round-9/validation.json
e8571db918b2c3237256342bd95f241be5661a96019e460990c7d1fe2fc32f94  reports/round-10/validation.json
b5a7841dd427885c599d8a3ca01d5e5bb96470239fab38e52cd7d4d0bba0cab6  reports/round-11/validation.json
773183b2d800c7c19e18b5dba09eb7e9a83e27f621560e6cdd79122baad9af5d  reports/round-12/validation.json
```

## Original broad controls are not silently called green

- Independently re-running the census erratum's C2 at **2026-10-18T00:00:21Z** returns **1** at its original all-file digest assertion. That sentinel intentionally includes the tracker, whose required new errata key changes the whole-file hash. The source report itself later records this caveat. Its C1 remains green.
- `fix-runner-hash.md` Control A at **2026-10-18T00:00:51Z** returns **1** at the broad zero-diff assertion after the runner/receipt/history bindings succeed. Its task-scoped Control B, re-run at **2026-10-18T00:04:49.164782+00:00**, still returns **1** because it requires the entire round-12 ledger to equal HEAD, conflicting with the independently authorized new exposure entry. The preceding SHA-binding and exact append-only controls verify the underlying retained runner and original ledger bytes without mislabeling that delivered command green.
- An initial verifier wrapper demanded exactly one shell fence in the index-classification report; the writer had added a second replay-wrapper fence. That **wrapper assertion**, not the classification control, failed on **2026-10-18T00:00:51Z**. Selecting the inspected first control block produced the green ten-assertion result above.

Integration must retain these distinctions. Do not cite the failed broad sentinels as passing, claim the whole historical tree unchanged, or revert the permitted corrections merely to obtain a zero diff. Use the explicit reconstruction control above when asserting preservation under the round's new-key/new-entry exception. No source control or historical artifact was edited by this verifier; this report is the only durable write for V03.
