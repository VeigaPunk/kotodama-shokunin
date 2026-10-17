# Round-4 AUDIT — linguistics (NON-CANON)

Snapshot: 2026-10-17T15:06:10Z; HEAD `c610e0abd8edf90d6c6d86ebebdc7a7cba8d4a0b`.
Scope: all 16 `corpus/knowledge/linguistics/*.md` entries; read-only over entries and triage ledgers. Only this report is written. All paths below are repo-relative; bare entry names are under `corpus/knowledge/linguistics/`.

## Audit rule and totals

- Required headers: nonempty `- topic:`, `- sources:`, `- couples:`; indented continuation blocks count as values. Admission context: `corpus/QUALITY.md:5-15`.
- The assignment requires a calibration **section**: a headed section containing status/limits counts, including a heading using “calibrated”; running prose alone does not. This is stricter than the current provenance gate's vocabulary/apparatus check.
- A live empirical `to-verify` flag needs a pre-existing row in a `corpus/lessons/*triage*/` ledger naming that entry and that claim. Bare and parenthesized markers both count. A row for a different claim in the same entry does not establish a basis.
- Policy/use-mention occurrences are not empirical claim flags. They are inventoried separately below, without pretending that a ledger's inventory note is a decision row.
- **Result: 14 PASS files; 2 files with defects; 2 findings.** Header findings: 0 across 48 populated fields. Missing calibration sections: 1. Unbased empirical flags: 1.
- Marker inventory: **16 occurrences on 16 lines = 4 empirical flags + 12 policy mentions**. Empirical flags: 3 have matching ledger rows, 1 has none. No flags were resolved, downgraded, or removed by this audit.
- Report data rows: **16 per-file verdict rows + 4 empirical flag-basis rows + 12 policy-mention rows = 32**.

## Per-file verdicts

Header evidence lists topic / sources / couples line numbers. Calibration evidence is the start of an actual headed section, not merely a vocabulary hit.

| Entry | Header evidence (all nonempty) | Calibration evidence | Empirical / policy markers | Verdict |
|---|---|---|---|---|
| color-terminology.md | 3 / 4 / 5 | §3 at :34; §7 at :84 | 0 / 0 | PASS |
| conlang-methodology.md | 3 / 4 / 5 | Calibration at :126 | 0 / 1 | PASS |
| historical-linguistics.md | 3 / 4 / 5 | §8 at :207 | 0 / 1 | PASS |
| kinship-terminology.md | 3 / 4–21 / 22 | §11 at :142 | 1 / 2; based at round-1-triage/L2.md:18 | PASS |
| language-contact.md | 3 / 4 / 5 | §7.2 at :93 | 0 / 0 | PASS |
| linguistic-anthropology.md | 3 / 4 / 5 | §2 at :28; §6 at :137 | 0 / 0 | PASS |
| morphological-typology.md | 3 / 4 / 5 | §10 at :99 | 0 / 1 | PASS |
| naming-systems.md | 3 / 4–33 / 34 | §8 at :122 | 1 / 1; based at round-1-triage/L4.md:26 | PASS |
| orality-formulaic-language.md | 3 / 4–25 / 26 | §10 at :137 | 0 / 1 | PASS |
| phonetics-phonology.md | 3–5 / 6–69 / 70–75 | §7 at :192, with solid/contested distinctions at :194–226 | 0 / 0 | PASS |
| politeness-taboo-euphemism.md | 3 / 4–34 / 35 | §7 at :118 | 1 / 2; occupational flag :73 lacks a matching ledger row | DEFECT — FLAG-01 |
| semantic-fields-lexicon-building.md | 3 / 4 / 5 | §5 at :81; §7 at :110 | 0 / 1 | PASS |
| semantics-pragmatics.md | 3 / 4 / 5 | No calibration heading; prose/labels at :44, :80, :97, :133 | 1 / 0; based at round-1-triage/L7.md:25 | DEFECT — CAL-01 |
| sociolinguistics-registers.md | 3 / 4–40 / 41 | §10 at :140 | 0 / 1 | PASS |
| syntax-typology.md | 3 / 4 / 5 | §5 at :90 | 0 / 0 | PASS |
| writing-systems.md | 3 / 4 / 5 | §2 at :27 | 0 / 1 | PASS |

Triage references in this table are under `corpus/lessons/`.

## Findings

1. **FLAG-01 — unbased occupational-taboo flag.** `corpus/knowledge/linguistics/politeness-taboo-euphemism.md:73` retains “occupational (hunters and fishers rename the quarry and ban boat-words; specific regional cases to-verify)”. Searches across the 87 triage ledgers present at this snapshot found no row naming this entry's occupational/regional claim. `corpus/lessons/round-3-triage/orchestrator-direct.md:10-16` names other claims in this file; :15 is explicitly the bìhuì renamed-title claim, not hunters/fishers or boat-word taboos. That row cannot be borrowed as this flag's basis. Leave the marker intact until an authorized freshness pass supplies an honest claim-specific decision and basis.
2. **CAL-01 — missing headed calibration section.** `corpus/knowledge/linguistics/semantics-pragmatics.md` contains substantive calibration prose, including the final “Calibration, plainly” paragraph at :133, but no calibration section heading. The preceding heading is §7 “Method: designing the meanings a culture actually needs” at :120. This is a section-form defect under the assignment, **not** a claim that calibration content is absent. A future authorized fix can retain the prose and expose the calibration as a section; this audit changes nothing.

## Empirical flag-basis audit (4 rows)

These are basis-presence findings, not fresh verification of the cited scholarship. Decisions below are historical ledger decisions, not new dispositions.

| Entry and live line | Flag summary | Matching ledger row / basis | Result |
|---|---|---|---|
| kinship-terminology.md:125 | “Brides carry terms with dowries” as a borrowing vector | `corpus/lessons/round-1-triage/L2.md:18` — DOWNGRADE: neighboring-language borrowing has cited cases, but the bride-borne vector could not be verified; the narrower marker is deliberately retained. | BASED; unresolved |
| naming-systems.md:103 | Specific role of kotoage in norito liturgy | `corpus/lessons/round-1-triage/L4.md:26` — DOWNGRADE: no norito attestation located; distinguishes Man'yōshū attestations from the unsupported liturgy attribution. | BASED; unresolved |
| politeness-taboo-euphemism.md:73 | Regional occupational taboos: hunters/fishers rename quarry and ban boat-words | No matching claim-specific row; `corpus/lessons/round-3-triage/orchestrator-direct.md:15` concerns bìhuì, not this claim. | UNBASED — FLAG-01 |
| semantics-pragmatics.md:49 | Royen (1929) attribution that all languages classify nouns | `corpus/lessons/round-1-triage/L7.md:25` — new flag inserted: attribution could not be confirmed from accessible sources; Aikhenvald 2000 full text was unavailable and a library check of pp. 1–2 was requested. | BASED; unresolved |

## Policy/use-mention inventory (12 rows)

No empirical assertion is being flagged at these locations. Evidence distinguishes an actual policy row from prose inventory/notes; missing policy decision rows are not silently counted as empirical bases.

| Entry and line | Why this is a policy mention | Existing triage record |
|---|---|---|
| conlang-methodology.md:124 | Citation-norm rule names the literal tag | `corpus/lessons/round-1-triage/L1.md:17` — explicit rule-reference row |
| historical-linguistics.md:85 | Instruction to mark contested laws in future handoffs | `corpus/lessons/round-1-triage/L2.md:24` — explicit no-claim note, not a decision row |
| kinship-terminology.md:136 | Handoff instruction to flag unresolved items | `corpus/lessons/round-1-triage/L2.md:7-9` — rule/pointer inventory, not a decision row |
| kinship-terminology.md:157 | Handoff format includes flagged items | `corpus/lessons/round-1-triage/L2.md:7-9` — rule/pointer inventory, not a decision row |
| morphological-typology.md:116 | Instruction to preserve future contested-claim markers | `corpus/lessons/round-1-triage/L4.md:6-8` — template-text inventory, not a decision row |
| naming-systems.md:134 | Canon-boundary handoff instruction | `corpus/lessons/round-1-triage/L4.md:6-8` — template-text inventory, not a decision row |
| orality-formulaic-language.md:151 | Canon-boundary handoff instruction | `corpus/lessons/round-1-triage/L5.md:23-25` — standing-rule note, not a decision row |
| politeness-taboo-euphemism.md:114 | Handoff instruction to flag unresolved items | `corpus/lessons/round-3-triage/orchestrator-direct.md:16` — policy row covering two lines |
| politeness-taboo-euphemism.md:133 | Canon-boundary handoff instruction | `corpus/lessons/round-3-triage/orchestrator-direct.md:16` — same two-line policy row |
| semantic-fields-lexicon-building.md:116 | Checklist instructs future lexicons to mark unverifiable etymologies | `corpus/lessons/round-2-triage/L12.md:6-10` — explicit instruction-only inventory, not a decision row |
| sociolinguistics-registers.md:155 | Canon-boundary handoff instruction | `corpus/lessons/round-1-triage/L7.md:7-10` — explicit rule-sentence inventory, not a decision row |
| writing-systems.md:149 | Conscript checklist names the lane's marker rule | `corpus/lessons/round-1-triage/L8.md:6` — explicit lane-rule inventory, not a decision row |

## Verification and caveats

- Read all 2,492 entry lines in windows of at most 120 lines. Inspected the relevant linguistics triage records and searched all `corpus/lessons/*triage*/` ledgers by filenames and flag subjects; 87 candidate ledgers existed at the snapshot, including round-4's unrelated `frozen-run-standard.md`.
- Unchanged scanner command: `python3 tools/gates/provenance-audit.py corpus/knowledge/linguistics` — exit **0**; final output `INFO scan: files=16 marks=16 mark-lines=16 findings=0 blocked=0`.
- Independent streaming header/heading inventory: `files=16 header-fields=48 header-defects=0 calibration-heading-files=15 missing-calibration-sections=1 marks=16 triage-ledgers=87`. Manual reading confirmed that the headed sections contain calibration material.
- Gate result is **not** this audit's verdict: `tools/gates/provenance-audit.py:298-331` does not require a calibration heading or inspect triage bases; :14–23 explicitly permits calibration vocabulary/prose. Its zero findings do not clear CAL-01 or FLAG-01. Gate code and fixtures were not edited; selftests that regenerate fixtures were not run.
- `git diff --exit-code HEAD -- corpus/knowledge/linguistics` — exit **0** before report creation. No entry, ledger, gate, LOG.md, or other worker's report was edited; no git commit was made. Round-level LOG bookkeeping is left to the parent because this assignment permits only the named report.
- PASS means conformance to these three audit checks only, not validation of every real-world citation or claim. Ledger basis existence is not proof that a disputed claim is true. No external source was newly verified and no uncertainty was promoted to fact. All material remains NON-CANON; lore-shokunin owns canon.
