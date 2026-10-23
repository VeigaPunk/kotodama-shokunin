# ScoutUNGEGNGlossary — round 58, claim C source seat (S500, S501)

I offer two rows from two separate UNGEGN documents on unstats.un.org. Both print LOCATE, BOILER, RELEVANCE and TOPIC PASS, and neither URL is in `corpus/SOURCES.md` (`grep -c -F` gave 0 for `unstats.un.org` and for `Glossary_of_terms`).

- **S500**, the UNGEGN Glossary: the definition of the specific element, which covers the "what a name is built from" decision.
- **S501**, the UNGEGN Toponymy Training Manual, Chapter 1: the creation of the first national names authority in 1890, which covers the "who standardises names" decision.

The Glossary also defines endonym, exonym, generic element and toponym. I used only one of its definitions because every Glossary URL serves the same publication, and two quotes from one page make one row. The alternate quotes from it are listed at the end.

## Rows

| S500 | United Nations Group of Experts on Geographical Names (UNGEGN), UN Statistics Division, 2002 (with Addendum ST/ESA/STAT/SER.M/85/Add.1, 2007), Glossary of Terms for the Standardization of Geographical Names, ST/ESA/STAT/SER.M/85, ISBN 92-1-061192-6 — https://unstats.un.org/unsd/geoinfo/ungegn/docs/pubs/Glossary_of_terms_rev.pdf (direct, HTTP 200) | docs | A | the UN standard definition of a place name's specific element as against its generic term | English glossary, entry 307 (specific element), PDF page 29: "The part of a toponym that does not constitute a generic term and that distinguishes it from others of the same feature class." | A place name's specific element is every part that is not the generic term, and it tells one feature apart from others of its class. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |
| S501 | Kerfoot, Helen, n.d. (chapter undated; its latest dated material is 2015), "Geographical names, their standardization, and their value as part of geospatial data infrastructures", Chapter 1 of the UNGEGN Toponymy Training Manual, UN Statistics Division — https://unstats.un.org/unsd/geoinfo/UNGEGN/docs/CHAPTER%201.pdf (direct, HTTP 200) | docs | A | when and by whose act the first national geographical names authority was created | Chapter 1, §1.3 (Guardians of a country's toponymy), p. 1-2: "In 1890, the United States Board on Geographic Names (US BGN) was created by Executive Order of the President, Benjamin Harrison." | In 1890 the United States created its Board on Geographic Names through an executive order of President Benjamin Harrison. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |

Note for the L1: the locator cells contain no double quotes. The first draft had the entry label in quotes, and rowcheck took that label as the quote and failed every leg. If you add a label in quotes when you integrate, the row will fail again.

## Gate lines

- S500 — https://unstats.un.org/unsd/geoinfo/ungegn/docs/pubs/Glossary_of_terms_rev.pdf — accessed 2026-10-23 — English glossary, entry 307 (specific element), PDF page 29: “The part of a toponym that does not constitute a generic term and that distinguishes it from others of the same feature class.” Grounds: A place name's specific element is every part that is not the generic term, and it tells one feature apart from others of its class. Seat: ScoutUNGEGNGlossary.
- S501 — https://unstats.un.org/unsd/geoinfo/UNGEGN/docs/CHAPTER%201.pdf — accessed 2026-10-23 — Chapter 1, §1.3 (Guardians of a country's toponymy), p. 1-2: “In 1890, the United States Board on Geographic Names (US BGN) was created by Executive Order of the President, Benjamin Harrison.” Grounds: In 1890 the United States created its Board on Geographic Names through an executive order of President Benjamin Harrison. Seat: ScoutUNGEGNGlossary.

## rowcheck output

`cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && timeout 900 python3 -B reports/round-58/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r58/ScoutUNGEGNGlossary/rows.md` (exit 0):

```
S500 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://unstats.un.org/unsd/geoinfo/ungegn/docs/pubs/Glossary_of_terms_rev.pdf | BOILER: root-clear https://unstats.un.org/; not a title, h1 or meta label | RELEVANCE: shared=['clas', 'featu', 'gener', 'term'] | TOPIC: quote_hits=1 function_words=6 page_hits=990 page_terms=743 need=1/2/3/2
S501 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://unstats.un.org/unsd/geoinfo/UNGEGN/docs/CHAPTER%201.pdf | BOILER: root-clear https://unstats.un.org/; not a title, h1 or meta label | RELEVANCE: shared=['1890', 'benja', 'board', 'creat', 'execu', 'geogr'] | TOPIC: quote_hits=1 function_words=6 page_hits=121 page_terms=100 need=1/2/3/2
```

## Draft sentences

S500:
- In the UN's standard vocabulary, the specific element is the part of a toponym that is not the generic term; it distinguishes one feature from others of the same class (S500).
- A built name therefore has two parts: a generic term that the specific element is not, and a specific element that tells this feature apart from the others of its feature class (S500).
- The Glossary's examples of the specific element are Port Elizabeth, Rio Negro and Cape of Good Hope. It adds that the part that is not the generic term may include an article or other linguistic elements (S500).

S501:
- Standing national naming authorities came late. The first was the United States Board on Geographic Names, created in 1890 by an executive order of President Benjamin Harrison (S501).
- After the Board on Geographic Names was created by executive order in 1890, its decisions became binding on all departments and agencies of the federal government (S501).

Page support for the S501 sentences: p. 1-2 says that it was not until the late nineteenth century that any country set up a national authority, that the first country to do so was the United States, and that the Board's decisions became binding on all federal departments and agencies.

## Alternate quotes from the same Glossary URL (one row only, not offered; checked by hand, rowcheck not run)

The L1 may want one of these instead of the entry-307 quote for S500. Each holds a naming-place window by the PLACE and NAMING stem sets in rowcheck.py.

- Entry 076 (endonym): "Name of a geographical feature in one of the languages occurring in that area where the feature is situated." This is 19 words, and the window is `name` to `geographical` at distance 3.
- Entry 081 (exonym): "The officially romanized endonym Moskva for Москва is not an exonym, nor is the Pinyin form Beijing, while Peking is an exonym." This is 22 words, and `endonym` and `exonym` sit in both stem sets. It is a full sentence showing that an official romanization is not an exonym but an outsider's form is. This point may overlap with ScoutPinyinUN.
- Not usable: the exonym definition clause ("Name used in a specific language for a geographical feature situated outside the area…") has no window within 3 words. The generic-element sentences (entries 110, 111 and 112) also have no window, because `feature`, `topographic` and `item` are not PLACE stems.

## rejected

- https://unstats.un.org/unsd/geoinfo/ungegn/docs/pubs/glossary.pdf (HTTP 200, 2,180,714 bytes): the same 2002 Glossary, ST/ESA/STAT/SER.M/85, without the 2007 addendum. A second row from it would be two quotes from one publication counted as two rows.
- https://unstats.un.org/unsd/ungegn/pubs/documents/Glossary_of_terms_rev.pdf (HTTP 200, 3,537,984 bytes): the same file as the S500 URL (same byte size), at a second path. It is a duplicate.
- https://unstats.un.org/unsd/ungegn/pubs/ (HTTP 200): the UNGEGN publications index, a list of links with no body text about place names. I used it only to find the Training Manual.
- https://unstats.un.org/unsd/geoinfo/UNGEGN/Training_Manual_by_chapter.html (HTTP 200, 14,939 bytes): the Training Manual's chapter index, which is navigation and chapter titles only. I used it to find Chapter 1.

Other Chapter 1 sentences I considered but did not offer:
- §1.3, explorers "using the naming process as a way of claiming sovereignty": `naming` is 4 words from `lands`, so the window fails.
- §1.7, the World Bank street-naming procedure: overlaps ScoutStreetNaming.
- §1.8, romanization: overlaps ScoutPinyinUN.
- §1.9, "farm and field names": the clause is a fragment.

installs: none. pypdf 5.4.0 was run through `uv run --with`, the same ephemeral environment that reopen-quote.py uses; nothing was installed persistently.
