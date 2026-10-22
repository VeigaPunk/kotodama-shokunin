# ScoutKongoEmbassies — Kongo envoys in Europe: what the records say they wore

Two opened sources, both museum-authored records of Kongo envoys in Europe, both bearing on dress and on how a European institution names and dresses a Kongo office-holder. NEW-ScoutKongoEmbassies-1 is the holding museum's own record for the three Copenhagen portraits. NEW-ScoutKongoEmbassies-2 is the Walters Art Museum's exhibition catalogue essay on the Caporale bust of António Manuel Ne Vunda in Santa Maria Maggiore, Rome, and on the competing images of him.

Every quoted string below was matched as a contiguous substring of the text I extracted from the file I read (whitespace normalised), so each quote is verbatim at the strength the page states. Danish quotes are given as the museum wrote them; my English renderings appear only in the draft sentences.

### NEW-ScoutKongoEmbassies-1

citation: Statens Museum for Kunst (SMK), Copenhagen. Collection records KMS7 "Dom Miguel de Castro", KMS8 "Pedro Sunda" and KMS9 "Diego Bemba", c. 1643, oil on panel, 75 x 62 cm, with the museum's gallery-label texts attached to each record; public domain (CC0). Stable ids: SMK object numbers KMS7, KMS8, KMS9; SMK Open API record ids 1170022834_object (KMS7), 1170022784_object (KMS8), 1170024702_object (KMS9).

url: https://api.smk.dk/api/v1/art/search/?keys=Miguel%20de%20Castro&offset=0&rows=10 and the single-object endpoint https://api.smk.dk/api/v1/art?object_number=KMS7

route: direct plain GET, HTTP 200, application/json, 29,400 bytes (search) and 10,712 bytes (object endpoint); no challenge, no login, no browser. The HTML front end https://open.smk.dk/en/artwork/image/KMS7 is a JavaScript shell that serves no record text, so the API record is the document read. Access date 2026-10-22.

kind: record

tier: A — the holding museum's own catalogue record and gallery text for its own three objects, including the inscriptions on the reverse that it quotes; the dress reading inside the labels is curatorial interpretation and is scoped below.

scope: what SMK's record and labels state about the three portraits: the sitters' names taken from the inscriptions on the reverse, the embassy's sponsor (the lord of Soyo), its route through Dutch Brazil and the 200 enslaved people presented there, the European and French dress and its parts, the two named servants and the elephant tusk, and the paintings' 1654 gift to Frederick III. Not: Kikongo terms, Kongo kingship, or any Kongo-side account of the embassy.

quotes:
- KMS7 record, second title field: "Dom Miguel de Castro, Ambassadør for herren af Sonho"
- KMS7 record, third title field: "Dom Miguel de Castro, Kongolesisk gesandt"
- KMS7 gallery label 1 (credited in the record to the SMK book 50 værker du skal se på SMK): "I 1640 opstod der i det tidligere kongerige Kongo en international strid mellem herren til Soyoprovinsen og kongen af Kongo."
- KMS7 gallery label 1: "Dom Miguel de Castro blev udsendt af herren til Soyo som ambassadør på en diplomatisk mission for at skaffe støtte hos De Forenede Nederlande."
- KMS7 gallery label 1: "forærede han 200 slavegjorte mennesker til guvernøren over Hollandsk Brasilien"
- KMS7 gallery label 1: "Under Dom Miguels efterfølgende rejse til Nederlandene bestilte Det Nederlandske Vestindiske Kompagni et portræt af ham."
- KMS7 gallery label 1, on the dress: "med en rigt mønstret skjorte, brun jakke, hvid kniplingskrave samt en hat i bæverskind med metalkæde og en lang, rød fjer"
- KMS7 gallery label 2: "Han er klædt efter tidens franske mode."
- KMS7 gallery label 2: "I 1654 skænkede Johann Moritz af Nassau-Siegen malerierne til den danske konge Frederik 3."
- KMS8 gallery label 1: "Dom Michael de Castro var på diplomatisk mission for greven af Sonho (Soyo), Daniel da Silva"
- KMS8 gallery label 1: "Med sig havde han sine to tjenere, Pedro Sunda og Diego Bemba."
- KMS8 gallery label 1: "Den kostbare elefantstødtand var måske én af de gaver, som delegationen havde med."

teaches: Copenhagen's record of three 1643 portraits names a Kongo embassy sent by the lord of Soyo, its European dress, its named servants and its royal-collection afterlife.

draft sentences:
- The record gives the sitter two offices at once, ambassador of the lord of Sonho and Kongo envoy, and its label says the lord of Soyo sent him, so a worldbuilder must choose whether such a man speaks for a province or for the kingdom (NEW-ScoutKongoEmbassies-1, KMS7 record title fields 2-3 and gallery label 1).
- The quarrel behind the mission is internal: the label dates it to 1640 as a dispute between the lord of the Soyo province and the king of Kongo, a usable pattern for a realm split between a crown and a great provincial house (NEW-ScoutKongoEmbassies-1, KMS7 gallery label 1).
- Its economy is stated without euphemism: as part of the mission he presented 200 enslaved people to the governor of Dutch Brazil, so an embassy in this world can carry human beings as its gift (NEW-ScoutKongoEmbassies-1, KMS7 gallery label 1).
- SMK's Danish label dresses him item by item in European clothing and a second label calls the outfit the French fashion of the period, while the record keeps the inscription Don Michael de Castro from the back of the panel, so a Kongo noble can be staged in borrowed court dress with his own name still on the reverse (NEW-ScoutKongoEmbassies-1, KMS7 gallery labels 1-2).
- The portrait was ordered by the Dutch West India Company during his journey north and reached Denmark in 1654 as Johann Moritz of Nassau-Siegen's gift to Frederick III, a chain from diplomatic errand to royal cabinet that a worldbuilder can reuse for how foreign visitors become collections (NEW-ScoutKongoEmbassies-1, KMS7 gallery labels 1-2).
- His two servants, Pedro Sunda and Diego Bemba, are named on their own panels, and an elephant tusk in one of them is offered only as possibly one of the delegation's gifts, a hedge worth keeping on a worldbuilder's prop (NEW-ScoutKongoEmbassies-1, KMS8 gallery labels 1-2).

### NEW-ScoutKongoEmbassies-2

citation: Lowe, Kate. 2012. "Visual Representations of an Elite: African Ambassadors and Rulers in Renaissance Europe." In *Revealing the African Presence in Renaissance Europe*, ed. Joaneath Spicer, 99-115 (Ne Vunda passage at 104-105; notes 27-32 at 114-115). Baltimore: Walters Art Museum, third printing 2013. ISBN 978-0-911886-78-8.

url: https://thewalters.org/wp-content/uploads/revealing-the-african-presence-in-renaissance-europe.pdf

route: direct plain GET, HTTP 200, application/pdf, 3,089,744 bytes; no challenge, no login, no browser; text extracted with pdftotext 26.08.0 (poppler, already installed) and the quotes matched against the extracted page text. Access date 2026-10-22.

kind: book (museum exhibition catalogue essay)

tier: A — a footnoted catalogue essay by a professor of Renaissance history, authoritative for how the Caporale bust and the paired prints, fresco and medal represent Ne Vunda; it is not the bust itself, and its kinzembe identification rests on Thompson and Cornet 1981 (note 29), which I did not open.

scope: the Caporale bust's commission by Paul V and execution under Urban VIII in 1629, its basis in the death mask, the raffia kinzembe or zamba kya mfumu and the nkutu a nyondo identification, the absence of Christian symbols, the two opposed print versions, the Quirinale fresco in European court dress, the medal of an audience that never took place, and the catalogue's statement that no European image of a Kongo ruler exists.

quotes:
- fig. 46 caption, p. 104: "Antonio Manuel, Marquis of Ne-Vunda, 1629. Marble."
- p. 104, Ne Vunda passage: "Commissioned by Paul V but executed only under Urban VIII"
- p. 104, Ne Vunda passage: "is based on Ne-Vunda’s death mask"
- p. 104, Ne Vunda passage: "yet no Christian symbols are displayed; instead, Ne-Vunda is portrayed as an African in African dress"
- p. 104, Ne Vunda passage: "a tunic or cape in raffia openwork mesh or netting known as a kinzembe or zamba kya mfumu"
- p. 104, Ne Vunda passage: "an article of clothing reserved in the Congo for chiefs or other important people"
- p. 104, Ne Vunda passage: "always slung across the left shoulder"
- p. 104, Ne Vunda passage: "the quiver in Caporale’s bust seems intended to represent a reworked nkutu"
- p. 104, Ne Vunda passage: "one depicting him in European dress"
- p. 105, continuation of the Ne Vunda passage: "and the other in African dress"
- p. 104, Ne Vunda passage: "There are no extant images of early Congolese ambassadors to Europe, many of whom traveled to Portugal but were allowed no further."
- p. 105, section text on rulers: "unfortunately there are none at all of rulers of the Congo"
- p. 105, section text on rulers: "Portraiture of African rulers is less stable than portraiture of African ambassadors"
- p. 114, note 32: "dated to 1616–17, shows him in European court dress"
- p. 114, note 32: "Although Pope Paul V did visit Ne-Vunda on his deathbed, Ne-Vunda never had a formal audience with the pope."
- p. 114, note 32: "Other depictions perpetuated “false” memories."

teaches: Rome's bust of the Kongo envoy dresses him in raffia regalia called kinzembe, while prints and frescoes show European dress and a medal invents an audience.

draft sentences:
- The bust in the Baptistery of Santa Maria Maggiore was commissioned by Paul V but carved only under Urban VIII, and the catalogue dates it 1629, so its face comes from a death mask while its dress is a later choice by the sculptor (NEW-ScoutKongoEmbassies-2, p. 104 and fig. 46 caption).
- Lowe identifies the garment as a raffia openwork tunic or cape, a kinzembe or zamba kya mfumu reserved in Kongo for chiefs and important people, and reads the quiver on the bust as a reworked nkutu a nyondo, the bag of power worn across the left shoulder (NEW-ScoutKongoEmbassies-2, p. 104).
- A monument made for a church displays no Christian symbols at all and presents him as an African in African dress, a usable pattern for a religious institution that honours a foreign dignitary without converting his image (NEW-ScoutKongoEmbassies-2, p. 104).
- The same envoy appeared in two nearly simultaneous prints, one in European dress and one in African dress, and a Quirinale fresco of 1616-17 puts him in European court dress, so a worldbuilder must decide which of these counts as the official image (NEW-ScoutKongoEmbassies-2, pp. 104-105 and p. 114, note 32).
- The catalogue records that Paul V visited him on his deathbed but never gave him a formal audience, that a medal was struck of that audience anyway, and that other depictions perpetuated false memories, which is a ready model for invented ceremony in a chronicle (NEW-ScoutKongoEmbassies-2, p. 114, note 32).
- Portuguese contact came in the 1480s and Christianization in 1491, yet it took more than a hundred years for a Congolese ambassador to reach Rome, the catalogue noting that many travelled to Portugal but were allowed no further, and it states that no European image of a Kongo ruler exists at all (NEW-ScoutKongoEmbassies-2, pp. 104-105).

## Notes for the entry

- Naming. Soyo appears in these records under the older Portuguese spelling Sonho; the man who sent Miguel de Castro is Daniel da Silva, called count of Sonho in KMS8's label and lord of Soyo in KMS7's. Miguel de Castro was that lord's envoy, not the Kongo king's, although SMK's own title fields call him a Kongo envoy as well. The entry should name the sponsor, not just "Kongo".
- Titles in European mouths. The catalogue captions Ne Vunda "Marquis of Ne-Vunda" (fig. 46), while the Roman records it cites give him the Portuguese form of a Kongo title; a worldbuilder rendering Kongo offices into European ranks has to choose and stay consistent. The catalogue also calls Álvaro II "the eighth Christian king of the Congo" (p. 104).
- Dress evidence is European-made in both rows. The Copenhagen portrait is a life-sitting by a Dutch painter for a Dutch company; the Roman bust is posthumous, from a death mask, carved two decades later. Neither is a Kongo-side record of costume, and the kinzembe identification is scholarship about the bust, not an inscription on it.
- Sensitivity. SMK's label states the 200 enslaved people plainly; keep the number and the recipient (the governor of Dutch Brazil). The catalogue's "bag of power" is its own gloss of nkutu a nyondo and stands in quotation marks there; do not carry the older exoticising vocabulary.
- Overlap. ScoutNkisiNkondi and ScoutKandaKinship cover nkisi objects, bags and titles from the Kongo side; my two rows are the European-record and dress angle and should not be stretched to cover kingship or language.
- Confidence. High for what each record says (every quote matched verbatim against the file read). Medium for the bust's garment identification (secondary, footnoted to Thompson and Cornet 1981, not opened here).

## Unrun checks

No acceptance command was run and nothing was landed: this is a leaf source seat. No tool was installed or upgraded; pdftotext 26.08.0 was already present.

unopened:
- Kate Lowe, "'Representing' Africa: Ambassadors and Princes from Christian Africa to Renaissance Italy and Portugal, 1402-1608," *Transactions of the Royal Historical Society* 17 (2007), 101-128, publisher PDF at cambridge.org — direct GET returned HTTP 429 "Too many automated requests from this network" (rate limit, no captcha shown); the archive.org availability API also answered 429. Not opened; its Ne Vunda material is reached through NEW-ScoutKongoEmbassies-2 instead.
- The Metropolitan Museum of Art record for Lucas Kilian's print of Ne Vunda, accession 2001.650 — the collection page returned a Vercel security checkpoint (HTTP 429) and the public collection API served metadata only, with no curatorial text, so it could carry no dress claim. Not opened as a text source.
- Queen's University QSpace record "Monument of Antonio Emmanuele Ne-Vunda" — opened (HTTP 200) but not filed: an unsigned repository abstract whose garment identifications duplicate NEW-ScoutKongoEmbassies-2 at lower authority; I did not verify its claims.
- VIVE (Vittoriano e Palazzo Venezia) event page "Converted in Rome: an ambassador from the Congo at the time of Pope Borghese" — opened (HTTP 200) but not filed: an event announcement that narrates the 1608 arrival and death and says nothing about clothing.
- Royal Museum for Central Africa (Tervuren) article "The Kongo kingdom" — opened (HTTP 200) but not filed: it names the bust and its maker, Francesco Caporale, and says nothing about what the sitter wears; other seats cover kingdom history.
