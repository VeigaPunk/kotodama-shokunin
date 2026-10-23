# MutCounterO — ACCEPT-O-62 pre-data counter robustness

## Scope and axes

- Axes: detector soundness; deterministic/reproducible fixtures; bounded execution; isolation and exact restoration.
- Read claims.json and round-61-verifier-spotcheck.md §7 before the counter. Frozen revision: `f0173481047a93c46798f90b68d71d4f169d2642`.
- Isolated clone: `/fast/scratch/hyaku/kotodama-r62/MutCounterO/clone`.
- Frozen counter SHA-256: `bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551` (matched the task).
- Exactly one counter mutation: disable the ORDER predicate at accept-o.py:327, only in `/fast/scratch/hyaku/kotodama-r62/MutCounterO/PROBE/accept-o.py`. No lane source/counter/tool was edited. This report is the only lane write.
- No installs, live fetching, subagents, background jobs, or integration/ship actions. All external commands were timeout-capped at at most 900 seconds.

## Single mutation probe

### Fixed control and expected detector

`/fast/scratch/hyaku/kotodama-r62/MutCounterO/reference.py` is a standalone, real-fetching control, copied unchanged to the clone's `tools/reopen-row.py`. It implements the row/fetch/caption contract but deliberately reverses collected results; its direct refusal-only branch keeps argument order. This models an ordering bug in fetched-result collection, not a tool keyed to fixture IDs/classes. It imports no counter and names none of the INDEP-forbidden strings. Its SHA-256, unchanged across the three runs, is:

`ac0ee9e27472b057def4bfa6fce756f67a0e0e4c9981994e54aee8ef033be155`

The same bounded behavioral detector was used for pristine, mutated and restored bytes:

`/fast/scratch/hyaku/kotodama-r62/MutCounterO/detector.py`

SHA-256: `3763caa0a407778c21270ebf1641670a4da6cec55d4bfebe7b36c36b94952451`.

It runs the counter against this fixed clone tool, expects counter exit 1 with **ORDER as the only failing leg**, and calls that `DETECTOR: PASS`. Acceptance of the bad-order control is `DETECTOR: FAIL`; unrelated failures are `INCONCLUSIVE`. Thus the baseline is a passing rejection detector, not an inconclusive baseline failure. Each full counter run generated its own random fixture as the frozen counter requires; control/detector bytes were fixed.

The detector invokes a fresh process group with `timeout --kill-after=5 880`, waits at most 890 seconds, and kills/reaps its process group even on exceptions. Its own invocation was capped at 895 seconds. `TMPDIR` was `/fast/scratch/hyaku/kotodama-r62/MutCounterO/runtime`, so counter-created files also stayed inside the seat scratch.

### Actual mutation diff (PROBE only)

```diff
@@ -324,7 +324,7 @@
         summary = f"REOPEN: {located}/{len(expect)} located"
         leg("GEN", not wrong and summary in out.splitlines(),
             f"rows={len(expect)} wrong={len(wrong)} {wrong[:6]} summary_ok={summary in out.splitlines()} exit={code}")
-        leg("ORDER", [s for s, _, _ in got] == ids, f"printed={len(got)} expected={len(ids)}")
+        leg("ORDER", True, f"printed={len(got)} expected={len(ids)}")
         bound_bad = []
         for sid, cls in expect:
             if cls in ("NOROW", "DEAD_PORT"):
```

The actual `diff -u` exited 1 (one differing line). Mutated counter SHA-256:

`b9117a54a511faaf14f441158b7203457903d386eec6c9eee15814e5b3fe88ca`.

### Run 0 — frozen no-tool control

Command, from the frozen clone: `timeout 900 python3 -B reports/round-62/accept-o.py`.

Full stdout and actual exit:

```text
TOOL FAIL path=tools/reopen-row.py exists=False
INDEP FAIL no tool
GEN FAIL no tool
ORDER FAIL no tool
BOUND FAIL no tool
EXIT FAIL no tool
PRIV FAIL no tool
DEFAULT FAIL no tool
ERR FAIL no tool
ACCEPT-O-62: FAIL
exit=1
```

RECEIPT MutCounterO/no-tool counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=TOOL,INDEP,GEN,ORDER,BOUND,EXIT,PRIV,DEFAULT,ERR

### Run 1 — pristine exact frozen bytes, reverse-order control

Counter invocation: `python3 -B /fast/scratch/hyaku/kotodama-r62/MutCounterO/PROBE/accept-o.py --root /fast/scratch/hyaku/kotodama-r62/MutCounterO/clone`, under the detector's timeout.

Full counter stdout:

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER FAIL printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S8421', 'REFUSED', 0), ('S2790', 'REFUSED', 0), ('S3572', 'REFUSED', 0)]
DEFAULT PASS rows=[('S3485', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
```

Counter exit 1; stderr empty. Detector wall 150.905 s, `DETECTOR: PASS`, detector exit 0. Counter hash before/after both frozen hash.

RECEIPT MutCounterO/reverse-pristine counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=ORDER

Raw detector record: `/fast/scratch/hyaku/kotodama-r62/MutCounterO/pristine-output.txt`.

### Run 2 — ORDER-disabled PROBE (not frozen control credit)

Same detector, invocation, tool and bounds; only counter line 327 changed.

Full counter stdout:

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S2861', 'REFUSED', 0), ('S4017', 'REFUSED', 0), ('S2229', 'REFUSED', 0)]
DEFAULT PASS rows=[('S1687', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
```

Counter exit 0; stderr empty. Detector wall 151.359 s, `DETECTOR: FAIL`, detector exit 1. Counter hash before/after both mutated hash.

PROBE-RECEIPT MutCounterO/reverse-order-disabled counter-sha256=b9117a54a511faaf14f441158b7203457903d386eec6c9eee15814e5b3fe88ca rev=f0173481047a93c46798f90b68d71d4f169d2642 probe=PASS exit=0 stopped-by=-

This run is explicitly **not** a receipt under the frozen counter and does not establish CONTROL-MET. It demonstrates exactly which control the weakened counter admits: reversed fetched-result output with the private-refusal path still ordered. General reversal of *all* output would also be stopped by PRIV's separate ordered comparison at lines 360-362; that general control was not run here.

Raw detector record: `/fast/scratch/hyaku/kotodama-r62/MutCounterO/mutated-output.txt`.

### Run 3 — restored exact frozen bytes

Same detector, invocation, tool and bounds after putting the exact original line back.

Full counter stdout:

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER FAIL printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S3932', 'REFUSED', 0), ('S2329', 'REFUSED', 0), ('S1354', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2031', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
```

Counter exit 1; stderr empty. Detector wall 152.489 s, `DETECTOR: PASS`, detector exit 0. Counter hash before/after both frozen hash.

RECEIPT MutCounterO/reverse-restored counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=ORDER

Raw detector record: `/fast/scratch/hyaku/kotodama-r62/MutCounterO/restored-output.txt`.

### Verdict and restoration

**Counter mutant KILLED:** pristine rejection detector PASS → ORDER-disabled detector FAIL (bad tool accepted) → restored detector PASS. All other acceptance legs passed in all three runs. This is evidence that ORDER is necessary and functioning in the frozen counter, not a surviving mutation or a frozen false acceptance.

NONE-MET MutCounterO/no-tool — frozen TOOL stops it; no counter change needed.

NONE-MET MutCounterO/reverse-order — frozen ORDER stops `/fast/scratch/hyaku/kotodama-r62/MutCounterO/clone/tools/reopen-row.py`; retain the line-327 ordered-ID comparison. The one-line PROBE weakening makes this control pass, but does not count as meeting the frozen control.

Observed final restoration evidence:

```text
exact-byte-restoration=True
frozen-clone-unchanged=True
control-unchanged=True
bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551  clone/reports/round-62/accept-o.py
bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551  PROBE/accept-o.py
ac0ee9e27472b057def4bfa6fce756f67a0e0e4c9981994e54aee8ef033be155  clone/tools/reopen-row.py
```

The runtime directory was empty after the runs; all three counter server threads exited with their processes, and the detector killed/reaped its own remaining process group. No process/service was intentionally left running. Total measured span of the three probes, including intervening edit/diff operations: 508.093 s. Scratch artifacts are retained as evidence, not installed in the lane.

## Concrete robustness findings (frozen accept-o.py line numbers)

These are read-only source/fixture findings, **not additional mutation probes or claims of observed frozen acceptance**. Where a counter outcome is not exercised, it is explicitly inference.

### 1. DEAD_PORT is racy and its connection-attempt bound is self-reported

- Lines 160-165 bind an ephemeral port, close the socket, then return the now-unreserved port. Lines 302-307 insert it into a later fixture run. Another process can acquire it before/during the tool invocation.
- A bounded diagnostic actually rebound and listened on the returned address immediately: `DEAD_PORT_IMMEDIATE_REBIND=SUCCESS`. This demonstrates the reservation gap, not an observed full-run race failure.
- [INFERENCE] If another service returns 404, a compliant tool stops after one attempt, while GEN at line 319 requires UNREACHABLE/9. If a listener stalls, the timeout/retry path changes as well. A loaded multi-seat host increases opportunity, though no frequency was measured.
- Lines 330-331 deliberately skip DEAD_PORT in BOUND; its nine connection attempts are verified only by the tool's printed integer (lines 319-323). [INFERENCE] A tool that reports nine without making nine refused connections can pass this part.
- Small repair: keep a socket bound but non-listening until fixture cleanup to reserve the port; distinguish self-reported counts from independently observed counts. Do not claim that server HTTP hit counts prove failed connection attempts.

### 2. ThreadingHTTPServer: isolation/counting is sound; load sensitivity remains

- Lines 115-118 lock each hit increment and route lookup together. Different counter processes bind their own port at line 135. No shared-hit-counter race or fixed-port collision was found.
- Actual Python 3.14.8 values in this environment: `request_queue_size=5`, `daemon_threads=True`, `block_on_close=True`.
- [INFERENCE] A tool that fetches many independent rows concurrently can overflow/back up the small accept backlog or experience scheduling/timeout pressure. Legitimate additional connection attempts then conflict with fixed GEN counts even when eventual server hit counts agree. No saturation test was run; the three serial-control runs had no such failure.
- Lines 137 and 151-153 do not retain/join the serve_forever thread. Normal shutdown was observed to clean up here. A server thread is not an orphan *server process*: it dies when its counter process exits. Raising the backlog and explicitly owning/joining the server thread would make fixture lifecycle less implicit without changing request expectations.

### 3. BODY_SPLIT markup is demonstrably unbalanced

- Line 182 opens `<em>` once but joins each later word with `</em> — <b>` and ends with only one `</b>`.
- The deterministic diagnostic (`diagnostics.py`, seed 6201) observed six unmatched `</em>` endings under `<b>` and an unclosed `<b>` at the `</span>` boundary:

```text
BODY_SPLIT_MISMATCHES=[('em', 'b'), ('em', 'b'), ('em', 'b'), ('em', 'b'), ('em', 'b'), ('em', 'b'), ('span', 'b')]
BODY_SPLIT_OPEN_AT_END=[]
```

- This is a fixture-construction defect, not evidence that this fixture necessarily changes the correct text verdict: all the words remain ordinary text, and this control parsed them successfully. [INFERENCE] It adds HTML-repair behavior to what is intended as an inline-text-normalisation test. Use balanced per-word wrappers instead; do not alter LOCATED expectations to accommodate a bad parser.

### 4. `content` is never covered; `title` coverage is random; head `<title>` is untested

- Contract lines 19-20 explicitly name `content`, `title`, all `data-*` attributes, and caption class **or id**. Line 189 samples only `alt`, `title`, `data-img-description`, `aria-label`; `content` is absent. Line 193 uses class only, never an id. These are definite fixture coverage gaps.
- The bounded diagnostic observed the complete four-member attribute set across 100 builds: `['alt', 'aria-label', 'data-img-description', 'title']`.
- Only two CAP_ATTR rows are generated (line 290), so a missing-title implementation avoids any title challenge with probability `(3/4)^2 = 0.5625`, before considering other defects. [INFERENCE] This can make an attribute-specific defective tool's outcome random; such a tool was not run here.
- Line 157 always puts literal `t` in head `<title>`, never the quote. A `title` *attribute* and a `<title>` *element* are different. Under the literal BODY exclusion list at lines 17-20, head/title text is not excluded; do not silently infer a rendered-body rule. Add separate, deterministic cases for content attributes, title attributes, caption ids and a quote in head/title with the explicitly chosen contract verdict.
- Other declared but unsampled branches include style/noscript/template exclusions. These were inspected, not mutation-tested.

### 5. DEFAULT permits wrong defaults and has a load-sensitive wall clock

- Lines 368-371 check nine hits/printed attempts and only a total wall window `100 <= wall <= 600`; `code4` is displayed but is **not in the predicate**.
- The declared nominal timing is `3 * 2 * 5 + 2 * 60 = 150` seconds (six retry gaps plus two inter-pass gaps). All three actual runs reported 150 s and passed.
- [INFERENCE] A wrong default gap of 35 s gives `30 + 2*35 = 100` s plus normal overhead and can satisfy this check despite the required 60 s. The test also cannot establish where the waiting occurred. No wrong-default full run was performed in this seat.
- [INFERENCE] Scheduling delay can make a correct implementation exceed 600 s on a sufficiently loaded host; conversely delay can conceal short waits. The wide window reduces but does not eliminate host-load dependence.
- [INFERENCE] A default invocation that prints the expected line/counts but exits 0 or 7 can satisfy DEFAULT, contrary to the exit contract. Add `code4 == 1`; independently measure request timestamps/pass boundaries for stronger timing evidence. Any counter revision must follow the task's pre-data freeze procedure; none was made here.

### 6. Output/error parsing has additional definite blind spots

- ROWLINE captures `url=...` (line 80), but parse drops that capture (line 245), and no later leg verifies match provenance. [INFERENCE] A tool printing `url=-` for LOCATED/CAPTION_ONLY can pass these comparisons.
- GEN summary is checked by line membership (325-326), not uniqueness/final placement. EXIT's body run (347-348) checks exit/summary, not that four correct ordered ROW records were produced. These are narrower than the output contract.
- ERR line 385 accepts `REOPEN_ERROR` as a substring anywhere, rather than a line starting with it (contract lines 39-40), and checks traceback text only on stderr. [INFERENCE] Wrongly formatted errors or a traceback printed on stdout can escape this leg. Anchor the prefix and inspect both streams if revising before data.

### 7. Temporary directory and timeout cleanup are incomplete on failure paths

- `mkdtemp`, tool copy and Fixture construction are at lines 276-279 **before** the try/finally at 280. [INFERENCE] Copy/server-construction failure leaks the directory; partial constructor failure can bypass close.
- Finally calls `fx.close()` before `rmtree` (389-390). [INFERENCE] A close exception skips directory removal; `ignore_errors=True` otherwise hides removal failures. A TemporaryDirectory context plus nested resource cleanup would close these paths.
- `run_tool` at lines 231-237 uses subprocess.run's direct-child timeout, not an owned process group. [INFERENCE] A tool-spawned descendant can survive a timeout; killing the direct tool does not prove all its children stopped. This seat's outer detector owned/killed the whole counter process group, so it did not rely on this cleanup for its own safety.
- Per-call limits do not give the counter a single global 900 s limit: three ordinary runs at 900, DEFAULT at 900, and five ERR cases at 120 total up to 4200 seconds of declared sequential timeouts. The seat used an independent outer deadline. No full timeout/leak scenario was induced.

## Handoff

The assigned one-mutant probe is complete and restored. Frozen controls run here were both rejected; no frozen CONTROL-MET claim is made. The actual weakened-counter acceptance and restored rejection are fully recorded above. No contract was changed to accommodate a mutant, and no runtime installation or lane integration is proposed as already done.
