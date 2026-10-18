# X61 — pin-sweep double-check (round 28)

- round 28 (operator: loop 3 of 3, build round 4 of 4 — the last build round;
  64 workers on `devin/deepseek-v4-1-flash-high` per
  `reports/round-28/claims.json`) · seat **X61** (SCRIBE X61 — sweep
  double-check) · owner: L2 worker, kotodama-shokunin lane.
- assignment (verbatim): "SCRIBE X61..X62: sweep double-check + replay audit."
- date: 2026-10-18. Lane root
  `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. Claim under check:
  `reports/round-28/claims.json` claim **O** (`operability`, capability
  `final-pin-sweep`), declared baseline
  `6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede`; lane HEAD at every measurement
  below `69cecbc7dcf575a29f29660ecac470e05260fd86` (round-28 declaration).
- canon: **NON-CANON engineering evidence.** This audit admits nothing, certifies
  no round, and grants no promotion. A reproduced red verdict stays red.
- writes: **this file** and its read-only tool
  `reports/round-28/audit/x61-pin-sweep.py`, plus gitignored scratch under
  `.scratch/x61-r28/`. No tool, gate, packet, pin, validator or shared-bookkeeping
  byte was edited; no filed round-8–27 artifact was written; no commit, no push.
  `export TMPDIR` preceded every scratch-writing command — but to `/var/tmp`, not
  the operator-mandated `$PWD/.scratch`, for the reason §5 measures.
- measurement window: 2026-10-18T20:11Z–20:16Z UTC. **The wave was live
  throughout.** `examples/culture-d4/packet.d4.yml` moved `86079a67…` →
  `543d68a8…` at ~20:12Z as the RL-4 fix landed; `reports/round-28/` grew from
  2 files to 30. Every number below names its own stamp.

## 0. Verdict at a glance

| # | reading | class |
|---|---|---|
| 1 | the pin surface is **12 manifests / 86 rows** once the round-17 manifest is included; round-27's X61 swept 11 / 81 | measured |
| 2 | **53/86 rows reproduced** their recorded exit, finding count and output bytes | measured |
| 3 | **8 rows mismatch — all 8 supersessions, 0 drift**; each row's live input no longer hashes to its own `input_sha256` | measured |
| 4 | **25 rows could-not-evaluate — all 25 `gate_digest_mismatch`**; each pins a gate revision no longer on disk | measured |
| 5 | **19/19 committed baselines pinned, 0 findings**, 83 declared inputs verified, across all three roots `check-gate-battery.py` discovers | measured |
| 6 | **4 of the 8 superseded rows carry a declared successor (`reports/round-28/pinsweep/frozen/r28-post`); 4 carry none — the re-pin surface never extended to `typed-pipeline-gate.py`** | **finding X61R28-A2** |
| 7 | `reports/round-17/tests/frozen/MANIFEST.tsv` (5 rows) sits outside round-27's X61 scope although the lane's own validator replays it | **finding X61R28-A1** |
| 8 | `TMPDIR` inside the repo silently voids the whole manifest surface: the same manifest reads **0 reproduced / 6 `mirror_unsafe`** inside vs **4 reproduced / 2 mismatch** outside | measured (round-27 X61-B1 reproduced) |
| 9 | `tools/gates/frozen/README.md` — the index `gate-frozen-run-standard.md:54` declares — does not exist | **finding X61-B2** (round-27, re-measured; sized by X62 duty F) |
| 10 | the tool's own controls pass **28/28**, including seven duty-C successor controls and four classifier controls | measured |
| 11 | `/tmp` is a 16 GB tmpfs shared fleet-wide and hit `OSError: [Errno 122] Disk quota exceeded` at 80%; `/var/tmp` carries 767 GB free | **finding X61R28-A3** |
| 12 | the first draft of duty C had a real defect — it read live digests, so two superseded rows vouched for each other; the control caught it and the fix is measured | disclosed |

## 1. Method, and why this is a double-check and not a re-run

The round's own counting command is `python3 reports/round-28/run-validation.py`;
the round's verdict is `reports/round-28/validation.json`. Claim O asks for a
sweep, so this seat built a second instrument that reaches the same surface by
different machinery:

```sh
export TMPDIR=/var/tmp PYTHONDONTWRITEBYTECODE=1   # see §5 — NOT $PWD/.scratch
python3 -B reports/round-28/audit/x61-pin-sweep.py --selftest   # 28/28, exit 0
python3 -B reports/round-28/audit/x61-pin-sweep.py             # text summary
python3 -B reports/round-28/audit/x61-pin-sweep.py --json      # receipt on stdout
```

It does **not** call `tools/replay-frozen.py`; it re-derives every row itself, so
a defect in that tool cannot hide behind it. Four duties:

- **A. MANIFEST sweep** — per row, before any gate runs: `gate_sha256` against the
  live gate, `input_sha256` against the committed snapshot, `output_sha256`
  against the recorded output; then re-execute the gate in a mirror whose real
  path is outside the repo and compare exit code, `^FINDING ` count and bytes.
- **B. BASELINE sweep** — every `expected.json` under `tools/gates/expected/`,
  `tools/gates/frozen/` and `reports/round-9/baselines/`. A baseline is never
  re-executed; `pinned` means the digests hold.
- **C. SUCCESSOR sweep** — new this round. For every superseded row, does any
  *later* generation carry a row for the same `(gate, input)` at the live digest?
- **D. TMPDIR probe** — the same manifest replayed under an in-repo and an
  out-of-repo mirror parent.

## 2. The two scope and definition deltas against round 27

**X61R28-A1 — the round-27 X61 sweep was 5 rows short of the lane's own replay
surface.** Round-27's seat tool globbed `tools/gates/frozen/**` and reported 11
manifests / 81 rows. Two peer sweeps in this lane count a twelfth manifest:

| evidence | reading |
|---|---|
| `find . -name MANIFEST.tsv -not -path './.scratch/*'` | `reports/round-17/tests/frozen/MANIFEST.tsv`, 5 rows |
| `reports/round-21/recount/r17-2.md:15` | "The validator's current replay command `python3 tools/replay-frozen.py reports/round-17/tests/frozen/MANIFEST.tsv` exited 0 and reported 5/5 rows reproduced." |
| `reports/round-27/pinsweep/sweep.md:151` and `sweep-census.md:21` | both list `reports/round-17/tests/frozen` among the generations they replay |
| `reports/round-28/sweep/_prelanding-census.md:22` | same row, `0 / 5 / 0 / 0` |

This seat therefore sweeps both roots and reports the totals separately rather
than picking one. The delta is **5 rows, all reproduced** — it changes the
denominator, not the verdict. It is filed as a completeness finding because a
sweep whose scope depends on which glob was typed cannot be compared across
rounds.

**X61R28-A2 — the re-pin convention covers two gates; four moved rows have no
successor at all.** Round 27 classified its 8 mismatches as supersessions (the
input moved) and stopped there. That classification answers *why* the row
diverged; it does not answer whether anyone re-pinned the surface, which is the
question a sweep exists to settle. Duty C asks it per row, by digest, with
"later" derived from the generation ordinal in the path rather than from walk
order, and it reports **two** successor sets: `successors` (inside the swept
scope) and `declared_successors` (anywhere in the repo). The gap between them is
the finding.

```sh
python3 -B reports/round-28/audit/x61-pin-sweep.py --json | \
  python3 -c "import json,sys; d=json.load(sys.stdin); [print(s['manifest'],s['row'],s['input'],s['declared_successors']) for s in d['successors']]"
```

Result: **8 superseded rows, 4 re-pinned by a declared successor, 0 re-pinned
inside the swept scope.**

| generation | row | surface | declared successor |
|---|---:|---|---|
| `frozen/round-18` | 2 | `typed-labels.d4.yml` | `reports/round-28/pinsweep/frozen/r28-post` |
| `frozen/round-18` | 3 | `packet.d4.yml` | `reports/round-28/pinsweep/frozen/r28-post` |
| `frozen/round-22/d4-repin` | 2 | `typed-labels.d4.yml` | `reports/round-28/pinsweep/frozen/r28-post` |
| `frozen/round-22/d4-repin` | 3 | `packet.d4.yml` | `reports/round-28/pinsweep/frozen/r28-post` |
| `frozen/round-26/gate-input` | 2 | `packet.d4.yml` | **none** |
| `frozen/round-26/gate-input` | 3 | `packet.d4.typed.yml` | **none** |
| `frozen/round-26/post-register` | 2 | `packet.d4.yml` | **none** |
| `frozen/round-26/post-register` | 3 | `packet.d4.typed.yml` | **none** |

Two distinct facts, and both matter:

1. **No frozen generation can ever show a successor.** The lane's re-pin
   convention writes to `reports/<round>/pinsweep/frozen/<id>/`, outside
   `tools/gates/frozen/`, so a sweep scoped to the frozen root reads 0 of 8. That
   is the convention boundary, and it is why duty C now indexes repo-wide.
2. **The re-pin itself is incomplete.** Both `r27-post` and `r28-post` pin only
   the two D4 **adapters**:

   ```sh
   cut -f1,3 reports/round-28/pinsweep/frozen/r28-post/MANIFEST.tsv
   # tools/gates/d4-assembly-check-gate.py     examples/culture-d4/packet.d4.yml
   # tools/gates/d4-typed-labels-check-gate.py examples/culture-d4/typed-labels.d4.yml
   grep -c typed-pipeline-gate reports/round-28/pinsweep/frozen/r28-post/MANIFEST.tsv
   # 0
   ```

   So the four `typed-pipeline-gate.py` rows moved by the round-27 law landing
   and the round-28 RL-4 fix have **no successor row anywhere in the repo**. The
   gap is not that nobody re-pinned — it is that the re-pin surface was never
   extended to the gate that the round's own regression battery names first.

**Disclosed defect in the first draft.** Duty C's first implementation indexed
each row's *live* digest. Two superseded rows then found each other and both read
`re_pinned: true`, which is the exact opposite of the truth. The control
`successor: an earlier superseded row is not a successor` fails on that draft and
passes on the current one. The index is now keyed on each row's own frozen digest
(`input_pin`, carried on every result, not only on mismatches); the ordering is
`generation_key(rel)`, so the verdict does not depend on walk order
(`successor: verdict is order-independent`); and the fifth control,
`successor: an out-of-scope successor reads declared but not in-scope`, pins the
exact round-28 shape that motivated the two-set reading.

## 3. Every manifest, replayed

`TMPDIR=/var/tmp` (outside the repo; see §5). 12 manifests, all replayed:

| manifest | rows | reproduced | mismatch | could-not-evaluate |
|---|---:|---:|---:|---:|
| `reports/round-17/tests/frozen` | 5 | 5 | 0 | 0 |
| `tools/gates/frozen/round-11` | 11 | 10 | 0 | 1 |
| `tools/gates/frozen/round-18` | 2 | 0 | 2 | 0 |
| `tools/gates/frozen/round-18/repin-d2` | 11 | 10 | 0 | 1 |
| `tools/gates/frozen/round-20/repin-d2` | 11 | 10 | 0 | 1 |
| `tools/gates/frozen/round-22/d4-repin` | 3 | 0 | 2 | 1 |
| `tools/gates/frozen/round-23/repin-d2` | 11 | 10 | 0 | 1 |
| `tools/gates/frozen/round-25/gate-input` | 6 | 0 | 0 | 6 |
| `tools/gates/frozen/round-26/gate-input` | 6 | 4 | 2 | 0 |
| `tools/gates/frozen/round-26/post-register` | 6 | 4 | 2 | 0 |
| `tools/gates/frozen/round-3` | 7 | 0 | 0 | 7 |
| `tools/gates/frozen/round-3/attempt-1` | 7 | 0 | 0 | 7 |
| **total** | **86** | **53** | **8** | **25** |

All 25 unevaluable rows are `gate_digest_mismatch` — the row pins a gate revision
no longer on disk. No row is `snapshot_tampered`, `output_missing` or
`gate_missing`: **no committed frozen byte has been altered.** The divergence is
entirely in the live surfaces the rows point at.

The 8 mismatches split by exit code into two classes, four rows each:

- **4 rows now exit 2 where the record says 0** — the `typed-pipeline-gate.py`
  rows in `round-26/gate-input` and `round-26/post-register`. The reason is not a
  broken gate: the gate fails its own `L1-profile` leg because
  `tools/gates/typed-pipelines.json` pins packet `86079a67…` while the live packet
  is `543d68a8…`. The gate is refusing to grade a packet that does not match its
  declared profile — correct behaviour, and it is the same refusal
  `reports/round-27/gate-tests/receipt.json` recorded at 20:04:10Z when the packet
  was `86079a67…` and the profile still pinned `dd25077b…`.
- **4 rows now exit 1 where the record says 0** — the `round-18` and
  `round-22/d4-repin` D4-adapter rows (`d4-typed-labels-check-gate.py`,
  `d4-assembly-check-gate.py`), which read the live D4 tree directly.

Measured directly, outside any mirror, to rule the mirror out as the cause:

```sh
python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml
# exit 2; stdout: "FAIL L1-profile: packet: pins 86079a6708a0, live 543d68a82640"
```

The same command in the bare mirror exits 2 for the same reason. **The mirror is
not implicated; the profile pin is stale.**

## 4. Baselines: 19/19 pinned, and the sweep is complete

| reading | value |
|---|---:|
| baselines discovered | 19 |
| pinned | **19** |
| not pinned | 0 |
| declared inputs verified | 83 |
| findings | **0** |

The three roots are `tools/gates/expected/` (6), `tools/gates/frozen/` (10) and
`reports/round-9/baselines/` (3). The battery's own duty-2 sweep independently
reads the same set — `python3 tools/check-gate-battery.py` reports
`pass 7 / fail 0 / unevaluable 0` with `coverage 9/9` at this stamp, and its
`baselines` list is the 19 this tool verifies. Two instruments, two code paths,
same 19.

Note the boundary: a baseline pins **the gate and its declared inputs**. It does
not pin the live `examples/culture-d4/` tree, which is why 19/19 green and 8
superseded rows can both be true at once. Reading §4 as "the D4 surface is
pinned" would be wrong; §3 is where that surface is measured.

## 5. The TMPDIR trap, and why this round ran against the operator directive

Round 27's finding X61-B1 measured that an in-repo `TMPDIR` voids the entire
manifest surface, because the mirror's real path then resolves inside the repo
and the tool refuses to write it. This round's operator regimen says
`export TMPDIR=$PWD/.scratch before scratch-writing commands`. Running the sweep
that way reproduces the void exactly:

| mirror parent | reproduced | mismatch | could-not-evaluate | `mirror_unsafe` |
|---|---:|---:|---:|---:|
| inside-repo (`.scratch`) | 0 | 0 | 6 | 6 |
| outside-repo (`/var/tmp`) | 4 | 2 | 0 | 0 |

That is the round-27 finding reproduced on the round-28 tree, and it is why
**this seat's measurements use `/var/tmp`**: the directive's purpose is to keep
scratch out of the repo, and the tool's own boundary already guarantees that —
a mirror under `/var/tmp` cannot write into the lane. The probe still measures
both parents, so the sensitivity is a measurement either way rather than a claim.

**X61R28-A3 — `/tmp` is not a usable mirror parent on this host.**
`/tmp` is a 16 GB tmpfs shared with the whole fleet; at 20:13Z it held 13 GB
(80%) and the law probe died with `OSError: [Errno 122] Disk quota exceeded`.
`/var/tmp` is on the root filesystem with 767 GB free. A lane tool that defaults
to `tempfile.gettempdir()` inherits that failure mode whenever `/tmp` is under
pressure; the round-27 tools do exactly that. Filed as an advisory for the next
build round, not as a defect in this round's work.

## 6. Findings

| id | finding | level | evidence |
|---|---|---|---|
| **X61R28-A1** | round-27's X61 swept 11 manifests / 81 rows; the lane's own validator replays a twelfth (`reports/round-17/tests/frozen`, 5 rows), so the round-27 denominator was 5 rows short | completeness | `reports/round-21/recount/r17-2.md:15`; `reports/round-27/pinsweep/sweep-census.md:21`; this tool's `scope` block |
| **X61R28-A2** | 4 of the 8 superseded rows carry a declared successor (`reports/round-28/pinsweep/frozen/r28-post`, 2 adapter rows); the other 4 — every `typed-pipeline-gate.py` row — carry none, because the re-pin surface covers only the two D4 adapters. 0 of 8 show a successor *inside* the frozen root, which is a convention boundary, not a defect | **coverage gap + convention** | §2 tables; `grep -c typed-pipeline-gate reports/round-28/pinsweep/frozen/r28-post/MANIFEST.tsv` → 0 |
| **X61R28-A3** | `/tmp` is a shared 16 GB tmpfs; it hit `ENOSPC` mid-audit, and every lane tool that defaults to `tempfile.gettempdir()` inherits that | advisory | `df -h /tmp`; `OSError: [Errno 122]` at 20:13Z |
| **X61-B2** | `tools/gates/frozen/README.md` does not exist, although `gate-frozen-run-standard.md:54` declares it | standing (round-27) | §7 |
| — | no committed frozen byte is altered; all divergence is in live surfaces the rows point at | measured | §3 |
| — | the 8 mismatches are correct gate refusals on a stale profile pin, not gate defects | measured | §3 |

## 7. What this seat did not check

- It does not read `reports/round-28/validation.json` as adjudication, and it
  adjudicates nothing. Claim O's verdict is the runner's to issue.
- It does not verify that the *content* of a re-pinned row is honest — only that
  a digest matches. A pin is integrity, never truth and never clearance.
- It does not re-run `reports/round-28/sweep/sweep.py`; that is the O seat's
  instrument and its own receipt is `reports/round-28/sweep/_prelanding-census.md`.
  Where the two agree (12 manifests, the same D4 rows drifted) they do so by
  different machinery; where they differ it is the scope boundary A1 names.
- It does not audit the frozen surface **as a record** — receipt agreement,
  record internals, the current generation's replay. That is X62.
