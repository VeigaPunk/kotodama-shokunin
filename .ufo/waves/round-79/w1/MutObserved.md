# MutObserved — observed_at_base off-by-one guard: fixtures and findings (round 79, W1 pre-data)

Base: `44f76d456c1b326a71ffdb381590af825cbf11be`. Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Scope: draft fixtures, mutants and review findings for the O guard's `observed_at_base` cross-check. No production guard, no counter, no ledger, no claim data, no freeze. Pre-data only.

## 1. What was run (observed, not assumed)

- Probe: `stage/MutObserved/mut_observed.py` (draft; sha256 `1395e7d0…243`). Repro in `stage/MutObserved/commands.md`.
- Fixture: an isolated `git init` repo under a fresh scratch dir. Root asserted with `git rev-parse --show-toplevel` before the first commit. No mutation of the lane or fleet repo.
- Truth is derived independently: python over `git show <rev>:<path>` bytes, never the guard's own observer. Hand-written case expectations are self-checked against that truth (self-check: True).
- Two runs were made on the final fixture. Matrix and raw observation bytes were identical (`results.json` / `run.txt`).
- Receipts: `stage/MutObserved/receipts/results.json` and `receipts/run.txt`. Scratch fixture removed after copying; `results.json` still names the removed scratch path.
- Tools: Python 3.14.8 and git 2.56.0, both pre-existing. No installs, no updates, no pacman, no host changes.

Run exit 0. `pristine clean: True | all mutants killed: True | controls behave: True | self-check: True`.

### Raw matrix (from `run.txt`)

```
guard                              result         disagreeing cases
M00_pristine                       CLEAN          -
M01_tolerance_pm1                  KILLED         C04,C05,C07,C08,C11,C13,C15,C17
M02_accepts_obs_minus1             KILLED         C05,C07
M03_le_instead_of_eq               KILLED         C05,C07,C09
M04_obs_prefix_of_rec              KILLED         C02,C09,C19,C20,C21
M05_lexical_ge                     KILLED         C04,C08,C13,C15,C18,C19,C22
M06_stated_compared_not_observed   KILLED         C01,C02,C03,C06,C11,C14,C17,C18,C19
M07_no_green_check                 KILLED         C11,C17
M08_missing_field_skipped          KILLED         C12
M09_token_is_group0                KILLED         C01,C02,C03,C06,C18,C19
M10_first_hit_not_refused          KILLED         C16
M11_reads_worktree_not_rev         KILLED         C01,C02,C03,C06
M12_committed_leading_token        KILLED         C18,C19
M13_prefix_without_boundary        KILLED         C22
C01_control_accept_all             CONTROL-OK     (accepts 14 false cases)
C02_control_reject_all             CONTROL-OK     (rejects 7 truthful cases)
```

### Raw observations at the pinned revs (from `results.json`)

```
B1       rc=0  '<B1>:keys.txt:3\n'
B2       rc=0  '<B2>:keys.txt:13\n'
B1Z      rc=1  ''                          (absence rule -> "0")
B1MULTI  rc=0  '<B1>:keys.txt:3\n<B1>:other.txt:2\n'   (two hits -> must refuse)
S        rc=0  '<B1>:status.txt:PASS legs=12/12\n'
B2-worktree-no-rev rc=0 'keys.txt:14\n'   (uncommitted line; must never be the observation)
```

## 2. The draft rule under test (stated once, in the probe docstring)

1. `observed_at_base` must be present and a string.
2. The recorded text must **state** the observed token. Normalized text equals the token, or starts with it at a non-alphanumeric boundary. So `3 matches in keys.txt` states `3`; `30` does not; `PASS` does not state `PASS legs=12/12`.
3. A `stated_token` equal to the observed token is a green pair and fails.
4. Observation reads committed bytes at a pinned rev. Exactly one parse hit is required; ambiguous output is unobservable, never first-hit.
5. Zero matches is `"0"` only via `git grep` exit 1 with empty stdout.

Items 2 and 4 are proposals for L1 to freeze or reject. Item 1 (absent field fails) is a design decision, flagged as such in case C12.

## 3. Fixture cases (22; hand expectations self-checked against truth)

- Truthful, expect PASS: C01, C02, C03 (exact, prose after boundary, whitespace), C06 (two-digit 13), C14 (zero), C18 (multi-token exact), C19 (multi-token plus prose).
- False, expect FAIL: off-by-one above and below (C04, C05, C07 across tens, C15 at zero), worktree value (C08), prefix truncation (C09, C20, C21, C22 `30` vs `3`), empty (C10), stated=observed green (C11, C17), absent field (C12), recorded=stated but not observed (C13).
- Ambiguity, expect not-PASS: C16 (two-file hit set).

## 4. Findings

### F1 — committed round-76 cross-check compares only the leading token (false negative on truthful records)

`reports/round-76/accept-ca.py` at `44f76d4`, lines 1663–1666:

```
rec = pair.get("observed_at_base")
if isinstance(rec, str):
    lead = (rec.split() or [""])[0]
    if norm(lead) != norm(obs):
```

A truthful record that states a multi-token observed value (`PASS legs=12/12`) is rejected because only `PASS` is compared. Mutant M12 reproduces this rule and is killed by C18 and C19. Truth in C18 and C19 is PASS, and M12 gives NOTPASS.
Impact in committed ledgers was **not checked** [NOT CHECKED]. This finding is about the rule's behaviour on the fixture, not about any filed ledger.

### F2 — committed counter silently skips the cross-check when the field is absent

Line 1664 `if isinstance(rec, str):` and line 1586–1587 (`if rec is not None and not isinstance(rec, str)`): an absent `observed_at_base` is never failed. Mutant M08 is killed by C12. The O guard should require the field; this is a design decision for L1 to confirm.

### F3 — committed counter takes the first regex hit, not exactly one

`reports/round-76/accept-ca.py` line 1330: `m = rx.search(out)`, first hit only. For multi-line output this silently undercounts or takes the first file's value. Mutant M10 is killed only by C16 (two hits, expected refuse). The round-73 draft convention (`.ufo/waves/round-73/w1/drafts/ledger-draft.json` line 8, committed at `44f76d4`) says the observed value is "the number of stdout lines matching parse". That contradicts first-hit. **The O guard must choose one semantics.** The draft refuses ambiguity; a count-of-lines semantic would need an explicit aggregating command.

### F4 — off-by-one coverage

Off-by-one in both directions (M01, M02, M03), at the tens boundary (C07), at zero (C15), and digit-prefix truncation (M04, M13, C09, C22) are each killed by at least one fixture. Several mutants share cases (M02 and M03 both die on C05 and C07), so the matrix shows overlap, not independent proofs. Coverage is adequate for this draft; it is not a proof of guard correctness.

### F5 — worktree trap is distinguishable only by the fixture's uncommitted line

M11 (drops the rev) is killed by truthful B1/B2 cases because the worktree count is 14 while committed B2 is 13. Without the uncommitted line, a worktree-reading guard would pass on the committed bytes and the trap would be invisible. The uncommitted line is therefore load-bearing for C08 and M11.

## 5. Process disclosure

- The first run reported `M00_pristine DIRTY`. The cause was a harness bug: verdicts were normalized to `NOTPASS` while expectations were compared as `FAIL`. Fixed by normalizing the expected side. The receipts here are from the final run; the dirty run is not preserved as evidence.
- A second harness revision added the multi-token key and boundary cases (C18–C22) and mutants M12–M13. All earlier results were superseded by the final matrix.
- No build, lint, or test of any production counter was run. The committed round-76 counter's selftest was **not** run. Statements about it are static reads only, cited by line.

## 6. Not verified / not claimed

- No production O guard exists at base; these fixtures test the draft rule only.
- No claim data, counter freeze, SCORECARD row, or ledger was written.
- Whether any committed ledger record hits F1 is [NOT CHECKED].
- The off-by-one fixtures do not establish that the committed counter's other legs are correct.

## 7. Handoff to L1

- Adopt or reject: boundary rule (item 2), absent-field fail (item 1 / F2), exactly-one-hit (F3), and the multi-token cases C18–C19.
- Freeze the case table with the probe as a committed draft. The probe currently writes scratch fixtures; L1 should decide whether the frozen run is in a materialized clone.
- Expected post-integration checks for L1 (not run by me): re-run `mut_observed.py` on a fresh work dir and confirm the matrix; confirm `pristine clean` before any mutant is treated as killed.

Lane git state after this seat: only the untracked paths `.ufo/waves/round-79/w1/` (this report and `stage/MutObserved/`) were written. No git or jj mutation, no commit, no push.
