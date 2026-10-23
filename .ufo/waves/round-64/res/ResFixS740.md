# ResFixS740 — RF5 repair on ScribeRowS740

## Scope

Repair seat for CriticRowsFinal RF5, lane repo `kotodama-shokunin`. One file edited:
`.ufo/waves/round-64/rows/ScribeRowS740/row.txt`. No other lane, fleet, or sibling file was
written; no commit, no jj operation, no git index operation, no subagent dispatch, no pacman,
no installs or updates. Scratch only in
`/home/vgpnk/.cache/hyaku/kotodama-r64-res/ResFixS740/`.

## Axes (godspeed)

1. **Operability** — cell 7 (`teaches`) must satisfy the assignment's `teaches <= 25` words.
2. **Calibration** — the cell must assert only the benefit the selected overgeneralization
   quote supports, and must keep an inferential hedge rather than upgrading the paper's
   `suggest` to a demonstrated fact.
3. **Preservation** — citation identity, scope, locator, anchor quote, tier, status, dates,
   used-by, BULLET, VERIFY, CAPTURE, and ACCESS unchanged. RF5's explicit non-finding is
   honored: **tier stays A** (the paper's own corpora observations, not an abstract-only
   authority).

## Change

Only cell 7 of the `ROW:` line changed (11-cell row; cell index 6 zero-based).

- **Old (43 whitespace words / 45 counter-normalized words):**
  `Documents that children overgeneralize noun titles (san versus chan, kun) rather than copying input verbatim, and that parental use of san for parent names does not grow with the child's age, so a designed address system can be rule-governed and still be mislearned.`
- **New (14 whitespace words / 15 counter-normalized words):**
  `Worldbuilders can model Japanese noun-title overgeneralizations as suggesting rule learning rather than input memorization.`

The new text is the critic's RF5 smallest-safe-correction example verbatim.

Why this is the grounded single benefit. The preserved anchor quote (22 words, unchanged,
independently re-measured) is:

> "These overgeneralizations suggest that children are not just memorizing the forms in their
> input, but also generating novel forms from a rule."

Each element of the new cell traces to that sentence or to the row's own unchanged scope cell
(`acquisition of honorific (san) and diminutive (chan, kun) noun titles by Japanese children`):
`overgeneralizations` ← quote; `suggesting` ← quote's `suggest` (hedge retained, not promoted
to assertion); `rule learning` ← `generating novel forms from a rule`; `input memorization` ←
`not just memorizing the forms in their input`; `Japanese noun-title` ← scope cell. The old cell
additionally asserted a parental-age result that the selected quote does not contain — the
shortening removes both the length breach and that unanchored clause, which is why no
substitute clause was added back.

Counts were reproduced independently with the checker's own normalizer definition
(`NONWORD = r"[\W_]+"`, NFKC, casefold — `.ufo/waves/round-64/check-rows.py`), because the
checker itself never measures cell 7 length.

## Preserved invariants (verified by re-parse and byte diff)

| Invariant | Value after edit |
|---|---|
| Cells in `ROW:` | 11 (unchanged) |
| `\|` inside any cell | none (none before either) |
| id / tier | `S740` / `A` (unchanged; RF5 non-finding honored) |
| citation cell (cell 2) | unchanged, byte-identical |
| scope cell (cell 5) | unchanged |
| anchor quote (cell 6) | unchanged, 22 words |
| status / opened / recheck / used-by | `mined` / `2026-10-23` / `180d` / `corpus/knowledge/linguistics/language-socialization-and-acquisition.md` (unchanged) |
| `BULLET:` line | unchanged |
| `VERIFY:` / `CAPTURE:` / `ACCESS:` | unchanged; LOCATED live URL, capture timestamp `20210414114152` |
| Non-`ROW:` lines | byte-identical (5-line file, 5 newlines before and after, LF only, trailing newline present) |
| Changed cells vs pre-edit snapshot | exactly `[6]` |

## Custody and hash evidence

The critic's stored snapshot for this row is reproducible from my pre-edit copy: the snapshot
stores the file text without its trailing newline, and
`sha256(snapshot_text.rstrip("\n")) == 4a14dec0ab7806e930e292e7a0a7d915473aa5b117f1d7e0e86f1b51e4a507a0`,
which is exactly the SHA-256 CriticRowsFinal lists for S740 (the assignment's 43/45-word and
22-word quote measurements also reproduce). Content was therefore unchanged between the
critic's read and my edit; the LSP-less byte comparison also shows the snapshot text equals my
pre-edit text minus the trailing newline.

| Artifact | SHA-256 |
|---|---|
| pre-edit file, raw bytes (`row.before.txt`, 3352 B) | `62c2cd1d55cf9d37af7d60d6c3e0e4c3fc9e2aac0d0b14bed8ef5faa1ac3ecb3` |
| pre-edit file, critic convention (no trailing newline) | `4a14dec0ab7806e930e292e7a0a7d915473aa5b117f1d7e0e86f1b51e4a507a0` |
| post-edit file, raw bytes (3209 B) | `e50673c41c119b070a1b98f4dd332537d2e629a9d39fad9b6d860c08dc7f54aa` |
| post-edit file, critic convention | `f275d1ec7f250da92047b859cb241599b62ad5304490f4c019a7eebd0533c4b5` |

Evidence files: `row.before.txt`, `row.before.sha256`, `row.after.sha256`,
`check-after-run1.txt`, `check-after-run2.txt` under
`/home/vgpnk/.cache/hyaku/kotodama-r64-res/ResFixS740/`.

## Checker evidence

```
python3 -B .ufo/waves/round-64/check-rows.py --rows-dir .ufo/waves/round-64/rows
```

- Run 1 (immediately after edit): `S740 OK`; `CHECK-ROWS: 32/32 clean`
- Run 2 (stability re-run under concurrent sibling edits): `S740 OK`; `CHECK-ROWS: 32/32 clean`

No transient non-32/32 appeared, so no reconciliation window was needed.

## Findings

No actionable defect remains in this row. Severity-ordered result: none — info only.

- **[info] Checker blind spot (not this row's defect, not repairable by this seat).**
  `check-rows.py` validates cell count, tier, status, opened, recheck, used-by, quote bounds
  (8–25), live URL, capture match, bullet shape, and VERIFY prefix, but never measures cell 7
  length. Its `32/32 clean` output is therefore silent on the `teaches <= 25` rule; the only
  evidence for RF5's closure is the independent count above (14 whitespace / 15 normalized).
- **[info] Sibling-seat boundary.** RF4 (S723) is the same class of finding; its report
  (`res/ResFixS723.md`) already exists and was not modified or relied on here.

## Residual risk

- **Semantic grounding is human-reviewed, not tool-verified.** `lsp` is not mounted in this
  runtime (`xd://lsp` → `No such tool`; mounted devices are `ast_edit` and `debug`), and no LSP
  server applies to a plain-text data row in any case. No text-grep output is presented as
  semantic proof of grounding; the traceability argument above is manual and could be judged
  over-generous in the `rule learning` paraphrase, though the `as suggesting` hedge keeps the
  assertion weaker than the quote's own `than`-contrast.
- **Concurrency.** Other seats were editing other row directories during both checker runs;
  this seat only read the shared checker and wrote its own row plus this report, so the clean
  result cannot be attributed to this seat alone beyond its own `S740 OK` lines.
- **Role-level checks out of scope:** one-canonical-runtime identity, same-identity rerouting,
  saturation claims, `resume_continuity_v1` preflight rejection, and judge/admission behavior
  are not exercised by a data-row text repair; nothing here asserts anything about them.
