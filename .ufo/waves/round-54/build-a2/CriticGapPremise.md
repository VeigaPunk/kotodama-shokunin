# CriticGapPremise — round 54 attempt 2, claim C premise attack

Seat: KotodamaR54a2.CriticGapPremise (critic, leaf). Date 2026-10-22. Axes judged: coverage, calibration.
Every file below was re-opened this session at the lane working copy (HEAD `7fa37fb`); nothing from attempt-1 scratch is used. Paths are relative to the lane root. Tools installed: none.

## Verdict

**The premise holds, but the gap evidence that supports it has to be corrected.** This is a fixable defect, not a reason to reject the claim. No entry owns masks as a cross-cultural system, so a new entry would not split an existing owner. The claim's gap evidence is narrower than the corpus, though, in three ways:

- It names the wrong partial owners. Two of the three culture-material files it names do not treat masks at all.
- It counts topic-line owners with a regex that misses three civilization entries whose topic lines own mask institutions.
- Its 41-file mention count includes 9 files that use "mask" or "masquerade" only as a metaphor.

This is the same "claim wider than its counting command" pattern that this round was chosen to escape. Here it shows up on the gap side rather than the acceptance side.

## 1. Do the four named files already own masks? Where the line falls

Mask-term counts below come from `grep -ciE '\bmask(s|ed|ing)?\b|masquerade'`.

| File | Mask content (re-read in full or by section) | What it owns that the masks entry must point to, not restate |
|---|---|---|
| `culture-material/ritual-garments.md` (156 lines) | **0 hits.** | Garment-as-office and investiture (`:20`); donning as a rite with fixed order and formula (`:21`); the sensory pole of sacred dress (`:22`); inalienable regalia (`:130`); the confiscated-vestment / U'mista pointer (`:141`). |
| `culture-material/costume-semiotics.md` (149 lines) | **1 hit, a metaphor only** (`:31`, Wilson's "fashion as … mask"). | The legibility dial (`:76-91`); the imposture theorem (`:90`); deniability (`:11`). A mask is the limiting case of the dial, where the wearer's identity is made deliberately unreadable. Cite §6 once; do not rebuild the dial. |
| `culture-material/funerary-material-culture.md` (221 lines) | **0 substantive hits.** Its single hit is a quoted pointer inside the sources ledger at `:12` to `zapotec-mixtec.md:124`. | The assemblage grammar (`:75-86`); the "Figurative substitution" row, "an image does the work the body … did" (`:68`); the grave-résumé rule (`:77`, citing `material-culture-inference-method.md:81`). A mask laid on or deposited with a corpse is an assemblage object, so point to `:68`/`:77`. A mask worn by a *living* performer at a funeral (for example the Roman imagines scout) is masks-entry ground. The funeral schedule, cost and law stay in the funerary entry. Pointer hygiene: the file's H1 and `- gap:` line call it `mortuary-material-culture`, but the file on disk is `funerary-material-culture.md`, so cite the on-disk name. |
| `myth-symbol/ritual-liminality.md` (136 lines) | **5 hits, each a list item:** `:14` (couples), `:22` ("masking" as a liminal-phase trait), `:38` (Turner: neophytes "anonymous (uniform, masking, secrecy)"), `:111` (masks in the liminal-costume list), `:117` (build step: "mask" as a liminal prop). | The van Gennep and Turner grammar; reversal-festival licensing (`:97`). Cite `:22`/`:38` once and do not re-teach the phases. |

**Owners the claim does not name, which carry more mask substance than any of the four:**

- `civilizations/igbo.md`: the topic line owns "mmanwụ costume and restricted associations". §5 (`:94-113`) already states the access-rule method: "ask which association controls membership, making, storage, revelation, appearance, and sanction" (`:97`). It also gives a costume assembly record (`:107`), the point that "Outsiders do not know the performer" and "nobody knows" are different claims (`:110`), and "control revelation through licensing" (`:112`).
- `civilizations/haudenosaunee.md`: the topic line owns "the boundaries around False Face medicine traditions". The section at `:132-143` rests on the Grand Council's 1995 policy (file-local `[S95]`, `:162`).
- `civilizations/hopi.md`: the topic line covers katsina; see `:15`, `:77-79` ("all are masks" is rejected) and `:101`.
- `civilizations/yoruba.md`: the Gelede section (`:120-136`). It separates Gelede from Egungun (`:135`), and `:199` treats UNESCO's matriarchy claim as heritage framing.
- `civilizations/fon-dahomey.md`: Gelede as a neighbouring parallel (`:83-97`).
- `civilizations/siam-thai.md`: the khon section (`:129-147`), including "Mask identity is composite" (`:121`) and teacher masks on altars (`:141`).
- `civilizations/newar-nepal.md`: `:147`, where making, keeping and wearing are different offices.
- `civilizations/pacific-northwest.md`: `:157`, masks as rights (U'mista).
- `civilizations/ancestral-puebloan.md`: `:159`, no "mask construction".
- `civilizations/zapotec-mixtec.md`: `:111`, a mask ensemble "may constitute ritual personification".
- The licensed-voice side:
  - `verification/phonology-sanity-gate.md:241` (mask acoustics are a transmission effect, not a change to the sound inventory);
  - `linguistics/sound-symbolism.md:85` (a dangling pointer to "`culture-material/` masks");
  - `linguistics/linguistic-anthropology.md:147`.
- The licensing logic: `myth-symbol/trickster.md:70` (licensed reversals) and `culture-material/calendar-festival-systems.md:107` (Carnival–Lent).

**Where the line must fall.** The new entry owns only the **cross-cultural method of the worn mask as an institution**:

- (a) how the mask complex breaks down into object, ensemble, performer, manifested presence and custodian institution;
- (b) a typology of access rules: who may make, keep, wear, see, touch, name and unmask;
- (c) the licensed voice: what the masked figure may say that its wearer may not;
- (d) the four occasions (ritual, funerary procession, theatrical, festival) as design choices;
- (e) retirement, which covers storage, destruction, sale and repair.

Every single-tradition register stays with its civilization owner and gets a one-line pointer.

Counterexample to "uncovered in substance": `igbo.md:97,107,110-112` and `newar-nepal.md:147` already give a generic design method in their own words. The new entry is new coverage only if it **generalizes across at least three unrelated traditions with sources opened this round**. Re-deriving Igbo rules with new S-ids does not count.

## 2. Does the entry fit PROVINCE.md, or does it drift?

The entry fits PROVINCE `:4-5` ("costume & material-culture terminology", "mythic and symbolic systems"). The mask is a worn object, and the presence it makes is a symbol system. The linguistic coupling (terms such as persona and prosopon, and licensed voice) is lane-native.

The drift risks follow the wave-2 scout roster:

- **Theatre studies.** Noh, Commedia, Venice, Talchum, Kolam, European carnival and Mummering scouts could pull in acting technique, dramaturgy and stage history. The test: each of their sentences must end in a worldbuilder decision (who may wear it, what it licenses, what it costs), not in how an actor performs.
- **Art history and museum cataloguing.** The Mexica mosaic and ancient death-mask scouts could pull in style attribution, workshop connoisseurship and authenticity debates. Use them only for the object facts the holding museum records.
- **Museum policy and repatriation law.** The Haudenosaunee, Kwakwaka'wakw and Yup'ik scouts sit next to it. PROVINCE `:18` refuses "real-world rights/attribution rulings", and `:25` says "Contested scope → report … never absorb". The entry may carry a community's own statement as a design constraint ("this form has named custodians who oppose its depiction"). It must not rule on ownership, repatriation or legality.

## 3. Traditions to treat only through the community's own public statements

**Where these traditions are concerned, the community statement overrides the assignment's general preference for museum records.** A holding museum's record of a restricted object is not a community statement. For the first two rows below, the community's own policy opposes depiction, so citing a catalogue description or image would breach the policy.

| Tradition | Community or custodian public statement | In-corpus anchor | Entry may carry |
|---|---|---|---|
| Haudenosaunee medicine masks (wooden and cornhusk) | Grand Council of the Haudenosaunee, 1995 policy (Tadadaho Leon Shenandoah) | `haudenosaunee.md:132-143,162` | Only the policy's own stated points: who holds authority, sacred regardless of size or age, opposition to exhibition, images and replicas. No features, materials beyond the policy's words, or occasions. Cite no museum records. |
| Hopi katsinam | Hopi Cultural Preservation Office | `hopi.md:13-15,77-79` | Only the stated harm of unauthorized publication. No mask patterns or calendar detail beyond the civilization entry. Cite no museum records. |
| Keresan, Zuni and other Pueblo ceremonial regalia | Community-authorized sources only | `ancestral-puebloan.md:101,159` | A pointer only. |
| Kwakwaka'wakw masks as hereditary privileges | U'mista Cultural Centre's own pages | `pacific-northwest.md:157`; `ritual-liminality.md:49` | Masks as rights, and the confiscation and return history as U'mista tells it. No Hamatsa or other ceremony content. |
| Yup'ik masks | Yup'ik-voiced or community-curated publications only. **[INFERENCE]** Which such sources exist is the scout's job. | — | Retirement and making as the community describes them. |
| Igbo mmanwụ | Igbo-authored and community accounts. UNESCO Ijele is a state-party framing (`igbo.md:192`). | `igbo.md:96-112` | A pointer. The performer's identity is restricted knowledge and must not be "revealed". |
| Yoruba Egungun | Practitioner and community accounts | `yoruba.md:135` (distinguished from Gelede) | No unmasking or contact detail beyond a public statement. **[INFERENCE]** The scout must source any restriction it states. |
| Chewa Nyau / Gule Wamkulu | The UNESCO nomination is the public frame | — | No initiation content. |
| Mende and other Sande sowei (a women's society) | Sande members' or community public statements | — | Museum records support object data only, never what happens in the society. |
| Tibetan cham | Monastic public statements | — | Public performance only; no esoteric (tantric) liturgy. |
| Newar Navadurga (Nine Durgas) | Custodial guthi or community accounts | `newar-nepal.md:142,147` | A pointer. |
| New Ireland malagan | Clan rights to designs, as the community states them. **[INFERENCE]** | — | Rights and retirement logic only. |
| Thai khon teacher (rishi) masks | — | `siam-thai.md:141` | Handling status only, by pointer. |

## 4. What would make "230" hollow

Each item below lets `accept-c.py` exit 0 while the coverage is empty.

- **H1. The floor counts IDs, not load.** FLOOR is `len(set(re.findall(r"\bS\d{3}\b", text))) >= 20` (`accept-c.py:81,91`). Twenty rows that each feed one exemplar cell make a gazetteer, not a method.
- **H2. No leg checks tier.** QUALITY (`corpus/QUALITY.md:25-27`) says a tier-C row "is a lead, never sole support". Twenty tier-B or tier-C rows still pass.
- **H3. UNESCO rows scoped as tier A for history.** The corpus already rejects UNESCO's origin and era framings (`igbo.md:192`, `yoruba.md:199`, `siam-thai.md:23`). A UNESCO row is tier A only for what the inscription or state party says.
- **H4. Museum records scoped as tier A for meaning or use.** They are tier A only for object data: accession number, materials and catalogued date. `igbo.md:108-109` gives the precedent: conservation "cannot confirm" the dance.
- **H5. Duplicate authority.** The best mask sources are already cited under file-local IDs in civilization entries:
  - UNESCO Gelede 00002 (`yoruba.md:25`, `fon-dahomey.md:184`);
  - UNESCO Ijele 00194 (`igbo.md:13`);
  - UNESCO Khon 01385 (`siam-thai.md:23`);
  - the NativeTech copy of the 1995 policy (`haudenosaunee.md:162`).

  `SOURCES.md` has no row for any of them (I grepped for unesco, nativetech, umista, teak.fi, seasite and Ijele). A new S2xx row for the same document is allowed, but the entry must not read it differently from the civilization entry's calibration without saying so.
- **H6. The "uncovered" claim rests on a narrow regex.** `grep -rlE '^- topic:.*(mask|masquerad)'` finds 1 file. The topic lines of `igbo.md`, `haudenosaunee.md` and `hopi.md` own mask institutions without using the word "mask".
- **H7. The 41-file mention count is inflated.** 9 of the 41 files use the word only as a metaphor:
  - `burma.md:180`, `byzantium.md:123`, `china-qing.md:117`;
  - `cuisine-food-lexicon.md:13,123,153`, `vessel-container-lexicon.md:52`, `costume-semiotics.md:31`;
  - `sacred-kingship-mythic-charter.md:12`, `deity-name-derivation-pipeline.md:179`, `dialect-faction-map-workflow.md:42`.

  Roughly 6 more files mention masks only in a couples line or pointer. That leaves about 26 files with substantive treatment.
- **H8. Category errors that pad the type list.** `china-shang-zhou.md:95-99` (the tāotiè "animal-mask" bronze ornament) and `java-majapahit.md:147` (the kāla threshold face) are mask *motifs*, not worn masks. `scythian-saka.md:125` (funeral horse masking) is not a human mask.
- **H9. No leg checks the line cap.** The 230-line cap is in the assignment, not in `claims.json`. A 400-line entry passes, and so does an entry whose length is mostly a sources header (as in `funerary-material-culture.md:2-40`).
- **H10. Calibration traps that would launder folk claims.** These are **[INFERENCE]** from prior knowledge; scouts must open sources before the entry states any of them.
  - "persona < per-sonare, 'to sound through'" is the Gavius Bassus derivation reported by Aulus Gellius 5.7, and is contested against an Etruscan *φersu* origin.
  - The "Mask of Agamemnon" is Schliemann's name for it, and its attribution is disputed.
  - The modern Venice carnival is a late-20th-century revival; compare `ritual-liminality.md:82`, which already says modern carnivals are 19th–20th-century stagings.
  - These universals are already rejected in the corpus: "mask ⇒ shaman or trance" (`nazca.md:75`), "every mask is ancestor worship" (`yoruba.md:200`), "secret society" as a precise label (`igbo.md:97`), and "all katsinam are masks" (`hopi.md:79`).

## Must-not list for the L1 and wave 2

1. Must not describe the features, materials, carving or occasions of Haudenosaunee medicine masks or Hopi katsinam beyond the custodians' own published words. Must not cite any museum record, image or replica of them.
2. Must not cite a museum record as support for a restricted tradition's meaning, use or performance; object data only.
3. Must not restate a civilization owner's register: mmanwụ, Gelede, khon, False Face, katsina, Navadurga, Kwakwaka'wakw privileges. Give each one line with a `civilizations/<file>.md:<line>` pointer.
4. Must not re-teach van Gennep or Turner (`ritual-liminality.md:20-44`), the legibility dial (`costume-semiotics.md:76-91`), vesting and donning (`ritual-garments.md:20-21`), or the assemblage grammar (`funerary-material-culture.md:75-86`).
5. Must not present the six-control access frame of `igbo.md:97` as new without citing it as in-corpus precedent.
6. Must not rule on repatriation, ownership, legality or "rightful" custody (PROVINCE `:18`). A community's own statement may be quoted as a design constraint.
7. Must not give acting, carving, making or choreography instructions (theatre and craft drift; also `ancestral-puebloan.md:159`).
8. Must not reveal or speculate on a masked performer's identity or on initiation content (mmanwụ, Egungun, Nyau, Sande, cham).
9. Must not scope a UNESCO row as tier A for dates, origins or "ancient" continuity, and must not let a tier-C row stand as a sentence's sole support.
10. Must not count motifs (tāotiè, kāla) or animal masking as worn human masks.
11. Must not state the per-sonare etymology, the Agamemnon attribution, or a carnival's antiquity without a contested or dated flag and an opened source.
12. Must not repeat the claim's "1 topic-line owner" and "41 passing mentions" in the entry's `- gap:` line without the corrections in §1 and H6–H7.
13. Must not edit `linguistics/sound-symbolism.md:85` to resolve its dangling pointer. It is outside claim C's three lands, and the pointers must stay one-way.
14. Must not exceed 230 lines, even though no leg checks it.
15. Must not use exoticizing framing ("primitive", "tribal", "mysterious", "pagan rite"), and must not call a living practice a relic or "mere theatre" (`igbo.md:113`).

## Concrete falsifiers for wave 2 (run on the integrated tip, from the lane root)

`E` stands for `corpus/knowledge/culture-material/masks-masquerade.md`.

- **F1, gazetteer test.** For each cited ID, count the lines that cite it: `for s in $(grep -oE '\bS[0-9]{3}\b' E | sort -u); do echo "$s $(grep -c "$s" E)"; done`. If more than 10 of the IDs are cited exactly once, and only in table exemplar cells, the entry is a gazetteer and the coverage claim fails review.
- **F2, method test.** The entry must have at least one decision table or checklist (QUALITY 4) whose rows are access-rule types (make, keep, wear, see, touch, name, unmask, retire). Each row must be sourced from at least 3 unrelated traditions. Fewer than that means the entry is not cross-cultural.
- **F3, restatement test.** `grep -nE 'mmanw|Gelede|Gẹ̀lẹ̀dẹ́|False Face|medicine mask|katsin|kachina|khon|Navadurga|Nine Durgas|Hamatsa' E`. Each tradition may appear on at most 2 lines, and each of those lines must contain its `civilizations/<file>.md:` pointer.
- **F4, restricted-description test.** Run `grep -nE 'False Face|medicine mask|katsin|kachina' E | grep -iE 'colou?r|eye|mouth|nose|carv|wood|hair|feature|husk|paint'`. Expected result: zero lines, except a verbatim policy quote with a locator.
- **F5, tier test.** For each cited row, read the tier cell (`corpus/SOURCES.md` column 4). Any entry sentence whose only citations are tier C fails. Any UNESCO or museum row tiered A must have a scope cell limited to the inscription or object data.
- **F6, history-from-heritage test.** `grep -niE 'ancient|pre-?colonial|pre-?Hispanic|immemorial|origin' E`. Each hit must cite a non-UNESCO row or carry `(to-verify)`.
- **F7, gap-line test.** The entry's `- gap:` line must name `igbo.md`, `haudenosaunee.md` and `hopi.md` as topic-line owners and the §1 section owners. It must not say "1 topic-line owner" unqualified.
- **F8, size test.** `wc -l E` must be 230 or less.
- **F9, province test.** `grep -niE 'repatriat|rightful|stolen|illegal|legal title|should be returned' E`. Each hit must be a quoted community statement with a locator, never the entry's own ruling. Also `grep -niE 'how to (carve|make|perform)|step [0-9].*(carv|paint)' E` must return zero.
- **F10, pointer test.** The `- couples:` targets must resolve on disk and must include:
  - `ritual-liminality.md` (`:22`/`:38`);
  - `costume-semiotics.md` §6;
  - `funerary-material-culture.md` (`:68`/`:77`);
  - `ritual-garments.md` (`:20-21`);
  - `phonology-sanity-gate.md:241`;
  - `sound-symbolism.md:85`;
  - `trickster.md:70`.

  Every `path:line` must land on the line quoted. Re-grep each one.
- **F11, lands test.** `git diff --name-only 7fa37fb..<tip> -- corpus/` must be a subset of {E, `corpus/README.md`, `corpus/SOURCES.md`} plus the lesson records listed in `claims.json` `records_not_claims`.
- **F12, quote-discipline test.** Every new row's Gate quotes must be 25 words or fewer, must not join fragments, and must have a locator. A Wayback route used after a challenge must say "challenge met, not passed" (QUALITY 10). ACCESS reads only marker words, so a reviewer must re-open a sample.

## Unrun checks

- I did not open any external source. Scouting is out of scope for this seat, so every **[INFERENCE]** item above (the persona and Agamemnon calibrations, Venice revival dates, the Yup'ik, malagan and Egungun custodial statements) needs a scout-opened source before it is used or stated.
- I did not run `accept-c.py`, `sweep.py` or `check-source-access.py`. The seat is a critic, and there is no landed entry to measure yet.
