# R9-D06 — D2 interop: is the d2 path still green after round 9?

- round 9 · worker `R9-D06` · date 2026-10-17 · command window 2026-10-17T20:48:22Z → 2026-10-17T20:49:52Z
- baseline revision `a7bb205d3aecdaa24d91c047c8719cd8689e4ddd` (HEAD of the delivered tree;
  all commands below ran there unless a section says otherwise)
- interpreter `Python 3.14.7` (`python3 -c "import sys;print(sys.version.split()[0])"`,
  2026-10-17T20:48:37Z) on Linux
- status: NON-CANON test record. **No tool, packet, artifact, gate or corpus file was edited by
  this shard.** The only file written is this one. Scratch lives in `.scratch/r9d06/` and was
  deleted at seal time.

## Assignment (from `reports/round-9/targets.json`, depth `R9-D06`)

> Interop: confirm d2-typed-labels and assemble-d2 still green after round 9 (no
> cross-contamination); record.

Claim context: round-9 claim **D** (`reports/round-9/claims.json`) requires, among other legs,
that the D3 acceptance does not disturb the already-admitted D2 path. This fragment covers the
interop leg only; `--check` drift diagnosis is `R9-D01`, determinism `R9-D02`, evidence-coupling
`R9-D03`, frozen replay `R9-D04`, CLI negatives `R9-D05`.

## 1. The assigned commands — result

| # | command | exit | stdout | stderr |
|---|---|---|---|---|
| 1 | `python3 tools/d2-typed-labels.py --selftest` | **0** | last line: `selftest: 39/39 checks passed — the three shard control matrices, the loader/parser malformed cases, the live-packet typing and reconciliation cases, and the CLI emit/check/tamper controls; no file outside the temporary directory touched` | empty (0 bytes) |
| 2 | `python3 tools/assemble-d2.py --check` | **0** | `packet.d2.yml: byte-identical deterministic assembly` | empty |

Both were run twice in the window:

- 20:48:22Z in the live worktree (first pass) — exits 0/0.
- 20:49:36Z in the live worktree again, *after* round-9 peer artifacts had appeared on disk
  (`tools/gates/expected/costume-era-consistency-gate/`, `tools/gates/frozen/handoff-packet-check/`,
  `tools/gates/frozen/lexicon-coverage-audit/`, `reports/round-9/{baselines,d3,freshness}/`) —
  exits 0/0, same bytes.

Stdout digests (the strongest available comparison, because round 8 recorded its own):

| command | stdout sha256 | matches round-8 admitted value? |
|---|---|---|
| `d2-typed-labels.py --selftest` | `7231139c5b06089866270f4869caa1ffe04a4011502014979c996c9b1ab83252` | **yes** — identical to `reports/round-8/validation.json` (`claims.D.measurement.selftest.stdout_sha256`) |
| `assemble-d2.py --check` | `2fa0c8c197459f549de2f0822b8895477e27dcce38def75e18346ba6d672e386` | **yes** — identical to `reports/round-8/validation.json` (`claims.D.measurement.regeneration.stdout_sha256`) |

So the d2 path is not merely "still exit 0": it is **byte-identical in output** to the state the
round-8 admission recorded, on the same inputs.

## 2. Input pins (and why "no cross-contamination" is checkable)

| file | sha256 at HEAD / seal (20:49:52Z) | round-8 value | same? |
|---|---|---|---|
| `tools/d2-typed-labels.py` | `0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802` | `0da0015f…` (`reports/round-8/validation.json`) | yes |
| `tools/assemble-d2.py` | `8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d` | — | (tool unchanged; not re-listed in round 8) |
| `examples/culture-d2/packet.d2.yml` | `e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643` | `e0f21509…` (round-8 admission regeneration, `claims.D.measurement.regeneration.reader_pin` block) | yes |
| `examples/culture-d2/typed-labels.d2.yml` | `e70ba1477dbeb830061db6fd12516b7d902587bddae173f55a3650015d380b2f` | `e70ba147…` (`reports/round-8/depth/test-determinism.md` seal, 17:33:21) | yes |
| `tools/gates/costume-era-consistency-gate.py` | `e6bffd7020c0b1168828902853320bbf37e903457c83dae5477820aeceec478f` | `e6bffd70…` (same, and packet `reader_sha256` pin) | yes |

The packet pins its own reader at `examples/culture-d2/packet.d2.yml:3322`
(`reader_sha256: "e6bffd7020c0b1168828902853320bbf37e903457c83dae5477820aeceec478f"`), and the
live gate digest equals that pin — so the gate/reader half of the d2 contract is internally
consistent at this revision.

**Read-set.** The d2 path reads exactly two files. Grep evidence
(`grep -n "PACKET\|READER" tools/d2-typed-labels.py`, 2026-10-17):

- `tools/d2-typed-labels.py:2213` — `PACKET_DEFAULT = ROOT / "examples/culture-d2/packet.d2.yml"`
- `tools/d2-typed-labels.py:2215` — `READER = ROOT / "tools/gates/costume-era-consistency-gate.py"`

`tools/assemble-d2.py` reads the same packet through that gate's reader
(`assemble-d2.py:23` `ROOT = Path(__file__).resolve().parent.parent`; `:31`, `:50` hashing/reading).
No round-9 artifact is in that read-set, which is why the concurrent peer writes listed in §1
cannot have influenced the result.

### 2.1 Round-9 commit delta

- `git log --name-only --pretty=format:'%h %s' e1694ba..HEAD` (2026-10-17T20:48:37Z) →
  one commit, `a7bb205 round-9: declare claims F/O/D (escalated residuals, gate baselines, D3 acceptance)`,
  touching only `reports/round-9/claims.json` and `reports/round-9/targets.json`.
- `git merge-base --is-ancestor e1694ba HEAD` → true: the declared baseline revision is an
  ancestor of HEAD, so `e1694ba..HEAD` is exactly round 9's committed delta.
- `git status --short -- tools examples corpus` at 20:48:37Z and at 20:49:31Z → **no tracked file
  under `tools/`, `examples/` or `corpus/` modified in the worktree** by any round-9 worker.
  (At the 20:49:52Z seal, three `corpus/knowledge/civilizations/*.md` files had become modified by
  the metadata re-audit shard — `bali.md`, `byzantium.md`, `carthage.md` — none of which is in the
  d2 read-set; the d2 pins above were re-taken after that and are unchanged.)

## 3. Isolation leg — results reproduced off the live tree

To separate "the live tree happens to be clean" from "the result is a property of the committed
revision", HEAD was exported with `git archive HEAD | tar -x -C <scratch>` (a tree containing no
untracked file at all) and both commands were re-run there (20:48:5xZ):

| command | isolated exit | isolated stdout sha256 |
|---|---|---|
| `python3 tools/d2-typed-labels.py --selftest` | 0 | `7231139c5b06089866270f4869caa1ffe04a4011502014979c996c9b1ab83252` |
| `python3 tools/assemble-d2.py --check` | 0 | `2fa0c8c197459f549de2f0822b8895477e27dcce38def75e18346ba6d672e386` |

All five §2 digests were re-hashed inside the isolated tree and came out identical. Same result
again at the round-8 admission revision `e1694ba` (§4.2). Conclusion for the assigned leg:
**the green result is a property of the committed revision, not of the live worktree state.**

Additional isolation evidence, same window:

- `python3 tools/assemble-d2.py --help` → exit 0; its own usage text states it may be run from any
  directory (`Run from any directory: python3 tools/assemble-d2.py ...`), and an absolute-path
  invocation from a foreign `cwd` returned exit 0 / `packet.d2.yml: byte-identical deterministic
  assembly`.
- Non-mutation: `examples/culture-d2/packet.d2.yml` and `typed-labels.d2.yml` digests were
  identical before and after the `--selftest`, `--check` and `--emit` runs in the isolated tree.
- `--selftest` writes only inside its own temporary directory (the selftest's own final line
  asserts this; independently, no tracked file changed in either tree).

## 4. Finding: one adjacent d2 command is RED — pre-existing, not round-9 damage

`python3 tools/d2-typed-labels.py --check` exits **1**, not 0. It was not one of the two commands
my assignment names, but it is on the same path, so it is recorded here rather than omitted.

### 4.1 What exactly differs

`python3 tools/d2-typed-labels.py --check` (20:48:5xZ, live and isolated trees alike):

```
examples/culture-d2/typed-labels.d2.yml differs from the deterministic projection
TOOL_CHECK_EXIT=1
```

A fresh projection emitted beside the artifact (`--emit` into scratch) differs from the on-disk
artifact by **exactly one line**, out of 81,469 bytes:

```
$ diff <emit> examples/culture-d2/typed-labels.d2.yml
9c9
<     "packet_sha256": "e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643",   # fresh projection
---
>     "packet_sha256": "8da90b0788f86fd19babc67958715c8c16cb90a98e13572380b1c1892622b81e",   # on-disk artifact
```

- on-disk artifact `e70ba147…` embeds the **pre-repair** packet digest `8da90b07…`;
- the live packet is `e0f21509…`;
- i.e. `examples/culture-d2/typed-labels.d2.yml:9` is a stale pin, and nothing else in the
  artifact is stale. The `reader_sha256` two lines below it (`e6bffd70…`) is current.

### 4.2 It is inherited from round 8, not caused by round 9

Round 8's own admission revision reproduces the identical three-command profile. `git archive
e1694ba` into scratch, run there (20:49:0xZ):

| command | at `e1694ba` (round-8 admission) | at HEAD `a7bb205` (round 9) |
|---|---|---|
| `d2-typed-labels.py --selftest` | exit 0 | exit 0 |
| `assemble-d2.py --check` | exit 0, `byte-identical deterministic assembly` | exit 0, same |
| `d2-typed-labels.py --check` | **exit 1, differs** | **exit 1, differs** |

All four d2 input digests are identical at `e1694ba` and at HEAD (§2), so round 9 changed nothing
on this path — the red predates the round.

Mechanism, from the file history and round 8's own record:

- `git log --oneline -- examples/culture-d2/packet.d2.yml` → last touched by
  `e1694ba 2026-10-17 17:44:17 -0300 round-8: admit F/O/D — freshness receipts, harness+gate
  repairs, d2-typed-labels`.
- `git log --oneline -- examples/culture-d2/typed-labels.d2.yml` → also last touched by that same
  commit — and the artifact committed there still carries `packet_sha256: 8da90b07…`
  (`git show e1694ba:examples/culture-d2/typed-labels.d2.yml | sed -n '8,10p'`, and the same lines
  at `HEAD`).
- `reports/round-8/depth/test-determinism.md` §3.5 (17:31) recorded `--check` exit 0 against an
  artifact and packet that were then both `8da90b07…`-consistent; §4 of that record documents the
  concurrent packet/gate repair that followed. So the artifact legitimately matched its packet
  when written, and the packet repair at 17:44:17 did not re-emit the projection.

Round 8's admitted evidence covered exactly the two commands in §1 (`validation.json` lists
`selftest` and `regeneration` = `assemble-d2 --check`); the tool's own `--check` was not part of the
round-8 acceptance, which is why this red could pass admission unnoticed.

### 4.3 The one-command repair — validated in scratch only, NOT applied

Verified in the throwaway export, never on the delivered tree:

```
python3 tools/d2-typed-labels.py --emit examples/culture-d2/typed-labels.d2.yml   # exit 1
python3 tools/d2-typed-labels.py --check                                          # exit 0
python3 tools/assemble-d2.py --check                                              # exit 0
```

- After the emit, the artifact becomes `a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43`
  and both d2 checks are green; the packet itself is unchanged (`e0f21509…` before and after),
  confirming the tool never rewrites the packet.
- **Exit-code caveat for whoever automates this:** `--emit` exits **1** even on success, because
  findings are present. `python3 tools/d2-typed-labels.py --json` (exit 1) reports
  `ok: false`, `exit_code: 1`, `packet: examples/culture-d2/packet.d2.yml`, `stats: {"fail": 0,
  "hold": 15, "note": 1, "labels": 58}`, 16 findings, first
  `{"code": "D2L-FORM-UNRESOLVED", "severity": "hold", "where": "GAR-01", "detail": "label_id
  LEX-GAR-01 has no supplied native/borrowed form"}`. So exit 1 here means "findings present",
  not "the command failed".
- Decision left to the orchestrator: this shard's assignment authorises writing only this record,
  so the repair was not applied to `examples/culture-d2/typed-labels.d2.yml`. Applying it changes
  one tracked artifact by one line (a digest pin), which is a bookkeeping change, not a domain
  change — but it is a change to an admitted artifact and belongs to the round's integrator.

## 5. Boundary notes (not adjudicated here)

- The frozen round-3 d2 input `tools/gates/frozen/round-3/inputs/examples/culture-d2/packet.d2.yml`
  is `54be6319e4907d20c8239555e3f79fcb9bb6b36d102a30a6beabf34b146459f4`, deliberately different from
  the live packet; `reports/supplement-opencode-1/07-historical-corrections.md:76` documents it as
  the round-3 v1 snapshot while the live packet is v1.1. Five of the eight round-3
  `MANIFEST.tsv` rows consume it. Whether the frozen replay still reproduces is `R9-D04`'s leg.
- `tools/gates/frozen/lexicon-coverage-audit/` and `tools/gates/frozen/handoff-packet-check/`
  appeared in the tree during this window (untracked, round-9 peers). Neither is in the d2
  read-set (§2), so neither affects the receipts above.
- Round-8 failure mode worth carrying forward: if a future edit touches
  `tools/gates/costume-era-consistency-gate.py` without re-emitting the packet, `assemble-d2.py
  --check` turns red by the same stale-pin mechanism (round-8 `test-determinism.md` §4 observed
  exactly that at 17:24). At this seal the gate is still `e6bffd70…`, equal to the packet's pin.
- `/tmp` (tmpfs, 16G) returned `No space left on device` for `mktemp -d` twice at 20:48:5xZ under
  the 64-worker wave — the same pressure round 8 recorded. The attempt failed before any command
  ran; scratch was re-homed to `.scratch/r9d06/` inside the repo (real disk) and deleted at seal.
  No receipt in this record depends on a `/tmp` write.

## 6. Verdict

- **Assigned leg: GREEN.** At HEAD `a7bb205`, `python3 tools/d2-typed-labels.py --selftest` exits 0
  with 39/39 checks and `python3 tools/assemble-d2.py --check` exits 0 with
  `packet.d2.yml: byte-identical deterministic assembly`; both stdout streams are byte-identical to
  the digests round 8 admitted, all five input digests are unchanged from round-8 values, and both
  results re-produce in a `git archive HEAD` export that contains no round-9 file.
- **No cross-contamination observed.** Round 9's committed delta is two report files; the d2
  read-set is exactly two committed files, both pinned and unchanged; the worktree carried no
  modification under `tools/`, `examples/` or `corpus/` at probe time.
- **One red recorded, attributed outside round 9.** `d2-typed-labels.py --check` exits 1 because
  `examples/culture-d2/typed-labels.d2.yml:9` still pins the pre-repair packet digest `8da90b07…`;
  the identical red exists at round-8's admission commit `e1694ba`. Repair command and its
  exit-code caveat are in §4.3; it was not applied here.
- Scope of this record: the two assigned commands, their output digests, their input pins, and the
  cross-contamination check, on this host and interpreter at the revision named above. It is not a
  claim about the D3 capability (other shards), nor about cross-host reproducibility.

Everything above ran on the delivered tree or on throwaway exports of it; no count appears without
its command, no negative claim without its scan, and no quote without its location.

Seal 2026-10-17T20:49:52Z — HEAD `a7bb205d3aecdaa24d91c047c8719cd8689e4ddd`;
`tools/d2-typed-labels.py` `0da0015f…`, `tools/assemble-d2.py` `8ea6bdde…`,
`examples/culture-d2/packet.d2.yml` `e0f21509…`, `examples/culture-d2/typed-labels.d2.yml`
`e70ba147…`, `tools/gates/costume-era-consistency-gate.py` `e6bffd70…`; scratch `.scratch/r9d06/`
removed.
