# R10-O03 — findings fixer: tracker rows idx 1 (S3) and idx 9 (S11)

- shard: R10-O03 (claim O fixer; round 10, loop 1 of 3, build round 3 of 4) — 2026-10-17, local UTC-03, measurement clock `2026-10-17T21:30Z` unless a row names its own.
- assignment (verbatim): "FINDINGS R10-O03 (fixer): tracker indices 1 and 9. reports/round-10/fix-03.md."
- index resolution: `reports/round-10/findings-tracker.json` (O01) is **0-based** (`idx` 0..23, severity-first ordering). "Indices 1 and 9" = the 2nd and 10th rows — the target's fallback pairing for fixer i=2 ("the i-th and i+8-th findings"). Both rows are from `reports/round-8/depth/findings.md`:
  - **idx 1 = R8-D16 S3** (blocking, cross-shard): D2 regeneration + round-3 replay red after post-pin gate repairs.
  - **idx 9 = R8-D16 S11** (low): the harness cannot enforce "capability row enters SCORECARD only on a demonstrated run".
- writes: this file only, plus the two tracker rows (updated under `flock`, §4). **No filed byte was edited by this shard** — `reports/round-8/run-validation.py` sha256 `d78da29f…4735` before and after (its pure functions were imported read-only, §2); note a **peer** round-10 fixer modified that same file at 18:32:28 (replay-pin repair, §1.3 last bullet), which is the digest measured here and which does not touch the `measure_d_docs` path S11 controls. All scratch lives in-lane under `.scratch/r10o03/`; `tools/replay-frozen.py` refuses a mirror inside the repo (`mirror_unsafe`: "temporary root is inside the repo"), so replay runs used `TMPDIR=/var/tmp` (round-9 precedent, `reports/round-9/d3/findings.md` §5), nothing persisted there.
- baseline revision at measurement: `e3a1ec9435787328ac9f828f96cb6390e4916b8f` (HEAD, round-10 availability attempt 3). The worktree carried concurrent round-10 workers' edits throughout (e.g. the peer harness repair at 18:32:28; `git status` showed `M SKILL.md`, `M corpus/README.md`, `M reports/round-8/run-validation.py`, `M reports/round-9/validation.json` from other shards) — none written by this shard.

## 1. idx 1 — R8-D16 S3 (blocking): D2 regeneration and round-3 replay are red because gates were repaired after their digests were pinned

### 1.1 Finding (tracker row, verbatim)

> S3 [locator §S3, lines 47-62] (blocking, cross-shard) — D2 regeneration and round-3 replay are red because gates were repaired after their digests were pinned: assemble-d2.py --check exit 1 (packet pins reader_sha256 29a9361c..., live e6bffd70...); replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv exit 2 (ROW 2 could-not-evaluate reason=gate_digest_mismatch gate=phonology-sanity-gate.py). Pins are doing their job; needs re-baseline of the packet + a new frozen manifest (integration decision - reported, not absorbed).

### 1.2 Part 1 — the regeneration: FIXED (measured today)

```sh
$ python3 tools/assemble-d2.py --check; echo $?
packet.d2.yml: byte-identical deterministic assembly
0
# stdout sha256 2fa0c8c197459f549de2f0822b8895477e27dcce38def75e18346ba6d672e386
```

- packet reader pin == live reader: `examples/culture-d2/packet.d2.yml:3322` carries `reader_sha256: "e6bffd7020c0b1168828902853320bbf37e903457c83dae5477820aeceec478f"` and `sha256sum tools/gates/costume-era-consistency-gate.py` → `e6bffd7020c0…478f`. Exact equality, no drift.
- the re-baseline was a round-8 integration act, recorded: `SCORECARD.md:105-107` "Owner action during integration: D2 packet regenerated to re-pin the reader sha after the legitimate costume-gate repair — drift was caused by in-round O repairs, not by the D tool."
- S3's first symptom (`--check` exit 1) no longer reproduces. Control: the command above.

### 1.3 Part 2 — the round-3 replay: still red, by design (measured today)

```sh
$ TMPDIR=/var/tmp python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv --json
exit=2  summary {"rows":7,"reproduced":0,"mismatch":0,"could_not_evaluate":7,"exit":2}
# every row: status could-not-evaluate, reason gate_digest_mismatch (7/7; all six gate files)
# stdout sha256 cbde6c5e17c7f77e…
```

Same result in an isolated tree whose gate bytes are restored from `HEAD` (`.scratch/r10o03/iso/`, `git show HEAD:tools/gates/<gate>`): exit 2, 7/7 `gate_digest_mismatch`. The round-3 manifest pins the **round-7** gate revisions; the round-8 repairs (committed at `e1694ba`) are legitimately different bytes, and the pins refuse edited bytes by design:

- `corpus/knowledge/verification/gate-frozen-run-standard.md:100` — a stale/edited revision is "barred from any conformance claim, and never silently re-pinned" (KTD-FR-S-0002); §6 class map: `gate_revised` → exit 2.
- round-8's own acceptance recorded exactly this state and accepted the then-reproducible isolated path: `reports/round-8/validation.json` claims.D.measurement.replay_frozen = `{"accepted": "isolated-pinned-revisions", "live_reference": {"exit": 2, ...}, "isolated": {"exit": 0, "summary": {"rows": 7, "reproduced": 7, "could_not_evaluate": 0}}}` — i.e. at round-8 admit the isolated tree still restored the *pinned* gate bytes; today `HEAD` gates are the repaired ones (round-9 registry: `git diff --stat e1694ba..HEAD -- tools/gates examples tools` → empty), so neither path reproduced at this shard's first measurement. That is S3's still-live half.
- **peer parallel repair, independently re-measured by me:** at 18:32:28 a round-10 fixer repaired the round-8 harness's `replay_isolated` (new `gate_blob_for_pin`, resolving each manifest pin against the git revisions that touched the gate path). I re-ran the repaired function read-only (`TMPDIR=/var/tmp`, import; 2026-10-17) → `exit 0`, `summary {"rows": 7, "reproduced": 7, "mismatch": 0, "could_not_evaluate": 0}`, `gates_restored_from_pin: 6/7`, resolved revision `291c7141…`. So the round-3 replay reproduces again through that path; §1.4's fresh-manifest control remains the other remedy S3 literally names and does not depend on the repaired file.
- no D2-packet manifest exists anywhere in the repo (the "new frozen manifest" S3 asks for):

```sh
$ find . -name 'MANIFEST*.tsv' -not -path './.git/*' -not -path '*/.scratch/*' | sort
./tools/gates/frozen/round-3/MANIFEST.tsv
./tools/gates/frozen/round-3/attempt-1/MANIFEST.tsv
./reports/supplement-opencode-1/scratch/29-local-boundaries/{baseline,exp-asm,exp-selftest}/tools/gates/frozen/round-3[/attempt-1]/MANIFEST.tsv   # 4 supplement scratch copies
# stdout sha256 42a7b57dd7fc8ec1…
```

### 1.4 Control — the remedy S3 names, demonstrated (fresh manifest pinned to current revisions)

A D2-packet manifest pinned to the **current** gate revisions replays clean:

```sh
$ TMPDIR=/var/tmp python3 tools/replay-frozen.py .scratch/r10o03/frozen-d2/MANIFEST.tsv --json
exit=0  summary {"rows":5,"reproduced":5,"mismatch":0,"could_not_evaluate":0,"exit":0}
# two runs byte-identical stdout (sha256 ce78801e13353e72c824546066837750940e63af7f5a7c5cbd7d5f2c3dfc4a93)
```

- manifest: `.scratch/r10o03/frozen-d2/MANIFEST.tsv`, sha256 `9adb38aea4fde88f9903ede521da7be56fcc27b08aee709e462c177e4e402df4`.
- rows (live gates on the live packet, `examples/culture-d2/packet.d2.yml` sha256 `e0f21509…b643`): phonology-sanity exit 1 / 3 findings; lexicon-coverage-audit 0/0; myth-consistency 0/0; costume-era-consistency 0/0; naming-collision 1/17. All five `reproduced`; the recorded `exit_code`/`finding_count`/`output_sha256` were re-verified by `replay-frozen` before each gate ran.
- builder (reproducible; run from the lane root, `TMPDIR` for scratch):

```sh
export TMPDIR=$PWD/.scratch
mkdir -p .scratch/r10o03/frozen-d2/inputs/examples/culture-d2
cp examples/culture-d2/packet.d2.yml .scratch/r10o03/frozen-d2/inputs/examples/culture-d2/packet.d2.yml
python3 - <<'PY'   # writes MANIFEST.tsv rows for the five packet gates
import hashlib, subprocess, pathlib
outdir = pathlib.Path('.scratch/r10o03/frozen-d2'); snap = outdir/'inputs/examples/culture-d2/packet.d2.yml'
cols = ["gate","gate_sha256","input","input_sha256","exit_code","finding_count","output","output_sha256","input_snapshot","command"]
rows = []
for gate in ["phonology-sanity-gate.py","lexicon-coverage-audit.py","myth-consistency-gate.py","costume-era-consistency-gate.py","naming-collision-gate.py"]:
    gp = f"tools/gates/{gate}"
    p = subprocess.run(["python3", gp, "examples/culture-d2/packet.d2.yml"], capture_output=True)
    op = outdir/gate.replace('.py','.out'); op.write_bytes(p.stdout)
    rows.append({"gate":gp,"gate_sha256":hashlib.sha256(pathlib.Path(gp).read_bytes()).hexdigest(),
      "input":"examples/culture-d2/packet.d2.yml","input_sha256":hashlib.sha256(snap.read_bytes()).hexdigest(),
      "exit_code":p.returncode,"finding_count":sum(1 for l in p.stdout.decode().splitlines() if l.startswith("FINDING ")),
      "output":str(op),"output_sha256":hashlib.sha256(p.stdout).hexdigest(),"input_snapshot":str(snap),
      "command":f"python3 {gp} examples/culture-d2/packet.d2.yml"})
with open(outdir/'MANIFEST.tsv','w') as fh:
    fh.write("\t".join(cols)+"\n")
    for r in rows: fh.write("\t".join(str(r[c]) for c in cols)+"\n")
PY
TMPDIR=/var/tmp python3 tools/replay-frozen.py .scratch/r10o03/frozen-d2/MANIFEST.tsv --json   # exit 0, 5/5
```

### 1.5 Disposition — `fixed-with-control` (residual named)

- part 1 (regeneration red): **fixed** — `assemble-d2.py --check` exit 0, reader pin equal to the live reader (§1.2); the fix landed in round 8 and is re-verified here.
- part 2 (round-3 replay red): **not a defect to repair in place** — the pins doing their job is the standard's required behavior (`gate-frozen-run-standard.md:100`); the remedy the finding names ("a new frozen manifest") is **demonstrated** (§1.4).
- residual (named, not hidden): the demonstrated manifest is scratch-only. Landing it at `tools/gates/frozen/round-10/MANIFEST.tsv` (or `examples/culture-d2/`) is an orchestrator bookkeeping act outside this fixer's write scope; the exact recipe is §1.4 and the pins are in the manifest itself. Until landed, the D2 packet has no committed frozen manifest — which is also the substance of tracker **idx 0 (S2)**; this control is handed to that row's owner.

## 2. idx 9 — R8-D16 S11 (low): the harness cannot enforce "capability row enters SCORECARD only on demonstrated run"

### 2.1 Finding (tracker row, verbatim)

> S11 [locator §S11, lines 81-83] (low) — the harness cannot enforce "capability row enters SCORECARD only on demonstrated run": run-validation.py uses the whole-file regex re.search(r"d2[-_ ]typed[-_ ]labels") and SCORECARD.md:117 already contains that string inside the Planned section, so the check passes without any demonstrated-run row. Anchor the check to a specific table/section.

### 2.2 Fail-before — reproduced today (filed harness imported read-only)

`reports/round-8/run-validation.py:1357` still decides the row with the whole-file regex (`row = re.search(r"d2[-_ ]typed[-_ ]labels", scorecard, re.I)`; it sat at `:1323` before a peer's 18:32:28 repair inserted ~34 lines above it — same `d78da29f…4735` bytes throughout this shard's measurements); the `measure_d_docs` path was not touched by this shard and not by the peer repair (the peer's `gate_blob_for_pin` repair touched only `replay_isolated`). Probe `.scratch/r10o03/s11/probe2.py` imports the module, points `ROOT` at a synthetic tree whose SCORECARD carries the string only inside a prose "Planned" paragraph (no capabilities table at all), and calls the harness's own `measure_d_docs()`:

```text
FILED CHECK on mention-only SCORECARD: scorecard_row = True | failures = []
```

The harness reports the docs check as satisfied on a mention-only SCORECARD — S11's mechanism reproduces exactly. On the real `SCORECARD.md` it also returns `True`; today that pass happens to be true (the row exists at `:128`), but it is true for the wrong reason — any prose mention would satisfy it.

### 2.3 Delivered correction — anchored matcher (drop-in) with both controls

The matcher scans **only "Capabilities addendum" tables**, requires the capability in the *name* cell and a runnable command in the *command/evidence* cell:

```python
import re

def anchored_capability_rows(scorecard_text, name="d2-typed-labels"):
    """Rows of any 'Capabilities addendum' table whose name cell is the
    capability and whose command/evidence cell names a runnable command."""
    def norm(cell):
        return re.sub(r"[-_ ]+", "-", cell.strip().strip("`").strip().lower())
    run_token = re.compile(r"python3|--selftest|\.py\b")
    rows, in_cap, seen_header = [], False, False
    for n, line in enumerate(scorecard_text.splitlines(), 1):
        stripped = line.strip()
        if re.search(r"capabilities addendum", stripped, re.I) and not stripped.startswith("|"):
            in_cap = True; seen_header = False; continue
        if re.match(r"^#{1,6}\s", stripped):          # any heading ends the section
            in_cap = False; continue
        if not in_cap or not stripped.startswith("|"):
            continue
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        if not seen_header:
            seen_header = True; continue               # header row
        if all(set(c) <= set("-: ") for c in cells if c):
            continue                                   # separator row
        if len(cells) < 4:
            continue
        if norm(cells[0]) == name and any(run_token.search(c) for c in cells[2:4]):
            rows.append({"line": n, "name": cells[0], "command_evidence": cells[2]})
    return rows
```

Controls (same probe; receipt `.scratch/r10o03/s11/receipt2.json`):

```text
ANCHORED MATCHER on mention-only   : rows = 0 -> FAIL (no demonstrated-run row)
ANCHORED MATCHER on real SCORECARD : [{"line": 128, "name": "d2-typed-labels",
  "command_evidence": "`python3 tools/d2-typed-labels.py --selftest`; `examples/culture-d2/typed-labels.d2.yml`"}]
```

i.e. fail-before (filed regex passes a mention-only SCORECARD) / fail-after and pass-after (anchored matcher rejects the mention-only file, accepts the real demonstrated-run row at `SCORECARD.md:128`, in the round-8 capabilities addendum). The round-9 addendum (`SCORECARD.md:154`) carries `culture-d3-acceptance` with its own run command; the matcher handles both because it scans every addendum section.

### 2.4 Disposition — `fixed-with-control` (residual named)

- the defect is demonstrated (fail-before) and the correction is delivered with both controls (§2.3).
- residual (named): the filed `reports/round-8/run-validation.py` bytes stay untouched — the lane rule is that filed report bytes are never rewritten, corrections are new entries (this file is that entry). Adoption belongs to new code: `reports/round-10/run-validation.py` (X03) or any successor harness can lift the function verbatim; the acceptance's O check should treat the anchored matcher's zero-row verdict as the failure ("capability row missing or not demonstrated").

## 3. Tracker rows written (under flock; O14: reconcile if a race lost one)

`reports/round-10/findings-tracker.json` before this shard: sha256 `3bfd40181ca98c830ef1042b23c3e446328b915ced9773dbc12b431d6b22d353`. Rows updated in place with `fcntl.flock` + atomic replace; every other row left byte-identical (verified by comparing the parsed other-rows against the pre-edit snapshot). Values written:

- **idx 1** → `disposition: "fixed-with-control"`, `disposition_by: "R10-O03"`, `disposition_at_utc: "2026-10-17T21:36Z"`, `evidence: "reports/round-10/fix-03.md"`, `control: {"regeneration": "python3 tools/assemble-d2.py --check -> exit 0, byte-identical; packet reader pin == live reader e6bffd70…", "replay_remedy": "TMPDIR=/var/tmp python3 tools/replay-frozen.py .scratch/r10o03/frozen-d2/MANIFEST.tsv --json -> exit 0, 5/5 reproduced, 0 mismatch, 0 could-not-evaluate", "round3_replay": "TMPDIR=/var/tmp python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv --json -> exit 2, 7/7 gate_digest_mismatch (by design, gate-frozen-run-standard.md:100)"}`, `residual: "demonstrated D2 manifest is scratch-only; landing under tools/gates/frozen/round-10/ is an orchestrator act (recipe fix-03.md §1.4); also supplies tracker idx 0 (S2)"`.
- **idx 9** → `disposition: "fixed-with-control"`, `disposition_by: "R10-O03"`, `disposition_at_utc: "2026-10-17T21:36Z"`, `evidence: "reports/round-10/fix-03.md"`, `control: {"fail_before": "harness measure_d_docs() on mention-only SCORECARD -> scorecard_row True, failures []", "fail_after": "anchored_capability_rows(mention-only) -> 0 rows", "pass_after": "anchored_capability_rows(real SCORECARD) -> row at line 128 with `--selftest`", "receipt": ".scratch/r10o03/s11/receipt2.json"}`, `residual: "filed round-8 harness bytes untouched by the no-rewrite rule; drop-in function for the round-10 runner in fix-03.md §2.3"`.

Verification against the round's own acceptance (read-only import, `TMPDIR=.scratch`, 2026-10-17): `reports/round-10/run-validation.py` `measure_o()` → `measurement.tracker` = `{"present": true, "rows": 24, "pending_rows": [0,2,3,4,5,6,7,8,10,…,23], "unrecognized_labels": [], "fixed_without_control": [], "documented_without_reason": []}`. Rows 1 and 9 are absent from `pending_rows` and clear the fixed-with-control evidence rule (the `evidence` path resolves and the `control` strings carry commands/exits). The runner's remaining O failures at that moment (22 other pending rows, four verifier verdict files, the findings scribe) are outside this shard's two rows.

## 4. Limits and to-verify

- The fresh D2 manifest pins the gate revisions of 2026-10-17 (digests embedded in the manifest). Any later gate edit invalidates it exactly as the round-3 pins were invalidated — that is the standard's design, not a defect of this control.
- `reports/round-8/run-validation.py` was **not** run end-to-end: it writes `reports/round-8/validation.json` (filed bytes). Only its pure functions were imported and called; the harness's own verdicts quoted here are from its filed `validation.json`, not re-produced.
- S3 part 2's "by design" reading rests on the standard's text (`gate-frozen-run-standard.md:100`, §6 class map) plus round-8's recorded acceptance; whether to land a round-10 D2 manifest is an orchestrator decision, not this shard's.
- Not dispositioned by this shard (other rows): idx 0 (S2) and idx 8 (F-D17-1) — both were dispositioned by their own owners during the wave (row 0: `wont-fix`; row 8: `fixed-with-control`); §1.4's control stays reusable for row 0.
- Out of province: canon, real-world rights, game mechanics, general research method — untouched.
- `to-verify` (not verifiable from this seat): whether X03's round-10 runner adopts the anchored matcher; whether the orchestrator lands the demonstrated manifest.

## 5. Receipts (all commands 2026-10-17, lane root unless noted)

```sh
python3 tools/assemble-d2.py --check; echo $?                              # exit 0 (2fa0c8c1…)
sha256sum tools/gates/costume-era-consistency-gate.py                      # e6bffd70… == packet.d2.yml:3322 pin
find . -name 'MANIFEST*.tsv' -not -path './.git/*' -not -path '*/.scratch/*'
TMPDIR=/var/tmp python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv --json   # exit 2, 7/7 gate_digest_mismatch
TMPDIR=/var/tmp python3 tools/replay-frozen.py .scratch/r10o03/frozen-d2/MANIFEST.tsv --json    # exit 0, 5/5 reproduced
python3 .scratch/r10o03/s11/probe2.py                                      # fail-before + anchored controls
sha256sum reports/round-8/run-validation.py SCORECARD.md                   # d78da29f… / cc032db8…
# isolated HEAD-restored round-3 replay: .scratch/r10o03/iso/ (exit 2, 7/7 gate_digest_mismatch)
# evidence bundle: .scratch/r10o03/evidence.json ; S11 receipt: .scratch/r10o03/s11/receipt2.json
```
