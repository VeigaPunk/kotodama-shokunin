# RevD3Evidence — attack on the D3 disposition (R65-D3: dispatch evidence)

Scope: claim **Ca**, leg **D3** only (`reports/round-66/accept-ca.py:18-21,144-154`), its receipt
(`reports/round-66/telemetry/seat-evidence.txt`), and the registry it cites
(`.ufo/waves/round-66/w1/swarm-registry.json`). Read-only; no lane mutation, no git/jj writes.
Axis: calibration. Observed at 2026-10-24 08:33–08:38 local (11:33–11:38 UTC).

**Verdict: the D3 design does not prove the ≥8 dispatched-seat floor. It proves only that a
receipt authored by the integrating seat names ≥8 existing `.md` paths. Every one of the R65-D3
failure artifacts passes it.** Detail and the falsifiers below.

## Instrument as implemented (canonical bytes)

`reports/round-66/accept-ca.py:144-154`:

```python
d3 = read(root, D3_RECEIPT) or ""
seat_paths = re.findall(r"(.ufo/waves/round-66/\S+\.md)", d3)
existing = [p for p in seat_paths if os.path.isfile(os.path.join(root, p))]
reported = len(seat_paths)
d3_ok = reported >= 8 and len(existing) >= 8 \
    and len(existing) == reported \
    and re.search(r"(?i)(seat|report|status)", d3)
```

The docstring (`accept-ca.py:18-21`) and the frozen claim text (`claims.json` Ca leg D3) promise
"names ≥8 seat report files … **with per-seat status** and **last-error text for dead seats**".
No code path parses a status line, an error line, a byte count, a timestamp, an agent id, or the
registry. The `(seat|report|status)` regex is satisfied by the receipt's own title — measured:
`re.search` matches `'seat'` at `'# seat-evidence.'`.

## Findings

### HIGH-1 — Existence is the whole test; empty files, no status, no errors pass
`os.path.isfile` (line 148) has no size or content predicate. Eight 0-byte files plus a receipt
whose only match for `(seat|report|status)` is its title line print `D3 PASS`. A round in which
every seat crashed before writing anything, but the L1 `touch`ed the paths, is indistinguishable
from a real 64-seat wave. The "dead seats carry a last-error line" clause of R65-D3
(`corpus/lessons/round-65-verifier-spotcheck.md:78`) is unimplemented; the leg cannot fail it.

### HIGH-2 — The leg, applied to round-65's already-refuted evidence, PASSES (decisive)
Round-65 failed R65-D3 with **0 dispatched seats** while `w1/` held **54 `.md` seat artifacts**
(`corpus/lessons/round-65-verifier-spotcheck.md:22`). Round-65's registry is byte-class identical
to round-66's seed:

```
.ufo/waves/round-65/w1/swarm-registry.json  members=64 nonnull_ids=0 created=2026-10-24T07:13:43.748Z updated=2026-10-24T07:13:43.748Z
.ufo/waves/round-66/w1/swarm-registry.json  members=64 nonnull_ids=0 created=2026-10-24T11:29:01.355Z updated=2026-10-24T11:29:01.355Z
```

Executed equivalence test (only the wave literal remapped; no files created) — the exact leg
arithmetic applied to r65's on-disk evidence:

```
R65 equivalence: reported=54 existing=54 -> leg_ok=True
```

Live corroboration at 08:35: `.ufo/waves/round-66/w1/*.md` already holds 16 seat files, i.e. a
receipt trimmed to those 16 paths — none of which has been integrated or validated — would print
`D3 PASS` today.

So the D3 disposition re-uses the artifact class the spotcheck already ruled insufficient. The
instrument is insensitive to the difference between "64 seats dispatched" and "0 seats
dispatched, 54 stale reports present". That is the defect: not a claim that this round is
dishonest, but that D3 cannot certify it either way.

### HIGH-3 — The registry contributes zero evidence and is not read by any leg
Measured over `.ufo/waves/round-66/w1/swarm-registry.json`: `members=64`, **`agentId` non-null in
0/64**, `item` non-null in 0/64, `updatedAt == createdAt` (never updated after seeding).
`grep -n "registry" reports/round-66/accept-ca.py` yields only the receipt path constant; no leg
opens the registry. The receipt hardcodes `(members=64)` with no registry hash — editing the
registry later changes nothing that D3 checks. The lane's own precedent shows the format *can*
carry identity: `.ufo/waves/round-50/build/swarm-registry.json` records
`"agentId": "ChousaR27R2.ExecGuard-4"` with `updatedAt (15:23:21) > createdAt (15:12:28)`.
Round-66 seeded the null form, so the claim's "dispatch registry **+** seat-evidence receipt" is
half missing.

### HIGH-4 — The seed receipt cannot pass even on a perfect 64/64 dispatch, and its cheapest green is a nonsense artifact
`re.findall` captures the template line `# report: each seat writes …/w1/<SEAT>.md` as a
65th path:

```
seed reported=65 includes_placeholder=True ; real_seat_entries=64
if all 64 real reports exist -> existing=64 != reported=65 -> leg_ok=False
```

Because of `len(existing) == reported`, a flawless wave still FAILs unless someone creates a file
literally named `<SEAT>.md`. The two ways green: (a) L1 rewrites the receipt at integration
(author-controlled, unverified), or (b) `touch '.ufo/waves/round-66/w1/<SEAT>.md'` — a nonsense
artifact that makes the floor pass. A check whose minimal satisfying action is to fabricate a
placeholder is not measuring dispatch.

### MED-5 — Duplicate path strings count toward the floor (no dedupe)
`seat_paths` is a list, never a set. Executed: 8 copies of one real path →

```
Duplicate flaw: reported=8 unique=1 existing=8 -> leg_ok=True
```

One report file can therefore satisfy the "≥8 seats" floor eight times.

### MED-6 — No time, authorship, content, or batching binding
- mtime is never compared to the dispatch window; files created at integration (after the fact) pass.
- Author == subject: the L1 writes the receipt *and* the files, then runs the counter.
- No `Report:` trailer / validator-rendered path is required, so a seat that never rendered counts.
- The floor counts *any* seat, including attack seats that report the receipt as broken: this file
  (`.ufo/waves/round-66/w1/RevD3Evidence.md`) is one of the 65 seeded paths, so this very report
  will raise `existing` by one toward a D3 PASS.
- No batch proof: R65-D3's requirement is "≥8 dispatched **in one batched call**"
  (`round-65-verifier-spotcheck.md:22,78`). The leg carries no call id and does not reference
  `.ufo/waves/round-66/taskcall-v2.json`. That file is the *prepared* form — identical schema, key
  set and counts to the round-65 artifact the spotcheck rejected
  (`ufo-swarm-wave-dispatch-v1`, keys `schema,wave,policy,counts,registry,compaction,taskCall,resumeSends,note`,
  both `{'spawn': 64}`, `note` the only difference); it records no returned ids.

### MED-7 — D3 evidence is unpinned and partly path-drifted
`git ls-files reports/round-66` = 0 and `git ls-files .ufo/waves/round-66` = 0 at the lane tip:
both the receipt and the seat files are untracked working-tree bytes. The receipt carries no
measured revision, tree hash, or sha256, so it is exempt from QUALITY criterion 17
(`corpus/QUALITY.md:55`) that D2 enforces on the three `final-measures-*.txt` — D3 evidence can be
edited after measurement with no ancestry, the exact R65-D2/M9 class. Path drift: `claims.json`
REC lands `.ufo/waves/round-66/registry.json`, which **does not exist**; the receipt names
`w1/swarm-registry.json`. Nothing reconciles the two.

### LOW-8 — Real dispatch appears to have happened, and the durable proof is evaporating
The live roster shows ≥34 named seat lanes plus "34 more live peer(s) omitted"
(e.g. `L1-kotodama-r66.ScoutRow04`), so r66 likely did dispatch. But the harness transcript is not
flushed: no `*.jsonl` under `/home/vgpnk/.omp/agent/sessions` was touched in the last 25 min, and
`history://`/`agent://` are runtime-only. The identity evidence exists in memory and will be lost
at integration unless captured at dispatch time — which is precisely what D3 should have required
and did not.

## What I would demand beyond existence

1. **Identity, not expectation.** Registry members carry non-null `agentId` (round-50 format
   `Lane.Seat-N`) and `item`, `updatedAt > createdAt`; ≥8 members distinct. The receipt states
   counts *derived* from the registry, plus the registry's sha256.
2. **Harness-authored dispatch record.** A captured task-call response (`agentId`, counts,
   timestamps, terminal status) written at dispatch, sha256'd into the receipt, with a call id;
   the returned ids must match the registry. Preparation artifacts are explicitly excluded
   (R65-D3 ruling).
3. **Per-seat terminal state.** Fixed vocabulary (`completed|errored|killed|timeout|refused`); every
   non-completed seat carries a verbatim last-error line (non-generic, ≥1 error-class token);
   a dead seat without one is a FAIL, not a silent skip.
4. **Content and time floor per report.** >0 bytes, a `Report:` trailer resolving to the named
   path, mtime ≥ registry `createdAt`, and the seat ≠ the receipt author.
5. **Set semantics.** `set()` the paths, reject `<SEAT>`/placeholder tokens, and count distinct
   registry members — not path strings or duplicates.
6. **Durability parity with D2.** The receipt is carried by a commit whose parent is the measured
   revision, and it names the revision/tree/counter sha; update `claims.json` REC lands to the real
   registry path.
7. **Honest refusal branch.** If the wave was refused or errored, accept a verbatim refusal record
   and report floor-not-met — never PASS (the spotcheck's own alternative: "dispatch … **or**
   record the refused/errored dispatch evidence").

Cheapest sufficient fix, in-place: in `accept-ca.py` D3, replace the existence test with
`members = json.load(registry)["members"]`, keep `[m for m in members.values() if m["agentId"]]`,
require `≥8` distinct, require each named report `size > 0` and `mtime ≥ createdAt`, require ≥1
status token per seat from the fixed vocabulary, reject `<SEAT>`, and dedupe with `set()`; keep
`len(existing) == reported` only over the receipt's status-block paths.

## Residual risk and verification gaps

- I did not execute `accept-ca.py` (its D3 artifacts are integration-time; running it now would only
  reprint the frozen `dry-run-ca.txt` FAIL). Findings are derived from canonical file bytes plus
  executed arithmetic/equivalence tests, not from a counter run.
- The equivalence test remaps only the wave literal (`round-66`→`round-65`) before the `isfile`
  check; a verbatim run needs r66 files that did not exist at 08:33 (`w1/*.md` count = 0).
- No `lsp` device is mounted (`xd://lsp` → "No such tool"; mounted: `ast_edit`, `debug`), so the
  caller check on `accept-ca.py` is a literal `grep` fallback: no code imports or invokes it — only
  lesson/claims prose reference it. Recorded as text search, not semantic proof.
- I did not audit D1/D2/D4/CRITERION/QUOTES beyond the shared receipt-durability class in MED-7.
- No tools installed or upgraded.

Report: .ufo/waves/round-66/w1/RevD3Evidence.md
