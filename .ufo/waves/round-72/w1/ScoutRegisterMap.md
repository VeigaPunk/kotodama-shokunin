# ScoutRegisterMap — register→staged id mapping, independent re-derivation

Seat: `L1Kotodama72.ScoutRegisterMap` (round 72, w1) · date 2026-10-25 · leaf, no dispatch.

Scope: the 21 `kotodama` rows of the absent-defect register and the staged
`SOURCES.append.md` ids they were URL-matched to at
`.ufo/waves/round-72/assimilation/reg-to-staged.txt`.

## Verdict

**The mapping is CORRECT. All 21 rows map to the right staged id(s). Zero corrections
needed to the id sets.** Every register row's URL matches at least one staged row — no
orphan row. Re-derived independently by exact-URL match over all 132 staged rows, with
prefix-match fallback for the one register row whose URL is truncated in the register
itself: **21/21 agreement** with `reg-to-staged.txt`.

Two defects found, both in the **artifact** (not the mapping's substance):
1. `reg-to-staged.txt` carries **truncated URLs for 4 rows** (S776, S791, S795, S796) —
   the map's own URL column is a 70-char prefix, not the register URL. The id sets are
   still right, but the file is not re-derivable from its own URL column by exact match.
2. The map keys the 3 unreachable-class rows as ``S807` `` / ``S812` `` / ``S835` ``
   (trailing backtick, inherited from the register's own malformed id cells). A grep for
   `^S[0-9]{3}` will not match them; any downstream id-collision check must strip the
   backtick first.

## The 21 rows, re-derived

Register URL column → staged ids. "exact" = byte-identical URL string after
trailing-slash normalisation; "prefix" = register URL is a strict prefix of the staged
URL (register-side truncation).

| register id | class | register URL → staged ids | how | map says | ✓ |
|---|---|---|---|---|---|
| S776 | payload-absent | `openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296` → **S859, S932** | exact ×2 | S859, S932 | ✓ |
| S778 | payload-absent | `eco.mtk.nao.ac.jp/koyomi/` → **S861** | exact | S861 | ✓ |
| S779 | payload-absent | `nao.ac.jp/news/topics/2026/20260202-rekiyoko.html` → **S862** | exact | S862 | ✓ |
| S786 | payload-absent | `conlang.org/26c3.pdf` → **S869** | exact | S869 | ✓ |
| S787 | payload-absent | `chinawriter.com.cn/n1/2023/0922/c404024-40083104.html` → **S870** | exact | S870 | ✓ |
| S791 | payload-absent | `ir.psych.ac.cn/bitstream/311026/14751/2/%E5%90%8D%E5%AD%97%E7…` → **S874** | prefix (register URL truncated at 140 chars) | S874 | ✓ |
| S792 | payload-absent | `journal.psych.ac.cn/xlkxjz/EN/10.3724/SP.J.1042.2021.01067` → **S875, S933** | exact ×2 | S875, S933 | ✓ |
| S795 | payload-absent | `obirin.ac.jp/academics/postgraduate/international_studies/course_humanities/…/BC-2-1-5-2-4_02.pdf` → **S878** | exact | S878 | ✓ |
| S796 | payload-absent | `kankyo-u.ac.jp/f/introduction/research/innovation/field/189.pdf` → **S879** | exact | S879 | ✓ |
| S804 | payload-absent | `kotobank.jp/word/苗字-392782` → **S886** | exact | S886 | ✓ |
| S814 | payload-absent | `lishisuo.cssn.cn/xsyj/qhs/yjcg/202103/t20210316_5318560.shtml` → **S897** | exact | S897 | ✓ |
| S816 | payload-absent | `chinawriter.com.cn/n1/2025/0605/c404024-40494534.html` → **S899** | exact | S899 | ✓ |
| S817 | payload-absent | `chinawriter.com.cn/n1/2022/1207/c404024-32582252.html` → **S900** | exact | S900 | ✓ |
| S820 | payload-absent | `onomastica.ijppan.pl/index.php/ONOM/article/download/574/763/` → **S903, S934** | exact ×2 | S903, S934 | ✓ |
| S823 | payload-absent | `chinafolklore.org/web/index.php?NewsID=10867` → **S906** | exact | S906 | ✓ |
| S824 | payload-absent | `ir.library.osaka-u.ac.jp/repo/ouka/all/77834/gbg_018_197.pdf` → **S907** | exact | S907 | ✓ |
| S825 | payload-absent | `digital.archives.go.jp/search` → **S908, S935** | exact ×2 | S908, S935 | ✓ |
| S827 | payload-absent | `doi.org/10.1007/978-3-032-03277-5_15` → **S910** | exact | S910 | ✓ |
| S807`` ` | unreachable | `doi.org/10.34158/ONOMA.51/2016/8` → **S890** | exact | S890 | ✓ |
| S812`` ` | unreachable | `doi.org/10.1017/cnj.2024.21` → **S894** | exact | S894 | ✓ |
| S835`` ` | unreachable | `omu.repo.nii.ac.jp/record/4358/files/2014000035.pdf` → **S918, S936** | exact ×2 | S918, S936 | ✓ |

**No register row matches zero staged rows.** The 4 rows matching two staged rows are
each a **live + archived-capture pair of the same document** — the paired ids are
content-consistent siblings, not competing attributions:

- S776 → S859 (live `newGbInfo` route) + S932 (same URL via Wayback `20260424031027id_`).
  S938 is a *third* staged row for the same standard at a *different* route
  (`showGb?type=online`), correctly **not** matched by URL. I verified live that
  `showGb` and `newGbInfo` return byte-identical bodies (both 24058 B,
  md5 `135a118d4690cb136dae9002fd6a8f04`).
- S792 → S875 (live EN) + S933 (same EN URL via Wayback `20220630094933id_`). S966/S969
  are the CN-mirror siblings at different URLs, correctly not matched.
- S820 → S903 (live PDF) + S934 (same PDF via Wayback `20251231111748id_`).
- S825 → S908 (live) + S935 (same URL via Wayback `20260422145052id_`).
- S835`` ` → S918 (live PDF) + S936 (same PDF via Wayback `20251010013419id_`).

## Flag: 2 of the 5 multi-match pairs are NOT content-identical — the archive capture
## now serves a *different paper* than the staged row claims

This is the one substantive flag. Both pairs below are pairs where the staged row's
**archive-capture citation no longer matches the bytes at that capture**.

### S820 — S934's anchor is wrong about which paper the capture holds

S934 describes the capture `20251231111748id_` of `…/ONOM/article/download/574/763/` as
Słon, «Names and the named: gender, femininity and given names in Poland», *Onomastica* 68,
and quotes it as «standard given names with lexemes reflecting feminine softness and
female aesthetic **associations**».

I fetched that exact capture (sha1-b32 `ZCYDDH2NSNNGJESPPEKUQTJVACTNUBDG`, matching the
Wayback CDX digest for `20251231111748`) and extracted its text. It is **not** Słon's
paper. It is:

> `https://doi.org/10.17651/ONOMAST.69.7` / `Onomastica LXIX, 2025` / `IRENA KAŁUŻYŃSKA`
> / **FLOWERS, PLANTS, AND TREES IN FEMALE NAMING IN CHINA**

— i.e. the *same* paper as S903 (the live row), not a second paper. Occurrence counts in
that capture: `Słon` 0, `Poland` 0, `Names and the named` 0, `Onomastica 68` 0,
`Onomastica LXIX` 1, `ONOMAST.69.7` 1. The phrase S934 quotes,
`female aesthetic associations`, occurs **0** times; the actual text reads
`…reflecting feminine softness and female aesthetic **values**`. The live PDF at the same
URL is the same Kałużyńska paper (`grep -c 'Kałużyńska'` = 13, reproducing S903's
recorded receipt), and the journal's own landing page for that article id
(`/ONOM/article/view/574`) is titled *Flowers, plants and trees in female naming in China*.

So: **S934 is a duplicate of S903 wearing a wrong paper identity**, and S903's own
recorded `grep -c 'Kałużyńska' -> 13` receipt is the one that reproduces. The register
row S820's own quote (`such names may be classified as 'standard given names with
lexemes…`) **is present** in the live PDF (present under punctuation-normalised match),
so the register's `payload-absent` verdict for S820 does not hold against the live
document either — the round-71 verdict file's `PRESENT` call for S820 is the correct one.

### S835`` ` — S936's anchor names a paper that is not in the capture

S936 describes the capture `20251010013419id_` of the omu PDF as *"the reference list in
the deposited article 纳日碧力戈・左振廷, « 三维铸牢中华民族共同体意识 », 中央民族大学学报
47(1), 2020"*, quoting the 参考文献 entry for 纳日碧力戈's book.

I fetched that exact capture (content-length 562907, `x-archive-orig-date: Fri, 10 Oct
2025`). It is the **same Japanese article** as the live file and as S918:
「名前から見る古代貴族の家族観」by 潘 蕾, 大阪府立大学人文学会 人文学論集 第32集 (2014),
DOI 10.24729/00004351. Occurrence counts in that capture: `三维铸牢` **0**,
`中央民族大学` 1 (and that single hit is the *publisher* field inside the 参考文献 entry
itself), `纳日碧力戈` (simplified) 0, `納日碧力戈` (traditional) 1, `名前から見る` 11.
The live file and the capture are **not** byte-identical (564692 B vs 562907 B, differing
md5) but they are the same article with the same 参考文献 block; the 纳日碧力戈 entry
(`納日碧力戈『姓名』中央民族大学出版社、2000`) is present in both.

So: **S918 and S936 describe one document with two different (mutually exclusive)
paper identities**, and S936's is the wrong one — the deposited article is 潘蕾's
Japanese paper on aristocratic family names, not 纳日碧力戈・左振廷's Chinese-language
article. S936's own recorded receipt is `pdftotext -layout - -` with **no grep count**,
so it carries no falsifiable assertion; S918's `grep -c '納日碧力戈' -> 1` reproduces
against the live file (I measured 1).

Also note S918 attributes the PDF to 明治大学 (明治大学 Academic Heritage). The
document's own front matter says 大阪府立大学人文学会 / 人文学論集 第32集 (2014), and the
hosting repository is `omu.repo.nii.ac.jp` (大阪公立大学 / Osaka Metropolitan University).
The staged file contains **no** occurrence of 大阪府立 anywhere, so this misattribution
is uncorrected in the staged set.

## Flag: 2 of the 5 archive-capture receipts do not reproduce as recorded

Both are "the live page no longer serves this text" claims where the live page now
*does* serve the text (or the capture does not contain it). This bears on the
`unreachable`/`withdrawn` framing the map inherits.

| staged row | recorded receipt | measured today (2026-10-25) |
|---|---|---|
| S932 | `grep -c '主管部门 中国科学院' -> 1` on the `20260424031027id_` capture | **0** — the live and archived HTML separate the label and value into different `<div>`s (`<div class="…title"> 主管部门 </div> <div class="…content"> 中国科学院 </div>`), so the literal one-space string never occurs. Reproduces only with whitespace/tag normalisation. |
| S933 | `grep -c '自我信息加工取向' -> 1` on the `20220630094933id_` capture | **2** (stable over two runs) |
| S935 | `grep -c '開始西暦年' -> 1` on the `20260422145052id_` capture | **3** |

The live counterparts still serve their quoted text, which contradicts the "the live
page no longer carries the quoted text" framing in S932 / S933 / S935:
- `openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=…` (live): `标准号：GB/T 33661-2017` ✓,
  `标准状态：现行` ✓, `发布日期 2017-05-12` ✓, `实施日期 2017-09-01` ✓, `主管部门` ✓,
  `中国科学院` ×2 ✓. S859's own receipt `grep -c '主管部门' -> 1` reproduces (measured 1).
- `journal.psych.ac.cn/xlkxjz/EN/…` (live): all four orientation labels present
  (2× each); S875's receipt `grep -c 'name uniqueness' -> 4` reproduces (measured 4).
  The CN mirror is live too (`实际影响取向` ×8, `含义效价` ×3).
- `digital.archives.go.jp/search` (live): `元号名称` ×3, `開始西暦年` ×3, and the era
  table rows 令和 2019 / 平成 1989 / 昭和 1926 / 大正 1912 / 明治 1868 are all present as
  `<td class="gengo-modal__td--label">…</td><td>…</td>` rows. S908's receipt
  `grep -c '元号名称' -> 3` reproduces (measured 3).

## Flag: the map's URL column is truncated for 4 rows (artifact defect)

`reg-to-staged.txt`'s URL column disagrees with the register and with the sibling
`reg-urls.tsv` for 4 of 21 rows. All four are 70-char prefixes of the real URL:

| id | map URL len | register/tsv URL len | example |
|---|---|---|---|
| S776 | 70 | 84 | map ends `…hcno=E107EA4DE9725EDF81`, real ends `…EDF819F33C60A44B296` |
| S791 | 70 | 140 | map ends `…%E5%90%8D%E5%AD%97%E7%` |
| S795 | 70 | 128 | map ends `…/international_studies/` |
| S796 | 70 | 74 | map ends `…/field/189` (drops `.pdf`) |

Consequence: re-running the map's own URL column through an **exact**-match re-derivation
returns **zero** staged ids for these 4 rows — they only resolve under prefix matching.
The id sets are nevertheless correct (the truncated prefix is unique to the right staged
row; I verified prefix matching on the truncated URLs pulls in **no extra** ids). So this
is a reproducibility defect in the artifact, not a mis-mapping. Recommend the map carry
the full register URL, or carry the register's URL verbatim from `reg-urls.tsv`.

## Cross-check: the mapping is NOT arithmetic (good news for claim C's REPOINTED leg)

The staged id is `register id + 83` for 19 of 21 rows and `+ 82` for two (S804→S886,
S812→S894). Had the map been produced by a shift rather than by document, those two
would be wrong — and they are not:

- S804 (kotobank 苗字) → **S886** (苗字). `+83` would give **S887** = 平安時代
  (kotobank/word/平安時代-128778) — a different document.
- S812`` ` (doi 10.1017/cnj.2024.21) → **S894** (Sowers-Wills, *Canad. J. Linguistics*
  69(3)). `+83` would give **S895** = 王昕玥《论〈龙族〉的叙事失控与世界观危机》
  (chinawriter 2025) — a different document.

So the map is document-derived, and the two off-by-one rows are the discriminating
evidence. This supports the REPOINTED leg's "re-pointed **by document**, no arithmetic"
requirement.

## Notes for downstream consumers of this map

1. **Strip the trailing backtick** from ``S807` ``, ``S812` ``, ``S835` `` before any
   id-set operation. `grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3}'` will not match them.
2. **Register ids are not a global key.** Across the whole register, 65 ids are reused
   by more than one lane (e.g. S037 = audio/round2 *and* kasegi/round1); all 65
   collisions are cross-lane. The register's key is `(lane, round, id)`, not `id`. The
   21 kotodama ids are unique within the lane, and none of them collides with another
   lane's row.
3. **Register ids live in a different id space from the lane registry.** The lane's
   `corpus/SOURCES.md` uses S859–S875 for completely different documents (UNESCO ICH
   dance entries, the settlement-state classifier) than the staged file's S859–S875.
   The staged file's ids are the *merge-package* numbering; the lane's own registry
   already occupies that numeric range. The lane's new rows **S874/S875** (ihchina /
   bunka) therefore sit numerically inside the staged package's own S859–S875 block.
   I confirmed the re-point chain the claim's REPOINTED leg requires: lane S874 carries
   **all** of staged S863's and S967's URLs (3/3), and lane S875 carries staged S867's
   URL (1/1) — so S863/S867/S967 are re-pointed by document, and no id collides with the
   *register's* id space (S874/S875 do not appear among the register's 219 distinct ids;
   the register's numeric range is 33–835).
4. The register's own `Totals` section overstates its coverage: it claims 194 rows with
   194 payload-absent, but the file carries a second, differently-shaped table (5 columns,
   not 7) for the `unreachable` class whose rows carry the malformed `S807\``-style ids
   and a class description where the `payload-absent` column would be. That second
   table is the source of the 3 backtick ids and is not covered by the Totals.

## Method / evidence

- Register: `/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md`,
  lines 118–135 (18 payload-absent rows) and 333–335 (3 unreachable rows).
- Staged: `/home/vgpnk/Projects/shokuknow/merge/kotodama/SOURCES.append.md` — 132 staged rows.
- Re-derivation: exact URL equality (trailing-slash-normalised) against every URL
  extracted from each staged row's source cell, then prefix matching; plus the reverse
  check (staged→register) to confirm no staged row was left unmapped and no row was
  double-claimed.
- Live verification: all 21 register URLs fetched (18 succeeded; `lishisuo.cssn.cn` now
  returns HTTP 403 — a fetch failure, not a mapping failure; S807/S812 DOI resolves to
  open metadata with no quoted span, matching the register's `unreachable` class).
  Wayback CDX + direct capture fetches for the four archive-cited ids (S932, S933, S935,
  S936), with sha1-base32 digests checked against the CDX records.
- Quote presence tested at three strictness levels (raw substring → tag-stripped →
  punctuation/whitespace-normalised → ordered subsequence) and with GB18030 / EUC-JP
  decoding where the page requires it (`chinafolklore.org` is GB18030; `eco.mtk.nao.ac.jp`
  is EUC-JP — decoded, both S778 fragments are present).
- Downloads: `/tmp/ScoutRegisterMap/` only (scratch fetch dir `fetch/`); nothing written
  outside the lane's assigned report path.
- No tools installed or upgraded for this seat.
