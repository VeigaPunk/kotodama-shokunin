- Seat: Ca01 | executor | claim Ca | date 2026-10-19 | baseline 456674d

# Ca01 — N3 pin-supersession record draft

This is an inventory and draft only; no live surface was edited. K02's required pin scout is available and its four-file scope is reflected below. The current argot gate digest was independently measured with `sha256sum tools/gates/argot-derivation-gate.py` as `10c884337fbb2b8f5cc64bedb70e2ddbc34b84c17aaa29fb9be15d049b324a75`.

```json
{
  "schema": "kotodama-round-41-pin-supersession-draft-v1",
  "round": 41,
  "seat": "Ca01",
  "claim": "Ca",
  "date": "2026-10-19",
  "baseline": "456674d",
  "current_argot_gate": {
    "path": "tools/gates/argot-derivation-gate.py",
    "sha256": "10c884337fbb2b8f5cc64bedb70e2ddbc34b84c17aaa29fb9be15d049b324a75",
    "evidence": "sha256sum output at this seat; reports/round-38/validation.json:17-18 also records the landed digest"
  },
  "historical_argot_digests": {
    "r38_pre_landing": "8c7dd098d9ac76a1702ad920bedd80402960816dee64a066f7ceb5616cbdef07",
    "r30_delivered_reader": "b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb"
  },
  "live_surfaces_from_K02": [
    {
      "path": "SKILL.md",
      "current_row": {
        "locator": "SKILL.md:382-389 (old-digest occurrence at :383)",
        "text": "Worked ceiling, measured 2026-10-18T21:53:04Z with reports/round-28/ceiling/measure-ceiling.py: reader b5406bcd… over the pre-integration packet 543d68a8…; 19 legal / 8 illegal. The surrounding text says this supersedes the pre-fix reading without rewriting it.",
        "classification": "Dated historical measurement, not a current gate pin. The passage does not literally say 'historical' before the proposed delta."
      },
      "refreshed_row": {
        "action": "Use Ca02's proposed replacement block at reports/round-41/calib/Ca02-skill-delta.md:30-55; integrator applies it. Preserve the measured b5406 value as historical provenance, explicitly label it historical, and append the dated supersession below.",
        "opening_lines": [
          "Historical worked ceiling, measured **2026-10-18T21:53:04Z** with",
          "`python3 -B reports/round-28/ceiling/measure-ceiling.py`: historical reader",
          "`b5406bcd…` over the pre-integration packet `543d68a8…` finds **19 legal / 8",
          "illegal** among **27** mark-axis plain words; the named institutional",
          "abstraction set has **1 legal / 4 illegal**."
        ],
        "new_dated_supersession_row": "**2026-10-19 supersession — current gate pin.** The measurement above is a historical reading with reader `b5406bcd…`, not a claim about the current gate bytes. Current `tools/gates/argot-derivation-gate.py` bytes have SHA-256 `10c884337fbb2b8f5cc64bedb70e2ddbc34b84c17aaa29fb9be15d049b324a75` (`sha256sum tools/gates/argot-derivation-gate.py`, 2026-10-19). Any new ceiling measurement must record that reader digest alongside its packet digest, command, and date. This supersedes the live reader reference for new runs only; it does not alter the historical measurement or its filed evidence."
      }
    },
    {
      "path": "SCORECARD.md",
      "current_row": {
        "locator": "SCORECARD.md:755",
        "text": "| depth | improved (claim D) | r36 register residue landed: F-6 counters (derived_forms=8/derived_ok=8 live; corrected derived_failures formula; argot selftest 35) + the RL-8 era leg on the argot host emitting D4L-ARGOT-ERA (39/39 controls; planted-probe pipeline visibility; typed pipeline 20/20) | argot/law gates; typed pipeline; python3 reports/round-38/run-validation.py | tools/gates/argot-derivation-gate.py (sha 10c88433…); round-38 depth fragments |",
        "classification": "Already-current r38 digest prefix; it matches the measured 10c884337fbb… digest. No stale-prefix hit.",
        "refreshed_row": "Unchanged; retain the round-38 observation. No delta is proposed (Ca03-scorecard-delta.md:3-10)."
      }
    },
    {
      "path": "corpus/README.md",
      "current_row": null,
      "classification": "K02's search found no old or current digest prefix; the ordinary argot mention at line 176 is descriptive prose, not a digest pin.",
      "refreshed_row": null
    },
    {
      "path": "AGENTS.md",
      "current_row": null,
      "classification": "K02's search found no old or current digest prefix.",
      "refreshed_row": null
    }
  ],
  "round_41_claim_and_validation_cross_references": [
    {
      "path": "reports/round-41/claims.json",
      "current_row": {
        "locator": "claims.json:20,23",
        "text": "The N3 claim names 8c7dd098… / b5406bcd… / earlier as the target stale prefixes and 10c884337fbb… as the required current digest; its counting-command string names the two old prefixes."
      },
      "classification": "Task-scope identifiers, not a statement that either old digest is the current artifact pin. The declaration is itself digest-pinned by dispatch-declared.json:17-18.",
      "refreshed_row": "No edit to this dispatched claim declaration; the dated supersession is recorded in the SKILL delta and this report."
    },
    {
      "path": "reports/round-41/targets.json",
      "current_row": {
        "locator": "targets.json:23",
        "text": "K02's mission lists 8c7dd098…, b5406bcd…, and 15f8b232… as search prefixes."
      },
      "classification": "Task-scope search text, not a gate pin. The targets declaration is digest-pinned by dispatch-declared.json:21-22.",
      "refreshed_row": "No edit to this dispatched target declaration."
    },
    {
      "path": "reports/round-41/validation.json",
      "current_row": null,
      "classification": "Could not evaluate: the file was absent in the round-41 file inventory at this scan. No in-tree validation runner was executed.",
      "refreshed_row": null,
      "owner": "integrator",
      "next_touch": "If validation.json lands, scan its digest cross-references without running reports/round-*/run-validation.py."
    }
  ],
  "filed_readings_to_preserve": [
    {
      "paths": [
        "reports/round-30/validation.json:1506",
        "reports/round-30/regression.json:126",
        "reports/round-30/regression-initial.json:88",
        "reports/round-30/audit/x38-law-gate-clean-state.json:22,48,104,130",
        "reports/round-30/audit/x38-law-gate-baseline.json:20,44,98,122",
        "reports/round-30/rerun.json:116-117"
      ],
      "reading": "Filed r30 digest records quote b5406bcd… as the old argot gate pin; the r40 N3 row names these r30 digest rows as superseded.",
      "disposition": "Preserve as filed readings; never rewrite reports/round-1..40."
    },
    {
      "paths": [
        "reports/round-38/validation.json:17-18",
        "reports/round-38/depth/D07-receipt.md:59-60",
        "reports/round-40/run-validation.py:11",
        "reports/round-40/calib/Ca03-receipt.md:85",
        "reports/round-40/op/defect-queue-v2.json:352-358"
      ],
      "reading": "The r38 validation records 10c884337fbb… as the landed argot digest and explains the superseded 8c7dd098… pin; D07 records the prior b5406bcd… reader; the r40 runner's 8c7dd098… constant is explicitly ARGOT_SHA_UNUSED; r40's N3 row records the carry.",
      "disposition": "Filed historical readings and runner bytes; preserve unchanged."
    },
    {
      "scope": "Other old-prefix hits under reports/round-1..40/**",
      "evidence": "Read-only Grep over reports returned old-prefix matches in filed rounds 27-40 (including filed discussions, receipts, and validations). Every such file is protected by the no-filed-byte rule; no rewrite is proposed. The relevant r30 pin rows and r38/r40 transition records are enumerated above.",
      "disposition": "Preserve all filed round bytes."
    }
  ],
  "additional_live_corpus_mentions_outside_K02_scope": [
    {
      "paths": [
        "corpus/knowledge/linguistics/register-lexicon-ceilings.md:18-20,137",
        "corpus/knowledge/linguistics/register-strata-attestation.md:343-369,421-423"
      ],
      "classification": "These current knowledge entries quote b5406bcd… as the reader for the dated 2026-10-18 measurement. They are not in K02's four-file census scope; they read as historical measurement records, but are not uniformly prefixed with the literal word 'historical'.",
      "disposition": "No corpus edits are authorized this round. If 'every live-file row' is interpreted to include these entries, this is an out-of-scope acceptance question requiring an authorized later correction; do not silently count it as refreshed."
    },
    {
      "path": "corpus/lessons/round-28.md",
      "classification": "A filed lesson also matched the broad prefix search; protected as historical evidence and not to be edited."
    }
  ],
  "current_law_gate": {
    "path": "tools/gates/register-law-gate.py",
    "sha256": "15f8b23251ca2ad0a203bb1ed5fda2611dff9514e6a1af8120f520b1e7ec4169",
    "classification": "Separate gate digest; K02 found no in-scope hit and this gate was not touched. Do not supersede it as an argot digest."
  },
  "verification_status": {
    "K02_pin_scout": "available; its four-file census matches the independent scan",
    "Ca04_Ca05_review_of_this_record": "owed: their checks predate this file; Ca04 explicitly recorded Ca01 as absent at its final check",
    "current_round_validation": "could-not-evaluate until reports/round-41/validation.json exists"
  }
}
```

## Owed

- `reports/round-41/validation.json` — absent at inventory; integrator to re-scan if it lands, without executing any in-tree round runner.
- `reports/round-41/calib/Ca04-verify.md` and `Ca05-verify.md` — their current checks predate this fragment; independently re-check this record's inventory and the claims' two-verifier requirement after it lands (`Ca04-verify.md:10-12`; `Ca05-verify.md:9-11`).
- Corpus knowledge references listed in the JSON — scope is `to-verify` if the claim is intended to include them; no corpus edits are allowed this round.

## Citations

- `reports/round-41/scout/K02-pin-scout.md:5-10,18-23` — binding four-file pin census, classifications, and exact current gate digest output.
- `SKILL.md:382-398`; `SCORECARD.md:746-755` — current rows and historical/current classifications.
- `reports/round-41/calib/Ca02-skill-delta.md:5-55`; `Ca03-scorecard-delta.md:3-10` — exact proposed SKILL replacement/supersession and unchanged SCORECARD row.
- `reports/round-41/claims.json:19-24`; `reports/round-41/targets.json:21-24`; `reports/round-41/telemetry/dispatch-declared.json:15-22` — claim/target scope text and digest-pinned declarations.
- `reports/round-38/validation.json:17-18`; `reports/round-38/depth/D07-receipt.md:59-60`; `reports/round-40/calib/Ca03-receipt.md:85`; `reports/round-40/op/defect-queue-v2.json:352-358` — r38/r40 N3 transition and filed readings.
- `reports/round-30/validation.json:1506`; `regression.json:126`; `regression-initial.json:88`; `audit/x38-law-gate-clean-state.json:22,48,104,130`; `audit/x38-law-gate-baseline.json:20,44,98,122`; `rerun.json:116-117` — protected r30 pin rows.
- `reports/round-40/run-validation.py:11` — protected unused `8c7dd098…` constant; the runner was not executed.
- `corpus/knowledge/linguistics/register-lexicon-ceilings.md:18-20,137`; `register-strata-attestation.md:343-369,421-423`; `corpus/lessons/round-28.md` — broader read-only matches outside K02's scope; no corpus changes.
- Command output: `sha256sum tools/gates/argot-derivation-gate.py` → `10c884337fbb2b8f5cc64bedb70e2ddbc34b84c17aaa29fb9be15d049b324a75`.
- Command output: read-only Grep `8c7dd098|b5406bcd|15f8b232|10c884337` over `SKILL.md`, `SCORECARD.md`, `corpus/README.md`, `AGENTS.md`, and `reports/round-41`; K02's separately recorded four-file search agrees. `ls reports/round-41` showed no `validation.json` or `run-validation.py`.
