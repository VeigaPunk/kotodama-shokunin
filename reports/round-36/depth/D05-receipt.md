- Seat: D05 | executor | claim D | date 2026-10-19 | baseline ce103bf

# D05 — depth receipt: claim D before→after with the counting commands

**Assignment** (`reports/round-36/targets.json:21`, seat D05): *"Depth receipt draft with the
before->after and counting commands."* Out path: `reports/round-36/depth/D05-receipt.md`.
Binding shared rules read at `reports/round-36/targets.json:4-9` — `:4` write only the assigned out
path under `reports/round-36/`; `:5` never edit filed bytes (`reports/round-1..35/**`,
`corpus/lessons/*.md`, `tools/gates/frozen/**`, fleet `.ufo/**`); `:6` corpus/tool changes are
DRAFTED as fenced blocks and applied by the integrator; `:7` no git commits/pushes/installs/network;
`:8` **ABSOLUTE**: never execute any `reports/round-*/run-validation.py` in-tree (F-C13-1), and any
`--freeze` of `reports/round-34/handoff/declared-in-r7` is forbidden; `:9` every claim cites
file:line or command output, unknowns are `to-verify`, never fabricate.

**Status: DRAFT.** Every *before* figure below is a live measurement taken by this seat in the
window named in §2. Nothing was landed by this seat: no packet byte, no component byte, no tool
byte, no pin, no corpus entry. No round runner was executed anywhere, in-tree or in a copy. No
`--freeze` was attempted.

## 0. Headline — the claim's *before* is a reading of a filed record, not of the tree

`reports/round-36/claims.json:18` declares claim D's before-state as *"Register-form domain empty
(reports/round-25/argot/ + SCORECARD r25 row); register law/strata exist but the form class has no
instances"*, and `:17` says the round exists to *"Close the r25 empty-domain record"*.

**That before-state is stale.** It is an accurate quotation of the r25 filed record
(`SCORECARD.md:312`, `reports/round-25/argot/delta.md` §8.3) and it was an accurate measurement of
the tree on 2026-10-18. It was closed **the very next round, by round 26**
(`SCORECARD.md:329`) — ten rounds before this one — and it is **false of the baseline this round
runs on** (`ce103bf`).

Measured live at `ce103bf`, the D4 packet carries the register-form domain in full:

```
$ python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
coverage: examples/culture-d4/packet.d4.yml records=187 register_scoped=14 derived_pairs=8
          claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0
dependency: tools/gates/naming-collision-gate.py sha256 d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d
exit=0
```

`derived_pairs=8` against r25's `derived_pairs=0`. The eight register forms
(`tuum/kit/lom/nees/huum/mees/reek/saam`) are delivered records in
`examples/culture-d4/packet.d4.yml:1009-1183`, authored in
`examples/culture-d4/components/04-lexicon.yml:236-243`, and fixed by the authoritative table at
`reports/round-26/register/forms.md:23-32`.

**Consequence for claim D's `after_required` (`reports/round-36/claims.json:19`).** Every clause of
it is already satisfied on the baseline tree, clause by clause, with the measurement in §3.2. The
round-36 D block's remaining work is therefore **not** "author the register-form content" — that
content exists and is verified. What is genuinely owed is (a) a *re-pin* question the claim raises
in its last clause, and (b) an honest re-scoping of the claim itself, which is the integrator's
call, not this seat's (§5).

## 1. Claim under receipt

`reports/round-36/claims.json:16-21` — claim **D**, axis **depth**:

| field | `reports/round-36/claims.json` | content |
|---|---|---|
| claim | `:17` | Close the r25 empty-domain record: build the register-form domain content into the D4 lineage — the register class was a design forecast whose domain is EMPTY in the delivered packet (r25 recorded "the register-form domain in the delivered D4 packet is EMPTY"). Author register-form component content and the register forms in the packet, re-run the register legs (derivation replay, law gate, typed pipeline), and re-pin as new rows. |
| before | `:18` | Register-form domain empty (`reports/round-25/argot/` + SCORECARD r25 row); register law/strata exist but the form class has no instances |
| after_required | `:19` | register-form domain non-empty with verified forms (derivation replay clean over the new forms; law gate exit 0 over them; typed pipeline holds updated with named gaps); every pin re-frozen as a new row; filed r25-r35 bytes untouched |
| counting_commands | `:20` | `python3 -B reports/round-36/run-validation.py` |
| thresholds | `:21` | forms verified by two independent seats; replay/law/typed legs green; zero filed-byte edits |

Axis-set context (`reports/round-36/claims.json:13`): *"Depth has one regimen-2 claim (r34);
coverage one (r35); calibration two (r33/r34). Depth is the least-claimed axis; claim D works it."*

## 2. Measurement window and state pins

| pin | value | command |
|---|---|---|
| lane root | `/home/vgpnk/Projects/shokunin/kotodama-shokunin` | — |
| baseline | `ce103bf5885af00023cdc4a174c17602476cdcf8` | `git rev-parse HEAD` |
| working tree | clean except this round's own directory: `?? reports/round-36/` | `git status --porcelain` |
| filed surfaces | clean: `git status --porcelain examples/ tools/ corpus/ reports/round-25 reports/round-26 reports/round-27 reports/round-28 reports/round-30` → empty | same |
| env | `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1` | before every scratch-writing command |
| date | 2026-10-19 | session reminder |

Because `git status --porcelain` is empty for every `examples/`, `tools/`, `corpus/` and
`reports/round-1..35` path, **the working tree is byte-identical to HEAD for every surface measured
in this receipt.** That is what makes the digests in §2.1 a recoverable state pin rather than an
assertion.

### 2.1 Digests (every reading below binds to these bytes)

```
sha256sum examples/culture-d4/packet.d4.yml examples/culture-d4/packet.d4.typed.yml \
          examples/culture-d4/typed-labels.d4.yml examples/culture-d4/expected-holds.json \
          examples/culture-d4/components/04-lexicon.yml \
          tools/gates/argot-derivation-gate.py tools/gates/register-law-gate.py \
          tools/gates/typed-pipeline-gate.py tools/gates/naming-collision-gate.py
```

| artifact | sha256 at `ce103bf` |
|---|---|
| `examples/culture-d4/packet.d4.yml` | `aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3` |
| `examples/culture-d4/packet.d4.typed.yml` | `d581e0ad5384ce56622839b6ae4d6cf8b5a4447300cf7d8cd295f3efea0c9182` |
| `examples/culture-d4/typed-labels.d4.yml` | `c23b0ab532cfb9d4bb403405c6996982a447098048e08facbbc9f341ea13f82e` |
| `examples/culture-d4/expected-holds.json` | `e6ae9828d6c82aa6e14431a02840ad565f9f7c30a660afcbed1b1079166bfba3` |
| `examples/culture-d4/components/04-lexicon.yml` | `ed7093d6b92111c2300e7c04b9100f9e57f6d5802101b69335f9fe138858755d` |
| `examples/culture-d4/components/13-register-law.yml` | `c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7` |
| `tools/gates/argot-derivation-gate.py` | `b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb` |
| `tools/gates/register-law-gate.py` | `15f8b23251ca2ad0a203bb1ed5fda2611dff9514e6a1af8120f520b1e7ec4169` |
| `tools/gates/typed-pipeline-gate.py` | `b749ad07cf1710279aea557c071587cf4b3a228a9fb4d03398b4b94d2f32ad85` |
| `tools/gates/naming-collision-gate.py` | `d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d` |

The r25/r26 readings in §0 and §3.1 were taken against **different** bytes — the r25-era packet was
`e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3`
(`reports/round-25/argot/current-state.md` §0; `reports/round-26/register/execution-4.md` §5) and the
argot gate was `5b5abe7865ed906c23fba87fd0dae8b6187c8dfc1a80137adbd364d4d88b0211`
(`reports/round-26/register/review.md` §1). **A digest that differs is a different revision, not a
contradiction** — that distinction is the whole of §3.1.

## 3. Before → after

### 3.1 Before — as the claim states it, and as it actually was

The claim's before-text (`reports/round-36/claims.json:18`) cites two sources. Both say what the
claim says they say:

| cited source | verbatim | file:line |
|---|---|---|
| SCORECARD r25 row | "the delivered-vs-forecast delta named honestly — the register-form domain in the delivered D4 packet is EMPTY (the register class was design-forecast, never built into components), so the leg stands ready over an empty domain, recorded as such" | `SCORECARD.md:312` |
| `reports/round-25/argot/` | "**F-5 remains vacuous**: the delivered packet has `derived_pairs=0`, so there is no argot form whose check could pass" | `reports/round-25/argot/delta.md` §8.3 |

So the before-text is **faithfully quoted**. It is also **ten rounds out of date**, and the two
records that supersede it are filed in this same repository:

| superseding source | verbatim | file:line |
|---|---|---|
| SCORECARD r26 row | "The round-17 register forecast CLOSED: the `stamp` attestation register lands in the delivered furnace-league tree — 8 verified register forms (tuum/kit/lom/nees/huum/mees/reek/saam) with the discovered axis-to-operation rule (mark->reverse, fire->lengthen), era E1 scoped, derivation replay clean (8 derived pairs, 0 violations over 170 records)" | `SCORECARD.md:329` |
| r26 filed census, pre-landing | "`derived_pairs` | **0**" then, post-landing, "`derived_pairs=8`" | `reports/round-26/register/execution-4.md:44-49` and §3 of the same file |

`reports/round-26/register/execution-4.md` §3 is the instrument that keeps the two readings from
being confused, and it says so itself: *"Both statements are true at once and neither displaces the
other … A reader who runs only the delivered census sees an empty domain and a green gate; a reader
who runs only the candidate census sees 8 pairs and a green gate. The pair of readings is the honest
report."* The round-36 claim's before-text is the **first** of those two readings; the baseline is
the **second**.

This is a **state-drift defect in the round's declaration, not a defect in the round's work**: the
r36 claim was declared at `2026-10-19T09:20:00Z` (`reports/round-36/claims.json:7`) against a tree
that had carried the forms since 2026-10-18 (`reports/round-26/register/repin.json`, `"date":
"2026-10-18"`). It is reported here rather than repaired, per `AGENTS.md` (*"reports contested scope
instead of absorbing it"*): the integrator decides whether to re-scope the claim or to let the D
block stand as a re-verification.

### 3.2 After — measured live at `ce103bf`, clause by clause

Each row of `after_required` (`reports/round-36/claims.json:19`) with the command that grades it.

| # | clause | command | observed | verdict |
|---|---|---|---|---|
| A-1 | "register-form domain non-empty with verified forms" | `python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | `records=187 register_scoped=14 derived_pairs=8 claimed_chains=8 violations=0`, exit 0 | **already satisfied** |
| A-2 | "derivation replay clean over the new forms" | same command | `derived_pairs=8 … violations=0` | **already satisfied** |
| A-3 | "law gate exit 0 over them" | `python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml` | `law_rows=5 identity_rows=8 record_ids=183 registers=17 speaker_tokens=3 force_failures=0 consequence_failures=0 dangling=0 findings=0`, exit 0 | **already satisfied** |
| A-4 | "typed pipeline holds updated with named gaps" | `python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml \| tail -1` | `summary: 20/20 legs passed`, exit 0; the leg list includes `ok L3b-argot` | **already satisfied** |
| A-5 | "every pin re-frozen as a new row" | see §4 | `tools/gates/typed-pipelines.json` `profiles[0]` (generation `round-30-qreg-records`) matches **all five** live digests; `tools/gates/expected/register-law-gate/r30-post/expected.json` pins the live packet `aac91246…` and the live gate `15f8b232…` | **already satisfied** |
| A-6 | "filed r25-r35 bytes untouched" | `git status --porcelain examples/ tools/ corpus/ reports/round-25 … reports/round-35` | empty | **already satisfied** (and this seat wrote none) |

Supporting legs, all green at `ce103bf`:

```
$ python3 -B tools/gates/argot-derivation-gate.py --selftest        # selftest: 27/27 checks passed
$ python3 -B tools/gates/register-law-gate.py --selftest            # selftest: 45/45 checks passed
$ python3 -B tools/gates/typed-pipeline-gate.py --selftest          # selftest: 19/19 checks passed
$ python3 -B tools/gates/lexicon-coverage-audit.py examples/culture-d4/packet.d4.yml   # exit 0, no output
$ python3 -B tools/assemble-culture-d4.py --check                   # packet.d4.yml: byte-identical deterministic assembly
$ python3 -B tools/check-gate-battery.py                            # battery_exit 0, pass 7, fail 0, unevaluable 0
$ python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet
handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4
            v2_subset=equal alias_leg=landed packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19
```

### 3.3 The negative control — the leg is discriminating, not green-by-construction

A green leg over a domain is only evidence if the leg can go red. This seat authored one control in
its own scratch (`TMPDIR=$PWD/.scratch`, `.scratch/d05/neg-tamper.yml`), a copy of the delivered
packet with a single register form tampered (`kit` → `kat`, a wrong `reverse` of `tik`):

```
$ python3 -B tools/gates/argot-derivation-gate.py .scratch/d05/neg-tamper.yml
FINDING D4L-ARGOT-DERIV: FAIL — register-scoped form L-56 'kat' (register 'stamp'): declared chain
  'reverse' applied to 'tik' yields 'kit'; the stated inputs and rules do not yield the candidate
coverage: .scratch/d05/neg-tamper.yml records=187 register_scoped=14 derived_pairs=8
          claimed_chains=8 borrow_pairs=6 violations=1 rule_holds=0
exit=1
```

`violations=1`, `exit=1` on the tampered copy; `violations=0`, `exit=0` on the delivered packet.
**The `derived_pairs=8 / violations=0` reading in A-1 is a real reading.** The same control shape is
filed independently by round 26 at `reports/round-26/validation.json` (`claims.D.measurement.
control_violating_derivation`: `perturbed_pair {id L-56, term kit, wrong_form kit2}`, `exit 1`,
`ids_emitted ["D4L-ARGOT-DERIV"]`) — a **second, independently authored** control on the same leg.

### 3.4 The two-independent-seats threshold (`reports/round-36/claims.json:21`)

The threshold is *"forms verified by two independent seats"*. Round 26 filed four, and this seat read
them (attribution, not this seat's measurement):

| seat | artifact | what it did independently | result |
|---|---|---|---|
| R26-D04 | `reports/round-26/register/review.md` | reviewed the design against the delivered bytes; filed RD-1..RD-6 | *"8 of 8 forms clean, the required control `D4L-ARGOT-DERIV` fires, and with the one new rule declared the leg exits 0"* |
| R26-X60 | `reports/round-26/audit/x60-register-derivation-spotcheck.md` | built its **own** derivation instrument — *"a different YAML parser, a different `head2`/`reverse` implementation written from the round-17 prose, no naming-gate kernel"* | *"reproduces the argot gate's coverage line exactly"*; ran the design end-to-end inside a scratch clone: `derived_pairs=0` → `derived_pairs=8` with zero violations |
| SCRIBE X64 | `reports/round-26/scribe/x64-d4-chain-cold-rerun.md` | cold re-run inside an isolated `git clone --shared`, *"never in the lane worktree"* | reproduced every published probe number exactly, including `probe-rule2-bad.yml` → `violations=1` `D4L-ARGOT-DERIV` |
| R26-D17 | `reports/round-26/gate-tests/D17-typed-gate.md` | re-measured the typed gate against the settled tree | `20/20` legs on the source packet, `L3b-argot` **ok**, `counts {'fail': 0, 'hold': 12, 'note': 0}` == `expected-holds.json` |

X60 and X64 are the load-bearing two: X60 is a **different instrument** (independent parser and
independent operation implementations), X64 is a **different execution environment** (isolated
clone). Both reproduce `derived_pairs=8` on the delivered packet. **The threshold is met by filed
evidence, at round 26, not by this seat.**

### 3.5 What this seat did *not* re-verify

Stated plainly so the receipt is not read as broader than it is:

- This seat did **not** re-author the register forms. It measured the delivered bytes; the
  authorship evidence is round 26's (`reports/round-26/register/forms.md:23-32`,
  `examples/culture-d4/components/04-lexicon.yml:236-243`).
- This seat ran **no** `reports/round-*/run-validation.py`, in-tree or in a copy (shared rule `:8`).
  Every command in §3.2 is a gate, an assembler check, or an audit tool — never a round runner.
- This seat attempted **no** `--freeze` and touched no pin (shared rule `:8`).
- `reports/round-36/run-validation.py` — the claim's own `counting_command`
  (`reports/round-36/claims.json:20`) — **does not exist yet** at the time of writing
  (`ls reports/round-36/` → `claims.json targets.json cov/ cross/ depth/ review/ scout/ scribe/
  telemetry/`). The claim's counting command is therefore **not runnable by this seat**; it is the
  integrating parent's artifact (`reports/round-36/targets.json`, seat S01:
  *"Integration dossier: fleet-report material + validation-leg spec for reports/round-36/
  run-validation.py"*). Recorded under `## Owed`.
- The `registers: L-55..L-62` typed-label classification claim (`SCORECARD.md:329`, *"typed labels
  classify the register forms"*) was **not** independently re-verified here; this seat measured only
  that `typed-labels.d4.yml` contains 8 rows naming `L-55..L-62` in `component`/`field`/`record`
  form. Whether those rows are the *correct* classification is `reports/round-36/review/R01-d-review.md`'s
  assignment.

## 4. The pin surface — what is already re-frozen, and what is not

The claim's last `after_required` clause is *"every pin re-frozen as a new row"*. Measured:

| pin surface | live value | pinned value | state |
|---|---|---|---|
| `tools/gates/typed-pipelines.json` `profiles[0]` (id `d4`, generation `round-30-qreg-records`) — `packet` | `aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3` | identical | **current** |
| … `projection` | `c23b0ab532cfb9d4bb403405c6996982a447098048e08facbbc9f341ea13f82e` | identical | **current** |
| … `expected` | `e6ae9828d6c82aa6e14431a02840ad565f9f7c30a660afcbed1b1079166bfba3` | identical | **current** |
| … `assembler` | `tools/assemble-culture-d4.py` | identical | **current** |
| … `adapter` | `tools/assemble-d4-typed.py` | identical | **current** |
| `tools/gates/expected/register-law-gate/r30-post/expected.json` `inputs` | packet `aac91246…`, gate `15f8b232…` | identical | **current** |
| `examples/culture-d4/expected-holds.json` | `packet_sha256 aac91246…`, `active_pin_generation round-30-qreg-records` | identical | **current** |

Verification command (a digest comparison, not a re-pin):

```
$ python3 -c "import json,hashlib; d=json.load(open('tools/gates/typed-pipelines.json')); p=d['profiles'][0];
  [print(('OK ' if hashlib.sha256(open(p[k]['path'],'rb').read()).hexdigest()==p[k]['sha256'] else 'STALE'), k)
   for k in ('packet','projection','expected','assembler','adapter')]"
OK   packet
OK   projection
OK   expected
OK   assembler
OK   adapter
```

**The superseded pin rows still exist, as rows, and were not edited** — which is what "frozen as a
new row" requires. `tools/gates/typed-pipelines.json` carries a **second** `d4` profile entry (the
round-28 generation, packet `543d68a82640…`) beside the current one; the file's own `note` states the
rule: *"Every field carries the live digest it was pinned at; editing this file cannot silently
re-point a run — a stale pin refuses (exit 2, L1-profile) until it is re-pinned with a command and a
date. No filed receipt is edited by a re-pin; the pins move in this file and are recorded in the
round's fragments."* The same discipline is visible in
`examples/culture-d4/expected-holds.json` (`pin_generations[]` carries both the round-28 and the
round-30 generation; `reports/round-26/register/repin.json` carries `new_pins` beside
`superseded_pins`), and in `reports/round-26/register/repin.json`'s own scope note: *"kind: re-pin of
this seat's own surfaces; the hold ROWS are unchanged, only the digests move"*.

**A-5 is therefore satisfied at the baseline.** No re-pin is owed *by the register stratum*. Whether
any pin is owed by *this round's* work is a function of what the D block actually changes — and on
the evidence in §3, the honest answer is that the register content needs no change at all, so the D
block's output is a **re-verification**, not a re-pin. That is a scope question for the integrator
(§5), not a measurement question.

### 4.1 The frozen generations still carry the superseded digest, and that is correct

`tools/gates/frozen/**` contains **23** occurrences of the r25-era packet digest
`e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3` across four generations:

```
$ for d in tools/gates/frozen/*/; do n=$(grep -rl "e7ecd204" "$d" 2>/dev/null | wc -l); \
    [ "$n" -gt 0 ] && printf "%-40s %s files\n" "$d" "$n"; done
tools/gates/frozen/round-18/             3 files
tools/gates/frozen/round-22/             6 files
tools/gates/frozen/round-25/             3 files
tools/gates/frozen/round-26/             2 files
```

This is **not** a stale pin and **not** a re-pin debt. A frozen generation is an append-only record
of the revision it was frozen at — `tools/gates/frozen/round-26/post-register/` is the generation
frozen *after* the register landing and carries `dd25077bc01681bc17f4586b40cfdd6959d4f45fc63e4f33f13fdc9b2cc88e67`
(the r26 packet digest), while `round-26/gate-input/` carries the pre-landing `e7ecd204…`. Both are
correct for their own generation. Editing them would destroy the record, which is exactly what
shared rule `:5` (`never edit filed bytes … tools/gates/frozen/**`) forbids. **A-5's "frozen as a new
row" is satisfied by the generations that exist; a future landing adds a generation, it does not
rewrite one.**

### 4.2 Post-window observation (not this seat's work)

At this seat's close, `git status --porcelain` returned a second row:

```
 M reports/round-35/validation.json
?? reports/round-36/
```

`reports/round-35/validation.json` was **clean** for the whole of §2's measurement window (§2 pins
`git status --porcelain examples/ tools/ corpus/ reports/round-25 … reports/round-30` → empty) and
was modified afterwards, by another seat or the parent integrating this round. This seat wrote no
byte of it — the diff is `2 insertions(+), 4 deletions(-)`. Recorded here because a reader
re-running §2's pins at a later stamp will see a dirty tree and must be able to tell which row is
this seat's (`?? reports/round-36/`) and which is another actor's. **Every measurement in this
receipt was taken at the clean stamp of §2.**

## 5. Named for the integrator (reported, not absorbed)

`AGENTS.md` requires this lane to *"report contested scope instead of absorbing it"*, and canon
decisions are lore-shokunin's. Four items:

1. **Claim D's before-state is stale and its after-state is already true.** `reports/round-36/
   claims.json:18-19` describe a tree that no longer exists. The evidence is §3.1-§3.2 above. The
   decision — re-scope claim D to a re-verification, restate its before/after against the `ce103bf`
   bytes, or leave it and record the drift — is the integrator's. This seat does not edit
   `reports/round-36/claims.json` (out of its write scope, `reports/round-36/targets.json:4`).
2. **The r25 empty-domain record is closed by r26 and the closure is already on record.**
   `SCORECARD.md:329` and `reports/round-26/register/execution-4.md` §3. If claim D is admitted on
   its current text, the SCORECARD r36 row will record an improvement against a before-state that was
   never true at `ce103bf` — a **false before→after**, which is the failure mode
   `REGIMEN.md` (per-round contract) exists to prevent.
3. **`reports/round-36/run-validation.py` does not exist**, so claim D's declared `counting_command`
   (`reports/round-36/claims.json:20`) cannot be run by any seat. It is owed by the S01 integration
   draft (`reports/round-36/targets.json`, seat S01).
4. **The same falsification was reached independently by five sibling D seats**, so this is not one
   seat's reading. Filed while this receipt was being written: `reports/round-36/depth/D02-packet-draft.md`
   (*"That premise is stale. It was true when round 25 filed it and it was closed by round 26"*),
   `D06-gap-fill.md` §1 (*"claim D's `before` state is stale, and the block must not build on it"*),
   `D07-verify.md` (*"confirmed by my own independent parse"*), `D09-gap-fill.md` §1 (*"the domain was
   filled in r26"*), and `D10-scribe.md`. D06 and D09 are the corroborating pair — both measured the
   premise rather than assuming it, from independently written commands. The integrator has five
   independent witnesses, not one.

## 6. Counting commands for this receipt

Every command below was run by this seat, in this seat's shell, at the revision in §2, with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`. None is a round runner; none writes to the
repo except the scratch control.

```sh
# state pins
git rev-parse HEAD                                    # ce103bf5885af00023cdc4a174c17602476cdcf8
git status --porcelain                                # only "?? reports/round-36/"
sha256sum examples/culture-d4/packet.d4.yml examples/culture-d4/packet.d4.typed.yml \
          examples/culture-d4/typed-labels.d4.yml examples/culture-d4/expected-holds.json \
          examples/culture-d4/components/04-lexicon.yml

# the claim's after_required, clause by clause (§3.2)
python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml    # derived_pairs=8 violations=0, exit 0
python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml        # findings=0, exit 0
python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml | tail -1   # summary: 20/20 legs passed
python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml | grep -i argot  # ok   L3b-argot

# selftests
python3 -B tools/gates/argot-derivation-gate.py --selftest        # 27/27
python3 -B tools/gates/register-law-gate.py --selftest            # 45/45
python3 -B tools/gates/typed-pipeline-gate.py --selftest          # 19/19

# the register forms are delivered records, not forecast
grep -n 'derived_from' examples/culture-d4/packet.d4.yml          # 9 hits: the schema field + 8 records
sed -n '236,243p' examples/culture-d4/components/04-lexicon.yml   # the 8 authored rows

# the negative control (§3.3) — scratch only, the delivered tree untouched
cp examples/culture-d4/packet.d4.yml .scratch/d05/neg-tamper.yml
python3 - <<'PY'
p='.scratch/d05/neg-tamper.yml'; s=open(p).read()
open(p,'w').write(s.replace('term: "kit"','term: "kat"',1))
PY
python3 -B tools/gates/argot-derivation-gate.py .scratch/d05/neg-tamper.yml   # D4L-ARGOT-DERIV, exit 1

# the pin surface (§4)
python3 -B tools/assemble-culture-d4.py --check                   # byte-identical deterministic assembly
python3 -B tools/check-gate-battery.py                            # pass 7, fail 0, unevaluable 0
python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet     # exit=0, packet_sha256=45f57132…
```

## Owed

| # | owed artifact | owner | reason |
|---|---|---|---|
| 1 | `reports/round-36/run-validation.py` | integrating parent / seat S01 (`reports/round-36/targets.json`) | claim D's declared `counting_command` (`reports/round-36/claims.json:20`) does not exist at the time of writing; `ls reports/round-36/` shows no runner. This seat may not execute a round runner in-tree (shared rule `:8`) and has none to execute in a copy. |
| 2 | the re-scope decision on claim D's `before`/`after_required` (`reports/round-36/claims.json:18-19`) | integrating parent | the declared before-state is false of `ce103bf`; `reports/round-36/claims.json` is outside this seat's write scope (`reports/round-36/targets.json:4`). Evidence: §3.1-§3.2. |
| 3 | independent re-verification of the typed-label classification of `L-55..L-62` | `reports/round-36/review/R01-d-review.md` / `R02-d-review.md` | this seat measured that 8 typed rows name those records; whether the classification is *correct* is the D-block reviewers' assignment (`reports/round-36/targets.json`, seats R01/R02). |
| 4 | `head2`'s empty proper domain, the axis→operation rule's non-totality (13 of 54), and the register law's replay coverage | carried from `reports/round-26/register/review.md` RD-2/RD-3/RD-5 | named gaps that the r26 landing recorded and did **not** close; unchanged at `ce103bf`. Not this seat's assignment, listed so the receipt does not read as claiming a closed register program. |

## Citations

Every line reference below was read in this window at the revision in §2.

| # | citation | what it establishes |
|---|---|---|
| 1 | `reports/round-36/claims.json:16-21` | claim D — claim text, before, after_required, counting_commands, thresholds |
| 2 | `reports/round-36/claims.json:7` | `declared_at_utc 2026-10-19T09:20:00Z` |
| 3 | `reports/round-36/claims.json:9-10` | `baseline_commit ce103bf` |
| 4 | `reports/round-36/claims.json:13` | lowest-axis reasoning (depth is the least-claimed axis) |
| 5 | `reports/round-36/targets.json:4-9` | binding `shared_rules` |
| 6 | `reports/round-36/targets.json:21` | seat D05, role executor, claim D, out `depth/D05-receipt.md` |
| 7 | `SCORECARD.md:312` | the r25 row the claim's before-state cites (register-form domain EMPTY) |
| 8 | `SCORECARD.md:329` | the r26 row that closes it (8 verified register forms, `derived_pairs=8`) |
| 9 | `reports/round-25/argot/current-state.md` §0, §4 | r25 digests and the argot token census (`derived_pairs`-era evidence) |
| 10 | `reports/round-25/argot/delta.md` §8.2, §8.3 | the r25 reading of `derived_pairs=0` and its "F-5 remains vacuous" conclusion |
| 11 | `reports/round-26/register/execution-4.md:44-49` and §3 (`:80-95`) | the two-census instrument: delivered `derived_pairs=0` vs candidate `derived_pairs=8` |
| 12 | `reports/round-26/register/forms.md:23-32` | the authoritative 8-form table with base/axis/op/form |
| 13 | `reports/round-26/register/review.md` §1, §8 | R26-D04's independent review; RD-1..RD-6 summary table |
| 14 | `reports/round-26/audit/x60-register-derivation-spotcheck.md` §0, §1 | R26-X60's independent instrument (different parser, different op implementations) |
| 15 | `reports/round-26/scribe/x64-d4-chain-cold-rerun.md` §0, §1b | SCRIBE X64's isolated `git clone --shared` cold re-run |
| 16 | `reports/round-26/gate-tests/D17-typed-gate.md` §0 | 20/20 legs, `L3b-argot` ok, hold counts |
| 17 | `reports/round-26/register/repin.json` | the pin re-freeze as new rows (`new_pins` beside `superseded_pins`), `date 2026-10-18` |
| 18 | `reports/round-26/validation.json` `claims.D.measurement` | the filed 8-pair list, the coverage counters, and the `kit→kit2` negative control |
| 19 | `examples/culture-d4/packet.d4.yml:39-42` | `contract.record_fields.lexicon` already lists `register`, `derived_from`, `derivation`, `doublet_of` |
| 20 | `examples/culture-d4/packet.d4.yml:1009-1183` | the 8 delivered register-form records (`L-55..L-62`) with `derived_from` + `derivation{op,base}` + `register: stamp` |
| 21 | `examples/culture-d4/packet.d4.yml:1329-2472` | the `registers:` block, `QREG-01..08` |
| 22 | `examples/culture-d4/packet.d4.yml:2788` | the `register_law:` block, `RGL-01..05` |
| 23 | `examples/culture-d4/components/04-lexicon.yml:236-243` | the 8 authored register rows, with the comment block at `:220-232` naming the design authority and the gate that replays them |
| 24 | `tools/gates/typed-pipeline-gate.py:80-84`, `:517-537` | the typed gate carries the argot leg as `L3b-argot` (closes r25 `delta.md` §8.3 item 3) |
| 25 | `tools/gates/expected/register-law-gate/r30-post/expected.json` | a frozen row pinning the live packet `aac91246…` and the live gate `15f8b232…` |
| 26 | `tools/gates/typed-pipelines.json` (`note`, `profiles[0]`, `profiles[1]`) | the pin discipline: a stale pin refuses (exit 2), a re-pin is a new row, filed receipts are never edited |
| 27 | `examples/culture-d4/expected-holds.json` | `packet_sha256 aac91246…`, `active_pin_generation round-30-qreg-records`, two `pin_generations` rows |
| 28 | `tools/check-gate-battery.py:117-132` | `GATE_NAMES` / `BASELINE_ONLY_GATE_NAMES` / `REGISTERED_GATE_NAMES`; the battery's gate list is a fixed constant and does not name `argot-derivation-gate.py` (the typed gate is the argot leg's invocation path, not the battery) |
| 29 | `REGIMEN.md:25`, `:41-43` | the per-round contract; "Admit only when every claim verifies and no axis is harmed; otherwise … never force a pass (rounds 11/17/22 precedent)" |
| 30 | `AGENTS.md:10`, `:13` | "Never fabricate domain knowledge or sources: cite a file, a command output, or a source"; "reports contested scope instead of absorbing it" |
| 31 | `reports/round-36/depth/D02-packet-draft.md` §0, `D06-gap-fill.md` §1, `D07-verify.md`, `D09-gap-fill.md` §1, `D10-scribe.md` | the five sibling D seats that reached the same falsification independently (§5 item 4) |
| 32 | `tools/gates/frozen/round-{18,22,25,26}/**` | the append-only frozen generations carrying the superseded `e7ecd204…` digest correctly (§4.1); `round-26/post-register/` carries the r26 `dd25077b…` |

---

*This receipt claims no promotion, no canon, no clearance and no closure. A green gate is a
measurement, not a verdict. The one substantive finding — that claim D's declared before-state is
false of the baseline, corroborated independently by five sibling D seats (§5 item 4) — is reported
for the integrator and deliberately not repaired by this seat.*
