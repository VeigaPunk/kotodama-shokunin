# Round 25 — Scope watch (SCRIBE X39)

- **Axes:** filed-artifact immutability (rounds 8–24); fleet-root cleanliness; bounded, reproducible evidence.
- **Assignment:** scope watch — filed rounds 8–24 untouched, fleet root clean.
- **Date:** 2026-10-18. All timestamps UTC unless a `−03:00` local form is given.
- **Write scope:** this fragment only. No shared bookkeeping, source fixes, historical validators, Git mutations, commits, pushes, sibling writes. Scratch (`TMPDIR=$PWD/.scratch`) is lane-internal and gitignored.

## Verdict

**PASS for the filed-round surface; NOT CLEAN for the fleet root.**

- **Filed rounds 8–24: PASS.** At the initial sample and all three closing-watch samples, all **1,158** tracked paths under `reports/round-{8..24}` matched the declared baseline `e06581b7fc2b50050a336f7f38a7e2baebcc6abc` in Git blob identity and executable/symlink mode — **0 mismatches**. `git diff --name-status <baseline> HEAD -- reports/round-{8..24}` is empty and `git status` over that surface is empty. No round-25 seat write to a filed round-8–24 path was observed.
- **Fleet root: NOT CLEAN.** Two debris families exist under the fleet root, both with last-write times **before** the round-25 dispatch commit (14:23:25−03:00). Neither is a kotodama filed artifact, and one is **invisible to `git status`** (see the masking control below). The assignment's "fleet root clean" clause therefore **fails as observed**; the debris predates this round and is disclosed, not dispositioned, here.

This is a scoped observation at the recorded times, not round acceptance and not a claim that no transient write ever occurred.

## Baseline binding

- Declared baseline `reports/round-25/claims.json:5` = `e06581b7fc2b50050a336f7f38a7e2baebcc6abc` (round-24 close).
- Lane HEAD at watch = `f74fc9403d4b02c8ee76439eb133e3dea9b65b14` ("round-25: declare loop-3 build-1 claims O/D/C"), commit time 2026-10-18T14:23:25−03:00. `git merge-base --is-ancestor` is satisfied (baseline is the parent commit).
- `git diff --name-status e06581b..HEAD -- reports/round-{8..24}` **empty**: the declaration commit added only `reports/round-25/{claims,targets}.json`.
- Fleet HEAD = `8b150d6cffdb153c44edc3118ad62a853b16d3cb` ("close kotodama round-24"), unchanged across all samples.

## Protected-surface evidence (command + date on each)

All commands run **2026-10-18** with `export TMPDIR="$PWD/.scratch"`; script `.scratch/x39-watch.py`, transcripts `.scratch/x39-snapshot-1.json`, `.scratch/x39-watchlog.json`.

| Measurement | Command | Result |
|---|---|---|
| Tracked filed paths (8–24) | `git ls-tree -r <baseline> -- reports/round-{8..24}` | **1,158** |
| Blob/mode comparison vs working bytes | script `snapshot()` | **0 mismatches** |
| Observed-bytes manifest digest | sha256 of sorted `path\0bytes` rows | `dbacc2b475e881e20cef79c5920c3e0b04611c8924b03eab15ab8d9a2bb17755` |
| Baseline→HEAD diff, protected surface | `git diff --name-status` | empty |
| `git status` over protected surface | `--porcelain=v1 -uall` | empty |
| Ignored paths under protected surface | `git ls-files --others --ignored --exclude-standard` | **11** (below) |
| Lane-wide status | `--porcelain=v1 -uall` | empty at sample 1 (see closing watch) |

Ignored paths under `reports/round-{8..24}` (no committed baseline; observed stable across all samples):

`reports/round-9/baselines/{handoff-packet-check,myth-consistency-gate,naming-collision-gate}/run.log`,
`reports/round-11/handoff/{run.log,tamper-control.log}`,
`reports/round-20/handoff/run.log`,
`reports/round-22/handoff/{declared-in,declared-in-r2}/run.log`,
`reports/round-23/wording/declared-in-r3/run.log`,
`reports/round-23/__pycache__/run-validation.cpython-314.pyc`,
`reports/round-24/__pycache__/run-validation.cpython-314.pyc`.

(The round-23 watch recorded eight; three more are now present — two `__pycache__` byte-cache files from executed validators and one round-23 wording `run.log`. All three are ignorable build/run residue, none is a filed artifact, and all were stable across the three samples.)

## Detector control (the audit fires on tampering)

`.scratch/x39-watch.py control` on 2026-10-18, target `reports/round-8/claims.json`:

- baseline blob SHA-1 **matches** live bytes → `clean_match: true`
- appending `b"\nx39-in-memory-only-probe\n"` **in memory only** → blob SHA-1 differs → `tamper_detected: true`
- live file re-read **byte-identical** → `live_bytes_unchanged: true`

`pass: true`. This controls the *audit detector*, not any round's product. No file was created or altered.

## Fleet-root findings

Fleet root = `/home/vgpnk/Projects/shokunin`. `git status --porcelain=v1 -uall` returned **10 rows**, all `?? .scratch/*.out` — i.e. the fleet root is not status-clean, contrary to the round-23 observation.

### F1 — untracked fleet `.scratch/*.out` (10 files)

`ls -la .scratch/` and `stat -c '%Y %y %n'` (2026-10-18): eight files at **13:10:25−03:00** (`battery.out`, `coupling.out`, `craft.out`, `d2check.out`, `d3check.out`, `replay-r22.out`, `replay-r3.out`) plus three at **13:15:49−03:00** (`rv5-p.out`, `rv6-p.out`, `rv7-p.out`). Contents are single-line `python3: can't open file '<path>': [Errno 2] No such file or directory` errors — lane tools invoked from the fleet root rather than from a lane directory (e.g. `.../shokunin/tools/check-gate-battery.py`, `.../shokunin/tools/replay-frozen.py`, `/tmp/coldrun-b/export2/reports/round-5/run-validation.py`). All ten predate round-25 dispatch by over an hour and are lane-external scratch that leaked upward; they are not kotodama filed artifacts. Fleet `.gitignore` does not cover `.scratch/`, so they surface as untracked.

### F2 — stray `bash: ` directory tree holding a real receipt

A directory whose literal name is `bash: ` (six bytes: `b a s h : space`) sits in the fleet root, created **2026-10-18T14:01:47Z**. It is a nested path chain of **8 directories**, ending in a single **10,139-byte regular file** whose name is the truncated shell error string:

`bash: /home/vgpnk/Projects/shokunin/souji-shokunin/tests/tools/souji-verify.sh: No such file or directory`

- `sha256` of that file = `3a127f03b9afbfef76d8cfb4274e0cb16aa7d59b915ce19e70a236321e9b3c33`.
- Content is a **souji-shokunin round-4 adversarial seat S54** JSON receipt (`"seat": "S54"`, `"round": 4`, `"lane": "souji-shokunin"`, assignment rows p/q/r; `totals` pass 8 / fail 7 / warn 4 / info 1). It is a *duplicate* of a seat receipt written to a path that a mis-quoted command built: the leading `bash:` token was taken as a directory name and the error string as the filename, rather than the command being run. The receipt is souji-shokunin's product; this seat neither authored nor certifies it, and does **not** touch it.

### Masking control — why a plain status check would call this root clean

The stray tree is **hidden from `git status`** by the fleet ignore rule:

```
$ git check-ignore -v 'bash: /home/vgpnk/Projects/shokunin/souji-shokunin'
.gitignore:1:*-shokunin/	bash: /home/vgpnk/Projects/shokunin/souji-shokunin
$ git status --porcelain=v1 -uall -- 'bash: '      # → 0 rows
$ find 'bash: ' | wc -l                            # → 9 entries
```

The inner directory `.../shokunin/souji-shokunin` matches `*-shokunin/`, so Git reports the whole tree as ignored (`!! "bash: /home/vgpnk/Projects/shokunin/souji-shokunin/"`). A watch that only reads `git status` — the round-23 method — reports the fleet root clean while a 10 KB receipt sits in a stray directory. **This is the operative scope-watch defect:** fleet cleanliness must be asserted over the *filesystem*, not only over Git's untracked view.

## Closing watch

Read-only, `range(1, 4)` with `time.sleep(60)`; command run **2026-10-18**, exit **0**; samples at **17:25:45.581898Z**, **17:26:45.637236Z**, **17:27:45.693273Z**.

Held constant at all three samples: mismatches `[]`; manifest digest `dbacc2b4…`; protected status empty; baseline→HEAD diff empty; 11 ignored paths unchanged; 10 fleet status rows unchanged; fleet HEAD and lane HEAD unchanged. `tracked` = 1,158.

The **only** channel that moved was lane-wide status, and every delta is a **peer's new round-25** path, never a filed round-8–24 path:

| Sample | New untracked paths |
|---|---|
| 1 | — |
| 2 | `reports/round-25/audit/c31-lessons-index-audit.py` |
| 3 | `corpus/lessons/README.md`, `reports/round-25/audit/c31-lessons-index-audit.py`, `reports/round-25/lessons/lessons-index-census.py` |

These are live writes by the C-lessons claimants, all outside the protected filed surface. `watch_consistent` is therefore **false only for `lane_status`**, true for every protected and fleet channel.

## Read-only replay

From the lane root (`export TMPDIR="$PWD/.scratch"` first), this reproduces the protected verdict, the detector control, the fleet rows, and the masking control without writing any receipt or executing a historical validator:

```bash
export TMPDIR="$PWD/.scratch"
python3 .scratch/x39-watch.py snapshot    # protected: mismatches must be []
python3 .scratch/x39-watch.py control     # detector control: pass must be true
python3 .scratch/x39-watch.py stray       # lists fleet-root non-*-shokunin dirs
cd /home/vgpnk/Projects/shokunin
git status --porcelain=v1 --untracked-files=all          # 10 ?? .scratch/*.out rows
git check-ignore -v 'bash: /home/vgpnk/Projects/shokunin/souji-shokunin'
find 'bash: ' -type f                                    # 1 file, 10,139 bytes
```

Assertions: `snapshot().mismatches == []`; `control().pass is True`; the fleet status rows equal the ten listed names; `find 'bash: ' -type f` prints exactly the truncated-name file above.

## Limits and handoff

- Repeated sampling cannot prove no write-and-restore occurred between samples; the manifest digest is a stability anchor, not a historical identity claim.
- Ignored files have no Git baseline; observed stability does not establish their historical identity.
- F1/F2 attribution is by content and mtime only. The `bash: ` receipt's author is inferred from its own `"seat": "S54"` field, not verified. Both families predate round-25 dispatch, so no round-25 seat authored them.
- The fleet-root cleanliness clause **fails as observed**. Disposition of F1 (delete the ten `.out` files or ignore fleet `.scratch/`) and F2 (remove the stray tree; re-file the S54 receipt at its correct souji path) belongs to the parent integrator and the souji-shokunin lane — this seat left every path byte-identical to how it found it.
- No validator was executed here, including historical validators that could rewrite filed receipts.

FILES: reports/round-25/scope.md, .scratch/x39-watch.py, .scratch/x39-snapshot-1.json, .scratch/x39-watchlog.json
