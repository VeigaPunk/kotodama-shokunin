# ExecLintTool — round 61 wave 1, claim O build (clause-scoping lint)

Seat: `KotodamaR61.ExecLintTool` (leaf executor). Measured revision in a sandbox clone:
`78ad4b176695e9fcd490ab607cb8218e2ce62738`. The counter `reports/round-61/accept-o.py` was **not
run** (that is the L1's first data run); its sha256 in the clone is
`1ac83e18cb83576b6935944d5d38acacfa50b662ef0df16676736a8f5dde44cd`, matching the assignment.

## Files changed

- Built (outside the lane, per assignment):
  `/fast/scratch/hyaku/kotodama-r61/ExecLintTool/check-cited-lines.py`
  sha256 `443af102a3a68f1a4b4c609a5a66cffb8e917a6fc23a68bec9c853076feb9259`
  (11 822 bytes, Python 3 stdlib only). Destination for the L1: `tools/check-cited-lines.py`.
- Nothing was written in the lane or the fleet repo except this report.
- No installs, no upgrades, no host services touched.

## Behavior (the contract verbatim)

`python3 -B tools/check-cited-lines.py PATH [PATH ...]` reads each PATH (a file, or a directory
walked recursively for `*.md`; walk order is deterministic — directory names sorted, file names
sorted). An S-id is `\bS\d{3,}\b`. Per line, in line order:

- `MULTI-ID <path>:<lineno> <ids>` when the line carries two or more distinct S-ids
- `TABLE-ID <path>:<lineno> <ids>` when the line, leading whitespace removed, starts with `|` and
  carries at least one S-id

`<ids>` are that line's distinct ids sorted numerically and comma-joined with no space; a line may
give both findings, MULTI-ID first. Last stdout line is
`CITED-LINES: <k> finding(s) in <m> file(s)` where k counts findings (a two-id table row is two)
and m counts the Markdown files read (a file argument counts one). Exit 1 when k > 0, 0 when k = 0,
2 with `CITED_LINES_ERROR <message>` on stderr and nothing on stdout when there is no PATH, a PATH
does not exist, a PATH is neither regular file nor directory, or a file is unreadable / not valid
UTF-8. `--selftest` runs 26 in-process cases (line-scoping cases plus CLI cases through the real
`main()`) and ends with `selftest 26/26`; it takes no PATH and any PATH after it is an input error.
The source names neither `reports/` nor `accept-o` (`grep -cE 'reports/|accept-o'` → 0), so the
counter is not loaded or referenced.

## Retained evidence

### 1. Selftest, full stdout, `timeout 300 python3 -B check-cited-lines.py --selftest` (exit 0)

```
PASS multi-comma
PASS multi-semicolon
PASS multi-slash
PASS multi-and
PASS range-ascii
PASS range-endash
PASS sorted-numeric
PASS sorted-numeric-four
PASS repeated-one-id
PASS lookalikes
PASS two-digit-only
PASS table-leading-spaces
PASS table-leading-tab
PASS table-two-ids
PASS table-no-id
PASS table-not-leading
PASS cli-single-file-clean
PASS cli-single-file-findings
PASS cli-directory-md-only
PASS cli-summary-counts-findings
PASS cli-crlf-line-number
PASS err-missing-path
PASS err-no-path
PASS err-invalid-utf8-file
PASS err-invalid-utf8-in-directory
PASS err-selftest-with-path
selftest 26/26
exit=0
```

Each case is built to fail under one named plausible bug: separators (`,`, `;`, `/`, ` and `)
against a single-separator matcher; `S612-S615` / `S612–S615` as two end ids against a
range-expanding or range-as-one-token matcher; numeric sort `S613,S652,S700,S6120` against a
lexical sort; one repeated id against counting matches instead of distinct ids; `XS612 S612x S612_
s612 S61 S6` against an unanchored or `\d+` regex; `S12 S34` against `\d{2,}`; leading-space and
leading-tab table rows against a `^|`-only or no-`lstrip` matcher; pipe-after-prose against
`"|" in line`; a two-id table row giving both findings and `k=2` against a per-line counter;
`.txt` ignored inside a directory walk and the `.md`-file count against counting every file;
CRLF line numbering; invalid UTF-8, missing path and no-args all exit 2 with the stderr marker
against `errors="replace"`/exit-0-on-error behaviour.

### 2. Corpus run on the pinned `git archive` export

Export: `git -C clone archive 78ad4b176695e9fcd490ab607cb8218e2ce62738 corpus/knowledge | tar -x -C
/fast/scratch/hyaku/kotodama-r61/ExecLintTool/base` (235 `*.md` files).
Run: `cd .../base && timeout 300 python3 -B ../check-cited-lines.py corpus/knowledge` → **exit=1**,
full output retained at `/fast/scratch/hyaku/kotodama-r61/ExecLintTool/corpus-run.txt` (604 lines).

Summary line (last):

```
CITED-LINES: 603 finding(s) in 235 file(s)
```

First 10 findings:

```
MULTI-ID corpus/knowledge/civilizations/kongo-kingdom.md:16 S395,S397
TABLE-ID corpus/knowledge/civilizations/kongo-kingdom.md:42 S359
TABLE-ID corpus/knowledge/civilizations/kongo-kingdom.md:43 S404
MULTI-ID corpus/knowledge/civilizations/kongo-kingdom.md:44 S374,S375
TABLE-ID corpus/knowledge/civilizations/kongo-kingdom.md:44 S374,S375
MULTI-ID corpus/knowledge/civilizations/kongo-kingdom.md:45 S380,S382
TABLE-ID corpus/knowledge/civilizations/kongo-kingdom.md:45 S380,S382
TABLE-ID corpus/knowledge/civilizations/kongo-kingdom.md:46 S361
TABLE-ID corpus/knowledge/civilizations/kongo-kingdom.md:47 S394
TABLE-ID corpus/knowledge/civilizations/kongo-kingdom.md:48 S389
```

The R60-M6 line the REAL leg pins is present:

```
MULTI-ID corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md:95 S612,S613
```

### 3. Independent replication cross-check (my own code, not the counter)

A fresh scratch replication of the contract (own walk, own regex, `str.lstrip`) over the same export
equals the tool's parsed finding set exactly: `want 603 got 603 files 235 equal True missing []
extra []`, exit 1, empty stderr, and the R60 line detected (`r60 True`).

### 4. Randomized GEN/CLEAN/ERR controls (my own generators)

- 20 randomized fixture trees (4 `.md` files in random nested dirs, a `.txt` decoy, random ids and
  separators, all eight line kinds, shuffled): **20/20** matched the replication's finding set, exit
  1, exact summary `k`/`m`, no unparsed stdout lines.
- 20 randomized clean files (plain/single/repeated-id/lookalike/table-without-id lines): **20/20**
  exit 0 with exactly `CITED-LINES: 0 finding(s) in 1 file(s)` and empty stderr.
- Unreadable file (mode 000): exit 2, empty stdout,
  `CITED_LINES_ERROR cannot read unreadable.md: Permission denied`.

## Ledger (predicted legs, not a receipt)

TOOL (26/26 last line, exit 0), INDEP (no `reports/`, no `accept-o` in source), GEN (exact match,
602-line-scale reasoning above plus 20/20 randomized), CLEAN (0 findings, one file), ERR (missing
path, invalid UTF-8 each exit 2 with stderr marker), REAL (603 findings, 235 files, R60-M6 line in
the set) are all consistent with the frozen contract. The actual `ACCEPT-O-61: PASS|FAIL` line and
exit code belong to the L1's first run of `accept-o.py`.

## Risks

- The randomized cross-checks use my own replication of the contract, not the counter's `reference()`;
  a difference in the counter's fixture generator beyond the shapes I mirrored would not be caught
  here. The shapes mirrored are all of `gen_line`'s kinds as read from the counter source.
- Finding order is deterministic (sorted dirs/files, MULTI before TABLE per line), but the counter
  compares finding sets, so order is not load-bearing.
- The real corpus finding count (603) is large; that is data about the base corpus, not a tool
  defect, and the REAL leg does not impose a cap.
- `--bogus`-style argparse usage errors exit 2 through argparse with usage text, not a
  `CITED_LINES_ERROR` line; the contract does not specify that case and no leg exercises it.

## Blockers

None. The tool is complete and self-tested; it was deliberately not placed in the lane.
