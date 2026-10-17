# Round-8 conformance sweep — R12-O01/O02

- **Axis:** O / operability — report and protocol conformance.
- **Audit date:** 2026-10-17.
- **Scope:** Read-only review of the filed `.ufo/reports/round-8/kotodama.md`, round-8 lane evidence, `SHONEN.md`, and `LOG.md`. No round-8 through round-11 artifact was changed.

## Results

- **Report / SHONEN — pass.** The filed report has a `## SHONEN` heading and records only author-side `[~]` assertions; it claims no independent promotion review. The canonical `SHONEN.md` still has all boxes `[ ]`. No `marker-report` reference was found in the round-8 lane reports or the filed report. The report-to-marker distinction is intact; no `[x]` was added to the canonical checklist.
- **Cited work commit — pass.** The report cites `e1694bad6ac96aca45a11ca5746582b275929355`. `git cat-file -t` returned `commit`, and `git merge-base --is-ancestor e1694bad6ac96aca45a11ca5746582b275929355 HEAD` exited `0`; audited HEAD was `69d0c2191628c1396a85aea2fd7408f2d1bba08e`. The baseline citation `cf338a7` also resolves to a commit and is an ancestor of HEAD.
- **LOG — pass.** The round-8 admitted entry is present in `LOG.md` in both the cited work commit and current HEAD; its round-8 summary matches the report's closeout claim.

## Finding — filed validation receipt rewritten after round 8

The report and LOG say the round-8 acceptance command passed. This was true at the round-8 work commit: `reports/round-8/validation.json` there has `acceptance_checks_passed: true` and an empty failure list. At current HEAD the same filed path has `acceptance_checks_passed: false`, with later-tree O and D failures. This is **not** evidence that round 8 failed at close; it is evidence that its filed receipt was rewritten after close and now no longer preserves its original snapshot.

**Cause / corroboration:** the only post-close commit changing this path is the round-11 commit `a3f6fcef2d92a1099581140c81d4264e9a4e2aa3` (`git log ... e1694...HEAD -- reports/round-8/validation.json`, run 2026-10-17). Round-11 `adjacency.md` identifies the live receipt rewrite and the validator's write-to-`OUTPUT_REL` behavior; `reports/round-11/recheck/row-131.json` explicitly records that `python3 reports/round-8/run-validation.py` rewrites this filed JSON in place. Do not restore or regenerate the round-8 artifact in this sweep: preserve the observed drift as a finding and route it through the round-12 defect router for round 14.

## Evidence commands and date

All commands below were run on 2026-10-17; timestamps are local (`-03:00`).

- `git cat-file -t e1694bad6ac96aca45a11ca5746582b275929355`; `git merge-base --is-ancestor e1694bad6ac96aca45a11ca5746582b275929355 HEAD`; `git rev-parse HEAD` — run at 19:38:15; commit exists and is ancestral to the reported HEAD.
- Python `json.loads(git show <revision>:reports/round-8/validation.json)` comparison for `<revision>` = the cited round-8 work commit and `HEAD` — run at 19:38:48; original `true` / no failures versus current `false` / later O and D failures.
- `git log --format='%H %ad %s' --date=iso-strict e1694bad6ac96aca45a11ca5746582b275929355..HEAD -- reports/round-8/validation.json`; `git diff --quiet e1694bad6ac96aca45a11ca5746582b275929355 HEAD -- reports/round-8/validation.json` — run at 19:43:00; the round-11 commit is the only post-close change, and the receipt differs.
- Report, `SHONEN.md`, and `LOG.md` content checks — run at 19:43:00; heading and closeout LOG entry present, no `[x]` in the report, canonical checklist remains unchecked.
- Search for `marker[- ]report` in `reports/round-8/**` and the filed report — 2026-10-17; no matches.

**Disposition:** one open historical-receipt conformance defect; no repair attempted because the filed artifact is immutable under this assignment. Structural report checks pass; the receipt-integrity finding remains open for the round-12 router.
