# ScribeRegistryRows — round 83, wave 1

Seat: `ScribeRegistryRows` (leaf; no subagent dispatch). Milestone: `r83-v1`.
Lane: `kotodama-shokunin` (jj-colocated; git backend). Lane base
`3088bd7fe2a55a123214abba7008dcddf12b301c`; frozen claims/counters
`21277b089e3c64c247bb4e0fcb033abfdfa1e668`.

## Behavior delivered

`SKILL.md` `## Gates and probes` gained the 14 missing counter rows as one
contiguous block, inserted after the `accept-ca-75` row and before the
`accept-c-73 / accept-ca-73 correction` note row:

`accept-c-76`, `accept-ca-76`, `accept-ca-79`, `accept-o-79`, `accept-d-80`,
`accept-o-80`, `accept-c-81`, `accept-d-81`, `accept-o-81`, `accept-d-82`,
`accept-o-82`, `accept-o-83`, `accept-d-83`, `accept-c-83`.

Every row has the table's 8 cells (`name | kind | entry command | verdict map |
self-test | pinned values | write scope | owner`) and contains the counter's
repo-relative path verbatim in the entry-command cell. No cell contains a
literal pipe. `owner` is `kotodama-shokunin` throughout. No earlier row was
edited.

## Derivation

Each cell was read from the counter's frozen bytes at
`21277b089e3c64c247bb4e0fcb033abfdfa1e668`. The worktree copies hash-matched
the frozen copies at seat start; the post-reading counter revisions are recorded
under Findings 5. Entry flags come from the script's
argparse block, verdict labels and denominators from its print/refusal paths,
self-test spelling from its `__main__` guard, and pinned values from the literals
the script reads plus the `reports/round-NN/claims.json` block it loads with
`git show <freeze>:…` (for rounds 81-83 through `reports/round-83/counterlib.py`
`load_config`/`claim_config`).

R82-M3 reading authority: the frozen-object fetch receipts in
`stage/ScribeRegistryRows/rows.md` bind the row text. `ScoutSources` is the
independent second reading; no byte-count or quote disagreement was observed by
this seat because this seat read only the frozen lane objects. If its reading
differs, the disagreement is to be reported, not silently reconciled.

## Gates exercised (observable outputs)

1. Row-shape check (the assignment's required `python3 -c` form), recorded in
   `stage/ScribeRegistryRows/rows-validate.txt`:
   - 14 added rows; each parses to exactly 8 cells; no cell contains a pipe;
     each script path is a verbatim substring of its entry-command cell.
   - Result line: `PASS`.
2. Insertion-diff check, recorded in `stage/ScribeRegistryRows/skill-diff.txt`:
   - `git diff --numstat -- SKILL.md` → `14	0	SKILL.md` (14 insertions, 0 deletions).
   - HEAD `SKILL.md` had 60 data rows; the worktree has 74; the 14 added names
     are exactly the assignment list; no row was dropped; the pre-existing row
     order is preserved.

No acceptance counter was executed. The round's `accept-o83.py` gate and
`tools/check-gate-registry.py` are the main agent's verification, and
`tools/check-gate-registry.py` did not exist in the worktree at write time
(`ls` → no such file), which is expected: another seat owns that landing.

## Touched surfaces

- `SKILL.md` — 14 inserted data rows in `## Gates and probes`; no other section
  and no existing cell changed.
- Receipts (new): `.ufo/waves/round-83/w1/stage/ScribeRegistryRows/rows.md`,
  `.ufo/waves/round-83/w1/stage/ScribeRegistryRows/rows-validate.txt`,
  `.ufo/waves/round-83/w1/stage/ScribeRegistryRows/skill-diff.txt`, and this
  report.

Nothing in `corpus/`, `tools/`, `reports/`, `.ufo/state/`, `MANIFEST.json`,
`considerthese/`, the fleet repo, or a sibling lane was written. No git/jj
command mutated anything; the only git calls were read-only (`show`,
`rev-parse`, `diff`, `status`).

## Out of scope

- `tools/check-gate-registry.py` (owned by another seat) and its selftest.
- The round's three claims' data artifacts: `corpus/knowledge/myth-symbol/marriage-alliance-bridewealth.md`,
  `corpus/QUALITY.md` 31, `tools/check-cited-records.py`,
  `reports/round-82/counter-revisions.md`, the S908 superseding row.
- Any commit, push, or journal mutation; the L1 lands every byte.

## Findings

1. `reports/round-80/accept-d.py` docstring/code mismatch: the docstring lists
   "the lint tool at lands not matching its frozen sha256" as an exit-2 refusal,
   but `leg_lint` (`reports/round-80/accept-d.py:248-251`) implements it as a
   `LINT` leg failure and `main` has no refusal path for it. The registry row
   follows the code and names the leg. This does not change the counter's
   verdicts; it is a documentation erratum candidate for a later routed fix.
2. `reports/round-79/accept-o.py` and `reports/round-81/accept-c81.py` carry
   literal fixture paths (`reports/round-79/fixtures/{red,green}.json`,
   `reports/round-81/telemetry/red.txt`, `reports/round-81/annotations/disp.md`)
   that belong to their selftest fixture builders, not to the graded legs. The
   rows cite the frozen config pins instead; a reader who greps only the script
   literals would name the wrong fixtures.
3. The three round-83 counters expose `--junk` (a mutation battery) and no
   `--selftest`; passing `--selftest` is an argparse error (exit 2). The
   self-test cells say `—` and name `--junk` parenthetically.
4. Observation only: lane HEAD advanced from `774cc2e3…` (seen at seat start) to
   `1b0f3767ede846667d0be87297758ee8b35bc873` (seen at receipt write time) while
   this seat worked. The insertion diff is clean against the later HEAD; this
   seat committed nothing.
5. Post-reading counter revisions: the frozen and current bytes of
   `reports/round-83/accept-o83.py`, `reports/round-83/accept-d83.py` and
   `reports/round-83/accept-c83.py` now differ. The revisions are internal:
   loop-variable fixes in `missing_of` and `rows_leg`, materialising `tools/*.py`
   into the graded tree, a `None` guard on the checker shape read, and `C.NoOp`
   handling inside the `--junk` battery (the d83 worktree copy also carries an
   uncommitted copy of that fix). None alters the row-visible contract: the
   argparse flags, leg tables (8/9/9), verdict and refusal lines, and the
   absence of `--selftest` are unchanged, so the frozen-byte-derived rows remain
   accurate for the current counters. Recorded here so the two readings are not
   silently conflated.

## Known limits

- All verdict-map and pinned-value cells are transcriptions of committed code
  paths, not executed runs; no counter was run, and no row is offered as
  execution evidence.
- The 8-cell check is a local parse; the round's canonical registry checker
  (`tools/check-gate-registry.py`) was not available to run.
- The pinned values are the script's `git show <freeze>` config values plus its
  literals; the prose judgement of which values matter is this seat's, and the
  precise contract (numbers, regexes, paths) is in the frozen claims.

## Artifact paths (repo-relative)

- `.ufo/waves/round-83/w1/stage/ScribeRegistryRows/rows.md`
- `.ufo/waves/round-83/w1/stage/ScribeRegistryRows/rows-validate.txt`
- `.ufo/waves/round-83/w1/stage/ScribeRegistryRows/skill-diff.txt`
- `.ufo/waves/round-83/w1/ScribeRegistryRows.md`
- `SKILL.md` (modified, uncommitted)

## Tooling and scratch

No tool was installed or upgraded. Scratch was used only for the row draft and
was removed after the receipts were copied; nothing is left behind. No absolute
scratch path is cited by this report or its receipts. The only absolute paths in
`rows.md` are the required `--fleet-root`/`--fleet` flag values inside the row
contracts, which are lane-documented repo paths, not scratch locations.
