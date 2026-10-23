# Round-60 repair records — draft for L1 integration

Text-only handoff. The filed round-60 report is not rewritten. No LOG.md, SCORECARD.md, lesson, source, counter, or other lane file was changed; ACCEPT-D-60 was not rerun.

## Verification notes and commands/results

**Committed final measure.** I read `reports/round-60/telemetry/final-measure.txt`; I did not execute its counter command. The committed receipt records:

```text
$ PYTHONDONTWRITEBYTECODE=1 python3 -B reports/round-60/accept-d.py
(lane tip 47f27bd0cb0bea219f21cd731c2eb0fe71f7f626 + support-wave outputs in the worktree; counter sha256 cf068177330384edb449b006c9d88a24d1bcb85ce80f562da951398efe24b10d; 2026-10-23T07:56:27Z)
SET PASS cited=47 want=47 missing=[] extra=[] retired_cited=[]
LINES PASS bad=[]
OLDWORD PASS present=[]
ROWS PASS bad=[]
PINNED PASS bad=[]
JUDGED PASS entry equals the judged object
SUPPORT FAIL
ACCEPT-D-60: FAIL
exit=1
```

The full committed `SUPPORT FAIL` row lists these seat outcomes: `SupportA60:X2/sees:bash-cwd-outside-sandbox`, `SupportB60:Q2`, `SupportC60:Q2`, `SupportD60:X2/sees:deny:chr(`, `SupportE60:Q2`, `SupportF60:X2/sees:deny:chr(`, `SupportG60:Q2`, `SupportH60:Q2`, `SupportI60:Q2`, `SupportJ60:Q2`, `SupportK60:Q2`, `SupportL60:X2/sees:deny:chr(`, `SupportM60:Q2`, `SupportN60:Q2`, `SupportO60:Q2`, `SupportP60:X2/sees:bash-cwd-outside-sandbox`, `SupportQ60:X2/sees:bash-cwd-outside-sandbox`, `SupportR60:X2/sees:bash-cwd-outside-sandbox`, `SupportS60:X2/sees:kotodama`, `SupportT60:Q2`, `SupportU60:X2`, `SupportV60:X2/sees:bash-cwd-outside-sandbox`, `SupportW60:X2/sees:deny:chr(`, `SupportX60:Q2`.

Thus the 11 unqualified are **5** `bash-cwd-outside-sandbox` (A, P, Q, R, V), **4** `deny:chr(` (D, F, L, W), **1** `kotodama` BLIND token (S), and **1** bare `X2` with no verdicts (SupportU60). The receipt's qualified list contains SupportX60, and its NOT-SUPPORTED verdict on S646 is counted. It is not one of the voids.

**SupportU60 verdict count.** Requested check: `grep -c '^VERDICT ' .ufo/waves/round-60/support/SupportU60.md`. I used the specialized grep query `^VERDICT ` on that committed file; result: `No matches found` (zero matching lines). The committed SupportU60 report itself says it issues no per-block verdicts. This agrees with `SupportU60:X2` in the final-measure seats field.

**pypdf disclosures.** A specialized `pypdf` search of `.ufo/waves/round-60/` found the five materialization disclosures: `RescoreMechA3.md:13`, `MutEvidenceA3.md:94`, `CtlNarrowA3.md:617`, `CtlGenericA3.md:583`, and `CtlKeyedLabelA3.md:439`. Each records pypdf 5.4.0 through `uv run --with` for the pinned PDF locator/extraction. Other pypdf mentions in the search output describe reuse or no install, not additional materializations. No tool was installed or updated for this assignment.

**R60-M6 packet precision.** The committed entry has the S612-only statement at line 69, the S612/S613 joined statement at line 95, and the further S612 statement at line 120. `reports/round-60/build-packets.py:50-52` gathers every entry line that cites the id and joins them into the packet field. The committed `packet-SupportD60.md` P05 entry field visibly contains all three propositions, including the S613 `tälsäm boxes were strung as a necklace` clause. R60-M6 must say the packet joined lines 69, 95, and 120—not line 95 alone.

**S646 label discrepancy (do not silently repeat the supplied P07 label).** The assigned prompt and spot-check §5 call the S646 altars/temples finding `SupportB60 P07`. The committed `.ufo/waves/round-60/support/planted-key.json` maps `P01` to `S646` and `P07` to `PLANTED`; `packet-SupportB60.md` P01 is the Asian Ethnology page, and `SupportB60.md` P01 is the NOT-SUPPORTED altars/temples verdict. `corpus/SOURCES.md` S646 quotes the page's “in their own temples” and teaches “at their own altars.” Therefore the correction draft below identifies it as **SupportB60 P01** and explicitly records that the spot-check's P07 label conflicts with the committed packet/key. The S646 over-reach itself is verified; its label in §5 is not.

## (1) Appended report correction block — draft

```markdown
## Corrections to the round-60 report

The filed report remains unchanged; these are append-only corrections.

- **Missing heading and misplaced content.** The report has no `## Gate` heading. Its line 55 discernment text and line 57 “Real rejects this round” paragraph sit under `## SHONEN`; the underlying Gate section remains in `corpus/lessons/round-60.md`.
- **Control and revision history.** Report line 46's “five pre-data controls” is superseded by line 55: three controls met earlier counters (CtlNarrowA3, CtlKeyedLabelA3, MutEvidenceA3), while RescoreConfineA3 found an evasion. Revision 5 was forced by the L1's own pre-control review recorded in `claims.json` `revision_note_5`, not by a control receipt; report line 10 overstates the receipt provenance for that revision.
- **Unqualified-seat tally and SupportX60.** The 11 unqualified seats were five `bash-cwd-outside-sandbox` (SupportA60, P60, Q60, R60, V60), four `deny:chr(` (SupportD60, F60, L60, W60), one `kotodama` BLIND token (SupportS60), and one bare X2 with no verdicts (SupportU60). “Five `deny:chr(`” and “11 voided by CONFINED” are incorrect. SupportX60 was qualified and counted, including its S646 NOT-SUPPORTED verdict; it was not voided by the counter despite its self-reported `multi_tool_use.parallel` breach.
- **pypdf disclosure.** pypdf 5.4.0 was materialized through `uv run --with` by five seats: RescoreMechA3, MutEvidenceA3, CtlNarrowA3, CtlGenericA3, and CtlKeyedLabelA3—not only the first two named in report line 66.
- **R60-M6 precision.** The S612 packet entry joined entry lines 69, 95, and 120. Line 95 itself contains S612 and S613 claims; it was not the sole line joined into the packet.
- **Registry teaches candidate.** Add S646 to S601, S608, S614, S624, S636, S640, and S641 as a superseding-row candidate: the S646 teaches cell says “at their own altars,” while its source says “in their own temples.” The committed packet/key identify this as SupportB60 P01 (P07 is PLANTED); the spot-check §5's “SupportB60 P07” label is inconsistent with those committed artifacts. Keep the routed re-reviews of S604, S610, S615, S628, S631, and S646.
```

## (4a) LOG.md entry — draft

```markdown
## 2026-10-23 — Round 60 report corrections (records, not a claim)

- Filed report `.ufo/reports/round-60/kotodama.md` is not rewritten. Append the erratum: it has no `## Gate` heading (line 55 and the “Real rejects” paragraph at line 57 sit under `## SHONEN`); line 46's “five pre-data controls” is superseded by three met controls (CtlNarrowA3, CtlKeyedLabelA3, MutEvidenceA3) plus RescoreConfineA3's evasion; revision 5 came from the L1's own review in `claims.json` `revision_note_5`, not a control receipt.
- Correct the 11-seat breakdown from `reports/round-60/telemetry/final-measure.txt`: five `bash-cwd-outside-sandbox` (A/P/Q/R/V), four `deny:chr(` (D/F/L/W), one `kotodama` BLIND token (S), and SupportU60's bare X2 with no verdicts. SupportX60 is qualified and counted, not voided. The SupportU60 report has zero `VERDICT` lines.
- Correct the install disclosure: five seats materialized pypdf 5.4.0 via `uv run --with`—RescoreMechA3, MutEvidenceA3, CtlNarrowA3, CtlGenericA3, and CtlKeyedLabelA3.
- Clarify R60-M6: the S612 packet joined entry lines 69, 95, and 120, not only line 95. Add S646 to the superseding-row candidates S601, S608, S614, S624, S636, S640, S641; preserve the routed re-reviews of S604, S610, S615, S628, S631, and S646.
- **Packet-label conflict:** the requested/spot-check wording calls the S646 altars/temples reject SupportB60 P07, but committed `planted-key.json` maps P01 to S646 and P07 to PLANTED; `SupportB60.md` records the altars/temples reject at P01. Record it as P01, not P07. Evidence: `.ufo/waves/round-60/support/planted-key.json`, `packet-SupportB60.md`, `SupportB60.md`, and `corpus/SOURCES.md` S646.
- No claim verdict changes: the committed final measure remains ACCEPT-D-60 FAIL (SUPPORT FAIL; exit 1). Evidence: the final measure, spot-check §§1 and 5, and `corpus/lessons/round-60.md` R60-M6/R60-M7.
```

## (4b) SCORECARD correction-table block — draft

```markdown
Correction rows for round 60 (recorded in round 61; verifier spot-check §5; filed round-60 report not edited):

| corrected row | correction | evidence |
|---|---|---|
| round-60 report structure and pre-data controls | No `## Gate` heading; line 55 and “Real rejects” at line 57 are under `## SHONEN`. Line 46's “five pre-data controls” is superseded by three met controls plus RescoreConfineA3's evasion. Revision 5 was forced by the L1's review in `revision_note_5`, not a control receipt. | `.ufo/reports/round-60/kotodama.md` lines 10, 46, 48–59; `reports/round-60/claims.json` `revision_note_5`; spot-check §1 |
| round-60 unqualified seats and SupportX60 | 11 = five `bash-cwd-outside-sandbox` (A/P/Q/R/V), four `deny:chr(` (D/F/L/W), one `kotodama` BLIND (S), one bare X2 with no verdicts (SupportU60). SupportX60 is qualified and counted, not voided. | `reports/round-60/telemetry/final-measure.txt`; `.ufo/waves/round-60/support/SupportU60.md`; `SupportX60.md`; spot-check §1 |
| round-60 pypdf disclosure | Five materializations via `uv run --with pypdf==5.4.0`: RescoreMechA3, MutEvidenceA3, CtlNarrowA3, CtlGenericA3, CtlKeyedLabelA3. | `.ufo/waves/round-60/resid-a3/RescoreMechA3.md:13`, `MutEvidenceA3.md:94`; `.ufo/waves/round-60/w1-a3/CtlNarrowA3.md:617`, `CtlGenericA3.md:583`, `CtlKeyedLabelA3.md:439`; spot-check §1 |
| R60-M6 packet precision | S612 packet entry joined lines 69, 95, and 120; line 95 alone is not the full joined entry. | `reports/round-60/build-packets.py:50-52`; `.ufo/waves/round-60/support/packet-SupportD60.md` P05; amulets entry lines 69, 95, 120 |
| S646 registry teaches cell | Add S646 to the superseding-row candidates S601, S608, S614, S624, S636, S640, S641: its teaches cell says “at their own altars” where the source says “in their own temples.” Committed artifacts label the finding SupportB60 P01, not P07 (P07 is PLANTED), contrary to spot-check §5's label. | `corpus/SOURCES.md` S646; `.ufo/waves/round-60/support/planted-key.json`, `packet-SupportB60.md`, `SupportB60.md`; spot-check §5 |
```

## Scope and limits

These are drafted records for L1 integration only. No filed report, LOG, SCORECARD, round-60 lesson, packet, or counter was edited. The committed final-measure output was read, not regenerated; the report's own session-pin warning remains in force for any future ACCEPT-D-60 rerun. The P07/P01 mismatch is surfaced rather than reconciled by assumption.