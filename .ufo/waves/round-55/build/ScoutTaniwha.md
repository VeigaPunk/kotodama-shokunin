# ScoutTaniwha — taniwha in Te Ara and Te Aka

- seat: `KotodamaR55.ScoutTaniwha` (scout, claim C ground: monsters and hybrid beings)
- round: kotodama 55 (hyaku phase 4), 2026-10-22
- lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, declaration `8eda9543e940bdc4938fad90182ee6a6fe271d0f`, claim base `f4015e70b829523ed81e14ce4279bfab0e0233e4`
- assignment: claim C source item; Te Ara, the Encyclopedia of New Zealand (Manatū Taonga), entry "Taniwha", quoting what it says taniwha are and how they appear in public decisions
- draft ids used below: `NEW-ScoutTaniwha-1`, `-2`, `-3`; the L1 assigns the final `S` ids at integration

## Route summary

Two sources, four pages read: three URLs of the one Te Ara story (two filed as rows) and one dictionary page (filed). Every live `teara.govt.nz` request returned HTTP 403 with the Cloudflare
"Just a moment..." interstitial — challenge met, not passed. All Te Ara text below was read from Wayback
captures of the same URLs. Every quote below was verified by exact substring match against the normalized text of
the file it is attributed to (all quotes: hit, 0 misses). Te Aka answered a plain request directly.

| page | URL | live status | what was read |
|---|---|---|---|
| story, full print view | `https://teara.govt.nz/en/taniwha/print` | direct plain request, HTTP 403 (challenge met, not passed) | Wayback capture `20260208222348`, HTTP 200, 50802 bytes |
| story, page 1 "What are taniwha?" | `https://teara.govt.nz/en/taniwha/page-1` | direct plain request, HTTP 403 (challenge met, not passed) | Wayback capture `20260921201758`, HTTP 200, 661021 bytes |
| story landing page (read for cross-check; not filed as a row) | `https://teara.govt.nz/en/taniwha` | direct plain request, HTTP 403 (challenge met, not passed) | Wayback capture `20261005073958`, HTTP 200, 662755 bytes |
| dictionary entry | `https://maoridictionary.co.nz/search?keywords=taniwha` | direct plain request, HTTP 200 | served HTML, 171749 bytes |

Access date for all: 2026-10-22. The print view is one document carrying the whole ten-page story, so section
headings below are locators inside that document; page 1 is filed separately because it is the definitional page
and because a 2026-09-21 capture confirms its text still stands. The `page-9` URL ("Taniwha today") returned no
capture from the availability API; its text is inside the print view.

---

### NEW-ScoutTaniwha-1

citation: Keane, Basil. 2012. "Taniwha", Te Ara – the Encyclopedia of New Zealand, Manatū Taonga Ministry for Culture and Heritage, story published 22 September 2012, full-story print view. No DOI; the encyclopedia's own cite line on the story pages gives `https://teara.govt.nz/en/taniwha` as the stable address.

url: https://web.archive.org/web/20260208222348/https://teara.govt.nz/en/taniwha/print

route: direct plain request to `https://teara.govt.nz/en/taniwha/print` returned HTTP 403 with the Cloudflare "Just a moment..." interstitial (challenge met, not passed); opened from Wayback capture `20260208222348`, HTTP 200, 50802 bytes, text/html, access date 2026-10-22.

kind: web (signed entry in a national encyclopedia)

tier: A — Manatū Taonga's national encyclopedia, signed story by a named author, published 2012 and still served; authoritative for the summary it gives of named tribal traditions, with every claim kept attributed to it and none generalized to "Māori believe".

scope: the story's account of taniwha forms, waters and lairs; named beings across regions (Tūtaeporoporo of the Whanganui River, Āraiteuru of Hokianga, Ngārara Huarau, Takere-piripiri, Whātaitai and Ngake, Pelorus Jack/Tuhirangi); slaying methods; and the early-2000s Karutahi and Takauere construction disputes. It supports statements about what this encyclopedia reports, including that forms vary by tribal tradition and that Māori disagreed over the 2000s objections. It does not support any claim about what all Māori believe, about a living iwi's own account, or about the date of any tradition.

quotes:
- What are taniwha? — A creature of many forms: "They hid in lairs known as rua taniwha, which could be deep pools, caves, or dangerous waterways – areas that people avoided."
- Sharks — Tūtaeporoporo: "Then he began to change, with hard, spiky skin, bat-like wings, a lizard-like tail, webbed feet and claws like a hawk’s."
- Taniwha today — Karutahi: "Eventually, Transit New Zealand agreed to partially reroute the highway."
- Taniwha today — Takauere: "Ultimately, against these objections the prison was built."

teaches: A signed national encyclopedia account gives taniwha as shape-changing water beings with named lairs, guardian and man-eater roles, composite bodies, and 2000s highway and prison disputes.

draft sentences:
- Build the monster's body by accretion: Tūtaeporoporo begins as a shark and changes into hard, spiky skin, bat-like wings, a lizard-like tail, webbed feet and hawk-like claws, and his head becomes a featherless bird's while he retains shark's teeth (NEW-ScoutTaniwha-1, Sharks — Tūtaeporoporo).
- Put the being in water people already avoid: rua taniwha are deep pools, caves or dangerous waterways, so its address is a place on the travellers' route, not a separate world (NEW-ScoutTaniwha-1, What are taniwha? — A creature of many forms).
- Let the being enter public procedure: in 2002 the Ngāti Naho hapū objected to a Waikato highway that would destroy Karutahi's lair and Transit New Zealand partially rerouted it, while a Ngāwhā prison was built although local hapū said it would impede the travel of the log taniwha Takauere (NEW-ScoutTaniwha-1, Taniwha today — Karutahi and Takauere).

---

### NEW-ScoutTaniwha-2

citation: Keane, Basil. 2012. "Taniwha – What are taniwha?", Te Ara – the Encyclopedia of New Zealand, page 1 of the story, published 22 September 2012.

url: https://web.archive.org/web/20260921201758/https://teara.govt.nz/en/taniwha/page-1

route: direct plain request to `https://teara.govt.nz/en/taniwha/page-1` returned HTTP 403 with the Cloudflare "Just a moment..." interstitial (challenge met, not passed); opened from Wayback capture `20260921201758`, HTTP 200, 661021 bytes, text/html, access date 2026-10-22.

kind: web (signed entry in a national encyclopedia, page 1)

tier: A — same encyclopedia, same author and story, a distinct page URL; authoritative for the definitions and terms it sets out, scoped to this page and attributed to it.

scope: the story's definitional page — tribal variation of form, water habitats, rua taniwha as avoided places, the man-eater and kaitiaki split with karakia and offerings at dens, shape-changing, and the Waikato proverb that reads taniwha as great chiefs. Carries no dated case and no region-by-region detail; the public-decision cases are on the story's later pages (row 1 carries them).

quotes:
- What are taniwha? — A creature of many forms: "Taniwha are supernatural creatures whose forms and characteristics vary according to different tribal traditions."
- What are taniwha? — A creature of many forms: "Others refer to them as dragons – many taniwha looked like reptiles, had wings and ate people."
- What are taniwha? — A creature of many forms: "Others were kaitiaki, or protectors of iwi (tribes) and hapū (sub-tribes)."
- What are taniwha? — A creature of many forms: "Some taniwha could change their shape, moving between different forms."

teaches: The definitional page fixes taniwha as tribally variable, water-dwelling, sometimes shape-changing, split between man-eaters and kaitiaki honoured with karakia and offerings.

draft sentences:
- Write a bestiary by place and source rather than as one canonical profile: Te Ara says taniwha forms and characteristics vary according to different tribal traditions, so each entry needs the tradition it came from (NEW-ScoutTaniwha-2, What are taniwha? — A creature of many forms).
- Split the category by conduct, not by species: some taniwha were terrifying creatures that captured and ate people, while others were kaitiaki, protectors of iwi and hapū, respected and given karakia and an offering at their dens (NEW-ScoutTaniwha-2, What are taniwha? — A creature of many forms).
- Decide whether shape is fixed: the page says many taniwha looked like reptiles, had wings and ate people, and that some could change their shape, moving between different forms (NEW-ScoutTaniwha-2, What are taniwha? — A creature of many forms).

---

### NEW-ScoutTaniwha-3

citation: Moorfield, John C. Te Aka Māori-English, English-Māori Dictionary and Index. Online edition, © 2003–2026 John C Moorfield / Te Murumāra Foundation. Entries "taniwha" (sense 1), "niho taniwha", "taniwha hikuroa", "unuhanga taniwha", "mangō taniwha". No publication date on the entry pages.

url: https://maoridictionary.co.nz/search?keywords=taniwha

route: direct plain request, HTTP 200, text/html, 171749 bytes, access date 2026-10-22.

kind: web (dictionary)

tier: A — Moorfield's Māori–English dictionary, the reference work the site presents as continuing his Te Whanake suite, authoritative for the word's glosses, its sense range and its compound terms; the Journal of the Polynesian Society passages it quotes as examples are early twentieth-century journal record and would be tier B if used as ethnography.

scope: lexical — the sense range of `taniwha` (water spirit, monster, dangerous water creature, powerful creature, chief, powerful leader, something or someone awesome), the habitats the gloss names, and compounds: `niho taniwha` (a woven pattern), `taniwha hikuroa` ("a person with many followers"), `unuhanga taniwha` ("unleashing something that then proves impossible to control"), `mangō taniwha` (great white shark). Supports naming, derived-term and depiction sentences; not an authority for ritual practice, for any iwi's tradition, or for dating.

quotes:
- taniwha, sense 1: "water spirit, monster, dangerous water creature, powerful creature, chief, powerful leader, something or someone awesome"
- taniwha, sense 1: "taniwha take many forms from logs to reptiles and whales and often live in lakes, rivers or the sea."
- taniwha, sense 1: "They are often regarded as guardians by the people who live in their territory, but may also have a malign influence on human beings."
- niho taniwha: "The principal motif that represents the realm of mythology and a chief's lineage from the gods."

teaches: Te Aka gives the word's range — water spirit, monster, chief, awesome thing — its lake, river and sea habitats, and niho taniwha as a woven descent motif.

draft sentences:
- Decide what the common noun still carries before naming the species: Te Aka glosses taniwha as water spirit, monster, dangerous water creature, powerful creature, chief, powerful leader, something or someone awesome (NEW-ScoutTaniwha-3, taniwha, sense 1).
- Let habitat and movement identify the being as much as anatomy: the dictionary says taniwha take many forms from logs to reptiles and whales and often live in lakes, rivers or the sea (NEW-ScoutTaniwha-3, taniwha, sense 1).
- Carry the being into objects that outlive the story: niho taniwha is the saw-edged pattern of tukutuku panels and tāniko weaving on cloak hems, the principal motif for the realm of mythology and a chief's lineage from the gods (NEW-ScoutTaniwha-3, niho taniwha).

---

## Findings for the entry's design decisions

| design decision | what these three pages carry | evidence |
|---|---|---|
| what the culture calls the being and what the word means | the headword ranges from water spirit and monster to chief and "something or someone awesome", and the same root yields a chief with many followers (`taniwha hikuroa`) and a warning against "unleashing the monster" (`unuhanga taniwha`). Te Ara separately records the Waikato proverb "Waikato taniwha rau, he piko he taniwha", read by some as the river's many taniwha and by others as the area's many important chiefs | NEW-ScoutTaniwha-3 quotes 1–4; NEW-ScoutTaniwha-2 "Taniwha and chiefs" (proverb on the page, not quoted) |
| how its body is composed | Tūtaeporoporo: shark, then hard spiky skin, bat-like wings, lizard-like tail, webbed feet, hawk-like claws, a featherless-bird head, and he keeps shark's teeth. The page-1 summary says dragons, reptiles with wings, sharks, whales, octopuses, logs, and shape-changing between forms | NEW-ScoutTaniwha-1 "Sharks — Tūtaeporoporo"; NEW-ScoutTaniwha-2 quotes 2 and 4 |
| where it lives relative to the known world | in or near water — lakes, rivers, sea — with lairs called rua taniwha: deep pools, caves, dangerous waterways that people avoided; a being may also be a log drifting against the current, a geothermal spring, or a harbour head | NEW-ScoutTaniwha-1 quote 1 and "Whales, dolphins and enchanted logs — Rākau tipua – enchanted logs"; NEW-ScoutTaniwha-3 quote 2 |
| whether it warns, guards, punishes, teaches or devours | both: man-eaters that captured and ate people, and kaitiaki that protected iwi and hapū, passed with the right karakia and an offering, often a green twig. One dolphin-form taniwha played in the river "to warn its people of an impending invasion". A 1870s account read a drowning as punishment for taking flowers from a sacred rātā tree | NEW-ScoutTaniwha-2 quote 3; NEW-ScoutTaniwha-1 "Whales, dolphins and enchanted logs — Dolphins" and "Freshwater taniwha — Waipapa waterhole" (both on the page, not quoted) |
| who records or depicts it, and in what book or object | Te Ara itself is the modern recording object: a national encyclopedia story, whose own source list names Orbell's *A concise encyclopedia of Māori myth and legend* (1998) and the *Reed book of Māori mythology* (2004 rev. Calman) — the bestiary genre for this tradition. The being is also woven: niho taniwha on tukutuku panels and tāniko cloak hems, and the landing page's main image is Āraiteuru on a New Zealand Post stamp | NEW-ScoutTaniwha-3 quote 4; NEW-ScoutTaniwha-1 "External links and sources" (titles on the page, not opened); landing page main-image caption (not filed as a row) |
| what changes across periods | three kinds of change, all documented: a guardian re-identified across centuries (Kupe's taniwha Tuhirangi with the dolphin Pelorus Jack, and the 1955–56 dolphin Opo "believed by many Māori in the area to be a taniwha"); newspaper debate over what counts (1907 Te Pipiwharauroa on a "taniwha" that was probably a seal, "It is a sacred ‘taniwha’ protected by law"); and modern consent disputes (Karutahi rerouted, Takauere's prison built, with accusations that the objection sought compensation and open disagreement among Māori) | NEW-ScoutTaniwha-1 "Whales, dolphins and enchanted logs — Dolphins", "Is that really a taniwha?", "Taniwha today — Taniwha and identity" |

### The detail most useful to a worldbuilder, and not obvious from the entry's outline

The monster is a party to land-use decisions, and its evidence is a place. Both 2000s cases turn on a lair or a
travel route that a road or a prison would cut: Ngāti Naho said the highway would destroy Karutahi's lair and
Transit New Zealand partially rerouted it; local hapū said the Ngāwhā prison would impede Takauere's
travel and the prison was built anyway. Te Ara then records that "Some people suggested that the objection was an
attempt to get compensation, and that the taniwha could be paid to go away", and that "Even among Māori there was
disagreement as to whether the concerns about taniwha were genuine or not". A bestiary that files the being under
"belief" alone cannot represent this; the entry's decision is whether its monsters hold enforceable place-rights,
and who speaks for them.

### Caveats the L1 should carry into the rows or the entry

- Attribution, not voice: Te Ara is a national encyclopedia summarizing named traditions. Write "Te Ara records"
  or name the hapū and the river; never "Māori believe". The page itself notes that "Although not all Māori believe
  in taniwha, they are still important to many" (landing page).
- The story names its own limits: forms "vary according to different tribal traditions", and the 2000s section
  reports internal disagreement. That is the calibration sentence the entry needs, and it is the reason a
  single-profile bestiary is a design error, not just a simplification.
- Sacred and restricted material: rua taniwha are places people avoided, and the Waipapa waterhole account ties a
  death to taking flowers from a sacred rātā tree. Quote these as the page's account; do not present lairs as
  sites to visit, and do not turn tapu into a game mechanic label.
- No dating: the story gives no date for any tradition. The only dated items are the 1876 Waipapa case, the 1900
  and 1907 newspaper items, 1955–56 (Opo), 2002 (Karutahi) and the early 2000s prison. Do not imply antiquity for
  the rest.
- Tier discipline (QUALITY criterion 6): the Te Ara rows are A for what this encyclopedia reports; the Te Aka row
  is A for the lexicon only. Neither row supports a claim about a living iwi's own current statement, and neither
  is a primary text.
- The story's own source list (Orbell 1998, Reed 2004) is on the page as titles only. Those books were not opened
  here, so no row may cite them, and the entry must not lean on them without a separate opened row.
- Pelorus Jack and Opo are the period-change hinge and are on row 1's page but not among its four quotes; if the
  entry uses them, cite row 1's locators "Whales, dolphins and enchanted logs — Dolphins" and "Is that really a
  taniwha?".

## Registry row tails (paste after the assigned `| SNNN |`)

Field order copied from S277 so the L1 can drop them in; `used-by` is the claim C entry.

```
| Keane, Basil. 2012. "Taniwha", Te Ara – the Encyclopedia of New Zealand, Manatū Taonga Ministry for Culture and Heritage, story published 22 September 2012, full-story print view. — https://teara.govt.nz/en/taniwha/print (direct plain request, HTTP 403 Cloudflare interstitial: challenge met, not passed; opened from the Wayback capture 20260208222348, HTTP 200, text/html, access date 2026-10-22) | web | A | the signed story's account of taniwha forms, waters, lairs, named beings (Tūtaeporoporo, Āraiteuru, Ngārara Huarau, Takere-piripiri, Tuhirangi/Pelorus Jack), slaying methods, and the early-2000s Karutahi and Takauere disputes. (tier note: A — Manatū Taonga's national encyclopedia, signed and dated; authoritative for the summary it gives of named traditions, with every claim attributed to it.) | "What are taniwha? — A creature of many forms": "They hid in lairs known as rua taniwha, which could be deep pools, caves, or dangerous waterways – areas that people avoided."; "Sharks — Tūtaeporoporo": "Then he began to change, with hard, spiky skin, bat-like wings, a lizard-like tail, webbed feet and claws like a hawk’s."; "Taniwha today — Karutahi": "Eventually, Transit New Zealand agreed to partially reroute the highway."; "Taniwha today — Takauere": "Ultimately, against these objections the prison was built." | a signed national encyclopedia account gives taniwha as shape-changing water beings with named lairs, guardian and man-eater roles, composite bodies, and 2000s highway and prison disputes. | mined | 2026-10-22 | 365d | corpus/knowledge/myth-symbol/monsters-hybrid-beings.md |
| Keane, Basil. 2012. "Taniwha – What are taniwha?", Te Ara – the Encyclopedia of New Zealand, page 1 of the story. — https://teara.govt.nz/en/taniwha/page-1 (direct plain request, HTTP 403 Cloudflare interstitial: challenge met, not passed; opened from the Wayback capture 20260921201758, HTTP 200, text/html, access date 2026-10-22) | web | A | the story's definitional page: tribal variation of form, water habitats, rua taniwha as avoided places, the man-eater and kaitiaki split with karakia and offerings at dens, shape-changing, and the Waikato proverb reading taniwha as great chiefs. (tier note: A — same encyclopedia, author and story, separate page URL; authoritative for the terms it sets out and scoped to this page.) | "What are taniwha? — A creature of many forms": "Taniwha are supernatural creatures whose forms and characteristics vary according to different tribal traditions."; same section: "Others refer to them as dragons – many taniwha looked like reptiles, had wings and ate people."; same section: "Others were kaitiaki, or protectors of iwi (tribes) and hapū (sub-tribes)."; same section: "Some taniwha could change their shape, moving between different forms." | the definitional page fixes taniwha as tribally variable, water-dwelling, sometimes shape-changing, split between man-eaters and kaitiaki honoured with karakia and offerings. | mined | 2026-10-22 | 365d | corpus/knowledge/myth-symbol/monsters-hybrid-beings.md |
| Moorfield, John C. Te Aka Māori-English, English-Māori Dictionary and Index, online edition, © 2003–2026 John C Moorfield / Te Murumāra Foundation. Entries "taniwha" (sense 1), "niho taniwha", "taniwha hikuroa", "unuhanga taniwha", "mangō taniwha". — https://maoridictionary.co.nz/search?keywords=taniwha (direct plain request, HTTP 200, text/html, access date 2026-10-22) | web | A | the lexical range of taniwha — water spirit, monster, dangerous water creature, powerful creature, chief, powerful leader, something awesome — with its lake, river and sea habitats and the compounds niho taniwha, taniwha hikuroa, unuhanga taniwha and mangō taniwha. (tier note: A — Moorfield's Māori–English dictionary, authoritative for the glosses and compounds; the 1905 and 1946 Journal of the Polynesian Society examples it quotes would be B as ethnography.) | "taniwha, sense 1": "water spirit, monster, dangerous water creature, powerful creature, chief, powerful leader, something or someone awesome"; same sense: "taniwha take many forms from logs to reptiles and whales and often live in lakes, rivers or the sea."; same sense: "They are often regarded as guardians by the people who live in their territory, but may also have a malign influence on human beings."; "niho taniwha": "The principal motif that represents the realm of mythology and a chief's lineage from the gods." | Te Aka gives the word's range — water spirit, monster, chief, awesome thing — its lake, river and sea habitats, and niho taniwha as a woven descent motif. | mined | 2026-10-22 | 365d | corpus/knowledge/myth-symbol/monsters-hybrid-beings.md |
```

## Not run

No lane command was run: `python3 -B reports/round-55/accept-c.py` measures a state that does not exist yet (the
entry is the L1's to write), and this seat is read-only. No file in the lane was created or modified except this
report. No tool was installed or upgraded; nothing needed one (curl, python3 and the Wayback capture were enough). Tool
note: the Wayback CDX query endpoint answered "Internet Archive: Temporarily Offline" while the availability API
kept answering, so captures were located through the availability API only.

unopened: the live `teara.govt.nz` pages for all three URLs, which returned HTTP 403 with the Cloudflare
"Just a moment..." interstitial to plain requests (challenge met, not passed) and were replaced by the captures
named above; `https://nzhistory.govt.nz/culture/maori-religion` (NZHistory, Manatū Taonga), which returned HTTP 403
with the same interstitial and was not pursued, since the Te Ara story covers the same ground; Te Ara's page 9 URL
`https://teara.govt.nz/en/taniwha/page-9` ("Taniwha today"), for which the Wayback availability API returned no
capture, so it was read only through the print view; the story's own cited books, Orbell 1998 *A concise
encyclopedia of Māori myth and legend* and Reed 2004 *Reed book of Māori mythology* (rev. Calman), listed on the
page as titles only and not opened — they are the obvious next rows for the bestiary thread if a later seat wants
them; the 1907 and 1900 *Te Pipiwharauroa* issues and the 2004 *Critic* article that Te Ara quotes, which are
second-hand inside the row and must not be cited as if opened; and the Waitangi Tribunal or Environment Court
records that would show a taniwha objection argued in a formal proceeding, which were not searched this pass.
