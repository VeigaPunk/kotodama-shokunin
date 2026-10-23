# Round 59 — Errata and quality drafts

**Axes:** calibration (correct the record without overstating evidence); operability (make the errata and lesson rule reproducible and falsifiable).

## Draft (a): round-59 lesson errata

These are proposed additions under `## Errata (filed bytes not rewritten)` for `corpus/lessons/round-58-verifier-spotcheck.md` §5 items 2, 3, 4, and 6. No product lesson bytes were rewritten.

- `corpus/lessons/round-58-verifier-spotcheck.md:146` (§5 item 2): **The pre-data `accept-c.py` history has six entries in the specified range, not five.** `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin log --format='%h %cI %s' 91fb8fd9^..80f48c2c -- reports/round-58/accept-c.py` lists six entries. Commit `31cf8b6` adds the TOPIC leg: `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show '31cf8b6^:reports/round-58/accept-c.py' | grep -c TOPIC` prints `0`, and `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show '31cf8b6:reports/round-58/accept-c.py' | grep -c TOPIC` prints `3`. The five-revision account omitted this pre-data TOPIC change.
- `corpus/lessons/round-58-verifier-spotcheck.md:147` (§5 item 3): **The filed `claims.json` wording conflates declaration and final freeze.** `declared_at` says “before any wave dispatch and before any seat scored”; `revision_note` says revisions were made before data but “only pre-data control seats had scored.” State separately that the initial declaration preceded control scoring, control-forced revisions followed those scores but preceded data, and the final freeze preceded data. Command used to expose both fields: `python3 -c 'import json,subprocess; lane="/home/vgpnk/Projects/shokunin/kotodama-shokunin"; raw=subprocess.check_output(["git","-C",lane,"show","80f48c2c:reports/round-58/claims.json"]); d=json.loads(raw); print("declared_at: "+d["declared_at"]); print("revision_note: "+d["revision_note"].split("Revision 1",1)[0].strip())'`.
- `corpus/lessons/round-58-verifier-spotcheck.md:149-150` (§5 item 4): **The receipt's 123/123 full-predicate failures are not 123 equivalent demonstrations of support discrimination.** Deduplicating the fixture-summary records gives 18 fixtures failing only SUPPORT; 17 of those report `no registry: FileNotFoundError`, while the remaining `.ufo/waves/round-58/support-control/fixtures/offtopic` has NOT-SUPPORTED verdicts. Report the full-predicate total separately from the per-leg split and qualify the 17 missing-registry outcomes.

  Executed count command (the exact command and output are also in `/fast/scratch/hyaku/kotodama-r59/ScribeErrataQuality59/commands.md` and `support-split-deduplicated.txt`):

  ```sh
  timeout 60 python3 -c 'import re,pathlib; p=pathlib.Path("/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-58/telemetry/controls-c.txt"); t=p.read_text(); summaries=re.findall(r"(?m)^(.+?) -> ACCEPT-C-58: FAIL failing=\[(.*?)\]$",t); names=list(dict.fromkeys(n for n,legs in summaries if legs == "\x27SUPPORT\x27")); blocks=re.split(r"(?m)^## ",t); byname={b.splitlines()[0]:b for b in blocks[1:] if b.splitlines()}; missing=[]; other=[]
  for n in names:
   s=next((line for line in byname.get(n,"").splitlines() if line.startswith("SUPPORT FAIL ")), "")
   (missing if "no registry: FileNotFoundError" in s else other).append(n)
  print("support_only_unique",len(names)); print("support_only_missing_registry",len(missing)); print("support_only_other",len(other)); print("missing_registry_fixtures",", ".join(missing)); print("other_fixtures",", ".join(other))'
  ```

- `corpus/lessons/round-58-verifier-spotcheck.md:152` (§5 item 6): **C's declared lands omit a path read by its acceptance counter.** At `80f48c2c`, C's land list contains only `corpus/knowledge/linguistics/toponymy-place-names.md`, `corpus/README.md`, and `corpus/SOURCES.md`; `accept-c.py` reads `.ufo/waves/round-58/support/registry.json` and reviewer `<seat>.md` files. The support input is therefore outside C's declared lands. The command used was `git show 80f48c2c:reports/round-58/claims.json` piped to JSON extraction of `claims[0].lands`, followed by `git show 80f48c2c:reports/round-58/accept-c.py | grep -nE 'SUPPORT_DIR|registry.json|report = os.path.join'`; exact output is in `undeclared-support-path.txt`.

## Draft (b): QUALITY criterion 13

Append this as a new criterion; leave criteria 1–12 unchanged:

> 13. **Unreachable live sources are handled before data** — A predicate with a live-fetch leg declares before data how an unreachable page is treated: list an archived capture of that same page in the row, or define a bounded allowance for that fetch class with its own control. This treatment is frozen and is never relaxed after data. Grounded in the round-58 verifier spot-check §5 item 5 and its S510/S511 evidence: both live pages returned HTTP 403, and the no-slack predicate failed on those fetches.

## Draft (c): mistakes rows

| id | class | evidence pointer | captured-by | fix |
|---|---|---|---|---|
| R59-M1 | provenance / stray output — the round-58 closure report's “not attributable to a round-58 seat” statement is false; the 11 lane-root files were written by cancelled seat `ExecReasonSweep58` | `.ufo/reports/round-58/kotodama.md:54`; `corpus/lessons/round-58-verifier-spotcheck.md` §5 item 1 (file headers and transcript lines 256–358) | `HyakuCloseKotodama58` spot-check §5 item 1 traced the echo headers to the seat transcript | Attribute untracked outputs from their headers and seat transcript before calling them unknown; keep outputs in the assigned wave directory or scratch. Shown able to fail: M1 probe below, with the old “not attributable” claim as input and `ExecReasonSweep58` as the evidence actor (exit 1). |
| R59-M2 | revision arithmetic — the round-58 report says five pre-data revisions and omits `31cf8b6`, which added TOPIC (`TOPIC` mentions 0 → 3) | `.ufo/reports/round-58/kotodama.md:10,20`; `reports/round-58/claims.json` `revision_note`; the history slice and TOPIC commands above | `HyakuCloseKotodama58` spot-check §5 item 2, using the history and before/after TOPIC counts | Derive the count from the specified Git history slice and report the TOPIC-changing commit, rather than copying the abbreviated revision note. Shown able to fail: M2 probe below uses stale expected count `5` against the six-entry history (exit 1). |
| R59-M3 | control interpretation — “123 controls, 0 pass” is true only as a whole-predicate result; it overstates what the controls demonstrate if read without their SUPPORT split | `.ufo/reports/round-58/kotodama.md:10,42`; `reports/round-58/telemetry/controls-c.txt`; corrected unique-fixture split above | `HyakuCloseKotodama58` spot-check §5 item 4, re-counting per-leg outcomes and missing-registry reasons | Report the whole-predicate result alongside unique per-leg counts and distinguish absent-registry failures from reviewer judgments. Shown able to fail: M3 probe below feeds the actual receipt to a guard for an unqualified aggregate; 17 missing-registry SUPPORT-only fixtures make it exit 1. |

### Failing-probe commands and observed output

These are negative consistency probes for the stale statements, not lane acceptance tests. Each was run with the cited real round-58 record as input; each expected nonzero exit is recorded.

**M1 — stale attribution input.** Command: `timeout 10 python3 -c 'import pathlib,re; p=pathlib.Path("/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/lessons/round-58-verifier-spotcheck.md").read_text(); actual=re.search(r"written by the cancelled round-58 seat \*\*(.*?)\*\*",p).group(1); input_claim="not attributable to a round-58 seat"; print(f"input_claim={input_claim!r}; evidence_actor={actual!r}"); assert input_claim == actual, "stale attribution claim does not match the evidence"'`. Input: the old report claim and the actor named in the spot-check. Output:

```text
input_claim='not attributable to a round-58 seat'; evidence_actor='ExecReasonSweep58'
AssertionError: stale attribution claim does not match the evidence
probe_exit=1
```

**M2 — stale count input.** Command: `timeout 10 python3 -c 'import subprocess; lane="/home/vgpnk/Projects/shokunin/kotodama-shokunin"; cmd=["git","-C",lane,"log","--format=%h %cI %s","91fb8fd9^..80f48c2c","--","reports/round-58/accept-c.py"]; actual=len(subprocess.check_output(cmd,text=True).splitlines()); input_expected=5; print(f"input_expected={input_expected}; observed_history_entries={actual}"); assert input_expected == actual, "stale five-entry count fails against the declared history slice"'`. Input: stale expected count `5`; history range: `91fb8fd9^..80f48c2c`. Output:

```text
input_expected=5; observed_history_entries=6
AssertionError: stale five-entry count fails against the declared history slice
probe_exit=1
```

**M3 — aggregate-only control claim.** Command: `timeout 10 python3 -c 'import re,pathlib; t=pathlib.Path("/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-58/telemetry/controls-c.txt").read_text(); summaries=re.findall(r"(?m)^(.+?) -> ACCEPT-C-58: FAIL failing=\[(.*?)\]$",t); names=list(dict.fromkeys(n for n,legs in summaries if legs == "\x27SUPPORT\x27")); blocks=re.split(r"(?m)^## ",t); byname={b.splitlines()[0]:b for b in blocks[1:] if b.splitlines()}; missing=sum("no registry: FileNotFoundError" in next((line for line in byname.get(n,"").splitlines() if line.startswith("SUPPORT FAIL ")),"") for n in names); print(f"input=reports/round-58/telemetry/controls-c.txt; support_only={len(names)}; missing_registry={missing}"); assert missing == 0, "unqualified aggregate does not distinguish missing-registry support failures"'`. Input: `reports/round-58/telemetry/controls-c.txt`; the guard's stale assumption is zero missing-registry failures. Output:

```text
input=reports/round-58/telemetry/controls-c.txt; support_only=18; missing_registry=17
AssertionError: unqualified aggregate does not distinguish missing-registry support failures
probe_exit=1
```

## Work record, gates, and limits

- **Behavior:** drafted four errata lines, one append-only QUALITY criterion, and three mistake entries with provenance and negative probes. No axis verdict or claim result was added.
- **Gates:** read-only history/receipt inspection and three intentionally failing consistency probes only. No `accept-c.py`, `rowcheck.py`, separability gate, C/D gate, build, lint, or test suite was run.
- **Touched surfaces:** only this report under the lane and scratch evidence under `/fast/scratch/hyaku/kotodama-r59/ScribeErrataQuality59/`. No product code, lesson, QUALITY, claims, telemetry, manifest, SCORECARD, or other lane/fleet file was edited. No tools were installed.
- **Limits:** the prior `ExecReasonSweep58.md` report path is absent; attribution is based on the reopened round-58 spot-check and the cited seat transcript, not a new read of the old lane-root files. S510/S511 HTTP 403s are taken from the opened round-58 verifier evidence; they were not fetched again. The first support parser double-counted repeated summary lines (36); that result was discarded and the fixture-deduplicated parse gives 18. The first combined TOPIC command was rejected by the shell parser before execution; separate before/after calls succeeded.
- **Artifacts:** this report; `/fast/scratch/hyaku/kotodama-r59/ScribeErrataQuality59/commands.md`; `revisions.txt`; `topic-before.txt`; `topic-after.txt`; `provenance-contradiction.txt`; `support-split-deduplicated.txt`; `undeclared-support-path.txt`; `m1-attribution-fail.txt` / `m1-attribution-exit.txt`; `m2-revision-count-fail.txt` / `m2-revision-count-exit.txt`; `m3-control-qualification-fail.txt` / `m3-control-qualification-exit.txt`.
