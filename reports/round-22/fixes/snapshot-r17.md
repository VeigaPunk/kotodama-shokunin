# R22-O10 — R17 clone-snapshot disposition

- Axis: O / operability; disposition date: 2026-10-18.
- Status: **resolved-by-documentation, reproduced environmental scanner defect**. This resolves the clone-snapshot mechanism question; it does not claim a source repair to the frozen R17 runner or a new R17 acceptance result.
- Routed records: `reports/round-21/recount/dispositions.md` items 1 and 8; `reports/round-21/defects/routed.md` → `R17-CURRENT-RECOUNT-DISCREPANCY`; compare the later scanner explanation already recorded in `reports/round-21/rerun.json:93-101`.
- Measured revision: `cd9c8e4cb62896a8b5d0d642cd04966d41dd4d13`; declared R22 baseline: `46a03257ee75dd8f685a105e47da3f45a0154172`.
- Fresh, local, no-hardlinks clone: `.scratch/r22-o10-snapshot.iTM6Nv/clone`, created at `2026-10-18T14:40:24Z`. Every scratch write remained inside this lane. No full historical round validator was run, and no historical receipt was rewritten.

## New disposition row

| Row | Earlier statement | R22 ruling | Control and date |
|---|---|---|---|
| R22-O10-SNAPSHOT-1 | R21 dispositions called the mechanism unproven and suggested an incomplete snapshot despite matching files. | A complete clone below `.scratch` is sufficient to produce the zero: the runner tests absolute ancestor components, not paths relative to its own repository. This is an environment-sensitive enumeration bug, not evidence that the filed fragments are absent. | Fresh-clone scanner and counterfactual-root controls below; `2026-10-18T14:40:46Z`. |

This row supersedes the *unproven-mechanism disposition*, not the archived R17/R21 measurements. It does not reconstruct the transient contents of the original R21 clone; that historical snapshot is not needed to demonstrate the sufficient mechanism.

## Mechanism and measurements

`reports/round-17/run-validation.py:326-341` constructs `base = ROOT / prefix`, iterates `base.rglob("*")`, and drops a candidate when `".scratch" in path.parts`. `ROOT` is absolute (`:63`). In the mandated disposable-clone location, every otherwise valid evidence path has the lane's `.scratch` ancestor, so every file is dropped before `scan_files()` (`:344-346`) or claim C can read it. The same helper has other consumers; the control below is limited to the C census, not a full-run correctness claim.

The following observations all come from the reproduction script below on **2026-10-18 at 14:40:46Z**:

- Git inventory, files present, files matching `git show HEAD:<path>`, and files matching the live source checkout: **16 / 16 / 16 / 16**. The clone is complete for this evidence surface.
- Absolute evidence candidates: **16**; candidates containing `.scratch` in their absolute `Path.parts`: **16**.
- Unmodified `worktree_files("reports/round-17/civ")` and `scan_files(...)`: **0 / 0**. Unmodified `measure_c(...)`: **0 fragments, 0 fixed, 0 attempted, 12 missing targets**, C false.
- Positive control: temporarily rebase **only the enumeration helper's root** to `Path(".")`, preserving its original code, clone cwd, bytes, parsing, attribution and classification logic. Enumeration and scanning return **16 / 16**; `measure_c(...)` returns **16 fragments, 7 fixed, 5 attempted, 0 missing targets**, C true with no failures.
- Negative control: the original absolute-root scan remains **0** after restoration. The control did not mutate the module on disk or manufacture evidence.
- Before/after hashes of **1,030** tracked paths under reports rounds 8–21 and the original round-18 frozen tree: **0 changed** in the clone.

Runner SHA-256: `6b98abadef9951be7cfce006f339dad036f7b341cee6713ecc00be6e5f9095ec`. On 2026-10-18 at 14:41:01Z, `git diff --exit-code 8115eaaeb57c9dce157fe291337cb52dd914c6cf HEAD -- reports/round-17/run-validation.py reports/round-17/civ` exited 0: the R21 recount's measured revision and this clone contain identical scanner/evidence bytes.

## Reproduction command

Run from the lane root. `mktemp` creates a new directory rather than reusing any earlier clone. The Python portion imports the historical runner as a module inside the isolated clone; it never calls `main()` or `validate()`, so no receipt refresh or replay subprocess can escape this bounded experiment.

```sh
export TMPDIR=$PWD/.scratch
export PYTHONDONTWRITEBYTECODE=1
mkdir -p "$TMPDIR"
W=$(mktemp -d "$TMPDIR/r22-o10-snapshot.XXXXXX")
git clone --quiet --no-hardlinks --no-checkout . "$W/clone"
git -C "$W/clone" -c advice.detachedHead=false checkout --quiet cd9c8e4cb62896a8b5d0d642cd04966d41dd4d13
(
  cd "$W/clone"
  export TMPDIR=$PWD/.scratch
  mkdir -p "$TMPDIR"
  python3 -B - <<'PY'
import datetime, hashlib, importlib.util, json, subprocess
from pathlib import Path
root = Path.cwd()
lane = root.parents[2]
sha = lambda data: hashlib.sha256(data).hexdigest()
git = lambda *args: subprocess.check_output(['git', *args], cwd=root)
paths = git('ls-files', '-z', '--', 'reports/round-17/civ').decode().split('\0')[:-1]
protected = git('ls-files', '-z', '--', *[f'reports/round-{n}' for n in range(8, 22)],
                'tools/gates/frozen/round-18').decode().split('\0')[:-1]
before = {p: sha((root/p).read_bytes()) for p in protected}
spec = importlib.util.spec_from_file_location('r17_scanner', root/'reports/round-17/run-validation.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
claims = json.loads((root/'reports/round-17/claims.json').read_text())
original = m.worktree_files
original_c = m.measure_c(m.Evidence(), claims)
def relative_scanner(prefix):
    saved = m.ROOT
    m.ROOT = Path('.')
    try:
        return original(prefix)
    finally:
        m.ROOT = saved
m.worktree_files = relative_scanner
control_files = m.worktree_files(m.CIV_EVIDENCE_DIR)
control_scan = m.scan_files(m.CIV_EVIDENCE_DIR)
control_c = m.measure_c(m.Evidence(), claims)
m.worktree_files = original
summary = lambda c: {
    'passed': c['passed'], 'fragments': c['measurement']['fragments']['value'],
    'fixed': c['measurement']['fixed_count']['value'],
    'attempted': c['measurement']['attempted_count']['value'],
    'missing_targets': sum(row['disposition']=='missing' for row in c['measurement']['rows']),
    'failures': c['failures']}
result = {
    'date': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'tracked': len(paths), 'present': sum((root/p).is_file() for p in paths),
    'hash_match_git': sum(sha(git('show','HEAD:'+p))==sha((root/p).read_bytes()) for p in paths),
    'hash_match_source': sum(sha((lane/p).read_bytes())==sha((root/p).read_bytes()) for p in paths),
    'original_worktree_files': original(m.CIV_EVIDENCE_DIR),
    'original_scan_files': m.scan_files(m.CIV_EVIDENCE_DIR),
    'original': summary(original_c), 'relative_root': summary(control_c),
    'relative_root_files': len(control_files), 'relative_root_scan': len(control_scan),
    'protected_paths': len(protected),
    'protected_changed': [p for p in protected if before[p]!=sha((root/p).read_bytes())]}
print(json.dumps(result, indent=2))
assert result['tracked']==result['present']==result['hash_match_git']==result['hash_match_source']==16
assert result['original']['fragments']==0 and result['original']['missing_targets']==12
assert result['relative_root']['fragments']==16 and result['relative_root']['fixed']==7
assert result['relative_root']['attempted']==5 and control_c['passed']
assert result['original_worktree_files']==result['original_scan_files']==[]
assert result['protected_changed']==[]
PY
)
```

The executed capture is retained only as scratch output at `.scratch/r22-o10-snapshot.iTM6Nv/clone/.scratch/scanner.json`; the command and observations above are the filed evidence and do not require that ignored directory to survive.

Deliverable control: on 2026-10-18 at 14:42:02Z, a Python reader extracted this note's literal fenced shell command and ran it with `subprocess.run(['bash', '-e', '-c', script])` from the lane root. It created another fresh clone, exited 0, reproduced the original/control counts above, and reported `protected_paths 1030`, `protected_changed []`. At 14:43:23Z, `git diff --name-only HEAD -- reports/round-{8..21} tools/gates/frozen/round-18` returned no paths; `sha256sum` still returned runner `6b98abade…`, R17 receipt `3fa183feb…`, original R18 manifest `3688e8bc…` and freeze receipt `fb703c9f…`.

## Historical and ownership boundaries

- R17's filed receipt remains **C/O pass, D rejected, acceptance false**. The counterfactual C control is not a re-admission, source-freshness verdict, or clearance.
- The D4 adapter, D2 expected-holds re-pin and replay changes have separate dispositions; the scanner control does not silently settle them.
- No R17 runner fix is assigned here. Any future authorized runner must filter ignored descendants using paths relative to the intended scan root and carry both ordinary-root and `.scratch`-ancestor controls. Editing the filed runner in place is not this disposition.
- The parent owns integration into `routed-resolution.json`, LOG and retrospective. Suggested route status: `resolved-by-documentation`, evidence `reports/round-22/fixes/snapshot-r17.md`, mechanism `absolute-ancestor .scratch filter`, historical receipt preserved.
