# ScoutMapIds — by-document id map for the conlang-scholarship theme (round 73, w1)

Seat: ScoutMapIds (leaf scout). Date: 2026-10-25. Claim context: `reports/round-73/claims.json` claim C (coverage / assimilation-sourced); this report verifies the REPOINTED and COLLCHECK premises and regenerates the id-renumber map.

No tools installed (no pacman, no uv/npx/binary installs — plain read/grep/Python analysis only). No repo bytes mutated except the two assigned artifacts: `id-renumber-map-draft.json` (written) and this report.

---

## Three-namespace table (join by URL/document only)

| namespace | file | id range | count |
|---|---|---|---|
| staged | `shokuknow/merge/kotodama/SOURCES.append.md` | S859..S990 | 132 |
| register (absent-defect-register) | `shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md` | S776..S835 | (fleet-owned; not parsed here) |
| lane | `kotodama-shokunin/corpus/SOURCES.md` | S001..S875 | 799 |

Join rule applied: numeric equality across namespaces is meaningful ONLY as a defect signal (campaign id in a lane row naming an unrelated document). Document identity is established by URL, never by id.

---

## 1. Citation resolution for the staged conlang entries

Files scanned (all six staged theme files): `conlang-scholarship.md`, `conlang-scholarship.amend-2026-10-23.md`, `conlang-scholarship.amend-2026-10-23b.md`, `conlang-scholarship.amend-2026-10-23c.md`, `conlang-scholarship.amend-2026-10-24.md`, `conlang-methodology.amend-2026-10-24.md` (all under `shokuknow/merge/kotodama/knowledge/corpus/knowledge/linguistics/`).

17 distinct S-ids cited. Resolution:

### (a) Citations that resolve to a staged row, with NO lane collision (14 ids)

| cited id | file:line | staged doc (URL) | in lane same-id? | URL collision with any lane row? |
|---|---|---|---|---|
| S881 | conlang-scholarship.md:4 | Enguehard 2022, ojs.unito.it/…/view/7099 | no (lane ends at S875) | none (host `ojs.unito.it` = 0 hits in lane) |
| S882 | conlang-scholarship.md:5 | Сидорова/Шувалова 2006 booklet, philol.msu.ru/~sidorova/files/conlangs.pdf | no | none (`philol.msu.ru` = 0 hits) |
| S901 | conlang-scholarship.amend-2026-10-23.md:4 | Anderson/Grant/Sanders, sanders.phonologist.org/Papers/anderson-etal-cjl-sotl.pdf | no | none (`sanders.phonologist.org` = 0 hits) |
| S892 | conlang-scholarship.amend-2026-10-23.md:30 | Новиков 2022, journals.rudn.ru/semiotics-semantics/article/viewFile/31528/20955 | no | none (`journals.rudn.ru` = 0 hits) |
| S893 | conlang-scholarship.amend-2026-10-23.md:31 | Костюхин 2023, cyberleninka.ru/article/n/klassifikatsii-konlangov-v-sovremennoy-interlingvistike | no | none (`cyberleninka` = 0 hits) |
| S894 | conlang-scholarship.amend-2026-10-23.md:32 | Sowers-Wills 2024, doi.org/10.1017/cnj.2024.21 | no | none |
| S909 | conlang-scholarship.amend-2026-10-23b.md:4 | Петров 2024, philnauki.mgimo.ru/jour/article/viewFile/520/524 | no | none |
| S910 | conlang-scholarship.amend-2026-10-23b.md:5 | Windsor 2026, doi.org/10.1007/978-3-032-03277-5_15 | no | none |
| S915 | conlang-scholarship.amend-2026-10-23c.md:4 | Palgrave Handbook of Constructed Languages, Crossref API record | no | none |
| S929 | conlang-scholarship.amend-2026-10-24.md:4 | Luba 2025, linguistische-treffen.pl/articles/27/24_luba.pdf | no | none |
| S930 | conlang-scholarship.amend-2026-10-24.md:5 | Schreyer 2021, Crossref record 10.1146/annurev-anthro-101819-110152 | no | none |
| S920 | conlang-methodology.amend-2026-10-24.md:4 | Sowers-Wills 2024 (Wayback capture of cambridge.org PDF) | no | none |
| S922 | conlang-methodology.amend-2026-10-24.md:5 | Crossref journals endpoint (constructed+language) | no | none |
| S923 | conlang-methodology.amend-2026-10-24.md:6 | Goodall 2023, Crossref record 10.1146/annurev-linguistics-030421-064707 | no | none |

URL collision check method: normalized exact match (scheme/www stripped, trailing slash stripped, fragment stripped) of every staged URL against all lane-row URLs, PLUS a soft host/path grep of the lane file for each theme host. Zero collisions. This confirms the claim-C GROUND gap (0 owners at the 799-row registry) for the five theme URLs.

### (b) Campaign-id citations: staged id coincides with a lane id naming an UNRELATED document (3 ids, 4 citation sites)

| cited id | file:line | lane[id] document | relation to theme |
|---|---|---|---|
| **S728** | conlang-scholarship.md:11 | Henrike Frye 2022, *Child-directed Speech in Qaqet* (Qaqet child-directed speech) | UNRELATED — defect |
| **S769** | conlang-scholarship.amend-2026-10-23c.md:14 | Iona & Peter Opie, *The Lore and Language of Schoolchildren* | UNRELATED — defect |
| **S806** | conlang-scholarship.amend-2026-10-24.md:42 | Jaiswal & Williams, "A glimpse of Ayurveda …" | UNRELATED — defect |
| **S806** | conlang-methodology.amend-2026-10-24.md:17 | same (Ayurveda) | UNRELATED — defect |

All three are absent from the staged row set (staged namespace is S859..S990), so they are campaign ids: they name lane documents that have nothing to do with the conlang theme. The known set (S728, S769, S806) is exactly the found set — no additional unrelated-document coincidences exist among the 17 citations. Consequence for claim C REPOINTED: these three ids must appear nowhere in the admitted entries (the existing draft entries still cite them — see §4).

---

## 2. Stale round-71 map: assignments that no longer hold at the 799-row registry

Source: `.ufo/waves/round-71/assimilation/id-renumber-map.json` (registry_count 797, next_free S874, span S874→S1005, staged S859..S990 → S874..S1005).

Current lane registry: 799 rows, S001..S875. Therefore:

- **S859 → S874 no longer holds.** Target S874 is now a live lane row; it names the 中国非物质文化遗产网 · 中国非物质文化遗产数字博物馆 project list (`https://www.ihchina.cn/project.html`) — which URL-joins to **staged S863**, not staged S859.
- **S860 → S875 no longer holds.** Target S875 is now a live lane row; it names 文化遺産データベース（文化庁）文化財検索 (`https://online.bunka.go.jp/db/heritages/search`) — which URL-joins to **staged S867**, not staged S860.
- Every other old-map target (S876..S1005) is still unoccupied, so no other target-side assignment is broken by occupancy. However, the two URL joins above also mean the old map's pending entries for staged S863 and staged S867 are obsolete (their documents are already live as lane S874/S875).

Apparent drift observation [INFERENCE]: the actual adoption order did not follow the round-71 map's pairings (lane S874 = staged S863's doc, not S859's). What is hard fact is the join itself: staged S863's URL appears in lane S874; staged S867's URL appears in lane S875.

---

## 3. Regenerated map draft (five theme rows)

Written to `.ufo/waves/round-73/assimilation/id-renumber-map-draft.json` (7087 bytes). Summary:

| staged | target | derivation URL-join evidence |
|---|---|---|
| S881 | **S876** | URL `https://ojs.unito.it/index.php/ricognizioni/article/view/7099` in 0/799 lane rows; S876 unoccupied; staged id not a lane id |
| S882 | **S877** | URL `http://www.philol.msu.ru/~sidorova/files/conlangs.pdf` in 0/799 lane rows; S877 unoccupied; staged id not a lane id |
| S892 | **S878** | URL `https://journals.rudn.ru/semiotics-semantics/article/viewFile/31528/20955` in 0/799 lane rows; S878 unoccupied; staged id not a lane id |
| S893 | **S879** | URL `https://cyberleninka.ru/article/n/klassifikatsii-konlangov-v-sovremennoy-interlingvistike` in 0/799 lane rows; S879 unoccupied; staged id not a lane id |
| S901 | **S880** | URL `https://sanders.phonologist.org/Papers/anderson-etal-cjl-sotl.pdf` in 0/799 lane rows; S880 unoccupied; staged id not a lane id |

The draft JSON carries `derivation` per row (staged line in `SOURCES.append.md`: 29/30/40/41/49), `supersedes` pointing at the round-71 file, the two broken assignments, the two source-already-adopted joins, and the campaign-id defect list. Next free lane id: S876. Old→new recorded; filed (round-71) bytes untouched.

---

## 4. Notes for the claim-C predicate (read-only observations)

- The claim's REPOINTED leg and kill rule require that staged-only campaign ids S728/S769/S806 appear nowhere in the admitted entries. They are currently cited in the staged drafts (see §1b), so the scribes/counter must cut or re-point them before landing.
- The five theme rows' URLs are absent from the lane (0 collisions), consistent with the claim's GROUND receipt.
- No row in the staged set is appended as-is in any sense this seat can check (row normalization is the executor/scratch-mirror seat's area).
- Unknowns left for other seats: whether the staged S894/S910 payloads are reachable by ordinary means (Quarantine/RevSowersAccess seats); whether the register namespace (S776..S835) contains any entry whose document coincides with a theme URL (register is fleet-owned; probed URL evidence belongs to the quarantine seat).
