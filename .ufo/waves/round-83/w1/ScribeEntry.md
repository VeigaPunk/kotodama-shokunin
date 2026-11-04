# ScribeEntry-2 — round 83 wave 1 (milestone r83-v1)

Seat: scribe, axis **depth**. Owned path: `corpus/knowledge/myth-symbol/marriage-alliance-bridewealth.md`
(claim D's depth entry). Base revision `3088bd7fe2a55a123214abba7008dcddf12b301c`; frozen counters
`21277b089e3c64c247bb4e0fcb033abfdfa1e668`.

## Behavior

- Wrote exactly one product file: `corpus/knowledge/myth-symbol/marriage-alliance-bridewealth.md`,
  **56555 bytes**, installed as the **257th** knowledge file (base `git ls-tree -r --name-only
  <base> corpus/knowledge | grep -c '\.md$'` → 256).
- Shape, all mechanical items checked locally: header block with the eight required `- ` items and
  nothing else before `## 1.`; **7** `## ` sections (`1`, `2`, `2.1`, `3`, `4`, `5`, `6`); the exact
  strings `## 2. Six design decisions` (6 data rows) and `## 3. Attested anchors` (**52** `- `
  bullets, each with exactly one distinct S-id, ids `S909` ×13, `S910` ×10, `S911` ×14, `S912` ×8,
  `S904` ×2, `S905` ×5); no S-id in any table row; `## 2.1` lexicon interface with a six-field table
  and a worked NON-CANON derivation; `## 4` a 14-item craft checklist; `## 5` a NON-CANON worked
  example (the upland league of Tammar); `## 6` the lore handoff.
- Content: marriage as alliance **and transfer**. The six decisions are the payment direction
  (bridewealth / dowry / bride-service / gift-exchange / none), who may marry whom (exogamy,
  endogamy, the closed table of degrees), the rite and its performer, the name-and-dress change,
  the dissolution and return arithmetic, and the guarantor with the children's disposition. The
  organising claim is that the return clause, not the wedding, is the real constitution.
- Calibration is explicit in two places: the `## 3` preamble calibrates the 1911 article as a **dated
  legal survey** (tier B) that carries no evolutionary sequence, so none is attributed to it and no
  unilinear sequence is asserted anywhere in the entry;
  the `## 2` paragraph cites CAL-06 and treats the six rows as six independently settable switches,
  which is the registry's ordered disaggregation.

## Gates run (mine only; I did not run the round graders)

| gate | command | result |
|---|---|---|
| cited-line scoping | `python3 -B tools/check-cited-lines.py corpus/knowledge/myth-symbol/marriage-alliance-bridewealth.md` | `CITED-LINES: 0 finding(s) in 1 file(s)`, exit 0 |
| local structural check | section/bullet/table/header census over the written bytes | 7 sections; §2 = 6 data rows; §3 = 52 bullets; 0 rows carrying ids; all 8 header items present exactly once; 0 bullets with ≠1 distinct id |
| quote location, §3 | every `「…」` span matched against the folded read of the page the binding receipt names | **57 spans checked, 0 not located** |
| receipt digests | `sha256sum` of the fetched pages vs the rows seat's receipts | S909, S910, S911, S912 digests identical; S904/S905 byte counts identical (717782, 163266) |
| owner quotes, §1 | 23 quoted fragments matched against committed bytes at the base revision | 0 missing |

## Findings

1. **The 1911 article is a dated legal survey, and is calibrated as one.** The served "Marriage"
   article is volume 17 pp. 770–776: Roman law, canon law, England, Scotland, foreign marriages,
   concubinage and morganatic marriage, Hardwicke's Act, the deceased wife's sister, the German code
   of 1900. It contains **0** occurrences of "promiscuity", "group marriage" or "matriarchy"; its
   one use of "primitive" names Roman legal forms. This independently confirms the rows seat's
   calibration note. Per the L1's integration note the entry now calibrates it as a **dated 1911
   legal survey (tier B)**, not as framework-status stage theory, and asserts no unilinear sequence
   of its own; the round instruction's premise that EB11 would supply promiscuity/group-marriage
   vocabulary is not true of the located article and the entry does not manufacture it.
2. **Two different Griffith transcriptions (R82-M3 applied).** My first draft quoted the
   sacred-texts Griffith (296271 bytes, IAST spellings). The binding receipt names the Wikisource
   Griffith (70655 bytes, revision 14397100), which has "Surya" 30× and "Sūrya" 0×, "Pusan" 6× and
   "Pūṣan" 0×. **Authoritative reading: the rows seat's** — its receipt binds the row's page. All
   fourteen S911 quotations were re-pointed to the Wikisource spelling and re-verified there; no
   wording differed between the two transcriptions at the quoted verses. The disagreement is
   recorded, not silently resolved (see `.ufo/waves/round-83/w1/stage/ScribeEntry/quotes.md` and the
   message to `ScribeRows-7`).
3. **Four normalisation classes, fixed not waved through.** Avalon's §164 prints `the "Purchase
   price"` with a capital P; the entry quotes the served capitalisation. Church and Brodribb print
   "grand-children" across a line break, so the entry quotes a different clean span of that passage
   and paraphrases the entailment outside the quotation marks. Two Parsoid spans in the Britannica
   page are only locatable with tag-separator spaces ("confarreatio , coemptio in manum , and usus";
   "mancipatio ,"), so the entry quotes only spans that are contiguous in the folded read and
   paraphrases the connecting words. Gutenberg #10 uses U+2019 in possessives, and the Leviticus
   quotations carry it.
4. **The direction rule has two corpus readings and the entry names the authority.** 
   `linguistics/kinship-terminology.md:88` states the wife-giver/wife-taker asymmetry as a property
   of systems ("the debt outlives the wedding"); `culture-material/pastoralism-animal-husbandry.md:113`
   states the stock medium and one direction in a cell marked `(to-verify)`. The entry records the
   lexicon file as authoritative for the asymmetry and the herd file for the medium, and states that
   neither is authoritative for any culture's direction — that is the setting the entry returns.
5. **The gap census is measured, not asserted.** At the base: 0 owning filenames under
   `corpus/knowledge`; the institutional-core sweep `bridewealth|bride-price|bride price|dowry|betroth`
   → 14 lines in 9 files, every one a passing attribute; `- gap filled:` lines naming the surface →
   0; `- topic:` lines naming marriage → 9, each as a rule a neighbouring surface encodes. Live
   positive control: `adornment-body-codes.md:21`, `pastoralism-animal-husbandry.md:113` and
   `kinship-terminology.md:63` all touch the surface and all stop short of the institution.
6. **`ScoutGap/owners.md` landed after my first draft and changed the entry.** I re-read it and
   adopted four things it demanded: the `:82,88` kinship lines as the strongest partial owner with an
   explicit authority rule; the CAL-06 / CAL-140 calibration rows (`verification/calibration-registry.md:53,140`);
   three further adjacent owners (`sacred-kingship-mythic-charter.md:69`, `heraldry-emblems-identity-marks.md:79`,
   `ritual-liminality.md:22`); and an explicit scope-out of divorce/custody procedure, inheritance,
   adoption and demography. It also warned that `naming-systems.md:76`'s "dowry" is a metaphor — the
   entry does not cite it.
7. **`ScoutSources/sources.md` was absent at write time** (its stage dir held only `foldcount.py`), so
   no independent second reading was available to compare. The binding receipts carried the load; if
   the scout's reading later disagrees with a receipt, that is a report-level conflict for the L1, not
   something this entry resolved.
8. **`used-by` acknowledgements.** The entry cites both carried rows. The rows seat appended it to
   S904 and S905 (`guest-right-hospitality-law.md, marriage-alliance-bridewealth.md`) and reports its
   census validate at exit 0 with the entry on disk.

## Touched surfaces

- `corpus/knowledge/myth-symbol/marriage-alliance-bridewealth.md` — created (the only product byte).
- `.ufo/waves/round-83/w1/stage/ScribeEntry/lint.txt` — the cited-lines verdict.
- `.ufo/waves/round-83/w1/stage/ScribeEntry/quotes.md` — quote-location receipt (URLs, byte counts,
  digests, deviation log).
- `.ufo/waves/round-83/w1/ScribeEntry.md` — this report.

No commit, no push, no mutating git/jj command, no edit to `corpus/SOURCES.md`, `MANIFEST.json`,
`.ufo/state/`, another lane, or any fleet-root tracked file. No tool installs were needed. Scratch
The seat scratch directory held only fetched pages and was removed; the quote receipt was copied into
the stage directory first, and nothing is left behind.

## Out of scope (named, not absorbed)

- Divorce and custody **procedure**, inheritance and succession, adoption and fosterage, demography
  (rates, household size, age at marriage): no owner in this lane; a later legal-institutions entry
  or another lane may claim them. The entry states this in its `- scope:` cell.
- Canon: which world has which rule, who is married to whom — lore-shokunin.
- The four registry rows and S904/S905 `used-by`: the rows seat. `corpus/SOURCES.md` was not touched.
- The gate registry, SKILL.md, QUALITY criterion 31, the cited-records tool and the round-82 record
  repairs: other seats in this wave.

## Artifact paths (repo-relative)

- Entry: `corpus/knowledge/myth-symbol/marriage-alliance-bridewealth.md`
- Lint verdict: `.ufo/waves/round-83/w1/stage/ScribeEntry/lint.txt`
- Quote receipt: `.ufo/waves/round-83/w1/stage/ScribeEntry/quotes.md`
- Binding rows receipts (read, not written): `.ufo/waves/round-83/w1/stage/ScribeRows/S909.txt` …
  `S912.txt`
- Gap/owner map (read, not written): `.ufo/waves/round-83/w1/stage/ScoutGap/owners.md`,
  `gap-census.md`

## L1 integration note (applied)

The L1's note (agent `KotodamaR83`) asked for five quote spans to be matched to the binding bytes and for the
Britannica row to be calibrated as a **dated 1911 legal survey**, not as stage theory. Both were already
true or were applied on receipt: the five spans are at lines 91, 97, 99, 112 and 134 of the entry, all
verified against fresh fetches whose sha256 equals the receipts; the calibration wording at lines 39 and 82
now says "dated legal survey" and the entry asserts no unilinear sequence anywhere. Locations were reported
back to the L1.
