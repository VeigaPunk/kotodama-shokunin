# ExecGraderV6 — round-95 Claim O grader v6 candidate

Candidate: `stage/v6-candidate.py`, sha256 `f7981ba2881bff2a49a5c603436caefb90f416e6d6843e8e9cd6a63813ac1fec` (v5: `7957945db8036f52ab46436b281e92887c6fc22d0a89531d6f80279bcbad01ff`).

## Changed criteria (summary)

- Verdict-token refusals (rc 2, no traceback):
  - CD1 combining mark (Mn, e.g. U+0301): `VERDICT-COMBINE`
  - LR1 U+200E LRM (Cf outside strip set): `VERDICT-FORMAT`
  - TAB1 tab inside verdict token: `VERDICT-TAB`
- Id-token refusal:
  - ID1 small-cap letters (e.g. U+A731 for S): `ID-NONASCII`
- Heading anchors: numbering stripped from every position (nested `1.1`, roman `I.`, second-token `Notes 1)`); headings with <2 content tokens anchor nothing; refusal via `LEG FAIL TOPIC`.

## Receipts

- `stage/selftest.txt`: `SELFTEST PASS 134/134` (134 `ok` lines), plus a concurrent rerun in scratch also `PASS 134/134`, rc 0.
- `stage/battery.txt`: `BATTERY-SUMMARY survivors=0 unnamed=0 refused=14` (14 `CLASS` lines all `traceback=no outcome=REFUSED`); full output retained for read-only reference.
- `stage/reg-candidate.txt` vs `stage/ExecBattery95/reg-v5.txt`: `diff` empty (rc 0); `stage/reg-diff.txt` empty.
- Head-qualify-off mutant (local scratch only): selftest FAIL 133/134 rc 1, killed.

## Disposition-scanner region

The fallback line targeted by round-94 `dispo-fallback-off` is unchanged byte-for-byte at line 253:
`        m = DISPO_ANY_RE.search(plain)` (8-space indent, inside `_dispo_match`).
Changes in that region: only `dispositions()` now calls `_refuse_disguised(n, stripped)` after a successful match in addition to the previously invisible-line call; `_refuse_disguised` was widened with NFKD-minus-Mn recovery (`VERDICT-COMBINE`), out-of-set Cf recovery (`VERDICT-FORMAT`), tab-inside-token (`VERDICT-TAB`), small-cap id folding (`ID-NONASCII`), and tightened lowercase/non-ASCII guards (`not _dispo_match(plain)`) so clean lines are unaffected. Heading region changes (`_content_toks` + `head_span_anchors` only; `head_anchors` byte-identical to v5) are enumerated in the code comments.

## Tooling

Installed or upgraded: none.
