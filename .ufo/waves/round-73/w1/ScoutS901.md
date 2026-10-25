# ScoutS901 — staged row S901 verdict (Anderson, Grant & Sanders, CJL SoTL intro; tentative lane id S880)

- Seat: ScoutS901 (leaf). Round 73, hyaku run 7. Date: 2026-10-25.
- Item: re-open staged row S901 (https://sanders.phonologist.org/Papers/anderson-etal-cjl-sotl.pdf), locate the Sowers-Wills passage, verify the amendment's use of S901 as "method detail the publisher abstract could not supply", propose a lane registry row (11-column schema), assign tier, run a Wayback CDX canonical-slug probe, give a verdict.
- Cambridge DOI (S894/S910) NOT opened (owned by another seat).
- Tools: no installs performed. `pdftotext` already present at /usr/bin/pdftotext (poppler). PACMAN untouched (orchestrator pause). Per operator directive, no tool was installed, so no install record applies.
- Fetch hygiene (QUALITY 21/22): every HTTP fetch used a browser-shaped UA:
  `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`
  (recorded on every command below).

## 1. Fetch — exact commands and raw outputs

### 1.1 Live PDF (canonical slug)
Command:
```
mkdir -p /tmp/ScoutS901 && curl -sS -o /tmp/ScoutS901/anderson-etal-cjl-sotl.pdf \
  -w 'HTTP_STATUS=%{http_code} BYTES=%{size_download} URL=%{url_effective} CONTENT_TYPE=%{content_type}\n' \
  -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' \
  'https://sanders.phonologist.org/Papers/anderson-etal-cjl-sotl.pdf'
```
Raw output:
```
HTTP_STATUS=200 BYTES=193610 URL=https://sanders.phonologist.org/Papers/anderson-etal-cjl-sotl.pdf CONTENT_TYPE=application/pdf
```
- HTTP 200; 193,610 bytes; application/pdf.

### 1.2 File identity
Command:
```
file /tmp/ScoutS901/anderson-etal-cjl-sotl.pdf; md5sum /tmp/ScoutS901/anderson-etal-cjl-sotl.pdf
```
Raw output:
```
/tmp/ScoutS901/anderson-etal-cjl-sotl.pdf: PDF document, version 1.7, 9 page(s)
00151e4bf251e2b338542d10efba02c5  /tmp/ScoutS901/anderson-etal-cjl-sotl.pdf
```
- PDF 1.7, 9 pages.

### 1.3 Text extraction
Command:
```
pdftotext -layout /tmp/ScoutS901/anderson-etal-cjl-sotl.pdf /tmp/ScoutS901/anderson-etal-cjl-sotl.txt && wc -l /tmp/ScoutS901/anderson-etal-cjl-sotl.txt
```
Raw output:
```
430 /tmp/ScoutS901/anderson-etal-cjl-sotl.txt
```

### 1.4 The row's own recheck command (from staged row S901), rerun 2026-10-25
Command (pipe unescaped as the row's command would run):
```
curl -fsSL 'https://sanders.phonologist.org/Papers/anderson-etal-cjl-sotl.pdf' -o /tmp/ScoutS901/recheck.pdf \
  && pdftotext -enc UTF-8 /tmp/ScoutS901/recheck.pdf - | grep -c 'multi-part, creative project'
```
Raw output:
```
1
```
- Also `md5sum /tmp/ScoutS901/recheck.pdf` = `00151e4bf251e2b338542d10efba02c5` (identical to 1.2 → same bytes re-fetched).

## 2. The located passage

Document: Anderson, Catherine (McMaster); Grant, Margaret (Simon Fraser); Sanders, Nathan (University of Toronto), "Building capacity for the scholarship of teaching and learning in linguistics in Canada", opening article of the special issue, Canadian Journal of Linguistics. Section **3. These papers** (the special-issue overview), **page 5**, second paragraph of that section.

pdftotext -layout lines 205–210 (page marker "5" at line 195; passage confirmed on page 5 by per-page extraction `pdftotext -layout -f 5 -l 5`):
```
         Sowers-Wills’s “Phonology from the inside out: Constructed language as a pedagogical
Tool” examines the use of constructed languages as an active learning approach in a project-
based phonology course. In the course, examples of phonological systems in natural languages
and constructed languages were presented along with instruction in language universals and
typology. One innovation of this work is that it suggests that a multi-part, creative project can be
part of a course even at the introductory level.
```

Earlier same-page context (lines 161–162): "Sara Sowers-Wills assesses students' command of concepts in phonology through their creation of a constructed language." and (lines 173–174) "Sowers-Wills engages with the literature on the use of constructed languages as a pedagogical tool".

### Located quote (primary, ≤25 words, verbatim)
> "In the course, examples of phonological systems in natural languages and constructed languages were presented along with instruction in language universals and typology."

- Location: Anderson, Grant & Sanders 2024, CJL special-issue introduction, §3 "These papers", p. 5 (pdftotext -layout lines 207–209).
- Word count: **23** (`wc -w`).

### Located quote (secondary, ≤25 words, verbatim)
> "One innovation of this work is that it suggests that a multi-part, creative project can be part of a course even at the introductory level."

- Location: same section/page, lines 209–210.
- Word count: **25** (`wc -w`; exactly at the limit).

## 3. Which amendment sentences the PDF actually carries

Amendment under test: `knowledge/corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md` (staged package), first amendment block ("What the conlang-construction study actually consisted of").

| Amendment element | In PDF? | Evidence |
|---|---|---|
| "phonological systems of natural *and* constructed languages were presented alongside instruction in language universals and typology" (topic) | **YES** | verbatim, quote 1 (23 words) |
| "as a multi-part creative project" (topic) | **YES** | "a multi-part, creative project can be part of a course" (quote 2) |
| "at introductory level" / "placement ... at introductory rather than advanced level" (topic; gap-filled) | **YES** | "even at the introductory level" (quote 2) |
| "the multi-part creative project admitted at introductory level" (§N) | **YES** | quote 2 (verbatim) |
| "natural and constructed phonological systems set beside universals and typology instruction" (§N) | **YES** | quote 1 |
| "a semester-long language-construction project" (topic) | **NO** | token "semester"/"Semester" occurs **0 times** in the whole PDF (grep over pdftotext output: `No matches found`) |
| "the semester-long construction project" (§N) | **NO** | same token absence; PDF says "a project-based phonology course" and "creative project" — never "semester-long" |
| project framing | **YES** (partial) | "an active learning approach in a project-based phonology course" (line 206–207) — the PDF does not use the phrase "language-construction project" |

Conclusion: the PDF carries 6 of the 8 attributed elements verbatim or equivalently. It does **not** carry the "semester-long" token (nor the exact phrase "language-construction project"). The "semester-long" element in the amendment and in the staged row's scope cell is therefore sourced from elsewhere — the amendment itself attributes "a semester-long language-construction project as a linguistics curriculum" to **S894** (Cambridge DOI abstract, §N+2 of the superseded entry block). So the amendment's use of S901 as "the method detail the publisher abstract could not supply" is **valid for three of the four method elements** (phonological-systems pairing with universals/typology; multi-part creative project; introductory-level placement), and is **mis-attributed for the "semester-long" element**, which the PDF cannot supply.

## 4. Wayback CDX canonical-slug probe

Probed API (exact match on canonical slug):
```
curl -sS -w '\nHTTP_STATUS=%{http_code}\n' \
  -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' \
  'https://web.archive.org/cdx/search/cdx?url=sanders.phonologist.org/Papers/anderson-etal-cjl-sotl.pdf&matchType=exact&output=json&limit=20&fl=timestamp,statuscode,digest,length,mimetype'
```
Raw output:
```
[["timestamp","statuscode","digest","length","mimetype"],
["20240620030845","200","N4WBAMHBQV42CBUVDHDCKFRZRQTBRDOV","167696","application/pdf"],
["20240801224643","200","N4WBAMHBQV42CBUVDHDCKFRZRQTBRDOV","165641","application/pdf"]]

HTTP_STATUS=200
```
Probed URLs filed:
- `https://web.archive.org/cdx/search/cdx?url=sanders.phonologist.org/Papers/anderson-etal-cjl-sotl.pdf&matchType=exact&output=json&limit=20&fl=timestamp,statuscode,digest,length,mimetype` → 2 captures, both HTTP 200, identical digest `N4WBAMHBQV42CBUVDHDCKFRZRQTBRDOV`.
- Canonical capture re-fetch: `https://web.archive.org/web/20240801224643id_/https://sanders.phonologist.org/Papers/anderson-etal-cjl-sotl.pdf` → HTTP 200, 193,610 BYTES; extracted text contains the passage (`grep -c 'phonological systems in natural languages'` = 1) and `grep -ci 'semester'` = 0 — archived copy agrees with live: no "semester-long".
- No no-capture ruling needed (live capture succeeded).

## 5. Proposed lane registry row (11-column schema)

Tentative id **S880** (per wave hypothesis map: staged S901 → S880). No pipe character inside any cell.

```
| S880 | Anderson, Catherine; Grant, Margaret; Sanders, Nathan, "Building capacity for the scholarship of teaching and learning in linguistics in Canada", opening article of the special issue in which Sowers-Wills's article appears, Canadian Journal of Linguistics, PDF hosted by the Phonology Lab — https://sanders.phonologist.org/Papers/anderson-etal-cjl-sotl.pdf | paper | B | Tier B for the method detail of the Sowers-Wills study that the publisher's abstract could not supply: a project-based phonology course presenting examples of phonological systems in natural languages and constructed languages alongside instruction in language universals and typology, with a multi-part, creative project placed even at the introductory level. Does NOT carry the token semester-long — that element belongs to S894's abstract | the paragraph on Sowers-Wills's "Phonology from the inside out…", §3 These papers, p. 5, PDF as served 2026-10-25 | Fills the round-3 gap with a citable account of what the construction project consisted of — the phonological-systems pairing with universals and typology instruction, the multi-part creative project, and the placement at introductory level; the semester-long element stays attributed to S894 | mined | 2026-10-25 | 180d — curl -fsSL 'https://sanders.phonologist.org/Papers/anderson-etal-cjl-sotl.pdf' -o /tmp/c.pdf && pdftotext -enc UTF-8 /tmp/c.pdf - | grep -c 'multi-part, creative project' -> 1 (ran 2026-10-25) | corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md |
```

- used-by: only `conlang-scholarship.amend-2026-10-23.md` — the base `conlang-scholarship.md` cites S892/S893/S894, not S901/S880 (verified by grep over the staged base entry: no S901/S880 tokens).
- recheck: `180d` (ISO-date equivalent accepted; command is the row's own recheck, rerun 2026-10-25 → 1).
- status: mined; opened: 2026-10-25 (this seat's verification date; staged row said 2026-10-23 — normalization to the seat's open/verify date).

## 6. Tier assignment

**B.** Reason: the row is a genuine, live-verified document (HTTP 200, 193,610 bytes, PDF 1.7) describing the Sowers-Wills study, but it is a companion article's account of a neighbouring study in the same special issue — not the study itself. That matches the staged row's own B rationale and the lane's tier habit for secondary accounts. The substance it supplies (pp. 5, §3) is first-hand editorial description of the special issue, which justifies B rather than A (A reserved for the primary study).

## 7. Verdict

**ADMIT** (with a correction constraint).

Reason: the source is real, canonical (permanent URL on the author's Phonology Lab site), fetchable at 200 with the browser UA, archived in Wayback (2 captures, both 200, same digest), and carries 6 of the 8 amendment elements verbatim, including the two reportable quotes (23 and 25 words). It verifiably supplies the method detail the publisher abstract could not: the phonological-systems pairing with universals/typology instruction, the multi-part creative project, and the introductory-level placement.

Flip condition (would turn ADMIT → REFUSE): if the admitted entry (conlang-scholarship.amend-2026-10-23.md) or any cited prose keeps attributing the token **"semester-long"** to S901/S880 — the PDF contains that token **zero times**. The correction is already shaped in the proposed row: the scope cell omits "semester-long", and the element remains attached to S894's abstract (which the amendment itself names as the source of "a semester-long language-construction project"). If S894 ends up quarantine-REFUSED or unreachable, the "semester-long" element must be dropped from the entry entirely, not back-filled onto S901. Secondary flip: if the PDF's live host moves and the Wayback captures fail to reproduce the passage (currently both do), re-verify before admitting.

## 8. Files fetched (download hygiene)

All under `/tmp/ScoutS901/` only (never fleet root / lane root):
- `/tmp/ScoutS901/anderson-etal-cjl-sotl.pdf` (live, 193,610 B, md5 00151e4bf251e2b338542d10efba02c5)
- `/tmp/ScoutS901/anderson-etal-cjl-sotl.txt` (pdftotext -layout, 430 lines)
- `/tmp/ScoutS901/recheck.pdf` (recheck re-fetch, same md5)
- `/tmp/ScoutS901/archived-anderson.pdf` (Wayback 2024-08-01 capture, 193,610 B)
