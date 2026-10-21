# ReopenS060 — attack on SOURCES row S060 (Ahearn 2018, *Natural Hazards*)

Seat: `KotodamaR50-2.ReopenS060-21` (leaf, read-only). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Landed target: `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` (base `4ad26836552462d28a946ca3b067cab0b5ce3532`).
All lane bytes below read with `git show <sha>:<path>`; working tree not trusted. No lane edits, no git/jj writes.

## Verdict

**PARTIAL.** The URL opens, the Gate quote is verbatim at the stated section and PDF page, tier A is honest for the
row's stated scope under `corpus/QUALITY.md:29` (criterion 6), and the row's two risk-management claims are carried by
the paper. But the row's bibliographic page range is **false** (`92(Suppl 1):95–107`; publisher metadata and the PDF's
17 pages say **165–181**), and two entry citations overreach the source: `:47` attributes "species mix" as a hedge to
S060, which the paper never says, and `:67`'s "emic portfolio term" is not asserted by Ahearn (the round's own
directly-attesting companion source was opened but never registered). `:78` holds. Bounded fixes below.

## Evidence

### 1. URL opened this session

```
$ curl -sS -L -o ahearn2018.pdf -w 'HTTP %{http_code} type=%{content_type} size=%{size_download} url=%{url_effective}\n' \
    'https://d-nb.info/1152169939/34'
HTTP 200 type=application/pdf;charset=base64 size=979718 url=https://d-nb.info/1152169939/34
$ sha256sum ahearn2018.pdf
8f371366a6f3f67bf532ea1fa05cbcb855d1cdc04498fc72905cae537224ed3a  ahearn2018.pdf
$ pdfinfo ahearn2018.pdf
Title:    Herders and hazards: covariate dzud risk and the cost of risk management strategies in a Mongolian subdistrict
Subject:  Natural Hazards, https://doi.org/10.1007/s11069-017-3128-4
Author:   Ariell Ahearn
Creator:  Springer
Pages:    17
```

The fetched artifact is the publisher's open-access version, not a landing page or a different paper. `file(1)` prints
"10 page(s)" for this PDF; that libmagic count disagrees with `pdfinfo` and with `pdftotext` (page 17 is the end of the
reference list), so this report uses **17 pages**. DOI resolves live:
`https://doi.org/10.1007/s11069-017-3128-4` → `https://link.springer.com/article/10.1007/s11069-017-3128-4`, HTTP 200.

### 2. Gate quote is verbatim at the stated location

Gate bullet, `corpus/lessons/round-50.md:45`:

> S060 — https://d-nb.info/1152169939/34 — accessed 2026-10-21 — §2 Bayankhongor province ¶2 (PDF p. 4): “an aggregate of the “five snouts” represented by horses, yaks/cattle, camel, goats and sheep”. Seat: SrcMongolFiveSnouts.

Page-confined check (`pdftotext -f 4 -l 4`, whitespace-normalized):

```
$ python3 - <<'EOF'
import subprocess,re
p4=subprocess.run(['pdftotext','-f','4','-l','4','-layout','ahearn2018.pdf','-'],capture_output=True,text=True).stdout
n=re.sub(r'\s+',' ',p4)
q='an aggregate of the “five snouts” represented by horses, yaks/cattle, camel, goats and sheep'
print(q in n)
EOF
True
```

Context on PDF p. 4: “In Bayankhongor, the total herd count for 2012 was 2,640,831 head of livestock, **which is an
aggregate of the “five snouts” represented by horses, yaks/cattle, camel, goats and sheep** (National Statistical
Yearbook 2013, p. 212).” The §2 heading and ¶1 open on PDF p. 3; the quoted paragraph is §2 ¶2, landing on p. 4 — the
row and Gate locate it correctly. Access date 2026-10-21 matches today.

### 3. Row fields, `corpus/SOURCES.md:89`

- **source / title / journal / DOI / author / year** — correct. Springer metadata: `citation_title` matches, `citation_author`
  "Ahearn, Ariell", `citation_journal_title` "Natural Hazards", `citation_publication_date` "2018/11", DOI
  `10.1007/s11069-017-3128-4`.
- **pages — WRONG.** The row says `92(Suppl 1):95–107`. Four independent records say **165–181**:
  - Crossref `api.crossref.org/works/10.1007/s11069-017-3128-4`: `volume 92 issue S1 page 165-181`, `published-print 2018-11`;
  - OpenAlex `biblio`: `{volume 92, issue S1, first_page 165, last_page 181}`;
  - Semantic Scholar Graph API: `journal.pages "165-181"`, `volume "92"`;
  - Springer article page: `citation_firstpage 165`, `citation_lastpage 181`.
  The PDF itself is 17 pages — exactly 181−165+1 — while 95–107 would be 13. The build seat's own caveat records where the
  error came from: `.ufo/waves/round-50/build/SrcMongolFiveSnouts.md:151` — "Volume/pages (92 Suppl 1:95–107, 2018) come
  from the search metadata and the PDF header/DOI, not from the landing page." The PDF header carries the DOI but no page
  range; the pages were never checked against the publisher record.
- **kind** `paper` — correct. **tier A** — correct: original peer-reviewed open-access research, full text, and the
  row's scope explicitly bounds the statistic as *reported from* the National Statistical Yearbook 2013 (not re-derived).
  Not a publisher description or abstract, so criterion 6's B rule does not apply.
- **scope / anchor / status / opened / recheck / used-by** — honest. `mined` path exists and cites the row; 365d cadence
  is consistent with the round.
- **teaches** — two of three clauses hold (below); the "emic" qualifier does not.

Note on checkability: this DNB copy carries no printed page numbers (every page footer shows only the Springer "13" mark),
so the page range cannot be checked from the linked PDF alone. Publisher metadata is the only route, and it contradicts
the row.

### 4. Every `S060` citation in the knowledge entry

Census at the landed commit (`git grep -n 'S060' 1c779e4…`): entry `:7`, `:47`, `:67`, `:78`; `corpus/SOURCES.md:89`;
`corpus/lessons/round-50.md:45`.

| line | text (abridged) | support |
|---|---|---|
| `:7` | external-shelf list: "S060 Ahearn 2018 (Mongolian 'five snouts')" | bibliographic only; correct |
| `:47` | §3 typology, Nomadic row, risk strategy: "**species mix and movement are the hedge (S060)**" | **PARTIAL.** Movement is supported: the paper's winter-preparation list opens "Conduct otor migrations by using a smaller ger to move more frequently to access available pasture" (extraction line 489), and §3 frames "moving away from drought-stricken areas" as risk-averse practice under the high-reliability model (lines 291–292). **Species mix is not.** The paper's only species sentence is the five-snouts aggregate (lines 188–189); its documented splitting is "Herd livestock in separate groups **depending on age and health**" (line 524) and "Split up livestock herd and distribute to other families, sometimes to other soum" (line 525). No species diversification anywhere in the paper (`grep -n -i 'species'` returns only the aggregate line). |
| `:67` | "The Mongolian 'five snouts' — horses, yaks/cattle, camel, goats and sheep — is an **emic portfolio term** (S060)" | **PARTIAL.** The five-species list is exact. "Emic" is not in the paper (`grep -n -i 'emic'` → 0 hits); Ahearn presents it as "an aggregate of the 'five snouts'" **as reported in the National Statistical Yearbook 2013**, i.e. a statistical category, not an attested herders' usage. The build seat knew this and proposed a separate "direct emic-term attestation" — Chuluunbaatar 2012, *The Camel and its Symbolism…*, quote "all together they were – and still are – called the 'five snouts' (tavan xošū mal)" (build report lines 37–49). That source is **not in the landed registry** (`git grep` for Chuluunbaatar / tavan → none; final S049 is the FAO chapter) and is not in the "Opened but not registered" list at `corpus/SOURCES.md:142`. |
| `:78` | §5 table: "'five snouts' as one collective term (S060)" | **HOLDS** — "an aggregate of the 'five snouts' represented by horses, yaks/cattle, camel, goats and sheep". |

Adjacent, same table row as `:47`: the Labour cell "household herding; **splitting by species and age**" (no citation
marker) repeats the same mismatch — the paper splits by age and health (line 524), not by species.

### 5. Row `teaches` remaining claims

- "reliability-seeking risk management" — supported: abstract "high-reliability seekers rather than risk-averse" (line 24),
  §1 "high-reliability seekers rather than risk-averse" (line 86) and "reliability-seeking producers" (line 142),
  conclusion (line 676).
- "covariate dzud risk limits risk sharing" — supported: §1 "Covariate risk affects a large population at the same time
  (Vatsa and Krimgold 2000), compromising the effectiveness of mutual aid networks used to address more idiosyncratic
  risks" (lines 93–95); §4 "Traditional mutual help networks are also constrained during covariate natural hazard events"
  (lines 552–553).

## Smallest fix

1. **Pages (required).** Per the SOURCES preamble's append-only rule (`corpus/SOURCES.md:9–12`), do not rewrite S060's
   source cell in place. Append a superseding row (next free id — rows end at S069) whose `teaches` opens
   `supersedes S060 —`, carrying `Natural Hazards 92(Suppl 1):165–181` and the same DOI/URL/anchor; log the supersession
   in a round lesson per the contract. (If the lane treats page metadata as outside append-only, the minimum is still
   the corrected range in a new row, never a silent in-place edit.)
2. **`:47`.** Rewrite to what the source carries: "movement and herd-splitting are the hedge (S060)" — or
   "movement is the hedge (S060); species mix `(to-verify)`" — and correct the Labour cell "splitting by species and age"
   → "splitting by age and health (S060)".
3. **`:67`.** Either register the already-opened Chuluunbaatar 2012 attestation (re-open its URL before landing; the build
   report's quote is not itself evidence) and cite it for "emic", or drop the qualifier and write "the statistical
   aggregate called the 'five snouts' (S060)". Do not leave "emic" standing on S060 alone.

## Limits

- No installs, no pacman/uv/npx use; nothing to record under the tooling directive.
- The National Statistical Yearbook 2013 was not opened; the 2,640,831 figure is as-reported by Ahearn.
- Chuluunbaatar 2012 was not opened by this seat; the build report's quote is recorded only to locate the missing
  attestation, not as verified evidence.
- The page-range check rests on publisher metadata (Crossref/OpenAlex/Semantic Scholar/Springer) plus the PDF's 17-page
  extent; the DNB copy itself prints no page numbers.
- No clone was needed (`git show` sufficed). `/tmp/ahearn2018.pdf`, its text extraction, and the fetched HTML pages were
  deleted after the checks. Only this report was written.
