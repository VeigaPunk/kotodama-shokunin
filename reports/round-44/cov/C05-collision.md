# C05 — collision verify (claim C): two filed candidates, both collision-free, only one may land

- Seat **C05** | verifier | claim **C** (coverage) | round 44
- Observed at HEAD `c9f4eaa707b6e977ff6e1616463e91f4b8afea5d` (`git rev-parse HEAD`), 2026-10-19T17:28Z.
- Environment: `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.
- Mission (verbatim, `reports/round-44/targets.json`, seat `C05`): *"Collision verifier: independently enumerate the target partition at HEAD, confirm the proposed filename is unused AND the topic is unowned (no second owner), confirm landing changes no other file."*
- **Revision note:** this is the second cut of this seat's report. The first cut (17:25Z) tested only K04's dream candidate because K02 and C01 had not filed. K02 (`17:27:27Z`) and C01 (`17:27:43Z`) have since landed; this revision covers **both exact proposals** and supersedes the first cut's "only filed target" verdict.

## Verdict at a glance

**Both filed candidates are collision-free at the observed baseline. Claim C is `+1`, so exactly one may land; landing both would make 225 and fail the claim.**

| candidate | exact path | filename unused | topic unowned | sorts correctly | draft exists | collision verdict |
|---|---|---|---|---|---|---|
| **A — K02 cartography** | `corpus/knowledge/culture-material/cartography-and-mapmaking.md` | **yes** (no cartography/mapmaking/portolan/cadastral basename anywhere) | **yes** (11 topic-line hits, all metaphor/verb/adjacent; the partition's own cosmography line explicitly disclaims survey maps) | position 6 of culture-material | **no** — seed + outline + shelf in `K02-gap-scout.md` §4 | **PASS with a named boundary table** |
| **B — K04/C01 dream** | `corpus/knowledge/myth-symbol/dream-vision-trance.md` | **yes** (no dream/trance/vision/ecsta/shaman/incubat basename anywhere) | **yes** (2 topic-line hits, both adjacent: one divination technique row and one civilization datum) | position 11 of myth-symbol | **yes** — fenced entry in `C01-entry-draft.md` §4 | **PASS with a named boundary table** |

- The two candidates do **not** collide with each other: different partitions, different slugs, disjoint topic seeds. The collision is a **coordination** constraint (claim C is one entry, `+1`), not a duplicate-topic collision.
- C01's own draft says it is a **spare** if K02 names a different gap (`C01-entry-draft.md:9`), and K02 has now named a different gap. Whichever candidate the integrator does not choose is a spare, not a second landing.
- This seat does **not** choose between them. The collision evidence clears both; the choice and the draft-completeness consequence are stated in §6 and §11.

---

## 1. Live partition enumeration at HEAD (observed, not inferred)

```
$ git rev-parse HEAD
c9f4eaa707b6e977ff6e1616463e91f4b8afea5d

$ find corpus/knowledge -name '*.md' | wc -l
223

$ for d in corpus/knowledge/*/; do printf '%s=%s ' "$(basename $d)" "$(find $d -name '*.md' | wc -l)"; done
civilizations=94 culture-material=25 linguistics=25 myth-symbol=26 synthesis=29 verification=24

$ git status --porcelain
?? reports/round-44/
```

Target partitions at HEAD:

- `corpus/knowledge/myth-symbol/` — 26 files: `animal-symbolism.md`, `binding-speech-complex.md`, `celestial-symbolism-calendars.md`, `color-symbolism.md`, `comparative-frameworks.md`, `cosmology-cosmography.md`, `creation-myths-taxonomy.md`, `death-afterlife-eschatology.md`, `direction-symbolism.md`, `divination-omen-systems.md`, `eschatology-world-end-systems.md`, `flood-traditions.md`, `hero-journey-variants.md`, `mineral-stone-symbolism.md`, `motif-index-usage.md`, `myth-folktale-genres.md`, `myth-ritual-theories.md`, `number-symbolism.md`, `pantheon-archetypes.md`, `plant-symbolism.md`, `purity-pollution-boundary-systems.md`, `ritual-liminality.md`, `sacred-kingship-mythic-charter.md`, `sacred-topography-pilgrimage.md`, `symbolism-synthesis-method.md`, `trickster.md`.
- `corpus/knowledge/culture-material/` — 25 files: `adornment-body-codes.md`, `agrarian-field-system-lexicon.md`, `architecture-settlement-lexicon.md`, `bathing-and-body-hygiene.md`, `calendar-festival-systems.md`, `costume-semiotics.md`, `craft-artisan-lexicon.md`, `cuisine-food-lexicon.md`, `dress-through-eras.md`, `era-periodization-models.md`, `fire-fuel-light.md`, `funerary-material-culture.md`, `furniture-interior-lexicon.md`, `garment-lexicon-crosslinguistic.md`, `material-culture-inference-method.md`, `music-instrument-lexicon.md`, `ritual-garments.md`, `sumptuary-law-rank-display.md`, `textile-technology.md`, `timekeeping-instruments.md`, `trade-economy-lexicon.md`, `transport-mobility-lexicon.md`, `vessel-container-lexicon.md`, `warrior-material-culture.md`, `writing-media-surface-economy.md`.

Integrity readings at the same cut:

| reading | command | result |
|---|---|---|
| total | `find corpus/knowledge -name '*.md' \| wc -l` | **223** |
| naming convention | `find corpus/knowledge -name '*.md' -printf '%f\n' \| grep -Ev '^[a-z0-9]+(-[a-z0-9]+)*\.md$' \| wc -l` | **0 exceptions** |
| duplicate basenames | `... -printf '%f\n' \| sort \| uniq -d \| wc -l` | **0** |
| full listing digest | 229-line listing (223 names + 6 section headers) | sha256 `4d5647ca4c6ca96017c043f1d5c928630086f2207435643d8c886fa541fe7ab7` |
| corpus manifest | `find corpus/knowledge -name '*.md' -print0 \| sort -z \| xargs -0 sha256sum` (223 lines) | sha256 `45bed989dd61978099193c0718325dc68479b65ba4820a4a9a79c44d0d4b2fee` |
| README | `sha256sum corpus/README.md` | `7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd` |
| index sweep | `python3 -B reports/round-28/readme/sweep.py` | exit 0; `rows 223 files 223`; `totals_line 223 totals_ok True`; `footer_ok True` |

Sweep output quoted:

```
parts {"civilizations": 94, "culture-material": 25, "linguistics": 25, "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 223 files 223
missing_from_index 0 []   topic_mismatch 0 []   orphan_rows 0 []   header_drift {}
totals_line 223 totals_ok True
footer {"date": "2026-10-19", "command": "python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge", "total": 223, "dir_totals": [25, 26, 25, 29, 24, 94]}
footer_findings [] footer_ok True
readme_sha256 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
exit=0
```

README edit sites (verified line numbers, current bytes):

| site | line | current text |
|---|---|---|
| myth-symbol header | `corpus/README.md:205` | `## myth-symbol/ (26)` |
| myth-symbol insertion rows | `:215`, `:216` | `divination-omen-systems.md` row, then `eschatology-world-end-systems.md` row |
| culture-material header | `:234` | `## culture-material/ (25)` |
| culture-material insertion rows | `:240`, `:241` | `calendar-festival-systems.md` row, then `costume-semiotics.md` row |
| totals line | `:544` | `Total knowledge entries: 223.` |
| counts footer | `:546-548` | `(total 223 files; directory totals 25/26/25/29/24/94).` |

The footer vector order is `linguistics / myth-symbol / culture-material / synthesis / verification / civilizations` (`reports/round-28/readme/sweep.py` `footer_live.order`), i.e. `25/26/25/29/24/94`.

## 2. The two filed proposals

| field | A — K02 | B — K04 / C01 |
|---|---|---|
| artifact | `reports/round-44/scout/K02-gap-scout.md` (17:27:27Z) | `reports/round-44/scout/K04-gap-verify.md` (17:22:20Z); `reports/round-44/cov/C01-entry-draft.md` (17:27:43Z) |
| topic | cartography / mapmaking — the survey → projection → drawing → reproduction chain and the map as a claim | dream / vision / trance — the altered state, its induction, the visionary career, and the licensing institutions |
| path | `corpus/knowledge/culture-material/cartography-and-mapmaking.md` | `corpus/knowledge/myth-symbol/dream-vision-trance.md` |
| partition delta | culture-material 25 → 26 | myth-symbol 26 → 27 |
| total delta | 223 → 224 | 223 → 224 |
| draft status | **seed + section outline + source shelf only** (`K02-gap-scout.md` §4.2-§4.3); no entry body | **full fenced entry** (`C01-entry-draft.md` §4) |
| declared stand-in | selected after eliminating carried r35/r42 candidates | K04 chose independently because K02 was absent; C01's draft declares itself a **spare** if K02 names a different gap (`C01-entry-draft.md:8`) |

At my cut, `reports/round-44/cov/` contains `C01-entry-draft.md`, `C05-collision.md`, `C06-scribe.md`; `C02-readme-draft.md`, `C03-audit.md`, `C04-contract-audit.md` had not landed. **C06-scribe's verdict is built on K04's gap and predates K02 and C01** (`C06-scribe.md:6` says K02 and C01-C05 are absent), so its "one named gap" statement is superseded by K02's 17:27:27Z filing. C02/C03/C04, when they land, may target either candidate; the integrator must check which one their bytes serve before applying anything.

## 3. Collision tests — candidate A (cartography)

| # | requirement | command | result | verdict |
|---|---|---|---|---|
| 1 | exact path unused | `ls corpus/knowledge/culture-material/cartography-and-mapmaking.md` | `No such file or directory` | **PASS** |
| 2 | no filename collision | `find corpus/knowledge -type f \| grep -iE 'cartograph\|mapmaking\|portolan\|cadastr\|atlas\|itinerar\|survey\|topograph\|map\|chart'` | 3 hits: `myth-symbol/sacred-kingship-mythic-charter.md` (substring `chart` in "charter"), `myth-symbol/sacred-topography-pilgrimage.md` (place register), `synthesis/dialect-faction-map-workflow.md` (`map` as verb) — none is a mapmaking file | **PASS** |
| 3 | no topic-line owner | `grep -rinE -- '^- topic:.*(cartograph\|mapmak\|portolan\|cadastr\|atlas\|itinerar\|survey\|topograph\|\bmap\b\|\bcharts?\b)' corpus/knowledge/*/*.md` | 11 hits, all adjudicated in §3.1 | **PASS, with a named boundary** |
| 4 | no section-heading owner | `grep -rniE '^#{1,4} .*(cartograph\|mapmaking\|portolan\|cadastr\|atlas\|itinerar\|survey\|topograph\|\bmap\b\|\bcharts?\b)' corpus/knowledge` | many metaphor/verb hits; the nearest is `sacred-topography-pilgrimage.md:96` ("Sacred geography as a diagram — and the era drift of a holy map"), which owns the sacred place diagram, not map production. `cosmology-cosmography.md:71,:102` **explicitly disclaims** survey maps (see §3.2) | **PASS, with a named boundary** |
| 5 | no near-duplicate slug | `difflib` over all 223 basenames | no high-similarity mapmaking name; nearest are unrelated (`cartography` is a new stem) | **PASS** |
| 6 | naming convention | `grep -E '^[a-z0-9]+(-[a-z0-9]+)*\.md$'` | matches | **PASS** |
| 7 | sort position | `{ find corpus/knowledge/culture-material -name '*.md' -printf '%f\n'; echo cartography-and-mapmaking.md; } \| LC_ALL=C sort \| grep -n -B1 -A1` | `5-calendar-festival-systems.md` / `6:cartography-and-mapmaking.md` / `7-costume-semiotics.md` | **PASS** |
| 8 | partition arithmetic | `ls corpus/knowledge/culture-material/*.md \| wc -l` | 25 → 26; total 223 → 224 | **PASS** |

### 3.1 Adjudication of candidate A's 11 topic-line hits

Every hit is a metaphor, a verb, or a different owned object; none names mapmaking as its subject.

| entry:line | the hit | disposition |
|---|---|---|
| `civilizations/africa-primary-sources.md:2` | "a bounded **source map**" | metaphor — a source inventory |
| `civilizations/finnic-sami.md:3` | "gákti as an **identity map**" | metaphor |
| `civilizations/mesoamerica-primary-sources.md:3` | "a reference **map** for the four Mesoamerican bases" | metaphor; the *lienzo* row is at `:58`, a source-provenance class |
| `culture-material/ritual-garments.md:3` | "the b.Arakhin 16a **atonement map**" | metaphor |
| `linguistics/dialect-register-consistency.md:3` | "a built **dialect map**'s internal consistency" | metaphor — a lect inventory |
| `linguistics/sacred-registers-liturgical-language.md:3` | ritual events "**map** to the competences" | verb |
| `linguistics/sound-symbolism.md:3` | "the three-way **map** (arbitrariness / iconicity / systematicity)" | metaphor — a conceptual schema |
| `myth-symbol/number-symbolism.md:3` | "a variance **survey**" | statistical sense |
| `myth-symbol/purity-pollution-boundary-systems.md:4` | "purity is … a **boundary map**" | metaphor — that entry's master claim |
| `myth-symbol/sacred-topography-pilgrimage.md:5` | "sacred-geography **mapping** … as a diagram: radial, quartered, linear-corridor, or archipelago" | **nearest neighbour**; owns the sacred place register and route, not the survey/projection/drawing chain |
| `synthesis/dialect-faction-map-workflow.md:2` | "**Map** dialect features … onto travel networks" | verb |

### 3.2 The partition's own disclaimer — the strongest ownership evidence

`corpus/knowledge/myth-symbol/cosmology-cosmography.md:71` (T-O row):

> "Hereford Mappa Mundi c. 1300; T-O diagrams are **symbolic, not survey maps** (§10)"

`corpus/knowledge/myth-symbol/cosmology-cosmography.md:102`:

> "T-O diagrams are symbolic devices, **not cartographic** claims."

The corpus therefore *names the survey-map register and says its own cosmography entry does not own it*. That is the same "named but unbuilt" shape the r42 lithic entry used, and it makes cartography unowned without needing a high raw mention count.

Near neighbours that do own adjacent pieces, and the boundary the new entry must state:

- `myth-symbol/sacred-topography-pilgrimage.md:5,:96` — place register, route-as-rite, sacred-geography diagram; **not** survey, projection, drawing, reproduction.
- `myth-symbol/direction-symbolism.md:51` — the true-vs-magnetic "compass trap" (orientation coding); the map's compass rose is a different object.
- `culture-material/architecture-settlement-lexicon.md:95` — "surveyed with the **groma** … The grid is **cadastral**" — one handoff sentence inside the city-plan lexicon; the new entry owns land survey as a map-production step and must not restate the settlement vocabulary.
- `culture-material/writing-media-surface-economy.md:3` — the seven surface families and cost ladder; the new entry owns map-specific media and reproduction.
- `civilizations/mesoamerica-primary-sources.md:58` — the lienzo/cartographic-history source class; cite the genre, do not restate the provenance inventory.
- `culture-material/transport-mobility-lexicon.md` — route maintenance; the new entry owns the route's representation.
- `myth-symbol/cosmology-cosmography.md:71,:102` — the world-model typology and the flat-earth calibration; cite the T-O contrast, do not restate it.

**One-owner-per-topic verdict for A: PASS**, conditional on the boundary table above being in the entry. Without it, the sacred-topography and architecture overlaps would read as partial second owners.

## 4. Collision tests — candidate B (dream / vision / trance)

| # | requirement | command | result | verdict |
|---|---|---|---|---|
| 1 | exact path unused | `ls corpus/knowledge/myth-symbol/dream-vision-trance.md` | `No such file or directory` | **PASS** |
| 2 | no filename collision | `find corpus/knowledge -type f \| grep -iE 'dream\|trance\|vision\|ecsta\|shaman\|incubat'` | no output | **PASS** |
| 3 | no topic-line owner | `grep -rilE -- '^- topic:.*(dream\|trance\|ecsta\|vision quest\|visionary\|shaman\|incubat)' corpus/knowledge/*/*.md` | 2 hits: `myth-symbol/divination-omen-systems.md` (one of fourteen technique rows), `civilizations/mongol.md` ("shamanic vocabulary") | **PASS, with a named boundary** |
| 4 | no section-heading owner | `grep -rniE '^#{1,4} .*(dream\|trance\|ecsta\|shaman\|incubat\|vision quest\|altered state\|possession)' corpus/knowledge` | 2 hits: `divination-omen-systems.md:1` (dreams as a sign source), `australia-aboriginal.md:36` (ancestral Dreaming, a different concept) | **PASS, with a named boundary** |
| 5 | no near-duplicate slug | `difflib` over all 223 basenames | closest `naming-collision-gate.md` at 0.609; not a collision | **PASS** |
| 6 | naming convention | `grep -E '^[a-z0-9]+(-[a-z0-9]+)*\.md$'` | matches | **PASS** |
| 7 | sort position | `{ find corpus/knowledge/myth-symbol -name '*.md' -printf '%f\n'; echo dream-vision-trance.md; } \| LC_ALL=C sort \| grep -n -B1 -A1` | `10-divination-omen-systems.md` / `11:dream-vision-trance.md` / `12-eschatology-world-end-systems.md` | **PASS** |
| 8 | partition arithmetic | `ls corpus/knowledge/myth-symbol/*.md \| wc -l` | 26 → 27; total 223 → 224 | **PASS** |

Adjudication of B's two topic-line hits:

- `corpus/knowledge/myth-symbol/divination-omen-systems.md:3` — the subject is *"divination and omen-reading as a designed symbolic technology"*; `dream-oracles and incubation` is **one of fourteen technique rows**. Its H1 (`:1`) names dreams among the reading technologies. The owner object is the **reading**, not the state, its induction, its training, or the visionary career.
- `corpus/knowledge/civilizations/mongol.md:3` — *"… Heaven/earth and shamanic vocabulary, deel dress codes, …"*; `shaman` is a lexical/civilization datum, not a system entry on altered states.
- `corpus/knowledge/civilizations/australia-aboriginal.md:36` — `## Dreaming, Tjukurpa and ancestral law-language coupling` is the ancestral **Dreaming** (law-time), not ordinary sleep dreams. The entry must distinguish the two by name.

**One-owner-per-topic verdict for B: PASS**, conditional on the boundary section distinguishing the divination reading from the state and naming the Australian Dreaming distinction. C01's draft already carries that section (`C01-entry-draft.md` §1.5), and the fenced entry's `- gap filled:` line states the same split.

## 5. Landing-impact model — only the entry and README change

### 5.1 Dry runs (isolated byte-copies; no corpus write)

For each candidate, a copy of `corpus/` was made under `.scratch/c05/`; the `after` copy received a **synthetic placeholder** at the exact candidate path plus a synthetic README row at the correct insertion point. `diff -rq` results:

```
# candidate A — cartography
Only in .scratch/c05/dry3/after/knowledge/culture-material: cartography-and-mapmaking.md
Files .scratch/c05/dry3/base/README.md and .scratch/c05/dry3/after/README.md differ
diff-exit=1

# candidate B — dream
Only in .scratch/c05/dry2/after/knowledge/myth-symbol: dream-vision-trance.md
Files .scratch/c05/dry2/base/README.md and .scratch/c05/dry2/after/README.md differ
diff-exit=1
```

Each delta is exactly **one added entry and the README**. The placeholder rows were synthetic; the actual row must be the entry's own `- topic:` text byte-equal (README convention stated at `corpus/README.md:36` and re-stated at `:51,:61,:95`).

### 5.2 Why no secondary index exists

- `corpus/README.md` is the only enumeration of entries. No JSON/TSV/YAML manifest under `corpus/` or `tools/` indexes `corpus/knowledge/*.md`; the `grep -rln 'corpus/knowledge'` hits outside `reports/` are lesson sources, example packets, and gate fixtures, not an entry index.
- `tools/source-audit-inventory.py` is read-only by construction: *"It opens corpus files read-only and has no code path that writes inside a scan root"* (`tools/source-audit-inventory.py:16-17`).
- `reports/round-28/readme/sweep.py` reads README + files and reports; it writes nothing.

### 5.3 Post-landing verification

Baseline manifest: 223 lines, digest `45bed989…d4b2fee` (reproduced by the §1 command). After either landing:

```
find corpus/knowledge -name '*.md' -print0 | sort -z | xargs -0 sha256sum > /tmp/after.sha256
# expected: 224 lines = the 223 baseline lines (all byte-identical) + 1 new entry;
# README is outside this manifest.
comm -23 <(sort .scratch/c05/corpus-manifest-baseline.sha256) <(sort /tmp/after.sha256)   # must be empty
# ^ empty proves no baseline entry was removed or changed.
```

Any baseline line missing from the after-manifest is an overwritten/deleted entry; any changed digest is a modified entry. Both fail claim C. The README is the only `M` path expected.

## 6. Cross-candidate coordination (the +1 constraint)

Claim C's `after_required` is *"one new entry landed on a verified-unowned topic, total 224"* (`reports/round-44/claims.json:39-41`). Both candidates target 224 individually, and they are disjoint:

- **No mutual collision:** different partitions (`culture-material` vs `myth-symbol`), different slugs, and no shared subject terms. A cartography entry would not own dream/trance material, and a dream entry would not own maps/survey/projection.
- **Landing both is forbidden by the claim:** 223 + 2 = **225**, not 224; two entries would also be two C landings where the claim declares one.
- **Spare status:** C01's draft explicitly declares itself a spare if K02 names a different gap (`C01-entry-draft.md:9`). K02 has now named a different gap, so under the draft's own terms candidate B is the spare, not automatically the claim's landing — unless the integrator selects it.
- **Draft completeness differs:** B has a full entry draft; **A has a seed, a section outline and a source shelf but no drafted entry**. If the integrator selects A, a drafting seat (C01 successor or a new executor) must still produce the entry and C03/C04 must audit it; applying K02's seed directly would skip the claim's "drafts it under the partition's naming + entry contract, audits pre-landing" sequence. If the integrator selects B, the draft exists but its `- gap filled:` line and header claim K04 as the scout, not K02; the claim's wording does not require K02 specifically, but the evidence chain should record which scout the landing follows.

**This seat makes no selection.** Both candidates are collision-cleared; the integrator owns the one-gap ruling.

## 7. Pre-existing README defect observed (not caused by either landing)

`corpus/README.md:11` (revision 2.4 prose) records the vector move as
`25/23/25/29/24/94 → 25/23/26/25/24/94`. Neither vector is the live partition:
the "after" vector sums **217**, not 223, and it puts `23` in the linguistics slot
and `25` in the culture-material slot. The correct live vector — and the one in
the footer at `:548` — is **`25/26/25/29/24/94` = 223**. This is the rev-2.4
prose-vector defect C02's mission names. It does not create a collision and is
not fixed by this seat; C02 should either repair it in the rev-2.5 block or
record it as a carried defect, never silently reproduce it.

## 8. Residual risks (named, not hidden)

1. **Candidate choice (highest).** Both are collision-free; only one may land. If C02/C03/C04 artifacts target the unselected candidate, they are spare evidence and must not be applied.
2. **Boundary sections are conditions of the PASS.** A cartography entry without the sacred-topography/architecture/direction/cosmography boundaries, or a dream entry without the divination/state and Australian-Dreaming boundaries, would read as partial second ownership on review.
3. **Draft completeness for A.** K02's seed is not an entry. Selecting A without a drafted, audited entry fails the claim's sequence.
4. **README row byte-equality.** Each new row must equal its entry's `- topic:` line; the sweep's `topic_mismatch` leg will fail otherwise.
5. **C06-scribe is superseded on the gap count.** `C06-scribe.md:6` states K02 and C01-C05 were absent; K02 has since filed a different candidate. Its verdict candidate ("the named gap is dream") is not wrong as a measurement at its cut, but it is not the current filing state.
6. **Source-shelf risk (both).** A's modern cartography shelf and B's modern dream/trance shelf are largely not in-corpus; every unregistered item must be `(to-verify)`. That is a provenance risk for C03/C04, not a collision risk.

## 9. Re-run contract for the actual landing

Substitute the chosen slug and topic terms; run at the then-current HEAD before applying bytes. Every check must pass.

```bash
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
SLUG='myth-symbol/dream-vision-trance.md'          # or culture-material/cartography-and-mapmaking.md
TERMS='dream|trance|ecsta|vision quest|visionary'   # or cartograph|mapmak|portolan|cadastr|survey
FRAGMENTS='dream|trance|vision|ecsta|shaman|incubat' # or cartograph|mapmaking|portolan|cadastr

# 0. baseline integrity
git status --porcelain                          # expect only ?? reports/round-44/
find corpus/knowledge -name '*.md' | wc -l      # expect 223

# 1. exact path must be absent
test ! -e "corpus/knowledge/$SLUG" || { echo "COLLISION: path exists"; exit 1; }

# 2. no filename collision in any partition
find corpus/knowledge -type f -iname "$(basename "$SLUG")" | grep -q . && { echo "COLLISION: basename exists"; exit 1; }
find corpus/knowledge -type f | grep -iE "$FRAGMENTS" && exit 1

# 3. no topic-line owner; every hit must be adjudicated adjacent in the report
grep -rilE -- "^- topic:.*($TERMS)" corpus/knowledge/*/*.md

# 4. no section-heading owner
grep -rniE "^#{1,4} .*($TERMS)" corpus/knowledge

# 5. naming convention
printf '%s\n' "$(basename "$SLUG")" | grep -Eq '^[a-z0-9]+(-[a-z0-9]+)*\.md$' || exit 1

# 6. sort position within the target partition
{ find "corpus/knowledge/$(dirname "$SLUG")" -name '*.md' -printf '%f\n'; echo "$(basename "$SLUG")"; } \
  | LC_ALL=C sort | grep -n -B1 -A1 "$(basename "$SLUG")"

# 7. landing delta: only the new file + README may differ
find corpus/knowledge -name '*.md' | wc -l      # expect 224
python3 -B reports/round-28/readme/sweep.py     # expect rows 224 files 224, exit 0
```

Fail conditions: path exists; any filename/topic/heading owner is a real owner (not an adjudicated adjacent row); the slug violates the naming convention; the manifest shows any baseline entry changed or removed; any path other than the new entry and `corpus/README.md` differs; or **both** candidates land (total 225).

## 10. What this seat did not do

- Wrote only this file under `reports/round-44/cov/`. No `corpus/**` write, no staging, no README edit; the dry runs live under `.scratch/c05/` only.
- Did not run any `reports/round-*/run-validation.py` in-tree; the only instrument run was the read-only `reports/round-28/readme/sweep.py`.
- Did not edit any filed byte (`reports/round-1..43/**`, `corpus/lessons/*.md`, `tools/gates/frozen/**`), commit, push, install, or use the network.
- Did not choose between the two candidates and did not endorse either topic; both are tested because both are filed.

## 11. Handoff

- **Both exact paths are collision-cleared** at `c9f4eaa`:
  - A: `corpus/knowledge/culture-material/cartography-and-mapmaking.md` — PASS with the §3.2 boundary table; **no entry draft yet**.
  - B: `corpus/knowledge/myth-symbol/dream-vision-trance.md` — PASS with the divination/state and Australian-Dreaming boundaries; **full draft in `C01-entry-draft.md` §4**.
- **Claim C may land exactly one.** Landing both yields 225 and fails. The integrator must make the one-gap ruling first; C01's draft self-identifies as a spare if K02's gap differs, and K02's gap does differ.
- **README arithmetic for each choice:**
  - A: `## culture-material/ (25)` at `:234` → `(26)`; row between `:240` and `:241`; totals `:544` → 224; footer `:548` → `25/26/26/29/24/94`.
  - B: `## myth-symbol/ (26)` at `:205` → `(27)`; row between `:215` and `:216`; totals `:544` → 224; footer `:548` → `25/27/25/29/24/94`.
- **Re-run §9 against the chosen slug before applying bytes**; this clearance is a reading of one tree state at `c9f4eaa`, not a prediction that a later tree is unchanged.
- **Correction path:** if the integrator lands a target not covered here, file a successor collision note with the §9 outputs; do not edit this file's verdict in place.
