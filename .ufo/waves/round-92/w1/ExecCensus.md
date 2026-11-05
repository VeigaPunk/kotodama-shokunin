# ExecCensus — round-92 w1 — registry and census receipt

Date: 2026-11-05. Seat: ExecCensus (leaf, no dispatch). Lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin. All git ops read-only. Scratch removed before yield.

## Files written
- .ufo/waves/round-92/w1/stage/ExecCensus/census-base.txt (8549 bytes) — every command verbatim + output
- .ufo/waves/round-92/w1/stage/ExecCensus/registry-baseline.txt (745 bytes) — row count + last id

## Numbers measured (all 2026-11-05)
- Fleet census: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` → rc 0, final line `ok /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md`, 33 warnings (28× W04 duplicate-url-across-scopes, 5× W01 tierC-mined). Warnings allowed; none blocking.
- Row count: 880 (expected 880 — MATCH), over base bytes via materialized tree.
- Malformed rows: 0 (expected 0 — MATCH).
- Duplicate ids: none (expected none — MATCH).
- Enum violations / tier inflation: none (expected none — MATCH).
- Tier histogram: `A=518 B=333 C=29` (sums 880).
- Status histogram: `mined=773 queued=58 rejected=49` (sums 880).
- Last id: S956 (expected S956 — MATCH); last three via the assigned grep: S954, S955, S956.
- Mined used-by existence (frozen CORPUS.md command 7 over the materialized base tree): no missing paths.

## Verification of bytes
- Base commit exists (cat-file -t → commit); base tree d91c6873d9ab4d19b2b22241b73e61daac411de7.
- `git show 21350361…:corpus/SOURCES.md | sha256sum` → 242fcd49085134a3be03ed3ef1195922b672f339592abecf436c1cf67af568b0; `git archive | tar -x` copy has the identical sha256.
- Working-tree corpus/SOURCES.md has the identical sha256 and `git status --porcelain -- corpus/SOURCES.md` is clean (HEAD 66b3ae93…), so the fleet census (working tree) and the manual census (base bytes) measured the same registry bytes.

## Findings
- None blocking. The 33 census warnings are pre-existing base-state warnings (cross-scope duplicate urls; tierC mined rows), visible in the W04/W01 output retained verbatim in census-base.txt.
- Claims.json and measure92.py read as instructed; both frozen files consistent with the measured base state (`before` in O: registry 880 rows, last id S956 — confirmed).

## Tools installed: none. Pacman: not used. Sysctls: untouched.
