# ScribeReadmePlan — corpus/README.md delta draft (claim C, coverage)

Seat: leaf scribe (`L1-kotodama-r66.ScribeReadmePlan`), no dispatch. Draft only; the L1 integrates
and is the only committer. No `corpus/` byte, git index or jj state was touched.

## Behavior delivered

`stage/readme-plan.md` — a unified diff against `corpus/README.md` (4 hunks, 12,218 bytes), the
row/topic contract, the TOPIC-trap evidence, a tested one-row rewrite fallback and the post-landing
verification list. Companion bare diff `stage/readme-plan.diff` (byte-identical to the embedded one,
measured), pre-applied whole file `stage/_readme-build/README.new.md`
(sha256 `ea9276354734acf10a8c9f8c7174f4c09397efe82eb31c6da36d222ce2fee350`).

| # | anchor | old -> new |
|---|---|---|
| 1 | above `revision: 2.17` | new `revision: 2.18` block; new entry named **without** `.md` |
| 2 | `## culture-material/ (32)` (l.373) | `(32)` -> `(33)` |
| 3 | between rows at l.398 `ritual-garments.md` and l.399 `sumptuary-law-rank-display.md` | one row, filename order, entry `- topic:` payload verbatim |
| 4 | after the Round-65 frontier bullet | Round-66 bullet naming partial owners; `Total knowledge entries: 239.` -> `240.`; footer `(total 239 … 30/29/32/29/24/95)` -> `(total 240 … 30/29/33/29/24/95)` |

Counts, measured: `ls corpus/knowledge/<part>/*.md | wc -l` = 30/29/32/29/24/95 = 239;
`python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge` ->
`totals.files 239`. After landing: culture-material 33, total 240, vector `30/29/33/29/24/95` in the
sweep's canonical `PARTS` order (the order the footer already prints).

## Gates measured on the draft (not on the lane)

- `git apply --check stage/readme-plan.diff` -> **exit 0** at tip `94209e8f…`
  (`git diff <base> -- corpus/README.md` empty, so hunk line numbers are exact).
- End-state sweep with `reports/round-28/readme/sweep.py`'s own `sweep()` over a scratch tree
  (symlinks to the 239 files + a synthetic entry carrying the frozen topic): **`ok True`, rows 240,
  files 240, totals_line 240, totals_ok True, footer_ok True, topic_mismatch [], orphan_rows [],
  header_drift {}**, `footer_live {total 240, [30,29,33,29,24,95]}`.
- Same README against the live tree (entry absent): `rows 240 files 239`, header drift
  `culture-material 33 vs 32`, one orphan row, `footer_ok False` — the only residual is the missing
  entry file, the expected pre-landing state.
- `accept-c.py`'s **TOPIC leg replayed line-for-line** on the draft: first matching line is the
  index row, payload substring test **True**. Negative control (`.md` re-inserted into the revision
  note) flips the first match to the revision line and the leg to **False** — the trap is real and
  the draft avoids it by construction.
- `tools/check-readme-revisions.py --readme <new>` -> exit 0, findings 0 (labels strictly decreasing
  from 2.18; one carried `REVISION-ORPHAN` for the round-28 unheaded paragraph).
- `tools/check-readme-heading.py --readme <new>` -> exit 0, findings 0.

## Findings

1. **Frozen inputs arrived mid-draft.** `stage/entry-spec.md` was absent at first read; it appeared
   during the seat and its §2 `- topic:` payload replaced my provisional wording byte-for-byte, and
   its §1 documents the TOPIC first-match trap (revision note must not carry `.md`). The plan now
   matches spec §5 R1-R5 plus the frontier bullet this item owns. Any residual divergence is in
   hunk 4 only, which the spec labels optional.
2. The frontier bullet names `cuisine-food-lexicon.md` (grave-incense chopsticks `:93`, `:139`) and
   `funerary-material-culture.md` (`/cosmetic/` in its own gap/couples prose) as *passing mentions*,
   not partial registers. It deliberately omits `craft-artisan-lexicon.md`: those four hits are the
   temper-line word *nioi* ("scent"), a lexical accident — naming it would inflate the owner set.
   Named partial scopes: `adornment-body-codes.md` (cosmetic ×8), `bathing-and-body-hygiene.md`,
   `vessel-container-lexicon.md`, `timekeeping-instruments.md` (`:26` incense clocks),
   `sogdian-silk-road.md` (`:149` *küji* loanword).
3. Base ownership re-measured with claim C's own census command: **0** filename owners at
   `94209e8`. That command's exit 1 (no match) is the evidence, not an error.
4. Convention, stated: the footer's "Superseded reading" paragraph has not been appended to since
   revision 2.0 and the tail "Index rows re-measured" block stops at round 35 — this delta follows
   that precedent and touches neither. `Counts checked 2026-10-24` and its command stay unchanged and
   remain true; only the two numbers move.
5. Hunk 1 is the only hunk no counter checks, and per the replay it is the one that can *break* the
   counter if spelled with `.md`. If the L1 wants a minimal diff, dropping hunk 1 keeps all measured
   legs green — but then the file loses its 2.18 changelog entry, which every landing since 2.5 has.

## Touched surfaces

Writes, all inside the wave draft area: `stage/readme-plan.md`, `stage/readme-plan.diff`,
`stage/_readme-build/{README.orig.md,README.new.md,readme.diff}`, this report. Scratch symlink tree
and a sync-test lane were created and removed; the lane's `corpus/README.md` still hashes
`0c04517bcd485feb64b283d934db2037552f5d771449374a5a36f9cb3b26d3e7`. No tool installed or upgraded.

## Out of scope / not verified here

- The entry file, `corpus/SOURCES.md` rows S777-S800 and `accept-c.py` — other seats.
- Whether the 24 registry rows support every word of the frozen topic (claim C `review_only`).
- `accept-c.py` was not run: it needs the entry and the registry rows. Its TOPIC leg was replayed
  here in isolation; its SWEEP leg is the round-28 sweep measured above.

Report: .ufo/waves/round-66/w1/ScribeReadmePlan.md
