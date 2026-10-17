# Review — component 02-phonology (culture D2)

- reviewer: round-3 review worker
- target: `examples/culture-d2/components/02-phonology.yml` (509 lines, 39,433 bytes; delivered 2026-10-17 11:33:06)
- status: **CLEAN** — no corpus-forbidden violation found
- canon: not canonized (D2 design drill)

## Delivery history (why the review ran late in the window)

- Look 1 (~11:23): `examples/culture-d2/` did not exist. 60 s wait-and-retry
  per assignment protocol → still absent at 11:26:35.
- Bounded grace windows while sibling components landed (11 components by
  11:31:35, 02-phonology still the missing one). Delivered 11:33:06.
  Reviewed on the delivered bytes; no prior absent-verdict was filed.

## Violations

None. The list is empty — no entry of the form
`02-phonology | <violation> | <corpus path:section that forbids it>` was found.

## What I checked

Corpus read in <=80-line chunks: `corpus/knowledge/linguistics/phonetics-phonology.md`
(full, 278 lines) plus `corpus/knowledge/verification/phonology-sanity-gate.md`
§1–§5 for the executable audit axes, and `01-brief.yml` for the D2 contract
(SEED-05/07/08, failure modes).

1. **Inventory vs typology bands** — `phonetics-phonology.md:§2`,
   `phonology-sanity-gate.md:§3`. 15 consonants (p t k b d g m n s ʃ r l j w h)
   sit in the WALS "moderately small" band (15–18) with a contact-history
   justification (F-1); the 19–25 modal band is explicitly not chased. 5 vowel
   qualities (a e i o u) sit in the 5–6 modal band and match the triangular
   dispersion §2 carries for 5-vowel systems. No size = sophistication claim
   (§2, §9.6). Gate T-C and T-V silent.
2. **Phonotactics legality** — `:§3`. Template (C)V(C) written first; empty
   onset licensed word-initially only; coda set {n l r s}; no onset or coda
   clusters, no geminates, no consonant-only syllables, no triple-identical CV
   root (P-1..P-5). Legal shapes W-21 and negative controls W-22 (sta, tapl,
   kti, hamp) agree with the template. Gate P-PATTERN, P-NUCLEUS, P-CODA,
   T-SYL silent; A-VACUOUS silent (rule environments are possible under the
   declared template).
3. **Markedness and implications** — `:§4`. Walked one by one: no
   front-rounded vowel (M-ROUND not triggered), no ejective (M-EJECT not
   triggered), no voiced fricative (the voiced-fricative implication is not
   left hanging, C-4), nasals have same-place orals (M-NASAL silent), mid
   vowels have high peers (M-MID silent), the velar nasal is an allophone
   instead of a lone phoneme (C-3, §4 "add what your exotics entail"). No
   implication broken for flavor. Gate M-* silent.
4. **Allophony consistency** — `:§5`. Nine finite rules parse as one pass in
   stated order; they are three corpus families plus finite expansion (the
   four place-assimilation rules are one class rule over two voicing series —
   the count above §5's suggested 5–8 is expansion, not extra texture, stated
   in F-4). Every rule carries a drift origin (§9.10); no rule is a grab-bag;
   no feeding/bleeding claimed (AL-ORDER). Hand-verified the witnesses against
   the rules and template: hus → [ɸuh] (AL-5+AL-7), sanpa → [sampa] (AL-1),
   tika → [t͡sika] (AL-8), keka → [keka] and teka → [teka] (blocked sites),
   sara [sára] / [sará] (accent pair). Independent check: a small rule applier
   over the delivered rule list reproduced all 20 checked surface forms
   (W-1..W-16 shapes, the W-21 legal roots, and the kiru → [ciru] prediction
   noted below) with zero mismatches.
5. **Neutralization findings** — `verification/phonology-sanity-gate.md:§5`.
   The gate's three A-NEUTRAL findings (AL-1, AL-2, AL-7) are permitted by §5
   ("allophone neutralization into another phoneme's usual phone is
   permitted"), and the required reanalysis is supplied: the /n/ : /m/
   contrast is witnessed in onsets (W-4, W-5), and coda [h] cannot lose a
   contrast because /h/ is never licensed in a coda (P-3, AL-7 note). These
   are design intent, not defects.
6. **Prosody** — `:§6`. Pitch accent as a type distinct from tone (Hyman 2006
   via §6); `tones: 0` is consistent and no tone rule exists (A-TONE would
   fire otherwise). Culminative single peak, lexical minority class, licensed
   shifts, two levels, no contour storage (AC-1..AC-7, CX-NOTE). Tonogenesis
   origin carried as invented drift with the corpus model cited (AC-6, CAL-5).
   Intonation specified above word prosody (AC-7, CX-1..CX-4). The §6 apply
   line "long-distance speech takes pitch prominence" is used as a warrant
   (R-2, ENV-2). The discredited rhythm-class dichotomy is not used.
7. **Environment arbitration** — `:§7`. Exactly one solid coupling used as a
   warrant (whistled register: mountains + long-distance herding, R-1/ENV-1);
   all four contested seeds are DECLINED with statuses and citations
   (ENV-3..ENV-6, CAL-2, CAL-3), including the wind-noise claim that has no
   corpus source — marked to-verify instead of invented. §9.8 avoided.
8. **Sound symbolism** — `:§8` not used to select any phoneme or vowel (F-7);
   reserved for naming at population scale. §9.7 avoided.
9. **Pitfalls checklist** — `:§9` walked PC-1..PC-12; the two needing repair
   (achronic allophony, decoration prosody) are repaired in-file.
10. **Design spine (SEED-07/08)** — verticality: the accent is named and
    enacted as valley vs ridge locus, default peak = valley, licensed movement
    rightward = "up the slope" (AC-2..AC-4, spine_coupling). Wind: /h/ as the
    breath phoneme with wind-named allophones [ɸ]/[ç], the final-breath rule,
    and the whistled ridge register (C-5, AL-5..AL-7, R-1). Anti-import: no
    river, ferry, tying, binding, or knot-as-speech imagery appears anywhere in
    the file; the tally knot appears only as a deferred record technology
    (R-3, WR-1, spine_check) and explicitly not a phonological gesture.
11. **Executable gate** — `python3 tools/gates/phonology-sanity-gate.py
    examples/culture-d2/components/02-phonology.yml` on the delivered bytes:
    **exit 1**, exactly three REVIEW findings (A-NEUTRAL on
    notable_rules[1], [2], [7]), no FAIL, no G-DATA — byte-for-byte the claim
    in the file's own `gate_run`/`gate_result`. Negative controls on stdin
    (same file with the template removed; same file with `tones: 5`)
    additionally produced P-PATTERN and T-TONE, so the gate is demonstrably
    reading this file's `phonology` block rather than passing everything.
12. **Canon hygiene / provenance** — `canon: not canonized (D2 design drill)`
    present; `follows:` carries 12 corpus path+section citations; comparators
    are corpus entries, no fabricated scholarship; contested claims stay
    flagged; contract key names present
    ({consonants, vowels, phonotactics, tones, notable_rules}) and every
    record carries an id.

## Review-class observations (not violations, for the assembler)

- **Wording only:** W-11 calls the co-application of AL-5 and AL-7 "a feeding
  chain", while AL-ORDER correctly states no rule feeds or bleeds another.
  Neither rule creates the other's environment (the /s/ is word-final either
  way), so nothing in the ordering is affected. Cosmetic.
- **Coverage nit:** no positive witness exercises a coda /l/ or /r/ (coda
  licensing is positively tested for /n/ in W-3/6/7/9 and /s/ in W-11,
  negatively in W-22). Add one if the assembler wants full coda coverage.
- **Field hygiene:** W-21's `surface_ipa` holds a note ("sample legal
  shapes"), not an IPA string — read it as a phonotactics witness only;
  note that /kiru/ would surface [ciru] under AL-9 if the field is ever
  machine-read.
- `:§3`'s "generate 100 words" apply line is not instantiated here (22
  witnesses); the word list is assigned to the lexicon component by the
  01-brief registry and PC-4 records the deferral — not forbidden by §3,
  which addresses the design workflow, but the assembler should confirm the
  word list is generated against this template.

## Re-run condition

Per `01-brief.yml` discipline (supersede-by-new-file only): if a new file
revision is delivered, re-dispatch a review against the new bytes. Nothing in
this file is a finding about any later revision.