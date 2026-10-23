HOLDS

# ReviewRowsA3 — BUILD ATTACK on SOURCES rows S648–S651 (working tree, HEAD 14e6413820d482913f723432b62d566967ccd1a6)

Every assigned check was executed against the lane working tree `corpus/SOURCES.md:603-606`, the committed captures `reports/round-60/captures/`, live fetches I ran myself (`/fast/scratch/hyaku/kotodama-r60a3/ReviewRowsA3/fetches/`), and the locator `reports/round-60/reopen-quote.py` (`to_text`, `locate_in`, `normalise`, `row_target`). No row-level defect found.

## Per-check matrix

| check | S648 | S649 | S650 | S651 |
|---|---|---|---|---|
| 11-cell shape (`split('|')` → 13) | PASS | PASS | PASS | PASS |
| single row, inside `## Registry` (line 26; `## Paths` at 608) | 1 hit | 1 hit | 1 hit | 1 hit |
| first URL byte-equal to mapped row | =S602 | =S616 | =S623 | =S643 |
| extra URLs all Wayback captures of same page | n/a (1 URL) | PASS (wayback 20260610070727id_) | n/a | n/a |
| teaches opens `supersedes <mapped> —`, ≠ mapped teaches | PASS | PASS | PASS | PASS |
| status `mined`, tier A/B, used-by = entry | mined/B/yes | mined/A/yes | mined/B/yes | mined/A/yes |
| quote ≤25 words (normalised) | 23 | 24 | 23 | 18 |
| quote `locate_in` committed capture bytes | True | True | True | True |
| committed capture sha256 = manifest.json | MATCH | MATCH | MATCH | MATCH |
| live fetch bytes sha256 = manifest (I fetched) | MATCH | MATCH | MATCH | MATCH |
| no frozen OLD_PHRASE in scope/anchor/teaches cells | none | none | none | none |
| entry line: exactly 1 hit, not a base line, ≥6 shared content words | 14 | 18 | 9 | 13 |

## Access-note truth (fetched each URL myself, plain GET, desktop UA)

- **S648** `https://www.religionswissenschaft.uzh.ch/idd/prepublications/e_idd_pazuzu.pdf` → HTTP 200, application/pdf, **197,505 bytes**, sha256 `2dafb2a2…` = manifest. Note true.
- **S649** live `https://www.metmuseum.org/art/collection/search/464456` → HTTP **429, 34,222 bytes**; body contains "Vercel Security Checkpoint" + `vercel.link/security-checkpoint` — note "challenge met, not passed" is accurate and honest. Capture URL → HTTP 200, **246,282 bytes**, sha256 `945d52a2…` = manifest.
- **S650** `https://footwearresearchnetwork.org/articles/concealed-shoes-revealed` → HTTP 200, **248,354 bytes**, sha256 `5e353d2f…` = manifest. Note true.
- **S651** `https://collections.vam.ac.uk/item/O87367/` → HTTP 200, **46,556 bytes**, sha256 `8e4cf019…` = manifest. Note true.

## Scope / page-truth attacks

- **S650 teaches second clause** "and that they were connected to notions of good luck and hope" — verbatim `locate_in` in S650.bin = True; "the reason why people concealed shoes remains a mystery" = True (entry line's first clause is also page-carried). Scope cell ("Shawcross's account … including the uncertainty and interpretations") is narrower than the page, not wider.
- **S651 anchor placement claim** ("summary description … after its opening words This amulet case or ga'u of silver and coral (not the Physical description field)"): both strings locate; the capture carries *both* the old S643 quote ("An amulet box or ga'u used to contain rolled prayers … protect the wearer **against** evil") and the new S651 quote ("was used to hold … protect the wearer **from** evil") — they are distinct sentences and the anchor correctly names the summary paragraph. Not a quote swap.
- **S648 scope** matches the paper's statements (quote located inside §I of the PDF via pypdf text, 23 words). Anchor embeds a literal `locate_in: LOCATED <url>` note plus quote — unusual but first-quote extraction still returns the right string.
- **S649** tier A = museum object record, consistent with tiering of S566/S643/S639-style rows; scope narrower than the page (names only the hematite statement, not the gospel-inscription material the rejected S616 scope covered).

## Entry wiring (working-tree entry = L1 candidate byte-for-byte, sha256 `0073da7e…`)

- Cites: line 58 (S648), 70 (S651), 82 (S649), 103 (S650); zero occurrences of S602/S616/S623/S643 anywhere; `grep -cE` for new ids at `reports/round-60/base-entry.md` → 0, none of the four lines is a base line (raw or bare-normalised).
- No frozen OLD_PHRASE in normalised entry (OLDWORD equivalent: clean).

## sources-census.sh validate — full output

```
$ bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama
kotodama	W04	S127 duplicate url voices.uchicago.edu/goldinmeadowlab/people/susan-goldin-meadow/research-statement across scopes
kotodama	W04	S128 duplicate url pure.uvt.nl/ws/portalfiles/portal/100130712/Zeshan_deVos_Eds._2012.pdf across scopes
kotodama	W04	S129 duplicate url pmc.ncbi.nlm.nih.gov/articles/PMC10622114 across scopes
kotodama	W04	S130 duplicate url pmc.ncbi.nlm.nih.gov/articles/PMC6818964 across scopes
kotodama	W04	S131 duplicate url link.springer.com/article/10.1186/1477-7517-9-16 across scopes
kotodama	W04	S132 duplicate url ida.gallaudet.edu/cgi/viewcontent.cgi?article=1004&context=sls across scopes
kotodama	W04	S133 duplicate url www.cslds.org/apsl-consortium/sign-linguistics/module-7-sign-phonetics-and-phonology-symmetry-and-dominance-condition across scopes
kotodama	W04	S185 duplicate url www.internationalphoneticassociation.org/icphs-proceedings/ICPhS2003/papers/p15_2131.pdf across scopes
kotodama	W04	S186 duplicate url ich.unesco.org/en/RL/whistled-language-of-the-island-of-la-gomera-00172 across scopes
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
exit=0
```

Exit 0; all hits are W04 warnings (pre-existing pattern, 23 pre-existing rows flagged). S648–S651's duplicate-URL W04s are the structurally unavoidable consequence of the `supersedes` design (new row must carry the rejected row's page); not errors. Note: the live run truncated S186's URL in my paste above? — no, output shown verbatim; S186 line reads `…la-gomera-00172` in the tool's own output.

## Working-tree diff surface (for L1, out of my row scope)

- `git diff HEAD -- corpus/SOURCES.md` = exactly 4 added lines (S648–S651), 0 removed.
- `git diff HEAD -- corpus/knowledge/…/amulets-…md` = **2 changed lines**: besides the four new-id lines already present, line 51's S640 table cell was reworded from "guarded a woman against infertility and infant death" to "was used to guard against both infertility and infant death" — verbatim-aligned with S640's own anchor quote ("This elaborately detailed amulet from Kerala, Kochi was used to guard against both infertility and infant death."), so it is a *tightening*, but it is an entry-line change outside the four declared restorations; the judged-object bytes will include it. Flagging so the packet key / planted-rows record accounts for it.
- Untracked: `reports/round-60/captures/` (4 .bin + manifest.json; hashes verified above), `reports/round-60/telemetry/pycache-removed-a3.txt`.

## Nits (non-breaking)

- S650 source cell puts URL before citation (every sibling row: citation then URL). Harmless for `row_target` but inconsistent.
- S648 anchor embeds the literal locate URL inside the cell; fine for extraction, adds noise.
- `locate_in` note styles differ across rows (S650 uses backticked `locate_in=True`, S648 spells `LOCATED <url>`); cosmetic.

Verdict: the four rows survive every mechanical and content attack I could mount; access notes are truthful against my own fetches; committed captures are byte-identical to live pages and to the manifest. HOLDS.
