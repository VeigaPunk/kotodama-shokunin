# ScribeRecord — claim C record repairs (round 83, wave 1)

Lane base `3088bd7fe2a55a123214abba7008dcddf12b301c`; frozen claims `21277b089e3c64c247bb4e0fcb033abfdfa1e668`. This seat owns the three record repairs of claim C. No commit, no counter run: the worktree is uncommitted and the claim counter grades committed lands.

## Behavior

**(a) `reports/round-82/counter-revisions.md` — restored, 7051 B, sha256 `469fb8b273dfea002558364e0be03e2df1e1ca2b173de51f07e851a79704a673`.**

- Opens with the required line: "Restored in round 83 from those committed receipts: …", naming the seven telemetry receipts and `corpus/lessons/round-82.md` `## Mistakes` R82-M6.
- Names both revisions in full — `696835ee5a8f8361031262f02d88299ea775ff1a` (r1→r2) and `ea667212554f7062650ee6942d559bdd35736c05` (r2→r3) — with the old/new sha256 pairs, and states what each changed: r2's QUEUE DUE-set comparison, exactly-one-summary rule, MODULAR NNd boundary probe and selftest 12→14; r3's two added selftest scenarios and selftest 14→16. Red-before (`counter-r1-redbefore.txt`), red-after (`counter-r2-caught.txt`), re-grades (`lands-o82-graded-r2.txt`, `lands-o82-graded-r3.txt`), selftests and the 5/5 mutation receipt are cited repo-relative. All 13 backticked repo-relative tokens resolve at base.

**(b) `reports/round-83/annotations/errata-r82.md` — 1018 B, sha256 `d323391f989bc22de52afd0af84a6e5aebbbc79d33befa4da40467a9c9d710b0`.**

Names R82-M2, the filed `RECHECK-ERROR line 7` in the report parenthetical and lesson row, and the committed `line 5` printed by `.ufo/waves/round-82/w1/stage/ExecEvidence/malformed-row-probe.txt` and its tracked fixture. States the filed bytes stand as history and names the committed probe as the authoritative reading.

**(c) `corpus/QUALITY.md` — criterion 31 appended as line 221, body 3416 B.**

Three clauses binding from round 83: (i) a cited record is nonempty at the revision the report cites; (ii) a committed receipt cites only repo-relative paths that resolve at the cited revision, with no temporary or scratch roots; (iii) a round lesson's `## Gate` names the URL and access date for every row the round opens. The entry carries scope, the `tools/check-cited-records.py` check with its `CITED-RECORDS: <empty> empty / <scratch> scratch` line, the measured red-before at base, grounding in the round-82 verifier spot-check §6, and stated limits. `git diff --numstat -- corpus/QUALITY.md` = `20 0`: no earlier line moved, and the first 219 lines are byte-identical to base.

Red-before/green outputs: `.ufo/waves/round-83/w1/stage/ScribeRecord/checks.md`; delivered-byte hashes: `.ufo/waves/round-83/w1/stage/ScribeRecord/receipts.txt`.

## Gates

Claim-C legs checked in the worktree by construction:

| leg | worktree state |
|---|---|
| CRITERION | exactly one `^31\. ` line (221), body 3416 B, markers `nonempty`/`resolve`/`access date` all present |
| RECORD | 7051 B ≥ 400, both revision hashes present |
| ERRATUM | markers `R82-M2`, `line 5`, `line 7` all present |

Not graded here: BEFORE/FROZENCFG/CHECKER/SUPERSEDE/APPENDONLY/SEPARABLE. `tools/check-cited-records.py` is not yet in the worktree (owned by ExecCitedRecords) and no lands commit exists, so `accept-c83.py` was not run. The L1 must land all three files for the checker's `0 empty / 0 scratch` to hold.

## Findings

1. **Seat spec vs committed bytes (reported, not silently resolved).** The seat spec says "the file was never written". The committed history shows otherwise: `reports/round-82/counter-revisions.md` was committed at 3439 B in `696835ee…` and 5205 B in `ea667212…`, then truncated to 0 B by `d1129213` (the round-82 claim-D counter r2 commit); it is 0 B at base. The restoration follows the seats' receipts as instructed and records this provenance in the file, so the round-82 report's citation is shown to have been honest without asserting a false "never written".
2. **Red-after receipt precision.** The historical r2 record quoted a `QUEUE` first-diff line that the committed `counter-r2-caught.txt` does not print. The restored text states only what the receipt prints (`LEG FAIL MODULAR`, `FAIL legs=5/7`) and notes QUEUE is the other red leg by the count.
3. **r3 scenario count.** The r3 commit message says "three more selftest scenarios"; the diff adds two scenario checks and the receipt moves 14→16. The restored record says two and flags the message.
4. **Erratum location.** No file under `reports/round-82/telemetry/` prints a `RECHECK-ERROR` line. The committed `line 5` evidence is the tracked wave-stage probe and fixture named in the erratum; the erratum states this measured absence.
5. **Scratch roots.** The two round-82 receipts carrying scratch roots are the ones the verifier spot-check §6.6 names (`malformed-row-probe.txt`, `quality30-probe.txt`). The two new report/receipt files contain no scratch root.

## Out of scope

- The S908 superseding row and `SUPERSEDE` leg (rows seat; `corpus/SOURCES.md` was not touched).
- `tools/check-cited-records.py` (ExecCitedRecords).
- The round-83 lesson and its `## Gate` block (ScribeLesson).
- Any commit, push, or branch movement; the L1 lands the bytes.

## Artifacts

- `reports/round-82/counter-revisions.md`
- `reports/round-83/annotations/errata-r82.md`
- `corpus/QUALITY.md`
- `.ufo/waves/round-83/w1/stage/ScribeRecord/checks.md`
- `.ufo/waves/round-83/w1/stage/ScribeRecord/receipts.txt`
- this report: `.ufo/waves/round-83/w1/ScribeRecord.md`

## Limits

The record's self-reference is 0 B at base and 7051 B only once the L1 lands; the checker's green depends on that landing. The record and erratum are prose reconstructions from committed receipts, not new measurements of the round-82 counter runs. The seat scratch directory was created, used for the hash receipt, and removed; nothing was left behind.
