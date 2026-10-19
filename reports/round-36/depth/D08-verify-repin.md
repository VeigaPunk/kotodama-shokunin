- Seat: D08 | verifier | claim D | date 2026-10-19 | baseline ce103bf

# D08 — the re-pin census, run independently: nine pin surfaces, six falsified by mutation, D04's list verified complete

**Object under verification:** D04's re-pin list, `reports/round-36/depth/D04-repin.md`.

**Status: the object did not exist when I began, and landed at 06:34 while I wrote.** At my
first check `ls reports/round-36/depth/` → `D01-design.md D02-packet-draft.md
D03-isolated-verify.md D05-receipt.md D06-gap-fill.md D07-verify.md D09-gap-fill.md
D10-scribe.md` (no `D04-repin.md`), with `D10-scribe.md:72` and `:174` listing it
**absent — owed**. So this fragment does two things in order: (a) it builds the criterion my
mission names ("Verify D04's re-pin list completeness with your own census") **independently
and before reading D04** — §1 the census, §2 the mutation matrix, §4 the findings — and then
(b) it applies that criterion to D04 as landed, at **§3.0**. The independence is real: §1–§2
were written and measured before `D04-repin.md` existed on disk, and §3.0's verdict is
derived by mapping D04's rows onto the census rather than by adopting its structure.

**Verdict on the object: completeness PASS, with one material omission.** All nine of my pin
surfaces appear in D04's 10-row list or its §4 negative table, D04's list contains no surface
my census missed, and two of D04's independent measurements reproduce exactly (§3.0). The
omission is the `A-NN` renumbering row (my F1); D04 is silent on it (`grep -c "D4_COMPONENTS"`
→ 0). Detail and the row-by-row mapping: §3.0.

**Write scope:** this file only. No tool, gate, packet, component, pin or filed 1–35 byte
written. No `--freeze` of `reports/round-34/handoff/declared-in-r7` was issued — its bytes
are pinned by this round's hard boundaries. No `reports/round-*/run-validation.py` was
executed, in-tree or in a copy (F-C13-1). Every command ran with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`. Baseline
`ce103bf5885af00023cdc4a174c17602476cdcf8` (`git rev-parse HEAD`; `git status --porcelain`
→ `?? reports/round-36/` plus the F8 mutation described below).

**Method.** I did not accept any sibling's list. I (a) enumerated the surfaces by grepping
the live tree for each D4 artifact's own sha256, then (b) **falsified the census by
mutation** in an isolated `git archive ce103bf` copy at `.scratch/d08-iso` — a surface that
does not move when the artifact moves is not a pin surface. §1 is the census, §2 the
mutation matrix, §3 the reconciliation, §4 the findings.

## 1. Census — every live surface that pins the D4 packet set

Digests below are the live bytes at `ce103bf` (measured, `sha256sum`); "membership" is
against the 58-entry `inputs` map of `reports/round-34/handoff/declared-in-r7/expected.json`.

| # | surface | path:line | what it pins | in the r7 read set? |
|---|---|---|---|---|
| S1 | `tools/gates/typed-pipelines.json` — `profiles[0]` | `:6-38` (`id` `:6`, `generation` `round-30-qreg-records` `:7`, `packet.sha256` `:12-13`, `projection.sha256` `:20-21`, `expected.sha256` `:28-29`, `assembler.sha256` `:16-17`, `adapter.sha256` `:24-25`) | `aac91246cede…`, `c23b0ab532cf…`, `e6ae9828d6c8…`, `943f487ba991…`, `92f5460bcc34…` | **no** (tools/ is not a member; only 7 D4-named tools are) |
| S2 | `examples/culture-d4/expected-holds.json` | `:3` `packet_sha256`, `:4` `projection_sha256`, `:6` `active_pin_generation` | `aac91246cede…`, `c23b0ab532cf…` | **yes** (`:158`) |
| S3 | `examples/culture-d4/packet.d4.yml` — its own `assembly` block | `:2875-2888` `source_sha256:` → 13 component rows incl. `13-register-law.yml` at `:2888`; `:2864` `assembler_sha256`; reader `:2866`, serializer `:2868` | all 13 components, the assembler, reader, serializer | **yes** (`:160`) |
| S4 | `examples/culture-d4/typed-labels.d4.yml` | `:9` `assembly.packet_sha256` | `aac91246cede…` | **yes** (`:161`) |
| S5 | `examples/culture-d4/packet.d4.typed.yml` | `assembly.{packet,projection,adapter,assembler}_sha256` | the three upstream artifacts + adapter | **yes** (`:159`) |
| S6 | `tools/gates/expected/register-law-gate/r30-post/expected.json` | `:10` `gate_sha256`, `:19` `inputs["examples/culture-d4/packet.d4.yml"]`, `:20` gate digest, plus the mirrored copy `:…/r30-post/packet.d4.yml` | `aac91246cede…`, `15f8b23251ca…` | **no** (a tools/ baseline) |
| S7 | `tools/gates/expected/d4-assembly-check-gate/r19-pre/expected.json` | `:18-29` the 12 component rows, `:29`…`packet.d4.yml` = `e7ecd2045ef0…`, `:31` assembler | **pre-family-clean bytes**, `e7ecd2045ef0…` | **no** |
| S8 | `tools/gates/expected/d4-typed-labels-check-gate/{r19-pre,r20-post,r22-post}/expected.json` | `:20`/`:18`/`:15` `inputs["examples/culture-d4/packet.d4.yml"]` = `e7ecd2045ef0…` | **pre-family-clean bytes** | **no** |
| S9 | `reports/round-34/handoff/declared-in-r7/{expected.json,packet.md,twin.json,freeze.txt}` | `expected.json:144-161` the 19 D4 members of the 58-file `inputs`; `freeze.txt:2` `packet_sha256: 45f57132…` | `aac91246cede…` (packet), `c23b0ab532cf…` (projection), `d581e0ad5384…` (typed), `e6ae9828d6c8…` (holds), `ed7093d6b921…` (component 04) | **is** the read set — filed, and `--freeze` forbidden |

Negative results — measured, not assumed. `grep -rln <live-digest>` over the whole tree
excluding `.git/`, `.scratch/`, `__pycache__/`:

- `aac91246cede…` (packet) appears in **1** non-filed, non-frozen file in `tools/`:
  `tools/gates/expected/register-law-gate/r30-post/expected.json`. Plus
  `tools/gates/typed-pipelines.json` (S1). Nothing else live.
- `c23b0ab532cf…` (projection) appears in **1** live `tools/` file:
  `tools/gates/typed-pipelines.json`. Nothing else.
- `d581e0ad5384…` (typed packet) appears in **0** live `tools/` files.
- `e6ae9828d6c8…` (holds) appears in `tools/gates/typed-pipelines.json` and the two
  r7/`expected.json` rows. Nothing else.
- `c0d77181ac56…` (component 13) appears in `packet.d4.yml`, `packet.d4.typed.yml` and
  the mirrored `r30-post/packet.d4.yml` — **never** in `tools/exercise-handoff-e2e.py`.
- `tools/assemble-culture-d4.py` carries **no** digest literal; it *generates*
  `assembly.source_sha256`. `tools/gates/argot-derivation-gate.py` and
  `tools/gates/register-law-gate.py` carry no D4 digest either — both print the *naming
  gate's* digest as a dependency line and grade packet content.

## 2. Falsification by mutation — the isolated copy

Copy: `git archive ce103bf | tar -x -C .scratch/d08-iso` (69 MB). Byte-integrity of the
copy against the lane was verified for all eight artifacts I touched or read
(`packet.d4.yml` `aac91246cede`, `typed-labels.d4.yml` `c23b0ab532cf`,
`packet.d4.typed.yml` `d581e0ad5384`, `expected-holds.json` `e6ae9828d6c8`,
`04-lexicon.yml` `ed7093d6b921`, `13-register-law.yml` `c0d77181ac56`,
`exercise-handoff-e2e.py` `bfe1c78e479f`, `typed-pipelines.json` `76ecdfdcbf09` — 8/8 OK).
Every mutation was reverted and re-verified byte-identical (`restored: True`).

### 2.1 Baseline — every leg green in the copy

| leg | command | result | exit |
|---|---|---|---|
| B-1 | `assemble-culture-d4.py --check` | `byte-identical deterministic assembly` | 0 |
| B-2 | `gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | `records=187 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0` | 0 |
| B-3 | `gates/register-law-gate.py examples/culture-d4/packet.d4.yml` | `law_rows=5 identity_rows=8 record_ids=183 registers=17 … dangling=0 findings=0` | 0 |
| B-4 | `gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | `summary: 20/20 legs passed` | 0 |
| B-5 | `check-gate-battery.py` | `{battery_exit: 0, fail: 0, pass: 7, unevaluable: 0}` | 0 |
| B-6 | `exercise-handoff-e2e.py --profile v3 --quiet` | `packet_sha256=45f5713261762a95…` | 0 |

### 2.2 M1 — append one comment line to `13-register-law.yml` (NOT a read-set member)

| leg | result | exit |
|---|---|---|
| `assemble-culture-d4.py --check` | `packet.d4.yml differs from deterministic assembly` | **1** |
| `gates/d4-assembly-check-gate.py examples/culture-d4/packet.d4.yml` | `differs from the deterministic assembly` | **1** |
| `gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | `FAIL L1-assembler: packet bytes aac91246cede are not tools/assemble-culture-d4.py's deterministic assembly (5ef3cf77ad37)` | **2** |
| `gates/argot-derivation-gate.py` | `violations=0 rule_holds=0` — **green** | 0 |
| `gates/register-law-gate.py` | `findings=0` — **green** | 0 |
| `check-gate-battery.py` | `{pass: 7, fail: 0, unevaluable: 0}` — **green** | 0 |

### 2.3 M2 — one new register record into `04-lexicon.yml` (a read-set member) + rebuild

Component 04 `ed7093d6b921…` → `0e3cd5d0443d…`; packet `aac91246cede…` → `fb6226f77e0d…`.

| leg | result | exit |
|---|---|---|
| `assemble-culture-d4.py --check` | `byte-identical deterministic assembly` (rebuild re-synced) | 0 |
| `gates/d4-assembly-check-gate.py` | `byte-identical deterministic assembly` | 0 |
| `gates/d4-typed-labels-check-gate.py examples/culture-d4/typed-labels.d4.yml` | `differs from the deterministic projection` | **1** |
| `gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | `FAIL L1-profile: packet: pins aac91246cede, live fb6226f77e0d` | **2** |
| `gates/argot-derivation-gate.py` | `records=188 … violations=0 rule_holds=0` — **green** | 0 |
| `gates/register-law-gate.py` | `law_rows=5 identity_rows=9 record_ids=184 … findings=0` — **green** | 0 |
| `exercise-handoff-e2e.py --profile v3 --quiet` | `E2E-DIGEST: exa…` (exit 1, truncated tail) | **1** |
| `exercise-handoff-e2e.py --profile v3 --freeze .scratch/d08-freeze-probe` | `could not freeze: E2E-DIGEST examples/culture-d4/typed-labels.d4.yml assembly.packet_sha256: the tree recorded aac91246cede… but the bytes measure fb6226f77e0d…` | **1** |

**The freeze path itself refuses** — so a stale projection cannot be laundered into a
frozen row by running `--freeze` first. That is the fail-closed property the cascade needs.

### 2.4 M3 — add `13-register-law.yml` to `D4_COMPONENTS` (`tools/exercise-handoff-e2e.py:157-170`)

The `V3_READ_SET` spread is `:1953` (`*D4_COMPONENTS`); `:2577` iterates it;
`:3608` labels it `{rel: f"A-{i:02d}" for i, rel in enumerate(V3_READ_SET, start=1)}`.
Appending one member (12 → 13) and freezing to a scratch dir:

```
baseline packet_sha256: 45f5713261762a95      baseline input members: 58
freeze exit 0  read set: 59 files; component digests 26/26; d4 pins 8/8
new packet_sha256: 7f0e47909a77ad7f          members: 59
packet digest MOVED: True
twin_sha256   0e22913850cd -> 9ad1f6db8073   MOVED
counts equal: True    links equal: True    uncertainty equal: True
field_digests differing: ['artifact_manifest', 'validation']
added member: {'examples/culture-d4/components/13-register-law.yml'}
```

No D4 byte changed, yet the packet digest moved. Cause, measured on the frozen
`packet.md`: the `A-NN` label is positional, so **every later member shifts by one** —

| label | r7 row (58 members) | M3 row (59 members) |
|---|---|---|
| `A-45` | `components/12-provenance.yml` | `components/12-provenance.yml` (unchanged) |
| `A-46` | `tools/assemble-culture-d4.py` | **`components/13-register-law.yml`** |
| `A-57` | `reports/round-34/handoff/declared-in-r7/claims-map.md` | **`tools/harness/packet_links.py`** |
| `A-58` | `reports/round-19/validation.json` | **`claims-map.md`** |

Also measured in M3: `--profile v3 --quiet` → exit 1, `E2E-DIGEST: the assembled packet
does not match the frozen packet digest`; `--profile v3 --selftest` → exit 0.

### 2.5 M4 — replay every committed manifest, pristine vs. after a D4 edit

Every `MANIFEST.tsv` in the tree, run in the copy before and after the M1 mutation:

| manifest | pristine | after M1 | reading |
|---|---|---|---|
| `reports/round-31/sweep/frozen/r31-post/MANIFEST.tsv` | **0** (4/4 reproduced) | **1** (3 mismatch, 1 reproduced) | **the only manifest the landing invalidates** |
| `tools/gates/frozen/round-26/post-register/MANIFEST.tsv` | 1 (2 mismatch, 4 reproduced) | 1 (2 mismatch, 4 reproduced) | **already red at pristine** — pre-filed superseded |
| `tools/gates/frozen/round-18/MANIFEST.tsv` | 1 (2 mismatch, 0 reproduced) | 1 | already red at pristine |
| `reports/round-27/pinsweep/frozen/r27-post/MANIFEST.tsv` | 1 (2 mismatch) | 1 | already red at pristine |
| `reports/round-28/pinsweep/frozen/r28-post/MANIFEST.tsv` | 1 (4 mismatch) | 1 | already red at pristine |
| `tools/gates/frozen/round-3/MANIFEST.tsv` | 2 (7 could-not-evaluate) | 2 | already could-not-evaluate |
| `tools/gates/frozen/round-11/MANIFEST.tsv` | 2 (1 c-n-e, 10 reproduced) | 2 | already could-not-evaluate |
| `reports/round-17/tests/frozen/MANIFEST.tsv` | 0 (5/5) | 0 (5/5) | D4-neutral |

## 3. Reconciliation against the sibling lists — and against D04, which landed mid-write

**D04 landed at 06:34 while I was writing §1–§4.** It is `reports/round-36/depth/D04-repin.md`,
603 lines. §3.0 below is the verification of that object — the criterion my mission names —
run against the census in §1 and the matrix in §2. §3.1–§3.2 are the reconciliation against
the three sibling lists that existed before it.

### 3.0 Verification of `depth/D04-repin.md` — row-by-row against my census

D04's §5 gives a **10-row** set. Mapping each to my §1 census and to my §2 mutation evidence:

| D04 row | D04 surface | my census | my mutation evidence | verdict |
|---|---|---|---|---|
| 1–4 | `components/04-lexicon.yml` + the three generated artifacts | S3/S4/S5 (+ the source) | M2 moved packet `aac91246cede` → `fb6226f77e0d`, projection stale | **confirmed** |
| 5 | `expected-holds.json` new `pin_generations` row + 2 pointers | S2 | §2.3 (`FAIL L1-profile` names it) | **confirmed** |
| 6 | `typed-pipelines.json` new first-match generation | S1 | §2.3 `FAIL L1-profile: packet: pins aac91246cede, live fb6226f77e0d` | **confirmed** |
| 7 | `declared-in-r7/expected.json` successor | S9 | §2.3 `E2E-DIGEST`, §2.4 the 59-member freeze | **confirmed** |
| 8 | `declared-in-r7/twin.json` successor | S9 | §2.4 `twin_sha256 0e22913850cd → 9ad1f6db8073` | **confirmed** |
| 9 | `tools/exercise-handoff-e2e.py:1937-1938` default pair | S9 (as the pointer *to* S9) | §2.4 (the re-point moves the packet digest) | **confirmed** |
| 10 | `reports/round-31/sweep/frozen/r31-post/MANIFEST.tsv` successor generation | §2.5 | §2.5: pristine 4/4 → 3 mismatch, 1 reproduced | **confirmed** |

**Completeness: PASS against my census** — every one of my nine pin surfaces appears in
D04's list or in its §4 negative table, and D04's list contains no surface my census did not
find. Two of D04's independent measurements I re-derived rather than accepted:

- **D04 §4's mirror claim is exact.** `tools/gates/expected/d4-assembly-check-gate/r19-pre/expected.json`
  pins `packet.d4.yml` = `e7ecd2045ef0e5f9823c…` **and** the mirrored copy
  `…/r19-pre/packet.d4.yml` exists with that same digest (`e7ecd2045ef0e5f9823c…`), while the
  live packet is `aac91246cede…`. Same for `…/r19-pre/examples/culture-d4/components/01-brief.yml`
  = `a2bc3111b8e936d2…` against live `a1e532ad05a9ee2b…`. So D04 is right: these rows grade
  their **own snapshot**, the battery resolves them inside the baseline directory, and their
  staleness predates the landing. This independently confirms my F3 by a second mechanism
  (`check-gate-battery.py:568-583`: `target = base_dir / relative`, falling back to
  `gates_dir`/`repo_root` only if absent — the mirror wins).
- **D04's five-moving-members count is right and D02's four is short by one.** D04 §3.4
  reports `E2E-DIGEST: 5 read-set file(s) changed`. D02 §6 lists 4. The fifth is
  `examples/culture-d4/components/04-lexicon.yml` — the *source* component, which **is** an
  r7 member (`expected.json:149` = `ed7093d6b92111c2…`) and which the landing edits. D02's
  comparison script evidently compared only generated artifacts; D04's is correct.

**One material omission, and it is my F1.** `grep -c "D4_COMPONENTS"` over D04 → **0**;
`grep -n "D4_COMPONENTS\|A-NN\|renumber"` → **0 hits**. D04's list does not carry the
`A-NN` renumbering row that §2.4 measures. D04 cannot be faulted for leaving out a surface
no sibling named, but the gap is real and my §4 F1 is its evidence.

**One count I could not reproduce, then did — and D04 is right.** D04 §4 says
`examples/culture-d4/ASSEMBLY.md` §5 has **4** stale rows at HEAD (01-brief, 03-orthography,
04-lexicon, 09-costumes). My first parse found **1**, and I nearly filed that as a
discrepancy. It was my parser, not D04: the §5 table writes component rows with
**component-relative** paths (`| \`components/01-brief.yml\` | … |`, `ASSEMBLY.md:93-105`),
which resolve against `examples/culture-d4/`, while `packet.d4.yml` and
`tools/assemble-culture-d4.py` are repo-relative. Resolving both shapes gives **14 rows, 6
stale, 8 fresh**:

```
STALE examples/culture-d4/packet.d4.yml        2776d85cb2b3 -> aac91246cede
STALE tools/assemble-culture-d4.py             03a0754eec55 -> 943f487ba991
STALE components/01-brief.yml                  a2bc3111b8e9 -> a1e532ad05a9
STALE components/03-orthography.yml            de1820b0c115 -> 0f2ff45439fd
STALE components/04-lexicon.yml                74c2561b7c87 -> ed7093d6b921
STALE components/09-costumes.yml               82fb92ad1784 -> f61cc6845518
```

D04 named the four **component** rows (it excludes the packet and the assembler, which its
§4 row-1/row-2 already own). **D04's count is confirmed on its own scope**, and my §3.0
earlier "1 row" figure was a parse artifact. Recorded here rather than quietly corrected —
this is the second time in this round that a seat's negative claim looked wrong and was
right (compare D04 §4's mirror mechanism, which I re-derived above). The §5 table is stale
at HEAD and **stays** stale through the landing, because it is an r7 read-set member whose
bytes the landing does not move; the four component rows and the packet row all move under
the landing, so a *rebuild* of the table would add rows, not fix them. No machine check
reads it (D04 §4, `to-verify`, and my own sweep agrees — `grep` over `tools/` for
`ASSEMBLY.md` finds no digest comparison).

**D04's `r31-post` row matches my §2.5 narrowing** (§2.5: only that manifest is
clean-before/red-after). D04 §3.6 gives 4/4 → 4 mismatch for its landed copy; my M1 mutation
gives 4/4 → 3 mismatch, 1 reproduced — a *different* mutation (M1 changes a component without
re-assembling, so `typed-pipeline-gate` still reports `L1-assembler` for one row), so the
reproduced count differs while the "invalidated" verdict agrees.

### 3.1 Reconciliation against P01 / D03 / D02

| surface | P01 §5 | D03 §5 | D02 §6 | my census | verdict |
|---|---|---|---|---|---|
| `typed-pipelines.json` profile | P-1 | row 6 | §6 diff | S1 | **agrees** |
| `expected-holds.json` | P-2 | row 5 | §6 revision_note | S2 | **agrees** |
| `expected/register-law-gate/r30-post` | P-3 | row 7 ("not moved by this rehearsal") | — | S6 | **D03 and D04 agree against P01** — the mirror grades its snapshot (F3) |
| `expected/d4-assembly-check-gate/*` | P-4 | — | — | S7 | **P01 lists it as landing-invalidated; D04 §4 and I both measure it pre-existing-stale** (F3) |
| `expected/d4-typed-labels-check-gate/*` | P-5 | — | — | S8 | same as above |
| `tools/gates/frozen/…` new manifest | P-6 | `r31-post` supersession | — | §2.5 | **agrees, and I narrow it**: only `r31-post` is clean-before/red-after |
| r7 successor row + default re-point | §5.2 | §5 + §6 | §6.1 | S9 | **agrees** |
| `D4_COMPONENTS` 12→13 | §5.3 "cheap hardening, not a defect" | — | §6.1 (read set will not pin component 14) | §2.4 | **DISAGREE** — see F1; **D04 is silent** |
| the packet's own `assembly.source_sha256` block | — | — | — | S3 | **nobody lists it as a *surface to move***; it *is* what makes component 13 transitively covered (D07 §6 measured this) |

Measured at baseline, confirming the "nothing is owed *today*" reading all three seats
reach: `typed-pipelines.json profiles[0]` matches the live bytes on **all five** digests
(`packet`, `projection`, `adapter`, `expected`, `assembler` — 5/5 OK); `profiles[1]` is the
superseded `round-28` predecessor whose three stale pins (`543d68a82640…`,
`339bfd83bf66…`, `65f5a03e092f…`) are **inert** because profile matching is first-match
(`typed-pipelines.json` `note`: "Profile matching is first-match by the packet's declared
assembler"). So D05's A-5 reading is correct, and D04 must not "repair" `profiles[1]`.

## 4. Findings

**F1 (material — `D4_COMPONENTS` is a read-set member, not a cheap hardening).**
P01 §5.3 (`plan/P01-d-plan.md:306-310`) prices adding component 13 to `D4_COMPONENTS`
(`tools/exercise-handoff-e2e.py:157-170`) as "a cheap hardening, not a defect". §2.4
falsifies the price: the spread at `:1953` puts it **inside** `V3_READ_SET`, and the
positional `A-NN` labelling at `:3608` renumbers every later member, moving the packet
digest `45f57132…` → `7f0e4790…`, the twin `0e22913850cd…` → `9ad1f6db8073…`, and the
`artifact_manifest` + `validation` field digests — with **no D4 byte changed**. A
successor freeze plus a new default-pointer row is the *minimum*; the roster change is
not free and must not be bundled into a content landing without its own row. It is also
**not required**: D07 §6 measured that component 13 is already covered transitively
through S3, so both a member and a non-member edit redden the chain. My verdict: the
change is legitimate hardening, but D04's list must carry it as a *separate* row with the
renumbering named, or drop it.

**F2 (material — the battery does not red on a D4 move).** §2.2 and the `check-gate-battery`
row of §2.3 both report `{pass: 7, fail: 0, unevaluable: 0}` **after** the mutation.
Reading the battery's own JSON, the five D4/law baselines stay
`reading: "pinned"`, `findings: []`, `verdict_replay: "not-run: digests and pins verified
only"`, and `stdout_pin.reading: "run.log absent"`. So `check-gate-battery.py` verifies
*pin schema and gate digests*, not verdict replay, and its green is **not** evidence that
a D4 landing is safe. P01's P-3/P-4/P-5 rows imply the battery would catch a stale pin;
it does not. The legs that actually catch a D4 move are the four named in §2.2/§2.3 plus
`replay-frozen`. D04 must not cite a green battery as the cascade control.

**F3 (material — the `expected/` rows P01 lists are stale already, before any landing).**
P01 P-4/P-5 name `tools/gates/expected/d4-assembly-check-gate/r19-pre` and the three
`d4-typed-labels-check-gate` rows. Measured: all four pin the **pre-family-clean** packet
`e7ecd2045ef0…` (S7/S8 `:29`/`:20`/`:18`/`:15`), while the live packet is `aac91246cede…`
— i.e. they have been stale since the r20/r22 family-clean builds. They are pinned-schema
rows with `run.log absent`, so the battery reads them `pinned` and the staleness is
invisible (F2). Carrying them in D04's list as "invalidated by this landing" would
misattribute a pre-existing condition; they belong in a *hardening* row, not a
content-change row.

**F4 (finding — the freeze path fails closed, and that is a control D04 can cite).**
§2.3: `--freeze` on a tree with a stale projection refuses with
`E2E-DIGEST … assembly.packet_sha256: the tree recorded aac91246cede… but the bytes
measure fb6226f77e0d…`, exit 1. So the cascade order ("re-freeze must follow the re-point
edit, never precede it", P01 §5.4) is **enforced by the tool**, not merely recommended.
The corollary D04 needs: after any D4 content landing, `--freeze` cannot succeed until
`typed-labels.d4.yml` has been re-emitted from the new packet.

**F5 (finding — `typed-pipelines.json` has a two-pass self-reference, and D03 measured
convergence by luck).** D03 §5 reports the loop "happened to converge in pass 1" on their
draft but names the two-pass hazard. My §1 S1 reading confirms the mechanism: the profile
pins `expected.sha256`, and `expected-holds.json` is *itself* one of the artifacts the
landing rewrites, so editing it moves its own digest. D04's list must include the
re-measure step after writing `expected-holds.json`, not just the three pin values.

**F6 (finding — the r7 read set does not pin components 13 or 14, and will not).**
Measured on `reports/round-34/handoff/declared-in-r7/expected.json#inputs`: 58 members,
23 of them D4-related, of which exactly **12** are components (`01`…`12`);
`13-register-law.yml` → `False`, `14-register-forms.yml` → `False`. So D02's new component
14 (§3) and the existing component 13 are covered only through S3/S4. Any D04 list that
claims "component N is pinned by the read set" is wrong; the correct statement is
"covered transitively via the packet's `assembly.source_sha256`" (D07 §6).

**F7 (verifier-side negative — two legs are insensitive to the pin surface, by design).**
`argot-derivation-gate.py` and `register-law-gate.py` stayed green in **both** mutations
(§2.2, §2.3). They grade packet *content*, not pins; their green says nothing about the
cascade. Conversely, `typed-pipeline-gate.py` is the only single leg that reddens on both
M1 (exit 2, `L1-assembler`) and M2 (exit 2, `L1-profile`) — it is the cheapest
whole-cascade control D04 can cite.

**F8 (material, live, not mine — a filed round-35 byte is mutated on disk while I write).**
`git status --porcelain` during my final integrity check returned
` M reports/round-35/validation.json` — a **filed** round-1..35 path, outside my write
scope and outside every D seat's. Measured:

| reading | value |
|---|---|
| live `sha256sum reports/round-35/validation.json` | `8a40245dcecff27b42b9900abc2623b5fda5531e09a8bf7cc39587d4853d1113` |
| `git show HEAD:reports/round-35/validation.json \| sha256sum` | `328e97b39eff69f45cb23801861ad2e345f8e7b3f7ae5555f1465e8d2c472124` |
| live mtime | `2026-10-19 06:33:23.612 -0300` |
| diff shape | `measured_at_utc` bumped `06:19:14.685566 → 06:33:23.601283`; `cross/X1-X3.measurement` emptied from the `pending-by-construction` string to `{}` |

This is the **second** occurrence of the same class in this round's window: Ca02
(`calib/Ca02-recount-35.md:88-115`) filed an identical runner-shaped rewrite of the same
file at `06:29:35 → 06:29:59`, naming the mechanism — `reports/round-35/run-validation.py`
writes `out_path = f"{ROUND}/validation.json"` **cwd-relative** while `ROOT`/`os.chdir`
pin the live tree, so a sibling seat invoking a round runner with the live repo as cwd
publishes over the filed receipt. Ca02 recorded **zero** DIFF rows at 06:30; at 06:33 the
file is dirty again. **The r35 receipt was clean in between and is dirty now**, so the
event is recurring, not historical. Writer identity is `to-verify` — not provable from my
evidence, and I did not attempt to attribute it. **I wrote nothing to that path**: my only
in-tree write is `reports/round-36/depth/D08-verify-repin.md`, and the isolation of my
mutation work is controlled by `.scratch/d08-iso` being a `git archive` extract whose eight
artifacts I re-verified byte-identical to the lane (8/8 OK) after every probe. Carried to
the integrator: this is a live F-C13-1-class hazard that the D block's re-pin work will run
straight through, since the cascade touches `reports/round-31/…` and `reports/round-34/…`
manifest and handoff bytes.

## 5. What I could not verify

- **D04's `§2` digest values.** D04 §7 says so itself: "The digest values in §2–§3 are this
  seat's copy's values, not transferable" — six different packet digests for one landing
  across five seats. I verified D04's **row set and ordering**, not its digest literals, and
  D04 does not ask otherwise. The integrator re-measures on landed bytes.
- **Whether the integrator lands D01's Draft 1 or Draft 2** (D03 §4.4: both grade
  identically; the row shape is an open either/or). The *set* of surfaces in §1 is
  invariant across both — only the digest values differ — so this does not affect the
  census, only the after-values.
- **D03's `0f0828731366ce52`** for component 04: D07 §3 reports it as non-reproducible
  (likely a prose typo). I did not re-measure it; my own M2 mutation produced
  `0e3cd5d0443d…` from a different edit, so neither figure confirms the other.
  `to-verify` against D01 §5.1's actual applied bytes.

## Owed

1. **The `A-NN` renumbering row (F1) — D04's one material omission, and it has no owner.**
   Verified at §3.0: `grep -c "D4_COMPONENTS"` over `depth/D04-repin.md` → **0**. P01 §5.3
   prices the roster change as "cheap hardening", D02 §6.1 raises the read-set question, R03
   assigns the re-point drafts to D04 — nobody owns "does the roster change get its own row".
   For the integrator: either add it as a separate row with the `A-NN` renumbering named, or
   drop it (it is not required — §4 F1, D07 §6).
2. **`reports/round-36/depth/D07-verify.md`'s independence claim** — D07 and I both ran
   isolated copies (`.scratch/d07-*` and `.scratch/d08-iso`) from the same `ce103bf`; two
   copies is not two archives. A third seat rebuilding from a different baseline reference
   would be the stronger control.
3. **The recurring filed-byte rewrite (F8) needs an owner.** `reports/round-35/validation.json`
   is dirty in the worktree at my write time (`8a40245dcecf…` vs HEAD `328e97b39eff…`), the
   second occurrence in this round's window — D04 §7 saw the same file dirty and
   `reports/round-34/validation.json` earlier. Writer `to-verify`; the fix is a runner-side
   cwd guard or the integrator's `receipt_guard` (the r35 runner's `out_path` is
   cwd-relative, `reports/round-35/run-validation.py:502`). Not mine to repair — filed
   bytes are outside every seat's write scope, and Ca02 already owns the evidence.
4. **`examples/culture-d4/ASSEMBLY.md` §5 stale-row count (§3.0) — resolved, D04 confirmed.**
   D04 reports 4 stale rows; my first parse found 1 because the component rows are
   **component-relative** paths. Re-parsed: 14 rows, 6 stale (the 4 components D04 names plus
   the packet and the assembler, which D04's §4 already owns elsewhere). D04's count is
   correct on its scope; no `to-verify` remains on this. The table is stale at HEAD and no
   machine check reads it (both seats swept; `to-verify` on that negative stands).
5. **D03's `0f0828731366ce52`** for component 04 remains unreproduced (D07 §3 also failed to
   reproduce it). My own M2 mutation produced `0e3cd5d0443d…` from a *different* edit, so
   neither figure confirms the other. `to-verify` against D01 §5.1's actual applied bytes.

## Citations

- `reports/round-36/claims.json` (claim D `before`/`after_required`); `reports/round-36/targets.json` (D08 mission, `shared_rules`); `REGIMEN.md` (regimen-2 per-round contract).
- `tools/exercise-handoff-e2e.py:157-170` (`D4_COMPONENTS`), `:171-176` (`D4_ASSEMBLER`/`D4_TYPED_*`/`D4_RECEIPTS`), `:188` (`CLAIMS_MAP`), `:1937-1938` (`V3_BASELINE_DEFAULT`/`V3_FROZEN_DIR_DEFAULT`), `:1939-1962` (`V3_READ_SET`), `:1953` (`*D4_COMPONENTS`), `:2577`, `:3608` (`A-NN` labelling), `:3820-3836` (the r35 `E2E-READSET` guard).
- `tools/gates/typed-pipelines.json:6-38` (profile 0), `:41-65` (profile 1, superseded predecessor).
- `examples/culture-d4/expected-holds.json:3-6,22-26,34-44`; `examples/culture-d4/packet.d4.yml:2864-2889` (`assembly` incl. `source_sha256` → `:2888` component 13); `examples/culture-d4/typed-labels.d4.yml:9`; `examples/culture-d4/packet.d4.typed.yml` (`assembly` block).
- `tools/gates/expected/register-law-gate/r30-post/expected.json:10,19-20`; `tools/gates/expected/d4-assembly-check-gate/r19-pre/expected.json:18-31` + `freeze.txt`; `tools/gates/expected/d4-typed-labels-check-gate/{r19-pre:20,r20-post:18,r22-post:15}/expected.json`.
- `reports/round-34/handoff/declared-in-r7/expected.json:144-161` (the 19 D4 members of the 58), `freeze.txt:2`; `reports/round-34/handoff/repin.json` (the re-point-as-new-row precedent, rows `R34-D-default-pointer`/`R34-D-stale-row`).
- `reports/round-36/depth/D04-repin.md` (603 lines, landed 06:34 mid-write) — §1 (three isolated copies), §3.1–§3.6 (the six re-freeze rows), §3.4 (`E2E-DIGEST: 5 read-set file(s) changed`), §4 (the 8 negative surfaces incl. the mirror mechanism and the `ASSEMBLY.md` count), §5 (the 10-row set + ordering), §6 (post-landing leg state), §7 (the filed-byte note).
- `reports/round-36/plan/P01-d-plan.md:279-311` (§5 P-1…P-6, §5.2 freeze prohibition, §5.3 component 13, §5.4 cascade order); `reports/round-36/depth/D02-packet-draft.md:322-364` (§6 cascade + §6.1 freeze question); `reports/round-36/depth/D03-isolated-verify.md:325-380` (§5 pin cascade, two-pass hazard, `r31-post` supersession); `reports/round-36/depth/D07-verify.md:118-215` (§4 baseline legs, §6 the read-set/component-13 control); `reports/round-36/depth/D05-receipt.md:243-279` (A-5 reading); `reports/round-36/depth/D10-scribe.md:72,174` (D04 owed); `reports/round-36/calib/Ca02-recount-35.md:88-115` (the first filed-byte incident).
- `tools/check-gate-battery.py:568-583` (`target = base_dir / relative`, the mirror-first resolution that makes D04 §4's claim exact) and its JSON `baselines[].{reading,inputs_checked,stdout_pin}`.
- Commands: `git rev-parse HEAD` → `ce103bf5885af00023cdc4a174c17602476cdcf8`; `git archive ce103bf | tar -x -C .scratch/d08-iso`; the per-leg runs in §2.1–§2.5, all from `.scratch/d08-iso` with `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`; `sha256sum` over the eight artifacts (8/8 OK vs. the lane); `git show HEAD:reports/round-35/validation.json | sha256sum` (F8).
- Prior art: `reports/round-26/register/repin.json` (the re-pin-as-new-row shape), `reports/round-27/pinsweep/d4-pins.json`, `SCORECARD.md:330` (the self-referential tool-pin subtlety), `reports/round-29/defects/regression.md:52` (superseded, never rewritten).
