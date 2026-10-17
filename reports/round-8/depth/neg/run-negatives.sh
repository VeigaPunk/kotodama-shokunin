#!/bin/sh
# R8-D12 negative controls for tools/d2-typed-labels.py.
#
# The integrated tool reads one packet (`--packet PATH`, default the live D2
# packet) through the strict loader of reports/round-8/depth/shard-parser.md
# §4.1. Each fixture below is a small typed-label packet carrying exactly one
# label-level syntax defect; the loader must refuse it with exit 2, a stable
# P-* diagnostic and no traceback.
#
# Contract checked per case: exit 2 on two runs, the expected P-* code in the
# --json document, the diagnostic on stdout, byte-identical output across the
# two runs, no traceback anywhere. The live packet is the positive control
# (exit 0 or 1, never 2). A repaired twin of each fixture is also run, as a
# note only: it proves the defect is what the loader refuses, and any later
# pipeline trouble on a minimal synthetic packet is reported, not hidden.
#
# Read-only with respect to the repository. Usage: sh run-negatives.sh
set -u

HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
REPO=$(CDPATH= cd -- "$HERE/../../../.." && pwd)
TOOL="$REPO/tools/d2-typed-labels.py"
PACKET="$REPO/examples/culture-d2/packet.d2.yml"

failures=0

say() { printf '%s\n' "$*"; }
fail() { failures=$((failures + 1)); say "FAIL $*"; }
sha() { sha256sum "$1" | cut -d' ' -f1; }

# A temp file under ${TMPDIR:-/tmp}, with a fallback to the user cache: the
# shared /tmp is inode-exhausted by the 64-worker wave (df -i /tmp: 100% on
# 2026-10-17) and a control must not fail because a sibling filled it.
make_tempfile() {
    for base in "${TMPDIR:-/tmp}" "${XDG_CACHE_HOME:-$HOME/.cache}"; do
        [ -d "$base" ] || continue
        candidate=$(mktemp "$base/r8d12-twin.XXXXXX" 2>/dev/null) || continue
        if printf 'probe\n' >"$candidate" 2>/dev/null; then
            printf '%s\n' "$candidate"
            return 0
        fi
        rm -f "$candidate" 2>/dev/null
    done
    return 1
}

say "R8-D12 negative controls — tools/d2-typed-labels.py (integrated --packet interface)"
say "date: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
say "tool: $TOOL"
say "tool sha256: $(sha "$TOOL")"
say ""

# ---- positive control: the live packet ------------------------------------
work=$(make_tempfile) || work=""
if [ -n "$work" ]; then
    python3 "$TOOL" --packet "$PACKET" >"$work.p" 2>"$work.pe"
    prc=$?
    if [ "$prc" -eq 2 ]; then
        fail "positive control: the live packet was refused (exit 2)"
    elif [ "$prc" -ne 0 ] && [ "$prc" -ne 1 ]; then
        fail "positive control: unexpected exit $prc"
    fi
    if grep -q "Traceback" "$work.p" "$work.pe"; then
        fail "positive control: a traceback was printed"
    fi
    say "positive control (live packet): exit $prc (want 0 or 1, never 2), traceback: none"
    rm -f "$work" "$work.p" "$work.pe"
else
    fail "positive control: no writable temp base"
fi
say ""

run_case() {
    case_name=$1
    fixture=$2
    code=$3
    needle=$4
    repair=$5

    work=$(make_tempfile) || {
        fail "$case_name: no writable temp base"
        return 1
    }
    say "== case $case_name =="
    say "fixture:        $fixture"
    say "fixture sha256: $(sha "$fixture")"
    say "expected:       $code, exit 2"

    for run in 1 2; do
        python3 "$TOOL" --packet "$fixture" >"$work.r$run" 2>"$work.e$run"
        eval "rc$run=\$?"
    done
    python3 "$TOOL" --json --packet "$fixture" >"$work.json" 2>"$work.je"
    json_rc=$?

    [ "$rc1" -eq 2 ] || fail "$case_name: run 1 exited $rc1 (want 2)"
    [ "$rc2" -eq 2 ] || fail "$case_name: run 2 exited $rc2 (want 2)"
    [ "$json_rc" -eq 2 ] || fail "$case_name: --json exited $json_rc (want 2)"
    if grep -q "Traceback" "$work.r1" "$work.e1" "$work.r2" "$work.e2" "$work.json" "$work.je"; then
        fail "$case_name: a traceback was printed"
    fi
    grep -qF -- "$needle" "$work.r1" || fail "$case_name: expected diagnostic id not found: $needle"
    grep -qF -- "\"$code\"" "$work.json" || fail "$case_name: --json does not carry $code"
    cmp -s "$work.r1" "$work.r2" || fail "$case_name: stdout is not stable across runs"
    cmp -s "$work.e1" "$work.e2" || fail "$case_name: stderr is not stable across runs"
    [ -s "$work.e1" ] && fail "$case_name: the refusal wrote to stderr (diagnostic belongs on stdout)"

    say "malformed run: exit $rc1 and $rc2 (want 2/2), --json exit $json_rc, traceback: none"
    say "stdout (byte-identical across both runs):"
    sed 's/^/  /' "$work.r1"
    say "json finding: $(cat "$work.json")"

    # repaired twin: informational only — shows whether the loader accepts the
    # packet once the defect is repaired (later pipeline defects on minimal
    # synthetic packets are a tool matter, reported here, not absorbed)
    twin=$(make_tempfile) || twin=""
    if [ -n "$twin" ]; then
        sed "$repair" "$fixture" >"$twin"
        python3 "$TOOL" --packet "$twin" >"$twin.out" 2>"$twin.err"
        trc=$?
        if [ "$trc" -eq 2 ] && grep -qF -- "\"$code\"" "$twin.out"; then
            fail "$case_name: repaired twin still refused with $code"
        elif grep -q "Traceback" "$twin.out" "$twin.err"; then
            say "repaired twin: exit $trc; the loader accepted it and a later pipeline step traced back (tool matter, noted):"
            tail -1 "$twin.err" | sed 's/^/  /'
        elif [ "$trc" -eq 2 ]; then
            twin_msg=$(head -1 "$twin.out"); [ -n "$twin_msg" ] || twin_msg=$(head -1 "$twin.err")
            say "repaired twin: exit 2 on a different diagnostic (tool state, noted): $twin_msg"
        else
            say "repaired twin: exit $trc; the loader accepted it (no $code)"
        fi
        rm -f "$twin" "$twin.out" "$twin.err"
    fi
    say ""
    rm -f "$work" "$work.r1" "$work.r2" "$work.e1" "$work.e2" "$work.json" "$work.je"
}

run_case "neg-12a-unterminated-label-window" \
    "$HERE/packet-12a.unterminated-label-window.yml" \
    "P-UNTERMINATED-FLOW" \
    "D2L-DATA" \
    "s/era_window: \[E0, E2$/era_window: [E0, E2]/"

run_case "neg-12b-anchor-in-label-text" \
    "$HERE/packet-12b.anchor-in-label-text.yml" \
    "P-ANCHOR-TAG" \
    "D2L-DATA" \
    "s/text: \*the-transit-coat/text: \"the transit coat\"/"

if [ "$failures" -eq 0 ]; then
    say "result: 2/2 negative controls refused with exit 2, stable P-* diagnostics, no tracebacks"
    exit 0
fi
say "result: $failures check(s) failed"
exit 1
