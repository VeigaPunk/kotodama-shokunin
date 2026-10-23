# ScoutCrestRights — Round 57, claim C sources (crests as owned rights, Northwest Coast)

Seat draft id block: `NEW-ScoutCrestRights-<n>`. All quotes verified live with `reports/round-57/reopen-quote.py` (one-line `LOCATED` output pasted under each quote). All URLs fresh: `grep -c` of each URL's host/path in `corpus/SOURCES.md` printed 0.

## NEW-ScoutCrestRights-1

citation: Museum of Anthropology at UBC (University of British Columbia), n.d., "Background Information: NWC First Nations of B.C." (school-program resource), https://moa.ubc.ca/wp-content/uploads/2014/08/SchoolProgram-BackgroundInfo.pdf (stable id: MOA UBC, PDF, accessed 2026-10-22).
url: https://moa.ubc.ca/wp-content/uploads/2014/08/SchoolProgram-BackgroundInfo.pdf
route: direct, HTTP 200, PDF (909,643 bytes), text extracted this session with pypdf (uv ephemeral environment; no system install).
kind: docs
tier: A — the holding museum (UBC MOA) writing about its own collections and the region it collects from; B where the text generalizes across all Northwest Coast First Nations.
scope: what a crest is, that crests attach to families/individuals/lineages, that rights to use ancestral crests are defined and maintained, that poles and houseposts declare family crest ownership, and that potlatches publicly present and transfer hereditary rights and privileges.
quotes:
- m1: "Social positions and rights to use particular ancestral crests were and continue to be, carefully defined and maintained"
  `python3 -B reports/round-57/reopen-quote.py 'https://moa.ubc.ca/wp-content/uploads/2014/08/SchoolProgram-BackgroundInfo.pdf' 'Social positions and rights to use particular ancestral crests were and continue to be, carefully defined and maintained'` → LOCATED https://moa.ubc.ca/wp-content/uploads/2014/08/SchoolProgram-BackgroundInfo.pdf
- m2: "Crests are images from the animal, human and spirit worlds representing the history, and lineage of a family or an individual"
  → LOCATED https://moa.ubc.ca/wp-content/uploads/2014/08/SchoolProgram-BackgroundInfo.pdf
- m3: "Poles are erected by families as declarations of their ancestral heritage"
  → LOCATED https://moa.ubc.ca/wp-content/uploads/2014/08/SchoolProgram-BackgroundInfo.pdf
- m4: "Houseposts are the poles carrying the crest images belonging to the heads of a House"
  → LOCATED https://moa.ubc.ca/wp-content/uploads/2014/08/SchoolProgram-BackgroundInfo.pdf
- m5: "individuals and families use these occasions to reaffirm kinship ties and social ranking through the public presentation and transfer of hereditary rights and privileges"
  → LOCATED https://moa.ubc.ca/wp-content/uploads/2014/08/SchoolProgram-BackgroundInfo.pdf
teaches: On the Northwest Coast a crest is a lineage- or family-owned image whose use is a defined, maintained right, publicly declared on poles and transferred at potlatches.
draft sentences:
- On the Northwest Coast a crest is an image from the animal, human, and spirit worlds representing the history and lineage of a family or an individual (NEW-ScoutCrestRights-1, m2).
- Rights to use particular ancestral crests are carefully defined and maintained, especially by northern groups (NEW-ScoutCrestRights-1, m1).
- Families erect poles as declarations of their ancestral heritage, and most poles display figures from the histories of the owning families (NEW-ScoutCrestRights-1, m3).
- Houseposts are the poles carrying the crest images belonging to the heads of a House (NEW-ScoutCrestRights-1, m4).
- Potlatches publicly present and transfer hereditary rights and privileges such as land, property, songs, names, stories, and dances (NEW-ScoutCrestRights-1, m5).

## NEW-ScoutCrestRights-2

citation: Royal BC Museum, n.d., "Kwakwaka'wakw Heraldic Pole, 1953" (Thunderbird Park online exhibit, carvers Mungo Martin, David Martin, Mildred Hunt; photo RBCM 20122), https://rbcm.ca/exhibits/tbird-park/html/late/ex08/ex8.htm (accessed 2026-10-22).
url: https://rbcm.ca/exhibits/tbird-park/html/late/ex08/ex8.htm
route: direct, HTTP 200, text/html (23,665 bytes, served as ISO-8859-1; quotes verified against served bytes).
kind: docs
tier: A — the holding museum's own exhibit record of a pole object in its Thunderbird Park collection and its stated display conventions; B where it generalizes about Kwakwaka'wakw convention.
scope: the convention that a pole standing before a lineage house displays that house's own crests, one carver's deliberate choice to represent four Kwakwaka'wakw nations instead, and crest-to-family attributions (Thunderbird crest of an A'wa'etłala family; Grizzly Bear holding a Copper as ancestor of a Kwagu'ł family).
quotes:
- r1: "Rather than display his own crests on the pole, as was customary for a pole standing before a lineage house"
  `python3 -B reports/round-57/reopen-quote.py 'https://rbcm.ca/exhibits/tbird-park/html/late/ex08/ex8.htm' 'Rather than display his own crests on the pole, as was customary for a pole standing before a lineage house'` → LOCATED https://rbcm.ca/exhibits/tbird-park/html/late/ex08/ex8.htm
teaches: For a pole standing before a lineage house, displaying the house's own crests is customary, so including another set of crests is a deliberate, recorded choice.
draft sentences:
- Customarily a pole standing before a lineage house displays its own crests (NEW-ScoutCrestRights-2, r1).
- Mungo Martin chose instead to include crests representing four of the Kwakwaka'wakw nations, wanting to represent and honour all of them (NEW-ScoutCrestRights-2, r1).
- The page attributes crests to specific families, such as the Thunderbird as the crest of an A'wa'etłala family at Dzawadi, Knight Inlet (NEW-ScoutCrestRights-2, r1).

## Rejected

- U'mista Cultural Society, "Authenticity" statement (https://www.umista.ca/pages/authenticity): opened and located ("crests and designs that belong to specific families who have inherited the right to create and wear these ancient symbols"); not filed because the wave allowed 1–2 sources and named the three museums — kept as fallback community-statement intel for the L1.
- Canadian Museum of History Collection Online records: opened via the museum's own API (e.g. Haida copper VII-B-1595: "This very large Haida copper shield once belonged to Albert Edward Edenshaw … This copper portrays his female Grizzly Bear crest"; frontlet VII-B-1102; hat VII-B-899 "Male artists painted the hats with the crests of the commissioning family"). Text is served only by the JSON API (`POST /_api/_search/`); the public artifact pages `/collections/artifact/<id>` are empty SPA shells and the API URL carries `_search` + query, both refused by the locator — not usable under LOCATE. Recorded for other scouts (a CMH record row cannot vouch under the current locator).
- American Museum of Natural History, "Łingít/Tlingit" page (https://www.amnh.org/exhibitions/permanent/northwest-coast/lingit-tlingit): CAPTCHA challenge — challenge met, not passed; not used.
- Royal BC Museum main-site search (https://royalbcmuseum.bc.ca/search?q=crest): Cloudflare challenge — skipped; the rbcm.ca exhibit page above was used instead.
- warmuseum.ca old CMC exhibit URL (https://www.warmuseum.ca/cmc/exhibitions/aborig/nwca/nwcam09e.html): serves the Canadian War Museum navigation shell, not exhibit content; rejected.

## Tooling log

- `uv run --with pypdf` (ephemeral, pypdf 5.x) used to extract text from two PDFs (MOA SchoolProgram-BackgroundInfo.pdf, McCord Wearing-Our-Identity.pdf) for verbatim quoting — channel uv, no system install, reason: PDF text extraction.
- No other installs; no pacman transactions.

## Findings for L1 (facts, not claims)

- UBC MOA Collection Online records publish exact crest-right language ("each group owns the right to display specific crests", "the design becomes the property of the family and cannot be copied", button blanket record, "k'angextola (Button Blanket)") but every record URL is `/search/item?...` (path `search` + query) → refused by the locator; MOA cannot vouch via its catalogue URLs in the current round.
- The MOA background-info PDF is the cleanest locatable MOA source for crest/lineage/rights statements; all five quotes above located.
- RBCM's Thunderbird Park exhibit (rbcm.ca) is static, server-rendered and challenge-free.
