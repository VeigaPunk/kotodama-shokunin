# RevWaveShape — round-67 v2 wave shape (seat count, attack fraction, §3 role split, padding)

Seat: reviewer (attack). Scope: `.ufo/waves/round-67/spec-v2.json`, `taskcall-v2.json`,
`w1/swarm-registry.json`, and the frozen counters only where a seat item's landability turns on
them. Nothing edited outside this file; no git/jj write; no lane mutation.

**Verdict: band and §3 split PASS. One defect RESOLVED by L1 sequencing (per-claim lands separation
makes the S829+ rejects landable at Ca's commit; the single-lands-commit reading — the only one
`claims.json` states — still fails, so the ordering must be recorded in a frozen artifact). One
HIGH remains: Ca D4 is satisfiable by reclassifying already-mined base rows instead of adding
rejected rows, confirmed against the current counters; L1 ruled no revision, so it is residual
instrument risk. One HIGH staffing gap: the claim's central artifact (the entry body) has no author
seat.**

## 1. Counts — all three artifacts agree at 64

```
spec items: 64   taskcall tasks: 64   registry members: 64
counts: {'spawn': 64, 'resume': 0, 'total': 64}
policy: waveMinLanes 64, waveMaxLanes 128, declaredMaxLanes null
names equal spec<->taskcall<->registry: True | duplicate names: none
taskcall task = spec prompt + "/skill:godspeed" + lane bounds/judged/milestone/Report trailer
(no substantive prompt drift: 64/64 differ only by that appended trailer)
```

64 seats sits exactly on the v2 lower band (`waveMinLanes 64`), one `taskCall`, one wave. PASS.

## 2. Attack fraction — PASS (36/64 = 56.2%)

| role | seats | class |
|---|---|---|
| scout | 15 | build |
| scribe | 7 | build |
| executor | 4 | build |
| connector | 2 | build |
| critic | 12 | attack |
| reviewer | 20 | attack |
| mutation-tester | 2 | attack |
| revenger | 1 | attack |
| sentinel | 1 | attack (scope/security audit of the instruments) |
| **total** | **64** | |

Attack 36 (56.2%) / build 28 (43.8%); if `sentinel` is scored as build it is still 35/64 (54.7%).
Either way ≥25%. No role named `adversary` exists in the fleet role set; critic+reviewer+revenger+
mutation-tester+sentinel carry the attack class here.

## 3. §3 minimum role split — PASS

planner = L1 (outside the 64, per wave context) · connector 2 ≥ 1 · executor 4 ≥ 3 · scribe 7 ≥ 1 ·
scout 15 ≥ 1 · reviewer 20 ≥ 1 · critic 12 ≥ 1.

## 4. Reject-row ids vs claim C's append bound — RESOLVED by per-claim lands sequencing (design finding)

**Resolution (L1 ruling, received after the first draft of this report): per-claim lands separation,
no counter/claims revision. A_r (S801-S804 + r66 dispositions) lands first, C's receipt runs at
A_c where only S805-S828 append over base, and Ca's lands commit A_ca comes later carrying the
S829+ reject rows. Claims are stamped at their own lands commit; none is evaluated at tip.**

I re-ran the boundary on the scratch lane and the sequencing is arithmetically sound:

```
# A_c-equivalent: base + S801-S804 + S805-S828 (28 appended), no S829+
$ python3 -B reports/round-67/accept-c.py --root /tmp/r67shape --lands 6ab76c26…
SET    PASS missing=[] non-unique=[]
ROWS   PASS bad=[] n=0
APPEND PASS missing_old=[] appended=28 extra=[] immutable_violations=[]

# A_ca-equivalent: + S829-S832
$ python3 -B reports/round-67/accept-ca.py --root /tmp/r67shape --lands 91226196…
D4     PASS bad=[] r66_rejects=4 opened_today=10

# C re-run at A_ca (i.e. at tip)
$ python3 -B reports/round-67/accept-c.py --root /tmp/r67shape --lands 91226196…
APPEND FAIL missing_old=[] appended=32 extra=['S829','S830','S831','S832'] immutable_violations=[]
```

(`opened_today=10` is 8 sequenced rejects plus the two flips retained from §5's earlier commit —
the same artefact §5 describes.)

The single-lands-commit reading, which is the only reading the frozen artifacts state, still fails:

Claim C's `APPEND` leg is bounded to `NEW_IDS ∪ EXTRA_IDS` = S805–S828 ∪ {S801–S804}
(`reports/round-67/accept-c.py:67,70,357-358`). Three seats draft outside that bound:

- `ScoutReject1` — "write …/rows/ScoutReject1/row-S829.txt and row-S830.txt (temporary ids S829/S830)".
- `ScoutReject2` — "write rows/ScoutReject2/row-S831.txt and row-S832.txt (temporary ids S831/S832)".
- `ScribeGateRows` — "draft the rejected-row Gate lines for S801-S804 (r66 dispositions) **and
  S829-S832 (this round's rejects)**".

The wave already knows these ids are outside the instrument's view: `RevIntegrity`'s item asks
"which claim bytes could land outside counters' view — S829+ ids sneaking into the claim set".
No prompt tells the L1 to renumber S829-S832 into S801-S804, and the four S801-S804 slots are
already occupied by the r66 dispositions in every other seat's text.

Proof (scratch lane at /tmp/r67shape, clone of this repo, base tree + registry edits, committed
`b4f830c3a31795f150d20b3369bc4e0ba6350af5`; no lane mutation):

```
$ python3 -B reports/round-67/accept-c.py --root /tmp/r67shape --lands b4f830c3…
APPEND FAIL missing_old=[] appended=5 extra=['S829'] immutable_violations=[]
```

The same tree **without** S829 — four added reject rows S801-S804 — passes `APPEND` (see §5).
So on the single-commit reading the two reject seats produce registry bytes that flip the frozen C
predicate to FAIL, and `ScribeGateRows` drafts Gate evidence for the same ids: 2 of 28 build seats
and part of a 7th scribe item would be unlandable.

Residual defects after the sequencing ruling (none blocking, all documentation/observability):

1. `reports/round-67/claims.json` contains **zero** words about lands ordering — `A_c`/`A_ca`/
   "per-claim"/"first commit"/"later commit" all appear 0 times; the file lists C's and Ca's
   `lands` arrays as overlapping file sets (`corpus/SOURCES.md` and `corpus/lessons/round-67.md`
   are in both), and the "note" only contemplates a third commit for `post-records.txt`. The
   ordering that makes the pair satisfiable therefore exists only in the wave conversation, not in
   a frozen artifact a closure reader can consult. Recommend one line in `claims.json` (or the
   round-67 lesson) naming the order A_r → A_c → A_ca and the lands commit ids at closure.
2. Claim C's statement says the registry "grows append-only … bounded to" that set; that sentence
   is true at A_c and false at lane tip (proven above). The receipt is honest (it records the
   stamped revision), but the *statement* should say "at lands A_c".
3. Closure reproducibility now requires three checkouts (A_r, A_c, A_ca); a reviewer who clones the
   tip and runs `accept-c.py --lands <tip>` gets FAIL by design. That is the intended cost of lands
   separation, but it should be stated where the receipts are read.

## 5. HIGH — Ca D4 is satisfiable without a single new rejected row (mined→rejected flip)

*L1 ruled no counter revision; this is recorded as residual instrument risk for closure, not as a
blocker. Re-confirmed against the current working-copy counters after the QUOTES capture-group fix
(`git diff reports/round-67/accept-ca.py` shows only that one-line change).*

`accept-ca.py` D4 requires `rej_opened_today >= len(R66_REJECTS) + 2` = 6 rows with
`status=rejected` **and** `opened=2026-10-24` (`accept-ca.py:66,235`). At base there are
**0** such rows; claim C's id budget let only 4 added rows into the pre-A_ca history (S801-S804),
and pins S805-S828 to `status=mined` (`accept-c.py:267`). Under the frozen pair and the A_c/A_ca
sequencing, the sequenced commits supply the 4 real rejects at A_ca, so D4 is satisfiable as ruled
— but it is equally satisfiable with no appended rejects at all:

Because `accept-c.py`'s `APPEND` mutability clause treats the status cell as in-place mutable for any
base row (`oc[:7] == nc[:7] and oc[8] == nc[8]`, `accept-c.py:368-369`), and base has **49** rows
opened 2026-10-24, all `mined`, all `used-by` live entries. Flipping two of them is undetected by
either counter. Proven on the same scratch lane (base tree, +S801-S804, +S750/S751 status
`mined`→`rejected`, teaches and used-by untouched):

```
$ python3 -B reports/round-67/accept-ca.py --root /tmp/r67shape --lands e5804323…
STAMP PASS stamped=e5804323 evaluated=e5804323 equal=True tree=4a459d69
D4    PASS bad=[] r66_rejects=4 opened_today=6

$ python3 -B reports/round-67/accept-c.py --root /tmp/r67shape --lands e5804323…
APPEND PASS missing_old=[] appended=4 extra=[] immutable_violations=[]
```

Note the arithmetic artefact in D4's own receipt: `opened_today=6` is reported while only 4 rows
were added — the two "new" rejects are reclassified live sources that remain cited by their
entries (`S750`'s used-by is still `…/games-play-sport-contests.md`). No leg requires a rejected
row's teaches cell to carry `REJECTED:`/`flip:` except for the four hard-coded `R66_REJECTS`
(`accept-ca.py:221-226`), and no leg requires a rejected row's used-by to be `—`.

Consequence for wave shape: the two reject seats are not the mechanism the counter measures. A
wave can be fully green with those seats' drafts dropped and two base rows silently retired from
coverage — the exact R66-D5 failure class (rejections that are not first-class rows) reproduced
under a green predicate. This is a shortcut class in the frozen instrument, not a seat-count
problem, but it is why the seat allocation mispredicts what is needed.

## 6. HIGH — the entry body has no author seat

`ScribeEntrySpec`: "Draft the claim-C entry design at …/stage/entry-spec.md (**not the entry
itself**)". The 12 row scouts produce 24 row fragments; no seat drafts
`corpus/knowledge/culture-material/medicine-healing-codes.md`, the ≤250-line artifact claim C's
`FILE`/`RESTATE`/`TOPIC`/`ONEID` legs are all measured on. The build seats therefore cover rows
and scaffolding, and the claim's primary deliverable falls to the L1 (already planner,
integrator, and sole committer). Mitigation: the 24 `BULLET=` lines arrive from the row scouts, so
the entry's bullets are pre-composed; what remains unassigned is the section prose, Boundaries and
lore-handoff sections. For a 64-seat wave this is a staffing gap, not padding: the single largest
build task is the one with no seat.

## 7. MEDIUM — four seats carry a dangling "same contract" reference

- `RevSourceSupport2/3/4`: "Same contract for S811-S816 / S817-S822 / S823-S828." The contract
  lives only in `RevSourceSupport1`'s prompt. After stripping S-ids the three prompts are
  token-identical to each other (Jaccard 1.0), and no prompt names `spec-v2.json`, so a leaf can
  recover the contract only by guessing to read `.ufo/waves/round-67/spec-v2.json`.
- `ScoutReject2`: "Same contract as ScoutReject1" (restates ids, status, teaches shape and
  evidence demands, so this one is survivable; the reviewers' three are not).

Per the delegation contract (children start blank; supply full slice requirements) three of the
20 reviewers launch under-specified. Counts as an item-quality defect, not padding.

## 8. MEDIUM — declared axes vs seat staffing

`spec.axes` = coverage, operability, calibration, depth, freshness, adjacency. Seat-axis pairs:

```
coverage 20 · calibration 43 · operability 8 · adjacency 3 · depth 1 · freshness 0
```

`freshness` is staffed by zero seats and `depth` only by `ScribeEntrySpec`. The two claim
predicates that would carry them (none — all three claims are coverage/operability/calibration)
do not exist, so this is a declaration mismatch rather than lost coverage; flagging because the
wave presents six axes.

## 9. LOW — registry cannot bind seat→item; padding audit is not mechanical

`w1/swarm-registry.json`: all 64 members have `"item": null` and `"agentId": null`. The registry
therefore records role/axes/milestone only; "seats without a concrete item" cannot be audited
from the registry and had to be reconstructed from prompts (done in §10). Bookkeeping gap, no
behavioral effect.

## 10. LOW — `SET` diagnostic mislabels missing ids as non-unique

`accept-c.py:250-253`: `dup = [sid for sid in NEW_IDS if len(reg_by_id.get(sid, [])) != 1]`
treats 0 occurrences as non-unique. Visible in the committed base dry run:

```
SET FAIL missing=['S805', … 'S828'] non-unique=['S805', … 'S828']
```

Cosmetic in behavior, but it is printed into a receipt a closure reader will parse.

## 11. Saturation is honest; padding audit — no seat is padding in the "no concrete item" sense

Item inventory the 64 seats draw on is real and roughly saturated: 24 row openings (12 scouts × 2 —
an exact fit to claim C's S805-S828), 4 reject candidates, ~8 stage artifacts (entry spec, gate rows,
lesson draft, readme row, quality criterion, R66 log entry, R66 scorecard, separability manifest),
3 frozen counters, 1 tool, 2 record files, and the r66 disposition set. The 20 reviewers map to ~19
distinct targets and the 12 critics to 12 distinct targets (claims JSON, per-counter pre-data
attacks, sizing, separability design, registry, frontier, D1 manifest, receipt discipline, medicine
scope, r66 dispositions) — no duplicated stance on the same artifact beyond the intended
writer/reviewer pair (`stage/entry-spec.md`) and the pre-data (critic) vs lands (reviewer) split on
each counter, which are different evaluation points, not copies. A 56% attack share over ~25
artifacts is heavy redundancy, which is defensible for a round whose two predecessors were rejected,
but it is redundancy, not new work.

Every one of the 64 prompts names a concrete artifact or id (`rows/<seat>/row-S8xx.txt`,
`w1/<seat>.md`, `stage/<file>`, a counter/tool path, or an explicit S-range). Verified
mechanically: 0 prompts lack an artifact noun or S-id; 0 scouts lack a row/gap target; 0
duplicate report paths; the only shared path is `stage/entry-spec.md` (ScribeEntrySpec writes,
RevEntrySpec reviews) — a write/review pair, not a collision. The row scouts are an exact fit:
12 × 2 = 24 = claim C's S805-S828. The defect in §§4-6 is *misaimed* work (ids the counter
forbids, an unstaffed deliverable), not idle seats.

Delivered-state snapshot at my last read (timing, not a shape defect): `rows/` held 24 fragments —
20 of the 24 mined ids (S807, S808, S827, S828 still absent, their seats `ScoutRow02`/`ScoutRow12`
had not reported) plus reject rows S829-S832; `stage/` held entry-spec, gate-rows, lesson-draft,
log-r66, quality-c19, scorecard-r66 and the separability manifest; `w1/` held 65 `.md` files
including seat variants and one `L1-kotodama-r67.ScribeEntrySpec.md`-named report, i.e. the
reject rows the §4 sequencing depends on are already on disk.

## Residual risk

- The scratch-lane proofs use the base tree plus registry edits only. `APPEND`, `D4` and `STAMP`
  are the legs under test and their results are deterministic on that tree; the other legs' FAIL
  lines in those runs are meaningless (no entry, no dispositions) and are not cited.
- §4's resolution rests on the L1's sequencing ruling, which is not yet in `claims.json`; if the
  rule is dropped before A_c is stamped (or a reader applies the single-commit reading), the C
  predicate fails with `extra=['S829'…]` exactly as shown.
- §5's flip shortcut stays live: at A_ca a lane could satisfy D4 with zero appended rejects. L1
  ruled no revision, so this remains a latent R66-D5 regression path for any later round that
  reuses `accept-ca.py`'s D4 shape.
- Whether `freshness` is expected to be staffed is not defined in the wave artifacts I could
  reach; no claim asserts it.

## Verification gaps

- §11 judges seat items plus a delivered-state snapshot; 4 mined row fragments and ~7 seat reports
  were still absent at my last read, so completeness of delivery is the L1's acceptance job
  (`RevIntegrity`/`RevEntrySpec` cover content).
- No `lsp` device is mounted in this seat (`xd://lsp` → "No such tool… Mounted devices: ast_edit,
  debug"), so no semantic diagnostics were available; all instrument claims above are from
  direct reads of `reports/round-67/accept-c.py` / `accept-ca.py` at the lane tip plus the
  executions shown. The files are Python counters, not a symbol graph — no better source exists.
- Tool installs: none. Nothing was upgraded or installed for this seat.

Report: .ufo/waves/round-67/w1/RevWaveShape.md
