# ScribeEntry97 — round 97 claim C entry (linguistics, verbal duelling and ritual insult)

Seat: ScribeEntry97 (scribe). Wave `kotodama-r97-v1`, milestone r97-v1. Date 2026-11-05.
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (the only repo written).
Nothing committed, pushed, or published by this seat; the L1 is the only committer.

## 1. Files written (this seat owns these paths only)

| path | what |
|---|---|
| `corpus/knowledge/linguistics/verbal-duelling-ritual-insult.md` | NEW entry (the claim-C surface). sha256 `d021072f1e20e4db738df6e24f22eee64a28c0f8018c4a06d8c6a0682b7eb4a4`, 37 387 bytes |
| `corpus/README.md` | index edit: `## linguistics/ (41)` → `(42)`, one new row in filename order, trailing totals 268 → 269, footer vector `42/36/43/29/24/95`, and a `## Round 97 verbal duelling entry (2026-11-05)` section appended in the round-96 shape |
| `corpus/knowledge/linguistics/funerary-lament-dirge-formulae.md` | ONE added sentence (line 70) citing S993; no other change to the file (`git diff` = 2 insertions, 0 deletions, 0 modifications) |
| `.ufo/waves/round-97/w1/stage/ScribeEntry97/self-check.txt` | self-check output (self-check.txt) |
| `.ufo/waves/round-97/w1/stage/ScribeEntry97/selfcheck.py` | the seat's self-check script, kept so the measured numbers stay re-runnable after the scratch dir is deleted |
| `.ufo/waves/round-97/w1/ScribeEntry97/counterwork/` | the `--work` dir the frozen counter was run with |
| `.ufo/waves/round-97/w1/ScribeEntry97.md` | this report |

Not written by this seat: `corpus/SOURCES.md`, `reports/round-97/evidence/`, `tools/check-advance-evidence.py`,
`corpus/QUALITY.md`, any frozen file (`reports/round-97/claims.json`, `predispatch.py`, `predispatch-base.txt`,
`sweep-control.*`, `controls/*`), any file under `reports/round-96/` or earlier, and every sibling lane.

## 2. Entry shape (measured; every number has its command and rc — full transcript in self-check.txt)

Command for [1]: `python3 -B .ufo/waves/round-97/w1/stage/ScribeEntry97/selfcheck.py --entry corpus/knowledge/linguistics/verbal-duelling-ritual-insult.md --rows .ufo/waves/round-97/w1/stage/ExecRegistry97/rows.md --root .` → **rc 0**
(the seat script is kept in the stage dir so the numbers stay re-runnable after the scratch dir is removed).

| measurement | value | floor |
|---|---|---|
| bytes UTF-8 | 37 387 | 12 000 |
| h2 headings | 13 | 6 |
| best table | 7 data rows × 6 columns | ≥5 × ≥3 |
| frozen phrases in h2 headings / table data rows | 6/6 (`verbal duel`, `ritual insult`, `flyting`, `song duel`, `boast formula`, `audience adjudication`) | ≥4 |
| `- topic:` line | byte-equal to the frozen topic (372 bytes, one em dash U+2014) | byte-equal |
| qualifying ids cited | 8/8 (`S985`–`S992`) | all |

Structure: §1 scope and the four deferrals (oral-formulaic composition → `linguistics/orality-formulaic-language.md`;
binding-speech satire-as-curse → `myth-symbol/binding-speech-complex.md` + `linguistics/oath-blessing-curse-formulae.md`;
politeness/taboo → `linguistics/politeness-taboo-euphemism.md`; canon → lore-shokunin, research method → chousa);
§2 the verbal duel; §3 flyting and senna; §4 ritual insult; §5 song duels; §6 the boast formula;
§7 audience adjudication; §8 the contest-genre table (7 rows × 6 cols: tradition, form and venue, contestants,
adjudicator, stakes, source) plus a one-row-per-registry-row grounding list; §9 the six rules that keep an insult
ritual; §10 ten error patterns (incl. **insult with no frame**, **contest with no judge**, **ritual that slips
into real violence**); §11 the 19-step decision procedure and checklist plus a NON-CANON worked micro-example;
§12 limits, calibration and the lore handoff; §13 the inference ledger.

## 3. Cited registry ids (each cited at the claim it supports)

All eight are the landed claim-C rows from `.ufo/waves/round-97/w1/stage/ExecRegistry97/rows.md`
(ids read from the landed rows.md, not derived — round-96 lesson R96-M4).

| id | source | claim in the entry it supports | located quote (bytes.count == 1 on the landed capture) |
|---|---|---|---|
| S985 | Pagliai 2009, *The Art of Dueling with Words* | §2 definition, range of forms, catharsis critique; §4 duel ≠ ritual insult; §6 theme proposed by the audience; §7 audience adjudicates | "A common view of verbal duels posits that they are a cathartic expression of aggression" (S985.txt) |
| S986 | Hoebel 1954, *The Law of Primitive Man* | §5 song duel as juridical instrument, festive occasion, judge inside the contest | "Among the East Greenlanders song duels may be carried on for" (S986.txt) |
| S987 | Bellows, *Lokasenna* | §3 the senna at a feast, the guest who demands a seat | "Then Loki went into the hall, but when they who were there saw who had entered, they were all silent." (S987.html) |
| S988 | Dunbar & Kennedy, ed. Murphy | §3 the flyting as verbal competition | "The flyting was a verbal competition in which the participants vied in heaping abuse of" (S988.txt) |
| S989 | Ruszkiewicz 2020 | §3 the flyting's purpose (humiliate the opponent) | "the Scottish genre of flyting, whose main" (S989.txt) |
| S990 | Garzia 2007 | §7 the judges' panel as an institution of the contest | "the references to the verbal combats between bertsolaris and the social importance that such" (S990.txt) |
| S991 | Nadera 2019 | §7 the named adjudicator (*lakandiwa*) | "Balagtasan is an indigenous form of competitive Filipino debate poetry in the Tagalog language" (S991.txt) |
| S992 | Nicholson 1907 | §3 the Arabic *naqāʾid* recited before a partisan crowd | "Soon these 'Flytings' (_Naqá’iḍ_) were recited" (S992.txt) |

Quote recount command (self-check.txt [5]): a python3 pass over all 25 distinct quoted spans in the entry against
`reports/round-97/evidence/S985.txt` … `S992.txt` — **rc 0**, `QUOTES 25 NOT-LOCATED 0`. Every span is ≤25 words and
occurs exactly once (`bytes.count == 1`) in the named capture.

Uncited claims: every claim in the entry that is not carried by a registry row is marked `(design, not sourced)`
(the procedure, the tables of rules and error patterns, the worked example) or `(inference)` (see §5).

## 4. Inference list (marked *inference* in the body, §13 ledger in the entry)

1. That the four frame parts (licence, occasion, form, release) separate a ritual insult from a personal attack.
2. That a duel need not use insults; an insult-exchange is one option, not the genre.
3. That fixing the adjudication before the dialogue is the safest way to model a word-contest for fiction.
4. That the consequence rule (what the insult does *not* do) is the rule a reader checks first.
5. That a contest with no award is a different genre (a display), not a contest with a small prize.
6. That the catharsis reading of verbal duels is a twentieth-century scholarly framing rather than a description
   of the forms themselves.

## 5. Index edit (step 3)

Command: `python3 -B tools/check-corpus-index.py --root .` → **rc 0**, `CORPUS-INDEX: OK files=269 rows=269 findings=0`
(self-check.txt [2]). The edit is the round-96 shape: the `## linguistics/` heading count moved 41 → 42 (the
index tool's HEADER_DRIFT check compares the declared count with the partition's disk count), the new row sits in
filename order inside the section, the trailing totals line reads 269, the trailing footer reads
`(total 269 files; directory totals 42/36/43/29/24/95)`, and a `## Round 97 verbal duelling entry (2026-11-05)`
section is appended. Older totals blocks were left as filed (append-only).

## 6. Threnoi sentence (step 6)

`stage/ExecRegistry97/threnoi.md` reports a landed row **S993** (tier A, mined, opened 2026-11-05, used-by
`corpus/knowledge/linguistics/funerary-lament-dirge-formulae.md`), so the file was changed. Exactly one sentence
was added, in the professional-mourner part (§3 *Professional keeners: the licensed voice of grief*), at
**line 70** of `corpus/knowledge/linguistics/funerary-lament-dirge-formulae.md`:

> A Greek case supplies the same office under another name: in the Maniat lament of Epirus the dirge has a
> professional leader, and the source names that office when it describes "the leader of the dirge (koriféa), twice
> widowed, asks her audience" (S993).

Quote recount: `bytes.count` of that quote on `reports/round-97/evidence/S993.txt` = **1** (self-check.txt [8]).
`git diff` on the file = 2 insertions, 0 deletions — no other change.

## 7. Frozen-counter run over the lane tree

Command: `python3 -B reports/round-97/predispatch.py --root . --work <scratch> --base-rev 1ffc5a83d2c70e3bc581594efbcf32c562ba2569`
→ **rc 1**, `PREDISPATCH-97: FAIL legs=12/13` (self-check.txt [6]).

Claim-C legs, all PASS:
`C1 PASS bytes=37387 h2=13 table=7x6 phrases=6/6 topic-line=equal` ·
`C2 PASS rows=917 highest=S993 new=9 qualifying=8` ·
`C3 PASS added=9 removed=0` ·
`C4 PASS census rc=0` ·
`C5 PASS index rc=0` ·
`C6 PASS qualifying ids cited in entry: 8/8` ·
`C7 PASS qualifying ids with capture: 8/8` ·
`C8 PASS files scanned=269 other owners=0 []`.

The single FAIL is **O3** (`sha pin missing or malformed: reports/round-97/controls/mutants97.sha256`) — the mutation
driver pin, which belongs to the MutationTester97 seat and to the L1's landing, not to this seat. O0, O1, O2 and O4
PASS. This seat neither writes nor depends on that pin.

## 8. C8 ownership sweep (content, not filenames)

The entry is the only owner of the frozen phrases. Checked with the counter's own `sweep_owners` over
`corpus/knowledge`: `files scanned=269 other owners=0 []` (counter leg C8, PASS).
`python3 -B reports/round-97/sweep-control.py --root .` → **rc 0**: `R96-REPLAY … owners=2`, `R97-BASE … owners=0`,
`SWEEP-CONTROL: PASS` — the sweep is shown able to fail on the round-96 base.

No other knowledge file's `- topic:` line or heading carries a frozen phrase. The prose mentions that exist
(`orality-formulaic-language.md:112`, `myth-symbol/trickster.md:25` and `:62`) were not touched and are mentions,
not ownership.

## 9. Boundary respect (overlap.md, surface.md)

Deferred, not restated: oral-formulaic composition machinery and performer licensing
(`linguistics/orality-formulaic-language.md`); the binding/enforcement side and the cause grammar
(`myth-symbol/binding-speech-complex.md`, `linguistics/oath-blessing-curse-formulae.md`); politeness, taboo and
euphemism (`linguistics/politeness-taboo-euphemism.md`); the trickster figure (`myth-symbol/trickster.md`); contest
procedure and competitor status for bodies and boards (`culture-material/games-play-sport-contests.md`); the
qaṣīdah mode table and the Arabic invective calibration (`civilizations/arabia-pre-islamic.md`); the Gẹ̀lẹ̀dẹ́
performance account (`civilizations/yoruba.md`).
Canon deferred to lore-shokunin; research method deferred to chousa (PROVINCE.md).

## 10. Tools

**None installed or upgraded.** No pacman, no `uv tool install`, no release binary, no cargo/npm. The only tools
run are pre-existing: `python3` (3.x), `pdftotext` (poppler, already present), `curl` (not used by this seat —
the registry seat opened the sources), and the repo's own `tools/check-corpus-index.py`,
`tools/check-cited-lines.py`, `reports/round-97/predispatch.py`, `reports/round-97/sweep-control.py`.

## 11. Known limits and honest notes

- The claim-C base is **eight** opened rows from five traditions (Scots, Norse, Inuit, Basque, Filipino) plus one
  Arabic account; it is not a survey, and §12 says so.
- Two quotes are **line fragments** rather than whole sentences, because the capture's line breaks fall mid-sentence
  (S988 "…heaping abuse of" / "all sorts on each other, some of it quite gross."; S989 "…whose main" / "purpose was
  to humiliate the opponent"; S990 and S992 likewise). Each fragment is separately byte-exact and count==1 on its
  capture; the two halves of a split quote are quoted adjacently in the same sentence so the reading stays whole.
- The registry seat's cell forms flatten the newline to a space; the entry quotes the byte-exact capture form, so a
  reviewer comparing the entry with the registry cell sees the same words with the line break restored.
- The entry cites only ids that had landed rows at the time of writing (S985–S992). S993 (Threnoi) is the
  round-96 routed frontier row and is cited in the lament entry, not here; it is not one of claim C's qualifying
  rows and is deliberately absent from this entry.
- The registry seat's S986 evidence pair is an HTML details page plus a djvu OCR text; the quote lives on the OCR
  text (`S986.txt`), which is the file the entry's quote is counted against.
- Freshness is paused by the open L0 questions; this round moves no freshness axis, and this seat claims no axis move.
- Nothing in the fleet repo `/home/vgpnk/Projects/shokunin` was written; the only writes are in the lane repo and
  this seat's own stage/report paths.
