# RevEntryBaseFinal — attack on the landed base entry

**Object.** `corpus/knowledge/culture-material/worldbuilding-setting-practice.md` (267 lines, 4,317 words total /
3,694 body words after the first `## `), admitted as claim C's *base* entry under `corpus/QUALITY.md` 1–25 and
`PROVINCE.md`.

**Revisions attacked.** base `f7104cbce186bc2e1522abf0cfd619cc834628bb`; operative freeze
`00c408a0af2fa5ddf65af2224152ce258b26d896`; claim C lands `c4bf61a8d722f9168ce0fd8021a6261c000610c5`; claim Ca
lands `5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3`. Frozen claims read at the freeze
(`git show 00c408a0af2fa5ddf65af2224152ce258b26d896:reports/round-74/claims.json`, `config sha256 270e31790e2932c8…`) before any finding was
written; no rule was amended here.

**Verdict: WITH-CUTS.** No fabricated quotation, no invented source, no canon ruling, no word/header/cited-line
failure. One HIGH finding (S877 is cited outside its registered row scope — a records/scope defect, not a
fabrication), one MEDIUM (a false calibration reason) and nine LOW text/record defects. Exact cuts in C1–C12 (C11 sits inside the R1 bullet) below.

---

## Method and fetch record (QUALITY 21/22/24 hygiene)

All reads of the lane were `git show` / `cat` / the `read` tool against committed bytes; `git` was read-only; the
clone used for the claim-C counted commands lives at `/tmp/tmp.tkpecTtM96/lane` (local `main` = claim C lands); the
claim-Ca run used a second `mktemp -d` clone (path not retained) and the counter's own materialization printed
`clone=/tmp/r74-ca-oy2eapap/lands`. Scratch: `/tmp/RevEntryBaseFinal/`.

Every network fetch used exactly this User-Agent, recorded per request:

```
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36
```

| # | URL | HTTP | bytes | sha256 (body) | wall |
|---|---|---|---|---|---|
| 1 | `https://litmemo.com/ja/blog/novel-worldbuilding-guide` | 200 | 101,615 | `441fc921cadc744a7d59f91a055ff2eec1359d24f5c331d783104a1fa334ca64` | absent |
| 2 | `https://tuduku.space/column/novel-worldbuilding` | 200 | 17,068 | `754f504c34d796f40e86fb0d98c98946e36284c5fae511d7837f442662cfc1b7` | absent |
| 3 | `http://www.philol.msu.ru/~sidorova/files/conlangs.pdf` | 200 | 1,055,723 | `e512a20dd3eef97ed403bd4191545dea1147279d82b7cced32aaa6037ca595a9` | absent |
| 4 | CDX exact, litmemo slug | 200 | 3 | body `[]` | absent |
| 5 | CDX exact, tuduku slug | 200 | 3 | body `[]` | absent |
| 6 | CDX **positive control** `url=example.com` | 200 | 571 | 4 data rows returned | absent |
| 7 | CDX `matchType=domain`, `tuduku.space` | 200 | 3 | body `[]` | absent |
| 8 | CDX `matchType=domain`, `litmemo.com` | 200 | 542 | host captures returned (see F10) | absent |

Access date recorded as 2026-10-25 (lane convention, local UTC-3; request wall-clock 2026-10-25 23:0x local =
2026-10-26 ~02:0xZ). `automation: none`; no headless browser, no CAPTCHA, no block circumvented.

All three body hashes and byte counts reproduce the three `- source:` lines of the entry exactly.

---

## Findings

### F1 — HIGH — S877 is cited outside its registered row scope (QUALITY 6; SOURCES.md "tiers are scoped to the row's `scope`, never global")

`corpus/SOURCES.md:832` (identical at base and lands; only `status`/`recheck`/`used-by` may change in place, and
the round changed only `used-by`) registers S877 for:

```
SCOPE:   Tier B for the book's own framing: the classification of artificial languages (конланги), the
         vocabulary separating вымышленные языки from вспомогательные языки and from natural languages, the
         special status of Tolkien's languages, Klingon and D'ni, and the survey of the literature on imaginary
         languages. …
TEACHES: Supplies the Russian-language scholarly frame for constructed languages: a class system that separates
         fictional languages from auxiliary ones, a volume rule for how much language a world needs, and a dated
         literature survey
```

The entry leans on S877 for four substantive claims that none of those cells names, in §2 (entry lines 36–44) and
in its calibration row (line 23: "Sidorova & Shuvalova's framing of constructed worlds (2006) … a taxonomy of
constructed languages with an account of fictional worlds"):

- line 36: "Язык – главный инструмент построения вымышленных миров, дающий названия для их природных и
  социальных реалий" — the chief-instrument thesis (preface, p.7);
- line 38: "ВЯ в общем случае не служит средством коммуникации, он является предметом, темой коммуникации"
  (p.139, conclusion thesis 14);
- line 42: "связь между лингвоконструированием и моделированием миров неразрывна" (p.35);
- line 44: "некое научное или не совсем научное допущение" (p.36).

I verified all four spans live (see "Survived attacks" Q1), so this is **not** a fabricated or misplaced
quotation — it is a scope/records mismatch: the entry assigns S877 authority for theses the row's `scope` does not
declare, and the entry then calls the p.36 sentence "the strongest single design rule in this entry" (line 46).
The frozen pre-data correction A1 asserts the opposite of what the row records:

```
{'id': 'A1', 'by': 'RevAssimilationContract F1/F10', 'fix': 'S877 (reused row) gets a Gate record and an evidence
window; its use in the base entry is limited to the conlang-construction-as-modelling and world-building-context
claims inside its recorded scope.'}
```

There is no recorded scope clause for "conlang-construction-as-modelling" or "world-building-context"; the closest
cell content is `a volume rule for how much language a world needs` (TEACHES). The strongest defence of the entry
is the cell's opening phrase "Tier B for the book's own framing:" read broadly — that would reach the preface
sentence at p.7, but not the p.35–36 argument or the p.139 conclusion thesis, which are the book's claims rather
than its frame; those three uses still sit outside. Under SOURCES.md's own rule a citation outside the row's scope
has no declared tier, so §2 is unsourced for admission as filed.

**Fix (records, then optionally none):** file a superseding row (never an in-place tier/scope edit — SOURCES.md
"a correction is a new row whose `teaches` opens `supersedes S0NN —`") for the same document scoped to the
world-building / world-modelling passages, with its own anchor quote and evidence window; re-cite §2 and the §1
row to it. **If no superseding row is filed, apply cut C11**: delete §2's lines 38, 40, 42, 44 and the p.36 build
rule (line 46), keeping only the p.7 chief-instrument span, which the Gate did admit (round-74 Gate row S877).

### F2 — MEDIUM — a calibration reason is false on the page it describes (QUALITY 2 "with the reason")

Entry line 20:

```
| LitMemo five-step order | not mainstream — an unmeasured vendor-blog convention | one vendor blog for a writing
app, authored by the organisation, no named practitioner, no cohort and no citation; the page's own product calls
to action sit beside the advice |
```

The page does cite named authorities, with a year for one:

```
$ grep -o '1939年の講演「On Fairy-Stories」' /tmp/RevEntryBaseFinal/t881.txt
1939年の講演「On Fairy-Stories」
$ grep -o 'ファンタジー作家ブランドン・サンダースンは' /tmp/RevEntryBaseFinal/t881.txt
ファンタジー作家ブランドン・サンダースンは
```

and the entry's own §1 hard/soft row (line 24) concedes it: "the page names ブランドン・サンダースン but cites no
edition". "No citation" therefore contradicts both the page and the entry. (A "no named practitioner" reading as
"no named *author*" survives — the JSON-LD author is the organisation: `{"@type": "Organization", "name":
"LitMemo"}`.)

**Fix:** C2 below — narrow the reason to the five-step order itself.

### F3 — LOW — the S877 source line cites a page no sentence uses

Entry line 3: "cited here at printed pages 7, 35, 36, 139 and 140". The four quoted spans locate at PDF pages
7, 35, 36 and 139 (F-batch Q1 below); p.140 holds a claim the entry never uses:

```
$ cd /tmp/RevEntryBaseFinal && pdftotext -enc UTF-8 s877.pdf s877.txt && python3 locate.py
entry line 36 -> pdf page(s) [7]
entry line 38 -> pdf page(s) [139]
entry line 42 -> pdf page(s) [35]
entry line 44 -> pdf page(s) [36]
p140 first line: ['В-третьих, вымышленные миры не статичны. Они обладают историей, которая может писаться для них
«с обратным отсчетом» (от зафиксированной создателем мира точки, в которой мы «застаем» действие) и с отсчетом
прямым – в будущее. Историю имеют и фантастические языки.']
```

Offset is 0 (PDF page 35 prints "35"; PDF page 139 prints "139"; TOC puts Глава 2 at 35 and its first section at
36), so "printed page" and PDF page agree. A re-opener following the `- recheck:` instruction ("re-find each quote
on the printed page its sentence cites") has nothing to re-find on 140.

**Fix:** C1.

### F4 — LOW — §8's repair column adds advice the source does not give, under a header that claims the sources' words

Entry line 229: `| unused setting | … | cut it, or let it resonate somewhere |`, under the header at line 224
"Repair, **in the sources' own advice**". The page's advice is only resonance:

```
$ grep -o '物語のどこかに響かせましょう' /tmp/RevEntryBaseFinal/t881.txt
物語のどこかに響かせましょう
$ grep -c 'cut it' /tmp/RevEntryBaseFinal/t881.txt /tmp/RevEntryBaseFinal/t882.txt
t881.txt:0
t882.txt:0
```

No "cut it" advice anywhere on S881 or S882. **Fix:** C6.

### F5 — LOW — mistranslated cost term in a decision table

Entry line 184: `| cost | what the user loses: stamina, lifespan, memory, sanity, standing, uses |`. The page's
list is:

```
$ grep -o '代償は体力、寿命、記憶、正気、周りからの差別、使える回数の制限などから選べます。' /tmp/RevEntryBaseFinal/t881.txt
代償は体力、寿命、記憶、正気、周りからの差別、使える回数の制限などから選べます。
```

`差別` is discrimination/stigma, not social standing; a builder following "standing" designs a rank cost where the
source describes being shunned. **Fix:** C5.

### F6 — LOW — §10's coupling rationale misdescribes the note's section list

Entry line 259: "…because the note's first two sections are exactly those artefacts." The note's sections are
(entry lines 142–146, from S882): `世界地図・地名一覧`, `年表・歴史`, `魔法・能力一覧`, `人物一覧`,
`社会制度・用語集`. The map **and** the place-name list are both inside section 1; section 2 is the chronology,
which neither coupling names. **Fix:** C7.

### F7 — LOW — English glosses in quotation marks are presented as quotations but are not on the page

- Entry lines 78 and 88: "the reader's "why not just…" objection".
- Entry line 183: `write the "cannot" list first`.

The page's phrases, and the absence of the English glosses:

```
$ grep -o '読者からのツッコミを想定する：「なぜ〇〇しないのか」という疑問を先回りして設定に組み込む' /tmp/RevEntryBaseFinal/t882.txt
読者からのツッコミを想定する：「なぜ〇〇しないのか」という疑問を先回りして設定に組み込む
$ grep -o 'できること・できないこと：先に「できないこと」を決めるほうが早い' /tmp/RevEntryBaseFinal/t882.txt
できること・できないこと：先に「できないこと」を決めるほうが早い
$ grep -c 'why not just' /tmp/RevEntryBaseFinal/t882.txt; grep -c 'cannot' /tmp/RevEntryBaseFinal/t882.txt
0
0
```

The verdict is otherwise faithful to the source, so this is a quotation-shape defect,
not a content error. **Fix:** C3, C4.

### F8 — LOW — the couples-line gloss on the checklist contradicts the checklist's own scope and the entry's §9

Entry line 12: `` `synthesis/consistency-verification-checklist.md` (the verification side, whose verdicts lore
owns) ``. That entry says the opposite about its own statuses:

```
consistency-verification-checklist.md:2  … findings and alternatives go to lore-shokunin, which owns world-bible
                                          verification and every canon ruling.
consistency-verification-checklist.md:5  … checklist organization, statuses, and review procedure are lane-authored
                                          craft conventions, not findings attributed to those scholars.
consistency-verification-checklist.md:25 … Send the findings … Stop at handoff; do not select the official variant
```

and the base entry's §9 (line 255) states it correctly ("hands findings to lore"). **Fix:** C8.

### F9 — LOW — a line restates three source claims with no S-id (QUALITY 15's review-only clause-scope limb; the lint cannot see it)

Entry line 32: "…the entry's claims about worlds are confined to what the monograph states in this context — a
language is the chief instrument of world-building, a constructed language is its world's subject rather than a
means of talk, and a premise precedes the picture — so no tier-C page carries a claim alone about worlds." Three
content claims, no id on the line. `check-cited-lines.py` reports 0 findings because the line carries none (it
fires only on MULTI-ID/TABLE-ID), so this shape is invisible to the gate. **Fix:** C9.

### F10 — LOW — the two "no capture" rulings lack the probed URL and positive control the criteria require (QUALITY 21/24 records shape); the ruling itself is TRUE

Entry line 4: "the Internet Archive CDX holds no capture of this slug, probed 2026-10-25"; line 5: "no capture of
this slug or host in CDX". Neither names the probed URL or a positive control, and the round's Gate section
(`corpus/lessons/round-74.md:18-22`) records no CDX probe at all for S881/S882. I re-probed and the claim holds:

```
$ curl -sS -A "$UA" 'http://web.archive.org/cdx/search/cdx?url=litmemo.com/ja/blog/novel-worldbuilding-guide&output=json&limit=4'
[]
$ curl … 'url=tuduku.space/column/novel-worldbuilding&output=json&limit=4'
[]
$ curl … 'url=example.com&output=json&limit=4'          # positive control
[["urlkey","timestamp",…],["com,example)/","20020120142510",…]]      (571 B, 4 rows)
$ curl … 'url=tuduku.space&matchType=domain&output=json&limit=3&collapse=urlkey'
[]
$ curl … 'url=litmemo.com&matchType=domain&output=json&limit=3&collapse=urlkey'
[["urlkey","timestamp",…],["com,litmemo)/","20260911102443","https://litmemo.com/","text/html","200",…]]
```

So the *slug* has no capture (both hosts), the *tuduku host* has none, and the *litmemo host* does have captures
of other pages — the query shape demonstrably finds captures, which is the control the entry omits. **Fix:** C10
(record the two probe URLs and the control), no factual change.

### F11 — LOW — the `- sources:` line says the monograph supplies no build method, while §2 calls its p.36 sentence the entry's strongest design rule

Entry line 11: "the monograph is tier B and supplies what a constructed world is, **not how to build one**." Entry
line 46: "That is the scholarly counterpart of the practitioners' first step, and it is **the strongest single
design rule in this entry**: the first artefact is a one-sentence premise, and everything else is derived from it."
The p.36 sentence is a description of how SF authors work (`автор предлагает … допущение и далее строит вокруг него
ту картину мира`), from which the entry derives a build rule; "not how to build one" therefore contradicts the
use the entry makes of that sentence at line 46. **Fix:** C12.

---

## Exact cuts (WITH-CUTS)

- **C1** line 3: `printed pages 7, 35, 36, 139 and 140` → `printed pages 7, 35, 36 and 139`.
- **C2** line 20: `no named practitioner, no cohort and no citation` → `no named author, no cohort, and no citation
  for the five-step order itself (its two named authorities — Tolkien's 1939 lecture, Sanderson's split — carry no
  edition or page)`.
- **C3** lines 78 and 88: `the reader's "why not just…" objection` → `the reader's 「なぜ〇〇しないのか」 objection`.
- **C4** line 183: `write the "cannot" list first` → `write the 「できないこと」 list first`.
- **C5** line 184: `sanity, standing, uses` → `sanity, discrimination, uses`.
- **C6** line 229: `cut it, or let it resonate somewhere` → `let it resonate somewhere in the story`.
- **C7** line 259: `because the note's first two sections are exactly those artefacts` → `because the note's first
  section carries exactly those two artefacts (the drawn map and the place-name list)`.
- **C8** line 12: `(the verification side, whose verdicts lore owns)` → `(the verification side; its findings go to
  lore, which owns the canon ruling)`.
- **C9** line 32: end the sentence `…so no tier-C page carries a claim alone about worlds (S877).`
- **C10** lines 4–5: append the probe and control, e.g. `CDX probes 2026-10-25: exact url=litmemo.com/ja/blog/
  novel-worldbuilding-guide → []; control url=example.com → 4 rows returned.`
- **C12** line 11: `the monograph is tier B and supplies what a constructed world is, not how to build one` → `the
  monograph is tier B and supplies what a constructed world is and prescribes no authoring order (its p.36 account
  of how SF authors work yields the one design rule at line 46)`. (If C11 is taken, instead delete the parenthetical
  clause and keep "prescribes no authoring order".)
- **R1 (records, preferred for F1)** superseding SOURCES row for the same document scoped to the
  world-building/world-modelling passages (p.7 preface; pp.35–36; p.139 thesis 14), anchor quote + evidence; re-cite
  §2 and the §1 row. **C11** if R1 is not filed: delete §2 lines 38, 40, 42, 44, 46 and comparison-table rows 50–52
  (leaving the Gate-admitted p.7 paragraph at line 36 and rows 53–54), and trim the §1 row 23's reason to the
  registered classification/vocabulary/special-status scope.

---

## Attacks that FAILED (the claim survived), with evidence

**Q1 — quotation fidelity: every quoted span in the entry locates on the live source.** Method: tag-preserving
strip of the served bytes (block tags → newline, inline tags → nothing), then substring test after NFKC +
whitespace folding; for the PDF, `pdftotext -enc UTF-8` plain mode over the 186-page extraction and a page-index
search. Raw result:

```
S881 76 LIVE_OK   決めておくのは、展開に直接かかわる核の設定だけで十分です。
S881 237 LIVE_OK  全員が同じ設定資料を一つだけ使い、それを正本にします。
S881 253 LIVE_OK  同じ世界でシリーズや複数の作品を書くなら、世界観設定を作品をまたいで共有できます。
S881 58 LIVE_OK   物語が起きる世界の決まりごとの総体です
S881 103 LIVE_OK  外側の層が内側の層を決める
S881 112 LIVE_OK  約束を破る者
S882 126 LIVE_OK  勢力図・人間関係の構造：誰が権力を持ち、何が対立の軸になっているか
S882 136 LIVE_OK  特に重要なのは魔法・技術システムの「制約」です。
S882 138 LIVE_OK  魔法・技術システム：何ができて何ができないか。ルール（制約）が重要
S882 148 LIVE_OK  世界地図・地名一覧：手書きでよいので地図を描いておく
S882 218 LIVE_OK  世界観設定は「作者が知っていること」と「読者に伝えること」を分けて考えましょう。
entry line 36 -> pdf page(s) [7]
entry line 38 -> pdf page(s) [139]
entry line 42 -> pdf page(s) [35]
entry line 44 -> pdf page(s) [36]
```

The one apparent miss (`S881` line 253) is inline-link markup (`世界観設定を<a …>作品をまたいで共有</a>できます。`);
rendered text is verbatim. No punctuation drift: the full-width `：` and `（）` in the entry match the page's
characters exactly. **Attack failed.**

**Q2 — counters, run only inside my own clones** (clone procedure as assigned: `mktemp -d`, `git init -q`,
`rev-parse --show-toplevel` printed the temp dir, `git clone` into `$D/lane`, `branch -f main <lands>` after
`checkout --detach`).

```
$ python3 -B reports/round-74/accept-c.py --root . --lands c4bf61a8d722f9168ce0fd8021a6261c000610c5 --freeze 00c408a0af2fa5ddf65af2224152ce258b26d896 --fleet-root /home/vgpnk/Projects/shokunin
# stamped revision: c4bf61a8d722f9168ce0fd8021a6261c000610c5
# evaluated revision: c4bf61a8d722f9168ce0fd8021a6261c000610c5
# measured revision (lane main): c4bf61a8d722f9168ce0fd8021a6261c000610c5
# tree: 29c8c147c948b9fe03af8f092ac92028a23fed56
# frozen legs: 13 (ENTRIES,ROWS,REPOINTED,GATE,EVIDENCE,REJECTS,GROUND,CITEDLINES,CENSUS,SCRATCHMIRROR,COLLCHECK,FROZENCFG,INDEX)
LEG PASS ENTRIES            (leg lines elided)
…
LEG PASS INDEX
ACCEPT-C-74: PASS legs=13/13            (exit 0)

$ python3 -B reports/round-74/accept-ca.py --root . --lands 5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3 --freeze 00c408a0af2fa5ddf65af2224152ce258b26d896 --fleet-root /home/vgpnk/Projects/shokunin
LEG PASS LEDGER             (leg lines elided)
…
LEG PASS STAMP
ACCEPT-CA-74: PASS legs=11/11           (exit 0)
```

**Attack failed.** (Ca is not this seat's object; run for context.)

**Q3 — criterion 15 lint, with controls proving the lints are live on this entry's bytes.**

```
$ python3 -B tools/check-cited-lines.py corpus/knowledge/culture-material/worldbuilding-setting-practice.md
CITED-LINES: 0 finding(s) in 1 file(s)        exit 0
$ python3 -B tools/check-draft-ids.py corpus/knowledge/culture-material/worldbuilding-setting-practice.md
DRAFT_IDS: 0 findings                          exit 0
$ python3 -B tools/check-cited-lines.py --selftest
… 
selftest 26/26
# controls on a /tmp copy of the same bytes:
MULTI-ID ctl.md:30 S881,S882
TABLE-ID ctl.md:154 S881
CITED-LINES: 2 finding(s) in 1 file(s)        exit 1
DRAFT_ID ctl.md:30 ', -6'
DRAFT_IDS: 1 findings                          exit 1
```

**Attack failed** on the lint's two shapes; F9 records the review-only shape the lint cannot see.

**Q4 — header/provenance trio and template.** `- source:` ×3, `- verified-at:`, `- recheck:` are lines 3–7, before
any body; all nine fields the round's ENTRIES leg requires (`source, verified-at, recheck, ground, topic,
gap-filled, sources, couples, scope`) are present, no placeholder value, no `<…>` token (ENTRIES PASS above).
`- refuses:` is an extra tenth field. **Attack failed.**

**Q5 — ground claims.** Re-derived at base, read-only:

```
$ git ls-tree -r --name-only f7104cbce186bc2e1522abf0cfd619cc834628bb corpus/knowledge | grep -ciE 'worldbuilding|setting-practice'
0
$ git grep -lE '設定ノート|世界観|世界观' f7104cbce186bc2e1522abf0cfd619cc834628bb -- corpus/knowledge | wc -l
0
$ git show f7104cbce186bc2e1522abf0cfd619cc834628bb:corpus/SOURCES.md | grep -cE '^\| *S[0-9]{3} '
804
hosts at base: litmemo.com=0 tuduku.space=0 chinawriter.com.cn=0   (grep -c per host on the same blob)
```

**Attack failed.**

**Q6 — word floor.** Counter floor (whole-file minimum over the 247 base knowledge files) = **478** words
(`heritage-taxonomy-models.amend-2026-10-24-r13.md`); the entry's body is **3,694** words (7.7×). **Attack failed.**

**Q7 — coupling paths.** All six `- couples:` targets exist at base (`git cat-file -e base:<path>`): cartography,
naming-systems, conlang-scholarship, coupling-model, consistency-verification-checklist,
worldbible-integration-contract. No path is newly landed by another claim, so criterion 7 holds for these names.
**Attack failed** (quality of two glosses is F6/F8).

**Q8 — canon hygiene / PROVINCE handoff.** The entry decides no world's canon: the closing paragraph states "No
layer assignment, no element count, no depth target and no document layout is fixed for a setting by this entry";
every normative table is labelled as method (What to do / Question the layer must answer / Artefact it forces),
and the one column that claims the sources' words is F4. It rules on no real-world culture or reader, and makes no
rights/attribution ruling (the Sanderson hedge at line 192 — "used here only as a scale of explicitness, not as a
claim about Sanderson's text" — is the opposite of a ruling). The handoff names
`synthesis/worldbible-integration-contract.md` and assigns lore the canon decision, matching that contract's
"kotodama submits; lore issues disposition" (`worldbible-integration-contract.md:99`). In province for
`culture-material`. **Attack failed.**

**Q9 — calibration vocabulary.** All five §1 rows name a status with a reason; the vocabulary sentence (line 26)
maps the entry's labels onto QUALITY 2's three words ("not mainstream … nothing here is contested or
discredited"). "Not mainstream" is a negation of the canonical label, not one of the three; there is one lane
precedent (`linguistics/historical-linguistics.md`), so the shape is not novel, and the mapping is stated. I treat
this as compliant with a note, not a defect; the reason-level defect is F2. **Attack failed.**

**Q10 — index and separability.** `corpus/README.md:446` reproduces the entry's `- topic:` byte-for-byte (a python
comparison of the index row's tail with the entry's `- topic:` value printed `equal: True`); the INDEX leg passes; the entry cites only rows C itself lands (S881, S882) plus a
base row (S877), and names only base paths. **Attack failed.**

---

## QUALITY 1–25 disposition for this object

| # | Criterion | Disposition |
|---|---|---|
| 1 | Provenance | **Pass** — three real sources, three body hashes reproduced live, all quotes locate (Q1); F1 is a scope-record defect, F11 a framing defect in the `- sources:` line. |
| 2 | Calibration | **Pass with F2** — every framework row named and reasoned; one reason clause false. |
| 3 | Coupling | **Pass with F6/F8** — six couplings, two glosses wrong. |
| 4 | Usability | **Pass** — 15 tables (10 sections), worked micro-chain, worked town, worked power, four failure/repair tables. No essay section. |
| 5 | Canon hygiene | **Pass** — decides nothing; handoff closes the entry (Q8). |
| 6 | Claim-scoped authority | **FAIL — F1 (HIGH).** |
| 7 | Separability | **Pass** — Q7/Q10. |
| 8, 9 | Dry runs both ways | Out of entry scope (round counters; Q2 PASS). |
| 10 | Ordinary access | **Pass** — plain requests, no challenge; access records present. |
| 11 | Failable clauses | Out of entry scope; note F9's shape is not mechanically checked. |
| 12 | Re-test rejection grounds | Out of entry scope. |
| 13 | Unreachable handling | N/A — all three fetches returned 200 on the first pass, no retry budget needed. |
| 14 | Judged object frozen | Out of entry scope. |
| 15 | Cited-line shape | **Pass (lint 0 + controls)**; F9 is the review-only limb. |
| 16 | Bounded fetches / body-scoped quotes | **Pass** — quotes are body/heading text (no caption/alt/aria source); single-pass 200s. |
| 17–19 | Receipts/stamp/revision | **Pass** — Q2 stamp = evaluated = measured. |
| 20 | Trends | Out of entry scope. |
| 21, 24 | CDX no-capture discipline | **Claim true, record incomplete — F10.** |
| 22 | UA-bound wall records | N/A — no wall record in this object; every request 200 with the browser-shaped UA. |
| 23 | Counter selftest/red-before | Out of entry scope. |
| 25 | Freeze constants | Out of entry scope (frozen legs 13 read from `git show <freeze>`, Q2). |

---

## Residual risk and verification gaps

1. **Live-page drift is unpinned on the reading side.** The three body hashes are today's bytes; no archived capture
   of either Japanese page exists (probed: F10), only host-level captures of other pages on litmemo.com. A re-opener in six months can
   only re-fetch and compare hashes; the entry's `recheck: 180d` says so, but durability rests on the two hosts
   surviving.
2. **Rendering path.** The two Japanese pages were read from the served HTML with a tag-stripping parser; their
   JavaScript was not executed. Every quoted span occurs in the served bytes, so no quote depends on a script-only
   render — but a reader who opens the pages in a browser sees a rendered DOM this review did not compare against.
3. **Registry S877 page count disagrees with the entry** (185-page "typeset text" in the scope cell vs the imprint's
   `2006, с.184` and the entry's "184-page monograph"). The entry is right by the imprint; the row is a records-side
   oddity (out of this seat's cuts).
4. **The floor is a whole-file count compared to a body count** (`accept-c.py:680-691` returns the whole-file
   minimum; `leg_entries` compares it with body words). Conservative, so it cannot pass a stub — but the leg's
   docstring says "body at least the base tree's smallest entry", which is not what it computes. Not an entry
   defect; recorded because a later seat may mistake the 478 for a body floor.
5. **F1 cannot be closed by a text edit alone** unless C11 is taken; R1 is a records action for a later round's
   Gate, so the verdict is WITH-CUTS pending either.

## Tooling record

No installs, no upgrades, no `pacman`. Tools used: `curl` (system), `pdftotext` (system poppler), `python3` (system,
`-B`), `git` (read-only). Nothing was written outside `/tmp/RevEntryBaseFinal/`, the two throwaway clones, and this
report.
