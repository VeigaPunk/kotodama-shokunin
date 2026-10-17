# R9-O verifier rerun — `handoff-packet-check` frozen run `r9-pre`

- shard: round-9 claim O, targets `R9-O01..O14` — the independent re-run/validate seat for
  `handoff-packet-check`. Author half: `reports/round-9/baselines/handoff-packet-check/author.md`.
  Baseline bytes verified here: `packet.md`, `expected.json`, `run.log`, `freeze.txt`
  (byte-identical copies at `tools/gates/frozen/handoff-packet-check/r9-pre/`).
- date: 2026-10-17, measured 17:47–17:56 -03 (`date -Is`); lane revision
  `a7bb205d3aecdaa24d91c047c8719cd8689e4ddd` (round-9 claims commit, pre-integration).
- standard followed: `corpus/knowledge/verification/gate-frozen-run-standard.md` §4
  (`expected.json` fields), §5 (freeze procedure, used as the verify recipe) and §6 (digest
  check first, gate-revision check, then verdict; tamper semantics and class mapping).
- scope: the lane was read-only for this seat; **only this file was written inside the repo**;
  no commits, no gate change, no shared file touched (README/SKILL/corpus are the orchestrator's).
  Scratch lived outside the repo at `/home/vgpnk/.cache/kotodama-r9-ho-rerun/` because `/tmp` is
  inode-exhausted on this host (`df -i /tmp` → `1048576 1048576 0 100%`; `mkdir /tmp/...` →
  `No space left on device`). All gate runs below executed in that scratch copy tree, never on a
  live path.

## 1. Verdict

**Independent rerun matches the author's frozen run: §6 steps 1–3 PASS on a copied tree, and
both tamper drills behave per the standard.** The committed `clean` verdict (exit 0, empty
finding-ID set) is re-measurable from the snapshot bytes alone, and the digest pin refuses an
edit to those bytes — including the silent case where the gate's own stdout stays identical.
Two integration caveats, neither touching the bytes or the verdict, are recorded in §7.

## 2. Verified bytes (sha256, measured 2026-10-17 17:52–17:54 -03)

| file | sha256 |
|---|---|
| `packet.md` (graded snapshot; both homes) | `0d8d660bf9797d1c15da477f96ded75553a8d2ca7f04f75aa86a8a65e28fd2fc` |
| `run.log` (frozen stdout; both homes) | `7c5810479045c26bcc3b1c7364934f53147641504a766eeffeaaec4d2d624685` |
| `expected.json` (17:52:19 revision; both homes) | `9dc21cd508e3dcfb225564cdccf65a8f88d9768029e876ac7e47d4c55f21c690` |
| `freeze.txt` (17:53:24 revision; both homes) | `f83ac07529faf05e14a3e545f0fca22ff6406c5dd06c5a60cca555c720eba957` |
| `author.md` (17:53:35 revision; reports home only; not a pinned input) | `c82bb4637e081ad2687d111fc8f39b118a94522a6c3e4b2ee2412bb6639ad750` |
| gate `tools/gates/handoff-packet-check.py` | `e2fa3223b2aa57382807c51099a4360c1a9cc2559d5b4bedad1b54e9ab0ad575` |
| fixture `tools/gates/fixtures/handoff-packet-check.md` | `da066ec0e97b348e196e6b058a5a5179dfb7380339cd018324de6e9ae70ff0c8` |

- Command: `sha256sum` over the paths above (and `cmp` pairs) at 17:47–17:54 -03. `packet.md`,
  `run.log`, `expected.json` and `freeze.txt` are byte-identical across the two homes (`cmp`
  clean, 4/4; re-checked 17:53 and 17:54). `author.md` lives only in the
  `reports/round-9/baselines/handoff-packet-check/` home — the frozen home carries the four §3
  files only (`ls tools/gates/frozen/handoff-packet-check/r9-pre/`, 17:54).
- `expected.json` fields (read at 17:52): `schema` `kotodama-frozen-run-v1`, `gate`
  `handoff-packet-check`, `baseline_id` `r9-pre`, `revision` `a7bb205d…`, `inputs`
  `{packet.md: 0d8d660b…}`, `expected {exit: 0, class: clean, findings: []}`,
  `stdout_sha256 7c581047…`, plus `command` / `input_origin` / `frozen_at` / `frozen_by`.
  All §4-required fields present; `baseline_id` / `command` / `input_origin` are extra
  discovery keys (author states this in `author.md` §5; the battery ignores extras — §6 below).
- Snapshot provenance, re-measured by me at 17:51 -03:
  `cmp examples/culture-d3/handoff.md reports/round-9/baselines/handoff-packet-check/packet.md`
  → identical; both digests `0d8d660b…`. The live origin may advance later in the round; the
  pin protects the `r9-pre` bytes only (the baseline makes no claim about later edits).

## 3. §6 walk, steps 1–3 (copied tree)

Copy tree: `/home/vgpnk/.cache/kotodama-r9-ho-rerun/final/tree/` = the gate script plus the
baseline directory, copied byte-for-byte at 17:52:43 -03.

```bash
S=/home/vgpnk/.cache/kotodama-r9-ho-rerun; L=<lane>
mkdir -p $S/final/tree/tools/gates $S/final/tree/reports/round-9/baselines
cp $L/tools/gates/handoff-packet-check.py $S/final/tree/tools/gates/
cp -r $L/reports/round-9/baselines/handoff-packet-check $S/final/tree/reports/round-9/baselines/
cd $S/final/tree
```

| # | command | observed (2026-10-17) |
|---|---|---|
| 1 | python heredoc: recompute `inputs` digests against `expected.json` (the standard's step 1) | `inputs[packet.md] -> OK (0d8d660bf9797d1c…)` |
| 2 | same heredoc: `sha256(gate copy)` vs `gate_sha256` | `OK` — `e2fa3223b2aa5738…`; no `gate_revised` |
| 3 | `python3 tools/gates/handoff-packet-check.py reports/round-9/baselines/handoff-packet-check/packet.md` | exit **0**; stdout `INFO scan: fields=16/16 glossary-entries=20 findings=0`; stderr empty; observed finding-ID set `[]` == expected `[]`; stdout byte-equal to `run.log`, sha256 `7c581047…` == `stdout_sha256` |
| 4 | same run from another cwd (`$S/final`, relative paths) and the stdin form (`-`) | exit 0, same stdout line both ways |

- `git diff --stat e1694bad6ac96aca45a11ca5746582b275929355..HEAD -- tools/gates/handoff-packet-check.py`
  → empty (count 0 lines of diff, measured 17:51 -03): **no gate behavior change** since the
  round-8 admit revision; `git status --porcelain` for the gate and its fixtures → empty.
- Gate self-test, re-run by me at 17:47 -03 from the lane root:
  `python3 tools/gates/handoff-packet-check.py --selftest` → exit 0,
  `selftest: OK — fixture findings 11 across 9 ids (HO-BASELINE, HO-CANON-CLAIM,
  HO-CANON-MARKER, HO-CONTRACT-REF, HO-DEP-FLOAT, HO-EMPTY, HO-GLOSS-ETYM,
  HO-MANIFEST-DIGEST, HO-MISSING); clean control exit 0; …` — capability half only; the
  frozen run is the measurement half. An earlier independent run of the gate over a byte copy
  of the committed fixture (scratch, 17:47) printed the same 9-ID set with exit 1, matching
  `tools/gates/fixtures/handoff-packet-check.expected`.

## 4. Tamper and falsifiability slices (scratch copies only)

| # | edit (scratch copy of `packet.md`) | observed |
|---|---|---|
| 1 | verifier-appended byte: `printf '\n<!-- verifier appended byte -->\n' >> tampered.md` → digest `bb1a6d8e26b9a6ea456f5c345c0cd29a5d3aea817abab3182faeeac35b074c84` ≠ pin `0d8d660b…` | digest step reads **`snapshot_tampered`** — could-not-evaluate, check exit 2; the gate re-run over the same edited copy still printed `INFO scan: fields=16/16 glossary-entries=20 findings=0`, exit 0. Only the digest step can see this edit; a verdict-only comparison would call it a pass. |
| 2 | author's `t1.md` (`+ <!-- one appended comment line -->`, `.scratch/r9-handoff-author/`) | I re-hashed it: `d9b80af33c508945b5d70af9767266662d6280b61b31c10fb054945d5cd5f9c3`, equal to the author's stated digest; gate exit 0, same stdout line (silent under the verdict) |
| 3 | author's `t2.md` (`canon_standing` rewritten to a producer-side certification) | re-hashed: `5af09f9b836103292fe271f4dd9166f59a8d44f44a89cd0ccd19b59b2106868d` (matches author); gate exit **1**, `FINDING HO-CANON-CLAIM: FAIL — producer-side canon certification at line 20 …` — the committed `clean` verdict is falsifiable, not vacuous |

`diff` of `t2.md` vs `packet.md` (line 20): `- canon_standing: not canonized — lore disposition
required (lore-shokunin owns canon)` → `+ canon_standing: canonized — producer ratifies this
packet as canon`.

## 5. §6 class-mapping emulation (standalone checker in scratch, 17:52 -03)

A read-only checker (scratch only, not committed) implementing the standard §6 table over the
copied tree; one row per condition, all measured:

| condition (variant in scratch) | reading | check exit |
|---|---|---|
| intact baseline | `match (clean / exit 0)` | 0 |
| appended byte in `packet.md` | `snapshot_tampered (packet.md)` | 2 |
| gate copy edited (`+ # gate edit`) | `gate_revised` | 2 |
| `expected.json` written as `{not json` | `could-not-evaluate (expected.json malformed)` | 2 |
| `inputs` emptied (`{}`) | `unpinned (legacy)` | 2 |
| `expected.exit` flipped to 1 with the snapshot intact | `failed (observed exit 0, ids [])` — real drift, preserved | 1 |
| `expected.json` absent | `could-not-evaluate (no baseline)` | 2 |

Documented limit (demonstrated, not assumed): editing the snapshot **and** its `inputs` pin
together makes step 1 read `OK` — `expected.json` does not self-digest. The commit (content
addressing, KTD-FR-S-0010) is the anchor, not the file; the orchestrator's integration commit
carries the bytes that were reviewed here.

## 6. Battery (round-9 O15) cross-check on the same copied tree

`tools/check-gate-battery.py` (already carrying the O15 baseline check) was copied with the
seven gates and the fixture tree into the scratch tree; baseline root
`tools/gates/frozen/` holding only this baseline (17:52 -03):

- Full battery run: **all 7 gate selftests `pass`** (exit 0 each, in the mirror),
  `originals.preserved: true` (28 files hashed before/after, 0 modified/added/deleted);
  battery exit **2** because the six other gates are uncovered *by construction of the
  single-baseline scratch tree* (`BASELINE-GATE-UNCOVERED` ×6) — not a defect of this baseline.
- This baseline's record: `reading: pinned`, `inputs_checked: 1`, `gate_sha256: match`,
  `stdout_pin: match`, `verdict_replay: not-run…` (the battery verifies digests/pins; the
  verdict comparison is this rerun's receipt).
- Tampered variant (appended byte): reading **`snapshot_tampered`**, finding
  `BASELINE-TAMPERED`, exit 2 — never a silent pass.
- Pin-swap variant (snapshot + pin edited together): reading `pinned` — the same un-self-digested
  limit as §5, now measured through the battery's own inspector.
- Malformed variant (`{not json`): reading `no baseline`, finding `BASELINE-MALFORMED`, exit 2.
- Missing `expected.json` (snapshot present): no baseline records, `BASELINE-NONE-FOUND`, exit 2.

## 7. Findings for the orchestrator (ranked; evidence attached)

1. **Dual home, two byte-identical copies** — `reports/round-9/baselines/handoff-packet-check/`
   (round-9 pair-protocol home) and `tools/gates/frozen/handoff-packet-check/r9-pre/` (the
   standard §3 root and a battery default root). `cmp` clean 4/4 at 17:53. The round is split
   across three baseline roots (`tools/gates/expected/`, `tools/gates/frozen/`,
   `reports/round-9/baselines/`); the counting command and any discovery sweep must cover all
   three, or the round standardizes on one root by `git mv` (the author's `freeze.txt` §“root and
   relocation” records the same observation). One baseline id `r9-pre` — never treat the two as
   two freezes.
2. **`run.log` is gitignored** — `git check-ignore -v reports/round-9/baselines/handoff-packet-check/run.log`
   → `.gitignore:3:*.log` (exit 0, re-measured 17:52). Without `git add -f` (or a negation such
   as `!/**/run.log`) the committed baseline is missing a §3-required file. Both homes affected.
3. **Extra keys beyond §4** in `expected.json` (`baseline_id`, `command`, `input_origin`).
   Harmless for the battery (it reads the §4 fields; extras ignored — measured in §6), but any
   validator must not require key-exactness the standard does not state.
4. **Untracked author scratch** — `git status --porcelain` shows `?? .scratch/`
   (`.scratch/r9-handoff-author/{t1.md,t2.md}`); not gitignored. Remove or ignore before the
   integration commit so it cannot be added by a broad `git add`.
5. **`revision` names the pre-integration tree** `a7bb205d…`; the orchestrator's round-9 commit
   will carry the baseline (workers do not commit in this lane). Any later edit to the gate
   changes `gate_sha256` → `gate_revised`, re-freeze, never re-pin (standard §6).

## 8. Reproduction recipe (a stranger, from the integration commit)

```bash
cd <lane>                       # any tree carrying the round-9 integration commit
D=reports/round-9/baselines/handoff-packet-check
python3 - "$D/expected.json" <<'PY'          # §6 step 1
import hashlib, json, pathlib, sys
b = pathlib.Path(sys.argv[1]); exp = json.loads(b.read_text())
for rel, want in exp["inputs"].items():
    got = hashlib.sha256((b.parent / rel).read_bytes()).hexdigest()
    print(rel, "OK" if got == want else f"snapshot_tampered {got}")
PY
sha256sum tools/gates/handoff-packet-check.py   # §6 step 2: vs gate_sha256 e2fa3223…
python3 tools/gates/handoff-packet-check.py $D/packet.md; echo "exit=$?"   # §6 step 3: expect 0
cmp <(python3 tools/gates/handoff-packet-check.py $D/packet.md) $D/run.log && echo "stdout byte-equal"
python3 tools/check-gate-battery.py             # O15: this baseline reads `pinned`
```

(Never run these against `examples/culture-d3/handoff.md` and call it the baseline: the graded
bytes are the snapshot copy, standard §3.)

## 9. Limits of this rerun

- It re-measures digests, pins and the verdict of these bytes under this gate revision. It does
  **not** judge the packet's design quality, the truth of its claims, or canon standing; a
  matching run never becomes a design PASS (standard §10).
- The §6 class-mapping emulation in §5 is a standalone scratch checker, not the battery; the
  battery cross-check (§6) independently covers the digest/pin classes, and the verdict
  comparison is this file plus the frozen `run.log`.
- The scratch battery run exits 2 for uncovered sibling gates by construction; the lane-tree
  battery result across all seven gates belongs to the O15 seat, not here.
- `author.md`/`freeze.txt` were revised during my measurement window (17:49 → 17:53); the
  digest table in §2 pins the revisions I read. `packet.md` and `run.log` have been stable since
  17:49:02, and the `inputs`/`gate_sha256` pins were unchanged across the author's revisions.

Measured-by: round-9 O-axis verifier seat (role label only). Date: 2026-10-17.
