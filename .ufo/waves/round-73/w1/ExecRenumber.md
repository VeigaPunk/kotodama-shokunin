# ExecRenumber — item-10 collision guard, proved, and the id map regenerated from S876 (round 73, w1)

Seat: ExecRenumber (leaf executor). Date: 2026-10-25. Claim attacked/built against: `reports/round-73/claims.json` claim **C**, legs `COLLCHECK` (and the id half of `ROWS`/`REPOINTED`). The claim file was read, never edited.

Scope actually exercised: the item-10 guard from `/home/vgpnk/Projects/shokunin/CORPUS.md` §6 item 10 (prompt lines 440–545), the five theme rows, and the round-71 map's staleness. Every write landed under
`A=/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-73/assimilation` plus this report. Nothing written to the fleet repo, the shokuknow tree, `corpus/**`, `reports/**`, or any git/jj state.

Tools installed: **none** (no pacman — paused host-wide —, no uv/npx/binary). Live fetches: **none**, so no User-Agent applies and no source-reachability ruling is made here.

---

## 1. The guard, run exactly as CORPUS item-10 writes it

```
A=/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-73/assimilation; mkdir -p "$A"
grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md \
  | grep -oE 'S[0-9]+' | sort > "$A/reg-ids"
grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' /home/vgpnk/Projects/shokuknow/merge/kotodama/SOURCES.append.md \
  | grep -oE 'S[0-9]+' | sort > "$A/staged-ids"
comm -12 "$A/reg-ids" "$A/staged-ids" > "$A/collisions"
```

Output:

```
=== wc -l ===
 799 .../assimilation/reg-ids
 132 .../assimilation/staged-ids
  17 .../assimilation/collisions
=== collisions content ===
S859
S860
S861
S862
S863
S864
S865
S866
S867
S868
S869
S870
S871
S872
S873
S874
S875
=== duplicate check (uniq -d) ===            # empty: both lists are unique
```

Row counts also confirmed by the pattern itself: `grep -cE '^ {0,3}\|…'` = **799** on the registry, **132** on the staged package. `collisions` is non-empty → per item 10 the staged set is fixed **in scratch only**, adopted ids continue the lane registry, and every citation is re-pointed by document.

## 2. Guard proof — the pattern is proved before anything appends

Driver: `$A/guard-proof/run-guard-proof.sh`; transcript: `$A/guard-proof/guard-proof.txt` (exit **0**, `GUARD-PROOF: PASS`). Three fixtures, one variable — whether the planted `  | S881 |` row is indented. `mirror/` and `mirror-a3/` are the "lane roots" the census derives from `--file` (`dirname(file)/..`, `sources-census.sh:497-503`), with `corpus/knowledge`, `corpus/lessons`, `SKILL.md` symlinked so E11 (used-by on disk) resolves without copying 13 MB.

```
## 1. fixture A1 — unmodified copy (baseline, no planted row)
census rows: 799
validate exit: 0  (E-codes: 0; W-codes: 28)
A1 ids: reg.col0=799 reg.guard=799 staged=132
A1 collisions: col0=17 guard=17 -> identical: yes

## 2. fixture A2 — same copy + PLANTED INDENTED row (2 spaces) before the closing table
S875 row at scratch line: 830
planted line, leading spaces + first 60 chars (cat -A):
831:  | S881 | Planted guard fixture (Enguehard 2022, ojs.unito.it art$
leading-space count on planted line: 2
census rows (parser sees the indented row): 800
validate exit: 0  (E-codes: 0; W-codes: 28)
validate findings naming S881 (must be none): 0
A2 ids: reg.col0=799 reg.guard=800 (guard must be +1)
A2 control (column-zero-only): sees S881? 0  collisions=17
A2 guard   (0-3 spaces)     : sees S881? 1  collisions=18
A2 delta (guard minus control):
  S881

## 3. fixture A3 — separability: copy with the 17 pre-existing colliding rows dropped, planted indented row kept
A3 rows dropped: 17; census rows: 783
validate exit: 0  (E-codes: 0; W-codes: 28)
A3 control (column-zero-only) collisions: 0 ->
A3 guard   (0-3 spaces)      collisions: 1 -> S881

## 4. real pair (no fixture) — the item-10 command exactly as written in CORPUS.md
reg-ids=799 staged-ids=132 collisions=17
real column-zero-only control collisions: 17 (identical -> no indented row hides a collision today)

## 5. verdict
GUARD-PROOF: PASS
```

What each fixture establishes, and why all three are needed:

| fixture | registry state | column-zero control | 0–3-space guard | establishes |
|---|---|---|---|---|
| A1 | byte copy, no plant | 17 | 17 | today's registry is entirely column-zero (`grep -cE '^ +\|'` = **0**), so the guard's extra reach is latent — it costs nothing and hides nothing |
| A2 | + `  \| S881 \| …` | 17 (**S881 missed**) | 18 (**S881 caught**) | the control **false-greens**: a census-valid indented collision is invisible to `^\|` |
| A3 | A2 minus the 17 pre-existing colliding rows | **0 (empty)** | **1 (`S881`)** | separability: with no other collision in the fixture, the guard is the only thing that makes `collisions` non-empty |

The planted row is **census-valid**, which is the point of the proof: `sources-census.sh validate --file` exits **0** on A2 with the same 28 W04 warnings as the unmodified A1 and **zero findings naming S881**. The parser accepts 0–3 leading ASCII spaces (`sources-census.sh:40-42`; `row_pass`/`usedby_findings` both use `^ {0,3}`), and `census --file` counts the indented row (799 → **800**). So the census says "fine" and the broken extractor says "no collision" — the exact false-green item 10 warns about.

## 3. The five theme rows: staged ids vs lane ids

From `$A/theme-row-collision.txt` (driver `$A/analyze-map.py`, read-only):

```
## B. five theme staged rows: do their STAGED ids collide with lane ids?
staged  in reg-ids?  staged doc (first 90 chars of source cell)
S881    no           Guillaume Enguehard (2022), "Teaching linguistic methods with conlangs", *RiCOGNIZIONI. Ri
S882    no           М.Ю. Сидорова, О.Н. Шувалова, «Интернет-лингвистика: вымышленные языки», М.: «1989.ру», 20
S892    no           Новиков, Филипп Н. (2022), «Искусственные языки как семантические и семиотические системы»
S893    no           Костюхин, А. А. (2023), «Классификации конлангов в современной интерлингвистике», *Вестник
S901    no           Anderson, Catherine (McMaster); Grant, Margaret (Simon Fraser); Sanders, Nathan (Toronto),
```

**Verdict: none of the five theme rows collides.** The collision rule that actually holds is the numeric one — a staged id collides iff the lane already uses that number, i.e. **ids ≤ S875**. All five theme ids are > S875, and the 17-id collision set is exactly `S859..S875`. Stated per row:

| staged id | ≤ S875? | in `reg-ids`? | collision |
|---|---|---|---|
| S881 | no | no | none |
| S882 | no | no | none |
| S892 | no | no | none |
| S893 | no | no | none |
| S901 | no | no | none |

The collision set is also classified by document, not just by number (`analyze-map.py`, URL-normalized):

- **17/17 same-number pairs name a different document** — so no collision is an "already adopted at this number" case; each is a pure numeric clash needing renumbering only if ever adopted.
- **3 staged rows are already in the lane by URL under other ids**: staged **S863 → lane S874** (`ihchina.cn/project.html`), staged **S867 → lane S875** (`online.bunka.go.jp/db/heritages/search`), staged **S967 → lane S874** (the Wayback variant of the same ihchina page). Adopting any of these would be a within-scope URL duplicate (census E04): refuse or supersede, never renumber into a fresh id.

## 4. The adopted ids S876..S880 are absent from `reg-ids`

```
## C. adopted lane ids S876..S880: absent from reg-ids, and what they mean in each namespace
S876: in reg-ids=False  staged row with the same number names: Roland Barthes, "Introduction à l'analyse structurale des récits", *Communicatio
S877: in reg-ids=False  staged row with the same number names: 荻原 祐二 (2023),「名前を正しく読むことはなぜ難しいのか」/ "Why Reading Japanese Names Correctly Is Diff
S878: in reg-ids=False  staged row with the same number names: 「古代日本人の名前の研究」(2007 年度博士学位論文（要約） …
S879: in reg-ids=False  staged row with the same number names: 吉田 光男 (兰州大学 研究員レポート),「氏名は特定の記号として、人類社会に普遍」
S880: in reg-ids=False  staged row with the same number names: 「日本人著者の名前についての調査」, 『図書館学会年報』 39(1), 2005, 1–13
```

Registry shape at the 799-row state: rows **799**, distinct ids **799**, first **S001**, last **S875**. The registry is **not contiguous**: 76 numbers below the max are unoccupied — `S455-S480`, `S492-S499`, `S544-S559`, `S563`, `S577-S599`, `S777-S778`. Append-only therefore means "continue from `max(id)+1`", i.e. **S876**, never "fill the lowest hole".

The trap worth naming for the counter: lane S876..S880 will numerically equal **five other staged rows** (Barthes, 荻原, 古代日本人の名前, 吉田, 日本人著者の名前). Same number, different document, legal under the three-namespace rule — but any later adoption of staged S876..S880 must renumber by document, and every join in this round must stay URL-based. The same hazard is quantified across namespaces in `$A/register-id-overlap.txt`: the register's 21 kotodama data rows are `S776 S778 S779 S786 S787 S791 S792 S795 S796 S804 S807 S812 S814 S816 S817 S820 S823 S824 S825 S827 S835`, and **20 of those 21 are also lane ids** (only S778 is not; 0 of 21 are staged ids). Numeric equality across register and lane is meaningless — only URL joins count.

## 5. Round-71 map staleness, re-derived

Source: `.ufo/waves/round-71/assimilation/id-renumber-map.json` (read-only; bytes untouched). Its own state: `registry_count 797`, `next_free S874`, `span S874→S1005`, 132 entries, `collisions` = S859..S873 (15), and the mapping is **pure arithmetic** (`staged + 15`: S859→S874 … S990→S1005).

```
## E. round-71 map staleness (registry_count 797, next_free S874 -> now 799 rows, last S875)
old map: registry_count=797 staged_count=132 next_free=S874 span=S874→S1005 entries=132
old collision list n=15 last=S873   now n=17 last=S875
old-map entries whose TARGET is now an occupied lane id: n=2
  staged S859 -> S874 OCCUPIED; lane S874 now names: 中国非物质文化遗产网 · 中国非物质文化遗产数字博物馆（文化和旅游部主管）,「国家级非物质文化遗产代表性项目名录」清单页 — https://www.ihchina.cn/project.h
    staged S859 document: GB/T 33661-2017《农历的编算和颁行》… record page
  staged S860 -> S875 OCCUPIED; lane S875 now names: 文化遺産データベース（文化庁, Agency for Cultural Affairs）, 文化財検索 — https://online.bunka.go.jp/db/heritages/s
    staged S860 document: 中国科学院紫金山天文台（国家天文台）,《国家标准〈农历的编算和颁行〉解读材料》…
old-map targets still free: n=130 (all targets S876..S1005, none occupied)

old-map targets for the five theme rows (offset +15 arithmetic):
  staged S881 -> old target S896; round-73 document-derived target S876
  staged S882 -> old target S897; round-73 document-derived target S877
  staged S892 -> old target S907; round-73 document-derived target S878
  staged S893 -> old target S908; round-73 document-derived target S879
  staged S901 -> old target S916; round-73 document-derived target S880
```

Re-derived verdict — the map is stale in three independent ways, any one of which kills it:

1. **Two entries now map onto occupied ids**: `S859 → S874` and `S860 → S875`. Both targets are live lane rows naming **unrelated** documents (PRC ICH project list; Agency for Cultural Affairs heritage DB). Writing there would duplicate ids (census E03).
2. **All 132 targets carry a dead offset.** The lane appended 2 rows after the map was written, so the next free id is S876 while the map starts at S874. The five theme rows would land at S896/S897/S907/S908/S916 — 20 ids too high, leaving an un-fillable hole that append-only order forbids.
3. **Its collision list is two ids short**: it lists S859..S873 (15); the real set at 799 rows is S859..S875 (17).

The map's own `stale_warning` ("apply only from S874+") is therefore itself stale — applying from S874+ still lands on S874/S875.

## 6. Regenerated map (supersedes round-71, old→new recorded)

Written to `$A/id-renumber-map.json` (9.7 KB, `json.load` verified). It supersedes the round-71 file without touching it (`superseded_file_untouched: true`) and is a companion to ScoutMapIds's `id-renumber-map-draft.json` (same five targets; this file adds per-row collision class, namespace overlap and the staleness re-derivation).

| staged | staged line | document (URL identity is the evidence) | old target | **new lane id** |
|---|---|---|---|---|
| S881 | `SOURCES.append.md:29` | Enguehard 2022, RiCOGNIZIONI 9(18) — `ojs.unito.it/…/view/7099` | S896 | **S876** |
| S882 | `:30` | Сидорова/Шувалова 2006 booklet — `philol.msu.ru/~sidorova/files/conlangs.pdf` | S897 | **S877** |
| S892 | `:40` | Новиков 2022, Вестник РУДН 13(2) — `journals.rudn.ru/…/31528/20955` | S907 | **S878** |
| S893 | `:41` | Костюхин 2023, Вестник МГЛУ 2(870) — `cyberleninka.ru/…/klassifikatsii-konlangov…` | S908 | **S879** |
| S901 | `:49` | Anderson/Grant/Sanders, CJL SoTL — `sanders.phonologist.org/…/anderson-etal-cjl-sotl.pdf` | S916 | **S880** |

Per-row evidence, re-derived here (not copied from the draft): the entry's `source:` line carries the identical URL (`conlang-scholarship.md:4,5`; `conlang-scholarship.amend-2026-10-23.md:4,30,31`), the lane registry contains **0** rows for each host (`ojs.unito.it`, `philol.msu.ru`, `journals.rudn.ru`, `cyberleninka.ru`, `sanders.phonologist.org`), and the target id is absent from `reg-ids`.

Order rule recorded explicitly: **staged-id ascending**, and order is a free choice — the binding constraint is per-row URL identity, never arithmetic. (Entry reading order is *not* the rule: the amend cites S901 first and is still mapped after S892/S893.)

**Conditional sixth row.** The amend also cites **S894** (`conlang-scholarship.amend-2026-10-23.md:32` + three inline mentions; staged `:42`, DOI `10.1017/cnj.2024.21`, register row S812, quarantine). If the quarantine seat admits it, its id is **S881** — which numerically equals staged S881 (Enguehard). If it is refused, the amend must drop line 32 and its inline mentions (claim kill rule) and no sixth id is issued. The map records this as `conditional_assignments`, not as an assignment.

## 7. Notes the counter/scribes need (read-only observations, no widening)

- `COLLCHECK` as written ("collisions file … has zero id tokens for the adopted ids") holds **only for the five adopted ids**: the file legitimately carries 17 tokens, so the leg must test for `S876..S880` (and `S881` if S894 is admitted), not for an empty file.
- The claim's `REPOINTED` leg names S728/S769/S806 as campaign ids that must vanish. I re-confirmed the S728 case against the lane: `corpus/SOURCES.md:683` = Henrike Frye 2022, *Child-directed Speech in Qaqet* — unrelated to the conlang theme. The map records all three with their lane documents.
- A3's "drop the 17 colliding rows" step is fixture-only; the real registry must never be edited that way.
- The lane's own end-of-round census (`validate --root … kotodama`) was **not** run by this seat — leaf rule: no lane-gate execution while the wave is in flight. What I ran is scratch-mirror validation only (§2), and its exit 0 is evidence for the fixture, not for the lane.

## 8. Files written (all under `$A` + this report)

- `$A/reg-ids`, `$A/staged-ids`, `$A/collisions` — the item-10 outputs (799 / 132 / 17).
- `$A/guard-proof/run-guard-proof.sh`, `guard-proof.txt` (PASS, exit 0), `mirror/`, `mirror-a3/`, `validate-A1..A3.txt`, `A1.*`, `A2.*`, `A3.*`, `A3.dropped-ids`.
- `$A/theme-row-collision.txt` (driver `$A/analyze-map.py`), `$A/register-id-overlap.txt`.
- `$A/id-renumber-map.json` — the regenerated map superseding round-71 (round-71 bytes untouched; `id-renumber-map-draft.json` untouched).
- This report: `.ufo/waves/round-73/w1/ExecRenumber.md`.

One stray: an early draft wrote `/tmp/reg-slice-ids.txt`; it was deleted and its content re-filed as `$A/register-id-overlap.txt` (with backticks stripped — the register's id cell sometimes carries a trailing backtick, which is why the first pass undercounted the overlap 17 → 20/21).

**Blockers: none.** The guard is proved, the five theme rows do not collide, S876..S880 are free, and the round-71 map is superseded with old→new recorded.
