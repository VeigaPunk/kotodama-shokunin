# MutationTesterV3 — round-92 w1 (operability, mutation attack)

Full report: .ufo/waves/round-92/w1/stage/MutationTesterV3/mutation-report.md

- Tool sha256 (working tree and freeze 066b9728 extract): 905be2fed386c491d52224832ea75ed8c7b02e67c1b021b2c66511658c1c1422 (identical).
- Frozen mutation pass (`reports/round-92/mutants.py`, committed bytes): MUTATION-SCORE 60/60 killed, 0 survived, 0 broken-pattern, rc 0.
- Receipt: committed reports/round-92/mutation-score.txt sha256 6b2a1b8aa622449239b40b273f7b8b80f4e6db40517caa3ba492b102e06c5d41 is byte-identical to the re-run receipt. Header: `# clean selftest rc=0 ['SELFTEST PASS 89/89']`, tool sha matches. No committed mutation-score.json exists (mutants.py writes one; predicate names only the .txt).
- Stub control (`--tool reports/round-92/controls/stub-tool.py`): 0/60 killed, 60 broken-pattern, rc 1. Stub prints `SELFTEST PASS 89/89` but only 34 `  ok ` lines, so OKCOUNT refuses it.
- Gap hunt (10 mutated scratch copies, selftest as oracle): 1 KILLED (gap-readme-graded-off), 9 SURVIVED. Survivors (rc 0, 89 ok lines):
  1. gap-manifest-graded-off: `args.base_registry, 'corpus/README.md', args.manifest]:` -> `args.base_registry, 'corpus/README.md']:`
  2. gap-entry-graded-off: `[args.lesson, args.lands_registry, args.entry,` -> `[args.lesson, args.lands_registry,`
  3. gap-lands-graded-off: `[args.lesson, args.lands_registry, args.entry,` -> `[args.lesson, args.entry,`
  4. gap-lesson-graded-off: `[args.lesson, args.lands_registry, args.entry,` -> `[args.lands_registry, args.entry,`
  5. gap-traversal-off: `if rel.startswith('/') or '..' in rel.split('/'):` -> `if rel.startswith('/'):` (capture_error)
  6. gap-fetch-offset-optional: `(?:Z|[+-]\d{2}:\d{2})$')` -> `(?:Z|[+-]\d{2}:\d{2})?$')` (FETCH_RE)
  7. gap-fetch-date-off: `if fm.group(1) != as_of:` -> `if False:`
  8. gap-cap-slash-capture-error-off: `rel.startswith(cap_dir.rstrip('/') + '/')):` -> `rel.startswith(cap_dir.rstrip('/'))):` (capture_error block)
  9. gap-port-strip-off: `if (scheme == 'http' and host.endswith(':80')) or (scheme == 'https' and host.endswith(':443')):` -> `if False:` (norm_url)
- The three hardenings named in the assignment: norm_url fragment strip and surface_error year check are already killed in the frozen 60 (shadow-norm-off, archive-year-off); the corpus/README.md graded-list extension is killed by gap-readme-graded-off.
- Scope of survivors: selftest-level only. They are not in the frozen 60 nor the 21 O.refusal_cases, so the O kill rule is not failed by them. End-to-end acceptance of each in entry mode was not built or measured.
- Lane writes: this trailer and the stage dir only. No git mutation; no tools installed.
