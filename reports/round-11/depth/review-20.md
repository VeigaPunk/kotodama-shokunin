# R11-D20 — adversarial review: wiring vs `design.md` coherence

- seat: **R11-D20** (adversarial reviewer, wiring vs design spec), round 11 (loop 1 of 3,
  build round 4 of 4), 2026-10-17
- assignment (verbatim): "DEPTH R11-D20 (reviewer): wiring vs design.md coherence review;
  findings to reports/round-11/depth/review-20.md."
- writes: **this file only** (plus in-lane scratch under `.scratch/d20/`). No tool, gate,
  packet, component, projection, baseline, manifest, `reports/round-{8,9,10}/**` or other
  seat's round-11 byte is edited by this seat; every mutation control ran in an isolated
  copy under `.scratch/d20/`. No commit, no push.
- clock: stamps UTC (`date -u`); lane local time is UTC-03:00. **The wave was in flight while
  this file was written**; every statement is bound to the revision named beside it, and §1.3
  records the churn observed.
- canon: NON-CANON engineering review. Nothing here admits a round, a capability or a canon
  fact; the ten owed garment forms stay open design debt and lore's business.

## 0. Verdict (read first)

**The wiring satisfies design.md's substance and the depth claim's outcome.** At the reviewed
revision, `python3 tools/typed-gate-flow.py --flow` over `examples/culture-d2` exits **0** with
10/10 checks; the emitted finding set is 16 = **15 holds + 1 note + 0 fails** with the same
`(id, severity, where)` population design §4 names; the ten English glosses leave the sound
channel with **zero** PHON artifact naming an off-channel record and the differential is exactly
the ten `PHON-INVENTORY` removals; the ten owed slots are carried as named holds; the projection's
stale pin is closed at **exactly** design §5.1's predicted bytes; and the round-11 frozen
generation replays **10/10, exit 0**. The claim's counting command reads **claim D: PASS** in my
isolated copy at 22:18:35Z (claim F still red — another seat's scope, §7.3).

**But the landed wiring is not the wiring design.md specifies.** Ten divergences are recorded
below; four of them matter beyond bookkeeping (F2 mechanism, F3 `--check` blindness, F6 the
prescribed frozen location vs the battery, F10 the hold `where` canonicalization). None of them
makes the claim's four `after_required` legs false as measured; each needs the parent's explicit
disposition, because several round-11 fragments and the capability-row draft are written to the
design's interfaces, not the landed ones.

| id | severity | finding | owner of the disposition |
|---|---|---|---|
| F1 | medium | landed wiring is **one** tool (`tools/typed-gate-flow.py`), not the design's two (`tools/assemble-d2-typed.py` + `tools/gates/typed-pipeline-gate.py`); CLI surface differs; no manifest row pins the flow | parent / D05 |
| F2 | **high** | routing uses the gate's `compare_only` channel; design §2.3/§3.3 specified moving the checked field to `garment_gloss`, and round-8 `design-spec.md` §1.3 R3 names `compare_only` as **not** a licensed exemption channel | parent (design amendment or wiring change) |
| F3 | **high** | `--check` exits **0** with the committed expected baseline deleted (isolated-copy control); no selftest control covers it | D05 |
| F4 | medium | design §3.2's mandatory banner and §4.5's `EXPECTED_HOLDS` constant are absent | D05 / parent |
| F5 | low-med | design §2.2's "assembler identity" rule is not implemented as written (digest pins stand in for it) | parent |
| F6 | medium | design §5.2's prescribed baseline path (`tools/gates/expected/typed-pipeline/r11/`) trips the battery (`BASELINE-GATE-UNKNOWN`, simulated); the landed manifest idiom avoids it | parent (record the deviation as deliberate) |
| F7 | low | design §5.2's "green" recipe omits that replay needs a `TMPDIR` outside the repo; in-lane it reads 10/10 `mirror_unsafe`, exit 2 | parent (acceptance recipe) |
| F8 | resolved | at 22:17Z the counting command found no e2e evidence (claim D FAIL); the tool gained `--flow/--e2e/--typed-flow/--wired-flow` at 22:18Z and claim D then read PASS | closed — record the coupling |
| F9 | low | the rank holds carry `code: R-RANK-CONFLICT` while design §4.2's column names the `id` `D2L-RANK` | parent (keying note) |
| F10 | medium | the ten label holds' `where` is canonicalized from the record id (`GAR-01`) to the owed slot (`LEX-GAR-01`); design §4.2/§4.4 name the record id | parent / D05 |

## 1. Subject, pins, method

### 1.1 The objects reviewed

| artifact | sha256 at review close (22:19:28Z) | note |
|---|---|---|
| `reports/round-11/depth/design.md` | `addd0ea2ecf71871621814aa5917347ae6503d0040bcf64c31cae0f4baa69c49` | the spec under review (459 lines) |
| `tools/typed-gate-flow.py` | `5758e315593bb818dbf38c3c3ed7f79eb9ea555955331fadab4b50b2faa92075` | the wiring, 827 lines, R11-D05; stable 22:18:09→22:19:28Z |
| `examples/culture-d2/packet.d2.typed.yml` | `e8a83445e46deadde358e3ebb20c2d47decee91d3f2a1341d28ebfe6934e09bb` | derived typed packet |
| `examples/culture-d2/typed-gate.expected.json` | `7ed597317b32b238d880af0a602fcbfa1ffd92608008879f049db9fd02aa03aa` | committed expected set (design called it `expected-holds.json`) |
| `examples/culture-d2/typed-labels.d2.yml` | `a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43` | re-pinned projection; **byte-equal to design §5.1's prediction** |
| `examples/culture-d2/packet.d2.yml` | `e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643` | base packet, unchanged through the wave |
| `tools/d2-typed-labels.py` | `0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802` | projector, unchanged in round 11 |
| `tools/gates/frozen/round-11/MANIFEST.tsv` | `4ddb911ced45288533b8f3dadc76a339b966f31611351a9b86645349d5904376` | new frozen generation, 10 rows |

### 1.2 Method

1. Read `design.md` in full, extracted its normative statements (interfaces, legs L1–L4, the
   expected hold set §4, freeze/verification mechanics §5) and the authorities it cites.
2. **Re-ran every measurement `design.md` records**, sha-for-sha, before accepting any statement
   of it (§2).
3. Read the landed wiring's bytes and diffed its actual interfaces/mechanism against the spec
   (§3, §4).
4. Ran the claim's legs and the counting command in **isolated copies** (`cp -r tools examples
   [corpus|reports] .scratch/d20/iso*`), so no lane artifact was written by this review, and
   mutation controls (delete/tamper) could run without touching the lane (§6).
5. Cross-read the sibling fragments only to avoid double-filing and to date the churn
   (`reports/round-11/depth/{review-21,review-22,design-review,repin,frozen-records,test-e2e}.md`);
   their conclusions are theirs, not reused as evidence here.

### 1.3 Revision churn observed during the review (report, do not compare across)

| stamp (UTC) | `tools/typed-gate-flow.py` | committed expected set | observation |
|---|---|---|---|
| 22:11:56 | (artifact written) | `typed-gate.expected.yml` | the expected set first landed as **YAML** at `examples/culture-d2/typed-gate.expected.yml` |
| 22:12:52 | `d97fcfa5…` | (missing) | `EXPECTED_DEFAULT` pointed at `.json`; the default run exited 1 `FAIL expected-present`, and passing the `.yml` exited 1 `expected-parse` ("not valid JSON") |
| 22:13:37 | `ae55e6fa…` | `e962849a…` (`.json`) | e2e green, 10/10; hold `where` = `GAR-01..10` |
| 22:18:09 | `5758e315…` | `7ed59731…` | **reviewed revision**: hold `where` canonicalized to `LEX-GAR-01..10`, record kept in `record`; `--flow/--e2e/--typed-flow/--wired-flow` added |

Consequence for every reader: round-11 fragments that pinned the earlier bytes (e.g.
`test-e2e.md` pins `typed-gate.expected.json e962849a…` and its T1–T4 equality under the then-current
key) are **revision-bound**; the parent's integration run must re-verify equality against
`7ed59731…`, not against the fragment's quoted hashes.

## 2. `design.md`'s measured claims, independently reproduced

All commands run from the lane root; scratch-writing commands with `export TMPDIR=$PWD/.scratch`.
No design claim in this table failed reproduction.

| design claim | my command | result (mine) | design's recorded value |
|---|---|---|---|
| §1.1 legacy naming run | `python3 tools/gates/naming-collision-gate.py examples/culture-d2/packet.d2.yml` | exit 1, 17 lines, stdout `ebc8850d…`; PHON-INVENTORY 10 / NAME-NEAR 6 / CROSS-HOLD 1 | identical (`design.md:31`) |
| §1.2 typed populations | `python3 tools/d2-typed-labels.py --json` | `{labels: 58, hold: 15, note: 1, fail: 0}`; `translated-label 10 / native-form 46 / borrowed-strata 2` | identical (`:47-52`) |
| §1.3 experiment 1 (GAR-01 routed) | `.scratch/d20/route-experiments.py` (byte-copy rename `garment:`→`garment_gloss:` in the GAR-01 record only) | naming 17→16 lines, PHON 10→9, stdout `842d606a1cc2d6ffb1c5368a90f75e69ff399f3d662dd47748d1bd2a7124505c`; every other line identical | identical (`:64-65`) |
| §1.3 experiment 2 (all ten routed) | same script | naming 7 lines (NAME-NEAR 6, CROSS-HOLD 1), PHON ×0, stdout `feb6488127f115f986bf7602c0b074ce911c951751e5e2c63e32e5d23bb52bd9` | identical (`:66-68`) |
| §1.3 other four gates unchanged | same script | phonology `1ce5f0cd…`; lexicon, myth, costume each 0 bytes / `e3b0c442…` (empty) — identical across legacy/GAR-01/all-routed | identical (`:70-72`) |
| §1.4 stale projection pin | `python3 tools/d2-typed-labels.py --check` (pre-re-pin) | exit 1 "differs from the deterministic projection"; one differing line `assembly.packet_sha256 8da90b07…` vs packet `e0f21509…` | identical (`:79-84`) |
| §1.4 round-3 replay | `python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv` | exit 2, 7/7 `could-not-evaluate reason=gate_digest_mismatch` | identical (`:85-91`) |
| §4.2/§4.3 expected set | projector `--json` findings, triples `(id, severity, where)` | 15 holds: `D2L-FORM-UNRESOLVED`×10 (GAR-01..10), `D2L-NATIVE`×2 (L-15, L-16), `D2L-RANK`×3 (`TR-04#a\|TR-06#a`, `WR-02#g\|WR-09#g`, `WR-08#g\|WR-09#g`); note `D2L-RANK` `SR-01#a\|SR-01#b`; fail ∅ | identical (`:252-283`) |
| §5.1 re-pin prediction | `python3 tools/d2-typed-labels.py --emit .scratch/d20/proj-emit.yml` | 3010 lines, sha `a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43`, single differing line `assembly.packet_sha256` | identical (`:320-321`) |
| §5.4 pre-wire baseline | `assemble-d2.py --check`; `d2-typed-labels.py --selftest`; `assemble-culture-d3.py --check`/`--selftest`; `check-gate-battery.py` | exit 0; 39/39; exit 0 and 85/85; exit 2 `{pass: 7, fail: 0, unevaluable: 0, findings: []}` + 5 baselines pinned, 2 gates uncovered | identical (`:373-378`) |
| §5.2 landed generation replays green | `TMPDIR=/var/tmp/r11d20 python3 tools/replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv` | exit 0, `REPLAY OK: 10/10 rows reproduced` | design predicted this shape; see F1/F6/F7 |

Two design-side risks I checked and found **sound**:

- **The §1.3 mechanism claim is not over-read.** The design says the differential is "exactly the
  ten `PHON-INVENTORY` lines … no cascade, no new finding, no lost finding". Reproduced
  line-for-line: `17 − 10 = 7`, and the other four gates are byte-identical between the legacy and
  routed packets.
- **The re-pin is not self-referential in its *value*.** §5.1's predicted digest was recorded before
  the artifact moved and the moved artifact hash equals it. (Whether the *set* it is compared against
  blesses itself is `review-22.md`'s circularity audit, not this file's.)

## 3. Wiring vs `design.md`, item by item

### F1 (medium) — the landed interface is not the specified interface

`design.md:123` names the adapter `tools/assemble-d2-typed.py`, `:179` names the gate
`tools/gates/typed-pipeline-gate.py`, and `:406-407` maps them to seats D03/D04 and D05. Landed:

```sh
ls tools/assemble-d2-typed.py tools/gates/typed-pipeline-gate.py examples/culture-d2/expected-holds.json
# all three: No such file or directory (22:19Z)
```

One tool, `tools/typed-gate-flow.py`, does both jobs and self-describes as "the D2 typed-pipeline
wiring (round 11, R11-D05)". Consequences, all measurable:

- design §2.2's adapter contract (`--packet/--projection/--emit PATH/--check [PATH]/--selftest`) and
  §3.1's gate entry (`[PACKET]`, `--json`) do not describe the landed CLI
  (`--packet --typed-packet --expected --typed-override --json --flow/--e2e --emit --check
  --freeze [DIR] --selftest`; `--emit`/`--check` take no path).
- design §3.1's L1–L4 are implemented, but as checks with different ids (`typed-packet-pinned`,
  `sound-channel-clean`, `differential-exact`, `owed-slots-crosscheck`, `hold-set-equal`,
  `expected-pins`, `expected-delta-match`, `expected-verdicts-match`, `expected-file-current`), not
  as named legs — a reader tracing L1→L4 cannot grep for them.
- design §5.2 wanted the new frozen baseline to pin "the typed-pipeline gate" with
  `gate_sha256 of the typed-pipeline gate` and a row `gate=tools/gates/typed-pipeline-gate.py,
  exit_code=0, finding_count=15` (`:345-347`). The landed generation instead records **10 rows = the
  five culture gates × {typed, legacy}** (`MANIFEST.tsv` row list verified; the five typed rows
  carry exit 1/1/0/0/0 and counts 7/3/0/0/0, the legacy rows 17/3/0/0/0). No row names the flow:
  `grep -c "typed-gate-flow" tools/gates/frozen/round-11/MANIFEST.tsv` → **0**, while
  `tools/gates/frozen/round-11/typed-gate-flow.out` (2197 B, the flow's own stdout) sits in the
  generation **unreferenced and unpinned** — the one file in a frozen generation with no digest row
  (standard §3's "every file … the gate reads" discipline, cf. `analysis`-free but inconsistent with
  the generation's own indexing).
- Everything that keyed to the design's paths (`capability-draft.md:137-141`, `neg-18.md:142-144`,
  `test-boundary.md:14`, `scribe.md:73`) is stale as written. That is a *reporting* defect of the
  wave, not of the tool.

### F2 (high) — the routing mechanism is the one the round-8 spec names as unlicensed

design §2.3 row 1 says the `translated-label` record's "checked field [is] moved to `*_gloss`", and
§3.3 says explicitly "The **wiring needs no gate edit**: routing the record off the checked field
removes the finding at the source (`§1.3`)". The landed typed packet does **not** rename the field:

```sh
grep -c garment_gloss examples/culture-d2/packet.d2.typed.yml     # 0
grep -n "typed_label_kind\|compare_only\|owed_form" examples/culture-d2/packet.d2.typed.yml | head -3
# 1882: typed_label_kind: "translated-label"
# 1883: compare_only: true
# 1884: owed_form: "LEX-GAR-01"
```

The ten records keep `garment:` and are marked `compare_only: true` — the gate's own
key-equivalence skip (`tools/gates/naming-collision-gate.py:223` declares the field; the skip sites
are `:1045`, `:1090`, `:1121`, `:1154`). Against the authority the design itself cites:

> **R3** … `compare_only` is therefore **not** a licensed exemption channel for typed labels; a
> record setting it while unresolved is `D2L-SCOPE` (misuse), not a pass (the gate's own
> `compare_only` skip sits at `tools/gates/naming-collision-gate.py:1097-1098`).
> — `reports/round-8/depth/design-spec.md:163-169`

and `examples/culture-d2/ASSEMBLY.md:94`: the unresolved LEX-GAR slots "are not silently filled or
bypassed with `compare_only`".

**Mitigation, measured — this is not a silent pass.** The same tool carries the holds by name
(`owed_form: LEX-GAR-0x` on each record; finding `D2L-FORM-UNRESOLVED` per owed slot), cross-checks
declared owed slots against the holds (`owed-slots-crosscheck` ok), asserts no PHON artifact names an
off-channel record (`sound-channel-clean` ok, `off = GAR-01..GAR-10`), and pins the differential
(`differential-exact` ok: 10 removed, 0 added, retained lines identical). So the claim's requirement
("owed native forms are carried as named holds (not PHON artifacts)") is *satisfied by evidence*, while
the *mechanism* is the channel the round-8 spec forbids by name. Both readings are defensible; the
parent must decide, because `design.md` (this round's contract) and `design-spec.md` (the standing
authority it cites) disagree with the landed bytes here.

### F3 (high) — `--check` is blind to a deleted expected baseline

Isolated copy (`.scratch/d20/iso2`, refreshed to the reviewed revision), expected set moved away:

```sh
mv examples/culture-d2/typed-gate.expected.json ../exp-removed.json
python3 tools/typed-gate-flow.py --check     # exit 0: "typed gate artifacts: byte-identical deterministic derivation"
python3 tools/typed-gate-flow.py             # exit 1: FAIL expected-present — missing: examples/culture-d2/typed-gate.expected.json
```

`--check` computes drift over only two check ids (`typed-packet-pinned`, `expected-file-current`) and
`expected-file-current` is only created when the expected file exists
(`tools/typed-gate-flow.py:755-763` at `ae55e6fa…`; same shape at `5758e315…`), so **"expected set
absent" and "expected set unparseable" are invisible to `--check`** while the default run is red.
Controls that *do* work, verified in the same copy: typed packet removed → `--check` exit 1; one byte
appended to the typed packet → `--check` exit 1. The tool's selftest contains no missing-expected
control (its controls are: mirrored e2e, repeat-run byte-identity, `--check` on pinned bytes, `--json`,
typed-packet tamper/restore, smuggled label, dropped owed form, laundered hold, unparseable expected,
malformed packet, missing packet — 14/14 pass).

Why it matters beyond the tool: fragments cite `--check` exit 0 as the typed artifacts' pin evidence
(`frozen-records.md:23`), and a green `--check` receipt over a tree whose expected baseline is missing
is exactly the laundering shape the round's negative controls are meant to exclude. Cheapest fix
(owner's call; **not applied by this seat**): add `expected-present` and `expected-parse` to
`--check`'s drift set, and add the deletion control to `--selftest`.

### F4 (medium) — the design's mandated banner and embedded constant are absent

`grep -n "TYPED-PIPELINE\|EXPECTED_HOLDS" tools/typed-gate-flow.py` → **0 matches** at the reviewed
revision. design §3.2 (`:205-217`) requires the banner *"TYPED-PIPELINE: exit 0 = the emitted findings
equal the frozen expected hold set; every hold below is still open design debt"* before the finding
lines; the landed report opens with `typed-gate-flow — D2 typed pipeline (R11-D05)` and prints
`findings: 16 (hold 15, note 1)` plus the 15 `[hold]` lines verbatim (form `FINDING <code>:
[<severity>] <where> — <detail>` — design §3.2's format is matched). design §4.5 (`:310-311`) requires
the gate's `--selftest` to assert an embedded `EXPECTED_HOLDS` constant equal to the committed file
"both directions"; the landed tool instead compares the observed findings to the committed file at run
time (`hold-set-equal`) and checks the file is the deterministic derivation
(`expected-file-current`) — arguably stronger (no duplicate constant to drift), but it is a departure
from a normative clause and should be recorded as such, not read as compliance.

### F5 (low-medium) — assembler identity is done by digest pin, not by re-derivation

design §2.2 (`:133`) requires the adapter to verify that `--packet` bytes equal `assemble-d2.py`'s
deterministic assembly "call the assembler's own build path; do not re-implement", exit 2 on failure.
The landed tool loads `tools/assemble-d2.py` **only** for its serializer (`SERIALIZER` at `:69`, used
at `:298-299` for `yaml_lines`); it never calls the assembler's build path. Fail-closed effect is
preserved differently: the packet's digest is pinned in the committed expected set
(`packet_sha256`) and any packet change fails `expected-pins` (exit 1, not 2). Equivalent for a
hand-edited packet; weaker in that the pin lives in the file a re-pin rewrites, and the exit code
differs from the design's (1 vs 2). Likewise the design's "projection freshness" rule (call
`d2-typed-labels.py --check`; stale pin is a hard error, `:134`) is not called: the flow re-runs the
projector in-process. In the event the committed projection **was** re-pinned and is fresh
(`--check` exit 0, `a3aa452c…`).

### F6 (medium) — the prescribed frozen location would trip the battery; the landed one does not

design §5.2 (`:332`) puts the new revision under `tools/gates/expected/typed-pipeline/r11/` — inside a
battery baseline root. Simulated in an isolated tree (`.scratch/d20/sim`, a full `tools/`+`examples/`
copy plus a stand-in `expected.json` at exactly that path declaring `gate: typed-pipeline-gate.py`):

```
BASELINE-GATE-UNKNOWN — declared gate 'typed-pipeline-gate.py' is not one of the seven registered
gates      (baseline reading: no baseline; gate: None)
```

because `tools/check-gate-battery.py:92-100` fixes `GATE_NAMES` to the seven registered gates and
resolves every baseline against it. The landed implementation avoided this by choosing the legacy-TSV
generation idiom under `tools/gates/frozen/round-11/` (no `expected.json` → nothing for the battery's
baselines duty to read). Measured live at 22:16:07Z, default roots: battery `{pass: 7, fail: 0,
unevaluable: 0}`, inner `5 baselines found / 5 pinned`, uncovered `{myth, naming}` — i.e. **exactly
design §5.4's predicted unchanged state**. So the design's §5.4 claim holds *only because the
implementation deviated from §5.2*. The parent should record the deviation as deliberate, not repair
it back to the prescribed path (which would need a battery co-change — `review-22.md`'s C4 pattern).

### F7 (low) — the "green" replay recipe omits an environment condition

```sh
TMPDIR=$PWD/.scratch python3 tools/replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv
# exit 2; 10/10 could-not-evaluate reason=mirror_unsafe ("temporary root is inside the repo")
TMPDIR=/var/tmp/r11d20 python3 tools/replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv
# exit 0; REPLAY OK: 10/10 rows reproduced
```

design §5.2 states the green condition as the bare command (`:348-349`); the lane's standing rule
exports `TMPDIR` **inside** the repo, under which every manifest reads `mirror_unsafe`. The condition
is corroborated by three sibling fragments (`repin.md` §6.5, `frozen-records.md` §6.5, `test-e2e.md`
§5.7); this file measures it independently. The parent's acceptance run must use an out-of-repo
`TMPDIR` (or `--repo-root` on a mirror) and say so in the round report, or a green generation reads
red.

### F8 (resolved during the review) — e2e discovery was red, then green

At 22:17Z, the claim's counting command run in a refreshed isolated copy read:

```
claim D: FAIL — e2e: no round-11 e2e evidence found — no JSON receipt under reports/round-11 with
command + expected_holds, no wired flow (--e2e/--flow) tool, no documented e2e command in
reports/round-11/depth/design.md
```

Cause, verified: the flow's CLI had no `--e2e/--flow/--typed-flow/--wired-flow` alias
(`reports/round-11/run-validation.py:808-813` is the runner's predicate), no committed JSON receipt
under `reports/round-11/` carried `command` + an expected-holds key, and `design.md` contains no bare
`python3 …` e2e line (`grep -n "e2e" design.md` → `:120` prose only). At 22:18:09Z the tool gained
exactly those four flag aliases (`help="… accepted as an explicit flag for round-11 runners"`,
`tools/typed-gate-flow.py:775-778`), and **claim D then read PASS** in my refreshed isolated copy at
22:18:35Z. Recorded because it shows the D-evidence leg is coupled to a *discovery surface*, not to
the wiring's correctness — a future change to either the runner's predicate or the CLI's flags must be
co-checked.

### F9 (low) — `code: R-RANK-CONFLICT` vs the design's `id: D2L-RANK`

design §4.2's "finding id" column names `D2L-RANK` for the four rank entries; the committed expected
set and the flow's set comparison key on the projector's `code`, which is `R-RANK-CONFLICT` for those
entries (`examples/culture-d2/typed-gate.expected.json` `expected_findings`: 10×`D2L-FORM-UNRESOLVED`
+ 2×`D2L-NATIVE` + 3×`R-RANK-CONFLICT` hold + 1×`R-RANK-CONFLICT` note). The round-8 spec's own §8.1
note ("ids are names, the classes in §6 are the contract"; the projection carries both `id` and
`code`) makes this coherent, but the round-11 design does not say which field the equality is on, so
a reader comparing against §4.2's table will see a mismatch on four rows.

### F10 (medium) — the ten label holds' `where` was canonicalized to the owed slot

At the reviewed revision the projector's label holds (`where: GAR-0x`) are rewritten by the flow to
`where: LEX-GAR-0x` with the record id preserved in a new `record` field
(`tools/typed-gate-flow.py:275-285`), and the emitted line carries both
(`FINDING D2L-FORM-UNRESOLVED: [hold] LEX-GAR-01 (GAR-01) — label_id LEX-GAR-01 …`). design §4.2/§4.4
(`:252-295`) names the *record* (`GAR-0x`) as the `where` of rows 1–10 and fixes the comparison key
as `(id, severity, where)`. The canonicalization is internally consistent (expected file and emitted
set agree, `hold-set-equal` ok, `expected-file-current` ok) and arguably better (the debt is the
missing form, named by its slot), but it is a design divergence, and it is the reason fragments
pinned to `e962849a…` no longer describe the current bytes (§1.3).

## 4. The claim's core: "findings exactly equal to the expected hold set"

Measured at the reviewed revision, both sides read from live bytes:

- emitted: `python3 tools/typed-gate-flow.py --flow` → `findings: 16 (hold 15, note 1)`, exit 0,
  10/10 checks, stdout sha256 `204857cbb84d49cf39b51272651451609fa9a5ad29f4befdc712b07067d1f181`;
- committed: `typed-gate.expected.json` `7ed59731…` → `expected_findings` 16 rows
  (10 `D2L-FORM-UNRESOLVED` hold / 2 `D2L-NATIVE` hold / 3 `R-RANK-CONFLICT` hold /
  1 `R-RANK-CONFLICT` note), `off_sound_channel` = the ten GAR records, `owed_slots` =
  `LEX-GAR-01..10`, pins `packet_sha256 e0f21509…` and `typed_packet_sha256 e8a83445…`;
- equality is checked on the full `(code, severity, where, detail)` tuple
  (`finding_key`, `:236`), i.e. stricter than design §4.4(1)'s triple and consistent with §4.4(3)'s
  "detail strings are pinned too"; the set equality passed (`hold-set-equal` ok), as did
  `expected-delta-match` (the per-gate differential) and `expected-verdicts-match` (per-gate exit +
  finding count + stdout digest).

Design §4's population choice (the projector's **top-level** `findings`, not the nested
`era_material_reconciliation.findings`) is implemented as specified. The nested population — nine
`R-MAT-BRIDGE-MISSING` holds that never surface in `/findings` — is therefore **outside** the compared
set; that is `design-review.md` DR-01's finding (scoped there to the population/severity question),
and it is reproducible: the projection document carries 9 nested holds the top-level list does not.
This review does not re-file it; it notes only that the wiring implements the design's choice
faithfully, so if the parent revises the population, the adapter's `expected_findings` derivation is
where the change lands.

## 5. Claim-D legs at my stamp

| leg (claims.json D `after_required`) | measurement | state |
|---|---|---|
| assembler or documented adapter consumes typed labels | `python3 tools/assemble-d2.py --check` exit 0 (packet unchanged); adapter step documented in the tool's docstring + `typed_view` block; no assembler edit | met (via the documented adapter step the claim allows) |
| gates evaluate the typed packet; translated labels never on the sound channel | typed-run `off=GAR-01..GAR-10`; `sound-channel-clean` ok; differential `naming 17→7, removed 10, added 0`, other gates unchanged | met |
| owed native forms carried as named holds, not PHON artifacts | 10 `D2L-FORM-UNRESOLVED` holds naming `LEX-GAR-0x`; `owed-slots-crosscheck` ok; typed-run PHON-INVENTORY lines naming off-channel records: 0 | met |
| e2e over `examples/culture-d2` exits 0, findings == expected set exactly | exit 0, 10/10 checks, hold set equal (§4) | met |
| frozen replay re-pinned and green | `frozen/round-11/MANIFEST.tsv` `4ddb911c…`, 10/10 reproduced exit 0 — **with an out-of-repo TMPDIR** (F7) | met, conditioned |
| d2/d3 selftests + battery remain green | `d2-typed-labels.py --selftest` 39/39 exit 0; `assemble-culture-d3.py --selftest` 85/85 + `--check` exit 0; battery `{pass: 7, fail: 0}`, default-root coverage gap unchanged (5 pinned, 2 uncovered) | met |
| counting command `python3 reports/round-11/run-validation.py` | isolated copy, 22:18:35Z: **claim D: PASS** (claim O: PASS; claim F: FAIL — other seats' scope) | met at that stamp |

## 6. Falsification receipts (this seat's own runs)

```sh
export TMPDIR=$PWD/.scratch                      # lane rule; TMPDIR=/var/tmp/r11d20 only where noted
# design §1.1/§1.3 reproductions (route-experiments.py renames garment: in byte copies)
python3 .scratch/d20/route-experiments.py        # 15 gate runs, shas as §2
# projection re-pin prediction
python3 tools/d2-typed-labels.py --emit .scratch/d20/proj-emit.yml   # exit 1 (findings), sha a3aa452c…
# stale pin, then post-re-pin
python3 tools/d2-typed-labels.py --check         # exit 1 pre-re-pin → exit 0 at 22:13Z ("byte-identical")
# round-3 divergence and the new generation
python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv   # exit 2, 7/7 gate_digest_mismatch
TMPDIR=/var/tmp/r11d20 python3 tools/replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv  # exit 0, 10/10
# battery, default roots (22:16:07Z) and the §5.2 stand-in simulation
python3 tools/check-gate-battery.py              # exit 2; pass 7 / fail 0; 5 baselines pinned; 2 uncovered
python3 .scratch/d20/sim/tools/check-gate-battery.py   # +BASELINE-GATE-UNKNOWN on the stand-in baseline
# wiring e2e and controls
python3 tools/typed-gate-flow.py --flow          # exit 0, 10/10, stdout sha 204857cb…
python3 tools/typed-gate-flow.py --check         # exit 0
python3 tools/typed-gate-flow.py --selftest      # exit 0, 14/14
# mutation controls, isolated copy (.scratch/d20/iso2, tool copied to the reviewed revision)
#   expected baseline deleted  → --check exit 0 (F3) / default run exit 1 expected-present
#   typed packet deleted       → --check exit 1 typed-packet-pinned
#   typed packet +1 byte       → --check exit 1 typed-packet-pinned
# claim counting command, isolated copy (.scratch/d20/iso3), 22:18:35Z
python3 reports/round-11/run-validation.py       # exit 1; claim D PASS / claim O PASS / claim F FAIL
```

## 7. Residual risk, limits, and to-verify

1. **Churn.** `tools/typed-gate-flow.py` and the expected set changed twice during this review
   (§1.3). Every finding above was re-verified at `5758e315…` except F8, which is explicitly
   stamp-scoped, and F1's path absence, re-checked at 22:19Z. A later edit invalidates this file's
   §3 verdicts: re-read, never compare across revisions.
2. **`design.md` itself is not amended.** The design still prescribes two files, the field-move
   mechanism, the `expected-holds.json` name/schema, the `expected/typed-pipeline/r11/` location and
   the banner/constant. The round cannot claim "wiring conforms to design" as written; it can claim
   (and I measured) that the wiring satisfies the *claim's* legs. `to-verify` for the parent's
   integration decision.
3. **Claim F and parts of O** read red in my 22:18Z isolated run (recheck receipts). Out of this
   seat's scope; named so the parent does not read my "claim D: PASS" as a round verdict.
4. **The nine nested `R-MAT-BRIDGE-MISSING` holds** stay outside the compared set by design
   (§4); if that population is revised, the expected-set derivation is the change point.
5. **Unpinned artifact inside a frozen generation** (`typed-gate-flow.out`, F1) — the parent may
   prefer a manifest row (or its removal) in the integration pass.
6. **I did not re-run the frozen generation's own `--freeze`** (it writes into
   `tools/gates/frozen/round-11/`, owned by D08/D05); I verified the landed bytes replay instead.
   Whether a re-freeze is needed after the 22:18Z tool edit is for the owners: the manifest pins the
   five gate scripts, not the flow, so the tool edit does not invalidate those rows — but the
   generation's `typed-gate-flow.out` is now the output of a *superseded* tool revision.

Out of province (report, never absorb): canon status of the ten owed garment forms (lore), whether a
real project would license an English gloss as an in-world name (lore), any real-world-language claim
about the glosses (not asserted here, none verified), and the game-side or rights questions
(`PROVINCE.md`).

## 8. Sources and receipts

All paths repo-relative; digests read with `sha256sum` at the stamps named. Scratch receipts under
`.scratch/d20/` (gitignored): `route-experiments.py` + `.log`, `proj-emit.yml`, `flow-e2e-v3.out`,
`flow-selftest.out`, `replay-r11-vartmp.out`, `replay-round3-vartmp.out`, `battery-r11b.out`,
`iso-A2-check.out`, `iso-A2-e2e.out`, `iso3-validation-3.out`, `sim/`, `iso2/`, `iso3/`.

Read for the review: `reports/round-11/depth/design.md` (contract), `reports/round-8/depth/design-spec.md`
§1.3/§6, `reports/supplement-opencode-1/22-label-representation.md` §1/§2, `examples/culture-d2/ASSEMBLY.md:94`,
`corpus/knowledge/verification/gate-frozen-run-standard.md` §3–§6, `tools/check-gate-battery.py:92-100,300-470`,
`tools/gates/naming-collision-gate.py`, `tools/replay-frozen.py` (pin-before-run), and — for boundaries
only, not as evidence — `reports/round-11/depth/{review-21,review-22,review-23,design-review,repin,frozen-records,test-e2e,capability-draft}.md`.

No web retrieval was used; every claim is a repository file, a command output, or a receipt above.
Claims I could not settle are marked `to-verify` (§7.2, §7.6).
