# Guard proof — CORPUS.md item-10 id-collision extractor (round 75, ExecRenumber)

Purpose: prove, before this lane's first append under prompt §6 item 10, that the
id-collision extractor sees every row shape the census parser sees, and that the
old column-zero-only pattern is the false-green the contract warns about.

Contract clauses under test (`/home/vgpnk/Projects/shokunin/CORPUS.md`):

- maintained parser note: "accepts 0–3 leading ASCII spaces before Markdown table rows and
  headings; 4 or more spaces are indented code and are ignored".
- §6 item 10: extractor `^ {0,3}\|[[:space:]]*S[0-9]{3,}`; "a column-zero-only pattern
  false-greens an indented collision".

## Fixtures

`make-fixtures.py` builds six mirror trees `mirror-<name>/corpus/SOURCES.md`:

- each registry is the real lane registry at base `f556d1049fe651d3d63975600b13acd9fb686f15`
  (808 rows, sha256 `c8da0a5a765de26506a1c4d9b66d9b47c9ffe4e0d62a87fc510077a7f83c5614`)
  with ONE planted row inserted immediately after S884, inside the `## Registry` table;
- the planted row is a clone of lane row S884 with the id cell set to a STAGED id the lane
  does not hold at base (S985, S986, S987, S988, S989), its URLs rewritten to
  `example.invalid/guard-proof/planted-<id>.pdf`, and its kind/tier/status/used-by cells
  normalised to `paper` / `A` / `queued` / `—`, so the planted row introduces **no new
  census finding** and the ONLY difference between the control and a planted fixture is
  the id collision itself;
- indent per fixture: `control` = none (the real registry, byte-identical), `1sp` = 1 space,
  `2sp` = 2 spaces, `3sp` = 3 spaces, `4sp` = 4 spaces (indented code per the census
  parser note), `tab` = one leading TAB (the Markdown table-row grammar is spaces, not
  tabs);
- `corpus/knowledge` and `corpus/lessons` are symlinks to the lane's real dirs and
  `SKILL.md` is a symlink, so the census `used-by` existence check (E11) resolves exactly as
  it does on the lane.

## Command

    python3 make-fixtures.py <root>        # builds mirror-<name>/ trees
    sh run-guard.sh <root> <out>            # runs the extractor on each fixture

Each fixture runs the exact item-10 pair plus the column-zero control pattern and the census:

    ITEM10='^ {0,3}\|[[:space:]]*S[0-9]{3,}'
    COLZERO='^\|[[:space:]]*S[0-9]{3,}'
    grep -oE "$ITEM10" <registry> | grep -oE 'S[0-9]+' | sort -u > <label>.reg-ids
    comm -12 <label>.reg-ids <staged-ids> > <label>.collisions
    sources-census.sh census   --file <registry>
    sources-census.sh validate --file <registry>

## Observed (`out/*.summary.txt`, 2026-10-27)

| fixture | census rows | ITEM10 ids | ITEM10 sees the plant | collisions | collisions name the plant | COLZERO sees the plant | census exit / findings |
|---|---|---|---|---|---|---|---|
| control | 808 | 808 | 0 (no plant) | 26 | 0 | 0 | 0 / 31 (all W04) |
| 1sp | **809** | **809** | **1** | **27** | **1** | **0** | 0 / 31 (all W04) |
| 2sp | **809** | **809** | **1** | **27** | **1** | **0** | 0 / 31 (all W04) |
| 3sp | **809** | **809** | **1** | **27** | **1** | **0** | 0 / 31 (all W04) |
| 4sp | 808 | 808 | 0 | 26 | 0 | 0 | 0 / 31 (all W04) |
| tab | 808 | 808 | 0 | 26 | 0 | 0 | 0 / 31 (all W04) |

- 1sp, 2sp and 3sp: the planted staged id is counted by the census (`rows 809`), seen by
  the item-10 extractor, and **reported as a collision** by `comm -12` against the staged
  id list — with **no new census finding**, so its appearance is not an error artefact;
- 4sp: ignored by both the census (`rows 808`) and the extractor — the code-block control
  behaves as CORPUS.md says;
- tab: also ignored by both. A tab-indented row is not a Markdown table row at all (the
  grammar is spaces), so it is not a row for the census and not a row for the guard;
- the column-zero-only pattern misses all three indented plants: the false-green is
  reproduced, so the 0–3-space pattern is the one to ship.

## Real registry (what the round actually runs)

`out/real.summary.txt` and `out/real-collision-set.txt`:

    ITEM10 reg-id count: 808
    staged-ids count: 132
    collisions count: 26
    collisions: S859 S860 S861 S862 S863 S864 S865 S866 S867 S868 S869 S870 S871 S872 S873 S874 S875 S876 S877 S878 S879 S880 S881 S882 S883 S884
    adopted lane ids S885..S893 present in reg-ids: 0
    adopted lane ids S885..S893 present in collisions: 0
    COLZERO pattern id count: 808

The 26 collisions are staged-vs-lane numeric overlaps whose documents are all unrelated
(0 of 26 share a normalized URL), so the intersections are namespace drift, not duplicate
registrations; the guard's acceptance is *by document*, not "collisions is empty" — which is
unattainable while the package keeps its S859–S884 rows. The adopted lane ids S885–S893
are free: none is in `reg-ids` and none is in `collisions`.

See `../id-renumber-map.json` for the by-document map, the per-id lane/staged document
table for every collision, and the post-adoption cross-namespace overlap table.
