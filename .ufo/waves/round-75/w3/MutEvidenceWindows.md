# MutEvidenceWindows — round 75 wave 3

Verdict: **PARTIAL** (the requested mutation and live-body probes were not completed; no claim of a full pass/fail result).

Scratch clone checked out exactly `4f5e3b2535c2c06c51627dc2736c40183847cae1` at `/fast/scratch/hyaku/kotodama-r75/MutEvidenceWindows/lane`. Pristine `capture-evidence.py --verify` succeeded for all nine files. Each output reported `quote-in-window=yes`, HTTP 200, access-date 2026-10-27. Thus the verifier's own NFKC+whitespace quote check passed for all nine stored windows.

| Evidence | Stored bytes / SHA256 | Pristine verify |
|---|---:|---|
| S885 | 109588 / 20b571d7a6a9bc3835b1406079adeea4279dc2bc4c5e7134c1ce31dbf25de034 | PASS; window 3720 chars |
| S886 | Not independently recorded here | PASS; window 3526 chars |
| S887 | Not independently recorded here | PASS; window 3073 chars |
| S888 | Not independently recorded here | PASS; window 4096 chars |
| S889 | Not independently recorded here | PASS; window 4098 chars |
| S890 | Not independently recorded here | PASS; window 4098 chars |
| S891 | Not independently recorded here | PASS; window 2169 chars |
| S892 | Not independently recorded here | PASS; window 4097 chars |
| S893 | Not independently recorded here | PASS; window 4103 chars |

Code inspection confirms `verify_file` rejects a changed window without matching `window-sha256`, non-200 `http-status`, excerpt windows under the minimum, and whole-document windows whose `visible-chars` is >= minimum or mismatches window length. It checks the stored quote using whole-string NFKC plus whitespace collapse. However, the assigned mutation matrix (including recomputed-hash residual, UA mutation, truncation, and whole-document mutation), accept-c detector runs for those cases, live re-fetch/hash comparison, and restoration-hash evidence were not performed. Consequently no live-movement result is asserted. S885's stored source metadata is documented above; it is not a comparison against today's body.

The scratch clone/bytes were left untouched after the pristine verification; no mutation was applied. No tools were installed.