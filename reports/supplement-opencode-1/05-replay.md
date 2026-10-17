# 05 — frozen replay executor (supplement-opencode-1)

**Scope of this fragment:** `tools/replay-frozen.py` and this file only. No LOG.md,
SCORECARD.md, SKILL.md, corpus, packet or frozen-artifact writes; no source claims are
made here (the freshness axis rows belong to the source-audit worker's files).
**Baseline revision:** `fe34faaafbe0add59ff68827a0df6c5782a72404`, worktree clean under
`tools/` when the work started. Sibling workers edited unrelated files
(`corpus/knowledge/civilizations/africa-primary-sources.md`, `examples/culture-d2/components/06-*`,
`07-*`, `tools/assemble-d2.py`) during the run; none of them affects this replay, which reads
only pinned snapshots and digest-pinned gate bytes.

**Deliverable.** `tools/replay-frozen.py` (stdlib only, 606 lines,
sha256 `762db76d24edbd11918088bce41e887b413d5c9cbafb9ba1f32d9e79875e5ea0`) implementing
`python3 tools/replay-frozen.py <MANIFEST.tsv> [--repo-root DIR] [--json] [--timeout SEC]`
and `--selftest` over the existing `tools/gates/frozen/round-3/MANIFEST.tsv` column schema
(`gate gate_sha256 input input_sha256 exit_code finding_count output output_sha256
input_snapshot command`).

## Contract implemented

- **Exit 0** = every row reproduced its recorded verdict — *reproduction only*. A reproduced
  `exit_code=1` (or `2`) row is still red/could-not-evaluate; the tool never reads a design
  as clean.
- **Exit 1** = replay mismatch: the pins verified and the gate ran, but observed exit code,
  finding count, or output bytes disagree with the record.
- **Exit 2** = could-not-evaluate: `gate_digest_mismatch`, `snapshot_tampered`,
  `expected_output_tampered`, `record_inconsistent`, `gate_not_whitelisted`,
  `gate_unsafe_path` / `snapshot_unsafe_path` / `output_unsafe_path` / `input_unsafe_path`
  (absolute, traversal, symlink, outside-repo), `*_missing`, `gate_missing`,
  `record_malformed`, `manifest_malformed`, `manifest_unreadable`, `gate_timeout`,
  `gate_launch_failed`, `mirror_unsafe`. Exit 2 has precedence over exit 1: an unevaluable
  row leaves the replay incomplete whatever the other rows showed.
- **Verification order:** gate whitelist + safety → `gate_sha256` → `input_snapshot`
  safety → `input_sha256` (`snapshot_tampered`) → output safety → `output_sha256`
  (`expected_output_tampered`) → record self-consistency (`finding_count` vs the number of
  `^FINDING ` lines in the recorded output) → launch. A failed pin never reaches the launch.
- **The `command` column is never executed.** It is parsed, echoed into the report/JSON as
  `recorded_command_ignored`, and nothing else. argv is constructed as
  `[sys.executable, <digest-pinned gate>, <original input path>]`, cwd = an isolated
  self-cleaning temp mirror holding a verified copy of the snapshot at the row's own `input`
  relative path. The mirror is required for byte-faithfulness: the provenance rows echo the
  path they were given, so passing the snapshot path directly changes the bytes (measured:
  rows 7–8 would differ), while the original relative path against copied snapshot bytes
  reproduces all rows exactly. `PYTHONDONTWRITEBYTECODE=1` is set so a run never drops
  `__pycache__` into the repo.
- **Gate whitelist:** a non-symlink `*.py` file directly under `<root>/tools/gates`, inside
  the realpath of `<root>`; the gate bytes must equal the row's `gate_sha256` before it is
  started. A later edit of any gate turns its rows into `could-not-evaluate
  gate_digest_mismatch` — drift is reported, never blessed.

## Evidence

### 1. Selftest — isolated fixtures, positive and negative controls

`python3 tools/replay-frozen.py --selftest` → **`selftest: 52/52 checks passed`, exit 0**
(13 isolated fixture repositories, each with its own generated gate that records every launch
into a marker file; every scenario asserts the CLI exit code, the reason id in stdout, whether
the gate was launched, and — for the 12 scenarios that run to a verdict — that the fixture
tree is byte-unchanged afterwards).

| scenario | exit | reason | gate launched |
|---|---|---|---|
| clean-green (recorded exit 0, no findings) | 0 | `reproduced` | yes |
| expected-red (recorded exit 1, 2 findings) | 0 | `reproduced` | yes |
| mismatch-bytes (record self-consistent, gate no longer prints it) | 1 | `replay_mismatch` | yes |
| mismatch-exit (recorded 0, gate exits 1) | 1 | `replay_mismatch` | yes |
| snapshot-tampered (snapshot edited after pinning) | 2 | `snapshot_tampered` | **no** |
| gate-digest-mismatch | 2 | `gate_digest_mismatch` | **no** |
| output-tampered (recorded output edited after pinning) | 2 | `expected_output_tampered` | **no** |
| record-inconsistent (`finding_count=7`, output has 1) | 2 | `record_inconsistent` | **no** |
| traversal-gate (`../tools/gates/…`) | 2 | `gate_unsafe_path` | **no** |
| symlink-gate | 2 | `gate_unsafe_path` | **no** |
| gate-not-whitelisted (`tools/fake-gate.py`) | 2 | `gate_not_whitelisted` | **no** |
| absolute-snapshot (`/nowhere/…`) | 2 | `snapshot_unsafe_path` | **no** |
| malformed manifest header | 2 | `manifest_malformed` | **no** |

The clean-green manifest's `command` column is `touch pwned-marker.txt`; the selftest asserts
that file never appears ("recorded command string never executed"), and 12 "fixture tree
unchanged" checks cover every scenario that ran the tool. The gate-drift control **was**
exercised here (`gate_digest_mismatch`) and on a replica root (below); it was deliberately not
exercised by editing the tracked gate files, which would alter historical bytes and race with
sibling workers.

### 2. Actual round-3 replay — `python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv` → exit 0

```
ROW 2 reproduced gate=tools/gates/phonology-sanity-gate.py  exit=1/1 count=3/3  bytes=match
ROW 3 reproduced gate=tools/gates/lexicon-coverage-audit.py  exit=0/0 count=0/0  bytes=match
ROW 4 reproduced gate=tools/gates/myth-consistency-gate.py   exit=1/1 count=1/1  bytes=match
ROW 5 reproduced gate=tools/gates/costume-era-...-gate.py    exit=1/1 count=10/10 bytes=match
ROW 6 reproduced gate=tools/gates/naming-collision-gate.py   exit=1/1 count=20/20 bytes=match
ROW 7 reproduced gate=tools/gates/provenance-audit.py (mesoamerica)  exit=0/0 count=0/0 bytes=match
ROW 8 reproduced gate=tools/gates/provenance-audit.py (gate-frozen-run-standard) exit=0/0 count=0/0 bytes=match
REPLAY OK: 7/7 rows reproduced the recorded verdicts
```

`--json` gives the same summary (`{"rows": 7, "reproduced": 7, "mismatch": 0,
"could_not_evaluate": 0, "exit": 0}`) plus per-row observed digests, so a reviewer can
re-derive the finding counts without trusting the manifest's own numbers.

### 3. Superseded `attempt-1` manifest also replays 7/7 (exit 0)

`python3 tools/replay-frozen.py tools/gates/frozen/round-3/attempt-1/MANIFEST.tsv` → 7/7
reproduced, including row 5 `exit=2/2 count=1/1 bytes=match` (the recorded
"expected a number, got None" could-not-evaluate run over the pre-fix packet snapshot). That
is history reproducing, **not** an endorsement: the recorded verdict of that row is itself a
could-not-evaluate.

### 4. Real-data tamper control (replica copy; repo bytes untouched)

```
tmp=$(mktemp -d); mkdir -p "$tmp/tools"; cp -r tools/gates "$tmp/tools/"
# append one comment line to the *copy* of the pinned snapshot, then replay against it
python3 tools/replay-frozen.py "$tmp/tools/gates/frozen/round-3/MANIFEST.tsv" --repo-root "$tmp"
```
Observed: **exit 2**, row 8 `could-not-evaluate reason=snapshot_tampered`, the other six rows
`reproduced` (`{"rows": 7, "reproduced": 6, "mismatch": 0, "could_not_evaluate": 1, "exit": 2}`).
The repository's own frozen bytes were never modified.

### 5. The baseline carries its own historical gate revision — no drift is blessed

`git show fe34faa:tools/gates/<gate>.py | sha256sum` equals the manifest's `gate_sha256` for
all six gates (e.g. `phonology-sanity-gate.py` → `fb05c644…`, `provenance-audit.py` →
`4aaea6e9…`), and `git diff --stat c610e0a fe34faa -- tools/gates/` lists only
`frozen/round-4/*.out` files — the six gate `.py` files are byte-identical between the round-3
commit and the baseline. So the recorded round-3 verdicts are reproduced with the baseline's
**own committed instrument**, not with drifted code. The residual gap is structural, not
drift: `tools/gates/frozen/round-3/` holds inputs, outputs and the manifest but no frozen copy
of the gate code, so gate integrity rests entirely on the `gate_sha256` pin plus this tool's
pre-launch digest check. If the parent wants a self-contained frozen revision, the option is a
frozen copy of the six `.py` files under the frozen directory plus a schema/whitelist decision
— flagged as an integrator call, not taken here.

### 6. Calibration counts (reproducible, from committed frozen bytes)

- **Record-level count reconciliation: 7/7.** Every recorded `finding_count` equals the number
  of `^FINDING ` lines in the recorded output (`replay_row` recomputes it; a mismatch aborts
  the row as `record_inconsistent`). No count in this report comes from the live packet.
- Round-3 naming classes (`awk '/^FINDING /{print $2}' tools/gates/frozen/round-3/naming-collision-gate.out | sed 's/:$//' | sort | uniq -c`):
  `CROSS-HOLD 1, DERIV-HOLD 8, PHON-CODA 1, PHON-INVENTORY 10` (20).
- Round-4 naming classes, same command on `tools/gates/frozen/round-4/naming-collision-gate.out`:
  `CROSS-HOLD 1, NAME-NEAR 6, PHON-CODA 1, PHON-INVENTORY 10` (18) — this recomputes the
  baseline's `claims.json` `naming_findings` (6+1+10+1) from a committed artifact and confirms
  the number is derivable rather than asserted.
- Live `examples/culture-d2/packet.d2.yml` hashed `d5fb4088…` during this run, matching
  `claims.json`'s `d2_packet_sha256`; the round-3 snapshots (`54be6319…`, `a916a4c2…`,
  `7b3bdc80…`) differ, which is why replay must read snapshots rather than live paths.
- **Round 4 is not replayable as a frozen run:** `tools/gates/frozen/round-4/` contains five
  `.out` files and **no `MANIFEST.tsv`**, and three of the five (`costume-era-consistency-gate`,
  `lexicon-coverage-audit`, `myth-consistency-gate`) are 0 bytes. Any round-4 finding count
  cited from that directory needs that gap named; only the naming (18) and phonology
  (`A-NEUTRAL 3`) outputs carry content.
- Usage sanity: no-args → exit 2; `--help` → exit 0; missing manifest → exit 2
  `manifest_unreadable`.
- Repo hygiene: `find tools -newermt <run-stamp> -type f` after a replay is empty; nothing was
  written under `tools/` by any run in this fragment.

## Limits, unresolved items, decisions left to the parent

1. `gate_timeout` and `gate_launch_failed` are implemented but not exercised by the selftest
   (they need a hanging/failing interpreter), so they are untested code paths.
2. stderr is not a column of the frozen schema: it is reported as an observation, never
   compared. If a future gate's verdict depends on stderr, the manifest schema needs a pin.
3. Exit-2 precedence over exit-1 is my documented choice, not something the assignment fixed.
4. The finding-count definition (`^FINDING ` lines) is this repo's convention and agreed with
   all 7 recorded counts; the tool states it in its own header. A gate that ever numbers
   findings differently would need this line changed, not silently bent.
5. The tool requires the gate to be a direct child of `tools/gates`; subdirectories are refused
   by design.
6. Registry row (parent's call — SKILL.md is not mine to write): name `replay-frozen.py`,
   kind `gate` (it can fail and has a selftest) or `probe` at the parent's discretion, entry
   `python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv`, verdict map
   `0 clean / 1 failed / 2 could-not-evaluate`, self-test `python3 tools/replay-frozen.py
   --selftest`, pinned values: the per-row `gate_sha256` / `input_sha256` / `output_sha256` in
   `tools/gates/frozen/round-3/MANIFEST.tsv`, write scope read-only over the repo plus a
   self-cleaning temp mirror, owner `kotodama-shokunin`.

This fragment is author-side evidence; it claims no SHONEN box, no rank change and no axis
score.

## Addendum — parent review fixes (2026-10-17, supplement-opencode-1)

Two bounded defects, both in `tools/replay-frozen.py`. This addendum supersedes the earlier
sections where they describe the tool's path safety; the tool digest quoted in **Deliverable** is
superseded by `a2fb5c98260a07f0801f4bf21f349283638da6796645780393262e4368c79464` (was
`762db76d…`). Nothing else in this fragment changed; the 52 pre-existing selftest checks and the
expected-red handling are intact.

### Fix 1 — traversal is refused on the raw spelling, before normalization

`repo_path()` previously ran `os.path.normpath()` and screened the *result*, so a raw token with an
internal `..` component (`tools/gates/../gates/fake-gate.py`) normalized into an accepted path and
the raw spelling was handed to the gate. The raw spelling is now split into components and refused
if any component is `..` (or if nothing remains after dropping `.`/empty segments). Verdict:
could-not-evaluate with `<field>_unsafe_path`, gate not launched.

### Fix 2 — flag-like and stdin gate arguments are refused

A row's `input` is the argv token handed to the gate, and the committed gates read their own argv:

- `tools/gates/provenance-audit.py:506-515` — `--selftest` is an argparse flag whose help text is
  "regenerate tools/gates/fixtures/provenance/ and self-check"; it calls `selftest(root)`, which
  writes inside the repo.
- `tools/gates/phonology-sanity-gate.py:1268-1269`, `tools/gates/lexicon-coverage-audit.py:974`,
  `tools/gates/myth-consistency-gate.py:827` — the same flag spelling returns their own selftests;
  the committed myth selftest output records "fixture and expected rewritten under
  tools/gates/fixtures/" (`tools/gates/frozen/round-3/selftests/myth-consistency-gate.out`).
- `tools/gates/phonology-sanity-gate.py:1276-1277` — `-` means read stdin, not a path.

A manifest could therefore have made the replay write inside the repository. `repo_path()` now
refuses any component starting with `-` (`--selftest`, `./--selftest`, `-`, `--help`) as
`<field>_unsafe_path`, before the gate is launched, for all four path fields. Recorded
relative-path stdout is unchanged: legal rows are still passed verbatim as the argv token against
the mirrored snapshot, and round-3 still reproduces 7/7 byte-exactly.

### Evidence (commands and observed results)

| command | observed |
|---|---|
| `python3 tools/replay-frozen.py --selftest` | `selftest: 79/79 checks passed`, exit 0 (was 52/52) |
| `python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv` | exit 0, `REPLAY OK: 7/7` |
| `python3 tools/replay-frozen.py tools/gates/frozen/round-3/attempt-1/MANIFEST.tsv` | exit 0, 7/7 |
| real-data replica proof (below) | exit 2, `ROW 8 … reason=input_unsafe_path … launched=no`, 0 replica files added or changed |

New selftest cases, each asserting exit 2, the reason id, gate **not launched**, and fixture tree
byte-unchanged:

| case | token under test | reason |
|---|---|---|
| `traversal-internal-gate` | `tools/gates/../gates/fake-gate.py` | `gate_unsafe_path` |
| `traversal-internal-snapshot` | `tools/gates/frozen/<case>/inputs/../inputs/<input>` | `snapshot_unsafe_path` |
| `traversal-internal-input` | `examples/../examples/fixture-input.yml` | `input_unsafe_path` |
| `flag-input-selftest` | `--selftest` | `input_unsafe_path` |
| `flag-input-dot-selftest` | `./--selftest` | `input_unsafe_path` |
| `flag-input-stdin` | `-` | `input_unsafe_path` |

The three flag cases run against a generated fixture gate that carries a stand-in for the real
`--selftest` branch: it writes a marker file and exits 0 when handed the flag. The suite asserts
that marker never appears ("gate's own selftest never triggered"), so the refusal is proven at the
point of danger instead of inferred from an exit code. The `command` column of those cases reads
`python3 tools/gates/fake-gate.py --selftest` — the exact invocation that would have been
dangerous — and it is still never executed (26 new checks total: 6 cases × 4, plus one regenerate
check for each of the three flag cases).

Both families are genuine regression tests: under the pre-fix logic the three internal-`..` tokens
normalized into legal paths (the gate case would have been accepted and launched) and the three
flag tokens were passed straight through to the gate.

### Real-data replica proof

`tmp=$(mktemp -d)`; copy `tools/gates/` into it; rewrite the **copy's** round-3 manifest so its
last row (provenance-audit over `corpus/knowledge/verification/gate-frozen-run-standard.md`) carries
`input=--selftest`; run
`python3 tools/replay-frozen.py "$tmp/tools/gates/frozen/round-3/MANIFEST.tsv" --repo-root "$tmp"`.
Observed: exit 2; `ROW 8 could-not-evaluate reason=input_unsafe_path gate=tools/gates/provenance-audit.py input=--selftest … launched=no`;
detail `input: flag-like component refused (options and stdin are not paths): '--selftest'`; the
other six rows reproduced; replica files added by the run: **0**, changed: **0**. A launched
`--selftest` would have rewritten `tools/gates/fixtures/provenance/*` in the replica; the real
repository's frozen bytes were untouched and no real gate was ever handed a flag.

### Unchanged, and new limits

- **Live-tree movement does not touch the replay.** During this addendum sibling workers changed
  `packet.d2.yml`, `SKILL.md`, `SCORECARD.md`, `corpus/README.md` and corpus entries; round-3 still
  reproduced 7/7 because the replay reads pinned snapshots and digest-pinned gate bytes.
- Pre-existing limits stand: `gate_timeout`/`gate_launch_failed` unexercised; stderr unpinned;
  exit-2 precedence over exit-1; the `^FINDING ` count definition; no round-4 `MANIFEST.tsv`.
- New limit: the flag refusal is component-based, so a legitimate file whose name begins with `-`
  could not be replayed from a manifest. No such path exists in this repo, and refusal is the
  fail-closed side of the defect.

Author-side evidence; no SHONEN box, rank, or axis score is claimed by this addendum.
