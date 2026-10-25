# ScribeEntryBase — round 74 wave 1 — base entry draft for claim C

Seat: ScribeEntryBase (leaf, no dispatch). Date: 2026-10-25. Item: draft the base entry
`corpus/knowledge/culture-material/worldbuilding-setting-practice.md` from the staged
`/home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge/culture-material/worldbuilding-setting-practice.md`,
to the lane bar (`corpus/QUALITY.md` criteria 1–24) and the lane entry format, citing only the
tentative lane ids S877 (existing row), S881 (litmemo) and S882 (tuduku).

Artifact written (the only draft path this seat touched):
`/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-74/drafts/worldbuilding-setting-practice.md`
— 265 lines, 4,194 words, 27,262 bytes, sha256
`658a8fa477a9502e255a83debc9989c24e50b4028d226ecf0e35b03e9986b00b`. Ten sections (§1 calibration
key, §2 the scholarly frame, §3 what a setting is / how much, §4 build order, §5 four-layer chain,
§6 five elements and the note, §7 two sub-sheets, §8 depth / genre / failures, §9 single-source
discipline, §10 coupling and handoff), 15 decision or typology tables, 85 table rows, no table row
carrying an id, one S-id on every cited line.

Scratch: `/tmp/ScribeEntryBase/` (`litmemo_com_ja_blog_novel-worldbuilding-guide.html`,
`tuduku_space_column_novel-worldbuilding.html`, `conlangs.pdf`, `sidorova.txt` (pdftotext),
plus the tag-stripped `.txt` derivations).

## 1. Fetches — commands, raw outputs, User-Agent

One browser-shaped User-Agent was used for every live fetch and CDX probe, verbatim:

`Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`

```
$ cd /tmp/ScribeEntryBase
$ UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
$ curl -sS -L -A "$UA" -o litmemo_com_ja_blog_novel-worldbuilding-guide.html -w '%{http_code}' \
    https://litmemo.com/ja/blog/novel-worldbuilding-guide
200        # 101,615 bytes on disk
$ curl -sS -L -A "$UA" -o tuduku_space_column_novel-worldbuilding.html -w '%{http_code}' \
    https://tuduku.space/column/novel-worldbuilding
200        # 17,068 bytes on disk
$ curl -sS -L -A "$UA" -o conlangs.pdf -w '%{http_code}' \
    http://www.philol.msu.ru/~sidorova/files/conlangs.pdf
200        # 1,055,723 bytes on disk
$ sha256sum litmemo_com_ja_blog_novel-worldbuilding-guide.html tuduku_space_column_novel-worldbuilding.html conlangs.pdf
441fc921cadc744a7d59f91a055ff2eec1359d24f5c331d783104a1fa334ca64  litmemo…html
754f504c34d796f40e86fb0d98c98946e36284c5fae511d7837f442662cfc1b7  tuduku…html
e512a20dd3eef97ed403bd4191545dea1147279d82b7cced32aaa6037ca595a9  conlangs.pdf
$ pdftotext -enc UTF-8 conlangs.pdf sidorova.txt && wc -l sidorova.txt
11434 sidorova.txt
```

No wall, no challenge, no redirect off the cited URL on any of the three — re-run with `-w`:
`HTTP 200 -> https://litmemo.com/ja/blog/novel-worldbuilding-guide bytes=101615`;
`HTTP 200 -> https://tuduku.space/column/novel-worldbuilding bytes=17068`;
`HTTP 200 -> http://www.philol.msu.ru/~sidorova/files/conlangs.pdf bytes=1055723 type=application/pdf`.
The two page hashes equal
the hashes the wave-1 scouts recorded independently (`ScoutLitmemo` 441fc92…, `ScoutTuduku`
754f504…), so this seat's bytes are the same bytes two other seats opened. The PDF's byte count
equals the lane's S877 row (1,055,723 B).

Wayback CDX (QUALITY 21/24, positive control included), same UA:

```
GET https://web.archive.org/cdx/search/cdx?url=https://litmemo.com/ja/blog/novel-worldbuilding-guide&output=txt&limit=5
  -> HTTP=200 B=0                      (empty body)
GET …?url=https://tuduku.space/column/novel-worldbuilding&output=txt&limit=5
  -> HTTP=200 B=0                      (empty body)
GET …?url=example.com&output=txt&limit=5   [positive control]
  -> HTTP=200 B=226, five rows (20020120142510 200 http://example.com:80/ …)
GET …?url=litmemo.com/ja/blog/*&output=txt&limit=5   [prefix probe]
  -> curl: (28) Operation timed out after 30000 ms, 0 bytes received   (contributes nothing)
GET …?url=tuduku.space&output=txt&limit=5            [host probe]
  -> HTTP=200 B=0
```

Ruling carried into the entry's source lines: no archived capture of either slug on 2026-10-25, with
the control returning rows so the empty answers are answers. The litmemo prefix probe timed out and
is reported as a timeout, not as absence; the exact-slug probe is the one the entry's claim rests on.

## 2. Locator map — what each quoted sentence rests on

S877 — Сидорова & Шувалова 2006, printed page numbers (the PDF's own printed markers, re-found in the
flattened `pdftotext` text; `wc -w` tokens / `wc -m` chars, `grep -c -F` = 1 after flattening
line breaks):

| # | Quote | Location | tokens / chars |
|---|---|---|---|
| 1 | «Язык – главный инструмент построения вымышленных миров, дающий названия для их природных и социальных реалий» | ch. 1, p. 7 | 15 / 108 |
| 2 | «для создания атмосферы вымышленного мира, не используются в реальной коммуникации» | classification list, item 2.3, p. 16 | 10 / 81 |
| 3 | «связь между лингвоконструированием и моделированием миров неразрывна» | ch. 2 opening, p. 35 | 7 / 68 |
| 4 | «некое научное или не совсем научное допущение» | §Фантастическая литература и вымышленные языки, p. 36 | 7 / 45 |

S881 — litmemo.com/ja/blog/novel-worldbuilding-guide (all spans contiguous in the *visible* text:
`<script>`/`<style>` stripped first, so a hit cannot be a JSON-LD or alt-attribute hit):

| # | Quote | Location | tokens / chars |
|---|---|---|---|
| 1 | 「世界観の作り方は、①物語の核になるルールを決める ②主人公の生活圏から作る ③自然→社会→文化→個人の順に因果をつなぐ ④物語で使う分だけ掘り下げる ⑤一か所にまとめて書きながら更新する、の5ステップです。」 | lead paragraph before h2「世界観とは」 | 5 / 103 |
| 2 | 「物語が起きる世界の決まりごとの総体です」 | h2「世界観とは：物語の舞台とルールのまとめ」 | 1 / 19 |
| 3 | 「決めておくのは、展開に直接かかわる核の設定だけで十分です。」 | FAQ「書き始める前に世界観をすべて決めておくべきですか？」 | 1 / 29 |
| 4 | 「自然環境が社会の仕組みを決め、社会の仕組みが文化を生み、文化が登場人物の価値観を作る。」 | h3「3. 外側の層へ因果をつなぐ」 | 1 / 43 |
| 5 | 「外側の層が内側の層を決める」 | h2「世界観の4つの層」 | 1 / 13 |
| 6 | 「約束を破る者」 | same section, the sea/trade example | 1 / 6 |
| 7 | 「読者は登場人物の目を通して世界を見ます。」 | h3「第4層：個人の経験」 | 1 / 20 |
| 8 | 「決めた設定は一つの場所に集め、本文を書くたびに参照します。本文で設定を変えたら、その場で設定資料も書き換えます。」 | h3「5. 一か所にまとめ、書きながら更新する」 | 1 / 56 |
| 9 | 「全員が同じ設定資料を一つだけ使い、それを正本にします。」 | FAQ「合作やTRPGなど、複数人で世界観を作るときはどう管理しますか？」 | 1 / 27 |

Headings cited (not counted as quotations): 「世界観の作り方：5つのステップ」, 「世界観の4つの層」,
「5. 一か所にまとめ、書きながら更新する」 — all present verbatim.

S882 — tuduku.space/column/novel-worldbuilding:

| # | Quote | Location | tokens / chars |
|---|---|---|---|
| 1 | 「勢力図・人間関係の構造：誰が権力を持ち、何が対立の軸になっているか」 | list item 5 of the「世界観設定の5要素」box | 1 / 33 |
| 2 | 「特に重要なのは魔法・技術システムの「制約」です。」 | paragraph after that box | 1 / 24 |
| 3 | 「魔法・技術システム：何ができて何ができないか。ルール（制約）が重要」 | list item 3 of the same box | 1 / 33 |
| 4 | 「世界地図・地名一覧：手書きでよいので地図を描いておく」 | list item 1 of the「設定ノートの構成例」box | 1 / 26 |
| 5 | 「世界観設定は「作者が知っていること」と「読者に伝えること」を分けて考えましょう。」 | the KEY POINT box | 1 / 40 |

Every quote is ≤25 whitespace tokens; the two Japanese lines that run to two sentences are 56 and 103
characters and carry one/two sentence boundaries, not multi-sentence digests. Nesting: S882's item 5
and key-point quotes are inside a box whose own label is 「世界観設定の5要素」/「設定ノートの構成例」;
both labels are named on the entry's source line, which is where a re-opener starts.

## 3. Quote verification actually run

A script stripped `<script>/<style>/<noscript>`, removed tags, unescaped entities, removed all
whitespace, and attributed each draft span to exactly one source text (`L` = litmemo, `T` = tuduku,
`PDF` = flattened `pdftotext`). Final run over the final draft bytes: 26 spans, attributed
**L 12 / T 9 / PDF 4**, 25 of 26 resolving to exactly one source, max 15 whitespace tokens. The one
unresolved entry is the nested term 「制約」 inside two quoted spans (it occurs 2× in L and 3× in T and
is never used as an independent citation). Two spans that occur more than once on a page were not
quoted (「設定資料集」 occurs 10 times; 「決まりごとの総体」 twice).

One sentence was deliberately checked in the raw HTML rather than in the stripped text, because
`<strong>` tags sit inside it: the five-step sentence exists verbatim with its spaces
(`…ルールを決める ②主人公の生活圏から作る…`) as a single `<p>` text node.

## 4. Gates exercised (only what was run, on the draft — not on a landed entry)

```
$ python3 -B tools/check-cited-lines.py .ufo/waves/round-74/drafts/worldbuilding-setting-practice.md
CITED-LINES: 0 finding(s) in 1 file(s)      # exit 0
$ python3 -B tools/check-draft-ids.py .ufo/waves/round-74/drafts/worldbuilding-setting-practice.md
DRAFT_IDS: 0 findings                        # exit 0
$ wc -l -w -m .ufo/waves/round-74/drafts/worldbuilding-setting-practice.md
265 4194 25367
$ grep -o 'S[0-9]\{3\}' <draft> | sort | uniq -c
      6 S877
     31 S881
      9 S882
```

Base checks re-derived from the base commit (not from the worktree), all at
`f7104cbce186bc2e1522abf0cfd619cc834628bb`:

```
$ git ls-tree -r --name-only <base> corpus/knowledge | grep -ciE 'worldbuilding|setting-practice'
0
$ git grep -lE '設定ノート|世界観|世界观' <base> -- corpus/knowledge | wc -l
0
$ git show <base>:corpus/SOURCES.md | grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
804
$ git show <base>:corpus/SOURCES.md | grep -cE 'litmemo|tuduku|chinawriter'
0
$ git show <base>:corpus/SOURCES.md | grep -oE '^\s*\|\s*S[0-9]{3,}' | tail -1
| S880
```

Corpus-size floor for the claim's ENTRIES leg (smallest knowledge entry at base, measured over all
247 files with `git show`): **478 words**
(`culture-material/heritage-taxonomy-models.amend-2026-10-24-r13.md`). The draft is 4,194 words.

Couple-path existence, checked file by file at base:

```
OK synthesis/coupling-model.md
OK linguistics/naming-systems.md
OK synthesis/worldbible-integration-contract.md
OK synthesis/consistency-verification-checklist.md
OK culture-material/cartography-and-mapmaking.md
OK synthesis/glossary-registry-format.md
OK culture-material/architecture-settlement-lexicon.md
OK linguistics/conlang-scholarship.md
MISSING myth-symbol/narrative-structure-frameworks.md
```

Six of the first eight are the paths named in the entry's `- couples:` line. The missing one is a
finding (§5 F6), not a path this seat used.

Not run (so not claimed): the round's accept-c counter, any landing, any registry row, the Gate
records, the evidence windows, the census, and any second-reader provenance pass.

## 5. Findings — staged text against the pages as served

F1. **"six tables" is wrong; the page lists five.** The staged entry's §4 heading reads "The five
elements and the six tables", and the staged S884 `teaches` cell says "the six tables a settings
note should hold". The「設定ノートの構成例」box on the page lists five items (世界地図・地名一覧 /
年表・歴史 / 魔法・能力一覧 / 人物一覧 / 社会制度・用語集). The draft says five everywhere and its
§6 table has five rows. Re-verified: five `<li>` items, raw lines 201–205.

F2. **Two staged locators name strings that are not on the page.** "世界観の作り方 4層の節" matches
no heading — the real ones are 「世界観の作り方：5つのステップ」 and 「世界観の4つの層」; and the
tuduku section names are *box labels* under h2s (「世界観設定の5要素」 sits under h2
「世界観設定に必要な5つの要素」; 「設定ノートの構成例」 under h2 「設定ノートの作り方｜管理と整理の
実践法」). The draft's source lines name the real h2s and box labels.

F3. **The staged `ground:` cites a file that exists in neither tree.** "round 1's CANNOT-ANSWER §5" —
`git ls-tree -r --name-only <base> | grep -ci CANNOT-ANSWER` = 0 in the lane, and
`find merge/kotodama -iname '*CANNOT*'` = 0 in the staged package. Replaced with the executed base
checks quoted in §4.

F4. **The staged `ground:` also cites two campaign ids that name unrelated lane documents.** "the
practitioner mandate had been met in Chinese only (S729, S730)". In this lane S729 is Neer et al. on
infant-directed speech and S730 is Genesee & Nicoladis on bilingual first-language acquisition
(`corpus/SOURCES.md:684-685`). Carrying them into the entry would reproduce the claim's own kill rule
("an id naming an unrelated lane document"). The sentence is cut; the Chinese-language register
belongs to the companion amendment.

F5. **The staged `recheck:` cites an absent campaign file.** "the three row recheck commands in round
2's `SOURCES-PROPOSED.md` (S882 -> 2, S883 -> 4, S884 -> 1)" —
`git ls-tree -r --name-only <base> | grep -ci SOURCES-PROPOSED` = 0, and the "-> n" cells are
campaign-internal counters. Replaced by a self-contained re-locate instruction.

F6. **One staged couple path does not exist at base, and one existing lane entry has the same
defect.** `myth-symbol/narrative-structure-frameworks.md` is absent from `corpus/knowledge` at base
(`git ls-tree … | grep -ci narrative-structure` = 0). It is cut from this entry's `couples:` line and
replaced by six paths that exist. Note for the calibration wave, not repaired here:
`corpus/knowledge/linguistics/conlang-scholarship.md`'s `- couples:` line also names
`myth-symbol/narrative-structure-frameworks.md` — a pre-existing dangling path in a landed entry
(round 73's base entry), outside this seat's write surface.

F7. **The staged `sources:` sentence overstates the monograph.** "S882, a tier-B row, states the
scholarly framing that the practitioner guides elaborate." What the book states is narrower: a
fictional language is the naming instrument of a fictional world (p. 7), its function is atmosphere
rather than communication (p. 16), language construction and world modelling are inseparable in
either direction (p. 35), and a science-fiction world is built around a premise (p. 36). It does not
elaborate a five-step order, four layers or five elements — no page of it mentions such a scheme in
the parts opened. The draft's §1 states the split and §2 quotes only what is there.

F8. **The staged §3 line conflates the two schemes.** "物語の核になるルール → 生活圏 → 自然環境 →
社会の仕組み → 文化 → 個人の経験" runs the page's *steps* 1–2 into its *layers*. The page's order has
five steps (step 3 is the causal link, steps 4–5 are depth and recording) and the chain is its own
four-layer block. The draft keeps them apart (§4 order, §5 chain) and gives the two orders a
side-by-side table.

F9. **Staged labels abbreviate the page's list items.** 勢力図 / 年表 / 能力一覧 / 制度・用語集 are
substrings of 勢力図・人間関係の構造 / 年表・歴史 / 魔法・能力一覧 / 社会制度・用語集. Fine as
paraphrase, wrong inside quotation marks. The draft uses the full labels and quotes item 5 and item 1
in full.

F10. **The staged S883 anchor points at a different article.** "設定資料集 を本文とズレさせない3ステップ
節" occurs only as the title of a related-post card (2 occurrences), not as a section of this page;
the phrase 信頼できる唯一の情報源 occurs once, inside that card's blurb. Consequence for the draft:
the single-source claims rest on step 5, the FAQ answer and the「設定同士が食い違う」failure, and the
"one document per series" reading is marked `(to-verify)` in §9 because it is the linked article's
promise, not this page's own body. The staged S883 anchor cell should be re-anchored before landing
(the wave-1 scout reached the same conclusion independently).

F11. **S877's scope cell does not name the framing this entry quotes.** The row scopes "the book's
own framing: the classification … the vocabulary separating вымышленные языки …". The quotes used
here extend it to the world-modelling framing (pp. 7, 35–36) and the fictional-class function
definition (p. 16). I cite the row as it stands and do not edit it; the freeze should either widen
the `scope` cell or accept the quotes as inside "the book's own framing". The row's `used-by` cell
must become `corpus/knowledge/linguistics/conlang-scholarship.md; corpus/knowledge/culture-material/worldbuilding-setting-practice.md`
(old→new logged) — currently it names only `conlang-scholarship.md`
(`sed -n '832p' corpus/SOURCES.md | awk -F'|' '{print $12}'` prints
` corpus/knowledge/linguistics/conlang-scholarship.md `).

F12. **The litmemo page's own `dateModified` is the day of the staged fetch.** The served JSON-LD
reports 2026-10-23T11:50:12Z (scout reading; I did not re-read JSON-LD), so the staged anchors may
describe a pre-rewrite version of the page [INFERENCE]. It changes nothing in the draft: the entry's
quotes are from today's bytes, whose sha256 is recorded in the source line.

F13. **The staged "tier C as method evidence" line survives the check.** Both pages are tier C for
good reason (vendor blog; editorial-service column, no byline, 約1,100文字 by its own count), and
the draft never lets a tier-C page carry a claim about a world alone: the two world-level claims it
does make are the monograph's.

## 6. Every staged sentence cut, kept or rewritten

| Staged text (verbatim, truncated) | Disposition | Why |
|---|---|---|
| `source: S882 — …conlangs.pdf — аннотация — fetched 2026-10-23` | rewritten as S877, fetched 2026-10-25, locator widened to pp. 2, 7, 16, 35–36 | id re-pointed by document; the fetched artefact is the whole book, not the аннотация |
| `source: S883 — …litmemo… — 世界観の作り方 4層の節 — fetched 2026-10-23` | rewritten as S881, accurate headings named, fetched 2026-10-25, sha256 recorded | heading string in the staged line matches nothing (F2) |
| `source: S884 — …tuduku… — 世界観設定の5要素・設定ノートの構成例 — fetched 2026-10-23` | rewritten as S882, box labels named under their h2s, fetched 2026-10-25 | labels are boxes, not headings; fetch date re-stamped |
| `verified-at: 2026-10-23` | → `2026-10-25` | this seat re-opened all three |
| `recheck: 180d — re-run the three row recheck commands in round 2's SOURCES-PROPOSED.md (S882 -> 2, S883 -> 4, S884 -> 1) (ran 2026-10-23)` | cut, replaced by a self-contained re-locate instruction | absent file, campaign counters (F5) |
| `ground: round 1's CANNOT-ANSWER §5 — the practitioner mandate had been met in Chinese only (S729, S730), with no Japanese-language practitioner source; round 2 supplies the Japanese counterpart and pairs it with a tier-B scholarly row.` | cut, replaced by executed base checks | absent file; unrelated ids (F3, F4) |
| `Round 1's S729 and S730 carried the Chinese practitioner vocabulary (世界观 as rule-system; the two-or-three-character naming heuristic) with no Japanese counterpart and no scholarly pairing.` | cut | unrelated lane documents; the Chinese material is the companion amendment's |
| `topic: …a five-step build order, the four-layer causal chain … the five elements … the settings-note tables … and the single-source discipline…` | kept, tightened to name the two sub-sheets and the note's five sections and four fields | structure named so each header field is checkable |
| `gap filled: the lane's synthesis/ partition couples domains but records no method for *authoring* a setting.` | kept in substance, with the base checks behind it | true at base (804 rows, 0 files, 0 CJK terms) |
| `sources: the three rows above. S883 and S884 are tier C and are never the sole support: S882, a tier-B row, states the scholarly framing that the practitioner guides elaborate.` | kept with ids re-pointed and the claim narrowed | the monograph does not elaborate the method (F7) |
| `couples: synthesis/coupling-model.md …; linguistics/naming-systems.md …; myth-symbol/narrative-structure-frameworks.md` | first two kept, third cut, four existing paths added | path absent at base (F6) |
| `scope: a reference method for the culture-material partition. It records how practitioners specify and maintain a setting; it decides no culture's canon.` | kept and extended | unchanged in substance; canon line kept |
| `### Proposed body` + numbered outline + trailing `---` | cut | draft scaffolding, not entry content |
| outline §2 "Worldview as rule-set — … linguistic construction as modelling of other realities, and what a constructed world is assumed to be" | rewritten as §2 around four located quotes | the phrase is the аннотация's; the served pages give p. 7 / 16 / 35 / 36 statements instead |
| outline §3 "The build order and the four layers — … with the causal chain written explicitly" | split into §4 and §5 | one section holding both became an essay and failed criterion 4 |
| outline §4 "The five elements and the six tables — … the settings note that holds 世界地図・地名一覧, 年表, 能力一覧, 人物一覧, 制度・用語集" | rewritten as §6, five sections, full labels | "six" is false; abbreviations are not the page's labels (F1, F9) |
| outline §5 "Single-source discipline — one authoritative 設定資料集 per series; what happens when a setting changes mid-draft" | rewritten as §9; "per series" marked `(to-verify)` | that wording is another article's (F10) |
| outline §6 "Coupling to the world bible — the handoff to lore-shokunin and what stays on this side" | kept as §10, expanded with the contract path and the split of duties | criterion 5 wants the handoff named |

Additions not in the staged outline, all from the same opened pages and no new source: §3's distance
table (架空世界の作り込み度合), §7's country sheet (架空の国の作り方, eight fields) and magic sheet
(魔法の設定で決めること, seven questions, plus the hard/soft scale marked `(to-verify)`), §8's depth
table (核/背景/彩り), genre table and the two failure lists with a repair column.

Two placeholders remain, both intentional and marked: the hard/soft magic attribution `(to-verify)`,
and the per-series single-source reading `(to-verify)`. No TODO, TBD or FIXME anywhere
(`grep -nE 'TODO|TBD|XXX|FIXME'` = no match).

## 7. Out of scope / handoffs

- Registry rows S881–S884, the by-document map, `reports/round-74/*`, `claims.json`, the Gate section
  of `corpus/lessons/round-74.md`, the evidence windows and the companion amendment
  (`worldbuilding-setting-practice.amend-2026-10-23.md`) belong to other seats. This seat wrote the
  base entry only and read the S877 row without editing it.
- F11 is a freeze question (S877 scope and `used-by`), not a scribe decision.
- F6's dangling couple in `conlang-scholarship.md` is a landed-entry defect for the calibration wave
  (claim Ca or a successor); this seat did not touch it.
- The entry's ids are the pre-data tentative map (S881 litmemo, S882 tuduku, S877 the monograph). If
  the freeze renumbers, every `source:` line and inline id must be re-pointed by document — the
  draft's quotes and locators are document-anchored, so re-pointing is mechanical.
- Landing the draft at `corpus/knowledge/culture-material/worldbuilding-setting-practice.md`, the
  README/index row and the accept-c legs are the executor's steps.

## 8. Tooling

Nothing installed. `pdftotext` (Poppler) was already on the host and was used read-only. No pacman, no
uv/npx/cargo, no git writes, no writes outside the draft path, this report and
`/tmp/ScribeEntryBase/`.

## Post-wave update — L1 residuals applied (round 74, post-wave)

Mandate: `KotodamaR74` L1 follow-up — the three residuals in `RevEntryQuality.md` §6. The draft was
updated in place; it is now 267 lines, 4,317 words, 26,097 bytes, sha256
`465051db89ef9e77b9e24e0ec4f95d50610c72596b071d13505fcdaaba0e65fc`. Only the draft and this report
were written; no registry row, no Gate record, no evidence file, no landing.

### 1. QUALITY 2 vocabulary (residual 1) — done

The §1 Status column now uses the three-term vocabulary in every row, and a mapping line sits directly
under the table:

> Status vocabulary, in QUALITY 2's terms: **not mainstream — unmeasured practitioner convention;
> nothing here is contested or discredited**.

| Row | Old status cell | New status cell |
|---|---|---|
| LitMemo five-step order | practitioner convention, unmeasured | not mainstream — an unmeasured vendor-blog convention |
| tuduku five elements and settings note | practitioner convention, unmeasured | not mainstream — an unmeasured editorial-service convention |
| four-layer chain | practitioner convention stated causally, unmeasured | not mainstream — one page's causal assertion, unmeasured |
| Sidorova & Shuvalova's framing | descriptive scholarship, single monograph, one school | not mainstream — a single monograph, one school; neither contested nor discredited here |
| hard magic / soft magic split | reported second-hand on the LitMemo page, (to-verify) | not mainstream as reported; second-hand and uncited, (to-verify) |

`grep -c -E 'mainstream|contested|discredited' <draft>` → **6**.

### 2. Per-series reading (residual 2) — done

Old sentence: "The per-series reading — one authoritative document for a whole series — is the linked
article's promise, not this page's own body; only one document for the shared project is stated here
(to-verify) (S881)."

New sentence keeps `(to-verify)` and reverses the location claim: the capability **is** in this page's
body, in the まとめ方 section — 「同じ世界でシリーズや複数の作品を書くなら、世界観設定を作品をまたいで共有
できます。」 — and the reason it stays a lead is that it is stated as a capability of the page's product,
in a paragraph listing what that product does, not as a rule for authoring.

### 3. Ids and S877 scope (residual 3 / mandate item 3) — done for the draft, row-level part not mine

- Ids in the draft: **S877** (5 lines), **S881** (31), **S882** (9). `grep -c 'S729\|S730\|S742\|S743\|S754\|S895'` → **0**; no
  `S882`-as-Sidorova citation (S882 is tuduku everywhere; the monograph is S877 everywhere).
- S877's one out-of-pin citation was the classification-item quote on **p. 16**. It carried the claim
  "fictional languages exist for a world's atmosphere, not for communication"; that claim now rests on
  **p. 139**: 「ВЯ в общем случае не служит средством коммуникации, он является предметом, темой
  коммуникации」. The source line's locator list was narrowed to the pinned pages (7, 35, 36, 139 and
  140) and the comparison-table row that mirrored the old wording was updated to match.
- No claim that S877 states a framing of setting method: §2's id-bearing sentences cover only
  world-building as the context of conlang-making (p. 7 instrument, p. 139 topic-not-means, p. 35
  either direction, p. 36 premise), and the §2 scope paragraph limits the entry's claims about worlds
  to the three it enumerates — instrument, subject-not-means, premise; the p. 35 line states the
  relation between construction and modelling, not a fact about any world.
- RevEntryQuality §6's third residual is row-level (the staged S883 title and anchor must not be
  appended as-is). The draft's source lines already replace all three staged locators; the registry
  row itself is outside this seat.

### 4. Quotes added or changed — verified this turn (fetch + extraction in `/tmp/ScribeEntryBase/r74/`)

| Span | Source | Locator | Check run |
|---|---|---|---|
| 「ВЯ в общем случае не служит средством коммуникации, он является предметом, темой коммуникации」 (13 w) | S877 | printed p. 139 | `pdftotext -enc UTF-8 -f 139 -l 139` → `grep -c -F` = 1 |
| 「同じ世界でシリーズや複数の作品を書くなら、世界観設定を作品をまたいで共有できます。」 (41 ch) | S881 | h2「世界観設定のまとめ方」, final paragraph before 「おわりに」 | 1 hit in the tag-stripped, whitespace-folded page. **Raw-HTML `grep -F` = 0**: an inline `<a href="/ja/features/series-management">` wraps 「作品をまたいで共有」, so the span only resolves on extracted text |
| Gate quote 「自然環境が社会の仕組みを決め、社会の仕組みが文化を生み、文化が登場人物の価値観を作る。」 | S881 | h3「3. 外側の層へ因果をつなぐ」 | 1 hit in raw HTML |
| Gate quote 「勢力図・人間関係の構造：誰が権力を持ち、何が対立の軸になっているか」 | S882 | item 5 of the「世界観設定の5要素」box | raw HTML splits at `<strong>`; 1 hit in tag-stripped text |

Both pages were re-fetched this turn with the recorded browser-shaped User-Agent:
`HTTP 200` litmemo `bytes=101615`, `HTTP 200` tuduku `bytes=17068` — the same sizes the draft's source
lines record. The PDF was not re-fetched; its sha256 was re-derived from the stored copy and still
equals the source line's `e512a20dd3eef97ed403bd4191545dea1147279d82b7cced32aaa6037ca595a9`, and every
pinned page was re-extracted and re-located this turn.

### 5. Lints (pasted, read-only)

```
$ python3 tools/check-cited-lines.py .ufo/waves/round-74/drafts/worldbuilding-setting-practice.md
CITED-LINES: 0 finding(s) in 1 file(s)          # exit 0
$ python3 tools/check-draft-ids.py .ufo/waves/round-74/drafts/worldbuilding-setting-practice.md
DRAFT_IDS: 0 findings                            # exit 0
$ grep -o 'S[0-9]\{3\}' <draft> | sort | uniq -c
      5 S877
     31 S881
      9 S882
$ wc -l -w -m <draft>
267 4317 26097                                  # ENTRIES floor is 478 words
$ grep -ci 'six tables' <draft>
0
```

### 6. Stale text left standing above

- §2's locator table still lists the p. 16 quote, and §4's census still reads 265 lines / 4,194 words /
  6 S877. Both are the wave-1 record of what was verified then; the current draft cites no p. 16 span
  and carries 5 S877 lines. They are left unedited rather than rewritten, so the record stays auditable.
- F10's reason for the `(to-verify)` ("the linked article's promise, not this page's own body") is
  superseded by residual 2 and now appears only there.

### 7. Not done

Registry rows and the S877 `used-by` edit, the round-74 `## Gate` records, the `reports/round-74/evidence/`
windows, the counter `reports/round-74/accept-c.py`, the README/index row, and any landing — all other
seats' legs.
