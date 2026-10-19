- Seat: O02 | executor | claim O | date 2026-10-19 | baseline 9bccc9b

# O02 — isolated verification of O01's roster guard

**Mission** (`reports/round-38/targets.json` seat `O02`): *"Isolated verify of O01: guard
fires on the r7 row (named) and is green on a synced fixture; r7 default chain still exits 0
with packet 45f57132…"*.

**Dependency note.** O01 was one of the 10 seats the interrupted batch never ran; this seat
started with no draft to verify, reconstructed the guard from R02's guard-point
recommendation and R03-C1, and measured it. **`op/O01-guard-design.md` landed mid-run** (§6,
patch digest `c4141c71…`). This fragment therefore verifies **O01's actual draft** — its
patch applied verbatim to a fresh `git archive 9bccc9b` — and the reconstruction's
measurements serve as the second, independent reading.

**Verdict: O01's draft verifies.** The patch applies cleanly, the patched tool digest
reproduces O01's `e5812751…` exactly, the r7 default chain is exit 0 with packet
`45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19`, exactly one
`manifest-roster` row names `examples/culture-d4/components/13-register-law.yml`, the
`--selftest` is exit 0 with 45 controls (m15a named / m15b green), and the guard goes green
on the synced fixture. Every load-bearing constraint is reproduced independently, including
the vacuity of the obvious pair (§3) and the two rejected shapes (§4).

**One defect, cosmetic:** O01 §4 labels its in-sync digest `26a7882d…` "O04 variant C".
Measured, `26a7882d…` is the **tail insert** (O04 variant B); the `D4_COMPONENTS` splice
(variant A) gives `9e003970…`, matching O05's independent reading. Both are valid in-sync
readings and the tail insert is the better choice — only the label is wrong. §5.

All runs: `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`; fresh `git archive
9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26` copies only; no in-tree
`reports/round-*/run-validation.py` executed (F-C13-1); no `--freeze` against
`reports/round-34/handoff/declared-in-r7`; zero filed bytes written (`git status --short` →
`?? reports/round-38/` only).

---

## 1. The draft applies, and its digests reproduce exactly

O01 §6's fenced diff was extracted from the filed fragment, written to
`.scratch/o02/o01-guard.patch`, and applied to a fresh archive:

```
patch sha256 : c4141c716c5b634051ae8dd2cb6fbc13893b291f9ce6913a8a60e7bc4e0e4d9d
               O01 §6 claims c4141c716c5b634051ae8dd2cb6fbc13893b291f9ce6913a8a60e7bc4e0e4d9d  ✓
patch -p1 --dry-run : rc=0, "checking file tools/exercise-handoff-e2e.py"
patch -p1           : rc=0, "patching file tools/exercise-handoff-e2e.py"
patched tool sha256 : e581275129eb765399355374e8c5e29b50399fb98cbf860012b333b3eb02a553
               O01 §6 claims e581275129eb765399355374e8c5e29b50399fb98cbf860012b333b3eb02a553  ✓
```

The patch is self-contained (the `D4_ROSTER_MEMBER` constant, the
`v3_manifest_roster_gap` helper at `:3811`, the guard at `:3832`, and both fixtures at
`:4540`) and touches no other file. Unpatched tool sha256 remains
`bfe1c78e479f74784e3d2b53b053b43cd8333214c46bcc8b908b3b45ebff0aa9`.

## 2. The three mission thresholds, measured on O01's patch

| threshold (`claims.json:20-21`, `targets.json` O02) | required | measured | verdict |
|---|---|---|---|
| names the r7 member | `13-register-law.yml` named | `FAIL manifest-roster: examples/culture-d4/components/13-register-law.yml: in the packet component manifest (13 members, packet.d4.yml assembly.source_sha256) but not in the live read set (58 members) — the roster is incomplete; the bytes are still digest-checked` | **met** |
| r7 default chain unchanged | exit 0, packet `45f57132…` | `exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19` | **met** |
| selftest green with the two new controls | ≥2 controls, exit 0 | `selftest: OK — positive run (…) plus 45 controls`, incl. `m15a roster gap named, not raised …` and `m15b in-sync roster green …` | **met** |
| green on a synced fixture | manifest ⊆ read set | `OK manifest-roster: the packet component manifest (13 members) is carried by the live read set (59 members)`, exit 0 | **met** |
| r7 packet sha unchanged | `45f57132…` | `sha256sum reports/round-34/handoff/declared-in-r7/packet.md` → `45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19` | **met** |
| zero freeze bytes moved | r7 row byte-identical | `expected.json bbe15887…`, `packet.md 45f57132…`, `twin.json 0e229138…`, `claims-map.md d181de28…` | **met** |

The guard's own patch **does not move the packet**: the record-only check changes no bytes, so
the assembled packet is byte-identical to the filed r7 row. Confirmed by the `frozen-packet`
leg remaining `ok=True`.

## 3. O01 §1's pair choice is right, and the obvious pair is provably vacuous

O01 §1 claims the packet's `artifact_manifest` is read-set-derived and therefore cannot be the
guard's subject. Measured directly on the assembled packet:

```
artifact_manifest rows : 59
distinct paths         : 59
paths outside read set : ['§glossary payload (inline, this packet)']
13-register-law in artifact_manifest: False
```

`v3_manifest_rows` (`tools/exercise-handoff-e2e.py:2580-2594`) builds exactly one row per
`V3_READ_SET` member plus one inline-payload row, and `assert_manifest_equality`
(`:3645-3662`) hard-requires `checked == len(V3_READ_SET)`. So a guard comparing the artifact
manifest against the read set is **always in sync by construction** — confirmed, vacuous.
O01's choice of `assembly.d4["components"]` (mined from the source packet at `:2045-2056`)
is the only non-vacuous pair.

## 4. The two rejected shapes are rejected on measurement

Both re-derived independently in fresh copies (record-only variants, so only the rows differ):

| shape | r7 default chain | rows named | verdict |
|---|---|---|---|
| D4-scoped record-only (**O01's, accepted**) | exit **0**, packet `45f57132…` | **1** | accept |
| D4-scoped **raising** | exit **1** `E2E-READSET` | 1 | reject — violates the claim's own "r7 chain still exits 0" |
| **global** (D2+D3+D4) | exit 0 | **7** (6 D2 false reds + 1 D4) | reject — reddens the legitimate green path |
| rendered-text guard (R03-C1 trap) | exit 0 | **0** — reads 12 rows, names nothing | reject — vacuous |

The global shape's 6 D2 rows reproduce R02 Finding 2's count exactly; D2's partial read set is
documented at `:51-52` and `:2255-2262`. The rendered-text guard is the trap R03-C1 named: the
rendered `packet.md` carries 12 D4 rows, so a guard written against the frozen artifact passes
forever.

## 5. Finding — O01 §4's in-sync digest is labelled with the wrong variant

O01 §4 states: *"Reproducing O04 variant C in isolation … packet_sha256=26a7882d…"* and adds
that it differs from O04/O05's values *"because the renderer emits `V3_BASELINE_DEFAULT` into
the packet prose at `:3189`, so the successor digest is a function of the successor path
name"*. The path-dependence explanation is **correct** (it reproduces O05 D-2's mechanism),
but the value is attributed to the wrong variant. Measured, same successor path
`reports/round-38/handoff/declared-in-r8`, O01's guard applied, differing only in where the
13th member is inserted:

```
tail insert  (after "reports/round-19/validation.json")  -> packet 26a7882d313d63101de5f3fb9ff97457df2a670c1e814cc6ffaf340963c14ffa
D4_COMPONENTS splice (after 12-provenance.yml)           -> packet 9e00397054ca5bcc685fe77e0dab8dbd25ac048a0c241358f08aecf3170caf02
```

`26a7882d…` is O04 **variant B**; `9e003970…` is O04 **variant A/C** — and matches O05 §3's
independently measured value for the round-38 successor path. Both readings are honest; the
label is what is wrong. This matters only because O04 §2 recommends variant B on a
"narrower diff" argument that O05 D-1 falsified: the tail insert leaves `D4_COMPONENTS` at 12
and drops the D4 role label. O01's §4 is **not** landing that choice — its patch touches only
the guard, not the read set — so no action is owed beyond the label.

## 6. The landed dependency

`reports/round-38/op/O01-guard-design.md` (filed mid-run, 08:10-era):

- patch digest `c4141c716c5b634051ae8dd2cb6fbc13893b291f9ce6913a8a60e7bc4e0e4d9d` (verified exact)
- patched tool digest `e581275129eb765399355374e8c5e29b50399fb98cbf860012b333b3eb02a553` (verified exact)
- guard point `:3832`, helper `:3811`, record name `manifest-roster` (distinct from the
  existing `read-set-roster`, satisfying R02's "distinct detail" with no new convention)
- O01 §2's ordering claim — guard **before** the supersession abort, so the row is emitted even
  on the failing path — verified on all four filed rows:

```
r2 (declared-in-r2): exit 1  manifest-roster + read-set-roster (claims-map.md)
r5 (declared-in-r5): exit 1  manifest-roster + read-set-roster (claims-map.md)
r6 (declared-in-r6): exit 1  manifest-roster + read-set-roster (claims-map.md)
r7 (declared-in-r7): exit 0  manifest-roster only
```

The `manifest-roster` row is emitted in **every** case, including where the run aborts at
`E2E-READSET` — O01 §2's ordering argument holds, and the row survives to the CLI's record
print (`:4661`). This also supplies O08's owed reading (R02 Finding 5): the "only r7 names,
others green" threshold is false as written; the correct reading is *"the new D4 guard adds
exactly one row to every row that reaches it, and changes no existing row's verdict"*.

## 7. Residual risk O02 cannot clear (named, not claimed)

- **The in-sync control uses a module-global swap.** O01 §6's m15b sets
  `globals()["V3_READ_SET"] = expanded` and restores it in a `finally`. It passes, but the
  guard and the check it feeds read the module global, so the control exercises a state the
  shipped tool never enters by that route. A future landing that makes `V3_READ_SET` a
  parameter would make the control stronger. Not a defect — the `finally` restores the global
  and the selftest's later controls (m8, tamper-scan, missing-artifact) all still pass.
- **The guard is naming, not detection.** The 13th component is already digest-checked by
  `v3_verify_component_digests` (`:2208-2222`) — a mutated 13th component reds `E2E-DIGEST`
  with or without the read-set expansion (O05 §4, R02 Finding 6). Under the guard, a tampered
  13th component still cannot produce the per-input `input-digest` leg, because the file is
  not a read-set member; it surfaces through the assembled-vs-frozen packet compare
  (`:3951-3957`). The claim's "no vacuous-pass" threshold is met through the **named row**,
  never through new detection power. Claim O must not be reported as closing a detection gap.
- **`reports/round-38/run-validation.py` is absent** (`ls` → No such file or directory). Claim
  O's second counting command and its threshold command are `to-verify` regardless of what
  lands; every number here comes from the tool CLI.

## Owed

- **O03 (independent verification of O02):** re-run §1/§2/§4 against the same patch digest
  `c4141c71…`; this fragment's readings are one seat's. The falsifiers are §4's two rejected
  shapes and §3's 59-row artifact-manifest census.
- **O01 (label fix, cosmetic):** §4's `26a7882d…` should read "tail insert (O04 variant B)";
  the variant-C/splice value for the round-38 successor path is `9e003970…`. No code change.
- **O08 (regression sweep):** rewrite the threshold per §6's four-row table; the 5 pre-existing
  `E2E-READSET` reds are pre-existing, not guard regressions.
- **Integrator:** apply O01 §6 as one step; reconcile it with the §1 reconstruction in this
  seat's first pass (identical guard point and scope; O01's version is the one to land — it
  factors the gap into a helper and carries the two fixtures).
- **Not owed / out of scope:** no read-set edit, no re-freeze, no `CLAIMS_MAP` move, no
  freshness axis-move, no filed-byte rewrite.

## Citations

- `reports/round-38/op/O01-guard-design.md` §1-§6 (the draft under verification; patch digest
  `c4141c716c5b634051ae8dd2cb6fbc13893b291f9ce6913a8a60e7bc4e0e4d9d`)
- `reports/round-38/targets.json` (seat O02, `shared_rules`); `reports/round-38/claims.json:13-24,26`
- `reports/round-38/review/R02-o-review.md` Findings 1-6, guard-point recommendation;
  `reports/round-38/review/R03-cross-review.md` §3 (C1), §5 (C2); `reports/round-38/op/O04-fix-route.md`
  §1-§2; `reports/round-38/op/O05-verify-route.md` §1,§3,§4
- `tools/exercise-handoff-e2e.py:51-59,157-171,188,1937-1965,2045-2056,2208-2222,2255-2262,2580-2594,
  3189,3645-3662,3811,3821,3832-3838,3951-3957,4149-4169,4510-4514,4540,4661`
- `examples/culture-d4/packet.d4.yml:2875-2888`; `examples/culture-d4/typed-labels.d4.yml`
- `reports/round-34/handoff/declared-in-r7/{expected.json,packet.md,twin.json,claims-map.md}`
- Command evidence (fresh `git archive 9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26` copies, `TMPDIR=$PWD/.scratch`):
  - `.scratch/o02/o01-guard.patch`: extracted from O01 §6 → `sha256 c4141c71…`; `patch -p1 --dry-run` → rc 0;
    `patch -p1` → rc 0; patched tool → `e581275129eb765399355374e8c5e29b50399fb98cbf860012b333b3eb02a553`
  - `.scratch/o02/o01v` (O01 patch): `--profile v3` → exit **0**, one `FAIL manifest-roster` naming
    `examples/culture-d4/components/13-register-law.yml`, packet `45f57132…`; `--selftest` → exit **0**,
    "plus 45 controls" incl. `m15a roster gap named, not raised` and `m15b in-sync roster green`
  - `.scratch/o02/o01v`: `--baseline` on r2/r5/r6 → exit **1** with `manifest-roster` + `read-set-roster`
    (`reports/round-20/handoff/claims-map.md`); r7 → exit **0** with `manifest-roster` only
  - `.scratch/o02/o01clean` (fresh archive + O01 patch + splice + round-38 successor): `--freeze
    reports/round-38/handoff/declared-in-r8` → exit 0, packet `9e00397054ca5bcc685fe77e0dab8dbd25ac048a0c241358f08aecf3170caf02`;
    `--profile v3` → exit 0, `OK manifest-roster: the packet component manifest (13 members) is carried by the
    live read set (59 members)`
  - `.scratch/o02/vc-tail` (O01 patch + tail insert + round-38 successor): `--freeze` → packet
    `26a7882d313d63101de5f3fb9ff97457df2a670c1e814cc6ffaf340963c14ffa` (§5)
  - `.scratch/o02/guard-global` / `guard-raising` / `guard-rendered` (record-only reconstructions):
    7 rows / exit 1 `E2E-READSET` / 0 rows named with "RENDERED packet manifest (12 D4 component rows)"
  - `.scratch/o02/base` artifact-manifest census: 59 rows, 59 distinct paths, 1 outside the read set
    (`§glossary payload (inline, this packet)`), `13-register-law` absent; `assert_manifest_equality`
    requires `checked == 58`
  - `sha256sum` (unmoved): `tools/exercise-handoff-e2e.py bfe1c78e479f74784e3d2b53b053b43cd8333214c46bcc8b908b3b45ebff0aa9`;
    r7 `expected.json bbe15887…`, `packet.md 45f57132…`, `twin.json 0e229138…`, `claims-map.md d181de28…`;
    `examples/culture-d4/components/13-register-law.yml c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7`
  - `git rev-parse HEAD` → `9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26`; `git status --short` → `?? reports/round-38/` only
