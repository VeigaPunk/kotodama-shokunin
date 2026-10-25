# SimplifierRows — the minimal honest row set for claim C (minimality attack)

Seat: SimplifierRows · round 74 / hyaku 7 · wave 1 · 2026-10-25
Lane base `f7104cbce186bc2e1522abf0cfd619cc834628bb`. Leaf seat: no subagents, no background jobs, no writes outside this file.
`reports/round-74/claims.json` was read and **not** edited. Nothing under `corpus/`, `reports/`, `.ufo/state`, the fleet root or
`/home/vgpnk/Projects/shokuknow` was written; the lane's git index and jj/git state were not touched (all git use was `git show`
against the base revision).

## 0 Verdict, in one paragraph

The minimal honest row set is **the declared one, unchanged**: four appended rows S881 (litmemo), S882 (tuduku), S883
(chinawriter 2025-06-05), S884 (chinawriter 2022-12-07), plus the **reused** row S877 (the МГУ PDF), with zero additions and
zero deletions. No row is droppable without either (a) deleting whole sections of a drafted entry, or (b) making an already-frozen
leg false; and no row is single-sentence — the thinnest is S877 at 6 cites, then S882 at 9. The surplus the simplifier does find is
**inside the row payloads and in two entry sentences**, not in the row count: three cuts (K1–K3), one prohibition (do not widen S877's
scope cell, K4), two "do not add" rulings (K5–K6), and four anchor cells that are still rehearsal-only and must be replaced before any row can pass ROWS/GATE (§4).

## 1 What I read, and what I ran

Read: `reports/round-74/claims.json` (all 126 lines); the two drafts `drafts/worldbuilding-setting-practice.md` (265 lines) and
`drafts/worldbuilding-setting-practice.amend-2026-10-23.md`; the two staged entries and `SOURCES.append.md` rows S880–S900 under
`/home/vgpnk/Projects/shokuknow/merge/kotodama/` (read-only); the scratch-mirror rows and receipts under
`.ufo/waves/round-74/assimilation/` (`validate/corpus/SOURCES.md`, `validate-notes.md`, `validate-receipt-draft.txt`,
`id-map-draft.json`); wave-1 seat reports ScoutLitmemo / ScoutTuduku / ScoutChinawriter2025 / ScoutChinawriter2022 / ScribeEntryBase;
the base registry and base knowledge tree; the round-73 counter `reports/round-73/accept-c.py` for the implementation of ROWS and
REPOINTED; `scripts/sources-census.sh` for the E/W code table.

Exercised (results in §7): id census over both drafts; `tools/check-cited-lines.py` on both drafts; a host scan over **all 21** lane
registries; re-derivation of claim C's `before` legs at the base commit; `git cat-file -e` on all six coupled paths; word counts.

**Not** exercised: no live fetch of any URL (every page fact below is a wave-1 scout's, whose User-Agent and byte counts are recorded
in those reports; this seat fetched nothing and names nothing as fetched); no run of the round-74 counter (it does not exist yet —
`reports/round-74/` holds only `claims.json` and `telemetry/`); no census run by me (the mirror receipt is ExecScratchMirror's and is
cited as theirs); no commit, no entry landing, no acceptance.

## 2 Keep/cut, per row

Counts are cites in the draft (`grep -noE 'S(877|881|882|883|884)'`); "sections" are the draft sections that would have to be deleted
with the row. Two conventions in the last column: **ROWS goes false for every cut** (its text is "the registry diff base..<lands> adds
*exactly* S881..S884 (contiguous)"); **REPOINTED goes false only if a cite survives the cut** (it checks that every `source:` line and
inline id resolves to an adopted row) — so an honest cut must delete the sentences, never re-point them to a bare URL (§5, last
paragraph).

| row | staged | document | cites | where | verdict | if cut: sections lost | legs that go false |
|---|---|---|---|---|---|---|---|
| S881 | S883 | litmemo.com/ja/blog/novel-worldbuilding-guide | 31 | base draft lines 4, 28, 56–60, 72–74, 88–118, 148–198, 220–241, 251 (§§1,3,4,5,7,8,9) | **KEEP** | §3 definition/distance, §4 five-step order + fork, §5 four-layer chain (all of it), §7 both sub-sheets, §8 depth + failure list, §9 single-source | ROWS always; REPOINTED if any of the 31 cites survives |
| S882 | S884 | tuduku.space/column/novel-worldbuilding | 9 | base draft lines 5, 76, 124, 134–136, 146, 206–218 (§§1,4,6,8) | **KEEP** | §6 five elements + the settings-note section table, §4's comparison column, §8's genre budget + key-point + failure table | ROWS always; REPOINTED if any of the 9 cites survives |
| S883 | S899 | chinawriter.com.cn/n1/2025/0605/c404024-40494534.html | 20 | amend lines 3, 21–33, 38–45, 63 (§§1,2,3,5) | **KEEP** | §2 build order (its first three bullets), §3 the whole derivation rule, §5's first gate table, §1's headline/body bullet | **GATE** — the leg names this row by id: "S883/S884 rows state the re-quote"; ROWS always; REPOINTED if any of the 20 cites survives |
| S884 | S900 | chinawriter.com.cn/n1/2022/1207/c404024-32582252.html | 16 | amend lines 4, 23, 34, 51–59, 71, 85 (§§1,2,4,5,6) | **KEEP** | §4 the whole delivery schedule (9 bullets), §5's second table, §6's tier-C sentence, §1's 李玮 bullets | **GATE** (same clause); ROWS always; REPOINTED if any of the 16 cites survives |
| S877 | S882 | philol.msu.ru/~sidorova/files/conlangs.pdf | 6 | base draft lines 3, 34–42 (§§1,2) | **KEEP, reuse** (in-place `used-by` only) | §2 entirely — the entry's only tier-B support and the premise rule | ROWS (the leg, and the after-state sentence, name the S877 used-by edit; with no reuse there is no in-place change at all); REPOINTED only if a cite survives. See §3 for why a fifth row is worse |

### S881 (litmemo) — no cut
It is not "one section's row": it carries the entry's spine (§3–§5), the two sub-sheet tables (§7), the failure list and its worked
rewrite (§8), and the operating rule of §9. The only sentences it does *not* touch are §2 (S877) and §6's first table (S882). A cut
would leave a 4,194-word entry with the monograph summary and a component list. QUALITY 15 does not bind here (row-set-neutral, §7),
so the case rests on content + ROWS + REPOINTED — both of which flip.

### S882 (tuduku) — no cut, and the best of the four *if the round wanted a cut*
It is the only source of "five elements", the settings-note section table, the genre budget and tuduku's own failure list — i.e. the
"components" half of the base entry's declared topic ("five elements a setting must supply, the five sections and four fields of the
settings note"). Cutting it would not free a row cheaply: it would force the base entry's `sources:` sentence ("the three rows above.
The two practitioner pages are tier C"), the topic line, the §1 calibration row, §4's comparison and the amend's gap-fill sentence
("the entry this amends records … the settings-note tables that carry it") to be rewritten — and the amend's statement would become
false. Net: one row saved, two entries' headers rewritten, half a method table lost. Not a simplification.

### S883 / S884 (the two chinawriter interviews) — no cut; the GATE leg forbids it by name
The GATE leg is written as "… S883/S884 rows state the re-quote …" — it names both **rows**, not the documents. With the claim as
drafted, dropping either makes that clause unsatisfiable at `<lands>` → `any leg false at <lands> -> the claim fails as declared`.
The two rows also carry different content, so neither is the other's spare: S883 is the build order and the derivation rule
(premise → inference → material form → laws → mechanics), S884 is the delivery schedule (hook first, released gradually, inside
roughly twenty chapters). §2's last bullet, where S884 corroborates the order, is the only true overlap — and it costs no row.

## 3 The two keeps that need an argument

**(a) S877 is reused, not re-appended — this is the anti-duplication measure, not a shortcut.**
The PDF is already lane row S877 at base (`corpus/SOURCES.md:832`, inside a registry of 804 rows: title, ISBN, full-text URL, Wayback
mirror, tier B, `used-by corpus/knowledge/linguistics/conlang-scholarship.md`). The base draft's source line cites that exact URL.
Appending the staged S882 document as a *fifth* row would put the same URL in a second row of the same lane: census
`validate` reports **E04 duplicate URL+scope (no supersedes)** → the CENSUS leg (exit 0, no E-codes) goes false, and ROWS
("adds exactly S881..S884") goes false anyway. Reuse costs exactly one in-place cell edit, which the registry preamble allows
("only `status`, `recheck` and `used-by` change in place"): old `corpus/knowledge/linguistics/conlang-scholarship.md` → new
`corpus/knowledge/linguistics/conlang-scholarship.md, corpus/knowledge/culture-material/worldbuilding-setting-practice.md`
(the mirror's §2 states the same old/new). Two things make the reuse honest rather than convenient: the entry quotes the *whole
book* (its source line says so), and the row's `scope` already covers the classification framing it quotes — so no scope edit is
owed (§4 K4).

**(b) S884 is the one keep that rests on a reading of QUALITY 1.**
§4 of the amendment (delivery schedule, 9 bullets) has S884 as its **sole** support, and S884 is tier C. QUALITY 1 says a tier-C row
is "a lead, never sole support for an admitted claim". The row survives because (i) the entry's calibration is `contested` and §4
quotes the author's hedges (`大概`, `我觉得是问题不大的`) while §6 says outright "The delivery schedule rests on one tier-C row, so it
is recorded as a lead"; (ii) GATE names the row, so its removal is a pre-data claim change, not a landing decision; (iii) the
alternative removes half the amendment. **If a reviewer rules that tier C cannot support §4 at all**, the honest move is a
`pre_data_correction` deleting S884 *and* §4 (and the after-state sentence "the two entries on uncovered ground" survives, since the
amend would then be build-order-only) — not a silent keep. I record this as the one place where the row set is a judgement, and the
judgement is "keep, with the lead framing load-bearing".

## 4 Cuts that do **not** change the row count (the real minimality findings)

- **K1 — cut the per-series sentence.** `drafts/worldbuilding-setting-practice.md:251`: "The per-series reading — one authoritative
  document for a whole series — is the linked article's promise … (to-verify) (S881)." It is the **only** sentence in either draft
  that attributes substance to a document with no row: ScoutLitmemo §3 found the phrase 信頼できる唯一の情報源 only inside a
  related-article card for a *different* URL, whose slug is not in the served HTML, and did not fetch it ([UNRESOLVED]). The
  `(to-verify)` marker makes it QUALITY-1-legal, but it carries no decision that §9's FAQ/shared-project rule does not already
  carry. Cut it; keep the proveable half ("only one document for the shared project is stated here"). If kept, the round owes a
  fifth row for that article → ROWS false.
- **K2 — cut the id `S729` out of the new row's `teaches` cell.** The mirror row `S881` (`.ufo/waves/round-74/assimilation/
  validate/corpus/SOURCES.md:836`) says "… the Japanese counterpart to the Chinese practitioner vocabulary of round 1's S729". In
  the lane, **S729 is Neer et al. 2025, infant-directed speech** (base registry, unrelated document); "round 1's S729" is a campaign
  id, and in-campaign it meant the 世界观/设定 vocabulary of the staged entry's ground line. A new lane row may not carry an id that
  names an unrelated lane document — REPOINTED's clause ("an id naming an unrelated lane document") and QUALITY 15's table shape
  (a table row carries no id) point the same way. Rewrite without the id. Note the checker cannot catch this: `check-cited-lines.py`
  prints 907 findings on `SOURCES.md` (pre-existing rows), i.e. the registry is outside its scope — which is why the fix is by hand.
- **K3 — rewrite one clause in the base draft's `gap filled:`.** `:9`: "The Chinese-language practitioner register is the companion
  amendment". At base the registry holds **0** rows containing 世界观 / 世界観 / 设定 / 設定, so there is no Chinese *register* in the
  corpus for the amendment to be; the amendment is one author's recorded practice. Name that instead ("the companion amendment records
  one Chinese author's build order and delivery schedule"). No row impact either way; it removes a cross-reference a reader cannot
  verify from any row.
- **K4 — do not widen S877's `scope` cell** (ScribeEntryBase F11 offers "widen the `scope` cell or accept the quotes as inside the
  book's own framing"). The append-only rule allows in-place change only in `status`/`recheck`/`used-by`; ROWS is written as "the only
  in-place registry change is S877's used-by cell"; and the alternative remedy — a superseding row for the same PDF — adds a fifth id
  (S885), breaking ROWS' "exactly S881..S884 (contiguous)" and the frozen map. Accept the quotes as in scope: the cited URL is already
  in the row, and the row's scope names "the book's own framing … the classification of artificial languages". **Prohibition, not a cut.**
- **K5 — do not add Wayback mirror URLs to the four new source cells** (optional, not needed). ROWS checks *membership* of the map
  URL in the source cell (round-73 `accept-c.py:640-643`, `norm_url(...) in neutral_url_keys(urls_in(cells[2]))`); GATE and EVIDENCE
  require a **live** fetch with the browser-shaped UA and a body sha256. Adding a capture URL is leg-safe (REPOINTED only checks
  entry URLs ⊆ row URLs, `accept-c.py:704-710`) and S877 shows the precedent — but it buys nothing this round and the scout reports
  already carry the captures (`20250610015519id_`, `20221207080111id_`) where they matter.
- **K6 — do not merge the two entries.** One entry citing all five rows would have the identical row set (and one `used-by` path in
  five cells instead of two): zero row savings, and it breaks the lane's amendment convention (`heritage-taxonomy-models.amend-*`,
  `calendar-festival-systems.amend-*`, …). Minimality does not touch entry count.
- **K7 — the four anchor cells in the mirror are rehearsal-only and must be replaced.** They still carry the *staged* locator strings
  (`the 「非凡特性来自最初造物主」 answer …`, `the 「这个我肯定考虑过…」 answer …`), which is exactly the R68/R71 pattern the claim was
  written to avoid. Until they are replaced, ROWS' "the evidence quote inside the anchor cell" and GATE are false for **all four**
  rows — a payload fix, not a row cut. The four page-located candidates with counts, from the scouts (`wc -w` / `wc -m`; CJK is one
  whitespace token):
  | row | candidate quote | location | w/c |
  |---|---|---|---|
  | S881 | 自然環境が社会の仕組みを決め、社会の仕組みが文化を生み、文化が登場人物の価値観を作る。 | h2 世界観の4つの層 / step-3 sentence (ScoutLitmemo §3) | 1 / 43 |
  | S882 | 勢力図・人間関係の構造：誰が権力を持ち、何が対立の軸になっているか | info-box 世界観設定の5要素, item 5, raw line 150 (ScoutTuduku §4 Q1) | 1 / 33 |
  | S883 | 整个过程里，我先做的是世界观，再考虑怎么升级，再考虑升级的表现。 | P68, sub-heading 确定风格、设定世界、推导故事 (ScoutChinawriter2025 §3) | 1 / 32 |
  | S884 | 把它放在前面大概20章之内慢慢来，我觉得是问题不大的。 | para 35, final sentence tail (ScoutChinawriter2022 §3 Q1) | 1 / 27 |
  Use the **same** quote in the Gate record, the row's anchor cell and the stored evidence window — EVIDENCE is written as "the
  counter checks the Gate quote occurs inside that stored window", so two different quotes per row would have to be stored twice.

## 5 The opposite test — is any cited-in-entry source missing a row?

No, after the cuts above. Evidence:

- Both drafts cite only lane ids: base draft `S877 ×6, S881 ×31, S882 ×9`; amend `S883 ×20, S884 ×16`. No other `S[0-9]{3,4}` token
  appears in either file (id census, §7). Every inline id resolves to one of the five rows → REPOINTED's second clause holds.
- **The staged prose ids are gone.** Staged base entry ground line cites "round 1's S729, S730"; staged amend line 11 cites
  "round 3's S754 … round 2's S742/S743"; staged amend line 44 builds a whole section from S895. None of `S729 S730 S742 S743 S754
  S895` occurs in either draft (count 0). Their lane numbers all name **unrelated** documents — S729 Neer et al. 2025 (infant-directed
  speech), S742 classroom greetings, S743 Akita 2012 (Japanese morphophonology), S754 UNESCO ICH (tugging rituals) — so citing them
  would have been the worst kind of REPOINTED failure, and not citing them is correct.
- **S895** (王昕玥, 《论〈龙族〉的叙事失控与世界观危机》, chinawriter 2025-10-30) is cited 3× in the staged amendment and its
  section ("What makes a world-view fail": 叙事驱动机制 / 价值共识框架 / 类型标识系统) is **not carried** into the draft → no row is
  owed. Note the inverse: appending S895 today would create a row no entry cites, whose `used-by` could not be "exactly the citing
  entries" → the kill rule's "used-by not exactly the citing entries" fires. The row set is closed on both sides.
- Coupled paths all exist at base (6/6 checked with `git cat-file -e`): `culture-material/cartography-and-mapmaking.md`,
  `linguistics/naming-systems.md`, `linguistics/conlang-scholarship.md`, `synthesis/coupling-model.md`,
  `synthesis/consistency-verification-checklist.md`, `synthesis/worldbible-integration-contract.md` → no phantom dependency, no
  fifth row owed for a coupling target.
- **No duplicate authority.** `synthesis/worldbible-integration-contract.md` is an interface/provenance contract (§3 ownership
  decision table, §5 per-artifact minimum record content for systems/lexica/ledgers). It does not define a settings-note schema, so
  the new entry's §6/§7 tables create no second convention; the handoff framing is coherent.
- The only unrowed attribution found is **K1**.

**The cut that no leg would catch (the attack a reviewer should run).** Cuts are honest only when they **delete sentences**. A "cut"
that kept the sentence and replaced the id with an inline URL would leave every mechanical leg green: REPOINTED inspects `source:`
lines (one id, URL registered on that row), inline S-ids, and a `forbidden_ids` list only (`accept-c.py:678-724`) — an inline URL in a
body sentence is invisible to it; CITEDLINES counts ids, ROWS counts rows, and census counts cells. QUALITY 7
warns against "inline URLs standing in for the registry rows" for separability, but no claim-C leg fires. So the reviewer's question
is not "is the row set four" but "does any surviving sentence in either entry name a document without a row?" — today the answer is
one (K1), and after K1 the answer is none.

## 6 Kill-rule consequence, per hypothetical cut

Reading rule: the kill rule fires on "any leg false at `<lands>`". **ROWS** ("adds *exactly* S881..S884, contiguous") fails for every
row cut and every row addition. **REPOINTED** fails only if a cite to the dropped row survives. **GATE** fails only for the two
chinawriter rows, which it names. Delete-and-rewrite survives REPOINTED and still fails ROWS; keep-the-cite-and-drop-the-row fails
both.

| cut | what must go with it | legs that go false | mechanism |
|---|---|---|---|
| S881 | base draft §§3,4,5,7,8,9 (2,746 of the draft's 4,194 words, measured `awk 'NR>=54&&NR<=254'`) | ROWS; REPOINTED if a cite survives | "adds exactly S881..S884" / 31 cited-but-unrowed ids |
| S882 | base draft §6's first two tables, §4 column, §8's genre+key-point+failure tables | ROWS; REPOINTED if a cite survives | same; plus the base header's "the three rows above / the two practitioner pages" become false (review, not mechanical) |
| S883 | amend §§2(first 3 bullets),3,5(table 1),1(headline) | **GATE**; ROWS; REPOINTED if a cite survives | GATE names the row: "S883/S884 rows state the re-quote" |
| S884 | amend §4 entirely, §5 table 2, §6, §1(李玮) | **GATE**; ROWS; REPOINTED if a cite survives | same clause; and §4 would then have no support at all — a QUALITY-1 hole, not a leg |
| add S895 (or any 5th) | a whole new section + Gate + evidence | ROWS | "adds exactly S881..S884 (contiguous)" |
| re-append the PDF as a 5th row | — | CENSUS (E04), ROWS | duplicate URL+scope, no supersedes |
| append a staged id as-is (S899/S900/S882..884) | — | CENSUS (E03), ROWS | duplicate id in the lane / not the mapped id |

## 7 Mechanical facts (exercised)

| check | command | result |
|---|---|---|
| base registry shape | `git show <base>:corpus/SOURCES.md \| grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` | **804** rows, last S880 (matches census-start) |
| draft id census | `grep -oE '\bS[0-9]{3,4}\b'` on both drafts, piped to `sort \| uniq -c` | base draft **S877 ×6, S881 ×31, S882 ×9**; amend **S883 ×20, S884 ×16** — no id outside the five-row set, no line with two ids (the numeric collision with campaign ids is §8 item 5) |
| base ground (a),(b),(c) | `git ls-tree -r --name-only <base> corpus/knowledge \| grep -ciE 'worldbuilding\|setting-practice'`; `git grep -lE '設定ノート\|世界観\|世界观' <base> -- corpus/knowledge \| wc -l`; per-host grep on the base registry | **0 / 0 / 0-0-0** |
| fleet URL duplication | per-lane grep for the three host names over **21** `*/corpus/SOURCES.md` | 0 hits → **no W04/E04** risk for the four URLs; the only occurrence is the lane's own scratch mirror |
| id availability | lane max id S880 vs S881..S884 | **no E03**; staged ids would have collided (staged S883/S884 = lane S883/S884), hence the renumber |
| QUALITY 15 shape | `python3 -B tools/check-cited-lines.py` on both drafts | **0 findings / 0 findings**, exit 0 — and it is row-set-neutral: deleting a row plus its cites leaves one id per line, so this criterion cannot be what protects the row set |
| mirror census | (not re-run by me; cited from `assimilation/validate-receipt-draft.txt`) | exit 0, E-codes 0, W01 ×3 (S881/S882/S884), W04 ×28 all inherited, none touching S877–S884 |
| row cell shape | mirror §2 | each appended row splits to **NF=13**; no ASCII pipe in any cell (E01/E09 rehearsal) |
| entry length floor | smallest entry at base `wc -w` | **478** (`culture-material/heritage-taxonomy-models.amend-2026-10-24-r13.md`); drafts are **4,194** and **1,989** → the ENTRIES floor does not bind, so "the entry would get too short" is **not** an argument for any row; only ROWS/REPOINTED/GATE are |
| coupled paths | `git cat-file -e <base>:<path>` ×6 | 6/6 present |
| workspace pollution | this seat | one scratch file `/tmp/q74simple_files.txt` (base entry path list); no tool installed; no download |

## 8 Claims-text issues met while deciding the row set (adjacent, for the claim owner — not edited here)

1. **GATE's premise is imprecise.** The leg says "the staged S899/S900 quotes were absent: R72 refusal, URL-quote mispairing".
   ScoutChinawriter2025 §2 shows the staged S899 span **is present byte-for-byte** on its own page; the refused register span
   (S816: `这个我肯定考虑过。我自己就是资深读者…`) belongs to the **S900** page. The rows should state that (register-span mispairing),
   not "the quotes were absent". Same shape, different wording; pre-data only.
2. **"R72" vs the wave record's R68/R71 quarantine (register S816/S817).** One of the two round numbers is wrong.
3. **The kill rule's "a refused/unknown staged id" clause can never fire** once the entries cite only lane ids — it protects nothing.
   The operative protection is REPOINTED's URL equality; keep it, do not rely on the staged-id clause.
4. **S877's `used-by` edit must be logged old→new in `corpus/lessons/round-74.md`** (append-only rule), and the lesson's `## Gate`
   needs per-row URL + 2026-10-25 + a located ≤25-word quote + locator for all four — that Gate record is what GATE and EVIDENCE
   read, so the anchor-quote choice in K7 is a single decision made once.
5. **The counter must not test for campaign ids by bare id — the namespaces collide on exactly the ids the amend cites.** Lane S883
   (chinawriter 2025-06-05) is numerically the campaign id for **litmemo**, and lane S884 (chinawriter 2022-12-07) is numerically the
   campaign id for **tuduku** (id-map `post_adoption_numeric_overlap`). The round-73 REPOINTED implementation greps a `forbidden_ids`
   list over the whole entry text (`accept-c.py:720-721`); if round 74 copies that shape with the campaign ids S882..S884/S899/S900,
   the amend's *correct* lane cites of S883/S884 fail REPOINTED — a false positive on the landing bytes. The leg's wording is already
   right ("an id naming an unrelated lane document"); the implementation must decide "unrelated" by the **URL join** (row URL vs cited
   URL, the check at `accept-c.py:704-710`), never by the bare id.

## 9 Where I stop

The next deletion that would still "help" is a row cut, and every one of those fails ROWS plus (for the chinawriter pair) GATE, or
forces a pre-data rewrite of the after-state map while halving a declared deliverable. That is the point where the attack costs more
than the weight it removes, so I stop here: **four new rows, one reuse, three payload/entry cuts (K1–K3), one prohibition (K4), two
"do not add" rulings (K5–K6), and four anchor cells to re-quote (K7)**. Nothing in this report is a landing decision; `claims.json`
and the registry are untouched by this seat.
