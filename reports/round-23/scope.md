# Round 23 — Scope watch (SCRIBE X02)

- **Axes:** filed-artifact immutability; fleet-root cleanliness; reproducible, bounded evidence.
- **Assignment:** filed rounds 8–22 untouched; fleet root clean.
- **Date:** 2026-10-18; timestamps below are UTC, except the three Git/commit-time events which carry the lane's local −03:00 form in parentheses.
- **Write scope:** only this evidence fragment. No shared bookkeeping, source fixes, historical validators, Git mutations, commit, push, sibling writes, or scratch files.

## Verdict and revision binding

**PASS for the round-23 window at the recorded observations, with one disclosed inherited deviation.** At the initial 15:04:17Z replay and the three closing watch samples (15:05:03Z, 15:06:03Z, 15:07:03Z), all **1,094 tracked filed paths** under `reports/round-{8..22}` matched the declared baseline in Git blob identity and executable/symlink mode **except one**: `reports/round-22/fixes/regression.md`, an uncommitted working-tree edit that predates round-23 dispatch and never changed during this watch. No round-23 seat write to a filed rounds 8–22 path was observed; `baseline_to_HEAD` diff over the protected surface is empty; fleet-root status is empty. This is a scoped observation, not round acceptance and not a claim that no transient write ever occurred.

The declared baseline (`reports/round-23/claims.json:5`) is `0e81d9d99514631d6717e1ff354d5a5a759aa980` (the round-22 close, 11:59:16−03:00); observed lane HEAD is `7b181a52eb74319e5e5c40cdb1f0a1a1dc652079` (round-23 declaration, 12:00:40−03:00); `git merge-base --is-ancestor` returned success. `git show --stat HEAD` shows the declaration commit adds only `reports/round-23/claims.json` and `reports/round-23/targets.json`, so no filed rounds 8–22 path changed at commit level between baseline and HEAD.

Fleet HEAD was `3335751b161cedbde7903f06d7bb62c2a546a191` ("close kotodama round-22: REJECTED on D"); `git -C /home/vgpnk/Projects/shokunin status --porcelain=v1 --untracked-files=all` returned empty at 15:04:17Z and at every watch sample. The fleet's `.gitignore:1:*-shokunin/` ignores this lane (`git check-ignore -v kotodama-shokunin`). Fleet cleanliness does not establish sibling-repository cleanliness or byte identity for ignored fleet files.

## The one deviation — timing adjudication, not disposition

`reports/round-22/fixes/regression.md` differs from its filed blob (`fb73108`) in the working tree: an uncommitted rewrite of the round-22 O12 regression report from an `IN PROGRESS` stub to a completed closing-snapshot verdict (16,646 bytes, mode 0644). Observed facts, all from commands on 2026-10-18:

- Worktree mtime **11:59:32−03:00** (14:59:32Z): **16 seconds after** the round-22 close commit (11:59:16−03:00) and **68 seconds before** the round-23 declaration commit (12:00:40−03:00), i.e. inside the round-22 → round-23 handoff gap, before any round-23 seat was dispatched.
- `git diff --name-status 0e81d9d..HEAD -- reports/round-{8..22}` is empty (15:04:17Z): the edit was **never committed**, and no post-close commit touched any protected path.
- `Path.lstat()` metadata (mtime_ns `1792335572822711470`, size `16646`, mode `420`) was identical at all three watch samples: **no further write during the round-23 window**.

Adjudication: the edit is a **round-22 straggler** (a seat's final write that missed the close commit), not a round-23 violation — no round-23 seat could have authored a file whose last modification predates dispatch. Content certification is explicitly **not** this seat's: I neither verified the completed O12 verdict's claims nor ran its commands. Disposition — commit as a late round-22 fragment or restore the filed bytes — belongs to the parent integrator; this seat left the file byte-identical to how it was found.

## Protected-surface evidence

All commands in this section were run on **2026-10-18**, with `export TMPDIR="$PWD/.scratch"` before the command batch; no scratch files were written.

- `git ls-tree -r 0e81d9d99514631d6717e1ff354d5a5a759aa980 -- reports/round-{8..22}` inventories **1,094** tracked filed paths. The direct working-file Git-blob/mode comparison returned **1,093 matched, 1 mismatch** (the straggler above) at 15:04:17Z. The sorted `path + NUL + sha256(bytes) + LF` manifest digest of the **observed** bytes was `592c1bf6c9d5dc8429a10226f1de72bec045e5b4af8fb13c8c99fac1a1138c08` — a watch-digest that includes the straggler's current bytes, so it is a stability anchor, not an identity claim for that one path.
- `git status --porcelain=v1 --untracked-files=all` over the whole lane returned exactly one row, ` M reports/round-22/fixes/regression.md` (15:04:17Z): no other tracked-path modification and no untracked non-ignored file exists anywhere in the lane.
- `git ls-files --others --ignored --exclude-standard -- reports/round-{8..22}` returned **eight** ignored paths at 15:04:17Z: `reports/round-9/baselines/{handoff-packet-check,myth-consistency-gate,naming-collision-gate}/run.log`, `reports/round-11/handoff/{run.log,tamper-control.log}`, `reports/round-20/handoff/run.log`, `reports/round-22/handoff/declared-in/run.log`, `reports/round-22/handoff/declared-in-r2/run.log`. They have no committed baseline; their SHA-256 digests were recorded and held constant across all watch samples (`reports/round-9/baselines/myth-consistency-gate/run.log` is the empty-file digest `e3b0c442…b855`).
- Detector control at 15:04:41Z: `git rev-parse <baseline>:reports/round-21/claims.json` matched the Git blob SHA-1 of the live bytes; appending `b'\nx02-in-memory-only-probe\n'` **in memory only** produced a mismatch; the probe file re-read unchanged. All three assertions passed; no control file was created or altered. This controls the audit detector, not any round's product fixes.

## Closing watch

The read-only `python3 -` watch repeated the blob/mode comparison, protected status/diff, ignored-file digests, straggler `lstat` metadata, and fleet-root status in `range(1, 4)` with `time.sleep(60)` between samples. Command run **2026-10-18**, exit **0**; observations at **15:05:03.036140Z**, **15:06:03.060450Z**, and **15:07:03.084937Z**.

At each sample: mismatches exactly `[reports/round-22/fixes/regression.md]`; protected status exactly ` M reports/round-22/fixes/regression.md`; `baseline_to_head_diff` empty; eight ignored digests unchanged; straggler metadata unchanged; fleet status empty; fleet HEAD and lane HEAD unchanged. `WATCH_CONSISTENT=True`. These are point-in-time observations; metadata stability is relative to the watch's first sample, not a Git historical-mtime claim.

Other workers' live writes were visible after the watch: new round-23 report fragments under `reports/round-23/integration/` (`fragment-ledger.json`, `fragment-ledger.md`, `ledger-gen.py`) at the 15:08:40Z status check. None of those paths is in the protected filed-round surface; this scope seat neither edited nor certified their content. The final verdict binds the observations here, not later parent integration.

## Read-only replay

From the lane root, run the following command. It inventories baseline paths independently of the index, checks actual file bytes and modes, reports ignored paths without giving them baseline identity, checks the fleet root, and asserts the protected surface matches the recorded verdict including the single disclosed straggler. It writes no receipts and executes no historical validator.

```bash
export TMPDIR="$PWD/.scratch"
python3 - <<'PY'
from pathlib import Path
import datetime, hashlib, json, stat, subprocess
baseline = '0e81d9d99514631d6717e1ff354d5a5a759aa980'
paths = [f'reports/round-{n}' for n in range(8, 23)]
KNOWN = 'reports/round-22/fixes/regression.md'
def git(*args):
    return subprocess.check_output(['git', *args])
rows = [r for r in git('ls-tree', '-r', '-z', baseline, '--', *paths).split(b'\0') if r]
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
result = {
    'observed_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'tracked_paths': len(rows), 'mismatches': mismatches,
    'baseline_to_head_diff': git('diff', '--name-status', baseline, 'HEAD', '--', *paths).decode(),
    'protected_status': git('status', '--porcelain=v1', '--untracked-files=all', '--', *paths).decode(),
    'fleet_status': git('-C', '/home/vgpnk/Projects/shokunin', 'status', '--porcelain=v1', '--untracked-files=all').decode().splitlines(),
}
print(json.dumps(result, indent=2))
assert result['mismatches'] == [KNOWN]
assert not result['baseline_to_head_diff'] and not result['fleet_status']
assert result['protected_status'] == f' M {KNOWN}\n'
PY
```

## Limits and handoff

Repeated observations cannot prove there was no write-and-restore between samples, and the straggler's mtime proves only the last write, not its author — the timing adjudication above is inference from commit timestamps and dispatch order, recorded so the parent can confirm or override it. Ignored files have no Git baseline; observed stability cannot establish their historical identity. The earlier transient round-9 receipt rewrite/restoration remains disclosed in `reports/round-20/scope.md:83` and is not erased by a clean present comparison. No validator was executed here, including historical validators that could rewrite filed receipts. The straggler's disposition and the final post-integration scope check remain the parent integrator's responsibility.
