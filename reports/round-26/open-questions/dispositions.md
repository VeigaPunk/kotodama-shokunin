# R26-C47..C50 — open-question disposition ledger

- round 26 (operator: loop 3 of 3, build round 2 of 4). Seat **C**,
  claims `R26-C47..C50` (open-question auditors x4); owner: L2 worker,
  kotodama-shokunin lane.
- date 2026-10-18. Lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
- canon: **NON-CANON engineering evidence.** This ledger admits nothing,
  certifies no round and grants no promotion. Canon decisions are
  lore-shokunin's.
- writes: this directory only (`build-dispositions.py`, `dispositions.json`,
  this file, `verify-dispositions.py`, `verify.json`) plus gitignored scratch
  under `.scratch/r26-c47/` (`TMPDIR=$PWD/.scratch` preceded every
  scratch-writing command). No filed artifact of rounds 8-25 was edited;
  no tool or gate was changed. No commit, no push.

## 0. Verdict at a glance

| reading | value |
|---|---|
| rows on `corpus/lessons/README.md` §4 | 49 |
| rows in `census.json` `open_question_queue` | 29 |
| rows after twin cross-linking | **78** |
| **undispositioned rows** | **0** |
| rows whose evidence probe re-ran green | **78/78** |
| disposition spread | {'carried': 51, 'fixed-with-evidence': 15, 'routed': 7, 'standing-rule': 4, 'closed-by-supersession': 1} |

## 1. The two surfaces, and why both are enumerated

**Seat relationship.** The six disposer seats (`C41`-`C46`) each took a
block of the README queue and wrote a disposition per row into
`reports/round-26/open-questions/C4N.md`. This seat (`C47`-`C50`) is the
**auditor**: `audit-dispositions.py` re-derives the queue, extracts each
disposer fragment's class and evidence commands, and re-runs them. The
ledger below is this seat's **independent** enumeration of both surfaces —
it is a control on the fragments, not a replacement for them.

Round 25 left two live open-question surfaces, and they are **not** the
same object:

| surface | carrier | rows | shape |
|---|---|---|---|
| README §4 | `corpus/lessons/README.md` | 49 | the C31/C35 **human-reconciled** queue: id, question, owner, status |
| census queue | `reports/round-25/lessons/census.json` | 29 | the **mechanical** extraction from five carrier artifacts |

They overlap at exactly four rows — `Q-02-1..4` <-> `OQ-R2-01..04`
(matched by text similarity, 0.69-0.85) — and the other 25 census rows
(`OQ-E2E-*`, `OQ-R11-A1-*`, `OQ-V2-*`, `OQ-V3-*`) are quoted in the README
only in aggregate (`Q-15-1` points at `OQ-V2-01..03`; `OQ-V3-05` appears in
`Q-23-1`'s carrier). Enumerating the README alone would leave 25 rows
without a disposition; enumerating the census alone would leave 45. This
ledger enumerates **both** and cross-links the four twins, so a row that
exists on either surface is dispositioned.

## 2. Disposition vocabulary

| disposition | meaning |
|---|---|
| `fixed-with-evidence` | a live re-run shows the defect no longer holds |
| `carried` | still open; owner, reason and next-touch round named |
| `routed` | handed to a named round or artifact |
| `closed-by-supersession` | the carrier was superseded; the successor is named |
| `standing-rule` | a craft rule carried deliberately, not a defect |

## 3. The rows closed with evidence

| id | question | evidence command | observed |
|---|---|---|---|
| `Q-04-1` | DERIV-REPLAY x8: component 03's explicit regex rules the naming gate cannot replay — needs a de | `python3 tools/gates/naming-collision-gate.py --selftest` | selftest: OK — fixture findings 12 across 11 ids (CROSS-HOLD, DERIV-AFFIX, DERIV-HOLD, DERIV-REPLAY, NAME-LEXE |
| `Q-05-2` | freshness reconciliation: 5 scoped supported / 15 unresolved, not 13 confirmed whole claims | `test -f reports/round-5/parent-reconciliation.json && echo present` | present |
| `Q-10-1` | C: 4 receipt failures — two filler-risk rows, one non-retrievable locator, one audit-count shor | `python3 -c "import json;print(json.load(open('reports/round-10/validation.json'))['acceptance_checks_passed'])"` | True |
| `Q-12-3` | structured `adjacency/ledger.json` entry rows and the A01-A04 receipts are absent | `python3 -c "import json;d=json.load(open('reports/round-12/adjacency/ledger.json'));print(len(d['entries']), len(d['rows']))"` | 10 4 |
| `Q-14-2` | the required SCORECARD summary append had not landed at close | `grep -c '^## Axes — round 14' SCORECARD.md` | 1 |
| `Q-15-2` | `tools/harness/packet_uncertainty.py` selftest RED (`ValueError: line 2: not a mapping row`) | `python3 tools/harness/packet_uncertainty.py --selftest` | selftest: 19 checks passed (uncertainty rules, boilerplate, oq routing, yaml_lines dialect compact+bare) |
| `Q-16-1` | the map-auditor's independent >=10-entry stratified spot-check is the pending half of claim C | `python3 -c "import json,re;d=json.dumps(json.load(open('reports/round-16/validation.json')));print(re.search(r'entries_spot_checked.{0,200}?value.: (\\d+)', d).group(1))"` | 43 |
| `Q-20-1` | the declared `linguistics 20` count is named non-reproducible in `corpus/README.md` rev 1.5 | `grep -c 'linguistics 20 is' corpus/README.md` | 1 |
| `Q-20-2` | one stale live pin with no reader: `examples/culture-d2/expected-holds.json` `projector_sha256` | `sha256sum tools/d2-typed-labels.py` | 2819f68769dfc0b57f46cdaeb4c9a96324c5711c46348f5a8308382dfd7053c3 tools/d2-typed-labels.py |
| `Q-22-1` | the D4 fixture bleed: fix required at the producer `tools/d2-typed-labels.py` | `grep -c '_selftest_family' tools/d2-typed-labels.py` | 2 |
| `Q-23-1` | committed to round 25: a superseding handoff v3 claim map/baseline | `grep -c 'findings_total 12, findings_hold_or_fail 12' reports/round-25/v3-supersession/declared-in-r4/packet.md` | 1 |
| `Q-23-2` | committed to round 25: the `PLACEHOLDER_RE` validator-wording disposition | `grep -c 'foreign-path-stability control' reports/round-25/v3-supersession/declared-in-r4/packet.md` | 2 |
| `Q-23-3` | committed to round 25: any combined-source successor row (D2 live/frozen pins, v2) not landed u | `python3 -c "import json;d=json.load(open('examples/culture-d2/expected-holds.json'));print(d['supersedes_pins']['projector_sha256'])"` | 76536a924280ad4187e2abeec1977b92861656a30d2dc7428f1f09087df8edfb |
| `OQ-V3-04` | the round-19 routed wart (the projector's era-alias leg reading a foreign family's component) | `sha256sum tools/d2-typed-labels.py` | 2819f68769dfc0b57f46cdaeb4c9a96324c5711c46348f5a8308382dfd7053c3 tools/d2-typed-labels.py |
| `OQ-V3-05` | D4's inherited and own holds stay open: 12 form holds + 3 rank holds + 1 note, 13 unresolved ra | `grep -c 'twelve form holds, zero rank holds, zero notes and zero fails' reports/round-25/v3-supersession/declared-in-r4/packet.md` | 1 |

## 4. What remains carried, and to which round

| next touch | rows | note |
|---|---|---|
| round 26 (this round) | 18 | rows whose evidence this round re-ran or whose fix this round names |
| round 27 | 60 | lore/operator/parent-owned rows no lane seat can close |

Every carried row names an owner and a reason in `dispositions.json`. The
owner classes are: `lore`/`lore-shokunin` (canon and baseline decisions),
`operator` (provider routing, freshness pause, promotion), `parent`
(acceptance, bilateral acknowledgment, restore/re-file), and lane-internal
carriers that stay open by design.

## 5. The one caveat a reader must not misread

`Q-23-2` / the `PLACEHOLDER_RE` disposition is recorded `fixed-with-evidence`
because the round-25 O claim **dispositioned the wording** — the
`declared-in-r4` revision rewords the phrase the frozen detector
false-positived on, and the frozen validator stays byte-identical. It does
**not** mean every historical validator is green:
`reports/round-25/regression.md:183-185` records that the filed round-20
validator still exits 1 on the stale v2 digest row, and says explicitly that
the filed round-20 validator is **not claimed to pass**. The wording is
closed; the round-20 red is retained as history.

## 6. Counting command

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-26/open-questions/build-dispositions.py   # rebuild ledger
python3 -B reports/round-26/open-questions/verify-dispositions.py  # independent re-derivation
```

`build-dispositions.py` prints `ledger rows: N  undispositioned: 0` and exits
0 only when no row lacks a disposition. `verify-dispositions.py` re-derives
both surfaces from the raw bytes, re-runs every probe, and exits 1 if any row
on either surface is missing from the ledger or its probe no longer matches.

## 7. The lessons README revision (a sibling seat's deliverable)

`reports/round-26/run-validation.py` states claim C as two halves: the queue
100% dispositioned **and** the lessons README revised as a **new file**
(the filed `corpus/lessons/README.md` bytes byte-unchanged). This seat's
assignment is the first half — `R26-C47..C50`, the open-question auditors.

Both halves are observable at this seat's closing stamp:

- **Immutability** — `git hash-object corpus/lessons/README.md` →
  `a31870556c733498243b56697896504a2fb3679a`, equal to the runner's own
  `README_BASELINE_BLOB`. The filed bytes are untouched.
- **The revision** — `reports/round-26/open-questions/README-rev3.md`
  landed during this seat's window, authored by the C41-C46 disposer
  seats. It is a new file, not an in-place rewrite.

This seat did not author that revision and does not certify it; the
disposition rows it carries are audited by `audit-dispositions.py`, which
re-runs the evidence of all six disposer fragments.

