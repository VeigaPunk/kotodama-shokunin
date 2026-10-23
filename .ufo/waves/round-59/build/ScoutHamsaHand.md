# ScoutHamsaHand — the protective hand (hamsa / Hand of Fatima / hamesh), S608–S609

Claim C source seat. Subtopic: the protective hand in Jewish and Islamic contexts, museum and scholarly sources.
Two rows offered, ids S608 and S609 only. No installs, no updates, no background jobs this session.
Every fetch below was a plain GET (curl or python urllib) to a public page; no browser, no challenge was bypassed.

## Registry rows

| S608 | Schroeder, Sarah. 2026. "Hand of Fatima", object record in *Explore Islamic Art Collections*, Museum With No Frontiers (Discover Islamic Art virtual museum); object 19th century, Alawid, made in Morocco, Tangier, FBQ Museum, Shahaniya, Qatar, inventory FBQ.HH.358, silver and engraving, 24 x 16 cm — https://islamicart.museumwnf.org/database_item.php?id=object;EPM;qt;Mus22;21;en (direct, HTTP 200, 33124 bytes; no Wayback capture exists for this record URL, checked 2026-10-23) | docs | A | one Moroccan khamsa's named forms, Jewish makers, silver material and two placements, in a Gulf museum object record | locator: "Jewish silversmiths in Morocco became known for casting and engraving pieces such as this one, used as a talismanic doorknob or jewellery pendant." | Moroccan Jewish silversmiths cast and engraved hand-shaped amulets that hung as talismanic doorknobs or were worn as jewellery pendants. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |

| S609 | Kopel, Jonathan. 2022. "The Eye of Providence and the Hamsa in medicine", *Proceedings (Baylor University Medical Center)* 35(2):263-265, DOI 10.1080/08998280.2021.1993114, PMCID PMC8865327, open access — https://pmc.ncbi.nlm.nih.gov/articles/PMC8865327/ (direct, HTTP 200, 112796 bytes); capture https://web.archive.org/web/20250202021811id_/https://pmc.ncbi.nlm.nih.gov/articles/PMC8865327/ | paper | A | the palm-shaped hamsa's two display scales, jewellery worn on the body and wall hangings hung in a room | Abstract, sentence on the hamsa: "In Arabic cultures, the Hamsa is a palm-shaped amulet that is popular in jewelry and wall hangings." | The same palm-shaped hamsa amulet is made as jewellery for wearing and as a wall hanging for display, so scale follows setting. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |

## Gate

- S608 — https://islamicart.museumwnf.org/database_item.php?id=object;EPM;qt;Mus22;21;en — accessed 2026-10-23 — Object description, sentence on makers and use: “Jewish silversmiths in Morocco became known for casting and engraving pieces such as this one, used as a talismanic doorknob or jewellery pendant.” Grounds: Moroccan Jewish silversmiths cast and engraved hand-shaped amulets that hung as talismanic doorknobs or were worn as jewellery pendants. Seat: ScoutHamsaHand.
- S609 — https://pmc.ncbi.nlm.nih.gov/articles/PMC8865327/ — accessed 2026-10-23 — Abstract, sentence on the hamsa: “In Arabic cultures, the Hamsa is a palm-shaped amulet that is popular in jewelry and wall hangings.” Grounds: The same palm-shaped hamsa amulet is made as jewellery for wearing and as a wall hanging for display, so scale follows setting. Seat: ScoutHamsaHand.

## rowcheck output (verbatim, exit 0)

```
S608 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://islamicart.museumwnf.org/database_item.php?id=object;EPM;qt;Mus22;21;en | BOILER: root-clear https://islamicart.museumwnf.org/; not a title, h1 or meta label | RELEVANCE: shared=['doork', 'engra', 'jewel', 'jewis', 'moroc', 'penda'] | TOPIC: quote_hits=1 function_words=7 page_hits=7 page_terms=8 need=1/2/3/2
S609 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://pmc.ncbi.nlm.nih.gov/articles/PMC8865327/ | BOILER: root-clear https://pmc.ncbi.nlm.nih.gov/; not a title, h1 or meta label | RELEVANCE: shared=['amule', 'hamsa', 'hangi', 'jewel', 'palm', 'shape'] | TOPIC: quote_hits=1 function_words=6 page_hits=5 page_terms=27 need=1/2/3/2
```

Command: `cd /fast/scratch/hyaku/kotodama-r59/ScoutHamsaHand && timeout 900 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-59/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r59/ScoutHamsaHand/rows.md --entry /fast/scratch/hyaku/kotodama-r59/ScoutHamsaHand/stub.md`

## draft sentences

Moroccan Jewish silversmiths cast and engraved silver hand pieces that could serve as a talismanic doorknob on a house or as a jewellery pendant on the body (S608).
The same record treats silver as adding amuletic force and reads the engraved phoenix and salamanders as signs of life, rebirth and fertility (S608).
One object carries the names Hand of Fatima, Khamsa and Hand of Venus, so its naming layers an Islamic, a numerical and a classical reading (S608).
The same palm-shaped amulet is worn as jewellery and hung on a wall, so one object type covers a person and a room (S609).
The article places the palm form in Arabic-speaking settings, where the hand is a common amulet rather than a rare one (S609).
Because the palm shape is the same in both uses, a protective sign can move between a body and a room without being redesigned (S609).

Carry note for the L1: S608 sentence 1 is carried by the anchor quote word for word in substance (maker, casting/engraving, doorknob or pendant). S608 sentences 2 and 3 are carried by the same opened page (the silver-as-amuletic-power sentence, the phoenix/salamanders sentence, and the naming block “Hand of Fatima”, “Khamsa”, “Hand of Venus”), not by the anchor quote. S609 sentence 1 is carried by the anchor quote; sentences 2 and 3 are page-level readings of the same article. If the blind SUPPORT reviewer enforces quote-only support for every entry sentence, use each row's sentence 1 only.

## What the opened pages carry beyond the quotes

S608 page (Discover Islamic Art, MWNF, record by Sarah Schroeder; FBQ Museum, Shahaniya, Qatar; object 19th century, Alawid, Morocco, Tangier, silver, 24 x 16 cm, inventory FBQ.HH.358):
- names stacked on one object: “Hand of Fatima”, Khamsa “(the Arabic word for 'Five')”, “Hand of Venus” or “Aphrodite”.
- material rationale: “While silver casts additional amuletic power, the phoenix and salamanders symbolize life, rebirth and fertility.”
- the hand's origin story as the record tells it: “Carthaginian excavations traced the open hand to ancient Egypt ... believed to grant protection against ill will.”
- Islamic reading: Fatima “defends anyone regardless of faith against evil”; the five fingers as “five pillars of Islam, five daily prayers and five keys to the unseen”; the fingers “indistinguishable” in this piece.
- history of the object: “How date and origin were established”, “How Object was obtained: Purchase”.

S609 page (Kopel 2022, Proc (Bayl Univ Med Cent) 35(2):263–265):
- naming: “Khamsa (five in Arabic), hamesh (five in Hebrew), hamesh hand, and chamsa are all names for the Hamsa hand.”
- posture: “The splayed digits of the Hamsa hand can be used to ward off aggressors and to blind evil. To bring good luck, the digits of the Hamsa might be closed together. The digits may be pointing upwards or downwards.”
- sign detail: “The Hamsa hand's palm may have an eye to repel malevolent gazes.”
- dedications: hand of Fatima Zahra in Islam, Hand of Miriam in Judaism; five fingers as the Five Books of Moses.

## Spare (opened, mechanically tested, NOT offered — I hold only S608 and S609)

The British Museum Islamic Gallery record, “Pendant, amulet”, museum number 2014,6009.1, Morocco, 1890s, silver, enamel, glass — https://islamicworld.britishmuseum.org/collection/RRM46563 (direct, HTTP 200, 50495 bytes). Its curator's comments read: “The belief in the protective power of hand amulets dates back millennia.” and “These examples may have been used by Muslims or Jews to ward off the 'eye of envy'.” Tested with a placeholder id in a scratch draft: `S609 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://islamicworld.britishmuseum.org/collection/RRM46563 | BOILER: root-clear https://islamicworld.britishmuseum.org/; not a title, h1 or meta label | RELEVANCE: shared=['amule', 'back', 'hand', 'mille', 'prote'] | TOPIC: quote_hits=1 function_words=3 page_hits=11 page_terms=6 need=1/2/3/2`, exit 0 (no entry file, so the entry legs were not exercised). I did not offer it because its best quotable sentence teaches only the antiquity of the belief, and a second Moroccan khamsa would duplicate S608's region, metal and genre; it is a viable swap if either offered row fails at acceptance.

## rejected (opened this session, not offered)

- https://www.imj.org.il/en/collections/226313-0 and https://www.imj.org.il/en/collections/369214-0 (The Israel Museum, Jerusalem; hamsa records with curatorial text) — `curl: (60) SSL certificate OpenSSL verify result: unable to get local issuer certificate (20)` / `HTTP 000 bytes 0`. A TLS failure cannot be repaired by ordinary means.
- https://collection.sciencemuseumgroup.org.uk/objects/co102789/amulet-hand-of-fatima-in-black-glass-set-in-silver-mount-with-small-suspension-ring — `HTTP 403 bytes 919`.
- https://www.si.edu/object/hand-fatima:chndm_1997-59-2 (Cooper Hewitt) — `HTTP 403 bytes 46496`.
- https://www.brooklynmuseum.org/opencollection/objects/122039 — `HTTP 429 bytes 34217`.
- https://www.metmuseum.org/art/collection/search/316492 — `HTTP 429 bytes 34224`; the Met Collection API endpoint used to find objects, `https://collectionapi.metmuseum.org/public/collection/v1/search?q=hamsa`, answered `METAPI HTTP 410 bytes 438`.
- https://www.britishmuseum.org/collection/object/W_2014-6009-2 — `HTTP 403 bytes 5557` (the Islamic Gallery subdomain served the same object fine; see Spare).
- https://wellcomecollection.org/concepts/zjuw3vp9 — `HTTP 405 bytes 2131`; the Wellcome catalogue API (`api.wellcomecollection.org/catalogue/v2/works?query=hamsa`) returned only unrelated “hams” records (bacon, Sanskrit texts), no hand amulet.
- The Jewish Museum (New York) object records opened at HTTP 200 — /collection/5614-belt-clip-with-amulets (97,531 bytes), /collection/4489-childbirth-amulet (89,612), /collection/29759-amulet-amulet-for-expectant-mother (93,031), /collection/20087-amuletic-necklace (93,234) — but they carry catalogue fields only (“Object Name : Belt Clip with Amulets Place Made : Hamsa: Tunisia ...”); no sentence of body prose to quote, so LOCATE would rest on a field label.
- V&A: `https://api.vam.ac.uk/v2/objects/search?q=hamsa` answered 200 with unrelated records (O1277211 “Raja Hamsa Pal”, O143553 “Ikat length”, O24803 “Sculpture” ...); no hamsa amulet record was found, and the one V&A page opened (O141913) was a theatrical photograph with no protective-object text.
- Khalili Collections site search (`https://www.khalilicollections.org/?s=hamsa`, HTTP 200, 57432 bytes) returned fuzzy matches (“The Tale and the Image Volume Two”, “Falnamah”, “Ewer in the Shape of a Goose or Swan”), no hand amulet.
- Wayback capture `https://web.archive.org/web/20261010064012id_/https://pmc.ncbi.nlm.nih.gov/articles/PMC8865327/` — 8,132 bytes, a Google reCAPTCHA challenge page (`<base href="https://www.google.com/recaptcha/challengepage/">`), not the article; replaced in the row by the 2025 capture 20250202021811 (30,781 bytes, which does carry the quote).
- Wayback availability for the S608 record URL returned `{"url": "islamicart.museumwnf.org/database_item.php?id=object;EPM;qt;Mus22;21;en", "archived_snapshots": {}}`, so the row lists no capture.

## Confidence and unknowns

- S608: high confidence in the verbatim sentence, the maker statement and both placements. The page is a museum object record (MWNF / Discover Islamic Art) rather than a peer-reviewed article; the text is signed “Sarah Schroeder” in the page's own citation line and the site dates itself 2026. Unknown: whether MWNF will keep serving this PHP record without a challenge; the URL answered 200 on three separate GETs today (curl and urllib), but no capture exists as a fallback, so this is the pair's single point of failure.
- S609: high confidence in the verbatim sentence (it sits in the article's abstract) and in the article's metadata (`Proc (Bayl Univ Med Cent) 2022;35(2):263–265`, DOI 10.1080/08998280.2021.1993114, PMCID PMC8865327). Only one sentence on that page passes the CHARM-GUARD window at 10–25 words, so the row's quote is not a matter of choice; the naming and posture material is page-level and must not be attributed to the quote.
- Neither row states a universal: S608 is one Qatari-held, Moroccan-made object; S609 speaks of “Arabic cultures” as the article does, and the entry should not widen that to “the Islamic world”.
- Archive access from this host was intermittent at the end of the session: two of three `web.archive.org` GETs failed with `curl: (7) Failed to connect to web.archive.org:443` and one `URLError <urlopen error [Errno 111] Connection refused>`, while the successful one served the 2025 capture in full. FETCH-59 skips an erroring URL, so the capture is listed as a fallback, not as a dependency.
