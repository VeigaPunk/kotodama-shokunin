# controls-design — round-76 do-nothing and junk controls for claims C and Ca

Seat `ExecGapSweep` (wave 1, leaf). Base `98c486bdb4650ba5b8e651d332910e8ee60ad121`. 2026-10-27.
Nothing here was executed against a round-76 counter (none exists yet); every "expected" column is a
design commitment to be fitted to `reports/round-76/accept-c.py` / `accept-ca.py` at the freeze and
then MEASURED. Where a round-75 fixture already exercises the same shape, its raw result is quoted
and the control is marked `carried`. Where no round-75 fixture exists the control is marked `new`.

Inputs read (read-only):
- `.ufo/waves/round-76/CLAIMS-DRAFT.md` (claims C, Ca; before-state; kill rule).
- `reports/round-75/telemetry/controls-c.txt`, `junk-c.txt`, `controls-ca.txt`, `junk-ca.txt`.
- `reports/round-75/accept-c.py` (legs: ENTRIES 1176, ROWS 1282, REPOINTED 1730, GATE 1995,
  EVIDENCE 2340, REJECTS 2566, GROUND 2761, CITEDLINES 2831, CENSUS 2873, SCRATCHMIRROR 3017,
  COLLCHECK 3101, FROZENCFG 3635, INDEX 3927; `_ENTRIES_WORD_FLOOR = 478`).
- `reports/round-75/accept-ca.py` (legs: LEDGER 1328, BASEMISMATCH 1523, REPAIR 1581, ANNOTATE 1715,
  APPENDONLY 1812, NOSTUB 2014, SEPARABLE 2076, RECEIPTS 2235, R1EXEMPT 2458, COMBINED 2542,
  FROZENCFG 2585, STAMP 2634; `OBSERVE_ALLOW` 219, `INTERPRETERS` 224, `SHELL_META` 228,
  `R74_TMPDIR = "/tmp"` 2175).
- `.ufo/waves/round-75/counters/junk-fixtures.py` (`_newly_red` 1215; `accepted` = the counter's
  verdict was PASS, i.e. `accepted: no` = junk correctly refused).
- This seat's receipt `.ufo/waves/round-76/w1/stage/ExecGapSweep/gap-sweep.txt` (before-state
  numbers, staged-row shape, candidate shapes).
- Sibling wave-1 findings used, not duplicated: `w1/CritClaims1.md` (F1 false pre-state, F2 n/floor,
  F3 stub control, F5 ground, F6 body campaign ids, F8 identity, F9 README), `w1/CritCounterReuse.md`
  (freeze candidates not a row_set; dynamic n/k; `/tmp` worklist), `w1/ScribeEntryD.md` (F7 campaign
  ids in a lane-shaped field).

---

## 0. What a control is for, and the three ways a round-76 control can be worthless

A control is a landing the claim must REFUSE. A control is worthless if (i) it would also be refused
with no data landed (then it distinguishes nothing), (ii) the leg it is aimed at is already red on a
clean landing (then "newly-red" is empty and the leg's kill is unproven), or (iii) the mutation is
not in the bytes the leg reads (then a different leg fires and the aimed clause stays untested).
All three happened in round 75:

- (ii) `junk-ca.txt` baselines for J4/J4b/J4c/J4m/J4f/J5/J6/J7/J8/J9/J10 all read
  `baseline-legs: … APPENDONLY=FAIL, … COMBINED=FAIL, …`, so J6/J7/J10 report
  `newly-red: (none)` against `expected-legs: APPENDONLY` — three APPENDONLY fixtures proved nothing.
  Only fixture `R` reached APPENDONLY (`newly-red: APPENDONLY`).
- (iii) J4f was built to reach the Ca LEDGER clause: `expected: … the FROZEN ledger itself
  constant-prints expected_after … (this is the only fixture that reaches the LEDGER clause itself)`,
  yet its raw receipt reads `LEG PASS LEDGER` … `newly-red: FROZENCFG` / `expected-legs: LEDGER`.
  The mutation was committed at lands `8233ddb` while `--freeze 5d016746` still named the clean
  ledger, so LEDGER read the clean blob. **No round-75 fixture ever turned LEDGER red.**
- (i) r75 avoided this shape with `ACCEPT-C-75: FAIL legs=4/13` at `lands == freeze` (see C-a).

Design rule 1 (baseline first). Every fixture run must be preceded by the same counter on a clean
landing whose `baseline-legs:` line is all PASS. If a baseline leg is red, the fixture is void and
must be reported void, not as `newly-red: (none)`.
Design rule 2 (mutate the blob the leg reads). A config leg reads the blob at `--freeze`
(`accept-ca.py:1338` `if cfg.get("ledger_raw") is None: … a worktree copy is never read`); a tree
leg reads the blob at `--lands`. Mutations therefore go into a COMMIT, and the commit chosen for
`--freeze` vs `--lands` is part of the control's definition.
Design rule 3 (state the pass convention). `legs=A/B` in r75 counts PASSES
(`ACCEPT-C-75: FAIL legs=4/13` with nine `LEG FAIL` lines). Round 76 must print, per leg,
`expected` and `observed`, and the receipt must carry the quadruple
`baseline-legs / red-legs / newly-red / expected-legs` plus `accepted: yes|no`.
Design rule 4 (print the derivation). Claim C's admission set is a THRESHOLD (`n>=2` over four
candidate paths) and `k` is defined by document identity, so the counter must print the derived
`n`, the derived `k`, the admitted paths, and the document key per row before it grades them.
Without that, a control's red is unattributable (CritCounterReuse.md §(c)).
Design rule 5 (content, not counts). A control built only from counts cannot fail a content clause.
C-b2 below is the control that decides whether the frozen clause set is strong enough.

---

## 1. Claim C controls

### C-a — do-nothing: `lands == freeze` (`carried`, r75 controls-c control 1)

Mutation: none. `--lands <freeze> --freeze <freeze>` on a clean clone at the freeze.

Expected (r76): verdict `FAIL`; exit 1; `ENTRIES`, `ROWS`, `REPOINTED` must be in `newly-red`
(the draft says "must FAIL the data legs"), together with the quote/index legs that read landed
bytes (`GATE`, `EVIDENCE`, `REJECTS`, `CITEDLINES`, `INDEX`); `GROUND`, `CENSUS`, `COLLCHECK`,
`FROZENCFG` legitimately PASS (they measure base-relative facts).

Round-75 raw (controls-c.txt, `lands == freeze = 5d016746…`):
```
LEG FAIL ENTRIES / ROWS / REPOINTED / GATE / EVIDENCE / REJECTS / CITEDLINES / SCRATCHMIRROR / INDEX
LEG PASS GROUND / CENSUS / COLLCHECK / FROZENCFG
ACCEPT-C-75: FAIL legs=4/13
exit=1
```
Caveat to fix or disclose in r76: `FROZENCFG` PASSes at `lands == freeze` even though the same leg
prints `NOTE lands == freeze: do-nothing control shape; … a PASS is refused`. Round 76 must either
make FROZENCFG FAIL in that shape or state the note as a disclosed caveat of the leg.

### C-b — four header-only stubs at the four candidate paths, zero rows, zero evidence (`carried`, r75 J1 shape; `new` for amends)

Mutation (one commit): write the four candidate files as header-only stubs — the staged
`source:`/`verified-at:`/`recheck:`/`ground:`/`- topic:`/`- gap filled:`/`- sources:`/`- couples:`/
`- scope:` bullets copied verbatim, no `## ` section, no body — and add NO registry row, NO README
row, NO evidence file.

Why it must fail (measured in gap-sweep.txt §3.3): the shipped staged files themselves have
`h2=1/0/0/0` and 1094/445/275/340 words; the r75 ENTRIES leg requires "at least one `## ` section,
and a body of at least 478 words", and 478 is exactly the base minimum (`heritage-taxonomy-models.
amend-2026-10-24-r13.md` = 478 words), i.e. the floor is an amend-shaped norm, not a full-entry bar.

Expected `newly-red`: `ENTRIES` (section + floor), `ROWS` (row additions empty while four entries
cite documents), `REPOINTED` (entry `source:` lines carry campaign ids with no lane row), `INDEX`
(0 README rows for 4 new files), `GATE`/`EVIDENCE` (no committed window).

Round-75 raw (junk-c.txt J1 — two stubs plus rows whose used-by named the stubs):
```
newly-red: ENTRIES, INDEX, REPOINTED, ROWS      expected-legs: ENTRIES      accepted: no
```
C-b is a superset-red of J1's shape: it must be graded as `newly-red ⊇ {ENTRIES, ROWS, REPOINTED, INDEX}`.

### C-b2 — stubs plus sed-renumbered rows (the sizing control) (`new`)

Mutation: C-b's stubs, plus the six staged rows for the five documents rewritten minimally by sed —
campaign ids renumbered to the planned lane ids, `status mined`, `opened 2026-10-27`, `used-by` =
the four stub paths, the pipeline pipe in the recheck cell deleted (cell becomes `180d`), plus a
README row per stub and a Gate table with an admit and a reject.

This is CritClaims1.md F3's control. It is the one that separates a claim graded on counts from a
claim graded on content. Expected `newly-red` under an adequate clause set: `EVIDENCE` (no window
grammar / quote not inside a window), `GATE` (no locator, no access date), `CITEDLINES`, and
`ENTRIES` (body floor). **If C-b2 lands and the counter returns PASS, the frozen claim is
under-specified and the freeze must add the content clause** — that is the finding this control
exists to produce. Do not "fix" it by adding legs after the fact; freeze the clause first.

### C-c — the staged rows and entries appended verbatim (`new`, must be built)

Mutation (one commit): append `merge/kotodama/SOURCES.append.md`'s rows as-is and copy the four
staged entries as-is.

Why it must be red (measured in gap-sweep.txt §3.1): of 132 staged rows, `NF=13` only 7; `NF=14`
115, `NF=15` 9, `NF=16` 1, because the recheck cell holds an unescaped `|` from a shell pipeline
(e.g. S908 `180d — \`curl -fsSL '…/search' | grep -c '元号名称'\` -> 3`) and the used-by cell then
holds a grep count instead of entry paths. `opened` is `2026-10-23/24`, not `2026-10-27`.

Expected `newly-red`: `CENSUS` (`sources-census.sh validate` → `E01` malformed rows, exit 1; the
fleet script's own selftest asserts `E01-malformed-row` is killed), `ROWS` (cells ≠ 11 / a pipe in a
cell / recheck not cadence-only / opened / used-by), `REPOINTED` (campaign ids), `COLLCHECK` (the
35 ids S859–S893, `wc -l .ufo/waves/round-76/assimilation/collisions` → 35).

Round-75 precedent: no fixture lands verbatim staged rows. The nearest supporting evidence is the
ROWS docstring's reading R3 ("`row_cells` splits on every `|` … the row is failed for the escaped
pipe first (the as-is tell) and for the cell count second") and `scripts/sources-census.sh`'s
`E01-malformed-row` selftest. C-c is the one control that must be BUILT in wave 2 and whose red must
be shown, because the draft's kill rule explicitly names "a row appended as staged".

### C-d — borrowed support: entry files landed, every claim resting on a held row (`new`; J1/J2 shapes carried)

Mutation (one commit): land the four entry files with their `source:` lines re-pointed to the HELD
row S885 (Barthes, `persee.fr/doc/comm_0588-8018_1966_num_8_1_1113`) and add no new row; optionally
widen S885's `used-by` to the four entries.

Expected `newly-red`:
- `REPOINTED` — by-document join: S885's registered URL names Barthes, not the calendar/era document
  (`accept-c.py:1730` docstring: "every source line names exactly one id whose registered row URL
  names the cited document").
- `ROWS` — row additions empty against `k>=2` cited documents, and, if S885's `used-by` was widened,
  the "every pre-existing row is byte-identical" reading (R1/R5 both-ways used-by) fails.
- `EVIDENCE` — the window committed for S885 is round-75's Barthes window; the new Gate quote is not
  inside it (J2's exact clause).
- `GATE` — the row URL/anchor in the lesson do not match the admitted entry's document.

Round-75 raw: J1 `newly-red: ENTRIES, INDEX, REPOINTED, ROWS` (used-by rewritten to stub paths);
J2 `newly-red: EVIDENCE` (quote removed from a window whose sha256 was recomputed).

### C-e — the draft's own false ground receipt, landed as the receipt (`new`, cheap, recommended)

Mutation (one commit): land `reports/round-76/telemetry/gap-sweep.txt` with the draft's before-state
verbatim — i.e. `git grep -l -E 'GB/T 33661' 98c486b -- corpus` recorded as "0 files, exit 1" — while
the bytes actually give 2 files, exit 0 (gap-sweep.txt §2.1).

Expected `newly-red`: `GROUND`. Under r75's reading the leg scores the receipt per fragment (a
standalone `0` inside the fragment's own window, `accept-c.py:2800-2823`) and then re-derives absence
from the BASE REGISTRY (`2824-2828`). A receipt that prints exit 0 / 2 files for `GB/T 33661` has no
standalone 0 in that fragment's window → red. This control protects against the defect found in the
draft (sibling CritClaims1 F1, independently reproduced here) and costs one file.

---

## 2. Claim Ca controls

### Ca-a — do-nothing: `lands == freeze` (`carried`, r75 controls-ca control 1)

Expected (r76): verdict `FAIL`; the landing legs `REPAIR`, `ANNOTATE`, `NOSTUB` in `newly-red`;
`LEDGER`, `BASEMISMATCH` legitimately PASS (they read the freeze ledger and the base clone by design,
so they cannot distinguish a landing from no landing); `FROZENCFG`, `STAMP`, `SEPARABLE`,
`APPENDONLY`, `R1EXEMPT` expected green.

Round-75 raw (controls-ca.txt, `lands == freeze = 5d016746…`):
```
LEG FAIL REPAIR / ANNOTATE / NOSTUB / RECEIPTS / COMBINED
LEG PASS LEDGER / BASEMISMATCH / APPENDONLY / R1EXEMPT / SEPARABLE / FROZENCFG / STAMP
ACCEPT-CA-75: FAIL legs=7/12
exit=1
```
Carry the disclosed quirk: FROZENCFG PASSes here under the note "a PASS is refused"; r76 must decide
whether that note becomes a red leg or stays a disclosure, and the control's expectation must match
the frozen wording. `RECEIPTS`/`COMBINED` were red here because the r75 receipt set and the
`--combined` revision require a real landing; r76 should state whether they are landing legs.

### Ca-b — constant-printing `observe_cmd`, the FREEZE-side placement (`new`; J4f's intent, never achieved)

This is the control that must exist, because r75 never turned LEDGER red.

Mutation, three commits on a throwaway clone:
1. `M0` = base.
2. `M1` = base + the frozen round-76 config (`claims.json` with `ledger_raw`/`ledger_meta`) + a
   `reports/round-76/ledger.json` whose every `observe_cmd` is a literal constant printer
   (`["echo", "<expected_after>"]`, `["printf", "%s\n", "<expected_after>"]`) and whose
   `stated_at`/`parse`/`expected_after` fields are otherwise well-formed.
3. `M2` = `M1` + the real Ca landing.
Run `--freeze M1 --lands M2` (i.e. **`--freeze` names the printer ledger**).

Expected `newly-red`: `LEDGER` exactly (`observe_problem` → `argv[0] 'echo' not in the observe
allowlist`, `accept-ca.py:1137-1139`; `INTERPRETERS` refuses `python3 -c`). `FROZENCFG` must PASS —
freeze and lands carry the same ledger bytes — which is what separates this control from Ca-b2.

Shape variants that must all be included, each its own commit pair (r75 ids in brackets):
| variant | observe_cmd | expected | r75 evidence |
|---|---|---|---|
| literal echo/print | `["echo","<exp>"]` | LEDGER red | J4 (`newly-red: FROZENCFG` — placement wrong) |
| evasive printer | `["python3","-c","import os;assert os.sep;print(str(<exp>))"]` | LEDGER red (interpreter) | J4b |
| shell string with metacharacters | `"grep -c 'x' f \| wc -l"` | LEDGER red (not an argv) | J4c |
| allowlist escape | `["awk","-F|","{print $2}","corpus/SOURCES.md"]` | LEDGER red (`awk ∈ INTERPRETERS`); also `["env",…]`, `["xargs",…]`, `["sed",…]` | none in r75 |
| min-pairs trim | 2 well-formed pairs | LEDGER red (`pairs < min_pairs`) | J4m |
The `awk` variant matters beyond the control: the round-76 ledger cannot express a histogram pair
with `awk` (`OBSERVE_ALLOW` at `accept-ca.py:219` is git/grep/wc/sha256sum/ls/cat/head/tail/cut), so
any census-derived pair must be `git grep -c`-shaped or measured by a non-ledger receipt.

### Ca-b2 — constant printers at the LANDS side (`carried`, r75 J4/J4b/J4c/J4m)

Mutation: `--freeze <real freeze>` with a clean ledger; at `--lands` a commit whose `ledger.json`
carries the printers. Expected `newly-red`: `FROZENCFG` only (the freeze-vs-lands byte pin), NOT
LEDGER. Round-75 raw (four fixtures): `LEG PASS LEDGER` … `newly-red: FROZENCFG`,
`expected-legs: LEDGER, FROZENCFG`, `accepted: no`.
This control is kept precisely to document that it does NOT exercise LEDGER — r76 must not count it
as the constant-printer control.

### Ca-c — correction rows naming only ids (`carried`, r75 J5)

Mutation: land the real repairs, then reduce one `## Corrections — round 76` row to `| L76-01 |`.

Expected `newly-red`: `ANNOTATE` and `NOSTUB` (NOSTUB's minimum shape = leading id + old token +
new token + the pair's re-derivation command, `accept-ca.py:2014`).

Round-75 raw (J5): `newly-red: ANNOTATE, NOSTUB` / `expected-legs: ANNOTATE, NOSTUB` /
`accepted: no`. Two variants worth adding for r76 (both already one-fixture-cheap):
- SEPARABLE — the same row cites a claim-C lane id (S894–S898 or S885). r75 J8:
  `newly-red: SEPARABLE`.
- rederive honesty — the row carries old token, new token and a rederive command that does NOT
  reproduce the new token. r75's NOSTUB grades the shape only; the r76 counter should EXECUTE the
  rederive (allowlist: `git`, `grep`, …) and compare its output to the row's new token. Without that
  execution the clause "the pair's re-derivation command" is graded as prose.

### Ca-d — the routed `/tmp` defect (`new`, one static + one dynamic assertion)

The draft's Ca carries a routed defect: "the round-76 counters honour `TMPDIR`/`--work`/
`$HYAKU_SCRATCH` and write nothing under a literal `/tmp`". The defect in the round-75 instruments:
- `accept-ca.py:2175` `R74_TMPDIR = "/tmp"` is forced as the child `TMPDIR` when reproducing the
  round-74 counter's own receipts (`_run_r74_counter`, `2171-2182`; `HOME` fallbacks `/tmp` at
  `1165`, `2181`, `2220`).
- `accept-c.py:6024` refuses `/tmp` as `--work` (`banned = {os.path.abspath("/tmp"), …}`) but falls
  back to `tempfile.gettempdir()` when `$HYAKU_SCRATCH` is unset (`4450`, `5594`).

Control (static): `grep -n '/tmp' reports/round-76/accept-c.py reports/round-76/accept-ca.py` must
show no write path and no forced child `TMPDIR`; a hit is a finding, not a warning.
Control (dynamic), run as a fixture:
1. `--work $S/controls/ca-d/work` → every clone root printed in the receipt lies under `--work`;
2. `--work /tmp/hyakur76` → the counter refuses (r75 precedent at `accept-c.py:6024`);
3. the same fixture with `TMPDIR=$S/controls/ca-d/tmpdir` and no `--work` → the scratch root is
   `$HYAKU_SCRATCH/…` or `$TMPDIR/…`, never `/tmp`;
4. diff the receipt's own path tokens: no `/tmp/` substring.
Expected: all four hold; a failure is reported as the routed defect surviving into round 76.

---

## 3. Expected-red summary (freeze this table into claims.json)

| control | claim | mutation commit placement | expected `newly-red` ⊇ | must stay green | r75 status |
|---|---|---|---|---|---|
| C-a | C | none (`lands==freeze`) | ENTRIES, ROWS, REPOINTED | GROUND, CENSUS, COLLCHECK | carried (legs=4/13) |
| C-b | C | lands | ENTRIES, ROWS, REPOINTED, INDEX | GROUND, CENSUS, COLLCHECK, FROZENCFG | carried (J1 superset) |
| C-b2 | C | lands | EVIDENCE, GATE, CITEDLINES, ENTRIES | GROUND, CENSUS, COLLCHECK, FROZENCFG | new (decides clause adequacy) |
| C-c | C | lands | CENSUS, ROWS, REPOINTED, COLLCHECK | GROUND, FROZENCFG | new (must build) |
| C-d | C | lands | REPOINTED, ROWS, EVIDENCE, GATE | GROUND, CENSUS, COLLCHECK | new (J1/J2 shapes) |
| C-e | C | lands (receipt) | GROUND | CENSUS, COLLCHECK, FROZENCFG | new (guards F1) |
| Ca-a | Ca | none (`lands==freeze`) | REPAIR, ANNOTATE, NOSTUB | LEDGER, BASEMISMATCH, FROZENCFG, STAMP | carried (legs=7/12) |
| Ca-b | Ca | **freeze** (`--freeze M1`) | LEDGER (exactly) | FROZENCFG | new (J4f failed to reach it) |
| Ca-b2 | Ca | lands | FROZENCFG (not LEDGER) | LEDGER | carried (J4/J4b/J4c/J4m) |
| Ca-c | Ca | lands | ANNOTATE, NOSTUB (+SEPARABLE variant, +rederive-execution variant) | LEDGER, FROZENCFG, STAMP | carried (J5/J8) |
| Ca-d | Ca | none (probe) | (defect if any of the four assertions fails) | — | new |

Every row must be measured twice: (i) the clean-landing baseline, all PASS; (ii) the fixture, with
`newly-red` printed. A fixture whose baseline shows any red leg is void and is reported void.

## 4. Fixture mechanics (identical to r75, plus the two disciplines above)

- Scratch: `S=/fast/scratch/hyaku/kotodama-r76/ExecGapSweep`; each fixture under `$S/controls/<id>/`
  with its own `repo/` clone; `trap 'rm -rf -- "$S"' EXIT` after receipts are copied into
  `.ufo/waves/round-76/w1/stage/ExecGapSweep/controls/`. Never `/tmp`, never the lane.
- Clone: `git clone <lane> repo && git -C repo checkout --detach <base>`; identity `junk`
  (`git -C repo config user.name junk; … user.email junk@invalid`) set ONLY inside the clone;
  before the first commit `git -C "$D" rev-parse --show-toplevel` must print exactly `$D`.
- Every mutation is committed (`git -C repo add -A; git -C repo commit -q -m '<control id>'`), because
  CENSUS/INDEX/GATE read committed bytes; `--lands` is a commit, never a worktree.
- Receipt per fixture: `fixture/id/claim/mutation/commits(--freeze,--lands,--base)/command/exit/
  LEG lines/baseline-legs/red-legs/newly-red/expected-legs/accepted`. Raw stdout pasted, per the
  r75 file grammar in `reports/round-75/telemetry/junk-c*.txt`.
- The counter is never run from the lane worktree during wave 1; wave 1 writes design and receipts
  only, and no build/lint/test is executed here.

## 5. Open decisions the freeze must fix before any of this can be measured

1. Leg names and the pass-count convention (`legs=PASS/total`), and whether r76 keeps r75's 13/12
   leg split or adds legs (tier-C support, couples resolution, content probes, TMPDIR).
2. `--freeze` vs `--lands` reads for each new leg (design rule 2), stated in the counter docstring.
3. The tier-C clause's scope: lane-wide is RED at base (4 pre-existing `W01` rows: S881, S882, S884,
   S893 in `reports/round-76/telemetry/census-start.txt`); it must be scoped to the round's admitted
   entries, or the claim fails before data.
4. Document identity (S908+S935 folded; S932 vs S938 split) and therefore `k` — CritClaims1 F8.
   A control cannot be written against `k` until the fold rule and the map are frozen.
5. The content clause that C-b2 tests (quote ≤ 25 tokens inside the cited row's window, per admitted
   entry) — CritClaims1 F3. Without it C-b2 PASSes and the claim is a count claim.
