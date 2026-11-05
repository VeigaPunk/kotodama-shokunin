# MutationTesterV3 — round-92 mutation pass (w1, attack seat)

Scope: re-run the frozen 60-pair mutation pass over committed bytes; hunt gaps by
mutating scratch copies of the frozen tool. Lane writes: this stage dir and the
Report trailer only. Scratch: /fast/scratch/hyaku/kotodama-r92/MutationTesterV3/
(deleted before yield). Tools installed: none (python3 stdlib only). Date of all
measurements: 2026-11-05.

## 1. Tool bytes and freeze pin

| command | result |
|---|---|
| `sha256sum tools/check-advance-evidence.py` (working tree) | `905be2fed386c491d52224832ea75ed8c7b02e67c1b021b2c66511658c1c1422` |
| `git show 066b9728fc64e78735769c4740d05c1000d31a3b:tools/check-advance-evidence.py > $S/frozen-check-advance-evidence.py; sha256sum` | `905be2fed386c491d52224832ea75ed8c7b02e67c1b021b2c66511658c1c1422` (identical) |

## 2. Frozen mutation pass (committed bytes)

Command (rc 0):
`TMPDIR=$S python3 -B reports/round-92/mutants.py --root <lane> --work $S/mut --out $S/mutation-score`

Result: `MUTATION-SCORE: 60/60 killed, 0 survived, 0 broken-pattern` (60 `KILLED` rows, rc=0).

Receipt header check:
- Committed `reports/round-92/mutation-score.txt`, sha256 `6b2a1b8aa622449239b40b273f7b8b80f4e6db40517caa3ba492b102e06c5d41`.
- Re-run `$S/mutation-score.txt`, sha256 `6b2a1b8aa622449239b40b273f7b8b80f4e6db40517caa3ba492b102e06c5d41`.
- `diff` of the two files: no output (IDENTICAL).
- Header line 1: `# tool sha256 905be2fed386c491d52224832ea75ed8c7b02e67c1b021b2c66511658c1c1422` (equals the run's own tool sha, and the freeze pin).
- Header line 2: `# clean selftest rc=0 ['SELFTEST PASS 89/89']` (the clean run's own rc, the routed D4 fix).
- Observation: mutants.py also writes `<out>.json`; the lane has no committed `reports/round-92/mutation-score.json`. The O predicate names only the `.txt`, so this is not a kill-rule failure, but the .json is not carried.

## 3. Stub control

Command (rc 1, expected):
`python3 -B reports/round-92/mutants.py --root <lane> --tool reports/round-92/controls/stub-tool.py --work $S/mut-stub --out $S/stub-score`

Result: `MUTATION-SCORE: 0/60 killed, 0 survived, 60 broken-pattern`. Stub tool sha256 `a37c05539d018e63c6aad875e2a9e1159799587e4c89f0cc07fd1ac70e73b53a`. Its clean selftest prints `SELFTEST PASS 89/89` with rc 0, but `python3 -B stub-tool.py --selftest` emits 34 lines beginning `  ok ` (`grep -c '^  ok '`, command run 2026-11-05), not 89. OKCOUNT therefore refuses the stub. The frozen tool's clean selftest emits 89 (`clean_ok_lines` in gap-results.json).

## 4. Gap hunt (mutated scratch copies, selftest is the oracle)

Driver: `stage/MutationTesterV3/gap_hunt.py` (copied here). Each row is one hardening removal applied to a copy of the frozen tool; verdict KILLED iff the mutated tool's `--selftest` exits non-zero.

| # | name | old -> new (exact, on one line) | verdict | rc | ok lines |
|---|---|---|---|---|---|
| 1 | gap-readme-graded-off | `args.base_registry, 'corpus/README.md', args.manifest]:` -> `args.base_registry, args.manifest]:` | KILLED | 1 | 88 |
| 2 | gap-manifest-graded-off | `args.base_registry, 'corpus/README.md', args.manifest]:` -> `args.base_registry, 'corpus/README.md']:` | SURVIVED | 0 | 89 |
| 3 | gap-entry-graded-off | `[args.lesson, args.lands_registry, args.entry,` -> `[args.lesson, args.lands_registry,` | SURVIVED | 0 | 89 |
| 4 | gap-lands-graded-off | `[args.lesson, args.lands_registry, args.entry,` -> `[args.lesson, args.entry,` | SURVIVED | 0 | 89 |
| 5 | gap-lesson-graded-off | `[args.lesson, args.lands_registry, args.entry,` -> `[args.lands_registry, args.entry,` | SURVIVED | 0 | 89 |
| 6 | gap-traversal-off | `if rel.startswith('/') or '..' in rel.split('/'):` (capture_error) -> `if rel.startswith('/'):` | SURVIVED | 0 | 89 |
| 7 | gap-fetch-offset-optional | `(?:Z\|[+-]\d{2}:\d{2})$')` -> `(?:Z\|[+-]\d{2}:\d{2})?$')` (FETCH_RE) | SURVIVED | 0 | 89 |
| 8 | gap-fetch-date-off | `if fm.group(1) != as_of:` -> `if False:` | SURVIVED | 0 | 89 |
| 9 | gap-cap-slash-capture-error-off | `rel.startswith(cap_dir.rstrip('/') + '/')):` + `return f'capture outside` (capture_error block) -> `rel.startswith(cap_dir.rstrip('/'))):` | SURVIVED | 0 | 89 |
| 10 | gap-port-strip-off | `if (scheme == 'http' and host.endswith(':80')) or (scheme == 'https' and host.endswith(':443')):` -> `if False:` (norm_url) | SURVIVED | 0 | 89 |

Notes on the gap driver: the first form of row 9 (`rel.startswith(cap_dir.rstrip('/') + '/')` alone) was BROKEN-PATTERN (the text occurs twice, in capture_text and capture_error); it was re-run with the capture_error block as context (row 9). Mutated-copy sha256s are in gap-results.json.

The three hardenings named in the assignment:
- norm_url fragment strip (`u = str(u).strip().split('#', 1)[0]` -> no strip): already in the frozen 60 as `shadow-norm-off`, KILLED.
- surface_error year check (`if int(stamp[:4]) < int(as_of[:4]):` -> `if False:`): already in the frozen 60 as `archive-year-off`, KILLED.
- corpus/README.md graded-list extension: row 1 above, KILLED (selftest case "capture byte-copies corpus README" catches it).

## 5. Survivor gaps (selftest-level)

Nine single-line hardening removals leave all 89 selftest checks green (rc 0, 89 ok lines). The selftest has no fixture for these classes. Each is a gap in the O grader's own test set, reported with exact pair above. They are not among the 60 frozen mutants and not among the 21 O.refusal_cases, so the frozen O predicate and kill rule are not failed by them.

- S1 manifest byte-copy (row 2): a capture equal to the manifest bytes under another path is not refused.
- S2 entry byte-copy (row 3): a capture equal to the entry bytes is not refused.
- S3 lands-registry byte-copy (row 4): a capture equal to the lands registry is not refused.
- S4 lesson byte-copy (row 5): a capture equal to the round lesson is not refused. (The lesson is refused when it is also in --graded; the untested case is the un-graded path.)
- S5 capture path traversal (row 6): `reports/<cap_dir>/../../...` is accepted by the confinement check when the traversed file is not in graded_shas. Mitigation present in the tool: graded_shas catches traversal to a graded file only.
- S6 fetched_at without UTC/offset (row 7): a naked local time `2026-11-05T19:00:00` passes FETCH_RE.
- S7 fetched_at date mismatch (row 8): a fetched_at date different from as_of is not refused by any fixture.
- S8 capture-dir sibling prefix (row 9): `reports/round-90/evidence-evil/...` passes the `startswith(cap_dir)` check without the trailing slash.
- S9 default-port shadow (row 10): `https://host:443/x` vs `https://host/x` is not normalised, so a port-suffixed shadow of a base url is not caught.

Not demonstrated: that each survivor is accepted end-to-end in entry mode. This pass measured selftest-level survival only; building a full entry-mode fixture per survivor was not done.

## 6. Commands and rc (all run 2026-11-05)

- `sha256sum` (tool, freeze extract, stub, receipts): rc 0.
- `git show 066b9728…:tools/check-advance-evidence.py > $S/frozen-…py`: rc 0 (read-only).
- `mutants.py --root <lane> --work $S/mut --out $S/mutation-score`: rc 0, 60/60 killed.
- `mutants.py --tool stub-tool.py --work $S/mut-stub --out $S/stub-score`: rc 1, 0/60 killed, 60 broken-pattern.
- `stub-tool.py --selftest`: rc 0, 34 `  ok ` lines.
- `gap/gap_hunt.py`: rc 0; 1 KILLED, 8 SURVIVED (+1 BROKEN-PATTERN re-run as row 9, SURVIVED).
- Frozen selftest on the frozen bytes via the gap driver: rc 0, 89 ok lines.

No git mutating command was run; the only git call was read-only `git show`.

## 7. Files

- stage/MutationTesterV3/mutation-report.md (this file)
- stage/MutationTesterV3/gap_hunt.py (gap driver)
- stage/MutationTesterV3/gap-results.json (verdicts, mutated sha256s, clean run)
- stage/MutationTesterV3/mutation-score.txt (re-run receipt, identical to the committed one)
- stage/MutationTesterV3/stub-score.txt (stub control receipt)
