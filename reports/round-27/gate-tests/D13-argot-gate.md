# R27-D13 — the argot gate on the amended packet: green, deterministic, law landed

- **Seat:** R27-D13 (gate runs 1 of 4), round 27, loop 3 build 3 of 4, claim **D**
  `register-law` (`reports/round-27/claims.json:14-28`).
- **Date:** 2026-10-18. Declared baseline
  `4f09c990d4c17f23b5e2cda0871f81db875635fc` (`claims.json:5`); lane HEAD
  `b95fca1e40f32f7346937ab6426f9ccca60e319f` at every measurement.
- **Write scope:** `reports/round-27/gate-tests/{run-gate-tests.py,fixtures/**,receipt.json,D13..D16*.md}`
  plus gitignored scratch under `.scratch/r27-d13/`. `export TMPDIR=$PWD/.scratch`
  preceded every scratch-writing command. **No tool, gate, packet, component,
  projector, pin, fixture or filed rounds 8–26 byte was written; no commit, no
  push.**
- **Canon:** NON-CANON engineering evidence. A green gate is a measurement, not a
  clearance; a hold stays a hold.

## 0. Verdict

**The argot gate is green on the amended packet, three runs byte-identical, and
the register law it grades has landed on the delivered surface.**

Measured (`2026-10-18T19:4xZ`, `TMPDIR=$PWD/.scratch`):

| check | command | exit | evidence |
|---|---|---:|---|
| the graded run | `python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | **0** | `records=175 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0` |
| determinism | the same, 3× | 0,0,0 | **1** distinct stdout digest |
| the gate's own controls | `... --selftest` | **0** | `selftest: 27/27 checks passed` |
| the whole battery | `python3 reports/round-27/gate-tests/run-gate-tests.py` | **0** | `summary: 55/55 checks passed` |
| the runner's controls | `... --selftest` | **0** | `selftest: 18/18 checks passed` |
| the register block | `grep -n '^registers:' …` | — | present; `QREG-01..04` |
| the register **law** block | `grep -n '^register_law:' …` | — | present; `RGL-01..05` |

Pinned at the measurement:

```
tools/gates/argot-derivation-gate.py   sha256 b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb
examples/culture-d4/packet.d4.yml      sha256 86079a6708a0d360bedfed60306274c09ec4f4e76a5912b94a05f762d17caebc
examples/culture-d4/components/13-register-law.yml
                                       sha256 c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7
```

**Cite blocks by id, not by line.** The packet was regenerated more than once
while this seat was measuring (the law landing, then a re-pin), and line numbers
moved under it. Every claim in this file names a **block and a record id**
(`registers`/`QREG-0n`, `register_law`/`RGL-0n`), which survives a regeneration;
the line numbers quoted in the first draft did not, and were replaced.

The coverage line's own dependency row names the peer the gate loaded, so the
replay says which bytes it used rather than assuming them:

```
dependency: tools/gates/naming-collision-gate.py sha256 d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d
```

## 1. What the coverage line means, and what it does not

| counter | value | reading |
|---|---:|---|
| `records` | **175** | every packet record the gate walked (170 before the law landed; +5) |
| `register_scoped` | 14 | 8 register forms + 6 borrow pairs on declared register layers |
| `derived_pairs` | 8 | the 8 register forms, each replayed against its own stated inputs |
| `claimed_chains` | 8 | the same 8 under the packet's declared rule registry |
| `borrow_pairs` | 6 | the loan-adaptation leg over declared layers |
| `violations` | **0** | no replayed form disagrees with its stated derivation |
| `rule_holds` | **0** | no declared derivation is unreplayable |

`violations=0` with `derived_pairs=8` is the substantive result: the register
stratum's arithmetic is **checked**, not merely declared.

**The law rows add records but no derivations, and that is the right shape.**
`records` moved 170 → 175 (the five `RGL-0n` rows) while `register_scoped`,
`derived_pairs` and `violations` are unmoved: the law is a *declaration* about
admissibility, not a new set of derived forms, so it correctly adds nothing to
the derivation domain. A law that had changed any of those three counters would
have been changing the stratum's arithmetic, which is `04-lexicon.yml`'s.

**Not a clearance.** Exit 0 means "every register-scoped form that states its
inputs re-derives". It does **not** say the law is enforced, that any hold
elsewhere is closed, or that the stratum is sound — §2 and D15 grade the law's
own surface.

## 2. The law has landed, in a new block

The claim's `after_required` asks for "a D4 component [that] declares the stamp
register's speech-act rules (what may be said in-register, by whom, with what
record consequence), wired into the packet deterministically". Measured present:

```
$ grep -n '^registers:\|^register_law:' examples/culture-d4/packet.d4.yml
1311:registers:                       # QREG-01..04 — the register identity
2633:register_law:                    # RGL-01..05 — the speech-act law
$ grep -c 'id: "RGL-0' examples/culture-d4/packet.d4.yml
5
```

The law landed as a **new component**,
`examples/culture-d4/components/13-register-law.yml`
(sha256 `c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7`), which
declares `packet_keys: [register_law]` and is merged by the assembler **without
an assembler edit** — a component's own `packet_keys` declaration fixes its
packet contribution (`tools/assemble-culture-d4.py:255-266`), so a new block
needs no allowlist entry. The 13th component is above the registry's 12-file
floor (`MINIMUM_COMPONENTS`, `:66`). `01-brief.yml` registers it as component
`C-13` and declares the block's record fields
(`register_law: [id, register, axis, kind, act, speaker, holder, force,
consequence, design_row, evidence, follows]`, `:183`).

**The contract-side declaration is what closes a real gap, and the peer
instrument measured it.** Peer X59's law `L9` reads that the block "reaches the
packet only through the component's own per-file `packet_keys` declaration":
because `register_law` is in neither `PACKET_KEYS` nor `RECORD_FIELDS`
(`tools/assemble-culture-d4.py:81,118`), the assembler's record validator has no
field list for it, so stripping an `id` from a law row assembles exit 0 and lands
`id: None` — where the same edit to a `lexicon` row refuses exit 2. The
`01-brief.yml` field declaration above addresses the *schema* half of that; the
*validator* half is the assembler's and is recorded as X59's `L9-HOLD`, which is
still open at this stamp.

**The two blocks are different things and this seat does not conflate them:**

| block | rows | what it declares |
|---|---|---|
| `registers` | `QREG-01..04` | the register **identity**: what `plain` and `stamp` are, the axis→operation rule, the era rule |
| `register_law` | `RGL-01..05` | the **speech-act law**: the act, the holder, the consequence |

The law rows carry `{id, register, axis, kind, act, holder, consequence,
evidence, follows, cite}`. The component's own `law_binding` block states what
they bind to and — importantly — states that **no gate executes them**:

> *"no gate executes these rows. The era leg (RGL-05) is specified and
> unimplemented … The rows are a declared law with named non-execution, not a
> claim of enforcement."*

That honesty is the correct shape for this round. The enforcement leg is
unowned and priced (`reports/round-27/law/design.md` §5's E-1..E-7, which
measures that widening the projector's kind set alone would produce a **silent
`not-applies`** rather than an evaluation — strictly worse than the current
honest hold).

## 3. The runner this seat lands

`reports/round-27/gate-tests/run-gate-tests.py` is the executable form of the
four seats. It is self-describing (every measurement names its command, exit and
date) and carries a dependency-free selftest (15/15, `--selftest`):

```
$ python3 reports/round-27/gate-tests/run-gate-tests.py --selftest
selftest: 15/15 checks passed
$ python3 reports/round-27/gate-tests/run-gate-tests.py
summary: 55/55 checks passed
```

Design rules it works inside:

- Every measurement names its command, its exit code and its date.
- The law control copies the **working tree** into scratch, never the lane
  worktree, and never a `git clone` (the round-27 landing is uncommitted, so a
  clone of HEAD would baseline the *pre-law* tree — see D15 §1.1).
- No file outside `reports/round-27/` and `.scratch/` is written.
- Where the round-27 law surface has no owning lane gate, that is recorded as a
  **named gap** rather than papered over with a private checker.

## 4. Limits

- **This seat measures; it does not repair.** It wrote no gate, no component, no
  packet and no pin.
- **Green here is green at one stamp, and the tree is mid-wave.** The round-27
  landing is *uncommitted* at `b95fca1`; the digests above are of the working
  tree. If a further edit lands after this file is filed, this reading is
  superseded and needs a dated refresh — one command, since the runner prints and
  pins both columns.
- **`rule_holds=0` is not "no holds anywhere".** The gate's holds are its own
  scope's; the D4 typed gate's 12 holds are D14's surface.
