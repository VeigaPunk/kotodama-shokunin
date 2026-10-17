# Review — component 03-morphosyntax (culture D2)

- reviewer: round-3 review worker
- target: `examples/culture-d2/components/03-morphosyntax.yml`
- status: **ABSENT — component not delivered**
- canon: not canonized (D2 design drill)

## Evidence

- Look 1 (~14:25Z): `examples/culture-d2/` does not exist; `examples/`
  contains only `handoff-packet.sample.md` / `.yml`.
- Wait-and-retry: 60 s sleep, per assignment protocol → same result.
- Look 2 (~14:26:33Z, after the retry window): `03-morphosyntax.yml`
  still absent; **no sibling components present either** (no
  `components/` and no `reviews/` directory existed before this file).
- Repo was not idle: `tools/gates/fixtures/*` were modified within the
  5 minutes preceding look 2, so this lane had active writers while
  component 03 was missing. Absence is therefore "not yet delivered",
  not "repo untouched".

## What I checked instead (corpus side complete)

Chunk-read in <=80-line windows, so the review can run immediately on
a re-dispatch:

- `corpus/knowledge/linguistics/morphological-typology.md` (116 lines,
  full) — §1 two axes, §3 typology cost sheet + marking locus, §4
  process catalog, §5 root-and-pattern calibration, §6 Mithun cline,
  §7–§8 cascades, §9 Givón/Hopper–Traugott wheel, §10 calibration,
  §11 application protocol (steps 2, 5, 6 bind the component).
- `corpus/knowledge/linguistics/syntax-typology.md` (109 lines, full) —
  §1 order + Greenberg/Dunn calibration, §2 alignment + split triggers,
  §3 relative-clause strategy + Karlsson center-embedding ceiling, §4
  evidential sizing table + mirativity, §5 calibration, §6 consistency
  checklist (8 items = review axes).
- `corpus/knowledge/linguistics/phonetics-phonology.md` — §2 inventory
  anchors, §3 phonotactics, §6 prosody (Hyman 2006 pitch accent), §7
  whistled-speech coupling (mountains + long-distance herding), §9
  pitfalls. Read for the planned 02 cross-check.

## Pre-registered checklist for re-run

When `03-morphosyntax.yml` lands, the review will test, each violation
as `component-id | violation | corpus path:section that forbids it`:

1. Synthesis + fusion index given as numbers, wheel position dated to
   an era (`morphological-typology.md:§1, §9, §11.1`).
2. >=1 non-affixal process, with a pitch-accent-relevant one (tone/
   ablaut) rather than a bare affix stack (`:§4, §11.2`).
3. Marking locus set with typology, not left random (`:§3` corollaries).
4. Full paradigm (8–12 forms) + sentence family present (`:§11.5`).
5. Order chosen and harmonic sweep run; no both-free-order-and-zero-
   morphology language without stated history
   (`syntax-typology.md:§1, §6.2`).
6. Alignment chosen with any split trigger and ellipsis pivot (`:§2`).
7. Evidential system sized to a 2–5 term model and consistent with the
   name/rumor/storm-law ecology; nothing past the Fleck 2007 ceiling
   (`:§4`); mirativity not double-marked against phonology.
8. RC strategy matched to order + dominant genre; Karlsson ceiling
   respected (`:§3`).
9. Cross-check against **02 phonology**: every morpheme listed must be
   buildable from 02's segment inventory, phonotactics and pitch-accent
   rules; pitch-accent placement in the morphology must match 02's
   prosody block. (02 was also undeclared at review time — if 02 lands
   after 03, this item degrades to a `to-verify` note rather than a
   violation.)
10. Design-spine coupling: verticality (ascent/descent, seasonal poles)
    and wind (breath, soul-carrier, storm law) present in grammatical
    categories or registers; **no silent D1 import** (river/tying/
    binding imagery) (`PROVINCE.md` spine + packing/tying contrast in
    the D1/D2 brief).
11. `canon: not canonized (D2 design drill)` present; `follows:` list
    cites the corpus decision tables above; no fabricated scholarship
    (real-language exemplars only, `(to-verify)` where unsure).

## Re-run condition

Re-dispatch a review worker against the same path once the component
writer reports delivery. Nothing in this file is a finding about the
component's content — no content was available to inspect.