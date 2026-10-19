# Round 31 — Scope watch (SCRIBE X16)

- **Axes:** filed-artifact immutability; lane-local write boundaries; reproducible, bounded evidence.
- **Assignment:** SCRIBE X16 — scope watch.
- **Date:** 2026-10-18; observation times below are UTC.
- **Write scope:** `reports/round-31/scope.md` only. This seat wrote no scratch files, ran no historical validators, made no source or pin changes, and ran no Git-mutating commands, commits, or pushes. Commands used `export TMPDIR="$PWD/.scratch"` and `python3 -B`; the final replay also disables Git optional locks.

## Verdict

**PASS at the recorded instants for the protected tracked surface.** The four primary samples at 22:41:29.668Z, 22:42:29.712Z, 22:43:29.754Z and 22:44:29.798Z compared **1,823 tracked paths** with declared baseline `71cd9d376ebd144e94e4f12d997f73e5d2839aa9`. Each found **0 byte/mode mismatches, 0 missing paths, 0 protected status rows, 0 baseline-to-HEAD diff rows, and 0 tracked mtimes newer than the declaration**. Command/date for these counts: the read-only `python3 -B -` watch described below, **2026-10-18**.

The supplemental watch also found the full frozen-gate surface unchanged and no observed changes to ignored historical files. No protected breach was observed. This is **not** round acceptance, a semantic review of peer claims C/O/D, fleet-root cleanliness, or proof against a transient write-and-restore between samples.

## Baseline binding and census

`reports/round-31/claims.json:5` and `reports/round-31/targets.json:4` declare the same baseline. At **2026-10-18T22:40Z**, `git show -s --format='%H %P %cI %s' <baseline> HEAD` returned:

- Baseline `71cd9d376ebd144e94e4f12d997f73e5d2839aa9` (round-30 admit), committed `2026-10-18T19:33:05-03:00` (22:33:05Z).
- Declaration HEAD `e8d2d0dadd3ccd1fbb7481793cfaf9bcd761826c`, whose parent is the baseline; committed `2026-10-18T19:34:08-03:00` (22:34:08Z). This fixed declaration time is the mtime cutoff.
- `git merge-base --is-ancestor <baseline> HEAD` exited **0**, same command batch/date.
- `git diff-tree --no-commit-id --name-status -r HEAD`, **2026-10-18T22:40Z**, listed only the declaration's additions `reports/round-31/claims.json` and `reports/round-31/targets.json`.

The primary protected surface is `reports/round-{8..30}` plus `tools/gates/frozen/round-{8..30}` (the round-tagged frozen roots), bound to the baseline tree by `git ls-tree`. `reports/round-31/run-validation.py` — the claims' counting command — was **not present** at observation time (checked **22:47Z**) and was not executed by this seat; if it later declares a different protected-root set, reconciliation belongs to the validator seat.

Census command/date: `python3 -B -` enumerating `git ls-tree -r -z <baseline> -- <protected roots>`, **2026-10-18T22:40Z**:

- Reports: **1,688** tracked paths. The reports-only counts are r8 153; r9 87; r10 73; r11 252; r12 44; r13 2; r14 40; r15 20; r16 23; r17 67; r18 60; r19 71; r20 81; r21 45; r22 77; r23 43; r24 20; r25 67; r26 100; r27 127; r28 131; r29 46; r30 59.
- Round-tagged frozen gates: **135** tracked paths: r11 18; r18 12; r20 5; r22 39; r23 15; r25 14; r26 32; other round-tagged roots in the range have no tracked entries.
- Total **1,823** = 1,688 + 135. The rounds 8–29 subset is 1,629 + 135 = **1,764**, exactly `reports/round-30/scope.md:27-28`; the increase is exactly the **59** newly protected round-30 report paths, not a discrepancy in the older census.

## Primary observation record

Command/date for every row: `python3 -B -` reading baseline entries with `git ls-tree -r -z`, calculating Git blob SHA-1 and executable/symlink mode from live bytes, reading `git status --porcelain=v1 -uall -- <protected roots>` and `git diff --name-status <baseline> HEAD -- <protected roots>`, and scanning mtimes against 22:34:08Z, **2026-10-18**. Consecutive samples used `time.sleep(60)`; neither hashes nor controls write objects or files.

| UTC | Tracked | Byte/mode mismatches | Missing | Protected status / HEAD diff | Newer mtimes |
|---|---:|---:|---:|---:|---:|
| 22:41:29.668 | 1,823 | 0 | 0 | 0 / 0 | 0 |
| 22:42:29.712 | 1,823 | 0 | 0 | 0 / 0 | 0 |
| 22:43:29.754 | 1,823 | 0 | 0 | 0 / 0 | 0 |
| 22:44:29.798 | 1,823 | 0 | 0 | 0 / 0 | 0 |

Every live primary manifest SHA-256 was:

`0e9b66e1abb0b4b8fe2eb02c81349c862cde137da98ce292e82e7fffcfc42a70`

The manifest is SHA-256 of sorted `path + NUL + sha256(file bytes) + LF` rows; modes are checked separately. An independent command, **`python3 -B -` using `git cat-file --batch` to read the protected baseline blobs at 2026-10-18T22:41:42Z**, produced that same digest over **1,823** entries and consumed the batch exactly. Thus the live manifest is independently bound to baseline bytes, not merely stable across live samples.

**Detector controls, command `python3 -B -`, 2026-10-18T22:44:30Z:** `reports/round-8/claims.json` and `reports/round-30/claims.json` each matched its baseline blob/mode; appending `X16-IN-MEMORY-CONTROL` only to an in-memory byte string changed the calculated Git blob; toggling the in-memory executable mode differed from the baseline mode; rereading each real path showed unchanged bytes/mode. All controls passed. No probe was written to a protected path, and there is no fix claimed by this seat.

## Supplemental frozen, ignored-file and province checks

Command/date: a parallel read-only `python3 -B -` watch using `git ls-tree -r -z <baseline> -- tools/gates/frozen`, live blob/mode/mtime comparison, and `git ls-files --others --ignored --exclude-standard -z -- <protected roots>`, **2026-10-18**, at **22:41:29.642Z, 22:42:29.656Z and 22:43:29.669Z**, each separated by `time.sleep(60)`.

- The **237** tracked paths under **all** `tools/gates/frozen` (including generations outside the primary round-tagged set) had **0 mismatches, 0 missing paths, and 0 mtimes newer than the declaration** at all three samples. The all-frozen manifest digest `9e2910cc3815e04ab0c645f05152fbd894088d6f103036cdb158ef344f35f5eb` equals both round-30's recorded value (`reports/round-30/scope.md:54`) and this seat's independent baseline-blob binding over **237** entries at **22:41:42Z**, so the frozen surface is byte-identical across rounds.
- The **35** ignored paths under the primary roots had **0 additions, 0 removals, 0 byte/mode/mtime changes against the first supplemental observation** at all three samples. They are **22** historical run/tamper-control logs and **13** `__pycache__` `.pyc` files — no file with a committed baseline identity. The only ignored path under the newly included round-30 root is `reports/round-30/handoff/declared-in-r6/run.log`, consistent with the 34 → 35 delta against `reports/round-30/scope.md:55` (that watch covered rounds 8–29 only).
- The ignored-file manifest, covering sorted `path + NUL + sha256(bytes) + NUL + mode + NUL + mtime_ns + LF` rows, was identical at all three samples: `96d877dee029c05a386fad5226635605b2ce948f74a0579951901955873e8cd4`.
- `git diff --name-status <baseline> -- PROVINCE.md` was empty at all three supplemental samples, command `python3 -B -` invoking that Git comparison, **2026-10-18**.

## Lane working-tree boundary

The lane was clean at **22:39:52Z**, command `git status --porcelain=v1 -uall`, **2026-10-18** (0 rows). Peer wave work subsequently appeared outside the protected roots. At **22:46:46Z**, the same command counted **14** lane status rows, all untracked, all under `reports/round-31/`: the C seat's `closure-ledger.json`, two `jinii/` drafts, three `sweep-audit*` files, and eight `telemetry/` files. No modified tracked paths existed at that instant, and the protected-status column of every primary sample stayed 0 throughout. This fragment itself was not yet written at that count. This seat does not certify peer fragments' semantics, assignment ownership, or claim results; fleet-root cleanliness is deliberately **not assessed** and no commands inspected siblings, the fleet root, the world bible, or domain source trees.

## Read-only replay

From this lane root, the following is a single-snapshot replay of the measured comparisons, with the same baseline and fixed declaration cutoff. It also recomputes the supplemental ignored-file manifest and the in-memory detector controls. The recorded primary/supplemental watches performed these comparisons in loops with 60-second sleeps; a later replay is a new observation, not an extension of their historical time window. No historical validator is invoked.

```bash
export TMPDIR="$PWD/.scratch" GIT_OPTIONAL_LOCKS=0
python3 -B - <<'PY'
import datetime, hashlib, json, os, stat, subprocess
BASE = '71cd9d376ebd144e94e4f12d997f73e5d2839aa9'
CUTOFF = datetime.datetime.fromisoformat('2026-10-18T22:34:08+00:00').timestamp()
ROOTS = [f'{root}/round-{n}' for root in ('reports', 'tools/gates/frozen') for n in range(8, 31)]
EXPECTED = '0e9b66e1abb0b4b8fe2eb02c81349c862cde137da98ce292e82e7fffcfc42a70'
FROZEN = '9e2910cc3815e04ab0c645f05152fbd894088d6f103036cdb158ef344f35f5eb'
IGNORED = '96d877dee029c05a386fad5226635605b2ce948f74a0579951901955873e8cd4'
def git(*args):
    return subprocess.check_output(['git', *args])
def blob(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
def live(path):
    st = os.lstat(path)
    if stat.S_ISLNK(st.st_mode):
        data, mode = os.fsencode(os.readlink(path)), '120000'
    else:
        with open(path, 'rb') as stream:
            data = stream.read()
        mode = '100755' if st.st_mode & 0o111 else '100644'
    return data, mode, st.st_mtime_ns

def entries(roots):
    found = []
    for row in git('ls-tree', '-r', '-z', BASE, '--', *roots).split(b'\0'):
        if row:
            mode, kind, oid = row.split(b'\t', 1)[0].decode().split()
            found.append((os.fsdecode(row.split(b'\t', 1)[1]), mode, oid))
    return found

def measure(rows):
    mismatches, missing, newer, manifest = [], [], [], []
    for path, expected_mode, oid in rows:
        try:
            data, mode, mtime = live(path)
        except FileNotFoundError:
            missing.append(path)
            continue
        if (blob(data), mode) != (oid, expected_mode):
            mismatches.append(path)
        if mtime / 1_000_000_000 > CUTOFF:
            newer.append(path)
        manifest.append(os.fsencode(path) + b'\0' + hashlib.sha256(data).hexdigest().encode() + b'\n')
    return dict(tracked=len(rows), mismatches=mismatches, missing=missing,
                newer_than_declaration=newer,
                manifest_sha256=hashlib.sha256(b''.join(sorted(manifest))).hexdigest())

primary_rows = entries(ROOTS)
primary = measure(primary_rows)
frozen = measure(entries(['tools/gates/frozen']))
by_path = {path: (mode, oid) for path, mode, oid in primary_rows}
controls = []
for path in ('reports/round-8/claims.json', 'reports/round-30/claims.json'):
    data, mode, _ = live(path)
    expected_mode, oid = by_path[path]
    reread, reread_mode, _ = live(path)
    mutant_mode = '100755' if mode == '100644' else '100644'
    controls.append(dict(path=path, clean_matches=(blob(data), mode) == (oid, expected_mode),
        byte_tamper_detected=blob(data + b'\nX16-IN-MEMORY-CONTROL\n') != oid,
        mode_tamper_detected=mutant_mode != expected_mode,
        reread_unchanged=(data, mode) == (reread, reread_mode)))
ignored_paths = sorted(os.fsdecode(p) for p in git('ls-files', '--others', '--ignored',
    '--exclude-standard', '-z', '--', *ROOTS).split(b'\0') if p)
ignored_rows = []
for path in ignored_paths:
    data, mode, mtime = live(path)
    ignored_rows.append(os.fsencode(path) + b'\0' + hashlib.sha256(data).hexdigest().encode()
                        + b'\0' + mode.encode() + b'\0' + str(mtime).encode() + b'\n')
ignored_digest = hashlib.sha256(b''.join(ignored_rows)).hexdigest()
protected_status = git('status', '--porcelain=v1', '-uall', '--', *ROOTS).decode().splitlines()
head_diff = git('diff', '--name-status', BASE, 'HEAD', '--', *ROOTS).decode().splitlines()
result = dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(), baseline=BASE,
    head=git('rev-parse', 'HEAD').decode().strip(), primary=primary, all_frozen=frozen,
    protected_status=protected_status, baseline_head_diff=head_diff, controls=controls,
    protected_ignored_count=len(ignored_paths), ignored_manifest_sha256=ignored_digest,
    ignored_matches_observed_window=ignored_digest == IGNORED,
    province_diff=git('diff', '--name-status', BASE, '--', 'PROVINCE.md').decode().splitlines(),
    lane_status_count=len(git('status', '--porcelain=v1', '-uall').decode().splitlines()))
print(json.dumps(result, indent=2))
assert primary['tracked'] == 1823 and primary['manifest_sha256'] == EXPECTED
assert not primary['mismatches'] and not primary['missing'] and not primary['newer_than_declaration']
assert frozen['tracked'] == 237 and frozen['manifest_sha256'] == FROZEN
assert not frozen['mismatches'] and not frozen['missing'] and not frozen['newer_than_declaration']
assert not protected_status and not head_diff and not result['province_diff']
assert len(ignored_paths) == 35 and ignored_digest == IGNORED
assert all(all(row[key] for key in ('clean_matches', 'byte_tamper_detected',
                                   'mode_tamper_detected', 'reread_unchanged')) for row in controls)
PY
echo REPORT_REPLAY_EXIT_0
```

## Filed-deliverable replay verification

At **2026-10-18T22:49:06Z** (a first identical extraction at **22:48:53Z** also exited 0), the replay above was extracted from this actual filed fragment and executed without a scratch script. Command: `python3 -B -` extracting the sole `bash` fenced block and calling `subprocess.run(['bash'], input=blocks[0], text=True, capture_output=True)`. It exited **0** and printed `REPORT_REPLAY_EXIT_0`.

That replay snapshot found **1,823** primary tracked paths and **237** all-frozen tracked paths, both with **0 mismatches, 0 missing paths and 0 newer mtimes**; the primary/frozen manifests matched the digests above. Protected status, baseline-to-HEAD diff and province diff were empty; the **35** ignored files still matched the observed-window manifest; both byte/mode detector controls passed. The lane status count was then **18** rows, outside the primary protected surface. Counts, commands and date are from this filed-deliverable replay, **2026-10-18**. No round-31 acceptance or claim C/O/D verification is inferred from its success.

## Limits and parent handoff

- This fragment measures observations at the recorded instants, not every filesystem event. Neither a final hash nor finite mtime sampling rules out all intervening writes.
- Ignored paths have only an observed-window reference, not a committed historical baseline. Scratch paths were not surveyed or certified.
- Lane-local peer fragments are visible but not attributed or judged here. Claims C/O/D, the closure ledger, the final sweep, the jin'i-ryu delta and round acceptance remain the relevant seats' and integrator's work.
- Historical validator execution was deliberately avoided: `reports/round-28/scope.md:12` records that a historical round-27 battery rewrote a filed receipt even when invoked with `--check`; `reports/round-31/run-validation.py` did not exist during this watch.
- The parent should integrate this fragment into append-only `LOG.md` bookkeeping and rerun the read-only snapshot after final integration if it needs a later endpoint. This seat does not append shared bookkeeping.

FILES: reports/round-31/scope.md | SUMMARY: X16 observed rounds 8–30 plus round-tagged frozen artifacts clean across four 60-second samples (1,823 tracked paths, manifest bound to baseline blobs); supplemental all-frozen and ignored-file watches clean; fleet scope not assessed.
