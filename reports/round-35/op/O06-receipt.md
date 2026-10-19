- Seat: O06 | scribe | claim O | date 2026-10-19 | baseline 4a7aede

# O06 — operability receipt draft (claim O / R34-N1 hardening)

Cut 2026-10-19T08:22:29Z (`date -u +%FT%TZ`) at HEAD
`4a7aede22cd8395b01ce6dd9f46bcae364ca24e4` (`git rev-parse HEAD`);
`git status --porcelain` → `?? reports/round-35/` only.

Mission (`reports/round-35/targets.json`, seat O06): "Operability receipt draft."
This fragment is the draft receipt: the before-state measured by this seat, the
mechanism pinned to the line, the counting-command ledger, two reconciliations
the O block still owes (measured here, not asserted from peers), and the
landed-changes material with the after-column marked owed.

## 0. Isolation, dependency status, fences kept

- Isolation: `git archive HEAD | tar -x -C .scratch/o06-iso/repo`; the renderer
  in the copy hashes to the same `34c85f57…` as the in-tree file. The r6 replay,
  both real-artifact negatives and the v1 mirror probe ran **only** in the copy.
- Non-freeze in-tree runs (`--profile v3 --quiet`, `--selftest`) were made with
  `git status --porcelain` captured before and after: identical (no tree
  mutation). No `--freeze` was run anywhere; no `reports/round-*/run-validation.py`
  was executed anywhere (F-C13-1 rule).
- Dependencies landed at this cut and read in full: `scout/K03-keyerror-path.md`,
  `op/O08-validation-legs.md`, `op/O10-scribe.md`, `scribe/S02-o-receipt.md`.
  **Folded after the first cut** (landed while this seat ran):
  `op/O01-patch-draft.md` (patch sha `ebc6e1cc…`, patched renderer `84276189…`),
  `op/O02-controls.md`, `op/O03-isolated-verify.md` (patch derived from P02 §3
  verbatim; patched renderer `1a003d67…`), `op/O04-regressions.md`; their values
  are folded into §3/§5/§6/§7 and their Owed cells dropped. **Landed after this
  seat's last fold, not read here:** `op/O05-verify.md`, `op/O09-gap-fill.md`,
  `op/O11-verify-2.md` (the two independent verifications of O03's patch and the
  second gap-fill — the integrator's fold must reconcile their observed counts
  and quiet-mode readings with §3.1-§3.3); `plan/P02-oa-plan.md` and
  `review/R04-o-review.md` likewise landed unread (see Owed). **Still not
  landed at the last check:** `op/O07-gap-fill.md`, `review/R05-o-review.md`;
  `reports/round-35/run-validation.py` does not exist.
- Claim-O after-state is therefore **not achieved**: the renderer is unpatched
  (live sha256 `34c85f57…` == `git show HEAD:tools/exercise-handoff-e2e.py`).
  Three draft variants exist and only one may land (§3.3).

## 1. Before-state — nine measurements (all this seat, reproducible)

Commands from the lane root or the isolated copy, with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

| # | command | exit | observed |
|---|---|---|---|
| B1 | `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json` (isolated) | **1** | stdout empty; stderr `Traceback … line 3822, in v3_exercise` / `KeyError: 'reports/round-20/handoff/claims-map.md'`; no summary line, no named diagnostic |
| B2 | `… --profile v3 --quiet` (isolated **and** in-tree) | **0** | `handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19` |
| B3 | `… --profile v3 --selftest` | **0** | header `… plus 39 controls:`; `grep -c '^  - '` = **40** result lines |
| B4 | `… --selftest` (default profile v1, the claim's counting command) | **0** | header `… plus 17 controls:`; 18 result lines |
| B5 | real-artifact negative, flipped `packet_sha256` in `reports/round-34/handoff/declared-in-r7/expected.json` (isolated tamper copy) | **2** | `handoff-v3: E2E-BASELINE: baseline integrity digest mismatch — the baseline file was edited without re-freezing (re-freeze with --profile v3 --freeze DIR and read the diff it prints)` |
| B6 | real-artifact negative, content-tampered read-set member `reports/round-19/validation.json` (isolated tamper copy) | **1** | non-quiet: `handoff-v3: E2E-DIGEST: 1 read-set file(s) changed since the baseline was frozen: reports/round-19/validation.json`; `--quiet`: summary line only, **no code token**; `--quiet --json`: `"code": "E2E-DIGEST"` plus a failing record `reports/round-19/validation.json: frozen 7dbc346ccab1… live e5ac9806abe2…` |
| B7 | v1 mirror-site probe: synthetic v1 baseline (filed `reports/round-11/handoff/expected.json` + one vanished member `reports/round-20/handoff/claims-map.md`, re-signed with the module's own `v1_baseline_digest`), `--profile v1 --quiet --baseline <abs path>` (isolated) | **1** | `Traceback … line 1440, in v1_exercise` / same `KeyError` — the second site is triggerable, not merely latent |
| B8 | `… --profile v1 --quiet` (filed round-11 baseline; isolated) | **1** | pre-existing red, not patch-related: `handoff-e2e: exit=1 fields=? glossary=?/20 findings=? packet_sha256=(not assembled)`; verbose: `handoff-e2e: E2E-DIGEST: 1 read-set file(s) changed since the baseline was frozen: tools/d2-typed-labels.py` (frozen `0da0015f7003…` vs live `2819f68769df…`); agrees with O04 R9 |
| B9 | `… --profile v2 --quiet` (isolated) | **0** | `handoff-v2: exit=0 claims=15 links=50/50 drift=named(tools/harness/packet_links.py round-16)`; agrees with O04 R9 |

**Pinned digests at the baseline.** Renderer `34c85f57…`; r6
`expected.json` `ea1e2927…`, `packet.md` `6ced88ad…`, `freeze.txt` `6fe70c0c…`;
r7 `expected.json` `bbe15887…`, `packet.md` `45f57132…`, `freeze.txt`
`3969954b…`, `twin.json` `0e229138…`, `claims-map.md` `d181de28…`; r20
`claims-map.md` `4b1b9a35…` (still on disk, unchanged). Baseline integrity
digests read from the module: r6 `714b41fc…`, r7 `1fce3820…`.

**Preservation.** Per-file `sha256sum` vs `git show HEAD:<path>` for the nine
tracked files under `reports/round-30/handoff/declared-in-r6/` and
`reports/round-34/handoff/declared-in-r7/`: all **SAME**; the two `run.log`
files are gitignored (`.gitignore:3`) and were not written by any run here.

## 2. Defect mechanism, pinned

- `tools/exercise-handoff-e2e.py:3819` — `drifted = [rel for rel, digest in
  baseline["inputs"].items() if assembly.digests.get(rel) != digest]`: the
  tolerant `.get` selects a vanished member (yields `None` ≠ digest), so the
  refusal intent is correct.
- `:3822` — the *reporting* line indexes `assembly.digests[rel]` directly →
  `KeyError`; `:3823`'s designed `Failed("E2E-DIGEST", …)` is unreachable for
  membership-only drift.
- `:3479-3484` — `V3Assembly.digests` is built over the live `V3_READ_SET`
  only; `:1935-1958` — the live set names the r34 successor map (`:184`).
- Set arithmetic (module import, both `inputs` maps): both 58 members; r6-only
  = `reports/round-20/handoff/claims-map.md` (present on disk at the frozen
  digest — this is membership, not content drift); r7-only =
  `reports/round-34/handoff/declared-in-r7/claims-map.md`; 57 shared.
- Contract broken: `:89` "Exit codes (stable messages, **no traceback**)".
  `EXIT_FAIL = 1` (`:113`) equals CPython's uncaught-exception status, so a leg
  asserting `exit == 1` alone is green on the unfixed tree (K03 §1, O10 R1).
- Second site: `:1435-1441` (v1) is byte-for-byte the same pattern; **B7 shows
  it is triggerable** with any baseline pinning a member the live
  `V1_READ_SET` (`:462`) does not carry. The filed v1 default
  (`reports/round-11/handoff/expected.json`, `:460`) is a 21/21 subset of
  `V1_READ_SET` (baseline-only set = ∅), so the filed chain cannot reach it —
  the exposure is real but synthetic-triggered.

## 3. Two reconciliations — measured here, now sharpened by the landed patch draft

### 3.1 Quiet mode hides the named diagnostic (O10 R2 / O08 leg O1 / O02 §2.5 vs O01 §1) — the one open decision

Measured on the *existing* designed path (B6): with `--quiet`, a refusal prints
only the summary line — the code line at `:4603-4604` is gated by
`not args.quiet`, so **no `E2E-*` token reaches stdout+stderr**. Without
`--quiet` the same run prints `handoff-v3: E2E-DIGEST: …`. The `--json`
document (`:4605-4608`) is *not* quiet-gated and carries `"code"` plus the
failing record's detail, which includes the member path.

Three landed positions, and they conflict:

- **O08's leg O1** asserts the `E2E-READSET` token **and** the member path on a
  `--quiet` run's combined output; **claim O's counting command is `--quiet`**
  (`reports/round-35/claims.json:48`). As the renderer stands, a patch that only
  raises `Failed("E2E-READSET", …)` returns through `:4603` and stays invisible
  in quiet mode — the leg and the claim's own evidence path would both miss the
  name.
- **O02 §2 item 5 proposes the hoist** (`if err and not args.quiet:` → `if err:`
  at `:4603`), recording the trade: a *failing* quiet stdout gains one line, and
  no filed consumer parses a failing quiet stdout (the filed validators read
  `packet_sha256=` from successful runs). O04 §4 (O04-F1) files the same finding
  with three options (hoist; carry the code into the summary line; drop
  `--quiet` from the leg).
- **O03 §2/§7.2 also hoists** (`if err:` in both v1 and v3, v2's print untouched)
  and **measured the result**: its L1 shows the `--quiet` r6 replay printing
  `handoff-v3: E2E-READSET: 1 baseline read-set member(s) are not in this
  revision's read set: reports/round-20/handoff/claims-map.md` with
  `grep -c Traceback` → 0, and its `m12d` control asserts exactly that shape
  (`reports/round-35/op/O03-isolated-verify.md` §5).
- **O01 §1 deliberately declines the hoist** — the binding patch draft leaves the
  `--quiet` summary line byte-identical and the quiet path diagnostic-free,
  because filed rounds quote the v3 `exit=1` line verbatim
  (`reports/round-30/regression.json:698`, `reports/round-22/bleed/evidence/attempt-01-verification.json:241`,
  cited by O01 §1). O01's §4.1 instead directs the acceptance leg to assert the
  **non-quiet** form (exit 1, no `Traceback`, `handoff-v3: E2E-READSET: …`).

So the integrator must pick one of two coherent packages, and the receipt must
record which:

- **Package A (O01 as drafted):** quiet stdout unchanged → O08's O1 must drop
  `--quiet` (or read `--quiet --json`, which today carries `"code"` and the
  member path — measured B6), and the claim's counting command as declared
  cannot demonstrate the name; the receipt must say the evidence command is the
  non-quiet replay.
- **Package B (O02's or O03's hoist):** the quiet run prints
  `handoff-v3: E2E-READSET: …` and both O08's O1 and the claim's counting
  command work as declared; the cost is one extra line on a failing quiet stdout
  (O02 measured no consumer of that surface; O03's L1/m12d demonstrate the
  behaviour on the patched bytes).

What must not happen: the guard lands with neither, leaving O08's O1 and the
claim's own counting command unable to show the name.

What must not happen: the guard lands with neither, leaving O08's O1 and the
claim's own counting command unable to show the name.

### 3.2 Selftest host and count (O10 R1 / O08 O2 / S02 L2 / O04 §7 row 3 / O01 hunk 4 / O02 §4) — three landed counts, one binding

- Measured: `--selftest` = **v1** suite, 17 controls (B4); `--profile v3
  --selftest` = **v3** suite, 39 controls / 40 bullets (B3).
- The r6 row is a v3 baseline, so the superseded-row control can only live in
  `v3_selftest` (`:4154`); S02's L2 (v1 17 → 19) cannot host it. A v1-side
  control would have to be synthetic (B7) and is not what claim O asks for.
- **Three counts are now on record and only one can land:**
  - **O01 (binding draft, hunk 4): one new control `m12c`** → header
    **39 → 40**, bullets **40 → 41**; O01 §3 row 1 and §4.2 measured exactly
    this on the patched isolated copy. O01 deliberately does not duplicate the
    digest path because `m12b` already covers it (`:4430`).
  - **O08 leg O2 / O04 §7 row 3: `≥ 41` controls / `plus 41 controls`, 42
    lines** — one more than O01's patch produces, so O08's O2 would fail on a
    correct O01 patch.
  - **O02's prototype: four controls (`m13a/m13b/m14a/m14b`) → 43** — a richer
    design, but it is a prototype over its own guard.
  - **O03's verified realization (P02 §3 verbatim, §5 L3): three v3 controls
    (`m12c` superseded, `m12d` quiet observability, `m12e` precedence) → header
    42 / bullets 43**, plus a v1 control (`L4`: v1 18 controls, matching S02's
    L2 17 → 19 for the *bullet* count). O03 measured the patched renderer at
    `1a003d67…`.
- Measured anchors that hold under any of them: the "preserved `E2E-DIGEST`
  digest-mismatch path" is already green pre-patch — the v3 suite prints `m12b
  tamper read-set (D4 projection): exit 1 E2E-DIGEST naming the changed file`
  (`:4430`) and `m8 re-typed v2 row: exit 1 E2E-DIGEST` (`:4438`); 10 pre-patch
  lines contain `E2E-DIGEST`.
- Recommendation for the validator: assert the landed control's **name line**
  (the `E2E-READSET` + superseded-row + exit-code triple that O08 §2 O2 and
  O03's m12c both carry) plus a bullet-count floor, and assert the *header* count
  only after reconciling it with the applied patch — the header prints
  `len(results) - 1` while every result is printed (`:4464-4467`), so header and
  bullet counts differ by one by construction.

### 3.3 Three draft variants, one to land (the integrator's single-source decision)

| variant | v1 site | `--quiet` failure line | v3 controls | v3 header / bullets | patched renderer sha | measured by |
|---|---|---|---|---|---|---|
| **O01** §2 (+ optional §5 v1 hunk) | out of the required diff (optional hunk `e784186e…`) | **unchanged** (`if err and not args.quiet`) | 1 (`m12c`) | 40 / 41 | `84276189…` (patch `ebc6e1cc…`) | O01 §3 |
| **O03** §3 (P02 §3 verbatim) | patched | hoisted to `if err:` in v1 and v3 | 3 (`m12c`/`m12d`/`m12e`) + 1 v1 control | 42 / 43 | `1a003d67…` | O03 §5 L1-L9 |
| **O02** §3 (prototype guard) | out of scope | hoisted to `if err:` | 4 (`m13a`/`m13b`/`m14a`/`m14b`) | 43 | not stated (prototype copy) | O02 §4-§6 |

All three satisfy claim O's binding text (`E2E-READSET` + member path, exit 1,
no traceback, r7 chain green, freeze bytes unmoved — each measured). They differ
in blast radius, quiet-path behaviour and control count, and **two must not land
at once** (O03 §Owed says the same). Consequences the receipt pins:

- Whichever lands, the validator's selftest assertion must match **that**
  variant's count (O01 40/41, O03 42/43, O02 43 header / 44 bullets by the same
  off-by-one) and the quiet-mode assertion must match its quiet behaviour (§3.1)
  — this is why §4's ledger and §5's table are written per-variant rather than
  as a single number.
- The r6 replay's observable output differs between variants: under O01 the name
  appears only off `--quiet`; under O03/O02 it appears on the `--quiet` path too
  (O03 L1 measured `handoff-v3: E2E-READSET: 1 baseline read-set member(s) are
  not in this revision's read set: reports/round-20/handoff/claims-map.md` with
  `grep -c Traceback` → 0 and the single-line code+path regex matching).
- O03 §7.3 also measured the exit-2 (`Unevaluatable`) alternative end-to-end
  (CLI only, controls not re-authored) — if the integrator picks it, four
  assertions flip and `claims.json:48`'s "(expect: exit 1)" becomes a named
  deviation.

## 4. Counting-command ledger (claim O, `reports/round-35/claims.json:47-51`)

| command | status at this cut | evidence / caveat |
|---|---|---|
| `python3 -B tools/exercise-handoff-e2e.py --selftest` | green pre-patch: exit 0, **v1** suite, 17 controls | B4 — this suite cannot host the r6-row control (§3.2); the claim's threshold ("selftest N/N") should name the v3 suite |
| `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json` | **failing pre-patch**: exit 1 with `KeyError`, no diagnostic | B1; under O01's binding draft this command (declared `expect: exit 1`) returns exit 1 with **no** `E2E-READSET` token in quiet mode — the name shows on the non-quiet replay or via `--json`; under Package B (O02's hoist) the token appears in quiet mode too (§3.1) |
| `python3 reports/round-35/run-validation.py` | **absent** — the round is in flight | `ls reports/round-35/run-validation.py` → no such file; spec owed by O08 §6 / the integrator |

## 5. Acceptance-leg reconciliation (measured, not asserted)

| O08 leg | S02 leg | state at this cut |
|---|---|---|
| O1 named diagnostic (r6 replay, `--quiet`, token+path, no traceback) | L1 | pre-patch red (B1); the `--quiet` form is satisfiable only under Package B — O01's draft surfaces the name on the non-quiet path (§3.1) |
| O2 v3 selftest ≥ 41 + anchors | L2 (v1 17→19) | host/count conflict §3.2: O01's binding draft lands header 40 / bullets 41, so `≥ 41` on the header fails by one; assert the m12c line + bullet floor instead |
| O3 r7 default chain exit 0 + packet sha | L3 | green both sides (B2); O01 §3 row 4 measured it identical on the patched copy; sha == on-disk `packet.md` |
| O4 freeze bytes unmoved | L5 | nine tracked files SAME as HEAD (measured); O01 §3 row 6 measured the five r7 files byte-identical on the patched copy; `run.log` digest-only, gitignored |
| O5 patch present (renderer sha ≠ `34c85f57…`) | — | red pre-patch; O01's draft names the patched digest `84276189…` (to be re-measured on the applied bytes) |
| O6 validator fences (no `--freeze`, no filed runner) | L6 (round acceptance) | n/a until `run-validation.py` exists |
| — | L4 m12a/m12b/m8 preserved | green pre-patch (B3); B5/B6 independently confirm the same shapes on the real r7 baseline; O01 §3 row 5 and O02's m14a/m14b cover the boundary |

## 6. Landed-changes / fleet-report material (draft; after-column owed)

| surface | before (4a7aede, measured) | after (three drafts; owed on the applied bytes) |
|---|---|---|
| `tools/exercise-handoff-e2e.py:3819-3823` | exit 1 + `KeyError` at `:3822`, no diagnostic (B1) | every variant lands a roster/superseded guard raising `E2E-READSET` at exit 1 with the member named; observed on patched copies: O01 §3 row 3 (`read-set-roster` record + `handoff-v3: E2E-READSET: …`), O03 §5 L1 (`--quiet` prints the code+path line, no traceback) |
| `tools/exercise-handoff-e2e.py` digest | `34c85f57…` | O01 `84276189…` / O03 `1a003d67…` — ⟨owed: the applied file's sha256, plus a **new** repin row (`reports/round-34/handoff/repin.json:11` is filed bytes)⟩ |
| `v3_selftest` control matrix | 39 controls / 40 bullets (B3) | O01 40/41 (`m12c`), O03 42/43 (`m12c`/`m12d`/`m12e`), O02 43/44 — one variant lands; the validator's count must match it (§3.2/§3.3) |
| `main()` quiet contract (`:4603`) | failing `--quiet` run prints summary only | O01 keeps it byte-identical; O02 §2.5 and O03 §2/§7.2 hoist `if err:` and O03 measured the quiet-path code line — ⟨owed: the integrator's recorded choice (§3.1)⟩ |
| r7 default chain | exit 0, packet `45f57132…` (B2) | unchanged on every patched copy (O01 §3 row 4, O03 L2) |
| v1 default chain | exit 1, `E2E-DIGEST` naming `tools/d2-typed-labels.py` (B8) | unchanged in substance (O03 L9: same file, same digests, exit 1 before and after; the hoist only adds the code line under `--quiet`) |
| filed freeze bytes | 9/9 SAME as HEAD; no `--freeze` run | unchanged (O01 §3 row 6, O03 §6) |
| v1 mirror site `:1435-1441` | same pattern, triggerable (B7) | O01 §5 offers an optional behavior-preserving hunk (`e784186e…`); O03 patches it as part of its variant; recommendation stands: apply or route as a named finding, never silently (O10 F1) |

Paste-ready wording for the round report's operability row (fill the ⟨owed⟩
values after the patch lands; the fuller block is O10 §"Paste-ready"):

> **O / operability:** the r6-row replay died with an unhandled `KeyError:
> 'reports/round-20/handoff/claims-map.md'` at `tools/exercise-handoff-e2e.py:3822`
> (exit 1, no diagnostic) → ⟨owed⟩; r7 default chain exit 0 both sides, packet
> `45f57132…` unchanged; v3 selftest 39 → ⟨owed⟩ controls; the designed
> `E2E-DIGEST`/`E2E-BASELINE` tamper legs still trip (B5, B6, m12a/m12b).

## 7. Findings for the record (observations, not rulings)

- **O06-F1 — quiet mode suppresses every named diagnostic** (measured, §3.1);
  it affects O08's O1 as written and the claim's own `--quiet` counting command.
  Remedies now split: O02 §2 item 5 and O03 §2/§7.2 hoist the print (`if err:`,
  O03 measured the result), O04-F1 lists three options, and **O01 §1
  deliberately declines** (filed rounds quote the quiet `exit=1` line verbatim).
  Owner: integrator — pick Package A (leg reads the non-quiet form / `--json`)
  or Package B (hoist), and record it.
- **O06-F2 — the count expectations conflict and must follow the variant that
  lands** (O01 = one control → header 40 / bullets 41; O03 = three v3 controls →
  42/43; O02 = four → 43/44; O08 leg O2 and O04 §7 row 3 expect 41/42; §3.2/§3.3).
  Owner: integrator/validator author — assert the `E2E-READSET` superseded-row
  control line plus the count of the applied variant, never a bare header floor.
- **O06-F3 — the v1 mirror site is triggerable**, not merely latent (B7;
  corroborates O10-F1 / K03 §2's "latent only" with the synthetic-baseline
  qualifier). Owner: O01/R04 decision.
- **O06-F4 — the drift leg is one-directional and its green count text
  over-claims** (`:3819` iterates baseline members; `:3824` counts
  `len(V3_READ_SET)`). Found and executed first by S02 (§3 of
  `scribe/S02-o-receipt.md`); this seat's B5/B6 runs are consistent with it and
  add nothing beyond corroboration. Not widened by claim O's `after_required`.
- **O06-F5 — the v1 default chain is red pre-existing at HEAD** (B8): exit 1,
  `E2E-DIGEST` naming `tools/d2-typed-labels.py` (frozen `0da0015f…` vs live
  `2819f687…`), independent of this round's patch; the v2 chain is green (B9).
  Agrees with O04 R9. Consequence for the receipt: the claim's threshold "the r7
  default chain still exits 0" is about **v3** and must not be read as "every
  profile's default chain is green" — the v1 red is pre-existing filed-baseline
  drift, out of claim O's scope, and the patch must leave it exactly as it is.
- `to-verify`: whether the integrator lands exit 1 or exit 2 for the new code —
  both satisfy claim O (`claims.json:45`, `:51`). The three landed drafts all
  choose **exit 1** (`Failed` class): O01 §1 decision 2 (binding draft),
  O02 §2 item 1, K03 §4's primary recommendation; the filed r6 control records
  exit 1 (`reports/round-34/handoff/repin.json:19-21`). O08's leg accepts {1, 2}.
  If the integrator instead lands exit 2, the receipt must record the deviation
  from `claims.json:48`'s "(expect: exit 1)" and the code must move to the
  `Unevaluatable` family (O01 §Owed notes exactly which four sites change).

## Owed

- `reports/round-35/op/O01-patch-draft.md` — **landed and folded**; the remaining
  owed work is the *applied* state: the integrator single-sources one variant
  (§3.3), applies it, re-measures the renderer sha256 and files a new repin row.
- `reports/round-35/op/O03-isolated-verify.md` — **landed and folded** (patched
  renderer `1a003d67…`, verified legs L1-L9); its own owed item stands: the
  integrator must not land it alongside O01's draft, and the exit-2 alternative
  it measured needs the `claims.json:48` deviation recorded if adopted.
- `reports/round-35/op/O05-verify.md`, `op/O09-gap-fill.md`,
  `op/O11-verify-2.md` — landed after this seat's last fold and **not read
  here**; O05/O11 are the independent isolated verifications of the patch and
  O09 the second gap-fill. The remaining owed work is their reconciliation with
  §3.1-§3.3 plus fresh observation on the **applied** in-tree bytes (r6 replay
  code line + exit, r7 chain, v3 selftest count).
- `reports/round-35/op/O07-gap-fill.md`, `review/R05-o-review.md` — not landed
  at the last check.
- `reports/round-35/plan/P02-oa-plan.md` and `review/R04-o-review.md` — landed
  but **not read by this seat** (they arrived after this seat's cut): P02 owns
  the exit-class convention O01 §Owed defers to and its §3 sketch is what O03
  applied verbatim; R04 is the adversarial pass on claim O. The integrator's fold
  must reconcile them with §3.1-§3.3 before the validator's counts and
  quiet-mode assertions are fixed.
- `reports/round-35/run-validation.py` — absent; its claim-O group should encode
  the §3.1 choice (quiet visibility), the §3.2/§3.3 applied count and the
  single-sourced variant as decisions, not as pre-patch assumptions.
- The final receipt fold: `scribe/S02-o-receipt.md` is rev 1 (pre-peer-fold) at
  this cut; a later revision (not an edit) should fold this draft, O01, O02, O03,
  O04, O08, O10 and the patch fragments.
- Landed peers folded at this revision: `op/O01-patch-draft.md`,
  `op/O02-controls.md`, `op/O03-isolated-verify.md`, `op/O04-regressions.md`
  (read in full; their Owed cells dropped above).

## Citations

Paths:lines

- `tools/exercise-handoff-e2e.py:89-93` (exit-code/no-traceback contract),
  `:112-114` (`EXIT_PASS/EXIT_FAIL/EXIT_UNEVALUATED`), `:184` (`CLAIMS_MAP`),
  `:460`, `:462` (v1 baseline default, `V1_READ_SET`), `:1435-1441` (v1 mirror
  block; crash `:1440`), `:1933-1934` (v3 defaults), `:1935-1958` (`V3_READ_SET`),
  `:3478-3484` (`V3Assembly` digests), `:3772-3804` (`v3_load_baseline`
  integrity checks), `:3819`, `:3822`, `:3823`, `:3824` (drift leg),
  `:4154` (`v3_selftest`), `:4412`, `:4422`, `:4430`, `:4438`, `:4457`
  (controls), `:4461-4467` (selftest count/print), `:4539`, `:4578` (CLI
  dispatch), `:4594-4602` (summary), `:4603-4604` (quiet-gated code line),
  `:4605-4608` (`--json`), `:4613`
- `reports/round-35/claims.json:40` (claim O), `:45` (`after_required`),
  `:47-51` (counting commands, thresholds), `:56-62` (non-goals)
- `reports/round-35/targets.json` (seat O06; `shared_rules`), `REGIMEN.md:25-58`
- `reports/round-34/handoff/repin.json:11`, `:19-21`, `:50` (R34-N1 routed)
- Peers read in full: `reports/round-35/scout/K03-keyerror-path.md`,
  `reports/round-35/op/O08-validation-legs.md`, `reports/round-35/op/O10-scribe.md`,
  `reports/round-35/scribe/S02-o-receipt.md` (S02-F1 attributed in §7), and
  folded after the first cut: `reports/round-35/op/O01-patch-draft.md` (§1 the
  two decisions + the deliberate quiet non-change, §2 the fenced diff with sha
  `ebc6e1cc…` / patched renderer `84276189…`, §3 the isolated verification table,
  §4 acceptance-leg guidance, §5 the optional v1 hunk `e784186e…`),
  `reports/round-35/op/O02-controls.md` (§2 item 5 quiet hoist, §4 m13a/m13b,
  §5 m14a/m14b, §6 expected outputs),
  `reports/round-35/op/O03-isolated-verify.md` (§2 patch shape, §3 the fenced
  diff with patched renderer `1a003d67…`, §5 legs L1-L9, §7 scope choices and
  the measured exit-2 alternative),
  `reports/round-35/op/O04-regressions.md` (§2 R9 profiles, §3 shared drift loop,
  §4 O04-F1, §7 row 3 count)
- Landed but **not read** by this seat: `reports/round-35/plan/P02-oa-plan.md`,
  `reports/round-35/review/R04-o-review.md` (see Owed)
- Frozen artifacts: `reports/round-30/handoff/declared-in-r6/{expected.json,packet.md,twin.json,freeze.txt}`,
  `reports/round-34/handoff/declared-in-r7/{expected.json,packet.md,twin.json,freeze.txt,claims-map.md}`,
  `reports/round-11/handoff/expected.json`, `reports/round-20/handoff/claims-map.md`,
  `reports/round-19/validation.json`

Commands (this seat; `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`)

- `git rev-parse HEAD` → `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4`;
  `git status --porcelain` → `?? reports/round-35/` (before and after the
  in-tree runs: `diff pre post` → no change)
- `git archive HEAD | tar -x -C .scratch/o06-iso/repo`; `sha256sum` of the
  renderer in both trees → `34c85f57…` (equal)
- B1 `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json` (isolated) → exit 1, `KeyError` traceback (`:3822`)
- B2 `… --profile v3 --quiet` (isolated and in-tree) → exit 0, packet `45f57132…`
- B3 `… --profile v3 --selftest` → exit 0, `plus 39 controls`, 40 `^  - ` lines
- B4 `… --selftest` → exit 0, `plus 17 controls`, 18 lines
- B5 flipped `packet_sha256` in the r7 baseline (isolated tamper copy) → exit 2, `E2E-BASELINE: baseline integrity digest mismatch — the baseline file was edited without re-freezing …`
- B6 content-tampered `reports/round-19/validation.json` (isolated tamper copy) → exit 1, `E2E-DIGEST: 1 read-set file(s) changed since the baseline was frozen: reports/round-19/validation.json`; `--quiet` → summary only, no token; `--quiet --json` → `"code": "E2E-DIGEST"` + the member path in `checks`
- B7 synthetic v1 baseline (one vanished member, re-signed) → exit 1, `KeyError` traceback (`:1440`)
- B8 `… --profile v1 --quiet` (filed round-11 baseline, isolated) → exit 1, summary only; verbose → `handoff-e2e: E2E-DIGEST: 1 read-set file(s) changed since the baseline was frozen: tools/d2-typed-labels.py` (frozen `0da0015f7003…` vs live `2819f68769df…`)
- B9 `… --profile v2 --quiet` → exit 0, `handoff-v2: exit=0 claims=15 links=50/50 drift=named(tools/harness/packet_links.py round-16)`
- `python3 -B` module import: `V3_READ_SET` vs both `inputs` maps → 58/58, r6-only = r20 claims-map, r7-only = r34 claims-map, 57 shared; `V1_READ_SET` = 21 == the filed v1 baseline's 21 (baseline-only ∅); `grep -o 'E2E-[A-Z]*'` → `E2E-READSET` 0 occurrences
- `sha256sum` (digests in §1) and per-file `sha256sum` vs `git show HEAD:<path>` for the nine tracked freeze files → all SAME
- `grep -n 'E2E-DIGEST' .scratch/o06-iso/selftest-v3.out` → 10 lines (m8, m12b, 8 edge-carry controls)
