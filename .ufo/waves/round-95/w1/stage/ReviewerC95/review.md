# ReviewerC95 — independent attack of claim C (funerary laments and dirges)

Date: 2026-11-05 (all commands run 2026-11-05, process cwd `/home/vgpnk/Projects/shokunin`,
commands rooted at scratch `/fast/scratch/hyaku/kotodama-r95/ReviewerC95/`).
Lane repo: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (base rev
19aa4dd03dfd37b435d0b8ea5b313635d9d51592, freeze commit d41eb594d27fa71869c0c28d9c2dc051fda40079,
HEAD = freeze commit; nothing under the lane was modified by this seat).

Verdict: `REVIEWER-C-95: PASS legs=5/5` — Leg 4 passes with one `UNMEASURED` caveat
recorded in leg 5. No defect found in the artifacts under review. One defect was found
and routed in my own review repro harness (`R95-RM1`, below).

Dependencies: all three DONE markers landed at the end of the 45x60s bounded wait
(= 44 minutes: `for i in $(seq 1 45); do all=1; for d in ExecRegistry95 ScribeEntry95
ScribeLesson95; do [ -f <stage>/$d/DONE ] || all=0; done; [ $all = 1 ] && break;
sleep 60; done; echo $d; done`; rc 0; wall time 2640 s; no BLOCKED path).

## Leg 1 — captures (PASS, no defect)

sha256 of every committed capture (`sha256sum`, rc 0), both files per row:

```
S970.txt dc7394e9862003b0b26e7631520e3dcb19832d25b19ddd4e6898cda06c371316
S970.pdf e8fb753b6b3adf3fe45075604e36e6c20034c5432748d19dd26aeb36465d3a8e
S971.txt 656c45388dbfcab8f9de8a233eada5d8f8571647a1f04955605bff71cbc4a26a
S971.pdf 85b821c7233c85bf1d3907b5db5ce98d368d19f6a06cdacc029a7df628345fbe
S972.txt d3ff0209b9d80418bcc9345535f5fd440a3fc8a2433da6982c42a65d777293ce
S972.pdf 1e0b0f8d8b529aae60ff2138d591aeb40465e778d11702b88b176d68334b30c8
S973.txt e017b3958dac14b32ff08a11f1750638e997c5df43ec9674a91413f5c42cac76
S973.pdf 8750510347c20a3ef8a12112435cc917c2737a42a4ffeadab3f85b557720a5d9
S974.txt 251b4d3f420164baa4bdc6508e54736cb0d00a42bc66940363203c264060159d
S974.pdf f1e4be9fd0868713bf363ea18b368a501dd48d87dc7bd3039e801f4954ad2672
```

All ten match the `## Gate` table in
`.ufo/waves/round-95/w1/stage/ScribeLesson95/round-95.md` byte-for-byte (read of the
Gate table + `sha256sum`).

Quote verification (Python 3 `bytes.count`-equivalent over the UTF-8 decoded captures,
38 words by `len(quote.split())`), per row, Gate table columns and quote spans:

| row | table quote | own `.txt` | words (declared / measured) |
|---|---|---|---|
| S970 | `the antiphonal way of performing Seto songs` | 1 | 7 / 7 |
| S971 | `The antiphonal nature of voceru performance` | 1 | 6 / 6 |
| S972 | `Professional keeners took over.` | 1 | 4 / 4 |
| S973 | `was important in the role of the female professional mourner` | 1 | 10 / 10 |
| S974 | `ends with a refrain exclamation` | 1 | 5 / 5 |

Every row's quote occurs **exactly once** in that row's own committed capture
(`S97x.txt`); each is ≤ 25 words. All five bullets' **longer** Gate spans also occur
exactly once in their own `.txt` (7 words不去 — measured spans: 14, 15, 8, 12, 11 words,
all ≤ 25; counts 1/1/1/1/1, rc 0). No quote drifted.

Spot-reopen (leg 1 obligation): row **S970**,
`https://sciendo.com/pdf/10.2478/jef-2025-0006`, plain `curl -L --max-time 30`,
default UA (no override), rc 0:

```
url=https://sciendo.com/pdf/10.2478/jef-2025-0006 http=200 bytes=950971
type=binary/octet-stream; curl rc=0
sha256 = e8fb753b6b3adf3fe45075604e36e6c20034c5432748d19dd26aeb36465d3a8e
```

= byte-identical to the committed `S970.pdf` capture (same timestamp, same 950971
bytes). No difference observed, byte-identity re-confirmed.

## Leg 2 — entry (PASS, no defect)

Entry-draft floors on
`.ufo/waves/round-95/w1/stage/ScribeEntry95/funerary-lament-dirge-formulae.md`
(`wc -c` = 50148; 12 `## ` headings; table 11 x 5; all six frozen phrases present in
headings or table rows per claims.json C1 grammar; `- topic:` line byte-equal to the
frozen topic in `reports/round-95/claims.json`), cross-checked three ways:

- frozen counter byte `predispatch.py` C1 grammar, reimplemented in a byte
  re-measurement (`norm()` + separator/row/cell parser), =50148 =12 =11 =5 =6/6
  `topic-line=equal`, cf. frozen `C1 … detail` format — same result, rc 0.
- frozen grader v5 entry-mode, `python3 -B tools/check-advance-evidence.py entry
  --root <scratch> --entry <entry> --lesson <lesson> --capture-dir captures
  --base-registry base` with claims.json `frozen_topic` passed via `--topic`
  (`ENTRY-EVIDENCE: PASS legs=8/8`).
- strongest-run: grader v6 bytes (`ExecGraderV6/v6-candidate.py`
  f7981ba2881bff2a…), same flags **plus `--base-lesson` pinned to the base-tree
  round-94 lesson, and entries as of 2026-11-05**: `ENTRY-EVIDENCE: PASS legs=9/9`
  (the strongest run: all nine grader legs at the claimed floors).

My reimplemented floors (dvV1 parser): bytes=50148, h2=12, table=11x5, phrases 6/6,
topic-line equal → PASS rc 0. Filename stems `funerary`, `lament`, `dirge`,
`formulae` all present in prose (concise present-participle sweep).

`python3 -B tools/check-cited-lines.py <entry>` → 0 findings, rc 0 (one-S-id-per-line
lint pass at v2). Every cited S-id (S970, S971, S972, S973, S974) exists in
`ExecRegistry95/SOURCES.append.md` (and in the SOURCES mirror), count 5/5,
`sorted(set)==ids-of-append rows`, rc 0.

## Leg 3 — registry/index (PASS, no defect)

- Census receipt (ExecRegistry95): `census.txt` shows a mirror built at
  `/fast/scratch/hyaku/kotodama-r95/ExecRegistry95/mirror/tree` and
  `sources-census.sh validate --file …` ending in exit 0. My *independent* rerun:
  I rebuilt a mirror from the lane's **own current tree** (`git archive` the freeze
  commit's `corpus/SOURCES.md` baseline + `ExecRegistry95/SOURCES.append.md`,
  entered between `## Registry` and `## Paths` of the live file, plus the new entry
  at `corpus/knowledge/linguistics/funerary-lament-dirge-formulae.md` and the mirror
  of `corpus/README.md`) and reran the census over **my** mirror:
  `sources-census.sh validate --file <my-mirror>/corpus/SOURCES.md` → rc 0
  (`--- E-codes: 0 ; W-codes: 35` — the same 35 pre-existing warnings the base tree
  carries; no new E- or W-finding from the appended rows; `ok` on the mirror path).
- Index receipt: ExecRegistry95's `index.txt` prints `CORPUS-INDEX: OK files=267
  rows=267 findings=0`. My independent rerun over my full mirror — entry + appended
  registry + *their* `README.new.md` in place of the mirror's base `README.md` —
  printed `CORPUS-INDEX: OK files=267 rows=267 findings=0`, rc 0.
- `README.new.md` vs base `corpus/README.md` (`diff -u`): 24 `+` lines, 1 `-` line.
  The `-` line is `## linguistics/ (39)` matched byte-for-byte by the same index and
  offset in the mirror `## linguistics/ (40)`; the remaining `+` lines are the
  round-95 header block (8 lines), the linguistics-block entry row (after
  `evidentiality-epistemic-marking`, before `gesture-co-speech-pointing`), and the
  new trailing `## Round 95 lament entry (2026-11-05)` section (header, 12 lines,
  total footer, `Counts checked…` block and directory-totals line). All `+` line
  strings occur byte-for-byte in `README.new.md` and all `-` line strings occur in
  the base file; no undeclared line pattern (no third-party entry block, no totals
  drift elsewhere, header block above `revision: 2.23` exactly as their README.diff
  shows). Result: touches only the declared lines, measured, rc 0.
- Registry rows in my mirror: 898 (893 base + 5 appended), highest S974; tier A 5/5,
  status mined 5/5, opened 2026-11-05 5/5, used-by exactly
  `corpus/knowledge/linguistics/funerary-lament-dirge-formulae.md` 5/5, scope
  parses 11-column (13 `|` count) 5/5 → C2/C3 grammar re-measured on my mirror,
  rc 0. (`grep -c '^| S[0-9]' = 898`; census-reported `rows` equal to 898 because
  893+5 = 898 both grammars agree.)

## Leg 4 — lesson gate (PASS with UNMEASURED caveat)

- Tool run `python3 -B tools/check-gate-quotes.py <round-95.md>` → `GATE_QUOTES: 0
  findings`, rc 0.
- Byte-equality of the Gate table quote column vs the registry anchor cells (my
  re-measurement, both `anchor quote "…"` in `SOURCES.md` and the table's quoted
  span from the lesson): S970/S971/S972/S973/S974 `byte-equal: True`, rc 0 (no
  unicode normalization was applied anywhere — the check is byte-`==`).
- Criterion 37 sweep over `## Gate` of the round-95 draft:
  `awk … | grep -E '^- ' | grep -vE '^- S[0-9]+ admit' | wc -l` = 29 bullets;
  none of the 29 lacks a topic / access / scope reason class (`criterion 37`'s rule
  per-bullet sweep): every bullet carries a reason token (`UNREACHABLE, reason class
  access:` or `excluded, reason class scope:` or `not fetchable at this locator`).
  The same sweep over the round-94 *committed* lesson prints 0 (rules survive the
  round-94 baseline — no regression introduced).

`UNMEASURED` (recorded, non-fatal): the round-95 lesson at line 58 counts
`27 query operations (25 API plus 2 site)` while the same lesson elsewhere says
263 + 2 = 265 returned/screened. 265 is stated exactly twice; 27 and the split
25+2 are stated exactly once each, in the same line, as is 253 and the split
`(DOAJ 42, OpenAlex 161, Crossref 60)`. The arithmetic identity `263 + 2 = 265` is
depended on but never re-derived inside the lesson, and 27 = 25 + 2 labels the
first two addends; `253 + 12 = 265` is also different arithmetic in the same
sentence and is never re-derived. These are stated counts, not measured identities;
if the L1 wants them verified, three one-line Python checks over the API JSON
capture files (not part of any staged evidence dir I can see) would close it. Not
a claim-C leg failure — the frozen claim legs do not measure the lesson's prose
counts.

## Leg 5 — verdict, evidence, report

- Verdict line above.
- `stage/ReviewerC95/review.md` (this file's short twin) carries the same PASS and
  the four substantive-leg outcomes in one line each; `DONE` written after it, as
  `sha256(review.md)`, per the acceptance contract.
- `Report:` trailer file written at
  `.ufo/waves/round-95/w1/stage/ReviewerC95/review.md` (full detail, including all
  commands and rc), plus this report as the graded artifact.

## Defect routed inside my repro harness (`R95-RM1`) — not a claim-C artifact defect

The harness I wrote after leg 1 (`/fast/scratch/hyaku/kotodama-r95/ReviewerC95/
review_c.py`, first two iterations) had two latent mismatches that my own
calibration caught, not defects in any graded artifact, both self-fixed before
this review:

1. `re.findall(r'^\| (S\d+) l', ...)` on the lesson was shifted by one column
   (parsed `S969` and the round-94 lullaby quote, not `S970` and this round's
   quote) — matched on a different byte shape (`l` vs `l` — a regex ambiguity),
   self-corrected after reading the actual `S965–S969` lines in the live
   `corpus/SOURCES.md`; the final re-measurement runs over this round's lesson.
2. My first independent registry mirror build reproduced a census failure (`E11`
   `S897 missing used-by …`, `E12` `S974 outside Registry section`) that the real
   grader would not face, showing the whole-class census run needs the `tools/`
   and `SKILL.md` and `reports/round-95/evidence/` files the used-by cells name;
   rebuilt on the cold-start rule (candidates from the *live* SOURCES.md tail,
   inserted before `## Paths`) → matches the receipts end-to-end.

These are scratch artifacts in **my** stage dir (none touches a graded file); the
final runs recorded above are all built on the corrected harness.

## Residual risk (from a coverage seat's perspective)

- S975–S981 remain staged-capture-only (in `ScoutTopic95/evidence/`, 12 rows
  staged, 5 in `ExecRegistry95/evidence/`, 0 landed as rows). R95-M6 already
  routes the drop-reason recording to the L1 at landing. From the coverage side
  the five landed rows do ground all **six** frozen sub-topics jointly (my
  re-measurement: the spn5 union of the five rows' verify/scope text mentions
  `professional keeners` (S972+), `antiphonal` (S970+S971), `refrain` (S974),
  `praise of the dead`/`praises` (S974), `female professional mourner`/
  `gendered mourning` (S973), and the design-procedure facet; each of the six
  frozen sub-topic phrases has ≥ 1 landing row grounding it) — no claim-C leg is
  weakened by the not-landed seven; the coverage *breadth* simply stays as wide
  as five rows can be.
- `reports/round-95/evidence/manifest.json` (the per-row capture manifest the
  grader's CAPTURE leg reads) is still not on disk (`R95-M5`, already routed):
  grader v5 entry-mode over the staged artifacts could only be driven by **my**
  manifest files living in my scratch (built from the staged artifacts byte-for-byte
  and never touching `reports/`), and returns `PASS 8/8` (and the strongest-run 9/9
  with the v6 candidate) once that manifest is staged to the grader's expected
  relative path at the L1's landing. Both receipts are recorded above.
