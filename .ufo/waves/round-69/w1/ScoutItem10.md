# ScoutItem10 — round-69 w1 — read-only re-derivation of the shokuknow absent-defect register, kotodama slice

Seat: ScoutItem10 (leaf, no dispatch). Date: 2026-10-24. Read-only: nothing was
executed inside `/home/vgpnk/Projects/shokuknow/`; no corpus bytes were
appended, renumbered or adopted in any repo; the only file this seat wrote is
this report. No network fetches were made; no tools were installed.

## Inputs (all read from disk)

- Register: `/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md`
  — 375 lines, sha256
  `5afe1810a6c3d62f37987b575a954f5b1197daa23005d4bb2f1d982f64bad833`.
- Verdict source: `corpus/lessons/round-68.md` `## Quarantine` (lines 100–117),
  whose recipe line 102 is the awk one-liner reproduced below.
- Raw round-68 evidence (read for the cross-check, not modified):
  `.ufo/waves/round-68/assimilation/quarantine-slice` (21 lines),
  `quarantine-handcheck.json` (18 entries), `quarantine-pdf-pass.json` (5 PDF hits).
- The shokuknow addendum (`RECOVERY-RULES.md`, "An addendum to every lane brief
  in this wave") owns request budgets, not the recipe; the recipe's canonical
  in-lane quote is `corpus/lessons/round-68.md:102`.

## Re-derivation — the recipe, verbatim, run from /tmp (cwd outside shokuknow)

```
cd /tmp && awk -F'|' -v l=kotodama '$2 ~ ("`" l "`") && $3 ~ /round[0-9]+/ && $4 ~ /S[0-9]+/ {print NR": "$2" "$3" "$4}' \
  /home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md
```

Real output (21 matching lines):

```
118:  `kotodama`   round1   S776 
119:  `kotodama`   round1   S778 
120:  `kotodama`   round1   S779 
121:  `kotodama`   round1   S786 
122:  `kotodama`   round1   S787 
123:  `kotodama`   round2   S791 
124:  `kotodama`   round2   S792 
125:  `kotodama`   round2   S795 
126:  `kotodama`   round2   S796 
127:  `kotodama`   round3   S804 
128:  `kotodama`   round4   S814 
129:  `kotodama`   round4   S816 
130:  `kotodama`   round4   S817 
131:  `kotodama`   round4   S820 
132:  `kotodama`   round5   S823 
133:  `kotodama`   round5   S824 
134:  `kotodama`   round5   S825 
135:  `kotodama`   round5   S827 
333:  `kotodama`   round3   S807` 
334:  `kotodama`   round3   S812` 
335:  `kotodama`   round6   S835` 
```

Row count: **21** (18 `payload-absent` rows in the register's Rows table at
lines 118–135 + 3 never-checked rows at lines 333–335). The three never-checked
ids carry a trailing backtick in the register's id cell (`S807`` `) — a
register formatting defect — but the recipe's `$4 ~ /S[0-9]+/` still matches
them, so the slice is complete without a second pass.

The id set and order match the round-68 artifact
`.ufo/waves/round-68/assimilation/quarantine-slice` line for line (21 ids).

## Comparison with the round-68 verdict list

Verdict ids extracted mechanically from `corpus/lessons/round-68.md` lines
111–114 (present / refused / unverifiable / unverifiable-prose bullets):

```
cd /tmp && sed -n '111,114p' corpus/lessons/round-68.md | grep -oE 'S[0-9]{3}' | sort > /tmp/item10-verdict-ids.txt
awk … (recipe above, ids normalized) | sort > /tmp/item10-awk-ids.txt
comm -3 /tmp/item10-awk-ids.txt /tmp/item10-verdict-ids.txt
```

`awk_ids=21 verdict_ids=21`; the `comm -3` output is empty — the two sets are
identical. Per-bucket reconciliation against the raw evidence:

- present (9): S776, S778, S786, S795, S796, S804, S820, S823, S824 — 4 HTML
  `found` hits in `quarantine-handcheck.json` (S776/S778/S804/S823) + 5 PDF
  `pdftotext` hits in `quarantine-pdf-pass.json` (S786/S795/S796/S820/S824).
- refused (8): S779, S787, S792, S814, S816, S817, S825, S827 — handcheck
  entries with HTTP 200 and `found: null` (quote absent from served bytes).
- unverifiable (1): S791 — handcheck shows HTTP 400 (register URL truncated
  mid-percent-sequence; broken locator, not fabrication).
- unverifiable, register prose (3): S807, S812, S835 — absent from handcheck by
  design (register records the source was never fetched; no locator to check).

18 handcheck entries + 3 prose rows = 21 = every register row. The register's
own "By lane" table prints kotodama = 18 because it counts only
`payload-absent` rows; a reader reconciling that number against 21 verdicts
must also read the "Rows whose quotes were NEVER CHECKED" section — a trap the
round-68 lesson already navigated, restated here as a finding.

## VERDICTs

- VERDICT: PASS — re-derivation: the addendum-quoted awk recipe reproduces the
  kotodama slice exactly: 21 data rows, ids S776 S778 S779 S786 S787 S791 S792
  S795 S796 S804 S807 S812 S814 S816 S817 S820 S823 S824 S825 S827 S835,
  byte-consistent with round-68's committed `quarantine-slice` artifact.
- VERDICT: PASS — coverage: the round-68 `## Quarantine` verdict list covers
  every register row (21/21; mechanical set difference empty; per-bucket counts
  9 present / 8 refused / 4 unverifiable reconcile against the raw JSONs).
- VERDICT: NOT-EVALUATED — re-fetching the 9 present / 8 refused rows live:
  out of scope this round (no external network fetching is authorized), the
  round-68 handcheck evidence is on disk and unmodified (sha256s recorded
  therein), and re-adjudication would belong to a reopening round, not this seat.
- Adoption status: **adoption stays CLOSED this round (round 69).** No
  shokuknow register row was adopted, appended, renumbered or marked settled in
  any repo; the shokuknow repo was touched only by reads (`ls`, `Read`, awk over
  an absolute path with cwd=/tmp). Verdicts remain the round-68 per-row ones;
  the register's rows are candidates, not verdicts, per its own header.

## Notes for the L1

- Namespace collision (already recorded at round-68, restated): register S-ids
  are the shokuknow campaign package's numbering, disjoint from this lane's
  `corpus/SOURCES.md` registry ids that reuse the same S-numbers (the lane's
  S776 is a different row than the register's S776). Any future adoption round
  must remap ids before touching lane bytes.
- The three never-checked rows (S807, S812, S835) are prose-class "source could
  not be fetched" entries with no recorded locator; they are neither
  fabrications nor verifications, and remain permanently uncheckable unless the
  campaign records locators.
