# ReviewSec05 — falsify seat report on §5 "Herd lexicon and ownership marks"

**Seat:** `KotodamaR50-2.ReviewSec05-21` (leaf reviewer; no delegation, no background jobs, no swarm).
**Target:** `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` (`corpus/knowledge/culture-material/pastoralism-animal-husbandry.md`), base `4ad26836552462d28a946ca3b067cab0b5ce3532`.
**Method:** read-only. All landed bytes were taken from a private clone (`git clone --shared` → `/tmp/r50sec05-4180537`, checked out at `1c779e4`), never from the lane working tree. The clone was deleted after the run.
**Scope:** §5 (lines 69–81) — herd lexicon and ownership marks — plus the in-corpus `path:line` anchors and S-ids the entry uses in that section, and the calibration/canon status of that section's claims.

---

## 0. Answer summary

**Verdict on the attacked item (§5 + its anchors + its S-ids): PARTIAL.**

Every in-corpus `path:line` anchor the entry cites, in §5 and elsewhere, resolves at `1c779e4` to a real file and a real line, and every one of those lines supports the sentence that cites it. Every S-id in §5 (`S052`, `S059`, `S060`, `S065`) resolves to a `corpus/SOURCES.md` row whose scope covers the claim, and every one of those rows names this entry in `used-by`. The section's decision table is a usable conlang instrument, the S052/S060/S065 rows are honestly quoted, and §5 leaks no canon.

Three defects, all inside §5, hold the section at PARTIAL:

- **F1 (P1)** — §5 line 79: the *Livestock → wealth* row prints a **change-path** design rule whose "Livestock" half no registered row supports. The row is titled "Livestock → wealth" and glosses PIE `*peku-` as "wealth, movable property" (S065) — but AHD's `*peku-` entry contains the string "livestock" **zero times** (it glosses *wealth*, *movable property*, and the Latin reflexes `pecūnia` "property, wealth" / `pecūlium` "riches in cattle"). The "livestock" sense belongs to Pokorny/Wiktionary, which are unregistered and unreferenced. So the row asserts a livestock→wealth direction on the authority of a row that carries no livestock sense.
- **F2 (P1)** — §5 line 77: the *Ownership mark* row's design rule ("mark = lineage + cut + side; a mark change is a dated event") is residue from **Baroin 2010** (Menabe ear-cuts: right ear patrilineal, left matrilineal; Fulani marks "switched after misfortune"), a source opened in the build wave and **never registered**: `grep -c Baroin corpus/` → 0, absent from `SOURCES.md` and from the round-50 search log's "Opened but not registered" list. The rule is also stronger than its cited row S059 supports: S059 says an earmark *names the owner*, is *personal* and *registered for one sameby*, not lineage-coded.
- **F3 (P2)** — §5 line 75: the *Colour × distribution* row presents the quote `"its colours and the way in which they are distributed on its body"` as the claim's warrant. The located source sentence is *"In naming a Nuer cow one has to notice its colours and the way in which they are distributed on its body."* The entry's fragment drops the source's own epistemic verb ("one has to notice"), so the quotation attributes to the Nuer a statement the source makes about the ethnographer's act of noticing. Honest as a fragment, overclaiming as a warrant.

A fourth, whole-entry finding (**F4**, P2) falls just outside §5 but bears on it: the head's *In-corpus anchors* list advertises five line-ranges (`:117`, `:137-146`, `:170-172` of `hunting-foraging-subsistence.md`; `:80` of `agrarian-field-system-lexicon.md`) that **no sentence in the body cites**. §5 is unaffected (all three of its in-corpus anchors are cited), but the head claims a provenance it does not use.

No canon defect was found anywhere in §5 (§5 contains no world-fact; the section is method and design rule). Detail and smallest fixes below.

---

## 1. What was verified as holding (so the reader can discount the findings)

### 1.1 §5's own table, cell by cell

Landed bytes — `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:73-79`:

```
73	| Dimension | Attested pattern | Conlang design rule |
74	|---|---|---|
75	| Colour × distribution | Nuer cow names follow "its colours and the way in which they are distributed on its body" (S052, ch. I §VIII) | base colour roots + a placement affix set, not a flat list |
76	| Age × sex | Nuer separate bull, cow, ox, heifer and calf terms (S052) | an age × sex grid of prefixes |
77	| Ownership mark | a Sámi earmark is a combination of cuts in both ears and names the owner (S059) | mark = lineage + cut + side; a mark change is a dated event |
78	| Species set | "five snouts" as one collective term (S060) | one collective noun; species stay separate roots |
79	| Livestock → wealth | PIE *peku- glossed "wealth, movable property" (S065); Latin *pecūnia* (`trade-economy-lexicon.md:69`) | model as a documented change path; never print the root as settled social history |
```

**Row 76 (Age × sex)** — S052's scope (`corpus/SOURCES.md:81`) is *"Evans-Pritchard's own 1940 assertions about Nuer cattle idiom and cattle naming"* and its `teaches` cell carries *"age/sex cattle terms"*. The build seat's own located page list (`.ufo/waves/round-50/build/SrcEvansPritchard.md:103`) gives the seven Nuer terms the row generalises — `tut` bull, `yang` cow, `thak` ox, `nac` heifer, `ruath` male calf, `dou` female calf, `kol` calf not yet grazing — with the composition rule *base colour × distribution term × horn shape/ear cut × sex/age prefix*. The landed row's "an age × sex grid of prefixes" is exactly that rule, correctly scoped to one 1940 ethnography, and §13 line 186 already carries the `B` status for the companion Nuer claim. **HOLDS.**

**Row 78 (Species set)** — S060 (`corpus/SOURCES.md:89`) `teaches`: *"the five snouts as an emic portfolio term"*, anchored at §2 Bayankhongor province ¶2. The landed row's design rule ("one collective noun; species stay separate roots") is a method prescription and does not overreach the row's own scope. **HOLDS** (with one cross-seat caveat recorded in §4 below).

**Row 79, second half** — `trade-economy-lexicon.md:69` reads in full: `| fee, pecuniary | Gmc \**fehu*, Lat. *pecūnia* < *pecus* 'cattle' | PIE \**peḳu-* 'movable wealth = cattle' (Watkins); cf. Nuer cattle as the idiom of all value (Evans-Pritchard 1940) |`. The Latin reflex the row prints (`*pecūnia*`) is on that line; the corpus row's own design guidance ("wealth counted by heads", row 70) is consistent. **HOLDS** as a citation.

### 1.2 §5's in-corpus anchors all resolve and all support their sentence

Resolution run over the landed tree (every `path:line` pair in the entry, 29 unique anchors, all inside `corpus/knowledge/`):

| anchor | landed file | line content | supports §5's use? |
|---|---|---|---|
| `semantic-fields-lexicon-building.md:70` | `corpus/knowledge/linguistics/semantic-fields-lexicon-building.md:70` | *"Pastoral wealth vocabulary (herd-age, herd-color, herd-condition terms) indexes property systems; reconstructable PIE horse/wheel/pastoral vocabulary mapped against archaeology is the model case"* | **Yes** — §5's master claim ("A herd vocabulary is a property index") is exactly this line's "indexes property systems" |
| `trade-economy-lexicon.md:69` | `corpus/knowledge/culture-material/trade-economy-lexicon.md:69` | the fee/pecuniary row quoted above | **Yes** for `*pecūnia*`; see F1 for the *livestock* half |

Both are inside §5 (lines 71 and 79). Every other in-corpus anchor the entry uses elsewhere also resolves to a live line whose content matches the citing sentence — `hunting-foraging-subsistence.md:27` (the "not 'people who lack farming'" register sentence), `:36` (the wild-source test, "not planted, herded or owned"), `:195` (the living-practice flag); `agrarian-field-system-lexicon.md:62` (the agropastoral row); `cuisine-food-lexicon.md:86` (the three rival taboo explanations incl. Harris's cattle economy); `trade-economy-lexicon.md:69`; `fire-fuel-light.md:37` (dung-as-fuel vs manure); `textile-technology.md:27` (wool as the fork); `transport-mobility-lexicon.md:95` (the draught row); `semantic-fields-lexicon-building.md:105` (the steppe-pastoral field bundle); `animal-symbolism.md:73` (Nuer "cattle of money") and `:110` (the faunal-economy idiom line); `symbolism-synthesis-method.md:69` ("an animal taboo implies a rite"); `sacred-kingship-mythic-charter.md:65` (the ruler as shepherd); `ritual-liminality.md:63` (calendrical/maintenance rites); `celestial-symbolism-calendars.md:28` ("pastoralists on milky/river figures"); `mongol.md:40` ("not a ladder from 'primitive nomad' to 'civilization'"); `turkic-steppe.md:148` (not isolation), `:193` (chronicle bias), `:194` (reject the ladder); `scythian-saka.md:70` (pastoralism ≠ absence of farming); `finnic-sami.md:140` (do not map herding status onto Sámi identity), `:150` (pastoralism has a history, not the eternal condition); `dine-navajo.md:125`; `inca.md:128` ("all wool, all alpaca" is too simple); `calibration-registry.md:35-39` (the R/C/B/H/T code table) and `:142` (the stage-ladder row); `writing-media-surface-economy.md:3` (the "sherd" non-owner). No dangling anchor, no anchor whose line contradicts its citation.

The 21 corpus files the entry cites are **byte-identical between base `4ad2683` and landed `1c779e4`** (`git diff --stat` over the explicit file list → no output), so every `path:line` in the head's anchor list still resolves at the landed commit. No line drift.

### 1.3 §5's S-ids resolve, are scoped, and are mined against this entry

All 22 S-ids the entry cites (S048–S069) resolve to `corpus/SOURCES.md` rows, and every row's `used-by` names this entry:

```
$ awk -F'|' '/^\| S0(4[89]|5[0-9]|6[0-9]) / {gsub(/^ +| +$/,"",$2); gsub(/^ +| +$/,"",$12); print $2, "->", $12}' corpus/SOURCES.md
 S048 -> corpus/knowledge/culture-material/pastoralism-animal-husbandry.md
 ... (22 rows, all identical) ...
 S069 -> corpus/knowledge/culture-material/pastoralism-animal-husbandry.md
```

This satisfies claim C's acceptance clause *"every cited S-id resolves to a SOURCES row whose used-by names the entry"* (`reports/round-50/claims.json:17`).

### 1.4 §5 leaks no canon

§5 contains no statement about any world. Its rows are method and design rule; §12 is labelled `**NON-CANON.**` (line 169) and §15 (line 199) hands *"which herds, routes, marks, raids and rites exist in a world"* to lore-shokunin. QUALITY criterion 5 is satisfied for §5, and the §5 handoff to lore is consistent with the `- couples:` line (line 8: *"lore-shokunin (canon: which herds, routes, marks and raids exist in-world)"*).

---

## 2. Findings

### F1 — P1 · §5 line 79 · the "Livestock → wealth" row's direction is not carried by its cited row

**Where:** `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:79` (and the row title "Livestock → wealth").

**The claim as landed:**

> `| Livestock → wealth | PIE *peku- glossed "wealth, movable property" (S065); Latin *pecūnia* (`trade-economy-lexicon.md:69`) | model as a documented change path; never print the root as settled social history |`

**Evidence — the cited row does not carry the livestock sense.** S065 (`corpus/SOURCES.md:94`) is scoped *"the dictionary gloss of PIE *peku- and its Latin reflexes; lexical derivation only, never PIE social history"*, tier **B**, anchored at *"entry *peku-, headword gloss"*. The build seat's own located quote (`.ufo/waves/round-50/build/SrcPeku.md:51`) is the whole of what AHD gives:

```
Wealth, movable property. Oldest form *pek̑u‑, becoming *peku‑ in centum languages.
```

and the second located quote (`:58`) is the Latin reflex list — `pecūnia` "property, wealth", `pecūlium` "riches in cattle, private property". The sibling re-open seat measured the page directly and reports the string count as zero:

> `.ufo/waves/round-50/falsify/ReopenS065.md`: *"It contains **zero** occurrences of the string 'livestock' (`grep -o -i 'livestock' ahd.html | wc -l` → `0`) and no statement about herding, PIE society, archaeology or dating."*

So AHD supports *wealth / movable property* and the Latin reflexes. It supports no **livestock** sense, and therefore no **livestock → wealth** direction. The livestock sense of the root is AHD-absent and, in the build wave, was carried by other sources: the §5 scribe seat's draft row read *"PIE *peḱu- 'livestock, domestic animals' → Latin *pecūnia*"* attributed to `[SRC: WIKT-PECUS, lead]` — Wiktionary, which that seat itself classed **tier C, "lead only, never sole support"** (`.ufo/waves/round-50/build/ScribeSec05Lexicon.md:43`) — and by the Pokorny index `[SRC: LRC-POK]`, tier B for headword only (`:42`). Neither became a `SOURCES.md` row; neither appears in the round-50 search log's "Opened but not registered" list (`corpus/SOURCES.md:142`). And the S065 row's own `teaches` cell says only *"livestock/movable-wealth gloss; Latin pecūnia and pecūlium"* — the "livestock" half of that cell is the row's summary of what the *dictionary* teaches, while the dictionary's own headword gloss (the row's stated anchor) is "Wealth, movable property."

The row's *design rule* — "model as a documented change path" — is therefore a rule about a path whose **livestock end-point is undocumented in the registry**. The row is honest that the root is not settled social history ("never print the root as settled social history"), but it is not honest that the livestock leg of the path is documented at all.

**Note on the corpus anchor.** `trade-economy-lexicon.md:69` does print `PIE \**peḳu-* 'movable wealth = cattle' (Watkins)` — but that is *in-corpus*, in a row whose `used-by` set is unchanged, and it is the **corpus's** claim, not a source the entry may lean on as its warrant. It is also Watkins, an unattributed gloss with **no `(to-verify)` marker anywhere in that file** (`grep -c "to-verify" corpus/knowledge/culture-material/trade-economy-lexicon.md` → **0**), even though the §5 scribe seat recorded it as *"that row's Watkins gloss is `(to-verify)`; this seat did not open Watkins"* (`.ufo/waves/round-50/build/ScribeSec05Lexicon.md:57`). The entry cites `:69` for `*pecūnia*` (fine); the row's *title* leans on the livestock sense (not fine).

**Smallest fix (author-lane advice, two words + a scope cell):**
- Retitle the row to remove the unsupported direction, e.g. `| Movable wealth → money | ... |` or keep "Livestock → wealth" only if the livestock sense is sourced; **and**
- amend S065's `teaches` cell to `"movable-wealth gloss (no livestock sense on the page); Latin pecūnia and pecūlium"`. Since `SOURCES.md` is append-only for `scope`/`anchor`/`teaches` (`corpus/SOURCES.md:9-13`; only `status`, `recheck`, `used-by` change in place), the correct instrument is a **superseding row** (a new `S0NN` whose `teaches` opens `supersedes S065 —`), logged old→new in `corpus/lessons/round-50.md` per the round's own log convention (`corpus/lessons/round-50.md:56-62`). If the author prefers the minimal change inside claim C's lands, retitling the row and adding "the livestock sense is not on the cited page" to the row's design-rule cell is sufficient and touches no registry cell.

### F2 — P1 · §5 line 77 · the ownership-mark design rule is unregistered-source residue and outruns its cited row

**Where:** `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:77`.

**The claim as landed:**

> `| Ownership mark | a Sámi earmark is a combination of cuts in both ears and names the owner (S059) | mark = lineage + cut + side; a mark change is a dated event |`

**Evidence — the design rule is Baroin 2010, and Baroin is not a registered row.** The §5 scribe seat's draft row (`.ufo/waves/round-50/build/ScribeSec05Lexicon.md:17`) read:

```
| Ownership mark | Menabe ear-cuts: right ear patrilineal, left matrilineal [SRC: BAROIN2010]; Fulani ear-marks cut in ritual, switched after misfortune [SRC: BAROIN2010] | Mark = lineage name + cut shape + side; a mark change is a dated event |
```

The landed design-rule cell is that draft's design-rule cell almost verbatim — *"mark = lineage + cut + side; a mark change is a dated event"* — while its **attested-pattern cell was swapped** to the Sámi earmark (S059). The Baroin material survives only in the design rule.

Baroin 2010 (*"Livestock property marks in Africa"*, in Evans/Yatsenko/Perrin, *Traditional Marking Systems*) was opened in the build wave and quoted with page locators (`.ufo/waves/round-50/build/ScribeSec05Lexicon.md:41`: *"Marks on the right ear refer to the owner's patrilineal affiliation, and marks on the left ear to his matrilineal ties"*; *"a mark is not an individual's, but a primary patrilineage's property"*; *"It usually does not indicate who is the precise owner of the marked animal"*), but it was **never registered**:

```
$ grep -rc "Baroin" corpus/ | grep -v ":0"      # → no output
$ grep -c "Baroin" corpus/SOURCES.md            # → 0
$ grep -c "Baroin" corpus/lessons/round-50.md    # → 0
```

It is also absent from the round-50 search log's "Opened but not registered" list (`corpus/SOURCES.md:142`), which names 17 dropped leads (Dyson-Hudson, Herskovits, Galaty & Johnson, Khazanov 1994, Barfield, FAO newsroom, Sametinget companions, Morello & Rizk, Ostrom 1990, Marett, Goody & Tambiah, Kozuh, Hammurabi, O'Hare, Samec, Bello-Bravo). **Baroin is not on that list either.** So the rule rests on a source the registry never recorded — no S-id, no tier, no scope, no anchor, no lead entry. Under QUALITY criterion 1 (*"every factual claim carries a cited, checkable source"*) the design rule is unsupported.

**The rule also contradicts the row it cites.** S059 (`corpus/SOURCES.md:88`) is scoped *"the **Swedish** earmark institution as stated by the agency that keeps the register; **not Norwegian law**"*, tier A, anchored at *"page Renmärken (H1), opening paragraph"*. Its `teaches` cell: *"an earmark is a combination of cuts in both ears that names the owner; personal, usually inherited, registered for one sameby; unmarked reindeer are the sameby's collective property"*. The opened page says the mark *"talar om vem som äger renen"* — **it names the owner** — and that it is *"mycket personligt"*, *"går vanligtvis i arv inom släkten"*, *"registrerat för användning inom viss sameby"*. S059 supports **owner-named, personal, sameby-registered**. It does **not** support "lineage": a mark that names an owner is the opposite of a lineage code, and the one source that does describe lineage-coded marks (Baroin's Menabe: right ear patrilineal / left ear matrilineal) is unregistered. The design rule's "side" element is likewise Baroin-only; S059's page describes cuts in *both* ears ("kombinationen av snitt på både höger och vänster öra"), not side-coding.

**Two narrower defects in the same cell:**
- **"a mark change is a dated event"** — Baroin's *"switched after misfortune"* (Fulani) and Baroin's *"marking is a social signal, a form of message"*. S059 has no such claim; the Sametinget page's only date is the page footer *"Senast uppdaterad: 13 december 2024"* — a page-update date, not a per-mark date. The rule is unregistered residue twice over.
- **Country qualifier missing.** S059 is Sweden-scoped ("not Norwegian law"); the entry writes "a Sámi earmark" with no qualifier anywhere — `grep -ni 'sweden\|swedish\|norway\|norwegian' <entry>` returns no hits. The same defect at line 116 is flagged by the S059 re-open seat as F1 (`.ufo/waves/round-50/falsify/ReopenS059.md` §6), so §5:77 is the same defect in a second location. §5's row is additionally the one place where the *design rule* invites a worldbuilder to encode "lineage" in marks, so the missing country qualifier propagates further here than at line 116.

**Smallest fix (author-lane advice):** rewrite the design-rule cell to what S059 actually supports — e.g. `mark = owner + cut (both ears) + sameby registration; a mark change is recorded against the owner` — and delete "lineage" and "side" unless a lineage-coding source is registered; add "Swedish" to the attested-pattern cell (or scope the row to Sweden). If the author wants Baroin's side-coding, register it as a new row (`S0NN`) with tier B and the "reported second-hand via Baroin" caveat the scribe seat recorded, cite it in this cell, and add it to the round-50 search log's lead list — that is a round-50 lesson edit plus a registry addition, not a silent reuse.

### F3 — P2 · §5 line 75 · the Nuer naming quote is truncated at the source's own epistemic verb

**Where:** `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:75`.

**The claim as landed:**

> `| Colour × distribution | Nuer cow names follow "its colours and the way in which they are distributed on its body" (S052, ch. I §VIII) | base colour roots + a placement affix set, not a flat list |`

**Evidence.** The located sentence (`.ufo/waves/round-50/build/SrcEvansPritchard.md:92`, read on the page image at printed p. 41) is:

> *"In naming a Nuer cow one has to notice its colours and the way in which they are distributed on its body."*

The entry's quoted fragment is a contiguous but **truncated** substring of that sentence — the leading *"In naming a Nuer cow one has to notice"* is cut, and the source's predicate (the ethnographer **notices** colour and distribution) is what the entry's grammar replaces with *"cow names follow"*. The truncated string is thus quoted as the warrant for a claim ("cow names follow …") that the source does not make in that form. Compare §5 line 106, where the entry quotes the same book and *does* keep the full predicate (*"Nuer tend to define all social processes and relationships in terms of cattle"*) — so the entry's own practice elsewhere is the fuller quotation; line 75 is the outlier.

Two further notes on the same row, both **not** defects:
- The locator `(S052, ch. I §VIII)` matches S052's anchor (*"Ch. I §I pp. 18–19; §VIII pp. 41–46"*) and the re-open seat confirms the §VIII anchor reaches the cited content (`.ufo/waves/round-50/falsify/ReopenS052.md` §3, with two one-line locator slips in the **row**, not the entry: the `(printed page = PDF page − 24)` parenthetical is not a constant offset, and §VIII runs to p. 47). Those belong to the row, not to §5.
- The design rule *"base colour roots + a placement affix set, not a flat list"* is a method prescription; it is not a claim about the world and needs no further source.

**Smallest fix:** extend the quote to the full sentence — `Nuer cow names follow "one has to notice its colours and the way in which they are distributed on its body"` — or keep the fragment but move the verb inside it, e.g. `Nuer cow names follow colour × distribution: "one has to notice its colours and the way in which they are distributed on its body"`. One line, one cell.

### F4 — P2 · head line 6 · the anchor list advertises 15 line numbers no sentence cites

**Where:** `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:6`.

**The claim as landed** (head `- sources:`): *"In-corpus anchors (repo-relative `path:line`, each re-read at `4ad2683` on 2026-10-21)"*, followed by a list naming, among others, `hunting-foraging-subsistence.md:117,:137-146,:170-172` and `agrarian-field-system-lexicon.md:80`.

**Evidence.** A resolution pass over the landed body (lines 8–199) finds every `path:line` the entry actually cites. The listed-but-uncited set is:

- `culture-material/hunting-foraging-subsistence.md:117` — the "Storage as the hinge of rank" bullet; uncited.
- `culture-material/hunting-foraging-subsistence.md:137-146` — the hunting decision table; uncited.
- `culture-material/hunting-foraging-subsistence.md:170-172` — the hunting `## 12. NON-CANON` heading block; uncited.
- `culture-material/agrarian-field-system-lexicon.md:80` — the secondary-products-revolution bullet; uncited.

Every other listed anchor is cited in the body at least once, and §5's three in-corpus anchors (`:70`, `:69`, and the §-level `:105` used at line 156) are all cited. So this is a head-list over-declaration, not a §5 defect: the head claims a re-read provenance for lines the entry never leans on. Under QUALITY criterion 1 (provenance per claim) the over-declaration is harmless to the claims themselves, but it makes the head an unreliable index of what the entry rests on — and it is the head a reviewer reads first.

Two smaller notes on the same line, for the record:
- The head calls the list *"repo-relative `path:line`"*, but the paths are **partition-relative** (`culture-material/…`, `linguistics/…`) and do not exist at the repo root (`ls culture-material` → *"No such file or directory"*). The lane's own model entry, `hunting-foraging-subsistence.md:6-17`, writes the same class of list with **full** repo-relative paths (`corpus/knowledge/civilizations/algonquian.md`) **and sha256 pins**. The landed entry does neither. A reviewer resolving `culture-material/hunting-foraging-subsistence.md:27` from the repo root gets a miss; from `corpus/knowledge/` it hits. This is a real, if low-severity, mislabel — the paths are corpus-relative, not repo-relative.
- The head does not pin sha256 for the load-bearing files, unlike the model entry. Cosmetic; QUALITY does not require it.

**Smallest fix:** either delete the four uncited line-ranges from the head list, or cite them where they belong (`:137-146` and `:170-172` are the hunting decision table and NON-CANON block, which the entry's §11/§12 structurally mirror but do not cite); and relabel the list as `corpus/knowledge`-relative, or rewrite the paths in full repo-relative form with sha256 as the model entry does.

---

## 3. Cross-seat corroboration and boundaries

- **ReopenS065** (`.ufo/waves/round-50/falsify/ReopenS065.md`) independently measured the AHD page and reports the string "livestock" **zero** times, and finds the row itself passes criterion 6. My F1 is the *entry-side* consequence of that measurement: the row is honest, the entry's row title is not. **Consistent, no conflict.**
- **ReopenS059** flags the missing country qualifier at the entry's lines 77 and 116 as F1 and the "personal"-without-sameby-holder compression as F2, with the row itself HOLDS. My F2 covers the **design-rule** half of the same cell — the `lineage`/`side`/`dated` residue from unregistered Baroin — which that seat does not address. **Complementary.**
- **ReopenS060** reports the S060 row's page range is wrong (`92(Suppl 1):95–107` should be **165–181**) and that `:67`'s *"emic portfolio term"* is not asserted by Ahearn, the round's own directly-attesting companion source (Chuluunbaatar 2012) having been opened but never registered. Both are **row-level** defects in `corpus/SOURCES.md` and outside §5; I record them here only so the integrating ledger does not treat the row as clean. §5:78 itself **holds** — its design rule is a method prescription and does not assert emicity.
- **URLs were not re-opened by this seat** (other seats own re-opens). Every external claim above rests on the landed registry cell, the landed lesson Gate bullet, and the landed build-seat reports.

---

## 4. Residual risk and verification gaps

1. **§5's row 75 quote-fidelity (F3) rests on the build seat's page-image reading**, not on my own re-open of the PDF (`SrcEvansPritchard.md:92`, corroborated by `ReopenS052.md` §3). I did not open `people.duke.edu/.../Evans_Pritchard...pdf`. The full-sentence wording "In naming a Nuer cow one has to notice its colours and the way in which they are distributed on its body" should be re-read against the page image before the fix is applied.
2. **F1's AHD measurement** is the S065 re-open seat's (`grep -o -i 'livestock' ahd.html | wc -l` → 0), not mine; I did not re-open the URL. I confirmed the build seat's own quote (`SrcPeku.md:51`) contains no livestock sense, which is consistent with that measurement. The "zero occurrences" figure is second-hand and should be treated as such if the fix text quotes it.
3. **F2's Baroin attribution** is a textual-diff finding (draft row → landed cell), not an independent reading of Baroin 2010. The draft's quoted phrases are the seat's; whether Baroin says "lineage" of "lineage-code" in exactly that shape is unverified by me.
4. **The §5 count rule ("write 'a very large set', never a number")** at line 81 is a house style rule the entry imports; I found no registered row that states it (the §5 draft cited EP1940's "several thousand expressions" as *contested* — the draft's calibration row 25 — and that counter-row was dropped at landing, leaving the rule without its contestation). This is a **minor** calibration-traceability note, not a finding against a claim: the rule itself is a house convention, and the entry cites no source for it, so nothing is asserted beyond method. Recorded here so the ledger sees the dropped contestation.
5. **The S065 `teaches` cell** still says *"livestock/movable-wealth gloss"* although the row's own anchor (the headword gloss) carries no livestock sense. Fixing that cell is a superseding-row operation under the append-only rule (`corpus/SOURCES.md:9-13`); the integrating seat should decide whether to open one now or log it as a residual.
6. **Not checked by me** (out of seat scope, other seats own them): the O gates (`tools/harness/receipt_guard.py`, `tools/check-readme-revisions.py`, the jj-colocation probe), the Ca checker/fixture, the README sweep, and the §4/§8/§9/§11–§13 prose (covered by ReviewSec01/03/04/08/09/11/12/13).

---

## 5. Measurement run (read-only, in the private clone)

```
$ cd /tmp/r50sec05-4180537 && git rev-parse HEAD
1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0

# §5 row inventory + S-id usage
$ awk 'NR>=69 && NR<=81 {printf "%d\t%s\n", NR, $0}' corpus/knowledge/culture-material/pastoralism-animal-husbandry.md
   → 13 lines; 5 data rows at 75,76,77,78,79; master claim at 71; count rule at 81

# every path:line in the entry, resolved against the landed tree
$ (python3)  → 29 unique anchors, all resolve to a live file+line; 0 out-of-range; 0 missing
   cited-in-body check → uncited: hunting-foraging :117,:137-146,:170-172; agrarian :80   [F4]

# every S-id the entry cites
$ (python3)  → 22 distinct S-ids, all S048..S069, all present in corpus/SOURCES.md

# used-by of all 22 new rows
$ awk -F'|' '/^\| S0(4[89]|5[0-9]|6[0-9]) / {...}' corpus/SOURCES.md
   → all 22 rows: used-by = corpus/knowledge/culture-material/pastoralism-animal-husbandry.md

# cited corpus files unchanged base -> landed
$ git diff --stat 4ad2683 1c779e4 -- <21 cited corpus files>
   → no output (byte-identical; no anchor drift)

# unregistered-source residue
$ grep -rc "Baroin" corpus/ | grep -v ":0"        → no output
$ grep -c "Baroin" corpus/SOURCES.md              → 0
$ grep -c "Baroin" corpus/lessons/round-50.md      → 0
$ grep -c "Wiktionary" corpus/SOURCES.md          → 0
$ grep -c "Pokorny" corpus/SOURCES.md             → 0

# Watkins marker check in the in-corpus anchor the entry cites
$ grep -c "to-verify" corpus/knowledge/culture-material/trade-economy-lexicon.md   → 0

# canon scan of §5
$ (manual) → §5 states no world-fact; §12 NON-CANON at :169; §15 handoff at :199
```

Tools: GNU git, awk, grep, python3 (stdlib), sed/head — all preinstalled. **No installs, no pacman transaction, no background jobs, no delegation.** Temp clone `/tmp/r50sec05-4180537` deleted after the run.

---

## 6. Verdict

**Item attacked:** §5 "Herd lexicon and ownership marks" of `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` at `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0`, its in-corpus `path:line` anchors, its S-id support, and its calibration/canon status.

**Verdict: PARTIAL.**

- All in-corpus anchors resolve and support their sentences; all S-ids resolve, are in-scope, and are mined against this entry; no canon leak; no anchor drift between base and landed.
- **F1 (P1)** — `:79`: the "Livestock → wealth" row's livestock end-point is carried by no registered row (AHD: zero "livestock" occurrences). Fix: retitle the row and correct S065's `teaches` via a superseding row, or add the "livestock sense not on the cited page" caveat to the design-rule cell.
- **F2 (P1)** — `:77`: the ownership-mark design rule ("lineage + cut + side"; "a mark change is a dated event") is unregistered Baroin-2010 residue, and contradicts the cited row S059 (owner-named, personal, sameby-registered, Sweden-only). Fix: rewrite the design rule to S059's actual content, add the country qualifier, and either register Baroin with its second-hand caveat or drop the lineage/side elements.
- **F3 (P2)** — `:75`: the Nuer naming quote is truncated at the source's own predicate ("one has to notice"), so the fragment is quoted as a warrant the source does not give. Fix: quote the full sentence.
- **F4 (P2)** — head `:6`: four listed line-ranges are cited nowhere in the body, and the list's paths are corpus-relative while labelled "repo-relative". Fix: drop or cite the four ranges; relabel or rewrite the paths.

Author-lane advice, not admission; a verdict here is a recommendation and does not admit, integrate, or ship anything.
