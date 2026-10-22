VERDICT: claim O's counting command re-runs exactly as declared at both ends (exit 0 at `454a2dc`, exit 1 with the declared failures at base `f4015e7`), the criterion-11 controls receipt reproduces byte-identical, and the landing commit touches only `tools/check-gate-quotes.py`. No finding.

Checked items (sandbox clone `/fast/scratch/hyaku/kotodama-r55-falsify/RerunAcceptO/lane`, git checkout; no lane or fleet writes):

- `reports/round-55/accept-o.py` at `454a2dc813c8e4caa0b3811266bbf8864e7286f5` — CARRIED, exit 0. Output:
  ```
  DOUBLED PASS count=13 missing=[] extra=[]
  TRUNC PASS count=17 missing=[] extra=[]
  NOFALSE PASS stray=[]
  EXIT PASS round54=1 adversarial=1
  ESCAPE PASS missing=[] extra=[]
  KEEP53 PASS exit=1 lines=12 base=12 first_diff=none
  FORMAT PASS malformed_runs=[]
  SELFTEST PASS exit=0 SELFTEST: 24/24 pass
  ```
  All eight legs PASS; matches the claim's `after_required` ("all eight legs PASS (exit 0)", claims.json).
- `reports/round-55/accept-o.py` at base `f4015e70b829523ed81e14ce4279bfab0e0233e4` — CARRIED, exit 1. Output:
  ```
  DOUBLED FAIL count=0 missing=['S239', 'S240', 'S243', 'S246', 'S249', 'S259', 'S262', 'S265', 'S266', 'S267', 'S268', 'S275', 'S277'] extra=[]
  TRUNC FAIL count=0 missing=['S241', 'S242', 'S244', 'S248', 'S250', 'S251', 'S253', 'S255', 'S259', 'S263', 'S264', 'S265', 'S275', 'S276', 'S277', 'S278', 'S279'] extra=[]
  NOFALSE PASS stray=[]
  EXIT FAIL round54=0 adversarial=0
  ESCAPE FAIL missing=[('S901', 'words=26'), ('S902', 'words=26'), ('S904', 'words=22'), ('S905', 'words=26')] extra=[]
  KEEP53 PASS exit=1 lines=12 base=12 first_diff=none
  FORMAT PASS malformed_runs=[]
  SELFTEST PASS exit=0 SELFTEST: 12/12 pass
  ```
  Matches the declared `before`/`expected_pre_landing_counting`: DOUBLED count=0, TRUNC count=0, EXIT round54=0 adversarial=0, ESCAPE four missing; NOFALSE, KEEP53, FORMAT, SELFTEST (12/12) PASS.
- `python3 -B reports/round-55/criterion11-controls-o.py <clone> f4015e70b829523ed81e14ce4279bfab0e0233e4` — CARRIED, exit 0, 179 lines stdout, empty stderr, trailer `CONTROLS 16/16 as expected`. `diff -u` against `reports/round-55/telemetry/criterion11-controls-o.txt` is empty (diff exit 0): the recorded receipt is honest, including the BASE exit-1 block, GREEN exit 0, and all 15 red controls failing only their own leg.
- `git show 454a2dc813c8e4caa0b3811266bbf8864e7286f5` — CARRIED. `--name-status` shows exactly `M tools/check-gate-quotes.py` (193 insertions, 42 deletions); parent `d52c9dffbecdd957596521cc19783cc3fac12c20`; subject "round-55: claim O lands — tools/check-gate-quotes.py gains doubled-locator and registry-backed truncated-grounds classes, wrapped/guillemet/inter-span-ellipsis/star-row escapes, selftest 24/24". No other file touched, so the claim's `lands: [tools/check-gate-quotes.py]` holds.

Residual risk: this seat re-verified the acceptance harness and controls only. Whether the landed tool's rules generalise beyond the routed lines (review-only clause) and whether the `--selftest` 24/24 cases are themselves honest is the mutation-testers' scope (`MutateEscapes.md` and siblings report 4/4 kills). The sha256 pins inside accept-o.py were exercised indirectly (both runs exited as expected, so no pin mismatch), not by tampering a pinned file.

Unrun checks: pin-tamper negative run of accept-o.py (a corrupted fixture should exit 2; not required by the assignment and covered by accept-o.py's exit-2 contract only on paper). No tools installed; all pacman transactions paused per directive.
