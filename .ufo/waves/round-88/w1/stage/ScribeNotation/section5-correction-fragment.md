# §5 correction fragment — one bullet, staged not applied

Scope: this file proposes a precise replacement for **one** bullet in
`corpus/knowledge/linguistics/numerals-and-measures.md` §5 ("Counting technologies:
fingers, bodies, tallies, knots, rods"). It is a fragment for the integrator to apply;
nothing here was written to the production entry, and no other part of the entry is
touched. The entry's own history — its round-10 authorship note, its bibliography, its
`(to-verify)` list and its section order — is left exactly as it stands.

## The bullet as it stands today (line 111 at base `4956282281`)

```
- **Numeral notation vs numeral words** is a separate system: cumulative tallies, ciphered signs (Greek alphabetic numerals, Roman), and positional notation with a zero (Babylonian place value; the Indian decimal positional system) are typological stages (Chrisomalis 2010). A culture can count in words fluently and write numerals cumulatively — the mismatch is a dating tool (`writing-systems.md`).
```

## What is wrong with it, and what is not

Four defects, each separable, each with an opened source behind it. Nothing else in the
bullet needs to move.

1. **"typological stages" is a teleology the opened source rejects.** The two-axis
   typology is a classification of five attested structures, not a sequence. S931
   (Chrisomalis 2018, "Classifying numerical notations", body paragraph 10) states that
   the typology "avoids the teleological argument of Ifrah (1987) and Dehaene (1997) that
   sees decimal, positional numeration as the end-point of a developmental sequence
   towards perfection" and that "it is evident that there is no perfect system". The
   bullet's word "stages" is exactly the framing the source disowns.
2. **The list is not the typology's list, and it is not one axis.** It mixes three
   items — cumulative, ciphered, positional — where the source's grid is
   three coefficient principles (cumulative, ciphered, multiplicative) across two
   power-combination principles (additive, positional), yielding five types and one
   excluded combination. S931, body paragraph 7: "All numerical notations fall into five
   basic typological categories, across two dimensions".
3. **"cumulative tallies" conflates two different systems.** A tally has no base and
   every mark stands for one unit; a cumulative *notation* is base-structured. S931,
   body paragraph 21 (section "Tallying"): "whereas numerical notation systems are
   structured through a base". The entry's own §5 already treats tallies separately.
4. **"positional notation with a zero (Babylonian place value …)" is wrong about
   Babylon.** The opened Babylonian page reports that there was "no zero to put into an
   empty position", so 1 and 1,0 had the same representation, and that a symbol for the
   empty place was invented later. S932, body, paragraph on the empty place.

Not wrong, and to be kept: that numeral notation is a separate system from numeral
words; that a culture can count fluently in words and write cumulatively; that the
mismatch is a dating tool; and the cross-reference to `writing-systems.md`.

## Proposed replacement bullet (single line, one id)

```
- **Numeral notation vs numeral words** is a separate system: the graphic numeral systems in the record are five attested types on two axes — a coefficient principle inside each power of the base (cumulative, ciphered, multiplicative) crossed with a power-combination principle across powers (additive, positional), which yields five types and one excluded combination (§4b; S931). They are types, not stages: the typology carries no perfect system and no developmental order, and a culture may write numbers in a form its neighbours read differently (S931). A tally is not a notation — it has no base, and each mark still stands for one unit (S931). Babylonian place value is the standard positional case and ran without a zero for the empty place until a sign was later added (S932). A culture can count in words fluently and write numerals cumulatively — the mismatch is a dating tool (`writing-systems.md`).
```

## Why this shape and not another

- **One S-id per line is preserved.** The replacement carries S931 twice and S932 once
  on one line, so it must be split across lines or reduced to one id. The proposed
  replacement above is a single line and therefore **fails QUALITY criterion 15's
  clause-scoping lint** (`tools/check-cited-lines.py` reports MULTI-ID on any line
  holding two or more distinct S-ids). The integrator must use this **split** form:

```
- **Numeral notation vs numeral words** is a separate system: the graphic numeral systems in the record are five attested types on two axes — a coefficient principle inside each power of the base (cumulative, ciphered, multiplicative) crossed with a power-combination principle across powers (additive, positional) — and they are types, not stages (§4b; S931).
- The typology carries no perfect system and no developmental order, so a culture may write numbers in a form its neighbours read differently, and a choice of type is a choice of trade-offs rather than a stage (S931).
- A tally is not a notation: it has no base, and each mark still stands for one unit (S931).
- Babylonian place value is the standard positional case and ran without a zero for the empty place until a sign was later added (S932).
- A culture can count in words fluently and write numerals cumulatively — the mismatch is a dating tool (`writing-systems.md`).
```

- **"Chrisomalis 2010" is not deleted.** The 2010 monograph, *Numerical Notation: A
  Comparative History*, stays in the entry's bibliography (frontmatter, library-level
  citations, "not re-fetched this round"). The replacement stops using it as the
  warrant for a stage order, because this round opened the 2018 article (S931) and the
  2010 locator was not re-fetched. A `(to-verify)`-grade locator is left standing in
  the bibliography rather than silently promoted or silently dropped.
- **No new section numbers are invented.** The replacement points at §4b, which the
  integrator adds in the same landing; if §4b does not land, the pointer is dropped
  rather than left dangling.
- **Nothing is claimed about historical truth.** Every clause of the replacement is
  about how the typology is structured and what two opened sources report; the
  calibration of the type names as one scholar's analytical grid lives in §4b.6, not
  here.

## Checks the integrator can run

```
python3 -B tools/check-cited-lines.py corpus/knowledge/linguistics/numerals-and-measures.md
```

must exit 0 after the landing (no MULTI-ID line, no table row carrying an S-id), and

```
grep -c 'typological stages' corpus/knowledge/linguistics/numerals-and-measures.md
```

must return 0, and

```
grep -c '## 4b. Numeral notation: two axes, five types, and their trade-offs' corpus/knowledge/linguistics/numerals-and-measures.md
```

must return exactly 1.
