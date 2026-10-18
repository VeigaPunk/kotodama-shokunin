# Round 27 — Scope watch (SCRIBE X51)

- **Axes:** filed-artifact immutability (rounds 8–26, and the frozen gate generations that go with them); fleet-root cleanliness; bounded, reproducible evidence.
- **Assignment:** scope watch — filed rounds 8–26 untouched, fleet root clean.
- **Date:** 2026-10-18. Timestamps are UTC unless a local `−03:00` form is given.
- **Write scope:** this fragment only. No shared bookkeeping, source fixes, packet/validator/pin edits, historical validator runs, Git mutations, commits, pushes, or sibling writes. `export TMPDIR=$PWD/.scratch` was set before every scratch-writing command; scratch lived in `.scratch/x51/` (gitignored, lane-internal). No filed rounds 8–26 byte was written by this seat.

## Verdict (scoped to this seat's observations)

**PASS for the filed-round surface; NOT CLEAN for the fleet root.**

- **Filed rounds 8–26 + frozen generations: PASS.** At the initial sample and all three closing-watch samples of both runs, all **1,460** tracked paths under `reports/round-{8..26}` **plus** `tools/gates/frozen/round-{8..26}` matched the declared baseline `4f09c990d4c17f23b5e2cda0871f81db875635fc` in Git blob identity **and** executable/symlink mode — **0 mismatches, 0 missing**. `git diff --name-status <baseline> HEAD -- <protected>` is empty, `git status` over that surface is empty, and no tracked path under the surface has an mtime later than round-27 dispatch. No round-27 seat write to a filed round-8–26 path was observed.
- **Fleet root: NOT CLEAN — and it drifted this cycle.** The two debris families the round-25/26 watches disclosed (F1 ten `?? .scratch/*.out` files; F2 a stray `bash: ` directory tree holding a 10,139-byte souji-shokunin receipt) are both still present, byte-identical and mtime-identical. **Two further families are new since round 26** — F3 `.scratch/goal-20261018-game-dev-2d-training.md` and F4 a modified `.ufo/l0-questions.md`. All four predate round-27 dispatch, so no round-27 seat authored them; they are host-level activity, disclosed here, not dispositioned. The assignment's "fleet root clean" clause therefore **fails as observed**.

This is a scoped observation at the recorded times, not round acceptance and not a claim that no transient write ever occurred.

## Baseline binding

- Declared baseline `reports/round-27/claims.json:5` = `4f09c990d4c17f23b5e2cda0871f81db875635fc` ("round-26: admit D/O/C — register stratum closes the r17 forecast; r5 pin chain (devin)", commit time 2026-10-18T16:10:02−03:00).
- Lane HEAD at watch = `b95fca1e40f32f7346937ab6426f9ccca60e319f` ("round-27: declare claims D/O/C (register law, pin sweep, register knowledge)", 16:11:04−03:00 = 19:11:04Z). `git merge-base --is-ancestor 4f09c99 HEAD` → success (2026-10-18T19:12Z). **Round-27 dispatch instant = 19:11:04Z**, used as the mtime cut-off below.
- `git show --stat HEAD` (2026-10-18T19:12Z) shows the declaration commit adds exactly two paths — `reports/round-27/claims.json` (`blob 96db04f35d7f48849d669d4834eb9889c9154f37`) and `reports/round-27/targets.json` (`blob cfb4a778c8a2219639eea1dfb2fd5acc2fd767a3`) — 44 insertions, and no filed round-8–26 path and no frozen path.
- Fleet HEAD = `f4e1e9bf6e270bdfbd9166ee38f8d84e481aabc7` ("close kotodama round-26: admitted (register stratum; r17 forecast closed)", 16:10:31−03:00), unchanged across all samples.

## Protected surface — what it actually is

The round-26 runner's own `PROTECTED` (`reports/round-26/run-validation.py:119`) is `reports/round-{8..25}` **plus** `tools/gates/frozen/round-{8..25}`; its filed receipt measures **1,328** protected paths (`reports/round-26/validation.json` → `protected_filed_artifacts.measurement.protected_paths`). Round 27's landing adds a round, so this seat's surface is **`reports/round-{8..26}` + `tools/gates/frozen/round-{8..26}` = 1,460 tracked paths**, which strictly supersedes the 1,328 figure. The reports-only subset is **1,325** paths. (All 237 tracked paths under `tools/gates/frozen` were also checked for diff/status/mtime; only the 135 round-tagged ones are inside the round-indexed surface.)

Per-round tracked counts at baseline (2026-10-18T19:12Z), command `git ls-tree -r <baseline> -- reports/round-<n>`:

| round | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reports paths | 153 | 87 | 73 | 252 | 44 | 2 | 40 | 20 | 23 | 67 | 60 | 71 | 81 | 45 | 77 | 43 | 20 | 67 | 100 |
| frozen paths | – | – | – | 18 | – | – | – | – | – | – | 12 | – | 5 | – | 39 | 15 | – | 14 | 32 |

Reports subtotal **1,325**; frozen round-tagged subtotal **135**; surface **1,460**.

## Protected-surface evidence (command + date on each)

All commands run **2026-10-18** from the lane root with `export TMPDIR="$PWD/.scratch"`; script `.scratch/x51/watch.py`, transcripts `.scratch/x51/watchlog.json` (reports-only run), `.scratch/x51/watchlog-ext.json` (extended run), `.scratch/x51/control.json`.

| Measurement | Command | Result |
|---|---|---|
| Tracked protected paths | `git ls-tree -r <baseline> -- reports/round-{8..26} tools/gates/frozen/round-{8..26}` | **1,460** |
| Blob SHA-1 + mode comparison vs working bytes | `python3 -B .scratch/x51/watch.py snapshot 3` | **0 mismatches, 0 missing** at all 4 samples of each run |
| Observed-bytes manifest digest | sha256 over sorted `path\0sha256(bytes)` rows | reports-only `f938a1ba2108…`; extended `0ecd290a9b8c…` — constant at all 8 samples |
| Baseline→HEAD diff, protected surface | `git diff --name-status <baseline> HEAD -- <protected>` | empty |
| `git status` over protected surface | `--porcelain=v1 -uall` | empty |
| Ignored paths under protected surface | `git ls-files --others --ignored --exclude-standard -- <protected>` | **18** (reports-only) / **21** (extended) — below |
| Tracked protected paths with mtime > dispatch | mtime scan vs `2026-10-18T19:11:04Z` | **0** (also 0 across all 2,196 lane tracked paths) |
| Lane-wide status | `--porcelain=v1 -uall` | 0 rows at sample 1, then peer round-27 paths (below) |
| Fleet status | `--porcelain=v1 -uall` in `/home/vgpnk/Projects/shokunin` | **12 rows**, constant at all 8 samples |

Ignored paths under the protected surface (no committed baseline; observed stable across all samples; sha256 first 16 hex from the 19:16Z re-take). Round 26 recorded 12 on the reports-only surface; round 27 observes **18** there — the six additions are all round-26 landing residue, not round-27 writes:

| sha256 (16) | Size | Path |
|---|---|---|
| `60d2965858c1f25c` | 472 | `reports/round-11/handoff/run.log` |
| `3645db7a7d0b8ad6` | 2983 | `reports/round-11/handoff/tamper-control.log` |
| `fc92dfdd386a3651` | 1601 | `reports/round-20/handoff/run.log` |
| `32bae9fe627d9834` | 1603 | `reports/round-22/handoff/declared-in/run.log` |
| `ba68aee78efa6d7a` | 1603 | `reports/round-22/handoff/declared-in-r2/run.log` |
| `e67b4d9c9e0624c6` | 85299 | `reports/round-23/__pycache__/run-validation.cpython-314.pyc` |
| `de634c6000d0a4c0` | 2349 | `reports/round-23/wording/declared-in-r3/run.log` |
| `7e6e8812496b62a5` | 94714 | `reports/round-24/__pycache__/run-validation.cpython-314.pyc` |
| `8c1503f75e762320` | 81921 | `reports/round-25/__pycache__/run-validation.cpython-314.pyc` |
| `2bc695721e54b3e8` | 46366 | `reports/round-25/v3-supersession/__pycache__/v3-supersession-check.cpython-314.pyc` |
| `ddfdba2dff36d775` | 125947 | `reports/round-26/__pycache__/run-validation.cpython-314.pyc` |
| `43fded40f2da5a67` | 1603 | `reports/round-26/handoff/declared-in-r5/run.log` |
| `a69547a76d2bc9d3` | 24163 | `reports/round-26/lessons/__pycache__/c51-revision-audit.cpython-314.pyc` |
| `373ce32b0b53d825` | 1603 | `reports/round-26/register/v3-baseline-r26/run.log` |
| `ba68aee78efa6d7a` | 1603 | `reports/round-26/remainders/v3-baseline-r26/run.log` |
| `7c5810479045c26b` | 55 | `reports/round-9/baselines/handoff-packet-check/run.log` |
| `e3b0c44298fc1c14` | 0 | `reports/round-9/baselines/myth-consistency-gate/run.log` |
| `ebc8850d08ec1b7e` | 3927 | `reports/round-9/baselines/naming-collision-gate/run.log` |
| `9a69985aabdf3e9b` | 2604 | `tools/gates/frozen/round-11/typed-pipeline/run.log` |
| `9a69985aabdf3e9b` | 2604 | `tools/gates/frozen/round-18/repin-d2/typed-pipeline/run.log` |
| `9a69985aabdf3e9b` | 2604 | `tools/gates/frozen/round-20/repin-d2/typed-pipeline/run.log` |

Note the shared digests: the two round-26 `v3-baseline-r26/run.log` files are byte-identical to each other and to `reports/round-22/handoff/declared-in-r2/run.log`, and the three `typed-pipeline/run.log` files are byte-identical — consistent with copies, not independent runs. Every one of these is ignorable build/run residue under an `*.log` or `__pycache__/` rule, has no committed baseline, and sits outside every tracked path (the tracked-path mtime scan returns 0). None is a filed artifact and this seat did not create any.

## Detector control (the audit fires on tampering)

`python3 -B .scratch/x51/watch.py control` on 2026-10-18T19:12Z, two targets:

- `reports/round-8/claims.json` — baseline blob SHA-1 `1902149194b5d44f22288631c17ae28d537b2a7c` **matches** live bytes → `clean_match: true`; appending `b"\nx51-in-memory-only-probe\n"` **in memory only** → blob SHA-1 differs → `tamper_detected: true`; live file re-read **byte-identical** → `live_bytes_unchanged: true`.
- `reports/round-26/claims.json` (the newest filed round, and the one whose declaration this round builds on) — baseline blob `3ffa3c0aa0fd3a029f3b6eeeb86452f2f9ba8de1` **matches** → `clean_match2: true`; in-memory probe detected → `tamper_detected2: true`; live bytes unchanged → `live_bytes_unchanged2: true`.

`pass: true`. This controls the *audit detector*, not any round's product. No file was created or altered. The round-26 target matters because a watch that only ever probes round 8 cannot show that the newly-frozen round is inside the same comparison.

## Closing watch

Read-only, `range(1, 4)` with `time.sleep(60)`; two runs, each **2026-10-18**, exit **0**.

- Reports-only run (rounds 8–26): samples at **19:12:16Z**, **19:13:16Z**, **19:14:16Z**, **19:15:16Z**.
- Extended run (rounds 8–26 + frozen): samples at **19:13:06Z**, **19:14:06Z**, **19:15:06Z**, **19:16:06Z**.

Held constant at all samples of both runs: mismatches `[]`; missing `[]`; manifest digest (`f938a1ba2108…` / `0ecd290a9b8c…`); protected status empty; baseline→HEAD diff empty; `tracked_newer_than_dispatch` `[]`; the 18/21 ignored paths and their digests; the 12 fleet status rows; fleet HEAD `f4e1e9b`; lane HEAD `b95fca1`; `protected_tracked_paths` 1,325 / 1,460.

The **only** channel that moved was lane-wide status, and every delta is a **peer's new round-27** path, never a filed round-8–26 path:

| Sample | Lane-wide status rows (extended run) |
|---|---|
| initial (19:13:06Z) | `?? reports/round-27/scribe/x56-census.py` |
| closing-1 (19:14:06Z) | the above plus `?? reports/round-27/audit/entry-audit.py`, `?? reports/round-27/readme/sweep.py` |
| closing-2 (19:15:06Z) | the above plus `?? reports/round-27/audit/x57-lessons-audit.py`, `?? reports/round-27/audit/x59-register-law-negatives.py`, `?? reports/round-27/audit/x61-pin-sweep.py`, `?? reports/round-27/audit/x63-entry-source-resolvability.py` |
| closing-3 (19:16:06Z) | the above plus `?? reports/round-27/audit/x57-lessons-receipt.json`, `?? reports/round-27/audit/x57-lessons-selftest.json`, `?? reports/round-27/audit/x64-cold-rerun.py` |

These are live writes by the round-27 D/O/C claimants, all outside the protected filed surface and all under `reports/round-27/`. `watch_consistent` is therefore **false only for `lane_status`**, and true for every protected and fleet channel. The verdict binds the observations above, not later parent integration.

## Fleet-root findings

Fleet root = `/home/vgpnk/Projects/shokunin`. Surface inventory (2026-10-18T19:16Z): **2,909** tracked files, **15** tracked top-level files, **6** tracked top-level directories (`.devin`, `.omp`, `research`, `scripts`, `templates`, `.ufo`). `git status --porcelain=v1 -uall` returns **12 rows**; without `-uall` it returns **2** (`M .ufo/l0-questions.md`, `?? .scratch/`). Fleet HEAD moved once this cycle, at 16:10:31−03:00 (the round-26 close), i.e. before round-27 dispatch.

### F1 — ten `?? .scratch/*.out` (inherited, unchanged)

All ten present, byte-identical and mtime-identical to the round-25 and round-26 records: `battery.out`, `coupling.out`, `craft.out`, `d2check.out`, `d3check.out`, `replay-r22.out`, `replay-r3.out` (all 2026-10-18 13:10:25−03:00); `rv5-p.out`, `rv6-p.out`, `rv7-p.out` (all 13:15:49−03:00). Each is a one-line `python3: can't open file '<path>': [Errno 2] No such file or directory` error from a lane tool invoked at the fleet root (seven name `/home/vgpnk/Projects/shokunin/tools/...`; three name `/tmp/coldrun-b/export2/reports/round-{5,6,7}/run-validation.py`). The fleet `.gitignore` does not cover `.scratch/`. **F1: unchanged from round 26 — no new row, none removed.**

### F2 — the stray `bash: ` tree (inherited, unchanged)

9 filesystem entries (8 directories + 1 file); the file `bash: /home/vgpnk/Projects/shokunin/souji-shokunin/tests/tools/souji-verify.sh: No such file or directory`, 10,139 bytes, sha256 `3a127f03b9afbfef76d8cfb4274e0cb16aa7d59b915ce19e70a236321e9b3c33`, created **2026-10-18T14:01:47.324772589−03:00** — byte-identical to the round-25/26 record. Its content is a souji-shokunin round-4 adversarial seat S54 JSON receipt (`"seat": "S54"`, `"round": 4`, `"lane": "souji-shokunin"`), written to a path a mis-quoted command built. **F2: unchanged from round 26.**

### F3 — NEW this cycle: `.scratch/goal-20261018-game-dev-2d-training.md`

6,543 bytes, sha256 `e56e047b619b8c5da2ce77dd3a79b39bc19930e9ecb8a071e1212f2f90c71bb0`, mtime **2026-10-18T16:00:35−03:00** (= 19:00:35Z), i.e. **~10 min before round-27 dispatch**. Header reads "Goal — game-dev-2d-shokunin training loop (39 rounds) + 3D Epic re-vendoring side-round … Created 2026-10-18 by write-goal flow with the operator." It is a host-level goal contract, not a kotodama artifact, and it is the **only new member of the fleet `.scratch/` family** since round 26. It is lane-external scratch: it is neither explained debris nor a kotodama write, and it is not dispositioned here.

### F4 — NEW this cycle: modified `.ufo/l0-questions.md`

Tracked file at fleet HEAD, now **modified in the working tree**: `git diff --stat` → `1 file changed, 1 insertion(+)`; blob `b671b8af6ff5d9c4f6b5c3b1913985c09e3b5ed7` (HEAD) → live sha256 `a64fe9c9708adb30006784f5bb6aa45d33ec9eaf615e52fa4e32d3c40d476a5c`, mtime **2026-10-18T15:40:17−03:00** (= 18:40:17Z), i.e. **~31 min before round-27 dispatch**. The added line is a **kama** round-8 open question ("wire id `opencode-go/glm-5.3-flash-free` is NOT in this host dispatch catalog …"). Round 26's watch recorded fleet status as 10 rows, all untracked; this **tracked-file modification is new**. It is a peer lane's open-question append, not a kotodama write.

### Masking control — why a plain status check would call this root clean

The stray tree is hidden from Git's default untracked view by the fleet ignore rule `*-shokunin/` matching its inner `…/shokunin/souji-shokunin` component (2026-10-18T19:16Z):

```
$ git check-ignore -v 'bash: /home/vgpnk/Projects/shokunin/souji-shokunin'
.gitignore:1:*-shokunin/	bash: /home/vgpnk/Projects/shokunin/souji-shokunin
$ git status --porcelain=v1 -- 'bash: '                 # → 0 rows
$ git status --porcelain=v1 -uall --ignored -- 'bash: ' # → 1 row: !! "bash: …/souji-verify.sh: No such file or directory"
$ find 'bash: ' | wc -l                                 # → 9 entries
```

Two independent blind spots therefore hide it: the `*-shokunin/` ignore rule, and `git status`'s default directory collapsing (`?? .scratch/` instead of the ten leaf files). The same collapsing is what reduces the 12-row fleet reading to 2 rows without `-uall`. **Fleet cleanliness must be asserted over the filesystem, not only over Git's untracked view.** The remaining ignored top-level families are `.tower/comms` (96 rows), `.ufo/waves` (36), and the fourteen `*-shokunin/` lane directories — all expected by the fleet ignore rules.

## Limits and handoff

- Repeated sampling cannot prove no write-and-restore occurred between samples; the manifest digest is a stability anchor, not a historical identity claim.
- Ignored files have no Git baseline; observed stability does not establish their historical identity.
- F1/F2 attribution is by content and mtime only. The `bash: ` receipt's author is inferred from its own `"seat": "S54"` field, not verified. F1/F2 predate round-26 dispatch, so no round-26 or round-27 seat authored them; F1 also predates round-25 dispatch. F3 and F4 both **predate round-27 dispatch by minutes**, so no round-27 seat authored them either; F4's author is inferred from the appended line's own `kama` prefix.
- The fleet-root cleanliness clause **fails as observed**. Disposition of F1 (delete the ten `.out` files or ignore fleet `.scratch/`) and F2 (remove the stray tree; re-file the S54 receipt at its correct souji path) belongs to the parent integrator and the souji-shokunin lane; F3 is host-goal machinery the parent should leave alone or relocate; F4 is a peer lane's pending open-question edit for its own lane to commit. This seat left every path byte-identical to how it found it.
- The protected surface here is **1,460** paths, wider than the 1,325 the assignment's "filed rounds 8–26" phrasing implies and wider than the 1,328 the round-26 receipt measures, because it includes the frozen gate generations. The parent should adopt one figure; this seat recommends the 1,460 form, since a frozen gate generation is as filed as the report beside it.
- No validator was executed here, including historical validators that could rewrite filed receipts. Peer round-27 writes appeared during the watch; this seat neither edited nor certified their content.

## Read-only replay

From the lane root (`export TMPDIR="$PWD/.scratch"` first), this reproduces the protected verdict, the detector control, the ignored-path census and the fleet rows without writing any receipt or executing a historical validator:

```bash
export TMPDIR="$PWD/.scratch"
python3 -B .scratch/x51/watch.py snapshot 0   # protected: mismatches must be []
python3 -B .scratch/x51/watch.py control      # detector control: pass must be true
git diff --name-status 4f09c990d4c17f23b5e2cda0871f81db875635fc HEAD -- \
  reports/round-8 reports/round-9 reports/round-10 reports/round-11 reports/round-12 \
  reports/round-13 reports/round-14 reports/round-15 reports/round-16 reports/round-17 \
  reports/round-18 reports/round-19 reports/round-20 reports/round-21 reports/round-22 \
  reports/round-23 reports/round-24 reports/round-25 reports/round-26 \
  tools/gates/frozen/round-8 tools/gates/frozen/round-9 tools/gates/frozen/round-10 \
  tools/gates/frozen/round-11 tools/gates/frozen/round-12 tools/gates/frozen/round-13 \
  tools/gates/frozen/round-14 tools/gates/frozen/round-15 tools/gates/frozen/round-16 \
  tools/gates/frozen/round-17 tools/gates/frozen/round-18 tools/gates/frozen/round-19 \
  tools/gates/frozen/round-20 tools/gates/frozen/round-21 tools/gates/frozen/round-22 \
  tools/gates/frozen/round-23 tools/gates/frozen/round-24 tools/gates/frozen/round-25 \
  tools/gates/frozen/round-26            # must print nothing
cd /home/vgpnk/Projects/shokunin
git status --porcelain=v1 -uall         # 12 rows: 1 M .ufo/l0-questions.md, 11 ?? .scratch/*
git check-ignore -v 'bash: /home/vgpnk/Projects/shokunin/souji-shokunin'
find 'bash: ' -type f                   # 1 file, 10,139 bytes
sha256sum .scratch/goal-20261018-game-dev-2d-training.md   # e56e047b…, 6,543 B
```

Assertions: `snapshot().mismatches == []`, `missing == []`, `tracked_newer_than_dispatch == []`, `protected_tracked_paths == 1460`; `control().pass is True`; the baseline→HEAD diff over the protected surface is empty; the fleet status rows are the twelve listed at the 19:16Z sample (the fleet reading is a live snapshot and will grow as peer lanes write); `find 'bash: ' -type f` prints exactly the truncated-name file above.

FILES: reports/round-27/scope.md, .scratch/x51/watch.py, .scratch/x51/watchlog.json, .scratch/x51/watchlog-ext.json, .scratch/x51/control.json | SUMMARY: X51 scope watch — filed rounds 8–26 plus frozen gate generations (1,460 tracked paths) byte- and mode-clean against baseline `4f09c99` across 8 samples with a two-target detector control passing; fleet root not clean, carrying the inherited round-25/26 debris (10 `?? .scratch/*.out`, stray `bash: ` tree with a 10,139-byte souji receipt) plus two new pre-dispatch families (F3 `.scratch/goal-20261018-game-dev-2d-training.md`, F4 modified `.ufo/l0-questions.md`).
