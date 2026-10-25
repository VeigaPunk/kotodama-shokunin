# MutRegistryCollision — verdicts

Mutation tests of the id-collision guard for the shokuknow adoption
(claim C leg COLLCHECK). Contract extraction pattern:
`grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}'`; guard = extraction on both
sides + set intersection (`comm -12`).

| # | fixture | mutated point | detector output | verdict |
|---|---|---|---|---|
| (a) | reg-slice-a.md: indented `  \| S874 \|` row (2 leading spaces), staged slice contains S874 | indent tolerance | reg={S874,S900}; staged={S874,S875}; intersection={S874} | **caught (killed)** — no false negative on indented rows |
| (b) | reg-slice-b.md: `\| S874 \|` at column 0, staged slice contains S874 | column-0 row | reg={S874,S901}; staged={S874}; intersection={S874} | **caught (killed)** — no false negative on column-0 rows |
| control | control-reg {S900..S902} vs control-staged {S910,S911} | pristine baseline | intersection empty | **no false positive** |
| probe | probe-reg-indent4.md: 4-space indented S874 row | indent boundary | extraction empty (no match) | **missed, by design** — pattern caps leading whitespace at 3; documented limitation, not a regression |
| (c) | real lane `corpus/SOURCES.md` vs staged shokuknow `SOURCES.append.md` | real bytes | 797 reg-ids (S001..S873) ∩ 132 staged-ids (S859..S990) = **S859..S873 (15)**; S874/S875 ∈ staged, ∉ reg-ids | **collision caught; adopted NEW ids S874/S875 are next-free** — matches COLLCHECK expectation |

Notes:
- No bytes were modified by the detector (read-only grep/comm); before/after hashes in `hashes.txt`. Restoration N/A.
- Real staged set is contiguous S859–S990 (132 rows, seq-check missing=0); the overlap band is the first 15 ids S859–S873, all caught by the guard.
- Real registry is 797 unique ids S001–S873 (no duplicates); S874/S875 absent → the adoption's two new ids avoid every staged collision.
- Adjacent observation (not part of the guard): the wave's existing `reg-to-staged.txt` keys three ids with stray backticks (`S807``, `S812``, `S835``); those lines are not markdown-table rows so the guard pattern does not apply, but any other parser of that map should strip them.
