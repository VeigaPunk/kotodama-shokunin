# R28-D21 — capability-row draft: the register law's replay leg

- round: 28 (operator: loop 3 of 3, **build round 4 of 4 — the last build round**;
  64 declared workers, `devin/deepseek-v4-1-flash-high`). Seat **R28-D21**
  (D-scribe 1 of 4).
- claim under draft: `reports/round-28/claims.json` claim **D**, axis `depth`,
  capability `register-law-replay`.
- date: 2026-10-18. Declared baseline `6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede`
  (the round-27 admit). Lane HEAD at this seat's final stamp
  `69cecbc7dcf575a29f29660ecac470e05260fd86` (the round-28 declaration).
- **final stamp 2026-10-18T20:15:52Z; post-stamp drift to 20:19:59Z recorded in
  §0a.** The tree moved **once** inside this seat's measurement window (the RL-4
  `packet_keys` fix, ~20:13Z, which moved the D4 packet `86079a67…` → `543d68a8…`
  and the projection `88a94422…` → `339bfd83…`), and **twice more after it** (the
  O seats' `r28-post` freeze at 20:17:09Z, the C seats' ceiling amendment at
  20:19:39Z). §1–§5 bind to the 20:15:52Z stamp; §0a and §6 record the later
  readings explicitly rather than rewriting the earlier ones.
- **status: DRAFT ONLY — the orchestrator admits.** This seat edits no
  `SCORECARD.md`, no `SKILL.md`, no `LOG.md`, no tool, gate, example, component or
  packet. Everything below is proposed text plus read-only receipts.
- writes: this file only, plus gitignored scratch under `.scratch/`
  (`export TMPDIR=$PWD/.scratch` preceded every scratch-writing command; the
  frozen replays need `TMPDIR` **outside** the repo — §5a). No commit, no push.
  No filed artifact of rounds 8–27 was modified.
- canon: **NON-CANON engineering evidence.** A capability row records a
  demonstrated run; it is not canon, not lore acceptance, not a clearance and not
  a real-world register claim.

## 0. Verdict — and the claim's own runner now grades it PASS

**The register law's replay leg landed at 20:20:4xZ, after this seat's stamp, and
this seat verified it independently. The claim's `after_required` is now met on
every leg it names, and `python3 reports/round-28/run-validation.py` reads
`claim D: PASS`.** The two readings below are kept side by side: what this seat
measured at its own stamp (**no leg**), and what it measured on re-run once the
gate landed (**the leg works, six tamper routes caught by name**). A draft that
showed only the second would hide the round's most useful fact — that the gap was
real for the whole build window and closed at the wire.

| # | `after_required` leg (`claims.json:15`) | at this seat's stamp | on re-run (20:22:38Z) | evidence |
|---|---|---|---|---|
| 1 | **the law gains a replay/checking leg** — speaker classes resolve against delivered records, forces against a declared vocabulary, consequences against the roll/rank machinery | **NOT MET** | **MET** | **`tools/gates/register-law-gate.py`** landed (`cfbff16b…` when this seat measured it; **`bbad3578…` at 20:31Z** — the gate was still being refined, `--selftest` **33/33** at both stamps, so **re-hash rather than quote either**) with eight named finding ids (`D4L-LAW-DATA/ROW/SPEAKER/FORCE/CONSEQUENCE/REGISTER/AXIS/KIND/DANGLING/COVERAGE`). On the clean packet: `coverage: law_rows=5 identity_rows=4 record_ids=179 registers=9 speaker_tokens=3 force_failures=0 consequence_failures=0 dangling=4 findings=4`, exit 1 (the four `DANGLING` holds are real: `RGL-01..03` name `QREG-05..08`, design rows that never landed as packet records). §2 |
| 2 | **a tampered row is a named finding (`D4L-LAW-*` class)** | **NOT MET** (0 emitted) | **MET — 6 of 6 field routes caught by name; 12 of 14 routes name the row** | block-scoped tampers of the first law row: `force` → `D4L-LAW-FORCE`, `speaker` → `D4L-LAW-SPEAKER`, `consequence` → `D4L-LAW-CONSEQUENCE`, `register` → `D4L-LAW-REGISTER`, `axis` → `D4L-LAW-AXIS`, `kind` → `D4L-LAW-KIND`. `--selftest` **33/33**. The round's own X54 spot-check reads **0/14** — a **false negative** from an output-format mismatch, controlled in §2.6 |
| 3 | **RL-4 fixed** — the components declare `packet_keys` | **MET** | MET | `03-orthography.yml:24` declares `packet_keys: [orthography, records, literacy_institutions]` (`0f2ff454…`); `09-costumes.yml:22` adds `enforcement` (`f61cc684…`). §1 |
| 4 | **the records reach the packet** | **MET** | MET | all eight ids `OR-01..03`, `LI-01..03`, `EN-01..02` resolve as **packet records** (round 27: `LI-*`/`EN-*` were 0). Three new list blocks: `enforcement:` (2), `literacy_institutions:` (3), `records:` (3). Argot census `records=175` → **`183`**; the law gate's own reader counts `record_ids=179`. §1 |
| 5 | **the named-holds set updated honestly** | **PARTLY MET** (counts right, pin stale) | **MET** | `expected-holds.json` was **re-pinned** (`857417e9…` → **`65f5a03e…`**); its `packet_sha256` now equals the live `543d68a8…`, and the counts are **12/0/0 unchanged** — the honest reading, since the new blocks add records, not forms. §4 |
| 6 | **the D4 typed gate + argot gate + assemblers green** | **MIXED** (typed gate exit 2 on a stale pin) | **MET — all green** | `typed-pipeline-gate.py` **`summary: 20/20 legs passed`, exit 0**; `tools/gates/typed-pipelines.json` re-pinned (`packet 543d68a8… OK`, `projection 339bfd83… OK`, `expected 65f5a03e… OK`); argot gate exit 0; `assemble-culture-d4.py --check` byte-identical and `--selftest` 81/81; both D4 adapter gates exit 0, stdout byte-identical to every earlier row; battery `pass 7 / fail 0 / coverage 9/9`. §5 |
| 7 | **the RL-3 ceiling recorded as a design constraint in the knowledge entry** | **NOT MET** | **MET** | 20:19:39Z `## 13. Amendment (round 28)` landed (313 → **436 lines**, 12 → **13** `##` headings, all twelve earlier headings present); 20:20:06Z `corpus/knowledge/linguistics/register-lexicon-ceilings.md` landed (287 lines, gap-named, external sources with calibration; directory **20 → 21**); 20:20:23Z `corpus/README.md` **revision 1.9** reconciled it (`:138` index row, `Total knowledge entries: 201.`). §6 |

**The claim's own runner confirms it, and by 20:23:02Z the whole round is green:**
`claim D: PASS`, `claim O: PASS`, `claim C: PASS`,
`acceptance_checks_passed: True`. (The O failure recorded in the earlier reading
of this file closed when the O seats landed
`reports/round-28/pinsweep/v3-baseline-r28/` — `--profile v3` now reads **exit 0**,
`fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27`.)

**One sentence for the parent.** Claim D is **delivered and independently
verified**: the law now has a leg that names each tampered clause, RL-4's records
are packet records, and the pins are current. The one thing this seat would flag
is that the leg landed **at the wire** — for the whole build window
`grep -rl "D4L-LAW" tools/` read 0, so any artifact written before 20:20Z
describes a tree without it. **This draft is the artifact that did**, and its §0
keeps both readings for exactly that reason.

## 0a. The landings inside and after this seat's window

A seat that hides its own drift is not a measurement. Six movements, all stamps
UTC, 2026-10-18.

| stamp | what moved | effect on this file |
|---|---|---|
| ~20:13:00 | **the RL-4 `packet_keys` fix lands** (sibling seat) | the packet `86079a67…` → `543d68a8…`; every reading in §1 was taken after this, so the file grades the **post-fix** tree |
| 20:17:09 | **the O seats freeze `reports/round-28/pinsweep/frozen/r28-post/`** | replays **2/2 OK**, and its `MANIFEST.tsv` pins exactly the rows §2.1 of the sibling `frozen-rows.md` proposed — an independent confirmation of the two D4 rows |
| 20:19:39 | **the C seats land `## 13. Amendment (round 28)`** | leg 7 splits from **NOT MET** to **HALF MET**; §6 records each reading |
| 20:20:06 | **the C seats land `register-lexicon-ceilings.md`** | leg 7 → the two entry halves met; directory 20 → 21 |
| 20:20:23 | **`corpus/README.md` reconciled to revision 1.9** | leg 7's last residual closes |
| **20:20:4x** | **the D seats land `tools/gates/register-law-gate.py`** | **legs 1 and 2 flip from NOT MET to MET**; §2 is re-measured against it |
| 20:22:3x | the O seats re-pin `expected-holds.json` (`65f5a03e…`) and `typed-pipelines.json` | leg 5 → MET, leg 6 → all green |
| 20:22:5x | the O seats land `reports/round-28/pinsweep/v3-baseline-r28/` | `--profile v3` exit 0; the round's last red clears |

**What did not move across all of them:** `packet.d4.yml` is still `543d68a8…`
and the RL-4 fix is unchanged. **The law gate reads the packet; it did not require
a packet change, which is the clean shape for a checking leg.**

## 1. RL-4 — the fix, and the reading that proves it

The round-27 finding (`reports/round-27/law/review.md:187`, RL-4) was that two
components' record blocks were legal in the component and invisible to every gate
that reads the packet. Measured **before** the fix at this round's baseline, and
**after** it at the final stamp:

| component | round-27 `packet_keys` | round-28 `packet_keys` | blocks newly merged |
|---|---|---|---|
| `03-orthography.yml` | *(absent — allowlist fallback)* | `[orthography, records, literacy_institutions]` | `records`, `literacy_institutions` |
| `09-costumes.yml` | `[costumes, materials, cloth_sources, rank_rules, form_slots]` | `[… , enforcement]` | `enforcement` |

Measured at the final stamp, from the assembler's own reader (not a re-parse):

```
$ python3 - <<'PY'
import runpy, pathlib
ns = runpy.run_path("tools/assemble-culture-d4.py")
doc = ns["reader_parse"]()(pathlib.Path("examples/culture-d4/packet.d4.yml").read_text())
print({b: len(doc.get(b) or []) for b in ("records","literacy_institutions","enforcement")})
print([r["id"] for r in doc["records"]], [r["id"] for r in doc["literacy_institutions"]],
      [r["id"] for r in doc["enforcement"]])
PY
# {'records': 3, 'literacy_institutions': 3, 'enforcement': 2}
# ['OR-01', 'OR-02', 'OR-03'] ['LI-01', 'LI-02', 'LI-03'] ['EN-01', 'EN-02']
```

**Every one of the eight ids now resolves as a packet record.** Round 27 measured
`LI-01: 0  LI-02: 0  LI-03: 0  EN-01: 0  EN-02: 0` by `grep -c` over the packet;
at this stamp all eight are **≥ 1**, and — the reading that matters — all eight
are carried by a *list block row that has an `id`*, which is what
`packet_record_ids()` (`reports/round-28/run-validation.py:516`, cited by revision
— the runner was still moving at this stamp) treats as ground truth.

**Why this is not cosmetic.** The round-27 law's `RGL-01` names its third speaker
as `mold-keeper (OR-02, component-only)`. Round 27 marked `QREG-07` `to-verify`
precisely because `OR-02` was a byte the gates could not see. At this stamp
`OR-02` is a packet record, so that citation resolves — the RL-4 fix removes a
**dangling citation** in the delivered law, not merely a bookkeeping line. The
round-28 independent instrument agrees: `rl4_keys_ok=2`, `rl4_ids_missing=0`.

**What the fix does *not* do.** It does not add `records`, `literacy_institutions`
or `enforcement` to the assembler's `PACKET_KEYS` or `RECORD_FIELDS` — all three
remain absent (measured: `'records' in ns['RECORD_FIELDS']` → **False**). The
blocks arrive by the **per-file `packet_keys` path**, which the assembler honors
per file (`tools/assemble-culture-d4.py:258-262`; `:258` reads the declaration,
`:262` is the allowlist fallback). That means the assembler's record
validator has **no field list** for them: a row missing an `id` would assemble
rather than refuse. This is the same class as the still-open `L9-HOLD` the round-28
`x59` instrument reports for `register_law`, and §3.1 records it as a named limit
rather than a green leg.

## 2. RL-1 — first measured as open (eight routes, no leg), then re-measured as closed

**Read §2.1 as the round's central negative measurement and §2.5 as its
resolution.** Both are kept: the negative is what the claim's `before` asserts,
and it held for the entire build window.

### 2.0 The state after the gate landed (20:20:4xZ) — the leg works

`tools/gates/register-law-gate.py` resolves each law clause against
the packet's other blocks. It was **`cfbff16b…` when this seat measured it and
`bbad3578…` at 20:31Z** — the D seats kept refining it after it first landed
(`--selftest` **33/33** at both stamps; the independent
`reports/round-28/scribe/x58-d4-chain-cold-rerun.md` records the same drift
independently). **Re-hash before quoting either digest.** Measured
2026-10-18T20:22:38Z:

```
$ python3 tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml
FINDING D4L-LAW-DANGLING: HOLD — RGL-01 design_row names QREG-05, which no delivered record carries …
FINDING D4L-LAW-DANGLING: HOLD — RGL-01 design_row names QREG-07, …
FINDING D4L-LAW-DANGLING: HOLD — RGL-02 design_row names QREG-06, …
FINDING D4L-LAW-DANGLING: HOLD — RGL-03 design_row names QREG-08, …
coverage: … law_rows=5 identity_rows=4 record_ids=179 registers=9 speaker_tokens=3 force_failures=0 consequence_failures=0 dangling=4 findings=4
$ python3 tools/gates/register-law-gate.py --selftest | tail -1
selftest: 33/33 checks passed
```

**The four `DANGLING` holds are a real, named finding, not a defect in the gate.**
`RGL-01..03` carry a `design_row` naming `QREG-05..08` — the four speech-act rows
the round-27 sibling design seats proposed. Those four rows **never landed as
packet records**; the `registers:` block still carries only `QREG-01..04`. So the
law's own cross-reference to its design authority is the one dangling citation
left, and the gate names it per row rather than staying silent. **That is the
distinction the round was missing: a leg that can say "this citation resolves to
nothing" is a leg.**

| tamper route (block-scoped rewrite of the first law row) | new finding id | caught? |
|---|---|---|
| `force` → `"no-such-force"` | `D4L-LAW-FORCE` | **yes** |
| `speaker` → `"nobody (ZZ-99)"` | `D4L-LAW-SPEAKER` | **yes** |
| `consequence` → `"nothing at all"` | `D4L-LAW-CONSEQUENCE` | **yes** |
| `register` → `"zzz"` | `D4L-LAW-REGISTER` | **yes** |
| `axis` → `"zzz"` | `D4L-LAW-AXIS` | **yes** |
| `kind` → `"zzz"` | `D4L-LAW-KIND` | **yes** |

**Six of six field routes are caught, each by a finding that names the clause.**
The gate's own `--selftest` proves three of them itself
(`delivered-force-tamper-adds-a-line`, `-speaker-`, `-consequence-`), so the
negative is established by the delivered artifact and not only by this seat.

**One calibration the gate declares about itself, and this file repeats rather
than launders.** The `force` vocabulary it grades against is the **gate's own
declared closed set**, quoted from the design (`reports/round-27/law/rules.md`
§2's `RU-L2`) — **the packet still declares no `force` vocabulary** (the round-28
`x59` instrument's `L10-HOLD`). So "forces against a declared vocabulary" is met
in the sense that a declared vocabulary exists and is enforced; it is met
**in the gate, not in the packet**. A successor that wants the packet to own its
own vocabulary should read `reports/round-28/law/vocab.md` §4–§5, which prices it.

### 2.1 The route table (this seat's stamp — the round's negative measurement)

Each route rewrites **exactly one value** in the packet's first law row (or
deletes a whole row), in a full-tree clone under `.scratch/`, so the projector
keeps its sibling `components/` and the argot gate its dependency path. "findings"
is the projector's own `findings_total` from its coverage line.

| route | field tampered | packet sha | projector findings | argot exit | `D4L-LAW-*` emitted |
|---|---|---|---:|---:|---|
| **R0** | *(clean control)* | `543d68a8` | **12** | 0 | **0** |
| T-force | `force: "no-such-force"` | `33f4c9ca` | **12** | 0 | **0** |
| T-speaker | `speaker: "nobody (ZZ-99)"` | `25ef9cdc` | **12** | 0 | **0** |
| T-consequence | `consequence: "no roll, no rank, nothing"` | `eacde010` | **12** | 0 | **0** |
| T-axis | `axis: "zzz"` | `56340004` | **12** | 0 | **0** |
| T-kind | `kind: "zzz"` | `159981e3` | **12** | 0 | **0** |
| T-register | `register: "zzz"` | `413b508d` | **12** | 0 | **0** |
| T-row-deleted | whole `RGL-05` row removed | `cdf69f33` | **exit 2** (`D2L-DATA`) | **2** | **0** |

**Six of the seven routes are invisible.** The clean packet and the six value
tampers are **byte-for-byte identical in every delivered verdict** — same
`findings_total=12`, same finding id (`D2L-FORM-UNRESOLVED`), same argot coverage
line, same exit code. This is round 27's RL-1 reproduced on the post-RL-4 tree:
the RL-4 fix did **not** close it, and the claim's `after_required` treats them as
separate legs, correctly.

**The seventh route is the honest edge.** Deleting a whole row does move things —
but for a **structural** reason, not a law reason: the row deletion left a
duplicate `register:` key, which the reader refuses (`D4L-ARGOT-DATA: duplicate
key 'register'`), collapsing the packet to `records=0`. That is the *reader*
failing closed, not a law checker firing. **A checker that only reacts to a
malformed document has no law leg.**

### 2.2 The pin caveat, stated so no reader is misled

The `typed-pipeline-gate` reacts to *every* one of these routes with the same
`FAIL L1-profile` — but it fires identically on the **clean** packet (`pins
86079a6708a0, live 543d68a82640`), because the profile is stale against the
post-RL-4 bytes. **That is a pin mismatch, not a law finding**, and it is the
reason the pin-bound gate cannot be used as evidence for or against RL-1. The
pin-free instruments (the projector and the argot gate) are the honest ones for a
value tamper, and they are silent.

### 2.3 Independent confirmation

Two other round-28 instruments, built by other seats on different machinery,
measure the same thing:

- `reports/round-28/scribe/x54-law-negatives-spotcheck.py` — 14 tamper routes
  (including whole-row operations, `design_row` and `cite` rewrites) →
  `verdict: delivered_checkers=0 evidence_checkers=3 clean_law_findings=0
  tamper_caught_by_name=0/14 rl1_reproduces=True`.
- `reports/round-28/audit/x59-register-law-negatives.py` → `FINDING L6b-HOLD:
  RL-1 still open at this tree: tampering a law field … did not produce a NEW
  named D4L-LAW-* finding in any delivered instrument (candidates run: 2; named
  findings seen: 0)`, with `named_law_findings=0 law_findings_clean=1
  law_findings_tampered=2`.

Three independent instruments, three agreeing readings, none of them mine alone.

### 2.4 The control that makes the negative meaningful

A negative claim is only as good as the control that shows the machinery *can*
discriminate. Two controls, both positive:

| control | what was broken | verdict |
|---|---|---|
| **C2** | one landed register form's surface (`L-55 tuum` → `xxzz`), breaking its declared `reverse` derivation | projector **12 → 13** findings; **argot gate exit 1** |
| **C1** | the whole `GAR-06` costume row removed | projector **exit 2**; argot **exit 2** (`records=0`) |
| **C3** | a law row's `register: "no-such-register"` | **12** findings — *invisible*, same class as T-register |

**C2 is the load-bearing one.** The delivered machinery demonstrably discriminates
a broken *derivation* — the argot gate fires and the projector's count moves. It
does not discriminate a broken *law*, because no instrument reads the law. The
difference between C2 and C3 is the whole of RL-1.

### 2.6 A NEW finding — the round's own spot-check cannot read the round's own gate

**This is a cross-instrument interface defect, found by this seat while
re-measuring after the gate landed, and it is not in any round artifact's
findings table.**

The gate emits findings in **one** shape; the round's independent spot-check
parses **another**. Measured 2026-10-18T20:24Z:

```
$ python3 tools/gates/register-law-gate.py .scratch/r28-d21/L-force.yml | grep D4L-LAW-FORCE
FINDING D4L-LAW-FORCE: FAIL — RGL-01 force 'no-such-force' names no declared illocutionary class …

$ python3 - <<'PY'
import re
line = "FINDING D4L-LAW-FORCE: FAIL — RGL-01 force …"
X54  = re.compile(r"^FINDING\s+(\S+):\s*\[(\w+)\]\s*(.*)$")   # X54, :101
RUNV = re.compile(r"D4L-LAW-[A-Z][A-Z-]*")                     # run-validation, :160
GT   = re.compile(r"\bD4L-LAW-[A-Z0-9-]+\b")                   # gate-tests, :245
print(bool(X54.match(line)), bool(RUNV.search(line)), bool(GT.search(line)))
PY
False True True
```

**The gate emits `FINDING <id>: <LEVEL> — <message>`; X54's reader requires the
round-27 bracket style `FINDING <id>: [<level>] <message>`.** The optional-bracket
form is not accepted, so X54 extracts **zero** law findings from a gate that is
emitting them, and its verdict reads:

```
verdict: delivered_checkers=1 evidence_checkers=5 clean_law_findings=0 tamper_caught_by_name=0/14 rl1_reproduces=True
```

**`tamper_caught_by_name=0/14` is a false negative, not a measurement.** The
control is a one-character regex change (`\[` → `\[?`, `\]` → `\]?`), applied to a
**copy** under `.scratch/` (no filed byte touched):

```
$ python3 .scratch/r28-d21/x54-probe.py            # unpatched — the control
verdict: delivered_checkers=1 … clean_law_findings=0  tamper_caught_by_name=0/14  rl1_reproduces=True
$ python3 .scratch/r28-d21/x54-probe.py            # with FINDING_RE patched to accept both shapes
verdict: delivered_checkers=1 … clean_law_findings=4  tamper_caught_by_name=12/14 rl1_reproduces=False
```

**The patched reading, which is the true one:** of **14** tamper routes the gate
catches **14** and names the tampered row on **12**. The two it catches without
naming the row are `T-09` and `T-10`/`P-02` — a `consequence` rewrite on `RGL-04`
and `RGL-05`, whose own `force` is the literal `none` (a sound-channel and a
dating constraint, not speech acts), so the gate's consequence clause correctly
does not apply to them. **That is the gate's declared calibration working as
documented, not a miss.**

| instrument | reader | sees the gate's findings? |
|---|---|---|
| `reports/round-28/run-validation.py:160` | `D4L-LAW-[A-Z][A-Z-]*` (loose `search`) | **yes** — this is why `claim D: PASS` is sound |
| `reports/round-28/gate-tests/run-gate-tests.py:245` | `\bD4L-LAW-[A-Z0-9-]+\b` (loose) | **yes** |
| `reports/round-28/scribe/x54-law-negatives-spotcheck.py:101` | `^FINDING\s+(\S+):\s*\[(\w+)\]\s*(.*)$` (strict brackets) | **no** — false negative |

**Why this matters beyond the one instrument.** A round whose acceptance runner
and whose independent spot-check disagree about the same gate's output cannot
report that disagreement as agreement. The claim still passes — `run-validation`
reads loosely and correctly — but **X54's published `0/14` must not be read as
evidence that the gate is silent.** This seat does not edit X54 (another seat's
file); it records the defect, the control, and the corrected count.

## 3. The capability row, in two halves

### 3.1 Landing-ready — the packet surface (the delivered half)

```markdown
| Register-law packet surface | a component declares its own packet contribution with a top-level `packet_keys:` list, and the assembler merges exactly those blocks — so a record block's ids are packet records and not prose cross-references; the declaration names the file's real contribution, not the allowlist's nearest hit | leave a record block to the `PACKET_KEYS` allowlist fallback; cite a component-only id (`OR-02`, `EN-01`) as a law row's authority; widen the packet surface without a declared reason | a legal-in-component record is invisible to every gate that reads the packet: the citation dangles, the id resolves to nothing, and `grep -c` over the packet returns 0 for a row the component carries | `examples/culture-d4/components/03-orthography.yml:24` and `09-costumes.yml:22` (the round-28 declarations); `tools/assemble-culture-d4.py:258-262` (the per-file path; `:262` is the allowlist fallback); measured `reports/round-28/scribe/capability-row.md` §1 |
```

### 3.2 NOT landing-ready — the checking leg (the missing half)

**This row may not be landed.** It is written here so the gap is on the record in
the place a capability row would otherwise claim it:

```markdown
| ~~Register-law replay leg~~ | ~~the law resolves against the delivered tree: every speaker resolves to a delivered record, every force to a declared vocabulary, every consequence to delivered roll/rank machinery; a tampered row is a named `D4L-LAW-*` finding~~ | — | — | **NOT DELIVERED.** At lane HEAD `69cecbc` no instrument emits `D4L-LAW-*`; seven value tampers of the law produce no new finding in any gate (measured `reports/round-28/scribe/capability-row.md` §2). The claim's `after_required` leg 1 is unmet |
```

The three resolutions the claim names, each measured against the delivered tree:

| resolution | what it would check | delivered vocabulary | state |
|---|---|---|---|
| **speaker** | every agent token `Name (ID)` in `speaker`/`holder` resolves to a delivered record | the packet now supplies the records RL-4 was hiding (`OR-02`, `RK-03`, `RK-04`), so the *inputs* now resolve | **inputs ready, no checker** |
| **force** | every `force` value names a declared illocutionary class | **no `force` vocabulary is declared anywhere.** Five distinct `force` strings are in use (`directive-binding for the charge; declarative-naming…`, `commissive-binding refused`, `directive-binding, not-rollable`, `none — a sound-channel constraint…`, `none — a dating constraint…`) and nothing lists what a legal value is | **no vocabulary, no checker** |
| **consequence** | every `consequence` names delivered roll/rank machinery | the packet supplies `rank_rules` (RK-01..04) and the `rite`/`tally`/`roll` strings the consequence texts name | **inputs ready, no checker** |

**The `force` row is the deepest of the three.** The claim asks that forces be
checked "against a declared vocabulary", and the delivered packet declares none —
so a checker written today would have to *invent* the vocabulary it grades
against, which is precisely the failure mode the round-27 design priced as E-4
("the kinds route to `cannot-evaluate` forever"). `reports/round-28/audit/x59`
reports this as `L10-HOLD: the law states 5 distinct force value(s) but the
packet declares no force vocabulary`. **A vocabulary declaration is a prerequisite
of the leg, not a detail of it.**

## 4. The named-holds set — re-pinned is not re-counted

`examples/culture-d4/expected-holds.json` (`857417e9…`, unchanged this round)
still carries `packet_sha256: 86079a67…` — the **pre-RL-4** packet — while the
live packet is `543d68a8…`. Measured:

```
$ python3 -c "import json,hashlib,pathlib; d=json.load(open('examples/culture-d4/expected-holds.json'));
  print(d['packet_sha256'][:12], hashlib.sha256(pathlib.Path('examples/culture-d4/packet.d4.yml').read_bytes()).hexdigest()[:12])"
86079a6708a0 543d68a82640
```

**The counts are right and the pin is stale, and both facts matter.**

- **Right:** `{"hold": 12, "note": 0, "fail": 0}` is the correct answer for the
  post-RL-4 tree. The three new blocks add **records, not forms** — no `OR`, `LI`
  or `EN` row obliges a surface form, so the twelve garment-form obligations still
  route to their twelve record/slot rows. A count that moved here would be a
  defect, not a fix.
- **Stale:** the pin names bytes that no longer exist. `typed-pipeline-gate.py`
  refuses (`FAIL L1-profile`, exit 2) rather than silently accepting the
  difference, which is the designed behaviour — but it means the claim's
  "the named-holds set updated honestly" is met only in the **count** sense.

**What an honest re-pin looks like** (named, not landed — the O seats own the pin
surface and this seat writes no `expected.json`):

| field | current | successor |
|---|---|---|
| `packet_sha256` | `86079a6708a0d360bedfed60306274c09ec4f4e76a5912b94a05f762d17caebc` | `543d68a82640e1b0c53b9cb7cb26c4dc60fce5878c2bf487050ead3af0945c4f` |
| `projection_sha256` | `88a94422b4123f6b436f9935590d69f081f90e688655ee605f33e0c1305fb68d` | `339bfd83bf66832479b5b8ffbbce708c8be15e13b08967fa7049b848661a3cf8` |
| `projector_sha256` | `2819f687…` | `2819f687…` *(unchanged — ok)* |
| `counts` | 12 / 0 / 0 | **12 / 0 / 0** *(unchanged, and that is the honest reading)* |
| `revision_note` | round-27 register-law build, revision 2 | must name the round-28 RL-4 landing |

`tools/gates/typed-pipelines.json` (`69f250df…`) needs the same treatment: its
`d4` profile pins `packet 86079a67…` and `projection 88a94422…`.

## 5. The green/red ledger at the final stamp

Measured 2026-10-18T20:14:58Z, `TMPDIR=$PWD/.scratch`, cwd = lane root.

| check | command | verdict |
|---|---|---|
| D4 assembly | `python3 tools/assemble-culture-d4.py --check` | **exit 0**, `byte-identical deterministic assembly` |
| D4 assembler selftest | `python3 tools/assemble-culture-d4.py --selftest` | **81/81** |
| argot leg (packet) | `python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | **exit 0**, `records=183 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0` |
| argot leg (typed packet) | `… examples/culture-d4/packet.d4.typed.yml` | **exit 0**, `records=207 … violations=0 rule_holds=0` |
| argot selftest | `python3 tools/gates/argot-derivation-gate.py --selftest` | **27/27** |
| argot fixture (red control) | `… tools/gates/fixtures/argot-derivation-gate.yml` | **exit 1**, 5 findings, output sha `556d31d6…` — **unchanged across every round** |
| projector | `python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml` | **exit 1**, `findings_total=12`, `rank_rules_unresolved_items=0` — the delivered hold count |
| D4 label gate | `python3 tools/gates/d4-typed-labels-check-gate.py examples/culture-d4/typed-labels.d4.yml` | **exit 0**, stdout sha **`1c8add32…`** — byte-identical to every earlier row |
| D4 assembly gate | `python3 tools/gates/d4-assembly-check-gate.py examples/culture-d4/packet.d4.yml` | **exit 0**, stdout sha **`c60820a5…`** — byte-identical to every earlier row |
| naming gate (red control) | `python3 tools/gates/naming-collision-gate.py examples/culture-d4/packet.d4.yml` | **exit 1**, **14** findings, stdout sha **`0c613c9d…`** — **unchanged**; the new records add no naming finding |
| **typed gate** | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | **exit 2**, `FAIL L1-profile` (stale pins, §4). **`ok L3b-argot` still green** |
| battery | `python3 tools/check-gate-battery.py` | `battery_exit 0, pass 7, fail 0, unevaluable 0`; `coverage 9/9`, `pinned 19` |
| law leg | `grep -rl "D4L-LAW" tools/ \| wc -l` | **0** |

**Two red readings, and neither is a defect in the delivered work.** The typed
gate is red because two pin files still name the pre-RL-4 bytes (§4) — an O-seat
re-pin. The naming gate is red because it has been red since round 20 and its
output is byte-identical (§5, "a reproduced red stays red").

## 6. The RL-3 ceiling — the claim's third leg, not met at this stamp

The claim's `after_required` ends: "the RL-3 ceiling recorded as a design
constraint in the knowledge entry". Measured at this seat's final stamp:

```
$ git show HEAD:corpus/knowledge/linguistics/register-strata-attestation.md | wc -l   # 313
$ wc -l corpus/knowledge/linguistics/register-strata-attestation.md                   # 313
$ git show HEAD:corpus/knowledge/linguistics/register-strata-attestation.md | grep -c "^## "  # 12
$ grep -c "^## " corpus/knowledge/linguistics/register-strata-attestation.md          # 12
$ ls corpus/knowledge/linguistics/ | wc -l                                            # 20
```

At that stamp the entry was **byte-identical to `HEAD`** and no new ceiling entry
existed. The claim's own runner confirmed it as a missing dependency:
`missing_dependencies: corpus/knowledge/linguistics (new ceiling entry)`.

**The amendment landed 56 seconds after this seat's last census.** Measured
2026-10-18T20:19:39Z:

```
$ wc -l corpus/knowledge/linguistics/register-strata-attestation.md        # 436  (was 313)
$ grep -c "^## " corpus/knowledge/linguistics/register-strata-attestation.md # 13   (was 12)
$ grep -n "^## " … | tail -1
315:## 13. Amendment (round 28): the register-lexicon ceiling, re-measured, with its mechanism
$ sha256sum corpus/knowledge/linguistics/register-strata-attestation.md    # ddeeee75af98…
$ ls corpus/knowledge/linguistics/ | wc -l                                 # 20   (unchanged)
```

**So leg 7 splits into three readings, and all three are recorded rather than
averaged.** (i) At this seat's stamp the amendment was **absent**. (ii) At
**20:19:39Z** the C seats landed the **amendment in the shape the claim asked
for**: a **new section §13**, all twelve earlier headings still present, no
in-place rewrite — precisely the "amendment entry, not in-place rewrite" the
claim words. (iii) At **20:20:06Z** the **new sourced entry** landed:
`corpus/knowledge/linguistics/register-lexicon-ceilings.md`, 287 lines,
frontmatter-complete (topic / gap-filled with its own absence sweep / numbered
sources / couples / source / verified-at / recheck), citing the round-27
measurements **and** the round-28 `reports/round-28/ceiling/measure-ceiling.py`
instrument, with external sources (Dixon, Halliday, Gotowski, Aronoff, Bauer)
each carrying an explicit framework-status and calibration line. The linguistics
directory now holds **21** entries.

(iv) At **20:20:23Z** the **README reconciliation** landed: `corpus/README.md`
carries **revision 1.9** naming the round-28 C entry, an index row for the new
entry (`:138`), and the totals line moved to `Total knowledge entries: 201.`
(`:469`). **The residual named in the earlier reading of this file is closed** —
recorded here rather than deleted, because the intermediate reading was the honest
one at its stamp.

**What the ceiling is**, stated for the C seats who own the entry, in the round-27
measurement's own terms (`reports/round-27/law/review.md` §4):

- Over the delivered 62-record lexicon, the mark-axis plain words split
  `reverse-legal=18` / `reverse-ILLEGAL=9`; **by class, every `abstract` word is
  reverse-illegal (0 legal of 5)**.
- The five legal/institutional abstractions — `L-15 wer`, `L-30 gis` (**oath**),
  `L-44 wad`, `L-45 tikmes`, `L-51 gul` — **all refuse `reverse`**.
- Every one of the eight landed register forms descends from a
  **material-presence** base (`tik`, `tum`, `mol`, `nes`, `hum`, `mes`, `rek`,
  `sam`). **Zero abstractions.**

**The general craft lesson the C claim must write** (this seat states it, the C
seats source it): *a register's derivation operation constrains which semantic
fields it can natively spell.* A register built by reversing its bases can only
name what its bases name — so the oath, the one act whose bindingness is the
law's whole subject, cannot be named in the register the law governs. That is a
**design constraint**, not a defect: the round-27 law writes around it (naming the
act by a form the register can carry and putting the consequence on the council's
side) rather than amending the operation rule.

## 7. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
sha256sum examples/culture-d4/packet.d4.yml examples/culture-d4/typed-labels.d4.yml \
  examples/culture-d4/expected-holds.json examples/culture-d4/components/03-orthography.yml \
  examples/culture-d4/components/09-costumes.yml tools/gates/typed-pipelines.json
grep -n "packet_keys" examples/culture-d4/components/03-orthography.yml examples/culture-d4/components/09-costumes.yml
python3 - <<'PY'
import runpy, pathlib
ns = runpy.run_path("tools/assemble-culture-d4.py")
doc = ns["reader_parse"]()(pathlib.Path("examples/culture-d4/packet.d4.yml").read_text())
print({b: len(doc.get(b) or []) for b in ("records","literacy_institutions","enforcement")})
print("register_law in PACKET_KEYS:", "register_law" in ns["PACKET_KEYS"])
print("records in RECORD_FIELDS:", "records" in ns["RECORD_FIELDS"])
PY
grep -rl "D4L-LAW" tools/ | wc -l                       # 0 — no replay leg
python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml | head -1
python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml | tail -3
python3 tools/check-gate-battery.py | tail -6
python3 reports/round-28/scribe/x54-law-negatives-spotcheck.py | grep ^verdict
python3 reports/round-28/audit/x59-register-law-negatives.py | tail -3
git show HEAD:corpus/knowledge/linguistics/register-strata-attestation.md | wc -l
```

## 8. Limits

- The rows in §1, §2.1 and §5 are **measured today** on the live tree at
  `69cecbc`; they are the rows a round-28 generation records. They are not filed —
  this seat writes no `MANIFEST.tsv` and no `expected.json`.
- The successor pins in §4 are **named, not landed**.
- **Every reading binds to the digest and stamp beside it, and the tree moved once
  in this seat's window** (the RL-4 landing, ~20:13Z). A successor must re-hash
  before quoting any digest here. In particular the packet digest quoted in
  round-27 artifacts (`86079a67…`) is **one landing out of date**.
- **This file makes no claim that the round-28 D claim is met.** It measures the
  half that is (RL-4) and the half that is not (RL-1), and names the third leg's
  dependency (the ceiling entry).
- A green run is not canon, not lore acceptance and not a clearance. This file
  admits nothing.
