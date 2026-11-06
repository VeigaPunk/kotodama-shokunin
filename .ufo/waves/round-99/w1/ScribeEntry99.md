# ScribeEntry99 — round 99 praise poetry and panegyric entry

- Seat: ScribeEntry99 (scribe, leaf; no subagent dispatch). Lane: kotodama-shokunin.
- Date: 2026-11-06. Milestone r99-v1. Axis: coverage.
- Base `527df3fee305b3454446946e6779ece45456307e`; claims frozen at
  `b1b80562edfc8f6082aec74bbbf0f25e152708a8`.
- Nothing committed, added, stashed or checked out. No model chosen. No tool
  installed or upgraded (none was needed: `python3`, `pdftotext`, `curl` already
  present; no pacman call was made).

## 1. What was written

| path | what | bytes | sha256 |
|---|---|---|---|
| `corpus/knowledge/linguistics/praise-poetry-panegyric.md` | the new knowledge entry (13 h2, 44,922 B) | 44922 | `1011940ebe519b0039b2e1018913ad7c948616e60dca5c2fd0e6d9f73a1b4842` |
| `corpus/README.md` | revision 2.25 block; `## linguistics/` 43 → 44; the entry's row in filename order between `politeness-taboo-euphemism.md` and `proverbs-riddles-attestation-solutions.md`; a `## Round 99 praise poetry and panegyric entry (2026-11-06)` section with totals 270 → 271 and footer `44/36/43/29/24/95` | — | — |
| `.ufo/waves/round-99/w1/stage/ScribeEntry99/self-check.txt` | self-check numbers with commands and rc | 2967 | — |
| `.ufo/waves/round-99/w1/stage/ScribeEntry99/DONE` | one line: the entry's sha256 (written last) | — | — |
| `.ufo/waves/round-99/w1/ScribeEntry99.md` | this report | — | — |

No other file was written. Scratch `/fast/scratch/hyaku/kotodama-r99/ScribeEntry99/`
was removed before yield.

## 2. Gates measured (command, rc, result)

| # | command | rc | result |
|---|---|---|---|
| 1 | `python3 -B /fast/scratch/hyaku/kotodama-r99/ScribeEntry99/selfcheck.py` (re-implements the frozen counter's C1/C2/C6/C7/C8 legs read-only; imports `FROZEN_TOPIC` from `reports/round-99/predispatch.py`) | 0 | see §3 |
| 2 | `python3 -B tools/check-corpus-index.py --root /home/vgpnk/Projects/shokunin/kotodama-shokunin` | 0 | `CORPUS-INDEX: OK files=271 rows=271 findings=0` |
| 3 | `python3 -B tools/check-cited-lines.py corpus/knowledge/linguistics/praise-poetry-panegyric.md` | 0 | `CITED-LINES: 0 finding(s) in 1 file(s)` |
| 4 | `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file corpus/SOURCES.md` | 0 | last line `file ok …/corpus/SOURCES.md`; `grep -c E11` = 0 (grep rc 1, no match) |
| 5 | `sha256sum corpus/knowledge/linguistics/praise-poetry-panegyric.md` | 0 | `1011940ebe519b0039b2e1018913ad7c948616e60dca5c2fd0e6d9f73a1b4842` |

## 3. Self-check output (verbatim from gate 1)

```
C1 bytes=44922 (>=12000 True)
C1 h2=13 (>=6 True)
C1 table=10x3 (rows>=5 cols>=3 True)
C1 phrases=6/6 ['praise poetry', 'praise singer', 'panegyric', 'genealogical recitation', 'praise epithet', 'praise performance'] (>=4 True)
C1 topic-line=equal
C2 rows=941 highest=S1017 new=11 qualifying=11 ['S1007', 'S1008', 'S1009', 'S1010', 'S1011', 'S1012', 'S1013', 'S1014', 'S1015', 'S1016', 'S1017']
C6 cited ids=['S1007', 'S1008', 'S1009', 'S1010', 'S1011', 'S1012', 'S1013', 'S1014', 'S1015', 'S1016', 'S1017']
C6 uncited qualifying=[]
C6 cited-not-qualifying=[]
C7 bound=11/11 failures=[]
C8 other owners=0 []
CITED-LINES rc=0 CITED-LINES: 0 finding(s) in 1 file(s)
8GRAM orality-formulaic-language.md shared=1
8GRAM toast-drinking-speech-formulae.md shared=7
8GRAM funerary-lament-dirge-formulae.md shared=1
8GRAM verbal-duelling-ritual-insult.md shared=9
INDEX rc=0 CORPUS-INDEX: OK files=271 rows=271 findings=0
```

The table shape reported is the §1 boundary table (10 rows × 3 cols); the §7
tradition table is 9 data rows × 5 columns and also clears the 5×3 floor.

## 4. Cited ids and what each supports

All eleven qualifying rows (tier A|B, `mined`, opened 2026-11-06, `used-by`
exactly `corpus/knowledge/linguistics/praise-poetry-panegyric.md`) are cited:

| id | source | cited at |
|---|---|---|
| S1007 | Finnegan, *Oral Literature in Africa* ch. 5 "Panegyric" (B) | §2 (court panegyric, praise names, subjects, validation, public reward, negative sanction), §3 (Zulu specialists, *imbongi*/*mmoki*, Hausa *maroka*, instrument rank, Mandingo freelances, gifts), §4 (praise names, *kirari*, *oriki*, epithet expansion), §5 (ancestors-first sequence, Yoruba annual recitation, pedigree claim, allusive genealogy), §6 (delivery, chant, audience, occasions, stanza order, rite of passage, performer test, recomposition), §7 (four African rows), §8 (derogatory remarks, Ngoni sarcasm, control on a ruler, Tswana composer's property) |
| S1008 | Opland, "Lord of the Singers" (A) | §3 (spontaneous praise of dignitaries; improvisation vs memorial Zulu mode), §6 (rally sequence; duty to greet with a royal praise name and the audience's repetition), §8 (praise yields to criticism, then exhortation) |
| S1009 | Barber, "Text and Performance in Africa" (A) | §2 (praise as a detachable text — "the praises of Dingaan"), §4 (obscurity as a political resource), §8 (obscurity encodes discreet criticism of royal power) |
| S1010 | Groenewald, "I Control the Idioms" (A) | §4 (renewal of formulae, new metaphors, resilience), §8 (the "curiosity" question; the genre's wide reach) |
| S1011 | Kaschula, "Mandela Comes Home" (A) | §3 (*imbongi* at the Great Place, decrying and praising, contemporary survival), §8 (licensed criticism, censorship undermining credibility) |
| S1012 | Pindar, *Extant Odes* (A) | §3 (five odes for Hieron and Theron; song-writer to all Hellenic states; refusal to be a patron's property), §7 (epinician row), §8 (praise overtaken by distaste from covetous men) |
| S1013 | *Y Gododdin*, trans. Williams (A) | §3 (praise chosen over reproach for the fallen lord), §7 (Welsh row) |
| S1014 | *Purananuru* (B) | §3 (bards moving patron to patron, gifts, counsel and embassy), §7 (Tamil row) |
| S1015 | Kertzer, "Trio Da Kali" (B) | §3 (griot function list; praise-singing the most audible manifestation) |
| S1016 | Potts, *Skaldic Poetry* (B) | §3 (money in poetry, rewards and renown, competition for favour), §7 (Norse row) |
| S1017 | Kavanagh, *Signs and Wonders* (B) | §7 (Irish limit), §8 (law-text rule against satire and over-praise; the *fili*'s economic dependence; *dúas*) |

## 5. Inference list (also §13 of the entry)

1. The four objects of praise are one act with different targets, and a tradition
   is characterised by which target it privileges.
2. The office's four questions (recruitment, licence, reward, obligation) are
   separable, and a singer missing one is a different social type.
3. The epithet's warrant is load-bearing; without it the phrase is a compliment,
   not a claim.
4. The order of a genealogical recitation is itself an argument.
5. The audience's answer is the uptake without which the speech act cannot
   succeed or fail.
6. The five limits distinguish a praise institution from a propaganda apparatus.
7. A praise that asserts nothing falsifiable cannot be tested.
8. The reward's visibility is what makes praise an economy.
9. The bearer-unit list transfers from carried marks to spoken epithets, while
   transmission does not transfer.

Two further inferences appear in the body and are not repeated in §13 because
they are single-sentence readings of cited material: that the office/incumbent
split is a resource (§2), and that the caller/checkable-order reading of the
toast rules applies to praise (§6). Both carry the *inference* tag in place.

## 6. Boundary work (adjacency)

The entry defers, without restating, to: `orality-formulaic-language.md` §3
(praise-names as formula lexicon — cited as prior art at `:60`, never
re-derived); `funerary-lament-dirge-formulae.md` §3/§6 (the keening office and
praise of the dead); `verbal-duelling-ritual-insult.md` §6/§7 (boast, taunt,
riposte, adjudication); `toast-drinking-speech-formulae.md` §5 (the three order
rules, cited and applied to a praise-specific station list, not borrowed as a
sequence); `synthesis/deity-name-derivation-pipeline.md` §4 (divine epithet
grammar routed there); `myth-symbol/sacred-kingship-mythic-charter.md` §8.5
(performed pedigree cited, charter not re-owned);
`myth-symbol/heraldry-emblems-identity-marks.md` §3 (bearer units borrowed as a
model, transmission not restated); `naming-systems.md` §2 (name slots stay
there); `polynesia-navigation.md` (branch selection cited once);
`kinship-terminology.md:153` (the Bohannan critique applied, not re-argued).
Canon is handed to lore-shokunin; research method to chousa (PROVINCE.md).

## 7. Out-of-scope items (not touched)

- `reports/round-99/claims.json`, `predispatch.py`, `battery99.py`,
  `battery99.sha256`, every control receipt and everything under
  `reports/round-99/controls/` — frozen; not read-modified, not written.
- `corpus/SOURCES.md` and `reports/round-99/evidence/` — ExecRegistry99's; read
  only (rows and manifest were read to bind the citations).
- Every other knowledge file, the grader `tools/check-advance-evidence.py`, and
  all sibling lanes — read-only or untouched.
- No commit, no `git add`, no jj command.

## 8. Findings and limits

1. **The six phrases are unowned elsewhere.** C8 over the landed tree reports
   `other owners=0`; the entry is the only topic-line or heading owner. Prose
   mentions in other files (13 occurrences in 9 files at base) were left alone.
2. **8-gram overlap is residual boilerplate.** The largest shared run with any
   neighbour is the corpus-wide metadata line
   `- source: corpus/SOURCES.md (the registry rows below, one id per line)` and
   the house section names; no sentence of prose is copied. Measured: 7 shared
   8-grams with the toast entry, 9 with verbal duelling, 1 each with orality and
   funerary.
3. **Two sources are reported at their own scope.** S1014 (*Purananuru*) and
   S1015 (Kertzer) are tier B and are used for what their captures state — the
   anthology's themes and the griot role list — not as surveys.
4. **S1012's "distaste" line is audience-side.** It is cited for the envy that
   praise provokes, not for a claim about Pindar's biography.
5. **The entry does not measure C9.** The non-author re-open is ReviewerC99's
   leg; this seat neither ran it nor claims it.
6. **The counter was not run end to end by this seat.** The C legs reported here
   are a read-only re-implementation of the frozen counter's own logic plus the
   two repository tools; the O legs belong to the operability seats and were not
   executed.
7. **No conflict arose** between the item text and the frozen counter: the C1
   floor, the phrase set, the topic string and the table shape all agree with
   `reports/round-99/predispatch.py`.
