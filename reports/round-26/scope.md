# Round 26 — Scope watch (SCRIBE X57)

- **Axes:** filed-artifact immutability (rounds 8–25); fleet-root cleanliness; bounded, reproducible evidence.
- **Assignment:** scope watch — filed rounds 8–25 untouched, fleet root clean.
- **Date:** 2026-10-18. Timestamps are UTC unless a local `−03:00` form is given.
- **Write scope:** this fragment only. No shared bookkeeping, source fixes, packet/validator/pin edits, historical validator runs, Git mutations, commits, pushes, or sibling writes. `export TMPDIR=$PWD/.scratch` was set before every scratch-writing command; scratch lived in `.scratch/x57/` (gitignored, lane-internal). No filed rounds 8–25 byte was written by this seat.

## Verdict (scoped to this seat's observations)

**PASS for the filed-round surface; NOT CLEAN for the fleet root.**

- **Filed rounds 8–25: PASS.** At the initial sample and all three closing-watch samples, all **1,225** tracked paths under `reports/round-{8..25}` matched the declared baseline `fc13cd27b9e78d5d7c4f70740fd26c9383a7447b` in Git blob identity **and** executable/symlink mode — **0 mismatches, 0 missing**. `git diff --name-status <baseline> HEAD -- reports/round-{8..25}` is empty, `git status` over that surface is empty, and no path under the surface has a tracked-file mtime later than round-26 dispatch. No round-26 seat write to a filed round-8–25 path was observed.
- **Fleet root: NOT CLEAN, unchanged from round 25.** The two debris families the round-25 watch disclosed (F1 ten `?? .scratch/*.out` files; F2 a stray `bash: ` directory tree holding a 10,139-byte souji-shokunin receipt) are both still present, byte-identical and mtime-identical. Neither is a kotodama filed artifact; both predate round-26 dispatch by hours. The assignment's "fleet root clean" clause therefore **fails as observed**; the debris is disclosed, not dispositioned, here.

This is a scoped observation at the recorded times, not round acceptance and not a claim that no transient write ever occurred.

## Baseline binding

- Declared baseline `reports/round-26/claims.json:5` = `fc13cd27b9e78d5d7c4f70740fd26c9383a7447b` ("round-25: admit O/D/C …", commit time 2026-10-18T14:58:37−03:00).
- Lane HEAD at watch = `1ad491a1a4b0aef9ebdc1861dfb8237727503825` ("round-26: declare claims D/O/C …", 14:59:43−03:00). `git merge-base --is-ancestor fc13cd2 HEAD` → success (2026-10-18T18:01Z).
- `git show --stat HEAD` (2026-10-18T18:04Z) shows the declaration commit adds exactly two paths — `reports/round-26/claims.json` (`blob 3ffa3c0a`) and `reports/round-26/targets.json` (`blob 27c98e26`) — 44 insertions, and no filed round-8–25 path.
- Fleet HEAD = `a4a9796787f9b94251dccd1e40761eb7815e75b8` ("close kotodama round-25: admitted (devin provider test)", 14:59:08−03:00), unchanged across all samples.

## Protected-surface evidence (command + date on each)

All commands run **2026-10-18** from the lane root with `export TMPDIR="$PWD/.scratch"`; script `.scratch/x57/watch.py`, transcripts `.scratch/x57/watchlog.json`, `.scratch/x57/control.json`.

| Measurement | Command | Result |
|---|---|---|
| Tracked filed paths (8–25) | `git ls-tree -r fc13cd2 -- reports/round-{8..25}` | **1,225** |
| Blob SHA-1 + mode comparison vs working bytes | `python3 .scratch/x57/watch.py snapshot` | **0 mismatches, 0 missing** |
| Observed-bytes manifest digest | sha256 over sorted `path\0sha256(bytes)` rows | `09031570283048595c92f494770f1639f7c2313197ff3f1e1fdd271cf391574c` (constant at all 4 samples) |
| Baseline→HEAD diff, protected surface | `git diff --name-status fc13cd2 HEAD -- reports/round-{8..25}` | empty |
| `git status` over protected surface | `--porcelain=v1 -uall` | empty |
| Ignored paths under protected surface | `git ls-files --others --ignored --exclude-standard` | **12** (below) |
| Lane-wide status | `--porcelain=v1 -uall` | empty at samples 1–2; peer round-26 paths at samples 3–4 (below) |
| Tracked protected paths with mtime > dispatch | `git ls-files -z … \| xargs -0 find -newermt 2026-10-18T17:59:43Z` | **0** |

Per-round tracked counts at baseline (2026-10-18T18:01Z): r8 153, r9 87, r10 73, r11 252, r12 44, r13 2, r14 40, r15 20, r16 23, r17 67, r18 60, r19 71, r20 81, r21 45, r22 77, r23 43, r24 20, r25 67 → **1,225**.

Ignored paths under the protected surface (no committed baseline; observed stable across all samples, sha256 first 16 hex shown from the 18:04Z re-take):

| sha256 (16) | Path |
|---|---|
| `60d2965858c1f25c` | `reports/round-11/handoff/run.log` |
| `3645db7a7d0b8ad6` | `reports/round-11/handoff/tamper-control.log` |
| `fc92dfdd386a3651` | `reports/round-20/handoff/run.log` |
| `32bae9fe627d9834` | `reports/round-22/handoff/declared-in/run.log` |
| `ba68aee78efa6d7a` | `reports/round-22/handoff/declared-in-r2/run.log` |
| `de634c6000d0a4c0` | `reports/round-23/wording/declared-in-r3/run.log` |
| `e67b4d9c9e0624c6` | `reports/round-23/__pycache__/run-validation.cpython-314.pyc` |
| `7e6e8812496b62a5` | `reports/round-24/__pycache__/run-validation.cpython-314.pyc` |
| `8c1503f75e762320` | `reports/round-25/__pycache__/run-validation.cpython-314.pyc` |
| `7c5810479045c26b` | `reports/round-9/baselines/handoff-packet-check/run.log` |
| `e3b0c44298fc1c14` | `reports/round-9/baselines/myth-consistency-gate/run.log` |
| `ebc8850d08ec1b7e` | `reports/round-9/baselines/naming-collision-gate/run.log` |

Round 25 recorded 11 of these; the twelfth, `reports/round-25/__pycache__/run-validation.cpython-314.pyc` (81,921 bytes, mtime 15:01:16−03:00), is a byte-cache produced by executing the **round-25** validator during the round-25/26 handoff. It is ignorable build residue under a `__pycache__/` rule, has no committed baseline, sits outside every tracked path (the tracked-path mtime scan above returns 0), and is stable across the watch. It is not a filed artifact and this seat did not create it.

## Detector control (the audit fires on tampering)

`python3 .scratch/x57/watch.py control` on 2026-10-18T18:01:11Z, target `reports/round-8/claims.json`:

- baseline blob SHA-1 `1902149194b5d44f22288631c17ae28d537b2a7c` **matches** live bytes → `clean_match: true`
- appending `b"\nx57-in-memory-only-probe\n"` **in memory only** → blob SHA-1 differs → `tamper_detected: true`
- live file re-read **byte-identical** → `live_bytes_unchanged: true`

`pass: true`. This controls the *audit detector*, not any round's product. No file was created or altered.

## Closing watch

Read-only, `range(1, 4)` with `time.sleep(60)`; command run **2026-10-18**, exit **0**; samples at **18:01:11Z**, **18:02:11Z**, **18:03:11Z**, **18:04:11Z**.

Held constant at all four samples: mismatches `[]`; missing `[]`; manifest digest `09031570…`; protected status empty; baseline→HEAD diff empty; the 12 ignored paths and their digests; the 10 fleet status rows; fleet HEAD `a4a9796`; lane HEAD `1ad491a`; `tracked` = 1,225.

The **only** channel that moved was lane-wide status, and every delta is a **peer's new round-26** path, never a filed round-8–25 path:

| Sample | Lane-wide status rows |
|---|---|
| initial (18:01:11Z) | empty |
| closing-1 (18:02:11Z) | empty |
| closing-2 (18:03:11Z) | `?? reports/round-26/audit/x60-register-derivation-spotcheck.py` |
| closing-3 (18:04:11Z) | the above plus `?? reports/round-26/audit/x63-lessons-audit.py`, `?? reports/round-26/lessons/r26-census.py` |

These are live writes by the round-26 D/C claimants, all outside the protected filed surface. `watch_consistent` is therefore **false only for `lane_status`**, and true for every protected and fleet channel. The verdict binds the observations above, not later parent integration.

## Fleet-root findings (inherited, unchanged)

Fleet root = `/home/vgpnk/Projects/shokunin`. `git status --porcelain=v1 -uall` returned **10 rows**, all `?? .scratch/*.out`; `git status --porcelain=v1` without `-uall` returns **1** row (`?? .scratch/`). The ten names, contents and mtimes are identical to the round-25 record (2026-10-18 13:10:25−03:00 for `battery.out`, `coupling.out`, `craft.out`, `d2check.out`, `d3check.out`, `replay-r22.out`, `replay-r3.out`; 13:15:49−03:00 for `rv5-p.out`, `rv6-p.out`, `rv7-p.out`). Each is a one-line `python3: can't open file '<path>': [Errno 2] No such file or directory` error from a lane tool invoked at the fleet root; the fleet `.gitignore` does not cover `.scratch/`. **F1: unchanged from round 25 — no new row, none removed.**

The stray `bash: ` tree is also unchanged: 9 filesystem entries (8 directories + 1 file), created **2026-10-18T14:01:47.324772589−03:00**, the file 10,139 bytes, sha256 `3a127f03b9afbfef76d8cfb4274e0cb16aa7d59b915ce19e70a236321e9b3c33` — byte-identical to the round-25 record. Its content is a souji-shokunin round-4 adversarial seat S54 JSON receipt (`"seat": "S54"`, `"round": 4`, `"lane": "souji-shokunin"`), written to a path a mis-quoted command built. **F2: unchanged from round 25.**

### Masking control — why a plain status check would call this root clean

The stray tree is hidden from Git's default untracked view by the fleet ignore rule `*-shokunin/` matching its inner `…/shokunin/souji-shokunin` component (2026-10-18T18:01Z):

```
$ git check-ignore -v 'bash: /home/vgpnk/Projects/shokunin/souji-shokunin'
.gitignore:1:*-shokunin/	bash: /home/vgpnk/Projects/shokunin/souji-shokunin
$ git status --porcelain=v1 -- 'bash: '                 # → 0 rows
$ git status --porcelain=v1 -uall --ignored -- 'bash: ' # → 1 row: !! "bash: …/souji-verify.sh: No such file or directory"
$ find 'bash: ' | wc -l                                 # → 9 entries
```

Two independent blind spots therefore hide it: the `*-shokunin/` ignore rule, and `git status`'s default directory collapsing (`?? .scratch/` instead of the ten leaf files). **Fleet cleanliness must be asserted over the filesystem, not only over Git's untracked view.**

### Fleet-root surface inventory (2026-10-18T18:04Z)

Fleet root holds 15 tracked files, 10 tracked directories, and these untracked/ignored top-level entries. Only the two families above are unexplained debris; `.scratch/` (11 entries: the 10 `.out` files + empty `r23-replay-mirrors/`) and the empty `reports/` directory (`git ls-files reports/` → 0 tracked paths) are lane-external scratch. Fleet HEAD moved once this cycle, at 14:59:08−03:00 (the round-25 close), i.e. before round-26 dispatch.

## Limits and handoff

- Repeated sampling cannot prove no write-and-restore occurred between samples; the manifest digest is a stability anchor, not a historical identity claim.
- Ignored files have no Git baseline; observed stability does not establish their historical identity.
- F1/F2 attribution is by content and mtime only. The `bash: ` receipt's author is inferred from its own `"seat": "S54"` field, not verified. Both families predate round-26 dispatch, so no round-26 seat authored them; F1 also predates round-25 dispatch.
- The fleet-root cleanliness clause **fails as observed**. Disposition of F1 (delete the ten `.out` files or ignore fleet `.scratch/`) and F2 (remove the stray tree; re-file the S54 receipt at its correct souji path) belongs to the parent integrator and the souji-shokunin lane — this seat left every path byte-identical to how it found it.
- No validator was executed here, including historical validators that could rewrite filed receipts. Peer round-26 writes appeared during the watch; this seat neither edited nor certified their content.

## Read-only replay

From the lane root (`export TMPDIR="$PWD/.scratch"` first), this reproduces the protected verdict, the detector control, the ignored-path census and the fleet rows without writing any receipt or executing a historical validator:

```bash
export TMPDIR="$PWD/.scratch"
python3 .scratch/x57/watch.py snapshot   # protected: mismatches must be []
python3 .scratch/x57/watch.py control    # detector control: pass must be true
git diff --name-status fc13cd27b9e78d5d7c4f70740fd26c9383a7447b HEAD -- \
  reports/round-8 reports/round-9 reports/round-10 reports/round-11 reports/round-12 \
  reports/round-13 reports/round-14 reports/round-15 reports/round-16 reports/round-17 \
  reports/round-18 reports/round-19 reports/round-20 reports/round-21 reports/round-22 \
  reports/round-23 reports/round-24 reports/round-25            # must print nothing
cd /home/vgpnk/Projects/shokunin
git status --porcelain=v1 -uall                                 # 10 ?? .scratch/*.out rows
git check-ignore -v 'bash: /home/vgpnk/Projects/shokunin/souji-shokunin'
find 'bash: ' -type f                                           # 1 file, 10,139 bytes
```

Assertions: `snapshot().mismatches == []` and `missing == []`; `control().pass is True`; the baseline→HEAD diff over the protected surface is empty; the fleet status rows equal the ten names listed; `find 'bash: ' -type f` prints exactly the truncated-name file above.

FILES: reports/round-26/scope.md, .scratch/x57/watch.py, .scratch/x57/watchlog.json, .scratch/x57/control.json | SUMMARY: X57 scope watch — filed rounds 8–25 (1,225 tracked paths) byte- and mode-clean against baseline `fc13cd2` across 4 samples with detector control passing; fleet root not clean, carrying the same inherited round-25 debris (10 `?? .scratch/*.out`, stray `bash: ` tree with a 10,139-byte souji receipt) that predates dispatch.
