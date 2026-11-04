<!--
ScribeLesson draft for L1 (round 89). Two edits to corpus/README.md, both required
by tools/check-corpus-index.py (read at 9ad00be1, unchanged since freeze 1cbd0efc):

EDIT 1 — heading bump (in place, line 344 at 9ad00be1):
    ## linguistics/ (33)   ->   ## linguistics/ (34)
  Why: audit() emits HEADER_DRIFT when a partition heading's declared count
  (SECTION_RE `^## ([a-z-]+)/ \((\d+)\)`) differs from the number of *.md files
  on disk in corpus/knowledge/<part>/ ("if declared is not None and declared !=
  len(disk): finding('HEADER_DRIFT', ...)"). The new file makes linguistics 34
  on disk, so a (33) heading gives rc 1. The supplemental row below needs no
  in-section placement: rows outside partition spans are assigned to the single
  partition whose directory holds the file (GHOST_ROW only if 0 or >1 owners).
  Precedent: round 86 bumped (32)->(33) for proverbs-riddles-attestation-solutions.md.

EDIT 2 — append the block below at the very END of the README (after the
  "## Round 88 notation deepening and finding sets" block). The auditor reads the
  LAST "Total knowledge entries:" line and the LAST "Counts checked" footer, so the
  block must be last. Shape copied from "## Round 85 metallurgy entry (appended
  2026-11-04)" (row, blank, totals, blank, footer); footer command line copied
  from the round-86 block, which already uses the index tool.

TOPIC RULE: the text after "— " must be byte-identical to the landed entry's
  `- topic:` value as TOPIC_RE extracts it (all lines up to the next "\n- <word>"
  line, each stripped, joined by single spaces). The topic below is a PLACEHOLDER
  CANDIDATE: ScribeEvidentiality had staged no entry when this was drafted. Regenerate
  the row from the landed entry with:
    python3 -c "import re,sys;t=open(sys.argv[1]).read();m=re.search(r'^- topic:(.*?)(?=\n- \w)',t,re.M|re.S);print('- \`evidentiality-epistemic-marking.md\` \u2014 '+' '.join(l.strip() for l in m.group(1).strip('\n').splitlines() if l.strip()))" corpus/knowledge/linguistics/evidentiality-epistemic-marking.md
  measure89 INDEX also requires the row prefix "- `evidentiality-epistemic-marking.md` — "
  (regex `^- `<basename>` \u2014 `, measure89.py:265).

Dry run by this seat: a shared clone at 9ad00be1 plus a stub entry carrying the
  candidate topic, EDIT 1 and EDIT 2 -> `python3 -B tools/check-corpus-index.py --root .`
  printed `CORPUS-INDEX: OK files=261 rows=261 findings=0`, rc 0; without EDIT 1 it
  printed HEADER_DRIFT, rc 1 (receipts/index-dryrun.txt).
-->

## Round 89 evidentiality entry (appended 2026-11-04)

- `evidentiality-epistemic-marking.md` — evidentiality (grammatical marking of information source) and its separation from epistemic modality as a conlang and culture design system — evidential system sizes and categories, where markers sit in grammar, how evidentials interact with person, questions, tense and reported speech, and the calibration traps of reading an evidential as a truth value, a politeness device or a national character.

Total knowledge entries: 261.

Counts checked 2026-11-04 from the repo root:
`python3 -B tools/check-corpus-index.py --root .`
(total 261 files; directory totals 34/36/43/29/24/95).
