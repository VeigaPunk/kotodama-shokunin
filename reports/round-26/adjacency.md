# Round 26 — Adjacency / connector (SCRIBE X61)

- **Date:** 2026-10-18. Every timestamp below is UTC from this seat's own runs.
  Command batches are anchored by `date -u` at **18:00:58Z**, **18:01:21Z**,
  **18:01:40Z**, **18:01:54Z**, **18:02:17Z**, **18:03:52Z**, **18:09:21Z** and
  **18:09:57Z**; observations between anchors were taken inside those windows
  (bounded, not individually stamped).
- **Axes:** adjacency (boundary invariants) + connector-surface evidence for the
  three declared claims — O (the round-25 remainders), D (the register stratum
  and the round-17 forecast closure), C (the open-question queue) — on the
  surfaces this fragment watches. Read-only cross-checks only; the claims' owners
  land the product.
- **Write scope:** only this fragment. No source fixes, no packet/validator/pin/
  gate edits, no shared bookkeeping, no historical validator run, no Git
  mutation, no commit/push, no sibling writes. `export TMPDIR=$PWD/.scratch` was
  set before every scratch-writing command; scratch lived under `.scratch/x61/`
  (gitignored, lane-internal). No filed rounds 8–25 byte was written by this
  seat.
- **Baseline binding:** declared baseline
  `fc13cd27b9e78d5d7c4f70740fd26c9383a7447b` (`reports/round-26/claims.json:5`);
  observed lane HEAD `1ad491a1a4b0aef9ebdc1861dfb8237727503825`;
  `git merge-base --is-ancestor fc13cd27… HEAD` → success (18:00:58Z).

## Verdict (scoped to this seat's observations)

**Adjacency: clean on the filed-round surface.** All **1,225** tracked filed paths
under `reports/round-{8..25}` are blob-identical to the declared baseline; the
`baseline..HEAD` diff over that surface is empty; `PROVINCE.md` and the handoff
interface contract are byte-unmoved across baseline/HEAD/worktree; `examples/`
and `tools/` carry no committed delta baseline→HEAD.

**Connector state: the two named round-25 tails now have round-26 successor rows
on disk, and this seat found a third connector failure neither round 25 nor round
26 has recorded.** (a) The r4 twin gap **stands** — `declared-in-r4/` still holds
`packet.md` + `expected.json` + `freeze.txt` only. (b) Both sibling pin tails
**reproduce unfixed on the filed round-20 bytes** and now carry round-26 re-point
rows. (c) **New:** the round-25 `declared-in-r4` successor checker reads **51/52**
over a HEAD clone, not the 52/52 its own filed receipt recorded — the round-25
`L3b-argot` leg moved the D4 gate from the 19/19 the frozen round-20 runner
hardcodes to 20/20, and that failure is *not* in the checker's declared-tail
allowance. Mechanism isolated with a two-sided A/B control (§5).

**The round-26 counting command does not exist at this seat's stamp**, so all
three claim counts are `to-verify` until its owner lands
`reports/round-26/validation.json`. Nothing here substitutes for it.

## 1. Boundary observations

Batch at **18:00:58Z**, from the lane root:

- `git ls-files reports/round-{8..25} | wc -l` → **1,225** tracked filed paths.
  Per-round at baseline: r8 153, r9 87, r10 73, r11 252, r12 44, r13 2, r14 40,
  r15 20, r16 23, r17 67, r18 60, r19 71, r20 81, r21 45, r22 77, r23 43, r24 20,
  r25 67.
- `git status --porcelain=v1 --untracked-files=all -- reports/round-{8..25}` →
  empty, at every sample (18:00:58Z, 18:01:54Z, 18:09:21Z, 18:09:57Z).
  `git diff --name-status fc13cd2 HEAD -- reports/round-{8..25}` → empty. The
  declaration commit added only `reports/round-26/{claims,targets}.json`, so no
  filed path changed at commit level baseline→HEAD.
- **Detector control (per-path blob comparison), 18:01:54Z:** a read-only
  `python3 -` pass walked all **1,225** baseline tree entries
  (`git ls-tree -r -z <baseline> -- reports/round-{8..25}`) and compared each
  working file's `git hash-object` to its baseline blob → **0 mismatches, 0
  missing**. True-positive control: `git rev-parse <baseline>:reports/round-25/validation.json`
  equalled the live blob (**True**); hashing the same bytes with an appended
  in-memory probe produced a differing SHA-1 (**True**); the file re-read
  unchanged afterwards (**True**). The detector demonstrably reports a deviation,
  so the 1,225 clean paths are a positive observation, not a blind pass.
- **PROVINCE accuracy:** `git rev-parse <baseline>:PROVINCE.md`,
  `git rev-parse HEAD:PROVINCE.md` and `git hash-object PROVINCE.md` all return
  `313b182f251564b7997b06996b4f063370778f11` (18:00:58Z). Read against the live
  tree its boundary statements hold: own-repo write scope; the refuses list
  matches the sibling lanes that exist (`lore-shokunin`, `chousa-shokunin`,
  `kake-shokunin`, `kotoba-shokunin`, `game-dev-2d-shokunin`,
  `game-dev-3d-shokunin` all present, 18:09:21Z); the adjacent-contract path
  exists and is digest-stable below. No correction drafted.
- **Committed source surface unmoved:** `git status --porcelain=v1 -uall --
  examples tools` → empty at 18:01:54Z and 18:09:21Z. Spot blobs equal at
  baseline/HEAD/worktree: `examples/culture-d4/packet.d4.yml`
  `3f6f15be4add885110d134d70ddb0453ff22a329`;
  `tools/gates/typed-pipeline-gate.py` `262775fa495f5ff341dc4bfe11079079ba5b122f`
  (sha256 `b749ad07cf1710279aea557c071587cf4b3a228a9fb4d03398b4b94d2f32ad85`);
  `tools/gates/argot-derivation-gate.py` `93b9f0ff14ccdf32e5a87bbd88d8e2e8e73ad2ed`
  (sha256 `5b5abe7865ed906c23fba87fd0dae8b6187c8dfc1a80137adbd364d4d88b0211`).
- **Fleet root:** `git -C /home/vgpnk/Projects/shokunin status --porcelain=v1
  --untracked-files=all` returns exactly **ten** rows, all `?? .scratch/*.out`
  (`battery`, `coupling`, `craft`, `d2check`, `d3check`, `replay-r22`,
  `replay-r3`, `rv5-p`, `rv6-p`, `rv7-p`) — the same ten the round-25 watch
  disclosed, still present and unmodified. This seat corroborates the round-26
  scope watch (X57) and the round-25 watch (X43): the fleet root is **NOT
  CLEAN**, the debris predates this round's dispatch, and it is not a kotodama
  filed artifact. Disclosed, not dispositioned.

## 2. Connector invariants (interface + envelopes)

- **Handoff interface contract unmoved:** `git rev-parse` at baseline and HEAD
  plus `git hash-object` on the worktree all give blob
  `66987ff3ef921bffe6d497608b2bc049f3b5ed9e` for
  `corpus/knowledge/synthesis/worldbible-integration-contract.md` (18:00:58Z);
  its SHA-256 is
  `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069` — the same
  digest the v2 baseline read set pins and the r26 v3 row re-pins (§4). No
  contract drift across the boundary. The L0 contract-digest ratification
  question remains open and escalated — not absorbed here.
- **Structural envelope green on the newest v3 revisions:**
  `python3 tools/gates/handoff-packet-check.py
  reports/round-23/wording/declared-in-r3/packet.md` → exit **0**,
  `fields=16/16 glossary-entries=20 findings=0`; the same over
  `reports/round-25/v3-supersession/declared-in-r4/packet.md` → exit **0**,
  identical counts (18:01:40Z batch). The envelope passes on both revisions —
  which is precisely why it is **not** semantic integration evidence (the round-12
  contract audit's asymmetry, `reports/round-12/adjacency/contract.md:9-10,23`).
- **Live D4 gate green:** `python3 tools/gates/typed-pipeline-gate.py
  examples/culture-d4/packet.d4.yml` → exit **0**, **20/20** legs, including
  `ok L3b-argot`; the flagless D2 default → exit **0**, **16/16**; the D2 source
  entry → exit **0**, **16/16**; the D2 typed entry → exit **0**, **13/13**; the
  D4 typed entry → exit **0**, **17/17** (18:03:52Z batch, TMPDIR set).
- **Register-verdict independence:** `python3 tools/gates/argot-derivation-gate.py
  examples/culture-d4/packet.d4.yml` → exit **0**,
  `records=156 register_scoped=6 derived_pairs=0 claimed_chains=8 borrow_pairs=6
  violations=0 rule_holds=0`; `--selftest` → exit **0**, `21/21 checks passed`
  (18:01:40Z, re-confirmed 18:09:57Z). The leg is green over an **empty
  derivation domain** — the round-25 finding, unchanged (§3).
- **Gate bytes are the live bytes:** the D4 gate's sha256 `b749ad07…` is the
  digest the round-26 gate-input freeze binds
  (`tools/gates/frozen/round-26/gate-input/freeze-receipt.json`, 18:08:08Z). So
  §5 is a defect on the **live pinned tool**, not a drifted working copy.

## 3. Claim D connector — the register stratum is still not on disk

Measured 18:01:40Z, 18:02:17Z, 18:09:21Z and 18:09:57Z:

- **The delivered packet carries no derivation relation.** `grep -n
  "derived_from\|derivation:\|head2\|reverse" examples/culture-d4/packet.d4.yml
  examples/culture-d4/packet.d4.typed.yml` → **0 matches** in both. `grep` for
  `form_slots\|slot_ref\|doublet_of` finds only the brief's prose rule line
  (`packet.d4.yml:108`) and the D2-shaped `form_slots:` block (`:2124`).
- **The argot gate's own coverage line agrees:** `register_scoped=6`,
  `derived_pairs=0`. The six register-scoped records are the symbol/contact/layer
  rows the gate counts via `record_register` (`tools/gates/argot-derivation-gate.py:293`),
  not register-scoped *forms*.
- **No committed or working change to the example tree:** `git diff --stat
  fc13cd2 HEAD -- examples tools` → empty; `git status -uall -- examples/culture-d4`
  → empty. `examples/culture-d4/{packet.d4.yml,packet.d4.typed.yml,typed-labels.d4.yml,expected-holds.json}`
  all carry 06:44–11:50 local mtimes, i.e. pre-round-26.
- **The `D4L-REGISTER-UNRESOLVED` class has no engine path:** it appears in
  `examples/` and `tools/` in **0** files (round-25 §2 recorded the same).

**Convergence, stated as convergence.** This seat's reading was taken before
reading the round-26 D fragments and agrees with all four of them:
`reports/round-26/argot/D24-forecast-closure.md` states the formal closure
condition is *delta zero* and measures it **not** met — "the *checking leg* is
delivered … but the *relation* is not", with `derived_pairs=0`;
`reports/round-26/register/review.md` (D04) records the leg green and the
stratum's two legs unimplemented; `reports/round-26/argot/D21-adversarial-replay.md`
and `D22-label-typing-crosscheck.md` attack the checking surface because the
stratum itself is absent. The round-25 forecast's Δ3 domain is therefore still
empty at this observation, and the honest closure is **"delta named"**, not
"delivered". The D-claim verdict is the runner's and the parent's, not this
seat's.

## 4. Claim O connector — the three round-25 remainders, measured

### 4a. The r4 twin gap — **stands**

| revision | `packet.md` | `expected.json` | `freeze.txt` | `twin.json` |
|---|---|---|---|---|
| `reports/round-20/handoff` | yes | yes | yes | **yes** |
| `reports/round-22/handoff/declared-in` | yes | yes | yes | **yes** |
| `reports/round-22/handoff/declared-in-r2` | yes | yes | yes | **yes** |
| `reports/round-23/wording/declared-in-r3` | yes | yes | yes | **no** |
| `reports/round-25/v3-supersession/declared-in-r4` | yes | yes | yes | **no** |

`ls reports/round-25/v3-supersession/declared-in-r4/twin.json` → *No such file or
directory* (18:01:21Z). `find reports tools -name "twin.json"` → exactly three
files, all round-20/round-22. So the round-25 X48 remainder is unchanged: the
newest two revisions land packet-only. The r26 v3 re-point row does land the full
five-file set including a twin (§4c), which is the **shape** the gap names — but
that is a different row on a different revision, and this seat neither claims it
closes the r4 gap nor reads the round-26 O seat's own "different tail, not
claimed" note (`reports/round-26/remainders/pins.md` §4) as a disposition here.

### 4b. The two sibling pin tails — **reproduce, unfixed on the filed bytes**

Both round-25 remainders are still live on the **filed round-20** surfaces at
18:01:21Z, each with its own control:

| tail | surface | stale value | live value | verdict |
|---|---|---|---|---|
| A (v2 successor) | `reports/round-20/wart/expected-v2-07-r20.json` `inputs["tools/d2-typed-labels.py"]` | `76536a924280ad4187e2abeec1977b92861656a30d2dc7428f1f09087df8edfb` | `2819f68769dfc0b57f46cdaeb4c9a96324c5711c46348f5a8308382dfd7053c3` | **stale** |
| B (v3 baseline) | `reports/round-20/handoff/expected.json` `packet_sha256` | `e92f5e6775b657c24fa6260e340e4e7a04cf6c3777188cba80678bed079ae43b` | `a97a0f0a0a497cb4410124607065df7686bbc7f78b4b46bdaaaa1d66ba4d1b6e` | **stale** |

**Control that keeps tail A honest:** the same pin file's entry for
`corpus/knowledge/synthesis/worldbible-integration-contract.md`
(`5f4c02bf…`) **does** equal the live bytes (**True**), so the mismatch is a real
stale pin, not a broken comparison. Tail B is confirmed by the frozen round-20
runner itself, which reports it as a failure (§5's receipt).

**Round-26 successor rows exist** (observed 18:09:21Z):
`reports/round-26/remainders/v2-successor-r26/expected.json`
(sha256 `f695b910699ab5310b0853fe38471b7714616973f7deff366e1298888b766bc3`, pin
`2819f687…`; `baseline_digest 803ec02f…`) and
`reports/round-26/remainders/v3-baseline-r26/` (`packet.md` sha256
`a97a0f0a…`, `twin.json` sha256 `d3de56a8…`, plus `expected.json`, `freeze.txt`,
`run.log`). Running the declared checker
`python3 reports/round-26/remainders/pin-repoint-check.py --check` → **exit 0**,
**17/17** controls, including the red arms (`control-stale-v2-row-replays-red`
exit 2 `V2F-DIGEST: 1 pinned file(s) changed since the freeze:
tools/d2-typed-labels.py`; `control-stale-v3-row-replays-red` exit 1
`E2E-DIGEST: 4 read-set file(s) changed`) and the green arms (new rows exit 0).
This seat reproduces the checker's verdict; it does **not** certify the
disposition, which is the O seats' and the parent's. The filed round-20 bytes are
byte-identical to baseline — the re-point is a new row, as the lane's rules
require.

### 4c. The r4 successor checker — **51/52 at HEAD, a third connector failure**

`python3 reports/round-25/v3-supersession/v3-supersession-check.py --root
.scratch/x61/clone --check` (HEAD clone, 18:04:00Z receipt) →

```
passed False   passed_controls 51 / 52
positive failures:
  claim D: v2 successor row not green: reports/round-20/wart/expected-v2-07-r20.json exit 2 —
    V2F-DIGEST: 1 pinned file(s) changed since the freeze: tools/d2-typed-labels.py
  claim D: v3 baseline reports/round-20/handoff/expected.json pins packet e92f5e6775b6…
    but the run assembled a97a0f0a0a49…
  claim O: D4 gate legs summary: 20/20 legs passed != 19/19
```

The failing control is
`positive-control-remaining-failures-are-inherited-open-tails-only`, whose
`undeclared_failures` is exactly `["claim O: D4 gate legs summary: 20/20 legs
passed != 19/19"]` (`reports/round-25/v3-supersession/v3-supersession-check.py:509-516`).
The checker's allowance list covers only the two round-23 tails
(`OPEN_TAIL_V2_ROW`, `OPEN_TAIL_V3_PIN`, `CLAIM_D_LEGACY_V3_PIN`, `:105-108`) — the
leg-count delta is **not** declared, so the third failure is undeclared, not
inherited.

**Mechanism, with controls (see §5).** The frozen round-20 runner the checker
binds hardcodes `D4 gate legs {gate_scan.group(0)} != 19/19`
(`reports/round-20/run-validation.py:1119`). Round 25 added the `L3b-argot` leg to
`tools/gates/typed-pipeline-gate.py`, moving that gate from **19/19** to
**20/20** on the same D4 input.

**Why round 25 did not see it.** The filed X48 receipt
`.scratch/r25-x48/r4-check.json` records `passed True, passed_controls 52/52` at
**2026-10-18T17:39:17Z** — over a clone created **14:35:18 local**, i.e. before
the round-25 integration commit at **14:58:37 local**. That clone's gate is
`04ad4bb479562c419b48d750a8f9303c4a5a717ca7f2fe3b3658cc1bb9578a48` (pre-`L3b`)
and reads **19/19**, so 52/52 was correct *for the tree it measured*. The
round-25 commit then swept in the post-argot gate, and the connector surface the
receipt certified moved underneath it. No round-25 or round-26 artifact records
51/52: `grep -rn "51/52" reports/round-26/` → **0 files** (18:09:21Z).

**Convergence, stated as convergence.** The sibling round-26 spot-check
(`reports/round-26/audit/x60-register-derivation-spotcheck.md` §3) independently
found the same leg-count drift from the other side — the round-25 *frozen
manifest* pins gate `879d40bf…` (which is not on disk) while the recorded outputs
read `19/19` without `L3b-argot` — and the round-26 O seats' `pins.md` §4 names
the `20/20 != 19/19` reading and declines it as their tail ("Reported, not
absorbed"). This seat's contribution is the **checker-side** consequence: the
same drift drops the r4 successor checker's own control count from 52 to 51 and
lands an undeclared failure inside a control whose whole purpose is to assert
that no undeclared failure exists. The remedy (widen the allowance, or re-point
the frozen runner as a new row) is the O seats' and the parent's; this fragment
lands no pin and edits no byte.

## 5. The two-sided A/B control for §4c

Three clones, same checker, same command, one variable — the tree revision:

| clone | HEAD | `typed-pipeline-gate.py` sha256 (first 8) | D4 gate legs | r4 checker |
|---|---|---|---|---|
| `.scratch/x61/clone-pre` | `f74fc94` (pre-integration) | `04ad4bb4` | **19/19** | **52/52**, `passed True` |
| `.scratch/r25-x48/clone` (X48's, reused read-only) | `f74fc94` | `04ad4bb4` | **19/19** | 52/52 at 17:39:17Z |
| `.scratch/x61/clone` | `1ad491a` (HEAD) | `b749ad07` | **20/20** | **51/52**, `passed False` |

- **Direct leg control:** in the HEAD clone, hiding the sibling gate
  (`mv tools/gates/argot-derivation-gate.py` aside) drops the D4 run back to
  **19/19**; restoring it returns **20/20**. The leg count flips exactly on the
  `L3b-argot` leg's presence, and on nothing else — the guard is
  `if generalized and ARGOT_GATE.is_file()` (`typed-pipeline-gate.py:522`), and
  the D2 default path is unchanged (16/16 at HEAD and before).
- **Commit control:** `git show e571894:tools/gates/typed-pipeline-gate.py`
  contains neither `L3b-argot` nor `ARGOT_GATE`; `git show fc13cd2:…` contains
  both. The leg entered at the round-25 integration commit.
- **Pre-tree receipt:** running the checker against `.scratch/x61/clone-pre`
  reproduces **52/52, `passed True`**, with only the two declared tails failing —
  i.e. the checker's own verdict is revision-dependent, and its filed 52/52 was a
  true measurement of a pre-integration tree, not a mis-recorded number.
- **Non-claim:** this seat does not assert the round-25 gate change was wrong. The
  gate's own `--selftest` was updated in the same commit (now **19/19** checks,
  up from 12/12), so the leg-count move was visible to the seat that made it. The
  defect is the **un-updated expectation** in a frozen validator and in a filed
  checker's allowance list.

## 6. Claim C connector — the queue is dispositioned, and the numbers agree

- **README queue rows:** independent parse of `corpus/lessons/README.md` §4 at
  18:09:57Z → **49** data rows, 0 duplicates, first `Q-02-1`, last `Q-S1-1`.
  (The round-25 index measured 49 as well.)
- **Round-26 dispositions:** `reports/round-26/open-questions/dispositions.json`
  (sha256 `ebf9aabddac3698cc56530399f79253e78a648f6bbf1f2a4315ccb43ca9b3b2c`,
  observed 18:07:14Z) declares `ledger_rows: 78`, `undispositioned: []`,
  `disposition_counts {carried 51, fixed-with-evidence 15, routed 7,
  standing-rule 4, closed-by-supersession 1}`, surfaces `readme 49` +
  `census 29`, and 8 overlap ids (`OQ-R2-01..04` ↔ `Q-02-1..4`).
- **Cross-check that the two surfaces agree:** the disposition ledger's `readme`
  rows number **49** and their id set **equals** the 49 ids this seat parsed out
  of the README table (**True**); the `census` rows number **29**, matching the
  declared surface. Every ledger row carries a `disposition` (**0** rows without
  one) and the ids are unique (78/78). This seat reproduces the *arithmetic*; it
  does not certify any individual disposition's correctness, which is the C
  seats' and the parent's.
- **Not this seat's to close:** the README carries 49 rows and the disposition
  ledger 78 because it also carries the round-25 census surface — the claim's
  "zero rows without a disposition" is asserted over the ledger, and this seat
  confirms the ledger's own consistency, not the queue's completeness against
  prose.

## 7. Regressions re-run (controls for "no axis harmed")

Batch at **18:03:52Z**, TMPDIR set, `PYTHONDONTWRITEBYTECODE=1`:

| command | exit | result |
|---|---|---|
| `tools/gates/typed-pipeline-gate.py --selftest` | 0 | `19/19 checks passed` |
| `tools/gates/naming-collision-gate.py --selftest` | 0 | 12 findings across 11 ids; positive control clean; malformed exit 2 |
| `tools/gates/argot-derivation-gate.py --selftest` | 0 | `21/21 checks passed` |
| `tools/gates/handoff-packet-check.py --selftest` | 0 | 11 findings across 9 ids; clean control exit 0 |
| `tools/gates/phonology-sanity-gate.py --selftest` | 0 | 15/15 planted IDs; 29 control cases |
| `tools/gates/myth-consistency-gate.py --selftest` | 0 | planted IDs present; clean control exit 0 |
| `tools/gates/d4-typed-labels-check-gate.py --selftest` | 0 | `163/163 checks passed` |
| `tools/gates/lexicon-coverage-audit.py --selftest` | 0 | `14/14 checks passed` |
| `tools/gates/provenance-audit.py --selftest` | 0 | SELFTEST OK; planted IDs; exit 2 on missing path |
| `tools/d2-typed-labels.py --selftest` | 0 | `163/163 checks passed` |
| `tools/assemble-d4-typed.py --check` | 0 | byte-identical deterministic typed packet |
| `tools/assemble-culture-d4.py --check` | 0 | byte-identical deterministic assembly |
| `tools/assemble-culture-d3.py --check` | 0 | both outputs byte-identical |
| `tools/assemble-d2.py --check` | 0 | byte-identical deterministic assembly |

`tools/gates/d4-assembly-check-gate.py --selftest` → exit **2**, but the tool
takes a packet path, not `--selftest` (`assembly error: [Errno 2] No such file
or directory: '--selftest'`). That is a **usage** result, not a regression; this
seat did not find a selftest entry point for that gate and does not claim one
exists. `costume-era-consistency-gate.py --selftest` → exit 0 with its expected
fixture line.

## 8. Limits and non-claims

- No round acceptance, no promotion claim, no canon/rights/freshness
  certification. `reports/round-26/run-validation.py` **was still being written**
  during this seat's window (44,891 B at 18:07Z → 79,352 B at 18:09Z, sha256
  `7e9b4457d0ec61c7d1fca75396023eec22df8bac580e16824fb9796cda3e70ed` at the later
  stamp), and `reports/round-26/validation.json` **did not exist** at 18:09:57Z.
  The declared counting command is therefore `to-verify` until its owner lands a
  receipt; nothing here substitutes for it, and any artifact arriving after a
  stated stamp needs a dated refresh, not an inferred worker failure.
- The round-26 wave was **in flight** at these observations: `reports/round-26/`
  gained `scope.md`, `availability.json`, `argot/D2{1..4}*`, `register/{design,
  forms,rules,review}.md`, `audit/x60*`, `audit/x63*`, `gate-tests/*`,
  `lessons/*`, `open-questions/*`, `remainders/*`, `scribe/*` between 18:01Z and
  18:09Z, and `tools/gates/frozen/round-26/gate-input/` appeared at 18:08:08Z. All
  are untracked working-tree files. This seat read several for coordination
  (§3, §4c) and says so; none is re-certified here, and no round-26 sibling
  fragment was written by this seat.
- Sibling fragments were read for coordination only; every measurement in §1-§7
  was taken by this seat's own commands, and where a sibling agrees (§3, §4c) it
  is stated as **convergence**, not inheritance.
- No historical round validator was executed; no filed rounds 8–25 byte was
  written; no Git mutation was performed. The only lane write is this fragment,
  plus gitignored scratch under `.scratch/x61/` (clones `clone`, `clone-pre`,
  receipts `r4-check-receipt.json`, `r4-check-pre-receipt.json`, `x60.out`,
  `x60-nocontrol.out`, `repoint.out`).
- The fleet-root debris (§1) is disclosed, not dispositioned: it is not a
  kotodama filed artifact and it predates this round's dispatch.
- The third connector failure (§4c) is **reported, not repaired**: repairing it
  moves a frozen validator or a filed checker's allowance list and therefore
  requires the repin/new-row discipline the lane's rules impose. This seat edits
  no gate byte, lands no pin, and claims no fix.
