# CriticC97 — falsification attempt on claim C (r97 w1)

Full detail, all commands with rc, and the supporting outputs: `stage/CriticC97/critic.md` (plus sweep-base.txt, sweep-work.txt, overlap.txt, counter.txt, verify-c2.txt, sample*.txt, census-final.txt and the scripts). Lane files were not edited; nothing committed.

## Verdict

Claim C **survives the frozen predicate**. The frozen counter (predispatch.py, read-only, work dir in scratch, base 1ffc5a8) returns C1–C8 PASS on the landed tree (rc 1 overall, because O3 fails on the not-yet-landed mutation pin; outside claim C). No C-leg is falsified.

Three sourced or adjacency sub-claims are falsified (F1–F4 below). The frozen counter does not measure them. They are defects for the L1 to record and repair; they are not a C-leg failure.

## Key numbers (command, rc)

- Base C8 replication, `sweep.py base`: rc 0; 268 files; surface owners 0; prose/table mentions 3.
- Landed sweep excluding the entry: other owners 0 (the entry's own H1 is the only surface hit, excluded by the frozen counter).
- Census `validate --file corpus/SOURCES.md`: rc 0; E-codes 0; W-codes 35 (warnings).
- `tools/check-corpus-index.py --root <lane>`: rc 0, `CORPUS-INDEX: OK files=269 rows=269 findings=0`.
- Registry: base 908 rows, highest S984; landed 917 rows, highest S993; new S985–S993 (9); entry cites S985–S992 (8); rows.md ids = S985–S993; S993 = Threnoi row, outside claim C.
- Located-quote recount S985–S992: count == 1 on each recorded capture (rc 0). All eight rows opened 2026-11-05; tier A or B; status mined; used-by exactly the entry path.
- Overlap, word 8-grams (overlap.py, rc 0) vs oath-blessing-curse-formulae.md: **294** shared distinct 8-grams (4.6% of the entry's 6325 distinct); top spans 44 / 43 / 33 tokens (boundary and handoff prose). greeting-leave-taking: 7 shared, one 14-token span. Other adjacent owners (orality, politeness, secret-ludic, binding-speech, trickster, arabia, games): 0.
- Source sampling: 35 checks, rc 0. 27 quoted or keyword substrings count 1; one quoted token absent (see F1).

## Falsifications

- **F1 (quote discipline, S986 §5).** The entry quotes "judgement". The capture has no such token (count 0); the source reads `judg- [page break] … mcnt” in his favor`. The substance is supported; the quote is not an exact substring.
- **F2 (unsourced, marked design, contradicted by its cited source, S985 §4).** "…the person insulted is required to sit still rather than answer… no single author to blame…" is attributed to an unnamed "tradition this entry opens" and labelled design. S985 states the haló offended party "is expected to answer—even with physical violence", and that in the ashik case the angry poet "would literally be seen as the cause of the offense".
- **F3 (neighbour misstatement, §6).** "the same four slots the corpus already teaches for the binding utterance — performative framing, assertion, warrant and consequence". oath-blessing-curse-formulae.md names five slots at :59 and six at :200 and :225; none of the four names matches; "warrant" is not a slot there.
- **F4 (duplicate authority, adjacency; blind to C8).** The canon-boundary, calibration and handoff paragraphs of the entry are near-verbatim adaptations of oath-blessing-curse-formulae.md:35, :37, :225, :227, :229 (294 shared 8-grams).

Minor, not separately falsified: "not invited" (S987 has no invitation sense; Othin does order "Find a seat at our feast" so "given one" holds); "named office" unmarked; "whole region" overreaches "all down the west coast"; some table cells credited to Bellows/Ruszkiewicz are design cells.

## Step-by-step

1. Surface unowned by content: yes. Base has no topic or heading carrying a frozen phrase. Closest substantive neighbour is arabia-pre-islamic.md:69–74 (Fakhr/Hijāʾ qaṣīdah modes); the entry's naqāʾid paragraph overlaps that domain without citing it. Expansion, not duplicate contest authority.
2. Overlap: see numbers above.
3. Row recount and id match: pass (8/8 at count 1; rows.md = entry ids plus Threnoi).
4. Unsourced claims and source support: F1, F2, F3, minor list; 35 sampled checks.
5. Verdict: claim C survives its frozen legs; sourced-accuracy and adjacency defects F1–F4 are not captured by C1–C8.

## Smallest safe correction (for the L1)

Unquote "judgement" (paraphrase); rewrite §4 with a named tradition, the S985 haló statement and the ashik passage, or mark it inference with the contrary passage cited; correct the §6 slot sentence to cite oath :59 and :200/:225; replace the copied boundary/calibration/handoff paragraphs with a pointer to oath §1/§12; mark or remove the minor inferences.

## Tooling

None installed or upgraded. Scratch dir /fast/scratch/hyaku/kotodama-r97/CriticC97/ removed before yield.
