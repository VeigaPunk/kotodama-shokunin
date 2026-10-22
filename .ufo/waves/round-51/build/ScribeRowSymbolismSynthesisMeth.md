# Scribe row: symbolism-synthesis-method.md — Claim D candidate neighbour

**Seat:** KotodamaR51a3.ScribeRowSymbolismSynthesisMeth
**Date:** 2026-10-22
**Assigned item:** one Claim-D row for the pastoralism entry's section-2 one-owner boundary table; neighbour candidate `corpus/knowledge/myth-symbol/symbolism-synthesis-method.md`; seam = the symbolic taboo and paired-rite consistency rule versus herd production consequences.

## Verdict: ADD

The candidate is a distinct in-corpus neighbour with a real, body-developed seam. It is not filler and not a split of the existing `animal-symbolism` row.

- **Distinct neighbour:** the candidate is not in the §2 table (current first cells: `agrarian-field-system-lexicon.md:56,:62`, `hunting-foraging-subsistence.md:36,:116`, `cuisine-food-lexicon.md:67,:81,:152`, `transport-mobility-lexicon.md:92,:95`, `trade-economy-lexicon.md:69`, `textile-technology.md:22,:27`, `semantic-fields-lexicon-building.md:70,:105`, `fire-fuel-light.md:37`, `animal-symbolism.md:73,:110`, `sacred-kingship-mythic-charter.md:65`, `civilizations/`). `symbolism-synthesis-method.md` is a 12th distinct target.
- **Distinct from the animal-symbolism row (not a split):** `animal-symbolism.md:73` (Nuer "cattle of money" — livestock-as-wealth idiom) and `:110` ("Faunal economy writes the idiom ... Decide which species is the culture's idiom of value") own the **sign content and the value idiom**. `symbolism-synthesis-method.md:69` owns the **method/consistency rule** — "An animal taboo implies a rite; write both or neither." Same myth-symbol partition, different owner claims; the pastoralism body already treats them as separate owners (§10 row 4 cites `:69` for the rule; §10 preamble line 150 hands the signs to `animal-symbolism.md:73,:110`).
- **Real seam:** the pastoralism entry writes the herd's ritual ledger (surplus males, culling, tally-stick count) but the taboo→rite pairing rule lives in the synthesis method; the entry already defers to it twice (evidence below).

## (a) Exact table row to add (after the `animal-symbolism` row, line 39 of the entry)

```
| `symbolism-synthesis-method.md:69` | the rule that an animal taboo implies its paired rite, and the symbol-grammar method that enforces it | the herd's ledger the rite audits — surplus males, culling, the tally-stick count (§10, §11) |
```

**Anchored line, verbatim** (`myth-symbol/symbolism-synthesis-method.md:69`, re-read in the lane worktree):
"No **Prey apologetics**: a hunting culture that keys a prey animal symbolically generates apology and release rites for the kill — the Circumpolar bear ceremonial is the classic case (Hallowell 1926). An animal taboo implies a rite; write both or neither."

The ownership-supporting sentence is "An animal taboo implies a rite; write both or neither." (line 69, 11 words).

**Anchor resolution:** basename unique in `corpus/knowledge` (glob: one hit, `myth-symbol/symbolism-synthesis-method.md`); file length 172 lines ≥ 69, so `symbolism-synthesis-method.md:69` resolves under `boundary-count.py`. The row's first cell carries exactly one backticked anchor → keeps `rows == resolved == distinct`.

## (b) Boundary already developed in the body

The entry already develops this boundary — explicit deferral of the rule to the neighbour — at two places:

- §10 (Ritual, myth and symbol), "Sacrifice economy" row, **line 147**: `an animal taboo implies a rite (`symbolism-synthesis-method.md:69`); sacrifice belongs to myth-symbol`
- §11 (Decision table and build order), step 8 row, **line 163**: `each taboo written with its rite | §10; `symbolism-synthesis-method.md:69``

No new body text is required. Optional prose-level sentence (≤40 words; no external sources; no S-ids above S070; no mention of sign languages), if the L1 wants the boundary sharper outside the table — add to §10 after line 150:
"Where a herd taboo appears in a world, the paired rite follows the neighbour's rule (symbolism-synthesis-method.md:69); this entry supplies only the books the rite counts — surplus males, culling, the tally-stick."

## (c) Falsifier

If the pastoralism entry ever presents a herd taboo without its paired rite, or assigns the taboo→rite rule to any other owner, the row's ownership cell fails. Likewise if the anchored line 69 ceases to state the rule (it currently does). (The row itself must not cite the round's C entry path or any S-id from S071 upward — it cites neither.)

## Evidence / measured state

- `python3 -B reports/round-51/boundary-count.py` run at the lane worktree: `rows=11 resolved=11 distinct=11` exit 0 (before-state; this row alone moves rows to 12; the other three new rows come from sibling scribe seats).
- Candidate `:69` re-read raw at the lane worktree (verbatim quote above).
- `animal-symbolism.md:73,:110` re-read to confirm the distinctness split.
- No files created/modified in the lane other than this report.

## Blockers / unrun checks

None. (Main agent runs the final counter after all four rows land; I cannot land my row in the entry myself — integration is the L1's.)
