# R30-O14 — independent operability verification

**Verdict: integration-blocked, not all green.** The final dependency watch measured **37/40 current regression commands green**, with three parent-owned integration dependencies still red. Three routed fixes independently pass; the other two are documented with owner and reason rather than promoted to verified fixes. This is not round acceptance, promotion verification, or canon clearance.

Date: **2026-10-18**. Final measured instant: **2026-10-18T22:07:27+00:00**. Raw receipt: `reports/round-30/operability-verification.json`; regression outputs: `reports/round-30/regression.json`. Every command, observation date, exit, stdout/stderr and output digest is filed there. The verifier source at that observation is SHA-256 `2211ba8e5137248e1c7b9312ad1c9f3d7de194ab43906914fa37a0a4766f1c5a`.

## Reproduce

```sh
export TMPDIR="$PWD/.scratch" PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-30/verify-operability.py --selftest
python3 -B reports/round-30/verify-operability.py --wait 180
```

The exact commands above ran on **2026-10-18**: verifier selftest **7/7**, exit 0; the bounded dependency watch, exit 1. It made three 60-second pending notifications and a final measurement. `--wait` is capped at 1,200 seconds; `--check` prints JSON without publishing either receipt; `--regressions-only` measures the command matrix. Eight independent command workers run in parallel. Ordinary controls use temporary copies under `$PWD/.scratch`; frozen replay/mirror-safety selftests use `/var/tmp` and clean their mirrors.

The instrument does not run historical acceptance runners or receipt-writing gate-test runners. It compares emitted finding **lines**, not only saturated finding-class sets, and limits field changes to the top-level `register_law` block so the newly delivered earlier QREG fields cannot absorb a purported law tamper.

## Five independently checked routes

- **QREG dangles — verified bounded fix.** Clean delivered law CLI exits 0 with zero finding lines. A separate law-row `design_row: [QREG-99]` mutation exits 1 and adds `D4L-LAW-DANGLING`, naming RGL-04 and QREG-99. The actual cited QREG-05..08 now exist. This does not claim that proposed act records are a new executed domain or that broader law-prose limitations disappeared.
- **Law battery — registration verified, default baseline still missing.** Battery selftest is **44/44**, exit 0. The default battery runs seven structural selftests successfully and pins **19/19** discovered baselines, but coverage is **9/10**, exit 2: only `register-law-gate.py` is uncovered. An independently built fixture omitting only the law baseline also returns exit 2 and exactly 9/10, proving the new registration fails closed rather than silently omitting law.
- **X63-F2 — verified companion amendment.** `fixes/x63-f2.md` is a new, dated correction file explicitly withdrawing the false phrase-zero inference. The original corpus bytes remain preserved. A separate `git show 6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede:corpus/knowledge/linguistics/sound-symbolism.md` census independently finds the preexisting phrase at line 106, in the ideophone-field sense, rejecting the original zero. The historical auditor does not consume companion amendments and is not relabelled green.
- **Tokenless speaker tail — still open in delivered bytes.** A law-block `speaker: "no-such-speaker"` mutation still exits 0 with no added finding line; a separate `stamp-holder (ZZ-99)` mutation exits 1 and adds the named speaker finding. The delivered selftest is **29/33**, exit 1. The report-only owner's candidate is not a landed fix; the orchestrator must apply `fixes/speaker-tamper.md` to the shared gate and rerun the delivered CLI.
- **Telemetry durability — verified bounded fix.** The operating rule is present. Worker-observation and declaration snapshots now use distinct paths; both owner checkers execute successfully. Independently copying only durable telemetry and AGENTS into a disposable mirror, then deleting its scratch directory, still gives exit 0. Changing a source reference to `.scratch/claims.json` produces exit 1 with `non-durable-or-wrong-source:declared_request`; appending one raw-input newline produces exit 1 with `source-digest-mismatch:declared_request`. Historical missing samples are not recovered, and partial/null runtime counters are not converted into completion percentages.

Those counts and outcomes are from the dated `verify-operability.py --wait 180` receipt, not inherited owner assertions. Independent dangling, force, ID-bearing speaker and consequence CLI controls each pass; the deliberately tokenless speaker probe is the observed failing control.

## Initial defects retained, later state distinguished

The first dated sweep, retained in `regression-initial.json`, returned **32/40** exit-zero commands, no source movement, and preservation over **1,764** historical paths. Its broad initial matrix did not yet separate the immutable R28 generation control from current regression commands. The final inventory adds the generalized typed-pipeline selftest and explicitly separates that historical row: **41 actual commands = 40 current + 1 historical**. The different denominators are named, not normalized.

During integration this verifier identified two additional dependencies that later settled:

- A telemetry collision initially let two producers target incompatible `dispatch-stats.json` schemas. The declaration checker now reads `dispatch-declaration-x37.json`; both real checkers and the independent mirror controls pass on the final bytes.
- QREG's first successor-only hold-file approach stranded the v3 harness's conventional path. The owner replaced it with new predecessor/successor `pin_generations` rows in `expected-holds.json`, retaining historical pointers/digest, and an additive profile generation. The wider v3 selftest now passes. The **default v3 baseline remains stale**, which is a distinct remaining failure, not a continuing hold-path mismatch.

## Preservation and remaining work

The final sweep and independent probes both have **empty source-drift lists**. All **1,764** tracked protected report/frozen paths for rounds 8–29 match baseline `87bfc9956f0fc60e6821fe53b622d0043e28be10` in Git blob identity and mode, with no protected status rows. Manifest SHA-256: `c3bc68dd9c1f1e5bd875e873e543abb59cfa39d32a7860e6a0700b1dc76f9884`. Command/date: `python3 -B reports/round-30/verify-operability.py --wait 180`, **2026-10-18**. Finite before/after sampling proves endpoint byte/mode preservation, not absence of a transient rewrite.

The parent must, in order:

1. Land the candidate gate edit in `fixes/speaker-tamper.md`; rerun the delivered selftest and independent tokenless/ID-bearing controls.
2. Freeze a **new** default-root law baseline against those final gate and packet bytes; obtain default battery **10/10**, retaining seven structural execution legs.
3. Land a **new durable v3 baseline generation** and route the default regression to it. The current default rejects six changed read-set files at `E2E-DIGEST`; `--profile v3 --selftest` is green and the packet owner reports a green explicit fresh-baseline replay, but scratch-only freeze evidence cannot replace the default durable pin.
4. Rerun this verifier and the round counting command, then update the two documented resolution rows with their actual final evidence. Do not weaken digest checks, overwrite historical freezes, or count this blocked snapshot as a green sweep.

`python3 -B reports/round-30/run-validation.py --selftest` independently passed **44/44** on 2026-10-18. Its read-only `--check` was also executed and returned exit 1: C passed; O retained the same three current regression failures; D awaited the orchestrator's Register craft landing and post-landing box-1 receipt. An earlier check also caught this ledger's removed intermediate hold-file reference; the ledger was corrected to the final conventional path, and an independent `validate_resolution` replay now accepts all five rows: three fixed-with-control, two documented with owner/reason. No shared validation receipt was published by this seat.

## Write boundary

Only the assigned round-30 O13–O15 artifacts were written: `verify-operability.py`, `regression-initial.json`, `regression.json`, `operability-verification.json`, `regression.md`, `verify.md`, and `routed-resolution.json`. No shared tool, component, packet, corpus entry, bookkeeping file, filed round-8–29 artifact, or Git state was edited. Parent integration owns LOG.md and round adjudication; no commit or push was made.
