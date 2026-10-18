# R17-D21..D24 — `tools/assemble-culture-d4.py` implementation record (O claim)

- round: 17 (operator loop 2 of 3, build round 1 of 4; 64 declared workers,
  `opencode-go/deepseek-v4.1-flash`) · seats: **R17-D21..D24** (O-assembler,
  single writer) · claim **O `assemble-culture-d4`** (`reports/round-17/claims.json:25-32`).
- assignment (verbatim): "D4 R17-D21..D24 (assembler tool O, single writer of
  tools/assemble-culture-d4.py): implement --check/--selftest per the d2/d3
  assembler idiom; fixture controls positive/tamper/malformed/missing;
  reports/round-17/assembler/{impl,tests}.md."
- date: 2026-10-18. Reference revision `9b49a4a` (round-17 declare); baseline
  `f30b6f8188937632bbedd0e7b29aeefff6f8b07b` (round-16 admit).
- canon: NON-CANON engineering evidence. This fragment is not a canon record, a
  lore handoff, a rights/clearance statement, or a culture proposal; the D4
  content it merges is a design drill.
- writes: `tools/assemble-culture-d4.py` (this seat's tool, new file) and this
  fragment plus `reports/round-17/assembler/tests.md`; scratch under
  `.scratch/r17-o/` (`export TMPDIR=$PWD/.scratch` preceded every
  scratch-writing command). No component, design, packet, projection, or
  earlier-round byte is edited by this seat; `reports/round-{8..16}/**` and
  `tools/gates/{frozen,expected}/**` are filed and read-only. No commit, no push.
- status: **tool implemented and green on the delivered tree**: `--check` exit 0
  and two regenerations byte-identical (receipt in `tests.md` §3.5); `--selftest`
  81/81 exit 0; the round-17 counting command's no-write run reports claim O
  `passed=true`. Claim D's remaining blockers are other seats' artifacts plus
  F-O-6 below.

## 0. Verdict

1. `tools/assemble-culture-d4.py` exists, is stdlib-only, and implements the
   d2/d3 assembler idiom: default build writes exactly one owned output
   (`examples/culture-d4/packet.d4.yml`); `--check` compares bytes without
   writing (exit 0 equal / 1 drift / 2 error); `--selftest` drives the same CLI
   over a fixture tree inside one temporary directory with positive, tamper,
   malformed and missing controls (81 checks, exit 0).
2. The contract is taken from the round's own records, not invented: the
   artifact path, the fail-closed legs and the pin block come from
   `reports/round-17/d4/design-brief.md` §9.1–§9.3 and the D4 derivation
   contract `reports/round-17/d4/typed-support-1.md` §5.1–§5.2; the component
   registry and per-component packet keys come from the component files
   themselves (`reports/round-17/d4/components/01-brief.yml` registry C-01..C-12
   and each file's top-level `packet_keys:`).
3. Two load-bearing findings were measured and handled, not absorbed:
   **F-O-1** the lane's stdlib YAML-subset reader breaks on component prose
   (block scalars containing a colon), so the assembler elides block scalars
   before parsing and records the counts; **F-O-2** two parallel D4 design
   families are landing (weigh-court and furnace-league), so the assembler
   merges by the per-file `packet_keys` declaration with a documented
   allowlist fallback, and records every non-packet key under
   `assembly.skipped_keys` instead of guessing a single design.
4. `assemble()` is the callable build path the D4 typed adapter's
   assembler-identity leg must call (`typed-support-1.md` §5.2 B4: "the D4
   adapter's identity leg must call `assemble-culture-d4.py`'s own build (the O
   claim's tool) — never re-implement it").
5. On the delivered tree (`examples/culture-d4/`, landed by the integrator at
   09:44Z with brief.md + 12 components + packet.d4.yml): `--check` exits 0,
   two in-place regenerations are byte-identical to the delivered bytes
   (sha256 `39c2d56a…`, 80,509 bytes), and the round-17 counting command in its
   no-write mode reports **claim O passed=true** (selftest 81/81 with all four
   control tokens; d2/d3 regressions green). Claim C passes; claim D still
   fails on other seats' artifacts (typed packet, projection, expected holds,
   round-17 frozen manifest) and on F-O-6 (the brief's refusal sentence
   matching the runner's clearance substring).

## 1. Interface

```
python3 tools/assemble-culture-d4.py            # write packet.d4.yml
python3 tools/assemble-culture-d4.py --check    # 0 equal / 1 drift / 2 error
python3 tools/assemble-culture-d4.py --selftest # fixture controls, temp dir
```

- Owned output: `examples/culture-d4/packet.d4.yml` — exactly one gate-facing
  packet (`design-brief.md` §9.1: "emitting **exactly**
  `examples/culture-d4/packet.d4.yml` (gate-facing) on a default build").
- Inputs: every `*.yml` / `*.yaml` / `*.json` under
  `examples/culture-d4/components/`, at least 12 files (`reports/round-17/scope.md`
  §5 D1: "the 12 components + brief … all exist"; the runner requires
  `>= 12` component files: `reports/round-17/run-validation.py:487-489`).
- Serializer: `yaml_lines` from `tools/assemble-d2.py`, loaded read-only via
  `runpy` (no dependency added; same idiom as `assemble-culture-d3.py:140-148`).
- Reader: `parse_packet` from `tools/gates/costume-era-consistency-gate.py`,
  loaded read-only, with its `Malformed` turned into a `ValueError` (same idiom
  as `tools/assemble-d2.py:34-46`).
- Exit codes: 0 success; 1 `--check` drift (or missing output); 2 could-not-
  evaluate (missing/malformed component, missing block, collision, missing
  reader/serializer). No traceback on any fail-closed path.

## 2. Merge contract

1. **Per-file packet keys.** A component's top-level `packet_keys: [...]`
   declaration fixes that file's contribution exactly; without one, the
   `PACKET_KEYS` allowlist applies. Sources: the furnace registry
   (`reports/round-17/d4/components/01-brief.yml`, C-01..C-12 rows) and the
   weigh-court registry (`reports/round-17/d4/design-brief.md` §5) unioned in
   the allowlist.
2. **Nothing merges silently.** A key outside a file's contribution (or outside
   the allowlist) is per-file design metadata: it is recorded under
   `assembly.skipped_keys` with the files that declared it.
3. **Collisions fail closed.** Two files declaring the same packet key with
   unequal values exit 2 naming both files; equal duplicates collapse.
4. **Required core.** `phonology` (mapping), `lexicon`, `names`, `eras`,
   `costumes`, `materials` (non-empty record lists) must be present, typed,
   record-shaped, with unique ids and the declared minimum counts. `eras` also
   accepts plain era tags (the D2 packet shape: `eras: [E0, E1, …]`).
5. **Packet-owned keys.** `name`, `canon`, `assembly` are constants of the
   tool; component declarations of them are recorded, never merged. The packet
   declares NON-CANON (`design-brief.md` §9.5).
6. **Normalization.** A component-declared `era_dates` block is carried as
   `source_era_dates` — the `assemble-d2.py:151-156` precedent, kept because the
   costume gate refuses a non-numeric `era_dates` mapping
   (`tools/gates/costume-era-consistency-gate.py:440-453`, `Malformed` →
   exit 2). Recorded in `assembly.normalizations`.

## 3. Determinism and pins

- Output bytes are deterministic: fixed key order (packet-owned keys, then
  `PACKET_KEYS` order, then any extra declared keys sorted), `yaml_lines`
  emission, LF, no timestamps, no host paths.
- `assembly` pins: `assembler_sha256` (this tool's own digest — the
  `design-brief.md` §9.2 self-pin), `reader_sha256`, `serializer_sha256`,
  `source_sha256` (every component file), plus `skipped_keys`,
  `block_scalars_elided`, `normalizations` and NON-CANON `unresolved` notes.
- A changed component or a changed tool is drift: `--check` exits 1 (or the
  adapter's identity leg exits 2), never a silent edit.

## 4. Findings

- **F-O-1 — the stdlib subset reader breaks on component prose.** Measured
  2026-10-18: `reports/round-17/d4/components/05-naming.yml` (staged component,
  sha256 in `tests.md` §3) failed `parse_packet` with "input is not one mapping
  (or has unparsed trailing lines)"; bisection pinned line 15 — the `scope: >-`
  block whose first continuation line contains a colon ("Eight delivered name
  records: four personal names, …"), which the reader reads as a mapping entry.
  Two earlier components (`02-phonology.yml`, `03-orthography.yml`) use the
  same construct and parse only because their prose happens to avoid colons.
  **Handling:** `elide_block_scalars()` replaces each `key: |` / `key: >-`
  header (at any depth) with a quoted placeholder and drops its continuation
  lines before the reader; counts are recorded under
  `assembly.block_scalars_elided`. A *packet* block declared as a block scalar
  arrives as a string and fails `validate_blocks` closed, never silently. This
  is a reader shim in the assembler, not a gate or reader edit (the reader's
  bytes are untouched and pinned).
- **F-O-2 — two D4 design families are landing in parallel.** The staged
  component tree follows the furnace-league design
  (`reports/round-17/d4/components/01-brief.yml` SEED-01..SEED-08: "FIRE and
  MARK"), while `reports/round-17/d4/design-brief.md` specifies the weigh-court
  quote-register design (COUNT × QUOTE) with a different 12-file registry
  (`01-brief.yml`, `02-phonology.yml`, `03-morphosyntax.yml`,
  `04-ledger-script.yml`, … vs the staged `03-orthography.yml`,
  `04-lexicon.yml`, …). This seat does not adjudicate the design; the
  assembler is contract-flexible over both (per-file `packet_keys` + allowlist
  union) and reports the divergence here for the integrator/parent. The
  weighing: whichever component set is landed in
  `examples/culture-d4/components/` assembles deterministically; a mixed tree
  fails closed on collisions.
- **F-O-3 — `--check` exit 2 before the tree lands is correct, not a defect.**
  At this stamp `examples/culture-d4/` does not exist, so a default build exits
  2 with "components directory not found: examples/culture-d4/components"
  (measured, `tests.md` §3.4). The runner measures the settled tree
  (`run-validation.py:559-565` runs `--check` only `if (ROOT / D4_ASSEMBLER).is_file()`;
  the O leg runs it unconditionally and fails on non-zero,
  `run-validation.py:963-971`).
- **F-O-4 — the O leg's selftest evidence is token-graded.**
  `run-validation.py:972-980` requires the `--selftest` stdout to carry
  `positive|clean`, `tamper`, `malformed` and `missing` (or an `N/M checks
  passed` count with N ≥ 4). This tool's summary line carries all four tokens
  and the `81/81` count (`tests.md` §2).
- **F-O-5 — a staged component carries a duplicate flow-mapping key and blocks
  the whole D4 assembly.** Measured 2026-10-18T09:41Z:
  `reports/round-17/d4/components/07-symbolism.yml` (write stamp 09:40:53Z)
  fails the lane's stdlib subset reader with "duplicate key 'evidence' in flow
  mapping"; the duplicate is on the file's line 47, a flow mapping declaring
  `evidence` twice (the quoted self-sweep string and `evidence: design-choice`).
  The other eight staged components parse (after the F-O-1 elision). Impact:
  while this file stands as written, every build of the delivered tree exits 2
  and the runner's D3 and O legs fail. Disposition belongs to the component's
  seat or the integrator; this seat does not edit another seat's file
  (`AGENTS.md`: workers write only their assigned evidence fragments). The
  assembler's refusal is the correct fail-closed behaviour and names the file
  and the key. **Resolved by its own seat at 09:42Z** (the file now parses; the
  12-component mirror build at 09:43Z is green).
- **F-O-6 — the landed brief trips the runner's clearance scan on a refusal
  sentence.** Measured 2026-10-18T09:45Z with
  `python3 reports/round-17/run-validation.py --check`:
  `examples/culture-d4/brief.md` line 5 reads "It is **not canon, not a
  world-bible entry, and not accepted by lore-shokunin**" — the negated
  substring "accepted by lore" matches the runner's third
  `CLEARANCE_FORBIDDEN` pattern (`run-validation.py:131`,
  `\b(approved by lore|accepted by lore|lore[- ]accepted)\b`), so claim D's
  NON-CANON leg reports `clearance/acceptance claim found` and fails. The
  sentence's intent is the opposite of a clearance claim; the scan is
  substring-based and the fix is a rewording (e.g. "no lore acceptance is
  claimed") in the brief's own file — not this seat's write scope. Sweep
  evidence: a pattern scan over every file under `examples/culture-d4/`
  (2026-10-18) reports exactly this one hit; `packet.d4.yml` and all 12
  components are clean.

## 5. Non-absorbed scope (reported, never decided here)

- The D4 design content, the hold set, the typed projection/adapter/gate, and
  the frozen manifest are other seats' deliverables; this tool only produces
  the gate-facing packet they read.
- The design-family divergence (F-O-2) and the reader-prose class (F-O-1) are
  reported to the integrator; no component, gate, design doc or D2/D3 byte is
  edited by this seat.
- Canon status, real-world referents, clearance and rights questions are lore
  scope (`PROVINCE.md`); the packet carries NON-CANON markers and zero
  real-world clearance claims.

## 6. Limits

- A green `--check`/`--selftest` is a structural reproduction result, not a
  design verdict: the packet is red by design (holds are carried by the typed
  pipeline, not laundered here).
- The `block_scalars_elided` shim means component *prose* is not carried into
  the packet (it is component metadata); component *content* blocks are
  unaffected and pinned by digest.
- Counts in this fragment carry their command and date; a digest pin is a
  read-time pin (a later mismatch means the file changed after the read).
