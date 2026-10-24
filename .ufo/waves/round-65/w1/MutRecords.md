# MutRecords — mutation probe of the R1–R7 / CRITERION / QUOTES fixes (round 65, claim Ca)

seat: MutRecords (mutation tester) · date 2026-10-24 · lane `kotodama-shokunin` @ `17c32302`
target: the counting legs of `reports/round-65/accept-ca.py` (claim Ca, predicate ACCEPT-CA-65)

## 1. What was attacked

The claim-Ca predicate is ten string/counting legs over committed bytes:

| leg | what it actually asserts (read from the counter at the lane tip) |
|---|---|
| R1 | receipt contains `measured revision: 8bab271c…`, a `^tree: <rev-parse 8bab271c^{tree}>$` line, the word `re-stamped`, and `measured revision: 95c9194e…` **after** the marker `original receipt bytes`; plus the literal `Correction (round 65, R1)` in `LOG.md`, `SCORECARD.md`, `.ufo/waves/round-64/w2/LessonFinal.md` |
| R2 | `revisions.txt` starts with the byte-exact base bytes, and contains `Correction (round 65, R2)` + the substring `final-measures-c.txt` |
| R3 | `LOG.md` contains both `w1/ReviewerCa.md` and `w2/ReviewerCa.md`; `SCORECARD.md` contains `Correction (round 65, R3)` |
| R4 | `reports/round-64/claims.json` contains `statement_correction`, `at least their pinned leg`, and the frozen predicate sentence |
| R5 | `control-o.txt` contains `c27a9fef`, `b7d22703`, `revision 3`; `LOG.md` matches /control-o binding/i |
| R6 | `corpus/lessons/round-64.md` contains `Correction (round 65, R6)` **and** `R64-M12` |
| R7 | the entry's `^- verified-at:` line exists and does **not** match /skeleton\|await L1/i |
| CRITERION | `QUALITY.md` has a line matching `^1[7-9]\.\s` and contains `tree hash` |
| QUOTES | `tools/check-gate-quotes.py corpus/lessons/round-65.md` exits 0 **and** prints `0 finding` |

## 2. Fixture and baseline

- `.ufo/waves/round-65/stage/records-fix/` **does not exist** at probe time (dependency finding D1): the ExecRecordsFix draft was unavailable, so the fixes were enumerated from `corpus/lessons/round-64-verifier-spotcheck.md` §6 (R1–R7) plus the counter docstring (CRITERION, QUOTES).
- Because no fix bytes existed, an isolated scratch was built: `git clone --shared` of the lane into `/tmp/mut-ca` (lane HEAD `17c32302`; shared clone holds no lane write), then the untracked round-65 counters and wave dir copied in. **Lane tip baseline, unmodified:** all 10 legs FAIL, `ACCEPT-CA-65: FAIL`, exit 1 (`/tmp/lane-tip-ca.txt`). Lane HEAD and porcelain unchanged throughout (only the pre-existing untracked `reports/round-65/`, `.ufo/waves/round-65/`, `tools/check-row-fragments.py`, and two stray `-.png` files).
- Reference fix set authored **in the scratch only**, faithful to §6: receipt re-stamped with tree `0ec0e50e…` + preserved original bytes; R2/R6 append-only corrections; R1/R3/R5 LOG+SCORECARD+LessonFinal repeats; R4 `statement_correction` with the honest wording; R7 verified-at rewritten; QUALITY criterion 17; a two-row `## Gate` placeholder for the round-65 lesson (that file is a lessons-seat land and is absent at the tip). **Gold baseline: 10/10 PASS, `ACCEPT-CA-65: PASS`, exit 0.** Every mutant below is one edit away from that passing state.
- Runner: each mutant applied to the gold state, `python3 -B reports/round-65/accept-ca.py --root /tmp/mut-ca` executed, then the ten touched files restored from `/tmp/gold` (byte copies of the gold state) and verified with `sha256sum -c`.

## 3. Mutant table

| # | target | mutant (the "looks done but is wrong" edit) | expected detector | observed output | verdict |
|---|---|---|---|---|---|
| M1 | R1 | `tree:` line carries the **wrong commit's** tree — `d6c56169…` (tree of `95c9194e`, the revision the receipt falsely stamped) instead of `0ec0e50e…` | R1 | `R1 FAIL restamp=False tree=0ec0e50ea828… repeats_…=True`; 8 PASS / 1 FAIL, exit 1 | **KILLED** |
| M2 | R2 | false header clause rewritten **in place** (`final-measures-c.txt measured 8d2041fa…` → `0c892ce…`) instead of appending | R2 | `R2 FAIL original_intact=False named=True`; exit 1 | **KILLED** |
| M3 | R4 | frozen predicate sentence edited (`every leg…prints` → `all legs…print`) **only in the claim's `predicate` field** | R4 | no leg fails; 9 PASS, `ACCEPT-CA-65: PASS`, exit 0 | **SURVIVED** |
| M3b | R4 | same edit **plus** the same sentence inside the `statement_correction` quotation | R4 | `R4 FAIL honest_wording_patch=True`; exit 1 | **KILLED** |
| M4 | R6 | correction written in the **wrong lesson** (`corpus/lessons/round-65.md`), removed from `round-64.md` | R6 | `R6 FAIL status_correction=False`; exit 1 | **KILLED** |
| M5 | R7 | fabricated verification: `verified-at: 2026-10-24 — all 26 cited claims re-opened live this round: every URL returned HTTP 200 …` (no such run) | R7 | no leg fails; `ACCEPT-CA-65: PASS`, exit 0 | **SURVIVED** |
| M6 | R3 | correction states the **opposite** mapping: "actual path is `w2/ReviewerCa.md`; erratum target `w1/ReviewerCa.md`" | R3 | no leg fails; PASS, exit 0 | **SURVIVED** |
| M7 | R2 | header present but body **re-asserts the false claim** ("the final-measures-c.txt lines stand as written, including the 8d2041fa header") | R2 | no leg fails; PASS, exit 0 | **SURVIVED** |
| M8 | R5 | binding named but **wrong**: "binds counter revision 5 (`cdee063e…`) measured at `b7d22703`; rev3 was interim" | R5 | no leg fails; PASS, exit 0 | **SURVIVED** |
| M9 | R1 | restamp correct, but the `LessonFinal.md` repeat dropped | R1 | `R1 FAIL … repeats_log_score_lessonfinal=False`; exit 1 | **KILLED** |
| M10 | R6 | `Correction (round 65, R6)` attached to **R64-M11**, explicitly saying "not R64-M12", while M12's stale sentence is untouched | R6 | no leg fails; PASS, exit 0 | **SURVIVED** |
| M11 | CRITERION | criterion 17 present, contains `tree hash`, but **denies the rule**: "a receipt may optionally include a tree hash …; the counter sha is sufficient in practice, and a receipt's stamped revision is taken on trust" | CRITERION | no leg fails; PASS, exit 0 | **SURVIVED** |
| M12 | R7 | stale line **reworded**: `verified-at: 2026-10-23 — cited source claims pending insertion and review.` | R7 | no leg fails; PASS, exit 0 | **SURVIVED** |
| M13 | QUOTES | a `## Gate` row with a 36-word quotation added to `round-65.md` | QUOTES | `QUOTES FAIL exit=1 out=['GATE_QUOTES: 1 findings']`; exit 1 | **KILLED** |

Tally: **13 mutants — 6 killed, 7 survived, 0 inconclusive.**

## 4. Coverage findings (survivors)

1. **R4 is a whole-file containment test, not a predicate check (M3).** Any one occurrence of the exact frozen sentence satisfies the leg. A member who edits the actual `"predicate"` field and leaves the correction quoting the old sentence still prints `ACCEPT-CA-65: PASS`. The leg only bites when the quoted copy is edited too (M3b). Fix shape for round 66: assert the predicate field's parsed value, not `in claims_text`.
2. **R7 is a two-word blocklist (M5, M12).** Rewording the stale sentence ("pending insertion") or substituting a fabricated verification claim both pass. The leg cannot distinguish "corrected" from "re-asserted in other words".
3. **R3 is polarity-blind (M6).** Both path strings must appear, nowhere is their role checked; a correction that inverts actual/erratum is green.
4. **R2 checks the marker, not the correction (M7).** A named entry that re-affirms the 8d2041fa claim passes; only the ordering/byte-prefix half is enforced.
5. **R5 checks the control file, not the binding (M8).** `control-o.txt` already contains the three tokens, so the leg's real content is the substring "control-o binding" in LOG; the binding can be stated as rev5 and pass.
6. **R6 is file-wide co-occurrence (M10).** The marker and `R64-M12` need only appear anywhere in the file; attaching the correction to a different defect (M11) passes with M12 stale.
7. **CRITERION is a keyword test (M11).** A criterion that *contradicts* the R1 rule passes on the words `tree hash`.

Kills are real for the mechanical half of each fix (M1/M2/M4/M9/M13): wrong-commit tree, in-place rewrite, wrong lesson, missing repeat, over-cap quote are each caught.

## 5. Detector quirks observed (instrument notes, not contract changes)

- **QUOTES fails closed but prints a green line:** with an unreadable/missing path, `check-gate-quotes.py` prints `GATE_QUOTES_ERROR: …` **and** `GATE_QUOTES: 0 findings`, exit **2**. accept-ca's QUOTES leg requires exit 0, so the leg fails; any reader grepping only the last line would read a false green.
- **QUOTES is unsatisfiable at the tip:** `corpus/lessons/round-65.md` does not exist (`ls` → absent), and the leg has no "file drafted elsewhere" carve-out. Until the lessons seat lands that file the claim cannot print PASS — a real dependency (D1), not a defect of the fix.
- R1 is the only leg that recomputes from git (`rev-parse`); the rest trust prose. The tree hash does pin the *rev*, but no leg checks that a tree hash was computed at run time — a fabricated but correct tree string passes (same class as M5, not separately probed).

## 6. Restoration evidence

Scratch state after the last mutant was restored from `/tmp/gold` and verified byte-equal; the post-restore run is the gold baseline again:

```
$ sha256sum -c /tmp/gold-hashes.txt        # all ten OK
4fd5c12199bbb0269b621d3cfa56201cf11b66b7debb05fda18206fc91a875ca  reports/round-64/telemetry/final-measures-ca.txt   OK
99fac98e5c50f477b7d4faa564351b2f568cbbc35fe2ed0d50d0e99bb0dce9ed  reports/round-63/telemetry/revisions.txt           OK
0bcfcde5e3693e6830b353b8a4fe5a6ea7b99f7a8a97bb19e8d19f671847f0ea  LOG.md                                             OK
7543befa227e262a5f2bf6b7b671a2c9ed72c4fb11959cbdb5a34f82542ef828  SCORECARD.md                                       OK
32f4625e8633cbc1d5d291e4fdd2c420c6a763944ca733ba14cacc0d295ddc33  .ufo/waves/round-64/w2/LessonFinal.md              OK
c282935cebf67a83f045a1eb280427c9cddc570fa5a2186f8101cc1414072777  reports/round-64/claims.json                       OK
c5788fbd20a0626b1322320ed16f461514628e93ac3f927955d4daadb53d07d5  corpus/lessons/round-64.md                         OK
145bd08ef63fc407b6dd85c1b516620f24f4d3c8cf16fe361475702452f04ef3  corpus/knowledge/linguistics/language-socialization-and-acquisition.md  OK
166d9372e71a34d9acb16ebb07a9807f3a589e2f4a136a0d7a98379ffe82c582  corpus/QUALITY.md                                  OK
4c499d48aa9f97e6411fd5445ed90eedc45c147aceda261b64b101fcbcfaca03  corpus/lessons/round-65.md                         OK

$ python3 -B reports/round-65/accept-ca.py --root .     # post-restore
CRITERION PASS … · QUOTES PASS exit=0 out=['GATE_QUOTES: 0 findings']
ACCEPT-CA-65: PASS                                     exit 0
```

The lane repo itself was never written: `git rev-parse HEAD` stays `17c32302c6845c8f164b985a8cb312d3181c8788`, no lane file or jj/git state touched; all mutation work lived in `/tmp/mut-ca` with the pristine gold in `/tmp/gold`.

## 7. Dependencies and tooling

- **D1 (dependency finding):** `.ufo/waves/round-65/stage/records-fix/` absent → fixes enumerated from spotcheck §6; `corpus/lessons/round-65.md` absent → QUOTES leg unsatisfiable until the lessons seat lands it.
- No tool installs or upgrades this session (host `git`, `python3`, `sha256sum` only).

Report: .ufo/waves/round-65/w1/MutRecords.md
