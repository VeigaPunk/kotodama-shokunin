# CriticPreO — claim O pre-data review

## Findings

### O1 — Filtered runs can still emit a green verdict (high)

`accept-o.py` says `FULL` re-executes the complete battery, but it only does so when `need("FULL")` is true (lines 1119–23); `need` is false for a filtered invocation that does not select `FULL` (lines 447–50). The `leg` helper prints `SKIP` for unselected legs without adding them to the verdict list (440–45), and the final verdict is `all(legs)` (1235–42). Thus `--only GEN` can produce a successful selected leg, skip `FULL`/other legs, return 0, and still print `ACCEPT-O-65: PASS [filtered: ...]`. This is a control-flow counterexample inferred from the code, not a run. The suffix and `SKIP` lines expose the filter, and such output does not literally satisfy “every leg ... prints PASS,” but the green verdict re-presents the filtered-green class the claim says FULL closes.

**Smallest safe correction:** filtered invocations must not emit an affirmative `ACCEPT-O-65: PASS` or success exit as the overall verdict. Keep per-leg filtering for diagnostics, but make the complete verdict require the exact expected leg set, each exactly once and PASS. Give FULL's internal subprocess an explicit internal mode (or otherwise validate its selected battery separately) so this stricter public verdict does not break the self-test.

### O2 — MUTEX is falsifiable; its committed receipt binding is weaker

The disclosed expected failure sets are executable: `SWEEP_EXPECT` is hardcoded (1141–52), measured failing legs are collected from each mutant run (1170–80), and `measured != expect` makes MUTEX fail. The pre-data `dry-run-o.txt` records m6 and m7 as measured `[]` rather than the expected `EDGE_308` and `EDGE_5TH200`, and records MUTEX FAIL. This demonstrates a falsifiable criterion, not merely descriptive prose.

There is a provenance hole in the committed-table check: the code compares only the final `len(sweep_rows)` lines of `exactness-sweep-o65.txt` with live rows (1192–1200). A stale or misleading header, command, or tool hash can survive if the last ten rows match. The receipt is absent in the pre-data telemetry, and the promised `reports/round-65/telemetry/controls-o.txt` (named at accept-o.py:106–07) is also absent from the telemetry listing.

**Smallest safe correction:** compare the complete committed file with generated `sweep_text` (including header/hash/command), and retain a committed O forcing-control receipt. The live expected-set comparison itself is a sound falsifier.

### O3 — The available no-op baseline fails overall, but FRAG is vacuous on empty rows

`dry-run-o.txt` is a negative base receipt: the ordinary round-64 battery legs pass, but FULL fails (`pass=21/23`, with three skips) and MUTEX fails, so this recorded do-nothing state does not satisfy the frozen O predicate. It also shows FRAG PASS with `FRAG: 0 finding(s) in 0 file(s)`. `accept-o.py` only requires the checker to exit 0 and its output to contain `0 finding` (1213–24); it does not require any row fragments or the expected S750–S775 IDs. The checker accepts a present empty rows directory with no findings. Therefore FRAG can claim closure without scanning a single row.

The exact 26 expected O leg names are present in `claims.json` and in the counter's `ALL_LEGS`, and the O predicate sentence matches: `ACCEPT-O-65: every leg of reports/round-65/accept-o.py prints PASS.` A round-64 counter form lacks FULL/MUTEX/FRAG and is not an exact match for that frozen leg set; the available base dry-run does fail. However, the script does not load/bind itself to `claims.json`'s expected set, and O has no separate forcing-control receipt, so the evidence does not independently demonstrate rejection of every stale-counter form. Also, the filter behavior in O1 lets an incomplete set produce a green-looking summary.

**Smallest safe correction:** have FRAG require the expected nonempty fragment set (ideally exactly S750–S775), in addition to zero findings. Preserve the expected-leg-set check in the actual verdict path, not only in the claim prose.

## Impacted axes

- **O (operability):** filtered green can be presented; FRAG can pass vacuously.
- **Records/provenance:** MUTEX currently validates measured table rows but not the committed receipt's header and identifying metadata.

## Evidence read

`reports/round-65/claims.json` claim O; `reports/round-65/accept-c.py`, `accept-o.py`, `accept-ca.py`; `tools/check-row-fragments.py`; `reports/round-65/telemetry/controls-c.txt`; and all present `dry-run-*.txt`. Telemetry directory contains no `controls-o.txt` or `exactness-sweep-o65.txt` at this pre-data snapshot.

Report: .ufo/waves/round-65/w1/CriticPreO.md
