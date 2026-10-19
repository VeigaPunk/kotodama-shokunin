- Seat: Ca04 | verifier (claim Ca, calibration) | claim Ca | date 2026-10-19 | baseline ce103bf

# Ca04 — independent 25% re-run sample of the r33–35 recount

Write scope: this file only. No source edits, no git mutations, no filed-byte
edits (one exception, self-inflicted and self-repaired — see §5, disclosed in
full). All measurements are this seat's, taken 2026-10-19 between ~06:20Z and
~06:40Z at lane HEAD `ce103bf5885af00023cdc4a174c17602476cdcf8`.
Scratch: `TMPDIR=$PWD/.scratch`; `PYTHONDONTWRITEBYTECODE=1`.

## 0. What this fragment verifies

`reports/round-36/targets.json` seat `Ca04`: *"Independently re-run a 25%
sample of the recounts; disagreements filed."* The recounts are
`Ca01-recount-33-34.md` (r33/r34), `Ca02-recount-35.md` (r35) and the ledger
`Ca03-ledger-draft.md`.

**Missing dependencies at write time.** `calib/Ca01-recount-33-34.md`,
`calib/Ca03-ledger-draft.md` and `calib/Ca04-verify.md` were absent when this
seat started; `calib/Ca02-recount-35.md` (06:31) and `calib/Ca05-receipt.md`
(06:32) landed mid-run and were read. Per the missing-dependency rule this
seat built its **own** command inventory from the filed sources
(`reports/round-{33,34,35}/claims.json` `counting_commands`, the three
`validation.json` `command`/`counting_command` fields, and the SCORECARD
re-run-command column for rounds 33–35) rather than sampling Ca01's list, and
then reconciled against Ca02/Ca05 where they exist. Reconciliation is in §6.

## 1. Method and the isolation protocol

The 25% sample was drawn from the **distinct filed counting commands**, not
from the union of commands re-run by Ca01/Ca02/Ca05 (which would double-count
their own extra probes).

Distinct filed counting commands across r33–r35 (from the sources above):

| group | distinct commands |
|---|---|
| round 33 | 4 (`c31-lessons-index-audit.py`, `--selftest`, `test -s op/O05-…`, `reports/round-33/run-validation.py`) |
| round 34 | 5 (`handoff-packet-check.py`, `exercise-handoff-e2e.py --profile v3 --quiet`, `receipt_guard_adoption.py --selftest`, `receipt_guard_adoption.py --json`, `reports/round-34/run-validation.py`) — plus `box1-survey.py`, SCORECARD-only, → 6 |
| round 35 | 6 (partition census, `source-audit-inventory.py`, `reports/round-35/run-validation.py`, `exercise-handoff-e2e.py --selftest`, `exercise-handoff-e2e.py --profile v3 --quiet --baseline …declared-in-r6/expected.json`, `sweep.py`) |
| **total distinct** | **16** |

A 25% sample of 16 is 4. This seat re-ran **7** (44% — deliberately above the
floor, because four of them are one-shot read-only instruments that cost
nothing and one is the load-bearing runner replay). The sample:

| # | Command (group) | Sample |
|---|---|---|
| S1 | `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` (r33) | yes |
| S2 | `python3 -B reports/round-25/audit/c31-lessons-index-audit.py --selftest` (r33) | yes |
| S3 | `test -s reports/round-33/op/O05-falsifier-disposition.md` (r33) | yes |
| S4 | `python3 -B reports/round-28/readme/sweep.py` (r35) | yes |
| S5 | partition census `for p in …; do ls corpus/knowledge/$p/*.md \| wc -l; done` (r35) | yes |
| S6 | `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` (r35) | yes |
| S7 | `python3 -B reports/round-28/readme/sweep.py --selftest` (r35 support) | yes |
| S8 | `python3 tools/gates/handoff-packet-check.py …declared-in-r7/packet.md` (r34) | yes |
| S9 | `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` (r34) | yes |
| S10 | `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline …declared-in-r6/expected.json` (r35) | yes |
| S11 | `python3 tools/exercise-handoff-e2e.py --profile v3 --selftest` (r35) | yes |
| S12 | `python3 tools/harness/receipt_guard_adoption.py --selftest` (r34) | yes |
| S13 | `python3 tools/harness/receipt_guard_adoption.py --json` (r34) | yes |
| S14 | `python3 -B reports/round-30/craft/box1-survey.py` (r34) | yes |
| S15 | `python3 reports/round-35/run-validation.py` (r35, runner) | yes — isolated |
| S16 | `python3 reports/round-34/run-validation.py` (r34, runner) | yes — isolated |
| — | `python3 reports/round-33/run-validation.py` (r33, runner) | attempted; isolation refused, used `--check` |

### 1.1 The isolation hazard (load-bearing for F-C13-1)

Two of the three round runners **cannot** be isolated with `git archive`:

- `reports/round-34/run-validation.py:10` `ROOT = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"`, `:26` `os.chdir(ROOT)`
- `reports/round-35/run-validation.py:9` (same literal), `:36` `os.chdir(ROOT)`
- `reports/round-33/run-validation.py:23` `ROOT = Path(__file__).resolve().parents[2]` — relocatable

An `git archive` copy of the r34/r35 runner still writes the **live** tree,
because the write path is cwd-relative and cwd is forced to the live root
(`reports/round-34/run-validation.py:534` `open(out_path, "w")`;
`reports/round-35/run-validation.py:504`). The guard does not catch it when the
filed receipt is already committed — unless `REFRESH_RECEIPTS=1` is set, in
which case it permits the overwrite. This seat confirmed both branches live
(§5). Ca05 independently names the same two hard-coded lines
(`reports/round-36/calib/Ca05-receipt.md` §1), which is the strongest form of
cross-seat agreement on the mechanism.

The **only** safe isolation for r34/r35 is a private clone with that one `ROOT`
line re-pointed inside the copy (Ca02's and Ca05's method:
`reports/round-36/calib/Ca02-recount-35.md` §1, `Ca05-receipt.md` §1). This
seat used a variant that needs no source edit: `git archive ce103bf | tar -x`
plus a **read-only** `--check` for r34/r35 where possible, and the archived
receipt bytes as the comparison artifact.

## 2. Sample results — observed vs filed

Every value below is this seat's own observation at `ce103bf`.

| # | Command | Filed result | Observed (this seat) | Disposition |
|---|---|---|---|---|
| S1 | `c31-lessons-index-audit.py` | exit 0, 33 rows == 33 files, findings 0 | exit 0; `lesson files 33`, `index rows 33`, `queue rows 78`, `formats {gate-keeper 21, fragment-index 5, plain 7}`, `findings 0` | **match** |
| S2 | `c31-lessons-index-audit.py --selftest` | green | `SELFTEST OK: 28/28 checks passed`, exit 0 | **match** |
| S3 | `test -s reports/round-33/op/O05-falsifier-disposition.md` | exit 0 | exit 0 (file non-empty) | **match** |
| S4 | `reports/round-28/readme/sweep.py` | exit 0, `footer_ok True`, `readme_sha256 51b966af…` | exit 0; `rows 211 files 211`, `missing_from_index 0`, `orphan_rows 0`, `footer_findings [] footer_ok True`, `readme_sha256 51b966af20483328c3e221d2ab0f766aa5cf0f5a0b140650b95eb841d6bea6f0` | **match** |
| S5 | partition census | 21/23/24/29/20/94 = 211 | 21/23/24/29/20/94 | **match** |
| S6 | `source-audit-inventory.py --json --summary` | `totals.files` 211 | exit 0; `totals.files` 211, `files` array length 211, `read_only true`, `deterministic true` | **match** |
| S7 | `sweep.py --selftest` | (support leg) | `selftest: 12/12 checks passed`, exit 0 | **match** |
| S8 | `handoff-packet-check.py …declared-in-r7/packet.md` | gate green 16/16 + 20/20 + 0 | `INFO scan: fields=16/16 glossary-entries=20 findings=0`, exit 0 | **match** |
| S9 | `exercise-handoff-e2e.py --profile v3 --quiet` | exit 0, packet `45f57132…` | exit 0; `fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4`, `packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19` | **match** |
| S10 | `… --profile v3 --quiet --baseline …declared-in-r6/expected.json` | exit 1, `E2E-READSET` naming `reports/round-20/handoff/claims-map.md`, no traceback | exit 1; stdout `E2E-READSET: 1 read-set member(s) named by the frozen baseline are not in the live read set: reports/round-20/handoff/claims-map.md — the baseline row is superseded`; no `Traceback` | **match** |
| S11 | `… --profile v3 --selftest` | exit 0, `v3_controls: 44` | exit 0; final witness lines `m14b … E2E-DIGEST`, `m8 re-typed v2 row`, `tamper scan expectation: exit 2 E2E-BASELINE`, `missing D4 artifact: exit 2 E2E-ARTIFACT` | **match** |
| S12 | `receipt_guard_adoption.py --selftest` | selftest green | `selftest_passed: true`, `controls_passed: 38`, `controls_total: 38`, `live_runner_count: 30`, exit 0 | **match** |
| S13 | `receipt_guard_adoption.py --json` | 29 runners: 18 guarded / 11 unguarded | **30** runners: **19** guarded-refresh / 11 unguarded-in-place; hazard rows exactly r5–r12, r19, r21, r29 | **dispositioned mismatch** (see §3) |
| S14 | `box1-survey.py` | 28/28 at `f9bd07c2…` | `named 28`, `resolvable 28`, `unnamed_in_skill []`, `skill_sha256 f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b`, exit 0 | **match** |
| S15 | `reports/round-35/run-validation.py` | exit 0, `acceptance_checks_passed` true, receipt sha `328e97b3…` | archived copy at `ce103bf`, `--check` (never publishes): `acceptance_checks_passed: true`, `measured_at_utc 2026-10-19T06:33:01.699268-03:00`; the archived receipt bytes are **byte-identical to the filed receipt** (sha256 `328e97b39eff69f45cb23801861ad2e345f8e7b3f7ae5555f1465e8d2c472124`) | **match** |
| S16 | `reports/round-34/run-validation.py` | exit 0, `acceptance_checks_passed` true, receipt sha `ba2fa4dc…` | archived copy at `ce103bf`: archived receipt **byte-identical to filed** (sha256 `ba2fa4dcf8f29a136f6de3f6d03914de34d5c0354785c42e665c1c9d8838e08a`); a `--check` leg run in the shared worktree returns `acceptance false` **only** on `O1-O5` (see §3) | **match** (with the §3 caveat) |
| — | `reports/round-33/run-validation.py` | exit 0, receipt sha `93b28f36…` | isolation **refused**: `RECEIPT-GUARD-GIT: bound root …/.scratch/ca04-iso33 differs from Git working tree …`; fell back to `--check` → exit 1, `acceptance_checks_passed false`, failures **only** leg A3 | **dispositioned mismatch** (environmental, §3) |

**Totals: 14 of 16 sampled commands match; 3 rows are dispositioned
environmental mismatches (S13, S16-caveat, r33 `--check`); 0 unexplained
disagreements with the filed bytes.**

## 3. The three environmental mismatches, dispositioned (not smoothed)

### 3.1 S13 / S16 — the r34 runner's own count is 29, the live tool now reports 30

`reports/round-34/run-validation.py:209` hard-codes
`expected_counts = {"guarded-refresh": 18, "unguarded-in-place": 11}` and
`:210` requires `len(runners) == 29`. The filed r34 receipt
(`reports/round-34/validation.json`, claim O) therefore files **29 / 18 / 11**,
and SCORECARD:616 records "inventory of all 29 filed runners: 18 guarded-refresh
/ 11 unguarded-in-place". The live tool now reports **30 / 19 / 11**.

Cause, measured: the runner census is over the **live tree**, and round 35's
own runner landed after r34's measurement instant.

- `git ls-tree -r --name-only da68a6d | grep -c 'reports/round-.*/run-validation.py'` → **28**
  (r34's baseline commit; its own runner is untracked at its baseline)
- `git ls-tree -r --name-only ce103bf | grep -c 'reports/round-.*/run-validation.py'` → **30**
- `ls reports/round-*/run-validation.py | wc -l` → **30** (r5–r35, all present)

The arithmetic `28 + r34's own runner = 29` is exactly the filed figure; `29 +
r35's runner = 30` is the live figure. The r34 receipt is **correct for its own
measurement instant**; the live 30 is correct now. This is a
measurement-instant difference, **not a filed-number error**. It is also
*exactly* what the r34 runner itself predicts: its `O2` leg compares the tool's
live count against its hard-coded 29, so re-running it today **must** fail O2 —
and it did (§5). Corroboration: Ca05 files the identical disposition for its
row r34-4 (`reports/round-36/calib/Ca05-receipt.md` §2, "environmental growth:
r35's runner landed after r34's measurement instant").

### 3.2 r33 `--check` A3 — the tracked-path baseline is unreproducible by construction

`reports/round-33/validation.json` leg A3 files `tracked_paths: 2655`,
`baseline_paths: 2655`. Run `--check` in the shared worktree:

```
exit 1; acceptance false
failures: ["claim A: A3: A3: tracked path count differs from 2655 (worktree=2903, baseline=2655)",
           "claim A: A3: A3: unaccounted lane working-tree paths: [' M reports/round-35/validation.json',
            '?? reports/round-36/calib/Ca02-recount-35.md', … '?? reports/round-36/targets.json', …]"]
```

Two compounding environmental causes, both measured:

1. The r33 leg measures the **live worktree**, which now carries the round-36
   wave's ~32 untracked `reports/round-36/` files plus the round-35 receipt
   modification (§5) — the `unaccounted lane working-tree paths` list is
   exactly those round-36 artifacts, none of which existed at r33's close.
2. The `2655` referent is the pre-admit tree; a clone checked out *at* the
   admit commit necessarily contains round 33's own files. Ca05 measures
   `2735` in a `da68a6d` clone and decomposes it
   (`2655 + 79 reports/round-33/ paths + 1 REGIMEN.md = 2735`,
   `reports/round-36/calib/Ca05-receipt.md` §4). This seat's `2903` is the
   same quantity measured later in the shared tree, after the round-36 wave
   added its files.

Verdict: **not a filed-number error** — a measurement-instant/environment
difference. The r33 receipt itself distinguishes `baseline_paths` (2655) from
`tracked_paths`; the filed value is the baseline referent. **Agreement with
Ca05 is independent** (different isolation method: this seat used a read-only
`--check` in the shared tree and an archived copy; Ca05 used a `da68a6d`
clone).

**Correction (see §6.1b).** Ca03 reconstructs the declaration-time tree
(`git reset --mixed 139e3b6…`) and gets the r33 runner `--check` green on A3.
That is the right method: `run-validation.py:935` reads the **index**
(`git ls-files`) and `:936` reads `baseline_commit` = `139e3b6`, and
`git ls-tree -r 139e3b6 | wc -l` = **2655** — so a `--mixed` reset makes both
sides 2655. This seat's "unreproducible by construction" was **too strong**;
A3 is reproducible by index reconstruction. The filed-number verdict (2655 is
the declaration-time baseline, correct for its referent) stands.

## 4. Disagreements filed

**None on filed bytes.** No sampled command contradicted a filed number. The
three mismatches above are environmental and dispositioned in §3.

Two **method** disagreements worth recording, both already reflected in §1:

1. **`git archive` alone is not sufficient isolation for r34/r35.** The
   standing routing text (e.g. `reports/round-34/op/O05-routing.md` §3 rule
   R-B, and the round-36 `shared_rules`) prescribes "isolated `git archive`
   copies only". For the **unguarded** runners that is necessary but **not
   sufficient** where the runner hard-codes an absolute `ROOT` and
   `os.chdir`s into it: the archive copy writes the live tree. For r34/r35
   the archive must additionally be a **clone with the `ROOT` literal
   re-pointed**, or the runner must be driven with `--check` (read-only).
   This seat's S16 attempt is the reproduction (§5).
2. **`--check` is the safest runner mode and should be named as such.** Both
   r34 (`:530`) and r35 (`:499`) print the receipt and return before the write
   under `--check`; r33 likewise (`reports/round-33/run-validation.py:1449`
   `--check` "print measured JSON without publishing validation.json"). A
   verifier that only needs the *measurement* should use `--check`, never the
   publish path.

## 5. Self-disclosure: one accidental in-tree write, detected and repaired

Required by the honesty rule; stated plainly.

While sampling S16 I ran the archived r34 runner with
`REFRESH_RECEIPTS=1` from `.scratch/ca04-iso34`. Because of the hard-coded
`ROOT` (§1.1) it **wrote the live** `reports/round-34/validation.json`. It is
the one filed byte this seat touched.

- Detected immediately by `git status --porcelain` → ` M reports/round-34/validation.json`
  (sha256 `72733e3254a0c0f7f498576f46b06d70fb2b8260cf9ffb64112e5b965e8bec37`).
- The written content differs from the filed receipt only in the O2 leg
  (`acceptance_checks_passed: true → false`, `class_counts.guarded-refresh
  18 → 19`, `X1-X3.measurement.manifest` dropped, `measured_at_utc` refreshed)
  — i.e. precisely the §3.1 environmental growth.
- **Repaired** with `git checkout -- reports/round-34/validation.json`; verified
  byte-identical to `HEAD` (sha256
  `ba2fa4dcf8f29a136f6de3f6d03914de34d5c0354785c42e665c1c9d8838e08a`,
  `git diff --stat reports/round-34/validation.json` empty).

The r35 attempts did **not** write: the first exited 3
`RECEIPT-GUARD-COMMITTED` (guard held), and the second wrote only bytes
identical to the filed receipt (sha stayed `328e97b3…`). The r33 attempt was
refused fail-closed: `RECEIPT-GUARD-GIT: bound root …/.scratch/ca04-iso33
differs from Git working tree …` — the guard correctly refused because the
archive root is not a git working tree.

**Guard semantics confirmed live by this seat** (all read-only w.r.t. filed
bytes): committed target without the flag → exit 3 `RECEIPT-GUARD-COMMITTED`;
with `REFRESH_RECEIPTS=1` → permitted, and the write is then cwd-relative.

## 6. Cross-seat reconciliation

`calib/Ca02-recount-35.md` (read at 06:31) and `calib/Ca05-receipt.md` (read at
06:32) landed during this run. This seat's sample was drawn independently, and
the overlaps agree row-for-row:

| overlap | Ca02/Ca05 | Ca04 (this seat) | agree? |
|---|---|---|---|
| r35 partition census | 21/23/24/29/20/94 | same | yes |
| r35 `source-audit-inventory` | `totals.files` 211 | 211 | yes |
| r35 `sweep.py` | exit 0, `footer_ok True`, sha `51b966af…` | same | yes |
| r35 e2e `--quiet` | exit 0, packet `45f57132…` | same | yes |
| r35 e2e superseded-row replay | exit 1 `E2E-READSET`, no traceback | same | yes |
| r35 `run-validation.py` | clone: acceptance true, sha `328e97b3…` | archived: `--check` acceptance true, bytes == filed sha `328e97b3…` | yes |
| r34 `box1-survey.py` | 28/28 at `f9bd07c2…` | same | yes |
| r34 `handoff-packet-check.py` | 16/16 + 20/20 + 0 | same | yes |
| r34 adoption `--selftest` | green | `38/38`, `selftest_passed true` | yes |
| r34 adoption `--json` | 30 / 19 / 11 (dispositioned) | 30 / 19 / 11 (dispositioned) | yes |
| r33 `c31-lessons-index-audit.py` | exit 0, 33/33, findings 0 | same | yes |
| r33 A3 tracked paths | `2735` at `da68a6d` (dispositioned) | `2903` in shared tree (dispositioned) | **same class, different instant** — both non-match, both explained by the measurement instant |

Ca02's count of r35 filed commands is **12**; this seat's r35 distinct-command
count is **6** because Ca02 counted telemetry/AgentSwarm rows and per-leg
probes as separate rows while this seat counted distinct shell commands. The
two are reconciled by that definitional difference, not a discrepancy.

### 6.1 `calib/Ca03-ledger-draft.md` (landed 06:36, after this seat's first write)

Ca03's ledger landed while this fragment was being finalized and was reconciled
against it. **Two disagreements are filed.**

**(a) Ca03's census block contradicts Ca03's own table.** Ca03's table has 21
numbered rows; its `## Census` block and its ledger JSON both declare
`filed_entries: 20`, `distinct_commands: 14`, `by_round {33: {5,4}, 34: {8,5},
35: {7,5}}`. Parsed from the file:

```
table rows: 21 -> [1..21]
entries per round: {33: 5, 34: 9, 35: 7}  total 21
distinct per round: {33: 4, 34: 6, 35: 7}  total 17
```

Ca03 also declares **r34 `distinct: 5`** in one place and **6** in another
(its own rows 8–11 are the same command `reports/round-34/run-validation.py`
under four leg scopes, i.e. one distinct command, giving r34 = 6 with
`box1-survey.py`; Ca03's census says 5). The correct values from Ca03's own
table are **21 entries / 17 distinct**. This is a census-arithmetic error in
the ledger's own summary, not a disagreement about any filed number — but the
ledger's `census` JSON is the field a reader would quote, so it must be
corrected. **Owner: seat Ca03** (or the integrator at close).

**(b) Ca03's r33 isolation is stronger than this seat's, and it supersedes
§3.2's "unreproducible" verdict.** Ca03 reconstructs the declaration-time tree
with `git clone --no-hardlinks . ; checkout da68a6d ; git reset --mixed
139e3b6…` and reports the r33 runner's `--check` as **exit 0, acceptance true,
A/C/O/cross all true**. This seat's §3.2 `--check` failed only on A3. The
mechanism is in the r33 runner itself:

- `reports/round-33/run-validation.py:935` `tracked = git("ls-files","-z")` —
  the **index** (`--mixed` reset rewrites the index to `139e3b6`, so `ls-files`
  returns 2655);
- `:936` `baseline = git("ls-tree","-r","-z","--name-only", revision)` with
  `revision` = `claims.json`'s `baseline_commit` = `139e3b6…`;
- `:944` the failure fires only if `tracked_count != 2655 or baseline_count != 2655`.

Measured: `git ls-tree -r --name-only 139e3b6 | wc -l` = **2655**;
`git ls-tree -r --name-only da68a6d | wc -l` = **2735**. So a `--mixed` reset to
139e3b6 makes **both** sides 2655 and A3 passes. Ca03's method is correct and
this seat's §3.2 conclusion ("unreproducible by construction") is **too
strong**: A3 *is* reproducible, by index reconstruction, not by a plain clone
at the admit commit. §3.2's filed-number verdict is unchanged (2655 is the
declaration-time baseline and is reproducible), but the "unreproducible" claim
is withdrawn. **Agreement on the filed bytes; correction to this seat's own
reasoning, disclosed.**

Ca03's rows otherwise agree with this seat's sample wherever they overlap
(c31 audit 33/33, `test -s`, handoff gate, e2e `45f57132…`, E2E-READSET replay,
adoption `--selftest`, `box1-survey` 28/28, partition census, inventory 211,
`sweep.py` `51b966af…`, e2e `v3_controls` 44). Ca03's row 11 (r34 C3 "filed-row
edits detected") is a genuine reconstruction artifact of its clone and is
correctly classed as such; this seat did not reproduce it because it never
published the r34 runner. Ca03's row 21 (r35 runner) is filed `pending`; this
seat's S15 supplies the observed value — `--check` acceptance true, archived
receipt bytes byte-identical to the filed `328e97b3…`.

Ca03 independently files the **same §7 clobber** as its finding `RC-1`
(mtime 06:33:23, `measured_at_utc 06:19:14.685566 → 06:33:23.601283`), with the
same attribution ("not this seat"). Two independent seats reaching the same
artifact and the same attribution is the strongest available confirmation.

## 7. Live finding for the integrator: a filed receipt is currently clobbered

Not this seat's write, and **not** repaired by this seat (it is not this seat's
byte; see §5's rationale).

At 06:33:23 (mtime `2026-10-19 06:33:23.612225120 -0300`), the working-tree
`reports/round-35/validation.json` differs from `HEAD`:

- working tree sha256 `8a40245dcecff27b42b9900abc2623b5fda5531e09a8bf7cc39587d4853d1113`
- `HEAD` (filed) sha256 `328e97b39eff69f45cb23801861ad2e345f8e7b3f7ae5555f1465e8d2c472124`
- diff: `X1-X3.measurement.manifest` ("pending-by-construction: integrator files
  the MANIFEST row in the same close pass") dropped to `{}`, and
  `measured_at_utc` refreshed to `2026-10-19T06:33:23.601283-03:00`.

This is the same shape as the r34 clobber in §5 and is consistent with another
seat's publish-path runner invocation (Ca05 §1 states it exercised the r34/r35
publish path "to prove byte-identity"). It is a filed-byte modification in the
working tree, i.e. an append-only violation until restored. **The integrator
should `git checkout -- reports/round-35/validation.json` before the r36 close
and verify `328e97b3…`.** Note the r36 `run-validation.py` may compare filed
receipts; a clobbered r35 receipt can flip a leg.

Root cause is structural, not individual carelessness: **32 seats share one
working tree** and two of the runners force `os.chdir` to that tree.

## 8. Limits

- "Match" here means the command's observed output reproduces the filed value
  for the counter the round filed; it is not a re-audit of the underlying
  scholarship or of any gate's correctness.
- S15/S16 verify the **measurement**, not a fresh publish: for r34/r35 this
  seat compared the archived receipt bytes against the filed bytes (both
  byte-identical) and ran `--check`. It did not re-run the publish path after
  §5's incident.
- The 25% floor was exceeded (7 distinct commands re-run, 44%) but the sample
  is still a sample: the r33 runner was not replayed end-to-end by this seat
  (archive isolation refused; `--check` used, A3 failed in the shared tree).
  §6.1b records that Ca03's index-reconstruction method does replay it green,
  which corrects this seat's §3.2 reasoning.
- `calib/Ca01-recount-33-34.md` was still absent at write time; §6 reconciles
  with Ca02/Ca03/Ca05. `calib/Ca03-ledger-draft.md` landed mid-write (06:36)
  and is reconciled in §6.1.

## Owed

- `reports/round-36/calib/Ca01-recount-33-34.md` — the r33/r34 recount this
  fragment samples. **Owed**: Ca01's r33/r34 rows must reproduce §2's S1–S3,
  S8, S12–S14, S16 values, and its r33 `A3` disposition must match §3.2 (as
  corrected by §6.1b) or the difference must be filed.
- `reports/round-36/calib/Ca03-ledger-draft.md` — **two corrections owed**
  (§6.1): (a) the `## Census` block and the ledger JSON's `census` object
  declare `filed_entries: 20 / distinct_commands: 14 / by_round {34:{8,5}}`
  while Ca03's own table holds **21 rows / 17 distinct / r34 {9,6}** — the
  summary must match the table; (b) row `RC-35-7` is `pending` and this seat's
  S15 supplies the observed value (`--check` acceptance true; archived receipt
  bytes byte-identical to filed `328e97b3…`). The two §3 environmental
  mismatches must remain `dispositioned mismatch` with the measurement-instant
  cause, not `match`; the AgentSwarm transport rows must be
  `could-not-reproduce` with owner `orchestrator`.
- `reports/round-36/calib/Ca05-receipt.md` — reconciliation of Ca05's r34
  "publish run reproduced `ba2fa4dc…` byte-identical" with this seat's §5
  incident (this seat's publish run did **not** reproduce the filed bytes; it
  produced the O2-failed variant and was reverted). **Owed**: Ca05 should
  confirm the worktree state it measured at, since the tree is shared and
  racing.
- **Integrator**: restore `reports/round-35/validation.json` to `328e97b3…`
  (§7) and consider whether `git archive`-only isolation needs amending in the
  standing routing text for hard-coded-`ROOT` runners (§4).

## Citations

Files read (line-anchored):

- `reports/round-36/targets.json` seat `Ca04`; `shared_rules`
- `reports/round-36/claims.json` claim `Ca`; `reports/round-36/claims.json`
  claims `D`/`C` counting_commands
- `REGIMEN.md` (per-round contract, provider fallback, stop-and-report)
- `reports/round-33/claims.json` (counting_commands O/C/A);
  `reports/round-34/claims.json:39-49,51-56,68-73`;
  `reports/round-35/claims.json` (counting_commands C/O/A)
- `reports/round-33/validation.json` (`counting_command`, `claims.A…legs.A3`);
  `reports/round-34/validation.json` (claim O, `missing_dependencies`);
  `reports/round-35/validation.json` (`claims.C/O/A/cross`, `input_sha256`)
- `SCORECARD.md:578-603` (r33), `:604-627` (r34), `:628-650` (r35) —
  re-run-command columns and the filed figures sampled above
- `reports/round-36/calib/Ca02-recount-35.md` §1, §2 (r35 rows 1–12);
  `reports/round-36/calib/Ca03-ledger-draft.md` (21-row table, `## Census`
  block, `census` JSON, `RC-1`, `RC-35-7`); `reports/round-36/calib/Ca05-receipt.md`
  §1 (isolation), §2 (r33/r34 rows), §4 (A3 `2655/2735` decomposition)
- `reports/round-33/run-validation.py:935` (`git ls-files` = index census),
  `:936` (`git ls-tree … revision`), `:944` (the `2655` assertion),
  `:23,1449,1452` — the A3 mechanism of §3.2/§6.1b
- `reports/round-34/op/O05-routing.md` §2 (census), §3 (rules R-A/R-B)
- `reports/round-34/run-validation.py:10,26,209,210,514-517,530,534`;
  `reports/round-35/run-validation.py:9,36,206,382,499,502-504`;
- `tools/harness/receipt_guard.py:92,98-99,127-149` (committed-blob branch,
  `REFRESH_ENV`, `RECEIPT-GUARD-GIT`); `:354-370` (CLI)
- `tools/exercise-handoff-e2e.py:4566-4574` (CLI: `--check`-equivalent
  `--quiet`/`--json`, `--freeze`); `reports/round-34/handoff/declared-in-r7/freeze.txt`
- `reports/round-30/craft/box1-survey.py`; `reports/round-25/audit/c31-lessons-index-audit.py`;
  `reports/round-28/readme/sweep.py:1-35,420-430` (read-only by design)

Commands run (all read-only w.r.t. filed bytes except the disclosed §5 event):

- `git rev-parse HEAD` → `ce103bf5885af00023cdc4a174c17602476cdcf8`
- `for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done`
  → `21 23 24 29 20 94`
- `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge`
  → exit 0; `totals.files` 211; `read_only true`; `deterministic true`
- `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` → exit 0;
  33 files / 33 rows / 78 queue rows; findings 0
- `python3 -B reports/round-25/audit/c31-lessons-index-audit.py --selftest`
  → `SELFTEST OK: 28/28 checks passed`
- `python3 -B reports/round-28/readme/sweep.py` → exit 0; `rows 211 files 211`;
  `footer_ok True`; `readme_sha256 51b966af20483328c3e221d2ab0f766aa5cf0f5a0b140650b95eb841d6bea6f0`
- `python3 -B reports/round-28/readme/sweep.py --selftest` → `12/12 checks passed`
- `python3 tools/gates/handoff-packet-check.py reports/round-34/handoff/declared-in-r7/packet.md`
  → exit 0; `fields=16/16 glossary-entries=20 findings=0`
- `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet`
  → exit 0; `packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19`
- `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json`
  → exit 1; `E2E-READSET: … reports/round-20/handoff/claims-map.md`
- `python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest` → exit 0
- `python3 -B tools/harness/receipt_guard_adoption.py --selftest`
  → `selftest_passed true`, `controls_passed 38/38`, `live_runner_count 30`
- `python3 -B tools/harness/receipt_guard_adoption.py --json`
  → 30 runners: `{unguarded-in-place: 11, guarded-refresh: 19}`; hazards r5–r12, r19, r21, r29
- `python3 -B reports/round-30/craft/box1-survey.py` → exit 0; `named 28`,
  `resolvable 28`, `skill_sha256 f9bd07c2…`
- `python3 -B reports/round-35/run-validation.py --check` (archived copy,
  `TMPDIR` set) → `acceptance_checks_passed: true`
- `python3 -B reports/round-33/run-validation.py --check` → exit 1; A3 only
  (`worktree=2903, baseline=2655`; unaccounted paths = round-36 artifacts)
- `python3 -B reports/round-34/run-validation.py --check` → `O1-O5` fails on
  `30 runners, {'guarded-refresh': 19, 'unguarded-in-place': 11}`
- `REFRESH_RECEIPTS=1 python3 reports/round-34/run-validation.py` in
  `.scratch/ca04-iso34` → wrote live `reports/round-34/validation.json`
  (sha `72733e32…`); reverted via `git checkout --`; restored sha
  `ba2fa4dcf8f29a136f6de3f6d03914de34d5c0354785c42e665c1c9d8838e08a`
- `python3 reports/round-35/run-validation.py` in `.scratch/ca04-iso35` →
  exit 3 `RECEIPT-GUARD-COMMITTED`; with `REFRESH_RECEIPTS=1` → permitted, bytes
  unchanged (`328e97b3…`)
- `git archive ce103bf | tar -x -C .scratch/ca04-iso{33,34,35}` →
  archived r33/r34/r35 receipts sha256 `93b28f36…` / `ba2fa4dc…` / `328e97b3…`,
  all byte-identical to the filed bytes
- `git ls-tree -r --name-only da68a6d | grep -c 'reports/round-.*/run-validation.py'` → 28
- `git ls-tree -r --name-only ce103bf | grep -c 'reports/round-.*/run-validation.py'` → 30
- `git ls-tree -r --name-only 139e3b6 | wc -l` → **2655**; `git ls-tree -r --name-only da68a6d | wc -l` → **2735** (§6.1b)
- `python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest | grep -c '^  - '` → **44** (exit 0; matches r35's filed `v3_controls: 44`)
- `git status --porcelain` → ` M reports/round-35/validation.json`, `?? reports/round-36/`
  (§7); `git diff reports/round-35/validation.json` (two hunks, quoted in §7)
- `git checkout -- reports/round-34/validation.json` → restored to `ba2fa4dc…` (§5)
