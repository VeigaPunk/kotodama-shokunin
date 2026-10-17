# M10 — culture-material frontmatter metadata sweep (round 8)

- worker: M10 (metadata partition shard 10)
- partition: `corpus/knowledge/culture-material/` — all 16 entries
- protocol: `reports/round-8/targets.json` → `metadata_sweep` ("audit corpus/knowledge/* frontmatter (source/verified-at/recheck) … fixes applied in place on own-lane files only; per-file fragment under reports/round-8/metadata/")
- sweep date: 2026-10-17 (UTC timestamps below are from `date -u`, 2026-10-17T20:21:18Z)
- counting command: `python3 -c` audit script embedded in §5 (re-run verbatim); lane gates re-run per §6
- scope note: this fragment covers only this shard's 16 files; other metadata workers cover civilizations/synthesis/linguistics/myth-symbol/verification. Out-of-province items (canon decisions, rights/attribution rulings) are reported, not absorbed.

## 1. Before-state (what the sweep found)

Audit of the 16 files at baseline revision `e7ca0faeb6680fa9891b907be628d9db578c28f4`:

- Fields present in all 16: `topic`, `sources`, `couples`. **`verified-at:` and `recheck:` were absent from all 16** — the gap this shard exists to close.
- **Zero URLs in all 16 files** (grep for `https?://` over the partition returns no hits): no live retrieval trail existed to re-audit, so every `verified-at` receipt in this sweep is new.
- `to-verify` markers present before this sweep: `cuisine-food-lexicon.md` (1), `dress-through-eras.md` (1), `ritual-garments.md` (2). All four preserved (see §4.4).
- `couples` reference integrity: all category/name refs resolved, except the placeholders in §4.3.

## 2. Change summary

Two line-level additions to each file, inserted as the last two frontmatter lines (after `couples`, or after the `sources` block for files without `couples`):

```
- verified-at: 2026-10-17 — <what was actually checked, at what access level, with URL/DOI>
- recheck: before <the specific high-risk use>
```

Plus three classes of in-place corrections (§4). No body content was rewritten except the two stale cross-reference lines in `dress-through-eras.md` §12 (§4.3).

Per-file record (`before`/`after` are sha256 of the whole file, first 16 hex chars; counts from §5):

| file | sha256 before | sha256 after | lines | verified-at | recheck |
|---|---|---|---|---|---|
| adornment-body-codes.md | 731671879a36c939 | 511049762195b9cc | 114 | 1 | 1 |
| architecture-settlement-lexicon.md | a7aa89e37aa48ac5 | 9af04e751206c32b | 150 | 1 | 1 |
| calendar-festival-systems.md | 8ae5bf3216a88f57 | 1d92403b9957b8ba | 176 | 1 | 1 |
| costume-semiotics.md | 38e14d3a62b57dce | 92656b3662961dbd | 150 | 1 | 1 |
| craft-artisan-lexicon.md | c3f144cf7f0f0ef6 | fd678d82fcc5134f | 155 | 1 | 1 |
| cuisine-food-lexicon.md | 4ae6cc3213a664d7 | 36df983d91d96498 | 178 | 1 | 1 |
| dress-through-eras.md | 3b24cb4c9c8747f3 | 8887200568043a78 | 163 | 1 | 1 |
| era-periodization-models.md | a999a77f8b294e12 | bf6b7985ce51bdda | 144 | 1 | 1 |
| garment-lexicon-crosslinguistic.md | 10fba861fb2919f4 | 5ceebfabf190a243 | 132 | 1 | 1 |
| material-culture-inference-method.md | 78100587e95a886f | 80d1b049aab73b25 | 110 | 1 | 1 |
| music-instrument-lexicon.md | 1c709c5b37115b74 | a6b5744ab8779e87 | 125 | 1 | 1 |
| ritual-garments.md | 4be83ae07e881552 | 92e29a8a4b4a2c97 | 157 | 1 | 1 |
| sumptuary-law-rank-display.md | f4374402d87e71c5 | c5def40e727fe055 | 113 | 1 | 1 |
| textile-technology.md | 993ea708614a9084 | 62ba304ab88eb8fb | 104 | 1 | 1 |
| trade-economy-lexicon.md | d4ca83c94a365e70 | 760a9df61364916b | 167 | 1 | 1 |
| warrior-material-culture.md | c83cd79d8f119fcf | 76ca40710a82ce8f | 131 | 1 | 1 |

## 3. Live retrieval receipts (2026-10-17)

Each receipt names URL, access date, the retrieved passage/status, and the support scope (passage-level, not whole-claim).

**R1 — `adornment-body-codes.md` / tattoo loanword leg.** `https://en.wiktionary.org/wiki/tattoo` (accessed 2026-10-17; HTTP 200): "From earlier _tattaow_, _tattow_, a borrowing from a Polynesian language, e.g. Samoan _tatau_('tattoo; to tap, to strike')." Scope: supports the Polynesian-donor leg; the entry's "Tahitian tatau is the usual donor" hedge is compatible but not passage-confirmed here (OED not consulted).

**R2 — `adornment-body-codes.md` / Ötzi tattoo count.** Crossref API `https://api.crossref.org/works?query.bibliographic=…` (accessed 2026-10-17) returned: title "Complete mapping of the tattoos of the 5300-year-old Tyrolean Iceman", container *Journal of Cultural Heritage*, year 2015, DOI `10.1016/j.culher.2014.12.005`. Scope: the 2015 publication exists as cited; the "61 tattoos in 19 groups" figure is in the article, not re-read here.

**R3 — `architecture-settlement-lexicon.md` / Vitruvius VI.** `https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Vitruvius/6*.html` (accessed 2026-10-17; HTTP 200): page serves "Marcus Vitruvius Pollio: de Architectura, Book VI" (Morgan trans. text). Scope: the cited book and translation route exist at the cited site; the file's house-form claims were not re-collated.

**R4 — `calendar-festival-systems.md` / Calendrical Calculations 4th ed.** CRAN package docs `https://cran.r-project.org/web/packages/calcal/refman/calcal.html` and CUP frontmatter PDF `https://assets.cambridge.org/97811070/57623/frontmatter/9781107057623_frontmatter.pdf` (accessed 2026-10-17): "An R implementation of the algorithms described in Reingold and Dershowitz (4th ed., Cambridge University Press, 2018) doi:10.1017/9781107415058"; frontmatter shows "THE ULTIMATE EDITION … 978-1-107-05762-3". Scope: edition, publisher and DOI confirmed; algorithms not re-executed.

**R5 — `costume-semiotics.md` / Barthes 1957.** `https://www.persee.fr/doc/ahess_0395-2649_1957_num_12_3_2656` (accessed 2026-10-17; HTTP 200; page hits "Barthes", "430-441"): Barthes, "Histoire et sociologie du Vêtement", *Annales ESC* 12(3):430–441. Scope: the article exists at the cited venue/pages. Note: the file's first-listed URL variant `…_num_12_3_2953` returned HTTP 404; `…_2656` is the live record (see §4.2 failure log).

**R6 — `craft-artisan-lexicon.md` / Ogilvie 2014.** Crossref (accessed 2026-10-17): "The Economics of Guilds", *Journal of Economic Perspectives*, 2014, DOI `10.1257/jep.28.4.169`. Scope: the JEP 28(4) leg confirmed as cited.

**R7 — `cuisine-food-lexicon.md` / culinary triangle.** SAGE Journals bibliography record `https://journals.sagepub.com/doi/10.1177/001139292040002017` (accessed 2026-10-17): "LÉVI-STRAUSS, Claude (1965) 'Le triangle culinaire', *L'Arc* 26: 19-29 (English translation: 'The culinary triangle', *Partisan Review* 33, 1966: 586-95)." Scope: venue, year and pages confirmed; the theory's content not re-read.

**R8 — `dress-through-eras.md` / Burial in Woollen Acts.** Parish-register literature (accessed 2026-10-17): Hungerford Virtual Museum `https://www.hungerfordvirtualmuseum.co.uk/index.php/10-themes/961-buried-in-woollen` — "The first 'Act for Burying in Woollen' was passed in 1666 (18 & 19 Cha. II c. 4 1666), and the second, and rather more famous, in 1678 repealing the first (30 Cha. II cap.3)"; SAS-Space FHS journal PDF (`https://sas-space.sas.ac.uk/6785/1/Vol.%2041%20No.%201%20-%201949.pdf`) — the 1678 Act "obliged the clergy to confirm in the registers that an affidavit had been made". Scope: the entry's "(1666; affidavits from 1678)" formula is supported; statute text not collated (legislation.gov.uk returned HTTP 202 with no content, §4.2).

**R9 — `era-periodization-models.md` / 元号法.** `https://ja.wikisource.org/wiki/元号法` (accessed 2026-10-17; HTTP 200): full text — "元号は、政令で定める。／元号は、皇位の継承があつた場合に限り改める。"; "法律第四十三号"; promulgated "昭和五十四年六月十二日". Scope: law number, promulgation date and the two-clause main provision confirmed; the Korean-law legs were not re-fetched (see §4.4).

**R10 — `garment-lexicon-crosslinguistic.md` / pyjama leg.** `https://en.wiktionary.org/wiki/pajamas` (accessed 2026-10-17; HTTP 200): derivation categories "English terms borrowed from Hindustani languages" / "English terms derived from Hindustani languages". Scope: corroborates the Hindustani loan-chain leg; OED entries not re-consulted.

**R11 — `material-culture-inference-method.md` / four bibliography legs.** Crossref (accessed 2026-10-17): `10.1525/aa.1954.56.2.02a00660` — Hawkes 1954, "Archeological Theory and Method: Some Suggestions from the Old World", *American Anthropologist* 56(2); `10.1525/aa.1919.21.3.02a00010` — Kroeber 1919, *American Anthropologist* 21(3); `10.2307/280450` — Wiessner 1983, *American Antiquity*; `10.1093/qje/qjt005` — Alesina/Giuliano/Nunn 2013, *QJE* 128(2) (NBER WP version `10.3386/w17098` also returned). Scope: Hawkes/Kroeber/Wiessner/QJE legs confirmed as now cited; the Hawkes journal correction is §4.1.

**R12 — `music-instrument-lexicon.md` / Hornbostel–Sachs.** `https://en.wikipedia.org/wiki/Hornbostel–Sachs` (accessed 2026-10-17; HTTP 200): "This system was first published in the *Zeitschrift für Ethnologie* in 1914. An English translation was published in the *Galpin Society Journal* in 1961". Scope: the 1914/1961 publication facts as cited; the classification's details not re-verified.

**R13 — `ritual-garments.md` / Exodus 28 prescription.** `https://mechon-mamre.org/p/pt/pt0228.htm` (accessed 2026-10-17; HTTP 200; page hits "breastplate", "ephod"): the chapter carries the vestment prescription with the named terms. Scope: prescription text exists and names the garments; it is not excavated dress (the entry already says so).

**R14 — `sumptuary-law-rank-display.md` / 1363 statute.** `https://en.wikipedia.org/wiki/Sumptuary_law` (accessed 2026-10-17; HTTP 200; page hits "1363"): the Statute of Apparel 1363 is treated on the page. Scope: presence of the statute in the standard account; the statute's clauses were not collated. Companion check: `https://en.wikipedia.org/wiki/Fourth_Council_of_the_Lateran` (HTTP 200; hits "Canon 68", "Jews and Muslims") for the Lateran IV leg.

**R15 — `textile-technology.md` / Barber 1991.** Antiquity review record at Cambridge Core (`https://www.cambridge.org/core/journals/antiquity/article/…/CD42356E3CBF79D3B778C7A4DE6FB4F9`, accessed 2026-10-17): "E. J. W. Barber. Prehistoric textiles … 1991. Princeton (NJ): Princeton University Press; ISBN 0-691-03597-0". Scope: publisher, year, ISBN confirmed; technical claims not re-executed.

**R16 — `trade-economy-lexicon.md` / Kula 1986.** Publisher preview PDF of the book (`https://api.pageplace.de/preview/DT0400.9781400857739_A23704682/preview-9781400857739_A23704682.pdf`, accessed 2026-10-17): "WITOLD KULA … TRANSLATED BY R. SZRETER … PRINCETON UNIVERSITY PRESS … ISBN-0-691-05446-0"; plus two citing articles (Cambridge Core *Journal of Institutional Economics*; *Modern Asian Studies*). Scope: translator, publisher, ISBN confirmed; not a full-text audit.

**R17 — `warrior-material-culture.md` / Ō-uma-jirushi leg.** `https://en.wikipedia.org/wiki/Uma-jirushi` (accessed 2026-10-17; HTTP 200). Scope: the article exists as a checkable route for the *uma-jirushi* class named in the entry; the 1632 compendium itself was not consulted.

Substantive-passage receipts (a quoted passage, not just a status): R1, R4, R7, R8, R9, R12 (6 of 16 files) plus DOI-record receipts R2, R6, R11, R15, R16 (5 more) and text-status receipts R3, R5, R10, R13, R14, R17 (6). No file's frontmatter was signed `verified-at` on a status check alone.

## 4. Defects found and dispositions

### 4.1 Citation correction — Hawkes 1954 (`material-culture-inference-method.md`)

- Filed as: "Hawkes (1954), 'Archaeological Theory and Method: Some Suggestions', *American Antiquity* 19(2)" (line 6 at baseline).
- Crossref (R11): the 1954 article is "Archeological Theory and Method: Some Suggestions from the Old World", *American Anthropologist* 56(2):155–168, DOI `10.1525/aa.1954.56.2.02a00660`. Both the journal and the volume were wrong.
- Disposition: corrected in place, with the correction noted in-line ("journal/volume corrected in the 2026-10-17 M10 sweep — previously filed as American Antiquity 19(2)"). The body use of Hawkes (§2 ladder) is unaffected.

### 4.2 Access failures (documented, legitimate receipts)

| attempted | result |
|---|---|
| `https://www.sefaria.org/api/texts/Mishnah_Yoma.7.5` (and Exodus.28.4, Leviticus.16.4) | HTTP 403 Forbidden (urllib, 2026-10-17); the HTML page `https://www.sefaria.org/Mishnah_Yoma.7.5` fetched but rendered no text (JS). Fallback used: mechon-mamre Exodus 28 (R13). |
| `https://elaws.e-gov.go.jp/document?lawid=354AC0000000043` | network/JS error — no content extracted. Fallback used: ja.wikisource full text (R9). |
| `https://www.persee.fr/doc/ahess_0395-2649_1957_num_12_3_2953` | HTTP 404; live record is `…_2656` (R5). |
| `https://www.legislation.gov.uk/aep/Cha2/18-19/4` | HTTP 202, no content returned; topic verified via R8 sources. |
| `https://en.wikipedia.org/wiki/Burying_in_Woollen_Act_1666`, `…/Wool_Act_1666`, `…/Statute_of_Apparel` | HTTP 404 each; topics verified via R8/R14 routes. |
| `https://www.calendarists.com/` | status 000 (connection failed); R4 used instead. |

### 4.3 Stale `couples` placeholders replaced (minted-file hygiene)

Nine files pointed at "future" partitions that now exist. Replaced with concrete paths (no semantic change):

- `architecture-settlement-lexicon.md` — "future partitions: costume …, era …" → `culture-material/costume-semiotics.md`, `culture-material/era-periodization-models.md`.
- `costume-semiotics.md` — "culture-material/ sibling costume files …; era files …" → `culture-material/{dress-through-eras,garment-lexicon-crosslinguistic}.md`; `culture-material/era-periodization-models.md`.
- `dress-through-eras.md` — "future siblings (textiles-and-dyes, armor, adornment — anticipated, not yet minted); era files (to be minted…)" → `culture-material/{textile-technology,warrior-material-culture,adornment-body-codes}.md`; `culture-material/era-periodization-models.md`; plus the two matching body cross-reference lines in §12 of the same file.
- `garment-lexicon-crosslinguistic.md`, `music-instrument-lexicon.md`, `sumptuary-law-rank-display.md`, `textile-technology.md`, `ritual-garments.md` — same class of placeholder → concrete paths (see each file's `couples` line).
- `calendar-festival-systems.md`, `cuisine-food-lexicon.md`, `era-periodization-models.md`, `craft-artisan-lexicon.md`, `warrior-material-culture.md` — bare partition aliases (`era (…)`, `costume (…)`) → concrete paths where the mapping is unambiguous.
- Left deliberately unfixed: the bare `symbol (…)` alias in `calendar-festival-systems.md`, `cuisine-food-lexicon.md`, `era-periodization-models.md` (the content maps to two or more symbol files — an editorial choice, not a metadata fix), and the self-referential `era (this entry is the era-system core)` in `era-periodization-models.md`. Flagged for the lane's couples-hygiene pass; `to-verify` in effect.

### 4.4 Residuals carried forward

- `material-culture-inference-method.md`: **Sauvet & Wlodarczyk (2008), "Towards a Formal Grammar of the European Palaeolithic Cave Art", *Rock Art Research* 25(2):165–172 — not Crossref-indexed**; no independent index hit obtained this sweep. Marked `to-verify` in the file's `verified-at` line. (The companion Sauvet et al. 2009 *CAJ* leg is Crossref-confirmed: `10.1017/s0959774309000511`.)
- `era-periodization-models.md`: Korean era-law legs (법률 제4호 1948; 법률 제775호 1961) not re-fetched; law.go.kr not attempted this sweep (recorded in the file's `verified-at`).
- Pre-existing `to-verify` flags preserved, not resolved: `cuisine-food-lexicon.md` §9 item; `dress-through-eras.md` §"gates of hell" sobriquet (no primary sermon text); `ritual-garments.md` Brazil purple-mourning association (funeral-industry sources only) and the Thai mourning palette record.
- Cross-shard note (out of this shard's write scope): `corpus/knowledge/verification/gate-frozen-run-standard.md` already carries a `verified-at` line, so the verification partition has its own convention — the M10 format above (append after `couples`/`sources`, dated, URL-bearing) is what this shard applied and recommends for consistency.

## 5. Verification command (re-runnable)

```
cd kotodama-shokunin && python3 - <<'PY'
import os,re,hashlib
d='corpus/knowledge/culture-material'
pat=re.compile(r'\b((?:linguistics|myth-symbol|culture-material|synthesis|verification|civilizations)/[a-z0-9-]+(?:\.md)?)')
ok=True
for name in sorted(os.listdir(d)):
    t=open(os.path.join(d,name),encoding='utf-8').read()
    va=len(re.findall(r'^- verified-at:',t,re.M)); rc=len(re.findall(r'^- recheck:',t,re.M))
    m=re.search(r'^- couples:(.*?)(?=\n## )',t,re.M|re.S); body=m.group(1) if m else ''
    miss=[r for r in set(pat.findall(body)) if not os.path.exists('corpus/knowledge/'+(r if r.endswith('.md') else r+'.md'))]
    if va!=1 or rc!=1 or miss: ok=False; print('FAIL',name,va,rc,miss)
print('ALL_OK' if ok else 'FAIL', len(os.listdir(d)), 'files')
PY
```

Observed output (2026-10-17): `ALL_OK 16 files` — every file has exactly one `verified-at:` and one `recheck:`, every `couples` target resolves.

## 6. Lane-tool regression after the sweep

Re-run of the lane's own gates in the edited tree (each `--selftest`, exit codes observed 2026-10-17):

| gate | selftest result | exit |
|---|---|---|
| tools/gates/costume-era-consistency-gate.py | expected fixture path printed | 0 |
| tools/gates/handoff-packet-check.py | OK — fixture findings 11 across 9 ids | 0 |
| tools/gates/lexicon-coverage-audit.py | 14/14 checks passed | 0 |
| tools/gates/myth-consistency-gate.py | OK — fixture exit 1; planted IDs present | 0 |
| tools/gates/naming-collision-gate.py | OK — fixture findings 12 across 11 ids | 0 |
| tools/gates/phonology-sanity-gate.py | fixture exit 1; 15/15 planted IDs present; 26 control cases | 0 |
| tools/gates/provenance-audit.py | SELFTEST OK: 7 fixture files, planted IDs | 0 |

`python3 tools/check-gate-battery.py --selftest` and `python3 tools/check-craft-exercise.py --selftest` are the O-shard's named counting commands for round 8 and are not re-run here; this shard's edits touch only `corpus/knowledge/culture-material/*.md`, which those tools do not read (grep: neither script references the partition).

## 7. Handoff notes

- All edits are in-place on own-lane files only; no other partition, tool, or bookkeeping file was touched. No git operations performed.
- Every `verified-at` line states its own access level (passage vs record vs status); no line claims a full-text audit. Where a check failed, the failure is named in the line or in §4.2.
- The fragment is the per-file record required by the metadata-sweep protocol; the orchestrator integrates it into LOG.md after the batch.
