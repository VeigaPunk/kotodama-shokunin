- Seat: A03 | executor (audit slice) | claim A (adjacency) | date 2026-10-19 | baseline 4a7aede

# A03 — Audit slice: the examples/ digest repoints + the culture-d3 repoint

Write scope: this file only. Every command below is read-only (`git show`,
`git log`, `git diff`, `git grep`, `sha256sum`, `python3` readers, two
read-only gate runs, one read-only scan of a frozen fixture). Scratch use is
limited to `export TMPDIR=$PWD/.scratch` and one `git archive` extraction
under `.scratch/a03-baseline/`. No filed `run-validation.py` was executed; no
freeze mode was run; no commit, push, install, or network. `git status
--porcelain examples/ tools/gates/frozen/` after every run → empty.

## Verdict

**PASS on four of five boundary legs; one named finding (A03-F1).**

The repoint itself is correct in substance: all six repointed digest cells
equal the live contract bytes, the edit is in-lane, and it introduces no
lore-asset claim. One consequence is unfiled and is a finding: repointing
`examples/handoff-packet.sample.md` invalidated a member of the D3
computational snapshot (`examples/culture-d3/expected.json`), so the
documented frozen check `check-evidence-coupling.py examples/culture-d3/packet.json
--frozen examples/culture-d3/expected.json` now exits 2 (1 × `D3-SNAPSHOT`)
where it exited 0 before r33.

## What the slice covers (population)

- r33 (`da68a6d`) modified exactly **4 files / 6 lines** under `examples/`:
  numstat 1/1, 2/2, 1/1, 2/2 (`git show da68a6d --numstat -- examples/`).
- r34 (`4a7aede`) modified **0** files under `examples/`
  (`git show 4a7aede --stat -- examples/` → no output). So the whole
  "examples digest repoints + culture-d3 repoint" surface is the r33 edit.
- Repointed cells (all old `50c4c2f2…` → new `5f4c02bf…`):
  `examples/handoff-packet.sample.md:21`; `examples/handoff-packet.sample.yml:45,78`;
  `examples/culture-d3/handoff.md:27,74`; `examples/culture-d3/README.md:104`.
- Census alignment: K04's touched-surface census rows 8–11 name exactly these
  four paths, risk class R3 (`reports/round-35/scout/K04-touched-census.md:46-49`).

## Leg 1 — repoint accuracy: GREEN

- Live measurement: `sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md`
  → `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069`.
  All six repointed cells carry exactly this value (`grep -n 5f4c02bf` on the
  four files, lines above). No abbreviated-form mismatch.
- The digest has been stable since `e1694ba` (2026-10-17 17:44:17 -0300, r8
  metadata pass; `git log -1 --format='%H %ci %s' -- <contract>`), so the
  pre-r33 `50c4c2f2…` cells were stale pins of the pre-`e1694ba` bytes, and the
  repoint replaces them with the live reading rather than inventing a value.
- The repoint is the application of r33's own finding A10-F14
  (`reports/round-33/adj/A10-receipt.md:76`, owner integrator/example owner,
  "not repaired by any seat" at finding time) and is recorded resolved in the
  assembled audit: "the former `50c4c2f2…` example pointers now produce zero
  matches" (`reports/round-33/adj/audit-assembled.md:35`) and the fresh scan
  "A recursive scan of `examples/` for the old full digest … returns 0 matches"
  (`reports/round-33/adj/audit-assembled.md:43`).

## Leg 2 — freeze read-set boundary: GREEN

- The r6 freeze (`reports/round-30/handoff/declared-in-r6/expected.json`,
  `inputs`, 58 members) and the r7 freeze
  (`reports/round-34/handoff/declared-in-r7/expected.json`, `inputs`, 58
  members) each pin **32 `examples/` members**. I hashed every member and
  compared to its pin: **32/32 OK in both** (python loop over `inputs`,
  `hashlib.sha256`; zero mismatches, zero missing).
- **None of the four repointed files is a member of either read set**:
  `examples/handoff-packet.sample.{md,yml}`, `examples/culture-d3/handoff.md`
  and `examples/culture-d3/README.md` are absent from both `inputs` maps (the
  frozen fixture provenance note agrees: "handoff/README deliberately
  excluded", `tools/gates/frozen/handoff-packet-check/r9-pre/packet.md:65`).
  So the repoint sits outside both freeze read sets: no freeze drift.
- `examples/culture-d3/expected.json` (`562b76cb…`) *is* a member of both read
  sets and still matches live bytes → that member is intact (see Leg 3 for the
  different, intra-file problem).

## Leg 3 — D3 computational-snapshot boundary: RED → finding A03-F1

Reproduction at HEAD:

```
$ python3 -B tools/check-evidence-coupling.py examples/culture-d3/packet.json \
      --frozen examples/culture-d3/expected.json
{"counts": {"D3-SNAPSHOT": 1, "total": 1}, "exit": 2,
 "findings": [{"id": "D3-SNAPSHOT",
   "message": "manifest digest mismatch for 'examples/handoff-packet.sample.md':
     declared 4e24bd3b887cf148155d89855d3c9eb842d3e325a4fa4302fccaa6c9d23dd712,
     actual   adfd7895461af85275d0170f7a2e057e0c5265ab2bc0ebadc298d2bae7766dc9",
   "record_id": "-"}]}
exit=2
```

Baseline replay (isolated copy, not in-tree):

```
$ rm -rf .scratch/a03-baseline && mkdir -p .scratch/a03-baseline
$ git archive da68a6d^ | tar -x -C .scratch/a03-baseline
$ cd .scratch/a03-baseline && python3 -B tools/check-evidence-coupling.py \
      examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json
{"counts": {"total": 0}, "exit": 0, "findings": []}
exit=0
```

Digest arithmetic (the causal chain, three independent readings):

| reading | command | value |
|---|---|---|
| manifest declares | `examples/culture-d3/expected.json:16` | `4e24bd3b887cf148155d89855d3c9eb842d3e325a4fa4302fccaa6c9d23dd712` |
| pre-r33 bytes | `git show da68a6d^:examples/handoff-packet.sample.md \| sha256sum` | `4e24bd3b…` (equal) |
| HEAD bytes | `sha256sum examples/handoff-packet.sample.md` | `adfd7895…` (mismatch) |

- The member is inside the 24-member manifest (`examples/culture-d3/expected.json:3-28`,
  member at `:16`) and is intended, not accidental: the coverage line names
  "effective reconciliation and handoff contract/sample" (`:32`).
- `examples/handoff-packet.sample.md` sat at `4e24bd3b…` from r2 (`1688790`)
  until r33 (`git log --oneline -4 -- examples/handoff-packet.sample.md`), so
  the manifest member was valid for 30+ rounds and went stale exactly at the
  repoint commit `da68a6d`.
- The manifest's own limits line anticipates this class: "later input edits
  invalidate this snapshot before verdict" (`examples/culture-d3/expected.json:33`).
  The red is therefore the designed invalidation signal; what is missing is
  the **record** and the per-input **re-acknowledgement**.
- Unfiled: `grep -rn "D3-SNAPSHOT" reports/round-3[0-4]/` → 0 hits;
  `grep -n "check-evidence-coupling" reports/round-33/validation.json
  reports/round-34/validation.json` → 0 hits; r33's fresh-check section scanned
  for the old digest *string* inside `examples/` (`audit-assembled.md:43`) but
  did not re-run the frozen leg. The plain (unfrozen) run is still green
  (`check-evidence-coupling.py examples/culture-d3/packet.json` → exit 0).
- Severity is bounded, not catastrophic: no filed round claimed this leg
  green, so no admission is contradicted. It is an unfiled consequence of a
  touched surface — the class claim A exists to catch.
- Cascade warning for any repair: `examples/culture-d3/expected.json`
  (`562b76cb…`) is itself pinned in both freeze read sets' `inputs` and in both
  packets' A-05 rows (`reports/round-30/handoff/declared-in-r6/packet.md:43`;
  `reports/round-34/handoff/declared-in-r7/packet.md:43`). Editing the manifest
  member moves that file's bytes and invalidates those pins, so a repair is a
  declared decision, not a silent edit.
- Remedy options for the integrator (routing, not absorbed here):
  (a) **Record-only (minimal, recommended):** file the invalidation with owner
  and leave the snapshot red-by-design, per its own limits line — no byte
  moves, no freeze pin moves.
  (b) **Per-input re-acknowledgement** of the member to `adfd7895…` citing the
  causing commit `da68a6d` and finding A10-F14 — the r10 precedent
  (`reports/round-10/findings-tracker.json:74`; `reports/round-10/fix-05.md:47`),
  which explicitly warns "never regenerate the manifest from live bytes". This
  option carries the cascade above and needs the declared-in-r7 read-set
  consequence named before it is taken.
  (c) **Revert the repoint** — rejected: it would restore a digest that no
  longer matches the contract bytes and undo a correct r33 fix.

## Leg 4 — frozen-fixture boundary: GREEN

- The two frozen `handoff-packet-check` fixtures hold a byte-identical copy of
  the r7-era `handoff.md` (`0d8d660b…` for both
  `tools/gates/frozen/handoff-packet-check/{r9-pre,r18-post}/packet.md`), and
  that frozen copy still carries the superseded digest at `:27,:74`. This is
  correct freeze semantics — "a frozen input must be a copy, not a live path"
  (`corpus/knowledge/verification/gate-frozen-run-standard.md:7`, KTD-FR-S-0003)
  — and the frozen bytes were not touched by either round
  (`git diff --name-only 139e3b6 4a7aede -- tools/gates/` → empty, matching
  K04's boundary check).
- The fixtures stay self-consistent: each `expected.json` pins
  `packet.md` = `0d8d660b…` and the gate stdout =
  `7c5810479045c26bcc3b1c7364934f53147641504a766eeffeaaec4d2d624685`; my
  read-only run of the gate on the frozen copy reproduced that stdout digest
  exactly, exit 0 (`python3 -B tools/gates/handoff-packet-check.py
  tools/gates/frozen/handoff-packet-check/r9-pre/packet.md | sha256sum`).
- No tool validates the fixture's `input_origin` against the live file
  (`grep -rn "input_origin" tools/*.py tools/gates/*.py` → 0 hits), so the r33
  edit to `examples/culture-d3/handoff.md` does not disturb the frozen
  fixtures or the r33 gate-battery leg that replays their pins
  (`reports/round-33/validation.json`, battery block: both handoff-packet-check
  baselines `reading: pinned`).

## Leg 5 — lore-asset / language boundary: GREEN

- Ownership: `PROVINCE.md:11` owns "this lane's … non-canon examples and
  reports"; all four paths are in-lane; no sibling-repo path is written or
  cited as a target.
- Language scan on the four files (`grep -niE "canon|clearance|promot|ratif|accept|approved|bless"`):
  every hit is a negation or a lore-routed pending state — "not canonized",
  "NON-CANON", "cannot be imported as canon without a lore baseline",
  "bilateral read pending", "canon standing is lore's alone"
  (`examples/handoff-packet.sample.md:1,3,11,15`; `examples/handoff-packet.sample.yml:1,14,70,71`;
  and the D3 pair's pending-§1 wording survives the repoint at
  `examples/culture-d3/handoff.md:27`). No canon, clearance, or promotion
  assertion is introduced by the repoint; the changed cells are digest-only.
- Gate re-runs on the repointed handoff files (read-only):
  `handoff-packet-check.py examples/handoff-packet.sample.md` → exit 0,
  `fields=16/16 glossary-entries=20 findings=0`;
  `handoff-packet-check.py examples/culture-d3/handoff.md` → exit 0, same
  counts. The repoint did not break either scan surface.

## Findings

| id | finding | class | owner | evidence |
|---|---|---|---|---|
| **A03-F1** | The r33 repoint of `examples/handoff-packet.sample.md:21` invalidated the D3 computational snapshot member `examples/culture-d3/expected.json:16`; the documented frozen check now exits 2 with 1 × `D3-SNAPSHOT` (declared `4e24bd3b…` vs actual `adfd7895…`), where the pre-r33 baseline exits 0. No r33/r34 record files the invalidation or the owed re-acknowledgement. | real finding — freeze-manifest member invalidated, unfiled; red is the designed signal, record owed | round-33 repoint author / integrator (record + remedy choice) | reproduction and baseline replay above; `examples/culture-d3/expected.json:16,32,33`; `git show da68a6d^:examples/handoff-packet.sample.md \| sha256sum`; `reports/round-10/findings-tracker.json:74` |
| **A03-F2** | The r33 LOG landed-changes block (`LOG.md:3519-3546`) does not name the four `examples/` repoints; the edit's only records are the assembled audit (`reports/round-33/adj/audit-assembled.md:35,43`) and the validation scope rows (`reports/round-33/validation.json:96-112`). | note — record completeness, not a byte defect | round-33 integrator | `sed -n '3519,3546p' LOG.md` (no `examples/` mention); the audit/validation pointers above |
| **A03-F3** | After the repoint, the only remaining live non-filed citation of the superseded full digest is `corpus/knowledge/verification/gate-frozen-run-standard.md:9` ("Digest of the file as read: `sha256:50c4c2f2…8fb7268c1`"), whose last commit is `e1694ba` itself — a truthful historical read-record, not a live pointer. Named so a later sweep does not re-file it as stale; no repair needed. Frozen copies under `tools/gates/frozen/**` also retain the old digest by design (Leg 4). | observation — no action | integrator (awareness only) | `git grep -n "50c4c2f2" -- . \| grep -vE "^reports/round-[0-9]+/\|^corpus/lessons/\|^LOG.md"`; `git log --oneline -3 -- corpus/knowledge/verification/gate-frozen-run-standard.md` |

## Owed: none

No dependency fragment is missing for this slice (K04's census exists and rows
8–11 cover the four paths; A07/A11 re-run seats can reuse the commands below).
The remedy for A03-F1 is routed to the integrator as a decision, not owed as a
fragment.

## Citations

Paths:lines

- `reports/round-35/targets.json` (A03 seat object: mission, `out: adj/A03-examples.md`); `reports/round-35/claims.json` (claim A `before.state` names "examples digest repoints")
- `PROVINCE.md:11` (owns non-canon examples), `:16-20` (refuses canon/rights), `:22-25` (adjacency contract)
- `examples/handoff-packet.sample.md:21`; `examples/handoff-packet.sample.yml:45,78`; `examples/culture-d3/handoff.md:27,74`; `examples/culture-d3/README.md:104` (the six repointed cells)
- `examples/culture-d3/expected.json:3-28` (24-member manifest), `:16` (the invalidated member), `:32` (coverage names "handoff contract/sample"), `:33` (limits: "later input edits invalidate this snapshot before verdict")
- `examples/culture-d3/README.md:77,91` (documented frozen command and its r7-era observed exit 0 — a dated snapshot by its own header `:18`)
- `reports/round-30/handoff/declared-in-r6/expected.json` (`inputs`, 58 members, 32 under `examples/`, all matching); `reports/round-34/handoff/declared-in-r7/expected.json` (same, all matching)
- `reports/round-30/handoff/declared-in-r6/packet.md:43`; `reports/round-34/handoff/declared-in-r7/packet.md:43` (both pin `examples/culture-d3/expected.json` = `562b76cb…`)
- `reports/round-33/adj/A10-receipt.md:76` (finding A10-F14, stale `50c4c2f2` example pointers); `reports/round-33/adj/audit-assembled.md:35,43` (repoint recorded resolved, zero old-digest matches in `examples/`)
- `reports/round-33/validation.json:96-112` (scope rows listing the four ` M examples/...` files); battery block (frozen handoff-packet-check baselines `pinned`)
- `reports/round-10/findings-tracker.json:74`; `reports/round-10/fix-05.md:47` (r10 precedent: per-input re-acknowledgement citing the causing commit; never regenerate from live bytes)
- `tools/gates/frozen/handoff-packet-check/r9-pre/packet.md:27,74` and `r18-post/packet.md:27,74` (frozen copies retain the superseded digest); their `expected.json` `inputs.packet.md` = `0d8d660b…`, `stdout_sha256` = `7c581047…`
- `corpus/knowledge/verification/gate-frozen-run-standard.md:7,9` (frozen-input-is-a-copy rule; the historical read-record)
- `reports/round-35/scout/K04-touched-census.md:46-49` (rows 8–11, the same four paths, risk class R3)

Commands run (read-only unless noted)

- `git show da68a6d --numstat -- examples/` → 1/1, 2/2, 1/1, 2/2 (4 files, 6 lines)
- `git show 4a7aede --stat -- examples/` → empty (r34 touched nothing under `examples/`)
- `sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md` → `5f4c02bf…f79069`
- `git log -1 --format='%H %ci %s' -- corpus/knowledge/synthesis/worldbible-integration-contract.md` → `e1694ba` 2026-10-17 17:44:17 -0300
- python loop over `inputs` in both freeze `expected.json`s: 32/32 examples members match live bytes in each; none of the four repointed files is a member
- `python3 -B tools/check-evidence-coupling.py examples/culture-d3/packet.json` → exit 0, findings []
- `python3 -B tools/check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json` → **exit 2, 1 × D3-SNAPSHOT** (message quoted above)
- `rm -rf .scratch/a03-baseline && mkdir -p .scratch/a03-baseline && git archive da68a6d^ | tar -x -C .scratch/a03-baseline` then the same frozen command inside the copy → exit 0, findings []
- `git show da68a6d^:examples/handoff-packet.sample.md | sha256sum` → `4e24bd3b…`; `sha256sum examples/handoff-packet.sample.md` → `adfd7895…`
- `git log --oneline -4 -- examples/handoff-packet.sample.md` → `da68a6d`, `1688790` (bytes unchanged r2→r33)
- `python3 -B tools/gates/handoff-packet-check.py examples/handoff-packet.sample.md` → exit 0, 16/16, glossary 20, findings 0
- `python3 -B tools/gates/handoff-packet-check.py examples/culture-d3/handoff.md` → exit 0, 16/16, glossary 20, findings 0
- `python3 -B tools/gates/handoff-packet-check.py tools/gates/frozen/handoff-packet-check/r9-pre/packet.md | sha256sum` → `7c581047…` (equals the fixture's pinned stdout), exit 0
- `git status --porcelain examples/ tools/gates/frozen/` → empty after all runs
- `git grep -n "50c4c2f2" -- .` (full stale-digest census, classified in A03-F3)
- `grep -rn "D3-SNAPSHOT" reports/round-3[0-4]/` → 0 hits; `grep -n "check-evidence-coupling" reports/round-33/validation.json reports/round-34/validation.json` → 0 hits
- `grep -rn "input_origin" tools/*.py tools/gates/*.py` → 0 hits
