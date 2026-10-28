# Round 77 — kotodama honest stop

## Mistakes

| id | class | evidence pointer | captured-by | fix |
|---|---|---|---|---|
| R77-M1 | calibration: the candidate Ca ledger recorded fabricated base observations and included a pair that was not red | `.ufo/waves/round-77/w2/MutCaLedger.md:43-54`; `.ufo/waves/round-77/w2/ScoutLogPairs.md:43-70` | W2 independent mutation/re-observation; the pre-freeze pair checker validated structure and execution but did not compare the recorded base observation to the executed result | Rebuild every pair from its exact stated line and a re-run observation at the pinned base; reject a pair unless its stated token differs from the observed token, and record that observed token rather than a hand-set value. Do not freeze this ledger. |
| R77-M2 | assimilation triage: one staged naming-systems artifact was omitted, one hold rationale named a nonexistent quarantine issue, and several dispositions lacked a flip | `.ufo/waves/round-77/w2/CritTriage.md:85-123,125-187` | W2 package-wide enumeration and per-disposition review | Enumerate the theme and amendments directories separately; disposition every staged artifact with its own evidence-based reason and flip before freezing the Gate. |
| R77-M3 | source attribution: the drafted entry contradicted its own D1 access record and had unlocatable or mislocated D2 wording | `.ufo/waves/round-77/w2/CritEntryQuality.md:7-33,57-65` | W2 non-author content review against the stored live source windows | Reconcile each sentence with the captured source and per-UA response; use only verbatim-locatable quotes and accurate section/page locators before admitting the entry. |
| R77-M4 | counter configuration: the claim-C README ownership exemption was a bare path and therefore carried no edited line or frozen before/after text | `.ufo/waves/round-77/w2/RevSeparability2.md:101-103` | W2 combined-read/write-set review | Require the frozen exemption object to identify the exact base line and its before/after text; verify it against base and combined trees before freezing. |

## Round status

No claim was frozen or landed. The W1 and W2 drafts remain attack artifacts, not accepted work. These findings are recorded as round lessons; no registry or knowledge-entry change was made.
