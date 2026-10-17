# myth-consistency-gate — frozen-run baseline, author fragment (round 9, claim O)

- role: **author seat** of the `myth-consistency-gate` baseline pair (author + independent
  auditor). This seat wrote the baseline files in this directory and this fragment; the
  auditor seat independently re-runs and validates them. Nothing here was committed — the
  orchestrator integrates and commits once per round (lane AGENTS.md).
- date: 2026-10-17, local (-03:00). Freeze time `2026-10-17T17:50:38-03:00`.
- lane revision at freeze: `a7bb205d3aecdaa24d91c047c8719cd8689e4ddd` (HEAD). Declared
  round-9 `baseline_revision` is `e1694bad6ac96aca45a11ca5746582b275929355`; the two differ
  only in `reports/round-9/{claims,targets}.json` —
  `git diff --stat e1694ba..HEAD` = 2 files changed, 159 insertions, 0 deletions, and
  `git diff --stat e1694ba..HEAD -- tools/gates examples corpus` is empty. The graded
  artifact tree is identical between both revisions; recorded, not assumed.
- standard followed: `corpus/knowledge/verification/gate-frozen-run-standard.md` §4 (required
  `expected.json` fields), §5 (freeze procedure), §6 (verify procedure, tamper semantics,
  class mapping), §7/§9 (first real baseline grades a D2 protocol packet; this gate's turn
  in the §9 gate order). Self-test = capability, frozen run = measurement (two-evidences).

## 1. Files this seat wrote (all under `reports/round-9/baselines/myth-consistency-gate/`)

| file | sha256 / content |
|---|---|
| `packet.yml` | `e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643` — byte copy of `examples/culture-d2/packet.d2.yml` (cmp clean) |
| `run.log` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` — 0 bytes; a clean run prints no FINDING lines |
| `expected.json` | schema `kotodama-frozen-run-v1`; all §4 required fields plus advisory pins (see file) |
| `freeze.txt` | freeze procedure, 10 numbered steps, quoted observed results |
| `author.md` | this fragment |

`expected.json` verdict: `expected.exit 0`, `expected.class clean`, `expected.findings []`;
`gate_sha256 5368b13542cd4b8a5bd850d83835e588df13a72b7d6c502b2aa016ee36b95f08`
(`tools/gates/myth-consistency-gate.py` at freeze).

## 2. Why this input, this root, this phase

- **Input — the D2 protocol packet.** §7 of the standard names the committed fixture as the
  format example and says the *first real* baseline should grade a D2 protocol packet once
  one exists; §9 fixes the D2 packet's gate order (phonology → lexicon → naming → myth →
  costume → handoff). The packet exists (`examples/culture-d2/packet.d2.yml`, 3345 lines)
  and this gate is its fourth grader, so the graded input is a byte copy of it. A
  fixture-only baseline would re-measure the self-test's own synthetic input; the D2 packet
  is the artifact whose future edits these pins are meant to catch.
- **Root — `reports/round-9/baselines/<gate-name>/`.** The round-9 shard map places the
  fragment per gate there; a peer fragment (naming-collision-gate author) declares the same
  root and a discovery glob `reports/round-9/baselines/*/expected.json`, and the
  phonology-sanity-gate pair works in the same shape. The standard's §3 directory shape
  (`<gate-name>/<baseline-id>/`) is kept as directory = `<gate-name>` plus the
  `baseline_id` field inside `expected.json`. Divergent peer roots observed in flight are
  reported in §6, not absorbed.
- **Phase — `r9-pre`.** No gate-behavior edit lands in round 9 (claim O forbids them;
  `git diff --stat e1694ba..HEAD -- tools/gates` empty). Had one landed, a `r9-post`
  baseline would be required instead of rewriting this one (append-only rule).

## 3. Commands and observed results (2026-10-17, all re-executed, outputs quoted)

| # | Command | Observed |
|---|---|---|
| 1 | `git status --porcelain tools/gates/myth-consistency-gate.py examples/culture-d2/packet.d2.yml` | empty — no tracked modification around gate or input |
| 2 | `python3 tools/gates/myth-consistency-gate.py --selftest` | exit **0**: "selftest: OK — fixture exit 1; planted IDs present: MC-P01, MC-P02, MC-M01, MC-M02, MC-S01, MC-S02; clean control exit 0 (0 findings); fixture and expected verified against the embedded constants under tools/gates/fixtures/". `git status` before/after identical; fixture digests unchanged (yml `f94a700c…`, expected `c871b6d3…`) |
| 3 | `cp examples/culture-d2/packet.d2.yml <baseline>/packet.yml; cmp` | byte-identical | 
| 4 | `python3 tools/gates/myth-consistency-gate.py <baseline>/packet.yml > <baseline>/run.log` | exit **0**; stdout empty (0 bytes) — clean verdict, no FINDING lines |
| 5 | same gate over the live path `examples/culture-d2/packet.d2.yml` | exit 0; stdout byte-identical to `run.log` — path-independent |
| 6 | isolated mirror (gate + packet copies in `/dev/shm`, different cwd) | exit 0; stdout byte-identical — run is not directory-dependent |
| 7 | tamper: scratch copy + `printf '\n# tampered byte\n' >>` | sha256 `265bd5c6a37fd90a5e0692ce39a6564622e0a787bc4293cf7dcedf944f7009d7` ≠ pinned `e0f21509…` → `snapshot_tampered` (could-not-evaluate); the gate over the tampered copy still exited 0 with stdout byte-identical to `run.log` (both empty) — under a clean verdict **only** the digest step detects the edit |
| 8 | bounded mutant: MOT-04 `index_checked: true` → `cf_atu: "ATU 1200"` + `index_checked: false` | sha256 `2e6c2d675f985dd6f6de5f42c8edcb6943f26de1b83661ec7b1c4fc0a932da5c`; exit **1**: `FINDING MC-M02: motif MOT-04 claims comparison 'ATU 1200' without a checked entry, edition, or narrative witness [spec §4 MC-M02]` — the clean verdict is contingent on the graded bytes |
| 9 | digest re-verify against the `inputs` pin | `packet.yml: OK`; exit 0 |
| 10 | `df -i /tmp` | `tmpfs 1048576 1048576 0 100%` — `/tmp` inode-exhausted during this wave; scratch controls used `/dev/shm` (observed hazard, not a blocker: every command ran) |

Reading of the §6 procedure (the reason rows 7–8 are built the way they are): digest check first → gate-revision check →
verdict comparison. This baseline's `run.log` being empty makes the point sharply — a
byte-comparison of stdout can never distinguish the tampered copy from the frozen one
here; the `inputs` digest map is the only detector, which is why it is populated even
though the gate reads exactly one file (`myth-consistency-gate.py:847-849` is the graded
read path; `1058-1095` is selftest-only).

## 4. What this proves, and what it does not

- Proves: these exact bytes (packet `e0f21509…`, gate `5368b135…`) produced this exact
  verdict (exit 0, no findings) under this revision; the verdict is reproducible from a
  copy in isolation; an edit to the snapshot reads `snapshot_tampered` rather than a silent
  pass; the verdict is sensitive to a two-token semantic edit.
- Does not prove: that the D2 packet is good design, that `MC-*` semantics match real-world
  scholarship, or that the packet is canon. A frozen run is lane-local engineering
  evidence; lore-shokunin owns world-bible decisions (lane AGENTS.md).
- The `--selftest` is capability evidence only and never substitutes for this run; neither
  substitutes for the other (§2 of the standard).
- Controls in §3 rows 5–8 are author-side re-executions. The independent re-run is the
  paired auditor seat's job; this fragment does not claim it.

## 5. Integration notes (for the orchestrator; none of these is a lane-local edit)

1. **`run.log` is ignored by `.gitignore`** (`*.log`, line 3) and is empty; force-add it:
   `git add -f reports/round-9/baselines/myth-consistency-gate/run.log`.
2. **Registry rows** (O17 scribe): the pinned-value path for `myth-consistency-gate` gains
   `reports/round-9/baselines/myth-consistency-gate/expected.json` (verdict map unchanged,
   no gate behavior changed).
3. **Battery extension** (O15): discovery here is `reports/round-9/baselines/*/expected.json`;
   digest-verify must run before verdict comparison, and a digest mismatch must read
   could-not-evaluate (exit 2), never a pass — the §3 row-7 measurement is the reason.
4. The standard's §3 `tools/gates/frozen/README.md` index is a shared file across all seven
   gate shards and was deliberately **not** written here to avoid seven-way writes to one
   path; the natural home for those rows is the registry scribe's
   `reports/round-9/baselines/registry.md`.

## 6. Contested scope — reported, not absorbed (lane stop rule)

Three baseline roots were observed in flight this round (2026-10-17):

- `reports/round-9/baselines/<gate-name>/` — **this baseline**; naming-collision-gate
  author (its `expected.json` `layout_note` declares the same root + discovery glob) and
  the phonology-sanity-gate pair ("the author seat owns expected.json, the snapshot copy,
  run.log and freeze.txt in the same directory").
- `tools/gates/expected/<gate-name>/r9-pre/` — costume-era-consistency-gate author.
- `tools/gates/frozen/<gate-name>/<baseline-id>/` — handoff-packet-check author (the
  standard's §3 literal root).

This seat did not duplicate the baseline into the other roots: the standard §3 resolves a
bare baseline id under exactly one gate directory and two candidates fail closed, and a
second copy of the same id would manufacture that ambiguity. One baseline, one root. The
integrator should reconcile the seven authors onto one root before the O16 runner counts
"7/7 carry a baseline"; a root-agnostic discovery that maps rows by the `gate` field and
fails closed on duplicate ids across roots would be robust to the divergence if it cannot
be reconciled.

## 7. Handoff to the paired auditor seat

Verify independently (in a copied tree, never against this live path): recompute the
`inputs` digests and `gate_sha256` against `expected.json`; re-run the gate over a fresh
copy of `packet.yml` and expect exit 0 / no findings; tamper one byte and confirm the
digest step, not the run, refuses comparison. Findings that contradict any number in this
fragment should be filed against it, not silently smoothed.
