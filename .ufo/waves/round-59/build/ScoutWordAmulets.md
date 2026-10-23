# ScoutWordAmulets — claim C source seat (S638, S639)

Subtopic: words and letters as protection — written amulets, inscribed names, magic squares.
Two rows offered, both opened this session by ordinary GETs. No installs, no updates.

Scratch: /fast/scratch/hyaku/kotodama-r59/ScoutWordAmulets/ (rows.md, stub.md, fetches, rowcheck output).

## 1. Registry rows (exactly 11 cells each)

| S638 | Urbanová, Havel, Mutlová, Knauber, Schellner and Gorczyca 2021, "Christian textual amulet on a lead sheet from Rękawczyn in Greater Poland Province", Sprawozdania Archeologiczne 73/2, 339-364, CC BY-NC-ND, DOI 10.23858/sa/73.2021.2.2498 — https://journals.iaepan.pl/sa/article/download/2498/2871 (direct, HTTP 200, 9,410,020 bytes, application/pdf); capture https://web.archive.org/web/20220103013529id_/https://journals.iaepan.pl/sa/article/download/2498/2871 | paper | A | one fourteenth-century lead amulet, its inscription and its making: a long Gospel of John quotation followed by an apotropaic formula with magical words, compared with German and Bohemian lead amulets and attributed to monks and educated clerics | p. 350 (PDF p. 12), on comparable finds: "Other amulets do not cite the Gospels but use an apotropaic adjuration formula by which they banish evil spirits and diseases." | A written amulet can work by adjuration alone, its formula ordering evil spirits and diseases away instead of quoting scripture. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |
| S639 | Victoria and Albert Museum, London, "Amulet" (silver magic-square amulet), accession 87-1873, Lebanon, 1860-1870, sheet silver engraved with Arabic characters; record created 8 April 2003. — https://collections.vam.ac.uk/item/O79669/ (direct, HTTP 200, 47,443 bytes) | docs | A | what one magic-square amulet is and how the museum reads it: sheet silver divided into 25 squares of single Arabic characters, a suspension hole in the top edge, and the claim that a magic square's potency lies in its arrangement and hidden meanings | Summary: "Amulets, which were believed to protect the owner against harm of all kind, were widely worn in the Islamic world." | Amulets worn across the Islamic world were expected to protect their owner from harm of every kind, and they took many forms. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |

## 2. Gate lines

- S638 — https://journals.iaepan.pl/sa/article/download/2498/2871 — accessed 2026-10-23 — p. 350, on comparable finds: "Other amulets do not cite the Gospels but use an apotropaic adjuration formula by which they banish evil spirits and diseases.". Grounds: A written amulet can work by adjuration alone, its formula ordering evil spirits and diseases away instead of quoting scripture. Seat: ScoutWordAmulets.
- S639 — https://collections.vam.ac.uk/item/O79669/ — accessed 2026-10-23 — Summary: "Amulets, which were believed to protect the owner against harm of all kind, were widely worn in the Islamic world.". Grounds: Amulets worn across the Islamic world were expected to protect their owner from harm of every kind, and they took many forms. Seat: ScoutWordAmulets.

## 3. rowcheck output (verbatim)

Command: `cd /fast/scratch/hyaku/kotodama-r59/ScoutWordAmulets && timeout 900 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-59/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r59/ScoutWordAmulets/rows.md --entry /fast/scratch/hyaku/kotodama-r59/ScoutWordAmulets/stub.md`

```
S638 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://journals.iaepan.pl/sa/article/download/2498/2871 | BOILER: root-clear https://journals.iaepan.pl/; not a title, h1 or meta label | RELEVANCE: shared=['adjur', 'amule', 'disea', 'evil', 'formu', 'spiri'] | TOPIC: quote_hits=2 function_words=5 page_hits=201 page_terms=183 need=1/2/3/2
S639 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://collections.vam.ac.uk/item/O79669/ | BOILER: root-clear https://collections.vam.ac.uk/; not a title, h1 or meta label | RELEVANCE: shared=['amule', 'harm', 'islam', 'kind', 'owner', 'prote'] | TOPIC: quote_hits=1 function_words=6 page_hits=13 page_terms=11 need=1/2/3/2
```

Margins: S638 page 201 windows / 183 terms; S639 page 13 / 11 (needs 3 / 2).

## 4. Draft entry sentences

```
## Words as the working part

A protective object may be a text before it is a thing: a folded lead sheet, worn at the neck or sewn into cloth, carries a Gospel quotation followed by an apotropaic formula of magical words (S638). Where a Gospel quotation is missing, an inscribed adjuration orders evil spirits and diseases to depart instead (S638). Comparable lead amulets from Germany and Bohemia were attributed to monks, and textual amulets were made by educated clerics for a client's stated wish (S638).

A protective grid can be made of sheet silver divided into twenty-five squares, each containing a single Arabic character (S639). A hole drilled through the top edge is for suspension, and amulets of this kind were widely worn on the body (S639). The square's potency is credited to its arrangement, whose letters and numbers form words or phrases with hidden meanings (S639).
```

What each sentence drags from the opened page, for the L1's checking:
- lead sheet / Gospel quotation + apotropaic formula with magical words: S638 abstract (p. 339) and p. 350 ("The amulet was supposed to protect a certain Herwihin"; the text contains "a long quotation from the Gospel of John followed by an apotropaic formula with magical words").
- folded and worn: S638 p. 347 ("the amulet was rolled up or folded and could be worn around the neck or put into a piece of cloth and worn close to the body"); the Rękawczyn tablet itself was "folded in half along the longer axis and then into four" (p. 346).
- names worn on the body: S638 p. 350 ("followed by the names of other Christian entities: Jesus Christus, Maria mater, and the names of the Four Evangelists") — available if the L1 wants an "inscribed names" sentence; it is on the same page, so it can cite S638 too.
- monks / educated clerics: S638 p. 344 ("Manufacture of similar amulets has been attributed mainly to monks") and p. 346 ("Textual amulets were obviously made prevalently by well-educated clerics according to the believers' wishes").
- silver grid of 25 squares / Arabic characters / suspension hole / arrangement and hidden meanings: S639 physical description and Summary.
- S638's own page also lists what such inscriptions carried (p. 347: "incantations, prayers, divine names, passages of the Scripture, historiolae, and magical signs and symbols") — useful if the entry needs the full repertoire rather than one formula.

## 5. rejected (opened this session, not offered)

- Metropolitan Museum object page https://www.metmuseum.org/art/collection/search/452894 — `429 34219` (curl `%{http_code} %{size_download}`); the search page https://www.metmuseum.org/art/collection/search?q=talismanic+scroll — `429 34224`. Bot protection; no capture may be listed for a page that could not be opened live.
- Met Collection API v1 search — `410 438` with body `{"message":"/public/collection/v1/search was retired on 2026-10-01. It was backed by Solr and returned every matching object ID in one response; use /public/collection/v1.1/search, ..."}`. v1.1 answers `200 167` with object IDs only, no text to vouch for a quote.
- Wellcome Collection work page https://wellcomecollection.org/works/cw8xxzu9 — `405 2131` with `<title>Human Verification`; search page `405 2131` likewise. Access control; not used.
- Smithsonian National Museum of African Art https://africa.si.edu/collection-item/?q=amulet — `403 46530`, `<title>Smithsonian request verification`.
- British Museum collection search https://www.britishmuseum.org/collection/search?keyword=amulet — `403 5640`.
- Penn Museum https://www.penn.museum/collections/search.php?search=amulet — `403 961`.
- Museum of Fine Arts, Boston https://collections.mfa.org/search/objects/*/abracadabra — `202 0`.
- Art Institute of Chicago API — empty response body: `json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)` for q=magic%20scroll, q=talisman, q=abracadabra.
- Yale University Art Gallery https://artgallery.yale.edu/collections/search?search_api_fulltext=amulet — `403 5741`, `<title>Just a moment...`; Princeton https://artmuseum.princeton.edu/search/objects?search=amulet — `403 5673`, same challenge.
- Museum of Witchcraft and Magic, object 1583 "Charm: Talisman SATOR square" https://museumofwitchcraftandmagic.co.uk/object/charm-talisman/ — `503 3571` on two attempts.
- Khalili Collections talismanic shirts, four records (TXT 545, TXT 574, TXT 463, TXT 471) — `200` each (100,028 / 95,222 / 94,753 / 103,229 bytes) but the extracted text carries only 5 CHARM-GUARD windows per page, all in the navigation menu ("All Collections"), and the curatorial "Other Notes" makes no protective claim beyond "covered with Qur'anic verses, prayers and invocations to God"; no quotable protective sentence for a row.
- Cleveland Museum of Art, "Necklace (ashän ketab) with amulet pendants (tälsäm)", 2025.152 — https://clevelandart.org/art/2025.152, `200 84820`, but only 2,093 characters of text and no protection claim beyond the object name; nothing to quote.
- Martor 28 (2023), Hajnalka Tamás, review essay "Magical Objects, Magical Writing: Amulets Across the Ages" — http://martor.muzeultaranuluiroman.ro/wp-content/uploads/2023/11/Martor-28_18_Tamas.pdf, `200 1027067`, strong text (79 windows, 64 discipline terms), but it is a review of an edited volume, so every claim is second-hand, and only two S-ids were assigned; recorded as the best unused alternate.
- University of Kent, Hetty Taylor, "Place, period and purpose: migration(s) of the SATOR AREPO formula" — https://research.kent.ac.uk/material-studies-network/place-period-and-purpose-migrations-of-the-sator-arepo-formula-by-hetty-taylor/, `200 91765`; it PASSED all four legs with the quote "there is evidence that the sator square, in textual amulet form, was being adapted into a ritual to address social, rather than medical concerns" (`S639 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | ... TOPIC: quote_hits=1 function_words=7 page_hits=4 page_terms=15 need=1/2/3/2`) but was not offered: the second row went to the V&A record (museum curatorial text, wider TOPIC margin, and it carries the material/placement/arrangement points the entry needs). If the L1 wants an explicit SATOR-square row from the unused block, this row is ready to register as-is; its page margins are thin (4 windows), and its only Wayback captures carry no body text (`200 23128`, zero occurrences of "sator"), so it should be listed live-only.
- Word Ways 13(1) 1980, "The Sator Square Revisited" — https://digitalcommons.butler.edu/wordways/vol13/iss1/5/ `200 57029`, landing page is metadata only (0 windows, 0 discipline terms); the article body is a separate `viewcontent.cgi` PDF that I did not open.
- Sprawozdania Archeologiczne landing page for the same article https://journals.iaepan.pl/sa/article/view/2498 — `200 113995`; not used as the row URL because the anchor sentence sits in the article body, not on the landing page; the PDF URL locates it.
- V&A Collections API (api.vam.ac.uk) and Cleveland open-access API responses — used only to find object numbers; not vouchable pages.

## 6. Notes and risks

- Both rows list the live URL first; only S638 adds one Wayback capture, and that capture is of the same page (`/sa/article/download/2498/2871`), byte-identical (9,410,020 bytes) and verified to locate the anchor quote.
- Reserved hosts: none used. Hosts: journals.iaepan.pl, collections.vam.ac.uk — two distinct hosts, both new URLs (checked with `grep -F` against corpus/SOURCES.md).
- Neither row overgeneralises: S638 speaks of one find and its comparanda in Germany and Bohemia; S639 of one Lebanese object and the V&A's own reading, with "in the Islamic world" kept inside the quote.
- The entry is not written by this seat; corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md does not exist yet.
- Tooling: no installs or updates.
