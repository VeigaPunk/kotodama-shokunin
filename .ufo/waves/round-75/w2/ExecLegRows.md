# ExecLegRows — round 75, wave 2: `leg_rows` (registry row diff) for claim C

Seat: ExecLegRows (executor, leaf). Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, base
`f556d1049fe651d3d63975600b13acd9fb686f15`. Wrote exactly two things: the part file and this report.
Claims/ledger/registry/lesson were read only; no git or jj state touched; shokuknow, the fleet repo and
sibling lanes untouched; no tool installed (nothing needed: `git`, `python3`, `tar`).
Scratch `/fast/scratch/hyaku/kotodama-r75/ExecLegRows/` (base extract, mock, lab driver) deleted before
yield; the full receipt text is in §5, so no scratch path is citable evidence.

**Part file** `.ufo/waves/round-75/w2/parts/leg-rows.py`, 184 lines, function definitions only, no
top-level code, no new imports:

```
597228d1b68a9828dcc5d3a4010679694bd3d1ea835cb02a413bbc6a1821c441  parts/leg-rows.py
```

`PART A (accept-c.py:1-510) + part` compiles clean (`python3 -B -m py_compile`).

## 1. The leg wording as I read it

Frozen text (`reports/round-75/claims.json`, claim C, `legs[1]` — verbatim):

> ROWS: the registry diff base..\<lands> adds exactly the frozen row_set (contiguous ids), none
> removed; each row status mined, opened 2026-10-27, a cadence-only recheck cell, 11 cells, no pipe in
> any cell, the evidence quote inside the anchor cell, used-by exactly the admitted entries whose
> source: lines cite it; every pre-existing row is byte-identical

Graded clauses, in the order the part checks them:

| # | clause | implementation |
|---|---|---|
| 1 | diff adds exactly the frozen row_set | `Counter` line multiset of `corpus/SOURCES.md` at `mat_base` vs `mat`; added non-blank lines must all be rows of `cfg["rows"]` and their multiset must equal it; a row line twice fails |
| 2 | contiguous ids | the ids actually added must be a run |
| 3 | none removed | any removed non-blank line fails, naming the row id |
| 4 | every pre-existing row byte-identical | same diff: a changed pre-existing line shows up as one removal + one non-row_set insertion |
| 5 | status mined | `cells[STATUS] == "mined"` |
| 6 | opened 2026-10-27 | `cells[OPENED] == cfg["access_date"]` (never a literal) |
| 7 | cadence-only recheck cell | `RECHECK_RE` **and** `_rows_cadence_ok` (see A2) |
| 8 | 11 cells / no pipe in any cell | `"\\|" in row` fails first (as-is tell), then `len(row_cells(row)) == NCELLS` |
| 9 | the evidence quote inside the anchor cell | evidence file's `quote:` vs `cells[ANCHOR]`, NFKC + whitespace folded, one wrapping quotation pair optionally stripped |
| 10 | used-by exactly the admitting entries | `row_usedby(cells)` == the set of `cfg["entries"]` whose `source:` header lines cite the id (`_entry_citations`), **and that set is non-empty** |
| 11 | (whole leg) | `leg("ROWS", not bad, ...)`; ids `S885..S893` from `cfg["rows"]`, paths from `cfg["entries"]` |

Nothing else is graded. The by-document map, the document URL in the source cell, the multi-id
`staged` field and `row_doc` are **not** ROWS clauses (they belong to FROZENCFG/REPOINTED/COLLCHECK);
the r74 template's map-URL check inside `leg_rows` is deliberately dropped so this leg is neither
stronger nor weaker than its wording, and so `leg_rows` has no dependency on `_map_records` (owned by
`leg-repointed.py`).

## 2. Ambiguities and how I resolved them

**A1 — the multiset diff allows a blank line but nothing else.** "adds exactly the frozen row_set" is
graded on the whole registry line multiset, not only row lines: a prose line inserted beside the rows
is an addition that is not in the row_set (mutant m13). A blank line adds no row and hides no row, so
it is tolerated on either side (control t1) — that is the only addition/removal that passes.

**A2 — "a cadence-only recheck cell" is stronger than `RECHECK_RE` as written.** PART A's
`RECHECK_RE` (`^(?:\d+d|[a-z][a-z0-9]*(?:[ -][a-z0-9]+)*)$`) accepts any all-lowercase phrase, so the
campaign recheck sentence `re-open on 2026-10-23 and re-count the span in the served transcription`
**passes it** (mutant m4b, verified: PASS before the fix, FAIL after). Its own docstring states the
real rule — "never an ISO date, never a composite cell with prose in it". The part therefore requires
`RECHECK_RE` **and** an inline `re.fullmatch(r"\d+d|[a-z][a-z-]{0,23}(?: [a-z][a-z-]{0,23}){0,2}", cell)` (the stdlib caches string patterns, so no module-level constant and no per-row compile):
a `NNd` cadence or at most three lower-case/hyphen words with no digits. The lane's own vocabulary is
`365d 180d 90d on-release` (390/230/18/14 base rows; the other 154 base rows carry `2027-10-2x` dates,
which the claim's "cadence-only" clause excludes from *new* rows and which no clause touches because
pre-existing rows must stay byte-identical). Control t3 proves `365d 180d 90d on-release quarterly
"per round" "each round"` all pass. **PART A diff requested from the L1** (see §6).

**A3 — "used-by exactly the admitted entries whose source: lines cite it" is non-empty.** A row whose
used-by is `—` because no configured entry cites it satisfies the equality trivially (empty == empty):
that is the r74 template's survivor and SimplifierRows §2.2's "ORPHAN ROWS ARE COUNTER-LEGAL" trap. Read
as an exact bijection, the clause is satisfied by an empty cell, which would let a row claim coverage no
entry delivers — the very thing the claim's `after` ("Each adopted row is opened this round …", "one row
per distinct document") and the kill rule ("any staged row is appended as-is") forbid. So the leg
requires the citing set to be non-empty and reports the orphan explicitly (mutant m1). The set is
derived only from `source:` header lines (`_entry_citations`) — an inline mention in the body does not
bind a row; that is the registry contract's own binding (`used-by` names the entries that cite the row
through their `source:` line).

**A4 — "the evidence quote".** Read as the evidence file's `quote:` field, never its self-attested
`quote-found:`/`quote-found-verbatim:` flags (round-74 H2 discipline). A row with no committed evidence
file has no quote to sit inside its anchor cell: it fails here too (mutant m14), not only in EVIDENCE.
The comparison is `nfkc_ws(quote) in nfkc_ws(anchor)`; because the producer may store the span bare
while the anchor wraps it in `«…»`/`「…」`, one wrapping quotation pair is stripped as an accepted second
form (control t2). The anchor cell is the 6th cell (`ANCHOR`), the field the registry contract calls the
anchor; the `scope` cell's prose is not used for location.

**A5 — reused rows.** `claims.json` declares `reused_rows: []`, and the wording grants no in-place
exception ("every pre-existing row is byte-identical"), so the r74 template's reused-row branch is not
implemented: any removed non-blank line fails. `cfg["reused"]` is read by no clause of this leg. If a
later freeze declares a reused row, that is a predicate change, not a counter change.

**A6 — no evidence-quote direction check on the anchor's locator prose.** Only the quote text has to be
inside the anchor cell; the locator half of the anchor cell is GATE's business, not ROWS'.

**A7 — detail line length.** Details are `"; ".join(...)` with no newlines; the first line can exceed
300 characters on multi-row failures exactly as r74's legs do (`leg()` in PART A prints it verbatim and
does not truncate). Truncating would hide which rows failed.

## 3. Interface facts a sibling/owner must not break

* Calls from PART A only: `read_tree`, `parse_rows`, `row_cells`, `row_usedby`, `nfkc_ws`, `dedupe`,
  `leg`, `Missing`, `QUOTE_RE`, `RECHECK_RE`, `REGISTRY`, `EVIDENCE_DIR`, `ROW_RE`, `NCELLS`,
  `STATUS`, `OPENED`, `RECHECK`, `ANCHOR`, `USEDBY`, `Counter`.
* Calls from **part-cfg.py** (never redefined here): `_entry_citations(mat, entries, bad)` and
  `_evidence(mat, sid)` (the latter calls `_window`). Both must keep the r74 signatures/return shapes:
  `{sid: set(entry paths)}` and a lower-cased key dict with `quote`, or `None` when the file is absent.
* `leg_rows` reads `cfg["rows"]` (ordered lane ids), `cfg["entries"]` (the admitted paths) and
  `cfg["access_date"]` only. `row_staged` (multi-id lists), `row_doc`, `map_*` and `owned_inplace` are
  not read by this leg — the multi-id staged rows (`S876/S885/S917/S921` → one row) are enforced here
  by the fact that `S885` can be added exactly once and is the only row allowed for it.
* Private helpers carry the `_rows_` stem: `_rows_quote_core`, `_rows_cadence_ok`. The file is function
  definitions only — no module-level constant and no import (the cadence pattern is an inline literal).

## 4. Landing consequences the L1 should see before the append

1. **`used-by` is bound only by `source:` header lines.** The drafts as they stand put the base entry's
   five documents behind **one** `source:` line (`S885`); the other four (`S888`, `S889`, `S890`,
   `S893`) are cited in the body/`sources:` prose only. Mutant **m16** (the real draft dropped in) is
   red on exactly those four rows. The landing must carry one `source:` line per row it adopts — which
   REPOINTED's "exactly one id per `source:` line" already forces. The mock positive does that.
2. **The staged rows in `assimilation/validate/corpus/SOURCES.md` are already the right shape**
   (11 cells, `mined`, `2026-10-27`, `180d`, no `\|`) except for their `used-by` cells, which name the
   two-entry set (S891/S892 point at `amend-2026-10-23.md` instead of `amend-2026-10-23b.md`). They must
   be recomputed from the entries actually landed.
3. **Do not carry a blank line between appended rows if you want zero noise** — tolerated, but it is
   the one non-row difference this leg allows.

## 5. Positive / mutant table (executed, final part bytes)

Mock (built in scratch, deleted): base tree extracted from `f556d104…` with `git archive`; the three
**unlanded** drafts copied to `corpus/knowledge/myth-symbol/`; the base entry extended with one
`source:` line per document (S885, S888, S889, S890, S893); the nine staged rows S885..S893 inserted
after S884 with `used-by` recomputed from the three entries' `source:` lines; nine evidence files whose
`quote:` is each row's anchor quote (the probe receipts under
`.ufo/waves/round-75/counters/probe-receipts/` carry the *notice-title* quotes, so they cannot serve as
the mock's located quotes — the shape was taken from them, including `S892`'s whole-document form).
Harness: `exec(PART A lines 1-510) + part-cfg stand-in + parts/leg-rows.py` in one namespace, ctx =
{root, lands, mat, mat_base, cfg, fleet_root, scratch}; `cfg` built by hand per CFG-CONTRACT.md
(`part-cfg.py` does not exist yet).

| case | mutation | result |
|---|---|---|
| positive | none | `LEG PASS ROWS` |
| m1-orphan-dash | S892's `source:` line removed from amend-23b **and** its used-by set to `—` | FAIL — `S892 is cited by no admitted entry (orphan row; used-by='—')` |
| m2-usedby-extra | S886's used-by gains the base entry (which does not cite it) | FAIL — `S886 used-by=[…amend-2026-10-23.md, …frameworks.md] (want exactly the admitting entries [ …amend-2026-10-23.md])` |
| m3-usedby-missing | S892's used-by names the base entry instead of amend-23b | FAIL — `S892 used-by=['…frameworks.md'] (want exactly the admitting entries ['…amend-2026-10-23b.md'])` |
| m4-staged-recheck | S887 recheck = `curl … \| pdftotext … \| grep -c … -> 3 (ran 2026-10-23)` | FAIL — `S887 row has 13 cells (want 11: no pipe inside any cell)` |
| m4b-staged-recheck-plain | S887 recheck = `re-open on 2026-10-23 and re-count the span in the served transcription` (no pipe) | FAIL — `S887 recheck='…' is not a cadence-only cell` |
| m5-escaped-pipe | S890 teaches cell gains `story \| quest` | FAIL — `S890 row carries an escaped pipe (a staged cell appended as-is)` |
| m6-opened-staged | S889 opened = `2026-10-23` | FAIL — `S889 opened='2026-10-23' (want 2026-10-27)` |
| m7-status-queued | S888 status = `queued` | FAIL — `S888 status='queued' (want mined)` |
| m8-pre-existing-edit | pre-existing row S100's tier cell edited | FAIL — `pre-existing S100 line removed (every pre-existing row must stay byte-identical) …; row lines added ['S100', …]` |
| m9-row-removed | pre-existing row S884 deleted | FAIL — `pre-existing S884 line removed …; rows present at base but not at lands: ['S884']` |
| m10-noncontiguous | S891 row and its `source:` line deleted → S885..S890, S892..S893 | FAIL — `added ids are not contiguous: [885, …, 890, 892, 893]; rows missing at lands: ['S891']` |
| m11-duplicate-row | the S885 line inserted twice | FAIL — `a row line is added twice: ['S885']` |
| m12-anchor-no-quote | S885's anchor cell replaced by its locator only | FAIL — `S885 anchor cell does not contain its evidence quote ('Innombrables sont les récits du monde.')` |
| m13-extra-prose | a prose sentence inserted beside the rows | FAIL — `registry line added outside the frozen row_set: 'These rows were adopted in round 75 by claim C.'` |
| m14-missing-evidence | `reports/round-75/evidence/S885.txt` deleted | FAIL — `S885 has no committed evidence file (reports/round-75/evidence/S885.txt)` |
| m15-no-rows-added | registry = base bytes (do-nothing landing) | FAIL — `row lines added [] (want the frozen row_set [S885…S893]); … rows missing at lands: [S885…S893]` |
| m16-drafts-as-is | the real unlanded base draft (single `source:` line) | FAIL — `S888/S889/S890/S893 is cited by no admitted entry …` (see §4.1) |
| t1-blank-line | one blank line inserted between the new rows | **PASS** (tolerance intended) |
| t2-quote-wrapped | S885 evidence `quote:` wrapped in `«…»` while the anchor has it bare | **PASS** (A4) |
| t3-cadence-vocabulary | all nine rows set to `365d/180d/90d/on-release/quarterly/per round/each round/…` | **PASS** (A2) |

Verbatim driver output for every case is reproduced above (same text the seat's `lab.py` printed; the
only compression is the `…` elisions marked in two long detail lines).

## 6. Requests / open points for the L1 (nothing in claims.json edited by me)

1. **PART A `RECHECK_RE` (accept-c.py constant block).** It cannot express "cadence-only" (A2). Either
   keep it and rely on `_rows_cadence_ok` (works today), or tighten the constant to
   `^(?:\d+d|[a-z][a-z-]{0,23}(?: [a-z][a-z-]{0,23}){0,2})$`. The part is compatible with both.
2. **Claim C `entries` vs `used-by` derivation** — §4.1: the landing must bind every adopted row with a
   `source:` line, otherwise ROWS (this leg) and REPOINTED both go red on the same four rows.
3. **`part-cfg.py` must expose `_entry_citations` and `_evidence` with the r74 bodies** (§3). I could
   not test against the real `part-cfg.py` (it did not exist at 16:5x); the stand-in is the r74 text
   quoted in CFG-CONTRACT.md ("the r74 lines 473-745").

## 7. Not done (deliberately outside this seat)

No claim/ledger edit; no acceptance counter assembled; no build/lint/test of the lane; no network fetch
(no source was opened by this seat); no judgement of any sibling leg; no commit, stage or git/jj
mutation anywhere. Scratch removed; only `parts/leg-rows.py` and this report were written.
