# ScoutDragonLong — the long and the European dragon are not one creature

- seat: `KotodamaR55.ScoutDragonLong` (scout, claim C ground: monsters and hybrid beings)
- round: kotodama 55 (hyaku phase 4), 2026-10-22
- lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, declaration `8eda9543e940bdc4938fad90182ee6a6fe271d0f`, claim base `f4015e70b829523ed81e14ce4279bfab0e0233e4`
- assignment: calibration item — a Chinese *long* and a European dragon are not one creature; open holding-museum records or official museum essays that say what each stood for in a named period, quote each record, aim draft sentences at design decisions
- draft ids used below: `NEW-ScoutDragonLong-1` … `-5`; the L1 assigns the final `S` ids at integration
- all five rows were opened this session by ordinary means; every quote below was re-checked by substring match against the fetched bytes (0 misses) and is at most 25 words

## Route summary

| # | source | route | status |
|---|---|---|---|
| 1 | Cleveland Museum of Art, *Jar with Dragon Design*, 1986.85 (Korea, Joseon) | `openaccess-api.clevelandart.org` record, plain request | HTTP 200, CC0, no challenge |
| 2 | Victoria and Albert Museum, *Robe* (emperor's dragon robe), T.12-1950 | collection page plus the museum's JSON record | HTTP 200 both, no challenge |
| 3 | Aberdeen University Library MS 24, folio 66r (dragon, continued) | project page with Latin transcription and English translation | HTTP 200, no challenge |
| 4 | The Met, "Animals in Medieval Art" (Holcomb and Boehm) | live page refused; Wayback capture | live HTTP 429; capture 20250415163651 HTTP 200 |
| 5 | Cleveland Museum of Art, *Dragon and Tiger*, 1959.136.1 (Japan) | `openaccess-api.clevelandart.org` record, plain request | HTTP 200, CC0, no challenge |

The contrast the calibration asks for is carried by rows 1, 2, 3 and 5 together: on the East Asian side the being is
named for rain and for rulership and is drawn on vessels and court dress (rows 1, 2, 5); on the Latin Christian side
the being is a serpent read as the Devil, born in Ethiopia and India, and written into a moralising book (row 3, with
the genre framed by row 4). Nothing in either set of records describes the other's being.

---

### NEW-ScoutDragonLong-1

citation: Cleveland Museum of Art, "Jar with Dragon Design", accession 1986.85, Korea, Joseon dynasty (1392–1910), 1700s, porcelain with underglaze cobalt decoration, CC0; collection record and description, no author or publication date on the record.

url: https://openaccess-api.clevelandart.org/api/artworks/153401 (the public object page is https://clevelandart.org/art/1986.85; the two text fields quoted are `description` and `did_you_know` in that JSON)

route: direct plain request (curl) to the museum's open-access API, HTTP 200, no challenge, no login, 2026-10-22

kind: record

tier: A — the holding museum's own catalogue record for its object; authoritative for the object's fields and for the description the museum itself publishes. The rain-and-rulership sentence is the museum's own summary sentence, not a dated argument with a cited source, so the row supports "this museum says", not "this was universally believed".

scope: one Korean Joseon jar — the being as rain-maker and as a symbol of rulers in premodern East Asia, the flaming wish-granting jewel it pursues, the court use of the short and the tall jar types, and the 1700s date. It is a Korean object and the record speaks of premodern East Asia, not of China; it says nothing about the being's body parts, its enemies, or popular as opposed to court use.

quotes:
- description, first sentence: "As a mythical creature believed to make rain, the dragon served as a symbol of rulers in premodern East Asia."
- description, second sentence: "Here, a cobalt blue dragon is depicted flying through clouds to catch a flaming, wish-granting jewel called a cintamani."
- description, third sentence: "In the royal court, the shorter type of dragon jar held wine, while the tall type, like this one, held flowers."
- did you know, second clause: "the image of dragons was used exclusively for the king's paraphernalia"

teaches: A Korean court jar's museum record gives the being two jobs at once, making rain and marking royal authority, and a jewel to pursue.

draft sentences:
- Decide the being's power before its temper: this Korean jar's record calls the creature one believed to make rain, and only then a symbol of rulers (NEW-ScoutDragonLong-1, description, first sentence).
- Give the being something to chase rather than only something to fight: on this jar it flies through clouds after a flaming wish-granting jewel (NEW-ScoutDragonLong-1, description, second sentence).
- Let the image sit on vessels of different court uses, since the short jar held wine and the tall jar held flowers (NEW-ScoutDragonLong-1, description, third sentence).
- Keep the rain power separate from the rank restriction: the record says the dragon image was used exclusively for the king's paraphernalia (NEW-ScoutDragonLong-1, did you know, second clause).
- Date the pairing before generalising it, because this is a Joseon-dynasty jar of the 1700s, not a timeless East Asian arrangement (NEW-ScoutDragonLong-1, record fields `culture` and `creation_date`).

---

### NEW-ScoutDragonLong-2

citation: Victoria and Albert Museum, London, "Robe" (dragon robe for an emperor), accession T.12-1950, made in China 1750–1800, Qing dynasty, satin-weave silk with silk and metallic-thread embroidery, silk-damask lining, given by the Forrer Family; record created 25 June 2009, last modified 8 June 2026.

url: https://collections.vam.ac.uk/item/O498858/robe-unknown/ (page text; corroborated field by field by the museum's own JSON record at https://api.vam.ac.uk/v2/museumobject/O498858)

route: direct plain request (curl), HTTP 200 on both the page and the JSON record, no challenge, 2026-10-22

kind: record

tier: A — the holding museum's record of its own object; authoritative for materials, date, measurements and for the summary of imperial dress rules the museum publishes. It is not a decree: the record cites no statute and gives no rank table for other wearers.

scope: one Qing emperor's robe — the bright-yellow restriction, the Twelve Imperial Symbols of Sovereignty of which the dragon is one, five-clawed dragons on front and back, the hem border of earth, sea and rocks, the clouds, bats and swastikas scattered over the silk, and the 1750–1800 date. Says nothing about dragons and rain, nothing about earlier dynasties, and nothing about who below the emperor could wear a dragon.

quotes:
- Summary, first sentence: "In imperial China, official dress was highly regulated."
- Summary, second sentence: "Only the emperor and empress were allowed to wear bright yellow."
- Summary, on the symbol set: "Robes made for the emperor featured the Twelve Imperial Symbols of Sovereignty"
- Summary, closing sentence: "These represent the emperor's righteous reign."
- Physical description: "There are five-clawed dragons on the back and front, and a deep hem border of earth, sea and rocks."
- Physical description, on the rest of the field: "There are cloud forms scattered all over, along with bats, swastikas and the 'Twelve symbols'."

teaches: On a Qing emperor's robe the dragon is one item in a fixed set of sovereignty symbols, five-clawed, under a colour restriction.

draft sentences:
- Treat a dragon on clothing as a licence rather than decoration: official dress was regulated and only the emperor and empress could wear bright yellow (NEW-ScoutDragonLong-2, Summary).
- Put the being inside a closed set instead of loose on the field, since the dragon is one of the Twelve Imperial Symbols of Sovereignty that stand for the emperor's righteous reign (NEW-ScoutDragonLong-2, Summary).
- Count the claws and place the ground: this robe carries five-clawed dragons on front and back above a hem border of earth, sea and rocks (NEW-ScoutDragonLong-2, Physical description).
- Decide what else the garment may carry, because clouds, bats and swastikas are scattered across the silk beside the symbols (NEW-ScoutDragonLong-2, Physical description).
- Date the convention: the museum dates this robe 1750–1800, so the five-claw rule here is a late imperial arrangement, not a timeless Chinese one (NEW-ScoutDragonLong-2, record fields `productionDates`, 1750–1800, and `styles`, Qing).

---

### NEW-ScoutDragonLong-3

citation: Aberdeen University Library, MS 24 (the Aberdeen Bestiary), folio 66r, England, c. 1200; digitised with Latin transcription, English translation and the project's editorial commentary by the University of Aberdeen Bestiary Project. No author or publication date on the page.

url: https://www.abdn.ac.uk/bestiary/translat/66r.hti

route: direct plain request (curl), HTTP 200, 15,121 bytes, no challenge, 2026-10-22

kind: book

tier: A — the holding library's digitisation of its own leaf, printing the Latin transcription beside its English translation; primary for this folio's text. The English wording is the project's rendering, so a claim about the English phrasing is a claim about that translation.

scope: the dragon chapter's continuation — the tail of its etymology, the cave-and-air behaviour, the body (crest, small mouth, narrow blow-holes, strength in the tail, freedom from poison), the elephant killing, the birthplaces Ethiopia and India, and the devil allegory read clause by clause. It does not carry the chapter's opening sentences, which stand on folio 65v (already quoted in `.ufo/waves/round-55/build/ScoutBestiaryAberdeen.md`), and it says nothing about dragons outside this text.

quotes:
- translation, Of the dragon: "The dragon, it is said, is often drawn forth from caves into the open air, causing the air to become turbulent."
- translation, Of the dragon: "The dragon has a crest, a small mouth, and narrow blow-holes through which it breathes and puts forth its tongue."
- translation, Of the dragon: "Its strength lies not in its teeth but in its tail, and it kills with a blow rather than a bite."
- translation, Of the dragon: "Dragons are born in Ethiopia and India, where it is hot all year round."
- translation, Of the dragon: "the dragon knots its tail around their legs and kills them by suffocation"
- translation, Of the dragon, the allegory: "The Devil is like the dragon; he is the most monstrous serpent of all"

teaches: This dragon is crested with a small mouth and force in the tail, is born in Ethiopia and India, and is read as the Devil.

draft sentences:
- Put the monster's homeland on the map: this dragon is born in Ethiopia and India, where it is hot all year round, so it belongs to a real region and a real climate (NEW-ScoutDragonLong-3, translation, Of the dragon).
- Choose which organ does the killing: the text gives a crest, a small mouth and narrow blow-holes, and puts the strength in the tail, not the teeth (NEW-ScoutDragonLong-3, translation, Of the dragon).
- Give the body an effect on the weather rather than only on people, since drawn from its cave it makes the air turbulent (NEW-ScoutDragonLong-3, translation, Of the dragon).
- Match the prey to the body: it waits on the paths elephants use, knots its tail round their legs and suffocates them (NEW-ScoutDragonLong-3, translation, Of the dragon).
- State the reading the book attaches, because this dragon is the Devil, the most monstrous serpent, so its danger is doctrinal as well as physical (NEW-ScoutDragonLong-3, translation, Of the dragon, the allegory).

---

### NEW-ScoutDragonLong-4

citation: Melanie Holcomb and Barbara Drake Boehm, "Animals in Medieval Art", in *Heilbrunn Timeline of Art History*, New York: The Metropolitan Museum of Art, October 1, 2001, revised January 1, 2012.

url: https://web.archive.org/web/20250415163651id_/https://www.metmuseum.org/essays/animals-in-medieval-art (the live URL is https://www.metmuseum.org/essays/animals-in-medieval-art)

route: the live page returned HTTP 429 (rate limited) to a plain request; the essay was read from Wayback capture 20250415163651, HTTP 200, 2026-10-22, and no challenge was presented or circumvented

kind: web

tier: B — a curatorial essay that summarises scholarship for a general audience; authoritative for what the Met publishes as its overview of the genre, not primary for any bestiary text. Rated B under QUALITY criterion 6.

scope: when and from what the bestiary genre developed, its stated double purpose, the passage of its fabulous creatures into medieval art, and the point that exotic animals also reached Europe as gifts and war treasure rather than only through books. It does not interpret the dragon itself and gives no single manuscript.

quotes:
- section "The Bestiary", first paragraph: "The Bestiary developed in medieval Europe in the twelfth century."
- section "The Bestiary", first paragraph, on the genre: "a collection of descriptions and interpretations of animals, intended as both a natural history and a series of moral and religious lessons"
- section "The Bestiary", second paragraph: "bestiaries offered tales about the existence of bizarre and loathsome creatures, many of which appeared in medieval art"
- section "Exotic Animals", first paragraph: "such beasts were sometimes sent as diplomatic gifts to European rulers or brought back as treasure from pilgrimage or Crusade"

teaches: The Met dates the bestiary to twelfth-century Europe as a moralised natural history whose fabulous creatures entered art, and whose exotic animals also arrived as gifts.

draft sentences:
- Choose the book's double purpose deliberately: a bestiary is a natural history and a series of moral lessons at once, so its dragon chapter is meant to teach as well as to describe (NEW-ScoutDragonLong-4, section The Bestiary, first paragraph).
- Date the form being imitated, since the Met places the bestiary's development in twelfth-century Europe and not in antiquity (NEW-ScoutDragonLong-4, section The Bestiary, first paragraph).
- Plan how the creature leaves the book, because bestiary tales of bizarre and loathsome creatures passed into medieval art and had a second life in images (NEW-ScoutDragonLong-4, section The Bestiary, second paragraph).
- Do not derive every monster in the art from a book, since exotic beasts also arrived as diplomatic gifts, pilgrimage souvenirs and crusade treasure (NEW-ScoutDragonLong-4, section Exotic Animals, first paragraph).

---

### NEW-ScoutDragonLong-5

citation: Cleveland Museum of Art, "Dragon and Tiger", accession 1959.136.1, Japan, Muromachi period (1392–1573) to Momoyama period (1573–1615), c. 1546–56, painting, CC0; collection record and description, no author or publication date on the record.

url: https://openaccess-api.clevelandart.org/api/artworks/135593 (the public object page is https://clevelandart.org/art/1959.136.1; the text quoted is `description` and `did_you_know` in that JSON)

route: direct plain request (curl) to the museum's open-access API, HTTP 200, no challenge, 2026-10-22

kind: record

tier: A — the holding museum's record for its own object and the description it publishes; scoped to what that description says. The cosmology sentence is the museum's summary of Chinese cosmology, quoted about a Japanese painting, so the row is not evidence about Chinese practice or Chinese objects.

scope: how one museum reads a Japanese dragon-and-tiger painting through Chinese cosmology — dragons producing rain clouds, the dragon passing in and out of cloud, the wave below read as water pulled toward the sky, and the Chinese Ming models behind the painter. It is a Japanese object; it carries no Chinese ritual, no Chinese date and no dragon anatomy.

quotes:
- description, first sentence: "In Chinese cosmology, dragons produce rain clouds."
- description, second sentence: "The dragon disappearing into and reemerging from clouds in this painting seems to generate rough waves in the water below, pulling it toward the sky."
- did you know: "may have taken inspiration from Chinese Ming-dynasty works in the style of 13th-century Chinese painter Chen Rong"

teaches: A Japanese painter's dragon carries Chinese cosmology, in which dragons make rain clouds, and the museum reads the painted wave as water pulled skyward.

draft sentences:
- Let the body make weather: in the Chinese cosmology the museum reports, dragons produce rain clouds, so a dragon can be depicted as a cause rather than a character (NEW-ScoutDragonLong-5, description, first sentence).
- Show the effect inside the picture, since the dragon passes into and out of cloud while the rough water below seems pulled toward the sky (NEW-ScoutDragonLong-5, description, second sentence).
- Decide how far a meaning travels with a motif: a Japanese painter of the 1540s–50s worked from Chinese Ming models, so the rain-making reading crossed a border with the image (NEW-ScoutDragonLong-5, did you know).

---

## Calibration: two beings behind one English word

Observed in the records above, not inferred from general knowledge:

| | East Asian side (rows 1, 2, 5) | Latin Christian side (rows 3, 4) |
|---|---|---|
| what the being is for | makes rain; symbol of rulers; one of the imperial sovereignty symbols | read as the Devil; a lesson attached to a natural description |
| where the words sit | on a court jar and on an emperor's robe; a Japanese painting carrying Chinese cosmology | in a moralising book of animals, written and illuminated in England around 1200 |
| body | not described in these records | crest, small mouth, narrow blow-holes, force in the tail, no poison |
| where it lives | in cloud, over water | born in Ethiopia and India, drawn out of caves |
| who is restricted | the image: king's paraphernalia; bright yellow for emperor and empress only | the reading: the creature is doctrine, so its danger is moral |
| period of the record | Joseon 1700s; Qing 1750–1800; Japanese painting c. 1546–56 | England, c. 1200, in a genre the Met dates to the twelfth century |

What the records do **not** support: that the *long* and the European dragon share a body plan, a habitat, a moral
valence or a social function. The English word "dragon" is a translator's label over unlike beings. Three of the five
rows are records of objects in which the being is beneficial or rank-bearing; one row is a book in which the being is
the Devil.

## Design decisions this seat can source

| decision | source in this report |
|---|---|
| what the culture calls the being and what the word means | row 1: a creature "believed to make rain" and "a symbol of rulers"; row 2: one of the Twelve Imperial Symbols of Sovereignty; row 3: the Latin chapter read as the Devil |
| how its body is composed | row 3 only: crest, small mouth, narrow blow-holes, tail-strength, freedom from poison. No opened record in this seat describes the *long*'s composite body (see gaps) |
| where it lives relative to the known world | row 3: born in Ethiopia and India, in heat; row 5: in cloud, above water it pulls skyward |
| whether it warns, guards, punishes, teaches or devours | row 3: strangles elephants and is read as the Devil (devours and teaches); row 1 and row 2: marks rank and brings rain (neither warns nor devours); row 5: causes weather |
| who records or depicts it, in what book or object | rows 1 and 2: court ceramics and court dress, catalogued by holding museums; row 3: a moralising animal book; row 4: the genre that book belongs to and its passage into art |
| what changes across periods | row 4: the genre's twelfth-century formation; row 2: a 1750–1800 Qing arrangement; row 5: a Japanese painter of the 1540s–50s reworking Chinese Ming models |

## Overlap, gaps and routing notes for the L1

1. **Overlap with `ScoutBestiaryAberdeen.md`.** That seat opened folio 65v and quoted the dragon chapter's closing
   address to the reader ("the dragon, the serpent of old") plus the illustration note, but did not register a row for
   it. My row 3 is the continuation on folio 66r, a different URL. The L1 should either file row 3 alone (with the 65v
   quotes left where they are) or file one merged dragon row listing both folio URLs in its `url:` line — not two rows
   that both claim the Aberdeen dragon, which would pad FLOOR with one source counted twice.
2. **No duplication with `CriticCalibrationMonsters.md`.** That report's dragon row is Britannica (tier B, cover-term
   argument). A grep of `corpus/SOURCES.md` for the five hosts and paths in this report returns 0 hits, so each of the
   five draft rows is a new URL for the registry; none appears in the other build reports I searched for museum domains.
3. **Gap: the *long*'s composite body.** No opened museum record in this seat describes horns, scales or claws. If the
   entry wants "the being is assembled from other animals' parts" for the Chinese side, another seat's source must
   carry it; my rows only carry the Aberdeen body for the European side, and the Aberdeen leocrota row in
   `ScoutBestiaryAberdeen.md` carries the part-list technique.
4. **Gap: a Chinese holding museum.** The Palace Museum, Beijing, would be the natural authority for the *long* as an
   imperial emblem, and the National Palace Museum, Taipei, for its painting. Neither could be reached by ordinary
   means this session (see `unopened`). The Chinese-side statements in rows 1 and 5 are therefore a Korean record and
   a Japanese record speaking about East Asia and about Chinese cosmology respectively; the entry must attribute them
   that way and not as Chinese institutional claims.
5. **Row numbering for the claim.** Five distinct URLs, five distinct rows, all above S285. Each draft id is used only
   inside its own row's draft sentences.

## Not run

`python3 -B reports/round-55/accept-c.py` was not run: the entry is not landed, so every leg would only re-measure the
base. No file in the lane was created or modified except this report. No tool was installed or upgraded. Quote checks
run: substring match of every quote against the fetched bytes (all true) and a word count of every quote (maximum 25).

unopened:
- https://www.metmuseum.org/essays/animals-in-medieval-art — live URL returned HTTP 429 (rate limited) to a plain
  request; read through the Wayback capture instead (row 4). Recorded as rate limiting, not a challenge.
- https://www.britishmuseum.org/collection/object/A_1936-1012-1 and the British Museum collection search — live pages
  returned HTTP 403 with a Cloudflare interstitial ("Just a moment"): challenge met, not passed. No British Museum row
  was attempted from a capture, because the V&A and Cleveland records already carry the two East Asian claims.
- https://www.npm.gov.tw/en/ (National Palace Museum, Taipei) — HTTP 403 Cloudflare interstitial: challenge met, not
  passed; not routed around.
- https://asia.si.edu/search/?q=dragon (Smithsonian National Museum of Asian Art) — HTTP 403; no record opened.
- https://en.dpm.org.cn/ (Palace Museum, Beijing, English) — HTTP 502; https://intl.dpm.org.cn/article/list.html —
  HTTP 404; the Palace Museum's English landing, explore and culture pages opened (HTTP 200) but carried no dragon
  text, so no row.
- https://collections.mfa.org/search/objects/dragon (Museum of Fine Arts, Boston) — HTTP 202 with an empty body; the
  collection search renders by script and no record text came back.
- https://www.metmuseum.org/art/collection/search/69974 (Met dragon robe) — live HTTP 429; the Met's collection API
  returned metadata only (accession 52.126.23, "Robe, Dragon", Qing dynasty) with no description field, so there was
  no quotable sentence and the V&A robe was used instead.
- https://www.abdn.ac.uk/bestiary/ms24/64v, /bestiary/description, /bestiary/about — 404s on those exact paths; the
  page that exists is `/bestiary/about.php`, read by `ScoutBestiaryAberdeen` and not needed again here.
