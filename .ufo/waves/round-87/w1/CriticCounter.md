# CriticCounter — r87-v1, author-side bounded review

Axes: operability (the single claimed O axis); evidential identity and finite discrimination are review lenses, not additional acquisition claims. No admission or universal certification is made.

## Inputs and preservation

Reviewed exact claims and measure87.py at `2a3b5643899c3520867ae930593cafef6ef19cad`, controls at `732c45394c73fcffd9fc623b939d446c7b11a9db`, and baseline packet/tool lookup at `83846a22ee1e9da7aa52ac505ccebf4455169247`. Counter SHA-256: `131b29e84d39c2cbd22993aaadd469b5a96602651927730c980503cc74738e62`. All five examined prefreeze artifacts are byte-identical to their frozen counterparts. No frozen instrument/claim, production, Git/index, or sibling files changed.

All evidence below is in `.ufo/waves/round-87/w1/stage/CriticCounter/`: original counter/claims, control and forgery sources, full stdout/stderr/return-code receipts, hashes, receipt audit, and summary. No external sources or installations; existing Python 3.14.8. Scratch was dedicated to this seat; receipts retain the original execution paths.

## Executed controls and counterexamples

| Candidate/probe | Result | Evidence |
|---|---|---|
| Prefreeze constant-pass non-reader | 3/12, rc1 | `constant-pass.receipt.json` |
| Non-JSON constant output | 0/12, rc1 | `non-json.receipt.json` |
| Always-red RECORD_ID | 1/12, rc1 | `always-red.receipt.json` |
| Wrong positive population, records=5 | 0/12, rc1 | `wrong-positive-population.receipt.json` |
| Filename-only oracle, never opens packet body | **12/12, rc0** | `filename-spoof.receipt.json`, matching `.py` |
| Filename positive split, all eight labels on every negative, records=-999 and nonexistent record IDs on negatives; non-JSON error substring on malformed case | **12/12, rc0** | `all-labels-wrong-record.receipt.json`, matching `.py` |
| JSON findings=null | rc1 traceback; no aggregate measurement receipt | `null-findings.receipt.json` |
| Frozen counter transport selftest | rc0; expected/observed 12,3,1,0 | `transport-selftest.receipt.json` |
| Actual base, no candidate override | 0/12 TOOL_ABSENT, rc1 | `base83846.receipt.json` |
| Frozen claim revision, no candidate override | 0/12 TOOL_ABSENT, rc1 | `baseline.receipt.json` |

The final row is not a failed production candidate: the freeze commit is the measurement/claims snapshot and does not contain the proposed production tool. Production must be evaluated at its actual later committed revision. Forgery receipts deliberately use `--candidate`; their revision field remains the freeze revision, not provenance for the forged bytes.

## Strongest survived forgery and smallest safe correction

**Counterexample:** a non-reader can return a lookup table keyed solely by the basename of `--packet`. Fixed case filenames disclose the complete expectation. Source anchors in the preserved counter: lines 20–36 define the table; 42 writes case names into filenames; 82–85 explicitly use this technique for the transport oracle. The independent filename spoof achieved 12/12.

**Impacted axis:** operability evidence supports only this finite battery, not packet-sensitive semantic correctness or rejection of arbitrary substitutes. This is an expressly excluded finite limit in claims.bounds, not by itself a contradiction of the exact frozen O predicate. No authority to adjudicate admission here.

**Smallest safe correction now:** retain the frozen instrument unchanged; attach the forgery receipts and prohibit interpreting 12/12 or MEASURE87_SELFTEST as an anti-forgery/domain-truth certificate. Require L1's receipt for the actual committed production bytes without `--candidate`, tied to candidate SHA and revision. If stronger discrimination is desired later, separately freeze a new instrument using independently named inputs and independent behavioral expectations; random names alone do not defeat content memorization.

**Second counterexample:** negative cases accept presence of one expected ID, not exact findings, record identity, record count, detail, or absence of unrelated labels (lines 50–55). The all-labels forgery passed with invented record IDs and records=-999. The invalid-JSON case passed with stderr `NOT_ATTESTATION_ERROR_SUFFIX` and non-JSON stdout: line 53 only searches a substring. This does not show production emits wrong labels; it shows the battery cannot establish full CLI output-shape or precise error localization. Stronger future checking would enforce the documented output schema, intended affected records, permitted findings, and a structured exact error label. Do not silently expand this round's frozen acceptance criterion.

## Fail-closed defect and timeout limits

`findings:null` triggers TypeError at line 50 rather than a failed-case row, because only JSON decoding ValueError and subprocess TimeoutExpired are handled. This forgery does not obtain credit; it removes the normal receipt. Safe current handling is to treat any counter crash or missing complete receipt as failure, never 0/12 success or omitted evidence. A future instrument can validate findings as a list before iteration and persist the malformed-output case as failed.

A per-case timeout is **present**: 15 seconds at line 45, with a failed timeout row at 59–60. No hanging candidate was executed. Inspection, not measurement: Git blob retrieval at 16–18 lacks timeout; captured output is not size-limited; subprocess handling does not establish process-group/descendant termination or a whole-run deadline. Thus bounded simple CLI cases are supported, hostile-resource universal operability is not. Probe invocations additionally had outer deadlines (90 seconds; baseline lookups 30 seconds). No broad timeout absence is alleged.

## Claims / labels / positive-control requirement

The literal predicate is exactly 12/12 through the public packet CLI. Three accepted positives require records=6 and findings=[]; eight structural negatives require expected rc1 plus an ID; malformed JSON requires rc2 plus substring. The three-positive population is genuine and prevents both all-red and constant-pass from satisfying O. The frozen broad case_contract mentions empty IDs, all clocks, and several blank record fields; the battery samples duplicate IDs, origin deletion, and blank sense only. Do not describe these samples as exhaustive coverage of all listed variants.

Prefreeze persisted receipts parse completely: `constant-pass.json` contains MEASURE87 3/12; `counter-selftest.json` contains MEASURE87_SELFTEST with four expected/observed transport counts; `no-work.json` actually records **TOOL_ABSENT**, not a missing-work-directory experiment. Its name must not be used as evidence of work-directory validation. Source inspection shows the work-directory check, but that branch was not executed here.

A positive transport oracle is necessary to show the counter can award 12/12, but insufficient for production capability: its deliberate filename lookup never reads packet semantics. The production `tools/check-attestation-packet.py --selftest --work EXISTING_DIR` claimed in claims.cli is a distinct actual-CLI domain test and was **not** run by this seat. Require the actual production positive clean six-record packet to yield rc0, records=6, findings=[], plus the full 12-row counter receipt at the committed production hash. Never substitute the transport selftest receipt for that evidence. No first-completeness-checking claim: the existing r86 stage checker is expressly acknowledged.

## Concrete kill conditions for L1/canonical evaluation

- Any production named case misses its expected exit or required finding ID, or a positive lacks exact records=6/findings=[]: O's stated kill rule applies.
- Any run crashes, times out, lacks complete case evidence, or uses different counter bytes: it cannot establish the exact frozen 12/12 claim.
- A candidate-override forgery, transport selftest, or unrelated revision/hash is presented as the committed production run: identity/provenance fails.
- Full output-schema correctness, all-field coverage, arbitrary substitute rejection, semantic attestation truth, or universal resource safety is claimed from this battery: the evidence does not establish that broader claim.

Remaining L2 planner-policy conflict and lowest-axis calibration debt are disclosed in the frozen claims; this review neither resolves nor waives them. L1 alone integrates; canonical Rust judgment alone decides admission. No production candidate was reviewed or certified by this seat.

Report: .ufo/waves/round-87/w1/CriticCounter.md
