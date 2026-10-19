- Seat: O03 | verifier | claim O | date 2026-10-19 | baseline 9bccc9b

# O03 — independent verification of O02 (and of the O01 draft it reconstructs)

**Mission** (`reports/round-38/targets.json` seat `O03`): *"Independent isolated verification of
O02."*

**Dependency state at seat start.** Both O01 and O02 were absent when this seat started (they
are two of the 10 seats the interrupted batch never ran). This seat therefore reconstructed the
guard itself in isolated `git archive` copies and measured a seven-variant matrix (§2). **O01
(`op/O01-guard-design.md`, 08:22), O02 (`op/O02-isolated.md`, 08:25) and O08
(`op/O08-regression.md`, 08:26) landed during the run**; §1, §4 and §5 below verify the filed
drafts as artifacts, and §2's matrix is the independent reconstruction they can be checked
against. All halves are reported.

**Verdict.** O01's draft **verifies against every claim-O threshold**: applied to a fresh
`git archive 9bccc9b` copy, its documented patch (sha `c4141c716c5b634051ae08dd2cb6fbc13893b291f9ce6913a8a60e7bc4e0e4d9d`)
reproduces its documented patched-tool hash (`e581275129eb765399355374e8c5e29b50399fb98cbf860012b333b3eb02a553`)
exactly, names the r7 member, leaves the r7 default chain at exit 0 with packet `45f57132…`, and
passes `--selftest` at **exit 0, "plus 45 controls"** with both `m15a` and `m15b` present. O02's
fragment is **substantively correct on the four load-bearing constraints** (global scope,
rendered-text vacuity, the two-build control split, the distinct row class) and its §5 and §7
controls reproduce here — but it carries **three measured defects** (§4.1: its selftest count
`44` is wrong, the artifact yields `45`; §4.2: its `m15b` description contradicts O01's actual
assertion; §4.3: its §7 tamper prediction names the wrong leg). One **shared limitation** of both
drafts is named in §3 and is the round's most consequential finding for the O08 sweep: both
guards read the **live** `V3_READ_SET`, so they are **row-blind** — they name the r7 member on
*all 10* filed v3 rows and cannot see any row's own frozen-row defect. A **fourth defect** (§4.4)
concerns the O08 fragment: its patched-tool digest `ae22013b…` is its own variant, not O01's
filed patch, so its claim that the two agree is false — though O08's readings reproduce and its
row-blindness census independently confirms §3.1.

All runs: `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`; isolated `git archive` copies
only; **no in-tree `reports/round-*/run-validation.py` executed anywhere** (F-C13-1); no
`--freeze` issued against `reports/round-34/handoff/declared-in-r7`; zero filed bytes written
(`git status --short` → `?? reports/round-38/` only; `git diff --name-status 9bccc9b` → empty).

---

## 1. Verification of the O01 artifact as filed

O01 §6 embeds the patch in a fenced `diff` block. I extracted the block from the filed markdown
and hashed it — it is **byte-identical to the `o01-guard.patch` on disk**:

```text
extracted fenced diff bytes: 4584
extracted sha256: c4141c716c5b634051ae08dd2cb6fbc13893b291f9ce6913a8a60e7bc4e0e4d9d
O01 documented   : c4141c716c5b634051ae08dd2cb6fbc13893b291f9ce6913a8a60e7bc4e0e4d9d  (match)
o01-guard.patch on disk: c4141c716c5b634051ae08dd2cb6fbc13893b291f9ce6913a8a60e7bc4e0e4d9d
identical text: True
```

Applied to a fresh `git archive 9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26` copy:

```text
patch -p1 --dry-run < o01-guard.patch   -> checking file tools/exercise-handoff-e2e.py / DRYRUN_OK
patch -p1        < o01-guard.patch      -> patching file tools/exercise-handoff-e2e.py / APPLIED
sha256sum tools/exercise-handoff-e2e.py -> e581275129eb765399355374e8c5e29b50399fb98cbf860012b333b3eb02a553
                                           (O01 documented patched hash — exact match)
base tool sha256                        -> bfe1c78e479f74784e3d2b53b053b43cd8333214c46bcc8b908b3b45ebff0aa9
```

Claim-O thresholds, measured on that patched copy:

| threshold (`claims.json:20-21`) | required | measured | verdict |
|---|---|---|---|
| manifest-member-not-in-readset **named** | `13-register-law.yml` appears | `FAIL manifest-roster: examples/culture-d4/components/13-register-law.yml: in the packet component manifest (13 members, packet.d4.yml assembly.source_sha256) but not in the live read set (58 members) — the roster is incomplete; the bytes are still digest-checked` | **met** |
| r7 default chain unchanged | exit 0, packet `45f57132…` | `exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19` | **met** |
| `--selftest` green with **≥2** new controls | 2 controls, exit 0 | `plus 45 controls`; `m15a roster gap named, not raised …`; `m15b in-sync roster green …`; exit **0** | **met** |
| r7 packet sha unchanged | `45f57132…` | `sha256sum reports/round-34/handoff/declared-in-r7/packet.md` → `45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19` | **met** |
| zero freeze bytes moved | r7 row byte-identical | `claims-map.md d181de28…`, `expected.json bbe15887…`, `freeze.txt 3969954b…`, `packet.md 45f57132…`, `run.log ffae4ecd…`, `twin.json 0e229138…` | **met** |
| fix route still reachable | `--freeze` not blocked | see §3.3 | **met** |

**Independent re-derivation of the guard's green half.** O01 §4 claims the guard "goes green —
not silent" once the fix route lands. I rebuilt that state independently (13th member added to
`D4_COMPONENTS`, defaults re-pointed, O01's patch applied) and re-froze:

```text
OK   manifest-roster: the packet component manifest (13 members) is carried by the live read set (59 members)
handoff-v3: exit=0 … packet_sha256=fd28d25d008ec069589484b191bdfdf39aacba509fdbf25fe8d4a3d9a86ddf51
```

The digest differs from O01's `26a7882d…`, O04's `b102aa70…` and O05's `9e003970…` because the
successor path string differs in each run (O05 D-2: the renderer emits `V3_BASELINE_DEFAULT`
into the packet prose at `tools/exercise-handoff-e2e.py:3189`). **The green reading itself
reproduces; the pinned digest is path-coupled** — an independent confirmation of O05 D-2, and
the reason no seat's successor digest should be treated as canonical.

## 2. The independent reconstruction — a seven-variant matrix

Before O01/O02 landed I built seven guard variants by patching a single anchor
(`assembly = V3Assembly(root)`, `tools/exercise-handoff-e2e.py:3821`) in separate archives.
Each is a different answer to "which two sets does the guard compare?":

| variant | manifest side | read-set side | r7 default chain | rows named on r7 | selftest |
|---|---|---|---|---|---|
| **G1** global raise | D2+D3+D4 manifests | live `V3_READ_SET` | exit **1**, packet not assembled | **7** (6 D2 + 1 D4) | n/a |
| **G2** D4 raise | D4 manifest | live `V3_READ_SET` | exit **1** | 1 | **breaks** (AssertionError) |
| **G3** D4 record-only | D4 manifest | live `V3_READ_SET` | exit **0**, `45f57132…` | 1 | exit **0**, 43 controls |
| **G4** row record-only | D4 manifest | `baseline["inputs"]` (live manifest ∖ frozen row) | exit **0**, `45f57132…` | 1 | n/a |
| **G5** frozen-row self-consistency | the **row's own** `packet.md` prose count | the **row's own** `inputs` count | exit **0**, `45f57132…` | 1 | exit **0** |
| **G6** preflight-placed raise | D4 manifest | live `V3_READ_SET` | exit **1** | 1 | n/a |
| **G7** rendered-text | the **rendered** `packet.md` table | `baseline["inputs"]` | exit **0**, `45f57132…` | **0 — vacuous** | n/a |

**G1 reproduces R02's Finding-2 count exactly**: 7 named rows, 6 of them the legitimate D2
partial read set (D2's manifest holds 9 members, the read set carries 4 —
`tools/exercise-handoff-e2e.py:51-52`, `:2255-2262`). R02 reported exit 1 because its variant
raised; mine records. **The disagreement is the raise, not the scope** — R02 and this seat agree
on the rows.

**G2 confirms R02 Finding 3 and O01 §3 from an independent build**: the raising shape breaks the
selftest's own positive run, `AssertionError` at `tools/exercise-handoff-e2e.py:4200`, because
the fixture freeze pins exactly `V3_READ_SET` (`:4165-4169`) and so reproduces the asymmetry.

**G7 confirms R03-C1 from an independent build**: a guard that parses the **rendered** packet
table sees 12 D4 rows, never names the 13th, and reports green. The rendered channel is
**vacuous** — it can never name the defect it was written for.

**G6 tests placement, which no filed draft measures.** A guard placed inside `v3_preflight`
(`:3295`) instead of inside `v3_exercise` (`:3821`) is **fatal to the fix route**: `v3_freeze`
(`:3997-4005`) calls `v3_preflight` directly and refuses to freeze a packet that fails it —

```text
G6 --freeze /tmp/g6succ
could not freeze: E2E-ROSTER refusing to freeze a packet that fails preflight:
  examples/culture-d4/components/13-register-law.yml: in the D4 packet component manifest but not in the live read set
```

So a guard that **refuses** at the preflight site blocks its own remedy. O01's choice of the
`v3_exercise` site (after `:3821`, before the supersession block at `:3823`) is therefore not
cosmetic — it is the difference between a guard and a deadlock. This seat confirms O01 §2's
placement by construction and by contrast.

## 3. The shared blind spot — both filed guards are row-blind

### 3.1 Measured

O01's guard compares the **live** D4 manifest against the **live** `V3_READ_SET` (its
`roster_gap` at the patched `:3835` reads `V3_READ_SET`, never `baseline["inputs"]`). O02 §1's
reconstruction does the same. Replaying the filed v3 rows under O01's patched tool — **all
ten** of them (the census is 10, not 6; see §3.5) — every one emits the same row:

```text
round-20/handoff                    exit=1  manifest-roster: 13-register-law.yml (identical text)
round-22/handoff/declared-in        exit=1  manifest-roster: 13-register-law.yml (identical text)
round-22/handoff/declared-in-r2     exit=1  manifest-roster: 13-register-law.yml (identical text)
round-26/handoff/declared-in-r5     exit=1  manifest-roster: 13-register-law.yml (identical text)
round-26/register/v3-baseline-r26   exit=1  manifest-roster: 13-register-law.yml (identical text)
round-26/remainders/v3-baseline-r26 exit=1  manifest-roster: 13-register-law.yml (identical text)
round-27/pinsweep/v3-baseline-r27   exit=1  manifest-roster: 13-register-law.yml (identical text)
round-28/pinsweep/v3-baseline-r28   exit=1  manifest-roster: 13-register-law.yml (identical text)
round-30/handoff/declared-in-r6     exit=1  manifest-roster: 13-register-law.yml (identical text)
round-34/handoff/declared-in-r7     exit=0  manifest-roster: 13-register-law.yml (identical text)
```

`d4roster=1` on every row. The guard's output is **identical on every row** — it is a property
of the live tree, not of the row being replayed. Consequence: it cannot distinguish a row that
has the defect (r6, r7, r27, r28) from one that does not (r20, r2, r5). X02 §4a measured that
r6 carries the **same frozen-row defect** as r7 (`its frozen packet declares 13 D4 components,
its frozen inputs carry 12`); under O01's guard r6 is named for the *live* reason, not its own,
so the r6 defect is **never actually detected** — only coincidentally named. **This is
independently confirmed by O08** (`op/O08-regression.md` §0(a): "the guard names the D4 member
on **all 10** filed v3 rows — including r20, r2, r5"), which measured the same row-blindness
from a separately built tree. O08 and this seat agree.

### 3.2 The formulation that does discriminate

G5 compares the **row's own frozen bytes against each other**: the D4 count the row's own
`packet.md` prose declares (`9 D2, 4 D3, N D4`, emitted by
`tools/exercise-handoff-e2e.py:2542` from `len(d4["components"])`) against the D4 member count
in the row's own `inputs`. Measured across the filed v3 rows that carry a full baseline shape:

| filed row | frozen prose D4 | frozen table D4 rows | frozen `inputs` D4 | G5 verdict |
|---|---|---|---|---|
| `round-20/handoff` | 12 | 12 | 12 | **OK** |
| `round-22/handoff/declared-in` | 12 | 12 | 12 | **OK** |
| `round-22/handoff/declared-in-r2` | 12 | 12 | 12 | **OK** |
| `round-26/handoff/declared-in-r5` | 12 | 12 | 12 | **OK** |
| `round-26/register/v3-baseline-r26` | 12 | 12 | 12 | **OK** |
| `round-26/remainders/v3-baseline-r26` | 12 | 12 | 12 | **OK** |
| `round-27/pinsweep/v3-baseline-r27` | **13** | 12 | 12 | **FAIL** — internally inconsistent |
| `round-28/pinsweep/v3-baseline-r28` | **13** | 12 | 12 | **FAIL** — internally inconsistent |
| `round-30/handoff/declared-in-r6` | **13** | 12 | 12 | **FAIL** — internally inconsistent |
| `round-34/handoff/declared-in-r7` | **13** | 12 | 12 | **FAIL** — internally inconsistent |


G5 reproduces X02 §4a's discrimination (the defective rows name, the clean ones stay green) from
an independently written guard, and it is the **only** variant of the seven that does. Its r7
default chain is also unchanged: `exit=0 … packet_sha256=45f57132…`. **Its row set is wider than
X02 §4a's**: X02 sampled only the four `declared-in*` directories and reported r6 + r7; the full
census in §3.5 shows **four** rows carry the asymmetry — `r27/pinsweep`, `r28/pinsweep`, r6 and
r7. G5 was run against **all 10** filed rows and returns exactly those four `FAIL` and six `OK`
(`v3-baseline-r26` ×2 → `OK`; `v3-baseline-r27` → `FAIL`; `v3-baseline-r28` → `FAIL`). O08
independently measured the same four (`op/O08-regression.md` §0(b)) from a separately built
guard, and this seat's G5 confirms both. So X02's r6+r7 is correct-but-incomplete, and O01 §2
and O02 §1 inherited the incomplete form by citing it.

### 3.3 Why G5 is additionally freeze-compatible

G5 reads the **frozen row's** bytes, not the live read set, so it raises nothing on the live
tree and `--freeze` remains reachable (measured: `froze /tmp/g5succ: packet sha256 45f57132…`).
O01's guard is equally freeze-safe — but for the different reason that it records rather than
raises. A **raising** guard is unsafe at *either* site: at the `v3_exercise` site it reds the r7
chain (G2), at the preflight site it deadlocks `--freeze` (G6).

### 3.4 The finding

**The O claim's wording is under-specified in a way that decides the outcome.** `claims.json:20`
says the guard compares *"a frozen baseline's read set and the packet's own component manifest"*.
Read literally ("the frozen baseline's read set"), the read-set side is `baseline["inputs"]` —
which makes the guard **row-sensitive** and, in G4's live form, names *every* row. Read as the
drafts implement it (the live `V3_READ_SET`), the guard is **row-blind** and names every row
anyway. Only the **G5** reading — the row's own bytes against each other — yields a guard that
both keeps r7 green and discriminates the defective rows from the clean ones.

For the round's own O08 mission ("every filed frozen row replayed in isolation under the guard —
only the r7 row names; others stay green", `targets.json` seat `O08`), the measured truth is:

- **O01/O02's landed guard**: names `13-register-law.yml` on **all 10** filed v3 rows (§3.1) —
  so "only r7" is false by construction, and the nine extra names are the *live* defect reported
  against rows that do not have it. The correct reading is "the new guard adds exactly one row to
  every replay that reaches it, and changes no existing row's verdict" (O01 §Owed already says
  this; O08 §6 reaches the same form independently).
- **A G5-style guard**: names the **four** asymmetric rows (r27, r28, r6, r7) — the only reading
  under which the sweep's expectation is satisfiable at all, and the one O08 §0(b) also
  identifies.

This is not a defect in O01's landing (it satisfies claim O as written, and claim O does not
promise row discrimination). It is the reason the sweep's threshold must be rewritten, and the
reason a future round should consider the G5 formulation if row-level attribution is wanted.

### 3.5 The census is 10, not 6 — one extra path is a twin, not a baseline

O08 §1 reports the filed v3 row census as **10**. This seat's independent `python3 -c` sweep over
every `reports/**/expected.json` returns **11** paths carrying
`profile: kotodama-handoff-e2e/3`, one of which is not a replayable baseline:

```text
11 paths with profile kotodama-handoff-e2e/3
  - 10 are v3 baselines (carry `inputs`, `expected_exit`, … — the shape v3_load_baseline requires)
  - 1 is reports/round-26/remainders/r4-twin/expected.json — a twin record, not a baseline:
    keys ['binding','date','declared_by','kind','limits','packet_sha256','packet_version',
          'profile','reason','revision','source_packet','twin_counts','twin_path','twin_sha256',
          'v2_subset_digest'], with **no** `inputs`
```

Replaying it as a baseline fails as expected: `E2E-BASELINE: frozen baseline is missing
['packet_id','expected_exit',…,'inputs',…] — it was not written by this exercise`. So **O08's
count of 10 is correct and this seat's raw profile count of 11 is a false positive** — the
`r4-twin` record is a twin descriptor that shares the profile string. O08's §1 table is right;
R02 Finding 5's six-row sample was the incomplete one (O08 adds `r26/register`,
`r26/remainders`, `r27/pinsweep`, `r28/pinsweep`).


## 4. Defects in O02 (and one in O08)

### 4.1 D-1 — O02 §2's selftest count `44` is wrong; the artifact yields `45`

O02 §2's threshold table records *"58-member build: `selftest: OK … plus 44 controls`"* and
*"59-member build: `selftest: OK … plus 44 controls`"*. Measured on the filed artifact:

```text
unpatched tool:  38 `results.append` calls -> selftest prints "plus 43 controls"
O01-patched:     40 `results.append` calls -> selftest prints "plus 45 controls"
```

Two new controls added to a 43-control suite is **45**, not 44 — O02's arithmetic dropped one.
O01's own §6.1 reports `45` and is correct. The discrepancy is cosmetic to the claim (the
threshold is "≥2 new controls", which is met either way) but it is a wrong number in a filed
verification fragment, and a downstream seat copying it would inherit the error.

### 4.2 D-2 — O02 §2's `m15b` description contradicts O01's actual assertion

O02 §2's threshold table describes the in-sync control as *"the `manifest-roster` leg is green
and names nothing"*, and its §1 control **m15b** code asserts
`not any(... not r["ok"] for r in records)`. O01's landed `m15b` asserts the opposite shape —
the row is present **and green and names the member**:

```text
O01 patched tool :4567  assert D4_ROSTER_MEMBER in str(green[-1]["detail"]) or "carried by the" in green[-1]["detail"], green
actual selftest output : m15b in-sync roster green: the read set carries every manifest member, exit 0 with the manifest-roster row green
```

The live guard records a **green** `manifest-roster` row when the roster is in sync (O01 §6's
`if not roster_gap:` branch, patched `:3845-3850`), so "names nothing" is false — the leg
*names the manifest as carried*. The actual artifact matches O01; O02's prose does not.

### 4.3 D-3 — O02 §7's tamper prediction does not reproduce

O02 §7 predicts that content-tampering the non-member `13-register-law.yml` under the guard
yields `E2E-DIGEST: the assembled packet does not match the frozen packet digest` (the
assembled-vs-frozen leg). Measured under O01's patched tool:

```text
tamper 13-register-law.yml (non-member) + O01 patch:
  E2E-DIGEST: D4 component examples/culture-d4/components/13-register-law.yml:
              the assembler recorded c0d77181ac56… but the bytes measure a4e8a3f0c1c7…
```

The **per-component digest leg** fires (`v3_verify_component_digests`, `:2208-2222`) — inside
`V3Assembly`, which is constructed at `:3834` **before** the guard at `:3835` and long before
the frozen-packet compare at `:3951-3957`. Identical on the unpatched tree, which is O05 §4's
finding. O02's *conclusion* in §7 is right (the guard is naming, not detection, and a
verifier expecting the `CLAIMS_MAP`-style `input-digest` detail will not find it here); its
*mechanism* is wrong — the leg that fires is the component leg, not the frozen-packet leg.
O02 §7's last paragraph in fact cites O05 §4 / R02 Finding 6, which state the correct mechanism.

### 4.4 D-4 — O08 and O01 declare different patched-tool digests; O08's citation of O01 is false

O08 §1 and §8 state that its patched tree's digest `ae22013b5ddd77aa1b598cef1f5a57f0fb76bfc6eb8541d56e180fe70abcf6c2`
*"is exactly the digest O01 §6 declares"*. **O01 declares a different value.** Measured:

```text
O01 §6 (op/O01-guard-design.md:144, :309)  declares patched tool -> e581275129eb765399355374e8c5e29b50399fb98cbf860012b333b3eb02a553
this seat: apply o01-guard.patch to a fresh git archive  -> e581275129eb765399355374e8c5e29b50399fb98cbf860012b333b3eb02a553  (O01's value)
O08's own tree (.scratch/o08/treeO)                     -> ae22013b5ddd77aa1b598cef1f5a57f0fb76bfc6eb8541d56e180fe70abcf6c2
```

O08's tree differs from O01's declared artifact by **exactly one hunk** — the `m15b` result
string:

```diff
< "m15b in-sync roster green: the read set carries every manifest member, exit 0 with no "
< "manifest-roster row"
---
> "m15b in-sync roster green: the read set carries every manifest member, exit 0 with the "
> "manifest-roster row green"
```

The `<` side is O08's tree, the `>` side is O01's declared patch (and the filed O01 §6 fenced
block). So `ae22013b…` is **O08's own variant**, not O01's patch — the two are not the same
artifact, and O08's claim that its digest "is exactly the digest O01 §6 declares" is false. O08's
own §8 line even prints the base tool as `bfe1c78e…` and then asserts the identity, which cannot
both hold with O01 §6. Note this is the *same* `m15b` string that O02 D-2 (§4.2) gets wrong, and
in the same direction: both O02 and O08 describe `m15b` as "no row / names nothing", while the
**filed O01 artifact records a green row and names the member**. O08's digest mismatch is
therefore evidence that O08 patched a pre-O01 variant of the guard, not O01's filed draft.

Both trees are functionally equivalent for the claim's thresholds (this seat ran O08's treeO:
`--profile v3` → exit 0, packet `45f57132…`, one `manifest-roster` row; `--selftest` → exit 0,
`plus 45 controls`), so O08's *readings* stand; only its provenance claim is wrong.

## 5. Controls that reproduce exactly (so O02's substance stands)

These O02 claims were re-measured here and **confirm**:

- **§3 global scope = false-red machine.** G1 → 7 named rows (6 D2 + 1 D4). Row identities and
  count reproduce exactly.
- **§4 rendered-text guard is vacuous.** G7 → 12 rendered D4 rows, names nothing, exit 0.
  R03-C1 confirmed on the live tree.
- **§5 the in-sync control cannot be a mutation of the defective tree.** Removing the 13th row
  from `examples/culture-d4/packet.d4.yml` dies at the **projection pin** before any roster leg:
  `examples/culture-d4/typed-labels.d4.yml assembly.packet_sha256: the tree recorded
  aac91246cede… for examples/culture-d4/packet.d4.yml but the bytes measure 0809bc63c820…`.
  Confirmed — the honest in-sync fixture is the post-fix tree.
- **§6 the two row classes are distinct for free.** The existing supersession check records
  `read-set-roster` (`:3827`) and O01's guard records `manifest-roster`; on the r6 replay both
  appear, and the `E2E-READSET` verdict remains the supersession one. Confirmed.
- **§8 no redundancy.** D4 files outside the read set are exactly **two**: `README.md` (already
  named by the existing artifact-manifest leg) and `13-register-law.yml` (the defect). Confirmed
  independently: `read_set 58 | d4 files 20 | d4 not in read set: ['examples/culture-d4/README.md',
  'examples/culture-d4/components/13-register-law.yml']`.
- **§2's r7 thresholds** (named / exit 0 / `45f57132…` / selftest green / zero bytes moved):
  all confirmed in §1 above.

## 6. What this seat ran, and what it did not

- **Ran**: thirteen isolated `git archive 9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26` copies
  (base, G1, G2, G3, G4, G5, G6, G7, G3-synced, G5-synced, O01-doc-patched, O01-synced,
  O08-treeO); `--profile v3`, `--quiet`, `--selftest`, `--freeze`; **ten** filed-baseline
  replays; `patch -p1 --dry-run` + apply against three patch variants; `runpy` probes;
  `sha256sum`, `git status`, `git diff --name-status`, `diff`, `grep`.
- **Did not run**: any in-tree `reports/round-*/run-validation.py`, in-tree or in a copy;
  no re-freeze of `declared-in-r7`; no edit to any filed byte, tool, or example. All patches
  live in `.scratch/o03/*` (gitignored) as drafts. O08's own tree (`.scratch/o08/treeO`) was
  read and executed for the §4.4 reconciliation but not modified.

## Owed

- **`reports/round-38/run-validation.py` — absent** (`ls` → No such file or directory). Claim
  O's second counting command (`python3 reports/round-38/run-validation.py`) and both claims'
  threshold command are **`to-verify`** regardless of what lands; every number in this fragment
  comes from the tool CLI. Per F-C13-1 the runner must never be executed in-tree even once it
  lands.
- **O08 (regression sweep):** the threshold must be rewritten before the sweep runs. O01/O02's
  landed guard names `13-register-law.yml` on **all 10** filed v3 rows alike (§3.1) — "only the
  r7 row names; others stay green" is unsatisfiable against it. O08 §0 and §6 already reach the
  corrected form independently and this seat confirms it: "the new guard adds exactly one row to
  every replay that reaches it and changes no existing row's verdict", with the **9** pre-existing
  `E2E-READSET` reds recorded as pre-existing (O08 §1's 10-row census; R02 Finding 5's 6-row
  sample was incomplete). If row-level attribution is wanted, §3.2's frozen-row self-consistency
  formulation is the measured one — it names the **4** asymmetric rows (r27, r28, r6, r7), it is
  **not** what landed, and it would be a new claim.
- **O02 fragment (filed):** D-1 (`44` → `45`), D-2 (`m15b` names the member, green, rather than
  "names nothing") and D-3 (§7's mechanism is the component leg, not the frozen-packet leg)
  should be corrected in a follow-up row or folded into the landing record. The fragment's
  conclusions stand; only these three statements are wrong.
- **O08 fragment (filed):** D-4 — §1/§8's claim that its patched digest `ae22013b…` "is exactly
  the digest O01 §6 declares" is false; O01 §6 declares `e5812751…`, and the two artifacts differ
  by the `m15b` result string. O08's readings and census stand; only the provenance claim needs
  correcting (it should say "a variant of O01 §6 with the `m15b` string adjusted", or simply not
  attribute the digest to O01).
- **Integrator:** apply O01 §6 as one step (helper + guard + the two controls). O01's draft and
  O02's reconstruction agree on the guard's shape; O01's is the artifact that reproduces its
  own documented hashes, so **O01 §6 is the patch to land** — not O08's `ae22013b…` variant.
- **Not owed / out of scope:** no read-set edit, no re-freeze, no `CLAIMS_MAP` move, no
  freshness axis-move, no filed-byte rewrite, no canon/promotion/closure verdict.

## Citations

- `reports/round-38/targets.json` (seats O01, O02, O03, O08; `shared_rules`);
  `reports/round-38/claims.json:13-24,26` (claim O text, thresholds, counting commands, non-goals)
- `reports/round-38/op/O01-guard-design.md` §1-§7 (the draft verified here; its documented patch
  sha `c4141c716c5b634051ae08dd2cb6fbc13893b291f9ce6913a8a60e7bc4e0e4d9d` at `:145`, `:309`
  reproduces exactly from the fenced block at `:147`)
- `reports/round-38/op/O02-isolated.md` §1-§9 (the fragment verified here; defects D-1/D-2/D-3)
- `reports/round-38/op/O08-regression.md` §0, §1, §6, §8 (10-row census and row-blindness reading
  confirmed here; D-4 on the `ae22013b…` provenance claim at `:18`, `:83`, `:241`, `:250`)
- `reports/round-38/review/R02-o-review.md` Findings 1-6, guard-point recommendation;
  `reports/round-38/review/R03-cross-review.md` §3 (C1), §5 (C2);
  `reports/round-38/cross/X02-honesty.md` §3, §4, §4a, §4b;
  `reports/round-38/op/O04-fix-route.md` §1-§5; `reports/round-38/op/O05-verify-route.md` §1,§3,§4
- `tools/exercise-handoff-e2e.py:51-59,157-171,188,1937-1965,2045-2056,2208-2222,2255-2262,2542,
  2585-2590,3189,3295-3298,3646-3662,3811-3838,3839-3843,3951-3957,3997-4005,4165-4169,4193-4200,4543-4570`
- `examples/culture-d4/packet.d4.yml:2875-2888`; `examples/culture-d4/typed-labels.d4.yml` (the
  pin that blocks the in-sync mutation, §5); `examples/culture-d4/components/13-register-law.yml`
  (`sha256 c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7`)
- `reports/round-34/handoff/declared-in-r7/{expected.json,packet.md,twin.json,claims-map.md,freeze.txt,run.log}`
- The 10 filed v3 baselines replayed in §3.1/§3.2: `reports/round-20/handoff/expected.json`,
  `reports/round-22/handoff/declared-in/expected.json`, `reports/round-22/handoff/declared-in-r2/expected.json`,
  `reports/round-26/handoff/declared-in-r5/expected.json`, `reports/round-26/register/v3-baseline-r26/expected.json`,
  `reports/round-26/remainders/v3-baseline-r26/expected.json`, `reports/round-27/pinsweep/v3-baseline-r27/expected.json`,
  `reports/round-28/pinsweep/v3-baseline-r28/expected.json`, `reports/round-30/handoff/declared-in-r6/expected.json`,
  `reports/round-34/handoff/declared-in-r7/expected.json`; plus the non-baseline
  `reports/round-26/remainders/r4-twin/expected.json` (§3.5)
- Command evidence (all in `git archive 9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26` copies under
  `.scratch/o03/`, `TMPDIR=$PWD/.scratch`):
  - `.scratch/o03/o01doc`: `patch -p1 --dry-run` → `DRYRUN_OK`; apply → patched tool
    `e581275129eb765399355374e8c5e29b50399fb98cbf860012b333b3eb02a553`; `--profile v3` → exit 0,
    one `FAIL manifest-roster` naming `13-register-law.yml`, packet `45f57132…`; `--selftest` →
    exit 0, `plus 45 controls`, `m15a` + `m15b` present; `--quiet` → exit 0
  - `.scratch/o03/o01synced`: `--freeze .scratch/o03/succ01` → exit 0, packet
    `fd28d25d008ec069589484b191bdfdf39aacba509fdbf25fe8d4a3d9a86ddf51`; `--profile v3` → exit 0,
    `OK manifest-roster: … (13 members) is carried by the live read set (59 members)`
  - `.scratch/o03/G1_global_raise` → 7 `FAIL manifest-roster` rows, exit 1;
    `G2_d4_raise` → exit 1 + `AssertionError` at `:4200`; `G3_d4_record_only` → exit 0, packet
    `45f57132…`, selftest exit 0; `G4_row_record_only` → exit 0 on r7, names on every replay;
    `G5_frozenrow` → r6/r7 `FAIL`, r20/r2/r5 `OK` (the full G5 sweep in §3.2 covers r27/r28 too);
    `G6_preflight` → exit 1 and
    `could not freeze: E2E-ROSTER refusing to freeze a packet that fails preflight`;
    `G7_rendered` → exit 0, names nothing
  - `.scratch/o03/base`: `--profile v3` → exit 0, packet `45f57132…`; `--selftest` → exit 0,
    `plus 43 controls`; filed-row replays → r20/r2/r5/r6 exit 1 `E2E-READSET`
    (`claims-map.md`), r7 exit 0
  - `.scratch/o03/o01doc`, all **10** filed v3 baselines replayed → `d4roster=1` on every row,
    exit 1 on the nine, exit 0 on r7 (§3.1); `reports/round-26/remainders/r4-twin/expected.json`
    → exit 2 `E2E-BASELINE: frozen baseline is missing […,'inputs',…]` (§3.5)
  - `.scratch/o08/treeO` (O08's own variant, read + executed, not modified): `--profile v3` →
    exit 0, packet `45f57132…`, one `manifest-roster` row; `--selftest` → exit 0, `plus 45 controls`;
    `diff` vs O01's patched tree → one hunk, the `m15b` result string (§4.4)
  - `.scratch/o01/{o01-guard.patch,from-doc.patch,final.patch}` applied to fresh archives →
    `e5812751…` (apply exit 0), `e5812751…` (exit 0), and `bfe1c78e…`/apply exit 1 (the
    working-tree diff `final.patch` does not apply to HEAD — it is a diff of O01's own scratch
    trees, not a HEAD patch); `grep -rl ae22013b` over the repo → only `.scratch/o08/{treeO,mutO}`
  - `.scratch/o03/o02s7`: tamper `13-register-law.yml` + O01 patch → `E2E-DIGEST: D4 component
    … recorded c0d77181ac56… but the bytes measure a4e8a3f0c1c7…`; identical unpatched
    (`.scratch/o03/o05cmp`)
  - `.scratch/o03/o02s5`: 13th manifest row removed → `E2E-DIGEST: examples/culture-d4/typed-labels.d4.yml
    assembly.packet_sha256: the tree recorded aac91246cede… but the bytes measure 0809bc63c820…`
  - `runpy` probe: `read_set 58 | d4 files 20 | d4 not in read set: ['examples/culture-d4/README.md',
    'examples/culture-d4/components/13-register-law.yml']`
  - profile census: 11 paths carry `profile: kotodama-handoff-e2e/3`; 10 are baselines, 1
    (`r4-twin`) is a twin record with no `inputs` (§3.5)
  - control arithmetic: base `38 results.append` → `plus 43 controls`; O01-patched
    `40 results.append` → `plus 45 controls`
  - `sha256sum` (unmoved): `tools/exercise-handoff-e2e.py bfe1c78e479f74784e3d2b53b053b43cd8333214c46bcc8b908b3b45ebff0aa9`;
    r7 `claims-map.md d181de28…`, `expected.json bbe15887…`, `freeze.txt 3969954b…`,
    `packet.md 45f57132…`, `run.log ffae4ecd…`, `twin.json 0e229138…`;
    `examples/culture-d4/components/13-register-law.yml c0d77181ac56…`
  - `git rev-parse HEAD` → `9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26`; `git status --short` →
    `?? reports/round-38/` only; `git diff --name-status 9bccc9b` → 0 rows
