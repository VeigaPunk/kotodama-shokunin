# ExecRenumber — collision guard + by-document id map (round 74, w1)

Seat: ExecRenumber (leaf). Lane repo: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Base revision `f7104cbce186bc2e1522abf0cfd619cc834628bb` == `git rev-parse HEAD`.
Lane `corpus/SOURCES.md` is byte-identical to that base (`git diff <base> -- corpus/SOURCES.md`
empty, sha256 `93d6046444f2170e14514b2cc50cd21267a9592dc319513dd79fbffc3d018774`).
Nothing was written outside `.ufo/waves/round-74/assimilation/` and
`.ufo/waves/round-74/w1/ExecRenumber.md`; `/home/vgpnk/Projects/shokuknow` was read only
(mtimes still 2026-10-24) and no campaign tool was run.

## 1. The item-10 guard, run exactly as CORPUS/prompt specify

    S=/home/vgpnk/Projects/shokuknow
    A=/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-74/assimilation; mkdir -p "$A"
    grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md \
      | grep -oE 'S[0-9]+' | sort > "$A/reg-ids"
    grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' "$S/merge/kotodama/SOURCES.append.md" \
      | grep -oE 'S[0-9]+' | sort > "$A/staged-ids"
    comm -12 "$A/reg-ids" "$A/staged-ids" > "$A/collisions"

Observed:

| file | lines | sha256 |
|---|---|---|
| `$A/reg-ids` | 804 (S001 … S880) | `94a495c7d634123c0d40e6895b7916892e204f450a536ce00cf4af9aef26ca86` |
| `$A/staged-ids` | 132 (S859 … S990) | `bab11d7d0ee0d84795b1ff80274fe371670fff73a477c747b2fd3cad4c25ddad` |
| `$A/collisions` | **22** | `130ec2d15f923b005a9a91f03e8a9a949a9233d8b70f432663d93031ee041721` |

    collisions = S859 S860 S861 S862 S863 S864 S865 S866 S867 S868 S869 S870 S871 S872
                 S873 S874 S875 S876 S877 S878 S879 S880

Re-derived a second time and `cmp`-ed against the three stored files: `reg-ids reproduced`,
`staged-ids reproduced`, `collisions reproduced`. Inputs: staged package sha256
`7fb4f488807e8364d204a3081a2e57379d6caafaa92dbab9dfbc381757223754`, red
register sha256 `5afe1810a6c3d62f37987b575a954f5b1197daa23005d4bb2f1d982f64bad833`.

## 2. Guard proof (scratch, committed as wave evidence)

`$A/guard-proof/` — `make-fixtures.py`, `run-guard.sh`, `README.md`, mirrors
(`mirror-control|2sp|3sp|4sp/corpus/SOURCES.md`), and `out/*` with every command output.
Each mirror is the real registry with ONE planted row inserted after S880 inside the Registry
table: a clone of lane row S880 with the id cell set to `S883` (a **staged** id) and its URLs
rewritten to `example.invalid/guard-proof/planted.pdf`; `corpus/knowledge`, `corpus/lessons`
and `SKILL.md` are symlinks to the lane's real objects so census E11 resolves as on the lane.

| fixture | census `rows` | item-10 ids | item-10 sees S883 | `collisions` | column-zero pattern sees S883 | census exit / findings |
|---|---|---|---|---|---|---|
| control (no plant) | 804 | 804 | 0 | 22 | 0 | 0 / 28 (all W04) |
| 2 spaces | **805** | **805** | **1** | **23** | **0** | 0 / 28 (all W04) |
| 3 spaces | **805** | **805** | **1** | **23** | **0** | 0 / 28 (all W04) |
| 4 spaces (code block) | 804 | 804 | 0 | 22 | 0 | 0 / 28 (all W04) |

Exact control-pattern command pair:

    ITEM10='^ {0,3}\|[[:space:]]*S[0-9]{3,}'; COLZERO='^\|[[:space:]]*S[0-9]{3,}'
    grep -oE "$ITEM10"  mirror-2sp/corpus/SOURCES.md | grep -oE 'S[0-9]+' | grep -c '^S883$'   # 1
    grep -oE "$COLZERO" mirror-2sp/corpus/SOURCES.md | grep -oE 'S[0-9]+' | grep -c '^S883$'   # 0  <- false green

Verdict: **the guard is proven and the column-zero-only pattern is the false-green CORPUS.md
warns about.** 0–3-space rows are rows to the census and to the item-10 pattern (`rows` 805,
`collisions` 23, no new census finding — the planted row itself is clean); a 4-space row is
indented code to both (`rows` 804, no collision). The census exit code is 0 for every mirror
because the only findings are the lane's pre-existing 28 W04 duplicate-URL warnings, identical
in the control.

## 3. Do the four theme staged ids collide with lane ids? — the premise is FALSE

The dispatch parenthetical ("the lane holds S883/S884/S899/S900 as different documents") does
**not** hold. Verified in three ways:

    $ grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md
    804                                   # last id S880 (S878/S879/S880 rows printed)
    $ grep -cE '^S(883|884|899|900)$' "$A/reg-ids"
    0
    $ grep -nE '^ {0,3}\| *S(883|884|899|900) *\|' corpus/SOURCES.md
    (no output)
    $ grep -cE '^S(883|884|899|900)$' "$A/collisions"
    0

Fleet-wide cross-check (read-only, all lane registries):

    $ for d in */corpus/SOURCES.md; do [ -f "$d" ] || continue; echo "$d rows=$(grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' "$d") max=$(...sort -n|tail -1) theme_hits=$(grep -cE '^ {0,3}\|[[:space:]]*S(883|884|899|900)[[:space:]]*\|' "$d")"; done
    ... every lane: theme_hits=0 ; kotodama rows=804 maxnum=880 (highest in the fleet)
    (kumitate 200, tsukuroi 207, souji 215, kotoba 222, tameshi 260, mado 289, kama 329,
     kake 422, mori 484)

So at base **and** at worktree HEAD no lane — kotodama or any sibling — holds S883, S884, S899
or S900. What is actually true, and is what the map handles:

1. **Post-adoption** the lane will hold `S883` = chinawriter 2025/0605 interview and `S884` =
   chinawriter 2022/1207 article — documents different from staged `S883` = litmemo and staged
   `S884` = tuduku. That is a two-id cross-namespace numeric overlap created by the adoption
   itself, resolved by one simultaneous substitution, not a pre-existing collision.
2. No lane id `S899`/`S900` exists now or after adoption; those staged ids (the chinawriter rows
   themselves) collide with nothing and simply retire.
3. `$A/collisions` is nonempty (22) **before** the theme touches it: staged `S859..S880`
   numerically overlap lane `S859..S880`, and **0 of 22 pairs name the same document** (URL
   join below). The file is therefore not evidence for the dispatch parenthetical; no adopted
   row is implicated and no adopted document is already in the lane under another id.

Naming what the lane holds under those numbers anyway (for the record, from the lane registry):
`S883`, `S884`, `S899`, `S900` — none exist. The nearest lane ids are `S878` (Новиков 2022,
RUDN semiotics), `S879` (Костюхин 2023, MSLU), `S880` (Anderson/Grant/Sanders, CJL SoTL).

## 4. By-document map — `$A/id-renumber-map.json`

Written, sha256 `d3573f7d3cf23afa7296c281d201225eed643aef2b406b3a403c2a67aeb24afa`. Join key is
the normalized URL (lowercase host without `www.`, stripped trailing slash, query kept); never
arithmetic. Contents:

| staged id | line in `SOURCES.append.md` | document | URL | new lane id | lane URL hits |
|---|---|---|---|---|---|
| S883 | 31 | LitMemo 創作ノート「小説の世界観はどう作る？」 | https://litmemo.com/ja/blog/novel-worldbuilding-guide | **S881** | 0 |
| S884 | 32 | tuduku.space コラム「Web小説の世界観・設定の作り方」 | https://tuduku.space/column/novel-worldbuilding | **S882** | 0 |
| S899 | 47 | 爱潜水的乌贼 网络文学"破壁者"访谈（文汇报/邵燕君等）, 中国作家网 2025-06-10 | https://www.chinawriter.com.cn/n1/2025/0605/c404024-40494534.html | **S883** | 0 |
| S900 | 48 | 爱潜水的乌贼：网络文学不断"升级"的"奥术"（《青春》李玮）, 中国作家网 2022-12-07 | https://www.chinawriter.com.cn/n1/2022/1207/c404024-32582252.html | **S884** | 0 |
| S882 | 30 | Сидорова/Шувалова, «Интернет-лингвистика: вымышленные языки» (2006) | http://www.philol.msu.ru/~sidorova/files/conlangs.pdf | **S877 — reused, NOT appended** | 1 (S877) |

URL presence probes: `grep -c litmemo` = 0, `grep -c tuduku` = 0, `grep -c chinawriter` = 0,
`grep -c philol.msu.ru` = 1 (lane S877). None of `S881..S884` appears in `reg-ids`
(registry state: 804 rows, S001..S880, next free S881, next free after adoption S885).

`substitution_rule` recorded in the file: **simultaneous single pass** over the old ids with one
lookup table — staged `S883→S881`, `S884→S882`, `S899→S883`, `S900→S884`, `S882→S877` are all in
the same table and the targets are also staged ids, so any sequential second pass would
re-map an already-mapped lane id.

Document-level join across the whole package (why the 22 collisions are benign):

    8 staged->lane same-document pairs by normalized URL:
      S863->S874, S867->S875, S881->S876, S882->S877, S892->S878, S893->S879, S901->S880,
      S967->S874 (wayback form; S863 is the live form of the same lane row S874)
    same-document pairs among the 22 numeric collisions: 0

The map also carries the refusal context for the two chinawriter rows (rounds 68/71 quarantined
the staged *quoted spans*, not the pages; round 74 must quote the page) and the per-id lane
document for all 22 collisions.

## 5. Register-id overlap — `$A/register-id-overlap.txt`

sha256 `a50b983499d0df2f39064ac30deb7a4f957470f69092dd0c6184b737e7e150b8`.
Intersection of staged ids with register ids: **0**, against both the kotodama slice
(`comm -12 $A/staged-ids /tmp/regslice.ids | wc -l` = 0) and the register's whole id universe
(`comm -12 $A/staged-ids /tmp/regall.ids | wc -l` = 0). Structurally: register max id = S835,
staged min id = S859. The file records what the adjacent register rows mean —
`S816`/`payload-absent`/chinawriter 2025/0605 (staged S899 → lane S883),
`S817`/`payload-absent`/chinawriter 2022/1207 (staged S900 → lane S884) whose registered span is
a *Sowers-Wills* passage carried by register row `S812` (`doi:10.1017/cnj.2024.21`), the pure
URL↔quote mispairing, and `S787` (chinawriter 2023/0922, the refused staged S870 document) —
plus two register facts that matter to the counter: the `## By lane` summary is stale
(`kotodama | 18` vs 21 derived data rows) and three data rows carry a trailing backtick in the
id cell (`S807\``, `S812\``, `S835\``, the `unreachable` prose family).

## 6. Round-73 map untouched

    $ P=.ufo/waves/round-73/assimilation/id-renumber-map.json
    $ git -C $L rev-parse f7104cb…:$P    -> 54fa7fdfa9330572686edf13309b1d87436eb7b0
    $ git -C $L rev-parse HEAD:$P        -> 54fa7fdfa9330572686edf13309b1d87436eb7b0
    $ sha256sum $L/$P                    -> 3010ac5b48613970cb8d1334a2f22bb15db1a7c577bfcd038191d90dfc8cc691
    $ git -C $L show f7104cb…:$P | cmp - $L/$P   -> identical
    $ git -C $L show HEAD:$P     | cmp - $L/$P   -> identical
    $ git -C $L status --porcelain -- $P         -> (empty)

The round-74 map supersedes nothing on disk: the round-73 map keeps its bytes, its blob and its
`S876..S880` targets; the only assignment they share is staged `S882 → S877`, a pre-existing
lane row.

## 7. Files written (all inside the assigned scratch/report paths)

| path | sha256 |
|---|---|
| `.ufo/waves/round-74/assimilation/reg-ids` | `94a495c7…ca86` |
| `.ufo/waves/round-74/assimilation/staged-ids` | `bab11d7d…ddad` |
| `.ufo/waves/round-74/assimilation/collisions` | `130ec2d1…1721` |
| `.ufo/waves/round-74/assimilation/id-renumber-map.json` | `d3573f7d…4afa` |
| `.ufo/waves/round-74/assimilation/register-id-overlap.txt` | `a50b9834…50b8` |
| `.ufo/waves/round-74/assimilation/guard-proof/{make-fixtures.py,run-guard.sh,README.md,staged-ids,mirror-*/corpus/SOURCES.md,out/*}` | see `guard-proof/out/*.summary.txt` |
| `.ufo/waves/round-74/w1/ExecRenumber.md` (this report) | — |

No repo file under `corpus/`, `reports/`, `.ufo/state`, `LOG.md`, `SCORECARD.md`, `SKILL.md`
was touched; `claims.json` was read only; the round-73 w2 seat files were left exactly as
inherited. Sibling seats concurrently added `assimilation/validate-notes.md`,
`assimilation/validate-receipt-draft.txt` and `assimilation/validate/SKILL.md`; those are not
mine and were not modified.

## 8. Risks / caveats

- **The dispatch parenthetical is wrong and must not be copied into the frozen claim.** The
  claim's `after` text and the counter must speak of the *post-adoption* overlap (lane S883/S884
  vs staged S883/S884) and of a 22-id staged-vs-lane drift with 0 same-document pairs — not of
  the lane already holding S883/S884/S899/S900.
- `$A/collisions` is nonempty and always will be while the package keeps its S859..S880 rows;
  a counter that treats "nonempty collisions" as failure will red the round for a benign state.
  The discriminator is the document join, not the file's emptiness.
- The 22-id drift is *not* repairable here (campaign-local ids stay campaign-local); if a later
  round adopts any of staged S859..S880 it must renumber by document, and the same single-pass
  rule applies.
- Guard proof scope: it proves the extractor on 0/2/3/4-space ASCII indents (the class CORPUS.md
  names). Tab-indented and lowercase ids were not tested by me; the mutation seat covers them.
- Census `validate --file` resolves `used-by` relative to `dirname(dirname(registry))`, so the
  mirror trees need the knowledge/lessons/SKILL.md symlinks to reach exit 0; a bare fixture file
  elsewhere returns exit 1 on E11 alone. Documented in `guard-proof/README.md`.
- A page's live status is not re-tested here: the chinawriter liveness/UA facts in the map are
  attributed to the L1 probe of 2026-10-25 (`/tmp/q74/`), not to a fetch by this seat.

Tool installs: none (no pacman, no uv/npx). Downloads: none.
