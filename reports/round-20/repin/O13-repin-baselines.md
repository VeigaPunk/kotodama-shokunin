# R20-O13 — the baseline surface: round-9 baselines do **not** pin the projector (negative reading), the D4 family does

- round: 20 (operator: loop 2 of 3, build round 4 of 4) · shard: **O11..O14**
  (re-pin ×4) · owner: L2 worker, kotodama-shokunin lane.
- assignment (verbatim): "O R20-O11..O14 (re-pin x4): update the pins that name
  d2-typed-labels.py (round-18 repin-d2 rows, round-16 v2-07 expected.json pins,
  **round-9 baselines if pinned**) as NEW rows with the before/after table
  extended; replay green; reports/round-20/repin/."
- date: 2026-10-18, readings 12:56Z–13:16Z.
- canon: NON-CANON engineering evidence; a negative reading is a measured result,
  not a clearance.
- writes: this file only (plus the evidence files named in §5). No baseline byte
  of any round is edited.
- **status: COMPLETE. The `if pinned` clause resolves to a measured negative for
  round 9 and to a peer-landed new revision for the D4 family; both readings are
  below with their commands.**

## 1. The scan (command-carried)

```sh
python3 - <<'EOF'
import json, pathlib
root = pathlib.Path(".")
files = sorted(p for base in ("reports/round-9/baselines", "tools/gates/expected", "tools/gates/frozen")
               for p in (root / base).rglob("expected.json"))
total = 0; naming = []
for path in files:
    inputs = (json.loads(path.read_text()).get("inputs") or {})
    total += len(inputs)
    hits = [k for k in inputs if "d2-typed-labels" in k]
    if hits: naming.append((str(path), hits, len(inputs)))
print(len(files), "expected.json files;", total, "pins;", len(naming), "name the projector")
for row in naming: print("  ", row)
EOF
```

Result at 13:12Z (the transcript is `evidence/baseline-projector-scan.txt`):

```text
expected.json files: 18
total pins across them: 79
files whose inputs name tools/d2-typed-labels.py: 2
   tools/gates/expected/d4-typed-labels-check-gate/r19-pre/expected.json  6 inputs
   tools/gates/expected/d4-typed-labels-check-gate/r20-post/expected.json 4 inputs
```

## 2. Round-9 baselines: not pinned → nothing to re-pin

The eight round-9 files the lane's battery discovers pin **27 inputs in total,
none of them the projector**:

| round-9 file | gate | pins | names the projector |
|---|---|---:|---|
| `reports/round-9/baselines/naming-collision-gate/expected.json` | naming-collision-gate | 1 (`packet.yml`) | no |
| `reports/round-9/baselines/myth-consistency-gate/expected.json` | myth-consistency-gate | 1 | no |
| `reports/round-9/baselines/handoff-packet-check/expected.json` | handoff-packet-check | 1 (`packet.md`) | no |
| `tools/gates/expected/phonology-sanity-gate/r9-pre/expected.json` | phonology-sanity-gate | 1 | no |
| `tools/gates/expected/costume-era-consistency-gate/r9-pre/expected.json` | costume-era-consistency-gate | 1 | no |
| `tools/gates/frozen/handoff-packet-check/r9-pre/expected.json` | handoff-packet-check | 1 | no |
| `tools/gates/frozen/lexicon-coverage-audit/r9-pre/expected.json` | lexicon-coverage-audit | 1 | no |
| `tools/gates/frozen/provenance-audit/r9-pre/expected.json` | provenance-audit | 20 (corpus copies) | no |

The same holds for the seven round-18 `r18-post` baselines. Reason, stated
plainly: those baselines grade the seven **structural gates**, and each pins the
gate script (`gate_sha256`) plus the packet or corpus copies the gate reads — the
typed-label projector is not in their read set. So the `if pinned` clause has no
subject in round 9, and **no round-9 pin was created or moved by this seat**. A
re-pin of a pin that does not exist would be filler.

## 3. The D4 family: the one baseline surface that does pin the projector

`tools/gates/expected/d4-typed-labels-check-gate/r19-pre/expected.json` (round 19,
filed, sha `93b84da0cbd3b2a8531319555c9848c0fb85a79e675a4fc8768096e2b22f776a`)
pins six inputs including `tools/d2-typed-labels.py` at `0da0015f…` **and two D2
component copies** (`examples/culture-d2/components/11-costumes.yml`,
`12-rank-rules.yml`) — the wart in one line: a D4 baseline had to declare D2
inputs because the projector's era-alias leg read the D2 component for a D4
packet.

The round-20 input edit (the projector) and the wart's close make that a later
phase, and the standard answers a moved input with a **new baseline id**. The
O-wart seat (R20-O05..O10) landed it; this seat verified it rather than
duplicating it:

| item | `r19-pre` (filed, unchanged) | `r20-post` (new, peer-landed) |
|---|---|---|
| `expected.json` sha256 | `93b84da0…` | see the file (`tools/gates/expected/d4-typed-labels-check-gate/r20-post/expected.json`) |
| pinned inputs | 6 | **4** — the two D2 component copies are gone |
| projector pin | `0da0015f…` | `76536a92…` |
| graded input | `typed-labels.d4.yml a59990bb…` | `typed-labels.d4.yml cbcf997f…` (round-20 build) |
| gate `gate_sha256` | `05f99629…` | `05f99629…` (the adapter did not move) |
| stdout pin | `3aa55393…` | `0d92cb4f…` (path string inside the stdout line) |
| battery leg | `reading: pinned`, `inputs_checked 6`, gate/stdout `match`, `findings []` | `reading: pinned`, `inputs_checked 4`, gate/stdout `match`, `findings []` |

Battery readings around the change (`python3 tools/check-gate-battery.py`,
default roots, exit 0 both times):

```text
12:58Z  baselines_found 17, pinned 17, coverage "9/9", gates_uncovered [], readings {"pinned": 17}
13:14Z  baselines_found 18, pinned 18, coverage "9/9", gates_uncovered [], readings {"pinned": 18}
```

The `+1` is the new revision; the two D4 legs (`r19-pre`, `r20-post`) both read
`pinned` with no findings. Note what the battery checks: the **in-baseline
copies** against their pins and the gate script against its pin — so the filed
`r19-pre` leg stays green after the projector moves (its projector copy is a
frozen snapshot), and a new revision is a *record*, not a repair.

## 4. What this leg did and did not do

- did: measure the surface (command above), report the negative for round 9 with
  the per-file table, verify the peer's `r20-post` revision and the battery
  readings, and record both in the round-20 table (`O14-repin-table.md`).
- did not: create a second `r20-post` for the D4 gate (the peer's revision is a
  complete pin of the same run), and did not touch `r19-pre` (filed round 19).
- would have: if the peer's `r20-post` had not landed, this seat's builder had a
  ready `--d4` mode producing the same layout; it was exercised in a full-repo
  mirror in `/var/tmp` (battery read `18/18`, exit 0) and then not run in the
  live tree because the peer's revision is already there.

## 5. Evidence files (landed with this report)

| file | what it is |
|---|---|
| `evidence/baseline-projector-scan.txt` | the §1 scan transcript |
| `evidence/readings-before.txt` | the 12:56Z before readings (hashes, pin surfaces, D2 controls, replay) |
| `evidence/readings-after.txt` | the 13:14Z after readings (replays, battery, frozen-verify, D2 controls, filed re-hashes) |
| `evidence/runner-claim-o.json` | the counting command's claim-O section at 13:16Z (failures `[]`) |
| `evidence/runner-final.json` | the counting command at 13:19Z: exit 0, claims D/O/C all `failures: []`, no missing dependencies |
| `evidence/readings-final.txt` | the post-freeze verification block (replay, selftests, v2-07 verifies, filed-path controls) |

## 6. Limits

- A baseline pins bytes and a verdict; `pinned` in the battery is a coverage
  reading, not a quality reading. Neither D4 leg certifies the projection.
- The battery verifies digests and pins, never re-runs a baseline's verdict
  (`verdict_replay: "not-run"`); the verdict comparison belongs to each
  baseline's own re-run receipt.
- The scan covers `expected.json` under the three default baseline roots. A pin
  held anywhere else (a profile file, a receipt) is outside this leg — the
  live-artifact pins are in `O14-repin-table.md` §2.
