# R30-X38 — law-gate clean-state spot-check

Seat: SCRIBE X38. Date: 2026-10-18. Claim: O / operability, specifically the law-gate clean state after the QREG dangle repair. Axes: operability (clean replay with discriminating controls), calibration (dated commands and exact input digests), depth (independent record-resolution check). NON-CANON engineering evidence; not round admission, promotion verification or canon clearance.

## State

**QREG dangle repair verified with a discriminating control; the broader law-gate regression state is NOT GREEN.** At `2026-10-18T21:58:18Z`, raw and typed law replay both exited 0 with zero findings, and a fresh dangling reference still produced its named HOLD. The unchanged delivered gate's self-test is 29/33 and the tokenless-speaker control remains silent. The orchestrator must integrate the report-only speaker/self-test candidate before claiming the full routed item or regression suite closed. No gate or packet was repaired by this seat.

## Before observation

At `2026-10-18T21:52:42Z`, these real CLI commands produced four dangling-reference HOLDs in the raw packet and a passing 33/33 self-test:

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B tools/gates/register-law-gate.py --packet examples/culture-d4/packet.d4.yml
python3 -B tools/gates/register-law-gate.py --selftest
```

The later machine-readable baseline, measured `2026-10-18T21:53:45Z`, is `reports/round-30/audit/x38-law-gate-baseline.json`:

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-30/audit/x38-law-gate-clean-state.py --receipt reports/round-30/audit/x38-law-gate-baseline.json
```

- Both packet forms exited 1 with four `D4L-LAW-DANGLING` HOLDs: RGL-01 → QREG-05/QREG-07; RGL-02 → QREG-06; RGL-03 → QREG-08.
- Each carried five law rows and four register records; there were 179 distinct top-level record IDs in the raw packet and 180 in the typed packet. Ruby's full YAML parser independently reproduced all four unresolved references; no lane parser was imported by that cross-check.
- Planted CLI controls caught a fresh dangling reference, an invalid force, an explicit unknown speaker ID, and a machinery-free consequence (4/5). Tokenless `speaker: "nobody-nowhere"` added no finding (the separately routed speaker tail).
- The gate self-test was 33/33, but its delivered-packet check required a nonempty baseline finding set. The dangle repair's own owner also identified this clean-state dependency in `reports/round-30/fixes/qreg-dangles.md`.
- The baseline caught in-flight assembly/projection drift during parallel component integration; those dated exits are not a final regression verdict.
- Instrument correction: the baseline's argot command incorrectly supplied `--packet`, which that gate does not accept. The audit instrument now uses its documented positional packet argument. Preserve the baseline as the actual initial observation; do not read that usage-error exit as a delivered argot defect.

Observed baseline law gate SHA-256: `bbad35784bfb463d41912908748ebb711f72109d811d0dc8f0110657e3b4c026`; raw packet: `543d68a82640e1b0c53b9cb7cb26c4dc60fce5878c2bf487050ead3af0945c4f`; typed packet: `15c81ec11b42efaa7d683dd9320bfc7cd9b5d1e812e042d99dbf8d8726ec5da6`. Full digests, command outputs and UTC timestamps are in the baseline receipt. The measured lane HEAD was `44145d5f337dea425c20dccafee98e0882678660`; the claim's declared baseline is separately recorded in `reports/round-30/claims.json`.

## Final observation — dangles closed; delivered gate regression remains

The following command first completed at `2026-10-18T21:58:18Z` and was repeated on the current instrument at `2026-10-18T22:02:05Z`–`22:02:06Z`, with the same outcome. The latest receipt is `reports/round-30/audit/x38-law-gate-clean-state.json`; its command, per-leg timestamps, exact outputs, independent-parser results and before/after input digests are the counting record.

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-30/audit/x38-law-gate-clean-state.py --receipt reports/round-30/audit/x38-law-gate-clean-state.json
```

**Dangle-fix result: verified with control.** Both delivered packet forms exit 0, with `law_rows=5`, `identity_rows=8`, `dangling=0`, `findings=0`. The raw packet has 183 distinct top-level record IDs and the typed packet 184. Independently parsing each through Ruby YAML finds QREG-01..08 and resolves all four RGL design-row references. The raw/typed law clauses and references agree. Comparing their stored `law_fields` to the baseline receipt preserves every RGL act, speaker, holder, force and consequence; the new QREG-06 explicitly retains the binding-oath refusal rather than adopting the historical positive oath proposal.

The fresh-dangle control replaces only RGL-01's `design_row` with `[ZZ-99]`; the real gate exits 1 and emits exactly one `D4L-LAW-DANGLING: HOLD` naming that row and token. Thus zero clean findings is obtained by supplying the missing records, not by weakening the resolver. Scoped invalid-force, explicit-speaker-ID and consequence controls each likewise exit 1 with their named finding. Restored clean packets are rerun after all controls. Temporary copies under `.scratch/` are removed automatically.

**Outstanding: X38 is NOT GREEN overall.** Only four of five negative controls pass. The tokenless RGL-01 speaker `nobody-nowhere` still returns exit 0 with zero finding lines. The delivered self-test returns exit 1, `29/33`: `delivered-packet-replays` plus all three delivered force/speaker/consequence tail checks fail. The first requires `bool(base)` on a genuinely clean packet; the three global first-match substitutions now change earlier QREG identity-row fields instead of the `register_law` block. X38's own control transformer is law-block-scoped, so it does not inherit that false coverage.

All four adjacent regression commands in the latest receipt pass:

- `python3 -B tools/assemble-culture-d4.py --check`: exit 0, byte-identical deterministic raw packet.
- `python3 -B tools/assemble-d4-typed.py --check`: exit 0, byte-identical deterministic typed packet.
- `python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml`: exit 0, 20/20 legs; the declared open design holds remain open. At the latest `22:02:05Z` call, the profile hashes `76ecdfdcbf09…` and references `examples/culture-d4/expected-holds.json` at `e6ae9828d6c8…`, through a new first-match R30 profile row that retains the earlier D4 row. The earlier `21:58:17Z` call used provisional profile `b42ebfaf9016…` and `expected-holds.r30-qreg.json`; these are different dated input generations, not byte-identical replays of the same profile. X38 did not change either pin surface.
- `python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml`: exit 0, eight derived pairs, eight claimed chains, six borrow pairs, zero violations and rule holds.

The final snapshot remains byte-stable over the measured inputs. Raw packet SHA-256: `aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3`; typed packet: `d581e0ad5384ce56622839b6ae4d6cf8b5a4447300cf7d8cd295f3efea0c9182`. The gate remains the baseline `bbad35784bfb463d41912908748ebb711f72109d811d0dc8f0110657e3b4c026`; component 13 also retains its baseline digest. Syntax parsing of the X38 instrument passed, and `git diff --name-only -- reports/round-{8..29}` showed no filed-report edits at `2026-10-18T21:58:18Z`.

## Dependency wait and parent action

The `--wait 1200` attempt sampled at `21:54:14Z`, `21:55:14Z`, `21:56:14Z` and `21:57:14Z` on 2026-10-18; every sample had raw/typed exit 0 and self-test exit 1. It was intentionally stopped after reading `reports/round-30/fixes/speaker-tamper.md`: that worker's scope is report-only, and the candidate must be installed by the orchestrator. Continuing to wait for a parent-owned edit before handing results to that parent would create a circular integration dependency. The stopped wait produced no final receipt; the foreground command above produced the filed receipt. No background task is left running by X38.

**Owner: Round-30 orchestrator.** Land the speaker/self-test candidate described in `fixes/speaker-tamper.md`, then run its delivered self-test and the X38 instrument again, filing a new post-integration receipt rather than treating candidate-only 45/45 results as delivered success. Ensure the round runner scopes its tampers to RGL law fields. Any law baseline or pin needed by battery registration must name the final gate bytes in a new generation. Do not count the broader O regression clause closed on this seat's current finding-free packet alone.

## Write boundary

Only this seat's `reports/round-30/audit/x38-*` evidence is authored. No gate, component, delivered packet, shared bookkeeping, pin row or filed round-8–29 artifact is edited by this seat; no commit or push. The parent owns integration into LOG.md and whole-round adjudication. This spot-check does not substitute for battery registration/coverage or the other four routed-item dispositions.
