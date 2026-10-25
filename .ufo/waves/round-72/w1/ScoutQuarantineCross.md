# ScoutQuarantineCross — round 72 wave 1 (scout seat, read-only)

Seat: `L1Kotodama72.ScoutQuarantineCross`. Question: re-derive the round-71 quarantine
verdicts from committed evidence, map the register ids to staged ids, state the staged
REFUSED set, and confirm the adoption citations are outside the register slice.

Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` at HEAD `b60c7b1` (the round-72
frozen base). Read-only source tree: `/home/vgpnk/Projects/shokuknow` (no writes, no campaign
tools run there). No tools installed; no lane file mutated other than this report.

## 1. The three verdict sets re-derived — CONFIRMED

Source: `reports/round-71/telemetry/quarantine-verdicts.md` (sha256
`3f993b0c46642ab66af8c3e19b0912e999c14c5f29e0ed27b5c54e68c64512ea`, committed in `1d1b432`,
table re-derived in `57e0a72`; the file is clean in the worktree — `git status --porcelain`
returns nothing for it).

Parsed every table row with `^\|\s*(S\d+[`]*)\s*\|\s*(PRESENT|REFUSED|UNVERIFIABLE)\s*\|`:

| verdict | count | ids |
|---|---|---|
| PRESENT | 10 | S776, S778, S795, S796, S804, S820, S823, S824, S825, S827 |
| REFUSED | 7 | S779, S786, S787, S792, S814, S816, S817 |
| UNVERIFIABLE | 4 | S791, S807, S812, S835 |

**All three sets are exactly as claimed.** Set equality was checked as `set(parsed) == set(claimed)`
per label: every label returned `EQUAL`, no missing and no extra ids. 21 rows parsed, 21 unique
ids, no duplicates. The file's own tally line (`:36`) reads `PRESENT 10 · REFUSED 7 ·
UNVERIFIABLE 4 = 21`, consistent.

Slice/table bijection also holds: `.ufo/waves/round-72/assimilation/quarantine-slice` lists 21
ids (18 `payload-absent` + 3 unreachable-class) and the id sets are equal — `sorted(slice_ids)
== sorted(table_ids)` is `True`.

### Independent re-verification by live fetch (8 of 21 rows, 2026-10-25)

The register slice was re-fetched live and the quoted spans re-checked, rather than trusting
the filed notes. Fetched to `/tmp/ScoutQuarantineCross/` (scratch only).

| register row | verdict re-derived | evidence |
|---|---|---|
| S776 | PRESENT | HTTP 200, 24142 B. All five quoted metadata fragments present (`标准号：GB/T33661-2017`, `标准状态：现行`, `发布日期2017-05-12`, `实施日期2017-09-01`, `主管部门中国科学院`). |
| S778 | PRESENT | HTTP 200, 10291 B, header declares `charset=EUC-JP`. Decoded as EUC-JP both spans found (1 hit each). Confirms the round-71 correction (UTF-8 misdecode produced the garbage). |
| S779 | REFUSED | HTTP 200, title `令和9（2027）年暦要項の発表 | 国立天文台(NAOJ)`. Chinese spans `国务院先后于2006年` / `国家级非物质文化遗产代表性项目名录` → 0 hits. Confirmed. |
| S786 | REFUSED | PDF fetched (753374 B, `conlang.org/26c3.pdf` → redirects to `cl101.pdf`). Quote 1 `conlanging (n): the art and craft of making your very own language` → 1 hit; the Chinese quote `我喜欢把写小说想象成邀请读者走进一个由我搭建的幻想屋` → 0 hits. Multi-quote row fails. Confirmed. |
| S787 | REFUSED | HTTP 200, title `我是怎样创作网络小说的--网络文学--中国作家网`. Register quote `作品中的人物名字和地名` → 0 hits (the page does contain `世界观`×11 and `打开小说幻想屋的钥匙`×1 — the staged row S870's own subject). Confirmed. |
| S792 | REFUSED (with a caveat — see §5) | HTTP 200, 159831 B, title `Psychological and behavioral effects of personal names in real world…`. The exact quoted span `实际影响取向 / 社会认知取向 / 自我信息加工取向 / 文化产品取向` is **not** present as a contiguous string (neither with spaces+slashes nor whitespace-collapsed). |
| S804 | PRESENT | HTTP 200, 212464 B. Span found at index 52627 under punctuation-insensitive comparison: the source reads `日本人が名のる苗字は，決して中国人の考える姓ではない。` (fullwidth comma) vs the register's `、` (ideographic comma) — the filed note's "Japanese comma/ellipsis variation" is accurate. |
| S814 | REFUSED | HTTP 200, 143252 B, title `魏斌:單名與雙名：漢晉南方人名的變遷及其意義`. Quoted `次のように細分してもよい` → 0 hits. Confirmed. |
| S816 | REFUSED | HTTP 200, 48536 B. **sha256 of my live fetch is byte-identical to the committed capture** `.ufo/waves/round-71/assimilation/fetches/s816.html` (sha256 `a3b6640c…d5c`). Quote spans `考虑过` / `资深` / `容忍度` / `我自己就是` → 0 hits. Confirmed; round-68 also refused it. |
| S817 | REFUSED | HTTP 200, 62604 B, title `爱潜水的乌贼：网络文学不断"升级"的"奥术"--网络文学--中国作家网`. `Sowers-Wills` / `Phonology from the inside out` / `Sowers` → 0 hits. Confirmed. |

Also re-confirmed as UNVERIFIABLE by construction (the register supplies **no quoted span** for
these three, so no quote can be checked even though the sources now fetch — see
`.ufo/waves/round-71/w1/ScoutQuarantineFetch3.md:9-13`, which itself made this argument):
S807` `https://doi.org/10.34158/ONOMA.51/2016/8`, S812` `https://doi.org/10.1017/cnj.2024.21`,
S835` `https://omu.repo.nii.ac.jp/record/4358/files/2014000035.pdf`. S791's register URL is
truncated (`…%E5%90%8D%E5%AD%97%E7%`), so the exact document is unfetchable.

## 2. Register id → staged id mapping (`.ufo/waves/round-72/assimilation/reg-to-staged.txt`)

The map has 21 lines, one per register row, in the form
`<register-id> <url> -> ['<staged-id>', …]`.

**Structural check (all 21 lines):** every map URL is byte-equal to the register row's
`cited source` cell in
`/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md`
(21/21 match), and every listed staged id resolves to a row in
`/home/vgpnk/Projects/shokuknow/merge/kotodama/SOURCES.append.md` whose text contains that
same URL (21/21, 26 staged ids total, 0 mismatches). The map is a **URL join**, not an
arithmetic id relation — which is what makes it trustworthy.

### The mapping table

| register | verdict | staged ids |
|---|---|---|
| S776 | PRESENT | S859, S932 |
| S778 | PRESENT | S861 |
| S779 | REFUSED | S862 |
| S786 | REFUSED | S869 |
| S787 | REFUSED | S870 |
| S791 | UNVERIFIABLE | S874 |
| S792 | REFUSED | S875, S933 |
| S795 | PRESENT | S878 |
| S796 | PRESENT | S879 |
| S804 | PRESENT | S886 |
| S814 | REFUSED | S897 |
| S816 | REFUSED | S899 |
| S817 | REFUSED | S900 |
| S820 | PRESENT | S903, S934 |
| S823 | PRESENT | S906 |
| S824 | PRESENT | S907 |
| S825 | PRESENT | S908, S935 |
| S827 | PRESENT | S910 |
| S807` | UNVERIFIABLE | S890 |
| S812` | UNVERIFIABLE | S894 |
| S835` | UNVERIFIABLE | S918, S936 |

Five register rows carry **two** staged ids (S776→S859/S932, S792→S875/S933, S820→S903/S934,
S825→S908/S935, S835→S918/S936). In each pair the second id is a second staged row for the
**same document** (a companion/alternate row in the merge package), not a different document:
e.g. S932 is the `openstd.samr.gov.cn` registry-record row and S859 the `GB/T 33661-2017`
record row; S933 is the archive-capture companion of S875 (both `心理科学进展` 29(6):1067–1085);
S935 is the National-Archives database row companion of S908 (the search-form row);
S936 the reference-list row companion of S918. So the 21 register rows map onto **26** staged
ids, and the staged verdict sets below inherit that 1→N shape.

## 3. The staged REFUSED set — stated explicitly

**staged REFUSED = { S862, S869, S870, S875, S897, S899, S900, S933 }** (8 ids)

Derivation: the 7 REFUSED register rows {S779, S786, S787, S792, S814, S816, S817} union their
staged images.

For completeness, the other two staged sets:

* staged PRESENT (13) = { S859, S861, S878, S879, S886, S903, S906, S907, S908, S910, S932, S934, S935 }
* staged UNVERIFIABLE (5) = { S874, S890, S894, S918, S936 }

Union of all three = 26 = every staged id the slice reaches; no staged id is unassigned.

Subject lines of the staged REFUSED rows (from `SOURCES.append.md`), for the record:

| staged | document |
|---|---|
| S862 | 国立天文台 ニュース「令和9（2027）年暦要項の発表」(2026-02-02) — nao.ac.jp |
| S869 | Milburn/Fink/Peterson, "Conlanging 101", 26C3 (2009) |
| S870 | 三九音域「世界观是打开小说幻想屋的钥匙」, 中国作家网 (2023-09-22) |
| S875 / S933 | 包寒吴霜、蔡华俭 (2021)《姓名对个体心理与行为的实际影响》, 心理科学进展 29(6) (live CN page / archive capture companion) |
| S897 | 魏斌〈單名與雙名：漢晉南方人名的變遷及其意義〉, 中国社科院历史研究所 (2021-03-16) |
| S899 | 爱潜水的乌贼「我先设定世界观，再考虑怎么升级」, 中国作家网 (2025-06-10) |
| S900 | 爱潜水的乌贼：网络文学不断"升级"的"奥术", 中国作家网 (2022-12-07) |

### Mapping verified by URL (the assignment's "verify two of the mappings yourself by URL")

I verified **seven** of the 21 by live fetch, i.e. fetched the register URL and confirmed the
staged row that the map names is the row for that URL. Two are called out as the requested
spot-checks, the other five as corroboration:

**Spot-check A — S787 → S870.** Register URL
`https://www.chinawriter.com.cn/n1/2023/0922/c404024-40083104.html`. Fetched HTTP 200, 45238 B,
title `我是怎样创作网络小说的--网络文学--中国作家网`. The merge package row **S870** is
`三九音域「世界观是打开小说幻想屋的钥匙」, in《我是怎样创作网络小说的——网络文学名家六人谈》, 中国作家网（中国作家协会主办）, 2023-09-22` — the same article at the same URL. The register's
quoted span `作品中的人物名字和地名也一样…` is absent from the served bytes (0 hits for
`作品中的人物名字和地名`), which is why S787/S870 is REFUSED, not PRESENT. Mapping confirmed
*and* the verdict independently confirmed.

**Spot-check B — S816 → S899.** Register URL
`https://www.chinawriter.com.cn/n1/2025/0605/c404024-40494534.html`. Fetched HTTP 200, 48536 B,
title `爱潜水的乌贼："我先设定世界观，再考虑怎么升级"--网络文学--中国作家网`. Merge package row
**S899** is exactly that interview, same URL. My fetch is **sha256-byte-identical** to the
committed round-71 capture `.ufo/waves/round-71/assimilation/fetches/s816.html`, so the page
has not drifted since the round-71 hand-check. The register's quoted span
`这个我肯定考虑过。我自己就是资深读者…` → 0 hits (`考虑过`, `资深`, `容忍度`, `我自己就是` all
0). REFUSED confirmed. Mapping confirmed.

Corroborating spot-checks (same method): S779→S862 (NAOJ 暦要項 page, title matches the S862
row), S786→S869 (the fetched `26c3.pdf`/`cl101.pdf` is the "Conlanging 101" paper the S869 row
names), S814→S897 (fetched CSSN page title `魏斌:單名與雙名…` matches the S897 row),
S817→S900 (fetched title `爱潜水的乌贼：网络文学不断"升级"的"奥术"` matches the S900 row),
S804→S886 (fetched Kotobank 苗字 page, span located).

**Confidence: high** on the REFUSED/PRESENT/UNVERIFIABLE partition and on the URL join; the
one soft spot is S792 (§5), which does not change the *set membership* of anything but does
qualify one filed note.

## 4. Staged S863 / S867 / S967 (the adoption citations) are NOT in the register slice — CONFIRMED

Three independent checks, all negative:

1. **Not staged images of the slice.** The 26 staged ids the slice reaches are listed in §2/§3.
   `S863 ∉ {…}`, `S867 ∉ {…}`, `S967 ∉ {…}`. A staged id is in the slice iff some register row
   in the slice maps to it; none does.
2. **Not register rows.** The register's kotodama slice ids are exactly
   `{S776, S778, S779, S786, S787, S791, S792, S795, S796, S804, S814, S816, S817, S820, S823,
   S824, S825, S827, S807`, S812`, S835`}`. Neither `S863`, `S867` nor `S967` appears as a
   register id — not in the kotodama lane's rows and not in **any** lane's rows of
   `absent-defect-register.md`.
3. **Not by document.** The three adoption citations' documents are
   `https://www.ihchina.cn/project.html` (S863), `https://online.bunka.go.jp/db/heritages/search`
   (S867) and the 2020-02-16 Internet Archive capture of the former (S967). No register row in
   the slice cites `ihchina` or `bunka.go.jp` — `grep` over the 21 slice URLs: 0 hits for
   `ihchina`, 0 hits for `bunka.go.jp`. Consistent with the claim-C "before" state
   (`grep -c 'ihchina' = 0`, `'bunka.go.jp' = 0` over the 797-row registry).

Corroborating: the live lane registry `corpus/SOURCES.md` (797 rows) holds **0** rows mentioning
`ihchina.cn` or `bunka.go.jp`, so the adoption surface is genuinely uncovered ground.

### Namespace hazard the caller must not miss

`S863` and `S867` **do** exist as ids in the live kotodama-shokunin registry
(`corpus/SOURCES.md:818` and `:822`) — but they are *different documents*:

* live registry `S863` = UNESCO ICH "Chhau dance" (element 00337)
* live registry `S867` = UNESCO ICH "Kabuki theatre" (element 00163)

while the **staged** `S863`/`S867` in `SOURCES.append.md` are the ihchina.cn 国家级名录 page
and the bunka.go.jp 文化財検索 database respectively. `S967` exists only in the staged space
(absent from the live registry, whose max is S873). The claim-C leg "REPOINTED" already
anticipates this ("staged S863/S867/S967 re-pointed by document; no arithmetic"), and the
round-71 id-renumber map (`.ufo/waves/round-71/assimilation/id-renumber-map.json`) confirms the
arithmetic map would have sent them elsewhere entirely (S863→S878, S867→S882, S967→S982).
`S863`/`S867`/`S967` must be read as **staged** ids only. The claim-C counter's `COLLCHECK`
leg ("S874/S875 not in reg-ids") is satisfied: neither `S874` nor `S875` appears in the
round-71 `reg-ids` list (784 ids, max S860) nor in the live 797-row registry (max S873).

Also note the pre-existing collision shape the round-71 verdicts file itself flags (`:37`):
`S859`/`S860` are recorded as id collisions at `.ufo/waves/round-71/assimilation/collisions`.
Two of the staged REFUSED ids (`S862`, `S869`, `S870`) also happen to exist as *live lane
registry* rows for unrelated documents (Mevlevi Sema, Benesh International, ICKL). That is
harmless for claim C, whose REJECTED entries are keyed to staged S870 and staged S899/S900 —
and I confirmed those three staged ids do carry the REFUSED verdict:
`narrative-structure-frameworks.md` cites staged S870 (line 32), and
`worldbuilding-setting-practice.amend-2026-10-23.md` cites staged S899 and S900 (lines 4–5),
all three being staged REFUSED rows.

## 5. Findings / caveats (not blockers for claim C)

**F-1 (MEDIUM) — the S792 filed note is inaccurate, though its verdict may still hold.** The
filed note (`:20`) reads "journal page is the English article; the four Chinese headings
absent". My live fetch (HTTP 200, 159831 B — byte-count identical to the round-68 hand-check's
`status` field `200 159831 text/html;charset=UTF-8` and to the shokuknow `.qcache` capture
`ad6b88b792e4afe19ace8af5.raw`, 159831 B, dated 2026-10-23) shows the page **does** contain all
four headings `实际影响取向`, `社会认知取向`, `自我信息加工取向`, `文化产品取向` — 2 hits each in
the raw HTML, and they sit in the Figures/Tables block as a four-row table
(`研究取向 | 分析层面 | 效应主体 | …`), repeated once for the CN and once for the EN rendering.
The **exact quoted span** (`实际影响取向 / 社会认知取向 / 自我信息加工取向 / 文化产品取向` joined
by ` / `) is genuinely absent — the page never renders the four as one contiguous slash-joined
string, because they are table rows separated by other cells. So:
* under the register's exact-span rule the REFUSED verdict is defensible; and
* the round-68 census (`found: null`) reached the same verdict for the same bytes, so this is
  not a round-71 drift.
But the *note's stated reason* ("the four Chinese headings absent") is factually wrong, and a
reader relying on it would believe the document does not discuss the four orientations at all.
The document plainly does. **Recommendation for whoever files the round-72 lesson:** the S792
row should be described as "the four headings are present as separate table rows; the
slash-joined quoted span does not occur" — not "the headings are absent". This changes no set
membership: S792 stays REFUSED, so staged S875 and S933 stay in the staged REFUSED set.

**F-2 (LOW) — the register id space is a third namespace, and the round-71 wave-1 cross-check
already misread it.** The register's ids are the *fleet corpus-expansion-1 census* ids
(`.ufo/waves/corpus-expansion-1/quote-lint-full-v5.json`, e.g. finding
`{"lane":"kotodama","round":"round1","id":"S776","verdict":"ABSENT"}`), **not** the live lane
registry ids and not the staged ids. Hence the round-71 note on S776 — "lane registry S776 is a
different source (Penn Museum) — register id mismatch recorded" — and the
`RevQuarantineCrossCheck.md` observation that register S778 has no row in `corpus/SOURCES.md`
(which has S776 then S779). Consequence for this wave: **do not** join the register slice to
`corpus/SOURCES.md` by id. The staged side is unambiguous (the merge package), and
`reg-to-staged.txt` joins by URL, which is the only sound join available. My §2 verification
exploited exactly this.

**F-3 (LOW) — `S778` has no row in the live lane registry.** `grep -cE '^\| S778 \|'`
`corpus/SOURCES.md` → 0. Pre-existing (flagged by round-71 `RevQuarantineCrossCheck.md`),
unchanged by round 71, and outside this wave's scope. It does not affect the verdict sets
(the verdict is about the register row's cited URL, which resolves fine) nor the staged mapping.

**F-4 (INFO) — the round-71 verdicts file's tally and label split are internally consistent.**
`:36` reads `PRESENT 10 · REFUSED 7 · UNVERIFIABLE 4 = 21`, and `:40-42` reconciles
UNVERIFIABLE = the 3 unreachable-class rows + S791 (truncated URL). My re-derivation agrees on
all three numbers. The `10/6/5` figure mentioned in the round-72 `claims.json` Ca "before"
text is the *pre*-`57e0a72` state; the committed file already carries the corrected `10/7/4`,
so Ca's before/after framing for this file is stale but the landed evidence is right.

## 6. Bottom line for the caller

* The three verdict sets are re-derived and **exactly** as specified:
  REFUSED {S779,S786,S787,S792,S814,S816,S817}, PRESENT {S776,S778,S795,S796,S804,S820,S823,
  S824,S825,S827}, UNVERIFIABLE {S791,S807,S812,S835}. 21 rows, no dups, bijection with the
  round-72 `quarantine-slice`.
* **Staged REFUSED = {S862, S869, S870, S875, S897, S899, S900, S933}** (8 staged ids from 7
  register rows).
* The adoption citations **staged S863 / S867 / S967 are NOT in the register slice** — by
  staged-image set, by register-id set, and by document URL — so no adopted entry can be
  citing a quarantine-REFUSED row through them.
* The claim-C REJECTED entries do cite staged REFUSED rows (S870; S899+S900), exactly as the
  claim's REJECTS leg states.
* No blocker for claim C. One accuracy fix recommended for the round-72 lesson text: the S792
  note (F-1).
