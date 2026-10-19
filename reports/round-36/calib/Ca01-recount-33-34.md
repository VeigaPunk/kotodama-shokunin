- Seat: Ca01 | executor | Ca | date 2026-10-19 | baseline ce103bf

# Ca01 — recount of every counting command filed in rounds 33 and 34

Mission (`reports/round-36/targets.json`, seat `Ca01`): re-run each counting
command filed by rounds 33–34 and record observed vs filed. Claim `Ca`
(`reports/round-36/claims.json`, `Ca`): one row per filed command, each with
observed output and disposition; mismatches named with causes, none smoothed.

Scope note: this fragment covers rounds 33–34 only. Round 35 is seat `Ca02`'s;
round 36's own legs belong to the round. Cross-references to r35 below are
limited to what the r35 *recount* must inherit from this seat's isolation
method, and are labelled as such.

## 1. Method and isolation

- Baseline `ce103bf5885af00023cdc4a174c17602476cdcf8` (`git rev-parse HEAD`,
  2026-10-19). Filed receipts re-verified against `SCORECARD.md` prefixes
  before any recount: r33 `93b28f3635cc1176…` == `93b28f36…`
  (`SCORECARD.md:584`); r34 `ba2fa4dcf8f29a13…` == `ba2fa4dc…`
  (`SCORECARD.md:611`). Both also equal their `HEAD:` blobs, so no filed byte
  of r33/r34 moved.
- Isolation for runner-invoking commands: no `reports/round-*/run-validation.py`
  was executed in-tree (F-C13-1). Two isolated carriers were used:
  `.scratch/ca01-clone` (a real `git clone --shared` at `ce103bf`, so `HEAD`
  and the object store exist) and `.scratch/ca01-c34`
  (`git clone --no-checkout` then `git checkout -f 4a7aede`), plus
  `.scratch/ca01` (a `git archive HEAD` extraction) for the standalone tools.
- Runner output was captured to `.scratch/`, not `/tmp`: `/tmp` is a tmpfs at
  80% (13G/16G) and redirected runs there die with exit 120 (`ls -la
  /tmp/r33c.json` → 0 bytes, `df -h /tmp` → `13G used, 3.1G avail`). This is
  the cause of the empty redirects seen mid-recount, not a runner failure.
- 13 filed command entries (10 distinct commands) were recounted: 5 entries in
  `reports/round-33/claims.json:32,47,60` and 8 entries in
  `reports/round-34/claims.json:31,46,61`.

## 2. Recount table

`MATCH` = observed == filed. `MISMATCH-DISPOSITIONED` = observed differs, cause
named. `ENV` = the command cannot return its filed value at `HEAD` for a reason
outside the filed record.

| # | Source | Command | Filed | Observed | Disposition |
|---|---|---|---|---|---|
| 1 | r33 O[0] | `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` | exit 0, 33 rows == 33 files, findings 0 | exit 0; `lesson files: 33`, `index rows: 33`, `queue rows: 78`, formats `{gate-keeper 21, fragment-index 5, plain 7}`, all six checks PASS, `findings: 0` | MATCH (exact) |
| 2 | r33 O[1] | same, `--selftest` | still green | exit 0, `SELFTEST OK: 28/28 checks passed` | MATCH |
| 3 | r33 O[2] | `test -s reports/round-33/op/O05-falsifier-disposition.md` | disposition landed | exit 0 (file 20935 bytes, sha256 `6499d3b3fa8813e2…`) | MATCH |
| 4 | r33 C[0] | `python3 reports/round-33/run-validation.py` | C legs green | **in isolated clone at `ce103bf`: `C passed True`, failures `[]`** | MATCH |
| 5 | r33 A[0] | same runner, A legs | A legs green | in clone: A1/A2/A4/A5/A6/A7 green, A5 `last_touch: c53782a`; **A3 failed**, X1 failed | MISMATCH-DISPOSITIONED (see §3.1) |
| 6 | r34 D[0] | `python3 tools/gates/handoff-packet-check.py reports/round-34/handoff/declared-in-r7/packet.md` | exit 0, 16/16 + 20/20, findings 0 | exit 0, `fields=16/16 glossary-entries=20 findings=0` | MATCH (exact) |
| 7 | r34 D[1] | `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` | exit 0, packet sha == freeze.txt | exit 0; `fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4`; `packet_sha256=45f5713261762a95…` == `freeze.txt` and == the filed `freeze_packet_sha256` | MATCH (exact) |
| 8 | r34 D[2] / O[2] / C[1] | `python3 reports/round-34/run-validation.py` | `acceptance_checks_passed: true`, D/C/O legs green, O `class_counts {guarded-refresh 18, unguarded-in-place 11}` | **D green, C green, cross green; O failed**: `O2: inventory counts differ: 30 runners, {guarded-refresh 19, unguarded-in-place 11}` | MISMATCH-DISPOSITIONED (see §3.2) |
| 9 | r34 O[0] | `python3 tools/harness/receipt_guard_adoption.py --selftest` | selftest green | exit 0, `"selftest_passed": true` | MATCH |
| 10 | r34 O[1] | `python3 tools/harness/receipt_guard_adoption.py --json` | 29 runners, 18/11 | at `HEAD`: 30 runners, `{guarded-refresh 19, unguarded-in-place 11}`; **evaluated against r34's delivered revision (clone at `4a7aede`): 29 runners, `{guarded-refresh 18, unguarded-in-place 11}`** | MISMATCH-DISPOSITIONED at HEAD; MATCH at r34's revision (see §3.2) |
| 11 | r34 C[0] | `python3 -B reports/round-30/craft/box1-survey.py` | 28/28 at `f9bd07c2…` | exit 0; `named 28`, `resolvable 28`, `unnamed_in_skill 0`, `skill_sha256 f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b` | MATCH (exact, digest included) |

Tally: 8 entries MATCH exactly; 2 entries MISMATCH-DISPOSITIONED with named
causes; 0 could-not-reproduce; 0 unexplained.

## 3. Dispositions

### 3.1 r33 A3 — post-hoc `HEAD` advance (ENV, not a filed-value defect)

`reports/round-33/run-validation.py:943-944` hard-pins
`tracked_count == 2655 and baseline_count == 2655`. In the clone at `ce103bf`
the runner observed `worktree=2903, baseline=2655`. The divergence is entirely
the worktree side and is expected: `ce103bf` is a later revision than r33's
declared baseline `139e3b6`, and the tree grew by 248 tracked paths across
r34/r35. The baseline side still measures exactly 2655, i.e. the r33 record's
own pinned constant is intact. `unexpected_paths: []` and
`status_unchanged_during_measurement: true`, so no scope-watch row was
violated.

`X1` fails in the clone because `.ufo/reports/round-33/kotodama.md` is not
tracked by git (`git ls-files .ufo` → 0 rows) and is therefore absent from a
checkout. That file exists in the fleet tree and carries the four required
headings and an ISO date (`grep -n '^##' .ufo/reports/round-33/kotodama.md`
→ `Work performed` :13, `Landed changes` :55, `Before → after measurements`
:87, `SHONEN` :117; heading `:1` has `2026-10-19`). Environmental, not a defect.

A5 (`PROVINCE last touch == c53782a`) is green in the clone
(`last_touch: c53782a`) and red only from the `git archive` carrier, where
`PROVINCE.md` is untracked. Recorded so the method's limits are explicit.

### 3.2 r34 O2 — the runner census is not hermetic across revisions

`reports/round-34/run-validation.py:209-210` pins
`expected_counts = {"guarded-refresh": 18, "unguarded-in-place": 11}` and
`len(runners) == 29`. At `HEAD` the same tool reports 30 runners and
`{guarded-refresh: 19, unguarded-in-place: 11}`. The +1 is the r35 runner
itself, correctly classified `guarded-refresh` — `reports/round-35/run-validation.py`
was added after r34 filed, so the constant is a function of the tree at filing
time, not a hermetic expectation.

Evidence that the filed figure is right for r34's revision: invoking the tool
with the working directory inside the clone at `4a7aede`
(`.scratch/ca01-c34`) yields exactly `29` runners and `{guarded-refresh: 18,
unguarded-in-place: 11}`. So the r34 record is not defective; the leg is
non-replayable at a later `HEAD` by construction. This is the recount finding
the Ca ledger must carry as a standing class: **a filed census constant is
only reproducible at the revision that filed it.**

Related mechanism (recorded because it silently defeats "run it in a clone"):
`reports/round-34/run-validation.py:10` and `reports/round-35/run-validation.py:9`
hard-code `ROOT = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"` and
`os.chdir(ROOT)` at import time (`:26` and `:36`). Running those runners from a
clone therefore measures the **live** tree, not the clone — which is exactly how
the first attempt produced 30/19 while the clone's own tree held 29 runners.
`reports/round-33/run-validation.py:23` instead derives
`ROOT = Path(__file__).resolve().parents[2]`, which is why r33's legs did
respond to the clone (`A5 last_touch: c53782a` from a clone run). Any round-33+
recount must therefore either use r33-style relative `ROOT`, or evaluate the
underlying tool directly against the clone, or record `ENV`.

## 4. Cross-check inherited by Ca02 (round 35), verified here

Two r35 legs do **not** reproduce under concurrency, and the cause is a shared
resource under the temp directory, not the filed record. Measured boundary: the
shared resource is not `/tmp` capacity alone — two concurrent
`tools/d2-typed-labels.py --selftest` runs both returned 0 with a shared
`TMPDIR=/tmp` at 80% full, so the failing configuration is a second *v3 selftest*
consumer — the r34 runner I ran alongside invoked
`tools/exercise-handoff-e2e.py --profile v3 --quiet`
(`reports/round-34/run-validation.py:180`), which builds the same packet chain —
i.e. nesting depth plus shared temp state, not disk pressure:

- `reports/round-35/run-validation.py --check`, run **alone**, returns
  `acceptance_checks_passed: true`, `failures: []`, all four claims green,
  `v3_controls: 44`. Run concurrently with a second v3-selftest consumer, the
  same command reports `v3_controls: 0` and fails O1/O3/O4 with
  `v3 selftest lacks control m13a/m13b/m14a/m14b`, plus `O4: r7 default chain
  not green or sha moved`.
- Root cause, reproduced directly: two concurrent
  `tools/d2-typed-labels.py --selftest` runs succeed when `TMPDIR` differs, but
  when the second v3 selftest runs alongside r34's runner the nested witnesses
  go red — `tools/exercise-handoff-e2e.py:4188`
  (`TemporaryDirectory(prefix="handoff-selftest-")`) aborts with `Failed: the
  D4-CL08 landed form is not backed by this run: the alias witnesses are red
  (tools/d2-typed-labels.py --selftest exit 1; tools/assemble-d4-typed.py
  --selftest exit 1)`, even though each witness passes alone (163/163 for
  `d2-typed-labels.py --selftest`).
- Consequence for Ca02: r35's filed `O1`/`O2`/`O3`/`O4` values are only
  reproducible when the r35 runner is the sole v3-selftest consumer. A
  concurrent run is a **false red** and must not be filed as a mismatch.

## 5. Live-tree integrity (outside my write scope, filed for the integrator)

The r35 filed receipt has moved **after** filing. This is the `P1` leg that
appeared in my first (concurrent) r35 run and that I could **not** reproduce
serially:

- `HEAD:reports/round-35/validation.json` sha256 `328e97b39eff69f4…` == the
  `328e97b3…` cited at `SCORECARD.md:636`; the live file is now
  `8a40245dcecff27b…`.
- Live mtime `2026-10-19 06:33:23.612225120 -0300`. The JSON diff is two fields:
  `measured_at_utc` moved `06:19:14.685566-03:00` → `06:33:23.601283-03:00`, and
  the MANIFEST leg's measurement went from
  `{"manifest": "pending-by-construction: integrator files the MANIFEST row in
  the same close pass"}` to `{}`.
- `reports/round-35/run-validation.py:496-505` writes its receipt in default
  mode (`reports/round-34/run-validation.py:526-535` is the same pattern),
  guarded by `tools/harness/receipt_guard.py`, which refuses *unsafe* writes but
  not a legitimate re-run. A concurrent seat re-running the r35 runner in
  default mode is therefore the most likely author; I cannot prove the identity,
  so the cause is `to-verify` and the owner is the r35 integrator / Ca03.
- **Not this seat.** Every runner invocation I made used `--check`, which
  returns at `reports/round-35/run-validation.py:499-500` before `guard_receipt()`
  and the `open(out_path, "w")` at `:503-505`; the r35 receipt still carries
  sha256 `8a40245dcecff27b…` and mtime `06:33:23.612225120`, i.e. it did not move
  during this seat's recount window.
- Cross-check: r33 and r34 receipts are byte-identical to their `HEAD` blobs
  (`93b28f3635cc1176…`, `ba2fa4dcf8f29a13…`), so the drift is r35-only.

This is a recount-visible integrity fact, not a count mismatch: no r35 number
in the table above depends on it, and no filed byte of rounds 1–34 moved.

## Owed

- `reports/round-36/calib/Ca03-ledger-draft.md` — this seat's 13 rows
  (§2) must be merged into the round-36 recount ledger by Ca03; the
  two named disposition classes (post-hoc `HEAD` advance; non-hermetic census
  constant) and the concurrency rule (§4) are the ledger's disposition
  vocabulary for rounds 33–34.
- `reports/round-36/calib/Ca04-verify.md` — independent re-run of a 25% sample
  should sample rows 4, 8, 10 and 11; rows 8/10 only reproduce at r34's
  revision, so the verifier must be told the carrier, not just the command.
- **Could-not-reproduce, owner: r35 integrator / Ca03** — the author of the
  in-place rewrite of `reports/round-35/validation.json` (§5). Cause is
  `to-verify`; the file's `measured_at_utc` and mtime bound the window to
  `2026-10-19T06:19:14-03:00 … 06:33:23-03:00`.
- Not in scope for this seat and left to Ca02/Ca03: the same recount for round
  35's filed counting commands, and the `--freeze`/packet legs, which I did not
  touch (any `--freeze` of `reports/round-34/handoff/declared-in-r7` is
  forbidden; its bytes are pinned).

## Citations

- `reports/round-36/claims.json` (claim `Ca`; sha256 `b8d1af8fd1fb3814…`),
  `reports/round-36/targets.json` (seat `Ca01`; sha256 `39ddbc72345d15bc…`).
- `reports/round-33/claims.json:32,47,60`; `reports/round-34/claims.json:31,46,61`
  — the filed counting commands recounted in §2.
- `reports/round-33/validation.json` (sha256 `93b28f3635cc1176…`, acceptance
  true, `baseline_revision 139e3b66…`); `reports/round-34/validation.json`
  (sha256 `ba2fa4dcf8f29a13…`, acceptance true, `baseline_expanded
  da68a6d705e41f369f21e8607bfaab5b54077f84`).
- `SCORECARD.md:584,611,636` — filed receipt digest prefixes.
- `reports/round-33/run-validation.py:23` (relative `ROOT`), `:876,1454`
  (`os.chdir`), `:943-944` (2655 pin), `:977` (PROVINCE pin).
- `reports/round-34/run-validation.py:10` (hard-coded `ROOT`), `:26`
  (`os.chdir`), `:209-210` (29 / 18 / 11 pins), `:526-535` (receipt write +
  guard).
- `reports/round-35/run-validation.py:9` (hard-coded `ROOT`), `:36`
  (`os.chdir`), `:201-216` (v3-selftest control legs), `:264-281` (P1 leg).
- `tools/exercise-handoff-e2e.py:4188` (`handoff-selftest-` temp dir);
  `tools/d2-typed-labels.py:3033` (`family-clean-`); `tools/assemble-d4-typed.py:424`
  (`assemble-d4-typed-`).
- `tools/harness/receipt_guard.py:152-168` (`guard_receipt` refusal semantics).
- Command outputs (all 2026-10-19, `.scratch/`-based):
  `c31-lessons-index-audit.py` exit 0 / 33 == 33 / findings 0 and
  `--selftest` 28/28; `handoff-packet-check.py` exit 0 / 16-16 / 20 / 0;
  `exercise-handoff-e2e.py --profile v3 --quiet` exit 0 /
  `packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19`;
  `box1-survey.py` 28/28 at `f9bd07c2…`;
  `receipt_guard_adoption.py --json` → 30/19 at `HEAD`, 29/18 at `4a7aede`;
  `reports/round-33/run-validation.py --check` in `.scratch/ca01-clone`
  (A5 `c53782a`, C green, A3/X1 red);
  `reports/round-35/run-validation.py --check` in `.scratch/ca01-clone`
  (exit 0, acceptance true, `v3_controls: 44`) and the concurrent control run
  (`v3_controls: 0`).
- `git rev-parse HEAD` → `ce103bf5885af00023cdc4a174c17602476cdcf8`;
  `git ls-files | wc -l` → 2903; `git ls-tree -r --name-only 139e3b6 | wc -l`
  → 2655; `git log -1 --format=%h -- PROVINCE.md` → `c53782a`;
  `stat -c '%y' reports/round-35/validation.json` → `2026-10-19 06:33:23`.
