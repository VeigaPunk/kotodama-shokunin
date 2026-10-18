# shard-5 — claim-to-record links and the atomic edge table (R20-D05..D12)

- topic: every claim row carries machine-checkable `path#token` links, and the
  coupling edges are atomic rows with claim back-links — the round-12 findings
  closed inside the exercise, extended to D4.
- date: 2026-10-18.

## 1. Links (105 specs, all resolved)

- The 15 v2 rows carry their filed v2 link specs unchanged; the twelve D4 rows
  carry `claims-map.md`'s specs; both are written fully qualified
  (`path` or `path#token`), never shorthand.
- The exercise's preflight enforces: every row has ≥1 link; every link parses;
  every named path is a file of the v3 read set (`E2E-LINK` otherwise) —
  control **m7** fires on a path outside the read set.
- The authoritative resolution is the harness: the machine twin (re-parsed
  from the delivered Markdown) is judged by `tools/harness/packet_links.py
  --repo-root <repo>`.

```sh
export TMPDIR=$PWD/.scratch
python3 tools/exercise-handoff-e2e.py --profile v3 --quiet
# -> … links=105/105 … findings=0
```

- 105/105 resolved, zero findings. Control **m6**: a dangling selector
  (`packet.d4.yml#ER-99`) in the twin → harness exit 1 with
  `L-TOKEN-MISSING`.

## 2. Edges (88 atomic rows)

- The 34 v2 rows (BR01–BR05, D2E-01..29) are carried verbatim from the v2
  machine twin — the D2 coupling notes stay one edge per record, the round-11
  aggregate row stays gone.
- The 54 D4 rows are one atomic row per live relation, measured from the
  packet bytes at assembly time:
  - costume→form-slot 6, costume→material_ref 6, rank rule→wearer ranks 4,
    era→costume seam 4, borrowed label→layer 6, name→formation/bases 8,
    symbol→era 8, festival/rite→calendar 10, contact→layer route+loans 2.
  - Every source and target resolves through the twin's record index; the
    D2/D4 index extras (`A-03`, `R-01`, `R-03`, `SYN-23`, `RG-01`.., era tags,
    rank names, layer names) are carried as the packet's own value tokens,
    never invented.
  - Derived relations say so in their `limits` cell (era→costume seam and the
    register values are derived from the records' own fields; unresolved
    mentions stay text).
- Every edge names ≥1 existing claim (`E-EDGE-NO-CLAIM` otherwise); the
  exercise's preflight enforces source, targets and claim back-links
  (`E2E-COUNT`).

## 3. Measured

- `coupling_edges` rows: **88** (34 v2 + 54 D4); `claims` back-links cover
  `D2-CL01`, `CL08`–`CL12`, `D4-CL01`–`D4-CL05`, `D4-CL07`, `D4-CL10`.
- Baseline `counts`: `edges: 88`, `d4_edges: 54`, `claims: 27`.
