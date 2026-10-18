# R17-C02 — fixer: muisca.md 4 hard-fail `muysca.cubun.org` locators (claim C)

- seat: **R17-C02** (fixer, claim C, round 17 — operator regimen loop 2 of 3,
  build 1 of 4; 64 workers on opencode-go/deepseek-v4.1-flash), 2026-10-18
  local (-03:00); access window 09:10–09:25Z, last stamp `2026-10-18T09:20:19Z`.
- assignment (verbatim): "C R17-C02 (muisca fixer): same protocol for the 4
  hard-fail muysca.cubun.org URLs in muisca.md; reports/round-17/civ/muisca.md."
- write scope: **this file** and the `muisca.md` entry's `- verified-at:` /
  `[DG]` desk-row repair (§5) — the assignment names the entry and the round-16
  reason trail is carried in the edited text. No other corpus byte written; no
  filed round-8–16 byte written or edited; no git operation; scratch under
  `.scratch/` only (`TMPDIR=$PWD/.scratch` set before every scratch-writing
  command). All artifacts NON-CANON; no real-world rights/clearance ruling.
- baseline: `reports/round-17/claims.json` declares baseline
  `f30b6f8188937632bbedd0e7b29aeefff6f8b07b`; HEAD at start and close `9b49a4a`
  ("round-17: declare loop-2 build-1 claims D/C/O"). The wave is live and the
  civ worktree is shared, so the pre-edit bytes are pinned **by hash, not by
  clean status**: pre-edit sha256 `b1f013ac…` equals the hash recorded in
  `reports/round-16/civ-map.json` / `reports/round-16/civ/060-071.md:95`, and
  `git status --porcelain -- corpus/` at 09:22Z already listed concurrent
  seats' in-flight entry edits (`inuit.md`, `maya-classic.md`,
  `mesoamerica-primary-sources.md`, `mongol.md`, `rapa-nui.md`,
  `siam-thai.md`) — none of those is this seat's.

## 0. Object under fix, stamped

| object | sha256 | note |
|---|---|---|
| `corpus/knowledge/civilizations/muisca.md` (pre-edit, 2026-10-18T09:18Z) | `b1f013acb4daf9be3e06f5275a759a5ebf02c83ffdd39fd964dc56c903899468` | 29 556 bytes; hash **equals** the round-16 map's entry-68 row (`reports/round-16/civ-map.json`) and the round-16 shard row (`reports/round-16/civ/060-071.md:95`) — no drift since round 16 |
| last touch | `e1694ba` 2026-10-17 ("round-8: admit F/O/D…") | `git log -1 --format='%h %ad %s' --date=short -- corpus/knowledge/civilizations/muisca.md` |

Post-edit hash: `417b7086b5b3e8270b8509e17223c4bc966bd60d7d82cc444bf5a979b4237064` (re-measured in §5; the delivered file's hash is
whatever the tree holds after the parent integrates — this seat does not
commit).

## 1. Reason trail carried (round 16, reproduced)

- Round-16 map entry 68 (`reports/round-16/civ-map.json`): status
  `stale-documented`; reason verbatim: *"4 hard-fail 000 URLs on main lexical
  host muysca.cubun.org (r16 C06 in-repo verification)"*; evidence
  `reports/round-16/civ/060-071.md`.
- Round-16 shard (`reports/round-16/civ/060-071.md:95`): debt verbatim — *"4
  hard-fail (000) URLs from M §3: `muysca.cubun.org` `/chunso` `/chyquy`
  `/nyia` `/psihipqua` — M §7 names this dictionary as the entry's main lexical
  host; no re-attempt rounds 9–15. Heaviest debt in the shard"*.
- Origin sweep (`reports/round-8/metadata/m04-civ-58-76.md`):
  - `:87–90` — the four `000` rows, verbatim:
    ```
    000  muisca.md  http://muysca.cubun.org/chunso
    000  muisca.md  http://muysca.cubun.org/chyquy
    000  muisca.md  http://muysca.cubun.org/nyia
    000  muisca.md  http://muysca.cubun.org/psihipqua
    ```
  - `:68` — entry's 8-URL sweep tally `2 | 6` (2 live, 6 non-2xx/failed).
  - `:224` — routed action: *"re-attempt with alternate access routes and
    record a documented access failure per URL if still unreachable (muisca's
    `muysca.cubun.org` dictionary is 4 of the 9 and is the entry's main lexical
    host)"*.
- Round-16 auditor (`reports/round-16/civ/map-audit.md:75`) independently
  re-derived the debt as 4 of the 9 × 000 hard failures.
- **No-re-attempt sweep reproduced** (negative claim needs its sweep):
  ```
  grep -rn "muysca.cubun\|rubruck\|florentinecodex.getty\|totonicapan_simonetta\|liblilly" \
    reports/round-9 reports/round-10 reports/round-11 reports/round-12 \
    reports/round-13 reports/round-14 reports/round-15
  → 0 matches (grep exit 1), 2026-10-18
  ```
  i.e. rounds 9–15 contain no re-attempt receipt for these URLs; the only
  in-repo hits for `muysca.cubun` after round 8 are round-16 map/shard/audit
  restatements of the debt.

## 2. Re-attempt — the four URLs are live (three independent samples)

| sample | method | command shape | result (2026-10-18) |
|---|---|---|---|
| 1 | `curl` GET, follow redirects, own UA | `curl -sS -o FILE -w '%{http_code} %{size_download} %{time_total}' -L --max-time 25 URL` | **200 ×4** — `/nyia` 30 692 B / 9.7 s; `/chunso` 25 827 B / 8.7 s; `/chyquy` 33 028 B / 3.0 s; `/psihipqua` 32 263 B / 0.8 s |
| 2 | `curl -I` HEAD | `curl -sS -I -o /dev/null -w '%{http_code} %{http_version}' --max-time 25 URL` | **200 ×4**, HTTP/1.1 |
| 3 | `python3` `urllib.request` GET, distinct UA, fresh bytes | `urllib.request.urlopen(Request(url, headers=UA), timeout=30)` | **200 ×4**, byte counts identical to sample 1 (`nyia` 30 692 B `sha256 68342c14f9cc6479…`, `chunso` 25 827 B `12a05c944c6745a9…`, `chyquy` 33 028 B `1220ae0c56216328…`, `psihipqua` 32 263 B `a2568b599786ed9c…`); server header `Apache/2.4.52 (Ubuntu)` |
| 4 | stamped re-confirmation | `date -u` + the §3 anchor loop | `STAMP 2026-10-18T09:20:19Z` → `200` ×4 |

- **Scheme finding (negative, swept):** `https://muysca.cubun.org/{nyia,chunso,chyquy,psihipqua}`
  → `000` on **all four** (25 s timeout each, 2026-10-18). The host is
  **http-only**. The round-8 `000` rows are therefore consistent with a
  scheme/host access outcome on that sweep date, not with a dead resource; the
  `000`-as-locator-death reading is *not* supported by today's re-attempt.
  Consequence for the entry: **the locator strings stay unchanged** — a
  "modernize to https" edit would break them.
- Timing note: `%{time_total}` is 0.8–9.7 s GET / 2.3–7.2 s HEAD — the host is
  slow but responsive; sample 4's run took 16.9 s wall for 8 requests.

## 3. Content verification — the live pages carry the entry's own anchors

The entry cites `[DG]` with manuscript/folio anchors (`muisca.md:88–95`,
`:110–118`). Those anchors were re-checked **on the live pages** (not from a
cached copy), 2026-10-18:

| URL | anchor on live page (verbatim) | entry's claim it supports | match |
|---|---|---|---|
| `/nyia` | `Ms. 2923. fol. 31v`; `Ms. 158. Voc. fol. 59r` | "Gold: Ms. II/2923, fol. 31v; money: Ms. 158 vocabulary, fol. 59r" | yes (siglum nuance below) |
| `/chunso` | `Ms. 158. Voc. fol. 124r`; `Ms. 158. Voc. fol. 80v` | "'ídolo': Ms. 158 vocabulary, fol. 124r; a gold-to-image example occurs at fol. 80v" | yes |
| `/chyquy` | `Ms. 158. Voc. fol. 112r`; `Ms. 158. Con. fol. 139r`; `Ms. 158. Con. fol. 136v` | "'Sacerdote': Ms. 158 vocabulary, fol. 112r"; "[DG] notes application to both Indigenous and Catholic priests" | yes — page reads *"Así se denominaban tanto a los sacerdotes de las religiones indígenas como a los sacerdotes católicos"* |
| `/psihipqua` | `Ms. 158. Voc. fol. 31v`; `104r`; `113v`; `Ms. 158. Con. fol. 131r` | "Lord/chief and related colonial glosses" | yes — page head gloss "Señor, cacique, príncipe, gobernador, monarca" |

Reproducible anchor command (2026-10-18):

```
for u in nyia chunso chyquy psihipqua; do
  printf "[%s] " "$u"
  curl -sL --max-time 25 "http://muysca.cubun.org/$u" \
    | grep -oE "Ms\. (2923|158)[^<]{0,30}" | sort -u | tr '\n' ';'
  echo
done
→ [nyia] Ms. 158. Voc. fol. 59r;Ms. 158. Voc. fol. 76r;Ms. 158. Voc. fol. 77r;Ms. 2923. fol. 31v;
  [chunso] Ms. 158. Voc. fol. 124r;Ms. 158. Voc. fol. 80v;
  [chyquy] Ms. 158. Con. fol. 136v;Ms. 158. Con. fol. 139r;Ms. 158. Voc. fol. 112r;
  [psihipqua] Ms. 158. Con. fol. 131r;Ms. 158. Voc. fol. 104r;Ms. 158. Voc. fol. 113v;Ms. 158. Voc. fol. 31v;
```

**Reported, not absorbed (observation, R17-C02-OBS-1):** the entry writes
`Ms. II/2923` (`muisca.md:88`) where the live page writes `Ms. 2923.` — a
siglum/rendering difference, not a locator failure. Whether the entry's `II/`
prefix follows this lane's own citation convention for that manuscript could
not be settled from in-repo evidence (grep for `II/2923` across `corpus/` and
`reports/` → only this entry, 2026-10-18), so the folio siglum was left
untouched; the verifier/owner may rule.

## 4. Disposition — all four `stale-fixed` (debt closed, locator unchanged)

- Round-16 status: `stale-documented` ("4 hard-fail 000 URLs…").
- Round-17 status: **`stale-fixed`** for all four rows — re-attempted,
  HTTP 200, content-verified against the entry's own manuscript anchors. No
  replacement URL was needed, so the claim-C branch "locator replaced with a
  live, content-verified source … or kept stale-documented with the reason
  updated to name the replacement attempt" is satisfied on its first branch in
  substance: the source at the cited locator is live and content-verified; the
  attempt history is recorded in the entry (§5) and here.
- Residual for this entry's URL apparatus (adjacent probe, **not** this
  seat's claim, **not absorbed**): of the other 4 cited links, `arxiv.org/html/0812.0574v3`
  → 200 and `repository.cam.ac.uk/…/download` → 200 today, while
  `catalog.hathitrust.org/Record/101231772` → 403 and
  `doi.org/10.1017/S0003598X00047918` → 429 — the same bot-wall/rate-limit
  classes m04 §6 classified as access outcomes, not link rot. Entry apparatus
  therefore reads **6 live / 2 access-limited** on 2026-10-18 vs round-8's
  "2 live / 6 non-2xx or failed". These two were **not** written into the entry
  beyond the verified-at note's one-clause mention (§5).

## 5. Entry edits (old → new)

Edit 1 — `- verified-at:` (`muisca.md:6`), historical text kept, repair note
appended:

- old (tail): `…all 8 cited links status-swept on 2026-10-17 (2 live, 6 non-2xx or failed); no passage, catalogue, or dated-object re-inspection in this pass`
- new (tail): `…no passage, catalogue, or dated-object re-inspection in that pass. 2026-10-18 round-17 locator repair (claim C; evidence reports/round-17/civ/muisca.md): the four [DG] muysca.cubun.org entry URLs, hard-fail 000 in the round-8 sweep (reports/round-8/metadata/m04-civ-58-76.md:87-90; carried as debt in reports/round-16/civ-map.json entry 68 and reports/round-16/civ/060-071.md:95), were re-attempted and are live — all four HTTP 200 on 2026-10-18 across three independent samples, with the entry's manuscript anchors re-checked on the live pages; the locator strings are unchanged (the host is http-only — https times out 000 on all four — so do not "upgrade" the scheme); the remaining 4 cited links keep their round-8 status classes apart from an adjacent probe (arXiv and Cambridge repository 200; HathiTrust 403 and the Antiquity DOI 429 remain access limits, not hard fails).`

Edit 2 — `[DG]` source-desk row (`muisca.md:31`), note appended:

- old (tail): `…Dynamic scholarly transcription resource; use the manuscript/folio anchors below, not an unattributed modern word list.`
- new (tail): `…Dynamic scholarly transcription resource; use the manuscript/folio anchors below, not an unattributed modern word list. Re-probed 2026-10-18 (round 17, claim C): all four entry URLs HTTP 200 and the folio anchors cited below re-checked on the live pages; the host serves http only (https fails), so keep the plain-http locators.`

No other line was touched. Post-edit hash of `muisca.md`:
`417b7086b5b3e8270b8509e17223c4bc966bd60d7d82cc444bf5a979b4237064` (command in §8).

## 6. Adjacent probe detail (2026-10-18, informational)

```
403  5492 B    https://catalog.hathitrust.org/Record/101231772
200  2105796 B https://arxiv.org/html/0812.0574v3
429  1302 B    https://doi.org/10.1017/S0003598X00047918
200  7762988 B https://www.repository.cam.ac.uk/bitstreams/f908fef3-39a1-43bf-8605-c2423881c0d3/download
```

## 7. Honesty limits

- **Not a freshness axis-move claim.** The freshness pause (LOG.md:3021-3029)
  bars *freshness* claims; this seat's checks establish **locator reachability
  and anchor presence on 2026-10-18**, not that the entry's scholarship is
  current in the world. No dated-object, passage, or catalogue re-inspection
  was performed, and none is claimed.
- The live re-attempt is the round-17 claim-C disposition work (coverage),
  which is what makes it admissible despite the pause; the entry text says
  "re-attempted", never "re-verified".
- `stale-fixed` here means the named debt row (4 × 000) no longer reproduces;
  it is not a verdict on the other 8-link sweep row or on the entry's content
  calibration.
- One observer, one network path, one date: 200/000 outcomes are
  point-in-time measurements (m04 §6's run-to-run variance lesson applies);
  the three-sample agreement above narrows but does not eliminate that limit.
- All artifacts here are NON-CANON; no canon, rank, rights, or clearance
  ruling is made or implied. Nothing outside this repo was written.

## 8. Machine-readable block (for the round-17 validator / map integration)

```json
{
  "shard": "R17-C02",
  "round": 17,
  "claim": "C",
  "entry": "corpus/knowledge/civilizations/muisca.md",
  "entry_sha256_pre_edit": "b1f013acb4daf9be3e06f5275a759a5ebf02c83ffdd39fd964dc56c903899468",
  "entry_sha256_post_edit": "417b7086b5b3e8270b8509e17223c4bc966bd60d7d82cc444bf5a979b4237064",
  "prior_status": "stale-documented",
  "prior_reason": "4 hard-fail 000 URLs on main lexical host muysca.cubun.org (r16 C06 in-repo verification)",
  "prior_evidence": ["reports/round-16/civ-map.json#entry-68", "reports/round-16/civ/060-071.md:95", "reports/round-8/metadata/m04-civ-58-76.md:87-90", "reports/round-8/metadata/m04-civ-58-76.md:224"],
  "new_status": "stale-fixed",
  "status": "stale-fixed",
  "new_sha256": "417b7086b5b3e8270b8509e17223c4bc966bd60d7d82cc444bf5a979b4237064",
  "reason_trail": ["reports/round-16/civ-map.json#entry-68", "reports/round-16/civ/060-071.md", "reports/round-16/civ/map-audit.md:75", "reports/round-8/metadata/m04-civ-58-76.md"],
  "evidence": ["reports/round-17/civ/muisca.md"],
  "urls": [
    {"url": "http://muysca.cubun.org/nyia", "old_status": "000", "new_status": 200, "samples": 3, "bytes": 30692, "body_sha256_prefix": "68342c14f9cc6479", "anchor_checked": ["Ms. 2923. fol. 31v", "Ms. 158. Voc. fol. 59r"]},
    {"url": "http://muysca.cubun.org/chunso", "old_status": "000", "new_status": 200, "samples": 3, "bytes": 25827, "body_sha256_prefix": "12a05c944c6745a9", "anchor_checked": ["Ms. 158. Voc. fol. 124r", "Ms. 158. Voc. fol. 80v"]},
    {"url": "http://muysca.cubun.org/chyquy", "old_status": "000", "new_status": 200, "samples": 3, "bytes": 33028, "body_sha256_prefix": "1220ae0c56216328", "anchor_checked": ["Ms. 158. Voc. fol. 112r"]},
    {"url": "http://muysca.cubun.org/psihipqua", "old_status": "000", "new_status": 200, "samples": 3, "bytes": 32263, "body_sha256_prefix": "a2568b599786ed9c", "anchor_checked": ["Ms. 158. Voc. fol. 31v", "Ms. 158. Voc. fol. 104r", "Ms. 158. Voc. fol. 113v"]}
  ],
  "scheme_negative": {"https_all_four": "000 (25s timeout each)", "http_all_four": 200, "conclusion": "host is http-only; locator strings unchanged by design"},
  "locator_replaced": false,
  "entry_edits": ["muisca.md:6 verified-at append", "muisca.md:31 [DG] row append"],
  "adjacent_probe_not_absorbed": {"arxiv": 200, "cam_repository": 200, "hathitrust": 403, "antiquity_doi": 429},
  "observations": [{"id": "R17-C02-OBS-1", "text": "entry 'Ms. II/2923' vs live page 'Ms. 2923.' — siglum rendering difference, left untouched, owner may rule"}],
  "freshness_axis_move": false,
  "non_canon": true,
  "checked_at_utc": "2026-10-18T09:20:19Z"
}
```

## 9. Commands (all 2026-10-18, `TMPDIR=$PWD/.scratch`)

```
date -u +%Y-%m-%dT%H:%M:%SZ                                        # → 2026-10-18T09:18:12Z / 09:20:19Z
sha256sum corpus/knowledge/civilizations/muisca.md                 # → b1f013ac… (= round-16 map row 68)
wc -c corpus/knowledge/civilizations/muisca.md                     # → 29556
git log -1 --format='%h %ad %s' --date=short -- corpus/knowledge/civilizations/muisca.md   # → e1694ba
for u in nyia chunso chyquy psihipqua; do curl -sS -o .scratch/muysca-$u.html \
  -w "%{http_code} %{size_download} %{time_total}\n" -L --max-time 25 "http://muysca.cubun.org/$u"; done   # → 200 ×4
for u in nyia chunso chyquy psihipqua; do curl -sS -I -o /dev/null \
  -w "%{http_code} %{http_version}\n" --max-time 25 "http://muysca.cubun.org/$u"; done                     # → 200 ×4, 1.1
python3 - <<'EOF'  # sample 3: urllib, distinct UA, sha256 of bodies  → 200 ×4, byte-identical to sample 1
EOF
for u in nyia chunso chyquy psihipqua; do curl -sS -o /dev/null -w "%{http_code}\n" -L --max-time 25 \
  "https://muysca.cubun.org/$u"; done                                                                       # → 000 ×4 (https negative)
for u in nyia chunso chyquy psihipqua; do curl -sL --max-time 25 "http://muysca.cubun.org/$u" \
  | grep -oE "Ms\. (2923|158)[^<]{0,30}" | sort -u | tr '\n' ';'; echo; done                                # §3 anchors
grep -rn "muysca.cubun\|rubruck\|florentinecodex.getty\|totonicapan_simonetta\|liblilly" \
  reports/round-9 reports/round-10 reports/round-11 reports/round-12 reports/round-13 reports/round-14 reports/round-15   # → 0 matches
sha256sum corpus/knowledge/civilizations/muisca.md                 # → 417b7086b5b3e8270b8509e17223c4bc966bd60d7d82cc444bf5a979b4237064 (post-edit)
```

This file is a fixer receipt, not a promotion verdict: the round-17 verifier
and parent own acceptance.

## 10. Interaction with the round-16 validator (checked, not run in place)

- `python3 reports/round-16/run-validation.py` was attempted 2026-10-18 and
  **refused at startup** — the receipt guard blocked overwriting the committed
  `reports/round-16/validation.json`:
  `receipt_guard: refusing overwrite path=reports/round-16/validation.json committed_sha=9b49a4a0fca6ceeab917d401945358fdedeb7e11 [RECEIPT-GUARD-COMMITTED]`.
  No filed byte was written; the run was **not** forced with
  `REFRESH_RECEIPTS=1` (that would touch a filed round-16 artifact).
- Read-only audit of what that validator makes of this edit: its
  filed-preservation check covers `FILED = reports/round-8..15`
  (`run-validation.py:64, 240–281`) — corpus bytes are outside it; its civ-map
  pin check hashes the **evidence shard** (`reports/round-16/civ/*.md`), not
  the entry (`:475–479`); corpus entry bytes are recorded only as
  `evidence.inputs` (`:295`), never asserted against a pin. So no round-16
  failure condition is invalidated by this repair — but no green re-run was
  obtained by this seat, and none is implied.
- For the round-17 map/validator: `muisca.md` post-repair hash `417b7086…`
  (30 589 bytes) differs from the round-16 shard's recorded `b1f013ac…`
  (29 556 bytes). That drift is the intended outcome of claim C's entry edit; a
  round-17 map row for muisca should read `stale-fixed` with this file as its
  evidence.
