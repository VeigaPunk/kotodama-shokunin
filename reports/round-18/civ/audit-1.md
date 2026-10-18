# R18-C09 — adversarial audit of the round-17 map-patch transitions (round-18 claim C input)

- Seat: **C R18-C09** (round-18 C-auditors, seat 1 of 2; sibling seat C10 in `audit-2.md`).
  This seat audited the *transition evidence*; it did not build the map revision and did
  not write any corpus byte.
- Claim under audit: `reports/round-18/claims.json` claim **C** — the round-18 civ-map
  revision applies the round-17 patch (transitions with fix-evidence pointers), every
  transitioned row's new status carries date+command, the map's counting command
  reproduces 94, the round-16 map stays filed/unchanged, and any transition lacking live
  evidence is demoted.
- Date: 2026-10-18 (all runs this date; UTC stamps where quoted). HEAD
  `c66ac3c951b346a2a56f9386e3324b4f5fe33902`; claim baseline
  `3dd3754207032cb81f5fb3e202fe85cf79211339`.
- Objects audited (pins at audit time):
  - `reports/round-17/civ/map-patch.json` — sha256 `79ceafabac9fd84d6bec5cb701e3d1791b075e5e1300d7164126e40f9876e77e`
  - `reports/round-16/civ-map.json` — sha256 `07cabb69b4a41c51b74767212a07ba4ffae3c09ef8c2571abd954b37342cb943`
    (equals the patch's `target.sha256`; re-verified by this seat, not copied)
  - `reports/round-18/civ-map-r18.json` — sha256 `5fb4dd1cb948abbbbdb7b3182e5ba47cb15057da3519bd8bc63ad022ad8bf796`
    (the applied revision; audited in `audit-2.md` §3, cross-checked here)
  - the 12 fix receipts under `reports/round-17/civ/`, hashed against the round-17
    validation pins (`reports/round-17/validation.json` `input_sha256`).
- **Method, stated before results.** Per transition row: (1) assert the patch's `from_`
  block byte-equals the filed round-16 row (my own comparison, not the patch's claim);
  (2) re-hash the corpus entry and compare against `disposition.sha256_after`, and
  compare `disposition.sha256_before` against the round-17 validation baseline entry;
  (3) check the receipt's existence, date line, command carriage, and pin equality;
  (4) re-run the decisive claims (replacement targets, previously-failing URLs, entry-side
  repair assertions) — see `audit-2.md` §1 for the live results; (5) apply the demotion
  rule below. Machine ledger: `reports/round-18/civ/auditor-ledger.json`.
- **NON-CANON.** Status/locator-class verification only. No freshness axis-move (pause
  respected — every live probe below re-verifies a receipt's reproducibility, not a
  source's current scholarship), no canon, rights, clearance, rank or promotion ruling.

## 1. Structural legs (all re-run by this seat, 2026-10-18)

| leg | command (abbreviated) | result |
|---|---|---|
| patch `from_` == filed round-16 rows (12 rows, all keys) | python3 comparison over both JSONs (`from_.evidence_path: null` read as "row has no key") | **12/12 equal** |
| round-16 map bytes == patch `target.sha256` | `sha256sum reports/round-16/civ-map.json` | `07cabb69…cb943` — **match** |
| before-chain: `disposition.sha256_before` == round-17 validation `baseline_sha256` | join of `reports/round-17/civ/map-patch.json` × `reports/round-17/validation.json` `claims.C.measurement.corpus_edits` | **12/12 equal** |
| after-chain: current corpus bytes == `disposition.sha256_after` | `sha256sum corpus/knowledge/civilizations/<file>` × 12 | **12/12 equal** |
| round-17 C evidence immutability | re-hash of 18 C-related round-17 files vs `validation.json` pins (16 × `reports/round-17/civ/*` + `claims.json` + `targets.json`) | **18/18 match** |
| counting command | `ls corpus/knowledge/civilizations/*.md | wc -l` → **94** | reproduces |

The before→after chain therefore closes against **two independent filed sources** (the
patch's own digests and the round-17 validator's baseline/current digests) and the
current disk bytes.

## 2. Demotion rule (declared before verdicts)

A transition is **KEPT** iff all four legs hold: (a) current bytes == receipt-claimed
after-hash; (b) the fix receipt exists, carries a date and a runnable command, and its
bytes match the round-17 validation pin; (c) every decisive claim reproduces on an
independent re-run (decisive set = all replacement targets + all URLs the receipt
singles out as fixed/live/blocked/hard-fail + the specific in-repo assertion the fix
claims); (d) the applied row carries date+command. A failure of any leg would **demote**
the row to `stale-documented` with the failing leg named in the ledger. The auditor's
own probe failures that are explained by client-side classes (TLS chain caveats, bot
walls, single-vantage throttling) are classified, not blindly counted as demotions —
each such case is named in the ledger notes with the evidence that establishes the class.

## 3. Per-row verdicts (12/12 KEEP, 0 demotions)

Decisive reproduction values are the auditor's own re-runs; full per-check lists are in
`auditor-ledger.json` → `entries[].live_repro`.

| # | entry | group | proposed → applied | decisive reproduction (this seat) | verdict |
|---|---|---|---|---|---|
| 1 | inuit.md | fixed-type | stale-documented → stale-fixed | old locator 404 `95720 B`; new 200 `515139 B` + body sha256 `61388588…660d` (downloaded, MATCH) | **KEEP** |
| 2 | maya-classic.md | fixed-type | → stale-fixed | Sacbe 200 `178576 B` + sha256 `94b6bdaf…7e90` MATCH; in-entry `sacbeob` hits 0 → **8**; reciprocal couples pointer present | **KEEP** |
| 3 | mesoamerica-primary-sources.md | fixed-type | → stale-fixed | strict 000 ×3 (documented TLS classes); `-k` 200/`267502`, 200/`3499309`, 404/`146` — all exact; replacements 200/`19081`, 200/`130398`; strict control 200/`3162177` | **KEEP** |
| 4 | mongol.md | fixed-type | → stale-fixed | rubruck 200 `289660 B`; full entry 10/10 live | **KEEP** |
| 5 | muisca.md | fixed-type | → stale-fixed | 4× http 200 with exact `25827/33028/30692/32263`; nyia body sha16 `68342c14f9cc6479` MATCH + anchor `Ms. 2923. fol. 31v`; https negative 000 reproduces | **KEEP** |
| 6 | persia-sasanian.md | never-swept | → stale-fixed | SR14 replacement 200 `948943`; avesta fallback 200 `127638`; jstor DOI → stable URL 200; ucpress/uci exact; avesta 000 TLS expired reproduces; fallback in entry (line 14) | **KEEP** |
| 7 | polynesia-navigation.md | never-swept | → stale-fixed | 9/9 new targets 200; old pollex/wehe 301 chains → 200 (`31663`/`117921`); sweep 24×200 + 2×403 = receipt tally | **KEEP** |
| 8 | rapa-nui.md | never-swept | → stale-fixed | 8×200 exact (82124/427128/37175/373137); archive.org live ±2 B; metmuseum 429 reproduces | **KEEP** |
| 9 | rome.md | never-swept | → **current** | OCRE paren URL 200 (compressed `11046` exact; body sha16 `dfa92e87f8ad338f` MATCH); tacitus `17659`/`8f605172cdba5905`; suetonius `326426`/`9344cf5845ccb962`; cambridge asset `731447`/`6c450b438b4ed57f`; DOI 429 | **KEEP** |
| 10 | ryukyu.md | never-swept | → stale-fixed | MDPI 403 (`398 B`, byte-identical to C01); 11×200 incl. exact `183135`/`1679959`; sweep 11/1 = claim | **KEEP** |
| 11 | scythian-saka.md | never-swept | → stale-fixed | Leiden 301 target 200 `8911`; samples exact `92359/498050/76005`; sweep 11/1 = claim | **KEEP** |
| 12 | siam-thai.md | never-swept | → stale-fixed | both 301 targets 200 `118615`/`1657019` exact; excerpt `199008`; unesco 200 `155463` (claim `155457`, +6 B dynamic); loc.gov 403 reproduces | **KEEP** |

No transition lacked live evidence: the demotion list is **empty**
(`auditor-ledger.json` → `demotions: []`, `demotion_count: 0`).

## 4. Cross-corroboration

- **C01/C02 (`reports/round-18/civ/patch-apply.md`) r18_recheck** vs this seat: byte-for-byte
  agreement on every decisive locator, including inuit old locator 404 `95720`, rome OCRE
  raw `80524`, persia Wayback `127638` (their note: "byte count differs by 5-8 B from the
  receipt's 127643 / the verifier's 127635 (wayback re-renders)"), ryukyu MDPI `403/398`,
  muisca 4 exact sizes, siam `118615/1657019`.
- **R17-V01/V02** (filed, pinned): all 12 rows VERIFIED, with only non-dispositional
  findings (F-V01-1 CDX wording; F-V02-1 `--compressed` byte column; F-V02-2 dynamic-page
  hash variance), each of which this audit reproduced where applicable (F-18AUD-3/F-18AUD-4).
- **R17-V03/V04** (patch builders, pinned): patch target sha, `from_` equality assertion,
  and limits text independently reproduced by this seat.

## 5. Findings (full text and evidence in `auditor-ledger.json`)

- **F-18AUD-1** — label policy (`current` vs `stale-fixed`): resolved by the revision —
  patch labels applied verbatim **and** `transition.terminal_status=current` carried per
  row, normalization documented as an option. Consistent under both readings.
- **F-18AUD-2** — paren-URL extraction artifact: a naive `https?://` regex truncates the
  rome OCRE id at the first `)` and yields a false 404; balanced-paren extraction is 200
  with the exact body hash. My own initial sweep hit it and was corrected before
  classification (same class as V34-1/V02-2).
- **F-18AUD-3** — dynamic-size variance (±bytes) on 5 URL/page instances (archive.org,
  Wayback, unesco, metmuseum wall, nature) — all live; static decisive targets byte-exact.
- **F-18AUD-4** — rome receipt byte column is `--compressed` wire size (11046/17659/5419
  reproduce exactly only with `--compressed`); confirms F-V02-1/F-V34-2.
- **F-18AUD-5** — `openn.library.upenn.edu/…/mscoll700_item221.html` 000 on 5 attempts
  (2026-10-18): outside every transition's decisive set; carried as a future-sweep item.
- **F-18AUD-6** — "the 5 attempt-documented rows" has two readings (round-17 validator's
  `attempted` set vs the patch's 5 fixed-type rows); all 12 rows carry live re-checks, so
  both readings are satisfied.
- **F-18AUD-7** — numismatics.org throttling after repeat probes (3×200 incl. byte-exact
  body, then 1 timeout) — host-side, not rot.
- **F-18AUD-8** — evidence immutability: 18/18 C-related round-17 files match their pins;
  2 non-C files (`d4/typed-run.md`, `report-draft.md`) differ from their pins but are
  worktree-clean — the divergence predates round 18.
- **F-18AUD-9** — two transitioned rows (`maya-classic`, `mesoamerica-primary-sources`)
  carry a `command` string with no executable token; the current runner's carrier rule
  (`command` + `verified_r18` + `transition.r18_recheck.command`) passes both, and **claim
  C reports zero failures** on the current runner (see `audit-2.md` §4). Optional hardening
  only; no action required for C as filed.

## 6. Limits

NON-CANON (see header). Point-in-time (single-day, 2026-10-18); 403/429/000 classes are
read per the M04 convention and named per case; probes come from one network vantage; map
scribe and audit are separate seats, so agreement is corroboration, not independent
laboratory reproduction. The round-18 validator was still being written during this
audit; both `--check` runs (intermediate and current runner) are recorded in
`audit-2.md` §4 — C is green on the current runner; the overall rc=1 at check time comes
from claims D and O, whose work was still in flight.

Reproduction entry point: `python3 .scratch/r18c09/build-ledger.py` (re-derives every
leg above and rewrites `reports/round-18/civ/auditor-ledger.json` from the filed inputs;
scratch JSONs `probe-run1.json`, `sweep-all.json` carry the raw probe records).
