# ScoutIdMap — round 77 W1

## Finding

The adopted documents D1 and D2 are new to the BASE lane registry; the proposed map is staged S897 → lane S897 (D1) and staged S903 → lane S898 (D2). The remaining named candidate rows are not adopted by Claim C, so they receive no lane ID this round. Rejected-document rows that duplicate a cited staged artifact are mapped to its document identity, not to a second lane row: S934 → same document as S903/D2; S936 → same PDF as S918 (but the PDF is 潘蕾, “名前から見る古代貴族の家族観,” not the alternate description in S936). S933 is the same document as staged S875, not a base lane row. No document in the task's enumerated staged naming IDs matches a BASE lane document.

## By-document map: named staged naming IDs

| staged id | document URL (normalized: scheme/trailing slash/fragment removed; query retained) | proposed lane id / disposition |
|---|---|---|
| S897 | lishisuo.cssn.cn/xsyj/qhs/yjcg/202103/t20210316_5318560.shtml | S897 — D1, adopted; no BASE match |
| S903 | onomastica.ijppan.pl/index.php/ONOM/article/download/574/763 | S898 — D2, adopted; no BASE match |
| S906 | chinafolklore.org/web/index.php?NewsID=10867 | none — held, not adopted |
| S907 | ir.library.osaka-u.ac.jp/repo/ouka/all/77834/gbg_018_197.pdf | none — held, not adopted |
| S911 | sites.google.com/jnjh.mlc.edu.tw/cht/%E9%A6%96%E9%A0%81/%E5%9C%8B%E5%AD%B8%E5%B8%B8%E8%AD%98/%E4%B8%AD%E5%9C%8B%E7%9A%84%E5%90%8D%E8%88%87%E5%AD%97 | none — held, not adopted |
| S912 | opac.agulin.aoyama.ac.jp/iwjs0011opc/bdyview.do?bodyid=BD00000012&elmid=Body&fname=tf02143409.pdf&loginflg=on&once=true | none — held, not adopted |
| S913 | kci.go.kr/kciportal/landing/article.kci?arti_id=ART001733226 | none — held, not adopted |
| S914 | tdr.lib.ntu.edu.tw/handle/123456789/68394?mode=full | none — held, not adopted |
| S918 | omu.repo.nii.ac.jp/record/4358/files/2014000035.pdf | none — held, not adopted; same artifact as S936 |
| S933 | journal.psych.ac.cn/xlkxjz/EN/10.3724/SP.J.1042.2021.01067 | none — rejected; same document as staged S875 (not base lane) |
| S934 | onomastica.ijppan.pl/index.php/ONOM/article/download/574/763 | S898 document identity — rejected duplicate of S903/D2; row's Słon description conflicts with fetched artifact |
| S936 | omu.repo.nii.ac.jp/record/4358/files/2014000035.pdf | same document identity as S918; rejected bibliography bridge |
| S939 | sciscanpub.com/uploads/2024/01/22/8fc3f53fec6aeef6f695d96def4979fb.pdf | none — rejected this round |
| S940 | docin.com/p-1248229707.html | none — rejected this round |
| S941 | ndlsearch.ndl.go.jp/books/R100000136-I1970867909914725168 | none — rejected this round |
| S942 | ndlsearch.ndl.go.jp/books/R100000136-I1971712334815706289 | none — rejected this round |
| S943 | waseda-up.co.jp/social/post-421.html | none — rejected this round |
| S944 | cir.nii.ac.jp/crid/1981149385500149504.json | none — rejected this round |

## Base document sweep

`git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show 211f9526800906e0c585d878d265c37e5e090c15:corpus/SOURCES.md > /fast/scratch/hyaku/kotodama-r77/ScoutIdMap/SOURCES.base.md` — 953 lines; 820 `| S` rows.

`python3` URL extraction and normalization over the BASE registry and the 18 named staged IDs (scheme, trailing slash, fragments removed; Wayback wrappers unwrapped; queries retained) — exact normalized URL matches: none. Token sweep over BASE source rows for each named document's host/path/identifier — no document hits. The one broad `onomast` hit is S543, a different ICONN proceedings PDF (`4_13_Katalin_Reszegi_ICONN_6.pdf`), not D2's Onomastica article. Query-bearing staged URLs were compared with query intact to avoid conflating distinct records.

Same-artifact checks from direct bytes:

- `curl -sSL -o s934.pdf -w 'HTTP %{http_code} %{size_download}B\\n' --max-time 60 'https://onomastica.ijppan.pl/index.php/ONOM/article/download/574/763/'` → `HTTP 200 417093B`; `pdftotext -f 1 -l 1 s934.pdf -` begins `https://doi.org/10.17651/ONOMAST.69.7`, `Onomastica LXIX, 2025`, `IRENA KAŁUŻYŃSKA`, `FLOWERS, PLANTS, AND TREES IN FEMALE NAMING IN CHINA`. Therefore S934's URL is the D2 document despite its Słon/Poland source-cell description.
- `curl -sSL -D omu.headers -o omu.pdf --max-time 60 'https://omu.repo.nii.ac.jp/record/4358/files/2014000035.pdf'` → HTTP 200, `Content-Type: application/pdf`, `Content-Length: 564692`; `pdftotext -f 1 -l 1 omu.pdf -` → `名前から見る古代貴族の家族観`, metadata author 潘蕾; reference list includes `納日碧力戈『姓名』中央民族大学出版社、2000`. Therefore S936 is the same artifact as S918, and its source-cell description is a reference-list locator within that PDF, not the PDF's own title.

## Global staged-ID collision context

A sweep of all staged rows (not just the naming subset) establishes why the round's doc-identity map is necessary. At BASE, 27 staged IDs intersect lane IDs; these URL matches identify existing documents (the map is staged id → held lane id):

| staged id | existing lane id |
|---|---|
| S859 | S895 |
| S863 | S874 |
| S864 | S888 |
| S865 | S889 |
| S866 | S890 |
| S867 | S875 |
| S870 | S893 |
| S876 | S885 |
| S881 | S876 |
| S882 | S877 |
| S883 | S881 |
| S884 | S882 |
| S885 | S885 |
| S892 | S878 |
| S893 | S879 |
| S899 | S883 |
| S900 | S884 |
| S901 | S880 |
| S902 | S886 |
| S904 | S887 |
| S905 | S891 |
| S908 | S894 |
| S919 | S892 |
| S932 | S895 |
| S935 | S894 |
| S937 | S896 |
| S967 | S874 |

The exact-URL matching sweep output was:

```text
S859 -> S895; S863 -> S874; S864 -> S888; S865 -> S889; S866 -> S890; S867 -> S875; S870 -> S893; S876 -> S885; S881 -> S876; S882 -> S877; S883 -> S881; S884 -> S882; S885 -> S885; S892 -> S878; S893 -> S879; S899 -> S883; S900 -> S884; S901 -> S880; S902 -> S886; S904 -> S887; S905 -> S891; S908 -> S894; S919 -> S892; S932 -> S895; S935 -> S894; S937 -> S896; S967 -> S874
```

The command used was the normalization sweep in `/fast/scratch/hyaku/kotodama-r77/ScoutIdMap`; its raw ID intersection fixture is retained in `stage/ScoutIdMap/staged-ids.txt`, `reg-ids.txt`, `collisions.txt` (the collision rows are ID collisions, while the URL matching table above is the distinct-document check). Note S859 staged and lane S895 share the exact openstd newGbInfo document; this is the round-76 showGb/newGbInfo document-identity class. The requested named naming rows are not among those base-document matches.

## Guard proof

Fixture registry bytes (also copied to `w1/stage/ScoutIdMap/guard-registry.txt`):

```text
  | S903 | fixture planted indented row | docs | B | scope | §1 | fixture | queued | 2026-10-27 | 90d | — |
```

Command: `grep -E '^ {0,3}\\| S[0-9]{3,} \\|' guard-registry.txt | sed -E 's/^ {0,3}\\| (S[0-9]{3,}) \\|.*/\\1/' | sort -u > guard-extracted-ids.txt` → raw output `S903`.

Command: `comm -12 staged-ids.txt guard-extracted-ids.txt` → raw output `S903`.

The planted ID S903 is present in the staged ID set, so the indented row produces an intersection as required. Supporting fixture files are in `.ufo/waves/round-77/w1/stage/ScoutIdMap/`.

## Evidence limitations

No full fetch was made for the other held/rejected candidate documents; their listed URLs are extracted from staged source cells, not independently opened. No git fixture repository was needed for this pure text/list intersection. No installs or upgrades were performed. Report scratch was removed before completion.
