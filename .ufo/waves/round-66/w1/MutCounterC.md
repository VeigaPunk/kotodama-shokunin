# MutCounterC — mutation probe of `reports/round-66/accept-c.py` (ACCEPT-C-66)

Seat: mutation-tester, wave w1, round 66 (hyaku run 5). Lane base `94209e8f8096…b8616`.
Target instrument: `reports/round-66/accept-c.py`, sha256 `0726b4bc99eefe05a81c92cb6fd1bb3819a041b68679466aa6278350c19dda86` (frozen, pre-data).
Mutants and pristine copy live only under `.ufo/waves/round-66/stage/mut-c/`; the committed instrument was never edited (hash identical before and after the probe).

## Method (same detector on pristine, mutant, restored bytes)

`stage/mut-c/build_and_run.py` builds a **fixture land state** inside a `git clone --shared` of the lane (`stage/mut-c/fx`, sha-1 94209e8 present, `main` ref controllable). The fixture is a full synthetic land: 24 rows S777–S800 (11 cells, kind `docs`, tier A/B, `mined`, `2026-10-24`, used-by ENTRY), 24 distinct hosts, 24 distinct live URLs each with a `web.archive.org/web/<14d>id_/` capture, entry with one H1 / one H2 / `- topic:` / one `(S###)` bullet per row carrying 5 in-order quote words + 1 novel word, README row containing the topic verbatim. Then one defect per mutant is injected. Every run is the unmodified counter script against the fixture: 5 scripts × 5 land states + the pre-data lane tip.

Declared fixture double: `reports/round-28/readme/sweep.py` was replaced by a 3-line stub (`totals_ok True`, exit 0) in the fixture only, so the SWEEP leg is satisfied without modelling the README counts footer. SWEEP is not under test here; no mutant touches it.

Negative-control sanity: on the **clean** fixture the pristine counter prints `ACCEPT-C-66: PASS` and every mutant also prints `PASS`; on each defect state the pristine counter prints `FAIL` at exactly the mutated leg and the other four mutants still `FAIL` at that same leg — so each mutant is isolated to one leg, and the defect states are genuine.

## Mutant table

| # | byte change (one line, `diff -u` vs committed) | leg relaxed | sha256 | defect land state ("kill description") | pristine output | mutant output | verdict |
|---|---|---|---|---|---|---|---|
| M1 | `if inq < 3 or cov >= 0.8 or not novel:` → `cov >= 0.99` | RESTATE | `2870f4d6…d2a13` | S777 bullet restates 9/10 teaches words in order (`cov=0.90`) plus 5 quote words + novel word — a near-copy of the teaches cell | `RESTATE FAIL bad=['S777:quote_words=5 teaches_cov=0.90 novel=5']` → `ACCEPT-C-66: FAIL` | `RESTATE PASS bad=[]` → `ACCEPT-C-66: PASS` | **SURVIVED** |
| M2 | `if count != 1:` → `if count < 1:` | ONEID | `d82d1325…b5832e` | S777 cited twice on one bullet line `… (S777) … (S777)`; RESTATE still sees exactly 1 bullet for S777 | `ONEID FAIL bad=['S777:citations=2']` → `FAIL` | `ONEID PASS bad=[]` → `PASS` | **SURVIVED** |
| M3 | `append_ok = len(missing_old) == 0` → `len(missing_old) <= 2` | APPEND | `a3a1c540…eabe4` | tip deletes 2 base registry rows (S1, S2 region) — registry no longer append-only | `APPEND FAIL missing_old=2 appended=24` → `FAIL` | `APPEND PASS missing_old=2 appended=24` → `PASS` | **SURVIVED** |
| M4 | `"no-capture" not in src.casefold()` → `"capture" not in src.casefold()` | CAPTURE | `9a2c104b…cf160` | S777 source cell `… - https://h0.example.org/a0 ; capture pending` (no archive URL, no `no-capture` token) | `CAPTURE FAIL bad=['S777']` → `FAIL` | `CAPTURE PASS bad=[]` → `PASS` | **SURVIVED** |

Restored/clean bytes under each mutant: `PASS` (no over-strictness introduced — all four are pure relaxations). Cross runs on defect states: M1 on d2/d3/d4 → `FAIL` (correct leg), M2 on d1/d3/d4 → `RESTATE`/`APPEND`/`CAPTURE` `FAIL`, M3 on d1/d2/d4 → `FAIL`, M4 on d1/d2/d3 → `FAIL`. Full matrix: `stage/mut-c/results.json` (25 runs).

## "Does a landed tree kill it?"

**No, on the evidence available.**

- The genuine land state does not exist yet (pre-data): `corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md` is absent, so the lane tip run is a **baseline failure**, which is *inconclusive*, not a kill — pristine and all four mutants print `ACCEPT-C-66: FAIL` identically there (`FILE/SET/ONEID/RESTATE/HOSTS/CAPTURE/TOPIC FAIL`).
- On a **clean** land state all four mutants print `PASS` exactly as the pristine counter does. A clean tree therefore cannot distinguish any of them: only a land state that *contains the exact defect* distinguishes a mutant, and the round ships exactly one validated land state.
- The round's only declared pre-data control is the do-nothing control (`reports/round-66/telemetry/controls-c.txt`: "counter FAILS before lands"). All four mutants also fail it identically (run above), so the frozen control suite cannot kill any of these mutants.
- `accept-c.py` has **no self-test / no negative-control leg** (`grep -c selftest` = 0); claims.json's controls text only promises "a counter a do-nothing control passes is revised", which none of these mutants violates.

## Operability findings (coverage, not contract)

1. Each of the four relaxations is invisible to every other leg on the defect tree — i.e. the counter's own cross-coverage does not catch them. Most consequential: **M3** — `corpus/SOURCES.md` is outside the NOHARM diff scope (`-- corpus/knowledge` only), so deleting/editing up to N base registry rows is caught by APPEND alone; relaxing APPEND's count turns registry history edits into a silent PASS.
2. **M2** shows the `one-row-per-bullet` and `cited-once` checks are separable only by ONEID: a bullet with two citations on the same line satisfies RESTATE's `bullets == 1` test.
3. **M4** widens on any occurrence of the substring `capture`, which every real row carries (`capture https://web.archive.org/…`); a row with `capture pending` passes with no archive evidence at all.
4. Fix (not applied; instrument is frozen for this round): add a `--selftest` mode that replays these four defect land states and asserts `FAIL` per leg. Expected additions: `cov ≥ 0.8` near-copy, duplicate same-line citation, 1–2 removed base rows, `capture pending` without archive URL.

## Files and restoration evidence

- Committed `reports/round-66/accept-c.py` sha256 `0726b4bc…dda86` before and after the probe (report field `same after: True`).
- Mutant copies: `stage/mut-c/M1_coverage_0.8_to_0.99.py` `2870f4d6…d2a13`, `M2_oneid_exact_to_atleast.py` `d82d1325…b5832e`, `M3_append_count_relaxed.py` `a3a1c540…eabe4`, `M4_capture_substring_widened.py` `9a2c104b…cf160`; pristine byte copy `stage/mut-c/pristine.py` `0726b4bc…dda86`.
- Harness/receipts: `stage/mut-c/build_and_run.py` (`ba8ae4ff…b1b26e`), `stage/mut-c/results.json`, `stage/mut-c/err.txt` (empty), fixture clone `stage/mut-c/fx` (own `.git`, `main` restored to `clean`, commit `e274298`).
- Lane jj/Git state untouched: `git status --porcelain` unchanged from pre-probe (` M tools/check-claim-separability.py`, `?? .ufo/`, `?? reports/`); no commit, no index write, no lane file edited. All writes are under `.ufo/waves/round-66/stage/mut-c/` and this report.
- No tools installed or upgraded (stdlib python3 3.14 + git only).

Report: .ufo/waves/round-66/w1/MutCounterC.md
