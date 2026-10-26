# ExecRenumber — collision guard + by-document id map (narrative-structure theme)

Seat: ExecRenumber (executor, leaf). Lane: kotodama-shokunin. Base: `f556d1049fe651d3d63975600b13acd9fb686f15`.
Scope: the CORPUS §6 item-10 id-collision guard, proved on planted collisions; the lane↔staged
id collision set; and the by-document map (join key = normalized URL) that the adopted entries'
citations must follow. Read-only on the staged package and on the fleet repo; the only bytes
this seat wrote are under the lane's own wave dir (below).

## Deliverables (all under `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-75/assimilation/`)

| file | sha256 | what it is |
|---|---|---|
| `reg-ids` | `dd090b02e0f5c1e1b0eca105c9c37f913a9c937930737ec2c6450d74244e859e` | 808 lane registry ids at base, extracted with the item-10 pattern |
| `staged-ids` | `bab11d7d0ee0d84795b1ff80274fe371670fff73a477c747b2fd3cad4c25ddad` | 132 staged package ids, same pattern |
| `collisions` | `01ad6576b56d150ad9505beda35775a2cf982ab110affd6c425704e21a357754` | `comm -12` of the two: 26 ids |
| `id-renumber-map.json` | `778068a431db1f82e9492007f0f4ecf03af21c46679695e91f9981dff56d5155` | the by-document map, the reverse per-entry substitution table, the collision analyses |
| `substitution-table.txt` | `5c6084336d92bfd688b27b3e676fcd9df64d644b7c0b8277048b09e44a6780d3` | the same substitution table, human-readable (generated from the map) |
| `collision-documents.txt` | `f90bf4e154b51fea8ae500f67a1c774723182c6d4a643ab2eba6920ba3666fe2` | per-id lane/staged document table for the 26 collisions |
| `build-map.py` | `f4b1365e98b10506017c5e0eef5f4862bbae550b4518865814da4017025e7b2e` | regenerates the three id files, the map and the substitution table from the base revision (read-only inputs) |
| `guard-proof/` | (dir) | the guard proof: `make-fixtures.py`, `run-guard.sh`, `README.md`, `proof.txt`, `out/` |

`guard-proof/proof.txt` sha256 `b01d2eeb14623ac5b33c74c2073e8fc1a61b1e854bbb06f9fd537ab369c4b7d4`;
`guard-proof/README.md` `9f6b01b4ff5776058643d30b19b34d7ee9e31b99f80fbfb052c2b371e47f657b`;
`make-fixtures.py` `5f71109a63e20d7fa40a649bb7e74f5c4c64b07409a805fdb194beb997dde5b0`;
`run-guard.sh` `92c1fd1da05f02797a6c09c27dcf429458b79a56807fe8515dbc505132af963d`.

**The L1 must set `claims.json` claim C's `map.sha256` to
`778068a431db1f82e9492007f0f4ecf03af21c46679695e91f9981dff56d5155`** (the frozen `map.path`
already reads `.ufo/waves/round-75/assimilation/id-renumber-map.json`). Re-hash after any
edit to the map: the FROZENCFG leg compares the frozen blob's hash with that constant.

## 1. Both id lists, and the collision count

**`reg-ids` — 808 ids**, `S001`…`S884` with these gaps (the lane's own history, not a defect):
455–480, 492–499, 544–551, 554–559, 563, 577–596, 777–778. Last id `S884`; next free `S885`.

**`staged-ids` — 132 ids**, `S859`…`S990`, contiguous.

**`collisions` — 26 ids** (`comm -12` of the two):

```
S859 S860 S861 S862 S863 S864 S865 S866 S867 S868 S869
S870 S871 S872 S873 S874 S875 S876 S877 S878 S879 S880
S881 S882 S883 S884
```

**0 of the 26 are the same document** (normalized-URL join; per-id table in the map's
`numeric_collisions_at_base.lane_document_by_id`). Every one is namespace drift: staged
`S864` is the UCASS narratology syllabus while lane `S864` is UNESCO ICH's "Carnival of
Oruro"; staged `S870` is the chinawriter 2023 practitioner piece while lane `S870` is ICKL's
Labanotation page; staged `S876` is Barthes while lane `S876` is Enguehard on conlangs
teaching. **The guard's acceptance is by document, not "collisions is empty"** — emptiness is
unattainable while the package keeps its S859–S884 rows.

**No adopted lane id is in `reg-ids`**: `grep -cE '^S(88[5-9]|89[0-3])$' reg-ids` = 0, and
the same grep over `collisions` = 0. S885…S893 are free at base.

## 2. The guard proof (planted collisions)

`guard-proof/` proves the extractor before it is relied on. Six fixture mirrors, each the
real lane registry at base (808 rows, sha256 `c8da0a5a765de26506a1c4d9b66d9b47c9ffe4e0d62a87fc510077a7f83c5614`)
with ONE planted row inserted after S884 inside the `## Registry` table. The planted row's
id is a **staged** id the lane does not hold (S985…S989), so each plant is a genuine
staged-vs-lane collision; its URLs are rewritten to `example.invalid/…` and its cells
normalised to `paper`/`A`/`queued`/`—` so the plant adds **no new census finding** — the only
difference from the control is the collision.

| fixture | census rows | ITEM10 ids | sees the plant | collisions | names the plant | COLZERO sees the plant |
|---|---|---|---|---|---|---|
| control (0 sp) | 808 | 808 | — | 26 | 0 | 0 |
| 1sp | **809** | **809** | **1** | **27** | **1** | **0** |
| 2sp | **809** | **809** | **1** | **27** | **1** | **0** |
| 3sp | **809** | **809** | **1** | **27** | **1** | **0** |
| 4sp | 808 | 808 | **0** | 26 | 0 | 0 |
| tab | 808 | 808 | **0** | 26 | 0 | 0 |

- **1/2/3 spaces: found.** The census counts the planted row (`rows 809`), the item-10
  extractor sees the id, and `comm -12` against the staged list **reports it as a collision**
  (27, and the planted id is among them) — with no new census finding, so its appearance is
  not an error artefact.
- **4 spaces: not found.** Ignored by the census (`rows 808`) and by the extractor. Correct:
  4+ leading spaces is indented code per CORPUS's maintained parser note.
- **tab: not found.** A tab-indented row is not a Markdown table row at all (the grammar is
  spaces), so it is neither a census row nor a guard row.
- **column-zero-only misses the indented ones.** `^\|[[:space:]]*S[0-9]{3,}` sees 0 of the
  three indented plants in every fixture — the false-green the contract warns about. The
  0–3-space pattern is the one to ship.

Re-derivation: `python3 make-fixtures.py <root>` then `sh run-guard.sh <root> <out>`; the
per-fixture receipts are `guard-proof/out/*.summary.txt` and the census raw output beside them.

## 3. The by-document map (join key = normalized URL)

**Normalization** (derived from the data, not assumed): host lowercased without `www.`;
path percent-decoded; `persee.fr/doc/page/<slug>/<transcription>` collapsed to
`/doc/<slug>` (a per-page transcription is a **view** of the document, not a second
document); a `web.archive.org/web/<ts>/…` wrapper stripped to the embedded original (a capture
is a **carrier** of the document, not the document). **Never arithmetic, never a numeric id
comparison.**

| staged id | lane id | document | URL |
|---|---|---|---|
| S876 | **S885** | Barthes, *Introduction à l'analyse structurale des récits*, Communications 8 (1966) | `https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113` |
| S885 | **S885** | same document (staged full-text view) | same URL |
| S917 | **S885** | same document (per-page transcription `T1_0011_0000`) | same URL after R2 |
| S921 | **S885** | same document (per-page transcription `T1_0006_0000`) | same URL after R2 |
| S902 | **S886** | Todorov, *Les catégories du récit littéraire*, Communications 8 (1966) | `https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1120` |
| S904 | **S887** | Greimas, *Éléments pour une théorie de l'interprétation du récit mythique*, Communications 8 (1966) | `https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1114` |
| S864 | **S888** | UCASS 研究生院, 《叙事学》course syllabus | `https://jw.ucass.edu.cn/kcdg/zyk/xwcb/xushixue.pdf` |
| S865 | **S889** | 小方 孝, 「物語生成の物語論あるいはポストナラトロジー」, *Cognitive Studies* 25(2) | `https://www.jstage.jst.go.jp/article/jcss/25/2/25_200/_pdf` |
| S866 | **S890** | 村井 源, 「物語構造の階層的記述方式の提案」, *情報知識学会誌* 32(2) | `https://www.jstage.jst.go.jp/article/jsik/32/2/32_2022_017/_pdf` |
| S905 | **S891** | Barthes, *S/Z* (Seuil 1970) — the « S/Z » excerpt | `https://www.unige.ch/lettres/framo/cernet/biblio/barth70.html` |
| S919 | **S892** | Marrone, « L'âge d'or de la sémiotique littéraire », *Signata* 5 (2014) | `https://iris.unipa.it/retrieve/e3ad891d-ad9f-da0e-e053-3705fe0a2b96/2014%20marrone%20age%20dor---2.pdf` |
| S870 | **S893** | 三九音域「世界观是打开小说幻想屋的钥匙」, 中国作家网 2023-09-22 | `https://www.chinawriter.com.cn/n1/2023/0922/c404024-40083104.html` |

**Cross-check against the DRAFT claim: 9/9 rows agree.** For each adopted lane id, the set of
staged rows naming that same document under the normalized join is *exactly* the staged set
`claims.json` names (the map's `cross_check` block, one row per lane id, each
`by_document_join_agrees_with_claim: true`). The four persee-1113 staged rows collapse onto
one lane row S885; every other document has exactly one staged row.

**The map is not arithmetic — proven, not asserted.** The twelve assignments have **ten
distinct numeric offsets**: −36, −32, −27, −17, −16, −14, 0, +9, +23, +24. No single offset
reproduces the map; S876→S885 is +9 while S917→S885 is −32 and S864→S888 is +24.

**Post-adoption cross-namespace overlap** (the map's `post_adoption_numeric_overlap`): the
lane ids S885–S893 are *themselves* staged ids in the campaign namespace, and after the
landing each names a different document on the two sides (lane S886 = Todorov vs staged
S886 = Kotobank 苗字; lane S890 = 村井 源 vs staged S890 = Kałużyńska; lane S891 = the
*S/Z* excerpt vs staged S891 = Zhao et al.; and so on for all nine). Resolution: the staged
ids stay campaign-local and are replaced by the lane ids in the frozen map's single pass.

## 4. The reverse per-entry substitution table

Every S-id occurrence in the five staged narrative files, with its replacement. The full
machine-readable table is the map's `entry_substitutions` block (36 occurrences over 5 files);
`map.json` also carries the per-file `cited_by_file` derivation.

**The substitution must be a SIMULTANEOUS single pass over one lookup table.** A sequential
per-id replacement corrupts the result: lane ids S885–S893 are staged ids in the campaign
namespace, and the four persee-1113 staged rows S876/S885/S917/S921 all collapse onto lane
S885, so a second pass would re-map an already-mapped id.

| staged file | staged ids present (occurrences) | replacements |
|---|---|---|
| `narrative-structure-frameworks.md` | S876×3, S864×2, S865×2, S866×2, S870×4 | S876→**S885**, S864→**S888**, S865→**S889**, S866→**S890**, S870→**S893** |
| `…amend-2026-10-23.md` | S902×3, S904×3, S885×2, S744×1 | S902→**S886**, S904→**S887**, S885→**S885**, S744→**S885** (prose) |
| `…amend-2026-10-23b.md` | S905×3, S744×1 | S905→**S891**, S744→**S885** (prose) |
| `…amend-2026-10-23c.md` | S917×3, S744×1, S763×1 | S917→**S885**, S744→**S885** (prose), S763→**S887** (prose) |
| `…amend-2026-10-24.md` | S919×3, S921×3 | S919→**S892**, S921→**S885** |

### The four prose ids that are NOT staged rows — rewritten, never arithmetic-mapped

**S744** (3 occurrences: `amend-2026-10-23.md:11`, `amend-2026-10-23b.md:12`,
`amend-2026-10-23c.md:12`) and **S763** (1 occurrence: `amend-2026-10-23c.md:12`) are
**not rows of the staged package** — they are scope-file ids of earlier campaign rounds.
Their subject is recoverable by document:

- **S744** = campaign-scope id (`corpus-expansion-3`, round 3) for *Barthes's levels of
  description and the two readings, full 1966 text* — **the same document as staged
  S876/S885/S917/S921** → rewrite to lane **S885**.
- **S763** = campaign-scope id (`corpus-expansion-4`, round 4) for *Greimas's two isotopies*
  — **the same document as staged S904** → rewrite to lane **S887**.

**Both are safe same-document rewrites, and neither may be left alone or mapped by number.**
Left alone, `S744` resolves in the lane registry to **Dictionary.com's ushanka page** and
`S763` to **the tafl-games article** — the REPOINTED leg's "no campaign-namespace id is cited
as a lane row" would catch them, and the claim's own text would then misattribute a Barthes
claim to the ushanka row.

This is the hazard the campaign's own `lanes/kotodama/ID-REMAP.md` names: *"The map is scoped
per round: the same id in two rounds names two different rows, so a round-blind substitution
would move one round's citations onto another's rows while every structural check stayed
green."* S744 and S763 are exactly that case, and the lane registry already reuses both
numbers for unrelated documents.

### Per-row used-by derivation (for the ROWS leg's `used-by` cell)

The map's `cited_by_file` gives, per adopted lane id, the staged files that cite it. **Only
the two frozen entries may appear in a landed row's `used-by`** — the other three staged
narrative files (`amend-2026-10-23b/-23c/-2026-10-24`) are not in claim C's frozen `entries`,
so their rows' `used-by` depends on whether the L1 admits those files this round:

- files in claim C's frozen `entries`: `corpus/knowledge/myth-symbol/narrative-structure-frameworks.md`
  and `corpus/knowledge/myth-symbol/narrative-structure-frameworks.amend-2026-10-23.md`.
- Under the frozen two-entry set: **S885** is cited by both; **S886, S887** by the
  amendment; **S888, S889, S890, S893** by the base entry. **S891 and S892 would then have no
  citing frozen entry** — both are cited only by `amend-2026-10-23b` and `amend-2026-10-24`.
  The ROWS leg requires `used-by` to equal exactly the admitting entries, so **if S891/S892
  land, those two amendments must land too, or their rows' `used-by` has no citing entry**.
  This is the L1's landing decision; the map records the derivation either way.

## 5. Findings for the L1 (attack results against the DRAFT)

1. **`claims.json` claim C `rejects.refused_staged_not_appended` holds PROSE, not an id
   list.** Its value is `["S870's staged quote (absent on page; source re-opened as S893
   with a fresh quote)"]`. A counter that reads this field with an id-list parser (round-74's
   `_id_list`, which requires every item to fullmatch `S\d{3,}`) **raises ConfigError and
   refuses with exit 2** — the counter never grades. Recommend: make the field a list of ids
   (`["S870"]`) and put the prose in a separate note field, or have the counter read ids out
   of the string. Also note the id it names is **S870**, which *is* in the frozen `row_set`
   (as lane S893) — so what is refused is the staged **quote**, not the row. The map records
   S870→S893 as **conditional**: the row lands only if this round's Gate locates a fresh
   quote on the re-opened page; otherwise no lane row is appended and the rejection keeps
   its reason+flip.
2. **The claim's row_set `staged` field for S885 is a 4-id composite** (`"S876/S885/S917/S921"`)
   while every other row carries a single id. The round-74 counter's `_row_pairs` requires
   each `staged` value to fullmatch a single `S\d{3,}` — the composite raises ConfigError
   there too. The map's `assignments` gives **one entry per staged id** (12 entries) with
   `new_lane_id` repeated, so a counter that reads `assignments` gets 12 unambiguous
   (staged → lane) records; the `map` dict additionally carries all 12 staged→lane pairs.
   Recommend: keep `assignments` as the counter's read path and treat `row_set[i].staged` as
   the display form, or relax `_row_pairs` to accept a list.
3. **S892's URL form differs between the claim cell and everything else.** The claim's
   `row_set` document cell writes the PDF filename with **spaces**
   (`…/2014 marrone age dor---2.pdf`); the staged row, the L1's own lesson draft and every
   working URL write it **%20-encoded** (`…/2014%20marrone%20age%20dor---2.pdf`). A counter
   that checks the map's `url` as a substring of the landed row's source cell will fail if
   the two diverge. The map carries the **%20 form** as `url` and lists all three forms in
   `url_variants`; the landed row and the map must agree.
4. **The claim's `before` text is false on one point, as a sibling seat already recorded**
   (`ConnectorSiblings.md` §3): it says the base tree holds "no file governs narrative
   structure" and that `comparative-frameworks.md` "neither names a structuralist narrative
   source" — but `comparative-frameworks.md` names **Greimas (1966) *Sémantique structurale*
   and Propp's actantial model** at base, and `costume-semiotics.md` already cites Barthes.
   The claim's *new* ground is the narrative-structure literature itself (Barthes 1966,
   Todorov, Greimas 1966 on the mythic narrative, *S/Z*, the Chinese and Japanese
   scholarship), which the base registry indeed lacks (0 rows for any of the 8 documents).
   The GROUND leg measures the registry fragments, so it passes; the *prose* is what
   overstates. The L1's own draft entry already carries the corrected sentence ("the lane's
   knowledge tree does carry Genette … Barthes … and none of those is a narrative-structure
   source"), which is the right form.
5. **Post-adoption namespace overlap is nine ids, not two.** Round-74's dispatch premise was
   that the lane holds S883/S884 as different documents; that was false at base. Here the
   truth is: at base the lane holds S001–S884 and the adopted ids S885–S893 are free, but
   the *staged* package also carries ids S885–S993, so after the landing **nine** numbers
   (S885…S893) name different documents on the two sides. That is expected and handled by the
   single-pass substitution, but it is the reason the map must never be applied
   sequentially.

## 6. Scope, methods, and what was not done

- **Nothing was mutated outside the lane's wave dir.** Read-only on the staged package
  (`/home/vgpnk/Projects/shokuknow/merge/kotodama/`), on the fleet repo
  (`/home/vgpnk/Projects/shokunin/`) and on the lane's git state — no writes, no index
  changes, no commits. `reports/round-75/claims.json` and `reports/round-75/ledger.json`
  were read and never edited; the fleet's `LOG.md`, `SCORECARD.md`, `scripts/`, `templates/`
  and `.ufo/state` were not touched.
- **The id files are derived from the base revision**, not the working tree: `reg-ids` from
  `git show f556d104…:corpus/SOURCES.md` (the worktree copy is byte-identical —
  sha256 `c8da0a5a765de26506a1c4d9b66d9b47c9ffe4e0d62a87fc510077a7f83c5614` both ways —
  so the two agree), `staged-ids` from the staged package file
  (sha256 `7fb4f488807e8364d204a3081a2e57379d6caafaa92dbab9dfbc381757223754`).
- **Guard fixtures were built in scratch** under
  `/fast/scratch/hyaku/kotodama-r75/ExecRenumber/` and deleted before this report; the
  receipts (`guard-proof/out/`) and the two scripts were copied into the wave dir, and
  `make-fixtures.py` regenerates the mirrors deterministically from the base revision.
- **No counter was run and no acceptance leg was graded** — the round-75 counter does not
  exist yet, and the parent owns the post-integration gate. What is asserted here is
  measured: the counts, the joins and the guard behaviour above, each re-derivable from the
  committed scripts and receipts.
- **No tool was installed** for this seat; everything used (`grep`, `comm`, `gawk` via
  `sources-census.sh`, `python3`, `git`) was already present.
