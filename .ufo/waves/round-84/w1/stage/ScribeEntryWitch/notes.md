# ScribeEntryWitch — notes for the claim-D draft

Draft path: `.ufo/waves/round-84/w1/stage/ScribeEntryWitch/witchcraft-sorcery-accusation-institution.md`
Landing path (L1 only): `corpus/knowledge/myth-symbol/witchcraft-sorcery-accusation-institution.md`
Access date for every source below: 2026-11-04. Ordinary plain HTTP GET, no login, no paywall workaround, no challenge met or passed, automation none.

## 1. Which frozen contract this draft targets

- The assignment text this seat received cites frozen commit `3ca2cf288fb593618e0559ea86a36e2dd3110eb8` and the section headings `## 2. The decision table` / `## 4. Attested anchors`.
- The lane tip at the time of writing is `7e6ee2f8` (freeze revision r2, "SOUNDLAW_ERROR shape marker accepts the label constant (fixture-proven, pre-dispatch)"), whose frozen claim D uses `## 2. Six design decisions` / `## 3. Attested anchors`. Freeze r1 (`e160a72e`, "entry section headings aligned to the house shape") introduced those headings; r2 changed only claim O's shape-marker list (verified: `git diff e160a72e 7e6ee2f8 -- reports/round-84/accept-d84.py` is empty and the D block is byte-identical).
- This draft follows the **lane tip's** frozen claim D, because the live wave spec (`.ufo/waves/round-84/spec-v1.json`) and the L1 fixtures both name r1/r2, and the seat prompt itself was regenerated with `## 2. Six design decisions` / `## 3. Attested anchors` in `.ufo/waves/round-84/spec-v1.json`.
- Flag for the L1: a counter run with `--freeze 3ca2cf288fb593618e0559ea86a36e2dd3110eb8` would read the older headings and fail DECISIONS and ANCHORS on this draft. The r1 commit message says the heading change was made pre-dispatch precisely to fix that mismatch; the lane tip is the current contract.

Counter-shape facts measured on the draft with the frozen counter's own leg logic (local replication, no commit):

| leg | measured | floor |
|---|---|---|
| ENTRY bytes | 55,830 | 16,000 |
| SECTIONS | 15 | 7 |
| DECISIONS rows under `## 2. Six design decisions` | 6 | 6 |
| ANCHORS bullets under `## 3. Attested anchors` | 43 | 20 |
| ANCHORS distinct ids | 25 | 4 |
| ANCHORS malformed bullets (zero or two ids) | 0 | 0 |
| LINT | `CITED-LINES: 0 finding(s) in 1 file(s)`, rc 0 | 0 findings |

Header markers are present in the house order (`- topic:`, `- gap filled:`, `- sources:`, `- couples:`, `- source:`, `- verified-at:`, `- recheck:`, `- scope:`).

Note on the ANCHORS leg: the frozen counter's duplicate guard is `found[0] in bad`, where `bad` collects line prefixes rather than ids, so repeated ids are not treated as malformed. This draft does not rely on that leniency: the 43 bullets carry 25 distinct ids, so it passes under a stricter reading as well.

## 2. Sources opened (my own fetch, not the rows' receipts)

| id | URL | HTTP | bytes served | sha256 of served bytes |
|---|---|---|---|---|
| S914 | https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Witchcraft | 200 | 98,968 | `68511af97aaf96f3abaadfcd85af0a9ef2dff0a93cb32c49e2041a14140a0ef4` |
| S915 | https://www.gutenberg.org/cache/epub/22822/pg22822.txt | 200 | 450,230 | `884075101bb1ce9d975faff86d09a6a9851c46560e966ca75d8038b050c003c4` |
| S916 | https://en.wikisource.org/wiki/Malleus_Maleficarum/The_Bull_of_Innocent_VIII | 200 | 73,365 | `cc7b7d31bf089db6df181e1b347daf785736056885b4971352034e40f035b322` |
| S917 | https://www.gutenberg.org/cache/epub/17845/pg17845.txt | 200 | 1,801,648 | `925e3634e0226c4a5378595edccbfbb4386471678c5d5b688784be085aa09539` |

- **S915 substitution, recorded.** The first candidate was `https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Sorcery` (HTTP 200, 60,730 bytes, sha256 `2c4092db343fa6274f3f5edccbb72016cf5e9ead485fd7024b3fc83644a84726`). Its article body is a single short definition paragraph (roughly ninety words: "SORCERY, magic, enchantment, witchcraft; ... derived from the O. Fr. sorcerie ... sortes (see Magic, Divination and Witchcraft)"), not enough for the row's scope. Per the L1's source correction this seat uses Howard Williams, *The Superstitions of Witchcraft* (London: Longman, Green, Longman, Roberts, & Green, 1865), Project Gutenberg eBook #22822, instead. The stub is cited nowhere in the entry.
- **S916 page, recorded.** The Malleus top page is a cover and contents page; the body text present on that page is the table of contents. The Bull subpage named above is the page this seat quotes; the entry's S916 bullets quote only the Bull's own words (crime list, empowerment clause, date).
- S917's edition is Charles Wentworth Upham, *Salem Witchcraft, Volumes I and II*, Project Gutenberg eBook #17845 (release 2006-02-24, most recently updated 2021-10-15). Page locators come from the e-text's own volume/page markers (`[i.190]`, `[i.407]`, `[i.408]`, `[i.410]`, `[i.350]`, `[i.351]`).

### Quote inventory used in the entry

S914 (body extracted from the served HTML; 8 quotes checked, all found):
- opening definition, "malevolent (“black”) magic of women" — opening paragraph;
- "learned product—the result of scholastic and inquisitorial ingenuity" — section "Witchcraft among Primitive Peoples";
- "these admissions, wrung from their victims by rack or thumb-screw, were described as voluntary" — "Further Development", third-period paragraph;
- "the absence of judicial torture made the cases proportionately less numerous" — England paragraph;
- "he pricked the body of the witch to find anaesthetic areas"; "those who did not sink were adjudged guilty"; "One of the most famous witch-finders was Matthew Hopkins, himself hanged for witchcraft after a career of some three years." — same paragraph;
- "The total number of victims ... from 100,000 to several millions" — closing paragraphs.
- Durability fact (source scout, independently re-read): the only Wayback capture of this page (2008-10-06) predates the Wikisource transcription and does not contain the quoted text; the entry therefore makes no capture claim for this row.

S915 (Williams; 3 quotes checked, all found):
- "children of tender years, have been committed to the rack and to the stake on the same accusation which condemned the old and the ugly" — Part II, ch. I ("The Witch-Compact"), the paragraph on the age and sex of the accused;
- "Agnes, the wife of Odo the merchant, accused Gideon of sorcery; and he was acquitted by the judgment of iron" — Part II, ch. II, the paragraph on the earliest English trials;
- "Cupidity or malice was the cause of this informer's accusation" — Part II, ch. II, the paragraph on the De Spencers and John of Nottingham.
- Locator note: the Gutenberg e-text carries no page markers, so these locators are Part + chapter + the paragraph's opening subject, per the source scout's correction; the printed page numbers in the 1865 contents (47, 63) are not verifiable on the served artifact and are not used in the entry.

S916 (Bull; 2 quotes checked, both found):
- "many persons of both sexes, unmindful of their own salvation and straying from the Catholic Faith, have abandoned themselves to devils, incubi and succubi" — printed pp. xliii–xlv, crime paragraph;
- "be empowered to proceed to the just correction, imprisonment, and punishment of any persons, without let or hindrance" — printed pp. xliii–xlv, empowerment clause; the Bull is dated Rome, 9 December 1484.
- Durability facts (source scout, independently re-read): the printed text carries literal ellipses at three points and both quotes end before any of them; there is **no Wayback capture** of the Bull page, and the entry therefore claims none. The manual's own body is not transcribed on Wikisource (its part subpages return 404), so no procedural anchor is attributed to the manual; the entry's S916 material is only what the Bull says (the licence against heresy and maleficium and its date).

S917 (Upham; 6 quotes checked, all found):
- "it did not break the force of the accusation to bring hundreds of witnesses to prove that he was, at the very time, in another remote place" — vol. i, p. 407;
- "If any thing strange or remarkable could be discovered in the persons, histories, or deportment of accused persons" — vol. i, p. 408;
- "When any one was arrested on the charge of witchcraft, a search was immediately made for puppets from garret to cellar" — vol. i, p. 408;
- "their failure to come forth at the bidding of her defamers was regarded as a sure and irrefragable proof of her guilt" — vol. i, p. 410;
- "He instituted prosecutions of Procter and others for defamation, and recovered against them all." — vol. i, p. 190;
- "I declare I am as free of witchcraft as any child; but, being delated by a malicious woman" — vol. ii, p. 350 (quoting Sinclair);
- "being defamed for a witch, she knew she would starve" — vol. ii, p. 351.
- Durability fact (source scout, independently re-read): the 2022 Wayback capture is body-identical to the served text (header/footer-only diff) and carries the quoted spans.

Existing rows (S280, S295, S297, S349, S350, S381, S382, S403, S605, S610, S621, S622, S644, S645, S854, S901, S902, S903, S905, S909, S912): every `「…」` fragment in §3 was checked character-for-character (after whitespace normalisation) against the row's own `anchor` cell in `corpus/SOURCES.md` at the lane tip. Two transcription mismatches were found and fixed (curly vs straight apostrophes in the S621 and S382 quotes). Final check: 43 bullets, 41 quoted fragments, 0 misses.

## 3. Before-state facts re-measured at the base

At `81499ee45b5751d388fefc78583810878de01ecd`:
- `git ls-tree -r --name-only <base> corpus/knowledge | grep -c '\.md$'` = 257;
- `git show <base>:corpus/SOURCES.md | grep -cE '^ {0,3}\| *S[0-9]{3,} *\|'` = 837;
- topic-line owners = 0; filename owners = 0;
- word-boundary occurrences = 19 lines across 11 files.

The entry's `- gap filled:` line states the measured file count (11). The frozen claim's before-text says "19 times across 10 files"; the difference is one file under this seat's sweep. The count of 19 lines agrees; the entry reports its own measurement rather than the claim's rounded one. ScoutGapWitch's census is the independent check.

## 4. Choices made in the draft

- **Structure follows the house shape** used by `guest-right-hospitality-law.md`: §1 partial owners, §2 six design decisions (table), §3 attested anchors, then the topic sections, checklist, worked example, handoff.
- **Every table is id-free.** The §2, §4, §6, §9, §10 tables carry no S-id, so the lane's `TABLE-ID` lint has nothing to flag; §3 is the only place an id appears.
- **No bullet double-cites.** Each §3 bullet names one row; multi-source claims are split into separate bullets or left to prose.
- **The four new rows are cited for their own material.** S914 for the 1911 overview and its English/continental contrast; S915 for Williams's survey (the body-independent charge, the informer's malice, the iron acquittal); S916 only for the Bull's own words; S917 only for Salem procedure and Upham's 1867 narration.
- **Design method is marked as craft.** The six thresholds, the five-slot lexicon, and the worked example are labelled as design defaults or NON-CANON. No sentence attributes them to a source.
- **Boundary compliance.** No claim is made about any living community or person; the two boundary rows are cited as method constraints in §3's last group; the entry contains no accusation procedure and no interrogation script; all historical material is period scholarship with its dates stated in `- recheck:`.

## 5. What this seat did not do

- Did not write `corpus/SOURCES.md` (ScribeRowsWitch/L1 own the four rows) and did not add `used-by` cells.
- Did not commit, push, or run a mutating git/jj command; the L1 lands every byte.
- Did not edit `SKILL.md`, `corpus/QUALITY.md`, `MANIFEST.json`, `.ufo/state/`, or any sibling lane.
- Did not install or upgrade any tool; `curl`, `python3` (stdlib only) and read-only `git` were sufficient. No pacman transaction was attempted.
