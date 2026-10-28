# RevQualityFitness — wave-2 falsify: six-month maintainability of the adopted naming-systems entry and its two row claims

Seat: RevQualityFitness (leaf, wave 2, attack-only). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`,
base `211f9526800906e0c585d878d265c37e5e090c15`. Date: 2026-10-27.

Judged objects (read-only):
- staged entry `/home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge/linguistics/naming-systems.amend-2026-10-23.md` (65 lines);
- the lane-rewrite draft it is admitted through: `.ufo/waves/round-77/w1/drafts/corpus/knowledge/linguistics/naming-systems.amend-2026-10-23.md` (123 lines, ScribeEntryA W1 deliverable — the bytes L1 lands);
- CLAIMS-DRAFT.md row claims D1 (line 13) and D2 (line 15);
- W1 receipts `.ufo/waves/round-77/w1/stage/ScribeEntryA/{d1-live.text,d2-live.text}` (fetches dated 2026-10-27).

L1 is not installed: `git -C <lane> rev-parse HEAD` → `211f9526800906e0c585d878d265c37e5e090c15` (HEAD == base),
`git status --porcelain` → only `?? .ufo/waves/round-77/` and `?? reports/round-77/`; `reports/round-77/` holds
only `telemetry/census-start.txt`. No frozen claims.json/ledger/counter exists yet, so entry-level and row-level
claims are judged from the CLAIMS-DRAFT and W1 artifacts only.

## Probe verdicts (the three seat questions)

1. **One amendment within linguistic-cultural province — PASS.** The single adopted entry stays inside the
   onomastic province of `linguistics/naming-systems`: both sources are naming studies (a 漢晉 naming-structure
   history; a female-name lexeme classification), and the census-derived statistics are carried as onomastic
   data with sample scoping, not as demographic findings. Exact lines: draft line 15 `- scope: … it decides no
   world's names and sets no canon.`; line 49 `Eighty-eight is a count inside a corpus, not a claim that
   Chinese has eighty-eight plant words.`; line 51 (sample sizing `2,500 characters … 85,567 females`, cohort
   `born approximately 1900–1980`); §7 row `The inventory's frequency shifted between the two samples |
   indicative, not a measured trend` with the two-sample mismatch named. No drift into era-periodization or
   any sibling territory; couples (draft line 14) name only naming/lexicon/place-name files, both coupled
   paths verified present at base (`git ls-tree 211f9526… -- corpus/knowledge/linguistics/toponymy-place-names.md
   corpus/knowledge/linguistics/semantic-fields-lexicon-building.md` → both listed).
2. **Hands off rather than canonizes — PASS in substance, one defect (F1).** §6 levers are `sheets to fill
   rather than rules to obey … stated as questions`; line 91 worked shape `deciding nothing about any world`;
   §10 hands to `lore-shokunin through the world-bible integration contract` — and that contract name resolves
   in the lane (`git grep -c "world-bible integration contract" 211f9526… -- corpus` hits 4 files, incl.
   `corpus/knowledge/synthesis/naming-canon-workflow.md`). The base entry's own couples line already carries
   the convention (`naming-systems.md:36` tail: `lore-shokunin (canon handoff — this file yields options and
   systems, never canon)`). Defect: F1 below — the handoff sentence asserts a reverse pointer the landed tree
   will not have.
3. **Inference and scholarship distinguished — STRONG, one defect (F2).** §7 is a 9-row calibration table that
   marks what is the article's argument vs this file's method (`A name lexicon is a countable inventory | the
   method both documents use, not a finding either states — the file adopts it as a design method, and says
   so`); the 88-count quote carries its 2008 attribution inside the span and is graded tier B (`reported from
   the author's own 2008 monograph … not re-counted`, lines 13, 47); tier A is scoped per claim, not per
   document (line 13). Defect: line 53's subset sentence (F2).

## Findings

### F1 (MEDIUM) — the handoff asserts a reverse pointer and base-file gains that the declared lands cannot produce

Draft line 14: `- couples: linguistics/naming-systems.md (the entry this amends — its §2 slot table gains a
fusion date and an acquisition channel; its §7 pipeline gains steps 2a and 4a, below)`. Draft line 123 (§10):
`This amendment appends to linguistics/naming-systems.md, which points here through its couples: line.`

Evidence, all at base `211f9526…`:

```
$ git -C <lane> show 211f9526…:corpus/knowledge/linguistics/naming-systems.md | awk 'NR==36' | grep -c "amend-2026"
0        (full line ends: … costume (…), lore-shokunin (canon handoff — this file yields options and systems, never canon))
```

The base entry does not point at any amendment, and the claim's declared lands are exactly one NEW entry
(253→254) plus two S-rows — no base-file edit is declared, so at the revision the round stamps, line 123 is
false of the tree it lands in, and line 14's "gains" claims acquisitions the base file never receives.

This is not a wording convention the corpus lacks: the executed precedent shows what the sentence requires.

```
$ git -C <lane> show 211f9526…:corpus/knowledge/myth-symbol/narrative-structure-frameworks.md | awk 'NR==14' | grep -c "amend-2026"
1        (the base entry's couples line names its landed amend file)
$ git -C <lane> show 211f9526…:corpus/knowledge/myth-symbol/narrative-structure-frameworks.amend-2026-10-23.md | awk 'NR==140'
This amendment appends to `myth-symbol/narrative-structure-frameworks.md`; the base points here through its `couples:` line. …
```

Six-month consequence: the couples graph is the corpus's discovery spine. As drafted, a reader of the base
entry cannot discover this amendment at all, and a reader of the amendment chases a pointer into nothing —
the handoff records an edge that does not exist. Fix, one of two, decided at freeze:
(a) L1 edits `naming-systems.md`'s couples line as an explicitly declared land (as the precedent round's tree
did) and the frozen config accounts for a changed pre-existing entry; or
(b) reword lines 14 and 123 to a one-way pointer, e.g. `the base's couples line does not name this file at
the lands revision; discovery is by this path and the round receipt`. Do not land the sentence as written.

### F2 (MEDIUM) — a cross-corpus subset is stated as the article's own ranking rule (inference dressed as scholarship)

Draft line 53, second sentence: `Seventeen of eighty-eight is the ranking rule, and the article names the
source volume (《姓氏人名用字分析统计》, 语文出版社, 1991) and the census behind it (PRC, 1982).`
Draft line 91 (§6 worked shape): `a culture's plant-class given-name lexicon is counted at 88 members in one
corpus, ranked, and the top 17 re-checked against a second sample forty years later; 6 have vanished, 2 rose
on homophony, 9 fell.`

The two numbers come from two different bases, which the paper itself keeps distinct (W1 receipt
`stage/ScribeEntryA/d2-live.text`):

- line 175-177 (§3): `According to Kałużyńska (2008, pp. 223, 232), there were altogether 88 terms … among
  the names of women figuring in the research material of the work` — and lines 241-243 define that research
  material as `the work "Chinese female namings. Past and Present" (Kałużyńska, 2008)`;
- §4 heading + lead-in: `LIST OF THE 17 MOST COMMON LEXEMES/CHARACTERS … The top lexemes/characters …
  occurring in female names as seen in statistical materials ("Xingshi"), are the following` — the 17 are
  ranked inside Xingshi (1991 volume over the 1982 census), a different corpus from the 2008 monograph's.

The article nowhere derives the 17 from the 88 — the extracted text layer carries `88` on exactly one line:

```
$ grep -n "88" d2-live.text
175:According to Kałużyńska (2008, pp. 223, 232), there were altogether 88 terms
```

So `Seventeen of eighty-eight` and the §6 cycle `counted at 88 … ranked … top 17 re-checked` are this file's
own reconstruction, presented inside a quoted, S898-cited paragraph as if the article held the numbers
together (§7's `the method both documents use` row repeats the single-pipeline reading). A reader citing the
entry will report that the 2025 article ranked an 88-term inventory down to 17 — false. Fix: at line 53, name
the two bases and mark the identity as the file's reconstruction; at line 91, say the cycle is assembled from
figures no single study produced end-to-end (count in one corpus, rank in another sample's statistics,
re-date against a third list) — which is the actually more maintainable lesson for the instrument.

### F3 (LOW) — the recheck block is internally inconsistent in two cells (draft lines 6-9, one edit)

(a) Line 6: `Both documents answered HTTP 200 to a plain client on 2026-10-27` — but line 8, two lines
below: `the plain client curl/8.7.1 answered the same URL with HTTP 403 and 162 bytes`. The same term names
two different clients; a +180d re-opener running line 6's belief against D1 gets a 403 and must reverse-
engineer the terminology from line 8. Sharpen line 6: `plain, automation-free request (D1 under the
browser-shaped User-Agent, D2 under curl)`.
(b) Line 6 names the S898 fallback capture `20251231111748`, while line 4 and §8 line 113 designate
`20260901045105` as the byte-identical pair — line 113: `Capture 20260901045105 is byte-identical to the
live PDF … so it is the capture the row should pair with the live URL; 20251231111748 is an earlier OJS
regeneration`. Both captures locate the spans, so this is guidance, not error — but the entry's own recheck
line sends a re-opener to the witness §8 just disqualified. Point line 6 at `20260901045105`.

### F4 (LOW) — the S898 recheck command writes into the working directory

Draft line 9: `curl -sS -o onom69.pdf …` — executed at the lane root (the natural place a future session
runs a lane recheck) it drops an untracked file into the repo. Pipe to pdftotext's stdin
(`curl -sS … | pdftotext -layout - -`) or name an explicit scratch path.

## Confirmed-fixed (staged defects this seat re-verified as repaired in the draft)

- Staged lines 7/47 recheck pointers (`round 4's/3's SOURCES-PROPOSED.md`): the file exists nowhere —
  `git ls-tree -r --name-only 211f9526… | grep -ci "SOURCES-PROPOSED"` → `0`; `find
  /home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge -iname "*SOURCES-PROPOSED*"` → nothing. Draft
  lines 6-9 replace it with self-contained argv. ✓
- Staged lines 8/48 ground pointers (`round 3's/2's CANNOT-ANSWER`): `git grep -c "CANNOT-ANSWER"
  211f9526… -- corpus` → exit 1, no match; same `find` → nothing. Draft line 10 grounds on the base entry's
  actual §2/§6 gaps. ✓
- Staged lines 33-65 (the retained "Superseded passage" block citing S886/S888/S889/S890/S891/S896, which
  name six different documents in the lane registry — W1 F1): dropped; draft §9 (lines 117-119) records the
  drop by subject and round, never by id, and states `Nothing in §1–§8 depends on it.` ✓
- Staged line 21's dangling couples path `culture-material/era-periodization-models.amend-2026-10-23.md`:
  replaced by two lane-existing paths (verified by ls-tree, probe 1). ✓
- Cited-lines lint re-run by this seat, not inherited:
  `python3 -B tools/check-cited-lines.py .ufo/waves/round-77/w1/drafts/corpus/knowledge/linguistics/naming-systems.amend-2026-10-23.md`
  → `CITED-LINES: 0 finding(s) in 1 file(s)`, exit 0. ✓
- Draft line 3's page-anchored cells spot-checked against `d1-live.text`: title line 1 carries
  `中国社会科学院历史研究所`, line 217 `发布日期：2021-03-16`, closing lines 2944-2947
  `來源：《歷史研究》/2012/年第/1` — the draft's `(posted 2021-03-16; the page's own closing line reads
  來源：《歷史研究》2012 年第 1 期)` is faithful; the draft's `served as a reprint by
  中國社會科學院古代史研究所` anchors to the page footer, line 2952 `版权所有： 中国社会科学院古代史研究所`.
  Note for the row writer: the same page carries BOTH institute names (title bar: 历史研究所; footer
  copyright: 古代史研究所 — a 2019 CASS renaming artifact), while CLAIMS-DRAFT D1 says
  `中国社会科学院历史研究所`. Bind each cell to the page element it reads, or a future verifier grepping the
  other element will file one of the two as misdescribed. ✓ with note.

## Residual risk and verification gaps

- No live fetch was made by this seat; every artifact quote comes from W1 stage receipts dated 2026-10-27
  (same day as the draft's `verified-at`). A fresh fetch could differ; the rows' recheck cells own that risk.
- Numbers cited from W1 reports (word floor 352/208, 253→254, 820→822) are their measurements, not re-derived
  here (criterion 29 hygiene: not attributed to lane bytes by this seat).
- claims.json / ledger.json / counters do not exist yet (L1 not installed); whether F1 is fixed by a declared
  base-file land or by rewording is a freeze-time decision this seat cannot bind. F2/F3 are pure draft edits
  and are reachable before freeze.
- Whether the Gate's ≤25-word evidence windows bind the draft's §4/§5 quote lines (47, 49, 51, 53, 55, 59, 61)
  is the L1's freeze work, unrun here; the 17-word 88-count span already carries its attribution inside the
  window (line 47).

## Scratch and installs

Scratch `/fast/scratch/hyaku/kotodama-r77/RevQualityFitness` was never created (first mkdir attempt failed on
a missing cwd; not retried — `ls` confirms `No such file or directory`), so there is nothing to delete;
sibling seats' scratch dirs were not touched. No tool installed, no pacman run. The only lane write is this
report file.
