# Scribe row report: numerals-and-measures.md as Claim-D neighbour (round 51, attempt 3)

Seat: KotodamaR51a3.ScribeRowNumeralsAndMeasures (leaf; no subagents dispatched).
Task: Claim D candidate row — neighbour candidate `corpus/knowledge/linguistics/numerals-and-measures.md` for the pastoralism entry's §2 one-owner boundary table.

## Verdict: ADD

`numerals-and-measures.md` is a distinct in-corpus neighbour not named in the pastoralism entry's §2 table (current 11 rows: lines 31–41 of `pastoralism-animal-husbandry.md`, re-read at the lane worktree; the file's bytes equal base `bff83ba`). The seam is real, not filler and not a split of an existing row:

- The pastoralism entry already touches counting language twice: §5 line 75 frames the herd vocabulary as a property index — "what an owner must count" — and §10 line 144 quotes the Sumerian farmer's taunt "Every night your count is made and your tally-stick put into the ground" (S064). Tally sticks and tally marks are counting technologies owned by `numerals-and-measures.md` (§5, line 109).
- `numerals-and-measures.md:101` explicitly names "head of cattle" as a counting unit it owns: "This entry owns only the *words* — mensural classifiers, counting units (*pair*, *head of cattle*, *dozen*, *score*)". This is the exact expected seam: counting units and tallies (numerals-and-measures) versus herd composition and wealth counts (pastoralism).
- The row is not a split of the existing `trade-economy-lexicon.md:69` row (money words) nor of `semantic-fields-lexicon-building.md:70,:105` (vocabulary field): it names a different file owning different content.

## Drafted row (ready to paste into §2 table, after row at line 41)

```
| `numerals-and-measures.md:101,:109` | counting units and measure words ("head of cattle", pair, dozen); tally marks and counting technologies | the herd composition and wealth counts the words denote; the counting words and tallies themselves stay there |
```

Anchored line quoted verbatim (re-read at `numerals-and-measures.md:101`):

> "This entry owns only the *words* — mensural classifiers, counting units (*pair*, *head of cattle*, *dozen*, *score*), and the way a classifier system maps a noun inventory into count classes."

Line 109 supports the tally part of the ownership cell (verbatim): "**Tally marks** are the material counterpart: one mark per unit, grouped for legibility." Both anchors resolve; the row's two anchors name one distinct target file.

## Boundary development (drafted sentence, ≤40 words)

The pastoralism body touches the seam (§5:75, §10:144) but never names the counting-words owner, so the boundary needs one sentence. Insert at end of §5 (after line 85, before `## 6.`):

> Counting words and tally records — "head of cattle", tally marks — belong to `numerals-and-measures.md:101,:109`; this entry owns the herd facts those counts denote, not the counting system.

(30 words; no new external sources, no S-ids above S070, no mention of sign languages; pastoralism entry stays at 205 lines after insertion, under the 250-line cap.)

## Falsifier

If a reviewer finds that `numerals-and-measures.md:101` does not support the ownership cell (i.e., the anchor does not say "head of cattle"/counting units), or that the pastoralism body carries no sentence or passage naming the numerals-and-measures boundary, this row fails. A non-author review must confirm the anchor resolves and the row names a distinct neighbour not already in the table.

## Evidence

- `reports/round-51/claims.json` (claim D: before `rows=11 resolved=11 distinct=11`, after required `rows=15 resolved=15 distinct=15`; must-not-cite list does not include numerals-and-measures).
- `pastoralism-animal-husbandry.md:27-41` (§2 table, 11 data rows; no numerals-and-measures row), `:73-85` (§5, property-index line 75, counts-guard line 85), `:138-150` (§10 tally-stick row line 144).
- `numerals-and-measures.md:101` (quoted above), `:109` (tally marks).
- `reports/round-51/boundary-count.py` — counter logic read; not rerun (baseline state documented in claims.json).

## Unrun checks

- `python3 -B reports/round-51/boundary-count.py` (post-edit count 12 with this row alone; final 15 requires the other scribes' rows to land). L1 runs the full count at integration.
- Non-author review of the anchored line's support for the ownership cell (falsifier above).
