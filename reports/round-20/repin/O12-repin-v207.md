# R20-O12 — re-pin: the round-16 v2-07 helper baseline, new revision `r20`

- round: 20 (operator: loop 2 of 3, build round 4 of 4) · shard: **O11..O14**
  (re-pin ×4) · owner: L2 worker, kotodama-shokunin lane.
- assignment (verbatim): "O R20-O11..O14 (re-pin x4): update the pins that name
  d2-typed-labels.py (round-18 repin-d2 rows, round-16 v2-07 expected.json pins,
  round-9 baselines if pinned) as NEW rows with the before/after table extended;
  replay green; reports/round-20/repin/."
- date: 2026-10-18; readings 12:56Z–13:16Z; freeze 13:14Z.
- canon: NON-CANON engineering evidence. A pin is bytes-and-verdict evidence, not
  a clearance: the packet this baseline grades still carries `partial 5` and
  `unresolved 2` claims.
- writes: **`reports/round-20/repin/expected-v2-07-r20.json`** (new file) and this
  file. The filed round-16 and round-18 baselines are opened read-only; no byte
  under `reports/round-15/` or `reports/round-16/` or `reports/round-18/` changes.
- **status: COMPLETE.** New revision frozen (`sha256 e594137c…`,
  `baseline_digest 34615988…`), helper verify exit 0; **1 of 28 input pins moved**
  — the projector.

## 1. What is being re-pinned

`reports/round-16/handoff/expected-v2-07.json` is the baseline the round-15
helper `reports/round-15/handoff/frozen-verify.py` reads with `--baseline`. Its
read set is the helper's own constants: the round-15 v2 packet twins
`packet-v2-05.{md,yml}`, the shape gate `tools/gates/handoff-packet-check.py`,
the two harness validators, the D2/D3 artifacts the manifest rows name, the
corpus/lesson documents, and the projector `tools/d2-typed-labels.py` — 28 digest
pins plus verdict pins (scan line, whole-stdout digest, census, uncertainty,
links, manifest row count).

Round 18 landed a successor revision (`reports/round-18/repin/expected-v2-07-r18.json`)
with 0 moved pins. Round 20 moved one of the 28 inputs: the projector
`tools/d2-typed-labels.py 0da0015f… → 76536a92…` (claim O's per-family era-alias
leg, §4 of `O11-repin-d2.md`). A pin file is never rewritten to match a later
revision, so the successor is a new file:

```sh
python3 reports/round-15/handoff/frozen-verify.py --freeze \
    --baseline reports/round-20/repin/expected-v2-07-r20.json
```

The helper's freeze writes only the path it is given, and its `measure()` runs
twice and refuses a moving tree (`V2F-DIGEST`), so the freeze is itself a
stability control. The provenance fields (`supersedes`, `revision_note`,
`frozen_by`) were added after the freeze and `baseline_digest` recomputed with
the helper's own canonicalization (imported from the helper, so the landed file
reads green).

## 2. Before pins — filed revisions

| item | round-16 filed | round-18 revision |
|---|---|---|
| file sha256 | `dc75c5d7e347987e81efe6f6fe17314e8f6a2ce26a12a1ca7ec3567a21dcaad1` | `d5fda399490d47eb35be2d14f14d8652fe8fd071df46de0fb90fdc1567b899f9` |
| `baseline_digest` | `7f0fd619…` | `ee9f6277…` |
| input pins | 28 | 28 |
| projector pin | `0da0015f…` | `0da0015f…` |
| verify reading at 13:14Z (live tree) | **exit 2** — drift | **exit 2** — drift |
| verify reading at 12:56Z (pre-projector-change) | exit 0 | exit 0 |

The two filed revisions read **exit 2 today, and that is the correct reading**:
they pin the projector revision that was live when they were frozen, and the
round-20 projector revision is not that revision. The helper detects it as input
drift against the live tree. This is exactly the class the standard answers with
a new revision id, not an edit.

## 3. After pins — `reports/round-20/repin/expected-v2-07-r20.json`

| item | value |
|---|---|
| file sha256 | `e594137c4fe4402bd9edb5cce324346ed0aa654c23ea3365526c74ee7b0efd63` |
| `baseline_digest` | `34615988a0156fb040a7399f444d646987d3a8da1845912c1ae1fe7b87084b5a` |
| `supersedes` | `reports/round-18/repin/expected-v2-07-r18.json (sha256 d5fda399490d47eb35be2d14f14d8652fe8fd071df46de0fb90fdc1567b899f9)` |
| `frozen_at` / `frozen_by` | `2026-10-18` / `kotodama-shokunin round-20 O11-O14 re-pin seat via reports/round-15/handoff/frozen-verify.py --freeze` |
| input pins | 28 |
| `packet_sha256` / `packet_yml_sha256` | `24f9dd39bdad…` / `39cf4d53b02a…` (unchanged) |
| `gate_stdout_sha256` | `7c581047…` (unchanged: `fields=16/16 glossary=20/20 findings=0`, exit 0) |
| census / uncertainty / links / `manifest_rows` | `15 {supported 8, partial 5, unresolved 2}` / `{exit 0, claims 15, findings 0, require_oq 0}` / `{exit 0, links 50, resolved 50, findings 1}` / 26 — all unchanged |
| verify reading (live tree, 13:14Z) | **exit 0** — `frozen-v2: exit=0 fields=16/16 glossary=20/20 findings=0 claims=15/15 … links=50/50 packet_sha256=24f9dd39bdad…` |

## 4. Before/after movement table

| pin class | before (round-18 revision) | after (round-20 revision) | movement |
|---|---|---|---|
| `inputs["tools/d2-typed-labels.py"]` | `0da0015f…` | `76536a92…` | **1 moved — the re-pin** |
| the other 27 input pins | values in the round-18 file | key-by-key identical | **0 moved** (measured by comparing the two `inputs` maps key by key) |
| packet `packet_sha256` / `packet_yml_sha256` | `24f9dd39…` / `39cf4d53…` | identical | none |
| shape-gate `gate_stdout_sha256` | `7c581047…` | identical | none |
| `expected_scan` | `16/16`, `20`, `0` | identical | none |
| `census` | 15 / `{8, 5, 2}` | identical | none |
| `uncertainty` / `links` / `manifest_rows` | as filed | identical | none |
| `baseline_digest` | `ee9f6277…` | `34615988…` | changed — the digest covers `frozen_at`/`frozen_by`/`supersedes`, which is what a new revision is |
| helper verify, filed revisions | exit 0 (pre-change) | **exit 2** (drift, correct) | red by construction |
| helper verify, new revision | — | **exit 0** | green |

## 5. One pin, two homes: the peer revision, named

The O-wart seat (R20-O05..O10) independently froze the same surface at
`reports/round-20/wart/expected-v2-07-r20.json` (13:06Z). It verifies **exit 0**
against the live tree and its projector pin is the same live value
(`76536a92…`); this seat verified it and did not rely on it.

- Why this file exists anyway: the assignment names this surface for **this**
  home, and the round's counting command discovers re-pin rows by name under
  `reports/round-20/**`.
- Why it is not hidden: the duplication is deliberate and recorded here. Both
  files pin the same 28 live values; they differ in provenance fields
  (`supersedes`/`revision_note` name the round-18 revision in this file, the peer
  file carries the helper's default `frozen_by` and no `supersedes`).
- If the integrator prefers one home, drop one file — the surviving file is a
  complete pin of the same bytes, and neither is referenced by any tool.

## 6. Re-verification commands (third party, no scratch needed)

```sh
python3 reports/round-15/handoff/frozen-verify.py \
  --baseline reports/round-16/handoff/expected-v2-07.json        # exit 2: filed pin, drift (expected)
python3 reports/round-15/handoff/frozen-verify.py \
  --baseline reports/round-18/repin/expected-v2-07-r18.json      # exit 2: filed pin, drift (expected)
python3 reports/round-15/handoff/frozen-verify.py \
  --baseline reports/round-20/repin/expected-v2-07-r20.json      # exit 0
python3 reports/round-15/handoff/frozen-verify.py \
  --baseline reports/round-20/wart/expected-v2-07-r20.json       # exit 0 (peer revision)
sha256sum reports/round-20/repin/expected-v2-07-r20.json \
          reports/round-20/wart/expected-v2-07-r20.json
python3 -c "import json;d=json.load(open('reports/round-20/repin/expected-v2-07-r20.json'));\
print(d['inputs']['tools/d2-typed-labels.py']);print(len(d['inputs']),'pins')"
```

## 7. Limits

- The 28-pin read set is the helper's own constant list and was **not** widened
  here: a value the helper does not read is not pinned by this file.
- The pinned packet pair is the round-15 v2 twins (`packet-v2-05.*`); `v2-07` is
  the round-16 keyed-build label carried by the baseline id, not a different
  packet pair. A change to the helper's read set is a tool change and needs its
  own selftest run, which this seat did not modify.
- A green verify is reproduction, not acceptance. The packet's own claim statuses
  (`partial 5`, `unresolved 2`) are the design-level reading and they did not
  move.
