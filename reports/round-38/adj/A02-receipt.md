- Seat: A02 | executor | claim A | date 2026-10-19 | baseline 9bccc9b

# A02 — adjacency receipt draft + verifier coordination

**Status: dependency-limited receipt. No adjacency axis verdict.** Assignment
(`reports/round-38/targets.json:160-165`): *"Adjacency receipt draft + verifier coordination."* Out
path `adj/A02-receipt.md`. Claim **A** is carried by three seats (A01/A02/A03,
`targets.json:152-172`) but is **not declared in `reports/round-38/claims.json`**, which files only
`D` and `O` (`claims.json:13-24`; `axes_in_play` `:9` = `["depth","operability"]`). Round 38 therefore
declares **no adjacency axis-move**; this fragment is a scope/bleed watch and a coordination record,
not a claim-A verdict, and nothing here is round acceptance or a canon/clearance/promotion statement
(`claims.json:26-27`).

**Dependency state — and it moved under this seat.** `find reports/round-38 -type f` returned **7
files** at 2026-10-19T11:07Z (the two declarations, the two telemetry records, `adj/A03-verify.md`,
`depth/D05-verify.md`, `scribe/S02-telemetry-draft.md`), and this seat took every measurement in
§1–§4 and §7 against that state. **`adj/A01-scope.md` landed at 11:07Z, between this seat's final
measurement and its write**, together with `depth/D07-receipt.md` and `depth/D10b-verify.md`; §6
folds A01 as it landed. The remaining D/O executor and design fragments (`scout/`, `plan/`,
`depth/D01..D04`, `op/O01..O02`, `cross/`, `review/`) were **still absent at 11:08Z**. Sections §1–§5
and §7 are this seat's own first-hand measurements and inherit nothing; the missing slices are named
as owed rather than folded.

## 1. Method, window, and what "first-hand" means here

Lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`,
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, interpreter `python3 -V` → **Python 3.14.7**,
observation window **2026-10-19T11:04:20Z–11:07:49Z**. Every count, digest and diff in §2–§5 and §7 was
taken by this seat in that window; no number is inherited from a fragment. Exit codes were captured
unpiped. No `reports/round-*/run-validation.py` was executed — in-tree or in a copy (F-C13-1,
`targets.json:8`) — no `--freeze` was attempted, and no git-mutating command was run. This seat wrote
only its own out path. §6 and the F-A02-3 generalization were added after that window, against the
sibling fragments named in `## Citations`; A01's §3 experiments were not re-run by this seat and are
attributed to A01 throughout.

## 2. Scope census

| surface | command | observed |
|---|---|---|
| baseline resolves | `git rev-parse HEAD`; `git rev-parse 9bccc9b` | both `9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26` |
| tracked cleanliness | `git diff --name-status 9bccc9b`; `git diff --stat 9bccc9b` | empty / empty (0 rows) |
| untracked scope | `git status --porcelain --untracked-files=all` | 7 rows, **all** `?? reports/round-38/…`; zero non-round-38 rows |
| protected roots, tracked | `git diff --name-status 9bccc9b -- 'reports/round-[1-9]' 'reports/round-[1-3][0-9]' corpus/lessons tools/gates/frozen` | **0 rows** |
| protected roots, untracked | `git status --porcelain --untracked-files=all -- <same roots>` | **0 rows** |
| `LOG.md` untouched | `git diff --name-status 9bccc9b -- LOG.md` | 0 rows |
| frozen gate bytes | `git diff --name-status 9bccc9b -- tools/gates/frozen/` | 0 rows |

Verdict for the Git-visible surface: **clean**. The pre-dispatch tree is exactly the declared baseline,
and no out-of-lane path is Git-visible. This is a point-in-time census, not a continuous-write
guarantee, and Git does not observe untracked filesystem writes outside the repository — neither is
asserted absent (same limit `reports/round-37/adj/A03-scope.md` recorded).

## 3. Pin integrity — the round's adjacency-critical bytes

The r7 pinned pair is byte-unchanged and matches the claim-O threshold string:

```
45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19  reports/round-34/handoff/declared-in-r7/packet.md
0e22913850cd85bc393fe6d0d7a8bf448e9b253aa2884457d4c8999ac9096599  reports/round-34/handoff/declared-in-r7/twin.json
bbe15887b710bb36def5e1c82fa5b1c1ef37df3cb5581c7c2982a0498e829d55  reports/round-34/handoff/declared-in-r7/expected.json
```

`45f57132…` is exactly the digest `claims.json:24` names as claim O's acceptance threshold, and
`bbe15887…` matches the pin `reports/round-38/depth/D05-verify.md` §4 recorded. The default v3 chain
re-renders that pair and exits 0 with no tree write:

```
python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet
→ exit=0  fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4
          v2_subset=equal alias_leg=landed packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19
untracked_before=6  untracked_after=6  git diff --name-status → 0 rows
```

So the claim-O acceptance threshold *"r7 packet sha unchanged 45f57132…"* holds **at baseline**. Whether
it still holds after the O guard lands is R03's cross-claim question
(`reports/round-38/targets.json:188-192`), not this seat's.

## 4. Bleed scan

- **Credential sweep — clean.** `grep -rniE 'bearer|authorization|api[_-]?key|secret|password|token'`
  over `claims.json`, `targets.json` and both telemetry records → **0 hits** (`AGENTS.md:31`: no
  credentials or authorization headers in telemetry). The only route string present is the lane name
  `xai-oauth`.
- **Freshness pause — respected.** `claims.json:11` `freshness_pause_in_force: true`; `:26` non-goal
  *"no freshness axis-move"*. No seat wrote a freshness claim, and this seat made no fetch.
- **Language / cross-domain scan of the round's drafts — clean at this cut.** The seven round-38 files
  carry no `game-dev`/mechanics, chousa/source-research-method, kake/web-publishing or
  kotoba/prompt-skill language; no sibling-repository or world-bible path is written or cited as a
  target. The D/O drafts name only in-lane paths (`tools/gates/*`, `tools/exercise-handoff-e2e.py`,
  `examples/culture-d4/*`), all inside `PROVINCE.md:9-11` ownership. This is a structural scan of seven
  files, not a scholarship or admission verdict.

## 5. Live adjacency candidates found this round

**F-A02-1 — the A block carries an undeclared claim id.** `claims.json` declares exactly `{D, O}`
(`:13-24`) and lists `axes_in_play` without adjacency (`:9`), while the seat census is
`{D: 13, O: 10, cross: 6, A: 3}` over 32 unique ids and 32 unique out paths. Cross-checked against the
regimen-2 rounds: r33/r34/r35/r36/r37 all match their seat claim census; **r38 is the first that does
not** (independently found by `reports/round-38/scribe/S02-telemetry-draft.md` §2, F2). Class: a
**declaration-form defect**, not a seat-count defect (32 == 32, `dispatch-declared.json:7`). Disposition:
**routed, not absorbed** — the integrator must either record it as a declaration-form difference with the
A block named as unadjudicated adjacency work, or have the round-38 runner assert the partition against
`claims.json` and fail on the extra block. The one thing the record must not do is silently accept a
superset. This seat does not re-scope the round.

**F-A02-2 — the r37 README placeholder row is now satisfied; the duplicate heading is not.** The r37
defect queue carries `R36-README-E3-PLACEHOLDERS` and `R36-README-DUPLICATE-HEADING`, both
`carried-with-owner` (`reports/round-37/op/defect-queue.json`). Measured live:

```
grep -c '__E3_PLACEHOLDER__' corpus/README.md  → 0
grep -c '^# kotodama-shokunin corpus index' corpus/README.md → 2
corpus/README.md sha256 b80274bcd24b8b6e621f499fb20d4a07aa3b7b48dbb3508e0a9ac974f68e1d74
```

The placeholders were removed by `fa90c77` (*"…r35 placeholder repair"*, `-2` lines), so that queue row
is **stale as a live defect** and should be closed-with-evidence at the r38 census cut — not silently
dropped. The duplicate title heading **persists** (`:1` and `:3`, byte-identical, confirmed with
`cat -A`) and remains a live, unabsorbed integration candidate; `reports/round-37/op/O09-routing.md:12`
routes it to *"round 38, corpus-index integration"* and this seat did not edit the corpus
(`targets.json:5`; `PROVINCE.md:9-11` owns the partition, so an index editor is the owner, not this
lane's adjacency seat).

**F-A02-3 — the read-set roster defect is carried, is claim O's target, and is NOT r7-only.**
The r7 freeze read set omits `examples/culture-d4/components/13-register-law.yml` while the packet
manifest records 13 D4 component digests: `D4_COMPONENTS` (`tools/exercise-handoff-e2e.py:157-170`) is
a **12**-tuple feeding `V3_READ_SET` (`:1939-1953`); the r7 `expected.json` `inputs` map holds 12 D4
component rows. Filed in the r37 queue as `R36-R7-READSET-13` and `r37-A01-readset-roster-defect`, both
`carried-with-owner`. Adjudicated in `reports/round-37/adj/A01-freeze-adjudication.md:5` as a
**roster/completeness defect, not a documented skip** — and not an integrity bypass, because
`v3_verify_component_digests` (`tools/exercise-handoff-e2e.py:2208-2222`) measures the 13th component
transitively through the packet's own manifest.

**This seat independently reproduced X02's generalization of the class.** Every filed handoff baseline
carries the same 58-entry `inputs` map with only **12** D4 components and no `13-register-law.yml`:

| filed baseline | `inputs` | D4 components | has `13-register-law` |
|---|---:|---:|---|
| `reports/round-22/handoff/declared-in/expected.json` | 58 | 12 | no |
| `reports/round-22/handoff/declared-in-r2/expected.json` | 58 | 12 | no |
| `reports/round-26/handoff/declared-in-r5/expected.json` | 58 | 12 | no |
| `reports/round-30/handoff/declared-in-r6/expected.json` | 58 | 12 | no |
| `reports/round-34/handoff/declared-in-r7/expected.json` | 58 | 12 | no |

And the r6 *packet* names 13 components exactly as r7 does: `grep -o` on
`reports/round-30/handoff/declared-in-r6/packet.md` returns both `13 component digests` and
`9 D2, 4 D3, 13 D4`, while its own `expected.json` `inputs` holds 12 D4 components. So the mismatch
is present in **at least r6 and r7**, not in r7 alone — independently found by
`reports/round-38/cross/X02-honesty.md` §4a/§4b and reproduced here. Consequence for claim O's
acceptance shape, recorded because it is an adjacency-visible contract risk: the seat-O08 expectation
*"only the r7 row names"* is **unsatisfiable as written** against a manifest-completeness guard, and a
guard narrowed until it misses r6 would be vacuous on the very class the claim exists to catch. The
correct expectation is **r6 and r7 name; r2/r5 (and `declared-in`) stay green** — the integrator's call,
not this seat's. Round 38's claim O targets the class; **zero freeze bytes may move** (`claims.json:22`),
and the fix route remains a re-freeze as a new baseline row (A01 §3c).

**F-A02-4 — no declared fallback for position 6; the devin substitution is a named deviation.**
`REGIMEN.md:16` (schedule row 6) carries no fallback clause, unlike row 4 (`REGIMEN.md:14`).
`reports/round-38/telemetry/availability-attempt-1.json:7-13` records 32 requested / 0 launched / 0
completed / 32 failed at launch with `403 out of credits (grok.com)`, and dispositions the devin
re-dispatch as a **named deviation** with owner + reason. Telemetry-relevant (S02 §3 owns the record
form); adjacency-relevant only in that the observed record must not be made to read as though a
fallback had been declared. Recorded here, routed to the integrator/operator — the admission call is
not this seat's.

## 6. Verifier coordination

**A01 landed (11:07Z) and carries the round's real scope hazard** — measured, not argued. In
isolated `git archive` copies A01 found that (a) appending one comment to
`tools/gates/register-law-gate.py` turns `python3 -B tools/check-gate-battery.py` from exit 0 into
**exit 2 `BASELINE-GATE-REVISED`**, because the gate is pinned at `15f8b232…` by
`tools/gates/expected/register-law-gate/r30-post/expected.json` and that baseline must not be
repointed; (b) the same edit to `tools/gates/argot-derivation-gate.py` leaves the battery green
(its digest `b5406bcd…` is pinned by no `expected.json`); and (c) adding
`examples/culture-d4/components/13-register-law.yml` to `D4_COMPONENTS` makes
`python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` **exit 1 with `E2E-DIGEST`**, so the
O fix route must be a re-freeze as a new baseline row. A01 also records that the D claim's *"the two
named tool/example artifacts"* (`claims.json:16,27`) is an **unbound declaration** — no round-38 byte
names which two. **These are the load-bearing adjacency items of round 38 and this receipt adopts
them as findings, attributed to A01**, because they are exactly the class claim A exists to surface:
the cost of applying the round's own drafts to filed pins. I did not re-run A01's experiments; A01's
fragment is the evidence, and its §3 method statement (copy-only, never in-tree, no round runner)
matches the standard this receipt held itself to. The §3a/§3c *observed exits* (battery exit 2 on the
law-gate edit; `E2E-DIGEST` exit 1 on the 13th read-set member) are therefore **`to-verify` by
independent re-run** — this seat verified their *premises* read-only (the r30-post pin
`tools/gates/expected/register-law-gate/r30-post/expected.json` holds `gate_sha256 15f8b232…`, byte-equal
to the live script; no `expected.json` anywhere pins the argot gate's `b5406bcd…`; and
`corpus/knowledge/verification/gate-frozen-run-standard.md:74` states baselines are never rewritten),
but not the mutated-copy exit codes themselves.

**A03 landed and reproduces this receipt's evidence base independently** — it is a genuine
cross-check, not an echo. Its table (`reports/round-38/adj/A03-verify.md` §Independent reproduction)
matches this seat's readings on every overlapping surface: baseline `9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26`;
tracked diff empty; untracked rows all under `reports/round-38/` at its earlier cut; frozen bytes
unmoved; r7 pins `45f57132…`/`0e229138…`; the 13th component's live digest
`c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7` equal to the packet manifest pin;
argot `derived_pairs=8 violations=0`, law `findings=0`, typed `20/20 legs passed`; gate selftests
`27/27` and `45/45`; v3 chain exit 0 with the packet pin held. **Its `D4_COMPONENTS`=12 / manifest=13
roster reading is the same asymmetry this seat's F-A02-3 names.** A03 also independently confirmed
F-6's absence (zero `derived_forms`/`derived_ok` under `examples/` or `tools/`) and that the RL-8 era
leg is unimplemented. A03 sampled before A01 landed and filed its claim-specific comparison of A01's
prose as owed; A01 has now landed, so that comparison is **owed but now possible** and is the one
coordination item this seat cannot close. A03 ran its gates in isolated `git archive` copies and
recorded that it executed no in-tree runner and no `--freeze`; this seat's §3 v3 run was likewise
tree-neutral (untracked count unchanged across it, tracked diff still empty), so all three A-block
records agree the round's own measurements did not mutate the tree.

**Independent agreement between A01, A03 and D07 on the round's premises.** Three seats reached the
same readings without coordinating: the roster asymmetry 12-vs-13 (A01 §4, A03, D07 §Owed 6); the r7
pin triple `45f57132…`/`0e229138…`/`bbe15887…`; the baseline gate readings (argot `derived_pairs=8
violations=0`, law `findings=0`, typed `20/20`); and the two named-artifact ambiguity (A01 §4, D07
§Owed). D07 additionally demonstrates the RL-8 gap with a live E0-stamp tamper that produces no
finding from either gate — the same blind spot A03 recorded by grep. That is the strongest
adjacency signal available this round: the premises are not seat-specific.

**Coordination request — the one still open.** A03's outstanding item is the claim-specific
comparison of A01's landed prose; A01's is that *"the two named artifacts"* be bound to an explicit
roster (`A01-scope.md` §Owed). Both are for A03/the integrator, not this seat. This seat adds
F-A02-1 (the undeclared `A` claim id) and F-A02-2 (the now-satisfied placeholder row vs the live
duplicate heading), which no other A-block seat named.

## 7. Baseline digests the integrator diffs after landing

Recorded now so the post-landing delta is checkable against the declared baseline rather than against
a moving tree. All at HEAD `9bccc9b`:

```
b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb  tools/gates/argot-derivation-gate.py
15f8b23251ca2ad0a203bb1ed5fda2611dff9514e6a1af8120f520b1e7ec4169  tools/gates/register-law-gate.py
bfe1c78e479f74784e3d2b53b053b43cd8333214c46bcc8b908b3b45ebff0aa9  tools/exercise-handoff-e2e.py
c23b0ab532cfb9d4bb403405c6996982a447098048e08facbbc9f341ea13f82e  examples/culture-d4/typed-labels.d4.yml
aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3  examples/culture-d4/packet.d4.yml
05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6  PROVINCE.md
5ae7a9c8abab0843cfc6db09849f2fff369c0e880085deb546ec7ab764333808  AGENTS.md   (40 lines, 0 fence markers)
```

These are baseline readings, not landed-artifact claims: no D or O artifact has landed at this cut, and
this seat verifies none of them. A01's §3 adds the complementary pin facts: the battery pin
`tools/gates/expected/register-law-gate/r30-post/expected.json` at `gate_sha256 15f8b232…` (byte-equal
to the live script) and the absence of any `expected.json` pinning the argot gate's `b5406bcd…`.

## Owed

- A03's claim-specific comparison of A01's **landed** prose — A01 was absent when A03 sampled and has
  since landed (`adj/A01-scope.md`, 11:07Z). This is the one A-block coordination item still open.
  Owner: A03, then the integrator.
- Binding *"the two named tool/example artifacts"* (`claims.json:16,27`) to an explicit roster — no
  round-38 byte names which two (A01 §4; D07 §Owed). Owner: integrator / a later seat, before any
  draft is applied.
- Applying A01's §3 blast-radius findings at apply time: file a **new**
  `tools/gates/expected/register-law-gate/<new-id>/` baseline before landing the law-gate draft (never
  repoint r30-post), and keep the O guard's r7 output non-refusing so the filed chain stays at exit 0.
  Owner: integrator.
- A claim-A verdict for round 38 — **cannot be made from this round's declaration**: `claims.json`
  declares no adjacency claim (`:9,:13-24`). Whether the A block is a watch-only posture or an
  undeclared claim is the integrator's/operator's call (F-A02-1). This seat does not invent one.
- F-A02-1 `A`-block disposition; F-A02-2 placeholder-row closure + duplicate-heading ownership;
  F-A02-4 route adjudication. Owner: integrator.
- Correct claim O's acceptance expectation from *"only the r7 row names"* to **"r6 and r7 name;
  r2/r5 and `declared-in` stay green"** (F-A02-3; `reports/round-38/cross/X02-honesty.md` §4a/§4b,
  reproduced here). As written the expectation is unsatisfiable, and the narrowing that would satisfy
  it makes the guard vacuous on the class it exists to catch. Owner: integrator, against the O08
  regression sweep.
- Post-landing re-check of §7 digests and of the claim-O threshold (`45f57132…` unchanged, zero freeze
  bytes moved). Owner: R03/integrator, after the O guard lands.
- The D/O executor and design fragments (`scout/`, `plan/`, `depth/D01..D04`, `op/O01..O02`, `cross/`,
  `review/`) were **all absent** at this seat's cut; nothing in this receipt should be read as a verdict
  on them.

## Citations

- Binding rules and this seat's assignment: `reports/round-38/targets.json:3-8` (shared rules; `:8`
  F-C13-1), `:160-165` (A02 row, out path), `:152-172` (the A block); `reports/round-38/claims.json:9,11,13-24,26-27`.
- Scope/pin/bleed evidence: command outputs in §2–§4 and §7, taken 2026-10-19T11:04:20Z–11:07:00Z at
  lane root with `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1` — `git rev-parse`, `git diff
  --name-status/--stat 9bccc9b`, `git status --porcelain --untracked-files=all` (7 rows at that cut,
  all `reports/round-38/`; 11 rows at 11:07:14Z, still all `reports/round-38/`), `sha256sum` of the r7
  pair and the seven baseline artifacts, `python3 -B tools/exercise-handoff-e2e.py --profile v3
  --quiet`, `grep -c` on `corpus/README.md`, `cat -A` on its first four lines, and the
  credential/language greps.
- Roster asymmetry and F-6/RL-8: `tools/exercise-handoff-e2e.py:157-170,1939-1953,2208-2222`;
  `reports/round-34/handoff/declared-in-r7/expected.json` (`inputs`); `reports/round-37/adj/A01-freeze-adjudication.md:5,24-35`;
  `reports/round-36/scout/K01-register-scout.md:115,210-211`; `examples/culture-d4/components/13-register-law.yml:49,57`.
- Carried rows and routing: `reports/round-37/op/defect-queue.json` (`R36-R7-READSET-13`,
  `r37-A01-readset-roster-defect`, `R36-README-E3-PLACEHOLDERS`, `R36-README-DUPLICATE-HEADING`);
  `reports/round-37/op/O09-routing.md:12`; `fa90c77` (`corpus/README.md` −2 lines).
- Roster class generalized (F-A02-3): the five filed baselines
  `reports/round-22/handoff/declared-in/expected.json`, `reports/round-22/handoff/declared-in-r2/expected.json`,
  `reports/round-26/handoff/declared-in-r5/expected.json`, `reports/round-30/handoff/declared-in-r6/expected.json`,
  `reports/round-34/handoff/declared-in-r7/expected.json` (each 58 `inputs`, 12 D4 components, no
  `13-register-law.yml`), and `reports/round-30/handoff/declared-in-r6/packet.md` (`13 component
  digests`; `9 D2, 4 D3, 13 D4`) — read by this seat 2026-10-19T11:07Z;
  `reports/round-38/cross/X02-honesty.md` §4a/§4b (independent finding of the same generalization).
- Route/telemetry: `reports/round-38/telemetry/availability-attempt-1.json:7-13`;
  `reports/round-38/telemetry/dispatch-declared.json:7`; `REGIMEN.md:14,16,66-69,73-75`.
- Sibling fragments folded, each read in full: `reports/round-38/adj/A01-scope.md` (§3a–§3d blast
  radius: battery pin `15f8b232…`, the unpinned argot digest, the 13th-member `E2E-DIGEST` exit 1, the
  one-directional existing roster guard; §4 the two-named-artifacts ambiguity);
  `reports/round-38/adj/A03-verify.md` (independent reproduction, sampled before A01 landed);
  `reports/round-38/depth/D07-receipt.md` (§3.1 F-6 producer census, §4.2 the E0-stamp tamper control,
  §5 the pin surface, §Owed 6 the roster defect); `reports/round-38/depth/D05-verify.md` §4 (the
  `bbe15887…` r7 baseline pin); `reports/round-38/scribe/S02-telemetry-draft.md` §2/F2 (undeclared `A`
  block — independently found); `reports/round-38/cross/X02-honesty.md` §4a/§4b (the roster class is
  not r7-only — reproduced here).
- Boundary: `PROVINCE.md:9-11,22-25`; `AGENTS.md:15-31` (telemetry content rules);
  `corpus/knowledge/verification/gate-frozen-run-standard.md:74` (via A01 §3a: baselines are never
  rewritten to match a new run).
