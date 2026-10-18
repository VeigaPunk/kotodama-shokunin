# R17-D30 — negative: a gloss smuggled onto the sound channel (run receipts)

- round: 17 (loop 2 of 3, build round 1 of 4) · shard: **D30** (negatives ×3,
  claim D `culture-d4-assembly`) · owner: L2 worker, kotodama-shokunin lane
- assignment (verbatim): "D4 R17-D30..D32 (negatives x3): gloss smuggled onto
  sound channel; owed form silently dropped; loan without layer ref — each must
  be caught; reports/round-17/tests/neg-<n>.md."
- date: 2026-10-18. Baseline revision
  `f30b6f8188937632bbedd0e7b29aeefff6f8b07b` (`reports/round-17/claims.json:5`);
  working-tree HEAD `9b49a4a` at write time.
- canon: NON-CANON engineering evidence. Fixtures are synthetic controls derived
  from the filed D2 example; nothing here is a culture design, a canon record, a
  handoff, or a real-world claim.
- writes: **this file only** plus gitignored scratch under `.scratch/r17-d-neg/`
  (`export TMPDIR=$PWD/.scratch` preceded every scratch-writing command). No
  tool, gate, packet, component, projection or earlier-round byte is edited by
  this seat; `reports/round-{8..16}/**` and `tools/gates/{frozen,expected}/**`
  are filed and read-only here. No commit, no push.
- **status: complete — caught.** The smuggled gloss is caught by the gate's
  `L2-channel` leg with a record-addressed line (§3.1), and the raw-packet
  variant by the projector's `D2L-NATIVE` fails (§3.2).

## 1. The hazard, and the catch criterion

The typed pipeline moves a translated label's checked field off the
sound-and-identity channel: `garment` → `garment_gloss`, with one `typed_channel`
routing row per record naming the source field, the off-channel field and the
owed slot (`examples/culture-d2/packet.d2.typed.yml:3324-3424`). The hazard is
the inverse move: the gloss is put **back** on the checked field, so the naming
gate reads an English gloss as a surface form.

Catch criterion (design §6 hazard control 1, `tools/gates/typed-pipeline-gate.py:507`):
the run must exit non-zero **and** a named check must name the off-channel
record. A bare nonzero exit is not a catch.

## 2. Fixtures (scratch, byte-pinned)

| id | fixture (`.scratch/r17-d-neg/…`) | sha256 | injection |
|---|---|---|---|
| 1a | `typed-smuggle-gloss.yml` | `99e780b66355721b7c6207fe18db450f4062ba77bcd9af8a7a8357bb6f278b4e` | first `    garment_gloss: "winter valley coat` → `    garment: "winter valley coat` in the typed packet (the moved gloss restored to the checked field) |
| 1b (raw variant) | `packet-smuggle-gloss-raw.yml` | `3d8b887b9b80eb60182b53016c8b04393e0fdf1d053a92c54b97633a8248c099` | a hand-authored `typed_labels` entry declaring GAR-01's own English gloss `kind: native-form`, `status: supplied`, slot `LEX-GAR-01`, inserted before `costumes:` in the raw packet |

Base bytes: `examples/culture-d2/packet.d2.typed.yml` sha256
`1b5010b7f449ec78755e9a8b0efea62c705af7ec5c592ceda6cf2c072dfac8a3`;
`examples/culture-d2/packet.d2.yml` sha256
`e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643`.
Both fixtures are one byte-range replacement each; generation was a `python3`
heredoc from the lane root with `TMPDIR=$PWD/.scratch` (the exact replacement
strings are the table's injection column, byte for byte).

Tool revisions at every run below: `tools/gates/typed-pipeline-gate.py`
`d102fd1dd1bae3cc4c9d0ea33844b2f706a2098707938c82c75ce9fb6368e27d`;
`tools/d2-typed-labels.py`
`0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802`;
`tools/assemble-d2-typed.py`
`c7e5a7493601d3312f2eb55185ac4d081139cdaa0e11f67dd69f67250b037071`.
Python 3.14.7.

## 3. Receipts

Positive control, same date and revisions: `python3 tools/gates/typed-pipeline-gate.py`
→ exit 0, `summary: 16/16 legs passed` (`.scratch/r17-d-neg/gate-positive.txt`);
`--selftest` → exit 0, `selftest: 12/12 checks passed`
(`.scratch/r17-d-neg/gate-selftest.txt`).

### 3.1 Typed-packet smuggle — caught by `L2-channel`

```sh
python3 tools/gates/typed-pipeline-gate.py .scratch/r17-d-neg/typed-smuggle-gloss.yml
```

counts (that command, 2026-10-18): exit **1**, `summary: 12/13 legs passed`
(`run-typed-smuggle-gloss.txt:32`). The failing leg, verbatim (`:22`):

```text
FAIL L2-channel — off-channel lines in the typed run: ["naming-collision-gate.py: FINDING PHON-INVENTORY: FAIL — name GAR-01 'winter valley coat (heavy felted wool; uncombed finish optional)': symbol /v/ at position 7 is not in the declared inventory (consonants {p, t, k, b, d, g, m, n, s, ʃ, r, l, j, w, h}, vowels {a, e, i, o, u})"]
```

The catch names both the gate (`naming-collision-gate.py`) and the record
(`GAR-01`) — record-addressed, not a bare exit. Corroborating line (`:18`):
`channel: 9 PHON artifact(s) retired, 0 added, retained lines identical` against
10 routed records: one retirement was lost, and that lost one is the smuggled
record. The `L2-channel` check is the leg that requires
`removed_total == len(off_records)` **and** zero off-channel lines
(`tools/gates/typed-pipeline-gate.py:288`).

### 3.2 Raw-packet variant — caught by the projector

```sh
python3 tools/d2-typed-labels.py --packet .scratch/r17-d-neg/packet-smuggle-gloss-raw.yml --json
```

counts (that command, 2026-10-18): exit **1**, `stats {fail: 2, hold: 14,
labels: 59, note: 1}` (`run-packet-smuggle-gloss-raw.json`). Two `D2L-NATIVE`
fails name the smuggled record (the R4 pair rule and the record's own pass,
`tools/d2-typed-labels.py:668`):

```text
D2L-NATIVE fail NEG-SMUGGLE-01 — supplied form 'winter valley coat (heavy felted wool; uncombed finish optional)' carries symbols outside the declared inventory: ['(', ')', ';', 'c', 'f', 'v', …]
```

The live control projection (`examples/culture-d2/packet.d2.yml`, no injection)
reports `stats {fail: 0, hold: 15, labels: 58, note: 1}`
(`.scratch/r17-d-neg/proj-live.json`) — the two fails are the injection's.

Boundary note (reported, not absorbed): handing the same raw fixture to the gate
gives exit **2**, `FAIL L1-assembler_identity — packet bytes are not
assemble-d2.py's deterministic assembly (3d8b887b9b80 vs e0f21509e14a)`
(`run-gate-smuggle-raw.txt:1-2`). The adapter refuses a packet that is not the
deterministic assembly before the channel leg runs, so the end-to-end injection
point for the raw channel is the **components**, not the packet bytes. For D4
this seat's typed-packet injection (§3.1) is the channel-leg control; a
component-level injection belongs to D4's own build tests.

## 4. Sweep

Every run of this shard is recorded under `.scratch/r17-d-neg/`; the sweep is
`ls .scratch/r17-d-neg/run-*` plus the two control receipts (2026-10-18).
Exits observed: positive 0, selftest 0, 1a **1**, 1b projector **1**, 1b gate
**2**; no smuggled variant exited 0, and no run produced a traceback.

## 5. D4 re-point (to-verify at write time)

D4's design contracts landed during this shard
(`reports/round-17/d4/typed-support-1.md` §5.3-5.6,
`typed-support-2.md` §2-3); state at last poll (2026-10-18 09:32Z):
`tools/assemble-culture-d4.py` has landed (its `assemble()` is the identity leg
the D4 adapter must call, per `typed-support-1.md` §5.2), while
`examples/culture-d4/` is still absent (components drafting under
`reports/round-17/d4/components/`, 3/12 at that stamp). Re-point recipe when D4
lands:

1. apply the same single byte-run injection to D4's typed packet
   (`examples/culture-d4/packet.d4.typed.yml`) — restore the first
   `<field>_gloss` value to `<field>` (the routing row's `off_channel_field`
   names the pair; the row's hold is `D4L-FORM-UNRESOLVED`,
   `typed-support-1.md` §5.3);
2. run the D4 gate over the tampered packet;
3. caught = nonzero exit **and** a channel check naming the record. If D4's gate
   names the check differently (`L2-channel` here), the record-addressed line is
   the criterion, not the check id. The D4 gate must print holds verbatim and
   compare the set exactly (`typed-support-1.md` §5.4), so a restored gloss
   cannot pass silently.

This is `to-verify` — the catch mechanism is shared (`typed-pipeline-gate.py`
grading, `L2-channel` at `:288`), but it has not been re-run over D4 bytes by
this seat.

The D4-specific control battery is separate (`reports/round-17/d4/design-brief.md`
§8, C-01..C-10 — e.g. C-09, "gloss re-typed as native"); this file is the
pipeline-level analog of that class and does not discharge it.

## 6. Sources

- `tools/gates/typed-pipeline-gate.py` `d102fd1d…` — `L2-channel` (`:217-292`),
  hazard control 1 (`:507-518`), selftest
- `tools/d2-typed-labels.py` `0da0015f…` — `check_sound_form` (`:668`),
  `validate_labels` (`:733`)
- `examples/culture-d2/packet.d2.typed.yml` `1b5010b7…` (`typed_channel`
  `:3324-3424`); `examples/culture-d2/packet.d2.yml` `e0f21509…`
- receipts: `.scratch/r17-d-neg/gate-positive.txt`, `gate-selftest.txt`,
  `run-typed-smuggle-gloss.txt`, `run-packet-smuggle-gloss-raw.json`,
  `run-gate-smuggle-raw.txt`, `proj-live.json`
- `reports/round-11/depth/neg-17.md` (R11-D17, the same hazard on the round-11
  wiring — read as the prior art; this file re-runs it on the landed gate)
