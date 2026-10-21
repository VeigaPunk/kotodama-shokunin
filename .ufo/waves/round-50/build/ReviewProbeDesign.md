# ReviewProbeDesign: Claim O, plain-git reproduction of JjAuditKotodama R1-R3 on base tool bytes

- Seat: ChousaR27R2.ReviewProbeDesign-4 (leaf; no delegation, no background jobs).
- Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. Base: `4ad26836552462d28a946ca3b067cab0b5ce3532`.
- Date: 2026-10-21. Advice to the author lane, not an admission.
- Judged on: coverage (3 of 3 defects, state controls, jj parity), operability (one script, about 3 s, re-runnable), calibration (each verdict has a state-only control; limits listed).

## Verdict

| defect | reproduces on base bytes (plain git 2.56.0) | jj 0.45.1 parity | calibrated severity |
|---|---|---|---|
| R1: guard cites unlanded local HEAD as `committed_sha` | **REPRODUCED.** Exit 3; `committed_sha` is a detached empty commit one ahead of `origin/main`, and `origin/main` is its ancestor, not the reverse. | **REPRODUCED.** Same exit and same identity. | Label-level in this state. The refusal is correct (tree equals `origin/main`'s tree); the printed sha is not landed evidence. |
| R2: HEAD-only receipt probe misses a landed receipt | **REPRODUCED.** Exit 0 while the receipt blob is on `origin/main` and `refs/heads/main`. | **REPRODUCED.** Exit 0. | High: the guard permits a write over a landed receipt. The write itself was not executed. |
| R3: pinned-base control SKIPs when the object is missing | **REPRODUCED.** Selftest exit 0, `SKIP control: base c42d675 ... (base object unreachable)`, `selftest skips: 1`. | Not run. The trigger is object absence, not jj. | Medium: silent pass. `claims-freshness` on the same pin fails closed (exit 2). |

Counting oracle on base bytes: **3 of 3 reproduce**. Each verdict flips under its state-only control.

## Design

1. **Base bytes.** `git -C LANE archive 4ad2683 tools` extracted to `/tmp`. Blob ids equal `git -C LANE rev-parse 4ad2683:<path>`: `receipt_guard.py` `4610b23b...`, `check-readme-revisions.py` `b897204e...`, `claims-freshness.py` `25246717...`.
2. **Sandboxes.** Each is `git init -b main` with a bare `origin`, and base `tools/` committed and pushed. Only plain git builds the states:
   - **R1** (jj `@-` = empty unpushed commit above `origin/main`): receipt A pushed, then `git checkout -q --detach && git commit -q --allow-empty`. `refs/heads/main` = `origin/main` = A.
   - **R2** (jj `new <older>`): C1 (no receipt), C2 (receipt, pushed), then `git checkout -q --detach C1`.
   - **R3** (pin object absent): a sandbox with no `c42d675` object. Control: a temp clone of the lane, where the object exists.
3. **Oracles.**
   - R1: guard exit 3, `committed_sha` = HEAD, and `git merge-base --is-ancestor HEAD origin/main` rc 1.
   - R2: guard exit 0, `git cat-file -e origin/main:<path>` rc 0, and `git ls-tree HEAD -- <path>` empty.
   - R3: selftest exit 0, SKIP line present, and `git cat-file -e c42d675...^{commit}` rc non-zero.
4. **State-only controls.**
   - R1c: HEAD = `origin/main`. Identity becomes landed (ancestor rc 0).
   - R2c: HEAD = `origin/main`. Exit becomes 3.
   - R3c: object present. Control becomes PASS with `selftest skips: 0`.
5. **jj parity.** Real `jj 0.45.1`: `jj git init --colocate` then `jj new` (R1), and `jj new <C1>` (R2), in `/tmp` sandboxes only.

Full scripts: Appendix A (plain git, `/tmp/r50-o/repro-plain.sh`) and Appendix B (jj parity, `/tmp/r50-o/jj-parity.sh`). Both write only under `/tmp`.

## Results: exact commands and exits

### R1 (`L` = `/tmp/r50-o/repro-plain/r1/lane`)

| # | exact command | exit | observed |
|---|---|---|---|
| 1 | `git -C $L rev-parse HEAD` | 0 | `96278f5e...` (X, unpushed) |
| 2 | `git -C $L rev-parse origin/main` | 0 | `f39236b2...` (A) |
| 3 | `git -C $L symbolic-ref -q HEAD` | 1 | detached |
| 4 | `git -C $L rev-parse 'HEAD^{tree}' 'origin/main^{tree}'` | 0 | both `c5f11c25...` |
| 5 | `git -C $L merge-base --is-ancestor HEAD origin/main` | 1 | X is not landed |
| 6 | `git -C $L rev-list --count origin/main..HEAD` (checked after the run) | 0 | `1`; `origin/main` is an ancestor of HEAD (rc 0) |
| 7 | `python3 $L/tools/harness/receipt_guard.py --repo-root $L reports/round-49/validation.json` | 3 | `committed_sha=96278f5e... committed_blob=203e7040... [RECEIPT-GUARD-COMMITTED]` |
| 8 | `env REFRESH_RECEIPTS=1 python3 ...same guard command...` | 0 | `committed_sha=96278f5e... [RECEIPT-GUARD-REFRESH]` (the permit also cites X) |
| C | `r1-tip` (HEAD = `origin/main`), same guard | 3 | `committed_sha=f39236b2...` = `origin/main`; ancestor rc 0 |

### R2 (`L` = `/tmp/r50-o/repro-plain/r2/lane`; C1 `1893d643...`, C2 `746d0cb9...`)

| # | exact command | exit | observed |
|---|---|---|---|
| 1 | `git -C $L rev-parse HEAD` | 0 | `1893d643...` (C1) |
| 2 | `git -C $L rev-parse origin/main` | 0 | `746d0cb9...` (C2) |
| 3 | `git -C $L cat-file -e origin/main:reports/validation.json` | 0 | blob present on `origin/main` |
| 4 | `git -C $L cat-file -e refs/heads/main:reports/validation.json` | 0 | blob present on local `main` |
| 5 | `git -C $L ls-tree -r --name-only HEAD -- reports/validation.json` | 0 | empty: the HEAD probe sees nothing |
| 6 | `python3 $L/tools/harness/receipt_guard.py --repo-root $L reports/validation.json` | 0 | no output: **allowed** (false negative) |
| C | `r2-tip` (HEAD = `origin/main`), same guard | 3 | `committed_sha=c850ba60... committed_blob=203e7040... [RECEIPT-GUARD-COMMITTED]` |

### R3 (`L` = `/tmp/r50-o/repro-plain/r3/lane`)

| # | exact command | exit | observed |
|---|---|---|---|
| 1 | `git -C $L cat-file -e c42d675be96b6b3957e6e5c00ab192080cb70083^{commit}` | 128 | `fatal: Not a valid object name` |
| 2 | `python3 $L/tools/check-readme-revisions.py --selftest` | 0 | `SKIP control: base c42d675 README flagged (r49 defect) (base object unreachable)`; `selftest skips: 1`; `selftest: all checks passed`; the other 10 controls PASS |
| C | temp clone of the lane (object present), same tool bytes, `--selftest` | 0 | `PASS control: base c42d675 README flagged (r49 defect)` with REVISION-DUP at lines [55, 57] and REVISION-STUB at line 55; `selftest skips: 0` |
| X | `python3 $L/tools/harness/claims-freshness.py --claims <pin.json> --root $L` (pin absent) | 2 | `REFUSE: input is malformed at c42d675...: baseline_commit ... does not resolve ...; exit 2 -- no freshness verdict is possible` |

### jj 0.45.1 parity (`/tmp/r50-o/jj-parity/`)

| # | exact command | exit | observed |
|---|---|---|---|
| jR1 | `jj git init --colocate`, then `jj new` | 0, 0 | `Parent commit (@-): mlsnxlnm c31935cf (empty)`. HEAD = `c31935cf...`; `origin/main` = `9bd8c221...`; `symbolic-ref` rc 1; ancestor rc 1; `rev-list --count` 1 with `origin/main` an ancestor. Guard exit 3, `committed_sha=c31935cf...`. |
| jR2 | `jj new 3c3ab7c5...` (C1 = `base tools`) | 0 | `Removed 1 files`. HEAD = `3c3ab7c5...`; `origin/main:reports/round-49/validation.json` present (cat-file rc 0). Guard exit 0. |

The jj states match the plain-git states: detached HEAD on an empty unpushed commit one ahead of `origin/main` (R1), and HEAD at a pre-receipt commit below the tip (R2). The exits match too.

## Calibration observations

- **Existing controls do not cover the defects.** Base `receipt_guard.py --selftest`, run in the R2 sandbox, passes **45/45** with exit 0. None of its controls exercises an anchored-below-tip or remote-ref state, so its green is not evidence for R1 or R2.
- **The R3 wording hides the skip.** Base `check-readme-revisions.py --selftest` exits 0 and prints `selftest: all checks passed` with `selftest skips: 1`. The one skipped control is the only one that guards the real r49 defect.
- **Audit line refs verified at base bytes.**
  - `receipt_guard.py`: `:54` dispatcher, `:69` `rev-parse HEAD^{commit}`, `:73` `symbolic-ref`, `:76` `show-ref`, `:92` `--show-toplevel`, `:129` `ls-tree HEAD`, and fixture-only `:216`, `:247`, `:252`, `:260`, `:299`.
  - `check-readme-revisions.py`: `:67` `BASE_COMMIT`, `:233` `skip()`, `:306` `git show`.
  - `skip()` appends to `skips` and does not touch `ok` (`:233-235`). The selftest returns `ok` (`:344-345`).
- **R3 skip branch is broader than the audit states.** `:310` skips on any non-zero `git show`. "Object absent" and "pin present, `corpus/README.md` absent at that commit" both SKIP. [INFERENCE from reading `:306-311`; not run.]
- **Severity calibration.** R1's exit stays correct here, so the harm is a provenance label. This holds unless a downstream consumer treats `committed_sha` as landed evidence. [INFERENCE: downstream use was not inspected beyond the audit's description.] R2 is the high-severity defect. R3 is medium.

## Lane state (read-only, observed now)

- `.jj` is **present**, so the lane is colocated. The audit recorded it absent.
- HEAD is attached to `refs/heads/main` = `4ad2683` = `refs/remotes/origin/main`. R1 is therefore not live at this instant: it needs a jj mutation that detaches HEAD. R2 is live-capable (`jj new <older>`).
- Pin object `c42d675` is present (`cat-file -t` returns `commit`). R3 needs the object to disappear.

## Notes for the O executors (advice)

- **Oracle for the fixed probe.**
  - R1: the sha the guard cites must be reachable from `origin/main`, or the guard must report the landed sha separately from HEAD. The state is the R1 anchored sandbox.
  - R2: the guard must exit 3 in the anchored state, with the path matched on `refs/heads/main` or `refs/remotes/origin/main`.
  - R3: the guard must exit non-zero with the pin absent and 0 with the pin present.
- **Keep the fixes separable in controls.** An R1-only fix still exits 0 on R2. An R2-only fix still cites HEAD.
- **Add plain-git controls** (no jj needed): `git checkout --detach` below the tip; `git commit --allow-empty` on detached HEAD; absent pin object.
- **R1 oracle is a base-defect predicate, not a fix oracle.** Appendix A's R1 verdict checks that `committed_sha` equals an unlanded HEAD. A fixed guard that prints `committed_sha=<HEAD>` alongside a landed field would still match. The fix oracle must test ancestry of the reported landed field against `origin/main`.

## Unrun checks and limits

- **Not run:** the fixed tools, and `reports/round-50/jj-colocation-probe.py`, which does not exist at base and is outside this seat.
- **Not run:** landed-tools evaluation. To run the same states against landed tools, change `$BASE_SHA` in Appendix A to the landed commit (it feeds `git archive`, the `rev-parse` display, the sandbox commit message, and the R3 clone checkout). States and oracles are unchanged.
- **Not run:** R3 under jj `gc`. Object survival under jj is the audit's observation, not re-run here.
- **Not run:** pin present with the README absent (see the R3 skip-branch note).
- **Lane untouched:** `lane HEAD` before and after the scripts is `4ad2683`. No `git status`, no jj command, no write in the lane. Lane reads were limited to `archive`, `rev-parse`, `cat-file`, `symbolic-ref`, `for-each-ref`, and `clone --no-hardlinks` used as a source.
- **Tooling:** no installs or upgrades. Pre-existing tools used: git 2.56.0, python 3.14.8, `jj 0.45.1` at `/home/vgpnk/.local/bin/jj`. jj ran only inside `/tmp` sandboxes.

## Appendix A: plain-git reproduction (`/tmp/r50-o/repro-plain.sh`)

```bash
#!/usr/bin/env bash
# JjAuditKotodama R1-R3 on base tool bytes (git -C LANE archive 4ad2683 tools), plain git only.
# The lane is read-only here: archive, rev-parse, and clone-as-source. All writes stay under $W.
set -u
LANE=/home/vgpnk/Projects/shokunin/kotodama-shokunin
BASE_SHA=4ad26836552462d28a946ca3b067cab0b5ce3532
PIN_SHA=c42d675be96b6b3957e6e5c00ab192080cb70083
W=/tmp/r50-o/repro-plain
for v in $(compgen -e | grep '^GIT_'); do unset "$v"; done
rm -rf "$W" && mkdir -p "$W/base" || exit 2
exec > >(tee "$W/transcript.txt") 2>&1
BT="$W/base/tools"
RC=-1; OUT=""
x()   { printf '$ %s\n' "$*"; "$@"; RC=$?; printf '  exit=%d\n' "$RC"; }
xc()  { OUT=$("$@" 2>&1); RC=$?; printf '$ %s\n%s\n  exit=%d\n' "$*" "$OUT" "$RC"; }
die() { echo "SETUP-FAIL: $*"; exit 2; }

echo "lane HEAD before: $(git -C "$LANE" rev-parse HEAD)"
git -C "$LANE" archive "$BASE_SHA" tools | tar -x -C "$W/base" || die "archive"
x git -C "$LANE" rev-parse "$BASE_SHA:tools/harness/receipt_guard.py"
x git hash-object "$BT/harness/receipt_guard.py"

mk() {  # mk NAME: disposable lane with base tools committed on main and pushed to a bare origin
  local d="$W/$1" L="$W/$1/lane"
  mkdir -p "$d" || die "mkdir $d"
  git init -q -b main "$L" && git init -q --bare "$d/origin.git" || die "init $1"
  git -C "$L" config user.name repro && git -C "$L" config user.email repro@example.invalid \
    && git -C "$L" config commit.gpgsign false && git -C "$L" remote add origin "$d/origin.git" || die "config $1"
  cp -R "$BT" "$L/tools" && git -C "$L" add -A tools \
    && git -C "$L" commit -q -m "base tools ($BASE_SHA)" && git -C "$L" push -q -u origin main || die "base $1"
}
r1() {  # r1 NAME anchored|tip: receipt A on main+origin; anchored => HEAD on empty unpushed X above A
  mk "$1"; local L="$W/$1/lane"
  mkdir -p "$L/reports/round-49" && printf '{"filed": true}\n' > "$L/reports/round-49/validation.json" \
    && git -C "$L" add reports && git -C "$L" commit -q -m "round-49 receipt A on main" \
    && git -C "$L" push -q origin main || die "receipt $1"
  if [ "$2" = anchored ]; then
    git -C "$L" checkout -q --detach && git -C "$L" commit -q --allow-empty -m "X: empty, unpushed" || die "anchor $1"
  else
    git -C "$L" checkout -q --detach origin/main || die "tip $1"
  fi
}
r2() {  # r2 NAME anchored|tip: receipt C2 on main+origin; anchored => HEAD detached at pre-receipt C1
  mk "$1"; local L="$W/$1/lane" C1
  printf 'pre-receipt state\n' > "$L/NOTES.txt" && git -C "$L" add NOTES.txt \
    && git -C "$L" commit -q -m "C1 pre-receipt" || die "C1 $1"
  C1=$(git -C "$L" rev-parse HEAD)
  mkdir -p "$L/reports" && printf '{"filed": true}\n' > "$L/reports/validation.json" \
    && git -C "$L" add reports && git -C "$L" commit -q -m "C2 receipt on main" \
    && git -C "$L" push -q origin main || die "C2 $1"
  if [ "$2" = anchored ]; then git -C "$L" checkout -q --detach "$C1" || die "anchor $1"
  else git -C "$L" checkout -q --detach origin/main || die "tip $1"; fi
}

echo "== R1: receipt_guard reports local HEAD as committed_sha, which is not a landed commit =="
r1 r1 anchored; L=$W/r1/lane; G=$L/tools/harness/receipt_guard.py
R1_X=$(git -C "$L" rev-parse HEAD)
x git -C "$L" rev-parse HEAD
x git -C "$L" rev-parse origin/main
x git -C "$L" symbolic-ref -q HEAD
x git -C "$L" rev-parse 'HEAD^{tree}' 'origin/main^{tree}'
x git -C "$L" merge-base --is-ancestor HEAD origin/main; R1_ANC=$RC
xc python3 "$G" --repo-root "$L" reports/round-49/validation.json; R1_RC=$RC; R1_OUT=$OUT
xc env REFRESH_RECEIPTS=1 python3 "$G" --repo-root "$L" reports/round-49/validation.json
case $R1_OUT in *"committed_sha=$R1_X "*) R1_HIT=1 ;; *) R1_HIT=0 ;; esac
if [ "$R1_RC" = 3 ] && [ "$R1_HIT" = 1 ] && [ "$R1_ANC" = 1 ]; then R1_V=REPRODUCED; else R1_V=NOT-REPRODUCED; fi
echo "-- R1 control: same guard with HEAD = origin/main (pre-jj steady state)"
r1 r1-tip tip; T=$W/r1-tip/lane; GT=$T/tools/harness/receipt_guard.py
T_X=$(git -C "$T" rev-parse HEAD)
x git -C "$T" merge-base --is-ancestor HEAD origin/main; T_ANC=$RC
xc python3 "$GT" --repo-root "$T" reports/round-49/validation.json; T_RC=$RC
case $OUT in *"committed_sha=$T_X "*) T_HIT=1 ;; *) T_HIT=0 ;; esac

echo "== R2: receipt_guard probes only HEAD; a receipt committed on main/origin is missed =="
r2 r2 anchored; L=$W/r2/lane; G=$L/tools/harness/receipt_guard.py
x git -C "$L" rev-parse HEAD
x git -C "$L" rev-parse origin/main
x git -C "$L" cat-file -e 'origin/main:reports/validation.json'; R2_CF=$RC
x git -C "$L" cat-file -e 'refs/heads/main:reports/validation.json'; R2_CFM=$RC
R2_LS=$(git -C "$L" ls-tree -r --name-only HEAD -- reports/validation.json)
x git -C "$L" ls-tree -r --name-only HEAD -- reports/validation.json
xc python3 "$G" --repo-root "$L" reports/validation.json; R2_RC=$RC
if [ "$R2_RC" = 0 ] && [ "$R2_CF" = 0 ] && [ "$R2_CFM" = 0 ] && [ -z "$R2_LS" ]; then R2_V=REPRODUCED; else R2_V=NOT-REPRODUCED; fi
echo "-- R2 control: same guard with HEAD = origin/main (pre-jj flow)"
r2 r2-tip tip; T2=$W/r2-tip/lane; GT2=$T2/tools/harness/receipt_guard.py
xc python3 "$GT2" --repo-root "$T2" reports/validation.json; T2_RC=$RC
echo "-- calibration: base receipt_guard --selftest run inside the anchored R2 sandbox"
SJ=$(python3 "$G" --selftest 2>/dev/null); SRC=$?
printf '$ python3 %s --selftest | summary\n' "$G"
printf '%s' "$SJ" | python3 -c 'import json,sys; d=json.load(sys.stdin); print("  controls_passed=%d/%d selftest_passed=%s" % (d["controls_passed"], d["controls_total"], d["selftest_passed"]))'
printf '  exit=%d\n' "$SRC"

echo "== R3: check-readme-revisions selftest control 9 skips when the pinned base object is absent =="
mk r3; L3=$W/r3/lane
x git -C "$L3" cat-file -e "$PIN_SHA^{commit}"; R3_PIN=$RC
xc python3 "$L3/tools/check-readme-revisions.py" --selftest; R3_RC=$RC; R3_OUT=$OUT
case $R3_OUT in *"SKIP control: base c42d675 README flagged"*) R3_SK=1 ;; *) R3_SK=0 ;; esac
if [ "$R3_PIN" != 0 ] && [ "$R3_RC" = 0 ] && [ "$R3_SK" = 1 ]; then R3_V=REPRODUCED; else R3_V=NOT-REPRODUCED; fi
echo "-- R3 control: identical tool bytes, pin object present (temp clone of the lane, read as source)"
mkdir -p "$W/r3-present" && git clone -q --no-hardlinks "$LANE" "$W/r3-present/lane" || die "clone"
P=$W/r3-present/lane
x git -C "$P" checkout -q --detach "$BASE_SHA"
x git -C "$P" cat-file -e "$PIN_SHA^{commit}"; P_PIN=$RC
xc python3 "$P/tools/check-readme-revisions.py" --selftest; P_RC=$RC
case $OUT in *"PASS control: base c42d675 README flagged"*) P_PASS=1 ;; *) P_PASS=0 ;; esac
echo "-- R3 contrast: claims-freshness on the same missing pin (documented fail-closed side)"
cat > "$W/r3/claims-pin.json" <<EOF
{"round": 50, "baseline_commit": "$PIN_SHA", "claims": [{"id": "PIN", "axis": "calibration", "before": "pinned base probe", "before_checks": []}]}
EOF
xc python3 "$L3/tools/harness/claims-freshness.py" --claims "$W/r3/claims-pin.json" --root "$L3"; R3_CF=$RC

echo "== SUMMARY git=$(git --version | cut -d' ' -f3) python=$(python3 -V | cut -d' ' -f2) base=$BASE_SHA =="
echo "R1  $R1_V  guard_exit=$R1_RC committed_sha_is_HEAD=$R1_HIT HEAD_ancestor_of_origin_main_rc=$R1_ANC"
echo "R1c control HEAD=origin/main: guard_exit=$T_RC committed_sha_is_HEAD=$T_HIT HEAD_ancestor_rc=$T_ANC"
echo "R2  $R2_V  guard_exit=$R2_RC origin_main_blob_rc=$R2_CF refs_heads_main_blob_rc=$R2_CFM HEAD_ls_tree_empty=$([ -z "$R2_LS" ] && echo yes || echo no)"
echo "R2c control HEAD=origin/main: guard_exit=$T2_RC"
echo "R3  $R3_V  pin_object_rc=$R3_PIN selftest_exit=$R3_RC skip_line=$R3_SK"
echo "R3c pin present: pin_object_rc=$P_PIN selftest_exit=$P_RC pass_line=$P_PASS"
echo "R3x claims-freshness missing pin: exit=$R3_CF"
echo "lane HEAD after: $(git -C "$LANE" rev-parse HEAD)"
```

## Appendix B: jj 0.45.1 parity (`/tmp/r50-o/jj-parity.sh`)

```bash
#!/usr/bin/env bash
# Cross-check: do plain-git anchor states match real jj 0.45.1 colocated states? Sandboxes under $W only.
set -u
LANE=/home/vgpnk/Projects/shokunin/kotodama-shokunin
BASE_SHA=4ad26836552462d28a946ca3b067cab0b5ce3532
W=/tmp/r50-o/jj-parity
for v in $(compgen -e | grep '^GIT_'); do unset "$v"; done
rm -rf "$W" && mkdir -p "$W/base" || exit 2
exec > >(tee "$W/transcript.txt") 2>&1
BT="$W/base/tools"
RC=-1; OUT=""
x()   { printf '$ %s\n' "$*"; "$@"; RC=$?; printf '  exit=%d\n' "$RC"; }
xc()  { OUT=$("$@" 2>&1); RC=$?; printf '$ %s\n%s\n  exit=%d\n' "$*" "$OUT" "$RC"; }
die() { echo "SETUP-FAIL: $*"; exit 2; }
JJ=(jj --config 'user.name="repro"' --config 'user.email="repro@example.invalid"')

git -C "$LANE" archive "$BASE_SHA" tools | tar -x -C "$W/base" || die "archive"
x jj --version

setup() {  # setup NAME: base tools commit C1 on main, receipt commit C2 on main, both pushed to bare origin
  local d="$W/$1" L="$W/$1/lane"
  mkdir -p "$d" && git init -q -b main "$L" && git init -q --bare "$d/origin.git" \
    && git -C "$L" remote add origin "$d/origin.git" || die "init $1"
  git -C "$L" config user.name repro && git -C "$L" config user.email repro@example.invalid \
    && git -C "$L" config commit.gpgsign false || die "config $1"
  cp -R "$BT" "$L/tools" && git -C "$L" add -A tools && git -C "$L" commit -q -m "base tools (C1)" \
    && git -C "$L" push -q -u origin main || die "C1 $1"
  mkdir -p "$L/reports/round-49" && printf '{"filed": true}\n' > "$L/reports/round-49/validation.json" \
    && git -C "$L" add reports && git -C "$L" commit -q -m "receipt on main (C2)" \
    && git -C "$L" push -q origin main || die "C2 $1"
}

echo "== jj R1: jj colocate + jj new leaves HEAD on an empty local commit above origin/main =="
setup jr1; L=$W/jr1/lane
( cd "$L" && x "${JJ[@]}" git init --colocate )
( cd "$L" && x "${JJ[@]}" new )
x git -C "$L" rev-parse HEAD
x git -C "$L" rev-parse origin/main
x git -C "$L" symbolic-ref -q HEAD
x git -C "$L" merge-base --is-ancestor HEAD origin/main
xc python3 "$L/tools/harness/receipt_guard.py" --repo-root "$L" reports/round-49/validation.json

echo "== jj R2: jj new <C1> anchors HEAD below the tip; receipt on main/origin is missed =="
setup jr2; L=$W/jr2/lane
( cd "$L" && x "${JJ[@]}" git init --colocate )
C1=$(git -C "$L" rev-parse main~1)
x git -C "$L" rev-parse origin/main
( cd "$L" && x "${JJ[@]}" new "$C1" )
x git -C "$L" rev-parse HEAD
x git -C "$L" cat-file -e 'origin/main:reports/round-49/validation.json'
xc python3 "$L/tools/harness/receipt_guard.py" --repo-root "$L" reports/round-49/validation.json
echo "lane HEAD after: $(git -C "$LANE" rev-parse HEAD)"
```
