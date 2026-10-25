# ScoutDanceOwners — claim C gap-surface proof

Seat: `L1Kotodama71.ScoutDanceOwners` (LEAF, no delegation). Date: 2026-10-25.
Question: prove claim C's gap surface — 0 word-bounded filename owners and 0 topic-line
owners for the dance/performance/movement register before `dance-performance-movement-codes.md`
(claim C surface, `reports/round-71/claims.json` line 17).

## 1. Exact command outputs

Working dir: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.

### (1) Filename sweep
```
$ find corpus/knowledge/culture-material -maxdepth 1 -type f -name '*danc*'
(no output — 0 files, exit 0)
```
**0 filename owners** (also 0 files named `*choreograph*` / `*performance*` / `*movement*`
at that depth — verified by directory listing).

### (2) Topic-line sweep (as specified)
```
$ grep -rniE '^- topic:.*(danc|choreograph|movement culture|performance)' corpus/knowledge/culture-material/*.md
corpus/knowledge/culture-material/funerary-material-culture.md:4:
- topic: how a culture disposes of its dead ... WORD (the death register: avoidance terms, ...
```
1 match in 1 file. **This match is a false positive**: extracting the matched token gives
`danc` as the substring inside **"avoidance"** (`grep -oE '(danc|choreograph|movement culture|performance)'`
→ `1 danc`; the only occurrence sits in `avoidance terms` in the WORD register of
funerary-material-culture.md). Re-running with word boundaries confirms zero true claims:
```
$ grep -rniE '^- topic:.*\b(danc|choreograph|movement culture|performance)\b' corpus/knowledge/culture-material/*.md
(no output — exit 1)
```
Supplementary (beyond the spec, to close the classification): topic lines in
myth-symbol + linguistics contain no dance/performance/movement claims either — the only
tokens matching an extended pattern `\b(danc|choreograph|movement culture|performance|music|theater|theatre|stage)\b`
are `stage` (4×, e.g. "life-stage" in hero-journey-variants, purity-pollution-boundary-systems,
language-shift-obsolescence-revival topics). Zero `danc`/`choreograph`/`performance`/`movement culture`
tokens in any topic line of the three dirs.

**0 topic-line owners for the dance/performance/movement register.**

### (3) Word sweep (as specified)
```
$ grep -rniE '\b(danc|choreograph|movement)\b' corpus/knowledge/culture-material/*.md corpus/knowledge/myth-symbol/*.md corpus/knowledge/linguistics/*.md
69 matches in 28 files (full 69 lines captured verbatim; per-file counts below)
```

## 2. Classification — no whole-register owner

Whole-register owner = topic line claims dance/performance/movement as its surface. **None
exists.** All 69 hits are incidental (one-word usage) or partial owners of *adjacent*
registers. Per-file classification (counts from `grep -rc`):

Culture-material (12 files):
| file | hits | hit(s) | class |
|---|---|---|---|
| adornment-body-codes.md | 1 | 109 "revival movement" | incidental (social movement) |
| bathing-and-body-hygiene.md | 1 | 90 "public-bath movement" | incidental (social movement) |
| costume-semiotics.md | 1 | 70 "tightness, transparency, movement" | incidental (display axis in a list) |
| dress-through-eras.md | 1 | 13 "choreograph movement/posture/opacity" | **partial owner** (corpus's only `choreograph` token; body display choreography) |
| era-periodization-models.md | 2 | 40,90 "4-Movement" | incidental (Aztec day-sign name) |
| funerary-material-culture.md | 1 | 61 "cremation movement" | incidental (social movement) |
| games-play-sport-contests.md | 1 | 115 "movement of games along routes" | incidental (physical transit) |
| hunting-foraging-subsistence.md | 1 | 58 "seasonal camp movement" | incidental (mobility logic) |
| medicine-healing-codes.md | 1 | 33 "diet, sleep, movement" | incidental (bodily regimen) |
| pastoralism-animal-husbandry.md | 11 | movement/mobility as production logic (16,21,57,59,61,204,206 …) | **partial owner** (movement in mobility sense; explicitly "owns the herd's movement logic") |
| transport-mobility-lexicon.md | 1 | 3 "no vehicles, roads, or movement vocabulary — this entry fills it" | **borderline topic-line claimant** — see §3 |
| masks-masquerade.md | 0 (regex blind spot) | 15 true dance tokens in 9 lines (20,52,59,62,63,64,86,122,133: dancer/dances/dance/performance) | **partial owner** (nearest to dance) — invisible to `\bdanc\b` because all tokens are inflected (`dance/dances/dancer`); found via supplementary `\bdanc(e|es|er|ing|ers)?\b` |

Myth-symbol (11 files): animal-symbolism (Olin movement day-sign), cosmology-cosmography
("4 Movement" Fifth Sun), death-afterlife-eschatology (2: "movement nationalizes a death rite",
hospice movement), divination-omen-systems (3: 2012 date-divination movement), eschatology-world-end-systems
(4: purity/social movement rows), heraldry-emblems ("inspection at movement"), myth-ritual-theories
(2: goddess-spirituality movement), plant-symbolism (Chipko movement), purity-pollution-boundary-systems
(4: purity movement), sacred-topography-pilgrimage (circumambulation: "movement *is* the rite"),
symbolism-synthesis-method (peace-movement emblem). **All incidental.**

Linguistics (5 files): gesture-co-speech-pointing (6: head/body movement as communication —
**partial owner**), language-shift-obsolescence-revival (4: "revival movement" — incidental),
orality-formulaic-language (1: madīḥ "movement" = ode section — incidental), phonetics-phonology
(1: movement carries contrast — sign parameter — incidental), register-lexicon-ceilings (1:
syllable movement — language-game operation — incidental), sign-languages-manual-modality (13:
movement as Stokoe phonological parameter — **partial owner** of movement in the sign modality).

## 3. Blocker check

**No whole-register owner exists → no claim-C blocker.**

One nuance to surface: `transport-mobility-lexicon.md:3-4` is the only file whose topic
block explicitly claims "movement vocabulary" as its surface ("gap: transport/mobility register
absent … no vehicles, roads, or movement vocabulary — this entry fills it"; topic = "mobility
as a four-layer material system"). Under a literal reading of the word *movement*, this is a
topic-line claimant — but of the **transport/mobility** register, not the dance/performance/movement
register claim C targets. It does not block the dance/performance gap; flagging for the main
agent's reading of claim C's sweep.

## 4. Three nearest partial-owner files (one-line topics)

1. **masks-masquerade.md** — topic: "masks and masquerade as worn object, embodied presence and
   licensed voice — what a mask is said to be (portrait, presence, type, voice), the masking
   complex (object, ensemble, wearer, presence, keeper), access rules …" — 15 dance tokens
   (dancer/dances/dance, + "performance" line 86); treats dance and music as components of the
   masking complex without owning them.
2. **dress-through-eras.md** — topic: "how real costume systems organize the three things a
   scene can show — silhouette (the load-bearing lines), materials (the fiber/dye/fastening
   stratum), and who-wears-what rules (rank, gender, life-stage, cult) — across six era-clusters
   …" — line 13 "choreograph movement/posture/opacity": the only `choreograph` token in the corpus.
3. **gesture-co-speech-pointing.md** — topic: "co-speech gesture, pointing and quotable gestures
   as a conlang and worldbuilding method — gesture as part of the utterance …" — 6 movement hits,
   all body movement as communication (head-movement inversion, eye-gaze head movement, mirror-neuron
   movement topography); owned by linguistics.

Honourable mentions: sign-languages-manual-modality.md (13 movement hits as phonological parameter),
pastoralism-animal-husbandry.md (11 movement hits as herd-mobility logic), transport-mobility-lexicon.md
(borderline topic-line claimant, §3), music-instrument-lexicon.md (music register; 1 dance token,
`bugaku` dance-music genre name, line 74), costume-semiotics.md (1 movement token as modesty axis).

## 5. Verdict

Claim C's gap surface **holds**: 0 filename owners, 0 topic-line owners for the
dance/performance/movement register (the single literal topic-grep match is the `danc`⊂"avoidance"
false positive), and no whole-register owner to block it. The closest standing content is
masks-masquerade (dance-in-masquerade), dress-through-eras (choreography of display), and
gesture-co-speech-pointing (body movement as communication) — all partial, none claiming the
register surface.

Note: the assigned command (3) regex `\b(danc|choreograph|movement)\b` undercounts dance
content because all dance tokens in corpus are inflected (`dance/dances/dancer`); the claim-C
sweep should use `\bdanc(e|es|er|ing|ers)?\b` to see masks-masquerade. No tools installed
(no installs needed; pacman untouched).
