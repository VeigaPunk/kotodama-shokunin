# R8-F10 freshness receipt — priestly garment terminology and the evidential status of the Exodus 28 prescription

- shard: `reports/round-8/targets.json` freshness[9]
- prior row: **R6-08-B**, prior disposition **partial-support** (`corpus/lessons/round-6-sources/08.json`)
- entry: `corpus/knowledge/civilizations/israel-ancient-hebrew.md`, section 7 lines 121–141 in the current file (lines 118–138 at receipt time, before a +3 frontmatter shift; line 125; table lines 129–136; line 138), section 1 line 25 (was 22)
- entry sha256 at receipt: `f25a4b4066f6172afc697a279854ee85ed8a01ee1efdf00097e1d418ed1e80aa` — equals the round-6 baseline hash (`sha256sum` run 2026-10-17T20:14:55Z)
- entry sha256 current (2026-10-17T20:19:26Z): `57fb4bd4f1c0491c7c7851cf1bb435e8a73e29465dfaf6ced07139e9bb43d76e` — the entry was modified in place after the receipt-time hash by the round-8 metadata sweep (`git diff` 2026-10-17: two added frontmatter lines only, `verified-at` and `recheck` from `reports/round-8/metadata/m03-civ-39-57.md`; all content line numbers +3). Every line this receipt cites was re-located in the modified file; no cited content changed.
- accessed-at for every retrieval below: **2026-10-17**
- question: *Check priestly garment terminology and the evidential status of the cited biblical prescription; distinguish a dated transmitted text and its translation from excavated dress or a uniform for all Israelites.*

## Verdict

- **Passage support: retrieved** — 6 passages, 5 distinct sources (two of them the entry's own cited URLs), all fetched fresh in round 8.
- **Whole-claim support: supported, text-side and bounded** — sub-claims (a) *bigdei kehuna* vs the chapter's own *bigdei qodesh*, (b) the named garment terms with their verse anchors, (c) priest-scoped addressees and service scope, (d) the four/eight schema as later Mishnah-level and the whole complex as T-layer prescription all hold against the round-8 retrievals.
- **Not supported by anything retrieved:** that the prescription documents practice, compliance, or any excavated priestly dress.
- Labels kept distinct: round-6 worker verdict `supported` (whole-bounded-claim, `corpus/lessons/round-6-sources/08.json`); round-6 parent disposition `partial-support` (`reports/round-6/parent-reconciliation.json`, and `raw_label` in the JSON receipt); reconciled round-8 disposition `supported-bounded` (recorded here; `reports/round-8/freshness/reconciliation.json` is another shard's file).
- Harness measurement (run 2026-10-17 with `reports/round-8/run-validation.py` functions, output redirected to `/tmp` so the filed `validation.json` stayed untouched): this receipt reads as shape `retrieved`, passage/claim separation true, and counts as one of the round's substantive passages.

## Retrieved passages

**L1 — main text re-fetch.** [mechon-mamre.org/p/pt/pt0228.htm](https://mechon-mamre.org/p/pt/pt0228.htm) (entry's own cited page; JPS 1917 English with pointed Hebrew). Locators: Exodus 28:1, 2, 4, 36, 39, 40, 42, 43.
- 28:2 "And thou shalt make holy garments for Aaron thy brother, for splendour and for beauty." (וְעָשִׂיתָ בִגְדֵי־קֹדֶשׁ)
- 28:4 "… a breastplate, and an ephod, and a robe, and a tunic of chequer work, a mitre, and a girdle; and they shall make holy garments for Aaron thy brother, and his sons"
- 28:36 "… engrave upon it, like the engravings of a signet: HOLY TO THE LORD."
- 28:40 "And for Aaron's sons thou shalt make tunics, and … girdles, and head-tires …"
- 28:42–43 linen breeches "to cover the flesh of their nakedness", worn "when they go in unto the tent of meeting"
- Scope read: every table-row term (ketonet 28:39, mikhnesei vad 28:42–43, avnet 28:39–40, mitznefet/migba'ot 28:39–40, me'il 28:31–35, ephod 28:6–12, hoshen mishpat 28:15–30, tzitz 28:36–38) occurs in the retrieved chapter; addressees are Aaron and his sons "from among the children of Israel" (28:1); the wearing clause is sanctuary-service scoped (28:43).

**L2 — the four/eight classification from the entry's own cited URL.** [mishnah.org/learn/yoma/7/5/](https://www.mishnah.org/learn/yoma/7/5/). Locator: Yoma 7:5 opening and enumeration.
- "Throughout the year the High Priest serves in eight garments, and the common priest serves in four: In a tunic and trousers and a mitre and a belt. The High Priest adds another four garments … A breastplate, and an ephod, and a robe, and a frontplate."
- Round 6 used a different URL (he.wikisource); this round-8 leg uses the URL the entry itself lists. The same mishnah also ties the eight garments to Urim-and-Thummim consultation — an institutional coupling beyond the entry's table.

**L3 — peer-reviewed scholarship.** [Religions (MDPI) 13(12):1220, 15 December 2022](https://www.mdpi.com/2077-1444/13/12/1220). Sections "1. Biblical Accounts of Priestly Garments", "3. Mishnah on Priestly Garments", "4. Amoraic Literature…".
- "Exodus chapters 28 and 39 each offer expansive accounts of the priestly vestments … with a set of four items prescribed for all priests and several others specifically for the High Priest."
- "No language relating to atonement appears in descriptions of the priestly garments in biblical literature, with the exception of the case of the forehead-plate."
- "No expiatory role is applied to these priestly garments in early (Tannaitic, 2nd–early 3rd century CE) rabbinic literature … This avoidance of expiatory language shifts when we look at the Amoraic period (late 3rd–6th century CE)."
- Read: the standard-priest set is priest-scoped; the atoning reading is a later (Amoraic) layer, exactly the layer-separation the entry's caution requires.

**L4 — dated excavation, Iron Age (non-priestly).** [PLOS ONE 16(1): e0245897, 28 January 2021, via PMC7842898](https://pmc.ncbi.nlm.nih.gov/articles/PMC7842898/) (Sukenik, Iluz, Amar, Varvak, Shamir, Ben-Yosef).
- "The samples originated from excavations at the extensive Iron Age copper smelting site of 'Slaves' Hill' (Site 34), which is tightly dated by radiocarbon to the late 11th–early 10th centuries BCE."
- "textiles are rare in the archaeological record … their preservation requires special conditions"; the Timna finds are "dozens of fragments", the largest Iron Age assemblage in the Southern Levant, from a semi-nomadic, early-Edomite industrial context.

**L5 — dated excavation, Middle Bronze Age dyed object.** [Journal of Archaeological Science: Reports (2024), ScienceDirect abstract page](https://www.sciencedirect.com/science/article/abs/pii/S2352409X24003018) (Sukenik et al., Cave of Skulls; DOI 10.1016/j.jasrep.2024.104673 per the phys.org companion record).
- "the fabric of the red-dyed textile discussed in this article … was radiometrically dated to 3540 ± 30 years BP, calibrated … to 1954–1767 BCE"
- "The red textile in question (IAA no. 2017–9071 …) includes two small fragments (1.4 cm × 1.8 cm; 0.8 cm × 1 cm)"
- "Despite the fact that these textile fragments measure no more than 1.5 cm, their significance is immense, as they bear witness to the utilization of scale insects for dyeing textiles during the Middle Bronze Age, the earliest of its kind known to date."
- Read: the object is real, dated and analysed to dye species (*Kermes vermilio*) — but it is a ~1.5 cm fragment establishing dye technology, elite consumption and trade, **not** an Israelite priestly garment. Popular framing ("fabrics of the biblical Tabernacle and the priestly garments", israelhayom.com 2024-07-18) is press framing, not the paper's claim.

**L6 — dated text vs translation (edition provenance).** [mechon-mamre.org/p/pt/pt0.htm](https://mechon-mamre.org/p/pt/pt0.htm).
- "According to the Masoretic Text and the JPS 1917 Edition"; the English is "based on the electronic text (c) by Larry Nelson" with site corrections.
- Read: the display names its layers — transmitted consonantal text, Masoretic vocalization, 1917 translation, HTML edition — so it is a dated transmitted text and its translation, not a manuscript.

## Documented access failures (attempted command + status, 2026-10-17)

| Attempted | Status |
|---|---|
| `FetchURL https://ore.exeter.ac.uk/repository/bitstream/handle/10871/27594/WagstaffB_TPC.pdf?sequence=2&isAllowed=y` | network error: "Failed to extract meaningful content from the page. The page may require JavaScript to render." |
| `FetchURL https://ore.exeter.ac.uk/repository/handle/10871/27594` | same extraction failure |
| `FetchURL https://mechon-mamre.org/p/pt/ptpref.htm` | HTTP 404 Not Found |

## Search sweeps (2026-10-17)

1. "excavated Iron Age Israelite textiles Judean garment archaeology tunic find" — Timna papers, Shamir first-century CE burial textile, Nahal Omer tunic (8th–9th c. CE), Wagstaff Exeter thesis, ASOR 2018 Timna abstract; no Iron Age Israelite priestly ensemble.
2. "priestly garments Exodus 28 prescription versus practice archaeology evidence scholarly" — surfaced L3 and devotional sites (not used as evidence).
3. "excavated high priest garments archaeology textile Jerusalem found evidence priestly vestments survived" — later/other-context vestments (Anglo-Saxon, early modern Catholic), L5, and a BAS item theorizing a Temple-Mount find "may have been one of the bells sewn to the high priestly garments" (**to-verify**; primary report not retrieved, not absorbed).
4. "Timna Valley Iron Age textiles assemblage Sukenik Ben-Yosef published paper radiocarbon" — located L4.

**Negative claim (sweep-bounded):** no excavated Iron Age Israelite priestly-garment ensemble surfaced in these sweeps; nearest dated textile evidence is fragmentary and non-priestly (L4, L5). Bounded to these sweeps — a search-sweep finding, not an exhaustive bibliographic proof; the entry's own wording ("this entry collates no such dated ensemble") is consistent with it.

## Limits retained

No recovered Iron Age priestly garment, no compliance evidence, no fibre/cut certainty; gem names and silhouettes remain philological reconstructions; prescription ≠ practice and priests ≠ all Israelites stay intact.

## Counting commands

- `python3 reports/round-8/run-validation.py` (round acceptance harness; not authored by this shard)
- `sha256sum corpus/knowledge/civilizations/israel-ancient-hebrew.md` (2026-10-17T20:14:55Z) → `f25a4b4066f6172afc697a279854ee85ed8a01ee1efdf00097e1d418ed1e80aa` (= round-6 baseline); re-run 2026-10-17T20:19:26Z → `57fb4bd4f1c0491c7c7851cf1bb435e8a73e29465dfaf6ced07139e9bb43d76e` (post metadata-sweep frontmatter addition)
