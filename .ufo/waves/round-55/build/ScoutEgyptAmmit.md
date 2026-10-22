# ScoutEgyptAmmit — Ammit in two British Museum papyrus records

- seat: `KotodamaR55.ScoutEgyptAmmit` (scout, claim C ground: monsters and hybrid beings)
- round: kotodama 55 (hyaku phase 4), 2026-10-22
- lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, declaration `8eda9543e940bdc4938fad90182ee6a6fe271d0f`, claim base `f4015e70b829523ed81e14ce4279bfab0e0233e4`
- assignment: claim C source item; the British Museum records for the Papyrus of Hunefer (EA9901,3) and the Papyrus of Ani (EA10470,3), quoting the record's description of the creature and its role in the weighing of the heart
- draft ids used below: `NEW-ScoutEgyptAmmit-1` and `-2`; the L1 assigns the final `S` ids at integration

## Route summary

The live British Museum collection pages answered with a bot challenge and were not passed. Both records were
read from Wayback captures of those same pages. Everything below is quoted from the captured HTML, byte-checked
by substring match against the fetched files (all quotes below: hit, 0 misses).

| record | URL | live status | what was read |
|---|---|---|---|
| EA9901,3, Book of the Dead of Hunefer, frame 3 | `https://www.britishmuseum.org/collection/object/Y_EA9901-3` | direct plain request, HTTP 403 (challenge met, not passed) | Wayback captures `20230319160059id_` (HTTP 200, 211329 bytes), `20260919094742` (HTTP 200, 188089 bytes) and `20200808073903id_` (HTTP 200, 121655 bytes) |
| EA10470,3, Papyrus of Ani, frame 3 | `https://www.britishmuseum.org/collection/object/Y_EA10470-3` | direct plain request, HTTP 403 (challenge met, not passed) | Wayback capture `20240529085805id_`, HTTP 200, 224493 bytes |

Access date for both: 2026-10-22. The record text is server-rendered in these captures (object-detail `<dt>`/`<dd>`
fields, then "Curator's comments"), so the quotes are not an artefact of one snapshot: every Hunefer quote below was
substring-matched in all three captures named above, from 2020, 2023 and 2026, and the wording of the Ammit passage
is identical in each. Both records are the museum's own catalogue entries for objects in its Department of Egypt and
Sudan, each carrying its own bibliography, exhibition history and conservation fields, which are not used here.

---

### NEW-ScoutEgyptAmmit-1

citation: The British Museum, Department of Egypt and Sudan. Collection online record, museum number EA9901,3 ("papyrus"; Book of the Dead of Hunefer, frame 3), registration number 1852,0525.1.3, 19th Dynasty, acquired 1852. No author and no publication or revision date printed on the record. The record itself cites Trismegistos text 134351 as a stable external id.

url: https://www.britishmuseum.org/collection/object/Y_EA9901-3

route: direct plain request returned HTTP 403 (bot challenge: challenge met, not passed); record read from Wayback capture `20230319160059id_` of the same URL, HTTP 200, 211329 bytes; the same passage re-checked in captures `20260919094742` and `20200808073903id_`. Access date 2026-10-22.

kind: record

tier: A — the holding museum's own catalogue record for its own object, and the museum's own description of that object's scene and inscription; authoritative for what this record says about this papyrus. The English of the inscription is the museum's rendering, not a named scholarly edition, so the row does not support a claim about the Egyptian wording of the epithet or of the body formula.

scope: this frame of Hunefer's papyrus as the museum describes it — object type and decoration, the judgement vignette's running order (Hunefer adoring a named company; Anubis leading him to the balance; the balance's two pans; Ammit below the balance; Thoth writing; Horus conducting Hunefer to Osiris), the museum's gloss of Ammit as "Devourer of the Damned", the three-part body formula quoted as the inscription beside her, the museum's dating of the genre from c.1450 BC and its statement about scribes and draftsmen, the presence of spell 30B passages, and the catalogue's indexing of Ammit under "Representation of". Does not support: the Egyptian name or etymology, any statement that this is spell 125, what happens to a heart that fails, any period change in the figure, or any location beyond the findspot field "Egypt".

quotes:
- Description: "Book of the Dead of Hunefer (Hw-nfr) frame 3; fully coloured vignettes; coloured border."
- Description: "The scene (vignettes) shows episodes in Hunefer's judgement."
- Curator's comments, first paragraph: "'Book of the Dead' papyri are first found in the early New Kingdom c.1450 BC"
- Curator's comments, first paragraph: "the finest (like Hunefer's) were written by expert scribes and decorated by master draftsmen"
- Curator's comments, first paragraph: "Perhaps, as royal scribe, it was Hunefer himself who put brush to ink to inscribe his own papyrus."
- Curator's comments, second paragraph: "Below the balance crouches Ammit, the 'Devourer of the Damned', accompanied by a short inscription which describes her:"
- Curator's comments, second paragraph, the inscription as the record renders it: "'Her front is a crocodile, her rear a hippopotamus, her middle a lion.'"
- Curator's comments, second paragraph: "On the left scale-pan is Hunefer's heart, and on the right the feather hieroglyph which symbolises Maat."
- Curator's comments, second paragraph: "Thoth, ibis-headed, holds a pen and scribal palette to record the outcome of the weighing."
- Curator's comments, second paragraph: "The lines of inscription above the scenes contain passages from spell 30B of the Book of the Dead."
- Associated names field: "Representation of: Ammit (represented in the vignette)"

teaches: The record names Ammit as devourer, quotes a three-part body formula, and sets her below the balance while Thoth writes the verdict.

draft sentences:
- Decide whether the name is a job title: the record calls her Ammit, glosses her as the "Devourer of the Damned", and its own English keeps a feminine pronoun for her (NEW-ScoutEgyptAmmit-1, Curator's comments, second paragraph).
- Build the body from three named donors and let the culture's text say it, because the museum gives the formula as the inscription beside the figure rather than as its own description (NEW-ScoutEgyptAmmit-1, Curator's comments, second paragraph).
- Place the being at the apparatus, not in a landscape: she crouches below a balance whose pans hold the heart and the feather hieroglyph that symbolises Maat (NEW-ScoutEgyptAmmit-1, Curator's comments, second paragraph).
- Give the scene a clerk, since Thoth holds pen and palette "to record the outcome of the weighing", which makes the monster wait on a written verdict rather than on appetite (NEW-ScoutEgyptAmmit-1, Curator's comments, second paragraph).
- Choose the object and its makers deliberately: a fully coloured papyrus of vignettes, in a genre the museum dates from c.1450 BC and whose finest copies were written by expert scribes and decorated by master draftsmen (NEW-ScoutEgyptAmmit-1, Curator's comments, first paragraph).
- Pair the devourer with a spell: the lines above these scenes carry passages from spell 30B, so decide what ritual text stands beside your monster and who is licensed to copy it (NEW-ScoutEgyptAmmit-1, Curator's comments, second paragraph).

---

### NEW-ScoutEgyptAmmit-2

citation: The British Museum, Department of Egypt and Sudan. Collection online record, museum number EA10470,3 ("'Book of the Dead', Papyrus of Ani, frame 3"), registration number 1888,0515.1.3, 19th Dynasty, production date 1250BC (circa), findspot Tomb of Ani (Thebes). No author and no publication or revision date printed on the record.

url: https://www.britishmuseum.org/collection/object/Y_EA10470-3

route: direct plain request returned HTTP 403 (bot challenge: challenge met, not passed); record read from Wayback capture `20240529085805id_` of the same URL, HTTP 200, 224493 bytes, access date 2026-10-22.

kind: record

tier: A — the holding museum's own record for its own papyrus, written by the department that curates it; authoritative for the scene as this record describes it. The description is the museum's prose about the vignette, not a translation of the papyrus's own spell text.

scope: the museum's account of Ani's judgement scene — the Hall of Judgment, the balance with heart and feather of Maat, the baboon form of Thoth on the upright, Anubis steadying the pan, Thoth as scribe of the gods with palette and reed brush, the unnamed monster on a mat behind Thoth ready to consume the heart if Ani fails, its composite parts, the gods seated to deliver judgment with Shay, Renenutet and Meskhenet observing, Ani and Tutu entering, spell 30B addressed to the heart, and the favourable outcome. Also the record's own fields: 19th Dynasty, production date, Thebes findspot, associated title "Book of the Dead (Chapter 30B)", and the indexing "Representation of: Ammit". Does not support: that the papyrus's own text names Ammit (this description never does), the Egyptian form of the name, the monster's fate or afterlife, or any comparison with other periods.

quotes:
- Description: "the scene is the Hall of Judgment"
- Description: "On a mat behind Thoth sits a monster ready to spring forward to consume Ani's heart if he fails to pass the test."
- Description: "This creature has the head of a crocodile, the forepart of a lion, and the hindquarters of a hippopotamus."
- Description: "he is the scribe of the gods"
- Description: "ready to note down the results of Ani's interrogation"
- Description: "the great gods of Egypt are shown, formally seated on thrones, waiting to deliver judgment"
- Description: "Ani mutters the words of Spell 30B of the 'Book of the Dead', which are addressed to his heart in the balance."
- Description: "All, it seems, goes well for Ani; he has qualified for the Afterlife."
- Associated names field: "Representation of: Ammit"
- Production date field: "1250BC (circa)"

teaches: A second papyrus record leaves the same being unnamed, calls it a monster, rebuilds it from three animals and makes it eat a failing heart.

draft sentences:
- Decide whether your bestiary names a being or only describes it: this record's description calls her "a monster" throughout and never uses the name, while the catalogue indexes her as "Representation of: Ammit" (NEW-ScoutEgyptAmmit-2, Associated names field).
- Make the devouring conditional rather than habitual: she sits ready to spring forward and consume the heart only if the dead man fails the test, so the monster is the consequence of a verdict (NEW-ScoutEgyptAmmit-2, Description).
- Recompose the body by naming a head, a forepart and hindquarters from three different animals, and decide whether your culture fixes that order or lets each workshop settle it (NEW-ScoutEgyptAmmit-2, Description).
- Site the monster in a furnished room with an audience: the scene is the Hall of Judgment, she sits on a mat behind Thoth, and the great gods are formally seated on thrones waiting to deliver judgment (NEW-ScoutEgyptAmmit-2, Description).
- Keep a clerk inside the scene, because Thoth is the scribe of the gods with palette and reed brush, ready to note down the results of the interrogation (NEW-ScoutEgyptAmmit-2, Description).
- Fix the stakes with a spell and a verdict: the dead man mutters spell 30B, addressed to his heart in the balance, and the record closes with him qualified for the Afterlife (NEW-ScoutEgyptAmmit-2, Description).

---

## Findings for the entry's design decisions

Every line is observed in the two records unless marked inference. The comparison column is the useful part for
the entry: the same museum, the same department, the same period, two papyri, and two different ways of handling
the same creature.

| design decision | what the two records carry | evidence |
|---|---|---|
| what the culture calls the being, and what the word means | Hunefer's record gives a proper name plus a functional gloss, "Ammit, the 'Devourer of the Damned'"; Ani's record gives no name in its description at all, only "a monster", and the name survives only in the catalogue field. No Egyptian word, etymology or translation of the name is given by either record | EA9901,3 Curator's comments, second paragraph; EA10470,3 Description and Associated names field |
| how its body is composed | two part-lists of the same three animals in different arrangements. Hunefer's inscription, as the record renders it: "Her front is a crocodile, her rear a hippopotamus, her middle a lion." Ani's description: "This creature has the head of a crocodile, the forepart of a lion, and the hindquarters of a hippopotamus." | EA9901,3 Curator's comments, second paragraph; EA10470,3 Description |
| where it lives relative to the known world | not in a landscape: below the balance (Hunefer), on a mat behind Thoth in the Hall of Judgment (Ani). The only geography is the object's findspot — "Egypt" for Hunefer, "Tomb of Ani (Thebes)" for Ani | EA9901,3 Findspot field and Curator's comments; EA10470,3 Description and Findspot field |
| whether it warns, guards, punishes, teaches or devours | devours, and only as a sanction: Ani's record makes consumption conditional on failing the test; Hunefer's record names her devourer of the damned but does not say what she does. Neither record makes her a guardian, an omen or a teacher | EA10470,3 Description; EA9901,3 Curator's comments, second paragraph |
| who records or depicts it, and in what book or object | a funerary papyrus with fully coloured vignettes, made for a named individual (royal scribe Hunefer; Ani and his wife Tutu), by scribes and master draftsmen, and possibly by the owner himself; inside the scene the record-keeper is Thoth with pen, palette and reed brush. The catalogue files Ammit in the same "Representation of" list as Osiris, Isis, Nephthys, Anubis, Thoth and Horus | EA9901,3 Description and Curator's comments, first and second paragraphs; EA10470,3 Description; both records' Associated names fields |
| what changes across periods | nothing in these two records: both are 19th Dynasty, and Hunefer's record carries no production date at all, only the culture/period field, while Ani's is dated 1250BC (circa). The only temporal statement is about the genre — Book of the Dead papyri "first found in the early New Kingdom c.1450 BC" | EA9901,3 Cultures/periods and Curator's comments, first paragraph; EA10470,3 Production date field |

### The detail most useful to a worldbuilder, and not obvious from the entry's outline

The monster stands inside a procedure with a written outcome. In Hunefer's frame the sequence the museum records
runs Anubis leading the man to the balance, the heart against the feather of Maat, Ammit crouching below, Thoth
holding "a pen and scribal palette to record the outcome of the weighing", and Horus then conducting Hunefer to
Osiris. In Ani's frame the same order holds with the addition that the monster is "ready to spring forward" and
that Thoth is "ready to note down the results of Ani's interrogation". Both records also place spell 30B in the
same scene. Hunefer's record says: "The lines of inscription above the scenes contain passages from spell 30B of
the Book of the Dead." Ani's says that he "mutters the words of Spell 30B of the 'Book of the Dead', which are
addressed to his heart in the balance". The counter-measure to the devourer is therefore a text spoken to the
heart, not a weapon or an amulet — observed in both records, and the single most transferable design move in this
pair.

### Caveats the L1 should carry into the rows or the entry

- Access: the live British Museum pages returned HTTP 403 to a plain request. The challenge was met, not passed;
  both records come from Wayback captures of the same URLs, and the capture ids belong in the route text because
  the URL alone does not say which snapshot was read. The Hunefer wording was checked in three captures from 2020,
  2023 and 2026, so a later revision of the page, if one exists, does not affect these quotes.
- Neither record gives the Egyptian name, an etymology, or a translation warrant for "Devourer of the Damned"; the
  English is the museum's. Do not build an entry sentence on the etymology of "Ammit".
- Neither record says what happens to a heart that fails: Hunefer's record stops at the epithet, Ani's at the
  creature's readiness. The entry must not assert that the heart is eaten in either papyrus.
- Ani's description does not name the creature; the name appears only in the catalogue's associated-names field.
  Any sentence of the form "the papyrus calls her Ammit" would be false for this record.
- The two body formulas disagree in arrangement, not in the animals used. That is a fact about two records, not
  evidence of a chronological change; the entry should present it as variation between copies.
- Both records are 19th Dynasty Theban funerary papyri, so nothing here supports the entry's "what changes across
  periods" decision. That decision needs a source outside this pair (see unopened).
- The museum indexes Ammit among represented deities rather than in a separate monsters category; that is a fact
  about this catalogue's practice, not about Egyptian classification.

## Not run

No lane command was run. This is a read-only scouting seat and the entry that consumes these rows does not exist
yet, so `python3 -B reports/round-55/accept-c.py` would only re-measure the base (0 cited ids, 230 files) and would
tell the L1 nothing it does not already have in the claims file. No file in the lane was created or modified
except this report. No tool was installed or upgraded.

unopened: the British Museum's live pages for both objects, which returned HTTP 403 to plain requests (challenge
met, not passed) and were replaced by the captures named above; the Met's record for 66.99.142, a Ptolemaic
"Part of a funerary papyrus showing the judgment before Osiris" dated ca. 230–150 BCE, whose open API record
carries no description text and whose website page answered HTTP 429 — not opened, and it is the obvious
candidate for the "what changes across periods" gap, if a later seat wants it; the Louvre collections search for
"Ammit", HTTP 429 on two attempts, not opened; the Museo Egizio (Turin) collections search, which answered HTTP 200
but served a page whose text does not contain the search term, so not opened; the British Museum's
Papyrus of Ani landing page for the whole manuscript (`Y_EA10470-1`/`,2`), not opened, since the frame carrying the
judgement is the one read here; and the museum's own bibliographic citations on both records (Taylor 2010, Parkinson
2010, Quirke 1993, Strudwick 2006), read only as titles in the records and not opened, because they are print
monographs and outside this seat's question.
