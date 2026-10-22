# Scribe report — Claim D candidate row: ritual-liminality

Seat: KotodamaR51a3.ScribeRowRitualLiminality (leaf; no subagents).
Assignment: claim D candidate row, neighbour candidate `corpus/knowledge/myth-symbol/ritual-liminality.md`.

## Verdict: ADD

`ritual-liminality.md` is a distinct in-corpus neighbour not present in the section-2 table's
11 rows; it has a real seam with the herd's production ledger (sacrifice typology and
substitution versus the herd's surplus-male victim pool), it is not filler, and it does not
split an existing row (the nearest existing rows — `animal-symbolism.md:73,:110` signs/idiom,
`sacred-kingship-mythic-charter.md:65` shepherd-king office — own different registers).

## (a) Exact table row

```
| `ritual-liminality.md:65` | sacrifice substitution logic — a lesser life for the owed life (ram for Isaac, qurbani, katashiro) | the herd's culled surplus males are the standing pool of substitute victims; the typology and its ethics belong to myth-symbol, the victim supply here |
```

Anchored line, quoted verbatim, `corpus/knowledge/myth-symbol/ritual-liminality.md:65`:

> `| substitution / proxy | a lesser life for the owed life | aqedah — ram instead of Isaac (Gen 22); Eid al-Adha qurbani (Qur'an 37 names no son; Islamic tradition mostly Ismail); Japanese katashiro paper dolls floated at ōharae (origin of hina dolls) | mercy economics; the discount price of a soul — plot-gold |`

The line supports the ownership cell: it is the substitution/proxy row of the sacrifice
typology table ("a lesser life for the owed life"; ram-for-Isaac, qurbani, katashiro). The
anchor resolves: file is 136 lines, so `:65` is in range; basename is unique under
`corpus/knowledge` (single `ritual-liminality.md`). No S-id, no mention of sign languages, no
new-C-entry path — none of claim D's `must_not_cite` constraints are touched.

## (b) Where the body already develops this boundary

Already developed in `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` §10:

- `:140` — "write the rite from the herd's books outward (`ritual-liminality.md:63`)"
  (the §10 intro already routes rites outward to the same neighbour).
- `:147` — Sacrifice economy row: "offerings drawn from the herd's surplus males
  `(to-verify)` | an animal taboo implies a rite (`symbolism-synthesis-method.md:69`);
  sacrifice belongs to myth-symbol".

Optional strengthening sentence (at most 40 words; no external sources, no S-ids above S070,
no sign languages) the L1 may add after the §10 table (after `:150`), making the substitution
link explicit:

> Substitution extends the ledger: culled surplus males are the standing pool of lesser lives
> for any owed-victim rite (`ritual-liminality.md:65`); the typology stays with myth-symbol.

(24 words.) The new row alone, with `:147`, already satisfies "developed or explicitly
narrowed in the entry body"; the sentence is belt-and-braces, not required. Entry stays well
under 250 lines (now 204).

## (c) Falsifier

- `python3 -B reports/round-51/boundary-count.py` prints anything other than
  `rows=12 resolved=12 distinct=12` (exit 0) after the row lands (before-state verified this
  session: `rows=11 resolved=11 distinct=11`, exit 0).
- A non-author review finds `ritual-liminality.md:65` does not support the "sacrifice
  substitution logic" ownership cell (e.g. reading the line as only about paper dolls).
- The row gains a second anchor in its first cell, or names the round's new C entry
  (sign-languages) or any S-id from S071 upward.

## Evidence

- `reports/round-51/claims.json:18-27` — claim D statement and falsifier.
- `corpus/knowledge/myth-symbol/ritual-liminality.md:65` — anchored line verbatim (above);
  file is 136 lines.
- `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:29-41` — current §2
  table (11 rows; ritual-liminality absent); `:140`, `:147` — §10 body development;
  `:204` — line count.
- `python3 -B reports/round-51/boundary-count.py` — before-state `rows=11 resolved=11
  distinct=11` (exit 0), run at the lane worktree this session.

## Unrun checks

- The counter is **not** re-run on a tree containing the new row (the L1 owns landing the
  row; the L1's verification is the 12/12/12 run).
- No edit was made to the entry (scribe is read-only on product code).
