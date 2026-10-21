# ReviewSec06 — falsify attack on §6 (Products) and the Sherratt calibration of the landed pastoralism entry

Seat: `KotodamaR50-2.ReviewSec06-21` (leaf member; no delegation, no background jobs, no mutating git/jj command in the lane).
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Landed target: `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` (base `4ad26836552462d28a946ca3b067cab0b5ce3532`).
Method: private clone `git clone -q --shared /home/vgpnk/Projects/shokunin/kotodama-shokunin /tmp/r50sec06 && git -C /tmp/r50sec06 checkout -q 1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` (read-only; deleted afterwards). Every byte quoted below was read **at the landed commit** in that clone — the lane working tree was never trusted for a landed claim. No lane file was edited except this report. URLs were not re-opened (other seats own the URL seats); I checked each row's own `scope`/`anchor`/`teaches` text and each in-corpus `path:line` at the landed commit.
Tooling: no installs (host-wide pacman pause respected; nothing needed beyond `git`, `python3`, `grep`). Temp clone under `/tmp` removed at end.

## Verdict

**PARTIAL.** The §6 table's *design* half holds — every in-corpus anchor it leans on resolves at the landed commit and supports the sentence it is attached to — and the Sherratt *thesis* is correctly marked contested. But the Sherratt *attribution* and *finding* in §6 misstate what the cited row actually licenses, one §6 cell asserts an uncited fact, and the file's calibration discipline for Sherratt is weaker than its own discipline for Herskovits two lines away.

| id | severity | locus | defect |
|---|---|---|---|
| **F1** | MODERATE–HIGH | `:93` | the quoted fragment is the **review's** abstract prose presented as Sherratt's words; S051's own scope says "not primary for Sherratt", and the build seat forbade exactly this ("Do not put words in Sherratt's mouth") |
| **F2** | MODERATE | `:93`, `:183` | "the review finds adoption **regional and staged**" — S051's `teaches` says "idiosyncratic"; "staged" is not the review's finding and inverts its critique of any tidy sequence |
| **F3** | MODERATE | `:183` | calibration code for the *one-horizon* proposition softened from the build draft's "C → R as a single wave" to plain **C** — inconsistent with the file's own use of **R** at `:162`/`:179` when a source refutes a reading |
| **F4** | MODERATE | `:90` | "castrated adults" — an uncited factual claim: no S-id, no in-corpus anchor, and the cell's only pointer (`:95`) does not mention castration. QUALITY criterion 1 |
| **F5** | LOW–MODERATE | `:195` vs `:181` | §14's recheck opens the unopened primaries for Herskovits and Ostrom but **not for Sherratt**, while §6/§13 name Sherratt and quote his thesis — asymmetric discipline on the same defect class |
| **F6** | LOW–MODERATE | `:85-91` | §6 carries no per-row status code; the build draft's `Code` column (B/C) and its "narrow sample, do not generalise" caution were dropped. QUALITY criterion 2 |
| **F7** | LOW | `:88` | S061's plateau scope dropped in §6 (kept in §4 `:63`): "yak butter is the main milk product in most places" reads as a general claim |
| **F8** | LOW | `:91` | "one dung per season" is not an actionable design rule (QUALITY criterion 4) |

Appendix A records the whole-file anchor / S-id sweep I ran for coverage. Author-lane advice, not admission.

---

## F1 (MODERATE–HIGH) — §6 quotes the review's abstract under Sherratt's name

`corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:93`:

```
Sherratt's "secondary products revolution" — "a more diversified exploitation of secondary applications and products such as milk, wool, textiles, and traction" (S051) — is **C**: …
```

The quoted fragment is not Sherratt's text. `corpus/SOURCES.md:80` (row S051) says so in its own words:

```
| S051 | Marciniak 2011, The Secondary Products Revolution: … Journal of World Prehistory 24(2):117–130 — … | paper | B | what Sherratt's secondary-products thesis claims and this review's three-region critique (Central Anatolia, Balkans, North European Plain); **not primary for Sherratt** | Abstract; Introduction ¶1–2; Discussion and Conclusions ¶1 | … | mined | 2026-10-21 | 365d | corpus/knowledge/culture-material/pastoralism-animal-husbandry.md |
```

The build seat that opened the page recorded where the fragment actually sits — `.ufo/waves/round-50/build/SrcSherratt.md` (landed in the same commit):

```
Location: Abstract, first (opening) sentence — the sentence that begins "Andrew Sherratt is perhaps best known for the concept of a 'Secondary Products Revolution', which stressed that the 'primary' pattern of exploiting domesticated animals for meat in the Early Neolithic was followed by …". The fragment starts mid-sentence; the preceding clause names the meat-first Neolithic.
```

and, as a standing instruction to the entry author:

```
1. **Do not put words in Sherratt's mouth.** The assigned row is a review. Write "Sherratt's model, as Marciniak summarises it, …" or cite the review directly; never "Sherratt (1983) says …" on the strength of this row.
```

The landed `:93` puts the review's prose in Sherratt's mouth: the sentence subject is *Sherratt's* "secondary products revolution", the quoted fragment follows as its content, and the `(S051)` tag reads as a page-cite for Sherratt rather than as a tier-B secondary that the row's own scope bars from speaking for him. The file shows it can do this correctly — `:187` codes the same class of problem honestly ("**B** — S057 is a description only (QUALITY criterion 6)"), and `:106` quotes Evans-Pritchard directly because S052 *is* his own book (tier A, primary). `:93` gets neither treatment. QUALITY criterion 1 requires a cited, checkable source for a claim; criterion 6 keeps a tier-B row scoped to what the row itself says; here the entry asks a tier-B review to be the primary voice for Sherratt's wording.

This is not a stylistic quibble: the tier-A route to Sherratt's own text was blocked on 2026-10-21 (the same build seat logged `https://www.tandfonline.com/doi/abs/10.1080/00438243.1983.9979887` → **HTTP 403**, Crossref → no abstract, JSTOR → bot wall), so the entry's own citation cannot be read as primary.

**Smallest fix** (`:93`, one clause): `Sherratt's "secondary products revolution", as the review phrases it — "a more diversified exploitation of secondary applications and products such as milk, wool, textiles, and traction" (S051) — is **C**: …`

## F2 (MODERATE) — "regional and staged" is not the review's finding; §13 repeats it

Same sentence, `:93`:

> the review finds adoption regional and staged, not one horizon (S051)

and `:183`:

> | Sherratt's secondary products arrived as one revolution | C — S051 | regional, staged product sequences |

The registered teaching of S051 (`corpus/SOURCES.md:80`, `teaches` column) is:

> adoption **idiosyncratic** and not tied to one century or millennium

"Staged" is not in the row, and the review's own conclusion — as the build seat recorded it (`.ufo/waves/round-50/build/SrcSherratt.md`, §13 section) — is the opposite of a staged sequence:

> the review's own finding: across all three regions the introduction of secondary products "was idiosyncratic and highly diverse" … and the linked changes are "by no means associated with a single century or millennium"

A "staged" regional sequence is exactly the tidy horizon the review criticises; the review's finding is that adoption was *idiosyncratic per region*, not that it ran through a common sequence. The entry therefore credits the review with a finding it does not make, and — worse for a calibration entry — hands the reader a staged model to write with in place of the model the review actually leaves standing (a locally dated trajectory, product by product).

**Smallest fix** (`:93` and `:183`, one word each): replace "regional and staged" with "idiosyncratic and regionally diverse" (or with the row's own phrase "not tied to one century or millennium"), and change `:183`'s remedy cell to "regional, idiosyncratic product sequences".

## F3 (MODERATE) — the one-horizon proposition is coded **C** where the file's own rule and the build draft say **R**

`:183`:

> | Sherratt's secondary products arrived as one revolution | **C** — S051 | regional, staged product sequences |

Two internal yardsticks disagree with the code:

1. **The registry code semantics.** `corpus/knowledge/verification/calibration-registry.md:35-39` (which `:175` cites as the code table) defines **R** = "Rejected/discredited as the specified general inference | Do not use as evidence" and **C** = "Contested … Preserve alternatives, scope, and discriminating evidence; do not report one reading as settled". The proposition as worded — *arrived as one revolution* — is the very proposition S051's `teaches` denies ("not tied to one century or millennium"). It is refuted for the three regions reviewed, so **R** for that reading; **C** belongs to the SPR as a research programme, which the entry does need for §6.
2. **The file's own practice.** At `:162` and `:179` the entry codes **R** precisely when the source reports a reading as refuted ("FAO reports the evolutionary-stage reading refuted (S048)"). The same evidentiary shape at `:183` was coded **C** — the file is inconsistent with itself across a single file.

The build draft had this right and it was softened on landing — `.ufo/waves/round-50/build/ScribeSec06Products.md`:

> | One Near East-to-Europe horizon, "idiosyncratic nature of the introduction of secondary products" | **C → R as a single wave** | write regional sequences; mortality profiles are a lead, not proof … |

**Smallest fix** (`:183`, one cell): `R as a single horizon — S051 (adoption idiosyncratic, not tied to one century or millennium); C for the SPR as a research programme` and add the same split at `:93`, where `is **C**` currently attaches to the thesis-with-a-single-horizon without saying which part is which.

## F4 (MODERATE) — "castrated adults" is an uncited factual claim (§6 traction row)

`:90`:

```
| Traction and carrying | castrated adults | cite `transport-mobility-lexicon.md:95` for loads |
```

Nothing in the registry or the corpus licenses "castrated adults":

- `corpus/SOURCES.md` contains **0** occurrences of `castrat` (checked at the landed commit: `grep -c "castrat" corpus/SOURCES.md` → `0`), so no S-row teaches it;
- the corpus at large has **one** husbandry-side occurrence — `corpus/knowledge/civilizations/mongol.md:146` (Cleves 1982 on geldings for station keepers) — and it is not a citation the entry can use;
- the cell's own pointer, `corpus/knowledge/culture-material/transport-mobility-lexicon.md:95` (landed commit), is the transport decision table's **Draft** row: `| Draft | human porterage, ox, horse/mule, camelid, dog, wind | load figure + daily distance + terrain law; harness and feed vocabulary | … |` — it lists draft animals and never mentions castration;
- `transport-mobility-lexicon.md:64` (Ox and yoke) and `:70` (load figures) likewise say nothing about castration.

The build draft had both the evidence chain and the code, and the quote it carried does not support castration either — `.ufo/waves/round-50/build/ScribeSec06Products.md`:

> | Traction | living adults, castrated at 3–4 yr | "clay models of carts and paired draught animals" [SRC: …same Marciniak URL…] | **C** | a draught herd leaves old castrated males in the bone record; **narrow sample, do not generalise** |

The landed row keeps the unsupported detail ("castrated adults"), drops the age, drops the code, and drops the "narrow sample, do not generalise" caution, then points the reader at a corpus line that does not say it. This is QUALITY criterion 1: "every factual claim carries a cited, checkable source … A claim the author cannot verify is marked `(to-verify)` inline — never laundered into assertion." The neighbouring §6 cells show the house pattern (`:48` and `:51` carry `(to-verify)` where the source does not reach) — this cell simply forgot it.

**Smallest fix** (`:90`, one cell): either ground it — `castrated adults for traction, culled bulls and dry cows kept for breeding (S061) — narrow sample, do not generalise` — or, if no registered row licenses it, mark it `(to-verify)` and cite `transport-mobility-lexicon.md:95` only for the load rule it actually states.

## F5 (LOW–MODERATE) — §14 re-checks the unopened primaries for Herskovits and Ostrom, but not for Sherratt

`:195` (§14):

> Before relying on any §13 row, re-check its row id in `corpus/SOURCES.md`; open Herskovits 1926 and Ostrom 1990 before quoting them (only S053 and S055 are opened); re-open S050 and S067 before quoting a date; …

`:181` (§13, Herskovits row) applies exactly that discipline to its own claim:

> C — S053 attributes the label to Herskovits 1926 and criticises its analyst vocabulary; **the 1926 text is unopened `(to-verify)`**

§6 and §13 name Sherratt and attribute a wording to him (F1) while S051's scope says "not primary for Sherratt" and his 1981/1983 text was never opened (403 on the publisher route, per the build seat). The file marks the identical defect for two other rows and leaves it unmarked for Sherratt — the one row where the entry actually quotes.

**Smallest fix** (`:195`, one clause): `…; open Herskovits 1926, Ostrom 1990 and Sherratt 1981/1983 before attributing a wording to them (only S053 and S055 are opened); …`

## F6 (LOW–MODERATE) — §6 lost its per-row status codes and its "narrow sample" caution

The build draft's §6 table had five columns, two of them load-bearing for the corpus's own admission bar:

```
| Product | Taken from | Evidence chain (opened) | **Code** | Design rule |
```

and per-row codes `B` (meat/hide/blood/bone row, dung row) and `C` (milk, wool/hair, traction rows), plus the design-rule cautions "write any bleeding of living stock as its own practice, or omit it", "goat and camel hair `(to-verify)`", "narrow sample, do not generalise", "milk predates the thesis dates; wool and traction dates stay open `(to-verify)`".

The landed table (`:85-91`) has three columns — `Product | Taken from | Design rule` — so a reader of §6 sees factual claims ("yak butter is the main milk product in most places", "castrated adults") with no per-row status, while the neighbouring §4 table (`:57-65`) has a `Calibration` column and §8 (`:112-116`) a `Status` column. QUALITY criterion 2 requires every framework claim to name its status with the reason; the file's own convention is per-table-row status columns, and §6 is the only product table that lost it.

**Smallest fix** (`:85-91`): add a `Status` column carrying the draft's codes (`B` for the meat and dung rows, `C` for milk/wool/traction), and restore the two dropped `(to-verify)`s — bleeding of living stock (Scribe draft) and goat/camel hair — as inline markers.

## F7 (LOW) — S061's plateau scope is dropped in §6 but kept in §4

`:88`:

> dairy needs pails, a curd/butter chain and storage; yak butter is the main milk product in most places (S061)

`corpus/SOURCES.md:90` scopes S061 to "yak husbandry, products and herders' social context **on the Qinghai-Tibetan Plateau**"; the source sentence behind the claim is "Butter, made in traditional fashion, is the main product from the milk in most places" — "most places" means most places *in the yak-rearing range*, i.e. the plateau. The entry keeps the bound in §4 (`:63`: "cultural claims bounded to the FAO synthesis (S061)") and loses it in §6, where the row reads as a general husbandry law. The same cell also asserts a curding/storage requirement that the build draft carried as unopened (`ScribeSec06Products.md`: "butter, cheese, ghee `(to-verify)`"; "dairy shelf-life: not opened. `(to-verify)`").

**Smallest fix** (`:88`): `yak butter is the main milk product in most places on the plateau (S061)`; and either mark the curd/storage specifics `(to-verify)` or cite the opened chain.

## F8 (LOW) — "one dung per season" is not actionable

`:91`:

> | Dung | any herd | one dung per season: fuel or field (`fire-fuel-light.md:37`) |

`corpus/knowledge/culture-material/fire-fuel-light.md:37` (landed commit) is the fuel-ladder row: `| Dried dung | the herds' output, and therefore the fields' | a hot, fast, smoky fire | a real trade-off against manure; fuel-poor pastoral cultures pay for it in soil |`. The anchor supports the fuel-versus-field trade-off, but the rule text "one dung per season" is not something a worldbuilder can act on — QUALITY criterion 4 requires decision rules a worldbuilder can execute (compare `:73`'s "mark = lineage + cut + side", which is executable).

**Smallest fix** (`:91`): `one dung-store decision per season: fuel or field; the manure-for-manure trade-off is a plot point (`fire-fuel-light.md:37`)`.

---

## Appendix A — whole-file anchor and S-id sweep (coverage)

Run at the landed commit in `/tmp/r50sec06`.

**S-ids.** All 22 ids cited by the entry (`S048`–`S069`) resolve to rows in `corpus/SOURCES.md`; every one of those rows has `status = mined` and `used-by = corpus/knowledge/culture-material/pastoralism-animal-husbandry.md`; no id outside `S048–S069` is cited, and every `S048–S069` row carries a Gate bullet in `corpus/lessons/round-50.md`. Checked mechanically:

```
S-ids in entry: ['S048' … 'S069']
missing rows: []
used-by mismatch: []
outside S048-S069: []
```

**In-corpus anchors.** Every `path:line` anchor used in the body resolves at the landed commit and supports the sentence it is attached to — spot-verified in full for §6 (`fire-fuel-light.md:37`, `textile-technology.md:27`, `transport-mobility-lexicon.md:95`) and for the §4/§5/§7/§8/§9/§10 anchors (hunting-foraging `:27,:36,:116,:195`; agrarian `:56,:62`; trade-economy `:69`; cuisine `:67,:86`; semantic-fields `:70,:105`; animal-symbolism `:73,:110`; symbolism-synthesis `:69`; sacred-kingship `:65`; ritual-liminality `:63`; celestial-symbolism `:28`; mongol `:40`; finnic-sami `:140,:150`; inca `:128`; dine-navajo `:125`; scythian-saka `:70`; turkic-steppe `:148,:193,:194`; calibration-registry `:35-39,:142`). The registry codes table is exactly at `calibration-registry.md:35-39` (R,C,B,H,T) and `:142` is the "subsistence predicts a total social stage — **R**" row, which supports `:162`/`:179`.

**Head-declared anchors never used in the body** (declared at `:6`, used nowhere else) — a completeness defect in the entry's own source list, and one of them is load-bearing for this seat's subject:

| declared anchor | landed content | consequence |
|---|---|---|
| `culture-material/agrarian-field-system-lexicon.md:80` | `- **Secondary-products revolution** (Sherratt 1981: traction, milk, wool, manure arriving after domestication) — a generator for "the animal that became a machine"; contested as a single horizon (to-verify).` | the corpus's **existing owner** of the SPR row already carries the claim *and* its `(to-verify)` marker; §6's SPR paragraph and §13's SPR row never cite it, so the file restates the SPR without the corpus's own calibration of it (see F2/F3/F5) |
| `culture-material/hunting-foraging-subsistence.md:117` | "Storage as the hinge of rank" | declared only |
| `culture-material/hunting-foraging-subsistence.md:137-146` | that file's decision table | declared only |
| `culture-material/hunting-foraging-subsistence.md:170-172` | that file's NON-CANON block | declared only |

Note on `agrarian-field-system-lexicon.md:80`: the build seat flagged it explicitly — `ScribeSec06Products.md`: "`agrarian-field-system-lexicon.md:80` — Sherratt 1981 SPR 'contested as a single horizon (to-verify)'. Present; the single-horizon row now has an opened 2011 critique behind it, **1981 still `(to-verify)`**." The landed entry does not carry that marker forward. Cross-reference: the in-corpus SPR row also lists **manure** among the SPR products; the build seat's anti-laundering note #3 warns manure "must not be sourced to this row" (S051) — the landed §6 dung row correctly cites `fire-fuel-light.md:37` and not S051, so that laundering did **not** occur. Good.

**Other §6-adjacent observations (not claimed as findings in this seat; for the owning seats)**

- `:87` and `:88` encode the SPR primary/secondary distinction ("the dead animal (one harvest)" vs "living females, repeatable") — a claim whose registered home is S051's Introduction ¶1–2, but S051's `teaches` column (`corpus/SOURCES.md:80`) records only "milk, wool, textiles and traction as secondary products; adoption idiosyncratic …". The registry row that is supposed to license §6's central column does not state the distinction it licenses. Fix direction is a new SOURCES row (append-only), or an in-row anchor citation.
- `:59` "managed in the upper Euphrates c. 11,000–10,000 BP (S050)" and `:60` "goats first in the Zagros, sheep in SE Anatolia (S050)" go one clause finer than S050's `teaches` ("four species under management c. 11,000–10,000 BP; species order is regional"); the row's `anchor` does name "§Initial Animal Domestication in the Fertile Crescent, paragraph 3", so this is defensible but the row `teaches` does not carry the loci.
- `:155` "herd ceiling set by labour and disease" cites S049, whose `teaches` says "herd wealth tracks household labour" — "disease" is uncited (criterion 1).
- `:36` `textile-technology.md:27` is registered as owning the "fibre-to-cloth chain", while the chain table sits at `textile-technology.md:19-25` and `:27` is the worsted/woolen fork bullet.
- §6's design-rule column is the only table in the file whose factual cells have no `Status`/`Calibration` column (§4 has `Calibration`, §8 has `Status`) — see F6.

**Canon hygiene.** §6 and the Sherratt calibration take no canon decision: §12 is fenced `**NON-CANON.** … invented to demonstrate the method; canon belongs to lore-shokunin` and §15 hands off "which herds, routes, marks, raids and rites exist in a world". QUALITY criterion 5 satisfied for this seat's section. The Sherratt *citation* problem is a criterion-1/criterion-6 problem, not a canon problem.

## Smallest-fix set (one edit each)

1. `:93` — `Sherratt's "secondary products revolution", as the review phrases it — "…" (S051) — is **C** for the thesis; **R** for the single-horizon reading: adoption idiosyncratic and not tied to one century or millennium (S051). Write product sequences per region.`
2. `:183` — split the code: `R as a single horizon — S051; C for the SPR as a research programme` / remedy `regional, idiosyncratic product sequences`.
3. `:90` — ground "castrated adults" in a registered row or mark it `(to-verify)`; keep `transport-mobility-lexicon.md:95` for the load rule only.
4. `:195` — add "and Sherratt 1981/1983" to the list of unopened primaries to open before quoting.
5. `:85-91` — add a `Status` column (B/C) and restore the two dropped `(to-verify)` markers.
6. `:88` — add "on the plateau"; mark the curd/storage specifics or cite them.
7. `:91` — make the dung rule executable.
8. `:6` — either cite `agrarian-field-system-lexicon.md:80` from §6/§13 (the corpus's own SPR owner, with its `(to-verify)`) or drop it from the declared list, along with the three unused hunting-foraging anchors.

**Author-lane advice, not admission.** Nothing here says the entry fails its round; it says the Sherratt wording and the §6 traction cell are not yet carried by the registry as landed, and that the fix is one clause per site.
