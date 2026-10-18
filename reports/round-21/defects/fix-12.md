# R21-O12 — R20 fragment-index collision

- **Disposition:** open; preserve both indexes and route canonical-pointer choice to R22.
- **Finding:** `reports/round-20/fragment-index.md` and `reports/round-20/fragment-index-x24.md` coexist. X24's path note states that both seats produced an index and that the parent owns the canonical choice; neither index claims to settle the other.
- **Control:** the X24 index embeds a stdout-only inventory check and negative controls. Its recorded run on 2026-10-18T13:28:33Z (`python3 -B - <<'PY'`, `reports/round-20/fragment-index-x24.md` §Index verification) reports `indexed=72 observed=72`, `unindexed=[]`, `unavailable=[]`, and `INDEX_CONTROL=PASS`; in-memory duplicate, dropped-row, and missing-path cases were rejected.
- **Bounded action:** keep both snapshots intact. R22 parent/integrator selects or generates a canonical index pointer and refreshes it after the final artifact set settles; do not delete or rewrite the peer-owned index.
- **Limit:** X24's test proves only its own snapshot's inventory/shape at the recorded time. It does not establish which index is authoritative.
