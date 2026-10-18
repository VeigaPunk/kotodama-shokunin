# Round 29 — Scope watch (SCRIBE X02)

- **Axes:** immutability of filed rounds 8–28 and their frozen gate generations; kotodama lane working-tree scope; bounded, reproducible evidence.
- **Assignment:** SCRIBE X02 — scope watch.
- **Date:** 2026-10-18. Sample timestamps below are UTC.
- **Write scope:** this fragment only. This seat did not run a round validator, edit source or protected artifacts, mutate Git state, commit, or push. Commands set `TMPDIR="$PWD/.scratch"`; this seat created no scratch files.

## Verdict

**PASS for the measured protected surface at all six samples.** The 1,718 tracked paths in `reports/round-{8..28}` plus `tools/gates/frozen/round-{8..28}` matched the declared baseline in Git blob identity and mode: every sample reported **0 mismatches, 0 missing paths, 0 protected status rows, 0 baseline-to-HEAD diff rows, and 0 tracked paths newer than the round-29 declaration timestamp**. The observed-byte manifest digest was identical at all six samples.

**Lane-wide status changed only outside the protected surface.** At the first four samples, `git status --porcelain=v1 -uall` had 0 rows. At the follow-up it had 5 rows and then 6, all new `reports/round-29/` paths from peer seats. This seat did not inspect or certify their contents. The `scope.md` file itself is being filed after those samples and is not included in their status counts.

The fleet root outside this lane was **not assessed**: the assignment's boundary is the kotodama lane, and no commands were run outside it. This is not a fleet-cleanliness claim or round acceptance.

## Baseline and protected surface

- `reports/round-29/claims.json:5` declares baseline `3b13a2f2821ed6f8ac1217842ab6830d592c7935`. On **2026-10-18**, `git show -s --format='%H %P %cI %s' 3b13a2f2821ed6f8ac1217842ab6830d592c7935 HEAD` showed baseline commit time `2026-10-18T17:50:46-03:00` and HEAD `e923d6ecaf5fd9d256e4b377745bd3d24f5e2d47`, whose parent is that baseline and whose declaration time is `2026-10-18T17:51:47-03:00` (`20:51:47Z`). `git merge-base --is-ancestor <baseline> HEAD` exited 0 at **20:53:13Z, 2026-10-18**. The snapshot used the declaration commit timestamp, `20:51:47Z`, as the mtime cutoff.
- On **2026-10-18 at 21:00:35Z**, a read-only `python3 -B` census running `git ls-tree -r --name-only <baseline> -- <round-path>` for each `n` in `range(8, 29)` returned **1,583** report paths and **135** frozen paths, **1,718 total**. Reports round 28 contributes **131** paths; the other report counts were r8 153, r9 87, r10 73, r11 252, r12 44, r13 2, r14 40, r15 20, r16 23, r17 67, r18 60, r19 71, r20 81, r21 45, r22 77, r23 43, r24 20, r25 67, r26 100, and r27 127. Frozen paths are r11 18, r18 12, r20 5, r22 39, r23 15, r25 14, and r26 32; the other round-tagged frozen directories in this range have 0 tracked paths. Command and date: `python3 -B -` invoking `git ls-tree -r --name-only <baseline> -- f"{root}/round-{n}"` for both roots and each round, **2026-10-18**.
- This is a scope extension, not a count discrepancy with `reports/round-28/scope.md:26,32–35`: that report covered rounds 8–27 (1,452 report paths + 135 frozen = 1,587); this watch adds the 131 tracked round-28 report paths, giving 1,718.

## Measurement record

The read-only snapshot command enumerated baseline tree entries with `git ls-tree -r -z`, compared each live Git-blob SHA-1 and file mode with the baseline entry, and collected the sorted-path/sha256-bytes manifest. It also queried protected `git status`, baseline-to-HEAD `git diff`, ignored paths, lane status, and mtimes against the HEAD declaration timestamp. Command: `python3 -B -` with the replay logic below; date **2026-10-18**.

| Sample time (UTC) | Tracked | Mismatches | Missing | Protected status / baseline→HEAD diff | Post-declaration mtimes | Manifest SHA-256 |
|---|---:|---:|---:|---:|---:|---|
| 20:55:48.914 | 1,718 | 0 | 0 | 0 / 0 | 0 | `64564895f8a32e1a19a17b88b7fa1cee587066e431fcaf1279b67f961cec35c0` |
| 20:56:49.050 | 1,718 | 0 | 0 | 0 / 0 | 0 | same |
| 20:57:49.217 | 1,718 | 0 | 0 | 0 / 0 | 0 | same |
| 20:58:49.368 | 1,718 | 0 | 0 | 0 / 0 | 0 | same |
| 21:00:50.794 | 1,718 | 0 | 0 | 0 / 0 | 0 | same |
| 21:01:50.846 | 1,718 | 0 | 0 | 0 / 0 | 0 | same |

The first four samples were spaced about 60 seconds apart; the two follow-up samples were also spaced about 60 seconds apart. Every row above is from the snapshot command on **2026-10-18**. It tests the current bytes and modes against the baseline; finite sampling cannot rule out a transient write-and-restore between samples.

At the four initial samples (**20:55:48Z through 20:58:49Z**), `git ls-files --others --ignored --exclude-standard` counted **34 ignored paths** inside the protected directories. The two follow-up snapshots did not query this count. The four counts were returned by the initial snapshot command on **2026-10-18**; ignored files have no tracked baseline, and this seat does not infer their history from that count. A path/size/short-SHA256 inventory was independently printed by `python3 -B -` at **2026-10-18T21:00:35Z**.

The in-memory detector control in the snapshot command used `reports/round-8/claims.json` and `reports/round-28/claims.json`: both live blobs matched the baseline, a probe appended only in memory changed the calculated blob, and both files remained byte-identical on reread. Command: same read-only `python3 -B -` run before sample 1 on **2026-10-18**. No probe was written to disk.

Lane-status observations, command `git status --porcelain=v1 -uall`, **2026-10-18**:

- At **20:55:48Z, 20:56:49Z, 20:57:49Z, and 20:58:49Z**: 0 lane rows.
- At **21:00:35Z**: 5 rows, `reports/round-29/adjacency/register-law.md`, `reports/round-29/recount/C05.md`, `C06.md`, `C07.md`, and `C08.md`.
- At **21:00:50Z and 21:01:50Z**: 6 rows, the same five plus `reports/round-29/rerun.json`.

The 5→6 transition was entirely in round 29; the protected-surface checks remained green in both follow-up samples. This seat neither altered nor attributed those peer files.

## Read-only replay

From the kotodama lane root, this reproduces a single protected-surface snapshot without executing any historical validator or writing a receipt. `export TMPDIR="$PWD/.scratch"` was set before the command. The six-sample watch used this same comparison with a 60-second interval.

```bash
export TMPDIR="$PWD/.scratch"
python3 -B - <<'PY'
import datetime, hashlib, os, stat, subprocess
base = '3b13a2f2821ed6f8ac1217842ab6830d592c7935'
paths = [f'reports/round-{n}' for n in range(8, 29)] + [f'tools/gates/frozen/round-{n}' for n in range(8, 29)]
def git(*args):
    return subprocess.check_output(['git', *args])
def blob(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
entries = []
for row in git('ls-tree', '-r', '-z', base, '--', *paths).split(b'\0'):
    if row:
        meta, rawpath = row.split(b'\t', 1)
        mode, _, oid = meta.decode().split()
        entries.append((os.fsdecode(rawpath), mode, oid))
cutoff = datetime.datetime.fromisoformat(git('show', '-s', '--format=%cI', 'HEAD').decode().strip()).astimezone(datetime.timezone.utc)
mismatches, missing, newer, manifest = [], [], [], []
for path, mode, oid in entries:
    try:
        st = os.lstat(path)
        data = os.readlink(path).encode() if stat.S_ISLNK(st.st_mode) else open(path, 'rb').read()
    except FileNotFoundError:
        missing.append(path)
        continue
    live_mode = '120000' if stat.S_ISLNK(st.st_mode) else ('100755' if st.st_mode & 0o111 else '100644')
    if (blob(data), live_mode) != (oid, mode):
        mismatches.append(path)
    manifest.append(path.encode() + b'\0' + hashlib.sha256(data).hexdigest().encode() + b'\n')
    if datetime.datetime.fromtimestamp(st.st_mtime, datetime.timezone.utc) > cutoff:
        newer.append(path)
print('tracked', len(entries), 'mismatches', mismatches, 'missing', missing)
print('manifest_sha256', hashlib.sha256(b''.join(sorted(manifest))).hexdigest())
print('protected_status', git('status', '--porcelain=v1', '-uall', '--', *paths).decode().splitlines())
print('baseline_head_diff', git('diff', '--name-status', base, 'HEAD', '--', *paths).decode().splitlines())
print('tracked_newer_than_declaration', newer)
print('protected_ignored_count', len(git('ls-files', '--others', '--ignored', '--exclude-standard', '-z', '--', *paths).split(b'\0')) - 1)
PY
```

## Limits and handoff

- The measured pass is byte/mode cleanliness at the six recorded instants, not proof that no transient rewrite occurred between them.
- The ignored-path inventory is outside the tracked baseline; no historical-identity claim is made for it.
- Fleet-root cleanliness is deliberately not asserted because this worker's allowed work surface is this lane.
- No round-25–28 validators were run; this seat's scope fragment is not a substitute for claim C/O/A verification or parent integration.

FILES: reports/round-29/scope.md | SUMMARY: X02 scope watch — rounds 8–28 plus frozen generations passed six baseline blob/mode samples over 1,718 tracked paths; 0 protected changes, with peer round-29 files outside the protected surface.
