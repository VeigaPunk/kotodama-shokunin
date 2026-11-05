# ScoutSurface96 — coverage surface and adjacency map for claim C

Round 96, attempt 1. Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Base `0539276c0e329743200b60e98bf289c540f78864`; freeze `deca7e6fff988061f01bfc501a91e18fca892822`;
correction `063f70c9ab9aed5297741773292ded6d713d537a`.
Seat is read-only on the lane repo: nothing in `kotodama-shokunin/` was created or edited by this seat.

Frozen artifacts read first (not edited):
- `reports/round-96/claims.json` — claims O and C; frozen topic, phrases, thresholds.
- `reports/round-96/predispatch.py` — the frozen counter (legs C1–C7 measured against it below).
- `reports/round-96/predispatch-base.txt` — do-nothing control, `PREDISPATCH-96: FAIL legs=3/12`.

Axes for this seat: **coverage** (zero-owner proof), **adjacency** (neighbour boundaries),
**structure** (skeleton and phrase landing), **census** (partition placement).

---

## 1. Zero owned file at base — evidence

All commands run from the lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.

| # | Command | rc | Result |
|---|---|---|---|
| 1 | `ls corpus/knowledge/*/ \| grep -i -E 'oath\|curse\|bless\|malediction\|imprecat\|vow\|swear\|sanction\|witness'` | 1 | no output — zero matching filenames |
| 2 | `find corpus/knowledge -type f \( -iname '*oath*' -o -iname '*curse*' -o -iname '*bless*' -o -iname '*maledict*' -o -iname '*imprecat*' -o -iname '*vow*' -o -iname '*swear*' -o -iname '*sanction*' -o -iname '*witness*' \) -print` | 0 | no output — zero matching files anywhere under `corpus/knowledge/` |
| 3 | `git ls-tree -r --name-only 0539276c0e329743200b60e98bf289c540f78864 corpus/knowledge \| grep -i -E 'oath\|curse\|bless\|malediction\|imprecat\|vow\|swear\|sanction\|witness'` | 1 | no output — zero matching filenames **at the base commit itself** |
| 4 | `find corpus/knowledge -name '*.md' \| wc -l` | 0 | 267 (worktree) |
| 5 | `git ls-tree -r --name-only 0539276c... corpus/knowledge \| wc -l` | 0 | 267 (base tree) |
| 6 | `find corpus/knowledge -name '*.md' \| awk -F/ '{print $3}' \| sort \| uniq -c` | 0 | see §5 |
| 7 | `git ls-tree -r --name-only 0539276c... corpus/knowledge/linguistics \| wc -l` | 0 | 40 |

Command 1 output in full (the `ls` listing was truncated by the tool at 768 B; the grep filter itself
returned nothing):

```
RC=1
```

**Conclusion: the claim C "before" state holds — zero owned knowledge file at base.** The
round-95 lesson's filename sweep (`corpus/lessons/round-90.md:80-90`, the precedent for this move:
"The C claim is a coverage move on ground the coverage map did not hold… no knowledge filename
carried prayer|petition|votive|supplicat") is reproduced here with the oath/curse/blessing
vocabulary.

### Coverage map (`corpus/README.md`) — per-term grep

`grep -n -i -E '<term>' corpus/README.md` (rc=0 for every term with hits, rc=1 for zero-hit terms):

| Term | matches | rc | Lines |
|---|---|---|---|
| `oath` | 6 | 0 | 408, 431, 624, 873, 875, 876 |
| `curse` | 2 | 0 | 408, 449 |
| `blessing` | 2 | 0 | 408, 536 |
| `malediction` | 0 | 1 | — |
| `imprecation` | 1 | 0 | 408 |
| `swearing` | 0 | 1 | — |
| `vow` | 3 | 0 | 385, 460, 970 |

Every hit is inside an existing entry's one-line index description, never a dedicated row.
Line 408 is the `myth-symbol/binding-speech-complex.md` row (the one entry that already covers
the surface as a *myth-side machinery*); line 385 is `petitionary-and-votive-formulae.md`
(the conditional vow); 970 is the round-90 footer block repeating line 385's text.

The `## Known gaps (frontier)` section (README lines 638–817) contains **zero** hits for the
surface vocabulary: `awk 'NR>=638 && NR<=817' corpus/README.md | grep -c -i -E 'oath|curse|blessing|malediction|imprecation|\bvow\b|swear'`
→ `0`, rc=1. So the gap list neither claims nor forecloses this surface.

The registry's teaching cells (the third surface named in the task) also carry no owner:
a Python scan of all 898 parsed `corpus/SOURCES.md` rows for the same vocabulary in the
`teaches` cell returns **6 hits, none of them an owning row** —
S839, S840 (`hair-grooming-codes.md`, Nazirite vow), S901, S902 (`ordeal-judicial-proof-rituals.md`),
S945 (`petitionary-and-votive-formulae.md`, vocative), S950 (a round-90 *rejection* row).

---

## 2. Files that touch the surface in title / topic line / teaches cell

Nine files carry the vocabulary in their `- topic:` line. Full topic text was extracted with the
index checker's own regex (`^- topic:(.*?)(?=\n- \w)`, `re.M|re.S`), so these are the exact strings the
index tool compares against the README row.

| File (partition) | Topic line (abridged; full text read from disk) | Owns the surface? |
|---|---|---|
| `myth-symbol/binding-speech-complex.md` | "the binding-speech complex as a designed system for a fictional culture — the four channels (oath, curse, blessing, name-power) treated as one machinery with four directions of binding… the oath in depth (formula anatomy: invocation / assertion / self-imprecation / uptake…)…" | **Owns the machinery.** This is the near-twin of the new entry. |
| `linguistics/petitionary-and-votive-formulae.md` | "petitionary address and votive formulae: vocative address to deities, petition mood (imperative, optative, precative), **the conditional vow**, votive inscription grammar, prayer-register archaism and parallelism, design procedure and failure modes" | Touches only: the votive/conditional vow (promise-to-god), not the oath/curse/blessing formula grammar. |
| `myth-symbol/ordeal-judicial-proof-rituals.md` | "judicial proof as a ritual system… the proof ladder (vindicatory oath → compurgation → ordeal → judicial battle)…" | Touches only: oath as *proof evidence*. |
| `myth-symbol/guest-right-hospitality-law.md` | "guest-right and hospitality as a *sacral-legal institution*… the seal families (**oath by a god** / material token / shared meal / hand-clasp…)" | Touches only: oath as one seal among five. |
| `myth-symbol/witchcraft-sorcery-accusation-institution.md` | "witchcraft and sorcery as an **accusation institution**… the proof technology (**oath-compurgation**, ordeal, oracle…)" | Touches only: oath inside a proof ladder. |
| `myth-symbol/sacred-kingship-mythic-charter.md` | "…(the word 'oath' appears in the topic line, in the legitimation-channel list)…" | Touches only: oath as a royal legitimation channel. |
| `civilizations/scythian-saka.md` | "Evidence-calibrated coupling of language, myth, **oath**, animal imagery, period, and costume across Pontic Scythian…" | Touches only: a civilization frame. |
| `culture-material/craft-artisan-lexicon.md` | "…the sumitsubo 'ink-pot'… **build-curses**…" | False positive: "build-curses" is the joiner's curse tool, not a curse formula. |
| `culture-material/hair-grooming-codes.md` | "…tonsures and uncut-hair **vows**, royal and state hair edicts…" | Touches only: vow as a hair-status marker. |
| `verification/verification-independence-anti-circularity.md` | "…the circularity modes… ('**bless**-the-tamper' re-pins…)" | False positive: "bless" as in "bless the tamper", not a blessing formula. |

Files with a surface term in the **title** (filename): **none** — see §1 command 1 (rc=1).
Files with a surface term in a **teaches cell**: the 6 registry rows listed in §1, none owning.

So: **no file owns the oath/curse/blessing formula-grammar surface.**
`myth-symbol/binding-speech-complex.md` is the only file that owns *binding speech* — but it owns
it as myth-side machinery (enforcement ledger, executor doctrine, seven curse genres, release
procedures), not as the linguistic formula grammar of the six frozen phrases.

---

## 3. Adjacency table — owners, touch ranges, and the boundary to respect

| Adjacent owner | Touch range (line numbers in that file) | What it owns | Boundary the new entry must respect |
|---|---|---|---|
| `myth-symbol/binding-speech-complex.md` | §4 oath 99–139; §5 curse 140–167; §6 blessing 168–179; §7 name-power 180–195; §8 enforcement ledger 196–219; §9 release 220–235; §3 master channel table 85–98; §1 boundary table 39–59; §14 canon boundary 301–305 | the four-channel machinery, the binding triangle, the **executor doctrine** (line 62: "a word holds only where an executor exists"), the four enforcement models, the curse dials, the blessing asymmetry, the release taxonomy | **Defer, do not restate.** The new entry owns the *formula grammar* (how the words are built and parsed); this entry owns *who executes and what happens*. Cite `binding-speech-complex.md` by path for the machinery; do not re-table the four channels, the enforcement models, the seven curse genres or the release taxonomy. It sits in `myth-symbol/`; the new entry sits in `linguistics/` — different partitions, so the deferral is natural. |
| `linguistics/register-strata-attestation.md` | header/`gap filled` line 3; couples line 25; §2 table rows 58, 68–69; §4 example 88; law rows 134–136; 195; 204 (`QREG-06` attested oath); 230–236; 265; 373 | the **register law**: who may speak an attested oath, and what record consequence follows | The register law owns *licensing* (which register, which speaker, what record). The new entry owns the *formula parts* (invoked witness, conditional sanction, self-imprecation, performative verb). Do not restate `QREG-01..RGL-05` or the in-register/stamp-holder machinery. |
| `linguistics/sacred-registers-liturgical-language.md` | §1 ownership table 26–40; §7 item 2 line 113 ("Liturgical force is not attestation force"); item 3 line 115 (divine-name avoidance routed out) | the sacred register system: the H/L specialization, six competences, liturgical fossilization, closure devices | The new entry's "sacred register" row must **name** this owner and defer the register system itself. Note the warning at line 113: liturgical force ≠ attestation force — the new entry must not blur them either. |
| `linguistics/politeness-taboo-euphemism.md` | 75 (taboo domain: "sacred words (gods, **oath formulas** — couples myth-symbol)"); 78 (swearing calibration); 102 (**minced oaths**); 106 (design rule: minced oath per taboo seed); 115 (coronation-oath stress scene) | taboo domains and sanctions, the euphemism treadmill, **minced oaths** as a taboo-stratum fossil | Only touch: the *lexical* register of oath fragments. The new entry owns the formula grammar; do not re-table taboo domains or euphemism ladders. Note line 75 already routes "oath formulas" to myth-symbol — the new entry's cousins are the linguistic-side cousin. |
| `linguistics/taboo-strata-lifecycle.md` | 14 (registers `Swearing` at `politeness-taboo-euphemism.md:34`) | the lexical form-history of a forbidden word | No touch on oath/curse/blessing formulas (grep count 0 for the surface vocabulary in the body beyond line 14). Defer entirely. |
| `linguistics/naming-systems.md` | §4 theonymy 73–79; §6 name taboo and name magic 87–108; line 105 ("Kotodama proper (言霊…): the belief that spoken words carry spirit-power to **bless, curse**, and actualize") | the **name** system: anthroponymy, toponymy, theonymy, name taboo, name magic | The new entry may *invoke* a divine name as a witness, but the derivation and avoidance of that name is `naming-systems.md`'s. Do not restate theonymy or the name-magic table. `binding-speech-complex.md` §1 already fixed this boundary ("the *name system* … this entry takes the *narrative* uses of name-power"). |
| `linguistics/semantics-pragmatics.md` | 94 (the Searle table row: "commissives \| promise, vow \| **oath formulae with self-curse clauses**") | speech-act classification (Austin/Searle five classes) | The new entry builds on the commissive row; it does not re-teach the five-class taxonomy. The frozen phrase "self-imprecation" is the linguistic name for what this row calls "self-curse clauses" — say that once, then move on. |
| `linguistics/kinship-terminology.md` | **0 hits** for the surface vocabulary (`grep -c` → 0, rc=1) | kinship systems | No boundary needed. The new entry may use kinship as one *ground* for a curse's legitimacy (the way `binding-speech-complex.md:166` does), but must not teach kinship terminology. |
| `culture-material/sumptuary-law-rank-display.md` | **0 hits** for the surface vocabulary (`grep -c` → 0, rc=1) | rank display law | No boundary needed. Sanction in this file is a dress penalty, not a sanction clause. |
| `myth-symbol/ordeal-judicial-proof-rituals.md` | 3, 6, 7, 14, 25–26, 70–71, 148 | the proof ladder (oath → compurgation → ordeal) | Touches the oath only as *proof*. The new entry owns the formula; this owns what happens when the oath stops being enough. Its line 6 already defers to `binding-speech-complex.md` for the oath as speech act. |
| `myth-symbol/guest-right-hospitality-law.md` | 16, 34–35, 101, 119 | the seal families of guest-right | Oath is one of five seals. Defer. |
| `myth-symbol/witchcraft-sorcery-accusation-institution.md` | 3, 6, 17, 34, 70–71, 148 | the accusation institution | Line 17 already states: "`binding-speech-complex.md` — owns the oath, the curse, the blessing, name-power and the enforcement ledger." Defer entirely. |
| `myth-symbol/ritual-liminality.md` | 33 (guild/craft table: apprenticeship under oath); 112 (ritual language is performative) | the rite as the unit | The new entry takes the *utterance* as the unit. Cite 112 for performativity; do not re-table sacrifice or calendrical ritual. |
| `myth-symbol/creation-myths-taxonomy.md` | 104 (the language-coupling checklist naming oath forms as mini-creations) | creation myth taxonomy | One-line cite only. |
| `synthesis/religion-language-co-evolution.md` | 36 (register table row) | the workflow of religion and language | One-line cite only. |

**No contested scope** — every neighbour above has an explicit existing deferral line or owns a
disjoint object. The only genuinely close pair is `myth-symbol/binding-speech-complex.md`, and the
split is clean: *grammar vs. enforcement*.

---

## 4. Section skeleton for the new entry (six or more h2) and phrase landing

The counter's C1 leg measures: bytes ≥ 12000; h2 count ≥ 6; a table with ≥ 5 data rows × ≥ 3 cols;
≥ 4 of the 6 frozen phrases present in h2 headings **or** table data cells; the topic line
byte-equal to `- topic: ` + the frozen topic (354 B as one line; the em dash is U+2014).

Frozen phrases: `oath formula`, `blessing formula`, `curse formula`, `self-imprecation`,
`witness invocation`, `sanction clause`.

Proposed skeleton (h2 headings numbered so the grader's `_content_toks` stripping sees ≥ 2 content
tokens after the number, and so the phrases land in **headings**, not only in cells):

```
# Oath, blessing and curse formulae: the performative word-acts that bind, bless or harm
   (header block: - topic: <frozen, byte-equal>; - sources:; - verified-at:; - recheck:;
    - couples: -> myth-symbol/binding-speech-complex.md, linguistics/register-strata-attestation.md,
    linguistics/sacred-registers-liturgical-language.md, linguistics/semantics-pragmatics.md,
    linguistics/politeness-taboo-euphemism.md, linguistics/naming-systems.md)

## 1. Scope: the formula grammar this entry owns, and the enforcement it defers
   -> boundary sentence naming binding-speech-complex.md as the machinery owner
   -> the six frozen phrases introduced in prose (all six natural)

## 2. The oath formula: invocation, assertion, self-imprecation, uptake
   -> "oath formula" lands here (h2)
   -> cites semantics-pragmatics.md:94 for the commissive class

## 3. The blessing formula: transfer, not wish
   -> "blessing formula" lands here (h2)

## 4. The curse formula: genres, cause grammar, release
   -> "curse formula" lands here (h2)

## 5. The witness invocation: who is called to hear, and what that costs
   -> "witness invocation" lands here (h2)

## 6. The sanction clause: the conditional penalty and its dials
   -> "sanction clause" lands here (h2)

## 7. Registers: sacred, legal, everyday
   -> three-row register table; names sacred-registers-liturgical-language.md and
      register-strata-attestation.md as owners; defers both

## 8. Master grammar table (the counter's table: >= 5 data rows x >= 3 cols)
   -> columns: Part | Function | Real form | Design question | Failure mode
   -> data rows: performative verb / invoked witness / conditional sanction /
      self-imprecation / uptake / release clause  (6 rows)
   -> cells carry "witness invocation", "self-imprecation", "sanction clause" so a phrase
      is present in a *cell* as well as in headings

## 9. Error patterns: the oath that binds nobody, the curse with no witness
   -> named failure modes

## 10. Design procedure and checklist for a fictional oath or curse system
   -> decision steps; the checklist
```

**Why this landing is safe against the counter and the grader.**
Measured on a synthetic entry in a scratch mirror (never in the lane repo):
- C1 measures `bytes`, `h2`, table shape, phrase hits, topic-line equality from the *raw file*;
  it counts an h2 only when the line starts with `## ` and a table row only after a
  `|---|---|` separator. My synthetic file returned `bytes=51952 h2=7 table=6x3 phrases=6/6 topic-line=equal`
  → `LEG C1 PASS` against the frozen counter.
- The grader's own TOPIC leg (v6, `tools/check-advance-evidence.py:646-723`) is stricter than the
  counter in one respect: the phrase anchors must **span ≥ 2 heading/table surfaces**
  (`min_anchor_span`), and a heading anchors only when it carries ≥ 2 content tokens after its
  leading number is stripped (`_content_toks`, v6 NUM1/RM1/NUM2). The skeleton above puts each
  frozen phrase in a numbered h2 that carries several content words, and repeats three of them in
  table cells — so both the counter and the grader's span rule are satisfied.
- `stem_words` from the filename (`oath`, `blessing`, `curse`, `formulae`, all ≥ 4 chars) must
  appear in the entry text (grader line 662); the skeleton names them in §1 and in headings.

**Two machine constraints the scribe must respect** (measured, not inferred):
1. The topic line must be exactly one line: `- topic: ` + frozen text (354 B). Multi-line topics
   break the counter's `tline == '- topic: ' + FROZEN_TOPIC` byte comparison.
2. The index checker compares the **README row text** to the **file's topic field** with
   `actual != topic` → `TOPIC_MISMATCH` (`tools/check-corpus-index.py:130-137`), and the README row
   is cut with `ROW_RE = ^- \`([^\`]+\.md)\` — (.*)$`. So the README row must carry the topic text
   **verbatim** after `— `, and it must be placed inside the `## linguistics/ (N)` span or it is
   filed as a supplemental row (still resolvable, but the section header count must still match).

---

## 5. Partition counts and placement

`find corpus/knowledge -name '*.md' | awk -F/ '{print $3}' | sort | uniq -c` (rc=0):

```
     95 civilizations
     43 culture-material
     40 linguistics
     36 myth-symbol
     29 synthesis
     24 verification
```

Total 267, equal to `find corpus/knowledge -name '*.md' | wc -l` (rc=0) and to
`git ls-tree -r --name-only 0539276c... corpus/knowledge | wc -l` (rc=0).

**The new entry belongs in `linguistics/`** (40 → 41). Reasons, each anchored:
1. The claim's frozen surface names the path: `corpus/knowledge/linguistics/oath-blessing-curse-formulae.md`
   (`reports/round-96/claims.json`, claim C `surface`; `reports/round-96/predispatch.py` `ENTRY_REL`).
2. The frozen topic is a *formula grammar*: "performative word-acts… the formula grammar (invoked
   witness, conditional sanction, self-imprecation, performative verb), registers (sacred, legal,
   everyday) and the design procedure". Formula-grammar reference knowledge is what this partition
   owns: the four sibling formula entries live here —
   `petitionary-and-votive-formulae.md` (round 90), `funerary-lament-dirge-formulae.md` (round 95),
   `greeting-leave-taking-formulae.md` (round 93), `lullaby-child-song-formulae.md` (round 94).
   `find corpus/knowledge -name '*formula*'` returns exactly those five linguistics files plus
   `orality-formulaic-language.md`.
3. `myth-symbol/` (36) already holds `binding-speech-complex.md`, the enforcement-side owner.
   Placing the grammar entry in the same partition would put the two halves of one surface in one
   partition and invite the restatement the deferral is meant to prevent.
4. The linguistics partition is where the linguistic neighbours live (`semantics-pragmatics.md`,
   `register-strata-attestation.md`, `sacred-registers-liturgical-language.md`,
   `politeness-taboo-euphemism.md`, `naming-systems.md`), so the couples can be one-way.

The **coverage map** `corpus/README.md` must gain, for leg C5:
(a) one index row inside `## linguistics/ (40)` → the section header must read `(41)`;
(b) `Total knowledge entries: 267.` → `268.`;
(c) the last footer line `(total 267 files; directory totals 40/36/43/29/24/95).` →
    `(total 268 files; directory totals 41/36/43/29/24/95).`;
(d) a dated `## Round 96 …` footer section (the checker's `FOOTER_RE` takes the **last**
    "Counts checked <date> from the repo root:" block).

I verified this recipe on a scratch mirror of the base tree: before the four edits,
`python3 -B tools/check-corpus-index.py --root <mirror>` → `CORPUS-INDEX: FINDINGS files=268
rows=267 findings=5 ids=FOOTER_DIR_TOTALS,FOOTER_TOTAL,HEADER_DRIFT,MISSING_ROW,TOTALS_DRIFT`, rc=1;
after them → `CORPUS-INDEX: OK files=268 rows=268 findings=0`, rc=0. The counter then reported
`LEG C5 PASS index rc=0 last: CORPUS-INDEX: OK files=268 rows=268 findings=0`.

**Routing gap — read this before the scribe lands.** No seat in `.ufo/waves/round-96/w1-spec.json`
is told to write `corpus/README.md`: `ExecRegistry96` is "the ONLY writer of `corpus/SOURCES.md`
and `reports/round-96/evidence/`", `ScribeEntry96` is "the only writer of that file"
(the entry). The round-95 equivalent (`ExecRegistry95`) *did* own the README work — its item text
has step 5, "README.new.md: insert the index row … bump the section count … add a `## Round 95
lament entry (2026-11-05)` footer section" — and produced `stage/ExecRegistry95/README.new.md`
plus `README.diff`. Round 96's `ExecRegistry96` prompt has no README step, and leg **C5**
(`index rc=0`) cannot pass without it. The L1 is the only committer, so the README bytes must be
produced by a seat and landed by the L1; the recipe in this section is exactly what is needed.
I have not written to the lane repo and did not touch `corpus/README.md`.

---

## 6. Files read (all read-only)

Lane repo `kotodama-shokunin/`: `reports/round-96/claims.json`, `reports/round-96/predispatch.py`,
`reports/round-96/predispatch-base.txt`, `reports/round-95/predispatch-lands.txt`,
`reports/round-95/claims.json` (not opened; listed only), `reports/round-95/evidence/` (listing),
`corpus/README.md`, `corpus/SOURCES.md`, `corpus/QUALITY.md`, `corpus/LOG.md` (not opened),
`corpus/lessons/round-90.md`, `corpus/lessons/round-91.md`, `corpus/lessons/round-94.md`,
`corpus/lessons/round-95.md`, `tools/check-corpus-index.py`, `tools/check-advance-evidence.py`,
`tools/check-cited-lines.py`, `tools/check-evidence-coupling.py` (usage line),
`tools/ledger-token-guard.py` (copied to the scratch mirror only),
`corpus/knowledge/linguistics/` — all 40 filenames listed; opened in full or in part:
`petitionary-and-votive-formulae.md`, `sacred-registers-liturgical-language.md`,
`politeness-taboo-euphemism.md`, `taboo-strata-lifecycle.md`, `naming-systems.md`,
`kinship-terminology.md`, `semantics-pragmatics.md`, `register-strata-attestation.md`,
`greeting-leave-taking-formulae.md`, `funerary-lament-dirge-formulae.md`,
`lullaby-child-song-formulae.md`, `orality-formulaic-language.md`;
`corpus/knowledge/myth-symbol/` — `binding-speech-complex.md` (read in four ranges),
`ritual-liminality.md`, `creation-myths-taxonomy.md`, `guest-right-hospitality-law.md`,
`ordeal-judicial-proof-rituals.md`, `witchcraft-sorcery-accusation-institution.md`,
`sacred-kingship-mythic-charter.md`, `pantheon-archetypes.md` (grep);
`corpus/knowledge/culture-material/` — `sumptuary-law-rank-display.md`, `craft-artisan-lexicon.md`,
`hair-grooming-codes.md`; `corpus/knowledge/civilizations/scythian-saka.md`;
`corpus/knowledge/synthesis/religion-language-co-evolution.md`;
`corpus/knowledge/verification/verification-independence-anti-circularity.md`;
`.ufo/waves/round-96/w1-spec.json`, `.ufo/waves/round-96/w1-dispatch.json` (structure),
`.ufo/waves/round-95/w1-spec.json`, `.ufo/waves/round-95/w1/stage/ExecRegistry95/` (listing),
`.ufo/waves/round-96/w1/` (listing only).
Fleet repo (read-only): `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh`,
`/home/vgpnk/Projects/shokunin/scripts/hyaku/disk-guard.sh`.

Scratch mirror (mine, deleted at yield): `/fast/scratch/hyaku/kotodama-r96/ScoutSurface96/`.

---

## 7. Tooling

**None installed or upgraded.** No pacman, no `uv tool install`, no release binary, no
`cargo`/`npm` install. All measurements used pre-existing tools: `grep`, `find`, `awk`, `sed`,
`python3` (stdlib only), `git` (read-only: `ls-tree`, `log`, `show`, `status`), and the lane's own
`tools/check-corpus-index.py` and `reports/round-96/predispatch.py`. pacman is host-paused by
orchestrator ruling; no pacman command was run. No host sysctl was touched.

## 8. Commands and rc (summary)

| Command | rc |
|---|---|
| `ls corpus/knowledge/*/ \| grep -i -E 'oath\|curse\|bless\|malediction\|imprecat\|vow\|swear\|sanction\|witness'` | 1 |
| `find corpus/knowledge -type f \( -iname '*oath*' … \)` | 0 (no output) |
| `git ls-tree -r --name-only 0539276c… corpus/knowledge \| grep -i -E 'oath\|…'` | 1 |
| `find corpus/knowledge -name '*.md' \| wc -l` | 0 → 267 |
| `find corpus/knowledge -name '*.md' \| awk -F/ '{print $3}' \| sort \| uniq -c` | 0 → 95/43/40/36/29/24 |
| `grep -c -i -E '\boath\|\bcurse\|blessing\|malediction\|\bvow\b\|swear' corpus/knowledge/linguistics/kinship-terminology.md` | 1 → 0 |
| same on `corpus/knowledge/culture-material/sumptuary-law-rank-display.md` | 1 → 0 |
| `python3 -B tools/check-corpus-index.py --root .` (lane) | 0 → `CORPUS-INDEX: OK files=267 rows=267 findings=0` |
| `python3 -B tools/check-corpus-index.py --root <scratch mirror>` before README edits | 1 → FINDINGS 5 |
| same, after README edits | 0 → OK files=268 rows=268 findings=0 |
| `python3 -B reports/round-96/predispatch.py --root <scratch mirror> --work … --base-rev 0539276c… --base-registry …` | 1 → `LEG C1 PASS bytes=51952 h2=7 table=6x3 phrases=6/6 topic-line=equal`; `LEG C5 PASS` |
| `bash scripts/sources-census.sh validate --file corpus/SOURCES.md` (lane) | 0 (`file ok`) |
| `python3 -B tools/check-cited-lines.py corpus/knowledge/linguistics/funerary-lament-dirge-formulae.md` | 0 → 0 findings |
| `python3 -B tools/check-cited-lines.py corpus/knowledge/myth-symbol/binding-speech-complex.md` | 0 → 0 findings |
| `bash scripts/hyaku/disk-guard.sh status` | 0 |
