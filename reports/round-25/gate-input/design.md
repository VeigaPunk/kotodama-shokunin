# Round 25 — O R25-O01..O03 — gate-input minimal-fix design

- **Seat:** R25-O-gate-input, round 25 (claim O, before-clause (a)).
- **Date:** 2026-10-18. Companion to `diagnosis.md` in this directory, which
  carries the reproduction and the byte-level evidence.
- **Status:** **this seat did not edit the real
  `tools/gates/typed-pipeline-gate.py`.** A **sibling round-25 seat (O08..O10)**
  landed a stronger fix **and** the repin cascade in the working tree while this
  file was being written (final sha
  `879d40bf977eef659cabd7e87b7abd8dd5237cbd2cfa4c1a51c5ab622dbe4126`) — §8
  verifies that revision against this seat's whole control set. The patch below
  was proved on a scratch copy (`.scratch/r25-o1/gate-patched.py`) before the
  sibling's landed; it is kept as the independent second derivation, and §8.1
  maps it against what shipped. Per the claim's own `after_required` the accepted
  outcome is "either a named input-class diagnostic … or the L2/L3 legs handle
  null owed_slots correctly" — the landed revision satisfies **both** branches
  (input class + `owed_slot_of`), where this seat's §3 does the latter and §6
  had listed the former as the alternative.

## 1. Requirements the fix must satisfy

From the claim's `after_required`, plus the lane's standing rules:

1. Feeding the typed packet back **can no longer manufacture findings**.
2. The gate **fails closed and honestly** on any real defect — every existing
   negative control must still exit 1 or 2.
3. The documented source-packet entry (`… packet.d4.yml`) still passes **19/19**,
   and the flagless D2 default and the D2 typed direction must be
   **byte-identical** (the round-18 O claim: the default path is exactly the
   pre-generalization behavior).
4. Pins are **new rows**; no filed artifact of rounds 8–24 is edited.

## 2. Minimal fix, part 1 — the L2 legacy arm reads the declared source

`tools/gates/typed-pipeline-gate.py:588-608` becomes:

```python
    legacy_bytes = None
    source_doc = None
    declared_legacy = Path(config["packet"])
    if typed_arg is not None and declared_legacy.is_file():
        try:
            source_doc = load_packet_strict(
                declared_legacy.read_text(encoding="utf-8"), reader).get("packet")
        except Exception:
            source_doc = None
    if carries_typed_document(source_doc, typed_doc):
        # the declared, digest-verified legacy packet is the L2 legacy arm: the
        # pipeline's own source packet, not a rebuild of its product
        legacy_bytes = declared_legacy.read_bytes()
    elif typed_arg is not None:
        # reconstruct the legacy packet by moving the off-channel fields back
        …                                          # unchanged fallback
    else:
        legacy_bytes = Path(packet_path).read_bytes()
```

with, next to `moved_field()`:

```python
TYPED_ONLY_KEYS = ("typed_channel", "typed_pipeline", "typed_assembly", "assembly",
                   "pipeline_findings", "pipeline_counts", "schema")


def carries_typed_document(source_doc, typed_doc):
    """True when the declared source is the document the typed packet came from.

    A typed packet's non-typed keys are a superset of its source's: the adapter
    moves a field and appends its own blocks, it drops nothing. A declared
    source that does not carry them is not this packet's source (the round-18 d9
    fixture declares a three-key stub), and the rebuild stays the fallback.
    """
    if not isinstance(source_doc, dict) or not isinstance(typed_doc, dict):
        return False
    return (set(typed_doc) - set(TYPED_ONLY_KEYS)) <= set(source_doc)
```

**Why this is the minimal and the *faithful* fix.** `config["packet"]` is not a
guess: it is the pipeline's declared source, and the gate already verifies its
digest on this very run — the `d4` profile pins
`e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3` in
`tools/gates/typed-pipelines.json` (`L1-profile`), and the typed packet's own
`assembly.packet_sha256` carries the same digest, which `L4-pins` re-verifies.
The information the leg needs was already in hand; line 608 simply never read
it. No new file, flag, or declaration channel is introduced.

**Why the guard is required, not optional.** The unguarded form of this branch
was written first and **broke a pinned control**: `--selftest-generalized` fell
from 14/14 to 11/14, because the round-18 d9 fixture declares a *three-key byte
stub* as its source (`examples/culture-d9/packet.d9.yml` = `name`/`assembly`/
`components`), which the five gates cannot grade — `L2-channel` returned exit 2
("phonology-sanity-gate.py: exit 2"). The containment test keeps the declared
source as the legacy arm exactly when it *is* the packet's source (the D2 and
D4 real pipelines: 34 ⊆ 39 keys) and leaves the fixture on the rebuild fallback.

**Residual exposure (must be stated, not hidden).** When the declared source is
unreadable or is not the packet's source, the rebuild fallback still runs, so a
*genuinely unfaithful* rebuild can still be graded. That is the no-declared-
source case — not the D4 case — and §5.4 R3 names the stronger form (fail closed
with a named input-class diagnostic instead of silently rebuilding).

## 3. Minimal fix, part 2 — the null-ish guard the leg was missing

Add the guard next to `moved_field()` and use it in `routed_slots`:

```python
def nullish(value):
    """A routing scalar that names nothing: missing key, empty, or the lane's
    reader keeping an unquoted `null`/`none`/`~` as its own string."""
    if not isinstance(value, str) or value.strip().lower() in ("", "null", "none", "~"):
        return None
    return value
```

```python
-    routed_slots = sorted(row.get("owed_slot") for row in routing
-                          if moved_field(row) and row.get("owed_slot"))
+    routed_slots = sorted(slot for row in routing
+                          if moved_field(row)
+                          and (slot := nullish(row.get("owed_slot"))))
```

`moved_field()` is left alone (its `off_channel_field` guard is correct);
`nullish()` is the same predicate factored out so the two routing keys cannot
drift apart again. The walrus keeps the filtered value rather than re-reading
the key.

**Deliberately NOT changed:** `routing_hold_ids` (`:741`) uses the same bare
truthiness test, and `hold` is a *required* key on a moved row, so the honest
failure mode there is different (see §5.4 R1/R2). Changing it here would widen
the blast radius past the claim without closing a measured false red.

## 4. Patch size, and the pin cascade it triggers

The proved patch is **3 hunks, +41/−3 lines** (two new functions, one branch, one
expression):

```
$ diff -u tools/gates/typed-pipeline-gate.py .scratch/r25-o1/gate-patched.py
@@ -183,6 +183,31 @@   +TYPED_ONLY_KEYS, +nullish(value), +carries_typed_document(…)
@@ -585,7 +610,19 @@  the declared-source branch
@@ -745,8 +782,9 @@  routed_slots = … nullish(…) …
41 added, 3 removed; 1360 → 1398 lines
```

`typed-pipeline-gate.py` is sha-pinned, so the fix is a **re-pin cascade**, routed
like the round-22→25 recipe (new rows, never edits to filed receipts):

| pin that moves | where | new row |
|---|---|---|
| gate sha `04ad4bb4…` → live digest | `tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv` row 4 | a `reports/round-25/gate-input/repin.json` row + a `tools/gates/frozen/round-25/…` manifest; the round-22 MANIFEST stays as filed |
| `tools/gates/frozen/{round-11,round-18/repin-d2,round-20/repin-d2,round-23/repin-d2}/MANIFEST.tsv` gate column | same shape | same |
| `tools/gates/typed-pipelines.json` (no gate sha field today) | — | unchanged |
| `tools/check-gate-battery.py` baselines | only if a baseline pins this gate | verify; none found in `tools/gates/expected` or `tools/gates/frozen/*/expected.json` |

## 5. Verification — controls, all on the scratch copy

Patched gate (v2, the form in §2/§3) sha
`0e3152c750113edeb4e63ce3979f486c968f13132469e6af2a3317c450fc5fae`.
All commands 2026-10-18, `TMPDIR=$PWD/.scratch`.

### 5.1 The false red is gone (claim requirement 1)

| Input | Unpatched | Patched |
|---|---|---|
| `examples/culture-d4/packet.d4.typed.yml` | exit **1**, 14/16 | exit **0**, **16/16** |

```
$ python3 .scratch/r25-o1/gate-patched.py examples/culture-d4/packet.d4.typed.yml
ok   L2-channel
ok   L3-routing-consistency
summary: 16/16 legs passed
```

`--json`: `ok: true`, `exit_code: 0`,
`sound_channel = {"added": 0, "removed": 6, "routed": 12, "translated_on_sound_channel": 0}`
— the six real field moves, zero added findings. The leg's two halves now agree
with each other and with the packet.

### 5.2 No regression (claim requirement 3 — byte-level, not just exit-level)

| # | Run | Patched | Identity check |
|---|---|---|---|
| C1 | source packet `… packet.d4.yml` | exit **0**, 19/19 | stdout sha `b064da286d2dd029…` = the `d4-repin` MANIFEST pin `b064da286d2dd02904788fc3fe4f3bd97fe7e88bbcac657cee114d0a607100bd` |
| C2 | `--selftest` | exit **0**, 12/12 | stdout **byte-identical** to the unpatched selftest |
| C2b | `--selftest-generalized` | exit **0**, 14/14 | 14/14; the unguarded form of §2 scored **11/14** — this is the control that forced the `carries_typed_document` guard |
| C3 | flagless (D2 default) | exit **0**, 16/16 | stdout **byte-identical** to unpatched |
| C4 | `examples/culture-d2/packet.d2.typed.yml` (D2 typed direction) | exit **0**, 13/13 | stdout **byte-identical**, sha `9a69985aabdf3e9b…` |
| C5 | frozen round-11 typed row | exit **0** | stdout sha `9a69985aabdf3e9b…` = the pinned `9a69985aabdf3e9bf233653f7b31ce6f3bf5fd12858cfedf7e9ebca14ada4606` |

C5 generalised to **all five frozen `typed-pipeline-gate.py` rows** (round-11,
round-18/repin-d2, round-20/repin-d2, round-22/d4-repin, round-23/repin-d2):
**5/5 reproduced, `bytes=match`**, exit codes 0/0, counts equal. Full manifest
replay under an out-of-repo TMPDIR still reports
`REPLAY OK: 3/3 rows reproduced` for the `d4-repin` manifest.

The fix is therefore **behavior-preserving on every path the lane has pinned**,
including the D2 typed direction — which also proves the declared-source branch
is a no-op there (D2 declares no `assembly`/`typed_pipeline` source, so
`config["packet"]` is `PACKET_DEFAULT`… which *is* the file D2's `main()` passes
as `packet_path`; both arms read the same bytes).

### 5.3 It still fails closed on real defects (claim requirement 2)

| # | Negative control | Patched | What fires |
|---|---|---|---|
| N1 | one routing row dropped (`GAR-06`) | exit **1** | `FAIL L2-channel` (PHON-INVENTORY on the un-moved field) + `FAIL L3-routing-consistency` (holds 12 vs routed 11) |
| N2 | `owed_slot: "LEX-GAR-99"` on the `GAR-01` row | exit **1** | `FAIL L3-routing-consistency` — `routed` gains `LEX-GAR-99` |
| N3 | `GAR-01` field never moved, routing still claims the move | exit **1** | `FAIL L2-channel` — "off-channel lines in the typed run: … GAR-01 …" |
| N4 | `--legacy-packet <the typed packet>` (self-referential arm) | exit **2** | `FAIL L1-assembler` — bytes `ffece0fe…` ≠ the assembler's deterministic `e7ecd204…` |

N2 is the key control for part 2: the `nullish()` filter drops only
`''`/`'null'`/`'none'`/`'~'`; **any other string still enters the comparison**,
so a smuggled slot is caught. N1 and N3 are the controls for part 1: with the
declared source read, the L2 leg still catches a field that did not move and a
row that vanished.

### 5.4 Named residuals (not fixed; the claim's "honestly" clause must not be over-read)

- **R1 (new, this diagnosis — `hold: null` on a moved row):** patched gate exit
  **0, 16/16**; the reader's `'null'` string is kept as a hold id by
  `routing_hold_ids` (`:741`) and the resulting mismatch cancels out. Same gap on
  the source path (unpatched source run is 19/19 with the same code).
- **R2 (new — the `hold` key absent on a moved row):** patched gate exit
  **0, 16/16**; the record drops out of both sides of the comparison.
- **R3 (inherited from round 24, N3):** the rebuild fallback in §2 still exists
  for a pipeline whose declared source is unreadable or is not the packet's
  source. A stronger form — *refuse* with a named input-class diagnostic ("this
  is a typed packet and its declared source is not readable; grade the source")
  at exit 2 — is the alternative the claim's `after_required` allows, and would
  remove the fallback entirely.
- **R4 (structural, from `diagnosis.md` §3.4):** `moved_records` (`:572`) is
  built from all 12 routing rows while only 6 costumes move a field; the
  `generalized` branch at `:658-664` patches around it. It is latent and not a
  measured false red today, but it is why `L2-channel`'s detail says
  "removed 6, routed 12".

R1/R2/R4 are **out of scope** for R25-O01..O03 (they are not the two reproduced
symptoms and none is exercised by the claim's counting command). They are named
so the round does not promote "the L3 leg is honest" beyond what was measured.

## 6. What the parent must decide

1. **Nothing blocking on the gate itself** — a sibling seat (O08..O10) has landed
   both a stronger fix and the §4 repin cascade (§8), and this seat's whole
   control set passes against the settled revision. What remains open is the
   **observability** gap: `reports/round-25/run-validation.py` checks this
   surface only via `replay-frozen.py --selftest`, which does not replay a
   manifest, so neither the new generation's `6/6` nor the earlier manifests'
   declared refused rows are observed by the round's counting command (§8.3).
2. **Part 2 alone or both parts?** Moot for the landed revision, which ships
   both. It stays relevant if the patch is ever re-derived: part 1 (declared
   source) removes the `DERIV-REPLAY` class and is the honest fix; part 2 (the
   null-ish guard) removes the phantom slots. They are independent — either alone
   changes the typed run's verdict, and part 2 alone leaves the manufactured
   `DERIV-REPLAY` lines in place (L2 would still fail). **Part 1 must ship in a
   guarded form** — this seat's `carries_typed_document` (§2), the landed
   revision's digest-check + input class (§8.1), or its `phonology`-non-empty
   test: the *unguarded* form breaks `--selftest-generalized` (14/14 → 11/14)
   against the round-18 d9 fixture.
3. **The §5.4 R3 alternative** (fail closed with a named input-class diagnostic,
   exit 2) if the parent prefers the first branch of the claim's
   `after_required` over the declared-source read.

## 7. Reproduce everything

```bash
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch
# 1. the false red
python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml          # 0, 19/19
python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.typed.yml   # 1, 14/16
# 2. the patch (3 hunks; scratch copy only)
cp tools/gates/typed-pipeline-gate.py .scratch/r25-o1/gate-patched.py                # then apply §2/§3
python3 .scratch/r25-o1/gate-patched.py examples/culture-d4/packet.d4.typed.yml      # 0, 16/16
python3 .scratch/r25-o1/gate-patched.py examples/culture-d4/packet.d4.yml            # 0, 19/19
python3 .scratch/r25-o1/gate-patched.py --selftest                                   # 0, 12/12
python3 .scratch/r25-o1/gate-patched.py --selftest-generalized                       # 0, 14/14
python3 .scratch/r25-o1/gate-patched.py                                              # 0, 16/16 (D2 default)
# 3. negative controls (inputs under .scratch/r25-o1/neg/)
python3 .scratch/r25-o1/gate-patched.py .scratch/r25-o1/neg/dropped-row.yml          # 1
python3 .scratch/r25-o1/gate-patched.py .scratch/r25-o1/neg/smuggled-slot.yml        # 1
python3 .scratch/r25-o1/gate-patched.py .scratch/r25-o1/neg/unmoved-field.yml        # 1
```

Scratch artifacts (gitignored): `.scratch/r25-o1/{source-run,typed-run,typed-patched,
source-patched,st-*,d2-default-*,d2t-*,frozen-r11-patched}.txt`,
`.scratch/r25-o1/rebuilt-legacy.yml`, `.scratch/r25-o1/rebuilt-pattern-fixed.yml`,
`.scratch/r25-o1/neg/*.yml`, `.scratch/r25-o1/gate-patched.py`.

## 8. Addendum — a sibling seat (O08..O10) landed a stronger fix and the repin cascade while this file was written

**This seat did not edit `tools/gates/typed-pipeline-gate.py`.** My writes are
`reports/round-25/gate-input/` only (`git status` shows the gate as modified by
another seat). Two sibling edits landed during this seat's run, and the final
state is theirs:

| when | sha | state |
|---|---|---|
| start (pinned) | `04ad4bb4…` | the false red of §1 reproduces |
| 14:31:07 | `ec65d655…` | first fix; `--selftest-generalized` green; earlier manifests begin to refuse |
| 14:31:58 | `a6e8d9c8…` | **transiently broken** — `--selftest` raised `KeyError: 'owed_slot_of'` |
| 14:33:25 (settled) | **`879d40bf977eef659cabd7e87b7abd8dd5237cbd2cfa4c1a51c5ab622dbe4126`** | the final revision: stronger fix + full cascade |

The 14:31:58 break is worth flagging: for about 90 seconds the lane's gate did
not run at all. All results below are against the settled `879d40bf…`.

### 8.1 The landed fix is a superset of this seat's design

| | this seat's design (§2/§3) | landed revision (`879d40bf…`) |
|---|---|---|
| null-ish owed-slot guard | new `nullish()` in `routed_slots` | new `owed_slot_of(row)` (`:213`) in `routed_slots` |
| L2 legacy arm | read `config["packet"]`, guarded by `carries_typed_document` | read the **declared source**, digest-checked against the pin the typed packet carries (`:636-648`) |
| when no source resolves | silent rebuild (named as residual R3) | named input class + refusal (see below) |
| new leg | none | `L2-legacy-source` / input-class reporting |
| patch size | +41/−3, 3 hunks | ~+200 lines incl. selftest controls |

The convergence on the two root causes is the useful signal: two independent
seats, from the same round-24 reading, found the same two surfaces. The landed
revision additionally implements **the first branch of the claim's
`after_required`** — the named input-class diagnostic — which this seat had left
as the §6 alternative: `result["input_class"]` takes
`typed-declared-source` / `typed-unresolvable` / `typed-stale-source` /
`typed-rebuilt` / `typed-unfaithful-rebuild` (`:631-660`, `:756-758`), and
`typed-unresolvable` / `typed-stale-source` are exit-2 refusals. So the claim's
`after_required` is satisfied by **both** of its allowed branches, not one.

### 8.2 Verified by this seat against the settled `879d40bf…` (14:3x, `TMPDIR=$PWD/.scratch`)

| check | result |
|---|---|
| `… packet.d4.typed.yml` | exit **0**, 16 legs, `input_class = typed-declared-source` |
| `… packet.d4.yml` | exit **0**, 19/19 — stdout **byte-identical** to the pre-fix capture |
| `--selftest` / `--selftest-generalized` | exit **0** / exit **0** |
| flagless D2 / D2 typed | exit 0, **byte-identical** to the pre-fix captures |
| all five earlier frozen typed-pipeline rows re-run | **5/5 `MATCH`** their pinned stdout digests |
| negative controls N1/N2/N3/N4 | exit 1 / 1 / 1 / 2 — unchanged |
| truncated packet (the runner's teeth control) | exit **2** |
| the new fail-closed controls | `typed-without-source` exit **2**, `typed-stale-source` exit **2** |
| `replay-frozen.py` on the new round-25 manifest | **`REPLAY OK: 6/6 rows reproduced`** |

### 8.3 The cascade is done, and the earlier manifests' refusal is the declared convention

The §4 cascade has landed: `tools/gates/frozen/round-25/gate-input/MANIFEST.tsv`
is a new generation (6 rows: both families × source/typed, plus two exit-2
fail-closed controls) whose `freeze.txt` binds the new gate digest and names the
predecessor `04ad4bb4…`.

The five earlier manifests that pinned the predecessor each still report **one**
`could-not-evaluate` row (`gate_digest_mismatch`; `10/11` and `2/3`
reproduced), which I initially read as an unfinished cascade. The new
`freeze.txt` declares this as intended:

> cascade: this re-pin moves the gate digest, so every earlier generation that
> pinned the predecessor now refuses its typed-pipeline row with
> gate_digest_mismatch … Restoring the predecessor blob
> (`git show f74fc94:tools/gates/typed-pipeline-gate.py`) returns those manifests
> to full reproduction; no historical manifest is edited here.

So the convention is: historical generations keep their pins and refuse the moved
gate row rather than being edited; the predecessor blob stays reachable in git
for restoration. That is consistent with the lane rule that pins are new rows and
filed artifacts are never edited.

**One caveat worth keeping:** `reports/round-25/run-validation.py` exercises this
surface only through `replay-frozen.py --selftest` (79/79 pass, no manifest
replay), and `replay-frozen.py` exits 0 on `COULD-NOT-EVALUATE`. The round's own
counting command therefore does not observe either the earlier manifests'
refused rows or the new generation's 6/6. If the round wants that held, the
runner needs a manifest-replay row; otherwise the check lives only in this
seat's evidence and in `freeze.txt`.

