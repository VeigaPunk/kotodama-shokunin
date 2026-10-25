# CritD2 — attack on claim D2's error-signature requirement (round-69 w1)

Seat: attack leaf, godspeed posture, 2026-10-24. Lane
`/home/vgpnk/Projects/shokunin/kotodama-shokunin`, base `793f7974`, read at
HEAD `6a98d7d0` (jj-colocated; read-only git only). Production bytes untouched;
every mutation below is a copy under `/tmp` (`/tmp/critd2-collision.py`,
`/tmp/critd2-mutants.py`, `/tmp/critd2-scan/`).

## What the frozen counter actually enforces

`reports/round-69/accept-d.py` (`:160-165`) is the whole of the
error-signature requirement:

```python
ep_start, ep_end = section_span(lines, "## Error patterns")
ep_text = "\n".join(lines[ep_start:ep_end]) if ep_start is not None else ""
missing_sig = [r[3] for r in rows if len(r) >= 4 and r[3] and r[3] not in ep_text]
res.add("SIGNATURES", not missing_sig, "missing=%s" % (missing_sig or "none"))
```

Exact, case-sensitive substring containment of each table's 4th cell
("Error signature") anywhere inside the `## Error patterns` span (up to the
next `## ` heading, i.e. `## Boundaries (hard)` — both tables and any prose
count). Nothing more: no distinctness check, no requirement that the string
sit in an Observation cell, no line-anchor resolution (the EVIDENCE leg
`accept-d.py:167-175` only extracts a path token via `PATH_RE` and
`os.path.exists`).

## What a named error signature must look like to be usable there

Derived from the section's own grammar (31 existing observation cells:
22 in the craft table `| Observation | Reading |`, 9 leading the uncertainty
table) and the lane's two named-code vocabularies
(`D2L-*`/`D3-*` executable finding ids vs the fixture's lowercase-kebab
compounds):

1. **Names an artifact state you can point at** — a registry cell value, a
   cell absence, or a `tools/check-supersession-settlement.py --scan` output
   line — never a category or the chain-state label restated.
2. **Short kebab compound, byte-identical in both places** — it must appear
   exactly twice in SKILL.md after landing (table cell + Error patterns
   Observation); the leg is substring-based, so any case drift breaks it.
3. **Five names, five different observables** — no two reducible to the same
   cell condition (the counter does not check this; the claim wording does).
4. **Observation cell carries the condition, Reading cell the action+anchor**
   — shape: ``| `name` — condition sentence | reading; writer's action;
   anchor (S859; tools/check-supersession-settlement.py:NNN) |``.
5. **No collision** with any existing observation, string-wise or by domain.

The kebab grammar is the only executable-honest choice today: the settlement
checker emits class tokens (`PENDING`, `SETTLED-*`) and counters
(`pending=N missing_paths=K`), **no per-state finding id** — and
`STALE-USED-BY` exists only in its docstring (`grep -n "STALE-USED-BY"
tools/check-supersession-settlement.py` → line 21 only, never printed by
`scan()`).

## The five candidates

| Chain state | Candidate | Observable condition (the thing you see) | Executable anchor | vs pre-registered fixture name |
|---|---|---|---|---|
| `pending` | `chain-left-pending` | a supersedes pair with no ruling: scan prints `PENDING Sxxx>Syyy …`, `SETTLEMENT: pending>=1` | `check-supersession-settlement.py:132-133` | same |
| `settled-active` | `entry-not-repointed` | successor row `status=mined` whose `used-by` cell is `—` (no entry re-pointed); scan keeps it `PENDING` with `used_by=0` | `:127-128` | same |
| `settled-retired` | `retired-row-mined` | a `rejected` correction row still cited/read as current (still in a used-by chain or Paths) | `:125-126`; **not gated** — scan exit gates `pending` only | same name; fixture's Evidence cites the wrong line (below) |
| `settled-closed` | `closed-successor-dropped` | the kept successor row is missing from the registry / its supersedes pointer erased — the chain vanishes from `scan()` entirely (no pointer, no chain); only receipts/diffs see it | `:123-124`; review teeth only | **amended** from fixture `closed-chain-kept` |
| `settled-split` | `scope-limiter-missing` | both rows `mined` and the successor `teaches` lacks a `for … only` clause (`SPLIT_RE`, `:54`); scan prints `PENDING S002>S001 s=mined t=mined …` | `:129-131` | same |

Distinctness: five disjoint artifact conditions — unruled pair; empty used-by
cell; rejected-but-still-cited; kept row missing; limiter-less teaches. No two
collapse into the other.

Why the one amendment: the fixture's `closed-chain-kept` contradicts its own
pre-registered reading — `accept-d.py:58`: "the closed chain's successor was
**dropped**". A name that says "kept" for a dropped-successor defect fails the
observable-condition bar; `closed-successor-dropped` states exactly what you
see. The counter is indifferent (mutant D below), so this is a craft choice,
free of teeth.

## Collision cross-check (mechanical)

`python3 /tmp/critd2-collision.py` over live SKILL.md:

```
observation_rows=31   (22 craft + 9 uncertainty; header excluded)
chain-left-pending: 0     entry-not-repointed: 0    retired-row-mined: 0
closed-chain-kept: 0      closed-successor-dropped: 0    scope-limiter-missing: 0
kebab tokens present in the section: 45, all path fragments or prose
hyphenations — none matches a candidate
```

Semantically: existing observations live in lexicon/myth/costume/naming/loan/
label/handoff-claim domains; the nearest neighbors (the uncertainty-table rows
"A claim's status rides as prose…", "A digest match or gate exit 0 offered as
a claim's basis") are about the handoff packet's claim ledger, a different
artifact from the `corpus/SOURCES.md` registry. Zero collision.

## Attack findings (each demonstrated against a /tmp copy)

Pre-data controls first — both instruments healthy at HEAD:

```
$ python3 -B reports/round-69/accept-d.py --selftest
GREEN FIXTURE: PASS (legs 8/8)
DO-NOTHING FIXTURE: FAIL (as required) (legs 1/8)
SELFTEST: 2/2
$ python3 -B tools/check-settlement-fixture.py --selftest
PASS fixture-green rc=0 pending=0 missing_paths=0
PASS fixture-negative rc=0 pending=0 missing_paths=1
PASS fixture-pending rc=1 pending=1 missing_paths=0
FIXTURE: 3/3
```

`python3 /tmp/critd2-mutants.py` (mutates copies of the counter's own green
fixture, re-runs `evaluate()`):

```
MUTANT A-dup      -> PASS (8/8 legs)          all five signature cells identical
MUTANT B-recycle  -> PASS (8/8 legs)          cell 1 = "A record with no declared kind at all" (existing O13)
MUTANT C-case     -> FAIL (7/8 legs)  failed: SIGNATURES   "Chain-Left-Pending" vs lowercase in Error patterns
MUTANT D-amend    -> PASS (8/8 legs)          closed-chain-kept -> closed-successor-dropped in both places
```

- **F1 — distinctness is unenforced** (A-dup). Five identical signatures
  print `ACCEPT-D-69: PASS`. The claim's "each distinct" lives only in the
  wording; a duplicated-name table is indistinguishable to the counter.
- **F2 — a recycled observation passes with no new Error-patterns row** (B).
  Reusing an existing observation string satisfies the substring without
  listing anything new; the claim's "also listed under `## Error patterns`"
  is weaker than the leg that carries it.
- **F3 — the coupling is byte-exact** (C). Case drift alone fails the leg.
  L1 self-check after landing: `grep -c <name> SKILL.md` must print `2` for
  each of the five names.
- **F4 — fixture/data vocabulary is unpinned** (D). The landed table may use
  amended names; the counter cannot tell. Prefer landing the amended set
  above (or fixture-verbatim, consciously) and record the choice in
  `corpus/lessons/round-69.md`.
- **F5 — the pre-registered Evidence line anchors are partly stale.**
  `grep -n` on the checker: `:123-124` settled-closed, `:125-126`
  settled-retired, `:127-128` settled-active, `:129-131` settled-split,
  `:132-133` pending. The fixture table (`accept-d.py:46-50`) cites
  `:112` for pending (the `def classify` head, not the pending branch) and
  `:129` for settled-retired (that line is the **settled-split** condition).
  EVIDENCE only checks path existence, so it cannot catch this; land the
  table with corrected anchors.
- **F6 — no signature has executable teeth.** The checker's exit gates
  `pending` alone; `retired-row-mined` and `closed-successor-dropped` move no
  exit code, and `STALE-USED-BY` is docstring-only. The depth claim must not
  imply gate enforcement; anchor Evidence to the true branch lines and, where
  honest, to the registry bytes/receipts.

Real scan line for the anchoring shape (pending pair, missing used-by file):

```
PENDING S002>S001 s=mined t=mined same_url=True used_by=1
SETTLEMENT: pending=1 chains=1 usedby_paths=1 missing_paths=1
```

## Recommendation to the L1

Land Set B — `chain-left-pending`, `entry-not-repointed`, `retired-row-mined`,
`closed-successor-dropped`, `scope-limiter-missing` — with corrected Evidence
anchors (`:132-133`, `:127-128`, `:125-126`, `:123-124`, `:129-131`), rows in
frozen order pending → settled-active → settled-retired → settled-closed →
settled-split (the STATES leg lowercases `rows[i][0]` and compares in order),
names byte-identical in table and Error patterns (grep-count 2 each), each
Error-patterns Reading naming the writer's action and the anchor. All of this
is counter-compatible today; F1/F2 remain open as leg-strength limits, not
data defects.

## Verdicts

- VERDICT: PASS — five candidate signatures proposed; each distinct, each
  naming an observable registry/scan condition rather than a category;
  mechanically collision-free against all 31 existing Error patterns
  observations.
- VERDICT: PASS — pre-data instruments healthy (accept-d selftest 2/2,
  settlement fixture 3/3); the amendment `closed-successor-dropped` lands
  clean through the counter (mutant D).
- VERDICT: FAIL — the SIGNATURES leg is weaker than the claim's depth bar:
  substring-only containment (F2), distinctness unenforced (F1), case-brittle
  (F3), Evidence line anchors unresolved (F5). These are leg-strength limits
  for the record; they do not block the data.
- VERDICT: FAIL — executable-anchor claim: none of the five signatures has a
  gate emitter today; `STALE-USED-BY` is docstring-only (F6). Depth wording
  must stay review-anchored.
- VERDICT: NOT-EVALUATED — the landed data itself: the SKILL.md table, the
  S859 SOURCES row and `corpus/lessons/round-69.md` are absent at measurement
  time (`grep -c S859 corpus/SOURCES.md` → 0; `ls corpus/lessons/round-69.md`
  → not found) — pre-data by design, judged by the integrating L1, not this
  seat.
