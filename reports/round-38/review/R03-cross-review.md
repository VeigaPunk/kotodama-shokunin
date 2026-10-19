- Seat: R03 | reviewer | cross | date 2026-10-19 | baseline 9bccc9b

# R03 — cross-claim review: the D pins vs the O guard

**Mission** (`reports/round-38/targets.json` seat `R03`): *"Cross-claim review: the D
pins vs the O guard (does the guard's named-row output change any D leg?)"*. Out path
this file only.

**Write scope and isolation.** Only `reports/round-38/review/R03-cross-review.md` was
written. All mutation happened in `git archive 9bccc9b | tar -x` copies under
`.scratch/r38-r03/` (gitignored). No in-tree `reports/round-*/run-validation.py` was
executed, in-tree or in a copy (F-C13-1). No `--freeze` was issued against
`reports/round-34/handoff/declared-in-r7`; the filed pair is byte-unchanged (digests
in §8). Every leg ran with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.
`HEAD` = `9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26`.

---

## 0. Verdict

**Answer to the mission question: no — the guard's named-row output does not change any
D leg, and the D legs do not change the guard's verdict.** The two claims are
*mechanically independent on the r7 row*: the guard reads the read-set roster, the D
legs read the packet and two gates that are not read-set members. Neither consumes the
other's output.

But the review surfaces four things the round's own drafts do not yet state, one of
them decisive:

| id | finding | severity |
|---|---|---|
| **R03-C1** | **The O guard cannot read its manifest from the rendered packet.** The rendered `packet.md` carries 12 D4 component rows; the source packet carries 13. A guard written against the rendered text is **vacuous** — it can never name the r7 member. This is the difference between a guard that works and one that passes forever. | **blocking** |
| **R03-C2** | The guard's *placement* is unconstrained by the measured behavior: a refuse-in-`v3_preflight` guard is **green on the r7 row** (measured, §3.2), while X02 (`cross/X02-honesty.md`) asserts the guard "must name" it. Both can be satisfied, but only if the naming happens on a channel the default chain does not run. A1/B1 selftest controls must be defined against that channel, not the exit code. | high |
| **R03-C3** | The D block's route choice is a **pin decision**, and the drafts' preferred gate-route is the only pin-neutral one. The projector route forces a re-freeze of the r7 baseline, which the round's non-goals forbid (`claims.json:26`). Measured cascade in §4. | high |
| **R03-C4** | The D and O blocks share exactly **one** artifact on the r7 read set — `examples/culture-d4/typed-labels.d4.yml`. The D block can touch it only by taking the forbidden route; the O block's fix route does not touch it this round. So there is no mutual interference, and the pins cascade is one-directional. | informational |

This fragment does not certify either claim. Both remain **partial**: the round's
`reports/round-38/run-validation.py` does not exist (`ls` → No such file or directory),
so claim D's third declared counting command and both claims' threshold command are
`to-verify` regardless of what lands.

---

## 1. Method

Pristine control first, so every later red is attributable. Isolated copy
`.scratch/r38-r03/ctrl` = `git archive HEAD | tar -x`, unmodified:

```
$ python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet
handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27
  statuses=16/7/4 v2_subset=equal alias_leg=landed
  packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19   exit 0
$ python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
coverage: … records=187 register_scoped=14 derived_pairs=8 claimed_chains=8
  borrow_pairs=6 violations=0 rule_holds=0                                        exit 0
$ python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml
coverage: … law_rows=5 identity_rows=8 record_ids=183 registers=17 speaker_tokens=3
  force_failures=0 consequence_failures=0 dangling=0 findings=0                    exit 0
```

All three green, packet `45f57132…` reproduced. Matches D03 §1 and A01 §3c.

---

## 2. The collision model — what each block actually touches

### 2.1 D block — three candidate hosts, one read-set membership

| candidate host for the F-6 counters / era leg | in `V3_READ_SET`? | in `typed-pipelines.json`? | battery-registered? |
|---|---|---|---|
| `tools/gates/argot-derivation-gate.py` (sha `b5406bcd…`) | **no** | no | **no** |
| `tools/gates/register-law-gate.py` (sha `15f8b232…`) | **no** | no | **yes** (`expected/register-law-gate/r30-post/expected.json:10`) |
| `tools/d2-typed-labels.py` (sha `2819f687…`) | **yes** (`expected.json:176`) | **yes** (`profiles[0].assembler`… see §4) | n/a |

Measured with `python3 -c` over `expected.json["inputs"]` and the live digests:

```
PINNED  examples/culture-d4/typed-labels.d4.yml   c23b0ab532cfb9d4…   (expected.json:161)
PINNED  examples/culture-d4/expected-holds.json   e6ae9828d6c82aa6…   (expected.json:158)
PINNED  tools/d2-typed-labels.py                  2819f68769dfc0b5…   (expected.json:176)
free    tools/gates/argot-derivation-gate.py
free    tools/gates/register-law-gate.py
free    tools/gates/typed-pipeline-gate.py
free    tools/exercise-handoff-e2e.py
```

So the D block is **pin-neutral if and only if** both residues land in the two gates —
which is exactly the route D03 §5.2 and P01 §0 already measured and recommend. This
review independently confirms it (§4) and adds the failure mode for the other route.

### 2.2 O block — the guard reads the roster, not the packet

The existing roster guard is **one-directional** and reads only `baseline["inputs"]`:

```
tools/exercise-handoff-e2e.py:3823-3836
    dropped = sorted(rel for rel in baseline["inputs"] if rel not in assembly.digests)
    … raise Failed("E2E-READSET", "… are not in the live read set: …")
```

A live-only 13th member is invisible to it. The new guard must walk the **other**
direction (live manifest members ∖ frozen inputs), and that is the direction the r7
defect has. Confirmed independently by A01 §3d.

### 2.3 Independence on the r7 row

The guard compares `V3_READ_SET` against the frozen `inputs` map. The D legs run
`argot-derivation-gate.py` / `register-law-gate.py` / `typed-pipeline-gate.py` over
`examples/culture-d4/packet.d4.yml`. These sets do not intersect — verified by
inspection of `tools/exercise-handoff-e2e.py` (no `argot`, `register-law`, or
`register_law` token anywhere in the file):

```
$ grep -n "argot\|register-law\|register_law" tools/exercise-handoff-e2e.py
(no output)
```

The v3 renderer never runs the argot or law gate. So the guard's output cannot reach a
D leg, and a D-leg result cannot move the guard. **The mission question answers no by
construction, not by luck.**

---

## 3. R03-C1 (blocking) — the guard's text source is load-bearing

### 3.1 The rendered packet does not carry the 13th component

The claim (`claims.json:20`) says the guard compares *"a frozen baseline's read set and
the packet's own component manifest"*. That phrasing admits two sources, and only one
of them works.

```
$ python3 -c "<source_sha256-indent regex over both files>"
source examples/culture-d4/packet.d4.yml, indent-4 digest pairs : 13
rendered reports/round-34/handoff/declared-in-r7/packet.md      :  0
rendered packet.md, markdown-table manifest rows                : 59
  of which examples/culture-d4/components/ rows                 : 12
  13-register-law present among them                            : False
  12-provenance   present among them                            : True
```

The rendered manifest is a **markdown table** (`packet.md:39` onward, rows `A-01`…
`A-59`; the D4 components are `A-34`…`A-45`). The 13th component is absent from it. A
guard that parses the rendered `packet.md` — the natural reading of "the packet's own
component manifest" if the implementer works from the frozen artifact — would compare
12 rows against 58 inputs, find nothing missing, and **pass on the r7 row forever**.

### 3.2 The source packet does carry it, and the renderer already mines it

```
$ python3 -c "<runpy v3_mine_d4, compare to V3_READ_SET>"
v3_mine_d4 components                        : 13
13-register-law in mined components          : True
V3_READ_SET members                          : 58
mined-but-not-in-read-set                    : ['examples/culture-d4/components/13-register-law.yml']
```

`v3_mine_d4` (`tools/exercise-handoff-e2e.py:2045-2056`) already extracts all 13 from
`assembly.source_sha256` and `v3_verify_component_digests` (`:2208-2222`) already
measures all 13. **The correct guard point is one line beside the existing check**:

```
tools/exercise-handoff-e2e.py:3823  (existing, one direction)
    dropped = sorted(rel for rel in baseline["inputs"] if rel not in assembly.digests)
```

The new guard should read the same `assembly.digests`-style map that `v3_mine_d4`
produced — i.e. the **source packet's** `assembly.source_sha256`, not the rendered text.
Drafting guidance, not a patch (integrator applies).

### 3.3 The trap, stated

> If the O guard is written against the rendered `packet.md`, its r7 control goes
> **green**, and the round will read that green as "the guard works". The measured
> truth is the opposite: green there means the guard is blind to the very defect it was
> written to name.

The `>=2 selftest controls` the claim requires (`claims.json:21`: *manifest-member-not-
in-readset named; in-sync green*) must therefore be defined over the **source-packet**
channel. A control built on the rendered channel will pass the "named" half by
accident only if the fixture differs from the live tree — which is precisely the
false-green to avoid. X02 (`cross/X02-honesty.md` §3) independently flags that the O
claim's "only the r7 row names" is false as written; C1 explains *why* an implementer
would land the vacuous version and believe it correct.

---

## 4. R03-C3 — the D block's route choice is a pin decision

Measured cascade in `.scratch/r38-r03/expF` and `expG` (isolated copies). Route A is
the forbidden one; route B is the recommended one.

### Route A — emit the F-6 counters from the projector (the "packet/components" reading)

`derived_forms`/`derived_ok` have exactly one coverage block in the tree, and it is
produced by the projector:

```
tools/d2-typed-labels.py:2879-2895   coverage = { "typed_labels": …, "labels_by_kind": …,
                                     "rank_rules_component": …, "reconciliation_records": …,
                                     "conflicts": …, "findings_total": …, "findings_hold_or_fail": … }
```

Patch that block, then run the sanctioned regeneration chain. Each step reds a
different filed pin:

| step | command | result |
|---|---|---|
| 1 | patch `tools/d2-typed-labels.py` coverage block | — |
| 2 | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` | exit 1 · `E2E-DIGEST: expected-holds.json projector_sha256: the tree recorded 2819f687… but the bytes measure 0309e45e…` |
| 3 | `d2-typed-labels.py --packet … --emit typed-labels.d4.yml` then repin `expected-holds.json` | — |
| 4 | `assemble-d4-typed.py --check` | `FAIL projection_freshness: stale projection pin: projection records … packet hashes aac91246…` |
| 5 | `assemble-d4-typed.py --emit packet.d4.typed.yml` | wrote 108251 bytes |
| 6 | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` | exit 1 · `E2E-UNC: the D4-CL08 landed form is not backed by this run: the alias witnesses are red (tools/d2-typed-labels.py --selftest exit 1; …)` |
| 7 | `d2-typed-labels.py --selftest` | `selftest: 162/163 checks passed — failures: boundary compatibility: D2 projection keeps its exact baseline digest` |
| 8 | re-freeze `.scratch-newbase` | **refused**: `could not freeze: E2E-UNC the D4-CL08 landed form is not backed by this run` |

Step 7 is the decisive one. The projector carries a **hard-coded digest control**:

```
tools/d2-typed-labels.py:3114-3115
        check("boundary compatibility: D2 projection keeps its exact baseline digest",
              hashlib.sha256(ns["serialize"](d2)).hexdigest()
              == "a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43")
```

Any projector edit that changes the serialized D2/D4 projection breaks a pinned
selftest control, which the renderer treats as a **landed-form witness**
(`tools/exercise-handoff-e2e.py:3472-3477`, `v3_selftest_witness` requires
`checks == total >= minimum`; the witnesses are `d2-typed-labels.py --selftest` (min 50)
and `assemble-d4-typed.py --selftest` (min 12), `:3547-3556`). So route A does not
merely move pins — it **cannot re-freeze at all** without also repairing that control,
which is itself a second, unclaimed change to a pinned tool.

**Verdict on route A:** it moves `typed-labels.d4.yml`, `expected-holds.json`,
`packet.d4.typed.yml`, `tools/d2-typed-labels.py`, the r7 `packet_sha256`/`twin_sha256`,
`typed-pipelines.json profiles[0]`, and breaks a pinned selftest. It is not available
this round.

### Route B — emit from the gate's own coverage line (the D03/P01 route)

D03 §5.2 measured this route moves **no** packet, projection, or pin byte. This review
confirms the membership half (§2.1) and notes the consequence for the pins cascade:

- `argot-derivation-gate.py` — not in `V3_READ_SET`, not in `typed-pipelines.json`, not
  battery-registered (`grep -rl b5406bcd tools/ reports/round-9` → no match, per A01
  §3b). **Pin-neutral.**
- `register-law-gate.py` — not in `V3_READ_SET`, but **battery-registered** via
  `tools/gates/expected/register-law-gate/r30-post/expected.json:10` (`gate_sha256
  15f8b232…`). Editing it flips `check-gate-battery.py` to exit 2 with
  `BASELINE-GATE-REVISED` until a **new baseline id** is filed beside `r30-post`.
  Confirmed by A01 §3a and D03 §5.1 from independent samples.

So the RL-8 leg owes one new-row baseline and the F-6 leg owes none. The r7 packet pin
`45f57132…` is untouched by either.

### The consequence the claim should state

Claim D's `after_required` (`claims.json:16`) says *"filed bytes untouched except the
two named tool/example artifacts"*. Under route B the two artifacts are the two gates,
neither of which is a filed round-1..37 byte — consistent. Under route A the statement
is false. **The claim is satisfiable, but only on route B**, and the round's drafts
should say so explicitly rather than leaving the route to the integrator. This is the
one place where R03's answer to the mission question is "no, but conditionally".

---

## 5. R03-C2 — the guard's placement and the channel it names on

Measured in `.scratch/r38-r03/expH`: a roster guard inserted at the top of
`v3_preflight` (`tools/exercise-handoff-e2e.py:3295-3298`), checking source-packet
manifest members against `read_set_paths`:

```
$ python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet
handoff-v3: exit=0 fields=16/16 … packet_sha256=45f57132…   exit 0
```

**Green on the r7 row.** That is the correct outcome for the *default chain* — the
round's non-goal is that the r7 default chain still exits 0 unchanged
(`claims.json:22`) — but it means the guard's "named" half is **not observable from the
exit code**. Compare `v3_freeze` (`:3997-4005`), which calls the same `v3_preflight`:
if the guard *refuses* there, `--freeze` aborts and the fix route (re-freeze absorbs
the member) becomes unreachable — the guard would prevent its own remedy.

Therefore the guard must be **non-refusing on the read-set side** and name the member
on a diagnostic channel, and the two selftest controls must assert on that channel:

| control | asserted over | expected |
|---|---|---|
| manifest-member-not-in-readset **named** | the guard's own record/diagnostic output | the 13th member appears, exit unaffected |
| in-sync **green** | a synced fixture | no name, exit unaffected |
| r7 default chain unchanged | `--profile v3` exit + packet sha | exit 0, `45f57132…` |
| r7 `--freeze` still reachable | `v3_freeze` path | not blocked by the new guard |

X02 §3 asks for the named row; C2 supplies the constraint that makes the naming
compatible with the r7 row staying green. **Both must hold simultaneously**, and a
guard drafted without this distinction will either red the r7 chain (failing the
claim's own threshold) or name nothing (failing C1).

---

## 6. R03-C4 — the pins cascade, and the one shared artifact

The only artifact on both blocks' paths is the D4 projection:

```
examples/culture-d4/typed-labels.d4.yml   r7 inputs c23b0ab532cfb9d4…   (expected.json:161)
```

- The O guard's **fix route** (add the 13th member to `D4_COMPONENTS`) is measured to
  red the chain on its own — independently reproduced here (A01 §3c matches):

```
$ git archive HEAD copy, +13th member to tools/exercise-handoff-e2e.py:157-170
handoff-v3: exit=1 fields=16/16 … v2_subset=equal alias_leg=landed packet_sha256=(not assembled)
handoff-v3: E2E-DIGEST: the assembled packet does not match the frozen packet digest
```

  Mechanism: the assembled packet embeds the component digests
  (`examples/culture-d4/packet.d4.yml:2875-2888`), and `assert_manifest_equality`
  asserts `checked == len(V3_READ_SET)` (`tools/exercise-handoff-e2e.py:3661-3662`).
  So the fix route is **re-freeze as a new baseline**, which the claim already declares
  and defers (`claims.json:21-22`, "no re-freeze this round"). Zero freeze bytes move
  this round — consistent with the non-goal.
- The D block's **route B** does not touch the projection, so it does not collide with
  the fix route. Route A would, and route A is unavailable (§4).

Net: **the D pins and the O guard share no moving artifact this round.** A future round
that takes the O fix route will move the r7 `packet_sha256`/`twin_sha256`; if the D
route were A, that same re-freeze would also carry the F-6 keys. Recording this so the
integrator sequences them: **land route B first (pin-neutral), take the O fix route in
a round that owns the re-freeze.**

---

## 7. Consumer holes the cross-review confirms (not new claims, but load-bearing)

Two vacuous-pass routes survive both claims as drafted. Both are stated by other seats;
recorded here because they are the reason the cross-claim picture is "independent but
jointly insufficient".

1. **The typed pipeline cannot see a law-gate era finding.** The `L3b-argot` leg filters
   the argot gate's output to one prefix:

```
tools/gates/typed-pipeline-gate.py:530-539
        argot_lines = [line for line in proc.stdout.splitlines()
                       if line.startswith("FINDING D4L-ARGOT-")]
```

   The pipeline does not invoke the law gate at all. A `D4L-LAW-ERA` FAIL therefore
   never reaches `typed-pipeline-gate.py`, and a tampered packet reads green there
   (P01 §6.2, D10b §2-§3). Claim D's `after_required` says *"the era leg runs … typed
   legs green"* — green on the pipeline is **not** evidence the era leg ran.

2. **A key-only emitter passes the letter of F-6.** `derived_forms`/`derived_ok` present
   in a coverage line proves nothing about agreement. D03 §3.1 built the consumer probe
   that refuses a key-only or lying emitter; it lives at `.scratch/d03/` and is
   therefore **not filed**, so as of this review the F-6 threshold has no durable
   instrument. D10b's hole is closed only by a scratch probe.

Neither is a cross-claim defect; both are the reason R03's "no interference" verdict is
not a "both claims are sound" verdict.

---

## 8. Filed-byte integrity

```
$ sha256sum reports/round-34/handoff/declared-in-r7/{expected.json,packet.md,twin.json}
bbe15887b710bb36def5e1c82fa5b1c1ef37df3cb5581c7c2982a0498e829d55  expected.json
45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19  packet.md
0e22913850cd85bc393fe6d0d7a8bf448e9b253aa2884457d4c8999ac9096599  twin.json
$ git status --short
?? reports/round-38/
$ git rev-parse HEAD
9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26
```

`packet.md` `45f57132…` matches `expected.json:192` `packet_sha256`; `twin.json`
`0e229138…` matches `:195`. No filed byte moved. No freeze was issued against the r7
pair at any point in this review.

---

## Owed

- `reports/round-38/run-validation.py` — absent; claim D's third counting command and
  both claims' threshold command are `to-verify` until it lands.
- `reports/round-38/op/O01-guard-design.md` — absent at this review's sample; **R03-C1
  cannot be verified against the actual draft.** If O01 parses the rendered `packet.md`,
  the r7 control is vacuous and the guard must be re-drafted against the source
  `assembly.source_sha256`. This is the review's load-bearing owed input.
- `reports/round-38/depth/D01-f6-design.md`, `depth/D02-rl8-design.md` — absent; the
  route choice (A vs B) in claim D is therefore unverified against the drafts, and
  R03-C3's conditional stands on the route the drafts choose.
- `reports/round-38/depth/D04-pins.md`, `depth/D06-verify-pins.md` — absent; the pins
  census for the D block is owed. This review supplies the membership half (§2.1) and
  the battery-row half (§4) only.
- `reports/round-38/op/O02-isolated.md`, `op/O08-regression.md` — absent; the guard's
  behavior across the r2..r7 filed rows is unverified here. X02 §3 reports a second
  filed row (r6) with the same mismatch; that claim is **unverified by this seat** and
  is carried as `to-verify`.

## Citations

- `reports/round-38/claims.json:13-24,26` — the D and O claim text, thresholds,
  counting commands, and non-goals reviewed here.
- `reports/round-38/targets.json` seat `R03`, `shared_rules` — mission and boundaries.
- `tools/exercise-handoff-e2e.py:157-170` (`D4_COMPONENTS`, 12 members);
  `:1939-1963` (`V3_READ_SET`, 58 members); `:2045-2056` (`v3_mine_d4`, mines 13);
  `:2208-2222` (`v3_verify_component_digests`); `:3295-3298` (`v3_preflight`);
  `:3472-3477` (`v3_selftest_witness`); `:3547-3556` (`d4_legs` witnesses);
  `:3661-3662` (`assert_manifest_equality` count assert); `:3823-3836` (existing
  one-directional roster guard); `:3997-4005` (`v3_freeze` → `v3_preflight`).
- `examples/culture-d4/packet.d4.yml:2875-2888` — the 13 `assembly.source_sha256`
  component digests.
- `reports/round-34/handoff/declared-in-r7/expected.json:124-183` (58 inputs);
  `:158,160,161,174,176` (the pinned D4 artifacts); `:192,195` (packet/twin sha).
- `reports/round-34/handoff/declared-in-r7/packet.md:39` onward — the rendered
  markdown manifest table, rows `A-01`…`A-59`, D4 components at `A-34`…`A-45` (12).
- `tools/d2-typed-labels.py:2879-2895` (the only coverage block); `:3111-3117` (the
  pinned D2 baseline digest control).
- `tools/gates/argot-derivation-gate.py:917-920` (the coverage line);
  `tools/gates/typed-pipeline-gate.py:84,525-539` (the `D4L-ARGOT-` filter);
  `tools/gates/register-law-gate.py` sha `15f8b232…`.
- `tools/gates/expected/register-law-gate/r30-post/expected.json:10,19-20` — the
  battery pin on the law gate.
- `tools/assemble-d4-typed.py:127-148` (`projection_fresh`).
- Command/output evidence, all in `git archive 9bccc9b` copies under `.scratch/r38-r03/`:
  pristine `--profile v3` exit 0 `45f57132…`; expF/expG route-A cascade (7 steps,
  including `selftest: 162/163` and the refused re-freeze); expH `v3_preflight` guard
  exit 0; the `+13th member` chain red; the `runpy` component census (13 mined, 1 not
  in read set); the rendered-vs-source manifest regex census (12 vs 13).
- Prior art reviewed and cross-checked: `reports/round-38/depth/D03-isolated.md` §1,§5;
  `depth/D05-verify.md` §0,§2; `depth/D07-receipt.md` §0; `depth/D10b-verify.md` §1-§3;
  `plan/P01-d-plan.md` §0,§6.2; `cross/X02-honesty.md` §0,§3; `adj/A01-scope.md` §3a-§3d;
  `reports/round-37/adj/A01-freeze-adjudication.md`.
