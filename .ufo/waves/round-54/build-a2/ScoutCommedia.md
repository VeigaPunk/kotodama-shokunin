# ScoutCommedia — commedia dell'arte: the mask as stock type, and dialect as the type's licence

Round 54, attempt 2. Seat: source scout for claim C entry `corpus/knowledge/culture-material/masks-masquerade.md`.
Slice: commedia dell'arte masks (Arlecchino, Pantalone, Il Dottore, Brighella) — the mask as a stock type
carrying a fixed dialect, costume and behaviour. Two sources opened this session (2026-10-22), both by
ordinary means; one direct, one through a Wayback capture after the direct route answered with a block.

Axes I worked: (1) independent sources opened this round, (2) source tier against the exact scope,
(3) design decisions a worldbuilder can act on (who may wear, what the mask is, when it appears, what it
licenses, what is restricted), (4) calibration — what the entry must not claim.

## Gap re-checked at base (my own commands, lane root, 2026-10-22)

```
find corpus/knowledge -iname '*mask*'            -> 0 lines (0 filename owners)
grep -rlE '^- topic:.*(mask|masquerad)'          -> corpus/knowledge/civilizations/siam-thai.md (1 topic owner)
grep -rliE '\bmask(s|ed|ing)?\b|masquerade'      -> 41 files
grep -rn -i 'commedia' corpus/knowledge          -> 1 hit: culture-material/garment-lexicon-crosslinguistic.md:90
```

The commedia partial owner is **`culture-material/garment-lexicon-crosslinguistic.md:90`** ("*Pantaloon* <
Pantalone, the Venetian merchant of commedia dell'arte — a stage costume became a trouser word"). That file
owns the loanword/garment-lexicon claim; the new entry should point at it for the trouser-word drift and not
restate it. No file in `corpus/knowledge` currently treats a mask as an object, a type or a licence.

## Sources, in the wave's row shape

### NEW-ScoutCommedia-1

citation: Crick, Olly. 2023. "Commedia dell'Arte: The Mechanisms of Othering." In *Representing Alterity through Puppetry and Performing Objects*, ed. John Bell, Matthew Isaac Cohen and Jungmin Song. Storrs: Ballard Institute and Museum of Puppetry, University of Connecticut. Digital Commons item 15, https://digitalcommons.lib.uconn.edu/ballinst_alterity/15
url: https://digitalcommons.lib.uconn.edu/cgi/viewcontent.cgi?article=1002&context=ballinst_alterity (chapter PDF); landing page https://digitalcommons.lib.uconn.edu/ballinst_alterity/15
route: landing page opened by plain request, HTTP 200, citation metadata read (author, title, date 2023, PDF URL); the PDF URL answered a plain request with HTTP 403 and a Cloudflare interstitial, which was met and not passed and was left unanswered; the same PDF was then read from the Wayback Machine capture `20240220134922` of that URL (HTTP 200, application/pdf, 261,509 bytes, 15 PDF pages = printed pp. 1–14); access date 2026-10-22
kind: paper (book chapter, open-access repository copy)
tier: A — the chapter author's own argument about regional othering and stage dialect in commedia, which is the scope this row is filed for; the historical facts he reports from Carlson (2009), Crohn Schmitt (2014) and Smith (1968), and the table he calls "indicative", are second hand in this row and B on their own
scope: that each Mask is a fixed type bundling a region, a social class and a regional stage dialect; that the spoken dialect was a comic theatrical remodel of the regional one, adjusted to each audience; that the mockery a Mask licenses is audience- and venue-dependent and was protected by patronage; nothing about mask-making as a craft, nothing about which physical masks survive, nothing about women's or unmasked roles' access rules
quotes:
- p. 6: "The Lovers came from Turin; Pantalone from Venice; the Doctor from Bologna; and the Zannis from Bergamo and the Po Valley"
- p. 7, Table 1 caption: "Commedia roles showing differentials of social class and regional origin."
- p. 7, Table 1, row Il Dottore, column "Place of Origin and Accent/Dialect": "Il Dottore | Academic Bourgeoisie | Bolognese Macaronic"
- p. 9: "the language spoken by each Mask, therefore, was not the pure dialect of the region, but a performatively comic version"
- p. 11: "whether the performance aims toward a positive or a comically reductive model of each region, the performative accent stays"
teaches: a commedia Mask is a place-plus-class-plus-speech package whose dialect is a deliberately comic stage version of the regional one; the accent is the type's fixed part, while whether the type is honoured or ridiculed depends on the town, the audience and the plot, and the troupe buys protection for that licensed mockery from secular patrons
draft sentences:
- Treat the mask as a bundle of origin, class and speech rather than a face: Crick's table assigns Pantalone to the Venetian mercantile bourgeoisie, Il Dottore to the Bolognese academic bourgeoisie speaking macaronic Bolognese, and Harlequin to a Bergamese recent arrival in the city (NEW-ScoutCommedia-1, p. 7, Table 1).
- Write the mask's speech as a stage dialect built from a regional one, not the region's real speech: the language spoken through each Mask was "not the pure dialect of the region, but a performatively comic version" (NEW-ScoutCommedia-1, p. 9).
- Keep the accent fixed while the type's valuation flips: the same Mask can stand for its region's way of life or for everything ridiculous about it, and "the performative accent stays" (NEW-ScoutCommedia-1, p. 11).
- Decide who the mask is licensed to mock, and let that change per venue, since the troupe "needs to socially fit in but perform difference" and aimed its comedy at whoever the local audience already othered (NEW-ScoutCommedia-1, pp. 9, 2).

### NEW-ScoutCommedia-2

citation: Victoria and Albert Museum, London. "Mask for the Commedia dell'Arte character Pulcinella", accession W.60-1929, made in Italy 1700–1725, maker unknown, given by Charles R. Beard, Theatre and Performance Collection.
url: https://collections.vam.ac.uk/item/O1113999/mask-for-the-commedia-dellarte-mask-unknown/
route: plain request, HTTP 200, page text read (title, date, place, materials and techniques, physical description, dimensions, credit line, object history, bibliographic reference); corroborated by the museum's own JSON record https://api.vam.ac.uk/v2/museumobject/O1113999 (plain request, HTTP 200); access date 2026-10-22
kind: record (holding museum's catalogue record for the object)
tier: A — the holding museum's own record of its own object for date, place, materials, technique, dimensions, accession and provenance note; B for the record's interpretive summary of the character's history and its English afterlife, and the identification itself is hedged in the record's brief description ("probably the Commedia dell'Arte character Pulcinella"), so the row supports "a leather mask catalogued as Pulcinella", not "Pulcinella's mask"
scope: how one commedia mask was made (moulded leather, cuir bouilli, over a wooden form), what survives of the craft (a second mask from the same mould, and a wooden Harlequin-mask mould held at the Palais Galliera), the mask's form (half-mask, upper face, tie, 19 × 15 × 11.5 cm), the character's loosened occupation range by the early 18th century, and the type's survival in English pantomime as Mr Punch; nothing about performance practice, dialect, or who was allowed to wear it
quotes:
- Description: "This moulded leather mask for the character of Pulcinella dates from the early 18th century"
- Materials and techniques: "The leather can then be moulded by hand in a press or over wooden forms."
- Object history: "Another mask, taken from the same mould, was recorded as being in the Mariano Andreu Collection"
- Description: "Whereas earlier versions had a moustache and beard hiding most of the actor's face, this is a half-mask."
teaches: the surviving commedia mask is a reproducible type-face, cast from a shared wooden form rather than carved as a portrait, worn as a half-mask that leaves the mouth free; its character could change trade while the mask stayed, and the type outlived both its stage role and its genre
draft sentences:
- Make the mask an object reproduced from a form, not a portrait: this leather half-mask was moulded over a wooden form, and another mask "taken from the same mould" was recorded in a private collection (NEW-ScoutCommedia-2, Materials and techniques; Object history).
- Free the mouth and fix the eyes: the surviving mask covers the upper face only, where earlier versions hid most of the actor's face behind moustache and beard, so the design choice is how much of the speaker the type is allowed to keep (NEW-ScoutCommedia-2, Description).
- Let the type outlive its trade and its genre: by the early 18th century Pulcinella could be a peasant, a dentist, a physician, a painter or a soldier, and he survived in Britain as Mr Punch after the stage part died (NEW-ScoutCommedia-2, Description).
- Record the hedge: the museum catalogues the object as "probably" Pulcinella, described by feature — a protruding nose and a lump on the left temple — so an identification by feature is exactly as strong as the feature list it rests on (NEW-ScoutCommedia-2, brief description; Physical description).

## Extra verbatim passages opened this session (for the L1 to swap into `quotes:` if it prefers them)

Crick 2023, from the same PDF capture:
- p. 2: "making their comic targets those othered by the inhabitants of each town and venue they performed in"
- p. 9: "The troupe needs to socially fit in but perform difference."
- p. 11: "dependent on secular patronage for income and for protection from the censorious Catholic church"
- p. 9, Crick quoting Carlson quoting Blunt (second hand twice over — use only as a definition of stage dialect): "A stage dialect is a normal dialect altered to the requirements of theatrical clarity and dramatic presentation"

V&A record, from the same page:
- Description: "Pulcinella was not necessarily a servant, but might be a peasant, a dentist, a physician, a painter or a soldier."
- Description: "he has survived in the UK in the form of Mr Punch in Punch and Judy shows."
- Materials and techniques: "An example of such a wooden form (used to produce Harlequin masks) can be found in the collections of the Palais Galliera" — Bibliothèque-musée de l'Opéra, MUSEE-34 (1); the record also names two Harlequin leather masks there, BMO MUS 297 (2) and BMO MUSEE-35 (1).
- Object history: the donor, Charles R. Beard, wrote up the mask in *The Connoisseur*, January 1930, and recorded its earlier history as unknown; a Neapolitan attribution for the other casting rests on unknown evidence.
- Record fields: accession W.60-1929; made Italy 1700–1725; height 19.0 cm, width 15.0 cm, depth 11.5 cm; credit line "Given by Charles R Beard"; categories Entertainment & Leisure / Pantomime / Theatre / Theatre costume.

## What this pair settles for the entry, and where the line runs

| Worldbuilding decision | What the two sources carry | Where to stop |
|---|---|---|
| Is the mask a portrait, a presence or a type? | A type: a casting from a shared mould (NEW-2), a bundle of place + class + speech (NEW-1, Table 1) | Not a portrait of a named person; the record does not say whose face the form was cut from |
| Who may wear it | Whoever can carry the type's region and class in voice — the type's identity is audible, not just visible (NEW-1, pp. 6–9) | The pair says nothing about gender, age or guild rules of access; do not invent them from these rows |
| What the wearer may say | Licensed mockery of the group the local audience already others, tuned per town, under patronage protection (NEW-1, pp. 2, 9, 11) | The licence is not general satire: it is aimed at targets the audience already holds in contempt |
| What the mask fixes | The accent and the stage dialect, even when the type's valuation flips between pride and ridicule (NEW-1, p. 11) | Not a fixed "pure" dialect: the stage speech is a comic remodel (NEW-1, p. 9) |
| How it is made | Moulded leather over a wooden form, cuir bouilli, half-mask with a tie (NEW-2) | One surviving object and one surviving mould class; do not generalise to all masks or to all characters |
| When and where it appears | Professional touring troupes, piazzas and hired venues, 16th–18th c. Italy and beyond; the object is dated 1700–1725 (NEW-1, NEW-2) | The pair gives no ritual, funerary or festival calendar — that belongs to the other scouts' rows |
| How the type ends | It can change trade while the mask stays, then leave the theatre: pantomime Harlequin, Mr Punch (NEW-2) | The drift is English and later; it is not evidence about Italian practice |

Calibrations the entry must carry, in the sources' own terms:
- "The Masks" is the trade's own shorthand for the *roles*; Crick uses "Mask" for the role throughout (pp. 6, 9, 11), so object and type share one word — the entry may use that, sourced to this row.
- Not every commedia character wore a mask. My sources show masked servant and master types (Pantalone, Il Dottore, Brighella, Harlequin, Pulcinella) and unmasked lovers and actresses in Table 1; the entry should not write "commedia characters wore masks" without that qualification. (Taviani, below, states the same limit explicitly, but I am not proposing his row.)
- The identification of the V&A object is hedged ("probably"); the strongest citable fact is the hook-nosed, lump-templed, half-face leather mask dated 1700–1725.

## Leads I opened but do not propose as rows

- Taviani, Ferdinando. 2018. "Knots and Doubleness: The Engine of the Commedia dell'Arte." In *Commedia dell'Arte in Context*, pp. 17–33. Cambridge UP, doi 10.1017/9781139236331. The chapter page answered a plain request with HTTP 429 ("Too many automated requests from this network"), which was met and not passed. I read it only from the Wayback capture `20251207000952` of the chapter page; that capture contains the chapter's full HTML body, and the page's own text ("As you have access to this content, full HTML content is provided on this page") suggests it was rendered to a reader with access, which I cannot verify from the capture. **Recommendation: leave it out of the registry or file it as a C lead, not as support for the entry.** Two passages, quoted here only so the L1 can judge, not for citation: "There are no real characters, only stock characters who always have the same name, the same costume and the same mask, passing from one commedia to the other" (section on the formula, p. 17–18 area); "commedia delle maschere, because it was based on stock characters and some of them wore masks" (opening section, on the names of the form). The second sentence is the cleanest statement of the mask-is-not-everyone limit that I met this session.
- Paris Musées / Palais Galliera collection search: HTTP 503 "Service indisponible" on a plain request; not retried, not opened. The Harlequin leather masks (BMO MUS 297 (2), BMO MUSEE-35 (1)) and the wooden mould (MUSEE-34 (1)) are therefore known to me only through the V&A record's cross-reference — cite them as the V&A record's statement, never as a Galliera record.

## unopened

- `https://www.cambridge.org/core/books/commedia-dellarte-in-context/knots-and-doubleness/A4773CCF4E5C8B279CF8CD4C886F130C` — HTTP 429 rate block on two plain requests; the Wayback capture I did read is of uncertain rendering status, so it is a lead, not a row (above).
- `https://digitalcommons.lib.uconn.edu/cgi/viewcontent.cgi?article=1002&context=ballinst_alterity` — HTTP 403 Cloudflare interstitial; met and not passed; content read from the Wayback capture recorded in NEW-ScoutCommedia-1.
- `https://www.parismuseescollections.paris.fr/fr/recherche?q=arlequin+masque+cuir` — HTTP 503; not opened.
- Nothing else was attempted: the pair above already covers this slice's design point, and further museum records would restate NEW-ScoutCommedia-2.

## Notes for the L1

- Suggested `used-by` target for both rows: `corpus/knowledge/culture-material/masks-masquerade.md` only.
- Suggested couples targets this slice can honestly feed: `culture-material/costume-semiotics.md` (the type-as-dress-code carrier), `culture-material/garment-lexicon-crosslinguistic.md:90` (Pantaloon; point, do not restate), `myth-symbol/ritual-liminality.md:117` (mask as liminal medium — that file owns the liminal reading, this slice supplies the theatrical-type mechanics), `linguistics/sociolinguistics-registers.md` (stage dialect as a performed register).
- Remaining unknown in my slice, for the entry's honesty: no opened source here addresses women's access to masked roles, the mask-makers' guild, or the prohibition side (where masking was banned or restricted). Those must come from another scout's rows or be marked `(to-verify)`.
- Tool installs or upgrades: none. No pacman, no network installs.
- Checks I did not run (not mine to run): `python3 -B reports/round-54/accept-c.py`, the census, and the access checker over the finished registry.
