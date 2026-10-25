# ScoutBunkaReopen — re-grounding of source 2 (bunka.go.jp 文化財検索)

Seat: L1Kotodama72.ScoutBunkaReopen (leaf, no dispatch). Date: 2026-10-25.
Scope: re-fetch `https://online.bunka.go.jp/db/heritages/search` live and record (a) HTTP status,
(b) the full flat option list of the 詳細検索「時代」select, (c) the「分野」tree top-level options
verbatim, (d) presence and labels of the record-level fields 材質・構造・技法 / サイズ / 所在地 / 指定区分.

No lane or fleet file was written other than this report. No tool was installed (python3 3.x with the
already-present `bs4` 4.15.0 / `lxml` 6.1.3 was used; `curl` was used for the fetch). PACMAN was not run.

## 1. HTTP status and payload identity

The lane's earlier fetch at `/tmp/bunka.html` was still present (231736 B, md5
`9849299d700a42a96770c5e56e10f489`), so it was re-fetched independently rather than reused.

```
$ curl -sS -o /tmp/ScoutBunkaReopen/bunka_recheck.html \
    -w 'HTTP_STATUS=%{http_code}\nCONTENT_TYPE=%{content_type}\nSIZE=%{size_download}\nURL_EFFECTIVE=%{url_effective}\nTIME=%{time_total}\n' \
    -L 'https://online.bunka.go.jp/db/heritages/search'
HTTP_STATUS=200
CONTENT_TYPE=text/html; charset=utf-8
SIZE=231736
URL_EFFECTIVE=https://online.bunka.go.jp/db/heritages/search
TIME=2.195287
```

| item | value |
|---|---|
| HTTP status | **200** |
| Content-Type | `text/html; charset=utf-8` |
| effective URL | `https://online.bunka.go.jp/db/heritages/search` (no redirect) |
| bytes | 231736 (both fetches, byte-identical in length) |
| page `<title>` | `文化遺産データベース` |
| md5 lane fetch `/tmp/bunka.html` | `9849299d700a42a96770c5e56e10f489` |
| md5 re-fetch `/tmp/ScoutBunkaReopen/bunka_recheck.html` | `bc9accaa9071717b12268fadd1930511` |

**The two payloads differ only in per-response anti-CSRF/nonce values.** After normalising the 9
`nonce="..."` attributes and the three 40-char `_token` hidden-input values, the two documents are
**The two documents are byte-for-byte identical** (verified by full-string comparison; the raw diff is 396 bytes, all inside
`nonce=` / `_token` values). Content is therefore stable between the lane's fetch and this re-fetch.

Result-set size as served on page 1: `全308473件中1～20件目を表示` (20 rows, page size selectable
20/50/100).

Two record detail pages were also opened (both HTTP 200) to check where the record-level fields live:

```
$ curl -sS -o detail.html -w 'HTTP=%{http_code} SIZE=%{size_download} URL=%{url_effective}\n' \
    -L 'https://online.bunka.go.jp/db/heritages/detail/663160'
HTTP=200 SIZE=19543 URL=https://online.bunka.go.jp/db/heritages/detail/663160
$ curl -sS -o detail_kokuhu.html -w 'HTTP=%{http_code} SIZE=%{size_download}\n' \
    -L 'https://online.bunka.go.jp/db/heritages/detail/65582'   # 国宝 (額田寺伽藍並条里図（麻布）)
HTTP=200 SIZE=24670
```

## 2. The「時代」select — full flat option list, verbatim

The element is a single flat `<select>` with no `<optgroup>`:

```html
<select name="era_cd[]" id="era_cd" multiple="multiple">
```

49 options, in DOM order. Every label is `<era> [<branch>]` with **one ASCII space (U+0020)**
before the bracket and **ASCII square brackets** (U+005B / U+005D) — e.g. `旧石器 [日本]` =
`U+65E7 U+77F3 U+5668 U+0020 U+005B U+65E5 U+672C U+005D`.
The three branches are contiguous blocks in this order: **日本, 中国, 朝鮮半島**.

### 「時代」— 日本 branch (18 options, DOM order)

| # | value | option text (verbatim) |
|---|---|---|
| 1 | `1` | `旧石器 [日本]` |
| 2 | `2` | `縄文 [日本]` |
| 3 | `3` | `弥生 [日本]` |
| 4 | `4` | `古墳 [日本]` |
| 5 | `5` | `飛鳥 [日本]` |
| 6 | `6` | `奈良 [日本]` |
| 7 | `7` | `平安 [日本]` |
| 8 | `8` | `鎌倉 [日本]` |
| 9 | `9` | `南北朝 [日本]` |
| 10 | `10` | `室町 [日本]` |
| 11 | `11` | `安土・桃山 [日本]` |
| 12 | `12` | `江戸 [日本]` |
| 13 | `13` | `明治 [日本]` |
| 14 | `14` | `大正 [日本]` |
| 15 | `15` | `昭和以降 [日本]` |
| 16 | `68` | `昭和 [日本]` |
| 17 | `69` | `平成 [日本]` |
| 18 | `70` | `令和 [日本]` |

### 「時代」— 中国 branch (21 options, DOM order)

| # | value | option text (verbatim) |
|---|---|---|
| 1 | `16` | `旧石器 [中国]` |
| 2 | `17` | `新石器 [中国]` |
| 3 | `18` | `夏 [中国]` |
| 4 | `19` | `殷（商） [中国]` |
| 5 | `20` | `周 [中国]` |
| 6 | `21` | `春秋時代 [中国]` |
| 7 | `22` | `戦国時代 [中国]` |
| 8 | `23` | `秦 [中国]` |
| 9 | `24` | `漢 [中国]` |
| 10 | `25` | `三国 [中国]` |
| 11 | `26` | `晋 [中国]` |
| 12 | `27` | `五胡十六国 [中国]` |
| 13 | `28` | `南北朝（六朝） [中国]` |
| 14 | `29` | `隋 [中国]` |
| 15 | `30` | `唐 [中国]` |
| 16 | `31` | `五代十国 [中国]` |
| 17 | `32` | `宋 [中国]` |
| 18 | `33` | `元 [中国]` |
| 19 | `34` | `明 [中国]` |
| 20 | `35` | `清 [中国]` |
| 21 | `36` | `近現代 [中国]` |

### 「時代」— 朝鮮半島 branch (10 options, DOM order)

| # | value | option text (verbatim) |
|---|---|---|
| 1 | `57` | `旧石器 [朝鮮半島]` |
| 2 | `58` | `新石器 [朝鮮半島]` |
| 3 | `59` | `青銅器 [朝鮮半島]` |
| 4 | `60` | `鉄器 [朝鮮半島]` |
| 5 | `61` | `高句麗・三韓 [朝鮮半島]` |
| 6 | `62` | `朝鮮三国 [朝鮮半島]` |
| 7 | `63` | `新羅 [朝鮮半島]` |
| 8 | `64` | `高麗 [朝鮮半島]` |
| 9 | `65` | `李氏朝鮮 [朝鮮半島]` |
| 10 | `66` | `近現代 [朝鮮半島]` |

The visible pop-up control (`div id="era_menu"`) carries the **same 49 labels in the same order**;
each is a `<label for="CHECKLIST-era-N">` whose text equals the corresponding `<option>` text verbatim
(49 checklist labels == 49 options). The select is the form-side mirror of that pop-up.

**The literal string `詳細検索` does not occur on the served page (0 occurrences).** The page's own
headings are `条件を入れて探す` (`<h1>` image alt, and the global nav item) and, inside the right-hand
condition panel, the `<dt>` labels are:

```
フリーワード
作品名
作家名
所蔵館名
時代
分野
地域
指定区分
```

So「時代」/「分野」/「地域」/「指定区分」are the served field names;「詳細検索」is a description used by
the registry row and the entry text, not a verbatim label on the page.

## 3. The「分野」tree — top-level options, verbatim

The element is again one flat `<select>` with **no `<optgroup>`**; the hierarchy is expressed only by
leading whitespace inside the option text:

```html
<select name="genre_cd[]" id="genre_cd" multiple="multiple"><option value="1">建造物</option><option value="2">　宗教建築</option>…
```

92 options total = 16 top-level + 76 children. Top-level = option text containing no U+3000
(ideographic space). The pop-up `div id="genre_menu"` carries the same 92 labels with the same
whitespace (92 checklist labels == 92 options), so the whitespace is part of the served label, not a
rendering artefact of the select.

### 「分野」top-level options, in DOM order (verbatim)

| # | value | option text (verbatim, whitespace shown) | stripped |
|---|---|---|---|
| 1 | `1` | `建造物` | `建造物` |
| 2 | `72` | `伝統的建造物群` | `伝統的建造物群` |
| 3 | `7` | `絵画` | `絵画` |
| 4 | `14` | `版画` | `版画` |
| 5 | `20` | ` 彫刻` | `彫刻` |
| 6 | `26` | ` 工芸` | `工芸` |
| 7 | `38` | ` 考古` | `考古` |
| 8 | `45` | ` 歴史` | `歴史` |
| 9 | `33` | ` その他の美術` | `その他の美術` |
| 10 | `84` | ` 民俗` | `民俗` |
| 11 | `49` | ` 伝統芸能` | `伝統芸能` |
| 12 | `88` | ` 工芸技術` | `工芸技術` |
| 13 | `78` | ` 文化財保存技術` | `文化財保存技術` |
| 14 | `55` | ` 史跡` | `史跡` |
| 15 | `61` | ` 名勝` | `名勝` |
| 16 | `67` | ` 天然記念物` | `天然記念物` |

So the 16 top-level 分野 categories, in served order, are:

`建造物`, `伝統的建造物群`, `絵画`, `版画`, `彫刻`, `工芸`, `考古`, `歴史`, `その他の美術`, `民俗`,
`伝統芸能`, `工芸技術`, `文化財保存技術`, `史跡`, `名勝`, `天然記念物`

**Whitespace caveat for verbatim quoting.** The 16 top-level labels are *not* uniformly prefixed:
the first four (`建造物`, `伝統的建造物群`, `絵画`, `版画`) carry **no** leading whitespace; the other
twelve carry a single **ASCII space (U+0020)** (e.g. `' 彫刻'`, `' 天然記念物'`). Their children
carry U+3000 — one ideographic space under the first four (`'　宗教建築'`), and
ASCII-space + U+3000 under the other twelve (`' 　木像'`). The visible checklist labels reproduce
the same prefixes. Any quote that strips whitespace is a normalisation, not a verbatim copy.

### 「分野」children (full list, for completeness)

| value | option text (verbatim) |
|---|---|
| `2` | `　宗教建築` |
| `3` | `　城郭建築` |
| `4` | `　住居建築` |
| `5` | `　近世以前その他` |
| `6` | `　近代その他` |
| `73` | `　武家町` |
| `74` | `　宿場町` |
| `75` | `　港町` |
| `76` | `　農・山村集落` |
| `77` | `　その他` |
| `8` | `　日本画` |
| `9` | `　油彩画` |
| `10` | `　水彩` |
| `11` | `　素描` |
| `12` | `　東洋画(日本画を除く)他` |
| `13` | `　その他` |
| `15` | `　木版画` |
| `16` | `　銅版画` |
| `17` | `　リトグラフ（石版画）` |
| `18` | `　シルクスクリーン` |
| `19` | `　その他` |
| `21` | ` 　木像` |
| `22` | ` 　金属像` |
| `23` | ` 　石像` |
| `24` | ` 　石膏像` |
| `25` | ` 　その他` |
| `27` | ` 　金工` |
| `28` | ` 　漆工` |
| `29` | ` 　染織` |
| `30` | ` 　陶磁` |
| `31` | ` 　ガラス` |
| `32` | ` 　その他` |
| `39` | ` 　石器・石製品類` |
| `40` | ` 　土器・土製品類` |
| `41` | ` 　金属製品類` |
| `42` | ` 　木簡・木製品類` |
| `43` | ` 　骨角・牙・貝製品類` |
| `44` | ` 　その他` |
| `46` | ` 　文書・書籍` |
| `47` | ` 　絵図・地図` |
| `48` | ` 　その他` |
| `34` | ` 　写真` |
| `35` | ` 　デザイン` |
| `36` | ` 　書` |
| `37` | ` 　その他` |
| `85` | ` 　有形民俗文化財` |
| `86` | ` 　無形民俗文化財` |
| `50` | ` 　能楽` |
| `51` | ` 　文楽` |
| `52` | ` 　歌舞伎` |
| `53` | ` 　音楽` |
| `54` | ` 　その他` |
| `89` | ` 　金工` |
| `90` | ` 　漆芸` |
| `91` | ` 　染織` |
| `92` | ` 　陶芸` |
| `93` | ` 　その他` |
| `79` | ` 　建造物` |
| `80` | ` 　美術工芸品` |
| `81` | ` 　伝統芸能` |
| `82` | ` 　工芸技術` |
| `83` | ` 　民俗芸能` |
| `56` | ` 　古墳` |
| `57` | ` 　社寺跡又は旧境内` |
| `58` | ` 　城跡` |
| `59` | ` 　集落跡` |
| `60` | ` 　その他` |
| `62` | ` 　庭園` |
| `63` | ` 　渓谷・渓流` |
| `64` | ` 　海浜` |
| `65` | ` 　山岳` |
| `66` | ` 　その他` |
| `68` | ` 　動物` |
| `69` | ` 　植物` |
| `70` | ` 　地質鉱物` |
| `71` | ` 　天然保護区域` |

## 4. Record-level fields 材質・構造・技法 / サイズ / 所在地 / 指定区分

These four labels occur in **two different roles** on the page, and only three of them are
record-level labels in the result rows.

| field | occurrences in `/tmp/bunka.html` | where it occurs | record-level field? |
|---|---|---|---|
| `材質・構造・技法` | 14 | `<li>材質・構造・技法：…</li>` inside each result row's `<!-- /その他詳細 -->` list | **yes** (labelled list item in the record row) |
| `サイズ` | 7 | same row list, `<li>サイズ：…</li>` | **yes** |
| `所在地` | 12 | same row list, `<li>所在地：…</li>` | **yes** |
| `指定区分` | **1** | the single occurrence is the **search-condition facet label** `<dt>指定区分</dt>` — not inside any result row | **no** — it is a filter field, not a per-record field |

Full census of labelled `<li>` fields inside the 20 result rows of page 1:

```
登録日          20
材質・構造・技法     14
所在地          12
サイズ          7
時代（年代）       6
```

Every record row's `<!-- /その他詳細 -->` block is a flat `<ul>` of `<li>` items, e.g. verbatim from
the row for `近江八景 　瀬田夕照` (id 663160):

```html
<li>
    時代（年代）：19世紀前期
</li>
<li>
    材質・構造・技法：紙本木版色摺
</li>
<li>
    サイズ：22.8×34.1
</li>
<li>
    登録日：2026/10/18
</li>
```

Note the separator is the **fullwidth colon U+FF1A (：)** and the labels are exactly
`時代（年代）` (fullwidth parens), `材質・構造・技法`, `サイズ`, `所在地`, `登録日` — the leading
`<li>` of each row also carries the `分野 / 時代 / 地域` triple (e.g. `木版画 ／ 江戸`) with no label.
Fields are per-record optional: of the 20 rows, 材質・構造・技法 appears in 14, 所在地 in 12, サイズ in 7.

### Where 指定区分 actually appears on a record

The record's designation is shown on the **detail** page as an **unlabelled** `<li class="kubun">`
in `ul.info`, never as `指定区分：`. Verified on 6 detail pages (all HTTP 200): `663160`, `65582`,
`654646`, `591314`, `591507`, `625035` — on every one of them the four labels
`材質・構造・技法` / `サイズ` / `所在地` / `指定区分` occur **0 times**.

```html
<ul class="info">
    <li class="spe"></li>
    <li>奈良時代</li>
    <li>麻布・朱墨</li>
    <li>縦113.70 cm 横72.50 cm</li>
    <li class="kubun">国宝</li>
</ul>
```

(`detail/65582` — 額田寺伽藍並条里図（麻布）, 国宝. The value rows carry no field labels at all;
`kubun` is the class that marks the designation.) The same design holds on the search page: the
classification exists only as the filter facet (`<dt>指定区分</dt>` + a 29-value checklist), and no
result row prints a `指定区分` field.

### The「指定区分」filter facet values (as served)

`id="classification_cd"`, 29 options, flat, no optgroup:

| value | option text |
|---|---|
| `1` | `国宝` |
| `2` | `重要文化財` |
| `3` | `登録有形文化財` |
| `4` | `重要無形文化財` |
| `5` | `記録作成等の措置を講ずべき無形文化財` |
| `6` | `重要有形民俗文化財` |
| `7` | `重要無形民俗文化財` |
| `8` | `記録作成等の措置を講ずべき無形の民俗文化財` |
| `9` | `史跡` |
| `10` | `名勝` |
| `11` | `天然記念物` |
| `12` | `特別史跡` |
| `13` | `特別名勝` |
| `14` | `特別天然記念物` |
| `15` | `重要伝統的建造物群保存地区` |
| `16` | `選定保存技術` |
| `17` | `未指定` |
| `18` | `有形文化財(建造物)` |
| `19` | `有形文化財(美術工芸品)` |
| `20` | `無形文化財` |
| `21` | `民俗文化財(有形民俗文化財)` |
| `22` | `民俗文化財(無形民俗文化財)` |
| `23` | `記念物(史跡)` |
| `24` | `記念物(名勝)` |
| `25` | `記念物(天然記念物)` |
| `26` | `伝統的建造物群保存地区` |
| `27` | `文化財保存技術` |
| `28` | `地方指定文化財` |
| `29` | `重要文化的景観` |

## 5. Grep census (both fetches byte-identical in these counts)

Both `/tmp/bunka.html` and the independent re-fetch give the same numbers, so the registry row's
recheck command `curl -fsSL 'https://online.bunka.go.jp/db/heritages/search' | grep -c '安土・桃山'`
still returns **3**.

| pattern | `grep -c` (lines) | occurrences |
|---|---|---|
| `安土・桃山` | 3 | 3 |
| `材質・構造・技法` | 14 | 14 |
| `サイズ` | 7 | 7 |
| `所在地` | 12 | 12 |
| `指定区分` | 1 | 1 |
| `時代` | 12 | 14 |
| `分野` | 1 | 1 |
| `朝鮮半島` | 15 | 33 |
| `絵画` | 3 | 3 |
| `版画` | 7 | 13 |
| `彫刻` | 3 | 3 |
| `工芸` | 9 | 15 |

(The gap between `grep -c` and occurrence count for `時代`, `朝鮮半島`, `版画`, `工芸` is because those
strings also live inside the long single-line `id_list_*` JavaScript arrays.)

## 6. Findings for the round-72 adoption (claim C, row S875)

1. **The source is live and stable.** HTTP 200; the lane's fetch and this re-fetch differ only in
   CSRF token/nonce, so the recorded option lists are reproducible today.
2. **「時代」= 49 flat options**, three contiguous branch blocks: 日本 (18, values 1–15 + 68–70),
   中国 (21, values 16–36), 朝鮮半島 (10, values 57–66). The 中国 branch ends at `近現代 [中国]`
   (value 36); `清 [中国]` (value 35) is present.
3. **「分野」= 92 flat options, 16 top-level**, as listed above. Any quoted 「分野」 enumeration must
   either keep the served leading whitespace or declare that it is stripped.
4. **Correction to the entry's `topic` line.** It names four *record-level* fields —
   `材質・構造・技法 / サイズ / 所在地 / 指定区分`. Three are record-level labels in the search result
   rows; **`指定区分` is not** — it is the search-condition facet label, and the record-level
   designation is an unlabelled `li.kubun` on the detail page. If the entry keeps the four-field
   enumeration it should say 「検索フォームのフィールド名（指定区分はフィルタ枠の名称）」rather than
   claiming four record-level fields, or drop 指定区分 from that list.
5. **Correction to the wording 「詳細検索」.** The string does not occur on the page; the panel is
   `条件を入れて探す` and the field names are `時代 / 分野 / 地域 / 指定区分`. The registry row's
   excerpt `詳細検索フォーム「時代」選択肢` is a description of the form, not a verbatim page string.
6. **S875's own recheck (`grep -c '安土・桃山'` → 3) holds** against the live page as of 2026-10-25.

## 7. Remaining unknowns

- Whether the site ever emits `<optgroup>` for 時代/分野 (two independent fetches say no; the
  checklist pop-up is the only hierarchical rendering).
- The served facet stops at 29 options (`28` = `地方指定文化財`, `29` = `重要文化的景観`); whether
  further values exist behind pagination in the facet pop-up was not checked. The facet value list
  and the `kubun` values printed on records are not 1:1 — `国宝` is facet value 1, but a record's
  `li.kubun` prints the bare name.
- Not verified: whether `https://online.bunka.go.jp/db/heritages/search` is rate-limited for the
  lane host (two fetches 2.2 s apart both returned 200; no throttling observed).

