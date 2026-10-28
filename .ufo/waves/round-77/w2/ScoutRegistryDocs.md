# ScoutRegistryDocs — round 77 W2 (falsifier)

Attacked item: **W1 `w1/ScoutIdMap.md` by-document id map** (staged-id → normalized document → lane-id), re-checked against the ACTUAL base `corpus/SOURCES.md` row set at `211f9526800906e0c585d878d265c37e5e090c15` and the staged registry `/home/vgpnk/Projects/shokuknow/merge/kotodama/SOURCES.append.md` (the file the W1 seat spec names). Verdict: **map confirmed; no falsifier found.** S897/S898 are unused lane ids; every adopted normalized document is unique; both archive wrappers unwrap exactly to their live URLs.

## 1. Row sets actually compared

- Base: `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show 211f9526800906e0c585d878d265c37e5e090c15:corpus/SOURCES.md` → 953 lines; row extractor `^\s{0,3}\|\s*(S\d{3,})\s*\|` → **820 rows, 820 unique ids**, min S001, max S896. (W1 claimed 820 — verified.)
- Staged: `SOURCES.append.md` → **132 rows, 132 unique ids**, S859–S990 contiguous. (W1 claimed S859–S990/132 — verified.)
- Named naming-id set (W1 seat spec, verbatim): `S897, S903, S906, S907, S911, S912, S913, S914, S918, S933, S934, S936, S939, S940, S941, S942, S943, S944` — 18 ids, all present in the staged registry; each also appears in at least one staged `naming-systems.amend-*.md` file (grep over `/home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge/linguistics/`).

## 2. S897/S898 are unused lane ids — VERIFIED

```
base rows: 820 unique ids: 820
base id range: min=S001 max=S896
S897 in base: False | S898 in base: False
anywhere-mention S897: NONE      (literal grep over full base file, not only id cells)
anywhere-mention S898: NONE
```

Base ids are contiguous only up to S896 as the *maximum* — the range has holes (S455–S480, S492–S499, S544–S563, S577–S599, S777–S778 never used). So "unused" here = the correct lane-id interpretation: S897/S898 are the next two ids after the max and appear nowhere in the file. Both also exist as *staged* ids (S897 = the cssn article = D1; S898 = an NDL NDC10 classification PDF, a DIFFERENT document — see §5 note).

## 3. Document normalization method (re-derived independently)

Per staged/base row cell: extract `https?://[^\s|)\]>,]+`, strip trailing `.,;:'"`; unwrap `web.archive.org/web/<14 digits><flags>_/<inner>` to `<inner>`; strip scheme, fragment, trailing `/`; lowercase; keep query. Identical rules to W1's description; the script was re-written this wave, not copied.

## 4. Exact by-document map (named staged naming ids)

| staged id | normalized document | base doc match | disposition per W1 map | my verdict |
|---|---|---|---|---|
| S897 | lishisuo.cssn.cn/xsyj/qhs/yjcg/202103/t20210316_5318560.shtml | NONE | → lane S897 (D1, adopted) | CONFIRM |
| S903 | onomastica.ijppan.pl/index.php/onom/article/download/574/763 | NONE | → lane S898 (D2, adopted) | CONFIRM |
| S906 | www.chinafolklore.org/web/index.php?newsid=10867 | NONE | held | CONFIRM |
| S907 | ir.library.osaka-u.ac.jp/repo/ouka/all/77834/gbg_018_197.pdf | NONE | held | CONFIRM |
| S911 | sites.google.com/jnjh.mlc.edu.tw/cht/%e9%a6%96%e9%a0%81/…/%e4%b8%ad%e5%9c%8b%e7%9a%84%e5%90%8d%e8%88%87%e5%ad%97 | NONE | held | CONFIRM |
| S912 | opac.agulin.aoyama.ac.jp/iwjs0011opc/bdyview.do?bodyid=bd00000012&elmid=body&fname=tf02143409.pdf&loginflg=on&once=true | NONE | held | CONFIRM |
| S913 | www.kci.go.kr/kciportal/landing/article.kci?arti_id=art001733226 | NONE | held | CONFIRM |
| S914 | tdr.lib.ntu.edu.tw/handle/123456789/68394?mode=full | NONE | held | CONFIRM |
| S918 | omu.repo.nii.ac.jp/record/4358/files/2014000035.pdf | NONE | held | CONFIRM |
| S933 | journal.psych.ac.cn/xlkxjz/en/10.3724/sp.j.1042.2021.01067 (wrapper + withdrawn-original both unwrap to this) | NONE | rejected; same doc as staged S875, NOT a base row | CONFIRM |
| S934 | onomastica.ijppan.pl/index.php/onom/article/download/574/763 (wrapper 20251231111748 + withdrawn-original both unwrap to this) | NONE | rejected duplicate of S903/D2 → lane S898 document identity | CONFIRM |
| S936 | omu.repo.nii.ac.jp/record/4358/files/2014000035.pdf (wrapper 20251010013419 + withdrawn-original both unwrap to this) | NONE | rejected; same doc as staged S918 | CONFIRM |
| S939 | www.sciscanpub.com/uploads/2024/01/22/8fc3f53fec6aeef6f695d96def4979fb.pdf | NONE | rejected | CONFIRM |
| S940 | www.docin.com/p-1248229707.html | NONE | rejected | CONFIRM |
| S941 | ndlsearch.ndl.go.jp/books/r100000136-i1970867909914725168 | NONE | rejected | CONFIRM |
| S942 | ndlsearch.ndl.go.jp/books/r100000136-i1971712334815706289 | NONE | rejected | CONFIRM |
| S943 | www.waseda-up.co.jp/social/post-421.html | NONE | rejected | CONFIRM |
| S944 | cir.nii.ac.jp/crid/1981149385500149504.json | NONE | rejected | CONFIRM |

## 5. Uniqueness of normalized documents

- 18 named ids → **16 distinct normalized documents**. The two shared-doc groups are exactly the ones W1 mapped to a single document identity: `{S903, S934}` (D2) and `{S918, S936}` (omu PDF). A third sharing crosses the named-set boundary: staged `S875` normalizes to the same psych.ac.cn document as `S933` — W1 said "S933 is the same document as staged S875," and I verified staged S875's raw URL `https://journal.psych.ac.cn/xlkxjz/EN/10.3724/SP.J.1042.2021.01067` == S933's unwrapped/withdrawn URL. (Base lane row S875 is a *different* document — `online.bunka.go.jp/db/heritages/search`, collision target of staged S867 — so S933 correctly maps to no base row.)
- The two adopted documents (D1, D2) are distinct from each other and from every other named document: each is unique and gets exactly one new lane row. No named staged document → two different lane ids. PASS.
- Near-duplicate token sweep over base rows: `grep -nE 'ijppan|10\.17651|view/574|ONOMAST\.69|cssn|5318560|download/574|psych\.ac\.cn|10\.3724|SP\.J\.1042|omu\.repo|4358' SOURCES.base.md` → **0 lines** (raw output: empty for every token). Broad `onomast` sweep → only S543 (Reszegi ICONN proceedings, `onomasticafelecan.ro` — different document, as W1 stated). DOI/alternate-path routes to the same D2 artifact (api.crossref, `article/view/574`, `ONOMAST.69.7`) are absent at base. Document-level duplicate via a second URL string: none found.
- Context note (not a defect of this map): the base registry itself contains 50 pre-existing internal same-document groups (e.g. `metmuseum.org/…/318318` under S395/S400/S486; `britannica.com/topic/tuareg` under S701/S858) — 820 rows → 874 distinct normalized keys because several rows cite multiple URLs and the same document recurs. None of these touch any named staged id; the D1/D2 additions do not enlarge this pre-existing condition.

## 6. Archive wrapper → live URL mapping — VERIFIED

Deterministic unwrap on the DRAFT's own pairs:

```
D1 (lane S897): inner==live-exact=True
   inner: http://lishisuo.cssn.cn/xsyj/qhs/yjcg/202103/t20210316_5318560.shtml
   norm : lishisuo.cssn.cn/xsyj/qhs/yjcg/202103/t20210316_5318560.shtml == lishisuo.cssn.cn/xsyj/qhs/yjcg/202103/t20210316_5318560.shtml
D2 (lane S898): inner==live-exact=True
   inner: https://onomastica.ijppan.pl/index.php/ONOM/article/download/574/763/
D2 alt capture (staged S934 row): inner==live-exact=True
   inner: https://onomastica.ijppan.pl/index.php/ONOM/article/download/574/763/
```

- D1 wrapper `web.archive.org/web/20240111092427id_/http://lishisuo.cssn.cn/…` → inner string identical to the staged live URL (http scheme preserved inside the wrapper; the extractor keeps `http://` because the unwrap runs before scheme-strip).
- D2 wrapper `…/web/20260901045105id_/https://onomastica.ijppan.pl/…/763/` and the S934-row wrapper `…/web/20251231111748id_/…` → inner identical to the D2 live URL.
- Independent corroboration in W1 receipts (not re-fetched by this seat): `stage/ScoutCDXPositive/cdx-d1.out` records CDX `original` = `http://lishisuo.cssn.cn/xsyj/qhs/yjcg/202103/t20210316_5318560.shtml` at ts 20240111092427 status 200 — the same string the wrapper wraps. `cdx-d2.out` records `original` = the D2 URL at both captures; `stage/ScoutDocS898/evidence.txt` records capture 20260901045105 byte-identical to live (sha `5d1bfa5a…29bc`, 417093 B).
- Staged rows S933/S934/S936 each carry BOTH a wrapper and a `(withdrawn original: …)`; both forms unwrap to the same normalized document, so the map is wrapper-safe in both directions.

## 7. Collision counts (exact)

| measure | count | detail |
|---|---|---|
| named staged ids → base, normalized-document collisions | **0** | all 18 rows print `base match: NONE` |
| adopted documents D1/D2 → base | **0** | incl. alternate-URL/DOI token sweep (0 hits) |
| staged ∩ base **id-level** collisions | **38** | S859–S896 contiguous (staged set ids that are already lane ids; S897–S990 are all free lane ids) |
| staged → base **document-level** collisions (whole 132-row set) | **27** | re-derived map equals W1's table verbatim (see below) |
| intra-named shared-document groups | **2** | {S903,S934}, {S918,S936}; +1 crossing boundary {staged S875,S933} |
| base internal dup-doc groups (context only) | **50** | none in the named set |

Re-derived 27 document collisions, identical to W1:
`S859→S895; S863→S874; S864→S888; S865→S889; S866→S890; S867→S875; S870→S893; S876→S885; S881→S876; S882→S877; S883→S881; S884→S882; S885→S885; S892→S878; S893→S879; S899→S883; S900→S884; S901→S880; S902→S886; S904→S887; S905→S891; S908→S894; S919→S892; S932→S895; S935→S894; S937→S896; S967→S874` — none of the 18 named naming ids appears on the left side. CONFIRM.

## 8. Asymmetry worth logging (not a falsifier)

Staged id S898 is *not* unused in the staged registry — it is the NDL NDC10 classification PDF (`ndl.go.jp/…/NDC10code202206.pdf`), a different document from D2. The lane-id assignment S898 → D2(staged S903) is therefore correct only because the map is document-level, exactly as the DRAFT states ("identity is document-level, not ID arithmetic"). If a future round adopts staged S898's document it will need a fresh lane id ≥ S899; a naive `staged==lane` assumption would silently conflate two documents. Same class of asymmetry: staged S933 == staged S875's document while lane S875 is yet another document. No action required this round; flagged for the freeze's by-document map to keep.

## 9. Commands run (verbatim, all under scratch `/fast/scratch/hyaku/kotodama-r77/ScoutRegistryDocs/`)

1. `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show 211f9526800906e0c585d878d265c37e5e090c15:corpus/SOURCES.md > SOURCES.base.md` → 953 lines.
2. `cp /home/vgpnk/Projects/shokuknow/merge/kotodama/SOURCES.append.md staged.append.md` → 132 `|` rows.
3. `grep -oE 'S[0-9]{3}' /home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge/linguistics/naming-systems.amend-*.md | sort -u` → per-file staged-id lists (adopted file cites S886 S888 S889 S890 S891 S896 S897 S903).
4. Python extraction + normalization scripts (§2–§5 outputs reproduced verbatim above).
5. `grep -nE '<token>' SOURCES.base.md` for the 12 near-dup tokens → empty output, all 12.
6. Wayback unwrap checks on the three DRAFT/staged wrapper pairs → `inner==live-exact=True` ×3.

No installs, no network fetches by this seat (CDX/fetch receipts cited are W1 artifacts read in place). Lane, fleet, and staged registries read-only throughout. Scratch `/fast/scratch/hyaku/kotodama-r77/ScoutRegistryDocs/` deleted before yield.

## Verdict

CONFIRMED: the W1 by-document map is correct against the actual base row set. S897 and S898 are free lane ids; the planned rows S897→D1, S898→D2 collide with nothing at base; each adopted normalized document is unique (named-set dupes are rejected-duplicate dispositions by design); every archive wrapper unwraps to its stated live URL. No falsifier.
