# Guard proof — CORPUS.md item-10 id-collision extractor (round 74, ExecRenumber)

Purpose: prove, before this lane's first append under prompt §6 item 10, that the collision
extractor sees every row shape the census parser sees, and that the old column-zero-only
pattern is the false-green the contract warns about.

Contract clauses under test (`/home/vgpnk/Projects/shokunin/CORPUS.md`):

- maintained parser note: "accepts 0–3 leading ASCII spaces before Markdown table rows and
  headings; 4 or more spaces are indented code and are ignored".
- §6 item 10: extractor `^ {0,3}\|[[:space:]]*S[0-9]{3,}`; "a column-zero-only pattern
  false-greens an indented collision (proven on a scratch `  | S002 |` fixture".

## Fixtures

`make-fixtures.py` builds four mirror trees `mirror-<name>/corpus/SOURCES.md`:

- each registry is the real lane registry (804 rows, sha256
  `93d6046444f2170e14514b2cc50cd21267a9592dc319513dd79fbffc3d018774`) with ONE planted
  row inserted immediately after S880, inside the `## Registry` table;
- the planted row is a clone of lane row S880 with the id cell set to `S883` — a staged id —
  and its two URLs rewritten to `example.invalid/guard-proof/planted.pdf`, so the row is a
  valid new 11-column row that can never be dismissed as a duplicate;
- indent per fixture: `control` = none (real registry), `2sp` = 2 spaces, `3sp` = 3 spaces,
  `4sp` = 4 spaces (indented code);
- `corpus/knowledge`, `corpus/lessons` and top-level `SKILL.md` are symlinks to the lane's real
  objects, so the census `used-by` existence check (E11) resolves as it does on the lane.

## Command

    sh run-guard.sh          # out/*.summary.txt holds each block below

Each fixture runs the exact item-10 pair plus the column-zero control pattern and the census:

    ITEM10='^ {0,3}\|[[:space:]]*S[0-9]{3,}'
    COLZERO='^\|[[:space:]]*S[0-9]{3,}'
    grep -oE "$ITEM10" <registry> | grep -oE 'S[0-9]+' | sort > <label>.reg-ids
    comm -12 <label>.reg-ids guard-proof/staged-ids > <label>.collisions
    sources-census.sh validate --file <registry>
    sources-census.sh census   --file <registry>

## Observed (out/*.summary.txt, 2026-10-25)

| fixture | census rows | ITEM10 ids | ITEM10 sees S883 | collisions | COLZERO sees S883 | census exit / findings |
|---|---|---|---|---|---|---|
| control | 804 | 804 | 0 | 22 | 0 | 0 / 28 (all W04) |
| 2sp | **805** | **805** | **1** | **23** | **0** | 0 / 28 (all W04) |
| 3sp | **805** | **805** | **1** | **23** | **0** | 0 / 28 (all W04) |
| 4sp | 804 | 804 | 0 | 22 | 0 | 0 / 28 (all W04) |

- 2sp and 3sp: the planted `S883` is counted by the census (`rows 805`) and caught by the
  item-10 extractor (`collisions` 23, `S883` present), with **no** new census finding — a
  valid row, so its appearance is not an error artefact.
- 4sp: ignored by both the census (`rows 804`) and the extractor — the code-block control
  behaves as CORPUS.md says.
- the column-zero-only pattern misses the planted id in both 2sp and 3sp: the false-green is
  reproduced, so the 0–3-space pattern is the one to ship.

Fixtures and outputs are committed scratch; the mirrors are disposable and regenerate from
`make-fixtures.py`.

## Real registry (what the round actually runs)

`out/real.summary.txt`:

    ITEM10 reg-id count: 804
    ITEM10 sees any theme id S883/S884/S899/S900: 0
    collisions count: 22
    collisions: S859 S860 S861 S862 S863 S864 S865 S866 S867 S868 S869 S870 S871 S872 S873 S874 S875 S876 S877 S878 S879 S880
    collisions containing a theme id: 0
    COLZERO pattern id count: 804

The 22 collisions are staged-vs-lane numeric overlaps whose documents are all unrelated
(0 same-document pairs by normalized URL); the four theme staged ids are not among them.
See `../id-renumber-map.json` for the by-document map and the premise check.
