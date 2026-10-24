# ScribeEntryAssemble — entry assembly (claim C)

Seat: `kotodama-r65.ScribeEntryAssemble` · round 65 v2 wave · 2026-10-24
Lane root: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` · base `17c32302c6845c8f164b985a8cb312d3181c8788`

## Result in one line

Assembler built, proven on fixtures, and run against the live wave: **0 of 26 row fragments had landed**, so the
threshold (>= 20) was not met. `.ufo/waves/round-65/stage/entry-draft.md` exists as a **partial assembly**: complete
frontmatter, all nine game-class sections, the worldbuilder table, and the four required closing sections — with zero
bullets, because zero fragments existed. The dependency is the finding.

## Dependency (blocking, recorded not worked around)

| Item | State at 01:52–01:58 local | Evidence |
|---|---|---|
| Row fragments under `.ufo/waves/round-65/rows/` | **0** of 26 | `find .ufo/waves/round-65/rows -type f -name 'row-*.txt' \| wc -l` → 0, re-checked at close; the only file is `ScoutGapGames/gap.md`, a gap note, not a fragment |
| `.ufo/waves/round-65/stage/entry-spec.md` | **absent** | `ls .ufo/waves/round-65/stage/` → `gate-spec.md mut-ca/ mut-o/ readme-patch.md` (seat `ScribeEntryBody` still running at scan time) |
| Registry rows S750–S775 in `corpus/SOURCES.md` | **absent** (L1's job) | `grep -cE '^\| S7(5\|6\|7)[0-9] ' corpus/SOURCES.md` → 0 |
| Fragment contract | known and parsed | row-seat prompts in `taskcall-final.json`; `tools/check-row-fragments.py` `LABEL_RE` |

Per the seat contract I did not wait on peers and did not synthesize fragments. The draft is therefore structure +
authored prose, and its citation count is 0.

## Behavior

I wrote a deterministic assembler rather than hand-building the draft, because the fragments land asynchronously and
the entry must satisfy frozen counter semantics line-for-line:

`python3 -B .ufo/waves/round-65/stage/assemble-entry.py --root .`

- Scans `rows/**/row-<SID>.txt` (skips `rejects.txt`), parses `ROW|BULLET|VERIFY|CAPTURE|ACCESS` in **both** the
  round-65 `KEY=` form and the round-64 `KEY:` form; first occurrence of a label wins; duplicate S-ids are recorded as
  conflicts and the first fragment is kept.
- Emits `stage/entry-draft.md` and `stage/assemble-audit.json` (per-row flags, per-row metrics, entry shape metrics).
- Re-runnable and idempotent: rerun after each fragment lands, no state carried between runs.

Checks implemented, each mirroring the frozen `reports/round-65/accept-c.py` leg where the leg's input is available from
fragments alone (registry insertion belongs to the L1):

- **FILE**: 1 H1, 0 H3, <= 16 H2, <= 250 lines, `- topic:` present.
- **ROWS**: 11 cells; tier A/B; `mined`; opened `2026-10-24`; recheck `180d`; used-by names the entry; anchor quote
  8–25 normalized words; live URL present; capture present and query-aware-normalize-equal to the live URL.
- **ONEID / NOMARK**: one S-id per line, bullets in `- clause (SID)` shape, no table row carrying an id.
- **RESTATE**: >= 5 content words; >= 3 in-order quote content words; no copied run > 12 words; at least one novel
  content word; verbatim teaches copy; and revision 1's **word-boundary teaches near-copy rule** (`word_tokens`,
  in-order subsequence coverage **>= 0.80 fails**).
- **HOSTS**: placeholder-host list.
- **LINK**: duplicate query-aware-normalized URLs across rows.

Section map and class assignment, fixed from the 26 row topics in `.ufo/waves/round-65/taskcall-final.json` (each row
appears in exactly one section; H2 budget 14 of the 16 the FILE leg allows):

| Section | Rows |
|---|---|
| 1. How games and play are classified | S750, S756, S757, S758, S759 |
| 2. Board and race games of the ancient world | S751, S752, S753, S773, S775 |
| 3. Strategy boards on the move | S763, S764, S765 |
| 4. Ballgames, ball materials and stick games | S761, S762, S771 |
| 5. Athletic and ritual contests | S754, S760, S772 |
| 6. Lots, dice and gambling toys | S755, S767, S768 |
| 7. Cards | S766 |
| 8. Children's playground repertoire | S769, S770 |
| 9. Target and throwing games | S774 |
| What a worldbuilder does with this | id-free table (avoid the `TABLE-ID` finding) |
| cross-cultural patterns | 14 conditional statements, emitted only when every required row landed |
| calibration | tier meaning, three stated limits, scope discipline |
| one-way pointing to partial owners | 7 pointers, one direction stated |
| lore handoff | boundary named, canon decisions left to lore-shokunin |

The four closing sections carry **no S-ids by construction**: a second citation of any id would break the ONEID leg's
`citations_exactly_once`, and a table row carrying an id would raise `TABLE-ID` from `tools/check-cited-lines.py`.
Cross-cultural statements are gated on their supporting rows (`PATTERNS` requires-sets) so the draft never asserts a
pattern whose rows have not landed.

## Commands and observed output

```text
$ python3 -B .ufo/waves/round-65/stage/assemble-entry.py --root .
ASSEMBLE landed=0/26 draft_lines=104 h2=14 cited=0 exactly_once=True
  draft=.ufo/waves/round-65/stage/entry-draft.md
exit=0

$ python3 -B tools/check-cited-lines.py .ufo/waves/round-65/stage/entry-draft.md
CITED-LINES: 0 finding(s) in 1 file(s)
exit=0

$ python3 -B tools/check-row-fragments.py --rows .ufo/waves/round-65/rows
FRAG: 0 finding(s) in 0 file(s)
exit=0
```

Fixture battery, in `/tmp` only (no lane bytes touched), to prove the assembler and the near-copy flag actually work:

```text
$ python3 -B .../assemble-entry.py --root /tmp/k65-asm        # KEY= format, 2 crafted fragments
ASSEMBLE landed=2/26 draft_lines=102 h2=14 cited=2 exactly_once=True
  S750 FLAGS in_order=0 teaches_nearcopy=0.94
audit: S751 flags=[] in_order=3 cov=0.214        # compliant control: clean

$ python3 -B .../assemble-entry.py --root /tmp/k65-colon      # round-64 KEY: format, real S718 row retargeted
ASSEMBLE landed=1/26 draft_lines=103 h2=14 cited=1 exactly_once=True
  S750 FLAGS opened=2026-10-23                    # round-64 opened date correctly rejected
```

The mutant is the round-64 routed bypass class reproduced literally: the teaches cell plus one trailing word. The
frozen counter's own control records `coverage 0.92` for it
(`reports/round-65/telemetry/controls-c.txt`); my measurement of my fixture is `0.94`, and the threshold is `0.80`.

## RESTATE flags on landed bullets

**None can be reported: no bullet landed.** The seat asks me to flag any bullet estimated to trip RESTATE
(token coverage of its teaches cell >= 80%). Two things are true instead:

1. The flag is implemented and demonstrated (0.94 mutant flagged, 0.21 control clean); every future run prints
   `teaches_nearcopy` for any bullet at or above 0.80 and `near_copy_watch` from 0.60 upward.
2. Bullets will be judged against the **final registry cells**, not the fragment cells. If a row seat's `ROW=` teaches
   cell is edited during L1 integration, a bullet that passes on the fragment can fail on the registry. Rerunning the
   assembler after integration is the cheap guard.

## Findings

- **F1 (dependency, primary).** 0 of 26 fragments landed; the >= 20 threshold is unmet. Draft is structural only.
  Reassembling is one command once fragments exist; projected size with all 26 bullets is ~112 lines against the
  250-line cap, and 14 H2 against the 16 cap — **only two H2 of headroom remain**, so a late tenth class section must
  be merged, not added.
- **F2 (spec absent).** `stage/entry-spec.md` did not exist at assembly time, so the round-64 shape was used, as the
  seat instructs: H1 + `- topic:` / `- source:` / `- verified-at:` / `- recheck:`, numbered H2 sections, a worldbuilder
  table, then the four round-65 sections. If `ScribeEntryBody` publishes a different skeleton, the section titles and
  the worldbuilder table need reconciliation against it; the bullets do not (they are keyed by S-id, not by section).
- **F3 (conflict, verbatim, for the canonical Rust judge).** Claim C's statement asserts the base filename counter
  `... | grep -ciE 'game|play|sport|contest|toy|mancala'` "prints 0". Scout `ScoutGapGames` measured **2** at the frozen
  base, from substring matches: `sumptuary-law-rank-display.md` (`play` in `display`) and
  `transport-mobility-lexicon.md` (`sport` in `transport`). Their report records it; I did not rerun the command. The
  topic-owner conclusion is not contradicted (their base `git grep` for mancala/knucklebone/astragal/tug-of-war/senet/
  hnefatafl/patolli returned nothing), but the stated predicate is false as written. This is a claim-statement defect,
  not something my draft can repair.
- **F4 (vacuous green).** `tools/check-row-fragments.py --rows .ufo/waves/round-65/rows` exits **0 with
  `0 finding(s) in 0 file(s)`** on an empty directory. A green FRAG leg is therefore not evidence that fragments exist;
  gate readers must pair it with a count. Reported as an observation about an instrument I do not own (claim O), not as
  a claim that the instrument is wrong.
- **F5 (fragment-shape drift).** The contract in the row-seat prompts specifies `KEY=` labels, while the round-64 model
  fragment `ScribeRowS718/row.txt` that seats were told to read uses `KEY:` labels. I accept both. Any fragment that
  uses the colon form would be invisible to a parser written only to `LABEL_RE` in `check-row-fragments.py`.
- **F6 (bullet wrappers).** Fragments whose `BULLET=` value already matches `- clause (SID)` are emitted verbatim;
  fragments that omit the leading dash or the trailing `(SID)` are wrapped to the shape the RESTATE leg requires, and
  `assemble-audit.json` records `bullet_normalized` for each such row so the L1 can see the difference.

## Touched surfaces

- `.ufo/waves/round-65/stage/entry-draft.md` (new, 104 lines)
- `.ufo/waves/round-65/stage/assemble-entry.py` (new, executable)
- `.ufo/waves/round-65/stage/assemble-audit.json` (new)
- `.ufo/waves/round-65/w1/ScribeEntryAssemble.md` (this report)
- `/tmp/k65-asm`, `/tmp/k65-colon` (fixtures outside the lane)

No product file, registry row, claim, counter, lesson, README, or lane jj/Git state was modified. No `git`/`jj` write
was run; no commit. `corpus/knowledge/culture-material/games-play-sport-contests.md` was **not** created — that path is
the L1's, and my draft lives under the wave directory as assigned.

## Out of scope (deliberately not done)

- No registry insertion, no README patch (seat `ScribeReadme` owns it), no gate/lesson records (`ScribeGateRecords`,
  `ScribeLessonR65`).
- No live re-open of any URL (the blind-reopen seats own that; there were no fragments to reopen anyway).
- No run of `reports/round-65/accept-c.py`: it needs the registry rows and the base tree, so a run now would be a
  guaranteed FAIL that proves nothing beyond F1. The legs it can support today were replicated in the assembler and
  exercised on fixtures.

## Tooling

Nothing installed or upgraded. Python 3 (stdlib only), `find`, `grep`, `sed` — all pre-existing. Pacman was not invoked.

## Artifacts

- `.ufo/waves/round-65/stage/entry-draft.md`
- `.ufo/waves/round-65/stage/assemble-entry.py`
- `.ufo/waves/round-65/stage/assemble-audit.json`
- `.ufo/waves/round-65/w1/ScribeEntryAssemble.md`
