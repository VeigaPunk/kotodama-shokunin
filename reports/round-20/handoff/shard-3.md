# shard-3 — v2-subset equality: the 15 v2 rows carried verbatim (R20-D05..D12)

- topic: the v3 ledger's 15 v2 claim rows are read from the filed v2 machine
  twin with the same reader the judges use and carried verbatim; the exercise
  proves it on the delivered bytes.
- date: 2026-10-18.

## 1. Mechanism

- Source: `reports/round-15/handoff/packet-v2-05.yml` (the v2 machine twin),
  parsed by `tools/harness/packet_uncertainty.py`'s own `read_packet` /
  `packet_sections` (via `runpy`) — the same reader the harness judges with.
- Carried fields per row: `claim_id`, `claim_kind` → `kind`,
  `evidence_status`, `uncertainty.status` → `uncertainty_status`,
  `uncertainty.basis` → `uncertainty_basis`, `links` (path#token specs,
  unchanged), `statement` → `statement`.
- The v2 twins are digest-pinned in the v3 baseline, and the exercise
  recomputes the normalized subset digest from the delivered ledger and
  compares it with the frozen value (`v2_subset_digest`).

## 2. Measured

```sh
export TMPDIR=$PWD/.scratch
python3 tools/exercise-handoff-e2e.py --profile v3 --quiet
# -> handoff-v3: exit=0 … v2_subset=equal …
```

- The 15 rows: `D2-CL01`, `D2-CL02`, `CL01`–`CL13` — statuses 8 supported /
  5 partial / 2 unresolved, exactly as filed in v2.
- `v2_subset_digest = ad35c860acf3b452c6f8974cd08a8333fa1ffd7758b371c12123b6437bde069b`
  (recorded in `reports/round-20/handoff/expected.json`).
- Control **m8** (selftest): re-typing one v2 row in an isolated copy →
  `exit 1 E2E-DIGEST` (the v2 twin digest is pinned; the subset equality is
  additionally enforced on the parsed rows).

## 3. Why this matters

- The round-12 reject was about semantics, not shape; carrying the v2 rows
  verbatim (rather than re-typing them in v3) keeps the v2 census auditable
  inside the v3 packet and makes any silent re-typing a stable `E2E-DIGEST`.
- The v3 packet's `validation` section carries the subset-equality row with
  the normalized digest prefix.
