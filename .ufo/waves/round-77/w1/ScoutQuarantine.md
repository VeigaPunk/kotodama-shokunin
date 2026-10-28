# ScoutQuarantine — round 77

## Re-derived slice

Command:
```sh
awk -F'|' -v l='kotodama' '$2 ~ ("`" l "`") && $3 ~ /round[0-9]+/ && $4 ~ /S[0-9]+/ {print $4, $5}' /home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md
```
Raw output saved at `.ufo/waves/round-77/w1/stage/ScoutQuarantine/slice.txt`. The count command was `... | wc -l`; raw output: `21`. This matches the requested expected count of 21. The output consists of 18 `payload-absent` entries (rounds 1–5) and three never-checked entries (printed IDs have a trailing backtick due to the register cell spelling `S###``; source table header is at register line 265).

## Per-row document-set collision

Compared each cited-source URL in the 21-row slice with URLs in the staged naming-systems set (`naming-systems.amend-2026-10-23[ b/c ].md`, `naming-systems.amend-2026-10-24*.md`) and staged `SOURCES.append.md`. A collision here means same cited URL/document appears in the staged naming set; it does not mean the row's *quote* was verified or that the row is admitted. The slice and document set are from the read-only shokuknow tree.

| Register row | Register cited source (short) | Collision? | Staged match / note |
|---|---|---:|---|
| S776 | openstd.samr.gov.cn … hcno=E107… | Yes | staged S859 and S932 in SOURCES.append.md; S932 also occurs in naming amend text |
| S778 | eco.mtk.nao.ac.jp/koyomi/ | No | — |
| S779 | nao.ac.jp/news/topics/2026/20260202-rekiyoko.html | No | — |
| S786 | conlang.org/26c3.pdf | No | — |
| S787 | chinawriter.com.cn/n1/2023/0922/c404024-40083104.html | No | — |
| S791 | ir.psych.ac.cn/bitstream/…/名字的心理效应… | No | — |
| S792 | journal.psych.ac.cn/xlkxjz/EN/10.3724/… | Yes | Same DOI/document occurs as staged S875 and Chinese-page S966 (r13); archive URL in staged S933 (24 Oct candidate). URL forms differ where noted, document identity is shared by DOI. |
| S795 | obirin.ac.jp/…/BC-2-1-5-2-4_02.pdf | No | — |
| S796 | kankyo-u.ac.jp/…/field/189.pdf | No | — |
| S804 | kotobank.jp/word/苗字-392782 | Yes | staged S886, companion reference in the adopted 23 Oct amend |
| S814 | lishisuo.cssn.cn/…/t20210316_5318560.shtml | Yes | staged S897, D1 |
| S816 | chinawriter.com.cn/n1/2025/0605/c404024-40494534.html | No | — |
| S817 | chinawriter.com.cn/n1/2022/1207/c404024-32582252.html | No | — |
| S820 | onomastica.ijppan.pl/…/download/574/763/ | Yes | staged S903, D2; also staged S934 is the same DOI/document in rejected 24 Oct candidate |
| S823 | chinafolklore.org/web/index.php?NewsID=10867 | Yes | staged S906, held 23b amendment |
| S824 | ir.library.osaka-u.ac.jp/…/gbg_018_197.pdf | Yes | staged S907, held 23b amendment |
| S825 | digital.archives.go.jp/search | Yes | staged S908, 23 Oct amend reference set |
| S827 | doi.org/10.1007/978-3-032-03277-5_15 | Yes | staged S910, 23 Oct amend reference set |
| S807` | doi.org/10.34158/ONOMA.51/2016/8 | Yes | staged S890, 23 Oct amend reference set; this is from NEVER CHECKED table, not payload-absent |
| S812` | doi.org/10.1017/cnj.2024.21 | No | — |
| S835` | omu.repo.nii.ac.jp/record/4358/files/2014000035.pdf | Yes | staged S918 and S936 (23c / rejected 24 Oct candidate) |

Collision tally: 11 of 21; no collision: 10 of 21. Distinguish direct URL hits from document identity: S792↔S875/S966/S933 is DOI-equivalent across language/archive URL variants. The three trailing-backtick IDs are exactly as emitted by the requested awk command; the register's never-checked table explicitly says those source quotes were not checked, so they are not fabrication verdicts.

## Evidence commands and raw outputs

- Register table section check: `grep -n '^## \|^| lane\|^|---' /home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md`; output: `## Rows` line 25, `## By lane` 232, `## Rows whose quotes were NEVER CHECKED` 256; table header at 265.
- Never-checked rows: `read` register lines 330–335; raw rows show kotodama S807`, S812`, S835` and their cited URLs. Register lines 333–335 give the full source mapping above.
- Staged URL mapping: `grep -F '<URL>' /home/vgpnk/Projects/shokuknow/merge/kotodama/SOURCES.append.md`; for all 21 source URLs, hits are the staged ids listed in the table (or no output for non-collisions). Examples: lishisuo → `| S897 |`; onomastica → `| S903 |` and `| S934 |`; omu.repo → `| S918 |` and `| S936 |`; chinafolklore → `| S906 |`; Osaka PDF → `| S907 |`; digital archives → `| S908 |`; Palgrave DOI → `| S910 |`; ONOMA DOI → `| S890 |`.
- Staged amend URL sweep: command iterated all `naming-systems*.md` under `/home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge/linguistics/`, extracted URL strings, and compared host/path patterns for the slice. Raw hits: 23 Oct amend (lishisuo, ONOMA DOI, Kotobank entries, onomastica); 23b (Osaka PDF); 23c (omu.repo); 24 (Wayback variants for psych article, omu.repo, onomastica); r13 (psych article Chinese page). Other naming amend files had no hits from the slice URL sweep.
- No live source re-fetch or quote-level adjudication was assigned or performed; collision is URL/document-set membership only.
