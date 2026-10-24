# CriticWaveShape — wave-shape audit

## Finding: claim O lacks explicit attack coverage for the non-new accept-o leg families

**Impact:** operability; wave-shape coverage. This is an allocation defect, not evidence that `accept-o.py` currently gives a false green.

`reports/round-65/claims.json` claim O freezes `ACCEPT-O-65` as every leg passing and enumerates 26 legs (lines 35–43). The O attack assignments are concentrated on the three new families: `RevCounterO` attacks FULL/MUTEX; `MutCounterO` mutates FULL/MUTEX/FRAG; `CriticPreO` asks about the do-nothing control, MUTEX, FULL, and predicate identity. `CriticControlO` maps the routed residuals, but does not ask for a leg-by-leg attack of the other accept-o legs. No O attack prompt explicitly challenges the remaining 23 leg entries: TOOL, INDEP, GEN, ORDER, BOUND, EXIT, PRIV, DEFAULT, ERR, REDIRECT, MALFORMED, GZIP, TRUNC, TIMEOUT, EDGE_SCHEMEREL, EDGE_USERINFO, EDGE_HTTPS, EDGE_MALTARG, EDGE_SLASHLESS, EDGE_308, EDGE_5TH200, DRIP, MUT.

This is a concrete gap against the requested “attack seats per leg family” check: a bypass/false-positive in an unaddressed family such as EDGE_USERINFO or GZIP has no assigned attack exercise. The prompts for C and Ca explicitly request leg-by-leg coverage (`CriticControlC`: “Walk accept-c.py leg by leg”; `CriticControlCa`: “Walk the nine legs”), while the O prompts do not.

**Smallest safe correction:** expand an existing O attack seat (preferably `CriticPreO`) to enumerate the non-new accept-o leg families and require an attack/control and expected leg verdict for each, or an explicit mapping when several legs share one implementation. This keeps the 64-seat cap and makes the intended family coverage auditable.

## Shape checks that pass

- `spec-v2.json` identifies `kotodama-r65-v2`, describes one v2 wave of 64 seats, and has 64 items. `taskcall-v2.json` also has 64 entries; its sorted seat names match the spec's sorted names.
- Attack-role mix is 14 reviewers + 9 critics + 6 mutation-testers = 29/64 (45.3%), above the 25% minimum (16 seats).
- All 35 non-attack-role/build items contain a lane-local `.ufo/waves/round-65/` output target; examples include ScoutRow01's row fragment, ScribeEntryBody's `stage/entry-spec.md`, ExecSeparability's manifest, and SentinelFinal's report.
- The two wave-rule lines are verbatim and present in all 64 spec prompts and all 64 taskcall prompts. All prompts also include the records-absent clause. Dependency-bearing prompts additionally give concrete absent handling, e.g. ExecGateFill, ScribeEntryAssemble, ScoutReopenA–C, and RevengerRouted.
