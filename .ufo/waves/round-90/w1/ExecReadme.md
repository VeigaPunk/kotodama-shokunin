# ExecReadme — corpus index accounting for claim C (round 90, w1)

Stage: `.ufo/waves/round-90/w1/stage/ExecReadme/`
Freeze: `d0b6f2a7f9cc36272682749a9b047b739406f0c8` (base `6b0b86e45ae902331aca75863db380f2991458c4`).
Lane files were read only; every write is inside the stage dir and
`/fast/scratch/hyaku/kotodama-r90/ExecReadme/` (deleted before yield).

Deliverables in the stage dir: `readme-row.md` (row grammar, partition
headings/counts with line numbers, the exact row, the sources cell, exact
old→new count pairs, the landing block), `notes.md` (what the index tool checks
and does not, with controls), `overlay-index.py` (the measured overlay), and
`evidence/` (`before.json`, `after.json`, `census-registry-unchanged.tsv`,
`controls.txt`).

## 1. Row grammar and current partition counts (pasted, with line numbers)

Row grammar as the tool parses it: one line,
``- `<filename>.md` — <topic>`` with an em dash (U+2014), topic cell to end of
line; the topic cell is compared **byte-equal** against the entry's own
`- topic:` field. There is no sources column in a README row.

```
344|## linguistics/ (34)
378|## myth-symbol/ (36)
412|## culture-material/ (43)
455|## synthesis/ (29)
487|## verification/ (24)
513|## civilizations/ (95)
933|Total knowledge entries: 261.

935|Counts checked 2026-11-04 from the repo root:
936|`python3 -B tools/check-corpus-index.py --root .`
937|(total 261 files; directory totals 34/36/43/29/24/95).
```

On disk at the freeze: 34/36/43/29/24/95 = 261, registry 865 rows, the
petitionary entry absent. This matches `claims.json` `C.before` exactly.

## 2. The row and the count updates

Insert **after line 359** (`orality-formulaic-language.md`), **before line 360**
(`phonetics-phonology.md`); filename sort puts the new basename at index 17 of
35 between those two. Row 287 bytes,
sha256 `1efc9279de60be06c3ccbfb4d8a4f2376bd12a70db1d0807d0915ae154df7114`:

```
- `petitionary-and-votive-formulae.md` — petitionary address and votive formulae: vocative address to deities, petition mood (imperative, optative, precative), the conditional vow, votive inscription grammar, prayer-register archaism and parallelism, design procedure and failure modes
```

Topic cell is `claims.json` `C.topic` byte for byte (29 words).

Sources cell — the entry header line, naming the admitted ids:

```
- sources: S942 S943 S944 S945 S946 S947 S948
```

ScribeEntry-9 states these seven rows are tier A/B, `mined`, opened 2026-11-04,
`used-by corpus/knowledge/linguistics/petitionary-and-votive-formulae.md`, all
cited in the entry's header and body; S949 is the lesson reject row (tier C,
`rejected`, `used-by corpus/lessons/round-90.md`) and is not cited by the entry,
so it is not in the sources cell. Verified against the registry: `S94[2-9]`
occurs 0 times in `corpus/SOURCES.md`, so the range is free and E03
(duplicate id) cannot fire from it.

Exact old → new pairs:

| where | old | new |
|---|---|---|
| line 344 (in place) | `## linguistics/ (34)` | `## linguistics/ (35)` |
| last totals line (base 933) | `Total knowledge entries: 261.` | `Total knowledge entries: 262.` |
| last footer total (base 937) | `(total 261 files; directory totals 34/36/43/29/24/95).` | `(total 262 files; directory totals 35/36/43/29/24/95).` |

The totals line and the footer are per-round dated records (rounds 73–89 each
appended a block), and the tool reads the **last** of each — so the landing
appends a `## Round 90 …` block carrying the 262 total and the
`35/36/43/29/24/95` footer, and the r89 block's 261 stays as the dated record
it is. The full block text is in `readme-row.md` §5.

## 3. Measured on the staged mirror (before → after)

Mirror = `git archive` of the freeze; overlay = row + header + landing block +
a two-line `- topic:`/`- sources:` fixture entry (the production body is
ScribeEntry's, not mine).

```
before  CORPUS-INDEX: OK files=261 rows=261 findings=0    rc=0
after   CORPUS-INDEX: OK files=262 rows=262 findings=0    rc=0
        parts: linguistics (declared 35, files 35, rows 35); other five unchanged
        totals_line 262; footer total 262; dir_totals [35,36,43,29,24,95]
```

Adjacent README controls unchanged by the overlay:
`check-readme-revisions.py` findings 0 / warnings 1 (the carried
`REVISION-ORPHAN` at lines 225/236, identical at base) and
`check-readme-heading.py` findings 0 (one H1).

## 4. Sources census

`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file
<mirror>/corpus/SOURCES.md --today 2026-11-04` — run with the registry
**unchanged**, because `.ufo/waves/round-90/w1/stage/ScribeEntry/rows.md` does
not exist yet (checked at start and again before yield; the scribe's stage holds
only an empty `evidence/` directory):

```
rc=0
counts: 1 ok line, 5 W01, 30 W04, no E codes
W01 = tier-C rows mined with a used-by path (S881 S882 S884 S893 S907)
W04 = same URL across scopes (S127–S133, S185, S186, S358, S482–S490, S561–S573,
      S648–S651, S830, S927, S928)
```

Warnings only; the lane is clean at base and stays clean. None of the W codes
touch the reserved range or the petitionary entry.

Measured dependency for integration (control, scratch only, dummy 11-cell row
in the registry section — not evidence content):

- registry row with `used-by corpus/knowledge/linguistics/petitionary-and-votive-formulae.md`
  and the entry file **absent** → `E11 missing used-by …`, rc 1;
- same row with the entry file **present** → `ok`, rc 0;
- a reject-shaped row pointing at `corpus/lessons/round-90.md` → `ok`, rc 0;
- the same row placed outside `## Registry` → `E12 row outside Registry section`, rc 1.

So the registry rows and the entry file must land in the same integration
revision, and ScribeEntry's `rows.md` must be re-validated once written.

## 5. What the index tool does not cover (so the report does not overclaim)

Measured, with controls recorded in `notes.md` and `evidence/controls.txt`:

- a two-line entry with only `- topic:`/`- sources:` is green — **entry content
  (size, headings, table, overlap, ids, gate, capture) is not checked**; those
  are claim C's other legs, run by the freeze-pinned counter;
- a stale `Total knowledge entries: 261.` above a live 262 is green (only the
  last line and last footer are read);
- a row moved out of filename order is green;
- a footer back-dated to `1999-01-01` with fenced command `false` is green (the
  date is never compared to the round or today, the command is never run);
- renaming file and row to `unrelated-name.md` with the same topic is green —
  the tool has no binding to claim C's `C.entry`;
- the `- sources:` ids are never resolved against the registry (that is the
  census' job), and registry append-only is invisible to it;
- a wrong-partition move is red (`MISSING_ROW`, `GHOST_ROW`, `HEADER_DRIFT`,
  `FOOTER_DIR_TOTALS`, rc 1), a duplicate row is red, and a one-word topic
  change is red — the tool is not vacuous.

Trap worth carrying into integration: `TOPIC_RE` ends only at a following
`- <word>` field, so an entry whose `- topic:` is the last field reads
`NO_TOPIC_FIELD`. My first overlay run measured exactly that (rc 1,
`kind=NO_TOPIC_FIELD`); adding `- sources:` under the topic turned it green.

## 6. Claim-C leg status from this seat

- INDEX: **passes** on the overlaid mirror (rc 0, files = rows = 262, findings 0),
  and the exact row/count pairs are handed over.
- APPENDONLY: nothing in my overlay touches an existing row; no base registry
  row is edited (registry unchanged in the mirror and in the lane).
- Not mine to claim: ENTRY/SHAPE/TOPIC/NEWIDS/GATE/CAPTURE (ScribeEntry's entry
  and rows), and freshness is not claimed.

## Risks and blockers

- `ScribeEntry/rows.md` absent at yield → census was run with the registry
  unchanged (rc 0). L1 must re-run the census after the rows land; the measured
  E11 control says the entry file must land with them.
- The production entry's `- topic:` must be byte-equal to the row above, and
  must be followed by another `- <word>` field; otherwise the index leg goes
  red on integration.
- The README row carries no source ids; the sources binding lives in the
  entry's `- sources:` header and the registry `used-by` cells (both
  ScribeEntry's). The admitted set I was told is S942–S948 (7); claim C needs
  ≥3.
- My fixture entry is a stand-in only; it is not in the lane and must not be
  mistaken for the production entry.

Assimilation: none.
Tooling: no installs or upgrades this seat (no package manager invoked).
