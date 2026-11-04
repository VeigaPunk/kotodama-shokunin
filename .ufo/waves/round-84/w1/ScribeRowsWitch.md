# ScribeRowsWitch — round 84, wave 1 (claim D registry rows S914–S918)

## Behavior

Opened all five candidate pages by plain HTTP GET on 2026-11-04 (UA
`kotodama-scribe/1.0`), recorded status, bytes, sha256 and Wikisource
revision, probed same-URL captures through the Wayback CDX API (the
availability API answered HTTP 429 throughout), and verified every located
quote against the served bytes in raw and whitespace-folded form. Wrote
the four mined 11-cell rows plus the S918 rejection row, the Gate bullets
the round lesson copies, and the recheck cadence.

Division of labour across the four mined rows (kept complementary, one topic
each so the entry can cite three or four without duplication):

- S914 EB11 "Witchcraft" — the accusation grammar and the confession
  ("admissions ... described as voluntary").
- S915 Williams, *The Superstitions of Witchcraft* — the Malleus criminal
  code as procedure (arrest on rumour) plus the black/gray/white taxonomy.
- S916 the Bull of Innocent VIII — the institutional warrant and the
  crime's definition.
- S917 Upham, *Salem Witchcraft* — the slander law in action and the
  social base of the Salem outbreak.
- S918 EB11 "Sorcery" — rejected: a 71-word dictionary stub, definition
  and etymology only; kept as the rejection row with its flip condition.

Row conformance: 5 rows, 11 cells each, no `|` inside any cell, longest
cell 916 chars, `teaches` 176–369 chars, `opened` 2026-11-04; S914–S917
`mined`, S918 `rejected` with its reason and flip in `teaches`,
`used-by` `corpus/knowledge/myth-symbol/witchcraft-sorcery-accusation-institution.md`,
anchor quotes 14–21 words.

## Gates

- `python3 -B tools/check-row-fragments.py --selftest` — `SELFTEST: PASS
  10/10`, exit 0. Its contract, as read from the source: scan mode walks a
  rows dir for `row-*.txt` fragments; each fragment's `ROW=` line must be
  an 11-cell Markdown row (cells are `line.split("|")[1:-1]`, so a `|`
  inside a cell destroys the count), the `teaches` cell is capped at 240
  chars, `status` must be `mined`, `opened` must equal the tool's constant,
  `used-by` must contain the tool's constant entry, `tier` must be A or B,
  the first URL must be present, a Wayback capture URL must end the source
  cell and normalize-equal the first URL, the anchor's quoted span must be
  8–25 words, and `BULLET=` must carry at least six words of length ≥ 4;
  findings print as `FRAG: <file>:<label>: <finding>` with a
  `FRAG: k finding(s) in m file(s)` summary and exit 0/1 (2 unreadable).
  **Calibration finding:** the scan-mode constants are round-65's
  (`EXPECTED_OPENED = 2026-10-24`, `ENTRY =
  corpus/knowledge/culture-material/games-play-sport-contests.md`, default
  rows dir `.ufo/waves/round-65/rows`), so the tool cannot grade round-84
  rows as committed; only its selftest is round-neutral. Recorded, not
  worked around.
- Scratch mirror of the frozen `corpus/SOURCES.md` plus the five rows,
  with one placeholder file per existing `used-by` path so E11 resolves:
  `../scripts/sources-census.sh validate --file
  <mirror>/corpus/SOURCES.md` (the validator lives in the fleet root, one
  level above the lane) → **exit 0**, zero E findings, 33 W warnings
  (all pre-existing W01/W04 from the frozen registry; none on S914–S918).
  The registry count in the mirror is 837 → 842 rows.
  The mirror lives outside the lane and is not citable evidence.

## Touched surfaces

Written (all under `.ufo/waves/round-84/w1/`):

- `stage/ScribeRowsWitch/rows.md` — the five rows, one line each.
- `stage/ScribeRowsWitch/gate.md` — per-row URL, access date, locator,
  quote and calibration, plus the S918 rejection record.
- `stage/ScribeRowsWitch/recheck.md` — cadence per row and why.
- `stage/ScribeRowsWitch/S914.txt`, `S915.txt`, `S916.txt`, `S917.txt`,
  `S918.txt` — fetch receipts with capture probes and quote counts.
- `stage/ScribeRowsWitch/census-mirror.txt` — validator command, exit code
  and finding counts.
- `ScribeRowsWitch.md` — this report.

No tracked lane file, no `corpus/SOURCES.md`, no `SKILL.md`, no entry and
no tool was modified. No git or jj command was run; nothing committed.

## Out of scope / not done

- Did not land the rows into `corpus/SOURCES.md` (L1 lands every byte) and
  did not edit the entry's `used-by` cells beyond naming the entry path in
  the five new rows.
- Did not run `reports/round-84/accept-d84.py`; the counter grades
  committed bytes, and nothing is committed yet.
- Did not touch `corpus/QUALITY.md`, `considerthese/`, `.ufo/state/`,
  `MANIFEST.json` or any sibling lane.

## Findings

1. **EB11 "Sorcery" serves a body; the rejection rests on content, not
   unquotability.** The L1's first premise ("only the Wikisource header +
   a Proofreadpage template, no article body") was a stripper artefact,
   which the L1 accepted on 2026-11-04: the body sits at raw byte 45964 of
   the same 60,730-byte read, one paragraph at p. 431, and the headword is
   split by an inline `<b>` tag, so a literal phrase grep returns 0. The
   S915 substitution (Williams) stands because the book carries far more
   substance for the scope; the EB11 stub is now recorded as REJECTED row
   S918 with its reason (71-word dictionary stub, definition only, zero
   accusation/trial/torture/evidence/law vocabulary) and its flip (a full
   EB11 article body transcribed at the same URL).
2. **S916 is scoped to the Bull, not the treatise.** The Malleus landing
   page (216,384 bytes, revision 15491287) is marked "This work is
   incomplete" and carries only front matter and contents; mainspace
   probes `Question_1/_2/_3/_14/_15/_16` all answer HTTP 404. The row
   therefore claims only the institutional warrant, and the entry must
   source the trial procedure from S914/S915, not from this row.
3. **S914's capture is a different render.** The 2026-01-29 capture is
   86,021 decoded bytes against the live 98,968 (an earlier Parsoid
   render), but the located quote is present once in the capture, so the
   span is render-stable even though the byte stream is not.
4. **The named pre-integration checker is not round-safe** (finding under
   Gates): `tools/check-row-fragments.py` scan mode is pinned to
   round-65's opened date and entry path; only `--selftest` is
   round-neutral. Any round-84 seat asked to run it in scan mode would get
   a false failure.
5. **S914 cannot carry the repeal.** The EB11 article ends at the
   psychology section and never mentions the 1735 Act; the entry's
   "slander law"/repeal material must not cite S914 for it.
6. **S915's rule detail is second-hand.** Williams prints Ennemoser's
   abstract of the Malleus's Third Part; the row says so, and the entry
   should quote it as a lead, not as the 1489 text.
7. Probe mechanics: the Wayback availability API returned HTTP 429 on
   every attempt (including one retry after 25 s); the CDX API answered
   normally and supplied all capture timestamps, statuses and digests.
   The Bull has no capture at all (all-time CDX `[]`), matching the
   round-83 S911 precedent.
8. **L1 telemetry receipts carry absolute scratch paths.**
   `python3 -B tools/check-cited-records.py --root . --from-round 84
   --bind-round 84` prints `CITED-RECORDS: 0 empty / 6 scratch`, all six
   from `reports/round-84/telemetry/smoke-d*.txt` and `smoke-o*.txt`
   (they cite an absolute per-seat scratch tree; the exact path is
   deliberately not reproduced here). The
   checker does not scan `.ufo/waves`, so this seat's documents contribute
   zero; the L1 files are the L1's to rewrite before landing (QUALITY 31).

## Artifact paths (repo-relative)

- `.ufo/waves/round-84/w1/stage/ScribeRowsWitch/rows.md`
- `.ufo/waves/round-84/w1/stage/ScribeRowsWitch/gate.md`
- `.ufo/waves/round-84/w1/stage/ScribeRowsWitch/recheck.md`
- `.ufo/waves/round-84/w1/stage/ScribeRowsWitch/S914.txt`
- `.ufo/waves/round-84/w1/stage/ScribeRowsWitch/S915.txt`
- `.ufo/waves/round-84/w1/stage/ScribeRowsWitch/S916.txt`
- `.ufo/waves/round-84/w1/stage/ScribeRowsWitch/S917.txt`
- `.ufo/waves/round-84/w1/stage/ScribeRowsWitch/S918.txt`
- `.ufo/waves/round-84/w1/stage/ScribeRowsWitch/census-mirror.txt`
- `.ufo/waves/round-84/w1/ScribeRowsWitch.md`
