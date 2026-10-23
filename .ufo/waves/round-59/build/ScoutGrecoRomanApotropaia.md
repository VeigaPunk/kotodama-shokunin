# ScoutGrecoRomanApotropaia — round 59, claim C source seat

Subtopic: Greek and Roman apotropaia — the gorgoneion, the fascinum, the child's bulla, apotropaic eyes on
vessels. Two sources opened and offered: S604 (the British Museum's own 1920 guide text on the bulla) and
S605 (a 2024 open-access Archaeopress volume's introduction by Christopher A. Faraone, on apotropaia at
boundaries and the frontal face as an amulet against plague).

Every URL below was fetched by me in this session with an ordinary plain GET (curl, desktop Firefox UA,
redirects followed, no challenge, no login, no paywall workaround). No URL already in `corpus/SOURCES.md`
was re-offered: `grep -F 'gutenberg.org/cache/epub/52081'`, `grep -F -i 'archaeopress.com'` and
`grep -F -i 'spathi'` each returned nothing (rc=1).

Pre-filing check (`rowcheck.py --draft … --entry …`) printed LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC
PASS for both rows, exit 0; output pasted verbatim below.

## Registry rows

| S604 | British Museum, Department of Greek and Roman Antiquities, A Guide to the Exhibition Illustrating Greek and Roman Life, 2nd ed. (London: Printed by Order of the Trustees, 1920), Project Gutenberg eBook 52081 — https://www.gutenberg.org/cache/epub/52081/pg52081.txt (direct, HTTP 200, 415476 bytes; read 2026-10-23); capture https://web.archive.org/web/20260512010533id_/https://www.gutenberg.org/cache/epub/52081/pg52081.txt (Wayback capture 20260512010533, HTTP 200, 415479 bytes, quote verified in the captured text) | book | B | the Museum's own catalogue text on the bulla: a flat bronze pendant with a circular receptacle, Etruscan in origin, made to hold amulets and charms, worn by freeborn Roman boys and sometimes by domestic animals | s.v. Bullae (the guide index lists BULLA, 136, 218): "They were designed to contain amulets and charms, and were worn principally by freeborn Roman boys, and occasionally by domestic animals." | A bulla is a receptacle for amulets and charms, hung chiefly on freeborn boys and sometimes on farm animals. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |
| S605 | Spathi, Maria G., Maria Chidiroglou and Jenny Wallensten (eds.), Apotropaia and Phylakteria: Confronting Evil in Ancient Greece (Oxford: Archaeopress Archaeology, 2024), publisher sample PDF of the open-access volume, CC BY-NC-ND 4.0, Faraone introduction pp. 1-10 — https://www.archaeopress.com/Archaeopress/DMS/84FE4CF1A07D4BD9A83AEA574427183A/9781803277493-sample.pdf (direct, HTTP 200, 1227583 bytes; read 2026-10-23); capture https://web.archive.org/web/20250925065631id_/https://www.archaeopress.com/Archaeopress/DMS/84FE4CF1A07D4BD9A83AEA574427183A/9781803277493-sample.pdf (Wayback capture 20250925065631, HTTP 200, 1227583 bytes, quote verified in the captured PDF text) | book | B | Faraone's introduction to the volume: the definition of amulet, phylakterion and apotropaion, apotropaia at entrances, and frontal faces and eyes as protective devices on city walls, shields, ships and the body, including an amulet against plague | Faraone, introduction (running head 3), the paragraph on shields and ships: "A frontal face was also used as a protective amulet to ward off the plague." | A frontal face was a protective amulet against plague, and apotropaic eyes served as a common device on ships. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md |

## Gate lines

- S604 — https://www.gutenberg.org/cache/epub/52081/pg52081.txt — accessed 2026-10-23 — s.v. Bullae (the guide index lists BULLA, 136, 218): “They were designed to contain amulets and charms, and were worn principally by freeborn Roman boys, and occasionally by domestic animals.”. Grounds: A bulla is a receptacle for amulets and charms, hung chiefly on freeborn boys and sometimes on farm animals. Seat: ScoutGrecoRomanApotropaia.
- S605 — https://www.archaeopress.com/Archaeopress/DMS/84FE4CF1A07D4BD9A83AEA574427183A/9781803277493-sample.pdf — accessed 2026-10-23 — Faraone, introduction (running head 3), the paragraph on shields and ships: “A frontal face was also used as a protective amulet to ward off the plague.”. Grounds: A frontal face was a protective amulet against plague, and apotropaic eyes served as a common device on ships. Seat: ScoutGrecoRomanApotropaia.

## rowcheck output (verbatim, exit 0)

```
S604 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.gutenberg.org/cache/epub/52081/pg52081.txt | BOILER: root-clear https://www.gutenberg.org/; not a title, h1 or meta label | RELEVANCE: shared=['amule', 'anima', 'boys', 'charm', 'freeb'] | TOPIC: quote_hits=2 function_words=4 page_hits=19 page_terms=18 need=1/2/3/2
S605 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.archaeopress.com/Archaeopress/DMS/84FE4CF1A07D4BD9A83AEA574427183A/9781803277493-sample.pdf | BOILER: root-clear https://www.archaeopress.com/; not a title, h1 or meta label | RELEVANCE: shared=['amule', 'face', 'front', 'plagu', 'prote'] | TOPIC: quote_hits=1 function_words=5 page_hits=146 page_terms=131 need=1/2/3/2
EXIT=0
```

Command run (working directory `/fast/scratch/hyaku/kotodama-r59/ScoutGrecoRomanApotropaia/`):

```
timeout 900 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-59/rowcheck.py \
  --draft /fast/scratch/hyaku/kotodama-r59/ScoutGrecoRomanApotropaia/rows.md \
  --entry /fast/scratch/hyaku/kotodama-r59/ScoutGrecoRomanApotropaia/stub.md
```

## draft sentences

A bulla is a pendant with a receptacle, made to contain amulets and charms rather than to display them (S604).

Bullae are worn chiefly by freeborn Roman boys and occasionally by domestic animals, so a child and a farm animal can carry the same protective pendant (S604).

The Museum's examples are flat bronze pendants with a circular receptacle in the middle, a form it calls an ornament of Etruscan origin introduced early into Rome (S604).

A frontal face worked as a protective amulet against plague, and the same eyes appear as an apotropaic device on ships (S605).

The volume defines an amulet as any object, text or image attached to a human or animal body, a house or a city, aiming at protection, healing or a further goal (S605).

Apotropaia cluster at entrances, and the introduction follows the image inward from the city gate and wall to the house and the human body (S605).

## Evidence notes

- S604, what the page actually says around the anchor. The paragraph runs, verbatim: "=Bullae.=--The flat bronze pendants (No. =384=), with a circular receptacle in the middle, are _bullae_. These are ornaments of Etruscan origin, introduced early into Rome. They were designed to contain amulets and charms, and were worn principally by freeborn Roman boys, and occasionally by domestic animals." The anchor's "They" is therefore the *bullae* of the two preceding sentences; the teaches cell supplies that noun, so a reviewer opening the page lands in the same paragraph. The guide's index line reads "BULLA, 136, 218", and the passage sits under the "=Bullae.=" heading; the same page adds, of a vase of children and pets, "More than one of the pigeons wears a _bulla_ round its neck (No. =660=) to avert the evil eye (see p. 136)" — I did not quote it (it embeds Gutenberg's "=660=" markup and runs past 25 words), but it is why the "domestic animals" clause is not a stray detail.
- S604, why this is a design row. The Museum describes a *container* rather than an emblem: the pendant holds amulets and charms, its wearer set is children and animals, and its origin is given as Etruscan with early Roman adoption. That is material, wearer and placement in one sentence.
- S604 tier = B: the printed guide is a museum publication describing the Museum's own objects, but it is a 1920 popular catalogue, superseded in detail; it is reliable for what the Museum said about this class of object, not for current scholarship.
- S605, what the page actually says around the anchor. Verbatim sequence in Faraone's introduction: "…someone carved a pair of frontal eyes on the city wall of Thasos, an image called a 'panther mask' by art historians… The image also appears occasionally on the outer surface of military shields. Eyes also appear as a common apotropaic device on ships. Recent discoveries of underwater archaeology have revealed that the irises of these eyes were sometimes painted with concentric circles, much like the frontal eyes of the Gorgon's head. A frontal face was also used as a protective amulet to ward off the plague." The next sentences give the Hellenistic Antioch story (a giant face of Charon carved into the mountain, with words inscribed "for the salvation of the city").
- S605, the definition passage (used for draft sentence 5, not for the anchor): the abstract defines an "amulet" as "any object, text or image attached to a human or animal body, to a house or city or in fact to any valuable human possession" aiming at "(i) protection; (ii) healing; or (iii) the acquisition of some abstract goal"; it derives *phulakteria* from *phulassein*, "to protect", and *apotropaia* from *apotrepein*, "to turn away", as the subset that protects by turning evil aside; and it says "Since apotropaia are mainly found at entrances, they are the primary focus of this chapter."
- S605 tier = B: a named scholar's introduction in a peer-edited, open-access academic volume (CC BY-NC-ND 4.0, © The authors and Archaeopress 2024, ISBN 978-1-80327-749-3), read from the publisher's own sample PDF. It is a secondary synthesis with its own footnotes (e.g. n. 14 to Faraone 2018: 68-70), not a primary text; the row supports the volume's own framing of these objects.
- Page floors, measured on the served pages (not only on the quote): S604 page 19 CHARM-GUARD windows and 18 DISCIPLINE matches; S605 page 146 windows and 131 matches. Both clear 3/2 on the whole page.
- Captures: both were verified as same-page `id_` captures that *carry the anchor*. Gutenberg capture 20260512010533 (HTTP 200, 415479 bytes; `locate_in` True, 415,142 chars of text). Archaeopress capture 20250925065631 (HTTP 200, 1227583 bytes; 18-page PDF; extracted text 61,582 chars; `locate_in` True).
- Scope honesty: neither row is offered as a universal. S604 is one museum's own catalogue wording about bullae in its cases, and its "designed to contain amulets and charms" is that catalogue's claim. S605 is one scholar's introduction: it says a frontal face "was also used" as an amulet against plague and that eyes were "a common apotropaic device on ships", i.e. it records a practice, not a rule that every frontal face or every ship's eye was apotropaic — the same page is explicit that the eyes' position on the prow is also explained by analogy with an animal's head. The entry sentences keep that hedging.
- Tooling: no packages installed or updated for this seat.

## Integration notes for the L1

- The two rows above are exactly as pre-filed: I copied lines 18-19 of this report into a fresh `rows.md`
  and re-ran the same command; both rows again printed LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS,
  exit 0.
- Locator-cell trap found while pre-filing: `reopen-quote.py`'s `row_target` takes the *first*
  double-quoted string in the anchor cell as the quote. A locator that quotes anything else (a printed
  page heading, an index line) silently becomes the anchor and LOCATE fails with `quote under 8 words`.
  Keep page/section references unquoted, as they are in both rows here.
- Both rows list a live URL first and one same-page `id_` Wayback capture second; both captures were
  fetched and the anchor located in the captured bytes, so FETCH-59's live-failure path is covered.
- Hosts added by this seat: gutenberg.org (already in SOURCES for other paths) and archaeopress.com (new).
- S605 is a PDF: LOCATE/BOILER/TOPIC all run it through the frozen locator's `to_text`, which shells to
  `uv run --no-project --with pypdf==5.4.0`; that worked here in 0.2 s and the extracted text located the
  quote on both the live and captured copies.

## rejected

Opened and not offered (each reason with the tool's own output where a tool result decided it):

1. https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.04.0063:entry=bulla-cn — Smith's *Dictionary of Greek and Roman Antiquities* (1890), s.v. BULLA, the source I most wanted for this subtopic. Fetch: `HTTP 429` on three attempts (the second after a 20 s pause), body 237 bytes each time: `<h1>Too many requests</h1> <p>You are sending requests faster than Perseus can handle. Please wait a minute and try again.</p>`, headers `Server: Varnish`, `Retry-After: 30`. Rejected because Perseus throttles plain GETs per IP and, in `reports/round-59/rowcheck.py`, `_fetch_once` retries only when the netloc is `web.archive.org`, so a single 429 at acceptance is final for that row (and BOILER would also fetch `https://www.perseus.tufts.edu/` a second time). I do not list a capture of a page I could not read live.
2. https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.02.0137:book=28:chapter=7 — Pliny, *Natural History* Book 28 (fascinum / remedies against fascination), Bostock-Riley at Perseus. Fetch: `HTTP 429`, 237 bytes, same body.
3. https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.04.0063:entry=amuletum-cn — Smith 1890, s.v. AMULETUM. Fetch: `HTTP 200 109979 bytes`, and the entry is strong: `smith amuletum: chars 16437 page_hits 41 terms 34`, with matter on materials (stones, the eagle-stone, gems), the difficulty ancient physicians had in separating a medicine from an amulet, and "the frequent use of Eastern symbols, and even inscriptions on amulets". Rejected only for the same Perseus throttling risk as (1) and because it is a general Graeco-Roman amulet entry rather than this subtopic's gorgoneion/fascinum/bulla/eye-cup ground.
4. https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Plutarch/Moralia/Roman_Questions*/E.html — Plutarch, *Roman Questions* (Loeb, Babbitt 1936) at LacusCurtius, questions 85-113. Fetch: `HTTP 200 87809 bytes`. Question 101 is the bulla question, but mechanically and editorially it fails: page metrics `## rq-E.html: window_hits=3 discipline=3 chars=30724` (exactly at the window floor) and the only 10-25-word sentence with a window is the question heading itself, `[1h 3f] 101 1 Why do they adorn their children's necks with amulets which they call bullae ?` — a heading, barred by the row rule. The declarative sentences that follow it (e.g. "and he received this amulet as a prize of valour from his father the king") have no GUARD stem within three words, so no other candidate exists on the page.
5. https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Plutarch/Moralia/Roman_Questions*/home.html — fetch `HTTP 200 83026`; the work's index page, not a source about objects. Opened only to find Q101.
6. https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Plutarch/Moralia/Roman_Questions*/D.html — fetch `HTTP 200 65527`, `bulla hits: 0`. No bulla material.
7. https://penelope.uchicago.edu/Thayer/E/Roman/Texts/secondary/SMIGRA*/home.html — Thayer's selection from Smith 1875. Fetch `HTTP 200 77423`; of its 276 entry links, nothing matches the bulla/amulet/fascinum/gorgoneion/praebia/crepundia words; the only hit in the wider set I grepped (which also carried medicus, anulus, monile, toga, lunula, phallus) was `Medicus.html`. No entry to cite.
8. https://penelope.uchicago.edu/Thayer/E/Roman/Texts/secondary/SMIGRA*/B*.html and …/A*.html — guessed per-letter pages: `HTTP 404 49` each.
9. https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Pliny_the_Elder/home.html — fetch `HTTP 200 35446`. LacusCurtius serves Pliny's Latin (Mayhoff); its own page points English readers to Perseus and to Holland's partial translation elsewhere. Latin-only, so no English quote.
10. https://www.metmuseum.org/toah/hd/gorg/hd_gorg.htm — the Heilbrunn essay on the gorgoneion. Fetch: `HTTP 429 34228 bytes`.
11. https://www.metmuseum.org/art/collection/search/253350 — Met object record. Fetch: `HTTP 429 34218 bytes`.
12. https://www.britishmuseum.org/collection/object/G_1873-0305-1 — British Museum object record. Fetch: `HTTP 403 5664 bytes` (bot challenge: challenge met, not passed). Not read, so not cited; the BM text I do offer is S604, its own printed guide.
13. https://www.clevelandart.org/art/399499 — Cleveland Museum, "Gorgoneion Antefix (Ornamental Roof Tile)", c. 500 BCE, culture "Greek / South Italian, Taranto". Web page `HTTP 200 82076 bytes` but the served HTML holds 1,880 chars of text (the description is rendered client-side): `## cle-399499.html: window_hits=0 discipline=7 chars=1880`. The open-access API record carries the prose (`HTTP 200 6701 bytes`) — "This mold-made terracotta antefix … takes the form of a Gorgoneion … perhaps considered both terrifying and protective" — but the record is too short for the page floors: `## cle-399499.json: window_hits=0 discipline=5 chars=3920`. TOPIC would fail (needs 3 windows, page_terms ok but hits 0).
14. https://openaccess-api.clevelandart.org/api/artworks/108840 — Cleveland, "Black-Figure Eye Cup: Iris and Satyrs (A, B); Gorgoneion (I)", c. 520-510 BCE. `HTTP 200 6416 bytes`; description reads "Although the eyes and Gorgoneion may serve to ward off evil, they also make for fluid identities while drinking…". Directly on subtopic, but the same failure: `## cle-108840.json: window_hits=0 discipline=4 chars=3622` (no CHARM stem within three words of a GUARD stem anywhere in the record), so TOPIC fails and the quote side has nothing to teach from. Its web page `https://www.clevelandart.org/art/108840` (`HTTP 200 86095`) serves only 2,079 chars of text: `window_hits=0 discipline=7`.
15. https://www.clevelandart.org/art/159603 and https://openaccess-api.clevelandart.org/api/artworks/159603 — Cleveland, "Gorgoneion Plaque". `HTTP 200 77589` (web, `window_hits=0 discipline=6 chars=1678`) and `HTTP 200 4214` (API). Same TOPIC failure; the one good sentence ("Both bear gorgoneia, or frontal Gorgon faces … perhaps meant to ward off evils") puts "gorgoneia" 16 words from "ward".
16. https://collectionapi.metmuseum.org/public/collection/v1/search?q=gorgoneion — the Met search API answers with an error, verbatim: `{"message":"/public/collection/v1/search was retired on 2026-10-01. It was backed by Solr and returned every matching object ID in one response; use /public/collection/v1.1/search, which is Elastic-backed and paginated via offset and limit. …","replacement":"/public/collection/v1.1/search", …}`. The v1.1 endpoint answers `{"total":82,"objectIDs":[256032,250968,255184,248331,253581]}` for "gorgoneion" and 1,308 for "eye cup", but Met object records carry no curatorial prose (title/medium/culture/credit line only), and the Met's own object web pages returned 429 above.
17. https://www.penn.museum/collections/ — fetch `HTTP 403 961 bytes` (block page).
18. https://collections.mfa.org/ — fetch `HTTP 202 0 bytes` (zero-byte challenge, nothing served).
19. https://uremuseum.org/ — fetch `curl: (7) Failed to connect to 172.17.0.3:443 after 0 ms: Could not connect to server` then `HTTP 301 0` (host resolved to a loopback-style address; not usable, and an IP/port URL is refused by the locator).
20. https://www.classarch.cam.ac.uk/ — fetch `curl: (6) Could not resolve host: www.classarch.cam.ac.uk` (HTTP 000).
21. https://www.getty.edu/art/collection/search?q=gorgoneion — fetch `HTTP 200 9098 bytes` with no object links in the served body (client-side search), and a search URL is refused as a row anyway (`search-url`).
22. https://api.archives-ouvertes.fr/search/?q=gorgoneion&fl=… — HAL API, `HTTP 200`; two hits, the only prose one being `2022 ART ['Au seuil des mondes : la face gorgonéenne dans l’imaginaire funéraire étrusque du viie siècle av. J.-C.', …] | https://hal.science/hal-03737255v1 | None` — `fileMain_s` is null, so no full text is deposited, and the article is in French. Landing page not opened; not quotable.
23. https://journals.openedition.org/ and https://hal.science/ — root probes only (`HTTP 200 5255` and `HTTP 200 12566`); opened to see whether open classics journals were reachable. No article was opened, so nothing is offered from them.
24. https://www.liverpoolmuseums.org.uk/ (`HTTP 200 25983`), https://www.ashmolean.org/ (`HTTP 200 356055`), https://www.beazley.ox.ac.uk/ (`HTTP 200 3766`) — host probes only; no object page opened, nothing quotable.
25. https://openaccess-api.clevelandart.org/api/artworks/?q=bulla&limit=5 — Cleveland API query for "bulla": `{'total': 0, …}` — no bulla in that collection; this is why the Roman bulla row comes from the British Museum guide (S604) instead.
26. https://www.archaeopress.com/Archaeopress/DMS/… sample PDF — offered as S605, not rejected; listed here only so the count of opened URLs is complete. Its front matter (`© The authors and Archaeopress 2024`, CC BY-NC-ND 4.0) is quoted in the evidence notes above.

Nothing else was opened. The two nearest misses worth a later round: the Cleveland eye-cup and gorgoneion records (exactly the right curatorial text, but each record is too short: 0 CHARM-GUARD windows against the 3-window floor) and Perseus's Smith "Bulla"/"Amuletum" entries (41 windows on AMULETUM), both blocked by host or record length rather than by topic.
