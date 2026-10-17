# neg-10 — negative control + repair receipt (shard R8-O10)

- **Round:** 8 · **shard:** R8-O10 (operability) · **claim:** O · **axis:** operability
- **Date:** 2026-10-17 (all commands below; last consolidated evidence runs at
  `checked_at_utc = 2026-10-17T20:30:12Z` live / `20:30:24Z` pre-fix)
- **Baseline:** declared `e7ca0fa…`; worktree HEAD `cf338a7`. The four gates
  named by the defect are byte-identical at both revisions — verified with
  `git show cf338a7:<path> | sha256sum`, matching the review-26 §0 pins
  `fb05c644…` (phonology), `8c5afb0a…` (naming), `26d246e9…` (myth),
  `29a9361c…` (costume).
- **Role:** repair shard. Writes only the repaired gates, this directory's
  control, its evidence files, and this report. No commit.
- **Defect:** inventory entry `idx 10 = R26-D6`
  (`reports/round-8/operability/defect-inventory.json`, `source_section: "§3 D6"`),
  the review-26 §3 D6 register entry: *"uncaught RecursionError on deep flow
  nesting prints a Python traceback and exits 1 — indistinguishable from a
  findings verdict, violating the documented '2 = could-not-evaluate'
  contract."* Worker-facing index convention confirmed by sibling shards:
  `neg-09` controls the tab-indentation register entry, `neg-11` states its
  defect as "review 26 §3, index 7" — so *defect index 6* is R26-D6, the entry
  `idx 10` of the inventory.

## 0. Dependency status

`reports/round-8/operability/defect-inventory.json` did not exist when this
shard started (`ls reports/round-8/operability/` → directory absent at
`20:12Z`). Per the shard fallback, both named reviews were read directly
(`reports/supplement-opencode-1/26-parser-controls.md`,
`reports/supplement-opencode-1/29-local-boundaries.md`) and defect index 6 was
taken from the review-26 register. The inventory landed during the run
(`20:22Z`) and confirmed the selection — no change of target was needed.

## 1. Fresh reproduction (pre-fix bytes)

Command (fresh at `20:15Z`, run against the worktree, whose four gates were
still at the pinned pre-fix bytes at that moment):

```bash
python3 - <<'PY'
import subprocess, sys, tempfile, os
deep = ("name: d\nphonology:\n  consonants: [" + "["*3000 + "]"*3000
        + "\n  vowels: [a]\n  phonotactics: (C)V\n  tones: 0\n")
for g in ("phonology-sanity-gate","naming-collision-gate","myth-consistency-gate",
          "costume-era-consistency-gate","lexicon-coverage-audit"):
    with tempfile.TemporaryDirectory() as d:
        p=os.path.join(d,"p.yml"); open(p,"w").write(deep)
        r=subprocess.run([sys.executable,"tools/gates/%s.py"%g,p],
                         capture_output=True,text=True,timeout=60)
        print(g, "rc=%d"%r.returncode, (r.stderr or r.stdout).strip().splitlines()[-1:])
PY
```

Observed (pre-fix): `phonology rc=1 RecursionError`, `naming rc=1
RecursionError`, `myth rc=1 RecursionError`, `costume rc=1 RecursionError` —
all four printed a traceback and no `G-DATA` finding; exit 1 is the gates'
"findings" code, so a caller cannot distinguish the crash from a verdict.
`lexicon rc=2` on this payload.

**Payload off-by-one discovery (recorded because it masked a fifth site).**
Review 26's own repro string is `"[" + "["*3000 + "]"*3000` — 3001 opening
brackets against 3000 closing ones (unbalanced). Lexicon's flow reader
rejects the unbalanced form as `unterminated flow value` (rc=2), which is why
the review and the first pass of this shard read lexicon as conformant. With
the **balanced** 3000/3000 payload, lexicon fails identically — fresh receipt:

```
$ python3 - <<'PY'   # balanced payload against git cf338a7 and the worktree
lexicon pre-fix   rc=1 ['RecursionError: maximum recursion depth exceeded']
lexicon post-fix  rc=2 ['ERROR: …/p.yml: flow nesting deeper than the supported 64 levels']
PY
```

The traceback sites at baseline: `_parse_scalar` (phonology, review-cited
`:327`), `_parse_flow`/`_parse_value` (naming, `:324-345`), `_parse_flow`
(myth), `_flow` (costume), `_flow_value` (lexicon, `:346`).

## 2. Repair applied (five gates, two layers each)

Layer 1 — a nesting-depth cap in each gate's flow scanner/entry, raising the
gate's own parse error so the existing could-not-evaluate path returns exit 2:

| gate | edit site (post-edit worktree) | error raised |
|---|---|---|
| `tools/gates/phonology-sanity-gate.py` | `:307` `MAX_FLOW_DEPTH = 64`; check at `:313` in `_flow_parts` | `PacketError` |
| `tools/gates/naming-collision-gate.py` | `:252` constant; check at `:263` in `_split_flow` | `YamlError` |
| `tools/gates/myth-consistency-gate.py` | `:165` constant; check at `:171` in `_split_top` | `GateParseError` |
| `tools/gates/costume-era-consistency-gate.py` | `:164` constant; check at `:170` in `_split_flow` | `ValueError` (wrapped to `Malformed` by `parse_packet`) |
| `tools/gates/lexicon-coverage-audit.py` | `:389` constant; `_flow_nesting_too_deep` helper `:392`; screen at `:411` in `_parse_flow` | `PacketError` |

Layer 2 — a `RecursionError` catch at the parse/evaluate entry (defence in
depth; also covers the JSON path, where `json.loads` raises the same error):
phonology `run_text` `:1120`, naming `evaluate_text` `:1695`, myth `main`
`:863`, costume `run_text` `:1160`, lexicon `main` `:1029`. Each returns exit
2 with a `G-DATA`-class message naming the depth, never a traceback.

Semantics chosen: 64 levels is a policy cap (real packets nest ≤ 4); deeper
input is *unevaluable* (exit 2), not a crash and not a findings verdict. The
cap fires before the recursion limit, so the process never reaches a
traceback.

## 3. Isolated negative control

`neg-10-control.py` — 13 checks: per gate, deep bracket nesting, deep brace
nesting, and the gate's own committed fixture packet (regression guard: the
cap must not reject real packets); plus one untouched-reference check that
`lexicon-coverage-audit.py` rejects deep nesting with exit 2. Payloads and any
pre-fix copies live in a temp directory (`--scratch`), gates run as
subprocesses, nothing under the repository is written.

**Pass-after (live gates)** — `evidence-live.txt`, `neg-10-live.json`:

```
NEG-10 SUMMARY: 13/13 checks passed; verdict=PASS      exit=0
```

Deep-nesting cells now read `rc=2 PASS` with
`flow nesting deeper than the supported 64 levels` and no traceback; fixture
cells stay `rc=1` (evaluated normally). Gate digests at that run: phonology
`d5fe087f…`, naming `d9e4e8f4…`, myth `5368b135…`, costume `e6bffd70…`,
lexicon `2c4dd397…`.

**Fail-before (pinned pre-fix bytes)** — `evidence-prefix.txt`,
`neg-10-prefix.json`:

```
NEG-10 SUMMARY: 4/12 checks passed; verdict=PRE-FIX-PATTERN-OBSERVED    exit=1
```

All eight deep-nesting cells on the four pinned copies (`git show cf338a7:…`,
sha256 verified against the review-26 §0 pins at materialisation) observe the
pre-fix pattern: `rc=1` with `Traceback (most recent call last):` and no
`G-DATA`; the four fixture cells still pass, proving the control isolates the
defect and not the gate's ordinary behaviour.

Reproduce:

```bash
python3 reports/round-8/operability/neg-controls/neg-10/neg-10-control.py            # expect exit 0
python3 reports/round-8/operability/neg-controls/neg-10/neg-10-control.py --rev cf338a7   # expect exit 1
```

Harness compatibility: `reports/round-8/run-validation.py` runs every `.py`
under `neg-controls/` with no arguments and requires exit 0 with no traceback
on stderr. Verified `20:30Z`: `python3 …/neg-10-control.py` (cwd = repo root,
no args) → `13/13 checks passed`, `exit=0`, 0 bytes on stderr. The scratch root
is probed (`--scratch`, `TMPDIR`, `/var/tmp`, system temp, repo — each probed
with a one-byte write) because the swarm saturated the tmpfs `/tmp` during this
round; the control selects `/var/tmp` in that state instead of crashing.

## 4. Regression evidence after the repair

- Gate selftests, all seven, `--selftest`, run `20:31Z` (same results at
  `20:26Z`): `phonology rc=0`
  (29 control cases), `naming rc=0`, `myth rc=0`, `costume rc=0`,
  `lexicon rc=0` (14/14), `provenance rc=0`, `handoff rc=0`.
- `python3 tools/check-gate-battery.py --selftest` → `SELFTEST OK 10/10`,
  exit 0; `python3 tools/check-craft-exercise.py --selftest` →
  `CLI-SELFTEST OK 18/18`, exit 0 (run `20:31Z`).

## 5. Cross-cutting consequences and limits

1. **Frozen-manifest pins now mismatch for all seven gates.**
   `python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv`
   (run `20:27Z`) reports `7 could-not-evaluate … gate_digest_mismatch`
   (phonology, lexicon, myth, costume, naming, provenance ×2): the round-3
   `MANIFEST.tsv` pins `gate_sha256` per gate, and every gate file has been
   edited this round by sibling shards and by this one. This shard's edits are
   part of that set; they are not its origin (`phonology` already mismatched
   before this shard's first edit — `git status` at `20:16Z`). The orchestrator
   must re-freeze the manifest or scope the replay claim before round close.
2. **Concurrency.** Sibling shards edited all five repaired files while this
   shard worked (digests changed repeatedly between runs). Every receipt above
   pins the sha256 of the exact bytes tested at run time; the final control run
   at `20:30:12Z` is green against the then-current bytes.
3. **Scratch space.** One run aborted with `OSError: [Errno 28] No space left
   on device` while materialising pre-fix copies under the tmpfs `/tmp` (swarm
   saturation). The control now probes candidate scratch roots and falls back to
   `/var/tmp` when `/tmp` is full; both final receipts record
   `NEG-10 scratch root: /var/tmp`, and `evidence-prefix.txt` carries the note.
4. **Coverage gap left open.** The gates' own `--selftest` suites still contain
   no deep-nesting case (review 26 §3 D10 registers that coverage gap, inventory
   `idx 14`); this control covers it externally. Adding in-gate cases belongs to
   the D10 shard, not here.
5. **Cap value not tuned.** 64 was chosen as a generous policy cap; the minimum
   depth that still reproduces the crash was not bisected, and no timing
   benchmark of the capped path was taken.
6. **Inventory status not updated.** `defect-inventory.json` entry `idx 10`
   still says `status_working_tree: "present_in_working_tree"`; that file is
   R8-O03's artifact and was left untouched. The repair receipt is here.

## 6. Files written by this shard

- `tools/gates/phonology-sanity-gate.py`, `tools/gates/naming-collision-gate.py`,
  `tools/gates/myth-consistency-gate.py`,
  `tools/gates/costume-era-consistency-gate.py`,
  `tools/gates/lexicon-coverage-audit.py` (layer-1 + layer-2 edits above)
- `reports/round-8/operability/neg-controls/neg-10/neg-10-control.py`
- `reports/round-8/operability/neg-controls/neg-10/evidence-live.txt`
- `reports/round-8/operability/neg-controls/neg-10/evidence-prefix.txt`
- `reports/round-8/operability/neg-controls/neg-10/neg-10-live.json`
- `reports/round-8/operability/neg-controls/neg-10/neg-10-prefix.json`
- `reports/round-8/operability/neg-controls/neg-10/neg-10-report.md` (this file)
