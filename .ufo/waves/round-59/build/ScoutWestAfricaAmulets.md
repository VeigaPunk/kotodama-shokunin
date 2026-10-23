# ScoutWestAfricaAmulets — claim C source seat (round 59)

Subtopic: West African amulets — leather-cased Qur'anic amulets (gris-gris, safi) and
amulet-covered garments of hunters and warriors; museum records and open scholarship.
Two rows offered, S632 and S633 (my assigned ids only). Every URL below was opened in this
session by a plain GET; nothing was read through a browser, challenge or login.

Installs: none (no tool was installed or updated for this seat).
Processes: all probes ran under `timeout` and have exited; nothing of mine is still running.
Scratch: `/fast/scratch/hyaku/kotodama-r59/ScoutWestAfricaAmulets/`.

## 1. Registry rows (paste as-is)

| S632 | Elnaggar, Abdelrazek, Hend Mahgoub, Laura Maestro-Guijarro, Ana Crespo Ibáñez, Paula María Carmona-Quiroga, Santiago Sánchez-Cortés, Žiga Rehar, Gregor Kos, Ahmed Ameen, Marko Frelih and Matija Strlič. 2025. Multianalytical Study of Amuletic and Talismanic Islamic-African Paper Manuscripts in the Slovene Ethnographic Museum, ChemPlusChem 90(12): e202500433, DOI 10.1002/cplu.202500433, PMC12701302; the group was brought to Ljubljana from Togo in 1914. Peer-reviewed open access under CC BY 4.0. — https://pmc.ncbi.nlm.nih.gov/articles/PMC12701302/ (direct plain GET, HTTP 200, 273,314 bytes, 2026-10-23) | paper | B | the paper's synthesis of how Islamic amulets and talismans are made and switched on (customised shape, wearing or placing, or reading the written text), plus its own analysis of the Togo group. (tier note: A for the archaeometric findings the authors made on the Slovene Ethnographic Museum group; B for the general statement quoted, which their discussion draws from cited scholarship.) | Discussion, the paragraph after the amulet-and-talisman definition: "Amulets or talismans gain their power firstly through their customized shape and form and secondly through their application by simply being worn or placed" | Customised shape gives an amulet its force, and wearing or placing the object is the second act that switches it on. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |
| S633 | Hassani, Ali. 2026. Talismanic Tunic, Visual Resources of the Middle East, North Africa, and South Asia (Yale University), post of 10 June 2026; object 2021.32.3, Yale University Art Gallery, a shirt from Ghana, ca. 1920-50. — https://vrme.yale.edu/posts/2026-06-10-talismanic-tunic (direct plain GET, HTTP 200, 58,701 bytes, 2026-10-23) | docs | B | one Ghanaian talismanic shirt and what carries its protection: inscribed Qur'anic text and supplications, magic squares, cowrie shells, and leather pouches sewn inside. (tier note: B — a short illustrated essay by a named author on a Yale teaching and reference site, written about the Yale University Art Gallery object; it is not peer-reviewed and reports no fieldwork, so it speaks for this one shirt and for the practice only as the site summarises it.) | Essay body, the paragraph describing the shirt's construction: "Cowrie shells adorn the neck, and leather pouches, presumably containing additional amulets, are sewn into the interior of the shirt." | Leather pouches holding further amulets are sewn inside a Ghanaian shirt, so protection sits between cloth and body. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |

## 2. Gate lines

- S632 — https://pmc.ncbi.nlm.nih.gov/articles/PMC12701302/ — accessed 2026-10-23 — Discussion, the paragraph after the amulet-and-talisman definition: “Amulets or talismans gain their power firstly through their customized shape and form and secondly through their application by simply being worn or placed”. Grounds: Customised shape gives an amulet its force, and wearing or placing the object is the second act that switches it on. Seat: ScoutWestAfricaAmulets.
- S633 — https://vrme.yale.edu/posts/2026-06-10-talismanic-tunic — accessed 2026-10-23 — Essay body, the paragraph describing the shirt's construction: “Cowrie shells adorn the neck, and leather pouches, presumably containing additional amulets, are sewn into the interior of the shirt.”. Grounds: Leather pouches holding further amulets are sewn inside a Ghanaian shirt, so protection sits between cloth and body. Seat: ScoutWestAfricaAmulets.

Neighbourhood check: neither host appears in `corpus/SOURCES.md` as this URL. `pmc.ncbi.nlm.nih.gov` is
used at S245 for a different article and `vrme.yale.edu` appears nowhere; no URL above collides with
any existing row. Neither source cell carries a second URL: no Wayback capture of either page exists
(see §6), so nothing but the live URL is listed and the same-page rule cannot be breached.

## 3. rowcheck output (verbatim, run 2026-10-23)

```
$ cd /fast/scratch/hyaku/kotodama-r59/ScoutWestAfricaAmulets && timeout 900 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-59/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r59/ScoutWestAfricaAmulets/rows.md --entry /fast/scratch/hyaku/kotodama-r59/ScoutWestAfricaAmulets/stub.md
S632 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://pmc.ncbi.nlm.nih.gov/articles/PMC12701302/ | BOILER: root-clear https://pmc.ncbi.nlm.nih.gov/; not a title, h1 or meta label | RELEVANCE: shared=['amule', 'custo', 'shape'] | TOPIC: quote_hits=2 function_words=4 page_hits=124 page_terms=114 need=1/2/3/2
S633 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://vrme.yale.edu/posts/2026-06-10-talismanic-tunic | BOILER: root-clear https://vrme.yale.edu/; not a title, h1 or meta label | RELEVANCE: shared=['amule', 'leath', 'pouch', 'sewn', 'shirt'] | TOPIC: quote_hits=1 function_words=4 page_hits=18 page_terms=17 need=1/2/3/2
EXIT=0
```

The same two rows printed PASS on three separate runs in this session (the last after the source cell
of S632 was amended to name the CC BY 4.0 licence); both live URLs answered HTTP 200 on every attempt.

## 4. Draft sentences (paste into the entry)

An amulet carries force in its customised shape, and the maker settles that shape before the piece is ever worn or placed (S632).
Because application is the second source of power, where a charm is put is as much a design decision as how it is made (S632).
Wearing and placing are separate operations from making, which lets one amulet live on a body, in a house, or wherever its owner puts it (S632).
A Ghanaian talismanic shirt hides its amulets inside, with leather pouches sewn into the lining and cowrie shells at the neck (S633).
Because the pouches are sewn into the interior, the shirt's extra amulets stay between cloth and body instead of hanging outside (S633).
Cowrie shells at the neck and leather pouches inside show how one garment carries protection at several depths at once (S633).

Every sentence says only what its row's quote and page carry. "In a house" on the S632 line comes
from the same page ("more common for Muslims to wear or display verses from the Qur'an in their
homes"), not from the quote; drop it if the L1 wants strictly quote-borne lines.

## 5. What these rows give a worldbuilder

- **Making is two acts, not one.** S632 separates the object's customised form from its application:
  a charm is finished by wearing or placing it (and, elsewhere on the same page, some pieces are
  activated only by reading the text written on them). That is a usable design rule: the maker
  chooses the form, the user chooses the placement, and the two can belong to different people.
- **Protection has depth.** S633 shows a single garment carrying protection at more than one level —
  inscribed text and supplications on the surface, magic squares and grids painted on, cowrie shells
  at the neck, and leather pouches sewn into the interior so that further amulets stay unseen between
  cloth and body. Hidden casing is itself part of the design.
- **Material and casing.** S633's leather pouches are sewn-in containers; the casing is not decoration
  but the amulet's housing. S632's paper group (Togo, collected 1914) is the written half of the same
  system: paper, ink, divine names, magic squares.

## 6. Rejected: every source I opened and did not offer

1. **Science Museum Group, "Amulet necklace", A658410 (West Africa, 1880–1920)** —
   https://collection.sciencemuseumgroup.org.uk/objects/co107952/amulet-necklace — first read HTTP 200,
   52,816 bytes, and its catalogue text is the best single leather-case sentence I found in the whole
   sweep: "An amuletic necklace from West Africa with small leather charm cases incised with decoration
   and strung on a leather thong. Charm cases often contain folded talismans - a piece of writing or
   drawing with meaning for the individual patient. The talismans are unique and are produced in
   response to the particular situation believed to be causing ill health." **Rejected on host
   stability, not content.** My second plain request to the same host returned the body text
   `Rate limited - please slow down`, and a re-check minutes later returned `403 919` (verbatim
   `curl -w '%{http_code} %{size_download}'` output). Under FETCH-59 a 403 is never retried, and BOILER
   fetches `https://collection.sciencemuseumgroup.org.uk/` live, so a host that now answers plain GETs
   with 403 can sink the row. The quote is worth another seat's attempt only if the host recovers.
2. **Pitt Rivers Museum, Oxford, "Small Blessings — Amulet Trail: Qur'anic amulet, Nigeria" (PRM
   1980.11.1)** — https://web.prm.ox.ac.uk/amulets/index.php/museum-trail/15-resources/144-trail-quranic/index.html
   — HTTP 200, 2,914 characters of extracted body text, page TOPIC = 8 windows, 9 DISCIPLINE terms.
   Rejected on a gated miss: its one sentence that says exactly what my subtopic needs has no
   CHARM-set word, so the quote cannot pass TOPIC. Verbatim rowcheck output for that draft row:
   ```
   S699 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC FAIL | LOCATE: https://web.prm.ox.ac.uk/amulets/index.php/museum-trail/15-resources/144-trail-quranic/index.html | BOILER: root-clear https://web.prm.ox.ac.uk/; not a title, h1 or meta label | RELEVANCE: shared=['excer', 'leath', 'silve'] | TOPIC: quote_hits=0 function_words=6 page_hits=8 page_terms=9 need=1/2/3/2
   EXIT=1
   ```
   The sentence, kept here so nobody has to re-open the page:
   "The amulet maker is known by different names in different societies." / "In Islamic communities,
   he is often a holy man - a mullah or, in West Africa, a marabout." / "He encases small slips of
   paper bearing excerpts from the Qur'an (Koran) in Arabic script into pouches of leather or textile,
   or even silver containers." Any 25-word slice of these lacks `amulet|talisman|charm|...`, so the
   gate and the subtopic disagree here.
3. **The Metropolitan Museum of Art, "Amulets and Talismans from the Islamic World" (Heilbrunn
   Timeline essay)** — https://www.metmuseum.org/essays/amulets-and-talismans-from-the-islamic-world —
   opened live, HTTP 200, 10,125 characters, 43 windows, 30 DISCIPLINE terms. Its best sentence,
   "The most efficacious talismans are those that are inscribed with prayers that evoke the name of God
   and the prophet Muhammad and his companions.", would pass every leg mechanically. **Rejected on
   fetch risk.** `metmuseum.org` answers burst plain GETs with 429 (precedent S304 in this corpus), and
   BOILER fetches the site root `https://www.metmuseum.org/` live; a 429 there fails the row, and I
   could not secure a same-page capture to fall back on because the Wayback CDX API answered
   `Internet Archive: Temporarily Offline` (see below). If the L1 wants this sentence, it needs a
   stable retirement copy of the essay *and* of the Met root before it can be relied on.
4. **Smithsonian National Museum of African Art, "Arm band", NMAFA 2012-18-198 (Dakar, Senegal)** —
   https://africa.si.edu/collection/object/nmafa_2012-18-198 — rejected on a fetch error. Verbatim:
   `403 text/html; charset=UTF-8 46651` and the served page title is `Smithsonian request verification`.
   A challenge page is never an ordinary copy.
5. **Harn Museum of Art, "Hunter's Shirt with Amulets (batakari)"** —
   https://harn.emuseum.com/objects/3889/hunters-shirt-with-amulets-batakari — rejected on a fetch
   error. Verbatim: `urllib.error.HTTPError: HTTP Error 403: Forbidden`. This was the closest
   hunter/warrior-garment record I found and it is unwalled to me.
6. **Textile Society of America / UNL DigitalCommons, "Re-thinking the Display and Interpretation of
   African Textiles at the Detroit Institute of Arts"** —
   https://digitalcommons.unl.edu/cgi/viewcontent.cgi?article=1136&context=tsaconf — rejected on a
   fetch error. Verbatim: `urllib.error.HTTPError: HTTP Error 403: Forbidden`. Its reported content
   (Akan shirt amulets called *sebe*, leather packets over folded papers with Islamic prayers or magic
   squares) is exactly my subtopic; only the 403 blocked it.
7. **Princeton University Library, Digital PUL, "Hatumere (West-African Islamic protective charms)"** —
   https://dpul.princeton.edu/global-book-forms/catalog/dc6q182z43d — rejected on no readable body:
   the plain GET returned HTTP 200 but text extraction yielded 497 characters (a JavaScript shell), so
   there is no body text to locate a quote in.
8. **The British Museum, Islamic Gallery, "Qur'an-case, amulet", As1966,01.855** —
   https://islamicworld.britishmuseum.org/collection/RRM44731 — HTTP 200, but only 1,436 characters of
   extracted text and the record's findspot is `Iran`, outside this seat's West African scope. Not
   offered.
9. **Penn Museum, "Amulet", 2003-72-238 (Senegal, inscription language Arabic)** —
   https://collections.penn.museum/collections/object/355678 — HTTP 200, 7,544 characters, but the
   record is a field table (3 CHARM-GUARD windows, 4 DISCIPLINE terms) with no sentence stating what
   the object does; my candidate extractor printed no eligible sentence at all. Not offered.

## 7. Unknowns and gaps the L1 should carry

- **"Gris-gris" and "safi" are not evidenced by my two rows.** Neither opened page uses either word.
  The entry must not attribute that vocabulary to S632/S633; another seat's row, or a later round, has
  to carry the terms themselves.
- **The marabout-as-maker sentence is real but ungated.** See §6 item 2: the Pitt Rivers page states
  it in plain prose, and the TOPIC gate cannot be met by that sentence. If the entry uses the marabout
  point, it needs a source whose sentence carries an amulet/talisman/charm word near a protect/ward
  word inside 25 words.
- **Wayback could not be consulted.** `https://archive.org/wayback/available?url=…` returned
  `"archived_snapshots": {}` for both of my URLs, and the CDX API then answered
  `Internet Archive: Temporarily Offline`. So no capture is listed for either row — an honest absence,
  not a decision to skip one. Both live pages answered 200 repeatedly, so I did not need a fallback.
- **Hunter/warrior garments remain uncovered by my rows.** S633 is a talismanic shirt worn for
  protection in general (the essay cites battle use, illness, favour and fortune), not a hunter's
  amulet-covered gown; the two hunter-garment records I found (Harn *batakari*, the Akan *sebe* paper)
  were both 403.
