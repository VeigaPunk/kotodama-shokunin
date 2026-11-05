# corpus/README.md — the one row to insert for claim C

Measured at the freeze `d0b6f2a7f9cc36272682749a9b047b739406f0c8`
(base `6b0b86e45ae902331aca75863db380f2991458c4`), file 937 lines,
sha256 `1896e3866be61e732c1a6762d825a326012b17e63771ea0dc06f5818d369cb21`.

## 1. Row grammar, as the index tool parses it

`tools/check-corpus-index.py` (read, not modified):

- `ROW_RE = ^- \`([^`]+\.md)\` — (.*)$` — one line, backticked filename ending
  `.md`, an em dash (U+2014) with one space each side, then the topic cell to
  end of line. Nothing else on the line is parsed; there is no sources column.
- `TOPIC_RE = ^- topic:(.*?)(?=\n- \w)` — the topic cell is compared
  **byte-equal** against the entry file's own `- topic:` field, whitespace
  collapsed across continuation lines. A topic block must be followed by
  another `- <word>` field (`- sources:` does this); with no following field
  the file reads as `NO_TOPIC_FIELD` — measured, see `notes.md` control C0.
- Rows are read only inside a partition span: a `## <partition>/ (<n>)`
  heading starts the span and the next `## ` line ends it. A row outside every
  span becomes "supplemental" and is assigned to the single partition whose
  directory holds that basename, or reported `GHOST_ROW` if 0 or >1 owners.
- Filename order is **not** parsed or enforced by the tool; it is the file's
  own convention and the reviewer's check.

Observed row shape in the linguistics span (line 359):

```
- `orality-formulaic-language.md` — Oral tradition linguistics — how extended verbal art is composed, ...
```

i.e. `- \`` + filename + `\`` + ` — ` + the entry's `- topic:` text verbatim.

## 2. Partition headings and counts as they are now

```
344|## linguistics/ (34)
378|## myth-symbol/ (36)
412|## culture-material/ (43)
455|## synthesis/ (29)
487|## verification/ (24)
513|## civilizations/ (95)
```

`PARTS` order in the tool is linguistics, myth-symbol, culture-material,
synthesis, verification, civilizations; the counts footer vector is that order.

Live totals / footer, as they are now (the last `Total knowledge entries:` line
and the last `Counts checked` block in the file):

```
933|Total knowledge entries: 261.

935|Counts checked 2026-11-04 from the repo root:
936|`python3 -B tools/check-corpus-index.py --root .`
937|(total 261 files; directory totals 34/36/43/29/24/95).
```

On-disk file counts at the freeze confirm them: 34/36/43/29/24/95 = 261.

## 3. The row to insert

Position: **after line 359** (`- \`orality-formulaic-language.md\` …`) and
**before line 360** (`- \`phonetics-phonology.md\` …`). Verified by sorting the
34 base basenames plus the new one: `petitionary-and-votive-formulae.md` lands
at index 17 of 35, between `orality-formulaic-language.md` and
`phonetics-phonology.md`.

Topic cell: `claims.json` `C.topic`, byte for byte. Row: 287 bytes,
sha256 `1efc9279de60be06c3ccbfb4d8a4f2376bd12a70db1d0807d0915ae154df7114`.

```
- `petitionary-and-votive-formulae.md` — petitionary address and votive formulae: vocative address to deities, petition mood (imperative, optative, precative), the conditional vow, votive inscription grammar, prayer-register archaism and parallelism, design procedure and failure modes
```

Sources cell (the entry header line that must carry the admitted ids; the
registry's `used-by` cells must name the entry in return):

```
- sources: S942 S943 S944 S945 S946 S947 S948
```

Admitted ids as stated by ScribeEntry-9: S942 S943 S944 S945 S946 S947 S948 —
seven rows, tier A/B, status `mined`, opened 2026-11-04, `used-by`
`corpus/knowledge/linguistics/petitionary-and-votive-formulae.md`, all cited in
the entry's `- sources:` header and body. S949 is the lesson's reject row
(tier C, `rejected`, `used-by` `corpus/lessons/round-90.md`) and is **not**
cited by the entry, so it does not appear in the sources cell.

The README row itself carries no source ids — that is the entry header's and
the registry's job — so the row above is complete as written.

## 4. Count updates, exact old → new

In-place (single live section header):

| where | old | new |
|---|---|---|
| line 344 | `## linguistics/ (34)` | `## linguistics/ (35)` |

Appended (the totals line and the counts footer are per-round dated records;
rounds 73–89 each appended a block rather than rewriting an older one, and the
tool reads the **last** `Total knowledge entries:` line and the **last**
`Counts checked` block):

| where | old | new |
|---|---|---|
| last totals line (base line 933, inside the r89 block) | `Total knowledge entries: 261.` | `Total knowledge entries: 262.` |
| last footer total (base line 937) | `(total 261 files; directory totals 34/36/43/29/24/95).` | `(total 262 files; directory totals 35/36/43/29/24/95).` |

Footer vector moves `34/36/43/29/24/95` → `35/36/43/29/24/95` (only the
linguistics slot moves; PARTS order preserved).

## 5. Landing block to append after line 937

```
## Round 90 petitionary and votive entry (2026-11-04)

`knowledge/linguistics/petitionary-and-votive-formulae.md` adds a dedicated
entry on petitionary address and votive formulae: vocative address to deities,
the petition mood (imperative, optative, precative), the conditional vow,
votive inscription grammar, prayer-register archaism and parallelism, and the
design procedure with its failure modes. At base the surface existed only as
sub-sections of six entries and no knowledge filename carried
prayer|petition|votive|supplicat. Sources S942–S948 were opened this round.
This is coverage, not freshness: no older registry row is re-verified,
re-dated or repaired.

Total knowledge entries: 262.

Counts checked 2026-11-04 from the repo root:
`python3 -B tools/check-corpus-index.py --root .`
(total 262 files; directory totals 35/36/43/29/24/95).
```

The r89 block's `Total knowledge entries: 261.` (line 933) and footer (935–937)
stay as the dated record they are; they are superseded, not edited.

## 6. Measured before → after (staged mirror, never the lane)

Staged mirror of the freeze in `/fast/scratch/hyaku/kotodama-r90/ExecReadme/`,
row + header + landing block + a topic/sources-only fixture entry overlaid,
then:

```
before  CORPUS-INDEX: OK files=261 rows=261 findings=0    rc=0
after   CORPUS-INDEX: OK files=262 rows=262 findings=0    rc=0
        parts: linguistics (35,35,35) — declared, files, rows
        totals_line 262, footer total 262, dir_totals [35,36,43,29,24,95]
```

Adjacent README controls stay as they were at base:
`check-readme-revisions.py` findings 0 / warnings 1 (the carried
`REVISION-ORPHAN` at lines 225/236, unchanged), `check-readme-heading.py`
findings 0.

The fixture entry is a two-line `- topic:` / `- sources:` stand-in only; the
production entry body is ScribeEntry's and its `- topic:` must be byte-equal to
the row above for the index leg to stay green.
