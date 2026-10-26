# CritFactBase2 — attack on `culture-material/worldbuilding-setting-practice.md` §6–§10 (claim C, round 74 w2)

Seat: CritFactBase2 (leaf). Target: the second half of
`corpus/knowledge/culture-material/worldbuilding-setting-practice.md`, from `## §6` (line 124) to
EOF (line 267), plus the calibration rows in §1 that the dispatch names, the coupling section
(§10), the canon/handoff section (§10 tail), and the cross-file relation to
`worldbuilding-setting-practice.amend-2026-10-23.md` (claim C's second entry).

Frozen inputs read before attacking:

- `git show 00c408a0af2fa5ddf65af2224152ce258b26d896:reports/round-74/claims.json` — sha256
  `270e31790e2932c8d418904e16e721a6ae5343e4e2c157e5409c1c27dfdeca19`; the graded tree's copy and
  the copy at claim C's lands `c4bf61a8` are the same bytes (all three hashes printed identical).
- Graded entry bytes are identical at C lands `c4bf61a8` and at worktree HEAD `1d7add3`:
  `worldbuilding-setting-practice.md` sha256
  `2a81bea69e9e06b3eb063c9c25f5c34cd1b9d67363367c9807523469c827da96`, amend
  `cdab71c6145ea50d217dd2c5d7c7e59c835c333b542b771c1b725e8369dd4529`
  (`git diff --stat c4bf61a8 HEAD -- <both files>` → empty).
- Authority read: `PROVINCE.md`, `corpus/knowledge/synthesis/worldbible-integration-contract.md`,
  `synthesis/consistency-verification-checklist.md`, `synthesis/coupling-model.md`.

## Verdict

**Claim C SURVIVED the second-half attack.** No BLOCKER. The claim's rule (the 13 frozen legs) does
not read quote truth beyond the Gate span, does not read `couples:` resolution, and does not read
the header's `gap filled` text, so none of the findings below flips a frozen leg — I verified that
by re-running both counters in my own clone (see §Counters). The prose, however, carries **one HIGH
and three MEDIUM fidelity defects** that a reader can check in one click, plus seven LOW defects.

**Overlap with sibling seats** (I read their landed wave-2 files; I did not message anyone). Five
findings are **full corroborations** of defects already filed — F1 = CritFactAmend2 F1,
F2 = ScoutReopenS877 F7, F5 = RevEntryBaseFinal (fix C6), F6 = ScoutReopenS882 F1,
F9 = CritFactBase1 F5 — and two are **partial**: F3's false sentence is RevEntryBaseFinal F6/C7 but
the uncoupled owners are not, F8's 差別 is C5 but two other gloss drifts are not. The **new**
material here is F4 (the §9/contract freeze collision), F7 (the currency dropped from the
quick-reference row), F10 (the `coupling-model` over-claim), F11 (the contract has no payload for
the schemas §10 hands off), the two uncoupled `era-periodization-models` /
`glossary-registry-format` paths, the verified S877 p. 16 datum that makes F2 repairable, the two
remaining gloss drifts, and the independent live-page evidence that makes each corroborated defect
re-checkable without trusting another seat's transcript.

| id | sev | one line |
|---|---|---|
| F1 | HIGH | the amend's `gap filled` says the entry it amends "does not say which part is built first" — the entry's §4 is titled *Build order* and prints two orders |
| F2 | MEDIUM | §10:261 attributes an "atmosphere function" to `conlang-scholarship.md`; that entry records the **poetic function** and Henning's **volume rule**, and the term occurs nowhere in the corpus but this line |
| F3 | MEDIUM | §10:259 justifies the map/name couples with "the note's first two sections are exactly those artefacts" — the note's second section is 年表・歴史 (chronology); the chronology and glossary sections have owners in the lane that are not coupled |
| F4 | MEDIUM | §9:248 ("write the change back the same day") is handed to lore as a discipline, but the contract freezes delivered versions (`contract:151`, `:155`); the pre-/post-handoff scope is unstated |
| F5 | LOW | §8:224 header "Repair, in the sources' own advice" — "cut it" is in neither page |
| F6 | LOW | §6:142–146 and §7:167–174 carry unmarked design inferences, one of them an audience claim that contradicts §1:28's own "not as 'this is how readers behave'" |
| F7 | LOW | §9:251 drops 通貨 (currency), the very unit its own body example drifts |
| F8 | LOW | §7:171/184/194 gloss drift: 何を買うか→"what money circulates"; 周りからの差別→"standing"; the keepers themselves (not "their children") are avoided in marriage |
| F9 | LOW | §1:20 "no citation" over-broad: the page cites Tolkien's 1939 lecture and names Sanderson and three works |
| F10 | LOW | §10:263 over-claims compatibility with `coupling-model.md`, whose stated position is "interderive constraints, not cultural essences" and whose graph has no individual-experience node |
| F11 | LOW | §10:265 hands off "the element and note schemas" but contract §5 defines no payload row for a setting note, element schema or build order |
| O1 | LOW (out of my claim) | claim Ca's `RECEIPTS` leg failed once in a clean clone (exit 2, empty stdout) and passed twice afterwards; the leg discards the re-run's stderr |

Fetch hygiene (QUALITY 21/22/24) — every fetch below used the recorded browser-shaped UA,
`Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`,
plain `curl`, one attempt, no wall, no automation:

```
$ curl -sS -A "$UA" -o S881.html -w 'code=%{http_code} size=%{size_download} url=%{url_effective}\n' \
    https://litmemo.com/ja/blog/novel-worldbuilding-guide
code=200 size=101615 url=https://litmemo.com/ja/blog/novel-worldbuilding-guide
$ sha256sum S881.html
441fc921cadc744a7d59f91a055ff2eec1359d24f5c331d783104a1fa334ca64  S881.html
$ curl -sS -A "$UA" -o S882.html ... https://tuduku.space/column/novel-worldbuilding
code=200 size=17068  (response date: Mon, 26 Oct 2026 02:00:57 GMT; local -0300 2026-10-25 23:00)
$ sha256sum S882.html
754f504c34d796f40e86fb0d98c98946e36284c5fae511d7837f442662cfc1b7  S882.html
```

Both bodies are byte-identical to the frozen evidence files
(`reports/round-74/evidence/S881.txt` `sha256: 441fc921…`, `S882.txt` `sha256: 754f504c…`), so the
quote checks below are against the same bytes the round froze. Re-extraction with a stdlib
`html.parser` walker (same drop/block rules as the recorded `extract:` line) gives **9855** chars for
S881 and **2953** chars for S882 — the recorded `visible-chars:` values, exactly.

---

## 1. Carried / not-carried table — every source sentence behind §6–§10

Locators are the served page's own headings. "verbatim" = found after NFKC + whitespace folding in
my live extraction; the quoted spans are ≤25 whitespace tokens.

| # | source claim (locator) | entry line | status |
|---|---|---|---|
| 1 | S882 h2 世界観設定に必要な5つの要素, box 世界観設定の5要素 items 1–5 | 126–134 | carried, 5/5; item 5 quoted verbatim |
| 2 | S882 「特に重要なのは魔法・技術システムの「制約」です。」 | 136 | **verbatim** |
| 3 | S882 「魔法・技術システム：何ができて何ができないか。ルール（制約）が重要」 | 138 | **verbatim** |
| 4 | S882 設定ノートの構成例, 5 items | 140–146 | carried, 5/5; the third column is the entry's addition, not the page's |
| 5 | S882 「世界地図・地名一覧：手書きでよいので地図を描いておく」 | 148 | **verbatim** |
| 6 | S881 世界観設定のまとめ方, 4 fields (種類/説明/ルール/関連) | 150–157 | carried, 4/4 |
| 7 | S881 架空の国の作り方「次の8項目」, table rows 1–8 | 163–174 | carried, 8/8; rows 171 and 172 gloss-drifted (F8) |
| 8 | S881 「「国の傷」は見落とされがちですが…世代ごとの価値観の違い…」 | 163, 176 | carried, correctly labelled "the eighth … easiest to overlook" |
| 9 | S881 魔法の設定で決めること, 7 rows + 「見落とされやすいのは最後の二つです。」 | 178–188 | carried, 7/7; "the last two … most often missed" is the page's own sentence |
| 10 | S881 代償のない力は物語の緊張を壊します…ピンチは生まれません | 190 | carried |
| 11 | S881 ハードマジック/ソフトマジック, ブランドン・サンダースン named, no edition | 192 | carried **as reported**, and explicitly not as Sanderson's text — correct handling |
| 12 | S881 霧隠の灯台守 example (thin the fog, never dispel; eyesight; honoured; marriage avoided) | 194 | carried; "their children" added (F8) |
| 13 | S881 深さ 核の設定/背景の設定/彩りの設定 + 本文に書くか | 200–206 | carried, 3/3 |
| 14 | S882 ジャンル別：設定の深さの目安, 5 rows | 210–216 | carried, 5/5, bound to the right page (S881 has a *different* genre table; the wording here matches S882's 魔法システム・身分制度・地理 etc.) |
| 15 | S882 KEY POINT box 「世界観設定は「作者が知っていること」と「読者に伝えること」を分けて考えましょう。…」 | 218 | **verbatim** |
| 16 | S882 失敗タイプ table, 4 rows | 220 | carried, 4/4 (symptoms/impacts folded) |
| 17 | S881 世界観づくりのよくある失敗, 4 items | 222 | carried, 4/4 |
| 18 | S881 ❌「…魔法使いは『詠み手』と呼ばれる…」/ ✅「その詠み手に口を開かせるな！」隊長が女の喉元に弩を突きつける | 231 | carried; "commander's threat at a woman's throat" is the page's ✅ line |
| 19 | S881 step 5 「決めた設定は一つの場所に集め、本文を書くたびに参照します。本文で設定を変えたら、その場で設定資料も書き換えます。」 | 235 | **verbatim**, and it is under heading 5. 一か所にまとめ、書きながら更新する (not misplaced) |
| 20 | S881 FAQ 合作やTRPG… 「全員が同じ設定資料を一つだけ使い、それを正本にします。」… | 237, 239, 241 | **verbatim**; the write-back and no-private-notes continuation and the public/GM split are all present |
| 21 | S881 「第3話で「金貨」と書いたものが第20話で「金竜貨」になる、という食い違いはここから起きます。」 | 243 | carried — **this example is really on the page** (attack A2 failed) |
| 22 | S881 「通貨・暦・長さや重さの単位・敬称・命名ルールは、一枚の早見表にまとめておくと便利です。」 | 251 | carried, but the row lists "units, calendar, titles, naming" and drops 通貨 (F7) |
| 23 | S881 まとめ方 product paragraph 「同じ世界でシリーズや複数の作品を書くなら、世界観設定を作品をまたいで共有できます。」 | 253 | **verbatim**, and correctly characterised as a product-capability paragraph, kept `(to-verify)` |
| 24 | S877 (pp. 7/35/36/139/140 per the header) | — | not cited in §6–§10; consistent (those pages sit in §2) |

Not carried from the two pages (by design, and the entry says so): S882's Notion/Google-Docs
tooling sentence, S881's template/CTA paragraphs, the reader-impact column of S882's failure table,
and S881's fantasy-subgenre table. None is claimed by the entry, so none is a defect.

Source claims the entry adds and does not attribute (collected under F5/F6): the third columns of
the tables at 128–134, 140–146, 165–174 and the "What it forces"/"What it prevents" columns.

Verbatim re-check of all eight quoted spans in §6–§10 (live extraction, NFKC + whitespace fold):

```
126 S882 live= True     136 S882 live= True     138 S882 live= True     148 S882 live= True
218 S882 live= True     235 S881 live= True     237 S881 live= True     253 S881 live= True
```

Two of the eight (§9's 235 and 253) lie **outside** the committed 4098-char excerpt window of
`reports/round-74/evidence/S881.txt` (`in-window= False`), which the frozen EVIDENCE leg permits
(it requires only the Gate span). They are true on the live page; my re-open is what closes them.
Recorded as a residual, not a defect.

## 2. Coupling paths — existence and what the sibling actually says

`git cat-file -e main:<path>` on each of the six `couples:` paths + the entry itself: all `OK`
(cartography 38971 B, naming-systems 27066 B, conlang-scholarship 13960 B, coupling-model 31331 B,
checklist 41048 B, contract; self and amend present).

| path | what the sibling records | what the entry claims (§10 / header) | verdict |
|---|---|---|---|
| `culture-material/cartography-and-mapmaking.md` | the map as instrument and claim; survey→projection→drawing→reproduction; build order | "the map that opens a settings note", "couples outward to the map" | ✅ exists, description fair (the mapmaking entry is far heavier than a hand sketch, but the entry couples *outward*, it does not restate it) |
| `linguistics/naming-systems.md` | anthroponymy, toponymy, theonymy, exonyms, naming pipeline | "the name and place-name lists the note carries" | ✅ exists, description fair |
| `linguistics/conlang-scholarship.md` | §4 "How much language the world actually needs" — **Henning's volume rule** (`:55`); §5 names **the poetic function in Jakobson's sense** (`:72`) | "the **atmosphere function** of a world's language sets how deep the language file goes" | ❌ **F2** — the term does not exist in the sibling (or anywhere else in `corpus/knowledge`) |
| `synthesis/coupling-model.md` | `X[t,place,community,occasion] = {L,M,S,E,C}` conditioned on `B` ecology/material production, `I` institutions/access, `H` inheritance/contact; "interderive constraints, not cultural essences" (`:20`) | "where the four layers meet the systems the rest of the corpus owns" | ⚠️ partial — `B`/`I`/`{L,M,S,E,C}` cover three of the four layers; no node carries 個人の経験, and the model's stance is constraint, not the entry's causal chain (**F10**) |
| `synthesis/consistency-verification-checklist.md` | COMPATIBLE/CONFLICT/VARIANT statuses (`:29–31`), findings go to lore (`:25`, C47 `:151`) | "owns conflict and variant statuses … hands findings to lore" | ✅ exact |
| `synthesis/worldbible-integration-contract.md` | §1 lore owns canon decisions and bible-wide verification; §5 payload rows (system, diachronic, lexicon, naming ledger, myth register, era-costume matrix, coupling register); §9 freeze/version rules | "Hand off under … supplies the order, the layers, the element and note schemas and the single-source discipline; lore decides …, records the canon, and verifies consistency" | ⚠️ authority half ✅ (`PROVINCE.md` Refuses/Adjacent, contract §1); payload half has no row (**F11**); §9 scope gap (**F4**) |
| *(not coupled)* `culture-material/era-periodization-models.md` (exists) | how cultures cut their own time | the note's 年表・歴史 section, "chronology is the first thing to drift" | ❌ missing couple — the note schema §6:143 needs it (**F3**) |
| *(not coupled)* `synthesis/glossary-registry-format.md` (exists) | canonical glossary-entry profile, identity/fields/history | the note's 社会制度・用語集 section, "one glossary prevents one object acquiring three names" | ❌ missing couple, but no schema restated, so no duplicate authority (**F3**) |
| *(not coupled)* `linguistics/toponymy-place-names.md` (exists) | place names | 地名一覧 | suggestion: `naming-systems` also covers toponymy, so not wrong; the more specific owner exists |

No duplicate authority found for the magic/technology sub-sheet: `ls corpus/knowledge/*/` shows no
magic-system or technology-system entry; §7 defines no schema the corpus already owns.

## 3. Statements about the lane and lore (PROVINCE + contract)

| statement | authority checked | verdict |
|---|---|---|
| §10:265 "lore decides which of them a given world adopts, records the canon, and verifies consistency" | `PROVINCE.md` Refuses ("claiming or recording canon — that is lore-shokunin"), Adjacent contract; contract §1 | ✅ no canon claimed, no rights ruled |
| §9:255 "the checklist that owns conflict and variant statuses takes a note like this as its input and hands findings to lore" | checklist `:29–31`, `:25`, C47 `:151` | ✅ (the checklist's remit says it runs "on a supplied candidate bundle"; a note as one artifact of a bundle is a fair reading — overreach at most) |
| §9:243/§10 header — verification "is not this entry's business" | `PROVINCE.md` (lore verifies; kotodama owns its own gates) | ✅ |
| §10:267 "Nothing here rules on any world. No layer assignment, no element count, no depth target and no document layout is fixed …" | spot-check of every imperative in §6–§10 | ✅ sentence-by-sentence: every imperative is labelled "Design consequence" or sits in a "What to do"/"Repair" column; the five/four counts are reported as the pages' checklists and §1:26 refuses reading them as a standard |
| §10:265 handoff payload | contract §4/§5 | ⚠️ F11 |
| §9 single-source rule as a handed-off discipline | contract §9:151, §9:155 | ⚠️ F4 |

**Canon/rights check, stated explicitly:** no sentence in §6–§10 decides canon for any world and no
sentence rules on rights. The two nearest misses are §10:265 (defers, does not decide) and §7:192
(declines to attribute the hard/soft split to Sanderson's text). The entry also does not rank or
disparage a real-world culture anywhere in this half.

---

## 4. Findings

### F1 — HIGH — the amendment's stated gap is false against the entry it amends (cross-file, same claim)

*Filed elsewhere:* CritFactAmend2 F1 (HIGH) reached the same defect independently (it adds the
index row landed with the claim as a second falsifier). My evidence below is the §4/§5 text and the
amend's own §6:90; it is recorded here so the round has two independent sightings, not one.

Command (both files byte-identical at C lands `c4bf61a8` and at HEAD; hashes in the header):

```
$ awk 'NR==10' corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md
- gap filled: the entry this amends records what a setting is made of and the settings-note tables
  that carry it; it does not say which part is built first, which part is derived from which, or
  when in a serial the reader is shown any of it.
$ awk 'NR==72;NR==74;NR==101' corpus/knowledge/culture-material/worldbuilding-setting-practice.md
## §4 Build order — the five steps, and the two orders they allow
The five-step order as the page states it: "世界観の作り方は、①物語の核になるルールを決める
  ②主人公の生活圏から作る ③自然→社会→文化→個人の順に因果をつなぐ ④物語で使う分だけ掘り下げる
  ⑤一か所にまとめて書きながら更新する、の5ステップです。" (S881).
## §5 The four-layer chain — cause outward, experience inward
```

The amended entry states the build order **twice** (S881's five steps at 74, S882's five moves at
78 and the comparison table 82–88), the "which part is derived from which" rule at 101 (the causal
chain), and the world-first/scene-first fork at 90–95. So "does not say which part is built first, which part is
derived from which" is false at lands. It is also inconsistent with the amend's own §6:90
("No second author's build order is compared here") — a second and a third author's orders are in
the very entry it amends, and the amend never relates its S883 order to them. A reader who trusts
the gap field will not look for §4; a reader who does will find two rival build orders with no
statement of how they relate.

Impacted axes: provenance/fidelity of claim C's second entry; the header field is what the ENTRIES
leg reads for shape, so this survives the counter while being false.

Smallest safe correction: narrow the gap to the true residue — *"it does not record one author's
stated build order and derivation rule, and it says nothing about when in a serial the reader is
shown the world's rules"* — and add one sentence to §6:90 naming §4's orders and saying why S883's
differs (world-view→progression→expression vs premise→living sphere→outward chain).

### F2 — MEDIUM — "atmosphere function" is not in the coupled entry (false attribution)

```
$ grep -rn -i 'atmospher' corpus/knowledge/ | grep -v civilizations | grep -v vessel
corpus/knowledge/culture-material/worldbuilding-setting-practice.md:261:It couples inward to the
language layer (`linguistics/conlang-scholarship.md`): the atmosphere function of a world's
language sets how deep the language file goes, not the other way round.
$ grep -n -i 'function\|volume' corpus/knowledge/linguistics/conlang-scholarship.md
55:The book reports Henning's volume rule: the required size and detail of lexicon and grammar
   follow from what the language is for (S877).
72:It names the leading function: where auxiliary languages are built for communication, fictional
   languages are built for the poetic function in Jakobson's sense — attention to the message for its
   own sake (S877 p. 21).
```

The coupled entry has no "atmosphere function"; it has Henning's **volume rule** (size follows what
the language is for) and the **poetic function**. The entry contradicts itself in the same file: §2
(line 40) already calls it "the same volume rule `linguistics/conlang-scholarship.md` records". So
the sentence is a term-invention with a false pointer, not a paraphrase of the sibling.

The word does exist one step further back — in the monograph the coupled entry reports, not in the
coupled entry. I verified it on the same PDF the round froze (fetch below, sha256 equal to
`reports/round-74/evidence/S877.txt`'s `e512a20…`), printed p. 16:

```
$ pdftotext -enc UTF-8 -f 16 -l 16 conlangs.pdf p16.txt && grep -n 'атмосфер' p16.txt
15:2.3. Фикциональные (для создания атмосферы вымышленного мира,
```

So a correct sentence is possible with the right pointer: the book's class 2.3 is "fictional
languages, for creating the atmosphere of an invented world, not used in real communication"
(S877 p. 16), and the volume rule says how much of one is needed. What is not possible is the
present pointer to an entry that does not carry the term.

*Filed elsewhere:* ScoutReopenS877 F7 (LOW) names the same attribution. I keep it at **MEDIUM**
because it is the only coupling in §10 a reader cannot follow, and because the entry's own §2:40
uses the correct term for the same rule — an internal contradiction, not a slip of phrasing.

Impacted axes: coupling fidelity. The substantive claim (depth follows function, not the reverse)
is sound and is exactly the volume rule, so this is a fixable defect, not a tradeoff.

Smallest safe correction: either restore the book's term with its page — *"the atmosphere function
of a world's language (S877 p. 16, class 2.3) sizes the language file, and Henning's volume rule
gives the amount (`linguistics/conlang-scholarship.md:55`); the reverse never holds"* — or drop the
attribution and keep the sibling's own words: *"Henning's volume rule (`:55`) and the poetic
function named at `:72` set how deep the language file goes, not the other way round."*

### F3 — MEDIUM — the §10 justification for the map/name couples is wrong, and two owned sections are left uncoupled

*Filed elsewhere, in part:* RevEntryBaseFinal F6 (LOW) files the sentence's error and fixes it as
C7. Its C7 rewrites the claim but leaves the note's second and fifth sections with no coupled owner;
that half — the coupling gap — is the part I rate MEDIUM and the part C7 does not close. Read the
two halves separately: the false sentence is LOW and already has a fix; the uncoupled
`era-periodization-models` / `glossary-registry-format` owners are the new material.

```
$ awk 'NR==259' corpus/knowledge/culture-material/worldbuilding-setting-practice.md
The chain couples outward to the map (`culture-material/cartography-and-mapmaking.md`) and to the
name lists (`linguistics/naming-systems.md`), because the note's first two sections are exactly
those artefacts.
```

The note's five sections (S882 設定ノートの構成例, live extraction, in order):

```
世界地図・地名一覧：手書きでよいので地図を描いておく
年表・歴史：「○年前に魔王が現れた」などの時系列を整理
魔法・能力一覧：各スキル・魔法の能力・制約・習得条件
人物一覧：名前・年齢・外見・性格・役割・他キャラとの関係
社会制度・用語集：独自の職業・身分・宗教・貨幣単位など
```

Section 2 is a **chronology**, not a name list; the place-name list is inside section 1. So the
sentence's "exactly those artefacts" is false under either reading, and the omission hides two
owners the lane already has:

```
$ ls corpus/knowledge/culture-material/era-periodization-models.md corpus/knowledge/synthesis/glossary-registry-format.md
corpus/knowledge/culture-material/era-periodization-models.md
corpus/knowledge/synthesis/glossary-registry-format.md
```

Impacted axes: coupling coverage; the couples header cannot be checked by any frozen leg, so the
gap is invisible to the counter.

Smallest safe correction: *"The chain couples outward to the map
(`culture-material/cartography-and-mapmaking.md`) and to the name lists
(`linguistics/naming-systems.md`; place names also `linguistics/toponymy-place-names.md`), because
the note's first section is the drawn map with its place names; its second section is a chronology
(`culture-material/era-periodization-models.md`) and its fifth holds a glossary
(`synthesis/glossary-registry-format.md`), which this entry names but does not schematise."* Add
the two paths to `couples:`.

### F4 — MEDIUM — "write the change back the same day" collides with the contract's freeze rule once handed off

```
$ awk 'NR==248' corpus/knowledge/culture-material/worldbuilding-setting-practice.md
| write the change back the same day | serialised drafting | the note lagging the text |
$ grep -n 'Freeze released versions\|pins exact delivered' corpus/knowledge/synthesis/worldbible-integration-contract.md
151:- Freeze released versions; corrections are new records/releases with `supersedes`/`derived_from`
     references, not rewrites of old receipts or accepted snapshots (PROV-DM revision; SemVer rule 3).
155:- Lore pins exact delivered versions and digests, not version ranges. No auto-upgrade, including
     PATCH: even a corrected citation needs an auditable adopted revision.
$ awk 'NR==70' corpus/knowledge/synthesis/worldbible-integration-contract.md
- Freeze the manifest before review; changing a referenced file invalidates that delivery's digest
  even if its filename stays unchanged.
```

§9 states an in-place update rule without a scope, and §10:265 hands "the single-source discipline"
to lore. A builder who applies §9:248 to a note already delivered under the contract silently
invalidates that delivery's digest (`:70`) and rewrites an object the receiver pinned (`:155`). This
is a scope gap, not a flat contradiction — S881's rule is for the authoring copy — but the entry
never draws the line, and the handoff sentence invites importing the rule as-is.

Impacted axes: handoff correctness; nothing in the frozen legs reads it.

Smallest safe correction: one clause on §9:248 — *"once a note is delivered under
`synthesis/worldbible-integration-contract.md` the delivered bytes are frozen (§9 there):
corrections are a new version with `supersedes`, not an in-place edit"* — and restate it at §10:265.

### F5 — LOW — "in the sources' own advice" over-attributes: "cut it" is not in either page

```
$ awk 'NR==224;NR==229' corpus/knowledge/culture-material/worldbuilding-setting-practice.md
| Failure | Symptom | Repair, in the sources' own advice |
| unused setting | a designed region or trade route never touched | cut it, or let it resonate somewhere |
$ grep -n '削除\|切る\|捨て\|やめ' /tmp/CritFactBase2/S881.txt /tmp/CritFactBase2/S882.txt
(no matches in either file)
```

S881's advice for an unused setting is 一つひとつの設定は…物語のどこかに響かせましょう ("let it resonate
somewhere in the story") and S882's failure row is a symptom only. "Cut it" is the entry's own
recommendation; a reader checking the pages for it finds nothing.

*Filed elsewhere:* RevEntryBaseFinal files the same cell and fixes it as C6 ("let it resonate
somewhere in the story"). My evidence is the independent live grep above.

Smallest safe correction: header → "Repair (source advice; the entry's addition in brackets)" or
drop "cut it" and keep "let it resonate somewhere".

### F6 — LOW — unmarked inferences, one of them an audience claim the entry itself disclaims

```
$ awk 'NR==28' corpus/knowledge/culture-material/worldbuilding-setting-practice.md
Read every imperative below as "these two pages say", not as "this is how readers behave".
...
$ awk 'NR==145;NR==143;NR==146' (same file)
| 人物一覧 | name, age, appearance, temperament, role, relations | relations are the facts readers catch first |
| 年表・歴史 | dated events in sequence | chronology is the first thing to drift in a long work |
| 社会制度・用語集 | invented trades, ranks, religions, currency units | one glossary prevents one object acquiring three names |
```

Two of the five "Why it is a separate sheet" cells are supported — but by the *other* page: the map
one by S881 「粗い地図を一枚描くだけで、この種の矛盾はほとんど防げます」 and the powers one by S881's
段階と上限 row (決めないまま進むと中盤以降に強さのインフレが起きます), while the column annotates S882's
list and carries no marker for the cross-source blend. "chronology drifts first", "readers
catch relations first" and "one glossary prevents three names" are generalisations absent
from both pages. "readers catch first" is a claim about readers, which §1:28 disclaims ("not as
'this is how readers behave'") and §1:32 confines class-C claims about worlds to the monograph.
§7:167–174's "Why it earns its place" column ("names date their
coiners", "it fixes who can be bribed", …) is the same class of unmarked design inference, though
none of it is an audience claim.

*Filed elsewhere:* ScoutReopenS882 F1 (MEDIUM) lists the same uncited third columns and calls them
what they are. My addition is the internal contradiction with §1:28 and the two cells that *do*
have support, which bounds the fix: only three of the five cells and the §7 column need a marker.

Smallest safe correction: rename the columns "Why the entry keeps it" and mark the reader sentence
as a design assumption, or drop that cell.

### F7 — LOW — the quick-reference row drops the unit its own example drifts on

```
$ awk 'NR==251' ...  | one quick-reference sheet for units, calendar, titles, naming | ... |
$ grep -n '通貨・暦・長さや重さの単位・敬称・命名ルール' /tmp/CritFactBase2/S881.txt
96:通貨・暦・長さや重さの単位・敬称・命名ルールは、一枚の早見表にまとめておくと便利です。第3話で「金貨」…
```

The page's list opens with 通貨, and §9:243's demonstrative example is the currency drift, yet the
row that is supposed to summarise the rule omits currency.

Smallest safe correction: "currency, calendar, units, titles, naming".

### F8 — LOW — three translation drifts in the country sheet and the power sheet

```
S881: 産業と通貨 / 何で稼ぎ、何を買うか            → entry:171 "what it earns with, what money circulates"
S881: 代償は体力、寿命、記憶、正気、周りからの差別…  → entry:184 "stamina, lifespan, memory, sanity, standing, uses"
S881: 灯台守は町で敬われているが、ほかの家からは縁談を避けられる
                                                    → entry:194 "the keepers are honoured and their children avoided in marriage"
```

`何を買うか` is "what it buys", not "what money circulates"; `周りからの差別` is discrimination/
ostracism by those around, and "standing" reads as the opposite direction (the entry's own worked
power shows ostracism); the marriage avoidance is applied to the keepers themselves, and "children"
is added. Each is small; together they are the only places where a builder cannot recover the
page's list item.

*Filed elsewhere, in part:* RevEntryBaseFinal files 差別→"standing" and fixes it as C5. The other
two drifts (`何を買うか`, and "children" added to the keepers) are not in that list, so C5 alone
leaves them.

Smallest safe correction: "what it earns with, what it buys"; "…sanity, ostracism from those
around, number of uses"; "the keepers are honoured but other families avoid marrying them". The
first and third of those need a new cut line; the second is C5.

### F9 — LOW — "no citation" is too broad for S881 (§1:20, calibration row)

```
$ grep -n 'トールキン\|サンダースン\|On Fairy-Stories\|指輪物語' /tmp/CritFactBase2/S881.txt
154:…『指輪物語』のJ.R.R.トールキンは1939年の講演「On Fairy-Stories」で…「第二の世界（Secondary World）」と呼びました。
203:ファンタジー作家ブランドン・サンダースンは、魔法を「ハードマジック」と「ソフトマジック」に分けて論じ…
217:『指輪物語』のガンダルフの魔法
```

The page names a dated lecture and an author, and cites three works as examples; "no citation" is
true only for the five-step method. "no named author" is correct — the JSON-LD `author` node is an
`Organization`, and the page shows no byline beyond つづく編集室 for S882.

Smallest safe correction: "no citation for its method (it names Tolkien's 1939 lecture and
Sanderson without an edition)".

*Filed elsewhere:* CritFactBase1 F5 (LOW) is the same defect with the same fix, and RevEntryBaseFinal
C2 is the cut line. §1 is the first-half seat's section; this entry is a corroboration, counted once
by the round. I keep it because my independent check of the served page also settles the adjacent
"no named author" claim (JSON-LD `Organization`), which that row needs in order to be repaired
correctly.

### F10 — LOW — §10:263 over-claims compatibility with `coupling-model.md`

```
$ awk 'NR==263' ...  It couples sideways to the relation model (`synthesis/coupling-model.md`),
which is where the four layers meet the systems the rest of the corpus owns.
$ awk 'NR==20;NR==21' corpus/knowledge/synthesis/coupling-model.md
- Condition every state on `B` = ecology/material production, `I` = institutions/access, and
  `H` = inheritance/contact history. None is a substitute for people's choices.
- **No total-culture switch:** different communities can share clothing but not language …
```

`B` and `I` do correspond to the chain's first two layers and `{L,M,S,E,C}` to 文化, so the coupling
is not false; but the fourth layer (個人の経験) has no node (H is inheritance/contact), and the model
opens with "interderive constraints, not cultural essences" — the stance the entry's causal chain
(`:101`) is calibrated against at §1:22 but never reconciled here. The sentence reads as if the
model already contains the chain.

Smallest safe correction: append "— with `B`/`I` for the first two layers and the model's own
constraint-not-cause rule (`coupling-model.md:20`) standing in for the fourth".

### F11 — LOW — the handoff names payloads the contract does not define

```
$ grep -n '^## 5. Artifact payloads' corpus/knowledge/synthesis/worldbible-integration-contract.md
72:## 5. Artifact payloads: systems, lexica, naming ledgers
   (rows: System specification, Diachronic specification, Lexicon, Naming ledger, Myth-symbol
    register, Era-costume matrix, Coupling register — no setting note, no element schema, no build order)
$ awk 'NR==265' ...
Hand off under `synthesis/worldbible-integration-contract.md`: this entry supplies the order, the
layers, the element and note schemas and the single-source discipline; lore decides which of them a
given world adopts, records the canon, and verifies consistency.
```

The authority half is right (contract §1, `PROVINCE.md`); the artifact half has no home in §4/§5, so
a builder following the pointer finds no envelope recipe for a setting note. §10:265 is also the
only handoff sentence in this half, so the gap is not covered elsewhere. The same phrasing exists in
`linguistics/conlang-scholarship.md:106` (2 files in the lane use "Hand off under …"), so it is an
established habit rather than an invention — which is why this is LOW.

Smallest safe correction: either name the two payload rows the note's contents can ride
(`claim_ledger` for the design decisions, `coupling_edges` for the layers) or record the missing
payload as an explicit open question in the entry's §10.

---

## 5. Attacks that FAILED (the claim survived, with the evidence)

| attack | result |
|---|---|
| A1 quote mutation — every quoted span in §6–§10 differs from its page | **failed**: 8/8 verbatim after NFKC + whitespace folding, against live bodies whose sha256 equals the frozen evidence |
| A2 fabricated example — the 金貨/金竜貨 drift (§9:243) is not on S881 | **failed**: it is at S881 line 96 of the extracted text, in the 早見表 sentence |
| A3 false "no capture" CDX ruling (header lines for S881/S882) | **failed**: canonical-slug CDX probes return `[]` for both slugs; positive controls work — `litmemo.com` root has 3 captures (`20260911102443`, `20260911102629`, `20261010230039`) and `example.com` has the expected 2002 captures; `tuduku.space` has no host-level capture either, so the S882 host claim also holds |
| A4 Gate locator invention | **failed**: S881's Gate span sits under h3 「3. 外側の層へ因果をつなぐ」 as the paragraph's 2nd sentence; S882's is info-box item 5 under h2 「世界観設定に必要な5つの要素」 — both as recorded |
| A5 dangling `couples:` path | **failed**: all six resolve at main; self and amend resolve |
| A6 canon or rights ruling hiding in §6–§10 | **failed**: none; §10:265 defers to lore, §7:192 refuses to attribute the split to Sanderson's text |
| A7 duplicate authority for the magic/tech sub-sheet | **failed**: the lane has no magic-system/technology-system entry; §7 restates no existing schema |
| A8 genre table misbound to the wrong page (S881 has its own genre table) | **failed**: the five rows match S882's 魔法システム・身分制度・地理 / 登場人物の背景・職場・家庭環境 vocabulary, not S881's |
| A9 the "1,100 characters by its own count" calibration claim is invented | **failed**: the served S882 prints 約1,100文字 in its own header block |
| A10 "no named author" is false | **failed**: page JSON-LD `author` is an `Organization`; no byline anywhere |
| A11 the entry's own five-section note is not the page's list | **failed**: one-to-one with S882's 設定ノートの構成例, in order |
| A12 the claim's legs do not hold at lands | **failed**: both counters PASS in my clone (below) |

## 6. Counters (run only inside my own clone, per the dispatch)

```
$ D=$(mktemp -d); git -C "$D" init -q; git -C "$D" rev-parse --show-toplevel   # printed $D
$ git clone -q /home/vgpnk/Projects/shokunin/kotodama-shokunin "$D/lane"
$ git -C "$D/lane" checkout -q --detach && git -C "$D/lane" branch -f main c4bf61a8d722f9168ce0fd8021a6261c000610c5
$ cd "$D/lane" && python3 -B reports/round-74/accept-c.py --root . \
    --lands c4bf61a8d722f9168ce0fd8021a6261c000610c5 \
    --freeze 00c408a0af2fa5ddf65af2224152ce258b26d896 --fleet-root /home/vgpnk/Projects/shokunin
…
LEG PASS INDEX
ACCEPT-C-74: PASS legs=13/13            EXIT=0
```

(Counter self sha256 `8d30487f…`; config read from the freeze, `270e3179…`; measured lane main
`c4bf61a8`.)

```
$ git -C "$D/lane" branch -f main 5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3 && cd "$D/lane" \
  && python3 -B reports/round-74/accept-ca.py --root . --lands 5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3 \
     --freeze 00c408a0af2fa5ddf65af2224152ce258b26d896 --fleet-root /home/vgpnk/Projects/shokunin
ACCEPT-CA-74: PASS legs=11/11           EXIT=0     (2nd and 3rd runs; see O1)
```

### O1 — LOW, routed to main (claim Ca, not my claim) — one transient `RECEIPTS` failure

First run, same clone, same pin, same command:

```
LEG FAIL RECEIPTS
     rev=2d1cd9140d3a receipts=['accept-c-73=50c60bb67f16', 'accept-ca-73=864c94192854']
     problems=['accept-c-73 re-run exit=2 (want 0)', "accept-c-73 re-run did not print
     'ACCEPT-C-73: PASS legs=11/11'", 'accept-ca-73 re-run exit=2 (want 0)', "accept-ca-73 re-run
     did not print 'ACCEPT-CA-73: PASS legs=9/9'",
     'reports/round-74/telemetry/accept-c-73-at-lands.txt: committed stdout differs from the re-run
     (bda16ca6deec vs e3b0c44298fc)', '…accept-ca-73-at-lands.txt: committed stdout differs from
     the re-run (55544779204d vs e3b0c44298fc)']
ACCEPT-CA-74: FAIL legs=10/11           EXIT=1
```

`e3b0c442…` is sha256 of the empty string, i.e. **both re-runs produced no stdout at all** and exited
2 — consistent with the round-73 counter failing before its first print (its own exit-2 paths print
to stderr, which `accept-ca.py:1739` captures and then discards). Both later runs of the same
command in the same clone passed with `problems=[]`, and I reproduced the round-73 counters
manually with the identical restricted env (`env -i … LC_ALL=C.UTF-8 TZ=UTC …`) — `ACCEPT-C-73:
PASS legs=11/11`, exit 0 — so the frozen bytes are fine and the leg is **non-deterministic**, not
wrong. `/tmp` was 97% full (5.0 GB free) at the time, and the leg nests three clones plus two
`git archive` trees under `/tmp` [INFERENCE: resource exhaustion inside the round-73 materialize].

Proposed fix (Ca side, one line): in `_run_r73_counter`, include `p.stderr[-2000:]` (or its sha256)
in the `problems` entry when `returncode != 0`, and give the leg one retry before failing — a
counter whose red can be an OOM is not reproducible for a grader. Recording both runs here so the
round does not mistake a flake for a pass or for a failure.

## 7. Tooling / hygiene

- No installs, no upgrades, no pacman (host-wide pause respected). Tools used: `git`, `curl`,
  `python3` (stdlib only), coreutils. Nothing written outside this file and `/tmp/CritFactBase2/`.
- Lane repo left untouched: no branch/index/worktree writes in
  `/home/vgpnk/Projects/shokunin/kotodama-shokunin`; all clone/pin activity was under `/tmp`.
- Fetches: 3 URLs, one attempt each, browser UA recorded above, HTTP 200, no wall, sha256 equal to
  the frozen evidence for each (S881 `441fc921…`, S882 `754f504c…`, S877 PDF `e512a20d…`,
  1,055,723 B; the PDF was read with `pdftotext -enc UTF-8 -f 16 -l 16` for the F2 cross-check).
  CDX probes: 5 queries (`litmemo` slug, `tuduku` slug, `litmemo.com`, `tuduku.space`,
  `example.com`), positive control present.
- Scratch: `/tmp/CritFactBase2/` (extractor, live bodies, extracted text, PDF page 16, counter logs).
