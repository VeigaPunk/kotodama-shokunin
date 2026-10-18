# Round-21 recount dispositions (C19-C22, filed by the integrator from the disposition seats' analysis)

Date: 2026-10-18. Every mismatch in reports/round-21/recount/ledger.json named:

1. **R17 fragment/count discrepancy — environmental snapshot mismatch; mechanism unproven.**
   Filed R17: 16 scanned inputs, 7 fixed, 5 attempted (D failed, so no pass was recorded).
   Recount clone: 0 fragments. Source and clone each hold the same 16 files with identical
   hashes at inspection → incomplete clone snapshot at recount time. Why: unproven
   (.scratch-scanner sensitivity suspected). The zero is NOT an accepted R17 pass.
2. **D2 pin difference — legitimate documented re-pin.** Projector 0da0015f→76536a92;
   D2 expected-holds pin a5dc26d5→7b9439c4 per reports/round-20/repin/O14-repin-table.md;
   D2 gate output byte-identical; round-20 frozen replay 11/11. Not a retroactive invalidation.
3. **R18 frozen replay omission — environmental, resolved.** Fresh clone omitted the
   gitignored round-11 run.log; copying the hash-matched log into the disposable clone
   reproduced 11/11. R17's round-11 replay shows the same symptom.
4. **R19 baseline count increase (17→18) — legitimate change.** Round 20 added
   r20-post/expected.json (commit 35b6797).
5. **R20 audit-verdict discrepancy — environmental selection drift.** Filed receipt
   selected audit-v3.md; the clone selected packet-v3-16.md; both rank at build 16 and the
   runner breaks ties by newest mtime (non-hermetic). Different artifacts judged, not
   contradictory judgments.
6. **R20 links 102 vs 105 — defect-class discrepancy, dispositioned by the contract audit.**
   The filed 102 was the build-16 archive number; the current v3 pair is 105/105 green.
   The mtime tie-break selected the archive in some runs — recorded as the candidate-
   selection drift defect routed to round 22.
7. **R20 corpus declaration — defect in the declared figure.** Live counts reproduce
   94/19/19/18/29/20 (199 total); the claim declared linguistics 20 where live is 19;
   README documents the delta. Filed-figure defect, not a live-count defect.
8. **Unresolved-open:** the R17 clone-snapshot mechanism (item 1) and the interop.md 92/92
   historical anomaly (superseded revision; not re-adjudicated) stay open with owners in
   reports/round-21/defects/routed.md.
