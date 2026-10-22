# ScoutMexicaMosaic — Teotihuacan stone masks and Mixtec-Aztec turquoise mosaic masks

Assigned question: what do the holding museums' own records say about a Teotihuacan
stone mask and a Mixtec-Aztec turquoise mosaic mask — material, date range, and what
the record says the mask was for (including where the record says the use is unknown)?

Round 54, lane `kotodama-shokunin`, base `260c68d`, access date 2026-10-22. Every quote
below was checked as an exact substring of the bytes fetched in this session; no quote
joins two fragments.

Result in one line: the Cleveland record gives a 1–550 CE greenstone Teotihuacan mask
tied through holes at the back, perhaps to a dressed body-shaped form with a headdress,
its eyes and mouth once inlaid; the Museum of Ethnography in Budapest, through its own
account of the investigations on its mask, gives an inventory line of type and materials
only, a late fifteenth to early sixteenth century date from alder wood with turquoise
tesserae set in pine resin, a probable Mixtec workshop for Aztec-period central Mexico,
and a suggested function inside a healing or mortuary bundle concealed in a dry cave on
the Puebla–Oaxaca border. The British Museum record for the turquoise mosaics could not
be opened: the site answered with a bot challenge on two plain requests, and no ordinary
copy was reachable this session.

### NEW-ScoutMexicaMosaic-1

citation: Cleveland Museum of Art (n.d.), collection record "Mask", accession 1942.1094,
Central Mexico, Teotihuacán, Classic period, 1–550 CE, greenstone; record read through
the museum's public artwork page and its open-access API record 121226.

url: https://www.clevelandart.org/art/1942.1094 (record also served as JSON at
https://openaccess-api.clevelandart.org/api/artworks/121226)

route: direct plain request, HTTP 308 then 200 at `www.clevelandart.org`
(79,617 bytes, server-rendered HTML, 2026-10-22); the JSON record returned HTTP 200.

kind: record.

tier: A — the holding museum's own catalogue record for the object it holds, and the
description is that museum's text; scope is limited to what this record states. Note:
the same opening sentence heads several of the museum's Teotihuacan mask records
(121226 greenstone, 127766 stone, 103046 ceramic, 155509 stone), so the description is
a note on the type, not a find report.

scope: this mask's date (1–550 CE), culture label (Central Mexico, Teotihuacán, Classic
period), medium (greenstone) and the museum's statements that masks of the type were
tied to something through holes at the back — perhaps a body-shaped form dressed in
garments, ornaments and a headdress — and that eyes and mouths once held inlays. It
does not carry: a findspot, an owner, a ceremony, a wearer, or any statement that the
mask was worn on a living face.

quotes:
- Object data: "1–550 CE"
- Description: "Many Teotihuacán masks were once tied to something via holes on the back"
- Description: "perhaps a body-shaped form dressed in garments, ornaments, and a headdress that identified the figure"
- Description: "The stone masks’ eyes and mouths once held inlays representing irises, pupils, and teeth."

teaches: a Teotihuacan stone mask is a dated greenstone face that the museum reads as
tied through back holes to a dressed, body-shaped form, with eyes and mouth built from
materials that are no longer present; the record does not say it was worn on a face.

draft sentences:
- The Cleveland record dates its greenstone mask 1–550 CE and files it under Central
  Mexico, Teotihuacán, Classic period, so a builder who wants one "Teotihuacan mask"
  inherits a five-century range and a culture label rather than a moment.
  (NEW-ScoutMexicaMosaic-1, Object data)
- The record reads the holes at the back as points where the mask was tied to
  something, perhaps a body-shaped form dressed in garments, ornaments and a headdress
  that identified the figure, so the museum's own guess puts the mask on a constructed
  body rather than on a face. (NEW-ScoutMexicaMosaic-1, Description)
- Eyes and mouth once held inlays for irises, pupils and teeth, so the face the museum
  describes was assembled from more than one material and the surviving stone is a
  partial face. (NEW-ScoutMexicaMosaic-1, Description)
- The same note heads several of the museum's Teotihuacan mask records, so this is the
  museum's statement about the type, and a builder should treat the tying as a class
  reading rather than an excavation finding. (NEW-ScoutMexicaMosaic-1, Description;
  compare records 127766, 103046, 155509)

### NEW-ScoutMexicaMosaic-2

citation: Museum of Ethnography (Néprajzi Múzeum), Budapest, "Aztec Mosaic Mask in the
Museum of Ethnography", museum news article, 2022 (page footer © 2022), reporting
investigations by the museum's specialist János Gyarmati with Hungarian and Leiden
laboratories.

url: https://www.neprajz.hu/en/hirek/2022/aztec-mosaic-mask-in-the-museum-of-ethnography.html

route: direct plain request, HTTP 200, 45,311 bytes, server-rendered HTML, 2026-10-22.

kind: web.

tier: A — the holding museum's own published statement about its own object and the
investigations carried out on it; limit: the article reports the archaeometry, the
laboratory reports themselves were not opened, and no inventory number is given.

scope: the museum's inventory wording for the mask, the materials it names for the
object and for the setting of the tesserae, the date range the investigations produced,
the attribution of the workmanship, the museum's suggested function of the ensemble it
belonged to, the reported find area, and the acquisition history. The healing-or-
mortuary reading is the museum's own suggestion ("suggesting"), not an excavated
context.

quotes:
- Paragraph on acquisition: "The entry in the museum’s inventory states merely: mosaic mask, Mexico, Mixtec; material: wood, turquoise, shell."
- Paragraph on the investigations: "The results revealed that the mask dates from the late fifteenth to early sixteenth century"
- Paragraph on cultural research: "the mask formed part of a healing or mortuary bundle, which was a figurine representing the gods or ancestors"
- Opening paragraph: "The first objects of this kind were brought back to Europe in 1533 by Dominican missionaries to Mexico"

teaches: a turquoise mosaic mask can enter a museum as a bare inventory line of type and
materials, be dated by its wood and resin, be attributed to Mixtec hands within
Aztec-period central Mexico, and be read by its holder as part of a wrapped deposit of
gods or ancestors hidden in a cave.

draft sentences:
- The Budapest inventory entry reads only "mosaic mask, Mexico, Mixtec; material: wood,
  turquoise, shell", so this mask entered a collection as a type and a material list,
  with no finder, place or owner attached. (NEW-ScoutMexicaMosaic-2, paragraph on
  acquisition)
- The investigations date the mask to the late fifteenth to early sixteenth century,
  identify an alder species native to Mexico, and find pine resin holding the tesserae,
  which fixes both the period and the method of setting the mosaic.
  (NEW-ScoutMexicaMosaic-2, paragraph on the investigations)
- The museum calls the turquoise genuine and the work probably that of Mixtec master
  craftsmen, so the mask as described is Aztec-period central Mexican work that the
  museum attributes to Mixtec craftsmen. (NEW-ScoutMexicaMosaic-2, opening paragraph)
- The museum suggests the mask formed part of a healing or mortuary bundle, a figurine
  representing gods or ancestors, concealed in a dry cave, which is a suggested setting
  rather than a recovered one. (NEW-ScoutMexicaMosaic-2, paragraph on cultural research)
- Museum documentation places related ensembles in caves on the Puebla–Oaxaca border,
  records that dealers sold very similar ensembles to museums in Belgium, Germany and
  America, and says this mask may have come to dealers during excavations there in the
  1960s, so the findspot is reconstructed from other collections.
  (NEW-ScoutMexicaMosaic-2, paragraphs on cultural research and the final paragraph)
- The same page records that the first objects of this kind reached Europe in 1533 as a
  gift to Pope Clement VII in an attempt to prove the conquered Mexicans were an
  advanced civilisation capable of sophisticated works of art, which is a documented
  later life for such a mask as an argument carried in an embassy.
  (NEW-ScoutMexicaMosaic-2, opening paragraph)

### Notes for the entry

The two rows answer different halves of the brief and should not be merged. Row 1 gives
the stone-mask half with a museum's own hedge ("perhaps a body-shaped form"): the mask
is a face for something built and dressed, and its identity depends on inlays that are
gone. Row 2 gives the mosaic half with its strong statements on who makes (probable
Mixtec hands), what the object is said to be (a figurine of gods or ancestors inside a
bundle), where it is said to appear (a dry cave on the Puebla–Oaxaca border, reachable
only through other museums' documentation), and how a mask changes audience
(1533 papal gift). Neither page says anyone spoke through a mask, so the entry must not
claim a spoken voice for these two cases; the licensed-voice material has to come from
other seats. On restriction, the Budapest page compares the turquoise's high zinc and
low iron content to turquoise found in the Templo Mayor precinct and stops there; no
opened source states an access rule for either mask, so the entry should not invent one.
The British Museum's own record for Am,St.400 — the mask most often used to
illustrate "Aztec turquoise mosaic mask" — was not opened, and no sentence in the entry
should be sourced to it from memory or from search snippets.

unopened:
- British Museum collection records https://www.britishmuseum.org/collection/object/E_Am-St-400
  and .../E_Am-St-396: two plain requests (a browser user agent and curl's default)
  returned HTTP 403 with page title "Just a moment..." (5,530–5,701 byte challenge
  pages). Challenge met, not passed; nothing from these pages is quoted, and a search
  snippet describing Am,St.400 was read but is not treated as evidence.
- Ordinary copies of the British Museum pages: `archive.org/wayback/available` returned
  no snapshot for the E_Am-St-396 URL, and both `archive.org` and `web.archive.org`
  served "Internet Archive services are temporarily offline" during this session, so no
  Wayback capture could be read.
- British Museum ResearchSpace SPARQL and resource endpoints
  (https://collection.britishmuseum.org/sparql): connection timed out, HTTP 000, twice
  at 30 s and once at 60 s.
- Metropolitan Museum of Art: object pages returned HTTP 429 on two attempts; the open
  API answered (object 310647 is a Teotihuacan travertine mask, 300–600 CE; 310650 an
  Aztec earflare disk in wood and turquoise; 313255 a Mixtec serpentine "Rain god mask",
  1325–1521) but carries no descriptive text for any of them, so the API alone could not
  answer the use question and was not made into a row.
- Other museum routes tried and not opened: Art Institute of Chicago API (HTTP 403),
  Yale University Art Gallery (HTTP 403 challenge), Penn Museum (HTTP 403), FAMSF (HTTP
  403 challenge), Brooklyn Museum (429 Vercel checkpoint), Museo Nacional de Antropología
  `mna.inah.gob.mx` (HTTP 468 SafeLine block), CERES/Museo de América Madrid (HTTP 429
  on three attempts), NMNH anthropology search (JavaScript-only shell), Musée du quai
  Branly collection app (single-page shell, no record reached), LACMA and Dallas Museum
  of Art search (client-side only, no records in the returned HTML), Dumbarton Oaks
  (HTTP 202, empty body).
- No tools were installed or upgraded for this seat.
