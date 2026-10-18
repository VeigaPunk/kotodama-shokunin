# R20-A09 — handoff v3 adversarial pass: D2+D3+D4 assembly, uncertainty grammar, resolving links (NON-CANON)

- seat: R20-A09 (handoff auditor, of R20-A09..A12). Lane:
  `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
- assignment (verbatim, my batch): *"AUDIT R20-A09..A12 (entry+handoff auditors x4):
  v3 packet adversarial pass; README-vs-files diff independent re-derivation;
  alias-wart negative re-runs; frozen replay audits."* This file is the first leg.
- date: 2026-10-18 (lane-local UTC−03:00; stamps UTC). Declared baseline
  `caf1beac…`; HEAD `122086b`. **The v3 tool was being written under this audit**:
  `tools/exercise-handoff-e2e.py` moved 1834 → 770 → 1556 → 2150 → 3318 → 3317
  lines between 13:07Z and 13:27Z. Readings below are stamped; none is a clearance.
- role limits: this seat audits and reports. Writes: this file plus gitignored
  scratch (`/tmp/kotodama-r20-audit/` receipts and a self-frozen baseline; no
  repo file). It edits no tool, freezes no committed baseline, admits no claim.
- claim D (`reports/round-20/claims.json`): v3 assembles from D2+D3+D4; D4 claims
  enter the ledger with uncertainty `{status, basis}` (grounding/restriction/open
  grammar); claim-to-record links resolve into culture-d4 records;
  `handoff-packet-check` 16/16 + 20/20; contract-v2 audit re-run pass-with-named-gaps
  or better; v2 paths unchanged and green.

## 1. Verdict at my stamp (13:22–13:27Z)

**Reproducible, with two caveats.** Against a baseline I froze myself from the
live tool (`.scratch`-style scratch at `/tmp/kotodama-r20-audit/v3b/`), the v3
exercise passes end to end: exit 0, `fields=16/16 glossary=20/20 findings=0
links=61/61`, packet sha256 `6de822f4ed8c7269…`, twin sha256
`b3e2bad74dbefd07…`. The claim's substance is therefore reproducible at that
revision. Caveats: (1) the **committed v3 baseline
`reports/round-20/handoff/expected.json` was not yet filed** at my stamp, so a
plain run exits 2 `E2E-BASELINE`; my pass uses my own frozen copy, which is a
control, not the lane's baseline. (2) The tool's **own `--selftest` currently
fails one control** (§4.2). Both are mid-wave states; the wave was still moving
when this file was written.

## 2. The passing run (13:23Z, against my scratch baseline)

```
OK   input-digest: 42 read-set digests match the frozen baseline
OK   preflight: 16 fields supplied, non-canon marker present, glossary vocabulary licensed,
     24 claim rows carry the uncertainty grammar and manifest-resolvable links, 48 edges name claims
OK   cross-references: contract §4 names = gate FIELD_NAMES = supplied fields; contract digest
     measured; 25/25 component digests matched; 8/8 d4 tree pins matched; manifest digests equal
     bytes for 42 files
OK   gate-exit: tools/gates/handoff-packet-check.py exit 0 (expected 0) over the isolated copy
OK   gate-scan: fields=16/16 glossary-entries=20 findings=0
OK   semantic-uncertainty: tools/harness/packet_uncertainty.py exit 0 over 24 claims (require-oq); findings 0
OK   semantic-links: tools/harness/packet_links.py exit 0; 61/61 links resolved against live bytes; findings 0
OK   frozen-packet / frozen-twin / frozen-claims (24) / frozen-glossary (20)
OK   preservation: the 42 read-set files are byte-identical before and after the run
handoff-e2e: exit=0 fields=16/16 glossary=20/20 findings=0 links=61/61 packet_sha256=6de822f4ed8c7269…
```

The freeze receipt (`/tmp/kotodama-r20-audit/v3b/freeze.txt`) records the same
scan plus `read set: 42 files; component digests 25/25; d4 pins 8/8` and
`semantics: uncertainty exit 0, links 61/61 resolved`. The read set is 21 v1
files (unchanged, A-01..A-21) plus the D4 tree rows A-22..A-24
(`packet.d4.yml` e7ecd204…, `packet.d4.typed.yml` e823db67…, the regenerated
`typed-labels.d4.yml` cbcf997f…) and the two harness validators — the claim's
"D4 artifacts enter the read set" is on the record.

## 3. Independent re-derivations (this seat, not the tool's own output)

- **Harness validators, run by this seat over the assembled twin**
  (`tools/harness/packet_uncertainty.py --packet twin.json --require-oq --json`):
  `claims 24, findings []`, exit 0.
  `tools/harness/packet_links.py --packet twin.json --json`:
  `links_checked 61, resolved 61, findings []`, exit 0.
- **Twin census, parsed by this seat** (`twin.json`, the machine form):
  24 claims; uncertainty statuses `supported 14 / partial 7 / unresolved 3`;
  **grammar violations 0** — every basis carries `grounding:`; every `partial`
  carries `restriction:`; every `unresolved` carries `open:` and `owner:`;
  **9 D4 claim rows** (`D4-CL01`..`D4-CL09`) and **25 claim links naming
  D4 artifacts** (A-22/A-23/A-24 or `culture-d4` paths) — the claim's "nine new
  D4 claim rows … links resolve into culture-d4 records" is re-derived.
- **D4 grounding spot-check**: `D4-CL01`'s links name
  `examples/culture-d4/packet.d4.yml#SYM-01; …#SYM-08` and the projection
  artifact id, and the manifest rows carry measured digests for those paths —
  the link validator's 61/61 over live bytes is the resolution evidence.
- **v2 path control**: the v2 baseline successor is filed as a **new** row
  (`reports/round-20/wart/expected-v2-07-r20.json`; its input table pins the
  unchanged D2 projection `a3aa452c…`). The round-15 `frozen-verify.py` over the
  *old* baseline reports `V2F-DIGEST: 2 pinned file(s) changed since the freeze:
  tools/d2-typed-labels.py, tools/harness/packet_links.py` — the projector is
  the expected round-20 O change; `packet_links.py` last moved in round 16
  (`f30b6f8`), i.e. the old baseline's pin was already stale pre-round-20. This
  seat did not re-derive the v2 *semantic* audit; the successor row is the
  lane's carry, and the v3 run itself exercises the same two validators green.

## 4. Defects and negatives observed (all stamped; the tool was moving)

1. **Mid-window crash (fixed within the window).** At 13:14Z `--freeze` and
   `--selftest` both died with `KeyError: 'findings_hold_or_fail'` at
   `tools/exercise-handoff-e2e.py:1419` (`open_question_rows`), while the same
   structure is read as `hold_or_fail` at lines 1174/1186. By 13:22Z the freeze
   path completed. Recorded because a reader of the 13:14Z tree would have seen
   a hard failure.
2. **The tool's own selftest fails one control at my stamp.**
   `python3 tools/exercise-handoff-e2e.py --selftest` → exit 1,
   `AssertionError: []` at the control labelled *"malformed-12 link to a
   non-manifest artifact id: preflight exits E2E-LINK"* (`:3147`): the control
   mutates a claim link to `A-99#SYM-01` and asserts preflight raises
   `E2E-LINK`; preflight returned no problems. Either the mutation anchor no
   longer matches the built packet (silent no-op) or the preflight check no
   longer fires. **Routed to the parent/D seat** — the tool is not
   self-consistent until this control is green again.
3. **Transient empty `--json` receipt.** One passing `--json` run at 13:22Z
   wrote an empty stdout (exit 0); an immediate re-run printed the full report.
   Classed as a mid-write artefact, recorded for the record.
4. **Earlier in the window (12:5x–13:05Z)** the plain run exited 2
   `E2E-BASELINE` (baseline absent) and `--freeze` crashed (§4.1) — the
   pre-conditions under which this audit's early readings were taken.

## 5. Not verified by this seat

- The committed v3 baseline and the D seat's own `audit-v3.md` verdicts were
  not re-derived (the former did not exist at my stamp; the latter is the D
  seat's evidence, read but not re-run).
- The "contract-v2 audit re-run yields pass-with-named-gaps or better" clause:
  this seat verified the mechanical contract checks the run performs
  (three-way field agreement, digest equality, claim kinds, preservation) but
  did not re-adjudicate the contract-v2 audit document's named gaps.
- Reproducibility across revisions: the tool changed under the audit; my
  passing run is bound to the revision that produced packet `6de822f4…`
  (tool mtime 13:2xZ). A re-run after the wave settles is the clean control.

## 6. Commands (all 2026-10-18; lane root; `TMPDIR=$PWD/.scratch`)

```sh
# freeze a scratch baseline from the live tool (no repo writes)
python3 tools/exercise-handoff-e2e.py --freeze /tmp/kotodama-r20-audit/v3b \
    --keep /tmp/kotodama-r20-audit/kept2
# pass against the scratch baseline
python3 tools/exercise-handoff-e2e.py --baseline /tmp/kotodama-r20-audit/v3b/expected.json
# this seat's independent harness runs
python3 tools/harness/packet_uncertainty.py --packet /tmp/kotodama-r20-audit/v3b/twin.json --require-oq --json
python3 tools/harness/packet_links.py --packet /tmp/kotodama-r20-audit/v3b/twin.json --json
# control matrix (red at this stamp, §4.2)
python3 tools/exercise-handoff-e2e.py --selftest
# v2 pin control
python3 reports/round-15/handoff/frozen-verify.py        # V2F-DIGEST: 2 pins drifted (expected/known)
```

## 7. Final addendum (13:33Z) — the caveats of §1 closed inside the window

After this file's first write, the D seat filed the committed baseline and
fixed the control:

- `reports/round-20/handoff/expected.json` (+ `packet.md`, `twin.json`,
  `freeze.txt`, `run.log`) is now filed; the plain official run
  `python3 tools/exercise-handoff-e2e.py` reads **exit 0**, `fields=16/16
  glossary=20/20 findings=0 links=61/61 packet_sha256=6de822f4ed8c7269…` — the
  same packet my scratch freeze produced, so §2's pass is now confirmed against
  the committed baseline, not only my own.
- `python3 tools/exercise-handoff-e2e.py --selftest` now reads **exit 0**; the
  §4.2 `malformed-12` control failure is closed at this stamp.
- §4.1 (the KeyError) and §4.3 (empty `--json`) remain on the record as
  mid-window states; both are absent in the final readings.

