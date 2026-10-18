# R26-X60 — spot-check audit: the register derivations, re-run independently

- Seat **R26-X60** (SCRIBE X60: spot-check auditor — register derivations re-run
  independently). Round 26 (operator: loop 3 of 3, build round 2 of 4; 64 workers
  on `devin/deepseek-v4-1-flash-high` — `reports/round-26/targets.json`:
  D-register 28, O-remainders 12, C-openq 14, X 10).
- Date: **2026-10-18**. Every count below carries its command and date; raw
  receipts live in this seat's scratch (`.scratch/x60/`, gitignored) and only
  this fragment is filed.
- Declared baseline `fc13cd27b9e78d5d7c4f70740fd26c9383a7447b`
  (`reports/round-26/claims.json:5`); lane HEAD `1ad491a1a4b0aef9ebdc1861dfb8237727503825`.
- **Write scope: this fragment and the audit instrument it names, plus scratch.**
  No filed round-8–25 byte is edited; no tool, gate, packet, component, fixture,
  pin or sibling fragment is changed; no Git mutation, commit or push. The
  round-26 runner was never executed in the lane worktree.
- **Independence.** Every command below was run by this seat, in this seat's own
  shell. Sibling fragments are cited as *attribution* (what they claim), never as
  this seat's measurement. Where a sibling's number and this seat's differ, both
  are printed.
- **Canon:** NON-CANON engineering evidence; canon standing is lore-shokunin's.

## 0. Headline

**The register stratum had not landed on disk at this seat's close, so the
derivation surface the round-26 D claim is about did not exist to re-run on the
delivered tree.** This seat therefore did three things instead of grading an
empty domain as clean:

1. it built an **independent** derivation instrument (a different YAML parser, a
   different `head2`/`reverse` implementation written from the round-17 prose, no
   naming-gate kernel) and used it to re-run every derivation the delivered tree
   *does* state, and to re-run the argot gate's own fixture;
2. it surveyed the **operability** surface the O claim is about, where it found a
   **real, reproducible defect** the round-25 audits did not catch (§3);
3. it took the D seats' register **design** and **executed it end-to-end inside a
   scratch clone** (§4b) — the design's plan, run as written, turns
   `derived_pairs=0` into `derived_pairs=8` with zero violations, and this seat's
   independent instrument agrees with the lane gate on every counter.

The independent instrument **reproduces the argot gate's coverage line exactly**
on the delivered D4 packet — `records=156 register_scoped=6 derived_pairs=0
claimed_chains=8 borrow_pairs=6 violations=0` — and reproduces the fixture's
finding set exactly, including all four planted `D4L-ARGOT-DERIV` FAILs. Three
audit findings are reported (§3, §4, §4c); none is a silent pass.

## 1. What was measured, at what revision

Digests measured by this seat, 2026-10-18, before and after the run set (all
identical across the window; scratch `.scratch/x60/digests-at-start.txt`):

| surface | sha256 |
|---|---|
| `examples/culture-d4/packet.d4.yml` | `e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3` |
| `examples/culture-d4/packet.d4.typed.yml` | `ffece0feb52c5b0b8ae6b0f8c1848d6220ad2dc2b36b1faac6385d62f4bfd84e` |
| `examples/culture-d4/typed-labels.d4.yml` | `60b526b0b3d07141875d20c472451cdf6658f61936d39fe18af4f3d981981092` |
| `examples/culture-d4/expected-holds.json` | `3826ba68d705b3c379b2a12737c14075d9095a1ba2aa2eb525de1851a9ecd2f7` |
| `tools/gates/argot-derivation-gate.py` | `5b5abe7865ed906c23fba87fd0dae8b6187c8dfc1a80137adbd364d4d88b0211` |
| `tools/gates/typed-pipeline-gate.py` | `b749ad07cf1710279aea557c071587cf4b3a228a9fb4d03398b4b94d2f32ad85` |
| `tools/gates/naming-collision-gate.py` | `d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d` |
| `tools/gates/fixtures/argot-derivation-gate.yml` | `c4c35294d581b204482427b3776776c57d1e7f83065a0b5f8f3906c38d8c2ccd` |
| `tools/gates/fixtures/argot-derivation-gate.expected` | `38a283ff3b7cef4336418237f345f3602c4faeee197baca4d1ebc1bb0f78a018` |
| `reports/round-25/run-validation.py` | `d19435251dccb738e456c01fe7fb94498c27bae7f70704a96f94ec9324ce35af` |

The naming gate's digest is the round-24/25 value, so the replay semantics this
seat exercised are the frozen ones. A poll for a register-stratum landing
(`.scratch/x60/poll-register.py`, every 60 s) ran from 15:06 local and saw the
packet digest, the `derived_from`/`derivation` count (0) and the `register`
count (12) all unchanged.

**Status of the claim-D surface at close.** The D-scribe's own draft
(`reports/round-26/scribe/capability-row.md`, R26-D25) independently reports the
same thing at 18:05:17Z: "the register stratum is NOT on disk … `registers:` /
`doublets:` / `doublet_of` / `#plain` / `#quote` → 0 files under `examples/`".
This seat confirms that observation but does not adopt it as its own measurement;
the measurement is §2's `derived_pairs=0` and the unchanged packet digest.

## 2. The independent instrument, and what it re-runs

**Instrument:** `reports/round-26/audit/x60-register-derivation-spotcheck.py`
(new, this seat's; NON-CANON audit evidence, not a lane gate). It is deliberately
built on different machinery from the gate it audits:

| dimension | the lane gate | this instrument |
|---|---|---|
| YAML parsing | the naming gate's hand-checked subset loader (`runpy` by path) | `ruby -ryaml` → JSON (a full YAML 1.1 loader) |
| `head2` / `reverse` | the gate's own `OPS` table + `syllabify()` | re-implemented from `design-language.md` §5 prose |
| pattern/output replay | the naming gate's budgeted matcher | the standard library `re` directly |
| kernel dependency | loads `naming-collision-gate.py` by path, prints its digest | none — no lane code is imported |

**Controls (a checker that never says no is not a checker).** Three planted
violations, all caught:

```
control control-1-planted-formation-mismatch     ok   violations=1
control control-2-planted-loan-mismatch          ok   violations=1
control control-3-clean-stays-clean              ok   violations=0
```

**Run 1 — the delivered D4 packet.** Command and result (2026-10-18, lane root,
`TMPDIR=$PWD/.scratch`):

```
$ python3 reports/round-26/audit/x60-register-derivation-spotcheck.py --controls
design-11-worked-derivations             ok
design-8-name-reversals                  ok
maximal-onset-is-load-bearing            ok
packet-records-counted                   ok
independent-reading-agrees-with-lane-gate ok
counters: borrow_pairs=6 claimed_chains=8 derived_pairs=0 records=156
          register_scoped=6 register_scoped_declared=18 rule_holds=0 violations=0
failures: 0
```

This **reproduces the gate's coverage line exactly** — `records=156`,
`register_scoped=6`, `derived_pairs=0`, `claimed_chains=8`, `borrow_pairs=6`,
`violations=0` — reached by a different parser and a different derivation
implementation. The agreement is checked **live**: the instrument runs the lane
gate on the same input and compares every counter, rather than asserting a number
frozen at this seat's writing, so it keeps its meaning if the tree moves. (The
check deliberately does *not* require `violations=0`: the committed fixture is a
negative control whose four violations are the expected result.) The gate's own
live run, for the record:

```
$ python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
coverage: examples/culture-d4/packet.d4.yml records=156 register_scoped=6 derived_pairs=0 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0
dependency: tools/gates/naming-collision-gate.py sha256 d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d
exit 0
```

**Run 2 — the gate's own fixture** (`tools/gates/fixtures/argot-derivation-gate.yml`).
This is the negative control that gives the leg its teeth. The instrument reports
the same four FAILs and the same one HOLD as the gate, with the same ids, forms,
rules, bases and replayed values:

```
$ python3 reports/round-26/audit/x60-register-derivation-spotcheck.py --packet tools/gates/fixtures/argot-derivation-gate.yml
MISMATCH ('Q-11', 'saalum', 'FAIL', 'head2', 'saalumi', 'saalu')
MISMATCH ('Q-12', 'kin',    'FAIL', 'reverse', 'kin', 'nik')
MISMATCH ('Q-13', 'suk',    'FAIL', 'reverse', 'sun', 'nus')
MISMATCH ('B-03', 'gal',    'FAIL', 'borrow', 'West layer', 'gol')
counters: borrow_pairs=3 claimed_chains=0 derived_pairs=8 records=14
          register_scoped=11 rule_holds=1 violations=4
$ python3 tools/gates/argot-derivation-gate.py tools/gates/fixtures/argot-derivation-gate.yml
FINDING D4L-ARGOT-DERIV: FAIL — register-scoped form Q-11 'saalum' (register 'quote'): …
FINDING D4L-ARGOT-DERIV: FAIL — register-scoped form Q-12 'kin' (register 'quote'): …
FINDING D4L-ARGOT-DERIV: FAIL — register-scoped form Q-13 'suk' (register 'quote'): …
FINDING D4L-ARGOT-DERIV: FAIL — register-scoped loan B-03 'gal' (register 'trade'): …
FINDING D4L-ARGOT-RULE: HOLD — register-scoped form Q-20 'nuka': declared derivation 'someop' …
exit 1
```

**Run 3 — the typed gate, end to end.** `python3 tools/gates/typed-pipeline-gate.py
examples/culture-d4/packet.d4.yml` → exit 0, `summary: 20/20 legs passed`,
including `ok L3b-argot`. The D4 chain is green at this revision.

**The 12/6 denominator, explained rather than papered over.** The instrument
counts both register denominators, and they differ by construction:
`register_scoped_declared=18` (every record declaring a non-plain register —
`CT-01/02`, `LY-01/02`, `SYM-01..08`, `L-49..54`) against the gate's
`register_scoped=6` (the subset that is also a replayable *lexical* form —
`L-49..L-54`). The 12 excluded rows carry prose in `form:`/`name:` (`symbols`
describes a medium; `contact`/`layers` labels a road or a stratum), not a string
the sound-and-identity channel could derive. The instrument applies the gate's
own two-part lexical rule (a form key **and** a lexical marker) and therefore
agrees on 6; the 12 prose rows are printed as a named list rather than dropped
silently. **This is a documentation point, not a disagreement.**

## 3. FINDING X60-F1 (operability, pre-existing — a pinned revision that is not in the repository)

**The round-25 gate-input freeze is not replayable from the committed tree.**

```
$ python3 tools/replay-frozen.py tools/gates/frozen/round-25/gate-input/MANIFEST.tsv
{"rows": 6, "reproduced": 0, "mismatch": 0, "could_not_evaluate": 6, "exit": 2}
  every row: reason=gate_digest_mismatch
  detail: gate: on-disk bytes are not the pinned revision: tools/gates/typed-pipeline-gate.py
```

The manifest (`MANIFEST.tsv`, `freeze.txt`) pins
`tools/gates/typed-pipeline-gate.py` at
`879d40bf977eef659cabd7e87b7abd8dd5237cbd2cfa4c1a51c5ab622dbe4126` and claims
"replay … exit 0, 6/6 reproduced, 0 mismatch". Both are correct *for the bytes
they were taken against*; the problem is that **those bytes are not in the
repository**:

- `git rev-list --all -- tools/gates/typed-pipeline-gate.py` yields exactly three
  revisions: `d102fd1dd1ba` (r11), `04ad4bb47956` (f74fc94) and `b749ad07cf17`
  (fc13cd2, the round-25 admission commit). A scan of **every blob object in the
  repository** finds no blob hashing to `879d40bf…`.
- `879d40bf…` *does* exist — it survives in round-25 scratch clones
  (`.scratch/r25-o18/final/tools/gates/typed-pipeline-gate.py`, plus 15 other
  copies; digest histogram in `.scratch/x60/`). It is the **pre-argot** revision:
  it contains the round-25 O input-class fix and **zero** `argot` references.
- Run inside such a clone, it reproduces the recorded outputs **byte for byte**:
  `d4-source exit=0 BYTES-MATCH`, `d2-typed exit=0 BYTES-MATCH` (all four rows
  match; `.scratch/x60/receipts-C-D.txt`).

**Root cause (timestamps, local −03:00).** The freeze was written at **14:33:49**
and its recorded outputs read `summary: 19/19 legs passed` with no `L3b-argot`
line. The argot-leg binding landed in `typed-pipeline-gate.py` at **14:46:32**,
adding the leg (the committed revision reads `20/20` on the same input). The
freeze therefore captured the **pre-argot** revision, and the commit that
admitted the round swept in the **post-argot** revision. The pin and the bytes
it names were separated by the round's own landing order.

**Why the round-25 audits did not catch it.** The X46 cold-rerun and the O18
adversarial audit *did* replay this manifest green (`REPLAY OK: 6/6 rows
reproduced`) — but at a moment when the on-disk gate really was `879d40bf…`,
i.e. before the argot binding landed. The round-25 runner itself only ever ran
`tools/replay-frozen.py --selftest` (`reports/round-25/run-validation.py:169`),
never the manifest, so the drift was never re-measured after the gate moved.

**Scope of the blast radius (this seat's measurement).** Only the round-25
manifest is fully dead. The five earlier typed-pipeline manifests each lose
exactly **one** row to the same digest mismatch, and that row is a *typed-packet*
input in every case:

| manifest | result (2026-10-18) | refused row |
|---|---|---|
| `round-11/MANIFEST.tsv` | 10/11 reproduced, 1 cne, exit 2 | `round-11/typed-pipeline/packet.d2.typed.yml` |
| `round-18/repin-d2/MANIFEST.tsv` | 10/11 reproduced, 1 cne, exit 2 | same path (cross-pinned) |
| `round-20/repin-d2/MANIFEST.tsv` | 10/11 reproduced, 1 cne, exit 2 | same path (cross-pinned) |
| `round-22/d4-repin/MANIFEST.tsv` | 2/3 reproduced, 1 cne, exit 2 | `examples/culture-d4/packet.d4.yml` |
| `round-23/repin-d2/MANIFEST.tsv` | 10/11 reproduced, 1 cne, exit 2 | `examples/culture-d2/packet.d2.typed.yml` |
| `round-25/gate-input/MANIFEST.tsv` | **0/6 reproduced, 6 cne, exit 2** | all six rows |

The round-25 `freeze.txt` predicted this cascade in the abstract ("every earlier
generation that pinned the predecessor now refuses its typed-pipeline row") but
did not notice that its own generation pins a revision that was never committed.

**What this is, and is not.** It is an **operability defect in a filed
round-25 artifact** (the freeze's own binding), reported here, not repaired —
repair is the O-claim seats' work and this seat writes only this fragment. It is
**not** a claim that the round-25 O fix was wrong: the committed revision carries
the same input-class fix, and its D2 rows are byte-identical to the recorded
outputs. The one behavioural delta between the pinned and committed revisions is
the added argot leg, which is the round-25 D claim's own landing.

**Suggested disposition (for the O seats, not taken here).** Either (a) re-point
the round-25 generation's `MANIFEST.tsv` and `freeze.txt` as a **new**
round-26 revision bound to `b749ad07…` and re-record the two D4 rows as `20/20`
and `17/17`, or (b) record the generation as **superseded** and bind the new
generation to the committed revision. Under this lane's rules either is a **new
row**, never an in-place edit of the filed round-25 bytes.

**Disposition observed while this fragment was being written (option (a), and it
works).** The D17..D20 seats landed
`tools/gates/frozen/round-26/gate-input/` at 18:08:08Z — a **new generation**
bound to the committed `b749ad07…`, with `freeze-receipt.json` naming the
round-25 generation as superseded *for exactly the reason above* ("the round-25
generation pins a gate revision that is not on disk; every row refuses
`gate_digest_mismatch` before a gate runs. A re-pin is a new generation, never an
edit."). This seat replayed the new generation independently:

```
$ TMPDIR=/tmp/x60mirror python3 tools/replay-frozen.py \
      tools/gates/frozen/round-26/gate-input/MANIFEST.tsv --json
{"rows": 6, "reproduced": 6, "mismatch": 0, "could_not_evaluate": 0, "exit": 0}
```

**6/6 reproduced, exit 0.** The round-25 generation is left byte-identical (its
refusal is now an honest, named one) and the defect X60-F1 raised is closed by a
new row rather than an edit — which is this lane's rule. Two independent seats
reached the same root cause; the corroboration is noted, not claimed as this
seat's.

**The gap is systemic, not one bad row.** `reports/round-26/run-validation.py`
— the round's own counting command — replays **no** frozen manifest: its only
replay leg is `("replay-selftest", ("tools/replay-frozen.py", "--selftest"))`
(`:193`), the same shape round 25 had. A manifest whose pin has drifted is
therefore invisible to the round's acceptance runner by construction. A
manifest-replay leg (even one leg over the newest generation) would have caught
X60-F1 at close. Recorded as an observation for the O seats; this seat does not
edit the runner.

## 3b. Cross-check of the D23 adversarial over-match claims

`reports/round-26/argot/D23-overmatch.md` (seat R26-D23) reports three
over-matches. This seat re-ran them from D23's own scratch fixtures. Two are
reproduced, one **with an independence limit stated**:

- **D23 attack B1 (the operation detector reads prose).** A rule whose
  `description` contains the substring `reverse` is read as *declaring* that
  operation, manufacturing a `D4L-ARGOT-COVERAGE` HOLD:
  `python3 tools/gates/argot-derivation-gate.py .scratch/r26-d21/desc-mentions-reverse.yml`
  → `FINDING D4L-ARGOT-COVERAGE: HOLD — packet declares the argot operation(s)
  reverse …`, exit 1. The paired control (`prose-reordered-ctl.yml`, the word
  `reordered`, no `reverse` substring) → exit 0, no finding. **Confirmed — but
  by the gate itself, not by this seat's instrument**, which implements only the
  derivation replay and the borrow adaptation, not the `D4L-ARGOT-COVERAGE` leg.
  The limit is stated rather than hidden; the reproduction is real, the
  independence is partial.
- **D23 attack B2 (the borrowed adaptation has no donor-side discipline).** A
  layer whose `substitutions` is `{a: e}` rewrites the donor nucleus
  (`khar` → `kher`) and the leg counts a clean adaptation:
  `borrow-oversub.yml` → `borrow_pairs=1 … violations=0`, exit 0. This seat's
  independent instrument agrees exactly (`borrow_pairs=1, violations=0`; receipt
  E) — the over-match is in the *rule*, not in one gate's implementation of it,
  because this instrument re-implemented the rule from the design and reached the
  same permissive result. **Confirmed, and shown to be implementation-independent.**

The third D23 finding (the `formation` leg graded beyond the register scope) is
visible in the same coverage line: `claimed_chains=8` on the delivered tree are
the eight `NM-01..NM-08` names, none register-scoped. This seat's instrument
grades the same eight and reaches the same count, so the scoping observation is
reproduced as a fact; whether it is a defect is D23's judgement, which this seat
neither adopts nor contradicts.

## 4. FINDING X60-F2 (spelling, carried from round 25 — now in a live claim)

The round-17 design and the round-25 claim both spell the id **`D4L-ARGOT-DERIV`**
(`design-brief.md:308,456`; `reports/round-25/claims.json:22`), and that is the
id the gate implements and the fixture's `.expected` asserts (four rows, all
`-DERIV`). The round-25 `impl-3.md` §4 recorded the variant `-DERV` as an
assignment-header typo and left it there. It is **no longer only a header typo**:
the round-26 claim's own `after_required` now writes the typo into the claim text
(`reports/round-26/claims.json:15`: "… or names violations `D4L-ARGOT-DERV`").

An implementer who reads the claim literally will emit `-DERV`, while the gate,
the fixture and every round-25 artifact emit `-DERIV`; a validator that greps the
claim's spelling will find zero rows. Recorded here, not repaired — the claim text
is the operator's. The correct spelling is `D4L-ARGOT-DERIV`.

## 4b. The register design's own plan, verified end-to-end (ahead of the D seats)

The D seats' register design landed in `reports/round-26/register/{design,forms,rules,review}.md`
while this seat worked. The design **does not** write the forms into
`examples/culture-d4/` — it names the requirement and the owner (design.md §5).
So the stratum is still not on the delivered tree. What this seat *could* do is
take the design's plan and run it, which is the most useful thing a spot-checker
can offer a design that has not yet been integrated.

**Method.** In a `git clone --shared` under `.scratch/x60/aclone2/` (never the
lane worktree), this seat patched `examples/culture-d4/components/04-lexicon.yml`
with exactly the two things `rules.md` says to add — the eight register records
(`RF-01..RF-08`, `register: stamp`, `derived_from`, `derivation`) and the
`LENGTHEN` rule — then ran the chain. Result:

```
$ python3 tools/assemble-culture-d4.py
Wrote examples/culture-d4/packet.d4.yml (85528 bytes)        exit 0
$ python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
coverage: … records=164 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0
exit 0
$ python3 reports/round-26/audit/x60-register-derivation-spotcheck.py --packet …/packet.d4.yml
independent-reading-agrees-with-lane-gate ok
counters: borrow_pairs=6 claimed_chains=8 derived_pairs=8 records=164 register_scoped=14 register_scoped_declared=26 rule_holds=0 violations=0
failures: 0
```

**This is the strongest evidence in this fragment.** The design's plan, executed
as written, turns the argot leg's coverage line from `derived_pairs=0` to
`derived_pairs=8` with **zero violations and zero rule holds**, and this seat's
*independently built* instrument agrees with the lane gate on every counter. The
eight forms also re-derive arithmetically from the design's own table under this
seat's independent `lengthen`/`reverse` implementations (8/8, no mismatches).
The `derived_pairs` clause of the round-26 D claim is therefore **reachable as
designed** — the blocker is integration, not arithmetic. (The typed gate refuses
the scratch packet on `L1-profile` because the pipeline pins the delivered
packet digest; that is the pin cascade the D seats must move when they land, not
a defect in the design.)

**Corroboration.** The D-seat's own review (`reports/round-26/register/review.md`
§1, row G-5) claims exactly this result from its own probe
(`.scratch/r26-d-reg/probe-rule2.yml`: "`derived_pairs=8 violations=0
rule_holds=0`, exit 0"). This seat reached the same numbers by a different route
— a fresh clone, a component patched from `rules.md` rather than from the probe,
and a second, independently written instrument — so the two are independent
confirmations of one design, not one measurement cited twice. The design's
arithmetic is sound; its **integration** is what the claim still needs.

## 4c. FINDING X60-F3 (the documented `LENGTHEN` snippet is not parseable as written)

`reports/round-26/register/rules.md:60-63` documents the rule to add as a
**multi-line flow mapping**:

```yaml
  - {id: LENGTHEN, kind: "vowel-length",
     pattern: "…",
     output: "{onset}{vowel}{vowel}{rest}",
     note: "…"}
```

Both consumers in this lane **reject that form**:

```
$ python3 tools/gates/argot-derivation-gate.py <rules.md:60-63 verbatim>
FINDING D4L-ARGOT-DATA: FAIL — input could not be evaluated: unexpected content after flow item at input line 4
exit 2
$ python3 tools/assemble-culture-d4.py     # component patched with the same snippet
assembly error: 04-lexicon.yml: input is not one mapping (or has unparsed trailing lines)
exit 2
```

The **single-line** flow form (`- {id: LENGTHEN, kind: …, pattern: …, output: …, note: …}`)
is accepted by both and is what the design's own probe
(`.scratch/r26-d-reg/probe-rule2.yml:209`) actually uses. So the rule *is* right;
the **documentation snippet is a copy-paste trap** — a D seat that copies
`rules.md:60-63` into the component gets an assembly refusal, not a replay.

Severity: low but real, and exactly the kind of thing a spot-check exists to
find, because the failure appears at integration time and its message
("input is not one mapping") does not point at the snippet. Recorded here, not
repaired; the fix is one line in `rules.md` (already landed, so a correction
would be a **new** file per this lane's rules).

## 5. What this seat did *not* do

- It did **not** grade the round-26 D claim. The register stratum is **still not
  on the delivered tree** at this seat's close (§1, §4b) — the D seats designed
  it but did not integrate it. This seat's headline numbers bind the
  **pre-register** tree; the parent must re-run the round-26 counting command on
  the settled post-register tree.
- It did **not** re-run `reports/round-26/run-validation.py`. The runner landed
  mid-window; running it against a moving tree inside the lane worktree is what
  the X64 seat's method avoids. No round-26 runner receipt is claimed here.
- It did **not** edit any pin, manifest, freeze file, tool, gate, fixture,
  component, packet or sibling fragment. The register-plan verification (§4b) was
  done entirely inside a scratch clone.

## 6. Limits

- A receipt binds the bytes it was taken against. Every number above carries its
  digest or its command; a number without one is not a measurement.
- The tree moved during this window (round-26 surfaces grew while this seat
  worked). The register-stratum poll (§1) is the control that says the packet
  itself did not move.
- The `879d40bf…` revision was recovered from **round-25 scratch clones**, which
  are gitignored and not part of any frozen artifact; the recovery is evidence of
  what the freeze captured, not a proposed pin.
- NON-CANON engineering evidence. No source-freshness certification, real-world
  rights clearance, lore acceptance or promotion is claimed.

## 7. Reproduce

```sh
export TMPDIR=$PWD/.scratch
python3 reports/round-26/audit/x60-register-derivation-spotcheck.py --controls
python3 reports/round-26/audit/x60-register-derivation-spotcheck.py \
    --packet tools/gates/fixtures/argot-derivation-gate.yml
python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
TMPDIR=/tmp python3 tools/replay-frozen.py \
    tools/gates/frozen/round-25/gate-input/MANIFEST.tsv --json    # 6 cne, exit 2
# recovery of the pinned revision, for comparison only:
cd .scratch/r25-o18/final && python3 tools/gates/typed-pipeline-gate.py \
    examples/culture-d4/packet.d4.yml                             # 19/19, pre-argot
# the register-plan verification (§4b), inside a scratch clone:
git clone --quiet --shared . .scratch/x60/aclone2
#   patch components/04-lexicon.yml with the eight RF rows + the SINGLE-LINE
#   LENGTHEN rule, then:
cd .scratch/x60/aclone2
python3 tools/assemble-culture-d4.py                              # exit 0
python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
#   -> derived_pairs=8 ... violations=0 rule_holds=0, exit 0
```

Receipts (scratch, gitignored): `receipts-A-B.txt` (instrument on the packet and
the fixture), `receipts-C-D.txt` (manifest replay + pinned-revision recovery),
`receipts-E.txt` (D23 cross-check), `receipts-F-G.txt` (register plan +
multi-line rejection), `digests-at-start.txt`, `poll.log`, and
`independent-run-final.out`.
