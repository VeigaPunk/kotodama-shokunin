# Round 58 — `## Mistakes` draft (ScribeMistakes58)

Draft rows for `corpus/lessons/round-58.md`:

| id | class | evidence pointer | captured-by | fix |
|---|---|---|---|---|
| R58-M1 | rejection-rationale calibration — the stated reason for not registering a source was false twice: round 56 said koon1244 had no quotable passage although its JSON/N3 exposed quotable fields; round 57 said CODH quotes were below the 8-word floor although four quotes locate | `corpus/lessons/round-56-verifier-spotcheck.md:129`; `corpus/lessons/round-57-verifier-spotcheck.md:169,203`; original reasons `corpus/lessons/round-56.md:83` and `corpus/lessons/round-57.md:92` | None at the time of either decision. Current draft `corpus/QUALITY.md:41`, criterion 12, now requires a named re-test tool and its verbatim output for measurable or tool-checkable rejection reasons. | Apply criterion 12 before filing each such reason. Failing historical fixture: run `python3 -B reports/round-57/reopen-quote.py <CODH URL> '<one of the four scout quote inputs>'` on the `/bukan/` and `/han/H236/` candidates. The non-author spot-check records `LOCATED` for all four, normalized lengths 11/10/15/11; the old “below 8 words” reason must fail that comparison. The same check must reject the round-56 “no quotable passage” explanation when the koon1244 JSON/N3 fields are supplied. The quoted CODH literals are not reproduced in the lane lesson; this is the prior closure's recorded result, not a fresh replay. |
| R58-M2 | report arithmetic — round 57's report said S413–S454 were tier A 34 / B 8; committed rows are A 36 / B 6 | `corpus/lessons/round-57-verifier-spotcheck.md:75-78,211`; report `.ufo/reports/round-57/kotodama.md:36` | None identified; the closure explicitly classed this as a report-only numeric defect, not a claim-counter error. | Derive report tallies from the committed registry range and assert them rather than transcribing them. Shown able to fail: the tier-count command below returns A 36 / B 6; an assertion against the stale report input A 34 / B 8 exits 1 (output below). |
| R58-M3 | prompt provenance, recurring and status-neutral — the lane identity committed the dispatched prompt in both rounds 56 and 57, rather than the integrator | `corpus/lessons/round-56-verifier-spotcheck.md:22-23` (commit `2075410`); `corpus/lessons/round-57-verifier-spotcheck.md:20,30-31` (commit `698531c`) | None identified; both closures recorded the mismatch as status-neutral, with no authorship assertion cited. | Add a closure assertion that the dispatched-prompt commit is authored by the named dispatcher/integrator, not the lane identity. Shown able to fail: test the old prompt commits `698531c` and `2075410`; the guard rejecting author `kotodama-shokunin` exits 1 for both (command and output below). |

## Count and failure evidence

Required tier count (the pipeline ran under `timeout 900`):

```text
awk -F'|' '/^\| S4(1[3-9]|[2-4][0-9]|5[0-4]) /{print $5}' /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md | sort | uniq -c
     36  A 
      6  B 
```

Stale-count assertion, input = S413–S454 in `corpus/SOURCES.md`, expected = the report's A34/B8. It exited 1 as intended:

```text
timeout 900 awk -F'|' '/^\| S4(1[3-9]|[2-4][0-9]|5[0-4]) /{t=$5; gsub(/^[ \t]+|[ \t]+$/, "", t); n[t]++} END {printf "observed A=%d/B=%d; old report A=34/B=8\n", n["A"], n["B"]; if (n["A"] != 34 || n["B"] != 8) exit 1}' /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md
observed A=36/B=6; old report A=34/B=8
exit 1
```

Prompt-author guard, input = the two prompt commits; it exited 1 as intended:

```text
timeout 900 bash -c 'bad=0; for c in 698531c 2075410; do author=$(git -C /home/vgpnk/Projects/shokunin show -s --format=%an "$c") || exit; printf "%s %s\\n" "$c" "$author"; if [ "$author" = kotodama-shokunin ]; then bad=1; fi; done; exit "$bad"'
698531c kotodama-shokunin
2075410 kotodama-shokunin
exit 1
```

A first draft of the tier assertion did not trim whitespace around the registry's tier cell and printed 0/0; the corrected assertion above trims the field and gives 36/6. M1's `LOCATED` results are inherited from the non-author spot-check; I did not rerun source retrieval or the locator merely to decorate this report.

## Scope and evidence status
- **Axis:** calibration (the judged axis).

- **Behavior:** supplies three lesson rows with explicit capture rules and falsifiable fixtures.
- **Gates:** the requested count was run; the stale-count and prompt-author guards were run and returned the expected failure status. No round acceptance predicate, build, or test suite was run. M1's locator evidence is from the cited prior closure, not this session.
- **Touched surface:** this report only. No lesson, source registry, QUALITY rule, product code, or judge was edited by this seat. Read-only evidence came from the two verifier spot-check lessons, the current QUALITY criterion text, `SOURCES.md`, and prompt commit metadata.
- **Out of scope:** no edits to the actual `## Mistakes` section and no external source fetches.
- **Artifact:** `reports/round-58/ScribeMistakes58.md` (the supplied `.ufo` destination is outside this seat's lane write boundary).
- **Installs:** none.
