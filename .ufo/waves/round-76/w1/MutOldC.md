# MutOldC — round-75 claim-C counter mutation probe

## Baseline
Command (run from clone root): `HYAKU_SCRATCH=/fast/scratch/hyaku/kotodama-r76/MutOldC python3 -B reports/round-75/accept-c.py --root . --lands 4f5e3b2535c2c06c51627dc2736c40183847cae1 --freeze 5d0167464309d8133991b30f7d7a7011a6a0fd14 --fleet-root /home/vgpnk/Projects/shokunin` (the successful run used the same command plus `--work /fast/scratch/hyaku/kotodama-r76/MutOldC/counter-work`). Raw verdict: `ACCEPT-C-75: PASS legs=13/13`, exit 0. Per-leg output was PASS for ENTRIES, ROWS, REPOINTED, GATE, EVIDENCE, REJECTS, GROUND, CITEDLINES, CENSUS, SCRATCHMIRROR, COLLCHECK, FROZENCFG, INDEX. Clone toplevel check: `git -C /fast/scratch/hyaku/kotodama-r76/MutOldC/clone rev-parse --show-toplevel` → `/fast/scratch/hyaku/kotodama-r76/MutOldC/clone` (equal to requested clone directory).

## Probes
Each mutant was made from clean lands `4f5e3b2535c2c06c51627dc2736c40183847cae1`, committed only inside the scratch clone, then graded with the same counter and frozen commit. `KILLED` means the counter returned FAIL; `SURVIVED` means PASS. Exact mutant diffs and full counter outputs are in `w1/stage/MutOldC/<name>.diff` and `<name>.output.txt`; `mutate.py` is the reproducible scratch driver.

| Leg | Mutant | Mutant commit | Raw counter verdict / failing legs | Result |
|---|---|---|---|---|
| ENTRIES | blank `verified-at` | c6f3e7732e02ba9e59ee4a4113316708ce330dde | `ACCEPT-C-75: FAIL legs=12/13`; `LEG FAIL ENTRIES` | KILLED |
| ENTRIES | truncate body below floor | 005eb87738cf4b4ea2bac620e2ff5d5de3c8435f | `ACCEPT-C-75: FAIL legs=12/13`; `LEG FAIL ENTRIES` | KILLED |
| ENTRIES | angle-bracket header value | de7d53ba1d3360ed169c8348f899243dfb53dc48 | `ACCEPT-C-75: FAIL legs=11/13`; `LEG FAIL ENTRIES`, `LEG FAIL INDEX` | KILLED |
| ROWS | empty S885 used-by | b329935f12eb5d0b83058886f0de63b7a9934f5a | `ACCEPT-C-75: FAIL legs=12/13`; `LEG FAIL ROWS` | KILLED |
| ROWS | append S999 row | a06742fd83681c0c07a4a35b68379085e8e7f538 | `ACCEPT-C-75: FAIL legs=11/13`; `LEG FAIL ROWS`, `LEG FAIL CENSUS` | KILLED |
| ROWS | S885 recheck prose | d6cbf784d5e36876dfa935eb56fa8c5ad7c7937e | `ACCEPT-C-75: FAIL legs=11/13`; `LEG FAIL ROWS`, `LEG FAIL CENSUS` | KILLED |
| GATE | replace quoted phrase | 33cbd63d62cd429b1a8d10cc0c3c3451a47e5aae | `ACCEPT-C-75: FAIL legs=12/13`; `LEG FAIL GATE` | KILLED |
| GATE | overlong quote | eeebeaabdfc9a13817e6ae135c71da82ca2e2d63 | `ACCEPT-C-75: FAIL legs=12/13`; `LEG FAIL GATE` | KILLED |
| GATE | alter S893 row id (reject row) | 150747ad1d5bb48e9c25936ff853580a4753833d | `ACCEPT-C-75: PASS legs=13/13` | SURVIVED |
| EVIDENCE | flip window SHA byte | 6cb317101255edf6e498cf18dcfc26ccca9ebfe3 | `ACCEPT-C-75: FAIL legs=12/13`; `LEG FAIL EVIDENCE` | KILLED |
| EVIDENCE | replace evidence quote | 54dfe31e0286aa182d055062c903f611c96b5b94 | `ACCEPT-C-75: FAIL legs=12/13`; `LEG FAIL ROWS` | KILLED, but not on expected EVIDENCE leg |
| EVIDENCE | change declared window length only | d8be87bc795c03d85215bb0a0bbe8167de21c05a | `ACCEPT-C-75: PASS legs=13/13` | SURVIVED |
| INDEX | paraphrase entry topic | 8c0712a0ca46e0b3c91a3d7bdf92426c5dfa88cb | `ACCEPT-C-75: FAIL legs=12/13`; `LEG FAIL INDEX` | KILLED |
| INDEX | footer total wrong | 8a1bbaeae19046af0045f8f97d73830ec66df22e | `ACCEPT-C-75: FAIL legs=12/13`; `LEG FAIL INDEX` | KILLED |
| INDEX | remove adopted index row | bb2fe687ce3997d4b4178348b761fa1137995cf0 | `ACCEPT-C-75: FAIL legs=12/13`; `LEG FAIL INDEX` | KILLED |

## Surviving coverage findings
- GATE: changing the S893 reject-row identifier to S893X survived. The counter did not enforce that this rejection row retained the frozen row identity / assimilation membership. Evidence: staged output `gate_reject.output.txt` contains `ACCEPT-C-75: PASS legs=13/13`.
- EVIDENCE: changing only the evidence record's declared `window: chars=3720` to `3000` survived. The digest-checked actual window remained unchanged; the detector did not bind this descriptive length field to the stored window. Evidence: `evidence_window_short.output.txt` contains `ACCEPT-C-75: PASS legs=13/13`.
- Evidence-quote probe was killed by ROWS, not EVIDENCE; it is not evidence of EVIDENCE coverage. The row probe was designed by changing the evidence quote string, which also changed the row quote binding.

## Hash/restoration evidence
Pristine-to-mutated-to-restored SHA-256 values are printed in each row of the driver output (recorded in the session output): ENTRIES `3ea4d6f80715460423fada252499dac9a95010a3bb4dd292c7ea834eab78fc13` restored after every mutant; SOURCES `c1f9f1e06a82de775175f89c7674a0aec677ecc45b0c1cc262c5463a9e01c477`; lesson `d110e42ba7a2aa87902df94eb69932d22dd23ae8ba4729022205cab5ec989805`; S885 evidence `9aa7e8fcf1387c57acee23c647e26267ce38cd7a31353aad9ec4b54330408321`; README `c434e78cd42f1475d8f90df3d3857af8899be4dc5a08735324881dd222ecc5f3`. For every completed mutant the driver printed `RESTORED=True`, meaning restored file hash equaled pristine and clone status was empty. Final clone HEAD command `git -C /fast/scratch/hyaku/kotodama-r76/MutOldC/clone rev-parse HEAD` output `4f5e3b2535c2c06c51627dc2736c40183847cae1`.

Probe commands were executed with `python3 -B /fast/scratch/hyaku/kotodama-r76/MutOldC/mutate.py`; its per-mutant counter command is recorded in the script and outputs copied beside each diff. No lane counter, frozen claim or production file was edited. No tools installed.