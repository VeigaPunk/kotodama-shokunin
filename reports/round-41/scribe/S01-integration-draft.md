- Seat: S01 | scribe | cross | date 2026-10-19 | baseline 456674d

## Fleet-report material

Draft only: this is report material for the integrator, not a landed-work or admission claim. The round is regimen 2, loop 1, position 9 (mid-loop verify), baseline `456674d`; the declared dispatch is one batched `openai-codex/gpt-6-luna-max` call requesting 32 workers. Actual launch/completion counts are not established by the declared allocation record and must come from observed telemetry. (REGIMEN.md:18-19; reports/round-41/claims.json:5-8; reports/round-41/telemetry/dispatch-declared.json:2-14)

**Work performed (draft):** Verify the operability runner-template/conformance-checker claim and calibration pin-supersession claim. Freshness remains paused; no promotion, canon, clearance, or closure is in scope. (reports/round-41/claims.json:9-10,26-28)

**Landed changes:** Leave this section pending integration evidence. The declared deliverables are the runner template, checker and census; queue-v2 disposition evidence for N7 and the r39 runner-root regression; and the pin-supersession record plus exact SKILL/SCORECARD deltas. No S01-owned source change or independent acceptance result is asserted. (reports/round-41/claims.json:12-24; reports/round-41/targets.json:41-52,76-87,125-157)

**Before → required after (not measured here):**
- **O / operability:** Before is six absolute-ROOT/chdir runners r34-r39, four receipts with `runner_sha256: null`, stale/duplicated r39 findings, and no reusable template. Required after is a five-point template, checker selftest, defect-class census, and queue-v2 rows fixed-with-evidence. The actual census and all checker results remain to be integrated. (reports/round-41/claims.json:12-18)
- **Ca / calibration:** Before is live-file references to pre-r38 argot bytes; required after is a dated supersession record, refreshed live rows, explicit filed-reading exceptions, no unmarked stale live references, and two independent verifiers. The live argot gate digest measured at this seat is `10c884337fbb2b8f5cc64bedb70e2ddbc34b84c17aaa29fb9be15d049b324a75` (`sha256sum tools/gates/argot-derivation-gate.py`). A read-only search for `8c7dd098|b5406bcd|15f8b232|10c884337fbb` found one hit in `SKILL.md:383`; its surrounding text calls this a measured past reading and says it is superseded (`SKILL.md:382-388`). The same search returned no matches for `SCORECARD.md`, `corpus/README.md`, or `AGENTS.md`. Preserve/classify the SKILL row as a historical quote unless the pin scout establishes otherwise; do not count it as a current pin. (reports/round-41/claims.json:19-24; reports/round-41/targets.json:21-24)

**SHONEN:** No promotion or canon conclusion. Any capability wording should remain conditional until the checker, census, pin record and verifier evidence have landed and the round's validation receipt has been produced. (reports/round-41/claims.json:26-28)

## Validation-leg spec

Use these as acceptance legs in the round-41 validation integration; do not treat missing artifacts or `could-not-evaluate` as green.

1. **Template/checker contract (O):** Require `templates/round-runner-template.py` and `tools/harness/round_runner_conformance.py`. Verify the template's five declared points: relative `ROOT = Path(__file__).resolve().parents[2]`; no `chdir`; `guard_receipt` dominates receipt publication; `runner_sha256` is non-null; findings/limits are round-specific. Run `python3 tools/harness/round_runner_conformance.py --selftest` and require all controls to pass. (reports/round-41/claims.json:14,17-18; reports/round-41/targets.json:44,51)
2. **Census (O):** Run the checker `--json`; require a row for every explicitly resolved runner path and named defect classes per row, and compare it row-for-row with the independent predicted census and verifier results. Require r40 to pass as the reference shape. Do not infer classes or pass from a total count alone. There is an unresolved denominator conflict: the claim says seven runners r34-r40 (seven paths), but its threshold and K01 mission name r33-r39 plus r40 (eight paths). The matching glob found r33-r39 runners, and `reports/round-40/run-validation.py` is also present. Resolve the exact manifest before setting an expected row count; until then this leg is blocked, not green. (reports/round-41/claims.json:14,18; reports/round-41/targets.json:16)
3. **Queue-v2 (O):** In the new round-41 queue artifact (never edit the filed round-40 queue), require `N7-receipt-fidelity` and `r39-runner-root-regression` to be `fixed-with-evidence`, with verification pointing to the landed template/checker and the measured census. Preserve all unrelated row history. (reports/round-41/claims.json:16; reports/round-41/targets.json:79-80; reports/round-40/op/defect-queue-v2.json:370-377)
4. **Pin refresh (Ca):** Verify the supersession record names each refreshed live row, its source surface, replacement digest, and any retained historical/filed reading. Recompute the current argot-gate SHA-256 and require it to match the record's new digest. Search all identified live surfaces (at minimum `SKILL.md`, `SCORECARD.md`, `corpus/README.md`, and `AGENTS.md`, plus live claims/validation cross-references); every remaining pre-r38 digest occurrence must be explicitly classified as historical. The claim's listed grep omits AGENTS and live claims/validation references, while K02's scout scope includes AGENTS and the law-gate pin if touched; reconcile that inventory before accepting a zero/marked-historical result. (reports/round-41/claims.json:20-24; reports/round-41/targets.json:21-24)
5. **Independent verification (Ca):** Require both verifier outputs to establish exactly-once delta anchors and historical-quote classification against the live tree after drafts are applied. Every mismatch, unavailable file, or unresolved stale hit stays a named failure/owed item; do not rewrite rounds 1-40. (reports/round-41/targets.json:134-157; reports/round-41/claims.json:22-24)
6. **Receipt boundary:** The declared round command is `python3 reports/round-41/run-validation.py`, but this seat did not execute it. Per the shared rule, no round runner may be executed in-tree; any parent verification must use an isolated copy and preserve the measured tree/receipt evidence. Checker selftest and `--json` are the separately declared O counting commands. (reports/round-41/claims.json:17,23; reports/round-41/targets.json:4-9)

## Owed

- `reports/round-41/op/O02-checker.md`, `op/O03-predicted.md`, `op/O04-verify.md`, `op/O05-traps.md`, and `op/O09-r40-verify.md`: checker implementation, independent census baseline, and verification evidence were not present at this seat's read time.
- `reports/round-41/op/O06-queue-update.md` and the integrated round-41 queue-v2 artifact: needed to verify both required row dispositions.
- `reports/round-41/calib/Ca01-supersession.md`, `calib/Ca02-skill-delta.md`, `calib/Ca03-scorecard-delta.md`, `calib/Ca04-verify.md`, and `calib/Ca05-verify.md`: needed to close the calibration legs.
- Resolve the seven-versus-eight runner denominator before the census threshold is adjudicated. Do not mark O or Ca admitted from this draft alone.

## Citations

- `REGIMEN.md:18-19,34-50` — position 9 and required report/receipt record.
- `reports/round-41/claims.json:5-28` — declared dispatch, claims, thresholds, and non-goals.
- `reports/round-41/targets.json:4-9,16,21-24,41-52,76-87,125-157` — shared boundaries and seat deliverables.
- `reports/round-41/telemetry/dispatch-declared.json:2-25` — declared allocation, digest sources, and open closing snapshot; no observed completion count.
- `SKILL.md:382-388` — historical b5406bcd reading and explicit supersession wording.
- `reports/round-40/run-validation.py:5-12,227-247` — r40 relative-root reference and runner publication path; read only, not executed.
- `reports/round-40/op/defect-queue-v2.json:370-377` — N7 queue row and intended cure location.
- Command output: `sha256sum tools/gates/argot-derivation-gate.py` → `10c884337fbb2b8f5cc64bedb70e2ddbc34b84c17aaa29fb9be15d049b324a75`.
- Read-only search output: pattern `8c7dd098|b5406bcd|15f8b232|10c884337fbb`; only `SKILL.md:383` matched among SKILL.md, SCORECARD.md, corpus/README.md, and AGENTS.md.
