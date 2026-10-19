- Seat: P01 | planner | Ca | date 2026-10-19 | baseline 57c8409

# Ca recount plan

## Assignment rule

Use K01's inventory as the controlling row set; preserve one row per filed command/result occurrence, including repeated runner strings for different claims or legs. Key each assignment by K01's row ID (or, if absent, by round + claim/leg + occurrence), not by deduplicated command text. Route rows by the receipt they originate from:

| Inventory row source | Executor | Assignment |
|---|---|---|
| Round 33 validation receipt | Ca01 | Every r33 command/result row, including nested commands in the receipt and claim-scoped runner rows. |
| Round 34 validation receipt | Ca02 | Every r34 command/result row, including the runner rows and the rejected/failed outcomes if any are filed. |
| Round 35 validation receipt | Ca03 | Every r35 command/result row. |
| Round 36 validation receipt | Ca04 | Every r36 command/result row, including the failed D leg and the rejected round outcome; recount the filed failure as filed, do not repair or reinterpret it. |
| Cross-round command not owned by a single receipt row | Ca05 | Only the additional cross-cutting commands named in its mission (c31 lessons audit, box-1 survey, sweep, adoption inventory, renderer selftests). If K01 already assigns an occurrence to a specific round receipt, that round's executor owns it; do not duplicate it in Ca05. |

Ca06 assembles all executor rows to the declared ledger schema. Ca07 and Ca08 each independently re-run a separately selected, disjoint sample of at least `ceil(N/4)` inventory rows, balanced across rounds and command types; record the frozen sample row IDs before running. Ca09 checks set equality and exactly-once coverage against K01. Ca13 checks every mismatch has an explicit cause; Ca16 strict-parses the final ledger and confirms its row count and digests. Spare seats fill only named uncovered rows. These assignments follow the r37 seat missions and the required coverage and independent-sample thresholds.

## Isolated runner protocol

1. Use only the exact acceptance command and filed result/source pointers from K01 and the round receipt. Keep runner rows separate by claim/leg even where their command strings are identical. Capture stdout, stderr, exit status, relevant structured fields, run date, and the source revision in `.scratch`.
2. A runner may be executed only from a fresh `git archive` extraction under `.scratch`, never from the live checkout. Before execution, inspect the archived runner and its helpers for absolute-root changes, `chdir`, subprocess paths, receipt writes, and Git discovery. Confirm every input and output resolves inside the isolated copy or `.scratch`; ensure a copy under `.scratch` cannot discover the live checkout's `.git`. Do not set `REFRESH_RECEIPTS=1` or use any publishing path.
3. Run only a verified non-publishing/check mode, and only after the path audit proves the runner reads the isolated copy. `--check` alone is not isolation: the filed r34/r35 runners hard-code the live repository root and `chdir` there, so an archived copy can still read/write live paths. If a runner cannot be made safely self-contained without changing the measured source or escaping the archive, do not execute it; file `could-not-reproduce` with the responsible owner and concrete reason. Never use an in-tree `reports/round-*/run-validation.py` invocation.
4. Compare the observed result with the filed result at the same row granularity. For a rejected round, reproduction means confirming its filed failed leg and rejection, not making it green. Keep each command's full output/evidence in scratch for the integrator; the durable ledger cites the command output and original receipt.

## Disposition vocabulary

- `match`: the observed result reproduces the filed result (include the compared exit status and measurements).
- `dispositioned-mismatch`: observed differs; name the exact differing field, cause, and mismatch class (`legitimate-change`, `environmental`, or `reconstruction-artifact` where supported by evidence). Do not smooth or silently normalize it.
- `could-not-reproduce`: command was not safely or technically reproducible; include a named owner and specific reason. This is not a match and must remain visible in coverage counts.
- Use `to-verify` for any unsupported cause/class, and leave it unresolved rather than infer a result.

## Owed

- `reports/round-37/scout/K01-command-inventory.md` was not present when this plan was drafted. The exact row IDs, complete command list, and filed-result coverage therefore remain owed; apply the source-round routing above once K01 lands. No runner was executed for this plan.

## Citations

- `REGIMEN.md:25-43` — recount and round admission requirements.
- `reports/round-37/claims.json:12-18` — Ca's coverage, disposition, and verifier-sampling requirements.
- `reports/round-37/targets.json:15,19-34` — P01 mission and Ca executors, verifiers, assembly, and audit seats.
- `reports/round-37/targets.json:23-28` — cross-cutting Ca05 mission, Ca06 schema, independent verifiers, and coverage checker.
- `reports/round-33/validation.json:4-8,1184-1184`; `reports/round-34/validation.json:5-8,167-167`; `reports/round-35/validation.json:5-8,199-199`; `reports/round-36/validation.json:4-8,144-167` — receipt claim commands, round outcomes, and r36 rejection.
- `reports/round-36/validation.json:49-78,145-165` — r36 D leg's filed failure and rejected status; preserve as a recount target.
- `reports/round-36/calib/Ca04-verify.md:69-90,198-212` — r34/r35 hard-coded-root hazard, archive-only isolation limitation, and check-mode caveat.
- `reports/round-36/calib/Ca02-recount-35.md:15-23` — r35 runner root behavior and prior isolation handling.
- `reports/round-36/calib/Ca03-ledger-draft.md:79-81` — prior disposition vocabulary and mismatch classes.
