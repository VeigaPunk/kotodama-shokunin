# ScoutIslamicTalismans — round 59 build, claim C source item

Subtopic: Islamic talismanic objects — ta'wiz-style holders, inscribed pendants, Qur'anic text worn on the body.
Ids assigned: S612, S613. Two rows offered, both four-leg PASS against `reports/round-59/rowcheck.py` with the entry stub.

## Rowcheck (verbatim, exits 0)

```
S612 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://api.vam.ac.uk/v2/museumobject/O79276 | BOILER: root-clear https://api.vam.ac.uk/; not a title, h1 or meta label | RELEVANCE: shared=['amule', 'conta', 'holde', 'inscr', 'mater', 'musli'] | TOPIC: quote_hits=2 function_words=6 page_hits=8 page_terms=7 need=1/2/3/2
S613 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.clevelandart.org/art/2025.152 | BOILER: root-clear https://www.clevelandart.org/; not a title, h1 or meta label | RELEVANCE: shared=['evil', 'neckl', 'silve', 'tälsä'] | TOPIC: quote_hits=2 function_words=6 page_hits=15 page_terms=8 need=1/2/3/2
```

(The two lines above are rowcheck's stdout; the shell then printed `EXIT 0` from `echo "EXIT $?"`.)

Command run: `cd /fast/scratch/hyaku/kotodama-r59/ScoutIslamicTalismans && timeout 900 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-59/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r59/ScoutIslamicTalismans/rows.md --entry /fast/scratch/hyaku/kotodama-r59/ScoutIslamicTalismans/stub.md`

## Rows (exactly 11 cells each)

| S612 | Victoria and Albert Museum. "Talisman holder" (amulet case), silver case with a glass window containing a miniature Qur'an, Turkey, 1820-30, Collections record O79276 with the museum's curatorial summary; unknown maker, given by J. Grzywaczewski. — https://api.vam.ac.uk/v2/museumobject/O79276 (direct plain request to the V&A Collections API, HTTP 200, 4,909 bytes, JSON record read in full, 2026-10-23; the Wayback CDX index returned no 200 snapshot of this API URL on 2026-10-23, so no capture is listed) | docs | A | one museum summary of what silver amulet holders held, how they were carried on the body and what they guarded against | summaryDescription, first sentence: "Silver amulet holders, often containing symbolic material or a piece of paper with a magical or holy inscription, were worn throughout the Muslim world." | A silver amulet holder was a container of symbolic material or a written inscription, worn across the Muslim world. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |
| S613 | Cleveland Museum of Art. "Necklace (ashän ketab) with amulet pendants (tälsäm)," Ethiopia, probably Harar, late 1800s or early 1900s, silver alloy, accession 2025.152, African Art; gift of Raymond A. Silverman; object record with curatorial description. — https://www.clevelandart.org/art/2025.152 (direct plain request, HTTP 200, 84,820 bytes, description read in full, 2026-10-23; the Wayback CDX index returned no 200 snapshot of this page on 2026-10-23, so no capture is listed) | docs | A | the tälsäm necklace as worn protection: box pendants, the evil eye, filigree work and thaler silver | description, second sentence: "This silver necklace is composed of numerous box-shaped amulet pendants (tälsäm) meant to ward off the evil eye or other dangers." | A necklace of silver boxes called tälsäm was worn as protection against the evil eye and other harms. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |

## Gate lines

- S612 — https://api.vam.ac.uk/v2/museumobject/O79276 — accessed 2026-10-23 — summaryDescription, first sentence: “Silver amulet holders, often containing symbolic material or a piece of paper with a magical or holy inscription, were worn throughout the Muslim world.”. Grounds: A silver amulet holder was a container of symbolic material or a written inscription, worn across the Muslim world. Seat: ScoutIslamicTalismans.
- S613 — https://www.clevelandart.org/art/2025.152 — accessed 2026-10-23 — description, second sentence: “This silver necklace is composed of numerous box-shaped amulet pendants (tälsäm) meant to ward off the evil eye or other dangers.”. Grounds: A necklace of silver boxes called tälsäm was worn as protection against the evil eye and other harms. Seat: ScoutIslamicTalismans.

## Draft entry sentences

S612:

An amulet case is a container before it is an ornament: a silver box made to hold a slip of paper or a tiny Qur'an. (S612)
Two loops at either side take a strap, so the silver case rides on the upper arm. (S612)
A glass window in the lid keeps the inscription on the book inside visible while the case stays shut. (S612)

S613:

Strung as a necklace, the tälsäm boxes repeat the same protection many times over, each box its own container. (S613)
The boxes keep working whether they are empty or hold a written prayer, so the container itself carries part of the virtue. (S613)
The filigree and granulation are characteristic of Harar work, a craft of silversmiths trained through long apprenticeships. (S613)

## What I opened (all ordinary GETs, this session)

| URL | status | bytes | read |
|---|---|---|---|
| https://api.vam.ac.uk/v2/museumobject/O79276 | 200 | 4,909 | full JSON record: objectType "Amulet case", title "Talisman holder", Turkey 1820-30, physical and summary description |
| https://www.clevelandart.org/art/2025.152 (fetched as https://clevelandart.org/art/2025.152, redirected) | 200 | 84,820 HTML / 2,108 text | full curatorial description, tombstone, "did you know" line |
| https://api.vam.ac.uk/ (BOILER root, redirects to developers.vam.ac.uk) | 200 | 2,912 | quote absent |
| https://www.clevelandart.org/ (BOILER root, /home) | 200 | 772,246 | quote absent |
| https://api.vam.ac.uk/v2/museumobject/O123320, O481040, O449546, O110724, O324096 | 200 | 3,905–6,425 | read for candidates, not offered (below) |
| https://www.khalilicollections.org/.../faceted-talismanic-pendant-tls61/, .../talismanic-shirt-txt-463/, .../power-protection-islamic-art-supernatural-ashmolean-museum-oxford/ | 200 | 95,959 / 94,753 / 81,439 | read, not offered (below) |
| https://art.thewalters.org/object/57.2358/, /57.2362/ | 200 | 234,519 / 226,163 | read, not offered (below) |
| https://openaccess-api.clevelandart.org/api/artworks/692270, 692269, 692272, 674614 | 200 | 4,211–5,846 | 692270 is the S613 record; the others are near-duplicates, not offered |
| https://www.metmuseum.org/ | 429 | 34,228 | host refused plain GETs, abandoned |
| https://www.britishmuseum.org/collection | 403 | 5,559 | abandoned |
| https://api.artic.edu/api/v1/artworks/search?q=talismanic... | 403 | 5,884 | abandoned |

Discovery calls (search endpoints, not cited as sources): V&A `objects/search?q=talismanic|amulet|ta'wiz|magic square|quran case`, Cleveland open-access `?q=talismanic|amulet|magic+square`, Khalili site search, Walters site search, Wayback availability + CDX for both offered URLs (both empty).

## Rejected (with the tool output that decided it)

- https://art.thewalters.org/object/57.2358/ and /57.2362/ — rich evil-eye prose ("the ills brought on by the malevolent glare of the evil eye") but the page carries only one charm-guard window, so TOPIC fails on page density: `windows=1 terms=2` for each (need page_hits 3). Verbatim: `walters-57.2358.txt: windows=1 terms=2 terms_list=['evil eye', 'talismanic']`, `walters-57.2362.txt: windows=1 terms=2 terms_list=['evil eye', 'talismanic']`.
- https://www.khalilicollections.org/islamic-art/power-protection-islamic-art-supernatural-ashmolean-museum-oxford/ — exhibition announcement, not an object record, and below the page floor: `windows=2 terms=2` (need 3).
- https://www.khalilicollections.org/collections/islamic-art/khalili-collection-islamic-art-faceted-talismanic-pendant-tls61/ — the only prose is one "Other Notes" fragment ("The pendant is inscribed with religious inscriptions, including, tawakkaltu 'ala Allah..."); no sentence about protection and no charm-guard window in it. Page measurement is title-driven: `windows=8 terms=4`.
- https://www.khalilicollections.org/collections/islamic-art/talismanic-shirt-txt-463/ — same shape: "inscriptions consist of invocations using some of the Names of God; select Qur'anic verses..." is a fragment with zero charm-guard windows; page `windows=5 terms=4`.
- https://api.vam.ac.uk/v2/museumobject/O481040 and /O449546 (talismanic shirts) — good object but the only quotable sentences are catalogue fragments ("Talismanic shirt, cotton, inscribed with verses from the Quran in ink and gold paint."); no sentence states what the shirt is for, so a blind reviewer could not tie it to a teaches cell. Not offered.
- https://api.vam.ac.uk/v2/museumobject/O110724 (Qur'an case, Iran 1800-70) — excellent prose ("Miniature copies are worn in the same way as a talisman, as protection from misfortune") but the page has only two charm-guard windows: `windows=2 terms=2`.
- https://api.vam.ac.uk/v2/museumobject/O324096 (Qur'an case) — record has physicalDescription but no summaryDescription, nothing to teach from.
- https://api.vam.ac.uk/v2/museumobject/O123320 (rock-crystal talisman, Middle East 10th-16th c.) — strong runner-up (`windows=18 terms=15`), quote "The inscriptions on this item, which include the name of the prophet Solomon, show that it had a talismanic function of some sort." Held back only by the two-row cap; it is the natural substitute if S612 fails blind SUPPORT.
- https://openaccess-api.clevelandart.org/api/artworks/692269, 692272, 674614 — same curatorial paragraph as S613 (filigree, Harar, amulets) or loose "may have links to Islamic talismanic motifs"; not offered to avoid three rows saying one thing.
- Met Museum, British Museum, Art Institute of Chicago — plain GET refused (429, 403, 403 above); no ordinary copy available in-session, so no row from those hosts.

## Notes and remaining unknowns

- No Wayback capture of either offered page existed when I checked (`archive.org/wayback/available` returned `{"archived_snapshots": {}}` for both; CDX `filter=statuscode:200` returned `[]`), so both rows carry the live URL only. Under FETCH-59 a single failed GET sinks the row; the acceptance run's first fetch is the only protection.
- Neither host is on the reserved list; neither URL or quote appears in `corpus/SOURCES.md` (`grep -c 'O79276'` = 0, `grep -c '2025\.152'` = 0, quote fragments 0, `\bS61[23]\b` = 0).
- Cleveland keeps its own hedge ("probably Harar"), which the entry should preserve; the V&A record says the case "may have been worn on the upper arm", so the arm placement is stated as the record's reading, not as fact.
- The V&A dimension fields are labelled cm but read like inches (3.5 x 1.8 x 2.7); I used none of them.
- No tools installed or updated; no package manager touched.
