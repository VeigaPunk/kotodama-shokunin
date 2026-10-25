# CritO2 — round-69 w1 attack on the O2 settlement-fixture harness

Seat: round-69 wave-1 attack role (operability). Date: 2026-10-24.
Lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin (read-only on production
bytes; all mutations shown below were made to copies under /tmp/crito2-*).
No installs were needed (system python3 3.14.8 sufficed); no network fetches.

Question asked: do `tools/check-settlement-fixture.py`'s three cases really
exercise the shape the live registry has, and what structural difference
between the fixture registry and live `corpus/SOURCES.md` could make the
harness green while the live registry is not?

---

## 1. Shape fidelity: fixture vs live registry

Live headings (`grep -n '^#' corpus/SOURCES.md`):
`# SOURCES` (l.1) → `## Registry` (l.26) → `## Paths` (l.814) → `## Search
log` (l.849) → `## Leads (unopened)` (l.861). Fixture order: `#` → `## Registry`
→ `## Paths` → `## Search log`.

Facts measured on the live file (script, real output):

```
in-registry well-formed rows: 782        malformed rows: 0
live header : | id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
fixture header present in harness: True
used-by path entries: 709  missing on disk: 0
supersedes chains: 47   (checker: pending=0; 46 trivially settled + S575>S420 SETTLED-SPLIT)
statuses: mined=687 queued=58 rejected=37; unique ids 782/782
separator live==fixture: True | in harness: True
S-row-shaped lines outside ## Registry: 0
live multi-path used-by rows: S001×3, S002×11, S003×2, S008×2, S013×9  (5 cells)
used-by paths outside corpus/: 0; rows whose used-by names SKILL.md today: 0
```

Per feature the round names:

- 11-column rows: fixture header AND separator row are byte-identical to live.
- `## Registry` section: present in both; this is the only heading the checker
  actually toggles on (`parse_registry`), identical semantics.
- `## Paths` / `## Search log`: present in both. Note: the checker never reads
  either section — they are shape decoration. Fine for fidelity, but the
  harness's "lane-shaped" claim is only load-bearing for `## Registry`.
- Mined successor + queued target: fixture green case is S002 `mined` with
  used-by, S001 `queued` — exactly the live settled-active majority shape
  (largest live chain class).
- Used-by path under corpus/knowledge/: yes (`corpus/knowledge/a.md`); all 709
  live used-by entries are under corpus/, so the fixture matches convention.

VERDICT: PASS — the harness's three cases exercise every named live-shape
feature; header/separator/status vocabulary match the live registry byte-wise.

Caveat on wording: FIXTURE_REGISTRY's preamble says "the same section order as
the live corpus/SOURCES.md", but live carries a fourth section
`## Leads (unopened)` that the fixture lacks. Harmless to the checker (0
row-shaped lines live outside `## Registry`), but the claim is not literally
true. (L1 routing note; counters are frozen — do not amend them.)

## 2. Negative case vs the R68-M1 defect class

Ran the committed harness and the round-69 counter on the live tree:

```
$ python3 -B tools/check-settlement-fixture.py --root $PWD
PASS fixture-green rc=0 pending=0 missing_paths=0
PASS fixture-negative rc=0 pending=0 missing_paths=1
PASS fixture-pending rc=1 pending=1 missing_paths=0
FIXTURE: 3/3
LANE: pending=0 missing_paths=0        (harness exit 0)

$ python3 -B reports/round-69/accept-o.py --root .
LEG PASS STAMP / TOOL / FIXTURE / NEGCASE / LANE / NEGPROBE / R68FROZEN
ACCEPT-O-69: PASS legs=7/7   exit=0
```

Independent mutation (live `corpus/` copied to /tmp, one solo used-by target
`corpus/knowledge/civilizations/moche.md` deleted):

```
D1 baseline (live copy) : (0, 'SETTLEMENT: pending=0 chains=47 usedby_paths=709 missing_paths=0')
D1 removed .../moche.md : (0, '... missing_paths=1')      # checker exit stays 0 (gates pending alone)
D1 harness --root copy  : exit=1 ['LANE: pending=0 missing_paths=1']
```

So the negative case fires on a live-shaped tree, and the harness's `--root`
mode adds the missing-path gate the raw checker exit deliberately lacks. The
fixture-vs-counter division of labor (NEGPROBE rebuilt independently in
accept-o.py) holds.

VERDICT: PASS — the negative case genuinely catches the R68-M1
missing-used-by defect class, including on live-shaped data.

## 3. Green-while-red vectors (mutations on /tmp copies)

Each demo: registry/statuses as noted, checker run on the mutated copy.
Correct settled-active shape used: successor mined+used-by, target queued.

```
D2 pending pair (mined/mined, no limiter): rc=1 pending=1          (red, correct)
D2 same debt, S002 row dropped to 10 cells: rc=0 pending=0 chains=0 (GREEN — debt invisible)

D3 settled-active, a.md cites S002        : rc=0 missing_paths=0   (green, correct)
D3 same, a.md cites NOTHING               : rc=0 missing_paths=0   (GREEN — citation truth unchecked)
D3 used-by path is a DIRECTORY            : rc=0 missing_paths=0   (GREEN — os.path.exists accepts dirs)

D4 settled shape, target id S999 dangling : rc=1 pending=1         (red — checker catches; fixture lacks this case)

D5 multi-path cell, only a.md exists      : rc=0 missing_paths=1   (split works, per-path counting works)
D5 multi-path cell, both exist            : rc=0 missing_paths=0
```

Findings, ranked:

1. GAP-CONFIRMED — malformed-row swallow (D2). Any registry row that does not
   split into exactly 11 cells is marked `malformed` and silently skipped from
   BOTH chain classification and used-by existence checks
   (check-supersession-settlement.py:85-87, 118, 141); the SETTLEMENT summary
   carries no malformed counter, so real pending debt becomes invisible
   (`chains=0`). The fixture is well-formed by construction and has no case
   asserting that a wrong-column row is flagged — a live mass column-corruption
   would leave the harness green while the live registry is red. Live today:
   0 malformed rows, so nothing is hidden NOW. The frozen round-69 counters
   cannot be amended; route a malformed-row case into a later round.
2. GAP-CONFIRMED — citation truth is promised but unimplemented (D3). The
   checker docstring defines STALE-USED-BY ("used-by names a path that does not
   contain the row's own id") but neither `scan` nor `validate_ledger` ever
   opens the file; only `os.path.exists` is tested. The fixture's
   USEDBY_FILE content ("cites S002 now") is decorative — the harness would
   stay green with a used-by file citing nothing. Directly relevant to D2
   data: S859's used-by will name SKILL.md (first such row — 0 today); nothing
   in the O2 gate verifies SKILL.md literally contains "S859".
3. GAP-CONFIRMED — multi-path used-by cells never exercised (D5). The live
   registry has 5 comma-separated multi-path cells (S002 has 11 paths); the
   checker's `re.split(r"[,;]", ...)` branch and its per-path missing counting
   work today, but the fixture only ever uses single-path cells, so a
   regression in the split would leave the harness green while live parsing
   breaks. My first demo run actually crashed on this exact shape before I
   split cells the way the checker does.
4. GAP-CONFIRMED — directory-instead-of-file false negative (D3). A used-by
   path that exists as a directory satisfies `os.path.exists`; docstring says
   "a real corpus path". Edge case, cheap to close in a later fixture case.
5. Coverage gaps that are NOT green-while-red vectors: dangling supersedes
   target (D4 — checker goes red, fixture never exercises it); settled-split /
   retired / closed states never green-tested by the harness (its three cases
   are green/negative/pending only); `--ledger` mode and `--registry` override
   unexercised. The harness's `missing_paths` counts (row, path) pairs, not
   unique files — with k rows citing one deleted live file it reports k; the
   fixture only ever sees k=1.

VERDICT: FAIL — as an attack finding, three confirmed green-while-red vectors
exist (malformed-row swallow, unchecked citation truth, unexercised multi-path
cells), though none is live-red today: the live tree is genuinely green
(pending=0, missing_paths=0, 0 malformed rows) and accept-o.py is 7/7 PASS
pre-data. The harness is a true positive for what it names (the R68-M1
missing-file class) and does not claim more than it tests — the residual risk
is in what the round's claims leave untested.

## 4. Tree cleanliness

`git status --porcelain` after all runs: only untracked `.ufo/waves/round-69/**`
wave files; no modification to any tracked production byte. Harness and
counter runs wrote only to tempdirs. One residual caveat: neither the harness
nor accept-o.py pins a sha256 for `tools/check-supersession-settlement.py`
(STAMP/R68FROZEN pin counters only), so a post-control edit to the checker
would float the O2 gate; the negative/pending behavior probes would catch most
such edits, but not ones confined to ledger/split/stale-citation logic.

VERDICT: NOT-EVALUATED — citation truth of the 709 live used-by entries
(file-exists-but-doesn't-cite) was not measured; it is unmeasurable through
the checker itself (see finding 2) and outside this seat's write bounds.

## 5. Suggested L1 routing (no production edits made by this seat)

- Round-69 counters stay frozen; none of the above blocks O2 as declared.
- corrections/future rounds: (a) malformed-row counter in the settlement
  summary + a harness case; (b) implement or retract the STALE-USED-BY
  docstring promise; (c) one multi-path-cell fixture case; (d) soften the
  FIXTURE_REGISTRY "same section order" preamble or add the Leads section;
  (e) for D2 data, write S859's used-by so SKILL.md literally contains "S859".
