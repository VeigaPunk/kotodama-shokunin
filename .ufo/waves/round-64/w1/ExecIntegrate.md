# ExecIntegrate — round-64 wave 1: claim C integration proof (copy-based)

Nothing in the real lane tree was written by this seat except this report. All assembly,
counter runs and git objects live under
`/home/vgpnk/.cache/hyaku/kotodama-r64-w1/ExecIntegrate/{lane,laneB,rows-diag,diag,diag2,real}`.

## Axes named

- **Coverage** — does the assembled corpus admit the new entry plus the 26 mined rows and the
  six disposition rows with every frozen row/citation leg green?
- **Operability** — does the staged assembler `.ufo/waves/round-64/integrate-w2.py` run end to
  end on real inputs, and what exactly does a land have to add around it?
- **Calibration** — which statements in `LOG.md` / `claims.json` / the skeleton are supported by
  a measurement, and which are asserted ahead of the measurement?

## Result

`ACCEPT-C-64: PASS` (10/10 legs, exit 0) in copy `real/`, built from **the real 32 row
contributions**. That PASS required four things the staged tooling does not do by itself:
(1) stage `readme-row.txt` (D6), (2) remove the id range from the skeleton's `- source:` line, or
align the assembler's strip with it (D1), (3) flip `S687` `mined -> queued` in `corpus/SOURCES.md`
(D2), and (4) commit the assembled entry on `main` so NOHARM sees it (D3). Items (1)-(3) are
one-line/one-cell edits; all four are outside this seat's write scope, so the L1 must apply them.

Two runs of the same assembled bytes followed. The first printed the full PASS below; the second
printed `LIVE FAIL ... bad=['S733:NOT_LOCATED ...PMC5507709']` and therefore `ACCEPT-C-64: FAIL`,
with every other leg still PASS. Both results are real: the nine deterministic legs are stable, and
the LIVE leg is host-rate-limited (measured in D5). I am not calling the predicate met — the
qualifying receipt is the L1's to take, and it must be taken on a run whose LIVE leg passes.

```
FILE PASS exists lines=81 h1=1 h2=10 h3=0 topic=True
ROWS PASS bad=[] checked=26
REJECTS PASS bad=[] checked=6
ONEID PASS bad=[] marks=[] cited_lines=26 cited_lines_tool=exit0 clean=True
RESTATE PASS bad=[] lines=26
HOSTS PASS bad=[]
LINK PASS bad=[]
APPEND PASS missing_base_lines=0 s687_queued=True base=643 measured=675 +32=True
NOHARM PASS diff=['corpus/knowledge/linguistics/language-socialization-and-acquisition.md']
SWEEP PASS exit=0 topic_row=True
LIVE PASS subset=['S718', 'S723', 'S728', 'S733', 'S738', 'S743'] bad=[]
ACCEPT-C-64: PASS
EXIT=0
```

## Row inputs at run time

Both missing rows landed during this run; nothing was fabricated in the measured tree.

- `ScribeRowS723/row.txt` appeared at 23:04 (Nottingham HELM RLE, tier B, 11-word quote).
- `ScribeRowS740/row.txt` appeared later (Chang et al. 2021, Collabra, tier A; live URL 403 to a
  plain client, so the row anchors on the 20210414114152 Wayback capture).
- `python3 -B .ufo/waves/round-64/check-rows.py --rows-dir .ufo/waves/round-64/rows` →
  `CHECK-ROWS: 32/32 clean`.
- A scratch-only fixture was used earlier, while S740 was absent, to reach the downstream legs
  (`rows-diag/`, `diag/`); it is **not** part of the result above and never entered a lane path.

## Derived README index row (`readme-row.txt`, not yet in the lane)

The ScribeEntrySkeleton seat wrote `readme-row.txt` only into a scratch directory that no longer
exists (`/home/vgpnk/.cache/hyaku/kotodama-r64/ScribeEntrySkeleton/`: `No such file or directory`),
and the staged `rows/ScribeEntrySkeleton/` carries only `entry.md`. Derived from the skeleton's
`- topic:` field with `re.search(r"^- topic:(.*?)(?=\n- \w)", re.M|re.S)` and whitespace-joined
continuations — the same extraction `integrate-w2.py:readme_row_from_skeleton` and
`reports/round-28/readme/sweep.py:topic_of` perform:

```
- `language-socialization-and-acquisition.md` — language socialization and acquisition as culturally organized participation in language across caregiver interaction, early talk, correction, multilingual life, narrative, literacy, and address — a sourced design reference for fictional language practices, not a universal developmental sequence.
```

- 350 bytes including the trailing `\n` (the file's last bytes are `sequence.\n`).
- `sha256 5cc727127a9928add54e89fd80d2c803f6d876aa5b94aa96c9f2d2c29b90e26f`.
- Verified equal to the generated entry's `- topic:` text by the assembler itself (it raises
  `README topic does not exactly match generated entry - topic:` otherwise) and by
  `sweep.py` (`topic_mismatch 0`).
- To land it: `mkdir -p .ufo/waves/round-64/rows/ScribeEntrySkeleton && cp <the file> .../readme-row.txt`.
  A copy exists at `/home/vgpnk/.cache/hyaku/kotodama-r64-w1/ExecIntegrate/real/.ufo/waves/round-64/rows/ScribeEntrySkeleton/readme-row.txt`.

## Assembly (copy `real/`, real rows)

Dry-run and real run, after the two copy-only corrections:

```
$ python3 -B .ufo/waves/round-64/integrate-w2.py --root . --rows-dir .ufo/waves/round-64/rows --dry-run
DRY-RUN root=/home/vgpnk/.cache/hyaku/kotodama-r64-w1/ExecIntegrate/real
registry: append 32 rows after current final row; 643 -> 675 rows
entry: write corpus/knowledge/linguistics/language-socialization-and-acquisition.md with 26 mapped bullets
README: insert index row; linguistics header 29 -> 30; total/footer 237 -> 238; directory totals 30/29/31/29/24/95
DRYEXIT=0

$ python3 -B .ufo/waves/round-64/integrate-w2.py --root . --rows-dir .ufo/waves/round-64/rows
PLAN root=/home/vgpnk/.cache/hyaku/kotodama-r64-w1/ExecIntegrate/real
registry: append 32 rows after current final row; 643 -> 675 rows
entry: write corpus/knowledge/linguistics/language-socialization-and-acquisition.md with 26 mapped bullets
README: insert index row; linguistics header 29 -> 30; total/footer 237 -> 238; directory totals 30/29/31/29/24/95
WROTE corpus/SOURCES.md
WROTE corpus/knowledge/linguistics/language-socialization-and-acquisition.md
WROTE corpus/README.md
ASSEMBLED registry_rows=675 entry_files=238
EXIT=0
```

Measured shape of the artefacts:

- registry `643 -> 675` rows (`grep -c '^| S' corpus/SOURCES.md` → `675`); 32 appended lines plus
  the one modified `S687` line (`git diff HEAD~1 -- corpus/SOURCES.md | grep -c '^+| S'` → `33`).
- entry `81` lines, 1 `# `, 10 `## `, 0 `### `, 26 bullets, placed exactly per the assembler's
  `BULLET_MAP` (verified section by section: §1 `S726`; §2 `S718,S719,S724,S729`;
  §3 `S720,S721,S722,S723`; §4 `S725,S737,S743`; §5 `S727,S728,S738,S742`;
  §6 `S730,S731,S732,S733`; §7 `S734,S735,S736`; §8 `S739,S740,S741`; §9 no bullets).
- README: `## linguistics/ (29)` → `(30)`, one index row appended after `writing-systems.md`,
  `Total knowledge entries: 237.` → `238.`, footer `(total 237 files; directory totals 29/29/31/29/24/95)`
  → `(total 238 files; directory totals 30/29/31/29/24/95)`.

## Companion checks in the same copy

```
$ python3 -B reports/round-28/readme/sweep.py
parts {"civilizations": 95, "culture-material": 31, "linguistics": 30, "myth-symbol": 29, "synthesis": 29, "verification": 24}
rows 238 files 238
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 238 totals_ok True
footer {"date": "2026-10-23", "command": "python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge", "total": 238, "dir_totals": [30, 29, 31, 29, 24, 95]}
footer_live {"total": 238, "dir_totals": [30, 29, 31, 29, 24, 95], "order": ["linguistics", "myth-symbol", "culture-material", "synthesis", "verification", "civilizations"]}
footer_findings [] footer_ok True
readme_sha256 6f674e1ffce78e7e34b16018b5fce0bdad9eee3856816aa23990b11ecdb1a118
EXIT=0

$ python3 -B tools/check-cited-lines.py corpus/knowledge/linguistics/language-socialization-and-acquisition.md
CITED-LINES: 0 finding(s) in 1 file(s)
EXIT=0

$ python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge
root: corpus/knowledge
totals.files: 238
totals.lines: 42716
read_only: True deterministic: True
EXIT=0

$ git diff --name-only ff30a205c8d23b35f1ac533740121a955a9fda96 main -- corpus/knowledge
corpus/knowledge/linguistics/language-socialization-and-acquisition.md
```

## Defects and required land steps

### D1 — DECISIVE: the skeleton's `- source:` metadata line makes assembly fail closed

- Evidence (real rows, unmodified skeleton):
  `INTEGRATE_ERROR generated entry would fail check-cited-lines.py at line 4: S718,S743` (`EXIT=2`),
  on both `--dry-run` and the real run.
- Cause: `rows/ScribeEntrySkeleton/entry.md:4` reads
  `- source: S718–S743 in \`corpus/SOURCES.md\` are the intended evidence anchors; each inserted claim must stay within its cited row.`
  The en-dash range is two distinct S-ids on one line. `integrate-w2.py:169-172` intends to strip
  exactly this range, but its replacement target is a **different, stale sentence**
  (`"Round-64 row citations S718–S743 in \`corpus/SOURCES.md\` supply the source claims; each claim is limited to its cited row."`),
  so the replace is a no-op and the fail-closed guard at `integrate-w2.py:206-207` trips.
- Forcing control: `tools/check-cited-lines.py` reports `MULTI-ID` for a range at one line
  (its own selftest case `range-endash`), and `accept-c.py`'s ONEID leg requires *every* entry line
  carrying an S-id to carry exactly one. Leaving it in place fails ONEID as well as the guard.
- Minimal fixes (either one is sufficient; both are single-line, pre-data, and both were measured):
  - (A) skeleton: replace line 4 with
    `- source: the round-64 registry rows in \`corpus/SOURCES.md\` are the intended evidence anchors; each inserted claim must stay within its cited row.`
    — measured: assembly succeeds (`ASSEMBLED registry_rows=675 entry_files=238`) and the generated
    entry is clean (`CITED-LINES: 0 finding(s)`), which is the copy that produced the PASS receipt.
  - (B) assembler: point the replacement target at the sentence the skeleton actually carries
    (`integrate-w2.py:170` → the `- source: S718–S743 ...` line, replacement `- source: the round-64
    registry rows in ...`). Measured in copy `laneB/`: `DRYEXIT=0`,
    `ASSEMBLED registry_rows=675 entry_files=238`, `CITED-LINES: 0 finding(s)`, and
    `diff` of the two generated entries → identical. This keeps the tool's documented intent
    ("Removing the two IDs keeps the resulting entry clean") and does not depend on one skeleton
    wording.
  - Neither variant touches a counter. The rule that catches the defect is frozen and unchanged:
    the assembler's mirror guard at `integrate-w2.py:206-207`, `accept-c.py`'s ONEID leg, and
    `tools/check-cited-lines.py` (whose own selftest case `range-endash` pins the range rule).
- This is a skeleton/assembler defect, **not** a counter defect: `accept-c.py` and
  `check-cited-lines.py` are right to reject a two-id line. No counter leg was touched.

### D2 — the assembler never enacts the `S687` `mined -> queued` flip that the frozen APPEND leg requires

- Evidence (assembled copy, no flip): `APPEND FAIL missing_base_lines=0 s687_queued=False base=643 measured=675 +32=True`.
  With the flip: `APPEND PASS ... s687_queued=True`.
- Cause: `integrate-w2.py:registry_output` only appends; the routed S687 disposition is a
  modification of an existing line. `reports/round-64/accept-c.py` tolerates exactly that change
  (`tolerated`/`s687_ok` in the APPEND leg), and `reports/round-64/claims.json` and
  `LOG.md:4156` already assert it is "enacted in `corpus/SOURCES.md` by this round's claim C land".
  Nothing in the staged tooling performs it.
- Required land step (one cell): in `corpus/SOURCES.md` line 642, status cell `mined` → `queued`
  (cell index 8 of the split, i.e. the 8th `|`-delimited field).
- Calibration note: `LOG.md:4156` is presently a forward-looking claim. It is true only after this
  edit lands; until then the log overstates the tree.

### D3 — NOHARM measures commits, so the entry must be committed on `main` as part of the land

- Evidence (assembled copy, working-tree only): `NOHARM FAIL diff=[]`.
  After committing the assembled state on `main`:
  `NOHARM PASS diff=['corpus/knowledge/linguistics/language-socialization-and-acquisition.md']`.
- The leg runs `git diff --name-only BASE main -- corpus/knowledge`, so an uncommitted (or
  jj-only-working-copy) entry cannot satisfy it. Land sequence: assemble → S687 flip → commit on
  `main` → run the counter.

### D4 — the counter cannot run in a copy without `.git` (contradicts the "minus .git" copy recipe)

- Evidence: a copy carrying `corpus/`, `tools/`, `reports/round-{28,61,64}` but no `.git` gives
  `FILE PASS ...` then `ACCEPT_C_INPUT_ERROR base: git show ff30a205c8d23b35f1ac533740121a955a9fda96:corpus/SOURCES.md failed`, `EXIT=2`.
- `reports/round-64/accept-c.py` needs `git show BASE:corpus/SOURCES.md` (APPEND), `git show
  BASE:reports/round-61/reopen-quote.py` (LIVE's locator pin) and `git diff BASE main` (NOHARM).
  My copies therefore keep a read-only `.git`; the lane's own git was only ever read.

### D5 — the LIVE leg is host-flaky, and that flakiness is not row evidence either way

- **Repeatability on identical bytes.** The assembled real-data copy was measured twice, minutes
  apart, with no file changed in between:
  - run 1: `LIVE PASS subset=['S718', 'S723', 'S728', 'S733', 'S738', 'S743'] bad=[]`,
    `ACCEPT-C-64: PASS`, counter exit 0.
  - run 2: `LIVE FAIL ... bad=['S733:NOT_LOCATED https://pmc.ncbi.nlm.nih.gov/articles/PMC5507709']`,
    `ACCEPT-C-64: FAIL`, counter exit 1.
    (In my transcript the trailing shell line for run 2 printed `EXIT=0` because that `$?` came from
    the `tail` in the pipeline, not from `accept-c.py`; the counter's own verdict line is the
    `ACCEPT-C-64: FAIL` above, and its documented exit for that state is 1.)
  - Earlier diagnostic runs on the same row data: run A failed `S718` and `S733`; run B failed
    `S733`; three consecutive manual `reopen-quote.py --row S733` invocations all failed.
- Root cause measured now, as a burst of 4 requests per client with an identical
  Firefox/131 User-Agent:

  ```
  urllib (the locator's client):
     PMC5507709 ['CAPTCHA', 'CAPTCHA', 'CAPTCHA', 'CAPTCHA']
     PMC4794163 ['CAPTCHA', 'CAPTCHA', 'CAPTCHA', 'CAPTCHA']
  curl (same UA):
     PMC5507709 ['body174950', 'body174950', 'body174950', 'body174950']
     PMC4794163 ['body197731', 'body197731', 'body197731', 'body197731']
  ```

  `pmc.ncbi.nlm.nih.gov` answers the locator's `urllib` request with a
  `Checking your browser - reCAPTCHA` interstitial (~20.6 kB) while `curl` receives the article
  (~175-198 kB) — a client-fingerprint/rate interaction, not a content difference. The fallback
  path is equally unreliable: `web.archive.org` alternates between `[Errno 111] Connection
  refused` for `urllib` and, minutes later, `Failed to connect to web.archive.org:443` for `curl`
  too, while earlier answering 200.
- Content is genuinely present. Feeding curl-fetched live bytes through the locator's own
  `to_text`/`locate_in` returns `True` for both `S718`
  (`"Lebanese mothers, compared to American mothers, produced more IDS"`) and `S733`
  (`"High phonological neighborhood density and lexical frequency promoted sign acquisition, even
  after controlling for iconicity."`).
- Consequence for the predicate: with correct data, LIVE can print FAIL purely from host
  rate-limiting, and a later PASS is not proof that anything was repaired. The frozen 3-attempt /
  20 s retry budget was exhausted on `S733` at least once with correct rows. A final receipt should
  state which run it records; the assembled-tree legs (FILE…SWEEP) are deterministic and were green
  in every run.
- Scope note, not a defect: the LIVE subset is `S718,S723,S728,S733,S738,S743` (every fifth id from
  718), so `S740` is never live-reopened by the counter. Its row is honest that the UC Press host
  answers `HTTP 403` to a plain client and that it anchors on the `20210414114152` capture; the
  frozen ROWS leg checks only that the capture is a same-page capture of the live URL, it does not
  fetch either. `LINK` and `ROWS` therefore pass, and no leg claims live readability for `S740`.

### D6 — `readme-row.txt` is missing from the lane's staged rows directory

Covered above: derived bytes and sha256 are given, and the file must be placed in
`.ufo/waves/round-64/rows/ScribeEntrySkeleton/readme-row.txt` before the real run (the assembler
reads it, and fails closed without it:
`INTEGRATE_ERROR cannot read .../readme-row.txt: [Errno 2] No such file or directory`).

### D7 — stale provenance line survives assembly (calibration)

The generated entry keeps
`- verified-at: 2026-10-23 — skeleton structure prepared; cited source claims await L1 insertion and review.`
after the 26 bullets have been inserted. It is not measured by any frozen leg, but it will be
false in the landed entry; the L1 should restate it at land time.

### D8 — cosmetic: index-row placement breaks the section's alphabetical order

`sweep.py` accepts it (`topic_mismatch 0`, `missing_from_index 0`), and the assembler's contract
says "after the last backtick-bulleted row", so it is not a leg failure. The section is otherwise
alphabetical, so the row lands after `writing-systems.md` instead of between
`kinship-terminology.md` and `language-contact.md`.

## Out of scope / not adjudicated

- Review-only content judgements raised by peers (`S735` "tries to help" → success framing,
  `S719` newborn-ADS counterexample, `S733` placed in a section titled "more than one language")
  are per-row support questions. Every one of them passed the frozen mechanical legs above; I make
  no claim about their interpretive accuracy.
- No counter leg was edited or weakened. No lane file, jj state or git index was touched. No
  commits were made outside the scratch copies.

## Tooling

No installs, no upgrades: `python3 3.14.8`, `uv 0.13.0`, `git` and `curl` were already present and
sufficient.
