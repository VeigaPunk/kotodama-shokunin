# Round-18 civ-map revision — README + delta vs the round-16 map

- Seat: **R18-C07/C08** (scribe, C-map lane; round 18 — operator loop 2 of 3, build 2
  of 4). Date: 2026-10-18. Lane: `kotodama-shokunin`; declare revision
  `c66ac3c951b346a2a56f9386e3324b4f5fe33902`; baseline
  `3dd3754207032cb81f5fb3e202fe85cf79211339` (round-17 filed).
- Writes: this file, `reports/round-18/civ/delta-vs-round16.json` and
  `reports/round-18/civ/lessons-entry.md`. No commit, no push; no filed round-8..17
  byte touched (every transition is a new row in a new file).
- **NON-CANON.** Coverage/status receipts only: no canon, lore acceptance, rights,
  clearance or freshness-axis verdict is made or implied here. The freshness
  axis-move pause stands (`LOG.md:3028`); the two round-11 ratios stay separate.

## 1. Object and identity (read 2026-10-18, ~10:31Z)

| artifact | sha256 | notes |
|---|---|---|
| `reports/round-18/civ-map-r18.json` | `5fb4dd1cb948abbbbdb7b3182e5ba47cb15057da3519bd8bc63ad022ad8bf796` | the revision (read-time pin; the builder's deliverable) |
| `reports/round-16/civ-map.json` | `07cabb69b4a41c51b74767212a07ba4ffae3c09ef8c2571abd954b37342cb943` | superseded base — byte-unchanged (also the patch's declared `target.sha256`) |
| `reports/round-17/civ/map-patch.json` | `79ceafabac9fd84d6bec5cb701e3d1791b075e5e1300d7164126e40f9876e77e` | the 12-row replacement proposal applied |
| `reports/round-18/civ/patch-apply.md` | builder's receipt | identity chain, apply preconditions, per-row table, probes (R18-C01/C02) |

Revision header facts (`reports/round-18/civ-map-r18.json`): `round 18`,
`revision_of reports/round-16/civ-map.json`, `supersedes.unchanged: true`,
`applied_patch.rows: 12` with `from_rows_asserted_equal_to_round16_map` naming all 12,
`built_by CIV R18-C01/C02`, `date_utc 2026-10-18T10:26:15Z`,
`git_head_at_build c66ac3c…`, `count: 94`, `complete: true`, `unreceipted: []`,
`status_counts {current: 83, stale-fixed: 11, stale-documented: 0}`,
`terminal_status_counts {current: 94, stale-documented: 0}`,
`transitions_applied: 12`, `rows_carried_verbatim: 82`.

## 2. Delta vs the round-16 map

94 rows in both maps; **12 changed, 82 byte-identical** (row objects equal, not
merely status-equal). Status movement: `stale-documented 12 → 0`,
`current 82 → 83`, `stale-fixed 0 → 11`. Row order is the round-16 order.

| # | file (round-16 idx) | from → to status | group | fix receipt | keys added to the row |
|---|---|---|---|---|---|
| 1 | `inuit.md` (44) | stale-documented → stale-fixed | fixed-type | `reports/round-17/civ/inuit.md` | evidence_path, attempt_row, reason_round16, transition, verified_r18 |
| 2 | `maya-classic.md` (61) | stale-documented → stale-fixed | fixed-type | `reports/round-17/civ/maya-classic.md` | ″ |
| 3 | `mesoamerica-primary-sources.md` (62) | stale-documented → stale-fixed | fixed-type | `reports/round-17/civ/mesoamerica.md` | ″ |
| 4 | `mongol.md` (67) | stale-documented → stale-fixed | fixed-type | `reports/round-17/civ/mongol.md` | ″ |
| 5 | `muisca.md` (68) | stale-documented → stale-fixed | fixed-type | `reports/round-17/civ/muisca.md` | ″ |
| 6 | `persia-sasanian.md` (77) | stale-documented → stale-fixed | never-swept | `reports/round-17/civ/persia-sasanian.md` | ″ |
| 7 | `polynesia-navigation.md` (78) | stale-documented → stale-fixed | never-swept | `reports/round-17/civ/polynesia-navigation.md` | ″ |
| 8 | `rapa-nui.md` (79) | stale-documented → stale-fixed | never-swept | `reports/round-17/civ/rapa-nui.md` | ″ |
| 9 | `rome.md` (80) | stale-documented → **current** | never-swept | `reports/round-17/civ/sed77.md` | ″ |
| 10 | `ryukyu.md` (81) | stale-documented → stale-fixed | never-swept | `reports/round-17/civ/sed78.md` | ″ |
| 11 | `scythian-saka.md` (82) | stale-documented → stale-fixed | never-swept | `reports/round-17/civ/sed79.md` | ″ |
| 12 | `siam-thai.md` (83) | stale-documented → stale-fixed | never-swept | `reports/round-17/civ/sed80.md` | ″ |

Each transitioned row also carries the original round-16 `reason` as `reason_round16`
(the round-8/9/16 trail stays readable in-map) and a dated `verified_r18` command
string; the full per-row transition ledger (`date`, `command`, `fix_receipt`
+ digest, `entry_edit`, `entry_sha256_before/after`, `group`, `r18_recheck`) lives in
the row's `transition` object and is tabulated in `reports/round-18/civ/patch-apply.md`
§3. For rows 2 and 3 the patch's `command` text names no shell token (it names the
repair class and points at the receipt); the dated command rides in `verified_r18`
instead — recorded, not patched over (patch-apply §3).

Machine-readable table: `reports/round-18/civ/delta-vs-round16.json` (seat-composed;
its `delta` block is the row-level computation below, its `meta` block pins the three
input digests at read time).

## 3. Independent re-derivation (this seat, read-only, 2026-10-18)

Run from the lane root (`TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):

- **Patch `from_` assertions 12/12 pass** against the filed round-16 rows; the check
  treats `from_.evidence_path: null` as "the round-16 row has no `evidence_path` key"
  (naive dict equality fails on this encoding — see `lessons-entry.md`, item 1).
- **Row set equality**: revision row set == round-16 row set == corpus partition
  (94 unique names; no additions, no drops).
- **Delta**: exactly the 12 patch rows changed; the other 82 rows byte-equal.
- **Pin checks**: all 20 `evidence_pins` (8 round-16 shard files + 12 round-17 fix
  receipts) hash to their declared digests; all 12 `transition.entry_sha256_after`
  values equal today's `corpus/knowledge/civilizations/<file>` digests; all 12
  `fix_receipt_sha256` values equal today's receipt digests. Zero drift.
- **Append-only**: `reports/round-16/civ-map.json` still hashes `07cabb69…`;
  `git status --porcelain` over rounds 8–17 shows no modified filed byte (untracked
  round-18 files only).

## 4. Re-verification of the attempt-documented five (and the seven)

- **The five attempt-documented rows** are the round-16 fixed-type group:
  `inuit`, `maya-classic`, `mesoamerica-primary-sources`, `mongol`, `muisca`
  (rows with `attempt_row: true`). The revision re-probed each on 2026-10-18
  (window 10:21–10:26Z, `curl -w '%{http_code} %{size_download}'`, UA
  `kotodama-metadata-audit/1.0`); per-row results and raw codes are in
  `transition.r18_recheck` and tabulated in `patch-apply.md` §4 — inuit's
  replacement PDF 200/515139 B whose body digest equals the patch's recorded digest
  byte-for-byte, its replaced old locator 404 (still dead); maya-classic's carried
  source 200 with `grep -c sacbeob` → 8 in-entry (round-16 repro was 0);
  mesoamerica's replacement 200 and the retained caveat URL 000 strict / 200 with
  `-k`; mongol 200/289660 B (the round-8 hard-fail does not reproduce); muisca
  ×4 HTTP 200 on the http-only lexical host.
- **The seven never-swept rows** were sampled one locator each in the same window
  (`patch-apply.md` §5); the only deltas are two recorded byte-level notes (Wayback
  render variance ±5–8 B on persia's fallback; rome's receipt column is the
  compressed wire size) and the re-observed bot walls (rapa-nui 429, ryukyu 403).
- **Naming disambiguation (recorded so cross-checks do not collide):** the round-17
  runner's stricter class `attempted` (7 fixed / 5 attempted, receipt 09:30:54Z,
  runner `3fece609…`) names a **different five** — `mongol`, `muisca`, `rapa-nui`,
  `rome`, `ryukyu` — the rows where no new external locator landed. The claim's
  "5 attempt-documented rows" and the revision's `attempt_row: true` follow the
  round-16 fix-type group; the two readings intersect at `{mongol, muisca}`.
  Because every one of the 12 transitioned rows carries its own `r18_recheck` probes,
  both readings' populations are re-probed; a future receipt should still name rows
  by filename, not by count.
- **Filed verification receipts (landed 10:34–10:36Z, after an earlier sweep at
  10:33Z found only `patch-apply.md`):** `reports/round-18/civ/verify-1.md` (C03:
  `inuit`, `maya-classic`, `mesoamerica-primary-sources`), `verify-2.md` (C04:
  `mongol`, `muisca` + the 5-attempt documentation check + the counting-command
  reproduction), `verify-3.md` (C05: `persia-sasanian`, `polynesia-navigation`,
  `rapa-nui`, `rome`), `verify-4.md` (C06: `ryukyu`, `scythian-saka`, `siam-thai` +
  the 12-row roll-up); each verdict **VERIFIED** with informational findings
  (F-C03-1 `openn.library.upenn.edu` 000 ×4 — a new, unlisted debt; F-C05-1 Wayback
  replay byte variance; F-C06-1 MDPI challenge page served as 200; rome's
  compressed-bytes column). The roll-up confirms 12/12 transitions match the patch
  `to` blocks and 82/82 carried rows byte-equal the round-16 map (`verify-4.md` §4).
- **Adversarial audit:** `reports/round-18/civ/audit-1.md` (C09) +
  `auditor-ledger.json` (generated 10:35:07Z) — **12 KEEP / 0 demotions**; 18/18
  round-17 evidence pins match; `revision_audit` re-derives sha `5fb4dd1c…`,
  `transitions_applied 12`, `rows_carried_verbatim 82`, status counts as in §2; its
  F-18AUD-6 independently records the two readings of "the 5 attempt-documented rows"
  (matching the disambiguation above). Seat 2 (`audit-2.md`, C10, landed ~10:41Z)
  re-ran the evidence on the wire — a decisive re-probe set plus a **complete 193-URL
  re-sweep of all 12 transitioned entries** — and audited the revision file: **0
  demoted**, 12/12 `fix_receipt_sha256` pins match live bytes, revision sha
  `5fb4dd1c…` stable, every reproduced value equal to §2's transitions.

## 5. Counting command — reproduces 94

- `ls corpus/knowledge/civilizations/*.md | wc -l` → **94** (2026-10-18); unchanged
  from the round-16 map's `counting_command`, and the row set stays the corpus
  partition (§3).
- The round's assigned counting command is `python3 reports/round-18/run-validation.py`;
  its receipt (`reports/round-18/validation.json`) was **not written** at this seat's
  close — negative sweep `test -f reports/round-18/validation.json` → absent
  (2026-10-18T10:32Z) — so no claim is made here about the runner's verdict; that
  receipt is the runner owner's to write and the parent's to read.
- The builder re-ran the round-16 validator's own civ-map checks against the revision
  (rebinding only `ROUND_DIR`/`CIV_MAP`/`COMMAND`): `passed: True`, status histogram
  `{current: 83, stale-fixed: 11, stale-documented: 0}` (`patch-apply.md` §7).

## 6. Label policy (recorded, not normalized)

The patch's `label_policy_note` files 11 `stale-fixed` + 1 `current` and delegates the
normalization question. The revision applies the patch labels **verbatim** and carries
the terminal reading explicitly per row (`transition.terminal_status: "current"`,
`terminal_status_counts {current: 94, stale-documented: 0}`) — rationale and both
readings in `patch-apply.md` §6. Claim C's counts hold under either label
(`stale-documented` 12 → 0), which is the number the claim moves.

## 7. Check (re-runnable)

```sh
# identity + append-only
sha256sum reports/round-16/civ-map.json      # 07cabb69…
sha256sum reports/round-17/civ/map-patch.json # 79ceafab…
sha256sum reports/round-18/civ-map-r18.json   # read-time pin, see §1

# delta + from_ assertions (expected: 94 rows; 12 changed; from_ OK 12)
python3 - <<'PY'
import json
r16={e['file']:e for e in json.load(open('reports/round-16/civ-map.json'))['entries']}
rev={e['file']:e for e in json.load(open('reports/round-18/civ-map-r18.json'))['entries']}
patch={r['file']:r for r in json.load(open('reports/round-17/civ/map-patch.json'))['rows']}
assert set(rev)==set(r16), 'row set differs'
changed=[f for f in r16 if r16[f]!=rev[f]]
print(len(rev), 'rows;', len(changed), 'changed;', sorted(changed))
for f,r in patch.items():
    row=r16[f]; frm=dict(r['from_'])
    if frm.get('evidence_path','x') is None and 'evidence_path' not in row:
        frm.pop('evidence_path')   # null encodes key-absence
    assert all(row.get(k)==v for k,v in frm.items()), f
print('from_ assertions: OK (12)')
PY
```

## 8. Append-only provenance

The revision is a **new file**; the round-16 map and all round-17 receipts are read-only
inputs. `supersedes.unchanged: true` is asserted in the revision and re-verified in §3.
The 12 row replacements are new rows in a new revision — never in-place edits of filed
bytes (round-16 map still `07cabb69…`; round-17 receipts still at their filed digests,
checked as `evidence_pins`). The 82 carried rows keep their round-16 receipts verbatim;
their shard pins still match (`patch-apply.md` §9).

## 9. Limits and boundary notes

- **Moving bytes at read time.** The revision was still being enriched by its builder
  while this seat read it: observed sha256 `3020401b…` (10:26:15Z build) → `fabcd3dd…`
  → `5fb4dd1c…` (the §1/§3/§7 pin) inside ~5 minutes, as row fields
  (`verified_r18`, `transition.r18_recheck`, `attempt_row`) were added. All pins in
  this file are **read-time** pins of the builder's deliverable; a later revision of
  the map supersedes them and needs a new dated read (round-15 lesson).
- Point-in-time probes: all re-verification ran 2026-10-18 in a 64-worker wave; a
  single-day probe cannot rule out intermittent failure. Bot walls (403/429) and the
  incomplete-TLS chain were re-observed, not worked around.
- No freshness axis-move, no source-content re-review; the entry bytes were not
  re-read in full. Coverage receipts only.
- The round verdict (claims O/D/C and the runner's receipt) belongs to the runner
  owner and the parent; this README documents the C revision, it admits nothing.

Companion files: `reports/round-18/civ/patch-apply.md` (builder receipt, R18-C01/C02),
`reports/round-18/civ/delta-vs-round16.json` (machine delta, R18-C07),
`reports/round-18/civ/lessons-entry.md` (R18-C08).
