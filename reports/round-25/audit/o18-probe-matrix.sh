#!/bin/sh
# R25-O18..O20 adversarial probe matrix (self-contained, read-only over the repo).
#
# Run from the lane root:
#   export TMPDIR=$PWD/.scratch && sh reports/round-25/audit/o18-probe-matrix.sh
#
# Builds every mutation it needs under $TMPDIR/o18-probe/ from the committed
# packets; writes nothing else and edits no repo byte. The typed gate is graded
# from its live bytes, so the matrix is a statement about the current revision —
# record `sha256sum tools/gates/typed-pipeline-gate.py` alongside the output.
set -u
G=tools/gates/typed-pipeline-gate.py
D4=examples/culture-d4/packet.d4.typed.yml
D4SRC=examples/culture-d4/packet.d4.yml
D2=examples/culture-d2/packet.d2.typed.yml
D2SRC=examples/culture-d2/packet.d2.yml
WORK="${TMPDIR:-.scratch}/o18-probe"
mkdir -p "$WORK"

python3 - "$WORK" "$D4" "$D4SRC" "$D2" "$D2SRC" <<'PY'
import hashlib, sys
from pathlib import Path
work, d4, d4src, d2, d2src = (Path(p) for p in sys.argv[1:6])
t = d4.read_bytes()
d2b = d2.read_bytes()

# B1 — filename is irrelevant: the gate keys on content, not the `.typed.` name
(work / "renamed-no-dot-typed.yml").write_bytes(t)
# B4 — the typed_channel block stripped: no longer typed input
(work / "stripped.yml").write_bytes(t[: t.index(b"typed_channel:")])
# X1 — a declared source that does not exist
(work / "absent-source.yml").write_bytes(t.replace(
    b'  packet: "examples/culture-d4/packet.d4.yml"',
    b'  packet: "examples/culture-d4/NOPE-absent.yml"', 1))
# X2 — a self-referential declared source (typed packet declares itself)
h = hashlib.sha256(t).hexdigest().encode()
(work / "selfref.yml").write_bytes(t.replace(
    b'  packet: "examples/culture-d4/packet.d4.yml"',
    b'  packet: "%s"\n  packet_sha256: "%s"' % (d4.as_posix().encode(), h), 1))
# X3 — a cross-family declared source (D4 typed packet declares the D2 source)
h2 = hashlib.sha256(d2src.read_bytes()).hexdigest().encode()
(work / "cross-family-source.yml").write_bytes(t.replace(
    b'  packet_sha256: "e7ecd2045ef0e5f9823ce0a067d21b8221b2ceb5e8f5799736981a1c88fa50d3"',
    b'  packet: "%s"\n  packet_sha256: "%s"' % (d2src.as_posix().encode(), h2), 1))
# N1 — a real defect: the field never moved while the routing still claims it
(work / "unmoved-field.yml").write_bytes(t.replace(b'    garment_gloss: "', b'    garment: "', 1))
# R1 / R1b — a hold nulled on one moved row, and on all of them
(work / "hold-null.yml").write_bytes(t.replace(
    b'    hold: "D2L-FORM-UNRESOLVED"\n    owed_slot: "LEX-GAR-01"',
    b'    hold: null\n    owed_slot: "LEX-GAR-01"', 1))
(work / "hold-null-all.yml").write_bytes(
    t.replace(b'    hold: "D2L-FORM-UNRESOLVED"\n', b'    hold: null\n'))
# R2 — the hold key absent on one moved row
(work / "hold-absent.yml").write_bytes(t.replace(
    b'    hold: "D2L-FORM-UNRESOLVED"\n    owed_slot: "LEX-GAR-02"',
    b'    owed_slot: "LEX-GAR-02"', 1))
# R2b — the same hole on the D2 typed packet (family-general check)
(work / "d2-hold-null.yml").write_bytes(d2b.replace(
    b'    hold: "D2L-FORM-UNRESOLVED"\n    owed_slot: "LEX-GAR-02"',
    b'    hold: null\n    owed_slot: "LEX-GAR-02"', 1))
print("inputs built under %s" % work)
PY

run() {
  printf '%s ' "$1"
  o=$(timeout 120 python3 "$G" "$2" 2>&1); e=$?
  tb=$(printf '%s' "$o" | grep -c Traceback)
  printf 'exit=%s traceback=%s :: %s\n' "$e" "$tb" \
    "$(printf '%s' "$o" | grep -E '^(FAIL|summary|NameError|KeyError|FileNotFound)' \
       | tail -1 | cut -c1-140)"
}

echo "gate: $G"
sha256sum "$G" | cut -c1-24
echo
run "source-packet            " "$D4SRC"
run "typed-packet             " "$D4"
run "d2-typed-packet          " "$D2"
run "renamed-typed-copy       " "$WORK/renamed-no-dot-typed.yml"
run "typed_channel-stripped   " "$WORK/stripped.yml"
run "absent-declared-source   " "$WORK/absent-source.yml"
run "selfref-declared-source  " "$WORK/selfref.yml"
run "cross-family-source      " "$WORK/cross-family-source.yml"
run "unmoved-field            " "$WORK/unmoved-field.yml"
run "hold-null-single-row     " "$WORK/hold-null.yml"
run "hold-null-all-rows       " "$WORK/hold-null-all.yml"
run "hold-key-absent-row      " "$WORK/hold-absent.yml"
run "d2-hold-null-row         " "$WORK/d2-hold-null.yml"
