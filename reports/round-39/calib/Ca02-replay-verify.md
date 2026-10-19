- Seat: Ca02 | verifier | Ca | date 2026-10-19 | baseline dfb0719

# Ca02 — protocol replay-verification of reports/round-34/run-validation.py --check

## Verdict: REPRODUCED

All four `could-not-reproduce` rows for round 34 in the r37 recount ledger
(`R37-Ca-05` C, `R37-Ca-06` D, `R37-Ca-07` O, `R37-Ca-08` cross;
`reports/round-37/calib/recount-ledger.json:60-111`) are **reproduced under
the isolation-replay protocol**: the filed results `passed=true; failures=[];
round accepted` (`reports/round-34/validation.json:2,5-9,25,27-30,45,47-50,65,67-71,159`)
re-emerge normalized-identical at the r34 close commit in a git worktree.
The r37 `could-not-reproduce` dispositions are not sustained; their stated
cause (absolute-root `chdir`, the O12 isolation hazard) was re-demonstrated
as the negative control, not as evidence against the round.

## Protocol mechanics as applied (claims.json-declared: worktree at close commit, relative-root requirement, TMPDIR isolation)

1. Worktree at the close commit: `git worktree add --detach .scratch/ca02-wt-r34 4a7aede`
   → HEAD `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4` (r34 admit commit; full sha
   from `git rev-parse HEAD` in the worktree). Worktree clean before and after
   both runs (`git status --porcelain` empty in the worktree).
2. Runner identity: `sha256sum` of `reports/round-34/run-validation.py` is
   `be11ff46f1fe399cbedcba956d39134a39e25fcfbb74e4b3dc958f2ab47090f9`
   identically at the live HEAD, at `4a7aede` (`git show 4a7aede:… | sha256sum`),
   and in the worktree — equal to the filed `runner_sha256`
   (`reports/round-34/validation.json:196`). `git diff --stat 4a7aede HEAD --
   reports/round-34/` is empty: filed r34 bytes did not move.
3. Replay copy (the relative-root requirement): one line changed, no other
   byte — `ROOT = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"`
   (`reports/round-34/run-validation.py:10`) → `ROOT = os.getcwd()`, so the
   `os.chdir` at `:26` binds to the launch directory instead of escaping to
   the live checkout. Diff is exactly `10c10` on that pair.
   Digests: pristine `be11ff46…0f9`, replay copy
   `46e55b803dbb0b2b1f42ea9ef06617b98000336297510624016457e6f694ce63`
   (copy at `.scratch/ca02-wt-r34/.scratch/ca02/replay-runner.py`).
4. Execution: from the worktree root with `TMPDIR=$WT/.scratch`,
   `PYTHONDONTWRITEBYTECODE=1`: `python3 -B .scratch/ca02/replay-runner.py --check`
   → rc=0. `--check` prints the receipt and never publishes
   (`reports/round-34/run-validation.py:522-531`); the default write path
   (`:532-538`) was never taken. No in-tree round runner was executed: both
   invocations ran the worktree's bytes.

## Run 2 — protocol replay result (the counted observation)

All legs green, matching the filed receipt exactly:

| claim | legs (status) |
|---|---|
| C | C1-C3 green |
| D | D1-D7 green |
| O | O1-O5 green |
| cross | CO1-CO5 green; CO6 could-not-evaluate (as filed); L1 green; P1 green; X1-X3 green; X4 green |

- `acceptance_checks_passed: true`, `failures: []` — equals filed
  (`reports/round-34/validation.json:2,169`).
- `runner_sha256` equals filed (`be11ff46…0f9`) — the receipt records the
  pristine worktree file, not the replay copy.
- `input_sha256` (10 inputs) equals the filed block byte-for-byte
  (`reports/round-34/validation.json:170-181`).
- `missing_dependencies` equals filed: `reports/round-34/cross/X00-connector.md`,
  `reports/round-34/depth/D17-verify-gates.md` — both genuinely absent from the
  close commit (`ls` in the worktree), so those rows compare equal
  (`reports/round-34/validation.json:190-200`).
- Normalized diff vs filed receipt (removing only `measured_at_utc` and the
  X1-X3 `manifest` note): **IDENTICAL** (python deep-compare of the full JSON).
- The two removed fields are the only deltas, both explained:
  (a) `measured_at_utc` is volatile (`2026-10-19T09:06:27-03:00` vs filed
  `2026-10-19T05:00:03-03:00`, `reports/round-34/validation.json:189`);
  (b) the filed X1-X3 measurement carries `"manifest": "pending-by-construction…"`
  (`:148`) because the close-time measurement (05:00:03) preceded the fleet
  MANIFEST row landing in the close pass (commit 05:01:17; live
  `/home/vgpnk/Projects/shokunin/MANIFEST.json` mtime 08:56 now contains exactly
  one `"round": 34` row, grep count 1). The runner's own limits declare this
  input class close-time (`:185`); with the row present the note legitimately
  does not fire. Neither delta touches any leg status or failure.

## Run 1 — negative control: unmodified runner from the worktree

`python3 -B reports/round-34/run-validation.py --check` from the worktree root
(unmodified bytes) escaped to the live checkout exactly as O12 predicts, via
the absolute `ROOT` + `os.chdir` (`reports/round-34/run-validation.py:10,26`):

- One failure: `claim O: O1-O5: O2: inventory counts differ: 33 runners,
  {'guarded-refresh': 22, 'unguarded-in-place': 11}` — the live tree at dfb0719
  has the rounds 35–38 runners (33) instead of the close-time 29 (filed counts
  29 = 18/11, `reports/round-34/validation.json:53-65` region). This is the
  documented later-tree recount class (cf. R37-Ca-01), not a round defect.
- Mechanical escape proof: the D4 tamper probe wrote `.scratch/r34-tamper/packet.md`
  into the LIVE tree (relative path resolved from the chdir'd live ROOT).
  Removed after the run; live `git status --porcelain` shows only
  `?? reports/round-39/` (untracked, this round's own fragments).
- C1-C3 green even in the escaped run (box-1 survey stable at 28/28), showing
  the escape is only detectable on tree-size-sensitive legs — which is why the
  r37 seats could not count an unmodified run either way.

## Disposition mapping (input to the successor ledger)

| r37 row | group | old disposition | new disposition |
|---|---|---|---|
| R37-Ca-05 | C | could-not-reproduce | reproduced-under-protocol (Run 2, C green) |
| R37-Ca-06 | D | could-not-reproduce | reproduced-under-protocol (Run 2, D green) |
| R37-Ca-07 | O | could-not-reproduce | reproduced-under-protocol (Run 2, O green) |
| R37-Ca-08 | cross | could-not-reproduce | reproduced-under-protocol (Run 2, cross green incl. X legs) |

This also closes the r37 owed item "reconsider r34/O and r34/cross"
(`reports/round-37/calib/Ca08-verify.md:32`): Ca08 reproduced only C/D under
bwrap with fleet inputs masked; this replay covers all four groups with the
fleet report and MANIFEST read unmasked (r34 fleet report mtime 04:53 predates
the close commit 05:01:17; no r34-filed digest of it exists to compare —
`to-verify` beyond mtime evidence). Consistent with Ca08's C/D result, not
contradicted anywhere.

## Fidelity limits

- Fleet-root absolute inputs (`FLEET_REPORT`, `MANIFEST`,
  `reports/round-34/run-validation.py:21-22`) were read from the live fleet
  root, not a close-time snapshot; r34's report is unchanged by mtime, the
  MANIFEST row is post-close by design (see above). Byte-digest equality with
  the 05:00 close-time values is `to-verify` (no filed digests exist for these
  two inputs).
- The replay copy adaptation (`ROOT = os.getcwd()`) is this seat's
  instantiation of the declared relative-root requirement; it is digest-pinned
  above so any protocol wording from Ca01 can be checked against exactly what
  ran.
- Worktree left in place at `.scratch/ca02-wt-r34` (disposable; scratch
  cleanup may remove it — every count above is reproducible from the cited
  commands). Raw run outputs retained at
  `.scratch/ca02-wt-r34/.scratch/ca02/run{1,2}-*.json`
  (sha256 `b03db516…4a86`, `6013469c…0fa5`) until cleanup.

## Owed

- `reports/round-39/calib/Ca01-protocol.md` / `calib/isolation-replay-protocol.md`
  did not exist at execution time (ls of `reports/round-39/calib/` returned
  empty, 2026-10-19 09:03). I applied the mechanics declared in
  `reports/round-39/claims.json` (worktree at close commit, relative-root
  requirement, TMPDIR isolation). Owner: Ca01/integrator. If the authored
  protocol prescribes different adaptation text or ordering, re-running the
  pinned commands is ~15 s; the digests above pin what ran.
- Successor recount-ledger rows for R37-Ca-05..08 with disposition
  `reproduced-under-protocol`, evidence = this fragment. Owner: integrator
  (claim Ca's after_required names the successor ledger; not this seat's out
  path).

## Citations

- `reports/round-39/claims.json:19-24` — claim Ca after_required: protocol
  mechanics (worktree at close commit, relative-root requirement, TMPDIR
  isolation), the 4 rows to re-disposition, zero-filed-edits threshold.
- `reports/round-37/calib/recount-ledger.json:60-111,451-455` — the four
  could-not-reproduce rows and the summary block.
- `reports/round-34/run-validation.py:10,26,522-538` — absolute ROOT,
  unconditional chdir, --check print-only ordering, default write path.
- `reports/round-34/validation.json:2,5-9,25,27-30,45,47-50,65,67-71,148,159,169,170-181,189,190-200` —
  filed acceptance, per-claim results, pending-manifest note, input digests,
  measured_at, missing_dependencies.
- `reports/round-37/calib/Ca02-r34.md:18,36` — the r37 isolation finding and
  owed item this run resolves.
- `reports/round-37/calib/Ca08-verify.md:23,27,32` — prior bwrap C/D
  reproduction, masked fleet inputs, the O/cross owed item.
- Command outputs recorded inline above (sha256sum, git worktree/rev-parse/
  diff/status, python deep-compare verdict `NORMALIZED DIFF run2-vs-filed:
  IDENTICAL`, Run 1 failure text, grep MANIFEST count 1, mtimes via stat).
