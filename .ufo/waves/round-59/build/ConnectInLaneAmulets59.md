# ConnectInLaneAmulets59 — in-lane partial owners for claim C (amulets, talismans, apotropaic marks)

Axes named: **coverage** (the claim's declared axis) and **adjacency** (the seat's judged axis — that the new entry points one-way at every existing owner and re-claims none of their lines). No scalar is offered; §6 lists the contradictions flat.

Method (this session, base `39c9ce8a`, read-only):

```
grep -rniE 'amulet|talism|apotrop|evil eye|phylacter|mezuz|omamori|ofuda|hamsa|nazar|witch mark|charm' corpus/knowledge
→ 51 hits / 34 files
```

Refinement that matters for every later count: `talism` also matches **capitalism** and **fatalism**, `charm` also matches an aesthetic quality ("narrative charm") and a cake token, and `rue\b` matches **true**. Filtered, the real protective-object content sits in **23 files / 28 lines**; the rest are false friends (§1c). Two further anchors (`architecture-settlement-lexicon.md:125`, `java-majapahit.md:147-148`) came from a separate `threshold|doorway|lintel` sweep and are not in the 51.

---

## 1. What the corpus already says (so the entry does not sell it as new)

### 1a. Direct sentences about protective objects

| Anchor | What it already says | The new entry may NOT say |
|---|---|---|
| `culture-material/adornment-body-codes.md:20` | "Roman *bulla* (freeborn boy's amulet, surrendered at the toga virilis)" inside the **jewelry-as-wealth ledger** | that the amulet is a "rite code" and the bulla its exemplar — the sentence already places it in a three-column ledger (wealth / rite / punishment) | 
| `culture-material/ritual-garments.md:118` | Rome row of the coming-of-age table: "bulla amulet doffed" at the toga virilis | the *lifecycle retirement* of an amulet as dress-rite — the attested doffing is already tabled here (this is the hinge in §7) |
| `myth-symbol/binding-speech-complex.md:164` (§5.2) | the curse's defense half: "*voces magicae* … amulets, apotropaic writing, and threshold deposits (Gager 1992)" | that the amulet is a **curse**-defense; the clause is owned and named |
| `myth-symbol/mineral-stone-symbolism.md:175` (§12) | "Precious stones are universal talismans" — **discredited** as a universal; the lapidary virtue-list is a specific medieval European form | any stone-virtue list presented as a universal property of the material |
| `culture-material/craft-artisan-lexicon.md:99` (§7), `:121` (§9) | "hidden curse-charms chalked into a building" (Lu Ban jing, Ruitenbeek 1993) — hostile writing as architecture | the *hostile* build-mark; craft owns it, and §9 already calls it "apotropaic **or** hostile" |
| `myth-symbol/celestial-symbolism-calendars.md:128` (§7) | eclipse table: "protective amulets (red cloth tied over the womb — attested for Ch'orti' Maya (Hull 2020: 280)…)" | the childbirth-danger amulet in situ; §7 owns the danger class **and** its amulet |
| `myth-symbol/monsters-hybrid-beings.md:97` (§8), `:115` | Pazuzu "set up as a shield against Lamashtu", amoral, appeasable (S304); his image out of use by Parthian times | the demon-image-as-apotropaion; §8 owns it and S304 is already a registered row |
| `civilizations/java-majapahit.md:147-148` (§8) | *kāla* "Fierce mask/face motif often marking an architectural threshold"; *makara* doorway arrangement | the threshold demon-face on a building |
| `culture-material/architecture-settlement-lexicon.md:125` (§7) | "Threshold rites everywhere: genkan shoe-lines, **yingbi spirit-screens**, pomerium furrows" | the spirit-screen as a built protective element |
| `civilizations/israel-ancient-hebrew.md:108` (§6), `:113` | Ketef Hinnom silver amulets: "protective inscriptions containing the divine name and wording related to the priestly blessing"; the Barkay et al. (2004) dating caution | the written-name amulet as a *case*; §6 owns the name-magic matrix (`:117`) |
| `civilizations/egypt-ancient.md:96-97` (§5) | wedjat: "Mythic repair, bodily protection, amulet manufacture"; scarab: "a form of seal/amulet may intersect" + "Not every scarab has one identical use" | what a given sign *means*; §5 owns the sign table |
| `civilizations/amazigh-berber.md:100` | "Hand-shaped pendants, afus / khamsa terminology … not an exclusively Amazigh symbol" | the khamsa's diffusion claim — the caution is already written |
| `civilizations/germanic-norse.md:65` | runic register table row "Protective formula / inscribed amulet — require object-specific evidence; an opaque sequence is not automatically a spell" | that an opaque rune string is a charm |
| `civilizations/china-tang.md:126` (§8) | "Sutra copying, dhāraṇī, and Daoist talismanic practices give writing different ritual functions" | that all Chinese written talismans are one technology |
| `civilizations/japan-medieval-sengoku.md:89` | Shingon row: "icons, talismans, Sanskrit-derived Siddham characters"; guard against "decorative 'magic runes'" | the bonji-on-object claim |
| `culture-material/warrior-material-culture.md:91` (§6), `:110` (§8) | bonji + sutra invocations "lacquered on armor — apotropaic grammar on the body"; renewal of the inscription | worn protective inscription on war gear |
| `culture-material/carthage.md:143` (§8) | "Amulets/small objects in urn processing … a deposition is not a complete outfit" | that grave amulets equal daily wear |
| `culture-material/vessel-container-lexicon.md:90` (§6) | Egyptian faience: "Egyptian amulets and vessels — a different material with a colliding name" | faience as an amulet material-class |
| `myth-symbol/color-symbolism.md:79` (§6) | China's "luck/protective complex": red envelopes, **red string amulets**, red underclothes in the zodiac year | red's protective load |
| `myth-symbol/death-afterlife-eschatology.md:91` (§6) | revenant management: "apotropaic rite, crossroads burial, the bean-throwing" | the apotropaic **rite** class (rite ≠ object) |
| `civilizations/burma.md:72` | Spiro's "nibbanic / kammatic / apotropaic distinctions … influential analytical categories, not three bounded native denominations" | "apotropaic" as a bounded Buddhist denomination |
| `civilizations/rapa-nui.md:161` (§10) | "not every portable carving is an amulet" | any equation of portable image with amulet |
| `civilizations/celts.md:154` | ogham "is an alphabet encoding language, not a collection of pictorial charms" | ogham or La Tène geometry as charm script |
| `civilizations/kongo-kingdom.md:83` (§8) | Bentley: older missionaries' use of *nkisi* for "holy" is "a very objectionable use"; 1887 dictionary glosses *nkixi* as "charm, enchantment, fetish and medicine" | *nkisi* as a synonym for amulet — the word's English glosses are themselves the evidence |
| `civilizations/malagasy-madagascar.md:72` | Richardson's *Andriamanitra* entry "includes sovereigns, charms, and other extraordinary things"; his dismissive language reveals missionary framing | the "charms" gloss as a neutral category |
| `synthesis/era-myth-language-costume-matrix.md:91` (§5), `:183` | Amarna: "non-Atenist amulets/figurines at Amarna complicate universal replacement" | the under-the-radar household-practice argument — §5 owns it |
| `culture-material/cuisine-food-lexicon.md:53` (§3) | "New Orleans king-cake charm" — the hidden-object token | the token/charm-in-food sense (homonym, §1c) |

### 1b. Terminological and translation guards already in place (use them, do not re-derive)

- `kongo-kingdom.md:83` and `malagasy-madagascar.md:72` are the lane's only two worked cases of **"charm" as a missionary gloss**; the new entry's amulet/talisman/charm definition table should cite them rather than invent a fourth treatment.
- `israel-ancient-hebrew.md:31` already carries the evidence-layer guard the entry needs for its own objects: "| Ostraca, seals, amulets | attested spellings, transactions, names, particular ritual uses | population-wide literacy or every wearer's private theology |" — an amulet proves one ritual use, never a population's belief. `:12` shows the lane already knows Barkay et al. (2004, *BASOR* 334) by name, and a case-insensitive search of `corpus/SOURCES.md` for `Barkay` this session returned **nothing** — so that article is an unspent lead, but it must be opened and registered before it can carry a row.
- `rapa-nui.md:161`, `celts.md:154`, `egypt-ancient.md:97`, `amazigh-berber.md:100` supply four independent **over-attribution** guards (portable carving, ogham, scarab, khamsa). Every "type" row in the new entry needs one of these or its own equivalent, or a blind reviewer can flip it on exactly these grounds.

### 1c. False friends (will inflate any keyword count; do not cite)

| Hit | Why it is not amulet content |
|---|---|
| `china-song.md:90,92,196,217`; `timekeeping-instruments.md:5,99`; `persia-sasanian.md:90,200`; `igbo.md:56` | `talism` ⊂ **capitalism / fatalism** |
| `comparative-frameworks.md:93` | "surface narrative **charm**, performance texture" — an aesthetic quality |
| `trickster.md:83` | "Br'er Rabbit as plantation **charm**" — metonym, the Harris frame |
| `cuisine-food-lexicon.md:53` | king-cake **charm** — a hidden token, not an apotropaion |
| `cuisine-food-lexicon.md:83` | `al-aḥkām al-khamsa` = the five **rulings** of Islamic law, not the hand — a keyword search for hamsa/khamsa collides here, so the entry's terminology table must keep the two apart |
| `monsters-hybrid-beings.md:111` | Mami Wata medallion — image recomposition, not protection |

---

## 2. One-way pointer lines the new entry should carry

Format follows the lane's own style (`` see `path` §N ``, as at `myth-symbol/divination-omen-systems.md:102`). **Load-bearing caveat:** nine of the targets below use *unnumbered* `##` headings, so a `§N` pointer would not resolve — for those, use `` `path:line` `` (the convention `heraldry-emblems-identity-marks.md` §2 already uses in its table). Marked ⚠.

### Must carry (7) — direct overlap; without these the entry is a second owner

```
see `myth-symbol/binding-speech-complex.md` §5.2 — the curse-defence half already names amulets, apotropaic writing and threshold deposits as one clause; this entry owns the object those words point at, not the defence.
see `myth-symbol/monsters-hybrid-beings.md` §8 — the demon set up as a shield (Pazuzu against Lamashtu) is a being's function there; this entry borrows the being, never the verdict.
see `myth-symbol/purity-pollution-boundary-systems.md` §4 — pollution travels by contact, ingestion, proximity or the immaterial carrier; this entry owns prevention, that entry owns removal.
see `myth-symbol/sacred-topography-pilgrimage.md` §5 — the votive deposit, the inscribed receipt and the token are the shrine's institutions; this entry keeps only the blessing that makes a sold object protective and its later demotion.
see `myth-symbol/heraldry-emblems-identity-marks.md` §3 — a mark there always names a bearer unit; an apotropaic mark names no bearer, which is the whole difference.
see `myth-symbol/mineral-stone-symbolism.md` §12 — "precious stones are universal talismans" is discredited; the stone list here is a material choice, not a virtue.
see `culture-material/ritual-garments.md` §6 ⚠ (`:114-124`) — the bulla doffed at the toga virilis is the lane's one attested amulet retirement; this entry generalises the term, that entry stages the dress.
```

### Should carry (9) — adjacent, one shared sentence each

```
see `myth-symbol/number-symbolism.md` §5 — the Luoshu 3×3 magic square as China's quincunx arithmetic; this entry uses the square as an inscribed device, not as number doctrine.
see `myth-symbol/death-afterlife-eschatology.md` §7 — grave goods as supply and the counter-flow ledger; an amulet buried with the dead is that entry's deposition question.
see `myth-symbol/ritual-liminality.md` §4 — substitution and the scapegoat; a worn substitute-object inherits that logic.
see `myth-symbol/color-symbolism.md` §6 — red's protective complex (red string, red underclothes in the zodiac year); colour meaning stays there.
see `culture-material/writing-media-surface-economy.md` §2, §6 — the surface inventory and cost ladder, and the medium as legal instrument; which surface an inscription uses, and what that costs, is that entry's.
see `culture-material/adornment-body-codes.md` §2 — the three-column wealth/rite/punishment ledger; an amulet is rite-code and cannot be sold, which is that ledger's rule.
see `culture-material/architecture-settlement-lexicon.md` §7 ⚠ (`:125`) — threshold rites and the yingbi spirit-screen; a threshold *rite* is not yet a threshold *object*, and this entry supplies the object.
see `culture-material/craft-artisan-lexicon.md` §7, §9 — the hidden build-curse chalked into a building; hostile writing stays there.
see `synthesis/era-myth-language-costume-matrix.md` §5 ⚠ (`:91`) — non-Atenist amulets at Amarna as evidence that household practice outlives a reform.
```

### Conditional (4) — cite only if the section is used

```
see `myth-symbol/celestial-symbolism-calendars.md` §7 — the eclipse danger classes and the red cloth tied over the womb; that row already carries an amulet.
see `civilizations/java-majapahit.md` §8 ⚠ (`:147-148`) — kāla/makara at the doorway; the one in-corpus building-threshold figure.
see `culture-material/funerary-material-culture.md` §3 — the grave as a document written by the living; a buried amulet is assemblage evidence.
see `synthesis/symbolism-consistency-rules.md` §10 — the symbol-audit procedure; hand the object grammar to it rather than write a second audit.
```

Header `- couples:` line should name, at minimum: `myth-symbol/binding-speech-complex.md`, `myth-symbol/purity-pollution-boundary-systems.md`, `myth-symbol/sacred-topography-pilgrimage.md`, `myth-symbol/mineral-stone-symbolism.md`, `culture-material/adornment-body-codes.md`, `culture-material/writing-media-surface-economy.md`, `synthesis/symbolism-consistency-rules.md`.

---

## 3. Civilization entries that hold amulet material (and what each may support)

| Entry | Anchor | Amulet material held | Pointer action |
|---|---|---|---|
| `egypt-ancient.md` | `:96-97` (§5) | wedjat + scarab as sign-and-amulet; "amulet manufacture" named | cite for sign→object; access to the sign table stays there |
| `israel-ancient-hebrew.md` | `:108`, `:113` (§6), `:117` | Ketef Hinnom silver amulets; the name-magic design matrix (`written form / permitted spoken form / … / object bearing the name`) | cite for a **written** amulet; the matrix is the best existing template for the entry's inscription section |
| `amazigh-berber.md` | `:100` | hand pendants, afus/khamsa; regional-limits caution (Camps-Fabrer 1991 §§28-29) | cite for a hand-shaped apotropaion; the diffusion caution is already made |
| `germanic-norse.md` | `:65` | inscribed amulet as a **register** in the runic table | cite for the object-specific-evidence rule |
| `china-tang.md` | `:126` (§8) | Daoist talismanic writing, dhāraṇī, sutra copying as distinct ritual technologies | cite for script-as-talisman; no "Chinese runes" |
| `japan-medieval-sengoku.md` | `:89` | Shingon talismans, bonji/Siddham | cite for Buddhist talisman carriers |
| `carthage.md` | `:143` (§8) | amulets in tophet urn processing | cite only for deposition ≠ adornment |
| `rapa-nui.md` | `:161` (§10) | "not every portable carving is an amulet" | cite as the over-attribution guard |
| `celts.md` | `:154` | ogham is not "pictorial charms" | cite as the mark-is-not-charm guard |
| `kongo-kingdom.md` | `:83` (§8), §9 | *nkixi* glossed "charm, enchantment, fetish and medicine"; §9 owns minkisi | cite for the translation trap only — **never** as an amulet row |
| `malagasy-madagascar.md` | `:72` | Richardson's "charms" inside *Andriamanitra*; missionary framing | cite for the gloss politics |
| `burma.md` | `:72` | Spiro's "apotropaic" as an analytic category | cite for the analytic-term caution |
| `java-majapahit.md` | `:147-148` (§8) | kāla/makara at the doorway | cite for building-threshold figures |
| `era-myth-language-costume-matrix.md` | `:91` (§5) | Amarna non-Atenist amulets/figurines | cite for reform-survival |

**Not amulet material** (do not cite): `china-song.md`, `timekeeping-instruments.md`, `persia-sasanian.md`, `igbo.md`, `maori.md` (§1c).

---

## 4. Coverage read — the ground really is uncovered

```
find corpus/knowledge -type f | grep -ciE 'amulet|talism|apotrop|charm|phylact|evil.?eye'  →  0
```

Term-by-term occurrence count over `corpus/knowledge` (files containing the term):

| term | files |
|---|---|
| `evil eye` | **0** |
| `mezuz` | **0** |
| `omamori` | **0** |
| `ofuda` | **0** |
| `nazar` | **0** |
| `phylacter` | **0** (the tefillin are the thing, and only `ritual-garments.md:118` names them) |
| `witch mark` | **0** |
| `tefillin` | 1 (`ritual-garments.md`) |
| `khamsa` | 2, but **only one is the hand**: `amazigh-berber.md:100`; `cuisine-food-lexicon.md:83` is `al-aḥkām al-khamsa`, "the five-rulings ladder (wājib, mandūb, mubāḥ, makrūh, ḥarām)" — a legal five, not the pendant |
| `scarab` | 1 (`egypt-ancient.md`) |

So the entire **evil-eye complex** (nazar, hamsa-as-eye, the eye's *gaze* as a pollution carrier), the **doorpost scroll** (mezuzah), the **Japanese printed talisman** (ofuda/omamori) and the **English building mark** (witch marks) have no owner anywhere in the corpus. `purity-pollution-boundary-systems.md` §4 names "gaze" as an *immaterial carrier* but never develops it. That is the freshest ground the entry can occupy without touching a single existing sentence.

---

## 5. URL collision risk for the S-rows (advisory to the L1 and the scouts)

`corpus/SOURCES.md` holds **525** rows. Host saturation among the museum sources an amulet entry will reach for: `metmuseum.org` 13, `britishmuseum.org` 8, `collections.vam.ac.uk` 7, plus `archive.org` 42 and `web.archive.org` 37. DISTINCT (≥10 hosts) is therefore easy, but per-URL dedup is not: these exact URLs are already spent and a scout offering any of them violates the "do not offer a URL already in SOURCES.md" rule —

- `https://www.metmuseum.org/exhibitions/listings/2014/assyria-to-iberia/blog/posts/pazuzu` (S304; **live returns HTTP 429**, read via capture 20171121161933)
- Met object pages `search/320053` (S395, S400, S486 — Mangaaka nkisi), `search/318318` (S399, S488 — St Anthony staff), `search/312342` (S396, S487 — male nkisi), `search/318324` (S394 — Kongo crucifix)
- `https://prm.web.ox.ac.uk/files/mavungupdf` (S401 — Pitt Rivers Mavungu)
- British Museum `W_1850-1228-2`, `Y_EA29472`, `Y_EA9901-3`, `Y_EA10470-3`, `E_Af1951-04-118`; VAM `O1053476`, `O498858`, `O456793`, `O322757`, `O1314738`, `O1113999`

Also note S395/S400/S486 and S399/S488 are *duplicate catalogues of the same object under different S-ids* — a precedent that the DISTINCT leg tolerates, but it means two rows quoting one object page will not be caught mechanically; a blind reviewer will catch it.

Reserved hosts for this round (`ryedalefolkmuseum.co.uk`, `horniman.ac.uk`, `magnes.berkeley.edu`, `foundlingmuseum.org.uk`, `nationalmuseet.dk`, `coriniummuseum.org`) are exactly the natural homes for witch marks, hamsa, mezuzah and Danish amulet collections — expect scouts to reach for them, and refuse.

---

## 6. Contradictions and risks, stated flat

1. **The strongest boundary is inside a sentence, not between files.** `binding-speech-complex.md:164` already enumerates "amulets, apotropaic writing, and threshold deposits" as one clause. If the new entry announces those three as its subject, it asserts ownership of an existing owner's enumeration. It may own the objects; it may not own the triad.
2. **Pazuzu is doubly claimed and its source is spent.** `monsters-hybrid-beings.md:97` owns the being's function and S304 its page. A new row about Pazuzu would need a different URL *and* would duplicate a claim another entry already carries — the mechanical distinctness leg would pass it, a blind reviewer is likely to fail it. Safest: Pazuzu appears in the new entry only as a pointed citation, never as a row.
3. **The commodification clause collides with `sacred-topography-pilgrimage.md` §5**, which already owns deposit/receipt/token and the badge-as-archaeology argument. Writing a "shrines sold protective tokens" section restates §5 in the abstract. The entry must instead say what §5 does not: who *blesses* the object (the authorisation step) and what happens when the claim lapses (§7).
4. **The word "charm" has three live senses** in the corpus already (aesthetic quality, cake token, metonymic "plantation charm"). An entry whose title uses "charms" without a disambiguation table will read as a fourth and will keep producing the false hits in §1c.
5. **`mineral-stone-symbolism.md:175` pre-disconfirms the most tempting materials section.** Any "stones were thought to…" paragraph must cite that row or it lands a discredited universal.
6. **Adjacency is not measured by `accept-c.py`.** The fifteen legs are mechanical except SUPPORT; a row can pass LOCATE/BOILER/RELEVANCE/TOPIC and still be failed by a reviewer who holds `kongo-kingdom.md` or `monsters-hybrid-beings.md` open beside it. The two highest-risk row families are therefore any nkisi/minkisi row and any Pazuzu row.
7. **Nine files cited in this report have unnumbered headings** — `amazigh-berber.md`, `celts.md`, `malagasy-madagascar.md`, `rapa-nui.md`, `germanic-norse.md`, `burma.md`, `japan-medieval-sengoku.md`, `java-majapahit.md`, `architecture-settlement-lexicon.md` — so a `§N` pointer written against any of them will not resolve. Four of them are §2 pointers (⚠-marked, use `:line`); the other five are already cited by line in §3. `ritual-garments.md` is numbered, but its bulla row is a table cell at `:118`, not a section of its own.

---

## 7. The one bounded move

**Define the object by its term, not its material or its shape.**

Every existing owner in the lane holds one *link* of a chain: a danger (`celestial §7`, `monsters §8`), a carrier (`purity §4`), a material (`mineral §12`, `color §6`), a surface (`writing-media §2`), a maker or shop (`craft §7`, `sacred-topography §5`), a deposition (`funerary §3`, `carthage §8`). Nobody holds the chain, and two links are held by no one at all: **placement** (body / child / threshold / building / animal / vehicle) and **retirement** (what happens when the term expires). The lane's only attested retirement is one table cell — `ritual-garments.md:118`, the bulla doffed at the toga virilis.

So the entry's spine is `danger → carrier → material → placement → authorisation → term → retirement`, and its original contribution is the last two links plus the chain itself. This is compatible with, not rival to, the round's other proposals: it *adds* the axis every scout's material is indexed by (each museum record states a danger and a placement) and it *cedes* every sentence §1a lists.

The non-obvious part is the term. It is what makes the commodification section land without touching `sacred-topography §5`: a protective object is defined by the interval it is licensed to cover (a childhood, a campaign, a pregnancy, a year, a house), and it becomes a **souvenir** precisely when its term is not renewed and its authorisation lapses — the same object, same material, same shape, different claim. That single rule (a) gives "amulet vs talisman vs charm" a workable operational difference that is not a museum-word inventory, (b) explains why the same form is an heirloom in one household and a trinket in the next, and (c) supplies the entry's build order without borrowing any existing section's content.

Risk: "term" is a design rule, not an attested doctrine, so it must be labelled as this entry's own craft instrument (the lane's `DR-` / decision-record convention), never as an ethnographic finding; and any row that would be made to carry the term rule must be dropped, because no quote about a doffing will also state the general rule.

---

## 8. Verification the L1 should run

1. Every pointer resolves: for each `` see `path` §N `` check that `grep -n '^## ' path` contains an `N`; for the four ⚠ targets in §2 (ritual-garments, architecture-settlement-lexicon, era-myth-language-costume-matrix, java-majapahit) check the cited `:line` exists instead. The marks in §2 are already the pass list.
2. Post-landing absence check (the claim's own command): `git ls-tree -r --name-only <rev> corpus/knowledge | grep -ciE 'amulet|talism|apotrop'` must go 0 → 1, and the file set 234 → 235.
3. Re-run §4's term table after landing: `evil eye`, `mezuz`, `omamori`, `ofuda`, `nazar`, `witch mark` should appear in exactly one file — the new one. Any second file means a sibling landed overlapping text and the adjacency line in §2 must be rewritten as a boundary.
4. Before the blind packet is sealed, read any candidate row's quote against `kongo-kingdom.md:83` and `monsters-hybrid-beings.md:97`: if the quote makes the same claim those two make, drop the row rather than defend it.

---

*Seat: ConnectInLaneAmulets59 (leaf; no delegation, no background jobs). Scratch: `/fast/scratch/hyaku/kotodama-r59/ConnectInLaneAmulets59/`. No installs. No writes outside this report file. Base read: `39c9ce8a`.*
