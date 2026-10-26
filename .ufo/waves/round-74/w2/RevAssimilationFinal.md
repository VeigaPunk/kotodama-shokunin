# RevAssimilationFinal — item-10 assimilation attack over landed bytes (round 74, wave 2)

Seat: `RevAssimilationFinal` (leaf; no delegation, no background jobs, no `task`).
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`; source repo read-only:
`/home/vgpnk/Projects/shokuknow`.
Base `f7104cbce186bc2e1522abf0cfd619cc834628bb`; operative freeze
`00c408a0af2fa5ddf65af2224152ce258b26d896`; claim C lands
`c4bf61a8d722f9168ce0fd8021a6261c000610c5`; claim Ca lands
`5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3`.
Writes: this file only. No repo mutation, no install (no tool was installed or upgraded).

Scope: prompt item 10 (`/home/vgpnk/Projects/shokunin/.ufo/prompts/kotodama-round-74.md:440-545`)
executed against the landed bytes. The claim's own legs were run as the claim's rule
(`accept-c.py` 13 legs, `accept-ca.py` 11 legs); the frozen claims were read at the freeze commit.

## Verdict

**The claim's declared legs all pass at their lands.** I reproduce C `PASS legs=13/13` and
Ca `PASS legs=11/11` in my own clones. Six findings: two MEDIUM and four LOW. The lesson's own
scratch-mirror paragraph is stale and contradicts the landed commit order (F1, MEDIUM); the
reused S877 row's recorded scope does not enumerate the world-building framing the base entry
draws from it, while the frozen correction A1 asserts that it does (F2, MEDIUM); the item-10
"paste both id lists" instruction is not in any committed report (F3, LOW); the per-entry
PROVINCE/QUALITY gate results live only in wave-1 seat reports, not in the lesson's Gate
(F4, LOW); a tracked telemetry receipt is truncated in the wave-2 worktree (F5, LOW, hygiene);
and the stripped recheck prose sits in the item-10 section rather than the named Gate block
(F6, LOW, form). No source, quote, row, quarantine verdict or counter fact was found false.

## Obligation walk

| item-10 obligation | state | evidence |
|---|---|---|
| source repo read-only; no campaign tool | MET | `find /home/vgpnk/Projects/shokuknow -newermt '2026-10-25 20:00' -type f \| wc -l` = **0**; package and register sha256 equal the round's map inputs (below) |
| one theme, 1–3 entries | MET | one theme (`worldbuilding-setting-practice`), two files: `corpus/knowledge/culture-material/worldbuilding-setting-practice.md`, `…amend-2026-10-23.md` |
| every cited source re-opened in-round | MET | five live byte-verified fetches/committed captures; all five Gate quotes re-located by me (below) |
| only cited rows appended; no staged row as-is | MET | four rows added, each cited by an admitted entry; staged rows 12 cells → landed 11; no literal/escaped `\|`; `used-by` exact; `opened` 2026-10-25; `recheck` `180d` |
| collision check in scratch before append, 0–3-space pattern proved | MET | `reg-ids` 804 sha `94a495c7…`, `staged-ids` 132 sha `bab11d7d…`, `collisions` 22 sha `130ec2d1…`, `cmp` OK; 2sp/3sp fixtures catch, 4sp and column-zero miss |
| scratch mirror gated BEFORE the registry append | MET in the commits; **lesson text says otherwise (F1)** | receipt committed `de93d91` 22:28:24; append committed `d7a3840` 22:48:30; mirror registry == lands (empty diff) |
| quarantine slice derived and verdicted | MET | prompt awk yields 21 rows (18 `payload-absent` + 3 prose-class); S816/S817 re-checked and refused; four clearing conditions recorded; register untouched |
| ≥1 admit and ≥1 reject in the lesson Gate | MET | 5 admit rows (S877, S881–S884), 4 reject rows, 6 refused families / 34 files with reason + clearing condition |
| refused families kept with reason + flip | MET | lesson `## Gate` family table, lines 44–51, 6 families summing to 34 files |
| `considerthese` absent → one report line | MET in the lesson; not yet in a round report (F3) | `ls considerthese` → ENOENT; lesson:183 |
| frozen claim not rewritten | MET | counters byte-identical at freeze and main (`8d30487f…` / `8052f1e2…`); claims.json read only from the freeze |
| counters pass at lands | MET | C `ACCEPT-C-74: PASS legs=13/13`; Ca `ACCEPT-CA-74: PASS legs=11/11` |

## Findings

### F1 — MEDIUM: the lesson (and `validate-notes.md`) say the scratch-mirror sequencing clause is "owed" after the landed commits satisfy it

The lesson's item-10 paragraph cites the **superseded draft** receipt and the **draft** mirror
hash, and declares the sequencing clause unexercised:

- `corpus/lessons/round-74.md:113-119` — "the two draft entries (`sha256 658a8fa4…9986b00b` and
  `bb5504e2…d80d8673e`) … `sha256 81fcebe1…f2f326` … (`assimilation/validate-receipt-draft.txt`).
  The claim's 'commit strictly before the registry-append commit' sequencing clause is not
  exercised by a leaf seat and stays owed."
- `.ufo/waves/round-74/assimilation/validate-notes.md:91` — "**not exercised** … so
  `A/validate-receipt-draft.txt` is a draft whose commit position is a later wave's job."

The landed commit order is the opposite:

```
$ git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin log --format='%h %s' \
    f7104cbce186bc2e1522abf0cfd619cc834628bb..main -- \
    .ufo/waves/round-74/assimilation/validate-receipt.txt corpus/SOURCES.md
d7a3840 round-74: claim C landing — worldbuilding-setting-practice entries, rows S881-S884, S877 used-by, README index, lesson, census
de93d91 round-74: freeze — final claims, ledger, counters, controls inputs, inherited round-73 w2 files, wave-1 evidence
```

`git log` is newest-first, so the receipt (`de93d91`, 22:28:24) precedes the registry append
(`d7a3840`, 22:48:30). The operative receipt is the non-draft file, and its bytes are identical
at every freeze/landing commit:

```
$ git show de93d91:.ufo/waves/round-74/assimilation/validate-receipt.txt | sha256sum | cut -c1-16
b55d531e2eb3322d
$ sha256sum .ufo/waves/round-74/assimilation/validate-receipt.txt | cut -c1-16
b55d531e2eb3322d
```

The receipt's own mirror registry hash and the landed registry agree:

```
$ sha256sum .ufo/waves/round-74/assimilation/validate/corpus/SOURCES.md
c8da0a5a765de26506a1c4d9b66d9b47c9ffe4e0d62a87fc510077a7f83c5614
$ diff .ufo/waves/round-74/assimilation/validate/corpus/SOURCES.md corpus/SOURCES.md | wc -l
0
```

The lesson's three draft hashes are from an earlier draft generation, not the final drafts or
the landed files: final drafts `465051db…` (base) / `0b2e06dc…` (amend); landed entries
`2a81bea6…` / `cdab71c6…` (the deltas are the `<base>` substitution in `- ground:` lines and
the amend's locator formatting, verified by `diff`). The census gate reads the registry and
`used-by` paths, not entry bytes, so the gate result is unaffected; the receipt's phrase
"byte copies of the FINAL drafts" is true of the drafts it copied.

Proposed fix: rewrite `corpus/lessons/round-74.md:113-119` and
`.ufo/waves/round-74/assimilation/validate-notes.md:91` to cite `validate-receipt.txt`
(sha256 `b55d531e…`), the mirror registry sha256 `c8da0a5a…`, and the `de93d91 < d7a3840`
order; state that the mirror copies the final drafts and that the landed entry delta is the
`<base>` fill, which the census gate does not read.

### F2 — MEDIUM: S877's recorded scope cell does not name the world-building framing the base entry draws from it, while frozen correction A1 asserts the use is "inside its recorded scope"

The reused row's `scope` cell (unchanged in place; only `used-by` changed) scopes the B tier to:

```
$ sed -n '832p' corpus/SOURCES.md | awk -F'|' '{print $6}'
 Tier B for the book's own framing: the classification of artificial languages (конланги),
 the vocabulary separating вымышленные языки from вспомогательные языки and from natural
 languages, the special status of Tolkien's languages, Klingon and D'ni, and the survey of
 the literature on imaginary languages. The full 185-page typeset text was opened …
```

The base entry imports four S877 claims from **other pages** of the same book and calls one of
them the entry's strongest rule:

```
$ grep -n 'S877' corpus/knowledge/culture-material/worldbuilding-setting-practice.md
3:  - source: S877 … cited here at printed pages 7, 35, 36, 139 and 140, the passages where the
       book treats world-building as the context of conlang-making …
36: language is the chief instrument for building fictional worlds … (S877)
38: a constructed language is normally not a means of communication … (S877)
42: the link between language construction and world modelling is unbreakable … (S877)
44: the author offers "некое научное или не совсем научное допущение" and then builds … (S877)
```

The wave-1 scribe flagged exactly this and asked the freeze to decide:

```
$ sed -n '257,259p' .ufo/waves/round-74/w1/ScribeEntryBase.md
F11. **S877's scope cell does not name the framing this entry quotes.** The row scopes "the book's
own framing: the classification … the vocabulary separating вымышленные языки …". The quotes used
here extend it to the world-modelling framing (pp. 7, 35–36) and the fictional-class function
definition (p. 16). I cite the row as it stands and do not edit it; the freeze should either widen
the `scope` cell or accept the quotes as inside "the book's own framing".
```

The frozen pre-data correction decides by assertion, and the lesson never records it:

```
$ python3 -c "import json; c=json.load(open('reports/round-74/claims.json')); print([x['fix'] for x in c['pre_data_corrections'] if x['id']=='A1'][0])"
S877 (reused row) gets a Gate record and an evidence window; its use in the base entry is limited to the conlang-construction-as-modelling and world-building-context claims inside its recorded scope.
```

Under CORPUS v1, `scope` is "the claim or topic the tier applies to"; on the face of the cell the
entry's pp. 7/35/36/139 claims are not in the enumerated list, and SOURCES rule 2 forbids
widening `scope` in place. Whether the opening phrase "the book's own framing" is broad enough to
cover them is exactly the judgment the scribe asked the freeze to make; the freeze asserts it
without recording the acceptance in the lesson.
The quotes themselves are real — I located all four on the PDF (`Язык – главный инструмент…` p.7,
`связь… неразрывна` p.35, `…допущение` p.36, `ВЯ … предметом, темой коммуникации` p.139) — so
this is a calibration-scope/bookkeeping defect, not fabrication. It matters because the kill
rule's "unrelated-document id" and the entry's own `sources:` sentence ("the monograph is tier B
and supplies what a constructed world is, not how to build one") are in tension with §2's
"strongest single design rule".

Proposed fix: record the F11 decision in the lesson's `## Gate` notes (accept-as-framing or not),
and, if the B tier is to cover the world-building framing, open a superseding row under SOURCES
rule 2 in a later round with a widened `scope` and a round-N located quote; otherwise restate
§2's S877 claims so the tier-B support is confined to the recorded framing.

### F3 — LOW: "Paste both id lists … into the report" is not in the lesson, and the round report does not exist yet

Item 10 requires both id lists, the collision count and the renumber map pasted into the report.
The lesson pastes the counts, ranges, sha256s and the renumber map, but not the lists:

```
$ sed -n '56,70p' corpus/lessons/round-74.md        # guard table
| `assimilation/reg-ids` | 804 (S001…S880) | `94a495c7…` |
| `assimilation/staged-ids` | 132 (S859…S990) | `bab11d7d…` |
| `assimilation/collisions` | 22 (S859…S880) | `130ec2d1…` |
$ ls /home/vgpnk/Projects/shokunin/.ufo/reports/round-74/
game-dev-2d.md  game-dev-3d.md        # no kotodama.md
```

The lists are committed (`assimilation/reg-ids`, `staged-ids`) and reproduce exactly, so this is
a form obligation, not a data gap; it may be discharged when the fleet report is written at
round close. The same absence means the quarantine verdicts ("verdicts land in the lane's lesson
and report") and the `considerthese` line are in the lesson and the wave-1 seat report but not in
the round report yet.

Proposed fix: when the fleet report lands, paste the two lists (or the full contents as
attachments, plus the first/last and sha256), the collision count, the renumber map, the 21-row
quarantine verdict table, and the `considerthese: absent` line.

### F4 — LOW: per-entry PROVINCE.md and QUALITY.md gates are not recorded in the lesson's Gate

Item 10 requires a `PROVINCE.md` scope check and the `QUALITY.md` bar per entry. Both were
performed in wave 1 — `ConnectorSiblings.md` (in-lane verdict, lore boundary, 0 sibling matches)
and `RevEntryQuality.md` (REFUSE-AS-IS for the staged files; three residual defects for the
drafts) — and the residuals are fixed in the landed bytes: QUALITY 2 vocabulary at
`worldbuilding-setting-practice.md:23-26`, the corrected `(to-verify)` location at :253, and the
row-level fixes at the four rows. The durable lesson's `## Gate` does not point at either report
or state the per-entry verdict.

Proposed fix: add one Gate note naming `ConnectorSiblings.md` §1–§3 and `RevEntryQuality.md` §1/§6
and the three residual fixes, so a reader of the lesson alone can see the per-entry gates.

### F5 — LOW (worktree hygiene, not a committed-byte defect): a tracked telemetry file is truncated in the worktree during wave 2

At review time `git status` shows a tracked file truncated to zero bytes:

```
$ git status --porcelain | head -1
 M .ufo/waves/round-74/counters/junk-r74-run.txt
$ git diff --stat -- .ufo/waves/round-74/counters/junk-r74-run.txt
 .ufo/waves/round-74/counters/junk-r74-run.txt | 242 --------------------------
$ ls -la --time-style=full-iso .ufo/waves/round-74/counters/junk-r74-run.txt
-rw-r--r-- … 0 2026-10-25 23:11:25 …
```

The committed bytes are intact (`git show main:…` is the 242-line receipt), and the truncation
is at 23:11, during wave 2, so it is concurrent wave-2 activity, not the claimed commits. It is
the same class as R74-M1 (worktree writes after landing) and should be restored or regenerated
before round close. The guard-proof mirrors and `assimilation/validate/` were untracked at 22:59
and are now committed by the orchestrator snapshot `92b8d4b` (23:17, "not a landing"); the
claim-side files are unchanged after `c4bf61a` (`git diff --stat c4bf61a..main` touches only
`reports/round-74/telemetry/{junk,measures}-*.txt` and wave-2/scratch files).

### F6 — LOW: the stripped recheck prose is recorded in the item-10 section and the entries, not in the `## Gate` block the contract names

Item 10 says the prose stripped from the four `recheck` cells is "recorded in the round lesson's
Gate block". The lesson's `## Gate` runs lines 11–53; the four-row recheck table is at lines
99–108 under `## Collision guard and scratch mirror (item 10)`. The substance is preserved
twice — the lesson table names each staged cell and its stripped cadence, and the entries'
own `recheck:` lines carry the full re-open instructions
(`worldbuilding-setting-practice.md:7`, `…amend-2026-10-23.md:6`) — but the named location is
not the one used. Proposed fix: move the four-row table (or a pointer to it) into the Gate
block on the next append-only lesson correction; no data change is needed.

## Attacks that FAILED (the claim survived)

### A1 — Source repo read-only: survived

```
$ find /home/vgpnk/Projects/shokuknow -newermt '2026-10-25 20:00' -type f | wc -l
0
$ sha256sum /home/vgpnk/Projects/shokuknow/merge/kotodama/SOURCES.append.md \
            /home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md
7fb4f488807e8364d204a3081a2e57379d6caafaa92dbab9dfbc381757223754  SOURCES.append.md
5afe1810a6c3d62f37987b575a954f5b1197daa23005d4bb2f1d982f64bad833  absent-defect-register.md
# id-renumber-map.json inputs: same two hashes plus the base registry 93d60464…
```

`git -C …/shokuknow status --porcelain` has 1918 entries, all from the campaign's own staging
work (the 2026-10-24 23:33 staging pass and one tabi series at 2026-10-25 13:34); the newest
mtime among them precedes this round's 20:51 start, and no path is newer than 2026-10-25 20:00,
i.e. unchanged by this round.

### A2 — one theme, two entries: survived

Theme `worldbuilding-setting-practice`; entries exactly
`corpus/knowledge/culture-material/worldbuilding-setting-practice.md` and
`…amend-2026-10-23.md`; claim C's `entries[]` names the same two and no third.
The package's `MERGE-REPORT.md` names both staged files (lines 48, 57) and flags the amend
path as a duplicate target (round3 folded-into-canonical vs round4 new-file); the round
resolves that conflict by dropping the folded "Superseded passage" (staged S895), which the
lesson records as a declared reject with reason and flip (lesson:36), and by landing the
round-4 amendment rebuilt from re-quoted sources rather than the folded text.

### A3 — every cited source re-opened in-round: survived

The entries cite only S877, S881, S882 (base) and S883, S884 (amend):

```
$ grep -ohE 'S[0-9]{3,}' corpus/knowledge/culture-material/worldbuilding-setting-practice*.md | sort | uniq -c
      5 S877
     31 S881
      9 S882
     20 S883
     16 S884
```

My independent re-fetch (fetch log at the end) reproduces the exact evidence bytes and quotes:

| source | verification | quote |
|---|---|---|
| S881 litmemo | HTTP 200, 101,615 B, sha256 `441fc921…ca64`; quote 1 hit raw + stripped | 「自然環境が社会の仕組みを決め、社会の仕組みが文化を生み、文化が登場人物の価値観を作る。」 |
| S882 tuduku | HTTP 200, 17,068 B, sha256 `754f504c…c1b7`; quote 1 hit tag-stripped | 「勢力図・人間関係の構造：誰が権力を持ち、何が対立の軸になっているか」 |
| S883 chinawriter 2025 | committed round-71 capture `s816.html` 48,536 B sha256 `a3b6640c…ee94d` = evidence sha; quote 1 hit | 「整个过程里，我先做的是世界观，再考虑怎么升级，再考虑升级的表现。」 |
| S884 chinawriter 2022 | committed capture `s817.html` 62,604 B sha256 `344de345…3d659` = evidence sha; quote 1 hit | 「把它放在前面大概20章之内慢慢来，我觉得是问题不大的。」 |
| S877 PDF | HTTP 200, 1,055,723 B, sha256 `e512a20d…a9`; quote on PDF page 7 | «Язык – главный инструмент построения вымышленных миров» |

Evidence windows are self-consistent (recomputed sha256 equals the declared `window-sha256` for
all five; each quote occurs inside its stored window after NFKC+whitespace folding; S882's
window is the whole 2,953-character document and equals `visible-chars`).

### A4 — only cited rows appended, no staged row appended as-is: survived

Registry diff `f7104cb..main` is 5 insertions / 1 deletion: four rows S881–S884 plus the S877
line. S877's only changed cell is `used-by`:

```
$ # cell-diff of the S877 line, base vs lands
CHANGED 10
  OLD: ' corpus/knowledge/linguistics/conlang-scholarship.md '
  NEW: ' corpus/knowledge/linguistics/conlang-scholarship.md, corpus/knowledge/culture-material/worldbuilding-setting-practice.md '
# cells 0-9 SAME; 11 cells both sides
```

Row-level diff is exactly `801c801` and `804a805,808` (S877 is row 801 of 804; the four new rows
are 805–808). All four landed rows are 11 cells and contain no pipe character:

```
S877 pipes 12 escaped 0 census-cells(naive split) 11
S881 pipes 12 escaped 0 census-cells(naive split) 11
S882 pipes 12 escaped 0 census-cells(naive split) 11
S883 pipes 12 escaped 0 census-cells(naive split) 11
S884 pipes 12 escaped 0 census-cells(naive split) 11
# staged counterparts S883/S884/S899/S900: 13 pipes, 1 escaped, 12 naive cells
```

Field-by-field staged→landed comparison (staged ids S883/S884/S899/S900 → lane S881/S882/S883/S884):

| cell | transformation | restriction dropped? |
|---|---|---|
| `id` | by-document map (S883→S881, S884→S882, S899→S883, S900→S884) | no — never arithmetic; single-pass rule stated |
| `source` | rewritten with round-74 verified detail: S881 title corrected to the served page title (`世界観の作り方…`; staged title `小説の世界観はどう作る？…` has 0 hits on the page), publication/update dates; S882 adds visible date + JSON-LD datePublished + Last-Modified; S883/S884 add the verified Wayback `id_` carrier URL and byline/责编 detail | no — adds verified facts; the S883 `http` vs `https` Wayback original is documented by the scout |
| `kind` | S883 `paper`→`docs`; S881/S882/S884 unchanged | no restriction in the kind cell; tier and scope carry the calibration; `docs` is the lane's web-article kind (362 rows) |
| `tier` | unchanged (C, C, B, C) | no |
| `scope` | rewritten: S881/S882/S884 add "never sole support / lead" hedges; S883 narrows B to the author's own testimony | no — restrictions are added; the scholar-conducted rationale moves to `source` and the entry `sources:` line, not dropped |
| `anchor` | replaced by the round-74 located quote(s) + fetch facts | no — the staged anchors were the mispaired/stale spans; the new anchors are verified |
| `teaches` | rewritten to the pages' bytes; tuduku's "six tables" corrected to the five-item note | no |
| `status` | `mined` unchanged | no |
| `opened` | 2026-10-23 → 2026-10-25 (re-opened this round) | no |
| `recheck` | prose curl+grep → `180d`; the stripped prose is reproduced in the lesson's four-row table and the entries' `recheck:` lines | no — the re-verify commands/counts are preserved |
| `used-by` | unchanged path; exactly the citing entry each | no |

The four rows are cited by the admitted entries, so the append satisfies "only cited rows":
`used-by` S881/S882 → base entry; S883/S884 → amend entry; S877 → conlang-scholarship.md plus
the base entry.

### A5 — collision guard with the 0–3-space pattern: survived

Re-derived from base bytes (the guard runs before the append, so the base registry is the input):

```
$ git show f7104cb:corpus/SOURCES.md > /tmp/rev.base-SOURCES.md
$ grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' /tmp/rev.base-SOURCES.md | grep -oE 'S[0-9]+' | sort > /tmp/rev.base-reg-ids
$ comm -12 /tmp/rev.base-reg-ids /tmp/rev.staged-ids > /tmp/rev.base-collisions
$ wc -l /tmp/rev.base-reg-ids /tmp/rev.staged-ids /tmp/rev.base-collisions
804 /tmp/rev.base-reg-ids
132 /tmp/rev.staged-ids
 22 /tmp/rev.base-collisions
$ sha256sum /tmp/rev.base-reg-ids /tmp/rev.base-collisions
94a495c7d634123c0d40e6895b7916892e204f450a536ce00cf4af9aef26ca86
130ec2d15f923b005a9a91f03e8a9a949a9233d8b70f432663d93031ee041721
$ cmp /tmp/rev.base-reg-ids .ufo/waves/round-74/assimilation/reg-ids && echo regOK
regOK
$ cmp /tmp/rev.base-collisions .ufo/waves/round-74/assimilation/collisions && echo collOK
collOK
```

`staged-ids` sha256 `bab11d7d…` matches the lesson and the committed file. The guard proof's
committed fixtures show the required discrimination: 2-space and 3-space planted rows are counted
by the census (805) and caught by item 10 (collisions 23, `S883` present) while the column-zero
pattern misses them (804); 4-space is ignored by both (804/22); real registry 804/22 with no
theme id. The guard's 22 collisions are all cross-namespace, 0 same-document pairs
(`id-renumber-map.json` `numeric_collisions_at_base.same_document_pairs = 0`).

### A6 — quarantine slice: survived

The prompt's awk reproduces 21 rows (18 `payload-absent` + 3 prose "could not be fetched"):

```
$ awk -F'|' -v l='kotodama' '$2 ~ ("`" l "`") && $3 ~ /round[0-9]+/ && $4 ~ /S[0-9]+/ {print $4, $5}' \
    /home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md
 S776 … S778 … S779 … S786 … S787 … S791 … S792 … S795 … S796 … S804 … S814 …
 S816 … S817 … S820 … S823 … S824 … S825 … S827   (18 payload-absent)
 S807` … S812` … S835`                            (3 prose / unreachable-class)
```

S816/S817 are the two register rows touching this theme. They were re-fetched this round with
the browser UA, were byte-identical to the committed round-71 captures (`a3b6640c…`,
`344de345…`), and their quoted spans are absent from the cited URLs (S816's span present once
on the 2022 page; S817's Sowers-Wills span on neither chinawriter page). Both stay REFUSED; the
documents are re-opened as new rows S883/S884 with round-74 located quotes; the four clearing
conditions are recorded (lesson:132-146). No register or campaign file was edited (hashes below).
The other 19 rows were not re-fetched this round and carry the standing round-71 verdicts, which
is compatible with item 10 because none of them is appended: the slice is a quarantine list, and
the full-slice hand-check was completed in the earlier rounds (round-72 lesson: "wave-4
quarantine-first completed by rounds 68-71"). No slice row was adopted.

### A7 — counters at their lands: survived

Run inside my own clones: `/tmp/RevAssimilationFinal.iGg4/lane` (C) and
`/tmp/RevAssimilationFinalCA.Sqek/lane` (Ca); each clone's local `main` was forced to that
claim's lands (`branch -f main <lands>` inside the clone) and `git rev-parse --show-toplevel`
printed the mktemp root before the clone.

Claim C:

```
python3 -B reports/round-74/accept-c.py --root . \
  --lands c4bf61a8d722f9168ce0fd8021a6261c000610c5 \
  --freeze 00c408a0af2fa5ddf65af2224152ce258b26d896 \
  --fleet-root /home/vgpnk/Projects/shokunin
…
LEG PASS CENSUS
     exit=0 last-line=kotodama	ok	/tmp/r74-fleet-…/kotodama-shokunin/corpus/SOURCES.md
LEG PASS SCRATCHMIRROR
LEG PASS COLLCHECK
LEG PASS FROZENCFG
     constants from git show 00c408a0af2f:reports/round-74/claims.json (sha256 270e31790e2932c8)
LEG PASS INDEX
ACCEPT-C-74: PASS legs=13/13
EXIT:0
```

Claim Ca:

```
LEG PASS LEDGER / BASEMISMATCH / REPAIR / ANNOTATE / NOSTUB / APPENDONLY / SEPARABLE / TRACKED / RECEIPTS / FROZENCFG / STAMP
ACCEPT-CA-74: PASS legs=11/11
EXIT:0
```

The counters are unchanged from the freeze to main (`accept-c.py` sha256 `8d30487f…` at
`00c408a`, at `c4bf61a` and at `main`; `accept-ca.py` `8052f1e2…` at freeze and main), so the
frozen claim's rule was not rewritten after data.

### A8 — `considerthese`: survived (absent)

```
$ ls -d considerthese
ls: cannot access 'considerthese': No such file or directory
```

Lesson:183 states the absence and that no proposal is mined.

### A9 — claim-side bytes at main equal claim C's lands: survived

`git diff --stat c4bf61a..main` touches only
`reports/round-74/telemetry/{junk-c,junk-ca,measures-c,measures-ca}.txt` (report-side), plus the
wave-2/scratch files from `1d7add3` and the orchestrator snapshot `92b8d4b` ("not a landing").
`corpus/SOURCES.md`, both entries, the lesson, `SCORECARD.md`, `SKILL.md`, `QUALITY.md` and
`corpus/README.md` are unchanged after `c4bf61a`, so the counter run at `c4bf61a` measures the
current claim bytes.

## Residual risk and verification gaps

- The fleet round report `/home/vgpnk/Projects/shokunin/.ufo/reports/round-74/kotodama.md` does
  not exist at review time. That is where F3's pasted id lists, the quarantine verdict table and
  the `considerthese: absent` line belong; the lesson carries the substance except the lists.
- I did not re-run the CDX "no capture" probes for S881/S882; I verified the live bytes and used
  the round's 13-shape CDX probe with its `example.com` positive control (`ScoutWayback.md`
  §2). The "no capture" ruling therefore rests on the recorded probe, not my own.
- S883/S884 were verified against the committed round-71 captures, which the round-74 scout and
  evidence sha256 show are byte-identical to the live 2026-10-25 fetch; I did not fetch the
  chinawriter pages live.
- The two post-lands telemetry receipts `junk-*.txt` / `measures-*.txt` were added at `1d7add3`
  after the claim's lands; they are report-side and not read by the claim's legs at `c4bf61a`.
- Out of item-10 scope, observed for routing: the lesson's `R74-M4` row still says
  `pending landing` although claim Ca landed at `5e4796c` with the SCORECARD LC-02/LC-03 rows;
  and `.ufo/waves/round-74/counters/junk-r74-run.txt` is truncated in the worktree (F5).

## Fetch log (UA recorded per fetch)

User-Agent for every fetch below: `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML,
like Gecko) Chrome/130.0 Safari/537.36`.

| fetch | HTTP | bytes | sha256 |
|---|---|---|---|
| `GET https://litmemo.com/ja/blog/novel-worldbuilding-guide` | 200 | 101,615 (31,737 transferred) | `441fc921cadc744a7d59f91a055ff2eec1359d24f5c331d783104a1fa334ca64` |
| `GET https://tuduku.space/column/novel-worldbuilding` | 200 | 17,068 (6,260 transferred) | `754f504c34d796f40e86fb0d98c98946e36284c5fae511d7837f442662cfc1b7` |
| `GET http://www.philol.msu.ru/~sidorova/files/conlangs.pdf` | 200 | 1,055,723 | `e512a20dd3eef97ed403bd4191545dea1147279d82b7cced32aaa6037ca595a9` |

No capture, no campaign tool, no install. The chinawriter pages were read from the committed
`round-71/assimilation/fetches/s816.html` / `s817.html` (sha256 equal to the round-74 evidence),
not fetched.
