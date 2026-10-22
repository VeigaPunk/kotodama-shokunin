# ScoutNkisiNkondi — minkisi and nkisi nkondi: three holding-museum records and one specialist essay

- seat: `KotodamaR56.ScoutNkisiNkondi` (scout, claim C ground: Kingdom of Kongo civilization reference base)
- round: kotodama 56 (hyaku phase 4), 2026-10-22
- lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, declaration `b4b7db91a38447bb2c07b0ef436fc9654dcec89c`, claim base `052f145cbcff6996c153d460d81ce346ce74bfbc`
- assignment: two holding-museum records written by the museum on what a nkisi nkondi did and who used it, plus one open scholarly source by MacGaffey or another specialist on what nkisi means; quotes with locators, `fetish` only as a flagged quotation
- draft ids used below: `NEW-ScoutNkisiNkondi-1` … `-4`; the L1 assigns final `S` ids inside S359–S418 at integration
- tools installed: none. Every fetch below was a plain `curl` request; no browser, no challenge worked around.
- substitution note: of the five museums named in the assignment, only the Met could be read (through a Wayback
  copy); the British Museum, the Smithsonian National Museum of African Art and the Brooklyn Museum refused plain
  requests, and the Royal Museum for Central Africa publishes no object-level record for these figures that I could
  reach. Two other holding museums with museum-written records, the Pitt Rivers Museum and the Cleveland Museum of
  Art, stand in for them and are rowed below.

## Route summary (four sources, all opened this session)

| # | institution | object / text | URL actually read | status |
|---|---|---|---|---|
| 1 | The Metropolitan Museum of Art | Mangaaka Power Figure (Nkisi N'Kondi), 2008.30, object record (label + MacGaffey audio transcript) | `https://web.archive.org/web/20251207060528id_/https://www.metmuseum.org/art/collection/search/320053` | Wayback capture, HTTP 200, 282425 bytes |
| 2 | Pitt Rivers Museum, Oxford | Mavungu, 1900.39.70, museum interpretive record (C. Morton, 2010) | `https://prm.web.ox.ac.uk/files/mavungupdf` | direct, HTTP 200, application/pdf, 9 pp. |
| 3 | Cleveland Museum of Art | Male figure (nkisi nkondi), 2010.432, object record | `https://openaccess-api.clevelandart.org/api/artworks/168726` | direct, HTTP 200, JSON (human page `https://clevelandart.org/art/2010.432` also 200) |
| 4 | Journal of Art Historiography (University of Birmingham) | John Mack, "Fetish: Magic Figures in Central Africa" | `https://arthistoriography.wordpress.com/wp-content/uploads/2011/12/mack-fetish.pdf` | direct, HTTP 200, application/pdf, 14 pp. |

Access date for all four: 2026-10-22. The Met's own HTML pages answered HTTP 429 with a Vercel Security
Checkpoint (script-and-cookie gate) on 2026-10-22: **challenge met, not passed**; the ordinary Wayback copy above
was read instead, and every Met quotation below comes from that capture. Every quotation from sources 1 to 3 was byte-checked against the
fetched bytes (whitespace-normalised substring match, 13 candidate strings, 13 hits); the four Mack quotations were
read off a 200 dpi render of the printed page, because that PDF's text layer is OCR output with visible errors.

---

### NEW-ScoutNkisiNkondi-1

citation: The Metropolitan Museum of Art, New York. *Mangaaka Power Figure (Nkisi N'Kondi)*, ca. 1880–1900, Yombe-Kongo artist and nganga (ritual specialist), object number 2008.30, Michael C. Rockefeller Wing. Object record: label text and audio stop 1547 with Wyatt MacGaffey. Undated record; page read 2026-10-22; Wayback capture id 20251207060528.

url: https://web.archive.org/web/20251207060528id_/https://www.metmuseum.org/art/collection/search/320053

route: Wayback capture 20251207060528 of the live object page; the live metmuseum.org page answered HTTP 429 with a Vercel Security Checkpoint on 2026-10-22 (challenge met, not passed). Archive copy HTTP 200.

kind: record

tier: A — the holding museum on its own accession and its own published label; the label's reading is the Met's curatorial interpretation, not a Kongo statement, so do not stretch it past this object and its class.

scope: what the Met says the Mangaaka class of nkisi nkondi was for (a force of jurisprudence, shown as a presiding authority and an enforcing lord or king), who made it (sculptor plus ritual specialist), its chiefly regalia (the mpu headdress, the missing beard marked by chin nails, the abdominal medicine cavity), how its embedded metals worked as a record of vows and treaties, and MacGaffey's statement in the same record that minkisi were aroused by nails, gunpowder explosions and insults. Says nothing about the Kongo cosmogram, about other nkisi classes, or about dating beyond the ca. 1880–1900 attribution.

quotes:
- object label, first paragraph: "Conceived to house specific mystical forces, they were collaborative creations of Kongo sculptors and ritual specialists."
- object label, second paragraph: "Its crowning element is the distinctive mpu headdress worn by chiefs or priests."
- object label, second paragraph: "They document vows sealed, treaties signed, and efforts to eradicate evil."
- audio transcript, MacGaffey: "Minkisi could also be aroused by other means, including explosions of gunpowder and insults."

teaches: The Met reads its Mangaaka figure as a joint work of sculptor and ritual specialist whose embedded metals document sealed vows and signed treaties.

draft sentences:
- Make a power object the joint product of two offices, not one craft: the Met calls such figures collaborative creations of Kongo sculptors and ritual specialists (NEW-ScoutNkisiNkondi-1, object label, first paragraph).
- Name the class after a jurisdiction rather than a person, and show that authority as a role: the label identifies Mangaaka as the preeminent force of jurisprudence, represented as a presiding authority and enforcing lord or king (NEW-ScoutNkisiNkondi-1, object label, first and second paragraphs).
- Put a chief's or priest's crown on the figure: its crowning element is the mpu headdress worn by chiefs or priests (NEW-ScoutNkisiNkondi-1, object label, second paragraph).
- Let metal points carry two jobs at once, record and evidence: the embedded metals document vows sealed, treaties signed and efforts to eradicate evil (NEW-ScoutNkisiNkondi-1, object label, second paragraph).
- Decide that a figure is woken by more than one act, and let the harsher options exist: MacGaffey's note in the same record says minkisi could also be aroused by explosions of gunpowder and insults (NEW-ScoutNkisiNkondi-1, audio transcript).

---

### NEW-ScoutNkisiNkondi-2

citation: Pitt Rivers Museum, University of Oxford. *Mavungu*, object 1900.39.70 (Kongo, Democratic Republic of Congo; collected by Mary Kingsley), museum interpretive record compiled by Christopher Morton, Head of Photography and Manuscript Collections, February 2010; published as a museum PDF. Undated web file, PDF dated 2010; read 2026-10-22.

url: https://prm.web.ox.ac.uk/files/mavungupdf

route: direct plain request, HTTP 200, application/pdf, 9 pages, no challenge.

kind: record

tier: B — a museum-authored interpretive record that carries its own citations (MacGaffey 1993; Thompson 2002; Dennett 1887, 1906): strong secondary for nkondi practice, and authoritative for what this museum documents about its own object, but the practice statements are the museum's synthesis, not primary testimony.

scope: the museum's gloss of the words (nkisi, plural minkisi; nkondi, plural minkondi, "hunter at night"; the record's own rejection of the older English gloss "nail fetish"), what a nganga did and how he was paid, the nganga's dress, the medicine cavity and its mirror, and how medicine containers left minkisi through missionaries and colonial agents, with Mavungu's own seizure and Kingsley bequest. Says nothing about cosmogram readings and does not date the figure beyond "the latter half of the nineteenth century".

quotes:
- section What is Mavungu?, opening: "Mavungu is a type of nkisi known as a nkondi (plural minkondi), which in the past was inadequately glossed as a 'nail fetish'."
- section What is Mavungu?, on the word: "The term nkondi means 'hunter at night'"
- section What is Mavungu?: "The nganga himself would often be of an equally striking and frightening appearance during such rituals, wearing a costume with charms attached."
- section How did Mavungu come to the Museum?: "Such medicine containers were mostly removed from minkisi by missionaries or colonial agents, since this was where their indigenous power was understood to reside."

teaches: The Pitt Rivers record explains nkondi as a night-hunting figure that a nganga worked with nails and medicines for paying clients, and whose power left with its medicines.

draft sentences:
- Say what the word means before describing the object: the museum glosses nkondi as "hunter at night", a figure sent after witchcraft practitioners by night (NEW-ScoutNkisiNkondi-2, section What is Mavungu?).
- Flag the outsider's name inside the entry as a misnomer the record itself rejects, since nkondi was in the past inadequately glossed as a "nail fetish" (NEW-ScoutNkisiNkondi-2, section What is Mavungu?).
- Give the ritual specialist a costume, not only a function: the nganga could cut an equally striking and frightening figure, wearing a costume with charms attached (NEW-ScoutNkisiNkondi-2, section What is Mavungu?).
- Make payment part of the mechanism: clients paid the nganga a sum of money to invoke a nkondi, and later paid to have the metal "contracts" others had made with the figure drawn out (NEW-ScoutNkisiNkondi-2, section What is Mavungu?, pp. 2–3).
- Treat collection history as part of the object's biography: medicine containers were mostly removed by missionaries or colonial agents, because the power was understood to reside in them (NEW-ScoutNkisiNkondi-2, section How did Mavungu come to the Museum?).

---

### NEW-ScoutNkisiNkondi-3

citation: Cleveland Museum of Art. *Male figure (nkisi nkondi)*, late 1800s–early 1900s, Kongo artist and nganga, accession 2010.432, African Art department, René and Odette Delenne collection. Object record released CC0 through the museum's open-access API (object id 168726); undated record, read 2026-10-22.

url: https://openaccess-api.clevelandart.org/api/artworks/168726

route: direct plain request to the museum's open-access API, HTTP 200, JSON; the public object page `https://clevelandart.org/art/2010.432` also answered HTTP 200.

kind: record

tier: A — the holding museum on its own accession: the descriptions of this figure's condition (mirrored eyes, resin cap, empty stomach chamber) and of how it was disempowered are the museum's own record. B if stretched to statements about minkisi in general.

scope: what a nkisi nkondi looks like after its empowering substances are removed, who empowered it (banganga, plural of nganga), the rule that a figure is desacralised when the nganga takes the materials out, the museum's statement that the finished sculpture was then discarded, and its note that Kongo people sometimes removed such materials as anti-colonial resistance before Europeans seized figures. Does not name this figure's spirit, does not date the removal, and says the museum does not know why this one was disempowered.

quotes:
- object record description, first sentence: "This nkisi nkondi (power figure) lacks most of the materials that transformed it into a vessel for a spirit."
- object record description, second sentence: "Carved by sculptors, minkisi hosted spirits after banganga (priests) placed substances inside to empower them."
- object record description, fourth sentence: "After the nkisi had served its purpose the nganga removed the materials, stripping it of its spiritual power; the remaining sculpture was discarded."
- object record description, fifth sentence: "Sometimes, Kongo people removed materials as acts of anti-colonial resistance, disempowering minkisi before Europeans seized them."

teaches: Cleveland records a nkisi nkondi deliberately stripped of its empowering substances, and notes that Kongo people sometimes removed such materials as anti-colonial resistance.

draft sentences:
- Decide what a stripped object is before you show one: Cleveland says this nkisi nkondi lacks most of the materials that transformed it into a vessel for a spirit (NEW-ScoutNkisiNkondi-3, object record description).
- Separate carving from empowering, and give each a different agent: sculptors carved, and banganga placed the substances that let the spirits in (NEW-ScoutNkisiNkondi-3, object record description).
- Give the object an end as well as a making: when it had served its purpose the nganga removed the materials, stripped its power and the sculpture was discarded (NEW-ScoutNkisiNkondi-3, object record description).
- Let people disarm your objects politically: the museum notes removal of materials as anti-colonial resistance carried out before Europeans seized the figures (NEW-ScoutNkisiNkondi-3, object record description).
- Keep the record's own uncertainty: Cleveland states that it does not know why this particular figure was disempowered, only that it is no longer spiritually active (NEW-ScoutNkisiNkondi-3, object record description, sixth sentence).

---

### NEW-ScoutNkisiNkondi-4

citation: Mack, John. 2011 [1995]. "Fetish: Magic Figures in Central Africa", *Journal of Art Historiography* 5 (December 2011), pp. 54–58 cited here; ISSN 2042-4752; Department of Art History, University of Birmingham. The journal states the essay was originally published in Anthony Skelton (ed.), *Fetishism: Visualising Power and Desire*, London: South Bank Centre with Lund Humphries, 1995.

url: https://arthistoriography.wordpress.com/wp-content/uploads/2011/12/mack-fetish.pdf

route: direct plain request, HTTP 200, application/pdf, 14 pages (redirect from arthistoriography.files.wordpress.com to arthistoriography.wordpress.com), no challenge.

kind: paper

tier: B — open-access peer-reviewed journal article, but a reprint of a 1995 exhibition-catalogue essay: expert interpretation of the class, with no new fieldwork and no primary Kongo text quoted at these pages.

scope: the specialist definition the entry needs: nkisi as a container term with a physical load of medicines, the rule that the object is neutralised without that load, the claim that the power is a named and personalised force from the unseen world of the dead rather than a general one, the rejection of the English word "fetish" as an external classification, and the argument that an encrusted surface is the interface between spirit and supplicant, not the essence. Says nothing about Kongo political history, and its page 54 dating of contact (1482, first baptism 1491, catechism 1556, dictionary 1652) is the essay's summary, not a document citation.

quotes:
- p. 54, section The Myth of the Fetish: "In the end, the perception of these objects as 'fetish' is an entirely spurious external view which classifies objects regardless of indigenous understanding."
- p. 56, section The Object and its Function: "In general, however, all such objects are referred to under the common term nkisi (or plural minkisi) and are thought of as containers."
- p. 56, section The Object and its Function: "Without these elements the nkisi is neutralised."
- p. 56, section The Object and its Function: "The powers, however, are not general but personalised and specific to individual objects which often bear their own name."

teaches: Mack defines nkisi as a container of medicines animated by a named power, and calls the outsider label "fetish" a spurious classification.

draft sentences:
- Treat the term as a container word with a physical core: all such objects are called nkisi or minkisi and are thought of as containers (NEW-ScoutNkisiNkondi-4, p. 56).
- Make power loadable and unloadable, so that an object can be switched off: without the medicines the nkisi is neutralised (NEW-ScoutNkisiNkondi-4, p. 56).
- Put the power's source outside the living world and let containment be what makes it usable: Mack describes nkisi as a power from the unseen world of the dead, otherwise inaccessible to human perception (NEW-ScoutNkisiNkondi-4, p. 56).
- Give each object its own name and reputation rather than a shared office: the powers are not general but personalised and specific to individual objects that often bear their own name (NEW-ScoutNkisiNkondi-4, p. 56).
- Quarantine the outsider's label and say so in the entry: Mack calls the perception of these objects as "fetish" an entirely spurious external view that classifies objects regardless of indigenous understanding (NEW-ScoutNkisiNkondi-4, p. 54).
- Read the encrusted surface as an interface, not an essence: for Mack it lies between the hidden world of the animating spirit and the outer fragile world of the human supplicant (NEW-ScoutNkisiNkondi-4, p. 58).

---

## Findings for the entry's design decisions

| design decision | what the opened records carry | evidence |
|---|---|---|
| what the objects and offices are called and what the words mean | nkisi (plural minkisi) as a container term; nkondi (plural minkondi) glossed "hunter at night"; nganga and its plural banganga for the ritual specialist; the class name Mangaaka for a force of jurisprudence | Mack p. 56; PRM sections What is Mavungu?; Cleveland record; Met label |
| who made and worked them | two offices in one object: Kongo sculptors and ritual specialists, with named ateliers (a master active along the coast of Congo and Angola at the end of the nineteenth century, geography given as the Chiloango River) | Met label, first paragraph |
| what was worn, carried, paid or made | the mpu headdress of chiefs or priests; a nganga's costume with charms attached, striking and frightening by design; a medicine cavity sealed with a mirror that gave the nganga visions of where danger lay; fees paid to invoke a nkondi and further fees to have metal "contracts" drawn out | Met label; PRM What is Mavungu? |
| how the object does its work | metals as record of vows sealed and treaties signed; arousal by nails, gunpowder explosions and insults; power specific and named, so one figure can heal, detect thieves or adulterers, judge and punish | Met label and transcript; Mack p. 56 |
| what changed between periods | materials removed by missionaries and colonial agents because power was thought to reside in them; removal also used as anti-colonial resistance before seizure; museums then displayed such figures as sculpture, which the Pitt Rivers record calls a movement from function to form | PRM How did Mavungu come to the Museum? and Mavungu in the Twentieth Century; Cleveland record |
| where an outsider's record over-reads or misnames | the English "nail fetish" is rejected by the holding museum as an inadequate gloss, and the specialist calls "fetish" a spurious external classification; the nails are invocations and records, not the essence | PRM What is Mavungu?; Mack p. 54 |

Entry budget: if the 230-line entry has to drop a row, drop Cleveland first (it restates the load model) and keep
Pitt Rivers plus Mack for naming and meaning, then the Met for regalia and the metal record.

Cross-source check: three independent museums (New York, Oxford, Cleveland) and one specialist agree on the
load-and-container model (medicines inside, power resident in them, removal neutralises). That agreement is the
strongest single design rule this seat can hand the entry: **the object is not the wood, and a stripped figure is a
different kind of thing from a working one**. [INFERENCE] from that agreement; each source states its own part.

## Caveats the L1 should carry into the rows or the entry

- The word "fetish" appears above only inside quotations, and it is the sources' word: the Pitt Rivers record puts
  "nail fetish" in quotation marks and rejects it, Mack puts "fetish" in quotation marks and rejects it. Do not let
  the entry use it in its own voice.
- The Met label is curatorial interpretation written for a general museum audience; the Met transcript is
  MacGaffey speaking, published by the Met as an audio stop, not a peer-reviewed text. If the entry needs
  MacGaffey's scholarly argument, this record is not it (see unopened).
- The Pitt Rivers record is a 2010 compilation whose practice statements rest on MacGaffey 1993, Thompson 2002 and
  Dennett; the museum is authoritative for Mavungu's own documentation (village of Nganzi in Kakongo, confiscation
  by Portuguese government agents about 1892, Kingsley bequest 1900) and secondary for nkondi practice.
- Cleveland's record is CC0 and machine-readable; its sentences are short and its "we don't know why" caveat should
  survive into the entry rather than being tidied into certainty.
- The Mack PDF is a scan with an OCR text layer (for example "negativify" for "negativity"); the four quotations
  used here were checked on a 200 dpi render of the printed page, not accepted from the text layer.
- None of these four sources carries the Kongo cosmogram or its contested readings; that ground belongs to another
  seat and I did not open it.

## Opened but not rowed

**Cleveland Museum of Art, Power figure (nkisi), 2010.438** — `https://openaccess-api.clevelandart.org/api/artworks/168732`,
HTTP 200, CC0, read 2026-10-22. Its record describes the *nduda* subtype: "This figure is of the nduda type,
characterized by the attached 'guns' loaded with gunpowder and used to shoot witches." and "It is the only figure that
adopts the threatening pose: the right hand raised, holding a spear or knife, and the left hand resting on the hip."
This is a named subtype with a weapon and a single permitted pose, which is useful if the entry wants to show that
minkisi were specialised and named rather than one generic class. Not rowed because the four rows above already
carry the load-and-container rule, and this record duplicates Cleveland's voice.

## Not run

No lane command was run: the entry that consumes these rows does not exist yet, so `python3 -B reports/round-56/accept-c.py`
would only re-measure the base. Nothing in the lane was created or modified except this report. No tool was installed
or upgraded. No git or jj write of any kind was made; scratch files live under
`/fast/scratch/hyaku/kotodama-r56/ScoutNkisiNkondi/`.

unopened: The British Museum collection database (nkisi records) — the search endpoint answered HTTP 403 with a
Cloudflare "Just a moment..." interstitial, challenge met, not passed; no ordinary copy was used, so the British
Museum is not a row. Smithsonian National Museum of African Art (`collections.si.edu` search and `africa.si.edu`
pages) — HTTP 403 on both, not passed; the Smithsonian Open Access API did answer with `DEMO_KEY` but returned
library catalogue records, not object records, so nothing was rowed. Art Institute of Chicago API — HTTP 403. Brooklyn
Museum open collection search — HTTP 429 with a Vercel Security Checkpoint, not passed. Met museum HTML pages —
HTTP 429 Vercel Security Checkpoint, not passed (the Wayback capture was read instead). MacGaffey, "Fetishism
Revisited: Kongo nkisi in Sociological Perspective", *Africa* 47 (1977), and "Complexity, Astonishment and Power",
*Journal of Southern African Studies* 14 (1988) — Unpaywall reports both closed, no open copy found. MacGaffey, "The
Eyes of Understanding: Kongo Minkisi", in *Astonishment and Power* (Smithsonian, 1993) — the Internet Archive copy is
lending-only ("PDF access not available"), which needs a login and does not count; the Haverford College repository
record answered HTTP 403. Cambridge Core search — HTTP 429. Persée search for nkisi and minkisi — the results page
renders client-side and I found no server-side JSON route, so no Persée article was opened. OpenAlex and Semantic
Scholar discovery APIs — HTTP 429 (used only to look for leads, never as sources). Royal Museum for Central Africa
(AfricaMuseum, Tervuren) — the collections pages I reached describe collection management and the human-sciences
holdings in general; I found no object-level record for a nkondi and no route to an online object catalogue, so no
AfricaMuseum record was opened.
