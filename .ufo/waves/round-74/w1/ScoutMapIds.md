# ScoutMapIds — round 74 w1 — by-document id map

Seat: ScoutMapIds (leaf scout). Read-only everywhere except this file and `id-map-draft.json` (same dir). Tools used: python3 parsing + grep; nothing installed, no network, no fetch.
Registry parse: `^ {0,3}\|\s*S\d{3,}\s*\|` (1-3 leading spaces allowed). Lane `corpus/SOURCES.md` = 804 rows, 804 distinct ids, S880 last (matches census-start). Staged `SOURCES.append.md` = 132 rows, 132 distinct ids, S859..S990. Join key = URL; id equality used only as a defect signal.

## 1. Ids cited in the two staged entries, resolved by document

Inline/source ids found (regex `S\d{3,}`):

| file | ids (count) |
|---|---|
| worldbuilding-setting-practice.md (26 lines) | S729(2) S730(2) S882(4) S883(4) S884(4) |
| worldbuilding-setting-practice.amend-2026-10-23.md (44 lines) | S742(1) S743(1) S754(1) S895(3) S899(3) S900(3) |

Two id generations are mixed inside the staged prose. `source:`/`recheck:` lines use the packaged staged ids (present in SOURCES.append.md). The `ground:`/`gap filled:` prose uses the round-local ids of earlier rounds (round 1 = S718..S730, round 2 = S731..S743, round 3 = S744..S755 per lanes/kotodama/round{2,3,4}/SOURCES-PROPOSED.md headers) — these are NOT in the staged append file (it starts at S859) and numerically hit unrelated lane rows.

| cited as | resolves (by document) to staged id | document | lane row with that URL | lane row that holds the SAME NUMBER (unrelated) |
|---|---|---|---|---|
| S882 | S882 | philol.msu.ru/~sidorova/files/conlangs.pdf | **S877** (same URL) | none at base (lane max S880); after adoption lane S882 = tuduku (unrelated) |
| S883 | S883 | litmemo.com/ja/blog/novel-worldbuilding-guide | none | none at base; lane S881 after adoption |
| S884 | S884 | tuduku.space/column/novel-worldbuilding | none | none at base |
| S899 | S899 | chinawriter 2025/0605/c404024-40494534.html | none | none at base (register S816 = Himalayan Art, unrelated lane row) |
| S900 | S900 | chinawriter 2022/1207/c404024-32582252.html | none | none at base (register S817 = Milwaukee Public Museum lane row, unrelated) |
| S895 | S895 | chinawriter 2025/1030/c404027-40592897.html (王昕玥) | none | none at base |
| S729 | S870 (round-1 local id; confirmed by round3/SEARCH-LOG.md:63 "六人谈 essay are round 1's S729") | chinawriter 2023/0922/c404024-40083104.html | none | **lane S729 = Neer et al. 2025, PLOS ONE infant-directed speech — UNRELATED** |
| S730 | S871 (round 1 S718..S730 ↔ S859..S871) | read.douban.com/submit/writing_guide | none | **lane S730 = Genesee & Nicoladis 2007, bilingual acquisition — UNRELATED** |
| S742 | S883 (round 2 S731..S743 ↔ S872..S884; litmemo = "layers") | litmemo | none | **lane S742 = Shields-Lysiak et al. 2020, classroom greetings — UNRELATED** |
| S743 | S884 ("notes") | tuduku | none | **lane S743 = Akita 2012, Berkeley Linguistics Society — UNRELATED** |
| S754 | S895 (round 3 S744..S755 ↔ S885..S896; amend line 11 "failure analysis of a world-view" = 王昕玥 §二世界观的预设缺陷) | chinawriter 2025/1030 | none | **lane S754 = UNESCO ICH Tugging rituals and games — UNRELATED** |

Confidence S754→staged S895: medium-high. The entry's own text (amend:11, :31, :44) ties "S754 … failure analysis" to S895. Counter-evidence: round6/QUOTE-RECHECK.md:53 uses "S754" for the Sowers-Wills `doi.org/10.1017/cnj.2024.21` row (a later id generation). Resolution by the entry's own context, not by arithmetic.

**Staged ids that coincide numerically with a lane id naming an UNRELATED document (at base):** S859..S880 — 22 ids, all 22 unrelated by URL join (0 same-document pairs among same-number pairs). Of the theme-cited ids none of S882..S884, S895, S899, S900 collides numerically at base; the five prose ids S729, S730, S742, S743, S754 all do (every one names an unrelated lane row). Same-document-different-id pairs (staged→lane, URL identical): S863→S874, S967→S874, S867→S875, S881→S876, S882→S877, S892→S878, S893→S879, S901→S880. None of the four new theme rows (litmemo, tuduku, chinawriter 0605, chinawriter 1207) has a URL already in the lane (0 hits for litmemo/tuduku/chinawriter/read.douban in corpus/SOURCES.md except S877's philol URL).

## 2. Recommended by-document map

| staged | → lane | document | action |
|---|---|---|---|
| S883 | **S881** | litmemo.com/ja/blog/novel-worldbuilding-guide | append |
| S884 | **S882** | tuduku.space/column/novel-worldbuilding | append |
| S899 | **S883** | chinawriter.com.cn/n1/2025/0605/c404024-40494534.html | append, re-quote from page |
| S900 | **S884** | chinawriter.com.cn/n1/2022/1207/c404024-32582252.html | append, re-quote from page |
| S882 | existing **S877** | philol.msu.ru conlangs.pdf | do NOT append; repoint; in-place used-by change |

Next free lane id at base: **S881**; after the four appends: **S885**. Holes below max (S455-S480, S492-S499, S544-S559, S563, S577-S599, S777-S778 per r73 map) must not be filled.

Findings the map alone does not fix (the entries must also change):
1. **Chained map ⇒ simultaneous substitution.** staged S883→S881, S884→S882, S899→S883, S900→S884, S882→S877: lane S883/S884 are numerically staged S883/S884 of a different document. Sequential per-id replacement (sed per id, or applying S899→S883 before S883→S881) re-maps already-mapped ids. Use one regex pass over a lookup table. I simulated a single pass over both staged files: result ids = S877(4) S881(4) S882(4) [base file] and S883(3) S884(3) [amend]; the prose ids S729/S730/S742/S743/S754/S895 stay untouched by the table (they are not keys) — i.e. they would survive as dangling/mis-resolving lane ids.
2. **Prose ids must be rewritten or removed, not mapped.** S742→S881, S743→S882 are safe rewrites (same document). S729/S730 (staged S870/S871) and S754/S895 are NOT in the row_set: staged S870 was refused round 72; S895's whole "Superseded passage" section (amend lines ~24-44, `source: S895`, 3 mentions) cites a row that is not adopted. Under the draft kill_rule ("cites a refused/unknown staged id or an id naming an unrelated lane document") these must be removed/reworded id-free, or S895 must be separately admitted (not in the draft row_set).
3. **S877 locator mismatch.** Staged base entry cites S882 "аннотация" and the staged row says "series announcement booklet"; lane S877 says the same URL serves the 185-page full text (anchor: Chapter 1, printed p.10) and "not an announcement booklet". Same URL ⇒ same document by the join rule, but the `source:` locator and §2 text were derived from the booklet and need re-checking against the text S877 opened. Lane S877 used-by is currently `corpus/knowledge/linguistics/conlang-scholarship.md` (13 cells, opened 2026-10-25).
4. All staged rows for this theme carry an escaped `\|` in the recheck cell (S870, S871, S882-S884, S895, S899, S900 each have 1) and opened 2026-10-23 — consistent with the claim's "not appended as-is".

## 3. Round-73 map and prior-id checks

- `.ufo/waves/round-73/assimilation/id-renumber-map.json` targets S876..S880 only (staged S881/S882/S892/S893/S901). Its only mention of S881 as a target is `conditional_assignments` S894→S881 ("new_target_if_admitted"); S894 was not admitted: lane has no `cnj.2024.21` / Sowers-Wills row (grep 0). Not reused: round-74 shares only the pre-existing S882→S877 pairing (an existing lane row, no new id). Do not merge the two maps — r73 keys "staged S881" (Enguehard→S876) and r74 targets "lane S881" (litmemo) are different namespaces.
- S881..S884 absent from the lane registry at base (804 rows, max S880) and from the worktree SOURCES.md (not modified vs base: `git status` shows only the six round-73 w2 files + untracked round-74 dirs).
- Prior appearances of "S881..S884" in lane lessons/LOG/SCORECARD: corpus/lessons/round-73.md:25-26 (staged S881→S876, staged S882→S877 — staged namespace), corpus/lessons/round-72.md:96 line mentions S874/S875/S878/S882 as old r71 map targets (stale round-71 map, staged→old target; not lane rows). LOG.md, SCORECARD.md: 0 hits. Other hits are staged-namespace lists (`.ufo/waves/round-69|70/assimilation/staged-ids`, reports/round-73/claims.json and accept-c.py fixtures). No lane row ever held S881..S884.
- Gotcha for counters: grep for `\bS88[1-4]\b` in the lane tree is NOT a clean "absent as prior id" test — it matches staged-namespace mentions. Use the registry parse (above) for the base-absent claim.

## Output
Draft JSON: `.ufo/waves/round-74/w1/id-map-draft.json` (valid JSON; fields: assignments, reused_rows, prose_ids_resolved_by_document, numeric_collisions_staged_vs_lane_at_base, post_adoption_numeric_overlap, round73_map_not_reused, substitution_rule). Not copied to `assimilation/` (not my write path).

Not done / not checked: no live fetch of any page (L1 probed them); did not diff the staged row cells against the pages; register file for S816/S817→staged S899/S900 taken from lessons/round-72.md:32 (register file itself not located).
