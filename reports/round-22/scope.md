# Round 22 — Scope watch (SCRIBE X02)

- **Axes:** filed-artifact immutability; fleet-root cleanliness; reproducible, bounded evidence.
- **Assignment:** filed rounds 8–21 untouched; fleet root clean.
- **Date:** 2026-10-18; timestamps below are UTC command observations.
- **Write scope:** only this evidence fragment. No shared bookkeeping, source fixes, historical validators, Git mutations, commit, push, sibling writes, or scratch files.

## Verdict and revision binding

**PASS at the recorded observations.** At the initial 14:40:17Z reading and the closing 14:42:41Z watch sample, all **1,018 tracked filed paths** under `reports/round-{8..21}` matched the declared baseline in both Git blob identity and executable/symlink mode. Baseline-to-HEAD and baseline-to-worktree diffs, protected-surface status, and fleet-root status were empty. This is a scoped observation, not a final admission or a claim that no transient write ever occurred.

The declared baseline (`reports/round-22/claims.json:5`) is `46a03257ee75dd8f685a105e47da3f45a0154172`; observed lane HEAD is `cd9c8e4cb62896a8b5d0d642cd04966d41dd4d13`. `git merge-base --is-ancestor` returned success. `git diff --name-status <baseline> HEAD` showed only the new round-22 declaration files, `reports/round-22/claims.json` and `reports/round-22/targets.json` (commands run 14:40:17Z).

Fleet HEAD was `cc421397ba830574488e1e9221147bbec5f9e43e`; `git -C /home/vgpnk/Projects/shokunin status --porcelain=v1 --untracked-files=all` returned empty at 14:39:45Z and 14:40:17Z and at every watch sample below. The fleet's `.gitignore:1:*-shokunin/` ignores this independent lane (`git check-ignore -v kotodama-shokunin`, 14:40:17Z). Fleet cleanliness does not establish sibling-repository cleanliness or byte identity for ignored fleet files.

## Protected-surface evidence

All commands in this section were run on **2026-10-18**, with `export TMPDIR="$PWD/.scratch"` before the command batch; no scratch files were written.

- `git ls-files reports/round-{8..21} | wc -l` returned **1,018** at 14:40:41Z. The baseline `git ls-tree -r -z` inventory and direct working-file Git-blob/mode comparison returned **1,018 matched, zero mismatches** at 14:40:17Z. The tracked SHA-256 manifest digest was `8eaa73b290eb0b85240b79d91d8f2cb5d41b77d2e009003be0072e699a896ff4` (replay below).
- `git diff --name-status 46a03257ee75dd8f685a105e47da3f45a0154172 HEAD -- reports/round-{8..21}` and the same command without `HEAD` returned empty at 14:40:17Z. `git status --porcelain=v1 --untracked-files=all -- reports/round-{8..21}` also returned empty.
- `git ls-files --others --ignored --exclude-standard reports/round-{8..21}` returned **six ignored paths** at 14:40:41Z: `reports/round-11/handoff/{run.log,tamper-control.log}`, `reports/round-20/handoff/run.log`, and `reports/round-9/baselines/{handoff-packet-check,myth-consistency-gate,naming-collision-gate}/run.log`. They have no committed baseline and are excluded from the baseline-identity claim.
- Detector control at 14:40:41Z: `git rev-parse <baseline>:reports/round-21/claims.json` matched the Git blob SHA-1 of the live bytes. Appending `b'\nx02-in-memory-only-probe\n'` **in memory only** caused a mismatch. Both assertions passed; no control file was created or altered. This controls the audit detector, not the round's product fixes.

## Closing watch

The read-only `python3 -` watch repeated the replay's blob/mode/manifest comparison in `range(1, 4)`, with `time.sleep(60)` between samples; it also compared `Path.lstat()`'s `st_mtime_ns`, size, and full mode against its first observation, SHA-256 of the ignored files against the watch's initial bytes, protected Git diff/status, and fleet-root Git status. Command run **2026-10-18**, exit **0**; observations were **14:40:41.097923Z**, **14:41:41.129571Z**, and **14:42:41.161888Z**.

At each sample: **1,018 baseline matches; zero mismatches; zero observed metadata changes; zero protected status/diff rows; six ignored paths with zero observed byte changes; zero fleet-root status rows**. Every sample reproduced the manifest digest above and the same fleet HEAD. These are point-in-time observations; metadata stability is relative to the watch's initial observation, not a Git historical-mtime claim.

Other workers' live changes were visible in `tools/d2-typed-labels.py`, `tools/exercise-handoff-e2e.py`, new `corpus/lessons/round-22.md`, and new round-22 report fragments. None of those paths is in the protected filed-round surface; this scope seat neither edited nor certified their content. The final verdict binds the observations here, not later parent integration.

The exact embedded replay below was executed directly from this report at 14:41:19Z and 14:41:30Z, both exit **0**. Report whitespace checks passed at 14:41:30Z. The verification wrapper initially treated `git diff --no-index --check /dev/null reports/round-22/scope.md`'s normal added-file exit **1** as a failure; the corrected check accepts that status only with empty diagnostics and independently rejects trailing whitespace. No product or filed artifact was changed for that correction.

## Read-only replay

From the lane root, run the following command. It inventories baseline paths independently of the index, checks actual file bytes and modes, reports ignored paths without giving them baseline identity, and checks the fleet root. Manifest framing is sorted `path + NUL + sha256(file bytes) + LF`. This command writes no receipts and executes no historical validator.

```bash
export TMPDIR="$PWD/.scratch"
python3 - <<'PY'
from pathlib import Path
import datetime, hashlib, json, stat, subprocess
baseline = '46a03257ee75dd8f685a105e47da3f45a0154172'
paths = [f'reports/round-{n}' for n in range(8, 22)]
def git(*args):
    return subprocess.check_output(['git', *args])
rows = [r for r in git('ls-tree', '-r', '-z', baseline, '--', *paths).split(b'\0') if r]
manifest = hashlib.sha256()
mismatches = []
for row in sorted(rows, key=lambda r: r.split(b'\t', 1)[1]):
    metadata, name = row.split(b'\t', 1)
    mode, kind, expected = metadata.decode().split()
    source = Path(name.decode())
    try:
        info = source.lstat()
        data = source.readlink().as_posix().encode() if stat.S_ISLNK(info.st_mode) else source.read_bytes()
    except FileNotFoundError:
        mismatches.append({'path': name.decode(), 'reason': 'missing'})
        continue
    actual = hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()
    actual_mode = '120000' if stat.S_ISLNK(info.st_mode) else ('100755' if info.st_mode & 0o111 else '100644')
    if (mode, expected) != (actual_mode, actual):
        mismatches.append(name.decode())
    manifest.update(name + b'\0' + hashlib.sha256(data).hexdigest().encode() + b'\n')
result = {
    'observed_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'tracked_paths': len(rows), 'mismatches': mismatches,
    'tracked_manifest_sha256': manifest.hexdigest(),
    'baseline_to_head_diff': git('diff', '--name-status', baseline, 'HEAD', '--', *paths).decode(),
    'baseline_to_worktree_diff': git('diff', '--name-status', baseline, '--', *paths).decode(),
    'protected_status': git('status', '--porcelain=v1', '--untracked-files=all', '--', *paths).decode(),
    'ignored_paths': git('ls-files', '--others', '--ignored', '--exclude-standard', '--', *paths).decode().splitlines(),
    'fleet_status': git('-C', '/home/vgpnk/Projects/shokunin', 'status', '--porcelain=v1', '--untracked-files=all').decode(),
}
print(json.dumps(result, indent=2))
assert not any(result[key] for key in ('mismatches', 'baseline_to_head_diff', 'baseline_to_worktree_diff', 'protected_status', 'fleet_status'))
PY
```

## Limits and handoff

Repeated observations cannot prove there was no write-and-restore between samples. Ignored files have no Git baseline; observed stability during this watch cannot establish their historical identity. The earlier transient round-9 receipt rewrite/restoration remains disclosed in `reports/round-20/scope.md:83` and is not erased by a clean present comparison. No validator was executed here, including historical validators that could rewrite filed receipts. Product-gate acceptance and the final post-integration scope check remain the parent integrator's responsibility.
