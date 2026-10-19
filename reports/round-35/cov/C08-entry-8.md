- Seat: C08 | executor | claim C | date 2026-10-19 | baseline 4a7aede

# C08 — entry author fragment: `sacred-kingship-mythic-charter` (myth-symbol, entry 8 of 10)

- round 35, seat C08 (entry author, claim **C** coverage). Mission: "Author entry 8
  (myth-symbol) with the same contract" — the C01 contract: the FULL entry bytes as
  one fenced block, frontmatter-complete, sourced, gap-named, decision-record
  carrying, every source pointer resolving or marked `to-verify` in-file.
- lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`; baseline
  `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4` (`reports/round-35/claims.json`); HEAD
  at write time `4a7aede` (measured: `git rev-parse HEAD` → `4a7aede22cd…`).
- canon: **NON-CANON**. This fragment drafts bytes; it admits no entry, certifies no
  round, and decides no canon (`corpus/QUALITY.md` item 5; canon is lore-shokunin's).
- writes: this fragment only (plus gitignored `.scratch/`). No `corpus/**` byte, no
  `tools/**` byte, and no filed round byte is written by this seat. Nothing in this
  fragment is applied; the integrator applies §3 and §5.

## 1. Deliverable

`corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md` — one new
myth-symbol entry (myth-symbol 19 → 20 as far as this seat is concerned; the round's
claim C total is the integrator's sum across C01–C10). The full entry bytes are in §3
inside one fenced block; the proposed index row is in §5 (C11 owns the README delta);
the header/apparatus evidence is in §4.

**Section numbering, stated once:** the fragment's own sections are §1–§3 (above the
fence) and §4–§7 (below it). The **entry's** sections are §1–§13 and are numbered
inside the fenced block only — a `## N.` heading that appears between the fences
belongs to the entry, not to this fragment. Nothing in the fragment's numbering refers
to the entry's sections.

Gap slug: **`sacred-kingship-mythic-charter`** — first author, no collision known at
write time (no `reports/round-35/cov/` fragment existed when this seat started; the
collision protocol is stated in §6).

## 2. Gap and why it is not filler

The partition carries kingship only as a by-product of other subjects. Nine of the
nineteen myth-symbol files mention it in passing; **none states the institution**.

| file:line | what it carries | what it is not |
|---|---|---|
| `myth-symbol/myth-ritual-theories.md:32-35,85` | Frazer's divine king and Hooke's ritual-kingship pattern **as a collapsed theory of myth's origin**, and divine kingship as a worldbuilding use of that theory | not the institution: no legitimation channels, no failing-king devices, no installation, no register |
| `myth-symbol/hero-journey-variants.md:56-57,110` | Raglan's 22-point **king pattern** as a hero-biography score; one clause assigning it to "sacred-kingship agrarian polity" | not the charter the pattern legitimates |
| `myth-symbol/pantheon-archetypes.md:49,61` | war gods "legitimize kingship by victory"; the dragon-slaying formula as "the charter of kingship" (one line each) | not the office that receives the charter |
| `myth-symbol/cosmology-cosmography.md:38,108` | celestial-pivot kingship in early China; the akītu king's cheek-strike and sceptre restoration, flagged late-attested/contested | not the system that stages it |
| `myth-symbol/plant-symbolism.md:77` | Frazer's sacred king, recorded **to warn** that the framework contaminates a world bible | not a treatment |
| `myth-symbol/ritual-liminality.md:40` | the status-reversal rite in which the king is ritually humiliated | not installation or succession |
| `myth-symbol/creation-myths-taxonomy.md:90,110,133`; `flood-traditions.md:26,34,76` | kingship as an implied value of the combat cosmogony; kingship re-founded after the deluge | not the ruler's charter |
| `civilizations/benin.md:42`; `civilizations/persia-achaemenid.md:1` | culture-specific divine-kingship treatments | culture files, not partition method; this entry couples to them instead of restating them |

Absence sweep, 2026-10-19, lane root, over `corpus/knowledge/`:
`for t in "divine kingship" "sacred kingship" "Hocart" "stranger-king" "regicide" "Sed festival" "devarāja" "Golden Stool" "mascapaycha" "k'uhul ajaw" "iyoba" "Ngwenyama" "Ndlovukati" "Kantorowicz" "royal touch" "king's two bodies" "ixiptla" "rex sacrorum" "sar puhi" "substitute king" "Feeley-Harnik"; do printf "%-22s %s\n" "$t" "$(grep -rli -- "$t" corpus/knowledge/ | wc -l)"; done`

| term | files | reading |
|---|---:|---|
| `divine kingship` | 3 | only `myth-ritual-theories.md:35,85` inside this partition |
| `sacred kingship` | 3 | theory-side mentions |
| `regicide` | 2 | `era-periodization-models.md:69`, `myth-ritual-theories.md:35` |
| `Hocart`, `stranger-king`, `Sed festival`, `Kantorowicz`, `king's two bodies`, `royal touch`, `rex sacrorum`, `Feeley-Harnik`, `mascapaycha`, `k'uhul ajaw`, `Ngwenyama`, `Ndlovukati`, `šar pūhi` | **0 each** | the institution's own vocabulary is absent from the corpus |
| `devarāja` / `Golden Stool` / `iyoba` / `ixiptla` / `substitute king` | 1–2 each | all culture-specific, none method |

Partition census at the same stamp (this is claim C's declared *before*, reproduced):
`for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done` → `21 / 19 / 18 / 29 / 20 / 94`;
`find corpus/knowledge -name '*.md' | wc -l` → `201`.

Why the entry is craft and not filler: it converts the four questions a polity cannot
leave open (who may rule / why them / what makes them able / what happens when they
fail) into a channel table with per-channel political cost, a conditional-vitality
table with an **observable channel** requirement, a failing-king device table with a
**reliability grade per device** (the regicide thesis is graded weak-to-contested and
the substitute king strong), a taboo cost-accounting rule, an installation beat-sheet,
and the lane's own half — the **royal register** as grammar (address levels, the
ruler's first person, the spokesman office, name taboo, praise-recitation, oath and
accession formulae), coupled to eight existing language files. It states its
unverified surface in-file (§12 of the entry: 61 `to-verify` marks on 47 lines,
counted by the house gate — §4 below).

## 3. The entry bytes (for the integrator to land at `corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md`)

````markdown
# Sacred kingship — the mythic charter of rule and the royal register

- topic: how a myth system legitimates a ruler — the eight legitimation channels (divine descent, incarnation or vessel, delegation from a god, election and acclamation, conquest-and-test, installation rite, marriage-alliance into the divine line, and the regalia as found title-deed) with attested exemplars and the political cost of each; the king's-body-is-the-land's-body doctrine and the rule that it needs an observable channel (flood, harvest, weather, plague, victory) or it is decoration; the failing-king device family (regicide, jubilee or renewal, substitute king, mock king, abdication, interregnum) with a reliability grade per device; dual and co-sovereign slots (the king's two bodies, queen-mother and she-elephant pairs, the priest-versus-warrior split); installation and regalia; taboo and seclusion cost accounting; the stranger-king and the pedigree-distance rule; the re-legitimation toolkit for usurpers and the reception check; and the **royal register** — the speech levels addressed to the ruler, the ruler's own first person, the spokesman institution, name taboos, praise-recitation as performed pedigree (oríkì, royal hymns), and the oath formula — with a build order, a decision record, and a calibration shelf for the Frazer–Hocart divine-kingship tradition. Reference and method only; canon decisions belong to lore-shokunin.
- gap filled: the partition carries kingship as a **by-product of other subjects** and has no entry for the institution itself. `corpus/knowledge/myth-symbol/myth-ritual-theories.md:32-35` supplies Frazer's divine king and Hooke's ritual-kingship pattern *as a collapsed theory of myth's origin*, and `:85` lists divine kingship only as a worldbuilding use of that theory; `hero-journey-variants.md:56-57` carries Raglan's 22-point **king pattern** as a hero-biography score and `:110` assigns it to "sacred-kingship agrarian polity" in one clause; `pantheon-archetypes.md:61` calls the dragon-slaying formula "the charter of kingship" in a single line and `:49` notes that war gods legitimize kingship by victory; `cosmology-cosmography.md:38` names "celestial-pivot kingship" in early China and `:108` the akītu king's cheek-strike; `plant-symbolism.md:77` records Frazer's sacred king only to warn that the framework "contaminates a world bible"; `ritual-liminality.md:40` holds the status-reversal rite where the king is ritually humiliated; `creation-myths-taxonomy.md:90,110,133` and `flood-traditions.md:26,34,76` treat kingship as an implied value or a post-flood legal output. Nine of nineteen myth-symbol files mention kingship in passing and **none states the institution**: the legitimation channels, the conditional-vitality doctrine, the failing-king devices, the co-sovereign slots, the installation, the taboo set, and the royal register. Absence sweep 2026-10-19 from the lane root over `corpus/knowledge/`: `Hocart`, `stranger-king`, `Sed festival`, `Kantorowicz`, `king's two bodies`, `royal touch`, `rex sacrorum`, `Feeley-Harnik`, `mascapaycha`, `k'uhul ajaw`, `Ngwenyama`, `Ndlovukati`, `šar pūhi` → **0 files each**; `divine kingship` → 3 files, only `myth-ritual-theories.md:35,85` inside this partition; `regicide` → 2 files, both in `culture-material/era-periodization-models.md:69` and `myth-ritual-theories.md:35`; `substitute king`, `iyoba`, `ixiptla`, `Golden Stool`, `devarāja` → 1–2 files each, all culture-specific (`civilizations/benin.md:42`, `civilizations/persia-achaemenid.md:1`). The culture-specific treatments stay where they are: this entry adds the **method** the civilizations files and the neighbours presuppose, and couples to them rather than restating them.
- sources:
  - James George Frazer (1890; 3rd ed. 1906–15), *The Golden Bough* — the rex Nemorensis of Nemi and the "sacred king slain when his strength fails" thesis; the dying-god complex. Framework status: **discredited** as history and as anthropology (evolutionist stadialism, no method for distinguishing custom from conjecture); retained here only as (a) the source of the vocabulary the field inherited and (b) a design inventory whose every item must be re-grounded in a dated attestation. This lane already constrains its use: `corpus/knowledge/verification/calibration-registry.md:91` requires the 1922 abridgment or a named full-edition volume, and `corpus/knowledge/myth-symbol/plant-symbolism.md:77` names the framework as the file's chief contamination risk. Read at lane HEAD `4a7aede`, 2026-10-19.
  - A. M. Hocart (1927), *Kingship*, Oxford University Press. The ritual-origin thesis: kingship began as ritual office (the king as the centre of a sacrificial and cosmic order) and only later acquired government; the "king is the centre of the ritual system" line. Framework status: **historically important, contested**; the origin claim is not testable against the record and the diffusionist scaffolding is dated. Used here for its inventory of **ritual functions attached to rule** (feeding the god, sitting on the throne, the sacred meal, the progress), each treated as a candidate device, never as an attested sequence. `Hocart` appears in **0** files of `corpus/knowledge/` (sweep above).
  - C. G. Seligman (1934), *Egypt and Negro Africa: A Study of Divine Kingship*, Routledge. The comparative program that made "divine kingship" a category (Egypt and the Nilotic Sudan in one frame). Framework status: **contested**; the equation of Egyptian pharaonic ideology with Shilluk kingship is a diffusionist reading. Cited as the category's source, not as evidence.
  - Henri Frankfort (1948), *Kingship and the Gods: A Study of Ancient Near Eastern Religion as the Integration of Society and Nature*, University of Chicago Press. The strongest surviving statement of the Mesopotamian/Egyptian contrast: in Egypt the king is the integrating point of cosmos and nature (the doctrine of maʿat; the king as the guarantor of the inundation and the seasons), in Mesopotamia he is the god's tenant — a servant who can be audited. Framework status: **mainstream** in Ancient Near Eastern studies, still the standard comparative starting point; calibration: the Egypt/Mesopotamia contrast is a scholarly construction of the sources' own rhetoric, so it describes ideology, not administration.
  - E. E. Evans-Pritchard (1948), "The Divine Kingship of the Shilluk of the Nilotic Sudan", Frazer Lecture, Cambridge University Press; reprinted in *Essays in Social Anthropology* (1962), Faber & Faber. The Reth of the Shilluk: kingship tied to the founding figure Nyikang, the king's body as the kingdom's wellbeing, and — the load-bearing caution — the king is removed not by a calendar of regicide but by **failure of health or vigour**, with the sources thin and the practice not directly observed. Framework status: **mainstream ethnography**; calibration: this is the single most important corrective to Frazer's universal regicide, and later work questions how much of even the Shilluk case was ritual killing versus succession crisis. Cite Evans-Pritchard against the thesis he is usually cited for.
  - Gillian Feeley-Harnik (1985), "Issues in Divine Kingship", *Annual Review of Anthropology* 14: 273–313 (page range **to-verify**). The survey that maps the field's real issues (the king's relation to the land, to ancestors, to the fertility of people and herds; the difference between sacredness and divinity; why "divine kingship" is a problem rather than a type). Framework status: **mainstream** review. `Feeley-Harnik` appears in **0** files of `corpus/knowledge/` (sweep above).
  - David Cannadine and Simon Price, eds. (1987), *Rituals of Royalty: Power and Ceremonial in Traditional Societies*, Cambridge University Press. The corrective to ceremony-as-mask: royal ritual is where power is *made*, contested, and negotiated, not a decorative layer over a real politics. Framework status: **mainstream** in the anthropology/history of ceremonial; used here as the entry's governing assumption about installation rites.
  - Ernst H. Kantorowicz (1957), *The King's Two Bodies: A Study in Mediaeval Political Theology*, Princeton University Press. The body natural / body politic distinction, built from the medieval jurists and the funerary *effigy*: the king dies, the kingship does not. Framework status: **mainstream** in medieval political thought and widely borrowed. `Kantorowicz` and `king's two bodies` appear in **0** files of `corpus/knowledge/` (sweep above). Used here as the general design device for dual sovereignty, not as a claim about any non-European polity.
  - Marc Bloch (1924), *Les rois thaumaturges*; English translation (1973), *The Royal Touch: Sacred Monarchy and Scrofula in England and France*, Routledge & Kegan Paul (translation details **to-verify**). The royal touch for scrofula ("the king's evil") as an institution with a ritual, a queue, a diagnostic, and a political cost when the cure rate fails. Framework status: **mainstream** history. `royal touch` appears in **0** files of `corpus/knowledge/` (sweep above).
  - Marshall Sahlins (1985), *Islands of History*, University of Chicago Press (the stranger-king: the ruler who comes from outside the society he rules, so that he can be both of it and above it), and Sahlins (1981), *Historical Metaphors and Mythical Realities*, University of Michigan Press (the Makahiki/Lono reading of Captain Cook's arrival and death). Framework status: **contested and productive**; the stranger-king structure is widely used in Polynesian and Southeast Asian studies, the Cook-as-Lono reading is the field's standing cautionary case (below).
  - Gananath Obeyesekere (1992), *The Apotheosis of Captain Cook: European Mythmaking in the Pacific*, Princeton University Press. The rebuttal: the "natives took Cook for their god" story is a European myth-making pattern projected onto Hawaiians, and the evidence for the identification is weak. Cited **paired** with Sahlins, always: a worldbuilder who wants the returning-god device should see that its most famous real-world case is exactly the one the field cannot settle.
  - David Graeber and Marshall Sahlins (2017), *On Kings*, HAU Books. Kingship treated as a cosmic office rather than a stage of political evolution, and the recurring pair of archetypes: the sacred king who stands *outside* the community (the stranger, the divine, the dead) and the popular king who stands *for* it. Framework status: **contested, current**; used here for the two-archetype design axis, not as a law of history.
  - T. O. Beidelman (1966), "Swazi Royal Ritual", *Africa* 36(4): 373–405 (details **to-verify**); Hilda Kuper (1947), *An African Aristocracy: Rank among the Swazi*, Oxford University Press for the International African Institute. The Incwala and the dual monarchy: the Ngwenyama (king) and Ndlovukati (queen mother, "she-elephant") as two offices of one kingship, with the ritual work of renewal and the king's body as the object of national work. Framework status: **mainstream** ethnography of the Swazi; `Ngwenyama` and `Ndlovukati` appear in **0** files of `corpus/knowledge/` (sweep above).
  - R. S. Rattray (1923), *Ashanti*, Oxford University Press (the Golden Stool as the nation's *sunsum* or soul, and the okyeame — the "linguist" through whom the Asantehene speaks, so that the king's own voice is mediated; details **to-verify**). Framework status: **foundational and dated**; Rattray's early colonial ethnography is used here for the *institutional shape* of mediated royal speech, which later work corroborates, and not for its cultural-evolutionary frame. `okyeame` appears in 1 file of `corpus/knowledge/`.
  - Godfrey Lienhardt (1961), *Divinity and Experience: The Religion of the Dinka*, Oxford University Press. The spear-masters: priestly figures with divine mediation and no government — the standing counter-case proving that "divine" and "king" are separate variables. Framework status: **mainstream**.
  - Thorkild Jacobsen (1976), *The Treasures of Darkness: A History of Mesopotamian Religion*, Yale University Press (the king as *sipa*, shepherd; the sacred-marriage material in the Sumerian love songs, read as ritual). Framework status: **mainstream** for the shepherd ideology; **contested** for the reconstruction of the hieros gamos as an annual performed marriage — the reading rests on poetic texts whose cult setting is inferred. Jane McIntosh? — not cited; the akītu side is carried by the next item.
  - Julye Bidmead (2002), *The Akītu Festival: Religious Continuity and Royal Legitimation in Mesopotamia*, Gorgias Press; and the entry already in this partition, `corpus/knowledge/myth-symbol/cosmology-cosmography.md:108`, which records that the king's cheek is struck and his sceptre restored at the New Year and that the reenactment link is **late-attested (Seleucid-era ritual text) and contested** (Sommer 2000; Debourse 2022). Use the humiliation-and-reinvestiture device; label its reconstruction as contested, per the partition's existing flag.
  - Simo Parpola (1993), *Letters from Assyrian and Babylonian Scholars*, State Archives of Assyria 10, Helsinki University Press. The substitute-king (*šar pūhi*, spelling **to-verify**) procedure in the royal correspondence: when the omens condemned the king, a substitute was enthroned, the real king took a subordinate name, and the substitute (with a queen) was disposed of after the danger passed. Framework status: **mainstream** Assyriology; used as the best-documented "swap the body" device.
  - Trevor Bryce (2002), *Life and Society in the Hittite World*, Oxford University Press (Hittite royal purification and the substitute-king oracles; details **to-verify**). Framework status: **mainstream** Hittitology.
  - Linda Schele and Mary Ellen Miller (1986), *The Blood of Kings: Dynasty and Ritual in Maya Art*, Kimbell Art Museum / George Braziller. Classic Maya rulership: the *k'uhul ajaw* ("holy lord", spelling **to-verify**) whose ritual obligation is bloodletting, with the king's blood as the channel between the polity and its gods. Framework status: **mainstream** in Maya epigraphy and art history, with the caution that "divine" here is a translation convention for a title, not a theological identity — the calibration is argued in Houston & Stuart below.
  - Stephen Houston and David Stuart (1996), "Of Gods, Glyphs and Kings: Divinity and Rulership among the Classic Maya", *Antiquity* 70: 289–312 (details **to-verify**). The direct argument that Maya rulers were not gods but **persons holding a god-like office**, with divinity distributed through titles, accession rites, and the impersonation of deities. Framework status: **mainstream**, the standard calibration for the Maya case. `k'uhul ajaw` appears in **0** files of `corpus/knowledge/` (sweep above).
  - Juan de Betanzos (1551; trans. Roland Hamilton and Dana Buchanan, 1996), *Narrative of the Incas*, University of Texas Press; Felipe Guaman Poma de Ayala (c. 1615), *El primer nueva corónica y buen gobierno* (specific claims **to-verify**). The Sapa Inca as *Intip churin*, "son of the Sun"; the royal mummies kept, fed, and consulted by their *panaca* corporations; the royal fringe (*mascapaycha*, spelling **to-verify**) as the title-deed object. Framework status: **mainstream** for the mummy cult and the panaca (colonial-era sources plus archaeology); calibration: the colonial chronicles are interested texts and the mummy-cult details rest largely on them.
  - Jacob Egharevba (1934; later editions), *A Short History of Benin*; R. E. Bradbury (1957), *The Benin Kingdom and the Edo-Speaking Peoples of South-Western Nigeria*, International African Institute (edition details **to-verify**). The Ọba of Benin: coral-bead regalia restricted to the royal house, the Iyoba (queen mother) title created by the reigning Ọba, and the palace as the ritual centre of the polity. The lane already holds the culture-specific treatment — `corpus/knowledge/civilizations/benin.md:42` ("Registers and the vocabulary of divine kingship") — and this entry couples to it rather than restating it. `iyoba` appears in 1 file of `corpus/knowledge/`.
  - Hermann Kulke (1978), *The Devarāja Cult*, Cornell University Southeast Asia Program (Data Paper 108, **to-verify**); George Coedès (1968), *The Indianized States of Southeast Asia*, University of Hawaii Press (the 802 CE consecration of Jayavarman II on Mount Kulen and the devarāja as the royal *liṅga*; the Sdok Kak Thom inscription as the main source). Framework status: **mainstream** for the Khmer state cult; calibration: the devarāja is a scholarly category built from one inscription family, and the cult's daily practice is not documented. `devarāja` appears in 2 files of `corpus/knowledge/` (sweep above).
  - Melvyn Goldstein (1997), *The Snow Lion and the Dragon: China, Tibet, and the Dalai Lama*, University of California Press (the *chösi* — *chos srid*, "religion and politics" — priest-patron framing; details **to-verify**). Framework status: **mainstream** in Tibetan studies for the priest-patron relation; the Dalai Lama's status as an emanation of Avalokiteśvara is a doctrinal claim of the tradition, cited as an emic self-description, never as a fact about a person.
  - Lanny Bell (1985), "Luxor Temple and the Cult of the Royal Ka", *Journal of Near Eastern Studies* 44: 251–294 (details **to-verify**). The Egyptian royal *ka*: the divine royal essence that each pharaoh incarnated and that passed between them, tying the living king to his predecessors and to Horus. Framework status: **mainstream** Egyptology.
  - Endymion Wilkinson (2018), *Chinese History: A New Manual*, 5th ed., Harvard University Press — for the Chinese naming taboo (*bìhuì*, spelling **to-verify**) and the imperial first person 朕 *zhèn*, restricted to the emperor after the Qin; already cited in this corpus at `corpus/knowledge/culture-material/era-periodization-models.md:8`. Framework status: **mainstream** reference work.
  - Joseph Errington (1988), *Structure and Style in Javanese: A Semiotic View of Linguistic Etiquette*, University of Pennsylvania Press; and the lane's own `corpus/knowledge/linguistics/politeness-taboo-euphemism.md:62`, which tabulates Javanese *ngoko / madya / krama / krama inggil* word-by-word re-grading. Framework status: **mainstream**. The Javanese case is the entry's demonstration that the royal register is **grammar**, not decoration.
  - Karin Barber (1991), *I Could Speak Until Tomorrow: Oriki, Women and the Past in a Yoruba Town*, Edinburgh University Press for the International African Institute. *Oríkì*: the Yoruba praise-recitation genre in which a lineage's or a ruler's history and titles are performed aloud — the charter recited, with the reciter as an office. Framework status: **mainstream**; `oríkì` appears in 2 files of `corpus/knowledge/` (sweep above).
  - Lilikalā Kame'eleihiwa (1992), *Native Land and Foreign Desires: Pehea Lā E Pono Ai?*, Bishop Museum Press (the *kapu* system, the *'aikapu* separating male and female eating, and the 1819 *'ai noa* abolition under Liholiho; details **to-verify**). Framework status: **mainstream** Hawaiian scholarship; the Hawaiian case is used for the doctrine that the ruler's person **radiates taboo** and that the system can be broken in a day.
  - Frank Felsenstein? — not cited. `regicide` in the European sense (the English 1649 and French 1793 cases as *anti*-kingship acts) is outside this entry's scope and is flagged in §10 as a distinct subject.
- couples: myth-symbol — `corpus/knowledge/myth-symbol/myth-ritual-theories.md` (Frazer's divine king and Hooke's ritual-kingship pattern as *theory*; this entry takes the institution the theory mis-explained), `hero-journey-variants.md` (Raglan's 22-point king pattern as biography score; the exposure legend as a legitimation device this entry assigns to an institution), `pantheon-archetypes.md` (the war god who legitimizes by victory; the dragon-slayer enthroned), `cosmology-cosmography.md` (the akītu humiliation-and-reinvestiture, the celestial-pivot kingship, the center that the throne occupies), `creation-myths-taxonomy.md` (the creation type that generates the ruler's legitimacy story), `flood-traditions.md` (the deluge as the divider between mythic and historical rule), `ritual-liminality.md` (installation as a rite of passage; the status-reversal humiliation; sacrifice), `symbolism-synthesis-method.md` (regalia and royal color as one culture's closed correlative system), `comparative-frameworks.md` (Eliade's center and eternal return, Campbell's pattern — the engines this entry's devices plug into), `plant-symbolism.md` (the vegetation-deity complex the dying-king reading grew from), `divination-omen-systems.md` (the omen that condemns the king; the substitute-king trigger; the oracle that confirms an accession), `direction-symbolism.md` (orientation of throne and temple; the direction of the dead king's journey), `number-symbolism.md` (regnal counts, jubilee intervals, titulary numbers), `animal-symbolism.md` (royal beasts and the cakravartin's white elephant), `color-symbolism.md` (royal white, purple, and the Burmese white-elephant title); linguistics — `corpus/knowledge/linguistics/politeness-taboo-euphemism.md` (krama inggil, honorifics, taboo vocabulary and its sanctions; the royal register is an extreme case of the file's system), `naming-systems.md` (name taboo and name magic; the ruler's name as the most tabooed string in the language; regnal names), `sociolinguistics-registers.md` (speech levels and register ecology; the court as a speech community), `kinship-terminology.md` (dynastic kin terms, the queen-mother slot, teknonymy in royal address), `orality-formulaic-language.md` (praise-recitation and royal hymns as formulaic art with an office attached), `semantics-pragmatics.md` (the royal first person, deixis of majesty, the spokesman as a displaced speaker), `register-strata-attestation.md` (the binding-speech register; the coronation oath as a record-making act), `historical-linguistics.md` (loanword strata in royal vocabulary as dating evidence); culture-material — `corpus/knowledge/culture-material/era-periodization-models.md` (Mandate of Heaven and translatio imperii as era-legitimation devices), `costume-semiotics.md` and `sumptuary-law-rank-display.md` (regalia and dress law as the ruler's legible body), `ritual-garments.md` (investiture dress), `calendar-festival-systems.md` (jubilee and renewal intervals), `architecture-settlement-lexicon.md` (palace, throne room, the capital as ritual center), `trade-economy-lexicon.md` (treasury, tribute, and the regalia's inalienability); civilizations — `corpus/knowledge/civilizations/benin.md:42` and `civilizations/persia-achaemenid.md:1` (the culture-specific divine-kingship treatments this entry supplies method for); verification — `corpus/knowledge/verification/myth-consistency-gate.md` (the gate a royal charter must pass), `calibration-registry.md:91` (the Golden Bough use rules); synthesis — `corpus/knowledge/synthesis/worldbible-integration-contract.md` (the handoff the charter travels in), `consistency-verification-checklist.md`; handoff target: lore-shokunin world bible (comparative data and method only; canon decisions are theirs per lane rules).
- source: the external frameworks are the items in the sources block (Frazer; Hocart; Seligman; Frankfort; Evans-Pritchard; Feeley-Harnik; Cannadine & Price; Kantorowicz; Bloch; Sahlins; Obeyesekere; Graeber & Sahlins; Beidelman; Kuper; Rattray; Lienhardt; Jacobsen; Bidmead; Parpola; Bryce; Schele & Miller; Houston & Stuart; Betanzos; Guaman Poma; Egharevba; Bradbury; Kulke; Coedès; Goldstein; Bell; Wilkinson; Errington; Barber; Kame'eleihiwa). The lane-side authorities are the cited files of this corpus, read at lane HEAD `4a7aede` on 2026-10-19, and the absence-sweep commands recorded in the `- gap filled:` line. No source was retrieved online this round: every bibliographic detail the author could not check against a held copy or a lane citation carries an inline `(to-verify)`, listed together in §12. The method is this lane's house style; the frameworks are cited, never blended into a claim about any real polity.
- verified-at: 2026-10-19 — written this round at lane HEAD `4a7aede` (`reports/round-35/claims.json` baseline `4a7aede`, `baseline_expanded` `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4`). Measured at write time with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`: partition census `for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done` → `21 / 19 / 18 / 29 / 20 / 94`, total `find corpus/knowledge -name '*.md' | wc -l` → `201`; myth-symbol files mentioning `kingship` → 9, `divine kingship` → 1; the absence sweep in the `- gap filled:` line. The entry's header apparatus was checked against the house gate at write time (`tools/gates/provenance-audit.py` on the draft: no findings, 0 marks — see the author fragment `reports/round-35/cov/C08-entry-8.md` §4). No per-source retrieval was performed in this pass; the sources' status labels are the author's, and the external citations were not re-verified against copies this round — the `(to-verify)` items in §12 are the honest residue.
- recheck: before quoting any device from §4 (the failing-king family) as a real practice — the regicide thesis is the field's most-repeated and least-supported claim, and the Shilluk case specifically must be cited with Evans-Pritchard's own caution; before using the akītu humiliation as a model, re-read the contested-status flag at `corpus/knowledge/myth-symbol/cosmology-cosmography.md:108`; before importing the Makahiki/Lono device, read Sahlins (1981) and Obeyesekere (1992) as a pair and never one without the other; before writing a Maya or Inca ruler as a god, apply Houston & Stuart (1996) and the Betanzos/Guaman Poma interest warning; before any claim that a real polity "had a divine king", check §11's category critique (Feeley-Harnik 1985; Lienhardt's counter-case); and whenever `corpus/knowledge/myth-symbol/` gains an entry that takes kingship as its subject (a sibling may land one in the same round), reconcile by extension — the house rule is that the later entry names the earlier one and adds the missing object, never restates it.

## 1. The charter, stated as four questions

**A mythic charter of rule is a story that answers four questions a polity cannot leave open: who may rule, why them, what makes them able to rule, and what happens when they fail.** A worldbuilder designing a sacred kingship is designing four answers, not one adjective. The failure of most fictional sacred kingships is that they answer only question two ("because the god chose him") and leave questions three and four to be improvised at the scene where they matter — the drought, the defeat, the sick king.

The four questions, with the design object each one produces:

| question | what it decides | the object you build |
|---|---|---|
| who may rule | the pool of candidates — a lineage, an office, a body, an outsider | the eligibility rule and its genealogy |
| why them | the source of title | the legitimation channel (§2) |
| what makes them able | the coupling between ruler and world | the conditional-vitality doctrine and its **observable channel** (§3) |
| what happens when they fail | the exit | the failing-king device (§4) |

Two craft rules govern all four. First: **the charter must be legible to the people who pay for it.** A legitimacy story that only the priests can state is a priests' instrument, not a charter — and the entry should decide, per culture, whether that is the intent. Second: **the charter must name its own failure condition.** A kingship with no stated way for a king to be wrong is not a sacred kingship; it is a claim of impunity, which no real polity can sustain and no fictional one can dramatize.

## 2. The legitimation channels — eight ways a myth makes a ruler

Each channel is a different machine, with a different political cost and a different vulnerability. Real polities usually run two or three at once (a descent claim *and* an installation rite *and* a victory); a polity that runs only one is brittle in a specific way, noted in the last column.

| # | channel | mechanism | attested exemplars | cost / vulnerability |
|---|---|---|---|---|
| 1 | **divine descent** | the ruler's line descends from a god or the founding figure | Egyptian pharaoh as Horus on earth and "son of Ra" (fivefold titulary; Bell 1985 on the royal *ka*); the Sapa Inca as *Intip churin*, son of the Sun (Betanzos); the Solomonic claim of the Ethiopian dynasty, sealed by the *Kebra Nagast* and the Ark at Aksum (**to-verify**) | every collateral branch of the line is a rival; genealogy becomes the main political document and the main forgery |
| 2 | **incarnation / vessel** | the ruler *is* the god, or the god's body is installed in him | the Khmer *devarāja*: the royal liṅga as the kingdom's divine essence, consecrated 802 CE (Kulke 1978; Coedès 1968); the Dalai Lama as an emanation of Avalokiteśvara (emic self-description; Goldstein 1997) | if the god can be present in a body, the body's defects are the god's defects; a rival body is a rival god |
| 3 | **delegation** | the ruler is the god's tenant, servant, or shepherd — an office, not a person | Mesopotamian kingship: the king as *sipa*, shepherd, with his rule audited by omens and the gods' assembly (Jacobsen 1976; Frankfort 1948); Chinese Mandate of Heaven (tianming), where the mandate is *withdrawn* from the corrupt (`corpus/knowledge/culture-material/era-periodization-models.md:67,69`) | the office can be vacated by its grantor: this channel makes deposition a theological act, and it needs a body of interpreters (priests, diviners, historians) |
| 4 | **election / acclamation** | the gods, the nobles, or the army *choose*, and the choice is ratified aloud | the imperial acclamation and the Roman *imperium* conferred by Senate and army (**to-verify** for details); the Holy Roman Emperor elected by the prince-electors; the Germanic king raised on the shield at the *thing* (**to-verify**) | election implies the electors can elect someone else; acclamation implies a public that can refuse to shout |
| 5 | **conquest and test** | the ruler proves title by winning — war, ordeal, or a prescribed feat | the Mexica coronation war (the new *tlatoani* must take captives to validate accession — **to-verify**); the dragon-slayer enthroned: Marduk receives kingship from the assembly after Tiamat (`pantheon-archetypes.md:61`); the Sumerian King List's logic that kingship is *carried off* by the victor (`flood-traditions.md:34`) | this channel makes every reign a probation; it also legitimizes usurpers perfectly, which is its real function |
| 6 | **installation rite** | title is conferred by a performed sequence: anointing, crowning, enthroning, feeding, naming | Israelite anointing (1 Sam 16 — **to-verify** for the European unction line); the Christian coronation with unction and oath; the Japanese accession rites including the *daijōsai* (**to-verify**) | the rite is repeatable, which is exactly what an interregnum, a rival, or a reformer needs; whoever controls the rite controls the title |
| 7 | **alliance / marriage into the divine line** | the ruler is joined to the divine by marriage, fosterage, or the transfer of a sacred object | the Sumerian sacred-marriage material, read as the king's union with the goddess's representative (Jacobsen 1976; **contested** — see §11); the Ashanti Golden Stool as the nation's soul, which no one may sit on (Rattray 1923; **to-verify**); the marriage of a dynasty into a shrine lineage (**to-verify**) | the allied party becomes a co-claimant; the sacred object can be captured, which is a casus belli in both directions (the War of the Golden Stool, 1900 — **to-verify**) |
| 8 | **the regalia as found title-deed** | title inheres in *objects*: the crown, the fringe, the stool, the regalia set | the Inca royal fringe *mascapaycha* (**to-verify**); the Japanese three regalia; the pharaonic crook and flail; the Yoruba beaded crown with its veil | objects can be hidden, stolen, duplicated, or replaced — the duplicate is the cheapest usurpation device in the whole system |

Craft rule: **pick the channel from the polity's economy, not from taste.** A raiding confederacy that legitimates by descent will be ruled by genealogists; a trade city that legitimates by installation will be ruled by the masters of ceremony. The channel determines who the second most powerful institution is.

## 3. The king's body is the land's body — and it needs a channel

The conditional-vitality doctrine — the ruler's state *is* the realm's state — is the load-bearing belief of most sacred kingships, and it is useless in fiction unless it is given an **observable channel**: a thing the story can show going wrong.

| doctrine | channel (observable) | attested case | what the story can do with it |
|---|---|---|---|
| the king's vigour is the people's | the king's health, wholeness, and appetite | Shilluk Reth: kingship tied to the founding figure Nyikang; the king removed on failure of health or vigour (Evans-Pritchard 1948, with his own caution) | a sick king, a hidden illness, a court that must not let the king be seen failing |
| the king's virtue is the weather and the harvest | drought, flood, famine | Egyptian: the king guarantees *maʿat* and the inundation (Frankfort 1948); Chinese: the emperor's misrule is read in portents and drought (`era-periodization-models.md:67,69`) | a famine that becomes a constitutional crisis; the court's competing readings of the omen |
| the king's body is the boundary between the polity and the gods | the success of ritual; the king's blood | Maya *k'uhul ajaw* whose obligation is bloodletting (Schele & Miller 1986), with the calibration that this is an office, not a divine identity (Houston & Stuart 1996) | ritual failure as political failure; the king who cannot bleed |
| the king's touch heals | the cure rate of a named disease | the royal touch for scrofula in England and France (Bloch 1924) | a public healing queue that is also a public audit of the king — the best "belief with a feedback loop" device in the set |
| the king's person is taboo | what happens to things and people that touch him | Hawaiian *kapu*: the ruler's person radiates taboo; the system's abolition in 1819 under Liholiho (Kame'eleihiwa 1992; **to-verify**) | a system that can be broken in a single act — an entire legitimacy order switched off in a day |
| the king's line holds the ancestors | the ancestors' continued service | Inca royal mummies kept, served, and consulted by their *panaca* (Betanzos 1996; **to-verify** for specifics) | the dead as a faction: the previous kings are players, not memories |

Two rules follow. **First: a doctrine with no channel is decoration.** If the entry says the king's vitality is the land's but never shows the land responding, the belief has no cost and no plot. **Second: choose the channel's failure mode deliberately.** Each channel fails differently — health is private and can be hidden; weather is public and cannot; the touch is auditable in numbers; the taboo breaks catastrophically. The failure mode is the polity's constitutional crisis generator, and it should be named in the design brief.

## 4. The failing-king device family

A sacred kingship that cannot lose a king is not a system, it is a person. Six devices, each with the grade of its real-world support — **use the grade, not the romance**:

| device | mechanism | attested case | reliability grade |
|---|---|---|---|
| **ritual regicide** | the king is killed when his strength fails, or on a schedule | the rex Nemorensis of Nemi (Frazer 1890, as literature); the Shilluk Reth (Evans-Pritchard 1948) | **weak-to-contested**: Frazer's universal law is discredited; Evans-Pritchard's own account says the removal is on failure of health or vigour, observed indirectly, and later work disputes how much was ritual killing versus ordinary succession struggle. Cite with the caution attached or not at all. |
| **jubilee / renewal** | the king is not killed but *re-made*: seclusion, purification, re-enthronement | Egyptian Sed festival (the jubilee after a long reign, rejuvenating the king's powers — Frankfort 1948; **to-verify** on the interval); the akītu New Year, where the king is humiliated and his sceptre restored — **late-attested and contested** per `corpus/knowledge/myth-symbol/cosmology-cosmography.md:108` | **solid as institution, contested in detail**: the Egyptian jubilee is epigraphically attested; the Babylonian humiliation sequence rests on a Seleucid-era ritual text and must be labelled as such (Sommer 2000; Debourse 2022, as the partition already records). |
| **the substitute king** | a body is swapped in: the real king takes another name, a substitute reigns, and the substitute absorbs the fate | Assyrian *šar pūhi* procedure in the royal correspondence (Parpola 1993); Hittite substitute-king oracles (Bryce 2002) | **strong**, and the best documented of the six: the trigger is an omen condemning the king, and the procedure has a bureaucracy, a duration, and a disposal. This is the device a worldbuilder should reach for when they want regicide's *effects* without its evidentiary problems. |
| **mock king / carnival inversion** | the reversal is temporary and licensed: a beggar, a child, or a fool is king for a day, then the order returns | the Saturnalian king of the feast; the Lord of Misrule; the King of the Bean (**to-verify**) | **solid as custom**, but note what it does: it *displays* the order by inverting it (Gluckman's argument, already carried at `corpus/knowledge/myth-symbol/trickster.md` §8). It is not a succession mechanism. |
| **abdication / retirement** | the king withdraws: to a monastery, a palace of seclusion, a shrine, or the status of ancestor | the Japanese cloistered rule (*insei*, **to-verify**); Roman imperial abdication (Diocletian, **to-verify**); the Byzantine practice of retirement to a monastery (**to-verify**) | **solid as institution**: this is the cheapest failing-king device and the most under-used in fiction — a sacred king who can *retire into the sacred* keeps the charter intact while removing the body. |
| **interregnum** | the throne is deliberately empty, and the emptiness is a rite with rules | the Roman *interregnum* and the *rex sacrorum* as the surviving ritual kingship under the Republic (**to-verify**); the accession formula "the king is dead, long live the king" as the European formula for continuity (**to-verify** on earliest attestation) | **solid**: the empty throne is the device that lets the myth survive a bad year, and it gives the story a countdown. |

Craft rule: **pick exactly one primary device and one emergency device.** A polity that can lose a king three ways has no rules; a polity that can lose one only by regicide is a tragedy with a scheduled ending. The pair that reads best in a world bible is *jubilee as the norm, substitute king as the emergency* — renewal plus a body to burn.

## 5. Dual and co-sovereign slots

Sovereignty in practice is rarely one body, and the split is where a worldbuilder gets the most institutional texture for the least exposition.

- **The two bodies (Kantorowicz 1957).** The king's natural body dies; the kingship does not. Design use: a polity with this doctrine can stage a funeral and a coronation in the same scene, and its jurists can argue about what a mad or captured king means. The effigy — the royal image carried at the funeral — is a concrete prop the doctrine produces.
- **The queen mother as co-sovereign.** Swazi dual monarchy: Ngwenyama (king) and Ndlovukati ("she-elephant") as two offices of one kingship (Kuper 1947; Beidelman 1966); Benin's Iyoba, a title created by the reigning Ọba for his mother (`corpus/knowledge/civilizations/benin.md:42`). Design use: the queen mother is the *continuity* half — she belongs to no marriage alliance, so she can be the regent who cannot inherit, which is exactly why the office exists.
- **The warrior and the priest.** Where the ruler is sacred, the *violent* function is often delegated: the Byzantine *symphonia* of emperor and patriarch (**to-verify**); the Tibetan *chösi* priest-patron pair (Goldstein 1997; **to-verify**); the Japanese pattern in which the emperor holds legitimacy and another house holds force (**to-verify**). Design use: two-office sovereignty lets a story have a legitimate king who is powerless and a powerful figure who is not legitimate — the engine of a great many historical plots, and a generator of the "who is really king?" question.
- **The stranger-king (Sahlins 1985).** The ruler comes from outside the society he rules — a foreign lineage, a captive, a younger son from elsewhere — so that he can be simultaneously *of* the people and *above* them. Design use: the stranger-king explains why so many dynasties found with a foreigner and why the second generation is always a crisis. Pair with Graeber & Sahlins (2017): the sacred king who stands outside the community versus the popular king who stands for it.
- **The double and the substitute.** The *šar pūhi* (§4) is a co-sovereign for the duration of a danger; the court "double" (a bodyguard who wears the royal dress — **to-verify**) is its low-cost version. Design use: a polity whose charter requires the king to be unseen needs doubles, and doubles create the classic recognition plot.

## 6. Installation: the rite that makes the body into an office

The installation sequence is the one place where all the channels become visible at once, and it is the highest-yield scene a world bible can specify. A house-style installation has six beats; drop or double any, but decide each explicitly:

1. **The gap** — the interregnum's rules: who holds power, what may not be done, how long the emptiness may last (§4).
2. **The finding** — how the candidate is identified: descent audit, omen, oracle, election, the predecessor's designation, capture. This beat is where the polity's second institution (priests, diviners, nobles, army) shows its hand.
3. **The separation** — seclusion before installation: the candidate is taken out of ordinary life (retreat, vigil, purification, fasting, confinement) — structurally the first phase of a rite of passage (`corpus/knowledge/myth-symbol/ritual-liminality.md`, van Gennep's grammar).
4. **The ordeal or the test** — the prescribed feat: a war, a journey, a night in a sacred place, a recitation, a wrestling match, a public answer. The Mexica coronation war (**to-verify**) and the dragon-slayer enthroned (`pantheon-archetypes.md:61`) are the same beat at different scales.
5. **The conferral** — the objects and the words: anointing, crowning, the fringe, the stool, the name, the title recited in full. **This is the beat that must be written word-for-word in the world bible**, because it is the moment the myth becomes a legal fact in front of witnesses.
6. **The showing** — the first public appearance in the new state: procession, audience, first judgment, first meal, first sacrifice. The showing is where a polity's *audience rules* (who may look, from where, in what dress) get stated, and it is the beat that most often produces a scene in play.

Two cross-cutting decisions: **who may perform the conferral** (a priest, a predecessor, the army, the people — the performer is the real sovereign-maker), and **what the king may not do afterwards** (§7).

## 7. Taboo and seclusion: the cost accounting of a sacred body

A sacred ruler accumulates prohibitions, and prohibitions are expensive: each one is a thing the polity must work around. The craft move is to design the taboo set **and its workarounds together**, because the workarounds are the institutions.

| taboo class | attested shape | workaround the polity invents |
|---|---|---|
| **contact** — the king must not touch the ground, common things, or blood | the Hawaiian *kapu* radiating from the ruler's person (Kame'eleihiwa 1992; **to-verify**); the king carried or screened (**to-verify**) | bearers, litters, screens, platforms; a servant class whose job is contact |
| **gaze** — the king may not be seen, or may not see certain things | the Yoruba beaded crown with its face-covering veil (**to-verify**); the veiled or screened ruler generally (**to-verify**) | veils, curtains, audience architecture, and a *showing* exception (§6, beat 6) — the rule is stated precisely by its exceptions |
| **speech** — the king's voice is not used for ordinary business | the Ashanti okyeame, the "linguist" who speaks for the Asantehene (Rattray 1923; **to-verify**); the king who speaks only in formulae | the spokesman office, the herald, the interpreter — and the political power that comes with being the only licensed mouth of the king (§8) |
| **name** — the king's name may not be said | the Chinese naming taboo *bìhuì* (Wilkinson 2018; **to-verify**); the general pattern that the ruler's name is the most tabooed string in the language (`corpus/knowledge/linguistics/naming-systems.md` on name taboo) | replacement characters, titles, epithets, periphrasis — and a whole class of scribal and poetic workarounds |
| **food and body** — the king eats alone, eats tested food, or eats prescribed food | the king who never eats in public (**to-verify**, Rattray 1923 for the Ashanti pattern) | tasters, kitchens as an office, ritual meals as state occasions |
| **motion** — the king may not leave the capital, or may not travel by ordinary means | the Shilluk Reth's constrained life (Evans-Pritchard 1948); the king who must remain at the ritual centre (**to-verify**) | regents who travel, progress as a rite rather than a journey, a substitute on the road |

**Cost accounting rule:** each taboo buys legitimacy and spends administrative capacity. A polity with six taboo classes needs six offices; a polity with one (the name) needs one. The design brief should state the budget: *how many workarounds does this state actually fund?* A poor polity with an elaborate taboo set is a contradiction the story can exploit — and a rich polity with none has no sacred king at all, only a rich man.

## 8. The royal register — the language half

This lane's own subject: the ruler's charter is *spoken*, and the speech around a sacred king is a designed system with at least seven parts. Each is a coupling to an existing file, not a new theory.

1. **Address levels.** The court grades its speech to the ruler. The Javanese system re-grades a sentence word by word — *ngoko* (plain) / *madya* / *krama* / *krama inggil* (high-honorific vocabulary) — with the king addressed in *krama inggil* (`corpus/knowledge/linguistics/politeness-taboo-euphemism.md:62`, after Geertz 1972 and Errington 1988). Design use: honorific grammar is a *measurable* legitimacy meter — the story can show a courtier's level slipping, which is a political act.
2. **The ruler's first person.** The king does not say "I" like other people. The Chinese 朕 *zhèn* was an ordinary first-person pronoun reserved to the emperor after the Qin (Wilkinson 2018; **to-verify**); the "royal we" of European chanceries (**to-verify**); the self-humbling royal style that inverts the honorific gradient (**to-verify**). Design use: the pronoun is a one-word tell, and a usurper's slip is a scene.
3. **The spokesman.** Where the king's voice is tabooed, an office speaks for him — the Ashanti okyeame (Rattray 1923; **to-verify**). The spokesman is a **displaced speaker**, which is a pragmatician's object: whose illocutionary force is it when the okyeame speaks? Design use: the spokesman is the second most powerful person in the room and the natural target for anyone who wants the king's ear.
4. **Name taboo and epithets.** The ruler's name is replaced in speech and writing (Chinese *bìhuì*; `naming-systems.md`). Design use: the taboo generates an epithet stock — titles, praise names, periphrases — which is the raw material for a **titulary**, the full string of names recited at installation (Egypt's fivefold titulary is the canonical case; Bell 1985, Frankfort 1948).
5. **Praise-recitation as performed pedigree.** The charter is not only believed, it is *recited*. Yoruba *oríkì* perform a lineage's or a ruler's history, titles, and character aloud, with the reciter as an office (Barber 1991; `oríkì` appears in 2 files of `corpus/knowledge/`). Sumerian royal hymns do the same work for the Mesopotamian king (Jacobsen 1976). Design use: the praise genre is where the charter is *publicly auditable* — a reciter who omits a title is making a political statement, and the genre's formulaic constraints make the omission visible (`orality-formulaic-language.md`).
6. **The oath and the binding formula.** Rule is sworn by, and on, the king: "by the head of the Oba" (**to-verify**); oaths on the king's life, the regalia, or the ancestors. This couples to the lane's attestation-register work (`register-strata-attestation.md`): the oath is where royal language becomes record-making speech, with consequences.
7. **The accession formula.** The one sentence the polity says at the seam — "the king is dead, long live the king" is the European version (**to-verify** on attestation) — plus the regnal name and the era name that reset the calendar (`era-periodization-models.md` on *gaiyuan* and era names). Design use: the formula is the shortest possible statement of the two-bodies doctrine (§5), and the era name is how a reign is dated in every subsequent document.

**Register rule:** the royal register's job is not decoration but **grading** — it tells every speaker in the room what their standing is, in real time, with the same precision as dress law. If a world bible specifies the king's regalia and not the king's grammar, the court scenes will all read at the same level, which is the tell of an under-built polity.

## 9. Pedigree distance, the stranger-king, and the re-legitimation toolkit

- **The pedigree-distance rule.** The further the founding god sits from the present king, the more room the interpreters have: a king descended directly from a god has a body to defend; a king descended from a god through forty generations has a **genealogy to be curated**, and the curators are the priests, the bards, and the archivists. Design decision: *distance = the second institution's power.* Raglan's king pattern is the biography-side of the same device (`hero-journey-variants.md:56-57`): the exposure legend manufactures a high-destiny ruler from a humble origin, and `:110` assigns it to exactly the sacred-kingship agrarian polity this entry describes. Use the pattern as a *legitimation device with an institution behind it*, never as a fact about a life.
- **The stranger-king (Sahlins 1985).** Founding by an outsider resolves the "of us / above us" tension; its cost is that the second generation must invent an inside claim — the classic dynastic crisis. Graeber & Sahlins (2017) supply the design axis: the sacred king who stands *outside* the community (stranger, god, or dead) versus the popular king who stands *for* it. A dynasty can move along this axis over its history, and the move is a plot.
- **The re-legitimation toolkit.** When a charter fails (a usurper, a lost war, a broken taboo), polities repair it with a small, recurring set of moves: **rewrite the genealogy** (annex a god, adopt a lineage); **find an object** (a relic, a regalia piece, a tomb — the found title-deed channel of §2.8); **obtain an oracle** (the divination file's whole apparatus, `divination-omen-systems.md`, exists to ratify or refuse); **re-stage the installation** (a second coronation, which is why §2.6's rite is repeatable); **change the name** (regnal and era names, §8.7); and **transfer the mandate** (the *translatio imperii* move, `era-periodization-models.md:75`). Design use: hand the usurper two of these moves and the story of a successful usurpation writes itself.
- **The reception check.** A sacred kingship has an *outside*: how do neighbours, rivals, and later empires describe the ruler? The colonizing description is itself a device (the "Oriental despot" label, the "god-king" exoticism) and a realistic one — the entry's own warning about the category (§11) is, in-world, a thing the characters can be wrong about.

## 10. Application protocol — building a fictional culture's sacred kingship

1. **Answer the four questions (§1) in one paragraph each**, in the world bible's own voice, before writing any ritual.
2. **Pick the legitimation channels (§2): one primary, one supporting.** Name the second institution the channel empowers, and give it a face.
3. **Choose the vitality channel (§3) and its failure mode.** Write the observable: what in the world goes wrong, who notices first, and what they are allowed to say about it.
4. **Choose one primary failing-king device and one emergency device (§4).** Grade them in your notes; do not let a Frazerian device in unlabelled.
5. **Design the co-sovereign slot (§5).** Decide whether the continuity half is the queen mother, a priest, a council, or a stranger lineage, and what it cannot do.
6. **Write the installation in six beats (§6)**, with beat 5 (the conferral) in full formulaic language.
7. **Build the taboo set with its workarounds and its budget (§7).** Each taboo names the office that pays for it.
8. **Build the royal register (§8):** the address level, the ruler's pronoun, the spokesman office, the name taboo and epithet stock, the praise genre and who performs it, the oath formula, the accession formula. Couple each to the language files, not to a mood.
9. **Set the pedigree distance (§9)** and let it set the curators' power.
10. **Run the reception check (§9)** and write the outside description in the neighbours' words.
11. **Failure modes to refuse:** a king who is divine by adjective and has no channel; a regicide imported from Frazer without the caution; a taboo set with no workarounds (an unfundable state); a court with regalia but no register; a usurpation with no re-legitimation move; a "divine king" in a polity whose economy cannot pay for the priests who would maintain him; and the biggest one — a charter that never names its own failure condition.

## 11. Calibration — what is mainstream, what is contested, what is this lane's

- **"Divine kingship" is a category with a history, not a type.** It was built by Frazer's comparative program, Hocart's ritual-origin thesis, and Seligman's Egypt–Africa frame; the twentieth-century ethnographic record then showed that the polities gathered under it differ in what is divine (the office, the body, the line, the regalia) and in who holds the divinity (the king, the queen mother, the ancestors, the stool). Feeley-Harnik (1985) treats the phrase as a *problem*, and Lienhardt's Dinka spear-masters (1961) are the standing counter-case: full divine mediation, no kingship at all. **Craft consequence:** the world bible should say which of the four is divine, and never write "the king is a god" as if it were one thing.
- **The regicide thesis is the field's most-repeated weak claim.** Frazer's law (the sacred king must die when his strength fails) is discredited; the Shilluk material that is usually cited for it comes with Evans-Pritchard's own caution about indirect evidence and succession politics (Evans-Pritchard 1948). Use the *substitute king* (§4) when you want the effect without the evidentiary problem.
- **The akītu humiliation-and-reinvestiture is late-attested and contested** — already flagged in this partition at `corpus/knowledge/myth-symbol/cosmology-cosmography.md:108` (Sommer 2000; Debourse 2022). The same caution applies to Hooke's ritual-kingship pattern (`myth-ritual-theories.md:33`) and to the reading of the Sumerian sacred-marriage songs as a performed annual rite (Jacobsen 1976; contested).
- **The Cook-as-Lono case is the standing warning.** Sahlins (1981) read Captain Cook's arrival and death through the Makahiki/Lono structure; Obeyesekere (1992) argued the identification is European myth-making. Whatever the verdict, the case demonstrates the failure mode this entry exists to prevent: a worldbuilder (or an anthropologist) reading a polity through a charter it may not hold. **Always cite the pair.**
- **Maya rulers were not gods** in the flat sense: Houston & Stuart (1996) argue for an office with god-like titles, accession rites, and deity impersonation. The Maya case is the best real-world demonstration of §1's rule that the charter has four answers, not one.
- **Colonial and interested sources are the base for several cases** (Inca mummy cult: Betanzos and Guaman Poma; Benin: Egharevba; Ashanti: Rattray; Hawai'i: the kapu system as described after its abolition). Their interest does not make the institutions unreal, but it does mean the *details* (this title, this taboo, this interval) carry `(to-verify)` marks in this entry — the marks are the honest residue of writing without a retrieval pass this round.
- **Oriental-despotism framing is refused.** "The king owned everything and was worshipped" is a European historiographical construction that flattens exactly the institutional variation this entry is built to preserve; where a source's own rhetoric claims total divinity, cite it as the source's rhetoric.
- **This lane's own contribution:** the four-question charter, the channel-and-failure-mode pairing, the taboo cost accounting, and the royal register as grammar (not mood). These are design devices, stated as such, and they are non-canon: nothing here says what is true in any world.

## 12. The `(to-verify)` census

Every bibliographic detail and every case-specific claim this entry could not check against a held copy or a lane citation, listed together so an auditor can find them without re-reading the entry. None of these is a source invented or a fact asserted; each is a claim the reader should treat as unconfirmed until a retrieval pass runs.

- **Details marked `(to-verify)` inline:** the Ethiopian Solomonic claim and the Ark at Aksum; Roman acclamation and *imperium* mechanics; the Germanic shield-raising at the *thing*; the Mexica coronation war; the European unction line and 1 Sam 16 linkage; the Japanese accession rites including the *daijōsai*; the Ashanti Golden Stool and the War of the Golden Stool (1900); the Inca *mascapaycha* spelling and details; the Egyptian Sed-festival interval; the Japanese *insei*; Diocletian's abdication; Byzantine imperial retirement; the Roman *interregnum* and *rex sacrorum*; the earliest attestation of "the king is dead, long live the king"; Byzantine *symphonia*; the Tibetan *chösi* framing; the Japanese emperor-holds-legitimacy pattern; the royal "double" bodyguard; the Hawaiian *kapu* details and the 1819 *'ai noa*; the Yoruba crown veil; the "by the head of the Oba" oath; the Chinese *bìhuì* and 朕 *zhèn* reservation; the Javanese royal address details beyond `politeness-taboo-euphemism.md:62`; the European royal "we"; the king who never eats in public; the king who must not leave the capital; the veiled/screened ruler pattern; the Saturnalian mock-king cases.
- **Bibliographic details marked `(to-verify)`:** Feeley-Harnik (1985) page range; Bloch (1924/1973) translation details; Beidelman (1966) volume and pages; Rattray (1923) specifics; Bryce (2002) specifics; Houston & Stuart (1996) pages; Parpola (1993) *šar pūhi* spelling; Kulke (1978) Data Paper number; Goldstein (1997) specifics; Bell (1985) pages; Egharevba and Bradbury edition details; Kame'eleihiwa (1992) specifics; Betanzos/Guaman Poma specifics; Coedès (1968) specifics; Wilkinson (2018) *bìhuì* treatment.
- **Audit consequence:** an auditor applying the house entry-audit runbook should count this section as the entry's own declaration of its unverified surface, and grade it accordingly — a clean entry here means *no unmarked* unverified claims, not that the marked ones have been confirmed.

## 13. Coupling notes

- → lore-shokunin: reference only. Which ruler means what in canon, and whether any world has a sacred kingship at all, is theirs; this file supplies the channels, the devices, the cost accounting, the register checklist, and the calibration.
- → myth files: the charter is written in the culture's own creation type (`creation-myths-taxonomy.md`), its cosmography (`cosmology-cosmography.md` — where the throne sits on the center), its divination apparatus (`divination-omen-systems.md` — the omen that condemns or confirms), and its flood-and-founding history (`flood-traditions.md` — the deluge as the divider between mythic and historical rule).
- → language files: the royal register is *applied* politeness, naming, and register work — `politeness-taboo-euphemism.md`, `naming-systems.md`, `sociolinguistics-registers.md`, `kinship-terminology.md`, `orality-formulaic-language.md`, `semantics-pragmatics.md`, `register-strata-attestation.md`, `historical-linguistics.md`. The entry's rule: specify the grammar, not the mood.
- → culture-material: regalia and dress law (`costume-semiotics.md`, `sumptuary-law-rank-display.md`, `ritual-garments.md`), the palace and the ritual center (`architecture-settlement-lexicon.md`), the calendar of renewal and jubilee (`calendar-festival-systems.md`), the treasury and tribute (`trade-economy-lexicon.md`), the era-name machinery of a reign (`era-periodization-models.md`).
- → verification: a royal charter is a myth record and passes the same gates — `myth-consistency-gate.md`, `calibration-registry.md:91` (the Golden Bough rules), `provenance-audit-ledger-format.md` (the `to-verify` disposition this entry's §12 relies on).
- → synthesis: the charter travels in the world-bible handoff (`worldbible-integration-contract.md`) and is checked by the consistency checklist (`consistency-verification-checklist.md`).

````

## 4. Apparatus self-check (measured, not asserted)

| check | command | exit | observed |
|---|---|---:|---|
| house provenance gate on the draft | `python3 -B tools/gates/provenance-audit.py .scratch/c08-entry-8.md` | 0 | `INFO to-verify-count: … 61 mark(s) on 47 line(s)`; `INFO scan: files=1 marks=61 mark-lines=47 findings=0 blocked=0` — **no findings**; the marks are inventory, never findings, per the gate's own docstring and `corpus/knowledge/verification/provenance-audit-ledger-format.md` |
| header fields present | `grep -c '^- \(topic\|gap filled\|sources\|couples\|source\|verified-at\|recheck\):' .scratch/c08-entry-8.md` | 0 | `7` (topic / gap filled / sources / couples / source / verified-at / recheck — the full header profile, superset of the gate's topic+sources+couples requirement) |
| calibration vocabulary | included in the gate run above | 0 | no `missing-calibration` finding (the gate fires only when `calibrat*` is absent; the entry carries §11 "Calibration") |
| internal reference resolution | regex sweep of every `*.md` and `*.md:line` reference in the draft against the tree (99 resolved) | 0 | **99 resolved, 0 out of range, 1 unresolved — and that one is the self-reference to this fragment's own path, which exists once this file is written** |
| cited-line spot checks | `sed -n '62p' …/politeness-taboo-euphemism.md`; `sed -n '91p' …/calibration-registry.md`; `sed -n '77p' …/plant-symbolism.md` | 0 | the Javanese `ngoko/madya/krama/krama inggil` row; the Golden Bough use rule; the Frazer "contaminates a world bible" warning — all three lines carry what §3 cites them for |

The gate was run **on the draft copy under `.scratch/`**, never on a corpus path: no
corpus byte is written or modified by this seat. The gate is not a freeze mode, and no
`--freeze` was invoked anywhere.

## 5. Proposed README row (C11 owns the README delta; this row is the entry's own `- topic:` text, byte-equal)

- `sacred-kingship-mythic-charter.md` — how a myth system legitimates a ruler — the eight legitimation channels (divine descent, incarnation or vessel, delegation from a god, election and acclamation, conquest-and-test, installation rite, marriage-alliance into the divine line, and the regalia as found title-deed) with attested exemplars and the political cost of each; the king's-body-is-the-land's-body doctrine and the rule that it needs an observable channel (flood, harvest, weather, plague, victory) or it is decoration; the failing-king device family (regicide, jubilee or renewal, substitute king, mock king, abdication, interregnum) with a reliability grade per device; dual and co-sovereign slots (the king's two bodies, queen-mother and she-elephant pairs, the priest-versus-warrior split); installation and regalia; taboo and seclusion cost accounting; the stranger-king and the pedigree-distance rule; the re-legitimation toolkit for usurpers and the reception check; and the **royal register** — the speech levels addressed to the ruler, the ruler's own first person, the spokesman institution, name taboos, praise-recitation as performed pedigree (oríkì, royal hymns), and the oath formula — with a build order, a decision record, and a calibration shelf for the Frazer–Hocart divine-kingship tradition. Reference and method only; canon decisions belong to lore-shokunin.

Byte-equality of this row's description against the entry's `- topic:` value is
checked mechanically at assembly time (the row was generated from that line, not
retyped); see the assembly note below. Landing the row is C11's/integrator's call —
myth-symbol section header 19 → 20, totals line 201 → 202 for this entry alone, and
the footer vector reconciled by the round's counting command.

## 6. Missing dependencies, collision protocol, integrator notes

- **P01 (`reports/round-35/plan/P01-c-plan.md`) was not present at write time**, so
  this seat self-assigned its topic from its own census and absence sweep (§2). If
  P01 assigns C08 a different myth-symbol topic, the integrator should either (a) land
  this entry as an additional gap (then the round's declared after-counts move beyond
  claim C's `24/23` and the claim must be reported as exceeded, not silently summed),
  or (b) hold §3 and record the reassignment. Do not rename the entry to a topic it
  does not treat.
- **Collision protocol if C07/C09/C10 landed the same slug** (no `reports/round-35/cov/`
  fragment existed when this seat started, so this seat cannot see them): apply the
  round-19 convention (`reports/round-19/gaps.md` "Collision log") — append `-b` to
  this entry's slug and filename (`sacred-kingship-mythic-charter-b.md`) and add one
  sentence to the entry's `- gap filled:` line naming the earlier claimant. Everything
  else in §3 stands unchanged; the entry was written as an independent treatment and
  does not depend on any sibling's bytes.
- **K01/K02 (`scout/K01-coverage-census.md`, `scout/K02-entry-audit-method.md`) were not
  present**; §2's census/gap analysis and §4's apparatus check are this seat's own, run
  with the commands printed above, and are reproducible by the integrator.
- The entry's `- gap filled:` line contains a self-referential census of sibling files
  (nine myth-symbol files, with `file:line`); if a sibling entry lands in the same round
  and changes those counts, the line's *claim* (kingship appears only in passing) still
  holds, but the integrator should re-run the sweep before quoting the counts.

## 7. Limits

- **No retrieval pass this round** (round rules: no network). Every external
  bibliographic detail and every case-specific claim this seat could not check against
  a held copy or a lane citation carries an inline `(to-verify)`; the entry's §12 lists
  them all (61 marks on 47 lines, gate-counted). An auditor should grade this entry as
  *clean of unmarked unverified claims*, not as *verified*. This is the honest residue,
  not a hidden defect.
- The census and sweeps are point-in-time at HEAD `4a7aede`, 2026-10-19, and are
  re-measured before quoting (`- recheck:` line in the entry).
- This fragment claims one entry; the round's coverage claim needs all ten (C01–C10)
  and the README reconciliation (C11). Nothing here certifies the round.

## Owed

- `reports/round-35/plan/P01-c-plan.md` — the topic assignment for C08; absent at write
  time, so the topic in §3 is this seat's own gap choice (justified in §2). The
  integrator reconciles per §6.
- `reports/round-35/scout/K01-coverage-census.md` — absent; §2's census stands in.
- `reports/round-35/scout/K02-entry-audit-method.md` — absent; §4's apparatus check
  stands in, and C12's runbook is the intended instrument for the audit.
- Application of §3 and §5 to `corpus/knowledge/` and `corpus/README.md` — **integrator
  only** (this seat never writes corpus bytes).

## Citations

Paths read (all at lane HEAD `4a7aede`, 2026-10-19, read-only):
- `reports/round-35/claims.json` (claim C before/after, thresholds, non-goals);
  `reports/round-35/targets.json` (seat C08 object; `shared_rules`); `REGIMEN.md`.
- `corpus/QUALITY.md` (the five-item admission bar); `corpus/README.md:123-245,342`
  (partition headers, index rows, Known gaps).
- `corpus/knowledge/myth-symbol/{myth-ritual-theories.md:32-35,85, hero-journey-variants.md:56-57,110, pantheon-archetypes.md:49,61,85, cosmology-cosmography.md:38,108, plant-symbolism.md:77, ritual-liminality.md:40, creation-myths-taxonomy.md:90,110,133, flood-traditions.md:26,34,76}`.
- `corpus/knowledge/civilizations/{benin.md:1,42, persia-achaemenid.md:1}`;
  `corpus/knowledge/culture-material/era-periodization-models.md:8,67,69,75`;
  `corpus/knowledge/verification/calibration-registry.md:91`;
  `corpus/knowledge/linguistics/politeness-taboo-euphemism.md:37,62`;
  `corpus/knowledge/myth-symbol/trickster.md` §8.
- `corpus/knowledge/linguistics/{naming-systems.md, sociolinguistics-registers.md,
  kinship-terminology.md, orality-formulaic-language.md, semantics-pragmatics.md,
  register-strata-attestation.md, historical-linguistics.md}`;
  `corpus/knowledge/culture-material/{costume-semiotics.md,
  sumptuary-law-rank-display.md, ritual-garments.md,
  architecture-settlement-lexicon.md, calendar-festival-systems.md,
  trade-economy-lexicon.md}`; `corpus/knowledge/synthesis/{worldbible-integration-contract.md,
  consistency-verification-checklist.md}`; `corpus/knowledge/verification/{myth-consistency-gate.md,
  provenance-audit-ledger-format.md}`.
- `tools/gates/provenance-audit.py:1-60,280-340` (the gate's checks, empty-value rule,
  and `to-verify`-is-inventory-not-finding rule); `tools/source-audit-inventory.py`
  (`--help`, then `--json --summary --root corpus/knowledge`).
- `reports/round-19/gaps.md` (the slug/collision convention §6 relies on);
  `reports/round-19/entries/R19-C12.md` (prior-round author-fragment shape).

Commands run (outputs recorded in §2 and §4):
- `for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done` → 21/19/18/29/20/94
- `find corpus/knowledge -name '*.md' | wc -l` → 201
- `grep -rci kingship corpus/knowledge/myth-symbol/*.md | grep -v ':0'` → 9 files, 1–6 hits each
- the 21-term absence sweep printed in §2
- `python3 -B tools/gates/provenance-audit.py .scratch/c08-entry-8.md` → exit 0, `findings=0 blocked=0`, 61 marks/47 lines
- `git rev-parse HEAD` → `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4`
