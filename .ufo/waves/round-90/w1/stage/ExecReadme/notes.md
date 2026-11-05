# notes.md — what `tools/check-corpus-index.py` checks, and what it does not

Tool: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-corpus-index.py`
(read, never modified). Every line below is a measurement on the staged mirror
`/fast/scratch/hyaku/kotodama-r90/ExecReadme/` at the freeze
`d0b6f2a7f9cc36272682749a9b047b739406f0c8`, or a direct read of the tool's own
source. Controls C0–C8 are scratch copies of that mirror; the lane was never
written.

## What it checks (each measured green or red)

| leg | finding class | what it compares |
|---|---|---|
| row ↔ file bijection | `MISSING_ROW` | a `.md` file in `corpus/knowledge/<part>/` with no row in that part's span |
| row ↔ file bijection | `GHOST_ROW` | a row with no such file; also a row outside every span with 0 or >1 owning partitions |
| duplicates | `DUPLICATE_ROW` | the same basename twice inside one partition span (C4: rc 1) |
| row topic | `TOPIC_MISMATCH` (`REWRITE` / `NO_TOPIC_FIELD`) | row topic vs the entry's own `- topic:` field, byte-equal after per-line strip and join; one changed word fails (C8: rc 1) |
| partition header | `HEADER_DRIFT` | `## <part>/ (<n>)` vs the on-disk file count of that directory |
| totals line | `TOTALS_DRIFT` | the **last** `Total knowledge entries: N.` vs the summed file count |
| counts footer | `FOOTER_ABSENT`, `FOOTER_MALFORMED`, `FOOTER_TOTAL`, `FOOTER_DIR_TOTALS` | the **last** `Counts checked …` block: the fenced command's presence, total, and the six-slot vector in `PARTS` order (arity and order included) |
| structure | `PARTITION_MISSING`, `PARTITION_UNKNOWN`, `PARTITION_DIR_MISSING`, `DUPLICATE_SECTION` | the six fixed partition names, their directories, and one section each |
| invocation | `CORPUS_INDEX_ERROR`, rc 2 | missing `--root`, root not a directory, missing `corpus/knowledge` or `corpus/README.md` |

Exit: 0 clean, 1 findings, 2 unusable input. `--json` prints the full finding
list; the default prints one `CORPUS-INDEX:` summary line.

## What it does not check (each demonstrated, not asserted)

- **C0 — a topic line with no following field reads as `NO_TOPIC_FIELD`.**
  `TOPIC_RE` ends only at `\n- \w`, so a one-field entry fails. Measured: the
  first overlay run with a bare `- topic:` fixture returned
  `TOPIC_MISMATCH:linguistics/petitionary-and-votive-formulae.md kind=NO_TOPIC_FIELD`
  (rc 1); adding `- sources:` under it turned the same tree green. Consequence
  for claim C: the entry must carry a field after `- topic:` — claims'
  `header_keys` already require `- sources:`, so this is a trap, not a gap.
- **C1 — entry content is not checked at all.** A two-line entry holding only
  `- topic:` and `- sources:` passes (rc 0). The index tool never measures the
  entry's byte size, heading count, table shape, topic-word overlap, new ids,
  lesson gate line or capture; those are claim C's ENTRY/SHAPE/TOPIC/NEWIDS/
  GATE/CAPTURE legs and belong to the freeze-pinned counter, not to this tool.
  A green index says the row is consistent with a file, never that the file is
  the entry the claim describes.
- **C2 — only the last totals line and the last footer block are read.** A tree
  with a stale `Total knowledge entries: 261.` above a live `262.` is green
  (rc 0). Earlier rounds' blocks are dated records by convention, and the tool
  cannot tell a superseded record from a live claim.
- **C3 — filename order is not parsed.** A row moved to the wrong position in
  its span is green (rc 0). Order is a file convention and a reviewer check.
- **C5 — the footer's date and command are parsed and never used.** A footer
  back-dated to `1999-01-01` whose fenced command is `false` is green (rc 0):
  the date is not compared with the round, the claims, or today, and the
  command string is never executed. A footer can therefore be stale or
  fictitious and still satisfy the footer leg.
- **C6 — no claim binding.** Renaming both the file and its row to
  `unrelated-name.md` while keeping the topic text is green (rc 0). The tool
  has no notion of which filename claim C names; the "is this the claimed
  entry" question is the counter's `C.entry` check and the reviewer's.
- **Not checked: the `- sources:` ids.** Nothing here resolves S942–S948
  against `corpus/SOURCES.md`; a row citing absent ids is green. That leg is
  `scripts/sources-census.sh validate` (E02/E03 id shape and duplicates, E11
  used-by path existence, W01/W03 tier/status pairing) — see the report.
- **Not checked: registry append-only.** The index tool cannot see that a base
  registry row's cells were edited; claim C's APPENDONLY leg is the counter's.
- **Not checked: the README's revision blocks or H1 count.** Those are
  `tools/check-readme-revisions.py` and `tools/check-readme-heading.py`; both
  were run on the overlaid mirror and stayed at base (findings 0, one carried
  `REVISION-ORPHAN` warning unchanged).

## Consequence for the report's wording

Claim C's INDEX leg can be reported as "the freeze-pinned index tool exits 0
over the lands tree with files = rows and zero findings". It must **not** be
reported as "the README is correct" or "the entry is present and complete": C1,
C5 and C6 show the tool accepts an empty entry, a fictitious footer, and any
filename. Coverage of the topic is carried by the entry's own legs, the
registry rows and the lesson gates — not by this tool.
