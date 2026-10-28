# MutCaRepair — W2 falsification: Ca REPAIR leg, L76-16 / SKILL.md:707

**Verdict: CONFIRMED DEFECT (coverage finding, repair-side).** The recorded
`LEG FAIL REPAIR — L76-16 statement_after no-match in SKILL.md` is genuine and
is caused exactly by phrasing, not by the digest value, the row anchor, or the
line placement. The landed repair at `SKILL.md:707` interposes the counter path
between "counter" and "sha256" and closes the digest cell with an ellipsis, so
the frozen grammar's literal run `committed counter sha256 `<12-hex>`` occurs
nowhere in the landed file. A single-token mutant that restores the frozen
phrasing flips the detector red→green; restored bytes are byte-identical to the
landing. No file was edited; no tool was installed.

## Frozen contract (graded bytes)

The Ca counter reads the pairs from the **ledger**, not claims.json
(`reports/round-76/accept-ca.py` @ `a43ed807`: `CLAIMS_REL` line 246,
`LEDGER_REL = "reports/round-76/ledger.json"` line 247;
`reports/round-76/claims.json` @ `df0f030` has keys round/status/frozen/base/
axes_note/pre_data_corrections/claims/frontier_step/attempt and contains **no**
pair entries). Graded pair (byte-identical at freeze `df0f030` and lands
`a43ed807`; `git diff df0f030 a43ed807 -- reports/round-76/{claims,ledger}.json`
empty):

- `reports/round-76/ledger.json` @ `df0f030`, entry `L76-16`:
  `statement_after.parse = "^\| accept-c-75 \|.*?committed counter sha256 \`([0-9a-f]{12})\`"`,
  `expected_after = "315c5f3f27fd"`, `stated_parse` token `fa5060b91bdb`.
- Detector semantics (`accept-ca.py` @ `a43ed807`, `statement_after()` lines
  1385–1407): compile with `re.M`, `finditer` over the whole statement file, no
  matches → `(None, False, "statement_after no-match in <path>")`; last match,
  capture group 1. `leg_repair()` line 1719 emits exactly
  `L76-16(statement_after no-match in SKILL.md)` — the recorded red.

## Landed line vs frozen grammar — the exact mismatch

`SKILL.md` @ `a43ed807` line 707 (unique `| accept-c-75 |` row; 1811 bytes),
decisive window:

> `… Measured 2026-10-27: committed counter `reports/round-75/accept-c.py` sha256 `315c5f3f27fd…`; the receipt header's `fa5060b91bdb…` …`

Two independent literal violations of the frozen parse; **either alone is fatal,
both are present**:

1. **Adjacency:** `committed counter ` is followed by the backticked path
   `` `reports/round-75/accept-c.py` `` — the grammar requires the contiguous
   literal `committed counter sha256 ` `. `.*?` cannot skip the path because the
   path itself is not between "counter" and "sha256" in the grammar's alphabet —
   the literal substring `committed counter sha256` does not occur anywhere in
   the landed file ("counter sha256" occurs only on lines 706/708, the
   `accept-ca-74`/`accept-ca-75` rows, which fail the `^\| accept-c-75 \|` anchor).
2. **Closure:** the digest cell is `` `315c5f3f27fd…` `` — 12 hex followed by
   U+2026, not a backtick — so `([0-9a-f]{12})\`` cannot match even where 12 hex
   digits exist.

For contrast, base `SKILL.md:707` @ `98c486b` (1619 bytes) reads
`…Measured 2026-10-27 at counter sha256 `fa5060b91bdb…`: `SELFTEST: 85/85`…`:
the w1 scout grammar `^\| accept-c-75 \|.*?counter sha256 \`([0-9a-f]{12})`
(`.ufo/waves/round-76/w1/stage/ScoutLedgerB/pairs.json` @ `df0f030`) matches it
with capture `fa5060b91bdb` (the original red), but the graded grammar matches
**neither** the base nor the landed bytes — it prescribes the exact repaired
surface form, and the landed phrasing is a grammatical paraphrase of it.

## Three-way mutation probe (bounded detector, exact `statement_after` semantics)

Scratch: `/fast/scratch/hyaku/kotodama-r76/MutCaRepair` (removed before yield).

| Run | bytes | sha256 | detector result |
|---|---|---|---|
| PRISTINE | `git show a43ed807:SKILL.md` (115881 B) | `c63d286db7d4b44775e4f4c9a25315791c768315f92c8fefff8b86467b9b3e4c` | **no-match** (red) — reproduces the recorded receipt |
| MUTANT M1 | same bytes, one replacement: ``committed counter `reports/round-75/accept-c.py` sha256 `315c5f3f27fd…` `` → ``committed counter sha256 `315c5f3f27fd` `` (115847 B) | `58e790e23c645fe5eba7b3418e6f20891b64a2c4d9da97945e285bebaf6eb556` | **match**, token `315c5f3f27fd` |
| RESTORED | pristine bytes rewritten | `c63d286d…` == pristine | **no-match** again (red) |

M1 also satisfies every remaining `leg_repair` branch: token == `expected_after`
(315c5f3f27fd == sha256 of `reports/round-75/accept-c.py` @ `a43ed807`,
`315c5f3f27fd36b7ee92cb5bff9c34c27a5013e28218d9481ee7f74b5c7ce261`, computed
from committed bytes); token ≠ stated token (`fa5060b91bdb`); base `stated_text`
no longer on the statement line → **green**. So the mutant is killed by the
frozen phrasing alone; no other surface (digest, anchor, line number) is at
fault.

Cross-checks: landing bytes under the scout grammar → no-match (same adjacency
break, independent of the "committed"/closing-backtick differences); base bytes
under the scout grammar → match `fa5060b91bdb` (red_at_base confirmed).

## Recorded receipts (quoted, not re-run)

- `reports/round-76/telemetry/measures-ca.txt:2` — argv: `--lands a43ed807…`
  `--freeze df0f030…`, counter sha256
  `c1fc755e926f8d25e622469ec018bc9ad6c22b2f99ba83447fa95baab4a9695b`;
  `:6` — `LEG FAIL REPAIR — L76-16 `statement_after` no-match in SKILL.md.`
  (committed at `af67443` "round-76: record measured claim outcomes", not at
  the Ca landing).
- `reports/round-76/telemetry/controls-ca.txt:44-45` (do-nothing control,
  lands=freeze=`df0f030`): `green=[] red=['L76-16(statement_after no-match in
  SKILL.md)']` — expected, since the graded grammar matches no historical state
  of the row either.
- Same red list in `.ufo/waves/round-76/w1/stage/L1/freeze-ca-control-ledger-redbefore.txt:44-45`.

## Scope statement

- No claims, counters, lane files, or reports edited; no builds/tests/linters
  run (the probe re-implements the counter's regex semantics in-process; no
  repo test executed).
- No tool installed or upgraded (`~/.omp/agent/RULES.md` gate not triggered);
  pacman untouched.
- Scratch removed; pristine/mutant hashes recorded above as restoration
  evidence (restored ≡ pristine by sha256).
- This is a coverage finding for the repair, not a contract change: the frozen
  grammar is the contract; the landed sentence is what fails it.
