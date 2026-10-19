- Seat: Ca02 | executor (claim Ca, round-35 recount) | claim Ca | date 2026-10-19 | baseline ce103bf

# Ca02 — recount of round-35 counting commands

Write scope: this file only. No source edits, no git mutations, no filed-byte
edits. Every measurement below is this seat's, dated 2026-10-19, taken at lane
HEAD `ce103bf5885af00023cdc4a174c17602476cdcf8`. Scratch:
`TMPDIR=$PWD/.scratch`; the round-35 runner was executed **only** in a local
clone at `.scratch/ca02/clone` with its `ROOT` line re-pointed inside the copy,
never in the live tree (F-C13-1).

## 1. Method

- Live-tree commands that only read are re-run in place at HEAD.
- `reports/round-35/run-validation.py` hardcodes the live tree
  (`reports/round-35/run-validation.py:9` `ROOT = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"`)
  and then `os.chdir(ROOT)` at `:36`, so an `git archive` copy of it still
  writes to the live tree. This seat therefore used a local clone
  (`git clone --no-hardlinks . .scratch/ca02/clone`, HEAD `ce103bf`) with that
  one line patched to the clone path, and ran it with `--check` (which never
  publishes). The patch is the only byte difference between the clone runner
  and the filed runner, and it shows up as the single `input_sha256` difference
  in §4.
- Recorded values are the ones filed by round 35 in `claims.json`,
  `SCORECARD.md`, `validation.json` and `telemetry/`.

## 2. Recount rows — one row per distinct filed counting command

| # | Source (filed by) | Command | Filed result | Observed at ce103bf | Disposition |
|---|---|---|---|---|---|
| 1 | `reports/round-35/claims.json` claim C; SCORECARD r35 coverage row | `for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md \| wc -l; done` | 21/23/24/29/20/94 = 211 | 21/23/24/29/20/94 | **match** |
| 2 | `reports/round-35/claims.json` claim C | `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` | `totals.files` 211 (runner leg C3) | exit 0, `totals.files` = 211 | **match** |
| 3 | `reports/round-35/claims.json` claims C/O/A; SCORECARD r35; `validation.json.counting_command`; `telemetry/availability-close-35.json` citation | `python3 reports/round-35/run-validation.py` | exit 0, `acceptance_checks_passed` true, receipt sha256 `328e97b3…` | clone run: exit 0, `acceptance_checks_passed` true, `failures: []`, **all 9 leg statuses equal to the filed receipt** | **match** |
| 4 | `reports/round-35/claims.json` claim O | `python3 -B tools/exercise-handoff-e2e.py --selftest` | exit 0 (leg O1) | exit 0 | **match** |
| 5 | `reports/round-35/claims.json` claim O; SCORECARD r35 operability row | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json` | exit 1, `E2E-READSET` naming `reports/round-20/handoff/claims-map.md`, no traceback | exit 1, stdout carries `E2E-READSET` and the member path; `grep -c Traceback` = 0 on both streams | **match** |
| 6 | SCORECARD r35 coverage row | `python3 -B reports/round-28/readme/sweep.py` | exit 0, `footer_ok True`, `readme_sha256 51b966af…` | exit 0, `footer_ok True`, `rows 211 files 211`, `missing_from_index 0`, `readme_sha256 51b966af20483328c3e221d2ab0f766aa5cf0f5a0b140650b95eb841d6bea6f0` | **match** |
| 7 | SCORECARD r35 operability row | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest` | filed `v3_controls: 44` (leg O1) | exit 0; the runner's own regex `(?m)^  - ` counts **44** (header prose says "43 controls"; the machine count is 44 — see §3 note) | **match** |
| 8 | SCORECARD r35 operability row | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` | exit 0, packet `45f57132…` | exit 0, `fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4`, `packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19` | **match** |
| 9 | `reports/round-35/telemetry/availability-attempt-{1,2,3}.json` | `AgentSwarm result: 64 seats outcome=failed, error='402 Upstream request failed: Insufficient account funds'` | 3 attempts, requested 64 / launched 0 / failed 64 each | **could-not-reproduce** — a provider-side dispatch result; not re-runnable read-only. The record is internally consistent (`requested_workers 64`, `launched_workers 0`, `failed_workers 64`, owner and counting date present in all three) | **could-not-reproduce** (owner: orchestrator; the AgentSwarm transport result is not observable from a seat) |
| 10 | `reports/round-35/telemetry/observed-dispatch.json` | `AgentSwarm result summary '<summary>completed: 64</summary>'` | launched 64 / completed 64 / failed 0, route key-1 fallback | **could-not-reproduce** — same transport-result class as row 9. Record is internally consistent: `actual_route` present, `runtime_concurrency` explicitly `null` with owner + reason, `state: open-at-seat-close` closed by `availability-close-35.json` | **could-not-reproduce** (owner: orchestrator) |
| 11 | `reports/round-35/telemetry/dispatch-declared.json` | `sha256sum reports/round-35/claims.json reports/round-35/targets.json; python3 seat census` | claims `ccfaafc3…`, targets `56ad0392…`, seat_count 64 | `ccfaafc363981d16729c351fa11135e8082b1b0695dc399884d5c91bcc9e26e4`, `56ad03927c7063a3616af2ed0e78ab7b1ca1f3ea43fdf67f2ecf60a7f1b63215`; census 64 rows, 64 unique `out`s | **match** |
| 12 | SCORECARD r35 adjacency row | `python3 reports/round-35/run-validation.py` (audit leg A1) | `surface_rows: 15` | `grep -cE '^\| [0-9]+ \|' reports/round-35/adj/audit-assembled.md` = 15 | **match** |

## 3. Per-counter cross-check of the filed receipt's measurements

Every measurement inside the filed receipt reproduces, either by the clone run
(rows 3) or by an independent direct command of this seat:

| Filed measurement (leg) | Filed value | Observed | Disposition |
|---|---|---|---|
| `C1-C8` `partition_counts` | 21/23/24/29/20/94 | same (row 1) | match |
| `C1-C8` `inventory_files` | 211 | 211 (row 2) | match |
| `C1-C8` `lesson_files` | 33 | `ls corpus/lessons/*.md \| wc -l` = 33 | match |
| `C1-C8` `to_verify_count` | 102 | 102, by the runner's own method `len(re.findall(r"\(to-verify\)", text))` summed over the 10 `NEW_ENTRIES` (per entry: 12/8/1/42/5/18 + 5/2/3/6) | match |
| `C1-C8` `sweep_tail[2]` `readme_sha256` | `51b966af…` | `51b966af…` (row 6) | match |
| `C1-C8` `audits` (C13/C14/C17 present + verdict substance) | all three present, `clean_or_defects` true | all three files exist and match the filed verdict regex | match |
| `O1-O7` `v3_controls` | 44 | 44 by the runner's regex (row 7) | match |
| `O1-O7` `quiet_sha` | `45f57132…` | `45f57132…` (row 8) | match |
| `O1-O7` `renderer_diff_lines` | 126 | `git diff 4a7aede… -- tools/exercise-handoff-e2e.py \| wc -l` = 126 | match |
| `O1-O7` `replay` | exit 1, named true, names_member true, traceback false | same (row 5) | match |
| `CO1-CO9` `baseline_expanded` | `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4` | `git rev-parse 4a7aede^{commit}` = same | match |
| `CO1-CO9` `seat_rows` / `role_counts` / `claim_counts` / `unique_outs` | 64; scout 4, planner 2, connector 1, executor 26, verifier 8, scribe 10, reviewer 9, critic 4; A 15 / C 24 / O 16 / cross 9; true | recomputed from `targets.json` — identical on every field | match |
| `CO1-CO9` `co9` | selftest_exit 0, quiet_exit 0 | both exit 0 | match |
| `A1-A6` `surface_rows` | 15 | 15 (row 12) | match |
| `L1` `files_scanned` | 71 | 71 by the runner's own walk+exclusion rule over `reports/round-35` | match |
| `P1` `corpus_baseline_ok` / `protected_moved` | `201/201`, 0 | `201/201`, 0 (same rule, baseline `4a7aede`) | match |
| `A3` PROVINCE last touch | `c53782a` | `git log -1 --format=%h -- PROVINCE.md` = `c53782a` | match |
| r7 pins (O6) | `packet.md 45f57132…`, `twin.json 0e229138…`, `claims-map.md d181de28…`, `expected.json bbe15887…`, `freeze.txt 3969954b…` | all five reproduce byte-exactly | match |
| `input_sha256` (5 of 7 entries) | claims / targets / dispatch-declared / observed-dispatch / availability-close-35 | all five reproduce byte-exactly | match |

**Note on `v3_controls`.** The selftest's human-readable header reads
"plus 43 controls" while the runner counts `44` lines matching `(?m)^  - `.
The filed value (44) is what the runner's regex produces, so the filed
*measurement* is correct; the header prose undercounts by one because the
first `  - ` line is the "selftest witnesses" line rather than a numbered
control. This is a cosmetic mismatch in the tool's prose, not a recount
mismatch; it is named here rather than smoothed.

## 4. The one observed difference — both entries dispositioned

| Key | Filed | Observed (clone) | Class | Cause |
|---|---|---|---|---|
| `input_sha256["reports/round-35/run-validation.py"]` | `4ed1ae59…` | `9160f093…` | **environmental (this seat's own patch)** | This seat re-pointed the copy's `ROOT` line so the clone could not write to the live tree. The filed digest is the digest of the unpatched runner; `sha256sum reports/round-35/run-validation.py` in the live tree still gives `4ed1ae59386acb8fa17e33dd4d6eba9d7a40581b85f45a33f104529e924bede0`, matching the filed value. No filed value is false. |
| `cross/X1-X3.measurement.manifest` | `"pending-by-construction: integrator files the MANIFEST row in the same close pass"` | `null` (the runner emits `{}` now) | **legitimate-change** | The MANIFEST row has since been filed: `/home/vgpnk/Projects/shokunin/MANIFEST.json` now contains a round-35 closure row (`"round": 35`, `admitted: true`, `closed_at 2026-10-19T06:21:36-03:00`). The filed measurement was correct at its own measurement instant and is superseded by a later filed artifact; it is not drift. |

Everything else in the filed receipt is byte-identical to the clone re-run.

## 5. Filed-byte mutation observed during this seat's run (F-C13-1 recurrence)

Recorded because a calibration seat is the right place to file it. Evidence
kept at `.scratch/ca02/ev/filed-byte-incident.txt`.

- **Window:** 2026-10-19 06:29:35 -0300 → 06:29:59 -0300 (09:29:35Z → 09:29:59Z).
- At 06:29:35 this seat's `git hash-object` read `reports/round-35/validation.json`
  live as `4a8a69f3…` against `HEAD` `11f241a4…` — **content-differing**. The
  `git diff` shape was exactly a runner re-write: `measured_at_utc` bumped
  `06:19:14.685566-03:00 → 06:29:42.347669-03:00`, and `cross/X1-X3.measurement`
  emptied from the `pending-by-construction` string to `{}`.
- At 06:29:59 the same file read back `11f241a4…` == `HEAD`, i.e. **restored**
  within ~24 s (`sha256sum` `328e97b39eff69f45cb23801861ad2e345f8e7b3f7ae5555f1465e8d2c472124`).
- `ps` in the same window listed sibling seats running
  `reports/round-{33,34,35}/run-validation.py` in **default (publishing) mode**
  from `.scratch/x01-iso2`, plus `--check` runs from `.scratch/k03/clone` and
  `.scratch/ca01`. The r35 runner's write path is cwd-relative
  (`out_path = f"{ROUND}/validation.json"`, `reports/round-35/run-validation.py:502`)
  while `ROOT`/`os.chdir` pin the live tree, so an invocation whose cwd is the
  live repo publishes over the filed receipt. Probable writer: a sibling seat,
  **`to-verify`** (not provable from this seat's evidence).
- Full live-vs-HEAD sweep of all 35 filed `validation.json` receipts at 06:30:
  **zero** DIFF rows. Filed bytes are currently intact.
- This seat's negative control: no round runner was ever executed with the live
  repo as cwd. The one archive-directory invocation was `--check` (never
  publishes) and was killed before completing.

**Mechanism note worth carrying to the D block / X00:** `reports/round-33/run-validation.py:23`
uses the relocatable `ROOT = Path(__file__).resolve().parents[2]`, while
`reports/round-34/run-validation.py:10` and `reports/round-35/run-validation.py:9`
hardcode the absolute live path. Rounds 34/35 runners are therefore **not**
isolatable by `git archive` alone, which is precisely what F-C13-1 requires.

## 6. Summary

12 distinct filed counting commands: **10 match**, 2 `could-not-reproduce`
(owner: orchestrator — provider transport results, not seat-observable).
All 19 filed measurement fields inside the receipt reproduce. The only
divergences are this seat's own `ROOT` patch and a since-filed MANIFEST row,
both dispositioned in §4. No mismatch was smoothed.

## Owed

- `reports/round-36/calib/Ca03-ledger-draft.md` is the ledger assembly seat's
  output; this fragment supplies its round-35 rows. This seat did not write it.
- Rows 9 and 10 stay `could-not-reproduce`; the closing owner is the
  orchestrator, and no seat can re-observe an AgentSwarm transport result.

## Citations

- `reports/round-35/claims.json` (sha256 `ccfaafc363981d16729c351fa11135e8082b1b0695dc399884d5c91bcc9e26e4`) — counting_commands for C/O/A.
- `reports/round-35/validation.json` (sha256 `328e97b39eff69f45cb23801861ad2e345f8e7b3f7ae5555f1465e8d2c472124`) — filed measurements.
- `reports/round-35/run-validation.py` (sha256 `4ed1ae59386acb8fa17e33dd4d6eba9d7a40581b85f45a33f104529e924bede0`) — `:9` ROOT, `:36` os.chdir, `:502` write path, `:206` v3_controls regex, `:192` to_verify method, `:248` surface_rows regex, `:315` files_scanned.
- `reports/round-35/telemetry/availability-attempt-{1,2,3}.json`, `observed-dispatch.json` (sha256 `f7a1e1f968a3d7b212e4393e42884675299b458cb891ab5dcc397f35b01c0c53`), `dispatch-declared.json` (sha256 `93e205a2c3dfb8f39b027ae9a50d7bb28459746ce893fc690789d2d8a4bfcd83`), `availability-close-35.json` (sha256 `e51ba5e0aec6e0aca74870691b7db1f51c1bcce68bcd6e94222b7f99a6991d4e`).
- `reports/round-35/adj/audit-assembled.md` (sha256 `13b7ff2f0f659072c0b7a1a655f73d9f0f6434c37d63b64660ea154c43fb68fb`) — 15 surface rows.
- `SCORECARD.md` lines 636-644 — round-35 axis table and re-run commands.
- `/home/vgpnk/Projects/shokunin/MANIFEST.json` — round-35 closure row (`closed_at 2026-10-19T06:21:36-03:00`).
- `/home/vgpnk/Projects/shokunin/.ufo/reports/round-35/kotodama.md` — fleet report (required section headings present).
- `.scratch/ca02/r35-iso-check.json` — clone re-run receipt (exit 0, acceptance true, zero failures).
- `.scratch/ca02/ev/filed-byte-incident.txt` — filed-byte mutation record (§5).
- `.scratch/ca02/ev/filed-byte-mutation.txt` — raw `git status`/`git diff`/hash capture.
- `.scratch/ca02/inv.json`, `.scratch/ca02/v3-selftest.txt`, `.scratch/ca02/replay.out` / `.err` — raw command captures.
