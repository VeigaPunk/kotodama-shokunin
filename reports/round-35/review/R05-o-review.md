- Seat: R05 | reviewer | O | date 2026-10-19 | baseline 4a7aede

# R05 — second O pass: evidence quality of the isolated verifications

**Mission** (`reports/round-35/targets.json:352-355`): *"Second O pass: the isolated
verifications' evidence quality."* At my first listing (`reports/round-35/op/`) only O04,
O08 and O10 existed; O01, O02, O03, O05 and O11 landed during my run and were read in full.
I audited them against a ground truth I built myself (an isolated `git archive 4a7aede`
copy) rather than against their own summaries.

## 1. Method and dependency status

- Own isolated copies: `.scratch/r05-iso` (pristine), `.scratch/r05-iso2` (O01's §2 patch
  applied), `.scratch/r05-iso3` (O03's §3 patch applied), `.scratch/r05-mut` (throwaway
  mutation probe). `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`; renderer sha256
  in every copy `34c85f57…` == in-tree before patching.
- No filed round runner was executed anywhere; no `--freeze` was run; no in-tree file was
  written by this seat. `git status --porcelain` = `?? reports/round-35/` throughout.
- Audited: `scout/K03-keyerror-path.md`, `op/O01-patch-draft.md`, `op/O03-isolated-verify.md`,
  `op/O05-verify.md`, `op/O08-validation-legs.md`, `op/O11-verify-2.md`,
  `scribe/S02-o-receipt.md` §2/§3/§6/§8. Not audited (outside claim O): the C/A/cross blocks.

## 2. Independent ground truth (pristine bytes) — the reference every verifier must match

| # | command (cwd = `.scratch/r05-iso`) | observed |
|---|---|---|
| R1 | `--profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json` | exit 1; **stdout 0 bytes**; stderr 945 bytes; `Traceback (most recent call last)`; frame `line 3822 … assembly.digests[rel]`; `KeyError: 'reports/round-20/handoff/claims-map.md'` |
| R2 | same, non-quiet | exit 1; stdout 0 bytes; stderr 941 bytes |
| R3 | `--profile v3 --quiet` (r7 default chain) | exit 0; `handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed packet_sha256=45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19` |
| R4 | `--profile v3 --selftest` | exit 0; header `… alias_leg=landed) plus 39 controls:`; `grep -c '^  - '` = 40 |
| R5 | `--selftest` (CLI default = v1) | exit 0; `… findings=0) plus 17 controls:`; 18 bullets |
| R6 | r6 baseline `inputs` vs live `V3_READ_SET` (module import) | baseline-only `{reports/round-20/handoff/claims-map.md}`; live-only `{reports/round-34/handoff/declared-in-r7/claims-map.md}`; both 58 members |
| R7 | `sha256sum reports/round-20/handoff/claims-map.md` | `4b1b9a35a18f0a4c937eec804d438852c672f13303b7dcd6ccde3a3d917caae8` == the digest the r6 baseline freezes for that path → **membership, not content** |
| R8 | 9 tracked freeze files: live sha256 vs `git show HEAD:<path>` | all SAME (r6 `expected.json` `ea1e2927…`, `packet.md` `6ced88ad…`; r7 `expected.json` `bbe15887…`, `packet.md` `45f57132…`, `twin.json` `0e229138…`, `freeze.txt` `3969954b…`, `claims-map.md` `d181de28…`) |
| R9 | `grep -o 'E2E-[A-Z]*' tools/exercise-handoff-e2e.py \| sort \| uniq -c` | COUNT 44, DIGEST 32, UNC 26, DATA 13, SCAN 11, LINK 10, BASELINE 10, GATE 8, ARTIFACT 6; `E2E-READSET` **0** |

K03 §1/§3/§4/§5, O08 §1 B1–B6, O03 §1, O05 §1, O11 §1 all reproduce these numbers exactly.
I also exercised O08's §6 regexes against the measured bytes: `SELFTEST_HEADER` matches and
captures `39`; `V3_SUMMARY` matches and its captured sha equals
`sha256sum reports/round-34/handoff/declared-in-r7/packet.md`; on the pre-patch r6 replay
the O1 leg fails as designed (`CRASH_RE` true, `E2E-READSET` token false, single-line
code+path false) — the leg is unsatisfiable pre-patch and satisfiable post-patch (§4).

## 3. The three isolated verifications: evidence quality, item by item

| item | O03 | O05 | O11 |
|---|---|---|---|
| E1 provenance (archive cmd + commit + copy-vs-live tool digest) | ✓ `git archive 4a7aede \| tar -x`; both digests `34c85f57…` (§1) | ✓ own archive; live == archive digest (§1) | ✓ own archive; also cross-checks `34c85f57…` == `repin.json` `surface_sha256_after` (§1) |
| E2 patch identity | ✓ diff `3d680b13…` / patched `1a003d67…` — **both re-derived by me** (§4) | ✓ diff `cae4b999…` / patched `2e126e4f…` / block `edd43861…` — *not re-measured by me* | ✓ applies O01's blocks: `84276189…` (block 0) and `16015c91…` (both) — `84276189…` re-derived by me |
| E3 raw capture, stream-labelled | ✓ verbatim outputs + per-log sha256s (§5, §8) | ✓ verbatim outputs; L1b/L1c/L2/N1–N5 | ✓ verbatim outputs, `--json` receipts, harness logs |
| E4 falsifiability (pre-patch column) | ✓ §1 traceback | ✓ §1 table | ✓ B1–B4 **plus a no-op-patch control** (10 passed / 8 failed) — the strongest instrument in the block |
| E5 forbidden-action proof | ✓ §6 (`git status` empty under the freeze dirs; "no `--freeze` was run anywhere") | ✓ §5 (explicit: only selftest-internal `v3_freezed_copy`) | ✓ §0, §8 (pins captured pre-patch) |
| E6 same-bytes bridge | n/a (draft) | owed (§Owed) | owed (§Owed: re-run harness on integrated bytes) |
| E7 count metrics named | ✓ 42 header / 43 bullets; pre-patch 39/40 | ✓ 41 / 42; pre-patch 39/40 | ✓ 40 / 41 on O01-alone; pre-patch 39/40; v1 17/18 |

All three satisfy E1–E5 and E7; E6 is owed by all three by construction (the patch is not
in-tree, §7). Two additional marks of quality worth naming because they are what makes the
evidence checkable rather than merely asserted: O03 §5b audits **another seat's** bytes
(O01's) and finds a defect there; O11 V-O11-5 discloses its own harness's first-revision
false negative and the byte-diff of the fix, and ships the harness as runnable bytes with a
digest (`3a33242b…`). An uncalibrated verifier harness is itself an unverified claim, and O11
is the only fragment that treats it that way.

## 4. Independent confirmations of the load-bearing claims

Each row is *my* measurement, not a restatement of theirs.

| claim | source | my measurement |
|---|---|---|
| O01's §2 fenced bytes are the bytes it verified | O01 §2/§3 | block extracts to 3937 B / 67 lines, sha256 `ebc6e1cc…` == claimed; `git apply -p1` clean; patched file `84276189…` == claimed; compiles |
| O03's §3 fenced bytes are the bytes it verified | O03 §3 | block extracts to 9858 B / 150 lines, sha256 `3d680b13…` == claimed; `patch -p1` clean; patched file `1a003d67…` == claimed |
| **O01-alone leaves the `--quiet` diagnostic invisible** | O03 §5b, O11-P1 | confirmed: on `.scratch/r05-iso2`, the r6 replay under `--quiet` prints only `handoff-v3: exit=1 fields=? … v2_subset=unequal … packet_sha256=(not assembled)` (no token); the non-quiet form prints `FAIL read-set-roster: …` + `handoff-v3: E2E-READSET: 1 read-set member(s) named by the frozen baseline are not in the live read set: reports/round-20/handoff/claims-map.md — the baseline row is superseded (re-point or re-freeze it)` |
| O01-alone's control count is below the O08 floor | O03 §5b | confirmed: `--profile v3 --selftest` → exit 0, `plus 40 controls:` (N=40 < 41), 41 bullets, m12c present, m12a/m12b preserved |
| O01-alone's `--json` receipt carries the code | F-R05-4 (mine, was `to-verify`) | **closed**: `--json` r6 replay → `exit=1`, `code=E2E-READSET`, checks `read-set-roster=False`, `verdict=False` |
| O03's mixed-case "nothing hidden" | O03 §5 m12e | confirmed on O03's own patched bytes: a baseline with one unresolvable member + one resolvable drift prints `FAIL input-digest: reports/round-18/d4/replay.md: frozen 832eeeb9a93a… live acad1b5423b9…` **and then** `handoff-v3: E2E-READSET: 1 baseline read-set member(s) are not in this revision's read set: reports/round-20/handoff/claims-map.md …`, exit 1 |
| the patch does not close the reverse direction | S02-F1 / S02 §8.4 | confirmed on O01's patched bytes: a 57-member baseline (r7 minus the claims-map row, re-signed) against 58 live → **exit 0** and `OK   input-digest: 58 read-set digests match the frozen baseline` (57 compared); identical on pristine bytes |
| `v2_subset=unequal` on an aborted run | H7 (mine) | confirmed: emitted by the r6 replay on O01's patch, and by the mutation probe (§5 H6) — it means "no subset record was produced", not "the subset check failed" |

O05's candidate patch is the one artefact in the block I did not re-measure: its evidence is
internally consistent (pre/post `FAIL`-line diff empty for the pre-existing v1 red, N1's
wrong-branch attempt disclosed and corrected) and its numbers are checkable by the same
commands, but no second seat has reproduced `2e126e4f…`. O03 and O11 both measured O01's
bytes instead. This is not a defect; it is the one evidence item left without a second
archive.

## 5. Hazards found (they apply to the validator as much as to the verifiers)

**H1 — `/tmp` capture can silently destroy evidence.** During the wave,
`printf '%01000d' 0 > /tmp/e1.out` failed with `write error: Disk quota exceeded` (0 bytes)
while the same write into the repo succeeded; a Python process whose stderr flush fails at
shutdown exits **120** with empty output. The identical r6 replay gave exit 1 + a 945-byte
traceback with no redirection, and **exit 120, stdout 0 bytes, stderr 0 lines** redirected to
`/tmp` (control: a 50-frame traceback → exit 120 / 0 bytes redirected, 484 bytes piped; a
4-line traceback redirected → exit 1). The condition is transient/load-dependent — 200–500 B
writes to `/tmp` succeeded minutes later — so it can hit one seat and not the next. Any O
evidence showing `exit 120` or an empty capture must be re-run with `TMPDIR=$PWD/.scratch` and
the capture in-repo or through a pipe. (Probe files `/tmp/r05_*` are ephemeral, outside the
repo, not round evidence.)

**H2 — `git rev-parse HEAD` inside an archive copy is not provenance.** An archive copy has
no `.git`, so git walks up to the enclosing repo: `git rev-parse HEAD` in `.scratch/r05-iso`
printed `4a7aede…` — the lane repo's HEAD, not the copy's. Provenance is the `git archive
<sha>` command itself (O11 §1 runs `rev-parse` in the lane tree, which is the correct use).

**H3 — the `--quiet` path prints nothing on the crash path** (R1/R2: stdout 0 bytes) **and a
degenerate summary on the caught path** (P2). The name surfaces only on the non-quiet path
(`tools/exercise-handoff-e2e.py:4603-4604`) and in `--json`.

**H4 — exit 1 does not discriminate.** CPython's uncaught-exception status is 1 and so is
`EXIT_FAIL` (`:112-114`); the pristine r6 replay already exits 1. O11's no-op-patch control
demonstrates this as a leg-design property (its "exit non-zero" assertion PASSes on a patch
that fixes nothing while the traceback assertion FAILs).

**H5 — header/bullet off-by-one.** The header prints `len(results) - 1` (`:4464`) while every
element of `results` is printed (`:4466-4467`): 39/40 pristine, 40/41 on O01-alone, 42/43 on
O03, 41/42 on O05, 17/18 for the v1 suite. Assert the bullet count and name which number is
meant.

**H6 — a red witness leg is misreported as a claim-D failure.** `V3Assembly` keys
`alias_state` on two `--selftest` witnesses (`:3543-3560`). Demonstrated deterministically in
`.scratch/r05-mut` (stub `tools/assemble-d4-typed.py` exiting 1 only for `--selftest`): the
renderer dies with `Failed: the D4-CL08 landed form is not backed by this run: the alias
witnesses are red (tools/d2-typed-labels.py --selftest exit 0; tools/assemble-d4-typed.py
--selftest exit 1)`, and the r7 default chain fails with the degenerate summary. I observed
exactly that message once on the **unmutated** pristine copy with `TMPDIR` unset (→ `/tmp`),
failing in 0.94 s while `/tmp` was quota-pressured; minutes later the same legs pass
standalone with `TMPDIR` unset (163/163 and 12/12) and the r7 chain exits 0. The
*misattribution mechanism* is proven; the cause of that one instance (EDQUOT inside a witness
leg) is **to-verify** — I did not capture the leg's own error. Rule: if the selftest or a
chain reports "the alias witnesses are red", re-run with a repo-local `TMPDIR` before filing
a patch defect.

**H7 — `v2_subset=unequal` on an aborted run** (CLI `subset = "equal" if any(ok) else
"unequal"`, `:4592`): it must never be read as a real subset mismatch.

## 6. Findings filed

- **F-R05-1 (integration hazard, high — owner: integrator).** The two control sets encode
  **opposite** mixed-case semantics and cannot be mixed. O03's `m12e` asserts the resolvable
  drift row is still recorded (`assert any("reports/round-18/d4/replay.md" in row["detail"]
  and not row["ok"] for row in records)`) — confirmed by my §4 run. O05's mixed control
  asserts the opposite (`assert superseded_rel in verdict and "drift not evaluated" in
  verdict`, `assert D4_BRIEF not in verdict`), which holds only for a guard that raises
  *before* the drift loop. Landing one patch with the other's control lines fails the
  selftest; a control asserting the wrong semantic would be worse than none. The integrator
  must land exactly one patch **plus its own** control set and state in the round record
  which mixed-case semantic is landed.
- **F-R05-2 (claim-text defect, medium — owner: integrator/scribe).** The declared counting
  command (`claims.json:47`, bare `--selftest`) runs the **v1** matrix — measured 17 controls
  / 18 bullets (R5) — which cannot see the new v3 controls (39/40 pre-patch, R4). O11's
  V-O11-1 is correct and is confirmed here. The acceptance must be
  `python3 -B tools/exercise-handoff-e2e.py --profile v3 --selftest` with N ≥ 41; the round
  record should note the corrected command rather than editing `claims.json` in place.
- **F-R05-3 (validator spec — owner: integrator, S04).** `run-validation.py`'s claim-O group
  must: (a) export a repo-local `TMPDIR` before spawning the renderer (H1/H6); (b) assert the
  bullet count, accept exit ∈ {1,2}, and require the `E2E-READSET` token **and** the member
  path on one line with no `Traceback`/`KeyError`; (c) never capture to `/tmp`; (d) require
  the **new** control, not merely "an `E2E-DIGEST` control line exists" — `m12b` exists
  pre-patch, so that anchor passes on the unfixed tree (confirmed: R4 lists m12a/m12b
  pre-patch); (e) carry O08's static legs O5/O6. S02 §8.5's correction of S04's
  `{"id": "O1", … --selftest … >= 19 (was 17)}` leg is confirmed by R5.
- **F-R05-4 (deviation bookkeeping — owner: integrator).** If O01 §2 lands **without** the
  `if err:` hoist, the claim's own declared command cannot show the name (confirmed on the
  patched bytes, §4) and O08 leg O1 fails on its own command shape. Either land the hoist
  (O02 §2.5, O03 §3, O05 §2 all carry it) or file the deviation with the non-quiet/`--json`
  form as the evidence command.
- **F-R05-5 (closed `to-verify`).** The patched renderer exposes `E2E-READSET` as the `code`
  field of the `--json` receipt (measured on O01's bytes: `exit=1`, `code=E2E-READSET`).
- **F-R05-6 (routed follow-up — owner to be named).** The reverse-direction over-claim
  (S02-F1 / §8.4) is **not** closed by any candidate patch: O03's and O05's guards both test
  only `rel not in assembly.digests` (baseline member missing live), and my run on O01's bytes
  shows exit 0 with the false count `OK   input-digest: 58 read-set digests match the frozen
  baseline` for a 57-member baseline. No receipt may describe the roster leg as
  bidirectional; if it is not fixed, file it routed with an owner.

## 7. Verdicts on the audited surfaces

| surface | verdict | basis |
|---|---|---|
| `scout/K03-keyerror-path.md` | green | every number reproduced (R1–R9) |
| `op/O01-patch-draft.md` | green (bytes + behaviour) | §4 rows 1–4; the `--quiet` gap is F-R05-4, and O01 named that trade itself (`O01:40-45`) |
| `op/O03-isolated-verify.md` | green | E1–E5, E7 ✓; §3 bytes re-derived; §5b defect independently confirmed |
| `op/O05-verify.md` | green on evidence quality; patch not re-measured by this seat | E1–E5, E7 ✓; internally consistent; one archive short of a second reproduction |
| `op/O08-validation-legs.md` | green on B1–B6; legs exercised | §2/§4; gaps filed as F-R05-2/F-R05-3 |
| `op/O11-verify-2.md` | green — best evidence discipline in the block | E1–E5, E7 ✓; calibrated no-op control; self-defect disclosed (V-O11-5) |
| `scribe/S02-o-receipt.md` §2/§3/§6 | green | S02-F1 reproduced on pristine and patched bytes; the v1/v3 suite split confirmed (R4/R5) |
| claim O's independent verification | **established, subject to F-R05-1..F-R05-4 before admission** | three independent archives (O03, O05, O11), two of them measuring the same landed candidate (O01's) |

No axis verdict is claimed here; that is the integrator's, on the delivered revision. At my
close the in-tree renderer is still `34c85f57…` (R8/R9; `git status --porcelain` =
`?? reports/round-35/`), so every post-patch number in this fragment is measured on a scratch
copy, and E6 (same-bytes bridge) remains owed by the whole block.

## Owed

- `reports/round-35/run-validation.py` — absent; F-R05-3 is the binding constraint on its
  claim-O group.
- Integrator decision on **F-R05-1** (one patch + its own control set; state the mixed-case
  semantic landed) and on **F-R05-4** (hoist the `--quiet` diagnostic, or file the
  deviation).
- Owner for **F-R05-6** (reverse-direction over-claim).
- **E6** for the whole block: after the in-tree apply, re-measure the patched renderer's
  sha256 and re-run the legs on the landed bytes; the scratch digests (`84276189…`,
  `1a003d67…`, `2e126e4f…`) are per-candidate, not interchangeable.
- `op/O05-verify.md`'s patch bytes (`2e126e4f…`) have no second-archive reproduction; if the
  integrator lands O05's wording instead of O01's/O03's, legs L1–L3 must be re-measured on
  the landed bytes.

## Citations

Files (at `4a7aede` unless noted):

- `reports/round-35/targets.json:352-355` (seat R05 mission/out), `:184-188`/`:198-202`/`:212-216`/`:443-447` (O01/O03/O05/O11 missions and outs)
- `reports/round-35/claims.json:38-52` (claim O: `:45` after_required, `:46-50` counting commands incl. `:47` bare `--selftest` and `:48` `--quiet` "expect: exit 1, named diagnostic", `:51` thresholds), `:67-73` (non-goals)
- `tools/exercise-handoff-e2e.py:112-114` (`EXIT_*`), `:89-93` (exit-code table), `:184` (`CLAIMS_MAP`), `:244-268` (exception taxonomy), `:3543-3560` (d4 legs / alias witnesses), `:3816-3824` (drift leg; defect `:3822`), `:4464-4467` (selftest header vs bullets), `:4592` (`v2_subset` computation), `:4603-4604` (quiet-gated verdict print), `:4154` (`v3_selftest`), `:1635` (`v1_selftest`), `:1435-1441` (v1 twin)
- `reports/round-35/scout/K03-keyerror-path.md`, `op/O01-patch-draft.md`, `op/O03-isolated-verify.md`, `op/O05-verify.md`, `op/O08-validation-legs.md`, `op/O11-verify-2.md`, `scribe/S02-o-receipt.md`, `review/R04-o-review.md:63-112,136-165`
- `reports/round-34/handoff/repin.json:19-22,50`, `reports/round-34/handoff/declared-in-r7/{expected.json,packet.md,twin.json,freeze.txt,claims-map.md}`, `reports/round-30/handoff/declared-in-r6/{expected.json,packet.md,twin.json}`, `reports/round-20/handoff/claims-map.md`, `.gitignore:3`

Commands (all from the lane root, `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`; scratch
copies under `.scratch/r05-*`):

- `git archive 4a7aede | tar -x -C .scratch/r05-iso` (2815 files); `sha256sum tools/exercise-handoff-e2e.py` both copies → `34c85f57…`
- `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet --baseline reports/round-30/handoff/declared-in-r6/expected.json` → exit 1, stdout 0 bytes, 945-byte traceback, `KeyError` at `:3822`
- same non-quiet → exit 1, stdout 0 bytes, stderr 941 bytes; stdout-only via pipe → 0 bytes, stderr-only → 945 bytes starting `Traceback (most recent call last):`
- `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` → exit 0, `packet_sha256=45f57132…`; `--profile v3 --selftest` → 39 controls / 40 bullets; `--selftest` → 17 / 18
- module import set-diff (r6 vs r7 vs live `V3_READ_SET`); `sha256sum reports/round-20/handoff/claims-map.md` → `4b1b9a35…`; per-file live vs `git show HEAD:` for 9 freeze files → all SAME; `grep -o 'E2E-[A-Z]*' … | sort | uniq -c` → census R9
- extraction + `git apply -p1` of `op/O01-patch-draft.md` block 1 → `ebc6e1cc…`, patched `84276189…`; runs: selftest 40/41 + m12c, r6 `--quiet` (no token), r6 non-quiet (`FAIL read-set-roster` + `handoff-v3: E2E-READSET: …`), r7 exit 0, `--json` `code=E2E-READSET`, reverse-direction scratch baseline → exit 0 + `OK   input-digest: 58 read-set digests match the frozen baseline`
- extraction + `patch -p1` of `op/O03-isolated-verify.md` block → `3d680b13…`, patched `1a003d67…`; r6 non-quiet → `E2E-READSET` line, exit 1; mixed case (unresolvable + resolvable-drifted, re-signed) → `FAIL input-digest: reports/round-18/d4/replay.md: frozen 832eeeb9a93a… live acad1b5423b9…` + `E2E-READSET` verdict
- mutation probe `.scratch/r05-mut` (stub `tools/assemble-d4-typed.py`, exits 1 only for `--selftest`) → `Failed: the D4-CL08 landed form is not backed by this run: the alias witnesses are red (…)`, and the r7 chain exit 1 with `v2_subset=unequal`
- `/tmp` quota probes: `printf '%01000d' 0 > /tmp/e1.out` → `write error: Disk quota exceeded`; 50-frame traceback redirected → exit 120 / 0 bytes, piped → 484 bytes; `git rev-parse HEAD` in `.scratch/r05-iso` → `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4`
