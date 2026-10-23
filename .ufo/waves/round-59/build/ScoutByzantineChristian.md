# ScoutByzantineChristian — claim C source seat, round 59

Subtopic: Byzantine and early Christian amulets (phylacteries, encolpia, holy-rider amulets, magical gems with Christian formulae).
S-ids assigned: S616, S617. Two rows offered, both pass the frozen rowcheck with the entry stub.
No installs, no upgrades (nothing was needed; pdftotext 26.08.0 already present, `uv`/pypdf 5.4.0 already present for the instrument).

## Row 1 — S616

| S616 | The Metropolitan Museum of Art, "Amulet Carved in Intaglio (Incised)", object 464456, Byzantine (Egypt), 6th–7th century, hematite with silver mount, 5 x 3.7 x 1 cm, Gift of J. Pierpont Morgan, 1917; collection record with the museum's description. — https://www.metmuseum.org/art/collection/search/464456 (direct plain request, HTTP 200, 208088 bytes, 2026-10-23) — capture https://web.archive.org/web/20260610070727id_/https://www.metmuseum.org/art/collection/search/464456 | docs | A | the museum's record of one Byzantine (Egypt) hematite amulet: the stone chosen for the ailment it was thought to cure, and the gospel miracle its inscriptions name | museum description, sentence on the stone: "Hematite was believed to stop the flow of blood and was a favorite medium for amulets related to female reproductive health and menstrual problems" | Hematite was a favourite medium for amulets against menstrual and reproductive complaints because the stone was thought to staunch bleeding. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |

- S616 — https://www.metmuseum.org/art/collection/search/464456 — accessed 2026-10-23 — museum description, sentence on the stone: “Hematite was believed to stop the flow of blood and was a favorite medium for amulets related to female reproductive health and menstrual problems”. Grounds: Hematite was a favourite medium for amulets against menstrual and reproductive complaints because the stone was thought to staunch bleeding. Seat: ScoutByzantineChristian.

What the row can carry for the entry (design decision: material answers the ailment): the stone is chosen for the trouble it is meant to counter — hematite was thought to staunch blood and therefore served amulets about menstruation and reproductive health. The same record also says the inscriptions identify the subject as the Woman with the Issue of Blood (Mark 5:25–34; Luke 8:43–48), i.e. a named gospel cure is inscriptional, but the offered quote itself carries only the material logic; entry sentences should stay on the stone.

## Row 2 — S617

| S617 | Tuerk, Jacquelyn. 2008. "Hierotopy, Narrative, and Magical Amulets." In *Hierotopy: Comparative Studies of Sacred Spaces*, ed. Alexei Lidov (Moscow: Indrik), the English text opening at p. 79 with a Russian summary at the end; the volume's own contents page lists the essay under this title and the 2008 Indrik imprint. — http://hierotopy.ru/contents/ComparativeStudySacredSpaces_06_Tuerk_NarrativeAmulets_2008_Eng.pdf (direct plain request, HTTP 200, application/pdf, 319854 bytes, text extracted with pypdf 5.4.0, 2026-10-23) | paper | B | how amuletic images and words work in Byzantine practice, at the point where the protective image moves from icon to engraved stone worn on the body | article body, p. 100, first sentence of the amuletic-icons passage: "In addition to holy icons and unorthodox amulets, there survive icons in the amuletic form of engraved stones to be worn on the body" | A protective image can shrink to an engraved stone worn on the body, so a gemstone carries the same amuletic work as a painted icon. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |

- S617 — http://hierotopy.ru/contents/ComparativeStudySacredSpaces_06_Tuerk_NarrativeAmulets_2008_Eng.pdf — accessed 2026-10-23 — article body, p. 100, first sentence of the amuletic-icons passage: “In addition to holy icons and unorthodox amulets, there survive icons in the amuletic form of engraved stones to be worn on the body”. Grounds: A protective image can shrink to an engraved stone worn on the body, so a gemstone carries the same amuletic work as a painted icon. Seat: ScoutByzantineChristian.

What the row can carry for the entry (design decision: how far a protective image can shrink and where it sits): an image with amuletic force need not be a panel or a pendant relief — it can be an engraved stone carried on the body, and the article treats amuletic stones and holy icons as one continuum of practice. Tier B: an expert essay in an edited conference volume, openly hosted by the project that published the volume; not the object records themselves.

## Rowcheck output (frozen instrument, both rows, with entry stub)

Command run from `/fast/scratch/hyaku/kotodama-r59/ScoutByzantineChristian`:

```
python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-59/rowcheck.py --draft rows.md --entry stub.md
```

Verbatim stdout:

```
S616 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.metmuseum.org/art/collection/search/464456 | BOILER: root-clear https://www.metmuseum.org/; not a title, h1 or meta label | RELEVANCE: shared=['amule', 'hemat', 'mediu', 'menst', 'repro'] | TOPIC: quote_hits=1 function_words=7 page_hits=8 page_terms=8 need=1/2/3/2
S617 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: http://hierotopy.ru/contents/ComparativeStudySacredSpaces_06_Tuerk_NarrativeAmulets_2008_Eng.pdf | BOILER: root-clear http://hierotopy.ru/; not a title, h1 or meta label | RELEVANCE: shared=['amule', 'body', 'engra', 'icon', 'stone', 'worn'] | TOPIC: quote_hits=4 function_words=7 page_hits=115 page_terms=77 need=1/2/3/2
```

Both rows: live URL first in the source cell; S616's single extra URL is the `id_` Wayback capture of that same Met page (20260610070727), inside the same-page rule. S617 lists one URL only. No DOI links, no IP/localhost/port URLs, no reserved host.

## Draft entry sentences

- Hematite was picked for amulets against menstrual and reproductive complaints because the stone was thought to stop bleeding (S616).
- Because the stone itself was thought to staunch blood, the amulet's power lay in its material as much as in its carving (S616).
- Engraved stones could serve as icons worn on the body, so a gemstone could do the protective work of a painted icon (S617).
- The article sets such stone amulets beside orthodox icons, treating amuletic stones and holy images as one continuous practice (S617).

(Each sentence shares at least two content stems with its row's quote and with its teaches — that is what RELEVANCE (c)/(d) checked above with `--entry`.)

## Rejected sources (opened, not offered)

1. **Harvard Art Museums, “Amulet with Holy Rider and Virgin Enthroned”, 1951.31.4.1868** — https://harvardartmuseums.org/collections/object/191293 (HTTP 200, 157,196 bytes). The catalogue text is exactly on-subtopic (Gyllou/Abyzou, the Virgin's general apotropaic force, a probable pregnant wearer, the word “womb” in the edge inscription), but the page's `<meta content>` carries the whole catalogue text, so every protective-content sentence is a label and BOILER fails. Verbatim rowcheck line:
   `S616 LOCATE PASS BOILER FAIL RELEVANCE PASS TOPIC PASS | LOCATE: https://harvardartmuseums.org/collections/object/191293 | BOILER: quote-is-title-heading-or-meta | RELEVANCE: shared=['amule', 'child', 'demon', 'envy', 'pregn', 'woman'] | TOPIC: quote_hits=1 function_words=7 page_hits=28 page_terms=25 need=1/2/3/2`
   The only label-free sentence with a CHARM-GUARD window on that page is metallurgical (“It is unlikely that the amulet was cast, as some of the border inscription lettering is continuous across the join between the two elements.”) and teaches fabrication, not protection.
2. **Princeton University Art Museum, “Amulet with Holy Rider”, y1931-34** — https://artmuseum.princeton.edu/art/collections/objects/19920 (HTTP 200, 201,383 bytes by plain curl; 403 to the instrument's request). The record is on-subtopic (bronze, Syria-Palestine or Egypt, obverse “One God conquering evil”, reverse “Iao, Sabaoth”) and its thematic paragraph on pilgrimage amulets passes RELEVANCE, but Cloudflare challenges the acceptance user agent and no Wayback capture exists. Verbatim:
   `S616 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://artmuseum.princeton.edu/art/collections/objects/19920 HTTPError | BOILER: not-located | RELEVANCE: shared=['amule', 'journ', 'memen', 'peril', 'warde'] | TOPIC: quote_hits=2 not-located`
   `ERR HTTPError HTTP Error 403: Forbidden` with `Cf-Mitigated: challenge`; `{"url": "artmuseum.princeton.edu/art/collections/objects/19920", "archived_snapshots": {}}`.
3. **Foskolou, “The Magic of the Written Word: the evidence of inscriptions on Byzantine magical amulets”, Deltion 35 (2014) 329–348** — the Deltion host is down to plain requests.
   `pdf 503 3194 text/html` (the “PDF” was a 3,194-byte HTML error page); landing page `artpage 503 3194`; no capture: `{"url": "ejournals.epublishing.ekt.gr/index.php/deltion/article/download/5217/4986.pdf", "archived_snapshots": {}}`.
4. **Walters Art Museum, “Amulet with the Evil Eye and the Holy Rider”, 54.2628** — https://art.thewalters.org/object/54.2628/ (live 403; read the 20260119230014 capture, HTTP 200, 230,875 bytes). Body text 2,968 chars, 8 DISCIPLINE terms, 4 CHARM-GUARD windows, but the page is template boilerplate (visit hours, provenance-glossary text, rights statements) with no curatorial description, e.g. “Provenance (from the French provenir , 'to come from/forth') is the chronology of the ownership…”. No body sentence to teach from.
5. **The British Museum, “magical gem; intaglio”, EA56087 (URL H_OA-9576)** — https://www.britishmuseum.org/collection/object/H_OA-9576 (live 403; read capture 20231119022257, HTTP 200, 193,981 bytes). Whole page text 3,713 chars, 0 DISCIPLINE matches, 1 window — below the page floor (3 windows, 2 terms); description is a semicolon list, not a sentence: “Magical gem; intaglio; haematite; oval; bevelled edge; engraved on the obverse: horseman to right spearing half-risen nude figure beneath; star in field; inscribed.”
6. **Kenyon College, Blick-Harris Study Collection, 2020.140** — https://digital.kenyon.edu/arthistorystudycollection/673/ (HTTP 200, 36,135 bytes). Text 1,493 chars, 4 DISCIPLINE terms, 2 CHARM-GUARD windows — below the PAGE_HITS floor of 3, and the page is a bare field list (creator, date, geography, medium, dimensions, credit line).
7. **Host probes that failed and were dropped** (no page opened): `https://artgallery.yale.edu/` → 403; `https://www.doaks.org/` → 0 bytes with HTTP 202 (challenge); `https://www.benaki.org/` → 403. `https://www.smb.museum/` answered 200 but no amulet record was reached, so nothing is claimed from it.

## Confidence and remaining unknowns

- Observed: both quotes are verbatim on the pages that located them now (LOCATE PASS on the live Met page and on the live hierotopy PDF); both pages carry the required window/term density; the four legs pass on the frozen instrument as pasted above.
- [INFERENCE] S616's live Met URL has answered 429 to other rounds' seats (S304, S345, S394); it answered 200 twice today to the instrument's own fetch. The capture is listed so a rate-limited live fetch falls back inside FETCH-59. S617's volume identification rests on the publisher's own contents page (`http://hierotopy.ru/en/?page_id=178`, which lists “Jacquelyn Tuerk. Hierotopy, Narrative, and Magical Amulets” under the Lidov/Indrik 2008 volume); the PDF itself carries the essay title and running heads but no volume title page, so the citation names the volume from that page, not from the PDF.
- Unknown: whether a blind reviewer reads the Tuerk quote as “about protective objects” — it is about amuletic icons and engraved stones, but the word “protection” does not appear in that sentence; the surrounding page is dense with it.
- Unknown: whether the Met record's object is dated 6th–7th century in the museum's own field or only on the display line; the page text read now gives “Byzantine (Egypt) 6th–7th century”, which is what the row says.
