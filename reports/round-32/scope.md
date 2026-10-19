# Round 32 — Scope watch (SCRIBE X17, the final watch)

- **Axes:** filed-artifact immutability; lane-local write boundaries; reproducible, bounded evidence.
- **Assignment:** SCRIBE X17 — scope watch (the final watch of the regimen).
- **Date:** 2026-10-19; observation times below are UTC (the wall clock rolled past midnight UTC shortly before the first sample).
- **Write scope:** `reports/round-32/scope.md` only. This seat wrote no scratch files, ran no historical validators, made no source or pin changes, and ran no Git-mutating commands, commits, or pushes. Commands used `export TMPDIR="$PWD/.scratch" PYTHONDONTWRITEBYTECODE=1` and `python3 -B`; the replay legs also disable Git optional locks.

## Verdict

**PASS at the recorded instants for the protected tracked surface.** The four primary samples at 00:34:51.023Z, 00:35:51.077Z, 00:36:51.133Z and 00:37:51.187Z (all **2026-10-19**) compared **1,870 tracked paths** with declared baseline `17e90b9047b289d7a63180a1dc1bebb074137e29`. Each found **0 byte/mode mismatches, 0 missing paths, 0 protected status rows, 0 baseline-to-HEAD diff rows, and 0 tracked mtimes newer than the declaration**. Command/date for these counts: the read-only `python3 -B -` watch described below, **2026-10-19**.

The supplemental watch also found the full frozen-gate surface unchanged (237 paths, byte-identical digests carried across from round 30/31) and no observed changes to ignored historical files. No protected breach was observed. This is **not** round acceptance, a semantic review of peer claims C/O/D, fleet-root cleanliness, or proof against a transient write-and-restore between samples.

## Baseline binding and census

`reports/round-32/claims.json:5` and `reports/round-32/targets.json:4` declare the same baseline. At **2026-10-19T00:33:20Z**, `git show -s --format='%H %P %cI %s' <baseline> HEAD` returned:

- Baseline `17e90b9047b289d7a63180a1dc1bebb074137e29` (round-31 admit, "round-31: admit C/O/D — closure ledger, final sweep, jin'i-ryu rule landed"), committed `2026-10-18T21:28:45-03:00` (2026-10-19T00:28:45Z).
- Declaration HEAD `4d500501a286d96f2eea8a6188c649255581301a`, whose parent is the baseline; committed `2026-10-18T21:30:17-03:00` (2026-10-19T00:30:17Z). This fixed declaration time is the mtime cutoff.
- `git merge-base --is-ancestor <baseline> HEAD` exited **0**, same command batch/date.
- `git diff-tree --no-commit-id --name-status -r HEAD`, **2026-10-19T00:33:20Z**, listed only the declaration's additions `reports/round-32/claims.json` and `reports/round-32/targets.json`.

The primary protected surface is `reports/round-{8..31}` plus `tools/gates/frozen/round-{8..31}` (the round-tagged frozen roots), bound to the baseline tree by `git ls-tree`. `reports/round-32/run-validation.py` — the claims' counting command — was **not present** during this watch (round-32 held only `claims.json` and `targets.json` at every sample) and was not executed by this seat; if it later declares a different protected-root set, reconciliation belongs to the validator seat.

Census command/date: `python3 -B -` enumerating `git ls-tree -r -z <baseline> -- <protected roots>`, **2026-10-19T00:34Z**:

- Reports: **1,735** tracked paths. Per round: r8 153; r9 87; r10 73; r11 252; r12 44; r13 2; r14 40; r15 20; r16 23; r17 67; r18 60; r19 72; r20 81; r21 45; r22 77; r23 43; r24 20; r25 68; r26 101; r27 128; r28 132; r29 46; r30 59; r31 42.
- Round-tagged frozen gates: **135** tracked paths (composition unchanged from `reports/round-31/scope.md:28`: r11 18; r18 12; r20 5; r22 39; r23 15; r25 14; r26 32 — every one of those roots is byte-clean at the baseline, so no composition change is possible without a mismatch).
- Total **1,870** = 1,735 + 135. Reconciliation with the prior watch is exact: rounds 8–30 at the round-31 watch baseline held **1,688** report paths (`reports/round-31/scope.md:27`); the round-31 admit added exactly **5** retroactive telemetry closing snapshots (`reports/round-19/telemetry/availability-close-19.json`, `reports/round-{25,26,27,28}/telemetry/availability-close-2{5,6,7,8}.json`, read from `git diff-tree -r 17e90b9`, **2026-10-19**) → 1,693; plus **42** newly protected round-31 report paths → 1,735. The five snapshots are precisely the retroactive act D13's landed jin'i-ryu rule required (rounds 19, 25, 26, 27, 28), so the closure rule's footprint is now visible in the protected surface itself.

## Primary observation record

Command/date for every row: `python3 -B -` reading baseline entries with `git ls-tree -r -z`, calculating Git blob SHA-1 and executable/symlink mode from live bytes, reading `git status --porcelain=v1 -uall -- <protected roots>` and `git diff --name-status <baseline> HEAD -- <protected roots>`, and scanning mtimes against 00:30:17Z, **2026-10-19**. Consecutive samples used `time.sleep(60)`; neither hashes nor controls write objects or files. Lane status (whole lane, `-uall`) was sampled in the same loop as a boundary indicator.

| UTC, 2026-10-19 | Tracked | Byte/mode mismatches | Missing | Protected status / HEAD diff | Newer mtimes | Lane status rows | Lane tracked modifications |
|---|---:|---:|---:|---:|---:|---:|---:|
| 00:34:51.023 | 1,870 | 0 | 0 | 0 / 0 | 0 | 8 | 0 |
| 00:35:51.077 | 1,870 | 0 | 0 | 0 / 0 | 0 | 8 | 0 |
| 00:36:51.133 | 1,870 | 0 | 0 | 0 / 0 | 0 | 9 | 0 |
| 00:37:51.187 | 1,870 | 0 | 0 | 0 / 0 | 0 | 12 | 0 |

Every live primary manifest SHA-256 was:

`712d09f0c4fadfe363165f2aa7fc727dc30614be497c2757ed9bcc4635463842`

The manifest is SHA-256 of sorted `path + NUL + sha256(file bytes) + LF` rows; modes are checked separately. An independent command, **`python3 -B -` using `git cat-file --batch` to read the protected baseline blobs at 2026-10-19T00:38:23Z**, produced that same digest over **1,870** entries and consumed the batch exactly. Thus the live manifest is independently bound to baseline bytes, not merely stable across live samples.

**Detector controls, command `python3 -B -`, 2026-10-19T00:37:51Z (final sample):** `reports/round-8/claims.json` and `reports/round-31/claims.json` each matched its baseline blob/mode; appending `X17-IN-MEMORY-CONTROL` only to an in-memory byte string changed the calculated Git blob; toggling the in-memory executable mode differed from the baseline mode; rereading each real path showed unchanged bytes/mode. All controls passed. No probe was written to a protected path, and there is no fix claimed by this seat.

## Supplemental frozen, ignored-file and province checks

Command/date: a parallel read-only `python3 -B -` watch using `git ls-tree -r -z <baseline> -- tools/gates/frozen`, live blob/mode/mtime comparison, and `git ls-files --others --ignored --exclude-standard -z -- <protected roots>`, **2026-10-19**, at **00:34:51.007Z, 00:35:51.064Z and 00:36:51.119Z**, each separated by `time.sleep(60)`.

- The **237** tracked paths under **all** `tools/gates/frozen` (including generations outside the primary round-tagged set) had **0 mismatches, 0 missing paths, and 0 mtimes newer than the declaration** at all three samples. The all-frozen manifest digest `9e2910cc3815e04ab0c645f05152fbd894088d6f103036cdb158ef344f35f5eb` equals both round-30's recorded value (`reports/round-30/scope.md:54`) and round-31's (`reports/round-31/scope.md:54`), so the frozen surface is byte-identical across rounds 30 → 31 → 32; the round-31 admit added no frozen-gate files (its diff touched only report paths, LOG/SCORECARD/AGENTS/SKILL).
- The **35** ignored paths under the primary roots had **0 additions, 0 removals, 0 byte/mode/mtime changes against the first supplemental observation** at all three samples. They are the same **22** historical run/tamper-control logs and **13** `__pycache__` `.pyc` files recorded by round 31 — round-31 contributes **0** ignored paths under the newly extended root. The only path class with a committed baseline identity is none of these; they are an observed-window reference, not a historical baseline.
- The ignored-file manifest, covering sorted `path + NUL + sha256(bytes) + NUL + mode + NUL + mtime_ns + LF` rows, was identical at all three samples and equals round-31's recorded value `96d877dee029c05a386fad5226635605b2ce948f74a0579951901955873e8cd4` (`reports/round-31/scope.md:56`) — untouched since that watch.
- `git diff --name-status <baseline> -- PROVINCE.md` was empty at all three supplemental samples, command `python3 -B -` invoking that Git comparison, **2026-10-19**.

## Lane working-tree boundary

The lane was clean at **2026-10-19T00:33:20Z**, command `git status --porcelain=v1 -uall`, **2026-10-19** (0 rows). Peer wave work subsequently appeared outside the protected roots: **8** untracked rows at the first two samples, **9** at the third, **12** at the fourth — all new files under `reports/round-32/` (the wave's own write surface). A dated follow-up reading at **00:40:22Z** (same command) counted **19** untracked rows, still **0** tracked modifications: the arrivals by then included the acceptance instrument `run-validation.py` (first present after the watch window — it was absent at every sample), the C seat's `completion-audit.md`/`completion-ledger.json`, two D dossier fragments, the sweep runner and audit set, and the telemetry directory. The protected status column never moved. This fragment itself was not yet written at the sample-time counts. This seat does not certify peer fragments' semantics, assignment ownership, or claim results; fleet-root cleanliness is deliberately **not assessed** and no commands inspected siblings, the fleet root, the world bible, or domain source trees.

## Read-only replay

From this lane root, the following is a single-snapshot replay of the measured comparisons, with the same baseline and fixed declaration cutoff. It also recomputes the supplemental ignored-file manifest and the in-memory detector controls. The recorded primary/supplemental watches performed these comparisons in loops with 60-second sleeps; a later replay is a new observation, not an extension of their historical time window. No historical validator is invoked.

```bash
export TMPDIR="$PWD/.scratch" PYTHONDONTWRITEBYTECODE=1 GIT_OPTIONAL_LOCKS=0
python3 -B - <<'PY'
import datetime, hashlib, json, os, stat, subprocess
BASE = '17e90b9047b289d7a63180a1dc1bebb074137e29'
CUTOFF = datetime.datetime.fromisoformat('2026-10-19T00:30:17+00:00').timestamp()
ROOTS = [f'{root}/round-{n}' for root in ('reports', 'tools/gates/frozen') for n in range(8, 32)]
EXPECTED = '712d09f0c4fadfe363165f2aa7fc727dc30614be497c2757ed9bcc4635463842'
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
for path in ('reports/round-8/claims.json', 'reports/round-31/claims.json'):
    data, mode, _ = live(path)
    expected_mode, oid = by_path[path]
    reread, reread_mode, _ = live(path)
    mutant_mode = '100755' if mode == '100644' else '100644'
    controls.append(dict(path=path, clean_matches=(blob(data), mode) == (oid, expected_mode),
        byte_tamper_detected=blob(data + b'\nX17-IN-MEMORY-CONTROL\n') != oid,
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
assert primary['tracked'] == 1870 and primary['manifest_sha256'] == EXPECTED
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

At **2026-10-19T00:40Z** the replay above was extracted from this actual filed fragment (the sole `bash` fenced block) and executed without a scratch script. Command: `python3 -B -` extracting the fenced block and calling `subprocess.run(['bash'], input=block, text=True, capture_output=True)`. Leg 1 ran with `TMPDIR="$PWD/.scratch"`; leg 2, the mirror leg, ran identically with `TMPDIR="/var/tmp"`. Both exited **0** and printed `REPORT_REPLAY_EXIT_0`; a confirming re-extraction of the same block from the final bytes of this file also exited **0** on both legs.

Each replay snapshot found **1,870** primary tracked paths and **237** all-frozen tracked paths, both with **0 mismatches, 0 missing paths and 0 newer mtimes**; the primary/frozen manifests matched the digests above. Protected status, baseline-to-HEAD diff and province diff were empty; the **35** ignored files still matched the observed-window manifest; both byte/mode detector controls passed. The lane status count was **19** rows at both legs, all untracked wave files under `reports/round-32/`, outside the primary protected surface. Counts, commands and date are from this filed-deliverable replay, **2026-10-19**. No round-32 acceptance or claim C/O/D verification is inferred from its success.

## Limits and parent handoff

- This fragment measures observations at the recorded instants, not every filesystem event. Neither a final hash nor finite mtime sampling rules out all intervening writes.
- Ignored paths have only an observed-window reference, not a committed historical baseline. A later ignored-manifest drift (e.g. a `.pyc` appearing under a protected root) fails the replay's assert by design and is **staleness evidence for a new dated reading**, not a defect in this index. Scratch paths were not surveyed or certified.
- Lane-local peer fragments are visible but not attributed or judged here. Claims C/O/D — the completion audit, the r32 final sweep, the final dossier — and round acceptance remain the relevant seats' and integrator's work.
- Historical validator execution was deliberately avoided: `reports/round-28/scope.md:12` records that a historical round-27 battery rewrote a filed receipt even when invoked with `--check`; `reports/round-32/run-validation.py` did not exist during this watch.
- This is the regimen's final scope watch. After the round-32 integration pass, the parent should rerun this replay for a new dated endpoint reading and bind the acceptance receipt to the stable read set. This seat does not append shared bookkeeping.

FILES: reports/round-32/scope.md | SUMMARY: X17 observed rounds 8–31 plus round-tagged frozen artifacts clean across four 60-second samples (1,870 tracked paths, manifest bound to baseline blobs, frozen surface byte-identical to rounds 30/31); wave wrote only untracked round-32 files; fleet scope not assessed.
