# Round 28 — Scope watch (SCRIBE X51)

- **Axes:** filed-artifact immutability (rounds 8–27, and the frozen gate generations that go with them); fleet-root cleanliness; bounded, reproducible evidence.
- **Assignment:** scope watch — filed rounds 8–27 untouched, fleet root clean.
- **Date:** 2026-10-18. Timestamps are UTC unless a local `−03:00` form is given.
- **Write scope:** this fragment only. No shared bookkeeping, source fixes, packet/validator/pin edits, historical validator runs, Git mutations, commits, or pushes. `export TMPDIR=$PWD/.scratch` was set before every scratch-writing command; scratch lived in `.scratch/x51/` (gitignored, lane-internal). No filed round-8–27 byte was written by this seat.

## Verdict (scoped to this seat's observations)

**FAIL for the filed-round surface; NOT CLEAN for the fleet root.**

- **Filed rounds 8–27 + frozen generations: FAIL as observed.** At the initial sample of both runs all **1,587** tracked paths under `reports/round-{8..27}` **plus** `tools/gates/frozen/round-{8..27}` matched the declared baseline `6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede` in Git blob identity **and** executable/symlink mode (**0 mismatches, 0 missing**). **One protected path then moved inside the watch window:** `reports/round-27/gate-tests/receipt.json`, a **filed round-27 artifact**, was rewritten in place at **20:13:21Z** and restored by **20:14:42Z**. Details in "The breach" below. Every other protected path held at all eight samples. **At the end of the window the bytes are baseline-identical but the path still carries a post-dispatch mtime (20:14:42Z) from the restore itself** — the residual trace of the breach, and the reason a settled tree still reads one row on the mtime channel.
- **Fleet root: NOT CLEAN, and it moved inside this window.** The four families the round-25/26/27 watches disclosed are all still present; F1 (ten `?? .scratch/*.out`), F2 (the stray `bash: ` tree) and F3 (`.scratch/goal-20261018-game-dev-2d-training.md`) are byte- and mtime-identical to the round-27 record. **F4 (`.ufo/l0-questions.md`) grew inside the round-28 window** — a second appended line, mtime **20:14:10Z**, i.e. after round-28 dispatch. The assignment's "fleet root clean" clause therefore **fails as observed**.

This is a scoped observation at the recorded times, not round acceptance and not a claim that no other transient write occurred between samples.

## Baseline binding

- Declared baseline `reports/round-28/claims.json:5` = `6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede` ("round-27: admit D/O/C — register law, syllabify fix, pin sweep, register entry (devin)", commit time 2026-10-18T17:09:19−03:00).
- Lane HEAD at watch = `69cecbc7dcf575a29f29660ecac470e05260fd86` ("round-28: declare claims D/O/C (law replay leg, packet_keys fix + sweep, ceiling knowledge)", 17:10:20−03:00 = 20:10:20Z). `git merge-base --is-ancestor 6c0ac44 HEAD` → success (2026-10-18T20:11Z). **Round-28 dispatch instant = 20:10:20Z**, used as the mtime cut-off below.
- `git show --stat HEAD` (2026-10-18T20:11Z) shows the declaration commit adds exactly two paths — `reports/round-28/claims.json` (`blob bfed39f1b4841c53f53b0f562b0b6b41b132012e`) and `reports/round-28/targets.json` (`blob 302b4184ec16d01f11efb4a31aa9d06b3cef0c70`) — 44 insertions, and no filed round-8–27 path and no frozen path.
- Fleet HEAD = `cdd444d3063db314ce0ca11154b5f3285c92b2df` ("close kotodama round-27: admitted (register law + pin sweep)", 17:09:48−03:00), unchanged across all eight samples.

## Protected surface — what it actually is

The round-28 runner's own `PROTECTED` (`reports/round-28/run-validation.py:119`) is `reports/round-{8..27}` **plus** `tools/gates/frozen/round-{8..27}`; its filed receipt measures **1,587** protected paths (`reports/round-28/validation.json` → `protected_filed_artifacts.measurement.protected_paths.value`), the same figure this seat measures independently. Round 27's landing added a round, so this seat's surface is **`reports/round-{8..27}` + `tools/gates/frozen/round-{8..27}` = 1,587 tracked paths**, up from round 27's 1,460. The reports-only subset is **1,452** paths. (All 237 tracked paths under `tools/gates/frozen` were also checked for diff/status/mtime; only the 135 round-tagged ones are inside the round-indexed surface.)

Per-round tracked counts at baseline (2026-10-18T20:11Z), command `git ls-tree -r <baseline> -- reports/round-<n>` / `-- tools/gates/frozen/round-<n>`:

| round | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reports paths | 153 | 87 | 73 | 252 | 44 | 2 | 40 | 20 | 23 | 67 | 60 | 71 | 81 | 45 | 77 | 43 | 20 | 67 | 100 | 127 |
| frozen paths | – | – | – | 18 | – | – | – | – | – | – | 12 | – | 5 | – | 39 | 15 | – | 14 | 32 | – |

Reports subtotal **1,452**; frozen round-tagged subtotal **135**; surface **1,587**.

## Protected-surface evidence (command + date on each)

All commands run **2026-10-18** from the lane root with `export TMPDIR="$PWD/.scratch"`; script `.scratch/x51/watch28.py`, transcripts `.scratch/x51/watchlog28.json` (run A), `.scratch/x51/watchlog28-ext.json` (run B), `.scratch/x51/control28.json`.

| Measurement | Command | Result |
|---|---|---|
| Tracked protected paths | `git ls-tree -r <baseline> -- reports/round-{8..27} tools/gates/frozen/round-{8..27}` | **1,587** |
| Blob SHA-1 + mode comparison vs working bytes | `python3 -B .scratch/x51/watch28.py snapshot 3` | **0 mismatches** at samples 1–2 of both runs; **1 mismatch** at samples 3–4 (`receipt.json`, below) |
| Observed-bytes manifest digest | sha256 over sorted `path\0sha256(bytes)` rows | `3d97dbc87faa…` at samples 1–2, `e03e699ce9ce…` at samples 3–4 (the receipt) |
| Baseline→HEAD diff, protected surface | `git diff --name-status <baseline> HEAD -- <protected>` | empty |
| `git status` over protected surface | `--porcelain=v1 -uall` | empty at samples 1–2; `M reports/round-27/gate-tests/receipt.json` at samples 3–4; empty again at 20:17:57Z |
| Ignored paths under protected surface | `git ls-files --others --ignored --exclude-standard -- <protected>` | **28** (extended) / **25** (reports-only) — constant at all 8 samples, below |
| Tracked protected paths with mtime > dispatch | mtime scan vs `2026-10-18T20:10:20Z` | **0** at samples 1–2; **1** (`receipt.json`, mtime 20:13:21Z) at samples 3–4; **1** (same path, mtime 20:14:42Z from the restore) at 20:19Z |
| Lane-wide tracked mtime scan | mtime scan over all 2,326 lane tracked paths | **0** newer than dispatch at 20:12Z; **8** at 20:19Z, all peer round-28 writes (`corpus/README.md`, four `examples/culture-d4/*`, `tools/exercise-handoff-e2e.py`) plus the restored `receipt.json` |
| Lane-wide status | `--porcelain=v1 -uall` | 0 rows at run A sample 1, then peer round-28 paths only (below) |
| Fleet status | `--porcelain=v1 -uall` in `/home/vgpnk/Projects/shokunin` | **12 rows**, constant at all 8 samples |

Ignored paths under the protected surface (no committed baseline; observed stable across all samples; sha256 first 16 hex from the 20:11Z take). Round 27 recorded 18 on the reports-only surface; round 28 observes **25** there — the seven additions are all round-27 landing residue, not round-28 writes:

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
| `2437745fd4a4bc2f` | 31423 | `reports/round-27/audit/__pycache__/entry-audit.cpython-314.pyc` |
| `9b2380b89fc25410` | 41229 | `reports/round-27/audit/__pycache__/x61-pin-sweep.cpython-314.pyc` |
| `61116a8d0e7f8128` | 40760 | `reports/round-27/audit/__pycache__/x62-frozen-record-audit.cpython-314.pyc` |
| `aae2447c1f28cb9e` | 28935 | `reports/round-27/audit/__pycache__/x64-cold-rerun.cpython-314.pyc` |
| `c60820a54742ecaa` | 73 | `reports/round-27/pinsweep/baselines/d4-assembly-check-gate/r27-post/run.log` |
| `1c8add321259a9f0` | 81 | `reports/round-27/pinsweep/baselines/d4-typed-labels-check-gate/r27-post/run.log` |
| `24835272c1d2313c` | 1603 | `reports/round-27/pinsweep/v3-baseline-r27/run.log` |
| `7c5810479045c26b` | 55 | `reports/round-9/baselines/handoff-packet-check/run.log` |
| `e3b0c44298fc1c14` | 0 | `reports/round-9/baselines/myth-consistency-gate/run.log` |
| `ebc8850d08ec1b7e` | 3927 | `reports/round-9/baselines/naming-collision-gate/run.log` |
| `9a69985aabdf3e9b` | 2604 | `tools/gates/frozen/round-11/typed-pipeline/run.log` |
| `9a69985aabdf3e9b` | 2604 | `tools/gates/frozen/round-18/repin-d2/typed-pipeline/run.log` |
| `9a69985aabdf3e9b` | 2604 | `tools/gates/frozen/round-20/repin-d2/typed-pipeline/run.log` |

Note the shared digests: the two round-26 `v3-baseline-r26/run.log` files are byte-identical to each other and to `reports/round-22/handoff/declared-in-r2/run.log`, and the three `typed-pipeline/run.log` files are byte-identical — consistent with copies, not independent runs. Every one of these is ignorable build/run residue under an `*.log` or `__pycache__/` rule, has no committed baseline, and sits outside every tracked path (the tracked-path mtime scan returns 0). None is a filed artifact and this seat did not create any.

## The breach — a filed round-27 artifact rewritten in place

This is the round's scope finding. It is **not** attributable to this seat and this seat asserts no disposition.

**Measured by this seat (watch runs A and B, both).** At samples 3 and 4 of each run, the protected comparison returned exactly one row:

```
{"path": "reports/round-27/gate-tests/receipt.json",
 "baseline_mode": "100644", "live_mode": "100644",
 "baseline_sha": "854ed1a37805a7f848ca2d17e8f005a34788b592",
 "live_sha":    "0727b1058416aa325a72d10d8ec41e60c40ba5d9"}
```

with `tracked_newer_than_dispatch` = `{"path": "reports/round-27/gate-tests/receipt.json", "mtime_utc": "2026-10-18T20:13:21Z"}` and `protected_status` = `M reports/round-27/gate-tests/receipt.json`. Present at **20:13:22Z** (run A) and **20:13:27Z** (run B); still present at 20:14:22Z / 20:14:27Z. Absent at 20:11:2xZ and 20:12:2xZ.

**The transient content** (read at 20:13:5xZ, 27,117 bytes, `date` field `2026-10-18T20:13:19Z`): the same 9 run labels as the filed receipt, but the two typed legs had gone red — `d4-typed` and `d4-source` each `exit: 2`, `legs: 2`, `failed_legs: ["FAIL L1-profile: packet: pins 86079a6708a0, live 543d68a82640 (examples/culture-d4/packet.d4.yml)"]`, `hold_lines: 0`. Every other run stayed at `exit: 0`.

**The mechanism (the actual defect).** `reports/round-27/gate-tests/run-gate-tests.py:820-821` writes `HERE / "receipt.json"` **unconditionally** on every invocation that is not `--selftest`:

```
    receipt_path = HERE / "receipt.json"
    receipt_path.write_text(json.dumps(receipt, indent=1, sort_keys=False) + "\n", ...)
```

`--check` is declared (`:770`, help "measure only, print") but **never consulted** — `grep -n "args\.check" reports/round-27/gate-tests/run-gate-tests.py` returns nothing, and `main()`'s only branch is `if args.selftest: return selftest()`. So the round-27 battery is a **self-overwriting filed receipt**: running it to *read* the round-27 verdicts rewrites the round-27 verdicts. A caller that passes `--check` believing it is safe gets the same in-place write.

The round-28 regression driver (`.scratch/r28-o33-o36-regression/sweep.py:229`, seat O33..O36) invokes it with `--check` **inside an isolated clone** (`sweep.py:260`, `cwd=clone`), so that call cannot reach the lane's filed byte. **No filed round-28 tool invokes the round-27 battery** — `grep -rln "round-27/gate-tests" reports/round-28/` returns only prose files (`adjacency.md`, `scope.md`, the three audit `.md`s, `validation.json`) plus the round-28 gate-tests runner, which *reads* `reports/round-27/gate-tests/fixtures/` and never executes the round-27 battery. So the write that breached the surface was an **unshipped, scratch-mediated invocation made directly in the lane worktree**, not a filed tool's leg.

**The restore.** At 2026-10-18T20:14:42Z the path is byte-identical to the baseline again: live git-blob SHA-1 `854ed1a37805a7f848ca2d17e8f005a34788b592`, 24,950 bytes, sha256 `bdb8d31c1cdf503e598bdcd55fdfb756b6dd8c12b0f50ff2acfafd7fa9883e28`; `git status` over the path is empty and `git diff <baseline> HEAD -- <path>` is empty. The **committed** blob never moved (`git rev-parse <baseline>:<path>` = `git rev-parse HEAD:<path>` = `854ed1a3…`).

**Independent corroboration — four other instruments, same round.** This seat is the fifth to observe the breach, not the first.

- `reports/round-28/adjacency.md` (peer, at **20:13:08Z**): committed blob `bdb8d31c…` (sha256) vs worktree `71e3f455…`, mtime **20:12:33Z**, restore verified at 20:15:06Z. That seat's verdict-identical control — stripping `date`/`head`/`copy` from both revisions and comparing the remainder as canonical JSON — returned `True`, and the only non-`date` changed rows were `head` (`b95fca1e…` → `69cecbc7…`) and `copy` (a scratch path). So **no verdict, exit code, finding id or command changed**: the breach was one of *form* (a filed byte moved in place), not of measured content. The `71e3f455…` revision is itself still on disk at `.scratch/x55/replay/reports/round-27/gate-tests/receipt.json` (24,949 bytes, `date` `2026-10-18T20:12:29Z`, `head` `69cecbc7…`, all 9 runs `exit 0`).

- `reports/round-28/audit/x60-sweep-completeness.md` (**X60-F5**, seat X60): "a filed round-27 artifact was rewritten in place during round 28 … moved from green (exit 0, legs 17/20) to red (exit 2, legs 2) at 20:13:19Z — after the 20:10Z round-28 dispatch — then was restored to its baseline bytes", and it names the same mechanism this seat found (`run-gate-tests.py:820` writes `HERE/receipt.json`).
- `reports/round-28/audit/x62-frozen-record-audit.md` (**X62R28-A3**, seat X62): "caught `reports/round-27/gate-tests/receipt.json` … was rewritten in place mid-wave and is restored at this stamp; the same event is in the round's own validator", with `git hash-object` on both sides giving `854ed1a3…`.
- `reports/round-28/audit/x61-pin-sweep.md:187` (seat X61) records the same path as a stale reading (the receipt stamped `20:04:10Z` when the packet moved).

So the breach was caught by **five** independent instruments in this round (this seat's watch, adjacency, X60, X61, X62) plus the round-28 runner's own protected check — an unusually well-corroborated finding, and one that no single seat's timing happened to miss.

**Third-party instrument reading.** `reports/round-28/run-validation.py` caught the same path with its own comparison: at `measured_at_utc` **20:17:26Z** its `protected_filed_artifacts` block read `passed: false`, `differences_total.value: 1`, `differences: [{"path": "reports/round-27/gate-tests/receipt.json", "baseline_blob": "854ed1a3…", "observed_blob": "fbc1f4b6c0fa1edbbde738cd7f801575079b881a14f25a1b94e684a35fd5a8f0"}]` — a **third** transient revision, not recoverable from this seat's copies. Re-run at `measured_at_utc` 20:17:33Z, the same block reads `passed: true`, `differences_total.value: 0`. So three distinct transient revisions were observed across instruments (this seat 20:13:21Z, the adjacency seat 20:12:33Z, the round-28 runner ~20:13:5xZ) and all are gone.

**A second, smaller defect in that instrument.** `protected_baseline()` (`reports/round-28/run-validation.py:362-377`) compares correctly (`git_blob_sha(data)` vs the `ls-tree` oid) but records the mismatch row's `observed_blob` as `sha(data)` — a **sha256** — beside a `baseline_blob` that is a **git blob SHA-1**. The two columns in the filed row are not the same digest function, so the row cannot be diffed against its own baseline without knowing which is which. This is reported, not fixed: the runner is a peer's live artifact this round.

## Detector control (the audit fires on tampering)

`python3 -B .scratch/x51/watch28.py control` on 2026-10-18T20:11Z, two targets:

- `reports/round-8/claims.json` — baseline blob SHA-1 `1902149194b5d44f22288631c17ae28d537b2a7c` **matches** live bytes → `clean_match: true`; appending `b"\nx51-in-memory-only-probe\n"` **in memory only** → blob SHA-1 differs → `tamper_detected: true`; live file re-read **byte-identical** → `live_bytes_unchanged: true`.
- `reports/round-27/claims.json` (the newest filed round, and the one whose declaration this round builds on) — baseline blob `96db04f35d7f48849d669d4834eb9889c9154f37` **matches** → `clean_match2: true`; in-memory probe detected → `tamper_detected2: true`; live bytes unchanged → `live_bytes_unchanged2: true`.

`pass: true`. This controls the *audit detector*, not any round's product. No file was created or altered. The round-27 target matters because a watch that only ever probes round 8 cannot show that the newly-frozen round is inside the same comparison. The control **did** fire on the real breach: the same comparison that reported `0 mismatches` at samples 1–2 reported the `receipt.json` row at samples 3–4, which is the detector working on live data rather than on a probe.

## Closing watch

Read-only, `range(1, 4)` with `time.sleep(60)`; two runs, each **2026-10-18**, exit **0**. Both runs compare the same extended surface (`reports/round-{8..27}` + `tools/gates/frozen/round-{8..27}`), launched 5 s apart.

- Run A samples at **20:11:22Z**, **20:12:22Z**, **20:13:22Z**, **20:14:22Z**.
- Run B samples at **20:11:27Z**, **20:12:27Z**, **20:13:27Z**, **20:14:27Z**.

Held constant at all eight samples: missing `[]`; protected tracked paths `1587`; the 28 ignored paths and their digests; the 12 fleet status rows; fleet HEAD `cdd444d3`; lane HEAD `69cecbc7`; baseline→HEAD diff over the protected surface empty.

The channels that moved:

| Channel | Movement |
|---|---|
| `mismatches` / `manifest_sha256` / `protected_status` / `tracked_newer_than_dispatch` | 0 → 1 at samples 3–4 in **both** runs — the `reports/round-27/gate-tests/receipt.json` breach above. No other protected path moved. |
| `lane_status` | 0 rows (run A sample 1) → 26 rows (samples 4), every delta a **peer round-28** path under `reports/round-28/` or an amended live file (`corpus/README.md`, `examples/culture-d4/*`). At 20:17:57Z it had reached **83 rows** (7 `M`, 76 `??`), all round-28. |

`watch_consistent` is therefore **false**, and correctly so: the breach is real and the lane channel legitimately moves during a live wave. The verdict binds the observations above, not later parent integration.

## Fleet-root findings

Fleet root = `/home/vgpnk/Projects/shokunin`. Surface inventory (2026-10-18T20:12Z): **2,910** tracked files (round 27: 2,909), **15** tracked top-level files, **6** tracked top-level directories (`.devin`, `.omp`, `research`, `scripts`, `templates`, `.ufo`). `git status --porcelain=v1 -uall` returns **12 rows**; without `-uall` it returns **2** (`M .ufo/l0-questions.md`, `?? .scratch/`). Fleet HEAD unchanged all cycle.

### F1 — ten `?? .scratch/*.out` (inherited, unchanged)

All ten present, byte-identical and mtime-identical to the round-25/26/27 records: `battery.out`, `coupling.out`, `craft.out`, `d2check.out`, `d3check.out`, `replay-r22.out`, `replay-r3.out` (all 2026-10-18 13:10:25−03:00); `rv5-p.out`, `rv6-p.out`, `rv7-p.out` (all 13:15:49−03:00). Each is a one-line `python3: can't open file '<path>': [Errno 2] No such file or directory` error from a lane tool invoked at the fleet root (seven name `/home/vgpnk/Projects/shokunin/tools/...`; three name `/tmp/coldrun-b/export2/reports/round-{5,6,7}/run-validation.py`). The fleet `.gitignore` does not cover `.scratch/`. **F1: unchanged from round 27 — no new row, none removed.**

### F2 — the stray `bash: ` tree (inherited, unchanged)

9 filesystem entries (8 directories + 1 file); the file `bash: /home/vgpnk/Projects/shokunin/souji-shokunin/tests/tools/souji-verify.sh: No such file or directory`, **10,139** bytes, sha256 `3a127f03b9afbfef76d8cfb4274e0cb16aa7d59b915ce19e70a236321e9b3c33`, created **2026-10-18T14:01:47.326772594−03:00** — byte-identical to the round-25/26/27 record. Its content is a souji-shokunin round-4 adversarial seat S54 JSON receipt (`"seat": "S54"`, `"round": 4`, `"lane": "souji-shokunin"`), written to a path a mis-quoted command built. **F2: unchanged from round 27.**

### F3 — `.scratch/goal-20261018-game-dev-2d-training.md` (inherited, unchanged)

6,543 bytes, sha256 `e56e047b619b8c5da2ce77dd3a79b39bc19930e9ecb8a071e1212f2f90c71bb0`, mtime **2026-10-18T16:00:35−03:00** (= 19:00:35Z) — byte-identical to the round-27 record. It is a host-level goal contract ("Goal — game-dev-2d-shokunin training loop (39 rounds) + 3D Epic re-vendoring side-round … Created 2026-10-18 by write-goal flow with the operator"), not a kotodama artifact, and it is not dispositioned here. **F3: unchanged from round 27.**

### F4 — modified `.ufo/l0-questions.md` (inherited, **and grown inside this window**)

Tracked file at fleet HEAD `b671b8af6ff5d9c4f6b5c3b1913985c09e3b5ed7`, modified in the working tree. Round 27 recorded **1 insertion** (sha256 `a64fe9c9708adb30006784f5bb6aa45d33ec9eaf615e52fa4e32d3c40d476a5c`, mtime 15:40:17−03:00). Round 28 finds **2 insertions** — live sha256 `60ccdc9e9a0a7179d97d82349a34e0cc53f1520c6f69c6db624f4f72beac51a6`, 38,356 bytes, mtime **2026-10-18T17:14:10−03:00 = 20:14:10Z**, `git diff --stat` → `1 file changed, 2 insertions(+)`.

```
+kama | round-8 | wire id `opencode-go/glm-5.3-flash-free` is NOT in this host dispatch catalog …   (round 27)
+game-dev-2d | round-101 | 3D side-round (Epic unreal-skills re-vendoring + UE-runtime docker unlock) DEFERRED: game-dev-3d lane is under an active round-104 run by a parallel session …   (new)
```

The second line's mtime, **20:14:10Z, is after round-28 dispatch (20:10:20Z)** — so unlike every earlier fleet finding, this one was written **inside** the round-28 window by host/peer machinery, not before it. It is a peer lane's open-question append (the line's own `game-dev-2d` prefix), not a kotodama write. **F4: grown from round 27; the only fleet-root write this seat observed inside a round window.**

### Masking control — why a plain status check would call this root clean

The stray tree is hidden from Git's default untracked view by the fleet ignore rule `*-shokunin/` matching its inner `…/shokunin/souji-shokunin` component (2026-10-18T20:12Z):

```
$ git check-ignore -v 'bash: /home/vgpnk/Projects/shokunin/souji-shokunin'
.gitignore:1:*-shokunin/	bash: /home/vgpnk/Projects/shokunin/souji-shokunin
$ git status --porcelain=v1 -- 'bash: '                 # → 0 rows
$ git status --porcelain=v1 -uall --ignored -- 'bash: ' # → 1 row: !! "bash: …/souji-verify.sh: No such file or directory"
$ find 'bash: ' | wc -l                                 # → 9 entries
```

Two independent blind spots therefore hide it: the `*-shokunin/` ignore rule, and `git status`'s default directory collapsing (`?? .scratch/` instead of the ten leaf files). The same collapsing is what reduces the 12-row fleet reading to 2 rows without `-uall`. **Fleet cleanliness must be asserted over the filesystem, not only over Git's untracked view.** The remaining ignored top-level families are `.tower/comms` (96 rows), `.ufo/waves` (36), and the sixteen `*-shokunin/` lane directories — all expected by the fleet ignore rules.

## Limits and handoff

- Repeated sampling cannot prove no write-and-restore occurred between samples; the manifest digest is a stability anchor, not a historical identity claim. That limit is exactly what bit this round: three transient revisions of one filed path were each observed by one instrument and each were gone when the next instrument looked. **The window is 60 s wide; a shorter-lived write is invisible to this watch by construction.**
- Ignored files have no Git baseline; observed stability does not establish their historical identity.
- **Attribution of the breach is by mechanism and timestamp only, and is marked `to-verify`.** The writer is a seat that invoked `reports/round-27/gate-tests/run-gate-tests.py` in the lane worktree without `--selftest`; the tool makes such a write unavoidable and its `--check` flag does not prevent it. The `head`/`copy` fields of the transient revisions name round-28's own declaration commit (`69cecbc7…`) and a scratch path (`.scratch/r27-d13/law-tree-…`, `.scratch/x55/replay/…`), which points at the round-28 D/O wave, but this seat did not observe the invoking process and asserts no attribution.
- F1/F2 attribution is by content and mtime only. The `bash: ` receipt's author is inferred from its own `"seat": "S54"` field, not verified. F1 predates round-25 dispatch, F2/F3 predate round-28 dispatch. **F4's second line postdates round-28 dispatch by ~4 min**, so it is not a kotodama write but *is* a write inside the window.
- **The filed-round clause fails as observed** (one path, restored) and **the fleet-root clause fails as observed** (four families, one grown). Disposition belongs to the parent integrator: for the breach, confirm the restore, decide whether the transient window needs a re-pin row or a note, and route the `--check`-ignored write defect to whoever owns the round-27 battery. **The successor carries the identical defect and is worth fixing before it too becomes filed:** `reports/round-28/gate-tests/run-gate-tests.py` also declares `--check` (`:22`, help "measure only, print") and also never consults it — `grep -n "args\.check"` on that file returns nothing, its `main()` branches only on `args.selftest` (`:1039`), and it writes `HERE / "receipt.json"` unconditionally at `:1086-1087`. So the round-28 battery will overwrite its own filed receipt the same way the round-27 one did; the round-28 copy has not yet been rewritten because it is still uncommitted and its wave has not finished. For F1/F2 the same dispositions round 25–27 named; F3 is host-goal machinery to leave alone or relocate; F4 is a peer lane's pending open-question edit for its own lane to commit. This seat left every path byte-identical to how it found it.
- The protected surface here is **1,587** paths (reports 1,452 + frozen 135). This agrees with the round-28 runner's own filed measurement, so the round-26/27 disagreement over the figure (1,328 / 1,460) is now settled in favour of the wider form.
- No validator was executed by this seat, including historical validators that could rewrite filed receipts. The round-28 runner's own `validation.json` readings are quoted as another instrument's output, not as this seat's measurement; that file is a peer's live artifact and moved twice during the window (20:13:51Z, 20:17:33Z). Peer round-28 writes appeared throughout the watch; this seat neither edited nor certified their content.

## Read-only replay

From the lane root (`export TMPDIR="$PWD/.scratch"` first), this reproduces the protected verdict, the detector control, the ignored-path census and the fleet rows without writing any receipt or executing a historical validator:

```bash
export TMPDIR="$PWD/.scratch"
python3 -B .scratch/x51/watch28.py snapshot 0   # protected: mismatches must be [] on a settled tree
python3 -B .scratch/x51/watch28.py control      # detector control: pass must be true
git diff --name-status 6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede HEAD -- \
  reports/round-8 reports/round-9 reports/round-10 reports/round-11 reports/round-12 \
  reports/round-13 reports/round-14 reports/round-15 reports/round-16 reports/round-17 \
  reports/round-18 reports/round-19 reports/round-20 reports/round-21 reports/round-22 \
  reports/round-23 reports/round-24 reports/round-25 reports/round-26 reports/round-27 \
  tools/gates/frozen/round-8 tools/gates/frozen/round-9 tools/gates/frozen/round-10 \
  tools/gates/frozen/round-11 tools/gates/frozen/round-12 tools/gates/frozen/round-13 \
  tools/gates/frozen/round-14 tools/gates/frozen/round-15 tools/gates/frozen/round-16 \
  tools/gates/frozen/round-17 tools/gates/frozen/round-18 tools/gates/frozen/round-19 \
  tools/gates/frozen/round-20 tools/gates/frozen/round-21 tools/gates/frozen/round-22 \
  tools/gates/frozen/round-23 tools/gates/frozen/round-24 tools/gates/frozen/round-25 \
  tools/gates/frozen/round-26 tools/gates/frozen/round-27            # must print nothing
grep -n "args\.check" reports/round-27/gate-tests/run-gate-tests.py  # must print nothing — the defect
grep -n "args\.check" reports/round-28/gate-tests/run-gate-tests.py  # must print nothing — the successor's copy of it
cd /home/vgpnk/Projects/shokunin
git status --porcelain=v1 -uall         # 12 rows: 1 M .ufo/l0-questions.md, 11 ?? .scratch/*
git check-ignore -v 'bash: /home/vgpnk/Projects/shokunin/souji-shokunin'
find 'bash: ' -type f                   # 1 file, 10,139 bytes
sha256sum .scratch/goal-20261018-game-dev-2d-training.md   # e56e047b…, 6,543 B
```

Assertions on a settled tree (re-verified 2026-10-18T20:18:27Z with `snapshot 0`): `snapshot().mismatches == []`, `missing == []`, `protected_tracked_paths == 1587`; `control().pass is True`; the baseline→HEAD diff over the protected surface is empty; **both** `grep -n "args\.check"` commands print nothing (the `--check` flag is inert in both batteries — do **not** run either in the lane worktree without `--selftest`); the fleet status rows are the twelve listed at the 20:12Z sample (the fleet reading is a live snapshot and will grow as peer lanes write); `find 'bash: ' -type f` prints exactly the truncated-name file above.

**One assertion that does *not* hold, and why it is the right kind of failure.** On the settled tree `tracked_newer_than_dispatch` is **not** empty: it still holds `{"path": "reports/round-27/gate-tests/receipt.json", "mtime_utc": "2026-10-18T20:14:42Z"}`, because the **restore itself** wrote the file and left a post-dispatch mtime on a byte-identical path. So the mtime channel stays red after the byte channel goes green — the filed path was touched inside the round window even though its content is exactly the baseline content. Any downstream check that asserts "no protected path has an mtime later than dispatch" will fail on this tree, correctly, and the parent should read that as the residual trace of the breach rather than as a new one.

FILES: reports/round-28/scope.md, .scratch/x51/watch28.py, .scratch/x51/watchlog28.json, .scratch/x51/watchlog28-ext.json, .scratch/x51/control28.json, .scratch/x51/control28-final.json, .scratch/x51/replay-check.json | SUMMARY: X51 scope watch — filed rounds 8–27 plus frozen gate generations (1,587 tracked paths) clean at samples 1–2 of two independent 4-sample runs against baseline `6c0ac448` with a two-target detector control passing, then **FAIL**: the filed `reports/round-27/gate-tests/receipt.json` was rewritten in place at 20:13:21Z and restored by 20:14:42Z (mechanism: the round-27 battery writes its receipt unconditionally and never reads `--check`; caught independently by this watch, `adjacency.md` at 20:12:33Z, X60-F5, X61, X62 and the round-28 runner's own protected check); fleet root not clean, carrying the unchanged round-25/26/27 debris (F1 ten `?? .scratch/*.out`, F2 stray `bash: ` tree with a 10,139-byte souji receipt, F3 host goal file) plus F4 `.ufo/l0-questions.md` grown to 2 insertions at 20:14:10Z, the only fleet write observed inside the round window.
