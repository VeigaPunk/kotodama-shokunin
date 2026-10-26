# RevLessonGate — round 74, wave 2 (falsify) — the round-74 lesson as a Gate

Seat: `RevLessonGate` (leaf; no delegation). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`
(read-only apart from this file). Base `f7104cbce186bc2e1522abf0cfd619cc834628bb`; operative freeze
`00c408a0af2fa5ddf65af2224152ce258b26d896`; claim C lands `c4bf61a8d722f9168ce0fd8021a6261c000610c5`;
claim Ca lands `5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3`; lane `main` at review `1d7add3`.

Scope: `corpus/lessons/round-74.md` as a Gate under `/home/vgpnk/Projects/shokunin/CORPUS.md`
SOURCES rules 1–2 and prompt item 10 (`.ufo/prompts/kotodama-round-74.md:440-545`): admit-row
grounding, ≥1 admit/≥1 reject, stripped-recheck record, S877 old→new, collision guard, Quarantine,
Mistakes table, census. The claim's rule is frozen; nothing here edits it.

**Verdict: the claim survives on its core.** All five Gate rows carry URL + access date + a
≤25-token located quote + a locator, and I re-located every quote against freshly fetched bytes;
the registry rows are schema-valid and the S877 `used-by` change is exactly the logged old→new;
the collision guard re-derives 804/132/22 with the stored sha256s; the Quarantine slice re-derives
21 rows with the 10/7/4 verdicts and the four clearing conditions hold; the census re-runs exit 0
and the row counts are 804 → 808. Eleven findings below are record/narrative defects, not a
failed admission. No BLOCKER.

## Fetch log (hygiene, QUALITY 21/22/24)

Every fetch used the browser-shaped UA
`Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`,
`curl -sS -L --compressed`, access date 2026-10-25 local (2026-10-26Z early hours).

| URL | HTTP | transferred | body bytes | body sha256 |
|---|---|---|---|---|
| `https://www.chinawriter.com.cn/n1/2025/0605/c404024-40494534.html` | 200 | 16723 | 48536 | `a3b6640c…bee94d` (matches evidence) |
| `https://www.chinawriter.com.cn/n1/2022/1207/c404024-32582252.html` | 200 | 21341 | 62604 | `344de345…d3d659` (matches evidence) |
| `https://litmemo.com/ja/blog/novel-worldbuilding-guide` | 200 | 31737 | 101615 | `441fc921…ca64` (matches evidence) |
| `https://tuduku.space/column/novel-worldbuilding` | 200 | 6260 | 17068 | `754f504c…c1b7` (matches evidence) |
| `http://www.philol.msu.ru/~sidorova/files/conlangs.pdf` | 200 | 1055723 | 1055723 | `e512a20d…95a9` (matches evidence) |
| `https://sanders.phonologist.org/Papers/anderson-etal-cjl-sotl.pdf` (S880 check) | 200 | 193610 | 193610 | `26dbcf2c…0d535` |

No walls, no retries needed. I ran no CDX probe; the lane's own `ScoutWayback.md` did (canonical
slug probes plus an `example.com` positive control, §2), which is the instrument the entries' "no
capture" rulings need and which the lesson does not mention. No tool installed or upgraded.

## Findings

### F1 — HIGH — the S899/S900 rejection rows and the S883/S884 "re-quote" clauses misstate the staged spans

Attack: the four reject rows' `reason` cells and the two admit rows' evidence-column clauses.
The lesson (`corpus/lessons/round-74.md`, "Rejections") says:

- "staged S899's quoted span was absent from the page it was bound to (register S816 mispairing; the span belongs to the 2022 interview)"
- "staged S900's quoted span was the Sowers-Wills clause, absent from this page (register S817 mispairing)"
- and the Gate table's S883/S884 rows: "re-quote: the staged span was absent …" / "… the staged span was absent (register Sowers-Wills span mispaired to this URL, R71 refusal)".

Raw check against the two served pages (my own fetch, sha-identical to the evidence bodies):

```
$ grep -o '非凡特性来自最初造物主' w2025.html | wc -l   -> 1
$ grep -o '非凡特性来自最初造物主' w2022.html | wc -l   -> 0
$ grep -o '这个我肯定考虑过' w2025.html | wc -l        -> 0
$ grep -o '这个我肯定考虑过' w2022.html | wc -l        -> 1
```

Staged row cells (escaped-pipe-aware parse of `merge/kotodama/SOURCES.append.md`):

- S899 cell 6: `the 「非凡特性来自最初造物主」 answer of 爱潜水的乌贼 — page as served 2026-10-23` → present on the 2025 page (1 hit).
- S900 cell 6: `the 「这个我肯定考虑过。我自己就是资深读者…」 answer of 爱潜水的乌贼 — page as served 2026-10-23` → present on the 2022 page (1 hit).

The lane's own wave-1 scout says the same, and says the refusals are register-side:
`.ufo/waves/round-74/w1/ScoutQuarantine816817.md` §4: "staged S899 (2025 URL) is cited for
`非凡特性来自最初造物主` … and staged S900 (2022 URL) for `这个我肯定考虑过…` … each pairing is
correct against the live bytes". The absent spans are the **register** quotes: register S816's
`这个我肯定考虑过…` is bound to the 2025 URL (0 hits there) and register S817's Sowers-Wills clause
is bound to the 2022 URL (0 hits for `Sowers`, `Wills`, `Phonology`, `inside out`); the Sowers-Wills
clause belongs to lane S880, whose PDF I fetched (`pdftotext` hits at lines 146, 158, 189). The
lesson's own M5 row agrees: "The fabrication class is the register pair as filed, not the pages and
not the staged row text."

So the refusals stand, but the stated reasons are false about the staged rows; the staged rows'
own cited spans are present on the pages they name. A round-75 re-check of "the reason cleared"
would re-quote the wrong thing (the staged anchor), not the register binding.

Correction: say "the *register* quote bound to this URL was absent (S816's `这个我肯定考虑过…` on the
2025 URL; S817's Sowers-Wills clause on the 2022 URL); the staged row's own anchor span is present,
and the new row re-quotes a fresh body sentence from the page". Apply the same wording to the two
evidence-column clauses, and drop the R68/R71 round labels from the staged-row sentences (the
register rows were refused in R68/R71; staged S899/S900 were refused in round 72 —
`corpus/lessons/round-72.md:60`).

### F2 — MEDIUM — the Gate says the EVIDENCE floor is unenforced; the frozen counter enforces it

Attack: Gate note 2, "`accept-c.py`'s `leg_evidence` does not read the floor, so the limb is vacuous
here (R74-M6)." The frozen counter's `_evidence_core` reads and enforces the scope:

```
$ sed -n '/def _evidence_core/,+70p' reports/round-74/accept-c.py
    Window scope (claim C, final): `excerpt` requires a window of at least 4096
    characters; `whole-document` is allowed only when the stored window is
    shorter than 4096 characters and its length equals the recorded
    `visible-chars:`. …
    if scope == "excerpt":
        if len(window) < MIN_WINDOW_CHARS: … bad
    elif scope == "whole-document":
        if len(window) >= MIN_WINDOW_CHARS: … bad
        if visible.isdigit() and int(visible) != len(window): … bad
```

`leg_evidence` calls `_evidence_core` for every row before coupling the window to the Gate quote.
The frozen M6 fix says the same ("the counter and the evidence tool enforce it"). The S882 capture
passes the whole-document branch: `window: chars=2953 min=4096`, `window-scope: whole-document`,
`visible-chars: 2953`, and my extraction of the page is exactly 2953 chars (631+33+2289).

Correction: "the frozen counter enforces the whole-document exception and the S882 window satisfies
it; the drafted counter (before the pre-data amendment) did not read the floor". M6's fix is
correct; the Gate note is stale and contradicts it.

### F3 — MEDIUM — the triage omits the package's four `amendments/` payloads (40 vs 44 files)

Attack: "2 adopted / 4 path-present … / 34 refused, of the 40 staged knowledge files" and the
family table. The package has two payload trees:

```
$ cd /home/vgpnk/Projects/shokuknow/merge/kotodama && find knowledge -type f | wc -l   -> 40
$ find amendments -type f | wc -l                                                      -> 4
$ find amendments -type f
amendments/corpus/knowledge/culture-material/calendar-festival-systems.md
amendments/corpus/knowledge/culture-material/era-periodization-models.md
amendments/corpus/knowledge/linguistics/conlang-methodology.md
amendments/corpus/knowledge/linguistics/naming-systems.md
```

All four differ from the lane's bytes (staged vs lane sha256, e.g. naming `6a758af1…` vs
`d972a1d6…`), and they are the append payloads `MERGE-REPORT.md` §Adopt checklist 5 says must be
appended to existing lane entries. The lesson's family table lists only the 40 `knowledge/` files;
the four `amendments/` payloads are neither adopted, path-present, refused, nor in "Routed to round
75". The naming row is also misdescribed: `find knowledge amendments -name '*naming-systems*'`
returns **12** files (base + 11 amendments), while the table says "base plus 10 amendments | 11";
the 11 `knowledge/` files are all amendments and the base is the 12th, untriaged file. Calendar is
4 files (base + 3), era 3 (base + 2), conlang-methodology 2 (base + amend); the table counts 3, 2,
1.

Correction: state that the 40-file universe is `merge/kotodama/knowledge/` only, and route the four
`amendments/` payloads with a verdict (they are amendment payloads for existing entries, not new
files); fix the naming/calendar/era compositions. The frozen counts (claims.json
`total_staged_files: 40`) are not edited by this finding; it is a scope disclosure the next round
needs.

### F4 — MEDIUM — M4's "`grep -c scenarios SCORECARD.md` = 0" is false at the C landing and at HEAD; the state is stale

Attack: `## Mistakes` row R74-M4 evidence and state. The Ca landing (5e4796c) precedes the C landing
(d7a3840/c4bf61a) and already added the LC-02/LC-03 correction rows:

```
$ git show f7104cb:SCORECARD.md | grep -c scenarios   -> 0
$ git show 5e4796c:SCORECARD.md | grep -c scenarios   -> 2
$ git show d7a3840:SCORECARD.md | grep -c scenarios   -> 2
$ grep -n 'scenarios' SCORECARD.md
1443:| LC-02 | 9 | 10 | git grep -h -o -E 'SELFTEST OK. [0-9]+ scenarios' f7104cb… -- reports/round-73/telemetry/selftest-r3.txt |
1444:| LC-03 | 9 | 10 | git grep -h -o -E 'SELFTEST OK. [0-9]+ scenarios' f7104cb… -- reports/round-73/telemetry/selftest-r3.txt |
```

The other limbs are true: `LOG.md:4297` and the fleet report `.ufo/reports/round-73/kotodama.md:10`
both say "Ca 9 scenarios"; `reports/round-73/telemetry/selftest-r3.txt:6` says "SELFTEST OK: 10
scenarios". But the SCORECARD limb was already 2 when the lesson landed, and the fix had landed at
5e4796c, not "pending landing".

Correction: "at base 0; the Ca landing's correction rows add 2 `scenarios` occurrences
(SCORECARD.md:1443-1444); the pair is closed at 5e4796c", and set the state to fixed at the Ca
landing.

### F5 — LOW/MEDIUM — R74-M7 and the Gate note call a 108-character clause "the sentence", and say the full sentence is on the evidence `quote:` line

Attack: the S877 trimming note and R74-M7. The 108-character, 15-token span is the comma-clause
(correct numbers), not the sentence; the sentence (to the period) is 285 chars / 37 tokens:

```
$ python3  # pdftotext of the fetched PDF
sentence: 'Язык – главный инструмент построения вымышленных миров, дающий названия для их
природных и социальных реалий, собственные имена, позволяющий создать для этих миров духовную
культуру (многие вымышленные миры имеют художественную литературу – поэзию и прозу на
сконструированных языках).'
chars 285 tokens 37
cell chars 54 tokens 7
clause chars 108 tokens 15
```

The evidence file's `quote:` line is the 54-char clause
(`reports/round-74/evidence/S877.txt`, last line), and its `locator:` line carries only a truncated
fragment with `…`; the full sentence is not stored. The long form therefore fails both limbs, not
"passes the token limb". The cell quote itself is valid (7 tokens, 54 chars) and the trim decision
stands.

Correction: "the located span is a 108-character comma-clause of a 285-character, 37-token
sentence; the cell and the evidence `quote:` line carry the 54-character, 7-token first clause; the
full sentence is not stored".

### F6 — LOW — "S877's round-73 evidence file … 1564 B" is wrong; the file is 2417 B

Attack: Gate note 3. `reports/round-73/evidence/S877.txt` is 2417 bytes at base, freeze and HEAD:

```
$ for rev in f7104cb 00c408a main; do git cat-file -s $rev:reports/round-73/evidence/S877.txt; done
2417
2417
2417
```

(The collapsed-window part alone is 1615 bytes including its newline, not 1564.) The rest of the
note (round-73 grammar, one collapsed paragraph, p.10 Chapter-1 quote) is true.
Correction: 2417 B.

### F7 — LOW — "false at base and at worktree HEAD … no lane row carries litmemo, tuduku or chinawriter" is false at the delivered HEAD

Attack: the collision-guard paragraph. At the base it is true; at the delivered HEAD the adoption
itself creates the hits:

```
$ for h in litmemo tuduku chinawriter; do printf '%s base=' $h; git show f7104cb:corpus/SOURCES.md | grep -c $h || true; printf ' head='; grep -c $h corpus/SOURCES.md || true; done
litmemo base=0 head=1
tuduku base=0 head=1
chinawriter base=0 head=2
$ git show f7104cb:corpus/SOURCES.md | grep -cE '^\| *S(883|884|899|900) *\|' -> 0
$ grep -cE '^\| *S(883|884|899|900) *\|' corpus/SOURCES.md -> 2
```

The check is also run against `assimilation/reg-ids`, a base snapshot
(`id-renumber-map.json: "head_at_write": "f7104cb…"`), so it cannot establish a HEAD property.
Correction: "false at base and at the pre-append worktree (`head_at_write` f7104cb); the adopted
rows S881–S884 create the litmemo/tuduku/chinawriter hits at lands".

### F8 — LOW — "8 of 132 staged rows have 11 cells" re-derives as 7

Attack: the guard-mutations paragraph's parenthetical. A mirror registry with the base registry
plus the 132 staged rows gives exactly the report's E01 count, and 132 − 125 = 7:

```
$ python3  # insert the 132 staged rows into the base Registry table, before "## Paths"
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file mirror2.md; echo exit=$?
    125 E01
      7 E09
    882 E11
     28 W04
exit=1
$ awk -F'|' '/^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|/{print NF}' SOURCES.append.md | sort | uniq -c
      7 13
    115 14
      9 15
      1 16
```

`MutRegistryCollision.md` itself prints "E01×125" and then says "only 8/132" — the 8 is one high.
Correction: 7 (or cite the census's E01 count and stop deriving a second number from it).

### F9 — LOW — M9 cites the wrong revision for the "post-repair control"

Attack: R74-M9 fix, "`telemetry/controls-ca.txt` at `00c408a0…` is the post-repair control". The
blob at 00c408a is the first-freeze run; the operative-freeze run is committed at 5e4796c:

```
$ for rev in 3595c91 00c408a 5e4796c; do git rev-parse $rev:reports/round-74/telemetry/controls-ca.txt; done
c334e826e352455b3ffcf7d9244815ebb8207ca1
c334e826e352455b3ffcf7d9244815ebb8207ca1
8544846180889bf242ac8895fb231a6b7b0031f4
$ git show 00c408a:reports/round-74/telemetry/controls-ca.txt | head -1
# controls-ca.txt — claim Ca do-nothing controls (round 74), measured at freeze de93d91cab5a… by the freeze-installed counter
$ git show 00c408a:… | grep 'counter sha256 (self)' | head -1
# counter sha256 (self): dd755893f72cb8e93b8c53577188ad3b868bd3367c76b0ab789e19227ca520ec
$ git show 5e4796c:reports/round-74/telemetry/controls-ca.txt | head -1
# controls-ca.txt — claim Ca do-nothing controls (round 74), measured at freeze 00c408a0af2fa5ddf65af2224152ce258b26d896 by the freeze-installed counter
$ git show 5e4796c:… | grep 'counter sha256 (self)' | head -1
# counter sha256 (self): 8052f1e25c366a18ccb28e1c47931fd1cdd91db042153fdda570fd9f0fa8470f
```

The 00c408a file is absent at de93d91c and was added at the re-freeze, but its content is the
de93d91c run (freeze line, counter sha); the 00c408a-run receipt is at 5e4796c. The substance
(the do-nothing control's SEPARABLE red is caused by the earlier receipt in the scanned set; the
real green is `measures-ca.txt` = `ACCEPT-CA-74: PASS legs=11/11` at 5e4796c) holds.
Correction: "`controls-ca.txt` at 5e4796c is the operative-freeze control; the 00c408a blob is the
first-freeze run carried forward".

### F10 — LOW — the S884 "para 35" locator depends on counting a commented-out `<p class="browserupgrade">`

Attack: the S884 admit-row locator. Under the amendment's stated recheck scheme ("para n =
the nth non-empty p …, para 1 = the browser-upgrade notice"), the quote is para 35 (the 14th 乌贼
answer). Counting only served/rendered paragraphs gives para 34:

```
$ python3  # 2022 page, non-empty <p> in document order
all p 72 nonempty 72
乌贼 answers 31; 14th answer at index 34
quote para index 34: '乌贼：这个我肯定考虑过。…把它放在前面大概20章之内慢慢来，我觉得是问题不大的。'
```

The browser-upgrade `<p>` is inside a conditional comment (`<![if lt IE 9]>…<![endif]-->`); a
reader who ignores comments lands one lower. The "14th 乌贼 answer" anchor is unambiguous, so this
is a reproducibility nuisance, not a wrong verdict.
Correction: state the counting scheme in the Gate row (or write "para 34 rendered / 14th 乌贼
answer").

### F11 — LOW — the census receipts do not carry the row counts the lesson attributes to them

Attack: "Before: exit 0, **804 rows** (`reports/round-74/telemetry/census-start.txt`). After: exit 0,
**808 rows** (`…/census-end.txt`)". Both files end with `exit=0` and the `ok` line; neither prints a
row count. The counts are true and I re-derived them:

```
$ git show f7104cb:corpus/SOURCES.md | grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' -> 804
$ git show main:corpus/SOURCES.md     | grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' -> 808
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama; echo exit=$?
… 3 W01, 28 W04, ok line … exit=0
```

but the parenthetical attribution is loose under CORPUS "a count carries its command".
Correction: add the row-count command to the receipts, or cite the grep beside the census file.

## Attacks that FAILED (the claim survived), with the evidence

1. **Every admit row has URL + access date + ≤25-token quote + locator.** Re-fetched all five
   sources and re-located every quote independently: S877 at PDF page 7 (the `Page 7` marker in
   `pdftotext`), 7 tokens / 54 chars in the cell; S881 the 2nd sentence of the paragraph under
   `h3 「3. 外側の層へ因果をつなぐ」` (1 hit, 1 whitespace token / 43 chars); S882 item 5 of the
   `「世界観設定の5要素」` box (1 hit, 33 chars), whole page extraction 2953 chars; S883 P68 of
   `div.end_article` (1 hit, 32 chars); S884 the 14th 乌贼 answer, final sentence (1 hit, 27
   chars). All five access dates are 2026-10-25. S882's 631+33+2289=2953 arithmetic and window
   geometry are exact.
2. **≥1 admit and ≥1 reject.** 5 admits / 4 rejects, each reject carrying a probed URL, reason and
   flip.
3. **Recheck prose stripped is recorded.** The four staged rows carry the exact escaped-pipe curl
   cells the table quotes (`自然環境` → 4, `設定ノートの構成例` → 1, `先做的是世界观` → 1,
   `20章之内慢慢来` → 1), split to 12 cells under awk (NF=14); the landed rows are `180d`.
4. **S877 `used-by` old→new exact.** Cell-level diff base→HEAD is empty for cells 1–10 and changes
   only cell 11 to `corpus/knowledge/linguistics/conlang-scholarship.md,
   corpus/knowledge/culture-material/worldbuilding-setting-practice.md`; the separator is the
   registry's own `, ` convention (S001–S003 multi-path rows). Base row 832 has book/B/mined/
   2026-10-25/180d as the lesson says.
5. **Collision guard.** Re-derived from the base registry and the current package:
   `reg-ids` 804, `staged-ids` 132, `collisions` 22 (`comm -12`), all three `cmp`-equal to the
   stored files and sha256-equal (`94a495c7…`, `bab11d7d…`, `130ec2d1…`); the URL join over the 22
   colliding ids gives 0/22 same-document. The staged-entry id counts the map predicts are exact:
   base entry S882×4, S883×4, S884×4; amend S899×3, S900×3.
6. **Quarantine.** The prompt awk re-derives 21 slice rows (18 `payload-absent`, 3 unreachable);
   the round-71 table reproduces 10 PRESENT / 7 REFUSED / 4 UNVERIFIABLE = 21, and
   `ScoutQuarantine816817.md` §5 lists the same table; S816/S817 are unchanged base→HEAD
   (`git diff … | grep '^[-+]\| S81[67] '` empty); the two register quotes are absent from the URLs
   they are bound to (`这个我肯定考虑过` 0/1, Sowers-Wills 0/0) and the Sowers-Wills clause is in the
   S880 PDF; the two clearing-condition documents are re-opened as S883/S884 and the quote is
   located from the round-74 capture (my re-fetch is byte-identical and the quote is unique on each
   page).
7. **`## Mistakes` shape.** All ten rows carry class · evidence · captured-by · fix (classes from
   the §5 vocabulary). M1's six freeze blobs equal the ledger's `must_track`/`content_pins` sha256
   (`CritEntryAmendFinal 290a6ccd…`, `ExecSelftestAll dfc8fe0d…`, `ScribeLogScorecard db254d88…`,
   `SimplifierEntries 9469d4d6…`, `drafts/log-entry 079728a5…`, `RevengerOrigins 7d145919…`;
   the last is absent at base). M2's receipts are the claimed PASS-at-lands stdout
   (`ACCEPT-C-73: PASS legs=11/11`, `ACCEPT-CA-73: PASS legs=9/9`). M3's junk receipts show no
   accepted junk landing (C: J1/J2/J3/J9 all FAIL; Ca: J4/J4b/J5/J6/J7/J8/J9 all FAIL). M8's
   selftest receipts print `SELFTEST: 69/69 scenarios` and `SELFTEST OK: 179 checks across 41
   scenarios reported-fail=0`. M10's two postwave files exist and the two round-73 files match the
   base blob (empty diff base→HEAD).
8. **Census.** The exact command re-runs exit 0 with 3 W01 and 28 W04; base 804 rows, lands 808;
   the W01 rows are S881/S882/S884, the tier-C rows.
9. **Base counts in the claims line.** `git ls-tree -r --name-only f7104cb:corpus/knowledge | wc
   -l` = 247; `grep -ciE 'worldbuilding-setting'` = 0; registry hits for litmemo/tuduku/chinawriter
   = 0; S883/S884/S899/S900 rows = 0.
10. **The four path-present files differ in all four and are untouched** (staged/lane sha256 differ;
    `git diff base..HEAD` for the four paths is empty).

## Verification gaps / unrun checks

- **The two frozen counters were not re-executed by this seat.** Their committed receipts are
  `reports/round-74/telemetry/measures-c.txt` (`ACCEPT-C-74: PASS legs=13/13`) and
  `measures-ca.txt` (`ACCEPT-CA-74: PASS legs=11/11`); I read them, and I independently verified the
  counting legs they overlap with (Gate quotes, evidence windows, registry rows, census) above. My
  clone attempt failed on `materialize f7104cb…` because `/tmp` is 100% full (220 MB free of 128 GB)
  from other seats' fixtures; I removed my clone and archive. The row-count and census checks were
  re-run directly. An unrun counter is not a passed counter; the PASS lines above are receipt
  claims, not this seat's re-execution.
- **No CDX probe was run by this seat**; the lane's `ScoutWayback.md` did canonical-slug probes with
  an `example.com` positive control and I read it. The lesson's Gate doesn't mention the probe, but
  the entries' "no capture" rulings are supported by that file.
- The `8 of 132` count was reproduced only through the mirror-census E01 count (125) and awk field
  counts; the exact mirror the report used is not preserved (`MutRegistryCollision.md` fixtures were
  in `/tmp`), so the one-off is inferred, not replayed.
- The "no seat scored landed data at any of the three freezes" negative has no sweep in the lesson
  and I did not attempt to enumerate seats' scoring times.
- I did not re-audit the campaign's quote-lint tool or the register generator; R74-M5's mechanism
  was checked in `census-adjudication.json` (S758/S759 `binding: id`, each `line` naming the next
  row), not in the generator.

## Tooling

No install/upgrade. Scratch: `/tmp/RevLessonGate/` (fetches, extractions, mirror); nothing written
under the lane except this report. The clone attempt under `/tmp` was removed; other seats' `/tmp`
fixtures were left untouched.

Disclosure: the first `write` of this report resolved against the session cwd and landed at
`/home/vgpnk/Projects/shokunin/.ufo/waves/round-74/w2/RevLessonGate.md`; I copied the bytes here and
removed that file, restoring the fleet-root tree. `RevScorecardCorrections.md` in the same fleet-root
directory is another seat's file and was left untouched.
