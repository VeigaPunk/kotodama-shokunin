# ExecCounterSmokeC — ACCEPT-C-66 counter smoke (build, operability)

Counter sha256 `0726b4bc99eefe05a81c92cb6fd1bb3819a041b68679466aa6278350c19dda86`
(verified against `sha256sum`), lane rev `94209e8f….`, pre-data tree. Counters not edited.

## What ran

1. `python3 -B reports/round-66/accept-c.py --root .` → **exit 1**, 0.088 s, 12 legs printed
   (FILE/SET/ROWS/ONEID/RESTATE/HOSTS/LINK/APPEND/NOHARM/SWEEP/CAPTURE/TOPIC), final
   `ACCEPT-C-66: FAIL`. Output is **byte-identical** to the frozen
   `reports/round-66/telemetry/dry-run-c.txt` and stable across reruns. The do-nothing control
   therefore behaves as `controls-c.txt` declares; no leg crashed on this path; no lane side effects.
2. `python3 -B reports/round-66/accept-c.py --help` → **exit 0**, `usage: accept-c.py [-h] [--root ROOT]`.
   No crash; missing-`--help` does not apply.
3. Extra paths: nonexistent `--root` → exit 2 (`ACCEPT_C_INPUT_ERROR registry`); `--bogus` → exit 2;
   run from `/tmp` with absolute root → legs unchanged but header misreports the revision.

## Findings (full detail + minimal fixes: `.ufo/waves/round-66/stage/execcountersmokec.md`)

HIGH
- **D1 crash** `accept-c.py:236` — `reg_by_id[sid][0]` raises `KeyError` (traceback, exit 1, **no verdict
  line**) when the entry cites `(S777)` once but the registry row is absent; reproduced in a shared clone.
  Fix: guard `if sid not in reg_by_id: restate_bad.append(f"{sid}:no-row"); continue`.
- **D2 bypass** `accept-c.py:281-286` — NOHARM diffs committed `BASE..main`, not the worktree; deleting
  `corpus/knowledge/culture-material/calendar-festival-systems.md` uncommitted still prints
  `NOHARM PASS diff=[]`. HEAD is detached and `main`/jj bookmark sit at base, so even post-commit the
  leg can stay vacuous. No other leg covers corpus/knowledge outside registry rows.
- **D3 receipt integrity** `accept-c.py:137` — `git rev-parse main` lacks `-C root`; from `/tmp` with a valid
  `--root` the header prints `measured revision … unresolvable` (or another repo's `main`). Fix: `-C root`, prefer HEAD.

MED
- **D4 false-FAIL** `accept-c.py:319-321` — TOPIC takes the *first* line mentioning the filename; the routine
  README revision prose (`corpus/README.md:3-10` pattern) precedes the index bullet (`:390`), so a correct
  round-66 landing FAILs TOPIC. Proved by swapping identical text order: bullet-first PASS, prose-first FAIL.
- **D5 false-PASS** `accept-c.py:155` + `:321` — a bare `- topic:` line passes FILE and TOPIC (`"" in row`).
- **D6** `accept-c.py:251-257` — HOSTS says "normalized" but counts raw netloc, so `www.`/bare double-count.
- **D7** `accept-c.py:104-105` vs `:21` — LINK is documented scheme/query-insensitive but `norm_url` keeps
  scheme and query (http↔https, `?utm_*` variants pass).
- **D8** `accept-c.py:108-113` — LINK checks only the first live URL per row; 233/701 base rows carry 2+ URLs,
  so reusing a base row's second URL passes.
- **D9** `accept-c.py:272-280` — APPEND set semantics: an exact duplicate base row reports `appended=0`, PASS;
  no leg counts rows.

LOW — SET labels missing ids as "non-unique" (`:189-190`); `|` inside an anchor quote trips
`ROWS cells=12` (`:78`); SWEEP detail prints the last line, not `totals_ok True` (`:297`); input-error path
emits a stray `FILE FAIL` before exit 2 (`:166-171`); ONEID/RESTATE are not bullet-scoped (`:217-245`);
`ROW_RE` is not table-scoped (`:51`); `base_ids` dead (`:178`).

## Files changed

- `.ufo/waves/round-66/stage/execcountersmokec.md` (new, detailed defects)
- `.ufo/waves/round-66/stage/evidence/accept-c-base-run.txt` (new, captured run == frozen receipt)
- `.ufo/waves/round-66/w1/ExecCounterSmokeC.md` (this report)

Scratch shared clone used for bypass reproduction was removed; lane tree, index, jj state and counters untouched.

## Risks / blockers

- D2 + D4 mean the frozen ACCEPT-C-66 cannot both certify the lands and be met by the normal README
  pattern as written; D3 makes the receipt's "measured revision" untrustworthy. If the L1 fixes the counter,
  re-freeze `controls-c.txt`/`dry-run-c.txt` before trusting data-leg output (frozen-predicate rule).
- No blockers: the assigned runs completed; no missing artifacts.

No tools installed or upgraded (pacman transactions paused; nothing needed).
