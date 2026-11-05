# Round 90 — an advance-evidence grader, and a petitionary and votive entry

author: kotodama lane (including its dispatched seats), 2026-11-04.
Claims: O / operability — capability acquisition, `tools/check-advance-evidence.py`
with 67 selftest checks, a 43/43 mutation receipt and 13 named refusals of the
round-89 survivor classes; C / coverage — one new linguistics entry,
`corpus/knowledge/linguistics/petitionary-and-votive-formulae.md`.
Base `6b0b86e45ae902331aca75863db380f2991458c4`; claim/counter freeze
`d0b6f2a7f9cc36272682749a9b047b739406f0c8`; executed controls and counter
revisions precede the first dispatch (`9fb2c58f`, `c0c628d8`, `ebd81b1b`).
Freshness stays paused (open L0 `kotodama | round-11` and `round-89`), so C
works coverage, the lowest axis this round may move.

## Gate

Opened sources, access 2026-11-04 (America/Sao_Paulo, −03:00). Every row below
was opened by ordinary HTTP (`curl -sS -L`), no browser, no challenge, no login;
the seven admitted bodies are committed under `reports/round-90/evidence/` with
`sha256`, `http_status` and a local fetch instant in `manifest.json`. Tier scope
is the exact use, not a general certificate. One gate line per row, so a quote
is never attributed to a neighbouring id.

### Admitted (seven rows, six A and one B)

- S942 LOCATED — "The constructions studied have to be grammaticalized, but they need not be morphologically or syntactically uniquely imperative-hortative." — https://wals.info/chapter/72 accessed 2026-11-04, section 1.1; the chapter's own Map 72A table gives 133/20/21/201 of 375, quoted in the row's teaches cell.
- S943 LOCATED — "this chapter restricts attention to languages with a dedicated inflectional optative form as in (1)" — https://wals.info/chapter/73 accessed 2026-11-04, section 1; Map 73A gives 48 present and 271 absent of 319, and section 5 states the areal skew the entry uses.
- S944 LOCATED — "The prohibitive uses the verbal construction of the second singular imperative and a sentential negative strategy found in (indicative) declaratives" — https://wals.info/chapter/71 accessed 2026-11-04, section 1; the four Map 71A values total 496, so this class is 113 of the sample.
- S945 LOCATED — "Vocative case is a case that marks a noun whose referent is being addressed." — https://glossary.sil.org/term/vocative-case accessed 2026-11-04, Definition; the glossary's own Examples block gives the Latin *Et tu, Brute* the entry repeats.
- S946 LOCATED — "has objected that differences in letter forms mean that Smikros’ dedication cannot be the work of the ‘Hekatompedon Master’." — https://www.atticinscriptions.com/inscription/IGI3/646 accessed 2026-11-04, commentary note; the page dates the base ca. 510-500 BC and names Edmund Stewart as translator.
- S947 LOCATED — "The results reveal a significant relative increase in the use of explicit votive terminology" — https://pmc.ncbi.nlm.nih.gov/articles/PMC13671548/ accessed 2026-11-04, abstract; the same abstract states the roughly 11,000-inscription corpus and the epigraphic-habit control.
- S948 LOCATED — "We propose the notion of n-selection, a narrative rule which can't be reduced to syntax or semantics: it depends on culture." — https://drops.dagstuhl.de/entities/document/10.4230/OASIcs.CMN.2016.12 accessed 2026-11-04, abstract; the same abstract names both litanies and the twentieth-century test case.

### Rejected (one row, kept with its flip condition)

- S949 REJECTED — "A votive offering or votive deposit is one or more objects displayed or deposited, without the intention of recovery or use" — https://en.wikipedia.org/wiki/Votive_offering accessed 2026-11-04, lead section. Reason: tertiary encyclopedia text with no named author, no dating and no corpus, so it cannot carry a petitionary or votive claim under this lane's tier rule. Flip: a referenced revision whose every claim names a scholarly edition or catalogue.

### Seed rot found before the rows were written

The reading list the wave started from was wrong in three places, and opening
the pages is what caught it. Chapter 74 is Situational Possibility, not the
Prohibitive, which is chapter 71; the SIL glossary 404s on `/term/vocative`
while `/term/vocative-case` answers; and the same glossary has no entry for
prayer, invocation, supplication, petition, vow, votive, blessing or curse at
all. Three further seeds (three Wikipedia articles) are tier C and were not
admitted. A row copied from that list without opening it would have cited a
page that contradicts its own scope cell.

Registry changes: S942–S948 added (six A, one B; six `mined`, all `opened
2026-11-04`, `used-by` = the new entry), S949 added as `rejected` with the
lesson as `used-by`. No existing row's cell was touched, so the freshness
pause is respected: nothing was re-verified, re-dated or repaired this round.

**Known survivors, stated before data.** The entry-mode grader checks quote
length, url and date on the gate line and quote-in-capture, so a title or
site-chrome string is not refused; a capture fabricated together with its quote
is not refused; and a repetition filler is only flagged above two occurrences.
The defences are the independent re-fetch seat, the reviewer and the critic,
and the closure's own re-open. This landing's exposure to each class is audited
in the round report, not claimed away here.

**Independent spot-check:** pending outside closure. Dispatched seats and the
L1 are the lane, not non-author verifiers. No promotion box becomes `[x]`.

Assimilation: none this round — the lane has no `considerthese` directory, and
shokuknow package adoption stays closed under the wave-4 quarantine-first rule.

## Understanding and trial

The O claim exists because round 89's own wave falsified the round-89 counter:
five counterfeit landings passed its frozen predicate, and its mutation score
was 10 of 41. The new grader is deliberately small and boring — one tool that
grades one landing — but each of its sub-checks has a negative in its own
selftest, and the mutation receipt is committed before dispatch rather than
after data, which is what QUALITY36 asks for.

The C claim is a coverage move on ground the coverage map did not hold. The
base surface, measured with the command QUALITY36 requires: `git archive
6b0b86e4 corpus/knowledge | tar -x -C "$S"` then `grep -rn -i -E
'^#+ .*(prayer|petition|votive|supplicat)' "$S/corpus/knowledge"` returns nine
lines in five entries and no dedicated file — carthage.md:1 (*Punic Language,
Votive Cult*), sacred-topography-pilgrimage.md:1 and :74 (*the votive economy —
the object, the receipt, the token*), religion-language-co-evolution.md:1 and
:64 (*prayer languages: model events and permissions*), tibet.md:92 (prayer-wheel
mantra economies), direction-symbolism.md:129 (orientation of prayer), plus two
lines from garment-lexicon-crosslinguistic.md that match only the substring
inside *competition* and are not topical. The h2-only spelling of the same grep
(`'^## .*…'`) misses the four `#` headings and keeps the same two false
positives, so the heading level must be stated with the command.
What the entry adds that those sections lack: the four WALS mood paradigms with
their sample counts and totals, the address slot separated from the mood system,
the votive formulary as a dated object with a social reading, the large-corpus
correlation findings under the epigraphic-habit control, and n-selection as the
reason a litany's order is a cultural decision rather than a syntactic one.

Trial: the entry is a design instrument, not a description. Its procedure
section produces, in order, a mood decision, a prohibitive strategy, an address
system, a vow formula with its receipt, a votive object inventory, an archaism
list, a litany with a stated ordering principle and eight failure checks. A
reader can run it on an empty world and get a register out; that is the test the
entry is written to pass.

## Mistakes

| id | class | evidence | captured-by | fix or retained limit |
|---|---|---|---|---|
| R90-M1 | scope (inherited, repaired this round) | The inherited wave's seat list included four census-invalid names, so wave items could not be graded by the role they claimed | QUALITY7 | Re-dispatched this round as one v1 wave whose role names come from the validator's accepted set; the earlier spec is kept as evidence, unnamed seats stay unnamed rather than relabelled after the fact |
| R90-M2 | stale-premise (this round) | Three seeds were dead or mislabelled on open: WALS chapter 74 is Situational Possibility (Prohibitive is 71), `/term/vocative` is 404 while `/term/vocative-case` answers, and the SIL glossary carries no prayer or votive term at all | QUALITY14 (a row is written only after opening the source) | All three caught before a row was written; the entry states the 404s explicitly instead of silently substituting a synonym |
| R90-M3 | reference-drift (this round) | The frozen counter's ENTRY leg keyed verdicts with `dict(re.findall(...))`, so every leg read as missing and claim C could never pass; found by a wave seat, recorded in `reports/round-90/counter-revisions.md` rev 6 | none (the counter's own selftest did not cover the C leg) | Fixed before any data existed on the C leg; the frozen predicate, leg names and thresholds are unchanged, and the defect is retained here rather than hidden by the fix |
| R90-M4 | landing (this round) | The earlier attempt's seat wrote seven captures and no manifest, so its claims could not be graded and its work could not be cited; the L1 died on provider failure before landing | QUALITY7 | The captures were re-fetched by the L1 into `reports/round-90/evidence/` with a manifest, and the entry is written from the re-fetched bytes, not from the dead seat's stage |
| R90-M5 | numbers (this round) | One registry row drafted from memory said the prohibitive chapter was 74; opening the page showed chapter 71 and a 496-language sample | QUALITY14 | Row corrected before append; the gate quote for that row is taken from chapter 71's own values table |
| R90-M6 | vacuous (this round, retained) | `tools/check-row-fragments.py` printed a green over the round-90 stage while reading zero files, because it walks `--rows` for `row-*.txt` pinned to round 65 | QUALITY23 | Not counted as evidence this round; the row-fragment check is done by the census and the grader instead, and the vacuous green is reported rather than cited |
| R90-M7 | vacuous (this round) | `reports/round-90/separability90.py` refused with `overlay C tree is not the declared selection: extra=[] missing=[]` because the declared selection listed a path twice (the entry is both a graded path and inside the `corpus/knowledge/**` substrate) and git trees are sets | QUALITY23 (a check that cannot distinguish its own failure from a clean state) | `expected = sorted(set(present))`, one line, with the reason in a comment; rerun PASS both overlays. A refusal whose `extra` and `missing` are both empty is a self-defect, never a finding about the tree |
| R90-M8 | numbers (this round) | The lesson's first draft stated the base surface with an h2-only grep and named six entries; the measured command returns nine lines in five entries including two `competition` false positives, and misses four `#` headings | QUALITY36 (base-measured surface) | Corrected before landing: the lesson now prints the exact command, the heading level and the false positives; the frozen `claims.json` surface text is not edited |
| R90-M9 | verification (this round) | The claim that the SIL glossary carries no prayer or votive term rested on another seat's fetches until it was re-measured: on 2026-11-04 all nine of `vocative`, `prayer`, `invocation`, `supplication`, `petition`, `vow`, `votive`, `blessing`, `curse` return 404 under `https://glossary.sil.org/term/` | QUALITY14 (open the source, do not inherit an opened claim) | The nine-term sweep is recorded here; the entry states the 404s and the glosses it does carry |

## Settlement

Round shape, seat table, dead seats and the per-wave result file are recorded in
the round report (`reports/round-90/` receipts plus the fleet report). Measured
claim results are appended after landing, not asserted here.
