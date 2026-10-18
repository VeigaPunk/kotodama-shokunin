# R18-D10 — replay: the round-18 frozen manifest

- round 18, shard **D10** (claim **D**, determinism + replay x4). Seat header,
  date, baseline, canon and write scope are shared with
  `reports/round-18/d4/determinism.md`; measurements 10:21–10:41Z 2026-10-18.
- verified deliverable: `tools/gates/frozen/round-18/MANIFEST.tsv` under
  `tools/replay-frozen.py` (`a2fb5c98260a07f0…`, unchanged since round 11).

## 0. Verdict

**REPLAY OK: 2/2 rows reproduced the recorded verdicts** — the two D4 check legs
(projection check, assembly check) reproduce byte-for-byte, and the generation
replays green with the gate under revision. The gate-pinned D4 typed-packet row
is not in the manifest yet (its input does not exist; `manifest.md` §1) so it
cannot go red either.

## 1. The replay command

`tools/replay-frozen.py` refuses an in-repo mirror root by design, so the replay
subprocess — and only it — runs with `TMPDIR` outside the repository (the lane's
usual `TMPDIR=$PWD/.scratch` cannot be used here; the round-11 README records the
same constraint):

```sh
mkdir -p /var/tmp/kotodama-r18
TMPDIR=/var/tmp/kotodama-r18 python3 tools/replay-frozen.py \
  tools/gates/frozen/round-18/MANIFEST.tsv
```

Observed (2026-10-18 10:41Z, lane root):

```
ROW 2 reproduced reason=- gate=tools/gates/d4-typed-labels-check-gate.py input=examples/culture-d4/typed-labels.d4.yml exit=0/0 count=0/0 bytes=match launched=yes
ROW 3 reproduced reason=- gate=tools/gates/d4-assembly-check-gate.py input=examples/culture-d4/packet.d4.yml exit=0/0 count=0/0 bytes=match launched=yes
REPLAY OK: 2/2 rows reproduced the recorded verdicts (reproduction only: a reproduced red verdict stays red)
```

## 2. What the replay asserts, and what it does not

- **Asserts**, per row and before any gate runs: the gate is a Python file
  directly under `tools/gates/`; the live gate bytes hash to the pinned
  `gate_sha256`; the input snapshot hashes to the pinned `input_sha256`; the
  recorded output hashes to the pinned `output_sha256` and carries exactly
  `finding_count` `FINDING` lines. Then the pinned gate runs over a private copy
  of the snapshot (temporary mirror, row's own relative input path, cwd = mirror)
  and the observed exit code, finding count and stdout bytes must equal the record.
- **Does not**: read or execute the `command` column (documentation only), judge
  whether a recorded verdict *should* be green, or touch the repository (the mirror
  is a self-cleaning temporary directory).

## 3. Earlier generations: what the generalization did to their pins

Measured 2026-10-18:

| generation | before the generalization (10:21Z) | after it (morning of the same wave) |
|---|---|---|
| `tools/gates/frozen/round-11/MANIFEST.tsv` | `REPLAY OK: 11/11` | `ROW 2 could-not-evaluate reason=gate_digest_mismatch gate=tools/gates/typed-pipeline-gate.py`, exit 2, the other 10 rows still reproduce |
| `tools/gates/frozen/round-18/repin-d2/MANIFEST.tsv` (O07-O10) | — | its typed row reads `gate_digest_mismatch` too: it pinned gate `ea95e2a1`, the live gate had moved to `68e4835a` when this shard measured |

Both readings are the historical-pin class the round-17 scope watch recorded
(r17 F-X02-3): a filed row pins the gate *bytes*, so a later gate revision
supersedes its row rather than reproducing it. Per the append-only rule neither
filed generation is edited; the re-pin is a new record
(`tools/gates/frozen/round-18/repin-d2/**` for the full 11-row cascade, and the
validator's own frozen-row leg, `reports/round-18/run-validation.py:542`).
`reports/round-18/run-validation.py:884-893` requires every round-18 manifest to
replay green, which is why this generation's manifest deliberately pins no gate
revision while the gate is still being revised (`manifest.md` §4).

## 4. Limits

- A green replay is a reproduction statement about pinned NON-CANON bytes, not a
  clearance, not a design verdict, and not a statement about any later revision of
  any pinned file.
- The two recorded rows read live peer files beside the frozen input (the packet,
  projection, components, assembler, projector); the pins in `freeze-receipt.json`
  name them, and a later edit there turns the affected row red by design.
- Row counts: the generation records 2 rows and carries 1 pending row; "2/2" is a
  statement about the recorded rows only.
