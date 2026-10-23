NONE-MET

# Records drafting — round 60 attempt 3, wave 1

**Axis:** calibration. **Scope:** byte-ready drafts for the L1; no claim or product change made by this scribe.

## Drafts

### A. `SCORECARD.md`

```md
Correction rows for round 59 (routed defects 1–3 of `corpus/lessons/round-59-verifier-spotcheck.md`; filed round-59 rows not edited):

| corrected row | correction | evidence |
|---|---|---|
| round-59 coverage row (`ACCEPT-C-59`, author-side PASS) | **MISSED** on the as-reviewed 47-row object: 14 legs PASS, but SUPPORT FAIL on S602, S616, S623 and S643 (one NOT-SUPPORTED verdict per id). The four rejected propositions were removed from the entry 12 seconds after the 03:39:56Z FAIL receipt (edit at 03:40:08Z; seven citing lines deleted; the four SOURCES rows remained filed as rejected). Run 2 at `84b931a5` also printed `ACCEPT-C-59: FAIL`, exit 1; `tail -3` cut the per-leg output, so the failing leg is not identified by the receipt. The frozen miss stands; do not score the narrowed object as the judged object. | `reports/round-59/telemetry/as-reviewed-c.txt`; `reports/round-59/telemetry/final-measures.txt` run 2; `corpus/lessons/round-59-verifier-spotcheck.md` §2 and §5 item 1; `reports/round-60/telemetry/judged-object-r59.txt` |
| separability line `C->REC via acceptance` | Annotate as a live-fetch re-run artifact, not a dependency: no `accept-c.py` leg reads a REC land, and C passed alone at `4abfb63d` before the records commit. The change across live-fetch re-runs does not establish a C→REC coupling. | `corpus/lessons/round-59-verifier-spotcheck.md` §2 (separability finding) and §5 item 3; `reports/round-59/telemetry/final-measures.txt` run 1 |
```

### B. `LOG.md`

```md
## 2026-10-23 — Round 59 correction: ACCEPT-C-59 missed on the judged object (records, not a new claim)

- **Correction to the coverage row:** record ACCEPT-C-59 as **MISSED** on the as-reviewed object, not as admitted on the later narrowed entry. The as-reviewed 47-row run at 03:39:56Z passed 14 legs and failed SUPPORT: S602, S616, S623 and S643 each received one NOT-SUPPORTED. The four rejected propositions were removed from the entry at 03:40:08Z, 12 seconds after the FAIL receipt; the diff deleted seven citing lines, while the four SOURCES rows remained filed as rejected. The frozen post-verdict miss is not cured by narrowing. Evidence: `reports/round-59/telemetry/as-reviewed-c.txt`; `corpus/lessons/round-59-verifier-spotcheck.md` §2.
- **Landed-revision re-run:** run 2 at `84b931a5` (03:51:01Z) also printed `ACCEPT-C-59: FAIL`, exit 1. The captured output was cut with `tail -3`, removing the per-leg diagnostics; the failing leg is therefore not identified here. Evidence: `reports/round-59/telemetry/final-measures.txt` run 2; spot-check §2 item 5.
- **Separability correction:** annotate `C->REC via acceptance` as a live-fetch re-run artifact. Static inspection found no REC land read by an `accept-c.py` leg; C passed alone at `4abfb63d` before the records commit. The re-run flip is not evidence of a dependency. Evidence: `corpus/lessons/round-59-verifier-spotcheck.md` §2 and §5 item 3; `reports/round-59/telemetry/final-measures.txt` run 1.
- Filed round-59 SCORECARD rows remain unchanged; this is an appended correction, not a rewrite.
```

### C. `corpus/lessons/round-59.md` erratum

```md
## Errata (filed bytes not rewritten)

- **R59-M5 (`corpus/lessons/round-59.md:120`; round-59 verifier spot-check §5 item 4):** The earlier `reports/round-59/__pycache__/` cleanup did not persist: `reopen-quote.cpython-314.pyc` and `rowcheck.cpython-314.pyc` were regenerated at 03:19:46Z and remained at round-59 closure. Round 60 removed the listed ignored caches at 2026-10-23T04:57:02Z; see `reports/round-60/telemetry/pycache-removed.txt`. The original R59-M5 line is retained; its “removed by the L1” wording applies only to the earlier cache files, not the regenerated copies.
- **Round-59 verifier spot-check §5 item 5:** `CtlKeyedLabels59` was held after a provider `cyber_policy` refusal; it was not scored and was not rerouted. Record it as an unscored/held control with that reason, not as a passed or failed control. Round 60 declares separately designed keyed controls `CtlKeyedLabelA3` and `CtlKeyedLaneA3`; this does not backfill a round-59 result. Evidence: `corpus/lessons/round-59.md` §“Pre-data control wave and revision 1”; `corpus/lessons/round-59-verifier-spotcheck.md` §5 item 5; `reports/round-60/claims.json` records item 5 and `.ufo/waves/round-60/gen-w1-a3.py` names both controls. The declaration/spec is not itself execution evidence for their outcomes.
- **Round-59 verifier spot-check §5 item 6:** `.ufo/waves/round-59/support/registry.json` labels its source “support task call (~03:40Z)”, later than the reviewer report mtimes (03:37:31Z) and the as-reviewed FAIL receipt (03:39:56Z). Treat `~03:40Z` as an erroneous chronology label, not a reliable task-call timestamp. The available record supports the source attribution (`KotodamaR59` task call; agent IDs as returned) and the separate report/receipt times only; do not invent a replacement call time. The filed registry remains unchanged. Evidence: registry.json; `corpus/lessons/round-59-verifier-spotcheck.md` §5 item 6 and §2 timestamps; `reports/round-59/telemetry/as-reviewed-c.txt`.
```

### D. `corpus/QUALITY.md` — criterion 14

```md
14. **The judged object stays frozen through adjudication** — When blind packets are built, record the exact entry-byte SHA-256 and the judged cited-id set in the packet key. At closure, compare that key with the entry at the measured revision using `python3 -B tools/check-judged-object.py --key <packet-key.json> --repo <repository> --rev <measured-revision> [--entry <entry-path>]`. Preserve the complete output and exit code: exit 1 is a measured mismatch, while exit 2 is an input error and is not a measured failure. If the bytes differ, record a miss; never delete, rewrite, re-key, or rescore rejected rows to make the narrowed object pass. The checker reports narrowed/widened ids when the key supplies a judged id set. Grounded in round-59 post-verdict narrowing (four rejected propositions removed after SUPPORT FAIL). Shown able to fail on round-59 bytes: `python3 -B tools/check-judged-object.py --key .ufo/waves/round-59/support/planted-key.json --repo . --rev d45985b2 --entry corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md` reported 47 judged ids versus 43 at the revision, narrowed ids `S602 S616 S623 S643`, `JUDGED_OBJECT: FAIL`, exit 1 (`reports/round-60/telemetry/judged-object-r59.txt`). Its recorded selftest also passes unchanged bytes, fails a one-word edit and a removed row line, and returns input error for a missing key.
```

## Evidence, gates, and limits

- **Read-only provenance:** read the declaration `reports/round-60/claims.json` first; then read the full round-59 spot-check §2 and §5, SCORECARD round-59 section, LOG round-59 section, `reports/round-59/telemetry/final-measures.txt`, the support registry, `corpus/lessons/round-59.md` (Errata and R59-M5), `corpus/QUALITY.md` criteria, `reports/round-59/telemetry/as-reviewed-c.txt`, `reports/round-60/telemetry/judged-object-r59.txt`, `reports/round-60/telemetry/pycache-removed.txt`, the named checker, and the round-60 declaration/spec references cited above. No shell, git/jj, network, build, test, install, or counter command was run by this scribe. Commands and outcomes inside the drafts are transcribed from those receipts, not this seat's executions.
- **Control status:** `NONE-MET` means no fixture was run by this scribe, so none was observed to pass while skipping the claimed work; it is not evidence that the frozen counter rejected such a fixture. No `RECEIPT` is claimed.
- **Touched surface:** only this requested report file was written. The four fenced blocks are drafts for the L1 to land; `SCORECARD.md`, `LOG.md`, `corpus/lessons/round-59.md`, and `corpus/QUALITY.md` were not edited here.
- **Known limits / out of scope:** no control fixture or candidate-build attack was run. The round-60 declaration and wave spec name `CtlKeyedLabelA3` and `CtlKeyedLaneA3`, but their outcome receipts were not in the evidence read for this records task; no execution result is asserted for them. No support review or claim verdict was performed.

**Artifact:** `.ufo/waves/round-60/w1-a3/ScribeRecordsA3.md`.
