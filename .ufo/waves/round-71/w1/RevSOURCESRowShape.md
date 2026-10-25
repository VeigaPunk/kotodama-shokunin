# RevSOURCESRowShape — round-71 w1 findings

Seat: L1Kotodama71.RevSOURCESRowShape · leaf reviewer · read-only
Date: 2026-10-25 · Scope: row-shape rule for this round's expected new SOURCES rows.

## 1. Column grammar (CORPUS.md § SOURCES.md / SOURCES-CONTRACT-v1)

The registry table has **11 columns**, in this exact order (CORPUS.md:86,
contract v1 lines 19–41):

`id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by`

Cell grammar (contract):
- `id` — `S` + 3 or more digits; next unused; never reused; **no `|` inside any cell**.
- `kind` — enum `spec | docs | paper | code | tool | dataset | talk | book | community | own-work`.
- `tier` — `A | B | C`; `community` never A.
- `status` — `queued | mined | rejected`.
- `opened` — ISO date (past/present). `recheck` — ISO date, `NNd`, or symbolic (`on-release`, `annual`, …).
- `used-by` — comma-separated repo-relative paths or `—`.

## 2. Acceptance grammar (verified on scratch fixtures)

Two parser generations exist; both were exercised:

**Maintained parser** `scripts/sources-census.sh` (acceptance documented at
CORPUS.md:150–155: "accepts 0–3 leading ASCII spaces before Markdown table rows
and headings; 4 or more spaces are indented code and are ignored"):

- Row gate: `^ {0,3}\|` (also for `##`/`#` headings and the `|---|` separator) — after stripping 0–3 spaces, split on `|`.
- Row identity: post-strip `^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|`.
- **11 columns ⇔ NF=13** (split on `|`: `$1`/`$13` empty, `$2…$12` = id…used-by).
  NF≠13 → `E01` (validate), reported `fields=N-2`.
- **No pipe inside a cell**: a literal `|` in a cell raises NF>13 → `E01`;
  there is no escaping mechanism (no `\|` handling) in any parser.
- Rows count only inside the `## Registry` section; table-shaped `S…` rows
  elsewhere → `E12`; 4+ leading spaces → ignored entirely (code block).

**Frozen manual census** (contract lines 64–81; `reports/round-49/run-validation.py`
CENSUS verbatim): column-zero only — row regex `^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|`,
malformed check `NF!=13` must print 0, etc. Indented rows are invisible to it.

## 3. Empirical results (scratch in /tmp; nothing mutated)

| fixture | maintained census | maintained validate | claim-C grep `^ {0,3}\|…S[0-9]{3,}` | frozen grep `^\|…` | frozen awk NF!=13 |
|---|---|---|---|---|---|
| 2-row: S861 @0 indent + S862 @3 spaces | rows=2, tier.B=2, queued=2 | `ok`, exit 0 | 2 | 1 (only S861) | 0 |
| S881 @1 space + S882 @2 spaces | rows=2 | `ok`, exit 0 | 2 | 0 | 0 |
| neg: S871 pipe-in-cell (NF=14), S872 @4 spaces, S873 outside Registry | rows=1 (S871; S872 ignored; S873 not in Registry) | `E01 S871 fields=12`, `E12 S873 row outside Registry section`, exit 1 | — | — | 1 |

- Per-row NF on the 2-row fixture: S861=13, S862=13 (11 columns confirmed).
- `sources-census.sh selftest` passes in full, including `indented-valid-{0,1,2,3}-counted` /
  `-clean` (and E06/E11/E12 variants at each indent width).
- Live registry today: 784 rows, all column-zero (0 rows with 1–3 leading spaces);
  frozen and maintained counts agree at 784.

## 4. Findings

- **V1 (confirms claim): the current registry accepts rows with 0–3 leading
  spaces.** The maintained parser counts and validates them (exit 0); the
  round-71 claim-C counting command
  `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md` also counts
  them (verified 2/2 on the 0/3-space fixture). Zero- to three-space indentation
  is safe for this round's expected new rows.
- **V2 (confirms): 11-column rule NF=13** holds; malformed rows (NF≠13) are
  flagged (E01) and never crash the scan; frozen malformed check prints 0 on
  well-formed rows.
- **V3 (confirms): no-pipe-inside-cell rule** — a pipe inside a cell breaks NF
  → E01; it also mis-shifts later cells (e.g., status enum check fires on a
  shifted field), so it cannot silently pass.
- **V4 (consistency note): the frozen seven census commands are column-zero
  only.** If new rows were written 1–3 spaces indented, the frozen commands
  (including `run-validation.py`) would silently undercount rows and skip those
  rows' histogram/duplicate/enum checks; the maintained parser and the claim's
  own grep would count them. Documented intent (CORPUS.md:150–155), not a
  defect — but any seat running the frozen seven must know the gap.
- **V5 (residual risk): the claim-C grep is weaker than the full row matcher** —
  it drops the trailing `|` and the `## Registry` restriction, so an indented
  `| S…` line outside the registry would overcount. None exist today; live count
  784 agrees with the strict matcher.
- **V6 (adjacent, out of row-shape scope):** `tools/source-audit-inventory.py
  --json --summary --root corpus/knowledge` prints no registry row count; the
  claim's "registry 784 rows" wording does not come from that tool's output.
  Flag for the claim-fidelity seat.

## 5. Verification gaps

None material. All scratch fixtures and runs done in /tmp; no lane/fleet file
touched. No tools installed (gawk/bash/coreutils already present).
