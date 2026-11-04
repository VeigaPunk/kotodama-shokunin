# ExecIndexAuditor — round 85 wave 1

Axes: depth and operability; calibration is evidenced by subprocess controls and a pinned base audit. Scope: stage-only implementation, no README/registry/production edits.

## Deliverable

Stage root: `.ufo/waves/round-85/w1/stage/ExecIndexAuditor/`.

- `check-corpus-index.py`: stdlib successor for landing at `tools/check-corpus-index.py`.
- `selftest.txt`: exact successful selftest output, command, tool SHA256 and exit.
- `base-audit.json`: complete structured base audit, including stable finding IDs, per-partition counts, supplemental ownership, authoritative footer and README digest.
- `base-audit.txt`: pinned revision/tree, materialization method, tool SHA256, commands, verbatim JSON/text outputs and exits.

Tool SHA256: `8d57afd0801e9ea78b6f95ab48b80cc3bc08c2eff02a83a9496ff7dd51317b71`.

CLI: `--root PATH [--json]` or `--selftest --work PATH`. Audit text emits one `CORPUS-INDEX:` summary. JSON emits one parseable document whose `summary` contains that same verdict. Findings exit 1; clean exits 0; missing/unreadable inputs and invalid invocation exit 2 with `CORPUS_INDEX_ERROR` on stderr and no traceback. Work must already exist; selftest creates/removes only its own temporary child.

Extracted parser provenance is in the module docstring: historical `reports/round-28/readme/sweep.py` at base `0d181583b18ae94e80a251ca5ab5f3055b16c74c`, SHA256 `7e0566ad1ae8ec2c5a0f10c62dc8de66abcc180ec3f7af560bceeba1601cad2b`. The historical instrument is unchanged. No runtime dependency on its location exists, so nonce fixtures need only a corpus.

Important calibration correction: the actual base historical script already uses `matches[-1]` for footer selection and totals, and already resolves supplemental rows to a unique disk partition. The frozen claim's first-footer characterization is stale; there was an existing index checker. This successor retains those existing capabilities, adds explicit-root operation and duplicate failure, and makes a malformed last dated block fail rather than skipping backward to an older parseable footer.

Six directories and six README partition sections are required. Duplicate sections/unknown partition-shaped sections fail too. Supplemental rows preserve unique-partition ownership, including the two round-73 rows; ambiguity/no owner fails. Duplicate detection covers effective rows after supplemental attribution. Missing rows, ghost rows, topics, headers, totals, authoritative footer total and six-component footer vector are independent finding classes. No real corpus counts or filenames are hardcoded in the implementation.

## Exercised checks

Explicitly assigned selftest: `SELFTEST: PASS (23 checks)`, exit 0. Every control invokes the actual CLI subprocess. Controls assert exit plus exact finding-class sets and stable ID prefixes; the text-mode clean control also requires exactly one summary line. Controls cover stale-first/correct-final green, missing, duplicate, ghost, topic rewrite/absence, header, totals, footer total, vector/value/arity, absent/malformed final footer, missing section/directory, supplemental unique/duplicate/absent/ambiguous ownership, continuation topic, and input errors.

Initial development selftest exposed a helper parameter named `kind` colliding with finding-detail `kind`; renamed the helper parameter to `category`. The retained successful receipt is after that fix.

Pinned base audit materialized only committed `corpus` bytes using read-only `git -C <lane> archive 0d181583b18ae94e80a251ca5ab5f3055b16c74c -- corpus` into exclusive scratch. It returned exit 1 in JSON and text modes:

```
CORPUS-INDEX: FINDINGS files=258 rows=253 findings=10 ids=FOOTER_DIR_TOTALS,FOOTER_TOTAL,HEADER_DRIFT,MISSING_ROW,TOTALS_DRIFT
```

Disk vector: `32/36/42/29/24/95`; final recorded footer/total: 253, vector `32/32/41/29/24/95`. Findings:

- `FOOTER_DIR_TOTALS:footer`
- `FOOTER_TOTAL:footer`
- `HEADER_DRIFT:culture-material`
- `HEADER_DRIFT:myth-symbol`
- `MISSING_ROW:culture-material/maritime-seafaring-lexicon.md`
- `MISSING_ROW:myth-symbol/guest-right-hospitality-law.md`
- `MISSING_ROW:myth-symbol/marriage-alliance-bridewealth.md`
- `MISSING_ROW:myth-symbol/ordeal-judicial-proof-rituals.md`
- `MISSING_ROW:myth-symbol/witchcraft-sorcery-accusation-institution.md`
- `TOTALS_DRIFT:totals`

Scratch `/fast/scratch/hyaku/kotodama-r85/ExecIndexAuditor` removed after receipts were retained. No installs/updates; no mutations of git/jj; no fixture commits; no source/network research was needed for this tool-only assignment. LSP unavailable in mounted tools; no symbol definition/reference/refactor service was offered.

## Integration boundary and risks

L1 must land the tool, integrate the separately owned README repair and gate registry row, then run frozen claim O acceptance at integrated bytes. I did not run the frozen end-to-end acceptance or any build/lint/formatter. No production README was repaired. The historical TOPIC_RE and immediate-directory Markdown census semantics are deliberately retained; this auditor does not certify prose, source authenticity or nested corpus layout. Footer dates are lexical dates, not a chronology sort: last physical dated block is authoritative.

Suggested parent gate: `python3 -B tools/check-corpus-index.py --selftest --work <existing-work>`; `python3 -B tools/check-corpus-index.py --root <integrated-root> --json`; frozen `reports/round-85/measure85.py` claim O with required revision/freeze/work arguments.

## Self-evaluation

Accuracy 4/5: pinned audit and 23 controls retained, but integrated acceptance remains parent-owned. Completeness 4/5: scoped deliverable complete; README and registry intentionally outside this seat. Clarity 4/5: stable IDs/one summary/JSON, though JSON carries the summary as a field rather than a separate line. Actionability 4/5: direct landing file and receipts supplied; parent integration still required. Conciseness 4/5: implementation includes 23 controls rather than the minimum 12. Overall 4.0. Highest-impact next action is the parent's integrated frozen O gate; preserve existing supplemental rows. User agreement: expected for this stage-only contract, not a claim of complete lane acceptance.
