# ResFixS723 — RF4 repair on ScribeRowS723

## Scope

Repair seat for CriticRowsFinal RF4, lane repo `kotodama-shokunin`. One file edited:
`.ufo/waves/round-64/rows/ScribeRowS723/row.txt`. No other lane, fleet, or sibling file,
no commit, no jj operation, no git index operation, no pacman, no installs.

## Axes (godspeed)

1. **Operability** — cell 7 must satisfy the assignment's `teaches <= 25` words.
2. **Calibration** — the teaches cell must state only the claim the selected overextension
   quote actually supports; underextension and the developmental-trajectory claim are not in
   that quote and were removed from the cell.
3. **Preservation** — source, locator, citation identity, tier, status, dates, used-by,
   anchor quote, and BULLET unchanged.

## Change

Only cell 7 (`teaches`) of the `ROW:` line changed.

- **Old (44 whitespace words / 44 NFKC-nonword-normalized words):**
  `Children of this age apply one simple word to many different referents (overextension) or hold one word to a single referent (underextension); both errors recede as vocabulary grows, so worldbuilders can treat early word breadth as a design variable rather than a fixed stage`
- **New (15 whitespace words / 15 normalized words):**
  `Worldbuilders can depict overextension as a child using one simple word for many different things.`

The new wording is the critic's RF4 smallest-safe-correction example verbatim. It is grounded
in the preserved quote — `In overextension, children use a simple word to refer to many
different things.` — and drops both the underextension clause and the unsupported "errors
recede / design variable" inference from the teaches cell.

Counts independently reproduced with the checker's own normalizer definition
(`NONWORD = r"[\W_]+"`, NFKC, casefold — `.ufo/waves/round-64/check-rows.py`), not the checker
alone, because the checker does not measure teaches length.

## Preserved invariants (verified by re-parse)

| Invariant | Value after edit |
|---|---|
| Cells in `ROW:` | 11 (unchanged) |
| `\|` inside any cell | none |
| id / tier | `S723` / `B` |
| scope (cell 5) | `overextension and underextension as early word-meaning errors in children aged 0-5` (unchanged) |
| anchor quote (cell 6) | `In overextension, children use a simple word to refer to many different things.` (13 words, unchanged) |
| status / opened / recheck / used-by | `mined` / `2026-10-23` / `180d` / `corpus/knowledge/linguistics/language-socialization-and-acquisition.md` (unchanged) |
| `BULLET:` line | unchanged, including underextension clause |
| `VERIFY:` / `CAPTURE:` / `ACCESS:` | unchanged; LOCATED live URL, capture timestamp `20260324122540` |
| File line count / endings / trailing newline | 5 content lines + trailing newline, LF (unchanged) |
| Post-edit SHA-256 (whole file) | `2a76a8b04a7dde68a1c80a5b08e04cbda26df6faa7832bc5c73398a90517bcf9` |

Critic snapshot SHA-256 for the pre-edit row was `e2e4696cdcc5be9af460e16278a0d533a19cd8d4d2b4e43528b01e01a028414f`;
the file hash necessarily changed, the identity metadata did not.

## Checker evidence

Command (run twice, both after the edit, per assignment's transient-failure rule):

```
python3 -B .ufo/waves/round-64/check-rows.py --rows-dir .ufo/waves/round-64/rows
```

- Run 1: `S723 OK`; `CHECK-ROWS: 32/32 clean`
- Run 2: `S723 OK`; `CHECK-ROWS: 32/32 clean` (tail verified through `S749 OK`)

## Findings and residual risk

- **No actionable defect remains in this row.** The teaches cell is 15 words, within the
  <=25 bound, and asserts only the overextension claim the quote carries.
- **Residual risk (checker blind spot, not this row's defect):** `check-rows.py` validates tier,
  status, dates, quote bounds (8–25), URLs, capture match, and bullet shape, but never measures
  cell 7 length. `32/32 clean` is therefore not evidence that any row satisfies the
  `teaches <= 25` rule — that bound is only covered by the independent measurement recorded
  above. RF5 (S740) is the same class and belongs to its own seat.
- **Verification limitation:** no LSP server applies to a plain-text data row, so caller /
  definition / diagnostics checks were done by structural re-parse of the row plus the
  checker, not semantic indexing. No grep output is presented as semantic proof.
- The `res/` directory did not exist at the start of this seat; it was created (empty) to hold
  this report. No sibling report was modified.
