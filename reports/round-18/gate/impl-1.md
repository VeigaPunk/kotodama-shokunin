# R18-O03 — Implementation: the declared-assembler identity leg

- round: 18 (operator loop 2 of 3, build round 2 of 4; 64 workers on
  `opencode-go-2/deepseek-v4.1-flash`) · shard: **O03** (impl, single writer of
  `tools/gates/typed-pipeline-gate.py`) · claim O `gate-generalization`
  (`reports/round-18/claims.json:8-14`).
- assignment (verbatim): "O R18-O03..O06 (impl x4, single writer owns the gate
  file): implement the generalization so the DEFAULT D2 path is byte-identical in
  behavior; the D4 path verifies against assemble-culture-d4.py --check output
  identity; fragments + integration evidence
  reports/round-18/gate/impl-{1..4}.md."
- date: 2026-10-18. Evidence window 10:18–11:1xZ (07:18–08:1x -03:00). Baseline
  revision `3dd3754207032cb81f5fb3e202fe85cf79211339` (round-17 close); HEAD
  `c66ac3c` (round-18 declare).
- canon: NON-CANON engineering evidence. Nothing here is a canon record, a lore
  handoff, a clearance, or a rights/attribution ruling.
- writes: **`tools/gates/typed-pipeline-gate.py`** and **`tools/gates/typed-pipelines.json`**
  (this shard's files, the single writer), plus `reports/round-18/gate/impl-{1..4}.md`;
  scratch under `.scratch/r18-o03/` (`export TMPDIR=$PWD/.scratch` preceded every
  scratch-writing command). No packet, projection, component, manifest, baseline,
  frozen receipt or earlier-round byte is edited. No commit, no push.
- **status: implemented and frozen.** Two revisions landed, both driven by
  measured requirements rather than preference:
  - `286d6e82…` — the resolver + identity leg + fixture controls (10:4xZ),
    immediately re-pinned by the re-pin seats;
  - `d96958b6a642c6c43fbc7b7ebf1c219f9fe7f276ca41b4ffbd2ffc5d71175617` (1349
    lines) — the sha-pinned profile channel and the digest-bearing
    resolution line, required by the D claim's legs in
    `reports/round-18/run-validation.py` (updated 10:44Z: "the D4 gate run names
    no declared assembler in its resolution line", "…names no assembler digest…",
    and `tools/gates/typed-pipelines.json` missing).
  The D2 default path is byte-identical at **both** revisions (`impl-2.md`).

## 0. Verdict

1. The hard-coded D2 binding is gone. L1 resolves an **assembler identity by
   declaration**, precedence: CLI flag > packet declaration > sha-pinned profile
   > family convention (`examples/culture-<family>/…`) > D2 defaults. With nothing
   declared the resolution lands on exactly the pre-generalization constants and
   the run takes the old code path — measured byte-identical on all four pinned
   invocations (`impl-2.md` §2).
2. A non-default assembler turns on an `L1-assembler` identity leg that loads the
   declared assembler with the lane's `runpy` idiom and calls its own
   `assemble()` — the same call `--check` makes — then requires the packet bytes
   to match, and, when the packet pins `assembly.assembler_sha256`, requires the
   live assembler bytes to hash to that pin. Never a re-implementation.
3. `tools/gates/typed-pipelines.json` is the flagless, sha-pinned channel the
   frozen rows can replay: matching is by the graded packet's own
   `assembly.generator` string (never a filename guess), and every pinned field is
   re-verified against live bytes — a stale pin refuses at `L1-profile` (exit 2).
4. Every non-default run prints one **resolution line** naming the profile, its
   file digest, and each resolved path with its live digest — on the normal report
   path *and* on the exit-2 path, so a blocked run still witnesses what it
   resolved.
5. Routing, expected-set and pin legs are generalized too (moved vs on-channel
   rows; the declared `expected-holds.json` as the expected source; the declared
   packet/projection/adapter/assembler pins re-verified), so a D4-family packet
   reaches L3/L4 instead of failing at a D2 constant.

## 1. The measured before-state

| subject | measured | receipt |
|---|---|---|
| `tools/gates/typed-pipeline-gate.py` (before) | `sha256 d102fd1dd1bae3cc4c9d0ea33844b2f706a2098707938c82c75ce9fb6368e27d` | `sha256sum`, 10:18Z; equals the round-11 frozen row's `gate_sha256` (`tools/gates/frozen/round-11/MANIFEST.tsv` row 2) |
| the D2 bindings | `SERIALIZER`, `PROJECTION_DEFAULT`, `EXPECTED_HOLDS_PATH`, `ADAPTER`, `PROJECTOR`, `EXPECTED_HOLDS/NOTES/COUNTS`, `GATE_NAMES` all module constants | pre-edit `typed-pipeline-gate.py:55-98` |
| the round-17 rejection | "the typed-pipeline gate L1 assembler-identity leg pins assemble-d2 output; D4 packets cannot be gated" | `reports/round-17/reviews/review-4.md` F6; `reports/round-17/d4/typed-support-1.md` B4/B5 |
| the delivered D4 self-declaration | `assembly.generator: "tools/assemble-culture-d4.py"`, `assembler_sha256: 943f487b…` | `examples/culture-d4/packet.d4.yml:2344-2346` |

## 2. The mechanism (code map, `tools/gates/typed-pipeline-gate.py` at `d96958b6…`)

| anchor | what it does |
|---|---|
| `D2_DEFAULTS` | the pre-generalization constants, key for key: `packet`, `typed`, `projection`, `adapter`, `expected`, `assembler`, `projector` |
| `PROFILE_DEFAULT`, `load_profile`, `profile_pins` | `tools/gates/typed-pipelines.json`: schema `kotodama-typed-pipelines-v1`, profiles matched on `assembly.generator`, each field's `sha256` re-verified against live bytes |
| `DECLARED_ALIASES` | the declaration vocabulary: `assembler`/`generator`, `projection`, `adapter`, `expected`/`expected_holds`, `packet`/`legacy_packet`, `typed_packet`, `projector` |
| `moved_field(row)` | the moved-vs-on-channel rule: a missing key or a null-ish value (`null`, `none`, `~`, empty — the lane reader keeps `null` as the string) means the row stays on channel |
| `candidate_path`, `family_of`, `family_paths`, `family_projector` | path resolution and the per-family convention (assembler `tools/assemble-culture-<fam>.py` else `tools/assemble-<fam>.py`, projection `typed-labels.<fam>.yml`, adapter `tools/assemble-<fam>-typed.py`, expected `expected-holds.json`, reader `tools/<fam>-typed-labels.py` when it exists) |
| `declared_paths`, `resolve_config` | the precedence chain and the single boolean `generalized` |
| `assembler_identity` | the identity leg: `runpy`-load, require a callable `assemble()`, compare bytes, then the optional self-pin |
| `resolution_line(config)` | the one line every non-default run prints (profile + file digest + 4 paths with live digests) |
| L1 declared identity | `L1-profile` (profile file unreadable, or a pinned field mismatched → exit 2), `L1-assembler`, `L1-expected-holds` (declared expected file, shape-checked) |
| L1 build | adapter from `config["adapter"]`, existence check, positional `build(packet, projection)` (the D2 idiom the design seat also expects), fail-closed `L1-build` |
| L2 moved/retained | the channel differential over moved rows only, plus `L2-retention` when any row stays on channel |
| L3 | expected set/counts/details from the resolved source; `L3-routing-consistency` reads the hold id off the routing rows |
| L4 | default: the three D2 pins verbatim; generalized: every declared pin re-verified against live packet/projection/adapter/assembler, exit 2 when a declared pin's live file is gone |
| `report` / `json_document` | the resolution line and the `resolved` block (with `profile`, `profile_file`, `profile_sha256`) appear **only** in non-default runs |
| `FIXTURE_ASSEMBLER`, `_fixture_typed_packet`, `selftest_generalized` | the fixture-level controls (14 checks) |

Declaration channels, all optional and additive:

- a `typed_pipeline:` block in the graded packet, or the delivered idiom
  `assembly.generator:` + `assembly.assembler_sha256:` (the pair
  `examples/culture-d4/packet.d4.yml` already carries);
- the profile file `tools/gates/typed-pipelines.json` (D4 profile: packet,
  assembler, projection, expected pinned to live digests; adapter pinned `null`
  until the D4 adapter lands — the path is resolved and its absence is what
  `L1-build` reports);
- the flags `--assembler/--projection/--adapter/--expected/--legacy-packet`,
  which override both.

`generalized` is true iff a flag was passed or a resolved path differs from its
`D2_DEFAULTS` value. For family `d2` (or no family) nothing resolves away from the
defaults, so the default runs stay on the old path by construction.

## 3. The identity leg, stated exactly

```
           declared_sha = document["assembly"]["assembler_sha256"]  (if any)
           expected     = load_peer(config["assembler"])["assemble"]()
           actual       = Path(identity_target).read_bytes()
  pass iff actual == expected  and  (declared_sha is None or declared_sha == sha256_file(assembler))
```

- `identity_target` is the graded packet itself in the legacy branch and the
  declared/sibling legacy packet (`config["packet"]`) when a typed packet is
  graded directly.
- Failure is exit 2 (could-not-evaluate): a packet whose bytes are not the
  declared assembler's output, a forged/stale self-pin, an assembler with no
  `assemble()`, an unreadable assembler — each with the resolved path and both
  digests named in the detail.
- The lane's reader keeps an unquoted `null` as the string `"null"` (measured:
  `a: null` → `'null'`), which is why `moved_field` treats the null-ish strings as
  "stays on channel" — the D4 register class declares `off_channel_field: null`.

## 4. Divergences from `reports/round-18/gate/design.md` (O01/O02)

| design proposal | landed | reason |
|---|---|---|
| `tools/gates/typed-pipelines.json` (§4) | **added**, and the gate reads it: matching by `assembly.generator`, `L1-profile` pin verification, resolution line | it is the channel the validator's D legs require, and it is the design's own pin discipline |
| `/ --profile <id>` flag (§4 rule 1) | not added; the profile resolves by the packet's declared generator | no flag is needed for the flagless channel; the validator's `--help` check covers `--assembler/--projection/--expected` only |
| family-convention / sibling-name resolution (§4 rejected alternatives) | kept as the **last** fallback below the profile | it is what makes the D4 path resolve before the profile landed, and it is inert whenever a profile matches. It never substitutes the D2 adapter for a non-default family |
| check id `L1-assembler_identity` | `L1-assembler` | the D2 adapter already emits its own `L1-assembler_identity` arm on the default path; a second, differently-sourced leg under the same id would be unreadable. The independent test seats measured the landed id and strings (`reports/round-18/gate/tests-3.md`, `reports/round-18/d4/scribe-1.md` A3) |
| diagnostics vocabulary `DECL-ASSEMBLER-*` on stderr | `FAIL L1-assembler: <detail>` in the gate's existing report shape | one reporting shape for all legs; the detail names the resolved path and both digests |
| identity failure = exit 1 | exit 2 | matches the gate's pre-existing L1 fail-closed shape and design §7.3's own "pin mismatch → could-not-evaluate" |
| `--assembler-sha256 HEX` flag | not added | the pin is read from the packet or the profile |

## 5. The pin ledger this shard owes

| surface | before (baseline `3dd3754`) | after (live) | how the cascade reads |
|---|---|---|---|
| `tools/gates/typed-pipeline-gate.py` | `d102fd1dd1bae3cc4c9d0ea33844b2f706a2098707938c82c75ce9fb6368e27d` | `d96958b6a642c6c43fbc7b7ebf1c219f9fe7f276ca41b4ffbd2ffc5d71175617` | new rows/files only: the filed round-11 row now reads could-not-evaluate/`gate_digest_mismatch`, and `tools/gates/frozen/round-18/repin-d2/MANIFEST.tsv` (written and re-pinned by the re-pin seats) pins row 2 on the live digest and replays 11/11 (`impl-4.md` §2). The first revision `286d6e82…` was pinned and superseded within the round; its intermediate records stay filed |
| `tools/gates/typed-pipelines.json` | (new file) | `434e90509a1c5e25d639dfb8b6027ab5c8a6045340c9b81f46a5ecb3b04af004` | new file, named in the resolution line of every non-default run and in the `resolved` block |

`tools/assemble-d2.py`, `tools/d2-typed-labels.py` and `tools/assemble-d2-typed.py`
are **not** touched by this shard, so the cascade's other three pinned surfaces
stay where they were.

## 6. Compliance

- Writes: `tools/gates/typed-pipeline-gate.py`, `tools/gates/typed-pipelines.json`,
  `reports/round-18/gate/impl-1..4.md`, scratch under `.scratch/r18-o03/**`. No
  commit, no push, no filed byte edited.
- Every receipt in this set carries its command and the sha it measured; the
  fragments were written against the frozen gate revision `d96958b6…` and no edit
  followed them.
