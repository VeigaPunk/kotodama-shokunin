# Round-18 conformance defect sweep — R21-O03..O04

- **Audit date:** 2026-10-18.
- **Scope:** round-18 lane-local final-report artifacts, claims/receipt baseline binding, and the round-18 admission records in `LOG.md` and `SHONEN.md`.
- **Mode:** read-only. No round validator or historical validator was run; no round-8..20 artifact was modified. The search was restricted to this repository; an external fleet-root report was not inspected.
- **Round state:** `reports/round-18/validation.json` records acceptance true and no failures; `LOG.md` and `SHONEN.md` record O/D/C admitted.

## Findings

### O03 — No lane-local final round report is present (open / external filing unverified)

The round-18 directory inventory (`ls reports/round-18`, audit date 2026-10-18) contains claims, validation, scope, gate, D4, civ-map and repin artifacts, but no `report-draft.md` or `kotodama.md`. The direct path check `test -e reports/round-18/kotodama.md` was false, and the in-repository `.ufo/reports/**/*.md` search returned no matches (2026-10-18). The parent-level records do contain the admitted outcome (`LOG.md:3242-3256`; `SHONEN.md:171-190`), but they do not supply the missing lane-local final report artifact. Whether the integrator filed an external report is outside this repository audit and remains unverified.

Disposition: retain the admitted status; request a pointer to the authorized final report or record its absence in the next permitted integration artifact. Do not create or revise historical round-18 files here.

### O04 — Admission record mislabels the round declaration as its baseline (medium)

The declared baseline is `3dd3754207032cb81f5fb3e202fe85cf79211339` in both `reports/round-18/claims.json:5` and `reports/round-18/validation.json:3`. `LOG.md:3244-3245` and `SHONEN.md:173-178` instead label `c66ac3c` as the baseline. `git show -s --format='%H %s' c66ac3c 3dd3754` (audit date 2026-10-18) identifies `c66ac3c` as the **round-18 claims declaration** and `3dd3754` as the **round-17 close**. Reproduce by comparing the filed claim/receipt fields with the closure text and resolving both revisions via `git show -s` (2026-10-18).

This is a closure-record binding error, not a failure of the green receipt. Preserve the historical LOG/SHONEN text; route a dated correction through a new authorized integration record.

## Preservation and verification boundary

Read-only preservation check on 2026-10-18: `git merge-base --is-ancestor 3dd3754207032cb81f5fb3e202fe85cf79211339 HEAD` exited 0; `git diff --name-only 3dd3754207032cb81f5fb3e202fe85cf79211339 HEAD -- reports/round-8 reports/round-9 reports/round-10 reports/round-11 reports/round-12 reports/round-13 reports/round-14 reports/round-15 reports/round-16 reports/round-17` returned no paths. This confirms current committed bytes for the protected interval only; no historical validator was run.

FILES: reports/round-21/defects/sweep-r18.md
SUMMARY: R18's filed receipt remains green; its lane-local final report is not present in this checkout, and the admission records misstate the baseline.
