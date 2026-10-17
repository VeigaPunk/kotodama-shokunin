# R9-D09 — adversarial review: circularity audit of the D3 acceptance evidence

- round: 9 (loop 1 of 3, build round 2 of 4) · shard **R9-D09** (adversarial reviewer, depth claim D / `culture-d3-acceptance`)
- date: 2026-10-17 · reviewer run 20:47Z–20:53Z (UTC) · local = UTC-3
- baseline revision `a7bb205d3aecdaa24d91c047c8719cd8689e4ddd` (`reports/round-9/claims.json:5`); every command below ran at that revision with the round-9 wave in flight
- **owns this file only.** Nothing else in the repo was written: all scratch is under `/var/tmp/d3audit/` (the shared `/tmp` was inode-exhausted at audit start — `df -i /tmp` 100%, matching D01 §0 / D04 §9 / D05 §"Environment receipts"; my first redirect did fail with `No space left on device`). No packet, component, pin, manifest, gate or tool was edited; `git status --short -- examples/culture-d3 tools/` stayed empty of `M`/`A` entries.
- canon: NON-CANON engineering evidence. This review admits nothing and adjudicates no re-pin.

**Assignment (verbatim):** audit the D3 acceptance evidence for circularity — a packet regenerated to bless its own change; a control that cannot fail; severity-ranked findings.

**Verdict in one line:** no fabricated or self-blessed green was found anywhere in the landed D3 evidence — every shard that touched the committed freeze reports it red/could-not-evaluate honestly — but the one remaining step to claim-D green (a re-pin of `examples/culture-d3/expected.json`) is *mechanically indistinguishable from a bless-the-tamper operation*, so acceptance is conditional on the re-pin record (S1). Two further green-by-construction surfaces (S2), one subset-only control matcher (S3) and three minor items (S4–S6) are ranked below, with everything I attacked that did **not** break in §3.

## 1. Audit method and anchors

Adversarial probes ran through the real CLI as subprocesses (and, for the disable-witness matrix only, through an in-process copy of the guard with specific checker functions stubbed — method limit noted in §4). Every numeric claim below is my own measurement, not a quotation of the fragments under review.

Audit-time anchors (so any post-review refresh is provably ordered after this file; measured 2026-10-17T20:51Z unless noted):

| artifact | sha256 | extra anchor |
|---|---|---|
| `examples/culture-d3/expected.json` (the freeze) | `74496aa8aa7db2d7b2d69ecbd7a5a6acf3d4f565f600fd74bfeab5480adf5080` | git blob `c420ac4cad4722848efd8bb79f8efab51c4559e9` (`git rev-parse HEAD:…`) |
| `examples/culture-d3/packet.json` | `bdf635ceaed4eb2f43ed68418aea968dc930b572bfa61b709372efe89baf4829` | `git hash-object` = `HEAD:…` = `0a971d5a3f894030f35c28adaef93ae204000482` |
| `examples/culture-d3/packet.gates.yml` | `306bcac7b920840ae26f544afcf39a1f09666d6a8c5e786a5089e89af4c70425` | git object = `HEAD:…` = `6ee7eb395dedbb1399536aca12de727f7242837f` |
| `tools/check-evidence-coupling.py` (guard) | `849494b0c4113885223f6d865110cd34ed6bb3aeec8b449d020f7b571eb2197e` | equals its own manifest entry (S4) |
| drifted gates: `costume-era-consistency-gate.py` / `naming-collision-gate.py` | `e6bffd70…ceec478f` / `d9e4e8f4…1a630a1d` | live == HEAD blobs |

Reviewed fragments (audit-time sha256, measured 20:51Z–20:52Z while their owners were still writing): `check-diagnosis.md` `fd699ff2…`, `determinism.md` `8075a76d…`, `evidence-coupling.md` `a4053219…`, `replay.md` `84f6377a…`, `cli-negatives.md` `afa0bd2a…`, `interop.md` `4ea268cc…`, `docs.md` `ea208cd4…`, `capability-draft.md` `a726f62a…`, `scribe.md` `b2e71388…`, `findings-10.md` (D10, read in full). D11 had not landed at 20:52Z.

Live results reproduced by me (receipts in §3): `assemble-culture-d3.py --check` exit 0; `--selftest` 85/85 exit 0; guard `--selftest` exit 0 (positive 5/5, domain 16/16, malformed 4/4, frozen 5/5); guard positive exit 0 `findings: []`; guard `--frozen examples/culture-d3/expected.json` **exit 2, exactly 3 × D3-SNAPSHOT**; `replay-frozen.py --selftest` 79/79 exit 0; D04's scratch proposal manifest replayed by me 5/5 exit 0.

## 2. Findings (severity-ranked)

### S1 — blocking acceptance condition: the re-pin is a blessing operation until it carries a re-verification record (severity: high for the round; no defect in any landed fragment)

*Claim tested:* "the committed freeze can simply be re-pinned, then claim D's *frozen replay clean* is green."

*Evidence.* In an isolated copy of the delivered tree (`/var/tmp/d3audit/tree`, tar copy, 17 MB):

1. baseline copy: `check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json` → exit 2, 3 × `D3-SNAPSHOT` (same three files as on the lane tree);
2. one byte appended to `components/04-language.json`, old freeze kept → exit 2, now **4** mismatches (the tampered component is caught — the pin genuinely fails closed);
3. then only the digest values re-measured into `expected-blessed.json` → **exit 0, `findings: []`**.

So a green frozen run proves *someone refreshed the manifest after the edit* and nothing about whether the edit was legitimate. The token `74496aa8…`/`c420ac4c…` in §1 is the pre-review freeze; a green run after a different `expected.json` token is a *new* claim that must stand on its own record.

*Is anyone making a false green today?* No. D01 (`check-diagnosis.md` §0/§6: "COULD-NOT-EVALUATE … Refreshing the pin is a cross-shard/orchestrator act, flagged not absorbed"), D03 §3, D04 Leg D/E ("**RED** — this is the round's D3 replay blocker unless the parent re-freezes with documentation"; refresh exercised in scratch only, "not committed", "no packet was regenerated to make a red pass"), D08 F1, D12 §3 ("stands as **could-not-evaluate**, honestly, not green and not a silent pass") and D10 F2 all report the red and refuse to re-pin. This finding is therefore a condition on the orchestrator's next move, not a defect accusation.

*Minimum record for a legitimate re-pin* (all of it is cheap; the pieces already exist in the fragments):

- the pre-refresh token of the freeze itself: sha256 `74496aa8…`, git blob `c420ac4c…` (from §1);
- the three keys with old → new digests, and the per-file causing commit (`e1694ba`, round-8 admit; corroborated by my git-blob check in §3);
- the verdict-preservation proof over the D3 projection (old vs new gate bytes): reproduced independently by me — stdout byte-identical, exit 1/1 for both gates (see §3, S2(b)); D01 §3 quotes the same pair with a trailing-newline-stripped hash convention (S6(a));
- the byte-level no-change traversal: all four components match their freeze pins; `packet.json`/`packet.gates.yml` worktree bytes hash to their `HEAD` git blobs; `--check` exit 0 and D04 Leg C's isolated regeneration reproduces the same bytes — i.e. the D3 artifacts themselves are untouched by the drift;
- `expected_exit: 0` / `finding_ids: []` kept predeclared and unedited, and the diff of the freeze shown to be exactly the three digest lines (D04 §5 demonstrates the technique: `expected-refresh.json` `083ca2b1…`, `diff` → 3 changed lines);
- a stamped revision + date, and — my recommendation — the re-run of the green performed by a *different* shard than the re-piner.

Without the first three items, the re-pin is exactly the operation demonstrated in step 3 above.

### S2 — green-by-construction surfaces among the acceptance legs (severity: medium; each disclosed by its author, but the summaries must not lean on them)

**(a) The guard's own selftest cannot see the committed freeze.** `tools/check-evidence-coupling.py:1863-1876` (selftest) builds the `frozen-good`/`frozen-tampered` manifest from **live bytes** at run time. I ran both surfaces at once: selftest exit 0 (`selftest_passed: true`) *and* `--frozen examples/culture-d3/expected.json` exit 2 — i.e. a green selftest is compatible with a red committed freeze, by construction. D03 §1 ("Note (for auditors)") and D08 F3 disclose this precisely; D12's ledger keeps the two rows separate ("COULD-NOT-EVALUATE" for the frozen row). *Condition:* no acceptance summary may cite `frozen 5/5`/`selftest_passed` as evidence for the frozen-replay leg; the leg's evidence is the `--frozen` run itself.

**(b) D04's proposed projection manifest is self-captured.** Leg B builds a manifest from live runs (`/home/vgpnk/r9d04-scratch/build-d3-manifest.py`, 20:50Z) and then replays it 5/5. Replay correctness is *not* circular — controls C1–C4 prove the tool can fail (snapshot/gate/output tampering → `could_not_evaluate`, exit 2; live-input drift → byte-identical receipt, proving the live path is never opened) — but the *rows* pin the current (post-round-8) gate revisions, so 5/5 alone blesses present behavior. The rows are nevertheless independently corroborated against pre-existing expectations: `examples/culture-d3/README.md:88-93` documents exactly naming CROSS-HOLD ×2 + NAME-NEAR and costume R-01; my own live run of the five gates reproduces the manifest's counts 2/47/3/1/3 exactly; and my old-vs-new gate differential shows round-7 vs round-8 gate bytes produce byte-identical stdout on this projection. *Condition if the orchestrator commits the proposal to a repo generation directory:* carry the README-hold correspondence and the differential into the commit record, and treat 5/5 as reproduction, not as design-cleanliness evidence (D04 §7.3 says as much).

### S3 — the control matcher accepts supersets: a guard that over-fires would stay "16/16 green" (severity: medium-low; test-only, no gate behavior affected)

`run_case` (`tools/check-evidence-coupling.py:1687-1706`) checks `expected_ids ⊆ actual` (`missing = want − got`); extra findings are ignored. My count-aware independent re-drive of all 16 domain controls shows this is not hypothetical: 5 controls emit more than their expectation —

| control | actual ids (my run, CLI subprocess) |
|---|---|
| `domain-D3-REFERENCE-bridge-target-unknown-record` | `D3-REFERENCE` ×1 **+ `D3-BRIDGE` ×1** (unexpected id) |
| `domain-D3-NATIVE-L07…` / `…DERIVATION-name-concat…` / `…OBJECT-ground-surface…` / `…ERA-material-route…` | expected id ×3 / ×2 / ×2 / ×2 |

D03's §4 table records exactly these supersets in prose (my counts match its table); the *mechanism* does not enforce them, and the positives only pin `findings == []` on three cases. Consequence for the acceptance argument: the control set demonstrates the guard *can* reject each trick; it does not demonstrate the guard's verdict is *exactly* the contract's. Recommendation (not blocking, and outside this shard's write scope): add an exact-verdict field to `controls.json` (e.g. `expected_extra_ids`/counts) or record subset semantics as the accepted standard.

### S4 — the freeze document is unpinned by construction (severity: low; documented design, residual only)

`expected.json` deliberately excludes itself from its own manifest (D01 §2; contract `reports/round-7/d3-contract.json` `guard_cli`), so nothing in-tool witnesses an in-place edit of `expected_exit`/`finding_ids`/manifest entries — only git and the round receipts do. Anchors for that gap are recorded in §1; I recommend the D12 ledger (or the admission receipt) carry the freeze's sha256 pre/post re-pin.

### S5 — `--selftest` is outside the assembler's exit-2 envelope (severity: low; independently reproduced; report-only)

D05's neighbouring finding (cli-negatives.md §"Neighbouring boundary"): `main()` calls `selftest()` at `tools/assemble-culture-d3.py:915-916`, before the `try` at `:917`. I reproduced the failure mode by a different method — monkeypatching `tempfile.TemporaryDirectory` to raise `OSError(28)` and calling `main()` with `--selftest`: the exception propagates out of `main()` (4-frame traceback, no exit-2 diagnostic). Not acceptance-affecting (all selftest runs cited by D01/D03/D04/D12 are green, including my own 85/85 and 79/79), but it sits on the evidence path several fragments quote; a temp-dir failure there degrades to a traceback, which the D3 CLI standard forbids elsewhere. Fix belongs to the assembler's owner; no change made.

### S6 — informational: receipt conventions and environment

- **Hash convention:** D01 §3's stdout sha256 values reproduce only with the trailing newline stripped (`c784dd03…`/`926ceb7d…`); raw-pipe `sha256sum` gives `506d1632…`/`40d4048c…`. Both represent byte-identical old-vs-new output; the conclusion is unaffected, but a re-runner must know the convention (state it in the fragment).
- **Evidence path used a full `--frozen`/`--selftest` surface** re-run by me; the disable-witness matrix (§3) used an in-process copy of the guard module with specific `check_*` functions stubbed, because run_checks calls globals. That matrix therefore measures control sensitivity to the owning checkers, not shipped-CLI behavior; all shipped-CLI behavior quoted in §2/§3 comes from subprocess runs.
- **Environment:** shared `/tmp` inode exhaustion (100% at audit start) — all my probes used `/var/tmp/d3audit/`; a re-runner needs `TMPDIR` elsewhere.

## 3. Attacks that did **not** break anything (verified clean)

1. **No vacuous or dead control.** Applied all 19 control patches with my own JSON-pointer implementation, verifying each `replace` actually changed the value (0 no-op patches) and each patch path resolved (0 failures), then ran the real CLI: every exit code and every `expected_ids` entry matched `controls.json`. Then the stronger test — *can the control fail?* — disabling (one at a time) each checker function capable of emitting the expected diagnostic, in an in-process guard copy, over that control's mutated packet: **16/16 domain controls lose their expected id, and the guard then exits 0**. Single-function witnesses exist for 15 of 16; `domain-D3-ERA-material-route-missing-costume-era` needs all three emitters (`check_eras`, `check_materials`, `check_costumes`) disabled — redundancy, not vacuity. No control passes regardless of its checker.
2. **Frozen mode really fails closed.** Isolated-copy component tamper → exit 2 with the added mismatch (S1 step 2); declared-digest tamper, unknown manifest entry, boolean `expected_exit` → exit 2 `D3-SNAPSHOT` (selftest frozen cases, re-run by me green; independently reproduced via step 2 and by the guard's own subprocess cases).
3. **Malformed kinds are genuinely malformed.** `invalid-json` truncation → `JSONDecodeError`; `invalid-utf8` prefix → `UnicodeDecodeError`; `wrong-root` is *valid* JSON `[]` rejected by the root-type check (D3-DATA "packet root must be a JSON object, got list", exit 2) — a type violation, not a parse error, and the control name is accurate; missing file → D3-DATA exit 2. No tracebacks on any of the three I ran directly.
4. **The pins are honest at authoring time.** Against revision `57c3ce6` (pin-authoring checkpoint) I hashed the three later-drifted files from git and compared to the *committed* `expected.json` there: all three **matched** — the freeze was correct when written, and drift entered with `e1694ba` (round-8 admit). This rules out "authored already-stale" (the worse variant) and corroborates D01 §2/D04 §4 independently.
5. **The drift is a systemic post-pin incident, not D3 corruption.** `tools/gates/frozen/round-3/MANIFEST.tsv` pins the *same old* gate hashes (`29a9361c…`, `8c5afb0a…`) as the D3 freeze — one round-8 repair invalidated several manifests; the D3 freeze is not independently wrong (D01 §3 same conclusion).
6. **No packet was regenerated to bless a change.** Worktree bytes of `packet.json`/`packet.gates.yml` hash to their `HEAD` git blobs (§1); components match their freeze pins; `--check` exit 0; D04's isolated regeneration reproduces the same bytes; `git log --oneline -1` for the D3 artifacts → `57c3ce6` (unchanged since round 7). The one writable assembler operation (`assemble` without `--check`) is not used by any fragment to rewrite outputs; D02's in-place double run changed nothing (`cmp` reproduced; git status showed no `M`).
7. **The "verifier verifies itself" loop is externally anchored this revision.** The guard's sha256 equals its own manifest entry, and that value is corroborated by my independent `hashlib` sweep (which used no guard code) — so the guard's self-pin is not merely self-asserted at this revision. Residual: an in-place guard edit + freeze refresh remains undetectable in-tool (S4).
8. **D04's headline replay claim reproduces from outside.** I re-ran `replay-frozen.py` over D04's scratch proposal manifest (`70affb9d…`): `REPLAY OK: 5/5`, exit 0, rows `count=2/47/3/1/3 bytes=match launched=yes`; and my direct five-gate run of the same input gives the same counts.

## 4. Coverage limits (what this audit does not certify)

- **Un-auditable at finish time:** `reports/round-9/d3/cross-check.md` (R9-D11, not landed at 20:52Z) and `reports/round-9/run-validation.py` / `validation.json` (claim-D counting command absent). When they land, re-apply S1's record test to any green they report; my §1 anchors make an ordering check possible.
- I read all landed D fragments but did not re-derive their numbers beyond the checks listed in §3; e.g. D06's D2 interop deltas were not re-run in full (I confirmed only `assemble-d2.py --check` exit 0 and that `packet.d2.yml`'s `reader_sha256` `e6bffd70…` equals the live costume gate — the round-8 re-pin precedent D01 §6 cites).
- This review does not adjudicate the honesty of the round-8 repairs themselves (round-8's own audit/replay fragments carry that) nor anything historical/canon: no authenticity, language-screening, cultural-permission or lore-acceptance claim is made or assessed.
- The disable-witness matrix used a stubbed in-process module (S6(b)); mutants are not shipped artifacts.

## 5. Reproduction

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=/var/tmp   # shared /tmp was inode-exhausted at audit time
python3 tools/assemble-culture-d3.py --check                      # exit 0, byte-identical
TMPDIR=/var/tmp python3 tools/assemble-culture-d3.py --selftest   # 85/85
TMPDIR=/var/tmp python3 tools/replay-frozen.py --selftest         # 79/79
python3 tools/check-evidence-coupling.py --selftest               # exit 0, 5/5 16/16 4/4 5/5
python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json \
        --frozen examples/culture-d3/expected.json                # exit 2, 3 × D3-SNAPSHOT
# independent digests (no guard code):
python3 -c "import hashlib,json;m=json.load(open('examples/culture-d3/expected.json'))['manifest'];print([k for k,v in m.items() if hashlib.sha256(open(k,'rb').read()).hexdigest()!=v])"
# isolated bless demonstration: /var/tmp/d3audit/ (runner scripts: run_controls.py, vacuity.py)
sha256sum examples/culture-d3/expected.json tools/check-evidence-coupling.py
git rev-parse HEAD:examples/culture-d3/expected.json
```

## 6. Addendum (20:53Z, after the counting command landed)

`reports/round-9/run-validation.py` and `reports/round-9/validation.json` (sha256 `788203a90dcbb8274497578052d7ca4cbff472af6df95731506e290e01d863c3`, measured 20:53:18Z) landed after the body of this file was written. Checked because claim D's counting command is the acceptance surface itself:

- the runner encodes the honest condition — "the D3 frozen expectation must replay without digest drift (`check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json` exits 0)" (`run-validation.py:64-66`);
- its current verdict is `claims.D.passed: false`, `acceptance_checks_passed: false`, with the failure text `tools/check-evidence-coupling.py --frozen examples/culture-d3/expected.json exit 2 (expected 0: no digest drift)` and `measurement.frozen_replay.finding_ids = [D3-SNAPSHOT ×3]` — i.e. the runner reports the frozen leg red rather than papering over it, and `measurement.replay_note` records that no round-9 D3 replay manifest was discovered.

This confirms, rather than contradicts, S1: the round as currently stood at 20:52Z has **no green frozen leg**. Any later green — from a re-pin, or from adopting D04's proposal manifest — is a new claim and must satisfy S1's record test (pre-refresh token `74496aa8…` / blob `c420ac4c…`, the three old→new digests with causing commit, the verdict-preservation differential, and the unchanged
`expected_exit`/`finding_ids`).
