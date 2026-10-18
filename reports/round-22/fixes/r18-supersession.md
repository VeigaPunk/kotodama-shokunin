# R22-O11 — explicit supersession of the original R18 D4 replay row

- Axis: O / operability; disposition date: 2026-10-18.
- Status: **resolved-by-documentation with a new named successor row and positive/negative replay controls**. The historical manifest remains unchanged and its current mismatch is preserved.
- Routed item: `R18-ORIGINAL-FROZEN-REPLAY` in `reports/round-21/defects/routed.md:106-110`; precursor `reports/round-21/defects/fix-16.md` and R20 `F-O15-1`.
- New record owner: R22-O11. This seat writes this note, not the frozen tree or shared integration records. All replay/recording effects are confined to fresh clones and sibling mirrors under the lane's `.scratch`.

## Named supersession row — additive, not an in-place re-pin

**R22-O11-SUPERSESSION-1** supersedes the original R18 projection row **for the committed post-R20 projection revision below**. It does not supersede the original assembly row or alter any archived acceptance verdict.

```json
{
  "id": "R22-O11-SUPERSESSION-1",
  "date": "2026-10-18",
  "status": "superseded-historical-projection",
  "supersedes": {
    "manifest": "tools/gates/frozen/round-18/MANIFEST.tsv",
    "manifest_sha256": "3688e8bc5e67e74039758515b849b61e0759f22dfd770c7f0770ee43ca1db68b",
    "manifest_line": 2,
    "input_sha256": "a59990bbfe5a8992ffa6e67e9b3e43e7ff477df9fc754e5af92b6f40d23fe11d"
  },
  "successor_revision": "cd9c8e4cb62896a8b5d0d642cd04966d41dd4d13",
  "input": "examples/culture-d4/typed-labels.d4.yml",
  "input_sha256": "cbcf997f5f38fac89b0fb1b6a6841ec42c9041a2599df44083ddefc5c22cfb4f",
  "projector_sha256": "76536a924280ad4187e2abeec1977b92861656a30d2dc7428f1f09087df8edfb",
  "packet_sha256": "e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3",
  "gate": "tools/gates/d4-typed-labels-check-gate.py",
  "gate_sha256": "05f99629d870280c55e15f46d799c29d7cfbc0645f0d0cd68a5fff1006181841",
  "exit_code": 0,
  "finding_count": 0,
  "output_sha256": "1c8add321259a9f026d6e37b0dbd95b0f548f31fe0a10c56098911c21532a6fe",
  "replay_command": "python3 tools/replay-frozen.py .scratch/r22-o11-successor-pre-r22/MANIFEST.tsv --json",
  "replay_date": "2026-10-18T14:42:02Z",
  "replay_exit": 0,
  "replay_reproduced": 2,
  "replay_rows": 2
}
```

This **persisted named record** is the selected disposition permitted by the route; it is not a claim that a new frozen generation was filed elsewhere. The successor snapshot is recoverable from the exact Git revision and input path above. The command below creates a disposable machine-readable manifest containing this new projection row and the unchanged original assembly row. Its scratch inputs/outputs are not independent sources of authority.

The immutable revision binding matters: R22's separately assigned family-clean projection fix will move the projection and projector again. This row documents the R18→R20 historical transition at the R22 declaration snapshot; it does **not** assert that its pins match the later moving R22 worktree. Any final-R22 re-pin is a further new row/generation owned by the current projection/re-pin seats, never an edit of this row or the old R18 manifest.

## Reproduced mechanism, with a historical positive control

The projection shim's own digest did not change. `tools/gates/d4-typed-labels-check-gate.py:33-50` runs its **live** peer `tools/d2-typed-labels.py` against the D4 packet beside that peer, while `replay-frozen.py` supplies the frozen projection as the comparison target. Thus an old projection can fail after a peer change even when the manifest's gate/input/output pins all verify. `reports/round-18/d4/replay.md:75-77` explicitly states that limitation.

On 2026-10-18, `git log --format='%H %s' e5718945a1ab0a0c3db955338d2cae77d68fd348..cd9c8e4cb62896a8b5d0d642cd04966d41dd4d13 -- tools/d2-typed-labels.py examples/culture-d4/typed-labels.d4.yml tools/gates/frozen/round-18/MANIFEST.tsv` identified the R20 admit `35b6797b42d48bec52e1e3ddba1f3afc9bb85046` as the committed change to the projector/projection. `reports/round-20/repin/O14-repin-table.md:24-38` records the same projector and D4 projection transitions. The original R18 manifest did not change.

Actual command for each original-manifest replay, with `TMPDIR` set to a sibling of the isolated clone:

```sh
python3 tools/replay-frozen.py tools/gates/frozen/round-18/MANIFEST.tsv --json
```

- **Historical positive, 2026-10-18T14:42:24Z:** fresh clone `.scratch/r22-o11-replay.cWR49r/history-r18` at R18 admit `e5718945a1ab0a0c3db955338d2cae77d68fd348`; original manifest **2/2 reproduced, exit 0**. Projector SHA-256 `0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802`; delivered projection `a59990bb…`; manifest `3688e8bc…`.
- **Stale-row negative, 2026-10-18T14:40:46Z:** fresh clone `.scratch/r22-o11-replay.cWR49r/clone` at `cd9c8e4cb62896a8b5d0d642cd04966d41dd4d13`; original manifest **1/2 reproduced, 1 mismatch, 0 unevaluable, exit 1**. Projection row line 2 launches, observes exit **1** versus recorded **0**, and stderr `examples/culture-d4/typed-labels.d4.yml differs from the deterministic projection`. Its stdout is empty (SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`). Assembly row line 3 still reproduces.
- **New-row positive, 2026-10-18T14:42:02Z:** command in the named row; successor manifest **2/2 reproduced, 0 mismatch, 0 unevaluable, exit 0**. The projection input digest changes to `cbcf997f…`; the gate, successful output digest and zero findings remain the same. Generated successor manifest SHA-256 `27ee8181f2a71e00d835d9aefee1f4d11e12ba4eff3fb87fa0d32ca724146163`.
- **Fail-closed control, same time:** `python3 tools/replay-frozen.py .scratch/r22-o11-successor-pre-r22/tampered-digest.tsv --json` uses a separate scratch manifest whose projection input digest is all zeroes. Exit **2**, projection reason `snapshot_tampered`, `gate_launched: false`; assembly still reproduces. No frozen snapshot is tampered with to make this fixture.

These controls distinguish a real historical peer-change mismatch from a missing ignored log or digest refusal. The R18/R20 `repin-d2` generations reproduce D2 rows; they do not supersede this D4 projection row. This note supplies the previously missing named D4 succession.

## Reproduction command for the new row and negative control

Run from the lane root. Replay tempdirs must be outside the **isolated clone root**, not outside the lane: sibling `$W/mirrors` satisfies the replay tool's guard while keeping every write inside this repo. No `/tmp` or `/var/tmp` path is needed.

```sh
export TMPDIR=$PWD/.scratch
export PYTHONDONTWRITEBYTECODE=1
mkdir -p "$TMPDIR"
W=$(mktemp -d "$TMPDIR/r22-o11-replay.XXXXXX")
git clone --quiet --no-hardlinks --no-checkout . "$W/clone"
git -C "$W/clone" -c advice.detachedHead=false checkout --quiet cd9c8e4cb62896a8b5d0d642cd04966d41dd4d13
mkdir -p "$W/mirrors"
(
  cd "$W/clone"
  export TMPDIR=$PWD/.scratch
  mkdir -p "$TMPDIR"
  python3 -B - <<'PY'
import csv, datetime, hashlib, io, json, os, subprocess
from pathlib import Path
root = Path.cwd()
sha = lambda b: hashlib.sha256(b).hexdigest()
protected = subprocess.check_output([
    'git','ls-files','-z','--',*[f'reports/round-{n}' for n in range(8,22)],
    'tools/gates/frozen/round-18'], cwd=root).decode().split('\0')[:-1]
before = {p:sha((root/p).read_bytes()) for p in protected}
with (root/'tools/gates/frozen/round-18/MANIFEST.tsv').open() as handle:
    rows = list(csv.DictReader(handle, delimiter='\t'))
original = dict(rows[0])
base = Path('.scratch/r22-o11-successor-pre-r22')
snapshot = base/'inputs/examples/culture-d4/typed-labels.d4.yml'
output = base/'d4-typed-labels-check-gate.out'
snapshot.parent.mkdir(parents=True, exist_ok=True)
snapshot.write_bytes((root/original['input']).read_bytes())
env = dict(os.environ, TMPDIR=str(root.parent/'mirrors'), PYTHONDONTWRITEBYTECODE='1')
recorded = subprocess.run(['python3', original['gate'], original['input']],
                          capture_output=True, env=env, cwd=root, check=False)
assert recorded.returncode==0 and recorded.stderr==b''
output.write_bytes(recorded.stdout)
row = dict(original, input_sha256=sha(snapshot.read_bytes()),
           input_snapshot=snapshot.as_posix(), output=output.as_posix(),
           output_sha256=sha(recorded.stdout), exit_code=str(recorded.returncode),
           finding_count=str(sum(line.startswith(b'FINDING ') for line in recorded.stdout.splitlines())))
def manifest(path, newrow):
    stream = io.StringIO(newline='')
    writer = csv.DictWriter(stream, fieldnames=list(original), delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows([newrow, rows[1]])
    path.write_text(stream.getvalue())
manifest(base/'MANIFEST.tsv', row)
manifest(base/'tampered-digest.tsv', dict(row, input_sha256='0'*64))
results = {}
for label, name in [('successor','MANIFEST.tsv'), ('tampered','tampered-digest.tsv')]:
    command = ['python3','tools/replay-frozen.py',(base/name).as_posix(),'--json']
    run = subprocess.run(command, capture_output=True, env=env, cwd=root, check=False)
    result = json.loads(run.stdout)
    results[label] = result
    print(datetime.datetime.now(datetime.timezone.utc).isoformat(), label,
          'exit', run.returncode, json.dumps(result['summary']))
    assert not run.stderr
assert results['successor']['summary']=={
    'rows':2,'reproduced':2,'mismatch':0,'could_not_evaluate':0,'exit':0}
assert results['tampered']['summary']['exit']==2
assert results['tampered']['rows'][0]['reason']=='snapshot_tampered'
assert not results['tampered']['rows'][0]['gate_launched']
assert row['input_sha256']=='cbcf997f5f38fac89b0fb1b6a6841ec42c9041a2599df44083ddefc5c22cfb4f'
assert sha((base/'MANIFEST.tsv').read_bytes())=='27ee8181f2a71e00d835d9aefee1f4d11e12ba4eff3fb87fa0d32ca724146163'
changed = [p for p in protected if before[p]!=sha((root/p).read_bytes())]
print('protected_paths',len(protected),'changed',changed)
assert changed==[]
PY
)
```

## Preservation and claim limits

Deliverable control: on 2026-10-18 at 14:43:23Z, a Python reader parsed the named JSON row, extracted this note's literal reproduction shell block, and ran it with `subprocess.run(['bash', '-e', '-c', script])` from the lane root. The fresh-clone reproduction exited 0; successor exit 0 / 2 of 2 reproduced and tampered-digest exit 2 / no projection gate launched both met their assertions. The protected comparison again reported `protected_paths 1030 changed []`.

- Before/after SHA-256 comparison in the executed new-row controls covered **1,030** tracked protected paths, **0 changed** (command above; 2026-10-18T14:42:02Z). Original R18 manifest SHA-256 before and after remains `3688e8bc5e67e74039758515b849b61e0759f22dfd770c7f0770ee43ca1db68b`; freeze receipt remains `fb703c9f3800594c422c5df56133a5bf6ff692c9b6822f67df50a205f47fee4c`.
- Replays assert reproduction of pinned NON-CANON bytes, not correctness, permission, canon, or acceptance. No historical round validator, commit, or push was executed by this seat.
- The original R18 frozen generation had two recorded check rows and a pending generalized typed-pipeline row (`reports/round-18/d4/manifest.md:15-38`; `freeze-receipt.json.pending`). Neither a historical nor a successor **2/2** replay proves that pending leg was recorded, or by itself proves R18 verified every part of R17's claim.
- Parent integration: record `R18-ORIGINAL-FROZEN-REPLAY` as `resolved-by-documentation`, reference this note and `R22-O11-SUPERSESSION-1`, retain the original mismatch, and keep the final R22 projection/gate re-pin evidence separate. Do not reinterpret the R18 admission or rewrite old replay notes.
