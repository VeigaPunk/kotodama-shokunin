# Worldbuilding setting practice — how a setting is specified, and kept from drifting

- source: S877 — http://www.philol.msu.ru/~sidorova/files/conlangs.pdf — the whole 184-page monograph (1,055,723 bytes, sha256 e512a20dd3eef97ed403bd4191545dea1147279d82b7cced32aaa6037ca595a9): cited here at printed pages 7, 35, 36, 139 and 140, the passages where the book treats world-building as the context of conlang-making — fetched 2026-10-25 live (HTTP 200, browser-shaped UA `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`, no wall), text read with `pdftotext -enc UTF-8` plain mode
- source: S881 — https://litmemo.com/ja/blog/novel-worldbuilding-guide — article as served 2026-10-25 (HTTP 200, 101,615 bytes, sha256 441fc921cadc744a7d59f91a055ff2eec1359d24f5c331d783104a1fa334ca64, same UA, no wall; the Internet Archive CDX holds no capture of this slug, probed 2026-10-25): h2「世界観の作り方：5つのステップ」with h3 steps 1–5, h2「世界観の4つの層」, the per-layer checklist h3 第1層–第4層, h3「5. 一か所にまとめ、書きながら更新する」, the FAQ box
- source: S882 — https://tuduku.space/column/novel-worldbuilding — article as served 2026-10-25 (HTTP 200, 17,068 bytes, sha256 754f504c34d796f40e86fb0d98c98946e36284c5fae511d7837f442662cfc1b7, same UA, no wall; no capture of this slug or host in CDX): the「世界観設定の5要素」and「設定ノートの構成例」list boxes, the failure table, the key-point box
- verified-at: 2026-10-25
- recheck: 180d — re-open the three URLs and re-locate each quoted span at the section its sentence names; extract the PDF with `pdftotext -enc UTF-8` and re-find each quote on the printed page its sentence cites (plain mode de-hyphenates; `-layout` keeps end-of-line hyphens); on the two Japanese pages re-check the h2 and box labels named on the source lines, then the quoted lists
- ground: at base f7104cbce186bc2e1522abf0cfd619cc834628bb the lane held no setting-practice entry and no practitioner term for one — `git ls-tree -r --name-only <base> corpus/knowledge | grep -ciE 'worldbuilding|setting-practice'` = 0, `git grep -lE '設定ノート|世界観|世界观' <base> -- corpus/knowledge | wc -l` = 0, and the registry's 804 rows held no row naming litmemo.com, tuduku.space or chinawriter.com.cn (`git show <base>:corpus/SOURCES.md | grep -c` = 0 for the three hosts; all re-derived from the base commit 2026-10-25)
- topic: the Japanese practitioner craft of specifying a setting, framed against a Russian-language monograph's account of constructed worlds: a five-step build order, a four-layer causal chain from environment to individual experience, five elements a setting must supply, the five sections and four fields of the settings note, two sub-sheets (a country, a magic or technology system), and the single-source discipline that keeps a long work consistent
- gap filled: the corpus couples systems (`synthesis/coupling-model.md`) and verifies them (`synthesis/consistency-verification-checklist.md`), and carried no entry on *authoring* a setting — what to decide first, how far to deepen, and what document holds the decisions. The Chinese-language practitioner register is the companion amendment; this entry is the Japanese-language one, quoted in Japanese
- sources: the three rows above. The two practitioner pages are tier C — a writing-app vendor blog and an editorial-service column, neither with a named author — so they are read as method evidence, reported as what they prescribe, and never as the sole support of a claim about the world; the monograph is tier B and supplies what a constructed world is, not how to build one
- couples: `culture-material/cartography-and-mapmaking.md` (the map that opens a settings note), `linguistics/naming-systems.md` (the name and place-name lists the note carries), `linguistics/conlang-scholarship.md` (how much language a world's function needs), `synthesis/coupling-model.md` (the parts a setting must relate), `synthesis/consistency-verification-checklist.md` (the verification side, whose verdicts lore owns), `synthesis/worldbible-integration-contract.md` (the handoff)
- scope: a reference method for the culture-material partition. It records how two practitioner pages order, fill and hold a setting, and what one scholarly source says a constructed world is; it decides no world's canon and rules on no real-world culture or reader
- refuses: canon for any world; any claim that either practitioner page is measured, tested or authoritative; a universal build order; reading the five-part or four-part schemes as a standard rather than two independent checklists; page counters and product claims as evidence

## §1 Calibration key — what each source can carry

| Framework | Status | Why it is placed there |
|---|---|---|
| LitMemo five-step order | not mainstream — an unmeasured vendor-blog convention | one vendor blog for a writing app, authored by the organisation, no named practitioner, no cohort and no citation; the page's own product calls to action sit beside the advice |
| tuduku five elements and settings note | not mainstream — an unmeasured editorial-service convention | an editorial-service marketing column of about 1,100 characters by its own count, no byline beyond the service name, checklists with one-clause glosses |
| four-layer chain 自然環境→社会の仕組み→文化→個人の経験 | not mainstream — one page's causal assertion, unmeasured | one page asserts the causality and offers no evidence; usable as a design heuristic, not as a finding about worlds |
| Sidorova & Shuvalova's framing of constructed worlds (2006) | not mainstream — a single monograph, one school; neither contested nor discredited here | a taxonomy of constructed languages with an account of fictional worlds; it prescribes no authoring order and reports rather than tests, and this entry opens no dispute with it |
| hard magic / soft magic split | not mainstream as reported; second-hand and uncited, (to-verify) | the page names ブランドン・サンダースン but cites no edition; treat the split as a lead until Sanderson's own essays are opened |

Status vocabulary, in QUALITY 2's terms: **not mainstream — unmeasured practitioner convention; nothing here is contested or discredited**. The two practitioner pages are conventions with no measured standing, the monograph is descriptive scholarship from one school, and no source opened for this entry disputes or discredits another.

Read every imperative below as "these two pages say", not as "this is how readers behave". Two independent pages agreeing on a step is corroboration of a convention, not evidence about an audience.

The LitMemo advice is also inseparable from the settings document its own product sells (S881).

The method rules below are reports of what these two pages prescribe; the entry's claims about worlds are confined to what the monograph states in this context — a language is the chief instrument of world-building, a constructed language is its world's subject rather than a means of talk, and a premise precedes the picture — so no tier-C page carries a claim alone about worlds.

## §2 What the scholarly source adds — a world is built around a premise

The monograph states that "Язык – главный инструмент построения вымышленных миров, дающий названия для их природных и социальных реалий" — language is the chief instrument for building fictional worlds, supplying the names of their natural and social realities (S877).

It records what such a language is for: "ВЯ в общем случае не служит средством коммуникации, он является предметом, темой коммуникации" — a constructed language is normally not a means of communication but its subject and topic (S877).

Design consequence: a world's language layer is sized to what the world must carry, not to a need for talk — the same volume rule `linguistics/conlang-scholarship.md` records.

The direction of construction is free: the book records that "связь между лингвоконструированием и моделированием миров неразрывна" — the link between language construction and world modelling is unbreakable — and that an author may run from world to language or from language to world (S877).

The same chapter states the rule the two practitioner guides open with: in science fiction the author offers "некое научное или не совсем научное допущение" and then builds around it the picture of the world that would follow if the premise held (S877).

That is the scholarly counterpart of the practitioners' first step, and it is the strongest single design rule in this entry: the first artefact is a one-sentence premise, and everything else is derived from it.

| Question | The scholarly source answers it | The practitioner pages answer it |
|---|---|---|
| what a constructed world is | a modelled world whose language names its realities | they assume it and start writing |
| why a world needs a language layer | it names the world's realities, and is the topic rather than a means of talk | which names a note must hold |
| where to start | a premise, then the world picture it implies | a premise, then the protagonist's living sphere |
| in what order to fill the parts | not addressed | five steps, five elements, five note sections |
| how to keep it consistent | not addressed | one document, updated in place |

## §3 What a setting is, and how much of one the work needs

The LitMemo page defines 世界観 as "物語が起きる世界の決まりごとの総体です" — the totality of the rules of the world in which the story happens — and distinguishes the written-out rules (世界観設定) from the collected document (設定資料 / 設定資料集) (S881).

It also refuses the fantasy-only reading: a contemporary novel needs no magic system and no political constitution, but it still needs the town, the workplace or school, and the invented company or district, decided once (S881).

How much to decide is therefore a function of how far the world stands from the real one; the page's own scale is the most transferable table on it (S881).

| Distance from the real world | What the page says is built | Amount to decide | The page's warning or instruction |
|---|---|---|---|
| complete other world | geography, history, species, all self-made | most | too many proper nouns at once; the reader cannot hold them |
| alternate history (IF) | the real record takes another path from one point | medium | research the record up to the divergence, then reason the change forward |
| real world plus a local lie | a few invented elements added to the real world | least | answer why the public never notices the secret |

Design consequence: fix the distance before the first map. The distance sets the size of the note, and choosing it late is how a short work acquires a three-month setting and no manuscript.

## §4 Build order — the five steps, and the two orders they allow

The five-step order as the page states it: "世界観の作り方は、①物語の核になるルールを決める ②主人公の生活圏から作る ③自然→社会→文化→個人の順に因果をつなぐ ④物語で使う分だけ掘り下げる ⑤一か所にまとめて書きながら更新する、の5ステップです。" (S881).

The same page caps the pre-writing work: "決めておくのは、展開に直接かかわる核の設定だけで十分です。" — only the core settings that bear on the plot need to be fixed before drafting (S881).

The tuduku column gives a five-step order of its own: the core concept in one sentence, the protagonist's day from waking to sleeping, deepening only the story-relevant parts, a contradiction check against past episodes, and a check against the reader's "why not just…" objection (S882).

Set beside each other, the two orders agree on the premise, the near field, the depth rule and the recording rule; they differ at the outward-causal step, which only the LitMemo page has, and at the last, where tuduku adds the objection check.

| Move | LitMemo's version | tuduku's version | What to do |
|---|---|---|---|
| 1 premise | 1–3 rules that change character choice, plus the work's temperature | the core concept in one sentence | write the premise and the temperature as two sentences |
| 2 near field | the protagonist's living sphere — town, daily route, organisations | the protagonist's day, wake to sleep | fill the ground the character actually walks |
| 3 outward cause | environment → society → culture → person, each layer a reason for the next | no separate step; its 歴史・背景 element asks why the present is as it is | use the layer chain; it is the difference between detail and design |
| 4 depth | only what the story's questions touch; blank fields are allowed | only the story-relevant parts, added as needed | leave the untouched regions blank and say so |
| 5 recording | one place, updated as the text changes | a settings note, cross-checked against past episodes, plus the reader's "why not just…" objection | keep one document and add the objection check |

The fork the page draws is real and worth deciding explicitly: starting from a scene or character, or starting from a world (S881).

| What you already have | How to proceed | What it suits |
|---|---|---|
| a scene or a character | fix the core rule, then add outward only the settings that scene needs | serialised web fiction, short and medium fiction, contest entries |
| a world | draw a coarse map, fix the protagonist's town and the surrounding powers, then add geography and history as needed | long fantasy, series, tabletop and game pitches |

Either way the page's own endpoint is the same — how a character lives in that world — which is the four-layer chain's last layer (S881).

## §5 The four-layer chain — cause outward, experience inward

The chain is stated as a causal sentence: "自然環境が社会の仕組みを決め、社会の仕組みが文化を生み、文化が登場人物の価値観を作る。" (S881).

Its own summary rule is "外側の層が内側の層を決める" — the outer layer decides the inner one (S881).

| Layer | What the page puts in it | Question the layer must answer |
|---|---|---|
| 自然環境 | geography, climate, creatures, resources | what does this place make possible, and what does it forbid? |
| 社会の仕組み | politics, economy, status, law — the checklist adds military and judgment | who decides, on what ground, and who pays? |
| 文化 | language, faith, habit, taboo | what is unthinkable here, and what is merely rude? |
| 個人の経験 | how a character feels this world | what does this character take for granted, and what does it cost them? |

The page's worked micro-chain: a sea-bound land grows shipping and trade, the town that prospered by trade gives merchants a strong voice, and in a town of strong merchants "約束を破る者" — the oath-breaker — is the most hated figure (S881).

That is the whole method in three clauses, and it is checkable: each clause is a reason for the next, and none of them is a fact about the world that the reader has to be told.

The page's four-row worked town makes the reader-visible payoff explicit: a fog-bound harbour, a lighthouse guild stronger than the crown's deputy, a taboo on lighting fires outdoors after dark, and a protagonist who has known since childhood that the fog-beast is the guild's story (S881).

Layer four is where the chain becomes usable: "読者は登場人物の目を通して世界を見ます。" — the reader sees the world through the character's eyes (S881).

The page draws the consequence sharply: a detailed political system that no character suffers under does not exist for the reader (S881).

Design consequence: write one line per layer and make each line answer "why is the inner thing like this?" A layer that cannot answer its outer layer is decoration, and detail that no layer explains is trivia.

## §6 The five elements, and the note that carries them

The tuduku page opens its list with five elements, and states the fifth in this full form: "勢力図・人間関係の構造：誰が権力を持ち、何が対立の軸になっているか" (S882).

| Element | What the page puts in it | Artefact it forces |
|---|---|---|
| 地理・環境 | terrain, how many states or regions, climate | a map, however rough |
| 歴史・背景 | why the present is as it is, what happened | a chronology with named turning points |
| 魔法・技術システム | what is possible and impossible; the constraints | a rules sheet with costs |
| 社会制度・文化 | status, religion, money economy, custom | an institutions list |
| 勢力図・人間関係の構造 | who holds power, what the conflict axis is | a faction and relation diagram |

The element with the strongest claim on the builder is the third, and the page says why: "特に重要なのは魔法・技術システムの「制約」です。" — the constraint is the important part (S882).

Its rule for what a constraint must contain is stated as an element gloss: "魔法・技術システム：何ができて何ができないか。ルール（制約）が重要" (S882).

| Settings-note section | What it holds | Why it is a separate sheet |
|---|---|---|
| 世界地図・地名一覧 | a drawn map plus the place names | the map is the cheapest consistency check there is |
| 年表・歴史 | dated events in sequence | chronology is the first thing to drift in a long work |
| 魔法・能力一覧 | each ability with its constraint and acquisition condition | powers inflate unless their ceiling is written down |
| 人物一覧 | name, age, appearance, temperament, role, relations | relations are the facts readers catch first |
| 社会制度・用語集 | invented trades, ranks, religions, currency units | one glossary prevents one object acquiring three names |

The note's opening section is glossed on the page with the loosest possible brief: "世界地図・地名一覧：手書きでよいので地図を描いておく" — a hand-drawn map is enough (S882).

The LitMemo page supplies the smallest record unit for a note entry: 種類 (place, organisation, item, species or rule), 説明, ルール (the fixed constraints that bind the plot), 関連 (what it belongs to and what it worships) (S881).

| Field | What it prevents |
|---|---|
| 種類 | a note that mixes a place with a rule, so neither can be searched |
| 説明 | an entry that cannot be recognised in the text two hundred pages later |
| ルール | a setting that is scenery instead of a constraint |
| 関連 | an entry that floats free of the polity and cult it belongs to |

Design consequence: the section list and the field set are two granularities — five sheets, and four fields inside every entry. Keeping only one gives either five folders of prose or tidy entries with nowhere to live.

## §7 Two sub-sheets a setting note needs

The LitMemo page gives an eight-field country sheet, and the eighth is the one easiest to overlook: the country's wound, the event the present population still carries (S881).

| Field | What to decide | Why it earns its place |
|---|---|---|
| name and etymology | who named it, and why | names date their coiners |
| position and terrain | coast, and what separates it from the neighbour | terrain prices every journey |
| polity | who decides | it fixes who can be bribed |
| relations with neighbours | alliance, enmity, dependency | it supplies the standing threat |
| industry and currency | what it earns with, what money circulates | it makes trade scenes possible |
| religion | a state cult or none, and the rite before departure | it puts ritual into ordinary action |
| language and names | the sound of the language; the page's example: two-syllable personal names, place names ending in 〜ラ | it makes the naming file consistent |
| the country's wound | the event still being lived down | it splits the generations' values |

The page explains why the last field is worth its row: it produces the generational value gap between those who remember the burning and those who do not (S881).

For a magic or technology system the same page gives seven questions, and the last two are the ones it calls the most often missed: the effect on society, and the relation to power (S881).

| Question | What it forces |
|---|---|
| source | where the power comes from — birth, training, contract, object |
| can and cannot | write the "cannot" list first |
| cost | what the user loses: stamina, lifespan, memory, sanity, standing, uses |
| who can use it | what fraction of people, and whether birth decides |
| stages and ceiling | how it rises, and what even the strongest cannot do |
| social effect | if healing exists, are there physicians; if flight exists, do walls mean anything |
| relation to power | reverence or fear, and whether an institution manages users |

The cost rule is the one that makes the rest usable: a power without a cost destroys the story's tension, because a protagonist who can always solve the problem has no predicament (S881).

The hard/soft distinction the page reports — hard magic with stated rules the reader can reason from, soft magic kept mysterious — is used here only as a scale of explicitness, not as a claim about Sanderson's text (S881).

The page's own worked power shows the whole mechanic-to-society chain in one paragraph: only the lighthouse-keepers' line can thin the fog, never dispel it; each use costs eyesight; the keepers are honoured and their children avoided in marriage (S881).

Design consequence: a power with no cost and no institution is scenery, and the cost row of the table above is the one a builder writes first.

## §8 Depth, genre and the failure list

The LitMemo page separates three depths, and only the first is written plainly in the text (S881).

| Depth | Content | Written in the text? |
|---|---|---|
| 核の設定 | the rules and facts the plot turns on | yes, plainly |
| 背景の設定 | the reasoning that supports the core | the author knows it; not all of it is written |
| 彩りの設定 | detail that adds flavour | touched occasionally, in scene |

The tuduku column calibrates the same axis by genre, which is the practical way to budget the work (S882).

| Genre | What to prioritise | Depth |
|---|---|---|
| 異世界ファンタジー | magic system, status order, geography | high — contradictions show |
| 現代恋愛 | characters' backgrounds, workplace, family | low — the real world carries it |
| SF / near future | technology, social change, terminology | high — readers check it |
| 歴史改変 | the divergence from the record, period setting | medium — the record underpins it |
| 学園もの | school system, class structure | low to medium |

The tuduku page's key-point box puts the split this way: "世界観設定は「作者が知っていること」と「読者に伝えること」を分けて考えましょう。" — what the author knows and what the reader is told are two different quantities (S882).

The tuduku page's failure table names four ways a setting damages a story: too much setting at the opening, too little so that contradictions appear, settings spoken aloud by characters as explanation, and settings that are built and never used (S882).

The LitMemo page lists four failures: three months of setting with no manuscript, an opening that explains too much, settings that contradict each other, and effort spent on material the story never reaches (S881).

| Failure | Symptom | Repair, in the sources' own advice |
|---|---|---|
| setting overload | an opening that explains the world before the story starts | show the setting inside a conflict |
| setting deficit | the rules change when the plot needs them | check the note before writing the scene |
| exposition dialogue | a character narrates the world to another character | give the line a purpose inside the scene |
| unused setting | a designed region or trade route never touched | cut it, or let it resonate somewhere |

The LitMemo page's own rewrite of an exposition line is the transferable move: it replaces the encyclopedia sentence about what a magic-user is called with the commander's threat at a woman's throat (S881).

## §9 Single-source discipline — one document, updated in place

The fifth step is stated as an operating rule: "決めた設定は一つの場所に集め、本文を書くたびに参照します。本文で設定を変えたら、その場で設定資料も書き換えます。" (S881).

For a shared project the page is stricter: "全員が同じ設定資料を一つだけ使い、それを正本にします。" — everyone uses one settings document and treats it as the authoritative copy (S881).

Its multi-author rule continues: whoever changes a setting writes the change back into that copy, and settings are not allowed to live in individual heads or private notes (S881).

For tabletop play it splits the document into a player-visible layer and a game-master-only layer, which is the same discipline with an access rule added (S881).

The drift the rule prevents is the page's own example: 金貨 in episode 3 becomes 金竜貨 in episode 20, because no table fixed the currency (S881).

| Rule | Applies to | What it prevents |
|---|---|---|
| one authoritative document | any work, one author or many | two versions of the same fact |
| write the change back the same day | serialised drafting | the note lagging the text |
| no setting facts in private notes | co-authored and tabletop work | a fact that exists for one person only |
| split public and hidden layers | tabletop, mystery plotting | the reveal spoiled by the shared sheet |
| one quick-reference sheet for units, calendar, titles, naming | long works | a coined term re-coined under pressure |

The per-series reading — one authoritative document spanning a whole series — is in this page's own body, in the まとめ方 section: "同じ世界でシリーズや複数の作品を書くなら、世界観設定を作品をまたいで共有できます。" It is stated as a capability of the page's product, in a paragraph listing what that product does, not as a rule for authoring, so it stays (to-verify) as a capability claim until a source prescribes it (S881).

Verification is not this entry's business: the checklist that owns conflict and variant statuses takes a note like this as its input and hands findings to lore.

## §10 Coupling and handoff

The chain couples outward to the map (`culture-material/cartography-and-mapmaking.md`) and to the name lists (`linguistics/naming-systems.md`), because the note's first two sections are exactly those artefacts.

It couples inward to the language layer (`linguistics/conlang-scholarship.md`): the atmosphere function of a world's language sets how deep the language file goes, not the other way round.

It couples sideways to the relation model (`synthesis/coupling-model.md`), which is where the four layers meet the systems the rest of the corpus owns.

Hand off under `synthesis/worldbible-integration-contract.md`: this entry supplies the order, the layers, the element and note schemas and the single-source discipline; lore decides which of them a given world adopts, records the canon, and verifies consistency.

Nothing here rules on any world. No layer assignment, no element count, no depth target and no document layout is fixed for a setting by this entry; the practitioner pages are reported as conventions, and a builder's own choice is the design decision.
