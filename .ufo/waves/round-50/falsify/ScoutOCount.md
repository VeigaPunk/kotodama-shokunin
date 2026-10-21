# ScoutOCount — Claim O, independent counting reproduction (round 50 / falsify)

- Seat: KotodamaR50-2.ScoutOCount-21 (leaf; no delegation, no background jobs).
- Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. Landed `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0`, base `4ad26836552462d28a946ca3b067cab0b5ce3532`.
- Attacked item: claim **O** (operability) counting command + gate semantics, per the ticket: rerun the landed `jj-colocation-probe.py` against both tool trees and compare with `reports/round-50/validation.json` `claims.O`.
- Date: 2026-10-21. Read-only; all runs in a private `/tmp` extraction. Advice to the author lane, not an admission.

## Verdict: **HOLDS**

The landed probe reproduces the receipt's `claims.O` numbers exactly, exits 0 on both trees, and the two gate properties named in the claim (multi-ref probe with remote-only `landed_sha`; unresolvable-pin fail-closed with `GIT_*` scrubbed) are present in the landed bytes and independently exercised. Two measurement/provenance boundaries are recorded below (F1–F2); neither changes the count on this artifact.

## Reproduction (exact)

```
D=$(mktemp -d /tmp/kotodama-scout-ocount-XXXX)
git -C LANE archive 4ad2683 tools | tar -x -C "$D/base-tools"          # keeps tools/ prefix
git -C LANE archive 1c779e4  tools | tar -x -C "$D/landed-tools"
git -C LANE show 1c779e4:reports/round-50/jj-colocation-probe.py > "$D/probe-landed.py"
# probe sha256 d3fff001f8fd08133ad20b83133ca743af4d3bc792710e351c263fd7212aafa5
# = header of reports/round-50/telemetry/jj-probe-v2.txt; working-tree probe is byte-identical (diff empty)
export GIT_CEILING_DIRECTORIES=/tmp
python3 probe-landed.py --tools-root "$D/base-tools"   --history-repo LANE   # rc=0
python3 probe-landed.py --tools-root "$D/landed-tools" --history-repo LANE   # rc=0
```

Output tails (second landed run identical, so the counts are stable across random fixture shas):

| tree | JJ_COLOCATION_FALSE_NEGATIVES | JJ_COLOCATION_FALSE_POSITIVES | exit |
|---|---|---|---|
| base `4ad2683` tools | `3/3` | `0/4` | 0 |
| landed `1c779e4` tools | `0/3` | `0/4` | 0 |

Per-case exits (landed): R1 `3`, R2 `3`, R3 `2`, P1/P2/P3/P4 `0`.
Per-case exits (base):   R1 `3`, R2 `0`, R3 `0`, P1/P2/P3/P4 `0`.

Landed evidence samples:
- R1: `receipt_guard: refusing overwrite ... committed_sha=eaf918d9... landed_ref=refs/remotes/origin/main landed_sha=490510f2...` (distinct shas, landed from the remote ref).
- R2: `... committed_blob=none landed_ref=refs/remotes/origin/main landed_sha=42add8c7...` exit 3 (refuses the below-tip overwrite).
- R3: readme selftest exit 2 with `BASE_COMMIT c42d675...` absent (fail closed), vs base exit 0 + `SKIP ... (base object unreachable)`.

## Comparison with `reports/round-50/validation.json` `claims.O`

| field | receipt | measured | match |
|---|---|---|---|
| `before.probe_false_negatives` | 3 | 3 | yes |
| `before.probe_false_positives` | 0 | 0 | yes |
| `after.probe_false_negatives` | 0 | 0 | yes |
| `after.probe_false_positives` | 0 | 0 | yes |
| `before.guard_remote_ref_lines` | 0 | `grep -c refs/remotes/origin` = 0 | yes |
| `after.guard_remote_ref_lines` | 24 | 24 | yes |
| `before.readme_skip_marker_lines` | 1 | 1 | yes |
| `after.readme_skip_marker_lines` | 0 | 0 | yes |
| `after.receipt_guard_selftest_rc` | 0 | 0 (69/69 controls) in a landed worktree | yes |
| `after.readme_revisions_selftest_rc` | 0 | 0 (15/15 PASS) in a landed worktree | yes |

## Gate semantics re-verified in landed bytes

- `tools/harness/receipt_guard.py:96-127` enumerates `for-each-ref ... refs/heads refs/remotes`; non-commit/symbolic/warning paths fail closed. `:207` selects `landed` only from `refs/remotes/`; `:215-218` refuses unless `REFRESH_RECEIPTS=1`. `_git` at `:56-59` drops every `GIT_*` key.
- Independent adversarial plain-git states against the landed guard (not the tool's selftest):
  - receipt only on `refs/heads/topic`, no remote holds it → exit 3, `landed_ref=none`, `hit_refs=refs/heads/topic` (detects local branch, does not mislabel it landed).
  - receipt only on `refs/remotes/upstream/main` → exit 3, `landed_ref=refs/remotes/upstream/main`, `landed_sha` distinct from `committed_sha`.
  - `refs/remotes/origin/dev` (no receipt) beside `refs/remotes/origin/main` (receipt) with HEAD above tip → `landed_ref=refs/remotes/origin/main` (first remote holder), exit 3.
  - normal state HEAD==origin/main, receipt absent → exit 0.
- `tools/check-readme-revisions.py:80` pin; `:236-248` `GIT_*` scrub (`GIT_NO_REPLACE_OBJECTS=1`); `:279/:295` unreachable pin is `ERROR` (exit 2, never SKIP); controls at `:465,:474,:480,:491` cover unreachable pin, git-free tree, shallow clone, and a foreign `GIT_DIR`. Observed in a landed worktree: all pass, rc 0. In a pinless bare tree the pinned-base control becomes ERROR and the selftest exits 2 — the intended fail-closed behavior.
- Selftest control retention: guard base 45/45 → landed 69/69, **every** base control name still present, 24 new `r50-*` controls. Gate base 11 control labels all present in the landed pin-reachable run (15 PASS), 4 new fail-closed controls.

## Boundary findings (not count failures)

**F1 — probe R1 does not assert the refusal, only the disclosure (medium, measurement).**
`reports/round-50/jj-colocation-probe.py:227-261`: `case_r1` computes `flagged = bool(stray) or not landed` (`:252`) and never inspects `result.returncode`, although the JjAudit R1 oracle (`.ufo/waves/round-50/build/ReviewProbeDesign.md:26`) required “guard exit 3”. Mutation evidence: a guard that emits a correct `landed_sha=origin/main` but **permits** the R1-state overwrite (exit 0, no `REFRESH_RECEIPTS`) scores `0/3`; a guard that mislabels local HEAD as landed scores `1/3` (caught). So the probe catches R1's original label defect but would not catch a future exit-code regression in that state. Smallest fix: `flagged = bool(stray) or not landed or result.returncode == 0` in `case_r1` (R1 always has a committed receipt and the probe strips `REFRESH_RECEIPTS`, so exit 0 is never legitimate there), then refresh both telemetry files.

**F2 — receipt provenance is weaker than “landed bytes” (low, evidence).**
`reports/round-50/validation.json` is **untracked** at `1c779e4` (`git ls-tree` absence; `git status` `?? reports/round-50/validation.json`), mtime 13:32:51 vs commit 13:03:10. Its `argv` names `/tmp/kr50-landed`/`/tmp/kr50-base`, which no longer exist, and the working-tree `reports/round-50/run-validation.py` differs from landed (`git diff`: the C topic-owner regex gains `\b`; O path unchanged). O's numbers still reproduce from the landed probe on freshly extracted trees, so the claim survives; the receipt itself is not reproducible from the commit alone.

**F3 — acceptance command needs a git worktree (informational).**
`probe --tools-root <bare archive tree>` exits 2 (`setup error: ... pinned base ... absent`) because the default history repo is “the work tree containing --tools-root”; the claim's `after_required` command omits `--history-repo`. Documented in the probe docstring (`:38-40`), but reviewers extracting with `git archive` must pass `--history-repo LANE` (as this run did).

## Unknowns / not exercised

- jj 0.45.1 was not invoked here; this is the plain-git leg only (the v2 telemetry does not claim jj parity; the R1/R2 state shapes match the audit's jj run).
- v1 probe bytes are not retained in the repo: `276eff71...` appears only in `reports/round-50/telemetry/jj-probe-v1.txt`'s header. The v1 output is landed and shows the pre-amendment `1/3` on the landed guard, so the amendment is recorded, but the v1 script itself cannot be re-run from landed bytes.
- C and Ca claims were out of scope for this seat.

## Environment

`python3 3.14.8`, `git 2.56.0`, plain-git fixtures under `mkdtemp` with `GIT_CEILING_DIRECTORIES=/tmp`. No installs, no lane writes, no jj commands; temp extraction and clone removed after the run.
