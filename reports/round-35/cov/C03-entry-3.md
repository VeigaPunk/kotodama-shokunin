- Seat: C03 | executor | claim C (coverage) | date 2026-10-19 | baseline 4a7aede

# C03 — entry author fragment 3 of 6 (culture-material): `writing-media-and-surface-economy`

- Round 35, seat C03 (entry authors ×6 culture-material, ×4 myth-symbol), claim **C** (coverage).
- Lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, baseline `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4` (= HEAD, verified `git rev-parse HEAD` this round).
- Writes: this fragment only. The corpus entry below is **drafted, not applied** — per `reports/round-35/targets.json` shared rule 3, the integrator writes `corpus/knowledge/**`.
- Topic authority: `reports/round-35/plan/P01-c-plan.md` does **not** exist at the time of writing (see `## Owed`). The topic below was chosen by this seat under the missing-dependency rule, from the census + a self-documenting delegate pointer (`corpus/knowledge/linguistics/writing-systems.md` `:7`); if P01 assigns entry 3 a different topic, this draft is reassignable — the bytes are self-contained.

## 1. Why this topic and not another (the gap, in one paragraph)

`corpus/knowledge/linguistics/writing-systems.md` owns script typology and touches the medium twice — `:117` (media bias: "clay survives fire … bamboo and silk rot; stone outlives archives") and `:149` (media-blind design: "Derive glyph shapes from tool physics") — and its build step 2 `:156`) tells the designer to "Choose medium and tool from economy and environment". But the same file's `couples:` line `:7`) hands the medium side away to another partition: "culture-material/\* (clay, papyrus, palm leaf, paper economies)". **That entry does not exist**, and no culture-material entry covers writing surfaces at all (§2 sweep below). The gap is therefore named by an existing corpus entry, not asserted by this seat.

## 2. Absence sweep (commands run 2026-10-19, lane root, HEAD `4a7aede`, `export TMPDIR=$PWD/.scratch`)

| command | result | reading |
|---|---|---|
| `grep -rli "papyrus\|parchment\|clay tablet\|palm leaf\|wax tablet\|ostra" corpus/knowledge/culture-material/` | 4 files | **all four are false positives** — `ostra` inside *prostration* (`architecture-settlement-lexicon.md` `:76,91`; `adornment-body-codes.md` `:5,80,90`); *papyrus* as a reed-boat hull material (`transport-mobility-lexicon.md` `:74`) |
| `grep -rli "papyrus" corpus/knowledge/` | 11 files | none in `culture-material/` as a writing surface |
| `grep -rli "inscription surface" corpus/knowledge/` | 0 | — |
| `grep -rli "surface econom" corpus/knowledge/` | 0 | — |
| `grep -rli "medium econom" corpus/knowledge/` | 0 | — |
| `grep -rli "wax tablet" corpus/knowledge/` | 0 | — |
| `grep -rli "ostraka" corpus/knowledge/` | 0 | — |
| `grep -rli "palm-leaf" corpus/knowledge/` | 4 | passing mentions only (checked; none is a treatment) |

**False-positive class reported rather than omitted** (round-28 `X63-F2` precedent): the `ostra` sweep is a substring sweep and its four hits are the word *prostration*; the honest statement is the narrower one — **zero culture-material entries treat writing surfaces as an object**.

Nearest neighbours, extended here and **never restated**: `culture-material/material-culture-inference-method.md` `:69` (perishability row — "what survives to be seen; memory politics") and `:76` (anti-determinism guard); `synthesis/loanword-material-dating.md` `:68` (material biographies and provenance chains); `synthesis/conlang-blueprint-template.md` `:22` (a bare `writing medium: [ ]` slot in the blueprint template, unpriced); `culture-material/vessel-container-lexicon.md` `:115–121` (containers as documents); `culture-material/craft-artisan-lexicon.md` `:76` (maker's-mark typology — this entry stops at the boundary and does not re-cover it).

## 3. Entry bytes — DRAFT for `corpus/knowledge/culture-material/writing-media-and-surface-economy.md`

Proposed filename: `writing-media-and-surface-economy.md` (alphabetically last in the partition; the index row text for C11 is in §5 below, byte-equal to the `- topic:` line).

````markdown
# Writing media and the surface economy — what a culture writes on, what it costs, and what survives

- topic: What a culture writes on, priced — the surface economy of inscription as a worldbuilding system: the seven surface families (clay and wax; stone and metal; papyrus and parchment; palm leaf, bark and cloth; bamboo and silk; paper; and the incidental surfaces — sherd, wall, pot, body), each with its preparation chain, its tool, its ink, its unit of text, and its cost driver; the master claim that **a medium is three prices wearing a script's clothes** — cost per unit of text, tool physics, and survival rate — and that a designer who has set only the script type has left two-thirds of the writing system unbuilt; the tool-physics rule (reed-on-clay makes wedges, brush-on-paper makes strokes, chisel-on-stone makes capitals, and an incising stylus makes long palm-leaf horizontals impossible) applied to the *economy* the script side leaves open; the cost ladder as the real literacy filter (who can afford to write, hence which register and which genre each medium carries); the survivor's ledger (what the culture's own archive will look like to its archaeologists, and why the lossy transform is a plot device rather than a defect); the medium as a legal instrument (seal, tally stock-and-foil, chirograph, potter's stamp, reign mark) at the boundary with `craft-artisan-lexicon.md`; erasure and recycling economies (palimpsest, tablet reuse, scrap, *damnatio memoriae*) as the generator of accidental survival; the archive commitment each medium forces (the dry room, the scriptorium, the library wall, the copy cycle); calibration of the legend-grade origins (Pergamum parchment, Cai Lun, Samarkand paper) and of strong media determinism; a decision record; and a NON-CANON worked example that prices the D4 stamp-hand record set. Reference knowledge and method only; canon decisions belong to lore-shokunin.
- gap filled: `corpus/knowledge/linguistics/writing-systems.md` states the medium as a constraint twice (`:117` media bias, `:149` media-blind design) and its build step 2 (`:156`) sends the designer to "economy and environment" — but its own `couples:` line (`:7`) delegates that work outward: "culture-material/* (clay, papyrus, palm leaf, paper economies)", and **no culture-material entry covers writing surfaces**. Absence sweep 2026-10-19, lane root, HEAD `4a7aede`: `grep -rli "papyrus\|parchment\|clay tablet\|palm leaf\|wax tablet\|ostra" corpus/knowledge/culture-material/` → 4 files, all four **false positives** (`ostra` inside *prostration*; *papyrus* as a reed-boat hull material); `inscription surface` → 0 files; `surface econom` → 0; `medium econom` → 0; `wax tablet` → 0; `ostraka` → 0; `papyrus` over `corpus/knowledge/` → 11 files, none in `culture-material/` as a writing surface. The nearest neighbours name the medium as a *variable* and leave it unpriced — `culture-material/material-culture-inference-method.md` `:69` (perishability), `synthesis/loanword-material-dating.md` `:68` (material biographies), `synthesis/conlang-blueprint-template.md` `:22` (the blueprint's bare `writing medium: [ ]` slot). This entry is the pricing: the surface inventory, the cost ladder, the survivor's ledger, and the decision rows that slot needs.
- sources:
  - KTD-WM-S-0001 — `corpus/knowledge/linguistics/writing-systems.md` (sha256 `76263260dd8181bae0d969c2d4cd647892535a692eb0e41033d83ea8f005a98b`, read at HEAD `4a7aede`, 2026-10-19): `:7` the `couples:` delegation of clay/papyrus/palm-leaf/paper **economies** to this partition; `:43` Uruk IV, "reed stylus on wet clay → abstract wedge forms"; `:47` "writing begins as bookkeeping … Script shape is tool physics — stylus angle makes wedges"; `:51` the Egyptian media split (chisel on stone / reed pen on papyrus; hieratic ~2600 BCE, demotic ~650 BCE); `:117` "clay survives fire and gets baked harder; bamboo and silk rot; stone outlives archives"; `:149` media-blind design; `:156` build step 2. **The script side; this entry is the medium side and restates none of it.**
  - KTD-WM-S-0002 — `examples/culture-d4/components/03-orthography.yml` (sha256 `0f2ff45439fd7db3e9014bd1012bd917e42d042f457b8cef2bed2c9a791d4e1b`): `:68–71` the `records` block with its `medium:` field (OR-01 "stamped into wax on the ingot or the seal bar"; OR-02 "stamped and incised; each sign is cut as a stamp first"; OR-03 "incised on clay and metal, painted on wood and hide; stamps survive for seals and marks"); `:113–115` the three `literacy_institutions` (the stamp-house; the mold-keeper's licence; the furnace roll); `:31` `spine_coupling` naming the league furnace accounts as the longest documents; `:136–137` CAL-O1/CAL-O2. **NON-CANON design drill** — the worked example in §11 prices this record set; the drill itself assigns no price.
  - KTD-WM-S-0003 — `corpus/knowledge/culture-material/material-culture-inference-method.md` (sha256 `7cc44399f81ab210081cf4a1497831598f7caa748cc109453711d5c6bd5d98c8`): `:69` the perishability constraint row ("what survives to be seen; memory politics"; Barber 1991; Hurcombe 2014) and `:76` the anti-determinism guard ("the culture still *chooses* … a chain with zero choices is a deterministic trap"). This entry applies both to media; it does not restate the ladder or the framework toolbox.
  - KTD-WM-S-0004 — `corpus/knowledge/verification/calibration-registry.md` (sha256 `cf7cceee9008a9db768d074671f490e4e99feb59ed4e10fb21fa0b72a4e0454c`), CAL-03 at `:78–88` (strong Whorf rejected; "weak relativity is always defensible is too broad"). Cited for the **calibration posture** applied to media determinism in §9: the same brake, a different claim.
  - KTD-WM-S-0005 — `corpus/knowledge/culture-material/trade-economy-lexicon.md` `:92,121`: the Exchequer tally's stock/foil split and "split-object authentication" (Greek *symbolon*; the chirograph and *indenture* cut through). The in-corpus statement of the medium-as-legal-instrument; §6 extends it to seals, stamps and tallies as a *surface* family.
  - KTD-WM-S-0006 — `corpus/knowledge/linguistics/register-strata-attestation.md` `:21` — Michael T. Clanchy (1979; 2nd ed. 1993), *From Memory to Written Record: England 1066–1307*, Blackwell: "the seal, the chirograph and the tally as instruments that make a spoken act survive its speaker". Already integrated in this lane at the two loci in KTD-WM-S-0005; cited here for the **survival-of-the-act** function, which is a media property, not a register property.
  - KTD-WM-S-0007 — `corpus/knowledge/linguistics/numerals-and-measures.md` `:10,110`: counting technologies (tally marks, knotted-cord records, counting rods) and the khipu's contested narrative readings. The pre-textual surface family; §2 keeps it as a row and does not re-cover the counting lexicon.
  - KTD-WM-S-0008 — `corpus/knowledge/culture-material/vessel-container-lexicon.md` `:115–121`: containers as documents (Roman *tituli picti*, *figlina* stamps, Chinese reign marks) and as chronometers (Petrie's sequence dating). §6 cross-reads it at the boundary; the stamp typology itself stays with `craft-artisan-lexicon.md` `:76`.
  - KTD-WM-S-0009 — `corpus/knowledge/culture-material/era-periodization-models.md` `:11,23`: the Three-Age system (Thomsen → Worsaae → Montelius) and the emic/etic periodization distinction. The reason the survivor's ledger (§5) is a periodization input: a culture whose writing decays gets dated by what did not.
  - Pliny the Elder, *Naturalis Historia* bk. 13 (papyrus manufacture; the Varro report that parchment was devised at Pergamum). Locator: book 13. **Consulted edition not inspected this round** — the chapter/section split differs by edition, so the pinpoint is `(to-verify)`; the claim used here is book-level only. In-corpus precedent for citing Pliny at book level: `corpus/knowledge/culture-material/material-culture-inference-method.md` (`:69`, "Pliny, NH 9") and `corpus/knowledge/culture-material/sumptuary-law-rank-display.md` (`:3`, "Pliny, *Naturalis Historia* bk. 9"). Framework status: **primary source, mainstream** as a technical report, **legend-grade** on the Pergamum origin (§9).
  - E. G. Turner (1980), *Greek Papyri: An Introduction*, 2nd ed., Oxford University Press. Roll construction, sheet joins, recto/verso, and the trade in used papyrus. **Not consulted this round** — record-level citation; page locators `(to-verify)`.
  - Ronald Reed (1972), *Ancient Skins, Parchments and Leathers*, Seminar Press. The parchment preparation chain (lime, scraping, tension drying) as distinct from leather. **Not consulted this round**; `(to-verify)`.
  - Tsien Tsuen-Hsuin (1985), *Paper and Printing*, Science and Civilisation in China vol. 5 pt 1, Cambridge University Press. Bamboo and wooden slips, the cord-bound bundle, silk as a writing surface, the archaeological paper fragments older than the traditional Cai Lun date. **Not consulted this round**; the pre-Cai-Lun fragment dates are `(to-verify)` at the year level.
  - Jonathan M. Bloom (2001), *Paper Before Print: The History and Impact of Paper in the Islamic World*, Yale University Press. Paper's westward route and the mill economy; the Samarkand/Talas origin story treated as legend-grade. **Not consulted this round**; `(to-verify)`.
  - Colin H. Roberts & T. C. Skeat (1983), *The Birth of the Codex*, Oxford University Press (for the British Academy). The scroll-to-codex transition and the Christian/pagan adoption asymmetry. **Not consulted this round**; the adoption percentages are `(to-verify)` and must not be printed as bare numbers.
  - Raffaella Cribiore (1996), *Writing, Teachers, and Students in Graeco-Roman Egypt*, Scholars Press (American Studies in Papyrology 36). Ostraka and tablets in the schoolroom; the exercise as a medium artifact. **Not consulted this round**; `(to-verify)`.
  - Alan K. Bowman (1994), *Life and Letters on the Roman Frontier: Vindolanda and its People*, British Museum Press. The wax tablet in ordinary correspondence and account-keeping — the everyday-draft surface, not a child's toy. **Not consulted this round**; `(to-verify)`.
  - William V. Harris (1989), *Ancient Literacy*, Harvard University Press. The argument that pre-modern literacy was low, elite, and unevenly distributed — the reason the cost ladder, not the script, is the literacy filter. **Not consulted this round**; the book's disputed figures are not used here; `(to-verify)`.
  - Harold A. Innis (1950), *Empire and Communications*, Oxford University Press; and Innis (1951), *The Bias of Communication*, University of Toronto Press. "Media bias" — durable/heavy vs light/perishable media favouring different social orders. Framework status: **contested in its strong form** (§9); cited for the *variable* (durability as a social parameter), not the thesis.
  - David N. Keightley (1978), *Sources of Shang History: The Oracle-Bone Inscriptions of Bronze Age China*, University of California Press. The oracle bone as an inscribed-and-heated surface; divination record-keeping as an archive practice. **Not consulted this round**; `(to-verify)`.
  - Albertine Gaur (1979), *Writing Materials of the East*, British Library. Palm leaf, bark, cloth and the incised-then-inked preparation chain; the pothi format and its cord. **Not consulted this round**; `(to-verify)`.
  - Elizabeth L. Eisenstein (1979), *The Printing Press as an Agent of Change*, Cambridge University Press; with Adrian Johns (1998), *The Nature of the Book*, University of Chicago Press. Cited only for §9's calibration that the "print revolution" thesis is **contested** and that print's effects were gradual and local. **Not consulted this round**; `(to-verify)`.
- calibration: the **surface inventory, the cost ladder, the survivor's ledger and the decision rows are this lane's design method**, assembled from the cited works; the works are cited for the mechanisms they document, never as evidence about any fictional world. **Strong media determinism** ("the medium is the message" as a law of social form) is rejected in §9 with the same brake `material-culture-inference-method.md` `:76` and `calibration-registry.md` `:78` apply to material and linguistic determinism. Three origin stories are labelled **legend-grade** in §9 (Pergamum parchment, Cai Lun's invention, Samarkand paper) and must not be shipped as history. Every external work in `- sources:` is marked **not consulted this round** — this seat had no network and the checks that would upgrade a locator are named in `verified-at`. The D4 record set is **NON-CANON** drill material.
- couples: linguistics — `../linguistics/writing-systems.md` (the script side; this file takes only the medium side its `couples:` line delegates), `../linguistics/orality-formulaic-language.md` (§9 textualization; the Great Divide calibration at `:139` is applied, not repeated), `../linguistics/numerals-and-measures.md` (tally and cord records), `../linguistics/register-strata-attestation.md` (the documentary institution that makes a spoken act survive its speaker), `../linguistics/semantic-fields-lexicon-building.md` (the surface lexicon as a semantic field), `../linguistics/language-contact.md` (media loanwords as contact strata); culture-material — `../culture-material/material-culture-inference-method.md` (perishability; the anti-determinism guard), `../culture-material/craft-artisan-lexicon.md` (owns the maker's-mark typology — this file stops at the boundary), `../culture-material/vessel-container-lexicon.md` (owns containers-as-documents), `../culture-material/trade-economy-lexicon.md` (owns split-object authentication), `../culture-material/textile-technology.md` (cloth as surface and the fiber economy), `../culture-material/architecture-settlement-lexicon.md` (the scriptorium, the library wall, the dry room as built space), `../culture-material/era-periodization-models.md` (the Three-Age system as a survival artifact); myth-symbol — `../myth-symbol/creation-myths-taxonomy.md` (the divine gift of writing as an etiological slot), `../myth-symbol/symbolism-synthesis-method.md` (sign drift applied to medium prestige); synthesis — `../synthesis/loanword-material-dating.md` (material biographies), `../synthesis/conlang-blueprint-template.md` (the `writing medium: [ ]` slot this file fills), `../synthesis/era-material-scoped-reconciliation.md` (media stages dated separately from language stages); verification — `../verification/calibration-registry.md` (CAL-03 posture), `../verification/citation-format-and-source-registry.md` (the source-registry form used above); siblings — lore-shokunin owns canon; chousa-shokunin owns source investigation.
- source: the design authority is the corpus entries named above read at HEAD `4a7aede` on 2026-10-19, plus the NON-CANON D4 orthography component (KTD-WM-S-0002); the external framework is the `- sources:` list, each item marked with what it supports and what it does not. The surface inventory, the cost ladder, the survivor's ledger and the decision rows are this lane's house method.
- verified-at: 2026-10-19 — in-repo pointers checked mechanically at HEAD `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4` from the lane root (`git rev-parse HEAD`): every cited `path:line` was read at that revision, and the four files carrying digests in `- sources:` were hashed with `sha256sum` the same day. **No external resource was fetched**: this seat ran without network access, so every external work carries "not consulted this round" and its missing check; the specific facts marked `(to-verify)` above are page-level or figure-level pins, and the book-level claims rest on the work's existence and subject, not on an inspected passage. **Not checked and therefore not claimed:** any capacity, price or percentage figure for a surface; any literacy rate; any manuscript count.
- recheck: before printing any surface cost, literacy rate, or survival percentage into a handoff; before dating a script stage by a medium change (media and language stages are separate clocks — `../synthesis/era-material-scoped-reconciliation.md`); and before repeating any of the three legend-grade origin stories. Corrections are new sections or new entries, never rewrites.
- scope: this entry covers the **material and economic** side of inscription — what surfaces exist, what each costs, what each survives, what each authenticates, and what archive each forces. It does **not** cover script typology, sign invention or decipherment (`../linguistics/writing-systems.md`), nor the counting lexicon (`../linguistics/numerals-and-measures.md`), nor the maker's-mark typology (`../culture-material/craft-artisan-lexicon.md`), nor containers-as-documents (`../culture-material/vessel-container-lexicon.md`), nor printing as an industry beyond the §9 calibration note. It records nothing about any world.

## 1. The gap this entry fills, and the one sentence it adds

- The script side answers *what signs*; this entry answers *what the signs are cut into, what that costs, and what of it will still exist*. The added sentence: **a medium is three prices wearing a script's clothes — cost per unit of text, tool physics, and survival rate — and the designer sets all three or the writing system is half-built.**
- Why the three are one object: they are not independent knobs. Tool physics is what the surface does to the stroke; cost per unit is what the surface does to *who writes and what gets written*; survival rate is what the surface does to *the future's evidence*. Changing the surface changes all three at once, which is why the choice is a decision and not a decoration.
- What this entry does not do: it does not tell you which surface a culture "should" have. It gives the ledger; the culture's own optimization is the design act (`../culture-material/material-culture-inference-method.md` `:76`).

## 2. The surface inventory — seven families, each with its cost driver

| family | preparation chain | tool | ink/mechanism | unit of text | cost driver |
|---|---|---|---|---|---|
| **clay / wax** | dig, temper, wedge, form; dry in air (firing is a *choice* or an accident) | reed stylus (clay); bronze/iron stilus (wax) | impression into a soft surface; no ink | the tablet; the wax board, erasable | the scribe's time; the tablet is re-usable while unfired, and a *wax* board is re-usable indefinitely |
| **stone / metal** | quarry or cast; dress, smooth, polish | chisel, punch, graver | incision; paint fills the cut | the monument, the stele, the vessel | the mason's and the metal's cost — the highest per character of any family, and the only family whose cost *buys permanence* |
| **papyrus / parchment** | papyrus: pith strips laid crosswise, pressed, joined into a roll; parchment: skin limed, scraped, dried under tension | reed pen (papyrus); quill (parchment) | carbon ink; later iron-gall | the sheet; the roll; the quire | the animal or the marsh — parchment consumes a herd over years, papyrus consumes a harvest |
| **palm leaf / bark / cloth** | leaf cut, boiled, dried, smoothed; bark beaten; cloth sized | incising stylus, then lampblack rubbed in; brush | incision-then-ink; or direct paint | the leaf, the strip, the bolt; bound through holes with cord | the tree and the beating labour; a *low-capital, high-labour* family |
| **bamboo / wood** | split, shave, plane; cord-bound into bundles | knife, brush | incised or brushed | the slip; the bundle | forest proximity; the binding cord is the archive's spine |
| **paper** | pulp, beat, screen, press, dry; size | brush, quill, pen | brushed ink | the sheet; the bound codex | the mill: paper is the first surface whose cost falls *with scale* |
| **incidental surfaces** | none (a sherd is already made; a wall is already standing) | stylus, brush, charcoal | scratch or paint | the note, the notice, the exercise | zero material cost — the only family a poor household can write on freely |

- **Design lever 1 — the re-usable vs the consumed surface.** A wax board is erased and re-used; a papyrus sheet is consumed. Re-usability decides whether a culture keeps *drafts* at all: a world with only consumed surfaces has no surviving first drafts, hence no visible composition process, hence no textual criticism. That absence is itself a period trait.
- **Design lever 2 — the mill threshold.** Paper is the only family whose cost *falls* with production scale; every other family's cost is roughly linear in the amount of text. A culture that has crossed the mill threshold gets cheap ephemera (notices, bills, letters) and therefore a documentary *flood*; a culture that has not gets curated text only. The threshold, not the script, is what produces a "documentary society".
- **Design lever 3 — incidental surfaces are the archaeologist's friend and the archivist's blind spot.** Sherd and wall writing is cheap, abundant, and almost never kept by the culture that made it. It is exactly the class that a fictional antiquarian would dismiss and that a modern excavator would prize.

## 3. Tool physics, applied to the economy (the script side, not repeated)

- The script side states the physics (`../linguistics/writing-systems.md` `:47,149`). The economy asks the next question: **what does the tool-physics lock-in cost?** Once the sign shapes are cut for one surface's tool, moving surfaces costs a *re-cutting of the repertoire*, not a translation — the reason script reform is expensive and therefore rare, and the reason a script that migrates (clay → papyrus, papyrus → parchment, slip → paper) visibly changes its ductus in the record.
- **The migration rule**: a script crossing surfaces keeps its *architecture* and loses its *geometry*. Counters, stroke order and the sign inventory survive; the wedge, the serif, the hairline do not. A designer who wants a script with a visible migration history writes the geometry change as a dated seam and leaves the inventory intact.
- **The three surface-forced geometries worth naming in a world bible**: (a) impression — the stroke is a *mould* of the tool, so shapes are few, angular and combinable; (b) incision — the stroke is a *cut*, so shapes are linear and resist curves across the grain (long horizontals across a leaf's veins are the classic loss); (c) brush — the stroke is a *pressure path*, so shapes are many, curvilinear and taper, and the repertoire can afford hundreds of distinctions.
- **Consequence for the lexicon**: the sign-name vocabulary is usually a *tool* vocabulary, not an abstract one — signs are named for the mark they are, and the mark is named for what made it. A culture that changes tools keeps the old names (the fossil), which gives the etymologist a dating tool.

## 4. The cost ladder — the real literacy filter

- **The claim**: for most of history the binding constraint on writing is not knowing the script, it is affording the surface. Literacy policy therefore lives in the *material* budget: cheap surfaces widen the writing population without any reform of the script or the school.
- **The ladder, from expensive to cheap, with what each rung buys:**

| rung | surface | who writes on it | register and genre it carries |
|---|---|---|---|
| 1 | stone, metal | the state, the temple, the lineage | the monumental register: titles, law, dedication, genealogy; formulaic, curated, addressed to the future |
| 2 | parchment, papyrus (fine grades) | the institution: chancery, temple, scriptorium | the authoritative document: scripture, charter, chronicle, letter of state |
| 3 | papyrus (coarse), paper (early), cloth | the office and the merchant | the account, the contract, the register, the ledger |
| 4 | paper (post-mill), palm leaf, bamboo | the household and the school | the letter, the note, the exercise, the receipt, the broadside |
| 5 | sherd, wall, slate, scrap | anyone, including the poor and the learning child | the ephemeral: practice, memo, graffiti, tally |

- **The register law this generates**: a culture's *durable* genres are its expensive genres, and its *vernacular* genres are its cheap ones. The register split in the surviving record is therefore a *price* artifact before it is a taste artifact — read the medium before concluding anything about what a culture "chose to write".
- **The two-way error to avoid**: (a) reading the expensive corpus as the culture's mind, when it is the culture's *budget*; (b) assuming cheap surfaces produce democratic writing, when they may produce only *abundant* writing under the same institutions. Cheapness widens the *base*, it does not redistribute the *authority*.
- **In-world lever**: if the plot needs a literacy jump, the cheapest, most realistic cause is a surface-cost collapse (a mill, a fiber, a scrap trade) — not a script reform. Script reform is what a state does when it wants *control*; a surface collapse is what a market does when it wants *volume*.

## 5. The survivor's ledger — what the medium does to the future's evidence

- **The rule**: a medium's survival rate is a property of the surface *plus its deposition*, not of its importance. Clay that is fired survives; clay that is not, returns to mud. Papyrus survives in dry sand and is lost in damp. Parchment survives damp and is lost to fire and to reuse. Palm leaf and bamboo survive only in specific climates. Paper survives in dry archives and burns everywhere.
- **The ledger to fill per culture** (this is the §2 of the D4 worked example, generalized):

| surface | survives when | lost when | typical survivor class |
|---|---|---|---|
| fired clay | always (fire helps) | crushed | the administrative and library tablet |
| unfired clay | almost never | the first rain | — |
| wax (the board) | the board survives; the text does not | erasure is the normal end | the board, re-used |
| stone / metal | always, until quarried away | reuse as building material | the monumental inscription |
| papyrus | dry sand, sealed jars, carbonization | damp, insects, reuse | the dry-climate archive; the carbonized roll |
| parchment | cool and dry, bound | fire, damp, scraping for reuse | the codex that was recopied |
| palm leaf / bamboo | dry tropics; sealed | insects, damp, fire | the bundle, the tied leaf |
| paper | dry archives | fire, damp, war | the mass archive — and, precisely because it is mass, the *sampled* archive |
| incidental (sherd, wall) | in the dump, under the plaster | cleaning, rebuilding | the note nobody meant to keep |

- **The three named biases to design deliberately**:
  1. **The monument bias** — the expensive surface over-represents the state, so the culture's own past looks more official than it was.
  2. **The recycling bias** — where surfaces are re-used (palimpsest, scrap, board), the surviving text is the text that was *least wanted*, which is why the humdrum (accounts, receipts, exercises) can outlive the literature.
  3. **The carbonization windfall** — a disaster can convert a perishable archive into a durable one (a burnt library's tablets; a carbonized roll). A world's best source may be its worst day.
- **Coupling to periodization**: a culture whose writing decays gets dated by what did *not* decay — so its own period names will be material names (Three-Age logic, `../culture-material/era-periodization-models.md` `:11,23`), and its antiquarians will be pot-and-metal men. A culture with a durable archive gets dated by *text* and invents era names and dynastic lists instead. **The medium chooses the periodization style**, which is why this file couples to era work.
- **The calibration this section must carry**: survivorship is not destiny. Absence of evidence is a *formation-process* result (`../culture-material/material-culture-inference-method.md` `:69`), and a designer who writes "this culture left no writing" has usually written "this culture's surfaces were perishable", which is a different and much more interesting fact.

## 6. The medium as a legal instrument — seal, tally, chirograph, stamp

- **The function**: a surface is not only a carrier; it is an *authentication device*. The material carries the proof, and the proof is often a *piece* of the material rather than a text on it.
- **The four instrument types to name in a world bible**:

| instrument | mechanism | what it proves | in-corpus anchor |
|---|---|---|---|
| **seal / impression** | a matrix pressed into clay, wax or lead; the matrix is the secret | that an office acted; the text's authority is the impression, not the hand | `../culture-material/craft-artisan-lexicon.md` `:76` (maker's-mark typology) |
| **tally, split object** | one object cut into matching halves, each party keeping one | that the two holders agree — proof by *reunion*, requiring no literacy | `../culture-material/trade-economy-lexicon.md` `:92,121` (Exchequer stock/foil; *symbolon*; chirograph; indenture) |
| **stamp / mark** | a repeatable impression identifying a maker or an assay | authorship and quality, in a form a non-reader can verify | `../culture-material/craft-artisan-lexicon.md` `:76`; `../culture-material/vessel-container-lexicon.md` `:115–121` (*figlina* stamps, reign marks) |
| **the bound document** | text plus seal plus witness list plus physical form (the roll, the chirograph's cut edge) | that the *act* happened and survives its speaker | `../linguistics/register-strata-attestation.md` `:21` (Clanchy: seal, chirograph, tally) |

- **The craft rule**: a culture's authentication surface and its writing surface are often *different materials*. Bronze seals on clay; wax seals on parchment; the tally's wooden stock against the text on the membrane. Design them as a pair, because the mismatch is where forgery lives — and the forgery economy is the natural plot engine (an unlicensed stamp is a cardinal fraud; `examples/culture-d4/components/03-orthography.yml:114`).
- **Boundary**: the mark typology is `../culture-material/craft-artisan-lexicon.md`'s; the container-document systems are `../culture-material/vessel-container-lexicon.md`'s; the split-object law is `../culture-material/trade-economy-lexicon.md`'s. This entry supplies only the *surface* reason they all work: an impression is cheap to make and hard to fake without the matrix.

## 7. Erasure and recycling — the economy of the second use

- **The four erasure regimes**, and what each does to the record:
  1. **Erasure (the wax board)** — the text is *meant* to vanish; the medium's purpose is reuse. Consequence: a board culture keeps no drafts, and its writing is invisible to archaeology except as styli and boards.
  2. **Washing (the palimpsest)** — parchment is scraped or washed and re-used; the under-text is sometimes recoverable. Consequence: the *discarded* text can be the survivor, and a world's most valuable document may be a text nobody wanted.
  3. **Recycling (scrap, filler, mummy cartonnage, binding waste)** — the surface becomes packaging or structure. Consequence: archives enter the archaeological record through *garbage*, so a culture's bookbinding and its rubbish are its real library.
  4. **Damnatio** — deliberate erasure of a name or a record as an act of state. Consequence: the *shape* of the absence is data; a chiselled-out name dates a political reversal as sharply as a surviving edict.
- **The design lever**: give each culture a stated **recycling threshold** — the price point at which a surface stops being written and starts being packaging. That threshold is a dateable economic fact, and it moves: a surface becomes recyclable exactly when it becomes cheap.
- **The plot lever**: because regimes 2–4 produce *inverted* survival (the unwanted outlives the wanted), a fictional scholar's best find is always in the binding, the dump, or the scrape — never in the archive the state maintained.

## 8. The archive commitment — what a medium forces you to build

- **Each family commits the culture to a building and a labour cycle**, and the commitment is the visible institution:

| surface | the building it forces | the labour cycle | the failure mode |
|---|---|---|---|
| clay | the tablet store; the kiln if fired deliberately | forming, drying, storing flat | rain, and the collapse of the store |
| papyrus | the dry room; the roll store with its labelled jars | marsh harvest, sheet-making, rolling, copy | damp, insects, and the loss of the *making* skill |
| parchment | the scriptorium: herd, lime pits, frames, copying room | herd years ahead of text demand; scraping; quiring; copying | fire, and the cost of every replacement |
| palm leaf / bamboo | the tied bundle store; the recitation or reading room | leaf preparation seasonally; incising; cord-binding | insects, damp, and the fragility of the cord |
| paper | the mill, the rag trade, the warehouse, the binder | pulp beating, screening, drying, sizing, binding | fire and war — and, because paper is cheap, the *volume* problem: nobody can catalogue it |
| incidental | none — the dump is the archive | none | cleaning, rebuilding, and the excavator's indifference |

- **The craft rule**: **the archive is the medium's shadow.** A world bible that names a script and no archive is missing the institution that makes the script matter. Name the building, the keeper's office, and the copy cycle; the rest follows.
- **The copy-cycle law**: a perishable medium forces copying, and copying forces *selection* — so a perishable-medium culture has an active canon (what gets recopied) and a silent majority (what does not). A durable medium permits *hoarding* and therefore produces the opposite pathology: an uncatalogued, unselected mass. Design the pathology you want: the canonizing culture or the accumulating one.
- **The scale trap**: paper's cheapness creates the first archive too large for its own society to read. An in-world scholar drowning in documents is a *period marker* (the documentary society), and the invention of the finding aid is the natural next institution.

## 9. Calibration — legend-grade origins, contested theses, discredited shortcuts

- **Pergamum invented parchment** — legend-grade. The story reaches us through Varro by way of Pliny (*Naturalis Historia* bk. 13) as an *etiological* account of a rivalry over papyrus supply. Skin writing predates it. **Use the story as a culture's own origin myth, never as history** (to-verify at the section level).
- **Cai Lun invented paper, 105 CE** — traditional attribution, and the archaeological record has earlier fragments. The honest formulation: a *court report* of a paper process is dated to 105 CE, and paper is older than the report. Print it that way (to-verify at the fragment-date level).
- **Samarkand paper, 751 CE** — legend-grade (the captives-of-Talas story), standing in for a slower westward transfer through Central Asia and the Abbasid mill economy (Bloom 2001, not consulted this round; to-verify).
- **Strong media determinism** — rejected in its strong form. Innis's "media bias" names a real variable (durability favours some social forms over others) and is **contested** as a causal law; the position here is the same one this corpus takes on material constraints (`../culture-material/material-culture-inference-method.md` `:76`) and on linguistic relativity (`../verification/calibration-registry.md` `:78`): the constraint sets a gradient, the culture chooses inside it. **A "no surface, no thought" claim is the media version of strong Whorf and gets the same treatment.**
- **The Great Divide (oral minds vs literate minds)** — already rejected in this corpus (`../linguistics/orality-formulaic-language.md` `:139`, Finnegan 1977; Street 1984) and **not re-argued here**; this entry applies the consequence: a change of surface changes the *record and the genre*, not the cognition.
- **"Parchment replaced papyrus"** — an oversimplification; the two coexisted for centuries, papyrus persisted in Egypt long after the codex won, and the replacement was regional and gradual. A staged, dated coexistence is the correct model.
- **"Clay tablets were fired for preservation"** — mostly false as a default: sun-drying was normal and fire was usually accident or, for some libraries, deliberate policy. State which one your culture does; the difference is the survival rate.
- **"Wax tablets were for children"** — false; they were ordinary correspondence and account media. The schoolroom is one use, not the use.
- **"The codex won because it was cheaper"** — one proposal among several (capacity, ease of reference, Christian adoption, codex-vs-roll statistics). The adoption percentages that circulate are edition- and sample-dependent; **do not print a bare percentage** (to-verify).
- **"Literacy was widespread because the alphabet was simple"** — the alphabet does not carry the cost; the surface does. Alphabet simplicity is a real variable in *learning* and a weak one in *affording* (§4).
- **Print-revolution thesis** — **contested** (Eisenstein 1979 against Johns 1998; neither consulted this round). Cited here only to keep a world's "printing arrives" scene from becoming a switch-flip: print's effects are local, gradual, and mediated by the same institutions the manuscript medium built.

## 10. Decision record — the media-economy decisions this entry fixes

Each row is a decision a worldbuilder (or a later reviser of this file) must take *explicitly*; the "rejected alternative" column names the option that must not be taken silently. Ids are stable so later rounds can amend rows without rewriting the file.

| ID | Decision | Why | Rejected alternative | Evidence |
|---|---|---|---|---|
| DR-1 | Name the culture's **primary surface** and its **secondary surface**, and date the secondary one as an event | two surfaces read as history; three or more read as noise, and the second surface is a dateable import or invention | a culture with every surface at once | §2; `../linguistics/writing-systems.md` `:43,51` |
| DR-2 | State the surface's **cost per unit of text** in the culture's own units (a day's wage, a measure of grain) | the cost is what the ladder in §4 is read from, and it is the only number that makes the literacy claim testable | pricing the surface in an abstract "expense" | §4; Harris 1989 (to-verify) |
| DR-3 | Derive the **stroke geometry** from the tool and record the derivation as a design note | tool physics is the cheap half of a script's plausibility, and it is where the script side sends the designer (`:156`) | choosing a pretty script and a surface independently | §3; `../linguistics/writing-systems.md` `:149` |
| DR-4 | Fix the **re-usable vs consumed** character of the primary surface | it decides whether the culture has drafts, hence whether its own scholars can see a composition process | treating drafts as a universal | §2 lever 1 |
| DR-5 | Write the **survivor's ledger** as two lists: what was used, and what an excavator would find | formation processes make the two lists different; identical lists are archaeologically naive | letting the found assemblage stand for the used one | §5; `../culture-material/material-culture-inference-method.md` `:69` |
| DR-6 | Name the culture's **authentication surface** separately from its writing surface | the mismatch is where forgery lives, and the forgery economy is a plot engine | one material doing both jobs silently | §6; `../culture-material/trade-economy-lexicon.md` `:121` |
| DR-7 | State the **recycling threshold** (when a surface becomes packaging) and one dated consequence | the threshold is an economic fact and it moves; it also predicts what the record will invert | surfaces that are never re-used | §7 |
| DR-8 | Name the **archive building, its keeper's office, and the copy cycle** | the archive is the medium's shadow, and an institution is what makes the script matter | a script with no institution behind it | §8 |
| DR-9 | Choose the **archive pathology**: canonizing (perishable, copy-forced) or accumulating (durable, uncatalogued) | the two produce opposite scholarly cultures and opposite plot problems | assuming all archives are libraries | §8 |
| DR-10 | Decide which surface the culture **writes on freely** (the incidental family or its absence) | free surfaces produce ephemera, and ephemera produce the documentary flood and the graffiti layer | a culture whose cheapest surface is still expensive | §2 lever 3; §4 rung 5 |
| DR-11 | Label every **origin story** the culture tells about its own medium as legend-grade unless a source pins it | the three famous origins are etiological, and a world's own myth about writing is *characterization*, not history | shipping Pergamum/Cai Lun/Samarkand as facts | §9 |
| DR-12 | Keep **media stages and language stages on separate clocks**; date each medium change independently | a medium change is not a sound change and not a register change; conflating them fabricates synchrony | one timeline for script, medium, and language | §3; `../synthesis/era-material-scoped-reconciliation.md` |
| DR-13 | Route every unresolved figure (cost, literacy, survival, percentage) through the corpus's `to-verify` triage | corpus rule: unverifiable claims are marked, never asserted | printing a confident number | `../verification/to-verify-triage-protocol.md`; `corpus/QUALITY.md` `:5` |

## 11. Applying it to a fictional culture — build order

1. **Inventory the surfaces** (§2 table): fill the seven families with a yes/no and a reason. Most cultures have one dominant, one institutional, and one incidental.
2. **Price the primary surface** (DR-2) in the culture's own units, and write the price as a range with its source marked.
3. **Derive the tool physics** (DR-3) from the primary surface's tool, and note the geometry the tool forbids. If the culture has a script migration, write the geometry seam and keep the inventory.
4. **Set the re-usability** (DR-4) and say whether drafts exist.
5. **Build the ladder** (§4) by naming, for each rung, the institution that occupies it and the genre it carries. The ladder is the culture's *writing policy*, whether or not it has one.
6. **Write the survivor's ledger** (DR-5) — two columns, used vs found — and then name the *three biases* the culture's archaeology will show (monument, recycling, windfall).
7. **Pair the authentication surface** with the writing surface (DR-6), and name the forgery the mismatch invites.
8. **Set the recycling threshold** (DR-7) and one dated consequence (an archive that became binding waste in year N).
9. **Build the archive** (DR-8) and choose the pathology (DR-9).
10. **Couple and test**: run the invented surface list against the sibling decision tables — script geometry against `../linguistics/writing-systems.md`, the surface lexicon against `../linguistics/semantic-fields-lexicon-building.md`, medium loanwords against `../linguistics/language-contact.md`, and the material biographies against `../synthesis/loanword-material-dating.md`.
11. **Calibrate before handoff**: strike every claim that a medium proves a level of civilization; mark remaining doubts `(to-verify)`; and never let a legend-grade origin story enter the bible unflagged (§9, DR-11).

**Worked example (NON-CANON — a pricing of the D4 drill's own record set, not a world decision).** The D4 orthography component (`examples/culture-d4/components/03-orthography.yml`, sha256 `0f2ff454…`) declares three records with a `medium:` field and three literacy institutions, and assigns no price to either. Priced by this entry's ledger, the drill's own numbers imply three things the component does not state. (a) **The capital is the stamp, not the surface**: OR-02's medium is "stamped and incised; each sign is cut as a stamp first" (`:70`), so the binding cost is the stamp inventory, and the `stamp-house` (LI-01, `:113`) is a *capital-holding* institution, which is why the `mold-keeper's licence` (LI-02, `:114`) can make an unlicensed stamp the cardinal fraud — the monopoly is over the matrix, exactly the seal logic of §6. (b) **The longest documents sit on the least surviving surface**: `spine_coupling` (`:31`) names the league furnace accounts as the longest documents, and OR-03's medium (`:71`) is "incised on clay and metal, painted on wood and hide" — four surfaces with four survival rates, of which wood and hide are the worst in §5's ledger. D4's own archaeology would therefore recover stamps, seals and fired clay, and *not* the accounts that carry its legal memory; the drill's `OQ-O3` (`:133`, the E2 reversal with "no dated document") is the same absence seen from the other end. (c) **The periodization follows**: a culture whose longest documents are on wood and hide gets dated by its stamps and its metal, so its own antiquarians would be mark-and-ingot men (§5 coupling). None of the three is a canon claim; each is derived from the drill's declared fields by this entry's rows, and each is a candidate amendment for whoever owns the drill next.

## 12. Handoff note and canon boundary

- This entry ends at the handoff. It supplies: the seven-family surface inventory, the three-price model, the tool-physics economy, the cost ladder with its register law, the survivor's ledger with its three biases, the authentication-instrument table, the four erasure regimes, the archive-commitment table with its copy-cycle law, the calibration shelf, and the decision rows. It decides nothing about any world.
- **To lore-shokunin**: the receiving bible should take (a) the filled surface inventory with the primary/secondary marks, (b) the priced ladder with its genres, (c) the used-vs-found ledger, (d) the authentication pair and its forgery, and (e) every `(to-verify)` item still open — those must not be promoted to world-fact until resolved through `../verification/to-verify-triage-protocol.md`.
- **Known limits of this entry**: no external work was inspected this round (no network in the seat environment), so all page-level and figure-level pins are `(to-verify)` and the book-level claims rest on the works' existence and subject; the three origin stories are labelled legend-grade and are not evidence; no cost, literacy or survival figure is asserted anywhere in this file; the D4 material is NON-CANON drill. Media stages must be dated independently of language and register stages (DR-12).
````

*End of the draft entry bytes. The heading numbers below (§4–§6 of this fragment) are this fragment's own; the entry's own §1–§12 are inside the fence above. Fragment sections are §1–§3 (above the fence) and §4–§6 (below it).*

## 4. Self-check against the round's stated contract

| requirement (from `reports/round-35/claims.json` claim C and `corpus/QUALITY.md`) | state of the draft |
|---|---|
| frontmatter 4/4: `source` / `verified-at` / `recheck` / `scope` | all four present in the header block; plus `topic`, `gap filled`, `sources` (bullets), `calibration`, `couples` |
| gap named in-file | `- gap filled:` line, plus `## 1.`, with the eight-command absence sweep and the false-positive class reported |
| decision record | `## 10. Decision record`, 13 stable `DR-` rows with rejected alternatives |
| sourced, every pointer resolves or marked `to-verify` | in-repo pointers are `path:line` at HEAD `4a7aede` and were read this round; 4 files carry sha256 digests computed this round; every external work is marked **not consulted this round** with its missing check named in `verified-at` |
| zero fabricated sources | no URL is cited anywhere in the draft; every external work is a named, real monograph with publisher and edition, cited at book level only; the only non-book citations are in-repo paths |
| couples resolve | all `couples:` refs are `../<partition>/<file>.md` under `corpus/knowledge/`, each verified to exist by `ls corpus/knowledge/` this round |
| no canon / clearance / promotion language | the draft's only uses of *canon* are the boundary negations ("canon decisions belong to lore-shokunin", "NON-CANON"); the two uses of **canonizing** (`## 8.` and DR-9) are the archive-pathology term, not a canon claim, and are marked as such here so an auditor does not misread them |
| partition discipline | sits in `culture-material/` because `../linguistics/writing-systems.md` `:7` delegates the medium economy here; the script side is cited, never re-covered |
| QUALITY.md item 4 (usable) | 6 tables, 13 decision rows, an 11-step build order, and one worked example |

## 5. Verification receipt — the draft run through the lane's own audit instrument

The entry bytes were extracted from the fence above and run through the real instrument, in an **isolated sandbox root** (the draft copied to `.scratch/c03/audit-root/corpus/knowledge/culture-material/C03-draft.md`, with every real sibling partition and every real culture-material file symlinked in so that `../<partition>/<file>.md` refs resolve exactly as they would in-tree). **Nothing was written to `corpus/knowledge/`.**

```
$ python3 -B .scratch/c03/audit-root/reports/round-19/audit/entry-audit.py --json \
      .scratch/c03/audit-root/corpus/knowledge/culture-material/C03-draft.md
{
  "schema": "kotodama-entry-audit-v1",
  "entries": [{
    "path": "corpus/knowledge/culture-material/C03-draft.md",
    "sha256": "f039e6e120ed050ff16adebc0ad5cd9cff7965337799fe7cbc725ba0823d4601",
    "size_bytes": 46482,
    "header_fields": ["couples","recheck","source","sources","topic","verified-at"],
    "header_missing_required": [],
    "header_tail_ok": true,
    "source_bullets": 22,
    "source_bullets_with_locator": 22,
    "couples_resolved": 20,
    "couples_unresolved": [],
    "gap_named": true, "decision_record": true,
    "calibration_flagged": true, "canon_hygiene": true,
    "quality_bar": true
  }],
  "summary": {"total": 1, "pass": 1}
}
```

- The instrument copy at `.scratch/c03/audit-root/reports/round-19/audit/entry-audit.py` is a byte copy of `reports/round-19/audit/entry-audit.py`; its `HERE/../../..` root resolution is what the sandbox redirects. It was **not** modified.
- Two authoring defects were found and repaired by this pass, both recorded rather than hidden: (a) **first run `quality_bar: false`** — the sandbox's `culture-material/` held only the draft, so the seven self-partition `couples:` refs had nothing to resolve against; fixed in the sandbox by symlinking the real files, and the entry needed no change (round-tripped to `couples_unresolved: []`). (b) **`source_bullets_with_locator: 17/22`** — a real entry defect: the instrument's locator regex needs a backticked path ending in `.md`/`.yml`, so a ref written `` `path.md:92,121` `` (line numbers inside the ticks) does not register. All 57 `.md:` and 2 `.yml:` refs were rewritten to the lane's `path.md` + `:NN` form (`corpus/knowledge/linguistics/register-lexicon-ceilings.md` is the in-corpus precedent), and the Pliny bullet — the only bullet with no machine-readable locator — gained the in-corpus precedent paths. Re-measured: **22/22**.
- Additional checks run on the same extracted bytes: paren balance across all 201 lines (0 unbalanced lines), `grep -c 'https\?://'` → **0** (the draft cites no URL), `grep -c '^- scope:'` → **1** (the fourth frontmatter field the claim names).
- **Not verified by this seat**: the external works themselves (no network), and the landing itself (the integrator applies the bytes). A post-landing re-run of the same instrument against the real path is the acceptance leg.

## 6. Index-row material (for C11 / the integrator — not this seat's write)

`corpus/README.md` `:169` reads `## culture-material/ (18)`; the landing moves it to 19 and adds one row in filename order (last in the section, after `warrior-material-culture.md`). The row's text must be **byte-equal to the entry's own `- topic:` line** (§3 above). The counts footer at `corpus/README.md` `:471–473` (`total 201 files; directory totals 21/19/18/29/20/94`) moves to `202` / `21/19/19/29/20/94` on this entry's landing alone; the round-35 wave as a whole moves it to `211` / `21/23/24/29/20/94` if all ten land. **Both are C11's numbers to re-derive, not mine to assert.**

## Owed

- `reports/round-35/plan/P01-c-plan.md` — **missing at the time of writing** (K01's census, K02's audit method and P01's topic assignment had not landed; `reports/round-35/` contained only `claims.json`, `targets.json` and `telemetry/`). This seat therefore chose entry 3's topic itself and recorded the reasoning in §1–§2 above. **Integrator action**: confirm or replace the topic; if P01 assigns entry 3 a different subject, reassign these bytes to the seat whose topic is unclaimed and re-issue C03 against the assigned gap. If the topic stands, apply §3 to `corpus/knowledge/culture-material/writing-media-and-surface-economy.md`.
- `reports/round-35/scout/K01-coverage-census.md` and `reports/round-35/scout/K02-entry-audit-method.md` — **missing**; this seat re-derived the census (partition counts verified: linguistics 21 / myth-symbol 19 / culture-material 18 / synthesis 29 / verification 20 / civilizations 94 = 201; `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` → `totals.files 201`) and the entry shape contract (read from `corpus/knowledge/culture-material/sumptuary-law-rank-display.md`, `corpus/knowledge/linguistics/register-lexicon-ceilings.md` and `reports/round-19/entries/R19-C12.md`) rather than consuming K01/K02. No integrator action needed unless K01/K02 contradict these readings.
- **Cross-seat collision risk (flag, not a defect)**: C01–C06 each author a culture-material entry and P01's assignment is missing, so six independently chosen topics could collide. This seat's topic is unclaimed as of the sweep in §2 (`writing medium`/`writing media` appear in exactly 2 files corpus-wide, both outside `culture-material/`: `synthesis/conlang-blueprint-template.md` `:22` and `civilizations/levant-canaan-phoenician.md` `:53`). **Re-checked at 05:28Z against the sibling fragments that had landed** (`reports/round-35/cov/C01-entry-1.md`, `C02-entry-2.md`, `C05-entry-5.md`, `C06-entry-6.md`; C04 had not landed): C01 → `mortuary-material-culture.md`; C02 → `agrarian-field-system-lexicon.md`; C05 → furniture and the interior; C06 → fire, fuel and light (the hearth, the fuel ladder, lamps and candles). **No collision with this seat's topic** — the six are disjoint as far as they are observable, and C06 in particular claimed the fire/fuel/light gap that this seat had also considered and set aside. The integrator should still confirm C04's topic before applying, since C04 was the one seat not observable at that time.

## Citations

Every path below was read or executed at lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin` at HEAD `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4` on 2026-10-19.

- `REGIMEN.md` (round contract; read in full).
- `reports/round-35/claims.json` (claim C, before/after, thresholds, non-goals).
- `reports/round-35/targets.json` (C03 seat object: `mission`, `out`, `shared_rules`).
- `git rev-parse HEAD` → `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4`.
- `for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done` → 21 / 19 / 18 / 29 / 20 / 94 = 201.
- `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` → `totals.files 201`.
- `corpus/README.md` `:169` (`## culture-material/ (18)`), `:471–473` (counts footer `total 201 files; directory totals 21/19/18/29/20/94`), `:9–16` (revision 1.9 note).
- `corpus/QUALITY.md` `:5,9,13,16,18` (the five-item admission bar).
- `corpus/knowledge/linguistics/writing-systems.md` `:7,43,47,51,117,149,156`; sha256 `76263260dd8181bae0d969c2d4cd647892535a692eb0e41033d83ea8f005a98b`.
- `corpus/knowledge/culture-material/material-culture-inference-method.md` `:59,69,76,78`; sha256 `7cc44399f81ab210081cf4a1497831598f7caa748cc109453711d5c6bd5d98c8`.
- `corpus/knowledge/verification/calibration-registry.md` `:78–88` (CAL-03); sha256 `cf7cceee9008a9db768d074671f490e4e99feb59ed4e10fb21fa0b72a4e0454c`.
- `corpus/knowledge/culture-material/vessel-container-lexicon.md` `:115–121,137–160,171–177` (containers as documents; decision-record and handoff format copied).
- `corpus/knowledge/culture-material/trade-economy-lexicon.md` `:92,121` (tally stock/foil; split-object authentication).
- `corpus/knowledge/linguistics/register-strata-attestation.md` `:21` (Clanchy: seal, chirograph, tally).
- `corpus/knowledge/linguistics/numerals-and-measures.md` `:10,110` (counting technologies; khipu).
- `corpus/knowledge/linguistics/orality-formulaic-language.md` `:130–138,139–150` (textualization; the Great Divide rejected).
- `corpus/knowledge/culture-material/era-periodization-models.md` `:11,23` (Three-Age system; emic/etic).
- `corpus/knowledge/culture-material/craft-artisan-lexicon.md` `:76` (maker's-mark typology).
- `corpus/knowledge/synthesis/loanword-material-dating.md` `:68` (material biographies).
- `corpus/knowledge/synthesis/conlang-blueprint-template.md` `:22` (`writing medium: [ ]` slot).
- `corpus/knowledge/civilizations/levant-canaan-phoenician.md` `:53` (perishable media bias a surviving stone corpus).
- `examples/culture-d4/components/03-orthography.yml:31,68–71,97,112–115,133,136–137`; sha256 `0f2ff45439fd7db3e9014bd1012bd917e42d042f457b8cef2bed2c9a791d4e1b`.
- `corpus/knowledge/linguistics/register-lexicon-ceilings.md` (head block + `## 12. Errata` — the model for a head-block sweep with a reported false positive).
- `reports/round-19/entries/R19-C12.md` (entry-author fragment shape) and `reports/round-19/audit/entry-audit.py` (the mechanical bar: required header fields `topic`/`sources`/`couples`, `verified-at` + (`recheck`|`source`), ≥1 located source bullet, all `couples:` `.md` refs resolving, gap-named, decision-record).
- Sweep commands, all at lane root 2026-10-19: `grep -rli "papyrus\|parchment\|clay tablet\|palm leaf\|wax tablet\|ostra" corpus/knowledge/culture-material/` → 4 files, all false positives; `grep -rli "papyrus" corpus/knowledge/` → 11 files; `grep -rli "inscription surface" corpus/knowledge/` → 0; `grep -rli "surface econom" corpus/knowledge/` → 0; `grep -rli "medium econom" corpus/knowledge/` → 0; `grep -rli "wax tablet" corpus/knowledge/` → 0; `grep -rli "ostraka" corpus/knowledge/` → 0; `grep -rli "writing medium\|writing media" corpus/knowledge/` → 2 files (both outside `culture-material/`).
- `ls corpus/knowledge/myth-symbol/`, `ls corpus/knowledge/verification/`, `ls corpus/knowledge/synthesis/`, `ls corpus/knowledge/culture-material/` (every `couples:` target verified to exist).
- `sha256sum corpus/README.md` → `053966a2147e5e71675b290d12bd4e523b73b31c764513ccb26a672bed37d57c`.
- `python3 -B .scratch/c03/audit-root/reports/round-19/audit/entry-audit.py .scratch/c03/audit-root/corpus/knowledge/culture-material/C03-draft.md` → `PASS … src=22/22 couples=20 unresolved=[] gap=True dec=True` / `TOTAL 1/1 clear the bar` (sandbox root assembled by symlinking the real partitions; the instrument file is an unmodified byte copy of `reports/round-19/audit/entry-audit.py`).
- `git status --porcelain` → `?? reports/round-35/` only (no write outside this seat's out path).
