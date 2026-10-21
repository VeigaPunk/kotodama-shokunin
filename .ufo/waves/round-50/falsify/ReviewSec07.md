# ReviewSec07 — falsify attack on §7 "Herd as wealth and exchange"

- Seat: `KotodamaR50-2.ReviewSec07-21` (reviewer, leaf — no delegation, no background jobs).
- Item attacked: **C coverage**, section §7 of
  `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0:corpus/knowledge/culture-material/pastoralism-animal-husbandry.md`
  (landed file lines 95–106).
- Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. Read-only attack seat: **no lane file was
  edited, no git/jj command was run in the lane, no delegation, no background job, no installs.**
- Method: every line of §7 was read from the landed blob (`git show 1c779e4a…:<path>`, saved to
  `/tmp/r50-pastoral.md`); every `path:line` anchor in the whole entry was resolved and opened at
  1c779e4a; every S-id cited by §7 (S048, S049, S052) was checked against its `corpus/SOURCES.md`
  row (`scope`/`anchor`/`teaches`) and its `corpus/lessons/round-50.md` `## Gate` bullet.
  URLs were **not** re-opened (other seats own that).

---

## 0. Verdict

**§7 as landed: PARTIAL.** The three S-id-cited cells hold; the four *uncited* cells do not.
§7 is the only substantive section of the entry with **zero** in-corpus `path:line` anchors, and
the claims it makes without a source are exactly the claims an author would have to own
(`rights in wives and children`, `the borrower keeps some offspring`, `stock taken to rebuild
after loss`, `risk spread against local disaster`). One of them (`raids target … animals and
people, not grain`) is pointed at a section (§9) that does not contain it, and its second half
("and people") has no support anywhere in the corpus or in S048–S069. §7 also carries **no
calibration status** on any row, and the entry's §13 calibration bank has **no row for any of the
four transfer types** §7 introduces.

Severity order below. Each finding gives the exact landed line, the command and its output, and
the smallest fix.

---

## 1. HIGH — the Raid row's rule is unsupported and its pointer (§9) does not contain it

**Landed text** (`corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:104`):

```
| Raid | stock taken to rebuild after loss | raids target the form of wealth: animals and people, not grain (§9) |
```

**§9 does not say this.** §9 is `## 9. Pastoral–sedentary relations` (landed lines 120–131). Its
only raid-adjacent sentence is the bias-flag line 131, and the corpus file it points at does not
support raid targets either:

```
$ git show 1c779e4a…:corpus/knowledge/culture-material/pastoralism-animal-husbandry.md | sed -n '120,131p' | grep -n raid
12:Bias flags: Chinese dynastic histories are indispensable and not neutral (`turkic-steppe.md:193`); reject any ladder from "raider" to "state" (`turkic-steppe.md:194`); "barbarian" is a calibration defect. …

$ git show 1c779e4a…:corpus/knowledge/civilizations/turkic-steppe.md | sed -n '194p'
- **Colonial/evolutionist bias:** … Reject a ladder from “nomad/shaman” to “civilized/monotheist”; audit each claimed continuity separately.
```

Two defects in one sentence:
1. `turkic-steppe.md:194` says **nomad/shaman → civilized/monotheist**; the entry renders it as
   **raider → state**. That is a mis-transcription of the cited anchor (a §9 finding, owned by the
   §9 seat — recorded here because §7's Raid row is the only consumer of that pointer).
2. Nothing in §9, in the corpus, or in S048–S069 supports "**and people**". A raid targeting
   captive people is a substantive ethnographic claim with zero backing:

```
$ git grep -n -iE "raid|captive|slave" 1c779e4a… -- corpus/knowledge/civilizations/turkic-steppe.md corpus/knowledge/civilizations/mongol.md corpus/knowledge/civilizations/scythian-saka.md
(no output)
$ git grep -c -i raid 1c779e4a… -- corpus/knowledge | grep -v pastoralism
…/civilizations/rapa-nui.md:2 …/civilizations/china-qing.md:3 … (all unrelated: braid, garments, raids on settlements)
```

QUALITY criterion 1 requires a factual claim to carry a cited, checkable source or be marked
`(to-verify)` inline. This one carries neither — the `(§9)` is a topical pointer, not support.

**Smallest fix (one of):**
- mark the rule `(to-verify)` and drop "and people": `raids target the form of wealth — livestock, not grain — (§9, to-verify)`; or
- cite an opened source that says it (none currently exists — see §5 below); or
- delete the rule and keep only the design column (`stock taken to rebuild after loss`), which is
  the defensible half.

---

## 2. HIGH — §7 has no calibration status anywhere, and the calibration bank has no row for any §7 transfer type

**QUALITY criterion 2** (`corpus/QUALITY.md:9-12`): "every framework entry names its status:
mainstream / contested / discredited, with the reason."

§7's table has three columns and no status column (`pastoralism-animal-husbandry.md:99`):

```
| Transfer | What moves / who gains | Design rule |
```

Compare the sibling table two sections down, which does it right (`:112`):

```
| Model | Proposition | Status | Design use |
| Hardin 1968 | … | **R** as a law of pastoral life; **B** for genuinely open access | … |
```

And the entry's own §13 bank (`:177-187`) covers the stage ladder, "pure nomad", the cattle
complex, Hardin, Sherratt, herd management vs. morphology, Botai, the Nuer generalisation and the
publisher-summary rule — **but nothing about bridewealth, stock loans, herd splitting or raids**,
the four instruments §7 exists to teach:

```
$ git show 1c779e4a…:corpus/knowledge/culture-material/pastoralism-animal-husbandry.md | sed -n '179,187p' | cut -c1-60
| Nomadism is a rung on a ladder (hunting → herding → farming → state) | R — S048 repor…
| The "pure nomad" lives on the herd alone | R as description — S056: nomads always needed ex…
| Herskovits' "cattle complex": herders hoard cattle for prestige | C — S053 attributes the l…
| Hardin's tragedy describes pastoral commons | R as universal; B for unmanaged open access …
| Sherratt's secondary products arrived as one revolution | C — S051 | regional, staged produ…
| Herd management begins when bones get smaller | R — S050: management precedes morphologi…
| Botai horses are the ancestors of domestic horses | C → R for modern horses — S067 | trea…
| "Nuer define everything through cattle" generalises to herders | B — S052, one 1940 ethnogr…
| The publisher's summary of a book is the book's argument | B — S057 is a description only (…
```

The build-wave draft of §7 carried four calibration rows and a fourth table column
(`.ufo/waves/round-50/build/ScribeSec07Wealth.md`, "Calibration and source" column + a
`Claim | Status | Say instead` table: Goody B; Sahel B; insurance B `(to-verify)`; Khazanov B;
plus "Cattle as the single value organising all life | C"). **All of it was dropped in the
landing.** The landed §7 therefore asserts four cross-cultural instruments with no status and no
reason — the exact failure mode criterion 2 exists to prevent, and the strongest evidence that
the landing dropped §7's calibration layer rather than never having one.

**Smallest fix:** add a `Status` column to §7's table and one §13 bank row per transfer type, e.g.
`Bridewealth incidence follows descent | B — Goody & Tambiah 1973 sample hypothesis, not a universal
law (to-verify: HRAF record only) | …`, `Stock loan as insurance | H — insurance logic rests on
Dahl & Hjort 1976 (to-verify) | …`, `Raid as restock | B — Khazanov thesis, detail to-verify | …`.

---

## 3. MEDIUM-HIGH — §7 is the only substantive section with zero in-corpus `path:line` anchors; three of its factual cells are unsourced

```
$ python3 - <<'PY'
import re
lines=open("/tmp/r50-pastoral.md").read().splitlines()
sec=lines[94:106]
print("§7 path:line anchors:", re.findall(r"[A-Za-z0-9_./-]+\.md:\d+", "\n".join(sec)))
PY
§7 path:line anchors: []
```

Every other domain section of the entry carries at least one in-corpus anchor (§1 `:27,:36`,
§2 `:31-39`, §3 `mongol.md:40`, §4 `finnic-sami.md:140,:150`, §5 `semantic-fields…:70`,
§6 `textile-technology.md:27`, §8 `finnic-sami.md:150`, §9 `turkic-steppe.md:193,:194`,
§10 `symbolism-synthesis-method.md:69`, §11 `semantic-fields…:105`). §7 stands alone with none.

Consequence — three cells of §7's "What moves / who gains" column are unsourced assertions:

| Landed line | Unsourced factual cell | Nearest in-corpus owner (uncited by §7) |
|---|---|---|
| `:101` | `stock from groom's kin to bride's kin; rights in wives and children` | `myth-symbol/animal-symbolism.md:73` ("cattle as social idiom — names, songs, **bridewealth**"); `culture-material/adornment-body-codes.md:21` ("**Bridewealth and the woman's portion** … Goody & Tambiah (1973) is the comparative baseline") |
| `:102` | `an animal lent; the borrower keeps some offspring` | none in corpus (`git grep -i "livestock loan\|stock loan\|herd loan" corpus/knowledge` → only the pastoralism entry itself) |
| `:104` | `stock taken to rebuild after loss` | `linguistics/semantic-fields-lexicon-building.md:105` (steppe field bundle: `war (raid)`) — cited by §5 (`:37`) and §11 (`:156`), not by §7 |

**Boundary defect attached to `:101`.** §2's one-owner table (`:29-39`) never lists
`adornment-body-codes.md`, yet the entry's own scope claims the bridewealth register
(`:12`, `:199`: "herd wealth and transfer", "herd wealth, loans, bridewealth and raiding"). The
corpus already owns bridewealth-as-gendered-capital and the comparative baseline behind it, and
§7 neither cites it nor defers to it. The head's `- couples:` line (`:8`) does not mention it
either — `grep -c "adornment-body-codes" pastoralism-animal-husbandry.md` → `0`.

**Smallest fix:** add `myth-symbol/animal-symbolism.md:73` to the §7 bridewealth row and
`linguistics/semantic-fields-lexicon-building.md:105` to the Raid row; add an
`adornment-body-codes.md:21` row to §2 and to the `- couples:` line ("owns bridewealth-as-
gendered-capital and the woman's portion; this entry owns the herd-stock transfer form").

---

## 4. MEDIUM — "gift" is routed into §7 twice and delivered zero times; the corpus owner of the gift instrument is uncited

§1's register test forwards *gift* to §7, and §11's build step 5 does the same:

```
:23 | **Distribution by rule** | animals move as gift, loan, bridewealth and raid (§7) | market sale only: `trade-economy-lexicon.md` |
:155 | 5 | Wealth | herd ceiling set by labour and disease; loan and gift networks | §7; S049 |
```

But §7's four rows are Bridewealth / Stock loan-partnership / Herd splitting / Raid — **no gift
row** (`awk 'NR>=95 && NR<=106' | grep -ci gift` → `0`), and "gift" appears nowhere in §7. The
in-corpus owner of the gift instrument is Mauss's gift as a total social fact at
`myth-symbol/ritual-liminality.md:46`, which the entry cites only at `:63` (a different line, for
the rite-writing rule) — never for the wealth transfer that §1/§11 promise. Symmetrically, §7 has
a row (herd splitting) that §1's list does not name.

**Smallest fix:** add a Gift row to §7 citing `ritual-liminality.md:46` (or drop "gift" from
`:23` and `:155` and from the topic line `:3`/`:199`).

---

## 5. MEDIUM — the "risk buffer / risk spread" claims lost their `(to-verify)` in the landing

§7's master sentence (`:97`) asserts the herd is a "risk buffer"; the herd-splitting row (`:103`)
asserts "risk spread against local disaster". Neither carries a source or a `(to-verify)` marker:

```
:97  A herd works as marriage currency, loanable capital and risk buffer at once; design each transfer by what moves, who gains rights and what it insures.
:103 | Herd splitting | animals spread across kin and pastures | risk spread against local disaster; transhumance splits the herd (S048) |
```

The build draft marked exactly this: `insurance logic rests on Dahl & Hjort 1976, cited via FAO
§3.05 (to-verify)` (`ScribeSec07Wealth.md`). The landed §7 keeps `(to-verify)` only on the
*loan* row (`:102`) and drops it from the risk-sharing claim. S060 is the registry row that
actually carries risk-sharing content (`reliability-seeking risk management; covariate dzud risk
limits risk sharing`), and it is cited in the entry at `:47` and `:67` — but not in §7, where the
risk claim lives.

**Smallest fix:** mark `:97`'s "risk buffer" and `:103`'s "risk spread against local disaster"
`(to-verify)`, or cite S060 for the risk-sharing half.

---

## 6. LOW-MEDIUM — S048's registered anchor does not name the Transhumance subsection §7 relies on

§7 `:103` and §3 `:49` both attribute "herd splitting" under transhumance to S048. S048's
`anchor` cell (`corpus/SOURCES.md:77`, field 6) reads:

```
 §Classifying pastoral systems; §Pastoral enterprises (Nomadism, Enclosed systems and ranching); §Pastoral species; §History and origins of pastoralism
```

Its `teaches` cell (field 7) does cover the substance: "nomadic/transhumant/agropastoral/enclosed
as simplified degrees of movement; **herd splitting**; herders manage two to four species". So
the claim is broadly within the row's `scope` — but the *anchor* under-covers it: **Transhumance
is not among the anchored subsections.** Under the lane's own rule that the anchor records where
the quote was read, "transhumance splits the herd (S048)" is not traceable inside the registered
anchor. (SOURCES rows are append-only; `anchor` is not in the mutable set — only `status`,
`recheck`, `used-by` — so an in-place edit is not the fix.) URL re-opening is another seat's job;
this is a registry-side observation only.

**Smallest fix:** a superseding S-row (e.g. `S070`) with the anchor extended to
"§Pastoral enterprises (Nomadism, Transhumance, Enclosed systems and ranching)", cited by
`:49`/`:103`; or soften to "herd splitting is a degree of movement FAO registers (S048)".

---

## 7. LOW — the two sources §7's content was drafted from are not in the registry at all

The build draft sourced §7's loan and raid rows to FAO chapter 3 "Reconstitution and rehabilitation"
(`x5439e03.htm`, §3.12–§3.16) and its bridewealth row to Goody & Tambiah via HRAF
(`ScribeSec07Wealth.md`, "Sources opened this session", items 1 and 3, with verbatim quotes:
"a cow is loaned to another herder, the latter receiving the first three calves born before
returning the cow to her owner"; "Theft or raiding of stock is an alternative means by which an
individual herder or group of pastoralists can make good their losses relatively quickly").

Neither is a S-row. Goody & Tambiah is at least traceable as a lead (`corpus/SOURCES.md:142`:
"Goody & Tambiah via HRAF" in the opened-but-not-registered list). The **FAO chapter-3 PDF is
absent from both the registry and the lesson's lead list**:

```
$ git show 1c779e4a…:corpus/SOURCES.md | grep -c "x5439e03\|Reconstitution\|bitstreams"
0
$ git show 1c779e4a…:corpus/lessons/round-50.md | grep -c "x5439e03\|Reconstitution"
0
```

So §7's two most source-dependent cells (loan mechanics, raid-as-restock) rest on material that was
opened and quoted during the build and then dropped from every record the corpus keeps. If C's
intent was that §7 cite opened sources, the right move is to register that chapter as an S-row
rather than to re-derive the claims unsourced.

---

## 8. What HOLDS in §7 (verified, no action)

1. **S049 → "herd wealth tracks household labour"** (`:102`). `corpus/SOURCES.md:78` `teaches`
   field: "herd wealth tracks household labour; tenure is divided by ecology and the potential for
   agriculture; pastoral tenure is a common-property debate, not open access". The claim is
   verbatim within the row's scope ("social structure and pastoral land tenure as summarised for
   policy"). ✔
2. **S048 → "herd splitting"** (`:103`, and `:49`). In S048's `teaches` field. ✔ (anchor
   under-coverage noted in §6 above.)
3. **S052 → the Evans-Pritchard quote** (`:106`). The quote
   `"Nuer tend to define all social processes and relationships in terms of cattle"` matches the
   `## Gate` bullet verbatim — `corpus/lessons/round-50.md:37`: `Ch. I §I, p. 19: "Nuer tend to
   define all social processes and relationships in terms of cattle."` — and the entry's status
   `**B** to that people and period` matches S052's own scope ("Evans-Pritchard's own 1940
   assertions about Nuer cattle idiom and cattle naming; not contemporary Nuer practice, not a
   pastoral universal"). ✔
4. **Canon hygiene in §7**: no canon decision, no invented world fact. The only invented material
   (Ketrun) sits in §12 (`:167-171`) and is explicitly `**NON-CANON.**`; §15 (`:197-199`) hands
   canon to lore-shokunin. ✔
5. **Every S-id the whole entry cites resolves**, and all 22 new rows carry
   `used-by = corpus/knowledge/culture-material/pastoralism-animal-husbandry.md`:

```
$ for id in S048…S069; do … check field 12 …; done   # (lane read-only)
used-by check done      # zero mismatches
```

6. **All in-corpus anchors used elsewhere in the entry resolve and support their sentences** —
   opened at 1c779e4a: `agrarian-field-system-lexicon.md:56,:62,:80`; `trade-economy-lexicon.md:69`
   (Lat. *pecūnia* < *pecus* 'cattle' — supports ":79"); `fire-fuel-light.md:37`; `:27`;
   `transport-mobility-lexicon.md:95`; `hunting-foraging-subsistence.md:27,:36,:116,:195`;
   `semantic-fields-lexicon-building.md:70,:105`; `animal-symbolism.md:73,:110`;
   `symbolism-synthesis-method.md:69`; `sacred-kingship-mythic-charter.md:65`;
   `ritual-liminality.md:63`; `celestial-symbolism-calendars.md:28`; `mongol.md:40`;
   `turkic-steppe.md:148,:193,:194`; `scythian-saka.md:70`; `finnic-sami.md:140,:150`;
   `dine-navajo.md:125`; `inca.md:128`; `calibration-registry.md:35-39,:142`. ✔ (Note the §7-internal
   inconsistency: the head's in-corpus list at `:6` names `myth-symbol/animal-symbolism.md:73,:110`
   and `:37`/`:145` use the bare basename form `animal-symbolism.md:73,:110` — same file, two
   path spellings; cosmetic, not a defect.)

---

## 9. Residual risk / verification gaps

- **Not re-verified here (other seats own it):** whether the FAO, UNESCO, ETCSL, D-PLACE and
  AHD pages behind S048–S069 still say what `SOURCES.md` records. My S-id checks were made against
  the *registry rows and Gate bullets*, not against the live pages — per the seat's instruction.
- **S048's Transhumance anchor (§6)** can only be closed by re-opening
  `https://www.fao.org/4/y2647e/y2647e02.htm` §Pastoral enterprises/Transhumance. Until then the
  §7/§3 attribution of "herd splitting" to transhumance rests on `teaches`, not on `anchor`.
- **The FAO chapter-3 PDF (§7)** is not registered anywhere; whether its §3.14/§3.15 wording
  supports §7's loan and raid cells depends on a row that does not exist yet.
- **Ownership of the "rights in wives and children" formulation**: `adornment-body-codes.md:21`
  and `animal-symbolism.md:73` both touch it, and the entry's §2 does not list either — the
  duplication question (whose register owns bridewealth) is unresolved inside the corpus, not just
  inside this entry.
- I did not run the sweep, README, separability or any build/lint tool: those are O/Ca/C seats and
  the lane forbids in-tree validation runs.

---

## 10. Tooling

No tool installed or updated. Reads only: `git show`/`git grep`/`git ls-tree` (read-only, lane
untouched), `awk`/`grep`/`python3` on copies of the landed blobs under `/tmp`, `sed`/`cut` for line
extraction. `/tmp` artefacts: `/tmp/r50-pastoral.md`, `/tmp/r50-sources.md`, `/tmp/r50-lesson.md`,
`/tmp/r50-tree.txt`, `/tmp/r50-anchors*.py`, `/tmp/r50-sources.md`. No clone was needed (no
reproduction required the tree); nothing was written under `/tmp` beyond these small text files.

---

## 11. Smallest-fix summary (author-lane advice, not admission)

1. `:104` — mark the raid rule `(to-verify)` or cite a source; drop the unsupported "and people".
2. §7 table — add a `Status` column; add §13 bank rows for bridewealth / stock loan / herd
   splitting / raid (the four B-rows the build draft already drafted).
3. `:101`, `:102`, `:104` — cite `animal-symbolism.md:73`, `semantic-fields-lexicon-building.md:105`
   and (after registering) the FAO chapter-3 row; add `adornment-body-codes.md:21` to §2 and to
   `- couples:`.
4. `:23`, `:155` — add the promised Gift row (cite `ritual-liminality.md:46`) or delete "gift"
   from both lines and from `:3`/`:199`.
5. `:97`, `:103` — mark the risk-buffer / risk-spread claims `(to-verify)` or cite S060.
6. `:49`, `:103` — supersede S048 with an anchor that names the Transhumance subsection.
