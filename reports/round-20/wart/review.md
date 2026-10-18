# R20-O01..O04 — review: the landed per-family alias leg and the O claim at review time

- round: 20 (operator: loop 2 of 3, build round 4 of 4; 64 workers) · shard:
  **O01..O04 (wart analysis ×4)** · owner: L2 worker, kotodama-shokunin lane.
- date: 2026-10-18, readings 13:00–13:08Z. Method: independent commands in
  scratch mirrors + the round's own read-only runner
  (`python3 reports/round-20/run-validation.py --check`, writes nothing).
- **Moving target.** The wave was uncommitted and editing while this review ran:
  `tools/d2-typed-labels.py` moved `0da0015f…` (pre-fix) -> `de11f031…`
  (mtime 13:01:52Z) -> `76536a92…` (13:04:12Z); the D4 projection moved
  `a59990bb…` -> `cbcf997f…`; `tools/gates/typed-pipelines.json` moved to
  `7b67e370…` (13:05:55Z). Verdicts below are anchored to the revision named in
  each row and may already be superseded; re-run the commands in §6.
- canon: **NON-CANON** engineering evidence. A reproduced red stays red.

## 1. Verdict against the O claim's `after_required`

Claim text (`reports/round-20/claims.json`, claim O): the alias component
resolves per packet family; the round-19 wart erratum is closed; d2/d3/d4
projector runs + gate 19/19 + adapter selftest 12/12 green **without** the
mirror copying the foreign examples tree.

| requirement | status at 13:07:39Z | evidence |
|---|---|---|
| family resolution (d2 legacy; foreign = own declaration or skip) | **met** | `family_alias_leg` `:2512`; selftest controls 3d; D4 resolves `named_eras` (4 rows) |
| no foreign read for d4 | **met** | audit-hook trace: 0 `culture-d2` opens; wart mirror checks exit 0 |
| d2 byte-identical | **met** | `--emit` cmp clean; `--json` cmp clean; selftest 50/50; default gate 16/16 |
| d4 projector run green | **met** | `--check` exit 0; runner run `d4-projector-check` exit 0 |
| d3 leg green | **met as defined by the runner** | `d3-assembler-check` exit 0; `d3-projector-probe` is informational (exit 2, named parse error) |
| D4 typed-pipeline gate 19/19 | **met after the profile re-pin** | gate exit 0, `summary: 19/19 legs passed` |
| adapter selftest 12/12 | **met** | exit 0, `12/12 checks passed` |
| without the foreign tree in mirrors | **partially met** | projector: met (mirror control + runner `wart_mirror` green, no `culture-d2`); **adapter: open** — copytree still at `tools/assemble-d4-typed.py:418` |
| re-pin cascade as new rows; live pins match live bytes | **open** | new rows landed (`r20-post` baseline; profile re-pin), but 5 stale-pin failures + the re-pin-home failure below |

Runner verdict at 13:07:39Z: `acceptance_checks_passed: false`; claim O carries
7 failures (F1–F4 below). The green legs, quoted from the runner JSON: d2
projector check, d2/d3/d4 assembler checks, d4 projector check, projector
selftest 50/50, gate 19/19, adapter selftest 12/12, wart mirror both checks
exit 0, `d2_byte_identical: true`.

## 2. Independent re-measurements (mine, not the runner's)

| # | command (scratch mirror unless noted) | measured |
|---|---|---|
| M1 | pre-fix wart mirror, D4 packet | exit 2, `missing examples/culture-d2/components/12-rank-rules.yml; A1 cannot be recorded` |
| M2 | live D2 `--emit` vs committed `typed-labels.d2.yml` | byte-identical (cmp clean) |
| M3 | live D2 `--json` vs pre-edit tool | byte-identical |
| M4 | live projector `--selftest` | 50/50 checks passed |
| M5 | no-D2 mirror, live D4 `--json` | exit 1, `stats {fail: 0, hold: 15, labels: 74, note: 1}` |
| M6 | audit-hook read-set trace, same run | 0 opens containing `culture-d2`; only `examples/culture-d4/packet.d4.yml` |
| M7 | no-D2 mirror, D2 packet | exit 2, legacy error text (unchanged) |
| M8 | D2 component with the `era_aliases` block removed | exit 2, `declares no era_aliases map (A1)` |
| M9 | D4 packet + `era_aliases: {"era-9": [1, 2]}` | exit 1, tag `"[1, 2]"` applied **confirmed** (fail-open) |
| M10 | adapter scratch copy, copytree removed, `--selftest` | 12/12 checks passed |
| M11 | default gate / `--selftest-generalized` | 16/16 legs; 14/14 checks |
| M12 | battery / replays | battery exit 0 (7 pass); `repin-d2` 11/11 reproduced; round-11 10/11 (row 1 already could-not-evaluate pre-round-20) |
| M13 | D4 packet outside `examples/culture-d4/` (path `probe/`) | exit 2, legacy D2 missing-component error (path-key limit) |

## 3. Findings

**F1 — adapter still copies the foreign tree (open, seat in flight).**
`tools/assemble-d4-typed.py:418` (sha `1ddad6a7…`) still runs
`shutil.copytree(ROOT / "examples/culture-d2", …)` with the round-19 comment.
The runner's marker regex flags it (`foreign_tree_copy_in_adapter: true`).
Control M10: a scratch copy with lines 416–419 removed passes 12/12, so the
removal is safe now. Recommendation: delete the copytree + its comment; the
mirror's own control (projector selftest section 5) already proves the no-D2
mirror rebuilds the filed projection byte-for-byte.

**F2 — `examples/culture-d4/expected-holds.json` pins stale (open, cascade).**
`projector_sha256` `0da0015f…` != live `76536a92…`; `projection_sha256`
`a59990bb…` != live `cbcf997f…` (runner FAIL ×2, 13:07:39Z). The `holds`/`notes`
content is unchanged (M5: same 15 holds + 1 note), so only the pin fields move.
Recommendation: re-pin as a NEW artifact row, not an edit of a filed byte.

**F3 — typed-packet pins: runner expects keys the artifact does not carry (open, spec mismatch).**
`examples/culture-d4/packet.d4.typed.yml` (sha `f63ed531…`) has its original
`assembly:` block at `:2344` (generator/reader/serializer/source_sha256) and a
`typed_assembly:` block at `:2799` (generator/packet/projection/rules) — neither
carries `packet_sha256`/`projection_sha256`/`adapter_sha256`. The adapter's
in-memory pin block (`build_typed_packet`, `tools/assemble-d4-typed.py:270–274`)
is not emitted by the text transform, and `--check` on the committed file exits
0 (so the artifact is self-consistent, just pin-free). The runner's
`typed_packet` check reads the `assembly:` block and reports three stale pins
(`None != live`). Two consistent resolutions, for the O seat + integrator:
(a) emit the pin block into the typed packet's `assembly:` (bytes move -> the
typed packet, its adapter `--check` reading and all its pins re-pin as new
rows), or (b) revise the runner to read the pins where the adapter records them
(`typed_assembly:`) or to exempt a key the artifact never carried. Do not fix
by editing the runner's expectation silently — say which artifact owns the pins.

**F4 — re-pin row home (open, cascade).**
The runner wants round-20 re-pin rows under `reports/round-20/repin/**` or
`tools/gates/frozen/round-20/**`; neither exists (13:07:39Z). What landed is
`tools/gates/expected/d4-typed-labels-check-gate/r20-post/**` (the new baseline
id; inputs: packet + projector `76536a92…` + reader + projection `cbcf997f…`,
**no D2 components**) and `reports/round-20/wart/expected-v2-07-r20.json`.
Recommendation: land the round-20 re-pin record under the home the runner names
(a `reports/round-20/repin/table.md` + the frozen `round-20` row, or have the
integrator widen the runner's homes to include the `r20-post` baseline and say
so in the runner's limits).

**F5 — malformed declared tag applied silently (defect, fail-open).**
`packet_alias_rows` coerces with `str(...)` and does not screen tags. Measured
M9: `era_aliases: {"era-9": [1, 2]}` -> `era_aliases_applied {'era-9': '[1, 2]'}`,
`alias_rows` row `confirmed`. A1 ("no silent aliasing") is about exactly this:
a tag the grammar does not accept must not enter the projection as confirmed.
Recommendation: screen each declared tag with `ERA_TAG_RE` and fail closed (or
hold with a named finding) on a miss; refuse non-string entries instead of
coercing. Add the control to the projector selftest (the current family
controls do not include a malformed-tag row).

**F6 — family key is the path shape (limit, documented).**
`packet_family` `:2457` reads the parent directory name (the gate's `family_of`
convention). Measured M13: a D4 packet outside `examples/culture-d4/` falls back
to the D2 leg and exits 2 on the missing component. All claim surfaces keep the
shape, so the wart is closed where measured; but the packet also declares
`assembly.generator` (the string `typed-pipelines.json` matches on), which would
key the family regardless of location. Recommendation: record the limit in the
claim's limits; consider accepting the declared generator as a secondary key in
a later round.

**F7 — the claim's parenthetical was wrong, and the landed leg is better for it.**
"d4 packets declare no era-alias rules" is contradicted by the packet:
`named_eras` (`examples/culture-d4/packet.d4.yml:1915`, 4 name->tag rows) and
`era_records` (`:1794`). The landed leg resolves those declared rows; the skip
branch is exercised by the `era_reconciliation` leg (skipped row recorded) and
by the selftest's no-declaration control. Reviewers should read the claim's
"documented skip" as the fallback branch, not as the expected D4 behaviour.
Related: the "d3 projector run" in the assignment is informational in the
runner (`d3-projector-probe`, exit 2 with a named parse error, unchanged by this
work); the green d3 leg is `tools/assemble-culture-d3.py --check` (exit 0).

## 4. What this review does not establish

- It does not admit the round or the O claim: at 13:07:39Z the runner reports
  `acceptance_checks_passed: false` with 7 O failures (F1–F4).
- It does not certify the changed D4 era block as *correct*: the projection's
  `era_reconciliation` verdicts now come from the packet's own declarations
  (measured change: `era-1` was `mapped-confirmed` by D2, now `unmapped`;
  `the league` -> `E2` confirmed). That semantic change belongs to the O/D seats'
  acceptance, not to this review.
- The battery (exit 0, 7 pass) and the frozen replays (11/11, 10/11) stayed
  green, but a green battery is not clearance and a reproduced red stays red.
- Filed rounds 8–19 bytes were not compared here beyond the runner's own
  preservation leg; the runner reports the preservation result at close.

## 5. Re-check commands for the parent at close

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch
python3 reports/round-20/run-validation.py --check     # read-only acceptance JSON
python3 tools/d2-typed-labels.py --selftest            # 50/50 + family controls
python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml  # 19/19
python3 tools/assemble-d4-typed.py --selftest          # 12/12 (F1: after the copytree removal)
grep -n "copytree(ROOT / \"examples/culture-d2\"" tools/assemble-d4-typed.py   # expect no match
python3 - <<'EOF'
import json
e=json.load(open('examples/culture-d4/expected-holds.json'))
print('projector pin stale:', e['projector_sha256'] != __import__('hashlib').sha256(open('tools/d2-typed-labels.py','rb').read()).hexdigest())
EOF
```

## 6. State at handoff (13:10:12Z, read-only runner re-run)

The O failure list moved between the two runner runs while this review was being
written: `no round-20 re-pin rows landed` **cleared** (the runner was revised at
13:08:52Z and now finds the round-20 re-pin record), leaving **6** O failures:

1. adapter selftest still copies the foreign `examples/culture-d2` tree (F1);
2. `expected-holds.json projector_sha256` stale `0da0015f…` (F2);
3. `expected-holds.json projection_sha256` stale `a59990bb…` (F2);
4. `packet.d4.typed.yml packet_sha256` pinned `None` (F3);
5. `packet.d4.typed.yml projection_sha256` pinned `None` (F3);
6. `packet.d4.typed.yml adapter_sha256` pinned `None` (F3).

Still green at 13:10Z: projector selftest 50/50, D4 gate 19/19, D4 `--check`
exit 0, adapter selftest 12/12, `d2_byte_identical: true`, wart mirror both
checks exit 0; claim C passes, claim D is the D seat's open work (6 failures,
not this shard's). F4 is closed by the runner revision; F5–F7 stand as written.

Files written by this shard: `reports/round-20/wart/design.md`,
`reports/round-20/wart/review.md`; scratch under `.scratch/r20-o/**`.
