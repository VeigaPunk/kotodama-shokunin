# ReviewCSec04 — C entry §4 (community ecology) vs S091/S092/S093

Seat: KotodamaR51a3.ReviewCSec04, round 51 attempt 3 falsify, 2026-10-22. Attack target: `corpus/knowledge/linguistics/sign-languages-manual-modality.md` §4 (lines 68–79), figures against SOURCES rows S091 (`corpus/SOURCES.md:120`), S092 (`corpus/SOURCES.md:121`), S093 (`corpus/SOURCES.md:122`). Author-lane attack, not admission.

## Item attacked

§4 table cells: Adamorobe >10% in 1961 / ~2% by 2001 (S091); Bengkala recessive gene ≥7 generations, ~1,200 hearing signers (S092); Martha's Vineyard high hereditary deafness and shared signing (S093); schools row "most Deaf children learn their sign language only after entering school; ~5% are born to Deaf parents (S091)"; chief's deaf-deaf marriage bar (S091); endangerment cells (S091, S092). Also drift checks: clinical genetics, education policy, rights rulings, canon.

## Commands run (all exit 0 unless noted)

| Command | Output |
|---|---|
| `grep -n -E "1961\|1975\|per cent\|% \|survey" nyst2007.txt` (scratch pdftotext of S091 PDF) | `642: During a medical survey in 1961, Sir Alexander Drummond noticed an` / `645: estimated to occur in more than 10% of the population at that time.` / `799: from 10% in 1971 to around 2% at present` / `826: percentage of deafness from 10% in 1961 to 2% in 2001` |
| `curl -sS -L -o nyst2007.pdf https://www.lotpublications.nl/Documents/151_fulltext.pdf` | exit 0, 6,344,960 bytes, `PDF document, version 1.6`; `pdftotext -layout` converted (benign font-collection warnings on stderr) |
| `curl -sS -L -o elar-dk0124.html https://www.elararchive.org/dk0124` | exit 0, 49,692 bytes, title "Longitudinal Documentation of Sign Language Acquisition in a Deaf Village in Bali \| Endangered Languages Archive" |
| `curl -sS -o hup-direct.html -w "%{http_code}" https://www.hup.harvard.edu/books/9780674270411` | `http=202`, 0 bytes (JS/WAF interstitial; matches the S093 row's note) |
| `curl -sS -L -o hup-wayback.html "https://web.archive.org/web/20241210011800/https://www.hup.harvard.edu/books/9780674270411"` | exit 0, 297,892 bytes, title "Everyone Here Spoke Sign Language — Harvard University Press" |
| `grep -n -i -E "Mitchell\|Karchmer\|born to [Dd]eaf\|5% of" corpus/SOURCES.md` | no matches — no row in the registry is primary for the deaf-parent demographic figure |
| `grep -c "sign-languages-manual-modality.md" corpus/SOURCES.md` | 52 (S071–S122, each row's used-by cell names the entry) |

Downloads went to `/fast/scratch/hyaku/kotodama-r51a3-falsify/ReviewCSec04/` only (`realpath` verified). No writes in the lane except this report. No installs were needed (pdftotext, curl, python3 already present).

## Sources opened 2026-10-22

1. **S091** — https://www.lotpublications.nl/Documents/151_fulltext.pdf (Nyst 2007, full dissertation PDF). Found at the stated anchors (§1.3–§1.6, PDF pp. 19–35): §1.3.2 p. 23 "Out of a total sample of 400 inhabitants, 45 were found to be deaf … Deafness was then estimated to occur in more than 10% of the population at that time"; pp. 24–25 Table 1.1 (45 deaf / 400 in 1961; 35 / 1,356 in 2001) and "the drop of the percentage of deafness from 10% in 1961 to 2% in 2001"; p. 25 "The high immigration rate more effectively explains the drop … than does genetic counselling"; §1.3.4 pp. 26–27 boarding school at Mampong-Akuapem where "Ghanaian Sign Language (GSL) is used"; §1.3.5 pp. 28–29 "Former chief Nana Kwaakwa Asiampong II prohibited marriage between two deaf persons"; §1.4 p. 30 "proficiency in AdaSL depends on the degree of contact and ties with deaf persons"; §1.4 p. 32 "AdaSL should be classified as potentially endangered"; §1.5 p. 32 "the primary sign language of the school-going generation appears to be GSL"; §1.6 p. 33 "only an estimated 5% of Deaf children are born to Deaf parents. As a result, most adult members of the large Deaf communities acquired sign language only after entering school." Quote, tier A, and scope hold for the Adamorobe-case cells.
2. **S092** — https://www.elararchive.org/dk0124 (de Vos 2013, ELAR deposit landing page, public, HTTP 200). Found at the stated anchors, which exist verbatim as page sections ("Summary of the collection", "Group represented", "Language information"): "48 deaf signers, and 1,200 hearing community members used Kata kolok"; "caused by a recessive gene which emerged in the village at least seven generations ago"; "approximately 1,200 hearing signers"; "emerged in response to a sudden rise in the incidence of deafness"; "threatened by the increasing number of sign-bilinguals using Indonesian Sign Language … as well as recent changes in marital patterns". Quote, tier A (depositor's own statement), and scope hold.
3. **S093** — https://www.hup.harvard.edu/books/9780674270411 returned HTTP 202 with an empty body (script-gated, as the row notes); read via the row's cited Wayback capture https://web.archive.org/web/20241210011800/https://www.hup.harvard.edu/books/9780674270411. Found: product description ¶1 ("extremely high rate of profound hereditary deafness", integration) and ¶2 ("hearing and Deaf islanders alike grew up speaking sign language"), then a "Praise" block of six review blurbs (Sacks, Village Voice, Scientific American, British Journal of Audiology, Qualitative Sociology, Choice). Tier B publisher description correctly tiered per QUALITY criterion 6; substance holds (see finding L2 on the anchor label).

## Findings

### M1 (medium) — §4 schools cell generalizes past Nyst's scope and contradicts the sibling rows
`corpus/knowledge/linguistics/sign-languages-manual-modality.md:76`: "most Deaf children learn their sign language only after entering school; ~5% are born to Deaf parents (S091)". Nyst §1.6 (PDF p. 33) says "most **adult members of the large Deaf communities** acquired sign language only after entering school" — a retrospective claim scoped to large Deaf communities. The entry's recast drops the qualifier and turns it into a claim about Deaf children generally; read as written, it conflicts with the same table's village rows (deaf children in Adamorobe and Bengkala acquire the village sign at home). Smallest fix: "in large Deaf communities most members acquire their sign language only at school; ~5% of Deaf children are born to Deaf parents (S091)".

### M2 (medium) — S091's scope cell excludes the general demographic claim it is cited for
`corpus/SOURCES.md:120` scope: "the Adamorobe case as documented by Nyst's own 2001 fieldwork and the studies she reports … **not other sign-language claims**". The 5%/school-acquisition figure is §1.6 background about Deaf communities worldwide (Nyst states it without attribution), not the Adamorobe case; it falls inside the anchor list but outside the scope sentence, against QUALITY criterion 6's claim-scoping. No other registry row covers it (`grep` for Mitchell/Karchmer: 0 rows). Smallest fix: a superseding SOURCES row (never an in-place edit) whose scope explicitly adds "§1.6 general background: 5% Deaf-parent figure, school-acquisition pattern of large Deaf communities", or a dedicated demographics row.

### L1 (low) — S093 anchor mislabel: "product description ¶1 and ¶3"
`corpus/SOURCES.md:122`. The cited capture's description block has exactly two paragraphs; the third text on the page is a Choice review blurb under "Praise". The row's substance is supported at ¶1–¶2 (and the community-bilingualism line by the Choice blurb), so the row survives; only the anchor string is wrong. Smallest fix: superseding row with anchor "product description ¶1–¶2 (Praise: Choice blurb for the community-wide bilingualism line)".

### L2 (low) — §14 recheck list omits S091–S093
`corpus/knowledge/linguistics/sign-languages-manual-modality.md:219` mandates re-opening S080/S100, S085, S084/S116, S077/S120/S121 — but not S091–S093, which back the only numeric ecology cells in the entry (1961/2001 prevalence, ≥7 generations, ~1,200). Smallest fix: append "re-open S091–S093 before quoting the §4 ecology figures".

### L3 (low) — §4 table lacks the local uncited-cell convention note
`…manual-modality.md:70` introduces the six dials without the "cells without a citation are lane heuristics (**H**) or `(to-verify)`" marker that §3 (`:54`) and §11 (`:164`) each carry; §4's lever column is uncited by design. Smallest fix: one clause in the §4 intro mirroring `:54`.

### Observation (no defect) — Nyst's own base-year inconsistency
Nyst p. 24 says "from 10% in **1971** to around 2% at present" while p. 25 and Table 1.1 say 10% in **1961** (Drummond's 1961 estimate, reported by David et al. 1971). The entry uses the 1961 framing, which pp. 23/25 support; future quote-miners should not lift the p. 24 sentence.

## Verified as holding (attack failed on these cells)

- ">10% in 1961, ~2% by 2001 (S091)" — p. 23 and pp. 24–25 as quoted above; the entry's tilde covers Nyst's "around 2%".
- "hearing villagers sign, fluency tracks contact (S091)" — p. 30 verbatim.
- "a school generation can shift the language (AdaSL → GSL)" — pp. 31–32.
- "potentially endangered (S091)" — pp. 31–32; "mobility dilutes them" lever matches p. 25's immigration explanation.
- "former chief barred deaf-deaf marriage (S091)" — pp. 28–29; the entry omits the disputed 1975 date, which Nyst leaves uncertain, and the fact that deaf-deaf marriages still occur — no overclaim.
- "family transmission is the minority route (S091)" — p. 33 (5% figure) plus p. 28 ("Typically, deaf people in Adamorobe live in hearing families … expected for a recessive genotype").
- Bengkala cells (S092): recessive gene ≥7 generations, ~1,200 hearing signers, InSL-shift and marriage-pattern threats — all verbatim on the deposit page at the anchored sections. The entry attaches "≥7 generations" to the gene (not to signing generations, which the deposit caps at "at least 5") — correctly scoped. Terminology (Kata Kolok = language, Bengkala = village) matches the deposit's own note.
- Martha's Vineyard cells (S093): case label and "grew up signing together" are exactly what the description ¶1–¶2 state; no uncited figure imported.
- Drift checks: no gene name, no clinical guidance ("recessive gene" only as the deposit's attested label); Milan row carries `(to-verify)` (code T, `calibration-registry.md:39`) and "history, not law"; no education-policy or rights ruling; levers are design dials under a NON-CANON entry. §4 cites only S091–S093; no S123/S124, no round lesson, no D-side path.

## Verdict

**HOLDS-WITH-FIXES.** Every numeric and attested cell in §4 checks out against the re-opened S091–S093 at their anchors. The two medium findings are scope defects (entry paraphrase drift on `:76`; S091 registry scope vs the general 5%-figure use), each fixable by a one-line rewording / superseding row; three low findings are registry-anchor and housekeeping nits.

## Unrun checks

- The JS-rendered live HUP page beyond the WAF (202/empty body via curl; not needed — the row cites the Wayback capture, which I read).
- Non-§4 sections of the C entry and SOURCES rows outside S091–S093 (out of this seat's scope).
