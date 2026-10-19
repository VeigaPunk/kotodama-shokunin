- Seat: O07 | scribe | claim O | date 2026-10-19 | baseline 57c8409

# O07 — operability landed-changes material

This is receipt-ready history for claim O, not a new verification or disposition of the round-37 queue. The round-33/34/35 outcomes below are the outcomes recorded in their filed receipts and SCORECARD/LOG; I did not execute a round runner or claim an acceptance verdict.

## Landed-change summary

- **Round 33 — lessons index and falsifier audit.** The recorded operability move is the lessons index reconciliation: 33 lesson files / 33 index rows, 78 queue rows, zero findings, with the revision-3 README matching the verified reconstruction. The F-X16-3 false-positive audit was also re-keyed from the nonexistent `closing-snapshot.json` name to the content-keyed `closes` + `closes_sha256` convention; LOG records zero live matches and 7/7 fixture scenarios. These are separate changes: the README reconciliation does not itself close the falsifier instrument defect. Evidence: `SCORECARD.md:588-600`; `LOG.md:3526-3533`; the disposition/control material in `reports/round-33/op/O05-falsifier-disposition.md:73-93,132-147`.

- **Round 34 — receipt-guard adoption inventory and routing.** The filed round records a new `tools/harness/receipt_guard_adoption.py` instrument and inventory at 29 runners (18 guarded-refresh / 11 unguarded-in-place), plus routing for the unguarded class and a correction that r26 is guarded, not part of the unguarded hazard class. This is a historical, close-time count, not a current count: round 36 records 30 runners / 19 guarded / 11 unguarded, so the r34 inventory is superseded by population growth and should not be presented as a live census. Evidence: `SCORECARD.md:616`; `LOG.md:3604-3608,3633-3638`; `reports/round-36/cross/X02-conformance.md:383-409`.

- **Round 35 — R34-N1 diagnostic hardening.** The filed round records the superseded r6 replay changing from an unhandled `KeyError` to exit 1 `E2E-READSET` naming `reports/round-20/handoff/claims-map.md`, with no traceback; the r7 default chain stayed green at packet `45f57132…`, and the v3 selftest had 44 controls. The current renderer contains the baseline-member roster check and emits the named diagnostic on the v3 path. Evidence: `SCORECARD.md:641`; `reports/round-35/validation.json:75-89`; `tools/exercise-handoff-e2e.py:3823-3842,4684-4685`.

## Boundaries and still-carried risk

- **Do not mark F-C13-1 prevention fixed from the r34 routing or r36 restoration.** Round 36's LOG records an in-tree runner execution followed by restoration (`LOG.md:3695-3698`), but the r36 conformance audit later captured repeated r34/r35 receipt writes and an r35 receipt still divergent at that audit's close (`reports/round-36/cross/X02-conformance.md:37-63,126-176`). Ca05 independently records the r34/r35 absolute-root behavior and the failed plain-clone isolation assumption (`reports/round-36/calib/Ca05-receipt.md:28-45,145-174`). The cause is that both filed runners set an absolute live `ROOT` and `chdir` there, so a plain copied checkout does not contain their publish path (`reports/round-34/run-validation.py:10-11,26,532-535`; `reports/round-35/run-validation.py:9-10,36,502-505`). The repair must be a safe containment mechanism or successor runner; do not edit the filed runners. Round 37's O08/O12 fragments identify this as a distinct carried candidate, not just another row in the original 11 unguarded runners (`reports/round-37/op/O08-gap-fill.md:5-19`; `reports/round-37/op/O12-gap-fill.md:5-17`). Per-write actor attribution remains `to-verify` (`reports/round-36/cross/X02-conformance.md:227-234`).

- **R34-N1 is narrower than full read-set equality.** The current r35 code rejects a baseline member absent from the live read set, but its success comparison iterates baseline inputs and reports `len(V3_READ_SET)` (`tools/exercise-handoff-e2e.py:3823-3842`). S02 documented the reverse-direction case: a live member omitted from a re-signed baseline can pass while the success count overstates how many entries were compared (`reports/round-35/scribe/S02-o-receipt.md:303-312`). Keep that separate from the verified R34-N1 fix; its round-37 queue disposition still needs the census and owner evidence.

- **Round 36 did not claim operability.** Its declared claims are D/C/Ca, with D rejected and C/Ca verified; its in-tree runner incident is evidence relevant to the carried F-C13-1 defect, not an O-axis improvement (`reports/round-36/claims.json:15-33,139-143`; `reports/round-36/validation.json:139-145,157-168`; `SCORECARD.md:651-666`).

## Owed

- `reports/round-37/scout/K02-defect-census.md` and `reports/round-37/op/O01-queue-draft.md` — reconcile this history against the full defect census and the drafted queue before claiming coverage or a final disposition. At inspection, O05/O06 reported both absent (`reports/round-37/op/O05-verify.md:5-12`; `reports/round-37/op/O06-verify.md:3-11`).
- `reports/round-37/op/O02-fix-verify.md` — required non-author evidence before any queue row can be called fixed; absent at O06's inspection (`reports/round-37/op/O06-verify.md:3-11`).
- `reports/round-37/op/O03-carry-verify.md` and `reports/round-37/op/O09-routing.md` — carried-owner sanity and round-38+ routing remain to be folded; these outputs were not present in the inspected O-block file set. Targeted missions: `reports/round-37/targets.json:38-45`.
- Integrator: preserve the r34/r35 hardcoded-root issue as a distinct carried item unless O01 proves it is already represented with equivalent mechanism, owner, reason and next touch; do not label receipt restoration as a fix.

## Citations

- `SCORECARD.md:588-600,616,620-626,641,651-666` — round 33-36 recorded outcomes and named findings.
- `LOG.md:3526-3533,3604-3608,3633-3638,3662-3667,3695-3698` — landed changes, errata, and F-C13-1 incident records.
- `reports/round-33/op/O05-falsifier-disposition.md:73-93,132-147` — falsifier repoint and control observations.
- `reports/round-35/validation.json:75-89` — filed O-leg replay, packet digest and v3 control count.
- `tools/exercise-handoff-e2e.py:3823-3842,4684-4685` — current v3 read-set check and named diagnostic output.
- `reports/round-35/scribe/S02-o-receipt.md:303-312` — reverse-direction membership-count limitation.
- `reports/round-36/calib/Ca05-receipt.md:28-45,145-174`; `reports/round-36/cross/X02-conformance.md:37-63,126-176,187-234,383-409` — isolation mechanism, recurrent receipt writes, sampling/time limits, and inventory growth.
- `reports/round-37/op/O08-gap-fill.md:5-19`; `reports/round-37/op/O12-gap-fill.md:5-17` — round-37 carried-item evidence and proposed routing.
- `reports/round-37/claims.json:19-24`; `reports/round-37/targets.json:36-45` — claim O acceptance requirements and O-block missions.
