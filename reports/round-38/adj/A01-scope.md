- Seat: A01 | executor | claim A | date 2026-10-19 | baseline 9bccc9b

# A01 — scope watch + bleed scan

## Verdict

**PASS for the Git-visible scope boundary, with one measured bleed risk and one
named-artifact ambiguity routed.**

The inspected HEAD is the declared baseline `9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26`;
`git diff --name-status 9bccc9b` is empty and every untracked path is under
`reports/round-38/` (6 paths at the final sample). No filed round, `corpus/lessons/`
or `tools/gates/frozen/` byte has moved.

The round's two claims declare that tool/example changes are drafted, not applied,
and that exactly **two** artifacts may move. This seat measured what happens if the
integrator applies the drafts. The result is the round's real scope hazard: **the D
block's law-gate edit turns a filed frozen pin red, and the O block's read-set edit
breaks the r7 default chain.** Both are recoverable, but neither is inert. Details in
§3; the gate behavior is not documented anywhere in the round's records.

## 1. Baseline boundary census (measured)

| surface | command | result |
|---|---|---|
| baseline | `git rev-parse HEAD` | `9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26` |
| tracked drift | `git diff --name-status 9bccc9b` | empty |
| untracked scope | `git status --porcelain --untracked-files=all` | 6 rows, all `?? reports/round-38/…` |
| filed rounds | `git diff --name-status 9bccc9b -- reports/round-1…round-37` | empty |
| protected corpora | `git diff --name-status 9bccc9b -- tools/gates/frozen/ corpus/lessons/` | empty |
| r7 pin pair | `sha256sum reports/round-34/handoff/declared-in-r7/*` | packet `45f57132…`, twin `0e229138…`, expected `bbe15887…` — unchanged |

Protected inventories at baseline: 237 tracked files under `tools/gates/frozen/`,
179 tracked files under `corpus/lessons/`. `reports/round-34/handoff/declared-in-r7`
carries six files; all six digests are recorded in `## Citations` so a later
in-place edit is detectable.

## 2. Bleed scan over the landed round-38 drafts

At the final sample the round-38 tree held six files: `claims.json`, `targets.json`,
two telemetry records, and two peer fragments (`adj/A03-verify.md`,
`scribe/S02-telemetry-draft.md`). The 30 build seats' `out` paths had not landed.

- **Cross-domain / corpus language: clean.** Neither landed fragment edits or
  proposes to edit a corpus entry, a lessons file, or the world bible.
- **Credential sweep: clean.** No `bearer`, `authorization`, `api-key`, `secret`,
  `password` or token value appears in any round-38 byte. The only `oauth`
  occurrences are the lane name `xai-oauth` (`claims.json:8`).
- **Out-of-province claims: none.** The only `promot` hit is a negation
  (`scribe/S02-telemetry-draft.md:367`, "must never be promoted into"); no canon,
  clearance, promotion or closure verdict is claimed by any landed byte.
- **Freshness pause: held.** `freshness_pause_in_force: true` (`claims.json:11`) and
  the `no freshness axis-move` non-goal (`:26`) are both present.
- **Owed close-time artifacts named but absent** (consistent with an open round, not
  a defect): `reports/round-38/availability.json`, `reports/round-38/kotodama.md`,
  `reports/round-38/run-validation.py` — all three absent. `scribe/S02-telemetry-draft.md:412-414`
  flags the `availability.json` name as a round-30 decoy and the runner as absent.
- **Contested scope carried, not absorbed.** The live contract digest question
  recorded at `reports/round-37/adj/A04-contested.md` is untouched by round 38.

## 3. Measured blast radius of the two declared edit surfaces

This is the round's scope hazard, and it is the part no other seat measured. Method:
`git archive HEAD` copy under `.scratch/r38-A01`, edit applied **only in the copy**,
never in-tree; `reports/round-*/run-validation.py` was never executed. Each experiment
was reverted by re-extracting the file from `HEAD` and the digest re-checked.

**3a. D block — editing `tools/gates/register-law-gate.py` reds a filed pin.**

The gate is pinned by `tools/gates/expected/register-law-gate/r30-post/expected.json`
at `gate_sha256: 15f8b232…`, byte-identical to the live script. `check-gate-battery.py`
covers it as a `BASELINE_ONLY_GATE_NAMES` member (`tools/check-gate-battery.py:130-132`)
and classifies any digest mismatch as `BASELINE-GATE-REVISED` → exit 2
(`:541-544`). Measured in the isolated copy:

```
pristine:  python3 -B tools/check-gate-battery.py  -> battery_exit 0, pass 7, unevaluable 0
           readings {"pinned": 20}
appended 1 comment line to tools/gates/register-law-gate.py (sha -> 07a99897…):
           python3 -B tools/check-gate-battery.py  -> battery_exit 2, pass 7, unevaluable 0
           readings {"gate_revised": 1, "pinned": 19}
           BASELINE-GATE-REVISED: gate_sha256 15f8b23251ca2ad0… differs from the live
             register-law-gate.py 07a998979d7cef60…: re-freeze, never compare across
             an unnamed revision
```

Per the standard's append-only rule (`corpus/knowledge/verification/gate-frozen-run-standard.md:74`:
"Existing baselines are never rewritten to match a new run") the r30-post baseline must
**not** be repointed. So the D block's law-gate leg, if applied, converts a currently
green battery into an exit-2 reading until a **new** baseline id is filed beside
r30-post. The D claim's `after_required` (`claims.json:16`) asks only that
"argot/law/typed legs green" and that "filed bytes [be] untouched", and no landed
round-38 byte draws the consequence: `depth/D07-receipt.md:259` records the r30-post
pin as "identical / current" without stating what a gate edit does to it, and
`depth/D07-receipt.md:377` reads the battery only as evidence that the *argot* gate is
unregistered. So the round understates the D block's cost: applying the law-gate leg
buys the RL-8 era check at the price of a red battery row until a new baseline id is
filed. This is the reason the O block's "zero freeze bytes moved" (`claims.json:22`) is
necessary but not sufficient.

**3b. D block — the argot gate has a narrower blast radius.** Appending the same
comment to `tools/gates/argot-derivation-gate.py` left the battery at `battery_exit 0`,
`readings {"pinned": 20}`, 0 findings, and left `typed-pipeline-gate.py` at 20/20 exit 0.
The argot gate's sha `b5406bcd…` is pinned by **no** `expected.json`
(`grep -rl b5406bcd tools/ reports/round-9` → no match); it is consumed live
(`tools/gates/typed-pipeline-gate.py:84,525-526,1399`). Its `--selftest` (27/27) and the
law gate's `--selftest` (45/45) both stayed green under the edits, which confirms the
selftests are not the instrument that catches a gate revision — the battery pin is.

**3c. O block — adding the 13th read-set member breaks the r7 default chain.**

Adding `examples/culture-d4/components/13-register-law.yml` to `D4_COMPONENTS`
(`tools/exercise-handoff-e2e.py:157-170`) was measured in the isolated copy:

```
python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet
  -> exit 1
     E2E-DIGEST: the assembled packet does not match the frozen packet digest
     packet_sha256=(not assembled)
```

Mechanism, read from the source: the assembled packet embeds the component digests
(`examples/culture-d4/packet.d4.yml:2875-2888`), so a read-set member changes the
assembled packet; `assert_manifest_equality` re-measures the packet's own
`artifact_manifest` and asserts `checked == len(V3_READ_SET)`
(`tools/exercise-handoff-e2e.py:3661-3662`); and the v3 leg compares the assembled
digest to the frozen one (`:3951-3956`). The r7 chain therefore cannot absorb a 12→13
read-set change; the O claim's fix route must be **re-freeze as a new baseline row**,
which the claim already declares as its route (`claims.json:21-22`, "no re-freeze this
round") and which the r7 pair's own `freeze.txt` shows as the established pattern
(`re-freeze ... -> ...` lines).

**3d. The guard the O claim asks for cannot catch a live-side addition.** The existing
roster guard is one-directional: it iterates `baseline["inputs"]` and names members
missing from the **live** read set (`tools/exercise-handoff-e2e.py:3826-3838`,
`E2E-READSET`). A live-only 13th member is invisible to it — the inverse direction,
which is exactly the r7 defect's shape (the baseline omits a member the packet's
manifest records). So the new guard must check live-side members against the frozen
set, and §3c shows that a guard which *refuses* on that condition will fire on the
r7 row; §3a shows a gate revision is caught by the battery instead. A guard that
**names** without refusing (the shape `claims.json:20` allows: "refuses or names")
keeps the r7 default chain at exit 0. This is the load-bearing constraint for the O
block and it is `to-verify` against O01/O02 until those land.

## 4. Routed ambiguity — "the two named tool/example artifacts"

The D claim's `after_required` says "filed bytes untouched except the two named
tool/example artifacts" (`claims.json:16`) and its non-goal says "no filed byte
rewrites beyond the two named artifacts" (`:27`), but **no round-38 byte names which
two** (`grep -rn "two named" reports/round-38/` → only those two occurrences, no
roster). The plausible readings are `{argot-derivation-gate.py,
register-law-gate.py}` (the two register legs) or `{argot-derivation-gate.py,
typed-labels.d4.yml}` (the gate plus the counter's projection, since the F-6 counters
must "emit from the packet/components"). Both readings are inside the lane's
PROVINCE scope, so this is not an out-of-province item — it is an **unbound
declaration** that a later seat or the integrator should pin before applying drafts.
I do not decide it; I record that the claim text alone cannot be checked against it.

## 5. Record-shape rulings A02 asked this seat to make

`reports/round-38/adj/A02-receipt.md:160-164` routes two items to A01 as "declaration/
record-shape items inside A01's mission" that A02 "can name but cannot adjudicate". This
seat's mission is "scope watch + bleed scan over the round's drafts" (`targets.json:156`),
so both fall inside it. Measured rulings:

- **F-A02-1 (undeclared `A` claim id) — confirmed, and it is a scope-watch item, not a
  scope violation.** `claims.json` declares `axes_in_play: ["depth", "operability"]` and
  claim ids `["D", "O"]` only; `targets.json` carries three seats with `claim: "A"`
  (A01/A02/A03). This is a declaration-form gap (32 seats == 32 out paths; no seat is
  missing and no axis is claimed in the round's `claims.json`), not an out-of-lane
  write. **Disposition: routed, not absorbed** — whether the A block is a watch-only
  posture or an undeclared claim is the integrator's/operator's call. I do not invent a
  claim, and I do not treat the A seats' fragments as carrying an axis-move verdict.
  A02 reached the same reading independently (`adj/A02-receipt.md:90-97`); this is a
  second, independent confirmation of the same measurement, not a new finding.
- **F-A02-2 (README placeholder row vs duplicate heading) — the live defect is real and
  is on a corpus surface.** `corpus/README.md:1` and `:3` both carry the H1
  `# kotodama-shokunin corpus index` (measured with `sed -n '1,5p'` and `cat -A`), so
  the file opens with two identical top-level headings separated by one blank line.
  The file is tracked and **unchanged** at baseline (`git diff --name-status 9bccc9b --
  corpus/README.md` → empty), which is the right state for a watch seat: I neither edit
  it nor claim it as this round's. It is a genuine corpus-surface defect needing an
  owner. **Disposition: routed.** This is *not* an out-of-province item — `corpus/` is
  inside this lane's PROVINCE scope — but a corpus README edit is an integrator-applied
  change, not a watch seat's write, and the round's non-goals forbid filed-byte rewrites
  beyond the two unnamed artifacts. Owner: integrator (a one-line heading removal, or a
  recorded no-fix with reason).

## Owed

- **Integrator, at apply time:** before applying the D law-gate draft, file a **new**
  `tools/gates/expected/register-law-gate/<new-id>/` baseline (never repoint r30-post),
  or accept and record the battery `gate_revised` exit 2 as a declared round artifact.
  Evidence: §3a.
- **Integrator, at apply time:** the O guard must keep the r7 default chain at exit 0
  (name-only on the live-vs-frozen direction, §3d); a refusing guard reds the filed
  chain per §3c.
- **Integrator / a later seat:** bind "the two named artifacts" to an explicit roster
  (§4). Unresolvable from round-38 bytes as filed.
- **Integrator:** rule on F-A02-1 (A-block declaration form) and fix-or-record F-A02-2
  (`corpus/README.md` duplicate H1 at `:1`/`:3`). Evidence: §5.
- **This seat did not verify:** any D/O draft's correctness (none had landed), the
  `run-validation.py` legs (absent; and per F-C13-1 not runnable in-tree), and any
  untracked filesystem write outside the repository — the Git census cannot observe
  those.

## Citations

Files (sha256 measured 2026-10-19, cwd = lane root, `TMPDIR=$PWD/.scratch
PYTHONDONTWRITEBYTECODE=1`):

```
9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26                                   git rev-parse HEAD
45ff6f202a56704209144a6f5031a8c2f44a6dfd6ecd3d608cf26db8f793615d  reports/round-38/claims.json
fe3091b91623f47211d673070f7c3d9fac3711c1375361cd27de246c10f7c601  reports/round-38/targets.json
531b2dfa3b619dbba054098f27ed3335f24314ac6aca2288741c46106eb601eb  reports/round-38/telemetry/availability-attempt-1.json
7112af756da589ea359111feb5b2e9ef4b5266566672e16d4e46c2fca8f4599f  reports/round-38/telemetry/dispatch-declared.json
bfe1c78e479f74784e3d2b53b053b43cd8333214c46bcc8b908b3b45ebff0aa9  tools/exercise-handoff-e2e.py
15f8b23251ca2ad0a203bb1ed5fda2611dff9514e6a1af8120f520b1e7ec4169  tools/gates/register-law-gate.py
b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb  tools/gates/argot-derivation-gate.py
aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3  examples/culture-d4/packet.d4.yml
c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7  examples/culture-d4/components/13-register-law.yml
45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19  reports/round-34/handoff/declared-in-r7/packet.md
0e22913850cd85bc393fe6d0d7a8bf448e9b253aa2884457d4c8999ac9096599  reports/round-34/handoff/declared-in-r7/twin.json
bbe15887b710bb36def5e1c82fa5b1c1ef37df3cb5581c7c2982a0498e829d55  reports/round-34/handoff/declared-in-r7/expected.json
3969954bd817f5ab00137c018c82d6642fa15ac8dedc856ff1b761c9716c1223  reports/round-34/handoff/declared-in-r7/freeze.txt
d181de28ccafda2d34e40277a5390f7e42c64247fbbdcdec3df9a592aa48980c  reports/round-34/handoff/declared-in-r7/claims-map.md
ffae4ecdcf2558693e9ace21e918572e84d6be6607a5b8a5284805ab7e11136c  reports/round-34/handoff/declared-in-r7/run.log
```

Commands run (all from the lane root unless noted; every gate/experiment ran in a
`git archive HEAD` copy under `.scratch/r38-A01`, never in-tree):

```
git rev-parse HEAD                                                        # 9bccc9b…
git diff --name-status 9bccc9b                                            # empty
git status --porcelain --untracked-files=all                              # 6 rows, all reports/round-38/
git diff --name-status 9bccc9b -- tools/gates/frozen/ corpus/lessons/     # empty
python3 -B tools/check-gate-battery.py                                    # battery_exit 0, pass 7, unevaluable 0
python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet             # exit 0, packet 45f57132…
python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml   # 20/20, exit 0
python3 -B tools/gates/register-law-gate.py --selftest                    # 45/45
python3 -B tools/gates/argot-derivation-gate.py --selftest                # 27/27
# isolated experiments (copy only):
#   append 1 line to tools/gates/register-law-gate.py  -> battery exit 2, {"gate_revised":1,"pinned":19}
#   append 1 line to tools/gates/argot-derivation-gate.py -> battery exit 0, {"pinned":20}
#   add 13th member to D4_COMPONENTS -> v3 --quiet exit 1, E2E-DIGEST
#   revert each by `git show HEAD:<path> > <path>`; digests re-checked to baseline
git diff --name-status 9bccc9b -- corpus/README.md                        # empty (README unchanged)
sed -n '1,5p' corpus/README.md                                            # H1 duplicated at :1 and :3
python3 -c 'import json; d=json.load(open("reports/round-38/claims.json")); print(d["axes_in_play"], [c["id"] for c in d["claims"]])'
                                                                          # ['depth','operability'] ['D','O']
```

Source lines cited: `reports/round-38/claims.json:8,11,16,20-22,26-27`;
`reports/round-38/targets.json:3-8,156`;
`reports/round-38/adj/A02-receipt.md:90-97,160-164,186-191`;
`corpus/README.md:1,3`;
`tools/check-gate-battery.py:117-132,146-150,541-547,760-790`;
`tools/exercise-handoff-e2e.py:157-170,1939-1953,3661-3662,3826-3838,3951-3956`;
`tools/gates/typed-pipeline-gate.py:84,525-526,1399`;
`examples/culture-d4/packet.d4.yml:2875-2888`;
`corpus/knowledge/verification/gate-frozen-run-standard.md:74`;
`reports/round-37/adj/A04-contested.md`; `reports/round-38/adj/A03-verify.md`;
`reports/round-38/scribe/S02-telemetry-draft.md:367,412-414`.
