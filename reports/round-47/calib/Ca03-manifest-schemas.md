# Ca03 — MANIFEST ledger schema evolution: closure rows 33–42 vs lane close-receipt rows 43–44 (46)

Seat `Ca03`, claim **Ca** (calibration), round 47, loop 2 position 1. Read-only
reconciliation; this file is the only path written.

- Baseline commit: `6e9a30d` (matches `reports/round-47/claims.json:7`; `git rev-parse --short HEAD` -> `6e9a30d`).
- Ledger: `/home/vgpnk/Projects/shokunin/MANIFEST.json` — a **sibling**, read-only per
  `AGENTS.md` ("siblings … are read-only"); no write attempted.
- Observation window: first read `2026-10-19T17:46Z`; authoritative census
  `2026-10-19T17:53:10Z`.
- Pinned digest: `sha256 509305c8b95e5e732b26b59a5874e31f4c368afcba0193a10443023073724e32`,
  293,641 bytes, 281 `rounds[]` rows, mtime `2026-10-19 14:52:08 -0300`.
- Earlier read in the same window: `sha256 19ddec8b8c667f403a0006eb463c1604dd4f61bb7b08a29e366286832d2a705b`,
  291,909 bytes, 280 rows. The delta is **not** a kotodama change: one non-kotodama row
  (kotoba loop round 7, `closed_at 2026-10-19T17:52:08Z`) was appended at EOF between the
  two reads. The 13 kotodama rows compared field-by-field were unchanged. The ledger is
  live and append-ordered — hence a pinned digest, not a path, in this record.

**Scope.** This record covers the 13 kotodama close rows only (rounds 33–42, 43, 44, 46).
`rounds[]` as a whole is heterogeneous: measured `type` counts at the pinned digest are
`closure 122, closure-correction 56, train 63, retroactive-closure 13, mint 10, craft 5,
ops 3, work 2, train+audit 2, train+audit+unlock 1, scaffold 1, no-type 3`. Nothing here is
a whole-ledger schema specification.

## 1. Why this item is in the Ca queue (provenance correction)

The r47 Ca claim (`reports/round-47/claims.json:52`) lists "the two MANIFEST ledger
schemas documented" among the loop-1 closes. The loop-1 retrospective's carried list
(`reports/round-46/loop-1-retrospective.md:43-53`) has **five** bullets and **none** names
the MANIFEST schemas. The item originates in the r46 Ca01 audit's schema note
(`reports/round-46/audit/Ca01-manifest.md:7-8` and `:28-32`), restated in
`reports/round-46/review/R01-review.md:87-89` and in the r46 receipt's limits
(`reports/round-46/validation.json:147`).

Recorded as such rather than back-attributed to the retrospective. The audit itself called
the split "a schema-evolution observation, not missing rows" (`Ca01-manifest.md:31-32`), so
the correct class is **recorded**, not fixed-with-evidence: no defect is claimed and no filed
byte changes.

## 2. Schema S1 — fleet closure row (rounds 33–42)

`MANIFEST.json:4241` (r33, the first S1 row) through `:4806` (r42). All 10 rows carry the same
11-key set (verified by key-set census; 10/10 identical).

| field | type | presence | meaning |
|---|---|---|---|
| `round` | int | 10/10 | entry round |
| `date` | `YYYY-MM-DD` | 10/10 | close date (local) |
| `type` | `"closure"` | 10/10 | row kind |
| `closed_at` | ISO-8601 with offset | 10/10 | close timestamp |
| `lanes` | `{lane_id: status}` | 10/10 | fleet-scope lane status; status vocabulary `ok\|failed\|not-dispatched\|in-flight` (PROTOCOL.md:239-241) |
| `lane_rounds` | `{lane_id: int}` | 10/10 | lane-counter annotation; measured `lane_rounds.kotodama == round` for all 10 |
| `promotions` | array | 10/10 | empty in all 10 |
| `minted` | array | 10/10 | empty in all 10 |
| `admitted` | bool | 10/10 | close verdict: 8 true / 2 false (r36, r42) |
| `verdicts` | object, 6 axes | 10/10 | `depth, coverage, operability, freshness, calibration, adjacency`; values `unchanged`/`improved` |
| `notes` | string | 10/10 | freeform; carries receipt ids (e.g. r33 "receipt 93b28f36") and work commits |

S1 conforms to the round-entry shape in `PROTOCOL.md:237-243`
(`{round, date, type, lanes, promotions, minted, notes}` with `type`/`closed_at` optional).

## 3. Schema S2 — lane close-receipt row (rounds 43, 44, 46)

`MANIFEST.json:4860` (r43), `:4979` (r44), `:5030` (r46). All three carry the same 15-key
set; r46 extends the observed use beyond the two rows the r46 audit named.

| field | type | presence | meaning |
|---|---|---|---|
| `round` | int | 3/3 | entry round |
| `lane` | `"kotodama"` | 3/3 | lane id, flat (no `lanes` map) |
| `loop` | int | 3/3 | regimen loop number |
| `position` | int | 3/3 | position in the loop schedule (11, 12, 14) |
| `provider` | string | 3/3 | provider lane |
| `model` | string | 3/3 | model id |
| `requested_workers` | int | 3/3 | seat allocation |
| `filed` | int | 3/3 | fragments filed |
| `verdict` | string | 3/3 | `rejected-honest-stop` (43, 44), `admitted` (46) |
| `admitted` | bool | 3/3 | 2 false / 1 true |
| `claims` | `{axis: status}` | 3/3 | per-claim status; key sets measured `{O,C,Ca}` (43, 44) and `{A,O,Ca}` (46) — **not fixed** |
| `baseline_commit` | 7-hex short sha | 3/3 | dispatch baseline |
| `close_commit` | 7-hex short sha | 3/3 | lane close commit |
| `note` | string | 3/3 | freeform close note (singular) |
| `receipt` | repo-prefixed path | 3/3 | `kotodama-shokunin/reports/round-N/validation.json` — resolves from the **fleet root**, not the lane root |

**Absent from every S2 row** (measured, not inferred): `date`, `closed_at`, `type`, `lanes`,
`lane_rounds`, `promotions`, `minted`, `verdicts`. Consequence: S2 carries no ledger-local
timestamp; close time is recoverable only from the fleet commit or the receipt file.

## 4. Discriminator and keying rules

- **Discriminator (structural, since there is no per-row schema version).** S1 has
  `type == "closure"` **and** a `lanes` object; S2 has a flat `lane` string, `verdict`,
  and `receipt`, and **no** `type`. Top-level `version: 1` (`MANIFEST.json:2`) versions the
  ledger, not row shape — 12 `type` values and 3 typeless rows coexist under it.
- **The join key that works for both is `admitted`** (present 10/10 and 3/3). `round` alone
  is not a key: see trap T1.
- **Row identity per protocol.** `PROTOCOL.md:283-290`: a row describes lane-round
  `(lane_id, entry.round)`; `lane_rounds` "annotates it and never re-keys it".
  `PROTOCOL-APPENDIX.md:37` records the measured cost of violating this ("66 ok / 3 failed /
  13 not-dispatched / 1 in-flight over 83 rows, erasing 3 of the 4 carried in-flight rows").
- **Reference consumer.** `reports/round-46/run-validation.py:94-97` builds two maps —
  `closure = {r["lane_rounds"]["kotodama"]: r}` and `perlane = {r["round"]: r if lane ==
  "kotodama"}` — and selects at `:107-110` (`if n in closure: … elif n in perlane: …`).
  This is the only consumer in the repo that parses both schemas; it is correct for this
  window because all 10 S1 `lane_rounds.kotodama` values equal `entry.round`. Note it keys
  S1 by `lane_rounds`, the annotation map, not by `entry.round` — benign here, contrary to
  the identity rule in general (observation OBS-2).

## 5. Measured traps for consumers

**T1 — `round` is not unique and the array is append-ordered.** Rounds 37–42 each appear
twice: a kotodama closure row (`MANIFEST.json:4337` for r37) and a kotoba closure row
(`:4505` for r37), through r42 at `:4806` (kotodama) and `:4906` (kotoba). The newest row in
the pinned snapshot is kotoba loop round 7 at EOF (`:5075`), appended after round 46 — so
`rounds[]` is **not** sorted by `round` and a first-match lookup by round number is
ambiguous. Any consumer must filter by lane before keying by `round`.

**T2 — a single-filter read undercounts in either direction.** `lane == "kotodama"` sees
3 of 13 rows (S2 only); `lane_rounds` sees 10 of 13 (S1 only). The r46 audit already named
this (`reports/round-46/audit/Ca01-manifest.md:29-32`).

**T3 — near-colliding field names.** S1 uses plural `notes` and `verdicts` (axis map); S2
uses singular `note` and `verdict` (round verdict). A schema-agnostic merge on `notes`
silently drops S2's note; `row.get("verdict")` on S1 returns `None` (the key is `verdicts`).
Measured key sets confirm the split (11-key vs 15-key sets above).

**T4 — `claims` key set is not stable.** `{O,C,Ca}` at r43/r44 vs `{A,O,Ca}` at r46. A
consumer assuming a fixed three-axis set will KeyError or silently skip the `A` claim.

**T5 — S2's `receipt` is fleet-root-relative.** `kotodama-shokunin/reports/round-43/validation.json`
(`MANIFEST.json:4878`) does not resolve from the lane repo root, only from
`/home/vgpnk/Projects/shokunin/`.

**T6 — S2 diverges from the documented round-entry shape.** `PROTOCOL.md:237-243` specifies
`{round, date, type, lanes, promotions, minted, notes}`; S2 carries none of `date`, `type`,
`lanes`, `promotions`, `minted`. No clause in `PROTOCOL.md` or `PROTOCOL-APPENDIX.md`
describes the flat lane close-receipt schema (`grep -n "per-lane" PROTOCOL.md
PROTOCOL-APPENDIX.md` -> no match). Whether the integrator adopted it by an unrecorded
amendment or ad hoc is **`to-verify`**; the measured fact is the divergence and that a
protocol-shape validator would not recognize S2 rows. Class **recorded** (documentation; no
filed byte changes), owner integrator-of-record, per `PROTOCOL.md:194-196` (the integrator's
`MANIFEST.json rounds` append is one of its six main-repo writes).

## 6. Fenced successor row (DRAFT — integrator applies; Ca06 merges)

```json
{
  "id": "manifest-ledger-two-schema-evolution",
  "origin": "reports/round-46/audit/Ca01-manifest.md:7-8,28-32; reports/round-46/review/R01-review.md:87-89; reports/round-46/validation.json:147",
  "provenance_correction": "Not one of the loop-1 retrospective's five carried bullets (reports/round-46/loop-1-retrospective.md:43-53). The item originates in the r46 Ca01 audit's schema note; recorded here as the loop-1 close the Ca claim names, without back-attribution.",
  "class": "recorded",
  "v2_class_equivalent": "carried-with-owner",
  "owner": "integrator-of-record (MANIFEST.json rounds[] writer; PROTOCOL.md:194-196)",
  "reason": "The loop-1 ledger uses two row schemas for this lane. S1 (rounds 33-42, MANIFEST.json:4241-4806) is the documented fleet closure shape: 11 keys, type=closure, lanes/lane_rounds, admitted, per-axis verdicts, notes. S2 (rounds 43,44,46; MANIFEST.json:4860,4979,5030) is a flat lane close-receipt: 15 keys, flat lane, position/provider/model, verdict, per-claim status map, baseline_commit/close_commit, repo-prefixed receipt, singular note; no date/closed_at/type/lanes/verdicts. Both are machine-readable and both reconcile to their lane receipts (r46 validation 12/12), but they are not interchangeable: lane-only filtering sees 3 of 13 rows, lane_rounds-only sees 10 of 13, and no row-level schema version exists. This row records the two contracts and the consumer rules; it fixes nothing and edits no filed byte.",
  "next_touch": "Integrator: when appending round-47, pick one shape and apply it consistently. If S1, include date/type/lanes/admitted/verdicts and set lane_rounds only where the lane counter differs from round. If S2, include lane/position/provider/model/verdict/claims/baseline_commit/close_commit/receipt; add date or closed_at so close time is ledger-local. Either way do not rely on round alone as a key.",
  "evidence": "MANIFEST.json:4241 (r33 S1), :4337 (r37 kotodama), :4505 (kotoba r37, duplicate round), :4806 (r42 S1), :4860 (r43 S2), :4979 (r44 S2), :5030 (r46 S2); PROTOCOL.md:237-243 (round-entry shape), :283-290 (row identity), :194-196 (integrator write scope); PROTOCOL-APPENDIX.md:37 (lane_rounds keying cost); reports/round-46/run-validation.py:94-97,107-110 (two-schema consumer); reports/round-46/audit/Ca01-manifest.md:7-8,29-32; reports/round-46/validation.json:147.",
  "verification": "Commands run this seat (2026-10-19T17:53:10Z, ledger sha256 509305c8b95e5e732b26b59a5874e31f4c368afcba0193a10443023073724e32, 281 rows): schema census printed S1 rounds [33..42] 11 keys, S2 rounds [43,44,46] 15 keys; S1 lane_rounds==round true for all 10; S2 has date=False, closed_at=False for all 3; S2 claims key sets {43:[C,Ca,O],44:[C,Ca,O],46:[A,Ca,O]}; admitted S1 8T/2F, S2 2F/1T; duplicate round numbers 37-42 present for kotodama+kotoba. Full command and output at §7.",
  "findings": [
    {
      "id": "S1-contract",
      "class": "recorded",
      "owner": "integrator-of-record",
      "evidence": "MANIFEST.json:4241-4806; 10/10 rows share the 11-key set {round,date,type,closed_at,lanes,lane_rounds,promotions,minted,admitted,verdicts,notes}; admitted 8T/2F",
      "next_touch": "none - recorded"
    },
    {
      "id": "S2-contract",
      "class": "recorded",
      "owner": "integrator-of-record",
      "evidence": "MANIFEST.json:4860,4979,5030; 3/3 rows share the 15-key flat set; no date/closed_at/type/lanes/verdicts; receipt is fleet-root-relative",
      "next_touch": "none - recorded; add a close timestamp if S2 is reused"
    },
    {
      "id": "S2-protocol-shape-divergence",
      "class": "recorded",
      "owner": "integrator-of-record",
      "evidence": "PROTOCOL.md:237-243 names {round,date,type,lanes,promotions,minted,notes}; S2 has date/type/lanes/promotions/minted absent; grep -n 'per-lane' PROTOCOL.md PROTOCOL-APPENDIX.md -> no match",
      "next_touch": "to-verify: name the amendment if one exists, else record S2 as a named deviation at the next ledger touch"
    }
  ]
}
```

Two observations for the integrator's mint decision (not rows until minted):

```json
[
  {
    "id": "OBS-1",
    "proposed_row_id": "manifest-round-key-not-unique",
    "status": "candidate - integrator decides whether to mint",
    "owner": "future ledger consumer / runner author",
    "finding": "rounds[] is append-ordered, not sorted, and round numbers repeat across lanes: kotodama and kotoba both carry closure rows 37-42 (MANIFEST.json:4337 vs :4505 through :4806 vs :4906), and the newest row at the pinned digest is kotoba round 7 at EOF (:5075) after round 46 (:5030). A first-match lookup keyed on round alone is therefore ambiguous; filter by lane first.",
    "evidence": "MANIFEST.json:4337,4505,4806,4906,5030,5075; measured duplicate rounds 37-42."
  },
  {
    "id": "OBS-2",
    "proposed_row_id": "r46-validator-keys-s1-by-lane-rounds",
    "status": "candidate - integrator decides whether to mint",
    "owner": "future runner author",
    "finding": "reports/round-46/run-validation.py:95 keys S1 by lane_rounds['kotodama'] rather than entry.round, contrary to PROTOCOL.md:283-290 and the measured cost in PROTOCOL-APPENDIX.md:37. In the r33-42 window this is benign: all 10 lane_rounds.kotodama values equal entry.round (measured true for 10/10). It becomes wrong only where a lane counter differs from the entry round, which the appendix says has happened fleet-wide.",
    "evidence": "reports/round-46/run-validation.py:94-97; PROTOCOL.md:283-290; PROTOCOL-APPENDIX.md:37; measured lane_rounds==round 10/10."
  }
]
```

## 7. Reproduction

```bash
python3 - <<'PY'
import json, hashlib, collections
P='/home/vgpnk/Projects/shokunin/MANIFEST.json'
raw=open(P,'rb').read(); m=json.loads(raw); rows=m['rounds']
sel=[r for r in rows if isinstance(r.get('round'),int) and 33<=r['round']<=46
     and (r.get('lane')=='kotodama' or 'kotodama' in (r.get('lanes') or {}))]
s1=[r for r in sel if r.get('type')=='closure']
s2=[r for r in sel if 'lane' in r and 'type' not in r]
print('ledger sha256', hashlib.sha256(raw).hexdigest(), '| bytes', len(raw), '| rows', len(rows))
print('S1 rounds', [r['round'] for r in s1], '| keys', len(s1[0]))
print('S2 rounds', [r['round'] for r in s2], '| keys', len(s2[0]))
print('S1 lane_rounds==round:', all(r['lane_rounds']['kotodama']==r['round'] for r in s1))
print('S2 has date/closed_at:', {r['round']:(('date' in r),('closed_at' in r)) for r in s2})
print('S2 claims key sets:', {r['round']:sorted(r['claims']) for r in s2})
print('S2 verdict/admitted:', {r['round']:(r['verdict'],r['admitted']) for r in s2})
print('S1 admitted:', collections.Counter(r['admitted'] for r in s1))
print('S2 admitted:', collections.Counter(r['admitted'] for r in s2))
print('round-number duplicates 33-46:', {n:[r.get('lane') or sorted((r.get('lanes') or {})) for r in rows if r.get('round')==n] for n in range(33,47) if sum(1 for r in rows if r.get('round')==n)>1})
PY
```

Measured output at 2026-10-19T17:53:10Z:

```
ledger sha256 509305c8b95e5e732b26b59a5874e31f4c368afcba0193a10443023073724e32 | bytes 293641 | rows 281
S1 rounds [33, 34, 35, 36, 37, 38, 39, 40, 41, 42] | keys 11
S2 rounds [43, 44, 46] | keys 15
S1 lane_rounds==round: True
S2 has date/closed_at: {43: (False, False), 44: (False, False), 46: (False, False)}
S2 claims key sets: {43: ['C', 'Ca', 'O'], 44: ['C', 'Ca', 'O'], 46: ['A', 'Ca', 'O']}
S2 verdict/admitted: {43: ('rejected-honest-stop', False), 44: ('rejected-honest-stop', False), 46: ('admitted', True)}
S1 admitted: Counter({True: 8, False: 2})
S2 admitted: Counter({False: 2, True: 1})
round-number duplicates 33-46: {37: [['kotodama'], ['kotoba']], 38: [['kotodama'], ['kotoba']], 39: [['kotodama'], ['kotoba']], 40: [['kotodama'], ['kotoba']], 41: [['kotodama'], ['kotoba']], 42: [['kotodama'], ['kotoba']]}
```

Line-pin checks (`sed -n` / `grep -n` on the sibling ledger): r33 `:4241`, r37
kotodama `:4337`, kotoba r37 `:4505`, r42 `:4806`, r43 `:4860`, r44 `:4979`, r46 `:5030`,
EOF `:5075`. Protocol pins: `PROTOCOL.md:237-243`, `:283-290`, `:194-196`;
`PROTOCOL-APPENDIX.md:37`.

## 8. Integration instructions (for Ca06)

- Copy the first fenced JSON object (row `manifest-ledger-two-schema-evolution`) into the
  loop-1 queue successor. Keep `evidence` and `verification` byte-identical; if the successor
  schema needs a different id prefix, change only `id` and leave the text as is.
- The second fenced block is an **observations** array, not rows. Ca06/integrator decides
  whether to mint `manifest-round-key-not-unique` and `r46-validator-keys-s1-by-lane-rounds`.
- The parent `reports/round-40/op/defect-queue-v2.json` must stay byte-identical at
  `sha256 dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907`
  (pin recorded at `reports/round-43/calib/defect-queue-v2-successor-r43.json:7`). Re-run
  `sha256sum` before and after assembly; a mismatch means the parent was edited in place.

## 9. Boundary

- Only `reports/round-47/calib/Ca03-manifest-schemas.md` written.
- No filed byte edited (`reports/round-1..46/**`, `corpus/lessons/*.md`,
  `tools/gates/frozen/**`, fleet `.ufo/**` untouched); no corpus staging; no round runner
  executed; no git commit/push; no network or install.
- The ledger and protocol files are siblings and were read only.
- Unknowns: whether the S2 shape is a recorded amendment (`to-verify`, §5 T6). No other
  unverified assertion is made; all counts above are command output.
