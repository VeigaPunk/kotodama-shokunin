# Quarantine slice cross-check

Re-derived from read-only `/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md` using the exact requested awk:

```sh
awk -F'|' -v l='kotodama' '$2 ~ ("`" l "`") && $3 ~ /round[0-9]+/ && $4 ~ /S[0-9]+/ {print $3, $4, $5}'
```

The command emits **21 rows**: **18 `payload-absent`** and **3 unreachable** (register wording: cited source could not be fetched, so no quote was checked). This agrees with the 21-row slice and class split declared in frozen `reports/round-71/claims.json` item10 (lines 71–75). `payload-absent` denotes candidates whose relevant sources fetched but whose quote did not match; it is not itself a final hand-verification verdict. `unreachable` is explicitly not a fabrication verdict (register lines 6–14, 256–264).

## Random three-row registry cross-check

Sample selection: Python `random.seed(71)` followed by sampling three of the exact awk output rows. In the lane registry, status and teaches are taken from the matching `SOURCES.md` row. “Exists” means a row with that ID was found in the registry.

| Slice row | Class | Registry row exists? | Status | Teaches |
|---|---|---:|---|---|
| round4 / S814 | payload-absent | Yes | mined | Paracelsus: chemical and magical cures vs Galenic medicine |
| round5 / S825 | payload-absent | Yes | mined | Epidaurian iamata stelae and abaton dream incubation |
| round1 / S776 | payload-absent | Yes | mined | mancala family distribution and sowing gameplay |

Evidence: `corpus/SOURCES.md` rows S814 (line 768), S825 (line 779), S776 (line 732); their complete rows include status `mined` and the stated teaches fields.

## Cross-check discrepancy observed

A separate all-IDs existence scan found **S778** from the 21-row slice has no matching row in current `corpus/SOURCES.md` (searched neighboring S770–S782 and exact `S778`; registry goes S776 then S779). This does not alter the requested random-three result or the defect-register count, but is a concrete registry discrepancy to reconcile. The remaining 20 slice IDs were found. No tools were installed.
