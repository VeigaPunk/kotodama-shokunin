# R22-O01–O03 — carried-edge provenance correction

Date: 2026-10-18. Axes: operability, v2 compatibility, reproducibility. Source owner: this seat, `tools/exercise-handoff-e2e.py`. Status: declared_in source repair, paired controls, and the new revision-2 frozen verification are green in both the isolated clone and working tree. The separate D4 historical-claim wording remains an explicit parent-integration caveat below; this is not round-wide admission. No round validator ran and no filed round-8–21 artifact was edited.

## Contract and measured defect

The filed renderer calls all 34 v2 edge rows “carried verbatim.” The v2 source actually declares `declared_in` on every edge. Contract §4 requires source/invention provenance and justified relations; §9 requires changed releases and pins to be new records, not rewritten filed bytes. Therefore this repair preserves the original fields rather than weakening the claim. Adding the optional provenance column is a MINOR correcting revision, packet version **3.1.0**; the round-20 3.0.0 packet remains filed.

At **2026-10-18T14:39:59Z**, this command shape compared the filed v2 edges, read with the existing harness reader, with the matching filed v3 twin rows:

```python
reader = runpy.run_path('tools/harness/packet_links.py')
v2 = reader['read_packet'](Path('reports/round-15/handoff/packet-v2-05.yml'))
v3 = json.loads(Path('reports/round-20/handoff/twin.json').read_text())
old = {e['edge_id']: e for e in v2['coupling_edges']}
new = {e['edge_id']: e for e in v3['coupling_edges'] if e['edge_id'] in old}
Counter(k for eid, e in old.items() for k in set(e) | set(new[eid])
        if e.get(k) != new[eid].get(k))
```

Result: **34** v2 edges and **34** matching v3 edge IDs; differences were **34 `declared_in` omissions, five truncated `mechanism` values, and five truncated `limits` values**. All provenance values were strings. The truncations affect BR01–BR05 and were an additional loss in the same verbatim-carry contract. At 14:40Z, `[(e['edge_id'], k) for e in old.values() for k, v in e.items() if isinstance(v, str) and cell(v) != v]` returned `[]`: unbounded table-cell rendering preserves the filed scalar values exactly.

## Source repair and paired controls

- The generator reads complete v2 edge mappings from the **selected input root**, not a field allowlist rooted at the module checkout. `declared_in` is no longer dropped at selection. A mirror-root control changes just that field in a copied v2 source and proves the generator uses the selected root's bytes.
- Markdown emits the new `declared_in` column and does not length-limit relation, applicability, mechanism, or limits. The twin is still projected from the parsed delivered table and explicitly preserves `declared_in`. D4-generated edges name their actual D4 packet as provenance; that is not canon authority.
- `V3Assembly.assert_subset_equality()` now compares the **entire ordered 34-edge subset**, including all keys and list/scalar values, independently against the filed v2 source in **both Markdown and twin**. Existing 15-claim normalized subset checks remain unchanged.
- Eight negative checks drop/change `declared_in` or truncate mechanism/limits, separately in each delivered surface. Every mutation must raise `E2E-DIGEST`. A positive check verifies all 34 complete mappings, and the alternate-root check prevents a local fixture from being silently bypassed.
- The renderer's packet text, module contract, version and default baseline path name the correction. First new row: `reports/round-22/handoff/declared-in/expected.json` (3.1.0); current default: `reports/round-22/handoff/declared-in-r2/expected.json` (3.1.1, final combined-projector pins). Both new rows are preserved; old round-20 pins are never edited or silently accepted.

## Isolated verification of the provenance change

Commands ran in a real Git clone under `.scratch/r22-declared-in.GXeE3A/repo`, at baseline `46a03257ee75dd8f685a105e47da3f45a0154172`, with only this seat's renderer overlaid. Every scratch-writing command first exported `TMPDIR=$PWD/.scratch` and `PYTHONDONTWRITEBYTECODE=1`; subprocess TMPDIR was the clone's own `.scratch`. No round validator was invoked.

- **2026-10-18T14:41:54Z** — `python3 -B tools/exercise-handoff-e2e.py --profile v2`: exit **0**, **15** claims, **50/50** links, shape **16/16**, glossary **20**, zero findings apart from the two already-named tool-digest allowances. The filed v2 twins match their original pins.
- **2026-10-18T14:43:04Z** — `python3 -B tools/exercise-handoff-e2e.py --profile v3 --freeze reports/round-22/handoff/declared-in`: exit **0**. New isolated pin: packet `83504ee73d4b95451eb765867719e27dec41d49654a6233283781a523b45048f`; twin `19b4b915f5a16c6e8755250a244e5951f739a603443733bd81c67be28e8d4237`.
- **2026-10-18T14:43:06Z** — `python3 -B tools/exercise-handoff-e2e.py --profile v3`: exit **0**, **105/105** links, **27** claims, statuses **16 supported / 7 partial / 4 unresolved**, **88** edges, **16/16** fields, **20** glossary rows, zero findings. All **58** inputs, **25/25** component digests and **8/8** D4 tree pins match. Both carried-edge surfaces are exactly equal to the v2 source. The unchanged 15-claim subset digest is `ad35c860acf3b452c6f8974cd08a8333fa1ffd7758b371c12123b6437bde069b`.
- **2026-10-18T14:43:07Z** — `python3 -B tools/exercise-handoff-e2e.py --profile v3 --baseline reports/round-20/handoff/expected.json`: expected exit **1**, `E2E-DIGEST`, because the corrected packet no longer equals the old immutable packet pin. Semantic legs and v2 equality still pass. This is the supersession control, not a waived failure.
- **2026-10-18T14:43:09Z** — `python3 -B tools/exercise-handoff-e2e.py --profile v1 --selftest`: exit **0**, positive run plus **17** controls.
- **2026-10-18T14:43:10Z** — `python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest`: exit **0**, positive run plus **38** controls, including all provenance/truncation/root controls and the existing tamper controls.
- **2026-10-18, 14:43Z** — `git diff --check -- tools/exercise-handoff-e2e.py`: exit **0**. Renderer SHA-256 under test: `b707615c1848f89e1ae758b9d714b9791848a6119cd36d66513895ff39055aa3`.

## Integration dependency and witness control

At **2026-10-18T14:43:35Z**, a SHA-256 comparison of the isolated pin's 58 inputs against the working tree found only `tools/d2-typed-labels.py` moving. The D4 source/adapter owner is still repairing that tool and its derived outputs. The independent clone verifies this seat's change without adopting half-written D4 bytes. The new deliverable pin and final working-tree verification will be recorded below once that cascade is coherent; a stale/partial dependency is not a green integrated receipt.

The alias fix adds passing tests (its receipt reports 132/132), exposing a hard-coded `50/50` witness string in this handoff tool. The source now requires exit 0, a parsed `selftest: passed/total checks passed` summary, equal passed/total counts, and the original minimum of 50 projector checks or 12 adapter checks. Larger complete suites pass; partial, undersized, zero-sized, unparsed, and nonzero-exit suites fail. This change is required to integrate the stronger alias controls without weakening the evidence requirement. It has its own positive/negative matrix in the existing v3 selftest.

At **2026-10-18T14:45:31Z**, `python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest` in the same isolated clone passed, exit **0**, positive run plus **39** controls, with the unchanged **105/105** link and **27**-claim census. At **14:47:05Z**, the one-minute dependency poll still found the projector moving while the D4 projection retained its original `cbcf997f…` hash; no integrated freeze was claimed.

The concurrent family-clean D4 change also requires a later superseding D4 claim description, not just new hashes: the immutable round-20 `claims-map.md` describes the old inherited D2 debt (especially D4-CL05/06/07/09). This seat's provenance-only controls intentionally preserve those filed claims; the final D4 integration owner must not mistake that compatibility assertion for a claim that the inherited debt remains D4-owned after the separate source fix.

## Published new rows and final verification

The first working-tree row, `reports/round-22/handoff/declared-in/`, was frozen at **2026-10-18T14:49:14Z**, tested in its isolated snapshot at **14:49:30Z** (v3 exit 0, 105/105 links), and published without modifying any older row. Packet 3.1.0: `ba3d0deed2b0dfea05d62aa5a1464b1f6b6dba6efd0c05501b3ecc243c56b94c`; twin: `302c814368996d8350b0ad10e678390f809609875d27c9ac8ab6dab3ddaa0e44`.

The projector owner then finalized two comment-only corrections. At **14:50:41Z**, `python3 -B tools/exercise-handoff-e2e.py --profile v3` correctly exited **1 / E2E-DIGEST**, naming the changed projector and expected-hold source pin. That first new row was **not overwritten**. Its captured clone remains `.scratch/r22-declared-in-final-dj9n7392/repo`.

The successor is **3.1.1**, `reports/round-22/handoff/declared-in-r2/`. It supersedes the first new row's computational pins, preserves all claim rows and all v2 compatibility controls, and binds the final combined projector `2819f68769dfc0b57f46cdaeb4c9a96324c5711c46348f5a8308382dfd7053c3` plus expected holds `3826ba68d705b3c379b2a12737c14075d9095a1ba2aa2eb525de1851a9ecd2f7`. Each row contains `expected.json`, `packet.md`, `twin.json`, `run.log`, and `freeze.txt`.

Final commands ran on **2026-10-18**, with `TMPDIR=$PWD/.scratch` and `PYTHONDONTWRITEBYTECODE=1`, in the fresh snapshot `.scratch/r22-declared-in-r2-whpgj6nt/repo` unless explicitly marked live:

- **14:52:35Z** — `python3 -B tools/exercise-handoff-e2e.py --profile v3 --freeze reports/round-22/handoff/declared-in-r2`: exit **0**, new packet SHA-256 `a97a0f0a0a497cb4410124607065df7686bbc7f78b4b46bdaaaa1d66ba4d1b6e`, twin SHA-256 `d3de56a8be1d28fdcead751aa0ac9364f7b43ff2b8bad71b696f0b57955b4d5c`.
- **14:52:56Z (live)** and **14:52:59Z (clone)** — `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet`: both exit **0** and print the same new packet digest, **16/16** fields, **20/20** glossary, **0** findings, **105/105** links, **27** claims, statuses **16/7/4**, v2 subset equal, alias leg landed.
- **14:53:02Z** — `python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest`: exit **0**, positive run plus **39** controls. The final projector witness is **163/163**; adapter witness **12/12**. The widened witness reader accepts these complete suites without changing its minimum or exit requirement.
- **14:53:37Z** — `python3 -B tools/exercise-handoff-e2e.py --profile v2 --quiet`: exit **0**, **15** claims and **50/50** links, filed twins unchanged.
- **14:53:38Z** — `python3 -B tools/exercise-handoff-e2e.py --profile v1 --selftest`: exit **0**, positive run plus **17** controls.
- **14:54:00Z** — `python3 -B tools/exercise-handoff-e2e.py --profile v3 --baseline reports/round-22/handoff/declared-in/expected.json`: expected exit **1 / E2E-DIGEST**, naming exactly the projector and expected-hold pin that moved. This is the new-row supersession control; neither first-row digest was rewritten.
- **14:54:03Z (live)** — command shape `json.loads(expected/twin); parse_edges(packet); v3_load_v2_edges(ROOT); sha256(payloads/inputs); v3_baseline_digest(expected)` verifies both delivered digest pins and baseline integrity, **34/34** exact v2 edge mappings in **both** delivered formats, and **zero** live input drift. Renderer SHA-256: `c185500e173e1095c0d34f60a0a3a5e2bd11bfafbf5c52d7c7e9077fe8dae452`.
- **14:53Z** — `git diff --name-only -- reports/round-{8..21}` returns no paths. `git diff --check -- tools/exercise-handoff-e2e.py` is green.

The computational provenance assignment is verified. Round-22 counting-command admission/shared bookkeeping and superseding the stale D4 claim prose are the parent integrator's work, not passes claimed by this seat. A later integrated semantic packet needs another new row; do not rewrite either provenance row to hide the history.
