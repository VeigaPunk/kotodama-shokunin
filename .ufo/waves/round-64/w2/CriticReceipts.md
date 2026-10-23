# CriticReceipts — round-64 wave-2 telemetry integrity

## Scope and axes

- **Coverage:** receipts must support the actual entry/row work, not merely registry-shaped output.
- **Operability:** complete, correctly scoped counter output and identifiable executable bytes.
- **Calibration:** truthful run independence, revision attribution, historical forcing evidence, and measurement counts.

This is an evidence critique, not claim acceptance, admission, integration, or a round judgment. No receipt, counter, tool, index, jj state, or git index was edited. No counter, native judge, agent runtime, build, or test was invoked. Only this requested report was written.

Audit source snapshot: final hash observation at **2026-10-24T02:53:24Z**. C changed during this audit; O did not. All ten requested receipt files exist. The four declared O receipts are now present and the final O receipt is complete: the earlier wave-1 absence/truncation findings are historical, not current defects.

## Inventory and output-shape audit

Paths below are under `reports/round-64/telemetry/`. Counts come from static receipt parsing and `wc -lc`, not fresh acceptance runs.

| Receipt | Bytes / lines | Observed shape | Integrity assessment |
|---|---:|---|---|
| `dry-run-c.txt` | 999 / 14 | 11/11 named C legs; 8 FAIL, 3 PASS; `ACCEPT-C-64: FAIL`; `exit=1` | Complete historical baseline output. No counter hash/command; no longer matches current ONEID detail format after concurrent C revision. |
| `dry-run-ca.txt` | 491 / 9 | 6 FAIL legs; `ACCEPT-CA-64: FAIL`; `exit=1` | Historical rev0 output; **REVNAMES absent**, so not a seven-leg current-counter baseline. |
| `dry-run-o.txt` | 397 / 7 | TOOL through PRIV, all PASS | **Partial:** 16/23 legs absent; no terminal ACCEPT verdict or process-exit trailer. |
| `dry-run-o-baseline-copy.txt` | 397 / 7 | Exactly the same seven lines and random IDs | **Duplicate partial**, not independent baseline evidence. |
| `final-measures-o.txt` | 3847 / 29 | All 23 legs in declared order, all PASS; complete ten-mutant kill list; `ACCEPT-O-64: PASS`; `exit=0` | Complete rev3 capture; counter/tool hashes match current bytes. Not itself a canonical claim judgment. |
| `mut-o.txt` | 2840 / 27 | MUT PASS, 9 SKIP lines, verdict, `exit=0`; ten mutant-source hashes | Complete capture of the current selected-mode implementation, but **13 core SKIP slots are omitted** contrary to the documented output contract. Not a full O run. |
| `edge-o.txt` | 1561 / 16 | Seven EDGE legs + DRIP PASS; 2 SKIP lines; verdict; `exit=0` | Complete selected-mode capture with the same omitted 13 core slots. Not a full O run. |
| `control-o.txt` | 2972 / 42 | r63 no-match receipt (`grep_exit=1`), r63 unsupported-selector error (`exit=2`); then GEN/MUT PASS, 21 SKIP, verdict, `exit=0` | Complete for its two explicitly named controls. Cosmetic tool hash matches surviving scratch source. |
| `census-start.txt` | 3235 / 29 | 27 W04, 1 W03, final `kotodama\tok\t…` | Complete-looking **validate-mode** lane output; no command, exit, revision, producer hash, or registry hash recorded. |
| `census-wave1.txt` | 3451 / 31 | Two headers + identical 29-line validation body; header names command and exit 0 | Consistent validation result, not a numeric census or post-repair measurement. No source/producer digest recorded. |

For both selected O receipts the omitted names are exactly: INDEP, GEN, ORDER, BOUND, EXIT, PRIV, DEFAULT, ERR, REDIRECT, MALFORMED, GZIP, TRUNC, TIMEOUT.

## Counterexamples, defects, and smallest safe corrections

### R1 — HIGH: two O dry-run receipts terminate mid-run

**Evidence:** `dry-run-o.txt:1-7` and `dry-run-o-baseline-copy.txt:1-7` end at PRIV. Neither contains DEFAULT through MUT, `ACCEPT-O-64:`, or an exit trailer. The inner text `PRIV PASS exit=1` is a subprocess detail, **not** the counter's process-exit receipt. A full current O run prints 23 legs then the verdict (`accept-o.py:443-445,1110-1112`).

Neither file records its counter version, measured revision, command, or even whether the r63 or r64 counter produced it. These common core lines alone cannot identify the instrument. They establish no complete O baseline result and no negative EDGE/DRIP control.

**Axes:** operability, calibration. **Smallest safe correction:** preserve both historical partials; append an erratum classifying them as aborted/partial and do not count them as full runs. Main should file a separately named, fully captured and hash-bound baseline/control receipt if required. Never manufacture their missing tails.

### R2 — HIGH: duplicate filenames supply only one distinct O observation

**Executed static comparison:** `cmp reports/round-64/telemetry/dry-run-o.txt reports/round-64/telemetry/dry-run-o-baseline-copy.txt` returned no differences. Both SHA-256 values are:

`635a16b04356ef30522fbc00850f42c161d22d8b6c607173f845442f019877d8`.

The equality includes S2101/S2377/S2378 in the randomized PRIV fixture. This corroborates ReviewerCounterO2 M3: two paths are not two independent experimental observations. Nothing in the filenames demonstrates an independent r63-baseline run.

**Axes:** calibration, operability. **Smallest safe correction:** disclose one distinct captured payload and treat `baseline-copy` as a copy only. Use the separately recorded r63 control in `control-o.txt:11-16` for its narrow no-EDGE/DRIP/unsupported-selector proposition; it does not reconstruct a missing full baseline run.

### R3 — MEDIUM: Ca's baseline is six-leg history, not seven measured failures

`dry-run-ca.txt:2-7` prints CANONLOG/PTRS/HISTOGRAM/DISPO/NITS/R63SEP only. `claims.json:56` declares seven legs. Current `accept-ca.py:138-141` explicitly explains the old omission: rev0 computed REVNAMES but never printed or counted it. Its FAIL verdict is not truncated; it is an obsolete-instrument result.

The surviving wave-1 `CriticCa.md:33-45` supplies a separately executed seven-FAIL before run at current Ca hash `f222648e…`. That is supporting evidence, not an extra line present in the filed baseline.

**Axes:** calibration, operability. **Smallest safe correction:** retain the original six-leg receipt and explicitly label its instrument revision. Cite or separately preserve the actual seven-leg forcing/baseline capture under its own identity; do not relabel six observed failures as seven or insert an invented REVNAMES line.

### R4 — MEDIUM: observed C source drift makes the baseline's current-byte attribution false

C changed while this audit was active:

- Initial `accept-c.py`: `4df7b32b430282c81970acf9b6565c6ef96e598038f82ca843a2cace2de08a68`.
- At 02:53:24Z: `073e9716188251773c14c90b26f524454191c1cbf2b41793bfe5b3d4826fd23e`, docstring revision 3, read snapshot `2A2E`.
- Declaration-commit C blob: `3519c9c8ddca8dc556cca0646e9926d06b7c43a2d4af2e7985ca7f6062a09849`.

The new ONEID output unconditionally appends `citations_exactly_once=`, `missing=`, and `duplicates=` (`accept-c.py:279-283` at snapshot `2A2E`). `dry-run-c.txt:5` contains none of these. Thus it cannot be the full raw output of the newly observed counter bytes, even though the eleven leg names still match. The receipt records no counter hash at all. Its base-tree revision identifies the input tree, not which later counter measured it.

**Axes:** coverage, operability, calibration. **Smallest safe correction:** preserve the baseline as historical; pin each authorized counter revision and its forcing receipt, then create new separately named output bound to the actual counter digest. Do not reuse this receipt as current-byte evidence. CounterDrift and RevVerifyC were notified.

**Concurrent-repair prerequisite, not a tested receipt result:** snapshot `2A2E` also reads `teaches = cells(row)[6]` before assigning `row` for the current `sid` in RESTATE (lines 296 versus 300). This uses a prior row rather than the intended current row. The exact static location was sent to RevVerifyC/CounterDrift; this critic neither executed nor edited that in-flight repair. Future receipt generation must not be treated as proof that this guard is correct without the owner's forcing control.

### R5 — HIGH: O rev1/rev2 still cite a missing historical forcing receipt

`accept-o.py:94-112,1082-1086` says `final-measures-o.txt` preserves an earlier full run under counter hash `bb0c74a486ae53ebc9a09787670020b69a03ef373df68f04fee8a30a827bf280`, including all mutant failures. The actual file now records **rev3 / c27a9fef…**, MUT PASS, and exit 0. It is not that historical receipt.

The exact prior file survives at `/home/vgpnk/.cache/hyaku/kotodama-r64-w1/ExecCounterO/prior-partial-final-measures-o.txt`, SHA-256 `aef3faf6edf5834670b4ea4da7ed5342cc4f5c800048010d451171ee1a9183e4`. Direct reading confirms 22 PASS legs ending at DRIP: no MUT, no terminal verdict, no exit, no counter hash. It cannot substantiate the docstring's all-mutant observation. `ExecCounterO.md:235-243` explicitly records that the cited bb0c74a4 measurement is unavailable/unreconstructible. Searching the round artifacts found references to that hash, not a surviving matching full receipt.

**Axes:** calibration and operability; this is missing historical evidence, not current O hash drift. **Smallest safe correction:** append a provenance erratum stating the old forcing receipt is missing, and preserve the available partial without upgrading its evidentiary status. Any further authorized pre-data revision needs its own actual forcing capture. A new run can demonstrate behavior now but cannot retroactively become the missing historical run.

### R6 — MEDIUM provenance limit: O's named git revision does not contain its counter

All four O headers name `b7d22703dfb684713826a4064e614264867e8cd`. Read-only git resolves that valid 39-character abbreviation to:

`b7d22703dfb684713826a4064e614264867e8cd2`.

Its parent is correctly `097c21d0eba5023cfd38b767fb41d59409eef125`. However:

```text
git show b7d22703dfb684713826a4064e614264867e8cd:reports/round-64/accept-o.py
fatal: path 'reports/round-64/accept-o.py' exists on disk, but not in 'b7d22703dfb684713826a4064e614264867e8cd'
```

The attempted `git show … | sha256sum` also printed the SHA-256 of an empty stream after that fatal error; that empty-stream hash is **not a counter digest** and was not accepted as one.

The headers explicitly say working-copy bytes and do supply the correct counter SHA. Consequently this is **not a fabricated/nonresolving revision and not a current content-hash mismatch**, but a git-tree-only replay cannot recover the measured executable. The header's revision alone is insufficient provenance.

**Axes:** calibration, operability. **Smallest safe correction:** preserve the headers/receipts and append a manifest distinguishing the historical working-copy observation from its base commit, retaining the exact content-addressed counter snapshot and linking its eventual carrying commit. Do not describe the named git tree as containing all measured bytes.

### R7 — MEDIUM: selected receipts violate the advertised complete SKIP shape

`accept-o.py:18-19` promises every unrun leg prints `<LEG> SKIP`. `mut-o.txt:16-27` has only 10 leg-status lines (1 PASS + 9 SKIP); `edge-o.txt:5-16` likewise has 10 (8 PASS + 2 SKIP). The 13 core statuses are absent because `run_core=False` skips their entire block (`accept-o.py:443-445`), not because either capture was cut short.

Static byte comparisons against ExecCounterO's surviving raw captures were **True** for final, MUT-only, and EDGE-only outputs after excluding only the installed comment headers. The installed cosmetic-control receipt also ends with the exact raw control capture. Therefore these selected receipts are authentic to the observed implementation, but not conformant to its documented full status shape. `ExecCounterO.md:187-189` additionally claims the other 22 legs print SKIP in MUT-only mode; the receipt actually contains 9 SKIP lines.

**Axes:** operability, calibration. **Smallest safe correction:** preserve the outputs and append the scope/count erratum. The authorized counter owner should emit explicit core SKIP slots under selected mode, with the existing unknown-selector forcing control retained; no leg assertion should be relaxed. A selected-mode `ACCEPT-O-64: PASS` must never substitute for the full frozen command.

### R8 — HIGH scoped dependency: the separately declared C control receipt is absent

Beyond the ten explicitly enumerated files, `claims.json:70` names `reports/round-64/telemetry/controls-c.txt`. An exact-path glob reports it missing. The wave-1 `CriticClaims.md` does contain the executed stub/copy and teaches-copy controls, but that does not make the declared telemetry path exist.

**Axes:** coverage, operability, calibration. **Smallest safe correction:** Main must preserve the real control outputs at a separately identified durable artifact and explicitly reconcile the declared pointer. Do not fabricate a passing control or silently count the missing path as present. This dependency is recorded here without waiting for another seat.

### R9 — LOW provenance/count limits: census files are validation snapshots only

Static body comparison is exactly True: removing the two leading comment lines from `census-wave1.txt` yields `census-start.txt` byte-for-byte, SHA-256 `e55bb7f95ec692a56823d1427a9172fd154941c5f02b17b9d5a4366846f4d4da`. That equality is **not evidence of copied execution**: unlike O's randomized IDs, these validation rows are deterministic, and ScribeCensus reports the registry was unchanged for that run.

The output shape agrees with `scripts/sources-census.sh:737-745`: warning lines followed by lane `ok`. Twenty-seven W04 + one W03 + one ok equals **29 stdout lines**, not the 30 claimed in `ScribeCensus.md:31,133`. The installed 31 total lines are exactly two headers plus 29 body lines; no missing body line is required by this arithmetic.

Neither receipt pins the registry/producer bytes, and these are `validate` outputs, not the numeric `census` mode's row/tier/status totals. At this audit's current registry snapshot S687 is already queued; the receipts' S687 W03 therefore describes a **historical pre-flip** registry, not current post-repair validation. There is no post-repair census among these ten files. This is a scope/provenance limitation, not proof the old validation was false.

**Axes:** calibration, coverage. **Smallest safe correction:** append the 29-line count erratum and label both as historical validation snapshots. For final before→after claims, Main should record a new separately named current validation/numeric-census receipt with command, exit, producer and registry digests; never overwrite the historical pair or infer row totals from W-codes.

## What checks clean, and what the telemetry still cannot prove

1. **No observed O counter-hash drift.** All four O receipts name `c27a9fefb37c4a107e83867fd03f9194d89ce4e0dc8364e9b1b23e7821987b18`, exactly the current counter at both initial and final snapshots. Ca remains `f222648ea45517d5e4f7cf27c888e686253fdc67741b23ab458e9ef82081d678`. Future counter edits require new hash-bound measurements; this report asserts no future state.
2. **Tool identity is consistent.** Current tool, declared-base blob, and `reports/round-63/telemetry/freeze-sha256.txt:4` all equal `c0f10a8450b425bb0959b00c18031fde43ac4809a5334538e9c1d4d9199568a0`.
3. **Mutant provenance is consistent.** All ten persisted `reports/round-64/mutants/*.py` hashes match `mut-o.txt:6-15`. Static AST extraction of the counter's literal MUTANTS table found each needle once and each persisted source exactly equal to the declared tool substitution. No mutant was executed by this critic.
4. **Cosmetic control identity is consistent.** Surviving scratch `control-root/tools/reopen-row.py` hashes to the recorded `f3789feee1488b9a64da05f93e8aeeac3afadbc173ef76ad6a7b3362e7e9bb61`; its AST excluding the module docstring equals the unchanged tool's AST. The control header's c0f10a84 baseline identity and the explicitly distinguished f3789fee control identity should not be conflated.
5. **The raw outputs are not merely one renamed final run.** Final, MUT-only, EDGE-only, and cosmetic-control bodies agree with their separate surviving captures, and their randomized IDs differ. Each of the three MUT PASS lines names all ten mutants: m1, m10, m2, m3, m9, m5, m6, m7, m8, mread. m8 explicitly records both GEN and BOUND failures. Distinct payloads alone do not prove experimental independence beyond these observed captures.
6. **Complete kill telemetry is not exclusivity evidence.** The receipts demonstrate the recorded pinned kills, not the stronger `claims.json:32` wording “each fail exactly their pinned leg.” The inner command selects only pins (`accept-o.py:1076-1091`). The strongest surviving counterexample is wave-1 `CriticO.md:128-153`: the exact broad m5 fails both EDGE_SCHEMEREL and EDGE_SLASHLESS. No receipt here refutes that counterexample. Smallest safe repair remains the authorized all-defined-non-MUT-leg audit plus a genuinely slashless-only m5 patch; do not add collateral pins or weaken an EDGE leg merely to bless the existing receipt. Impact: operability/calibration. Canonical judgment remains outside this critic.

## Receipt hash manifest

```text
ff9e65f3e0c19b3a2829340a6f48f0c7a6709e5e454ebd489d0384bf68efc072  dry-run-c.txt
e1f1aa14319d7c5cbe2013966a6b4bfe34250c9444aee5896cfe58dfbbd09832  dry-run-ca.txt
635a16b04356ef30522fbc00850f42c161d22d8b6c607173f845442f019877d8  dry-run-o.txt
635a16b04356ef30522fbc00850f42c161d22d8b6c607173f845442f019877d8  dry-run-o-baseline-copy.txt
009bbde3c7720a496b26f224646a5d99e6e55f247d22b9d9c38da93ccad84193  final-measures-o.txt
7c5df1d5d2256cce84a3152a9e299d46ea7191031ff3c03ad47e85153aca1842  mut-o.txt
134d00444559837144ecf3d89df5618afa2b15168d83c49384800e48e59b9536  edge-o.txt
49eae130179c1125965097d75e2c6eb1ab2c4c5931e69c9311cc1d0c2ce11652  control-o.txt
e55bb7f95ec692a56823d1427a9172fd154941c5f02b17b9d5a4366846f4d4da  census-start.txt
0075cd255e95423a4b83e8898c0a49ff0a46d63db0a06ff3e65b30bfbec86ee3  census-wave1.txt
```

## Method, limitations, and disposition

Read the frozen claims, all ten receipts, their counter output definitions, the named wave-1 attacks, and surviving ExecCounterO captures/sources. Used read-only git object inspection, coreutils SHA/count/byte comparison, and static Python data/AST analysis through the tool; no counter module was imported or executed. The local `diff -u -I` binary rejected `-I` (exit 2); exact header-excluding comparisons were subsequently performed as static byte analysis, yielding the equalities reported above. No install/update was necessary or performed; no pacman transaction was attempted.

These are fixable evidence/output-contract defects or explicitly bounded missing historical prerequisites, not evidence of a beneficial axis trade. Recovery of the unavailable original bb0c74a4 full run is not something a new run can supply. Preserve historical bytes, disclose that gap, and bind any new authorized measurements to their actual source identities. All proposed executions/counter repairs belong to Main and their assigned owners; none is represented as already exercised here.

## Addendum — post-review counter drift observed at 03:01:10Z

**R10 — HIGH: all four O receipts are now stale against the current counter.** This later observation supersedes the earlier snapshot's “no observed O counter-hash drift” statement for current-byte use; it does not invalidate the historical rev3 captures.

After an incoming finding from `kotodama-r64.RevVerifyO2`, a direct SHA-256 snapshot recorded:

```text
6d9c9354f0d7a9535aba4e781541b04626dd3a91791175a7d5f845c559615fa1  reports/round-64/accept-o.py
979050ce21fa01758c075745b08bf3ecf7d6e73baad543a1df83f666ecc5de2b  reports/round-64/accept-c.py
7319ff4b9c7eb2cd23f866eb4db62d469a539b8dd99b8326fb6bae8f1cb0d4c5  reports/round-64/accept-ca.py
```

The O docstring now names revision 4 (read snapshot `A0AB`). All four O receipt-file hashes remain exactly those in the manifest above; their recorded counter identity remains **c27a9fef…**, not **6d9c9354…**. `final-measures-o.txt:2` directly confirms the old rev3 digest. Thus final/MUT/EDGE/control receipts cannot establish current-revision behavior. C and Ca have also changed again since the initial snapshot; their old baseline bytes remain historical.

**R11 — MEDIUM: the persisted m5 source and kill receipt now identify the old mutation, not the current one.** Static extraction of the current counter's literal MUTANTS table, applying its exact substitution to the unchanged tool without executing the result, yields:

```text
current expected m5 sha256 795b8d196eec4b64344b39338bf73a3cc6a73c075671702d4b963959a6e6ecb6
saved m5 sha256            83ecd7341afe979f68a55a0b4bb13acbb642057a0f9852429ecba44eeeee9abe
pins                      ['EDGE_SLASHLESS']
```

Only m5 differs from the saved fixture set in this comparison. Its recorded old hash still agrees with the old saved file, but that internal agreement does not bind it to revision 4.

**Related forcing evidence, attributed rather than rerun:** RevVerifyO2 reports the current generated m5 has `IndentationError: unexpected indent (line 605)` and fails both selected legs with empty row results; the revision-4 isolation assertion therefore cannot pass. Its reported mutant digest is the same `795b8d19…` independently derived above. The peer also reports the revision-history sentence reverses the intended outcomes. Current source `accept-o.py:118-119` indeed says the former EDGE_SCHEMEREL should FAIL and latter EDGE_SLASHLESS PASS, opposite the peer's stated code requirement and proposed correction. This critic did not rerun compilation, either leg, or the full counter.

**Axes:** operability and calibration; coverage measurements are separately unbound to the subsequently changed C counter. **Smallest safe correction:** finish the authorized m5 indentation/prose repair without weakening either leg or enlarging pins; preserve all old receipts as rev3 history; freeze the corrected source identity and record separately identified full/selected/control captures plus corresponding mutant identities. Merely updating receipt headers or carrying forward the old green MUT line would create false provenance. No acceptance result for 6d9c9354 or its successor is claimed here.

### Durable corroboration and transient-C correction

The completed `.ufo/waves/round-64/w2/CounterDrift.md:49-84` independently corroborates R5/R10/R11 and the invalid current m5. Its final identity table (`:26-38`) matches this report's later counter digests.

**Correction to R4's static mechanism inference:** CounterDrift's executed probe (`:179-188`) establishes that C snapshot `073e9716…` did not have a prior `row` binding: the misplaced read raised `UnboundLocalError`, rather than reading a previous row as initially inferred here. That exact transient snapshot was fixed at 02:56:55Z by moving the lookup above the guard; final `979050ce…` completes all eleven legs in that peer's probe. The transient C crash must not be attributed to final C bytes. Ca's intervening NameError was likewise fixed before the later `7319ff4b…` snapshot (`CounterDrift.md:190-196`). These are attributed peer executions, not checks rerun by this critic.

Report: .ufo/waves/round-64/w2/CriticReceipts.md
