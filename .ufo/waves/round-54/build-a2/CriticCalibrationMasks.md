# CriticCalibrationMasks — claim C calibration traps (round 54, attempt 2)

Seat: KotodamaR54a2.CriticCalibrationMasks (critic, leaf). Access date for every source: 2026-10-22. Every source below was opened this session with plain `curl` (no headless browser). Codes follow `corpus/knowledge/verification/calibration-registry.md:35-39` (R rejected, C contested, B bounded, H heuristic, T to-verify). Judged axes: coverage, calibration.

## Result

Of the eight popular claims, two are rejected as stated and none survives as a general truth. Two traps are only half traps: the evidence also blocks the over-corrected opposite, so marking them plain R would itself overclaim.

| # | Popular claim | Code for the bank | What the opened source says instead |
|---|---|---|---|
| 1 | "Persona comes from per-sonare, to sound through" | **R** if stated as the word's origin; **C** for the replacement (an Etruscan *phersu(na)* loan, possibly by way of Greek) | The ancient derivation is attested (Gavius Bassus in Gellius 5.7), but it needs a lengthened vowel. Mauss calls it "inventée après coup", and van den Berge calls it "doubtful etymology". The Etruscan alternative is itself unsettled: *phersu*'s meaning is unknown, and two of the sources disagree on whether the Greek *prosōpon* is involved. |
| 2 | "Masks are universal" | **R** for worn masks under a narrow definition; **T** under a broad definition (paint, tattoo) | Pernet: "the mask is practically absent from Polynesia", and there are "extensive zones in which masks are not used". With the broad definition the question "has not yet been systematically investigated". |
| 3 | "A mask always hides the wearer's identity" | **R** for "always"; **B** for concealment as one institution's rule | Pernet says the "primary function of masks is to represent rather than to conceal", and that women often know the mask's "true nature". Laciste: some masks do not fully cover the performer, and some have no face covering at all. NOMA: Venetian anonymity "was relative". |
| 4 | "Venetian masks existed so nobles could sin anonymously" | **R** as the reason masking existed; **B** for documented licence | Johnson says Venetians did not mask "for intrigue or corruption, as people visiting Venice at the time thought". Masking was "a token anonymity", the bauta was "required at official ceremonies", and masks were worn six months a year. NOMA also says the mask's secrecy "enabled a certain sexual freedom", so licence is not R. |
| 5 | "Death masks are portraits" | **B** (the term "death mask" covers different kinds of object); **R** as a general equation | The Mycenae "death-mask" was "hammered against a wooden background", not cast from a face, and it is only "so-called" Agamemnon. Pernet says some funerary masks "reveal traits that obviously did not belong to the deceased". The "absolutely true to nature" claim is Hutton's own 1893 framing, and his collection is "steeped in the legacy of Phrenology". |
| 6 | "African masks are art objects" | **B** (museum and market category); do not flip it to "not art" | The Met's own record classes the Kwifon crest as "Wood-Sculpture". The same record says it is "difficult to identify" once "stripped of their costumes", and that Kwifon "licenses their replication". Pernet calls the museum focus on the face "a distorted view". UNESCO notes that Gule Wamkulu is being reduced to entertainment for tourists. |
| 7 | Frazerian or evolutionist readings of masking | **R** as history or stage theory (existing CAL-04); **H** only as a period ideology | Pernet traces the evolutionist perspective, "survival" and the comparative method from Mannhardt to Meuli, and says the field turned away from such "ambitious theories". Frazer's own move: "In these northern maskers we see kings". |
| 8 | Jungian "persona" used as if it were ethnography | **H** (analytical-psychology term); **R** when used as evidence of what a community's masking means | The IAAP abstracts of Jung's Collected Works vol. 7 define persona in analytic, clinical terms: "only a mask for the collective psyche". Pernet: projecting Western mask-wearers' feelings onto other peoples is "if I were a horse" guesswork that "cannot be used as a general explanation". Existing registry row: `calibration-registry.md:132`. |

### Additional traps the bank should carry (found while testing the eight)

| # | Claim | Code | Evidence |
|---|---|---|---|
| 9 | "The wearer becomes the spirit or god" (the metamorphosis thesis) | **R** as a general account; **B** where a named community states it | Pernet: initiates stress that "only the uninitiated believe they are actually in the presence of a spirit or a god". Wipf & Stock series preface: the mask "is not generally used to enable its wearer to become what is represented". |
| 10 | "Masking is liberation or release" (carnival projection) | **R** as a general account; **B** for named carnival settings | Pernet: masking often "carries social responsibilities that make it a service rather than a liberation". Compare NOMA's Venetian "liberating effect", which holds for one city and period. |
| 11 | "Masks are as old as humanity" or "Paleolithic art shows masks" | **C** | Pernet: the Trois-Frères "Sorcerer" is now read as "a mythical mixed being (half man and half beast)", and "one cannot be categorical". Nunley's encyclopedia entry on the same page presents the ivory lion-headed figure as masking evidence. Do not cite Nunley for this. |
| 12 | "*Mask* comes from Arabic *maskhara*, from Egyptian *msk* 'second skin'" | **T** | This chain is carried only by Nunley (New Dictionary of the History of Ideas, on Encyclopedia.com) with no primary citation. I opened no lexicographic source this session, so it must not carry weight in the entry. |
| 13 | "Masks represent the dead or ancestors" (Meuli; Frobenius) | **R** as a general theory; **B** for named funerary masquerades | Pernet's conclusions say the mask "does not represent principally spirits or the dead" (Wipf & Stock). The lane already rejects "every mask is ancestor worship" at `civilizations/yoruba.md:200`. |

## Attacks on the entry, with the smallest safe fix

1. **Venice: R would be false provenance.** NOMA (a curator's feature) documents sexual licence and a "liberating effect". Johnson rejects intrigue as the *reason* masks were worn, not the occurrence of licence. Fix: mark R for "existed so that" and B for documented licence (Casanova, as NOMA cites it). Both sources are tier B: one is the author interviewed about his own book, the other a museum feature. The University of California Press preface (doi:10.1525/9780520948624-002) was not opened, so no sentence may cite the book's own wording.
2. **Universality: the strongest counterexample cuts both ways.** Pernet's article says only that the broad-definition question is *uninvestigated*. That makes it T, not R. Only the narrow-definition claim is refuted, and the counterexamples are Polynesia, highland New Guinea and other named zones. Fix: carry both codes and name the definition.
3. **Persona: do not swap one settled etymology for another.** van den Berge (2025, a preprint) says the word was "not derived from Greek prosōpon, but from Etruscan phersuna". Mauss (1938) reports Benveniste's suggestion that the Etruscans borrowed it from Greek. van den Berge also says *phersu*'s meaning is unknown, even whether it is a proper name. Fix: R for per-sonare as fact, C for the Etruscan origin and the Greek route. Cite Gellius as what one Roman grammarian proposed, not as the origin. Tier: Mauss is A for Mauss's position and B for the etymology (secondary, 1938). The preprint is B: it is a legal-history chapter, not a linguistics source.
4. **Death masks: the object class is split.** A plaster cast taken from a face (the Hutton collection) and a gold sheet hammered over a wooden form (Mycenae, National Archaeological Museum inv. 624) are both called "death masks". Princeton's own portal also calls its casts "3D portraits", so a flat R overclaims. Fix: B, with the variables kept apart: cast or made; taken from the face or idealised; purpose (relic, model for a portrait, phrenological specimen, grave good).
5. **"Art object": refuse the flip.** The Met's holding record classes the crest as "Wood-Sculpture", and Kwifon licenses copies. Art status and performance status coexist. Fix: B. The entry should say which regime it describes (museum, market, the society that owns the masquerade, tourism), not deny either one.
6. **In-lane collision.** `myth-symbol/ritual-liminality.md:38` lists the initiate as "anonymous (uniform, masking, secrecy)", which reads masking as anonymity without qualification. The entry should point to it one way and add the B qualification from trap 3, not restate Turner's register.
7. **Carrier risk on a page seats may reuse.** Encyclopedia.com's "Masks" URL hosts three articles. Pernet (Encyclopedia of Religion, 2005) is authoritative for the theory critique. Nunley's article (New Dictionary of the History of Ideas) carries traps 11 and 12 and universalist phrasing such as "Masks have existed from ancient times to space explorations". A row citing this URL must name which article it uses.
8. **Duplicate rows.** ScoutPersonaProsopon already opened Lewis & Short and Gellius 5.7 (`ScoutPersonaProsopon.md:13-14`). Where my rows 1-2 duplicate theirs, the L1 should keep one row per source so the registry gets no duplicate rows (the duplicate-row control in `accept-c.py`).

Impacted axes: calibration (codes 1-13) and coverage (the entry's calibration bank). There is no mechanical-leg impact: these are review-only clauses.

## Sources opened (draft ids)

### NEW-CriticCalibrationMasks-1
citation: Aulus Gellius, *Noctes Atticae* 5.7, trans. J. C. Rolfe (Loeb, 1927), LacusCurtius edition
url: https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Gellius/5*.html
route: direct, HTTP 200
kind: book (classical text)
tier: A (primary for what Gavius Bassus proposed); not evidence for the true etymology
scope: the ancient per-sonare derivation and its admitted vowel lengthening
quotes:
- NA 5.7.1: "he suggests that that word is formed from personare."
- NA 5.7.2: "it is for that reason called persona, the o being lengthened because of the formation of the word."
note: duplicates ScoutPersonaProsopon's Gellius row; keep one.

### NEW-CriticCalibrationMasks-2
citation: Lewis, Charlton T. & Short, Charles (1879), *A Latin Dictionary*, entry persōna, Perseus 1999.04.0059
url: https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.04.0059:entry=persona
route: direct, HTTP 200
kind: book (dictionary)
tier: B (a standard 19th-century dictionary that relays Bassus; not current etymology)
scope: that the standard dictionary relays the derivation as Bassus's, with the lengthening noted
quotes:
- headword bracket: "[acc. to Gabius Bassus ap. Gell. 5, 7, 1 sq., from per-sŏno, to sound through, with the second syllable lengthened]"
- sense I: "A mask, esp. that used by players, which covered the whole head"
note: duplicates ScoutPersonaProsopon's Lewis & Short row; keep one.

### NEW-CriticCalibrationMasks-3
citation: Mauss, Marcel (1938), "Une catégorie de l'esprit humain : la notion de personne, celle de « moi »", *Journal of the Royal Anthropological Institute* 68; Les Classiques des sciences sociales (UQAC) digital edition by J.-M. Tremblay
url: https://psychaanalyse.com/pdf/une_categorie_de_l_esprit_humain_la_notion_de_personne_celle_de_moi_marcel_mauss.pdf
route: direct, HTTP 200 (application/pdf). This is a mirror of the UQAC edition and the PDF carries the Classiques colophon; the UQAC origin was unreachable (curl exit 28: connection failed after 135 s).
kind: paper
tier: A for Mauss's own position; B for the etymology (secondary, 1938)
scope: Mauss's rejection of per-sonare and the Etruscan and Greek hypotheses as of 1938
quotes:
- ch. IV, p. 18: "Voici comment, avec quelque hardiesse, je puis me figurer cette histoire"
- ch. IV, p. 18: "l'explication des étymologistes latins, persona venant de per/sonare, le masque à travers (per) lequel résonne la voix (de l'acteur) est inventée après coup"
- ch. IV, p. 18: "En réalité, le mot ne semble même pas de bonne souche latine ; on le croit d'origine étrusque"
- ch. IV, p. 19: "M. Benveniste me dit qu'il se peut qu'il vienne d'un emprunt fait par les Étrusques au grec"

### NEW-CriticCalibrationMasks-4
citation: van den Berge, Lukas (2025), "Phersu, Prosōpon, Persona: On Legal Personhood, Roman Sculpture and the Art of Law", in *Forever Composed of Nows: Celebrating Jeanne Gaakeer's Work on Law, Language and Literature*, Boom; preprint, hdl 1874/483290
url: https://research-portal.uu.nl/ws/files/278388932/Phersu_Prosopon_Persona_final_version_.pdf
route: direct, HTTP 200
kind: paper (preprint)
tier: B (preprint; a legal-history chapter, not a linguistic authority)
scope: the current Etruscan-loan view and its uncertainty; per-sonare called doubtful
quotes:
- preprint PDF p. 4, n. 9: "a connection, to be sure, that is based on doubtful etymology"
- PDF p. 6: "Sadly, little more is known about this figure – not even if phersu should be understood as the man's proper name"
- PDF p. 6: "As scholars generally agree, it is this Etruscan word that the Romans incorporated in their language as persona."
- PDF p. 14: "Contrary to widespread belief, the Latin word persona ('mask') was not derived from Greek prosōpon, but from Etruscan phersuna"

### NEW-CriticCalibrationMasks-5
citation: Pernet, Henry (2005), "Masks", *Encyclopedia of Religion*, 2nd ed., ed. Lindsay Jones (Macmillan Reference / Gale), hosted by Encyclopedia.com (first of three articles on the page)
url: https://www.encyclopedia.com/sports-and-everyday-life/fashion-and-clothing/clothing-jewelry-and-personal-adornment/masks
route: direct, HTTP 200
kind: web (reference article)
tier: A for the state and critique of comparative mask theory (by the field's synthesising specialist); B for any single community's fact (secondary)
scope: universality, distribution, concealment versus representation, metamorphosis, evolutionist and Meuli theories, funerary masks, secrecy
quotes:
- Problems of Definition ¶1: "As M. C. Jedrej (1980) puts it, the word "mask" identifies no coherent class of institutions of any use to social anthropologists."
- Problems of Definition ¶2: "it is only when makeup, paintings, and tattoos are included in the definition of mask"
- Problems of Definition ¶2: "But is such a broad definition justified? No one can say, for this question has not yet been systematically investigated."
- Problems of Definition ¶3: "the focus on the face that museums, art galleries, and books on masks often maintain gives a distorted view of the ritual mask."
- The Geography of Ritual Masks ¶1: "Finally, in Oceania the mask is practically absent from Polynesia."
- The Geography of Ritual Masks ¶1: "even in regions that are traditionally considered the privileged domains of masks there exist extensive zones in which masks are not used."
- The Dating of Masks ¶1: "paleontologists now prefer to see in it the portrayal of a mythical mixed being (half man and half beast)"
- What Does the Ritual Mask Represent? ¶10: "The few examples given above also show that the primary function of masks is to represent rather than to conceal."
- The Mask and Its Wearer ¶4: "only the uninitiated believe they are actually in the presence of a spirit or a god"
- The Mask and Its Wearer ¶5: "the feeling of liberation experienced by Western mask wearers was projected onto African, American, or Melanesian mask wearers."
- The Mask and Its Wearer ¶5: "Even if such a feeling may exist among some of these people, it cannot be used as a general explanation of the masked-ritual phenomenon."
- The Mask and Its Wearer ¶6: "Moreover, wearing a mask often carries social responsibilities that make it a service rather than a liberation."
- The Mask and the Dead ¶8: "Others, sometimes called "idealistic," reveal traits that obviously did not belong to the deceased."
- Historical Overview ¶3: "the evolutionist perspective, following which the history of Western society can be reconstructed by classifying all known societies according to the degree of civilization"
- Historical Overview ¶1: "masks were interpreted as representing demons of the vegetal world."
- Masks, Women, and Secret Societies ¶3: "the best-documented reports from Africa, Melanesia, and the Americas acknowledge that women in particular know the true nature of masks"
note: this row carries more than four quotes because it backs eight traps; the L1 may split it or choose the quotes per sentence. The same URL also hosts Nunley's article (traps 11 and 12); do not cite that article.

### NEW-CriticCalibrationMasks-6
citation: Pernet, Henry (1992; Wipf and Stock reprint 2006), *Ritual Masks: Deceptions and Revelations*, trans. Laura Grillo, ISBN 9781597525855; publisher page with an excerpt from the series editor's preface (Frederick Mathewson Denny)
url: https://wipfandstock.com/9781597525855/ritual-masks/ (redirected to https://wipfandstock.com/products/ritual-masks-9781597525855?variant=59023972237647)
route: direct, HTTP 200
kind: web (publisher description)
tier: B (publisher description, QUALITY criterion 6)
scope: summary of Pernet's book-length conclusions only
quotes:
- series editor's preface excerpt: "the mask is not universal, it has not existed in all times, it does not represent principally spirits or the dead"
- same paragraph: "the mask is not generally used to enable its wearer to become what is represented."

### NEW-CriticCalibrationMasks-7
citation: Boston University, *BU Today* (21 February 2012), "Unmasking the Past", interview with James H. Johnson about *Venice Incognito: Masks in the Serene Republic* (University of California Press, 2011)
url: https://www.bu.edu/articles/2012/unmasking-the-past/
route: direct, HTTP 200
kind: web (interview)
tier: B (the author summarising his own book)
scope: why 18th-century Venetians masked; the duration and social function of masking
quotes:
- answer 1: "To learn that Venetians wore masks six months out of the year, from when the theater season started in the fall through Carnevale."
- answer 1: "Also, they were not wearing masks to disguise themselves or for intrigue or corruption, as people visiting Venice at the time thought."
- answer 2: "That didn’t mean that people were disguised and that they didn’t know each other’s rank, but it’s a token anonymity"

### NEW-CriticCalibrationMasks-8
citation: Schmid, Vanessa (New Orleans Museum of Art, 21 March 2017), "Behind the mask in 18th-century Venice", *Arts Quarterly* online feature
url: https://noma.org/behind-mask-18th-century-venice/
route: direct, HTTP 200
kind: web (museum feature)
tier: B (curator's secondary synthesis)
scope: relative anonymity, required and status-specific mask types, documented licence
quotes:
- para. "The anonymity of the mask…": "The anonymity of the mask was relative, of course. A member of the noble classes could easily be identified by his servant"
- same para.: "The bautta mask, for example, was reserved for the nobility and uppermost middle class and was required at official ceremonies."
- para. "At first glance…": "as profusely and notoriously demonstrated by Casanova’s exploits, the mask’s secrecy enabled a certain sexual freedom."

### NEW-CriticCalibrationMasks-9
citation: Hellenic Ministry of Culture and Sports, Odysseus portal, National Archaeological Museum, "Mask of 'Agamemnon'", inv. 624
url: http://odysseus.culture.gr/h/4/eh430.jsp?obj_id=4503
route: direct, HTTP 200 (page encoded windows-1253)
kind: record
tier: A (holding institution's object record)
scope: how this "death mask" was made and how it was attached; its "so-called" attribution; date
quotes:
- description ¶1: "This so-called mask of Agamemnon is the best known of Schliemann's finds from the royal tombs at Mycenae."
- description ¶1: "A death-mask, it was made from a thick sheet of metal hammered against a wooden background"
- description ¶1: "Two holes near the ears were used to hold the mask in place with twine over the deceased's face."
- features table: "Late Bronze Age, 16th century B.C."

### NEW-CriticCalibrationMasks-10
citation: Princeton University Library, Digital PUL, "Laurence Hutton Collection of Life and Death Masks" (portal home and "The History of the Collection")
url: https://dpul.princeton.edu/life-death-masks ; https://dpul.princeton.edu/life-death-masks/feature/the-history-of-the-collection
route: direct, HTTP 200 (both)
kind: record (holding library's collection portal)
tier: A for the library's statements about its own collection; the Hutton 1893 quote is primary for the 19th-century claim
scope: where the "death mask as true portrait" claim comes from; the phrenological purpose of the collection
quotes:
- home, epigraph (Hutton, *Harper's Monthly*, 1893): "The value of a plaster cast as a portrait of the dead or living face cannot for a moment be questioned."
- home, intro: "Beyond their eerie qualities, the masks also act as 3D portraits, speaking to Victorian relationships with celebrity, death, determinism and phrenology."
- history page, phrenology note, last para.: "The Laurence Hutton Death Mask Collection is undeniably steeped in the legacy of Phrenology and all that such a legacy means."

### NEW-CriticCalibrationMasks-11
citation: The Metropolitan Museum of Art, "Helmet crest from a Ngumba/Kwifon masquerade", Kom peoples, Tikar group, 19th century, object 1972.4.2
url: https://web.archive.org/web/20260217123445/https://www.metmuseum.org/art/collection/search/309790
route: Wayback capture 20260217123445. The live page served a Vercel Security Checkpoint (HTTP 429): challenge met, not passed.
kind: record
tier: A (holding museum's record)
scope: the mask as a regulatory society's property; licensed replication; loss of identity once stripped of its context; museum classification
quotes:
- label: "Given the popularity of the masks, Kwifon sometimes licenses their replication to local lineage groups."
- label: "Isolated from their performance contexts and stripped of their costumes, the glossy, iron-blackened dance crests become difficult to identify."
- metadata: "Classification: Wood-Sculpture"

### NEW-CriticCalibrationMasks-12
citation: Laciste, Kristen, "Masquerade basics", Smarthistory
url: https://web.archive.org/web/20251214145154/https://smarthistory.org/masquerade-basics/
route: Wayback capture 20251214145154. The live page served a Cloudflare "Just a moment" page (HTTP 403): challenge met, not passed.
kind: web (educational essay)
tier: B (secondary teaching essay by an art historian)
scope: "mask" in African contexts as an ensemble; partial or no concealment; the museum fragment
quotes:
- ¶ on identities: "In some instances, these do not completely cover the mask performers, so their identities are not entirely concealed from the audiences."
- same ¶: "In other cases, masks might not even have a facial covering or headpiece."
- ¶ on museums: "The absence of the accompanying costumes and accessories erroneously suggests that the facial covering or headpiece is the most valuable and significant component"

### NEW-CriticCalibrationMasks-13
citation: Frazer, James George (1922), *The Golden Bough: A Study in Magic and Religion*, abridged ed., Macmillan; Project Gutenberg eBook #3623
url: https://www.gutenberg.org/cache/epub/3623/pg3623.txt
route: direct, HTTP 200
kind: book
tier: A (primary for what Frazer argued; not evidence for the customs' meaning)
scope: the Frazerian move that turns European maskers into "Kings of the Wood"
quotes:
- ch. XXVIII §1 "The Whitsuntide Mummers" (Semic, Bohemia): "a mask hides his face, and for a sceptre he has a hawthorn switch in his hand"
- ch. XXVIII §1: "In these northern maskers we see kings"
- ch. XXVIII §1: "proclaim them unmistakably as, like their Italian counterpart, Kings of the Wood"

### NEW-CriticCalibrationMasks-14
citation: International Association for Analytical Psychology, "Volume 7: Two Essays on Analytical Psychology", Collected Works abstracts (entries 000171 and 000181; Jung, CW 7, 2nd ed., Princeton University Press, 1966, pp. 156-162 and 280-283)
url: https://iaap.org/resources/academic-resources/collected-works-abstracts/volume-7-two-essays-analytical-psychology/
route: direct, HTTP 200
kind: web (abstracts)
tier: B (abstracts, not Jung's text)
scope: that Jung's persona is an analytic and clinical construct about the individual and the collective psyche
quotes:
- abstract 000171: "The persona consists of the sum of psychic facts that are felt to be personal. It is, however, only a mask for the collective psyche."
- abstract 000181: "During analysis this mask is stripped off and the individual is seen to be, at bottom, collective."

### NEW-CriticCalibrationMasks-15
citation: UNESCO Intangible Cultural Heritage, "Gule Wamkulu" (Malawi, Mozambique, Zambia), inscribed 2008 (3.COM), proclaimed 2005
url: https://ich.unesco.org/en/RL/gule-wamkulu-00142
route: direct, HTTP 200, full text served to plain curl. ReviewSacredAccess reports a bot challenge on the same URL (`ReviewSacredAccess.md:182`), so the L1 may prefer their Wayback row; this seat met no challenge.
kind: web (heritage nomination summary)
tier: A (the inscribing body's own statement, for the scope of the inscription)
scope: masking held by an initiated men's society; tourist and political reuse (trap 6)
quotes:
- description ¶1: "It was performed by members of the Nyau brotherhood, a secret society of initiated men."
- description ¶3: "Gule Wamkulu performances are gradually losing their original function and meaning by being reduced to entertainment for tourists and for political purpose."

## Draft calibration-bank lines (each carried by an opened quote)

- Do not give per-sonare as the origin of *persona*: the derivation is Gavius Bassus's, as Gellius reports, and needs "the o being lengthened" (NEW-CriticCalibrationMasks-1, NA 5.7.2). Mauss called it invented after the fact (NEW-CriticCalibrationMasks-3, ch. IV p. 18). Code R as fact.
- Treat the Etruscan origin as the favoured but open hypothesis: one source says scholars "generally agree" (NEW-CriticCalibrationMasks-4, PDF p. 6), while Mauss reports Benveniste's suggestion of an Etruscan borrowing from Greek (NEW-CriticCalibrationMasks-3, ch. IV p. 19). Code C.
- Masks are not universal under a definition limited to worn face or head coverings: "in Oceania the mask is practically absent from Polynesia" (NEW-CriticCalibrationMasks-5, Geography ¶1). The broad-definition claim is untested (NEW-CriticCalibrationMasks-5, Problems of Definition ¶2). Code R and T.
- Decide per institution whether a mask conceals its wearer: the comparative literature finds masks mainly "represent rather than to conceal" (NEW-CriticCalibrationMasks-5, What Does the Ritual Mask Represent? ¶10), and some have no face covering at all (NEW-CriticCalibrationMasks-12, identities ¶). Code R for "always", B for named concealment rules.
- Venetian masking was a seasonal custom of "token anonymity", not a device for corruption (NEW-CriticCalibrationMasks-7, answer 2). The bauta was nonetheless required at official ceremonies (NEW-CriticCalibrationMasks-8, anonymity para.), and documented licence remains B (NEW-CriticCalibrationMasks-8, "At first glance" para.).
- Separate cast death masks from made funerary masks: the Mycenae mask was hammered over wood (NEW-CriticCalibrationMasks-9, description ¶1), and some funerary masks show traits "that obviously did not belong to the deceased" (NEW-CriticCalibrationMasks-5, The Mask and the Dead ¶8). Code B.
- Name the regime in which a mask counts as art: a holding museum classes a Kwifon crest as sculpture, yet stripped of its costume it becomes hard to identify, and the society licenses its copies (NEW-CriticCalibrationMasks-11, label and metadata). Code B.
- Use Frazer's maskers-as-Kings-of-the-Wood only as period ideology (NEW-CriticCalibrationMasks-13, ch. XXVIII §1; CAL-04). Use Jung's persona only as a designer heuristic, never as evidence of a community's meaning (NEW-CriticCalibrationMasks-14, abstract 000171; NEW-CriticCalibrationMasks-5, The Mask and Its Wearer ¶5).

## Unopened

- http://classiques.uqac.ca/classiques/mauss_marcel/socio_et_anthropo/5_categorie_de_l_esprit_humain/notion_de_personne.pdf (the UQAC origin of the Mauss text): curl exit 28, "Failed to connect to classiques.uqac.ca:80 after 135162 ms", HTTP 000. The server was unreachable (no access control), so the mirror copy was used instead.
- https://doi.org/10.1525/9780520948624-002 (Johnson, *Venice Incognito*, preface, De Gruyter Brill): HTTP 202 with an empty body, a challenge-type response. Challenge met, not passed; not routed around.
- https://library.princeton.edu/libraries/firestone/rbsc/aids/C0770/a-c.html (Hutton finding aid): Cloudflare HTTP 403. Challenge met, not passed; not routed around and not needed.
- archive.org copies of Jung, CW 7 (`twoessaysonanaly0007jung` and similar): lending-library items behind a login. Not attempted; the IAAP abstracts were used instead.
- Treccani "Persona", Springer doi:10.1007/s11196-021-09835-9, Etymonline and Wiktionary: seen only as search-result snippets, not opened, and not evidence here. Treccani's snippet repeats per-sonare as fact, which shows the trap persists in reference works.

Unrun checks: none of this seat's (critic, no gates). Tools: none installed or upgraded. Temporary files under /tmp were deleted; nothing was written outside this report.
