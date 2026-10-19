- Seat: R02 | reviewer | claim O | date 2026-10-19 | baseline 9bccc9b

# R02 — adversarial review of the O block (guard correctness: no new false reds)

**Verdict: the claim's target is real but its guard is only safe under two
narrow constraints, and one of the O block's own thresholds (O08) is already
falsified on the live tree.** A manifest-vs-read-set guard is *not* a
from-scratch addition — a one-directional `read-set-roster` check already
exists at `tools/exercise-handoff-e2e.py:3823-3838` — and the obvious
implementation (global, or raising) breaks the legitimate green path with **7
false reds**. A D4-scoped, record-only guard names exactly the r7 row, leaves
the r7 chain at exit 0 and packet `45f57132…` unchanged, and passes the full
`--selftest`. Separately, **5 of the 6 filed v3 baselines already exit 1
`E2E-READSET` on the live tree**, so "only the r7 row names; others stay green"
(`reports/round-38/targets.json` O08) is false as written.

All runs were in isolated `git archive HEAD` copies under `.scratch/`; no
in-tree file was executed or edited (`git status --porcelain` → only
`?? reports/round-38/`).

## Finding 1 — the guard direction already exists, and it is load-bearing

`tools/exercise-handoff-e2e.py:3823-3838` already computes
`dropped = baseline["inputs"] not in assembly.digests`, records a
`read-set-roster` row per member, and raises `E2E-READSET`. Its direction is
*baseline-named member ∉ live read set* (the superseded-row class), which is
**green on r7**: r7's 58 `inputs` are all live read-set members, so the
existing check never fires for the r7 defect. The r7 class is the *opposite*
direction — a packet-manifest member absent from the read set — which the
existing check does not test. So claim O's "land a renderer guard" is a new
*direction* at an existing site, not a new site; the new check must not
displace the existing one, which is the leg that caught the r35 re-point
(`git log -S'reports/round-20/handoff/claims-map.md' -- tools/exercise-handoff-e2e.py`
→ `ce103bf round-35`).

## Finding 2 — a global manifest-vs-read-set guard is a false-red machine (7 rows)

The D2 read set is **intentionally partial**, and it is documented twice:
`tools/exercise-handoff-e2e.py:51-52` ("the **four** D2 component inputs the D2
projector's selftest fixture copies") and `:2255-2262`
(`D2_COMPONENT_INPUTS`, 4 paths). Measured per tree against the live read set:

| tree | manifest members | outside `V3_READ_SET` | read-set members outside manifest |
|---|---|---|---|
| D2 | 9 | **6** | 1 (`12-rank-rules.yml`) |
| D3 | 4 | 0 | 0 |
| D4 | 13 | **1** (`13-register-law.yml`) | 0 |

D2's packet manifest is `examples/culture-d2/packet.d2.yml:3323-3332` (9
members); the read set carries only 05/09/11
(`tools/exercise-handoff-e2e.py:1939-1963`), and `12-rank-rules.yml` is in the
read set (`:2255-2262`) but **not** in the D2 manifest.

Isolated control (patched `.scratch/r02/` only, global forward guard that
raises): the default chain goes **exit 1 with 7 named rows** — the 6 D2 members
plus `13-register-law.yml`:

```
FAIL manifest-roster: examples/culture-d2/components/02-phonology.yml: in the packet component manifest but not in the live read set
... (03-morphosyntax, 06-pantheon, 07-myths-motifs, 08-symbols, 13-naming) ...
FAIL manifest-roster: examples/culture-d4/components/13-register-law.yml: in the packet component manifest but not in the live read set
handoff-v3: exit=1 ... packet_sha256=(not assembled)
```

A global guard therefore **harms** operability: it reddens the legitimate green
path. Any D-block or O-block reviewer that lands the guard globally, or scoped
to "all trees", violates claim O's own "no new false reds" and the round's
no-harm admission rule.

## Finding 3 — the guard must be D4-scoped **and** record-only (no raise)

Two isolated variants, both patched only in `.scratch/`:

- **D4-scoped, record-only** (`record(...,False)` with no `raise`): names
  exactly `examples/culture-d4/components/13-register-law.yml`, and the r7 chain
  stays **exit 0**, `packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19`,
  `fields=16/16 glossary=20/20 findings=0 links=105/105`. The full
  `--profile v3 --selftest` also exits 0.
- **D4-scoped, raising** (`raise Failed("E2E-READSET", ...)`): the r7 chain goes
  **exit 1**, which fails the claim's threshold "the r7 default chain still
  exits 0 unchanged". It also **breaks the selftest's own positive run**: the
  fixture freeze pins exactly `V3_READ_SET` (`tools/exercise-handoff-e2e.py:4165-4169`),
  so it reproduces the asymmetry, and the positive assertion at `:4193-4194`
  fails with the named row.

So the claim's wording "refuses **or** names" is only satisfiable by **naming**.
"Refuses" contradicts the claim's own exit-0 threshold and the selftest.

## Finding 4 — the fix route is a re-render/re-freeze, not a documentation tweak

The assembled packet **embeds the read-set count**: `tools/exercise-handoff-e2e.py:2825`
("`{len(V3_READ_SET)} read-set files plus one inline-payload row`"). Adding the
member to the read set therefore changes the packet bytes: measured packet sha
`45f57132…` → `7ca92109…` under a patched `V3_READ_SET` of 59. This is
consistent with `reports/round-37/adj/A01-freeze-adjudication.md:24-35` and
`reports/round-37/op/O09-routing.md:10` ("add direct membership in a new
baseline revision, never re-freeze the filed r7 pair"), and it means the
"documentation-only" route (leave the read set alone, document the transitive
contract) is the only one that keeps "zero freeze bytes moved". O04's fix-route
document should state that the guard's *naming* is orthogonal to the *fix*: the
guard names the row forever until a successor baseline is rendered.

## Finding 5 — O08's premise is falsified on the live tree

O08's mission (`reports/round-38/targets.json`) is "every filed frozen row
(r2..r7) replayed in isolation under the guard — only the r7 row names; others
stay green". Replaying the filed v3 baselines against the live tree (no guard,
`--profile v3 --baseline <row>`):

| filed baseline | observed |
|---|---|
| `reports/round-20/handoff/expected.json` | exit 1 `E2E-READSET` naming `reports/round-20/handoff/claims-map.md` |
| `reports/round-22/handoff/declared-in-r2/expected.json` | exit 1, same name |
| `reports/round-22/handoff/declared-in/expected.json` | exit 1, same name |
| `reports/round-26/handoff/declared-in-r5/expected.json` | exit 1, same name |
| `reports/round-30/handoff/declared-in-r6/expected.json` | exit 1, same name |
| `reports/round-34/handoff/declared-in-r7/expected.json` | exit 0, packet `45f57132…` |

Five rows are **already red** for the *superseded-row* class (`CLAIMS_MAP` was
re-pointed to `reports/round-34/.../claims-map.md` at r35, `tools/exercise-handoff-e2e.py:188`;
the r20-era baselines pin the r20 path). Only r7 is green. "Others stay green"
is false; O08 must instead assert "the new D4 guard adds no row beyond
`13-register-law.yml` and does not change any existing row's verdict", and must
record the 5 pre-existing reds as pre-existing, not as guard regressions.

## Finding 6 — the guard adds naming, not new detection (trade to report)

`13-register-law.yml` **is** already measured: `v3_verify_component_digests`
(`tools/exercise-handoff-e2e.py:2208-2222`) iterates the packet manifest and
raises `E2E-DIGEST` on changed bytes. `reports/round-37/adj/A01-freeze-adjudication.md:29`
and `A06-verify.md:21` independently demonstrated that mutation control. So the
D4 guard contributes **naming/completeness of the roster**, not new detection.
The X02 honesty critic should weigh whether this is a real operability move or a
near-vacuous one; the claim's "no vacuous-pass" threshold is met only because
the guard's output is a *named* row that a human can act on, not because it
catches a class nothing else catches.

## Guard-point recommendation (for O01/O02)

Insert inside `v3_exercise` immediately after `assembly = V3Assembly(root)`
(`tools/exercise-handoff-e2e.py:3821`), before the existing `dropped` block at
`:3823`, so
the existing check keeps priority. `assembly.digests` is keyed by `V3_READ_SET`
only (`:3485-3488`), so use `sorted(set(assembly.d4["components"]) - set(V3_READ_SET))`
— identical to `- assembly.digests.keys()`. The record detail must
**distinguish the two classes** ("manifest member not in the direct read set"
vs the existing "superseded baseline row") or the two become
indistinguishable `read-set-roster` rows in the same run.

## Owed

- O01/O02 executor: none blocked. This review is adversarial input to the O
  design; the constraints above (D4-scoped, record-only, distinct detail) are
  the falsifiable gates an O02/O03 verifier should re-run.
- O08 executor: rewrite the threshold from "only r7 names, others green" to the
  Finding-5 form; the 5 pre-existing reds are outside the guard's scope.
- O04 executor: state that naming ≠ fix; only a successor-baseline re-render
  clears the named row, and it moves the packet sha (`45f57132…` → `7ca92109…`).

## Citations

- `tools/exercise-handoff-e2e.py:51-52,188,1939-1963,2208-2222,2255-2262,2825,3485-3488,3811-3838,4165-4169,4193-4194`
- `examples/culture-d2/packet.d2.yml:3323-3332`; `examples/culture-d4/packet.d4.yml:2875-2888`
- `reports/round-34/handoff/declared-in-r7/expected.json` (58 inputs, no `13-register-law.yml`)
- `reports/round-37/adj/A01-freeze-adjudication.md:24-35`; `A06-verify.md:21`; `reports/round-37/op/O09-routing.md:10`
- `reports/round-38/claims.json` (claim O); `reports/round-38/targets.json` (seats O01-O08)
- Command evidence (isolated `git archive HEAD` copies only; no in-tree runner executed):
  - live per-tree manifest-vs-read-set probe → D2 6 outside / 1 reverse, D3 0/0, D4 1/0
  - `.scratch/r02` global raising guard, `--profile v3` → exit 1, 7 named rows
  - `.scratch/r02b` D4-scoped record-only guard, `--profile v3` → exit 0, packet `45f57132…`; `--selftest` → exit 0
  - `.scratch/r02c` D4-scoped raising guard, `--profile v3` → exit 1; `--selftest` → AssertionError on the positive run
  - filed-baseline replay (`--baseline <row>`) → 5× exit 1 `E2E-READSET` (`claims-map.md`), r7 exit 0
  - patched-`V3_READ_SET` packet rebuild → sha `45f57132…` → `7ca92109…`
  - `git status --porcelain` → only `?? reports/round-38/`
