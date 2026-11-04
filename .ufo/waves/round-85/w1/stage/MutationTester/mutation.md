# Round 85 mutation probes

Axes: depth, operability, calibration. Scope: falsification only; no integration or scholarship verdict.

## Mechanism and limits

Frozen counter SHA-256: `f4611703c3b031a36fb8c3f2342be0659ee1d6840084022079e62d76195e2871`.
`measure85.py` and `claims.json` here were read with `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show ed816e71a97dde9b65f9265276b77c7583274671:<path>`.

No commits are permitted. The unchanged counter normally reads committed blobs, so uncommitted fixture bytes cannot be scored by its CLI. `probe.py` imports the exact frozen module and substitutes **only blob transport and path enumeration** for the designated fixture bytes. It does not change checks, constants, invocation, expected statuses, or frozen lint. This is a mutation-sensitivity experiment, **not committed-revision acceptance**. Counter stamp/tree lines in overlay receipts describe the backing freeze commit, not fixture contents. Fixture hashes identify the actual tested bytes.

D clean substrate is explicitly synthetic and deliberately meets structural predicates; it makes no source-authenticity, metallurgy, canon, etymology, diffusion, or caste claim. Real entry and new registry rows were absent at the observed pre-data HEAD. Structural passage does not certify historical truth; frozen claims explicitly reserve source-body judgment for review.

Reproduce D probes from the fleet root:

```sh
python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-85/w1/stage/MutationTester/probe.py
```

The driver creates its explicitly assigned scratch directory, invokes the same bounded detector on clean/mutated/restored bytes, saves full outputs, hashes, and unified diffs here, and removes scratch on normal exit. `results.json` binds before/mutant/after hashes and failed leg IDs. Each `.txt` carries all three counter runs; each `.diff` shows its one mutation.

## D outcomes

| Mutant | Expected detector | Clean / mutant / restored rc | Observed findings | Verdict |
|---|---|---|---|---|
| S919 source URL points to Bronze_Age rather than Metallurgy; URL/quote shape preserved | Source-identity review, not a frozen mechanical leg | 0 / 0 / 0 | All eight legs pass | **Survived**; review-only coverage boundary |
| First anchor S919 → unregistered S99999 | SOURCED | 0 / 1 / 0 | `unknown=['S99999']` | **Killed** |
| S921 registry row removed, citations retained | SOURCED, ROWS | 0 / 1 / 0 | `unknown=['S921']`; `bad=['S921']` | **Killed** |
| S919 URL scheme https → http | ROWS | 0 / 1 / 0 | `bad=['S919']` | **Killed** |

All D restorations are byte-exact, including source-adulteration survivor. Pristine entry SHA-256 `ace2f1d722a660948084cd9bf1692f21f6fef8161a05499021f837bda118d63c`; pristine SOURCES SHA-256 `da3ba874f9facf838e138896b80291a073576ded54255dec46ca1ccc288250f4`. Full mutant hashes reside in `results.json`.

The source-adulteration survivor does not authorize accepting Bronze_Age or changing frozen predicates. It demonstrates that an arbitrary HTTPS source with a located-looking quote is structurally sufficient; L1 must bind each real source URL and quotation independently.

## Actual frozen CLI pre-data controls

No overlay was used for these controls. `control-{base,freeze}-{D,O}.txt` records exact command, exit, and output.

- Base `0d181583b18ae94e80a251ca5ab5f3055b16c74c`: D exit 1, 0/8 legs; O exit 1, 0/3 legs. FROZENCFG also fails because claims did not yet exist at base.
- Freeze `ed816e71a97dde9b65f9265276b77c7583274671`: D exit 1, 1/8 legs; O exit 1, 1/3 legs. Only FROZENCFG passes.

These red pre-data runs are negative controls, never green baselines for mutant-kill claims.

## Boundary and tool record

Round-28 `reports/round-28/readme/sweep.py` already checks the index. This work never claims otherwise; successor behaviors under test are explicit root, duplicate failure, and last-footer selection.

No installs/upgrades, no commits or other mutating git/jj commands, no production or sibling writes. Rules read: workstation RULES.md, lane PROVINCE.md, and relevant corpus/QUALITY.md mutation/revision/citation requirements. Existing Python stdlib suffices.

## O outcomes and reproducibility

Candidate SHA-256: `8d57afd0801e9ea78b6f95ab48b80cc3bc08c2eff02a83a9496ff7dd51317b71`. Byte-exact retained copy: `candidate-tool.py`. Direct probes execute a copy in the assigned scratch, never the shared candidate. Its selftest exits 0 with `SELFTEST: PASS (23 checks)`; unchanged base index exits 1 with ten findings (`candidate-selftest.txt`, `candidate-base-index.txt`).

The clean 258-file README fixture `candidate-README.md` combines base README, two header repairs (myth 32 → 36; culture 41 → 42), and ExecIndexReading's literal reconciliation append. It contains no D entry. The overlay adds a synthetic SKILL gates section naming both paths solely to isolate tool behavior. It does not establish that production SKILL registration has landed.

Reproduce the full battery using retained inputs:

```sh
python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-85/w1/stage/MutationTester/probe.py \
  --candidate /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-85/w1/stage/MutationTester/candidate-tool.py \
  --readme /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-85/w1/stage/MutationTester/candidate-README.md
```

| Mutant | Detector | Clean / mutant / restored rc | Exact observed result | Verdict |
|---|---|---|---|---|
| Omit nonce README row, file retained | Candidate auditor | 0 / 1 / 0 | `files=1 rows=0 findings=1 ids=MISSING_ROW` | **Killed** |
| Duplicate nonce README row | Candidate auditor | 0 / 1 / 0 | `files=1 rows=2 findings=1 ids=DUPLICATE_ROW` | **Killed** |
| Last footer total 1 → 2 | Candidate auditor | 0 / 1 / 0 | `files=1 rows=1 findings=1 ids=FOOTER_TOTAL` | **Killed** |
| Tool replaced by always-clean stdout/exit-0 stub (claims 99 selftests) | Frozen O counter, transport-overlay mode | 0 / 1 / 0 | Clean 10/10; mutant 6/10 with MISSING, DUPLICATE, FOOTER, ERROR failing; restored 10/10 | **Killed** |

Every nonce baseline retains the stale **old** footer (999 files) while its last footer truthfully says one file. It exits 0 before each mutation and after restoration. Thus stale-old-footer tolerance is demonstrated positively, not inferred from a red mutant. Full commands, stdout and hashes: `O-{omitted-row,duplicate-row,last-footer}.json`; diffs have matching basenames. Canned-tool triple-run output: `O-canned-all-clean.txt`.

Nonce pristine/restored README SHA-256: `994089ce59c1d4f99777dea516bd8e383efc3dcccf632fdeea110efda88dd3b5`.
Omitted-row mutant: `b2d989858185128f063a9298035d14cb1200549ee501797c5686c1b522fe27cd`.
Duplicate-row mutant: `ada936bac31c156c60b2c5cc851150c1699d57f17632fbed0c404197cec2f4ce`.
Last-footer mutant: `d80ceab0b1260896f27a33b5ec00f38994b8abbfd8453d70343dad33464e5b96`.
Canned tool mutant: `3355fcf85a37b697cded91d2208db31426dfbf63e1c2f5bc62965dc38c183327`.
All before/after pairs match byte-exactly. No inconclusive cases in the executed battery: seven killed, one survived.

## Historical calibration correction

Frozen prose says round-28 selects the first footer. The **actual pinned base code selects the last matching footer already**: `footer_reading` builds `list(FOOTER_RE.finditer(text))` and reads `matches[-1]` (lines 113–118). `r28-footer-provenance.txt` records a read-only `git show` at base and source SHA-256 `7e0566ad1ae8ec2c5a0f10c62dc8de66abcc180ec3f7af560bceeba1601cad2b`. This does not rewrite frozen targets. Last-footer tests are valid behavioral checks, but not evidence that last-well-formed-footer selection was absent before. Candidate additionally refuses to skip a malformed final dated header, requires explicit root, and fails effective duplicate rows. No claim that an index checker did not exist.

## Handoff and self-evaluation

L1 should run the byte-exact frozen CLI at its eventual integrated revision for each claim; overlay receipts do not substitute for that. Independently review actual S919–S922 source identities and quotes, since D source adulteration survives shape checks. No policy or contract change requested by this survivor.

Self-evaluation: accuracy 4 (raw receipts and hashes; overlay explicitly limits revision authority); completeness 4 (all requested attacks covered, D substrate synthetic rather than final scholarship); clarity 4 (separates counter versus tool and actual versus overlay runs); actionability 4 (retained candidate/README/driver reproduce probes; final integration remains L1's); conciseness 4 (full raw receipts necessarily separate from summary). Overall 4.0. Highest-impact improvement is an actual committed-revision L1 run after integration, not a change to this frozen predicate. User should agree this is a bounded mutation result, not acceptance.
