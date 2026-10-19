- Seat: O07 | executor | O | date 2026-10-19 | baseline 456674d

# O07 — operability receipt draft

**Status: could-not-evaluate at this seat's snapshot; claim O is not certified.** The delivered round-40 runner is a useful reference for several required contract points, but the round-41 template, checker, census, verifications, and queue update were not present when checked. The claimed after-state and its thresholds therefore remain unverified; later arrivals require a fresh integration check. No in-tree round runner was executed.

## Claim and denominator issue

Claim O requires the durable runner template and conformance checker, a green checker selftest, a runner census with defect classes, and queue-v2 updates for N7 and `r39-runner-root-regression` (`reports/round-41/claims.json:13-18`). The denominator is internally inconsistent:

- The claim body says **7 runners, r34–r40** (`reports/round-41/claims.json:14`).
- Its threshold says `reports/round-3[3-9]/run-validation.py` plus round 40, which selects **r33–r40 (8 paths)**. K01's census assignment also names r33–r40 while calling it a 7-runner census (`reports/round-41/targets.json:13-17`).
- The read-only file-existence check found all eight runner paths present (command output below). Do not silently choose a denominator; resolve whether the intended census is r34–r40 or r33–r40 before certifying 100% coverage.

## Baseline evidence

Round 40 demonstrates the intended reference shape in its runner: relative `ROOT` (`reports/round-40/run-validation.py:5`), receipt guard loading (`:227-231`), and the guard call preceding the receipt write (`:242-245`). A search of that file for `os.chdir`/`chdir(` returned no matches. Its filed receipt records acceptance true and a non-null runner hash, plus round-specific findings and limits (`reports/round-40/validation.json:2-3,129-145`). This supports r40 as a reference, not verification of a reusable template or checker.

For contrast, r39 still has an absolute `ROOT` and `os.chdir(ROOT)` (`reports/round-39/run-validation.py:5,13`). The r40 queue records N7 and the r39 root-regression item as carried rows, with r40 named as the intended cure (`reports/round-40/op/defect-queue-v2.json:102-109,312-376`). The round-41 claim requires new evidence and fixed-with-evidence updates; the r40 queue itself does not establish that those updates landed.

## Snapshot and result

The required sibling drafts and both deliverable files were checked with a read-only existence test; each returned `MISSING_OR_EMPTY`: O01 template draft, O02 checker draft, O03 predicted census, O04/O05 verifications, O06 queue update, O09 r40 verification, `templates/round-runner-template.py`, and `tools/harness/round_runner_conformance.py` (command and output below). Consequently neither `--selftest` nor `--json` could be run here. This is a snapshot of this receipt's check, not a statement about later arrivals.

## Owed

- Integrator/claim owner: reconcile the seven-versus-eight runner denominator before grading census coverage (`reports/round-41/claims.json:14,18`; `reports/round-41/targets.json:13-17`).
- O01/O02: land the template and checker drafts; O03: provide predicted census; O04/O05: independent checks; O06: queue update; O09: verify r40 against the delivered checker (`reports/round-41/targets.json:41-73,76-101`). These outputs were absent at this seat's snapshot.
- Integrator: after those arrive, rerun the checker’s declared `--selftest` and `--json` commands on the delivered files, reconcile actual census against the settled denominator, and only then assess O's required threshold (`reports/round-41/claims.json:16-18`). No round validation runner was executed.

## Citations

- Assignment and write boundary: `reports/round-41/targets.json:4-9,83-87`; sibling missions: `:41-73,76-101`.
- Claim O and its denominator/commands/threshold: `reports/round-41/claims.json:13-18`.
- R40 reference runner: `reports/round-40/run-validation.py:5,227-231,242-245`; `Grep` query `os\.chdir|chdir\(` in that file → no matches.
- R40 filed evidence: `reports/round-40/validation.json:2-3,129-145`.
- Prior runner-root example and unresolved queue rows: `reports/round-39/run-validation.py:5,13`; `reports/round-40/op/defect-queue-v2.json:102-109,312-376`.
- Runner inventory command (`cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1 && for n in 33 34 35 36 37 38 39 40; do p="reports/round-$n/run-validation.py"; if test -f "$p"; then printf 'PRESENT %s\n' "$p"; else printf 'MISSING %s\n' "$p"; fi; done`) → all eight paths `PRESENT`.
- Sibling/deliverable check (`cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1 && for p in reports/round-41/op/O01-template.md reports/round-41/op/O02-checker.md reports/round-41/op/O03-predicted.md reports/round-41/op/O04-verify.md reports/round-41/op/O05-traps.md reports/round-41/op/O06-queue-update.md reports/round-41/op/O09-r40-verify.md templates/round-runner-template.py tools/harness/round_runner_conformance.py; do if test -s "$p"; then printf 'PRESENT %s\n' "$p"; else printf 'MISSING_OR_EMPTY %s\n' "$p"; fi; done`) → all nine paths `MISSING_OR_EMPTY` at this receipt's snapshot.

