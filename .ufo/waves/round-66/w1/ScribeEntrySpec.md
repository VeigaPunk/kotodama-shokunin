# ScribeEntrySpec — round-66 claim C pre-read/design

Seat: ScribeEntrySpec (leaf, no dispatch). Lane repo `/home/vgpnk/Projects/shokunin/kotodama-shokunin`,
read-only throughout — no git/jj writes, no commits, no product-code edits.
Report: .ufo/waves/round-66/w1/ScribeEntrySpec.md

## Behavior

Read the frozen instruments before designing anything: `reports/round-66/accept-c.py` (all 12 legs,
full body), `reports/round-66/claims.json` (claims C/O/Ca + separability block),
`reports/round-66/telemetry/{dry-run-c,controls-c,census-start}.txt`,
`corpus/knowledge/culture-material/games-play-sport-contests.md` (the round-65 model entry),
`reports/round-28/readme/sweep.py` (regexes + `sweep()` semantics), `corpus/README.md`,
`corpus/SOURCES.md` (row shape, footer, append point).

Wrote the design artifact: `.ufo/waves/round-66/stage/entry-spec.md`.

## Gates — what was measured, not asserted

1. **Frozen-constant census.** `accept-c.py` self-sha `0726b4bc…dda86` (matches `dry-run-c.txt`);
   `NEW_IDS` = S777–S800; `ENTRY` = `corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md`.
2. **Registry state.** Base and tip both carry **701** rows (`^\|\s*S\d{3}\s*\|`); tip-only ids: none.
   So S776 (Ca's supersession row) is **not yet on disk** — S776/S777–S800 are all additions, and the
   append point is `corpus/SOURCES.md` line 731 (`| S775 |`), before the blank line 732 and `## Paths` 733.
3. **APPEND semantics.** Set-equality over full row lines: `missing_old == 0` today, and **any** in-place
   edit of an existing row (including a `used-by` flip) would fail the leg — contrary to the leg's own
   prose ("allowed status/used-by flips logged in the lesson"). Finding F2 below.
4. **TOPIC first-match trap, measured.** `TOPIC` takes `next(l for l in README.splitlines() if "<file>" in l)`,
   i.e. the **first** line naming the entry. The README revision block (lines 3+) precedes the index
   (`## culture-material/` at 373, rows 375–406). Measured on the existing games entry as control:
   first matching line is the revision note (`culture-material entry landed (\`games-play-sport-contests.md\`, games, play,`)
   → `TOPIC leg would be: False`; with the `.md` suffix removed from that note the first match becomes
   the index row → `TOPIC leg would be: True`. The spec's README recipe therefore writes the note as
   `` `scent-perfume-aromatics-codes` `` (no `.md`).
5. **README recipe validated end-to-end** in a throwaway tree (`shutil.copytree` of `corpus/knowledge`
   into `/tmp`, no lane writes), calling `sweep.sweep(modified_readme, root_override=tempknowledge)`:
   `ok True`, `total_files 240`, `total_rows 240`, `topic_mismatch []`, `missing_from_index []`,
   `orphan_rows []`, `header_drift {}`, `totals_line 240`, `totals_ok True`, `footer_findings []`,
   `footer_ok True`. Footer arithmetic confirmed from the live tree: 30/29/32/29/24/95 = 239 → 240 with
   culture-material 32 → 33.
6. **Skeleton measured with the counter's own conditions**: assembled head+skeleton = **137 lines**,
   `h1=1`, `h2=13`, `h3=0`, `- topic:` present, 24 `SLOT S777…S800` markers in id order, zero `(S`
   occurrences (so no ONEID/RESTATE contamination before fill-in), `FILE` leg shape passes.
   `sweep.ROW_RE` matches the produced index row and its captured topic equals the entry's `- topic:`
   text exactly; `sweep.TOPIC_RE` on the assembled entry yields the same string. Topic text: 58 words,
   367 chars, no backticks, one physical line.
7. **RESTATE arithmetic measured with the counter's own functions** (importlib of `accept-c.py`,
   no reimplementation): synthetic row, teaches = a two-clause sentence, quote = a resin/brazier
   sentence →
   `good` bullet `quote_words=6 teaches_cov=0.38 novel=5` PASS;
   teaches pasted verbatim `quote_words=6 teaches_cov=1.00 novel=0` FAIL (cov + novel);
   `short` bullet `Resin burns.` `quote_words=0 novel=2` FAIL (quote).
   Semantics corrected in the spec: the **quote** leg is membership (any order), the **teaches** leg is
   the only in-order one, and `content_words` drops <4-char words, stopwords and anything non-alpha
   (so ids and numerals contribute nothing).
8. **Read-only inventory tool** runs and exits 0 (`tools/source-audit-inventory.py --json --summary
   --root corpus/knowledge`) — used only to confirm the footer's own command is live; the footer edit
   recipe says re-run it for the honest 240.

Not run (deliberately): `accept-c.py` against a landed tree (entry and rows do not exist; the frozen
counter is pre-data and the L1 runs the predicate after integration). No source was opened, no capture
made, no row authored — all 24 slots are targets, not evidence.

## Touched surfaces

- `.ufo/waves/round-66/stage/entry-spec.md` (new, 479 lines) — head block, 13-H2 skeleton with one
  slot per S777–S800 grouped into 8 scent classes, the 11-cell row recipe, RESTATE arithmetic with
  measured examples, the validated README recipe, verification sequence, findings.
- `.ufo/waves/round-66/w1/ScribeEntrySpec.md` (this report).
- Nothing else. No product code, registry, README, lesson, telemetry or lane state was modified.

## Out of scope (explicitly not done)

- No row mining, no blind per-row support judgement, no captures (claims.json `review_only`).
- No S776 supersession row and no games-entry re-point (claim Ca's lands).
- No separability run, no `accept-o`/`accept-ca` work (other seats).
- No tool installs or upgrades this seat (nothing needed).

## Findings

- **F1 (MED, TOPIC trap).** `accept-c` `TOPIC` reads the first README line containing the entry
  filename; a revision note naming the `.md` file makes the leg fail while `SWEEP` still passes, so the
  failure appears only at integration. Fix carried in the recipe: revision note without `.md`.
  Live precedent: README line 4 already names `games-play-sport-contests.md`, so the same leg would fail
  if the games entry were the `ENTRY` under test.
- **F2 (MED, APPEND vs its description).** The leg tolerates no in-place edit at all; the claim text's
  "allowed status/used-by flips" cannot be exercised. Consequence: after claim Ca re-points the games
  entry to S776, S753's `used-by` cell still names the games entry and may not be corrected in place —
  record the flip in `corpus/lessons/round-66.md` instead. The counter cannot detect this staleness.
- **F3 (LOW, CAPTURE escape).** The literal substring `no-capture`/`nocapture` anywhere in the source
  cell satisfies the capture leg. It is a reason string, not evidence; an over-used escape is invisible
  to the counter. Row authors should prefer real same-page captures and justify each escape in the
  row's scope cell.
- **F4 (LOW, HOSTS counts netlocs).** 10 distinct netlocs can be bought with one institution supplying
  most rows. The spec sets a review-time cap of ≤3 rows per institution, which no leg enforces.
- **F5 (LOW, LINK normalization).** `norm_url` drops the fragment and a trailing slash but keeps the
  query, so rows differing only by `#anchor` or `/` collide; compare normalized URLs before writing.
- **F6 (INFO, quote leg shape).** The quote leg counts *occurrences* of quote content words in the
  bullet (`sum(1 for w in qw if w in bw)`), so a quote repeating one word three times could reach
  `>= 3` with fewer than three distinct words. Flagged so the 24 bullets aim at three distinct
  materials/proper nouns rather than exploiting it.
- **F7 (INFO, dependency).** `S776` does not exist at the tip; claim C's `NOHARM` leg permits the games
  entry to change, but the entry's S776 citation lands only with Ca's seat. If Ca does not land,
  claim Ca's D1 leg fails, not claim C's.

## Artifact paths

- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-66/stage/entry-spec.md`
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-66/w1/ScribeEntrySpec.md`

Report: .ufo/waves/round-66/w1/ScribeEntrySpec.md
