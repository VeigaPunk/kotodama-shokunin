- Seat: R03 | reviewer | cross | date 2026-10-19 | baseline ce103bf

# R03 cross-claim review — register content vs the freeze read set, and timekeeping vs the recount surfaces

Scope: the two cross-claim questions this seat was assigned. (1) Would the pinned
r7 packet re-render if claim D's register-form content lands — i.e. is the
r7 freeze row load-bearing against the D build? (2) Do claim C's timekeeping
landing and claim Ca's recount ledger collide on the same counting surfaces?

Every reading below was taken at HEAD `ce103bf5885af00023cdc4a174c17602476cdcf8`
(`git status --porcelain` → `?? reports/round-36/` only; no tracked file modified).
All python ran with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.
No `reports/round-*/run-validation.py` was executed in-tree (F-C13-1); the two
mutation probes ran in a `git archive HEAD` copy under `.scratch/r36-R03/iso`,
which was removed after the readings.

## 1. The load-bearing question, answered: YES — a D4 component-tree edit reddens the r7 default chain

**The read set.** `tools/exercise-handoff-e2e.py:1939-1962` defines `V3_READ_SET`;
the frozen roster it is checked against is `reports/round-34/handoff/declared-in-r7/expected.json#inputs`
— **58 members** (`expected.json` key census; `run.log:9` prints
`read set: 58 files measured`).

The D4 component membership is fixed by the `D4_COMPONENTS` tuple at
`tools/exercise-handoff-e2e.py:157-170`: **`01-brief.yml` … `12-provenance.yml`**.
Measured against the frozen roster:

```
python3 -c "import json; d=json.load(open('reports/round-34/handoff/declared-in-r7/expected.json'))['inputs']; print(len(d)); print('13-register-law.yml' in d)"
→ 58
→ False
```

So the r7 row already pins **12 of the 13** delivered D4 components. Round 27's
`13-register-law.yml` is **not** a read-set member, and never entered the roster
between r27 and the r34 freeze.

**Live control (no mutation).** The default chain is green at HEAD:

```
python3 tools/exercise-handoff-e2e.py --profile v3 --quiet
→ exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27
  statuses=16/7/4 v2_subset=equal alias_leg=landed
  packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19
```

**Probe A — edit a read-set member (`04-lexicon.yml`).** One added comment byte:

```
exit=1
E2E-DIGEST: D4 component examples/culture-d4/components/04-lexicon.yml:
  the assembler recorded ed7093d6b921… but the bytes measure d4bca30ca2e3…
```

**Probe B — add a NEW component file (`14-register-forms.yml`, claim D's shape).**
`tools/assemble-culture-d4.py:214-224` walks `COMPONENTS.iterdir()` and only
requires `>= MINIMUM_COMPONENTS` (12), so a 14th file is accepted and merged;
the run printed `Wrote examples/culture-d4/packet.d4.yml (102837 bytes)`. The
default chain then failed:

```
exit=1
E2E-DIGEST: examples/culture-d4/typed-labels.d4.yml assembly.packet_sha256:
  the tree recorded aac91246cede… for examples/culture-d4/packet.d4.yml
  but the bytes measure e01cf9e85b5b…
```

**Probe C — edit ONLY `13-register-law.yml`, the one component that is *not* a
read-set member.** This is the sharpest probe: the edited file itself is outside
the roster, yet because the assembler re-reads the whole directory the packet
moves anyway:

```
python3 tools/assemble-culture-d4.py → Wrote examples/culture-d4/packet.d4.yml (101892 bytes)
python3 tools/exercise-handoff-e2e.py --profile v3 --quiet → exit=1
E2E-DIGEST: examples/culture-d4/typed-labels.d4.yml assembly.packet_sha256:
  the tree recorded aac91246cede… but the bytes measure ba2794d42e97…
```

**Reading.** Read-set membership is **not** the protection. `packet.d4.yml`,
`packet.d4.typed.yml`, `typed-labels.d4.yml` and `expected-holds.json` are all
members, and the assembler rebuilds the packet from the directory, so *any*
component-tree change — including one to a file the roster never names — reddens
the r7 row. The failure mode is `E2E-DIGEST` (fail-closed), **not** the
`E2E-READSET` superseded-row path at `tools/exercise-handoff-e2e.py:3830-3840`
(the roster only grows when `V3_READ_SET` itself is edited).

**Consequence for claim D.** Claim D's `after_required` says "every pin re-frozen
as a new row". That is necessary and correctly declared — but the frozen row in
question is `reports/round-34/handoff/declared-in-r7/`, which `REGIMEN.md`
position 4's round-36 `non_goals` and the seat boundary both forbid re-freezing
("no re-freeze of declared-in-r7 (freeze bytes stay pinned)", `reports/round-35/claims.json#non_goals`;
the r36 seat boundary restates it). The only conformant move is the r34 precedent
(`reports/round-34/handoff/repin.json#rows[R34-D-default-pointer]`): land a
**successor** row and re-point `V3_BASELINE_DEFAULT`/`V3_FROZEN_DIR_DEFAULT`
(`tools/exercise-handoff-e2e.py:1937-1938`), leaving the r7 bytes untouched.
If claim D instead leaves the default pointed at r7, the round's own
`python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` — which is a filed
r34-D counting command and part of the standing regression — goes red. **A D
landing without a re-point cascade cannot admit.**

## 2. Claim D's `before` state is stale: the register-form domain is NOT empty at HEAD

Claim D's `before` reads: *"the register class was a design forecast whose domain
is EMPTY in the delivered packet (r25 recorded 'the register-form domain in the
delivered D4 packet is EMPTY')"*. That sentence is quoted accurately from the r25
SCORECARD row (`SCORECARD.md:312`), but it was **superseded two rounds later**.

Measured at HEAD:

```
python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
→ coverage: examples/culture-d4/packet.d4.yml records=187 register_scoped=14
  derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0
→ exit=0
```

Lexicon record census of `examples/culture-d4/packet.d4.yml` (block split on
`^[a-z_]+:$`, records on `^  -$`):

| measure | count | ids |
|---|---|---|
| lexicon records | 62 | `L-01..L-62` |
| `register: "stamp"` | 8 | `L-55`…`L-62` |
| `derived_from` + `derivation` block | 8 | `L-55`…`L-62` |
| `construction: "STAMP-*"` | 8 | `L-55` `STAMP-LENGTHEN` ×6, `L-56`/`L-57` `STAMP-REVERSE` |

The closing record is `SCORECARD.md:329` (round 26, `register-stratum`): *"The
round-17 register forecast CLOSED: the `stamp` attestation register lands in the
delivered furnace-league tree — 8 verified register forms (tuum/kit/lom/nees/huum/mees/reek/saam) … derivation replay clean (8 derived pairs, 0 violations over 170 records)"*.
The r25 "empty domain" sentence was true at r25 and was deliberately left filed as
a superseded reading, not corrected (the lane's append-only rule). It is **not**
a description of HEAD.

**Consequence.** Claim D as declared re-runs legs over a domain that is already
populated and re-pins bytes that already carry the forms. Before any content is
authored, the claim must be re-stated against a measured before-state. Two live
residues survive from the r25/r26 records and *are* real work: `head2` is declared
but unused (`examples/culture-d4/packet.d4.yml:278-281`, "over the delivered tree
it is an identity, not a derivation"), and the RL-3 ceiling (the five legal
abstractions refuse reverse — `SCORECARD.md:345,352`). Those, not an empty
domain, are the honest D target.

## 3. The re-freeze list claim D would owe (pin census)

Every filed/live surface holding a live D4 digest, by `grep -rl <digest>` over the
repo (excluding `.git`, `.scratch`):

| surface | live sha256 | files holding the digest |
|---|---|---|
| `examples/culture-d4/packet.d4.yml` | `aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3` | **44** |
| `examples/culture-d4/typed-labels.d4.yml` | `c23b0ab532cfb9d4bb403405c6996982a447098048e08facbbc9f341ea13f82e` | **29** |
| `examples/culture-d4/components/04-lexicon.yml` | `ed7093d6b92111c2300e7c04b9100f9e57f6d5802101b69335f9fe138858755d` | **21** |
| `examples/culture-d4/expected-holds.json` | `e6ae9828d6c82aa6e14431a02840ad565f9f7c30a660afcbed1b1079166bfba3` | **20** |
| `examples/culture-d4/packet.d4.typed.yml` | `d581e0ad5384ce56622839b6ae4d6cf8b5a4447300cf7d8cd295f3efea0c9182` | **19** |

Named live pin channels among them (each needs a new row, never an in-place edit):

- `tools/gates/typed-pipelines.json` profile `d4` (generation `round-30-qreg-records`) pins
  packet + assembler + projection + adapter + expected. The file's own `note` states the
  discipline: *"a stale pin refuses (exit 2, L1-profile) until it is re-pinned with a command
  and a date"* — so this is a **hard refusal**, not a warning.
- `tools/gates/expected/register-law-gate/r30-post/` (`expected.json`, `packet.d4.yml`, `inputs/`).
- `reports/round-31/sweep/frozen/r31-post/MANIFEST.tsv` + `inputs/`.
- `reports/round-30/handoff/declared-in-r6/expected.json` (the superseded row — replays red by design).
- `reports/round-34/handoff/declared-in-r7/{expected.json,packet.md,twin.json}` (the live default).

Live gate state at HEAD, all green (these are the legs claim D must keep green
through the change, not just re-pin):

```
python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml   → summary: 20/20 legs passed, exit 0
python3 tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml    → law_rows=5 identity_rows=8 record_ids=183 registers=17 dangling=0 findings=0, exit 0
python3 tools/gates/d4-assembly-check-gate.py examples/culture-d4/packet.d4.yml    → byte-identical deterministic assembly, exit 0
python3 tools/gates/d4-typed-labels-check-gate.py examples/culture-d4/typed-labels.d4.yml → byte-identical deterministic projection, exit 0
```

Note the asymmetry that makes this cascade unavoidable rather than optional:
`d4-assembly-check-gate.py` and `register-law-gate.py` are *live* gates over the
live packet (they go red the moment the packet moves and the assembled bytes stop
matching), while the `expected/` directories under them are *filed* baselines that
must not be rewritten — the r27 `d4-pins.json` precedent (`"kind": "re-pin as a NEW
row; every filed row stays byte-identical"`) is the shape to follow.

## 4. Timekeeping vs the recount surfaces — the collision is real but benign

Claim C lands one corpus entry and bumps `corpus/README.md` to rev 2.1
(212 rows). Claim Ca re-runs the r33-35 counting commands. Both touch the same
counting surface, so the ledger's "observed" side is round-order dependent.

Live state measured this round (the "before" of claim C, confirming its numbers):

```
for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done
→ 21 23 24 29 20 94   (total 211)
python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge → totals.files = 211
python3 -B reports/round-28/readme/sweep.py → exit 0; parts {civilizations 94, culture-material 24, linguistics 21, myth-symbol 23, synthesis 29, verification 20};
  rows 211 files 211; missing_from_index 0; orphan_rows 0; header_drift {}; totals_line 211 totals_ok True;
  footer_ok True; readme_sha256 51b966af20483328c3e221d2ab0f766aa5cf0f5a0b140650b95eb841d6bea6f0
```

`corpus/README.md` is at **revision 2.0** (`corpus/README.md:3`, the round-35
landing), whose own note carries the rule the r36 C landing must obey:
*"a later landing needs a new row, a bumped section header, a bumped totals line,
and its own revision block, never an edit of this one"* (`corpus/README.md:73-75`).
So claim C's declared rev 2.1 / 212 rows / footer vector is the right shape; the
footer vector claim C declares (`21/23/25/29/20/94`) is the correct successor of
the live `21/23/24/29/20/94`.

**The collision.** The r35 filed counting command
(`for p in …; do ls corpus/knowledge/$p/*.md | wc -l; done`) and
`reports/round-28/readme/sweep.py` are *both* enumerated by claim Ca and *both*
moved by claim C. If Ca records "observed" before C lands, the ledger shows 211;
after C lands it shows 212. Neither number is wrong, but a ledger that does not
stamp **which revision each observation was taken at** will read as a mismatch.
Ca's ledger draft should therefore carry a per-row `observed_at_revision` (or an
explicit ordering statement) rather than a bare observed value. This is a drafting
requirement, not a defect — and it is the same class the r29 recount already
handled ("revision boundaries documented 175/183", `SCORECARD.md:382`).

## 5. Recount of the r33-35 filed counting commands (this seat's own verification)

Re-run at HEAD `ce103bf`. `reports/round-{33,34,35}/run-validation.py` rows are
**not** re-executed in-tree (F-C13-1) and are dispositioned
`could-not-reproduce-in-tree` below.

| round | claim | command | filed result | observed 2026-10-19 | disposition |
|---|---|---|---|---|---|
| 33 | O | `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` | exit 0, 0 findings, 33 rows == 33 files | exit 0, `findings: 0`, `PASS C34_pins_rederived / C34c_shape_cells_rederived / C34b_prose_arithmetic` | match |
| 33 | O | `… c31-lessons-index-audit.py --selftest` | green | `SELFTEST OK: 28/28 checks passed`, exit 0 | match |
| 33 | O | `test -s reports/round-33/op/O05-falsifier-disposition.md` | landed | present | match |
| 33 | C | `python3 reports/round-33/run-validation.py` | exit 0 | — | could-not-reproduce-in-tree (filed runner, F-C13-1) |
| 33 | A | `python3 reports/round-33/run-validation.py` | exit 0 | — | could-not-reproduce-in-tree |
| 34 | D | `python3 tools/gates/handoff-packet-check.py reports/round-34/handoff/declared-in-r7/packet.md` | exit 0 | `INFO scan: fields=16/16 glossary-entries=20 findings=0`, exit 0 | match |
| 34 | D | `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` | exit 0, packet `45f57132…` | exit 0, packet `45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19` | match |
| 34 | D | `python3 reports/round-34/run-validation.py` | exit 0 | — | could-not-reproduce-in-tree |
| 34 | O | `python3 tools/harness/receipt_guard_adoption.py --selftest` | green | `"selftest_passed": true`, exit 0 | match |
| 34 | O | `python3 tools/harness/receipt_guard_adoption.py --json` | inventory | — | not re-run (writes no receipt; class counts already filed: `guarded-refresh 18 / unguarded-in-place 11` in `reports/round-34/validation.json`) |
| 34 | O | `python3 reports/round-34/run-validation.py` | exit 0 | — | could-not-reproduce-in-tree |
| 34 | C | `python3 -B reports/round-30/craft/box1-survey.py` | 28/28 at `f9bd07c2…` | `"resolvable": 28`, `unnamed_in_skill: []`, `skill_sha256 f9bd07c2bd13462367be20e8d775cec1c5569eb2e575dc5d078519ecc72e5a9b`, exit 0 | match |
| 34 | C | `python3 reports/round-34/run-validation.py` | exit 0 | — | could-not-reproduce-in-tree |
| 35 | C | partition census | 21/23/24/29/20/94 | 21/23/24/29/20/94 (total 211) | match |
| 35 | C | `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` | total 211 | `totals.files 211`, `read_only True`, `deterministic True` | match |
| 35 | C | `python3 reports/round-35/run-validation.py` | exit 0 | — | could-not-reproduce-in-tree |
| 35 | O | `python3 -B tools/exercise-handoff-e2e.py --selftest` | green | exit 0, controls incl. `tamper read-set: exit 1 E2E-DIGEST naming the changed file`, `tamper scan expectation: exit 2 E2E-BASELINE`, `missing artifact: exit 2 E2E-ARTIFACT` | match |
| 35 | O | `… --profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json` | exit 1, **named diagnostic** | exit 1, `E2E-READSET: 1 read-set member(s) named by the frozen baseline are not in the live read set: reports/round-20/handoff/claims-map.md — the baseline row is superseded (re-point or re-freeze it)` | match — the r35 R34-N1 hardening holds; the r34 `KeyError` is gone |
| 35 | O | `python3 reports/round-35/run-validation.py` | exit 0 | — | could-not-reproduce-in-tree |
| 35 | A | `python3 reports/round-35/run-validation.py` | exit 0 | — | could-not-reproduce-in-tree |

Plus one command claim Ca does not enumerate but which the standing regression
depends on and which claim D threatens (see §1):

| — | — | `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` (default, r7) | exit 0 | exit 0, packet `45f57132…` | match **at HEAD**; breaks on any D4 component-tree edit |

Count: **11** filed commands reproduced match, **7** `run-validation.py` rows
`could-not-reproduce-in-tree` (owner: R03, reason: F-C13-1 forbids in-tree
execution of filed runners; the durable receipts are each round's own
`validation.json`), **1** not re-run with reason. No mismatch found.

## 6. Trades (for X01) and harms

- **Register content vs freeze integrity.** Landing claim D buys depth (the
  register class is a real capability) at the cost of a ~44-holder pin cascade and
  one renderer re-point. The trade is *not* neutral and must be reported, not
  averaged: the cascade is the price of the depth, and the r34 precedent says the
  price is payable as new rows. Declaring the depth improvement without the
  cascade would harm operability (`typed-pipelines.json` profile `d4` refuses,
  exit 2 L1-profile) — that is a **harm**, not a trade.
- **Timekeeping entry vs corpus breadth.** Claim C's +1 entry moves 211 → 212 on
  four counting surfaces (`corpus/README.md`, the census, the inventory, the
  sweep). It buys coverage and costs nothing measurable; the only exposure is the
  Ca ledger ordering issue in §4.
- **No axis is harmed by either claim as *declared*** — provided claim D is
  restated against the measured before-state (§2) and carries the re-point cascade
  (§1). As currently worded, claim D's `before` is unverifiable-at-HEAD (it
  asserts an emptiness that does not exist), and its `after_required` names
  "every pin re-frozen as a new row" without naming the renderer default move the
  r34 precedent shows is required.

## 7. Verdicts

| question | verdict |
|---|---|
| Would the r7 packet re-render if D lands? | **Yes.** `E2E-DIGEST` via `packet.d4.yml` membership; a successor row + renderer re-point is mandatory (r34 precedent). Probe C shows even a non-member component edit moves it. |
| Is claim D's declared before-state accurate at HEAD? | **No.** The register-form domain is non-empty: 8 stamp forms, argot gate `derived_pairs=8 violations=0`. The r25 sentence was superseded by r26. |
| Do claim C and claim Ca collide? | **Yes, benignly.** Both move the 211→212 census/README surfaces; Ca's ledger needs a per-row revision stamp. |
| Do the r33-35 filed counting commands reproduce? | **11/11 non-runner commands match; 7 runner commands `could-not-reproduce-in-tree`** with owner + reason; no mismatch. |
| Any axis harmed by the claims as declared? | None as declared for C/Ca. **D as worded would harm operability** (stale before-state + missing re-point), so it must be restated before landing. |

## Owed

- **`reports/round-36/review/R03-cross-review.md` is this file** — the only path this seat writes.
- The re-point/re-freeze *drafts* for the successor row (the new `expected.json`,
  `freeze.txt`, `packet.md`, `twin.json`, and the `V3_BASELINE_DEFAULT` edit) are
  owed by the D executors (D04 `depth/D04-repin.md`); this review names the list
  and the 5 digest families, not the replacement bytes.
- `reports/round-{33,34,35}/run-validation.py` remain `could-not-reproduce-in-tree`;
  no in-tree execution was attempted and none should be (F-C13-1).
- The `receipt_guard_adoption.py --json` inventory was not re-run this seat; its
  filed class counts (`guarded-refresh 18 / unguarded-in-place 11`,
  `reports/round-34/validation.json#claims.O.measurement`) stand as the filed reading.
- `to-verify`: whether the round-36 integrator intends the successor row to be
  `reports/round-36/handoff/declared-in-r8/` (the naming pattern implies r8) or a
  `reports/round-36/pinsweep/v3-baseline-r36/` row (the r27/r28 pattern). Both
  precedents exist in-tree; the choice is the integrator's, and either satisfies
  the append-only rule.

## Citations

Commands (all run 2026-10-19 at HEAD `ce103bf5885af00023cdc4a174c17602476cdcf8`,
cwd = lane root, `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):

```
git rev-parse HEAD; git status --porcelain
python3 -c "import json; d=json.load(open('reports/round-34/handoff/declared-in-r7/expected.json'))['inputs']; print(len(d)); print('examples/culture-d4/components/13-register-law.yml' in d)"
python3 tools/exercise-handoff-e2e.py --profile v3 --quiet
python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml
python3 tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml
python3 tools/gates/d4-assembly-check-gate.py examples/culture-d4/packet.d4.yml
python3 tools/gates/d4-typed-labels-check-gate.py examples/culture-d4/typed-labels.d4.yml
sha256sum examples/culture-d4/packet.d4.yml examples/culture-d4/components/04-lexicon.yml examples/culture-d4/components/13-register-law.yml examples/culture-d4/expected-holds.json examples/culture-d4/packet.d4.typed.yml examples/culture-d4/typed-labels.d4.yml
for d in <the five live digests>; do grep -rl "$d" --exclude-dir=.git --exclude-dir=.scratch . | wc -l; done
for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done
python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge
python3 -B reports/round-28/readme/sweep.py
python3 -B reports/round-25/audit/c31-lessons-index-audit.py ; python3 -B reports/round-25/audit/c31-lessons-index-audit.py --selftest
test -s reports/round-33/op/O05-falsifier-disposition.md
python3 tools/gates/handoff-packet-check.py reports/round-34/handoff/declared-in-r7/packet.md
python3 -B tools/harness/receipt_guard_adoption.py --selftest
python3 -B reports/round-30/craft/box1-survey.py
python3 -B tools/exercise-handoff-e2e.py --selftest
python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json
# isolated probes (git archive copy under .scratch/r36-R03/iso, removed after)
git archive HEAD | tar -x -C .scratch/r36-R03/iso
#   probe A: append a comment byte to examples/culture-d4/components/04-lexicon.yml
#   probe B: cp components/13-register-law.yml components/14-register-forms.yml
#   probe C: append a comment byte to examples/culture-d4/components/13-register-law.yml
#   each followed by: python3 tools/assemble-culture-d4.py ; python3 tools/exercise-handoff-e2e.py --profile v3 --quiet
```

File:line:

- `tools/exercise-handoff-e2e.py:1937-1938` — `V3_BASELINE_DEFAULT` / `V3_FROZEN_DIR_DEFAULT` → `reports/round-34/handoff/declared-in-r7`.
- `tools/exercise-handoff-e2e.py:1939-1962` — `V3_READ_SET` (58 members).
- `tools/exercise-handoff-e2e.py:157-170` — `D4_COMPONENTS` (12 files; `13-register-law.yml` absent).
- `tools/exercise-handoff-e2e.py:3830-3840` — the `E2E-READSET` superseded-row path.
- `tools/exercise-handoff-e2e.py:2208-2240` — `v3_verify_component_digests` / `v3_verify_d4_pins` (the `E2E-DIGEST` legs).
- `tools/assemble-culture-d4.py:214-224` — `component_files()`: directory walk, `>= MINIMUM_COMPONENTS` (12).
- `tools/assemble-culture-d4.py:64` — `MINIMUM_COMPONENTS = 12`.
- `tools/gates/typed-pipelines.json` — profile `d4`, `generation: round-30-qreg-records`, pins packet `aac91246…` / expected `e6ae9828…`; `note` states the stale-pin refusal (exit 2, L1-profile).
- `examples/culture-d4/packet.d4.yml:278-281` — `head2` declared but unused ("an identity, not a derivation").
- `examples/culture-d4/packet.d4.yml:1329-1431` — the `registers` block `QREG-01..QREG-08`.
- `examples/culture-d4/packet.d4.yml:1020,1042,1064,1086,1108,1130,1152,1174` — the eight `derived_from:` lines of the stamp forms `L-55..L-62` (each record also carries `derivation:` with `op:`/`base:`, `doublet_of:`, `register: "stamp"`, `construction: "STAMP-*"`; `grep -n 'derived_from\|doublet_of\|head2' examples/culture-d4/packet.d4.yml`).
- `SCORECARD.md:312` — the r25 "EMPTY" sentence (superseded reading).
- `SCORECARD.md:329` — the r26 `register-stratum` landing that closed it (8 forms, 0 violations over 170 records).
- `SCORECARD.md:345,352` — the r27 register law + the RL-3 ceiling.
- `SCORECARD.md:382` — the r29 recount's revision-boundary discipline (175/183).
- `SCORECARD.md:628-655` — the r35 admitted row (201 → 211; README rev 2.0 sweep-green).
- `corpus/README.md:3` — revision 2.0; `:73-75` — the "later landing needs a new row … never an edit of this one" rule.
- `reports/round-34/handoff/repin.json#rows[R34-D-default-pointer]` — the re-point-as-new-row precedent and its control.
- `reports/round-27/pinsweep/d4-pins.json` — the earlier cascade: "kind: re-pin as a NEW row; every filed row stays byte-identical".
- `reports/round-34/handoff/declared-in-r7/run.log:7,9` — packet `45f57132…`; `read set: 58 files measured; component digests 26/26 matched; d4 tree pins 8/8`.
- `reports/round-36/claims.json` — claims D/C/Ca and their `before`/`after_required`.
- `reports/round-35/claims.json#non_goals` — "no re-freeze of declared-in-r7 (freeze bytes stay pinned)".
- `reports/round-34/validation.json#claims.O.measurement` — `guarded-refresh 18 / unguarded-in-place 11`.
