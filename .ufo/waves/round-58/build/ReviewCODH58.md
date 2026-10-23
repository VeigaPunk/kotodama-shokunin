# ReviewCODH58 — routed defect 1, CODH bukan not-registered reason (round-57 lesson :92)

Seat: `KotodamaR58A2.ReviewCODH58` (leaf reviewer; records, round-57 routed defect 1). Date 2026-10-23.
Instrument: `python3 -B reports/round-58/reopen-quote.py` (byte-copy of the round-57 locator — the very tool the filed reason names).

## Verdict: AGREE with the finding

The finding (spot-check §3, §5 item 1): `corpus/lessons/round-57.md:92` says the CODH bukan source is not registered because "its quotes normalise below the locator's 8-word minimum, so no row can be located". That reason is **false**. I re-opened both pages by ordinary plain curl (UA header, no challenge, no tool evasion) and re-ran the locator on the scout's four quotes; all four normalise to 10-15 words (≥8) and all four print `LOCATED` live.

Served-text check (this session, 2026-10-23):
- `https://codh.rois.ac.jp/bukan/` — direct, HTTP 200, 18,334 B text/html (byte-size equal to the scout's capture). The 381-bukan sentence is body prose in the project description ("武鑑全集 Edo+150 Projects" block), not footer/nav/boilerplate; the page carries the CC BY-SA 4.0 license lines (クリエイティブ・コモンズ 4 / ライセンス).
- `https://codh.rois.ac.jp/bukan/han/H236/` — direct, HTTP 200, 192,162 B text/html (equal to the scout's capture). The Owari H236 page is the per-domain longitudinal table (経時データ; columns 番号 / DOI / 武鑑書名 / 版元 / 出版年（和暦・西暦）/ 当主名 / 参府 / 御暇 / 居城地 / ページ); the 大成武鑑 天明2/1782 row with the crest-glyph cells （記号）「丸にエ」3 （記号）「丸にト」3 is genuine table data. Also CC BY-SA 4.0 on-page.

### Locator output (pasted, run 2026-10-23 against the live pages)

```
$ python3 -B reports/round-58/reopen-quote.py 'https://codh.rois.ac.jp/bukan/' 'CODHと国文学研究資料館が協働して公開する「日本古典籍データセット」には、2017年12月現在、 381点の『武鑑』 が含まれています。その中からまず 寛政武鑑（1789） を選んで'
LOCATED https://codh.rois.ac.jp/bukan/
$ python3 -B reports/round-58/reopen-quote.py 'https://codh.rois.ac.jp/bukan/han/H236/' '紋尽 松会 明暦4 1658 尾張右兵衛督様 なし なし 名古屋 00003 1'
LOCATED https://codh.rois.ac.jp/bukan/han/H236/
$ python3 -B reports/round-58/reopen-quote.py 'https://codh.rois.ac.jp/bukan/han/H236/' '大成武鑑 出雲寺〈江戸〉 天明2 1782 尾張大納言宗睦卿 （記号）「丸にエ」3 （記号）「丸にト」3 名古屋 00007-1'
LOCATED https://codh.rois.ac.jp/bukan/han/H236/
$ python3 -B reports/round-58/reopen-quote.py 'https://codh.rois.ac.jp/bukan/han/H236/' '寛政武鑑 須原屋 江戸 寛政1 1789 尾張大納言宗睦卿 子寅辰午申戌3月 丑卯巳未酉亥3月 名古屋 00006 1'
LOCATED https://codh.rois.ac.jp/bukan/han/H236/
```

Normalised word counts (locator's own `normalise`, NFKC + casefold + non-word split): 11 / 10 / 15 / 11 — the "4 quotes of 10-15 words" of the closure, confirmed. All are also within the 25-word cap. `MIN_WORDS = 8` was never the obstacle. (The round-58 copy of the locator behaves identically to the round-57 one it byte-copies; the spot-check §2 confirmed no diff between the revisions.)

## Exact fix (two parts; no filed bytes rewritten)

### 1. Register the source now — queued row S576

`grep -F 'codh.rois.ac.jp' corpus/SOURCES.md` → no matches, so the URL is free. No true exclusionary ground exists: ordinary direct access (both pages HTTP 200, no challenge), CC BY-SA 4.0 (criterion 10 clean), tier B dataset, quotes locate ≥8 normalised words, and the material is not carried elsewhere — the heraldry entry covers Edo commoner crests and reserved crests (S429/S432) but nothing on the bukan as a printed crest-inventory genre, and its own Owed line (`corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md:172`) still lists "Japanese-language bukan records once a locatable romanised passage exists". That Owed premise is also false as an instrument matter: the locator has no romanisation requirement, and the four quotes above locate as Japanese text with spaces. Registering S576 closes the Owed item and the defect in one move; a swapped-in replacement reason would only manufacture a second false entry.

Row (11 cells, claim-C row rules TOPIC/RELEVANCE not applied — records row; id in the records range S560-S599, outside the claim export S500-S559):

```
| S576 | ROIS-DS 人文学オープンデータ共同利用センター (CODH), 武鑑全集 (Bukan database), Edo+150 project; structured data adapted from the 日本古典籍データセット (NIJL), CC BY-SA 4.0 — https://codh.rois.ac.jp/bukan/ ; https://codh.rois.ac.jp/bukan/han/H236/ (direct, HTTP 200) | dataset | B | Edo bukan (daimyo armorials) as a printed crest-inventory genre: per-edition rows recording a domain's lord, service months, castle seat and mon glyphs | Owari H236 table, 大成武鑑 天明2/1782 row: "大成武鑑 出雲寺〈江戸〉 天明2 1782 尾張大納言宗睦卿 （記号）「丸にエ」3 （記号）「丸にト」3 名古屋 00007-1" | Edo bukan editions record a domain's crest as glyph symbols beside its lord and castle seat. | queued | 2026-10-23 | 2027-10-23 | — |
```

Gate line:

```
- S576 — https://codh.rois.ac.jp/bukan/han/H236/ — accessed 2026-10-23 — Owari H236 table, 大成武鑑 天明2/1782 row: “大成武鑑 出雲寺〈江戸〉 天明2 1782 尾張大納言宗睦卿 （記号）「丸にエ」3 （記号）「丸にト」3 名古屋 00007-1”. Grounds: Edo bukan editions record a domain's crest as glyph symbols beside its lord and castle seat. Seat: ReviewCODH58.
```

Anchor checks: 15 normalised words (8-25 ok); LOCATED above; not the root page of the site that locates it (locates on `/han/H236/`, quote absent from `/bukan/` root's own prose); not site boilerplate (table data row). If the L1 later cites S576 from an entry, the same used-by cell is updated per the append-only rules — no other cell changes.

### 2. Erratum line (draft for the L1 to append; never rewriting the filed bytes of round-57.md:92)

```
- `corpus/lessons/round-57.md:92` (CODH bukan): the not-registered reason is false. The scout's four quotes normalise to 11/10/15/11 words and each prints `LOCATED` under the locator (re-run 2026-10-23 by seat ReviewCODH58 on the live pages, both HTTP 200 at the scout's byte sizes, 18,334 B and 192,162 B); the 8-word minimum never blocked a row. Registered this round as S576 (queued, used-by `—`), which also closes the heraldry entry's Owed line about Japanese-language bukan records — the locator has no romanisation requirement.
```

QUALITY check the routed defect asks for: the reason named the locator, and the re-test used the locator (`reports/round-58/reopen-quote.py`) — output pasted above; this report is the receipt for that leg.

## Residual risk / gaps

- The two table-row anchors (Q2, Q4) and the root prose (Q1) are verified located but not offered as rows; S576 anchors only Q3. If the L1 prefers the prose anchor instead, Q1 also locates (11 words) but teaches dataset size/provenance, not crest inventory.
- Served HTML was saved at `/fast/scratch/hyaku/kotodama-r58/ReviewCODH58/` (`bukan-root.html`, `bukan-h236.html`) for re-inspection this session only.
- `git`/`jj` untouched in the lane; no files outside this report written there.

installs: none.
