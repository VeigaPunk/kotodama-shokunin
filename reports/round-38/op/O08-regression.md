- Seat: O08 | verifier | claim O | date 2026-10-19 | baseline 9bccc9b

# O08 — guard regression sweep: every filed v3 row replayed under O01's drafted guard

**Subject of the sweep.** The guard **design** landed as a fragment
(`reports/round-38/op/O01-guard-design.md`) but the tool patch is still a **draft**:
the live tree's `tools/exercise-handoff-e2e.py` sha256 is `bfe1c78e479f74784e3d2b53b053b43cd8333214c46bcc8b908b3b45ebff0aa9`
and contains **zero** `manifest-roster` occurrences. So "under the guard" below always
means *O01's §6 patch applied verbatim in an isolated `git archive` copy* — never an
in-tree edit. Zero tool bytes moved.

**Verdict.** The sweep ran and the guard is **regression-clean**: under O01's drafted
guard, **exactly one** `manifest-roster` row is added to every filed v3 row
(naming `examples/culture-d4/components/13-register-law.yml`), the record-count
delta is **+1** everywhere, **no existing row's verdict changes**, and the r7
default chain stays **exit 0** with packet `45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19`.
O01's patch applied verbatim reproduces its declared patched-tool digest
`ae22013b5ddd77aa…` exactly, and its selftest goes 43 → **45** controls.

The mission's literal threshold — *"only the r7 row names; others stay green"*
(`reports/round-38/targets.json` seat O08) — is **false**, and so is the
replacement form the sibling seats proposed. Two distinct measurements are
conflated in the O block's discussion and must be separated:

- **(a) the drafted guard's subject is the live tree.** `assembly.d4["components"]`
  is mined from the live `examples/culture-d4/packet.d4.yml`, not from the replayed
  row. Measured: the guard names the D4 member on **all 10** filed v3 rows —
  including r20, r2, r5. "r2/r5 stay green" (`X02` §4a, `O01` §2) is **not** what
  the drafted guard does.
- **(b) the per-row baseline asymmetry** is the row's own `packet.md` (13) vs its
  own `inputs` (12). Measured: **4** rows carry the 13-vs-12 asymmetry — r27, r28,
  r6, r7 — not the 2 that `X02` §4a reports.

X02 §4a sampled only the four `declared-in*` directories and generalised from them;
`O01` §2 inherited that form. Reading (b) is the one that measures the defect class;
reading (a) is the one the landed instrument emits. The corrected O08 expectation is
in §6.

## 1. Census — the filed v3 row set is 10, not 6

Rows carrying `profile: kotodama-handoff-e2e/3` (the v3 exercise baseline shape), by
`python3 -c` over every `reports/**/expected.json`:

| # | row | pre-existing verdict (unpatched) |
|---|---|---|
| 1 | `reports/round-20/handoff/expected.json` | exit 1 `E2E-READSET` |
| 2 | `reports/round-22/handoff/declared-in/expected.json` | exit 1 `E2E-READSET` |
| 3 | `reports/round-22/handoff/declared-in-r2/expected.json` | exit 1 `E2E-READSET` |
| 4 | `reports/round-26/handoff/declared-in-r5/expected.json` | exit 1 `E2E-READSET` |
| 5 | `reports/round-26/register/v3-baseline-r26/expected.json` | exit 1 `E2E-READSET` |
| 6 | `reports/round-26/remainders/v3-baseline-r26/expected.json` | exit 1 `E2E-READSET` |
| 7 | `reports/round-27/pinsweep/v3-baseline-r27/expected.json` | exit 1 `E2E-READSET` |
| 8 | `reports/round-28/pinsweep/v3-baseline-r28/expected.json` | exit 1 `E2E-READSET` |
| 9 | `reports/round-30/handoff/declared-in-r6/expected.json` | exit 1 `E2E-READSET` |
| 10 | `reports/round-34/handoff/declared-in-r7/expected.json` | **exit 0**, packet `45f57132…` |

`R02` Finding 5 measured six of these and missed **r26/register**, **r26/remainders**,
**r27/pinsweep**, **r28/pinsweep** — four more rows in the same class. All nine red
rows name the identical member: `reports/round-20/handoff/claims-map.md`, the r35
`CLAIMS_MAP` re-point (`tools/exercise-handoff-e2e.py:188`). This is a **pre-existing
supersession red, not a guard regression**.

Two rows that look like the same family are **not** v3 exercise baselines and must
not be swept as rows: `reports/round-23/wording/declared-in-r3/expected.json` and
`reports/round-25/v3-supersession/declared-in-r4/expected.json` both exit 2
`E2E-BASELINE: frozen baseline is missing [...17 keys...] — it was not written by
this exercise`. They are prose/declaration records (r3 is a wording supersession, r4
a v3 supersession). `O04` §5 and `reports/round-34/handoff/repin.json` R34-D-history
treat them as "rows" in a loose sense; for replay purposes they are not.

## 2. The drafted guard, applied verbatim

O01's §6 diff block was extracted from the filed fragment to
`.scratch/o08/o01-guard.patch` and applied with `patch -p1` in a fresh
`git archive 9bccc9b` copy:

```text
patch -p1 --dry-run < ../o01-guard.patch   → checking file tools/exercise-handoff-e2e.py  (clean)
patch -p1        < ../o01-guard.patch      → patching file tools/exercise-handoff-e2e.py
sha256sum tools/exercise-handoff-e2e.py    → ae22013b5ddd77aa1b598cef1f5a57f0fb76bfc6eb8541d56e180fe70abcf6c2
```

`ae22013b…` is exactly the digest O01 §6 declares. Unpatched tool sha256
`bfe1c78e479f74784e3d2b53b053b43cd8333214c46bcc8b908b3b45ebff0aa9`.

Selftest under the drafted guard, reproduced:

```text
python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest   → exit 0
selftest: OK — positive run (exit 0, fields=16/16, glossary-entries=20, findings=0,
links=105/105, claims=27, statuses=16/7/4, v2_subset=equal, alias_leg=landed) plus 45 controls:
  - m15a roster gap named, not raised: exit 0 None with a manifest-roster row naming
    examples/culture-d4/components/13-register-law.yml (the r7 class; the read set still carries every frozen member)
  - m15b in-sync roster green: the read set carries every manifest member, exit 0 with no manifest-roster row
```

43 → 45 controls, both new controls green — O01 §6.1 confirmed independently.

## 3. The sweep — 10 rows, unpatched vs drafted guard

Both trees are isolated `git archive 9bccc9b` copies; `--profile v3 --json --baseline <row>`.

| row | unpatched | drafted guard | records | manifest-roster rows | other verdicts |
|---|---|---|---|---|---|
| r20 `handoff` | exit 1 `E2E-READSET` | exit 1 `E2E-READSET` | 2 → 3 | **1** | unchanged |
| r22 `declared-in` | exit 1 `E2E-READSET` | exit 1 `E2E-READSET` | 2 → 3 | **1** | unchanged |
| r22 `declared-in-r2` | exit 1 `E2E-READSET` | exit 1 `E2E-READSET` | 2 → 3 | **1** | unchanged |
| r26 `declared-in-r5` | exit 1 `E2E-READSET` | exit 1 `E2E-READSET` | 2 → 3 | **1** | unchanged |
| r26 `register` | exit 1 `E2E-READSET` | exit 1 `E2E-READSET` | 2 → 3 | **1** | unchanged |
| r26 `remainders` | exit 1 `E2E-READSET` | exit 1 `E2E-READSET` | 2 → 3 | **1** | unchanged |
| r27 `pinsweep` | exit 1 `E2E-READSET` | exit 1 `E2E-READSET` | 2 → 3 | **1** | unchanged |
| r28 `pinsweep` | exit 1 `E2E-READSET` | exit 1 `E2E-READSET` | 2 → 3 | **1** | unchanged |
| r30 `declared-in-r6` | exit 1 `E2E-READSET` | exit 1 `E2E-READSET` | 2 → 3 | **1** | unchanged |
| r34 `declared-in-r7` | **exit 0** | **exit 0** | 15 → 16 | **1** | unchanged |

The guard row is identical in every run:

```text
FAIL manifest-roster: examples/culture-d4/components/13-register-law.yml: in the packet component
manifest (13 members, packet.d4.yml assembly.source_sha256) but not in the live read set (58 members)
— the roster is incomplete; the bytes are still digest-checked
```

`records` delta is **+1** on all ten rows; the non-guard record list (check name and
`ok` flag, in order) is **identical** to the unpatched run on every row — verified by
tuple comparison, not by eyeball. So the guard adds a row and changes nothing else.

## 4. Ordering — the guard is reachable despite the supersession abort

`X02` §4b constraint 1 and `O01` §2 both flag that an isolation run against a red row
aborts at `E2E-READSET` before any *later-added* check. Placing the guard **before**
the `dropped = …` block resolves it. Confirmed on r6, non-quiet, with **both** record
classes emitted before the raise:

```text
FAIL manifest-roster: examples/culture-d4/components/13-register-law.yml: in the packet component
manifest (13 members, …) but not in the live read set (58 members) — the roster is incomplete; …
FAIL read-set-roster: reports/round-20/handoff/claims-map.md: frozen 4b1b9a35a18f… not in the live read set (58 members)
handoff-v3: exit=1 fields=? … packet_sha256=(not assembled)
```

So a red row yields **two** named rows of **two distinct classes** — the new
`manifest-roster` and the pre-existing `read-set-roster` — and the sweep produces a
manifest verdict on every row, including the nine red ones. This is the concrete
answer to constraint 1: no bypass of the abort is needed.

## 5. Controls — non-vacuity, in-sync, rejected shapes, preservation

**Non-vacuity (mutation control).** With the drafted guard, appending a comment to
`examples/culture-d4/components/13-register-law.yml` in an isolated copy:

```text
exit 1  E2E-DIGEST: D4 component examples/culture-d4/components/13-register-law.yml:
        the assembler recorded c0d77181ac56… but the bytes measure 93ab43865684…
```

Byte-identical to the unpatched control run. **The guard adds naming, not
detection** — `v3_verify_component_digests` (`tools/exercise-handoff-e2e.py:2208-2222`)
already catches the mutation. Claim O must not be reported as closing a detection
gap (`O05` §4, `R02` Finding 6, `A01` r37:26-31 — all concur, reproduced here).

**In-sync control (the guard goes green, not silent).** With the read set expanded to
59 members in an isolated copy:

```text
OK   manifest-roster: the packet component manifest (13 members) is carried by the live read set (59 members)
```

The guard reports in-sync after the fix route lands; it never silently disables
itself. (That run also exits 1 on the frozen-packet leg, because the read-set
expansion moves the packet sha — the expected r7-baseline drift `O04` §2 measured.)

**Rejected shapes.** Reproduced independently: the **global raising** guard emits
**6** `manifest-roster` rows (D2's legitimate partial read set) and reddens the r7
chain to **exit 1** — the false-red machine `R02` Finding 2 and `O01` §3 name. The
**D4-scoped raising** shape is measured by O01 §3 and R02 Finding 3 (r7 red, and the
selftest's own positive run breaks); this seat did not re-run it and attributes those
readings.

**Preservation.** Live tree after every run: `git rev-parse HEAD` →
`9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26`; `git status --porcelain` →
`?? reports/round-38/` only; `git diff --name-status 9bccc9b -- tools/gates/frozen corpus/lessons reports/round-1 reports/round-34` → **empty**. Filed r7 bytes, re-measured
after the sweep:

```text
packet.md     45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19
expected.json bbe15887b710bb36def5e1c82fa5b1c1ef37df3cb5581c7c2982a0498e829d55
twin.json     0e22913850cd85bc393fe6d0d7a8bf448e9b253aa2884457d4c8999ac9096599
claims-map.md d181de28ccafda2d34e40277a5390f7e42c64247fbbdcdec3df9a592aa48980c
```

`diff -r` between the patched and unpatched copies' `reports/round-34/handoff` →
byte-identical. **Zero freeze bytes moved; no re-freeze of `declared-in-r7`; no
in-tree `run-validation.py` executed.**

## 6. The corrected O08 expectation (falsifiable, as measured)

Replace `targets.json` seat O08's *"only the r7 row names; others stay green"* with:

> **O08 corrected.** Sweep all **10** filed v3 rows (`profile:
> kotodama-handoff-e2e/3`; r3/r4 are declaration records, not v3 rows). Under the
> drafted guard each row gains **exactly one** `manifest-roster` row naming
> `examples/culture-d4/components/13-register-law.yml`; the record-count delta is
> **+1**; **no** existing row's verdict changes. The r7 default chain exits **0**
> with packet `45f57132…` unchanged; the other nine rows keep their **pre-existing**
> exit 1 `E2E-READSET` (naming `reports/round-20/handoff/claims-map.md`), recorded
> as pre-existing, not as guard regressions. The guard's subject is the **live**
> tree, so it names on all ten rows; the **per-row** 13-vs-12 asymmetry is a
> separate measurement and holds on **4** rows — r27, r28, r6, r7 — not 2.

This is the only form the evidence supports. The alternative — narrowing the guard
until it names only r7 — would make it vacuous on the class the claim exists to
catch (`X02` §4a's own argument), and would still be false against the live-tree
subject.

## Owed

- **Integrator (expectation):** `targets.json` seat O08's wording is unsatisfiable as
  filed and this seat may not edit it. Substitute §6's corrected form; the two
  readings (live-tree subject vs per-row asymmetry) must be stated separately or the
  acceptance test is ambiguous.
- **Integrator (census correction):** `R02` Finding 5 and `X02` §4a both under-count.
  The filed v3 row set is **10**, and the per-row asymmetry holds on **4** rows
  (r27/r28/r6/r7), not 6 and not 2 respectively. Any claim-O acceptance test that
  replays "r2..r7" should name the 10 rows and mark the nine pre-existing reds.
- **O01/O02/O03:** none blocked. §3's sweep is the regression leg the O block owed;
  the guard's shape (D4-scoped, record-only, placed before the abort) is confirmed
  regression-clean on the full census, not the 6-row sample.
- **Cross-claim (R03/X01):** claim O's operability value is **naming**, not
  detection (§5). The X02 honesty critic should weigh that explicitly; this seat
  does not.
- **Dependency gap:** `reports/round-38/op/O07-scribe.md` is filed **0 bytes**
  (empty) — the O block's scribe seat produced no bytes. Recorded, not repaired
  (another seat's out path).
- **Not owed / out of scope:** no filed-byte rewrite, no re-freeze, no `CLAIMS_MAP`
  move, no read-set edit, no freshness axis-move, no promotion/canon/closure verdict.

## Citations

- `reports/round-38/targets.json` seat O08 (`:230-235`); `reports/round-38/claims.json` claim O (`thresholds`: "selftest green with the new controls; r7 packet sha unchanged 45f57132…")
- `reports/round-38/op/O01-guard-design.md` §1-§7 (the patch applied verbatim; declared patched digest `ae22013b…`)
- `reports/round-38/op/O04-fix-route.md` §1-§3,§6; `reports/round-38/op/O05-verify-route.md` §1-§5; `reports/round-38/op/O06-receipt.md` §4.3
- `reports/round-38/review/R02-o-review.md` Findings 1-6 (esp. Finding 5's 6-row table and Finding 3's D4-raising reading)
- `reports/round-38/cross/X02-honesty.md` §4a (the 13-vs-12 table and the "r6 and r7 name" form), §4b (the abort-ordering constraint), §5 tests 4-5
- `reports/round-38/adj/A02-receipt.md` F-A02-3 (`:124-146`); `reports/round-38/cross/X00-connector.md:335,363`; `reports/round-38/scribe/S01-integration-draft.md:473-474`
- `tools/exercise-handoff-e2e.py:157-171,188,1939-1965,2045-2056,2208-2222,2255-2262,2585-2590,3646-3662,3821-3838,4165-4169,4660-4663`
- `reports/round-34/handoff/repin.json` R34-D-history; `reports/round-37/adj/A01-freeze-adjudication.md:5,26-35`; `reports/round-37/op/defect-queue.json` (`R36-R7-READSET-13`)
- Command evidence (all in isolated `git archive 9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26` copies under `.scratch/o08/`, `TMPDIR=$PWD/.scratch`):
  - `.scratch/o08/tree` / `treeP` / `treeO` / `treeG` / `mut` / `mutP` / `mutO` / `syncO` (unpatched, O01-landed, global-raising, mutation and in-sync variants)
  - `patch -p1 --dry-run < ../o01-guard.patch` → clean; `patch -p1` → applied; patched tool `ae22013b5ddd77aa1b598cef1f5a57f0fb76bfc6eb8541d56e180fe70abcf6c2`
  - `--profile v3 --quiet --baseline <row>` for the 10 rows, unpatched: 9× exit 1 `E2E-READSET` naming `reports/round-20/handoff/claims-map.md`; r7 exit 0 `packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19`
  - `--profile v3 --json --baseline <row>` under the drafted guard: `manifest-roster` rows = 1 on all 10; record delta +1; non-guard `(check, ok)` tuples identical to unpatched on r7/r6/r5
  - r6 non-quiet under the guard → `FAIL manifest-roster …` **and** `FAIL read-set-roster: reports/round-20/handoff/claims-map.md …`, then `exit=1`
  - `--profile v3 --selftest` under the guard → exit 0, "plus 45 controls", m15a/m15b green
  - `mutO` (guard + mutated 13th component) → exit 1 `E2E-DIGEST: D4 component … c0d77181ac56… but the bytes measure 93ab43865684…` (identical to unpatched `mut`)
  - `syncO` (read set 59) → `OK manifest-roster: the packet component manifest (13 members) is carried by the live read set (59 members)`
  - `treeG` (global raising) → exit 1, 6 `manifest-roster` rows (D2), r7 red
  - per-row baseline asymmetry probe → all 10 rows: `inputs` 58, D4 components 12; rows whose own `packet.md` names 13 components: r27, r28, r6, r7 (4 of 10)
  - r3/r4 declaration records → exit 2 `E2E-BASELINE: frozen baseline is missing [17 keys] — it was not written by this exercise`
  - `git rev-parse HEAD` → `9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26`; `git status --porcelain` → `?? reports/round-38/` only; `git diff --name-status 9bccc9b -- tools/gates/frozen corpus/lessons reports/round-1 reports/round-34` → empty
  - `sha256sum` (filed bytes, unmoved after the sweep): r7 `packet.md 45f57132…`, `expected.json bbe15887b710bb36def5e1c82fa5b1c1ef37df3cb5581c7c2982a0498e829d55`, `twin.json 0e229138…`, `claims-map.md d181de28…`; `tools/exercise-handoff-e2e.py bfe1c78e479f74784e3d2b53b053b43cd8333214c46bcc8b908b3b45ebff0aa9`; `diff -r` patched vs unpatched `reports/round-34/handoff` → byte-identical
