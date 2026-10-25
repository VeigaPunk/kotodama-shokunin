# Round 71 frontier census — BEFORE

Read-only baseline for the round-71 claims, recorded independently at the current lane tree before claim work. The frozen claims declaration says the registry baseline is 784 rows. This check confirms it.

## Registry-row command

Command requested:

```sh
grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md
```

Verbatim output:

```text
784
```

The `CORPUS.md` §SOURCES.md column-zero row command independently returned `784` as well.

## CORPUS.md §SOURCES.md manual census

Commands and output from the lane root (the exact commands are documented at `/home/vgpnk/Projects/shokunin/CORPUS.md:131-147`):

```text
--- rows (CORPUS.md command) ---
784
--- rows (claim space-tolerant command) ---
784
--- malformed NF!=13 ---
0
--- tier histogram ---
A=474 B=298 C=12 
--- status histogram ---
mined=689 queued=58 rejected=37 
--- duplicate ids (expect empty) ---
--- enum/tier-inflation (expect empty) ---
```

Histogram totals each equal 784. The duplicate-id and enum/tier-inflation commands produced no output.

## Maintained validator

Ran the requested command:

```sh
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama
```

Complete stdout:

```text
kotodama	W04	S127 duplicate url voices.uchicago.edu/goldinmeadowlab/people/susan-goldin-meadow/research-statement across scopes
kotodama	W04	S128 duplicate url pure.uvt.nl/ws/portalfiles/portal/100130712/Zeshan_deVos_Eds._2012.pdf across scopes
kotodama	W04	S129 duplicate url pmc.ncbi.nlm.nih.gov/articles/PMC10622114 across scopes
kotodama	W04	S130 duplicate url pmc.ncbi.nlm.nih.gov/articles/PMC6818964 across scopes
kotodama	W04	S131 duplicate url link.springer.com/article/10.1186/1477-7517-9-16 across scopes
kotodama	W04	S132 duplicate url ida.gallaudet.edu/cgi/viewcontent.cgi?article=1004&context=sls across scopes
kotodama	W04	S133 duplicate url www.cslds.org/apsl-consortium/sign-linguistics/module-7-sign-phonetics-and-phonology-symmetry-and-dominance-condition across scopes
kotodama	W04	S185 duplicate url www.internationalphoneticassociation.org/icphs-proceedings/ICPhS2003/papers/p15_2131.pdf across scopes
kotodama	W04	S186 duplicate url ich.unesco.org/en/RL/whistled-language-of-the-island-of-la-gomera-canary-islands-the-silbo-gomero-00172 across scopes
kotodama	W04	S358 duplicate url ich.unesco.org/en/RL/mask-dance-of-the-drums-from-drametse-00161 across scopes
kotodama	W04	S482 duplicate url periodicos.ufpb.br/index.php/srh/article/view/13999/7921 across scopes
kotodama	W04	S483 duplicate url web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-church-in-the-kingdom-of-kongo-149117501/2FB5AD22282AF36704DE49E593623693 across scopes
kotodama	W04	S485 duplicate url revistas.usp.br/sankofa/article/view/187402 across scopes
kotodama	W04	S490 duplicate url glottolog.org/resource/languoid/id/kiko1235.json across scopes
kotodama	W04	S561 duplicate url archive.org/download/englishheraldry00bout/englishheraldry00bout_djvu.txt across scopes
kotodama	W04	S564 duplicate url en.maiask.ru/data/documents/13_YatsenkoRogozhinskiiENG.htm across scopes
kotodama	W04	S565 duplicate url ag.colorado.gov/brands/about-brands across scopes
kotodama	W04	S566 duplicate url collections.vam.ac.uk/item/O1053476 across scopes
kotodama	W04	S569 duplicate url www.govinfo.gov/content/pkg/USCODE-2024-title4/html/USCODE-2024-title4-chap1-sec1.htm across scopes
kotodama	W04	S570 duplicate url www.lemondesiffle.free.fr/media/WhistledLanguages_and_Whistled_Speech_Encyclopedy.pdf across scopes
kotodama	W04	S571 duplicate url www.hmongstudiesjournal.org/uploads/4/5/8/7/4587788/hsj-v2n1_morrison.pdf across scopes
kotodama	W04	S572 duplicate url www.icphs2007.de/conference/Papers/1286/1286.pdf across scopes
kotodama	W04	W04	S573 duplicate url archive.mpi.nl/tla/islandora/object/lat:1839_00_0000_0000_0016_B509_0 across scopes
kotodama	W04	S648 duplicate url www.religionswissenschaft.uzh.ch/idd/prepublications/e_idd_pazuzu.pdf across scopes
kotodama	W04	S649 duplicate url www.metmuseum.org/art/collection/search/464456 across scopes
kotodama	W04	S650 duplicate url footwearresearchnetwork.org/articles/concealed-shoes-revealed across scopes
kotodama	W04	S651 duplicate url collections.vam.ac.uk/item/O87367 across scopes
kotodama	W04	S830 duplicate url collection.sciencemuseumgroup.org.uk/objects/co122693/disease-mask-for-healing-rituals across scopes
kotodama	ok	/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md
```

The complete validator stdout above contains 28 W04 warning records and the final `kotodama ok` line. Exit status: `0` (`census_exit=0`). The separately counted W04 records were `28` (`script_exit=0`).

## Observed facts / boundary

- Observed: row count 784; tier histogram A=474, B=298, C=12; status histogram mined=689, queued=58, rejected=37; malformed rows 0; duplicate IDs and enum/tier-inflation output empty; validator exits 0 with W04=28.
- This is a BEFORE snapshot only; no files other than this requested report were changed by this assignment. No tools were installed.
- No CORPUS.md file exists inside the lane's `corpus/` directory; used the fleet-root `/home/vgpnk/Projects/shokunin/CORPUS.md` section named in the assignment.

