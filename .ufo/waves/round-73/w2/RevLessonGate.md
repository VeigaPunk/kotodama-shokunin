# RevLessonGate — wave 2 (FALSIFY) review of `corpus/lessons/round-73.md` as a Gate record

Seat: RevLessonGate (kotodama round 73, hyaku run 7, wave 2, leaf). Date: 2026-10-25.
Target: the round-73 lesson (lane revision 0316b8883b4f8d44b8efd720140e7f52f734a102, base 8841ad3b896a0227674fa0725b818c999118046f; claims frozen at af65165).
Mode: read-only against the lane; all experiments (counter runs, selftest repro) in throwaway clones (`mktemp -d` + clone at the pinned revision); live web probes recorded with UA/status/bytes. No lane bytes mutated except this report file; no installs (no pacman; no tool added).

---

## Result summary

- **No BLOCKER.** Every claim leg the lesson feeds (admit rows, reject rows, collision guard numbers, mirror sha256, Mistakes-table red-befores, quarantine table, considerthese absence) reproduced under re-derivation.
- **1 MINOR finding** (false support statement): the sibling-overlap note says the handoff contract `corpus/knowledge/synthesis/worldbible-integration-contract.md` is "cited by both entries"; the amend entry `conlang-scholarship.amend-2026-10-23.md` does **not** cite it (0 mentions). See Finding M-1.
- Everything else checked reproduced; residual gaps listed at the end.

---

## 1. Gate admit rows (item 1) — all five reproduce

Checked per row: URL vs evidence fetch line vs SOURCES source cell; access date; quote `wc -w` ≤25; verbatim presence inside the evidence context window; locator; evidence pointer file exists; sha256 prefix; HTTP 200; bytes.

| row | quote words (wc -w) | sha256 prefix vs evidence | bytes vs evidence | HTTP | locator vs evidence |
|---|---|---|---|---|---|
| S876 | 16 ✓ | e7260b49370e9a1e ✓ | 30289 ✓ | 200 ✓ | "Abstract paragraph ... page-source line 267": re-fetched the live page (`curl` browser UA, 200, 30289 B) and the quote sits exactly on page-source line 267 ✓ |
| S877 | 9 ✓ | e512a20dd3eef97e ✓ | 1055723 ✓ | 200 ✓ | "printed p. 10, Глава 1 …" ✓ (verbatim in window) |
| S878 | 24 ✓ | 9f745ddaccdbccbf ✓ | 959171 ✓ | 200 ✓ | "Abstract, p. 455" ✓ |
| S879 | 16 ✓ | 709e186b934c9ccb ✓ | 97622 ✓ | 200 ✓ | "comparison section, item 2.2 (printed p. 32)" ✓; "PDF p. 5 = printed p. 32" equivalence not re-derived (gap) |
| S880 | 25 ✓ | 26dbcf2c0fab6d75 ✓ | 193610 ✓ | 200 ✓ | "§3 These papers, p. 5" ✓ |

Evidence files `reports/round-73/evidence/S876.txt`..`S880.txt` each carry fetch line, browser-shaped UA (`Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`), `access-date: 2026-10-25`, `http-status: 200`, bytes, full 64-hex sha256 (prefixes match the Gate rows), `quote-found-verbatim: yes`, `quote-words` matching my `wc -w`, and the quote inside the context window. SOURCES rows S876–S880 (lines 831–835) carry the map URL verbatim, `mined`, `opened 2026-10-25`, `recheck 180d`, used-by exactly the citing entry (S876/S877 → `conlang-scholarship.md`; S878/S879/S880 → `.amend-2026-10-23.md`), tier B ×5. Staged→lane map (S881→S876, S882→S877, S892→S878, S893→S879, S901→S880) matches `assimilation/id-renumber-map.json` exactly and is corroborated by the w1 scout reports (ScoutS882/S892/S893/S901 name the tentative lane ids; ScoutS881 fetch metadata matches the evidence capture).

## 2. Reject/not-adopted rows (item 2) — reproduce, incl. QUALITY 22 grammar

- Every refuse/not-adopted row states reason + flip + probed URLs (verified full cells, incl. S894's probed URL list: DOI, Crossref record, CDX query; S909/S910 row: Springer chapter + MGIMO PDF; S869: conlang.org live + Wayback 20100107110431; S915 / S929-S930 / S920/S922/S923 rows carry their probed URLs).
- QUALITY 22 greps from `reports/round-73/telemetry/quality22-controls.txt` run over the lesson:
  - `GROUND='^\|.*\| *(wall|captcha|status):'` → **2** matches (rows S894, S909/S910)
  - `SHAPE='UA "[^"]{8,}" -> HTTP [1-5][0-9]{2}, [0-9]+ B, wall (present|absent).*UA "[^"]{8,}" -> HTTP [1-5][0-9]{2}, [0-9]+ B, wall (present|absent)'` → **2** matches (same rows)
  - `automation: (none|probed)` → **2** matches
  - control file expects `GROUND=2 SHAPE=2 automation-none=2 -> PASS` → reproduces exactly.
- Live re-probe of both walled sources (recorded UA/status/bytes) reproduces the status fields verbatim:
  - Cambridge `https://www.cambridge.org/core/product/identifier/S0008413124000215/type/journal_article`:
    - `curl/8.7.1` → HTTP 429, 1302 B, "Too many automated requests"
    - browser UA → HTTP 429, 1302 B, "Too many automated requests"
  - Springer `https://link.springer.com/chapter/10.1007/978-3-032-03277-5_15`:
    - `curl/8.7.1` → HTTP 200, 325225 B, no wall
    - browser UA → HTTP 200, 3038 B, "Client Challenge" shell
- Wayback CDX re-probe (recorded `curl/8.7.1`): `doi.org/10.1017/cnj.2024.21` → 0 captures; `cambridge.org/core/product/identifier/S0008413124000215` → 0 (also as prefix); `link.springer.com/chapter/10.1007/978-3-032-03277-5_15` → 0; `cyberleninka.ru/article/n/klassifikatsii-konlangov-v-sovremennoy-interlingvistike` → exactly **1** capture `20261025222414` (the this-round Save-Page-Now; none before this round — consistent with the lesson's "live leg only" + disclosed SPN). The SPN body itself could not be re-fetched (see gaps).

## 3. Collision guard / scratch mirror (item 3) — reproduce exactly

- `reg-ids` = 799 lines (S001..S875), `staged-ids` = 132 lines (S859..S990), `collisions` = 17 lines (S859..S875). S876–S880 present in neither (`grep -cE '^S87[6-9]$|^S880$'` → 0/0).
- `git show 0316b8883b4f8d44b8efd720140e7f52f734a102:corpus/SOURCES.md | sha256sum` → `93d6046444f2170e14514b2cc50cd21267a9592dc319513dd79fbffc3d018774` — equals the lesson's and `validate-receipt.txt`'s mirror registry sha256 (`93d6046444f2170e…018774`) exactly. Pre-append base registry sha256 `31a5739c83ad5737…824d8` also matches the receipt's "lane registry (pre-append)" line. Registry rows 799 → 804 (`grep -cE '^\| S[0-9]+ \|'` at landing = 804).
- `validate-receipt.txt`: `sources-census.sh validate --file` exit 0 on the mirror; CITED-LINES 0/2; ids block present (appended after first grading, per R73-M6).
- Guard proof: `guard-proof/guard-proof.txt` verdict PASS (planted 2-space-indented row seen by the 0–3-space guard, missed by column-zero control; A2 delta S881; A3 separability; real pair 799/132/17). `w1/MutRegistryCollision.md` mutation matrix documents m1–m6 and the declared scope (4-space/tab indents survive by design, matching the census parser note).

## 4. Mistakes table (item 4) — every pointer resolves; fixes shown able to fail

- R73-M1: `corpus/lessons/round-72-verifier-spotcheck.md:65` names exactly the two untracked files; `git ls-tree -r 8841ad3 --name-only` has neither; landing tree has both (`ScoutMergeScan.md`, `ScribeLesson.md`).
- R73-M2: `SCORECARD.md:1401` reads "ACCEPT-CA-72 PASS legs=12/12 at the measured revision"; `reports/round-72/telemetry/measures-ca.txt` reads `ACCEPT-CA-72: FAIL legs=12/12` exit 1; `telemetry/measures-ca72-rerun.txt` tail reads `ACCEPT-CA-72: PASS legs=12/12`/exit 0 at 21ad3088 with flee pin appended; ledger pair L06 (stated PASS vs observed FAIL) present.
- R73-M3: `telemetry/quality22-controls.txt` filed; live two-UA probes above reproduce both directions exactly.
- R73-M4: reproduced in a throwaway clone at base: `python3 -B reports/round-72/accept-c.py --selftest` → `SELFTEST: 10/11`, `--- clean fixture: expected PASS 10/10, got exit=1`, exit 1. Round-73 counters' receipts exist and pass: `selftest.txt` / `selftest-r2.txt` `SELFTEST: 29/29 … OK` (9 scenarios), `selftest-r3.txt` 29/29 OK (10 scenarios).
- R73-M5: `telemetry/red-before-r3.txt` exists with the exact promise (`SELFTEST FAIL: wt-only LEDGER: got 'PASS' want 'FAIL'`, exit 1); `counter-revisions.md` records r1 (frozen f8ebb5d8…), r2 (worktree-ledger bug fix), r3 (default-path guard + scenario 7b, sha256 222d4dd6d4082b49…); landing `accept-ca.py` sha256 = 222d4dd6d4082b49bfc949fa2dab804859e8f313703b70ec4e229653c2d12b89 ✓.
- R73-M6: `telemetry/gap-sweep.txt` section [7] present (literal-fragment recount appended after first grading); `validate-receipt.txt` ids block present; `id-renumber-map.json` has the `map` key (5 assignments, exactly the adopted map); `corpus/README.md` landing footer is additive and carries no claim-C ids (round-73 additions block, entries listed without S-ids; ledger-stamped "in-place footer" — verified via `git diff 8841ad3..0316b888`). Do-nothing C control `telemetry/controls-c.txt` shows `ACCEPT-C-73: FAIL legs=1/11` (only CENSUS green) exit 1; do-nothing Ca control `controls-ca.txt` shows FAIL legs=5/9 (REPAIR/ANNOTATE/NOSTUB/TRACKED red).
- Counter after-states reproduce in throwaway clones at the landing: `accept-c.py` → `ACCEPT-C-73: PASS legs=11/11` (needs the fleet `scripts/` adjacent; first bare clone run failed CENSUS for harness layout reasons, rerun with symlinked fleet scripts → PASS); `accept-ca.py` → `ACCEPT-CA-73: PASS legs=9/9`, SEPARABLE/TRACKED/STAMP green.

## 5. Quarantine table (item 5) — matches ScoutQuarantineConlang verbatim

- Row S786 → S869: PRESENT (title-page epigraph p. 1; live 200/753374 B; Wayback capture 20100107110431); the register's Chinese quote is a URL↔quote mispairing belonging to staged S870 — identical to the scout (§2, §6).
- Row S812 → S894: PRESENT in the Crossref abstract record; publisher page 429; "unverifiable at the publisher page, not fabrication; row not adopted" — matches scout §3.
- Row S827 → S910: PRESENT in Crossref record; publisher page serves in full under a plain UA; "wall" reading was UA-gated the other way (R73-M3) — matches scout §4 + this round's two-UA probe.

## 6. considerthese absence (item 6) — reproduces

`ls /home/vgpnk/Projects/shokunin/kotodama-shokunin/considerthese` → `cannot access … No such file or directory`, exit 2. Consistent with claims.json frontier_step and lesson.

## Findings

- **M-1 (MINOR)** — Lesson sibling-overlap note (lines 70–75): "the handoff contract `corpus/knowledge/synthesis/worldbible-integration-contract.md` is cited by both entries". `conlang-scholarship.md` cites it twice (line 11 `couples:`, line 104 hand-off); `conlang-scholarship.amend-2026-10-23.md` contains no mention (`grep -n 'contract\|handoff\|bible\|synthesis/'` → 0 hits). The contract file exists (28421 B, `corpus/knowledge/synthesis/worldbible-integration-contract.md`), but "cited by both entries" is false for the amend entry. The PROVINCE.md claim itself checks out (`lore-shokunin/PROVINCE.md` exists). No claim leg depends on this sentence; corrective wording: "cited by the base entry; the amend's handoff is the same contract via the base entry's `couples:` line" (or drop "both").

No further finding: no stale, vacuous, unsupported, or harmful statement found in what was exercised.

## What I could NOT check

1. **SPN shell body** — could not re-fetch `https://web.archive.org/web/20261025222414id_/https://cyberleninka.ru/article/n/klassifikatsii-konlangov-v-sovremennoy-interlingvistike` (curl ×4 with both UAs, `-4`, `--http1.1`, and the reader tool → all connection-refused/`ECONNREFUSED`; the CDX API endpoint worked, so serve paths were refused). The lesson's "does not carry the span" is taken from the wave-1 disclosure, not re-verified. Note: CDX metadata for that capture reports `length 24482` (digest KISPYG6AZ5ITJO6HOWZ6JBOZHSC5EPIU) vs the lesson's "23443 B" — likely WARC overhead vs body, but unconfirmed; flagged for the main agent.
2. **Live re-fetch/admit artifacts for sha256 re-derivation** — the five admit captures were verified against their stored evidence metadata (bytes/status/sha256/UA), not re-downloaded; live bytes may have rotated since the round.
3. **S879 "PDF p. 5 = printed p. 32" equivalence and S880 "p. 5"/S877 "printed p. 10" pagination** — evidence windows confirm the quotes verbatim and the printed-page locators, but I did not re-run full PDF pagination to re-derive PDF-leaf equivalence.
4. **Fleet report round-shape "37 seats"** — cross-checked `w1/spec.json` items = 37, with ConnectorSiblings/ScribeMistakes/ExecScratchMirror listed but report-less (matches the lesson's dead-seat note); the fleet report itself was not read.
5. **waves-1 scout reports S881/S892/S893** were checked at heads + relevant sections only (fetch lines/metadata consistent with evidence); full transcripts not re-audited.
