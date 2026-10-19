# C05 — Cartography freshness re-verification (round 47, claim C)

- seat: C05
- role: verifier, claim C (`reports/round-47/targets.json:25`)
- out: `reports/round-47/cov/C05-freshness.md` (the only path this seat wrote)
- observed: 2026-10-19T17:52:45Z
- repo HEAD: `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe` (`6e9a30d`)
- verdict: **PASS at this HEAD** — cartography is unowned by filename, topic line, heading and couples reference; the proposed slug is unused; a landing at the proposed path is an addition (`A`), not a modification (`M`). The verdict is pinned to `6e9a30d` and must be re-run at the integrator's apply-time HEAD (§8).

Scope: this seat re-verifies freshness only. Boundary adjudication is C08, contract audit C07, source audit C06/C12, README edit C09, post-landing check V01. No corpus byte was written or staged by this seat.

## 1. Contract being verified

Claim C's asserted `before` is:

> `total 223; cartography is a verified-fresh unowned gap (K02-r44: no owner, no prior proposal, not carried)`
> — `reports/round-47/claims.json:27`

Its baseline is `6e9a30d` (`reports/round-47/claims.json:7`), declared at `2026-10-19T17:46:52Z` (`:6`). The landing target is `corpus/knowledge/culture-material/cartography-and-mapmaking.md`, recommended at `reports/round-44/scout/K02-gap-scout.md:8` and `:213-224` (partition `culture-material/`, count 25 → 26, total 223 → 224).

## 2. Baseline integrity at observation time

```console
$ git rev-parse HEAD
6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe

$ git log -1 --format='%cI'
2026-10-19T14:46:42-03:00        # = 17:46:42Z, 10 s before declared_at_utc

$ git status --porcelain -- corpus/
(empty)

$ git diff --stat 6e9a30d..HEAD -- corpus/
(empty)
```

- `baseline_commit` == HEAD, so there is no baseline drift between declaration and this observation.
- The only worktree dirt at observation time was outside `corpus/`: `reports/round-46/review/` and `reports/round-47/` (untracked).
- Live total: `find corpus/knowledge -name '*.md' | wc -l` → **223**; culture-material → **25**.

## 3. Filename ownership — zero cartography owners

```console
$ for p in cartograph mapmak portolan cadastr atlas itinerar survey topograph; do
    printf '%-12s %s\n' "$p" "$(find corpus/knowledge -type f -iname "*$p*" | wc -l)"; done
cartograph   0
mapmak       0
portolan     0
cadastr      0
atlas        0
itinerar     0
survey       0
topograph    1

$ find corpus/knowledge -type f -iname '*map*'
corpus/knowledge/synthesis/dialect-faction-map-workflow.md

$ find corpus/knowledge -type f -iname '*chart*'
corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md
```

The three non-zero hits are not mapmaking owners:

| Path | Why it matches | Ownership reading |
|---|---|---|
| `corpus/knowledge/synthesis/dialect-faction-map-workflow.md:1-2` | `map` as a verb — "Map dialect features … onto travel networks" | isogloss/faction workflow, not the survey→sheet chain |
| `corpus/knowledge/myth-symbol/sacred-topography-pilgrimage.md` | `topograph` in the filename | owns the sacred place register and route, not map production (`:5`, `:96`) |
| `corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md` | substring `chart` inside "charter" | charter myth, not a chart |

No basename contains `cartograph`, `mapmaking`, `portolan`, `cadastr`, `atlas`, `itinerar`, or `survey`.

## 4. Topic-line ownership — zero owners, 11 broad hits adjudicated

Narrow sweep for the register's own vocabulary:

```console
$ grep -rniE -- '^- topic:.*(cartograph|mapmak)' corpus/knowledge/
(no output)                 # 0 files
```

Broad case-insensitive sweep (map/chart/survey/itinerary/atlas/topograph/lienzo/portolan/cadastral):

```console
$ grep -rilE -- '^- topic:.*(cartograph|mapmak|portolan|cadastr|atlas|itinerar|survey|topograph|\bmap\b|\bcharts?\b|lienzo)' corpus/knowledge/ | wc -l
11
```

All 11 are metaphor, verb, or a different owned object:

| file:line | token | reading | cartography owner? |
|---|---|---|---|
| `civilizations/africa-primary-sources.md:2` | map | "a bounded source map" | no — source inventory metaphor |
| `civilizations/finnic-sami.md:3` | map | "gákti as an identity map" | no — dress metaphor |
| `civilizations/mesoamerica-primary-sources.md:3` | map | "a reference map for the four Mesoamerican bases" | no — reference-inventory metaphor; see §5 |
| `culture-material/ritual-garments.md:3` | map | "the b.Arakhin 16a atonement map" | no — ritual metaphor |
| `linguistics/dialect-register-consistency.md:3` | map | "a built dialect map's internal consistency" | no — isogloss metaphor |
| `linguistics/sacred-registers-liturgical-language.md:3` | map | "ritual events map to the competences" | no — verb |
| `linguistics/sound-symbolism.md:3` | map | "the three-way map (arbitrariness / iconicity / systematicity)" | no — analytic metaphor |
| `myth-symbol/number-symbolism.md:3` | survey | "a variance survey of 3, 4, 5, 7, 8, 9, 12, 13, 40, and 108" | no — generic survey, not land survey |
| `myth-symbol/purity-pollution-boundary-systems.md:4` | map | "purity is … a boundary map" | no — metaphor |
| `myth-symbol/sacred-topography-pilgrimage.md:5` | itinerar | "the fixed itinerary vs the votive ramble" | **adjacent, not owner** — owns the place register/route, not the survey→sheet chain; boundary is C08 |
| `synthesis/dialect-faction-map-workflow.md:2` | Map | "Map dialect features and situational registers onto travel networks" | no — verb |

Heading-level ownership is also zero for the register's own vocabulary:

```console
$ grep -rniE '^#{1,4} .*(cartograph|mapmak|portolan|cadastr|lienzo)' corpus/knowledge/ | wc -l
0
```

The nearest heading is `myth-symbol/sacred-topography-pilgrimage.md:96` — "Sacred geography as a diagram — and the era drift of a holy map". It owns the sacred-geography diagram and its drift, not survey, projection, reproduction or the sheet. That is an adjacency for C08, not a second owner of cartography.

No `- couples:` line references a cartography/mapmaking path:

```console
$ grep -rnE -- '^- couples:.*(cartograph|mapmak|portolan|cadastr|lienzo)' corpus/knowledge/ | wc -l
0
```

No row in `corpus/README.md` names the topic (`grep -niE 'cartograph|mapmaking' corpus/README.md` → no output), and `corpus/lessons/` contains zero cartography/mapmaking proposals (`grep -rilE 'cartograph|mapmak' corpus/lessons/ | wc -l` → 0).

## 5. The two body mentions are by-products, one explicitly disclaiming ownership

```console
$ grep -rilE 'cartograph|mapmak' corpus/knowledge/ | wc -l
2
```

1. `corpus/knowledge/myth-symbol/cosmology-cosmography.md:71`

   > "…T-O diagrams are symbolic, not survey maps (§10)…"

   and `:102`:

   > "…T-O diagrams are symbolic devices, not cartographic claims."

   This is the strongest positive evidence for zero ownership: the nearest neighbour names the survey-map register and explicitly says its own cosmography entry does not own it. It is a disclaimer, not a claim.

2. `corpus/knowledge/civilizations/mesoamerica-primary-sources.md:58` — a table row listing "Lienzos and cartographic histories (Quauhquechollan, Tlaxcala, Coixtlahuaca)" as a manuscript/source class with custody cautions. It is a provenance inventory row for Mesoamerican sources, not a method entry for making or reading maps.

No other file in `corpus/knowledge/` mentions either term.

## 6. "Not carried" — prior-round proposal history

```console
$ grep -rilE 'cartograph|mapmak' reports/round-{1..43} reports/round-45 reports/round-46 2>/dev/null | wc -l
0
```

- Rounds 1–43 and 45–46 contain **zero** cartography/mapmaking files. The only prior-round mentions are inside round 44's own seed/audit chain (`reports/round-44/scout/K02-gap-scout.md`, `cov/C05-collision.md`, `cov/C06-scribe.md`, `adj/A01-scope.md`, `review/R01/R02`, `scribe/S01`) plus r47's contract files.
- r44 did **not** land cartography and did **not** draft an entry body for it:
  - `reports/round-44/validation.json:9`: "the fresh gap (cartography, K02) has no entry body."
  - `reports/round-44/cov/C05-collision.md:295`: "A: `corpus/knowledge/culture-material/cartography-and-mapmaking.md` — PASS with the §3.2 boundary table; **no entry draft yet**."
  - r44's claim C was blocked on the *dream* candidate (`reports/round-44/validation.json:9`; `reports/round-44/claims.json:40`), which was carried from `reports/round-42/scout/K02-myth-gaps.md:216`.
- The only file matching the slug anywhere outside `corpus/` is a 100-byte dry-run placeholder, `.scratch/c05/dry3/after/knowledge/culture-material/cartography-and-mapmaking.md:1` ("DRY RUN PLACEHOLDER — not the entry", mtime 2026-10-19 14:28), created by r44's collision/sweep test (`reports/round-44/cov/C05-collision.md:181`). It is not an entry and is not in the corpus tree.
- `LOG.md:3864` and `SCORECARD.md:864` both record r44 C as BLOCKED/unchanged at 223, with the cartography seed having no entry body.

**Interpretation note (flagged, not a failure).** The only prior-round naming of cartography is the authorizing r44 K02 seed itself (`K02-gap-scout.md:8`, `:207`: "fresh at HEAD c9f4eaa and is not carried from any prior round"). Read literally as "no naming in any prior round", that would make every r44-seeded topic carried and the r47 claim unsatisfiable. The operative distinction in r44's own filed record is a *drafted candidate* (dream, with a colliding slug named at r42) versus a *seed-only gap with no entry body* (cartography). On that distinction — and on r44's explicit "no entry draft yet" — cartography satisfies the claim's `before`. Reviewers R02/X04 should confirm this reading; it is the one residual interpretive risk I found, and it is named rather than hidden.

## 7. Slug uniqueness and `A` vs `M`

Presence checks at HEAD:

```console
$ test -e corpus/knowledge/culture-material/cartography-and-mapmaking.md && echo EXISTS || echo ABSENT
ABSENT

$ git ls-files --error-unmatch corpus/knowledge/culture-material/cartography-and-mapmaking.md
error: pathspec '…/cartography-and-mapmaking.md' did not match any file(s) known to git

$ git cat-file -e 6e9a30d:corpus/knowledge/culture-material/cartography-and-mapmaking.md
fatal: path '…/cartography-and-mapmaking.md' does not exist in '6e9a30d'
exit=128

$ git check-ignore -v corpus/knowledge/culture-material/cartography-and-mapmaking.md
(no output — NOT_IGNORED)

$ git status --porcelain -- corpus/knowledge/culture-material/cartography-and-mapmaking.md
(empty)
```

The path is absent from the worktree, the index and the HEAD tree; there is no deletion or modification to report. Therefore `git add` at this path can only produce an addition.

Direct confirmation in a throwaway shared clone at the same commit (probe file synthetic, clone removed after the test; no corpus write):

```console
$ git clone --shared --no-hardlinks -q . .scratch/c05-landcheck/repo
$ cd .scratch/c05-landcheck/repo && git checkout -q 6e9a30d
$ printf '# PROBE ONLY\n' > corpus/knowledge/culture-material/cartography-and-mapmaking.md
$ git add corpus/knowledge/culture-material/cartography-and-mapmaking.md
$ git status --porcelain -- corpus/knowledge/culture-material/cartography-and-mapmaking.md
A  corpus/knowledge/culture-material/cartography-and-mapmaking.md

$ git diff --cached --name-status -- corpus/knowledge/culture-material/cartography-and-mapmaking.md
A	corpus/knowledge/culture-material/cartography-and-mapmaking.md
```

Slug/sort checks:

- Exact basename `cartography-and-mapmaking` is absent from the 223-entry set; nearest `difflib` ratio is 0.53 to `sacred-topography-pilgrimage` (different subject), no high-similarity duplicate.
- Sort position with `LC_ALL=C sort`:

```text
5-calendar-festival-systems.md
6:cartography-and-mapmaking.md
7-costume-semiotics.md
```

- The addition would sit between the current positions 5 and 6 in `corpus/knowledge/culture-material/`, matching `reports/round-44/scout/K02-gap-scout.md:220` and the README row placement between `:240` and `:241`.

## 8. Partition listing and README state at this HEAD

Live partition census:

| partition | files |
|---|---:|
| civilizations | 94 |
| culture-material | 25 |
| linguistics | 25 |
| myth-symbol | 26 |
| synthesis | 29 |
| verification | 24 |
| **total** | **223** |

`corpus/knowledge/culture-material/` (25, numbered in C-sort order):

```text
 1 adornment-body-codes.md
 2 agrarian-field-system-lexicon.md
 3 architecture-settlement-lexicon.md
 4 bathing-and-body-hygiene.md
 5 calendar-festival-systems.md
 6 costume-semiotics.md
 7 craft-artisan-lexicon.md
 8 cuisine-food-lexicon.md
 9 dress-through-eras.md
10 era-periodization-models.md
11 fire-fuel-light.md
12 funerary-material-culture.md
13 furniture-interior-lexicon.md
14 garment-lexicon-crosslinguistic.md
15 material-culture-inference-method.md
16 music-instrument-lexicon.md
17 ritual-garments.md
18 sumptuary-law-rank-display.md
19 textile-technology.md
20 timekeeping-instruments.md
21 trade-economy-lexicon.md
22 transport-mobility-lexicon.md
23 vessel-container-lexicon.md
24 warrior-material-culture.md
25 writing-media-surface-economy.md
```

Read-only README sweep at this HEAD:

```console
$ python3 -B reports/round-28/readme/sweep.py
parts {"civilizations": 94, "culture-material": 25, "linguistics": 25, "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 223 files 223
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 223 totals_ok True
footer {"date": "2026-10-19", "command": "python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge", "total": 223, "dir_totals": [25, 26, 25, 29, 24, 94]}
footer_live {"total": 223, "dir_totals": [25, 26, 25, 29, 24, 94], "order": ["linguistics", "myth-symbol", "culture-material", "synthesis", "verification", "civilizations"]}
footer_findings [] footer_ok True
readme_sha256 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
rc=0
```

The live README footer (`corpus/README.md:548`: "total 223 files; directory totals 25/26/25/29/24/94") already matches the partition. The rev-2.4 **prose** vector is the defective one: `corpus/README.md:10-11` says the vector moved `25/23/25/29/24/94 → 25/23/26/25/24/94`, which sums 220 → **217**, not 223. The measured vector is `25/26/25/29/24/94` (sum 223); post-landing it must be `26/26/25/29/24/94` (sum 224). This is C09's repair, not this seat's, but it matters to claim C's "sweep-green AND prose vector corrected" threshold: **the sweep does not read the revision prose block**, so a green sweep alone does not prove the vector repair.

Expected README anchors for the landing (verified live): section header `corpus/README.md:234` (`## culture-material/ (25)`), row insertion between `:240` (`calendar-festival-systems.md`) and `:241` (`costume-semiotics.md`), totals line `:544` (223), footer `:548` (vector). Post-landing: 224 rows/files; culture-material 26; vector `26/26/25/29/24/94`.

Incidental observation, outside this seat's claim: `corpus/README.md:1` and `:3` are duplicate H1 lines. Not a freshness finding and not assessed here; flagged for the README editor (C09) to decide.

## 9. Landing-time re-run contract

This verdict is valid at `6e9a30d` only. Before the integrator applies the entry, and again in V01's post-landing check, run:

```bash
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
git rev-parse --short HEAD                              # must be recorded
find corpus/knowledge -name '*.md' | wc -l              # must be 223 pre-landing
ls corpus/knowledge/culture-material/*.md | wc -l       # must be 25 pre-landing
grep -rilE 'cartograph|mapmak' corpus/knowledge/ | wc -l # expected 2 (by-products)
test -e corpus/knowledge/culture-material/cartography-and-mapmaking.md \
  && echo COLLISION || echo ABSENT                       # must be ABSENT pre-landing
git cat-file -e HEAD:corpus/knowledge/culture-material/cartography-and-mapmaking.md; echo "rc=$?"  # expect 128 pre-landing
python3 -B reports/round-28/readme/sweep.py             # pre: 223==223; post: 224==224
```

Stop conditions: `COLLISION`, pre-landing total ≠ 223, culture-material ≠ 25, a new topic-line owner, or a benchmark HEAD different from the recorded apply-time HEAD without recording the new sha and re-running the ownership sweep. Post-landing, the expected delta is exactly one added file at the target path, culture-material 26, total 224, sweep `rows 224 files 224`, footer `26/26/25/29/24/94`; no other corpus file changes.

## 10. Evidence provenance and limits

- All commands above were read-only against the repo; no `reports/round-*/run-validation.py` was executed in-tree; no commit, push, install or network access occurred.
- The only path this seat wrote is `reports/round-47/cov/C05-freshness.md`. The temporary clone `.scratch/c05-landcheck/` was removed after the `A` test. The pre-existing `.scratch/c05/dry3/` placeholder is r44's and was not modified.
- No filed byte under `reports/round-1..46/**`, `corpus/lessons/*.md`, `tools/gates/frozen/**` or `.ufo/**` was touched.
- Not assessed here: whether the eventual entry's content is a real method entry (R03/C07), whether its boundary table correctly dispositions cosmography/sacred topography/divination/direction (C08/A02), whether its sources are honestly `to-verify` (C06/C12), and whether its `- couples:` tokens resolve (C13). Those are separate seats; this report only establishes that the path was free and the premise true at `6e9a30d`.
