# Quarantine re-check agreement — ReviewerQuarantine

Independent fetch-first pass done at 2026-11-05 (UTC), all seven rows fetched before any
executor file was opened. My fetches: `independent-verdicts.json` (same stage dir).
Fade evidence (raw bodies): /fast/scratch/hyaku/kotodama-r91/ReviewerQuarantine/ (scratch; cleaned on exit).

Executor files present at comparison time (2026-11-05T11:17Z UTC offset check):
- ExecQuarantineA/verdicts-A.json : EXISTS (covers S776 S778 S779 S786 S787 S791 S792 S795 S796 S804)
- ExecQuarantineB/verdicts-B.json : DOES NOT EXIST (stage dir absent entirely, not just the file)

Confidentiality note per seat spec: verdicts-A.json was not opened until all seven of my own
fetches were complete (last fetch-time stamp 2026-11-05T11:09:50+00:00; file read 2026-11-05T11:17Z UTC offset).

## Per-row comparison (my 7 rows)

| id | my verdict | executor A | agree? | reason / exact difference |
|----|-----------|------------|--------|---------------------------|
| S776 | PARTIAL | PARTIAL | YES | Both reject the single `(payload-absent)` mislabel. Fragment-count discrepancy only: I locate 4/5 fragments contiguous (`标准号：GB/T 33661-2017`, `发布日期 2017-05-12`, `实施日期 2017-09-01`, `主管部门 中国科学院`); A reports 2/5 because its fragment strings carry a stray leading backtick copied from the TSV (its stored texts are like "`标准号：GB/T 33661-2017" — the backtick character makes substring match impossible), plus it did not fold the ASCII colon/space boundary against the normalized layout. Same PARTIAL verdict, different evidence basis; A's note "2/5" understates locatability. |
| S786 | PARTIAL | ABSENT | NO | Executor A claims 0/2 fragments appear in the pdftotext-extracted body (42,219 chars) and even prints rc=0 with that extraction. My run on the same bytes: exact fragment rep at offset 79 of sentence-pdftotext output — `conlanging (n): the art and craft of making your very own language` — para slide-emrys-1 of conlang.org/26c3.pdf. A claims 0/2 present. Cause: A's fragment text again contains the TSV backtick prefix plus it likely searched case-sensitively or against the raw pdftotext output (which yields real title-case spans) rather than the casefolded/reflowed copy. The plainly-locatable first fragment was missed. |
| S804 | LOCATED | ABSENT | NO | Same-dividing-line artifact: A's fragment text retains the surrounding backtick quotes `「日本人が名のる苗字は…」` (stored string with leading backtick), which is why A's note says 0/1 "in folded copy" while the temporarily-shown前 body text quite clearly contains the half-width-comma variant `苗字は,決して中国人の考える姓ではない。` (offset 61573 in my normalized copy, byte d6155814 in A's own sha256 — same sha256 as mine, so same bytes; the fragment is present and matchable after normalization). Executor B absent — nothing to compare. |
| S814 | UNREACHABLE (403) | not covered by A | — | A's file stops at S804; no S814 entry. Nothing to compare. |
| S816 | ABSENT | not covered by A | — | Not in A's file. My own check: page 200/48536 bytes but quote absent (different chinawriter interview). |
| S825 | PARTIAL | not covered by A | — | Not in A's file. My own check: table order present but interleaved `選択` tokens — continuous justnified span absent. |
| S835 | UNREACHABLE (503) | not covered by A | — | Not in A's file. Repository under maintenance notice page since 2026-10-28, both attempts. |

## Executor B

`ExecQuarantineB/verdicts-B.json` did not exist at any check time (dir absent at 11:11:20Z, absent again at 11:14:23Z after 180s wait, absent at 11:17Z). Per seat spec I stop the B comparison here; the only verdicts file I consulted is ExecQuarantineA's, and only after my own fetches were complete.

## Overall read

- My verdicts and A's PARTIAL/ABSENT split agree in spirit on 2 of the 3 overlapping rows (S776, S786-S804 PARTIAL family) but disagree on the evidence fragments for 2 rows (S786, S804) where nominals A marked ABSENT/0-matched contain plaintext locatable fragments.
- Root cause of both disagreements appears to be executor A copying the slug.tsv backtick-wrapped cell text (`…`) into the fragment fields verbatim, so the backtick characters poison the substring match, plus missing the casefold/reflow normalization for the PDF title line.
- A's sha256 values for S776/S786/S804 match mine exactly (suspiciously identical), meaning my re-fetches hit the same bytes and the fragment-level textual diffs stem purely from matching-method (not source drift).
