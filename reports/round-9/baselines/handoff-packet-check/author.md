# R9-O baseline author — `handoff-packet-check` (frozen run `r9-pre`)

- shard: round-9 claim O, targets `R9-O01..O14` ("fragment per gate"); this file is the author
  half of the `handoff-packet-check` pair. The second (rerun/verifier) seat owns its own file.
- date: 2026-10-17. measured tree revision: `a7bb205d3aecdaa24d91c047c8719cd8689e4ddd`
  (pre-integration; the orchestrator's round-9 commit will carry the baseline).
- standard followed: `corpus/knowledge/verification/gate-frozen-run-standard.md` §3 (layout),
  §4 (`expected.json` fields), §5 (freeze procedure), §6 (verify/tamper/class mapping).
- scope kept: **no gate behavior change** (the gate source was not touched), no shared file
  written (`tools/gates/frozen/README.md`, `SKILL.md`, the corpus entry are the orchestrator's
  integration surface — races avoided deliberately), no commits.

## 1. Files written — one baseline, two homes (byte-identical, digests match)

| path | role |
|---|---|
| `<home>/packet.md` | byte copy of the graded input (role-named; `.md` because the graded packet is Markdown) |
| `<home>/expected.json` | §4 fields + `baseline_id`/`command`/`input_origin` (`clean`, exit 0, findings `[]`) |
| `<home>/run.log` | gate stdout verbatim over the snapshot copy |
| `<home>/freeze.txt` | command / revision / frozen_at / check result / battery validation / relocation record |
| `reports/round-9/baselines/handoff-packet-check/author.md` | this fragment (round-9 home only) |

- Home A (fragment + pair protocol): `reports/round-9/baselines/handoff-packet-check/`
- Home B (standard §3 + battery root): `tools/gates/frozen/handoff-packet-check/r9-pre/`
- Identity check, 2026-10-17 (`sha256sum`, both homes; final values): `packet.md 0d8d660b…`,
  `expected.json 9dc21cd5…`, `run.log 7c581047…`, `freeze.txt f83ac075…` → identical. The three
  pinned files never changed after the freeze; `freeze.txt` gained the battery-validation and
  divergence sections (an earlier reading was `3e56d2b7…`), so cite its digest only with a date.
- Why two homes rather than one: `tools/check-gate-battery.py` (the round-9 O15 instrument that
  claim O counts on) scans `BASELINE_ROOTS = tools/gates/expected/ + tools/gates/frozen/` and
  reads any gate without a baseline there as `BASELINE-GATE-UNCOVERED` (exit 2); the round-9 root
  is not scanned. Sibling pairs (naming, phonology) keep their files under the round-9 root, so
  the round needs both. One baseline id `r9-pre` — not two freezes; never re-pin one home alone.

Input choice: the **real** delivered artifact `examples/culture-d3/handoff.md` rather than the
planted-defect fixture. The standard (§7) used the fixture only because no real packet existed at
the time; a real D3 handoff packet exists now, and a frozen run is measurement, not capability —
the fixture already carries the capability half. The pin covers one file, which is exactly what
this gate reads (glossary bytes delivered only as external files get an INFO line, never a file
read — gate docstring, line 96).

## 2. Measured, with commands (2026-10-17, from the lane root)

| # | command | observed |
|---|---|---|
| 1 | `python3 tools/gates/handoff-packet-check.py --selftest` | exit 0; `selftest: OK — fixture findings 11 across 9 ids (HO-BASELINE, HO-CANON-CLAIM, HO-CANON-MARKER, HO-CONTRACT-REF, HO-DEP-FLOAT, HO-EMPTY, HO-GLOSS-ETYM, HO-MANIFEST-DIGEST, HO-MISSING); clean control exit 0; …; malformed inputs exit 2; CLI verified from another cwd` |
| 2 | `sha256sum examples/culture-d3/handoff.md tools/gates/handoff-packet-check.py` | input `0d8d660bf9797d1c15da477f96ded75553a8d2ca7f04f75aa86a8a65e28fd2fc`; gate `e2fa3223b2aa57382807c51099a4360c1a9cc2559d5b4bedad1b54e9ab0ad575` |
| 3 | `cp examples/culture-d3/handoff.md <home>/packet.md` | copy digest equals the source digest: byte-identical |
| 4 | `cd <home> && python3 <lane>/tools/gates/handoff-packet-check.py packet.md > run.log` | exit 0; stdout = `INFO scan: fields=16/16 glossary-entries=20 findings=0` (run.log sha256 `7c581047…`); stderr empty |
| 5 | digest check re-read from `expected.json` (python, §6 step 1) | `packet.md OK`; `stdout_sha256` matches `run.log`; gate `e2fa3223…` unchanged |
| 6 | gate re-run over `reports/round-9/baselines/handoff-packet-check/packet.md` after relocation | exit 0, stdout byte-identical to `run.log` — the verdict line carries no path |
| 7 | `python3 tools/check-gate-battery.py` (default roots) | this baseline's record: `"reading": "pinned"`, `inputs_checked 1`, gate sha match, stdout pin match, `findings []` (battery exit 2 comes from three other gates, below) |
| 8 | tamper drill on a copied root: `cp` the four files to `.scratch/r9-handoff-author/tamper-root/…`, append one byte to `packet.md` (`047b7d53…`), `python3 tools/check-gate-battery.py --baselines-root .scratch/r9-handoff-author/tamper-root` | record reads `snapshot_tampered`, `BASELINE-TAMPERED` ("packet.md: digest 047b7d53… does not match the pin 0d8d660b…"), exit 2 — never a silent pass |

Tamper/falsifiability slices on scratch copies (never the committed snapshot):

| # | edit | digest | gate re-run |
|---|---|---|---|
| 9 | `t1.md` = `packet.md` + one appended `<!-- one appended comment line -->` | `d9b80af3…` **≠** pin | exit 0, same `fields=16/16 … findings=0` → only the digest step can see this (§6's calibration case) |
| 10 | `t2.md`: the `canon_standing` line rewritten to a producer-side certification | `5af09f9b…` | exit **1**, `FINDING HO-CANON-CLAIM: FAIL — producer-side canon certification at line 20 …` → the committed `clean` verdict is falsifiable, not vacuous |

Note the division of labour: the battery verifies digests and pins only
(`verdict_replay: "not-run: …the verdict comparison belongs to the baseline's own re-run receipt"`),
so rows 4 and 6 carry the verdict half.

## 3. Root: relocation, dual home, and the round-9 divergence (recorded, not silent)

- Authored 17:49:02 at the standard §3 root `tools/gates/frozen/handoff-packet-check/r9-pre/`;
  relocated byte-verbatim (`mv`, no re-freeze) to
  `reports/round-9/baselines/handoff-packet-check/` after observing the sibling pair protocol;
  then **restored the frozen-root home as a byte-identical copy** once the O15 battery's
  discovery rule was read (`rglob` over `tools/gates/expected/` + `tools/gates/frozen/`; a gate
  missing there reads `BASELINE-GATE-UNCOVERED`).
- The divergence is fleet-wide: `costume-era-consistency-gate` landed at
  `tools/gates/expected/<gate>/r9-pre/`, `lexicon-coverage-audit` at
  `tools/gates/frozen/<gate>/r9-pre/`, while naming/phonology/myth keep files under
  `reports/round-9/baselines/<gate-name>/`. The naming seat's `freeze.txt` recorded
  `handoff-packet-check` at the frozen root before this move.
- Measured consequence, 2026-10-17 (`python3 tools/check-gate-battery.py`, default roots; the
  round is still in flight, so re-run before citing): covered = costume-era, handoff, lexicon,
  phonology, provenance (provenance landed during this shard's run); **uncovered = myth, naming**.
  Claim O's "battery validates every baseline" clause cannot read 7/7 until every gate's baseline
  sits under a scanned root. Reported here for the orchestrator; not absorbed.

## 4. Verifier reproduction recipe (independent re-run)

```bash
cd <lane>                                    # any tree carrying the integration commit
D=tools/gates/frozen/handoff-packet-check/r9-pre          # Home B (or the round-9 home A)
python3 - "$D/expected.json" <<'PY'          # §6 step 1: digests first
import hashlib, json, pathlib, sys
b = pathlib.Path(sys.argv[1]); exp = json.loads(b.read_text())
for rel, want in exp["inputs"].items():
    got = hashlib.sha256((b.parent / rel).read_bytes()).hexdigest()
    print(rel, "OK" if got == want else f"snapshot_tampered {got}")
PY
sha256sum tools/gates/handoff-packet-check.py         # §6 step 2: compare to gate_sha256
python3 tools/gates/handoff-packet-check.py $D/packet.md; echo "exit=$?"   # expect 0, findings=0
python3 tools/check-gate-battery.py                   # §O15: expect this gate's record "pinned"
```

Tamper test for the second seat: copy one home to a scratch tree, append one byte to `packet.md`,
and run the battery with `--baselines-root <scratch-root>`; expect `snapshot_tampered`, exit 2 —
**while the gate itself still exits 0**, so a validator comparing only the verdict calls it a pass.

## 5. What this baseline proves, and what it does not

- Proves: these bytes (`packet.md`), under gate revision `e2fa3223…`, produced exit 0 with an
  empty finding-ID set on 2026-10-17; the digest/pin half is machine-verified by the battery
  (`pinned`) and the tamper half by the drill (`snapshot_tampered`).
- Does **not** prove: that the packet is good design, that its claims are true, that lore accepted
  anything, or that the gate is honest (KTD-FR-S-0007). Lane-local engineering evidence only.
- Class note: `clean` (exit 0) rather than `findings`; the ID-set comparison is still exercised
  because the observed set is `[]`, and rows 9–10 show a real edit moves the verdict.
- `expected.json`: sorted keys, indent 2, final newline, ASCII-only; extra keys beyond §4
  (`baseline_id`, `command`, `input_origin`, `stdout_sha256` is optional in §4) match the sibling
  baselines' shape; the §4 fields a validator reads are all present.
- `revision` names the measured pre-integration tree because this lane forbids worker commits.

## 6. Left undone / integration surface (not this shard's write scope)

1. `tools/gates/frozen/README.md` index row (shared file):
   `r9-pre | handoff-packet-check | a7bb205 | clean (exit 0, findings [])`.
2. `run.log` matches `.gitignore:3` (`*.log`) in either home —
   `git check-ignore -v tools/gates/frozen/handoff-packet-check/r9-pre/run.log` → `.gitignore:3:*.log`.
   Force-add both: `git add -f reports/round-9/baselines/handoff-packet-check/run.log
   tools/gates/frozen/handoff-packet-check/r9-pre/run.log` (otherwise the committed baseline is
   incomplete). A `.gitignore` negation is the orchestrator's call.
3. `SKILL.md` §Gates registry row + `corpus/knowledge/verification/gate-frozen-run-standard.md` §8
   ("not implemented" for the frozen layout) both become stale once the seven baselines land; the
   corpus entry should also name the root the round actually used.
4. The `BASELINE-GATE-UNCOVERED` gates named in §3 (two at the last measurement: myth,
   naming) are an integration blocker for claim O's 7/7 reading; the routing/re-homing decision
   belongs to the orchestrator.
5. The second seat still owes the independent re-run/tamper audit; this fragment claims only the
   author half.
