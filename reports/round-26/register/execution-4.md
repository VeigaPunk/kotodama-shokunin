# R26-D16 — argot execution 4: the domain census, and the state it proves

- **Seat:** R26-D16 (D axis, argot execution 4 of 4), round 26, loop 3 build 2 of 4,
  claim **D** `register-stratum` (`reports/round-26/claims.json:14-23`).
- **Date:** 2026-10-18. Baseline `fc13cd27b9e78d5d7c4f70740fd26c9383a7447b`;
  worktree HEAD `1ad491a1a4b0aef9ebdc1861dfb8237727503825`. Stamps UTC.
- **Write scope:** `reports/round-26/register/execution-{1..4}.md` only; scratch
  under `.scratch/r26-d13/` only. No tool, gate, packet, component or filed
  rounds 8–25 byte written; no commit, no push.
- **Canon:** NON-CANON engineering evidence.

The assignment's clause is "the leg's domain no longer empty — the census proves
it". This file is the census, taken twice: over the **delivered** packet, and
over the **candidate** execution 1 built from the design. The two readings are
what the clause needs, because they differ.

## 1. The census instrument

`.scratch/r26-d13/argot-census.py` (scratch, this seat; sha256 `a3ef4ffd…`).
It reads the packet with the **gate's own** YAML subset loader (loaded
read-only by path from `tools/gates/naming-collision-gate.py`, so census and
gate cannot disagree about what the packet says) and counts:

- `records` — every mapping record in every top-level list block;
- `form_records` — records a language owns a form for (the gate's
  `is_form_record` rule);
- `register_scoped` — form records whose register is marked (declared
  `register:`, or a `loan_layer`/`layer` resolving to a register-bearing layer),
  with `plain`/`neutral`/`standard`/`ordinary` treated as unmarked;
- `derived_pairs` — records declaring `derived_from` **and** `derivation`;
- `claimed_chains` — records carrying the packet's own `formation{stem, rule}`;
- `borrow_pairs` — borrowed records whose layer carries `substitutions` and whose
  own `donor_form` is stated;
- `packet_declared_ops` / `declared_ops_on_pairs` — the argot operations declared
  and the operations the pairs actually name.

## 2. Census A — the delivered packet (the state round 25 left)

```
$ export TMPDIR=$PWD/.scratch
$ python3 .scratch/r26-d13/argot-census.py examples/culture-d4/packet.d4.yml
```

| counter | value |
|---|---|
| `records` | **156** |
| `form_records` | **62** |
| `register_scoped` | **6** |
| `derived_pairs` | **0** |
| `derived_pairs_register_scoped` | **0** |
| `claimed_chains` | **8** |
| `borrow_pairs` | **6** |
| `declared_ops_on_pairs` | **{}** (empty) |
| `packet_declared_ops` | **[]** (empty) |
| registers seen | `{trade: 4, craft: 2}` |
| packet rule ids | `CX-01, CX-02, CX-03` |

The 6 register-scoped records are the trade/craft loans `L-49..L-54`
(execution 3 §1). **The register derivation domain is empty**: zero
`derived_from`/`derivation` pairs, zero declared operations.

The gate's own coverage line agrees counter for counter:

```
coverage: examples/culture-d4/packet.d4.yml records=156 register_scoped=6
          derived_pairs=0 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0
exit 0
```

That is the round-25 shape exactly — a **structural pass on an empty domain**,
which the gate's own docstring says is "a capability plus a replay, not a
clearance" (`argot-derivation-gate.py:52-54`).

## 3. Census B — the candidate built from the design

Execution 1 §1 built `.scratch/r26-d13/enriched-d4.yml` (delivered bytes + the
design's 8 records + the `LENGTHEN` row + the schema fields + the `registers:`
block, by pure insertion). The same census over it:

| counter | delivered | candidate | delta |
|---|---|---|---|
| `records` | 156 | **166** | +10 (8 lexicon records + 2 registers rows) |
| `form_records` | 62 | **70** | +8 |
| `register_scoped` | 6 | **14** | +8 |
| `derived_pairs` | **0** | **8** | **+8** |
| `derived_pairs_register_scoped` | 0 | **8** | +8 |
| `claimed_chains` | 8 | 8 | 0 |
| `borrow_pairs` | 6 | 6 | 0 |
| `declared_ops_on_pairs` | `{}` | **`{lengthen: 6, reverse: 2}`** | +2 ops |
| registers seen | `{trade: 4, craft: 2}` | **`{stamp: 8, trade: 4, craft: 2}`** | +`stamp` |
| packet rule ids | CX-01..03 | **CX-01..03 + `LENGTHEN`** | +1 |

**The census therefore proves the domain is non-empty under the design, and
empty on the delivered tree.** Both statements are true at once and neither
displaces the other:

- The clause "the leg's domain no longer empty" is **satisfied by the design's
  data**, measured: `derived_pairs=8`, `register_scoped=14`, 8 of them in
  `stamp`.
- The clause is **not satisfied by the delivered packet**: `derived_pairs=0`,
  `register_scoped=6`, no `stamp` register anywhere.

The census is the instrument that keeps those two from being confused. A reader
who runs only the delivered census sees an empty domain and a green gate; a
reader who runs only the candidate census sees 8 pairs and a green gate. The
pair of readings is the honest report.

## 4. The leg's verdict over each domain

| run | input | `derived_pairs` | `violations` | `rule_holds` | exit |
|---|---|---|---|---|---|
| A | delivered packet | 0 | 0 | 0 | **0** |
| B | candidate, op as `rules.md` §2 spells it (`lengthen`) | 8 | 0 | **6** | **1** |
| C | candidate, op as `rules.md` §3 spells it (`LENGTHEN`) | 8 | 0 | **0** | **0** |

Run B is the defect execution 1 §2 names; run C is the clean replay. The
register derivations **replay clean in both runs** (`violations=0`); the two runs
differ only in whether the declared operation name matches the declared rule id.

## 5. Digests (a reading binds to these bytes)

Measured 2026-10-18T18:12:57Z, `sha256sum`:

| artifact | sha256 |
|---|---|
| `examples/culture-d4/packet.d4.yml` | `e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3` |
| `examples/culture-d4/packet.d4.typed.yml` | `ffece0feb52c5b0b8ae6b0f8c1848d6220ad2dc2b36b1faac6385d62f4bfd84e` |
| `examples/culture-d4/components/04-lexicon.yml` | `74c2561b7c875c7c98708c589002b85b7989fc64bafa6abf794210401c69a9a5` |
| `tools/gates/argot-derivation-gate.py` | `5b5abe7865ed906c23fba87fd0dae8b6187c8dfc1a80137adbd364d4d88b0211` |
| `tools/gates/naming-collision-gate.py` | `d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d` |
| `.scratch/r26-d13/argot-census.py` | `a3ef4ffd0adcc7f54cda9ca908da91ed5e7c17109710d6b453576a4205a3dea8` |
| `.scratch/r26-d13/argot-enrich.py` | `f53b914cf197afc06737c33f476fa008eab6e1443cfb936621aac35233cd4991` |
| `.scratch/r26-d13/enriched-d4.yml` | `369b0fd83b3e7d7a00bffe4b0b8c805272be05a6f5e368e68ba73d0ae6505dcb` |
| `.scratch/r26-d13/argot-execute.py` | `e8e8aa2e6e6e5881fdd5b29cebed72785bb327fcb68b325fecdc72086f6f1d00` |
| `.scratch/r26-d13/argot-controls.py` | (scratch; receipt `.scratch/r26-d13/controls.json`) |

The gate's own dependency line names the loader it used, so a reader can tell
which bytes the replay ran against:

```
dependency: tools/gates/naming-collision-gate.py sha256 d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d
```

## 6. The watch: the landing was polled, and it did not arrive in this window

Three independent pollers ran for the stratum's landing, all finding the packet
byte-still:

- this seat's `.scratch/r26-d13/argot-watch.py` — snapshots at 18:01:36Z and
  every interval after; packet digest constant, census constant;
- `.scratch/r26d/poll-register.sh` (peer D-scribe) — greps for
  `D4L-REGISTER-UNRESOLVED` every 60 s;
- `.scratch/x60/poll-register.py` (peer X audit) — logs
  `digest=e7ecd2045ef0e5f9 derived=0 register=12 keys_new=[]` at 15:06–15:11
  local (18:06–18:11Z).

At this seat's close (2026-10-18T18:13:53Z) the packet is still `e7ecd204…`,
`examples/culture-d4/components/06-register-contract.yml` does not exist, and
`grep -c "register: stamp"` over the components is 0. **The D-register data
seats were live and their design landed; the data did not.** This is reported as
the state, not as a seat failure.

## 7. What a re-read requires

When the stratum lands, the four executions re-run unchanged against the new
packet digest: `argot-census.py` gives the new counters, the gate gives the new
coverage line, and execution 1's Run A/B distinction either disappears (if the
landing spells the op and the rule id alike) or persists as the named defect.
The re-read is a single command per execution; the harnesses are scratch-only
and take the packet path as an argument.

## 8. Limits

- The census counts **declared** structure; it does not judge whether a declared
  register should exist or whether a form is the "right" word. Those are design
  questions the design itself labels as design choices (`forms.md` CAL-1..CAL-4).
- The candidate is this seat's reconstruction of the design's table. It is
  scratch-only and is not a delivered artifact; no delivery of the stratum is
  claimed by any of these four files.
