# ExecRegistryCensus — round 83, wave 1

## Deliverables (repo-relative)

- `.ufo/waves/round-83/w1/stage/ExecRegistryCensus/registry-census.json` — machine census:
  `{"instruments":[61 paths],"rows":60,"missing":[14 paths],"proposed":{counter path:[8 cells]}}`.
- `.ufo/waves/round-83/w1/stage/ExecRegistryCensus/registry-census.md` — method, cross-checks,
  copy-paste proposed rows, interface constraints, peer reconciliation, defect register, limits.

No other lane file was written; no commit, push, or mutating git/jj command was run.

## Result

Basis: committed bytes at frozen commit `21277b089e3c64c247bb4e0fcb033abfdfa1e668` (lane base
`3088bd7fe2a55a123214abba7008dcddf12b301c`), read with `git show`/`git ls-tree` only.

- Instruments (`reports/round-*/accept-*.py`): **61**.
- `## Gates and probes` data rows: **60** (54 parse to 8 cells; 6 parse to 9 — see risk 2).
- Covered by an entry-command cell: **47**; missing: **14**.
- Missing: rounds 76 (2), 79 (2), 80 (2), 81 (3), 82 (2), 83 (3) — the three r83 counters are part of
  the 61 at the frozen commit and of the 14 missing rows.
- `proposed`: 14 rows × 8 cells, every cell pipe-free, every entry command naming its counter path.
  Each verdict map is quoted with `file:line` from the script's own bytes (argparse, verdict print,
  refusal print/return, selftest print).

## Cross-checks (measured)

- Lane base holds 58 counters; the frozen revision adds exactly the three round-83 counters → 61.
- `accept-o83.py` BEFORE constants read from its bytes: base instruments 58, base-missing 11
  (`reports/round-83/accept-o83.py:116-120`, `:164-167`). 11 + 3 = 14 = this census's missing set.
  Both numbers are right for their own revision.
- Dead-token scan over every entry-command cell at the frozen revision: **0 dead** `.py` tokens
  (o83 `dead_of` semantics).
- Independent re-derivation using o83's `registry_rows` parser reproduces 60 rows.
- AST audit of all 61 scripts: 61/61 have a main guard or `main`/`main_entry` function and declared
  exit sites; none falls under the "no main, no exits" defect rule.

## Peer reconciliation (worktree state; frozen object remains the census basis)

`ScribeRegistryRows` inserted the 14 rows into the worktree `SKILL.md`. Measured with this census's
rules against the worktree: **61 instruments, 74 data rows, 0 missing, 0 dead** — the exact after-state
the claim line needs (`0 missing / 74 registered / 61 instruments / 0 dead`, subject to the tool's own
count). Additions are the same 14 names as this census's missing set; only the within-block order of
the three round-83 rows differs (no coverage effect). No byte-count or quote disagreement exists in
the material available: the claim-D source seats count sources, not counter rows.

Two derivation differences were resolved toward the committed code and the affected cells corrected:

1. `accept-d-80`: the docstring lists a lint-tool sha256 mismatch as an exit-2 refusal, but the code
   grades it as a `LINT` leg failure (`reports/round-80/accept-d.py:248-251`). The verdict cell now
   says so.
2. `accept-o-79` / `accept-o-81`: the `red.json`/`green.json`/`refusals/` and `absent.py` literals are
   selftest fixture-builder values, not graded pins; the pinned-values cells now name the frozen
   config pins and mark those literals as selftest-only (same distinction as `ScribeRegistryRows`
   Finding 2).

`ScribeRegistryRows` Finding 5 records that the three round-83 counters were revised in the worktree
after the freeze (loop-variable fixes in `missing_of`/`rows_leg`, tool materialisation, a `None`
guard, `C.NoOp` in the junk battery). The defect below is measured against the **frozen** bytes and
stands there; the worktree revision already carries the fix, so the revised counter bytes — not the
frozen ones — must land for claim O to be gradeable green by its own counter.

## Headline risk — needs an L1 decision

`reports/round-83/accept-o83.py` as frozen **cannot reach exit 0**:

- `registry_rows()` appends `(cells, lineno)` (`:62`), but `missing_of()` (`:67`) and `rows_leg()`
  (`:166`) test `p in c[2]` behind `len(c) > 2`; a 2-tuple never satisfies the guard, so both
  classify every instrument as missing (measured with those exact semantics on the frozen
  `SKILL.md`: 61/61 instead of 14/61; every prepared row path "absent").
- Therefore REGISTRY (`:139-160`) and ROWS (`:164-167`) can never pass; the counter exits 1 even
  with a perfect registry, and two of its three `--junk` trials (`rows-dropped`, `canned-tool`) pass
  vacuously. `dead_of()` (`:70-77`) unpacks tuples correctly, so DEAD is unaffected.
- The proposed row remains the correct registry entry (8 legs, 0/1/2 exits, exact files); I did not
  amend the counter. Decide: land the revised counter, or grade claim O with this defect recorded.

## Secondary observations

1. Six existing rows (rounds 66–67, `SKILL.md:686-691`) are 9-cell because of a literal `|` inside
   the verdict-map cell. Entry-command coverage is unaffected. `check-gate-registry.py` should split
   on `|` and accept >= 3 cells (as o83 does), not require exactly 8; the 14 new rows avoid `|`.
2. `reports/round-76/accept-c.py:6381-6395` lists leg name `INDEX` twice (13 entries) and has no
   SEPARABLE leg; its printed denominator is 13, which the row states. Calibration flag, not a
   blocker.
3. The three r83 counters have no `--selftest` (passing it is an argparse error, exit 2); `--junk` is
   a mutation battery. The rows state `—` for self-test, matching rows 698–699's house wording.
4. `accept-c-76`/`accept-ca-76` selftests refuse without a scratch root rather than invent the
   system temp dir (`accept-c.py:6531-6537`, `accept-ca.py:3739-3743`); stated in the rows.

## Interface constraints handed to the O-tool seat (derived from o83's checks)

- Summary line: `GATE-REGISTRY: 0 missing / <r> registered / <i> instruments / 0 dead`; groups are
  missing, registered, instruments, dead (`accept-o83.py:144-148`).
- `--json` must carry `instruments`, `registered`, `missing`, `dead`, `rows`; graded comparisons need
  `sorted(instruments)` == lands instrument set, `missing == []`, `dead == []`
  (`accept-o83.py:141-160`, canned shape `:226-231`).
- `registered` must be >= the data-row count: o83 grades `reg >= len(rows) - 1` over a parse that
  includes the header row (`:155-160`). At the expected lands table (60 + 14 = 74 data rows), that is
  `registered >= 74`; `<i>` is 61.

## Authoritative reading (R82-M3)

`ScribeRows`' fetch receipts bind the registry rows; `ScoutSources`' reading is the independent
second reading. This census is a third, purely byte-derived reading. Any disagreement on a byte
count or quote must be reported and reconciled against the committed bytes at `21277b0…`; none was
found in the available material.

## Verification performed

- Read-only `git ls-tree`/`git show` at both revisions; in-memory AST parsing of all 61 scripts.
- Static coverage/dead checks over the worktree table (read-only), reported above.
- No counter executed; no build/lint/test/formatter run (wave rule).
- Absolute paths are absent from this report and both stage artifacts (QUALITY 31); all citations
  are repo-relative.

## Scratch

Seat scratch directory removed on exit; nothing left behind (parent scratch tree untouched).

## Blockers

None for the census. The accept-o83 leg defect is a decision item, not a blocker to the row set.
