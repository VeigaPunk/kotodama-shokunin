- Seat: D08 | executor | claim D | date 2026-10-19 | baseline 9bccc9b

# D08 — spare gap-fill: the two residue items, prototyped, and the pin coupling that decides where they live

Mission (`reports/round-38/targets.json`, seat `D08`): "Spare gap-fill." Claim D
(`reports/round-38/claims.json`) lands the r36 register residue under a corrected
claim: **(a)** the register F-6 counters `derived_forms` / `derived_ok`, and
**(b)** the RL-8 era leg. This seat is the D block's spare, so it did the two
things a spare is positioned to do and the numbered design seats (D01/D02) are
not: it **prototyped both items in isolated `git archive` copies of the baseline**
and measured the **pin coupling** each one drags. Both are now known-good at the
baseline; the placement decision they force is stated in §3 and §4.

No file outside this one was written. Every command below ran in this seat's own
shell against `git archive 9bccc9b` extractions under `.scratch/`; the live tree
was never written to (`git status --porcelain` at the stamp: only `?? reports/round-38/`).

Stamp: **2026-10-19T11:08:19Z** (`date -u +%FT%TZ`), `HEAD = 9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26`,
`TMPDIR=$PWD/.scratch`, `PYTHONDONTWRITEBYTECODE=1`.

**Canon:** NON-CANON engineering evidence. A digest is integrity, never truth,
never clearance. No filed byte is edited; the patches below are DRAFTED as fenced
blocks for the integrator.

---

## 1. Residue census at the baseline — the residue is exactly three items, and F-6/RL-8 are two of them

Measured, not read from a summary:

```
$ grep -rl "derived_forms\|derived_ok" examples tools      # exit 1, no match
$ sed -n '29,47p' examples/culture-d4/typed-labels.d4.yml
  "coverage": { "labels_by_kind": {...}, "typed_labels": 82, "rank_rules_*": ...,
                "reconciliation_records": 6, "findings_total": 12 }
```

| residue | live state at `9bccc9b` | evidence |
|---|---|---|
| **F-6** `derived_forms` / `derived_ok` | **absent, and no producer exists** | `grep -rl` → no match (exit 1); the projection's coverage block carries no derivation counter |
| **RL-8** era leg | **absent** | `register-law-gate.py:121` declares `era` in `DECLARED_KINDS` but nothing grades the dating; `reports/round-26/register/rules.md:110-128` specifies `REGISTER-ERA-01` (stamp ⇒ `stage >= E1`; E0 → `D4L-ERA` FAIL); `reports/round-27/law/impl-8.md:68` names it "unimplemented … whoever grows the leg" |
| **`head2`** | **declared, no domain** | `packet.d4.yml:277` lists `head2` in `derivation_ops`; the packet's own note (`:281`) says "declared but unused: over the delivered tree it is an identity"; op census over the 8 stamp forms is `{lengthen: 6, reverse: 2}`, zero `head2` |

Claim D names (a) and (b) only. The `head2` item is not claimed; it is recorded
here so the integrator's "new coverage named (no vacuous-pass)" threshold does not
silently absorb it (§6).

**The baseline register legs are green and non-vacuous** (re-measured, clean tree):

```
$ python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
coverage: … records=187 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0   # exit 0
$ python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml
coverage: … law_rows=5 identity_rows=8 record_ids=183 registers=17 speaker_tokens=3 force_failures=0 consequence_failures=0 dangling=0 findings=0   # exit 0
$ python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml   # summary: 20/20 legs passed
```

---

## 2. F-6 — the counter emitter (DRAFT, verified in isolation)

### 2.1 The patch

`derived_forms` is the count of replayable derived pairs; `derived_ok` is the
subset that replays. Both already exist as internal counters — `derived_pairs`
and `violations` — so F-6 is a **key-set gap, not a missing capability** (K01 r36
§4 said the same). The patch renames nothing and adds two keys to the coverage line.

**File: `tools/gates/argot-derivation-gate.py`, replace `:917-921`:**

```python
    derived_ok = totals["derived_pairs"] - totals["violations"]
    print("coverage: %s records=%d register_scoped=%d derived_pairs=%d claimed_chains=%d "
          "borrow_pairs=%d violations=%d rule_holds=%d derived_forms=%d derived_ok=%d"
          % (shown, totals["records"], totals["register_scoped"], totals["derived_pairs"],
             totals["claimed_chains"], totals["borrow_pairs"], totals["violations"],
             totals["rule_holds"], totals["derived_pairs"], derived_ok))
```

**Add two selftest controls to the same file** (so the counters are *consumed*, not
merely printed — this is the vacuous-pass guard D10b is assigned to hunt). Insert
after the existing `positive-control-replayed-borrows` check:

```python
    checks.append(("derived-counters-agree-on-clean-control",
                   pos_totals["derived_pairs"] > 0
                   and pos_totals["derived_pairs"] - pos_totals["violations"]
                   == pos_totals["derived_pairs"]))
    checks.append(("derived-counters-disagree-on-negative-fixture",
                   _totals["derived_pairs"] - _totals["violations"]
                   != _totals["derived_pairs"]))
```

(`_totals` is already bound in the selftest at the fixture replay.)

### 2.2 Verified — and the counters are discriminating, not always-true

In an isolated archive, after applying the patch:

```
$ python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
coverage: … derived_pairs=8 … violations=0 … derived_forms=8 derived_ok=8      # agree
$ python3 -B tools/gates/argot-derivation-gate.py tools/gates/fixtures/argot-derivation-gate.yml
coverage: … derived_pairs=8 … violations=4 … derived_forms=8 derived_ok=4      # DISAGREE
$ python3 -B tools/gates/argot-derivation-gate.py --selftest      # 27/27 checks passed
```

`derived_forms == derived_ok` on the delivered packet and `derived_forms !=
derived_ok` on the gate's own planted-violation fixture. The signal moves with the
data; it is not a constant.

### 2.3 Pin cost: **zero**

```
$ python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet
handoff-v3: exit=0 … packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19
$ python3 -B tools/check-gate-battery.py        → baseline_exit=0, gate_revised=0
$ python3 -B tools/gates/typed-pipeline-gate.py …   → 20/20 legs passed
```

**Why.** The argot gate is in **no** frozen set: it is not a `V3_READ_SET` member,
not in the r7 `expected.json` inputs (58 entries), not a battery-registered gate
(`check-gate-battery.py:117-132`), and not in `examples/culture-d4/expected-holds.json`.
It is reached by the typed pipeline, which reads **only** `FINDING D4L-ARGOT-`
lines (`typed-pipeline-gate.py:531`), not the `coverage:` counters. So adding the
two keys moves no pin, breaks no leg, and leaves `packet 45f57132…` byte-identical.

---

## 3. The F-6 placement decision — the literal "coverage block" and the zero-cost home are different artifacts

The forecast says the **coverage block** must report the two counts
(`reports/round-17/d4/design-brief.md:306-307`). Two artifacts answer to that name,
and they are not interchangeable:

| home | what changes | pin cascade | semantic cost |
|---|---|---|---|
| **(A) the argot gate's `coverage:` line** (§2) | `tools/gates/argot-derivation-gate.py` | **none** (§2.3) | none — the gate already owns the op semantics |
| **(B) the typed projection's `coverage` object** | `tools/d2-typed-labels.py` `:2894` | **full projector cascade**: `expected-holds.json` `projector_sha256` + `projection_sha256`, the r7 `expected.json` (`tools/d2-typed-labels.py`, `typed-labels.d4.yml`), `examples/culture-d4/typed-labels.d4.yml`, a new `pin_generations` row, and a d4-typed-labels-check-gate re-freeze | **high** — the projector holds the packet but not the argot ops; it would have to re-implement `head2`/`reverse`, which `typed-pipeline-gate.py:519-522` explicitly refuses ("the sibling gate owns the semantics … never re-implemented here") |

Measured for (B): patching the projector's coverage object at `:2894` and running
`python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` → **exit 1**:

```
handoff-v3: E2E-DIGEST: examples/culture-d4/expected-holds.json projector_sha256:
  the tree recorded 2819f68769df… for tools/d2-typed-labels.py but the bytes measure b13c9ed1520a…
```

and `tools/d2-typed-labels.py --selftest` → **161/163** ("the mirror build is
byte-identical to the filed d4 projection" now fails). So (B) is not a two-key
edit; it is the whole D4 projection repin.

**Recommendation for the planner (this seat decides nothing):** land F-6 in **(A)**,
the argot gate's own coverage line, because it is the artifact that owns the
derivation semantics, it is where the numbers already exist, it costs zero pins,
and its counters are asserted by the gate's own selftest. If the integrator judges
the forecast's "coverage block" to bind the *projection* literally, (B) is the
honest reading — but it must then be priced as the full D4 projection repin in §3
row (B), not as a counter addition, and the argot semantics must still not be
duplicated in the projector.

---

## 4. RL-8 — the era leg (DRAFT, verified in isolation)

### 4.1 The rule

`reports/round-26/register/rules.md:110-112`:

```
rule REGISTER-ERA-01:
  a record with register == "stamp" must carry stage >= E1
  a `stamp` record with stage E0  ->  D4L-ERA (FAIL)
```

The delivered packet supports this cleanly: all 8 `stamp` **forms** carry `stage:
E1` (`L-55..L-62`), and the 12 other `register: stamp` rows (`QREG-02..08`,
`RGL-01..05`) carry **no `stage` key at all** — so a leg keyed on `stage` cannot
false-red on the law or identity rows.

### 4.2 The patch

**File: `tools/gates/register-law-gate.py`** — add a block iterator near
`packet_record_ids` (defined at `:214`), and insert the era leg inside
`evaluate_packet` **before** the no-law-block early return at `:258-263`
(see §4.3 for why):

```python
def packet_blocks(packet):
    """Every list block of the packet, as (block-name, rows)."""
    if not isinstance(packet, dict):
        return []
    return [(name, value) for name, value in packet.items() if isinstance(value, list)]
```

```python
    # ---- RL-8 era leg: a `stamp` form dated before the register exists (RGL-05).
    # Placed BEFORE the no-law-block early return: the dating clause is a property
    # of the form class, not of the speech-act block, so an era defect must not be
    # masked by a missing `register_law` block.
    era_floor = "E1"
    for _block, _entries in packet_blocks(packet):
        for _entry in _entries:
            if not isinstance(_entry, dict):
                continue
            if text_of(_entry.get("register")).strip() != "stamp":
                continue
            _stage = text_of(_entry.get("stage")).strip()
            if not _stage:
                continue  # a law/identity row carries no dating of its own
            if _stage < era_floor:
                counters["era_failures"] += 1
                findings.append(finding(
                    "D4L-ERA", "FAIL",
                    "%s is a `stamp` form dated %s; RGL-05 dates every stamp form "
                    "available_from %s (03-orthography), so an earlier claim is a defect"
                    % (text_of(_entry.get("id")).strip() or "?", _stage, era_floor)))
```

**Add four selftest controls** (before the `no-law-block-fires-coverage` check at
`:539`), so the leg is not vacuous:

```python
    era_text = ("registers:\n  - {id: QREG-02, register: stamp}\n"
                "register_law:\n  - {id: RGL-05, register: stamp, axis: mark, kind: era, "
                'force: "none \u2014 a dating constraint", speaker: "any speaker", '
                'consequence: "a constraint statement", design_row: []}\n'
                "lexicon:\n"
                "  - {id: L-99, term: tuum, register: stamp, stage: E0}\n"
                "  - {id: L-98, term: kit, register: stamp, stage: E1}\n")
    era_fired = _classes(run(era_text)[1], "D4L-ERA")
    checks.append(("era-leg-fires-on-early-stamp-form", len(era_fired) == 1))
    checks.append(("era-leg-names-the-row-and-the-stage",
                   bool(era_fired) and "L-99" in era_fired[0]["message"]
                   and "E0" in era_fired[0]["message"]))
    checks.append(("era-leg-silent-on-e1-stamp-form",
                   not _classes(run(era_text.replace("stage: E0", "stage: E1"))[1],
                                "D4L-ERA")))
    checks.append(("era-leg-not-masked-by-missing-law-block",
                   bool(_classes(run("lexicon:\n"
                                     "  - {id: L-99, term: tuum, register: stamp, stage: E0}\n")[1],
                                "D4L-ERA"))))
```

### 4.3 The trap the design must not fall into

The natural insertion point — beside the other `kind` checks at the end of the
`for row in speech:` loop — is **wrong**: `evaluate_packet` returns early at
`:258-263` when the packet has no `register_law` block (`D4L-LAW-COVERAGE`). A
packet whose only defect is an E0 stamp form would then read clean. The patch
places the leg above that return, and the fourth selftest control pins exactly
that (an E0 stamp form with no law block still fires). This is the placement
defect a mechanical "add a check" edit would ship.

### 4.4 Verified

```
$ python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml
coverage: … findings=0      # exit 0 — the 8 stamp forms are all E1; law/identity rows carry no stage
$ python3 -B tools/gates/register-law-gate.py --selftest
selftest: 49/49 checks passed     # 45 + the 4 new controls
# planted control: L-55 stage E1 -> E0 in an isolated copy of the packet
$ python3 -B tools/gates/register-law-gate.py .scratch-planted.yml
FINDING D4L-ERA: FAIL — L-55 is a `stamp` form dated E0; RGL-05 dates every stamp form available_from E1 (03-orthography), so an earlier claim is a defect
coverage: … findings=1      # exit 1
```

### 4.5 Pin cost: **one pin, and it must be paid in the same edit set**

Unlike F-6, the law gate **is** a registered gate with a frozen baseline. Measured:

```
$ python3 -B tools/check-gate-battery.py        # with only the gate edited
"summary": { "baseline_exit": 2, "pinned": 19, "unevaluable": 1,
             "readings": { "gate_revised": 1, "pinned": 19 } }
  BASELINE-GATE-REVISED: gate_sha256 15f8b23251ca2ad0… differs from the live
    register-law-gate.py …: re-freeze, never compare across an unnamed revision
```

`tools/check-gate-battery.py:540` compares the baseline's `gate_sha256` against
the live script. The frozen row is
`tools/gates/expected/register-law-gate/r30-post/expected.json`
(sha256 `4070e76bbc3c4b57717e46510f88d60f5fa9de7a0fc4be195cee667fad4a8296`).

**Two routes, both measured:**

- **New baseline id (the standards-conforming route).** `expected.json`'s own
  `append_only_note` reads "never rewritten: a gate/input revision produces a NEW
  baseline id (`gate-frozen-run-standard.md` section 3)", and the d4-typed-labels
  gate's three rows (`r19-pre`/`r20-post`/`r22-post`) show the precedent — each
  new id names the one it `supersedes`. A new dir added **alone** still reds the
  old row (measured: `gate_revised=5`, `baseline_exit=2`); it clears only when the
  old row's stale `gate_sha256` is resolved.
- **In-place repin of `r30-post`.** Measured: updating `gate_sha256` **and** the
  mirrored snapshot copy `r30-post/tools/gates/register-law-gate.py` together →
  `baseline_exit=0, pinned=20, gate_revised=0`. Updating the JSON alone is not
  enough — the battery also hash-checks the mirrored snapshot and reports
  `BASELINE-TAMPERED`.

**Integrator note:** either route is a real, priced cost that claim D's
`after_required` ("pins updated as new rows") anticipates but does not size. The
law-gate edit, its new/repinned baseline, and the refreshed snapshot must land as
one edit set or the battery reds.

---

## 5. What is verified, and by what

| item | verified at `9bccc9b` | command | result |
|---|---|---|---|
| F-6 emitter | isolated archive | argot gate on D4 packet / on negative fixture | `derived_forms=8 derived_ok=8` / `8,4` |
| F-6 zero pins | isolated archive | `exercise-handoff-e2e.py --profile v3 --quiet`; `check-gate-battery.py` | exit 0, `packet 45f57132…`; `baseline_exit=0` |
| F-6 selftest | isolated archive | argot `--selftest` | 27/27 |
| RL-8 era leg | isolated archive | law gate on D4 packet | exit 0, `findings=0` |
| RL-8 fires | isolated archive | law gate on planted E0 packet | exit 1, `D4L-ERA … L-55 … E0` |
| RL-8 selftest | isolated archive | law `--selftest` | 49/49 |
| RL-8 pin coupling | isolated archive | battery after gate-only edit / after repin+snapshot | `baseline_exit=2, gate_revised=1` / `baseline_exit=0, pinned=20` |

Both patches are DRAFTED fenced blocks for the integrator; neither is applied to
the live tree by this seat.

---

## 6. The `head2` item — recorded, not claimed

`head2` is declared in `packet.d4.yml:277` and is an identity over the delivered
tree (`:281`; op census `{lengthen: 6, reverse: 2}`). It is **not** in claim D, and
this seat does not absorb it. Named so a reviewer does not read "the register
residue landed" as covering it: F-6 and RL-8 close two of the three r36 residue
items; `head2` remains open, and its honest disposition is either a measure-word
stratum (a component decision) or a recorded permanently-declared-but-unused
operation. Owner: the D executor who scopes the residue, per K01 r36 §6.

## Owed

- **F-6 placement decision** (argot coverage line vs projection coverage block) —
  the planner's/integrator's call; §3 gives both patches and both pin prices.
  Owner: `P01` / the integrator.
- **RL-8 baseline re-freeze** — a new `r30-post`-successor baseline id (or an
  in-place repin + refreshed mirrored snapshot) in the **same** edit set as the law
  gate. Owner: whoever applies the RL-8 patch; §4.5 has the measured route.
- **`head2`** — not closed by this round; owner per §6.
- **`run-validation.py` for round 38** does not exist at this stamp (`ls
  reports/round-38/run-validation.py` → absent), so claim D's counting command
  `python3 reports/round-38/run-validation.py` is `to-verify` until the integrator
  lands it. Per F-C13-1 it must not be run in-tree regardless.
- **Not measured by this seat:** the full `assemble-culture-d4.py --selftest` /
  `--check` under the patched gates (the patch set does not touch the assembler or
  any component, and `--check` was not re-run after the law patch). The assembler
  reads components, not the law gate, so no coupling is expected; recorded as
  unmeasured rather than assumed.

## Citations

Files (sha256 measured 2026-10-19T11:08:19Z, cwd = lane root, `TMPDIR=$PWD/.scratch`):

```
b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb  tools/gates/argot-derivation-gate.py
15f8b23251ca2ad0a203bb1ed5fda2611dff9514e6a1af8120f520b1e7ec4169  tools/gates/register-law-gate.py
2819f68769dfc0b57f46cdaeb4c9a96324c5711c46348f5a8308382dfd7053c3  tools/d2-typed-labels.py
b749ad07cf1710279aea557c071587cf4b3a228a9fb4d03398b4b94d2f32ad85  tools/gates/typed-pipeline-gate.py
4070e76bbc3c4b57717e46510f88d60f5fa9de7a0fc4be195cee667fad4a8296  tools/gates/expected/register-law-gate/r30-post/expected.json
aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3  examples/culture-d4/packet.d4.yml
c23b0ab532cfb9d4bb403405c6996982a447098048e08facbbc9f341ea13f82e  examples/culture-d4/typed-labels.d4.yml
e6ae9828d6c82aa6e14431a02840ad565f9f7c30a660afcbed1b1079166bfba3  examples/culture-d4/expected-holds.json
c4c35294d581b204482427b3776776c57d1e7f83065a0b5f8f3906c38d8c2ccd  tools/gates/fixtures/argot-derivation-gate.yml
bbe15887b710bb36def5e1c82fa5b1c1ef37df3cb5581c7c2982a0498e829d55  reports/round-34/handoff/declared-in-r7/expected.json
```

Commands run (lane root, `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`; isolated
copies = `git archive 9bccc9b | tar -x -C .scratch/d08<letter>`):

```
grep -rl "derived_forms\|derived_ok" examples tools                        # no match, exit 1
python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml          # exit 0
python3 -B tools/gates/argot-derivation-gate.py tools/gates/fixtures/argot-derivation-gate.yml  # exit 1, 4 DERIV
python3 -B tools/gates/argot-derivation-gate.py --selftest                 # 27/27
python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml              # exit 0, findings=0
python3 -B tools/gates/register-law-gate.py --selftest                     # 45/45 baseline, 49/49 patched
python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml            # 20/20
python3 -B tools/d2-typed-labels.py --selftest                             # 163/163 baseline, 161/163 after projector probe
python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet              # exit 0, packet 45f57132…
python3 -B tools/check-gate-battery.py                                     # baseline_exit=0 clean; 2 gate_revised=1 after law-only edit
git rev-parse HEAD                                                         # 9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26
date -u +%FT%TZ                                                            # 2026-10-19T11:08:19Z
```

Source lines cited: `tools/gates/argot-derivation-gate.py:917-921`;
`tools/gates/register-law-gate.py:121,214,246,258-263,374,539`;
`tools/d2-typed-labels.py:2894`; `tools/gates/typed-pipeline-gate.py:519-522,531`;
`tools/check-gate-battery.py:117-132,540`;
`examples/culture-d4/packet.d4.yml:277,281`;
`examples/culture-d4/typed-labels.d4.yml:29-47`;
`reports/round-17/d4/design-brief.md:296-310` (Δ3, F-6 at `:306-307`);
`reports/round-25/argot/forecast.md:33-41`;
`reports/round-26/register/rules.md:110-112,128`;
`reports/round-27/law/impl-8.md:68`;
`reports/round-36/scout/K01-register-scout.md` §4-§5;
`tools/gates/expected/register-law-gate/r30-post/expected.json` (`append_only_note`);
`tools/gates/expected/d4-typed-labels-check-gate/{r19-pre,r20-post,r22-post}/expected.json`.
