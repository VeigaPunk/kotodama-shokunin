# R10-O09 — findings fixer: tracker indices 7 and 15, and every row beyond 15

- shard: **R10-O09** (findings fixer, claim O), round 10 (loop 1 of 3, build round 3 of 4), 2026-10-17
- baseline revision: `e3a1ec9435787328ac9f828f96cb6390e4916b8f` (`e3a1ec9`, HEAD at work start; `git rev-parse HEAD`, 2026-10-17)
- write scope: **this file only**. The tracker (`reports/round-10/findings-tracker.json`) is a shared
  surface written by R10-O01/R10-O14; this shard does not write it. Ready-to-paste tracker rows are in §7.
- scratch: `export TMPDIR=$PWD/.scratch` for every scratch-writing command (`/tmp` remains inode-exhausted — §4.3).
- canon: NON-CANON engineering evidence. Nothing here admits a claim, blesses a gate or touches lore.
- method: read the tracker, then re-drive every claim with the shipped CLI; a disposition is
  `fixed-with-control` only where a control that can fail was demonstrated, otherwise `wont-fix`
  with the reason recorded. All counts carry their command; all negative claims carry their sweep.

---

## 0. Index resolution — what rows 7 and 15 are

The assignment names "tracker indices 7 and 15 (and any beyond 15)". The tracker landed while this
shard was working (`reports/round-10/findings-tracker.json`, sha256
`3bfd40181ca98c830ef1042b23c3e446328b915ced9773dbc12b431d6b22d353`, `compiled_at_utc`
`2026-10-17T21:27Z`, 24 rows). Its own ordering rule (`ordering` field, quoted):

> "Open findings first, severity-ranked (blocking/acceptance-affecting -> medium -> low ->
> informational); the six resolved-at-source trail rows (idx 18-23) last."

The tracker's indices are therefore **severity-ranked**, not file-ordered; the fallback rule in
`reports/round-10/targets.json` (fixer *i* takes the *i*-th and *i+8*-th finding; O09 is *i*=8 →
8th and 16th → 0-based idx 7 and 15) lands on the same two rows. Rows owned by this shard:

| idx | source | finding | severity | disposition (§) |
|---|---|---|---|---|
| 7 | `reports/round-9/d3/findings.md` §2 S3 | control matcher accepts supersets (test-only) | medium-low | wont-fix + control (§2) |
| 15 | `reports/round-8/depth/findings-17.md` §3 F-D17-3 | layer reference shape vs spec §1.4 B1 | low | fixed-with-control (§3) |
| 16 | `reports/round-9/d3/findings.md` §2 S6 | receipt conventions and environment (informational) | informational | wont-fix, documented (§4) |
| 17 | `reports/round-9/d3/findings-10.md` §2 F1 | two artifacts declare the rule with different sentences | informational | wont-fix, documented (§5) |
| 18-23 | `reports/round-8/depth/findings.md` §Resolved table (S1, S4, S5, S7, S8, S9) | resolved-at-source; need re-verification | resolved | re-verified (§6) |

Tracker-drift note (2026-10-17, re-read at the end of this shard): peer fixers rewrote the tracker
while this shard worked — sha256 `3bfd4018…` (compiled `21:27Z`) → `43338715…`; `finding_count` stays
24, `compiled_at_utc` stays `21:27Z`, and rows 7, 15, 16, 17 and 18-23 are unchanged in identity
(same source file, same severity) and were still `pending` at the re-read. The index mapping above
therefore still holds; the scribe should merge §7 against the live tracker.

Live anchors measured at this revision (2026-10-17, `sha256sum`):

| artifact | sha256 |
|---|---|
| `tools/d2-typed-labels.py` | `0da0015f700345c938184cb45ca07178c33e98f798c3c09729007487fb89c802` |
| `examples/culture-d2/typed-labels.d2.yml` | `e70ba1477dbeb830061db6fd12516b7d902587bddae173f55a3650015d380b2f` |
| `examples/culture-d2/packet.d2.yml` | `e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643` |
| `tools/check-evidence-coupling.py` | `849494b0c4113885223f6d865110cd34ed6bb3aeec8b449d020f7b571eb2197e` |
| `examples/culture-d3/controls.json` | `f00ccf7aac931fb23719e4c3715f0e987c924fc79d7f9881236567d260d2ae70` |
| `examples/culture-d3/expected.json` | `562b76cb48f14bdb7bcf6362f78d8b5c5506934a10d9f912f6c4a0a554bf90fc` |
| `tools/gates/naming-collision-gate.py` | `d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d` |
| `tools/gates/costume-era-consistency-gate.py` | `e6bffd7020c0b1168828902853320bbf37e903457c83dae5477820aeceec478f` |

---

## 1. Disposition summary

| idx | disposition | one-line reason |
|---|---|---|
| 7 | **wont-fix** (reason + demonstrated control) | superset semantics confirmed by a count-aware re-drive of all 16 domain controls; the guard is not this shard's write scope; recommendation (b) — record subset semantics as the accepted standard — is adopted here and the census is supplied as the standing exactness check |
| 15 | **fixed-with-control** | the current tool emits `borrow.layer_ref` and resolves it against the packet's declared layers with a fail path; `donor_layer` is gone; two mutation controls fire `D2L-BORROW` |
| 16 | **wont-fix** (documented) | informational convention note; all three parts reproduced live and the conventions are recorded here |
| 17 | **wont-fix** (documented) | no consumer reads either sentence; the only "fix" (unify + regenerate) is acceptance-affecting (breaks the `expected.json` pin); the difference is recorded as intentional |
| 18 | re-verified | `--selftest` 39/39 exit 0, no traceback; alias ordering confirmed; latent fragility noted (§6.1) |
| 19 | re-verified | `D2L-*` ×69 in tool, ×37 in artifact; live codes observed; `R-RANK-*` aliased to `D2L-RANK` (§6.2) |
| 20 | re-verified | `label_kinds` is exactly three values (§6.3) |
| 21 | re-verified | exit 1 with 15 holds; exit map code-quoted (§6.4) |
| 22 | re-verified (residual re-checked) | five CLI flags present; two emits byte-identical; D15 residual state checked (§6.5) |
| 23 | re-verified (residual stands, honest) | `script/representation/scheme/evidence` 58/58/68/58; `pronunciation` 0 with source evidence (§6.6) |

---

## 2. idx 7 — R9-D09 S3: the control matcher accepts supersets

**Source claim** (`reports/round-9/d3/findings.md` §2 S3, lines 64-73): `run_case` checks
`expected_ids ⊆ actual`; extra findings are ignored; 5 of 16 domain controls emit more than their
expectation, so "16/16 green" does not pin exact verdicts. Recommendation: add an exact-verdict
field to `controls.json` **or** record subset semantics as the accepted standard.

**Code re-read (2026-10-17).** `tools/check-evidence-coupling.py:1677` `def run_case(...)`;
`:1703` `if passed and want_ids and parsed is not None:`; `:1704` `got = {x.get("id") for ...}`;
`:1705` `missing = sorted(set(want_ids) - got)`; the branch fails only on `missing`. Extras are
never inspected — the subset semantics are exactly as reported.

**Count-aware re-drive through the shipped CLI** (harness
`.scratch/r10o09-superset-census.py`, sha256 `d6fdb84fcfa34c0eb616de35440c10b17aa6a4c87377a7e268552dd3ff5ded55`¹, reconstructible from §9; per control:
deep-copy `packet.json`, apply its JSON-pointer `patches`, run
`python3 tools/check-evidence-coupling.py <mutated>`, count ids as a multiset):

```text
domain-D3-REFERENCE-bridge-target-unknown-record               exit=1  want {'D3-REFERENCE': 1} -> got {'D3-REFERENCE': 1, 'D3-BRIDGE': 1}
domain-D3-NATIVE-L07-forms-consistent-nonprofile-glyph         exit=1  want {'D3-NATIVE': 1}    -> got {'D3-NATIVE': 3}
domain-D3-DERIVATION-name-concat-does-not-yield-declared-form  exit=1  want {'D3-DERIVATION': 1}-> got {'D3-DERIVATION': 2}
domain-D3-OBJECT-ground-surface-marked-worn                    exit=1  want {'D3-OBJECT': 1}    -> got {'D3-OBJECT': 2}
domain-D3-ERA-material-route-missing-costume-era               exit=1  want {'D3-ERA': 1}       -> got {'D3-ERA': 2}
domain controls=16  multiset-exact=11  multiset-differing=5
```

This reproduces R9-D09's §3 table exactly (its prose counts match mine), and it refines the
tracker's paraphrase: **5 controls differ, but only 1 emits an extra *distinct* id** (D3-BRIDGE);
the other 4 differ by *multiplicity* of the expected id. The tracker row's "5 of 16 domain controls
emit extra ids" is a paraphrase of the source's table, which is itself correct.

**Is the extra id noise?** No. Full output for the one control with a distinct extra
(`python3 tools/check-evidence-coupling.py .scratch/ctl-01.json`, 2026-10-17):

```json
{"counts": {"D3-BRIDGE": 1, "D3-REFERENCE": 1, "total": 2}, "exit": 1,
 "findings": [
   {"id": "D3-REFERENCE", "message": "bridge target 'U99' is not an existing D3 record id", "record_id": "BR01"},
   {"id": "D3-BRIDGE", "message": "bridge targets ['U99', 'U02'] differ from the declared design-only mapping ['U01', 'U02']", "record_id": "BR01"}]}
```

The control patches `/bridges/0/target_ids/0` → `U99`; both diagnostics are true statements about
that mutation. **Control that can fail:** the census was run against deliberately wrong
expectations (`D3-NOSUCHID` for every control) and flagged 16/16 — the census is not a rubber stamp
(`self-test: bogus expectations flagged = 16/16`).

**Disposition — `wont-fix`, with reason and control.**
Reason: the matcher lives in `tools/check-evidence-coupling.py`, which this shard may not write; and
the guard's *acceptance* legs do not rely on exact verdicts (the frozen leg compares declared
digests and `finding_ids: []`, `examples/culture-d3/expected.json`). Mitigation adopted per the
source's own recommendation (b): **subset semantics are recorded here as the accepted standard for
`controls.json`**, with the census above as the standing exactness check that the guard owner (or
any later round) can adopt. Residual risk (bounded, stated): a guard regression that *over-fires*
would keep the selftest green; the census is the only surface that would show it.

¹ computed after the run; the harness is scratch and not committed, per the round's write rule.

---

## 3. idx 15 — F-D17-3: layer reference shape — FIXED, controls demonstrated

**Source claim** (`reports/round-8/depth/findings-17.md` §3, lines 220-225): the label carries
`donor_layer: "Salt-road trade layer"` inline, derived by stage (`donor_layer()`,
`tools/d2-typed-labels.py:431`), rather than the spec §1.4 B1 `layer_ref` resolving against a packet
`layers` block; the name is correct (matches `packet.d2.yml:2540`), but field name and resolution
path differ from the spec. Measured at `623b5b1f` (R8-D17's snapshot).

**Current revision closes the divergence.** Live reads (2026-10-17):

- `tools/d2-typed-labels.py:569` builds `"layer_ref": layer_name` into the label's borrow block;
  `:701-704` `layer_ref = borrow.get("layer_ref"); layer = layers.get(layer_ref) if _is_str(layer_ref) else None`;
  `:704` fail path `"layer_ref {layer_ref!r} does not resolve to a declared layer"`; `:711-730`
  the B2/B3 checks (`donor_form`, `apply_substitutions`, layer-substitution contradiction).
- `grep -c donor_layer tools/d2-typed-labels.py` → **0** in the emitted projection
  (`.scratch/d2-now.yml`) and **0** in the committed artifact — the stage-derived inline field is gone.
- The committed artifact carries the resolved reference on the `kas` record:
  `examples/culture-d2/typed-labels.d2.yml:2409-2461` — `"layer_ref": "Salt-road trade layer"`,
  `"donor_form": "gas"`, `"substitutions": {"bh": "p", "dh": "t", "g": "k", "sh": "s"}`,
  `"text": "kas"` (the donor form is carried as provenance, never substituted for the checked form).
- The packet declares the layer at `examples/culture-d2/packet.d2.yml:2539-2552` (`layers:` →
  `name: "Salt-road trade layer"`), so the reference resolves against a declared block, not a stage.

**Control 1 — the resolution path can fail** (rename the layer in a scratch packet copy; the live
packet is never edited):

```sh
cp examples/culture-d2/packet.d2.yml .scratch/mut-layer.yml   # then replace the layers[0].name once
python3 tools/d2-typed-labels.py --packet .scratch/mut-layer.yml --json      # exit=1
# {"code": "D2L-BORROW", "detail": "layer_ref 'Salt-road trade layer' does not resolve to a declared layer",
#  "id": "D2L-BORROW", "severity": "fail", "where": "L-26"}
```

**Control 2 — the derivation check can fail** (declare `g: "t"` instead of `g: "k"` on the layer):

```sh
python3 tools/d2-typed-labels.py --packet .scratch/mut-subs.yml --json        # exit=1
# {"code": "D2L-BORROW", "detail": "substitutions derive 'tas' from donor 'gas', not 'kas'", "where": "L-26"}
```

Both controls fire `D2L-BORROW` at the label's `where`; the unmutated packet emits no
`D2L-BORROW` at all (`Counter({'D2L-FORM-UNRESOLVED': 10, 'R-RANK-CONFLICT': 4, 'D2L-NATIVE': 2})`,
`--json` exit 1).

**Disposition — `fixed-with-control`.** The spec §1.4 B1 field name and the packet-layers resolution
path now exist and fail closed; the `donor_layer()` stage-derived inline field is absent. (R8-D17's
sibling F-D17-1 — donor form / substitutions / borrow-derivation check — is closed on the same
evidence: artifact `donor_form: gas` + `substitutions` + the `D2L-BORROW` derivation control above;
that row, idx 8, belongs to another fixer.)

---

## 4. idx 16 — R9-D09 S6: receipt conventions and environment (informational)

Three parts, each reproduced live (2026-10-17):

**(a) Hash convention — reproduced exactly.** The pinned round-7 naming gate
(`git show 57c3ce6:tools/gates/naming-collision-gate.py`, sha256 `8c5afb0a…`) and the live gate
(`d9e4e8f4…`) produce **byte-identical stdout** on the committed D3 projection
(`examples/culture-d3/packet.gates.yml`, exit 1, 458 bytes):

```sh
sha256sum < raw pipe      → 506d163231051f294b221d1bb46f78605a689a834ece776b65847a4dc5e3f386
python3 -c "hashlib.sha256(open(f,'rb').read().rstrip(b'\n'))"  → c784dd037f62bf63501fe5f22c10519c50dee7213e5c75a4be2be50d48f2fe04
```

Both values match R9-D09's S6(a) numbers, and the equality across gate revisions is the same
verdict-preservation differential R9-D09 §3 recorded. **Convention recorded here (and recommended
for the round ledger/lessons):** when a receipt quotes a stdout hash for a run compared against a
`reports/round-9`-era value, state whether the trailing newline was stripped — raw-pipe and
stripped hashes of the same bytes differ.

**(b) Disable-witness matrix method limit.** R9-D09 §3 used an in-process guard copy with stubbed
`check_*` functions; the finding's own qualification ("measuring control sensitivity to the owning
checkers, not shipped-CLI behavior") stands as filed. Supplement supplied this round: the idx-7
census re-drove **all 16 domain controls through the shipped CLI as subprocesses** (§2), so the
CLI-level behaviour is now evidenced independently of the stubbed matrix.

**(c) `/tmp` inode exhaustion — still live.**

```sh
df -i /tmp   # tmpfs 1048576 1048576 0 100% /tmp        (2026-10-17)
```

Every scratch write in this shard used `TMPDIR=$PWD/.scratch`; no write to `/tmp` was attempted.

**Disposition — `wont-fix`, documented.** Informational; no artifact change is required. The
conventions are recorded here (a) and the CLI-level supplement (b) and the live environment fact (c)
are attached to the record.

---

## 5. idx 17 — R9-D10 F1: the two committed artifacts' rule sentences differ

**Source claim** (`reports/round-9/d3/findings-10.md` §2 F1): `packet.gates.yml:438` and
`packet.json:16` (`assembly.legacy_projection.rule`) carry different sentences; the 36-byte delta is
the only byte difference between R9-D10's independent reconstruction and the committed projection.
Recommendation: unify the sentence **or** record the difference.

**Live confirmation (2026-10-17).** Both strings are present as reported; the generator holds two
separate literals (`tools/assemble-culture-d3.py:374-377` for the projection, `:396-400` for the
packet). Patching the sentence in a scratch copy of `packet.gates.yml` reproduces R9-D10's
arithmetic independently:

```text
committed sha256 : 306bcac7b920840ae26f544afcf39a1f09666d6a8c5e786a5089e89af4c70425  (14191 B)
patched  sha256  : 829c5eb99779d1fed1b336ade42d6174cc5a47e52c7fbfad4dce2693e4eb2cf3  (14227 B)
delta: 36 B — and the patched hash equals R9-D10's own independent reconstruction (mine.yml, 829c5eb9…)
```

**Negative claim, with its sweep:** no consumer reads either sentence.
`grep -rn "assembly\.rule\|legacy_projection\|native constructed forms only" tools/ examples/culture-d3/*.json reports/round-7/d3-contract.json`
(excluding `tools/assemble-culture-d3.py`) returns only: the two artifact literals, the round-7
contract's prose, and a frozen round-9 handoff-check copy — **no gate or tool reads the strings**;
`grep -rn "assembly\|legacy_projection" tools/gates/*.py` returns only unrelated `rite: "guild
assembly"` fixtures. No byte-level cross-artifact assertion exists today.

**Why not fix it in this round.** The unify step is a generator edit **plus regeneration**, and
`examples/culture-d3/packet.gates.yml` is pinned in `expected.json`'s 24-entry manifest
(`…/packet.gates.yml: 306bcac7…`); the patched bytes hash to `829c5eb9…` ≠ the pin, so the edit
would turn the D3 frozen leg red until a re-pin — a re-pin that would then owe R9-S1's
re-verification record. Cost (acceptance-affecting, cross-shard) far exceeds the benefit
(informational, no behaviour).

**Disposition — `wont-fix`, documented, control attached.** The difference is **recorded here as
intentional** (F1's own second option); the patched-hash control above proves the divergence is
exactly one sentence and that the "fix" is acceptance-affecting. Recommendation for the next
generator-touching round: unify at a re-pin, or add a `limits` line stating the two keys are worded
differently by design.

---

## 6. Rows beyond 15 — re-verification of idx 18-23 (resolved-at-source)

All receipts 2026-10-17 at `e3a1ec9`; commands from the lane root.

### 6.1 idx 18 — R8 S1 (`--selftest` RecursionError at `6a80ffe4`): holds

```sh
python3 tools/d2-typed-labels.py --selftest    # exit=0; grep -c Traceback → 0
# last line: "selftest: 39/39 checks passed — the three shard control matrices, the loader/parser
#  malformed cases, the live-packet typing and reconciliation cases, and the CLI emit/check/tamper
#  controls; no file outside the temporary directory touched"
grep -n '^def selftest' tools/d2-typed-labels.py   # 1369 (rank block), 2598 (CLI selftest)
grep -n 'selftest_rank_block' tools/d2-typed-labels.py  # 66 (docstring), 1452 (alias), 2619 (call)
```

Resolved and still green. **Latent fragility (new observation, not a regression):** the alias
`selftest_rank_block = selftest` at `:1452` binds the rank-block function (defined `:1369`) *before*
`:2598` rebinds the module name `selftest` to the CLI selftest; the call at `:2619` therefore reaches
the rank block. The R8 defect shape (an alias placed after the rebind) is gone, but the correctness
now depends on the definition order — a future edit that moves the alias below `:2598` reintroduces
the recursion. Worth a note for the tool's owner; no change made.

### 6.2 idx 19 — R8 S4 (`D2L-*` vocabulary absent at `623b5b1f`): holds

```sh
grep -c "D2L-" tools/d2-typed-labels.py            # 69
grep -c "D2L-" examples/culture-d2/typed-labels.d2.yml   # 37
python3 tools/d2-typed-labels.py --json            # live codes: D2L-FORM-UNRESOLVED ×10, D2L-NATIVE ×2, R-RANK-CONFLICT ×4
```

`D2L-RANK` exists as a finding class (`tools/d2-typed-labels.py:424`, `:2226`) and the live
`R-RANK-*` codes are aliased to it (`:2253` `("R-RANK-", "D2L-RANK")`); the emitted rank code on the
live packet is `R-RANK-CONFLICT`. Vocabulary confirmed present; the tracker row's expectation
"report emits D2L-FORM-UNRESOLVED, D2L-NATIVE, D2L-RANK" is accurate with the alias nuance above.

### 6.3 idx 20 — R8 S5 (exactly three label kinds): holds

`.scratch/d2-now.yml:515-519` (fresh `--emit`) carries
`"label_kinds": ["translated-label", "native-form", "borrowed-strata"]` — exactly three, matching
the spec. The artifact agrees (`typed-labels.d2.yml` carries the same list).

### 6.4 idx 21 — R8 S7 (exit map): holds

```sh
python3 tools/d2-typed-labels.py --json > .scratch/d2.json; echo $?   # exit=1, findings=16, holds=15
```

Code: `tools/d2-typed-labels.py:812` `exit_code = 2 if fails else (1 if holds else 0)`; the CLI
document path mirrors it at `:2493` (`2 if any D2L-DATA else (1 if hard else 0)`). The R8 defect
(exiting 0 with holds present) is gone: 15 holds → exit 1. Limit of this receipt: the live D2 packet
deliberately carries owed form slots, so no hold-free live packet exists to exercise the exit-0
branch directly; that branch is evidenced by the quoted code and the selftest's fixture controls,
not by a live clean packet. (`--check` also exits 1, but for a different reason — §8.2.)

### 6.5 idx 22 — R8 S8 (CLI shape + byte-deterministic `--emit`): holds; residual re-checked

```sh
python3 tools/d2-typed-labels.py --help   # --packet / --json / --emit PATH / --check [PATH] / --selftest
python3 tools/d2-typed-labels.py --emit .scratch/e1.yml ; python3 tools/d2-typed-labels.py --emit .scratch/e2.yml
sha256sum .scratch/e1.yml .scratch/e2.yml   # both a3aa452cd5ae77c351d9532a707fb1f1ababf77c3fad8b9d28089e6958364a43
```

The residual in the row ("D15's fragment still needs its checklist pass") is **superseded by later
evidence, not rewritten**: `reports/round-8/depth/docs.md` §3 is the docstring audit against that
fragment, §5.1 left its interface lines `to-verify` *because* the tool then failed its own selftest;
that condition is now met (39/39, stable revision `0da0015f` committed at `e1694ba` and unchanged
through round 9 — `reports/round-9/d3/interop.md` records the same tool digest). Spot re-checks of
two §3.0 lines at this revision: imports are stdlib-only (`tools/d2-typed-labels.py:79-90` —
`argparse, contextlib, hashlib, io, json, pathlib, re, runpy, shutil, subprocess, sys, tempfile`; no
`socket`/`urllib`/`requests`/`http` import, sweep 2026-10-17) and the tool is non-mutating
(`sha256sum examples/culture-d2/packet.d2.yml examples/culture-d2/typed-labels.d2.yml` after every
run in this shard → `e0f21509…` / `e70ba147…`, both unchanged; `git status --short -- examples/culture-d2/ tools/` empty). Filed-report bytes were not touched; this paragraph is the correction
entry.

### 6.6 idx 23 — R8 S9 (contract §5 fields; `pronunciation` residual): holds, residual honest

Fresh `--emit` counts: `script` 58, `representation` 58, `scheme` 68, `evidence` 58,
`pronunciation` 0 (`grep -c "\"<field>\"" .scratch/d2-now.yml`, 2026-10-17). The residual stands as
filed. Source evidence that the 0 is honest, not a gap in the tool:
`grep -rn pronunciation examples/culture-d2/components/` → 3 hits, all prose policy
(`02-phonology.yml:464` PC-9 register policy, `04-orthography.yml:395` an E3 spelling-revival
feature, `12-rank-rules.yml:377` a precedent sentence) — **no per-label pronunciation datum exists
in the components**, so emitting the field would fabricate one. Disposition: residual documented;
contract §5's field list is aspirational for D2 at this revision.

---

## 7. Tracker rows (ready to paste) — for R10-O14

This shard may not write the shared tracker; the scribe can merge these. Dispositions use the
tracker's own vocabulary plus the row's evidence locator.

```json
[
 {"idx": 7,  "disposition": "wont-fix",
  "reason": "Superset semantics confirmed by a count-aware re-drive of all 16 domain controls through the shipped CLI (multiset-exact 11, differing 5: 1 extra distinct id D3-BRIDGE + 4 multiplicity-only); run_case subset check re-read at tools/check-evidence-coupling.py:1703-1705; the guard is not this shard's write scope and the acceptance legs do not rely on exact verdicts. Recommendation (b) adopted: subset semantics recorded as the accepted standard with the census as the standing exactness check. Residual: a guard regression that over-fires stays green in the selftest and is visible only in the census.",
  "control": "reports/round-10/fix-09.md §2 (census + 16/16 bogus-expectation self-test)"},
 {"idx": 15, "disposition": "fixed-with-control",
  "reason": "Current tool emits borrow.layer_ref and resolves it against the packet's declared layers (tools/d2-typed-labels.py:569, :701-704, fail path :704); donor_layer absent (count 0 in projection and artifact); artifact carries layer_ref/donor_form/substitutions on L-26 (typed-labels.d2.yml:2409-2461).",
  "control": "reports/round-10/fix-09.md §3 — renamed-layer copy → D2L-BORROW 'does not resolve to a declared layer'; g:k→g:t layer edit → D2L-BORROW 'substitutions derive tas from donor gas, not kas'"},
 {"idx": 16, "disposition": "wont-fix",
  "reason": "Informational conventions; all three parts reproduced live: (a) raw 506d1632… vs stripped c784dd03… on identical 458-byte gate stdout, convention recorded in this round's report; (b) stubbed-matrix limit stands, supplemented by the shipped-CLI census (§2); (c) df -i /tmp = 1048576/1048576 100%, TMPDIR=.scratch used throughout.",
  "control": "reports/round-10/fix-09.md §4"},
 {"idx": 17, "disposition": "wont-fix",
  "reason": "Divergence is exactly one sentence (patched scratch bytes 829c5eb9… = R9-D10's independent reconstruction, 14227 B vs committed 14191 B); no gate or tool reads either string (sweep in §5); the unify fix is acceptance-affecting (packet.gates.yml is pinned in expected.json at 306bcac7… and the patched hash differs) and would owe an R9-S1 re-pin record. Difference recorded as intentional; recommend unify-at-re-pin or a limits line.",
  "control": "reports/round-10/fix-09.md §5"},
 {"idx": 18, "disposition": "fixed-with-control",
  "reason": "Re-verified at e3a1ec9: --selftest 39/39 exit 0, 0 tracebacks; duplicate-def shape understood (rank block :1369 aliased at :1452 before the CLI rebind at :2598; call :2619). Latent fragility recorded (alias ordering).",
  "control": "reports/round-10/fix-09.md §6.1"},
 {"idx": 19, "disposition": "fixed-with-control",
  "reason": "Re-verified: D2L-* ×69 tool / ×37 artifact; live codes D2L-FORM-UNRESOLVED ×10, D2L-NATIVE ×2, R-RANK-CONFLICT ×4 with R-RANK-* aliased to D2L-RANK (:2253).",
  "control": "reports/round-10/fix-09.md §6.2"},
 {"idx": 20, "disposition": "fixed-with-control",
  "reason": "Re-verified: label_kinds exactly ['translated-label','native-form','borrowed-strata'] in the fresh emit (:515-519).",
  "control": "reports/round-10/fix-09.md §6.3"},
 {"idx": 21, "disposition": "fixed-with-control",
  "reason": "Re-verified: --json exit 1 with 15 holds; exit rule quoted (tool :812). Exit-0 branch evidenced by code + selftest fixtures (no hold-free live packet exists).",
  "control": "reports/round-10/fix-09.md §6.4"},
 {"idx": 22, "disposition": "fixed-with-control",
  "reason": "Re-verified: five CLI flags; two emits byte-identical (a3aa452c…); residual re-checked — docs.md §5.1's to-verify gate (tool failing its own selftest) is met since e1694ba; stdlib-only imports and non-mutation spot-checked; filed bytes untouched.",
  "control": "reports/round-10/fix-09.md §6.5"},
 {"idx": 23, "disposition": "fixed-with-control",
  "reason": "Re-verified: script/representation/scheme/evidence = 58/58/68/58; pronunciation = 0 and the components carry no per-label pronunciation datum (3 prose-only hits) so the residual is honest; contract §5 list noted as aspirational for D2.",
  "control": "reports/round-10/fix-09.md §6.6"}
]
```

---

## 8. Residuals, corrections and new observations (reported, not absorbed)

1. **Tracker paraphrase (idx 7).** The tracker row reads "5 of 16 domain controls emit extra ids";
   the source table (correct) shows 1 distinct extra id + 4 multiplicity differences. No action
   needed beyond the scribe's wording; the census in §2 is the precise form.
2. **`python3 tools/d2-typed-labels.py --check` exits 1 on the live tree** — the committed artifact
   `typed-labels.d2.yml:9` pins `packet_sha256 8da90b07…` while the live packet is `e0f21509…`; the
   diff against a fresh emit is exactly that one line. This is **pre-existing and already documented**
   (`reports/round-9/d3/interop.md` §4, inherited from round 8, reproduced by this shard) — it is not
   one of my rows and I did not regenerate the artifact (write scope). Flagged for the orchestrator:
   it is a stale pin on a committed pair, one `--emit` away from green, and it makes `--check` red for
   a reason unrelated to holds (§6.4).
3. **`/tmp` remains 100% inode-exhausted** (live measurement, §4.3) — re-runners need
   `TMPDIR=$PWD/.scratch`; the in-lane `.scratch/` is untracked.
4. **Counting-command nuance:** `grep -c` exits 1 when the count is 0 (hit while counting
   `pronunciation`); a counting script that chains `grep -c` under `set -e` will fail on a
   legitimate zero. Recorded because the round's counting commands aggregate such probes.
5. **Selftest alias ordering** (§6.1) — latent fragility in `tools/d2-typed-labels.py`, no
   regression; owner's call.
6. **Out of province / not assessed:** canon, real-world rights, game mechanics, general research
   method (PROVINCE.md). No lore acceptance is claimed or implied; this file is engineering evidence.

---

## 9. Reproduction

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch                     # /tmp is inode-exhausted
# idx 7 — census (harness: .scratch/r10o09-superset-census.py; the multiset variant is inline in §2)
python3 .scratch/r10o09-superset-census.py     # set-based: exact 15, superset 1, missing 0; self-test 16/16
# idx 15 — layer-ref controls
python3 tools/d2-typed-labels.py --json                                        # exit 1, no D2L-BORROW
cp examples/culture-d2/packet.d2.yml .scratch/mut-layer.yml                    # rename layers[0].name once
python3 tools/d2-typed-labels.py --packet .scratch/mut-layer.yml --json        # D2L-BORROW, exit 1
# idx 16 — convention + environment
git show 57c3ce6:tools/gates/naming-collision-gate.py > .scratch/naming-gate-r7.py
python3 .scratch/naming-gate-r7.py examples/culture-d3/packet.gates.yml | sha256sum       # 506d1632…
df -i /tmp                                                                     # 1048576 1048576 0 100%
# idx 17 — rule-sentence delta
python3 - <<'PY'   # patch the sentence in a scratch copy; hashes as in §5
PY
# rows 18-23 — re-verification
python3 tools/d2-typed-labels.py --selftest ; python3 tools/d2-typed-labels.py --help
python3 tools/d2-typed-labels.py --json | python3 -c "import json,sys,collections;d=json.load(sys.stdin);print(collections.Counter(f['id'] for f in d['findings']))"
python3 tools/d2-typed-labels.py --emit .scratch/e1.yml ; python3 tools/d2-typed-labels.py --emit .scratch/e2.yml
sha256sum .scratch/e1.yml .scratch/e2.yml examples/culture-d2/packet.d2.yml examples/culture-d2/typed-labels.d2.yml
```

---

## 10. Limits

- The idx-7 census covers `controls.json`'s 16 **domain** controls; the 3 positive and 4 malformed
  controls were not re-driven here (R9-D09 §3.1 applied all 19 patches and ran the real CLI, §3.3
  checked the malformed kinds; not re-opened).
- `--check`'s stale-pin red (§8.2) is reported from measurement, not fixed — regenerating the D2
  artifact is outside this shard's write scope and would collide with the round's other writers.
- The exit-0 branch of the D2 exit map (§6.4) has no live hold-free packet to exercise it.
- Verdicts are pinned to the hashes in §0; a later tool/artifact revision invalidates them and
  requires a re-run of §2-§6.
- The census harness is scratch (not committed, per the round's write rule); it is reconstructible
  from §2 and §9.

FILES: reports/round-10/fix-09.md | SUMMARY: Dispositioned all ten tracker rows assigned to R10-O09 (indices 7, 15 and every row beyond 15) with live controls — idx 7 (superset control matcher) wont-fix with a count-aware re-drive of all 16 domain controls through the shipped CLI (5 differ: 1 distinct extra id D3-BRIDGE + 4 multiplicity-only) and a 16/16 bogus-expectation self-test; idx 15 (layer reference shape) fixed-with-control — the tool now emits borrow.layer_ref resolved against the packet's declared layers with a fail path and donor_layer is gone, demonstrated by two scratch mutations that fire D2L-BORROW; idx 16 (conventions/environment) and idx 17 (two rule sentences, 36-byte delta, patched bytes = R9-D10's independent reconstruction, no consumer reads either string, the fix is acceptance-affecting) wont-fix with reasons and controls; idx 18-23 re-verified at e3a1ec9 (selftest 39/39, D2L-* ×69/×37, exactly three label kinds, exit 1 with 15 holds, byte-identical emits, contract §5 counts 58/58/68/58 with an honest pronunciation-0 residual); residuals reported: the pre-existing documented d2 --check stale packet pin, /tmp still inode-exhausted, a latent selftest alias-ordering fragility, and a grep -c zero-count nuance; the shared tracker was not written (write scope) — ready-to-paste rows are in §7.
