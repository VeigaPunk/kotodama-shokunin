# ScoutWelshStandard — round 58, claim C source item (Welsh standardised place-names)

Seat: KotodamaR58A2.ScoutWelshStandard. S-ids: S522, S523. Both rows pass all four rowcheck legs. Both URLs: `grep -F welshlanguagecommissioner corpus/SOURCES.md` → 0 lines (neither host nor path already registered). All fetches: plain `curl -sL`, HTTP 200, no access control.

## Rows

| S522 | Welsh Language Commissioner (Comisiynydd y Gymraeg), n.d. (live 2026-10-23), Standardisation of Welsh place-names — https://www.welshlanguagecommissioner.wales/policy-and-research/standardisation-of-welsh-place-names (direct, HTTP 200) | docs | A | who standardises Welsh place-names and what the panel weighs | section The Place-names Standardisation Panel's work: "In forming its recommendations, the panel also gives consideration to the meaning, history and etymology of the place-names, as well as their current usage." | The Welsh standardisation panel weighs what a place-name means, its history and its etymology together with how people use it today. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |
| S523 | Welsh Language Commissioner (Comisiynydd y Gymraeg), 2025, Guidelines for Standardising Place-names in Wales (publication date 28/02/2025) — https://www.welshlanguagecommissioner.wales/media/twgbcoaa/20250228-dg-s-guidelines-for-standardising.pdf (direct, HTTP 200) | docs | A | Welsh generic elements in lake names and tautological topographical names | p. 5, §13 Tautological topographical names: "Llyn is commonly omitted at the beginning of other lake names (Glaslyn, Gloywlyn)." | In Welsh lake names the generic word llyn is commonly left off the front when the name already contains it, as in Glaslyn. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |

The locators have no double quotes on purpose: rowcheck treats the first double-quoted span as the quote, and an earlier draft that put the section titles in quotes failed LOCATE with "quote under 8 words".

## Gate lines

- S522 — https://www.welshlanguagecommissioner.wales/policy-and-research/standardisation-of-welsh-place-names — accessed 2026-10-23 — section The Place-names Standardisation Panel's work: “In forming its recommendations, the panel also gives consideration to the meaning, history and etymology of the place-names, as well as their current usage.” Grounds: The Welsh standardisation panel weighs what a place-name means, its history and its etymology together with how people use it today. Seat: ScoutWelshStandard.
- S523 — https://www.welshlanguagecommissioner.wales/media/twgbcoaa/20250228-dg-s-guidelines-for-standardising.pdf — accessed 2026-10-23 — p. 5, §13 Tautological topographical names: “Llyn is commonly omitted at the beginning of other lake names (Glaslyn, Gloywlyn).” Grounds: In Welsh lake names the generic word llyn is commonly left off the front when the name already contains it, as in Glaslyn. Seat: ScoutWelshStandard.

## rowcheck output

`cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && timeout 900 python3 -B reports/round-58/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r58/ScoutWelshStandard/rows.md` (exit 0):

```
S522 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.welshlanguagecommissioner.wales/policy-and-research/standardisation-of-welsh-place-names | BOILER: root-clear https://www.welshlanguagecommissioner.wales/; not a title, h1 or meta label | RELEVANCE: shared=['etymo', 'histo', 'name', 'panel', 'place'] | TOPIC: quote_hits=2 function_words=8 page_hits=54 page_terms=53 need=1/2/3/2
S523 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.welshlanguagecommissioner.wales/media/twgbcoaa/20250228-dg-s-guidelines-for-standardising.pdf | BOILER: root-clear https://www.welshlanguagecommissioner.wales/; not a title, h1 or meta label | RELEVANCE: shared=['commo', 'glasl', 'lake', 'llyn', 'name'] | TOPIC: quote_hits=1 function_words=4 page_hits=39 page_terms=31 need=1/2/3/2
```

Legs (c) and (d) of RELEVANCE were not run, because they need `--entry` and the entry doesn't exist yet. The L1 should re-run with `--entry corpus/knowledge/linguistics/toponymy-place-names.md` once the sentences have landed.

## draft sentences

S522 (each sentence says only what the opened page says):
- In Wales the standard spelling of a place-name is recommended by the Welsh Language Commissioner's Place-names Standardisation Panel, which weighs the name's meaning, history and etymology alongside its current usage (S522).
- The panel includes academics, a Welsh Government representative and members of the Welsh Place-Name Society, and its chief aim is to interpret, revise and extend the standardisation conventions of A Gazetteer of Welsh Place-Names (1967) (S522).
- Before recommending a form, the panel consults local authorities so that local opinion and knowledge are considered, and it advises Ordnance Survey on the place-name forms used in its mapping products (S522).
- This gives a worldbuilder one model of a naming authority: an expert panel whose stated aims are consistent place-name spelling nationwide and avoiding a multiplication of forms, while it weighs etymology and history against current usage (S522).

S523 (each sentence says only what the opened PDF says):
- Welsh lake names show the generic element merging into the specific: llyn is commonly omitted at the beginning of lake names such as Glaslyn and Gloywlyn, where the name already contains it (S523).
- The Commissioner's guidelines treat names such as Llyn Dulyn and Llyn Cwellyn, which repeat the lake element, as tautological, and allow the descriptive noun llyn before such names where that is the most common form (S523).
- Keeping the generic word can also tell apart two features that share one basic name, as with Llyn Hiraethlyn and Afon Hiraethlyn (S523).
- The same guidelines say to avoid pedantic or revived antiquarian forms and literal or whimsical translations unless they are in common use, but they allow logical coinages from established names, such as Dwyrain Aberddawan for East Aberthaw (S523).

Other material in the same S523 PDF that the L1 may use in S523 sentences (all opened and read; not separate rows, because one URL is one row):
- §4: settlement names are written as one word (Nantperis) to tell them apart from the topographical feature they are named from (Nant Peris).
- §5: Welsh adaptations of personal names are common (Treforys/Morriston).
- §7: dialect and local evidence count, but standard orthography is preferred because "place-names belong to the whole of Wales".
- §8: where the Welsh and English forms differ by only one or two letters, a single Welsh form is preferred, but established pairs such as Biwmares/Beaumaris and Wrecsam/Wrexham are recognised.
- §9: the definite article can be part of a name (Y Bala). The panel keeps it when in doubt, to guide mutation (i'r Bala, not i Fala).
- Scope: the guidelines cover settlement names (villages, towns, cities) and topographical features (lakes, rivers, mountains).

Notes for the reviewer: the S523 quote is prose under §13, not a numbered sub-item. The words "other lake names" refer back to the section's tautology examples (Llyn Dulyn, Llyn Cwellyn), which supports "already contains it". The S522 quote is body prose. The page also carries the advisory-service history: bilingual road signs after 1960s campaigns, then the Welsh Office, the Welsh Language Board, and the Commissioner from 2012.

## rejected

- https://www.welshlanguagecommissioner.wales/public/place-names — HTTP 404 (a guessed path; not used).
- https://www.welshlanguagecommissioner.wales/public/place-names/list-of-standardised-welsh-place-names — HTTP 404 (a guessed path; not used).
- https://www.welshlanguagecommissioner.wales/ — the site root, used only to find links (it is BOILER's ROOT page). Not a source.
- https://www.welshlanguagecommissioner.wales/standard-welsh-place-names — the list portal itself: a search form and filters with no body prose to quote. The list is reachable but this page has no claim sentence.
- https://www.welshlanguagecommissioner.wales/policy-and-research/standardisation-of-welsh-place-names/technical-guidance — HTTP 200 and relevant (naming new developments from the List of Historic Place Names; signs must give the radical, unlenited form, e.g. Caernarfon, not Gaernarfon after "Croeso i"). Not offered because the assignment caps this seat at 2 rows and the two above cover the brief (the authority and its principles) better. Not run through rowcheck. The most quotable sentences either exceed 25 words or lack a NAMING-PLACE window inside the quote, judged by hand from the rowcheck stem sets.
- https://www.welshlanguagecommissioner.wales/policy-and-research/standardisation-of-welsh-place-names/standardisation-projects — HTTP 200 (Eryri lake-name pilot 2023, Cadw monuments). Not offered because of the 2-row cap, and it is thin (197 words).
- https://www.welshlanguagecommissioner.wales/policy-and-research/standardisation-of-welsh-place-names/international-place-names — HTTP 200 (Welsh exonyms for countries, made jointly with the Welsh Government Translation Service, following the FCDO Geographical Names Index). Not offered because of the 2-row cap. It is a possible exonym row for another seat if one is free.

## installs

none (used the existing `curl`, `pdftotext` and `python3`; rowcheck's own `uv run --with pypdf==5.4.0` ran as written in the instrument).
