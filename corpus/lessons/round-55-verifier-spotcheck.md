author: hyaku closure (non-author integrator, @m_opus)

# Round 55 — verifier spot-check (non-author closure)

Lane-round: kotodama round 55 (hyaku phase 4, L1 KotodamaR55, attempt 1). Base `89973ba74c4bb0efa7fac1eb60766820c6bd6625`, lane tip `2935c47011049527842b6d3f08691d9629c3b983`. Report `.ufo/reports/round-55/kotodama.md` (fleet `39360c0`). Closure run 2026-10-22, 20:44Z–20:56Z. Seven read-only seats (six reviewers, one critic) ran the source re-opens, the claim-O set re-derivation and the separability ruling. This closure ran the conformance checks, the claim-C counts and the census itself.

Driver digest (copied from `.ufo/watchdog.log`, lines 752 and 759):

- 2026-10-22T16:46:13-03:00 launch kotodama round=55 pgid=618401 driver=hyaku-inline attempt=1
- 2026-10-22T17:43:58-03:00 complete kotodama round=55; hyaku-inline attempt=1

## 1. Step-1 conformance

| check | command | observed | result |
|---|---|---|---|
| report committed by lane identity | `git log --format='%an %H' -- .ufo/reports/round-55/kotodama.md` | `kotodama-shokunin 39360c0c5e8601d5450b687eabb4a39793c96238` (17:43:37-03:00, after the tip commit at 17:43:35) | pass |
| SHONEN heading, one line per box | read the report, `## SHONEN` | 4 lines, all `[~]` | pass |
| cited commits exist and are ancestors of `main` | `git cat-file -t <h>; git merge-base --is-ancestor <h> main` for d44309a, 662239d, f4015e7, 8eda954, b9c44a2, 81178c8, d52c9df, 454a2dc, eb0a331, 173cab6, 2935c47 | all `commit`, all exit 0; author `kotodama-shokunin` on every one | pass |
| lane pushed | `scripts/hyaku/jj-lane.sh state …` | `branch=main local=remote=2935c470… ahead=0 behind=0 head=detached tracked=0 untracked=0` | pass |
| leftovers | `git status --porcelain` | empty | pass |
| prompt carries the template contract | every placeholder-free line of `templates/round-prompt.md` searched verbatim in `.ufo/prompts/kotodama-round-55.md` before `## 6.` | 105 lines, 0 missing; addendum at `## 6.` (line 141); prompt committed `cf56f8d` at 16:46:11, before launch | pass |

Note: the addendum heading reads "hyaku (百) phase 3" while the report and the session say phase 4. This is orchestrator-side wording, not a lane defect.

## 2. Claims

Two claims were declared: **C — coverage** (learning claim and sourced claim) and **O — operability** (capability acquisition).

### Claim C (re-measured)

| measure | command (plain, over committed bytes) | observed | reported | match |
|---|---|---|---|---|
| knowledge files | `git ls-tree -r --name-only <rev> corpus/knowledge \| grep -c '\.md$'` | 230 at `89973ba7`, `f4015e7` and `454a2dc`; 231 at `eb0a331` and the tip | 230 → 231 | yes |
| myth-symbol files | the same, over `corpus/knowledge/myth-symbol` | 26 → 27 | 26 → 27 | yes |
| new entry | `git diff --name-only 89973ba7 2935c470 -- corpus/knowledge` | `myth-symbol/monsters-hybrid-beings.md` is new (186 lines at `eb0a331`, 188 at the tip). The other three paths are the routed fixes `b9c44a2`, `81178c8` and `d52c9df` | 186 lines | yes |
| S-ids cited by the entry | `git show <rev>:<entry> \| grep -oE '\bS[0-9]{3}\b' \| sort -u` | 73 unique at `eb0a331` and at the tip, all ≥ S285, none below | cited 73 | yes |
| SOURCES rows | `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` | 284 → 357 (`eb0a331`) → 358 (tip) | 284 → 358 | yes |
| status totals | CORPUS.md status-histogram awk | 240/34/10 → 313/34/10 (`eb0a331`) → 313/35/10 (tip) | 240/34/10 → 313/35/10 | yes |
| new-row tiers, status, used-by | awk over S285–S358 | A 56, B 18 (S358 is B); mined 73, queued 1; used-by the entry 73, `—` 1 | A 56 / B 17, plus S358 B | yes |
| malformed and duplicate rows | CORPUS.md NF!=13 and `uniq -d` commands | 0 and none | — | pass |
| index row | `grep -n monsters-hybrid corpus/README.md` | lines 4 and 316 | README rev 2.12 row | yes |
| Gate lines | awk over the `## Gate` section, `^- S[0-9]+ ` | 74, no duplicate ids | 74 | yes |
| census | `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` | `kotodama ok`, exit 0; 10 W04 warnings (S127–S133, S185, S186, S358) | exit 0, `ok` | yes |

**Instrument (evidence-verified, not executed; §Gate standard).** For `reports/round-55/accept-c.py`, the committed `reports/round-55/telemetry/declaration-dry-run.txt:3-10` reads `SET FAIL count=230`, `SWEEP FAIL rows 230 files 230`, `FLOOR FAIL cited=0` and `exit 1`. The committed `reports/round-55/telemetry/final-measures.txt:3-10` reads seven legs PASS (`count=231`, `rows 231 files 231`, `cited=73`, `ACCESS PASS`) and `exit 0`. The criterion-11 controls receipt (`criterion11-controls.txt`) ends `CONTROLS 14/14 as expected`. Every count above agrees with those receipts.

### Claim O (re-derived by a seat, evidence-verified)

- **Plain re-derivation (ClaimOPlainRemeasure seat).** The seat wrote its own python over `git archive 2935c470` and did not run the lane tool.
  - `doubled-locator` is a quoted span that repeats the locator text before it. It found exactly 13 rows: S239, S240, S243, S246, S249, S259, S262, S265, S266, S267, S268, S275 and S277.
  - `truncated-grounds` is a Gate Grounds that is a proper prefix of the registry `teaches` cell. It found exactly 17 rows: S241, S242, S244, S248, S250, S251, S253, S255, S259, S263, S264, S265, S275, S276, S277, S278 and S279.
  - Both sets equal the round-54 closure's §5 items 1–2. One nuance: a strict prefix test without quote stripping gives 15 and misses S263 and S279, whose registry cells contain `"`. The routed 17 hold under the tool's quote-stripping normalisation.
- **Committed evidence.**
  - Before, at `f4015e7`: `declaration-dry-run.txt:23-31` reads DOUBLED and TRUNC `count=0` with the 13 and 17 missing, EXIT and ESCAPE FAIL, and `exit 1`.
  - After: `final-measures.txt:12-20` reads eight legs PASS and `SELFTEST: 27/27`. `RerunAcceptO.md:1` names exit 0 at `454a2dc` and exit 1 at `f4015e7`.
  - Controls: `criterion11-controls-o.txt` reads `CONTROLS 16/16 as expected`.
  - Mutants at `454a2dc`, all killed: MutateDoubled 4/4, MutateTruncated 4/4, MutateEscapes 4/4.
  - Selftest lineage: 12/12 at `f4015e7`, 24/24 at `454a2dc`, 27/27 at the tip. Only `173cab6` touches the checker after landing.
  - Landing scope: `git show --stat 454a2dc` changes `tools/check-gate-quotes.py` only.
- **Gaps.** `final-measures.txt` and `declaration-dry-run.txt` do not name the revision they measured. They identify it only by "lane worktree after falsify fixes" and "pre-landing", and `RerunAcceptO.md` and SCORECARD supply the hashes.

### Separability ruling (AXES.md "causally separable")

The declared check `python3 -B tools/check-claim-separability.py reports/round-55/separability-manifest.json` exits 1 at the landed tree, with `SEPARABILITY_DEPENDENCY O->C … tools/check-gate-quotes.py:355` (`final-measures.txt:74-77`). The author disclosed this as R55-M5. **Ruling: C and O are causally separable, and each verifies on its own. The red check is a conformance defect of the declared input, not a dependency.**

- **Every hit is a fixture.** `git show {454a2dc,2935c470}:tools/check-gate-quotes.py | grep -nP '\bS(28[5-9]|29[0-9]|[3-9][0-9][0-9])\b'` matches only the selftest fixture ids S900 and S901 (lines 322–386 at `454a2dc`, 331–403 at the tip). The exact range of C's rows, `\bS(28[5-9]|29[0-9]|3[0-4][0-9]|35[0-7])\b`, has 0 hits at both revisions.
- **O verifies without C.** O landed at `454a2dc`, whose parent `d52c9df` has no C byte: 230 files, 284 rows. accept-o exits 0 there (`RerunAcceptO.md`). accept-o reads `corpus/SOURCES.md` `teaches` cells through `registry_teaches`, but the critic seat compared column 7 for every row below S285 at `f4015e7`, `454a2dc` and the tip, and all 284 are equal. `git diff 454a2dc eb0a331 -- corpus/SOURCES.md` adds S285–S357 only.
- **C verifies without O.** accept-c reads `corpus/knowledge`, `corpus/SOURCES.md`, `base-knowledge-files.txt`, `sweep.py` and `tools/check-source-access.py`. It reads no O byte: grepping it for `gate-quotes` exits 1, and O's commit touches only its own tool. `RerunAcceptC.md` ran at `eb0a331`, which already contains O, so it is not "C without O" evidence. The separability tool's per-unit acceptance runs on base plus each unit's own lands report `acceptance_runs=2` for 3 units, so both units passed on their first isolated run. That is committed evidence that C passes without O. Every claim-C count above is also a plain measure over bytes O never touches.
- **Route.** Declare exports as the exact id range a claim creates.

### Axis harm

`git diff 89973ba7 2935c470 -- SCORECARD.md` is append-only: one capability row (`gate-line shape checker`) and a new round-55 section. No earlier row changed. `SHONEN.md` changes only line 6, and its counts (358; 313/35/10) match the measurement above. No harmed axis was observed.

### Per-axis verdicts

| axis | verdict | basis |
|---|---|---|
| coverage | improved | re-measured: 230 → 231 files, myth-symbol 26 → 27, 73 new mined rows all cited; accept-c receipts exit 1 → exit 0 evidence-verified |
| operability | improved | both routed sets re-derived independently (13 and 17, exact); accept-o receipts exit 1 → exit 0 at named revisions; mutants 12/12 killed; selftest 27/27 at the tip (evidence-verified) |
| calibration | unchanged | not claimed; the routed fixes and mistakes R55-M1 to R55-M6 are recorded. Record nits are routed below |
| depth | unchanged | not claimed |
| freshness | unchanged | still paused by the open round-11 L0 question |
| adjacency | unchanged | not claimed; §11 lore handoff is proposal-only (spot-read) |

## 3. Discernment spot-check

The sample covers the four falsify row-slices that were cancelled unreported (S290–S294, S305–S309, S320–S324, S355–S358), plus three rejects. Sources were re-opened with `curl` (browser UA) on 2026-10-22. Word counts use a whitespace split.

| item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S291 Bosworth-Toller *aglǽca* (Gate) | admit | `lexicon.ff.cuni.cz/html/oe_bosworthtoller/b0029.html`, HTTP 200 | agree | The gloss is verbatim (13 words) in the lemma entry, and the base-noun etymology "misery … torment" is on the page. The four anchor quotes are all verbatim and ≤ 25 words. |
| S294 Te Aka *taniwha* (Gate) | admit | `maoridictionary.co.nz/search?keywords=taniwha`, HTTP 200 | agree | Sense 1 is verbatim (15 words). The habitat and niho taniwha passages that support the Grounds are on the page, and the four anchor quotes are ≤ 25 words. |
| S305 Florentine Codex fol. 70v (Gate) | admit | `florentinecodex.getty.edu/en/book/11/folio/70v`, `71r`, `71v`, HTTP 200 | agree | The López Austin transcription heading is verbatim (14 words). The hand-on-tail, drowning and spring details are in the 70v–71r transcription. |
| S308 Te Ara *taniwha* (Gate) | admit | Wayback `20260208222348/teara.govt.nz/en/taniwha/print`, HTTP 200 | agree | The quote is verbatim (21 words) under "A creature of many forms", and the page is signed by Basil Keane. The shape-change, guardian and highway/prison disputes in the Grounds are all present. |
| S309 Wengrow, *Origins of Monsters* (Gate) | admit | publisher PDF, HTTP 200, `pdftotext` | agree | The Introduction opens with the quoted 9 words, and the composite and urbanism Grounds are on pp. 2–3. Caveat: the press book page returned 403 (Cloudflare) to plain curl. |
| S321 Aberdeen Bestiary (Gate) | admit | `abdn.ac.uk/bestiary/what.php`, HTTP 200 | agree | The first sentence is verbatim (20 words). The "same weight as totally fabulous accounts" and didactic purpose clauses support the Grounds without over-reading. |
| S322 British Library (Gate, and newly written SOURCES row) | admit | `bl.uk/stories/blogs/posts/what-is-a-bestiary`, HTTP 200 | agree | The Gate quote is verbatim (20 words) under "Function and origins". The four SOURCES anchor quotes are 20, 20, 22 and 21 words, all verbatim and within the 25-word cap. |
| S324 Pliny NH 7.6 (Gate) | admit | `penelope.uchicago.edu/…/Pliny_the_Elder/7*.html`, HTTP 200 | agree | The Latin is verbatim (11 words) at §6. "ludibria sibi, nobis miracula" (§32) and "ad auctores relegabo" (§8) ground the Grounds. |
| S355 Columbia UP, *Abominable Science* (Gate) | admit | `cup.columbia.edu/book/abominable-science/9780231153201/`, HTTP 200 | agree | The description is verbatim (13 words) and names the five cryptids. |
| S357 Nature HSSC article (Gate) | admit | `nature.com/articles/s41599-020-0428-1`, HTTP 200 | agree | The quote is verbatim (18 words) in the paragraph beginning "For our purposes" after the Introduction heading. |
| S358 UNESCO Drametse (Gate, and newly written SOURCES row) | admit (queued, tier B) | `ich.unesco.org/en/RL/mask-dance-of-the-drums-from-drametse-00161`, HTTP 200 | agree | ¶2 s1 is verbatim (18 words). The row is appended, not edited: `git diff 89973ba7 2935c470 -- corpus/SOURCES.md \| grep '^[-+]\| S256'` is empty. Status is `queued` and used-by is `—`. |
| S256 tier A for practice claims | reject (superseded by S358 at tier B) | the same UNESCO page; `corpus/QUALITY.md:29` (criterion 6) | agree | The element description is the Secretariat's condensed summary. It is secondary for performers, order and occasion, and A only for inscription facts. This matches S258 at B, and the correction takes the superseding-row route the criterion prescribes. |
| Etymonline "monster (n.)" | reject (not registered; tier C, never sole support) | Wayback `20261004164107/etymonline.com/word/monster`, HTTP 200 | agree | It is a lead for English sense dates only. The *monere* derivation is carried by tier-A S286 (L&S) and S287 (Cicero), and no landed byte cites Etymonline. |
| Met lamassu, object 322608 | reject (opened, not cited, not registered) | `collectionapi.metmuseum.org/…/objects/322608`, HTTP 200 | agree | The record is real (gypsum alabaster, 883–859 BCE). The entry files the door-guardian claim under S317 and makes no claim this record would carry, so registering it would add an uncited row. |

**Mechanical check over all 74 Gate lines** (this stands in for the cancelled ReviewGateLines55 seat). A seat-written python script compared each line's `Grounds:` text with the matching SOURCES `teaches` cell. 68 are byte-equal and 6 differ only by HTML entities (S288, S305, S326, S341, S343, S348; `html.unescape` makes them equal). No quoted span exceeds 25 words; the longest is S296 at exactly 25.

**Census:** `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` → `kotodama ok`, exit 0. There are 10 W04 duplicate-URL warnings. S358's warning is expected, because a superseding row shares S256's URL.

## 4. Trend verdicts

- **expansion: improved.** Monsters and hybrid beings now have an owner: 0 filename owners at base, `myth-symbol/monsters-hybrid-beings.md` at the tip. Knowledge files are 231, 73 new mined rows are each cited by the entry, and one capability row was added (all re-measured).
- **quality: improved.** All 15 acceptance legs pass on committed evidence, and the routed 13 and 17 sets re-derive exactly. Mutation testing killed 12 of 12. The falsify fixes are recorded at `173cab6`, and every one of the 11 admitted rows re-opened here held. The bounds are the red declared separability check (a declared-input defect, ruled above) and the carried checker limits (entity decoding, KEEP53 scope).
- **discernment: improved.** The spot-check agrees with the gate on all 11 admits and all 3 rejects, including the four slices no falsify seat reviewed. The checker turns the round-54 closure's two routed shapes into mechanical findings, keyed on the registry rather than the closure's over-firing regex (R55-M4).

## 5. Routed defects (lane fixes next round)

1. **Separability manifest export too broad (R55-M5).** `reports/round-55/separability-manifest.json` declares C's export as S285–S999, so the declared check exits 1 at the landed tree. Future manifests must declare the exact id range a claim creates; for this round that is `\bS(28[5-9]|29[0-9]|3[0-4][0-9]|35[0-7])\b`. S358 is a record-unit row and outside C.
2. **SCORECARD record nits.** The round-55 calibration row says "mistakes R55-M1 to R55-M4", but the lesson has R55-M1 to R55-M6. The capability row and the operability row cite selftest 24/24 without naming `454a2dc`, while the tip measures 27/27. Fix both in an appended row, not in place.
3. **Receipts do not name their revision.** `reports/round-55/telemetry/final-measures.txt` and `declaration-dry-run.txt` carry a timestamp but no commit hash. §Gate standard requires that a verdict name the revision it was measured against. Have the receipt writers print `git rev-parse HEAD`.
4. **Cancelled falsify slices are partly covered.** This closure re-opened S291, S294, S305, S308, S309, S321, S322, S324, S355, S357 and S358, and all agree. S290, S292, S293, S306, S307, S320, S323 and S356 still have no row-level non-author re-open: carry them in Frontier until reviewed.
5. **S309 access note.** The row records the Princeton book page as reachable, but it returned HTTP 403 (Cloudflare) to plain curl on 2026-10-22, while the linked PDF returned 200. Record the access path in the row's next superseding note or in the recheck.
6. **Gate Grounds entities.** Six Grounds carry HTML entities where the registry cell has decoded marks. The checker's whole-teaches comparison does not decode them (Frontier item from ReviewGateToolCode, still open).

## 6. SHONEN note (operator-owned)

All four boxes stay `[~]`. A non-author measurement now confirms box 1's counts (358 rows; 313/35/10). Box 4 (no cross-domain bleed) is consistent with the spot-read §11 handoff, which is proposal-only and NON-CANON until lore receipts it. This closure exercised no end-to-end reviewer execution for boxes 2 and 3, so it does not recommend promotion.
