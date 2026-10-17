# R10-O04 — findings fixer: tracker idx 2 (R9-D09 S1) and idx 10 (R8-D16 S12)

- round 10 (loop 1 of 3, build round 3 of 4), 2026-10-17 · worker **R10-O04** (fixer)
- writes: **this file only**. No tool, spec, tracker, packet, pin or fragment was edited;
  all scratch is under in-lane `.scratch/` (`export TMPDIR=$PWD/.scratch` before every
  scratch-writing command). No commit made.
- worktree at work: revision `e3a1ec9` + dirty (`M reports/round-9/validation.json`,
  untracked `.scratch/`); all commands below ran from the lane root on 2026-10-17.
- index basis: `reports/round-10/findings-tracker.json` (landed `21:27Z`, sha-compiled at
  `e3a1ec9`) — **idx 2 = R9-D09 S1** (high) and **idx 10 = R8-D16 S12** (low), taken as
  written. Before the tracker landed I had derived idx 2 = R8-D16 S6 under a source-order
  reading and ran its controls meanwhile; those receipts are kept in Appendix A as a
  byproduct for idx 4's fixer, not as a disposition.
- canon: NON-CANON engineering evidence.

---

## idx 2 — R9-D09 S1: "the re-pin is a blessing operation until it carries a re-verification record"

**Disposition: `fixed-with-control`.** The re-pin happened in the round-9 admission
(`9dc18ec`); the record exists; every item of S1's minimum record is satisfiable at the
current revision and was independently re-run here by a shard that is **not** the re-piner.
The re-pin is distinguishable from blessing a tamper because the three drifted inputs are
round-8's committed changes, behavior-neutral on the D3 projection, with the predeclared
expectation untouched.

### Control (re-run of the green, by a different shard)

```sh
python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json \
        --frozen examples/culture-d3/expected.json
# exit=0
# {"counts": {"total": 0}, "exit": 0, "findings": [], "profile": "kotodama-d3-evidence-coupling/1"}
# stdout sha256 e282a0688498034144fb376ab43884c8607133bd6deaab763150d789b113669d
```

### S1 minimum-record test, item by item

| # | required item | observed (2026-10-17) |
|---|---|---|
| 1 | pre-refresh freeze token | sha256 `74496aa8aa7db2d7b2d69ecbd7a5a6acf3d4f565f600fd74bfeab5480adf5080` (`git show a7bb205:examples/culture-d3/expected.json \| sha256sum`), git blob `c420ac4c…` (diff header `index c420ac4..7f298ce`); anchored in round-9 receipts (`d3/scribe.md:104,209`, `d3/evidence-coupling.md:16`) |
| 2 | three keys, old → new + causing commit | `d3/check-diagnosis.md:74-75` carries the table; my re-measure of the semantic diff `a7bb205→9dc18ec` is **exactly** 3 changed manifest values: `corpus/knowledge/synthesis/worldbible-integration-contract.md` `50c4c2f25a72…`→`5f4c02bfc4e6…`; `tools/gates/costume-era-consistency-gate.py` `29a9361c7b96…`→`e6bffd7020c0…`; `tools/gates/naming-collision-gate.py` `8c5afb0a5abc…`→`d9e4e8f4f93a…`. `git log --oneline -1 -- <each of the three paths>` → `e1694ba round-8: admit F/O/D` for all three |
| 3 | verdict-preservation differential | re-run here: round-7 gate bytes (`git show 57c3ce6:…` → naming sha `8c5afb0a…`, costume `29a9361c…`, both equal to the old pins) vs current gates (`d9e4e8f4…`/`e6bffd70…`) on `examples/culture-d3/packet.gates.yml`: **byte-identical stdout** (`cmp`), exits 1/1 — naming `506d163231051f294b221d1bb46f78605a689a834ece776b65847a4dc5e3f386`, costume `40d4048c326e10373b8466cb668d51e92a5733668c9e5789533aae8143b63c64` (raw-pipe convention; R9-D09 S6(a) notes the newline-stripped pair `c784dd03…`/`926ceb7d…`) |
| 4 | byte-level no-change traversal | `python3 tools/assemble-culture-d3.py --check` → exit 0, "byte-identical deterministic assembly" (both artifacts); `git status --short -- examples/culture-d3` empty; worktree bytes = HEAD blobs (`packet.json` `0a971d5a3f894030f35c28adaef93ae204000482`, `packet.gates.yml` `6ee7eb395dedbb1399536aca12de727f7242837f`); independent `hashlib` sweep of the freeze's own manifest (no guard code): **24 entries, 0 mismatches** |
| 5 | `expected_exit`/`finding_ids` predeclared, unedited | semantic diff (item 2): `expected_exit: 0` and `finding_ids: []` identical pre/post, as are `profile`, `declared_expectation`, `coverage`, `limits`; 24 manifest entries both sides, none added/removed. The byte diff is a whole-file re-indent (33 insertions/33 deletions) — whitespace-only beyond the three values |
| 6 | stamped revision + date | `LOG.md:2972-2978` round-9 admission entry (2026-10-17; baseline `a7bb205`; "D3 pins refreshed"); post-refresh token `562b76cb48f14bdb7bcf6362f78d8b5c5506934a10d9f912f6c4a0a554bf90fc` (blob `7f298ced1624606ceb6ab7955d9ba24d32c4e42b`) recorded at `reports/round-9/validation.json:24` (`expected_sha256`) and `:991` — the record S4 (`scribe.md:215`) asked to carry post-refresh |
| 7 | independent re-run by a different shard | this run (R10-O04, not the re-piner): item 3 differential + item 4 traversal + the frozen green above |

Record test verdict: **7/7 satisfied**. The counting command's own verdict agrees
(`reports/round-9/validation.json` claims.D `passed: true`, `frozen_replay.exit 0`,
`finding_ids: []`, `drift_paths: []`; both the committed copy and the worktree copy).

### Limits for this row

- This is a re-verification of the record and of behavior neutrality at the current
  revision, not a historical certification of the round-8 repairs themselves (round-8's own
  audit carries that; `d3/check-diagnosis.md:116-117`).
- The freeze document remains unpinned by construction (idx 12 / R9-D09 S4 — another
  fixer's row); the pre/post tokens above are the anchors that row asked for.
- `reports/round-9/validation.json` is uncommitted-modified in the worktree (battery stdout
  hashes and `git_status` changed on a later re-run); the D-claim verdict is `passed: true`
  in both copies, so the re-pin's green does not depend on the dirty delta.

---

## idx 10 — R8-D16 S12: "D03's strict loader fragment cannot parse the lane's own packet (did not propagate)"

**Disposition: `fixed-with-control`** for the shipped artifact, with the filed fragment's
stale snippet **documented as the residual**. The delivered tool now ships an amended
`load_packet_strict` that parses both the exact S12 case and the real 156 KB packet; the
fragment as filed still reproduces the refusal and was **not** landed as-is — which is the
finding's own remedy ("do not land §4.1 as-is").

### Control A — the finding's count still holds

```sh
grep -c '^ *-$' examples/culture-d2/packet.d2.yml     # 312
```

### Control B — the filed fragment reproduces the defect (extraction is faithful)

Extracted §4.1's single python block (302 lines) from `reports/round-8/depth/shard-parser.md`
into `.scratch/d03-fragment.py` and ran it:

```text
load_packet_strict("costumes:\n  -\n    id: GAR-01\n")
 -> {'packet': None, 'findings': [{'code': 'P-UNTERMINATED-FLOW', 'line': 2,
     'detail': "content '-' is not a mapping line"}]}          # byte-for-byte D16's receipt
real packet -> packet is None; first refusal line 82 ("content '-' is not a mapping line")
```

### Control C — the shipped loader parses the lane's own packet (defect did not propagate)

`tools/d2-typed-labels.py` sha256 `0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802`
(= `git show e1694ba:tools/d2-typed-labels.py`, i.e. the committed loader), `run_pipeline`
loads through it (`:2430 load_packet_file` → `:396 load_packet_strict`):

```text
load_packet_strict("costumes:\n  -\n    id: GAR-01\n")
 -> {'packet': {'costumes': [{'id': 'GAR-01'}]}, 'findings': []}
real packet -> parses: 19 top-level keys, costumes 10, lexicon 40, names 8, layers 2,
               findings []
```

The delta is the list-item branch: the fragment accepts only `startswith("- ")`
(fragment lines 190, 194), the shipped `_parse_block` accepts a bare item
(`tools/d2-typed-labels.py:287 first[1] == "-" or …`, `:291 body == "-" or …`).
Shipped selftest: `--selftest` **39/39 exit 0**, including `loader: P-UNTERMINATED-FLOW
refused` (for genuinely malformed input) and `live packet: pipeline evaluates (exit 0/1,
never 2)`; the live run exits 1 with 16 findings and no `P-*` code.

### Residual (documented, not a live defect)

The filed fragment text still contains the defective branch. Per the lane's evidence rule
(filed bytes are not rewritten; corrections are new entries) it was left as-is; this entry
is the correction record. No shipped artifact carries the defect.

### Limits for this row

- The strict loader is a closed subset by design: it refuses a `|` block scalar, so
  `11-costumes.yml` (a *component* file, not the packet) is read via the assembler's block
  extractor (`tools/d2-typed-labels.py:2390-2396`) — deliberate, and outside this row.
- The fragment extraction covers §4.1's one fenced python block; D16's receipt and mine
  match exactly, so the extraction is not in question.

---

## Proposed tracker rows (for the integrator; I did not edit the tracker)

```json
{"idx": 2,  "disposition": "fixed-with-control",
 "control": "reports/round-10/fix-04.md §idx 2: frozen replay exit 0 (stdout sha256 e282a068…); semantic diff a7bb205→9dc18ec = exactly 3 digest values (74496aa8…→562b76cb…); old-vs-new gate differential byte-identical (506d1632…/40d4048c…), exits 1/1; 24/24 manifest entries match; predeclared expected_exit/finding_ids unchanged; record at round-9 d3/check-diagnosis.md:74-75 + d3/scribe.md:205-216 + LOG.md:2972-2978 + validation.json:24,991"},
{"idx": 10, "disposition": "fixed-with-control",
 "control": "reports/round-10/fix-04.md §idx 10: shipped loader 0da0015f parses the exact S12 case and the real 156 KB packet (19 keys, 10 costumes); filed fragment reproduces the refusal (line 82) and was not landed as-is; selftest 39/39"}
```

---

## Appendix A — byproduct receipts (NOT a disposition; offered for idx 4 / R8-D16 S6)

Recorded before the tracker landed, while the index basis was unresolved; they concern
idx 4, which another fixer owns.

- Costume-YAML `native_form: "vinter"` injected into GAR-01 (mirror `.scratch/mirror-s6/`):
  `--emit` differs from baseline **only** in the packet path/digest provenance lines; the
  findings list and stats are identical (16 findings, exit 1) — the key is still not read.
- Label-record channel (`typed_labels`): a supplied native-form for `LEX-GAR-01`
  (`text: vinter`) resolves the GAR-01 `D2L-FORM-UNRESOLVED` hold and the supplied bytes are
  checked — `D2L-NATIVE` on `/v/`, emitted **twice** (R4 loop `:806` and the general loop
  `:808` both fire on the same label — a duplicate-report observation, cosmetic);
  two supplied forms on the same slot → `D2L-DATA` "identity collision", exit 2 (L2).
  Raw outputs under `.scratch/` (uncommitted).

## Reproduction (all from the lane root, 2026-10-17)

```sh
export TMPDIR=$PWD/.scratch
python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json \
        --frozen examples/culture-d3/expected.json            # exit 0, findings []
git show a7bb205:examples/culture-d3/expected.json | sha256sum  # 74496aa8…
git rev-parse HEAD:examples/culture-d3/expected.json             # blob 7f298ced…
python3 tools/assemble-culture-d3.py --check                    # exit 0
grep -c '^ *-$' examples/culture-d2/packet.d2.yml               # 312
python3 tools/d2-typed-labels.py --selftest                     # 39/39, exit 0
```

FILES: reports/round-10/fix-04.md | SUMMARY: Tracker idx 2 (R9-D09 S1) and idx 10 (R8-D16 S12) dispositioned fixed-with-control with re-run controls — D3 re-pin green re-verified with the full 7-item minimum record (frozen exit 0, exactly-3-value semantic diff 74496aa8→562b76cb, byte-identical old-vs-new gate differential, 24/24 manifest match, predeclared expectation untouched, round-9 record + post-refresh token at validation.json:24,991); S12's fragment defect reproduced as filed (real packet refused at line 82) but absent from the shipped loader (exact case + 156 KB packet parse, selftest 39/39), remedy "do not land as-is" satisfied; tracker rows proposed, no other file written.
