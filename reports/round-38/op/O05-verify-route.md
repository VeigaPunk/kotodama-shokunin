- Seat: O05 | verifier | claim O | date 2026-10-19 | baseline 9bccc9b

# O05 — independent verification of O04's fix route

**Mission.** `reports/round-38/targets.json` seat O05: "Verify O04's fix-route against the
renderer's freeze mechanics." O04's draft (`reports/round-38/op/O04-fix-route.md`) was absent
when this seat started and landed at 08:08 during the run; this fragment now verifies the
draft as filed. All measurements are in isolated `git archive 9bccc9b` copies
(`TMPDIR=$PWD/.scratch`); no in-tree `run-validation.py` ran; no filed byte was written.

**Verdict.** O04's central result is **confirmed independently**: a read-set edit alone is a
red default chain, and the fix route is the paired move (read-set add **plus** the two default
constants re-pointed to a successor directory). Every digest O04 pins in §2/§3 that I re-ran
reproduced exactly. Two defects in the draft are named below: **(D-1)** its recommendation of
variant B rests on a false "equal functional coverage" claim — B leaves the named
`D4_COMPONENTS` tuple at 12 and silently drops the D4 role label; **(D-2)** variant C's packet
digest is a function of the successor directory's literal name, so O04's pinned `b102aa70…`
is valid only for the exact path `reports/round-39/handoff/declared-in-r8`. Plus one
non-vacuity control O04 did not run (§4) and one cascade surface it did not reach (§5).

## 1. Independent reproduction of O04's measured table

I re-built each variant from scratch in separate archives and re-froze. O04's §2 digests
reproduce exactly:

| variant | O04's packet sha256 | my packet sha256 | twin |
|---|---|---|---|
| A — member spliced into `D4_COMPONENTS` | `7f0e47909a77ad7f…` | **`7f0e47909a77ad7f…`** ✓ | `9ad1f6db80731529…` ✓ |
| B — member appended at the tail | `7ca92109e390d8e7…` | **`7ca92109e390d8e7…`** ✓ | `90b7f5f2f868db15…` ✓ |
| C — A plus the two constants → `reports/round-39/handoff/declared-in-r8` | `b102aa708a23d3ba…` | **`b102aa708a23d3ba…`** ✓ | `9ad1f6db80731529…` ✓ |

Reproduced controls:

- **Read-set-only edit is red.** With the member added and the constants left at r7:
  `handoff-v3: exit=1 … E2E-DIGEST: the assembled packet does not match the frozen packet digest`
  (the byte-compare at `tools/exercise-handoff-e2e.py:3951-3957`).
- **C's default chain is green.** `--profile v3 --quiet` → `exit=0 … packet_sha256=b102aa708a23d3ba…`;
  a second `--freeze` into the same successor dir → `no tracked value changed since the previous freeze`.
- **`CLAIMS_MAP` must not move in the same step (O04 §2, last bullet).** Splice + `CLAIMS_MAP`
  re-pointed to the r8 dir → `E2E-READSET: 1 read-set member(s) named by the frozen baseline are
  not in the live read set: reports/round-34/handoff/declared-in-r7/claims-map.md — the baseline
  row is superseded` — the *existing* roster guard, not `E2E-DIGEST`. Confirmed.
- **Twin sensitivity (O04 §2, bullet 3).** Twin A == Twin C (`9ad1f6db…`) while their packet
  shas differ; Twin B differs (`90b7f5f2…`). Comparing parsed twin objects, the **only** key that
  ever differs is `artifact_manifest`. Confirmed.
- **Ordering (O04 §2, bullet 2).** Variant A: r7's `A-46` path equals A's `A-47` path — the 13
  rows `A-46…A-58` shift +1. Variant B: r7's `A-46` path equals B's `A-46` path — zero
  renumbering, new tail id `A-59`. Confirmed.
- **§1's surface claim.** The packet's `artifact_manifest` holds 58 rows (`A-01`…`A-58`) and
  `assert_manifest_equality` (`:3646-3662`) requires `checked == len(V3_READ_SET)`; the mismatch
  is the *component* manifest (13, `examples/culture-d4/packet.d4.yml:2888`) vs the read set.
  Confirmed.
- **§3's `expected.json` diff.** r7 → A: `baseline_digest 1fce3820148430dc… → e4e6d370f1307ed4…`,
  `packet_sha256 → 7f0e4790…`, `twin_sha256 → 9ad1f6db…`, `inputs 58 → 59`, and exactly two
  `field_digests` changed (`artifact_manifest`, `validation`). r7 → B: `baseline_digest → 116cf7da63a259ab…`.
  Every other key unchanged. Confirmed.
- **§4 edit 5.** `:2783` already reads `thirteen authored components`; `grep -n "authored
  components"` returns that one hit. No edit owed. Confirmed.
- **§6 preservation.** `reports/round-34/handoff/declared-in-r7/*` measure identically before and
  after every variant; live tree `git status --short` → `?? reports/round-38/` only.

## 2. D-1 — variant B is not "equal functional coverage"; it leaves the named tuple at 12

O04 §2 calls variant B "A *narrower* diff at equal functional coverage" and §4 edit 1 offers B
as the recommended insert ("appended after `reports/round-19/validation.json`"). The byte diff
is indeed narrower (packet 10 diff lines vs A's 37; twin 6 vs 54), but the coverage claim is
false in two measurable ways:

1. **`D4_COMPONENTS` still holds 12 paths under B.** The tuple O04 §1 identifies as the
   instrument-level surface is untouched; only `V3_READ_SET` grows.

   ```text
   r38-o05-vB :  D4_COMPONENTS len: 12 | V3_READ_SET len: 59 | 13th in D4_COMPONENTS: False
   r38-o05-exp:  D4_COMPONENTS len: 13 | V3_READ_SET len: 59 | 13th in D4_COMPONENTS: True
   ```

   So the **manifest(13)-vs-`D4_COMPONENTS`(12) disagreement that claim O names persists under
   variant B.** A guard keyed on `D4_COMPONENTS` (O01's likely target) would still see 12 vs 13
   after B lands. Only variant A/C actually closes the named tuple.

2. **B silently drops the D4 role label for the 13th member.** The row-role loop is
   `for rel in D4_COMPONENTS: by_rel[rel] = "d4 authored component input (digest pinned by
   packet.d4.yml assembly)"` (`:2577-2578`), and the fallback is
   `f"read-set input, {size:,} bytes (digest-pinned)"` (`:2588`). Measured packet rows:

   ```text
   variant A/C: | A-46 | …/13-register-law.yml | d4 authored component input (digest pinned by packet.d4.yml assembly) | c0d77181ac56… |
   variant B  : | A-59 | …/13-register-law.yml | read-set input, 8,870 bytes (digest-pinned)                                        | c0d77181ac56… |
   ```

   B's narrower diff is bought by not registering the file as a D4 component — i.e. by leaving
   the defect's own surface unregistered. That is a **functional** difference, not a
   byte-count-neutral one. The recommendation should either prefer A/C or state the trade
   explicitly rather than as "equal coverage".

## 3. D-2 — variant C's packet digest is path-dependent (pinning hazard)

O04 §5's `R39-O-default-pointer` control pins `packet_sha256: b102aa708a23d3ba…` for variant C,
which is correct **only** for the literal successor path `reports/round-39/handoff/declared-in-r8`.
The renderer emits `V3_BASELINE_DEFAULT` into the packet prose (`:3189`, the §open_questions
row), so the successor packet digest is a function of the successor directory's name. With an
otherwise identical read set:

```text
C with successor = reports/round-39/handoff/declared-in-r8  -> packet  b102aa708a23d3ba…  (O04's value)
C with successor = reports/round-38/handoff/declared-in-r8  -> packet  9e00397054ca5bcc…  (this seat)
```

`b102aa70…` and `9e003970…` differ **only** by that one prose line. So O04's pinned control
value is correct as written but fragile: if the integrator lands the successor under any other
directory name (including the round-38 dir a same-round landing would use), the pinned digest
will not match and the repin row's own control reads red. The row should pin the control value
against the path it actually names, or record the path→digest coupling as a named limit.

## 4. Non-vacuity control O04 did not run — the expansion adds no detection power

Claim O's threshold requires "no vacuous-pass". O04 measured detection only indirectly (via
the frozen-baseline digest). I ran the direct control: mutate the 13th component and run the
default chain, with and without the read-set expansion.

```text
expanded read set (13 D4 components), 13-register-law.yml mutated:
  E2E-DIGEST: D4 component examples/culture-d4/components/13-register-law.yml: the assembler recorded c0d77181ac56… but the bytes measure bfd150874c2a…
UNPATCHED copy (12-component read set), same mutation:
  E2E-DIGEST: D4 component examples/culture-d4/components/13-register-law.yml: the assembler recorded c0d77181ac56… but the bytes measure bfd150874c2a…
```

**Both fire identically.** The transitive component-digest check (`v3_verify_component_digests`,
`:2208-2222`, traversing `d4["components"]` mined from the packet manifest at `:2045-2056`)
already detects the mutation with no read-set change. The expansion is therefore a
**roster/documentation correction, not a detection gain** — it makes the read set *state* what
the manifest already *enforces*. This is consistent with O04's own framing (§1 "component
manifest vs read set") but is worth stating explicitly, because it means the O-claim must not
be reported as closing a detection gap. A01 reached the same reading on the same control
(`reports/round-37/adj/A01-freeze-adjudication.md:26-31`).

## 5. Cascade surface O04 did not reach — the filed r34/r35 validators assert the old literals

O04 §5's repin row implies the re-point is the whole cascade. It is not: two **filed** round
runners assert the r7 default literals by exact string and will fail once the re-point lands.

- `reports/round-35/run-validation.py:225-226` — its O7 leg appends a failure if either
  `V3_BASELINE_DEFAULT = "reports/round-34/handoff/declared-in-r7/expected.json"` or
  `V3_FROZEN_DIR_DEFAULT = "reports/round-34/handoff/declared-in-r7"` is absent from the
  renderer. After the re-point both are absent (measured: `False` for both).
- `reports/round-34/run-validation.py:177-178` — its D5 leg has the same shape, parameterised
  on `R7 = f"{ROUND}/handoff/declared-in-r7"` (`:23`), so it too breaks.

The outliers are r34/r35; rounds 27 and 28 took the tolerant stance and read the constant live
(`reports/round-27/run-validation.py:1388-1389`, `reports/round-28/run-validation.py:1348-1349`).
Since filed bytes cannot be edited, the integrator must either land the successor in a round
that does not re-run r34/r35, or record those D5/O7 legs as superseded at landing. O04's §5 row
should carry this as a named finding.

## 6. What this seat ran, and what it did not

- **Ran**: five isolated `git archive 9bccc9b` copies (variant A, variant B, variant C at the
  round-39 path, splice+`CLAIMS_MAP`-moved, and two mutation controls); `--profile v3 --quiet`,
  `--freeze`, `--selftest` (exit 0, "positive run … plus 43 controls", including the read-set
  legs `m13a`/`m13b`/`m14a`/`m14b` at `:4467,4509`); `diff`, `sha256sum`, and parsed-JSON-object
  comparison.
- **Did not run**: any in-tree `reports/round-*/run-validation.py`; no re-freeze of
  `declared-in-r7`; no edit to any filed byte, tool, or example. The renderer patches exist only
  in `.scratch/r38-o05-*` as drafts for the integrator.

## Owed

- **O04 §4/§5 reconciliation (integrator):** D-1 (prefer A/C, or state B's coverage trade
  explicitly) and D-2 (pin the C control digest against the exact successor path) should be
  folded into the filed O04 draft, or into the landing record, before the route is executed.
- **O01 guard design (cross-claim):** D-1's measurement shows a guard keyed on `D4_COMPONENTS`
  stays red under variant B; a guard keyed on the packet's component manifest vs `V3_READ_SET`
  goes green under A/B/C. O01/R02/R03 should pick the pair deliberately, not by accident.
- **Landing seat:** decide the r34 `D5` / r35 `O7` literal assertions (§5) before re-running
  those filed runners; do not edit them.

## Citations

- `reports/round-38/op/O04-fix-route.md` §1-§6 (the draft under verification)
- `tools/exercise-handoff-e2e.py:51-59,157-170,188,1937-1938,1939-1962,2045-2056,2208-2222,2577-2578,2588,3189,3646-3662,3951-3957,4467,4509`
- `examples/culture-d4/packet.d4.yml:2888`; `examples/culture-d4/ASSEMBLY.md:12-24`
- `reports/round-34/handoff/declared-in-r7/{packet.md,twin.json,expected.json,freeze.txt,claims-map.md}`
- `reports/round-34/run-validation.py:23,177-178`; `reports/round-35/run-validation.py:22-26,225-226`; `reports/round-27/run-validation.py:1388-1389`; `reports/round-28/run-validation.py:1348-1349`
- `reports/round-37/adj/A01-freeze-adjudication.md:5,26-35`
- `reports/round-38/claims.json` (claim O); `reports/round-38/targets.json` (seat O05)
- Command evidence (all isolated archives of `9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26`):
  A packet `7f0e47909a77ad7f…`; B packet `7ca92109e390d8e7…`; C(round-39) packet `b102aa708a23d3ba…`;
  C(round-38) packet `9e00397054ca5bcc…`; r7 replay post-fix `E2E-DIGEST`; splice+CLAIMS_MAP-move
  `E2E-READSET` naming `reports/round-34/handoff/declared-in-r7/claims-map.md`; dual mutation
  controls both `E2E-DIGEST`; `--selftest` exit 0 with 43 controls; `git status --short` → `?? reports/round-38/` only.
