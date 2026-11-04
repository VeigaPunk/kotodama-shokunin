# ExecControls — round 87 ONE v1

Axes: finite CLI discrimination, transport fidelity, provenance, and honest non-vacuity limits. Author-side independent control receipt, not outside admission or an O judgment. No production integration or changes.

## Observed bounded executions

Used the unmodified counter from `2a3b5643899c3520867ae930593cafef6ef19cad`, baseline packet from `83846a22ee1e9da7aa52ac505ccebf4455169247`, and constant-pass control from `732c45394c73fcffd9fc623b939d446c7b11a9db`. Counter and constant-pass bytes are identical between prefreeze and frozen revisions (`frozen-comparison.json`). Every invocation used an existing exclusive scratch work directory, Python `-B`, and the public counter CLI. Full arguments, stdout, stderr, exit, per-case expectations and observed results are retained in each receipt.

| Execution | Observed | Counter exit |
|---|---|---|
| `--selftest` | clean transport 12/12; constant-pass 3/12; constant-reject 1/12; non-JSON 0/12; all four expected counts matched | 0 |
| no-work base | 0/12, `TOOL_ABSENT` | 1 |
| frozen constant-pass | 3/12: positive-six, unknown-explicit, reordered-records | 1 |
| additional always-red | 1/12: duplicate-record only | 1 |
| additional blanket-error | 1/12: invalid-json only | 1 |
| additional filename non-reader | 12/12, without opening any packet body | 0 |

Always-red emits one `RECORD_ID` finding and exit 1 for every input. Blanket-error emits `ATTESTATION_ERROR` and exit 2 for every input. The filename non-reader explicitly maps the public fixture stem to the expected exit/finding; it demonstrates a real finite-battery limit, not production implementation. Full rejection of these controls is **not** observed: each refusal control receives one incidental match, and the fixture-aware non-reader receives every match. Thus blanket refusal cannot satisfy the 12/12 predicate, but arbitrary non-reader rejection is false.

## Exact hashes (SHA-256)

- Counter: `131b29e84d39c2cbd22993aaadd469b5a96602651927730c980503cc74738e62`
- Frozen claims: `bfc2de174261ad410a63abb3949385d8be76fe29ef8aaa528ec8d0f9feb43264`
- Baseline packet: `4f631b60b5ea5d5cf42b2ef394d548ff557e4ccaa52f176d7327fead8f34c982`
- Constant-pass candidate: `78b66e106bb4a149849a09d92c02fc0b7dd43316fa66a680a22ec07eef01567d`
- Always-red candidate: `101a1ec1ed0b50c762a52fcf24c6c2b843d109d4d9bd0f59c0bf7b7d3c7f09ea`
- Filename non-reader candidate: `1daa4ffa04121a81b19407c401f548a9375768cafaf806cced4a99922d1ceca6`
- Blanket-error candidate: `0430f0951911b01d7f8c3098cd75fbf22e085e12f37d3bfc17754af9507770c5`

No-work candidate hash is inapplicable: the tool is absent. The production tool is also absent at the specified frozen revision (Git show exit 128 retained); no integrated production candidate was measured in this seat.

## Audit limits

The selftest proves only subprocess/exit/JSON comparison against a filename oracle generated from the same case list; it does not independently validate domain semantics or completeness. The counter checks expected finding membership, not exact findings, and positive cases require records=6 and empty findings. Invalid JSON requires exit 2 plus `ATTESTATION_ERROR` anywhere in stdout/stderr, not a particular structured error. Negative cases do not require accurate record counts, record ids, details, or absence of unrelated findings. The battery has three positive and nine negative cases; it neither certifies semantic truth nor proves arbitrary substitute-tool rejection. Public filenames permit explicit answer memorization, demonstrated above. These are disclosed bounds already compatible with frozen claims, not grounds here to rewrite the counter or claim broader integrity.

Existing r86 stage completeness checking is not new; O is framed only as the finite production CLI capability. Source ids and counter history were not edited. L1 canonical planning remains authoritative for this wave; the unresolved L2 planner-policy/lowest-axis conflict is disclosed, not resolved or waived here.

## Retained evidence and operations

All evidence is under `.ufo/waves/round-87/w1/stage/ExecControls/`: immutable `measure87.py`, `claims.json`, `packet.json`, `constant-pass.py`; three additional control sources; `assets.json`; `frozen-comparison.json`; `environment.json`; and six `*.receipt.json` files named selftest, no-work-base, constant-pass, always-red, filename-non-reader, blanket-error. No installs/updates, git mutations, production writes, background jobs, unrelated verification, or credential access. LSP is unavailable in this seat's mounted tool inventory; this source-only transport audit required no symbol refactor. Exclusive scratch was removed after retaining receipts.

Main owns post-integration production verification against the exact final candidate and frozen counter. This receipt must not be represented as an integrated-candidate 12/12 result.

Self-evaluation (author-side): accuracy 4/5 (no production-candidate observation); completeness 5/5 (all assigned controls executed and retained); clarity 4/5 (raw receipts carry detailed commands); actionability 5/5 (exact limits and next gate identified); conciseness 4/5 (hash inventory is deliberately explicit). Mean 4.4/5. Improvement: attach the main-owned integrated-candidate receipt before asserting O. User-agreement self-check: this reports transport evidence, not semantic admission.
