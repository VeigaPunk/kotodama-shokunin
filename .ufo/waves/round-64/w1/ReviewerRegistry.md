# ReviewerRegistry — claim C staged-row audit (round 64, wave 1)

Scope: all 32 declared rows S718–S749 under `.ufo/waves/round-64/rows/*/row.txt`, audited
against the eight seat criteria: (1) 11 cells / no `|` inside cells, (2) kind in enum,
(3) tier A only for primary/official sources, (4) scoped-not-global scope cell,
(5) anchor = verbatim 8–25-word quote + locator, (6) teaches ≤25 words,
(7) mined rows opened 2026-10-23 / recheck 180d, (8) reject rows
`REJECTED:`/`QUEUED-CANDIDATE:` + `; flip:` + used-by `—`.

Axes named (godspeed): coverage (duplicate/spurious rows shrink real coverage),
operability (does the staged artifact satisfy the frozen row contract the counter pins),
calibration (tier/scope honesty). All quotes below were extracted with the same
QUOTE_RE/cells logic as `.ufo/waves/round-64/check-rows.py`.

## Verdict per row

| Row | cells | kind | tier | scope | anchor | teaches | open/recheck | reject shape | Verdict |
|-----|-------|------|------|-------|--------|---------|--------------|--------------|---------|
| S718 | 11 | paper | A | scoped | 9w + locator ✓ | 16w | ✓ | — | OK (quote verified live) |
| S719 | 11 | paper | B | scoped* | 24w + locator ✓ | 16w | ✓ | — | OK |
| S720 | 11 | paper | A | scoped | 24w + locator ✓ | 20w | ✓ | — | OK (verified live) |
| S721 | 11 | paper | A | **wider than quote** | 18w + locator ✓ | 13w | ✓ | — | LOW (F5) |
| S722 | 11 | paper | B | scoped* | 17w + locator ✓ | 17w | ✓ | — | OK |
| S723 | — | — | — | — | — | — | — | — | **MISSING (F1)** |
| S724 | 11 | book | B | scoped* | 16w + locator ✓ | 16w | ✓ | — | OK (residual R1) |
| S725 | 11 | paper | B | scoped | 19w + locator ✓ | 16w | ✓ | — | OK |
| S726 | 11 | paper | A | scoped | 19w + locator ✓ | 13w | ✓ | — | OK |
| S727 | 11 | paper | B | scoped | 16w + locator ✓ | 15w | ✓ | — | OK |
| S728 | 11 | book | B | scoped | 14w + locator ✓ | 10w | ✓ | — | OK |
| S729 | 11 | paper | A | scoped | 17w + locator ✓ | 19w | ✓ | — | **DEFECT (F2)** |
| S730 | 11 | book | B | scoped* | 24w + locator ✓ | 18w | ✓ | — | OK (LOW, F6) |
| S731 | 11 | paper | A | scoped | 23w + locator ✓ | 17w | ✓ | — | OK (verified live) |
| S732 | 11 | paper | B | scoped | 19w + locator ✓ | 15w | ✓ | — | OK |
| S733 | 11 | paper | A | scoped | 15w + locator ✓ | 14w | ✓ | — | OK |
| S734 | 11 | paper | A | scoped | 16w + locator ✓ | 17w | ✓ | — | OK |
| S735 | 11 | paper | A | scoped | 17w + locator ✓ | 18w | ✓ | — | OK |
| S736 | 11 | paper | A | scoped | 10w + locator ✓ | 15w | ✓ | — | OK (verified live) |
| S737 | 11 | paper | A | scoped | 25w + locator ✓ | 16w | ✓ | — | OK (25w at boundary) |
| S738 | 11 | book | A | scoped | 20w + locator ✓ | 13w | ✓ | — | OK |
| S739 | 11 | paper | A | **mismatch** | 13w + locator ✓ | 17w | ✓ | — | **DEFECT (F3)** |
| S740 | — | — | — | — | — | — | — | — | **MISSING (F1)** |
| S741 | 11 | paper | A | scoped | 12w + locator ✓ | 13w | ✓ | — | OK (verified live) |
| S742 | 11 | paper | A | scoped | 23w + locator ✓ | 18w | ✓ | — | OK |
| S743 | 11 | paper | A | scoped | 10w + locator ✓ | 18w | ✓ | — | OK (verified live) |
| S744 | 11 | docs | B | scoped | 14w + locator ✓ | n/a | ✓ | REJECTED:+flip+— ✓ | OK |
| S745 | 11 | docs | A | scoped | 11w + locator ✓ | n/a | ✓ | REJECTED:+flip+— ✓ | OK |
| S746 | 11 | docs | B | scoped | 17w + locator ✓ | n/a | ✓ | QUEUED:+flip+— ✓ | OK |
| S747 | 11 | docs | B | scoped | **not verbatim** | n/a | ✓ | REJECTED:+flip+— ✓ | **DEFECT (F4)** |
| S748 | 11 | book | B | scoped | 11w + locator ✓ | n/a | ✓ | QUEUED:+flip+— ✓ | OK |
| S749 | 11 | community | C | scoped | 21w + locator ✓ | n/a | ✓ | QUEUED:+flip+— ✓ | OK (LOW, F7) |

\* = topic-style scope cells (see F6) — inside registry convention, flagged only where
it exceeds the anchored evidence.

## Findings

**F1 (coverage, blocking) — S723 and S740 have no `row.txt`.**
`.ufo/waves/round-64/rows/` contains 30 of the 32 declared rows; `ScribeRowS723` and
`ScribeRowS740` directories do not exist. Known inherited attempt-1 defect (30/32 under
check-rows.py); restaging is in flight (`kotodama-r64.ExecRowS723` peer live). Until both
land, claim C's 26-mined-row statement cannot be verified and `check-rows.py` reports them
as MISSING.

**F2 (coverage, real defect) — S729 is a same-work duplicate of S718.**
Both rows cite Farran, Lee, Yoo & Oller 2016, *Cross-Cultural Register Differences in
Infant-Directed Speech*, PLOS ONE 11(3):e0151518 — S718 via
`pmc.ncbi.nlm.nih.gov/articles/PMC4794163/`, S729 via the DOI URL
`journals.plos.org/plosone/article?id=10.1371/journal.pone.0151518`. Both scope and
teaches state the identical finding (Lebanese mothers' higher IDS utterances/minute vs
American mothers); their anchors quote the same Results sentence in two phrasings
(verified: `Lebanese mothers, compared to American mothers, produced more IDS …` and
`with the Lebanese mothers using more IDS Utterances per Minute across both Registers
than the American mothers`). `check-rows.py`'s dup_live_url leg cannot catch this because
the live URLs differ — it is a work-level duplicate, not a URL duplicate. Fix: drop one
row (or re-scope one row to a genuinely distinct claim of the paper) and substitute a new
source for the freed id; the entry bullet for the dropped row must be rewritten.

**F3 (coverage/calibration, real defect) — S739 anchor does not support the scoped claim;
tier A inflated.**
Scope = "parental use of address terms with children in urban Sleman, Indonesia" — i.e.
the paper's own findings. But the anchor quote, "Parents can use various terms of address
to children depending on situational contexts.", is the paper's *introduction citing Aledo
(2018)* — a secondhand general claim, not the study's Sleman evidence. The locator even
discloses it ("paragraph beginning According to Aledo (2018)"). As anchored, the row is
not primary evidence for the scoped claim, so tier A is inflationary; either re-anchor to
the paper's own results (keeping A if verbatim) or downgrade to B for the literature-review
claim.

**F4 (form defect, cosmetic on a reject row) — S747 anchor carries fabricated meta-text as
the "quote".**
`wording tested: "Britannica's Mortarboard page as evidence for mortarboard use in
academic dress"` is the scribe's description of intent, not verbatim source text — the
TEST line shows the real fetch was 403, so no verbatim quote could be captured. Other
rejects handle this honestly (S744 quotes the tested wording it expected; S745 quotes the
definition). Recommend reformatting S747's anchor to state the 403 outright (e.g.
`HTTP 403 on 2026-10-23; no verbatim quote retrievable`) rather than presenting intent as
a quotation.

**F5 (LOW) — S721 scope wider than its anchored evidence.**
Scope covers "infant vocal turn-taking **and** protoconversation in early development";
the quote only defines protoconversation. Narrow the scope to the protoconversation
definition or add a turn-taking anchor. Tier A itself is fine (the sentence is the
paper's own statement; verified live at PMC9271548).

**F6 (LOW / observation) — topic-style scopes: S719, S722, S724, S730 (and F5's S721).**
These scope cells name a topic/phenomenon rather than a bounded claim (e.g. S730
"simultaneous bilingual first-language acquisition from birth"). This is within existing
registry convention (cf. S001–S003) so not a violation, but S721 is the one case where the
topic exceeds the anchored quote.

**F7 (LOW) — S749 kind = `community`; registry convention for Wikipedia is `docs`.**
The only prior Wikipedia row, S178, uses `docs | C`. `community` for "Wikipedia
contributors" is defensible but inconsistent; align to `docs` for uniformity.

## Structural checks (all 30 present rows)

- Exactly 11 cells each; every ROW line starts `|` and ends `|`, so no unescaped `|`
  inside any cell.
- All kinds in the enum: paper×17, book×4, docs×4, community×1. `community|C` (S749) is a
  valid tier-kind pair under registry convention.
- All 24 mined rows: status=mined, opened=2026-10-23, recheck=180d, used-by =
  corpus/knowledge/linguistics/language-socialization-and-acquisition.md. ✓
- All 6 reject rows: teaches starts `REJECTED:` (S744, S745, S747) or `QUEUED-CANDIDATE:`
  (S746, S748, S749), contains `; flip:`, used-by = `—`. ✓ (Rejects also carry
  opened/recheck — extra but consistent with registry rows S028/S178.)
- Quote word counts: all 30 within 8–25 (min 9 @ S718; max 25 @ S737). All anchors carry
  a textual locator (section/paragraph/page). ✓
- Teaches ≤25 words on all mined rows (max 20 @ S720). Reject teaches exceed 25 by design
  (REJECTED:+flip format), matching registry precedent.
- Verbatim spot-verification against live sources, 2026-10-23 (curl, HTTP 200):
  S718, S720, S721 (PMC); S729 (PLOS); S731 (PMC); S736 (Frontiers); S741 (SciELO);
  S743 (BLS PDF via pdftotext). All eight match verbatim. Not verified offline: S719,
  S722, S724–S728, S730, S732–S735, S737–S739, S742, and reject-row tested wordings —
  `VERIFY: LOCATED` lines attest, not independently re-fetched here.

## Residual risk

- **R1:** S724's ACCESS line reports live direct GET = HTTP 403; the row's live URL and
  LOCATED claim rest on the archive capture. If accept-c's LIVE leg requires a live fetch
  for every mined row, S724 needs the same treatment S727 got (or its ACCESS wording
  reconciled); flagging so the integrator checks which leg applies.
- **R2:** The F2 duplicate means the 26-row breadth claim effectively buys 25 distinct
  sources until fixed.
- **R3:** Reject-row tiers (S745 = A for a rejected source) record the source's standing
  rather than usability; consistent with S178-type convention but worth a style note.
- **R4:** ~16 mined quotes unverified offline (see above); verbatimness rests on scribe
  LOCATED attestations.

## Tooling

No installs performed. Used: Python 3 (row parsing, same regexes as check-rows.py),
curl (live quote verification), system `pdftotext` for the BLS PDF. No files mutated
outside this report.
