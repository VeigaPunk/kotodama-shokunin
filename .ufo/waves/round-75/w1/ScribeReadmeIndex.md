# ScribeReadmeIndex — round 75, wave 1

Seat: `ScribeReadmeIndex` (leaf scribe). Lane `kotodama-shokunin`, base
`f556d1049fe651d3d63975600b13acd9fb686f15`. Report only: no product byte, no counter, no config
was edited; the artifact is a draft the L1 lands.

## 1. Behavior — what was produced

One file: `.ufo/waves/round-75/drafts/readme-rows.md` (579 lines). It drafts the whole
`corpus/README.md` change set for round 75, as exact bytes plus anchors plus a re-runnable
check, in seven sections. Contents by ticket item:

| ticket item | in the draft | owner label |
|---|---|---|
| (1) `## myth-symbol/` rows for the narrative-structure entries | §2.3, two rows, after the `myth-ritual-theories.md` row | claim C (`INDEX`) |
| (2) the four missing index rows (`conlang-scholarship.md`, its `amend-2026-10-23`, `heritage-taxonomy-models.md`, its `amend-2026-10-24-r13`) | §2.1 (2 rows, `linguistics/`) and §2.2 (2 rows, `culture-material/`) | claim Ca (`REPAIR`, pairs L75-02/L75-03 + the L75-04 sweep receipt) |
| (3) heading repairs | §2.4: `## linguistics/ (30)`→`(32)`, `## culture-material/ (36)`→`(40)`; **plus** a third, `## myth-symbol/ (29)`→`(31)`, flagged conditional | the first two are Ca's (`expected_after` tokens 32/40); the third is C's and is a rule decision, §6.1 |
| (4) appended footer | §2.5: `Total knowledge entries: 251.` + `Counts checked 2026-10-27 … (total 251 files; directory totals 32/31/40/29/24/95).`, N-parameterised (`249+N`, `32/(29+N)/40/29/24/95`) | claim C (`INDEX`) |

Rows are byte-exact and section-ordered: 6 rows total, each `- \`name.md\` — <entry's own
`- topic:` text>`. The two narrative rows were bound to the entry scribes' own 2026-10-27 drafts
(`.ufo/waves/round-75/drafts/narrative-structure-frameworks{,.amend-2026-10-23}.md`, 906 and 359
chars, one physical line each), not to the staged shokuknow text — the staged base topic
("the Western framing claim that round 1's entry had to assert from memory …") is
entry-relative and was rejected for that reason. The base entry's topic was revised mid-seat
by its scribe: 892 chars with "carried by one Western row at notice scope" → **906 chars with
"carried by one Western row at the scope the Gate locates"** (the page-level text proved
locatable on S885, so a notice-scope claim would assert a narrower scope than the Gate keeps).
The draft carries the 906-char version, records the supersession in §2.3, and was re-verified
after the change (both shipped checks green, §2 below). A conditional third row for
`.amend-2026-10-23b.md` (S/Z five codes) is drafted in §2.3a for the case that the L1 adds it to
claim C's `entries` before the freeze (N=3 → 252 files, `32/32/40/29/24/95`).

Nothing older is edited: all four existing `Counts checked` readings, the round-73 block and
the round-74 block stay byte-identical; the new block is a pure EOF append and deliberately
carries no row-shaped line.

## 2. Gates and controls actually exercised (all read-only over the lane)

Measured at base, 2026-10-27, in the lane:

1. **Base instrument state.** `python3 -B reports/round-28/readme/sweep.py --json` →
   `ok:false`, `total_files 249`, `total_rows 247`,
   `missing_from_index` = the four files, `orphan_rows` =
   `civilizations/conlang-scholarship{,.amend-2026-10-23}.md`, `header_drift`
   `linguistics 30/32` + `culture-material 36/40`, footer `243` vs `249`,
   `totals_line 243`, `topic_mismatch []`.
2. **Six-variant sweep matrix** (draft applied to a copy of the base README; a scratch copy of
   `corpus/knowledge` with the two entry drafts = 251 files; `sweep.py`'s own
   `disk_files`/`topic_of`/regexes, with two switches — partition ends at any `^## ` heading;
   last `FOOTER_RE`/`TOTALS_RE` match instead of first):

   | variant | missing | ghosts | mismatch | drift | footer | totals | ok |
   |---|---|---|---|---|---|---|
   | base README, unrepaired | 6 | 2 | 0 | 3 partitions | 243≠251 | 243 | False |
   | draft applied, unrepaired | 0 | 2 | 0 | {} | 243≠251 | 243 | False |
   | applied, last-footer only | 0 | 2 | 0 | {} | [] | 251 | False |
   | applied, heading-boundary only | 0 | 0 | 0 | {} | 243≠251 | 243 | False |
   | **applied, both switches** | 0 | 0 | 0 | {} | [] | 251 | **True** |
   | applied, both switches, E3 (myth-symbol heading) dropped | 0 | 0 | 0 | `myth-symbol 29/31` | [] | 251 | False |

   Green-row partitions: `linguistics 32, myth-symbol 31, culture-material 40, synthesis 29,
   verification 24, civilizations 95`, rows == files == 251, footer vector
   `[32,31,40,29,24,95]`.
3. **The two shipped scripts were executed, not asserted** — extracted from the draft file and
   run on a scratch pseudo-lane (`corpus/README.md` + `corpus/knowledge` + a copy of `sweep.py`):
   - §4.2 rows-bound: `OK hits=2` ×2, `OK hits=1` ×4, `ROWS-BOUND: PASS`, exit 0;
   - §4.6 index self-check: green tree → `INDEX-SELFCHECK: PASS`, exit 0; do-nothing control
     (`f556d10` README over the 249-file base tree) → `FAIL`, exit 1, naming the four missing
     files, the two drift partitions, `footer 2026-10-25 243 [30,29,36,29,24,95]`,
     `totals 249`; topic mutant (`how three` → `how four`) → `FAIL`, exit 1,
     `mismatch ['myth-symbol/narrative-structure-frameworks.amend-2026-10-23.md']`; ghost mutant
     (row naming `narrative-structure-frameworks-ghost.md`) → `FAIL`, exit 1,
     `ghosts ['myth-symbol/narrative-structure-frameworks-ghost.md']`.
4. **Row binding, byte level.** All 6 drafted rows equal `sweep.py:topic_of()` of the
   corresponding file in the scratch tree (`binding_mismatches 0`). The round-73 block's two
   rows (base lines 787-788) were separately shown to be word-for-word identical to the
   `conlang-scholarship` entries' topics — which is why §4.2 reports `hits=2` for exactly
   those two files and `hits=1` for the other four.
5. **Sibling controls on the patched text.** `tools/check-readme-heading.py --readme <patched>`
   exit 0, `findings 0`, `headings {"1":1,"2":10}` (base `{"1":1,"2":9}`: the appended block
   adds exactly one H2); `tools/check-readme-revisions.py --readme <patched>` exit 0,
   `findings 0`, `warnings 1` — the same pre-existing `REVISION-ORPHAN lines=[225,236]` the base
   file carries, so the new block adds no warning.

No tool was installed or upgraded (python3 stdlib + the lane's own instruments were sufficient).

## 3. Touched surfaces

- Created: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-75/drafts/readme-rows.md`.
- Created: this report.
- Scratch: `/fast/scratch/hyaku/kotodama-r75/ScribeReadmeIndex/` (fixture tree, patched README,
  pseudo-lanes, extracted scripts) — deleted before yielding; every number above is reproduced
  in this report, and both shipped scripts live inside the draft so the L1 can re-run them.
- Not touched: `corpus/README.md`, `corpus/knowledge/**`, `corpus/SOURCES.md`, `LOG.md`,
  `SCORECARD.md`, `SKILL.md`, `SHONEN.md`, `corpus/QUALITY.md`, `reports/round-75/*`,
  `reports/round-28/readme/sweep.py`, the fleet repo, the lane's git/jj state and index
  (read-only `git show`/`git diff` only), and `shokuknow` (read-only reads of the staged entries).

## 4. Findings for the canonical judge

**F1 (conflict, rule-level; needs the L1 before freeze).** The myth-symbol heading repair
(E3) is not reachable by claim Ca. Ca's `APPENDONLY` leg says: "changed lines elsewhere are a
subset of the stated_at lines of REPAIR pairs plus appended lines"; `## myth-symbol/ (29)` at
`corpus/README.md:376` is a changed line that is **not** any REPAIR pair's `stated_at`, so E3
reds `APPENDONLY` at the combined tree (`COMBINED` leg materializes both landings and runs all
12 legs). It also cannot become a Ca pair: unlike L75-02 (30≠32) and L75-03 (36≠40),
`## myth-symbol/ (29)` is **true at base**, so a pair naming it is not red at base and
`ExecLedger` drops it by rule. Without E3 the file becomes internally inconsistent the moment
claim C lands (footer says 31, heading says 29; `header_drift` red — measured in the matrix).
Drafted options, with the recommendation: (1) extend Ca's `APPENDONLY` clause pre-freeze by
exactly one class — the partition-count heading of a partition claim C's own entries move, plus
claim C's index rows, at `corpus/README.md` (same shape as the round-74 R1 exemption, red-free
at base); and (3) have C's `INDEX` leg grade the six headings against the six live partition
counts. Option 2 (ship the heading stale, name it as stale in the footer block, following the
round-73/74 precedent) is drafted as the fallback but leaves a fresh instance of the very
defect class this round's L75-02/L75-03 repair.

**F2 (finding; shapes Ca's L75-04 repair).** The only way `sweep-green-after.txt` can be green
is for the repaired sweep to end a partition at any level-2 heading. `SECTION_RE` closes a
partition only at the next `## <part>/ (<n>)` heading, so the round-73 block's two row-shaped
lines (base 787-788) are read as `civilizations/` ghosts. Adding the four in-section rows does
not remove them — measured: the `repair-no-boundary` row of the matrix still shows 2 ghosts.
De-shaping 787-788 is not available either (a changed line in an older block, unreachable by any
REPAIR pair for the same reason as F1). This is ExecSweepFix's instrument, not this file; the
draft states it in §6.2 and its §4.6 check implements it.

**F3 (finding; footer grammar fork).** The current `FOOTER_RE` needs the three-line shape
(`Counts checked <date> from the repo root:` / `` `cmd` `` / `(total N files; directory totals
a/b/c/d/e/f).`). The round-73 and round-74 footers are single-line and match nothing. So
"read the last footer" must mean the last **match**, and the new footer must therefore be
three-line (draft variant A, primary); if the repair instead broadens the regex to the round-74
one-line shape, variant B (in the draft) is the byte-exact alternate. Independently, the
`Total knowledge entries:` read must also take the **last** match — base's only match is `243`,
so no footer text can green `totals_line` without that half of the repair.

**F4 (finding; duplicate rows, named not hidden).** After Ca's two rows land, `corpus/README.md`
carries two rows for each `conlang-scholarship` file: the in-section row and the round-73
block's row (787-788), which are word-for-word identical. `sweep.py`'s duplicate leg is
per-section and outside its `ok`, but a reviewer will see it; the draft states it in §6.4 and
offers the only in-rules closure (same exemption as F1/F2).

**F5 (check; critic repair already satisfied).** `CritCCounterVacuity.md`'s ranked item 8 asks
`INDEX` to add "every README index row in the myth-symbol section names an existing `.md` file …
each adopted entry has exactly one such row whose topic equals its own `- topic:` value". The
drafted bytes satisfy that wording, and §4.6 implements exactly its two clauses with both
mutants caught (F5 is a green, not a defect).

**F6 (limit, stated).** The draft's numbers are `N`-parameterised (`N` = the frozen `entries`
length; currently 2 → 251 / `32/31/40/29/24/95`; `N∈{0,1}` substitutes to `249+N` /
`32/(29+N)/40/29/24/95` and E3 becomes `(30)`; `N=3` with `.amend-2026-10-23b.md` → 252 /
`32/32/40/29/24/95`, row drafted in §2.3a). `accept-c.py` and `accept-ca.py` did not exist
when this draft was written, so no leg of those counters is claimed here — §4's expected
readings are the *existing* instrument's (`reports/round-28/readme/sweep.py`) and the two
heading controls', plus the leg names from the draft claims file.

**F7 (found during the wave; resolved by its owner).** The base-entry draft's `couples:` line
(line 10) said `.amend-2026-10-23.md` carried "the S/Z codes". I read the cell and the amend's
own topic, relayed the mismatch to `ScribeEntryBase`, and it has re-read the staged file and
fixed the line to "Todorov's temporal deformation, Greimas's two isotopies, and Barthes read at
the level of description" — correct, since the amendment's own text says the five-code
enumeration "is still not recovered from any opened source". **No effect on this draft**: the
topic strings are unchanged (906 / 359 chars), so the two rows stand as drafted and no
re-verification was needed.

**F8 (finding; for the registry-rows builder, not this file).** Two consequences of the same read
that the `ROWS` leg will meet, neither of them a README matter: (a) the staged corpus
contradicts itself on S885's reach — the staged base entry scopes the row to notice + opening
paragraph (full text behind a JavaScript viewer) while the staged amendment claims the per-page
transcription service returns all 27 pages and that the full text was opened — so S885's Gate
row must carry the scope its own fetch establishes, not either staged claim; this draft's
`- topic:` text deliberately asserts no scope ("carried by one Western row at the scope the Gate
locates"), which is why the 906-char revision happened; (b) both admitted entries cite S885, so
that row's `used-by` cell must name both entry paths — a base-only derivation would look like a
content defect while being a row-derivation bug.

**Re-verification after the mid-seat topic revision (906 chars).** All six rows were re-extracted
from the draft and both shipped scripts re-run on a rebuilt pseudo-lane: §4.2 rows-bound →
`OK hits=2` ×2, `OK hits=1` ×4, `ROWS-BOUND: PASS` (exit 0); §4.6 self-check →
`INDEX-SELFCHECK: PASS` (exit 0) with `missing [] ghosts [] mismatch [] drift {}`,
`footer 2026-10-27 251 [32,31,40,29,24,95]`, `totals 251`. The table in §2.2 above was measured
before the revision; the revision touches one row's text only, and these two runs are its
post-revision evidence.

## 5. Out of scope, deliberately

No landing, no commit, no counter authoring, no `claims.json`/`ledger.json` edit, no
`reports/round-75/telemetry/` receipt, no entry edit, no registry edit, no sweep repair. The
four topic sources (the four `conlang-scholarship`/`heritage-taxonomy-models` blobs) were read at
base and their working-tree sha256 equals the `f556d10` blob (they are untouched since round 74).

## 6. Coordination

Two IRC messages sent (one each to `ScribeEntryBase`, `ScribeEntryAmend`) asking for the final
`- topic:` strings; `ScribeEntryBase` replied with its 892-char topic and the warning that its
file carries a second `- topic:` (Part 2 scope line, 275 chars) that `TOPIC_RE` must not reach;
`ScribeEntryAmend` committed its draft to
`.ufo/waves/round-75/drafts/narrative-structure-frameworks.amend-2026-10-23.md`, whose single
`- topic:` (359 chars) is the row text used.

## 7. Artifact paths

- Draft (the deliverable): `.ufo/waves/round-75/drafts/readme-rows.md`
- This report: `.ufo/waves/round-75/w1/ScribeReadmeIndex.md`
- Re-runnable checks live inside the draft: §4.2 (rows-bound), §4.6 (index self-check, boundary
  + last-footer semantics, four measured runs), §4.5 (plain `find` arithmetic), §3 (anchors).
