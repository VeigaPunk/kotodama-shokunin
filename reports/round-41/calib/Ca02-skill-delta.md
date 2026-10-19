- Seat: Ca02 | executor | Ca | date 2026-10-19 | baseline 456674d

## Draft delta — `SKILL.md`

### Before (`SKILL.md:382-398`)

```text
Worked ceiling, measured **2026-10-18T21:53:04Z** with
`python3 -B reports/round-28/ceiling/measure-ceiling.py`: reader `b5406bcd…`
over the pre-integration packet `543d68a8…` finds **19 legal / 8 illegal**
among **27** mark-axis plain words; the named institutional abstraction set
has **1 legal / 4 illegal**. `L-45 tikmes → sem.kit` is the surviving
abstraction; `L-30 gis → sig` is not legal. This supersedes the pre-fix
reader's 18/9 and 0/5 readings, without rewriting them. Test legality
**per syllable**: `all(is_legal_syllable(s) for s in syllabify(form))`.
The base-initial-coda predicate agrees on that measured population, not on
every possible language or arbitrarily shaped input. The transferable result
is the check over the **operation + base list + phonotactics + reader**, not
this fixture's ratio (`corpus/knowledge/linguistics/register-strata-attestation.md`
§13; `corpus/knowledge/linguistics/register-lexicon-ceilings.md` §§4,10;
`reports/round-28/argot/D20-ceiling-wording.md` §§3–4). Read the ceiling entry's
phrase-absence evidence with the separate qualification
`reports/round-30/fixes/x63-f2.md` §Applied amendment: that evidence correction
changes neither the measured arithmetic nor the declared ceiling.
```

### After (proposed replacement)

```text
Historical worked ceiling, measured **2026-10-18T21:53:04Z** with
`python3 -B reports/round-28/ceiling/measure-ceiling.py`: historical reader
`b5406bcd…` over the pre-integration packet `543d68a8…` finds **19 legal / 8
illegal** among **27** mark-axis plain words; the named institutional
abstraction set has **1 legal / 4 illegal**. `L-45 tikmes → sem.kit` is the
surviving abstraction; `L-30 gis → sig` is not legal. This supersedes the
pre-fix reader's 18/9 and 0/5 readings, without rewriting them. Test legality
**per syllable**: `all(is_legal_syllable(s) for s in syllabify(form))`.
The base-initial-coda predicate agrees on that measured population, not on
every possible language or arbitrarily shaped input. The transferable result
is the check over the **operation + base list + phonotactics + reader**, not
this fixture's ratio (`corpus/knowledge/linguistics/register-strata-attestation.md`
§13; `corpus/knowledge/linguistics/register-lexicon-ceilings.md` §§4,10;
`reports/round-28/argot/D20-ceiling-wording.md` §§3–4). Read the ceiling entry's
phrase-absence evidence with the separate qualification
`reports/round-30/fixes/x63-f2.md` §Applied amendment: that evidence correction
changes neither the measured arithmetic nor the declared ceiling.

**2026-10-19 supersession — current gate pin.** The measurement above is a
historical reading with reader `b5406bcd…`, not a claim about the current gate
bytes. Current `tools/gates/argot-derivation-gate.py` bytes have SHA-256
`10c884337fbb2b8f5cc64bedb70e2ddbc34b84c17aaa29fb9be15d049b324a75`
(`sha256sum tools/gates/argot-derivation-gate.py`, 2026-10-19). Any new ceiling
measurement must record that reader digest alongside its packet digest,
command, and date. This supersedes the live reader reference for new runs only;
it does not alter the historical measurement or its filed evidence.
```

## Owed

None for this seat's `SKILL.md` delta draft. No live file was edited.

## Citations

- `SKILL.md:382-398` — exact existing ceiling measurement row, its historical reader digest, method, and interpretation.
- `reports/round-41/claims.json:20-24` — Ca claim requires marking old digest readings as historical and carrying the current argot-gate digest in a dated supersession row; the filed readings are not to be rewritten.
- `sha256sum tools/gates/argot-derivation-gate.py` output — current full SHA-256: `10c884337fbb2b8f5cc64bedb70e2ddbc34b84c17aaa29fb9be15d049b324a75`.
- `Grep '8c7dd098|b5406bcd|15f8b232' SKILL.md` output — only the `b5406bcd…` hit is `SKILL.md:383`.
