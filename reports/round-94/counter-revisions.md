# Round-94 counter revisions

## rev1 → rev2 of `predispatch.py` (claim A counter)

- **rev1** (committed at `d4ff93c8`): the A1 leg excluded any link target whose
  *filename* contains `greet` from resolution checking
  (`targets = [t for t in LINK.findall(text) if "greet" not in t]`). ExecAdjacency94
  (wave-1 seat, stage report `.ufo/waves/round-94/w1/ExecAdjacency94.md`) showed the
  consequence: after the intended repoint to
  `linguistics/greeting-leave-taking-formulae.md`, the counter still prints
  `dangling 2`, because the one target the claim is supposed to produce is the one
  rev1 refuses to check. rev1 could never accept the claimed after-state.
- **Change (rev2):** every named `.md` target is checked; a pointer line is
  satisfied when any named target exists and mentions greeting/leave-taking.
  No other rule changed.
- **Timing:** no seat had scored claim A when this was written (claim A is scored
  by the L1 at integration, after WAVE-DONE). ExecAdjacency94 measured red-before
  only and did not run the frozen counter as a grader of record.
- **Base value re-stamped:** rev2 at base `e7fa8eafb7c5d9edd706f860cfc023e6c99b1ab2`
  (materialized via `git archive`) prints the same lines as rev1:
  `A1 dangling-greeting-pointers 2`, `C1 entry-present 0`, `C2 registry-rows 888
  highest-id S964`, `O0 tool-sha256 9799a96c…`, `CENSUS rc=0`, `INDEX rc=0`.
  `reports/round-94/predispatch-base.txt` now carries the rev2 stamp;
  `predispatch-base.rev1.txt` preserves the rev1 bytes.
- Claim predicates (claims.json) are unchanged; only the counter body was
  corrected, before data.
