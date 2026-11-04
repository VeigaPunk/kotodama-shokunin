# ExecAuditor — round 87 / w1

## Deliverable and axes

Candidate: `.ufo/waves/round-87/w1/stage/ExecAuditor/check-attestation-packet.py`

SHA-256: `4abcbbd058c33b95cc7c8acc4840493ccaeda0bdf01cb3947d074c3352c497aa`.

Axes: frozen CLI/case-contract fidelity, structural validation correctness, deterministic findings/exit codes, actual-subprocess selftest rigor, assigned-path compliance. Sole claimed axis is O operability, finite discrimination only. L1 owns integration and admission. Canonical L1 planning and unresolved L2 planner-policy/lowest-axis conflict remain disclosed, not resolved by this implementation.

## Design

- Stdlib-only local JSON reader. Reject duplicate keys at every nesting level and non-JSON constants. Top-level object/records-array/member-object shape failures, unreadable text, invalid JSON and CLI errors return exit 2 with structured `ATTESTATION_ERROR`; no uncaught ordinary malformed-type exception.
- Findings always contain string `id`, `record`, `detail`; JSON keys are sorted and findings follow input record order and fixed field order. Exit 0 clean, exit 1 findings. No six-record or historical-ID special cases.
- Reject empty/non-string/duplicate record IDs. Require nonblank sense, wording, genre, composition_status. Each of attestation/origin/collection/design requires a clock object, explicit value (null or canonical YYYY-MM-DD), nonblank reason even for unknown dates, and nonblank scope. Additional stable label `CLOCK_SCOPE` identifies missing/blank scope.
- Frozen relationships: unresolved solutions may not select an answer (`SOLUTION_CONFLICT`); record wording may not equal a different conjectured rather than transmitted wording (`EDITORIAL_CONFLICT`); known target attestation may not predate translation_date (`TRANSLATION_CLOCK`). Present malformed relationship objects get `RECORD_FIELD`; malformed translation dates get `CLOCK_DATE`.
- Does not infer historical origins from wording or date coincidence. Null dates remain allowed with explicit reason/scope. Does not rewrite or promote NON-CANON metadata. The inherited six-record packet and pre-existing `check-craft.py` were read: this is not the first completeness checker, nor a replacement for its stricter exercise-specific schema.
- `--selftest --work EXISTING_DIR` creates and cleans an isolated temporary directory under work and invokes this file's actual `--packet PATH --json` CLI for every fixture. First check is clean green. Thirty-seven checks include 1/3/7-record positives, known leap date, null dates, all frozen relationships and counterexamples, malformed types, duplicate keys at two levels, missing clocks/values/reasons/scopes, canonical dates and non-JSON constants. Each asserts exact exit, stable finding-ID sequence, records count and finding shape, and retains raw stdout/stderr in its receipt.

## Exact retained evidence

All paths below are under `.ufo/waves/round-87/w1/stage/ExecAuditor/`:

- `frozen-claims.json`, `frozen-measure87.py`: exact bytes fetched using `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show 2a3b5643899c3520867ae930593cafef6ef19cad:reports/round-87/{claims.json,measure87.py}`. Frozen originals unchanged.
- `selftest-run.json`: exact executed argv, exit 0, candidate hash.
- `selftest.stdout.json`: 37/37 passing checks, each with expected exit/IDs and actual exit/stdout/stderr; `selftest.stderr.txt` is empty.
- `battery-run.json`: exact executed frozen-driver argv with explicit `--candidate` stage path, immutable revision and scratch work directory; exit 0.
- `battery.stdout.json`: frozen battery 12/12, raw per-case outputs, candidate/counter/baseline-packet hashes; `battery.stderr.txt` is empty.
- `evidence-manifest.json`: retained artifact hashes and cleanup state.

Only the two expressly assigned executable checks ran: candidate selftest and immutable frozen battery against this candidate. No unrelated build/lint/formatter, no production edit, no Git/jj mutation, no source/counter-history rewrite. Parent must perform post-integration committed-path gate; candidate evidence is not that gate.

## Limits, risks and blockers

Trusted local JSON only; no adversarial resource-exhaustion or semantic-proof claim. No network/source registry additions, cultural authenticity, quotation support, arbitrary substitute-tool rejection, lore canon, or numeric expertise score claimed. A syntactically valid origin copied from attestation with a misleading explanation is outside the frozen structural contract and can remain clean. Editorial comparisons are exact text equality; no paraphrase detection. Record IDs are exact strings (nonblank checked with whitespace stripping, identity itself not normalized). No hardcoded count/case IDs; record populations can vary.

No installation/update performed. Python uses the existing system executable. No LSP tool is exposed in this seat's tool inventory; symbol definitions were read directly rather than claiming an empty LSP response. Independent review/mutation/domain-trial owners were given final candidate path/hash; their results are not asserted here. No implementation blocker.

## Self-evaluation

Accuracy 4/5: exact frozen 12/12 and selftest 37/37, but finite tests are not universal proof. Completeness 4/5: requested candidate, subprocess checks and receipts delivered; committed production integration deliberately belongs to L1. Clarity 4/5: stable IDs and explicit limits, though malformed shape errors are packet-level rather than record findings. Actionability 5/5: standalone candidate, exact argv/hash and raw evidence ready for L1. Conciseness 4/5: embedded selftest dominates source length but keeps delivery dependency-free. Mean 4.2/5. Highest-impact remaining action is L1's committed-path integration gate; no semantic expansion recommended under this contract.
