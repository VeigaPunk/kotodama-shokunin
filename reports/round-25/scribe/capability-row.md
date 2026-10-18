# R25-D18 — capability-row draft: argot-derivation checking on D4

- round: 25 (operator loop 3 of 3, build round 1 of 4; 64 declared workers,
  `devin/deepseek-v4-1-flash-high`). Seat **R25-D18** (D-scribe 1 of 3).
- claim under draft: `reports/round-25/claims.json` claim **D**, capability
  `argot-derivation-check`.
- date: 2026-10-18. Claim baseline revision `e06581b7fc2b50050a336f7f38a7e2baebcc6abc`
  (declared); worktree HEAD at this seat's first measurement
  `f74fc9403d4b02c8ee76439eb133e3dea9b65b14`, `git status --porcelain` clean.
- **status: DRAFT ONLY — the orchestrator admits.** This seat edits no
  `SCORECARD.md`, no `SKILL.md`, no `LOG.md`, no tool, gate, example, component
  or packet. Everything below is proposed text plus read-only receipts.
- writes: this file only, plus gitignored scratch under `.scratch/r25d/`
  (`TMPDIR=$PWD/.scratch` preceded every scratch-writing command). No commit,
  no push. No filed artifact of rounds 8–24 was modified; no earlier frozen
  generation was edited in place.
- canon: **NON-CANON engineering evidence.** A capability row records a
  demonstrated run; it is not canon, not lore acceptance, not a clearance and
  not a real-world etymology check.

## 1. What the row would assert — and what it must not

The row records a **capability**: a machine-checked derivation relation between
two records of one packet (a quote form and its plain base), replayed against a
declared, fully specified operation, plus the negative control that proves the
relation can fail. It is not a claim that any D4 form is a good name, that the
argot design is sound, or that the register system is complete — the register
slots stay held (`D4L-REGISTER-UNRESOLVED`), and the delivered packet's own
debt set is expected to carry **zero** `D4L-ARGOT-DERIV` rows, because that id
is a **control-only** id (`reports/round-17/d4/design-brief.md:308-310`).

**Admission gate.** `reports/round-25/claims.json` requires the leg "implemented
and executed on D4". At 2026-10-18T17:29Z the leg was **not on disk** (no `ARGOT`
token in `tools/` or `examples/`). It landed at 17:30Z and was still being
revised through 17:33Z; at **17:33:42Z** it reads
`tools/gates/argot-derivation-gate.py`, sha256
`07db6e9b4e01539e1dbb8af9e51eada6fe37784145915a0387f48f2ecd99f8fe`,
with `--selftest` **18/18 green** and the D4 run green (§4). One condition still
gates the row: `tools/gates/frozen/round-25/` holds a `gate-input/` generation
(the O claim's) but **no argot generation** at this stamp, so the frozen rows
remain drafts (§3, and `frozen-rows.md`).

The row below is **landing-ready text**, exactly as the round-9 precedent gated
its D3 row (`reports/round-9/d3/capability-draft.md` §2). **The gate was edited
three times during this seat's window** (`82f48649…` → `55f83442…` →
`3deb6bb6…` → `75aee372…` → `07db6e9b…`); only the last revision is cited, and
every digest here must be re-measured at integration.

## 2. LANDING-READY — SCORECARD "Capabilities" table row

Intended surface: `SCORECARD.md` §Capabilities (`SCORECARD.md:41-53`), whose
columns are `name | demonstrated behavior | command / evidence | first working`.

```markdown
| argot-derivation checking (D4) | A register-scoped form that claims a derivation from a stated base is replayed against the declared operation (`head2` maximal-onset / `reverse`) or the packet's own machine-readable `pattern`/`output` rule; a form the stated inputs and rules do not yield is `D4L-ARGOT-DERIV` FAIL, an unreplayable declaration is `D4L-ARGOT-RULE` HOLD, and a declared-but-undelivered relation is `D4L-ARGOT-COVERAGE` HOLD; on the delivered D4 packet the leg reads exit 0 (6 register-scoped records, 6 borrow pairs replayed, 0 violations) and the delivered packet carries zero `D4L-ARGOT-DERIV` rows by design; the committed fixture pair carries 4 planted `D4L-ARGOT-DERIV` + 1 `D4L-ARGOT-RULE` and `--selftest` reads 18/18 | `python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` (exit 0, stdout sha256 `49060ed39b8725f5f7268a24492adc52e944f80e8eff517541d2a56d0483104f`); `--selftest` (18/18); gate sha256 `07db6e9b…`; negative controls in §4; `python3 reports/round-25/run-validation.py` | round 25 (declared round 17, forecast only — `reports/round-17/d4/design-brief.md:296-310`; delivered-vs-forecast delta `reports/round-25/argot/`) |
```

Notes for the orchestrator on this row:

- "declared round 17, forecast only" mirrors the D2 row's "round 3; selftest
  supplement-opencode-1" and the D3 row's "declared round 7; round-7 acceptance
  runner exited false" pattern (`SCORECARD.md:46`; `reports/round-9/d3/capability-draft.md` §2).
- The row must carry the **zero-rows-by-design** clause. Omitting it would let a
  reader conclude the delivered packet was cleaned of argot defects; in fact the
  id is control-only and the packet was never required to carry one.
- The row must also carry the leg's **own honest scope**, stated in the gate's
  docstring: exit 0 means "every register-scoped form that states its inputs
  re-derives", not that the stratum is complete or that any hold elsewhere is
  closed. On D4 the forecast relation is **declared, not delivered**
  (`derived_pairs=0`), and the delta is named in `reports/round-25/argot/delta.md`.
- If the orchestrator prefers the addendum style used in round 18, the same row
  can land under "Capabilities addendum (round 25)"; the columns are identical.
- **Re-pin obligation.** Any edit to the projector, the naming gate, the typed
  adapter or the packet after the leg lands moves the pins in §3. Re-run the §3
  commands at integration and re-pin before citing any digest in this file.

## 3. Frozen rows this capability needs (new rows only)

The frozen-row precedent is `tools/gates/frozen/round-18/` (README: "a re-freeze
is a new recording, never an in-place edit") and the later generations
`round-20/`, `round-22/`, `round-23/`. The round-25 generation directory does
**not** exist at this seat's measurement; this section supplies the row text the
recording seat would freeze. Every digest below is measured at
2026-10-18T17:29Z (`sha256sum`, cwd = lane root).

| proposed row | gate | gate_sha256 | input | input_sha256 |
|---|---|---|---|---|
| R25-1 | `tools/gates/naming-collision-gate.py` | `d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d` | `examples/culture-d4/packet.d4.yml` | `e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3` |
| R25-2 | `tools/gates/d4-typed-labels-check-gate.py` | `05f99629d870280c55e15f46d799c29d7cfbc0645f0d0cd68a5fff1006181841` | `examples/culture-d4/typed-labels.d4.yml` | `60b526b0b3d07141875d20c472451cdf6658f61936d39fe18af4f3d981981092` |
| R25-3 | `tools/gates/d4-assembly-check-gate.py` | `df1a364b3970365c217a9b6a16f075bab854ee87aefab831de50df4a9d71544a` | `examples/culture-d4/packet.d4.yml` | `e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3` |
| R25-4 | `tools/gates/typed-pipeline-gate.py` | `879d40bf977eef659cabd7e87b7abd8dd5237cbd2cfa4c1a51c5ab622dbe4126` | `examples/culture-d4/packet.d4.yml` | `e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3` |
| **R25-5** | `tools/gates/argot-derivation-gate.py` | `07db6e9b4e01539e1dbb8af9e51eada6fe37784145915a0387f48f2ecd99f8fe` | `examples/culture-d4/packet.d4.yml` | `e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3` |

Measured verdicts for those five rows at 2026-10-18T17:28-17:33Z
(`TMPDIR=$PWD/.scratch`). Rows R25-4/R25-5 are quoted at the **settled**
17:33:42Z revision of each gate:

| row | command | exit | finding_count | stdout_sha256 |
|---|---|---|---|---|
| R25-1 | `python3 tools/gates/naming-collision-gate.py examples/culture-d4/packet.d4.yml` | 1 | 14 | `0c613c9d973f3c32bb20f4db7a43a02da7a5edcaa1bc3382531acce21e2a89f7` |
| R25-2 | `python3 tools/gates/d4-typed-labels-check-gate.py examples/culture-d4/typed-labels.d4.yml` | 0 | 0 | `1c8add321259a9f026d6e37b0dbd95b0f548f31fe0a10c56098911c21532a6fe` |
| R25-3 | `python3 tools/gates/d4-assembly-check-gate.py examples/culture-d4/packet.d4.yml` | 0 | 0 | `c60820a54742ecaa1edef972c6c94cce3f88313fbace8ef19eaeddd9a42572a7` |
| R25-4 | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | 0 | 12 | `b064da286d2dd02904788fc3fe4f3bd97fe7e88bbcac657cee114d0a607100bd` |
| R25-4b | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.typed.yml` | **0** | 12 | `38dc76dc5965ceecbb6d0aac141655344111dd558e301b2b0dfd7e741d9131ce` |
| **R25-5** | `python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | **0** | 0 | `49060ed39b8725f5f7268a24492adc52e944f80e8eff517541d2a56d0483104f` |

- Row R25-1 records a **red** verdict (exit 1, 14 findings: 7 `NAME-NEAR`,
  6 `PHON-INVENTORY` on the six garment glosses, 1 `CROSS-HOLD`). A reproduced
  red verdict stays red; recording it is the contract, not a failure.
- Rows R25-2..R25-5 are green checks on NON-CANON artifacts. R25-4's 12 findings
  equal the expected hold set (`examples/culture-d4/expected-holds.json`,
  `3826ba68d705b3c379b2a12737c14075d9095a1ba2aa2eb525de1851a9ecd2f7`).
- **R25-4b is the O claim's fix, measured.** The same gate fed the **derived
  typed packet** now reads exit 0 with the identical 12-finding set, where the
  round-24 cold run read exit 1 with two failing legs. The false red is fixed on
  the runtime path.
- **R25-5 is the argot row.** The gate is flagless and single-input by design
  (its docstring: "Flagless and single-input, so `tools/replay-frozen.py` can pin
  a row"), so it satisfies the replay tool's `[python3, <gate>, <input>]`
  contract (`tools/replay-frozen.py:183-186`) without an adapter. It reads
  exit 0 with a 253-byte stdout whose content is the `coverage:` and
  `dependency:` lines (no `^FINDING ` lines, so `finding_count` = 0).
- R25-5 cannot be frozen yet either: `tools/gates/frozen/round-25/` does not
  exist. It is a **new row in a new generation** when the recording seat runs.

## 4. Measured controls (this seat)

**(a) The relation is replayable and can fail — true-negative control.**
Baseline: `python3 tools/gates/naming-collision-gate.py examples/culture-d4/packet.d4.yml`
→ exit 1, 14 findings, **0** matching `DERIV`. Mutating the packet's only
derivation rule (`morphology.derivation_rules[0]`, `CX-01`, `output: "{a}{b}"` →
`"{a}-{b}"`) in scratch and re-running the gate:

```sh
export TMPDIR=$PWD/.scratch
cp examples/culture-d4/packet.d4.yml .scratch/r25d/ctl/packet.d4.yml
# in-place edit of the CX-01 output only
python3 tools/gates/naming-collision-gate.py .scratch/r25d/ctl/packet.d4.yml
```

Observed 2026-10-18T17:29Z: **8** `DERIV-REPLAY` FAILs (one per NM-01..NM-08),
exit 1, e.g.

```
FINDING DERIV-REPLAY: FAIL — name NM-01 'tumhai': declared chain 'CX-01' applied to 'tum+hai' yields 'tum-hai'; the stated inputs and rules do not yield the candidate
```

and the unmutated copy run from the same scratch shape reads **0** `DERIV`
findings. So the replay leg distinguishes, it does not always fail. This control
grades the **name-side** relation (`formation.stem` under CX-01) — the sibling of
Δ3's argot relation, and the only derivation relation the delivered bytes carry
today.

**(b) The delivered packet carries zero argot rows — by design, and still true
after the leg landed.** The forecast id occurs **zero** times in the delivered
artifacts, because the id is control-only and the forecast relation is declared,
not delivered:

```sh
grep -c "ARGOT" examples/culture-d4/packet.d4.yml          # 0
grep -c "ARGOT" examples/culture-d4/packet.d4.typed.yml    # 0
grep -c "ARGOT" examples/culture-d4/typed-labels.d4.yml    # 0
grep -c "ARGOT" examples/culture-d4/expected-holds.json    # 0
```

The `ARGOT` token now exists only in the **gate** (which emits the ids) — not in
any packet byte.

**(c) The argot leg itself — live measurements (this seat; rows re-run at
2026-10-18T17:33:42Z on the settled gate revision).** Gate
`tools/gates/argot-derivation-gate.py`, sha256
`07db6e9b4e01539e1dbb8af9e51eada6fe37784145915a0387f48f2ecd99f8fe`.

| # | input | exit | stdout | what it shows |
|---|---|---:|---|---|
| a | delivered D4 packet | **0** | `coverage: … records=156 register_scoped=6 derived_pairs=0 borrow_pairs=6 violations=0 rule_holds=0` | the positive run; byte-identical across two consecutive runs (determinism) |
| b | scratch packet, two records, one correct `reverse` and one wrong | **1** | `FINDING D4L-ARGOT-DERIV: FAIL — register-scoped form Q-02 'WRONG' … declared chain 'reverse' applied to 'min' yields 'nim'` | the negative control fires and names the replayed value |
| c | scratch packet with `derivation_ops: [head2, reverse]` and one register-scoped form, no pair | **1** | `FINDING D4L-ARGOT-COVERAGE: HOLD — … declared, not delivered` | a declared-but-undelivered relation is a named HOLD, never silence |
| d | scratch record declaring `derivation: palindromize` | **1** | `FINDING D4L-ARGOT-RULE: HOLD — … neither a declared argot operation (head2, reverse) nor a licensed packet rule (none)` | an unreplayable declaration is a HOLD |
| e | missing input path | **2** | `FINDING D4L-ARGOT-DATA: FAIL — input could not be evaluated: [Errno 2] …` | could-not-evaluate, no traceback |
| f | `examples/culture-d2/packet.d2.yml` | **0** | `register_scoped=0 …` | a packet with no register surface reads clean, not red |

The design's own eleven worked derivations re-derive under the gate's embedded
table (`apply_op` over `DESIGN_TABLE` → all 11 True; `saalumi`→`saalu`,
`min`→`nim`, `makun`→`nukam`), and the forecast's control C-02 is stated in the
gate's own terms (`apply_op("head2","saalumi") != "saalum"` → True).

**(d) The gate's `--selftest` — first red (missing fixtures), then green.**
Between 17:30Z and 17:33Z the gate was revised five times; the intermediate
states are recorded here because a row must not cite a red selftest:

| stamp | gate sha256 (8) | `--selftest` | cause |
|---|---|---|---|
| 17:31Z | `82f48649` | exit 1 | `selftest: FAIL — fixture unreadable: … argot-derivation-gate.yml` (neither fixture file on disk) |
| 17:32:13Z | `55f83442` | exit 1 | `.yml` landed; `.expected` missing → uncaught `FileNotFoundError` traceback |
| 17:32:30Z | `3deb6bb6` | **16/18** | `fixture-names-the-violating-form` and `coverage-hold-fires` red |
| 17:32:52Z | `75aee372` | **17/18** | `coverage-hold-fires` green; one over-specific assertion left |
| **17:33:42Z** | **`07db6e9b`** | **18/18, exit 0** | settled |

The two transient reds were real defects at those revisions and were fixed
in-flight by the implementation seat; they are recorded, not silently dropped.
The final state is green.

**(e) Gate and projector health at the settled stamp (17:33:42Z)** (so the pins
above are not taken from a broken revision):

| command | exit | observed |
|---|---|---|
| `python3 tools/gates/naming-collision-gate.py --selftest` | 0 | `selftest: OK — fixture findings 12 across 11 ids (… DERIV-REPLAY …)` |
| `python3 tools/gates/typed-pipeline-gate.py --selftest` | 0 | `19/19 checks passed — … and input-class controls` |
| `python3 tools/gates/d4-typed-labels-check-gate.py --selftest` | 0 | (delegates to the peer projector) |
| `python3 tools/d2-typed-labels.py --selftest` | 0 | `163/163 checks passed` |
| `python3 tools/gates/argot-derivation-gate.py --selftest` | 0 | **`18/18 checks passed`** |

The typed-pipeline gate's selftest was **red in between** (`KeyError:
'owed_slot_of'`, exit 1, sha `a6e8d9c8…`) while its runtime path was already
fixed; the settled revision `879d40bf…` is green at 19/19. Both facts are
recorded because the O claim's fix landed on the runtime path before the
selftest caught up.

## 5. Before-state and forecast provenance (for the row's honesty)

- Claim D's before-clause: "The round-17 D4 design forecast the argot-derivation
  discipline (head2/reverse derivation-checked forms, control-only
  D4L-ARGOT-DERIV) but it was never implemented — round 19's analysts marked it
  design-forecast, not delivered." The forecast is enumerated element by element,
  with a source line per element, at `reports/round-25/argot/forecast.md` (seat
  R25-D01..D04), which this seat re-read rather than re-derived.
- The forecast's own sources, re-hashed by this seat 2026-10-18T17:29Z:
  `reports/round-17/d4/design-brief.md` `a5fdc84dfe3f98e92068e2737f6447c9adec82ff669914b3e22963ee8447e78f`;
  `reports/round-17/d4/design-language.md` `cfc2d698559ed552c85b527c3a34e32e4fe308cfd093137483f9d3c782b462cc`;
  `reports/round-17/d4/typed-support-1.md` `16f8bb0441a367970b47090cee00e73c7f69fed677941a9ac5e00b066f11b60c`;
  `reports/round-19/knowledge/analyst-3.md` `7c588529ae7849b2c20c827701683a262d0c6932a85927d009150d382aa5bd27`.
- The delivered packet's derivation table is **CX-01..CX-03 only**
  (`examples/culture-d4/packet.d4.yml:205-226`, and the identical block in
  `packet.d4.typed.yml`): a compound and two suffixes. The forecast's `head2`
  and `reverse` operations are **absent from the delivered bytes** — the eight
  delivered names are all CX-01 compounds
  (`examples/culture-d4/components/05-naming.yml`, `formation.rule: CX-01`).
  This is the delta the D axis must name, not absorb.

## 6. Limits and `to-verify`

1. **The row is a draft; the leg is live and green at the settled revision.**
   The gate landed at 17:30Z, was revised five times, and settled at 17:33:42Z
   with `--selftest` **18/18** and the D4 run exit 0 (§4c–§4e). What still
   gates the row is `tools/gates/frozen/round-25/`: it holds the O claim's
   `gate-input/` generation but **no argot generation**, so R25-5 is a draft row
   with no recording yet.
2. **Re-pin at integration.** The pins in §3 are worktree digests at
   `f74fc940`; sibling seats are editing the tree during this wave (both the
   argot gate and `typed-pipeline-gate.py` moved inside this seat's window —
   `git status --porcelain` at 17:33Z showed both as live changes, plus
   untracked `reports/round-25/**`, `corpus/lessons/README.md` and
   `tools/gates/frozen/round-25/`). A pin taken from a moving revision is
   `to-verify` by construction.
3. **The frozen-row whitelist.** `tools/replay-frozen.py` launches only
   `*.py` files directly under `tools/gates` (`gate_path()`,
   `tools/replay-frozen.py:131-140`). A row naming `tools/d2-typed-labels.py`
   or `tools/assemble-d4-typed.py` is refused `gate_not_whitelisted` before any
   digest check — which is why rows R25-2/R25-3 exist as thin gate-shaped
   adapters over the peer tools. `tools/gates/argot-derivation-gate.py` is
   itself a gate under `tools/gates/`, so R25-5 needs no adapter.
4. **Not a promotion verifier.** Nothing in this file admits a capability row,
   verifies another seat's receipt, or promotes any axis.
5. **Out of province, reported not absorbed:** SCORECARD admission, the frozen
   generation's directory name, the missing-fixture repair, and the decision to
   freeze at all are orchestrator/integration decisions.

## 7. Counting command for this file

```sh
export TMPDIR=$PWD/.scratch
grep -c "ARGOT" examples/culture-d4/packet.d4.yml examples/culture-d4/packet.d4.typed.yml \
  examples/culture-d4/typed-labels.d4.yml examples/culture-d4/expected-holds.json   # all 0
python3 tools/gates/naming-collision-gate.py examples/culture-d4/packet.d4.yml      # 14 findings, 0 DERIV
python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml      # exit 0, 0 findings
python3 tools/gates/argot-derivation-gate.py --selftest                            # 18/18, exit 0
python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.typed.yml  # exit 0, 16/16 legs
sha256sum tools/gates/argot-derivation-gate.py tools/gates/naming-collision-gate.py \
  tools/gates/d4-typed-labels-check-gate.py tools/gates/d4-assembly-check-gate.py \
  tools/gates/typed-pipeline-gate.py
```

FILES: reports/round-25/scribe/capability-row.md | SUMMARY: D18 scribe — draft SCORECARD capability row for the argot-derivation leg, measured at the settled revision (`tools/gates/argot-derivation-gate.py` sha `07db6e9b…`, `--selftest` 18/18, D4 run exit 0 with `register_scoped=6 derived_pairs=0 borrow_pairs=6 violations=0`; five revisions landed during this seat's window and every intermediate selftest state is recorded, including the two transient reds); five proposed frozen rows' digests measured at `f74fc940` with the argot row still unrecorded (`tools/gates/frozen/round-25/` holds only the O claim's `gate-input/` generation), plus six negative/positive controls including `D4L-ARGOT-DERIV` FAIL on a wrong `reverse` form, the `D4L-ARGOT-COVERAGE` HOLD, and the 11 round-17 worked derivations all re-deriving.

