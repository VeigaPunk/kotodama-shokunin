# ScoutMagicalGems — round 59, claim C source seat

Subtopic: Graeco-Egyptian magical gems and inscribed stones — Chnoubis/Abrasax gems, stones chosen for
properties, lapidary lore. Two sources opened and offered, S636 and S637. Every URL below was fetched
by me in this session with an ordinary plain GET (curl, desktop UA, redirects, no challenge solving);
no source listed in `corpus/SOURCES.md` was re-offered (checked with `grep -F` on each URL).

Pre-filing check: `rowcheck.py --draft rows.md --entry stub.md` printed
LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS for both rows, exit 0 (output pasted below).

## Registry rows

| S636 | Kelsey Museum of Archaeology (University of Michigan), DiSKO — Digital Study of Kelsey Objects Project; object page for the "Chnoubis Amulet", inventory 1963.04.0008, steatite, Roman/Egyptian, 1st-5th century CE; catalogue description unsigned and record undated, page read 2026-10-23. — https://diskoproject.kelsey.lsa.umich.edu/object/stomach-amulet/ (direct plain GET, HTTP 200, 200383 bytes); capture https://web.archive.org/web/20260508143745id_/https://diskoproject.kelsey.lsa.umich.edu/object/stomach-amulet/ (Wayback capture 20260508143745, HTTP 200) | docs | B | how a university museum catalogue reads one Chnoubis amulet: the lion-headed serpent as the amulet's protective force, the Egyptian Chnum joined to the Greek Agathodaimon, and the ailments the type answered | Description: "It represents the amulet’s protective nature, associated with both the Egyptian god Chnum and the Greek god Agathodaimon." | The Kelsey entry reads the lion-headed serpent on this steatite Chnoubis amulet as the object's protective force, joining the Egyptian god Chnum with the Greek Agathodaimon. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |
| S637 | Pliny the Elder, *The Natural History*, Volume 6 (of 6), translated by John Bostock and Henry T. Riley; Project Gutenberg eBook 62704 (release date 19 July 2020, most recently updated 18 October 2024), Book XXXVII on precious stones, chapter 37 on iaspis; public-domain translation, English. — https://www.gutenberg.org/cache/epub/62704/pg62704-images.html (direct plain GET, HTTP 200, 4667556 bytes; the nearest Wayback capture, 20260831093908, served 955802 bytes and does not carry the chapter, so no capture is listed) | book | A | Pliny's lapidary lore on iaspis: the standing eastern custom of wearing jasper as an amulet, and the varieties and defects he records for the stone | Book XXXVII, chap. 37 (Iaspis): "Throughout all the East, it is the custom, it is said, to wear iaspis by way of amulet." | Pliny records a standing eastern custom of wearing iaspis as an amulet, so this stone was itself carried for protection. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |

## Gate lines

- S636 — https://diskoproject.kelsey.lsa.umich.edu/object/stomach-amulet/ — accessed 2026-10-23 — Description: “It represents the amulet’s protective nature, associated with both the Egyptian god Chnum and the Greek god Agathodaimon.”. Grounds: The Kelsey entry reads the lion-headed serpent on this steatite Chnoubis amulet as the object's protective force, joining the Egyptian god Chnum with the Greek Agathodaimon. Seat: ScoutMagicalGems.
- S637 — https://www.gutenberg.org/cache/epub/62704/pg62704-images.html — accessed 2026-10-23 — Book XXXVII, chap. 37 (Iaspis): “Throughout all the East, it is the custom, it is said, to wear iaspis by way of amulet.”. Grounds: Pliny records a standing eastern custom of wearing iaspis as an amulet, so this stone was itself carried for protection. Seat: ScoutMagicalGems.

## rowcheck output (verbatim, exit 0)

```
S636 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://diskoproject.kelsey.lsa.umich.edu/object/stomach-amulet/ | BOILER: root-clear https://diskoproject.kelsey.lsa.umich.edu/; not a title, h1 or meta label | RELEVANCE: shared=['agath', 'amule', 'chnum', 'egypt', 'greek', 'prote'] | TOPIC: quote_hits=1 function_words=3 page_hits=8 page_terms=6 need=1/2/3/2
S637 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.gutenberg.org/cache/epub/62704/pg62704-images.html | BOILER: root-clear https://www.gutenberg.org/; not a title, h1 or meta label | RELEVANCE: shared=['amule', 'custo', 'iaspi'] | TOPIC: quote_hits=1 function_words=5 page_hits=43 page_terms=32 need=1/2/3/2
EXIT=0
```

Command run (from /fast/scratch/hyaku/kotodama-r59/ScoutMagicalGems/):

```
timeout 900 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-59/rowcheck.py \
  --draft /fast/scratch/hyaku/kotodama-r59/ScoutMagicalGems/rows.md \
  --entry /fast/scratch/hyaku/kotodama-r59/ScoutMagicalGems/stub.md
```

## draft sentences

The Kelsey Museum's entry on a steatite Chnoubis amulet reads the lion-headed serpent as the amulet's protective force, pairing the Egyptian god Chnum with the Greek Agathodaimon (S636).

The same description ties the amulet type to digestive, eye and reproductive ailments, so its protective charge answered specific bodily dangers (S636).

Pliny the Elder records that throughout the East it was the custom to wear iaspis, or jasper, as an amulet, which makes the stone itself the protective agent (S637).

The same lapidary notice places the practice across the East, so the choice of stone, not only its engraving, carried the protection (S637).

## Evidence notes

- S636 live page: "Chnoubis Amulet | Kelsey DiSKO"; object information "1963.04.0008", "Jewelry, Steatite, Roman; Egyptian", "Egypt, Unknown Provenance, 1-5th century CE"; description paragraph: "The Chnoubis amulet showcases a lion-headed serpent facing left. … It represents the amulet’s protective nature, associated with both the Egyptian god Chnum and the Greek god Agathodaimon. Some amulets, including the Chnoubis amulet, were specifically associated with female reproductive concerns. Alongside its primary association with digestive ailments, it was also believed to protect against sciatica, eye ailments, and fertility issues."
- S636 capture verified: I fetched `https://web.archive.org/web/20260508143745id_/https://diskoproject.kelsey.lsa.umich.edu/object/stomach-amulet/` with curl (HTTP 200, 199,819 bytes) and located the anchor quote in its text with the frozen locator (`locate_in` returned True; page text 4,401 chars). The capture is the same page and is real insurance.
- Tier S636 = B: the holding museum's own object page, but the description is unsigned and the record undated; it is a teaching-project catalogue, not a peer-reviewed or signed curatorial essay. It is reliable exactly for how the museum presents this object.
- S637 live page: Project Gutenberg HTML of *The Natural History of Pliny*, Volume 6 (of 6); machine header reads "Title : The Natural History of Pliny, Volume 6 (of 6) / Author : the Elder Pliny / Translator : John Bostock Henry T. Riley / Release date : July 19, 2020 [eBook #62704] / Most recently updated: October 18, 2024 / Language : English". The anchor sits in Book XXXVII, "CHAP. 37.—IASPIS; FOURTEEN VARIETIES OF IT. DEFECTS FOUND IN IASPIS."; the sentence on the page ends "… by way of amulet." and is followed by "The variety of this stone which resembles smaragdus in colour…".
- S637 tier = A: a primary ancient text in a public-domain English translation, read on the e-text publisher's own page; the row supports only what Pliny says and what the translation says.
- The Gutenberg page holds 43 CHARM-GUARD windows and 32 DISCIPLINE matches (amulet, amulets, bulla, charm, charms, evil eye, talisman); the Kelsey page holds 8 windows and 6 matches (amulet/amulets). Both clear the 3/2 floors on the whole served page, not just the quote.
- No packages installed or updated for this seat.
- Scope honesty: S637 is Roman lapidary lore about iaspis, not a Graeco-Egyptian gem record; the entry sentence says only that Pliny reports the eastern custom of wearing jasper as an amulet. Do not extend it to "magical gems" as a class. S636 is one steatite Chnoubis amulet in one museum catalogue; its "female reproductive concerns" line is that catalogue's wording, not a general rule for all Chnoubis gems.

## rejected

Opened and not offered (each reason with the tool's own output where a tool result decided it):

1. https://cbd.mfab.hu/cbd/187 — Campbell Bonner Magical Gems Database, "Magical gem: Chnoubis (A) Ἀβρασάξ (B)", CBd-187. Opened live: `200 17395 text/html; charset=UTF-8`. Rejected on TOPIC: the record is a databank stub (collection, inventory, material "chalcedony (colour unspecified)", dimensions, dating, iconography "Chnoubis?", the two face descriptions and a bibliography) with no protective-object language; computed on the served page: `b17497e5.html chars 7375 page_hits 1 terms 1 ['talismans']` — the single term is the site label "Talismans", the single window is that label, so page_hits 1 < 3 and the quote side has no protective sentence to teach from. Directly on subtopic (Chnoubis + Abrasax on one stone) but unusable as a row.
2. https://nds.museum-digital.de/object/79968?navlang=en — Museum August Kestner (Hanover), "Chnoubis, so called magical gem", K 1576. Opened live: `200 23931 text/html; charset=UTF-8`; English text read in full. It carries the best lapidary statement I found — "The choice of stone for the magical gems was not random … Galenos … had cured his own stomach problem with a green jasper even without the chnoubis representation usually used for these ailments. The lion-headed and serpentine Chnoubis was considered the 'Lord of the Stomach.'" — but the page never uses an amulet/talisman/apotropaic term and holds one window: `cand4.html chars 4104 page_hits 1 terms 0 []`. TOPIC would fail (needs 3 windows and 2 discipline terms). Rejected mechanically, not editorially; a future round with a wider DISCIPLINE set could use it.
3. https://quod.lib.umich.edu/s/sclamulets — University of Michigan, "The Campbell Bonner Collection of Magical Amulets". Live fetch: `403 5562 text/html; charset=UTF-8` (block page, no record text served). Not opened, so not quotable; no ordinary public copy of the 61-object catalogue was tried further.
4. https://collections.carlos.emory.edu/objects/25008/intaglio-gem-depicting-chnoubis — Michael C. Carlos Museum, "Intaglio Gem Depicting Chnoubis". Live fetch: `202 0 text/html; charset=UTF-8` (zero-byte challenge response). Nothing served to read; not quoted.
5. https://www.mfab.hu/artworks/6970/ — Museum of Fine Arts Budapest, "Magical gem with Anguipes and Chnoubis". Live fetch: `520 16 text/plain; charset=UTF-8`. Not served; not quoted.
6. https://core.ac.uk/download/pdf/43660338.pdf — Dasen, "Magic and Medicine: Gems and the Power of Seals" (Gems of Heaven volume), open PDF via CORE. Live fetch: `CORE 403 5576 text/html; charset=UTF-8` (bot challenge). Challenge met, not passed; rejected rather than worked around.
7. https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Pliny_the_Elder/37*.html — guessed LacusCurtius URL for Pliny Book 37. Fetch: `404 49`. No such page; the Book 37 text was taken from Project Gutenberg instead (S637).
8. https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.02.0138%3Abook%3D37 — Perseus, Pliny *Natural History* Book 37. Opened live: `200 2087022` (2,087,022 bytes). Rejected because the served text is the Latin (Mayhoff) text, not the English translation: the only amulet passages are Latin, e.g. "infantibus adalligari amuleti ratione prodest" and "totus vero oriens pro amuleto gestare eas traditur" (8 `amulet` string matches, all Latin). A Latin quote cannot bind two content stems to an English teaches cell or entry line; the English Bostock–Riley translation on Gutenberg (S637) carries the same passage.
9. https://echoesofegypt.peabody.yale.edu/egyptosophy/magical-gems-including-magical-gem-serapis-uroboros-and-incantations — Yale Peabody Museum, *Echoes of Egypt*, "Magical Gems including 'Magical Gem' with Serapis, Uroboros, and Incantations". Opened live: `YALE 200 41734 text/html; charset=utf-8`; served text holds `chars 7658 page_hits 7 terms 7 ['amulet', 'amuletic', 'amulets', 'magic bowls', 'magical papyri', 'magical papyrus']`, and its opening sentence — "Earlier Egyptian amuletic traditions reach a culmination in the Graeco-Egyptian magical amulets, in which image, text, and object interact more intensely than ever before." — would pass all four legs. Rejected only for the two-id slot: I kept one object record (S636) and one primary text on material choice (S637), which cover "what it protects against / how the figure is read" and "what it is made of and why" without overlapping. This page is the strongest free slot for a later round on how image, text and object combine.
10. https://diskoproject.kelsey.lsa.umich.edu/about/ — DiSKO project page, opened live `200 135737` to check who writes the object descriptions: "DiSKO stands for the Digital Study of Kelsey Objects Project … intended to be a resource for teaching and research." Confirms no named author for the catalogue text (used in the S636 tier note), but it is not itself a source about protective objects.
11. https://diskoproject.kelsey.lsa.umich.edu/about-disko/ — guessed project URL; fetch `404 96168` (WordPress "Page not found"). Not a source.
12. https://web.archive.org/web/20260831093908id_/https://www.gutenberg.org/cache/epub/62704/pg62704-images.html — Wayback capture of the S637 page. Fetched with curl `P 200 955802 text/html; charset=utf-8`, but the captured body does not carry Book XXXVII: `pliny locate: False chars 736659 page_hits 0 terms 0`. A capture that cannot vouch for the quote is not listed in the row.
13. https://collectionapi.metmuseum.org/public/collection/v1/search?q=magical%20gem — Met Collection API search used only to locate candidate objects. Fetch: `410 438`; no Met record was opened, so no Met row was offered.

Nothing else was opened. Two of the rejected pages (CBd-187, Kestner 79968) are on subtopic and would be the first re-checks in a later round if the discipline-term set widens.
