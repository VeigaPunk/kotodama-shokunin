# R18-C10 — independent live re-probe, full-inventory re-sweep and revision audit (auditor 2 of 2)

- Seat: **C R18-C10** (round-18 C-auditors, seat 2 of 2; sibling seat C09 in `audit-1.md`).
- Claim under audit: `reports/round-18/claims.json` claim **C** (as in `audit-1.md`).
- Date: 2026-10-18 (all probes this date; times UTC unless noted). HEAD
  `c66ac3c951b346a2a56f9386e3324b4f5fe33902`.
- What is different from C09: this seat re-ran the evidence **on the wire** — a decisive
  re-probe set plus a **complete 193-URL re-sweep of all 12 transitioned entries' cited
  URLs** — and audited the applied revision file (`reports/round-18/civ-map-r18.json`)
  against the patch and the ledger. C09 audited the evidence structure and demotion rule.
- Method: `curl -sS -o /dev/null -w '%{http_code} %{size_download} %{url_effective} %{content_type}' -L --max-time 12|15|25 -A 'Mozilla/5.0 (compatible; kotodama-metadata-audit/1.0)'`,
  retry once on 000, 8 concurrent; the fixer's stricter forms (`-k`, `--compressed`,
  range requests) where a claim depends on them. Raw records: `.scratch/r18c09/probe-run1.json`
  (67 probes + follow-ups), `sweep-all.json` (193 URLs), `artifact-hashes.json`, `muisca-nyia.html`.
- **NON-CANON.** Locator/status-class verification only; no freshness axis verdict (pause
  respected), no canon, rights, clearance, rank or promotion ruling.

## 1. Decisive re-probe (selected exact observations; full lists in the ledger)

| entry | decisive claim (receipt) | my observation (2026-10-18) | class |
|---|---|---|---|
| inuit | old locator 404; new 200/206 `515139 B` + sha256 | old **404 `95720`**; new **200 `515139`**; body sha256 `61388588…660d` (downloaded, MATCH) | exact |
| maya-classic | Sacbe 200 `178576` + sha; in-entry `sacbeob` > 0 | **200 `178576`**, sha `94b6bdaf…7e90` MATCH; `grep -ci sacbeob` → **8** (was 0); lexicon :20 pointer → entry present | exact |
| mesoamerica | strict 000 ×2 (TLS) + 1 hostname mismatch; `-k` content 200/200/404; replacements 200 | strict **000 ×3** (errors 60/20 reproduced); `-k` **200 `267502`**, **200 `3499309`**, **404 `146`**; replacements **200 `19081`**, **200 `130398`**; strict control **200 `3162177`** | exact |
| mongol | rubruck 200 `289660` | **200 `289660`** (full entry 10/10 live) | exact |
| muisca | 4× 200 `25827/33028/30692/32263`; https negative | all four **exact**; nyia body sha16 `68342c14f9cc6479` MATCH + anchor `Ms. 2923. fol. 31v`; https **000** | exact |
| persia | replacement 200 `948943`; fallback 200; avesta 000 | **200 `948943`**; fallback **200 `127638`** (retally note below); jstor DOI → `jstor.org/stable/599356?origin=crossref` 200; ucpress `168710`, uci `536387`/`2928181` exact; avesta **000 "certificate has expired"** | exact |
| polynesia | 9 re-pin targets 200; old hosts 301 | **9/9 200** (`37919/27732/32920/32101/28210/31663/15127/7986/117921`); old `pollex.eva.mpg.de/entry/moana` → **`pollex.org.nz/entry/moana` 200 `31663`**; old wehe → **wehe.hilo 200 `117921`** | exact |
| rapa-nui | 8×200 exact sizes; metmuseum 429 | zenodo `82124`, wiki `427128`, langsci `37175`, moevarua `373137` **exact**; archive.org `256645–256647` (dynamic, ±2); metmuseum **429** | exact / dynamic |
| rome | OCRE paren URL 200; `--compressed` byte column; body hashes | **200** raw `80524` / `--compressed` `11046` (exact); body sha16 `dfa92e87f8ad338f`; tacitus `17659` + `8f605172cdba5905`; suetonius `326426` + `9344cf5845ccb962`; cambridge `731447` + `6c450b438b4ed57f`; DOI 429 `1302` | exact (4/4 body hashes) |
| ryukyu | MDPI 403; 11×200 | MDPI **403 `398`** (byte-identical to C01); kyotoreview `183135`, lingdy `1679959` **exact**; samples 200 | exact |
| scythian | Leiden 301 target 200 `8911` | **200 `8911`** (old form resolves there too); samples `92359/498050/76005` exact | exact |
| siam | both 301 targets 200 `118615`/`1657019` | **exact**; cambridge excerpt `199008`; unesco `155463` (claim `155457`, +6 B dynamic); loc.gov **403** | exact / dynamic |

Retally notes: persia fallback `127638` vs receipt `127643` / verifier `127635` — Wayback
re-renders (identical to C01's observation); five instances of ±bytes dynamic variance on
live pages in total (F-18AUD-3). One URL could not be reached at all from this vantage
(`openn.library.upenn.edu`): 000 on 5 attempts — outside every transition's decisive set
(F-18AUD-5). After several probes in one session, numismatics.org timed out once following
three successful 200s including the byte-exact body (F-18AUD-7, host throttling, not rot).

## 2. Full-inventory re-sweep (193 URLs; complete cited-URL sets of the 12 entries)

| entry | n | my tally (2026-10-18) | receipt claim | verdict |
|---|---|---|---|---|
| inuit.md | 21 | 19×200, 1×403, 1×404 | old 404 + new 200 + alternates; others keep r8 classes | consistent |
| maya-classic.md | 10 | 6×200, 2×429, 2×403 | r8: 5 live / 4 blocked + new sources | consistent |
| mesoamerica-primary-sources.md | 49 | 36×200, 4×429, 4×403, 4×000, 1×202 | r8: 46 links (35 live / 11 non-2xx) + r17 dispositions | consistent; the 4×000 = the 3 documented TLS-class URLs + openn (F-18AUD-5) |
| mongol.md | 10 | 10×200 | locator live; entry 10 links | **exact** |
| muisca.md | 8 | 6×200, 1×403, 1×429 | 4 muysca + arXiv + cam 200; Hathi 403; DOI 429 | **exact** |
| persia-sasanian.md | 10 | 8×200, 1×429, 1×000 | 6×200 + replacement + fallback; cambridge 429; avesta 000 | **exact** |
| polynesia-navigation.md | 26 | 24×200, 2×403 | 24×200 (incl. 2 MUSE), 2×403 | **exact** |
| rapa-nui.md | 9 | 8×200, 1×429 | 8×200, 1×429 | **exact** |
| rome.md | 12 | 10×200, 2×429 | 10×200, 2×429 | **exact** (after paren correction, F-18AUD-2) |
| ryukyu.md | 12 | 11×200, 1×403 | 11×200, 1×403 | **exact** |
| scythian-saka.md | 12 | 11×200, 1×403 | 11×200, 1×403 | **exact** |
| siam-thai.md | 14 | 11×200, 1×202, 2×403 | 12 live (incl. 202) + 2×403 | **exact** |

No entry's tally contradicts its receipt. The one apparent rome 404 was my extractor's
paren truncation (F-18AUD-2), corrected by a balanced-paren re-probe before classification.

Sibling seats C03–C06 (`verify-1..4.md`, same window 10:19–10:33Z) ran their own
independent 193-URL sweep and agree with every row above; their three findings are the
same classes this audit records — F-C03-1 (openn unreachable) ≡ F-18AUD-5; F-C05-1
(Wayback replay byte variance) ≡ F-18AUD-3; F-C06-1 (ryukyu MDPI served as a 200 JS
challenge page, 2,224 B, at their vantage vs 403/398 at mine and C09's) extends
F-18AUD-3 — the bot-wall class is stable, only the code presentation varies by vantage.

## 3. Revision audit — `reports/round-18/civ-map-r18.json`

sha256 `5fb4dd1cb948abbbbdb7b3182e5ba47cb15057da3519bd8bc63ad022ad8bf796` (matches the
scribe's filed claim in `civ/patch-apply.md`).

| check | result |
|---|---|
| 12 transition rows equal the patch's `to` objects (status/verified_at/command/evidence_path/reason) | **12/12** |
| non-transition rows differ from round-16 map rows | **none (82 verbatim)** |
| entries / count / unreceipted / complete | 94 / 94 / **[]** / true |
| status counts | 83 current, 11 stale-fixed, **0 stale-documented** (was 12) |
| terminal reading | `terminal_status=current` on all 12 transitions (94/94 current) |
| evidence pins (20 files, incl. all 12 receipts) match live bytes | **20/20** |
| `fix_receipt_sha256` pins on the 12 transitions match live bytes | **12/12** |
| round-16 map bytes unchanged | sha `07cabb69…` + `git status --porcelain` empty for the path |
| counting command `ls corpus/knowledge/civilizations/*.md | wc -l` | **94** |
| label policy (F-18AUD-1) | patch labels applied verbatim + terminal_status carrier; normalization documented as an option — adjudicated consistent |
| "5 attempt-documented rows" (F-18AUD-6) | both readings satisfied (all 12 rows carry live re-checks; `attempt_row` flags the 5 fixed-type rows explicitly) |

The scribe's receipt also records a near-miss caught by their own gate before filing (the
`to` objects lack a `file` key; a build that wrote them raw produced "row #43 names no
civilization entry") and its fix — noted here because it is exactly the class of defect
this audit would have demoted for had it shipped.

## 4. The claim's counting command — `python3 reports/round-18/run-validation.py`

The runner was still being written when this audit began (no `__main__` entry point at
first read, 10:31Z; three distinct hashes observed during the audit). Two `--check`
(no-write) runs were made; **C is green on the current runner**:

- **Run 1** (runner sha `af21d2e2…`, 10:35:40Z): rc 1 — claim C **2 failures** ("row
  maya-classic / mesoamerica-primary-sources's transitioned status carries no
  date+command") under the then-current narrower carrier rule; D 2 failures (D4 typed
  artifact absent); O 6 failures (in-flight gate work, incl. "filed round-11 pin bytes
  changed"). This run predates the carrier fix; its C failures were a runner artifact, not
  missing evidence (F-18AUD-9), and the revision file did not change between runs
  (sha `5fb4dd1c…` stable from 07:27 local).
- **Run 2** (runner sha `905314f7…`, 10:38:33Z): rc 1 — **claim C: 0 failures**; claim D 2
  failures ("D4 typed artifact not found under examples/culture-d4"; D4 gate exit 2:
  "adapter missing: tools/assemble-d4-typed.py"); claim O 2 failures (D4 packet not
  accepted at exit 0; flag-declared assembler path not green). `acceptance_checks_passed:
  false` overall **because D and O work was still in flight mid-wave** — not a C finding.
- C-relevant controller reading: on the current runner every transitioned row passes the
  date+command carrier rule; the two rows whose own `command` prose lacks an executable
  token pass through their `verified_r18` / `transition.r18_recheck.command` fields
  (F-18AUD-9 — optional hardening only).

## 5. Ledger cross-check

`reports/round-18/civ/auditor-ledger.json` (this seat's machine deliverable): kept **12**,
demoted **0**, 9 findings, 18/18 round-17 C pins, 12/12 `fix_receipt_sha256` pins, all
per-row `live_repro` lists reproduce the values in §1–§2. Current ledger sha256
`36a17bd0cd8110b2…` — note that run 1 of the validator pinned an **earlier revision** of
my ledger (`4751e96c…`, before the validator-outcome block was added); the parent should
re-pin at the settled tree on the acceptance run.

Cross-seat reconciliation (no contradictions found): C03–C06 `verify-1..4.md` and this
audit agree on 12/12 transitions matching the patch's `to` blocks, 82/82 rows carried
verbatim, 12/12 post-fix entry hashes, the 94 count, and every decisive locator's class;
their documented findings map onto F-18AUD-3/5 as noted in §2. The scribe revision
(`patch-apply.md`, sha `f9c1fe70…` at this reading) and the four verifier reports are the
sibling-chain legs; none of them contradicts this ledger's KEEP verdicts.

## 6. Limits

NON-CANON (see header). Point-in-time: every observation is a single-day (2026-10-18)
status snapshot; single-day sweeps cannot rule out intermittent failure and say so
themselves. 403/429/000 classes are named per case per the M04 convention; probes come
from one network vantage; the map scribe, its verifiers and this audit are separate seats,
so agreement is corroboration rather than laboratory reproduction. The runner is a moving
target mid-wave — the acceptance run must be made on the settled tree.

Reproduction: `python3 .scratch/r18c09/sweep-all.py` (193-URL sweep) and
`python3 .scratch/r18c09/build-ledger.py` (re-derives pins and rewrites the ledger);
raw probe records under `.scratch/r18c09/`.
