# R18-C03 — independent verification of the round-17 civ patch, group 1 of 4 (fixed-type A)

- Verifier seat: **C R18-C03** (round-18 C-verifiers ×4: `verify-1..4.md`). This file
  covers the **fixed-type group A** rows of `reports/round-17/civ/map-patch.json`:
  **`inuit`, `maya-classic`, `mesoamerica-primary-sources`**. Sibling seats:
  `verify-2.md` (C04: `mongol`, `muisca` + the 5-attempt documentation check),
  `verify-3.md` (C05: `persia-sasanian`, `polynesia-navigation`, `rapa-nui`, `rome`),
  `verify-4.md` (C06: `ryukyu`, `scythian-saka`, `siam-thai` + the 12-row roll-up).
- Date: 2026-10-18; measurement window **10:19–10:33Z** (all stamps UTC; probe log
  `date -u` lines in `.scratch/r18c03/`). Lane HEAD during verification `c66ac3c`
  ("round-18: declare claims O/D/C"); the patch under test was applied by the
  round-17 close `3dd3754`; the pre-fix state is the round-16 close
  **`f30b6f8188937632bbedd0e7b29aeefff6f8b07b`** (the patch's own declared baseline
  is `3dd3754`, whose parent is `f30b6f8`).
- Assignment (verbatim, task brief): *"C R18-C03..C06 (verify x4): independently re-run
  each transitioned row's new evidence (fetch the replacement URLs, spot-check); verify
  the 5 attempt rows' documentation; counting command reproduces 94;
  reports/round-18/civ/verify-{1..4}.md."*
- **Status at verification time:** this seat's group-A measurements began 10:19Z, when
  `reports/round-18/` held only `claims.json`, `targets.json`, `scope.md` and
  `gate/tests-1.md`. The round-18 map revision **landed during the window**:
  `reports/round-18/civ-map-r18.json` (`built_by` "CIV R18-C01/C02 map revision",
  `date_utc` 2026-10-18T10:27:26Z, 94 entries) — so this file verifies the **patch rows
  + the corpus bytes they point at** (what that revision consumes), and §4 records the
  cross-check of the delivered revision against the patch (12/12 transitions match the
  patch `to` blocks; 82/82 carried rows byte-equal the round-16 map; the revision's
  declared `applied_patch.sha256` equals the patch file's sha256 — full details in
  `verify-4.md` §4).
- **NON-CANON.** Verification only: no canon, rank, rights/clearance, freshness or
  promotion ruling is made or implied. "Verified" below means *the fixer's dated,
  command-carried claims reproduce on this seat's independent re-run*, not that the
  sources' scholarship is current or correct. Recency/freshness stays as the patch's
  own limits state.

## 0. Method (stated before results)

1. Read each fixer receipt (`reports/round-17/civ/{inuit,maya-classic,mesoamerica}.md`)
   and the patch row that cites it; extract every claim that names a **command, a
   status code, a byte count or a digest**.
2. **Re-run the fetches myself** (independent of the fixer's scratch, which is not
   used as evidence anywhere in this file): `curl -sS -L --compressed -A
   'kotodama-r18-c-verify/1.0' --max-time 25` for bodies, plus `-k` where the claim is
   a TLS-class failure, and `openssl`/`pdfinfo`/`pdftotext` for content claims.
3. **Hash what I downloaded** (`sha256sum`) and compare byte-for-byte against the
   receipt's digest; where only a size was claimed, compare the **on-disk
   (decompressed) size**, not `%{size_download}` (see F-C03-2).
4. **Re-run the whole-entry URL sweep** for all 12 patch rows: 193 distinct cited URLs
   extracted from the 12 corpus entries, one sample each, 8-way parallel, same UA,
   `--max-time 25`, scratch `.scratch/r18c03/sweep.json` (49,241 B) + `entries-urls.json`.
   Class codes: 200 = live, 403/429 = bot/rate wall, 000 = connection/TLS class,
   4xx = rot.
5. **Diff the patch against filed bytes** (not against receipts): `from_` rows vs
   `reports/round-16/civ-map.json` (`07cabb69…`, unchanged), `sha256_before` vs
   `git show f30b6f8:…`, `sha256_after` vs the delivered working tree.
6. Re-run the counting command; record it with its date.

## 1. `inuit.md` — Dorais 2010 dead locator replaced (patch row 1 / map idx 44)

| # | fixer claim (receipt `civ/inuit.md`) | my independent re-run (2026-10-18) | verdict |
|---|---|---|---|
| 1 | old locator 404 ×3, redirect to `jackmanlaw.utoronto.ca` | `404`, 12,083 B, effective `https://jackmanlaw.utoronto.ca/sites/default/files/toc/…pdf` | reproduces |
| 2 | new locator `api.pageplace.de/preview/…9780773581623…pdf` = 200, **515,139 B**, application/pdf | **200, 515,139 B** body, `file` → PDF 1.5, 41 page(s) | exact |
| 3 | fetched copy sha256 `61388588ca884f514c3e29510fc4ba21cb3d14d0b849e2a728eb87502f5f660d` | my body sha256 **`61388588…f5f660d`** — identical | exact |
| 4 | 41-page front-matter/ToC preview | `pdfinfo` → **Pages: 41**, Title `9780773581623.pdf` (Kobo-distilled) | exact |
| 5 | copyright page shows cited ISBN `978-0-7735-3646-3` | `pdftotext` whole book → `isbn 978-0-7735-3646-3` at **lines 260 and 283**, Contents present | exact |
| 6 | after-hash `52c5a11b…ef0c5d` | `sha256sum corpus/knowledge/civilizations/inuit.md` → **identical** | exact |
| 7 | before-hash `312427a3…` = round-16 receipt bytes | `git show f30b6f8:…/inuit.md` sha256 → **`312427a38a52d7ee…`** | exact |
| 8 | entry carries old→new + round-8/9/16 trail in `- verified-at:` | line 5 quotes old URL → new URL, `m03:67,109`, `v03:72`, "round-16 map entry 44", receipt pointer; line 39 records the 2026-10-18 access | exact |
| 9 | other cited links keep their 2026-10-17 status, not re-swept in round 17 | my sweep: 21 URLs → 19 × 200, 1 × 403 (`itk.ca`), 1 × 404 (the retained old trail URL) | consistent |

**Verdict: VERIFIED — byte-exact on every claimed artifact.** Note for the map: the old
URL stays in the entry as the documented trail and will report 404 on every future
sweep by design; a status-counting pass must read the entry note, not the bare code.

## 2. `maya-classic.md` — round-10 N2 couples gap closed (patch row 2 / map idx 61)

| # | fixer claim (receipt `civ/maya-classic.md`) | my independent re-run | verdict |
|---|---|---|---|
| 1 | pre-fix bytes `d3520973…` | `git show f30b6f8:…/maya-classic.md` sha256 → **`d3520973b3458df2…`** | exact |
| 2 | `[S]` Sacbe re-fetch: 200, **178,576 B**, sha256 `94b6bdafaae439ccc171e6e1f3fe458bbebb8a0954a547609d2d4c0c5c567e90` | `GET https://en.wikipedia.org/wiki/Sacbe` → **200, 178,576 B**, sha256 **`94b6bdaf…c567e90`** — identical; matches round-10's recorded sha16 `94b6bdaf` (`reports/round-10/coverage/review-C08.md:176`) | exact |
| 3 | `[KH]` handbook re-download: **49,858,925 B**, sha256 `2327b090ed3dfb0ef2b891786aef22a5612589253bdaf2a40b290604f9d238f2` | my own 50 MB download of `mesoweb.com/resources/handbook/IMH2020.pdf` → **49,858,925 B**, sha256 **`2327b090…f9d238f2`** — identical, `file` → PDF 1.6 | exact |
| 4 | after edit the entry had 9 sacbe hit lines (was 0) | `grep -c -i sacbe` → **9** | exact |
| 5 | reciprocal couples pointer added; lexicon `:20` still names maya-classic (sacbeob) | `sed -n 20p corpus/knowledge/culture-material/transport-mobility-lexicon.md` → line 20 contains `civilizations/maya-classic.md (sacbeob)`; entry §14 present at EOF | exact |
| 6 | after-hash `d9608d84…8ce67b5` | delivered sha256 → **identical** | exact |
| 7 | 10 distinct cited URLs, 5 live + 4 non-2xx/blocked at round-8 class | my sweep: 10 URLs → 7 × 200, 1 × 403 (`doi.org/10.1086/300142`), 2 × 429 (`doi.org/10.1017/…`) | consistent (bot walls, pre-existing) |

**Verdict: VERIFIED — byte-exact, including the two source digests the round-10 sweep
had recorded as sha16s.** The lexicon bytes are untouched (not in `git status`).

## 3. `mesoamerica-primary-sources.md` — 3 hard-fail URLs + pin drift (patch row 3 / map idx 62)

| # | fixer claim (receipt `civ/mesoamerica.md`) | my independent re-run | verdict |
|---|---|---|---|
| 1 | `florentinecodex.getty.edu/en/book/12/folio/19v`: strict `000 0` | strict → **000, 0 B** | exact |
| 2 | same URL under `-k`: 200, **267,502 B**, text/html, title `Book 12 Folio 19v\| Digital Florentine Codex` | `-k` → **200, 267,502 B**, `<title>Book 12 Folio 19v\| Digital Florentine Codex&#x27;` | exact (dynamic page; no digest was claimed) |
| 3 | `iifilologicas.unam.mx/…/totonicapan_simonetta2.pdf`: strict `000 0` → `-k` 200, **3,499,309 B**, application/pdf | strict → **000, 0 B**; `-k` → **200, 3,499,309 B**, `file` → PDF | exact |
| 4 | `liblilly.sitehost.iu.edu/etexts/nahuatl/index.shtml`: real rot → 404, 146 B nginx under `-k` | `-k` → **404, 146 B**; body `<title>404 Not Found</title>` | exact |
| 5 | replacement live article: `scholarworks.iu.edu/…/view/3788` 200, 19,081 B (Schwaller, *Bookman*, 69–88) | **200, 19,081 B** (digest `c35800a93d03530f…`) | exact |
| 6 | replacement PDF galley `…/download/3788/3500` 200, **5,388,824 B**, application/pdf | **200, 5,388,824 B**, `file` → PDF | exact |
| 7 | archived raw snapshot `web.archive.org/web/20210227003441id_/…` 200, **130,398 B**, sha256 `27d6a210bfc3a88da9015e52537c51f6b529411b361b3f333b3b5120cbae09ae` | **200, 130,398 B**, sha256 **`27d6a210…cae09ae`** — identical | exact |
| 8 | dead-end control `indiana.edu/~liblilly/etexts/nahuatl/` = IU catch-all homepage, 200, 318,019 B | **200, 318,019 B**, title `Indiana University Bloomington \| Academics, research, and impact` | exact |
| 9 | round-11 pin `a916a4c2…` equals the frozen round-3 snapshot input (32,633 B); pre-edit live bytes `6d40a97d…` (46,781 B) = round-4 revision | `git show f30b6f8:…/mesoamerica-primary-sources.md` → **`6d40a97d2b025fb4…`** (patch's declared before-hash) | exact for the deliverable's bind |
| 10 | after-hash `d04d8913…` | delivered sha256 → **identical** | exact |
| 11 | entry edits carry the round-16 trail + caveat | line 38 records the re-attempt, the 2-live-with-caveat/1-replaced disposition and the pin re-base; line 30 [HIG] carries the UNAM caveat sentence verbatim in substance | exact |

**Verdict: VERIFIED — every claimed artifact reproduces (sizes, digests, titles,
controls, both statuses of the TLS class).**

**Finding F-C03-1 (new negative observation, route to the round-18 map):**
`https://openn.library.upenn.edu/Data/0002/html/mscoll700_item221.html` is cited by this
entry at line 30 (`[HIG]` source-table row, OPenn Ms. Coll. 700 Item 221) and **is
currently unreachable from this lane's vantage**: 4/4 attempts failed — 3 × connection
timeout at 40 s (`https`, including the host root `https://openn.library.upenn.edu/`),
1 × `Recv failure: Connection reset by peer` after a 302 on the `http` variant
(2026-10-18, 10:29–10:31Z). The string `openn` appears **nowhere** in
`reports/round-16/**` or `reports/round-17/civ/**`, so this is neither a round-16 debt
nor covered by the round-17 re-attempt; the entry's other links are unaffected. Class:
connection/TLS-class unavailability (point-in-time), not confirmed rot — same class as
the round-8 `rubruck.html` 000 that did not reproduce in round 17. **Recommendation for
the map revision: carry it as a new dated observation on this entry (or route to a
round-19 re-attempt), not as a passed row.**

**Finding F-C03-2 (method note, informational):** the receipts' byte columns are
**decompressed body sizes**; a re-run that reports `curl %{size_download}` with
`Accept-Encoding` enabled sees wire sizes instead (my first group-A pass recorded inuit
as 515,139 B because that host served the PDF uncompressed, but mongol as 103,225 B
where the body is 289,660 B). Every claimed body size in this group reproduces exactly
once measured on disk. The patch's own `limits` note already records this class for
rome; recording it here for the fixed-type rows.

## 4. Longitudinal checks this seat ran over all three rows

- `ls corpus/knowledge/civilizations/*.md | wc -l` → **94** (run 2026-10-18 ≈10:19Z and
  again 10:32:53Z — the map's counting_command; §2 of `verify-2.md` holds the full
  reconciliation, including the 7 never-swept rows' 94-URL baseline sum).
- `reports/round-16/civ-map.json` sha256 = `07cabb69b4a41c51b74767212a07ba4ffae3c09ef8c2571abd954b37342cb943`
  — byte-equal to the sha the patch declares as its target; `git status --porcelain
  reports/round-16/ reports/round-17/` → 0 lines: no filed byte of rounds 16/17 was
  edited by the round-17 fixes or by anything since.
- Patch `from_` blocks vs filed map rows: 12/12 byte-equal (indices 44, 61, 62, 67, 68,
  77–83 all match `idx_round16_1based`).
- Patch `sha256_before` vs `git show f30b6f8:corpus/knowledge/civilizations/<entry>`:
  **12/12 match**; `sha256_after` vs delivered bytes: **12/12 match** (all twelve rows,
  computed by this seat; group values in the four verify files).
- **Delivered round-18 revision cross-check** (`reports/round-18/civ-map-r18.json`,
  landed 10:27:26Z while this seat worked): transitions == patch `to` blocks 12/12,
  carried rows field-identical to the round-16 map 82/82, `applied_patch.sha256` == the
  patch file's sha256, count 94 — full table in `verify-4.md` §4.

## 5. Findings carried to the parent

- **F-C03-1** — `openn.library.upenn.edu` unreachable 4/4 (new, not in any debt list) — §3.
- **F-C03-2** — receipt byte columns are post-decompression body sizes (method note) — §3.
- **F-C03-3** — closing observation: the round-18 map revision landed mid-window and
  passed this seat's cross-check against the patch (12/12 transitions, 82/82 carried
  rows, patch sha, evidence pins), so the group-A verdicts below bind to a revision that
  now exists rather than to an absent one.

## 6. Compliance

Writes: **this file only**, plus gitignored scratch under `.scratch/r18c03/`
(`entries-urls.json`, `sweep.py`, `sweep.json`, `probe-fixed.py`, `probe2.py`,
`probe3.py` + `.json`, `bodies/**`; the scripted passes ran with
`export TMPDIR=$PWD/.scratch`, and the few ad-hoc fetches were still written inside
`.scratch/r18c03/bodies/` — no scratch byte landed outside `.scratch/`). No tool, gate,
packet, corpus entry, map, receipt or earlier-round byte was edited; no git mutation;
no commit; no read outside the lane repo except the HTTP fetches listed. Sibling
scratch (`.scratch/r18c09/probe-run1.log`) was **read for cross-reference only** and is
cited as such, never as this seat's evidence.
