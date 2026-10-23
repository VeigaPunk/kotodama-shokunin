# ExecRowHarvest59 — round-59 build: claim C row harvester

Seat: `KotodamaR59.ExecRowHarvest59` (leaf executor; no delegation, no background jobs,
no other orchestration runtime). Date: 2026-10-23 UTC. Report is the only lane write;
code, fixtures and all run output stay under
`/fast/scratch/hyaku/kotodama-r59/ExecRowHarvest59/`.

## Verdict

DONE. `harvest.py` is written, self-tested on synthetic fixtures (44/44 checks, exit 0),
and exercised on the live round-59 scout reports and on round 58. The final live snapshot
(24/24 scout reports, complete set) yields 49 rows, 48 ids, 48 Gate lines, 27 draft blocks,
with exactly one ERROR and zero WARNings. The one ERROR is a real defect in a scout report,
not a tool miss: `ScoutTerminologyMuseum` uses id S645 twice (offered AUB row at report
line 32 and a "Spare" Catholic Encyclopedia row at line 95). The L1 must land exactly one
of them; `rows.md` currently contains both and is not paste-ready until that is resolved.

## Files

- `/fast/scratch/hyaku/kotodama-r59/ExecRowHarvest59/harvest.py` — 1101 lines, 46,529 bytes,
  Python 3 standard library only; sha256
  `e343ae354c7e2e97ec1294bd6323068e81bd72af23b1e79eebb9e8b803e64b2a`.
- `/fast/scratch/hyaku/kotodama-r59/ExecRowHarvest59/round59-final-out/{rows,gate,sentences}.md`
  — live snapshot (24 reports): 49 rows, 48 Gate lines, 27 draft blocks.
- `/fast/scratch/hyaku/kotodama-r59/ExecRowHarvest59/empty-out/` — measured empty wave.
- `/fast/scratch/hyaku/kotodama-r59/ExecRowHarvest59/round58-out/`, `round58-final.txt`,
  `round59-final.txt`, `empty-run.txt`, `selftest-final.txt` — retained run logs.
- This report.

No other lane file was created, edited or deleted. No installs; no package manager touched;
no process left running.

## What the tool does

Reads every `Scout*.md` in a wave build directory and extracts:

1. Claim C registry rows: lines matching `--row-regex` (default `^\| S6[0-4][0-9] \|`,
   exactly the assignment's pattern). Each row is kept verbatim; cells are split on `|`
   the way `rowcheck.py --draft` splits them.
2. Gate lines: lines matching `--gate-regex`, default the contract shape
   `- S6xx — <URL> — accessed ...` (em dash, en dash or hyphen; case-insensitive). This
   deliberately does not treat a prose bullet such as `- S608: high confidence ...` as a
   Gate line (round-58 had those and they produced false duplicates in an earlier draft).
3. `draft sentences:` blocks, verbatim. Recognised labels include `draft sentences:`,
   `## (4) Draft sentences`, `## 4. Draft sentences (...)`, `## Draft entry sentences`,
   `**Draft sentences (2-4, each ending with the id):**`. A block may be bullets, plain
   paragraphs ending in `(S6xx).`, an S-id group marker with a wrapped continuation line,
   or a fenced code block containing a heading.

Writes to `--out`:

- `rows.md` — rows only, spec seat order, one row per line, no headings, so it can be fed
  directly to `reports/round-59/rowcheck.py --draft`.
- `gate.md` — extracted Gate lines only, same order.
- `sentences.md` — draft blocks grouped under `## <Seat>`, with an HTML comment carrying
  `report:Lstart-Lend ids=...`; block text is verbatim except that code-fence delimiter
  lines are dropped.

Seat pairs and order come from the wave build spec: `role=scout` items in array order,
each item's assigned ids read from its prompt (`S600,S601` ... `S646,S647` for round 59).
`PAIR-SEQUENCE` checks that those pairs, in seat order, are the consecutive block from
`--first-id` (default 600); `--first-id` exists so the same tool can audit round 58
(`--first-id 500`) without a false warning. If the spec is unreadable, pairs fall back to
`first_id + 2i` in filename order and the run says `PAIR-FALLBACK`.

## Checks and exit codes

ERROR (exit 1):

| code | condition |
|---|---|
| `OUT-OF-PAIR` | row id outside its seat's assigned pair (or the seat has no pair) |
| `DUP-ID` | one S-id on more than one row |
| `CELLCOUNT` | `line.split('|')` is not 13 parts (11 cells) |
| `KIND` | cells[3] outside `spec, docs, paper, code, tool, dataset, talk, book, community, own-work` |
| `SOURCES-URL` | a row URL's page already appears in `corpus/SOURCES.md` (Wayback capture, scheme and `www` normalised) |
| `DUP-URL` | one page cited by two rows (captures compared by captured page, as LOCATE's same-page rule does) |
| `DUP-QUOTE` | one anchor quote, normalised to words, carried by two rows |

WARN (advisory; exit stays 0): `ROW-PATTERN` (a `| S... |` line the extraction regex does
not match, e.g. `|S605|` or `| S650 |`), `URL-COUNT` (0 or >4 URLs; LOCATE tries four),
`URL-HOST` (IP literal, localhost, dotless host or explicit port; FETCH-59 revision 1),
`SAME-PAGE` (2nd+ URL is not a Wayback `id_` capture of the first), `GATE-MISSING`,
`GATE-ORPHAN`, `GATE-DUP` (only when the duplicate Gate lines are not identical),
`GATE-PATTERN`, `DRAFT-MISSING`, `DRAFT-COUNT` (<2 or >4 sentences ending in the id),
`UNKNOWN-SEAT`, `PAIR-MISSING`, `PAIR-SEQUENCE`, `PAIR-FALLBACK`.

Exit 2 on a missing reports directory, unreadable SOURCES.md, or an invalid regex.
The tool never fetches the web; it does not re-check LOCATE/BOILER/RELEVANCE/TOPIC or
SUPPORT. Run `rowcheck.py --draft` on `rows.md` next.

Defaults are lane-read-only (`--reports` and `--spec` point at the round-59 build) and the
default `--out` is this seat's scratch directory, never the lane.

## Live snapshot (24/24 scout reports, complete set)

- 49 rows, 48 unique ids, 48 Gate lines, 27 draft blocks from 24 reports.
- All 48 assigned ids S600-S647 are present (two per seat). The 49th row is the spare S645
  that reuses the offered id; see the ERROR below.
- Every row splits into 13 parts; every kind is in the enum; no row page is already in
  `corpus/SOURCES.md`; no duplicate page or quote across rows; every row's id is inside its
  seat's pair; every id has a Gate line; no URL-host warnings.
- `PAIR-SEQUENCE` is clean: the 24 scout pairs are S600-S647 in seat order.
- One ERROR: `DUP-ID ScoutTerminologyMuseum:L95 S645 repeats ScoutTerminologyMuseum:32`.
  The first is the offered AUB `Amulets & Talismans` row; the second is the "Spare (verified
  PASS, not offered)" Catholic Encyclopedia row, which reuses S645. The L1 should drop one
  (and, if the spare is chosen, rerun rowcheck on the replacement). `rows.md` contains both
  until that edit.
- The set is complete at capture, but a scout can still amend a report. Rerun the command
  below immediately before assembly; do not paste `rows.md` wholesale while the duplicate
  stands:

```
cd /fast/scratch/hyaku/kotodama-r59/ExecRowHarvest59 && \
timeout 300 python3 -B harvest.py --out /fast/scratch/hyaku/kotodama-r59/ExecRowHarvest59/round59-final-out
```

## Evidence

### 1. Final self-test (synthetic reports)

Command and full output:

```
$ cd /fast/scratch/hyaku/kotodama-r59/ExecRowHarvest59 && timeout 120 python3 -B harvest.py --selftest
SELFTEST PASS exit-1-on-errors
SELFTEST PASS rows-count
SELFTEST PASS row-order-spec
SELFTEST PASS gate-count
SELFTEST PASS gate-first
SELFTEST PASS sentences-seat-a
SELFTEST PASS sentences-seat-b
SELFTEST PASS sentences-seat-c
SELFTEST PASS sentences-block-verbatim
SELFTEST PASS sentences-plain-paragraph-count
SELFTEST PASS gate-identical-duplicate-silent
SELFTEST PASS sentences-block-ids
SELFTEST PASS post-block-prose-excluded
SELFTEST PASS fenced-block-extracted
SELFTEST PASS wrapped-marker-and-sentences
SELFTEST PASS flag-OUT-OF-PAIR
SELFTEST PASS flag-DUP-ID
SELFTEST PASS flag-CELLCOUNT
SELFTEST PASS flag-KIND
SELFTEST PASS flag-SOURCES-URL
SELFTEST PASS flag-DUP-URL
SELFTEST PASS flag-DUP-QUOTE
SELFTEST PASS flag-ROW-PATTERN
SELFTEST PASS flag-URL-COUNT
SELFTEST PASS flag-URL-HOST
SELFTEST PASS flag-SAME-PAGE
SELFTEST PASS flag-GATE-MISSING
SELFTEST PASS flag-GATE-ORPHAN
SELFTEST PASS flag-GATE-DUP
SELFTEST PASS flag-GATE-PATTERN
SELFTEST PASS flag-DRAFT-MISSING
SELFTEST PASS flag-DRAFT-COUNT
SELFTEST PASS flag-UNKNOWN-SEAT
SELFTEST PASS flag-PAIR-SEQUENCE
SELFTEST PASS dup-quote-ids
SELFTEST PASS same-page-warns-only-608
SELFTEST PASS clean-exit-0
SELFTEST PASS clean-no-findings
SELFTEST PASS clean-rows
SELFTEST PASS missing-reports-dir
SELFTEST PASS dup-url-capture-canonical
SELFTEST PASS empty-exit-0
SELFTEST PASS empty-rows-file
SELFTEST PASS empty-sentences-file
SELFTEST PASS 44/44
exit 0
```

The fixtures cover: two-seat spec order that differs from filename order; valid row with a
same-page capture; invalid kind; short cell count; out-of-pair id; duplicate id; duplicate
quote; duplicate page (live URL plus another row's capture); SOURCES.md reuse across
`http`/`https`; loose `|S606|` row; zero-URL row; loopback/port URL; foreign fallback URL;
identical versus non-identical duplicate Gate lines; orphan Gate line; malformed Gate line;
plain-paragraph draft sentences; fenced draft block with a heading inside; wrapped group
marker; post-block prose exclusion; missing reports dir; empty reports dir with empty
outputs; clean run with no findings.

### 2. Final live harvest

```
$ rm -rf /fast/scratch/hyaku/kotodama-r59/ExecRowHarvest59/round59-final-out && timeout 300 python3 -B harvest.py --out /fast/scratch/hyaku/kotodama-r59/ExecRowHarvest59/round59-final-out
HARVEST seat=ExecRowHarvest59 reports=24 seats-with-rows=24 rows=49 ids=48 gates=48 draft-blocks=27
PAIRS 24 from /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-59/build-spec.json
ERRORS 1 WARNINGS 0
ERROR DUP-ID         ScoutTerminologyMuseum:L95 S645 repeats ScoutTerminologyMuseum:32
WROTE /fast/scratch/hyaku/kotodama-r59/ExecRowHarvest59/round59-final-out/rows.md (49686 bytes)
WROTE /fast/scratch/hyaku/kotodama-r59/ExecRowHarvest59/round59-final-out/gate.md (21198 bytes)
WROTE /fast/scratch/hyaku/kotodama-r59/ExecRowHarvest59/round59-final-out/sentences.md (20447 bytes)
EXIT 1
```

`awk -F'|' 'NF!=13'` on `rows.md` printed nothing: all 49 rows split into 13 parts.

### 3. Empty wave (measured no-change)

```
$ timeout 60 python3 -B harvest.py --reports empty-reports --out empty-out
HARVEST seat=ExecRowHarvest59 reports=0 seats-with-rows=0 rows=0 ids=0 gates=0 draft-blocks=0
PAIRS 24 from /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-59/build-spec.json
ERRORS 0 WARNINGS 0
WROTE /fast/scratch/hyaku/kotodama-r59/ExecRowHarvest59/empty-out/rows.md (0 bytes)
WROTE /fast/scratch/hyaku/kotodama-r59/ExecRowHarvest59/empty-out/gate.md (0 bytes)
WROTE /fast/scratch/hyaku/kotodama-r59/ExecRowHarvest59/empty-out/sentences.md (0 bytes)
EXIT 0
```

### 4. Round-58 smoke test (real prose, different id block)

```
$ timeout 300 python3 -B harvest.py \
    --reports /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-58/build \
    --spec /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-58/build-spec.json \
    --sources /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md \
    --row-regex '^\| S5[0-9][0-9] \|' \
    --gate-regex '^- (S5\d\d)\s*[—–-]\s*https?://\S+\s*[—–-]\s*accessed\b' \
    --first-id 500 --out round58-out
HARVEST seat=ExecRowHarvest59 reports=23 seats-with-rows=23 rows=46 ids=45 gates=45 draft-blocks=27
PAIRS 22 from /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-58/build-spec.json
ERRORS 67 WARNINGS 4
ERROR SOURCES-URL    ... (47 rows; every round-58 row is now in SOURCES.md after landing)
ERROR KIND           ... (18 rows with kind 'web', which is outside the round-59 enum)
ERROR DUP-ID         ... (1 duplicate in a round-58 report)
ERROR OUT-OF-PAIR    ... (1 row outside the round-58 prompt pairs)
WARN  SAME-PAGE      ScoutSlavicGermanContact:L10 S529 not a capture of ... (2 such)
WARN  PAIR-MISSING   ScoutHeraldry41 spec prompt names no consecutive id pair
WARN  DRAFT-MISSING  ScoutHeraldry41:L24 S575 appears in no draft sentences block
WROTE .../round58-out/rows.md (37794 bytes)
WROTE .../round58-out/gate.md (20970 bytes)
WROTE .../round58-out/sentences.md (34811 bytes)
EXIT 1
```

This run is deliberately post-landing, so `SOURCES-URL` is expected for the 47 rows already
registered; `web` is outside the round-59 kind enum, and S5xx is outside the round-59 pair
block. It is a parsing exercise, not a judgment of round 58. It proved the extractor on 23
reports / 46 rows / 27 draft blocks, including the report formats listed below. Full output:
`/fast/scratch/hyaku/kotodama-r59/ExecRowHarvest59/round58-final.txt`.

### 5. Usage-error exits

```
$ timeout 60 python3 -B harvest.py --reports /does/not/exist --out bad-out
HARVEST_INPUT_ERROR no such reports dir: /does/not/exist
EXIT 2
$ timeout 60 python3 -B harvest.py --row-regex '(' --out bad-out2
HARVEST_USAGE_ERROR bad --row-regex/--gate-regex: missing ), unterminated subpattern at position 0
EXIT 2
```

### 6. Run log

Every tool invocation in development, with outcome. Earlier iterations were run to expose
parser defects in the growing live reports; their outputs are superseded by the retained
final runs above (intermediate output files were overwritten in scratch, except the
round-58 and final logs named above).

| # | command class | result |
|---|---|---|
| 1 | `--selftest` (first version) | exit 1, 29/35; fixture defects in gate count, duplicate-URL fixture, URL-COUNT fixture, gate-pattern fixture, same-page line, clean gate |
| 2 | `--selftest` after fixture repair | exit 0, 35/35 |
| 3 | `--selftest` after heading/plain-paragraph and Gate-identity work | exit 0, 37/37 |
| 4 | `--selftest` after SOURCES page-compare and safe default `--out` | exit 0, 37/37 |
| 5 | `--selftest` after strict Gate shape and `4.` numbering | exit 0, 37/37 |
| 6 | `--selftest` after trailing-period sentence detection | exit 0, 38/38 |
| 7 | `--selftest` after wrapped group-marker continuation | exit 0, 39/39 |
| 8 | `--selftest` after fenced-block handling | exit 0, 40/40 |
| 9 | `--selftest` after missing-dir error | exit 0, 41/41 |
| 10 | `--selftest` after URL-HOST check | exit 0, 42/42 |
| 11 | `--selftest` after dead-code cleanup | exit 0, 42/42 |
| 12 | `--selftest` after failed pair-sequence patch attempt (no file change) | exit 0, 42/42 |
| 13 | `--selftest` after pair-sequence audit | exit 0, 43/43 |
| 14 | final `--selftest` after `--first-id` | exit 0, 43/43 |
| 14b | `--selftest` after live-capture duplicate test | exit 0, 44/44 (final, pasted above) |
| 15 | live, 5 reports already present (misnamed `round59-empty-out`) | exit 0, 10 rows, 10 warnings |
| 16 | live, 6 reports | exit 0, 12 rows |
| 17 | live, 10 reports | exit 1, 21 rows, 1 error, 13 warnings |
| 18 | live, 13 reports | exit 1, 27 rows, 1 error, 4 warnings |
| 19 | live, 13 reports | exit 1, 27 rows, 1 error, 1 warning |
| 20 | live, 16 reports | exit 1, 33 rows, 1 error, 2 warnings |
| 21 | live, 16 reports | exit 1, 33 rows, 1 error, 0 warnings |
| 22 | live, 18 reports | exit 1, 37 rows, 1 error, 0 warnings |
| 23 | live, 19 reports | exit 1, 39 rows, 1 error, 0 warnings |
| 24 | live, 20 reports | exit 1, 41 rows, 1 error, 0 warnings |
| 25 | live, 22 reports | exit 1, 45 rows, 1 error, 0 warnings |
| 26 | live, 23 reports | exit 1, 47 rows, 1 error, 0 warnings |
| 26b | final live, 24 reports (complete set) | exit 1, 49 rows, 1 error, 0 warnings (pasted above) |
| 27 | round-58 smoke, first version | exit 1, 67 errors, 14 warnings |
| 28 | round-58 smoke, after strict Gate shape | exit 1, 67 errors, 4 warnings |
| 29 | round-58 smoke, final with `--first-id 500` | exit 1, 67 errors, 4 warnings (pasted above) |
| 30 | empty reports dir, first and final | exit 0, zero-byte outputs (final pasted above) |
| 31 | `--help` | exit 0 |
| 32 | missing reports dir; bad regex | exit 2, exit 2 (pasted above) |

## Defects the live reports exposed and the tool now handles

- `ScoutWordAmulets` wraps the whole draft block in a code fence and opens it with a
  `## Words as the working part` heading. The first version stopped at that heading and
  reported both rows as `DRAFT-MISSING`; fence state is now tracked so a heading inside a
  fence is text.
- `ScoutCommodificationTrade` continues an S647 group marker on a second, unindented line
  ("myth's naturalisation):"). The first version ended the block there and lost both S647
  sentences; a non-content line that follows a marker without a blank now continues it.
- Plain-paragraph draft sentences ending `(S632).` (WestAfrica, ConcealedObjects,
  TerminologyMuseum, MagicalGems, IslamicTalismans) were first read as intro prose because
  of the trailing period; sentence lines now allow `.`, `!` or `?` after `(S6xx)`.
- `ScoutHamsaHand` notes bullets `- S608: high confidence ...` were first extracted as Gate
  lines and produced false `GATE-DUP` warnings; Gate extraction now requires the contract
  URL and `accessed` shape.
- Reports use at least four draft labels (`draft sentences:`, `## 4. ...`,
  `## Draft entry sentences`, `**Draft sentences (...):**`); all are matched now.

## Risks and limits

1. The live set is moving. The final snapshot named above had 23 of 24 scout reports; the
   L1 must rerun after the last seat before assembly. The tool is deterministic for a fixed
   report set.
2. `rows.md` is a harvest, not an integration: it preserves duplicate ids and malformed
   rows so the flags can point at them. The current S645 duplicate must be resolved before
   padding the entry; `rowcheck.py --draft` would otherwise check both rows.
3. Row extraction follows the assignment's exact prefix pattern. A scout row written
   `|S605| ...` or `|  S600  |` is flagged `ROW-PATTERN` but not extracted; rerun with
   `--row-regex` after deciding the format, or have the scout fix it. A row line inside a
   fenced example is indistinguishable from a real row and would be extracted.
4. Gate extraction requires a URL and `accessed` in the contract position. A Gate line
   missing either is not extracted; if it still has `- Sxxx — URL`, it is flagged
   `GATE-PATTERN`. A Gate line with no URL is invisible.
5. Draft-block boundaries are heuristic. A prose paragraph after a blank ends the block;
   a sentence not ending in `(S6xx)` after bullets can be cut. `DRAFT-MISSING` and
   `DRAFT-COUNT` are the guard, and they were clean on all 23 live reports.
6. `DUP-QUOTE` compares words after normalisation; a close paraphrase is not flagged.
   `DUP-URL`/`SOURCES-URL` compare pages after lowercasing, stripping `www`/scheme and
   resolving a Wayback capture to its original; a different query string or path is a
   different page.
7. The tool does not judge whether a quote is body text, carries its teaches cell, or
   passes CHARM-GUARD/TOPIC; that remains `rowcheck.py` and the blind SUPPORT packet.
8. Pair assignment trusts the build spec prompts. `PAIR-SEQUENCE` checks they form a
   consecutive block from `--first-id`; a spec whose prompts disagree with the declared
   seat order would be flagged, not silently repaired.

## Tooling, process and blockers

- No installs or updates; no pacman, uv, npm or cargo transaction.
- Every shell command ran with `timeout` and with cwd
  `/fast/scratch/hyaku/kotodama-r59/ExecRowHarvest59/`. No relative output was written from
  the lane root. No git/jj write commands; no sandbox clone was needed because the tool
  only reads the lane.
- The only lane write is this report at
  `.ufo/waves/round-59/build/ExecRowHarvest59.md`.
- Blockers: none. The one live row defect (S645 duplicate) is reported for the L1 to
  resolve; it is not a tool blocker.
