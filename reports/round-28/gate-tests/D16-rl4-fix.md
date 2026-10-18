# R28-D16 — the RL-4 fix, present by record id, with a control that can say no

- **Seat:** R28-D16 (gate runs 4 of 4), round 28, loop 3 build 4 of 4, claim **D**
  `register-law-replay` (`reports/round-28/claims.json:9-18`).
- **Date:** 2026-10-18 (measurements 20:1x–20:2xZ). Declared baseline
  `6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede`; lane HEAD
  `69cecbc7dcf575a29f29660ecac470e05260fd86`.
- **Write scope:** this file only; scratch under `.scratch/r28-d13/`.
  `export TMPDIR=$PWD/.scratch` preceded every scratch-writing command. No
  component, packet, tool, fixture or filed rounds 8–27 byte was written.
- **Canon:** NON-CANON engineering evidence.

## 0. Verdict

**RL-4 is closed, and this seat closes it with a control rather than an
assertion.** The round-27 review measured that `03-orthography.yml` and
`09-costumes.yml` declared no `packet_keys` covering their record blocks, so
`OR-01..03`, `LI-01..03` and `EN-01..02` never reached the packet. Measured now:
all eight records are present **as records**, the two components declare the keys,
and the keys have left `assembly.skipped_keys`.

| check | result | evidence |
|---|---|---|
| every OR/LI/EN record reaches the packet **by id** | **yes, 8/8** | `records`→`OR-01..03`, `literacy_institutions`→`LI-01..03`, `enforcement`→`EN-01..02` |
| the component-only keys left `assembly.skipped_keys` | **yes** | none of `records`, `literacy_institutions`, `enforcement` is skipped |
| `03-orthography.yml` declares `packet_keys` | **yes** | `[orthography, records, literacy_institutions]` |
| `09-costumes.yml` declares the `enforcement` key | **yes** | `[costumes, materials, cloth_sources, rank_rules, form_slots, enforcement]` |
| the RL-4 control reproduces the round-27 defect | **yes** | stripping the declaration pushes all six OR/LI records back out |

Measured directly on the amended packet:

```
records:                OR-01, OR-02, OR-03
literacy_institutions:  LI-01, LI-02, LI-03
enforcement:            EN-01, EN-02
```

Pinned at the measurement:

```
examples/culture-d4/packet.d4.yml      sha256 543d68a82640e1b0c53b9cb7cb26c4dc60fce5878c2bf487050ead3af0945c4f
examples/culture-d4/components/03-orthography.yml
                                       sha256 0f2ff45439fd7db3e9014bd1012bd917e42d042f457b8cef2bed2c9a791d4e1b
examples/culture-d4/components/09-costumes.yml
                                       sha256 f61cc6845518d44f50e5179339a1a2fda2c5290efb52d6badb28cbec87768c23
tools/gates/register-law-gate.py       sha256 cfbff16bbb67d94d39b8d19f7f3fa14d985d18d1f306c8b8e39f79d20ad00e5e
```

**The id-based check is the load-bearing one.** A fix that declared the
`packet_keys` but dropped the records would leave the block empty and the ids
absent; a fix that homed the records under a differently-named block would still
pass, because the check asks "is this id a packet record", not "is this block
called `records`". That is deliberate: the claim requires the records to be
**present in the packet as records**, and the block name is the component's
choice.

## 1. The control: the check can say no

A presence check that cannot fail is not a check. The control strips the
orthography component's `packet_keys` declaration in a **clone**, rebuilds
through the lane's own assembler, and requires the records to leave:

```
$ python3 - <<'PY'   # clone, strip, rebuild, read the packet
landed: True
assemble exit 0 ['Wrote examples/culture-d4/packet.d4.yml (96989 bytes)']
OR/LI present after strip: []
skipped after strip: {'records': ['examples/culture-d4/.../03-orthography.yml'],
                      'literacy_institutions': ['examples/culture-d4/.../03-orthography.yml']}
```

The clone reproduces **the round-27 defect exactly**: with the declaration gone,
the assembler falls back to the `PACKET_KEYS` allowlist, the record blocks are
recorded under `assembly.skipped_keys`, and the ids vanish from the packet. The
control is measured in a clone, never the lane worktree — a control that moves
the tree it measures is not a control.

The same edit under round 27 would have been the *delivered* state; the control
therefore demonstrates that the fix, not the passage of time, is what closed the
gap.

## 2. The standing argot regression detector

The RL-4 packet change moved the D4 surface, so this seat re-runs the regression
detector the round-27 battery left in place. It is read **read-only** from
`reports/round-27/gate-tests/fixtures/` so this battery adds no fixture of its
own and cannot accidentally re-pin the old one.

| check | result |
|---|---|
| the design's eleven worked rows all re-derive | **yes, 11/11** |
| exactly one reading of `head2(tumkalker)` derives | **yes** — `s2` (constrained, `tumkal`) clean; `s1` (unconstrained, `tumka`) reads `D4L-ARGOT-DERIV` |
| the non-deriving reading names `D4L-ARGOT-DERIV` | **yes** |
| the gate agrees with the design's own worked row | **yes** — `head2(saalumi) == saalu` |
| the argot selftest still passes | **yes** — `27/27 checks passed` |

The reading pair is the discriminating detector: exactly one of the two readings
derives, so a change that made **both** clean (the leg stops discriminating) or
**both** red (the pair collapsed) fails. It stayed a pair across the packet move.

## 3. What this seat does not claim

- **The fix's correctness is not this seat's judgment.** This seat measures that
  the records reach the packet and that the components declare the keys. Whether
  the records *should* be in the packet, and whether the law's `mold-keeper`
  citation is now resolvable, are the design seats' calls. The peer measurement
  corroborates the direction: `OR-02` now resolves as a delivered record id
  (`.scratch/r28-d19/groundtruth-delta.txt`: round-27 `record_ids=171`,
  `OR-02 present=False`; round-28 `record_ids=179`, `OR-02 present=True`).
- **The hold set's counts are claim O's to re-verify, not this seat's.** They were
  unverifiable while the profile leg aborted (see `D14-typed-gate.md` §1); with
  the re-pin landed they read `{hold: 12, note: 0, fail: 0}`, equal to the frozen
  set. This seat records the fact and leaves the re-pin itself to claim O.
- **A green presence check is not enforcement.** The records being visible to
  gates is not the same as a gate checking them. That separate gap — RL-1 — was
  closed this same round by `tools/gates/register-law-gate.py`, and it is graded
  under D15, not here.

## 4. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
python3 -c "import runpy;n=runpy.run_path('tools/gates/naming-collision-gate.py');\
p=n['load_yaml'](open('examples/culture-d4/packet.d4.yml').read());\
print([r['id'] for r in p['records']],[r['id'] for r in p['literacy_institutions']],[r['id'] for r in p['enforcement']])"
grep -n '^packet_keys:' examples/culture-d4/components/03-orthography.yml examples/culture-d4/components/09-costumes.yml
python3 reports/round-28/gate-tests/run-gate-tests.py       # D16 checks, receipt rl4
python3 tools/gates/argot-derivation-gate.py reports/round-27/gate-tests/fixtures/s2-head2-constrained.yml
```
