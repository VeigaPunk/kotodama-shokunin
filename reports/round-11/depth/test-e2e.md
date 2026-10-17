# R11-D09 — test e2e: the wired typed pipeline over `examples/culture-d2`

- seat: **R11-D09** (test shard, claim D), round 11 (loop 1 of 3, build round 4 of 4), 2026-10-17
- assignment (verbatim): "DEPTH R11-D09 (test e2e): run the e2e command over examples/culture-d2;
  exit 0; findings exactly == expected hold set; reports/round-11/depth/test-e2e.md."
- writes: this file only (plus in-lane scratch under `.scratch/d09/`). No tool, packet, component,
  gate, baseline or earlier-round byte is edited by this seat; `reports/round-{8,9,10}/**` are filed
  and read-only here.
- canon: NON-CANON engineering evidence. A hold is a hold; nothing here admits a round, a capability
  or a canon fact.
- revision note: first filed against tool revision `ae55e6fa…` (exit 0, 10/10, `where=GAR-0x`); this
  revision records the **settled** tool `5758e315…` (§5.6 keeps both receipts). The wave was in flight
  throughout; every result is pinned to the revision stated beside it.

## 0. Verdict

**GREEN at the settled tested revision.** `python3 tools/typed-gate-flow.py` over
`examples/culture-d2` (the wired e2e entry, R11-D05) exits **0** with **10/10 checks passed**, and
the emitted finding set equals the **landed** committed expected set exactly:

- e2e run (22:19–22:20Z, tool `5758e315…`): exit 0; stdout sha256
  `204857cbb84d49cf39b51272651451609fa9a5ad29f4befdc712b07067d1f181` (49 lines); stderr empty;
  10 `ok` checks; `summary: 10/10 checks passed`; three consecutive runs byte-identical.
- findings: 16 = **15 holds + 1 note + 0 fails**; hold/note lines emitted verbatim (15 `[hold]`,
  1 `[note]`), counts `hold=15 note=1 fail=0` in the emitted set, the committed
  `typed-gate.expected.json` and the independent projector alike.
- equality (my harness, four checks T1–T4 over captured JSON): emitted == committed expected set
  (tool canonical key) **PASS**; counts **PASS**; emitted == the design's §4.2/§4.3 names in
  `(id, severity, where)` for 6 of 16 rows and in `(id, severity, record)` for all 16 — the ten
  `D2L-FORM-UNRESOLVED` holds are emitted with `where=LEX-GAR-0x` + `record=GAR-0x` where the design
  table and the independent projector name `where=GAR-0x` (**drift finding, §3.2 — D20/D21**).
- supporting legs at the same stamp: `tools/d2-typed-labels.py --check` exit 0 (projection re-pinned
  to the design's predicted `a3aa452c…`), `tools/assemble-d2.py --check` exit 0, projector
  `--selftest` 39/39 exit 0, `typed-gate-flow.py --check` exit 0 (byte-identical derivation).
- conditional caveat (environmental, not a verdict): replay of the round-11 frozen generation needs a
  `TMPDIR` outside the repo; with the lane's in-repo `.scratch` root it reads `mirror_unsafe` (§5.7).

## 1. Method, pins, environment

All commands ran in the lane repo root with `export TMPDIR=$PWD/.scratch` (standing round rule;
`/tmp` inode exhaustion is historical), all scratch under `.scratch/d09/`. Stamps are UTC; lane
local time is UTC-03:00. Pins as read at 22:19–22:20Z (the settled revision):

| artifact | sha256 | note |
|---|---|---|
| `tools/typed-gate-flow.py` | `5758e315593bb818dbf38c3c3ed7f79eb9ea555955331fadab4b50b2faa92075` | e2e entry, R11-D05; stable across 22:19–22:20Z runs |
| `examples/culture-d2/packet.d2.yml` | `e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643` | assembler output, unchanged in the wave |
| `examples/culture-d2/typed-labels.d2.yml` | `a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43` | **re-pinned** during the wave (was `e70ba147…`); matches design §5.1's prediction exactly |
| `examples/culture-d2/packet.d2.typed.yml` | `e8a83445e46deadde358e3ebb20c2d47decee91d3f2a1341d28ebfe6934e09bb` | committed typed packet (new, R11-D05) |
| `examples/culture-d2/typed-gate.expected.json` | `7ed597317b32b238d880af0a602fcbfa1ffd92608008879f049db9fd02aa03aa` | committed expected set, re-emitted 19:17:05 local (`--check` exit 0) |
| `tools/d2-typed-labels.py` | `0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802` | projector, unchanged in the wave |

The e2e command is the tool's default invocation — the design's "end-to-end command over
`examples/culture-d2`" (design.md §3.2, claim D c4):

```sh
python3 tools/typed-gate-flow.py                 # e2e; exit 0 = every check passes
python3 tools/typed-gate-flow.py --json          # one JSON document
python3 tools/typed-gate-flow.py --check         # byte-compare the derived artifacts; writes nothing
```

Harness: `.scratch/d09/verify-exact2.py` (my scratch; not a deliverable) runs the four equality
tests T1–T4 against captured JSON. Captured inputs at the settled revision: `.scratch/d09/e2e.json`
(flow `--json`, sha `121e8c8ca62d7572bfdcd817f469e4cdae711e4b798964744cd6a7f0eeb69f8b`),
`.scratch/d09/final{2,3,4}.out` (plain stdout, all `204857cb…`), `.scratch/d09/typed-live2.json`
(projector live `--json`, exit 1 its contracted verdict with holds) and `.scratch/d09/det-{1,2}.out`.

## 2. The e2e run

```sh
export TMPDIR=$PWD/.scratch
python3 tools/typed-gate-flow.py > .scratch/d09/final3.out 2>&1; echo $?
# 0
sha256sum .scratch/d09/final3.out
# 204857cb…   (49 lines; empty stderr)
```

Header, the re-named hold lines and the tail of the captured stdout:

```
typed-gate-flow — D2 typed pipeline (R11-D05)
packet: examples/culture-d2/packet.d2.yml e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643
typed packet: examples/culture-d2/packet.d2.typed.yml e8a83445e46deadde358e3ebb20c2d47decee91d3f2a1341d28ebfe6934e09bb
sound channel: off=GAR-01,…,GAR-10 on=0 untyped=none
FINDING D2L-FORM-UNRESOLVED: [hold] LEX-GAR-01 (GAR-01) — label_id LEX-GAR-01 has no supplied native/borrowed form
…  (10 of these, LEX-GAR-01..10 with the record in parentheses; then 2 D2L-NATIVE + 4 R-RANK-CONFLICT lines)
delta: 10 PHON artifact(s) retired, 0 added, retained lines identical
findings: 16 (hold 15, note 1)
ok   typed-packet-pinned
ok   no-untyped-records
ok   sound-channel-clean
ok   differential-exact
ok   owed-slots-crosscheck
ok   hold-set-equal
ok   expected-pins
ok   expected-delta-match
ok   expected-verdicts-match
ok   expected-file-current
summary: 10/10 checks passed
```

`--json` (exit 0, sha `121e8c8c…`): `ok: true`, `exit_code: 0`, `checks: 10` of which `passed: 10`,
and `sound_channel: {"off": ["GAR-01" … "GAR-10"], "on": [], "untyped": []}`.

`--check` (exit 0): `typed gate artifacts: byte-identical deterministic derivation` — the committed
typed packet and expected set are the tool's own deterministic derivation, re-derived without writing.

The channel signature of the claim is visible and exact: the ten English `GAR-*` glosses are
off-sound-channel (`off=GAR-01,…,GAR-10`, `on=0`, `untyped=none`), the naming gate's legacy 10
`PHON-INVENTORY` FAILs are retired and nothing else moved (`naming-collision-gate.py: legacy 17 →
typed 7; removed 10, added 0`; the other four gates byte-identical) — the same differential the design
measured pre-wiring (design.md §1.3).

## 3. Findings vs the expected hold set

### 3.1 The set

Counts are identical across the emitted set, the committed expected set and the independent projector:
**15 holds, 1 note, 0 fails**. Rows as emitted at the settled revision:

| # | id (`code` where `id` absent) | severity | `where` | extras | count |
|---|---|---|---|---|---|
| 1–10 | `D2L-FORM-UNRESOLVED` | hold | `LEX-GAR-01` … `LEX-GAR-10` | `record: GAR-01…GAR-10` | 10 |
| 11–12 | `D2L-NATIVE` | hold | `L-15`, `L-16` | — | 2 |
| 13–15 | `D2L-RANK` (`code: R-RANK-CONFLICT`) | hold | `TR-04#a\|TR-06#a`, `WR-02#g\|WR-09#g`, `WR-08#g\|WR-09#g` | — | 3 |
| 16 | `D2L-RANK` (`code: R-RANK-CONFLICT`) | note | `SR-01#a\|SR-01#b` | — | 1 |
| — | — | fail | — | — | **0** |

Design.md §4.2 names the same 16 rows with `where = GAR-01…GAR-10` for rows 1–10 and carries no
`record` field; the projector (`tools/d2-typed-labels.py --json`) likewise emits `where = GAR-0x`.
The landed emission (and the landed expected set, re-emitted from the tool) name the owed **slot**
in `where` and keep the affected record in `record`, with the text line printing
`LEX-GAR-01 (GAR-01)`. No row appears, disappears or changes severity; only this positional
naming differs (§3.2, §5.2).

### 3.2 The four comparisons

| test | comparison | key | result |
|---|---|---|---|
| T1 | emitted e2e findings vs design §4.2/§4.3 transcription | `(id, severity, where)` | **FAIL — 6/16 match; the 10 FORM rows differ only in `where` (`GAR-0x` vs `LEX-GAR-0x`)**; under `(id, severity, record)` all 16 match (the `record` field exists on exactly those 10 rows) |
| T2 | emitted e2e findings vs live projector `d2-typed-labels.py --json` | id-triples + full finding objects | **FAIL — same 10-row `where`/`record` difference; all other rows byte-identical** |
| T3 | committed `typed-gate.expected.json` `expected_findings` vs emitted e2e findings | tool canonical key `(code, severity, where, detail)` (`typed-gate-flow.py:227-231,414-418`) | **PASS** — exact, 16/16 |
| T4 | counts in all three sources | `hold=15 note=1 fail=0` | **PASS** everywhere |

So: **the e2e's own contract is met exactly** (exit 0; emitted set == landed expected set; counts
exact; no extra/missing/severity-swapped row). Against the **design's §4.2 names and the projector**,
the equality holds on 6 rows and fails on the ten FORM rows' `where` field alone. Because the
committed expected file was re-emitted from the running tool after the field change, T3 is
self-consistent by construction on this field; the independent anchors (design table, projector) are
what moved the drift into view. Disposition belongs to the wiring-vs-design and hold-set reviewers
(D20/D21) — this shard reports it, it does not adjudicate it (§5.2).

The ten holds are still **named holds for owed slots**, carried off the sound channel
(`owed-slots-crosscheck`: declared `['LEX-GAR-01'..'LEX-GAR-10']` = held), not phonology artifacts.

## 4. Supporting green legs and non-interference

```sh
python3 tools/typed-gate-flow.py --check        # exit 0, byte-identical derivation
python3 tools/d2-typed-labels.py --check        # exit 0, byte-identical deterministic projection  (re-pin landed)
python3 tools/assemble-d2.py --check            # exit 0, byte-identical deterministic assembly
python3 tools/d2-typed-labels.py --selftest     # exit 0, 39/39 checks passed
```

- **Determinism (light check only).** Three consecutive e2e runs at the settled revision produced
  byte-identical stdout (`final2/3/4.out` and `det-1/2.out` all `204857cb…`), exit 0 each. The full
  determinism matrix (cwd, hash seed, locale, mtime) is R11-D11's shard, not re-run here.
- **No repository writes by the e2e.** `git status --short` captured before and after a three-run
  sequence (`.scratch/d09/git-before.txt` vs `git-after.txt`) is identical; every scratch artifact
  lives under `.scratch/d09/`. (Other paths in the live `git status` — `reports/round-{5..9}/validation.json`,
  `reports/round-10/coverage/index-update-22.md` — are sibling seats' concurrent edits, present
  before my runs and unchanged across them.)
- **Exit-0 semantics.** The tool is judge-shaped as design §3.2 fixes: exit 0 means *the emitted
  findings equal the frozen expected set*, not that the culture is clean — the 15 hold lines are
  printed verbatim so the visible artifact stays red at the design level (§5.5).

## 5. Observations (reported, never absorbed)

1. **Entry-point name vs design.** design.md §3.1/§7 names the entry `tools/gates/typed-pipeline-gate.py`
   (writer D05); the landed wired tool is **`tools/typed-gate-flow.py`** (also D05), which the
   design's own §5.2 note accepts as "gate-shaped" (it sits directly under `tools/`, replayable via
   `replay-frozen.py`). This test's assignment ("the e2e command over `examples/culture-d2`") is
   satisfied by the landed tool's default invocation. Wiring-vs-design conformance is R11-D20's
   disposition, not this shard's.
2. **`where`/`record` naming drift on the ten FORM holds (new at the settled revision).** The design
   §4.2 table and the independent projector both name the hold at `where = GAR-0x`; the settled tool
   emits `where = LEX-GAR-0x` + `record = GAR-0x`, and the committed expected set was re-emitted to
   match. No design.md update accompanied the field change (design.md unchanged since 19:06 local).
   Consequences a reviewer should weigh: (a) under the design's own §4.4(1) key
   `(id, severity, where)`, "findings exactly equal" no longer holds for 10 of 16 rows; (b) the
   committed pin is self-referential on this field (tool → re-emit → pin, review-22 §1.1 C1/C2
   patterns) while the two independent anchors still disagree; (c) the change is arguably an
   improvement (the hold names the owed slot) but it needs the spec or the claim text to say so
   explicitly. `to-verify` for D20/D21 and the parent (§6).
3. **Banner text vs design §3.2.** The design requires a banner line "`TYPED-PIPELINE: exit 0 = the
   emitted findings equal the frozen expected hold set; every hold below is still open design debt.`"
   The landed stdout carries the header `typed-gate-flow — D2 typed pipeline (R11-D05)` and
   `summary: 10/10 checks passed`, but no such banner (grep over `.scratch/d09/final3.out` for
   `exit 0|frozen expected|design debt|TYPED-PIPELINE` finds only unrelated gate lines). The
   semantics are carried by the check list and the verbatim hold lines; exact banner conformance is
   D20's business.
4. **Excluded population (design-review DR-01).** The projector's `/findings` (the e2e's finding
   population) carries 15 holds + 1 note; nine `R-MAT-BRIDGE-MISSING` holds live under
   `era_material_reconciliation` and are outside the comparison by construction. The design chose
   this population (design.md §4.4(4): "the set is over the typed run only"); the exclusion is
   visible in the projection but its disposition (carried where, surfaced by which command) is
   `to-verify` for the reviewers — not re-adjudicated here.
5. **Exit-0 semantics dispute.** design-review §2.3 observes that no producer in the lane exits 0
   on holds; the landed flow reconciles the claim by being the *judge* whose subject is the equality
   (design §3.2). This test asserts the design's semantics as landed. The claim row's wording
   (`capability-draft.md` §4) and any re-reading remain for the parent/D20 — this report records both
   readings rather than picking one.
6. **Tool churn inside the window (why results are revision-bound).** Four tool revisions served
   inside ~7 minutes, each verifiable from its own receipt:
   | revision | stamp (UTC) | run | notes |
   |---|---|---|---|
   | `f3b417bb…` | 22:12:45Z | exit 1, 5/6 | `expected-present` red (expected artifact still `.yml`) |
   | `ae55e6fa…` | 22:13:58Z | exit 0, 10/10 | stdout `d236e8e2…`; `where=GAR-0x`; the first-filed version of this report (`e962849a…` pin) |
   | `a7e1224f…` | 22:16:58Z → re-emit 22:17:05Z | main run 8/10 transiently (exit 1: `hold-set-equal` + `expected-file-current` red before the artifact re-emit), then exit 0, 10/10 | stdout `204857cb…`; `where=LEX-GAR-0x` + `record` |
   | `5758e315…` | 22:19–22:20Z | exit 0, 10/10 | stdout `204857cb…` identical to `a7e1224f`'s; **settled revision tested here** |
   A later revision is a re-read, never a comparison across revisions.
7. **Frozen replay environment condition (adjacent, D08/D12/D25's shard).** Replaying the new
   generation with the lane's in-repo scratch root fails environmentally:
   `python3 tools/replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv` with
   `TMPDIR=$PWD/.scratch` → exit 2, `10 could-not-evaluate … reason=mirror_unsafe` ("temporary root
   is inside the repo") — no row is launched, so this is **not** a replay verdict. D25's record
   (`frozen-records.md` §0/§6.5) reports the same generation at **10/10 reproduced, exit 0** with an
   out-of-repo `TMPDIR`; I did not re-run that leg (out-of-repo scratch is outside this seat's write
   scope) and mark the replay verdict `to-verify` for R11-D12.

## 6. Limits and to-verify

- **Revision-bound.** Results hold for `tools/typed-gate-flow.py` `5758e315…`, packet `e0f21509…`,
  re-pinned projection `a3aa452c…`, typed packet `e8a83445…`, expected set `7ed59731…`. The wave was
  in flight throughout (§5.6); any later change requires a re-run of §2–§3.
- **Scope.** This shard covers the e2e positive, the exact-set comparison, a light determinism check
  and the no-write check. Boundary/malformed, CLI negatives, the legacy-vs-typed differential in
  depth, the full determinism matrix, replay-frozen and negative controls are sibling shards
  (D10–D19); their verdicts are not claimed here.
- **`to-verify`:** (a) the `where`/`record` naming of the ten FORM holds reconciled between
  design.md §4.2, the projector and the landed emission (D20/D21 + parent) — the one place where
  "findings exactly equal the expected hold set" depends on which naming is canonical; (b) round-11
  frozen replay green under an out-of-repo `TMPDIR` (D12/D25); (c) banner-text conformance vs
  design §3.2 (D20); (d) the excluded `R-MAT-BRIDGE-MISSING` population's disposition
  (design-review DR-01).
- **No web retrieval** was made for this shard; every claim is a repo file, a command output, or a
  scratch receipt with a hash. No real-world-language claim is made anywhere above.

## Receipts

```sh
# 2026-10-17 22:19-22:20Z (settled revision), lane repo root, TMPDIR=$PWD/.scratch, scratch .scratch/d09/
sha256sum tools/typed-gate-flow.py examples/culture-d2/{packet.d2.yml,typed-labels.d2.yml,packet.d2.typed.yml,typed-gate.expected.json}
# 5758e315…  tools/typed-gate-flow.py
# e0f21509…  examples/culture-d2/packet.d2.yml
# a3aa452c…  examples/culture-d2/typed-labels.d2.yml
# e8a83445…  examples/culture-d2/packet.d2.typed.yml
# 7ed59731…  examples/culture-d2/typed-gate.expected.json

python3 tools/typed-gate-flow.py                      # exit 0; stdout 204857cb…; 10/10 checks
python3 tools/typed-gate-flow.py --json > .scratch/d09/e2e.json   # exit 0; 121e8c8c…
python3 tools/typed-gate-flow.py --check              # exit 0; byte-identical deterministic derivation
python3 .scratch/d09/verify-exact2.py                 # T1 FAIL (10 FORM rows' where), T2 FAIL (same), T3 PASS, T4 PASS
grep -c "\[hold\]" .scratch/d09/final3.out; grep -c "\[note\]" .scratch/d09/final3.out   # 15; 1
sha256sum .scratch/d09/final2.out .scratch/d09/final3.out .scratch/d09/final4.out .scratch/d09/det-1.out .scratch/d09/det-2.out
# all 204857cb… (three consecutive runs byte-identical)

python3 tools/d2-typed-labels.py --json > .scratch/d09/typed-live2.json   # exit 1 (holds), report complete
python3 tools/d2-typed-labels.py --check              # exit 0; byte-identical deterministic projection
python3 tools/assemble-d2.py --check                  # exit 0; byte-identical deterministic assembly
python3 tools/d2-typed-labels.py --selftest           # exit 0; 39/39 checks passed

git status --short   # before vs after the three-run sequence: identical (.scratch/d09/git-{before,after}.txt)
python3 tools/replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv
# exit 2; 10 could-not-evaluate reason=mirror_unsafe (in-repo TMPDIR — environmental, no row launched)

# earlier revision receipt (first-filed version of this report, §5.6)
# tool ae55e6fa…: exit 0, 10/10; stdout d236e8e2…; expected set e962849a…; where=GAR-0x
```
