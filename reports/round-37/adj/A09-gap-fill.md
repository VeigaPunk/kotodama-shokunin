- Seat: A09 | executor | claim A | date 2026-10-19 | baseline 57c8409

# A09 — gap-fill: D3 snapshot invalidation follow-up

**Disposition: reproduced, carry forward; not fixed.** This gap-fill rechecks the existing round-35 A03-F1 / assembled-audit F12 finding about the D3 computational snapshot. It is separate from A01's r7 D4 read-set asymmetry, does not re-scan the eleven corpus entries, and does not by itself verify claim A (`reports/round-37/claims.json:25-30`; `reports/round-37/targets.json:49-57`).

## Recheck

At `HEAD=57c8409` (`git rev-parse --short HEAD`), with `TMPDIR=$PWD/.scratch` and `PYTHONDONTWRITEBYTECODE=1`, the read-only frozen check returned:

```text
$ python3 -B tools/check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json
{"counts": {"D3-SNAPSHOT": 1, "total": 1}, "exit": 2,
 "findings": [{"id": "D3-SNAPSHOT",
   "message": "manifest digest mismatch for 'examples/handoff-packet.sample.md': declared 4e24bd3b887cf148155d89855d3c9eb842d3e325a4fa4302fccaa6c9d23dd712, actual adfd7895461af85275d0170f7a2e057e0c5265ab2bc0ebadc298d2bae7766dc9",
   "record_id": "-"}]}
frozen_check_exit=2
```

The unfrozen counterpart, `python3 -B tools/check-evidence-coupling.py examples/culture-d3/packet.json`, returned `{"counts": {"total": 0}, "exit": 0, "findings": []}` (`unfrozen_check_exit=0`). `sha256sum` independently returned `adfd7895461af85275d0170f7a2e057e0c5265ab2bc0ebadc298d2bae7766dc9` for the current sample and `562b76cb48f14bdb7bcf6362f78d8b5c5506934a10d9f912f6c4a0a554bf90fc` for `expected.json`; the manifest's declared sample digest remains the `4e24bd3b…` value at `expected.json:16`. The manifest says later input edits invalidate the snapshot before verdict (`expected.json:33`).

This independently reproduces the prior finding: the round-35 evidence records a pre-r33 isolated baseline exit 0 and current frozen exit 2, identifies the sample digest change as the cause, and says the invalidation signal is expected but its record/re-acknowledgement is missing (`reports/round-35/adj/A03-examples.md:75-129`). The assembled audit carries it as F12 and routes it to the round-33 repoint author / integrator, with record-only as the minimal remedy; it also records that editing `expected.json` would invalidate r6/r7 pins (`reports/round-35/adj/audit-assembled.md:280-293`). This result is not evidence of a new cross-domain bleed or of a defect in the D4 r7 freeze pair.

No example, manifest, frozen packet, or filed-round byte was changed. No `reports/round-*/run-validation.py` was run.

## Owed

- Integrator: carry F12 into the round-37 assembled adjacency audit with its existing owner and record-only disposition (or file a separately evidenced remedy decision). The observed frozen check remains red; do not label this surface green without recording the invalidation. A09 does not adjudicate A01's D4 question or satisfy A02-A04.

## Citations

- Claim-A scope and required surfaces: `reports/round-37/claims.json:25-30`; A09 assignment and output: `reports/round-37/targets.json:57`.
- Frozen manifest member, coverage, invalidation limit: `examples/culture-d3/expected.json:16,32-33`.
- Prior baseline/current comparison and cause: `reports/round-35/adj/A03-examples.md:75-129`.
- Existing F12 ownership, remedy, and pin cascade: `reports/round-35/adj/audit-assembled.md:280-293`.
- Current command outputs: frozen check exit 2 with exactly one `D3-SNAPSHOT` digest mismatch; unfrozen check exit 0 with zero findings; `sha256sum examples/handoff-packet.sample.md examples/culture-d3/expected.json` → `adfd7895461af85275d0170f7a2e057e0c5265ab2bc0ebadc298d2bae7766dc9` and `562b76cb48f14bdb7bcf6362f78d8b5c5506934a10d9f912f6c4a0a554bf90fc`; `git rev-parse --short HEAD` → `57c8409`.
