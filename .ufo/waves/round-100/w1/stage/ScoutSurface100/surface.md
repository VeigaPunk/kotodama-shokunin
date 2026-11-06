# ScoutSurface100 — claim C coverage surface, adjacency map, skeleton, partition walk

Read-only scout. Nothing in the lane was written except this file and its DONE marker.
Base: `60010a55fb5f04ee728070c463b1a57ae1cc17fc` (claims.json `base`); freeze commit
`255d84776c12c918b7bfb2a7173d7b495e3f966e`. All commands run from
`/home/vgpnk/Projects/shokunin/kotodama-shokunin` unless a `cd` is shown.
Scratch: `/fast/scratch/hyaku/kotodama-r100/ScoutSurface100/`.

Question answered: is the work-song / labour-chant surface genuinely unowned at base, what
does each neighbour own that the new entry must *not* restate, where do the six frozen phrases
land naturally, and does `linguistics/` hold the entry.

---

## 1. Sweep outputs, with rc

### 1.1 Broad body sweep (the assigned command)

```
grep -rn -i -E 'work.?song|labou?r song|shant(y|ies)|chant(e)?y|call.and.response|hauling|rowing song|waulking|field holler|work rhythm|song leader|pounding song|threshing song|spinning song|weaving song|lumber|stevedore|chain gang' /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/knowledge
```

rc = 0, **14 hit lines** (captured to `sweep1.txt`, `wc -l` = 14).

Two of the 14 are false positives produced by the loose alternation, both from substrings:

| line | matched by | why false |
|---|---|---|
| `linguistics/numerals-and-measures.md:91` | `chant(e)?y` | the language name **Chantyal** (Minangkabau/Hungarian/Chantyal/Tongan/Haida classifier row) |
| `linguistics/politeness-taboo-euphemism.md:88` | `lumber` | **slumber** rooms (Mitford 1963 death-euphemism ladder) |

### 1.2 Word-boundary refinement

```
grep -rn -i -E '\b(work.?songs?|labou?r songs?|shant(y|ies)|chant(e)?y|call.and.response|hauling|rowing songs?|waulking|field hollers?|work rhythms?|song leaders?|pounding songs?|threshing songs?|spinning songs?|weaving songs?|lumber|stevedores?|chain gangs?)\b' corpus/knowledge
```

rc = 0, **12 hit lines in 7 files** (captured to `sweep2.txt`):

```
4  corpus/knowledge/linguistics/lullaby-child-song-formulae.md
3  corpus/knowledge/linguistics/funerary-lament-dirge-formulae.md
1  corpus/knowledge/linguistics/verbal-duelling-ritual-insult.md
1  corpus/knowledge/culture-material/material-culture-inference-method.md
1  corpus/knowledge/civilizations/mississippian.md
1  corpus/knowledge/civilizations/maori.md
1  corpus/knowledge/civilizations/balts.md
```

### 1.3 Ownership sweep — the C8 pre-check (headings and topic lines only)

C8 scans only `corpus/knowledge/**/*.md` (`predispatch.py:147-155`) and counts a file as an
owner when a frozen phrase appears in its `- topic:` line or in any markdown heading
(`predispatch.py:131-134`, prose and table cells are "mentions, not ownership").

```
for p in "work song" "call and response" "song leader" "shanty" "hauling song" "work rhythm"; do
  grep -rIn -i -F -E "$p" corpus/knowledge | grep -E '^[^:]+:[0-9]+:#' | wc -l
done
```

rc = 0 for the pipeline; **0 heading hits for each of the six phrases** (6 × 0).

```
for p in ...; do grep -rI -i -F -- "- topic:" corpus/knowledge | grep -c -i -F -- "$p"; done
```

rc = 0; **0 topic-line hits for each of the six phrases** (6 × 0).

```
grep -rIl -i -F "work song" corpus/knowledge
```

rc = 0; exactly **4 files**: `civilizations/balts.md`, `culture-material/material-culture-inference-method.md`,
`linguistics/funerary-lament-dirge-formulae.md`, `linguistics/lullaby-child-song-formulae.md`.
This reproduces claim C's own `before` clause ("'work song' appears only in prose of 4 knowledge files").

```
grep -rIn -i -w -E 'shanty|shanties' corpus/knowledge
```

**rc = 1** (no match). The token *shanty* is absent from the whole knowledge corpus today, in
any spelling. So is `hauling song`, `song leader`, `work rhythm`, `call and response` as a phrase.

**Verdict: the surface is unowned at base.** C8 passes by construction today, and the new entry
is the only file that may add an owner. Registry side agrees: `corpus/SOURCES.md` has 941 rows,
highest **S1017**, and no row's `teaches`/`scope` cell mentions work song, shanty, chantey,
call-and-response or hauling (grep rc = 0; the only `labour` hits are S032/S034 division-of-labour
and S618 birthing girdle, S856 labouring-folk — all unrelated).

---

## 2. Hit classification

Owner = topic line or heading. Substantive = a section or table row that argues the point.
Passing = one clause that mentions it in service of something else.

| # | file:line | class | the line, and what it is doing |
|---|---|---|---|
| 1 | `civilizations/balts.md:165` | passing (method directive) | "Couple work songs to a validated production chain" — an application bullet in the Baltic lyric-evidence section. It *asks for* the coupling the new entry supplies; it owns no work-song content. |
| 2 | `civilizations/maori.md:52` | passing (different domain) | karanga row: "Formal call and response in encounters such as pōwhiri". Encounter ritual, not labour. The new entry must scope "call and response" to work and leave this sense alone. |
| 3 | `civilizations/mississippian.md:145` | passing (arithmetic) | "at an invented 30 loaded trips per hauling day" — hauling as logistics, no song. No boundary needed. |
| 4 | `culture-material/material-culture-inference-method.md:15` | passing (routing pointer) | couples list: "linguistics/orality-formulaic-language (work songs, maker formulas, epic object biographies)". This is the stale routing: it sends work songs to the formula entry. The new entry supersedes the routing one-way from its own `- couples:` line; **do not edit this sibling**. |
| 5 | `linguistics/funerary-lament-dirge-formulae.md:129` | substantive (genre test) | "A lament refrain that is *too* singable … will be mistaken for a work song or a lullaby." A negative test the new entry must not restate. |
| 6 | `linguistics/funerary-lament-dirge-formulae.md:206` | substantive (table row) | performance-structure row: "antiphonal between two groups; a solo with a ritual answering chorus". Antiphony owned as *mourning* structure. |
| 7 | `linguistics/funerary-lament-dirge-formulae.md:245` | substantive (checklist) | "A mourning register that reproduces … its work-song logic has been copied rather than designed." Confirms work-song logic is a known other-register. |
| 8 | `linguistics/lullaby-child-song-formulae.md:193` | substantive (repertoire graph) | "a tune from a work song can be reused for a lullaby … the repertoire is therefore a graph of tunes". The clearest invitation: the lullaby entry already treats the work song as a graph node it does not own. |
| 9 | `linguistics/lullaby-child-song-formulae.md:245` | substantive (decision-table cell) | "the second makes it a work-song with a fixed duration" — work-song named as a *function option* of a lullaby. |
| 10 | `linguistics/lullaby-child-song-formulae.md:253` | substantive (decision-table cell) | "a tune shared with a work song or a dance" — the carrier row. |
| 11 | `linguistics/lullaby-child-song-formulae.md:285` | substantive (worked example) | "*Oren tal* shares its tune with a Tavrin boat-work song" — a NON-CANON boat-work song exists in the corpus as a named but unowned object. |
| 12 | `linguistics/verbal-duelling-ritual-insult.md:52` | passing (frame inventory) | "the challenge, the call-and-response, the naming of the sides" — one item in the duel-opening formula. |

Adjacent hits that the six-phrase sweep did **not** catch but that a designer will hit, found by
the broader `song|sing|chant|rhythm|refrain|verse|improvis` sweep (rc = 0, 301 lines over
`linguistics/` + `culture-material/`):

| file:line | what it is | why it matters |
|---|---|---|
| `culture-material/timekeeping-instruments.md:64` | table row "market and work bells — opening, closing, and **the rhythm of labor**" | the nearest collision on *work rhythm*: bells pace labour by clock, songs pace it by task. Must be stated. |
| `culture-material/cuisine-food-lexicon.md:68` | "brewing hymns = recipes in verse; a recipe is a song (kotodama hook)" | verse that carries a *procedure*, not a beat. The new entry must separate "song that times the task" from "song that stores the recipe". |
| `culture-material/trade-economy-lexicon.md:104,164` | "auction chant ('going once…')" as part of the bargain grammar | an occupational chant of a trade, owned as market register. Point at it, do not absorb it. |
| `culture-material/games-play-sport-contests.md:62,64,96,116` | singing games, counting-out formulas; `:116` defers music to `music-instrument-lexicon.md` | children's repertoire, not labour. |
| `culture-material/adornment-body-codes.md:29,36` | "chant protocol" of Samoan *tufuga* tattooing | craft-rite chant: rite, not labour timing. |
| `linguistics/sacred-registers-liturgical-language.md:101-107` | §6 "Recitation norms and chant" | owns **chant** as liturgical recitation norm. The frozen topic says "labour chant"; this is the sharpest lexical collision after *work rhythm*. |

---

## 3. Adjacency table — the boundary each neighbour imposes

Read these before writing; each row is "what it owns (read, not restated)" → "the sentence the new
entry owes it". Anchors are line numbers at base.

| neighbour (anchor) | what it owns | boundary the new entry must respect |
|---|---|---|
| `linguistics/orality-formulaic-language.md:30-37,99-129,151-153` | the Parry–Lord formula/type-scene/meter machinery, performer licensing, the "broadcast layer" | borrow the vocabulary ("formula", "incremental repetition") in one clause and cite §1/§8; do **not** re-derive the engine or the meter table, and do not claim work song as oral epic. Correct the stale routing at `material-culture-inference-method.md:15` from the new entry's own couples line. |
| `linguistics/lullaby-child-song-formulae.md:14,172-199,245,253,285` | tune-as-carrier, the repertoire graph, the lullaby register, the carrier decision table | the new entry owns the **work-song side of the shared tune** (the boat-work song *Oren tal* borrows is exactly this entry's object). It must not restate the lullaby register, the twelve-row table, or the carrier rule; cite §7 and hand the tune to the music owner as §7 does. |
| `linguistics/funerary-lament-dirge-formulae.md:15-31,84-109,177-196` | antiphonal **lament** structure, the keener's office, the "too singable → mistaken for a work song" test | own antiphony as **labour coordination** (alternation that sets a pull), never as mourning; cite the genre-confusion test once, do not restate it; claim no keening, no mourning licence. |
| `linguistics/praise-poetry-panegyric.md:21-43,172-198` | praise as public speech act, the epithet, the singer's office, the Yoruba oríkì/drummer row (**the R99-M2 cell lives in §7**) | a work song may name a crew, a leader or a task; praise-as-institution, epithet economy and the drummer's assembly of titles stay there. The new entry must not restate oríkì and must not build a second praise table. |
| `linguistics/verbal-duelling-ritual-insult.md:18-32,91-109` | the song duel as an **adjudicated contest** (boast/taunt/riposte, audience verdict, juridical instrument) | the work song's complaint and satire have **no adjudicating audience and no stake**. State it: "a work song that satirises the overseer is not a song duel — nobody wins and nothing is settled." Contest-carried-by-tune stays there. |
| `linguistics/sacred-registers-liturgical-language.md:101-107` | **chant** as an enforced recitation norm, invariance-as-authority, the six competences | "labour chant" has no doctrine, no institution and no invariant target: it is task-bound, improvised at the verse level, and its correctness is *whether the work goes right*. Cite §6 and stop. |
| `linguistics/toast-drinking-speech-formulae.md:21-38` | the cup-borne speech act, the toastmaster, the three order rules | a song sung at a shared cup is not a toast; cite the three order rules as a general principle if needed, do not relabel a toast table. |
| `linguistics/speech-surrogates-whistled-drummed.md:14-48` | channel design: what a whistle/drum carries, who may use the channel | a drummed work signal is a surrogate channel, owned there; the new entry takes **sung text** only. |
| `culture-material/music-instrument-lexicon.md:72-80,113-124` | organology, melody, ceremonial registers, instrument naming, the music–myth slot | the new entry owns **no melody, no instrument, no scale**; it owns text + task-rhythm coupling and hands contour/tempo/timbre to the music owner exactly as `lullaby:172-176` does. |
| `culture-material/dance-performance-movement-codes.md:53-63` | the dance–song–voice triad and procession registers | movement is theirs; a work beat is not a dance beat unless the culture explicitly couples them (then cite the coupling section). |
| `culture-material/maritime-seafaring-lexicon.md:22-32,54-57` | the hull's **working register**: one command set, the wage cycle ("working up the dead horse", S899), and *who times the work*; its §2 decision row already reads "the songs that pace shared labour" | **closest material-culture collision.** Maritime names the songs in one decision row and owns commands + pay cycle; the new entry owns the songs themselves. Cite `:29` one-way and say so in the boundary table. |
| `culture-material/agrarian-field-system-lexicon.md:13-33,35-48,50-67` | field typology, the labour calendar, cooperative-labour words, the harvest claim | take the **peak-labour month** as an input; do not restate field systems, tenure, rotation or the labour calendar. The entry owns only the song that times the peak. |
| `culture-material/craft-artisan-lexicon.md:17-22,125-137` | the workshop as a speech community, tool lexicon, guild ladder, marks, craft rites | craft **song text** is the new entry's; tool names, ranks and the quality formula stay there. |
| `culture-material/timekeeping-instruments.md:58-70` | bells that pace labour by clock; hour-wages | clock time is theirs; the new entry's "work rhythm" is *task*-derived, not clock-derived, and the two can disagree (a design lever, not a restatement). |
| `culture-material/cuisine-food-lexicon.md:66-70` | brewing hymns as recipe-in-verse | separate "song that times the task" from "song that stores the procedure"; cite, do not absorb. |
| `culture-material/trade-economy-lexicon.md:102-106,161-164` | auction chant inside the bargain grammar | occupational chant of a market trade stays there; the new entry may cite it as one occupational case. |
| `culture-material/games-play-sport-contests.md:62-116` | singing games, counting-out formulas, children's repertoire | not labour; do not fold children's work-play into the work song without saying which it is. |
| `civilizations/maori.md:52` | karanga, call-and-response **of encounter** | scope the phrase to labour and name this other sense as not-here. |
| `civilizations/balts.md:165` | the directive "couple work songs to a validated production chain" | the new entry is the answer to that directive; do not restate Baltic lyric evidence. |

Non-edit note: `material-culture-inference-method.md:15` will keep routing "work songs" to
orality after this round. That is accepted — the item forbids editing siblings, and the new
entry's `- couples:` line is the forward pointer. Record it in the entry's limits section so the
next reader sees the stale route is known.

---

## 4. Skeleton, and where the six frozen phrases land

C1 mechanics (`predispatch.py:336-372`): ≥ 12000 **bytes**; ≥ 6 lines starting `## `; one table
with ≥ 5 data rows × ≥ 3 columns; ≥ 4 of the six phrases found by *normalised containment*
(`norm()` = lowercase, every non-alphanumeric run → one space, `:99-100`) either in the joined
h2 headings or anywhere in a table data row; the `- topic:` line byte-equal to the frozen topic.

Because `norm()` maps `-` to a space, `work-song` matches `work song` and `call-and-response`
matches `call and response`. `shanty` does **not** match `shanties` under containment — use the
singular token somewhere in a heading or table row.

Proposed h2 set (11 sections; all six phrases are headings, giving 6/6 with margin over the
required 4):

| § | heading | frozen phrase carried |
|---|---|---|
| 1 | `## 1. Scope: the work-song surface this entry owns, and the neighbours it defers` | **work song** |
| 2 | `## 2. The task sets the metre: work rhythm and the labour it times` | **work rhythm** |
| 3 | `## 3. The song leader: who starts, who may change it, who is paid` | **song leader** |
| 4 | `## 4. Call and response: the coordination grammar` | **call and response** |
| 5 | `## 5. The repertories: hauling song, rowing song, pounding song, field and craft song` | **hauling song** |
| 6 | `## 6. The shanty: the occupational repertoire and its afterlife` | **shanty** |
| 7 | `## 7. Improvised verses, complaint and satire licensed by the work` | — (topic-line clause) |
| 8 | `## 8. Decision table for a fictional work-song tradition` | **work song** (repeat) |
| 9 | `## 9. A worked design example (NON-CANON)` | — |
| 10 | `## 10. Error patterns: songs that leave their task` | — |
| 11 | `## 11. Limits, calibration and the handoff to the lore world bible` | — |

Content plan per section, so the entry is a design surface and not a survey:

- **§1** boundary table, 13 rows × 3 cols (`neighbour (anchor)` | `what it owns` | `this entry's
  boundary`), lifted from §3 above. This is the ≥5×≥3 table; a second table follows in §2.
- **§2** the coupling claim: the task fixes the beat (pull, stroke, strike, stride, throw), the
  song supplies the count, the breath and the warning. Table: `task` | `body action` | `what the
  song must supply` | `failure if mismatched` (5+ rows: hauling, rowing, pounding, field, craft).
  State the clock-vs-task disagreement against `timekeeping-instruments.md:64`.
- **§3** the leader as an office: recruitment, licence, what the call inventory contains (count,
  warning, name, joke), what happens when the leader is absent (the work slows or a substitute
  counts), who may change a verse. Couples `praise-poetry:69` for office/patronage machinery
  (cited, not restated).
- **§4** alternation types (solo–chorus, solo–solo, chorus–solo, overlap), what the answer
  carries (confirmation, next instruction, complaint), and why the form distributes attention
  rather than decorating. One paragraph must fence off the karanga sense (`maori.md:52`).
- **§5** per-task repertoire: hauling song, rowing song, pounding song, field song, craft song —
  what each task demands of the text, and the one design rule per row.
- **§6** the shanty as a *named* occupational genre: its work types, its verse economy, its death
  when the task dies, and its revival as performance. The design question: what does a fictional
  culture call the genre, and who owns the name after the trade is gone.
- **§7** the licence the work grants: complaint, satire, the overseer, the taboo that the song may
  break and speech may not. Boundary sentence against song duels
  (`verbal-duelling-ritual-insult.md:91-109`) and against binding speech/curse
  (`oath-blessing-curse-formulae.md`).
- **§8** decision table, 10–12 rows × 5 cols (`decision` | `options` | `what each option gives` |
  `what it costs` | `status`), in the house style of `lullaby:239-260` and `funerary:197-220`.
- **§9** NON-CANON worked example: one crew, one task, one leader, one song, one failure.
- **§10** 6–8 numbered error patterns (song that outruns the task; song that is a performance;
  leaderless repertoire; shanty revival that forgets the work; satire with no licence; clock
  replacing task; a song that fits every task and therefore none).
- **§11** limits + `to-verify` + handoff to lore-shokunin under
  `synthesis/worldbible-integration-contract.md`; carry the stale-routing note.

Header fields to mirror `lullaby-child-song-formulae.md:1-13`: `# title`, `- topic:` (frozen,
byte-equal), `- sources:` (the ≥4 new S1018+ ids), `- verified-at: 2026-11-06`, `- recheck: 180d`,
`- couples:` (one parenthetical per neighbour saying what is borrowed vs deferred), `- scope:`
reference/method only, non-canon.

The frozen topic line the entry and the README row must both carry, byte-for-byte
(**442 bytes / 440 chars, 1 × U+2014 em dash, 2 straight apostrophes, 4 semicolons** — no curly
quotes):

```
- topic: work song and labour chant: song that times and coordinates shared labour — the song leader's call and the crew's response; hauling, rowing, pounding, field and craft songs and how their rhythm fits the task; the shanty and other occupational repertories; improvised verses, complaint and satire licensed by the work; and the design procedure for a fictional work-song tradition whose songs stay tied to their task, crew, leader and setting
```

---

## 5. Partition counts and why `linguistics/`

```
find /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/knowledge -name '*.md' \
  | awk -F/ '{print $(NF-1)}' | sort | uniq -c | sort -rn
```

rc = 0:

```
95 civilizations
44 linguistics
43 culture-material
36 myth-symbol
29 synthesis
24 verification
```

Total 271 files, matching `corpus/README.md`'s live footer (`total 271 files; directory totals
44/36/43/29/24/95`) and `find corpus/knowledge -name '*.md' | wc -l` = 271 (rc 0).

Why `linguistics/`:

1. **The surface is verbal art, not material culture.** The claim is about the *text* that times
   labour — who calls, who answers, what the verses may say. The corpus already partitions song
   *text* into linguistics and song *sound* into culture-material: `music-instrument-lexicon.md`
   owns organology, melody and ceremonial registers; `dance-performance-movement-codes.md` owns
   movement. Both are the entries the new one must defer to, which is only coherent if the new
   entry sits on the text side.
2. **Every sibling register of the same kind is in linguistics.** 13 linguistics entries carry
   song/sing/chant in their topic line
   (`grep -l -i -E '^- topic:.*(song|sing|chant)' corpus/knowledge/linguistics/*.md | wc -l` → 13,
   rc 0), including all six near neighbours: `lullaby-child-song-formulae`,
   `funerary-lament-dirge-formulae`, `praise-poetry-panegyric`, `verbal-duelling-ritual-insult`,
   `orality-formulaic-language`, `sacred-registers-liturgical-language`. The work song is the
   missing member of that set, not a member of any other set.
3. **The two material-culture entries that touch it own the surrounding institution, not the
   genre.** `maritime-seafaring-lexicon.md` owns the hull's working register (commands, wage
   cycle) and only *names* "the songs that pace shared labour" in a decision row;
   `agrarian-field-system-lexicon.md` owns the labour calendar and field typology. A new entry in
   culture-material would have to re-own one of those; in linguistics it owns only the song.
4. **`civilizations/` is single-tradition scope** (95 entries, one people each). The new entry is
   comparative method plus a design procedure, which is the linguistics partition's shape.
5. **Census arithmetic is cheap and honest here.** linguistics goes 44 → 45, total 271 → 272; the
   `## linguistics/ (44)` header, the totals line and the dated footer all move by one, which is
   the smallest possible index delta.

---

## 6. Planning data-walk: contract mechanics the executor will otherwise trip on

These are read off the frozen counter and the index tool; they are the legs most likely to fail
for a reason unrelated to the writing.

1. **C5 is not automatic — `corpus/README.md` must be edited, and the row topic must be
   byte-equal to the entry's `- topic:`.** `tools/check-corpus-index.py:77` reads
   `corpus/README.md` (not `corpus/knowledge/README.md`, which does not exist). It parses
   `- \`file.md\` — <topic>` rows (`ROW_RE`, `:30`) and compares `<topic>` to the entry's
   `- topic:` value after whitespace collapsing (`:120-135`, `TOPIC_MISMATCH`). Verified on a
   live sibling: the lullaby row and the lullaby topic line are equal, 277 chars each (python
   compare rc 0). **So the README row must repeat the whole 440-char frozen topic**, not a
   summary.
2. **Three count sites move together.** `## linguistics/ (44)` → `(45)` (`HEADER_DRIFT` compares
   declared to the live directory count, `:136-138`); a new **appended** footer block
   `Total knowledge entries: 272.` + `Counts checked 2026-11-06 from the repo root:` +
   `` `python3 -B tools/check-corpus-index.py --root .` `` +
   `(total 272 files; directory totals 45/36/43/29/24/95).` — `TOTALS_RE` takes the **last**
   match (`:140-146`) and `FOOTER_RE` takes the **last** header block (`:147-165`), so appending
   is the correct move and older blocks stay untouched.
3. **C8 does not see `corpus/README.md`.** `tree_knowledge()` walks only `corpus/knowledge`
   (`:147-155`), so the README row carrying all six frozen phrases creates no owner. Had the
   index lived under `corpus/knowledge/`, C8 would have failed on the index row itself.
4. **C1 counts bytes, not characters.** `size = len(raw.encode('utf-8'))` (`:344`); the em dash
   costs 3 bytes. 12000 bytes ≈ 11.7k characters of prose with em dashes.
5. **C1 phrase matching is normalised containment, h2 only.** `heads = [l for l in
   raw.splitlines() if l.startswith('## ')]` (`:345`) — `###` does not count, and a phrase split
   across a line break in a table row will not match.
6. **C2 row shape is exactly 11 cells** (`:397-400`): id, source, kind, tier, scope, anchor,
   teaches, status, opened, recheck, used-by. `used-by` must be exactly
   `corpus/knowledge/linguistics/work-song-labour-chant.md` (single path, no trailing comma, no
   second entry), `tier` ∈ {A,B}, `status` = `mined`, `opened` ∈ {2026-11-06, 2026-11-07}.
7. **C7 manifest schema** (`:478-535`): a JSON **list** of objects
   `{id, captures:[{file, sha256}], quote, quote_capture}`; `file` and `quote_capture` are
   **basenames inside `reports/round-100/evidence/`** (a `/` disqualifies them); `quote` is 1–25
   words after whitespace collapse, must occur **exactly once** in the collapsed capture text,
   and must be a substring of the registry row's `anchor` cell (cell index 5).
8. **C6** requires every qualifying id to be cited inside the entry, so the `- sources:` list and
   at least one in-text `(S10xx)` per id are both needed.

---

## 7. Files read

Linguistics: `orality-formulaic-language.md` (1-29, 30-72, 99-172), `lullaby-child-song-formulae.md`
(1-13, 1-28, 172-205, 237-290, 291-317), `funerary-lament-dirge-formulae.md` (15-32, 177-196,
headings), `praise-poetry-panegyric.md` (21-43, 172-198, headings),
`verbal-duelling-ritual-insult.md` (18-32, 91-109, headings), `toast-drinking-speech-formulae.md`
(21-38, headings), `speech-surrogates-whistled-drummed.md` (14-48, headings),
`sacred-registers-liturgical-language.md` (1-30, 101-116, headings), `numerals-and-measures.md:91`,
`politeness-taboo-euphemism.md:88`, `linguistic-anthropology.md` (headings).

Culture-material: `music-instrument-lexicon.md` (72-124, headings),
`dance-performance-movement-codes.md` (53-76, headings), `craft-artisan-lexicon.md` (17-22,
125-154, headings), `agrarian-field-system-lexicon.md` (13-50, headings),
`maritime-seafaring-lexicon.md` (12-32, 54-63, headings), `textile-technology.md` (headings),
`timekeeping-instruments.md` (58-70), `cuisine-food-lexicon.md` (66-70),
`trade-economy-lexicon.md` (102-106), `games-play-sport-contests.md` (62-116, grep),
`adornment-body-codes.md` (29-39, grep), `material-culture-inference-method.md:15`.

Civilizations: `balts.md` (160-170), `maori.md:52`, `mississippian.md:145`.

Lane machinery: `corpus/SOURCES.md` (header, registry shape, row count, highest id, adjacent-row
grep), `corpus/README.md` (section headers, totals, footers, lullaby row),
`reports/round-100/claims.json` (claim C), `reports/round-100/predispatch.py`
(header 1-47, `norm`/`PHRASES` 65-100, `tree_knowledge` 147-155, C1 336-372, C2 374-410,
C7 478-535, C8 540-546), `tools/check-corpus-index.py` (77-190).

---

## 8. Confidence and remaining unknowns

- **High confidence (observed, re-runnable):** the surface is unowned (0 heading owners, 0 topic
  owners, `shanty` absent rc 1); the 12 real prose hits and their classification; the partition
  counts; the C1/C2/C5/C7/C8 mechanics above; the README row must equal the topic byte-for-byte
  (proved on the lullaby pair).
- **Inference, marked:** that a 13-row boundary table plus the §2 task table will clear 12000
  bytes comfortably — a comparable entry (`lullaby-child-song-formulae.md`, 317 lines) is well
  over it, but the executor should measure `wc -c` before declaring C1.
- **Unknown / not scouted:** which four sources the miner will open (S1018+), and therefore
  whether the ≥4 qualifying rows can all reach tier A/B on one day's opening. That is the
  Miner/Scribe leg, not this one; the risk is source availability, not surface availability.
- **Deliberate non-action:** no sibling file was edited, including
  `material-culture-inference-method.md:15`, whose work-song routing is now stale by design.
