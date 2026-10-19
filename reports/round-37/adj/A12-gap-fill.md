- Seat: A12 | executor | claim A | date 2026-10-19 | baseline 57c8409

# A12 — couples fallback cross-check

**Scope.** This spare independently rechecks the `couples:` resolution leg for the eleven r35/r36 entries, with extra attention to abbreviated basename references. It does not repeat or certify A02's cross-domain-language scan, and is not a claim-A verdict (`reports/round-37/claims.json:25-30`; A12 assignment: `reports/round-37/targets.json:60`).

## Result

At baseline `57c8409`, a read-only `python3 -B` probe reproduced A02's couples totals: **334 distinct per-entry reference tokens** (319 path-resolved and 15 basename-shorthand), 0 ambiguous and 0 unresolved. Counts are summed per entry; a target repeated in two entries counts twice. The probe used the lane's established resolution order (entry directory, repo root, then `corpus/knowledge/`) and a unique-basename fallback, with `.md` token extraction and brace expansion as in the prior audit instrument (`reports/round-35/cov/C14-audit-6-10.md:239-288`; `reports/round-19/audit/entry-audit.py:74-96`).

The basename fallback is concentrated in one field, `corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md:37`. I checked its 15 unique fallback matches against the field's group labels; each matched the declared partition, not merely some same-named file elsewhere:

```text
linguistics (7): historical-linguistics.md, kinship-terminology.md,
  naming-systems.md, orality-formulaic-language.md,
  register-strata-attestation.md, semantics-pragmatics.md,
  sociolinguistics-registers.md
culture-material (6): architecture-settlement-lexicon.md,
  calendar-festival-systems.md, costume-semiotics.md,
  ritual-garments.md, sumptuary-law-rank-display.md,
  trade-economy-lexicon.md
verification (1): calibration-registry.md
synthesis (1): consistency-verification-checklist.md
```

The resolver output mapped all 15 to their matching `corpus/knowledge/{linguistics,culture-material,verification,synthesis}/` files; no group mismatch, ambiguity, or missing target was observed. This specifically reduces the risk that a permissive unique-basename fallback hides a wrong-partition target. It establishes file existence and group alignment only, not the content quality of those links or absence of bleed.

## Owed

- Integrator: use this as corroboration of the couples-resolution count and basename-group alignment only; A02's separate language scan and the complete claim-A assembly remain the relevant evidence for broader verdicts.

## Citations

- Claim-A scope and A12 assignment: `reports/round-37/claims.json:25-30`; `reports/round-37/targets.json:60`.
- A02 population, couples totals, and read-only scan output: `reports/round-37/adj/A02-entries-bleed.md:7-23,43-47`.
- Resolver conventions: `reports/round-35/cov/C14-audit-6-10.md:239-288`; `reports/round-19/audit/entry-audit.py:74-96`.
- Coupled source lines (each entry's `- couples:` field): `corpus/knowledge/culture-material/agrarian-field-system-lexicon.md:8`; `corpus/knowledge/culture-material/bathing-and-body-hygiene.md:7`; `corpus/knowledge/culture-material/fire-fuel-light.md:17`; `corpus/knowledge/culture-material/funerary-material-culture.md:39`; `corpus/knowledge/culture-material/furniture-interior-lexicon.md:14`; `corpus/knowledge/culture-material/writing-media-surface-economy.md:29`; `corpus/knowledge/culture-material/timekeeping-instruments.md:7`; `corpus/knowledge/myth-symbol/binding-speech-complex.md:34`; `corpus/knowledge/myth-symbol/death-afterlife-eschatology.md:12`; `corpus/knowledge/myth-symbol/eschatology-world-end-systems.md:16`; `corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md:37`.
- Command output, repo root, `HEAD=57c8409`, with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`: per-entry unique couples refs summed to 334; direct path matches 319; unique-basename matches 15 (all from `sacred-kingship-mythic-charter.md:37`); ambiguous 0; unresolved 0. The basename mappings are listed above. No `reports/round-*/run-validation.py`, freeze, corpus edit, or filed-round rewrite was made.
