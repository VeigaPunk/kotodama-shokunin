# R14-O06 — index-updater classification correction

- Axis: O / operability; calibration constraint: preserve historical measurements.
- Finding: `R10-IXCLS` (`reports/round-12/defects/ledger.json:105-109`), also `R10-SWEEP F-02` (`reports/round-12/defects/sweep-r10.md:15-21`).
- Disposition: **resolved-by-documentation with control**. The corrected role map and independently executable regression are below. This is not a claim that the filed runner was patched.
- Scope: only this new round-14 record is written. The round-10 runner, receipt, and updater fragments remain filed and unchanged by this assignment. No historical round validator is invoked.

## Evidence and corrected interpretation

`reports/round-10/targets.json:7-20` assigns separate author, reviewer, index-updater, and partition-auditor seats. `reports/round-10/coverage/index-update-22.md:224-244` explicitly identifies its backup-updater role and the classification defect. Its statement at lines 235-237 is a historical observation, not this worker's count.

The defect is the residual authorship bucket in `reports/round-10/run-validation.py:493-498`: it excludes `review-*`, `audit-*`, and only the exact `index-update.md`. Consequently `index-update-22.md` is counted as authorship. The filed receipt's `claims.C.measurement.fragments.authorship` must remain the historical value, not be silently corrected in `validation.json`.

The read-only control below computes the actual inventory, extracts and evaluates **only that legacy list-comprehension expression** from the runner's syntax tree, and compares it with this corrected map:

- `C[0-9]{2}.md` → author.
- `review-*` → reviewer; `audit-*` → auditor, preserving those existing role conventions.
- `index-update.md` or `index-update-<numeric seat>.md` → index updater, never author.
- Everything else → unclassified, never implicit author credit. A successor harness must report/reject unclassified fragments rather than turn them into authors by exclusion.

The canonical `index-update.md` presence and command/count checks at runner lines 499-506 are a separate requirement; recognizing a backup updater does **not** waive that requirement. The authorship minimum remains the runner's `C_MIN_ENTRIES` at line 80. This correction does not re-evaluate other coverage conditions or the historical C/F/O admission.

## Why no runner patch is permitted here

The only matching coverage-classification implementation is the filed round-10 runner. Inspection command (2026-10-17): search `reports/round-*/run-validation.py` for `authorship`, `coverage_dir`, and `index-update`; all matching locations are in `reports/round-10/run-validation.py`. `reports/round-12/run-validation.py` measures recount calibration, defect dispositions/regressions, and adjacency, not author roles. No round-14 runner existed at the inspection snapshot.

Under this assignment's explicit filed-round exception, the correction is recorded here instead of changing round 10, round 12, or another worker's harness. Future coverage runners can adopt the allowlisted `role()`/`authors()` implementation below and its missing-author regression. Integrators should point `R10-IXCLS` to this record using `resolved-by-documentation`, not `applied-with-control` or a claim that round 10 now rejects the planted case.

## Read-only before/after control

Command: from the lane root, execute the following shell block. It sets the required in-lane `TMPDIR`, creates no scratch files, does not import/execute the runner, and never writes a receipt. Its date is printed with every execution. Assertions exercise both real filenames and planted in-memory filenames; all tracked files under rounds 8-12 are hashed before/after, and the specific round-10 runner/receipt/backup-updater bytes are also checked against HEAD.

```sh
export TMPDIR=$PWD/.scratch
export PYTHONDONTWRITEBYTECODE=1
python3 - <<'PY'
import ast
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess

root = Path.cwd()
filed_roots = [f'reports/round-{n}' for n in range(8, 13)]
paths = subprocess.check_output(
    ['git', 'ls-files', '-z', '--', *filed_roots]).decode().split('\0')
paths = [p for p in paths if p]
def hashes():
    return {p: hashlib.sha256((root / p).read_bytes()).hexdigest()
            for p in paths}
before = hashes()
runner = 'reports/round-10/run-validation.py'
receipt_path = 'reports/round-10/validation.json'
backup = 'reports/round-10/coverage/index-update-22.md'
tree = ast.parse((root / runner).read_text())
measure_c = next(n for n in tree.body
                 if isinstance(n, ast.FunctionDef) and n.name == 'measure_c')
assignment = next(n for n in ast.walk(measure_c)
                  if isinstance(n, ast.Assign) and any(
                      isinstance(t, ast.Name) and t.id == 'authorship'
                      for t in n.targets))
legacy_code = compile(ast.Expression(assignment.value), runner, 'eval')
minimum = next(ast.literal_eval(n.value) for n in tree.body
               if isinstance(n, ast.Assign) and any(
                   isinstance(t, ast.Name) and t.id == 'C_MIN_ENTRIES'
                   for t in n.targets))
def legacy(names):
    return eval(legacy_code, {'__builtins__': {}, 'fragments': names})
def role(name):
    if re.fullmatch(r'index-update(?:-[0-9]+)?\.md', name):
        return 'index_updater'
    if re.fullmatch(r'C[0-9]{2}\.md', name):
        return 'author'
    if name.startswith('review-'):
        return 'reviewer'
    if name.startswith('audit-'):
        return 'auditor'
    return 'unclassified'
def authors(names):
    return [name for name in names if role(name) == 'author']
fragments = sorted(p.name for p in
                   (root / 'reports/round-10/coverage').glob('*.md'))
receipt = json.loads((root / receipt_path).read_text())
controls = []
def check(name, condition):
    if not condition:
        raise AssertionError(name)
    controls.append(name)
check('real inventory: disjoint assigned roles',
      Counter(map(role, fragments)) == {
          'author': 10, 'reviewer': 10, 'auditor': 4, 'index_updater': 2})
check('filed receipt and legacy expression reproduce inflated count',
      receipt['claims']['C']['measurement']['fragments']['authorship']
      == len(legacy(fragments)) == 11)
check('corrected real authorship still meets unchanged minimum',
      len(authors(fragments)) == minimum == 10)
check('both index updaters classified separately',
      role('index-update.md') == role('index-update-22.md') == 'index_updater')
extra = fragments + ['index-update-23.md', 'index-update-99.md',
                     'index-update-100.md']
check('additional updater fragments cannot inflate authorship',
      len(legacy(extra)) == 14 and len(authors(extra)) == 10)
missing_author = [name for name in fragments if name != 'C10.md']
check('missing-author negative: legacy false pass rejected',
      len(legacy(missing_author)) == 10
      and len(authors(missing_author)) == 9 < minimum)
check('updater-only negative: no author credit',
      not authors(['index-update.md', 'index-update-22.md',
                   'index-update-100.md']))
check('unknown-support negative: unclassified, never author',
      role('operator-notes.md') == role('index-update-backup.md')
      == 'unclassified'
      and len(authors(fragments + ['operator-notes.md',
                                  'index-update-backup.md'])) == 10)
check('specific filed inputs still match HEAD', all(
    (root / path).read_bytes() == subprocess.check_output(
        ['git', 'show', f'HEAD:{path}'])
    for path in (runner, receipt_path, backup)))
check('read-only control: tracked filed bytes preserved', hashes() == before)
print('observed_utc:', datetime.now(timezone.utc).isoformat(timespec='seconds'))
print('head:', subprocess.check_output(
    ['git', 'rev-parse', 'HEAD'], text=True).strip())
print('filed_measurement:', json.dumps(
    receipt['claims']['C']['measurement']['fragments'], sort_keys=True))
print('corrected_roles:', json.dumps(
    dict(sorted(Counter(map(role, fragments)).items())), sort_keys=True))
print('false_pass_control: legacy=10 corrected=9 minimum=' + str(minimum))
for name in controls:
    print('PASS:', name)
for path in (runner, receipt_path, backup):
    print('sha256:', before[path], path)
print('result: PASS')
PY
```

## Observed results and limits

Executed directly from this record's shell block at **2026-10-17T23:58:54+00:00**, HEAD `a7bc9e9ff05a57515c5efaaa7e50116eb30938ff`: **exit 0; all ten assertions PASS**. All counts below are the output of that dated command, not a regenerated round-10 receipt.

- Filed measurement reproduced: authorship **11**, review **10**, audit **4**, `index_update: true`.
- Corrected real inventory: **10 authors, 10 reviewers, 4 auditors, 2 index updaters**, with no unclassified fragment. The declared authorship minimum is still **10**, so this measurement correction alone does not reverse the historical coverage threshold.
- Extra-updater control: the legacy count grows to **14**, but corrected authorship stays **10**.
- Missing-author negative: remove `C10.md` only in memory; the legacy expression falsely counts **10**, while the corrected map counts **9** and fails the unchanged minimum of **10**.
- Updater-only and unknown-support controls grant no author credit. All tracked filed bytes are unchanged across execution; the runner, receipt, and backup updater also match HEAD.

Replay the exact embedded shell block without creating a script or receipt:

```sh
export TMPDIR=$PWD/.scratch
export PYTHONDONTWRITEBYTECODE=1
python3 - <<'PY'
from pathlib import Path
import subprocess
import sys
report = Path('reports/round-14/fix-index-classification.md').read_text()
block = report.split('```sh\n', 1)[1].split('\n```', 1)[0]
sys.exit(subprocess.run(['bash'], input=block, text=True).returncode)
PY
```

SHA-256 pins from the same dated execution:

- `reports/round-10/run-validation.py`: `23d6dc09002fe18c46778ac57d2c34246ab970a9371e7382950ca737d4019b0e`.
- `reports/round-10/validation.json`: `e8571db918b2c3237256342bd95f241be5661a96019e460990c7d1fe2fc32f94`.
- `reports/round-10/coverage/index-update-22.md`: `2c33853f117be0d3296427fb383d7ded71ed74cf2cbd6fbd99d14c71e2c22d83`.

An initial exploratory version additionally asserted that every filed round-8–12 path matched HEAD. That broad assertion failed; follow-up inspection at 2026-10-17T23:58:13Z showed a concurrent `R14-O03` erratum key in `reports/round-10/findings-tracker.json` (`git diff --name-status HEAD -- reports/round-{8,9,10,11,12}`; follow-up `git diff -- reports/round-10/findings-tracker.json`). That tracker is outside this assignment; this worker neither wrote nor reverted it. The final control checks the relevant inputs against HEAD and preserves all observed tracked filed bytes across its run instead of falsely requiring the parallel wave's whole historical tree to be clean.

This is a filename-role regression and correction record only. The round-10 receipt remains historical; the filed defective runner is intentionally not rerun or fixed. Battery/craft/D2/D3 regressions and the round-14 acceptance runner belong to the assigned integration/regression seats; no result from those seats is claimed here.
