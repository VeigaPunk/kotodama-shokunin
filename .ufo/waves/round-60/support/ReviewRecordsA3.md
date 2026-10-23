HOLDS: all six round-59 spot-check §5 items are routed at the frozen commit, no filed round-59 row was rewritten, and no `__pycache__` remains in the lane.

Seat: KotodamaR60A3.ReviewRecordsA3 (falsify, leaf). Lane tip checked = `/ commit `47f27bd0cb0bea219f21cd731c2eb0fe71f7f626` (`git rev-parse HEAD` printed exactly this hash). All reads read-only; no tools installed; no sandbox or clones needed; no process trees left running (every command capped with `timeout`).

## Command 1 — HEAD hash and log (full output)
```
$ timeout 30 git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin rev-parse HEAD && timeout 30 git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin log --oneline -5
47f27bd0cb0bea219f21cd731c2eb0fe71f7f626
47f27bd round-60: FREEZE (claim D, before any data seat) — freeze_note; packet-key hash (key built from the 1cd9db7c entry, kept outside the lane until the support wave settles); revision-9 residual re-score receipts (NONE-MET); records: SCORECARD and LOG round-59 corrections, round-59 errata, QUALITY criterion 14, round-60 lesson (pre-data parts)
a56b04f round-60: revision 9 (attempt 3, before any data seat) — CONFINED denies backslash-escaped slashes (RescoreConfineA3); L1 re-score of MutEvidenceA3 fixtures under revision 8 (seat refused, hold); support prompt asks for a novel page passage; residual reports
09be1e1 round-60: revision 8 (attempt 3, before any data seat) — EVIDENCE needs 5 words absent from the packet, a span no other pinned page carries, nested-quote parsing (MutEvidenceA3); residual control receipts so far; wave-1 connector and packets-dry reports
1cd9db7 round-60: claim D build (pre-freeze, before any data seat) — amulets entry restores the four round-59 propositions in source-scoped wording (S648-S651, superseding S602/S616/S623/S643 on the same pages) and narrows 19 base lines per the attempt-3 pre-freeze audits (w1-a3/AuditA3R01-R16, ScoutPlacementA3); SOURCES S648-S651; pinned captures S648-S651 (re-fetched byte-identical)
b9faed9 round-60: revisions 6-7 (attempt 3, before any data seat) — exact 24-seat roster and dissent scan over every frozen seat (CtlNarrowA3); CONFINED false voids fixed (dry runs); EVIDENCE: SUPPORTED counts only with >=10 words of the pinned page text not in the packet (CtlKeyedLabelA3); 47 pinned page texts; wave-1 pre-data control receipts and build audits (scored at 14e64138)
```

## Command 2 — `__pycache__` scan (full output)
```
$ timeout 60 /usr/bin/find /home/vgpnk/Projects/shokunin/kotodama-shokunin -name __pycache__
(no output — empty)
```
Reinforcement:
```
$ timeout 30 /usr/bin/find /home/vgpnk/Projects/shokunin/kotodama-shokunin -name '*.pyc' | wc -l
0
```
Item 4's removal receipts exist: `reports/round-60/telemetry/pycache-removed.txt` and `pycache-removed-a3.txt` (glob found both).

## Command 3 — no-rewrite check (full output)
```
$ timeout 120 git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin diff 9c82a6eb main -- SCORECARD.md LOG.md corpus/lessons/round-59.md

diff --git a/LOG.md b/LOG.md
index 3112b60..6e60beb 100644
--- a/LOG.md
+++ b/LOG.md
@@ -4118,3 +4118,9 @@ actual route stay recorded per round. Prior rounds stand as filed.
 - Evidence: control wave 8 seats (1 refused, CtlKeyedLabels59, hold), build wave 35 seats, support call 8 seats; receipts under `reports/round-59/telemetry/`; lesson `corpus/lessons/round-59.md`.
 - Re-verification: the round-58 kongo fixes were re-read on their sources by ReviewDKongoA59/B59/C59 (14/14 agree).
 - Routed round-58 defects: stray files deleted; census at start; FETCH-59 + QUALITY criterion 13; C lands name every SUPPORT input.
+
+## 2026-10-23 — Round 59 correction (recorded in round 60; records, not a claim)
+
+- ACCEPT-C-59 is recorded as **MISSED** on the as-reviewed 47-row object: 14 legs PASS and SUPPORT FAIL (S602, S616, S623, S643 one NOT-SUPPORTED each, `reports/round-59/telemetry/as-reviewed-c.txt`, 03:39:56Z). The four propositions were deleted at 03:40:08Z, 12 s after that receipt; the narrowed 43-row entry is not the judged object. Run 2 at `84b931a5` also printed FAIL (legs lost to `tail -3`). Source: `corpus/lessons/round-59-verifier-spotcheck.md` §2 and §5 items 1-2.
+- The round-59 separability line `C->REC via acceptance` is a live-fetch re-run artifact, not a dependency: no `accept-c.py` leg reads a REC land, and C passed alone at `4abfb63d` (spot-check §5 item 3).
+- Filed round-59 SCORECARD and LOG lines are unchanged; this entry and the SCORECARD correction table are appended. The amulets entry is re-entered under a new pre-data freeze as round-60 claim D.
diff --git a/SCORECARD.md b/SCORECARD.md
index 583a3eb..3ef0d64 100644
--- a/SCORECARD.md
+++ b/SCORECARD.md
@@ -1136,3 +1136,10 @@ Instruments `39c9ce8a` (revision 0), declaration `1b80ee41`, revision 1 and free
 Correction rows for round 58 (filed rows not edited): the round-58 instrument was revised six times before data, not five (`31cf8b6` added TOPIC); its "123 fixtures, 0 pass" holds only as a whole-predicate count — 18 failed only SUPPORT, 17 of them for a missing registry (`corpus/lessons/round-59.md` Errata).
 
 Frontier step (not a claim): `corpus/SOURCES.md` 525 → 573 rows (S600-S647 opened this round; 43 mined, 1 queued, 4 rejected); census exit 0 at start (`reports/round-59/telemetry/census-start.txt`) and end.
+
+Correction rows for round 59 (recorded in round 60; routed defects 1-3 of `corpus/lessons/round-59-verifier-spotcheck.md`; filed round-59 rows not edited):
+
+| corrected row | correction | evidence |
+|---|---|---|
+| round-59 coverage (`ACCEPT-C-59`, author-side PASS) | **MISSED** on the as-reviewed 47-row object: 14 legs PASS, SUPPORT FAIL on S602, S616, S623, S643; the four propositions were deleted 12 s after the FAIL receipt; run 2 at `84b931a5` printed FAIL (legs lost to `tail -3`). The narrowed object is not the judged object. | `reports/round-59/telemetry/as-reviewed-c.txt`; `reports/round-59/telemetry/final-measures.txt` run 2; spot-check §2 |
+| round-59 separability `C->REC via acceptance` | a live-fetch re-run artifact, not a dependency (no REC land read by `accept-c.py`; C passed alone at `4abfb63d`) | spot-check §2 and §5 item 3 |
diff --git a/corpus/lessons/round-59.md b/corpus/lessons/round-59.md
index fb9d791..b500c47 100644
--- a/corpus/lessons/round-59.md
+++ b/corpus/lessons/round-59.md
@@ -128,3 +128,10 @@ Eight reviewer seats (SupportA59-H59, one task call) judged 118 packet blocks: 9
 - Spares verified by seats and not registered: Catholic Encyclopedia "Amulet" (ScoutTerminologyMuseum), Kent SATOR post (ScoutWordAmulets), British Museum Islamic Gallery hand amulet (ScoutHamsaHand), Wessex Archaeology Bath Abbey marks (ScoutWitchMarks), V&A rock-crystal talisman (ScoutIslamicTalismans), Yale Peabody Echoes of Egypt (ScoutMagicalGems).
 - Uncovered by any row: senninbari belts, peach wood and door gods, West African hunters' shirts, nazar glassmaking; every on-topic host refused a plain GET.
 - Kongo fix 140 spans pp. 470-471 (ReviewDKongoA59/C59); fix 84a's watercolor date conflicts with the article's own "around 1750" (ReviewDKongoA59).
+
+## Errata added in round 60 (filed bytes not rewritten)
+
+- **R59-M5** (round-59 verifier spot-check §5 item 4): the earlier `reports/round-59/__pycache__/` cleanup did not persist; `reopen-quote.cpython-314.pyc` and `rowcheck.cpython-314.pyc` were regenerated at 03:19:46Z and were still present at closure. Round 60 removed the ignored caches at 2026-10-23T04:57:02Z (`reports/round-60/telemetry/pycache-removed.txt`) and a later attempt-2 regeneration at 07:04:21Z (`reports/round-60/telemetry/pycache-removed-a3.txt`). The "removed by the L1" wording of R59-M5 applies only to the earlier cache files.
+- **CtlKeyedLabels59** (spot-check §5 item 5): held after a provider `cyber_policy` refusal; never scored and never rerouted. It is dropped from round 59's shortcut list as unscored, with that reason. Round 60 scored a differently designed packet-only keyed control (`CtlKeyedLabelA3`, which met revision 6 under the probe and forced revision 7) and a lane-reader control (`CtlLaneReaderA3`); neither backfills a round-59 result.
+- **Support registry label** (spot-check §5 item 6): `.ufo/waves/round-59/support/registry.json` labels its source "support task call (~03:40Z)", later than the reviewer report mtimes (03:37:31Z) and the as-reviewed FAIL receipt (03:39:56Z). `~03:40Z` is an erroneous chronology label, not a task-call time; the record supports only the source attribution (the `KotodamaR59` task call, agent ids as returned).
+- **Final-measures run 2** (spot-check §5 item 2): run 2 at `84b931a5` printed `ACCEPT-C-59: FAIL`, exit 1; it is a FAIL instance at the landed revision, and its failing leg is unknown because `tail -3` cut the per-leg lines. Round 60 captures every counter run in full and its counter has no network leg (FETCH-60).
```
Summary:
```
$ timeout 30 git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin diff --stat 9c82a6eb main -- SCORECARD.md LOG.md corpus/lessons/round-59.md
 LOG.md                     | 6 ++++++
 SCORECARD.md               | 7 +++++++
 corpus/lessons/round-59.md | 7 +++++++
 3 files changed, 20 insertions(+)
```
Only additions: 20 insertions, 0 deletions, 0 modified lines. PASS.

## Routing of spot-check §5 items 1-6 (each read at the frozen commit)
1. **Post-verdict narrowing of C** — routed: SCORECARD.md:1144 (correction row 1: ACCEPT-C-59 MISSED on as-reviewed 47-row object); LOG.md:4124; round-60.md:9 (route table row 1); QUALITY.md criterion 14 (grep line 45: narrow-object FAIL grounded in §5 item 1); claims.json:47.
2. **Lost run-2 legs; non-deterministic predicate** — routed: round-59.md:137 (erratum "Final-measures run 2": FAIL at `84b931a5`, no tail capture, FETCH-60 no network leg); LOG.md:4124 (run 2 FAIL); round-60.md:10; claims.json:48 and fetch_rule FETCH-60 (claims.json:21: "no ACCEPT-D-60 leg fetches over the network… treatment is frozen here and never relaxed").
3. **Separability false positive** — routed: SCORECARD.md:1145 (correction row 2); LOG.md:4125; round-60.md:11 (ExecSeparabilityA3 `unshare -rn` runs byte-identical, 0 `connect`); claims.json:49.
4. **R59-M5 contradicted** — routed: round-59.md:134 (erratum R59-M5); round-60.md:12; claims.json:50; caches removed (04:57:02Z and 07:04:21Z receipts exist); current scan empty (Command 2).
5. **CtlKeyedLabels59 never scored** — routed: round-59.md:135 (erratum: dropped from round 59's shortcut list with reason, not rerouted); round-60.md:13 (CtlKeyedLabelA3 + CtlLaneReaderA3 scored instead); claims.json:51.
6. **Support registry label ~03:40Z** — routed: round-59.md:136 (erratum "Support registry label": erroneous chronology label corrected in a new record); round-60.md:14; claims.json:52.

No item is missing. The claims.json "records" block (lines 47-52) independently lists all six items as routed, matching the five checked files.

## Attempts to falsify (none succeeded)
- No-rewrite check: diff is pure additions (Command 3).
- Pycache check: `find -name __pycache__` and `find -name '*.pyc'` both empty (Command 2).
- Routing check: every item has at least the prescribed record type (SCORECARD row / LOG entry / erratum / lesson route / QUALITY criterion), with line-level references above.
- HEAD equals the frozen declaration hash `47f27bd…`; all records inspected are the committed bytes at that revision.

## Residual risk / verification gaps
- The routing is verified as present at the frozen commit; I did not re-execute the acceptance counters or the separability `unshare -rn` runs (read-only seat), so the *content* of the recorded evidence (e.g. `as-reviewed-c.txt`, `pycache-removed-a3.txt`) is cited but not re-derived. The telemetry receipts for pycache removal exist on disk.
- No tools installed; no processes left running; no sandbox writes made. Report written with a single `write` call at `.ufo/waves/round-60/support/ReviewRecordsA3.md`.
