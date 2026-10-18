# R14-C09 — SCORECARD loop-1 summary draft

Prepared 2026-10-17. Owner: R14-C09..C10 integration shard. This is a
parent-owned landing draft, not a write to `SCORECARD.md` and not an admission
of round 14. Append the proposed section; do not rewrite the filed round
sections. The census below reads receipts without invoking their runners.

## Proposed SCORECARD append

### Loop 1 recorded-outcome checkpoint — rounds 8–13 (2026-10-17)

| scope | filed final states | calibration / limits | counting command and evidence |
|---|---|---|---|
| loop 1, rounds 8–13 only | **4 admitted** (8, 9, 10, 12); **1 rejected** (11); **1 operator-skipped** (13) | Round 11's D/O claim flags pass, but F fails the unchanged 95% threshold; the round stays rejected. Round 12's A pass is an audit result, not acceptance of the semantically rejected handoff. Round 13 earns no completed-round credit. | Read-only `C09/C10-CENSUS` below, measured 2026-10-17; `reports/round-{8,9,10,11,12}/validation.json`; `LOG.md:3077-3080` |

The stored claim flags are **14 passed / 1 failed**, counted by
`C09/C10-CENSUS` on 2026-10-17; these are filed harness decisions, not an
independent certification that every literal threshold or later-tree check
is satisfied. The per-round threshold audit belongs in
`reports/round-14/loop1-retrospective.md` when integrated. Historical
admissions are not silently rescinded or recertified by this summary.

The round-11 denominators remain explicit: the filed F measurement has
147 stable / 189 comparable = 0.777777…; the all-row summary has
147 / 192 = 0.765625 (rounded 0.7656). Both are below 0.95, so neither
interpretation reverses rejection. Command: `C09/C10-CENSUS`, measured
2026-10-17. Evidence: `reports/round-11/validation.json` `claims.F.measurement`,
`reports/round-11/recheck/summary.json`, and
`reports/round-12/recount/dispositions.md:77-79`.

This is a checkpoint within the amended loop, not completion of loop 1.
The latest regimen places integration in round 14 and GLM work in rounds
15–16; the round-13 handoff-v2/civ-map work is deferred to those GLM rounds,
and D4 to a loop-2 build round. Source: `LOG.md:3065-3080`. Freshness
axis-move claims stay paused pending an operator ruling; no threshold is
retroactively relaxed, numeric quality score raised, or canon/permission
clearance inferred.

#### C09/C10-CENSUS — read-only count and denominator control

Run from the lane root. Observed 2026-10-17: states 4 admitted / 1 rejected /
1 skipped; stored claim flags 14 passed / 1 failed; F remains below 0.95
with both denominators. This command does not execute any round validator.

```bash
export TMPDIR=$PWD/.scratch
export PYTHONDONTWRITEBYTECODE=1
python3 - <<'PY'
from collections import Counter
from datetime import date
import json
from pathlib import Path
states, flags = Counter(), Counter()
for r, accepted in {8: True, 9: True, 10: True, 11: False, 12: True}.items():
    receipt = json.loads(Path(f"reports/round-{r}/validation.json").read_text())
    declaration = json.loads(Path(f"reports/round-{r}/claims.json").read_text())
    assert receipt["acceptance_checks_passed"] is accepted
    assert set(receipt["claims"]) == {c["id"] for c in declaration["claims"]}
    verdicts = {k: v["passed"] for k, v in receipt["claims"].items()}
    assert all(type(v) is bool for v in verdicts.values())
    state = "admitted" if accepted else "rejected"
    states[state] += 1
    flags.update("passed" if v else "failed" for v in verdicts.values())
    print(r, state, verdicts)
assert "**Round 13 status:** operator-skipped before any work landed" in Path("LOG.md").read_text()
states["skipped"] += 1
print(13, "operator-skipped", "LOG.md:3077-3080")
f = json.loads(Path("reports/round-11/validation.json").read_text())["claims"]["F"]
s = json.loads(Path("reports/round-11/recheck/summary.json").read_text())
m = f["measurement"]
assert f["passed"] is False
assert m["stable"] == s["stable"] == 147
assert m["rows_rechecked"] == 189 and s["rows_reckecked"] == 192
assert m["stable"] / m["rows_rechecked"] < .95 and s["stable"] / s["rows_reckecked"] < .95
print("F comparable/all-row", m["stable"] / m["rows_rechecked"], s["stable"] / s["rows_reckecked"])
print("measured_date", date.today().isoformat(), "states", dict(states), "stored_claim_flags", dict(flags))
PY
```

## Parent integration checks — not evidence of round-14 completion

- Keep round-14 O/D/C verdicts pending until the delivered-tree
  `python3 reports/round-14/run-validation.py` result exists. The summary
  above is independently landable historical bookkeeping, not a substitute
  for the retrospective, routed-resolution matrix, guard controls or full
  regression receipt.
- At the round-14 declared baseline, the filed defect ledger contains
  **15 entries: 8 fixed-with-control / 7 routed**, rather than the
  SCORECARD/LOG round-12 headline's 7 fixed / 8 routed. Measurement command,
  run 2026-10-17:
  `git show 926c86f8be3cc9307f8f10dce55768c290b6f94d:reports/round-12/defects/ledger.json | python3 -c 'import collections,json,sys; e=json.load(sys.stdin)["entries"]; print(len(e), dict(collections.Counter(x["status"] for x in e)))'`.
  `R11-DRAFT` is `fixed-with-control` in that snapshot. Round-14 append-only
  exposure entries are separate, not additional round-12 fixes/routes.
  Do not silently turn a fixed row into a route or shrink the declared
  round-14 eight-item worklist; require an explicit mapping in
  `reports/round-14/routed-resolution.json` and an append-only discrepancy
  disposition. Independent corroboration:
  `reports/round-14/retrospective-audit-C08.md:7`.
- The round-14 C declaration's historical "2 operator amendments" wording
  and the latest `LOG.md:3065` heading "Regimen amendment 3" are different
  accounts. Refer to the named amendment records at `LOG.md:3048-3080`
  rather than manufacturing a reconciled amendment count.
- No live rerun of a filed round validator is needed for this row. Earlier
  runner invocations can overwrite their committed receipts; round-14 guard
  verification belongs to its assigned owner. Do not set
  `REFRESH_RECEIPTS=1` merely to regenerate historical evidence.
