#!/bin/sh
# usage: run-controls.sh --freeze REV [--lands REV] [--base REV] [options]
#
# Round-77 do-nothing and gap-verification harness.  It materializes a clone of
# the lane under scratch (git clone --shared of the lane, its `main` pinned to
# the freeze — the do-nothing measured revision), hands that clone to both
# round-77 counters as --root, and records for each control the exact argv, the
# counter's stdout+stderr, its exit status and a verdict.
#
#   control 1  lands == freeze   the legal do-nothing relation with no data
#              landed.  Claim C must FAIL with its data legs red (ENTRIES,
#              ROWS) while FROZENCFG/STAMP stay green; claim Ca must FAIL with
#              REPAIR/ANNOTATE red while FROZENCFG/STAMP/LEDGER stay green.
#              A PASS (or a refusal summary) at the freeze is a violation: a
#              do-nothing landing may not pass and the frozen config may not be
#              unusable.
#   control 2  lands == base     the counters must REFUSE (exit 2) and print no
#              LEG line, because the base is not a descendant of the freeze.
#   control 3  no --work, no $HYAKU_SCRATCH, no $SHOKUNIN_SCRATCH, no $TMPDIR
#              the counters must REFUSE (exit 2) and print no LEG line.  A
#              counter that invents /fast/scratch/hyaku on its own is exactly
#              the graded gap this control exists to catch, so the fallback
#              directory is stat'ed before and after the run.
#   control 4  Ca without --combined  must REFUSE (exit 2), no LEG line; a red
#              COMBINED leg would read as a data defect instead of the input
#              error it is.
#
# Options:
#   --freeze REV       the round-77 freeze commit (required, 40 hex).
#   --lands REV        the round-77 landing (default: the freeze; it is the
#                      revision the harness records and the Ca --combined
#                      default, never a control's landing).
#   --base REV         the frozen claim base (default: the `base` field of
#                      <freeze>:reports/round-77/claims.json; a --base that
#                      disagrees with the frozen one is refused, because
#                      control 2 would then be unattributable).
#   --combined REV     --combined for the Ca controls (default: --lands when it
#                      differs from the freeze, else the freeze).
#   --main REV         revision the clone's `main` is pinned to (default: the
#                      freeze — the do-nothing measured revision).
#   --fleet-root DIR   fleet root handed to both counters (default
#                      /home/vgpnk/Projects/shokunin).
#   --lane DIR         lane repository (default
#                      /home/vgpnk/Projects/shokunin/kotodama-shokunin).
#   --scratch DIR      harness scratch root (default
#                      ${HYAKU_SCRATCH:-/fast/scratch/hyaku}/kotodama-r77/controls).
#                      The counters get --work inside it plus HYAKU_SCRATCH,
#                      SHOKUNIN_SCRATCH and TMPDIR pointing into it; no path in
#                      this script is a literal /tmp.
#   --out DIR          receipt directory (default <lane>/reports/round-77/telemetry,
#                      the two names the round-77 freeze manifest lists:
#                      controls-c.txt, controls-ca.txt).
#   --counter-dir DIR  take accept-c.py / accept-ca.py from DIR (rehearsal and
#                      the selfcheck); default: the clone's committed copy,
#                      then <lane>/reports/round-77/, then the wave counters
#                      directory, then the wave-1 stage drafts.
#   --require-red-c LIST / --require-green-c LIST
#   --require-red-ca LIST / --require-green-ca LIST
#                      the leg names control 1 insists on (empty = none).  The
#                      defaults are the legs the frozen claims name for the
#                      do-nothing shape; override when the frozen leg table
#                      differs and keep the override with the receipt.
#   --allow-base-mismatch  run control 2 even when --base differs from the
#                      frozen claim base (the refusal is then not attributable
#                      to the claim base; the divergence is printed).
#   --scratch-refusal both|ca|none
#                      which counter control 3 binds.  Default `ca`: the draft
#                      claim text that names this refusal names it for claim Ca
#                      only ("missing `--combined`/`--work` refused exit 2
#                      printing no leg line"); claim C's do-nothing control
#                      names only lands==freeze, lands==base and junk
#                      landings.  `both` opts in when the frozen C claim also
#                      names it (C denominator 3); `none` drops the control.
#   --selftest         build a fixture repo plus good/bad stub counters under
#                      --scratch and prove the harness passes the good pair and
#                      catches all seven bad controls.  Touches no lane path.
#   --plan             materialize the clone, resolve the counters and print
#                      the invocations; executes no counter, writes no receipt.
#   --rm               delete the materialized clone after the run (default:
#                      keep it and record its path).
#
# Receipts end with one verdict line each:
#   CONTROLS-C-77:  PASS controls=3/3   |  FAIL controls=<n>/3
#   CONTROLS-CA-77: PASS controls=4/4   |  FAIL controls=<n>/4
# Every failed assertion is named on the `# control verdict:` line of its
# control, so a FAIL is attributable without re-running anything.
#
# Exit: 0 every control met its expectation; 1 at least one control deviated
# (the receipts are still written); 2 setup error (bad revision, missing
# counter, clone failure) — nothing graded, no receipt written.

set -u

LANE=/home/vgpnk/Projects/shokunin/kotodama-shokunin
FL=/home/vgpnk/Projects/shokunin
TEL=reports/round-77/telemetry

FREEZE=
LANDS=
BASE=
COMBINED=
MAINPIN=
SCRATCH=
OUT=
CDIR=
PLAN=0
RM=0
SELFTEST=0
ALLOW_BASE_MISMATCH=0
# Which counter control 3 (the missing-scratch refusal) binds: both|ca|none.
# Default `ca`: the claim text that named this refusal named it for claim Ca
# only ("missing `--combined`/`--work` refused exit 2 printing no leg line"),
# while claim C's do-nothing control names only lands==freeze / lands==base /
# junk landings.  Asserting it for C by default would manufacture a violation
# against a clause C does not freeze; `--scratch-refusal=both` opts in when the
# frozen C claim does name it (the receipt then records 3 C controls).
SCRATCH_CTRL=ca

# Control-1 leg expectations (the frozen claims' do-nothing sentences).
# C green is FROZENCFG only: the reshaped draft's claim-C after-state names a
# 13-leg lineage set that has no STAMP (…FROZENCFG, INDEX), while the wave-1 C
# counter's table prints 15 legs and includes STAMP.  Asserting STAMP here
# would fail a legitimate freeze of the 13-leg shape; pass
# --require-green-c 'FROZENCFG STAMP' when the frozen table carries STAMP.
C_RED="ENTRIES ROWS"
C_GREEN="FROZENCFG"
CA_RED="REPAIR ANNOTATE"
CA_GREEN="FROZENCFG STAMP LEDGER"

die() { printf 'run-controls.sh: %s\n' "$*" >&2; exit 2; }

usage() {
  printf 'usage: run-controls.sh --freeze REV [--lands REV] [--base REV]\n' >&2
  printf '                      [--combined REV] [--main REV]\n' >&2
  printf '                      [--fleet-root DIR] [--lane DIR] [--scratch DIR]\n' >&2
  printf '                      [--out DIR] [--counter-dir DIR]\n' >&2
  printf '                      [--require-red-c LIST] [--require-green-c LIST]\n' >&2
  printf '                      [--require-red-ca LIST] [--require-green-ca LIST]\n' >&2
  printf '                      [--allow-base-mismatch] [--selftest]\n' >&2
  printf '                      [--plan] [--rm]\n' >&2
}

while [ $# -gt 0 ]; do
  case $1 in
    --freeze) [ $# -ge 2 ] || die "--freeze needs a revision"; FREEZE=$2; shift ;;
    --freeze=*) FREEZE=${1#--freeze=} ;;
    --lands) [ $# -ge 2 ] || die "--lands needs a revision"; LANDS=$2; shift ;;
    --lands=*) LANDS=${1#--lands=} ;;
    --base) [ $# -ge 2 ] || die "--base needs a revision"; BASE=$2; shift ;;
    --base=*) BASE=${1#--base=} ;;
    --combined) [ $# -ge 2 ] || die "--combined needs a revision"; COMBINED=$2; shift ;;
    --combined=*) COMBINED=${1#--combined=} ;;
    --main) [ $# -ge 2 ] || die "--main needs a revision"; MAINPIN=$2; shift ;;
    --main=*) MAINPIN=${1#--main=} ;;
    --fleet-root) [ $# -ge 2 ] || die "--fleet-root needs a directory"; FL=$2; shift ;;
    --fleet-root=*) FL=${1#--fleet-root=} ;;
    --lane) [ $# -ge 2 ] || die "--lane needs a directory"; LANE=$2; shift ;;
    --lane=*) LANE=${1#--lane=} ;;
    --scratch) [ $# -ge 2 ] || die "--scratch needs a directory"; SCRATCH=$2; shift ;;
    --scratch=*) SCRATCH=${1#--scratch=} ;;
    --out) [ $# -ge 2 ] || die "--out needs a directory"; OUT=$2; shift ;;
    --out=*) OUT=${1#--out=} ;;
    --counter-dir) [ $# -ge 2 ] || die "--counter-dir needs a directory"; CDIR=$2; shift ;;
    --counter-dir=*) CDIR=${1#--counter-dir=} ;;
    --require-red-c) [ $# -ge 2 ] || die "--require-red-c needs a list"; C_RED=$2; shift ;;
    --require-red-c=*) C_RED=${1#--require-red-c=} ;;
    --require-green-c) [ $# -ge 2 ] || die "--require-green-c needs a list"; C_GREEN=$2; shift ;;
    --require-green-c=*) C_GREEN=${1#--require-green-c=} ;;
    --require-red-ca) [ $# -ge 2 ] || die "--require-red-ca needs a list"; CA_RED=$2; shift ;;
    --require-red-ca=*) CA_RED=${1#--require-red-ca=} ;;
    --require-green-ca) [ $# -ge 2 ] || die "--require-green-ca needs a list"; CA_GREEN=$2; shift ;;
    --require-green-ca=*) CA_GREEN=${1#--require-green-ca=} ;;
    --allow-base-mismatch) ALLOW_BASE_MISMATCH=1 ;;
    --scratch-refusal) [ $# -ge 2 ] || die "--scratch-refusal needs both|ca|none"; SCRATCH_CTRL=$2; shift ;;
    --scratch-refusal=*) SCRATCH_CTRL=${1#--scratch-refusal=} ;;
    --selftest) SELFTEST=1 ;;
    --plan) PLAN=1 ;;
    --rm) RM=1 ;;
    -h|--help) usage; exit 0 ;;
    *) printf 'run-controls.sh: unknown argument: %s\n' "$1" >&2; usage; exit 2 ;;
  esac
  shift
done

[ -n "$SCRATCH" ] || SCRATCH=${HYAKU_SCRATCH:-/fast/scratch/hyaku}/kotodama-r77/controls
case $SCRATCH_CTRL in
  both|ca|none) ;;
  *) die "--scratch-refusal must be both|ca|none, got '$SCRATCH_CTRL'" ;;
esac
# Where a round-77 counter that invents its own scratch root would land; stat'ed
# around control 3 (it is never created or removed here).
FB_DIR=${HYAKU_SCRATCH:-/fast/scratch/hyaku}/kotodama-r77

# ---- helpers ---------------------------------------------------------------

# shq <word>: quote for display only (the argv is never re-parsed).
shq() {
  case $1 in
    ''|*[!A-Za-z0-9_./:=@%,+-]*)
      printf "'%s'" "$(printf '%s' "$1" | sed "s/'/'\\\\''/g")" ;;
    *) printf '%s' "$1" ;;
  esac
}

# emit_cmd <file|-> <argv...>
emit_cmd() {
  _ecf=$1; shift
  _ecl='$'
  for _eca in "$@"; do _ecl="$_ecl $(shq "$_eca")"; done
  if [ "$_ecf" = - ]; then printf '%s\n' "$_ecl"; else printf '%s\n' "$_ecl" >> "$_ecf"; fi
}

leg_lines() { grep -c '^LEG \(PASS\|FAIL\) [A-Z][A-Z0-9_]*$' "$1" 2>/dev/null || true; }
leg_red() { sed -n 's/^LEG FAIL \([A-Z][A-Z0-9_]*\)$/\1/p' "$1"; }
leg_green() { sed -n 's/^LEG PASS \([A-Z][A-Z0-9_]*\)$/\1/p' "$1"; }
leg_pcount() { leg_green "$1" | grep -c . || true; }
leg_fcount() { leg_red "$1" | grep -c . || true; }

# missing_from <names> <log> <PASS|FAIL>: prints the names with no such leg line
missing_from() {
  for _mn in $1; do
    grep -qx "LEG $3 $_mn" "$2" || printf '%s ' "$_mn"
  done
}

_stat() { if [ -e "$1" ]; then printf 'present'; else printf 'absent'; fi; }

# exec_counter <log> <strip:0|1> <argv...>
# strip=1 runs with HYAKU_SCRATCH, SHOKUNIN_SCRATCH and TMPDIR removed from the
# environment (control 3); strip=0 points all three into the harness scratch.
exec_counter() {
  _xo=$1; _xs=$2; shift 2
  if [ "$_xs" = 1 ]; then
    env -u HYAKU_SCRATCH -u SHOKUNIN_SCRATCH -u TMPDIR "$@" > "$_xo" 2>&1
  else
    env HYAKU_SCRATCH="$SCRATCH" SHOKUNIN_SCRATCH="$SCRATCH" TMPDIR="$SCRATCH/tmp" "$@" > "$_xo" 2>&1
  fi
}

# evaluate_donothing <label> <work-name> <red> <green> <summary-prefix> <argv...>
# Appends to $RCPT; bumps $RUN_VIO on a deviation.
evaluate_donothing() {
  _label=$1; _wn=$2; _red=$3; _green=$4; _sum=$5; shift 5
  _w=$SCRATCH/work/$R_TAG-$_wn
  set -- "$@" --work "$_w"
  if [ "$PLAN" = 1 ]; then
    printf '## %s\n' "$_label"
    emit_cmd - "$@"
    printf '\n'
    return 0
  fi
  mkdir -p "$_w" || die "cannot create $_w"
  _log=$_w/run.txt
  printf '## %s\n' "$_label" >> "$RCPT"
  emit_cmd "$RCPT" "$@"
  exec_counter "$_log" 0 "$@"
  _rc=$?
  cat "$_log" >> "$RCPT"
  printf 'exit=%s\n' "$_rc" >> "$RCPT"
  printf '# expected: exit=1, summary "%s: FAIL", red=[%s], green=[%s]\n' \
    "$_sum" "$_red" "$_green" >> "$RCPT"
  printf '# observed legs: PASS=%s FAIL=%s\n' "$(leg_pcount "$_log")" "$(leg_fcount "$_log")" >> "$RCPT"
  _bad=
  [ "$_rc" = 1 ] || _bad="$_bad exit=$_rc(want 1);"
  _n=$(leg_lines "$_log"); _n=${_n:-0}
  [ "$_n" -gt 0 ] || _bad="$_bad legs=0(nothing graded);"
  grep -q "^$_sum: FAIL" "$_log" || _bad="$_bad no-'$_sum: FAIL'-summary;"
  grep -q "^$_sum: FAIL legs=0/" "$_log" && _bad="$_bad refusal-summary-at-the-freeze;"
  _miss=$(missing_from "$_red" "$_log" FAIL)
  [ -z "$_miss" ] || _bad="$_bad red legs absent: $_miss;"
  _miss=$(missing_from "$_green" "$_log" PASS)
  [ -z "$_miss" ] || _bad="$_bad green legs failed: $_miss;"
  if [ -z "$_bad" ]; then
    printf '# control verdict: PASS\n\n' >> "$RCPT"
  else
    printf '# control verdict: FAIL —%s\n\n' "$_bad" >> "$RCPT"
    RUN_VIO=$((RUN_VIO + 1))
  fi
  return 0
}

# evaluate_refusal <label> <work-name|-> <strip:0|1> <reason-re> <argv...>
# `-` means the invocation carries no --work at all (control 3); <reason-re> is
# an ERE the refusal output must match, so an exit 2 for the wrong reason does
# not read as a pass.  Appends to $RCPT; bumps $RUN_VIO on a deviation.
evaluate_refusal() {
  _rlabel=$1; _rwn=$2; _rstr=$3; _rwhy=$4; shift 4
  R_SEQ=$((R_SEQ + 1))
  _rw=$SCRATCH/work/$R_TAG-refusal-$R_SEQ.txt
  if [ "$_rwn" != - ]; then
    set -- "$@" --work "$SCRATCH/work/$R_TAG-$_rwn"
  fi
  if [ "$PLAN" = 1 ]; then
    printf '## %s\n' "$_rlabel"
    emit_cmd - "$@"
    printf '# expected reason: /%s/\n' "$_rwhy"
    [ "$_rstr" = 1 ] && printf '# env: HYAKU_SCRATCH, SHOKUNIN_SCRATCH and TMPDIR unset; no --work\n'
    printf '\n'
    return 0
  fi
  [ "$_rwn" = - ] || mkdir -p "$SCRATCH/work/$R_TAG-$_rwn" || die "cannot create $_rw"
  printf '## %s\n' "$_rlabel" >> "$RCPT"
  emit_cmd "$RCPT" "$@"
  if [ "$_rstr" = 1 ]; then
    printf '# env: HYAKU_SCRATCH, SHOKUNIN_SCRATCH and TMPDIR unset; no --work\n' >> "$RCPT"
    printf '# fallback stat before: %s %s\n' "$FB_DIR" "$(_stat "$FB_DIR")" >> "$RCPT"
  fi
  exec_counter "$_rw" "$_rstr" "$@"
  _rrc=$?
  cat "$_rw" >> "$RCPT"
  printf 'exit=%s\n' "$_rrc" >> "$RCPT"
  printf '# expected: exit=2 (refused) on /%s/, no LEG line\n' "$_rwhy" >> "$RCPT"
  printf '# observed legs: %s (leg-shaped line count)\n' "$(leg_lines "$_rw")" >> "$RCPT"
  if [ "$_rstr" = 1 ]; then
    printf '# fallback stat after: %s %s\n' "$FB_DIR" "$(_stat "$FB_DIR")" >> "$RCPT"
  fi
  _rbad=
  [ "$_rrc" = 2 ] || _rbad="exit=$_rrc(want 2);"
  _rln=$(leg_lines "$_rw"); _rln=${_rln:-0}
  [ "$_rln" = 0 ] || _rbad="$_rbad $_rln LEG line(s) printed(want 0);"
  grep -Eqi -e "$_rwhy" "$_rw" || _rbad="$_rbad refusal not attributed to /$_rwhy/;"
  if [ -z "$_rbad" ]; then
    printf '# control verdict: PASS\n\n' >> "$RCPT"
  else
    printf '# control verdict: FAIL — %s\n\n' "$_rbad" >> "$RCPT"
    RUN_VIO=$((RUN_VIO + 1))
  fi
  return 0
}

# pick_counter <clone> <counter-dir|-> <name>: prints the counter path.
pick_counter() {
  if [ "$2" != - ]; then
    [ -f "$2/$3" ] || die "counter not found: $2/$3"
    printf '%s' "$2/$3"
    return 0
  fi
  for _pc in "$1/reports/round-77/$3" \
             "$LANE/reports/round-77/$3" \
             "$LANE/.ufo/waves/round-77/counters/$3" \
             "$LANE/.ufo/waves/round-77/w1/stage/ExecAdaptC/$3" \
             "$LANE/.ufo/waves/round-77/w1/stage/ExecAdaptCa/$3"; do
    if [ -f "$_pc" ]; then printf '%s' "$_pc"; return 0; fi
  done
  die "no round-77 counter '$3' (looked in the clone, $LANE/reports/round-77/, $LANE/.ufo/waves/round-77/counters/ and the wave-1 stage drafts; pass --counter-dir)"
}

# ensure_rev <clone> <rev> <label>
ensure_rev() {
  git -C "$1" cat-file -e "$2^{commit}" 2>/dev/null && return 0
  git -C "$1" fetch -q --no-tags origin "$2" > /dev/null 2>&1
  git -C "$1" cat-file -e "$2^{commit}" 2>/dev/null && return 0
  die "$3 $2 is not a commit in the clone (no lane ref reaches it; publish a ref)"
}

# receipt_header <file> <claim> <counter> <counter-sha>
receipt_header() {
  {
    printf '# %s — claim %s controls (round 77), freeze %s\n' "$(basename "$1")" "$2" "$R_FREEZE"
    printf '# harness: %s sha256=%s\n' "$0" "$HARNESS_SHA"
    printf '# lane: %s\n' "$LANE"
    printf '# repo handed to the counters: %s (git clone --shared of the lane)\n' "$RC_CLONE"
    printf '# clone HEAD: %s (main pinned to the freeze: the do-nothing measured revision)\n' "$RC_HEAD"
    printf '# clone tree: %s\n' "$RC_TREE"
    printf '# recorded lands: %s  base: %s  combined: %s  main pin: %s\n' \
      "$R_LANDS" "$R_BASE" "$R_COMBINED" "$R_MAINPIN"
    printf '# counter: %s sha256=%s\n' "$3" "$4"
    printf '# scratch: %s (HYAKU_SCRATCH, SHOKUNIN_SCRATCH and TMPDIR point here for every graded run; never a literal /tmp)\n' "$SCRATCH"
  } >> "$1"
}

# run_controls <repo> <lands> <freeze> <base> <main-pin> <combined> <cdir|-> <out> <tag>
run_controls() {
  R_LANDS=$2; R_FREEZE=$3; R_BASE=$4; R_MAINPIN=$5; R_COMBINED=$6
  R_OUT=$8; R_TAG=$9
  RUN_VIO=0; R_SEQ=0
  RC_CLONE=$SCRATCH/clone-$R_TAG

  rm -rf -- "$RC_CLONE"
  git clone -q --shared "$1" "$RC_CLONE" || die "git clone --shared $1 $RC_CLONE failed"
  _top=$(git -C "$RC_CLONE" rev-parse --show-toplevel 2>/dev/null) || \
    die "the clone at $RC_CLONE has no worktree toplevel"
  [ "$_top" = "$RC_CLONE" ] || \
    die "clone toplevel '$_top' != '$RC_CLONE'; refusing to touch it"

  ensure_rev "$RC_CLONE" "$R_FREEZE" freeze
  ensure_rev "$RC_CLONE" "$R_BASE" base
  ensure_rev "$RC_CLONE" "$R_LANDS" lands
  ensure_rev "$RC_CLONE" "$R_MAINPIN" main-pin
  if [ "$R_COMBINED" != - ]; then ensure_rev "$RC_CLONE" "$R_COMBINED" combined; fi

  git -C "$RC_CLONE" checkout -q -B main "$R_MAINPIN" || die "cannot pin the clone's main to $R_MAINPIN"
  RC_HEAD=$(git -C "$RC_CLONE" rev-parse HEAD) || die "cannot read the clone HEAD"
  RC_TREE=$(git -C "$RC_CLONE" rev-parse "$RC_HEAD^{tree}") || die "cannot read the clone tree"

  CC=$(pick_counter "$RC_CLONE" "$7" accept-c.py)
  CCA=$(pick_counter "$RC_CLONE" "$7" accept-ca.py)
  CC_SHA=$(sha256sum "$CC" | cut -d' ' -f1)
  CCA_SHA=$(sha256sum "$CCA" | cut -d' ' -f1)

  if [ "$PLAN" = 1 ]; then
    printf '# plan only: nothing executed, no receipt written\n'
    printf '# clone: %s (git clone --shared %s; main -> %s)\n' "$RC_CLONE" "$1" "$R_MAINPIN"
    printf '# counter C:  %s\n# counter Ca: %s\n\n' "$CC" "$CCA"
  else
    mkdir -p "$R_OUT" "$SCRATCH/work" || die "cannot create $R_OUT / $SCRATCH/work"
  fi

  # ---- claim C -------------------------------------------------------------
  _c_expect=2
  RCPT=$R_OUT/controls-c.txt
  [ "$PLAN" = 1 ] || receipt_header "$RCPT" C "$CC" "$CC_SHA"
  evaluate_donothing "control 1: lands == freeze (legal ancestor relation; no data landed)" c1 \
    "$C_RED" "$C_GREEN" ACCEPT-C-77 \
    python3 -B "$CC" --root "$RC_CLONE" --lands "$R_FREEZE" --freeze "$R_FREEZE" --fleet-root "$FL"
  evaluate_refusal "control 2: lands == base (refusal, no leg line)" c2 0 'base' \
    python3 -B "$CC" --root "$RC_CLONE" --lands "$R_BASE" --freeze "$R_FREEZE" --fleet-root "$FL"
  if [ "$SCRATCH_CTRL" = both ]; then
    _c_expect=3
    evaluate_refusal "control 3: no --work and no \$HYAKU_SCRATCH/\$SHOKUNIN_SCRATCH/\$TMPDIR (refusal, no leg line)" - 1 'scratch|--work|HYAKU_SCRATCH' \
      python3 -B "$CC" --root "$RC_CLONE" --lands "$R_FREEZE" --freeze "$R_FREEZE" --fleet-root "$FL"
  else
    if [ "$PLAN" = 1 ]; then
      printf '## control 3: skipped (--scratch-refusal=%s: the frozen claims do not bind the missing-scratch refusal to claim C)\n\n' "$SCRATCH_CTRL"
    else
      printf '## control 3: skipped (--scratch-refusal=%s: the frozen claims do not bind the missing-scratch refusal to claim C)\n\n' "$SCRATCH_CTRL" >> "$RCPT"
    fi
  fi
  [ "$PLAN" = 1 ] || {
    if [ "$RUN_VIO" = 0 ]; then
      printf 'CONTROLS-C-77: PASS controls=%s/%s\n' "$_c_expect" "$_c_expect" >> "$RCPT"
    else
      printf 'CONTROLS-C-77: FAIL controls=%s/%s\n' "$((_c_expect - RUN_VIO))" "$_c_expect" >> "$RCPT"
    fi
  }
  _c_vio=$RUN_VIO

  # ---- claim Ca ------------------------------------------------------------
  _ca_expect=3
  RCPT=$R_OUT/controls-ca.txt
  [ "$PLAN" = 1 ] || receipt_header "$RCPT" Ca "$CCA" "$CCA_SHA"
  evaluate_donothing "control 1: lands == freeze (no data landed, no corrections applied)" ca1 \
    "$CA_RED" "$CA_GREEN" ACCEPT-CA-77 \
    python3 -B "$CCA" --root "$RC_CLONE" --lands "$R_FREEZE" --freeze "$R_FREEZE" --fleet-root "$FL" \
    --combined "$R_COMBINED" --main "$R_MAINPIN"
  evaluate_refusal "control 2: lands == base (refusal, no leg line)" ca2 0 'base' \
    python3 -B "$CCA" --root "$RC_CLONE" --lands "$R_BASE" --freeze "$R_FREEZE" --fleet-root "$FL" \
    --combined "$R_COMBINED" --main "$R_MAINPIN"
  if [ "$SCRATCH_CTRL" = both ] || [ "$SCRATCH_CTRL" = ca ]; then
    _ca_expect=4
    evaluate_refusal "control 3: no --work and no \$HYAKU_SCRATCH/\$SHOKUNIN_SCRATCH/\$TMPDIR (refusal, no leg line)" - 1 'scratch|--work|HYAKU_SCRATCH' \
      python3 -B "$CCA" --root "$RC_CLONE" --lands "$R_FREEZE" --freeze "$R_FREEZE" --fleet-root "$FL" \
      --combined "$R_COMBINED" --main "$R_MAINPIN"
  else
    printf '## control 3: skipped (--scratch-refusal=%s)\n\n' "$SCRATCH_CTRL"
    [ "$PLAN" = 1 ] || printf '## control 3: skipped (--scratch-refusal=%s)\n\n' "$SCRATCH_CTRL" >> "$RCPT"
  fi
  evaluate_refusal "control 4: Ca without --combined (refusal, no leg line)" ca4 0 'combined' \
    python3 -B "$CCA" --root "$RC_CLONE" --lands "$R_FREEZE" --freeze "$R_FREEZE" --fleet-root "$FL" \
    --main "$R_MAINPIN"
  [ "$PLAN" = 1 ] || {
    _ca_vio=$((RUN_VIO - _c_vio))
    if [ "$_ca_vio" = 0 ]; then
      printf 'CONTROLS-CA-77: PASS controls=%s/%s\n' "$_ca_expect" "$_ca_expect" >> "$RCPT"
    else
      printf 'CONTROLS-CA-77: FAIL controls=%s/%s\n' "$((_ca_expect - _ca_vio))" "$_ca_expect" >> "$RCPT"
    fi
  }

  if [ "$RM" = 1 ]; then
    rm -rf -- "$RC_CLONE"
  fi
  [ "$RUN_VIO" = 0 ]
}

# ---- selfcheck -------------------------------------------------------------

# The stub counters below are the falsification fixture: `good` must satisfy
# every control, `bad` (the same bytes plus a bad-mode marker) must satisfy
# none, so the harness cannot pass by accident.
STUB_C=$(cat <<'STUB'
import os, subprocess, sys
CLAIM = "C"
LEGS = [("FROZENCFG", True), ("STAMP", True), ("ENTRIES", False), ("ROWS", False)]

def arg(name):
    a = sys.argv
    return a[a.index(name) + 1] if name in a else None

root = arg("--root") or "."
lands = arg("--lands") or ""
work = arg("--work")

def subject(rev):
    r = subprocess.run(["git", "-C", root, "log", "-1", "--format=%s", rev],
                       capture_output=True, text=True)
    return r.stdout.strip()

def refuse(msg):
    print("REFUSED: " + msg)
    print("ACCEPT-%s-77: FAIL legs=0/%d (refused: %s)" % (CLAIM, len(LEGS), msg))
    sys.exit(2)

if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "bad-mode")):
    for name, _ in LEGS:
        print("LEG PASS " + name)
    print("ACCEPT-%s-77: PASS legs=%d/%d" % (CLAIM, len(LEGS), len(LEGS)))
    sys.exit(0)

if not (work or os.environ.get("HYAKU_SCRATCH") or os.environ.get("SHOKUNIN_SCRATCH")
        or os.environ.get("TMPDIR")):
    refuse("no scratch root (none of --work, $HYAKU_SCRATCH, $SHOKUNIN_SCRATCH, $TMPDIR)")
if subject(lands).startswith("stub-base"):
    refuse("--lands equals the frozen claim base")
red = 0
for name, green in LEGS:
    print("LEG %s %s" % ("PASS" if green else "FAIL", name))
    if not green:
        red += 1
print("ACCEPT-%s-77: FAIL legs=%d/%d" % (CLAIM, len(LEGS) - red, len(LEGS)))
sys.exit(1)
STUB
)

STUB_CA=$(cat <<'STUB'
import os, subprocess, sys
CLAIM = "CA"
LEGS = [("FROZENCFG", True), ("STAMP", True), ("LEDGER", True),
        ("REPAIR", False), ("ANNOTATE", False)]

def arg(name):
    a = sys.argv
    return a[a.index(name) + 1] if name in a else None

root = arg("--root") or "."
lands = arg("--lands") or ""
work = arg("--work")
combined = arg("--combined")

def subject(rev):
    r = subprocess.run(["git", "-C", root, "log", "-1", "--format=%s", rev],
                       capture_output=True, text=True)
    return r.stdout.strip()

def refuse(msg):
    print("REFUSED: " + msg)
    print("ACCEPT-%s-77: FAIL legs=0/%d (refused: %s)" % (CLAIM, len(LEGS), msg))
    sys.exit(2)

if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "bad-mode")):
    for name, _ in LEGS:
        print("LEG PASS " + name)
    print("ACCEPT-%s-77: PASS legs=%d/%d" % (CLAIM, len(LEGS), len(LEGS)))
    sys.exit(0)

if not (work or os.environ.get("HYAKU_SCRATCH") or os.environ.get("SHOKUNIN_SCRATCH")
        or os.environ.get("TMPDIR")):
    refuse("no scratch root (none of --work, $HYAKU_SCRATCH, $SHOKUNIN_SCRATCH, $TMPDIR)")
if not combined:
    refuse("--combined is required")
if subject(lands).startswith("stub-base"):
    refuse("--lands equals the frozen claim base")
red = 0
for name, green in LEGS:
    print("LEG %s %s" % ("PASS" if green else "FAIL", name))
    if not green:
        red += 1
print("ACCEPT-%s-77: FAIL legs=%d/%d" % (CLAIM, len(LEGS) - red, len(LEGS)))
sys.exit(1)
STUB
)

# gc_at <repo> <git args...> — fixture identity passed per command, never
# written to any config.
gc_at() {
  _gr=$1; shift
  git -C "$_gr" -c user.name=selfcheck -c user.email=s@s.invalid -c commit.gpgsign=false "$@"
}

selfcheck() {
  _sc=$SCRATCH/selfcheck
  rm -rf -- "$_sc"
  mkdir -p "$_sc/repo" "$_sc/good" "$_sc/bad" "$_sc/out-good" "$_sc/out-bad" "$SCRATCH/tmp" "$SCRATCH/work" || return 2
  _repo=$_sc/repo
  git -C "$_repo" init -q || { printf 'selfcheck: git init failed\n' >&2; return 2; }
  _top=$(git -C "$_repo" rev-parse --show-toplevel 2>/dev/null) || return 2
  [ "$_top" = "$_repo" ] || { printf "selfcheck: fixture toplevel '%s' != '%s'\n" "$_top" "$_repo" >&2; return 2; }
  printf 'fixture\n' > "$_repo/marker" || return 2
  gc_at "$_repo" add -A > /dev/null && gc_at "$_repo" commit -qm stub-base || return 2
  _b=$(gc_at "$_repo" rev-parse HEAD)
  printf 'fixture\n' >> "$_repo/marker" && gc_at "$_repo" add -A > /dev/null && \
    gc_at "$_repo" commit -qm stub-freeze || return 2
  _f=$(gc_at "$_repo" rev-parse HEAD)
  printf 'fixture\n' >> "$_repo/marker" && gc_at "$_repo" add -A > /dev/null && \
    gc_at "$_repo" commit -qm stub-lands || return 2
  _l=$(gc_at "$_repo" rev-parse HEAD)
  printf '%s\n' "$STUB_C" > "$_sc/good/accept-c.py" || return 2
  printf '%s\n' "$STUB_CA" > "$_sc/good/accept-ca.py" || return 2
  printf '%s\n' "$STUB_C" > "$_sc/bad/accept-c.py" || return 2
  printf '%s\n' "$STUB_CA" > "$_sc/bad/accept-ca.py" || return 2
  : > "$_sc/bad/bad-mode"
  printf 'selfcheck fixture: base=%s freeze=%s lands=%s\n' "$_b" "$_f" "$_l"

  if run_controls "$_repo" "$_l" "$_f" "$_b" "$_f" "$_f" "$_sc/good" "$_sc/out-good" scgood; then
    _gvi=0
  else
    _gvi=$RUN_VIO
  fi
  if run_controls "$_repo" "$_l" "$_f" "$_b" "$_f" "$_f" "$_sc/bad" "$_sc/out-bad" scbad; then
    _bvi=0
  else
    _bvi=$RUN_VIO
  fi
  _save_ctrl=$SCRATCH_CTRL
  SCRATCH_CTRL=both
  if run_controls "$_repo" "$_l" "$_f" "$_b" "$_f" "$_f" "$_sc/good" "$_sc/out-scope" scscope; then
    _svi=0
  else
    _svi=$RUN_VIO
  fi
  SCRATCH_CTRL=$_save_ctrl

  _fail=
  [ "$_gvi" = 0 ] || _fail="$_fail good-run violations=$_gvi(want 0);"
  [ "$_bvi" = 6 ] || _fail="$_fail bad-run violations=$_bvi(want 6);"
  [ "$_svi" = 0 ] || _fail="$_fail scope-run violations=$_svi(want 0);"
  grep -q '^CONTROLS-C-77: PASS controls=2/2$' "$_sc/out-good/controls-c.txt" || \
    _fail="$_fail good run: no 'CONTROLS-C-77: PASS controls=2/2';"
  grep -q '^CONTROLS-CA-77: PASS controls=4/4$' "$_sc/out-good/controls-ca.txt" || \
    _fail="$_fail good run: no 'CONTROLS-CA-77: PASS controls=4/4';"
  grep -q '^## control 3: skipped' "$_sc/out-good/controls-c.txt" || \
    _fail="$_fail good run: C control 3 not recorded as skipped;"
  grep -q '^CONTROLS-C-77: PASS controls=3/3$' "$_sc/out-scope/controls-c.txt" || \
    _fail="$_fail scope run: no 'CONTROLS-C-77: PASS controls=3/3';"
  grep -q '^CONTROLS-CA-77: PASS controls=4/4$' "$_sc/out-scope/controls-ca.txt" || \
    _fail="$_fail scope run: no 'CONTROLS-CA-77: PASS controls=4/4';"
  grep -q '^CONTROLS-C-77: FAIL controls=0/2$' "$_sc/out-bad/controls-c.txt" || \
    _fail="$_fail bad run: no 'CONTROLS-C-77: FAIL controls=0/2';"
  grep -q '^CONTROLS-CA-77: FAIL controls=0/4$' "$_sc/out-bad/controls-ca.txt" || \
    _fail="$_fail bad run: no 'CONTROLS-CA-77: FAIL controls=0/4';"
  grep -q '^# control verdict: FAIL' "$_sc/out-bad/controls-c.txt" || \
    _fail="$_fail bad run: no per-control FAIL verdict;"
  [ -s "$_sc/out-bad/controls-ca.txt" ] || _fail="$_fail bad run: no Ca receipt;"

  if [ -z "$_fail" ]; then
    printf 'SELFCHECK-77: PASS good=2+4 controls green (default --scratch-refusal=ca), scope=3+4 with C control 3 asserted, bad=6 violations caught (%s)\n' "$_sc"
    return 0
  fi
  printf 'SELFCHECK-77: FAIL —%s (%s)\n' "$_fail" "$_sc"
  return 1
}

# ---- main ------------------------------------------------------------------

HARNESS_SHA=$(sha256sum "$0" 2>/dev/null | cut -d' ' -f1)

if [ "$SELFTEST" = 1 ]; then
  mkdir -p "$SCRATCH" || die "cannot create scratch root $SCRATCH"
  selfcheck
  exit $?
fi

[ -n "$FREEZE" ] || { usage; exit 2; }
[ -n "$LANDS" ] || LANDS=$FREEZE
[ -n "$MAINPIN" ] || MAINPIN=$FREEZE
if [ -z "$COMBINED" ]; then
  if [ "$LANDS" = "$FREEZE" ]; then COMBINED=$FREEZE; else COMBINED=$LANDS; fi
fi
if [ -z "$OUT" ]; then OUT=$LANE/$TEL; fi
case $OUT in /*) ;; *) OUT=$LANE/$OUT ;; esac

ishex40() {
  case $1 in *[!0-9a-f]*|'') return 1 ;; esac
  [ ${#1} -eq 40 ]
}
ishex40 "$FREEZE" || die "--freeze must be 40 hex, got '$FREEZE'"
ishex40 "$LANDS" || die "--lands must be 40 hex, got '$LANDS'"
ishex40 "$BASE" || die "--base must be 40 hex, got '$BASE'"
ishex40 "$COMBINED" || die "--combined must be 40 hex, got '$COMBINED'"
ishex40 "$MAINPIN" || die "--main must be 40 hex, got '$MAINPIN'"
[ "$BASE" != "$FREEZE" ] || die "--base equals --freeze: control 2 would grade the do-nothing relation"

_top=$(git -C "$LANE" rev-parse --show-toplevel 2>/dev/null) || \
  die "$LANE is not a git worktree"
[ "$_top" = "$LANE" ] || die "$LANE is not a worktree toplevel (git says $_top)"

for _r in "$FREEZE" "$LANDS" "$BASE" "$COMBINED" "$MAINPIN"; do
  git -C "$LANE" cat-file -e "$_r^{commit}" 2>/dev/null || \
    die "revision $_r is not a commit in $LANE"
done
if [ "$LANDS" != "$FREEZE" ]; then
  git -C "$LANE" merge-base --is-ancestor "$FREEZE" "$LANDS" 2>/dev/null || \
    die "--lands $LANDS does not descend from --freeze $FREEZE (no legal ancestor relation)"
fi

# The frozen claim base is what control 2 refuses on: derive it when the caller
# passed none, and refuse a --base that disagrees with it.
_fb=$(git -C "$LANE" show "$FREEZE:reports/round-77/claims.json" 2>/dev/null | python3 -c '
import json, sys
try:
    d = json.load(sys.stdin)
except Exception:
    sys.exit(1)
print(d.get("base") or "")' 2>/dev/null) || _fb=
if [ -z "$BASE" ]; then
  [ -n "$_fb" ] || die "--base not given and $FREEZE:reports/round-77/claims.json carries no base"
  BASE=$_fb
elif [ -n "$_fb" ] && [ "$_fb" != "$BASE" ] && [ "$ALLOW_BASE_MISMATCH" = 0 ]; then
  die "--base $BASE is not the frozen claim base $_fb (control 2 would be unattributable; pass --allow-base-mismatch to record the divergence)"
fi

mkdir -p "$SCRATCH" "$SCRATCH/tmp" || die "cannot create scratch root $SCRATCH"
if [ "$PLAN" = 0 ]; then mkdir -p "$OUT" || die "cannot create receipt directory $OUT"; fi

if [ -n "$CDIR" ]; then _cdir=$CDIR; else _cdir=-; fi

if run_controls "$LANE" "$LANDS" "$FREEZE" "$BASE" "$MAINPIN" "$COMBINED" "$_cdir" "$OUT" round77; then
  printf 'CONTROLS-77: PASS (receipts in %s)\n' "$OUT"
  exit 0
fi
printf 'CONTROLS-77: FAIL (%s control violation(s); receipts in %s)\n' "$RUN_VIO" "$OUT"
exit 1
