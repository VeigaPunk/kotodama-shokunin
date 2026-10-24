# ScribeGateRows — round 66 (kotodama-shokunin), 2026-10-24

## Behavior

Drafted the round-66 lesson Gate at `.ufo/waves/round-66/stage/gate-rows.md` from the fragments
under `.ufo/waves/round-66/rows/`, in the round-65 `## Gate` shape. Result at 12:20Z:

- **19 rows verified and paste-ready**: S776 (my re-derivation of the S753 repair) plus 18 of
  the 24 claimed ids — S779, S780, S781, S782, S784, S785, S786, S787, S788, S789, S790, S791,
  S792, S793, S794, S796, S799, S800.
- **2 rows blocked with the reason named**: S783 (nested straight quotes inside its anchor),
  S795 (capture is the JSTOR landing page, not the cited archive.org PDF).
- **4 rows awaiting fragments** (absent on disk): S777, S778, S797, S798.

No quote was invented, paraphrased, trimmed or re-quoted; each is the fragment's own anchor
string, and I re-located it myself in the fetched live body, capture body or PDF text before
gating it. Fragments were read in waves as seats published them (8 → 12 → 20 in-range plus 4
out-of-range at the last sweep).

## Gates

- **Shape validated by the frozen tool, not by eye**: the 19 drafted rows were extracted into a
  synthetic `## Gate` document and run through `python3 -B tools/check-gate-quotes.py
  /tmp/lesson-66-shape.md` → `GATE_QUOTES: 0 findings`, exit 0. Quote-run word counts 13-25
  (S779 and S796 sit exactly at the 25-word cap).
- **Round-65 shape reproduced exactly**, including the `https://` scheme on every capture
  (R65-M3): `- S### | <live URL> (<capture URL>) | 2026-10-24 | "<quote>"`.
- **Anchor verification by me**: every gated quote locates verbatim at its Wayback capture
  (200; byte counts in the draft's probe table) and at the live URL wherever the live host
  answers. S776's quote locates in the fresh capture `20261024111013`, and CDX shows that
  capture and `20250926172224` carry the same digest
  `F5PON6QPZ4DXOBF5DE2MQCTJPNVBUZVC` — the actual ground for "replays byte-exact". The old
  timestamp no longer replays its own bytes (HTTP 302 → the new capture), so it must not be
  restored.
- **S776 disposition written**: supersedes S753's capture for the same live URL; S753's row
  stays `mined`, the games entry re-points `(S753) -> (S776)` and cites S753 zero times
  (`accept-ca.py` D1 counts both directions).

## Touched surfaces

- Wrote `.ufo/waves/round-66/stage/gate-rows.md` (~20 KB, draft, uncommitted).
- Wrote `.ufo/waves/round-66/w1/ScribeGateRows.md` (this report).
- Read-only in the lane: `corpus/lessons/round-65.md`, `corpus/SOURCES.md` (S750/S753/S775
  cells), `tools/check-gate-quotes.py`, `tools/check-row-fragments.py`,
  `reports/round-61/reopen-quote.py`, `reports/round-66/{claims.json,accept-c.py,accept-ca.py}`,
  `reports/round-66/telemetry/{s753-recapture.txt,seat-evidence.txt}`,
  `.ufo/waves/round-66/spec-v2.json`, 24 `rows/*/row-S*.txt` fragments.
- Scratch only under `/tmp` (`s753-fresh.pdf`, `s753-plain.txt`, `bedini.pdf`, `bedini.txt`,
  `body786.bin`, `lesson-66-shape.md`). No product code, no registry/lesson edit, no git/jj
  write, no tool install or upgrade.

## Out of scope

- Writing the final Gate into `corpus/lessons/round-66.md` (absent; L1 integrates).
- Mining S777/S778/S797/S798, repairing S783's anchor, re-capturing S795, trimming over-long
  teaches cells, minting S776's registry row, and any tool/receipt repair named below.

## Findings

1. **`s753-recapture.txt` would fail D1 as it stands.** `accept-ca.py` requires the literal
   `QUOTE = "Versions of mancala are traditionally played across Africa and Asia"` in the
   receipt; the 1413-byte receipt (11:35Z) has **0** occurrences → `bad=['quote']`. Everything
   else D1 needs is there (live 200 pdf, `20261024111013`, `S776`). Its disposition line
   "committed capture 20250926172224 replays PDF not pdf" is undecodable and contradicts the
   receipt's own later `old_replay_status=200`.
2. **S783's anchor is malformed** — `"first-named, alcohol-based perfume, "Hungary water" is
   believed…"` embeds straight quotes; `check-row-fragments.py` reports `quote-words: S783:5`
   (floor 8) and a Gate line would split into two spans. Evidence itself is fine (live 200,
   capture `20201101061450` 200).
3. **S795's capture is not same-page** — `capture-url-mismatch: https://jstor.org/stable/1005923
   != https://archive.org/download/…1005923.pdf`; the fragment states the reason (no capture for
   that download URL, fresh save HTTP 523). Its quote is also OCR-interleaved in the 8.75 MB
   PDF (`By burningincense[we] knowthe | night, With graduated candle…`), so a contiguous test
   fails while the poem is plainly present — name the page, don't call it fabricated.
4. **Nine teaches cells exceed the frozen 240 cap** — S789 260, S790 258, S791 242, S792 260,
   S793 256, S794 264, S795 249, S796 271, plus out-of-range S801 249.
5. **The fragment checker hardcodes the round-65 entry** (`ENTRY = …/games-play-sport-contests.md`,
   no `--entry` flag), so a round-66 run emits a `used-by` finding for *every* row
   (`FRAG: 33 finding(s) in 24 file(s)`). Tool staleness, not row defects — do not route them.
6. **S801-S804 are outside the frozen claim range.** `ScoutReject01/02` are spec'd to
   "admit-or-reject for a row slot S801/S802", and `row-S801.txt`…`row-S804.txt` all exist as
   `mined` rows naming the scent entry. claims.json C says "exactly 24 … S777-S800" and
   `accept-c.py`'s SET leg iterates only S777-S800, so an admitted out-of-range row would land
   undetected and falsify the count.
7. **Id-counting bypass in the QUOTES leg** — `accept-ca.py` counts ids anywhere in the lesson
   (`len(gate_ids) >= 25`) and the checker's `ROW` regex needs only `- S<id>`. Pasting the
   draft's untouched `awaiting fragment` list would satisfy the count with zero anchored
   quotes. The draft says so; each pending line must be replaced, never supplemented.
8. **Captures ship with transfer encodings** — S782's capture is gzip, S786's is
   `content-encoding: zstd` (9860 B on the wire, 45391 B decoded); a plain `curl | grep` calls
   both quote-absent. Same class: `pdftotext -layout` breaks two-column PDFs and reports the
   S753 quote as absent while plain `pdftotext` finds it.
9. **archive.org transport flaps on this host** — HTTPS refused (curl 7 / 000) at 11:34Z and
   11:38Z, fine at 11:36Z, 11:45Z, 12:10Z; HTTP:80 refused where HTTPS worked seconds later.
   Every 000 in this session re-probed to 200. A `000` must not be routed as capture death.
10. **S781's live server answers 403 to `-A Mozilla`** today (200 with a full Chrome UA,
    93,515 B), so the fragment's quoted UA no longer reproduces; the capture locates the row,
    which is the round-65 challenge class, with the access note corrected.

## Report

`.ufo/waves/round-66/w1/ScribeGateRows.md`
