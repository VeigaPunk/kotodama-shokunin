# CriticPeriodDrift — round 55 falsify, claim C §8 (What the being is for) and §9 (Period drift)

## Verdict

The named dates and counts all hold against the re-opened sources: 35,257 entries as of November 2023, 444 paintings, 1717, Kyōsai 1890 after a posthumous 1889 first edition, Pazuzu almost out of use by Parthian times, and the Mami Wata steps of the fifteenth century, circa 1887 and 1901.

Four sentences still state more than the page carries, and each needs a routed fix:

- **Hyena (line 100).** The "not to be eaten" ruling comes from the Aberdeen project's modern commentary, not from the manuscript chapter.
- **Taniwha (line 113, repeated at line 171).** "English writers" is an attribution the page does not make.
- **Polesye (line 104).** The entry turns an eastern-edge belief, and a classification the article calls "scant, isolated evidence", into a statement about all of Polesye. This is the generalisation from one record to a culture that the assignment asked me to flag.
- **Pazuzu (line 115).** The heading "Cults end, images stay" contradicts the one sentence it cites.

There are also five wrong locators and four smaller over-reads. None of these touch the mechanical legs of C (SET, SWEEP, FLOOR, RANGE, STATUS, USEDBY, ACCESS). They are review-only defects against the landed text at `eb0a331`.

Working-copy note: during this review the uncommitted copy changed "an 1887" to "a circa-1887" (line 111) and added "almost always believed to" to the rusalki sentence (line 104). Line numbers below are the working copy's. Every finding below still stands against that text.

## Items checked

### §8. What the being is for

- **line 97, S304 (Pazuzu as guardian): CARRIED. The heading is a low-severity over-read.**
  - Evidence: "Pazuzu, as a powerful demon, was frequently set up as a shield against another supernatural terror: Lamashtu" (Wayback `20171121161933`, paragraph opening "To answer this question"). The same paragraph has "supernatural beings in ancient references seem to be presented as largely amoral."
  - In the source, the "terror" is Lamashtu. Nothing says Pazuzu guards *by* terror.
  - Fix: `**Guardian by terror.**` -> `**Guardian against a worse being.**`

- **line 98, S302 and S301 (Ammit, Thoth, spell 30B): CARRIED, but the S301 locator is wrong.**
  - S302, Description: "a monster ready to spring forward to consume Ani's heart if he fails to pass the test", and Ani "mutters the words of Spell 30B … addressed to his heart".
  - S301: "Thoth, ibis-headed, holds a pen and scribal palette to record the outcome of the weighing."
  - That S301 passage is the *third* blank-line block of Curator's comments, in both capture `20230319160059` and capture `20260919094742`. Block 1 begins "'Book of the Dead' papyri are first found…". Block 2 is the one-line "Full size polychrome vignette of Hunefer in judgement scene."
  - Fix: `S301, Curator's comments, ¶2` -> `S301, Curator's comments, ¶3`. The same locator appears at line 58.

- **line 99, S319 (Grendel): WRONG-LOCATOR. The heading is a moderate over-read.**
  - Harrison and Sharp number the lines as 711 "Þâ com of môre under mist-hleoðum" and 712 "Grendel gongan, godes yrre bär". The edition's own glossary also gives "godes yrre, 712".
  - "Bore God's anger" does not make Grendel an executioner acting for God. The text supports bearing the anger, not carrying out a sentence.
  - Fix: `- **Executioner.** Grendel comes from the moor bearing God's wrath (S319, line 711).` -> `- **Bearer of God's anger.** Grendel comes from the moor bearing God's wrath (S319, lines 711–712).`

- **line 100, S334 (Aberdeen hyena): DEFECT (false provenance) and OVER-READ.**
  - The manuscript gives only one ground for uncleanness: "Its nature is that it is sometimes male, sometimes female, and it is therefore an unclean animal" (f11v, translation).
  - "The hyena should not be eaten because it is dirty and has two natures" sits under the page's **Commentary > Illustration**. That is the Bestiary Project's modern note. The Latin transcription of f11v carries no eating rule. The chapter itself ends on the sons of Israel and "those among us who are slaves to luxury and greed".
  - The entry's "unclean because … haunts tombs, imitates a voice" also folds the tomb and voice behaviour into the ground for uncleanness, which the text does not do.
  - Fix: `The Aberdeen hyena is unclean because it is sometimes male and sometimes female, haunts tombs, imitates a voice to lure a man out, and closes with a scriptural identification and a ruling that it should not be eaten (S334, Of the hyena; Illustration).` -> `The Aberdeen hyena is unclean because it is sometimes male and sometimes female; it haunts tombs, imitates a voice to lure a man out, and is read as the sons of Israel who turned to idols (S334, Of the hyena). The Bestiary Project's illustration commentary adds that it should not be eaten (S334, Commentary, Illustration).`

- **line 101, S335 (Cleveland jar): WRONG-LOCATOR.**
  - `description`: "As a mythical creature believed to make rain, the dragon served as a symbol of rulers in premodern East Asia."
  - The words "used exclusively for the king's paraphernalia" appear only in `did_you_know` (open-access API, artwork 153401).
  - The source links rain-making to rulership causally ("As a … creature"). The entry's "then" reads as a sequence.
  - Fix: `calls the dragon a creature believed to make rain, then a symbol of rulers whose image was used only for the king's paraphernalia (S335, description)` -> `calls the dragon a symbol of rulers because it was believed to make rain, and says its image was used only for the king's paraphernalia (S335, description; did_you_know)`

- **line 101, S336 (V&A robe): low-severity OVER-READ.**
  - The Summary lists "sun, moon, stars, mountain, dragon, …", which is "dragon", not "five-clawed dragon".
  - The physical description lists "the 'Twelve symbols'" and then, separately, "There are five-clawed dragons on the back and front" (api.vam.ac.uk, O498858).
  - Fix: `On a Qing emperor's robe the five-clawed dragon is one of the Twelve Imperial Symbols of Sovereignty, under a colour rule (S336, Summary).` -> `On a Qing emperor's robe the dragon is one of the Twelve Imperial Symbols of Sovereignty, under a rule reserving bright yellow for emperor and empress (S336, Summary); five-clawed dragons fill its front and back (S336, Physical description).`

- **line 101, S337 (Aberdeen dragon): CARRIED, with a low-severity WRONG-LOCATOR.**
  - Evidence: "Dragons are born in Ethiopia and India, where it is hot all year round." and "The Devil is like the dragon" (66r).
  - The 66r page is headed "the dragon, continued". The "Of the dragon" heading is on the previous folio.
  - Fix: `(S337, Of the dragon)` -> `(S337, the dragon, continued)`

- **line 102, S338 (taniwha as man-eater and guardian): CARRIED.**
  - Evidence: "In some traditions, taniwha were terrifying creatures that captured people and ate them." and "Others were kaitiaki, or protectors of iwi (tribes) and hapū" (Wayback `20260921201758`, "A creature of many forms").
  - Duplicate authority: S308 (the Te Ara print view of the whole story) and S338 (page 1) are the same text. Line 73 cites S308 for the same "A creature of many forms" passage. One authority carries two S-ids.

- **line 103, S307 (nine-tailed fox): CARRIED against the received text.**
  - zh.wikisource 南山經 has "其狀如狐而九尾，其音如嬰兒，能食人；食者不蠱".
  - "Protects" is a loose rendering of 不蠱 (the eater is not afflicted by *gu*). This is a low-severity point.
  - Limits: the 1668 leaf `n15.jpg` was re-fetched (HTTP 200, 2,263,724 bytes), but I did not match it character by character. ctext.org served a Cloudflare Turnstile page; that challenge was met and not passed, and was not routed around.

- **line 104, S339 (Polesye): OVER-READ. This generalises from one record to a culture.**
  - p. 193 (English summary): "The complex of beliefs about the spirits of natural loci (the wood, water and field goblins; leshy, vodyanoy, polevik, respectively) is represented by scant, isolated evidence."
  - p. 182: the domovik as master of the house "выступает преимущественно в поверьях жителей русских сел на восточной окраине Полесья" (appears mainly in the beliefs of Russian villages on Polesye's eastern edge). That is where the belief that he "непременно должен обитать в каждом доме" (must live in every house) is recorded.
  - p. 183: for the western domovik, "Противоречиво оценивается полешуками факт присутствия в доме" (the people of Polesye judge his presence in the house in contradictory ways), meaning some say he must be expelled.
  - p. 186: field spirits are "Практически полностью отсутствуют" (practically entirely absent). In the west the forest is the devil's locus.
  - Fix: `Polesye records class leshy, vodyanoy and field spirits as spirits of natural loci and the domovik as a house spirit whose presence the household needs (S339, pp. 182, 193).` -> `Vinogradova's Polesye survey files leshy, vodyanoy and polevik as spirits of natural loci but finds them carried by scant, isolated evidence (S339, pp. 182, 193); the belief that a domovik must live in every house for the household to prosper is recorded mainly in Russian villages on Polesye's eastern edge, while in the west his presence is judged both harmful and useful (S339, pp. 182–183).`

- **line 104, S340 (rusalki): low-severity OVER-READ.**
  - p. 83: the unclean dead are "those who died by unnatural or untimely death, were not allowed to be buried properly". This is Zelenin's model as Dynda reports it, and it applies to "young women, girls, or infants".
  - The defining feature is the death. Improper burial follows from it.
  - Fix: `Rusalki are the unquiet dead of improper burial, almost always believed to appear in Rusalia Week (S340, pp. 83–84).` -> `Rusalki are the souls of girls and women who died untimely or unnatural deaths and were denied proper burial, almost always believed to appear in Rusalia Week (S340, pp. 83–84).`

- **line 105, S341 (Smithsonian, Mami Wata): CARRIED.**
  - Evidence: "Her very name, which may be translated as 'Mother Water,' is pidgin English" and "a 'capitalist' deity par excellence" (Wayback `20090407065020`, Introduction).
  - The "may be translated" hedge is dropped. This is low-severity.
  - Duplicate authority: the same page says "All images on this web site are courtesy of the Fowler Museum at UCLA". S341 and S342 are one exhibition, Drewal's, so the Mami Wata bullets in §8 and §9 rest on one curatorial text, not two independent witnesses.
  - Fix: `The Smithsonian reads` -> `The Smithsonian's online edition of the Fowler exhibition reads`

### §9. Period drift

- **line 111, S342 (Fowler, Mami Wata): the dates are CARRIED. The framing is an OVER-READ, and "by 1901" generalises a regional record.**
  - The dates check out: "a fifteenth-century bronze medallion" (Sources and Currents ¶2), "circa 1887" and "By 1901" (¶3), and "recast as a demon working with the devil" (¶6). The working copy's "circa-1887" fix is correct.
  - **Not imports.** The medallion was not an import: "Created by an African carver, it was commissioned by a visiting Portuguese client who supplied the European mermaid image" (¶2).
  - **Hedge dropped.** The Fowler also says "the wellsprings of Mami Wata's visual culture and history remain conjectural" (¶2).
  - **Not first.** Masks "attest to the pervasiveness of water spirit imagery in Africa" (¶2). S341 adds that her depictions were "influenced by representations of ancient, indigenous African water spirits". The heading "The image arrives first" runs against both.
  - **One region.** The 1901 reading is placed "in the Niger River Delta region of Nigeria" (¶3). The entry drops the place.
  - Fix: `- **The image arrives first.** The Fowler dates Mami Wata's body to imports — a fifteenth-century mermaid medallion, a circa-1887 snake-charmer chromolithograph read as a water spirit by 1901 — and records her recast as a demon in Ghanaian film` -> `- **Imported images recompose an old being.** The Fowler, calling her wellsprings conjectural, dates layers of Mami Wata's look to Euro-African contact — a fifteenth-century medallion an African carver made from a Portuguese client's mermaid image, a circa-1887 Hamburg snake-charmer chromolithograph read as a water spirit in the Niger Delta by 1901 — and records her recast as a demon in Ghanaian film`. The locator stays.

- **line 112, S340 (fish-tailed rusalka): CARRIED, with a low-severity attribution note.**
  - p. 84: "the rapidly growing ethnographic evidence decisively show[ed] that the 'Russian mermaids' were for the most part a literary chimaera (Zelenin 1995, 182–183; Pomeranceva 1970)".
  - n. 3: the image was "'re-folklorized' and later ethnographically recorded … usually about the so-called faraonki or beregini".
  - Fix: `Dynda calls the fish-tailed Russian mermaid for the most part a literary chimera, an image imposed in the nineteenth and twentieth centuries and then recorded as tradition` -> `Dynda, following Zelenin and Pomeranceva, reports the fish-tailed Russian mermaid as for the most part a literary chimera, an image imposed in the nineteenth and twentieth centuries and then recorded as tradition, usually of faraonki or beregini`

- **line 113, S343 (griffins): CARRIED.**
  - Evidence: "although not labelled 'griffins' in their respective cultures (Boardman 2002)". Witton and Hing are citing Boardman here.
  - The section title in the PDF is "Griffin origins, fossil influences and the overlooked griffin-like creatures of pre-classical cultures". The shortened locator is a low-severity point.
  - The Pure portal file's sha256 matches the row: `181be558…3f61`.

- **line 113, S338 (taniwha as dragons): UNSUPPORTED attribution, and the page reverses the bullet's point.**
  - The page says "Others refer to them as dragons – many taniwha looked like reptiles, had wings and ate people." It names no English writers.
  - Te Ara grounds the dragon label in the body, which is the opposite of "names travel apart from bodies".
  - The same sentence is repeated at line 171.
  - Fix: `Te Ara notes that English writers have called taniwha dragons (S338, A creature of many forms).` -> `Te Ara notes that some call taniwha dragons, a label it ties to the reptile-like, winged, man-eating forms many taniwha took (S338, A creature of many forms).`
  - Line 171 fix: `English writers have called taniwha dragons (S338, A creature of many forms). The count comes from the English label.` -> `Te Ara reports that some call taniwha dragons (S338, A creature of many forms). The count comes from the English label.`

- **line 114, S295 (Nichibunken): CARRIED, with a WRONG-LOCATOR.**
  - Evidence: "Over two decades later, as of November 2023, the database comprises 35,257 entries." The same section has "spanning from the late Edo period to the present".
  - Both sentences sit under the h3 "Development of the Database". "Overview of the Yōkai Database" is the page's opening section, and it carries neither.
  - Fix: `(S295, Overview)` -> `(S295, Development of the Database)`. The same applies at line 176: `(S295, What is Yōkai Culture?; Overview)` -> `(S295, What is Yōkai Culture?; Development of the Database)`.

- **line 114, S344 (Walters W.659): CARRIED, with a low-severity OVER-READ.**
  - Evidence: "an Ottoman illuminated and illustrated Turkish version of 'Aja'ib al-makhluqat … completed in 1121 AH/AD 1717 … There are 444 paintings" (Wayback `20250318040834`).
  - A Turkish version is a translation, not a copy.
  - Fix: `the Walters' 1717 Ottoman copy of al-Qazwīnī` -> `the Walters' 1717 Ottoman Turkish version of al-Qazwīnī's Wonders of Creation`

- **line 114, S345 (Kyōsai): CARRIED.**
  - The API record (object 78669, HTTP 200) has `objectDate` "1890 (first edition published posthumously in 1889)" and `artistDisplayBio` "Japanese, 1831–1889".

- **line 114 heading ("Catalogues grow"): UNSUPPORTED.**
  - None of the three records gives two counts for one catalogue. Nichibunken gives a 2002 launch date but no launch count. The bullet stacks three single-date records into a trend.
  - Fix: `**Catalogues grow.**` -> `**Catalogues are dated objects.**`

- **line 115, S304 (Pazuzu's decline): the date is CARRIED. The heading contradicts the cited sentence.**
  - Evidence: "By the time of the Parthians, Pazuzu's image was already almost out of use; only two representations of the demon can be dated to this period" (paragraph opening "The grand buildings on the screen").
  - The cited sentence says the *image* stopped being used. The page never calls Pazuzu's use a cult; it describes amulets and a shield against Lamashtu.
  - The only "image stays" evidence on the page is a modern revival, the 1973 *The Exorcist*, not continuity.
  - Fix: `- **Cults end, images stay.** By Parthian times Pazuzu's image was almost out of use (S304, § "The grand buildings on the screen").` -> `- **Use fades; the image returns later.** By Parthian times Pazuzu's image was almost out of use, with only two representations dated to the period (S304, § "The grand buildings on the screen"); the 1973 *The Exorcist* revives him as a possessing demon (S304, § "Perhaps the most famous modern Pazuzu").`

## Checks not run

- I did not match the 1668 Shanhaijing leaf `n15` character by character. I checked S307 against the received text on zh.wikisource only. ctext.org returned a Cloudflare Turnstile challenge, which was met and not passed.
- I did not retry the live British Museum, Met blog or Te Ara URLs. Their rows already record HTTP 403, 429 or Cloudflare challenges, so I used only the rows' own Wayback captures.
- I did not run any acceptance or gate scripts (`accept-c.py`, `check-gate-quotes.py`). They are outside the §8 and §9 source scope.
- I did not read cited sources outside §8 and §9, apart from noting the S308 and S338 duplication and the line 58, 171 and 176 repeats.

No tools were installed or updated. Scratch files are in `/fast/scratch/hyaku/kotodama-r55-falsify/CriticPeriodDrift/`.
