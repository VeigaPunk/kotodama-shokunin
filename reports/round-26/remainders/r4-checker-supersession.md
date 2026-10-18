# r4-checker supersession (integrator, 2026-10-18)

`reports/round-25/v3-supersession/v3-supersession-check.py` was authored against
the declared-in-r4 lineage. The round-26 register landing legitimately changed
the 6 D4 read-set files, and the v3 default baseline moved to declared-in-r5
(`reports/round-26/handoff/declared-in-r5/`, packet e3fb1ca5). The r4 checker's
two pin tails (v2 successor pin, v3 packet-baseline pin) are resolved by:

- `reports/round-26/remainders/pin-repoint-check.py --check` → exit 0, 17/17
  controls (stale rows replay red, new rows replay green, filed rows untouched);
- `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` → exit 0
  (16/16 + 20/20 + 105/105 + 27 claims 16/7/4, r5-pinned).

The r4 checker itself is SUPERSEDED, not repaired: its r4-lineage expectations
cannot see the r5 freeze without rewriting its pinned controls (which would
orphan its round-25 receipt). Its frozen round-25 receipt stands as historical.
