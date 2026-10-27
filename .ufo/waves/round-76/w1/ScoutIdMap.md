# ScoutIdMap — round 76 W1 by-document renumber map

**Verdict:** Produced pre-data map in the round-75 schema at `w1/stage/ScoutIdMap/id-renumber-map.json`. Join evidence is URL/document-based, never arithmetic. Eight direct campaign registry citations map to seven lane documents; campaign S908 and S935 collapse to one document. The five planned new lane ids match the draft, but there are additional unregistered documents mentioned by the candidate files and bare earlier-round ids that currently point to unrelated lane rows. The map does not itself adopt anything.

## Reproduction and registry bounds

Command: `cd /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-76/w1/stage/ScoutIdMap && python3 build-id-map.py`

Raw output:
```
assignments 8 map 8 collisions 35 relevant ['S887']
```

Command: `wc -l /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-76/assimilation/{reg-ids,staged-ids,collisions}`

Raw output:
```
817 .../reg-ids
132 .../staged-ids
35 .../collisions
```

Command: `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin rev-parse HEAD`

Raw output: `98c486bdb4650ba5b8e651d332910e8ee60ad121` (matches the pinned base).

The script independently extracts ITEM10 table rows from base `corpus/SOURCES.md` and `SOURCES.append.md` and asserts the three extracted id sets equal those supplied in round-76 assimilation. Its exact normalization follows `round-75/assimilation/build-map.py:52-67`: strip Wayback wrapper, lowercase host and strip `www.`, URL-decode path, collapse Persée per-page URL to article URL. The complete inputs, hashes, every id-pair and each occurrence are in the JSON.

## By-document assignments

The assignment output is directly derived from staged source cells (not numeric offsets). For each of the five planned rows, no matching base lane row exists; the row URL cell cannot yet be compared because no such lane cell exists. The proposed lane row must carry the document URL in the map. For already-held documents the two extant URL cells were opened and joined:

| Campaign row(s) | Lane target | Document-URL proof / disposition |
|---|---|---|
| S908 + S935 | S894 (planned) | Both source cells normalize to `digital.archives.go.jp/search`; S935's Wayback wrapper embeds that exact original URL. One document, one lane row. No match in base registry. |
| S916 | S895 (planned) | `xingzuobaike.com/huangli/wannianli/d165803.html`; no match in base registry. Tier C reproduction, not sole support. |
| S932 | S896 (planned) | Wayback capture embeds `openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107...`; identical to the staged S859 row's live URL. S859 is a same-document duplicate/reference in the package, not a second document. No match in base registry. |
| S938 | S897 (planned) | `openstd.samr.gov.cn/bzgk/std/showGb?type=online&hcno=E107...`; distinct route from `newGbInfo`, so retained as its own document row per the draft. No match in base registry. |
| S937 | S898 (planned) | `news.gmw.cn/2017-05/23/content_24559485.htm`; no match in base registry. |
| S919 | S892 (existing) | Wayback source URL resolves to `iris.unipa.it/retrieve/.../2014%20marrone...pdf`; lane S892 source cell has the direct URL and the same Wayback URL. Match. |
| S921 | S885 (existing) | Staged source is Persée p. 6 per-page transcription; lane S885 source cell includes the same p. 6 URL and the parent article URL. Per-page transcription is a view of the same article. Match. |

Command: `python3 - <<'PY' ...` (the mapping-inspection command recorded in the session; it printed every map key, normalized URL, staged URL cell, and existing lane URL cell)

Raw output (all eight assignments):
```
S908 -> S894 digital.archives.go.jp/search sourceUrls= ['https://www.digital.archives.go.jp/search'] lane= None
S935 -> S894 digital.archives.go.jp/search sourceUrls= ['https://web.archive.org/web/20260422145052id_/https://www.digital.archives.go.jp/search', 'https://www.digital.archives.go.jp/search'] lane= None
S916 -> S895 xingzuobaike.com/huangli/wannianli/d165803.html sourceUrls= ['https://www.xingzuobaike.com/huangli/wannianli/d165803.html'] lane= None
S932 -> S896 openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296 sourceUrls= ['https://web.archive.org/web/20260424031027id_/https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296', 'https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296'] lane= None
S938 -> S897 openstd.samr.gov.cn/bzgk/std/showGb?type=online&hcno=E107EA4DE9725EDF819F33C60A44B296 sourceUrls= ['https://openstd.samr.gov.cn/bzgk/std/showGb?type=online&hcno=E107EA4DE9725EDF819F33C60A44B296'] lane= None
S937 -> S898 news.gmw.cn/2017-05/23/content_24559485.htm sourceUrls= ['https://news.gmw.cn/2017-05/23/content_24559485.htm'] lane= None
S919 -> S892 iris.unipa.it/retrieve/e3ad891d-ad9f-da0e-e053-3705fe0a2b96/2014 marrone age dor---2.pdf sourceUrls= ['https://web.archive.org/web/20251111222249if_/https://iris.unipa.it/retrieve/e3ad891d-ad9f-da0e-e053-3705fe0a2b96/2014%20marrone%20age%20dor---2.pdf'] lane= ('S892', ['https://iris.unipa.it/retrieve/e3ad891d-ad9f-da0e-e053-3705fe0a2b96/2014%20marrone%20age%20dor---2.pdf', 'https://web.archive.org/web/20251111222249if_/https://iris.unipa.it/retrieve/e3ad891d-ad9f-da0e-e053-3705fe0a2b96/2014%20marrone%20age%20dor---2.pdf'])
S921 -> S885 persee.fr/doc/comm_0588-8018_1966_num_8_1_1113 sourceUrls= ['https://www.persee.fr/doc/page/comm_0588-8018_1966_num_8_1_1113/comm_0588-8018_1966_num_8_1_T1_0006_0000'] lane= ('S885', ['https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113', 'https://www.persee.fr/doc/page/comm_0588-8018_1966_num_8_1_1113/comm_0588-8018_1966_num_8_1_T1_0005_0000;'])
```

The S921 lane cell output truncates its later URL list at a semicolon in this parser; direct opening of the full lane row at base (`git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show 98c486bdb4650ba5b8e651d332910e8ee60ad121:corpus/SOURCES.md`, row S885) shows the explicit p. 6 URL `...T1_0006_0000`, exactly the staged S921 URL. Thus URL-cell comparison is affirmative; parser truncation does not imply absence.

## Bare-text hazards and scope check

The bare tokens are earlier campaign scope-file identifiers, not current-package row IDs. Resolving them through round scope notes/document descriptions exposes unrelated rows under several same-number lane IDs. The document description in the entry is not evidence for the row numerically registered in this lane:

| Bare token in candidate | Campaign document it means | Same-number lane row at base | Action |
|---|---|---|---|
| S750 (entry a) and S718 (entry d) | official openstd GB/T 33661 record; current package S859, same document as S932 | S750 = Culin games; S718 = Farran infant-directed speech | Repoint both to S896 by document. |
| S807 (entry a) | third-party xingzuobaike reproduction; current package S916 | Li et al. persistent median artery | Repoint to S895 by document; retain tier-C caveat. |
| S719 (entry d), S777 (entry a) | Purple Mountain Observatory interpretation PDF, staged package S860; S719/S777 resolve to the same PDF in their respective earlier round contexts | S719 = Cristia infant-directed speech; S777 has no base lane row | No planned lane row currently covers this PDF. Do not leave these citations as if registered; remove/repair the mentions or add a distinct row under a separately approved plan. |
| S757 (entry c) | NDL NDC10 classification PDF, staged package S898 | Huizinga *Homo Ludens* | No planned row covers it; do not use same-number S757 as this source. |

Command: `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show 98c486bdb4650ba5b8e651d332910e8ee60ad121:corpus/SOURCES.md | grep -nE '...S757|S718|S719|S750|S807...'` (specific row search; exact command used was the S-number loop in shell)

Raw output included:
```
| S718 | Farran et al., 2016, "Cross-Cultural Register Differences in Infant-Directed Speech..."
| S719 | Alejandrina Cristia, 2013. Input to Language: The Phonetics and Perception of Infant-Directed Speech...
| S750 | Stewart Culin, “Games of the North American Indians,” ...
| S757 | J. Huizinga, Homo Ludens: A Study of the Play-Element in Culture ...
| S807 | Li, Yong Ming 2021, "Persistent median artery may explain the transition from 11 to 12 meridians..."
| S885 | Roland Barthes, ... https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113 ... p. 6 ...T1_0006_0000
| S887 | A. J. Greimas, ... https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1114 ...
| S892 | Gianfranco Marrone, ... https://iris.unipa.it/retrieve/.../2014%20marrone%20age%20dor---2.pdf ...
```

The SOURCES registry rule observed at base is: “Append-only: only `status`, `recheck` and `used-by` change in place” (command: `sed -n '1,18p' /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md`; raw output is that header). Existing S885/S892 usage/scope therefore needs care: the S921/S919 join is by document, but their scope is Barthes's named levels and Marrone's scholarly account of the five-code/four-level relation, respectively; they are a contrast/example in candidate a, not evidence about the Chinese calendar. The existing lane rows' `used-by` cells do not yet list the calendar entry. A `used-by` amendment is permitted only with old→new logging in a round lesson.

## 35 numeric collisions and S887

Command: `cat /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-76/assimilation/collisions | tr '\n' ' '` (collision-set listing).

Raw output:
```
S859 S860 S861 S862 S863 S864 S865 S866 S867 S868 S869 S870 S871 S872 S873 S874 S875 S876 S877 S878 S879 S880 S881 S882 S883 S884 S885 S886 S887 S888 S889 S890 S891 S892 S893
```

The exact-ID scan across the four DRAFT candidates plus the named non-candidate comparison file found **S887 — `grep -nE '\bS[0-9]{3,}\b' <each candidate>`**: in `era-periodization-models.amend-2026-10-23.md` (file e, not one of draft candidates a–d), it denotes Kotobank 平安時代; lane S887 at base is Greimas's *Éléments pour une théorie de l'interprétation du récit mythique*. This is the explicit dangerous collision from the assignment: copying that citation literally is wrong. None of the current draft candidate files a–d cites any of the 35 colliding campaign IDs as a bare token; e is included only to answer the specifically named S887 case. The map JSON records every one of the 35 collisions, both source descriptions, normalized-document equality, and the per-entry occurrence scan.

Command: `grep -nE '\bS[0-9]{3,}\b' /home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge/culture-material/era-periodization-models.amend-2026-10-23.md`

Raw output:
```
4:S898 6:S898 7:S732 7:S746 17:S898 30:S887 32:S887 33:S732 36:S732 36:S726 43:S887
```

This also reveals that file e's S898 is the NDL NDC10 PDF (staged S898) while planned lane S898 is the GMW report (staged S937). It is a post-adoption numeric overlap and must not be copied as an id. S746 is an earlier-round citation to the same Kotobank page as staged S887, but is not a lane-row id remapping; keep it out of arithmetic substitutions.

## Unknowns / remaining checks

- The DRAFT's five planned rows do not include the Observatory PDF (S860/S719/S777) or NDL NDC PDF (staged S898/S757), despite candidate prose mentioning them. Whether to admit added source rows or trim those references is a landing decision; this scout did not edit claims or landing files.
- S908/S935 live-vs-capture status and whether cited content remains accessible were not re-fetched here; the map only establishes document identity. No access-control bypass or source-opening claims are made.
- No LSP device was available in this scout environment; this is data/schema/source-table recon, so source rows were inspected directly.
- No tests/build/lint were run. No tool was installed.

## Files

- `w1/stage/ScoutIdMap/id-renumber-map.json` — full machine-readable map/evidence.
- `w1/stage/ScoutIdMap/build-id-map.py` — deterministic read-only generator; its output is written only beside the script.

Report: .ufo/waves/round-76/w1/ScoutIdMap.md
