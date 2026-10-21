# ExecRunner: round-50 measurement runner

Assignment: `reports/round-50/run-validation.py`, a before/after measurement runner for claims C (coverage), O (operability) and Ca (calibration). Before = `--base-tree` (base 4ad26836552462d28a946ca3b067cab0b5ce3532), after = `--tree`. JSON on stdout.

## Artifacts

- Private clone: `.ufo/waves/round-50/work/ExecRunner` (checked out at 4ad2683).
- New file: `reports/round-50/run-validation.py`, mode 100755, 474 added lines (`git diff --stat`).
- Patch: `.ufo/waves/round-50/patches/ExecRunner.patch` (`git diff --output`, single new file via intent-to-add in the clone only).
- Lane untouched: no lane git command beyond `git clone` and `git ls-tree` (both read-only), no lane file edited.

## Usage and output

```
python3 -B reports/round-50/run-validation.py --tree DIR --base-tree DIR [--probe PATH] [--manifest PATH]
```

- Output: `schema`, `date`, `python`, `argv`, `tree`, `base_tree`, `probe`, `claims.{C,O,Ca}` (each: `axis`, `before`, `after`, `delta`, `acceptance.{before,after}`, `passed`), `acceptance_passed`.
- Each measure returns `absent` (missing inputs, values null), `values` (flat, judged), `detail` (command rc/status/output tail). A raising measure records `error`; a failed or timed-out command keeps `status`.
- Exit 0 when every check passes, 1 when one fails, 2 on bad arguments.

## What is measured

- **C:** `knowledge_entries` (find `-name '*.md'` semantics), `culture_material_entries`; entry `lines`/`h1`/`h3`/`topic`, eight-field head order (HEAD_FIELDS logic from `reports/round-49/run-validation.py:51-52,104-112`); README sweep `rc`, `rows`, `files`, `topic_mismatch`, `totals_ok`, `footer_ok` (parsed from `reports/round-28/readme/sweep.py:222-231` render lines); every cited S-id checked against a SOURCES row with `opened == 2026-10-21` and a used-by cell naming the entry; before-check counts (pastoral/husband/herd filenames, `^- topic:` lines matching pastoral/herd/husbandr/transhuman/livestock).
- **O:** `<runner dir>/jj-colocation-probe.py --tools-root <tree>` on both trees (`false_negatives`); `receipt_guard.py --selftest` and `check-readme-revisions.py --selftest` rc; before-check greps `refs/remotes/origin` (receipt_guard) and `base object unreachable` (check-readme-revisions).
- **Ca:** `tools/check-claim-separability.py` on `reports/round-50/separability/r49-fixture.json` (rc, `SEPARABILITY_DEPENDENCY` pairs, C->S detection), on the r50 manifest (rc), its `--selftest` rc; `corpus/QUALITY.md` separab line count (`grep -ci` equivalent) and `round-49-verifier-spotcheck` citation count; `tools/*separab*` file count before.

## Expectations (hard-coded `EXPECT`, from `reports/round-50/claims.json`)

- C before: knowledge 225, culture-material 27, entry absent, pastoral/husband/herd filename owners 0, pastoral topic lines 0. C after: knowledge 226, culture-material 28, entry present, H1 1, H3 0, topic 1, head ordered, sweep rc 0 / rows 226 / files 226 / topic_mismatch 0, cited sources >= 1 and none unresolved.
- O before: probe false negatives 3, `refs/remotes/origin` lines 0, skip marker lines >= 1. O after: probe false negatives 0, both selftests rc 0.
- Ca before: `tools/*separab*` files 0, QUALITY separab lines 0. Ca after: checker present, r49 rc 1 with C->S, r50 rc 0, checker selftest rc 0, QUALITY separab >= 1, spot-check citations >= 1.

## Judgement calls to verify at integration

1. **Probe output format is unknown to me.** The O probe is not in base and I did not read its landed bytes. The parser accepts JSON `false_negatives` (int), or text `false negatives: N`, or `N/M false negatives`. Anything else yields `probe_false_negatives: null`, which fails acceptance closed; the `tail` shows the output. Align the two regexes (`FALSE_NEG_RES`) with the landed probe.
2. **Probe location.** The runner always uses its sibling `jj-colocation-probe.py` with `--tools-root <tree>`, so base and landed tool bytes go through one instrument. Base has no probe file, so this is the only way to measure "3/3 on base".
3. **Checker CLI assumed:** `python3 -B tools/check-claim-separability.py <manifest>` and `--selftest`; findings parsed from `SEPARABILITY_DEPENDENCY X->Y via` on stdout or stderr. The checker reads claim bytes from git objects, so `--tree` and `--base-tree` should be git checkouts (clone or jj-colocated). An extract fails the checker leg visibly, with its rc recorded.
4. **r50 manifest path is a guess.** `reports/round-50/separability/r50-manifest.json` is not named in claims.json (its Ca lands list has only the fixture). Override with `--manifest`. The expectation rc 0 is inferred from claims.json's "run on reports/round-50/claims.json exits 0".
5. **Sweep.** `sweep.py` derives its tree from its own location (`HERE`), so running `<tree>/reports/round-28/readme/sweep.py` measures that tree.
6. **Extras beyond the bullet list**, each taken from claims.json text: head-field order, cited S-id check, before-check counts, O's two selftests (named in O's after_required), QUALITY spot-check citation (named in Ca's after_required). Drop them from `EXPECT`/`measure_*` if unwanted.
7. **Environment.** `PYTHONDONTWRITEBYTECODE=1` is set. `TMPDIR` is not overridden: round-49 pins it to `ROOT/.scratch`, but trees may lie outside the lane, so the runner does not write anywhere by default.

## Base-tree facts observed (read-only `git ls-tree 4ad2683`)

- Present: `corpus/QUALITY.md`, `reports/round-28/readme/sweep.py`, `tools/check-readme-revisions.py` (100755), `tools/harness/receipt_guard.py`, `reports/round-49/run-validation.py` (100755; mode mirrored).
- Absent at base: `tools/check-claim-separability.py`, any `reports/round-50/` path. The runner reports these as `absent` in the base measure, as intended.

## Unrun checks (not run: editing-wave no-verify rule; not instructed)

- `python3 -m py_compile reports/round-50/run-validation.py` (syntax).
- After integration: `python3 -B reports/round-50/run-validation.py --tree <landed checkout> --base-tree <base checkout at 4ad2683>`. Expect `acceptance_passed: true`, exit 0. Check `claims.O.after.detail.probe.tail` against the parser (judgement call 1).

## Tooling

No install or update. Python stdlib only. pacman untouched (paused per wave brief).

## Risks and blockers

- Risk: judgement calls 1, 3 and 4 are assumptions about sibling deliverables not yet landed. Any mismatch shows as a failed check with its evidence in the JSON, not a silent pass.
- Blockers: none for the runner. It depends on the O probe and Ca checker landing with the CLIs above; without them the runner reports `absent` and fails acceptance.
