# ScoutGapMed — claim-C gap scout (round 67, w1)

## Findings

**Gap CONFIRMED** at base ad5b52b0ab5691358cd38718ab75649dc9916f9a.

1. Filename census prints **0** — no file in `corpus/knowledge` (459 corpus files, 34 in
   culture-material) carries medicin/healing/physician/remedy/surgery/apothec/hospital/
   leech/physick/doctor/shaman/curander/herbal in its name. `medicine-healing-codes.md`
   does not exist at base.

2. Topic-line sweep returns exactly 6 owners, all partial-scope and matching the claim's
   expectation (bathing / scent prophylaxis / myth-symbol purity):
   - `civilizations/haudenosaunee.md` — "False Face medicine traditions" as a boundary
     (living-tradition exclusion), not register ownership.
   - `civilizations/mongol.md` — "shamanic vocabulary" inside a language/culture entry.
   - `culture-material/scent-perfume-aromatics-codes.md` — "status and disease codes"
     inside scent practice; the pomander row (S791) is prophylaxis-as-scent.
   - `myth-symbol/amulets-talismans-apotropaic-marks.md` — disease/plague as one danger
     class the apotropaic object answers.
   - `myth-symbol/sacred-kingship-mythic-charter.md` — plague as observability channel.
   - `myth-symbol/sacred-topography-pilgrimage.md` — "healing archive" inside the
     ex-voto economy.
   Plus body-level §8 of `bathing-and-body-hygiene.md` ("Health, medicine and the
   hygiene revolution") which explicitly owns only hygiene infrastructure and
   "let[s] the medicine be argued."

3. Sibling ownership: zero substantive hits in lore-shokunin / chousa-shokunin — only
   `.ufo/waves/round-29` receipt JSONs in chousa matched (fixtures, not canon). The
   register is unclaimed fleet-wide; standard lore handoff line suffices.

4. Registry boundary (supports ROWS/APPEND legs): base `corpus/SOURCES.md` has 724
   `| S*` rows, max id **S800**. S801–S804 vacant (Ca disposition rows), S805–S828 free
   for the 24 mined claim-C rows. S753 = Penn Museum mancala row, the one declared
   in-place used-by flip.

## Design finding (corroborated, resolved by L1)

Surface conflict verified independently: `accept-ca.py` D4 (line 235) requires
`rej_opened_today >= len(R66_REJECTS)+2 = 6` rejected rows opened 2026-10-24, i.e.
>=2 new rejected ids beyond S801-S804; `accept-c.py` APPEND (lines 357-375) bounds
appended ids to `NEW_IDS(S805-S828) | EXTRA_IDS(S801-S804)` — under a single lands
commit the two counters are jointly unsatisfiable. **L1 resolution (no revision):
per-claim lands separation** — C's receipt runs at A_c (only S801-S804 + S805-S828
appended over base; S801-S804 land earlier at A_r so EXTRA_IDS covers them); Ca's
receipt runs at later A_ca carrying the S829+ rejects and round-67 lesson. Joint
predicate satisfiable as sequenced. Cosmetic residue: dead `new_rejects` variable
at accept-ca.py:232. Also noted: 22 base rows already carry status `rejected`
(opened earlier — they don't count toward D4's today-dated floor).

## Confidence

High on the gap (two independent sweeps + sibling check agree). Medium on sibling
exhaustiveness: lore-shokunin content grep was filename+text `grep -rliE`, no LSP
server serves those repos — grep is the literal fallback (recorded per protocol).

## Remaining unknowns

- Row content for S805–S828 (mining is a build-seat job; gap seat only verified vacancy).
- Whether `bathing-and-body-hygiene.md` §8 needs a one-way pointer *to* the new entry —
  recommended but belongs to the builder's Boundaries pass.

## Tools

None installed (git + grep sufficed; pacman paused per guard, nothing needed).

Report: .ufo/waves/round-67/w1/ScoutGapMed.md
Detail: .ufo/waves/round-67/rows/ScoutGapMed/gap.md
