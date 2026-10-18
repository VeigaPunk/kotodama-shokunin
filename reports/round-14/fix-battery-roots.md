# R14-O01 — default battery baseline-root reconciliation

- Date: 2026-10-17.
- Axis: O / operability; preservation and fail-closed behavior are non-regression constraints.
- Disposition: **applied-with-control** for the default-discovery gap, `R9-SWEEP-01` / `O-R9-01`.
- Source: `reports/round-12/defects/sweep-r9.md:5-26`; routing: `reports/round-12/defects/routed.md:26-32`.
- Measured HEAD: `a7bc9e9ff05a57515c5efaaa7e50116eb30938ff` (`git rev-parse HEAD`, 2026-10-17T20:59:44-03:00).
- Changed executable: `tools/check-gate-battery.py`, SHA-256 `7aa898d627fe361517d2942a0fe2b337f15d8cdc1fcb4061b394eee60f03d574` (`sha256sum tools/check-gate-battery.py`, same timestamp).

## Applied change and bounded layout decision

`tools/check-gate-battery.py:115-119` retains both existing default roots and adds the preserved `reports/round-9/baselines` root. Paths remain anchored to the executable's repository, not the caller's working directory. The module's current root description is updated at `tools/check-gate-battery.py:16-20`.

This is a discovery compatibility exception for the existing round-9 layout, permitted by this assignment. It does **not** make the old directories conform to the `<gate>/<round>-<phase>` layout in `corpus/knowledge/verification/gate-frozen-run-standard.md:50-75`. Future baselines still use that standard layout. No baseline bytes, paths, IDs, pins, historical runner, or filed validation receipt were changed by this task. The round-9 registry's two-root description remains a filed historical observation, superseded for the current executable by this record.

The battery still verifies pins only; it does not replay frozen verdicts. A green result below means default selftests, digest checks, and gate coverage passed, not blanket frozen-run-layout conformance or a design/canon verdict.

## Before and after: the actual default command

Both runs used the following command from the lane root, without a baseline-root override:

```sh
export TMPDIR="$PWD/.scratch"
mkdir -p "$TMPDIR"
date -Iseconds
python3 tools/check-gate-battery.py
```

- **Before, 2026-10-17T20:57:35-03:00:** exit 2; selftests `pass=7, fail=0, unevaluable=0`; baseline summary `baselines_found=5, pinned=5`, with myth and naming uncovered and two `BASELINE-GATE-UNCOVERED` findings. This reproduces the routed defect.
- **After, 2026-10-17T20:58:44-03:00:** exit 0; selftests `pass=7, fail=0, unevaluable=0`; baseline summary `baselines_found=8, pinned=8, unevaluable=0`, all **7/7 gates covered**, no uncovered gates and no findings. Discovery found 2 expected-root files, 3 frozen-root files, and 3 round-9-root files. Eight pins are not eight distinct gates: handoff has two baselines, as recorded in `reports/round-9/baselines/registry.md:174`.
- The same default runs measured the live gate scripts/fixture tree as preserved: 28 files before and after, no modified/added/deleted files (`originals` in command stdout).

## Persistent regression control

`CTRL-BASELINE-DEFAULT-ROOTS`, implemented at `tools/check-gate-battery.py:941-958`, creates synthetic baselines under all required relative roots in a disposable repository-shaped tree, then mirrors the executable's real default-root configuration into that tree. Removing a required default root loses a synthetic baseline and fails the control; no live baseline is changed.

At 2026-10-17T20:58:44-03:00:

```sh
export TMPDIR="$PWD/.scratch"
python3 tools/check-gate-battery.py --selftest
```

Exit 0. Stdout ended with `SELFTEST OK 29/29 controls behaved as expected`. Existing snapshot-tamper, gate-revision, unpinned, unknown, malformed, missing-input, external-input, path-escape, uncovered-gate, crash and timeout controls remained green.

At 2026-10-17T20:58:46-03:00 the control was challenged with the original defect, planted **in memory only**:

```sh
export TMPDIR="$PWD/.scratch"
export PYTHONDONTWRITEBYTECODE=1
python3 - <<'PY'
import contextlib, importlib.util, io
spec = importlib.util.spec_from_file_location('battery', 'tools/check-gate-battery.py')
battery = importlib.util.module_from_spec(spec)
spec.loader.exec_module(battery)
battery.BASELINE_ROOTS = tuple(p for p in battery.BASELINE_ROOTS
    if p != battery.HERE.parent / 'reports' / 'round-9' / 'baselines')
stream = io.StringIO()
with contextlib.redirect_stdout(stream):
    code = battery.run_selftest()
print('observed_exit:', code)
print(stream.getvalue())
assert code == 1
assert 'SELFTEST FAIL CTRL-BASELINE-DEFAULT-ROOTS did not discover every required root' in stream.getvalue()
PY
```

The test harness exited 0 after observing the expected selftest exit 1 and the named `CTRL-BASELINE-DEFAULT-ROOTS` failure in captured stdout. The executable on disk was not modified for this challenge.

## Live-CLI negatives

At 2026-10-17T20:59:16-03:00:

```sh
export TMPDIR="$PWD/.scratch"
python3 tools/check-gate-battery.py \
  --baselines-root tools/gates/expected \
  --baselines-root tools/gates/frozen
```

Expected exit 2: 7 selftests passed, 5 baseline pins validated, myth and naming remained uncovered, and both `BASELINE-GATE-UNCOVERED` findings were retained. Explicit overrides still replace defaults; adding the legacy root did not turn uncovered gates into a silent pass.

At 2026-10-17T20:59:15-03:00 this separate real-CLI tamper drill ran:

```sh
export TMPDIR="$PWD/.scratch"
python3 - <<'PY'
import json, pathlib, shutil, subprocess, sys, tempfile
with tempfile.TemporaryDirectory(prefix='r14-o01-legacy-tamper-') as tmp:
    mirror = pathlib.Path(tmp)
    shutil.copytree('tools/gates', mirror / 'tools/gates')
    shutil.copy2('tools/check-gate-battery.py', mirror / 'tools/check-gate-battery.py')
    shutil.copytree('reports/round-9/baselines', mirror / 'reports/round-9/baselines')
    baseline = mirror / 'reports/round-9/baselines/myth-consistency-gate'
    spec = json.loads((baseline / 'expected.json').read_text())
    snapshot = baseline / next(iter(spec['inputs']))
    snapshot.write_bytes(snapshot.read_bytes() + b'\n# R14-O01 planted tamper\n')
    proc = subprocess.run([sys.executable, str(mirror / 'tools/check-gate-battery.py')],
                          cwd=mirror, capture_output=True, text=True)
    report = json.loads(proc.stdout)
    print(proc.returncode, report['baselines']['summary'], report['baselines']['findings'])
    assert proc.returncode == 2
    assert report['summary']['pass'] == 7
    assert len(report['baselines']['summary']['gates_covered']) == 7
    assert any(f['id'] == 'BASELINE-TAMPERED' and f['gate'] == 'myth-consistency-gate.py'
               for f in report['baselines']['findings'])
PY
```

The harness exited 0 after observing the expected battery exit 2: 8 baselines discovered, 7 pinned, 1 `snapshot_tampered`, and the myth `BASELINE-TAMPERED` finding. This tests the newly included root through the default CLI, in a disposable in-lane mirror only.

## Preservation control and scope

Before editing, a per-file SHA-256/path census covered all files under `tools/gates/expected`, `tools/gates/frozen`, and `reports/round-9/baselines`. The after-run census at 2026-10-17T20:58:44-03:00 and final census at 2026-10-17T21:00:07-03:00 matched it exactly: **123/123 existing files**, no changed bytes, additions, or deletions. The canonical JSON manifest digest was `fc011128689349af9f00b0927a9d2474c5cfd5856bc7341f68a714ed862c53c7`.

The final independent committed-file control used the following code (the digest also pins the complete measured tree, including advisory logs):

```sh
export TMPDIR="$PWD/.scratch"
python3 - <<'PY'
import hashlib, json, pathlib, subprocess
roots = ['tools/gates/expected', 'tools/gates/frozen', 'reports/round-9/baselines']
paths = subprocess.check_output(['git', 'ls-files', '--', *roots], text=True).splitlines()
hash_bytes = lambda b: hashlib.sha256(b).hexdigest()
committed = {p: hash_bytes(subprocess.check_output(['git', 'show', 'HEAD:' + p])) for p in paths}
live = {p.as_posix(): hash_bytes(p.read_bytes()) for root in roots
        for p in pathlib.Path(root).rglob('*') if p.is_file()}
extra = sorted(live.keys() - committed.keys())
ignored = subprocess.check_output(['git', 'check-ignore', '--', *extra], text=True).splitlines()
manifest = hash_bytes(json.dumps(live, sort_keys=True, separators=(',', ':')).encode())
print('tracked', len(committed), 'live', len(live), 'ignored_advisory_logs', len(extra), manifest)
assert committed == {p: live[p] for p in paths if p in live}
assert ignored == extra and all(pathlib.Path(p).name == 'run.log' for p in extra)
assert manifest == 'fc011128689349af9f00b0927a9d2474c5cfd5856bc7341f68a714ed862c53c7'
PY
```

Result: 114/114 tracked files match HEAD; the other 9 files are pre-existing ignored `run.log` advisory files and are included in the unchanged full-tree census. A first auxiliary HEAD census at 20:59:44 incorrectly required these ignored logs to be tracked and failed that assertion; the corrected tracked-subset/full-tree checks above passed. No baseline was altered to satisfy the control.

The scoped `git diff --exit-code -- tools/gates/expected tools/gates/frozen reports/round-9/baselines reports/round-8/validation.json reports/round-9/validation.json reports/round-10/validation.json reports/round-11/validation.json reports/round-12/validation.json` exited 0 at 2026-10-17T21:00:07-03:00. No historical validator was invoked.

A broader read-only historical-report diff also saw the concurrent R14-O03 errata addition to `reports/round-10/findings-tracker.json`; this task did not write or revert that path and does not assert that other workers' artifacts are unchanged. Only the battery's source and this assigned evidence fragment are deliverable changes from R14-O01. Overall round-14 craft/D2/D3 regressions and integration bookkeeping remain the parent/regression workers' responsibility.
