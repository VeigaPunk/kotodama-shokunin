# ReviewHead — falsify attack on the round-50 claim-C head block

Seat: `KotodamaR50-2.ReviewHead-21` (leaf; no delegation, no background jobs, no swarms).
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Landed target: `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` (base `4ad26836552462d28a946ca3b067cab0b5ce3532`).
Attacked artefact: head block (lines 1–13) of
`corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` (the entry is referred to below as
**PAH**), plus every in-corpus `path:line` anchor it names, plus every S-id it cites against the
landed `corpus/SOURCES.md` row scope/anchor, plus the QUALITY criteria 1–6 bar.

Method: private clone `git clone -q --shared <lane> /tmp/rh21-XXXX` → `checkout -q 1c779e4` (and a
second clone `/tmp/rh21-base` at `4ad2683` for the sweeps). All corpus bytes below were read from the
clone at the landed/base sha, never from the lane working tree. **No lane file was edited; no
`git add/commit/stash/checkout/reset` and no mutating `jj` command was run in the lane; the lane's git
index and jj state, the fleet repo, sibling lanes, `MANIFEST.json` and `.ufo/state` were not touched.**
Tool installs: **none** (no pacman/uv/cargo/npm transaction was needed; every check was
`sed`/`awk`/`grep`/`python3` against repo bytes). No URL was opened this session — URL re-opening
belongs to the `ReopenS0xx` seats — so every S-id check here is a **scope/anchor/support** check
against the landed row, never a re-fetch. `xd://lsp` is not mounted on this host (checked: "No such
tool: xd://lsp"), and the artefacts are Markdown, so all checks are byte-level text reads; no semantic
server answer is claimed anywhere below.

---

## Verdict

**PARTIAL.** The head block's *falsifiable* claims all hold when re-run at base `4ad2683`: both gap
sweeps return 0, the entry counts 225→226 and 27→28, the README sweep is green (rows 226, files 226,
`topic_mismatch 0`, exit 0), all 22 S-ids resolve to landed rows whose `used-by` names the entry, and
every verbatim quote I could check against the round-50 lesson's `## Gate` is a true substring. The
register gap itself is real and the entry does own it.

What does **not** hold: **six defects in the head/anchor layer** — one false cross-reference in the
`gap filled` field, one mislabelled path base that makes 20 anchors unresolvable as written, one
anchor attached to the wrong cell of the one-owner table (inverting the boundary), one unbacked
scope pointer, and three small head↔row mismatches. None of them breaks the coverage claim; all of
them are one-line fixes inside C's own lands.

---

## A. What I re-ran and confirmed (HOLDING)

### A1 — both gap sweeps at base `4ad2683` (head line 4)

```
$ cd /tmp/rh21-base && git rev-parse HEAD
4ad26836552462d28a946ca3b067cab0b5ce3532
$ find corpus/knowledge -iname '*pastoral*' -o -iname '*husband*' -o -iname '*herd*' | wc -l
0
$ grep -rniP '^- topic:.*\b(pastoral|herd|husbandr|transhuman|livestock)' corpus/knowledge/ | wc -l
0
$ grep -rniE '^- topic:.*(pastoral|herd|husbandr|transhuman|livestock)' corpus/knowledge/ | wc -l
1
corpus/knowledge/culture-material/writing-media-surface-economy.md:3  (hit word = "sherd")
```

The head's three numbers (`0`, `0`, "sherd at `writing-media-surface-economy.md:3`, a non-owner") are
**exact**. The un-bounded form's single hit is the word `sherd` in "the incidental surfaces — sherd,
wall, pot, body" — a non-owner, exactly as the head says. (The declared evidence command in
`reports/round-50/claims.json` — `grep -rniE` without `\b` — is the one the round lesson already logs
as mistake R50-M2; the entry's own line uses the word-bounded form, which is the honest one.)

I also ran a **wider** topic scan than the head's, to test whether the word-bounded pattern hides an
owner: `grep -rniE '^- topic:.*(cattle|cow|bull|oxen|nomad|camelid|camel|sheep|goat|reindeer|llama|alpaca|yak|breed|flock|herds|herding|stock|milk|wool)' corpus/knowledge/`
→ 9 hits, all already-cited partial owners or non-owners (`textile-technology.md:3` wool fibre,
`transport-mobility-lexicon.md:4` DRAFT, `balts.md:2` wool dress, `funerary-material-culture.md:4`,
`writing-media-surface-economy.md:3`, `semantic-fields-lexicon-building.md:3`,
`celestial-symbolism-calendars.md:3`, `motif-index-usage.md:3`). **No topic line owns the herding
register.** The gap premise holds; `CriticGapPremise2.md` reaches the same conclusion.

### A2 — the round-44 revival sentence (head line 4)

`reports/round-44/scout/K02-gap-scout.md:73` =
`| Pastoralism / husbandry | 0 | 0 | **named** r35 CM-2 | **carried — reject** |`
— supports "Round 44's gap scout carried pastoralism as a rejected candidate". The connector seat
independently reached the same reading
(`.ufo/waves/round-50/build/ConnectSiblingPastoral.md`: "Round 50 is therefore **the first round
deliberately reviving a carried gap**"), so "round 50 is its first deliberate revival" is corroborated.
A grep of `reports/round-45…49` shows no other pastoralism gap candidate between r44 and r50.

### A3 — the counts and the sweep (head line 10)

```
$ cd /tmp/rh21-base  && find corpus/knowledge -name '*.md' | wc -l   -> 225
                       ls corpus/knowledge/culture-material/*.md | wc -l -> 27
$ cd /tmp/rh21-XXXX && find corpus/knowledge -name '*.md' | wc -l   -> 226
                       ls corpus/knowledge/culture-material/*.md | wc -l -> 28
$ cd /tmp/rh21-XXXX && python3 -B reports/round-28/readme/sweep.py ; echo RC=$?
parts {"civilizations": 94, "culture-material": 28, "linguistics": 25, "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 226 files 226
missing_from_index 0 []   topic_mismatch 0 []   orphan_rows 0 []   header_drift {}
totals_line 226 totals_ok True   footer_ok True
RC=0
```

Every number in `verified-at` is exact, and the sweep is genuinely green (the script is read-only by
its own docstring and wrote nothing). `git rev-parse main` in the lane is now `1c779e4`; the landed
commit's parent is `4ad2683`, so "`git rev-parse main`" was the correct provenance wording at writing
time.

### A4 — the S-id rows (head line 7) and every quote I could check

`corpus/SOURCES.md` gained 22 rows, S048–S069, each with URL, kind, tier, scope, anchor, `teaches`,
status, opened `2026-10-21`, recheck `365d`, and `used-by` = the entry. The row shape matches the
table header at `corpus/SOURCES.md:28` (`id | source | kind | tier | scope | anchor | teaches | status
| opened | recheck | used-by`) and the contract's column set; no duplicate URL was introduced
(the only duplicated URLs in the file are the pre-existing S045/S046/S047 supersession rows), and
Evans-Pritchard 1940 has no earlier row to duplicate.

Every entry quote I could check against `corpus/lessons/round-50.md` `## Gate` is a **verbatim
substring**:

| entry | quote | Gate bullet |
|---|---|---|
| `:16` | "there is little or no impetus to herd animals" | S048 §Classifying pastoral systems ✔ |
| `:47` | "light enough for nomads to carry" | S062 Description 3rd sentence ✔ |
| `:75` | "its colours and the way in which they are distributed on its body" | S052 row `teaches` ✔ |
| `:77` | "Nuer tend to define all social processes and relationships in terms of cattle" | S052 Ch. I §I p.19 ✔ |
| `:93` | "a more diversified exploitation of secondary applications and products such as milk, wool, textiles, and traction" | S051 Abstract opening ✔ (attribution caveat B5) |
| `:114` | "Picture a pasture open to all" | S054 p.1244 ✔ |
| `:115` | "developed by the users of a resource" | S055 §4E p.15 ✔ |
| `:122` | "always experienced a need for external agricultural and handicraft products" | S056 Abstract p.85 ✔ |
| `:63` | "on pastures at high elevations" | S061 ch.8 ¶1 ✔ |
| `:67` | five snouts = "horses, yaks/cattle, camel, goats and sheep" | S060 §2 ¶2 ✔ |
| `:139` | "Every night your count is made and your tally-stick put into the ground" | S064 lines 130–142 ✔ |
| `:79` | *peku-* = "wealth, movable property" | S065 headword gloss ✔ |
| `:62` | modern horses do not descend from the Botai lineage | S067 Abstract ✔ |
| `:65` | "the only domesticated ungulates and pre-Hispanic pastoral societies of the Americas" | S068 Introduction ¶1 ✔ |
| `:49` | horizontal in plains/plateaus, vertical in mountains | S069 decision sentence 4 ✔ |
| `:112` | "is thus divided by both ecology and the potential for agriculture" | S049 §Land tenure ✔ |
| `:16` | FAO "no impetus to herd animals" / `:43` FAO "simplification" | S048 (second string **not** in Gate — see B10) |
| `:189` | living-practice rule | `hunting-foraging-subsistence.md:195` ✔ verbatim |

### A5 — QUALITY criteria 1–6, re-read for the entry as a whole

* **criterion 2 (calibration status): satisfied by house style.** The entry's `## 13. Calibration bank`
  codes R/C/B/H/T per `verification/calibration-registry.md:35-39` — the identical device the peer
  `hunting-foraging-subsistence.md` uses at its own `## 13` (same section number, same code line,
  same table shape). I checked the registry row text against the entry's gloss and they match
  (`R` rejected, `C` contested, `B` bounded, `H` heuristic, `T` to-verify). **No missing
  self-status is claimed** — the lane's convention is that the bank calibrates the *imported*
  frameworks, not the entry's own method.
* **criterion 3 (coupling): satisfied.** `- couples:` (head line 8) names eight in-corpus files plus
  `lore-shokunin` with a per-file boundary gloss.
* **criterion 4 (usability): satisfied.** §1 test table, §3 typology, §4 species table, §5–§9 design
  tables, §11 build order + error-pattern table.
* **criterion 5 (canon hygiene): satisfied.** `## 12. NON-CANON worked micro-example` (`:169`) declares
  the Ketrun invented; `## 15. Scope` (`:199`) hands canon to lore-shokunin and says "the lore intake
  of the integration contract is still pending, so every handoff is a candidate, not an import" —
  which matches the connector seat's `CM-g` finding (unacknowledged intake ⇒ candidate, not import).
  **No canon decision is made anywhere in the entry.**
* **criterion 1 (provenance): mostly satisfied** — see B8/B9 and peers `ReopenS050` (S050 ecology
  clauses), `ReviewSec04` F7 (Maasai), `ReopenS059` (generic Sámi earmark).

---

## B. Findings (severity order)

### B1 — MEDIUM — the head calls its anchor paths "repo-relative"; they are `corpus/knowledge`-relative, so 20 anchors do not resolve as written

`PAH:6` (head `- sources:`):

> `- In-corpus anchors (repo-relative `path:line`, each re-read at `4ad2683` on 2026-10-21): `culture-material/hunting-foraging-subsistence.md:27,:36,…`

Evidence that the label is wrong: the strings given are **not** repo-relative. `culture-material/…`
does not exist at the repo root; the real repo-relative path is
`corpus/knowledge/culture-material/hunting-foraging-subsistence.md`.

```
$ cd /tmp/rh21-XXXX && ls culture-material 2>&1 | head -1
ls: cannot access 'culture-material': No such file or directory
$ cd /tmp/rh21-XXXX && git ls-tree --name-only 1c779e4 | head
README.md  corpus  reports  tools  .ufo  .gitignore  …
```

The head itself uses the *other* base in the same field group: `PAH:4` cites
`reports/round-44/scout/K02-gap-scout.md:73`, which **is** repo-relative. So the head mixes two bases
and mislabels one of them.

This is also a deviation from the lane's own convention for this exact field: the peer
`corpus/knowledge/culture-material/hunting-foraging-subsistence.md:6-8` writes
"repo-relative `path:line`" and then gives **true** repo-relative paths with a per-file `sha256` pin:

> `corpus/knowledge/civilizations/algonquian.md` (sha256 `8260bad1…`): `:3` the regional seasonal-subsistence ownership; …

So "repo-relative" is a live house label meaning "resolvable from the repo root"; the new entry uses
the label with paths that are not.

**Smallest fix (one word, or a prefix):** either write "corpus/knowledge-relative `path:line`", or
prefix each path with `corpus/knowledge/` and add the peer-style `sha256` pin for the load-bearing
files. A checker following the head as written resolves none of the 20 anchors.

### B2 — MEDIUM — `textile-technology.md:27` is attached to the wrong cell of the one-owner table: it supports the entry's **own** boundary, not the neighbour's

`PAH:36` (§2 one-owner table row) and `PAH:8` (couples gloss):

> | `textile-technology.md:27` | **fibre-to-cloth chain** | flock management, shearing season, **fleece selection** |

The cited line is **not** the fibre-to-cloth chain. At the landed bytes:

```
$ sed -n '22p' corpus/knowledge/culture-material/textile-technology.md
| wool | *Ovis aries* | shear → wash (suint/urine, lanolin) → card or comb → spin | excellent — scaled fiber grips dye; … | worsted, woolen, fleece, staple, *Walker/Tucker* = fullers |
$ sed -n '27p' corpus/knowledge/culture-material/textile-technology.md
- **Wool technology is the fork that matters**: combed long-staple = **worsted** … Ryder (1983) traces fleece evolution: wild sheep are hairy; wool-dominant fleeces are a Bronze-Age artifact of selection — your culture's fleece quality is a *chronology* you can date.
```

* The **prep chain** ("shear → wash → card or comb → spin") is at `textile-technology.md:22`, not `:27`.
* `:27` is the **fleece-quality / worsted-vs-woolen** bullet — i.e. it supports "fleece selection",
  which the same table row assigns to **this entry's** boundary, while the "What it owns" cell
  ("fibre-to-cloth chain") is the thing `:27` does *not* say.

So the anchor is inverted against its own cell: it evidences the entry's half of the boundary and is
used to evidence the neighbour's half. `PAH:89` repeats the same anchor in the products table
("cloth stays in `textile-technology.md:27`").

**Smallest fix:** change the neighbour cell to "wool prep chain and fleece quality, `:22,:27`", and
either drop "fleece selection" from the entry's boundary cell or keep it and say which side owns it
(`textile-technology.md:27` tells the designer that fleece quality is datable; that is a *craft*
calendar, not a flock rule). One line.

### B3 — MEDIUM — the head's "cited one-way in §2" is false for `animal-symbolism.md:73,:110`, and the scope pointers that depend on §2 are unbacked

`PAH:4` (head `- gap filled:`):

> "Partial owners keep their pieces and are cited one-way in §2: … livestock-as-wealth idiom
> (`animal-symbolism.md:73,:110`)."

§2 (the one-owner table) is `PAH:29-39` and has **nine** rows — agrarian, hunting, cuisine, transport,
trade-economy, textile, semantic-fields, fire-fuel, `civilizations/`. It contains **no** myth-symbol
row:

```
$ sed -n '28,40p' corpus/knowledge/culture-material/pastoralism-animal-husbandry.md | grep -c 'animal-symbolism\|sacred-kingship\|ritual-liminality\|symbolism-synthesis'
0
```

The only body citation of `animal-symbolism.md:73,:110` is the single closing sentence of §10
(`PAH:145`); the file is named in the `- couples:` line (`PAH:8`) but not in §2. The head sentence is
therefore false about its own body.

The same hole propagates into two scope pointers, which is why I rank it above the peers' finding:

* `PAH:12` (head `- scope:`) — "it hands the field, the hunt, the dish, the cloth, the road, the market,
  the lexicon field, **the animal sign** and every canon decision to their owners **(\§2, §15)**" —
  §2 hands over no animal sign; the animal sign is handed over in the couples line and §10.
* `PAH:199` (§15) — "hands the field, the hunt, the dish, the cloth, the road, the market, the lexicon
  field, **the animal sign and the shepherd-king** to their owners **(\§2)**" — §2 has no animal-sign
  row and no shepherd-king row either (`sacred-kingship-mythic-charter.md:65` is cited at `PAH:141`
  and in the couples line only).

`CriticGapPremise2.md` (counterexample 1) reports the `PAH:4` half; the **scope-field and §15
pointer** half is this seat's addition.

**Smallest fix:** add two rows to §2 (`animal-symbolism.md:73,:110` — "the herd's signs";
`sacred-kingship-mythic-charter.md:65`, `ritual-liminality.md:63` — "shepherd-king office and
sacrifice typology"), or change the pointers at `PAH:12` and `PAH:199` to "(\§2, §10, couples)".
Either way the head's §2 claim becomes true.

### B4 — MEDIUM — the head's "Partial owners keep their pieces" is false for the agrarian secondary-products owner, which the head itself lists as an anchor

`PAH:4` — "Partial owners keep their pieces and are cited one-way in §2: …".
`PAH:6` — the head's own anchor list includes `culture-material/agrarian-field-system-lexicon.md:56,:62,:80`.

`agrarian-field-system-lexicon.md:80` (landed bytes):

> - **Secondary-products revolution** (Sherratt 1981: traction, milk, wool, manure arriving after
>   domestication) — a generator for "the animal that became a machine"; contested as a single horizon
>   `(to-verify)`.

The new entry restates and **regrades** the same proposition twice (`PAH:93` "… is **C** … (S051)";
`PAH:183` "Sherratt's secondary products arrived as one revolution | C — S051") while its §2 agrarian
row (`PAH:31`) cites only `:56,:62` — `:80` appears nowhere but the head's anchor list. Two corpus
entries therefore grade the same proposition differently (agrarian: *contested, `(to-verify)`*, no
source; PAH: **C**, S051) and neither points at the other. The head's "keep their pieces" sentence is
the sentence that overclaims here; it is my seat's field, and the head's own anchor list shows the
author had read `:80`.

(Corroborates `CriticGapPremise2.md` counterexample 2; the head-line wording is the addition.)

**Smallest fix:** one §2 row — "`agrarian-field-system-lexicon.md:80` | the secondary-products
framing and its contested status | product chain by region (§6 cites S051 as the opened review)" —
plus one clause at `PAH:93` pointing at `:80`.

### B5 — LOW–MEDIUM — the S051 quoted string is presented under Sherratt's name, but the row is the review and its scope says "not primary for Sherratt"

`PAH:93`: "**Sherratt's** "secondary products revolution" — "a more diversified exploitation of
secondary applications and products such as milk, wool, textiles, and traction" **(S051)** — is **C**".

`corpus/SOURCES.md:80` (S051) scope: "…**not primary for Sherratt**"; anchor "Abstract; Introduction
¶1–2; …"; and the round-50 lesson's Gate records the string as the **review's abstract, opening
sentence** — not as Sherratt's wording. The entry's own house convention is to attribute each quote
to the source it actually comes from (`:16` "FAO's synthesis …", `:77` "Evans-Pritchard **wrote that** …",
`:114` "Hardin 1968 | …"). The S051 quote is the one place where the subject named before the quote
is not the source of the quote.

`ReopenS051.md` (URL seat) judged the *substance* supported — the article does carry the thesis — and
recorded the criterion-6 posture as honest. I do not contest that. My point is attribution precision,
and a second, smaller word: the row's `teaches` says "adoption **idiosyncratic** and not tied to one
century or millennium", whereas `PAH:93` says "adoption **regional and staged**" and `PAH:183`
prescribes "regional, **staged** product sequences". "Staged" is a word the row does not license
("idiosyncratic" is the row's word), and §13 repeats it as the prescription.

**Smallest fix (two words, no source change):** `PAH:93` → "the review frames the SPR as
"a more diversified exploitation …" (S051) — **C**: adoption is regional and not tied to one century
or millennium (S051)"; and `PAH:183` → "regional, non-horizon product sequences".

### B6 — LOW — the transport gloss claims route ownership from the Draft row

`PAH:34` (§2) and `PAH:8` (couples): "`transport-mobility-lexicon.md:95` | **draught capacity chain,
route class, load figures**".

At the landed bytes `:95` is the **Draft** row ("load figure + daily distance + terrain law; harness
and feed vocabulary"); the **Route class** row is `:92`. The gloss is true of the file, not of the
anchor.

**Smallest fix:** `transport-mobility-lexicon.md:92,:95`.

### B7 — LOW — the head's S061 gloss understates the row's own anchor

`PAH:7`: "S061 Wiener et al. 2003 *The Yak* **ch. 8**". The landed row `corpus/SOURCES.md:90` anchors
"ch. 8 Management of Yak, Overview ¶1; **ch. 10 Products from Yak and Their Utilization**, Overview ¶2
and ¶4", and the entry's butter and dung-fuel claims (`PAH:88`, `PAH:91`) are the ch. 10 facts. The
head's one-gloss-per-row shorthand is accurate for 21 rows and short for this one.

**Smallest fix:** "ch. 8, 10".

### B8 — LOW — §3's Semi-nomadic row: the `(to-verify)` marker sits on one cell while three sibling cells assert unmarked facts

`PAH:48`: "| Semi-nomadic | part of household travels; a base is held | **village or winter camp plus
satellite camps** | base keeps the old, young and crop plot `(to-verify)` | **the base is store and
drought fallback** |".

Every other row of §3 carries at least two citations; this row carries none, and the only marker
covers the *labour* cell. The settlement cell ("village or winter camp plus satellite camps") and the
risk-strategy cell ("the base is store and drought fallback") are factual assertions about real
pastoral forms with neither citation nor `(to-verify)` — the marker placement signals the author knew
the row was uncertain, which makes the unmarked neighbours read as verified. (`ReopenS048.md` notes
the same row is not supplied by S048; it does not address the marker placement.)

**Smallest fix:** append `(to-verify)` to the settlement and risk-strategy cells of `:48`.

### B9 — LOW — §7's bridewealth row states uncited transfer mechanics; the `(to-verify)` marker is on a different clause

`PAH:101`: "| Bridewealth | **stock from groom's kin to bride's kin; rights in wives and children** |
descent and herd size set the scale `(to-verify)` per culture; do not import a Nilotic figure |".

The middle cell asserts the transfer mechanics and the rights over wives and children with no source
and no marker; the `(to-verify)` sits on the *scale* clause. QUALITY criterion 1: "A claim the author
cannot verify is marked `(to-verify)` inline — never laundered into assertion." The in-corpus neighbour
that does carry a bridewealth fact (`myth-symbol/animal-symbolism.md:73`, "cattle as social idiom —
names, songs, bridewealth") is a Nuer-specific claim, and the row's own instruction is "do not import a
Nilotic figure" — the mechanics cell does exactly that without a marker.

**Smallest fix:** mark the mechanics cell `(to-verify)` or cite the Nuer source for it explicitly and
bound it to Nuer.

### B10 — LOW — one quoted string is not recorded in the S048 row or the Gate bullet (hand-off to the URL seat)

`PAH:43`: "**Any classification of this type must be treated as a simplification** (S048)".

The Gate bullet for S048 records only "there is little or no impetus to herd animals"; the row's
`teaches` cell paraphrases ("nomadic/transhumant/agropastoral/enclosed as simplified degrees of
movement") without the quoted string. Every other quoted string I checked is recorded in the Gate or
in the row. I did not open the URL (not my seat), so I report this as a **recorded-evidence gap for the
URL seat**, not as a false quote.

**Smallest fix:** if the string is confirmed, extend the S048 `teaches` cell (append-only rule: a new
superseding row) or drop the quotation marks; if not confirmed, re-word to the paraphrase the row
licenses.

### B11 — NIT — the topic line enumerates four mobility systems; §3 has five

`PAH:3` — "mobility systems (nomadic, transhumant, agro-pastoral, enclosed)". §3 (`:47-51`) has
Nomadic, **Semi-nomadic**, Transhumant, Agro-pastoral, Enclosed/ranching. The README index row is
byte-equal to the topic line (the sweep reports `topic_mismatch 0`), so this is a topic-line omission,
not a row mismatch. Lowest severity on the list; fix only if the topic line is touched anyway.

---

## C. Corroborations (peers' findings I independently confirmed, credited, not re-claimed)

| finding | my check | peer seat |
|---|---|---|
| Maasai named as a living herding people with no source (S058=WoDaaBe, S059=Swedish Sámi, S063=Bedu; Mongolian ← S060 and Tibetan ← S061 are named but not cited; no opened row covers Maasai) | `PAH:189`; `grep -rni 'maasai' corpus/knowledge/` → the only other hits are beadwork/ochre topics, never herding | `ReviewSec04.md` F7 |
| Sherratt graded twice with no cross-citation (`agrarian:80` vs `PAH:93`/`:183`) | see B4 | `CriticGapPremise2.md` counterexample 2 |
| Nuer cattle idiom restated in PAH without citing `animal-symbolism.md:73`/`trade-economy-lexicon.md:69` | `PAH:59`, `:106` carry no in-corpus anchor for the idiom | `CriticGapPremise2.md` counterexample 3 |
| generic "a Sámi earmark" written from a Sweden-scoped row ("not Norwegian law") | `PAH:78`, `PAH:116` | `ReopenS059.md` |
| S050 ecology clauses ("grass and reliable water", "arid-tolerant small stock") not in the article | `PAH:59`, `PAH:60` | `ReopenS050.md` |
| S050 row anchor off by one paragraph | `corpus/SOURCES.md:79` | `ReopenS050.md` |
| S061 "in most places" is faithful to the source's own hedge | I initially flagged this as a scope overreach; on the peer's evidence (ch. 10 Overview ¶2 reads "…is the main product from the milk in most places") **I withdraw the objection** and record only that the SOURCES `teaches` cell drops the hedge | `ReopenS061.md` N4 |

---

## D. Residual risk and verification gaps

1. **No URL was opened here.** Every S-id judgement above is a scope/anchor/support check against the
   landed row. The strings I could not confirm from repo bytes (S048's "simplification" sentence;
   S059's inheritance/registration/collective-property propositions, whose recorded anchor is only
   "opening paragraph"; S051's "staged") remain open for the `ReopenS0xx` seats.
2. **The head's anchor list is a bare list.** Twenty anchors with no per-anchor note of what each one
   supports; the peer entry annotates every anchor. Three of the anchors are cited **nowhere in the
   body** (hunting `:117`, `:137-146`, `:170-172`; agrarian `:80` is used only as a read). A reader
   cannot tell a load-bearing anchor from a read-one. (Not scored as a defect: QUALITY does not
   require the annotation, and §2/§3/§4 do carry the load-bearing ones.)
3. **S048–S069 are 22 rows for one round.** The `used-by` column names the entry for all of them and
   the append-only rule is respected (no S001–S047 row changed `status`/`recheck`/`used-by` per
   `corpus/lessons/round-50.md` §Status-and-used-by-change-log), but the round's own criterion 7
   (separability) makes "the rows C cites are C's lands" the load-bearing assumption — see
   `reports/round-50/separability/r50-manifest.json`; I did not re-run the separability checker (Ca's
   seat owns it).
4. **Not attacked in this report** (other seats own them): the O claim's `receipt_guard.py` /
   `check-readme-revisions.py` behaviour and the jj-colocation probe; the Ca claim's checker, r49
   fixture and QUALITY criterion 7; the README row's revision-label/REVISION-ORPHAN residual
   (`ReviewReadmeRow.md` owns it).
5. **Host hygiene.** Both private clones (`/tmp/rh21-XXXX`, `/tmp/rh21-base`) were deleted after the
   checks; no scratch files were left behind (host disk is near full). The lane tree was never written
   to except for this report.

---

## E. Smallest-fix list (all inside C's own lands)

| # | file:line | fix |
|---|---|---|
| 1 | `PAH:6` | relabel the anchor list "corpus/knowledge-relative" **or** prefix `corpus/knowledge/` (+ peer-style sha256 pin) |
| 2 | `PAH:36` (+`:8`, `:89`) | neighbour cell → "wool prep chain and fleece quality, `textile-technology.md:22,:27`"; resolve who owns "fleece selection" |
| 3 | `PAH:29-39` (+`:4`, `:12`, `:199`) | add the myth-symbol rows to §2, or repoint the scope pointers to "(\§2, §10, couples)" |
| 4 | `PAH:31` (+`:93`, `:183`) | add an agrarian `:80` row to §2 and point `PAH:93` at `:80` so the two graders meet |
| 5 | `PAH:93`, `PAH:183` | attribute the quoted SPR string to the review; replace "staged" with the row's "idiosyncratic / not tied to one century or millennium" |
| 6 | `PAH:34` (+`:8`) | `transport-mobility-lexicon.md:92,:95` |
| 7 | `PAH:7` | S061 gloss → "ch. 8, 10" |
| 8 | `PAH:48` | `(to-verify)` on the settlement and risk-strategy cells |
| 9 | `PAH:101` | mark the transfer-mechanics cell `(to-verify)` or cite/bound it |
| 10 | `PAH:43` | confirm the S048 string with the URL seat; record it in the row or paraphrase |

**Author-lane advice, not admission.** No verdict here admits or rejects claim C; it reports what
holds in the landed bytes and what does not.
