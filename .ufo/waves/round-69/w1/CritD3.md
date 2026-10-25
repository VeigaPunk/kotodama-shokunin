# CritD3 — round-69 w1 — attack on claim D2's evidence rule

Seat: leaf, read-only on production bytes. Measured revisions:
- base (declared): `793f79746712a79f915bb481215e54bbea8b5e7a`
- HEAD (declaration commit that carries the r69 instruments): `6a98d7d042b6c58d2165773b1585069798111035`
- r68 receipt revision `44c9cc2863fed952bb3a2b04149c2ac279338c3b` (stamped inside `reports/round-68/telemetry/final-measures-o.txt`) — proven ancestor of base (`git merge-base --is-ancestor` → YES), so the receipt's claims stay re-derivable.

Claim D2's evidence rule (accept-d.py leg `EVIDENCE`, lines 167–175): for each of the
five table rows, path tokens matching `[A-Za-z0-9_./-]+\.(?:py|md|tsv|txt|json|ya?ml)`
are extracted from the Evidence cell and **at least one** must satisfy
`os.path.exists(root/token)`. Leg `SOURCE` (lines 177–189) additionally requires at
least one `S\d{3,}` id named anywhere in the table text to be a `corpus/SOURCES.md`
row with 11 cells, `status=mined`, and `SKILL.md` in the used-by cell.

## VERDICTS

- VERDICT: PASS — the D2 evidence rule is satisfiable at the measured revision
  today: every one of the five state rows can cite `tools/check-supersession-settlement.py`
  (exists at base AND HEAD, re-run green in this seat), so no row is forced to wait on unlanded data.
- VERDICT: FAIL — the GREEN fixture inside the frozen counter (`reports/round-69/accept-d.py:48`)
  points settled-retired at `tools/check-supersession-settlement.py:129`, but :129–131 is the
  **settled-split** branch; the honest retired branch is :125–126. The counter cannot see this
  (EVIDENCE checks path existence only, and the counter is frozen post-data). The landed SKILL.md
  table must NOT copy the fixture's line numbers.
- VERDICT: WEAK — the EVIDENCE leg polices existence only: a cell citing
  `tools/check-supersession-settlement.py:99999` passes. Line-number honesty is entirely on the writer.
- VERDICT: NOT-HONEST — citing `reports/round-68/dispositions/dedup-ledger.tsv` as the Evidence
  for the **pending** row: the ledger by construction contains only ruled/pre-settled rows
  (r68 settled all 34 pending chains; `--scan` shows pending=0). The honest pending citation is the
  classifier's else-branch (:132) plus the selftest's `PASS pending-detected` fixture (FIX1).
- VERDICT: DEAD-POINTER — `corpus/lessons/round-69.md` and `reports/round-69/corrections-r68.md`
  do not exist today (`test -f` MISSING for both); `corpus/SOURCES.md` carries no S859 row and
  zero rows whose used-by names SKILL.md (`grep -c` = 0 and 0). Any of these cited as a row's sole
  Evidence token before the r69 data lands is a dead pointer; `S859` alone (no path) fails
  PATH_RE outright and would fail EVIDENCE for that row.
- VERDICT: PASS — the r68 evidence chain is re-runnable end-to-end at the working tree:
  selftest 7/7, `--scan` pending=0 chains=47 usedby_paths=709 missing_paths=0 (byte-identical
  summary to the r68 receipt's PENDING line), `--ledger` rows=82 findings=0.

## 1. Path inventory the round-68 settlement work committed

`test -f` in the working copy, `git cat-file -e <base>:<path>` at the base revision:

```
$ for p in tools/check-supersession-settlement.py \
    reports/round-68/dispositions/dedup-ledger.tsv \
    reports/round-68/telemetry/final-measures-o.txt corpus/lessons/round-68.md \
    tools/check-settlement-fixture.py reports/round-69/accept-d.py; do
    test -f "$p" && echo "EXISTS $p" || echo "MISSING $p"; done
EXISTS tools/check-supersession-settlement.py
EXISTS reports/round-68/dispositions/dedup-ledger.tsv
EXISTS reports/round-68/telemetry/final-measures-o.txt
EXISTS corpus/lessons/round-68.md
EXISTS tools/check-settlement-fixture.py
EXISTS reports/round-69/accept-d.py

$ git cat-file -e 793f7974…:tools/check-supersession-settlement.py   # etc.
AT-BASE     tools/check-supersession-settlement.py
AT-BASE     reports/round-68/dispositions/dedup-ledger.tsv
AT-BASE     reports/round-68/telemetry/final-measures-o.txt
AT-BASE     corpus/lessons/round-68.md
NOT-AT-BASE tools/check-settlement-fixture.py        (added by the r69 declaration commit)
NOT-AT-BASE reports/round-69/accept-d.py             (same)
```

"The r68 ledger" = `reports/round-68/dispositions/dedup-ledger.tsv`; it is the only
ledger-shaped artifact under `reports/round-68/` (verified by `ls`). Its evidence
column also names per-seat audits `.ufo/waves/round-68/rows/{RevAuditA..G,AuditChain8}/audit.md`
— all present in the base tree (`git ls-tree`), but they are wave-scratch; durable SKILL.md
pointers should prefer `tools/`, `reports/`, `corpus/`.

Re-runnability class:
- `tools/check-supersession-settlement.py` — **re-runnable** (reads only; selftest builds temp fixtures).
- `reports/round-68/dispositions/dedup-ledger.tsv` — **re-runnable as tool input** (`--ledger`).
- `reports/round-68/telemetry/final-measures-o.txt` — NOT re-runnable (receipt transcript;
  stamped revision 44c9cc28, ancestor of base). Honest only as historical evidence
  (it records `PENDING PASS … pending=0 chains=47` and the R68-M1 `EXEC FAIL lands_pass=False`).
- `corpus/lessons/round-68.md` — NOT re-runnable (narrative; documents R68-M1 and the
  settle-apply slice bug R68-M3). Secondary citation only.
- `tools/check-settlement-fixture.py` — exists only from the declaration commit forward;
  never cite it in any "before base" statement.

## 2. Live re-runs (real output, this seat)

```
$ python3 -B tools/check-supersession-settlement.py --selftest
PASS pending-detected
PASS settled-active
PASS settled-retired-closed
PASS settled-split
PASS ledger-clean
PASS ledger-inconsistent-rejected
PASS unreadable-exit-2
SELFTEST: 7/7            (rc=0)

$ python3 -B tools/check-supersession-settlement.py --scan --root .
… 47 chain lines: 31 SETTLED-ACTIVE, 5 SETTLED-RETIRED, 10 SETTLED-CLOSED, 1 SETTLED-SPLIT …
SETTLEMENT: pending=0 chains=47 usedby_paths=709 missing_paths=0    (rc=0)

$ python3 -B tools/check-supersession-settlement.py --ledger \
    reports/round-68/dispositions/dedup-ledger.tsv --root .
LEDGER: rows=82 findings=0    (rc=0)

$ python3 -B reports/round-69/accept-d.py --root .          # do-nothing probe
LEG PASS STAMP …
LEG FAIL SECTION heading=### Registry correction chains
… ACCEPT-D-69: FAIL legs=1/8 (rc=1)                          # pre-data state, as declared

$ python3 -B reports/round-69/accept-d.py --selftest
GREEN FIXTURE: PASS (legs 8/8) / DO-NOTHING FIXTURE: FAIL (as required) (legs 1/8) / SELFTEST: 2/2
```
My selftest output matches the committed pre-data receipt
`reports/round-69/telemetry/controls.txt` line-for-line.

## 3. State → honest-evidence matrix

Classifier branches verified by reading `classify()` (tools/check-supersession-settlement.py:112–145):

| State | Honest tool line | Re-run demo | Ledger exemplar (dedup-ledger.tsv) | Fixture cites | Fixture honest? |
|---|---|---|---|---|---|
| pending | :132 (else) | `--selftest` → `PASS pending-detected` (FIX1) | **none exists** — no pending rows by construction | :112 (`def classify`) | imprecise, not false |
| settled-active | :127 | FIX2; `--scan` 31 chains | S126>S105 activate/repoint (audit RevAuditB) | :127 | yes |
| settled-retired | :125 | FIX3; S132/S070/S125/S186 scan lines | S132>S094 keep-reject "settled-retired at base"; retire rulings S070>S060, S125>S095, S186>S157 | **:129** | **no — :129–131 is the split branch** |
| settled-closed | :123 | FIX3 | S574>S159, S651>S643 keep-successor "settled-closed at base" | :123 | yes |
| settled-split | :129 | FIX4 → `PASS settled-split`; scan `SETTLED-SPLIT S575>S420` (only split chain) | S575>S420 keep-split (for-entry-only limiter) | :130 | inside branch; branch head is :129 |

`final-measures-o.txt` and `corpus/lessons/round-68.md` are honest secondary citations for any
row's background (the receipt proves the registry-wide settled state at r68; the lesson records
R68-M1) but should never be a row's only pointer — they are not re-runnable.

## 4. Dead pointers and staged paths flagged

1. `corpus/lessons/round-69.md` — MISSING today; claims.json's `sourced` field depends on it
   ("S859 … run and quoted in corpus/lessons/round-69.md `## Gate`"). Dead until data lands.
2. `reports/round-69/corrections-r68.md` — MISSING today (Ca2's data). Dead until landed.
3. S859 row — `grep -c S859 corpus/SOURCES.md` → 0; rows with used-by naming SKILL.md → 0.
   The SOURCE leg has **zero** qualifying rows in the tree today, so the leg lives or dies with
   the S859 landing; until then any table fails SOURCE regardless of EVIDENCE.
4. `S859` as an Evidence cell without a repo path — PATH_RE finds no token → that row fails EVIDENCE.
   Always pair the S-id with a real path (the fixture's `S859 — tools/….py:NNN` shape is correct on this axis).
5. Fixture's settled-retired `:129` — mis-aimed branch pointer, invisible to the frozen counter.
   The landed table should cite :125.
6. `.ufo/waves/round-68/rows/*/audit.md` — committed and alive, but wave-scratch; brittle as
   durable SKILL.md evidence. Prefer `reports/round-68/…` paths.

## 5. Counter laxities observed (depth notes, no exploit attempted)

- EVIDENCE: existence-only; wrong line numbers and irrelevant paths pass. Writer discipline required.
- SIGNATURES: `section_span` breaks only on `## ` — a table H3 placed inside `## Error patterns`
  would make the signatures "present" by placement alone. claims.json pins the table under
  `## Decision table`, which avoids the shortcut; keep it there.
- STAMP is trivially self-consistent when the counter is run from its own committed copy.
- TABLE/STATES/FIELDS are strict (exactly 5 header cells, the five state names in order
  `pending, settled-active, settled-retired, settled-closed, settled-split`, no empty cells) — solid.

## 6. Recommendation for the landed table (all cited paths exist at base AND HEAD)

Per-row Evidence of the shape `S859 — tools/check-supersession-settlement.py:<branch-line>` with
branch lines 132 / 127 / 125 / 123 / 129, optionally adding the ledger as a second token
(`reports/round-68/dispositions/dedup-ledger.tsv`) on the four settled rows — never on pending.
Do not copy the GREEN fixture's line numbers (its retired pointer is wrong); the fixture
demonstrates shape, not citation truth.
