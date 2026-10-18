# R18-D21 — scribe: frozen-manifest records (round 18, claim O/D boundary)

- round: 18 (operator loop 2 of 3, build round 2 of 4; 64 workers,
  `opencode-go-2/deepseek-v4.1-flash`) · seat **R18-D21** (scribes+docs ×8,
  shard D21) · owner: L2 worker, kotodama-shokunin lane.
- assignment (verbatim): "D R18-D21..D28 (scribes+docs x8): frozen-manifest
  records; fragment ledger; capability drafts; ASSEMBLY.md/README updates for
  culture-d4 (new files only); docs; run logs; disposition drafts; spot-check
  ledger. reports/round-18/d4/scribe-{1..8}.md."
- date: 2026-10-18. Stamps UTC unless marked local (lane-local = UTC-03:00).
  Reference revision `c66ac3c951b346a2a56f9386e3324b4f5fe33902` (round-18
  declare, 07:17:35 -0300); declared baseline
  `3dd3754207032cb81f5fb3e202fe85cf79211339` (`reports/round-18/claims.json:5`,
  HEAD's direct parent).
- canon: NON-CANON engineering record. This file records bytes and verdicts;
  it blesses no re-pin, admits no round, and certifies no canon. The parent
  owns the integration decision.
- writes: **this file only**, plus gitignored scratch under `.scratch/r18d21/`
  (`export TMPDIR=$PWD/.scratch` preceded every scratch-writing command). No
  tool, gate, packet, component, projection, manifest, baseline or filed
  round-8..17 byte is edited by this seat. No commit, no push.
- measurement window: 2026-10-18T10:19:55Z–10:26Z. The wave was writing
  throughout (first round-18 artifact landed 10:24:55Z, §7); every pin below
  names its stamp, and a later re-read is a new measurement.

## 0. Verdict at a glance

| # | reading | class |
|---|---|---|
| 1 | `tools/gates/frozen/round-11/MANIFEST.tsv` (11 rows) — replay **11/11 reproduced, exit 0** (out-of-repo TMPDIR) | **GREEN**, but row 1 pins the pre-round-18 gate bytes (`d102fd1d…`) — the re-pin target of claim O |
| 2 | `reports/round-17/tests/frozen/MANIFEST.tsv` (5 rows) — replay **5/5 reproduced, exit 0** | **GREEN**, but the record's live-path tie is now stale: its pinned packet copy `2776d85c…` (82635 B) is pre-normalization; live packet is `e7ecd204…` (82859 B) |
| 3 | `tools/gates/frozen/round-3/MANIFEST.tsv`, `round-3/attempt-1/MANIFEST.tsv` — exit 2, 7/7 `gate_digest_mismatch` | **RED-could-not-evaluate** (historical generation; re-measured, unchanged class) |
| 4 | `tools/gates/frozen/round-4/MANIFEST.tsv` — absent → exit 2 `manifest_unreadable` | **no manifest** (historical outputs only) |
| 5 | r9-pre baselines (8 `expected.json`, 7 gates) — pins re-read, all gate pins equal on-disk gates | **GREEN-pinned**; not touched by the generalization unless a culture gate changes |
| 6 | `reports/round-16/handoff/expected-v2-07.json` — pins `tools/d2-typed-labels.py` `0da0015f…` and `tools/assemble-d2.py` `8ea6bdde…` among 6 tool digests | **GREEN-pinned**; a projector/adapter digest change breaks this pin |
| 7 | round-18 D4 surfaces: `examples/culture-d4/expected-holds.json` (`09490a27…`, landed 10:24:55Z) and two new pinnable gates `tools/gates/d4-{assembly,typed-labels}-check-gate.py` | **new surfaces**, no frozen row yet at this seat's close (§7) |

## 1. Sweep — every frozen surface in the lane

```sh
find tools/gates/frozen tools/gates/expected -maxdepth 2 -name 'MANIFEST*.tsv' -o -maxdepth 2 -name 'expected.json'   # 10:19Z
find . -name 'MANIFEST*.tsv' -not -path './.git/*' -not -path './.scratch/*' | sort
find . -name 'expected.json' -not -path './.git/*' -not -path './.scratch/*' | sort
```

Live surfaces (all read-only over the lane):

| home | kind | rows / contents | digest(s) read |
|---|---|---|---|
| `tools/gates/frozen/round-3/MANIFEST.tsv` | legacy TSV replay | 7 | not re-hashed by this seat (unchanged class, replay re-run) |
| `tools/gates/frozen/round-3/attempt-1/MANIFEST.tsv` | legacy TSV replay | 7 | same |
| `tools/gates/frozen/round-4/` | unpinned outputs | 5 `.out`, no manifest | — |
| `tools/gates/frozen/round-11/MANIFEST.tsv` | TSV replay, live D2 generation | **11** | replay receipt §2 |
| `tools/gates/frozen/round-11/typed-pipeline/` | frozen typed run | `packet.d2.typed.yml`, `packet.d2.yml`, `inputs/…`, `run.log`, `run-receipt.json`, `freeze.txt` | row 1 pins input `1b5010b7…`, output `9a69985a…` |
| `tools/gates/{frozen,expected}/**/r9-pre/expected.json` + `reports/round-9/baselines/**/expected.json` | standard §3 baselines | 8 files, 7 gates | gate pins `e2fa3223…`, `5368b135…`, `d9e4e8f4…`, `e6bffd70…`, `d5fe087f…`, `2c4dd397…`, `8a96aaf4…` |
| `reports/round-17/tests/frozen/` | TSV replay, D4 legacy generation | 5 rows + packet copy + snapshot + 5 outputs | replay receipt §2 |
| `reports/round-16/handoff/expected-v2-07.json` | handoff baseline (profile `kotodama-handoff-v2/1`) | 26 manifest rows, 6 tool pins | `d2-typed-labels.py 0da0015f…`, `assemble-d2.py 8ea6bdde…`, `handoff-packet-check.py e2fa3223…`, `harness/packet_links.py 66d854cc…`, `harness/packet_uncertainty.py cdcc1931…`, `check-evidence-coupling.py 849494b0…` |
| `reports/round-15/handoff/expected.json`, `reports/round-11/handoff/expected.json`, `examples/culture-d3/expected.json` | exercise / guard freezes | n/a here | not re-measured by this seat |

## 2. Replay receipts (2026-10-18, TMPDIR outside the repo — `tools/replay-frozen.py` refuses in-repo mirrors)

| # | command | exit | observed |
|---|---|---:|---|
| 1 | `TMPDIR=/var/tmp/kotodama-r18d21 python3 tools/replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv` | 0 | `REPLAY OK: 11/11 rows reproduced the recorded verdicts` — every row `bytes=match launched=yes` (10:21–10:22Z) |
| 2 | same tool over `reports/round-17/tests/frozen/MANIFEST.tsv` | 0 | `REPLAY OK: 5/5 rows reproduced` (10:22Z) |
| 3 | same over `tools/gates/frozen/round-3/MANIFEST.tsv` | 2 | `REPLAY COULD-NOT-EVALUATE: 7 could-not-evaluate … gate: on-disk bytes are not the pinned revision` |
| 4 | same over `tools/gates/frozen/round-3/attempt-1/MANIFEST.tsv` | 2 | same 7/7 `gate_digest_mismatch` class |
| 5 | same over `tools/gates/frozen/round-4/MANIFEST.tsv` | 2 | `COULD-NOT-EVALUATE manifest_unreadable` |

Rows 3–5 are the recorded historical class: rounds 8–16 legitimately revised
those gates, so the old manifests fail closed. No filed manifest was edited to
make a row green.

## 3. The re-pin blast radius of the round-18 generalization (pin graph)

Measured 10:21:34Z by digest sweep (`grep -rl <digest-16> .` excluding
`.git`, `.scratch`, `__pycache__`):

| surface | digest (10:19:55Z) | files naming the digest | load-bearing pins |
|---|---|---:|---|
| `tools/gates/typed-pipeline-gate.py` | `d102fd1dd1bae3cc…` | 12 | `tools/gates/frozen/round-11/MANIFEST.tsv` row 1 (`gate_sha256`); `typed-pipeline/run-receipt.json` |
| `tools/d2-typed-labels.py` | `0da0015f700345c9…` | 67 | `examples/culture-d2/expected-holds.json` (`projector_sha256`); `reports/round-16/handoff/expected-v2-07.json` (inputs) |
| `tools/assemble-d2-typed.py` | `c7e5a7493601d331…` | 17 | `examples/culture-d2/packet.d2.typed.yml` (`assembly.adapter_sha256`); round-11 frozen typed packet + its `inputs/` copy |
| `tools/assemble-d2.py` | `8ea6bdde9514ee96…` | 77 | `examples/culture-d4/packet.d4.yml` (`assembly.serializer_sha256`); v2-07 expected; D3 artifacts |
| `examples/culture-d2/packet.d2.typed.yml` | `1b5010b7f449ec78…` | 9 | `tools/gates/frozen/round-11/MANIFEST.tsv` rows 1–2 (`input_sha256`) |
| `examples/culture-d2/typed-labels.d2.yml` | `a3aa452cd5ae77c3…` | 53 | D2 typed packet `assembly.projection_sha256`; v2-07 expected |
| `examples/culture-d2/packet.d2.yml` | `e0f21509e14ac03e…` | 70 | r9-pre baselines; v2-07 expected |
| `tools/assemble-culture-d4.py` | `943f487ba991d45d…` | 1 | `examples/culture-d4/packet.d4.yml` (`assembly.assembler_sha256`) |
| `examples/culture-d4/packet.d4.yml` | `e7ecd2045ef0e5f9…` | 1 | `examples/culture-d4/typed-labels.d4.yml` (`assembly.packet_sha256`); new `expected-holds.json` |
| `examples/culture-d4/typed-labels.d4.yml` | `a59990bbfe5a8992…` | 0 (before 10:24Z) | now pinned by the new `expected-holds.json` (`projection_sha256`) |

Reading for the cascade (claim O's "re-pin cascade lands"): a generalized
**gate** breaks exactly one live pin — round-11 manifest row 1 — plus the
round-11 receipt; a changed **projector or adapter** additionally breaks the
D2 typed packet's embedded pins and, through rows 1–2 of the same manifest,
the frozen typed-run generation; a changed **D2 packet or projection** is not
expected of this round at all (default path byte-identity is claim O's own
regression bar). The r9-pre baselines pin the five culture gates and the
handoff/provenance gates only — none of them pins the typed-pipeline gate —
so they are regression evidence, not re-pin targets, unless a culture gate
moves.

The append-only rule (standard §3/§6, `reports/round-11/depth/repin.md` §2):
a later gate revision produces a **new** generation or a new row with
before/after pins recorded; no filed manifest row is edited in place.

## 4. Round-17 frozen record — drift of its live tie (measured, not repaired)

| item | round-17 record (frozen 2026-10-18 06:45–06:58Z) | live at 10:19Z |
|---|---|---|
| packet bytes | copy `2776d85c…` 82635 B (pre eras-normalization) | `e7ecd204…` 82859 B |
| naming-gate verdict over the pinned copy | exit 1 / 8 findings (5 rows: 1/8, 1/1, 0/0, 0/0, 0/0) | over the live packet: exit 1 / **14** findings (7 `NAME-NEAR` + 6 `PHON-INVENTORY` + 1 `CROSS-HOLD`) |
| phonology over pinned copy | exit 1 / 1 | exit 1 / 1 (`A-CLASS`, unchanged) |
| costume / lexicon / myth | exit 0 / 0 each | exit 0 / 0 each |
| replay | 5/5 green (still true) | replay of the frozen copy stays green because the row pins a **snapshot copy**, never the live path |

The drift is a property of the record's *live-path* receipts
(`reports/round-17/tests/replay.md` §3), not of its pins: the manifest pins
its own snapshot and continues to reproduce. A round-18 D4 generation must
pin the **current** bytes (packet `e7ecd204…`, plus the typed packet once it
lands), per the standard's copy rule.

## 5. What a round-18 frozen generation must carry (requirements, not a record)

Derived from the standard and from the two new pinnable gates (landed
10:25Z, `tools/gates/d4-typed-labels-check-gate.py` `05f99629…` 2487 B;
`tools/gates/d4-assembly-check-gate.py` `df1a364b…` 2751 B, both exit 0 on
default invocation):

1. **D4 typed-run row** — the generalized typed-pipeline gate over
   `examples/culture-d4/packet.d4.typed.yml` (absent at this stamp), exit and
   finding-count as recorded, output bytes pinned.
2. **D4 projection-check row** — `d4-typed-labels-check-gate.py` over the
   delivered projection, exit 0, stdout `examples/culture-d4/typed-labels.d4.yml:
   byte-identical deterministic projection`.
3. **D4 assembly-check row** — `d4-assembly-check-gate.py`, exit 0, stdout
   `packet.d4.yml: byte-identical deterministic assembly`.
4. **Legacy D4 gate rows** — optional; the round-17 generation already pins
   the five legacy runs over the pre-normalized copy, and a round-18 row set
   would pin the live bytes instead.
5. New generation directory + `MANIFEST.tsv` + `freeze.txt` + per-row
   snapshots; never an in-place edit of round-11 or round-17 rows.

## 6. Reproduction

```sh
export TMPDIR=$PWD/.scratch
TMPDIR=/var/tmp/kotodama-r18d21 python3 tools/replay-frozen.py tools/gates/frozen/round-11/MANIFEST.tsv   # 11/11, exit 0
TMPDIR=/var/tmp/kotodama-r18d21 python3 tools/replay-frozen.py reports/round-17/tests/frozen/MANIFEST.tsv # 5/5, exit 0
python3 tools/gates/d4-typed-labels-check-gate.py; echo $?   # 0
python3 tools/gates/d4-assembly-check-gate.py; echo $?       # 0
```

## 7. In-flight state at close (poll log)

Poll cadence 60 s (`reports/round-18/d4/scribe-2.md` ledger carries the full
log; receipt `.scratch/r18d21/poll.log`): T1 10:23:55Z 2 round-18 files;
T2 10:24:55Z `examples/culture-d4/expected-holds.json` present; T3
10:25:55Z round-18 files 4 + two `tools/gates/d4-*-check-gate.py` present;
`tools/gates/typed-pipeline-gate.py` still `d102fd1d…` (pre-generalization) at
every poll through 10:25:55Z. **No frozen row for the D4 typed run existed at
this seat's last stamp**; the generalized gate's own digest is therefore
"before" only, and the after-pin belongs to the parent's integration.

## 8. Limits

- Hashes are read-time pins: a later mismatch means the file moved after this
  read, never that this read was wrong.
- `REPLAY OK` is reproduction only; rows recorded red stay red.
- This seat ran read-only commands plus its own `.scratch` receipts; nothing
  in `tools/`, `examples/`, `corpus/` or `reports/round-{8..17}/` was written.

## 9. Post-state addendum — the re-pin cascade as it landed (measured 10:29–10:37Z)

The wave landed the cascade while this seat's poll ran. Recorded here with
stamps; nothing below is inferred.

### 9.1 Before/after pins of the four live tool surfaces (full digests)

`before` = `git show 3dd3754:<path> | sha256sum` (the declared baseline);
`after` = `sha256sum` live at 10:36Z.

| surface | before (baseline `3dd3754`) | after (live 10:36Z) | changed |
|---|---|---|---|
| `tools/gates/typed-pipeline-gate.py` | `d102fd1dd1bae3cc4c9d0ea33844b2f706a2098707938c82c75ce9fb6368e27d` | `d4785d9afc0306afb0a9c78c3c2b014097090413bf9c889ed72fa9558c394ba0` | **yes** |
| `tools/assemble-d2-typed.py` | `c7e5a7493601d3312f2eb55185ac4d081139cdaa0e11f67dd69f67250b037071` | same | no |
| `tools/d2-typed-labels.py` | `0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802` | same | no |
| `tools/assemble-d2.py` | `8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d` | same | no |

The gate digest moved repeatedly inside the window — poll rows (receipt
`.scratch/r18d21/poll.log`): `d102fd1d…` 10:23:55–10:28:55Z; `bba60bc18ebc1282…`
10:29:55Z; `edfec5f37a511e09…` 10:30:55Z; `d09f7c3b0cb83742…` 10:31:55Z;
`3897833101be9c3a…` 10:32:55Z; `d4785d9afc0306af…` from 10:33:55Z. The digest
above is the last observed; a later write is a new reading, not a correction
of this one.

### 9.2 Default D2 path after the generalization (regression reading)

| # | command | exit | observed | stamp |
|---|---|---:|---|---|
| A1 | `python3 tools/gates/typed-pipeline-gate.py` | 0 | `summary: 16/16 legs passed`; stdout file digest `15cdfbda73cd56cb6107…` — **the same stdout digest the pre-change run and the D01/D02 fragment recorded** | 10:36Z |
| A2 | `python3 tools/gates/typed-pipeline-gate.py --help` | 0 | usage still `[-h] [--json] [--selftest] [packet]` — no `--assembler` flag visible at this revision, so the declared pin is packet-side at this stamp | 10:36Z |
| A3 | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | 2 | `ok L1-assembler`, `ok L1-expected-holds`, then `FAIL L1-build: adapter missing: tools/assemble-d4-typed.py`; zero FINDING/NOTE lines — receipt `.scratch/r18d21/gate-d4-after.out` | 10:37Z |

The refusal detail changed from `assembler_identity … e7ecd2045ef0 vs
e0f21509e14a` (pre, §2 row 14) to a missing D4 adapter: the assembler-identity
leg no longer blocks the D4 packet, and the remaining blocker is a not-yet-landed
adapter. That is the O family's gap to close, not a D-family defect.

### 9.3 The rounds-9/11 surfaces the cascade touched

| surface | state at 10:31Z |
|---|---|
| `tools/gates/frozen/<gate>/r18-post/` × 7 (costume, handoff, lexicon, myth, naming, phonology, provenance) | **new baseline ids**, revision `c66ac3c951b346a2a56f9386e3324b4f5fe33902`, gate pins equal the live gates; `r9-pre` homes untouched (`git status --porcelain -- tools/gates/frozen/<gate>/r9-pre` → empty for the three pre-existing ones) |
| `reports/round-9/**` | **no changes** at 10:31Z (`git status --porcelain -- reports/round-9` → empty; the 7 baseline dirs are all tracked) |
| `tools/gates/frozen/round-18-repin/MANIFEST.tsv` | 11 rows; row 1 pins `tools/gates/typed-pipeline-gate.py` at `5b4501a9dd8c1dfb3c6bcd444a6ee50b97138fc37087093224b781fdfd5419c8` with the round-11 verdict (exit 0 / 15 / output bytes `9a69985a…`) — a verdict-identical re-pin of round-11 row 1 |
| battery over the enlarged surface | exit 0, `pass 7, fail 0, unevaluable 0` (10:32Z) |

**Routed finding (F-D21-1, for the parent — not fixed here).** Replaying the
new generation at 10:36Z reads
`REPLAY COULD-NOT-EVALUATE: 1 could-not-evaluate, 0 mismatch, 10 reproduced of 11`
(exit 2), and the failed row is row 1/2 (the typed-pipeline row):
`could-not-evaluate reason=gate_digest_mismatch … on-disk bytes are not the
pinned revision: tools/gates/typed-pipeline-gate.py`. The generation pins
`5b4501a9…` while the live gate is `d4785d9a…`, so the generation must be
rebuilt at the final gate revision (or the gate revision must stop at the
pinned bytes) before claim O's "replays green" can be measured. Rows 3–12 of
the same manifest reproduce fine.

### 9.4 Provenance re-pin note (baseline home echo)

`tools/gates/frozen/provenance-audit/r18-post/` records stdout
`5dd12b31e79c22aa…` where `r9-pre` recorded `26f217410f2206bc…`, yet the
inputs digests are **identical**, the gate pin is identical (`8a96aaf4…`), and
`expected` (exit 1, the same six finding ids) is byte-equal. The delta is the
baseline home echoed into the scan lines (`…/r9-pre/inputs/…` vs
`…/r18-post/inputs/…`). A re-pin that moves a baseline's home therefore changes
its recorded stdout bytes while the verdict class and finding-ID set are
unchanged; the battery compares finding sets and stays green. Schema note:
`r18-post/expected.json` omits the `finding_counts` map that `r9-pre` carried.

### 9.5 Still absent at 10:37Z

`examples/culture-d4/packet.d4.typed.yml`; `tools/assemble-d4-typed.py`; a D4
typed row in any frozen manifest; `reports/round-18/repin/` (the manifest's
own index/freeze.txt at this stamp was not inspected). Negative claims rest on
`ls examples/culture-d4/` (7 entries) and the poll log.

### 9.6 Latest gate readings (the after-pin was not settled inside this window)

Poll rows after §9.1: `d4785d9afc0306af…` held from 10:33:55Z to 10:34:55Z,
then the writer moved again — `ea95e2a1452ef51d780a…` at 10:35:55Z (receipt
`.scratch/r18d21/poll.log`, i=13; `reports/round-18/` files 36 at the same
poll). The round-18 generation's own pin (`5b4501a9…`) predates even
`d4785d9a…`, so at this seat's close **no revision of the generalized gate is
pinned by a green frozen row**.

Consequence for the parent (routed, F-D21-1 extended): after the O family stops
writing, (a) take the final gate digest, (b) rebuild
`tools/gates/frozen/round-18-repin/MANIFEST.tsv` (or a fresh generation) so its
`gate_sha256` cell names that digest while the recorded verdict bytes stay the
round-11 `9a69985a…` value — a verdict-identical re-pin — and (c) re-run the
replay. Any before/after ledger the runner reads must name **both** digests
(before `d102fd1d…`, after the final one); this section names the observed
sequence so a ledger can be written without guessing.
