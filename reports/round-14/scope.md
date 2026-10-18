# Round 14 scope watch — X02

- **Date / seat:** 2026-10-17, R14-X02; non-canon engineering evidence, not a round-admission verdict.
- **Axes:** O — repository boundaries and historical-artifact preservation; D — prevention of receipt clobbers; C — distinguish observed bytes, additive corrections, and historical incidents.
- **Declared baseline:** `926c86f8be3cc9307f8f10dce55768c290b6f94d` (`reports/round-14/claims.json:5`). Lane HEAD throughout the initial checks: `a7bc9e9ff05a57515c5efaaa7e50116eb30938ff`, declaration at `2026-10-17T20:56:20-03:00`.
- **Worker write surface:** this file only. All commands ran from `/home/vgpnk/Projects/shokunin/kotodama-shokunin` with `export TMPDIR="$PWD/.scratch" GIT_OPTIONAL_LOCKS=0`; no scratch files, historical artifacts, fleet-root files, or sibling files were written by this seat. No commit or push.

## Findings

### 1. Fleet-root cleanliness — inherited exception, not a clean verdict

At `2026-10-17T20:57:37-03:00` and `20:58:57-03:00`, the read-only command

```sh
git -C /home/vgpnk/Projects/shokunin status --porcelain=v1 --untracked-files=all
```

returned exactly `?? baseline-analyze.txt` (one visible untracked path; audit date 2026-10-17). The root's tracked and staged diffs were empty at `20:57:37-03:00` (`git -C /home/vgpnk/Projects/shokunin diff --name-status` and the same command with `--cached`). Its HEAD was `272e49b3a23a708a87d23713e826be5390a5c2d5`, committed at `20:55:04-03:00`, before the lane declaration.

The Python `Path.stat()` check at `2026-10-17T20:57:59.858162-03:00` found that `/home/vgpnk/Projects/shokunin/baseline-analyze.txt` is 105 bytes with mtime and ctime `2026-10-17T20:30:10.645272-03:00`. Those recorded times predate Round 14; they do not identify an author or prove that no process can preserve timestamps. The file's content was not inspected. Do not attribute it to this round, and do not report the root as clean.

**Control / disposition:** reported as an inherited fleet-hygiene exception to the integrator. This lane has no authority to delete, move, ignore, stage, or rewrite the parent-tree file. The fleet owner must disposition it on its own authority; the acceptance control is a dated rerun of the root porcelain command, not an in-lane cleanup workaround. Compare later root path sets with this initial singleton to detect newly visible paths.

### 2. Filed rounds 8–12 — baseline preserved except a controlled additive-key correction

A read-only Git-object comparison completed at `2026-10-17T20:57:59.568047-03:00` (reproducer below). It compared every baseline-tracked file in `reports/round-8` through `reports/round-12` with its current bytes:

- Round 8: 153 baseline files, 153 byte-identical.
- Round 9: 87 baseline files, 87 byte-identical.
- Round 10: 73 baseline files, 72 byte-identical; `findings-tracker.json` differs.
- Round 11: 252 baseline files, 252 byte-identical.
- Round 12: 44 baseline files, 44 byte-identical.
- Total: 609 baseline files, 608 byte-identical, no missing files. No visible untracked additions under these historical report roots at that stamp (`git ls-files --others --exclude-standard -- reports/round-{8,9,10,11,12}`).
- `git diff --name-status 926c86f8be3cc9307f8f10dce55768c290b6f94d HEAD -- reports/round-{8,9,10,11,12}` returned no committed historical-path change at `20:57:59` and `20:58:44-03:00` on 2026-10-17.

The tracker was absent from lane porcelain at `20:57:37-03:00`, then appeared modified at `20:57:59-03:00`. `stat -c '%n | size=%s | mtime=%y | ctime=%z' reports/round-10/findings-tracker.json` at `2026-10-17T20:58:22-03:00` recorded mtime `20:57:52.616548915-03:00`, after declaration. This is a current-round delta, not the inherited round-11 fragment incident.

The diff adds the `errata` key containing `R14-O03`; it does **not** replace `final_state.verify_files` or any other original JSON value. The new entry's `control.evidence` names `reports/round-14/fix-tracker-pointer.md` (`reports/round-10/findings-tracker.json:388-414` at the inspected snapshot). Independent JSON comparison at `2026-10-17T20:58:44.545185-03:00` found every original key present, every original value equal, no removed keys, and only `errata` added. Thus it fits the worker directive's explicit **new-key append exception**, but it is not a literal byte append and it cannot support an unqualified assertion that all filed file bytes are unchanged.

Tracker hashes from that comparison:

- Baseline, 38,954 bytes: `5a0ca3de9a058de2b8e772f5f2af0bd5302a04957764e3639938f00ba496effc`.
- Current, 39,985 bytes: `4b983ae9237dda1b46fba59fac2ce8731a1a924ae9672925757bcc4ebc30def2`.

**Control / disposition:** retain the distinction between additive-key preservation and whole-file byte invariance. The old fields must remain equal to the baseline; added errata must identify their round, source, and independent evidence. The round declaration (`claims.json:14`) also promises that filed bytes are never modified, and the historical routing note (`reports/round-12/defects/routed.md:62`) says not to back-patch this tracker. The integrator must reconcile that stricter claim with the allowed new-key exception before asserting O green; a separate new Round-14 correction file avoids the conflict. This seat does not restore or modify another seat's work. Re-run both controls below at close, recording any additive exception explicitly rather than silently counting it as byte-identical.

#### Reproducible, read-only byte and additive-key controls

These are the algorithms executed by inline `python3 - <<'PY'` commands at the stamps above; they read Git objects and the worktree and write stdout only. The Git object format was the existing SHA-1 object format represented by the inspected tree IDs.

```sh
export TMPDIR="$PWD/.scratch" GIT_OPTIONAL_LOCKS=0
python3 - <<'PY'
from collections import Counter
from datetime import datetime
import hashlib, json, os, pathlib, subprocess
base = json.loads(pathlib.Path('reports/round-14/claims.json').read_text())['baseline_revision']
roots = [f'reports/round-{n}' for n in range(8, 13)]
def git(*args):
    return subprocess.check_output(['git', *args])
counts, changed, missing = Counter(), [], []
for entry in git('ls-tree', '-r', '-z', base, '--', *roots).split(b'\0'):
    if not entry:
        continue
    meta, rel = entry.split(b'\t', 1)
    mode, kind, oid = meta.decode().split()
    p = pathlib.Path(os.fsdecode(rel))
    scope = '/'.join(p.parts[:2])
    counts[(scope, 'baseline')] += 1
    if not p.exists() and not p.is_symlink():
        missing.append(str(p))
        continue
    raw = os.readlink(p).encode() if mode == '120000' else p.read_bytes()
    observed = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
    if observed == oid:
        counts[(scope, 'identical')] += 1
    else:
        changed.append(str(p))
print(datetime.now().astimezone().isoformat(), sorted(counts.items()))
print('changed', changed, 'missing', missing)
p = pathlib.Path('reports/round-10/findings-tracker.json')
old_raw = git('show', f'{base}:{p.as_posix()}')
new_raw = p.read_bytes()
old, new = json.loads(old_raw), json.loads(new_raw)
print('tracker', {'original_fields_unchanged': all(k in new and new[k] == v for k, v in old.items()),
                  'removed_keys': sorted(old.keys() - new.keys()),
                  'added_keys': sorted(new.keys() - old.keys()),
                  'literal_byte_append': new_raw.startswith(old_raw),
                  'old_sha256': hashlib.sha256(old_raw).hexdigest(),
                  'new_sha256': hashlib.sha256(new_raw).hexdigest()})
PY
```

### 3. Historical incidents — receipt restoration is not prevention

At `2026-10-17T20:58:57.562897-03:00`, an inline Python comparison using `git show <revision>:<path>`, `Path.read_bytes()`, and `hashlib.sha256()` found:

- `reports/round-8/validation.json` equals its admission-commit bytes at `e1694bad6ac96aca45a11ca5746582b275929355`; SHA-256 `359932a7debf6ec39f3182ac078ae3e900860efd97831f6b41bfe818b96ccfba`.
- `reports/round-9/validation.json` equals its admission-commit bytes at `9dc18ec1339bffd6f81e74f1a5742464ef578749`; SHA-256 `036f84278c4817901413d97839ceba78aa8a367f91579de7505c92800611e418`.
- `reports/round-10/coverage/index-update-22.md` matches the Round-14 baseline (`2c33853f117be0d3296427fb383d7ded71ed74cf2cbd6fbd99d14c71e2c22d83`) but **not** the round-10 filing at `94ca098b8ab03be52ec80f6925538e5e2c0ed327` (`1b30ea92afa5ceb4192840cc6e3edcd07e7b597d3b1eee95bf9adac4efbe6d5e`). It therefore remains a historical post-filing mutation, not a newly observed Round-14 rewrite. `reports/round-11/adjacency.md:69-77` supplies the contemporaneous incident evidence.

The earlier receipt-clobber mechanism remains established by `reports/round-11/adjacency.md:39-67`; current equality does not erase that history. The same principle applies to the out-of-lane V09 incident documented at `reports/round-9/adjacency.md:191-214`: a later clean snapshot would not prove it never occurred.

**Control / disposition:** never re-run historical round validators in the live lane for this scope audit. Check historical receipts by reading Git objects; run any necessary historical writer in an isolated in-lane mirror or redirect its output. The assigned guard owner must demonstrate the declared `REFRESH_RECEIPTS=1` opt-in and default refusal controls for successor runners; guard implementation and acceptance are not certified by this scribe. The round-8–11 runners must remain filed, per `claims.json:22`. Any explanation of the already-filed round-10 append belongs in a new record, not a restoration or rewrite by this seat.

### 4. PROVINCE remains accurate; ownership does not expand

`git diff 926c86f8be3cc9307f8f10dce55768c290b6f94d -- PROVINCE.md AGENTS.md corpus/knowledge/synthesis/worldbible-integration-contract.md` was empty at `2026-10-17T20:57:59-03:00`. `sha256sum` at that stamp returned:

- `PROVINCE.md`: `05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6`.
- `AGENTS.md`: `be3a9477ed28ba401352ebce7c182d529223e552d0dba0d75f3b97b956be2c8b`.
- `corpus/knowledge/synthesis/worldbible-integration-contract.md`: `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069`.

The scope mapping is unchanged:

- O fixes and regression records concern this lane's own gates, baselines, reports, and source-check records (`PROVINCE.md:9-14`).
- D's receipt guard protects this lane's own harnesses and filed records. Its reusable implementation does not grant ownership of fleet protocol or general research method; those remain excluded at `PROVINCE.md:13-14,19-20`.
- C's loop retrospective and local SCORECARD/LOG integration are this lane's own records, not authority to change sibling records or canon.
- Lore still owns the world bible and canon (`PROVINCE.md:16-25`). The unchanged contract says initial bilateral acknowledgement is pending and that each lane writes only its own authorized surfaces (`corpus/knowledge/synthesis/worldbible-integration-contract.md:14-19`). No retrospective admission of a craft round is a canon decision.

**Control / disposition:** no PROVINCE amendment needed for these declared Round-14 surfaces. Preserve the refusal and handoff boundaries and route contested or parent-tree scope to the integrator. `git ls-files --stage` showed no tracked symlinks at `2026-10-17T20:58:22.748466-03:00`; `Path('reports/round-14').resolve().is_relative_to(Path.cwd().resolve())` returned true. These check the assigned output destination, not all possible future worker writes.

### 5. Sibling watch and evidence limits

A read-only inline Python sweep finished at `2026-10-17T20:57:59.858162-03:00`. It iterated immediate fleet child directories with `.git`, excluding Kotodama, and ran `git -C <repo> status --porcelain=v1 -z --untracked-files=all`, `git -C <repo> log --since=2026-10-17T20:56:20-03:00 --format='%H %cI %s'`, and `git -C <repo> log -1 --format='%H %cI %s'`.

Of 19 siblings in that dated census, 18 had zero visible status entries. `lore-shokunin` had 44,825 entries (7 modified and 44,818 untracked), including its `.ufo/waves/round-98/` artifacts and corpus/tool work; its HEAD was `dd4df1b36a64b513e75b46da04ee2f3f7f3eb6cb` at `20:24:41-03:00`. All 19 siblings and the fleet root had zero commits at or after the declaration cutoff according to those `git log --since` queries. These are process-unattributed, non-atomic snapshots; no Kotodama attribution follows from a sibling being dirty.

The root ignores lane repositories (`git -C /home/vgpnk/Projects/shokunin check-ignore -v kotodama-shokunin` returned `.gitignore:1:*-shokunin/`; parent `git ls-files --stage -- kotodama-shokunin` was empty at `2026-10-17T20:57:59-03:00`). Therefore even a clean fleet root would not establish sibling cleanliness. Porcelain also excludes ignored scratch, ignored reports, and other ignored surfaces. This audit does not claim a complete filesystem or process-attribution proof.

## Follow-up snapshot and independent controls

### Filed-byte census and append-only exception

The report's embedded byte-comparison command was extracted and executed directly with `python3 -c <extracted-code>` at `2026-10-17T21:00:09.364747-03:00`; it exited 0. The updated census was **607/609 baseline files byte-identical**, with no missing files. The two differing files were the tracker above and `reports/round-12/defects/ledger.json`; all other baseline round-8–12 files still matched. This supersedes only the initial census, not its stamped observation. `git status --porcelain=v1 --untracked-files=all -- reports/round-{8,9,10,11,12}` at the same stamp listed only those two modified paths. No historical runner or validation receipt appeared in the dirty set.

The ledger delta appends `FRR-14-EXPOSURE` at `reports/round-12/defects/ledger.json:135-173`. Independent inline `python3` JSON and raw-byte controls at `2026-10-17T21:00:57.086361-03:00` found 15 original entries preserved as an equal prefix of the now-16-entry array; every other top-level value remained equal. Removing only the newly inserted entry and its JSON separator reconstructed the complete original file bytes. Baseline SHA-256 was `a100c048a2f29374d1da7ab0b147f915c06678c7ab2366a4aef60db235c08a69`; current SHA-256 was `328f33d2375a8b90213d8ece20e833523abcb675af51be11f7458f0424bd1a60`. This is the additive ledger erratum explicitly required by claim D, not a change to any historical disposition.

Exact ledger control (read-only, executed at the stamp above):

```sh
export TMPDIR="$PWD/.scratch" GIT_OPTIONAL_LOCKS=0 PYTHONDONTWRITEBYTECODE=1
python3 - <<'PY'
import json, pathlib, subprocess
p = pathlib.Path('reports/round-12/defects/ledger.json')
base = '926c86f8be3cc9307f8f10dce55768c290b6f94d'
old = subprocess.check_output(['git', 'show', f'{base}:{p}'])
new = p.read_bytes()
a, b = json.loads(old), json.loads(new)
assert b['entries'][:len(a['entries'])] == a['entries']
assert len(b['entries']) == len(a['entries']) + 1
assert b['entries'][-1]['id'] == 'FRR-14-EXPOSURE'
assert {k: v for k, v in a.items() if k != 'entries'} == {k: v for k, v in b.items() if k != 'entries'}
marker = b',\n  {\n   "id": "FRR-14-EXPOSURE"'
prefix, payload = new.split(marker, 1)
entry_text = (b'{\n   "id": "FRR-14-EXPOSURE"' + payload).decode()
_, end = json.JSONDecoder().raw_decode(entry_text)
assert prefix + entry_text[end:].encode() == old
print('PASS: original entries and complete original bytes preserved outside insertion')
PY
```

The complete tracker control in `reports/round-14/fix-tracker-pointer.md:26-125` was independently extracted and executed with `python3 -c <extracted-code>` at `2026-10-17T21:00:22.231172-03:00`, exit 0. It verified exact reconstruction of the original bytes, original finding-row bytes unchanged, and the effective verifier list matching the actual files. Its missing-verifier, nonexistent-verifier, and filed-row-mutation negative controls all passed. Thus both differing historical JSON files are verified additive exceptions; neither permits the phrase “all filed files byte-identical.”

### Guard boundary probes — no writer invoked

At `2026-10-17T21:00:33.498725-03:00`, an inline `python3` subprocess harness invoked the guard CLI with separate environments and asserted the following actual exit codes and diagnostics:

```sh
# REFRESH_RECEIPTS absent from the child's environment:
env -u REFRESH_RECEIPTS python3 -B tools/harness/receipt_guard.py --repo-root "$PWD" reports/round-8/validation.json
# exit 3; RECEIPT-GUARD-COMMITTED
env -u REFRESH_RECEIPTS python3 -B tools/harness/receipt_guard.py --repo-root "$PWD" reports/round-9/validation.json
# exit 3; RECEIPT-GUARD-COMMITTED
# Read-only preflight only, not an invocation of a receipt writer:
REFRESH_RECEIPTS=1 python3 -B tools/harness/receipt_guard.py --repo-root "$PWD" reports/round-8/validation.json
# exit 0; RECEIPT-GUARD-ALLOW
REFRESH_RECEIPTS=1 python3 -B tools/harness/receipt_guard.py --repo-root "$PWD" /home/vgpnk/Projects/shokunin/x02-unwritten-path-control.json
# exit 3; RECEIPT-GUARD-PATH
```

The guard implementation's SHA-256 was `d7199bd6f87c3ddec18407d6117c43cdd1bb092bfacd752219a9b41e5ef39c83` at that control. The harness compared the five round-8–12 `validation.json` SHA-256 values before and after; all were unchanged, and the planted out-of-lane destination did not exist after the probe. No writer or runner callback was invoked, and no out-of-lane file was created. The opt-in test does not authorize refreshing historical receipts. These probes establish the CLI's observed behavior only; they do not establish runner wiring, the full selftest suite, or dispatch-wide worker confinement. The helper itself expressly says it is not a sandbox for arbitrary callback writes (`tools/harness/receipt_guard.py:9-10`).

### Report checks and remaining scope limits

At `2026-10-17T21:00:09.369385-03:00`, an inline Python check compiled and executed the embedded census control, checked balanced Markdown fences and trailing whitespace, and printed `scope_report_format_and_embedded_control: PASS`. `git diff --check` at `21:00:09-03:00` also exited 0. Lane and root HEADs retained the values cited above at `21:00:09` and `21:00:22-03:00`, respectively. A final report-contract check at `2026-10-17T21:01:29.928952-03:00` compiled and executed both embedded Python controls, each exiting 0; the census remained 607/609 with only the two verified additive exceptions and no missing files. At `21:01:29-03:00`, the root still showed only `?? baseline-analyze.txt`, the PROVINCE / AGENTS / handoff-contract diff remained empty, and `git diff --check` again exited 0. The wave was still writing; none of these snapshots certifies later worker actions.

## Integration requirements

- Keep the inherited root exception visible until the authorized fleet owner dispositions it with a dated status control.
- Reconcile the allowed tracker new-key and ledger-entry additions with stronger whole-file-byte wording. Preserve original fields and all receipt bytes; prefer separate Round-14 correction files where possible. Record the additive exceptions explicitly rather than asserting whole-file identity.
- Preserve historical mutation evidence; do not mislabel baseline equality as equality to original filing.
- Re-run the byte, root, and PROVINCE controls on the settled tree. This in-flight scope report does not substitute for the assigned regression runners, guard tests, dispatch-boundary negative control, or the parent's final `reports/round-14/run-validation.py` acceptance run.
