# MutRegistryCollision — mutation test of the CORPUS item-10 id-collision guard (round 74 w1, kotodama hyaku run 7)

Seat: MutRegistryCollision-3 (leaf; no delegation, no background jobs). Date: 2026-10-25.
Base revision of lane bytes copied: worktree `corpus/SOURCES.md` = sha256 `93d6046444f2170e14514b2cc50cd21267a9592dc319513dd79fbffc3d018774` (registry ends at id S880, 804 rows); staged `SOURCES.append.md` = sha256 `7fb4f488807e8364d204a3081a2e57379d6caafaa92dbab9dfbc381757223754` (132 rows, ids S859..S990, all column-zero).
Writes: this report + fixture under `/tmp/MutRegistryCollision-3/` only. The lane worktree, `$A=.ufo/waves/round-74/assimilation/`, claims.json and every protected path were only read. No git was used (item's "avoid git entirely" option); no pacman (paused); no tools installed (grep/awk/comm/sha256sum + the fleet census script).

## Fixture and detector

`D=/tmp/MutRegistryCollision-3/fix.MDmCXR` (created with `mktemp -d` under the seat dir):

- `D/corpus/SOURCES.md` — byte-identical copy of the lane registry (mutation target; guard input 1).
- `D/SOURCES.append.md` — byte-identical copy of the staged package (guard input 2).
- `D/corpus/knowledge`, `D/corpus/lessons`, `D/SKILL.md`, `D/reports/…` — symlinks into the lane so the census `--file` used-by (E11) check resolves exactly as on the lane.
- `D/mirror/SOURCES.md` — generated per run: registry copy with all staged table rows inserted into the one Registry table (the item-10 pre-append mirror shape).

Detector script: `/tmp/MutRegistryCollision-3/detect.sh`. Per run it emits (artifacts in `D/out/`):

1. **Canonical item-10 pair** (the form the wave's own `assimilation/guard-proof/run-guard.sh` and committed reg-ids/staged-ids artifacts use): `grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' <file> | grep -oE 'S[0-9]+' | sort` on both inputs, then `comm -12` → collisions.
2. **Raw-pair variant** (plausible mis-implementation): `comm -12` on the un-normalized `grep -oE` lines (no second grep).
3. `sources-census.sh validate --file D/corpus/SOURCES.md` (the mutated registry copy).
4. `sources-census.sh validate --file D/mirror/SOURCES.md` (registry + staged rows in one table).
5. sha256 of both fixture inputs.

## Baseline (pristine, after one fixture repair)

First baseline run was **red for fixture reasons, not lane reasons**: lane rows S859/S860 carry `used-by SKILL.md` (a lane-root-relative path), and my first symlink set only covered `corpus/*`/`reports/*` → 2×E11 on the copy. After completing the used-by symlink set, and with the lane's own census re-run read-only just now (`validate --root /home/vgpnk/Projects/shokunin kotodama` → exit 0, `kotodama ok`), the clean baseline (`D/out/baseline2.*`) is:

- guard: 804 reg-ids, collisions = **22: S859..S880** (expected — see acceptance section); raw variant also 22.
- census `--file` on the pristine copy: **exit 0, 0 E** (matches `reports/round-74/telemetry/census-start.txt`).
- mirror census: exit 1 with **E01×125, E11×148, E03×0** — the staged rows as-is are almost all malformed (only 8/132 have 11 cells; the rest E01), and their `recheck`/`used-by` cells carry shell commands (E11). The mirror gate is red for as-is appends, exactly as item 10 requires, but via E01/E11, **not** E03.

## Mutation battery m1..m7 (+m7b control)

Plants were one at a time into `D/corpus/SOURCES.md` (inserted immediately after the Registry header separator, inside `## Registry`), each reverted before the next. Registry sha256 per state: baseline `93d60464…`, m1 `eaeaa45c…`, m2 `6556bdff…`, m3 `a2d11f72…`, m4 `adb096bf…`, m5 `27dec3c3…`, m6 `365bd49f…`, m7/m7b `e6881555…`. "new" = ids in collisions not present at baseline.

| m | plant | canonical guard | raw variant | census `--file` (registry copy) | mirror census | verdict |
|---|---|---|---|---|---|---|
| m1 | `  \| S883 \|` 2-space | **fires**: 805 ids, collisions 23, new=`S883` | missed (22, no new) | rc 0, 0 E — silent | no E03 (staged S883 twin is E01-malformed) | **pass — guard kills** |
| m2 | `   \| S883 \|` 3-space | **fires**: 23, new=`S883` | missed (22) | rc 0, silent | no E03 (same reason) | **pass — guard kills** |
| m3 | `    \| S883 \|` 4-space (code block) | no: 804 ids, 22 | no | rc 0, silent (rows stay 804) | nothing | **pass — correct negative** per census 0–3-space rule |
| m4 | `\|S883\|` no spaces, col 0 | **fires**: 23, new=`S883` (`[[:space:]]*` matches empty) | missed (22; `\|S883` ≠ `\| S883` lines) | rc 0, silent | no E03 | **pass — guard kills** |
| m5 | TAB `\t\| S883 \|` | **no: 804 ids** — pattern `^ {0,3}` excludes tab | no | rc 0, silent — census row gate `^ {0,3}\|` also excludes tab | nothing | **miss, consistent**: one tab = 4 colstops = code block for both detectors; census docstring says "4 or more spaces" and omits tabs (doc gap, no divergence) |
| m6 | `\| s883 \|` lowercase | **no: 804 ids** — pattern requires capital `S` | no | **rc 1, `file→E02→s883`** (id not `^S[0-9]{3,}$`) | E02 s883 | **pass via defense-in-depth** — guard blind, census E02 blocks the append (exit 1), though not as an id-collision |
| m7 | `\| S1005 \|` 4-digit, no staged twin | extracts: 805 ids, `S1005` ∈ reg-ids, but collisions stay 22 | no | rc 0, silent | nothing | **pass — `{3,}` handles 4+ digits**; empty collisions is a namespace fact (no S1005 in staged S859..S990), not a regex miss |
| m7b | m7 + well-formed `\| S1005 \|` twin planted in the staged copy | **fires**: 23, new=`S1005` | **fires**: 23, new=`\| S1005` | rc 0, silent (twin is in the *other* file) | **`file→E03→S1005 duplicate id`** — first E03 of the battery | **pass — positive control proves the census raises E03 for a well-formed in-file duplicate** |

Restoration: after all reverts, `D/corpus/SOURCES.md` = `93d6046444f2170e14514b2cc50cd21267a9592dc319513dd79fbffc3d018774` and `D/SOURCES.append.md` = `7fb4f488807e8364d204a3081a2e57379d6caafaa92dbab9dfbc381757223754` — byte-identical to the source files; a final `restored` detector run reproduces baseline exactly (`collisions` and `reg-ids` outputs `diff`-identical to `baseline2`).

## The acceptance question — collisions non-empty is expected here

- Pristine guard collisions are exactly S859..S880, and **all 22 are different-document id collisions**, not benign same-document leftovers: 20/22 have differing first-URLs lane-vs-staged, 2 (S859, S860) have no URL in the lane row at all; 0/22 match. Concrete: staged S877 = `www.jstage.jst.go.jp/article/jinbunxshakai/2/8/2_1/_pdf` vs lane S877 = `www.philol.msu.ru/~sidorova/files/conlangs.pdf`; staged S880 = `www.jstage.jst.go.jp/article/ajsls/39/1/39_13/_pdf` vs lane S880 = `sanders.phonologist.org/papers/anderson-etal-cjl-sotl.pdf` (full table: `D/out/baseline2-benignity.txt`). This is the R69-M13 class the round-69 note recorded ("the lane's own settlement row and the package's first staged row share an id").
- The lane registry contains **0 occurrences** of `litmemo|tuduku|chinawriter`, and the guard's real-registry run sees **no theme id** S883/S884/S899/S900 (0 in reg-ids, 0 in collisions) — the four theme staged ids are simply foreign-namespace ids that happen to be numerically free above S880.
- Therefore `collisions == empty` is unattainable for lane+package (it is already 22 at base and stays 22 after a correct by-document adoption) and is **not** the acceptance. The acceptance is the by-document map (staged S883→lane S881, S884→S882, S899→S883, S900→S884; staged S882 not appended because its document already holds lane S877). The guard's role is narrower: m1/m2/m4 prove it **does** fire the moment a theme row is appended as-is (any indent, even none), so "collisions grows by exactly the as-is-appended ids" is the observable the wave should assert.

## Guard weaknesses found (coverage findings, not contract changes)

1. **Raw-pair fragility (biggest footgun).** `comm` on the un-normalized `grep -oE` lines misses every plant whose leading whitespace/spacing differs from the staged side: m1, m2 and m4 all stay at 22 under the raw variant while the canonical pair shows 23. The canonical pair must keep the second `grep -oE 'S[0-9]+'` normalization; a re-implementation that `comm`s raw pattern output silently loses indented and no-space collisions.
2. **The guard is an intersection, not a duplicate-id check.** It is structurally blind to intra-registry duplicates and to registry-side ids absent from staged (m7). Coverage for that class lives in the census (in-file E03 — proven live by m7b's mirror `E03 S1005 duplicate id`) — so item 10's gate must keep running BOTH the guard pair and the mirror census; neither substitutes for the other.
3. **Single-file scope.** For every registry-side plant, `validate --file` on the registry copy alone stayed exit 0 / 0 E — the census cannot see a cross-file collision by construction. The m7b E03 fired only in the merged mirror.
4. **Case.** Lowercase ids are invisible to the guard (m6); the append gate still holds only because census E02 flags them (exit 1).
5. **Tab and 4+ space rows drop out of BOTH detectors silently** (m5, m3): rows counts and reg-ids both under-count, with no error anywhere. Per the 0–3-space contract this is "not a row", but the failure mode is silent under-counting; the census docstring's "4 or more spaces" also omits tabs.
6. **E01 precedence swallows E03.** A malformed twin never reaches the E03 branch (census `next`es E01 rows): staged S883 as-is yields E01 `fields=12` + E11, so even the merged mirror shows no E03 for it, and only 8/132 staged rows are 11-cell (mirror baseline E01×125, E11×148, E03×0). As-is appends are still blocked (exit 1), but "E03 fired" must never be used as evidence the duplicate check exercised these rows.

## Unrun / limits

- I did not test mutants against the lane census in `--root kotodama` mode (fixture uses the equivalent `--file`+symlink shape; the lane's own run was re-verified exit 0 once, read-only).
- I did not verify whether the lane's S859..S880 documents also exist in the package under *other* staged ids (URL-level join across all 132 staged rows) — out of my item; the wave's by-document mapper owns that join.
- No fetches were made; no Wayback probes (no 'no capture' ruling in this item).

Artifacts: `/tmp/MutRegistryCollision-3/` — `detect.sh`, `fix.MDmCXR/out/{baseline,baseline2,m1..m7,m7b,restored}.{reg-ids,collisions,collisions-raw,census.out,census.rc,mirror-census.out,mirror-census.rc,hashes,summary.txt}`, `fix.MDmCXR/out/hashes-pristine.txt`, `hashes-restored.txt`, `baseline2-benignity.txt`, `fixture-path.txt`.
