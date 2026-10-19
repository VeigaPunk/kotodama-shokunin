# C06 — freshness + collision verification (claim C, cartography)

- Seat: `C06` | role: verifier | claim: **C** (coverage) | round 48, loop 2, position 2
- Baseline measured: HEAD `a01405dd36367292255c2652ac0a601f4cd6a0af` (short `a01405d`), equal to
  `reports/round-48/claims.json:7` (`"baseline_commit": "a01405d"`).
- Out path: `reports/round-48/cov/C06-collision.md` (this file).
- Mission: cartography still 0 owners at landing HEAD; the slug is free; lands as **A** not **M**; no
  second owner of any register (boundary vs divination / cosmology-cosmography / direction-symbolism).
- Non-author statement: I drafted no entry, header, README or queue fragment. At my read time
  `reports/round-48/cov/` did not exist (`ls -la reports/round-48/` → only `claims.json`,
  `targets.json`, `telemetry/`), so this is a **pre-draft** verification of the landing slot plus a
  boundary matrix the assembled bytes must satisfy. The boundary sentences in §5 are a draft spec,
  not a review of bytes I did not see; each is `to-verify` against the assembled entry.

**One-line verdict. CLAIM C's freshness and collision legs PASS at the declared baseline.** The
cartography slot is genuinely unowned (0 filename owners, 0 topic-line owners, 2 body lines in 2
files, both disclaimers/metadata), the slug is untracked, not ignored, and has no case or directory
variant, and the index has no row for it. The entry lands as **A**; the only expected **M** in
`corpus/` is `corpus/README.md`. One finding is new against r47's B1–B9 and P2-7: the nearest
competing owner of the word "map" is not cosmology but **`sacred-topography-pilgrimage.md:96-100`
(§7, "Sacred geography as a diagram — and the era drift of a holy map")**, which r47's boundary table
cited only at `:5`/`:69`. Two more adjacent owners (`timekeeping-instruments.md` for the astrolabe
instrument class, `cosmology-cosmography.md:133` for the map's semantic content) are also
undispositioned. None of them owns the survey→projection→reproduction chain, so the register remains
single-owner — but the assembled boundary table must say so explicitly, row by row.

---

## 1. Live state measured (not carried)

All commands from the lane root, 2026-10-19, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

```
$ git rev-parse HEAD
a01405dd36367292255c2652ac0a601f4cd6a0af
$ git status --porcelain
?? reports/round-46/review/
?? reports/round-48/
$ find corpus/knowledge -name '*.md' | wc -l
223
$ for d in corpus/knowledge/*/; do printf '%s %s\n' "$(ls $d*.md | wc -l)" "$d"; done
94 corpus/knowledge/civilizations/
25 corpus/knowledge/culture-material/
25 corpus/knowledge/linguistics/
26 corpus/knowledge/myth-symbol/
29 corpus/knowledge/synthesis/
24 corpus/knowledge/verification/
```

The index instrument, read-only against the live tree (its only writes are planted-control
temp trees via `tempfile.mkdtemp()`, i.e. under `TMPDIR=$PWD/.scratch`,
`reports/round-28/readme/sweep.py:252-260,393-399`):

```
$ python3 -B reports/round-28/readme/sweep.py
parts {"civilizations": 94, "culture-material": 25, "linguistics": 25, "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 223 files 223
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 223 totals_ok True
footer {"date": "2026-10-19", ..., "total": 223, "dir_totals": [25, 26, 25, 29, 24, 94]}
footer_live {"total": 223, "dir_totals": [25, 26, 25, 29, 24, 94], "order": ["linguistics", "myth-symbol", "culture-material", "synthesis", "verification", "civilizations"]}
footer_findings [] footer_ok True
readme_sha256 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
exit=0
```

Partition length band (the right-sizing context this seat only uses to check that a landing is
sliceable, not to judge content):

```
$ wc -l corpus/knowledge/culture-material/*.md | sort -n
min 103 (textile-technology.md) / max 221 (funerary-material-culture.md) / median 149 / mean 150.24
```

No cartography file exists in the tree and no seat has staged one: `git status --porcelain` shows no
`corpus/**` entry at all.

---

## 2. Ownership test — three legs, zero owners

### 2.1 Filename leg — 0 owners

```
$ find corpus \( -iname '*cartograph*' -o -iname '*mapmaking*' -o -iname '*portolan*' \
      -o -iname '*cadastr*' -o -iname '*atlas*' -o -iname '*graticule*' \) | wc -l
0
$ find corpus -type d -iname '*carto*' -o -type d -iname '*map*'
(no output)
```

The only basename that brushes the vocabulary is `synthesis/dialect-faction-map-workflow.md`, and its
`- topic:` (`:2`) is "**Map** dialect features and situational registers onto travel networks…" — the
verb, not the artifact.

### 2.2 Topic-line leg — 10 hits, all dispositioned as non-owners

Command and count:

```
$ grep -rniE '^- *topic:.*(cartograph|mapmak|portolan|cadastr|atlas|itinerar|survey map|world map|graticule|theodolite|topograph|\bmap\b|\bcharts?\b)' corpus/knowledge/ | wc -l
10
```

| Hit | The matching phrase in its `- topic:` line | Class | Owner? |
|---|---|---|---|
| `linguistics/sound-symbolism.md:3` | "the three-way map (arbitrariness / iconicity / systematicity)" | metaphor | no |
| `linguistics/dialect-register-consistency.md:3` | "a built dialect map's internal consistency" | metaphor (model) | no |
| `linguistics/sacred-registers-liturgical-language.md:3` | "ritual events map to the competences they require" | verb | no |
| `myth-symbol/purity-pollution-boundary-systems.md:4` | "purity is not a substance but a boundary map" | metaphor | no |
| `myth-symbol/sacred-topography-pilgrimage.md:5` | "sacred-geography mapping (a culture's holy sites as a diagram…)" | **adjacent owner — place register** | no (see §4) |
| `culture-material/ritual-garments.md:3` | "the b. Arakhin 16a atonement map" | metaphor (ritual) | no |
| `synthesis/dialect-faction-map-workflow.md:2` | "**Map** dialect features…" | verb | no |
| `civilizations/finnic-sami.md:3` | "gákti as an identity map" | metaphor | no |
| `civilizations/mesoamerica-primary-sources.md:3` | "a reference map for the four Mesoamerican bases" | metaphor | no |
| `civilizations/africa-primary-sources.md:2` | "a bounded source map" | metaphor | no |

Zero topic-line owners. `sacred-topography-pilgrimage.md` is a **place-register** owner (holy-site
typology, route-as-rite, diagram geometry), not a production owner; §4 gives the ruling.

### 2.3 Body leg — 2 lines in 2 files, every one a disclaimer or a metadata citation

```
$ grep -rni 'cartograph' corpus/knowledge/
corpus/knowledge/myth-symbol/cosmology-cosmography.md:102: … T-O diagrams are symbolic devices, not cartographic claims …
corpus/knowledge/civilizations/mesoamerica-primary-sources.md:58: | Lienzos and cartographic histories … |
$ grep -rni 'cartograph' corpus/knowledge/ | wc -l
2
$ grep -rli 'cartograph' corpus/knowledge/ | wc -l
2
$ for t in mapmaking portolan graticule theodolite cadastr; do
    printf '%s files=%s lines=%s\n' "$t" "$(grep -rli "$t" corpus/knowledge/ | wc -l)" "$(grep -rni "$t" corpus/knowledge/ | wc -l)"; done
mapmaking files=0 lines=0
portolan files=0 lines=0
graticule files=0 lines=0
theodolite files=0 lines=0
cadastr files=2 lines=2
```

This reproduces r47 R03's B2 correction: **2 files / 2 lines**, not "2 files / 3 lines". The `:71`
line ("T-O diagrams are symbolic, not survey maps") contains no `cartograph` token and must not be
counted as one. The `cadastr` 2 hits are `architecture-settlement-lexicon.md:95` ("The grid is
cadastral") and `cosmology-cosmography.md`'s T-O row (Mappa Mundi), both disclaimers/false positives.

**Ownership verdict: 0 filename owners, 0 topic-line owners, 0 body owners.** The gap is real at the
declared baseline.

---

## 3. Slug and landing slot — free, A not M

### 3.1 The slug is free in every variant that could turn an A into an M

```
$ test -e corpus/knowledge/culture-material/cartography-and-mapmaking.md && echo COLLISION || echo FREE
FREE
$ test -e corpus/knowledge/culture-material/cartography.md && echo COLLISION || echo FREE
FREE
$ git ls-files corpus | grep -iE 'carto|mapmak|portolan|cadastr'
(no output; exit 1)
$ git check-ignore -q corpus/knowledge/culture-material/cartography-and-mapmaking.md && echo IGNORED || echo NOT-IGNORED
NOT-IGNORED
$ grep -c 'cartography-and-mapmaking' corpus/README.md
0
```

So: not on disk, not tracked, not ignored (an ignored path could silently vanish from `git status`),
no case variant (`find -iname` covers case-insensitive collision), no directory of that name, and no
index row. **Landing is an A on a new path.**

### 3.2 The index insertion point is unambiguous

`corpus/README.md` culture-material rows run in filename order, lines 236–260:

```
236  - `adornment-body-codes.md`
...
240  - `calendar-festival-systems.md`
241  - `costume-semiotics.md`
...
260  - `writing-media-surface-economy.md`
```

Filename order puts `cartography-and-mapmaking.md` **between `calendar-festival-systems.md` (:240)
and `costume-semiotics.md` (:241)** ("cal" < "car" < "cos"). The section header
`## culture-material/ (25)` is at `:234` and must move to `(26)`; the sweep checks that number
(`reports/round-28/readme/sweep.py:125-152`, `header_drift`). The footer counts line is
`corpus/README.md:548`: `(total 223 files; directory totals 25/26/25/29/24/94)`.

### 3.3 README landing precondition I verified (C10's edit, C06's collision concern)

The rev-2.4 prose vector is wrong and must be repaired in the same edit, else the rev-2.5 row
addition is arithmetically incoherent:

- `corpus/README.md:4-10` states the post-r42 vector as `25/23/26/25/24/94` → sums **217**.
- Live partition is `25/26/25/29/24/94` → sums **223**.
- Correct rev-2.5 vector is `25/26/26/29/24/94` → sums **224**.

The rev-2.4 line bumped myth-symbol and culture-material but left synthesis at 25 (live 29); three
slots are wrong, not one. This is C10/Ca's edit, recorded here only because the row collision test
(no existing row, one new row) runs against the same bytes.

---

## 4. Second-owner matrix — 14 neighbors, zero second owners, five under-dispositioned rows

The register claim under test: cartography owns the **survey → control → reduce → project →
symbolize → reproduce** chain and the sheet as a produced, warranted object. It does **not** own the
world model, the place register, the orientation register, the sign-reading technology, the
instrument families that measure time, the measure system, or the workshop.

| Neighbour | What it owns (live anchor I re-read) | What cartography may claim | Ruling |
|---|---|---|---|
| `myth-symbol/cosmology-cosmography.md` | world model / cosmogram; **"how the world is drawn (maps)"** (`:27`); toponyms as cosmographic claims, **"a fictional map is a set of etymological arguments"** (`:133`); T-O diagrams "symbolic, not survey maps" (`:71`), "not cartographic claims" (`:102`) | the surveyed, projected, reproduced sheet **as production**; no world-model content, no toponym derivation | adjacent; **cite `:27` and `:133`**, not only `:71`/`:102` (r47 B8 covers `:27`; `:133` is new) |
| `myth-symbol/sacred-topography-pilgrimage.md` | place register; **§7 "Sacred geography as a diagram — and the era drift of a holy map"** at `:96-100`; "The map is a claim" (`:98`); "the map's geometry is a claim about the world" (`:57`) | the sheet on which a site is located; no site typology, route-as-rite, diagram geometry, or drift mechanisms | adjacent; **cite `:96-100`**, not only `:5`/`:69` — **new, not in r47 B1–B9** |
| `myth-symbol/direction-symbolism.md` | direction register; **compass trap** (`:51`); relative-frame uses incl. "maps" (`:48`) | the map's orientation convention as a production decision (which north; declination handling) | adjacent; pointer to `:51`, never a re-derivation |
| `myth-symbol/divination-omen-systems.md` | sign-reading technology (`:3`); geomancy origin question (`:28`, `:175`, `:189`) | nothing divinatory; siting/geomancy is not this entry's | **NOT a collision**; add the one-line negative row so the check is visible |
| `myth-symbol/celestial-symbolism-calendars.md` | sidereal compass and star navigation (`:14`, `:84`) | the star chart as a produced sheet | adjacent; row missing in r47 (P2-7) |
| `myth-symbol/sacred-kingship-mythic-charter.md` | mythic charter / legitimation channels (`:3`) | the map as a legal-territorial instrument only; no charter theory | adjacent; row missing in r47 (P2-7) |
| `culture-material/architecture-settlement-lexicon.md` | settlement form; castrum grid "surveyed with the **groma**… The grid is cadastral" (`:95`); instrument + founding rite + claim word (`:101`) | land survey as a map-production step; the cadastral map as a form | adjacent; architecture owns the founding plan, not the sheet |
| `culture-material/timekeeping-instruments.md` | the five time-measuring instrument families incl. **the astrolabe** (`:3`, `:24`, `:27`) | distance/angle chains (chain, plane table, theodolite) as survey instruments; do **not** re-own the astrolabe/nocturnal family | adjacent; **new row — not in r47 at all** |
| `culture-material/trade-economy-lexicon.md` | measures and metrology (`:3`) | the map scale as a representation ratio, not a unit system | adjacent; row missing in r47 (P2-7) |
| `culture-material/craft-artisan-lexicon.md` | workshop as speech community and its apprentice→master ladder (`:3`, `:54-65`) | the mapmaker trade roles and products | adjacent; row missing in r47 (P2-7); ladder anchor is `:54-65`, **not** `:44` (r47 B4) |
| `culture-material/transport-mobility-lexicon.md` | route institution; "a route is only real if someone maintains it" (`:28`); DR-TR-02 (`:117`) | the representation of a route | adjacent |
| `culture-material/writing-media-surface-economy.md` | surface economy and reproduction cost (`:3`) | map-specific media and reproduction | adjacent |
| `linguistics/naming-systems.md` | toponymy; "a map is an archive of **coups**" (`:70`) | the toponym layer on the sheet | adjacent; quote exactly "coups" — do not apply r47 B3's false correction |
| `civilizations/mesoamerica-primary-sources.md` | the lienzo / cartographic-history source class (`:58`) | cites the genre as an exemplar | adjacent |

**No second owner.** Every neighbour above owns a *content* register (world model, place, direction,
signs, time, measures, workshop, route, surface, names) or an *instrument family* (timekeeping); none
owns the measured-and-reproduced sheet. The three explicitly named in my mission resolve as:
divination = not a collision (nothing divinatory may be claimed), cosmology-cosmography = adjacent
content owner (`:27`, `:133`), direction-symbolism = adjacent convention owner (`:51`).

**Under-dispositioned in r47:** `sacred-topography-pilgrimage.md:96-100`, `cosmology-cosmography.md:133`,
`timekeeping-instruments.md`, plus the four P2-7 rows (craft, trade, celestial, sacred-kingship).
Two of these are *new* relative to R03's B1–B9.

---

## 5. Boundary sentences the assembled entry must carry (draft spec, `to-verify` on bytes)

Minimal additions; place them in the existing boundary table and §1 gap sentence. They are written
to be dropped in as rows, not re-derived prose.

```markdown
| Neighbour | What it owns (live anchor) | What the cartography entry may claim | Ruling |
|---|---|---|---|
| `myth-symbol/cosmology-cosmography.md` | world model and cosmogram: "how the world is drawn (maps)" (`:27`); "a fictional map is a set of etymological arguments" (`:133`); T-O diagrams "symbolic, not survey maps" (`:71`, `:102`) | the surveyed, projected, reproduced sheet as production; cites `:27` and `:133` as the content boundary | adjacent, not a second owner |
| `myth-symbol/sacred-topography-pilgrimage.md` | place register and §7's "holy map": sacred geography as a diagram, "The map is a claim" (`:98`), six drift mechanisms (`:96-100`) | the sheet a site is plotted on; does not restate site kinds, route-as-rite, diagram geometry, or drift | adjacent, not a second owner |
| `myth-symbol/direction-symbolism.md` | orientation register and the compass trap (`:51`) | the map convention that resolves it (which north; declination handling), cited as a pointer | adjacent |
| `myth-symbol/divination-omen-systems.md` | sign-reading (`:3`); geomancy origin question (`:28`, `:175`, `:189`) | no divinatory reading, no geomantic siting | no collision; negative row |
| `culture-material/timekeeping-instruments.md` | time-measuring instrument families incl. the astrolabe (`:3`, `:24`, `:27`) | distance/angle survey chains; does not re-own the astrolabe or nocturnal | adjacent; new row |
| `myth-symbol/celestial-symbolism-calendars.md` | sidereal compass and star navigation (`:14`, `:84`) | the star chart as a produced sheet | adjacent |
| `culture-material/trade-economy-lexicon.md` | measures and metrology (`:3`) | the map scale as a representation ratio | adjacent |
| `culture-material/craft-artisan-lexicon.md` | workshop register and apprentice→master ladder (`:3`, `:54-65`) | the mapmaker trade roles and products | adjacent |
| `myth-symbol/sacred-kingship-mythic-charter.md` | mythic charter / legitimation (`:3`) | the map as a legal-territorial instrument only | adjacent |
```

And the `- gap filled:` count must be the measured one, not r47's unreproducible figure:

> 2 body lines in 2 files mention `cartograph` (`cosmology-cosmography.md:102` as a disclaimer,
> `mesoamerica-primary-sources.md:58` as a source-class row); `mapmaking`/`portolan`/`graticule`/
> `theodolite` = 0; 0 filename owners and 0 `- topic:` owners. A named-but-unbuilt register, not a
> high-demand omission.

---

## 6. Pre-landing re-check (the "gap re-verified unowned at landing" leg)

The integrator must run this at apply time and paste the output into the landing record. Expected
values are the ones I measured at `a01405d`; any drift means re-open the check, not carry this file.

```bash
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
git rev-parse --short HEAD                                   # expect a01405d (or record the new HEAD)
find corpus/knowledge -name '*.md' | wc -l                   # expect 223
ls corpus/knowledge/culture-material/*.md | wc -l            # expect 25
test -e corpus/knowledge/culture-material/cartography-and-mapmaking.md \
  && echo COLLISION || echo FREE                             # expect FREE
find corpus \( -iname '*cartograph*' -o -iname '*mapmaking*' -o -iname '*portolan*' \
  -o -iname '*cadastr*' \) | wc -l                           # expect 0
grep -rniE '^- *topic:.*(cartograph|mapmak|portolan|cadastr|survey map|graticule|theodolite)' \
  corpus/knowledge/ | wc -l                                  # expect 0
grep -rni 'cartograph' corpus/knowledge/ | wc -l              # expect 2
grep -rli 'cartograph' corpus/knowledge/ | wc -l              # expect 2
git ls-files --error-unmatch corpus/knowledge/culture-material/cartography-and-mapmaking.md \
  >/dev/null 2>&1 && echo TRACKED || echo UNTRACKED           # expect UNTRACKED
git check-ignore -q corpus/knowledge/culture-material/cartography-and-mapmaking.md \
  && echo IGNORED || echo NOT-IGNORED                         # expect NOT-IGNORED
grep -c 'cartography-and-mapmaking' corpus/README.md          # expect 0
```

A `COLLISION`, `TRACKED`, `IGNORED`, or a nonzero filename/topic count blocks the landing: route it
as a report, do not overwrite and do not rename around it (`targets.json` shared rule 5).

---

## 7. Post-landing assertions (A-not-M and no-second-row)

```bash
# 1. The entry is an addition, and nothing else under corpus/knowledge moves.
git status --porcelain=v1 --untracked-files=all -- corpus/knowledge
# before git add:  exactly  ?? corpus/knowledge/culture-material/cartography-and-mapmaking.md
# after  git add:  exactly  A  corpus/knowledge/culture-material/cartography-and-mapmaking.md
git status --porcelain -- corpus/knowledge | grep -c '^ M'    # expect 0
git diff --stat -- corpus/knowledge                           # expect empty

# 2. Census moved by exactly one, in exactly one partition.
find corpus/knowledge -name '*.md' | wc -l                    # expect 224
ls corpus/knowledge/culture-material/*.md | wc -l             # expect 26

# 3. No duplicate index row (the sweep has this leg even though it lacks a heading control).
python3 -B reports/round-28/readme/sweep.py --json | python3 -c \
  "import json,sys; r=json.load(sys.stdin); \
   print({k:(v['rows'],v['files'],v['duplicate_rows']) for k,v in r['parts'].items()}); \
   print('total',r['totals_line'],'ok',r['totals_ok'])"
# expect culture-material (26, 26, []) ; every part rows==files ; total 224 ok True ; exit 0
```

The only expected **M** in `corpus/` is `corpus/README.md` (row + section header + totals + footer +
vector). If `git status` shows an M on any other corpus entry, the landing violated the no-overwrite
rule and must be reverted before validation.

`git status --porcelain -- corpus` after apply should therefore read exactly two paths:
`M corpus/README.md` and `A corpus/knowledge/culture-material/cartography-and-mapmaking.md`.

---

## 8. Findings ranked, and what I did not verify

| ID | Finding | Severity for claim C |
|---|---|---|
| F1 | Freshness holds: 0 filename owners, 0 topic-line owners, 2 body lines (both disclaimers/metadata). | PASS — no action |
| F2 | `sacred-topography-pilgrimage.md:96-100` (§7 "holy map", "The map is a claim") is the nearest competing owner of the word "map"; r47 cited only `:5`/`:69`. | must fix in the boundary table — **new vs r47 B1–B9** |
| F3 | `cosmology-cosmography.md:133` ("a fictional map is a set of etymological arguments") is a content-ownership sentence distinct from `:27`; r47 B8 fixes only `:27`. | must fix — extends B8 |
| F4 | `timekeeping-instruments.md` owns the astrolabe class (`:3`, `:24`, `:27`); no r47 row exists. | add row — **new vs r47 P2-7** |
| F5 | `- gap filled:` must read 2 files / 2 lines and must not count `:71` as a `cartograph` hit. | enforce — reproduces r47 B2 |
| F6 | README rev-2.4 vector sums 217 (should be 223); rev 2.5 must repair to `25/26/25/29/24/94` then add to `25/26/26/29/24/94`. | landing precondition (C10/Ca) |
| F7 | Divination is **not** a collision; geomancy stays divination's (`:28`, `:175`, `:189`). | negative check passes |
| F8 | Slug is free in all variants; untracked, not ignored; lands as A; no index row. | PASS — no action |

**Not verified (honest limits).** (a) The assembled entry does not exist at my read time, so §5 is a
spec, not a byte review; the `to-verify` marks above must be closed by whoever verifies the assembled
bytes. (b) I did not judge content depth or arithmetic — C03/C05/C12/R03 own those. (c) I did not
re-run the freshness gate (`tools/harness/claims-freshness.py`); O01/O04 own it; my ownership test is
an independent live-tree measurement. (d) The README duplicate H1 at `:1`/`:3` is Ca's defect; I
recorded it only because I read the head block and the heading count is 2, not because claim C
depends on it.

---

## 9. Commands and write-surface statement

Every command above was run from `/home/vgpnk/Projects/shokunin/kotodama-shokunin` on 2026-10-19 with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`. The sweep is the read-only index instrument
(`reports/round-28/readme/sweep.py`); no `reports/round-*/run-validation.py` was executed, no
`declared-in-r7` freeze was touched, no network, no install, no git commit/push.

**Write surface: this file only** — `reports/round-48/cov/C06-collision.md`. No `corpus/**`,
`tools/**`, `README`, `LOG.md`, `reports/round-1..47/**`, `tools/gates/frozen/**`, or fleet `.ufo/**`
byte was edited or staged. No corpus file was created; the fenced boundary block above is a draft for
the integrator, deliberately not staged under `corpus/`.
