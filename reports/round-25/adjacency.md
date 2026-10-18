# Round 25 — Adjacency / connector (SCRIBE X43)

- **Date:** 2026-10-18. Every timestamp below is UTC from this seat's own runs;
  the command batches are anchored by `date -u` at **17:24:42Z**, **17:27:06Z**,
  **17:27:43Z** and **17:28:19Z**, and observations between anchors were taken
  inside those windows (bounded, not individually stamped).
- **Axes:** adjacency (boundary invariants) + connector-surface evidence for
  claim O's two tails (gate-input honesty; v3 supersession), with a read-only
  cross-check of claims D (argot-derivation forecast delta) and C (lessons
  index) as they bear on the connector surfaces this fragment watches.
- **Write scope:** only this fragment. No source fixes, no packet/validator/pin
  edits, no shared bookkeeping, no historical validator run, no Git mutation, no
  commit/push, no sibling writes. `export TMPDIR=$PWD/.scratch` was set before
  every scratch-writing command; scratch lived under `.scratch/x43/` (gitignored,
  lane-internal). No filed rounds 8–24 byte was written by this seat.
- **Baseline binding:** declared baseline `e06581b7fc2b50050a336f7f38a7e2baebcc6abc`
  (`reports/round-25/claims.json:5`); observed lane HEAD
  `f74fc9403d4b02c8ee76439eb133e3dea9b65b14`; `git merge-base --is-ancestor
  e06581b7… HEAD` → success (17:24:42Z).

## Verdict (scoped to this seat's observations)

**Adjacency: clean on the filed-round surface.** All 1,158 tracked filed paths
under `reports/round-{8..24}` are blob-identical to the declared baseline; the
`baseline..HEAD` diff over that surface is empty; `PROVINCE.md` and the handoff
interface contract are byte-unmoved across baseline/HEAD/worktree; the newest v3
revision still passes the structural envelope gate; the live D4 gate is green
against the landed pins.

**Connector state for claim O: both hazards reproduce unfixed at this seat's
observations, and both mechanisms are now isolated with controls.** (a) The
derived-packet false red is live on pinned gate bytes: feeding
`packet.d4.typed.yml` back gives exit 1 / 14-of-16 with two failing legs, and
this seat independently reproduced the L2 `DERIV-REPLAY` class to its source —
one over-escaped regex in the gate's own legacy rebuild. (b) The newest v3
revision on disk is still `declared-in-r3`; its D4 claim rows and `OQ-V3-05`
still carry the pre-family-clean numbers, and no `declared-in-r4` exists
anywhere in the tree.

**Fleet root: NOT CLEAN** (corroborating X39) — ten untracked `.scratch/*.out`
files at the fleet root, all last written before the round-25 dispatch commit.

## 1. Boundary observations

Batch at **17:24:42Z**, from the lane root:

- `git ls-files reports/round-{8..24} | wc -l` → **1,158** tracked filed paths.
- `git status --porcelain=v1 --untracked-files=all -- reports/round-{8..24}` →
  empty. `git diff --name-status e06581b7 HEAD -- reports/round-{8..24}` →
  empty. The declaration commit added only `reports/round-25/{claims,targets}.json`,
  so no filed path changed at commit level baseline→HEAD.
- **Detector control (per-path blob comparison), 17:27:06Z:** a read-only
  `python3 -` pass walked all **1,158** baseline tree entries
  (`git ls-tree -r -z <baseline> -- reports/round-{8..24}`) and compared each
  working file's `git hash-object` to its baseline blob → **0 mismatches**.
  True-positive control: `git rev-parse <baseline>:reports/round-24/validation.json`
  equalled the live blob (decl==live **True**); appending `\nx43-in-memory-probe\n`
  **in memory only** produced a differing SHA-1 (**True**); the file re-read
  unchanged afterwards (**True**). The detector demonstrably reports a
  deviation, so the 1,158 clean paths are a positive observation, not a blind
  pass.
- **PROVINCE accuracy:** `git rev-parse <baseline>:PROVINCE.md`,
  `git rev-parse HEAD:PROVINCE.md` and `git hash-object PROVINCE.md` all return
  `313b182f251564b7997b06996b4f063370778f11` (17:24:42Z). Read against the live
  tree, its boundary statements hold: own-repo write scope; the refuses list
  matches the sibling lanes that exist (`lore-shokunin`, `chousa-shokunin`,
  `kake-shokunin`, `kotoba-shokunin`, `game-dev-2d-shokunin`,
  `game-dev-3d-shokunin` all present, 17:27:43Z); the adjacent-contract path
  exists and is digest-stable below. No correction drafted.
- **Fleet root:** `git -C /home/vgpnk/Projects/shokunin status --porcelain=v1
  --untracked-files=all` returns exactly **ten** rows, all
  `?? .scratch/*.out` (`battery`, `coupling`, `craft`, `d2check`, `d3check`,
  `replay-r22`, `replay-r3`, `rv5-p`, `rv6-p`, `rv7-p`), mtimes 13:10–13:15
  local — **before** the round-25 dispatch commit (14:23:25−03:00). This seat
  corroborates X39's NOT-CLEAN verdict for the visible family and cites
  `reports/round-25/scope.md` §Verdict for the second, `git status`-invisible
  family and its masking control; this seat neither re-derived that control nor
  dispositioned either family. No kotodama filed artifact is involved.

## 2. Connector invariants (interface + envelopes)

- **Handoff interface contract unmoved:** `git rev-parse` at baseline and HEAD
  plus `git hash-object` on the worktree all give blob
  `66987ff3ef921bffe6d497608b2bc049f3b5ed9e` for
  `corpus/knowledge/synthesis/worldbible-integration-contract.md`
  (17:24:42Z); its SHA-256 is
  `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069` — the same
  digest the v2 baseline read set pinned (`reports/round-22/fixes/alias-coercion-v2-07.json`
  → `inputs`, per `reports/round-23/adjacency.md`). No contract drift across the
  boundary. The L0 contract-digest ratification question (SCORECARD round-8 row;
  fleet `.ufo/l0-questions.md`) remains open and escalated — not absorbed here.
- **Structural envelope green on both v3 revisions (control for §4):**
  `python3 tools/gates/handoff-packet-check.py
  reports/round-23/wording/declared-in-r3/packet.md` → exit **0**,
  `fields=16/16 glossary-entries=20 findings=0`; the same over
  `reports/round-22/handoff/declared-in-r2/packet.md` → exit **0**, identical
  counts (17:28:19Z, TMPDIR set).
- **Live D4 gate green against the landed pins:** `python3
  tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` → exit
  **0**, **19/19** legs; the D2 source entry → exit **0**, **16/16**; the
  flagless D2 default → exit **0**, **16/16**; the gate's own `--selftest` →
  exit **0**, `12/12 checks passed` (17:27:43Z batch, TMPDIR set).
- **Pipeline pins resolve:** `tools/gates/typed-pipelines.json` carries **10**
  distinct 64-hex digests; **6** are the live bytes of their declared paths
  (`tools/d2-typed-labels.py` `2819f687…`, `assemble-culture-d4.py` `943f487b…`,
  `assemble-d4-typed.py` `92f5460b…`, `typed-labels.d4.yml` `60b526b0…`,
  `expected-holds.json` `3826ba68…`, `packet.d4.yml` `e7ecd204…`) and **4** are
  historical/superseded (`cbcf997f…`, `a59990bb…`, `88c21ff3…`, `18d0cfce…`),
  correctly absent from live bytes. The `d4` profile carries **3**
  `repin_history` rows, the last dated `2026-10-18T14:53:59Z` (final
  combined-source binding). **No round-25 pin row, no
  `tools/gates/frozen/round-25/` and no `tools/gates/expected/…/r25-post/`
  exists yet** — the claim-O pin cascade is unlanded at this observation.
- **Gate bytes are the pinned bytes:** `sha256 tools/gates/typed-pipeline-gate.py`
  = `04ad4bb479562c419b48d750a8f9303c4a5a717ca7f2fe3b3658cc1bb9578a48`,
  which is the `d4-repin` MANIFEST pin — so §3 is a live defect on the pinned
  tool, not a drifted working copy. `sha256 tools/gates/naming-collision-gate.py`
  = `d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d`.
- **Determinism spot-check:** `assemble-d4-typed.py --check` → byte-identical
  deterministic typed packet; `assemble-culture-d4.py --check`,
  `assemble-culture-d3.py --check`, `assemble-d2.py --check` → all
  byte-identical (17:27:43Z).

## 3. Claim O tail (a) — the derived-packet false red, mechanism isolated

The two named symptoms reproduce verbatim on the pinned gate bytes:

| # | Command (2026-10-18) | Exit | Legs | Failing legs |
|---|---|---|---|---|
| R1 | `… typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | **0** | 19/19 | — |
| R2 | `… typed-pipeline-gate.py examples/culture-d4/packet.d4.typed.yml` | **1** | 14/16 | `L2-channel`, `L3-routing-consistency` |
| R3 | `… typed-pipeline-gate.py` (flagless, D2 default) | **0** | 16/16 | — |
| R4 | `… typed-pipeline-gate.py examples/culture-d2/packet.d2.typed.yml` | **0** | 13/13 | — |

**R4 is the control that scopes the defect:** the typed-input direction passes
for D2 (whose routing rows all carry a real `owed_slot`), so the failure is
specific to the D4 register class where `owed_slot: null` is legal.

**Root cause A — `routed_slots` reads the reader's `'null'` string as a slot.**
`tools/gates/typed-pipeline-gate.py:748-749` filters `moved_field(row)` but tests
`owed_slot` with bare truthiness, while `moved_field()` (`:186-194`) carries the
null-ish guard and its own docstring names the trap (the lane's reader keeps an
unquoted `null` as the string). Measured on the committed typed packet
(17:27:06Z): `typed_channel` holds **12** rows, **6** with `owed_slot` reading as
the string `'null'` (all of type `str`). So `routed_slots` gets 12 entries
against 6 held slots. The reported `holds … vs routed …` halves in fact
**agree** (12 = 12); only the `owed slots` half fails, and the intended
comparison (6 labelled slots = 6) is consistent — the missing filter
manufactures the mismatch. `L3-routing-consistency` has no `null`-valued
`owed_slot` negative control in the gate's own `--selftest` (12/12 covers
smuggle, dropped-row, laundered hold, adapter drift, malformed, missing).

**Root cause B — the L2 legacy arm is a rebuild of the product, not the source.**
This seat re-ran the gate's own rebuild path (deepcopy the parsed typed doc;
apply the `:588-598` field-move loop; pop the seven typed keys; serialize via the
D2 `yaml_lines`) and graded the result with the naming gate directly
(17:27:06Z):

```
naming-collision-gate.py examples/culture-d4/packet.d4.yml        → rc=1, 0 × DERIV-REPLAY
naming-collision-gate.py examples/culture-d4/packet.d4.typed.yml  → rc=1, 0 × DERIV-REPLAY
naming-collision-gate.py .scratch/x43/rebuilt-legacy.yml          → rc=1, 8 × DERIV-REPLAY
```

**Neither committed packet produces `DERIV-REPLAY`; only the gate's internal
rebuild does.** The eight lines name NM-01…NM-08 and are exactly the class
`L2-channel` reports. The rebuild is 65,128 bytes against the committed source's
82,859 (359 differing lines, sha256
`182f07b9229a44a83ad837df347341be0cd6fcc631e374227fe1376dff1c165e`), and the
corrupting diff is visible and small:

| file | `morphology.derivation_rules` CX-01 pattern | in-memory value |
|---|---|---|
| `examples/culture-d4/packet.d4.yml:209` | `"^(?P<a>.+)\\+(?P<b>.+)$"` | `^(?P<a>.+)\+(?P<b>.+)$` |
| rebuild | `"^(?P<a>.+)\\\\+(?P<b>.+)$"` | one backslash too many |

Plus the same class elsewhere: `onset_clusters: false` → `"false"`. With the
doubled escape the `\+` stops matching, `re.fullmatch` fails on `tum+hai`, and
one finding appears per CX-01 name. This is the round-24 cold-run F5 /
scribe-C2 mechanism, unchanged, and it **agrees numerically with the independent
round-25 diagnosis** at `reports/round-25/gate-input/diagnosis.md` §2-§3
(same two root causes, same rebuild sha, same isolation result). This seat
reproduced the mechanism independently before reading that file; the
corroboration is convergence, not inheritance.

**Disposition is not this seat's.** The claim's "after" admits either a named
input-class diagnostic (exit 2) or correct L2/L3 handling of null `owed_slot`;
both are code-level repairs that move pinned gate/serializer bytes and therefore
require the repin cascade as **new rows** (round-24 §3 N3). This fragment lands
no pin, edits no gate byte, and claims no fix.

## 4. Claim O tail (b) — v3 supersession: measured state

**The newest v3 revision on disk is still `declared-in-r3`.** No `declared-in-r4`
path exists anywhere under `reports/` or `tools/` (grep, 17:28:19Z); the only
occurrence of the token is the claim text itself (`reports/round-25/claims.json:14`).

| revision | path | sha256 |
|---|---|---|
| 3.1.1 (baseline) | `reports/round-22/handoff/declared-in-r2/packet.md` | `a97a0f0a0a497cb4410124607065df7686bbc7f78b4b46bdaaaa1d66ba4d1b6e` |
| 3.1.1 + one reworded phrase | `reports/round-23/wording/declared-in-r3/packet.md` | `084dc5db9a8d923bb06a987b0b437bf5bfee3caac2e41cd16743da0c71499250` |

`r3` is `r2` plus the round-23 wording supersession (`freeze.txt`: exactly the
`unchanged-foreign-path` → `foreign-path-stability` phrase in D4-CL08's
uncertainty basis, plus a provenance note). The structural envelope passes on
both (§2) — which is precisely why the envelope is **not** semantic integration
evidence, the asymmetry the round-12 contract audit recorded
(`reports/round-12/adjacency/contract.md:9-10,23`).

**Measured contrast, newest revision vs live bytes (17:27:06Z).** `r3` still
carries the pre-family-clean D4 prose:

| row | stale claim in `r3` | live value | source |
|---|---|---|---|
| `packet.md:150` D4-CL05 | `findings_total 16, findings_hold_or_fail 15` | `findings_total 12`, `findings_hold_or_fail 12` | `examples/culture-d4/typed-labels.d4.yml#coverage` |
| `packet.md:151` D4-CL06 | `expected-holds.json#counts (hold 15, note 1, fail 0)`, "twelve … holds … **and three** `D2L-RANK` holds, plus one `D2L-RANK` note" | `counts = {hold: 12, note: 0, fail: 0}` | `examples/culture-d4/expected-holds.json` |
| `packet.md:152` D4-CL07 | reconciliation `conflicts (4)`, `quarantine handles (3)` | `conflicts 0`, `rank_quarantine_handles 0` | `…typed-labels.d4.yml#coverage` |
| `packet.md:154` D4-CL09 | `rank_rules_unresolved_items 13`, `rank_quarantine_handles 3`, `#conflicts 4` | `0`, `0`, `0` | `…typed-labels.d4.yml#coverage` |
| `packet.md:309` OQ-V3-05 | "twelve form holds + **three rank holds** + **one note**, thirteen unresolved rank items, three quarantine handles and four conflicts" | 12 form holds, 0 rank holds, 0 notes, 0 unresolved, 0 handles, 0 conflicts | `expected-holds.json` + `…d4.yml#coverage` |

The live `typed_labels.stats` is `{fail: 0, hold: 12, labels: 74}` — consistent
with `coverage`, so the stale numbers are the packet's, not a measurement
artefact.

**Negative control that keeps the finding honest:** `packet.md:131` D2-CL01
carries `findings_total 16 with 15 hold-or-fail`, and the **live** D2 projection
measures `findings_total 16`, `findings_hold_or_fail 15`, `conflicts 4`,
`rank_quarantine_handles 3`, `rank_rules_unresolved_items 13`,
`reconciliation_records 10` (`examples/culture-d2/typed-labels.d2.yml#coverage`).
The D2 rows are **accurate**; the `16`/`15`/`13`/`3`/`4` numbers are not
globally stale — they are D2's true residuals that the D4 rows and `OQ-V3-05`
still quote as if they were D4's. That is exactly the family-clean confusion the
claim names, and it is why "the numbers are old" is the wrong reading: the
numbers are D2's, correctly, in the wrong rows.

The `OQ-V3-05` passengers (13 unresolved rank items, 3 quarantine handles,
4 conflicts, and the "three rank holds + one note" phrase) therefore remain
**undispositioned** at this observation. The claim's after-required asks for a
new revision `declared-in-r4` with corrected prose plus the passengers
dispositioned; neither has landed, and this seat writes neither.

## 5. Cross-checks for claims D and C (read-only, on the surfaces this fragment watches)

These are corroborating observations only; the claims' owners land the product.

- **Claim D (argot derivation).** At 17:27:43Z: `grep -c "ARGOT"` over `tools/`
  → **0**; `grep -c "D4L-"` over `tools/d2-typed-labels.py`,
  `tools/assemble-d4-typed.py`, `tools/assemble-culture-d4.py` → **0 each**. The
  D4 packet carries `derivation_rules` CX-01..CX-03 (compound/suffix, the naming
  gate's own mechanism) and `derived_from`/`head2`/`reverse` → **0 occurrences**;
  the `coverage` block has no `derived_forms`/`derived_ok` keys. So the round-17
  Δ3 forecast (a derivation-checked relation with its own control-only
  `D4L-ARGOT-DERIV`) has **no delivered artifact** at this observation: the
  connector surface between the forecast and the tree is still open. The
  round-25 sibling analysis is filed at `reports/round-25/argot/forecast.md`
  (read for coordination only; its content is not re-certified here).
- **Claim C (lessons index).** `corpus/lessons/README.md` now exists as an
  untracked working-tree file (21,367 B, sha256
  `f0a2b24bd9ecf98ab929465c1c355bb121a6d5b16f8d752021ae255ab993a1c4`,
  17:28:19Z). Independent read of its structure: **24** index rows over **24**
  lesson `.md` files, with explicit placeholder rows for the two gaps (round 13
  operator-skipped, no file; round 24's record is the promotion-review dossier)
  and for `supplement-opencode-1.md`; §3 documents the three census formats.
  The sibling audit `reports/round-25/audit/c31-lessons-index-audit.py`
  (read-only; run at 17:27:43Z) reports `C31_index_rows_eq_files` **PASS**,
  `C33_formats_documented` **PASS** (`{gate-keeper: 13, fragment-index: 5,
  plain: 6}`), `C34_pins_rederived` **PASS**, and `C32_owners_resolve` **FAIL**
  with one finding, `C32-1 unresolvable-owner` (8 rows, including a literal
  `owner` header cell and five `reports/round-25`/`round-4-audit` pointers it
  does not resolve). This fragment records that reading; the fix is the C
  seats' and the parent's.

## 6. Limits and non-claims

- No round acceptance, no promotion claim, no canon/rights/freshness
  certification. `reports/round-25/run-validation.py` did **not** exist at
  17:28:19Z (`ls`: No such file or directory), so the declared counting command
  is `to-verify` until its owner lands it; nothing here substitutes for it.
- The round-25 wave was **in flight** at these observations: `reports/round-25/`
  gained `scope.md`, `argot/forecast.md`, `gate-input/{diagnosis,design}.md`,
  `audit/{c31-…,x47-…}.py` and `lessons/lessons-index-census.py` between
  14:23Z and 14:28Z local. All are untracked working-tree files; none is
  re-certified here, and a file arriving after a stated stamp needs a dated
  refresh, not an inferred worker failure.
- Sibling fragments were read for coordination only
  (`reports/round-25/scope.md`, `reports/round-25/gate-input/diagnosis.md`,
  `reports/round-25/argot/forecast.md`); every measurement in §1-§4 was taken by
  this seat's own commands before or independently of that reading, and §3's
  agreement with `diagnosis.md` is stated as convergence.
- No historical round validator was executed; no filed rounds 8–24 byte was
  written; no Git mutation was performed. The only lane write is this fragment,
  plus gitignored scratch under `.scratch/x43/`.
- The fleet-root debris (§1) is disclosed, not dispositioned: it is not a
  kotodama filed artifact and it predates this round's dispatch.
