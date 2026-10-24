# ScribeReadme — README recipe for claim C (round 65)

**Seat:** `kotodama-r65.ScribeReadme` (build, claim C).
**Lane:** `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, HEAD `17c32302c6845c8f164b985a8cb312d3181c8788` (claim C's declared base; verified with `git rev-parse HEAD`).
**Deliverable:** `.ufo/waves/round-65/stage/readme-patch.md` — exact edits to `corpus/README.md` for after the entry lands.

## Behavior produced

A ready-to-apply patch with five edits, anchored to measured line numbers of the live README (713 lines, sha256 `c131ffd99196eed96c3251c1790c5c98ba65f9fc6abef23c6a287e551762da32`):

| # | edit | anchor | old → new |
|---|---|---|---|
| E1 | section header | line 364 | `## culture-material/ (31)` → `(32)` |
| E2 | index row | insert between lines 380 (`furniture-interior-lexicon.md`) and 381 (`garment-lexicon-crosslinguistic.md`) | `` - `games-play-sport-contests.md` — <DEP-1: entry `- topic:` text> `` |
| E3 | frontier bullet | insert after line 680 (round-64 bullet) | one-line bullet, games frontier gap closed (`frontier -> core`) |
| E4 | totals line | line 682 | `Total knowledge entries: 238.` → `239.` |
| E5 | counts footer | lines 684–686 | date `2026-10-23` → `2026-10-24`; `(total 238 files; directory totals 30/29/31/29/24/95)` → `(total 239 files; directory totals 30/29/32/29/24/95)` |

Filename order is forced and unique: `furniture-` < `games-` (`f`<`g`), `games-` < `garment-` (`m`<`r`). Footer vector order is the sweep's `PARTS` order (linguistics, myth-symbol, culture-material, synthesis, verification, civilizations).

Dependency marked, not guessed: **DEP-1** — the entry `corpus/knowledge/culture-material/games-play-sport-contests.md` does not exist at HEAD and no draft of it exists under `.ufo/waves/round-65/` (`rows/` empty; `stage/` held only this seat's file). The patch therefore carries the row as a labelled placeholder plus the exact derivation command that reproduces `reports/round-28/readme/sweep.py`'s `topic_of()` (NFKC-free, continuation lines space-joined, trailing period kept). **DEP-2** — the frontier bullet's gloss clause must be lifted from the landed `- topic:` line, not invented.

## Gates measured (read-only, no edits applied)

- `python3 -B reports/round-28/readme/sweep.py` at HEAD → **exit 0**, `total_rows == total_files == 238`, `topic_mismatch 0 []`, `header_drift {}`, `totals_line 238 totals_ok True`, footer `{total 238, dir_totals [30,29,31,29,24,95]}`, `footer_findings []`. This is the pre-landing baseline; it says nothing about the post-landing tree.
- Live partition counts (`ls corpus/knowledge/<part>/*.md | wc -l`): 30/29/31/29/24/95 = 238, matching README's headers and footer.
- Patch names the binding post-apply gates and expected readings: sweep (239, vector `30/29/32/29/24/95`), `tools/check-readme-heading.py`, `tools/check-readme-revisions.py`, `source-audit-inventory.py` (`totals.files 239`), and `reports/round-65/accept-c.py` SWEEP leg (sweep exit 0 **and** `topic_text in row_line`; that leg is a substring test, the sweep is the byte-equality test — both must pass).

## Findings

1. **Claim C's stated ownership command does not print 0.** `reports/round-65/claims.json` claim C says `git ls-tree -r --name-only 17c32302 -- corpus/knowledge | grep -ciE 'game|play|sport|contest|toy|mancala'` prints 0. Run at the declared base it prints **2** — `culture-material/sumptuary-law-rank-display.md` (`play` in "display") and `culture-material/transport-mobility-lexicon.md` (`sport` in "transport"). The ownership property is true only word-bounded: my word-bounded filename scan returns 0 lines. No accept-c leg runs this command, so `ACCEPT-C-65` is unaffected; the patch records the conflict verbatim for the canonical judge and does not edit the frozen `claims.json`. Consequence for the bullet: it states "word-bounded" and names the two false friends, so a reader's re-run cannot falsify it.
2. **Topic-line "0 owners" needs the mention qualifier.** A word-boundary scan of `^- topic:` lines for games/play/sport/contest terms returns exactly one line, `culture-material/music-instrument-lexicon.md:3` ("musical contests"). Wording follows README revision 2.9's own precedent ("0 filename owners and 1 topic-line mention that is not an owner, `music-instrument-lexicon.md:3`") rather than a bare zero.
3. **Round 64 landed without a revision block.** `git show 95c9194e -- corpus/README.md` shows header-count, row, frontier bullet, totals and footer changes only; no `revision: 2.17`. The top block is still `revision: 2.16 — Round-63` (line 3), whose prose correctly describes round 63 (236→237). Revisions 1.3–2.16 each carry a block, so round 64 is the outlier. The patch follows the landed precedent for its five named edits and offers an optional `revision: 2.17` block (satisfies `check-readme-revisions.py`: unique label, non-increasing order, non-stub body) — labelled optional because the assignment named four edits and L1 integrates.
4. **Round 64 left a stale footer date.** It committed 2026-10-24 00:28 -0300 but the footer still reads `Counts checked 2026-10-23`. `FOOTER_RE` captures the date and nothing checks freshness, so this is debt, not a failure. The patch bumps the date to the actual measurement day.
5. **Polysemy survives word boundaries** (`hunting-foraging-subsistence.md`: `game` = quarried animals; `civilizations/maya-classic.md` etc. match incidental words). Partial one-way owners named in the bullet are the ones with standing game content and line refs: `civilizations/taino.md`:90 (ballgame), `civilizations/greece-classical.md`:89 (athletic competition), `culture-material/calendar-festival-systems.md`:124 (assembly and games cycles); `olmec.md`:131 and `music-instrument-lexicon.md`:90 are listed in the patch's evidence block.

## Touched surfaces

- Written: `.ufo/waves/round-65/stage/readme-patch.md`, `.ufo/waves/round-65/w1/ScribeReadme.md`.
- Read only: `corpus/README.md`, `corpus/knowledge/**` (counts, topic scan), `corpus/knowledge/linguistics/language-socialization-and-acquisition.md`, `corpus/SOURCES.md` (not modified), `reports/round-65/{claims.json,accept-c.py,telemetry/dry-run-c.txt,telemetry/controls-c.txt}`, `reports/round-28/readme/sweep.py`, `tools/check-readme-heading.py`, `tools/check-readme-revisions.py`, `tools/source-audit-inventory.py`, git objects.
- Not mutated: `corpus/README.md` (still pre-edit sha `c131ffd9…2da32`, `git status --porcelain corpus/README.md` empty), lane jj state, lane Git index. No git/jj write, no commit, no push.

## Out of scope / not done

- No edit to `corpus/README.md`, `corpus/SOURCES.md`, `reports/round-65/claims.json` or any instrument.
- The row's final topic text (DEP-1) and the bullet gloss (DEP-2) await the landed entry; the seat did not invent either.
- Post-landing gate runs are specified, not executed (the entry is absent, so they cannot pass).
- No tool installed or upgraded this seat; nothing recorded for the tooling directive.

## Limits

- Line numbers are for the README at HEAD `17c32302`; E2's two-line insertion shifts E4/E5 anchors by two, so the patch keys edits by text anchors and states both readings.
- The baseline sweep reading (exit 0 at 238) is a pre-landing measurement, not evidence for the post-landing tree.
- The ownership scans are lexical: they establish no more than that no filename or topic line owns the register, and a partial-owner list read by line, not by semantic audit.
- Claim-C statement/evidence conflict (finding 1) is reported, not adjudicated; `claims.json` is frozen pre-wave and the canonical judge owns the reading.

Report: .ufo/waves/round-65/w1/ScribeReadme.md
