- Seat: C05 | auditor (completion seat) | claim C | date 2026-10-19 | baseline ac47c78

# C05 — independent audit of the four myth-symbol entry drafts

Round 42 (regimen 2, loop 1, position 10), seat **C05**, role **auditor** (completion seat: the
original C05 failed at dispatch), claim **C**. Mission: audit `cov/C01-entry-1.md`,
`C02-entry-2.md`, `C03-entry-3.md`, `C04-entry-4.md` against the established entry contract —
head-block fields, source-pointer resolution at HEAD `ac47c78`, couples resolution, decision-record
presence, absence-sweep honesty, and five fabrication spot-checks per entry — folding the landed
verifiers C07 and C08 and A01's scan instrument for the bleed leg.

- Lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`; `git rev-parse HEAD` →
  `ac47c7861b0b2cdb8e3c2f985c2220406d3ba0b4` == declared baseline `ac47c78`
  (`reports/round-42/claims.json:7`); `git log --oneline -1` → the round-41 admission commit;
  `git status --porcelain` → `?? reports/round-42/` only, no corpus/tool/README byte changed.
- **Writes: this file only**, plus gitignored `.scratch/c05/` (extractors and staged blocks). No
  `corpus/**` byte, no `tools/**` byte, no filed round-1..41 byte, no telemetry file. No commit,
  push, install, or network. **No `reports/round-*/run-validation.py` was executed**; the only
  filed instruments run read-only were `reports/round-42/adj/A01-scan-instrument.py` and
  `reports/round-28/readme/sweep.py` was *not* needed for the entry legs.
- **Canon: NON-CANON.** This seat audits bytes and files defects; it admits no entry, certifies no
  round, promotes nothing, clears nothing (`PROVINCE.md`; `corpus/QUALITY.md`). A green reading is a
  structural reading of named digests — never a verdict on the scholarship, never canon.
- **Literature legs are not audited for truth.** None of the four entries was fetched externally
  (no network in this seat, and the entries themselves declare `(to-verify)`). The spot-checks below
  verify only that each cited **in-corpus** line says what the entry claims it says.

## 0. Verdict at a glance

| entry | declared landing path | contract legs | absence sweeps | spot-checks | overall |
|---|---|---|---|---|---|
| C01 | `myth-symbol/mineral-stone-symbolism.md` | **pass** (9 head fields; required 6/6; 0 unresolved pointers/couples; 16 DR ids) | reproduce exactly | 10/10 match | **PASS-with-named-defects** — S2 staging fence; S2 duplicate topic/path with C04 |
| C02 | `myth-symbol/purity-pollution-systems.md` | **pass** (7 head fields; required 6/6; 0 unresolved; 15 DR ids) | zero-counts reproduce; three nonzero counts wrong unit | 9/9 match | **PASS-with-named-defects** — three S3 count defects |
| C03 | `myth-symbol/sacred-topography-pilgrimage.md` | **pass** (9 head fields; required 6/6; 0 unresolved; 12 DR ids + 1 cross-ref) | main counts reproduce; two literature probes fail; one contradictory sentence | 12/13 match | **PASS-with-named-defects** — S3 probes + S3 locator |
| C04 | `myth-symbol/mineral-stone-symbolism.md` | **pass** (8 head fields; required 6/6; 0 unresolved; 10 DR ids) | reproduce except one topic-owner probe | 14/16 match | **PASS-with-named-defects** — S2 duplicate topic/path + S3 locators |

**Round-level reading.** The four drafts are individually contract-valid, but they declare only
**three distinct topics and three distinct landing paths**: C01 and C04 both claim the lithic
register at `mineral-stone-symbolism.md`. Claim C's `myth-symbol 23 → 27` needs four distinct new
entries; as filed it has three. This is the round's count-blocking defect (§6 D1), and it is a
disposition for the integrator, not a verdict this seat can make.

## 1. Audited bytes and digest pins

Fragment pins are this seat's own `sha256` of the whole fragment; block pins are given under the
**named staging shape** so a later reader can reproduce the convention rather than compare
incompatible hashes. The trailing-newline convention accounts for every one-byte difference below.

| entry | fragment (lines / bytes / sha256) | block under the r35 stager regex | block by line range | author's pin |
|---|---|---|---|---|
| C01 | 538 / 129 691 / `b7140ce069ee55382c61326f4c6fa74a6f02d458506e1b2f60623f5f3d43faa3` | **0 matches** — 4-backtick fence (§6 D2) | lines 51–266: 216 text lines / 55 102 B / `7f102a5e376ec0e5644bf862a76c9aa0a8398e5bacab7ff495579b674d8b4755` | `6999a912…` 55 101 B / 215 `wc -l`, reproduces exactly on `.scratch/c01/entry-mineral.md` |
| C02 | 235 / 61 553 / `474c7fac52f4f6ef239e206f1e309df255306fe11c880b98df83625f46740938` | 1 match: 49 977 B / 188 newlines / `14455ddce6deb33a2ccf3b78cc2fd8590bc43f8faf9f3cab9cb7e7854c35b942` | lines 14–200 without the blank line: 49 976 B / `02b3536c…` | `14455ddc…` — **reproduces exactly** under the regex |
| C03 | 225 / 72 611 / `d7daa54b313233ed61635745ae33b486ff6117c6e0afa3917f9556d5d1b0bfae` | 1 match: 63 165 B / 182 newlines / `5ab039f10b6ecc3e49c71f3ea12879afd52d91cab6af42a5a73019823f841dc2` | lines 15–195: 63 164 B / `241113b5…` | no block digest declared |
| C04 | 295 / 82 336 / `2b8eb533dbfc0a89a84f7c0cb304f47e25ede44bc4af171ac3ee844b1fa63ac7` | 1 match: 61 885 B / 193 newlines / `e88cb1676516589bc33dca70d67bebbd03614415242c85e3d4f70f10a74fd671` | lines 54–245: 61 884 B / `c99f44ca…` | `e88cb167…` 193 / 61 885 — reproduces exactly on `.scratch/c04/stage/corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` |

Reading the table:

- **C01's pin is valid but the fence is not stageable.** The 55 101-byte pin equals the author's
  scratch artifact; the 4-backtick block captures 55 102 bytes under a line-range read. The
  one-byte difference is the trailing newline, not an edit.
- **C02's pin is valid and C08's D2-d is rejected.** `re.findall(r"^```(?:markdown|md)\s*$([\s\S]*?)^```\s*$", text, re.M)`
  on `C02-entry-2.md` returns exactly one block, 49 977 bytes, 188 newlines, sha256 `14455ddc…`.
  C08 §8's "no convention yields `14455ddc…`" search missed this capture (it discarded the blank
  line before the closing fence). No re-stamp is owed on this leg.
- **C03 declares no block digest.** Its `.scratch/c03/anchors.py` is a range/needle instrument, not
  a pin; the durable reading is the stager capture above.
- **C04's pin is valid.** `e88cb167…` is the stager's output (the fence block plus the stager's
  trailing newline). The block content itself is `c99f44ca…`; both readings are consistent and
  neither is stale.
- **C01's spare purity block** (5-backtick fence, `:291–516`) pins `5ba3a9fb…` / 57 899 B / 223
  `wc -l`, reproducing exactly on `.scratch/c01/entry-draft.md`. It is marked SPARE and is **not**
  this seat's deliverable; it must not be staged alongside C02.

## 2. Head-block and contract legs

| leg | C01 | C02 | C03 | C04 |
|---|---|---|---|---|
| `- topic:` | yes, single-line | yes, single-line | yes, single-line | yes, single-line |
| `- gap:` / `- gap filled:` | `gap filled` | `gap filled` | **both** | `gap filled` |
| `- sources:` | yes | yes | yes | yes |
| `- verified-at:` (ISO) | `2026-10-19` | `2026-10-19` | `2026-10-19` | `2026-10-19` |
| `- recheck:` | yes | yes | yes | yes |
| `- couples:` | yes, single-line | yes, single-line | yes, single-line | yes, single-line |
| decision record | §10, `DR-MS-01…16` | §13, `DR-PP-01…15` | §10, `DR-ST-01…12` (+ `DR-TR-02` cross-ref) | §11, `DR-MS-01…10` |
| backticked path tokens | 75 unique: 50 direct, 21 unique-basename, 2 glob, 2 dir, **0 unresolved** | 40: 28 direct, 11 basename, 1 dir, **0 unresolved** | 59: 50 direct, 5 basename, 2 glob, 2 dir, **0 unresolved** | 68: 52 direct, 12 basename, 2 glob, 2 dir, **0 unresolved** |
| explicit `name.md:NN` refs | 66 / 63 bound / **0 out of range** | 137 / 137 / **0** | 161 / 160 / **0** | 149 / 149 / **0** |
| couples refs | 30 / **0 unresolved** | 35 / **0 unresolved** | 39 / **0 unresolved** | 44 / **0 unresolved** |

Resolver rule (reproducible): extract every backticked token ending `.md` or beginning
`corpus/|reports/|tools/|examples/|templates/`; strip a `:NN` or `:NN-NN` suffix; one-level brace
expansion; try the path as written, then under `corpus/knowledge/` and `corpus/`, then a unique
basename; glob and directory tokens are excluded from the resolution count. Both the **C01** and
**C03** head blocks carry a `- scope:` line in addition; **C02** carries no `- scope:` (not a
required field) and **C04** carries one. The required field set is complete in every case; `- gap:`
and `- gap filled:` are alternatives and the latter is present in all four.

## 3. Couples resolution and the N6 wrapped-field check

`reports/round-42/adj/A01-scan-instrument.py` was run read-only on each staged block. The instrument
uses block extraction (field plus continuation lines), the adopted `.md` token rule, and a
direct → unique-basename → unresolved/ambiguous classification.

| entry | couples line | refs | direct | extless | unresolved | ambiguous | wrapped | language hits | PROVINCE-screen hits |
|---|---|---|---|---|---|---|---|---|---|
| C01 | 1 line, 30 refs | 30 | 30 | 0 | 0 | 0 | False | 0 | 0 |
| C02 | 1 line, 5 051 chars | 35 | 35 | 0 | 0 | 0 | False | 1 (benign) | 0 |
| C03 | 1 line, 39 refs | 39 | 39 | 0 | 0 | 0 | False | 0 | 0 |
| C04 | 1 line, 44 refs | 44 | 44 | 0 | 0 | 0 | False | 0 | 0 |

**N6 does not bite these entries.** The known N6 defect is the wrapped-field zeroing; all four
`- couples:` fields are single-line and the instrument reports `wrapped=False` for each, so no field
was silently truncated. The 21/11/5/12 unique-basename resolutions are ordinary in-partition
shorthand, not unresolved pointers. A01 §4's C02 reading (36 distinct tokens, 35 direct, 0
unresolved, one benign `promoted` at block line 126) is reproduced; A01's limitation is that it
scored only C02, so this table extends its instrument to C01/C03/C04 as the mission asks.

## 4. Absence-sweep honesty

Every claimed command was re-run from the lane root at `ac47c78` under
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`. The **zero-counts are the load-bearing
evidence**; the nonzero counts are reported as the draft states them, with the unit named.

### C01 — reproduces exactly

| claimed | measured | reading |
|---|---|---|
| filenames `mineral\|stone\|gem\|lithic` → 0 | **0** | ok |
| `lapidary` → 2 files | **2** | ok (`symbolism-synthesis-method.md:29`; `rome.md:33` epigraphic) |
| `gemstone` → 2; `precious stone` → 1 | **2; 1** | ok |
| `mineral` → 6; `lithic` → 24 | **6; 24** | ok |
| topic-line sweep → 2, both false positives | **2** (`sound-symbolism.md` "Dingemanse"; `death-afterlife-eschatology.md` "management") | ok — honestly labelled |
| myth-symbol 23 / total 220 | **23 / 220** | ok |

### C02 — zero-counts reproduce; three nonzero counts carry the wrong unit

| claimed | measured | reading |
|---|---|---|
| topic `pollution`, `impurity`, `defilement`, `contagion`, `purification`, `lustration`, `abomination` → 0 each | **0 each** | ok |
| combined purity pattern → 0; `boundary maintenance` → 0 | **0; 0** | ok |
| `taboo` → **122 files** | **121** case-sensitive; 122 only with `-i` | **case-insensitive file count reported as case-sensitive** |
| `taboo` topic-owners → 8 | **8** | ok |
| `purity` → **41 files** | **39** case-sensitive; 41 only with `-i` | **same unit error** |
| `purity` topic-owners → 2 | **2** | ok |
| `Douglas` → **31 files** | **13 files**; 31 matching lines; 32 occurrences | **line/occurrence count reported as a file count** |
| `Douglas (1966)` → 6 | **6** | ok |

### C03 — main counts reproduce; two literature probes fail as stated; one sentence contradicts itself

| claimed | measured | reading |
|---|---|---|
| `pilgrim` → 23 files, 7 in myth-symbol | **23 / 7** | ok |
| `shrine` → 49; `procession` → 30 | **49 / 30** | ok |
| `sacred geograph` → 14 | **14** | ok |
| topic-owner test → 3 hits, **none in myth-symbol** | **3 hits: `arabia-pre-islamic.md`, `architecture-settlement-lexicon.md`, `myth-symbol/plant-symbolism.md`** | **the third hit is in myth-symbol**; the same sentence lists it. The conclusion (none owns the *pilgrimage institution*) survives; the phrase "none in myth-symbol" does not |
| six absence probes → 0 each | **0 each** | ok |
| literature probes → 0 each, `Coleman` → 1 | `Eade` **138**, `Sumption` **69**; `Morinis`/`Bhardwaj`/`Stoddard`/`Elsner`/`Ibn Jubayr`/`Canterbury Tales`/`Compostela`/`tīrtha`/`ziyarat`/`Kumano`/`Saikoku`/`ampulla`/`Egeria` → 0; `Coleman` → 1 | **two probes fail as literal greps**: `reader` contains "eade", `consumption`/`assumption` contain "sumption". Word-boundary `grep -rlw Eade` → **0** and `grep -rlw Sumption` → **0**; the underlying absence is true, the stated command is not |

### C04 — table reproduces except one topic-owner probe

| claimed | measured | reading |
|---|---|---|
| `lapidary` myth 1 / all 2; `gemstone` myth 0 / all 2 | **1/2; 0/2** | ok |
| `gem register\|stone register` 0; `baetyl\|bethel` 0; `quarry` myth 0 / all 5 | **0; 0; 0/5** | ok |
| `mineral` myth 1 / all 6; `lithic` myth 3 / all 24 | **1/6; 3/24** | ok |
| `precious stone` 1; `sacred stone` 1; `meteorite` 1; `obsidian` 2 | **1; 1; 1; 2** | ok |
| `jade` myth 1 / all 14 / topic-owners 2 | **1/14/2** (`maya-classic.md`, `china-shang-zhou.md`) | ok |
| `turquoise` 5; `mine` myth 10 / all 129 / topic-owner 1 | **5; 10/129/1** | ok |
| topic-owner test `mineral/gem/lapidary/lithic/precious/quarry` → 0 each | `gem` → **2** (`sound-symbolism.md` "Dingemanse"; `death-afterlife-eschatology.md` "management"); the other five → 0 | **one probe fails**: both hits are substring artefacts, but the claim "0" does not reproduce as written |

## 5. Fabrication spot-checks (in-corpus citations only)

Each row is a cited `path:line`, the claim the entry makes for it, and the line actually read.
External works are not checked for truth; they are the entries' declared `(to-verify)` legs.

### C01 — 10/10

| citation | claim | read | verdict |
|---|---|---|---|
| `symbolism-synthesis-method.md:23` | five canonical registers | "the five canonical registers: color, animal, number, celestial body, direction" | match |
| `:29` | lapidary is a named package component | "bestiary + lapidary + numerology + heraldic code" | match |
| `plant-symbolism.md:15` | "a plant cannot flee" | exact | match |
| `color-symbolism.md:11` | colour carries no meaning without a code | "A color never carries a meaning by itself; a **code** does" | match |
| `funerary-material-culture.md:22` | Pliny 36.27 *sarcophagus* stone of Assos | exact, with the forty-day report and Bostock & Riley | match |
| `china-shang-zhou.md:106` | heirloom rule | "an old object in a later burial does not imply manufacture during the burial's dynasty" | match |
| `maori.md:20` | named knowledge holders / local checking | exact | match |
| `siam-thai.md:126` | Emerald Buddha palladium + anti-universal caveat | exact | match |
| `ritual-garments.md:59` | choshen 12 stones, zodiac attributed to Philo/Josephus | exact | match |
| `maya-classic.md:127` | "not every jade object expresses all associations" | exact | match |

### C02 — 9/9

| citation | claim | read | verdict |
|---|---|---|---|
| `symbolism-synthesis-method.md:40` | Douglas anomaly row, "take the anomaly engine only" | exact | match |
| `:48` | `pure/impure` among the polarity axes | exact | match |
| `:68` | anomaly picks the taboo | exact | match |
| `animal-symbolism.md:69` | pig taboo, two rival explanations | exact | match |
| `plant-symbolism.md:20` | "Do not re-derive the machinery; couple to that file and change the trigger" | exact | match |
| `death-afterlife-eschatology.md:49` | corpse status as a separate variable | exact | match |
| `bathing-and-body-hygiene.md:50` | status/contamination split, "must not be merged" | exact | match |
| `israel-ancient-hebrew.md:150` | intersecting classifications | exact | match |
| `cuisine-food-lexicon.md:8` / `bathing-and-body-hygiene.md:5` | Milgrom registered | both lines carry Milgrom | match |

### C03 — 12/13

| citation | claim | read | verdict |
|---|---|---|---|
| `ritual-liminality.md:6` | Turner & Turner 1978, *Image and Pilgrimage* | exact (later in the same source line) | match |
| `:85` | Hajj / ihram / tawaf row | exact | match |
| `:86` | Kumbh Mela + attendance caution | exact | match |
| `cosmology-cosmography.md:27` | cosmography "walked (processions, pilgrimage)" | exact | match |
| `:68` | Cusco ceque, 41 lines, 328 huacas | exact | match |
| `direction-symbolism.md:112` | tawaf, seven circuits | exact | match |
| `plant-symbolism.md:45` | Bodhi tree, vegetatively propagated, "place with a lineage" | exact | match |
| `architecture-settlement-lexicon.md:78` | *scrinium* → shrine | exact | match |
| `transport-mobility-lexicon.md:35` | Qhapaq Ñan, 40 000 km, *tambos*, *qullqas* | exact | match |
| `:52` | Q'eswachaca rewoven annually | exact | match |
| `arabia-pre-islamic.md:122` | Crone's challenge to the trade projection | exact | match |
| `divination-omen-systems.md:121` | Delphi as a state oracle | exact | match |
| `greece-classical.md:65` | "Greek tomb cult" | line 65 is **Olympian vs Olympic terminology**; tomb cult is at `:97–98` | **wrong locator** |

### C04 — 14/16

| citation | claim | read | verdict |
|---|---|---|---|
| `symbolism-synthesis-method.md:29` | lapidary package sentence | exact | match |
| `animal-symbolism.md:13` | White 1954 / Fox-Davies 1909 | exact | match |
| `plant-symbolism.md:3` | flora gap statement | exact | match |
| `cosmology-cosmography.md:37` | pillar row: djed, Ame-no-mihashira, omphalos, qutb | exact | match |
| `sumptuary-law-rank-display.md:53` | Qing hat-button finials graded gem-to-metal 1st→9th | exact (same long line, after the Ming *buzi*) | match |
| `craft-artisan-lexicon.md:44` | *tamahagane*, *kawagane/shingane*, *hada* | exact | match |
| `:47` | GIA 4Cs, "invented grading language … one century" | exact | match |
| `:3` | Kaogongji four-factor formula, *qiao/zhuo* | exact | match |
| `timekeeping-instruments.md:24` | Campus Martius obelisk, Pliny 36.71–72 | exact | match |
| `writing-systems.md:52` | Proto-Sinaitic at Serabit el-Khadim | line names Serabit and "Canaanite semilingual miners"; **the word "turquoise" appears nowhere in the file** | **unsupported qualifier** ("a turquoise-mining site") |
| `maya-classic.md:127` | jade caveat | exact | match |
| `maori.md:20` | named knowledge holders | exact | match |
| `cosmology-cosmography.md:132` | "Delphic omphalos and Quechua *qusqu*" | line 132 is **direction lexemes**; omphalos is at `:37`/`:43`; *qusqu* is at `direction-symbolism.md:66` (which points back to cosmology §9, where the token does not appear) | **wrong locator** |
| `architecture-settlement-lexicon.md:95` | *sulcus primigenius* / *pomerium* | exact | match |
| `animal-symbolism.md:53` | spirit-helper slot | exact | match |
| `color-symbolism.md:114` | anti-porting craft reading | exact | match |

**C04's K02 correction is itself correct.** `reports/round-42/scout/K02-myth-gaps.md:176,:525` lists
`culture-material/vessel-container-lexicon.md` as carrying "Pliny 36.27 again"; `grep -n '36.27'
corpus/knowledge/culture-material/vessel-container-lexicon.md` → **no output** (exit 1). C04's
`- verified-at:` reports this accurately; the scout fragment is the filed byte at fault, and C04
did not repeat the error.

## 6. Severity-ranked defects

Severity: **S1** = entry-content contract failure or fabricated source; **S2** = apply/count
blocking, must be resolved before landing; **S3** = named defect, apply-as-is with correction.

### S1 — none

No missing required head field, no unresolved source pointer, no unresolved couples target, no
missing decision record, and no fabricated external source was found. Every spot-checked in-corpus
citation except the three named below reads what the entry claims.

### S2 — apply/count blocking

**D1. C01 and C04 declare the same topic at the same landing path.**
- **Statement.** `C01-entry-1.md:1–4` declares `myth-symbol/mineral-stone-symbolism.md` (the purity
  draft is a marked spare); `C04-entry-4.md:5` declares the identical path. The four drafts
  therefore have **three distinct topics and three distinct paths**, not four.
- **Evidence.** C01:1–4; C04:5; C04:17; C08 §11 (D3) independently; K02 §R1 (lithic) and §R4
  (purity dispositioned to C02). The stager takes the first `corpus/knowledge/...` token as its
  target (C08 §7 hazard), so applying both paths silently overwrites one.
- **Why it blocks.** Claim C needs `23 → 27`, i.e. four distinct new files. Two files at one path
  give 26; two files at two slugs give 27 files but still only three distinct topics, and would
  leave the lithic register owned twice — the partition's one-owner rule is violated either way.
- **Disposition (integrator).** Admit **one** lithic entry; either re-topic the other to the
  unclaimed R2 (dream/vision/trance) as new bytes, or drop it and record that claim C delivered
  three entries. Do **not** land both. C01's spare purity block must not be staged alongside C02.

**D2. C01's deliverable is fenced with four backticks and is invisible to the house stager.**
- **Statement.** C01's deliverable opens at `:50` with ` ````markdown ` and closes at `:267` with
  ` ```` `. The r35 stager regex `^```(?:markdown|md)\s*$` matches **0 blocks** on the fragment
  (C02/C03/C04 each match 1). The block is extractable only by line range.
- **Evidence.** Reproduced command in §1; C01's own self-check says the entry contains no triple
  backtick, so the four-backtick fence was not needed. C04's self-audit records the same R01-10
  failure on its first draft and the fix (three backticks).
- **Fix.** Change the two C01 fence lines to three backticks (safe: no internal triple backtick), or
  have the integrator extract lines 51–266 and stage those bytes. Until then C01 is
  operationally not stageable by the standard pipeline.

**D3. C04's slot map misreads C01's current fragment.**
- **Statement.** `C04-entry-4.md:17` says "C01 → `purity-pollution-codes.md`" and cites
  `C01-entry-1.md:1–4`. C01's current `:1–4` declare `mineral-stone-symbolism.md` and retain the
  purity draft as a spare. The stale read is the proximate cause of D1.
- **Evidence.** C01:1–4 read live; C08 §11 attributes the race to C01's later re-slot. The citation
  is false against current bytes even though the write-order explanation is real.
- **Fix.** Correct the slot map in C04's fragment; the integrator must route on current bytes, not
  on C04's summary.

### S3 — named defects, apply-as-is with correction

**D4. C02's three nonzero counts carry the wrong unit.** `taboo` 121 case-sensitive / 122
case-insensitive (entry says 122 files); `purity` 39 / 41 (entry says 41); `Douglas` 13 files, 31
matching lines, 32 occurrences (entry says 31 files). The zero-counts reproduce exactly, so the gap
argument is intact. Fix: state the exact command or the correct counts (121 / 39 / 13). C07 D2 and
C08 D2-a/b/c independently reached the same reading.

**D5. C03's `Eade` and `Sumption` probes do not reproduce as stated.** Literal `grep -ril` gives
**138** and **69** files (substrings "reader", "consumption"/"assumption"); word-boundary
`grep -rlw` gives **0** and **0**. The underlying absence is true; the stated probe is false. Fix:
report the word-boundary command, or quote the `0` with the boundary condition.

**D6. C03's "none in myth-symbol" contradicts its own hit list.** The topic-owner test returns
`myth-symbol/plant-symbolism.md` (its `- topic:` contains "shrine"), and the same sentence lists
that file as the third hit. Fix: say "none of the three owns the *pilgrimage institution*; the
plant entry owns the grove as flora", which is what the paragraph means.

**D7. C03 cites `greece-classical.md:65` for tomb cult.** Line 65 is Olympian/Olympic terminology;
the tomb-cult material is `:97–98` ("Distinguish hero cult … from archaeological tomb cult"). Fix
the two occurrences (§2 P3 and §3 site kind 4) to `:97–98`.

**D8. C04's `gem` topic-owner probe returns 2, not 0.** Hits are `sound-symbolism.md` ("Dingemanse")
and `death-afterlife-eschatology.md` ("management") — substring artefacts, not owners. The "no
topic-owner" conclusion holds. Fix: use word boundaries, or report the two false positives the way
C01 does.

**D9. C04's "turquoise-mining site" is unsupported by `writing-systems.md:52`.** The line names
Serabit el-Khadim and "Canaanite semilingual miners"; the word "turquoise" appears **nowhere** in
the file. The core claim (a mining site on the script's route) is supported; the qualifier is
external. Fix: delete "turquoise-mining", or mark it `(to-verify)` / cite an external source.

**D10. C04's `cosmology-cosmography.md:132` locator is wrong.** Line 132 is direction lexemes;
omphalos is at `:37`/`:43`; *qusqu* is at `direction-symbolism.md:66`. Fix both occurrences (§6 and
the `- couples:` locator list) to `cosmology-cosmography.md:37` for omphalos and
`direction-symbolism.md:66` for *qusqu*.

**D11. C01 and C04 share the `DR-MS-*` decision-id namespace.** C01 defines `DR-MS-01…16`; C04
defines `DR-MS-01…10` with different semantics (e.g. C01 `DR-MS-02` = five sign-properties; C04
`DR-MS-02` = source regime). If both survive in any form, cross-references are ambiguous. Fix:
re-prefix one series (e.g. `DR-LT-*` for the loser) or ensure only one lithic entry lands.

**D12. Digest-shape note, not a defect.** C01's pin is the 55 101-byte scratch file; the 4-backtick
capture is 55 102 bytes; C03's stager capture is 63 165 bytes and its line-range capture 63 164;
C04's stager capture is 61 885 and its block content 61 884; C02's stager capture is 49 977. Every
difference is the trailing newline. The integrator should re-derive at apply time and pin the
**staged** bytes, not the fence text; no author is owed a re-stamp except C01 if it is re-fenced
(the block bytes do not change when only the fence marker changes).

## 7. Fold of the landed verifiers

- **C07 — agree.** C07 §6's contract reading of C02 (`PASS/review`, 0 contract defects, all 11
  spot-checked anchors reading what C02 claims) matches this audit. C07's **D2** is confirmed
  exactly: `taboo` 121/122, `purity` 39/41, `Douglas` 13 files (31 lines / 32 occurrences). C07's
  **D1** (the declared README vector `25/23/27/25/24/94` sums to 218 and names the wrong slot) is
  outside the entry contract but is agreed context; the correct vector is `25/27/25/29/24/94`.
- **C08 — agree on D1 and D3; reject D2-d.**
  - **D1** (declared footer vector) — agreed; not re-run here because it is a README leg, not an
    entry leg. C07 §5 and C08 §5 reached the same reading independently; each also cites R02 and
    X01, which this seat did not read.
  - **D3** (four entries, three distinct landing paths) — agreed, and sharpened: it is **three
    distinct topics**, not only three paths. Landing both lithic drafts at two slugs would still
    not give four distinct entries.
  - **D2-d** (C02's `14455ddc…` pin "does not reproduce") — **rejected.** The exact stager regex
    named in C02's self-audit returns one block, 49 977 bytes, 188 newlines, sha256 `14455ddc…`.
    C08's 8 × 41 × 3 search missed the blank line before the closing fence. No re-stamp is owed.
  - C08 §8/§9's contract verdicts (C02 and C03 `pass=True`, `clean=False`, 0 contract defects) are
    agreed; this audit adds the named S3 defects C08's spot-check set did not include (C03
    `greece:65`, C03 `Eade`/`Sumption`; C04 `writing:52`, `cosmology:132`). C08 did not audit C01 or
    C04 by lot, so no disagreement there.
- **A01 — agree, and extended.** A01 §4's C02 verdict (couples green, one benign `promoted` at
  block line 126, 0 PROVINCE hits) is reproduced. Running A01's instrument on C01/C03/C04 gives
  30/39/44 refs, 0 unresolved, 0 ambiguous, 0 extless, `wrapped=False`, 0 language hits, 0
  PROVINCE hits — so the bleed leg is green for all four, and the N6 wrapped-field defect does not
  affect any of them. A01's F-A01-1 (extension-less naming blind spot) does not bite these drafts:
  all four use full `.md` tokens in the couples field (C01 30/30, C02 35/35, C03 39/39, C04 44/44).
- **C08 §10/§11 row bytes.** C08's block digests (`7f102a5e…`, `02b3536c…`, `241113b5…`,
  `c99f44ca…`) are the line-range readings and match this audit's line-range column; C02's and
  C04's author pins are the stager captures and also match. The two readings are one byte apart by
  trailing newline, not contradictory.

## 8. Overall verdict per entry

- **C01 — PASS-with-named-defects.** Contract legs pass (9 head fields; required 6/6; 0 unresolved
  pointers; 0 unresolved couples; 16 decision rows; all claimed sweeps reproduce; 10/10 citations
  match). It is not a clean pass: the deliverable uses a four-backtick fence the house stager cannot
  see (D2), and it duplicates C04's topic and landing path (D1). The bytes are contract-valid; the
  fragment is not auto-stageable and its slot is contested.
- **C02 — PASS-with-named-defects.** Contract legs pass (7 head fields; required 6/6; 0 unresolved
  pointers; 0 unresolved couples; 15 decision rows; zero-counts reproduce; 9/9 citations match;
  digest pin reproduces). The only defects are the three count-unit errors (D4), all S3 and none
  load-bearing.
- **C03 — PASS-with-named-defects.** Contract legs pass (9 head fields; required 6/6; 0 unresolved
  pointers; 0 unresolved couples; 12 decision rows + one cross-reference; main counts reproduce;
  12/13 citations match). Defects: two literature probes fail as stated (D5), one contradictory
  sentence (D6), one wrong locator (D7). All S3.
- **C04 — PASS-with-named-defects.** Contract legs pass (8 head fields; required 6/6; 0 unresolved
  pointers; 0 unresolved couples; 10 decision rows; most counts reproduce; 14/16 citations match;
  staged pin reproduces). Defects: duplicate topic/path and false slot map (D1/D3, S2), plus four S3
  items (D8–D11).

**No entry is FAIL on the entry contract.** Each has the required head block, resolvable pointers
and couples, a decision record, and a gap statement; none fabricates an external source. The S2
defects are apply/count blockers, not content failures. If the integrator's only apply path is the
r35 stager, **C01 is operationally FAIL-to-stage until re-fenced**; that is a pipeline verdict, not
a scholarship verdict.

**Round-level.** The audit leg is 4/4 contract-pass-with-named-defects. The entry-count leg is
**3/4 distinct topics**. Claim C's `23 → 27` is therefore **not satisfiable as filed**: the
integrator must either (a) admit one lithic entry and commission a genuinely new fourth topic (R2
dream/vision/trance is unclaimed), or (b) admit three entries and record the shortfall. Landing both
C01 and C04 — at one path or two — does not satisfy the claim.

## 9. Owed

- **C01** — re-fence the deliverable to three backticks (or integrator extracts lines 51–266);
  correct the "215 lines" note to name the scratch-file shape; do not stage the spare purity block.
- **Integrator** — dispose of D1: pick one lithic entry, and either re-topic the other to R2 as new
  bytes or drop it; correct C04's slot map (D3); do not apply the declared README vector
  `25/23/27/25/24/94` (C07/C08 D1); re-derive all four README rows from landed bytes at apply time.
- **C02** — correct the three counts (121 / 39 / 13, or quote the exact commands).
- **C03** — correct the `Eade`/`Sumption` probes to word-boundary commands; fix the "none in
  myth-symbol" sentence; re-point `greece-classical.md:65` to `:97–98`.
- **C04** — fix the `gem` topic-owner probe; drop or `(to-verify)` the "turquoise-mining" qualifier;
  re-point `cosmology-cosmography.md:132` to `:37` (omphalos) and `direction-symbolism.md:66`
  (*qusqu*); re-prefix the `DR-MS-*` series if both lithic entries survive.
- **Post-apply sweep** — `python3 -B reports/round-28/readme/sweep.py` at `224 == 224` remains the
  integrator's measurement; this audit read bytes, not a delivered revision.
- **Literature** — all external works remain `(to-verify)`; no network was used, and no external
  claim was checked for truth.
- **Not run** — any `reports/round-*/run-validation.py`; any git mutation; any write outside this
  file and `.scratch/c05/`.

## Citations

- Assignment and boundaries: `reports/round-42/targets.json` seat C05 (auditor, claim C,
  `cov/C05-audit.md`), `shared_rules` (write only the out path; never edit filed bytes; no
  commits/pushes/installs/network; never run an in-tree `run-validation.py`); `claims.json` claim C
  (`myth-symbol 23 → 27`, total `220 → 224`, thresholds "sweep green; audits clean").
- Baseline: `git rev-parse HEAD` → `ac47c7861b0b2cdb8e3c2f985c2220406d3ba0b4`;
  `git log --oneline -1` → `ac47c78 round-41: admit O/Ca — round-runner template + conformance
  checker ...`; `git status --porcelain` → `?? reports/round-42/`.
- Audited fragments: `cov/C01-entry-1.md` (538 lines / 129 691 B / `b7140ce0…`),
  `cov/C02-entry-2.md` (235 / 61 553 / `474c7fac…`), `cov/C03-entry-3.md` (225 / 72 611 /
  `d7daa54b…`), `cov/C04-entry-4.md` (295 / 82 336 / `2b8eb533…`).
- Stager regex and block pins: §1; C02 `14455ddc…` (49 977 / 188), C03 `5ab039f1…` (63 165 / 182),
  C04 `e88cb167…` (61 885 / 193); C01 0 matches (4-backtick fence).
- Contract precedent: `reports/round-35/cov/C12-audit-runbook.md` §1 (five check families), §4
  (stager recipe), §5 (instrument), §8 (review tier); `reports/round-42/plan/P01-plan.md:407–434`
  (entry contract); `corpus/QUALITY.md:1–23` (admission bar).
- Sweeps: all commands in §4, run 2026-10-19 from the lane root at `ac47c78` under
  `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`; counts quoted in the tables.
- Spot-checks: the `path:line` reads in §5; the one wrong C03 locator and the two wrong C04
  locators are re-read in place (`greece-classical.md:65` vs `:97–98`;
  `writing-systems.md:52`; `cosmology-cosmography.md:132` vs `:37`/`:43`; `direction-symbolism.md:66`).
- Verifier fold: `reports/round-42/cov/C07-verify.md` §5 (D1), §6 (C02 contract + D2);
  `reports/round-42/cov/C08-verify.md` §5 (D1), §8 (C02), §9 (C03), §10 (rows), §11 (D3);
  `reports/round-42/adj/A01-entries-bleed.md` §2 (instrument), §4 (C02 verdict), §5 (F-A01-1);
  `reports/round-42/adj/A01-scan-instrument.py` (run read-only on all four staged blocks).
- Collision and routing: `reports/round-42/cov/C01-entry-1.md:1–4,:13–28`;
  `reports/round-42/cov/C04-entry-4.md:5,:17`; `reports/round-42/scout/K02-myth-gaps.md` §R1
  (lithic), §R4 (purity dispositioned to C02); `reports/round-42/scout/K02-myth-gaps.md:176,:525`
  (the `vessel-container-lexicon.md` Pliny 36.27 overclaim, which C04 correctly reports).
- Commands run (this seat, 2026-10-19, lane root, read-only): `git rev-parse` / `git log` /
  `git status`; the §1 extractor (`re.findall` stager regex + sha256); the §2 pointer/line-ref
  resolver; `python3 -B reports/round-42/adj/A01-scan-instrument.py` on each staged block; the §4
  grep battery; the §5 `sed -n` line reads; `grep -n '36.27'` on the vessel file;
  `grep -rlw` word-boundary checks. **Not run, deliberately**: any `reports/round-*/run-validation.py`;
  any network call; no write outside this file and `.scratch/c05/`.
