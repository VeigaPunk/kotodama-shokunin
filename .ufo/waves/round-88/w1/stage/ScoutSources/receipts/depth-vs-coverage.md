# Depth-not-coverage assessment and duplication check for the proposed section 4b

Question this seat was asked: does the proposed new notation section duplicate what the
corpus already knows, and is the work depth (thicker analysis of a held topic) rather than
coverage (a new topic)?

## 1. What the numerals entry already holds

`corpus/knowledge/linguistics/numerals-and-measures.md` (34,831 bytes at base) has 15 sections.
Its own `## 13. Handoff notes and open items` states the gap this round fills:

> (2) no entry yet exists for numeral *notation* as a writing subsystem (Chrisomalis-grade detail)
> - if the corpus wants it, it belongs beside `writing-systems.md`

The only place notation is currently touched is `numerals-and-measures.md:111`, one clause:

> cumulative tallies, ciphered signs (Greek alphabetic numerals, Roman), and positional notation
> with a zero (Babylonian place value; the Indian decimal positional system) are typological stages
> (Chrisomalis 2010)

Two facts follow. (a) The corpus holds a three-item list of notation kinds, with no axes, no
classification rule, no trade-offs, and no S-id anywhere in the file (`git show <base>:... |
grep -oE "\bS[0-9]{3}\b"` returns nothing). (b) That clause calls the three kinds "typological
stages" - precisely the teleological reading that S931 para 10 rejects: "This avoids the
teleological argument of Ifrah (1987) and Dehaene (1997)" and "it is evident that there is no perfect
system". So the new section does not repeat the corpus; it **corrects an existing corpus
statement** that currently mis-frames notation as a progression toward a perfect system.

## 2. Adjacent corpus files: is the same ground already covered?

| file | what it already says | overlap verdict |
|---|---|---|
| `corpus/knowledge/linguistics/writing-systems.md:21` | semasiography row lists "math notation" among non-writing semiotic systems | different owner: scripts and writing, not numeral-notation typology. The D claim's bounds already say the new section does not supersede writing-systems.md |
| `corpus/knowledge/linguistics/writing-systems.md:146` | "Missing plumbing: numerals (Brahmi->Hindu-Arabic via 9th-c. Baghdad; Roman numerals paired with the abacus; Maya vigesimal zero; Chinese rod numerals)" | names numerals as missing plumbing; a claim about corpus coverage, not a notation typology |
| `corpus/knowledge/myth-symbol/number-symbolism.md:100` | "| 60 | Sumerian/Babylonian | ... positional sexagesimal notation (Chrisomalis 2010); the 12-phalanges x 5-finger counting hypothesis ... is plausible but not proven" | number *meaning* and base symbolism; the myth-symbol file owns meaning, not notation structure |
| `corpus/knowledge/myth-symbol/number-symbolism.md:142` | "notation strata (tally -> positional notation, Chrisomalis 2010) as era markers" | era-marking use of strata, again a different question |
| `corpus/knowledge/linguistics/numerals-and-measures.md:135` | calendar/sexagesimal coupling | base-and-culture coupling, not notation typology |

No corpus file states a two-axis typology of numerical notations, a five-type classification, or the
trade-offs among the types. The proposed section is the first coverage of that ground, so the work
is both coverage (a genuinely new sub-field: notation as a writing subsystem) and depth (a
classification rule with axes and trade-offs applied to a field the corpus had only listed).

## 3. Depth axis - what the new material adds that the held entry lacks

| held | new |
|---|---|
| three notation kinds named in passing | a five-type classification with the six-to-five exclusion argument |
| no axes | two axes: how signs are formed and combined within any power of the base (intraexponential), and how the different powers are combined (interexponential) |
| no decision rule | the two questions that classify any notation |
| "typological stages" (teleological) | "no perfect system" (non-teleological), with the compactness-vs-inventory trade-off made explicit |
| Babylon/Egypt/India mentioned only as base or calendar facts | Babylon and Egypt classified as *types* with the mechanics of each (unit+ten signs within a power; position across powers) |

## 4. Wording hazard for the section author (source-faithfulness)

The dispatch prompt asks for "five types from coefficient vs power axes". That phrasing is not
Chrisomalis's. The paper's own words (para 7) are "How are the signs formed and combined within any
power of the base?" and "How are the different powers are combined together to take a total of a
numeral-phrase?", and para 8 names the two principles "intraexponential and interexponential".
A section that labels the axes "coefficient vs power" would be a paraphrase presented as the
source's terms, and the source's actual terms are the quoted ones. Use the quoted terms; keep the
axes descriptive in the writer's own words only if marked as paraphrase.

## 5. The five types, as the paper names them (for the table author)

| type | the paper's own example (para 9) |
|---|---|
| cumulative-additive | Greek acrophonic numerals (fig. 2), and early hieroglyphic numerals of predynastic Egypt (para 19) |
| cumulative-positional | Babylonian sexagesimal (base 60) numerals (fig. 3) |
| ciphered-additive | Georgian alphabetic numerals (fig. 4) |
| ciphered-positional | Lao numerals, "or for that matter like Western numerals" (fig. 5) |
| multiplicative-additive | classical Chinese numerals (fig. 6) |

The sixth, multiplicative-positional, is logically excluded (para 9). The trade-off paragraph is
para 10: ciphered-additive is the most compact; cumulative-positional uses "a much smaller inventory
of signs than other systems (often as few as two or three), but are far less compact". Para 25 adds
that cumulative-positional is "the rarest of the five types" and that the structure is "excellent for
manipulating numbers" but "among the least concise ways to write a number".
