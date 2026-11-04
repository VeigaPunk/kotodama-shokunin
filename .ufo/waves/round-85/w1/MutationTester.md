# MutationTester — round 85, v1

Axes: depth, operability, calibration.

**Result: seven mutants killed, one survived, none inconclusive.** Each detector ran on clean, mutated and restored bytes; every baseline/restored run exited 0. Exact before/mutant/after hashes, commands, rc, outputs and unified diffs are retained in `.ufo/waves/round-85/w1/stage/MutationTester/mutation.md`, `.ufo/waves/round-85/w1/stage/MutationTester/results.json`, and their per-mutant receipts.

| Probe | Baseline / mutant / restored rc | Finding / verdict |
|---|---|---|
| S919 source URL Metallurgy → Bronze_Age, shape retained | 0 / 0 / 0 | **Survived** structural D counter |
| Anchor → unregistered S99999 | 0 / 1 / 0 | SOURCED; killed |
| S921 source row omitted | 0 / 1 / 0 | SOURCED and ROWS; killed |
| S919 HTTPS scheme removed | 0 / 1 / 0 | ROWS; killed |
| Nonce index row omitted | 0 / 1 / 0 | MISSING_ROW; killed |
| Nonce index row duplicated | 0 / 1 / 0 | DUPLICATE_ROW; killed |
| Last footer total 1 → 2 | 0 / 1 / 0 | FOOTER_TOTAL; killed |
| Canned always-clean auditor, fake 99-check selftest | 0 / 1 / 0 | Frozen O MISSING/DUPLICATE/FOOTER/ERROR fail; killed |

The stale historical **first** footer remains at 999 in each green nonce control. Candidate SHA-256 `8d57afd0801e9ea78b6f95ab48b80cc3bc08c2eff02a83a9496ff7dd51317b71`; independent selftest exit 0, 23 checks. Unchanged base index exits 1 with ten findings. Raw receipts: `.ufo/waves/round-85/w1/stage/MutationTester/candidate-selftest.txt` and `.ufo/waves/round-85/w1/stage/MutationTester/candidate-base-index.txt`.

## Calibration and limitations

- **No commits permitted:** frozen counter reads committed blobs. The probe imports byte-exact frozen measure85 and substitutes only fixture blob transport/path enumeration. Frozen predicates and constants are unchanged. These are **transport-overlay sensitivity experiments, not committed-revision acceptance**. Printed revision/tree stamp lines refer to the backing freeze, not mutated fixture bytes.
- D substrate is explicitly synthetic; no historical/source-authenticity claim. O clean substrate uses the actual candidate, base corpus, ExecIndexReading README reconciliation, and a synthetic gates registry naming the two required paths. Clean/restored frozen O runs pass 10/10; canned tool passes only 6/10.
- Source adulteration survives because ROWS binds URL/quote shape, not source identity. This is a scoped coverage finding, not permission to accept Bronze_Age or rewrite frozen targets. L1 must independently bind actual S919–S922 source URLs and quotations.
- **Historical correction:** contrary to frozen descriptive prose, pinned base round-28 sweep already selects the last matching footer (`matches[-1]`, lines 113–118). It already was an index checker. Evidence: `.ufo/waves/round-85/w1/stage/MutationTester/r28-footer-provenance.txt`. Do not count last-well-formed-footer selection alone as newly acquired capability. Explicit root, effective duplicate failure and malformed-final-header refusal remain distinct successor behavior.

Actual unmodified frozen CLI controls also ran at both base and freeze: both D/O fail as expected before data. Their four `control-*.txt` receipts are retained; red pre-data controls were not used to claim mutant kills.

## Restoration and handoff

All eight restorations are exact; scratch removed; zero clones, commits, production/sibling edits, installs or upgrades. Evidence: `.ufo/waves/round-85/w1/stage/MutationTester/cleanup.json`.

L1 should run the actual frozen CLI against its eventual integrated revision for both claims. Reproducer and retained candidate inputs are in the stage directory; no production code is proposed by this seat. No builds, linters or unrelated tests ran.
