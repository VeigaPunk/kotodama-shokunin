# CriticC97 — attack on claim C (verbal duelling and ritual insult), r97 w1

Base 1ffc5a83d2c70e3bc581594efbcf32c562ba2569. Landed entry corpus/knowledge/linguistics/verbal-duelling-ritual-insult.md (37387 B, 6389 tokens). No lane file was edited. Supporting outputs are in this stage dir (sweep-base.txt, sweep-work.txt, overlap.txt, counter.txt, verify-c2.txt, sample*.txt, census-final.txt and the scripts used).

## Verdict

**Claim C survives the frozen predicate.** The frozen counter returns C1 through C8 PASS on the landed tree (counter.txt; command in §A.1). No frozen C-leg is falsified.

The predicate does not measure what claim C says it measures in one respect: the sourced statements. I falsify three sourced or adjacency sub-claims below. They are not frozen legs and are not in the counter's kill rule. The L1 should treat F1–F4 as defects to record and repair before scoring, not as a C-leg failure.

## A. Commands and rc

A.1 Frozen counter (read-only, work dir in scratch): `python3 -B reports/round-97/predispatch.py --root <lane> --work <scratch>/counter --base-rev 1ffc5a83d2c70e3bc581594efbcf32c562ba2569` → rc 1. Legs: O0 PASS, O1 PASS 155/155, O2 PASS (survivors=0 unnamed=0 refused=31), **O3 FAIL** ("sha pin missing or malformed: reports/round-97/controls/mutants97.sha256", not yet landed; outside claim C), O4 PASS 34/34, **C1 PASS** (bytes=37387 h2=13 table=7x6 phrases=6/6 topic-line=equal), **C2 PASS** (rows=917 highest=S993 new=9 qualifying=8), **C3 PASS** (added=9 removed=0), **C4 PASS** (census rc=0), **C5 PASS** (CORPUS-INDEX OK files=269), **C6 PASS** (8/8 cited), **C7 PASS** (8/8 captures), **C8 PASS** (files scanned=269 other owners=0). Summary: PREDISPATCH-97 FAIL legs=12/13. Claim C legs: 8/8.

A.2 Base C8 re-run (my own replication, git show of base): `python3 -B sweep.py base` → rc 0. 268 base knowledge files; surface (`- topic:` or heading) owners = 0; mentions = 3 (orality-formulaic-language.md:112, myth-symbol/trickster.md:25, :62, all prose or table cells). Matches sweep-control.txt R97-BASE owners=0.

A.3 Landed sweep with the entry included: `python3 -B sweep.py work <lane>` → rc 1, only because it counts the entry's own H1 (the frozen counter excludes ENTRY_REL). Other owners = 0.

A.4 Census: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file corpus/SOURCES.md` → rc 0; E-code lines 0; W-code lines 35 (warnings; not claim-C legs). Index: `python3 -B tools/check-corpus-index.py --root <lane>` → rc 0, `CORPUS-INDEX: OK files=269 rows=269 findings=0`.

A.5 Registry: base 908 rows, highest S984; landed 917 rows, highest S993. New ids S985–S993 (9). Entry cites S985–S992 (8). rows.md ids = S985–S993. S993 is the Threnoi row (used-by funerary-lament, outside claim C counts; the frozen counter excludes it, so C2 qualifying=8).

A.6 Located-quote recount, manifest vs captures: for S985–S992 the manifest quote_count is 1 and a fresh recount of `bytes.count(quote)` on the recorded capture is 1 for each (S985 91127 B, S986 S986.txt 844105 B, S987 S987.html, S988–S992 text captures). rc 0.

A.7 Access date: all eight manifest rows carry access 2026-11-05 (manifest.json). Tier A or B for all eight; status mined; used-by exactly the entry path (verified by the parsed rows, rc 0).

## B. Step 1 — is the surface unowned at base by content?

Yes. No base file has a topic line or heading carrying any frozen phrase (A.2 owners=0). Base hits are substantive but are sections of other owners, not contest-grammar sections:

| base file:line | what it teaches | relation to the new entry |
|---|---|---|
| linguistics/orality-formulaic-language.md:112 | §8 item 10, performer licensing: "competitive forms (Scottish flyting; Lokasenna-style senna)" | mention inside a checklist; the new entry treats the forms as contest genres (expansion, as the entry's own §1 says) |
| myth-symbol/trickster.md:25, :35, :62, :69 | Loki table row "flyting at Ægir's feast"; genre slot "Lokasenna belongs to the senna"; spectrum "pure flyting clown"; pragmatics of indirection incl. "the dozens" (Gates 1988) | figure-level owner; the entry defers the figure and cites the dozens only as a contest genre |
| civilizations/arabia-pre-islamic.md:69, :71, :74 | qaṣīdah mode table: Fakhr (boast) and Hijāʾ (invective) rows; "do not turn every insult into an ethnographic fact" | **closest substantive neighbour**: the mode table already teaches boast and invective as qaṣīdah modes. The entry's §3 Arabic naqāʾid paragraph (S992) overlaps this domain without citing the arabia row; it is expansion on the contest side, but a reader gets two accounts of Arabic invective with no stated boundary. Not a duplicate of the table. |
| linguistics/oath-blessing-curse-formulae.md:59, :84, :120 | slot grammar; S979 "seven requirements which compose any satire" | the entry defers satire-as-curse to this file (correct); see F4 for copied prose |
| myth-symbol/binding-speech-complex.md:80 | Norse níð and blessan as opposed formulas | machinery owner; entry defers (correct) |

Verdict on step 1: the new entry is an expansion of an unowned topic, not a duplicate authority on contest grammar. The only duplicate authority is the copied canon-boundary prose (F4).

## C. Step 2 — overlap (word-level, case-folded 8-grams; overlap.py; overlap.txt)

Entry: 6389 tokens, 6382 8-grams, 6325 distinct.

| adjacent owner (base copy) | owner 8-grams (distinct) | shared distinct 8-grams | shared multiset count | top spans (token length) |
|---|---|---|---|---|
| linguistics/oath-blessing-curse-formulae.md | 5041 (4927) | **294** | 294 | 44 "for an invented people it asserts nothing about canon no world no people no doctrine and no law is decided here design not sourced everything invented in this entry is marked non canon where it appears every design statement is marked design not sourced"; 43 "may be used by a fictional people is a decision for a canon layer and where rights are involved for a rights process this entry records design surfaces only design not sourced handoff to the lore world bible this entry hands the fictional"; 33 "design not sourced calibration where a source reports a practice in one tradition this entry records it as a report about that tradition and as a design option for a fictional one the" |
| linguistics/greeting-leave-taking-formulae.md | 3409 (3336) | 7 | 7 | 14 "may be used by a fictional people is a decision for a canon layer" |
| linguistics/orality-formulaic-language.md | 3619 (3618) | 0 | 0 | none |
| linguistics/politeness-taboo-euphemism.md | 3378 (3376) | 0 | 0 | none |
| linguistics/secret-and-ludic-languages.md | 3230 (3185) | 0 | 0 | none |
| myth-symbol/binding-speech-complex.md | 11673 (11613) | 0 | 0 | none |
| myth-symbol/trickster.md | 3316 (3312) | 0 | 0 | none |
| civilizations/arabia-pre-islamic.md | 4415 (4373) | 0 | 0 | none |
| culture-material/games-play-sport-contests.md | 2134 (2134) | 0 | 0 | none |

Oath overlap is 294 / 6325 = 4.6% of the entry's distinct 8-grams; the three top spans together cover 120 of 6389 tokens (1.9%). They are verbatim adaptations of the oath entry's own scope paragraph (oath :35/:37), calibration paragraph (:225), "No canon, no rights ruling" (:227) and handoff paragraph (:229). The shared material is boundary and handoff prose, not contest content. The frozen C8 leg cannot see it because it scans topic lines and headings only.

## D. Step 3 — row recount

Done in A.5 and A.6. Quote recount is 8/8 at count 1. rows.md ids equal the entry-cited ids (S985–S992) plus the Threnoi S993 row, which the entry does not cite and which claim C does not count.

## E. Step 4 — claims without cited source and sampling

Sampling: 35 checks (sample.txt, sample2.txt, sample3.txt, sample4.txt; `python3 -B` inline scripts, rc 0). Each check is a substring count on the cited capture.

Located quotes that support their sentences (count 1 unless stated): S985 definition "a genre of argumentative language that entails exchanges between two persons, parties" ✓; S985 "challenge each other to a performative display of verbal skillfulness in front of" ✓; S985 width "Verbal duels can be highly structured or more free-flowing; some traditions use rhymes," ✓; S985 catharsis ✓; S985 critique "it is important to avoid conflating verbal duels with" + "ritual insults, since these are substantially different, albeit overlapping, genres." ✓; S985 audience ✓ ×2; S985 "theme usually proposed by the audience" ✓ (the capture says "exchanging octets ... on a theme usually proposed by the audience"; the entry paraphrases octets as stanzas, acceptable). S986 "The song duels are juridical instruments insofar as they do serve" ✓; "The occurrence of the song-duel complex all down the west coast" ✓; "Among the East Greenlanders song duels may be carried on for" ✓; "laid to rest" ✓; "Stealth, cunning, and ambush are not part of such" (the entry's "stealth and ambush excluded") ✓; "as a sort of sporting performance before the assembled community" (entry: "public sporting performance", unquoted paraphrase) ~. S987 "The exchange or contest of insults was dear to the" ✓; "Then Loki went into the hall, ..." ✓; Othin orders "Find a seat at our feast" and Vithar pours drink, so "is given one" ✓. S988 "The flyting was a verbal competition ..." ✓; "all sorts on each other, some of it quite gross." ✓; "It was presumably, at least in part, a literary game." ✓. S989 "the Scottish genre of flyting, whose main" + "purpose was to humiliate the opponent" ✓. S990 "the Consistory, and thus the first proper championship of bertsolaris arose, with its rules, judges" ✓ (capture: "judges’ panel, and prizes"); "championships, when the judges announced their verdict, choosing Xalbador to participate in the" ✓. S991 "joust between two poets with an overseeing judge or emcee-adjudicator that evolved in part from the duplo" ✓; "Balagtasan is an indigenous form of competitive Filipino debate poetry in the Tagalog language" ✓. S992 "Soon these 'Flytings' (_Naqá’iḍ_) were recited" + "everywhere, and each poet had thousands of enthusiastic partisans who" ✓.

**Falsified or unsupported statements (the sampling finds these):**

- **F1 (quote discipline, S986 §5).** The entry writes: the account records that a contestant receives a "judgement" in his favour. The capture has no such token (`S986.txt` count of "judgement" = 0). The source reads `judg- [page break] … mcnt” in his favor` (raw bytes at index ~228127: "receives a "judg- ... mcnt” in his favor."). The quoted word is a reconstruction across a page-break hyphen, not an exact substring. The substance is supported (the complaint "laid to rest", count 1), but the quote is not located. Severity: low-medium (evidence discipline).

- **F2 (unsourced claim marked as design, contradicted by the cited source, S985; entry §4 "The rule that keeps an insult licensed…").** The entry states, "in the tradition this entry opens, the insult is bound to a ritual and therefore has no single author to blame for it, and the person insulted is required to sit still rather than answer, because answering would confirm the charge (design, not sourced)." The tradition is not named, no S-id is cited, and it is labelled design. S985 (captured) says the opposite for the haló: "In the haló the offended party is expected to answer—even with physical violence (Avorgbedor 1994)." S985 also says for the ashik case "an angry poet would literally be seen as the cause of the offense, not the victim of it" (so the poet is the cause, not "no single author to blame"). `liabil` count in S985 = 0. Severity: medium (a source-contradicted claim, mislabelled).

- **F3 (neighbour misstatement, entry §6 "The boast formula").** The entry says the boast grammar has four slots, "performative framing, assertion, warrant and consequence … the same four slots the corpus already teaches for the binding utterance". The corpus does not teach that set. oath-blessing-curse-formulae.md:59 names "the performative verb, the witness invocation, the assertion, the sanction clause and the uptake" (five). Its build procedure (line 200) lists six slots ("performative verb, witness invocation, assertion, sanction clause, self-imprecation, uptake"), and its calibration (line 225) names "the six-slot grammar of §8". binding-speech-complex.md teaches invocation/assertion/self-imprecation/uptake. None of the entry's four names matches those lists, and "warrant" is not a slot in either. Severity: medium (false statement about a neighbour's authority, on the adjacency axis).

- **F4 (duplicate authority, adjacency; C8 blind).** The entry's canon-boundary and calibration paragraphs (§1 scope; §12 "Calibration"; §12 "No canon, no rights ruling"; §12 "Handoff to the lore world bible"; the NON-CANON line) are near-verbatim adaptations of oath-blessing-curse-formulae.md (lines 35, 37, 225, 227, 229). 294 shared 8-grams, top span 44 tokens. The base had no duplicate contest authority; the duplicate is now the boundary prose. This is harm on the adjacency axis that the frozen counter does not measure. Severity: medium.

Minor, not separately falsified: S987 "not invited" is unsourced (`invit` count 0 in S987.html; the poem only says Loki asks "to ask of the gods" and is refused a seat); S986 "a decision handed down by a named office" is unmarked (no "office" sense located in the passage); S986 "the whole region" overreaches "all down the west coast"; the §8 table's "Norse senna … stakes: reputation, standing, and who yields" and Scottish "adjudicator" cells are design cells credited to Bellows/Ruszkiewicz although those sources do not state them.

## F. Scope note on the frozen counter

The counter measures structure, registry, census, index and content ownership. It does not measure whether a sourced sentence is supported by its capture, whether a quoted token is an exact substring, or whether a neighbour's slot grammar is stated correctly. F1–F4 are exactly that gap. Claim C's "sourced" premise is therefore only partly tested by the frozen predicate.

## G. Smallest safe correction (for the L1; not applied by me)

1. Replace "judgement" in §5 with an unquoted paraphrase of the S986 passage, or quote the exact OCR-visible text ("judg- ... mcnt" is not a usable quote; paraphrase instead).
2. Rewrite §4 paragraph: name the tradition with its S-id, cite S985's haló statement, and drop the "no single author to blame" and "required to sit still" claims or mark them inference with the contrary passage cited.
3. Rewrite §6 slot sentence to cite oath-blessing-curse-formulae.md:59 and its slot list, or remove the "same four slots" claim.
4. Replace the copied boundary/calibration/handoff paragraphs with a one-line pointer to oath-blessing-curse-formulae.md §1/§12, or rephrase them so 8-gram overlap falls below the level of a copied passage.
5. Mark the "not invited", "named office" and "whole region" statements as inference or remove.

Lane files were not edited by me. Nothing was committed.
