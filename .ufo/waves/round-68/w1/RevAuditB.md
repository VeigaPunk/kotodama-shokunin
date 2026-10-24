# RevAuditB — report (claim O residual, round 68)

Seat: L1-kotodama-r68-attempt2.RevAuditB. Chains assigned: S126>S105, S127>S079, S128>S086, S129>S117. Full rulings at `.ufo/waves/round-68/rows/RevAuditB/audit.md` (path relative to the lane repo).

## Verdicts (all four: activate | repoint, one target entry each)

| Chain | s URL status (2026-10-24 live re-open) | Ruling | Citing loci repointed |
|---|---|---|---|
| S126>S105 | HTTP 200 text/html 62,524 B; Glottolog 5.3; both declared sections; both quoted sentences verbatim | activate | entry :129 inline + Source cell (`S105` → `S126`; placement fact rests on S104) |
| S127>S079 | HTTP 200 text/html 58,031 B; both sections served | activate | entry :37, :62 clean; :64 flagged (see findings) |
| S128>S086 | HTTP 200 application/pdf 18,159,342 B; TOC confirms Introduction = printed pp. 2-26 | activate | entry :20, :45, :59 (×3), :61, :171, :191, :220 — all carried (anchor superset) |
| S129>S117 | HTTP 200 text/html 257,846 B; same article as S117; "In this review" ×3; abstract verbatim | activate | none — S117 has zero inline citations at base (tool scan used_by=0) |

Semantic proof via the frozen tool (read-only `--scan --root .`): all four chains PENDING; totals pending=34 chains=47 usedby_paths=686 missing_paths=0 — matching the declared base exactly. Ledger vocabulary observed: `activate` requires s status mined (L1's queued→mined mutation is in the frozen MUTABLE set); `retire` requires rejected (inapplicable — no s row here is a rejection).

## Findings

1. NON-BLOCKING (row basis): S128's supersedes basis claims the Introduction's generalizations carry hedges "usually"/"in most cases" — neither occurs in the declared span (checked plain and +3-cipher-decoded); those hedges live in later chapters (whole doc: usually ×31, tend to ×15, in most cases ×1). Tier-B basis (editors' survey) unaffected.
2. NON-BLOCKING (anchor coverage): S127's declared anchor omits "Hearing Gesture: The Gestures We Produce When We Talk", where the served page carries the co-speech content behind entry :64; the substantive non-conventionality claim at :64 is S087's. Successor anchor-widening row or explicit L1 note advised.
3. VERIFICATION GAP (extraction): the served S128 PDF's Introduction digits are unrecoverable through pdftotext (broken ToUnicode; letters decode by uniform +3 shift, digits do not), so :59's figures (≈150 signers; 90–200 years) were not byte-re-verified; carried transitively because S128's span strictly contains S086's pp. 2-10 in the same served artifact.
4. OBSERVATION: S126's declared sections never name ASL/LSF — the :129 repoint correctly splits placement fact (S104) from grouping status (S126); no sentence fix needed.
5. OBSERVATION: S117 uncited at base; its used-by cell naming the entry is stale and belongs to the settlement sweep's cell repair, not to any entry edit.

No registry row, entry file, or lane jj/git state was touched by this seat. No tools were installed or upgraded (curl, pdftotext, python3 already present); no pacman transactions attempted, per the 2026-10-20 pacman guard.

Report: .ufo/waves/round-68/rows/RevAuditB/audit.md
