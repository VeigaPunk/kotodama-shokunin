# ScoutGap — claim-D absence census and partial-owner map (round 83, wave 1)

Read-only recon against base `3088bd7f`. Full evidence (commands + raw output) in
`stage/ScoutGap/gap-census.md` and `stage/ScoutGap/owners.md`.

## Verdict

**Before-state proven, with one number corrected.** No file under `corpus/knowledge` owns
marriage; the surface exists only as passing attributes; the new entry would be the 257th file.

## 1. Before-state (claim D)

| measure | expectation | measured |
|---|---|---|
| filename owners (`marriage\|bride\|dowry\|wedding\|spouse\|betroth`) | 0 | **0 of 256** |
| exact institutional core (`bridewealth\|bride-price\|bride price\|dowry\|betroth`) | 9 files / **27 lines** | **9 files / 14 lines / 16 matches** |
| `- gap filled:` / `- gap:` claims naming the surface | 0 | **0 of 67 statements (59 + 8)** |
| headings owning the institution | 0 | **0** (6 name it; 1 substantive section, `kinship-terminology.md:80`) |
| topic lines claiming it as subject | 0 | **0** (9 name it as an attribute) |
| `- couples:` targeting a marriage path | 0 | **0** (no dangling pointer) |

**The "27 lines" does not reproduce.** The file count does. No pattern variant yields 27 lines at
9 files (`+dower` → 16/11; `+trousseau+bridal` → 40/18; `bride|dowry|betroth` → 39/22). The
Likely origin is a transposition from the round-82 hospitality entry, whose own gap sentence reads
"27 lines in 15 files" (`myth-symbol/guest-right-hospitality-law.md:4`) — a different surface. A
landing that copies 27 into the header installs an unmeasured number.

**Corroboration:** the landing entry itself (sibling-written, untracked) already states "14 lines
in 9 files" at base `3088bd7f` in its `- gap filled:` line — the entry and this census agree
independently, so the spec's 27 is the lone outlier.

Wide family, for the entry's gap sentence: **374 lines / 116 files**, of which **8 lines match
only the word "husbandry"** (lexical artifact → semantically clean population 366). Shape split:
189 prose bullets, 125 table rows, 21 bibliography, 14 prose paragraphs, 9 couples, 8 topic,
6 headings, 2 gap lines (both path citations of `pastoralism-animal-husbandry.md`).

Index state: 256 files vs 251 README rows (5 missing: `maritime-seafaring-lexicon.md`,
2× `conlang-scholarship*`, `guest-right-hospitality-law.md`, `ordeal-judicial-proof-rituals.md`);
section headers read `32/32/41/29/24/95` = 253. The entry lands in `myth-symbol/` (34 → 35,
header says 32); the new index row belongs between `hero-journey-variants.md` and
`mineral-stone-symbolism.md`.

## 2. Duplicate-document check (registry: 832 rows, `S001`–`S908`, all 11 cells)

| work | registered? | note |
|---|---|---|
| Code of Hammurabi | **no** | named as a *lead* in a round-50 section note (`SOURCES.md:910`), never rowed; cited in 3 knowledge files without a row |
| EB11 "Marriage" | **no** | EB11 rows are Chess/Veil/Ship/Ordeal/Guest — different documents; online-Britannica rows are a different edition |
| Rigveda, RV 10.85 | **no** | 0 rows for any Rigveda; Jamison & Brereton (2014), which the corpus cites in 4 files, also has 0 rows |
| Leviticus | **no** | S853 cites Lev 19:27 but registers the Jewish Encyclopedia article |
| Homer, *Odyssey* | **yes — S904** | `mined`, `used-by` guest-right; **reuse, do not re-open** |
| Tacitus, *Germania* | **yes — S905** | `mined`, same `used-by`; **reuse, do not re-open** |

Also: the registry already carries one grounded marriage-institution fact — heraldic marshalling
on marriage (`heraldry-emblems-identity-marks.md:79`, rows S560/S414). It is the entry's best
in-corpus positive control. And the registry's own evidence chain warns "before asserting any
marriage–terminology coupling" (`SOURCES.md:877`) — a coupling warning, not an owner.

## 3. Partial owners (ten named + eight found)

**0 owns / 7 mentions / 3 hands-off.** Strongest: `kinship-terminology.md:80-88` (owns the
lexicon encoding and the wife-giver asymmetry — including a sentence about the institution,
"the debt outlives the wedding"), `heraldry:79` (owns the visible status transfer, grounded),
`contact-scenario-builder.md:105-116` (owns intermarriage as a contact variable). Explicit
hands-off: `funerary-material-culture.md:213` (DR-MMC-08), `guest-right-hospitality-law.md:12-23`,
`purity-pollution-boundary-systems.md:186`.

**Two files state a direction rule** — `kinship:88` (in terms) and `pastoralism:113` ("stock from
groom's kin to bride's kin", `(to-verify)`). The new entry must say which is authoritative for the
direction; that is the R82-M3 rule applied inside the corpus.

## 4. Couplings and sibling surfaces

15 one-way couplings named as DR-MB-1..15 (owner file + line + what the new entry returns), in
`owners.md` §3. The lane's existing shape is a boundary table
(`binding-speech-complex.md:49-56`) plus a decision record (`funerary-material-culture.md:205-213`);
the entry should copy both rather than invent a third convention. Calibration binds:
`calibration-registry.md:53` (CAL-06 orders marriage rules **disaggregated**) and `:140`
("Kin terms prove group marriage … — R").

Sibling-lane surfaces **reported, not absorbed**: canon (lore-shokunin); family/household law as
procedure — divorce, inheritance, custody — which is **unowned in this lane** (0 filenames,
0 gap blocks); the wedding rite (`ritual-liminality`); the wedding garment (`ritual-garments`); the
contact/loanword workflow (`contact-scenario-builder`); the calibration rows; and demography, which
no file owns.

## 5. Source probe (independent, non-binding)

- EB11 "Marriage": 200, 147040 B — genuine article, but its spine is the three-stage evolutionary
  law S908 refused; 0 × dowry/bride-price, 9 × consanguinity. Definition + survey only.
- Hammurabi: `The_Code_of_Hammurabi` is an **index page** (71525 B, 0 marriage terms); real text at
  `The_Code_of_Hammurabi_(Harper_translation)` (147981 B, 26 × dowry).
- RV 10.85: Wikisource path **404**; `sacred-texts.com/hin/rigveda/rv10085.htm` 200 but **not
  byte-stable** (two fetches, same size, different sha256) → needs a fixed capture.
- Leviticus (JPS 1917): 200, 528437 B; 32 × "nakedness" (Lev 18), 0 × bride/dowry → anchors the
  prohibited-degrees boundary, not the transfer.

Per R82-M3 this is a **third, non-binding** reading: `ScribeRows`' receipts bind and
`ScoutSources` is the second reading. Neither peer had published a stage file when this seat ran,
so **the cross-reading comparison is outstanding** — if their byte counts or quotes disagree with
§5, report the disagreement rather than picking one.

## 6. Housekeeping

No tool installed or upgraded (nothing needed). The seat's out-of-repo working directory was
removed after its measurements were folded into the two stage files; nothing was left behind and
no receipt depends on it. No out-of-repo path appears in any file written, and no file outside
`stage/ScoutGap/` and this report was touched.
