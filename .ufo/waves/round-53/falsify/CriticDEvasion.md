# CriticDEvasion — round 53 falsify: does D's landed repair evade its counter?

- Seat: `KotodamaR53.CriticDEvasion` (critic, leaf, non-author of D's bytes).
- Item attacked: claim D, landed at `374ae5a4e4376049e45a7f597e740d09bf94cbc4`, against base `a9cf95fe47a82b516f6c2487cb76b89c3a71c493`. The file is `corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md`.
- Axis judged: depth.
- Tool installs: none.
- Lane writes: this report only. Read-only `git show`, `git diff`, `git archive` and `git log` were run in the lane. Scratch exports and fetched sources went to `/tmp/cde/` only.

## Verdict

- **No instance is reworded but still carries the same defect.** All 18 base instances were compared base line against landed line, and each landed sentence was checked against its re-opened source.
  - 17 are repaired.
  - 1 (line 176) is repaired but lost one statement its source carries: the Collins sense, quoted below.
- **No fragment was dropped without support.**
- **No landed sentence states something its cited page does not carry without a `(to-verify)` mark.**
- **D's falsifier does not trip:** OPEN 0, SID_BAD 0, highest cited S-id S184, no S187 or above.
- **Depth is improved overall, with one small loss on line 176.** The loss was forced by counter leg OVER6, which was built on a wrong premise.
- **The counter cannot see rewordings** (finding F4). D's truth therefore rests on review like this one, not on the counter, as the claim's `method_not_statement` already says.

## Commands and outputs

```
$ cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 -B reports/round-53/d-count.py
OPEN 0
SID_BAD 0 [] cited 50
exit 0

$ git archive a9cf95fe47a82b516f6c2487cb76b89c3a71c493 | tar -x -C /tmp/cde/basetree
$ python3 -B reports/round-53/clauses.py --base-tree /tmp/cde/basetree
C1 PASS added=['corpus/knowledge/linguistics/gesture-co-speech-pointing.md'] removed=[]
C2 PASS topic_chars=375
C3 PASS draft_tokens=[]
D1 PASS lines=196 base=196
D2 PASS lost=[]
exit 0
```

**Instance list.** `reports/round-53/telemetry/declaration-dry-run.txt` gives 18 instances.
- Fragments (FRAG): 106, 107, 113, 174, 177 three times, 179, 181 twice.
- Wrong rows: WROW1 at line 106, WROW2 at line 113.
- Over-reads: OVER1 and OVER2 at line 54, OVER3 at 76, OVER4 at 79, OVER5 at 121, OVER6 at 176.

The file is untracked at the base, so `git show a9cf95f:<it>` fails. The working-tree copy was used.

**Base and landed lines.** Both were taken with `git show <rev>:<entry>` and compared line by line. Line numbering is unchanged (196 lines both sides).

**Draft-id mapping.** Taken from `.ufo/waves/round-53/build/ScribeDFragments.md` §4. It agrees with `corpus/lessons/round-52-verifier-spotcheck.md`: `S162, S159, S174, S175, S176, S157, S180`.

### Sources re-opened (plain `curl`, 2026-10-22, ordinary means only)

| Row | Route and result |
|---|---|
| S135 | PDF, HTTP 200 |
| S139 | PMC, 200 |
| S141 | PDF, 200 |
| S147 | PDF, 200 |
| S151 | MPI archive, 200 |
| S152 | archive.org `633751_djvu.txt`, 200 |
| S160 | sibetrans, 200 |
| S162 | PDF, 200 |
| S163 | live, 200, no challenge; also Wayback `20260312095851` |
| S165 | Brown, 200 |
| S174 | NSF PDF, 200 |
| S180 | CNRS, 200 |
| S181 | dictionary.com, 200 |
| S157 | Wayback `20260204053249` |
| S159 | Wayback `20210519200637id_` .doc, converted with `soffice` |
| S166 | Wayback `20260311033125` |
| S182 | Wayback `20110131180047` |
| S183 | Wayback `20241223205906` |
| S140 | live: Anubis bot challenge met, not passed; read via Wayback `20260921032409` |

## Per-instance judgment (base line → landed line)

Every quote below was found verbatim in the fetched text.

| # | Instance | Judgment | Evidence |
|---|---|---|---|
| 1 | OVER1 line 54, "two tones (Suruí) force fixed formulas" | repaired | Landed text quotes S135 verbatim. S135 printed p. 7: "in tonal languages with low informational load on spoken pitch, whistled sentences are more formulaic and therefore more predictable". "trained listener" and "tone load" paraphrase S135: "the possibility of transmitting complex sentences to a trained listener depends on the informational load carried by pitch prosody". |
| 2 | OVER2 line 54, Hmong "(Laos, Thailand, United States) (S135)" | repaired (deleted; unsupported for whistled Hmong) | S135 has no "Laos". The country list survives on line 58 under S141, which names all three ("In current times, in Laos … Thailand … United States", S141 ¶[19]). The deletion also took the Chinantec half of the reach cell, which S135 does carry (F5). |
| 3 | OVER3 line 76, /b/ merging with /k/ | repaired | S147 printed p. 839: "The occlusive [p] is expressed mainly with this process and is therefore very similar to [k] in whistles". Landed: the occlusive /p/ whistled "very similar to [k]". |
| 4 | OVER4 line 79, "learned young" | repaired | S151 deposit title: "David Yetman and Mark Sicoli elicit spoken and whistled Chinantec from children in San Pedro Sochiápam". Age is marked `(to-verify)`. |
| 5 | FRAG line 106, `, -6` | repaired, to S162 | The draft id maps to S162. S162 p. 151: "(working their farms, hunting, or gathering)". |
| 6 | FRAG line 107, `, -6` | repaired, to S162 | S162 §2.1.2: "when someone gets lost in the bush". S160 carries "the organization of assistance after a hunting accident". |
| 7 | FRAG line 113, `, -4` | repaired, to S159 | S159 "2. Need for urgent safeguarding": "One of the most important threats to this element is the increase in the use of mobile phones." and "it is about to lose its communication function". |
| 8 | OVER5 line 121, "in Akan (Ghana) practice" | repaired | S165: "by seventeen he was appointed Royal Court Drummer to the high chief of the Aburi-Akuapim region". S166 abstract: "who fiercely resist change in repertoire and performance practice yet accept it in the realm of performance context". Both are verbatim, and the claim is narrowed to one biography. |
| 9 | FRAG line 174, `, -5` | repaired, to S174 | S174 §4: "Speech surrogates are found all around the world on a wide variety of instruments", naming Yorùbá, Ewe, Sabar and Bora. The base's "small set" is contradicted by that sentence and was removed. "most tonal languages have none" had no carrying row and is now `(to-verify)`: honest, not lost support. |
| 10 | OVER6 line 176, "primitive peoples" | repaired, but supported content lost | See F1. The base's unrouted over-read "used in 1958 for a relay of human runners (S182)" was also removed. That is correct: S182 has no "runner". |
| 11–13 | FRAG line 177, `, -5`, `, -6`, `, -7` | repaired, but re-sourced off the declared mapping (F3) | Mapped rows were S174, S176 and S175. Landed cites S139 and S152 instead, and S152 carries the new wording verbatim (ch. 17): "the very extra length of the drum stereotypes or holophrases leads to greater identifiability in rhythmic and tonal patterning". S175 and S176 stay cited on line 172, so no registry orphan results. |
| 14 | FRAG line 179, `, -12` | dropped; support intact | Mapped row S180 is not on line 179, so the drop departs from the declared method (F3). S183 carries every detail: "Meeting 12.COM (Jeju Island, 2017)", the Urgent Safeguarding List, and "in the context of parent-child relations". |
| 15 | FRAG line 181, `, -2` | repaired, to S157 | S157 (Wayback): "replicates the islanders' habitual language (Castilian Spanish) with whistling". |
| 16 | FRAG line 181, `, -12` | repaired, to S180 | S180: "we listed more than 70 of them", one counting standard next to S173's. |
| 17 | WROW1 line 106 | repaired | As in row 5. |
| 18 | WROW2 line 113 | repaired; the routed premise is partly wrong | See F2. S159 alone carries the line as written, so nothing was lost. |

Line 58 is not one of the 18 but was rewritten by D, so it was checked too. It is supported:
- S141 ¶[15]: "Consonants, however, cannot be pronounced by the qeej".
- S140 §3.5, read via Wayback after the live page served an Anubis challenge (met, not passed): "Catlin (1982) argues that this obscures direct tone-note correspondences to the extent that the qeej should be considered an encoding rather than abridging phonemic system".
- Same section: "This funeral repertoire is fixed and learned by rote".

Line 105 (S163 moved there) is verbatim on S163: "required the local population to find an alternative way to communicate across long distances".

## Findings

### F1 — medium (depth): line 176 dropped a sense its source carries, because counter leg OVER6 forced it

**What the text says.** Landed line 176 keeps only the American sense: "whose dictionary sense speaks of 'the natives of a jungle or bush region'…" (S181). The base's "primitive peoples" sub-quote is gone.

**What the source says.** S181 (https://www.dictionary.com/browse/bush-telegraph, British sense, credited on the page to Collins English Dictionary) reads: "a means of communication between primitive peoples over large areas, as by drum beats". The `corpus/SOURCES.md` row S181 already quotes it.

**Why it matters.**
- The round-52 closure's line "the sub-quote 'primitive peoples' is not on S181's page" (`corpus/lessons/round-52-verifier-spotcheck.md`, over-read list) does not reproduce.
- `d-count.py` OVER6 counts the bare string. So the leg certified the removal of a supported quote as a repair.
- The line's R verdict ("is a neutral technical name": rejected) now rests on the weaker of the two senses on the page. Some depth is lost, but nothing false was added.

**Fix (next round; the round-53 counter stays frozen).** Paste-ready line 176:

```
| 'Jungle telegraph' / 'bush telegraph' is a neutral technical name | R | it is an English idiom, "First recorded in 1875–80"; its American sense speaks of "the natives of a jungle or bush region" sending news "by runners, drum codes, or smoke signals", and its British (Collins) sense of "a means of communication between primitive peoples over large areas, as by drum beats" (S181); a 1958 TIME report says a medical team "got native chieftains to pass the word by jungle telegraph" (S182) — name the community's own system instead |
```

Also append an erratum to `corpus/lessons/round-52-verifier-spotcheck.md`, without rewriting its text: the string is on S181's page under the Collins sense. Any later counter must flag "primitive peoples" only on a line that does not attribute it to Collins. It must not flag the bare string.

### F2 — low (gate premise): S163 does carry the mobile-phone threat

**What the routing says.**
- The round-52 closure: "On line 113 the mobile-phone decline is in S159, not S163".
- `.ufo/waves/round-53/build/ReviewDWrongRows.md:36`: "The strings 'mobile' and 'phone' occur nowhere on the page."

**What the source says.** S163 (https://ich.unesco.org/en/USL/whistled-language-00658), summary paragraph: "One of the key threats to the practice is the use of mobile phones." The sentence is on the live page (HTTP 200, no captcha) and on Wayback capture `20260312095851`.

**Impact.** No content was lost. Landed line 113 cites S159, which carries the fact more strongly. But WROW2's "still cites S163" clause would count a supported co-citation as a defect.

**Fix.** No entry change is needed. Record in the round-53 closure or lesson that S163 also carries the threat, so later rounds do not repeat the premise. A future counter should not forbid S163 on that line.

### F3 — low (provenance): the 177 and 179 fragments did not follow the declared method

**What was declared.**
- The claim's `method_not_statement`: "Each fragment is replaced by the registered S-id its round-52 seat draft-id maps to … or dropped where the S-id is already on the line".
- The commit message: "10 draft-id fragments mapped to registered rows".

**What landed.**
- Line 177's three draft ids map to S174, S176 and S175 (ScribeDFragments §4). Landed cites S179, S139 and S152 instead.
- Line 179's `-12` maps to S180, which is not on that line. It was dropped.

Content is fully supported in both cases (rows 11–14 above), so D's falsifier does not trip.

**Fix.** Add one sentence to the round-53 lesson or closure: "Line 177 was re-sourced to S139 and S152, which carry the reworded text, instead of the mapped S174, S176 and S175; line 179's S180 was dropped as redundant with S183, which carries the 2017 inscription and the parent-child transmission."

### F4 — low (gate): `d-count.py` passes reworded over-reads (demonstrated)

**Setup.** On an export of `374ae5a` in `/tmp/cde/mut` (outside the lane), three over-reads were reintroduced in new words:
- line 79: "so the register is learned in childhood";
- line 54: "two tones (Suruí) compel set formulas";
- line 121: "in Akan court practice".

**Result.**

```
$ python3 -B reports/round-53/d-count.py --root /tmp/cde/mut
OPEN 0
SID_BAD 0 [] cited 50
exit 0
```

**Meaning.** The counter's docstring and the claim's method both disclose this limit, so this is not a sizing defect in D. It does mean D's after-value proves absence of wording, not truth. The per-instance review above is what carries truth here, and it found no reworded over-read.

**Fix.** No test is weakened. Later repair counters should add a quote-presence leg: every quoted string on a changed line must occur in a committed text copy of its cited source.

### F5 — low (depth): line 54 dropped the Chinantec half of the reach cell

**What the source says.** S135 p. 7: "high levels of intelligibility can be reached in unpredictable sentences in tonal languages with rich tonal systems for lexical load, such as Chinantec".

**Impact.** Line 79 still states it ("a rich tone system carries unpredictable sentences (S135)"), so the entry as a whole loses nothing.

**Fix (optional).** Append to the line-54 reach cell, before "(S135)": `, while "high levels of intelligibility can be reached in unpredictable sentences" in a rich tone system such as Chinantec's`.

### F6 — low (registry, outside D's land): S182's `teaches` cell keeps the "runners" over-read that D removed from the entry

**What the row says.** S182 `teaches`: "in 1958 press use the phrase named a relay of human runners in the Congo, not a drum code".

**What the source says.** The TIME page has no "runner". It says: "Working both sides of the stream, they got native chieftains to pass the word by jungle telegraph" (¶ beginning "Working both sides of the stream").

**Fix.** Set the cell to: `in 1958 press use a medical team "got native chieftains to pass the word by jungle telegraph" on the Ruzizi River (Ruanda–Congo boundary); the page does not say what the relay used`.

### F7 — low (access record): S140's route is not in its row

**What happened.** The live S140 page served an Anubis challenge to a plain curl, which was met and not passed. Wayback capture `20260921032409` carries both line-58 statements verbatim.

**Fix.** Add to the S140 anchor cell: `live page served an Anubis challenge on 2026-10-22, not passed; read via Wayback 20260921032409`.

### Residual wording on D's lines (pre-existing, unrouted, not D regressions)

- **Line 113.** "built for the ravine it dies when the settlement concentrates" is illustrated by a mobile-phone threat. S159 states the settlement mechanism separately: "Socio-economic factors are also behind the acceleration in rural-urban migration." Optional fix: cite that sentence for the concentration clause.
- **Line 79.** "whistles stay short" is a paraphrase. S135 says "whistled sentences tend to be simple with single-clause utterances and equally simple conversational repairs". Optional fix: write "whistles stay single-clause".

## Not checked

- The full text of S166 (restricted; the row covers the abstract only).
- Carrington 1949 behind S152.
- Line-by-line review of D's untouched lines, which is outside this item.
