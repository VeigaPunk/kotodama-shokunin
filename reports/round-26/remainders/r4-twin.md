# R26-O29..O32 — the declared-in-r4 twin gap, dispositioned

- **Seat:** O, round-26 claims R26-O29..O32 (r4 twin x4). This seat authored
  none of the lane's filed round 8–25 artifacts.
- **Date:** 2026-10-18. Declared baseline `fc13cd27b9e78d5d7c4f70740fd26c9383a7447b`
  (`reports/round-26/claims.json:5`); lane HEAD at seat work `1ad491a`.
- **Writes:** `reports/round-26/remainders/r4-twin/` only (`build-twin.py`,
  `verify-twin.py`, `twin.json`, `expected.json`, `freeze.txt`, this file).
  No git commit or push. No filed round 8–25 byte written. Scratch under
  `.scratch/r26-o29*` with `TMPDIR=$PWD/.scratch`.
- **Disposition: RESOLVED** — the twin is generated from the packet, frozen, and
  the r4 checker is green. `verify-twin.py --check` exits 0 at **24/24 controls**.

## 1. The remainder, measured

Round 25 left the v3 revision `reports/round-25/v3-supersession/declared-in-r4/`
**packet-only**. On the live bytes that directory holds exactly three files:

| path | sha256 | bytes |
|---|---|---|
| `declared-in-r4/packet.md` | `5f58db4a52b688568eac054b1c75e9bd110843370a1943cf4353fff75b46aa03` | 109,817 |
| `declared-in-r4/expected.json` | `c2d4eb7af2b9807afa9cae4720448144bcefa4bb0c678500bf8d6c41c660b093` | — |
| `declared-in-r4/freeze.txt` | — | — |

There is **no `twin.json`**, unlike both r22 siblings
(`reports/round-22/handoff/declared-in/twin.json` and
`.../declared-in-r2/twin.json`, each 103,155 bytes). The round-25 X48 shard
audit filed exactly this gap (`reports/round-25/audit/x48-v3-supersession.md`
§"The successor lands packet-only, with no companion `twin.json`"), and the
round-25 runner recorded it as the O claim's one short leg
(`reports/round-25/rerun.json:189`: "carries packet.md … but NO twin.json").
The corrected prose is on disk and verified; the revision's **ledger surface**
stays unauditable without the twin.

## 2. What the twin is, and why it is generated rather than authored

The twin is not a new artifact kind. It is exactly what
`tools/exercise-handoff-e2e.py`'s `v3_build_twin` (line 2621) emits at assembly
time — a projection of the packet's three Markdown tables
(`artifact_manifest`, `claim_ledger`, `coupling_edges`), the `open_questions`
passenger list, and the four `record_ids` indexes the edges and the harness
resolve against. `build-twin.py` performs that same projection on the filed
packet bytes and mines the indexes with the renderer's **own**
`v3_mine_d2` / `v3_mine_d3` / `v3_mine_d4` (imported read-only), so no
projection rule is re-implemented here.

`--selftest` is **12/12**, and the load-bearing control is:

| filed twin | declared sha256 | rebuilt | byte-identical |
|---|---|---|---|
| `reports/round-20/handoff/twin.json` | `58cb246081e03e351dc35c4c13ae7961ee9e046e569f0cc7081d76813de88628` | same | **yes** |
| `reports/round-22/handoff/declared-in-r2/twin.json` | `d3de56a8be1d28fdcead751aa0ac9364f7b43ff2b8bad71b696f0b57955b4d5c` | same | **yes** |

The r20 twin is the 3.0.0 shape (no `declared_in` edge column); the projection is
header-adaptive, so one code path renders both. Reproducing two filed twins
byte-for-byte is what makes the projection the renderer's, not this seat's
invention.

## 3. The twin, frozen

`build-twin.py --emit` wrote
`reports/round-26/remainders/r4-twin/twin.json` — **103,975 bytes**, sha256
**`1874efbc1a6f892d035e47bbfbb8ca228622b26fd622a002ee822594a5420b95`**,
from the 109,817-byte packet.

| field | value |
|---|---|
| `packet_id` | `kotodama.handoff.d2d3d4-e2e` |
| `packet_version` | `3.1.1` |
| `profile` | `kotodama-handoff-e2e/3` |
| `artifact_manifest` | 58 rows (the inline `§glossary` row is excluded, as in the filed twins) |
| `claim_ledger` | 27 rows |
| `coupling_edges` | 88 rows |
| `open_questions` | 10 rows |

`expected.json` pins that digest in the `twin_sha256` key — the same binding
mechanism as `reports/round-22/handoff/declared-in-r2/expected.json`, which
carries `twin_sha256: d3de56a8…`. The twin is written as a **new row** under
`reports/round-26/`; the filed round-25 directory is not written.

### 3.1 The read-set guard (why the twin is pinned to the packet, not the tree)

The record index is mined from four source packets. A concurrent round-26 D seat
was rewriting `examples/culture-d4/**` while this twin was built — measured:
live `examples/culture-d4/packet.d4.yml` = `dd25077bc01681bc…` against the
packet's own pinned `e7ecd2045ef0e5f9…`. So `build-twin.py` digest-checks each
source against the target packet's `artifact_manifest` rows **before** mining,
and refuses on mismatch:

```
$ python3 reports/round-26/remainders/r4-twin/build-twin.py --stdout
build-twin: source examples/culture-d4/packet.d4.yml is dd25077bc01681bc… but the
packet pins A-28 at e7ecd2045ef0e5f9… — pass --source-root at the pinned read set
```

Passed the pinned clone, the twin is byte-identical (`1874efbc…`). The twin is
therefore a pure function of the packet's declared read set, not of whatever the
live tree holds at build time. The four pinned digests — `A-02`
`bdf635ceaed4eb2f…`, `A-10` `e0f21509e14ac03e…`, `A-16` `1b9b16710ae12818…`,
`A-28` `e7ecd2045ef0e5f9…` — are carried unchanged from r20 through r22 to r4.

## 4. Content controls

- **The corrected rows are in the twin.** `D4-CL05`, `D4-CL06`, `D4-CL07`,
  `D4-CL09` all differ from the r22 predecessor twin and carry the family-clean
  present state (`findings_total 12`, `hold 12, note 0, fail 0`, zero conflicts
  and quarantine handles, zero unresolved rank items).
- **`OQ-V3-05` is corrected.** It reads "twelve form holds, zero rank holds,
  zero notes and zero fails" and names the D2-owned residuals (`OQ-V2-03`).
- **The stale-prose detector agrees.** The filed r25 checker's own `stale_hits`
  returns **0** hits on this twin and fires on all five rows
  (`D4-CL05/06/07/09`, `OQ-V3-05`) on the r22 predecessor twin. The detector is
  imported read-only, not re-implemented: a naive token scan would falsely flag
  D2-CL01's legitimate live "findings_total 16 with 15 hold-or-fail" and the
  corrected rows' honest negation ("zero `D2L-RANK` rows of either severity").
- **The 15 carried v2 rows are byte-identical** to the r22 predecessor's.

## 5. Evidence (commands + date)

All commands ran **2026-10-18** from the lane root with
`export TMPDIR="$PWD/.scratch"` and `PYTHONDONTWRITEBYTECODE=1`.

### 5.1 The checker

- `python3 reports/round-26/remainders/r4-twin/verify-twin.py --root .scratch/r26-o29-vc
  --source-root .scratch/r26-o29-clone --selftest` → exit 0, **22/22** controls.
- `… --root .scratch/r26-o29-vc --frozen-root .scratch/r26-o29-frozen
  --source-root .scratch/r26-o29-clone --check` → exit 0, **24/24** controls.
  Receipts `.scratch/r26-o29/{selftest,check}-receipt.json`.

The `--check` controls, in full: packet digest pin; twin pin vs live bytes; twin
pins its source packet; clone-matches-live for the builder, twin, baseline and
packet; twin re-derived from the packet; the two filed-twin reproductions; shape
3.1.1; census 58/27/88/10; no inline glossary row; the corrected D4 rows; the
corrected OQ passenger; clean under the filed stale detector; the detector fires
on the r22 predecessor; the 15 v2 rows verbatim; the frozen uncertainty judge;
the frozen links judge; the filed r25 r4 directory untouched; the twin is a new
row not an r25 write; the frozen r25 r4 checker green; the frozen r23 wording
checker unaffected.

### 5.2 Frozen verify (the "r4 checker green" clause)

`python3 reports/round-25/v3-supersession/v3-supersession-check.py --root
.scratch/r26-o29-frozen --check` (clone at the round-24 admit `e06581b`, the
revision's own declared baseline) → exit 0, `passed: true`, **52/52 controls**.
Its two declared open tails are the v2 successor row's projector re-pin and the
v3 baseline pin re-point — both sibling pins it does not own.

`python3 reports/round-23/wording/wording-check.py --root .scratch/r26-o29-frozen
--check` → exit 0, `passed: true`, **17/17 controls**.

### 5.3 The frozen harness judges (run on the twin)

- `tools/harness/packet_uncertainty.py --packet <twin> --require-oq` → exit 0,
  claims 27, findings `[]`.
- `tools/harness/packet_links.py --packet <twin> --repo-root <pinned clone>` →
  exit 0, **106/106** links resolved, findings `[]`.

### 5.4 Filed-byte preservation

`git diff --name-status fc13cd2 HEAD -- reports/round-{8..25}` prints nothing;
`git status --porcelain -- reports/round-25/` is empty. The round-25 r4
directory is byte-identical to how this seat found it, and the checker asserts
that directly (`filed-r25-r4-directory-untouched`).

## 6. An inherited tail surfaced, not owned

The frozen r25 r4 checker is green (52/52) at its **own declared baseline** and
**51/52** on the live round-26 tree, where a **third** inherited tail appears:

```
claim O: D4 gate legs summary: 20/20 legs passed != 19/19
```

The round-25 argot leg (added at `fc13cd2`) made the D4 typed-pipeline gate
report 20 legs while the frozen round-20 runner pins 19
(`reports/round-20/run-validation.py:1119`). This is the D seat's argot-leg work
— measured 20/20 at both `fc13cd2` and the live tree — not this seat's twin, and
this seat neither owns nor claims it. The checker's `--frozen-root` exists
precisely so its verdict is read against the state the revision pins, and the
third tail is reported here rather than hidden.

## 7. What this seat did not do

- No round-8–25 artifact was edited; the filed round-25 r4 directory stays
  packet-only on disk (the twin is a new round-26 row).
- No renderer, profile, frozen row, `SKILL.md`, or shared bookkeeping was
  changed. The `tools/exercise-handoff-e2e.py` renderer still emits 3.1.1 and
  its v3 baseline is untouched.
- The three round-25 remainders are dispositioned by *other* seats (the two pin
  tails) and by this one (the twin gap). The sibling pin tails remain open and
  are not waived here.

## Read-only replay

```bash
export TMPDIR="$PWD/.scratch"
# clones at the packet's pinned read set and at the revision's own baseline
git clone -q . .scratch/r26-o29-clone          # HEAD (carries the pinned read set)
git clone -q . .scratch/r26-o29-frozen && (cd .scratch/r26-o29-frozen && git checkout -q e06581b)
python3 reports/round-26/remainders/r4-twin/build-twin.py --selftest --source-root .scratch/r26-o29-clone
python3 reports/round-26/remainders/r4-twin/verify-twin.py --root .scratch/r26-o29-clone \
  --frozen-root .scratch/r26-o29-frozen --source-root .scratch/r26-o29-clone --check
```

Assertions: the builder selftest is 12/12 and both filed twins reproduce
byte-identically; the checker `--check` is 24/24 with `passed: true`.
