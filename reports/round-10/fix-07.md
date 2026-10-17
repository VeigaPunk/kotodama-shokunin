# R10-O07 — findings fixer: tracker idx 5 (R8-D16 S10) and idx 13 (R9-D09 S5)

- shard: R10-O07 (claim O, findings fixer) · round 10 (loop 1 of 3, build round 3 of 4), 2026-10-17
- baseline revision `9dc18ec1339bffd6f81e74f1a5742464ef578749`; every command below ran 2026-10-17 (local = UTC-3)
- tracker: `reports/round-10/findings-tracker.json` (R10-O01, compiled 18:28; rows are 0-based)
- write scope: **this file, plus the two assigned tracker rows** (idx 5 and idx 13), updated in place under `fcntl.flock` + atomic replace in the style the sibling fixers established (R10-O03), with every other row round-tripped byte-identical and the pre/post hashes recorded in §6 — the runner (`reports/round-10/run-validation.py`) fails any tracker row left `pending`, and the targets' fixer rule says "update the tracker row". All scratch lives under `.scratch/fix07/` (`export TMPDIR=$PWD/.scratch`), never `/tmp`.
- canon: NON-CANON engineering evidence. No packet, component, gate, tool, SCORECARD or filed report byte was modified by this shard (`git status --short` shows no change attributable to it; §5).

## 0. Assignment and mapping

The tracker row for each assigned index, quoted verbatim (fields `idx`, `source_file`, `severity`, `source_status`; `finding` abbreviated to its head):

| idx | source_file | head of `finding` | severity |
|---|---|---|---|
| 5 | `reports/round-8/depth/findings.md` | `S10 [locator §S10, lines 77-79] (medium) — "executable rank-rule adapter" overstates coverage: … rank_rules_component=21, rank_rules_gate_projected=5, rank_rules_unresolved_items=13 … The SCORECARD capability row should carry the ratio, not the adjective.` | medium |
| 13 | `reports/round-9/d3/findings.md` | `S5 [locator §2 S5, lines 79-81] (low; report-only, independently reproduced) — --selftest sits outside the assembler's exit-2 envelope: main() calls selftest() at tools/assemble-culture-d3.py:915-916, before the try at :917 …` | low |

Both findings are valid on the live tree. For each, the canonical fix touches a shared artifact outside this shard's write scope (SCORECARD.md; `tools/assemble-culture-d3.py`), so this shard delivers a **verified patch + demonstrated fail-before/pass-after control**, and states the landing condition. Disposition written to the tracker (§6): `fixed-with-control`, with a `residual` field recording whether the patch is applied and why not.

---

## 1. idx 5 — R8-D16 S10: the capability row must carry the rank-adapter ratio

### 1.1 Finding (as filed)

`reports/round-8/depth/findings.md` §S10 (lines 77-79): the tool's rank adapter is honest and quantified at the newest revision, "but '**executable** rank-rule adapter' still describes 5 gate-projected of 21 records. The SCORECARD capability row should carry the ratio (S11 is about how that row is checked)."

### 1.2 Live measurement (fail-before state), 2026-10-17

The ratio is grounded in the **live deterministic build**, not only the committed artifact — and it is identical in both:

```sh
export TMPDIR=$PWD/.scratch
python3 tools/d2-typed-labels.py --emit .scratch/fix07/typed-labels.live.yml   # exit 1 (see §3), writes the live build
grep -n 'rank_rules_component\|rank_rules_gate_projected\|rank_rules_normalized\|rank_rules_unresolved_items\|rank_quarantine_handles' .scratch/fix07/typed-labels.live.yml
# :40 rank_quarantine_handles 3   :41 rank_rules_component 21   :42 rank_rules_gate_projected 5
# :43 rank_rules_normalized 9     :44 rank_rules_unresolved_items 13
sha256sum .scratch/fix07/typed-labels.live.yml    # a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43
grep -c 'D2L-RANK' .scratch/fix07/typed-labels.live.yml   # 4
```

The committed artifact carries the same five numbers at the same line numbers (`examples/culture-d2/typed-labels.d2.yml:40-44`, sha256 `e70ba147…`); the only byte difference between the two files is the stale `packet_sha256` provenance line (§3).

The overstatement's live surface is **not** in the capability row today — the row is silent about the rank adapter, which is the gap the finding names. Sweeps (2026-10-17):

```sh
grep -n 'rank' SCORECARD.md        # one match: :182 (the round-8 claim-D declaration text in "Planned": "executable rank-rule adapter")
grep -c '5/21' SCORECARD.md        # 0 — the ratio appears nowhere in SCORECARD.md
sed -n '128p' SCORECARD.md         # the d2-typed-labels capability row: no rank coverage at all
grep -rn 'executable rank\|rank-rule adapter' SCORECARD.md SKILL.md README.md   # SCORECARD:182 only; SKILL.md/README: no match
```

So: the adjective survives only as the historical round-8 claim declaration (`SCORECARD.md:182`, in "Planned" — a declaration record, correct to leave as history), and the **capability row carries no ratio**. `corpus/lessons/round-8.md:89` ("implements … the rank-rule adapter") is the round-8 lesson record, same historical class.

### 1.3 Proposed patch (capability row, `SCORECARD.md:128`)

Landing site: the row of the round-8 "Capabilities addendum" table (line 128). Exact replacement:

- before: `| d2-typed-labels | Types D2 records across five kinds by declaration; enforces holds (TL-01/TL-02), borrow-ledger clock checks (B4), channel separation; emits typed projection | `python3 tools/d2-typed-labels.py --selftest`; `examples/culture-d2/typed-labels.d2.yml` | round 8 |`
- after: `| d2-typed-labels | Types D2 records across five kinds by declaration; enforces holds (TL-01/TL-02), borrow-ledger clock checks (B4), channel separation; emits typed projection; rank-rule adapter coverage 5/21 records gate-projected (9/21 normalized, 13 unresolved items, 3 quarantine handles) — not full rank semantics | `python3 tools/d2-typed-labels.py --selftest`; `examples/culture-d2/typed-labels.d2.yml` `rank_adapter` block | round 8 |`

Optional second site (same evidence, if the parent prefers the axis row too): `SCORECARD.md:112` (round-8 depth row) gains the same clause after "borrow-ledger checks". The adjective at `:182` stays — it is the historical declaration, and the finding asks for the ratio in the capability row, not for rewriting history.

### 1.4 Control (demonstrated, re-runnable)

`.scratch/fix07/check_s10.py` (sha256 `1a3fa49d…`) parses the live build's `rank_adapter` numbers and requires the capability row to carry the ratio and the four counts, so the row cannot drift from the artifact:

```sh
python3 .scratch/fix07/check_s10.py SCORECARD.md .scratch/fix07/SCORECARD.patched.md
# live artifact numbers: {'rank_rules_component': 21, 'rank_rules_gate_projected': 5, 'rank_rules_normalized': 9,
#                         'rank_rules_unresolved_items': 13, 'rank_quarantine_handles': 3} -> ratio 5/21
# [SCORECARD.md] FAIL: coverage ratio 5/21 absent from the capability row; artifact count rank_rules_gate_projected=5 absent …; rank_rules_normalized=9 absent …; rank_rules_unresolved_items=13 absent …
# [.scratch/fix07/SCORECARD.patched.md] PASS
```

Fail-before = the filed SCORECARD; pass-after = `.scratch/fix07/SCORECARD.patched.md` (filed SCORECARD + the §1.3 row replacement; `diff` = 1 changed line, byte delta +166 — the patch script asserts the anchor occurs exactly once). Output pinned: `.scratch/fix07/check_s10.out` sha256 `759178326e9e8185d30ba84dd817031464b9cb408d6d140d8119663903e7098c`.

### 1.5 Disposition (row 5 payload to merge)

```json
{"idx": 5, "disposition": "fixed-with-control",
 "disposition_evidence": "reports/round-10/fix-07.md §1",
 "control": "python3 .scratch/fix07/check_s10.py SCORECARD.md .scratch/fix07/SCORECARD.patched.md — FAIL (ratio absent) on the filed SCORECARD, PASS on the §1.3 row patch; ratio grounded in the live build's rank_adapter block (5/21 gate-projected, 9/21 normalized, 13 unresolved, 3 quarantine handles; 4 x D2L-RANK)",
 "landing": "not applied by this shard (SCORECARD.md is outside the assigned write scope); §1.3 row replacement is ready for the integration step"}
```

---

## 2. idx 13 — R9-D09 S5: `--selftest` outside the assembler's exit-2 envelope

### 2.1 Finding (as filed)

`reports/round-9/d3/findings.md` §2 S5 (lines 79-81): `main()` calls `selftest()` at `tools/assemble-culture-d3.py:915-916`, before the `try` at `:917`; a `tempfile.TemporaryDirectory` failure (`OSError(28)`) propagates out of `main()` as a traceback, with no exit-2 diagnostic — while the D3 CLI standard elsewhere maps failures to exit 2. Report-only, low; the fix belongs to the assembler's owner.

### 2.2 Reproduction on the live revision (fail-before)

Live file `tools/assemble-culture-d3.py` sha256 `ba8d19d5855fe670e5a828f0aca8133fb2cbf54ee865927917c9f20d5d17f014`; the cited structure is still exactly as filed (`:915` `if args.selftest:`, `:916` `return selftest()`, `:917` `try:`).

`.scratch/fix07/probe_s5.py` (sha256 `d7594a08…`) execs the module with `__file__` set to the real path (so `ROOT` resolves correctly), monkeypatches `tempfile.TemporaryDirectory` to raise `OSError(28)`, sets argv to `--selftest`, and calls `main()`:

```sh
python3 .scratch/fix07/probe_s5.py
# filed assembler sha256: ba8d19d5…
# [fail-before (filed source)] EXCEPTION ESCAPED main(): OSError: [Errno 28] No space left on device
# [fail-before (filed source)] traceback frames: 4
# [fail-before (filed source)] stderr captured: ''
# [pass-after (patched source)] main() returned rc=2; stderr='selftest error: [Errno 28] No space left on device\n'
# VERDICT: fail-before reproduces
# VERDICT: pass-after fixed
```

The 4-frame traceback matches R9-D09's independent reproduction. Output pinned: `.scratch/fix07/probe_s5.out` sha256 `d2f622a594339ca882374d8077aea61f0ae3f3f9714b202bfcfdea55c050c416`.

### 2.3 Patch (verified) and no-regression controls

Minimal patch at `tools/assemble-culture-d3.py:915-917` (filed) — wrap only the selftest call; `selftest()` itself is untouched:

```diff
     if args.selftest:
-        return selftest()
+        try:
+            return selftest()
+        except OSError as exc:
+            print(f"selftest error: {exc}", file=sys.stderr)
+            return 2
     try:
```

Controls on the patched bytes (patched sha256 `a18371dd0652b38853e8b9701e3c1bf46ac0b124fef9140a7bf4bd055fa93ff5`):

| control | command | observed |
|---|---|---|
| fail-before | `python3 .scratch/fix07/probe_s5.py` | OSError escapes `main()`, 4-frame traceback (§2.2) |
| pass-after (in-memory patch) | same probe, patched source | `rc=2`, stderr `selftest error: [Errno 28] No space left on device` |
| pass-after (patched full copy, ENOSPC) | probe against `.scratch/fix07/tree/tools/assemble-culture-d3.py` (`a18371dd…`) | `rc=2`, same diagnostic |
| no regression — selftest | patched copy `--selftest` | exit 0, `selftest: 85/85 checks passed` |
| no regression — check | patched copy `--check` | exit 0, `packet.json: byte-identical …; packet.gates.yml: byte-identical …` |
| baseline (filed bytes) | `python3 tools/assemble-culture-d3.py --selftest` / `--check` | exit 0 85/85 / exit 0 byte-identical |
| incidental real-world instance | patched copy in a mirror lacking `tools/gates/` | exit 2 + `selftest error: [Errno 2] No such file or directory: …/costume-era-consistency-gate.py` — a genuine `FileNotFoundError` now maps to exit 2 instead of a traceback |

The patched full copy lives at `.scratch/fix07/tree/` (rebuilt by: `tar --exclude=.git --exclude=.scratch -cf - . | (cd .scratch/fix07/tree && tar -xf -)`, then the §2.3 hunk); the probe's in-memory variant needs no copy.

### 2.4 Landing blocker: the assembler is pinned by the D3 freeze (documented reason)

`tools/assemble-culture-d3.py` is a manifest entry of `examples/culture-d3/expected.json` (sha256 `562b76cb…`), and the pin currently matches the live bytes:

```sh
python3 -c "import json,hashlib;m=json.load(open('examples/culture-d3/expected.json'))['manifest'];k='tools/assemble-culture-d3.py';print('pin matches live bytes:', m[k]==hashlib.sha256(open(k,'rb').read()).hexdigest())"
# pin matches live bytes: True   (declared == actual == ba8d19d5855fe670e5a828f0aca8133fb2cbf54ee865927917c9f20d5d17f014)
python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json
# exit 0, findings [] — the D3 frozen replay is GREEN on this tree today
```

Landing the patch **in place without a re-pin regresses that green check**. Demonstrated in the isolated full copy with only the §2.3 hunk applied:

```sh
cd .scratch/fix07/tree && python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json
# exit 2, counts {"D3-SNAPSHOT": 1, "total": 1}
#   manifest digest mismatch for 'tools/assemble-culture-d3.py': declared ba8d19d5…, actual a18371dd…
```

Exactly one new mismatch, and it is the patched file — every other manifest entry still matches (no collateral drift). Verdict preservation for a re-pin: the patched assembler's outputs are unchanged (`--check` exit 0 byte-identical, §2.3), so a re-pin would move one digest with no D3 verdict change. Per R9-D09 S1 any re-pin must carry its record (pre-refresh token `562b76cb…`, the old→new digest pair above, the causing change = this patch, and the byte-identical verdict preservation); that is an orchestrator act, not a worker act.

### 2.5 Disposition (row 13 payload to merge)

```json
{"idx": 13, "disposition": "fixed-with-control",
 "disposition_evidence": "reports/round-10/fix-07.md §2",
 "control": "python3 .scratch/fix07/probe_s5.py — fail-before: OSError escapes main() (4-frame traceback, no exit-2 diagnostic); pass-after: rc=2 + 'selftest error: [Errno 28] No space left on device'; no regression: patched copy --selftest 85/85 exit 0, --check exit 0 byte-identical",
 "landing": "deferred with reason: tools/assemble-culture-d3.py is a D3 freeze manifest entry (live bytes == pin ba8d19d5…); landing without a re-pin turns the green frozen replay red (1 x D3-SNAPSHOT). Patch verified; land in the integration step bundled with a re-pin record per R9-D09 S1"}
```

---

## 3. Adjacent observation (not absorbed; for the drift ledger)

`python3 tools/d2-typed-labels.py --check` exits **1** — "`examples/culture-d2/typed-labels.d2.yml` differs from the deterministic projection". The only byte difference is provenance: the committed artifact pins `packet_sha256: 8da90b07…` (the round-8-era packet) while the live packet is `e0f21509…`; `diff` is 4 lines (1 changed line). All three files were last committed in `e1694ba` (`git log --oneline -1 -- examples/culture-d2/packet.d2.yml examples/culture-d2/typed-labels.d2.yml tools/d2-typed-labels.py` → `e1694ba round-8: admit F/O/D …`), i.e. the artifact's packet pin is stale since round 8 — the rank numbers and every other projection line are identical (rank block `:40-44` in both). This is the freshness claim's territory, not idx 5's; recorded here so the F-scribe can rule it current|stale (the round-10 drift shards 02/04/11 re-ran `--selftest`/`--help`/B4 but not `--check`; `grep -n 'd2-typed-labels --check' reports/round-10/drift/*.md` → no match, 2026-10-17).

## 4. Limits and to-verify

- Both dispositions rest on controls run from this lane on 2026-10-17; a verifier re-runs §1.4/§2.3 verbatim. The `probe_s5.py` monkeypatch measures the shipped `main()` structure, not a real ENOSPC event (method limit, same class as R9-D09's own probe).
- The §1.3 patch text was validated against `SCORECARD.md` sha256 `cc032db8b2749d492cea0847a894d303916c944f23757f54dd2dd26f8d5f7bee`; if SCORECARD.md changes before integration, re-anchor the row (the control asserts a unique row).
- §2.4's re-pin record requirements are quoted from R9-D09 S1; the re-pin itself is out of this shard's province (canon/orchestrator act).
- Not assessed: whether the capability row should also cite the 4 `D2L-RANK` conflicts by id (a presentation choice, ratio included either way).

## 5. Reproduction and no-write sweep

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && export TMPDIR=$PWD/.scratch
python3 .scratch/fix07/check_s10.py SCORECARD.md .scratch/fix07/SCORECARD.patched.md   # FAIL then PASS
python3 .scratch/fix07/probe_s5.py                                                     # fail-before + pass-after
python3 tools/assemble-culture-d3.py --selftest ; python3 tools/assemble-culture-d3.py --check   # 85/85 ; byte-identical
python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json   # exit 0 (still green)
git status --short        # no tracked file changed by this shard; new/edited untracked files: reports/round-10/fix-07.md, reports/round-10/findings-tracker.json (rows 5/13, §6), .scratch/fix07/
```

Receipts (2026-10-17): probe `.scratch/fix07/probe_s5.py` `d7594a08…` → `.scratch/fix07/probe_s5.out` `d2f622a5…`; check `.scratch/fix07/check_s10.py` `1a3fa49d…` → `.scratch/fix07/check_s10.out` `75917832…`; live build `.scratch/fix07/typed-labels.live.yml` `a3aa452c…`; patched SCORECARD `.scratch/fix07/SCORECARD.patched.md`; patched assembler `a18371dd…` (in-memory, `.scratch/fix07/tree/`, `.scratch/fix07/mirror/`).

---

## 6. Tracker update (addendum, 2026-10-17T21:50Z)

Rows idx 5 and idx 13 were updated in place — the only shared-file write by this shard — under `fcntl.flock` + atomic replace, following the sibling fixers' precedent (`reports/round-10/fix-03.md` §4) and because `reports/round-10/run-validation.py` fails any row left `pending` (`PENDING_LABELS`; measurement key `tracker.pending_rows`). Without it, two rows of claim O would read as undispositioned.

- script: `.scratch/fix07/update_tracker3.py`; format self-check first — rows 0/6/7/12 re-serialized as `json.dumps(row, indent=1, sort_keys=True)` with a 2-space continuation prefix and compared byte-identical to their in-file text before any write.
- pre-write tracker sha256 `43338715b4dc82f0cec3ef86468b0041f75428b8ef2c05dc4a4ef5c0bd15f795`; post-write `151217d7fd98965f8f7225de5c91d4b100e89eea3aa2289e8fb0de10b0dcb5ff`. The file changed several times under concurrent sibling writers while this shard worked (`fb88314d…` → `2cbb08c6…` → `43338715…`); the update re-checks `disposition == "pending"` under the lock and aborts otherwise (two aborted drafts did no write).
- preservation proof (in-script assertions): every other row parsed-identical before/after, all top-level fields identical, and each updated row's `finding`/`severity`/`source_file`/`source_status` unchanged.
- values written (the §1.5/§2.5 payloads, `landing` renamed `residual` to match the sibling rows' field): idx 5 → `fixed-with-control`, `disposition_by: R10-O07`, `disposition_at_utc: 2026-10-17T21:50Z`, `evidence: reports/round-10/fix-07.md`, control = the §1.4 receipts, residual = SCORECARD row patch not applied by this shard (out of write scope; §1.3 ready for integration). idx 13 → same shape, residual = landing deferred with the §2.4 freeze-pin reason.
- effect at 21:50Z: the runner's pending set is `[2, 4, 7, 10, 12, 15, 16, 17, 18, 19, 20, 21, 22, 23]` — rows 5 and 13 are no longer in it (other fixers are still landing theirs).
