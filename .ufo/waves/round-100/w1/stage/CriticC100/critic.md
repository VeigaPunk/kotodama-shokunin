# CriticC100 — falsification of claim C (work song and labour chant entry)

Seat: critic (attack). Lane: kotodama, round 100, wave w1. Base `60010a55fb5f04ee728070c463b1a57ae1cc17fc`;
freeze `255d84776c12c918b7bfb2a7173d7b495e3f966e`. Read-only over the lane: nothing in
`/home/vgpnk/Projects/shokunin/kotodama-shokunin` was written except this file and its DONE marker.
Scratch `/fast/scratch/hyaku/kotodama-r100/CriticC100/` (deleted before yield).

Dependencies waited for (bounded loop, both appeared): `stage/ScribeEntry100/DONE` (09:31),
`stage/ExecRegistry100/DONE` (09:27).

---

## 0. Verdict

**Claim C survives.** No leg of C1–C8 is falsified on the landed tree; C9 was **unmeasurable at my
measurement time** (`.ufo/waves/round-100/w1/stage/ReviewerC100/reopen.json` absent — the seat's stage
dir was empty at 09:40), so the claim is not yet *demonstrated* either. Four content defects are real
and repairable without touching a leg; one registry defect must be **recorded, not repaired** (its cell
is frozen by C3).

The frozen counter, run by me over the landed tree (not read from a receipt):

```
python3 -B reports/round-100/predispatch.py --root <lane> --work $S/pdwork \
  --base-rev 60010a55fb5f04ee728070c463b1a57ae1cc17fc
LEG C1 PASS bytes=41933 h2=12 table=21x3 phrases=6/6 topic-line=equal
LEG C2 PASS rows=951 highest=S1027 new=10 qualifying=10
LEG C3 PASS added=10 removed=0 in-place-status/recheck/used-by=0 illegal=0 []
LEG C4 PASS census rc=0
LEG C5 PASS index rc=0 last: CORPUS-INDEX: OK files=272 rows=272 findings=0
LEG C6 PASS qualifying ids cited in entry: 10/10 uncited=[]
LEG C7 PASS qualifying ids bound: 10/10 captures-verified=15 failures=[]
LEG C8 PASS files scanned=272 other owners=0 []
LEG C9 FAIL reopen file missing: .ufo/waves/round-100/w1/stage/ReviewerC100/reopen.json
PREDISPATCH-100: FAIL legs=13/15
```
rc **1** (the two failures are O5, not claim C, and C9, the pending seat). **C1–C8 PASS as measured by
the frozen bytes; C9 is the only open leg.**

Surface verdict: the work-song surface is **unowned at base by content**, and the new entry is
**expansion, not duplicate authority** — measured, not asserted (§1, §2).

---

## 1. Task 1 — is the surface truly unowned at base by content?

### 1.1 The assigned body sweep

```
git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin grep -n -i -E \
 'work.?song|shant(y|ies)|call.and.response|hauling song|waulking|work rhythm|song leader' \
 60010a55fb5f04ee728070c463b1a57ae1cc17fc -- corpus/knowledge
```
rc **0**; `| wc -l` → **11** hit lines; `| wc -l` over `git grep -l` → **6** files.

Every substantive hit, inspected:

| file:line | the line | class |
|---|---|---|
| `civilizations/balts.md:165` | "Couple work songs to a validated production chain; couple wedding verses to address terms…" | passing — an application bullet asking for the coupling this entry supplies; owns no content |
| `civilizations/maori.md:52` | "Karanga \| Formal call and response in encounters such as pōwhiri" | passing — encounter ritual, a different sense of one frozen phrase |
| `culture-material/material-culture-inference-method.md:15` | "linguistics/orality-formulaic-language (work songs, maker formulas, epic object biographies)" | passing — a routing pointer; the target entry owns no work-song heading (measured below) |
| `linguistics/funerary-lament-dirge-formulae.md:129` | "will be mistaken for a work song or a lullaby" | passing — a genre test that uses work song as a contrast class |
| `linguistics/funerary-lament-dirge-formulae.md:206` | "antiphonal between two groups; a solo with a ritual answering chorus" | passing — antiphony owned as *mourning* structure |
| `linguistics/funerary-lament-dirge-formulae.md:245` | "A mourning register that reproduces … its work-song logic has been copied rather than designed" | passing — a checklist warning |
| `linguistics/lullaby-child-song-formulae.md:193` | "a tune from a work song can be reused for a lullaby" | passing — the repertoire-graph idea, work song as an unowned node |
| `linguistics/lullaby-child-song-formulae.md:245` | "the second makes it a work-song with a fixed duration" | passing — a decision-table cell inside the lullaby table |
| `linguistics/lullaby-child-song-formulae.md:253` | "a tune shared with a work song or a dance" | passing — carrier row |
| `linguistics/lullaby-child-song-formulae.md:285` | "*Oren tal* shares its tune with a Tavrin boat-work song" | passing — a NON-CANON worked example |
| `linguistics/verbal-duelling-ritual-insult.md:52` | "the challenge, the call-and-response, the naming of the sides" | passing — one item in a duel-opening inventory |

**No hit is a section.** Not one is a heading or a topic line.

### 1.2 Heading / topic-line ownership (the frozen definition)

```
git grep -n -i -E '^#+.*(work.?song|shant(y|ies)|call.and.response|hauling song|waulking|work rhythm|song leader)' 60010a55 -- corpus/knowledge
```
rc **1** (no match). Same pattern with `^- topic:` → rc **1** (no match).

```
git grep -n -i -E '^\| *[^|]*(work.?song|shant(y|ies)|call.and.response|hauling song|waulking|work rhythm|song leader)' 60010a55 -- corpus/knowledge
```
rc **0** — the only table-cell hits are the prose rows already listed above (lullaby decision table,
funerary table); none is a table whose first cell names the surface.

### 1.3 The frozen function, replayed on the base tree

```
git archive 60010a55 corpus/knowledge | tar -x -C $S/base          # 271 files
python3 -B -c "import predispatch; pd.sweep_owners(pd.tree_knowledge($S/base), pd.PHRASES)"
→ BASE-SWEEP files=271 owners=0 []
```
rc **0**. This reproduces `predispatch-base.txt` `C8 PASS … other owners=0 []` independently, on
extracted base bytes rather than the worktree.

### 1.4 The claim's own before-state, checked

```
git grep -c -i -F 'work song' 60010a55 -- corpus/knowledge
```
rc **0** → exactly **4** files (`civilizations/balts.md` 1, `culture-material/material-culture-inference-method.md` 1,
`linguistics/funerary-lament-dirge-formulae.md` 2, `linguistics/lullaby-child-song-formulae.md` 3).
This matches claims.json's "only in prose of 4 knowledge files" byte-for-byte in file count.

**Verdict on task 1: unowned at base, by content and by the frozen definition. The new entry is
expansion.** The nearest *semantic* neighbours (lullaby §7 tune-as-carrier, funerary §4 antiphony,
orality §1–2 metre, music-instrument §5 ceremonial registers, dance §53–64 coupling) each own a
different object; the entry's §1 boundary table names all of them.

---

## 2. Task 2 — overlap with adjacent owners (word-level, case-folded, 8-grams)

Method: NFKD-fold, lowercase, `[a-z0-9']+` tokens, set of 8-token shingles over the whole file, both
sides; entry shingles = **7094**. Owners taken from `stage/ConnectorOverlap100/overlap.md` §2 plus the
three civilizations files it names.

| owner | owner shingles | shared 8-grams |
|---|---|---|
| `linguistics/praise-poetry-panegyric.md` | 7355 | **7** |
| `linguistics/verbal-duelling-ritual-insult.md` | 6133 | **6** |
| `linguistics/funerary-lament-dirge-formulae.md` | 8588 | **1** |
| `linguistics/orality-formulaic-language.md` | 3592 | 0 |
| `linguistics/lullaby-child-song-formulae.md` | 7328 | 0 |
| `linguistics/toast-drinking-speech-formulae.md` | 8186 | 0 |
| `linguistics/speech-surrogates-whistled-drummed.md` | 6298 | 0 |
| `linguistics/sacred-registers-liturgical-language.md` | 5249 | 0 |
| `linguistics/sociolinguistics-registers.md` | 3941 | 0 |
| `linguistics/linguistic-anthropology.md` | 3075 | 0 |
| `culture-material/maritime-seafaring-lexicon.md` | 1743 | 0 |
| `culture-material/agrarian-field-system-lexicon.md` | 5661 | 0 |
| `culture-material/craft-artisan-lexicon.md` | 4477 | 0 |
| `culture-material/timekeeping-instruments.md` | 6084 | 0 |
| `culture-material/cuisine-food-lexicon.md` | 5193 | 0 |
| `culture-material/trade-economy-lexicon.md` | 4505 | 0 |
| `culture-material/music-instrument-lexicon.md` | 3710 | 0 |
| `culture-material/dance-performance-movement-codes.md` | 1466 | 0 |
| `civilizations/maori.md` | 4490 | 0 |
| `civilizations/balts.md` | 3752 | 0 |

Top three spans (all 14 shared shingles are **header boilerplate**, not prose):

1. `registry rows below one id per line sources` — from `- source: corpus/SOURCES.md (the registry rows below, one id per line)`
2. `the registry rows below one id per line` — same line
3. `verified at 2026 11 06 recheck 180d topic` — from the `- verified-at:` / `- recheck:` header pair
   (shared with praise-poetry, which landed the same day)

**No substantive 8-word overlap with any adjacent owner.** Cross-check: `stage/ScribeEntry100/self-check.txt`
reports `praise-poetry-panegyric.md=0; verbal-duelling-ritual-insult.md=0`. That is not reproducible on a
plain whole-file 8-gram (7 and 6 above); the difference is entirely the shared header block, so the
scribe's number is right for prose and wrong as stated for bytes. Recorded, not a defect.

---

## 3. Task 3 — quote recount, id equality, census

### 3.1 Every cited row's quote, recounted from the shipped captures

```
python3 -B -c "… ws(capture).count(ws(quote)) for each manifest entry …"
```
rc **0**. All ten: `count == 1`, `quote` is a substring of the row's `anchor` cell, and every
`captures[].sha256` matches the file on disk (15 captures, incl. the PDFs for S1022–S1025 and the HTML
for S1027).

```
S1018 count=1 words=16 anchor=True sha-ok=True
S1019 count=1 words=16 anchor=True sha-ok=True
S1020 count=1 words=20 anchor=True sha-ok=True
S1021 count=1 words=15 anchor=True sha-ok=True
S1022 count=1 words=19 anchor=True sha-ok=True (pdf+txt)
S1023 count=1 words=13 anchor=True sha-ok=True (pdf+txt)
S1024 count=1 words=21 anchor=True sha-ok=True (pdf+txt)
S1025 count=1 words=18 anchor=True sha-ok=True (pdf+txt)
S1026 count=1 words=12 anchor=True sha-ok=True
S1027 count=1 words=10 anchor=True sha-ok=True (html+txt)
```

### 3.2 rows.md ids == entry-cited ids

`stage/ExecRegistry100/rows.md` lists **S1018–S1027** (10). Entry cites **S1018–S1027** (10).
`cited-not-qualifying=[]`, `uncited-qualifying=[]`. Registry now holds **951** rows, highest **S1027**;
all ten rows are `tier A|B`, `status=mined`, `opened=2026-11-06`, `used-by` exactly
`corpus/knowledge/linguistics/work-song-labour-chant.md`.

### 3.3 Census and index, read-only

```
bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file corpus/SOURCES.md
→ file ok …/corpus/SOURCES.md   CENSUS-RC=0
python3 -B tools/check-corpus-index.py --root .
→ CORPUS-INDEX: OK files=272 rows=272 findings=0   INDEX-RC=0
```
Note: before the entry landed, census returned **rc 1** with ten `E11 missing used-by` findings
(`stage/ExecRegistry100/census.txt`); the leg is satisfied only because the entry exists at the exact
path. A path typo in the entry would have failed C4, not just C2.

### 3.4 C3 append-only, replayed

`difflib.SequenceMatcher` over base vs landed `corpus/SOURCES.md` → `added=10 removed=0`; no base line
touched. rc **0**.

### 3.5 C8 on the landed tree

`pd.sweep_owners(pd.tree_knowledge(root), pd.PHRASES, exclude=(ENTRY_REL,))` → `files=272 owners=0 []`.
rc **0**.

---

## 4. Task 4 — unsourced claims, citation sampling, tool runs

### 4.1 Tools

```
python3 -B reports/round-100/controls/feasibility/table_support_ref.py \
  --entry corpus/knowledge/linguistics/work-song-labour-chant.md \
  --evidence reports/round-100/evidence --root .
→ TABLE-SUPPORT: 0 finding(s) in 1 scoped table(s)      REF-RC=0
python3 -B tools/check-table-support.py --entry … --evidence … --root .
→ TABLE-SUPPORT: 0 finding(s) in 1 scoped table(s)      LANE-RC=0
python3 -B tools/check-table-support.py … --json
→ {"findings": [], "scoped_tables": 1}                  JSON-RC=0
```

Both tools agree, and both are **right to report nothing**: I checked the §7 cells by hand against
their captures (§4.3) and every cell's content words occur in its row's capture. The tools' silence is
not evidence of *meaning* — the contract's own `residual_honesty` says so — which is why §4.4 exists.

Table inventory (my own parse, rc 0):

| # | line | rows × cols | caption matches `\brecorded cases?\b` |
|---|---|---|---|
| 1 | 26 | 21 × 3 | no — neighbour-boundary table, design only, no sourced cell |
| 2 | 148 | 6 × 5 | **yes** — "Each row below is one recorded case…" |

Only one table carries sourced data, and it is the scoped one. No sourced table hides outside the
tool's caption scope. C1's table leg is satisfied by table 1 (21×3), not by table 2 — both qualify.

### 4.2 Sentences with no citation

250 paragraph-sentences; 184 carry no S-id or `path.md:a-b`. Read in full: they are design procedure
(§8 items 1–21), error patterns (§9), the checklist (§10), the NON-CANON worked example, and boundary
prose. All are tagged `(design, not sourced)` or are plainly method. **Two are not**, and both are
factual claims about the sources — see F1 and F2 in §5.

### 4.3 Ten sampled citations, with the supporting capture span

Every span below is an exact substring of the shipped capture (`reports/round-100/evidence/<id>.txt`),
located by `str.find` on the whitespace-normalised text.

1. **S1021** (entry §2: "in the alternating kind the precentor is also the foreman") —
   "bei letzteren ist der Vorsänger zugleich auch Vorarbeiter". Exact.
2. **S1021** (entry §4: "in work in uniform rhythm all exert themselves at the same moment, and the
   songs there become almost like a continuous command") — "oder sie erfordert gleichzeitige
   Kraftaufbietung aller Betheiligten: Arbeiten im Gleichtakt … gestalten sich bei den Arbeiten im
   Gleichtakt geradezu wie ein fortgesetztes Kommando". Exact translation; the entry's low lexical
   overlap with this capture is a language artifact, not a support gap.
3. **S1019** (entry §2: "It was only just a few words we had, but it made the thing come lighter") —
   "as a chanteyman once said to me, ' It was only just a few words we had, but it made the thing come
   lighter.'" Exact, including the surrounding "infected his work with tlie spirit of play".
4. **S1018** (entry §3: "a good one with a pretty wit was worth his weight in gold … excused all work
   save light or odd jobs") — "A good shantyman with a pretty wit was worth his weight in gold. He was
   a privileged person, and was excused all work save light or odd jobs." Exact.
5. **S1019** (entry §3: "worth a couple of extra hands") — "a capable chanteyman was worth a couple of
   extra hands". Exact.
6. **S1022** (entry §3: "a recognised leader of song in every boat; he started whatever air he
   pleased") — "There is a recognised leader of song in every boat. He starts whatever air he pleases".
   Exact.
7. **S1024** (entry §3: "the soloist calculated the psychological moment to raise the tune") — "the
   soloist calculates the psychological moment to raise the tune". Exact (Bourke quoting Campbell &
   Collinson).
8. **S1018** (entry §4: "two types … a double pull in each … the last word was usually shouted") —
   "It had two short choruses, with a double pull in each" and "The last word was therefore usually
   shouted." Exact.
9. **S1025** (entry §4: "25-30 strokes a minute, a recorded maximum of 46 under oar in the trireme
   trials") — "Steady state rowing between islands etc. was 25-30 strokes per minute. The highest speed
   under oar recorded in the Trireme Trials 1987, 1988 and 1990 was at a stroke rate of 46." Exact.
10. **S1024** (entry §5: "no genuine waulking … on Barra since the Second World War … pounding a dry
    blanket") — "no genuine waulking of cloth appears to have been done since the Sec- ond World War"
    and "set up a simulated waulking for the pur- pose, pounding a dry blanket in the way they
    remembered working the wet tweed". Exact; "1960s" is supported by "between 1965 and 1967".
11. **S1026** (entry §5: "collected at sea from 1861 … since 1872 I have not heard a shanty or song
    worth the name, and that steam spoilt them") — "Going to sea then, in 1861" and "Since 1872 I have
    not heard a Shanty or Song worth the name. Steam spoilt them." Exact.
12. **S1023** (entry §4: "groups waulking and milling songs, clapping songs and rowing songs under
    songs to facilitate group labour, and puts milking, spinning and quern songs under songs of
    occupation") — the capture's own contents list: "3. Songs to Facilitate Group Labor / 3.1 Waulking
    / Milling songs / 3.1.2 Clapping songs / 3.2 Rowing songs" and "2.2 Songs of occupation / 2.1.1
    Milking songs / 2.1.2 Spinning songs / 2.1.3 Quern songs". Exact.
13. **S1025** (entry §11: "Purser reports Collinson's suggestion … and states that he could not verify
    it despite wide enquiry") — "It has been suggested that there were two types of Gaelic rowing song,
    one for larger, one for smaller vessels (Collinson 1966: 81). Despite wide-spread enquiry, I have
    been unable to verify this statement". The hedge is **kept** here — good.
14. **S1022** (entry §4: "The title 'dreg-song' was given in Scotland to labour songs in general and in
    particular to those of the harvest field") — capture: "The title of dreg-song **seems to have
    been** given in Scotland to labour-songs in general, and in particular to those of the harvest
    field." **The hedge is dropped** — see F3.

### 4.4 §7 table cells, checked by hand against their captures

`hauling shanties` — "extempor" ×5 in S1018, "double pull", "last word … shouted" ✓.
`capstan chantey` — "precentor, or chanteyman, singing the verse and the workers the refrain",
"marching round the capstan", "required pace" ✓.
`Sea Islands rowing` — "two measures are to be sung to each stroke", "passenger boat at the [Beaufort]
ferry", "used when the load was heavy or the tide was against us" ✓.
`waulking` — "a brisk four-time", "a long table or board", "no song was sung twice" ✓.
`oyster dredging` — "a recognised leader of song in every boat", "keeping time most faithfully", "We
have heard it in the early morning many times, fully two and a half miles inland", "sing till the
dredge is hauled up" ✓.
`Hebridean iorram` — "call and response alternation of soloist and chorus", "The main determinant in
stroke speed and length is the sea state", "Steady state rowing between islands", "the needs of the
rowers come first" ✓.

Setting words checked against captures: `Sea Islands` ×9 in S1020 (raw `grep` returns 0 because the
capture is hard-wrapped; normalised count 9), `Kalinga` ×6 and `Mangali` ×9 in S1027, `Hebridean` ×23
in S1025, `Firth of Forth` ×4 in S1022, `Barra` in S1024, `Prestonpans` in S1022. **No setting word is
absent from its capture.**

---

## 5. Findings and repair recipes

### F1 — an unmarked universal over all ten sources (line 63)

Entry: "None of the reports makes the song decorative: **in each**, the song is the device by which a
gang's separate exertions become one movement."

Counterexample: **S1027** (SIL Mangali page) says only "Tug-om is sung by women while pounding rice or
coffee" and "Suggiyaw is a harvest song, often sung in the rice field after a day's work of cutting and
hauling" — it names occasions and never claims coordination. S1023 is a classification essay and makes
no such claim either. "in each" is false for at least two of the ten.

Class: an unmarked universal asserted over cited sources (R99-M2 family: the sentence outruns the
captures while every frozen leg passes — the tools are lexical and cannot see a quantifier).

**Repair (safe, entry-only):** replace "in each" with the set that does claim it —
"in the maritime, Gaelic and Sea Islands reports the song is the device by which a gang's separate
exertions become one movement (S1018, S1019, S1020, S1022, S1024, S1025, S1026); the Kalinga page
names occasions without claiming coordination (S1027)."

### F2 — internal contradiction about the sources' scope (line 250 vs line 260)

Entry §11 line 250: "**No source in the base is a survey: each reports work song inside one setting**,
and the entry therefore claims no grammar of the genre as a whole (design, not sourced)."
Entry §11 line 260: "Bücher is a **comparative** nineteenth-century treatise, not a field report (S1021)."

Counterexample: S1021's own text ranges over smith, locksmith, tinsmith/plumber (Klempner), coppersmith
(Kessler), joiner, shoemaker, weaver, and "im Bereiche der haus- und landwirthschaftlichen
Verrichtungen" — and it is cross-cultural, not one setting: `grep -c -i -E
'australier|indianer|neger|eskimo|malaien|polynesier' S1021.txt` → **43** (Australier 4, Indianer 20,
Neger 19, Polynesier 1). It is comparative across trades *and* peoples. The tag `(design, not sourced)`
does not rescue the sentence: it is a factual claim about the corpus, and the entry contradicts itself
six lines later.

**Repair (safe, entry-only):** "No source in the base is a survey of the genre: each of the field,
collection and archival sources reports work song inside one setting, and Bücher is the exception — a
comparative treatise whose developmental scheme is not used here (S1021). The entry therefore claims no
grammar of the genre as a whole."

### F3 — a source hedge reported as fact (line 106)

Entry: "The title 'dreg-song' **was** given in Scotland to labour songs in general and in particular to
those of the harvest field (S1022)."
Capture: "The title of dreg-song **seems to have been** given in Scotland to labour-songs in general,
and in particular to those of the harvest field."

Class: hedge dropped — the exact R99-M2 failure mode ("a hedged source stays hedged"). The frozen
tools cannot see it: the cell is lexically supported.

**Repair (safe, entry-only):** "The title 'dreg-song' **seems to have been** given in Scotland to
labour songs in general and in particular to those of the harvest field (S1022)."

### F4 — a duplicated paragraph in §12 (lines 278 and 280, byte-identical, 236 B each)

`python3` comparison of the two `The readings listed here are mine…` lines → `equal: True`, both 236
bytes. A copy-paste duplication in the inference ledger's preamble.

**Repair (safe, entry-only):** delete the second occurrence (line 280). No leg reads it; C1's byte
count stays far above 12000.

### F5 — three registry `teaches` cells overstate (record only: the cell is frozen by C3)

- **S1026**: "the earliest English description of the leader/response hauling song" — the capture says
  "In a medieval work of about 1450, called the Complaynt of Scotland, we have a description…"; the
  word "earliest" does not occur in that sense (`grep -c -i earliest S1026.txt` finds only "in the
  earliest days of the true sailing ship"). The entry itself does **not** repeat "earliest"
  (`grep -c -i earliest <entry>` → 0), so the entry is clean.
- **S1022**: "sung only when wind failed" — capture: "used when the wind was unfavourable or
  insufficient to tow the dredge". No "only". The entry does not repeat it (`grep -i 'only when'` → no
  match).
- **S1021**: "examples run smith, locksmith, tinsmith, **cooper**, carpenter, shoemaker, weaver" — the
  list is Schmied, Schlosser, Klempner, **Kessler** (coppersmith), Tischler, Schuster, Weber. "Cooper"
  is wrong (Böttcher appears elsewhere in the book, not in this list).

**Repair: none this round.** `predispatch.py` C3 treats cell index 6 (`teaches`) as fixed
(`fixed = (0,1,2,3,4,5,6,8)`), so an in-place edit of `teaches` would make **C3 fail**. Record these in
the round lesson for a later round; the entry already declines to repeat them.

---

## 6. Residual gaps (stated, not repaired)

- **C9 unmeasured.** `stage/ReviewerC100/` was empty at 09:40; `reopen.json` absent. C9 needs ≥3
  qualifying ids re-opened with `quote_count == 1` on fresh bytes by the non-author seat. If that file
  never lands, C9 fails and claim C fails on C9 alone — no content defect is involved.
- **C8's containment is blind to plurals of one phrase.** `norm("shanty")` does not match a heading
  "Shanties". A future file could take the shanty surface with a plural heading and C8 would not see
  it. Measured, not triggered: the landed tree has `owners=0`, and the entry's own §5 heading uses the
  singular.
- **The tools measure co-location, not entailment.** F1 and F3 are both invisible to battery100 and to
  both checkers; they were found by reading, which is what this seat is for.
- **`material-culture-inference-method.md:15` still routes "work songs" to orality.** The entry records
  the stale pointer in §11 and does not edit the sibling (correct under the item's non-goals).

### 6.1 Cross-claim regression check (praise entry is dirty in the worktree)

`git status --porcelain` shows ` M corpus/knowledge/linguistics/praise-poetry-panegyric.md` — the
optional ScribeTable100 repair. claims.json separability requires the Yoruba row label, the table
header and the Yoruba limit cell to stay byte-unchanged so O3 is unaffected. Measured against base:

```
yoruba-row-count base/cur: 1 1
header byte-equal: True
label byte-equal: True   (' Yoruba ')
limit-cell byte-equal: True   ('an epithet can recall danger or contested reputation rather than flatter')
```
rc **0**. And the counter's O3 on the current tree: `actual rc=0 findings=0; forged rc=1 findings=1;
forged-minus-actual=[('UNSUPPORTED-CELL','Yoruba','limit on the praise')] actual-minus-forged=[]` — the
repaired cells are supported, so the replay premise is intact. **No regression from the praise edit.**

---

## 7. Commands run (all read-only), with rc

| # | command | rc |
|---|---|---|
| 1 | `git grep -n -i -E 'work.?song\|shant(y\|ies)\|call.and.response\|hauling song\|waulking\|work rhythm\|song leader' 60010a55 -- corpus/knowledge` (11 lines / 6 files) | 0 |
| 2 | same, `^\| *[^\|]*` table-row form | 0 |
| 3 | same, `^#+` heading form | 1 |
| 4 | same, `^- topic:` form | 1 |
| 5 | `git grep -c -i -F 'work song' 60010a55 -- corpus/knowledge` (4 files) | 0 |
| 6 | `git archive 60010a55 corpus/knowledge` → 271 files; `sweep_owners` → owners=0 | 0 |
| 7 | 8-gram overlap over 20 adjacent owners (entry 7094 shingles) | 0 |
| 8 | manifest quote recount, 10 ids, `ws(capture).count(ws(quote))` | 0 |
| 9 | `sources-census.sh validate --file corpus/SOURCES.md` | 0 |
| 10 | `tools/check-corpus-index.py --root .` (files=272 rows=272) | 0 |
| 11 | `difflib` base-vs-land `corpus/SOURCES.md` → added=10 removed=0 | 0 |
| 12 | `sweep_owners` on landed tree excluding the entry → owners=0 | 0 |
| 13 | `table_support_ref.py --entry … --evidence … --root .` → 0 findings / 1 scoped table | 0 |
| 14 | `tools/check-table-support.py …` (text and `--json`) → 0 findings / 1 scoped table | 0 |
| 15 | table inventory + caption scope (2 tables; 1 scoped) | 0 |
| 16 | duplicate-line scan (`awk 'seen[$0]++'`) → line 280 duplicates 278 | 0 |
| 17 | `python3 -B reports/round-100/predispatch.py --root <lane> --work $S/pdwork --base-rev 60010a55…` → C1–C8 PASS, C9 FAIL (reopen absent), O5 FAIL | 1 |

No tool was installed or upgraded this round (none needed). No pacman, no sysctl, no git/jj mutation.
Scratch deleted before yield.
