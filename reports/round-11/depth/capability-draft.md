# R11-D24 — scribe: capability-row draft for `d2-typed-pipeline`

- seat: **R11-D24** (scribe, claim D), round 11 (loop 1 of 3, build round 4 of 4), 2026-10-17
- assignment (verbatim): "DEPTH R11-D24 (scribe): capability-row draft for d2-typed-pipeline; reports/round-11/depth/capability-draft.md."
- writes: this file only (scratch under `.scratch/d24-*`). No commit, no push, no tool/example/SCORECARD/LOG edit; `reports/round-{8,9,10}/**` are filed and untouchable here.
- canon: NON-CANON engineering evidence. **The row in §4 is a draft — the orchestrator admits it, if and when claim D's demonstrated run exists.**
- measurement tree: HEAD `e3ef1719c123ab4fb83ed94e033961dd61a2e8c7`, worktree dirty (see §1); all stamps UTC; local is UTC-3.
- status: **complete for this shard's scope — before-state measured, after-state bound to the landed wiring and re-measured green across its revision churn.** `tools/typed-gate-flow.py` ran the e2e over `examples/culture-d2` green at **two consecutive revisions** — `a7e1224f…` (`22:17:16Z`) and `5758e315…` (`22:19:23Z`) — both **exit 0, `summary: 10/10 checks passed`, `findings: 16 (hold 15, note 1)`**, with **byte-identical stdout** (`204857cb…`); one revision before them (`aea5eaaf…`, ~`22:16:45Z`) the same command was **exit 1, 8/10** (§3.1). The row names the revision measured last and the re-run-at-admission rule (§3.1, §7); `⟨…⟩` remains only for the orchestrator's admission act. §5.4 records three independent cross-checks against the design.

## 0. What this shard is and is not

The deliverable is one paste-ready SCORECARD capability row for the round-11 depth
capability `d2-typed-pipeline`, plus the exact commands and evidence paths by which
each of its clauses can be checked. It is not a claim of the capability, not an
acceptance run, and not a substitute for `reports/round-11/run-validation.py`
(claim D's counting command, owned elsewhere). Round 8's row (`d2-typed-labels`)
stays in SCORECARD as admitted; this draft proposes the *successor* row that the
round-11 D claim's after-state licenses — or nothing, if that state is not reached.

## 1. Measurement environment and stamps

```sh
git rev-parse HEAD && git status --porcelain && date -u +%FT%TZ
```

Observed `2026-10-17T22:00:55Z`:

```
e3ef1719c123ab4fb83ed94e033961dd61a2e8c7
 M reports/round-10/coverage/index-update-22.md
 M reports/round-5/validation.json
 M reports/round-6/checkpoint-validation.json
?? reports/round-11/depth/
```

- Sibling seeds write concurrently; the three modified paths are **filed earlier-round
  artifacts** (rounds 5, 6, 10) and are not this shard's files. Reported, not absorbed
  (§7.4) — a worker touching filed bytes is the conformance defect round 10 already
  recorded once.
- **Environment:** `export TMPDIR=$PWD/.scratch` before every scratch-writing command
  (standing round rule; `/tmp` inode exhaustion is historical here). No scratch left the repo.

## 2. Before-state, measured (the row's *before* clause)

### 2.1 The legacy checked channel still pronounces ten English garment labels

```sh
python3 tools/gates/naming-collision-gate.py examples/culture-d2/packet.d2.yml   # 22:0xZ
```

Exit **1**; `FINDING` lines: **10 × `PHON-INVENTORY: FAIL`**, the ten are exactly
`GAR-01`..`GAR-10` (captured `.scratch/d24-naming.out` sha256 `ebc8850d…`). Sample
verbatim: `FINDING PHON-INVENTORY: FAIL — name GAR-01 'winter valley coat (heavy
felted wool; uncombed finish optional)': symbol /v/ at position 7 is not in the
declared inventory …`. The same class is on record as the motivating defect:
`examples/culture-d2/ASSEMBLY.md:94` ("the naming gate treats costume garment labels
as entity names and tries to pronounce the supplied English descriptions as D2"),
frozen round-4 output 10/10 `GAR-*`
(`tools/gates/frozen/round-4/naming-collision-gate.out`). The residual round-8 limit
is the *before* text of claim D: "The D2 example's ten GAR labels remain on the legacy
gate's checked channel" (`reports/round-8/depth/skill-table-draft.md:299-303`).

### 2.2 The typed projection exists but is standalone (gates do not consume it)

```sh
python3 tools/d2-typed-labels.py --json        # exit 1 (findings present), report complete
```

Observed `22:0xZ` (`.scratch/d24-typed.json` sha256 `880d0e45…`):
`ok=false`, `stats {labels: 58, fail: 0, hold: 15, note: 1}`, finding codes
`D2L-FORM-UNRESOLVED ×10 (hold)`, `D2L-NATIVE ×2 (hold)`, `R-RANK-CONFLICT ×4
(3 hold + 1 note)` — 16 findings total. Ten of the holds are the owed GAR forms
(`label_id LEX-GAR-01..10 has no supplied native/borrowed form`). This is the §5
hold-set candidate; the gates above still evaluate the raw packet.

### 2.3 The round-8 artifact's packet pin is stale — `--check` is red by one line

```sh
python3 tools/d2-typed-labels.py --check
```

Exit **1**: `examples/culture-d2/typed-labels.d2.yml differs from the deterministic
projection`. Cause measured, not inferred: the emitted projection (`.scratch/d24-emit.yml`
sha256 `a3aa452c…`) differs from the committed artifact (`e70ba147…`) in **exactly one
line** — `assembly.packet_sha256`: emitted `e0f21509e14ac03e…`, artifact
`8da90b0788f86fd1…`.

History from git (all in-repo):

| revision | `examples/culture-d2/packet.d2.yml` sha256 | note |
|---|---|---|
| `c53782a` (supplement-opencode-1) | `8da90b07…` | the artifact's pin |
| `e1694ba` (round-8 admit) | `e0f21509…` | packet regenerated; diff is the `assembly.reader_sha256` line only (`29a9361c…` → `e6bffd70…`, the repaired costume gate) — `git diff c53782a e1694ba -- examples/culture-d2/packet.d2.yml` (2 lines changed) |

So the drift is the round-8 admit commit re-pinning the packet (SCORECARD round 8:
"Owner action during integration: D2 packet regenerated to re-pin the reader sha …
not by the D tool") while the typed artifact was not re-emitted. It is a **stale pin,
not a logic break**: the projection body is byte-identical apart from the pin line.
At this shard's first stamps the round-8 row's `--check (exit 0…)` leg was therefore
red on the live tree (same observation as `reports/round-11/depth/scribe.md` §1.2);
**D07's re-pin closed it at `22:14Z`** — the committed projection became `a3aa452c…`
(this seat's predicted bytes) and `--check` now exits 0 (§3 c7, measured `22:18Z`).
The before/after pair is exactly what claim D's re-pin leg was for.

### 2.4 The frozen replay is red on the live tree (the leg claim D must re-pin)

```sh
python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv
```

Exit **2**: `REPLAY COULD-NOT-EVALUATE: 7 could-not-evaluate, 0 mismatch, 0 reproduced
of 7 row(s)` — every row `gate_digest_mismatch` ("on-disk bytes are not the pinned
revision"), the pinned revisions being the round-3 gate bytes (captured
`.scratch/d24-replay.out` sha256 `76c00a6b…`; stamped ~22:02Z). This is the same
fail-closed state round 8 documented for its window (`reports/round-8/depth/test-replay.md`
§0: live tree "exit 2, 7/7 could-not-evaluate `gate_digest_mismatch`", with the
isolated pinned-gate control at 7/7 green). The pins are *doing their job*: rounds
8–9 legitimately repaired the gates. "Frozen replay re-pinned and green" (claim D)
means a round-11 re-pin whose replay reproduces the new generation's rows — **which
landed at `22:14Z`**: `tools/gates/frozen/round-11/MANIFEST.tsv` (`4ddb911c…`,
**10 rows** = 5 typed + 5 legacy, the round-3 manifest left as filed) replays
**`REPLAY OK: 10/10`, exit 0** (§3 c5; this seat's own run, `22:17:08Z`).

### 2.5 Standing green legs at draft time

| leg | command | result |
|---|---|---|
| tool selftest | `python3 tools/d2-typed-labels.py --selftest` | exit 0, `selftest: 39/39 checks passed` (22:02Z, re-run by this seat) |
| D2 assembly | `python3 tools/assemble-d2.py --check` | exit 0, `packet.d2.yml: byte-identical deterministic assembly` (22:00:41Z) |
| D3 (interop neighbour) | `python3 tools/assemble-culture-d3.py --check` | exit 0 (reported by `reports/round-11/depth/scribe.md` §1.1, 22:01Z — not re-run here) |

## 3. Claim-D after-state, clause by clause, bound to commands

From `reports/round-11/claims.json` claim D `after_required`; each clause gets the
command that can check it, bound to the design's named interfaces
(`reports/round-11/depth/design.md`, landed 22:06:15Z) and to the landed
implementation (`tools/typed-gate-flow.py`, sha256
`5758e315593bb818dbf38c3c3ed7f79eb9ea555955331fadab4b50b2faa92075` at the final
re-measurement, `22:19:23Z`; the readings below were taken green at both that
revision and its predecessor `a7e1224f…`, byte-identical stdout; the design's
separate `assemble-d2-typed.py` + `tools/gates/typed-pipeline-gate.py` names were
merged into this one tool — a name divergence reportable to the D20 wiring-vs-spec
review, not absorbed here).

| # | clause (claim D) | verifying command | measured at handoff (revision `5758e315…`, 22:19:23Z; identical at `a7e1224f…`, 22:17:16Z) | evidence path | status |
|---|---|---|---|---|---|
| c1 | assembler (or a documented adapter step) consumes typed labels | `python3 tools/typed-gate-flow.py --check`; `python3 tools/assemble-d2.py --check` | adapter = `tools/typed-gate-flow.py` (CLI `--packet/--typed-packet/--expected/--emit/--check/--freeze/--selftest`); `--check` → exit 0, "typed gate artifacts: byte-identical deterministic derivation"; base assembler exit 0 | `examples/culture-d2/packet.d2.typed.yml` `e8a83445…`; design §2 | **green** |
| c2 | gates evaluate the typed packet; translated labels never on the sound channel | `python3 tools/typed-gate-flow.py` (leg L2) | exit 0; `delta: 10 PHON artifact(s) retired, 0 added, retained lines identical`; `typed sound channel: 0 translated-label artifact(s)`; `differential-exact` ok | capture `.scratch/d24-tgf-e2e-green.txt` `204857cb…` | **green** |
| c3 | owed native forms carried as named holds, not PHON artifacts | same | the ten `D2L-FORM-UNRESOLVED` holds `LEX-GAR-01..10` emitted verbatim, plus the carried `D2L-NATIVE` ×2 and `D2L-RANK` hold ×3 | same capture (finding lines 5–20) | **green** |
| c4 | e2e exits 0, findings **exactly equal** the expected hold set | `python3 tools/typed-gate-flow.py [--json]`; acceptance `python3 reports/round-11/run-validation.py` | exit 0, `summary: 10/10 checks passed`, `findings: 16 (hold 15, note 1)`, `hold-set-equal` ok; the **same command was exit 1 / 8/10 one revision earlier** (`aea5eaaf…`, §3.1) | capture `204857cb…`; `examples/culture-d2/typed-gate.expected.json` `7ed59731…` | **green at measured revision** |
| c5 | frozen replay re-pinned and green | `TMPDIR=<outside repo> python3 tools/replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv` | exit 0, `REPLAY OK: 10/10 rows reproduced the recorded verdicts` (this seat's own run, 22:17:08Z; 5 typed + 5 legacy rows, my naming-gate hashes inside it); the rounded-3 manifest is left as filed and still exits 2 | `.scratch/d24-replay-r11.out` `19252931…`; `tools/gates/frozen/round-11/MANIFEST.tsv` `4ddb911c…`; `repin.md` §0 | **green** |
| c6 | d2/d3 selftests + battery remain green | `tools/d2-typed-labels.py --selftest`; `tools/assemble-culture-d3.py --selftest`; `tools/typed-gate-flow.py --selftest`; `tools/check-gate-battery.py --selftest` | `39/39` · `85/85` · `14/14` · battery selftest `28/28 controls` — all exit 0 (this seat, 22:02–22:17Z) | §2.5, §8.1 | **green** |
| c7 | the projection's stale pin (§2.3) is closed by the re-pin | `python3 tools/d2-typed-labels.py --check` | exit 0, "byte-identical deterministic projection"; committed projection sha `a3aa452c…` = D07's move-in = the design's §5.1 prediction = this seat's §5.4(3) measurement | `examples/culture-d2/typed-labels.d2.yml`; design §5.1 | **green** |

TMPDIR caveat for c5: `replay-frozen.py` refuses a mirror whose root contains
`TMPDIR` (`mirror_unsafe`, named in `repin.md` §6.5); the run above used
`TMPDIR=$HOME/.cache/d24-mirror`, outside the lane root, and wrote no lane file.

### 3.1 The e2e at handoff — measured, with the revision-churn warning

At `~22:16:45Z` the then-current `tools/typed-gate-flow.py` (`aea5eaaf…`) exited
**1** with `summary: 8/10 checks passed — hold-set-equal; expected-file-current`
(`hold-set-equal — observed 16 findings, expected 16`), and its `--selftest` was
`9/14`; `--check` failed on `expected-file-current` (the committed
`examples/culture-d2/typed-gate.expected.json` was not yet the deterministic
derivation — its sha then was `e962849a…`, now `7ed59731…`). Within the same minute
the tool was replaced (`a7e1224f…`) and the same commands went `10/10`, `14/14`,
exit 0; a **third revision** (`5758e315…`, `22:19:12Z`) followed and the commands
re-ran green with **byte-identical stdout** (`204857cb…`, the same capture hash as
the `a7e1224f…` run) — receipts §8.1.

Consequence for admission, matching the round-8 precedent and D22's C1 threat: **the
row names its measured revision**, and the orchestrator (or the acceptance harness)
must re-run the row's commands at integration and re-pin if the tool changes again. A
row quoting "exit 0" without the revision and without the re-run is exactly the
"harvested expectation" pattern the circularity review audits.

## 4. The draft row (paste-ready — orchestrator admits)

Landing surface: `SCORECARD.md` §Capabilities table, columns
`name | demonstrated behavior | command / evidence | first working`. Row text as it
would be pasted **once c1–c7 verify**; `⟨…⟩` marks values that must be read from the
landed fragments at admission (never invented here):

```markdown
| d2-typed-pipeline | The round-8 typed-label projection is consumed end-to-end by one documented adapter gate (`tools/typed-gate-flow.py`): the ten English `GAR-*` garment glosses leave the sound/identity channel (`delta: 10 PHON artifact(s) retired, 0 added, retained lines identical`; typed sound channel 0 translated-label artifacts) and the ten owed native forms are carried as named holds — `examples/culture-d2` exits 0 with findings exactly 15 holds + 1 pinned note + 0 fails, hold lines emitted verbatim; the projection's stale packet pin is closed (`--check` exit 0) and a new round-11 frozen generation replays 10/10 while the filed round-3 manifest keeps its bytes | `python3 tools/typed-gate-flow.py` (exit 0, `summary: 10/10 checks passed`); `python3 tools/typed-gate-flow.py --selftest` (14/14); `python3 tools/d2-typed-labels.py --selftest` (39/39); `python3 tools/d2-typed-labels.py --check` (exit 0); `python3 tools/replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv` (`REPLAY OK: 10/10`); measured revision `tools/typed-gate-flow.py` sha256 `5758e315…` (identical readings at `a7e1224f…`); acceptance `python3 reports/round-11/run-validation.py` | round 11 (⟨admitted by orchestrator⟩) |
```

- **Before-state for the row** (claim D, `reports/round-11/claims.json`): "The
  d2-typed-labels projection (round 8) is standalone: the D2 example's ten GAR labels
  remain on the legacy gate's checked channel … gates do not consume typed labels."
  Measured at draft time: §2.1 (10 `PHON-INVENTORY` FAILs naming `GAR-01..GAR-10`),
  §2.2 (projection emits 15 holds + 1 note but nothing downstream consumes it),
  §2.3 (its own committed artifact is stale-pinned).
- **Row semantics guard (design §3.2):** exit 0 must never be readable as "the
  culture is clean". The flow emits the 15 hold lines verbatim (`findings: 16 (hold
  15, note 1)`), so the artifact a reader sees stays red at the design level; a hold
  laundered into a note fails the hold-set comparison. The row's wording above says
  "exits 0 with findings exactly 15 holds + 1 pinned note" — never "passes clean" or
  "0 findings".
- **Revision discipline (not a formality):** the row names the revision measured last
  (`5758e315…`) because the **same commands exited 1 (8/10, selftest 9/14) two
  revisions earlier** (`aea5eaaf…`, §3.1) and only re-ran green — with byte-identical
  stdout — at the next two revisions. At admission the orchestrator must re-run the
  row's commands; if the tool has changed again, the row's numbers and the freeze are
  re-taken (§7.2).
- **Replay denominator:** measured, not assumed —
  `tools/gates/frozen/round-11/MANIFEST.tsv` (`4ddb911c…`) holds **10 rows** (5 typed
  + 5 legacy), and the replay reproduces `10/10`, exit 0 (`22:17:08Z`). The filed
  round-3 manifest is untouched and still exits 2 (its gates moved on, §2.4) — the
  row says "while the filed round-3 manifest keeps its bytes" precisely so the
  divergence is reported, never repaired by editing filed bytes.
- **The round-8 row is not deleted or edited by this draft.** `d2-typed-labels`
  (round 8) records the tool's own admission; if the orchestrator admits
  `d2-typed-pipeline`, the successor row's relationship to it (supersede / keep both)
  is the orchestrator's call, and its `--check` leg should be re-read against §2.3
  before any claim about it is repeated.
- **Nothing enters SCORECARD on this draft.** Claim D's own rule and the round-8
  precedent (`reports/round-8/depth/scribe.md` §5) apply: row only on demonstrated
  run; the demonstrated run is `reports/round-11/run-validation.py`.

## 5. The expected hold set — fixed by `design.md` §4

Claim D requires "findings exactly equal to the expected hold set" and D01–D02 must
"name each expected hold". That contract now exists: `reports/round-11/depth/design.md`
§4 (landed `22:06:15Z`) fixes it, and §4's row text uses it verbatim. This section
restates it only as far as the row depends on it, and records the independent
cross-checks (§5.4).

### 5.1 The set (design.md §4.2–4.3): 15 holds, 1 note, fail set ∅

| id | severity | where | reason | class |
|---|---|---|---|---|
| `D2L-FORM-UNRESOLVED` ×10 | hold | `GAR-01`..`GAR-10` | `LEX-GAR-*` has no supplied native/borrowed form; the gloss is routed off-channel (`garment` → `garment_gloss`) | **new to this wiring** — replaces the ten `PHON-INVENTORY` FAILs |
| `D2L-NATIVE` ×2 | hold | `L-15`, `L-16` | supplied `sára`/`sará` carry `á` outside the segment inventory; held for the form's owner, not failed | carried from the round-8 projection |
| `D2L-RANK` ×3 | hold | `TR-04#a\|TR-06#a`, `WR-02#g\|WR-09#g`, `WR-08#g\|WR-09#g` | rank adapter: `genuine-priority-gap` | carried |
| `D2L-RANK` ×1 | **note** | `SR-01#a\|SR-01#b` | `band-keyed-pair` | carried, **excluded from the hold set** |

The five carried holds are in the set because L3 compares the *whole* pipeline
finding set — a wiring that silently dropped them would be indistinguishable from one
that fixed them (design §4.2).

### 5.2 Exactness rules (design §4.4, binding on the gate)

1. Comparison key = the triple `(id, severity, where)` as a **set**, plus the counts
   `hold 15 / note 1 / fail 0`.
2. No extra hold, no missing hold, no severity swap; the note must be present and
   must **not** count as a hold.
3. `detail` strings are pinned too (canonical JSON, sorted by `(id, where)`): a prose
   rewrite is an explicit re-pin, not a pass. Advisory-drift-only comparison is
   **rejected** — it is the laundering channel D19 probes.
4. The set is over the **typed run** only; the legacy run's ten `PHON-INVENTORY`
   FAILs are not part of the set — they are the minus-basis of L2.

### 5.3 The hazards the set must exclude (design §6; negative controls D17–D19)

A translated label smuggled onto the sound channel (caught by L2: a typed-run finding
naming an off-channel record), an owed form dropped silently (caught by the adapter
coverage check and L3's count), a hold laundered as clean (caught by L3: notes are
pinned separately). Any hold-set wording that cannot be checked against these three
is not admissible.

### 5.4 Independent cross-checks between this seat and the design

Three numbers were measured by this seat **before** `design.md` landed
(22:01–22:04Z) and are independently pinned by the design (22:06:15Z) — relevant to
D22's circularity threat model (C1 "harvested expectation", C6 "self-issued
exemption"):

| # | this seat (command, capture, stamp) | design.md location | verdict |
|---|---|---|---|
| 1 | `d2-typed-labels.py --json`: 15 holds + 1 note, triples `(id, severity, where)` exactly as §5.1 (`.scratch/d24-typed.json` `880d0e45…`, ~22:01Z) | §4.2/§4.3, stats `{fail: 0, hold: 15, note: 1}` | **agree exactly** |
| 2 | naming gate over the live packet: 17 `FINDING` lines = `PHON-INVENTORY ×10` + `NAME-NEAR ×6` + `CROSS-HOLD ×1`, exit 1 (`.scratch/d24-naming.out` `ebc8850d…`, ~22:02Z) | §1.1, same split and same stdout sha256 `ebc8850d…` | **agree exactly** |
| 3 | `--emit` projection bytes: sha256 `a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43` (`.scratch/d24-emit.yml`, ~22:01Z) | §5.1's predicted post-re-pin bytes `a3aa452c…` | **agree exactly** |

What this does **not** settle: an expectation transcribed from the run under test is
still tautological by construction (D22's C1). The independent anchors are the
*legacy* run's ten `PHON-INVENTORY` FAILs (frozen round-4 output, `10/10 GAR-*`) and
the design's per-hold source column (`11-costumes` gloss routing; T1 table;
`era-language-staging.md:124`) — the D20/D22 reviews own that argument, not this
draft.

## 6. What the row must not claim (limits carried from round 8, still true)

- Typing is **representation discipline, not clearance**: separating the gloss from
  the sound channel "is not real-language clearance" (`SKILL.md:197`), a native form
  is not thereby real, and a loan's declared donor is not thereby historical
  (`reports/round-8/depth/skill-table-draft.md` §7).
- Holds are not a design PASS; a red ex-ante stays red where it should.
- No canon, no promotion, no lore receipt; the handoff boundary (`PROVINCE.md`) is
  untouched by anything this draft describes.
- The frozen replay verifies bytes and verdicts, never design quality or scholarship
  (`corpus/knowledge/verification/gate-frozen-run-standard.md`).

## 7. `to-verify` and open items

1. **Expected hold set — fixed, no longer open.** `design.md` §4 (landed 22:06:15Z)
   names all 15 holds and the 1 note; §5 restates it; §5.4 records three independent
   agreements with this seat's earlier measurements. If the realized wiring ships a
   different set, that is a finding against the design (or a re-pin event), not a
   silent edit of §4/§5 here.
2. **The e2e entry point — landed and measured green, with a named divergence.**
   The design's separate `assemble-d2-typed.py` + `tools/gates/typed-pipeline-gate.py`
   landed **merged** as `tools/typed-gate-flow.py` (`a7e1224f…`). That merge diverges
   from design §2.1/§3.1 and its single-writer map (§7); it is reported to the D20
   wiring-vs-spec review, not rewritten here. Measured at that revision: §3's c1–c7
   all green; one revision earlier (`aea5eaaf…`) the same commands were red (§3.1).
3. **Admission act — re-run, then admit.** At integration, re-run the row's commands
   against the then-current tool revision (§3.1's rule) before pasting the row:
   the freeze is `tools/gates/frozen/round-11/MANIFEST.tsv` (`4ddb911c…`, 10 rows,
   `10/10` reproduced by this seat 22:17:08Z); the committed expected set is
   `examples/culture-d2/typed-gate.expected.json` (`7ed59731…` — the design §4.5 name
   was `expected-holds.json`: another landed-name divergence, reported, not absorbed);
   the typed packet is `examples/culture-d2/packet.d2.typed.yml` (`e8a83445…`).
4. **Design-side items this draft inherits (reported, not absorbed; D20–D23 own them):**
   (a) the naming gate still exits 1 with zero FAIL lines after routing (6 REVIEW +
   1 HOLD, design §1.3/§8.2) — any leg keying off its *exit code* would be wrong;
   (b) the carried `native-form / status: to-verify` silent-class defect from round 10
   (design §8.3) — the adapter must inject the hold rather than patch the projector;
   (c) `detail`-string pinning (design §4.4(3)) is deliberate (the D19 defence) but
   contestable — the trade-off is named there so it is decided, not drifted; (d) the
   circularity argument for the re-pin is D22's, and its C1 threat ("harvested
   expectation") is only answered by the legacy-run anchors named in §5.4.
5. **Adjacent observation, reported not absorbed — growing:** filed earlier-round or
   round-10 artifacts modified in the worktree went from three to **seven** between
   `22:00:55Z` and `22:08:21Z` (`git status --porcelain`): `reports/round-5/validation.json`,
   `reports/round-6/validation.json`, `reports/round-6/checkpoint-validation.json`,
   `reports/round-7/validation.json`, `reports/round-8/validation.json`,
   `reports/round-9/validation.json`, `reports/round-10/coverage/index-update-22.md`.
   Six of the seven are `validation.json` files — the same shape as the round-10
   conformance defect that was reverted once already. Whoever owns the sweep should
   compare these against their committed bytes before integration; this shard wrote
   none of them (re-check at handoff in §8.4).
6. **The "PHON artifacts gone" clause now has live after-evidence:** the e2e's own
   `delta: 10 PHON artifact(s) retired, 0 added, retained lines identical` and
   `typed sound channel: 0 translated-label artifact(s)` with `differential-exact` ok
   (capture `204857cb…`) — real gate runs, not the design's scratch experiment
   (design §1.3). The legacy half of the differential is §2.1.

## 8. Receipts

### 8.1 Commands run by this seat (all with `TMPDIR=$PWD/.scratch`; stamps UTC)

```sh
# 2026-10-17 22:00–22:03Z, lane repo root
git rev-parse HEAD && git status --porcelain && date -u +%FT%TZ          # e3ef1719…, dirty §1
python3 tools/d2-typed-labels.py --check            # exit 1 — one-line pin drift (§2.3)
python3 tools/d2-typed-labels.py --emit .scratch/d24-emit.yml          # exit 1; a3aa452c…
diff .scratch/d24-emit.yml examples/culture-d2/typed-labels.d2.yml     # 1 changed line: packet_sha256
python3 tools/d2-typed-labels.py --json             # exit 1; 16 findings; 880d0e45… (§2.2)
python3 tools/d2-typed-labels.py --selftest         # exit 0; 39/39 (22:02Z)
python3 tools/assemble-d2.py --check                # exit 0 (22:00:41Z)
python3 tools/gates/naming-collision-gate.py examples/culture-d2/packet.d2.yml  # exit 1; 10 PHON-INVENTORY (§2.1); ebc8850d…
python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv         # exit 2; 7/7 c-n-e (§2.4); 76c00a6b…
git diff c53782a e1694ba -- examples/culture-d2/packet.d2.yml         # reader_sha256 line only
python3 tools/check-gate-battery.py --selftest      # exit 0; "SELFTEST OK 28/28 controls" (22:04Z)
```

```sh
# 2026-10-17 22:16–22:19Z — the wiring lands and churns; the row's measured legs
python3 tools/typed-gate-flow.py                    # aea5eaaf…: exit 1, "summary: 8/10 checks passed" (RED, §3.1)
python3 tools/typed-gate-flow.py --selftest         # aea5eaaf…: 9/14 (RED)
python3 tools/typed-gate-flow.py                    # a7e1224f…: exit 0, 10/10, "findings: 16 (hold 15, note 1)"
python3 tools/typed-gate-flow.py --selftest         # a7e1224f…: 14/14, exit 0
python3 tools/typed-gate-flow.py --check            # a7e1224f…: exit 0, "byte-identical deterministic derivation"
TMPDIR=$HOME/.cache/d24-mirror python3 tools/replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv
                                                   # exit 0, "REPLAY OK: 10/10 rows reproduced" (22:17:08Z)
python3 tools/d2-typed-labels.py --check            # exit 0 — the pin closes after D07's 22:14Z re-pin
python3 tools/assemble-culture-d3.py --selftest     # exit 0, 85/85
python3 tools/typed-gate-flow.py                    # 5758e315…: exit 0, 10/10, byte-identical stdout 204857cb…
python3 tools/typed-gate-flow.py --selftest         # 5758e315…: 14/14, exit 0
python3 tools/typed-gate-flow.py --check            # 5758e315…: exit 0
sha256sum tools/typed-gate-flow.py examples/culture-d2/packet.d2.typed.yml examples/culture-d2/typed-gate.expected.json
```

### 8.2 Digests as read (`sha256sum`)

| artifact | sha256 |
|---|---|
| `tools/assemble-d2.py` | `8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d` (22:02:46Z) |
| `tools/d2-typed-labels.py` | `0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802` (22:02:46Z) |
| `examples/culture-d2/packet.d2.yml` | `e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643` (22:02:46Z) |
| `examples/culture-d2/typed-labels.d2.yml` | **`a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43`** (22:18Z — D07's re-pin; was `e70ba147…`) |
| `tools/typed-gate-flow.py` | **`5758e315593bb818dbf38c3c3ed7f79eb9ea555955331fadab4b50b2faa92075`** (22:19:23Z; `a7e1224f…` at 22:17Z; `aea5eaaf…` red at ~22:16:45Z) |
| `examples/culture-d2/packet.d2.typed.yml` | `e8a83445e46deadde358e3ebb20c2d47decee91d3f2a1341d28ebfe6934e09bb` (22:18Z) |
| `examples/culture-d2/typed-gate.expected.json` | `7ed597317b32b238d880af0a602fcbfa1ffd92608008879f049db9fd02aa03aa` (22:18Z; `e962849a…` before the fix, §3.1) |
| `tools/gates/frozen/round-11/MANIFEST.tsv` | `4ddb911ced45288533b8f3dadc76a339b966f31611351a9b86645349d5904376` (22:18Z) |
| `tools/gates/naming-collision-gate.py` | `d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d` (22:02:46Z) |
| `tools/gates/costume-era-consistency-gate.py` | `e6bffd7020c0b1168828902853320bbf37e903457c83dae5477820aeceec478f` (22:02:46Z) |
| `reports/round-8/depth/skill-table-draft.md` | `0e9aca3a84ee4da360090ba921bdef9023f38c46dc47d7e7552fc8b0a1dbcac5` (22:02:46Z) |

### 8.3 Scratch captures (in-lane, remove-safe)

`d24-typed.json` `880d0e45…` · `d24-naming.out` `ebc8850d…` · `d24-replay.out`
`76c00a6b…` · `d24-emit.yml` `a3aa452c…` · `d24-tgf-e2e-green.txt` `204857cb…` ·
`d24-tgf-e2e-r3.txt` `204857cb…` (byte-identical across both green revisions) ·
`d24-replay-r11.out` `19252931…` · `d24-tgf.json` (the `--json` document of the
green run)

### 8.4 Poll record for the D-shard landings

60 s cadence per round rules (≤20 min), snapshots of `reports/round-11/depth/` plus
targeted `ls` of the implementation paths:

| stamp | observed |
|---|---|
| 22:00:55Z | `depth/` = `scribe.md` only (R11-D26) |
| 22:04:28Z | + `review-22.md`, `test-cli.md`, `test-interop-d3.md` |
| 22:06:15Z | + `design.md`, `frozen-records.md` (design = the binding contract, §5) |
| 22:07–22:08Z | + `design-review.md`, `neg-18.md`, `review-21.md`, `review-23.md`, `test-boundary.md`, `test-determinism.md`; `tools/exercise-handoff-e2e.py` (claim O, not this shard) |
| 22:08:21Z–22:12:39Z | **no implementation file yet**: `assemble-d2-typed.py`, `typed-pipeline-gate.py`, `expected-holds.json`, `tools/gates/frozen/round-11/MANIFEST.tsv` all absent |
| 22:13–22:16Z | + `shard-assembler.md`, `shard-gate-adapter.md`, `shard-holds.md`, `shard-validator.md`, `repin.md`, `neg-17.md`; then the implementation itself lands: `tools/typed-gate-flow.py` (red revision `aea5eaaf…`, then green `a7e1224f…`), `examples/culture-d2/packet.d2.typed.yml`, `examples/culture-d2/typed-gate.expected.json`, `tools/gates/frozen/round-11/MANIFEST.tsv` (10 rows), and the projection re-pin (`typed-labels.d2.yml` → `a3aa452c…`) |
| 22:17:16Z | e2e green (`10/10`), selftest `14/14`, round-11 replay `10/10` (this seat's runs) |
| 22:19:12–23Z | third tool revision `5758e315…`; re-run green with byte-identical stdout; git status: the re-pin + six filed earlier-round `validation.json` files modified (§7.5) |

Handoff state: the wiring exists, churns revisions within minutes, and was green at
the last two revisions measured. The integrator must re-run the row's commands at
whatever revision stands at integration; this seat pins only the revisions it
measured, each with its stamp.

## 9. Sources and locators

Repo-relative; earlier reads 22:00–22:03Z, wiring reads 22:14–22:19Z:

- `reports/round-11/claims.json` (claim D), `reports/round-11/targets.json` (R11-D01..D26)
- `reports/round-11/depth/design.md` §1.1–1.4, §2.2–2.3, §3.1–3.2, §4.2–4.5, §5.1–5.4, §6, §8
  (the binding contract §4/§5 restate)
- `reports/round-11/depth/repin.md` §0–§3 (re-pin mechanics; the round-11 manifest's
  10 rows), `shard-gate-adapter.md` §0–§1 (adapter contract, live differential,
  `A-STALE` refusal pre-re-pin), `shard-holds.md` §0 (TL-01/TL-02 → `D2L-*` mapping),
  `test-cli.md` §1, `review-22.md` §1.1 (the C1–C6 self-blessing threat model)
- `examples/culture-d2/ASSEMBLY.md:94`, `:85-87`; `examples/culture-d2/typed-labels.d2.yml:1-18`;
  `examples/culture-d2/typed-gate.expected.json`; `examples/culture-d2/packet.d2.typed.yml`
- `tools/typed-gate-flow.py` (CLI + `--selftest` output), `tools/gates/frozen/round-11/MANIFEST.tsv`
- `reports/round-8/depth/skill-table-draft.md:40,54-56,121,227,299-303,324,330`
  (the §7 limit and the 10/10 frozen count)
- `reports/round-8/depth/scribe.md` §5 (row format precedent), `§6.1`
- `reports/round-8/depth/test-replay.md` §0, §6 (re-pin precedent)
- `reports/round-11/depth/scribe.md` §1.1–1.2 (sibling baseline receipts)
- `corpus/knowledge/verification/gate-frozen-run-standard.md` (frozen-run shape)
- `PROVINCE.md`, `AGENTS.md` (write scope and evidence rules)
