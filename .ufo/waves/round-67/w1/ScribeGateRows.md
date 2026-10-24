# ScribeGateRows — round 67 (kotodama-shokunin), 2026-10-24

## Behavior

Drafted the round-67 lesson Gate at `.ufo/waves/round-67/stage/gate-rows.md` in
the round-66 house shape `- S<id> | <live URL> | 2026-10-24 | "<anchor quote>"`,
then filled it mechanically from the row fragments as they landed. State at
12:48Z:

- **All 28 ids filled from their own fragments** (32 Gate lines total): S805–S828
  as mined rows and S829–S832 as this round's rejects (`REJECTED: …; flip: …`
  from each fragment's teaches cell), plus the four S801–S804 dispositions.
- **No MISSING line remains**: the last fragments (S807/S808 from ScoutRow02,
  S827/S828 from ScoutRow12) landed at 12:48Z and were filled verbatim; the
  recipe is in the draft for a final re-run at integration.
- **4 r66 disposition rejects drafted** (S801–S804) with URL, date, anchor quote
  and `REJECTED: …; flip: …`, derived from the r66 row files plus the ownership
  locators their reviews raised; URLs and quoted spans compare byte-equal to the
  r66 `ROW=` cells.
- Includes the fill recipe (`ROW=` cell → Gate line, with the truncation rule
  for >25-word anchors) and the integration notes (reject placement under a
  `###` sub-heading inside `## Gate`; rejected rows carry no quoted body anchor,
  so the Gate preamble's "verbatim quote" sentence does not describe them).

## Gates run (all observed)

| check | command | result |
|---|---|---|
| Gate quote cap / shape | `python3 -B tools/check-gate-quotes.py .ufo/waves/round-67/stage/gate-rows.md` | `GATE_QUOTES: 0 findings`, exit 0 — run before the fill, after the fill and after the S813 cleanup |
| peer re-verification | `w1/RevGateQuotes.md` (12:49Z and 12:52Z) | final bytes: **32/32 Gate lines, 0 issues** — every quoted first span byte-verbatim in its fragment anchor (S807/S827/S828 included), all runs <=25 words (S813 23w + `(cont. in row)`), S801–S804 anchors verbatim in the r66 files with `REJECTED:`+`flip:`, S829–S832 tokens present, checker 0 findings/exit 0; recipe simulated against `row-S813.txt` and matched the landed line |
| fill fidelity | in-memory parse of the draft against every `rows/*/row-S8*.txt` on disk | all 32 Gate lines byte-equal (28 fragment-backed + 4 r66 reject rows) to their fragments' URL + quote/teaches cells; the only flag was S813's deliberate 23-word cap |
| reject-line fidelity (r66) | same parse against `.ufo/waves/round-66/rows/ScoutReject0*/row-S80*.txt` | S801–S804 `URL_EQ` + `QUOTE_EQ`; quoted runs 20/13/17/18 words |
| ownership locators at base | `git show ad5b52b0:<file> \| sed -n '<line>p'` | `adornment-body-codes.md:68` cosmetics H2; `purity-pollution-boundary-systems.md:58` miasma/pharmakos; `sacred-topography-pilgrimage.md:33` P2 relic; `myth-ritual-theories.md:32` contact magic; `SOURCES.md` holds exactly one `S791` row |
| base absence of S801–S804 | `git grep -n "S80[1-4]" ad5b52b0 -- corpus/SOURCES.md` | no output — the ids are free for the disposition append |
| APPEND-vs-D4 arithmetic | replay of `accept-c.py`'s APPEND branch on the base registry + one synthetic S829 row | `appended=['S829'] extra=['S829'] append_ok=False` — conflict resolved by the L1's per-claim lands sequencing (F7) |
| fragment shape lint | cells/kind/tier/teaches-length/capture/opened/used-by over every `row-S8*.txt` | defects named in F6/F8 (no fragment edited — not this seat's file) |

Not run, deliberately: `accept-c.py` / `accept-ca.py` (they stamp a materialized
clone at a lands revision), any network fetch (Gate quotes must come from
fragments; a re-fetch would create a second, unreviewed evidence path), and the
round-67 lesson itself (does not exist; the L1 inlines this draft).

## Touched surfaces

- `.ufo/waves/round-67/stage/gate-rows.md` — new draft.
- `.ufo/waves/round-67/w1/ScribeGateRows.md` — this report.
- Nothing else: no `corpus/`, `reports/`, `tools/`, lane git index, jj state or
  sibling lane was written; git use was read-only (`git show`, `git grep`).

## Findings (full text in the draft's `## Findings`)

- **F1 — fragment lag and moving bytes.** None at 12:37Z; all 28 by 12:48Z, arriving in batches (2→4→6→10→14→18→20→22→24→26→28).
  S805's `teaches` cell changed between two reads (244 chars → 189), so every
  filled line is a snapshot: the L1 must re-run the recipe after the last seat
  returns.
- **F2 — a placeholder Gate is checker-clean** (HIGH). Rows without a quoted
  span produce no finding, and `accept-ca.py:272-276` counts `S8[0-2]\d` ids
  anywhere in the lesson (`gate_ids >= 20`) — the L1's capture-group fix keeps
  the S prefix but not the placement. Inlining the MISSING lines would keep the
  QUOTES leg green with zero anchored quotes. Round-66 class
  (`.ufo/waves/round-66/w1/ScribeGateRows.md` item 7), unfixed apart from the
  threshold (25→20). Do not inline MISSING lines.
- **F3 — S801–S804 are dispositions of verified r66 rows, not bad sources.**
  Their r66 files carry live-200 quotes, same-page captures and `mined`; the
  rejection is fit/ownership (cosmetics owned at `adornment-body-codes.md:68`;
  miasma at `purity-pollution-boundary-systems.md:58`, with the scent register's
  prophylaxis slot already S791; relic adjudication at
  `sacred-topography-pilgrimage.md:33`/`myth-ritual-theories.md:32`; S804's
  anchor has no aromatic content). Registry `teaches` must be rewritten to
  `REJECTED: …; flip: …` for D4.
- **F4 — quote hygiene**: S803 carries a curly apostrophe; S816 and S830 embed
  quoted material of their own. Retyping or assembling a quote is the R66-M2
  class.
- **F5 — reject rows carry no status column** in the Gate; the registry row is
  the durable record.
- **F6 — S829–S832 exist and are fillable, with two length defects.** All four
  fragments are `status=rejected`, `opened=2026-10-24`, `used-by` `—`, carries
  `REJECTED: …; flip: …`, so D4's token test passes. S829's teaches cell is 274
  chars and S830's 311, over the row model's 240-char budget, and both sit at
  `tier=C` where the round's row model asks A/B (legal in the registry — C is a
  lead — but a shape deviation the L1 should decide). Rejected anchors are prose
  findings ("none reachable: …"), not located quotes.
- **F7 — C/Ca id conflict: mechanically real, resolved by lands sequencing.**
  APPEND allows only S805–S828 ∪ S801–S804; D4 needs 6 today-dated rejects in
  the registry. Replaying APPEND on base + one S829 row prints
  `appended=['S829'] extra=['S829'] append_ok=False`. The L1 ruled no counter or
  claims revision: A_r (S801–S804) < A_c (S805–S828, claim C stamped and
  evaluated there) < A_ca (S829+ and this lesson, where D4 counts six). The
  draft records the ruling and its two consequences — S807/S808/S827/S828 are
  critical-path for A_c, and a C receipt re-run at A_ca/tip would print APPEND
  FAIL, so the A_c evaluation is the C verdict (the r66-D3 class, reversed).
- **F8 — the only quote-cap breach is inside a fragment.** S813's anchor cell is
  26 words, over the row model's 8–25 band; the Gate line caps it at 23 words
  (trailing function words dropped) plus `(cont. in row)` so the checker stays
  clean, but the fragment should be shortened and the fill re-run; S814 (246
  chars) and S818 (242) also exceed the 240-char teaches budget at 12:48Z.

## Carried L1 actions (not this seat's writes)

- **Receipt re-stamp overwrote the old bytes (corrected at 12:53Z).**
  RevGateQuotes reported the base receipts pinning `5e8915ac…` against a shipped
  counter hashing `5382ffed…`. My own check finds the pin now equal
  (`dry-run-ca.txt` and `controls-ca.txt` both carry
  `5382ffed6f6c…4353c`, byte-identical to `sha256sum reports/round-67/accept-ca.py`),
  with file mtimes 12:46Z — i.e. the L1 re-ran them after the 12:33Z read, and
  `controls-ca.txt` names "revised counter rev1". The stale-pin HIGH therefore
  does not reproduce. **What does remain:** neither file preserves the earlier
  receipt bytes below a marker (grep for previous/superseded/preserved/marker/
  `5e8915ac` finds nothing), which is QUALITY criterion 17's re-stamp rule; and
  the control set still has no perfect-lesson case that a dead QUOTES leg would
  fail.
- **Lesson draft is a passing skeleton (HIGH):** `stage/lesson-draft.md` has 30
  placeholder Gate rows (316 lines, `gate_ids=24` by the leg's own regex) and
  `tools/check-gate-quotes.py` returns `0 findings`, exit 0. Merge
  `stage/gate-rows.md` as one physical line per row; never land the skeleton.
- **C.lands names the lesson (MEDIUM, records):** claims.json `C.lands` lists
  `corpus/lessons/round-67.md`, which under A_r < A_c < A_ca lands at A_ca, not
  A_c; the lesson's Gate also names S829–S832 whose registry rows land at A_ca.
  Lesson and those rows must travel together, or C.lands is amended as a
  declared change.
- **Registry reject-row hygiene (MEDIUM, reported by RevGateQuotes):** only 9 of
  22 existing `rejected` registry rows carry `REJECTED:` + `flip:`; D4 does not
  read them, but new reject rows should not add to that backlog.

## Out of scope / not done

- No edits to fragments, registry, lesson, README, LOG, SCORECARD, counters or
  claims — all L1-owned; fragment defects are reported, not fixed.
- F7 was resolved by the L1 (per-claim lands sequencing); the draft records the
  ruling, not a decision of this seat.
- No re-open of the S805–S826 live URLs or captures (their VERIFY lines claim
  HTTP 200/403/429 on 2026-10-24); that belongs to RevSourceSupport and
  RevGateQuotes, and this seat wrote no evidence it did not read from a
  fragment.

## Tooling

No install or upgrade. `python3` (stdlib) and the lane's existing
`tools/check-gate-quotes.py` only.

## Report

`.ufo/waves/round-67/w1/ScribeGateRows.md`
