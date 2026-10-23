HOLDS

Axes attacked: (1) `sources-census.sh validate` exit on lane `kotodama`, (2) S648–S651 11-cell registry shape at the lane tip, (3) those rows `mined` with used-by the amulets entry, (4) S602 S616 S623 S643 still `rejected` with used-by U+2014, (5) worktree `corpus/SOURCES.md` identical to the tip blob. No axis broke. No tools installed.

Lane tip is detached HEAD = `main` = `origin/main` = frozen declaration `47f27bd0cb0bea219f21cd731c2eb0fe71f7f626`. `corpus/SOURCES.md` blob `4365188c2ae344bd6ecad5f291ef9fc04197c180` matches `git hash-object` of the worktree file; `git diff --numstat HEAD` on that file and the amulets entry is empty. Each of the eight ids is one `| Snnn |` row inside `## Registry` (the second SOURCES hit for S602/S616/S623/S643 is only the later row's `supersedes` teaches). Header is the 11-column contract row (`id source kind tier scope anchor teaches status opened recheck used-by`). Census splits on `|` (`gawk -F'|'`): 11 cells means NF=13. None of these eight rows emitted E01. Validator exit is 0 (`ok`); W04 is defined as non-failing.

S648 line 603, S649 line 604, S650 line 605, S651 line 606: split length 13 (11 cells), status `mined`, tier B/A/B/A, used-by exactly `corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md` (that file exists, 22304 bytes). S602 line 557, S616 line 571, S623 line 578, S643 line 598: split length 13, status `rejected`, used-by cell codepoints `20 2014 20` (trimmed em dash `—`, the census unused sentinel).

W04 on S648–S651 is the same page URL as the rejected predecessor under a different scope string (W04, not E04). Teaches on the new rows also match `supersedes Snnn`, which is the within-scope duplicate exemption, but the scopes differ so E04 does not apply. Not a shape, status, or used-by miss.

Entry citations at this same tip (sha256 `36bd628b6af6a9e62e2cbeb2a51f32032e8f5837705f25f25c9aceaca6f770e2`, the freeze judged-object hash): S648, S649, S650, S651 once each; S602, S616, S623, S643 zero. Consistent with used-by, not a census miss.

## Command: tip identity

```
timeout 30 git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin rev-parse HEAD && timeout 30 git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin log -1 --format='%H%n%s%n%ci' && timeout 30 git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin rev-parse 47f27bd0cb0bea219f21cd731c2eb0fe71f7f626 && timeout 30 git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin merge-base --is-ancestor 47f27bd0cb0bea219f21cd731c2eb0fe71f7f626 HEAD; echo "ancestor_exit=$?" && timeout 30 git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin branch -vv --no-color && timeout 30 git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin status --porcelain=v1 -b
```

```
47f27bd0cb0bea219f21cd731c2eb0fe71f7f626
47f27bd0cb0bea219f21cd731c2eb0fe71f7f626
round-60: FREEZE (claim D, before any data seat) — freeze_note; packet-key hash (key built from the 1cd9db7c entry, kept outside the lane until the support wave settles); revision-9 residual re-score receipts (NONE-MET); records: SCORECARD and LOG round-59 corrections, round-59 errata, QUALITY criterion 14, round-60 lesson (pre-data parts)
2026-10-23 04:50:34 -0300
47f27bd0cb0bea219f21cd731c2eb0fe71f7f626
ancestor_exit=0
* (no branch)                  47f27bd round-60: FREEZE (claim D, before any data seat) — freeze_note; packet-key hash (key built from the 1cd9db7c entry, kept outside the lane until the support wave settles); revision-9 residual re-score receipts (NONE-MET); records: SCORECARD and LOG round-59 corrections, round-59 errata, QUALITY criterion 14, round-60 lesson (pre-data parts)
  main                         47f27bd [origin/main] round-60: FREEZE (claim D, before any data seat) — freeze_note; packet-key hash (key built from the 1cd9db7c entry, kept outside the lane until the support wave settles); revision-9 residual re-score receipts (NONE-MET); records: SCORECARD and LOG round-59 corrections, round-59 errata, QUALITY criterion 14, round-60 lesson (pre-data parts)
+ hyaku/s3-kotodama-r51-author bff83ba (/fast/scratch/hyaku/kotodama-r51-author) round-50 verifier spot-check: original separability self-application unmet
+ hyaku/s3-ready66-kotodama    bff83ba (/fast/scratch/hyaku/s3-ready66/kotodama-shokunin) round-50 verifier spot-check: original separability self-application unmet
## HEAD (no branch)
?? .ufo/waves/round-60/build-spec.json
?? .ufo/waves/round-60/build/
?? .ufo/waves/round-60/gen-build-spec.py
?? .ufo/waves/round-60/gen-support-spec.py
?? .ufo/waves/round-60/support-a3-spec.json
?? .ufo/waves/round-60/support/
```

## Command: validate (full stdout, exit 0)

```
timeout 180 /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama; echo "EXIT:$?"
```

```
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
kotodama	W04	S573 duplicate url archive.mpi.nl/tla/islandora/object/lat:1839_00_0000_0000_0016_B509_0 across scopes
kotodama	W04	S648 duplicate url www.religionswissenschaft.uzh.ch/idd/prepublications/e_idd_pazuzu.pdf across scopes
kotodama	W04	S649 duplicate url www.metmuseum.org/art/collection/search/464456 across scopes
kotodama	W04	S650 duplicate url footwearresearchnetwork.org/articles/concealed-shoes-revealed across scopes
kotodama	W04	S651 duplicate url collections.vam.ac.uk/item/O87367 across scopes
kotodama	ok	/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md
EXIT:0
```

## Command: blob identity, dash codepoints, citation counts

```
timeout 20 git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin rev-parse HEAD:corpus/SOURCES.md
timeout 20 git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin hash-object /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md
timeout 20 git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin diff --numstat HEAD -- corpus/SOURCES.md corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md
ls -l /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md
timeout 20 git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin branch -a --contains HEAD
timeout 20 git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show-ref --heads --dereference
```

```
=== HEAD blob vs worktree ===
4365188c2ae344bd6ecad5f291ef9fc04197c180
4365188c2ae344bd6ecad5f291ef9fc04197c180
=== diff stat SOURCES vs HEAD ===
=== entry exists ===
-rw-r--r-- 1 vgpnk vgpnk 22304 Oct 23 04:12 /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md
=== branches containing HEAD ===
* (no branch)
  main
  remotes/origin/HEAD -> origin/main
  remotes/origin/main
=== refs at tip ===
bff83ba65bf9559af4d7567e81703059667a0005 refs/heads/hyaku/s3-kotodama-r51-author
bff83ba65bf9559af4d7567e81703059667a0005 refs/heads/hyaku/s3-ready66-kotodama
47f27bd0cb0bea219f21cd731c2eb0fe71f7f626 refs/heads/main
ENTRY_CITES
S648 1
S649 1
S650 1
S651 1
S602 0
S616 0
S623 0
S643 0
SOURCES_ID_LINE_HITS
S648 [(603, '|', '| S648 |', 11)]
S649 [(604, '|', '| S649 |', 11)]
S650 [(605, '|', '| S650 |', 11)]
S651 [(606, '|', '| S651 |', 11)]
S602 [(557, '|', '| S602 |', 11), (603, '|', '| S648 |', 11)]
S616 [(571, '|', '| S616 |', 11), (604, '|', '| S649 |', 11)]
S623 [(578, '|', '| S623 |', 11), (605, '|', '| S650 |', 11)]
S643 [(598, '|', '| S643 |', 11), (606, '|', '| S651 |', 11)]
DASH_CODEPOINTS
S602 ['0x20', '0x2014', '0x20'] ' — '
S616 ['0x20', '0x2014', '0x20'] ' — '
S623 ['0x20', '0x2014', '0x20'] ' — '
S643 ['0x20', '0x2014', '0x20'] ' — '
S648 ['0x20', '0x63', '0x6f', '0x72', '0x70', '0x75', '0x73', '0x2f', '0x6b', '0x6e', '0x6f', '0x77', '0x6c', '0x65', '0x64', '0x67', '0x65', '0x2f', '0x6d', '0x79', '0x74', '0x68', '0x2d', '0x73', '0x79', '0x6d', '0x62', '0x6f', '0x6c', '0x2f', '0x61', '0x6d', '0x75', '0x6c', '0x65', '0x74', '0x73', '0x2d', '0x74', '0x61', '0x6c', '0x69', '0x73', '0x6d', '0x61', '0x6e', '0x73', '0x2d', '0x61', '0x70', '0x6f', '0x74', '0x72', '0x6f', '0x70', '0x61', '0x69', '0x63', '0x2d', '0x6d', '0x61', '0x72', '0x6b', '0x73', '0x2e', '0x6d', '0x64', '0x20'] ' corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md '
ENTRY_SHA 36bd628b6af6a9e62e2cbeb2a51f32032e8f5837705f25f25c9aceaca6f770e2
ENTRY_BYTES 22304
```

Cell parse (same file, `str.split('|')`; status and used-by trimmed): S648/S649/S650/S651 status `mined`, used-by the amulets path above; S602/S616/S623/S643 status `rejected`, used-by `—`. No other registry row for these ids. Confidence: high. Unresolved: none on this census check.
