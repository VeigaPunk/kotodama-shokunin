# CriticClaimO — falsification of claim O (round 82, w1)

Verdict: **claim O is NOT vacuous, but the frozen counter under-enforces two
contract clauses and under-determines NNd arithmetic.** Attack was on the
frozen instrument `reports/round-82/accept-o82.py`, not any draft. Full
dossier with commands and raw output:
`/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/CriticClaimO/falsify.md`;
verdict receipts in `.../stage/CriticClaimO/receipts/`.

## Measured (each with command + raw output in falsify.md)

1. **Before-state confirmed**: 0 recheck tools and 0 `RECHECK-QUEUE`
   occurrences at base `c285b2af…` (both greps exit 1 on no match).
2. **QUEUE binds via its own parser**: `want = tally(...)` (counter line 280)
   over `git show <freeze>:corpus/SOURCES.md`; my recompute with the
   counter's module gives `(0, 18, 14, 827, 0)` @2026-11-04 and
   `(813, 0, 14, 827, 0)` @2027-11-01 — matching claims.json and
   ExecEvidence's independent tally.
3. **Controls graded in a scratch clone** (`git clone --shared`, FREEZE
   c661e5c5 = base + byte-copy of claims.json; `rev-parse --show-toplevel`
   asserted == fixture dir before first commit; lane untouched):
   - A canned single-line stub → **FAIL 4/7** (QUEUE far date, MODULAR, ERROR).
   - B working parser WITHOUT the contract's `DUE <id> <date>` lines →
     **PASS 7/7** — DUE lines are never checked (`grep -c DUE` → 0).
   - C B + a decoy wrong summary line before the correct one → **PASS 7/7** —
     last-match-wins (lines 283-286); "exactly one summary line" unenforced.
   - D2 B ignoring `--registry` (default path byte-identical to frozen blob) →
     **FAIL 5/7**: QUEUE PASS, MODULAR + ERROR catch it.
   - E strongest canned adversary (correct numbers at both frozen dates,
     no registry read) → **FAIL 5/7** (MODULAR + ERROR).
4. **MODULAR blind spot (calibration defect)**: full-population sweep with the
   counter's parser — shifting every NNd due date ±1 day changes none of the
   four counts at either frozen date. A tool computing `opened + NN ± 1 days`
   passes all legs. MODULAR's due-row append uses an ISO cadence and its only
   NNd row is 365 days out; NNd arithmetic near boundaries is never exercised.
5. **SELFTEST floor is self-reported** (line 257 trusts the printed integer ≥
   8); controls printed "8"/"13" with no checks behind them. It does bind
   runnability — a syntax-broken tool died there and QUEUE/MODULAR/ERROR all
   gate on st_ok (270/302/343).
6. **Counter's own `--selftest`: PASS (12 checks)** — refusal spine verified
   (do-nothing control refused, LEGCOUNT refused, junk canned fails QUEUE,
   junk weak selftest fails SELFTEST, junk malformed-accepted fails ERROR).
7. **Under-specification register** (falsify.md §5): window boundaries
   inclusive both ends (lines 125/127); row membership = `ROW_RULE` id-anchor
   (line 42); fromisoformat superset for ISO cadences (108); success rc==0
   (287); RECHECK-ERROR may print to stdout OR stderr (353); `--registry`/
   `--window` defaults never exercised by any leg (180-183); cell stripping
   enforced.

## Smallest safe corrections

- DUE leg: compare per-id due sets against the counter's own parse; count
  SUMMARY matches and require exactly 1 in QUEUE/MODULAR/ERROR extraction.
- MODULAR: add an NNd synthetic row with due date on the as_of or
  as_of+window boundary (e.g. opened as_of−89, `90d`).

## Files written (absolute)

- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/CriticClaimO/falsify.md`
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/CriticClaimO/receipts/control{A,B,C,D2,E}.txt` (5 files)
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/stage/CriticClaimO/receipts/counter-selftest.txt`
- this report.

Installs: none. Unrun checks: none (all probes ran). Scratch
`/fast/scratch/hyaku/kotodama-r82/CriticClaimO` removed before yield. No lane,
fleet, or draft files mutated.
