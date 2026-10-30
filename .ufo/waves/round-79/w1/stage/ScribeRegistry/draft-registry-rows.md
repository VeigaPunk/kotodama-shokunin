# Draft SKILL.md registry rows — round 79 W1 (ScribeRegistry)

Status: DRAFT for L1 integration. Not applied to `SKILL.md`. Rows are appended inside the
first registry table after the last body row (base: line 709 is the last row; line 710 is blank),
never edited in place. Each candidate below states which cells are fixed now and which cells are
filled only from committed bytes at the lands revision; a candidate row is invalid until those cells
are filled, and `skill-row-check.py --rev <lands> --root <lane> --rows <names>` must print `ROW OK`
for it.

## 1. Required fields (contract the checker enforces)

Header, exact: `| name | kind | entry command | verdict map | self-test | pinned values | write scope | owner |`

| field | rule for a gate/probe row | checker code on violation |
|---|---|---|
| name | non-empty, unique in the file | NAME-EMPTY, NAME-DUP |
| kind | starts with `gate`, `probe` or `note`; `note` rows are exempt from the tool fields | KIND |
| entry command | a backticked `python3 [-B] <path>` or `sh` command; `<path>` exists at `--rev` (committed bytes) or in `--root` | CMD-EMPTY, CMD-NOT-PYTHON, CMD-PATH-ABSENT |
| verdict map | contains the exit codes 0, 1 and 2 as standalone numbers | VERDICT-NOCODES |
| self-test | a `--selftest` command, or a parenthesised reason that no selftest exists (a bare dash is a finding) | SELFTEST-BARE |
| pinned values | non-empty and not a bare dash; cells naming a frozen sha256 or commit are the strong form | PINNED-BARE |
| write scope | names the write discipline (read-only, scratch, regenerates, tempfile, clone, ...) | WRITE-EMPTY, WRITE-NOSCOPE |
| owner | non-empty | OWNER-EMPTY |

Cell rule (GFM): an unescaped `|` inside a code span still separates cells. Write `\|`.
Where a row's cell contains the verdict text `PASS|FAIL`, write `PASS\|FAIL`.

Not enforced by the checker (review-only, stated limits): that the verdict map matches the script's
real exit codes; that a pinned value is correct; that placeholder text is absent (a cell reading
`pending` passes the shape check). Consumers must run the counter itself.

## 2. Base findings (`SKILL.md` at 44f76d45, read-only probe)

Observed by `probe-base-rows.txt` (62 rows graded across two tables: 25 OK, 37 with findings).

| class | rows | observed cause | repair route |
|---|---|---|---|
| SHAPE (9 cells) | `accept-c-66` (686), `accept-ca-66` (687), `accept-o-66` (688), `accept-c-67` (689), `accept-ca-67` (690), `accept-o-67` (691) | verdict cell `ACCEPT-*: PASS…FAIL` contains an unescaped pipe between PASS and FAIL | append-only correction note (section 3, N1); do not edit the six rows |
| VERDICT-NOCODES | `uncertainty-inventory` (658) | verdict map gives 0 and 2 but no 1 | correction note (N2); the row's script exit 1 meaning is undocumented in the row |
| SELFTEST-BARE (20) | accept-c-53, -54, -55, -56, -57, -58, -59; accept-d-59, -60, -62; accept-c-61, -63, -64, -65, -68; accept-o-62, -63, -64; accept-ca-64, -65 | the counter has zero `--selftest` occurrences at base (grep count 0 each; `selftest-mentions.txt`), so the dash is accurate but carries no reason | correction note N3 giving the reason per row; no in-place edit |
| PINNED-BARE (30) | every counter row with a dash in pinned values (list in `probe-base-rows.txt`) | not yet read per counter; the pin may live in the script (QUALITY 23/25/28), but the row does not say so | correction note N4 pointing to the script's pin location, or accept as backlog |
| row 709 note | `accept-c-73 / accept-ca-73 correction` | kind `note`; prose verdict; now passes (`ROW OK`) because note rows are exempt | none |

No row names a script that is absent at base: CMD-PATH-ABSENT never fires on the 44f76d45 tree.

## 3. Append-only correction notes (candidate text; registry note-row pattern of row 709)

These are `note` rows. They keep every historical row byte-identical and name the cell they correct.
Row text is candidate wording for L1 to review; the cell values are the observed base values.

| name | kind | entry command | verdict map | self-test | pinned values | write scope | owner |
|---|---|---|---|---|---|---|---|
| N1 accept-*-66/67 shape | note | — | Correction of rows accept-c-66, accept-ca-66, accept-o-66, accept-c-67, accept-ca-67, accept-o-67: the verdict cell has an unescaped pipe between PASS and FAIL, which splits the row into nine cells in a GFM table. The intended cell escapes that pipe (backslash before it), with the same text: exit 0/1, 2 on unusable input. Historical rows unchanged. | — | — | — | kotodama-shokunin |
| N2 uncertainty-inventory | note | — | Correction of row uncertainty-inventory (line 658): the verdict map omits exit 1. The row reads `0 inventory produced, not scholarship verified / 2 could-not-evaluate`; exit 1 is not stated. L1 must read the script docstring before writing the meaning of 1. | — | — | — | kotodama-shokunin |

N3 and N4 are to be written only after the 20 SELFTEST-BARE and 30 PINNED-BARE rows are each re-read
against their counter (`selftest-mentions.txt` supplies the selftest grep; the pinned location is per-counter and not yet read).
They are NOT drafted here as final text. Writing them now would assert pin locations that were not observed.

## 4. Candidate rows for this round's claims (pending lands)

Shape used by accept-c-74 .. accept-ca-75 (the most recent rows); the new rows copy it.

### A. Ledger-token guard (O capability tool) — pending `tools/ledger-token-guard.py` at lands

| cell | value now | depends on lands |
|---|---|---|
| name | `ledger-token-guard` | no |
| kind | `gate` (grades a stated token against committed bytes) | no |
| entry command | `python3 -B tools/ledger-token-guard.py <its CLI flags as landed>` | yes: flags, arity, and the `--lands`/`--freeze`/`--work` names must be read from the landed file |
| verdict map | `0 clean / 1 token mismatch / 2 refused or could-not-evaluate` | yes: each code must be confirmed against the landed docstring and selftest |
| self-test | `python3 -B tools/ledger-token-guard.py --selftest` | yes: confirm the flag exists and prints a verdict line |
| pinned values | `tool sha256 <64-hex at lands>; base 44f76d45…` | yes: 64-hex is read from the landed bytes (QUALITY 28) |
| write scope | `read-only: git show of committed blobs; scratch only under explicit --work` | yes: confirm no other write path |
| owner | `kotodama-shokunin` | no |

### B. accept-o-79 (O counter) — pending `reports/round-79/accept-o.py` at lands

| cell | value now | depends on lands |
|---|---|---|
| name | `accept-o-79` | no |
| kind | `gate` | no |
| entry command | `python3 -B reports/round-79/accept-o.py --root . --lands <40-hex> --freeze <40-hex>` | yes: flag set as landed |
| verdict map | `Output ends ACCEPT-O-79: PASS legs=<n>/<n>` (exit 0) or `: FAIL legs=<n>/<n>` (exit 1); a refusal prints `ACCEPT-O-79: FAIL legs=0/<n> (refused: …)` and exits 2 | yes: leg count and refusal list |
| self-test | `python3 -B reports/round-79/accept-o.py --selftest` | yes |
| pinned values | `counter sha256 <64-hex>; freeze <40-hex>; base 44f76d45…; guard sha256 <64-hex>` | yes |
| write scope | `read-only against --lands (git show); selftest scratch via tempfile` | yes: confirm |
| owner | `kotodama-shokunin` | no |

### C. accept-ca-79 (Ca counter) — pending `reports/round-79/accept-ca.py` at lands

Same shape as B with `ACCEPT-CA-79`. Its pinned values name the S884 correction receipt digest and
the measured round-78 revision `4b255745dea45a45d88b17e3c3fea4cdb6700cf7` (as stated in the wave spec;
re-read from the round-78 registry blob before pinning, not copied from the spec).

## 5. Checks L1 runs after integration (commands, not run here)

```
python3 -B tools/check-registry-rows.py --skill <lands SKILL.md dumped to scratch> --root <lane> --rev <lands> --rows ledger-token-guard,accept-o-79,accept-ca-79,N1,N2
python3 -B tools/check-registry-rows.py --selftest <fixtures dir>
```

The checker is stage-only (`skill-row-check.py`). Its path and name are L1's choice; the command above
is the form the row would cite. The base-tree probe was run as stated in section 2 and is preserved in
`probe-base-rows.txt`.
