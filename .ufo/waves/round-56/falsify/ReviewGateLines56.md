# ReviewGateLines56 — mechanical check of round-56 Gate lines

Seat: KotodamaR56.ReviewGateLines56 (leaf seat, read-only lane; no subagents).
Scope: `corpus/lessons/round-56.md` `## Gate` lines vs `corpus/SOURCES.md` rows S359–S412 (claims C and O as landed).
Tools used: python3 standard library only (no installs performed or needed). Independent checker written at scratch `/fast/scratch/hyaku/kotodama-r56-falsify/ReviewGateLines56/check_gate.py` plus `row_details.py` / `row_lines.py`; official checker run as installed.

## Verdict

CARRIED — all 54 Gate lines pass every mechanical check. The claim-O checker prints 0 findings. No mismatches, no defects, no fix proposed.

## Method

For every `- S### ` line in the Gate section (physical lines 24–77 of round-56.md) I compared, with my own Python:

1. Grounds text vs the row's teaches cell (SOURCES column 7): byte for byte;
2. every URL in the line vs the row's source cell (column 2): verbatim equality;
3. every quoted span (straight, curly, guillemet pairs): at most 25 words and its inner text occurring verbatim in the row's anchor cell (column 6);
4. HTML character references: none in any Gate line.

I also ran the official checker: `python3 -B tools/check-gate-quotes.py corpus/lessons/round-56.md` printed `GATE_QUOTES: 0 findings` and exited 0.

## Checked items (one line per row)

Grounds relation notation: "grounds == teaches" means byte-for-byte equality up to the sentence-final period, which the Gate line consumes in `. Seat:` while the registry cell carries it; all 54 rows are identical in every other character (54/54), matching the lane's canonical comparison in the checker (which strips trailing periods).

- S359 (round-56.md:24) — CARRIED — grounds == teaches; 1 span, 18 words, verbatim in anchor; URLs in source cell. Span: "os ditos mercadores leuam cada dia nossos naturaes, filhos da terra e filhos de nossos fidallgos e vassallos".
- S360 (round-56.md:25) — CARRIED — grounds == teaches; 1 span, 16 words, verbatim in anchor; URLs in source cell. Span: "com mercadores desrespeitando as rotas estabelecidas e o monopólio real, Afonso I escreveu ao rei português".
- S361 (round-56.md:26) — CARRIED — grounds == teaches; 1 span, 18 words, verbatim in anchor; URLs in source cell. Span: "Some rules for the more easy understanding of the most difficult idiom of the people of the Congo".
- S362 (round-56.md:27) — CARRIED — grounds == teaches; 1 span, 17 words, verbatim in anchor; URLs in source cell. Span: "simba appears as ximba under X in the Dictionary, and as simba under S in the Appendix".
- S363 (round-56.md:28) — CARRIED — grounds == teaches; 1 span, 14 words, verbatim in anchor; URLs in source cell (including the page-level OCR parenthetical). Span: "In 1659 the Propaganda at Rome published a Congo Grammar of the same author".
- S364 (round-56.md:29) — CARRIED — grounds == teaches; 1 span, 11 words, verbatim in anchor; URLs in source cell (including the openedition.org full-text auxiliary). Span: "posição consolidada com o estabelecimento do domínio colonial oficial em 1888".
- S365 (round-56.md:30) — CARRIED — grounds == teaches; 1 span, 15 words, verbatim in anchor; URLs in source cell. Span: "c'est la suppression de l'institution royale par les Portugais en 1914, après la conquête coloniale".
- S366 (round-56.md:31) — CARRIED — grounds == teaches; 1 span, 14 words, verbatim in anchor; URLs in source cell. Span: "o cargo de rei do Congo passou a ser, oficialmente, a de juiz popular".
- S367 (round-56.md:32) — CARRIED — grounds == teaches; 1 span, 16 words, verbatim in anchor; URLs in source cell. Span: "Com a colonização de Angola – oficialmente desde 1885 – desenha-se outro mapa da sociedade kôngo".
- S368 (round-56.md:33) — CARRIED — grounds == teaches; 1 span, 15 words, verbatim in anchor; URLs in source cell. Span: "The Berlin Conference essentially consisted of a series of negotiations starting on 15 November 1884".
- S369 (round-56.md:34) — CARRIED — grounds == teaches; 1 span, 10 words, verbatim in anchor; URLs in source cell. Span: "The sign is thus the tip of a philosophical iceberg".
- S370 (round-56.md:35) — CARRIED — grounds == teaches; 1 span, 17 words, verbatim in anchor; URLs in source cell. Span: "There is no direct, unambiguous evidence for their conclusion, and there never will be in all likelihood."
- S371 (round-56.md:36) — CARRIED — grounds == teaches; 1 span, 12 words, verbatim in anchor; URLs in source cell (including image-check auxiliaries). Span: "dom Affonso por sua graça, Rei de Manicongo, e senhor dos Ambudos".
- S372 (round-56.md:37) — CARRIED — grounds == teaches; 1 span, 1 word, verbatim in anchor; URLs in source cell. Span: "1482-1483".
- S373 (round-56.md:38) — CARRIED — grounds == teaches; 1 span, 23 words, verbatim in anchor; URLs in source cell. Span: "Ielala rocks, situated on the left bank of the Zaire River, close to the Ielala Falls, approximately 150 km from the river's mouth".
- S374 (round-56.md:39) — CARRIED — grounds == teaches; 1 span, 16 words, verbatim in anchor; URLs in source cell. Span: "De nouo traduzida na lingoa do Reyno de Congo, por ordem do P. Mattheus Cardoso Theologo".
- S375 (round-56.md:40) — CARRIED — grounds == teaches; 1 span, 16 words, verbatim in anchor; URLs in source cell. Span: "an interlinear Portuguese–Kikongo catechism from 1624 translated under the leadership of the Portuguese Jesuit Mateus Cardoso".
- S376 (round-56.md:41) — CARRIED — grounds == teaches; 1 span, 10 words, verbatim in anchor; URLs in source cell. Span: "kanda means 'group or category,' as in makanda ma nza".
- S377 (round-56.md:42) — CARRIED — grounds == teaches; 1 span, 16 words, verbatim in anchor; URLs in source cell. Span: "A Kanda é o grupo de parentesco organizado em linha materna, descendente de uma antepassada comum."
- S378 (round-56.md:43) — CARRIED — grounds == teaches; 1 span, 15 words, verbatim in anchor; URLs in source cell. Span: "we term the Kikongo Language Cluster (KLC), a disparate continuum of closely related Bantu languages."
- S379 (round-56.md:44) — CARRIED — grounds == teaches; 1 span, 2 words, verbatim in anchor; URLs in source cell. Span: "level": "family".
- S380 (round-56.md:45) — CARRIED — grounds == teaches; 1 span, 13 words, verbatim in anchor; URLs in source cell. Span: "She said that Jesus Christ was born in São Salvador, which was Bethlehem".
- S381 (round-56.md:46) — CARRIED — grounds == teaches; 1 span, 12 words, verbatim in anchor; URLs in source cell. Span: "Eu sou Santo Antônio, filho primogênito da Fé e de São Francisco".
- S382 (round-56.md:47) — CARRIED — grounds == teaches; 1 span, 20 words, verbatim in anchor; URLs in source cell. Span: "Ces anges se distinguaient des autres parce qu'ils portaient sur la tête une couronne faite de l'écorce de l'arbre ensanda."
- S383 (round-56.md:48) — CARRIED — grounds == teaches; 1 span, 23 words, verbatim in anchor; URLs in source cell. Span: "This article argues that although Christianity in Kongo took a distinctly African form it was widely accepted both in Kongo and in Europe".
- S384 (round-56.md:49) — CARRIED — grounds == teaches; 1 span, 14 words, verbatim in anchor; URLs in source cell. Span: "unfolded in the mpu caps that served as emblems of status in the Kongo".
- S385 (round-56.md:50) — CARRIED — grounds == teaches; 1 span, 15 words, verbatim in anchor; URLs in source cell (including the landing-page auxiliary). Span: "les ethnonymes utilisés dépendaient plus des factoreries sur la côte africaine que des peuples eux-mêmes".
- S386 (round-56.md:51) — CARRIED — grounds == teaches; 1 span, 9 words, verbatim in anchor; URLs in source cell (search endpoint and single-object endpoint). Span: "Dom Miguel de Castro, Ambassadør for herren af Sonho".
- S387 (round-56.md:52) — CARRIED — grounds == teaches; 1 span, 7 words, verbatim in anchor; URLs in source cell. Span: "Antonio Manuel, Marquis of Ne-Vunda, 1629. Marble."
- S388 (round-56.md:53) — CARRIED — grounds == teaches; 1 span, 11 words, verbatim in anchor; URLs in source cell (download and effective content links). Span: "still very little is understood about the origins of the kingdom".
- S389 (round-56.md:54) — CARRIED — grounds == teaches; 1 span, 20 words, verbatim in anchor; URLs in source cell. Span: "With its mbanza or capital towns, which have been described as 'open, scattered garden-cities with a ceremonial and symbolic centre'".
- S390 (round-56.md:55) — CARRIED — grounds == teaches; 2 spans, max 8 words, both verbatim in anchor; URLs in source cell. Spans: "ngangula a Kongo literally means 'blacksmith of Kongo'" and "blacksmith of Kongo" (the Grounds re-quote; also verbatim in anchor).
- S391 (round-56.md:56) — CARRIED — grounds == teaches; 1 span, 12 words, verbatim in anchor; URLs in source cell. Span: "Le 29 octobre 1665, à Ulanga près d'Ambuila, les deux armées s'affrontent."
- S392 (round-56.md:57) — CARRIED — grounds == teaches; 1 span, 24 words, verbatim in anchor; URLs in source cell. Span: "É importante salientar que foi logo de manhã, por volta das 9 horas de 27 de Outubro de 1665, que aconteceu o primeiro confronto."
- S393 (round-56.md:58) — CARRIED — grounds == teaches; 1 span, 13 words, verbatim in anchor; URLs in source cell. Span: "delicately carved ivories and finely woven raffia cloths embellished with abstract geometric patterns".
- S394 (round-56.md:59) — CARRIED — grounds == teaches; 1 span, 17 words, verbatim in anchor; URLs in source cell. Span: "In 1491, the Kongo king Nzinga converted to Christianity, thereby strengthening ties with his counterpart in Portugal."
- S395 (round-56.md:60) — CARRIED — grounds == teaches; 1 span, 8 words, verbatim in anchor; URLs in source cell. Span: "collaborative creations of Kongo sculptors and ritual specialists".
- S396 (round-56.md:61) — CARRIED — grounds == teaches; 1 span, 16 words, verbatim in anchor; URLs in source cell. Span: "This work was the product of an intense collaboration between a sculptor and the initiated priest".
- S397 (round-56.md:62) — CARRIED — grounds == teaches; 1 span, 15 words, verbatim in anchor; URLs in source cell (record and public page). Span: "Zimpu (singular: mpu) are intricately knotted caps worn by men in parts of Central Africa."
- S398 (round-56.md:63) — CARRIED — grounds == teaches; 1 span, 18 words, verbatim in anchor; URLs in source cell (record and public page). Span: "An artist made this crucifix from wood and metal centuries after Catholicism became the Kongo Kingdom's official faith."
- S399 (round-56.md:64) — CARRIED — grounds == teaches; 1 span, 22 words, verbatim in anchor; URLs in source cell. Span: "Uniting symbols of Kongo religious and secular power, this prestige staff was used as an insignia of office by a Kongo chief."
- S400 (round-56.md:65) — CARRIED — grounds == teaches; 1 span, 16 words, verbatim in anchor; URLs in source cell. Span: "Conceived to house specific mystical forces, they were collaborative creations of Kongo sculptors and ritual specialists."
- S401 (round-56.md:66) — CARRIED — grounds == teaches; 1 span, 23 words, verbatim in anchor; URLs in source cell. Span: "Mavungu is a type of nkisi known as a nkondi (plural minkondi), which in the past was inadequately glossed as a 'nail fetish'."
- S402 (round-56.md:67) — CARRIED — grounds == teaches; 1 span, 19 words, verbatim in anchor; URLs in source cell. Span: "This nkisi nkondi (power figure) lacks most of the materials that transformed it into a vessel for a spirit."
- S403 (round-56.md:68) — CARRIED — grounds == teaches; 2 spans, max 23 words, both verbatim in anchor; URLs in source cell. Spans: "In the end, the perception of these objects as 'fetish' is an entirely spurious external view which classifies objects regardless of indigenous understanding." and "fetish" (the Grounds re-quote; also verbatim in anchor).
- S404 (round-56.md:69) — CARRIED — grounds == teaches; 1 span, 15 words, verbatim in anchor; URLs in source cell. Span: "This ifland furniflies the money ufed by the King of Congo and the neighbouring people".
- S405 (round-56.md:70) — CARRIED — grounds == teaches; 1 span, 23 words, verbatim in anchor; URLs in source cell. Span: "nzimbu shells (Olivancillaria nana), collected in the Luanda region to the southwest of the Kongo Kingdom, were used as a means of payment".
- S406 (round-56.md:71) — CARRIED — grounds == teaches; 1 span, 11 words, verbatim in anchor; URLs in source cell. Span: "Si pescano al lido per ordine del Re. Si chiamano Zimbo."
- S407 (round-56.md:72) — CARRIED — grounds == teaches; 1 span, 14 words, verbatim in anchor; URLs in source cell. Span: "In the Kongo Kingdom, the finest textiles were reserved for nobles with high status."
- S408 (round-56.md:73) — CARRIED — grounds == teaches; 1 span, 13 words, verbatim in anchor; URLs in source cell. Span: "Raffia woven cloth with a fringe on three sides. Possibly used as currency."
- S409 (round-56.md:74) — CARRIED — grounds == teaches; 1 span, 25 words, verbatim in anchor; URLs in source cell. Span: "with a knife they cut the cloth in the proper spots and rub it well with their hands, so that it looks like patterned velvet" (exactly at the 25-word cap, not over).
- S410 (round-56.md:75) — CARRIED — grounds == teaches; 1 span, 11 words, verbatim in anchor; URLs in source cell. Span: "traditions of origin in Kongo changed much more substantially over time."
- S411 (round-56.md:76) — CARRIED — grounds == teaches; 1 span, 19 words, verbatim in anchor; URLs in source cell. Span: "one of the largest constituted states of Southern Africa, which was active from the 14th to the 19th century".
- S412 (round-56.md:77) — CARRIED — grounds == teaches; 1 span, 11 words, verbatim in anchor; URLs in source cell. Span: "at this time it was already known as Kulumbimbi, from Nkulu".

## Tool-level checks

- `python3 -B tools/check-gate-quotes.py corpus/lessons/round-56.md` — CARRIED — printed `GATE_QUOTES: 0 findings`, exit 0.
- Independent checker — CARRIED — 54 rows parsed; relation counts: 54/54 grounds == teaches (sole difference the sentence-final period convention); max span words 25 (S409); max run words 25; every quoted span verbatim in its anchor cell; every URL (primary and auxiliary) verbatim in its source cell; zero HTML character reference pattern hits in any Gate line.
- Row coverage — CARRIED — the Gate section holds exactly S359–S412 once each, contiguous, and each has exactly one 13-cell SOURCES row (no missing, duplicate, or extra row).

## Whole-file note (not a Gate finding)

The only HTML character references in round-56.md sit outside the Gate section, in the round-55 errata and routed-fixes lines (physical lines 96–113 and 122–123), where the records commit literally quotes the old round-55 defects that claim O turns into failing checks. Those are not Gate rows; the mechanical Gate check remains clean. No action.

## Unrun checks

Live re-verification of each quote against the cited pages (URL reachability, OCR fidelity, source-wording truth) is out of this seat's assignment, which is the lesson-vs-registry mechanical check; those checks are covered by the other falsify reviewers. Nothing else from the assignment was left unrun.

## Conclusion

Claim C's Gate rows and claim O's Gate-line instrument both hold under the mechanical check: every Grounds is its row's whole teaches cell, every URL matches, every quoted span is at or under 25 words and sits verbatim in its row's anchor cell, and no Gate line carries an HTML character reference. Verdict: CARRIED, no fixes needed.
