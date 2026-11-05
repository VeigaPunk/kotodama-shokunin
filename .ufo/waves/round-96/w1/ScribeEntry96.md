# ScribeEntry96 — claim C entry, round 96 wave 1

Seat: scribe (coverage axis, milestone r96-v1). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Base `0539276c0e329743200b60e98bf289c540f78864`; freeze `deca7e6fff988061f01bfc501a91e18fca892822`;
correction `063f70c9ab9aed5297741773292ded6d713d537a`.

Frozen inputs read first, not edited: `reports/round-96/claims.json`, `reports/round-96/predispatch.py`,
`reports/round-96/predispatch-base.txt`.

## Files written

- `corpus/knowledge/linguistics/oath-blessing-curse-formulae.md` — the claim C entry (this seat is the
  only writer of that file; sha256 `4a604334469fa9eb40b202ba17153329e29e81f8310a5b74fc0fb2960b808b31`).
- `.ufo/waves/round-96/w1/stage/ScribeEntry96/self-check.txt` — the self-check output below.
- `.ufo/waves/round-96/w1/stage/ScribeEntry96/README.new.md` + `README.diff` — the corpus index patch,
  produced for the L1 to land (see "README routing" below). `corpus/README.md` itself was NOT written
  by this seat.
- `.ufo/waves/round-96/w1/stage/ScribeEntry96/DONE` — one line: the sha256 of the entry file.
- This trailer: `.ufo/waves/round-96/w1/ScribeEntry96.md`.

Nothing outside my stage dir was written except the entry file my item names. No commits, no pushes,
no mutating git/jj. Scratch `/fast/scratch/hyaku/kotodama-r96/ScribeEntry96/` is removed before yield.

## Tooling

None installed or upgraded. Every command in this report used tools already present on the host:
`python3` (stdlib only), `curl` (not used by this seat), `git` (read-only), `grep`, `sed`. No package
manager was run; pacman is PAUSED host-wide and was not touched. No host sysctl was mutated.

## Dependency

Waited for `.ufo/waves/round-96/w1/stage/ScoutSurface96/DONE` and
`.ufo/waves/round-96/w1/stage/ExecRegistry96/DONE` with a bounded loop
(`for i in $(seq 1 45); do [ -f <dep> ] && break; sleep 60; done`).

- `ScoutSurface96/DONE` appeared; its `surface.md` was read in full and its skeleton, adjacency table,
  zero-owner evidence and README recipe were used (the skeleton shaped the entry's eleven h2 headings;
  the adjacency table shaped the §1 deferral list; the README recipe produced the README patch).
- `ExecRegistry96/DONE` **had not appeared** when this seat's budget closed. Its dependency
  `ScoutSources96/DONE` appeared at 18:22, and `ScoutSources96/candidates.json` was read: eleven
  candidates, all `admitted: true`, each with a located quote whose `bytes.count == 1` against the
  scout's own capture (re-measured by this seat, all eleven = 1, words 3–19, all ≤ 25).

**The ids are OBSERVED, not derived.** `ExecRegistry96/rows.md` landed at 18:25 with ten rows,
S975–S984, and `ExecRegistry96/dropped.md` records one drop: *"C4: not written; reopened HTTP 404,
quote bytes.count=0"*. The landed mapping is C1→S975, C2→S976, C3→S977, C5→S978, C6→S979,
C7→S980, C8→S981, C9→S982, C10→S983, C11→S984 — the fifth and later ids shift by one relative to
the candidate-key order, because C4 was dropped.

This seat had already written an earlier version of the entry against ids derived from the scout's
candidate order (C1→S975 … C11→S985), before `rows.md` existed. That draft cited the dropped C4
(Ó Murchú's asseveration) and carried every id from the fifth onward one too high. When `rows.md`
landed, the entry was **re-keyed in place**: the two C4-grounded paragraphs were deleted, the
remaining nine ids were shifted down by one, and the `- sources:` header was rebuilt from the landed
ids. The entry now cites exactly the ten landed ids, each paired with that row's own anchor quote —
verified mechanically against `reports/round-96/evidence/manifest.json` (measurement 5 below). The
re-key was not cosmetic: without it the entry would have cited a dropped row and mis-attributed
nine quotes.

**Scratch was wiped mid-run by a sibling incident.** A `kake` lane seat reported at ~18:14 that it
had run `rm -rf` on the *parent* scratch directory of its own lane and deleted sibling seats'
scratch trees. That incident was in `kake-r97`; this lane's `kotodama-r96` tree survived (checked
immediately, `ls` rc 0, this seat's scratch intact). This seat's own scratch was nonetheless
re-created and its scripts rewritten, and the entry was re-keyed from the lane tree rather than
regenerated, so nothing was lost — but the scripts quoted in this report were rewritten after the
wipe and the numbers below are from the re-run.

## Measurements

Every number below has its command and rc.

**1. The frozen counter's own C1 leg, reproduced verbatim against the live tree.**
`python3 -B /fast/scratch/hyaku/kotodama-r96/ScribeEntry96/counter_c1.py` → rc 0:

```
LEG C1 PASS bytes=30143 h2=11 table=19x5 phrases=6/6 topic-line=equal
  phrase hits: ['oath formula', 'blessing formula', 'curse formula', 'self-imprecation', 'witness invocation', 'sanction clause']
```

The script reimplements the counter's C1 computation (lines 187–219 of the frozen
`reports/round-96/predispatch.py`) against
`corpus/knowledge/linguistics/oath-blessing-curse-formulae.md`: bytes 30143 (floor 12000),
11 h2 (floor 6), table 19 data rows × 5 columns (floor 5×3), 6 of 6 frozen phrases present in h2
headings or table data rows (floor 4), and the `- topic:` line byte-equal to
`'- topic: ' + FROZEN_TOPIC` (the em dash is U+2014). rc 0.

**2. The self-check** (`python3 -B selfcheck.py > …/stage/ScribeEntry96/self-check.txt`) → rc 0.
Output committed as `stage/ScribeEntry96/self-check.txt`:

```
TRUTH …/stage/ExecRegistry96/rows.md
BYTES 30143 (floor 12000) -> PASS
H2 11 (floor 6) -> PASS
TABLE 19x5 (floor 5x3) -> PASS
PHRASES 6/6 (floor 4) -> PASS hits=['oath formula', 'blessing formula', 'curse formula', 'self-imprecation', 'witness invocation', 'sanction clause']
TOPIC line 17 byte-equal -> PASS
CITED ids ['S975', 'S976', 'S977', 'S978', 'S979', 'S980', 'S981', 'S982', 'S983', 'S984']
CITED ids present in rows.md 10/10 missing=[]
QUOTE PAIRING wrong=[] multi-id lines=0
CAPTURES present for 10/10 missing=[]
SELFCHECK PASS
```

The three checks the self-check adds beyond the counter's C1: every cited id is present in the
registry's `rows.md` (10/10); every cited id's line carries that id's *own* manifest quote, with no
line carrying two ids; and every cited id has a capture file under `reports/round-96/evidence/`
(10/10, the counter's C7 condition).

**3. The grader's own entry legs, run against the draft.**
`tools/check-advance-evidence.py`'s `grade_entry` logic, reproduced against the file: SHAPE table 25 × 6
(the grader counts all pipe lines, not one table) with worst-sentence-repetition 1 (floor: a sentence
may repeat at most 2×); TOPIC shared content words with the declared topic 31 (floor 8) and filename
stem words 4/4 (`oath`, `blessing`, `curse`, `formulae` all present); phrase anchors 6/6 spanning 6
heading/table surfaces (floors: 4 phrases, span 3). All above the floors, rc 0.

**4. Clause-scoped citation lint.**
`python3 -B tools/check-cited-lines.py <entry>` → `CITED-LINES: 0 finding(s) in 1 file(s)`, rc 0.
No line carries two S-ids and no table row carries an id (QUALITY criterion 15).

**5. Every quoted span is an exact single-occurrence substring of its capture.**
`python3 -c "…json.load(open('reports/round-96/evidence/manifest.json'))…"` — the registry seat's own
manifest records `quote_count` = 1 for each of the ten landed ids, and this seat recounted the
quote-pairing against the entry: 22 citation lines, 0 wrong pairs, 0 multi-id lines. Independently,
`python3 -c "…open(capture,'rb').read().count(quote.encode())…"` over the scout's eleven captures
returned 1 for all eleven (words 3–19, every one ≤ 25). Quotes are embedded verbatim in the entry,
each on its own line with its own S-id.

**6. The README patch is verified, not asserted.** A scratch mirror was built from the lane's
`corpus/` + `tools/`, the patched README and the new entry copied in, and
`python3 -B tools/check-corpus-index.py --root .` run → `CORPUS-INDEX: OK files=268 rows=268
findings=0`, rc 0. Without the patch the same checker on the same mirror reports
`MISSING_ROW, HEADER_DRIFT, TOTALS_DRIFT, FOOTER_TOTAL, FOOTER_DIR_TOTALS` (rc 1), so the patch is
load-bearing for leg C5.

**7. Coupled paths all resolve.** `test -f` over the seven paths named in the `- couples:` line —
`myth-symbol/binding-speech-complex.md`, `linguistics/register-strata-attestation.md`,
`linguistics/semantics-pragmatics.md`, `linguistics/sacred-registers-liturgical-language.md`,
`linguistics/politeness-taboo-euphemism.md`, `linguistics/naming-systems.md`,
`myth-symbol/ritual-liminality.md` — 7/7 present, rc 0.

**8. The lane tree carries only this seat's entry.** `git -C <lane> status --porcelain` lists
`corpus/knowledge/linguistics/oath-blessing-curse-formulae.md` as the only corpus path this seat
added (the `M tools/check-advance-evidence.py` in the same listing is `ExecGraderV7`'s work, not this
seat's). No registry row, no README, no frozen file was touched.

## Cited ids

S975, S976, S977, S978, S979, S980, S981, S982, S983, S984 — the ten landed registry ids, read from
`stage/ExecRegistry96/rows.md`, each on its own line, each supporting one quoted sentence. The
`teaches` and `scope` cells below are the registry's own, not this seat's:

| id | source (registry row) | tier | the claim it grounds here |
|---|---|---|---|
| S975 | Faraone, "At the Limits of Efficacious Speech", OpenEdition | A | the oath frame is built around the self-curse |
| S976 | Nygaard, "ein lǫg ok einn siðr", Scandinavian-Canadian Studies 28 | A | the oath as a fixed utterance with prescribed wording |
| S977 | Homer, *Iliad* 19.258–262 (Greek), Perseus / Monro-Allen | A | the witness invocation as an address to a named power |
| S978 | Tuomi, "Ancient curses, medieval charms?", Studia Celtica Fennica 9 | B | the prohibition whose breach is itself the sanction (the *geis*) |
| S979 | Ní Mhaoldomhnaigh, *Satirical Narrative in Early Irish Literature*, Maynooth PhD | B | the curse as a composed genre with requirements |
| S980 | Frangulov, *Ritual speech, Performativity, and Modality*, Oxford MPhil | B | blessing/curse/hymn as one class of performative utterance |
| S981 | *Encyclopedia of Shinto*, "Amatsunoritohutonoritokō", Kokugakuin | B | the fixed formula as a text with an internal sectional structure |
| S982 | Eyong, Nwosu, Effiom & Onah, "The River as Witness", *Performance* 4(2) | A | the witness invocation paired directly with the enforcement clause |
| S983 | Aston, *Shinto: The Way of the Gods* ch. 12, Wikisource | A | the recited formula distinguished from free prayer |
| S984 | Holtz, "YHWH's Covenant: Why Moses Calls Heaven and Earth as Witnesses", TheTorah.com | B | the witness invocation borrowed from the treaty tradition |

## Claims left as inference

Marked in the entry as *design, not sourced*, in these places:

1. **The whole slot grammar of §8 and the register table of §7.** The six-slot inventory (performative
   verb, witness invocation, assertion, sanction clause, self-imprecation, uptake), the three-register
   division and the ten-row decision procedure of §10 are this entry's own analytic apparatus applied
   to the reports, not a claim that any tradition organises binding utterances under those slots.
2. **The `## 9` error patterns** — "the oath that binds nobody", "the curse with no witness", "the
   empty addressee", "register leakage", "the transferred penalty used as a threat", and the rest —
   are design rules with tests, derived from the slot grammar.
3. **The `## 10` checklist and the worked micro-example** (NON-CANON) are design instruments.
4. **The dropped candidate.** The registry seat dropped C4 (Ó Murchú) on independent re-opening
   (HTTP 404, quote count 0) and the entry cites nothing from it; the corresponding facets are
   covered by other rows, and no claim in the entry rests on the dropped source.
5. **§5's addressee-class table and §6's sanction-shape table** are the entry's design taxonomy; the
   five addressee classes and five sanction shapes are not claimed to be attested categories.

Nothing in the entry claims canon, rules on real-world rights or attribution, or decides what is true
in any world. Canon is deferred to lore-shokunin and research method to chousa, per `PROVINCE.md`'s
Owns/Refuses lines; the entry says so in §1 and §11.

## README routing (a gap this seat closed)

ScoutSurface96's `surface.md` §5 flagged that **no wave-1 seat owns `corpus/README.md`**, yet leg C5
(`tools/check-corpus-index.py --root <root>` rc 0) needs the index row for the new entry plus the
count bumps. `ExecRegistry96` confirmed by message that its item names only `corpus/SOURCES.md` and
`reports/round-96/evidence/` as its writes. This seat therefore produced, but did not apply, the
patch: `stage/ScribeEntry96/README.new.md` and `README.diff`, containing exactly four changes —
the index row inside `## linguistics/` (40 → 41), `Total knowledge entries: 267.` → `268.`, the
footer totals `(total 267 files; directory totals 40/36/43/29/24/95).` → `(total 268 files; directory
totals 41/36/43/29/24/95).`, and a dated `## Round 96 oath, blessing and curse formulae entry
(2026-11-05)` footer block. The index row text is extracted from the entry file with the index
checker's own `TOPIC_RE` regex, so it is byte-identical to the file's `- topic:` field and the
`TOPIC_MISMATCH` leg cannot fire. Verified on a scratch mirror (measurement 6 above): rc 0,
`files=268 rows=268 findings=0`. **The L1 must land it.**

## Out of scope for this seat

- `corpus/SOURCES.md` and `reports/round-96/evidence/` — `ExecRegistry96`'s writes.
- `corpus/README.md` — not this seat's file; the patch is staged for the L1.
- `reports/round-96/claims.json`, `predispatch.py`, `predispatch-base.txt` and everything under
  `reports/round-95/` — frozen, untouched.
- `tools/check-advance-evidence.py` v7 — `ExecGraderV7`'s write.
- The claim O battery, mutation and grader legs — other seats'.

## Known limits

1. **The ids are observed, not derived.** `rows.md` landed and the entry was re-keyed to it; the
   re-key is verified line-by-line against the registry's own `manifest.json` (measurement 5). The
   one consequence of the drop is that the Irish asseveration facet of §2 and §4 now rests on the
   other rows rather than on a dedicated one; the entry does not claim a dedicated Irish
   asseveration source.
2. **Leg C7 is satisfied.** All ten cited ids have a capture under `reports/round-96/evidence/`
   (10/10, measured). The registry seat's own `manifest.json` records the per-id sha256 and quote.
3. **The quoted spans are the scout's and registry seat's, re-verified by this seat against the
   scout's committed captures.** The reviewer seat should re-open two of the eleven live URLs and
   recount, per its own item.
4. **The base is eleven sources across eleven traditions**, and none of them is a survey of binding
   formulae. The entry says so in §11 and does not generalise any single case into a universal
   grammar.
5. **The entry was re-keyed after the dependency closed**, so a reviewer should read
   `stage/ScribeEntry96/self-check.txt` rather than trust the entry's own header alone: the
   self-check names `rows.md` as its source of truth and confirms the id/quote pairing, the capture
   coverage and the counter's C1 conditions in one place.
6. **The `README.new.md` / `README.diff` patch was regenerated after the re-key**, so its index row
   text is byte-identical to the *current* entry file's `- topic:` field. The L1 must land the patch
   as it now stands; an earlier version of it (generated before the re-key) has been overwritten.
