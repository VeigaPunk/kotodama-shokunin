# RevQuarantine — round 76 quarantine-table falsification

**Verdict: PASS for this scope.** I found no id/count drift, verdict upgrade, or reopened row in the 21-row round-76 carry-forward table.

## Evidence

- At base `98c486bdb4650ba5b8e651d332910e8ee60ad121`, the standing verdict table is `reports/round-71/telemetry/quarantine-verdicts.md:12-40`. Its rows are 18 payload-absent ids plus S807/S812/S835; tally is PRESENT 10, REFUSED 7, UNVERIFIABLE 4 (`:36-40`). S791 is the documented additional UNVERIFIABLE case because its truncated registry URL prevents fetching the exact document (`:19`, `:40`), not a newly reopened judgment.
- The standing slice re-derivation and count are independently recorded in `.ufo/waves/round-71/w1/RevQuarantineCrossCheck.md:3-9`; it specifies 21 rows, 18 payload-absent, 3 unreachable. That report records S778's absence from the lane registry at `:23-25`; this is an existing discrepancy, not an id newly added or removed in round 76.
- The round-76 derived slice is recorded in `.ufo/waves/round-76/w1/ScoutQuarantine.md:5-9`; its ids comprise S776, S778, S779, S786, S787, S791, S792, S795, S796, S804, S814, S816, S817, S820, S823, S824, S825, S827, S807, S812, S835. The trailing backticks on the three unreachable ids are identified as register-cell artifacts there. Its explicit 21-row table at `:24-47` carries each prior verdict unchanged.
- The committed round-76 lesson independently lists all 21 rows and carried verdicts at `corpus/lessons/round-76.md:37-65`, and states the same 10/7/4 tally and no upgrade/retirement at `:39`. This matches the round-71 table row-for-row.
- Comparing committed tree changes from base to Ca landing `a43ed807ea38b5fc5a7875a839d576cea73aba7c` and C landing `722e69ff6361aadf148cb46acbf6ac8fd147f59a` shows no change to `reports/round-71/telemetry/quarantine-verdicts.md`; the round-76 slice/table and lesson are additions, not amendments to standing verdicts. Frozen configuration is `df0f0309d61e5485bb17035d3f8791b1e6a11d40`.

## Disposition / residual risk

No quarantine row was upgraded or reopened: round 76 carries all 21 verdicts without re-fetching or claiming new verdict evidence. The earlier S807/S750/S777 id-text collision was a separate candidate-citation issue, not a quarantine verdict change; round-76 lesson `:65` says those staged citations were removed before admission. The known S778 lane-registry absence remains a reconciliation issue documented in the standing cross-check, but does not alter the 21-row slice or its verdict tally.

Verification was limited to committed files at the cited revisions and committed diffs; no builds, tests, linters, formatters, or tools were run/installed.