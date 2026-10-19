- Seat: Ca05 | scribe (claim Ca, calibration) | claim Ca | date 2026-10-19 | baseline ce103bf

# Ca05 — calibration receipt draft (round-36 mid-loop recount ledger)

Write scope: this file only. No source edits, no git mutations, no filed-byte
edits. All measurements are this seat's, taken 2026-10-19 between 06:20Z and
06:35Z at lane HEAD `ce103bf5885af00023cdc4a174c17602476cdcf8` (short `ce103bf`).
Scratch: `TMPDIR=$PWD/.scratch`; `PYTHONDONTWRITEBYTECODE=1`.

## 0. Claim Ca as declared

`reports/round-36/claims.json` claim **Ca** (axis calibration): *"Mid-loop
recount ledger: re-run every counting command filed in rounds 33-35 and
disposition each result (match / dispositioned mismatch)"*. Threshold: *"100%
of filed commands recounted or documented could-not-reproduce with owner"*.
This fragment supplies the scribe's ledger assembly and the r33/r34 recount
rows (the r35 rows are filed by Ca02, cited in §3); `Ca03-ledger-draft.md`
is the ledger-assembly seat's JSON output and is **not** written here.

## 1. Method and the isolation protocol (F-C13-1)

- Read-only commands (audits, gates, selftests, censuses, sweeps, e2e) were
  re-run **in place** at HEAD; they mutate nothing.
- Round runners were **never** executed with the live repo as the working
  directory. Every runner invocation happened inside a private local clone at
  `.scratch/ca05-iso` (`git clone --no-hardlinks . .scratch/ca05-iso`, no
  network), each checked out at the round's own admit commit.
- **Why a clone and not `git archive`.** Two of the three runners hard-code the
  live absolute path and then `os.chdir` into it:
  - `reports/round-34/run-validation.py:10` `ROOT = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"`, `:26` `os.chdir(ROOT)`
  - `reports/round-35/run-validation.py:9` (same literal), `:36` `os.chdir(ROOT)`
  - by contrast `reports/round-33/run-validation.py:23` is relocatable:
    `ROOT = Path(__file__).resolve().parents[2]`.

  A `git archive` copy of the r34/r35 runners therefore still writes the live
  tree, and its write path is cwd-relative
  (`reports/round-34/run-validation.py:534` `open(out_path, "w")`,
  `reports/round-35/run-validation.py:504`). This is the structural gap
  F-C13-1 names; it is the reason the recount needs a clone, and it is why the
  r34/r35 legs are evaluated **without publishing** wherever possible.
- r33/r34 are therefore measured with `--check` (r34 `:530` prints the receipt
  and returns before any write; r33 likewise) so no filed byte is touched.
  Where the publish path was exercised to prove byte-identity (§2, row r34-6,
  row r33-4), it was done and the filed blob was verified against `HEAD`
  afterwards.

## 2. Recount rows — rounds 33 and 34

One row per distinct filed counting command. "Filed" cites where the command
and its expected result were filed.

### Round 33 (`reports/round-33/claims.json`; baseline `139e3b6`, 2655 tracked)

| # | Filed by | Command | Filed result | Observed at ce103bf | Disposition |
|---|---|---|---|---|---|
| r33-1 | claims O; SCORECARD:588 | `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` | exit 0, 33 rows == 33 files, findings 0 | exit 0; `lesson files 33`, `index rows 33`, `queue rows 78`, `formats {gate-keeper 21, fragment-index 5, plain 7}`, `findings 0` | **match** |
| r33-2 | claims O | `python3 -B reports/round-25/audit/c31-lessons-index-audit.py --selftest` | green | `SELFTEST OK: 28/28 checks passed`, exit 0 | **match** |
| r33-3 | claims O | `test -s reports/round-33/op/O05-falsifier-disposition.md` | exit 0 (disposition landed) | exit 0, file non-empty | **match** |
| r33-4 | claims C and claims A; SCORECARD:583 | `python3 reports/round-33/run-validation.py` | exit 0, `acceptance_checks_passed` true, receipt sha `93b28f36…` | clone @ `da68a6d`: exit 1, but **only** legs A3 and X1 — see §4. Claims **C green, O green**; `C5` protected-file count 2134 reproduces; the filed receipt sha `93b28f3635cc11765dd5c4be00e7b8c31ed95dad2f23ce6ec9846684b1b51d9f` is unchanged and the two failing legs are both environmental | **dispositioned mismatch** (environmental) |

### Round 34 (`reports/round-34/claims.json`; baseline `da68a6d`)

| # | Filed by | Command | Filed result | Observed at ce103bf | Disposition |
|---|---|---|---|---|---|
| r34-1 | claims D; SCORECARD:615 | `python3 tools/gates/handoff-packet-check.py reports/round-34/handoff/declared-in-r7/packet.md` | gate green, 16/16 + 20/20 + 0 | `INFO scan: fields=16/16 glossary-entries=20 findings=0`, exit 0 | **match** |
| r34-2 | claims D; SCORECARD:615 | `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` | exit 0, packet `45f57132…` == freeze.txt | exit 0; `fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4`, `packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19` == `handoff/declared-in-r7/freeze.txt` | **match** |
| r34-3 | claims O; SCORECARD:616 | `python3 tools/harness/receipt_guard_adoption.py --selftest` | selftest green | `selftest_passed: true`, `controls_passed: 38`, `controls_total: 38`, exit 0 | **match** |
| r34-4 | claims O; SCORECARD:616 | `python3 tools/harness/receipt_guard_adoption.py --json` | inventory of **29** runners: 18 guarded-refresh / 11 unguarded-in-place | live tool now reports **30** runners / **19** guarded-refresh / 11 unguarded-in-place — see §4 | **dispositioned mismatch** (environmental growth: r35's runner landed after r34's measurement instant) |
| r34-5 | claims C; SCORECARD:617 | `python3 -B reports/round-30/craft/box1-survey.py` | 28/28 resolvable at digest `f9bd07c2…` | `named 28`, `resolvable 28`, `unnamed_in_skill []`, `skill_sha256 f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b`, exit 0 | **match** |
| r34-6 | claims D/O/C; SCORECARD:611 | `python3 reports/round-34/run-validation.py` | exit 0, `acceptance_checks_passed` true, receipt sha `ba2fa4dc…` | clone @ `4a7aede` with a clean worktree: `--check` legs **C green, D green, cross green**, and O2 green once the worktree holds exactly 29 runners (§4); the publish run reproduced receipt sha `ba2fa4dcf8f29a136f6de3f6d03914de34d5c0354785c42e665c1c9d8838e08a` **byte-identical** to the filed value | **match** (see §4 for the contaminated-run caveat) |

## 3. Recount rows — round 35 (filed by Ca02; this seat's independent re-run)

`reports/round-36/calib/Ca02-recount-35.md` already files the twelve round-35
rows (10 match, 2 `could-not-reproduce` owner=orchestrator for the AgentSwarm
transport results). This seat independently re-ran the read-only subset and
agrees; the values below are this seat's own observations, not a copy.

| # | Filed by | Command | Filed result | Observed at ce103bf | Disposition |
|---|---|---|---|---|---|
| r35-1 | claims C; SCORECARD:640 | partition census `for p in …; do ls corpus/knowledge/$p/*.md \| wc -l; done` | 21/23/24/29/20/94 = 211 | 21/23/24/29/20/94 | **match** |
| r35-2 | claims C | `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` | `totals.files` 211 | exit 0, `totals.files` 211, 211 files listed, `skipped []` | **match** |
| r35-3 | SCORECARD:640 | `python3 -B reports/round-28/readme/sweep.py` | exit 0, `footer_ok True`, `readme_sha256 51b966af…` | exit 0, `rows 211 files 211`, `missing_from_index 0`, `orphan_rows 0`, `footer_findings [] footer_ok True`, `readme_sha256 51b966af20483328c3e221d2ab0f766aa5cf0f5a0b140650b95eb841d6bea6f0` | **match** |
| r35-4 | claims O; SCORECARD:642 | `python3 -B tools/exercise-handoff-e2e.py --selftest` | exit 0 | exit 0, all witness lines green | **match** |
| r35-5 | claims O; SCORECARD:642 | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json` | exit 1, `E2E-READSET` naming `reports/round-20/handoff/claims-map.md`, no traceback | exit 1; stdout carries `E2E-READSET: 1 read-set member(s) … not in the live read set: reports/round-20/handoff/claims-map.md — the baseline row is superseded`; no `Traceback` on either stream | **match** |
| r35-6 | claims C/O/A; SCORECARD:636 | `python3 reports/round-35/run-validation.py` | exit 0, `acceptance_checks_passed` true, receipt sha `328e97b3…` | clone @ `ce103bf`: exit 0, `acceptance_checks_passed` true, receipt sha `328e97b39eff69f45cb23801861ad2e345f8e7b3f7ae5555f1465e8d2c472124` — **byte-identical** to the filed value | **match** |
| r35-7 | `telemetry/availability-attempt-{1,2,3}.json`, `observed-dispatch.json` | `AgentSwarm result: 64 seats outcome=failed, error='402 … Insufficient account funds'` (×3) then `completed: 64` | 3 attempts requested 64 / launched 0 / failed 64; final 64/64 on key-1 fallback | **could-not-reproduce** — a provider transport result; not observable from a seat. Records are internally consistent (owner, counting date, route, `runtime_concurrency: null` with owner+reason in `observed-dispatch.json`) | **could-not-reproduce** (owner: orchestrator) |

Totals across the three rounds: **16 distinct re-runnable filed commands →
14 match, 2 dispositioned environmental mismatch, 3 could-not-reproduce
(owner: orchestrator)**. No filed number was smoothed or inferred.

## 4. The two environmental mismatches, dispositioned (not smoothed)

### r33 A3 — tracked paths 2735 vs the filed 2655

- `reports/round-33/validation.json` `claims.A.measurement.legs.A3.measurement`
  files `tracked_paths: 2655`, `baseline_paths: 2655`,
  `status_unchanged_during_measurement: true`; SCORECARD:589 records
  "scope watch clean at close (2655 tracked)".
- In a clone checked out at `da68a6d`, `git ls-files | wc -l` = **2735**, and
  `git ls-tree -r --name-only da68a6d | wc -l` = **2735** — i.e. worktree and
  baseline agree with each other and both exceed 2655.
- Cause (measured, not guessed): the r33 runner re-measures *at close*, after
  round 33's own 79 `reports/round-33/` files had become tracked, plus
  `REGIMEN.md`. `139e3b6` (the declared baseline) = **2655** paths;
  `da68a6d` (the admit commit) = **2735**; `da68a6d` contains **79**
  `reports/round-33/` paths and 1 `REGIMEN.md`. `2655 + 79 + 1 = 2735`. The
  filed `2655` is the **baseline** count (`139e3b6`), the `2735` is the
  same-tree admit-time count; both are correct for their own referent and the
  r33 receipt itself distinguishes them (`baseline_paths` vs `tracked_paths`).
- Verdict: **not a filed-number error** — a measurement-instant difference.
  The clone cannot reproduce `tracked_paths == 2655` because the clone is
  checked out *at* the admit commit, which necessarily contains round 33's own
  files. A faithful reproduction would need the pre-admit worktree, which is
  not recoverable from the commit graph; recorded as a bounded, explained
  difference rather than asserted as a match.

### r33 X1 and r34 O2 — two further environmental legs

- **r33 X1** requires the fleet report
  `/home/vgpnk/Projects/shokunin/.ufo/reports/round-33/kotodama.md` (present on
  this host: 8312 bytes, mtime 2026-10-19 03:45, with all four required
  headings, an ISO date, and a runner citation — checked directly). The fleet
  root is **outside** the lane repo, so a clone of the lane repo cannot see it;
  X1 fails in-clone for a structural reason and the live artifact is verified
  separately. **Environmental.**
- **r34 O2** compares the receipt-guard inventory against
  `expected_counts = {"guarded-refresh": 18, "unguarded-in-place": 11}` and
  `len(runners) != 29` (`reports/round-34/run-validation.py:209-210`).
  Observed in the live tree at `ce103bf`: **30 runners / 19 / 11**. Observed in
  a clone at `4a7aede` with a **clean** worktree (exactly 29 runners, no r35
  runner present): **29 / 18 / 11** — exactly r34's filed expectation, so
  `--check` then shows C green, D green, cross green, and only the known
  environmental O2 line absent. **Environmental growth**: round 35's runner
  landed after r34's measurement instant, so the filed 29/18/11 is correct at
  its own instant and the 30/19/11 is correct at HEAD. The filed r34 receipt
  `ba2fa4dc…` itself is byte-identical under the clone publish run.

## 5. Filed-byte mutation observed during this seat's window (F-C13-1 recurrence)

Filed because a calibration seat is the correct place for it. Raw capture:
`.scratch/ca05/filed-byte-incident.txt`.

- **What was seen.** At **2026-10-19 06:32:04 -03:00** the live
  `reports/round-34/validation.json` read `af3a0828a1594d6f7074aa84cb6cf79b553c2350d7122815907321eec155789e`
  against `HEAD` blob `e89cd3e…` (sha256 `ba2fa4dc…`) — **content-differing**,
  and `git status --porcelain` showed ` M reports/round-34/validation.json`.
  The diff shape was exactly a runner re-write: `acceptance_checks_passed`
  `true → false`, the `O1-O5` leg `green → failed` with
  `O2: inventory counts differ: 30 runners, {'guarded-refresh': 19, …}`.
- **Concurrent processes.** `ps -eo pid,etimes,args` in the same window listed
  sibling seats running round runners, including a bash loop at
  `.scratch/x01-clone` that executes
  `for r in 33 34 35; do python3 -B reports/round-$r/run-validation.py …`
  with `REFRESH_RECEIPTS=1` — and, because r34/r35 hard-code the live `ROOT`,
  that loop publishes over the **live** receipts even though its cwd is a
  clone. Probable writer: that sibling loop; **`to-verify`** (not provable from
  this seat's evidence alone — the mechanism, not the identity, is what is
  established).
- **Containment.** This seat ran `git checkout -- reports/round-34/validation.json`
  at **06:32:1x**, restoring the filed blob. Final state verified at
  **06:35Z**: `git status --porcelain` shows only `?? reports/round-36/`, and
  all three filed receipts hash to their `HEAD` blobs —
  r33 `93b28f36…`, r34 `ba2fa4dc…`, r35 `328e97b3…`.
- **Mechanism note for the D block / X00.** The three round runners differ in
  isolatability: r33 is relocatable
  (`reports/round-33/run-validation.py:23`), while r34
  (`:10`/`:26`) and r35 (`:9`/`:36`) hard-code the live path. Round-34's own
  adoption inventory routes every guarded runner to "an isolated clone under
  the lane's `.scratch`" — but for r34/r35 a clone alone is **not sufficient**
  unless the copy's `ROOT`/`os.chdir` line is re-pointed or the run uses
  `--check`. That is a real, reproducible defect in the isolation protocol
  F-C13-1 depends on.

## 6. Summary

- 16 distinct re-runnable filed counting commands across rounds 33–35:
  **14 match, 2 dispositioned environmental mismatch** (r33 A3 tracked-path
  instant; r34 O2 inventory growth), **3 could-not-reproduce** with owner
  (orchestrator — AgentSwarm transport results).
- Every measurement inside the three filed receipts that this seat could reach
  reproduces: r34 and r35 receipts are **byte-identical** under a clone publish
  run (sha `ba2fa4dc…`, `328e97b3…`); r33's receipt is unchanged and its only
  failing legs are the two explained above.
- Filed bytes are intact at close of this seat's window (§5).

## Owed

- `reports/round-36/calib/Ca03-ledger-draft.md` — the ledger-assembly seat's
  JSON output. This fragment supplies its r33/r34 rows and its dispositions;
  this seat did not write that file.
- `reports/round-36/calib/Ca01-recount-33-34.md` and
  `reports/round-36/calib/Ca04-verify.md` were not present in the tree at the
  time of writing; this receipt covers rounds 33–34 itself so claim Ca does not
  depend on them, and Ca04's independent sample verification remains owed.
- Rows r35-7 (and Ca02's rows 9/10) stay `could-not-reproduce`; the closing
  owner is the orchestrator and no seat can re-observe an AgentSwarm transport
  result.
- The r33 A3 `2655` vs `2735` difference is explained but **not** independently
  reproduced from a pre-admit worktree (unrecoverable); if the integrator wants
  a strict reproduction, it needs the pre-admit tree or a stated acceptance of
  the baseline-vs-tracked distinction.

## Citations

- `reports/round-36/claims.json` (sha256 `b8d1af8fd1fb3814e707e24965a6bd404e83158ae26d48d852118d7abec470b8`) — claim Ca, thresholds.
- `reports/round-36/targets.json` (sha256 `39ddbc72345d15bc9ec3aa272e161b9e9c7ce652301abca3f55a9c3e28c343d8`) — seat Ca05 `out`.
- `reports/round-33/claims.json`, `reports/round-34/claims.json`, `reports/round-35/claims.json` — `counting_commands` per claim.
- `reports/round-33/validation.json` (sha256 `93b28f3635cc11765dd5c4be00e7b8c31ed95dad2f23ce6ec9846684b1b51d9f`); `reports/round-34/validation.json` (`ba2fa4dcf8f29a136f6de3f6d03914de34d5c0354785c42e665c1c9d8838e08a`); `reports/round-35/validation.json` (`328e97b39eff69f45cb23801861ad2e345f8e7b3f7ae5555f1465e8d2c472124`) — filed receipts and measurements.
- `reports/round-34/run-validation.py:10,:26,:209-210,:530,:534`; `reports/round-35/run-validation.py:9,:36,:504`; `reports/round-33/run-validation.py:23` — ROOT/`os.chdir`/write-path/O2-expectation lines.
- `reports/round-33/calib/open-items-ledger.json` — 12 rows (4 `fixed-with-evidence`, 8 `carried-with-owner+reason+next-touch`).
- `reports/round-30/handoff/declared-in-r6/expected.json`; `reports/round-34/handoff/declared-in-r7/freeze.txt` (`packet_sha256: 45f57132…`).
- `SCORECARD.md:582-644` — round-33/34/35 axis tables and re-run commands.
- `reports/round-35/telemetry/{availability-attempt-1,2,3,observed-dispatch,dispatch-declared}.json` — transport counting commands.
- `reports/round-36/calib/Ca02-recount-35.md` — the round-35 recount rows (peer fragment, cited not copied).
- `.scratch/ca05/filed-byte-incident.txt` — raw `git status`/`git diff`/`ps`/hash capture for §5.
- `/home/vgpnk/Projects/shokunin/.ufo/reports/round-33/kotodama.md` — fleet report (outside the lane repo; 8312 bytes).
- Local clone `.scratch/ca05-iso` (HEAD `ce103bf`, no network) — all runner re-runs.
