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

## Battery instrument revision 1 → 2 (manifest + battery94 class table)

- **What:** the battery manifest (`manifest.json`) and the driver's CLASSES table
  (`battery94.py`) originally listed guessed diagnostic token names for A1, B1, H1
  and K1 (`NON-ASCII-VERDICT`, `MANIFEST-ROW-NOT-OBJECT`, nothing for K1). The v5
  grader refuses each class with a *different named token* (`VERDICT-NONASCII`,
  `VERDICT-SOFTHYPHEN`, `MANIFEST-ROW-TYPE`, `VERDICT-LOWERCASE`), captured by
  direct probe before any claim scoring. The token lists were amended to accept
  the actual tokens (the originals kept). No expected_exit, no traceback rule and
  no refusal requirement changed: each class still requires nonzero rc, no
  Traceback, and a named upper-case diagnostic.
- **Timing:** found and amended before claim O was scored (no seat ran the battery
  against the candidate; CriticO94 attacked with its own fixture set; the L1 ran
  the graded battery at integration).
- **Control receipts (L1-run, 2026-11-05):**
  - Stub `reports/round-92/controls/stub-tool.py`: selftest prints
    `SELFTEST PASS 89/89` with only 34 `  ok ` lines (exactly-N-ok clause fails it)
    — rc 0; battery: `BATTERY-SUMMARY survivors=7 unnamed=0 refused=0` (every
    class SURVIVOR); mutants94: `MUTATION-SCORE: 0/88 killed, 0 survived,
    88 broken-pattern`. The stub fails SELFTEST (34 ≠ 89), BATTERY and MUTATION.
  - v4 base (seats' red-befores): battery `survivors=4 unnamed=3 refused=0`;
    routed mutants `0/5 killed, 5 survived`; selftest `114/114` with 114 ok lines.
  - v5 candidate: selftest `SELFTEST PASS 126/126`, 126 ok lines, rc 0, 4
    concurrent runs stable; battery `survivors=0 unnamed=0 refused=7` with named
    tokens per class; REG lines byte-identical to v4 (`diff` empty, 34 cases).
