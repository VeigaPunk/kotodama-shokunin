# CriticC99 — claim C (coverage) attack, round 99 w1

Stage detail: `.ufo/waves/round-99/w1/stage/CriticC99/critic.md` (sha256 in `DONE`).

## Verdict

**Claim C survives its frozen predicate — no leg C1–C9 falsified.** C legs measured 9/9 PASS on the landed tree with a byte-for-byte replica of the frozen C-leg code (`clegs.py`, rc 0): C1 bytes=44922 h2=13 table=10x3 phrases=6/6 topic equal; C2 rows=941 highest=S1017 qualifying=11; C3 added=11 removed=0 illegal=0; C4 census rc 0; C5 index rc 0 files=271 rows=271; C6 11/11 cited; C7 11/11 bound, 20 captures sha-verified; C8 271 files, 0 other owners; C9 11 ids re-opened count 1. The frozen counter itself (`predispatch.py`) reached O5 PASS and was still inside the O6 mutation leg when this report was written; the C legs are downstream of it and were measured by the replica.

**Content quality is not clean.** Two defects the predicate cannot see, one boundary gap:

1. `corpus/knowledge/linguistics/praise-poetry-panegyric.md:179` — §7 Yoruba limit cell, "titles are public property, so any drummer who knows them can assemble the praise", is in **no capture** (`public property` 0 in S1007 and S1009; `any drummer` 0; `knows them` 0). The table caption (`:174`) presents cells as recorded cases, so this breaks the entry's own grading rule (`:42`).
2. `:154` — "At a contemporary Xhosa **rally** … (S1008)". S1008's performance is a university lecture hall at a conference, not a rally; word-bounded `rally` in S1008 = 0 (the single bare hit is inside "o**rally**"). The sequence is supported; the setting word is not.
3. Boundary gap — `civilizations/yoruba.md:78-92` (oríkì economy) and `civilizations/germanic-norse.md:72-90` (skaldic economy) are never cited, yet the entry's §7 restates both cases. Mande (`:86`→`mali-songhai.md:53`) and Parthia (`:89`→`parthia.md:183`) are correctly deferred, so the asymmetry is the defect.

## Answers to the five assigned questions

1. **Unowned at base?** Only by the six frozen phrases. C8 (`sweep_owners`, topic lines + headings only) is 0 at base (270 files) and 0 at land (271 files), re-run with the counter's own functions. But the base teaches praise poetry as an institution in five h2 sections — `orality-formulaic-language.md:56` (§3) with the thesis bullet at `:60` ("the epithet system promoted to a social institution"), `yoruba.md:78`, `mali-songhai.md:50`, `parthia.md:165`, `zimbabwe-shona.md:87` — plus `sacred-kingship-mythic-charter.md:150` ("with the reciter as an office"). The claim's "mentioned only in prose of 12 files" understates this. On the written evidence the entry is an **expansion**, not a duplicate: it cites orality `:60` as prior art and defers eight further corpus owners with line locators (all 16 line references checked, all correct).
2. **Overlap (8-word, case-folded).** 19 adjacent owners: verbal-duelling 9, toast 7, polynesia 3, heraldry 2, orality 1, funerary 1, the other 13 zero. Top three spans: `source corpus sources md the registry rows below` (boilerplate), `linguistics verbal duelling ritual insult md the boast taunt and` (a cross-ref path), `a shorter performance is not automatically a corrupted longer one` (substantive, and attributed at `:133` to `polynesia-navigation.md:146`). No silent duplication at 8 words.
3. **Recount.** 11/11 quotes count 1 in the named capture, 11/11 inside the anchor cell, manifest ids == entry ids == rows.md ids, census rc 0, index rc 0, SOURCES diff +11/−0.
4. **Citation audit.** 32 cited sentences checked against captures; 30 supported verbatim or near-verbatim (spans tabulated in the stage file); the two exceptions are items 1–2 above. Design/inference material is correctly tagged; no other hedge reported as fact.
5. **Verdict.** Survives; no leg falsified.

## Smallest safe corrections (not applied — no lane writes by this seat)

1. `:154` — "At a contemporary Xhosa rally" → "At a contemporary Xhosa conference performance" (keep `(S1008)`).
2. `:179` — replace the unsourced limit cell with "praise may recall danger or contested reputation rather than flattery (`civilizations/yoruba.md:83`)" — supported verbatim by `yoruba.md:83` and it closes the Yoruba boundary gap in one edit.
3. `:184`/§1 table — add `civilizations/germanic-norse.md:72-90` as a boundary row (meter and economy stay there).
4. Claim text only: "mentioned only in prose of 12 files" → "…in prose of 12 files, five of which carry an h2 section on a praise institution".

Item 2 buys the most: it is the only unsourced factual claim in the entry and it also fixes the largest boundary gap.

## Files written

- `.ufo/waves/round-99/w1/stage/CriticC99/critic.md` (full report, commands with rc)
- `.ufo/waves/round-99/w1/stage/CriticC99/DONE` (sha256 of critic.md)
- `.ufo/waves/round-99/w1/CriticC99.md` (this file)

No lane file edited; no commit; no tool installed; scratch `/fast/scratch/hyaku/kotodama-r99/CriticC99/` removed.
