# Round-25 conformance defect sweep — R29-O01..O02

- **Audit date:** 2026-10-18.
- **Scope:** round-25 argot-derivation delivery, its production D4 evidence, and the gate-battery / hold-oracle integration boundary.
- **Mode:** read-only review of filed claims, runner source, receipts, and the independent review `reports/round-25/audit/o20-argot-leg-review.md`. No round validator was run for this sweep; quoted execution results are the dated measurements in that review.
- **Round state:** `reports/round-25/validation.json` records `acceptance_checks_passed: true`. These findings do not reverse that receipt or claim that the delivered argot gate is absent.

## Findings

### O01 — The production derivation leg passes over an empty derived-pair domain (known conformance boundary)

Claim D requires derivation rules for register-scoped forms to replay on D4 (`reports/round-25/claims.json:18-23`). The archived independent command `python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` measured on **2026-10-18** returned `records=156 register_scoped=6 derived_pairs=0 borrow_pairs=6 violations=0 rule_holds=0`, exit 0 (`reports/round-25/audit/o20-argot-leg-review.md`, §2). Thus the delivered packet exercises the borrow side but supplies no production derivation pair for the new arithmetic leg. Fixture mutations and selftests show the checker can discriminate; they do not establish that it checked a real D4 derivation.

The review explicitly called the clean result vacuous and the delta names the missing relation. Keep this as an **open coverage/conformance boundary**, not as a claim that the gate is broken or that the round's acceptance receipt was red. Whether the forecast remains deferred or must be delivered is a disposition for the owner, not this sweep.

### O02 — The argot leg has no standard-battery or expected-hold oracle entry

The typed-pipeline gate did acquire and execute `L3b-argot`; the round-25 runner separately registers `argot-gate-selftest` and `argot-gate-d4` (`reports/round-25/run-validation.py:174-175`). The narrower integration gap is confirmed by the dated audit: `grep -c "argot-derivation" tools/check-gate-battery.py` returned **0** on **2026-10-18**, and `D4L-ARGOT-*` is absent from `examples/culture-d4/expected-holds.json` (`reports/round-25/audit/o20-argot-leg-review.md`, §4). A green direct gate / typed pipeline therefore does not mean the standard battery or committed expected-hold comparison has an argot-specific entry.

Classify this as **battery/hold-oracle integration**, not as absence of all argot tests: the direct runner legs are present. The review records this as still open at its final sampled revision, while the gate's typed-pipeline wiring had already landed.

## Preservation boundary

This sweep makes no canon decision and does not regrade round 25. The numerical observations above are historical measurements dated 2026-10-18; no round-8–28 file was edited by this sweep.

FILES: reports/round-29/defects/sweep-r25.md | SUMMARY: the delivered derivation gate has no production pairs to grade, and its battery/hold-oracle integration remains incomplete.
