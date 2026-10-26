# SentinelScope — round 75 (hyaku run 10), wave 1: scope and safety review of the write surface

Seat: SentinelScope (sentinel, leaf). Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin` @ `f556d1049fe651d3d63975600b13acd9fb686f15` (working tree clean except the expected untracked `.ufo/waves/round-75/`, `reports/round-75/`).
Read-only seat: every command below is a read, a header/body probe into my own scratch, or an offline invocation. Nothing under the fleet root, the lane index, `corpus/**`, `/home/vgpnk/Projects/shokuknow/**` or a sibling lane was written; no git/jj state touched. Tools installed: **none** (`curl 8.23.0`, `pdftotext` already present). Scratch `/fast/scratch/hyaku/kotodama-r75/SentinelScope/` removed before yield; the receipts live in this file, not in the scratch.

Verdict: **no credential leak, no private-host URL, no login/consent/geo wall, no write path outside the granted roots.** The nine source URLs are reachable by ordinary means, but three of them are UA-sensitive and one is challenge-walled — and the round's own drafts do not yet record those in the QUALITY 22 grammar. Two landing-blocking scope defects stand (S-75-2, S-75-3), plus four medium path/normalisation defects.

Reviewed bytes, pinned at review time (the draft was still moving: `ScribeSkillGates.md:80` records a 19075 → 19300 B rewrite during the wave):

```
0f4fd1b040f75af9af055926058eb28e9b3b5ab7826ce3366ffa5f1d82e16a42  reports/round-75/claims.json   (19300 B)
48a8bc443fa8a90be7fba0bb497b16279616720f9427b462535a735d29f7d61c  reports/round-75/ledger.json    (11853 B)
7fb4f488807e8364d204a3081a2e57379d6caafaa92dbab9dfbc381757223754  SOURCES.append.md               (staged package)
43177eb5b58a5132e9bc5ffd46d4e455c7b7e033992d68cd6fbb01c542809e67  narrative-structure-frameworks.md
f129b734435da0fc73c0cff41e84bbd78505a25d23a73cb7503c3167d0047b55  narrative-structure-frameworks.amend-2026-10-23.md
0d542232abf09a8828e36f102bb7b059c406639fef7d7820c2fa248b8605777d  ...amend-2026-10-23b.md
42d5b593fe4ccdd95d8c172fd2c2422d9ca11d3f8052b064e0f98c5d75ef1c56  ...amend-2026-10-23c.md
8bf9584600d6b0c2f6c78098ec990fd658680d005b5f87e494b152466dce12e7  ...amend-2026-10-24.md
```

---

## 1. Credential / private-URL sweep of the staged narrative files, the staged rows, and the drafts — CLEAN

Pattern swept (case-insensitive) over the five staged `narrative-structure-frameworks*` files, the 214 KB staged `SOURCES.append.md` (plus `MERGE-REPORT.md`/`.json` provenance carry), `claims.json`, `ledger.json`, and every seat report present in `w1/` (17 files):

```
password|passwd|secret|api[_-]?key|apikey|bearer|authorization|op://|AKIA|ghp_|xox[bap]-|
BEGIN [A-Z ]*PRIVATE KEY|ssh-rsa|session[_-]?id|sessionid|auth=|sid=|cookie|localhost|
127\.0\.0\.1|0\.0\.0\.0|192\.168\.|\.internal|ssh://|file://|ftp://|Set-Cookie|OJSSID|__ddg
```

- Five narrative files: **0 hits**. `claims.json` / `ledger.json`: **0 hits**. Seat reports: **0 hits**.
- `SOURCES.append.md`: 2 lines hit, both **false positives** — line 54 `sID=` inside `?NewsID=10867` (a functional query parameter, not a session id), line 81 the English word “bearer” in prose.
- No email addresses, no `user:pass@` URL authorities, no `javascript:`/`data:`/`gopher://`/`dict://` schemes, and no absolute operator paths (`/home/`, `/Users/`, `C:\`) in the five narrative files or in the nine source URLs.
- Seat-report re-sweep for leaked response headers (`JSESSIONID`, `__ddg*`, `OJSSID`, support IDs, bearer strings, IPv4): 0 real hits; the only octet-string match is the browser UA literal `Chrome/124.0.0.0` in `ScoutUcass.md:16,22`.
- Probes did receive server-set cookies from `persee.fr` (`JSESSIONID`, `COOKIE_SUPPORT`, `GUEST_LANGUAGE_ID`) and one Cloudflare cookie from `iris.unipa.it`. They are server-issued session state, not credentials; I persisted no cookie value into any lane file, and no seat report carries one. Same hygiene note as round 73 (S-8): do not paste response headers into a committed evidence file.

Only absolute paths found in staged bytes: `/tmp/gb.pdf`, `/tmp/n.pdf`, `/tmp/j.pdf`, `/tmp/k.pdf`, `/tmp/f.pdf` inside staged **recheck cells** (rows S8xx/S9xx). Those are not secrets, but they are scratch-discipline breaches and non-reproducible fetches — see **S-75-5**.

## 2. The nine source URLs — public ordinary-means surfaces, with three UA-sensitive hosts and one challenge

Probes: plain `GET` with `-L`, two UAs, bodies saved to scratch, headers saved; 2026-10-27. UA-B = `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`; UA-C = `curl/8.23.0` (the default curl UA string as sent).

| # | URL (as it will be registered) | UA-B | UA-C | type | identity confirmed |
|---|---|---|---|---|---|
| S885 | `https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113` | 200, 109589 B | 200, 109582 B | text/html | Barthes, *Communications* 8 (1966) 1–27 |
| S886 | `https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1120` | 200, 109336 B | 200, 109329 B | text/html | Todorov, same issue, 125–151 |
| S887 | `https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1114` | 200, 118777 B | 200, 116872 B | text/html | Greimas, same issue, 28–59 |
| S888 | `https://jw.ucass.edu.cn/kcdg/zyk/xwcb/xushixue.pdf` | 200, 225123 B | 200, 225123 B | application/pdf | 中国社会科学院大学《叙事学》课程大纲 |
| S889 | `https://www.jstage.jst.go.jp/article/jcss/25/2/25_200/_pdf` | 200, 1085244 B | 502, 13808 B then **200, 1085244 B ×3** | application/pdf | 小方孝, *Cognitive Studies* 25(2) 200–217 (2018) |
| S890 | `https://www.jstage.jst.go.jp/article/jsik/32/2/32_2022_017/_pdf` | 200, 697092 B | 200, 697092 B | application/pdf | 村井源, 情報知識学会誌 32(2) 246–251 |
| S891 | `https://www.unige.ch/lettres/framo/cernet/biblio/barth70.html` | 200, 48789 / 49529 B | **200, 245 B “Request Rejected”** | text/html | S/Z excerpt page |
| S892 | `https://iris.unipa.it/retrieve/e3ad891d-…/2014%20marrone%20age%20dor---2.pdf` | **403, 5867 B** | **403, 5676 B** | text/html `Just a moment...` | via Wayback (see §3) |
| S870 | `https://www.chinawriter.com.cn/n1/2023/0922/c404024-40083104.html` | 200, 45238 B | 200, 45238 B | text/html | 我是怎样创作网络小说的--网络文学--中国作家网 |

No `WWW-Authenticate`, no `Location:` redirect, no consent interstitial, no geo-block marker on any of the nine; no host resolves to a private/loopback address (all public academic/CDN edges). No tracking query strings: the only `?` in the nine URL set is inside S870's page path (none) — the staged naming rows' `?NewsID=10867` is functional, and no `utm_*`/`fbclid`/`gclid` occurs anywhere in the staged package.

Four wall/refusal facts that must reach the Gate, and the reason each matters:

1. **S892 is challenge-walled on both UAs** (`403`, body `<title>Just a moment...</title>`, `cf-mitigated` header on both responses). QUALITY 22: a wall persisting under both UAs is a valid reject, so the live URL is *rejected for the quote* and the row must rest on the archive capture (§3). The record must say the challenge was **met and not passed** — passing it (or driving a browser through it) would make the row UNOPENED under QUALITY 10.
2. **S891 answers HTTP 200 with a 245-byte F5 “Request Rejected” page under the plain UA** and a 48–50 KB page under UA-B. A `status:`-only reading of this source is wrong: the status decides nothing (QUALITY 22). A reject resting on the curl-UA refusal is *voided* by the browser-UA 200 — so any Gate reject for S891 must be re-opened, and the evidence file must carry both requests in the QUALITY 22 grammar. Note also the two UA-B fetches differed in size (48789 vs 49529 B): the page is dynamic, so the evidence sha256 must be of the exact stored body and a re-opener cannot be promised the same byte count.
3. **S889 returned one transient `502` + J-STAGE maintenance page (“メンテナンス中です”) under the plain UA**, then 200 on three retries under both UAs. A scout that recorded `status: 502` as a wall has a false refusal; retry before recording. This one is a real trap because the 502 body is a normal-looking HTML page, not a challenge.
4. **The Persée PDF endpoint is CAPTCHA-protected**: `https://www.persee.fr/docAsPDF/comm_0588-8018_1966_num_8_1_1113.pdf` → `403`, body `<h1>This resource is protected by altcha</h1>`; `/doc/…1113.pdf` → `404`. The full text is nevertheless available on ordinary terms through the reader's own per-page transcription endpoints, which I verified carry the article text with no challenge: `/doc/page/comm_0588-8018_1966_num_8_1_1113/comm_0588-8018_1966_num_8_1_T1_0001_0000` → 200/3231 B, `…T1_0006_0000` → 200 (carries «On propose de distinguer dans l'œuvre narrative trois niveaux de description» verbatim), `…T1_0139_0000` (Todorov) → 200/3939 B, `…T1_0030_0000` (Greimas) → 200/3737 B. **So claim C's kill rule (“the persee page-level transcription service is used through any access control”) bites exactly here**: the transcription is legal to use, the `docAsPDF` route is not, and any evidence file whose fetch line is `docAsPDF` is a QUALITY 10 bypass that fails the claim. The transcription is OCR and visibly garbled (`l'bomme` for `l'homme`, `Roland Barihes` for `Barthes`), so a Gate quote must be copied from the transcription, not from a modern printed edition, or it will not locate after NFKC + whitespace folding.

## 3. `iris.unipa.it` ↔ Wayback binding: a capture of the same page, verified by content (QUALITY 18)

```
CDX (statuscode:200, limit 5): one capture
  urlkey   it,unipa,iris)/retrieve/e3ad891d-…/2014%20marrone%20age%20dor---2.pdf
  timestamp 20251111222249
  original https://iris.unipa.it/retrieve/e3ad891d-ad9f-da0e-e053-3705fe0a2b96/2014%20marrone%20age%20dor---2.pdf
  mimetype application/pdf   statuscode 200   digest WUQOTMBFQNXZDSOQTVPOY6B7DHMX2YVF   length 759396
```

- The capture's embedded original is **byte-identical** to the live URL in its `%20` form, and the raw-space form (as written in `claims.json`) normalizes to the same `urlkey`, so the query-aware/percent-aware limb holds. Live 403 (challenge) + one working same-page capture = QUALITY 18 satisfied.
- I fetched the capture (`…/20251111222249if_/…`, UA-B): 200, 763802 B, `application/pdf`, sha256 `8c0303670ff5db8625d034be958ad5729a2c79fa77f3642efc5f6341fb25a19a`, `PDF-1.6`. It is **the same document, not a different one**: `pdftotext` page 1 reads `SIGNATA 5 (2014) / ANNALES DES SÉMIOTIQUES / … Dossier dirigé par Jean-Pierre Bertrand, François Provenzano et Valérie Stiénon / Presses Universitaires de Liège 2015`; the row's anchor passage «Mais combien, et de quelle nature, sont ces codes ?» is at text line 257 and the row's recheck token `cinq codes sont en partie` at line 264.
- Rate-limit note: a second fetch of the same snapshot over `http://` (the scheme the staged row uses) returned **429 with a 620-byte body**. The counter must recompute the stored window's sha256 from the committed evidence file and never re-fetch at grading time; a human re-opener should use `https://` and expect throttling.
- Defect **S-75-2** below: the row and the claim do not narrate the live challenge, and the row URL is cleartext `http://`.

## 4. Draft claims' write paths — inside the granted roots; four path/normalisation defects

Enumerated every path token in `claims.json` and `ledger.json` and classified it:

| write | claim | class |
|---|---|---|
| `corpus/SOURCES.md` (appends only), `corpus/knowledge/myth-symbol/narrative-structure-frameworks{,.amend-2026-10-23}.md`, `corpus/README.md` (index rows + last footer), `corpus/lessons/round-75.md` (Gate), `reports/round-75/evidence/**`, `reports/round-75/telemetry/*`, `.ufo/waves/round-75/assimilation/**` | C | lane, in-surface |
| `SHONEN.md:6`, `corpus/README.md:344` + `:407`, `reports/round-28/readme/sweep.py`, `corpus/QUALITY.md` (criterion-23 append), `SCORECARD.md` `## Corrections — round 75`, `SKILL.md:701`, `corpus/lessons/round-75.md` (correction rows), `reports/round-75/telemetry/*` | Ca | lane, in-surface |
| `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate` | C (CENSUS leg) | fleet **read-only invocation** |
| `/home/vgpnk/Projects/shokunin` (`--fleet-root`, fleet git, `.ufo/reports/round-74/kotodama.md` at `fleet_pin 3a740160…`) | Ca | fleet **read-only** |
| `.ufo/reports/round-75/kotodama.md` | — (L1 report) | the only fleet write, and no seat prompt names it as a write target |

- `MANIFEST.json`, `templates/`, `.ufo/state`, `.ufo/watchdog.log`, `.ufo/gates`, `shokuknow/**`: **absent from both claims** (grep over `claims.json`/`ledger.json` returns nothing). The wave spec names `/home/vgpnk/Projects/shokuknow/…` only as read inputs and as “READ-ONLY source tree: never write”.
- `sources-census.sh` is write-free for `validate`/`census`: header line 7 states “writes only stdout or `--out`”, `out_sink()` appends only when `OUT` is set (solely by `--out`), and every `mkdir` sits inside the `--selftest` temp tree. My own run: `sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` → exit 0, `… ok /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md`; base counts re-derived through it: **808 registry rows, 249 knowledge files, 0 narrative files** — matching claim C's `before` and the committed `census-start.txt`.

Defects:

- **S-75-2 (MEDIUM) — the S892 URL is not one canonical string, and the wall is unrecorded.** `claims.json` writes the document as `https://iris.unipa.it/retrieve/…/2014 marrone age dor---2.pdf (via wayback capture)` — a **raw space** plus a prose suffix — while the staged row S919 writes the percent-encoded URL inside a `http://web.archive.org/…if_/` wrapper. A by-document map built by string equality (COLLCHECK / REPOINTED) cannot match these; and neither string says the live URL is Cloudflare-challenged. *Exploit path:* a counter that normalises naively maps S892 to nothing (or a scribe “fixes” it to the raw-space URL and the registry cell then fails `E01`/QUALITY 18). *Smallest remediation:* freeze S892's document as the percent-encoded live URL only; put “challenge met, not passed; opened via Wayback 20251111222249” in the Gate/evidence and in the row's source cell, not in the frozen document string.
- **S-75-3 (MEDIUM) — Ca's APPENDONLY leg polices a fleet blob against a sha256 that does not exist.** The leg reads “…the fleet round-74 report at the ledger's `fleet_pin` is byte-identical to the blob its sha256 names”, but `ledger.must_track` is `[]` and **no 64-hex sha256 appears anywhere in `claims.json` or `ledger.json`**. The only clause that touches fleet bytes is therefore unfalsifiable as drafted (it can neither pass nor fail). I computed what it would have to name: `git -C /home/vgpnk/Projects/shokunin cat-file -p 3a7401609325341eb3fe0efd42d0eec29d06be3c:.ufo/reports/round-74/kotodama.md` = 9859 B, sha256 `354273bc972d8b86a012a8aac024618d5defa73e72ea1eae5a960fdf64f84107`. *Smallest remediation:* add that pair to `must_track` (path + revision + sha256) before freeze, or delete the clause and keep “this lane writes no byte under the fleet root except its own round-75 report”.
- **S-75-4 (MEDIUM) — L75-04 cannot go green under its own legs, and its repair lands outside its stated line.** The pair's `stated_at` is `reports/round-28/readme/sweep.py:16`, its `stated_text` is the docstring sentence “This instrument adds that leg.” and its `observe_cmd` counts `FOOTER_RE.search` (which is line **108** of that file). (a) A token that is prose can never equal an observed count, so the REPAIR leg's “re-read the statement = the observed truth” is unsatisfiable whatever the repair does. (b) The described fix — “make the sweep read the LAST footer” — necessarily edits line 108, and the APPENDONLY leg admits “changed lines elsewhere … a subset of the `stated_at` lines of REPAIR pairs plus appended lines”, so the required edit is forbidden. *Smallest remediation:* re-point the pair at the code line it repairs and make `stated_text`/`stated_parse` read a token the observe command actually produces, or demote it to ANNOTATE.
- **S-75-5 (MEDIUM) — the staged rows carry `/tmp` paths and executable pipelines that the normaliser must strip.** Five staged recheck cells name `/tmp/{gb,n,j,k,f}.pdf` and are `curl -fsSL '<url>' \| pdftotext … \| grep -c '<span>' -> N (ran 2026-10-23)`; S919 adds a second site over `http://`. Claim C's kill rule already fails an as-is append, and the ROWS leg demands a cadence-only cell with no pipe in any cell — so the point of this finding is the remediation list: replace with the ISO cadence, drop every `/tmp` path, drop the `-> N` results, re-escape nothing, set `opened = 2026-10-27`, and keep the pipeline as a Gate note only if the Gate grammar can carry it.
- **S-75-6 (LOW) — three URL sets in the drafted entries are not what the rows will carry.** The staged base entry's `source:` lines cite staged ids `S876, S864, S865, S866, S870` and its `recheck:` line points at “the row recheck command in round 2's `SOURCES-PROPOSED.md`”; the 23b/23c/24 amendments cite `S905, S917, S919, S921`. `S870` is in no frozen row unless its quote locates this round, so an as-is adoption fails REPOINTED on that line alone. *Remediation:* the Scribe entries must carry exactly one lane id per `source:` line (`S885…S892`) and a cadence, not a command; if S870 is refused this round, its `source:` line and the §8 practitioner register paragraph go with it (or are marked tier-C-unopened).
- **S-75-7 (INFO) — two claims write the same two files.** `corpus/README.md` (C: index rows + last footer; Ca: heading lines 344/407) and `corpus/lessons/round-75.md` (C: Gate; Ca: correction rows). The `axes_note` promises each counter names the sibling's lines in its frozen exemptions; without that, the combined tree grades red on `INDEX`/`APPENDONLY`. Worth a reviewer's eye at freeze, not a scope breach.

## 5. Entry content — method, not a canon decision and not a rights ruling (PROVINCE)

- Both adopted staged files end their `- scope:` line with an explicit refusal of canon: “it decides no culture's story (lore-shokunin owns canon)” — the boundary PROVINCE.md draws.
- Rights vocabulary sweep over all five narrative files (`canon|rights|copyright|licen[cs]e|fair use|public domain|permission|attribut|infring|trademark|©`): the only hits are the word **attribution** used bibliographically (“corrects their attribution”, “each attributed to a precedent”) — a scholarly-priority statement, not a rights or permission ruling. No licence, no permission, no fair-use, no “may be reproduced” claim anywhere.
- The bodies are method and design orders (levels of description, two readings, story/discourse, three time axes, actantial model, ストーリー/クエスト/シーン format, 起承転結 as a minimal completable unit), each with a calibration line — they prescribe how to specify a narrative, not what is true in any world.
- No absolute operator paths and no non-https URL except the one archive capture; no credentials (§1).
- Residual, for `RevEntryQuality` rather than me: the staged base entry still contains a “Superseded passage … Trim it if the later entry supersedes it outright” block and a round-2-era `ground:`; the frozen entry must not ship that editorial instruction as body text.

## 6. Scratch roots — PASS for this wave so far

- `/fast/scratch/hyaku/kotodama-r75/` holds 20 directories (CritCaVacuity, CritTrendObservables, ExecEvidence, ExecLedger, ExecRenumber, ExecScratchMirror, ExecSweepFix, MutCaLedger, MutRegistryCollision, RevEntryQuality, ScoutJstageJsik, ScoutMapIds, ScoutPersee1113, ScribeEntryAmend, ScribeLesson, ScribeQuality, ScribeReadmeIndex, SentinelScope, SimplifierRows, l1-dryrun) — 1.2 GB total, **no file above 50 MB** (`find -size +50M` → none).
- Every seat report present in `w1/` declares a scratch dir under that root and its removal; **no seat report cites `/tmp` as its own evidence**. The single `/tmp` mention in a report is `ConnectorPatterns.md:56`, correctly flagging a `/tmp` path that sits *inside a committed round-73 receipt* — the right call, not a breach.
- `/tmp` leftovers are from earlier rounds (round-73/74 `p-ScribeSrc*.txt`, `exec-c2-diff-check.diff`, all 2026-10-26) and from another lane (`/tmp/hyaku/kaidoku-r39`), not this round.

## 7. Findings

| id | sev | finding | smallest remediation |
|---|---|---|---|
| S-75-2 | MEDIUM | S892 document string is non-canonical (raw space + prose suffix) in `claims.json` vs `%20` in the row ⇒ by-document map/REPOINTED mismatch; neither string records the live 403 challenge | freeze the percent-encoded live URL as the document; narrate “challenge met, not passed; opened via Wayback 20251111222249” in Gate/evidence/row cell |
| S-75-3 | MEDIUM | APPENDONLY's fleet clause names “the blob its sha256 names” but `must_track` is `[]` and no 64-hex sha256 exists in either frozen file — the only fleet-bytes clause is unfalsifiable | add `.ufo/reports/round-74/kotodama.md @ 3a740160… = 354273bc…` to `must_track`, or delete the clause |
| S-75-4 | MEDIUM | L75-04 states prose at `sweep.py:16` but observes a count from `sweep.py:108`; the fix edits line 108, outside the `stated_at` lines APPENDONLY permits | re-point the pair at the code line it repairs with a token the observe command returns, or demote to ANNOTATE |
| S-75-5 | MEDIUM | staged recheck cells carry `/tmp/*.pdf` paths and `curl \| pdftotext \| grep` pipelines (S919 over `http://`) | normalise to cadence-only, drop `/tmp` and `-> N`; pipeline stays a Gate note at most |
| S-75-6 | LOW | staged entries' `source:` lines cite staged ids (`S870, S864–S866, S876, S905, S917, S919, S921`); S870 is not in the row set unless re-quoted this round | one lane id per `source:` line from the frozen row set; drop or tier-C-unopen the S870 paragraph if refused |
| S-75-7 | INFO | C and Ca both write `corpus/README.md` and `corpus/lessons/round-75.md` | the frozen exemptions must name the sibling's lines (as `axes_note` promises) |
| S-75-8 | LOW | S891 answers 200 with a 245 B “Request Rejected” under the curl UA (browser UA 48–50 KB) ⇒ a curl-UA reject is void; S889 gave one transient 502 maintenance page | record both requests in the QUALITY 22 line grammar; retry jstage before any refusal |
| S-75-9 | LOW | Persée full text is free only via `/doc/page/…`; `docAsPDF` is altcha-protected (403) and `/doc/….pdf` is 404; transcription is OCR-garbled | fetch `/doc/page/…` only; copy Gate quotes from the transcription; any `docAsPDF` fetch line fails claim C |
| S-75-10 | INFO | S892 capture re-fetch over `http://` returned 429 (620 B); the page at S891 varies in size between two browser fetches | keep the stored window authoritative; re-openers use `https://` and expect throttling |
| S-75-11 | INFO | no secrets, no private hosts, no op:// refs, no userinfo URLs, no consent/geo/login wall in any reviewed byte; write surface inside lane + read-only fleet; content is method, not canon/rights; scratch roots compliant | none |

## 8. What I did **not** run (unrun ≠ passed)

- The counters `reports/round-75/accept-c.py` / `accept-ca.py` do not exist yet; no claim leg was graded, and I did not grade any.
- I did not re-derive Ca's eleven ledger observations at base (ExecLedger/ExecCaCounter's leg), and I did not check the `R1EXEMPT` fixtures (CritR1Exemption).
- I did not verify the quoted spans of the other seven sources against their documents (each scout's leg); I verified identity and access only, plus S892's anchor and the Barthes p.6 sentence as spot checks.
- I did not read the final Scribe drafts (`.ufo/waves/round-75/drafts/` was empty at review time), so §1 and §5 are sweeps of the staged sources the drafts derive from. The landing tree must be re-swept (recipe below).
- No geo-block test was possible beyond observing that all nine responses carried no geo/consent redirect; a restricted egress could still differ.

## 9. Re-check recipe for the landing tree (one pass, read-only)

```
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
grep -Ein 'password|passwd|secret|api[_-]?key|bearer|authorization|op://|AKIA|ghp_|BEGIN [A-Z ]*PRIVATE KEY|session[_-]?id|auth=|cookie|/tmp/|/home/|docAsPDF' \
  corpus/knowledge/myth-symbol/narrative-structure-frameworks*.md corpus/SOURCES.md corpus/lessons/round-75.md reports/round-75/evidence/*.txt
grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md          # 808 + k
grep -o 'https\?://[^ )"]*' corpus/knowledge/myth-symbol/narrative-structure-frameworks*.md | sort -u
git -C /home/vgpnk/Projects/shokunin status --porcelain | grep -v '^.M .ufo/state/'   # only lanes' own untracked dirs
```

Expected on a clean landing: zero hits for the secret/`/tmp`/`/home`/`docAsPDF` pattern; every `source:` URL one of the nine (no `web.archive.org` wrapper in a `source:` cell — the archive goes in the row cell and the Gate); no `/tmp` and no `-> N` in any recheck cell; every evidence file carrying `UA "…" -> HTTP …, … B, wall …` lines for the S891/S892/S889 cases.

Scratch: `/fast/scratch/hyaku/kotodama-r75/SentinelScope/` — created, used for probe bodies and the Wayback PDF only, removed before yield.
