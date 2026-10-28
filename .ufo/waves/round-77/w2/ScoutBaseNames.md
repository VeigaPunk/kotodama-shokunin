# ScoutBaseNames — independent broad base ground sweep (round 77, wave 2)

Seat: `ScoutBaseNames` (falsifier, leaf). Assigned item: independent broad base
ground sweep of `corpus/knowledge` (all six partitions) at base
`B=211f9526800906e0c585d878d265c37e5e090c15`, attacking the negative ground in
`CLAIMS-DRAFT.md` claim C: *"at the base the corpus holds no Chinese-language
system-level account of personal naming — the 姓/名 structure (名 predates 姓;
姓+名 a contact-era acquisition) and the onomastics literature's finite lexeme
classification of Chinese female given names."* Themes tested: 姓/名 succession,
Chinese naming periodization, plant/flower lexemes in female Chinese names,
88/17 counts. W1 anchor read: `w1/stage/ScoutCoverageSweep/naming-systems.base.md`
(byte-identical to the base file; diff below), `w1/stage/ExecGapSweep/README.md`,
`w1/stage/ScoutPathsSearch/sections.md`.

Lane state at read time: `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin
rev-parse HEAD` → `211f9526800906e0c585d878d265c37e5e090c15` (== base);
`git status --porcelain -- corpus/` → empty (nothing under `corpus/` dirty or
untracked). Nothing in lane or fleet was written except this file. Scratch dir
`/fast/scratch/hyaku/kotodama-r77/ScoutBaseNames` was not needed (all reads via
`git -C … show/grep`); removed nothing. No installs (pacman paused; none needed).

## Verdict: NO counterexample found — claim C's negative ground stands at base

Every base match was inspected in context (`git grep -n -C`, `git show` section
reads), not just counted. The closest approaches are below; none is the claimed
content. One scope caveat that falsifiers of the frozen config MUST respect is
recorded in §5 (lessons hits outside the claimed bound, the r76 pattern).

## 1. File census (all six partitions; command and raw output)

```
$ git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin ls-tree -d 211f9526800906e0c585d878d265c37e5e090c15 corpus/knowledge/
040000 tree 2d031ce…	corpus/knowledge/civilizations
040000 tree 47a5cc2…	corpus/knowledge/culture-material
040000 tree 3348625…	corpus/knowledge/linguistics
040000 tree 4927b14…	corpus/knowledge/myth-symbol
040000 tree 32ae5f0…	corpus/knowledge/synthesis
040000 tree 70ef0cf…	corpus/knowledge/verification
```

```
civilizations: 95
culture-material: 41
linguistics: 32
myth-symbol: 32
synthesis: 29
verification: 24
=== total ===
253
```

(per-partition: `git ls-tree -r --name-only $B corpus/knowledge/<p> | wc -l`;
total `git ls-tree -r --name-only $B corpus/knowledge | wc -l` → 253, matching
the claim's "253→254".)

## 2. 姓 / 名 glyph sweeps — every hit inspected

```
$ git grep -l '姓' $B -- corpus/knowledge
B:corpus/knowledge/civilizations/china-shang-zhou.md
B:corpus/knowledge/civilizations/china-song.md
B:corpus/knowledge/civilizations/japan-yayoi-kofun.md
B:corpus/knowledge/civilizations/korea-joseon.md
```

```
$ git grep -l '名' $B -- corpus/knowledge
B:corpus/knowledge/civilizations/china-ming.md
B:corpus/knowledge/civilizations/china-song.md
B:corpus/knowledge/civilizations/japan-edo.md
B:corpus/knowledge/civilizations/korea-joseon.md
B:corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-24.md
B:corpus/knowledge/culture-material/funerary-material-culture.md
B:corpus/knowledge/culture-material/heritage-taxonomy-models.amend-2026-10-24-r13.md
B:corpus/knowledge/culture-material/heritage-taxonomy-models.md
B:corpus/knowledge/culture-material/warrior-material-culture.md
B:corpus/knowledge/culture-material/worldbuilding-setting-practice.md
B:corpus/knowledge/myth-symbol/narrative-structure-frameworks.md
```

Per-file 名 counts (`git grep -n '名' | awk -F: '{print $2}' | sort | uniq -c`):
1/2/1/1 in the four civilization files above, 4/2/3/2/1/2 in the culture-material
files, 1 in narrative-structure-frameworks.md — all in compound CJK terms
(元号, 标准名称, 戒名, 名物帳, 地名, 諡號), none a 姓/名 structure account.

Inspected contexts (`git grep -n -C4`):

- `china-shang-zhou.md:163-169` — the ONLY xìng 姓/shì 氏 line in the corpus is
  `…-167`: "Do not impose a later, fully regularized xìng 姓 / shì 氏
  distinction on every inscription; exact reconstruction of a named individual's
  affiliation remains (to-verify)." The section (lines 162-169) gives Fu Hao /
  Mother Xin stem-designation cautions and a "naming worksheet" (attested
  designation, speaker, living/dead, kin, title, affiliation). It warns
  AGAINST the very structural claim; it asserts no 名-before-姓 succession and
  no 姓+名 acquisition history. Not the claimed content. (Read via
  `git show $B:corpus/knowledge/civilizations/china-shang-zhou.md` lines
  162-169, 75-144.)
- `china-song.md:172-183` — slot table `Surname and personal name, 姓 / 名`:
  "Surname normally precedes the personal name in Chinese order" plus 字/號/
  office/imperial-name slots; bullets: name avoidance affects transmission,
  generation characters "a possible lineage device." ORDER AND SLOTS ONLY —
  no historical structure, no predation, no inventory. Read at `…:172-200`.
- `china-ming.md:176-182` — "Distinguish family surname, personal name ming 名,
  courtesy name zi 字, sobriquet hao 號, office title, kinship address, and
  nickname"; women under "surname plus shi 氏"; generation characters/taboo
  `(to-verify)`. Slot inventory, no structure history. Read at `…:176-200`.
- `china-han.md:142-153` — "Namespace" table: `Family + personal name`
  (董｜仲舒, 公孫｜弘; "Compound surnames and multi-character personal names
  both occur"), courtesy names, posthumous designation, era title. Slot
  inventory for ONE dynasty slice; `…:169` names "ordinary women's naming" as
  thin coverage. No 姓/名 historical structure, no 單名/雙名 shift.
- `china-tang.md:152-162` — same shape: family-name-precedes-personal-name,
  compound surnames (Shangguan Wan'er), zi, office/place, imperial identifiers,
  bihui; `…:159` women's/non-elite names as archive caution.
- `china-qing.md:135-143` — Manchu hala/gebu vs Han slots; imperial-name stack;
  "name worksheet." No Chinese name-history.
- `japan-yayoi-kofun.md:156-161` — uji 氏/kabane 姓 is JAPANESE system; `…:161`
  warns against backdating one codified system. Non-Chinese, non-succession.
- `japan-edo.md:188` — kaimyō 戒名 mortuary names. Non-Chinese.
- `korea-joseon.md:139-146` — seong 성 姓/bon-gwan, hangnyeolja, pihwi: Korean
  system including the note that low-status records carry "a bare name with no
  surname" and kings chose rare single-character names to lighten taboo. This
  is a Korean naming structure note, not a Chinese 姓/名 succession account.
- `korea-three-kingdoms-goryeo.md:171-175` — Korean: don't assume the modern
  surname+two-syllable pattern; Silla Kim/Bak/Seok, Wang Geon≠Taejo.
- `vietnam.md:150-159` — Vietnamese naming layers incl. gendered middle-name
  patterns (Văn/Thị), the 1841 Hoa taboo. Vietnamese, not Chinese.

## 3. Periodization / succession theme — no hits

```
$ git grep -n '單名\|雙名\|单名\|双名' $B -- corpus/knowledge    → exit 1, no output
$ git grep -n '魏斌\|漢晉\|汉晋' $B -- corpus/knowledge           → exit 1, no output
$ git grep -n -i 'kaluz\|onomastic' $B -- corpus/knowledge
```

→ 17 hits in 15 files; ALL generic "onomastic(s)" or non-Chinese onomastics:
amazonia (Tupi-Guarani, thin), anatolia-hittite (theophoric), balts (Dini),
burma (not an onomastic work), finnic-sami (substrate test), fon-dahomey,
persia-sasanian (-dukht compounds, Gignoux corpora), rome (Salway JRS 84),
slavs-early (-slav-), swahili-coast (Taji), yoruba, funerary-material-culture
(:147, :199 — "a second onomastic system" for the dead), language-contact (file
seed), naming-systems.md:40 (four name systems), naming-collision-gate (:4
Hough handbook, :141), naming-canon-workflow (:27-30 Nyström/Ainiala/Sandnes in
Hough 2016), migration-founder-effects (:199 Beider Jewish onomastics),
deity-name-derivation-pipeline (:26 typed onomastic network),
loanword-material-dating (:32), contact-scenario-builder (:186),
costume-language-coupling-table (:18 Salway), religion-language-co-evolution
(:203 Schimmel, Islamic names). ZERO hits for Kałużyńska, the Onomastica
journal, lishisuo.cssn.cn, or Chinese anthroponymy literature. (confirms claim's
W1 sweep shape; I reproduced it as
`git grep -l -E 'lishisuo\.cssn\.cn|onomastica\.ijppan' $B -- corpus/knowledge`
→ exit 1, no output — but see §5 for the wider-tree caveat.)

Loose-phrase succession sweep (English paraphrases of "名 predates 姓 / 姓+名 a
contact-era acquisition"):

```
$ git grep -n -i 'predate\|earlier.than.\{0,30\}surname\|before.\{0,20\}surname\|contact.era\|name.\{0,20\}acquisition\|first.surname\|surname.\{0,20\}introduc\|adopted.surname' $B -- corpus/knowledge
```

→ ~60 hits, all inspected: none is a Chinese name-structure claim. The only
name-adjacent ones: amazonia (:183 Tupi-Guarani name-acquisition gap),
arabia-pre-islamic (:86 the NAME Allāh predates Islam), turkic-steppe (:74/:129/:185
qağan title predates imperial use — title, not surname), japan-medieval-sengoku
(:153 older place names), agrarian-field-system-lexicon (:103 "contact-era
referents" about loanwords), death-afterlife-eschatology (:152,:159 invented
contact-era rites). No "surname introduced/adopted" Chinese claim anywhere.

## 4. Plant/flower lexemes in female Chinese names — no hits

```
$ git grep -n -i 'orchid\|peony\|lotus\|jasmine\|plum.blossom\|chrysanthemum\|蘭\|兰\|梅\|菊\|花\|牡丹\|蓮\|莲\|桂花\|蘭花\|玉蘭' $B -- corpus/knowledge
$ git grep -n -i 'female nam\|women.\{0,20\}nam\|nam.\{0,20\}women\|feminine nam\|girl.\{0,10\}nam' $B -- corpus/knowledge
$ git grep -n '名.*[花樹木草蘭]\|[花樹木草蘭].*名' $B -- corpus/knowledge     → exit 1, no output
$ git grep -n '名.*[種類]\|[種類].*名' $B -- corpus/knowledge               → exit 1, no output
```

Plant-lexeme hits are landscape/costume/ritual items (Tao "Orchid Island",
Burmese lotus throne, Tang lotus iconography, shōchikubai, maebyeong 梅甁 vessel
type, siheyuan 垂花门 gate, kaō 花押 signature, Man'yōshū plum preface, 金莲记
title). ZERO plant/flower lexemes as female Chinese given-name material.

Female-name hits are all archive-bias cautions or non-Chinese classifications:
aksum-ethiopia (patronymic also for women), amazigh-berber (women select the
name), celts (:157,:190 female naming practice "thin"), china-han :169 /
china-song :14 / china-tang :159 (women's naming = documented-as-thin),
etruria, hopi, india-classical-sanskrit (:159 Manu 2.31-33 auspicious feminine
names — Sanskrit, prescriptive, not a counted lexeme inventory), japan-edo,
japan-medieval-sengoku, korea-joseon :144, persia-sasanian :186 (-dukht
compounds; "dedicated onomastic corpora" named but Gignoux, not Kałużyńska),
rome :129, migration-founder-effects, naming-canon-workflow (:8,:128 LGPN I
statistics 60,249 men / 5,700 women — Greek database census, not a Chinese
female-name classification). NO Chinese female-name lexeme inventory exists at
base.

Closest generic statement (inspected): `myth-symbol/plant-symbolism.md:132` —
"Plant names are also the commonest source of *personal* names and toponyms
(`naming-systems.md`): a culture with plant-name lineages has built its flora
register into its onomastics." Language-agnostic worldbuilding advice, not a
Chinese-language classification and no counts. `animal-symbolism.md:115` names
Chinese birth-year talk as a "performative species" hook — not an inventory.

## 5. 88 / 17 counts — no hits; lessons-scope caveat

```
$ git grep -n -i '88 terms\|altogether 88\|eighty-eight\|17 terms\|17 categor\|17 subcategor\|seventeen' $B -- corpus/knowledge
$ git grep -n '\b88\b\|\b17\b' $B -- corpus/knowledge
$ git grep -n '八十八\|十七\|八八\|十七種\|類別\|類型' $B -- corpus/knowledge  → exit 1, no output
```

The only `17`-adjacent hits are "seventeenth century" era spans and "Lesson 17"
teaching URLs; no "88 terms", no "17 categories/subcategories", no 八十八/十七種.
No counted inventory of anything name-related exists.

SCOPE CAVEAT (the r76 lesson pattern, must not be repeated): running the same
patterns over the whole `corpus/` tree instead of `corpus/knowledge` exits 0:

```
$ git grep -l '魏斌\|Kałużyńska\|單名\|雙名\|88 terms\|onomastica.ijppan\|lishisuo.cssn' $B -- corpus/
B:corpus/lessons/round-68.md
B:corpus/lessons/round-72.md
```

- `corpus/lessons/round-68.md:111` — quarantine verdict names "S820
  (onomastica.ijppan.pl PDF, pdftotext hit)" — a CAMPAIGN-id mention, not a
  knowledge entry.
- `corpus/lessons/round-72.md:110` — names staged S934's Kałużyńska-capture
  misdescription and staged S936 — a fabrication-class warning, not corpus
  knowledge.

Consequence: the frozen `sweeps[].scope` for GROUND must stay `corpus/knowledge`
(or `corpus/knowledge corpus/SOURCES.md`), exactly as the draft states ("negative
sweep scope = corpus/knowledge only"). If any frozen sweep widens to `corpus`
or repo-root, it exits 0 at base on lesson mentions and GROUND fails
"already present at base" — the exact r76 defect class. The counter's
`leg_ground` (`w1/stage/ExecAdaptC/accept-c.py:2186-2206`) runs
`_grep_tree(mat_base, sweep["scope"], sweep["pattern"])` over the declared scope
with no lessons exemption. Verified by reading the counter.

## 6. naming-systems.md base scope — verified identical to W1 capture

```
$ git show $B:corpus/knowledge/linguistics/naming-systems.md | wc -l   → 136
$ diff <(git show $B:corpus/knowledge/linguistics/naming-systems.md) \
       .ufo/waves/round-77/w1/stage/ScoutCoverageSweep/naming-systems.base.md
  (empty; DIFF-IDENTICAL)
```

Structure (headings): §1 four name systems; §2 anthroponymy slot system;
§3 toponymy; §4 theonymy; §5 endonym/exonym; §6 name taboo/magic; §7 derivation
pipeline; §8 calibration; §9 canon boundary. Chinese content: `:54` the slot row
("surname first + given + generation-pool character; hereditary surname
~ancient"), `:94-97` the bìhuì taboo table (incl. Korea row), `:22-23` Wilkinson
2018 + Shiji taboo citations, `:71` pinyin/UNGEGN, `:84` route layering,
`:122` worked micro-example. Claim's characterization is exact: "covers Chinese
taboo, name slots/order and generation pools, not the historical structure or
finite lexeme-count classification." No 名-predates-姓 line, no 單名/雙名, no
female-name inventory, no Kałużyńska citation anywhere in the file.

## 7. Adjacent checks (completeness of the four themes)

- `linguistics/kinship-terminology.md:84` — tang 堂/biao 表 marriageability by
  surname/lineage: kin-term morphology, not naming history.
- `synthesis/symbol-lexicon-colexification.md:14` — names Watson (1986) "The
  Named and the Nameless: Gender and Person in Chinese Society" as a "dated
  anchor for the general structure" alongside naming-systems.md §6. A gendered
  name-USE anchor (Hong Kong New Territories), not the 姓/名 historical
  structure or a lexeme classification; item-level permissions explicitly left
  `(to-verify)`.
- `synthesis/taboo-euphemism-lifecycle.md:125-141` §8 — "imperial Chinese name
  avoidance" capsule: separation of surname/personal/reign/temple/posthumous
  for the taboo rule; no structure history.
- `synthesis/era-language-staging.md:111-119` — regnal-name typology
  (birth/throne/titulary), Egyptian-anchored; not Chinese personal naming.
- `verification/naming-collision-gate.md` — generic gate; grep for
  china/chinese/姓/名/female/women inside it → 0 hits.
- `synthesis/naming-canon-workflow.md` — Hough-2016 onomastics method rows +
  LGPN stats; no China section.
- `culture-material/era-periodization-models.md` — era-name (nianhao)
  periodization, which is the "periodization" a *cultural* file owns; it is not
  personal-name periodization and does not satisfy the ground by any reading.
- `culture-material/politeness-taboo-euphemism.md:75` — bìhuì restated
  (taboo domain), thin-documented caveat.
- `sogdian-silk-road.md:167` — Chinese-form names (Kang/An) are
  `(to-verify)` leads for Sogdians, explicitly not a naming generator.
- `austronesia-philippines-taiwan.md:190`, `ryukyu.md:168-171`,
  `turkic-steppe.md:162` — Chinese-looking names in neighbors, treated as
  transcription pitfalls.

## 8. What WOULD have been a counterexample (and was not found)

Any base knowledge file carrying (a) a 姓-vs-名 historical/structural account —
e.g., "名 predates 姓", xìng/shì distinction treated as *history* rather than a
reconstruction hazard, or Han–Jin 單名→雙名 shift — or (b) a counted/classified
inventory of Chinese female given-name lexemes (Kałużyńska's 88 terms / 17
subcategories, or any Chinese source). Neither exists; the four China files are
slot-and-order tables per dynasty slice, the two Sinosphere neighbors' files
are non-Chinese, and the only xìng/shì line warns against asserting the
distinction at all. The lessons-only Kałużyńska mention is a quarantine warning
about a misdescribed staged row — evidence AGAINST treating it as held ground,
not a counterexample.

## Commands run (audit list, all in lane repo, read-only)

1. `git -C $L ls-tree -d $B corpus/` and `corpus/knowledge/`
2. per-partition + total `git ls-tree -r --name-only $B corpus/knowledge… | wc -l`
3. `git grep -l '姓' / '名' $B -- corpus/knowledge`; `-n -C4` context greps
4. `git grep -n '名' $B … | awk -F: '{print $2}' | sort | uniq -c`
5. `git grep -n '單名\|雙名\|单名\|双名' / '魏斌\|漢晉\|汉晋' $B -- corpus/knowledge`
6. `git grep -n -i 'kaluz\|onomastic' $B -- corpus/knowledge`
7. `git grep -l -E 'lishisuo\.cssn\.cn|onomastica\.ijppan' $B -- corpus/knowledge`
8. `git grep -n -i 'surname' / 'given.name\|personal.name\|forename' $B … | awk/uniq -c` (census)
9. `git ls-tree -r --name-only $B corpus/knowledge | grep -i 'nam'`
10. `git grep -n -i 'chinese.\{0,80\}nam\|nam.\{0,80\}chinese' $B -- corpus/knowledge`
11. `git grep -n '名字\|姓名\|氏' / '輩行\|辈行\|字輩\|字辈\|generation.*' $B -- corpus/knowledge`
12. `git grep -n -i 'single.character nam\|double nam\|two.character nam\|one.character nam\|monosyllabic nam\|disyllabic nam\|single nam\|two syllable nam\|one.syllable nam' $B …`
13. `git grep -n -i 'female nam\|women.\{0,20\}nam\|nam.\{0,20\}women\|feminine nam\|girl.\{0,10\}nam' $B …`
14. `git grep -n -i 'orchid\|peony\|lotus\|jasmine\|plum.blossom\|chrysanthemum\|蘭\|兰\|梅\|菊\|花\|牡丹\|蓮\|莲\|桂花\|蘭花\|玉蘭' $B …`
15. `git grep -n -i '88 terms\|altogether 88\|eighty-eight\|17 terms\|17 categor\|17 subcategor\|seventeen' / '\b88\b\|\b17\b' / '八十八\|十七\|八八\|十七種\|類別\|類型' $B …`
16. `git grep -n '諱\|讳\|避' / '名.*[種類花樹木草蘭]…' $B …`
17. `git grep -n -i 'predate\|earlier.than.\{0,30\}surname\|before.\{0,20\}surname\|contact.era\|name.\{0,20\}acquisition\|first.surname\|surname.\{0,20\}introduc\|adopted.surname' $B …`
18. `git grep -l '魏斌\|Kałużyńska\|單名\|雙名\|88 terms\|onomastica.ijppan\|lishisuo.cssn' $B -- corpus/` (scope-boundary check)
19. `git grep -n 'onomastica.ijppan\|Kałużyńska' $B -- corpus/lessons/round-68.md corpus/lessons/round-72.md`
20. `git show $B:corpus/knowledge/linguistics/naming-systems.md` (+ `wc -l`,
    `grep -n '^#'`, `grep -n -i 'china\|chinese\|姓\|名\|han \|han-\|dynast'`)
21. `diff <(git show $B:…/naming-systems.md) w1/stage/ScoutCoverageSweep/naming-systems.base.md` → identical
22. `git show` section reads: china-shang-zhou (75-169), china-han (99-172),
    china-tang (151-162), china-song (170-200), china-ming (176-200),
    china-qing (135-143), vietnam (150-162), plant-symbolism (125-140),
    symbol-lexicon-colexification (8-20), taboo-euphemism-lifecycle (123-150),
    era-language-staging (111-119), naming-collision-gate (all CJK grep → 0),
    korea-joseon (138-146), korea-three-kingdoms-goryeo (95-175),
    siam-thai/islamic-caliphate/migration-founder-effects (name lines)
23. `git rev-parse HEAD`; `git status --porcelain -- corpus/`
24. `read` of `w1/stage/ExecAdaptC/accept-c.py:2185-2244` (leg_ground) and
    `w1/stage/ExecAdaptC/diff-summary.md` (leg table, "sweeps absent at base
    unconditionally") — to confirm the graded scope behavior cited in §5.

## Remaining unknowns / handoff notes

- The counter's GROUND leg also requires each frozen sweep PRESENT in the
  admitted entry (`…/accept-c.py:2196-2206`) — out of this seat's scope; if a
  frozen sweep pattern uses a spelling the admitted file doesn't carry, that is
  a different defect. Not evaluated here.
- If the freeze widens any sweep `scope` beyond `corpus/knowledge` (incl.
  `corpus/lessons`, `corpus/SOURCES.md` only, or repo-root), §5's lesson hits
  make the before-side FALSE — flag for RevCounterC/CritGround.
- `corpus/SOURCES.md` was not re-swept for D1/D2 URLs (W1's `ScoutIdMap`
  covered staged-id→registry mapping; the draft asserts no base registry
  document match — that is a document-identity question outside my assigned
  glyph/theme sweep).

Report: `.ufo/waves/round-77/w2/ScoutBaseNames.md`
